# MAFFT

- **Category:** phylogenetics
- **Papers in survey:** 346
- **Journals:** PNAS (208), Nature (106), Cell (20), Science (11), Lancet (1)
- **Years:** 2021 (39), 2022 (60), 2023 (63), 2024 (71), 2025 (83), 2026 (30)
- **Versions named:** 7.475 (15), 7.490 (14), 7.453 (14), 7.505 (10), 7.407 (8), 7.487 (7), 7.450 (7), 7.526 (6), 7.310 (6), 7.520 (5)
- **Pipeline stages it appears in:** alignment/mapping (325), read trimming (40), structure determination (17), dimensionality reduction/clustering (16), visualisation (12), registration (5), variant calling (5), machine learning (2), differential/statistical testing (1)

## Papers

### The emergence and ongoing convergent evolution of the SARS-CoV-2 N501Y lineages. (Cell 2021)

- DOI: 10.1016/j.cell.2021.09.003 | PMCID: PMC8421097 | PMID: 34537136
- Evidence: ...ompact/clades tn93-cluster Kosakovsky Pond et al., 2018 https://github.com/veg/tn93 raxml-ng Kozlov et al., 2019 https://github.com/amkozlov/raxml-ng MAFFT Katoh et al., 2002 https://mafft.cbrc.jp/alignment/software/ Other ObservableHQ notebook detailing N501Y lineage-specific selection results (other clades included as well) This paper https://observablehq.com/@spond/n501y-clades@3752 ObservableH...
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> visualisation [Python] -> stage not stated [Pangolin]

### Virus-encoded histone doublets are essential and form nucleosome-like structures. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.032 | PMCID: PMC8357426 | PMID: 34297924
- Evidence: Method details Histone sequence alignment and secondary structure prediction Predicted Marseilleviridae histone-like proteins were aligned with eukaryotic histone proteins with HHpred’s Multiple Alignment using Fast Fourier Transform (MAFFT) with a 1.53 gap open penalty.
- Full pipeline: alignment/mapping [MAFFT] -> quantification [R, RSEM, edgeR] -> normalisation [R, RSEM, edgeR] -> structure determination [PHENIX] -> stage not stated [NAMD, UCSF Chimera, VMD v1.9.3]

### A selective sweep in the Spike gene has driven SARS-CoV-2 human adaptation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.007 | PMCID: PMC8260498 | PMID: 34289344
- Evidence: ...cloning vector Sikorski and Hieter, 1989 pRS313 pRS313-T7-N This paper N/A Software and algorithms Minimap 2 Li, 2018 https://github.com/lh3/minimap2 MAFFT Katoh and Standley, 2013 https://mafft.cbrc.jp/alignment/software/ OmegaPlus Alachiotis et al., 2012 https://cme.h-its.org/exelixis/web/software/omegaplus/index.html RAiSD Alachiotis and Pavlidis, 2018 https://github.com/alachins/raisd Schrödin...
- Full pipeline: alignment/mapping [MAFFT, minimap2] -> stage not stated [Pangolin, PyMOL]

### Identification of novel bat coronaviruses sheds light on the evolutionary origins of SARS-CoV-2 and related viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.008 | PMCID: PMC8188299 | PMID: 34147139
- Version used: **7.450**
- Evidence: ...ie2 Kraken v2.0.9 Wood et al., 2019 https://ccb.jhu.edu/software/kraken/ Geneious v2021.0.1 The Biomatters development team https://www.geneious.com/ MAFFT v7.450 Nakamura et al., 2018 https://mafft.cbrc.jp/alignment/software/ Clustal Omega v1.2.2 Sievers et al., 2011 http://www.clustal.org/omega/ BLAST Camacho et al., 2009 https://blast.ncbi.nlm.nih.gov/Blast.cgi SAMtools v1.10 Li et al., 2009 ht...
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2, MAFFT v7.450] -> stage not stated [BLAST, Bowtie2 v2.4.1, PyMOL v2.4.0a, RAxML, SAMtools v1.10]

### A stony coral cell atlas illuminates the molecular and cellular basis of coral symbiosis, calcification, and immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.005 | PMCID: PMC8162421 | PMID: 33945788
- Evidence: We built multi-sequence alignments of each homology group with MAFFT ( Katoh and Standley, 2013 ) (using up to 10,000 rounds of iterative refinement and the E-INS-i algorithm; trimmed the alignments using ClipKIT ( Steenwyk et al., 2020 ) (retaining parsimony-informative and constant sites and removing sites with a gap threshold over 0.7).
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [Bowtie2, DIAMOND, IQ-TREE, MACS2, MAFFT, edgeR, eggNOG] -> dimensionality reduction/clustering [SAMtools] -> structure determination [IQ-TREE, MAFFT] -> stage not stated [HMMER, R]

### Transmission, infectivity, and neutralization of a spike L452R SARS-CoV-2 variant. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.025 | PMCID: PMC8057738 | PMID: 33991487
- Evidence: ...V-2-Spike-D614G + W152C This study N/A Software and algorithms BBTools suite, v38.87 Bushnell, 2021 , https://jgi.doe.gov/data-and-tools/bbtools/ N/A MAFFT aligner v7.388 Katoh and Standley, 2013 , https://mafft.cbrc.jp/alignment/software/ N/A Geneious v11.1.5 Kearse et al., 2012 , https://www.geneious.com N/A Nextstrain/Augur pipeline v3.0.0 https://github.com/nextstrain/augur N/A PANGOLIN v.2.3....
- Full pipeline: alignment/mapping [BLAST, MAFFT, Nextstrain] -> stage not stated [IQ-TREE v1.6, Python v3.7.9, R v4.0, SciPy]

### Early introductions and transmission of SARS-CoV-2 variant B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.061 | PMCID: PMC8018830 | PMID: 33891875
- Evidence: ...mmunity/treeannotator Rambaut et al., 2018 BEAST v1.10 http://beast.community Suchard et al., 2018 BWA https://github.com/lh3/bwa Li and Durbin, 2010 MAFFT https://mafft.cbrc.jp/alignment/software/ Katoh and Standley, 2013 iVar 1.2.1 https://github.com/andersen-lab/ivar Grubaugh et al., 2019 Samtools http://samtools.sourceforge.net/ Li et al., 2009 TrimGalore https://github.com/FelixKrueger/TrimGa...
- Full pipeline: alignment/mapping [BWA, MAFFT, SAMtools] -> normalisation [BEAST v1.10] -> differential/statistical testing [BEAST v1.10] -> structure determination [BEAST v1.10] -> stage not stated [Nextstrain, Pangolin, TreeTime v0.8.0, Trim Galore, ggplot2]

### Massive expansion of human gut bacteriophage diversity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.029 | PMCID: PMC7895897 | PMID: 33606979
- Version used: **7.453**
- Evidence: ...seemann/prokka BWA-MEM v0.7.16a-r1181 Li and Durbin, 2009 https://github.com/lh3/bwa Kraken2 Wood et al., 2019 https://github.com/DerrickWood/kraken2 MAFFT v7.453 Katoh et al., 2002 https://mafft.cbrc.jp/alignment/software/ Easyfig v2.2.5 Sullivan et al., 2011 https://mjsull.github.io/Easyfig/files.html Other ICEberg 2.0 Bi et al., 2012 https://db-mml.sjtu.edu.cn/ICEberg/ ImmeDB Jiang et al., 2019...
- Full pipeline: alignment/mapping [BWA v0.7.16a, Kraken2, MAFFT v7.453, SAMtools v1.5] -> machine learning [SPAdes v3.10.0] -> stage not stated [BLAST v2.6.0, HMMER v3.1b, Keras v2.2.4, Prokka v1.5, Python, TensorFlow v1.10.0]

### In vivo structural characterization of the SARS-CoV-2 RNA genome identifies host proteins vulnerable to repurposed drugs. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.008 | PMCID: PMC7871767 | PMID: 33636127
- Version used: **7.313**
- Evidence: Multiple sequence alignments of all collected viral sequences were constructed using MAFFT v.7.313 ( Nakamura et al., 2018 ).
- Full pipeline: read trimming [Bowtie2, SAMtools, Trimmomatic] -> alignment/mapping [MAFFT v7.313] -> differential/statistical testing [SciPy] -> simulation/modelling [UCSF Chimera] -> structure determination [UCSF Chimera] -> visualisation [RAxML v8.2.12] -> stage not stated [AutoDock Vina]

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Evidence: Insertion calls from all 3,202 samples that were positively genotyped with a PASS filter flag were then clustered by genomic location and aligned using MAFFT ( Katoh and Standley, 2013 ).
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### Emergence of immune escape at dominant SARS-CoV-2 killer T cell epitope. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.002 | PMCID: PMC9279490 | PMID: 35931021
- Evidence: ... development of phylogenetic workflows, NAR Genomics and Bioinformatics, Volume 3, Issue 3, September 2021, https://github.com/evolbioinfo/gotree N/A MAFFT Katoh et al., 2002 http://mafft.cbrc.jp/alignment/server/ MAFFT, RRID: SCR_011811 IQ-TREE Nguyen et al., 2015 . https://doi.org/10.1093/molbev/msu300 http://iqtree.org IQ-TREE, RRID: SCR_017254 MixCR v3.0.13 Bolotin et al., 2015 https://github....
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT] -> stage not stated [CCP4 v7.1, PyMOL v2.3.4, R v4.0, REFMAC v5.8, tidyverse]

### Short prokaryotic Argonaute systems trigger cell death upon detection of invading DNA. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.012 | PMCID: PMC9097488 | PMID: 35381200
- Evidence: ...e 49787 Plasmid DNA This study See Table S2 Software and algorithms HMMER https://www.hmmer.org v3.3.1 InterProScan ( Jones et al., 2014 ) v5.51-85.0 MAFFT ( Katoh and Standley, 2013 ) v7.475 trimAI ( Capella-Gutiérrez et al., 2009 ) v1.4 IQtree ( Minh et al., 2020 ) v2.0.4 ModelFinder ( Kalyaanamoorthy et al., 2017 ) N/A iTOL https://itol.embl.de ( Letunic and Bork, 2021 ) v6 Diamond blastp ( Buc...
- Full pipeline: quality control [FastQC, HISAT2, featureCounts] -> differential/statistical testing [BLAST, Cytoscape, FastQC, HISAT2] -> stage not stated [HMMER, InterProScan, MAFFT, R]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **7.475**
- Evidence: 84 http://www.iqtree.org/ MAFFT 7.475 Katoh and Standley 85 https://mafft.cbrc.jp/alignment/server/ HMMER 3.3.2 Mistry et al.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### Structure of the endosomal Commander complex linked to Ritscher-Schinzel syndrome. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.003 | PMCID: PMC10187114 | PMID: 37172566
- Evidence: ...3.3.1 110 https://cryosparc.com AlphaFold2 Multimer 54 , 55 https://github.com/deepmind/alphafold ColabFold 56 https://github.com/sokrypton/ColabFold MAFFT L-INS-i (v7.505) 111 https://mafft.cbrc.jp/alignment/software/ IQTree2.1.3 112 http://www.iqtree.org Consurf 113 https://consurf.tau.ac.il/consurf_index.php Other Superose6 Increase10/300 GL column Cytiva Cat# 29091596 HiLoad™ Superdex75 PG col...
- Full pipeline: alignment/mapping [ColabFold, MAFFT, PyMOL] -> normalisation [CCP4] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, HMMER v3.3.2, PHENIX, RELION, Topaz]

### Minimal and hybrid hydrogenases are active from archaea. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.032 | PMCID: PMC11216029 | PMID: 38866018
- Version used: **7.304**
- Evidence: 116 N/A MAFFT v7.304 Katoh and Standley 117 N/A METABOLIC Zhou et al.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [Nextflow] -> stage not stated [AlphaFold, BLAST, Clustal Omega v1.2.2, HMMER v3.2.1, IQ-TREE v1.6.12, MAFFT v7.304, R, StringTie v2.2.1]

### RAF-like protein kinases mediate a deeply conserved, rapid auxin response. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.021 | PMCID: PMC10783624 | PMID: 38128538
- Version used: **7.505**
- Evidence: 123 https://bioconductor.org/packages/release/bioc/html/DESeq2.html Other AuxPhos This paper Source code: https://github.com/WeijersLab/AuxPhos Webtool: https://weijerslab.shinyapps.io/AuxPhos MAFFT v7.505 Nakamura et al.
- Full pipeline: quality control [FastQC v0.11.9, HISAT2 v2.1.0] -> visualisation [ggplot2, tidyverse] -> stage not stated [AlphaFold, Cytoscape v3.10.1, DESeq2, ImageJ, MAFFT v7.505, OrthoFinder, featureCounts v2.0.0]

### Highly conserved Betacoronavirus sequences are broadly recognized by human T cells. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.015 | PMCID: PMC12392877 | PMID: 40774254
- Evidence: For each of these clusters a multiple sequence alignment was inferred using the Multiple Alignment using Fast Fourier Transform (MAFFT) software 58 with the most accurate options, which was then used to calculate a consensus sequence.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Version used: **7.407**
- Evidence: 104 https://ginolhac.github.io/mapDamage/ MAFFT v7.407 Katoh and Standley 105 https://mafft.cbrc.jp/alignment/software/ ModelTest-NG v0.1.7 Darriba et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### Mechanism of DNA capture by the MukBEF SMC complex and its inhibition by a viral DNA mimic. (Cell 2025)

- DOI: 10.1016/j.cell.2025.02.032 | PMCID: PMC7617805 | PMID: 40168993
- Evidence: 79 https://huygens.science.uva.nl/VolcaNoseR/ MMseqs2 Steinegger and Soding 80 https://github.com/soedinglab/MMseqs2 MAFFT Katoh et al.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [AlphaFold, ChimeraX, MAFFT, PHENIX, RELION]

### Therapeutic potential of allosteric HECT E3 ligase inhibition. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.001 | PMCID: PMC12087876 | PMID: 40179885
- Evidence: Redundant sequences with an identity higher than 90% were removed using mmseq2 and the obtained profiles were aligned with MAFFT.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [AlphaFold, PyMOL]

### Efficacy of ChAdOx1 nCoV-19 (AZD1222) vaccine against SARS-CoV-2 variant of concern 202012/01 (B.1.1.7): an exploratory analysis of a randomised controlled trial. (Lancet 2021)

- DOI: 10.1016/s0140-6736(21)00628-0 | PMCID: PMC8009612 | PMID: 33798499
- Version used: **7.402**
- Evidence: Consensus sequences were aligned using MAFFT version 7.402.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.402] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [Pangolin v2.1.7]

### Independent infections of porcine deltacoronavirus among Haitian children. (Nature 2021)

- DOI: 10.1038/s41586-021-04111-z | PMCID: PMC8636265 | PMID: 34789872
- Version used: **7.407**
- Evidence: The final full-genome dataset assembled included 104 PDCoV genomes from pigs, 4 from sparrows (Supplementary Table 1 ) and 3 newly sequenced Hu-PDCoV strains, which were aligned with MAFFT v.7.407 (ref.
- Full pipeline: alignment/mapping [MAFFT v7.407] -> dimensionality reduction/clustering [PyMOL] -> visualisation [PyMOL] -> stage not stated [IQ-TREE v2.0.6]

### The structural basis of odorant recognition in insect olfactory receptors. (Nature 2021)

- DOI: 10.1038/s41586-021-03794-8 | PMCID: PMC8410599 | PMID: 34349260
- Evidence: 11a , the alignment between the sequences of Mh OR1 and Mh OR5 was done using MAFFT implemented in JalView 57 with minimal manual adjustment based on the structure of Mh OR5.
- Full pipeline: alignment/mapping [MAFFT, MotionCor2, RELION v3.0] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [scikit-learn] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, PyMOL]

### Universal nomenclature for oxytocin-vasotocin ligand and receptor families. (Nature 2021)

- DOI: 10.1038/s41586-020-03040-7 | PMCID: PMC8081664 | PMID: 33911268
- Evidence: Gene tree phylogeny analyses Exonic nucleotide tree Exonic sequences from all the OTR-VTRs from representative species that had the most-complete assembled genes were aligned with MAFFT under the E-INS-i parameter set, which is optimized for sequences with multiple conserved domains and long gaps.
- Full pipeline: alignment/mapping [BLAST, MAFFT] -> stage not stated [RepeatMasker]

### Anaerobic endosymbiont generates energy for ciliate host by denitrification. (Nature 2021)

- DOI: 10.1038/s41586-021-03297-6 | PMCID: PMC7969357 | PMID: 33658719
- Evidence: For the ciliate phylogeny, sequences obtained from Sanger sequencing of picked ciliates were added to the EukRef-Ciliphora 30 Plagiopylea subgroup alignment using MAFFT 79 online service version 7 (argument:--addfragments).
- Full pipeline: read trimming [SPAdes v3.13.0, Trimmomatic] -> alignment/mapping [BLAST, MAFFT, MUSCLE, SPAdes v3.13.0, eggNOG] -> quantification [SAMtools] -> dimensionality reduction/clustering [MUSCLE] -> structure determination [Trimmomatic] -> stage not stated [Bowtie2, IQ-TREE, Prokka, RAxML]

### SARS-CoV-2 evolution during treatment of chronic infection. (Nature 2021)

- DOI: 10.1038/s41586-021-03291-y | PMCID: PMC7610568 | PMID: 33545711
- Version used: **7.475**
- Evidence: All sequences were aligned to the SARS-CoV-2 reference strain MN908947.3 , using MAFFT v7.475 with automatic flavour selection 31 .
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [MAFFT v7.475] -> stage not stated [BCFtools, IQ-TREE v2.1.2, Nextstrain, Picard, SAMtools v1.11]

### Giant lungfish genome elucidates the conquest of land by vertebrates. (Nature 2021)

- DOI: 10.1038/s41586-021-03198-8 | PMCID: PMC7875771 | PMID: 33461212
- Evidence: Individual loci were filtered with PREQUAL 73 , aligned with MAFFT ginsi 74 and highly incomplete positions (>80%) trimmed with BMGE 75 .
- Full pipeline: read trimming [MAFFT, Trimmomatic v0.36] -> alignment/mapping [HISAT2 v2.1.0, IQ-TREE, MAFFT, MUSCLE, RAxML v8.2.4, StringTie v1.3.6, kallisto v0.46.1] -> dimensionality reduction/clustering [R v3.6] -> structure determination [RAxML v8.2.4, StringTie v1.3.6] -> stage not stated [BUSCO, RepeatMasker, SPAdes v3.13.3, phytools]

### Functional refolding of the penetration protein on a non-enveloped virus. (Nature 2021)

- DOI: 10.1038/s41586-020-03124-4 | PMCID: PMC8297411 | PMID: 33442061
- Evidence: We retrieved rotavirus sequences from GenBank 46 with BioPython 47 , aligned them with MAFFT 48 , and used ESPript 49 to display the multiple sequence alignments of VP4 ( Supplementary Data 1 ), VP7 ( Supplementary Data 2 ), and VP6 ( Supplementary Data 3 ).
- Full pipeline: alignment/mapping [IMOD, MAFFT, MotionCor2, Python] -> registration [MotionCor2] -> structure determination [EMAN2] -> stage not stated [CTFFIND, Matplotlib, PyMOL]

### A 2-million-year-old ecosystem in Greenland uncovered by environmental DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05453-y | PMCID: PMC9729109 | PMID: 36477129
- Evidence: We used MAFFT 84 to align each of these sets of reference sequences, and inspected multiple sequence alignments in NCBI MSAViewer to confirm quality 85 .
- Full pipeline: alignment/mapping [BWA, Bowtie2, MAFFT, Picard, Python, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [BCFtools, Kraken2]

### Direct activation of a bacterial innate immune system by a viral capsid protein. (Nature 2022)

- DOI: 10.1038/s41586-022-05444-z | PMCID: PMC9712102 | PMID: 36385533
- Evidence: 1 , sequences were aligned with MAFFT L-INS-i v7.453 (ref.
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> stage not stated [AlphaFold, BLAST, CCP4, PHENIX]

### Borgs are giant genetic elements with potential to expand metabolic capacity. (Nature 2022)

- DOI: 10.1038/s41586-022-05256-1 | PMCID: PMC9605863 | PMID: 36261517
- Evidence: Proteins were compared using blastp and aligned using MAFFT 47 v.7.407 to visualize homologous regions and check conserved amino acid residues that constitute the active site or are required for cofactor and ligand binding.
- Full pipeline: alignment/mapping [BLAST, IQ-TREE v1.6.6, MAFFT, SciPy] -> quantification [SciPy] -> visualisation [BLAST, IQ-TREE v1.6.6, MAFFT] -> stage not stated [HMMER]

### Structure of the OMEGA nickase IsrB in complex with ωRNA and target DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05324-6 | PMCID: PMC9581776 | PMID: 36224386
- Evidence: Representative sequences containing IF-3-N-terminal regions and PLMP domains from the IscB/IsrB family were obtained from UniProt and the National Center for Biotechnology Information, and aligned using MAFFT-einsi.
- Full pipeline: alignment/mapping [MAFFT, MotionCor2] -> structure determination [ColabFold, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND, Python]

### Visualizing translation dynamics at atomic detail inside a bacterial cell. (Nature 2022)

- DOI: 10.1038/s41586-022-05255-2 | PMCID: PMC9534751 | PMID: 36171285
- Evidence: ...se 69 ; (iv) as M. pneumoniae M129 is not among the representative species, its protein sequences were added to the multiple sequence alignments with MAFFT software 70 ; (v) for each COG multiple sequence alignment, the number of amino acids in every representative species (including M. pneumoniae M129) present at positions before the N terminus and after the C terminus positions of E. coli K-12 s...
- Full pipeline: alignment/mapping [MAFFT, eggNOG] -> dimensionality reduction/clustering [eggNOG] -> structure determination [Coot, PHENIX, Python v3.7.7] -> visualisation [ChimeraX] -> stage not stated [RELION v3.0]

### Divergent genomic trajectories predate the origin of animals and fungi. (Nature 2022)

- DOI: 10.1038/s41586-022-05110-4 | PMCID: PMC9492541 | PMID: 36002568
- Evidence: We manually curated the 69 OGs that survived to this filter by performing individual phylogenies for each one, using MAFFT 40 v7.123b [-einsi] for sequence alignment, trimAl 41 v1.4.rev15 [-gappyout] for alignment trimming and IQ-TREE 42 v1.6.7 for maximum-likelihood (ML) phylogenetic inference, using ModelFinder 43 for model selection.
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [BLAST, IQ-TREE, MAFFT, OrthoFinder, eggNOG] -> dimensionality reduction/clustering [OrthoFinder, eggNOG] -> differential/statistical testing [NumPy, Python, ggplot2] -> structure determination [R] -> stage not stated [Keras, SciPy, TensorFlow]

### Pandemic-scale phylogenomics reveals the SARS-CoV-2 recombination landscape. (Nature 2022)

- DOI: 10.1038/s41586-022-05189-9 | PMCID: PMC9519458 | PMID: 35952714
- Evidence: We then aligned the sequences of all descendants for each trio using MAFFT 30 , focusing specifically on recombination-informative sites, that is, where the allele of the recombinant node matched one parent node but not the other.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [Pangolin, R]

### Structures and mechanism of the plant PIN-FORMED auxin transporter. (Nature 2022)

- DOI: 10.1038/s41586-022-04883-y | PMCID: PMC9477730 | PMID: 35768502
- Evidence: In brief, MAFFT was used for multiple sequence alignment (MSA), BMGE was used for MSA pruning and FastME was used for unrooted tree generation.
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [PHENIX, RoseTTAFold] -> visualisation [PyMOL] -> stage not stated [Coot]

### Biosynthetic potential of the global ocean microbiome. (Nature 2022)

- DOI: 10.1038/s41586-022-04862-3 | PMCID: PMC9259500 | PMID: 35732736
- Version used: **7.310**
- Evidence: Briefly, the 31,398 terpene biosynthetic core genes identified across all predicted BGCs were filtered (length > = 120aa, removing < 2% of the sequences), dereplicated (using MMSEQS2 13.45111 101 clustering, 60% identity) into 2,904 protein sequences and aligned with the 195 MIBiG proteins using MAFFT v7.310 102 .
- Full pipeline: read trimming [IQ-TREE v2.0.3] -> alignment/mapping [BWA v0.7.17, DIAMOND v0.9.30, IQ-TREE v2.0.3, MAFFT v7.310, MUSCLE v3.8.1551] -> dimensionality reduction/clustering [MAFFT v7.310, UMAP] -> visualisation [R v4.0.0, ggplot2 v3.3.0] -> stage not stated [HMMER v3.1b, eggNOG v5.0, featureCounts v2.0.1]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **7.471**
- Evidence: A total of 3,971 single-copy orthologues gene clusters were then generated and 32-way protein alignments for these genes were computed using MAFFT (v.7.471) (ref.
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Reversible RNA phosphorylation stabilizes tRNA for cellular thermotolerance. (Nature 2022)

- DOI: 10.1038/s41586-022-04677-2 | PMCID: PMC9095486 | PMID: 35477761
- Evidence: Bacterial and archaeal homologs of ArkI are added using MAFFT ( https://mafft.cbrc.jp/alignment/server/ ).
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [PHENIX, PyMOL] -> visualisation [PyMOL]

### Prolonged viral suppression with anti-HIV-1 antibody therapy. (Nature 2022)

- DOI: 10.1038/s41586-022-04597-1 | PMCID: PMC9177424 | PMID: 35418681
- Version used: **7.487**
- Evidence: Phylogenetic analysis Nucleotide alignments of env sequences were translation aligned using MAFFT v7.487 under the BLOSUM62 cost matrix.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [MAFFT v7.487] -> stage not stated [SPAdes v3.13.0]

### Rapid epidemic expansion of the SARS-CoV-2 Omicron variant in southern Africa. (Nature 2022)

- DOI: 10.1038/s41586-022-04411-y | PMCID: PMC8942855 | PMID: 35042229
- Evidence: These sequences were aligned together with a set of five high-quality BA.1, six BA.2 and one BA.3 sequences (representing the known diversity of these clades on 5 December 2021) using MAFFT 62 with the default settings.
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT] -> variant calling [GATK] -> normalisation [TreeTime] -> structure determination [FastQC] -> visualisation [PyMOL] -> stage not stated [BEAST v1.10.4, Nextflow, Nextstrain, R, emmeans]

### Malaria protection due to sickle haemoglobin depends on parasite genotype. (Nature 2022)

- DOI: 10.1038/s41586-021-04288-3 | PMCID: PMC8810385 | PMID: 34883497
- Evidence: To further inspect sequence identity, we used MAFFT to generate a multiple sequence alignment (MSA) corresponding to the 1001 bp sequence centred at each locus.
- Full pipeline: alignment/mapping [MAFFT, STAR v2.7.3a, minimap2] -> variant calling [GATK] -> stage not stated [Stan]

### Enhanced fusogenicity and pathogenicity of SARS-CoV-2 Delta P681R mutation. (Nature 2022)

- DOI: 10.1038/s41586-021-04266-9 | PMCID: PMC8828475 | PMID: 34823256
- Evidence: We next collected 334 representative SARS-CoV-2 sequences and aligned the entire genome sequences using the FFT-NS-1 program in the MAFFT suite (v.7.407) 34 .
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [MAFFT, fastp v0.21.0] -> variant calling [SAMtools v1.9] -> stage not stated [BWA v0.7.17, IQ-TREE, ImageJ v2.2.0]

### Bacteriophages suppress CRISPR-Cas immunity using RNA-based anti-CRISPRs. (Nature 2023)

- DOI: 10.1038/s41586-023-06612-5 | PMCID: PMC10651486 | PMID: 37853129
- Evidence: Selection and cloning of Racr candidates Candidate Racrs were chosen on the basis of their similarity of sequence and secondary RNA structure to the relevant CRISPR repeats in the model system (MAFFT alignments, FastTree approximately maximum-likelihood phylogenetic trees; Extended Data Figs.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, Bowtie2, MAFFT, SAMtools v1.16.1]

### A pan-influenza antibody inhibiting neuraminidase via receptor mimicry. (Nature 2023)

- DOI: 10.1038/s41586-023-06136-y | PMCID: PMC10266979 | PMID: 37258672
- Evidence: Protein sequences were aligned to a reference NA sequence using MAFFT 82 .
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT, MotionCor2] -> stage not stated [R, RELION, UCSF Chimera]

### Ancient gene linkages support ctenophores as sister to other animals. (Nature 2023)

- DOI: 10.1038/s41586-023-05936-6 | PMCID: PMC10232365 | PMID: 37198475
- Version used: **7.310**
- Evidence: Identification of orthologues in other species For each of the 291 orthologues, we aligned the proteins using MAFFT (v.7.310) 100 , built a hidden Markov Model using hmmbuild in hmmer (v.3.3.2) 101 , then found the best match using hmmsearch in the proteins of the genomes of other species, including the ctenophore B. microptera , the cladorhizid sponge, T. adhaerens 102 , H. vulgaris 12 , N. vecte...
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.310, STAR v2.7.1a, Trinity v2.5.1, minimap2 v2.23] -> differential/statistical testing [MrBayes v3.2.7a] -> visualisation [MrBayes v3.2.7a] -> stage not stated [BLAST, BUSCO, OrthoFinder v2.3.7, hifiasm v0.16.1]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Evidence: The sequence-selected region or regions were then retrieved and aligned against the corresponding GRCh38 region using MAFFT.
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Mirusviruses link herpesviruses to giant viruses. (Nature 2023)

- DOI: 10.1038/s41586-023-05962-4 | PMCID: PMC10132985 | PMID: 37076623
- Evidence: Finally, we included reference RNApolB amino acid sequences from Bacteria, Archaea, Eukarya and giant viruses 9 : the sequences were aligned with MAFFT 49 v7.464 and the FFT-NS-i algorithm with default parameters and trimmed at >50% gaps with Goalign v0.3.5 ( https://www.github.com/evolbioinfo/goalign ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [BLAST, BWA v0.7.15, MAFFT, SAMtools] -> dimensionality reduction/clustering [OrthoFinder] -> differential/statistical testing [IQ-TREE, SAMtools] -> structure determination [BLAST, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, RoseTTAFold]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Version used: **7.3**
- Evidence: Alignments derived from each orthologue were aligned using MAFFT (v.7.3) 84 , trimmed for misaligned regions using BMGE (v.1.12) 85 and assembled in a supermatrix.
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Genomic investigations of unexplained acute hepatitis in children. (Nature 2023)

- DOI: 10.1038/s41586-023-06003-w | PMCID: PMC10170458 | PMID: 36996872
- Evidence: Samples were aligned along with known reference strains from GenBank using MAFFT 65 (version v7.271), and the trees were built with IQ-TREE 66 (multicore version 1.6.12) with 1,000 rapid bootstraps and approximate likelihood-ratio test support.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Picard v2.26.9, SAMtools, Trim Galore] -> alignment/mapping [BCFtools, BWA, IQ-TREE, MAFFT, Picard v2.26.9, SAMtools, minimap2] -> variant calling [BCFtools] -> visualisation [Picard v2.26.9, SAMtools] -> stage not stated [Bowtie2, Kraken2, R]

### Adeno-associated virus 2 infection in children with non-A-E hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05948-2 | PMCID: PMC7617659 | PMID: 36996873
- Evidence: All linear complete AAV2 genomes returned from BLAST against the GenBank nucleotide database with a query coverage of >75% were selected and combined with the AAV sequences de novo assembled here and aligned using MAFFT.
- Full pipeline: read trimming [BWA, IQ-TREE, Trim Galore] -> alignment/mapping [BWA, IQ-TREE, MAFFT, Trim Galore] -> quantification [QuPath v0.3.2] -> differential/statistical testing [R]

### Adeno-associated virus type 2 in US children with acute severe hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05949-1 | PMCID: PMC10170441 | PMID: 36996871
- Evidence: For HAdV-41, 22 representative HAdV-41 genomes were aligned using MAFFT, and for AAV, 11 genomes representing AAV1–AAV8 were aligned using MAFFT.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.0.3, SciPy] -> visualisation [Jupyter, Matplotlib v3.3.2, Python, seaborn v0.11.0] -> stage not stated [Bowtie2, IQ-TREE v1.6.1]

### From primordial clocks to circadian oscillators. (Nature 2023)

- DOI: 10.1038/s41586-023-05836-9 | PMCID: PMC10076222 | PMID: 36949197
- Evidence: A multiple sequence alignment of the selected 1,538 sequences was generated using MAFFT 39 – 41 (Supplementary Dataset 1 ).
- Full pipeline: alignment/mapping [IQ-TREE v1.6, MAFFT, RAxML v8.2.9] -> simulation/modelling [UCSF Chimera v1.15] -> structure determination [Coot v0.9.81, PHENIX v1.20.1] -> visualisation [PyMOL v2.6.0]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Evidence: In addition, 15 curated CHRD and CHRDL protein sequences (and an outgroup) were obtained from various sources (Supplementary Table 10 ) and aligned together with O. fusiformis CHRD and CHRDL sequences in MAFFT (v.7) 91 with the G-INS-I iterative refinement method and default scoring parameters.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Cas12a2 elicits abortive infection through RNA-triggered destruction of dsDNA. (Nature 2023)

- DOI: 10.1038/s41586-022-05559-3 | PMCID: PMC9811890 | PMID: 36599979
- Version used: **7.490**
- Evidence: Phylogenetic analysis of Cas12a2 proteins within type V systems The amino acid sequences of Cas12a2, Cas12a and Cas13b orthologues were aligned using MAFFT (v.7.490) 53 .
- Full pipeline: read trimming [RAxML] -> alignment/mapping [Bowtie2, MAFFT v7.490, RAxML] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST, Python]

### Phenotypic signatures of immune selection in HIV-1 reservoir cells. (Nature 2023)

- DOI: 10.1038/s41586-022-05538-8 | PMCID: PMC9908552 | PMID: 36599977
- Evidence: Phylogenetic distances between sequences were examined using maximum-likelihood trees in MEGA ( https://www.megasoftware.net ) and MAFFT ( https://mafft.cbrc.jp/alignment/software ), and visualized using highlighter plots ( https://www.lanl.gov ).
- Full pipeline: quality control [UMAP] -> alignment/mapping [MAFFT, SAMtools v1.9] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [R] -> visualisation [MAFFT, UMAP] -> stage not stated [Cutadapt v2.5]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Version used: **7.427**
- Evidence: Ribosomal markers were aligned using the L-INSi algorithm of MAFFT (v.7.427) 82 and trimmed using BMGE using the default parameters 83 .
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Evidence: Unique sequences were identified by clustering at 100% identity using CD-Hit 96 and were aligned using MAFFT 119 v.7.490.
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Releasing a sugar brake generates sweeter tomato without yield penalty. (Nature 2024)

- DOI: 10.1038/s41586-024-08186-2 | PMCID: PMC11578880 | PMID: 39537922
- Version used: **7.525**
- Evidence: The annotated protein sequences were subjected to multiple sequence alignment using MAFFT (version 7.525) 80 and phylogenetic tree construction using the neighbour-joining method in the MEGA program (version 11.0.10) 81 .
- Full pipeline: alignment/mapping [MAFFT v7.525] -> quantification [ImageJ] -> visualisation [ggplot2 v3.4.4] -> stage not stated [IQ-TREE, PLINK, Python, VCFtools v0.1.16]

### Rifaximin prophylaxis causes resistance to the last-resort antibiotic daptomycin. (Nature 2024)

- DOI: 10.1038/s41586-024-08095-4 | PMCID: PMC11602712 | PMID: 39443798
- Evidence: Modelling was performed based on the consensus between sequence alignments from MAFFT-DASH 69 , T-COFFEE 70 and Clustal-W 71 (within Maestro), which were manually optimized to minimize sequence gaps.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2, HTSeq, MAFFT] -> quantification [Bowtie2, HTSeq] -> differential/statistical testing [tidyverse v1.3.1] -> visualisation [R v4.0.3, tidyverse v1.3.1] -> stage not stated [IQ-TREE v2.1.2, Kraken2]

### An ancient ecospecies of Helicobacter pylori. (Nature 2024)

- DOI: 10.1038/s41586-024-07991-z | PMCID: PMC11541087 | PMID: 39415013
- Version used: **7.505**
- Evidence: When looking at specific genes ( vacA , ureA , ureB ), gene sequences were first obtained from the individual strains annotation file then aligned using MAFFT (v.7.505, option --auto) 61 .
- Full pipeline: alignment/mapping [MAFFT v7.505, PLINK v1.9] -> dimensionality reduction/clustering [GEMMA v0.93, PLINK v1.9, pheatmap v1.0.12] -> stage not stated [BLAST v2.11.0, NumPy v1.23.2, Prokka, R, SPAdes, VCFtools v0.1.17, ggplot2 v3.3.6, tidyverse v1.3.2]

### Diverse anti-defence systems are encoded in the leading region of plasmids. (Nature 2024)

- DOI: 10.1038/s41586-024-07994-w | PMCID: PMC11541004 | PMID: 39385022
- Evidence: The pHMM database included all subclusters with more than five members after aligning the orthologues with MAFFT 67 and building the model using HMMer suite’s hmmbuild (v.3.3.2) 68 .
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> visualisation [ChimeraX] -> stage not stated [BLAST, HMMER, Prokka]

### Drosophila are hosts to the first described parasitoid wasp of adult flies. (Nature 2024)

- DOI: 10.1038/s41586-024-07919-7 | PMCID: PMC11424482 | PMID: 39261731
- Version used: **7.49**
- Evidence: For all phylogenies, sequences were aligned using MAFFT 7.49 (ref.
- Full pipeline: alignment/mapping [MAFFT v7.49] -> visualisation [R] -> stage not stated [Flye v2.9.1]

### Mechanism of BRCA1-BARD1 function in DNA end resection and DNA protection. (Nature 2024)

- DOI: 10.1038/s41586-024-07909-9 | PMCID: PMC11464378 | PMID: 39261728
- Evidence: Sequence analysis of BRCA1 and BARD1 proteins Alignment of the BRCA1 region 931–1171 and of the BARD1 region 123–261 were generated using the MAFFT method 58 and represented using Jalview 59 .
- Full pipeline: alignment/mapping [MAFFT]

### Mapping glycoprotein structure reveals Flaviviridae evolutionary history. (Nature 2024)

- DOI: 10.1038/s41586-024-07899-8 | PMCID: PMC11410658 | PMID: 39232167
- Evidence: These nucleotide sequences were translated using the Geneious Prime Find ORFs tool (v2022.0) ( https://www.geneious.com/ ) 58 and along with protein sequences aligned to annotated reference sequences (where available) using MAFFT FFT-NS-I X2 (v7.402) to assess genome completeness 59 .
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Clustal Omega v1.2.4, MAFFT, MUSCLE v5.1] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX] -> stage not stated [AlphaFold v2.3, BLAST v2.0.9, ColabFold v1.5.1, IQ-TREE, InterProScan, Python, phytools v1.5]

### Global marine microbial diversity and its potential in bioprospecting. (Nature 2024)

- DOI: 10.1038/s41586-024-07891-2 | PMCID: PMC11390488 | PMID: 39232160
- Version used: **7.407**
- Evidence: The multi-sequence alignment of PETase candidates was carried out by MAFFT (v7.407), and the phylogenetic tree was constructed by FastTree (v2.1.10) 117 .
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.407, MUSCLE v3.8.31] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [AlphaFold v2.3.0, InterProScan v5.0, Prokka v1.14.6, R, ggplot2 v3.5.1]

### Spillover of highly pathogenic avian influenza H5N1 virus to dairy cattle. (Nature 2024)

- DOI: 10.1038/s41586-024-07849-4 | PMCID: PMC11485258 | PMID: 39053575
- Version used: **7.515**
- Evidence: In brief, multiple sequence alignments were performed using MAFFT (v7.515) 63 ; maximum likelihood trees were inferred using IQ-TREE (v1.6.12) 64 , and the initial tree was refined using sequence metadata through the augur refine subcommand.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.515, Trimmomatic v0.39] -> structure determination [IQ-TREE v1.6.12, MAFFT v7.515] -> stage not stated [Bracken, Medaka, Nextstrain v21.0.1, Prokka, TreeTime v0.9.4]

### In situ targeted base editing of bacteria in the mouse gut. (Nature 2024)

- DOI: 10.1038/s41586-024-07681-w | PMCID: PMC11338833 | PMID: 38987595
- Evidence: The sequences were aligned using MAFFT 74 v.7.520 with default parameters and with the option --treeout to export the guide tree.
- Full pipeline: alignment/mapping [MAFFT, Python] -> dimensionality reduction/clustering [QIIME 2] -> stage not stated [Cutadapt v3.3, Matplotlib, fastp, seaborn]

### Zinc mediates control of nitrogen fixation via transcription factor filamentation. (Nature 2024)

- DOI: 10.1038/s41586-024-07607-6 | PMCID: PMC11222152 | PMID: 38926580
- Version used: **7.490**
- Evidence: FUN protein sequences were identified by BLAST and SHOOT 44 and aligned with MAFFT 7.490 and a tree constructed using FastTree 2.1.11.
- Full pipeline: alignment/mapping [MAFFT v7.490] -> quantification [ImageJ]

### The complete sequence and comparative analysis of ape sex chromosomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07473-2 | PMCID: PMC11168930 | PMID: 38811727
- Version used: **7.520**
- Evidence: The sequences of the 5′ UTR, CDS exons, 3′ untranslated regions and introns were retrieved and the generated fasta files were then used for alignment with MAFFT v7.520 111 .
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.520, STAR, minimap2] -> variant calling [GATK, VCFtools] -> quantification [VCFtools] -> stage not stated [BEDTools, BUSCO, Flye, HMMER, RepeatMasker]

### Life-cycle-coupled evolution of mitosis in close relatives of animals. (Nature 2024)

- DOI: 10.1038/s41586-024-07430-z | PMCID: PMC11153136 | PMID: 38778110
- Version used: **7.490**
- Evidence: The multiple sequence alignment was done with MAFFT v.7.490 using ‘linsi’ optimized for local homology 53 .
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [HMMER v3.3.2, ImageJ, Matplotlib, NumPy, OpenCV, Python, SciPy, scikit-image]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: ... identity between preliminary MAGs; USEARCH 71 v.11.0.667 for clustering sequences on the basis of similarity before phylogenetic tree constructions; MAFFT 72 v.7.505 for calculating and trimAl 73 v.1.4.1 for trimming multiple sequence alignments; ModelFinder 74 for predicting best-fitting models; and UFBoot2 (ref.
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### Phylogenomics and the rise of the angiosperms. (Nature 2024)

- DOI: 10.1038/s41586-024-07324-0 | PMCID: PMC11111409 | PMID: 38658746
- Version used: **7.480**
- Evidence: In the first iteration, all sequences for a given gene were aligned using MAFFT v.7.480 (ref.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MAFFT v7.480] -> stage not stated [IQ-TREE v2.2.0, R]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Version used: **7.453**
- Evidence: Candidate cis -regulatory element orthologues across all species were then combined into a multi-fasta file and aligned using MAFFT v.7.453 (parameters: --adjustdirectionaccurately --localpair --maxiterate 1000).
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: We randomly selected 100 and 50 α-satellite monomers from the HOR/dimeric array and monomeric regions, respectively, and aligned them with MAFFT 79 , 80 (v.7.453).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### Complexity of avian evolution revealed by family-level genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07323-1 | PMCID: PMC11111414 | PMID: 38560995
- Evidence: This was done with an iterative PASTA 54 v.1.8.5 pipeline that included TreeShrink 55 v.1.3.1 to remove outlier sequences, alignment with MAFFT 56 v.7.149b G-INS-i with a variable scoring matrix 57 to isolate potentially unrelated segments and removal of these blocks.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE, RAxML]

### The complex polyploid genome architecture of sugarcane. (Nature 2024)

- DOI: 10.1038/s41586-024-07231-4 | PMCID: PMC11041754 | PMID: 38538783
- Version used: **7.487**
- Evidence: Multiple sequence alignments among syntenic orthogroups for sugar transport gene candidates were performed using MAFFT (v.7.487) 73 and were visualized using ggmsa 74 (script MSAalignmentPlots.R).
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, MAFFT v7.487, R, SAMtools, minimap2 v2.20] -> variant calling [minimap2 v2.20] -> machine learning [AUGUSTUS v3.1.0] -> visualisation [MAFFT v7.487] -> stage not stated [BEDTools, BUSCO, Jupyter, RepeatMasker]

### Homo sapiens reached the higher latitudes of Europe by 45,000 years ago. (Nature 2024)

- DOI: 10.1038/s41586-023-06923-7 | PMCID: PMC10849966 | PMID: 38297117
- Version used: **7.453**
- Evidence: MAFFT (v7.453) 75 was used to realign all ten newly reconstructed human mtDNA genomes to the rCRS with previously published mtDNA genomes from 54 modern humans, 19 ancient humans and 2 Neanderthals.
- Full pipeline: alignment/mapping [BWA] -> registration [MAFFT v7.453] -> structure determination [MAFFT v7.453] -> stage not stated [BEAST v2.6.6, QGIS, R v4.1, SAMtools]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Version used: **7.467**
- Evidence: A multiple reference-based genome alignment for all sequences was generated in MAFFT v7.467 94 (using parameters: --adjustdirection --auto --fastaout --reorder).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### The hagfish genome and the evolution of vertebrates. (Nature 2024)

- DOI: 10.1038/s41586-024-07070-3 | PMCID: PMC10972751 | PMID: 38262590
- Version used: **7.305**
- Evidence: To do that, we generated individual alignments using MAFFT (v.7.305) 95 , filtered them using BMGE and reconstructed a tree using IQ-TREE and an LG+R model 89 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.1, MAFFT v7.305, SAMtools, STAR v2.5.2b, StringTie v1.3.3b] -> quantification [R, Salmon v1.10.0, WGCNA v1.7.0] -> dimensionality reduction/clustering [R, WGCNA v1.7.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.305] -> machine learning [RAxML v8.2.12] -> stage not stated [BLAST, BUSCO, ImageJ v1.53k, RepeatMasker v1.0.11, Trinity v2.11.0, eggNOG]

### Bioactive glycans in a microbiome-directed food for children with malnutrition. (Nature 2024)

- DOI: 10.1038/s41586-023-06838-3 | PMCID: PMC10764277 | PMID: 38093016
- Evidence: Concatenated nucleotide sequences of 142 identified core genes were aligned using MAFFT 52 (v.7.313).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, IQ-TREE, R, Trim Galore, edgeR] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT, R, kallisto, scikit-learn] -> quantification [kallisto, lme4] -> normalisation [edgeR] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [GSEA, edgeR, lme4] -> stage not stated [BLAST, Bracken, DESeq2, Flye, Kraken2, Pilon, fgsea]

### Predicting multiple conformations via sequence clustering and AlphaFold2. (Nature 2024)

- DOI: 10.1038/s41586-023-06832-9 | PMCID: PMC10808063 | PMID: 37956700
- Evidence: The selected 1,270 sequences were aligned using MAFFT 63 .
- Full pipeline: read trimming [RAxML v8.2.9] -> alignment/mapping [AlphaFold, MAFFT, RAxML v8.2.9] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST v2.6.0, ColabFold, IQ-TREE, PyMOL, SciPy]

### Florigen activation complex forms via multifaceted assembly in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-025-09704-6 | PMCID: PMC12711580 | PMID: 41225013
- Evidence: MAFFT 75 v.7.490 with auto parameters was used for protein sequence alignment.
- Full pipeline: alignment/mapping [MAFFT] -> quantification [Cellpose v2.2.3] -> stage not stated [AlphaFold, ColabFold, IQ-TREE v1.5.5]

### Viral NblA proteins negatively affect oceanic cyanobacterial photosynthesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09656-x | PMCID: PMC12695635 | PMID: 41224996
- Version used: **7.475**
- Evidence: Genes were predicted with Prodigal (v.2.6.3) 84 and maximum-likelihood phylogeny was reconstructed with Phylophlan (v.3.0.2) 85 , Diamond (v.2.1.8) 86 , MAFFT (v.7.475) 87 , trimAl (v.1.4.1) 88 and IQ-TREE (v.2.1.2) 89 ) based on concatenated alignments of protein sequences of nine core genes: primase-helicase, exonuclease, portal protein (head-to-tail adaptor), head assembly protein, major capsid...
- Full pipeline: alignment/mapping [IQ-TREE v2.1.2, MAFFT v7.475] -> quantification [featureCounts] -> structure determination [IQ-TREE v2.1.2, MAFFT v7.475] -> stage not stated [AlphaFold, BLAST, ColabFold, HMMER v3.4, eggNOG, lme4 v1.1]

### A vaccine central in A(H5) influenza antigenic space confers broad immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09626-3 | PMCID: PMC12657240 | PMID: 41094140
- Version used: **7.515**
- Evidence: After preprocessing, sequences were aligned using MAFFT (v.7.515) 63 , and the alignment was trimmed to the start and stop codons of the majority of sequences.
- Full pipeline: read trimming [MAFFT v7.515] -> alignment/mapping [MAFFT v7.515] -> differential/statistical testing [ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [R v4.4.3]

### Isolation, engineering and ecology of temperate phages from the human gut. (Nature 2025)

- DOI: 10.1038/s41586-025-09614-7 | PMCID: PMC12629997 | PMID: 41094135
- Evidence: The protein sequences were concatenated and aligned using MAFFT 55 (v.7.310) before gaps were trimmed with trimAI 56 (v.1.4.1).
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT] -> structure determination [Python] -> visualisation [RAxML, ggplot2 v3.5.1, ggpubr v0.4.0] -> stage not stated [BEDTools v2.26.0, BLAST v2.7.1, Bowtie2, HMMER, SAMtools]

### Somatic mutation and selection at population scale. (Nature 2025)

- DOI: 10.1038/s41586-025-09584-w | PMCID: PMC12611758 | PMID: 41062696
- Evidence: We built a multiple sequence alignment of these genomes with MAFFT 65 using Jalview 66 .
- Full pipeline: alignment/mapping [MAFFT] -> variant calling [BEDTools, GATK] -> differential/statistical testing [lme4] -> stage not stated [BCFtools, R]

### A miniature CRISPR-Cas10 enzyme confers immunity by inhibitory signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09569-9 | PMCID: PMC12657230 | PMID: 41034576
- Evidence: Sequences were trimmed and aligned using MAFFT alignment with default parameters in Geneious Prime (v2023.2.1).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Matplotlib v3.7.2, Python, seaborn v0.13.2] -> stage not stated [ColabFold, Galaxy, Jupyter, PHENIX]

### One mother for two species via obligate cross-species cloning in ants. (Nature 2025)

- DOI: 10.1038/s41586-025-09425-w | PMCID: PMC12507663 | PMID: 40903579
- Evidence: Alignments for each of 5,856 single-copy genes were built separately using MAFFT 75 .
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [MAFFT, SAMtools v1.15.1, fastp v0.23.2] -> variant calling [GATK v4.3, VCFtools v0.1.16] -> stage not stated [BCFtools v1.15.1, BUSCO v4.0.5, IQ-TREE v2.07, PLINK, Python, QUAST v5.0]

### Microbial iron oxide respiration coupled to sulfide oxidation. (Nature 2025)

- DOI: 10.1038/s41586-025-09467-0 | PMCID: PMC12545173 | PMID: 40866705
- Version used: **7.407**
- Evidence: The alignment for EPA was generated using MAFFT v7.407 with --add option.
- Full pipeline: alignment/mapping [MAFFT v7.407, RAxML v8.2.12] -> structure determination [RAxML v8.2.12] -> visualisation [R v4.1] -> stage not stated [AlphaFold v2.3.2, AutoDock Vina v1.1.2, DESeq2 v3.19, HMMER, ImageJ, featureCounts]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Version used: **7.471**
- Evidence: We constructed sequence alignments for all families including more than 6 genes, more than 3 species and fewer than 400 sequences in total using MAFFT (v.7.471) 78 filtered with CLIPKIT (v.1.1.6, -m gappy) 79 and an initial tree reconstructed with IQ-TREE (v.2.1.1) assuming the LG + R model 80 .
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Evidence: These sequences were aligned using MAFFT 73 and then manually corrected using Geneious Prime (v.2021.1.1; https://www.geneious.com ).
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Complete biosynthesis of salicylic acid from phenylalanine in plants. (Nature 2025)

- DOI: 10.1038/s41586-025-09175-9 | PMCID: PMC12408352 | PMID: 40702181
- Version used: **7.526**
- Evidence: The retained protein sequences with at least one conserved domain (Supplementary Table 10 ) were then used for multiple sequence alignment with MAFFT v7.526 69 and construction of maximum-likelihood gene trees with 500 bootstrap replicates and optimal model using RAxML (v.8.2.12) 70 .
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.526, Picard, RAxML v8.2.12] -> stage not stated [InterProScan v5.69]

### Deciphering phenylalanine-derived salicylic acid biosynthesis in plants. (Nature 2025)

- DOI: 10.1038/s41586-025-09280-9 | PMCID: PMC12408371 | PMID: 40702180
- Evidence: The identified sequences were aligned using MAFFT 68 v7.490, and poorly aligned regions were trimmed using TrimAl 69 v1.4.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> visualisation [Cytoscape] -> stage not stated [IQ-TREE, ImageJ v1.42q]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **7.490**
- Evidence: Multiple sequence alignment was carried out with MAFFT (version 7.490).
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Cryptic variation fuels plant phenotypic change through hierarchical epistasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09243-0 | PMCID: PMC12282530 | PMID: 40634606
- Version used: **7.505**
- Evidence: Retrieved protein sequences were aligned using MAFFT (v.7.505) using the default parameters.
- Full pipeline: read trimming [STAR v2.6.1, Trimmomatic] -> alignment/mapping [HMMER v3.3.2, MAFFT v7.505, STAR v2.6.1, Trimmomatic] -> dimensionality reduction/clustering [DESeq2, scikit-learn] -> differential/statistical testing [DESeq2, scikit-learn] -> stage not stated [IQ-TREE v2.2.2, PyTorch, statsmodels]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: The alignment was performed with MAFFT 70 , and the phylogenetic tree was calculated using IQ-TREE 71 with the following settings: -m MFP --con-tree --burnin 250 -B 1000 -T 36 --wbtl.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Protein-primed homopolymer synthesis by an antiviral reverse transcriptase. (Nature 2025)

- DOI: 10.1038/s41586-025-09179-5 | PMCID: PMC12483538 | PMID: 40436039
- Evidence: These proteins were aligned with MAFFT 35 (LINSI option) and a phylogenetic tree was constructed from the resulting alignment with FastTree [-wag -gamma options] 36 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, MAFFT, SAMtools, featureCounts] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX v1.21.2] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, BLAST, HMMER, R v4.4.0]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Version used: **7.505**
- Evidence: For all ten conserved orthologues or gametologues, we: (1) used blastn (BLAST+ v.2.14.1) and bedtools (v.2.31.0) getfasta, to find and extract nucleotide sequences for full-length genes (including introns); (2) aligned each gene matrix with MAFFT (v.7.505), using the options ‘--localpair --maxiterate 1000’; and (3) inferred maximum-likelihood trees with IQ-TREE (v.1.6.12) with the options ‘-MFP -b...
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Evidence: Sequence divergence Sequence divergence for BUSCO genes was calculated from the MAFFT alignment (described below) in R, with the function ‘dist.dna’ from the ape package 60 .
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Deep origin of eukaryotes outside Heimdallarchaeia within Asgardarchaeota. (Nature 2025)

- DOI: 10.1038/s41586-025-08955-7 | PMCID: PMC12222021 | PMID: 40335687
- Evidence: The marker sequences were aligned with MAFFT 68 (v.7.487, -linsi) and pruned using BMGE 69 (v.1.12) (-m BLOSUM30).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [MAFFT] -> stage not stated [Bowtie2, HMMER, IQ-TREE, SAMtools, SPAdes]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Version used: **7.475**
- Evidence: Relevant A. thaliana orthologous genes containing the required domains were retrieved from TAIR ( https://www.arabidopsis.org ), and profile hidden Markov models (HMMs) were constructed using HMMER (v.3.1b1) on the basis of multiple sequence alignments generated by MAFFT (v.7.475).
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: Individual reads mapped to the reference (G1 NA12889 Y assembly) and covering the indel call plus 150 bp of flanking sequence were extracted from all samples using subseq ( https://github.com/EichlerLab/subseq ), followed by alignment using MAFFT 110 , 111 (v.7.508) with the default parameters.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: We adopted the strategy of extracting one CentO repeat unit at every fiftieth interval on each chromosome to select some CentO repeats for a subsequent similarity comparison across genomes using MAFFT 95 (v.7.490).
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Structure of the ATP-driven methyl-coenzyme M reductase activation complex. (Nature 2025)

- DOI: 10.1038/s41586-025-08890-7 | PMCID: PMC12176620 | PMID: 40240609
- Evidence: Phylogenetic analysis Sequences for McrC, Mmp7, CfbD and the Nif reductases family were collected from the National Center for Biotechnology Information BLASTP and aligned using Multiple Alignment using Fast Fourier Transform (MAFFT) 68 .
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [Coot v0.9.8.92, PHENIX v1.21] -> machine learning [Topaz] -> visualisation [ChimeraX v1.6.1] -> stage not stated [AlphaFold, IQ-TREE, UCSF Chimera v1.17.3]

### Ancient DNA from the Green Sahara reveals ancestral North African lineage. (Nature 2025)

- DOI: 10.1038/s41586-025-08793-7 | PMCID: PMC12043513 | PMID: 40175549
- Evidence: The BEAST analysis of mitochondrial genomes involved 216 mtDNA sequences, aligned using MAFFT 83 v.7.508 and adjusted by removing specific poly-C regions.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, MAFFT] -> variant calling [SAMtools v1.3] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> stage not stated [PLINK, tidyverse v1.3.0]

### Solanum pan-genetics reveals paralogues as contingencies in crop engineering. (Nature 2025)

- DOI: 10.1038/s41586-025-08619-6 | PMCID: PMC11964936 | PMID: 40044854
- Evidence: MAFFT 94 was used to align each locus individually.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.5c] -> alignment/mapping [BUSCO, MAFFT, Python, STAR v2.7.5c, minimap2 v2.17] -> quantification [STAR v2.7.5c] -> stage not stated [OrthoFinder, R, ggplot2, hifiasm, tidyverse]

### Expanding the human gut microbiome atlas of Africa. (Nature 2025)

- DOI: 10.1038/s41586-024-08485-8 | PMCID: PMC11839480 | PMID: 39880958
- Version used: **7.407**
- Evidence: 104 ) and MAFFT v.7.407 (ref.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [BWA v0.7.17] -> quantification [lme4] -> differential/statistical testing [lme4] -> stage not stated [MAFFT v7.407, QUAST v5.2.0, R, ggplot2 v3.4.2, pheatmap v1.0.12, tidyverse v2.0.0, vegan v2.6]

### Learning the fitness dynamics of pathogens from phylogenies. (Nature 2025)

- DOI: 10.1038/s41586-024-08309-9 | PMCID: PMC11735385 | PMID: 39743587
- Evidence: For H3N2, we aligned all HA sequences using MAFFT 42 (v.7.309) with default settings.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BWA, GATK, MAFFT] -> structure determination [BEAST v1.10.4] -> stage not stated [Stan]

### Centrophilic retrotransposon integration via CENH3 chromatin in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-024-08319-7 | PMCID: PMC11735389 | PMID: 39743586
- Version used: **7.453**
- Evidence: For ALE , we aligned the concatenated integrase and reverse transcriptase hidden Markov model domains retrieved from TEsorter for ALE with MAFFT (v.7.453, --globalpair --maxiterate 1,000) 72 .
- Full pipeline: read trimming [Cutadapt v4.4, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.5.3, MAFFT v7.453, MUSCLE v3.8.1551, Picard, SAMtools v1.9, Trimmomatic v0.39, minimap2 v2.15] -> visualisation [ggplot2 v3.4.4, tidyverse v1.1.4] -> stage not stated [BEDTools v2.31.1]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Evidence: Then, per transposase variant, a multiple sequence alignment was generated for the set of deduplicated flanks with MAFFT 61 (v.7.526).
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Version used: **7.526**
- Evidence: We extracted the nucleotide sequences of 13 mitochondrial protein-coding genes and aligned sequences using MAFFT (v7.526) 51 with default parameters.
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### Heart-nosed bat alphacoronaviruses use human CEACAM6 to enter cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10394-x | PMCID: PMC13149331 | PMID: 42020746
- Version used: **7.526**
- Evidence: We constructed the spike protein-coding DNA sequence alignment using MAFFT (v.7.526) 49 , 50 by integrating structural alignments of homologous spike protein structures queried from the UniProt Reference Clusters 51 .
- Full pipeline: alignment/mapping [BEAST v1.10.5, MAFFT v7.526] -> quantification [statsmodels] -> dimensionality reduction/clustering [MAFFT v7.526] -> structure determination [BEAST v1.10.5, IQ-TREE v2.3.4] -> stage not stated [AlphaFold, ChimeraX, ColabFold, PyMOL, QGIS, R v4.4.1, Seurat v5.3.0]

### EBV strain interacts with host HLA to drive nasopharyngeal carcinoma risk. (Nature 2026)

- DOI: 10.1038/s41586-026-10416-8 | PMCID: PMC13190245 | PMID: 41986726
- Version used: **7.490**
- Evidence: Multiple sequence alignment was performed using MAFFT (v7.490) 104 with the ‘–keeplength’ parameter to preserve the original length of the reference genome (171,823 bp) and establish homologous alignment.
- Full pipeline: quality control [PLINK v1.9] -> read trimming [fastp] -> alignment/mapping [MAFFT v7.490, VCFtools v0.1.13] -> variant calling [PLINK v1.9] -> stage not stated [AlphaFold, GATK, GEMMA, IQ-TREE, Picard v2.18.14, PyMOL v3.1.6.1, R]

### Dogs were widely distributed across western Eurasia during the Palaeolithic. (Nature 2026)

- DOI: 10.1038/s41586-026-10170-x | PMCID: PMC13017512 | PMID: 41882128
- Version used: **7.505**
- Evidence: Mitochondrial DNA analysis Majority consensus (75%) mitochondrial genomes were called for all ancient samples, and those with sufficient coverage (over 2×) were aligned with 220 publicly available ancient and modern canid mitogenomes (Supplementary Table 5 ) using MAFFT v.7.505 (ref.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.4, MAFFT v7.505] -> differential/statistical testing [BEAST v2.6.7] -> stage not stated [ADMIXTURE v1.3.0]

### Natural maternal immunity protects neonates from Escherichia coli sepsis. (Nature 2026)

- DOI: 10.1038/s41586-026-10225-z | PMCID: PMC13108393 | PMID: 41813901
- Version used: **7.526**
- Evidence: Multiple sequence alignment was performed using MAFFT (v.7.526) with the autoalignment function enabled 93 .
- Full pipeline: quality control [FastQC v0.12.1, NanoPlot v1.46.0] -> alignment/mapping [MAFFT v7.526, QUAST v5.2.0.2] -> stage not stated [Python, SPAdes]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Version used: **7.150b**
- Evidence: Sa. ludwigii LTRs were first aligned using the program MAFFT (v.7.150b) 84 .
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### Transmission of MPXV from fire-footed rope squirrels to sooty mangabeys. (Nature 2026)

- DOI: 10.1038/s41586-025-10086-y | PMCID: PMC12960232 | PMID: 41673146
- Version used: **7.505n**
- Evidence: This dataset plus one representative MPXV genome per species from the TNP 2022/2023 outbreak ( n = 28) were aligned using MAFFT v.7.505n 49 .
- Full pipeline: read trimming [BWA, Flye v2.9.2, SPAdes v3.13.0] -> alignment/mapping [BWA, IQ-TREE v2.1.4b, MAFFT v7.505n, Picard v2.13.3] -> structure determination [IQ-TREE v2.1.4b] -> stage not stated [BEAST v1.10.5, Nextstrain v3.12.036, minimap2 v2.17]

### Bacterial immune activation via supramolecular assembly with phage triggers. (Nature 2026)

- DOI: 10.1038/s41586-025-10060-8 | PMCID: PMC13017515 | PMID: 41639456
- Evidence: Homologues ( n = 150) were used to generate the multiple sequence alignment by MAFFT.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, Cutadapt v1.15] -> alignment/mapping [Bowtie2 v2.3.4.1, Cutadapt v1.15, MAFFT, NumPy, SAMtools v1.7] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> machine learning [Topaz]

### A prophage-encoded abortive infection protein preserves host and prophage spread. (Nature 2026)

- DOI: 10.1038/s41586-025-10070-6 | PMCID: PMC13043305 | PMID: 41606329
- Evidence: Hits from each round were aligned using MAFFT 63 (automatic strategy selection).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT] -> structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BEDTools v2.27.1, PHENIX, SAMtools v1.1]

### An ancient DNA perspective on the Russian conquest of Yakutia. (Nature 2026)

- DOI: 10.1038/s41586-025-09856-5 | PMCID: PMC12893923 | PMID: 41501450
- Evidence: The multi-FASTA sequence data, corresponding to the 45 modern viral genome, including the reference genome, were further aligned using MAFFT 102 and manually corrected wherever appropriate.
- Full pipeline: alignment/mapping [Bowtie2, IQ-TREE v1.6.12, MAFFT] -> variant calling [ANGSD v0.930, BCFtools v1.17] -> registration [GATK, Picard] -> differential/statistical testing [vegan] -> structure determination [IQ-TREE v1.6.12] -> stage not stated [ADMIXTURE v1.3.0, HUMAnN v3.0, MetaPhlAn, SHAPEIT]

### The Microflora Danica atlas of Danish environmental microbiomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09794-2 | PMCID: PMC12823411 | PMID: 41339548
- Evidence: Multiple-sequence alignment of protein sequences was performed with MAFFT 150 v.7.490.
- Full pipeline: read trimming [Cutadapt, fastp] -> alignment/mapping [Flye, HMMER, MAFFT, minimap2] -> stage not stated [DADA2, IQ-TREE, SAMtools, data.table, ggpubr, tidyverse]

### Dated gene duplications elucidate the evolutionary assembly of eukaryotes. (Nature 2026)

- DOI: 10.1038/s41586-025-09808-z | PMCID: PMC12872463 | PMID: 41339551
- Version used: **7.508**
- Evidence: Identifying candidate gene families Candidate pre-LECA duplications were identified with the domain origins (DO) pipeline, which consists of the following steps: sequence retrieval (HMMER, v.3.3.2 76 ), filtering and aligning (MAFFT, v.7.508 77 ) these sequences, building new HMMs for iterating this search, clustering the results (MCL, v.22-282 78 ), selecting representatives to produce a represen...
- Full pipeline: alignment/mapping [HMMER v3.3.2, MAFFT v7.508] -> dimensionality reduction/clustering [HMMER v3.3.2, MAFFT v7.508] -> visualisation [Matplotlib, seaborn]

### Progressive coevolution of the yeast centromere and kinetochore. (Nature 2026)

- DOI: 10.1038/s41586-025-09779-1 | PMCID: PMC12925627 | PMID: 41299172
- Version used: **7.505**
- Evidence: Constructing gene trees, removing outliers and reconstructing and dating the species tree For each of the 1,270 sets of homologues, we used MAFFT (v.7.505) 59 with the E-INS-i option to align sequences, trimAl v.1.4.rev15 build[2013-12-17] 60 with the -gappyout option to remove phylogenetically noisy positions and FastTree v.2.1.11 Double precision (No SSE3) 61 with options -spr 4 -mlacc 2 -slownn...
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.505] -> structure determination [MAFFT v7.505] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5.5, IQ-TREE, NumPy, Python]

### Semantic design of functional de novo genes from a genomic language model. (Nature 2026)

- DOI: 10.1038/s41586-025-09749-7 | PMCID: PMC12804078 | PMID: 41261132
- Version used: **7.526**
- Evidence: Following identification of ORFs in generated sequences using Prodigal (v2.6.3, default parameters, -p meta) with default parameters in metagenome mode (-p meta) 66 , generated proteins were aligned against the full-length prompt protein sequence using MAFFT (v7.526) 67 for sequence identity calculations.
- Full pipeline: alignment/mapping [MAFFT v7.526] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [igraph v0.11.6] -> visualisation [ChimeraX, Matplotlib] -> stage not stated [AlphaFold, BLAST, HMMER v3.3.0, Python v3.11.8, SciPy v1.11.4]

### Convergent genome evolution shaped the emergence of terrestrial animals. (Nature 2026)

- DOI: 10.1038/s41586-025-09722-4 | PMCID: PMC12804077 | PMID: 41225002
- Version used: **7.505**
- Evidence: 67 ), using dependencies of MAFFT v.7.505 (ref.
- Full pipeline: stage not stated [BLAST v2.14.0, BUSCO v5.4.7, IQ-TREE v2.2.2.6, MAFFT v7.505, OrthoFinder, R, ggplot2, phytools, vegan]

### Ecology and spread of the North American H5N1 epizootic. (Nature 2026)

- DOI: 10.1038/s41586-025-09737-x | PMCID: PMC12779553 | PMID: 41225000
- Version used: **7.5.20**
- Evidence: We first aligned sequences using MAFFT v.7.5.20, sequence alignments were visually inspected using Geneious and sequences causing significant gaps were removed and nucleotides before the start codon and after the stop codon were removed 70 , 71 .
- Full pipeline: alignment/mapping [MAFFT v7.5.20] -> differential/statistical testing [BEAST v1.10.4] -> structure determination [BEAST v1.10.4] -> stage not stated [Nextstrain]

### LinearTurboFold: Linear-time global prediction of conserved structures for RNA homologs with applications to SARS-CoV-2. (PNAS 2021)

- DOI: 10.1073/pnas.2116269118 | PMCID: PMC8719904 | PMID: 34887342
- Evidence: As negative controls, LinearPartition and Vienna RNAfold predicted structures for each sequence separately; LinearAlignment and MAFFT generated sequence-level alignments; RNAalifold folded prealigned sequences (e.g., from MAFFT) and predicted conserved structures.
- Full pipeline: alignment/mapping [MAFFT] -> registration [MAFFT]

### Structure-function analysis of the nsp14 N7-guanine methyltransferase reveals an essential role in <i>Betacoronavirus</i> replication. (PNAS 2021)

- DOI: 10.1073/pnas.2108709118 | PMCID: PMC8670481 | PMID: 34845015
- Evidence: A total of 47 CoV nsp14 sequences were retrieved (a complete list is provided in SI Appendix , Table S1 ) and aligned using MAFFT.
- Full pipeline: alignment/mapping [MAFFT] -> visualisation [UCSF Chimera]

### Evolutionary history and pan-genome dynamics of strawberry (<i>Fragaria</i> spp.). (PNAS 2021)

- DOI: 10.1073/pnas.2105431118 | PMCID: PMC8609306 | PMID: 34697247
- Evidence: Orthogroups where at least 94.4% of the species had single-copy genes in an orthogroup were selected and sequences aligned by MAFFT ( 77 ).
- Full pipeline: alignment/mapping [ANNOVAR, MAFFT, SAMtools] -> variant calling [GATK] -> dimensionality reduction/clustering [GCTA] -> stage not stated [ADMIXTURE, BUSCO, HMMER, IQ-TREE, InterProScan, PLINK, Pilon v1.22, R, RAxML, RepeatMasker]

### Distant residues modulate conformational opening in SARS-CoV-2 spike protein. (PNAS 2021)

- DOI: 10.1073/pnas.2100943118 | PMCID: PMC8639331 | PMID: 34615730
- Evidence: Iterative sequence alignment of the 67 strains of SARS-CoV-2 spike protein sequences from the PDB database was performed using the Multiple Alignment using Fast Fourier Transform with Database of Aligned Structural Homologs (MAFFT-DASH) program ( 83 ) using the G-INS-i algorithm.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [UCSF Chimera]

### Elucidation of an anaerobic pathway for metabolism of l-carnitine-derived γ-butyrobetaine to trimethylamine in human gut bacteria. (PNAS 2021)

- DOI: 10.1073/pnas.2101498118 | PMCID: PMC8364193 | PMID: 34362844
- Version used: **7.455**
- Evidence: A multiple sequence alignment was generated using MAFFT v7.455 ( 64 ) of the BbuA homolog protein sequences and 2,388 representatives of protein clusters with >80% amino acid sequence identity from the top 10,000 hits of a BLAST search of the UniProt database (release 2019_07) using the E. timonensis SN18 BbuA protein as a query.
- Full pipeline: alignment/mapping [MAFFT v7.455] -> dimensionality reduction/clustering [MAFFT v7.455] -> differential/statistical testing [R v3.6, ggplot2] -> visualisation [IQ-TREE v1.6.12] -> stage not stated [Prokka]

### A squalene-hopene cyclase in <i>Schizosaccharomyces japonicus</i> represents a eukaryotic adaptation to sterol-limited anaerobic environments. (PNAS 2021)

- DOI: 10.1073/pnas.2105225118 | PMCID: PMC8364164 | PMID: 34353908
- Version used: **7.402**
- Evidence: A total number of 128 selected sequences ( SI Appendix , Table S4 and Dataset S6 ) were subjected to multiple sequence alignment using MAFFT version 7.402 ( 91 ) in “einsi” mode.
- Full pipeline: read trimming [RAxML v0.8.1] -> alignment/mapping [HMMER, MAFFT v7.402, RAxML v0.8.1] -> stage not stated [Flye v2.7.1, Pilon v1.18]

### Ongoing global and regional adaptive evolution of SARS-CoV-2. (PNAS 2021)

- DOI: 10.1073/pnas.2104241118 | PMCID: PMC8307621 | PMID: 34292871
- Evidence: The alignment was constructed using a multithreaded compilation of the Multiple Alignment using Fast Fourier Transform (MAFFT) software ( 81 ), and sites corresponding to protein-coding ORFs were mapped to the alignment from the reference sequence NC_045512.2 excluding stop codons.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE]

### Connecting structure and function from organisms to molecules in small-animal symbioses through chemo-histo-tomography. (PNAS 2021)

- DOI: 10.1073/pnas.2023773118 | PMCID: PMC8300811 | PMID: 34183413
- Version used: **7.394**
- Evidence: The sequences were aligned using MAFFT v7.394 ( 66 ) in G-Insi mode.
- Full pipeline: alignment/mapping [MAFFT v7.394] -> stage not stated [scikit-image]

### Systematic mining of fungal chimeric terpene synthases using an efficient precursor-providing yeast chassis. (PNAS 2021)

- DOI: 10.1073/pnas.2023247118 | PMCID: PMC8307374 | PMID: 34257153
- Evidence: Multiple sequence alignments were produced in MAFFT using a highly accurate setting (L-INS-i) and 1,000 iterations of improvement.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [HMMER]

### Fifty million years of beetle evolution along the Antarctic Polar Front. (PNAS 2021)

- DOI: 10.1073/pnas.2017384118 | PMCID: PMC8214695 | PMID: 34108239
- Evidence: Multiple sequence alignments (MSA) were then undertaken for each gene using the L-INS-i option (an iterative refinement method) in MAFFT (Multiple Alignment using Fast Fourier Transform) v.7.130b ( 80 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Clustal Omega, MAFFT] -> dimensionality reduction/clustering [R, RAxML] -> differential/statistical testing [MrBayes v3.2.6] -> structure determination [MAFFT] -> stage not stated [BEAST v2.5]

### The ORF8 protein of SARS-CoV-2 mediates immune evasion through down-regulating MHC-Ι. (PNAS 2021)

- DOI: 10.1073/pnas.2024202118 | PMCID: PMC8201919 | PMID: 34021074
- Evidence: The sequence alignment of complete genome sequences was performed using MAFFT software with default parameters ( 54 ).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT]

### Phenotypic and genetic characterization of MERS coronaviruses from Africa to understand their zoonotic potential. (PNAS 2021)

- DOI: 10.1073/pnas.2103984118 | PMCID: PMC8237650 | PMID: 34099577
- Evidence: Representative and complete MERS-CoV genome sequences from predesignated clades (A, B, and C) were downloaded from GenBank and aligned by MAFFT.
- Full pipeline: alignment/mapping [MAFFT]

### Anaerobic gut fungi are an untapped reservoir of natural products. (PNAS 2021)

- DOI: 10.1073/pnas.2019855118 | PMCID: PMC8106346 | PMID: 33906945
- Evidence: Sequences were aligned using MAFFT (Multiple Alignment using Fast Fourier Transform) ( 70 ) with subsequent removal of nonreliable aligned positions using trimAl ( 71 ).
- Full pipeline: alignment/mapping [AUGUSTUS, MAFFT] -> dimensionality reduction/clustering [BLAST] -> visualisation [Cytoscape] -> stage not stated [OrthoFinder, RAxML]

### The diversity of stomatal development regulation in <i>Callitriche</i> is related to the intrageneric diversity in lifestyles. (PNAS 2021)

- DOI: 10.1073/pnas.2026351118 | PMCID: PMC8040647 | PMID: 33782136
- Version used: **7.453**
- Evidence: The sequences retrieved were aligned using MAFFT v7.453 ( 55 ).
- Full pipeline: read trimming [RAxML v8.2.12] -> alignment/mapping [MAFFT v7.453] -> stage not stated [BLAST]

### Predicting transcriptional responses to cold stress across plant species. (PNAS 2021)

- DOI: 10.1073/pnas.2026330118 | PMCID: PMC7958178 | PMID: 33658387
- Version used: **7.149**
- Evidence: Multiple sequence alignments for the annotated CDSs for all seven genes within a group were generated by using MAFFT (v7.149) with the parameter setting L-INS-i ( 59 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [HTSeq v0.6.1, MAFFT v7.149, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [BEAST v5.1, DESeq2] -> simulation/modelling [BEAST v5.1] -> stage not stated [R]

### The cyanobacterium <i>Prochlorococcus</i> has divergent light-harvesting antennae and may have evolved in a low-oxygen ocean. (PNAS 2021)

- DOI: 10.1073/pnas.2025638118 | PMCID: PMC7980375 | PMID: 33707213
- Evidence: Predicted amino acid sequences were aligned using MAFFT ( 51 ) version 7.271.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, IQ-TREE, SPAdes v3.5]

### Diel transcriptional oscillations of light-sensitive regulatory elements in open-ocean eukaryotic plankton communities. (PNAS 2021)

- DOI: 10.1073/pnas.2011038118 | PMCID: PMC8017926 | PMID: 33547239
- Evidence: Cryptochrome/photolyase, phytochrome, rhodopsin, and LOV protein sequences described in the literature ( 32 , 57 , 71 , 72 , 109 ) were aligned with Multiple Alignment using Fast Fourier Transform (MAFFT) version 7.313 (parameters: –localpair–maxiterate 100–reorder–leavegappyregion) ( 110 ) and used to generate hmm-profiles ( Dataset S2 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R] -> stage not stated [HMMER v3.1b, RAxML v8.2.8]

### A modern scleractinian coral with a two-component calcite-aragonite skeleton. (PNAS 2021)

- DOI: 10.1073/pnas.2013316117 | PMCID: PMC7826372 | PMID: 33323482
- Evidence: The P. antarcticus mitogenome was aligned using MAFFT version 7 ( 58 ) to 57 other scleractinians and 12 corallimorpharians previously published mitogenomes, of which corallimorpharians were used as the outgroup ( SI Appendix , Table S2 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [MrBayes] -> stage not stated [BEAST, RAxML]

### The squalene route to C30 carotenoid biosynthesis and the origins of carotenoid biosynthetic pathways. (PNAS 2022)

- DOI: 10.1073/pnas.2210081119 | PMCID: PMC9907078 | PMID: 36534808
- Evidence: We combined the resulting target sequences (~14,000) into a single dataset, aligned them using MAFFT ( 50 ), and trimmed gap positions using trimAL (–gt 0.2) ( 51 ) and some other non-informative regions manually.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [IQ-TREE, MAFFT] -> structure determination [IQ-TREE] -> stage not stated [BLAST]

### Genomic diversification of the specialized parasite of the fungus-growing ant symbiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2213096119 | PMCID: PMC9907069 | PMID: 36508678
- Version used: **7.475**
- Evidence: Sequences were aligned individually using MAFFT v7.475 ( 85 , 86 ) with default parameters, then trimmed using trimAL v1.2rev59 ( 87 ) with the “-automated1” flag.
- Full pipeline: read trimming [MAFFT v7.475, fastp] -> alignment/mapping [MAFFT v7.475] -> visualisation [Cytoscape v3.8.0] -> stage not stated [BUSCO, IQ-TREE, InterProScan, OrthoFinder, R, RepeatMasker, SPAdes v3.11.1, ggplot2, pheatmap, tidyverse]

### Transposable elements drive intron gain in diverse eukaryotes. (PNAS 2022)

- DOI: 10.1073/pnas.2209766119 | PMCID: PMC9860276 | PMID: 36417430
- Evidence: We employed multiple alignment using fast Fourier transform (MAFFT) ( 44 ) to conduct multiple sequence alignments for each Introner family in each species.
- Full pipeline: alignment/mapping [MAFFT, SAMtools] -> differential/statistical testing [R, lme4] -> stage not stated [Python, RepeatMasker, phytools]

### Reactive granulopoiesis depends on T-cell production of IL-17A and neutropenia-associated alteration of gut microbiota. (PNAS 2022)

- DOI: 10.1073/pnas.2211230119 | PMCID: PMC9860329 | PMID: 36409919
- Evidence: Then, the phylogenic tree was created by FastTree ( 62 ) after alignment with MAFFT ( 63 ).
- Full pipeline: read trimming [QIIME 2] -> alignment/mapping [MAFFT] -> stage not stated [DADA2]

### Tissue-specific regulation of lipid polyester synthesis genes controlling oxygen permeation into <i>Lotus japonicus</i> nodules. (PNAS 2022)

- DOI: 10.1073/pnas.2206291119 | PMCID: PMC9704718 | PMID: 36375074
- Evidence: The protein alignment was done in MAFFT using default settings ( 63 ) and nonconserved regions were removed by manually trimming gaps in the alignment.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> quantification [ImageJ] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, R] -> stage not stated [RAxML, ggpubr v0.4.0.999, pheatmap]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Version used: **7.407**
- Evidence: The sequences of each locus were then aligned with MAFFT v7.407 ( 93 ) with the option –adjustdirection and visually inspected to confirm the presence of a target site duplication when possible.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Coevolution of tandemly repeated <i>hlips</i> and RpaB-like transcriptional factor confers desiccation tolerance to subaerial <i>Nostoc</i> species. (PNAS 2022)

- DOI: 10.1073/pnas.2211244119 | PMCID: PMC9586280 | PMID: 36215485
- Evidence: For the phylogenetic analysis, the Hrf1 sequences from representative species were aligned using the MAFFT multiple alignment program and the maximum-likelihood phylogenetic tree was generated by RAxML v8.1.20 under the PROTGAMMA model with 1,000 bootstrap replicates ( 71 , 72 ).
- Full pipeline: alignment/mapping [MAFFT, RAxML v8.1.20]

### Substitutions near the HA receptor binding site explain the origin and major antigenic change of the B/Victoria and B/Yamagata lineages. (PNAS 2022)

- DOI: 10.1073/pnas.2211616119 | PMCID: PMC9586307 | PMID: 36215486
- Evidence: Nucleotide sequences were aligned with MAFFT version 7, and indels were inspected manually.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [R]

### Leveraging orthology within maize and Arabidopsis QTL to identify genes affecting natural variation in gravitropism. (PNAS 2022)

- DOI: 10.1073/pnas.2212199119 | PMCID: PMC9546580 | PMID: 36161933
- Evidence: Finally, the multiple alignment between the DNA sequences of the three accessions was carried out with MAFFT version 7 ( 55 ) and visualized with benchling ( https://benchling.com ).
- Full pipeline: alignment/mapping [MAFFT] -> visualisation [MAFFT] -> stage not stated [BEDTools, BLAST]

### Extracellular carbonic anhydrase activity promotes a carbon concentration mechanism in metazoan calcifying cells. (PNAS 2022)

- DOI: 10.1073/pnas.2203904119 | PMCID: PMC9546546 | PMID: 36161891
- Evidence: ...fgenomics ( http://reefgenomics.org ) databases, and aligned and compared with the sequenced sequences from the sea urchin larvae via the online tool MAFFT (Multiple Alignment using Fast Fourier Transform) ( https://www.ebi.ac.uk/Tools/msa/mafft/ ).
- Full pipeline: read trimming [MUSCLE] -> alignment/mapping [MAFFT, MUSCLE]

### Using phylogenetics to infer HIV-1 transmission direction between known transmission pairs. (PNAS 2022)

- DOI: 10.1073/pnas.2210604119 | PMCID: PMC9499565 | PMID: 36103580
- Evidence: For each pair, we built multiple sequence alignments using MAFFT ( 18 ) and removed the columns from the alignment where gaps were found in greater than 25% of sequences.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [R]

### Convergent evolution of a genotoxic stress response in a parasite-specific p53 homolog. (PNAS 2022)

- DOI: 10.1073/pnas.2205201119 | PMCID: PMC9478680 | PMID: 36067283
- Evidence: Phylogenetic trees were generated from p53 protein sequences by first using the FastME/OneClick Workflow function at NGPhylogeny.fr ( 38 ) to perform multiple sequence alignment with Multiple Alignment using Fast Fourier Transform (MAFFT) (auto flavor, gap extend penalty = 0.123, gap opening penalty = 1.53) and alignment trimming with Block Mapping and Gathering with Entropy (BMGE) (estimated matr...
- Full pipeline: read trimming [MAFFT, RAxML] -> alignment/mapping [MAFFT]

### Signatures of adaptive evolution in platyrrhine primate genomes. (PNAS 2022)

- DOI: 10.1073/pnas.2116681119 | PMCID: PMC9436310 | PMID: 35994669
- Evidence: ...sence of at least one capuchin lineage; 2) aligning CDS sequences for these filtered orthologs groups by codon using Guidance2 v.2.02 ( 58 ) with the MAFFT aligner v.7.419 ( 122 ) with 100 guidance bootstraps; and 3) visually inspecting all alignments for errors and editing as required to reduce the likelihood of false positives.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BUSCO v3.0.2, RepeatMasker v4.0.7]

### Correlations between alignment gaps and nucleotide substitution or amino acid replacement. (PNAS 2022)

- DOI: 10.1073/pnas.2204435119 | PMCID: PMC9407537 | PMID: 35972964
- Version used: **7.475**
- Evidence: We examined the test behavior using optimal alignments from Clustal Omega (version 1.2.2) ( 16 ), MAFFT (version 7.475) ( 17 ), Muscle (version 3.8.31) ( 18 ), and Prank (version 170427) ( 19 ).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2, MAFFT v7.475]

### Two mutations in the ORF1 of genotype 1 hepatitis E virus enhance virus replication and may associate with fulminant hepatic failure. (PNAS 2022)

- DOI: 10.1073/pnas.2207503119 | PMCID: PMC9407470 | PMID: 35969750
- Evidence: Genomic sequences from each genotype were aligned using the MAFFT algorithm in Geneious Prime software version 2022.1.1.
- Full pipeline: alignment/mapping [MAFFT] -> variant calling [MAFFT]

### Radiation and hybridization underpin the spread of the fire ant social supergene. (PNAS 2022)

- DOI: 10.1073/pnas.2201040119 | PMCID: PMC9407637 | PMID: 35969752
- Version used: **7.475**
- Evidence: Then, we aligned the circularized sequences using MARS and MAFFT (v.7.475) ( 98 , 99 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.475, R, ggplot2] -> variant calling [BCFtools, freebayes v1.3.2] -> normalisation [VCFtools v0.1.16] -> visualisation [ape (R)] -> stage not stated [IQ-TREE, SAMtools, phytools]

### Molecular determinants of pH sensing in the proton-activated chloride channel. (PNAS 2022)

- DOI: 10.1073/pnas.2200727119 | PMCID: PMC9351481 | PMID: 35878032
- Evidence: PAC N-terminal sequence alignment was created using MAFFT software v7.427 (2019 March 29) ( 30 ).
- Full pipeline: alignment/mapping [MAFFT] -> simulation/modelling [OpenMM v7.5.0]

### Uncovering the enigmatic evolution of bears in greater depth: The hybrid origin of the Asiatic black bear. (PNAS 2022)

- DOI: 10.1073/pnas.2120307119 | PMCID: PMC9351369 | PMID: 35858381
- Version used: **7.486**
- Evidence: Based on BAM files, the consensus mt genomes and Y chromosome sequences were filtered using the mpileup module of SAMtools ( 45 ) and aligned using MAFFT version 7.486 ( 49 ).
- Full pipeline: read trimming [BWA v0.78] -> alignment/mapping [BWA v0.78, MAFFT v7.486, SAMtools v0.1.18] -> registration [GATK v3.7] -> structure determination [RAxML v8.2.11] -> stage not stated [Picard v1.87, VCFtools v0.1.14]

### The Hippo pathway regulates axis formation and morphogenesis in &lt;i&gt;Hydra&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2203257119 | PMCID: PMC9304002 | PMID: 35858299
- Evidence: For generation of the phylogenetic tree, the sequences were aligned using MAFFT (Multiple Alignment using Fast Fourier Transform) ( https://www.ebi.ac.uk/Tools/msa/mafft/ ) or Clustal Omega ( https://www.ebi.ac.uk/Tools/msa/clustalo/ ) and analyzed using Akaike Information Criterion ( www.atgc-montpellier.fr ).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT]

### Posttranslational modifications optimize the ability of SARS-CoV-2 spike for effective interaction with host cell receptors. (PNAS 2022)

- DOI: 10.1073/pnas.2119761119 | PMCID: PMC9282386 | PMID: 35737823
- Evidence: Multiple sequence alignment was carried out using the Multiple Alignment using Fast Fourier Transform (MAFFT) program ( 90 ) and visualized using Jalview ( 91 ).
- Full pipeline: alignment/mapping [MAFFT] -> simulation/modelling [NAMD, VMD] -> visualisation [MAFFT]

### Anti-bat ultrasound production in moths is globally and phylogenetically widespread. (PNAS 2022)

- DOI: 10.1073/pnas.2117485119 | PMCID: PMC9231501 | PMID: 35704762
- Evidence: Sequences for the six genes were aligned in MAFFT ( 72 ), then manually trimmed and concatenated in GENEIOUS version (v).11.1.5.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, R] -> dimensionality reduction/clustering [UMAP] -> structure determination [R] -> stage not stated [IQ-TREE v1.6.2, scikit-learn]

### Denitrification in foraminifera has an ancient origin and is complemented by associated bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2200198119 | PMCID: PMC9231491 | PMID: 35704763
- Evidence: Multiple sequence alignments used in the current study were obtained in MAFFT ( 79 ) (ver.
- Full pipeline: quality control [FastQC v0.11.5] -> read trimming [Trimmomatic] -> alignment/mapping [MAFFT, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE] -> stage not stated [BLAST, BUSCO, SPAdes]

### Retrotransposition facilitated the establishment of a primary plastid in the thecate amoeba <i>Paulinella</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121241119 | PMCID: PMC9191642 | PMID: 35639693
- Version used: **7.453**
- Evidence: The combined set of all HLI/Hli sequences was aligned using MAFFT (v7.453; --localpair --maxiterate 1000), and a maximum-likelihood phylogenetic tree was inferred using IQ-TREE (v1.6.12; -m MFP -bb 2000 -alrt 2000 -bnni) ( 54 ), allowing the program to choose the best evolutionary model for the alignment ( 55 ).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, SAMtools, Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, IQ-TREE v1.6.12, MAFFT v7.453, SAMtools, minimap2 v2.17] -> quantification [RSEM v1.3.3] -> normalisation [DESeq2 v1.30.1] -> stage not stated [BEDTools, BLAST]

### Co-component signal transduction systems: Fast-evolving virulence regulation cassettes discovered in enteric bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2203176119 | PMCID: PMC9214523 | PMID: 35648808
- Evidence: Identified sequences were submitted to the MAFFT server ( 67 ) to generate multiple sequence alignments with the default strategy.
- Full pipeline: alignment/mapping [MAFFT, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, HMMER]

### Human pathogenic RNA viruses establish noncompeting lineages by occupying independent niches. (PNAS 2022)

- DOI: 10.1073/pnas.2121335119 | PMCID: PMC9191635 | PMID: 35639694
- Evidence: In all cases, sequences were harmonized to DNA (e.g., U was transformed to T to amend software compatibility) and aligned with MAFFT ( 26 ), using default settings.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE]

### Ancient proteins resolve controversy over the identity of <i>Genyornis</i> eggshell. (PNAS 2022)

- DOI: 10.1073/pnas.2109326119 | PMCID: PMC9995833 | PMID: 35609205
- Evidence: Masked sequences were aligned using MAFFT l-ins-i v7.453 ( 110 , 111 ), and trailing ends at the beginning and the end of the alignment were trimmed manually (alignments are available on FigShare [10.6084/m9.figshare.15084879]).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, MUSCLE v3.8.31] -> stage not stated [AlphaFold, ColabFold, R v4.1, RAxML v1.0.3, phytools]

### ENPP1's regulation of extracellular cGAMP is a ubiquitous mechanism of attenuating STING signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2119189119 | PMCID: PMC9173814 | PMID: 35588451
- Evidence: Multiple sequence alignment was performed using MAFFT and visualized using Jalview.
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> visualisation [MAFFT]

### Genes and evolutionary fates of the amanitin biosynthesis pathway in poisonous mushrooms. (PNAS 2022)

- DOI: 10.1073/pnas.2201113119 | PMCID: PMC9171917 | PMID: 35533275
- Version used: **7.304b**
- Evidence: The CDSs were aligned by MAFFT v7.304b ( 63 ) with default settings.
- Full pipeline: quality control [FastQC v0.11.3, Trimmomatic v0.32] -> read trimming [FastQC v0.11.3, Trimmomatic v0.32] -> alignment/mapping [MAFFT v7.304b] -> dimensionality reduction/clustering [OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, BUSCO, GATK, Python, RAxML, RepeatMasker, SAMtools, StringTie]

### Origin and early evolution of the plant terpene synthase family. (PNAS 2022)

- DOI: 10.1073/pnas.2100361119 | PMCID: PMC9169658 | PMID: 35394876
- Evidence: Sequences were aligned using MAFFT (einsi) with 1,000 iterations of improvement.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [HMMER v3.0, RAxML]

### Genome-wide CRISPR screen reveals CLPTM1L as a lipid scramblase required for efficient glycosylphosphatidylinositol biosynthesis. (PNAS 2022)

- DOI: 10.1073/pnas.2115083119 | PMCID: PMC9169118 | PMID: 35344438
- Evidence: Protein sequences taken from UniProt were aligned by the MAFFT to generate the tree file and illustrated using iTOL ( 65 , 66 ).
- Full pipeline: alignment/mapping [MAFFT] -> visualisation [PyMOL v2.3]

### The virota and its transkingdom interactions in the healthy infant gut. (PNAS 2022)

- DOI: 10.1073/pnas.2114619119 | PMCID: PMC9060457 | PMID: 35320047
- Evidence: Protein alignments of ORF1 of the Anelloviridae contigs identified in this study and the 108 known RefSeq anelloviruses downloaded from the NCBI (September 2019) were built using MAFFT ( 85 ) and trimmed using trimAl ( 86 ) (gappyout setting).
- Full pipeline: quality control [R] -> read trimming [BWA, MAFFT, Trimmomatic] -> alignment/mapping [BWA, Kraken2, MAFFT] -> quantification [BWA] -> differential/statistical testing [IQ-TREE, ggplot2, phyloseq] -> visualisation [ggplot2, phyloseq] -> stage not stated [BLAST, DADA2, InterProScan, eggNOG]

### Amino acid sensor conserved from bacteria to humans. (PNAS 2022)

- DOI: 10.1073/pnas.2110415119 | PMCID: PMC8915833 | PMID: 35238638
- Evidence: MSAs were built using MAFFT ( 40 ).
- Full pipeline: stage not stated [AlphaFold, AutoDock Vina, HMMER, MAFFT, MrBayes]

### Diverse methylotrophic methanogenic archaea cause high methane emissions from seagrass meadows. (PNAS 2022)

- DOI: 10.1073/pnas.2106628119 | PMCID: PMC8892325 | PMID: 35165204
- Evidence: ( 74 ) comprising classical and divergent McrA protein sequences using the MAFFT alignment program (version 7).
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [MAFFT] -> stage not stated [HMMER, IQ-TREE, QGIS, SPAdes]

### A flavin-dependent monooxygenase produces nitrogenous tomato aroma volatiles using cysteine as a nitrogen source. (PNAS 2022)

- DOI: 10.1073/pnas.2118676119 | PMCID: PMC8851548 | PMID: 35131946
- Evidence: Multiple sequence alignment and homology analysis of the DNA and protein sequences was performed using MAFFT ( 72 ).
- Full pipeline: alignment/mapping [MAFFT]

### Somatostatin-type and allatostatin-C-type neuropeptides are paralogous and have opposing myoregulatory roles in an echinoderm. (PNAS 2022)

- DOI: 10.1073/pnas.2113589119 | PMCID: PMC8851493 | PMID: 35145030
- Evidence: This was accomplished using MAFFT 7 with the iterative refinement method set to L-INS-i and scoring matrix for amino acid sequences set to BLOSUM62, ensuring an optimal alignment.
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [MAFFT] -> stage not stated [ImageJ]

### A peptide toxin in ant venom mimics vertebrate EGF-like hormones to cause long-lasting hypersensitivity in mammals. (PNAS 2022)

- DOI: 10.1073/pnas.2112630119 | PMCID: PMC8851504 | PMID: 35131940
- Version used: **7.304b**
- Evidence: The remaining 313 unique sequences were aligned using local pairwise alignment (L-INS-i) with the regional alignment tool (v0.2) in MAFFT v7.304b ( 33 ).
- Full pipeline: alignment/mapping [MAFFT v7.304b, RSEM] -> quantification [RSEM] -> structure determination [IQ-TREE v2.0.6] -> stage not stated [BLAST]

### Template switching in DNA replication can create and maintain RNA hairpins. (PNAS 2022)

- DOI: 10.1073/pnas.2107005119 | PMCID: PMC8794818 | PMID: 35046021
- Version used: **7.310**
- Evidence: Ancestral Sequence History and Inference of TSMs Sequence clusters were aligned with MAFFT (version 7.310; FFT-NS-I; 1,000 iterations) ( 48 ) and then trimmed with TrimAl ( 49 ) and “automated” mode.
- Full pipeline: read trimming [MAFFT v7.310] -> alignment/mapping [BLAST v2.6.0, MAFFT v7.310] -> dimensionality reduction/clustering [MAFFT v7.310] -> visualisation [R, ggplot2] -> stage not stated [IQ-TREE v1.6.1]

### Acquisition of the arginine deiminase system benefits epiparasitic Saccharibacteria and their host bacteria in a mammalian niche environment. (PNAS 2022)

- DOI: 10.1073/pnas.2114909119 | PMCID: PMC8764695 | PMID: 34992141
- Evidence: A total of 21 single-copy genes were then concatenated, aligned with MAFFT (12,726 aligned amino acids), and used to construct the phylogeny using methods previously described ( 7 ).
- Full pipeline: alignment/mapping [MAFFT, MUSCLE, RAxML v8.2.11] -> visualisation [MUSCLE] -> stage not stated [Python, eggNOG]

### Rapid radiation in a highly diverse marine environment. (PNAS 2022)

- DOI: 10.1073/pnas.2020457119 | PMCID: PMC8794831 | PMID: 35042790
- Evidence: Genotypes were converted to continuous sequence (Fasta format) using a custom Perl script and reverse complemented if necessary, and individual genes were aligned with MAFFT ( 80 ) to their FToL homologs (git 19.3 to 19.6).
- Full pipeline: alignment/mapping [BWA, MAFFT] -> variant calling [GATK, MAFFT, SHAPEIT] -> differential/statistical testing [GEMMA] -> structure determination [IQ-TREE] -> stage not stated [BCFtools, R, RAxML, VCFtools]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Version used: **7.453**
- Evidence: Protein sequences of each family were aligned with MAFFT v7.453 (option --auto) ( 74 ) and alignments were trimmed with trimAl v1.4.rev15 ( 75 ).
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### &lt;i&gt;GRASSY TILLERS1&lt;/i&gt; (&lt;i&gt;GT1&lt;/i&gt;) and &lt;i&gt;SIX-ROWED SPIKE1&lt;/i&gt; (&lt;i&gt;VRS1&lt;/i&gt;) homologs share conserved roles in growth repression. (PNAS 2023)

- DOI: 10.1073/pnas.2311961120 | PMCID: PMC10742383 | PMID: 38096411
- Evidence: The peptide sequences that met the cut-off were aligned using MAFFT ( 65 ).
- Full pipeline: read trimming [STAR v2.7.9a, Trimmomatic] -> alignment/mapping [HTSeq, MAFFT, STAR v2.7.9a, Trimmomatic] -> differential/statistical testing [DESeq2] -> visualisation [IQ-TREE, R]

### Diversity, evolution, and classification of the RNA-guided nucleases TnpB and Cas12. (PNAS 2023)

- DOI: 10.1073/pnas.2308224120 | PMCID: PMC10691335 | PMID: 37983496
- Evidence: The TnpBs from the passing windows were aligned using MAFFT and used to construct a matrix of pairwise protein sequence identity.
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> stage not stated [AlphaFold]

### Resistance gene-guided genome mining reveals the roseopurpurins as inhibitors of cyclin-dependent kinases. (PNAS 2023)

- DOI: 10.1073/pnas.2310522120 | PMCID: PMC10691236 | PMID: 37983497
- Evidence: Kinase sequences were collected from UniProt ( SI Appendix , Table S5 ), trimmed to include only the kinase domain in the alignment, and aligned using MAFFT v7 ( https://mafft.cbrc.jp/alignment/server/ ) ( 47 ) using the default settings.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, PyMOL] -> structure determination [CCP4] -> visualisation [PyMOL]

### Male-killing virus in a noctuid moth &lt;i&gt;Spodoptera litura&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2312124120 | PMCID: PMC10655585 | PMID: 37931114
- Evidence: The RdRP sequences were aligned using MAFFT, trimmed manually, as well as using TrimAl, and then used for maximum likelihood tree reconstruction using RAxML, by applying the best evolutionary model found by ModelTest-NG.
- Full pipeline: read trimming [MAFFT, RAxML] -> alignment/mapping [MAFFT, RAxML] -> structure determination [MAFFT, RAxML] -> stage not stated [BLAST]

### Evidence for an ancient aquatic origin of the RNA viral order &lt;i&gt;Articulavirales&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2310529120 | PMCID: PMC10636315 | PMID: 37906647
- Version used: **7.490**
- Evidence: In this case, sequences were aligned in MAFFT v7.490 ( 33 ), and the phylogenetic tree was inferred using the maximum likelihood approach in IQ-TREE v1.6.12 ( 31 ) with ModelFinder, which selected LG+F+R10 as the best-fit model.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [IQ-TREE v1.6.12, MAFFT v7.490, MUSCLE v5.1] -> quantification [RSEM v1.3.0] -> visualisation [R v4.1] -> stage not stated [BLAST v2.0.9]

### Bacterial tolerance to host-exuded specialized metabolites structures the maize root microbiome. (PNAS 2023)

- DOI: 10.1073/pnas.2310134120 | PMCID: PMC10622871 | PMID: 37878725
- Version used: **7.475**
- Evidence: They were first concatenated, then aligned using MAFFT v.
- Full pipeline: alignment/mapping [MAFFT v7.475] -> stage not stated [DESeq2, R, RAxML v8.2.12, emmeans, phyloseq, phytools]

### Red fluorescent proteins engineered from green fluorescent proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2307687120 | PMCID: PMC10636333 | PMID: 37871160
- Evidence: The tree was generated using MAFFT ( 10 ) and iTOL ( 11 ).
- Full pipeline: stage not stated [MAFFT, PHENIX]

### Amine-recognizing domain in diverse receptors from bacteria and archaea evolved from the universal amino acid sensor. (PNAS 2023)

- DOI: 10.1073/pnas.2305837120 | PMCID: PMC10589655 | PMID: 37819981
- Evidence: Protein sequence regions corresponding to the dCache_1 domain were extracted from the identified sequences and divided into four separate datasets, and each was aligned on the local computational cluster using the FFT-NS-2 algorithm of the MAFFT package ( 59 ).
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> differential/statistical testing [MrBayes] -> stage not stated [AlphaFold, AutoDock Vina, Open Babel, PyMOL]

### Changes in parrot diversity after human arrival to the Caribbean. (PNAS 2023)

- DOI: 10.1073/pnas.2301128120 | PMCID: PMC10576146 | PMID: 37748079
- Version used: **7.455**
- Evidence: MAFFT v.
- Full pipeline: read trimming [fastp] -> alignment/mapping [BWA v0.7.13, IQ-TREE v2.1.2, SAMtools v1.10] -> stage not stated [BCFtools v1.12, MAFFT v7.455, R v4.1]

### Scaphopoda is the sister taxon to Bivalvia: Evidence of ancient incomplete lineage sorting. (PNAS 2023)

- DOI: 10.1073/pnas.2302361120 | PMCID: PMC10556646 | PMID: 37738291
- Version used: **7.453**
- Evidence: Sequences <100 amino acids (a.a.) were removed from OrthoFinder output fasta files, and those sampled for ≥50% of taxa were aligned with MAFFT v7.453 ( 82 ).
- Full pipeline: alignment/mapping [BWA, Cufflinks v2.3.1, HISAT2 v2.2.1, MAFFT v7.453] -> differential/statistical testing [MrBayes] -> stage not stated [BLAST v2.13.0, BUSCO v5.4.2b, IQ-TREE, OrthoFinder v2.4.0, RAxML, hifiasm v0.13]

### Evolutionary history of MEK1 illuminates the nature of deleterious mutations. (PNAS 2023)

- DOI: 10.1073/pnas.2304184120 | PMCID: PMC10450672 | PMID: 37579140
- Evidence: All collected sequences were used to generate a MSA using MAFFT v7 L-INS-i algorithm ( 91 ).
- Full pipeline: stage not stated [MAFFT]

### Frequent transitions in mating-type locus chromosomal organization in <i>Malassezia</i> and early steps in sexual reproduction. (PNAS 2023)

- DOI: 10.1073/pnas.2305094120 | PMCID: PMC10410736 | PMID: 37523560
- Version used: **7.310**
- Evidence: For species-tree reconstruction, single-copy orthologs were identified across Malassezia spp. and the outgroup U. maydis with OrthoFinder v2.5.4 ( 72 ) and aligned with MAFFT v7.310 ( 73 ).
- Full pipeline: read trimming [Canu v2.1.1, STAR v2.7.4a, Trim Galore v0.6.7] -> alignment/mapping [MAFFT v7.310, OrthoFinder v2.5.4, STAR v2.7.4a, Trim Galore v0.6.7] -> quantification [DESeq2 v1.36.0, featureCounts v2.0.1] -> differential/statistical testing [DESeq2 v1.36.0, featureCounts v2.0.1] -> structure determination [MAFFT v7.310, OrthoFinder v2.5.4] -> stage not stated [IQ-TREE v2.1.3, Pilon v1.22]

### Data-driven large-scale genomic analysis reveals an intricate phylogenetic and functional landscape in J-domain proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2218217120 | PMCID: PMC10410713 | PMID: 37523524
- Version used: **7.487**
- Evidence: We then aligned this seed using MAFFT (v7.487) ( 72 ) and manually identified a region comprising 55 positions defining the pseudoZFLR domain.
- Full pipeline: alignment/mapping [MAFFT v7.487] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold]

### Origin of the OAS-RNase L innate immune pathway before the rise of jawed vertebrates via molecular tinkering. (PNAS 2023)

- DOI: 10.1073/pnas.2304687120 | PMCID: PMC10400998 | PMID: 37487089
- Evidence: Significant hits were aligned using the L-INS-I strategy implemented in MAFFT and refined manually ( 51 ).
- Full pipeline: alignment/mapping [MAFFT, minimap2] -> structure determination [MAFFT] -> stage not stated [AlphaFold, HMMER, IQ-TREE v2.0]

### Genomic and geographical structure of human cytomegalovirus. (PNAS 2023)

- DOI: 10.1073/pnas.2221797120 | PMCID: PMC10372631 | PMID: 37459519
- Evidence: Multiple sequence alignments were obtained using MAFFT v7 ( 81 ), particularly variable sections were realigned using MUSCLE ( 82 ) and checked manually.
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> registration [MAFFT, MUSCLE] -> stage not stated [IQ-TREE, Python, R]

### A periplasmic phospholipase that maintains outer membrane lipid asymmetry in <i>Pseudomonas aeruginosa</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302546120 | PMCID: PMC10374164 | PMID: 37463202
- Version used: **7.490**
- Evidence: Protein sequences of the MlaA homologs were aligned using MAFFT v7.490 in Geneious Prime with the BLOSUM62 scoring matrix, a gap open penalty of 1.53, and an offset value of 0.123 ( 74 , 75 ).
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.490, PyMOL] -> stage not stated [AlphaFold, IQ-TREE v1.6.12]

### Mechanism of RanGTP priming H2A-H2B release from Kap114 in an atypical RanGTP•Kap114•H2A-H2B complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301199120 | PMCID: PMC10629556 | PMID: 37450495
- Evidence: These contacts were then manually curated and mapped onto a multiple sequence alignment generated by MAFFT ( 51 ) and visualized by ESPript 3.0 ( 50 ).
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [ChimeraX, PHENIX, UCSF Chimera] -> visualisation [MAFFT] -> stage not stated [PyMOL v2.5]

### Identification of a second glycoform of the clinically prevalent O1 antigen from <i>Klebsiella pneumoniae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2301302120 | PMCID: PMC10629545 | PMID: 37428935
- Evidence: S8 ) of WbbZ orthologs encoded in polysaccharide-biosynthesis loci from bacteria with known polysaccharide structures ( SI Appendix , Table S3 ) MAFFT was used to generate the alignment and build the tree, and bootstrap values greater than 20 (from 100 iterations) are shown.
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [MAFFT] -> stage not stated [AlphaFold, BLAST]

### Qualitative metabolomics-based characterization of a phenolic UDP-xylosyltransferase with a broad substrate spectrum from &lt;i&gt;Lentinus brumalis&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2301007120 | PMCID: PMC10334773 | PMID: 37399371
- Version used: **7.310**
- Evidence: Sequences containing a Pfam domain “UDP-glucoronosyl and UDP-glucosyl transferase (PF00201)” were retrieved and aligned for a phylogenetic analysis, using MAFFT (v7.310) with the “auto” setting ( 78 ).
- Full pipeline: read trimming [R v3.26.8, Trim Galore v0.6.6, edgeR v3.26.8] -> alignment/mapping [Clustal Omega, HTSeq, MAFFT v7.310, R v3.26.8, edgeR v3.26.8] -> quantification [R v3.26.8, edgeR v3.26.8] -> normalisation [R v3.26.8, edgeR v3.26.8] -> stage not stated [AlphaFold, ColabFold, HISAT2, HMMER]

### Echoes of ancient introgression punctuate stable genomic lineages in the evolution of figs. (PNAS 2023)

- DOI: 10.1073/pnas.2222035120 | PMCID: PMC10334730 | PMID: 37399402
- Version used: **7.450**
- Evidence: The filtered sequences were aligned with MAFFT 7.450 ( 62 ), and sites with over 75% gaps were removed using TrimAl ( 63 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.450, RAxML] -> stage not stated [SAMtools]

### Plant lysin motif extracellular proteins are required for arbuscular mycorrhizal symbiosis. (PNAS 2023)

- DOI: 10.1073/pnas.2301884120 | PMCID: PMC10318984 | PMID: 37368927
- Evidence: We then retrieved 304 homologous protein sequences from 50 plant species and performed phylogenetic analysis using MAFFT ( SI Appendix , Table S1 ).
- Full pipeline: stage not stated [AlphaFold, MAFFT]

### Replitrons: A major group of eukaryotic transposons encoding HUH endonuclease. (PNAS 2023)

- DOI: 10.1073/pnas.2301424120 | PMCID: PMC10288648 | PMID: 37307447
- Version used: **7.471**
- Evidence: Alignment was performed using MAFFT v7.471 and the L-INS-i method ( 70 ).
- Full pipeline: alignment/mapping [MAFFT v7.471] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BEDTools, IQ-TREE v2.0.3]

### A specialized integrin-binding motif enables proTGF-β2 activation by integrin αVβ6 but not αVβ8. (PNAS 2023)

- DOI: 10.1073/pnas.2304874120 | PMCID: PMC10268255 | PMID: 37279271
- Evidence: Full-length TGF-β sequences were aligned with MAFFT ( 37 ); the portion between the β7 and β10 strands ( Fig.
- Full pipeline: alignment/mapping [MAFFT] -> normalisation [CCP4] -> structure determination [Coot, PHENIX]

### <i>oskar</i> acts with the transcription factor Creb to regulate long-term memory in crickets. (PNAS 2023)

- DOI: 10.1073/pnas.2218506120 | PMCID: PMC10214185 | PMID: 37192168
- Version used: **7.510**
- Evidence: All identified sequences were then aligned with MAFFT (v 7.510) ( 61 ).
- Full pipeline: read trimming [Cutadapt v3.4, RSEM v1.2.29, STAR v2.7.0e] -> alignment/mapping [MAFFT v7.510] -> quantification [Cutadapt v3.4, ImageJ, RSEM v1.2.29, STAR v2.7.0e] -> visualisation [RAxML]

### A tale of two copies: Evolutionary trajectories of moth pheromone receptors. (PNAS 2023)

- DOI: 10.1073/pnas.2221166120 | PMCID: PMC10193968 | PMID: 37155838
- Evidence: To reconstruct putative ancestral sequences of OR5 and OR75, a multiple sequence alignment was first performed using MAFFT ( 58 ) with homologous amino acid sequences from Noctuidae species, including S. littoralis , S. litura , S. exigua , S. frugiperda , Helicoverpa armigera , H. zea , Athetis dissimilis, and A. lepigone .
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2, MAFFT] -> dimensionality reduction/clustering [AlphaFold, R] -> structure determination [MAFFT] -> stage not stated [ChimeraX]

### Chitin utilization by marine picocyanobacteria and the evolution of a planktonic lifestyle. (PNAS 2023)

- DOI: 10.1073/pnas.2213271120 | PMCID: PMC10194020 | PMID: 37159478
- Evidence: Each set of sequences were then aligned in MAFFT ( 80 ) with the automatic algorithm selection option.
- Full pipeline: alignment/mapping [HTSeq, MAFFT] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2] -> stage not stated [BLAST]

### Vertebrate-tropism of a cressdnavirus lineage implicated by poxvirus gene capture. (PNAS 2023)

- DOI: 10.1073/pnas.2303844120 | PMCID: PMC10193959 | PMID: 37155884
- Version used: **7.487**
- Evidence: For phylogenetic analyses, regions of apvRep proteins gained by gene fusion were manually trimmed prior to alignment with cressdnavirus references using MAFFT v7.487 ( 74 ), and analysis with IQ-TREE v2.2.0 ( 75 ).
- Full pipeline: read trimming [IQ-TREE v2.2.0, MAFFT v7.487] -> alignment/mapping [AlphaFold v2.1.1, BEDTools, BLAST v2.0.15, IQ-TREE v2.2.0, MAFFT v7.487] -> visualisation [AlphaFold v2.1.1]

### Elucidating the origins of phycocyanobilin biosynthesis and phycobiliproteins. (PNAS 2023)

- DOI: 10.1073/pnas.2300770120 | PMCID: PMC10151467 | PMID: 37071675
- Version used: **7.450**
- Evidence: Multiple sequence alignments were constructed in MAFFT v7.450 ( 97 ).
- Full pipeline: alignment/mapping [MAFFT v7.450] -> visualisation [VMD] -> stage not stated [AlphaFold]

### Genomic and structural basis for evolution of tropane alkaloid biosynthesis. (PNAS 2023)

- DOI: 10.1073/pnas.2302448120 | PMCID: PMC10151470 | PMID: 37068250
- Evidence: Protein sequences of 108 single-copy orthologous families were aligned by MAFFT ( 38 ) and were then corrected by Gblocks ( 39 ).
- Full pipeline: alignment/mapping [BUSCO, MAFFT] -> dimensionality reduction/clustering [OrthoFinder] -> visualisation [PyMOL v2.4] -> stage not stated [AlphaFold, AutoDock Vina v1.1.2, IQ-TREE]

### Bayesian phylodynamics reveals the transmission dynamics of avian influenza A(H7N9) virus at the human-live bird market interface in China. (PNAS 2023)

- DOI: 10.1073/pnas.2215610120 | PMCID: PMC10151560 | PMID: 37068240
- Evidence: The resulting alignment of 798 sequences was made using MAFFT v7 ( 77 ) and checked using AliView v1.26 ( 78 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BEAST, R v4.0]

### Standing genetic variation fuels rapid evolution of herbicide resistance in blackgrass. (PNAS 2023)

- DOI: 10.1073/pnas.2206808120 | PMCID: PMC10120058 | PMID: 37043536
- Version used: **7.407**
- Evidence: Multiple alignments of all haplotypes per population were performed with MAFFT v7.407 ( 75 ), trees were inferred with RAXML-NG v0.9.0 ( 71 ), and minimum spanning networks were visualized with POPART v.1.7 ( 76 ) ( Fig.
- Full pipeline: read trimming [BUSCO] -> alignment/mapping [MAFFT v7.407] -> variant calling [MAFFT v7.407] -> visualisation [MAFFT v7.407] -> stage not stated [ADMIXTURE, ANGSD v0.930, GATK v4.1.3.0, InterProScan]

### Large-scale invasion of unicellular eukaryotic genomes by integrating DNA viruses. (PNAS 2023)

- DOI: 10.1073/pnas.2300465120 | PMCID: PMC10120064 | PMID: 37036967
- Version used: **7.490**
- Evidence: All candidate MCP genes were clustered with MMseqs2 at 30% identity across 80% length, and each cluster was aligned with MAFFT v7.490 ( 44 ) with the alignment used as an input to HHpred ( https://toolkit.tuebingen.mpg.de/tools/hhpred ) (settings: global:realign).
- Full pipeline: alignment/mapping [BEDTools, ColabFold, MAFFT v7.490, MUSCLE v3.8.1551] -> registration [MAFFT v7.490] -> dimensionality reduction/clustering [ColabFold, HMMER v3.1b, MAFFT v7.490, MUSCLE v3.8.1551] -> stage not stated [AlphaFold, Cytoscape, Flye v2.9, minimap2]

### Evolution of insect innate immunity through domestication of bacterial toxins. (PNAS 2023)

- DOI: 10.1073/pnas.2218334120 | PMCID: PMC10120054 | PMID: 37036995
- Version used: **7.450**
- Evidence: Sequences were aligned in MAFFT v7.450 ( 40 , 41 ), and protein topologies were inferred using maximum likelihood as implemented in W-IQ-TREE ( http://iqtree.cibiv.univie.ac.at/ ) ( 42 ) using the best-fit model as assessed by BIC in ModelFinder.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.450] -> stage not stated [AlphaFold v2.1.0]

### The <i>Holothuria leucospilota</i> genome elucidates sacrificial organ expulsion and bioadhesive trap enriched with amyloid-patterned proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2213512120 | PMCID: PMC10120082 | PMID: 37036994
- Evidence: Multiple sequence alignments for all gene families mentioned above were built with the Multiple Alignment using Fast Fourier Transform (MAFFT) aligner, while their corresponding phylogeny was inferred with RAxML, followed by visualization with Evolview.
- Full pipeline: alignment/mapping [BUSCO, BWA, MAFFT, RAxML] -> normalisation [DESeq2] -> visualisation [MAFFT, RAxML] -> stage not stated [AlphaFold, InterProScan]

### <i>Starships</i> are active eukaryotic transposable elements mobilized by a new family of tyrosine recombinases. (PNAS 2023)

- DOI: 10.1073/pnas.2214521120 | PMCID: PMC10104507 | PMID: 37023132
- Evidence: Alignments were generated using MAFFT with default parameters.
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega, MAFFT, MrBayes] -> differential/statistical testing [Clustal Omega, MrBayes] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.0.3]

### Euglenozoan kleptoplasty illuminates the early evolution of photoendosymbiosis. (PNAS 2023)

- DOI: 10.1073/pnas.2220100120 | PMCID: PMC10041101 | PMID: 36927158
- Evidence: Each protein dataset was aligned using the Multiple Alignment using Fast Fourier Transform (MAFFT) algorithm (with the default parameters) from the MAFFT package v7.271 ( 56 ).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [IQ-TREE, MAFFT] -> differential/statistical testing [IQ-TREE] -> stage not stated [BUSCO, SPAdes v3.10.1]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Version used: **7.294b**
- Evidence: We used 244 orthogroups that retained three or four chicken ohnologs and performed coding sequence alignments using MAFFT (v7.294b) ( 104 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### A global phylogenomic analysis of the shiitake genus <i>Lentinula</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2214076120 | PMCID: PMC10013852 | PMID: 36848567
- Version used: **7.487**
- Evidence: Phylogenetic analyses of leggt and lecsl genes or Pfam domains were performed using IQ-TREE v2.0.3 (-B 1000) ( 35 ) following aligning with MAFFT v7.487 (--auto) ( 62 ) and trimming using ClipKIT v1.3.0 ( 63 ).
- Full pipeline: quality control [SAMtools] -> read trimming [IQ-TREE v2.0.3, MAFFT v7.487] -> alignment/mapping [IQ-TREE v2.0.3, MAFFT v7.487, SAMtools, freebayes] -> dimensionality reduction/clustering [PLINK, ggplot2] -> structure determination [BLAST v2.5.0] -> visualisation [PLINK, R, ggplot2] -> stage not stated [BEAST v2.6.3, BUSCO v5.3.2, HMMER v3.3.2, OrthoFinder, RAxML, SPAdes v3.12.0, VCFtools]

### A conserved zinc-binding site in <i>Acinetobacter baumannii</i> PBP2 required for elongasome-directed bacterial cell shape. (PNAS 2023)

- DOI: 10.1073/pnas.2215237120 | PMCID: PMC9974482 | PMID: 36787358
- Evidence: Protein sequences were aligned with MAFFT L-INS-i v7.490 ( 78 ) and analyzed in Jalview v2.11.1.4 ( 79 ).
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [CCP4] -> visualisation [PyMOL]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Version used: **7.475**
- Evidence: These single-copy gene protein sequences were aligned using MAFFT v7.475, alignments trimmed by TrimAl v1.4.rev15, and used to infer a phylogenomic species tree using IQ-TREE v2.2.0.3.
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### White-tailed deer (<i>Odocoileus virginianus</i>) may serve as a wildlife reservoir for nearly extinct SARS-CoV-2 variants of concern. (PNAS 2023)

- DOI: 10.1073/pnas.2215067120 | PMCID: PMC9963525 | PMID: 36719912
- Version used: **7.453**
- Evidence: Sequences from the present study were grouped according to its VOC classification, and nucleotide sequence alignments were performed individually for each group of VOCs using MAFFT v7.453 ( 38 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.453, QGIS] -> dimensionality reduction/clustering [QGIS] -> visualisation [IQ-TREE, QGIS] -> stage not stated [Nextstrain, Pangolin v4.0.6]

### Edaphic specialization onto bare, rocky outcrops as a factor in the evolution of desert angiosperms. (PNAS 2023)

- DOI: 10.1073/pnas.2214729120 | PMCID: PMC9963280 | PMID: 36716359
- Evidence: Loci with less than 95% occupancy were removed and the remaining 229 loci aligned using MAFFT ( 50 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [RAxML]

### MITE infestation accommodated by genome editing in the germline genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213985120 | PMCID: PMC9942856 | PMID: 36669106
- Version used: **7.450**
- Evidence: All the nucleotide sequences ≥500 bp for the repeat families identified by RepeatClassifier as LINE or LINE/RTE-x: rnd-1_family-273, rnd-1_family-276 and rnd-4_family-193 were aligned to one another with MAFFT v7.450 (automatic algorithm) ( 94 ), with the option to automatically determine sequence direction [via the MAFFT plugin for Geneious Prime ( 95 )].
- Full pipeline: alignment/mapping [AUGUSTUS, Bowtie2 v2.4.2, MAFFT v7.450, SAMtools v1.10, minimap2 v2.17] -> dimensionality reduction/clustering [RepeatMasker v2.0.1, SAMtools v1.10] -> machine learning [MAFFT v7.450] -> stage not stated [SciPy, featureCounts v2.0.1]

### Origins of genome-editing excisases as illuminated by the somatic genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213887120 | PMCID: PMC9942806 | PMID: 36669098
- Evidence: ...genomes together with PiggyBac-like elements from other eukaryotic lineages and domesticated PiggyBac homologs from other ciliates were aligned using MAFFT ( 63 ) and used to generate the phylogenetic tree using FastTree2 ( 64 ), using the Geneious bioinformatic software ( 65 ) plug-ins for both tools.
- Full pipeline: alignment/mapping [MAFFT] -> machine learning [RepeatMasker v2.0.1] -> stage not stated [BUSCO, Flye v2.7, HMMER, OrthoFinder, eggNOG]

### Natural variation in the binding pocket of a parasitic flatworm TRPM channel resolves the basis for praziquantel sensitivity. (PNAS 2023)

- DOI: 10.1073/pnas.2217732120 | PMCID: PMC9910428 | PMID: 36574686
- Version used: **6.864**
- Evidence: For the calculation of TRPM PZQ amino acid identity, sequences were aligned using MAFFT (v6.864) and aligned sequences analyzed using the Ident and Sim interface using standard groups for amino acid similarity ( 65 ).
- Full pipeline: alignment/mapping [MAFFT v6.864]

### Photosynthetic demands on translational machinery drive retention of redundant tRNA metabolism in plant organelles. (PNAS 2024)

- DOI: 10.1073/pnas.2421485121 | PMCID: PMC11670086 | PMID: 39693336
- Version used: **7.525**
- Evidence: S8–S10 ). using RAxML v 8.2.12 ( 103 ) after aligning sequences using MAFFT v7.525 ( 104 ) trimming with trimAl v1.5 ( 105 ).
- Full pipeline: read trimming [MAFFT v7.525, RAxML v8.2.12, SPAdes v3.15.4] -> alignment/mapping [MAFFT v7.525, RAxML v8.2.12] -> visualisation [Python]

### Canonical terpene synthases in arthropods: Intraphylum gene transfer. (PNAS 2024)

- DOI: 10.1073/pnas.2413007121 | PMCID: PMC11665903 | PMID: 39671179
- Version used: **7.520**
- Evidence: MAFFT v.7.520 ( 55 ) was used to perform the multiple sequence alignment with maxiterate 1000.
- Full pipeline: alignment/mapping [MAFFT v7.520, STAR v2.7.10a, minimap2] -> quantification [RSEM v1.3.1, edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> visualisation [BEDTools] -> stage not stated [HMMER v3.0, OrthoFinder, RAxML]

### Order of amino acid recruitment into the genetic code resolved by last universal common ancestor's protein domains. (PNAS 2024)

- DOI: 10.1073/pnas.2410311121 | PMCID: PMC11670089 | PMID: 39665745
- Evidence: We aligned downsampled sequences for each Pfam using MAFFT v.7 ( 89 ), to infer a preliminary tree with IQ-Tree ( 90 ), using a time nonreversible amino acid substitution matrix trained on the Pfam database (NQ.PFAM) ( 91 ), and no rate heterogeneity among sites.
- Full pipeline: alignment/mapping [MAFFT] -> machine learning [MAFFT] -> stage not stated [InterProScan, R, phytools]

### Mutation-based mechanism and evolution of the potent multidrug efflux pump RE-CmeABC in &lt;i&gt;Campylobacter&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2415823121 | PMCID: PMC11665921 | PMID: 39602248
- Evidence: Then, qualified cmeR - cmeABC sequences (n = 80,408) were aligned by using MAFFT ( 65 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic] -> alignment/mapping [Bowtie2, MAFFT] -> stage not stated [Python]

### Emergent collective behavior evolves more rapidly than individual behavior among acorn ant species. (PNAS 2024)

- DOI: 10.1073/pnas.2420078121 | PMCID: PMC11621464 | PMID: 39576350
- Evidence: We followed the standard PHYLUCE protocol for processing UCEs in preparation for phylogenomic analysis, aligning the monolithic unaligned FASTA file with the phyluce_align_seqcap_align command, using MAFFT ( 62 ) as the aligner (--aligner mafft) and opting not to edge-trim the alignment (–no-trim).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R] -> stage not stated [IQ-TREE v2.1.2, phytools]

### MurA-catalyzed synthesis of 5-enolpyruvylshikimate-3-phosphate confers glyphosate tolerance in bryophytes. (PNAS 2024)

- DOI: 10.1073/pnas.2412997121 | PMCID: PMC11588093 | PMID: 39527734
- Evidence: Confirmed EPSPS and MurA protein sequences were aligned in MAFFT using the L-INS-I algorithm ( 53 ) and visualized in Unipro Ugene v.
- Full pipeline: alignment/mapping [MAFFT] -> visualisation [MAFFT] -> stage not stated [AlphaFold, BLAST, ChimeraX]

### Tolerance and efficient metabolization of extremely high ethanol concentrations by a social wasp. (PNAS 2024)

- DOI: 10.1073/pnas.2410874121 | PMCID: PMC11536130 | PMID: 39432778
- Version used: **7.490**
- Evidence: The sequence alignment was performed using MAFFT v7.490 as implemented in Geneious Prime 2023.2.1 under the E-ins-i algorithm.
- Full pipeline: alignment/mapping [MAFFT v7.490] -> differential/statistical testing [R v4.2.1]

### &lt;i&gt;Prevotella&lt;/i&gt; are major contributors of sialidases in the human vaginal microbiome. (PNAS 2024)

- DOI: 10.1073/pnas.2400341121 | PMCID: PMC11388281 | PMID: 39186657
- Version used: **7.508**
- Evidence: We used HMMER (v3.3.2) to find ribosomal proteins, aligned the sequences with MAFFT (v7.508) and used RAxML (v.8.2.10) to create the phylogenetic trees.
- Full pipeline: alignment/mapping [HMMER v3.3.2, MAFFT v7.508, RAxML v8.2.10] -> stage not stated [AlphaFold, InterProScan, Python]

### Climate, demography, immunology, and virology combine to drive two decades of dengue virus dynamics in Cambodia. (PNAS 2024)

- DOI: 10.1073/pnas.2318704121 | PMCID: PMC11388344 | PMID: 39190356
- Evidence: After selection, sequences were aligned by serotype in the program MAFFT ( 74 ), and the best fit nucleotide substitution model for each serotype was evaluated in ModelTest-NG ( 75 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [BEAST] -> stage not stated [R, RAxML]

### Elucidating the sustainability of 700 y of Inuvialuit beluga whale hunting in the Mackenzie River Delta, Northwest Territories, Canada. (PNAS 2024)

- DOI: 10.1073/pnas.2405993121 | PMCID: PMC11348011 | PMID: 39136992
- Evidence: The mitochondrial sequences were aligned using MAFFT v/7.392 ( 89 ) using default settings.
- Full pipeline: alignment/mapping [BWA, MAFFT, RepeatMasker, SAMtools] -> registration [GATK, Picard] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ANGSD]

### Flexible oviposition behavior enabled the evolution of terrestrial reproduction. (PNAS 2024)

- DOI: 10.1073/pnas.2312371121 | PMCID: PMC11295038 | PMID: 39042675
- Evidence: Sequences of each gene were aligned separately using MAFFT ( 35 ) and the best substitution model for each gene was estimated using ModelTest-NG ( 36 ), executed within raxmlGUI 2.0 ( 37 ) ( SI Appendix , Table S3 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.2] -> stage not stated [ImageJ, RAxML v1.0.3, emmeans, lme4, phytools]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Version used: **7.511**
- Evidence: To examine the presence of a protease, we aligned with NS3Pro of Classical swine fever virus (CSFV), Pangolin pestivirus, and the divergent flavi-like virus with MAFFT v7.511 ( 65 ) L-INS-I method.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### Multisubstrate specificity shaped the complex evolution of the aminotransferase family across the tree of life. (PNAS 2024)

- DOI: 10.1073/pnas.2405524121 | PMCID: PMC11214133 | PMID: 38885378
- Evidence: For structure-guided multiple sequence alignment, amino acid sequences were aligned by a MAFFT-DASH ( 49 ) using a BLOSUM62 scoring matrix (gap opening penalty = 1.53).
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [seaborn] -> simulation/modelling [AutoDock Vina v4.2.6] -> stage not stated [AlphaFold v2.1.0, HMMER v3.3.1, RAxML v1.2.0]

### Identification of two archaeal GDGT lipid-modifying proteins reveals diverse microbes capable of GMGT biosynthesis and modification. (PNAS 2024)

- DOI: 10.1073/pnas.2318761121 | PMCID: PMC11214058 | PMID: 38885389
- Evidence: The combined sequences were aligned using MAFFT on XSEDE (7.505) with the BLOSUM62 scoring matrix and a gap penalty of 1.53 ( 69 ) and the resulting alignments were used to construct phylogenetic trees with IQtree (2.2.0) using ModelFinder (best fit model chosen: LG+I+I+R10) and 1,000 ultrafast bootstraps for Gms ( 70 – 73 ) and FastTreeMP on XSEDE (2.1.10) with the JTT+CAT model and 1,000 local s...
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [AlphaFold]

### Illuminating the coevolution of photosynthesis and Bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2322120121 | PMCID: PMC11194577 | PMID: 38875151
- Evidence: ...g to the same order (see individual figure captions for details), a sequence alignment for the selected sequences was prepared through alignment with MAFFT (--localpair --maxiterate 1000) (v7.427) ( 94 ) and trimming with trimAl (v1.4.rev22) ( 95 ) with a gap threshold of 0.3 (0.1 for type I reaction centers, 0.05 for type 2 reaction centers and PufA, and 0.6 for PRK and the RuBisCO large subunit)...
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [IQ-TREE v2.1.3, MAFFT] -> stage not stated [AlphaFold, BEAST v2.6.6, Prokka v1.14]

### <i>Rickettsia</i> symbionts spread via mixed mode transmission, increasing female fecundity and sex ratio shift by host hormone modulating. (PNAS 2024)

- DOI: 10.1073/pnas.2406788121 | PMCID: PMC11194588 | PMID: 38865267
- Version used: **7.520**
- Evidence: Nucleotide sequences were aligned using MAFFT v7.520 with the L-INS-i method.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, MAFFT v7.520] -> differential/statistical testing [edgeR] -> structure determination [MrBayes v3.2.7]

### Estimation of SARS-CoV-2 fitness gains from genomic surveillance data without prior lineage classification. (PNAS 2024)

- DOI: 10.1073/pnas.2314262121 | PMCID: PMC11194495 | PMID: 38861609
- Evidence: MSA was performed by MAFFT ( 22 ) as described on the GISAID platform.
- Full pipeline: quantification [Nextstrain] -> stage not stated [MAFFT]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: The protein sequences of each OG were aligned using MAFFT ( 97 ) and trimmed by trimAL ( 98 ) using default parameters.
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Natural variation of immune epitopes reveals intrabacterial antagonism. (PNAS 2024)

- DOI: 10.1073/pnas.2319499121 | PMCID: PMC11161748 | PMID: 38814867
- Evidence: Phylogenetic trees for bacteria relatedness were built using GToTree, and protein trees were built using MAFFT for sequence alignment and IQ-TREE tree building.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT]

### DELLA proteins recruit the Mediator complex subunit MED15 to coactivate transcription in land plants. (PNAS 2024)

- DOI: 10.1073/pnas.2319163121 | PMCID: PMC11087773 | PMID: 38696472
- Version used: **7.0**
- Evidence: The protein sequences were aligned with MAFFT 7.0, using the L-INS-I method ( 42 ), followed by manual curation.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9] -> alignment/mapping [Cutadapt, FastQC v0.11.9, HISAT2, HTSeq, MAFFT v7.0] -> quantification [Cutadapt, DESeq2 v1.24.0, FastQC v0.11.9, HISAT2, HTSeq] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [ggplot2]

### Frequent nonhomologous replacement of replicative helicase loaders by viruses in <i>Vibrionaceae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2317954121 | PMCID: PMC11087808 | PMID: 38683976
- Version used: **7.212**
- Evidence: For the tree of the VdhL genes, the amino acid sequences of the CDSs were aligned using MAFFT version 7.212 ( 79 ) with default parameters.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.212] -> visualisation [PyMOL, R, ggplot2] -> stage not stated [AlphaFold, BLAST, eggNOG]

### Identification and epidemiological study of an uncultured flavivirus from ticks using viral metagenomics and pseudoinfectious viral particles. (PNAS 2024)

- DOI: 10.1073/pnas.2319400121 | PMCID: PMC11087778 | PMID: 38687787
- Evidence: Multiple sequence alignments were performed using the MAFFT ( 70 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [MrBayes v3.2.7a]

### Evolution of homologous recombination rates across bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2316302121 | PMCID: PMC11067023 | PMID: 38657048
- Evidence: These universal orthologs were then aligned with MAFFT and concatenated ( 54 ).
- Full pipeline: alignment/mapping [MAFFT, eggNOG] -> dimensionality reduction/clustering [eggNOG] -> differential/statistical testing [R] -> simulation/modelling [R] -> stage not stated [HMMER, RAxML]

### What one genus of showy moths can say about migration, adaptation, and wing pattern. (PNAS 2024)

- DOI: 10.1073/pnas.2319726121 | PMCID: PMC11047066 | PMID: 38630713
- Evidence: Sequences of the identified FMOs were aligned with MAFFT ( 56 ) and provided to IQ-TREE (v1.6.12) ( 57 ) for phylogeny inference.
- Full pipeline: alignment/mapping [AlphaFold, BUSCO, HMMER, IQ-TREE v1.6.12, MAFFT] -> stage not stated [scikit-learn]

### A region of suppressed recombination misleads neoavian phylogenomics. (PNAS 2024)

- DOI: 10.1073/pnas.2319506121 | PMCID: PMC11009670 | PMID: 38557186
- Version used: **7.475**
- Evidence: These were aligned using MAFFT v.7.475 ( 63 ) and cleaned using Gblocks v.0.91b ( 64 ).
- Full pipeline: alignment/mapping [MAFFT v7.475] -> dimensionality reduction/clustering [R, clusterProfiler v4.6.2]

### Intergenerational protective anti-gut commensal immunoglobulin G originates in early life. (PNAS 2024)

- DOI: 10.1073/pnas.2309994121 | PMCID: PMC10990157 | PMID: 38517976
- Version used: **7.475**
- Evidence: Consensus sequence of Sanger sequenced splenic isolates was aligned with MAFFT v7.475 ( 50 ) to IgG bound bacteria 16S and reference genome 16S sequences and trimmed to overlapping region.
- Full pipeline: read trimming [Bowtie2 v2.4.1, MAFFT v7.475] -> alignment/mapping [Bowtie2 v2.4.1, MAFFT v7.475] -> dimensionality reduction/clustering [Docker] -> visualisation [R v4.0, phyloseq] -> stage not stated [BLAST, RAxML]

### The evolutionary genomics of adaptation to stress in wild rhizobium bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2311127121 | PMCID: PMC10990125 | PMID: 38507447
- Version used: **7.475**
- Evidence: Amino acid sequences of nreA , nreX , and nreY were each aligned using MAFFT v.
- Full pipeline: quality control [Prokka v1.13.3] -> read trimming [MUSCLE] -> alignment/mapping [MAFFT v7.475, MUSCLE] -> differential/statistical testing [lme4 v1.1] -> visualisation [R] -> stage not stated [RAxML, SPAdes v3.14.1]

### Unsupervised identification of significant lineages of SARS-CoV-2 through scalable machine learning methods. (PNAS 2024)

- DOI: 10.1073/pnas.2317284121 | PMCID: PMC10962941 | PMID: 38478692
- Version used: **7.453**
- Evidence: Each sequence was aligned to the reference sequence hCov-19/Wuhan/WIV04/2019 ( 43 ) using the tool MAFFT v7.453 ( 44 ) on an Ubuntu Windows subsystem for Linux v20.04.1 LTS and Biopython v1.78 scripts.
- Full pipeline: alignment/mapping [MAFFT v7.453] -> dimensionality reduction/clustering [Pangolin, UMAP] -> stage not stated [Python v3.10.0]

### Rapid dissemination of host metabolism-manipulating genes via integrative and conjugative elements. (PNAS 2024)

- DOI: 10.1073/pnas.2309263121 | PMCID: PMC10945833 | PMID: 38457521
- Evidence: MAFFT alignments using automatic alignment parameters ( 52 ) were used to examine structural conservation of the backbone genes and identify sites of accessory gene integration.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, R]

### The metabolic domestication syndrome of budding yeast. (PNAS 2024)

- DOI: 10.1073/pnas.2313354121 | PMCID: PMC10945815 | PMID: 38457520
- Version used: **7.471**
- Evidence: We performed multiple sequence alignment on each of the 1,218 orthogroups using MAFFT (version 7.471) ( 71 ).
- Full pipeline: alignment/mapping [MAFFT v7.471] -> dimensionality reduction/clustering [OrthoFinder v2.4.0] -> stage not stated [RAxML]

### Rubisco is evolving for improved catalytic efficiency and CO<sub>2</sub> assimilation in plants. (PNAS 2024)

- DOI: 10.1073/pnas.2321050121 | PMCID: PMC10945770 | PMID: 38442173
- Evidence: Translated RbcL and RbcS protein sequences were aligned using the MAFFT L-INS-i algorithm ( 125 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE, OrthoFinder]

### Foraging predicts the evolution of warning coloration and mimicry in snakes. (PNAS 2024)

- DOI: 10.1073/pnas.2318857121 | PMCID: PMC10945821 | PMID: 38437547
- Version used: **7.487**
- Evidence: DNA sequences of five mitochondrial and five nuclear regions were obtained from GenBank ( Dataset S1 ) and aligned with MAFFT 7.487 ( 55 ).
- Full pipeline: alignment/mapping [MAFFT v7.487] -> dimensionality reduction/clustering [R]

### Incipient functional SARS-CoV-2 diversification identified through neural network haplotype maps. (PNAS 2024)

- DOI: 10.1073/pnas.2317851121 | PMCID: PMC10927536 | PMID: 38416684
- Version used: **7.453**
- Evidence: For maximum likelihood (ML) phylogenetic analysis, genome sequences were aligned using MAFFT v7.453 software ( 58 ).
- Full pipeline: alignment/mapping [MAFFT v7.453] -> structure determination [TreeTime v0.7.6] -> stage not stated [Nextstrain]

### Global diversity of enterococci and description of 18 previously unknown species. (PNAS 2024)

- DOI: 10.1073/pnas.2310852121 | PMCID: PMC10927581 | PMID: 38416678
- Evidence: In order to generate a phylogenetic tree, we identified the set of 320 orthologous groups representing genes found in single copy across all isolates (i.e., SCC), performed multiple-sequence alignment using MAFFT-linsi v7.407 ( 69 ), converted this alignment to a codon-based alignment using PAL2NAL v14 ( 70 ), and then used this alignment to construct a phylogenetic tree using IQ-TREE (v1.7-beta9)...
- Full pipeline: alignment/mapping [IQ-TREE v1.7, MAFFT, Pilon v1.23] -> dimensionality reduction/clustering [HMMER, OrthoFinder v2.3.3]

### Pyrenoid proteomics reveals independent evolution of the CO<sub>2</sub>-concentrating organelle in chlorarachniophytes. (PNAS 2024)

- DOI: 10.1073/pnas.2318542121 | PMCID: PMC10927497 | PMID: 38408230
- Evidence: Sequence alignments were generated using the L-INS-i method in the MAFFT package ( 61 ) and poorly aligned positions were removed using trimAl with the automated1 option ( 62 ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, IQ-TREE v2.2.0]

### Chromosomal evolution, environmental heterogeneity, and migration drive spatial patterns of species richness in <i>Calochortus</i> (Liliaceae). (PNAS 2024)

- DOI: 10.1073/pnas.2305228121 | PMCID: PMC10927571 | PMID: 38394215
- Version used: **7.023b**
- Evidence: Mapped transcriptome sequences were aligned to Angiosperm V1 reference sequences using MAFFT v7.023b ( 84 ).
- Full pipeline: read trimming [Trimmomatic v0.40] -> alignment/mapping [BWA, MAFFT v7.023b] -> stage not stated [BEAST v6.6, IQ-TREE, QGIS, R, SAMtools v1.3, lme4]

### Targeted hypermutation of putative antigen sensors in multicellular bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2316469121 | PMCID: PMC10907252 | PMID: 38354254
- Version used: **7.407**
- Evidence: These 257 amino acid sequences were aligned with MAFFT v7.407 ( 78 ) in einsi mode and trimmed using TrimAl v1.4.rev15 (-gappyout) ( 79 ).
- Full pipeline: read trimming [MAFFT v7.407] -> alignment/mapping [MAFFT v7.407, SAMtools, minimap2 v2.24] -> visualisation [HMMER] -> stage not stated [InterProScan]

### Loss of activation by GABA in vertebrate delta ionotropic glutamate receptors. (PNAS 2024)

- DOI: 10.1073/pnas.2313853121 | PMCID: PMC10861852 | PMID: 38285949
- Version used: **7.450**
- Evidence: Sequences were aligned with MAFFT v7.450 ( 60 ) in Geneious Prime (Dotmatics).
- Full pipeline: alignment/mapping [MAFFT v7.450] -> visualisation [PyMOL v4.6] -> stage not stated [AlphaFold, AutoDock Vina v4.2, ChimeraX v1.4, ColabFold]

### Recurrent viral capture of cellular phosphodiesterases that antagonize OAS-RNase L. (PNAS 2024)

- DOI: 10.1073/pnas.2312691121 | PMCID: PMC10835031 | PMID: 38277437
- Evidence: All alignments ( SI Appendix ) were generated using the MAFFT plug-in ( 47 ) with default parameters in Geneious Prime v2022.2.1.
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [AlphaFold] -> stage not stated [ChimeraX]

### Decoupled evolution of the <i>Sex Peptide</i> gene family and <i>Sex Peptide Receptor</i> in Drosophilidae. (PNAS 2024)

- DOI: 10.1073/pnas.2312380120 | PMCID: PMC10801855 | PMID: 38215185
- Evidence: ( A ) A consensus sequence based on MAFFT alignment of the resolvable amino acid sequences of SPR coding sequences.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### Phylogenomics of the psychoactive mushroom genus <i>Psilocybe</i> and evolution of the psilocybin biosynthetic gene cluster. (PNAS 2024)

- DOI: 10.1073/pnas.2311245121 | PMCID: PMC10801892 | PMID: 38194448
- Version used: **7.475**
- Evidence: Nucleotide sequence output from exonerate for each amino acid query was combined and aligned using the multiple sequence alignment program MAFFT version 7.475 ( 74 ) with the parameters --maxiterate 1000 --localpair --reorder.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10] -> read trimming [SPAdes v3.15.2] -> alignment/mapping [MAFFT v7.475] -> differential/statistical testing [FastQC v0.11.9, MultiQC v1.10] -> visualisation [FastQC v0.11.9, MultiQC v1.10] -> stage not stated [BLAST, BUSCO, IQ-TREE, Picard, R]

### Contingency, repeatability, and predictability in the evolution of a prokaryotic pangenome. (PNAS 2024)

- DOI: 10.1073/pnas.2304934120 | PMCID: PMC10769857 | PMID: 38147560
- Version used: **7.490**
- Evidence: Alignments of universal single-copy genes were constructed using MAFFT version 7.490 ( 31 ).
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [BLAST, R, scikit-learn]

### Distinct classes of gut bacterial molybdenum-dependent enzymes produce urolithins. (PNAS 2025)

- DOI: 10.1073/pnas.2501312122 | PMCID: PMC12771579 | PMID: 41439715
- Evidence: The unique sequences were then aligned using MAFFT-linsi v7.505 ( 87 ) and trimmed using trimal (v1.4.1, -gappyout) ( 88 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> quantification [statsmodels] -> differential/statistical testing [DESeq2 v1.44.0, statsmodels]

### A SynB1-conjugated antibody cocktail crosses the blood-brain barrier to produce a therapeutic effect on rabies. (PNAS 2025)

- DOI: 10.1073/pnas.2516465122 | PMCID: PMC12772202 | PMID: 41433073
- Evidence: To verify the broad-spectrum neutralization of the four human–mouse chimeric mAbs against RABV, 2,817 amino acid sequences of RABV-G were obtained from NCBI, and the variation in amino acids at different epitope sites was calculated and analyzed by using MEGA11 and MAFFT software.
- Full pipeline: stage not stated [MAFFT]

### Versatile NTP recognition and domain fusions expand the functional repertoire of the ParB-CTPase fold beyond chromosome segregation. (PNAS 2025)

- DOI: 10.1073/pnas.2527592122 | PMCID: PMC12704722 | PMID: 41343662
- Version used: **7.490**
- Evidence: Proteins were aligned using MAFFT v7.490, and alignments clipped using Clipkit v2.25 (mode gappy).
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [AlphaFold, AutoDock Vina, Docker, HMMER v3.4, IQ-TREE]

### Ribonuclease RNase Z is an evolutionarily conserved deAMPylase. (PNAS 2025)

- DOI: 10.1073/pnas.2515155122 | PMCID: PMC12663964 | PMID: 41264253
- Evidence: Additionally, active site conservation was evaluated for candidate deAMPylases using the Weblogo algorithm ( 60 ) after collecting homologs by BLAST searches and aligning them using the MAFFT method ( 61 ).
- Full pipeline: alignment/mapping [MAFFT]

### A tripartite protein complex promotes DNA transport during natural transformation in Firmicutes. (PNAS 2025)

- DOI: 10.1073/pnas.2511180122 | PMCID: PMC12663950 | PMID: 41259146
- Evidence: They were then aligned using the MAFFT accuracy-oriented E-INS-i method ( 62 ).
- Full pipeline: alignment/mapping [ColabFold, MAFFT] -> visualisation [AlphaFold, ChimeraX]

### Rubisco is slow across the tree of life. (PNAS 2025)

- DOI: 10.1073/pnas.2501433122 | PMCID: PMC12663927 | PMID: 41248286
- Version used: **7.475**
- Evidence: Cluster representatives were then aligned with MAFFT (v7.475, default parameters) ( 66 ) and columns with more than 95% gaps were removed using trimAl (v1.4.rev15, -gt 0.05) ( 67 ).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.475] -> normalisation [UMAP] -> dimensionality reduction/clustering [MAFFT v7.475, UMAP] -> stage not stated [scikit-learn]

### Diffuse pacemaker mechanism with distinctive organization drives pulsation in the octocoral &lt;i&gt;Xenia umbellata&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2500611122 | PMCID: PMC12646211 | PMID: 41218114
- Evidence: Additional phylogenetic analysis related to Dataset S5 can be found in https://doi.org/10.5281/zenodo.17099444 (nexus format) (102) , https://doi.org/10.5281/zenodo.17107413 (MAFFT alignment) ( 103 ).
- Full pipeline: read trimming [Cutadapt v1.15, Trim Galore v0.4.5] -> alignment/mapping [MAFFT] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, R, clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.9.0] -> stage not stated [BLAST, SLEAP]

### GH25 lysozyme mediates tripartite interkingdom interactions and microbial competition on the plant leaf surface. (PNAS 2025)

- DOI: 10.1073/pnas.2510124122 | PMCID: PMC12626018 | PMID: 41201826
- Evidence: 23 ) as well as all bacterial 16S rRNA sequences were aligned using MAFFT Multiple Sequence Alignment Software Version 7.
- Full pipeline: alignment/mapping [MAFFT] -> visualisation [AlphaFold] -> stage not stated [ImageJ v1.53K, Python]

### Methanogenic archaea encoding Pyrrolysine maintain ambiguous amber codon usage. (PNAS 2025)

- DOI: 10.1073/pnas.2517473122 | PMCID: PMC12626013 | PMID: 41196353
- Evidence: Sequences were aligned using MAFFT and trimmed to 90% with TrimAl.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [Cufflinks v2.2.1, DESeq2 v1.20.0, HISAT2 v2.1.0, MAFFT] -> stage not stated [Prokka, RAxML, SciPy]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Evidence: We aligned all potential COI matches using MAFFT ( 84 ) and manually inspected sequences using Mesquite ( 85 ).
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### Apusomonad rhodopsins: A new family of ultraviolet to blue light-absorbing rhodopsin channels. (PNAS 2025)

- DOI: 10.1073/pnas.2510619122 | PMCID: PMC12557545 | PMID: 41082663
- Evidence: The sequences were aligned with MAFFT v.7 ( 92 ) and trimmed with trimAl v.1.2 ( 93 ) using a gap threshold of 0.5 and manual inspection.
- Full pipeline: read trimming [IQ-TREE v1.6.11, MAFFT] -> alignment/mapping [IQ-TREE v1.6.11, MAFFT] -> differential/statistical testing [IQ-TREE v1.6.11] -> structure determination [IQ-TREE v1.6.11] -> stage not stated [AlphaFold, BLAST, GROMACS v4.5.7]

### Temperature adaptation in structure and function in lactate dehydrogenase-A reflects convergent evolution in a few key protein regions. (PNAS 2025)

- DOI: 10.1073/pnas.2517759122 | PMCID: PMC12557798 | PMID: 41071662
- Version used: **7.487**
- Evidence: Sequences were aligned by using MAFFT v7.487 ( 33 ), and the sequence logos were generated by aligning LDH-A sequences to the ggseqlogo v0.2 R package ( 34 ).
- Full pipeline: alignment/mapping [MAFFT v7.487, R] -> simulation/modelling [GROMACS v2021.3, XGBoost] -> machine learning [TensorFlow] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5, VMD]

### A nonenzymatic effector disrupts &lt;i&gt;Bacteroides&lt;/i&gt; cell wall homeostasis via OmpA targeting to mediate interbacterial competition. (PNAS 2025)

- DOI: 10.1073/pnas.2513207122 | PMCID: PMC12541434 | PMID: 41055976
- Evidence: A conservation analysis was constructed based on BF9343_3708 and BF9343_3708 286-end , the sequence was used in blastp against the nonredundant (nr) protein database from the National Center for Biotechnology Information (NCBI) including in the Bacteroides database, and 2 to 5 homologous sequences in different strains were chosen with a cutoff identity 60% and aligned using MAFFT (Version 7.487).
- Full pipeline: alignment/mapping [AlphaFold, BLAST, MAFFT] -> structure determination [AlphaFold] -> stage not stated [IQ-TREE]

### Duplication of a conserved mitochondrial enzyme gene arms parasitoid wasps with venom cytotoxicity and oogenesis regulation. (PNAS 2025)

- DOI: 10.1073/pnas.2512820122 | PMCID: PMC12501140 | PMID: 40996803
- Evidence: Mature proteins without signal peptides or mitochondria-targeting peptides were aligned using MAFFT ( 61 ) v7.490 and reverse-transcribed into codons using pal2nal ( 62 ) v12.
- Full pipeline: quality control [fastp] -> alignment/mapping [MAFFT] -> quantification [fastp] -> structure determination [phytools] -> stage not stated [AlphaFold, BLAST, HMMER]

### SARS-CoV-2 mutant spectrum complexity is an epidemiologically evolvable trait. (PNAS 2025)

- DOI: 10.1073/pnas.2515706122 | PMCID: PMC12501184 | PMID: 40991435
- Version used: **7.453**
- Evidence: Genome sequences were aligned using MAFFT v7.453 software ( 76 ).
- Full pipeline: alignment/mapping [MAFFT v7.453, Nextstrain v2.14.1]

### Transcriptional regulation of thorn tip sclerification in plants. (PNAS 2025)

- DOI: 10.1073/pnas.2510775122 | PMCID: PMC12501164 | PMID: 40986360
- Evidence: For phylogenetic analysis, we aligned MYB protein sequences using MAFFT, constructed a phylogenetic tree with IQTREE, and visualized it on the ITOL platform.
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT] -> visualisation [IQ-TREE, MAFFT]

### Language models reveal a complex sequence basis for adaptive convergent evolution of protein functions. (PNAS 2025)

- DOI: 10.1073/pnas.2418254122 | PMCID: PMC12501123 | PMID: 40986350
- Version used: **7.505**
- Evidence: The orthologs of focal genes were identified by corresponding anchor sequences and then aligned by MAFFT v7.505 ( 75 ).
- Full pipeline: alignment/mapping [MAFFT v7.505] -> differential/statistical testing [IQ-TREE v2.2.5] -> structure determination [IQ-TREE v2.2.5] -> stage not stated [BLAST, OrthoFinder v2.5.5, R]

### Structure of a polymorphic repeat at the &lt;i&gt;CACNA1C&lt;/i&gt; schizophrenia locus. (PNAS 2025)

- DOI: 10.1073/pnas.2415650122 | PMCID: PMC12452837 | PMID: 40932769
- Evidence: To identify similar CACNA1C VNTR sequences, multiple sequence alignments were created using “MAFFT ––text ––globalpair ––maxiterate 1000.” Final alignments for each Type were created using “MAFFT ––op 4 ––text ––globalpair.” A consensus sequence for each Type was defined from the most frequent unit at each alignment position.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [R, VCFtools]

### Convergent evolution of &lt;i&gt;NFP&lt;/i&gt;-facilitated root nodule symbiosis. (PNAS 2025)

- DOI: 10.1073/pnas.2424902122 | PMCID: PMC12452920 | PMID: 40924454
- Evidence: 17 using MAFFT ( 54 ) as previously reported.
- Full pipeline: stage not stated [BEDTools, BLAST, MAFFT, RAxML]

### Specificities of chemosensory receptors in the human gut microbiota. (PNAS 2025)

- DOI: 10.1073/pnas.2508950122 | PMCID: PMC12415202 | PMID: 40857311
- Evidence: Multiple sequence alignments were built using MAFFT ( 72 ), computational docking was carried out using DiffDock ( 73 ), and phylogenetic tree analysis was performed using MrBayes ( 74 ).
- Full pipeline: alignment/mapping [MAFFT, MrBayes] -> stage not stated [AlphaFold]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Version used: **7.475**
- Evidence: Multiple alignments were generated for each orthologous group using MAFFT (v.
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### Coordinated actions of NLR-assembled and glutamate receptor-like calcium channels in plant effector-triggered immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2508018122 | PMCID: PMC12415192 | PMID: 40844808
- Version used: **7.505**
- Evidence: Amino acid sequences were aligned by MAFFT (v7.505) with the auto parameter, using the L-INS-i strategy.
- Full pipeline: quality control [FastQC] -> alignment/mapping [MAFFT v7.505] -> stage not stated [ComplexHeatmap, DESeq2 v1.38.0, R, ggplot2 v3.4.2]

### Evolution of developmental bias explains divergent patterns of phenotypic evolution in two nematode clades. (PNAS 2025)

- DOI: 10.1073/pnas.2507529122 | PMCID: PMC12403097 | PMID: 40828025
- Version used: **7.49**
- Evidence: We aligned the protein sequences using MAFFT v7.49 ( 63 ) and used IQ-TREE 2.2.0.3 ( 64 ) to infer a gene tree for each BUSCO gene, allowing the best-fitting substitution model to be automatically selected ( 65 ).
- Full pipeline: alignment/mapping [IQ-TREE v2.2.0.3, MAFFT v7.49] -> differential/statistical testing [R] -> stage not stated [BUSCO v5.2.2, emmeans v1.10.3, ggplot2 v3.5.1]

### Evolutionarily divergent nidovirus with an exceptionally large genome identified in Pacific oysters undergoing mass mortality. (PNAS 2025)

- DOI: 10.1073/pnas.2426923122 | PMCID: PMC12377751 | PMID: 40758866
- Evidence: The RdRp amino acid sequences were aligned using MAFFT version 7 ( 103 ) and trimmed using Clipkit v.1.4.1 ( 104 ) for phylogenetic reconstruction ( SI Appendix , Extended Materials and Methods ).
- Full pipeline: read trimming [MAFFT, SPAdes v3.15.2, Trimmomatic v0.38] -> alignment/mapping [MAFFT] -> differential/statistical testing [R v4.2.1] -> structure determination [MAFFT] -> stage not stated [BLAST, IQ-TREE v2.2.0.3, InterProScan v5.59]

### Tat-dependent bundling pilus of a halophilic archaeon assembles by a strand donation mechanism and facilitates biofilm formation. (PNAS 2025)

- DOI: 10.1073/pnas.2514980122 | PMCID: PMC12337348 | PMID: 40737320
- Evidence: For phylogenetic analysis, the sequences were aligned using MAFFT web server ( 66 ) with the G-INS-1 option.
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [AlphaFold, ChimeraX, PHENIX]

### Paleobiome dynamics shaped a large Gondwanan plant radiation. (PNAS 2025)

- DOI: 10.1073/pnas.2502129122 | PMCID: PMC12304948 | PMID: 40663609
- Version used: **7.023b**
- Evidence: Sequences in each orthologous cluster were machine-aligned using MAFFT v7.023b ( 83 ) using the “mafft” function in the R package ips ( 84 ) with automatic selection of alignment method.
- Full pipeline: alignment/mapping [MAFFT v7.023b, R] -> dimensionality reduction/clustering [MAFFT v7.023b, R] -> stage not stated [IQ-TREE]

### Sleeping upside-down: Knockdown of a sleep-associated gene induces daytime sleep in the jellyfish &lt;i&gt;Cassiopea&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505074122 | PMCID: PMC12305049 | PMID: 40658847
- Version used: **7.429**
- Evidence: A maximum-likelihood protein alignment of putative nAChRs used MAFFT (version 7.429) and manually filtered following previously described criteria ( 28 ).
- Full pipeline: read trimming [STAR v2.5.3a, Trimmomatic v0.39] -> alignment/mapping [MAFFT v7.429, STAR v2.5.3a] -> normalisation [Bioconductor] -> dimensionality reduction/clustering [Python] -> differential/statistical testing [DESeq2, Python] -> structure determination [IQ-TREE v2.2] -> stage not stated [AlphaFold, BLAST, HMMER]

### Heritable symbiont producing nonribosomal peptide confers extreme heat sensitivity and antifungal protection on its host. (PNAS 2025)

- DOI: 10.1073/pnas.2509873122 | PMCID: PMC12232616 | PMID: 40569380
- Version used: **7.520**
- Evidence: Orthologous proteins were assigned using OrthoFinder (v2.5.5) ( 54 ) and 269 shared single-copy orthologs were aligned using MAFFT (v7.520).
- Full pipeline: read trimming [edgeR] -> alignment/mapping [MAFFT v7.520, OrthoFinder v2.5.5] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [R, survival (R)]

### Homoploid hybridization adds clarity to the origins of octoploid strawberries. (PNAS 2025)

- DOI: 10.1073/pnas.2502814122 | PMCID: PMC12207424 | PMID: 40531871
- Evidence: MAFFT ( 73 ) and IQ-Tree were used to align orthologs and infer gene trees.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [GATK, IQ-TREE, OrthoFinder, SAMtools]

### Predicting high-fitness viral protein variants with Bayesian active learning and biophysics. (PNAS 2025)

- DOI: 10.1073/pnas.2503742122 | PMCID: PMC12184641 | PMID: 40489612
- Evidence: The remaining sequences were aligned using MAFFT ( 49 ).
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [scikit-learn]

### Parallel sensory compensation following independent subterranean colonization by groundwater salamanders (&lt;i&gt;Eurycea&lt;/i&gt;). (PNAS 2025)

- DOI: 10.1073/pnas.2504850122 | PMCID: PMC12168003 | PMID: 40460121
- Version used: **4.475**
- Evidence: Geneious Prime 2024.0.3 (GraphPad Software, LLC) was used to assemble forward and reverse sequences and aligned using MAFFT 4.475 ( 97 ); bases with more than a 1% chance of an error were trimmed from the sequence ends ( SI Appendix , Table S19 ).
- Full pipeline: read trimming [MAFFT v4.475] -> alignment/mapping [MAFFT v4.475] -> differential/statistical testing [R] -> structure determination [phytools v2.3] -> stage not stated [IQ-TREE v2.3.4]

### Anthropogenic iron alters the spring phytoplankton bloom in the North Pacific transition zone. (PNAS 2025)

- DOI: 10.1073/pnas.2418201122 | PMCID: PMC12168011 | PMID: 40455985
- Evidence: Custom-made hmm-profiles, generated using reference protein sequences described in the literature for ISIP1 and ISIP2a ( 63 ) and flavodoxin-clade 2 ( 40 ), were aligned with Multiple Alignment using Fast Fourier Transform (MAFFT) version 7.313 (parameters: – localpair–maxiterate 100–reorder–leavegappyregion) ( 64 ) and masked at positions with 25% or more gaps.
- Full pipeline: alignment/mapping [MAFFT] -> quantification [kallisto] -> stage not stated [HMMER v3.1b, RAxML]

### Horizontal transmission of functionally diverse transposons is a major source of new introns. (PNAS 2025)

- DOI: 10.1073/pnas.2414761122 | PMCID: PMC12130899 | PMID: 40402243
- Evidence: First, we generated multiple sequence alignments for each candidate introner family using MAFFT ( 69 ) and viewed alignments using Aliview ( 70 ).
- Full pipeline: alignment/mapping [BLAST, MAFFT] -> normalisation [TreeTime] -> structure determination [RepeatMasker]

### A vetiver-specific terpene synthase &lt;i&gt;VzTPS9&lt;/i&gt; contributes to the high attractiveness of vetiver to rice stem borer. (PNAS 2025)

- DOI: 10.1073/pnas.2424863122 | PMCID: PMC12107173 | PMID: 40324074
- Evidence: Multiple sequence alignments were performed using MAFFT and trimmed with TRIMAL under default parameters ( 46 , 47 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [HISAT2, MAFFT, MUSCLE, StringTie] -> quantification [RSEM] -> stage not stated [AUGUSTUS, BUSCO v5.0, HMMER, IQ-TREE, OrthoFinder, RepeatMasker]

### Phylogenomics of the tetraploid Hawaiian lobeliads: Implications for their origin, dispersal history, and adaptive radiation. (PNAS 2025)

- DOI: 10.1073/pnas.2421004122 | PMCID: PMC12088406 | PMID: 40324077
- Version used: **7.490**
- Evidence: For each group of homologs, potential nonchimeric paralogs were aligned in MAFFT v.7.490 ( 81 ) using the function mafft in ips v.0.0.11 ( 82 ).
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [BEAST v2.7.5, IQ-TREE v2.2.2.6, R]

### Accurate, scalable, and fully automated inference of species trees from raw genome assemblies using ROADIES. (PNAS 2025)

- DOI: 10.1073/pnas.2500553122 | PMCID: PMC12088440 | PMID: 40314967
- Evidence: ( 40 ), was generated using 250 single-copy BUSCO genes (using Amino acid sequences) and running MAFFT, RAxML-NG, and ASTRAL-MP (in summary mode) sequentially.
- Full pipeline: stage not stated [BUSCO, MAFFT, RAxML, Snakemake]

### Gag proteins encoded by endogenous retroviruses are required for zebrafish development. (PNAS 2025)

- DOI: 10.1073/pnas.2411446122 | PMCID: PMC12067270 | PMID: 40294259
- Evidence: Gag and Pol amino acid sequences were extracted and aligned separately using MAFFT in einsi mode (gap extension penalty = 0) ( 64 ).
- Full pipeline: read trimming [STAR v2.11a, Trimmomatic] -> alignment/mapping [IQ-TREE v2.06, MAFFT, PyMOL, STAR v2.11a, Trimmomatic] -> stage not stated [AlphaFold, BEDTools v2.30.0, BLAST, ColabFold, HMMER v3.3.2, ImageJ, SAMtools v1.18]

### Host use drives convergent evolution in clownfish. (PNAS 2025)

- DOI: 10.1073/pnas.2419716122 | PMCID: PMC12054820 | PMID: 40279387
- Evidence: We aligned the gene sequences of all clownfish species and P. moluccensis with MAFFT [strategy L-INS-I; v.7.841; ( 68 )], and we reconstructed the gene trees with RAxML [GTR+G model, 100 bootstrap replicates; v.8.2.12; ( 69 )].
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [MAFFT, RAxML, SAMtools] -> variant calling [GATK] -> structure determination [MAFFT, RAxML, phytools] -> visualisation [R] -> stage not stated [BEAST, BWA]

### A selfish supergene causes meiotic drive through both sexes in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2421185122 | PMCID: PMC12054836 | PMID: 40267129
- Evidence: For each X-linked gene where Liftoff was able to find full ORFs across all four genomes, we aligned the CDS sequences using MAFFT [v7.505 ( 60 )], and then used iqtree [v1.6.12 ( 61 )] to construct gene trees.
- Full pipeline: alignment/mapping [BEDTools, MAFFT] -> stage not stated [Flye v2.9, Pilon v1.24, R v4.3.0, phytools]

### Fungal Argonaute proteins act in bidirectional cross-kingdom RNA interference during plant infection. (PNAS 2025)

- DOI: 10.1073/pnas.2422756122 | PMCID: PMC12054834 | PMID: 40267130
- Evidence: The alignment was performed by MAFFT and bootstrap was calculated based on 1,000 replicates.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST]

### A diverse single-stranded DNA-annealing protein library enables efficient genome editing across bacterial phyla. (PNAS 2025)

- DOI: 10.1073/pnas.2414342122 | PMCID: PMC12054835 | PMID: 40258142
- Evidence: The sequences were aligned using MAFFT ( 89 ) (version 7) and the tree was constructed with IQ-Tree ( 90 ) (version 1.6.12).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [BLAST, Python]

### Discovery and functional characterization of a bombesin-type neuropeptide signaling system in an invertebrate. (PNAS 2025)

- DOI: 10.1073/pnas.2420966122 | PMCID: PMC12002301 | PMID: 40153458
- Evidence: The precursor sequences ( SI Appendix, Table S2 ) were aligned using the MAFFT online tool ( https://mafft.cbrc.jp/alignment/server/ ) and a phylogenetic tree was generated using FigTree.v1.4.4 ( http://tree.bio.ed.ac.uk/software/figtree/ ).
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [IQ-TREE]

### Structural assembly of the PAS domain drives the catalytic activation of metazoan PASK. (PNAS 2025)

- DOI: 10.1073/pnas.2409685122 | PMCID: PMC11962487 | PMID: 40106358
- Evidence: Full-length metazoan PASK sequences were aligned using MAFFT alignments (MAFFT V7.2).
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> stage not stated [AlphaFold, ChimeraX v1.7, ColabFold, RoseTTAFold]

### Diversification, niche adaptation, and evolution of a candidate phylum thriving in the deep Critical Zone. (PNAS 2025)

- DOI: 10.1073/pnas.2424463122 | PMCID: PMC11962464 | PMID: 40100630
- Version used: **7.49**
- Evidence: These gene families were aligned using MAFFT v7.49 ( 82 ) and trimmed using TrimAL v1.4 ( 59 ).
- Full pipeline: quality control [OrthoFinder v2.5.5] -> read trimming [MAFFT v7.49, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.5, HMMER v3.4, IQ-TREE v2.3.0, MAFFT v7.49, MUSCLE v5.1] -> stage not stated [Cutadapt v4.1, DADA2, Prokka v1.14, QIIME 2 v2023.7]

### Subfunctionalization and epigenetic regulation of a biosynthetic gene cluster in &lt;i&gt;Solanaceae&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2420164122 | PMCID: PMC11874288 | PMID: 39977312
- Version used: **7.490**
- Evidence: Each orthogroup was aligned using MAFFT (v7.490) ( 62 , 63 ).
- Full pipeline: alignment/mapping [MAFFT v7.490] -> quantification [DESeq2] -> normalisation [DESeq2] -> visualisation [Python v3.9] -> stage not stated [IQ-TREE v2.1.4, OrthoFinder v2.5.4]

### Emergence and evolution of heterocyte glycolipid biosynthesis enabled specialized nitrogen fixation in cyanobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2413972122 | PMCID: PMC11804610 | PMID: 39869795
- Evidence: Genes were individually aligned with MAFFT ( 63 ), the alignment was trimmed with trimAl (v1.4.rev15) ( 64 ), and the aligned sequences were concatenated per genome.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> visualisation [IQ-TREE v2.1.2]

### Antiviral Mx proteins have an ancient origin and widespread distribution among eukaryotes. (PNAS 2025)

- DOI: 10.1073/pnas.2416811122 | PMCID: PMC11789081 | PMID: 39854241
- Evidence: We used Clustal Omega ( 128 ) or MAFFT ( 55 ) to align sequences obtained from the same query.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT]

### The &lt;i&gt;Aedes aegypti&lt;/i&gt; mosquito evolves two types of prophenoloxidases with diversified functions. (PNAS 2025)

- DOI: 10.1073/pnas.2413131122 | PMCID: PMC11761970 | PMID: 39808654
- Evidence: Sequence alignments were generated using MAFFT ( 83 , 84 ).
- Full pipeline: alignment/mapping [MAFFT] -> simulation/modelling [GROMACS] -> stage not stated [AlphaFold, AutoDock Vina, ChimeraX v1.8]

### Conservation of symbiotic signaling since the most recent common ancestor of land plants. (PNAS 2025)

- DOI: 10.1073/pnas.2408539121 | PMCID: PMC11725925 | PMID: 39739802
- Version used: **7.520**
- Evidence: A set of 37 protein sequences was aligned using MAFFT v7.520 with the E-INS-i method ( 41 ).
- Full pipeline: quality control [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> read trimming [BEDTools, Cutadapt, FastQC, SAMtools, Trim Galore] -> alignment/mapping [MAFFT v7.520] -> differential/statistical testing [R v4.1.2, edgeR] -> structure determination [HMMER v3.4, IQ-TREE v2.2.2.3] -> stage not stated [ImageJ]

### The interaction of &lt;i&gt;Serratia&lt;/i&gt; bacteria and harmonine in harlequin ladybird confers an interspecies competitive edge. (PNAS 2025)

- DOI: 10.1073/pnas.2417873121 | PMCID: PMC11745345 | PMID: 39793111
- Version used: **7.47133**
- Evidence: A total of 1,106 single-copy orthogroups were identified using OrthoFinder version 2.5.5, and the protein sequences were extracted with seqkit v2.2.032, independently aligned by MAFFT v7.47133, and filtered through trimAl v1.434 with default parameters.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, MAFFT v7.47133, OrthoFinder v2.5.5] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2 v1.35.0] -> stage not stated [Canu v1.6, Cutadapt v2.7, DADA2, IQ-TREE v1.6.1035, Kraken2, QIIME 2, RAxML, fastp v0.20.0, survival (R)]

### Uncovering ParB-dependent and -independent subclasses of T-dioxygenases from bacteriophage. (PNAS 2026)

- DOI: 10.1073/pnas.2522060123 | PMCID: PMC13229309 | PMID: 42189983
- Evidence: Phylogenetic tree of ( B ) ParBs and ( C ) 5mYOXs generated using FastTree algorithm from a MAFFT calculated MSA in Geneious Prime.
- Full pipeline: alignment/mapping [AlphaFold] -> stage not stated [MAFFT]

### Novel Knotted Solenoid fold with order-shifted coil arrangement leads to nontrivial 3&lt;sub&gt;1&lt;/sub&gt; topology. (PNAS 2026)

- DOI: 10.1073/pnas.2525920123 | PMCID: PMC13123833 | PMID: 42018416
- Evidence: Subsequently, a multiple sequence alignment (MSA) was generated using MAFFT ( 63 ), which was then used with HMMER ( 41 ) to perform sequential searches across the entire AlphaFold database, e-value cutoff: 10 − 3 .
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> simulation/modelling [GROMACS v2023.1] -> stage not stated [AlphaFold]

### Ancient environmental genome reveals a migratory brown bear individual in Early Holocene Scandinavia. (PNAS 2026)

- DOI: 10.1073/pnas.2527944123 | PMCID: PMC13099568 | PMID: 41973920
- Version used: **7.526**
- Evidence: For the phylogenetic tree and haplotype network, the FISK2006 mitochondrial genome was aligned with the 46 published mitochondrial genomes using MAFFT v7.526 ( 59 ) and inspected in SeaView v5.0.5 ( 58 ).
- Full pipeline: read trimming [Cutadapt v2.3, fastp v0.24] -> alignment/mapping [ANGSD v0.940, BCFtools v1.20, MAFFT v7.526, RepeatMasker v2.0.1] -> variant calling [BCFtools v1.20, MAFFT v7.526] -> registration [BCFtools v1.20] -> visualisation [R v4.3] -> stage not stated [BEDTools v2.29.2, IQ-TREE v2.4.0, Kraken2, SAMtools]

### A secreted citrus protease cleaves an outer membrane protein of the Huanglongbing pathogen. (PNAS 2026)

- DOI: 10.1073/pnas.2528641123 | PMCID: PMC13079941 | PMID: 41945448
- Version used: **7.490**
- Evidence: MUSCLE v5.1 ( 56 ) or MAFFT v7.490 ( 57 ) alignments were generated, as indicated, of FASTA amino acid sequences.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, MAFFT v7.490, MUSCLE v5.1, Trimmomatic v0.39] -> quantification [Bioconductor, DESeq2] -> normalisation [Bioconductor, DESeq2] -> stage not stated [AlphaFold, ChimeraX, HMMER, ImageJ]

### Mycoviruses confer hypovirulence but enhance antifungal volatile organic compound production in a phytopathogenic fungus. (PNAS 2026)

- DOI: 10.1073/pnas.2526822123 | PMCID: PMC13080020 | PMID: 41941638
- Version used: **7.0**
- Evidence: Phylogenetic trees were constructed using MAFFT 7.0 with the L-INS-i method to align viral protein sequences ( 51 ), and all analyzed mycoviral sequences are provided in figshare ( https://doi.org/10.6084/m9.figshare.30024784.v2 ).
- Full pipeline: alignment/mapping [ChimeraX, MAFFT v7.0] -> normalisation [ComplexHeatmap] -> dimensionality reduction/clustering [ComplexHeatmap, HMMER v3.3.2] -> visualisation [ChimeraX, ComplexHeatmap, ImageJ] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.2.6]

### Spider venom phospholipase D toxin structure: Interfacial binding site, mechanism, activation, and head group preference. (PNAS 2026)

- DOI: 10.1073/pnas.2513997123 | PMCID: PMC13079978 | PMID: 41941646
- Evidence: Sequences were aligned using MAFFT ( 70 ), curated to exclude >90% identity with MMseqs2 ( 71 ) and visualized using WebLogo V2.8.3 ( 72 ) ( https://weblogo.berkeley.edu/ ).
- Full pipeline: alignment/mapping [MAFFT] -> normalisation [CCP4] -> structure determination [REFMAC] -> visualisation [ChimeraX, MAFFT]

### Decoding antibody response to MERS-CoV in wild dromedary camels. (PNAS 2026)

- DOI: 10.1073/pnas.2513716123 | PMCID: PMC12913009 | PMID: 41662528
- Version used: **7.310**
- Evidence: RBD sequences were aligned to MERS-CoV reference HCoV-EMC/2012 sequence ( YP_009047204.1 ) using MAFFT v7.310 program.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.4, MAFFT v7.310, MUSCLE v3.8.1551] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.3, PyMOL] -> stage not stated [CCP4]

### A nuclear CobW/WW-domain factor represses the CO&lt;sub&gt;2&lt;/sub&gt;-concentrating mechanism in the green alga &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2518136123 | PMCID: PMC12891040 | PMID: 41637450
- Evidence: Multiple sequence alignment was performed using MAFFT version 7 online service ( 39 ).
- Full pipeline: alignment/mapping [MAFFT] -> quantification [ImageJ] -> normalisation [ImageJ]

### Germline fate determination by a single ARGONAUTE protein in &lt;i&gt;Ectocarpus&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2518712123 | PMCID: PMC12867755 | PMID: 41604268
- Evidence: Sequence alignment (MAFFT L-INS-i), trimming (BMGE), model selection, and tree inference (SPR; SH-like aLRT support) were performed within the OneClick workflow.
- Full pipeline: quality control [Trimmomatic] -> read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT, STAR, featureCounts] -> quantification [DESeq2, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### Soluble adenylyl cyclase in nonmammalian sperm is directly controlled by pH, not by HCO&lt;sub&gt;3&lt;/sub&gt;&lt;sup&gt;-&lt;/sup&gt; or Ca&lt;sup&gt;2&lt;/sup&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2505026123 | PMCID: PMC12867704 | PMID: 41591904
- Evidence: Candidate sAC proteins were identified based on homology and validated through phylogenetic analysis (MAFFT alignment, PhyML tree building).
- Full pipeline: alignment/mapping [AlphaFold v2.2.4, ColabFold v1.5.2, MAFFT] -> stage not stated [BLAST, SciPy v1.15.1, statsmodels v0.14.4]

### The Japanese Archipelago sheltered cave lions, not tigers, during the Late Pleistocene. (PNAS 2026)

- DOI: 10.1073/pnas.2523901123 | PMCID: PMC12890994 | PMID: 41587328
- Version used: **7.505**
- Evidence: ...losa ), six modern tigers, two leopards ( Panthera pardus ), two modern lions, 11 American lions, and 30 cave lions ( SI Appendix , Table S7 ), using MAFFT v7.505 ( 82 ) with default setting.
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [ANGSD, BWA v0.7.17, SAMtools v1.11] -> stage not stated [MAFFT v7.505, Python]

### STING single amino acid polymorphisms modulate iridovirus immune evasion and pathogenicity spectrum. (PNAS 2026)

- DOI: 10.1073/pnas.2523268123 | PMCID: PMC12846800 | PMID: 41576079
- Evidence: Phylogenetic trees were constructed using mitochondrial genes or STING protein sequences, with alignments performed via MAFFT.
- Full pipeline: alignment/mapping [MAFFT]

### Molecular structure of the ESCRT-III-based archaeal CdvAB cell division machinery. (PNAS 2026)

- DOI: 10.1073/pnas.2525941123 | PMCID: PMC12818579 | PMID: 41543908
- Evidence: Aligned with MAFFT online in auto mode ( 26 ).
- Full pipeline: alignment/mapping [MAFFT, PyMOL] -> structure determination [Coot, PHENIX, RELION] -> visualisation [ChimeraX v1.7.1] -> stage not stated [AlphaFold, MotionCor2]

### A prenylated dsRNA sensor protects against severe COVID-19. (Science 2021)

- DOI: 10.1126/science.abj3624 | PMCID: PMC7612834 | PMID: 34581622
- Version used: **7.453**
- Evidence: Matches were aligned using MAFFT v7.453 and inspected for covering all regions of the probe.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, SAMtools] -> alignment/mapping [BEDTools, MAFFT v7.453, SAMtools, STAR] -> quantification [BEDTools, MultiQC] -> differential/statistical testing [Bioconductor, R, SAMtools] -> stage not stated [BLAST, DESeq2, HMMER v3.2.1, HOMER]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Evidence: Sequencing read mapping was performed with Bowtie, with alignment using MAFFT and visual inspection using Geneious Prime (all version numbers given below).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### SARS-CoV-2 within-host diversity and transmission. (Science 2021)

- DOI: 10.1126/science.abg0821 | PMCID: PMC8128293 | PMID: 33688063
- Evidence: The resulting set, along with the reference genome Wuhan-Hu-1 (RefSeq ID NC_045512 ), were aligned using MAFFT ( 64 ), with some manual improvement of the algorithmic alignment and removal of problematic sequences performed as a postprocessing step.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT] -> structure determination [IQ-TREE, RAxML] -> stage not stated [Docker, Pangolin]

### Broad and potent activity against SARS-like viruses by an engineered human monoclonal antibody. (Science 2021)

- DOI: 10.1126/science.abf4830 | PMCID: PMC7963221 | PMID: 33495307
- Evidence: ( A ) Phylogenetic tree of 57 sarbecoviruses constructed via MAFFT (Multiple Alignment using Fast Fourier Transform) and maximum likelihood analysis of RBD subdomain 1 amino acid sequences extracted from the European Nucleotide Archive and GISAID database.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [Pangolin]

### Unadjuvanted intranasal spike vaccine elicits protective mucosal immunity against sarbecoviruses. (Science 2022)

- DOI: 10.1126/science.abo2523 | PMCID: PMC9798903 | PMID: 36302057
- Evidence: Sequence alignment was performed with MAFFT in JalView (v2.11.2.3).
- Full pipeline: alignment/mapping [MAFFT]

### The molecular epidemiology of multiple zoonotic origins of SARS-CoV-2. (Science 2022)

- DOI: 10.1126/science.abp8337 | PMCID: PMC9348752 | PMID: 35881005
- Version used: **7.453**
- Evidence: Genomes were aligned using MAFFT v7.453 ( 58 ) to the SARS-CoV-2 reference genome (Wuhan/Hu-1/2019) and 388 sites were masked at the 5′ and 3′ ends and at sites based on De Maio et al .
- Full pipeline: alignment/mapping [MAFFT v7.453] -> stage not stated [IQ-TREE v2.0.7, TreeTime v0.8.1]

### Broadly neutralizing antibodies target the coronavirus fusion peptide. (Science 2022)

- DOI: 10.1126/science.abq3773 | PMCID: PMC9348754 | PMID: 35857439
- Version used: **7.450**
- Evidence: Performed using MAFFT v7.450 using a BLOSUM62 scoring matrix and the L-INS-I algorithm.
- Full pipeline: stage not stated [MAFFT v7.450]

### PIM1 controls GBP1 activity to limit self-damage and to guard against pathogen infection. (Science 2023)

- DOI: 10.1126/science.adg2253 | PMCID: PMC7615196 | PMID: 37797010
- Evidence: Protein sequences were aligned with MAFFT ( 74 ), and incomplete data was removed with MaxAlign v1.1 ( 75 ).
- Full pipeline: alignment/mapping [MAFFT] -> quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [ChimeraX v0.93, MACS2, PHENIX, Topaz]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: Open reading frames were identified in all ccDNA sequences and the corresponding amino acid sequences were realigned using MAFFT ( 54 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

### Brainwide silencing of prion protein by AAV-mediated delivery of an engineered compact epigenetic editor. (Science 2024)

- DOI: 10.1126/science.ado7082 | PMCID: PMC11875203 | PMID: 38935715
- Evidence: A MAFFT multiple sequence alignment was performed using the FFT-NS-i (standard) strategy with a maximum of two iterations ( 104 ) and then used for phylogenetic tree construction implementing IQ-TREE software ( 105 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT, STAR v2.7.1a, featureCounts v1.6.2, minimap2 v2.26] -> quantification [STAR v2.7.1a, featureCounts v1.6.2] -> differential/statistical testing [DESeq2] -> visualisation [NumPy v1.26.3, seaborn v0.13.2] -> stage not stated [BEDTools v2.31.0, CellProfiler, QuPath]

### TIGR-Tas: A family of modular RNA-guided DNA-targeting systems in prokaryotes and their viruses. (Science 2025)

- DOI: 10.1126/science.adv9789 | PMCID: PMC12045711 | PMID: 40014690
- Evidence: Repeats and approximately 30 nt of flanking sequences were extracted, aligned using MAFFT ( 89 ), and manually adjusted to refine the alignment.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, MAFFT, PyMOL] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [MAFFT, PHENIX] -> stage not stated [CTFFIND, ColabFold, Coot, HMMER, MotionCor2, RELION, Topaz]

