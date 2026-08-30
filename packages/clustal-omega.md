# Clustal Omega

- **Category:** phylogenetics
- **Papers in survey:** 257
- **Journals:** PNAS (167), Nature (67), Cell (19), Science (4)
- **Years:** 2021 (23), 2022 (45), 2023 (47), 2024 (52), 2025 (67), 2026 (23)
- **Versions named:** 1.2.4 (11), 1.2.2 (9), 1.2.3 (4), 2.1 (1), 2.0.12 (1), 1.2.0 (1), 1.2 (1)
- **Pipeline stages it appears in:** alignment/mapping (226), visualisation (15), dimensionality reduction/clustering (8), structure determination (2), read trimming (2), differential/statistical testing (1)

## Papers

### The epitope arrangement on flavivirus particles contributes to Mab C10's extraordinary neutralization breadth across Zika and dengue viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.010 | PMCID: PMC8724787 | PMID: 34852239
- Evidence: Multiple sequence alignments were calculated using Clustal W and Clustal C version 2 on the EBI server.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CCP4, ChimeraX v1.2.5, PHENIX v1.14, PyMOL, RELION v2.1, UCSF Chimera v1.11.2]

### Bacterial Vipp1 and PspA are members of the ancient ESCRT-III membrane-remodeling superfamily. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.041 | PMCID: PMC8281802 | PMID: 34166615
- Evidence: Figure S5 Vipp1 secondary structure assignment and sequence alignment with PspA and ESCRT-III, related to Figure 2 Sequences were aligned using Clustal Omega and include Vipp1/IM30 Nostoc punctiforme (Uniprot code B2J6D9 ), Vipp2 Nostoc punctiforme (Uniprot code B2J6E0), Escherichia coli PspA (Uniprot code P0AFM6 ), Synechocystis sp .
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE, MotionCor2] -> stage not stated [GROMACS, HMMER, ImageJ, PHENIX, RELION v3.1, VMD]

### Identification of novel bat coronaviruses sheds light on the evolutionary origins of SARS-CoV-2 and related viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.008 | PMCID: PMC8188299 | PMID: 34147139
- Version used: **1.2.2**
- Evidence: ...ious v2021.0.1 The Biomatters development team https://www.geneious.com/ MAFFT v7.450 Nakamura et al., 2018 https://mafft.cbrc.jp/alignment/software/ Clustal Omega v1.2.2 Sievers et al., 2011 http://www.clustal.org/omega/ BLAST Camacho et al., 2009 https://blast.ncbi.nlm.nih.gov/Blast.cgi SAMtools v1.10 Li et al., 2009 http://samtools.sourceforge.net/ Figtree v1.4.4 http://tree.bio.ed.ac.uk/softwa...
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2, MAFFT v7.450] -> stage not stated [BLAST, Bowtie2 v2.4.1, PyMOL v2.4.0a, RAxML, SAMtools v1.10]

### High-resolution profiling of pathways of escape for SARS-CoV-2 spike-binding antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.045 | PMCID: PMC8096189 | PMID: 34010620
- Evidence: ...https://github.com/kassambara/rstatix coin http://coin.r-forge.r-project.org/ Custom code This paper https://github.com/meghangarrett/Spike-Phage-DMS Clustal Omega https://www.ebi.ac.uk/Tools/msa/clustalo/ GraphPad Prism version 9 GraphPad Software N/A Other Protein A Dynabeads Invitrogen Cat. # 10002D Protein G Dynabeads Invitrogen Cat. # 10004D 1.1 mL 96-deep-well polypropylene U-bottom plate Br...
- Full pipeline: stage not stated [Clustal Omega, Nextflow, R v4.0.2, SAMtools, ggpubr, tidyverse, xarray]

### Simultaneous binding of Guidance Cues NET1 and RGM blocks extracellular NEO1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.045 | PMCID: PMC8063088 | PMID: 33740419
- Evidence: ...and Schuck, 2006 ) http://www.analyticalultracentrifugation.com/default.htm ImageJ ( Schneider et al., 2012 ) https://imagej.nih.gov/ij/download.html Clustal Omega ( Chojnacki et al., 2017 ) https://www.ebi.ac.uk/Tools/msa/clustalo/ GraphPad Prism GraphPad Software http://www.graphpad.com/scientific-software/prism/ ASTRA 6 Wyatt https://www.wyatt.com/products/software/astra.html EPU FEI https://ww...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [MotionCor2] -> stage not stated [CTFFIND v4.1, Clustal Omega, ImageJ, PHENIX, PyMOL, RELION v3.1, UCSF Chimera]

### G3BPs tether the TSC complex to lysosomes and suppress mTORC1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.024 | PMCID: PMC7868890 | PMID: 33497611
- Evidence: Visualization of sequence alignments was done using Texshade based on a ClustalW alignment of the whole protein sequences.
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CellProfiler, RSEM] -> visualisation [Clustal Omega] -> stage not stated [BCFtools, BLAST, ImageJ v1.50b, MACS2, Python, R, SAMtools, TrackMate]

### A family of conserved bacterial virulence factors dampens interferon responses by blocking calcium signaling. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.028 | PMCID: PMC9596379 | PMID: 35568036
- Evidence: FASTA files for the top 100 most similar proteins were extracted, and aligned with Clustal Omega ( Sievers and Higgins, 2018 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [DESeq2 v1.28.0, GSEA, R] -> differential/statistical testing [GSEA] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BLAST, ImageJ, Nextflow, RSEM, Singularity]

### Cryo-ET of Env on intact HIV virions reveals structural variation and positioning on the Gag lattice. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.013 | PMCID: PMC9000915 | PMID: 35123651
- Evidence: Multiple sequence alignments were carried out using the Clustal Omega web service ( Madeira et al., 2019 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ChimeraX, Coot, EMAN2, IMOD v4.10.15, ImageJ, RELION v2.1, UCSF Chimera]

### De novo protein identification in mammalian sperm using in situ cryoelectron tomography and AlphaFold2 docking. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.017 | PMCID: PMC10842264 | PMID: 37865089
- Evidence: Sequence alignment was performed using Clustal Omega 32 server and displayed in Jalview 66 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler v4.4.1] -> differential/statistical testing [Bioconductor] -> visualisation [IMOD] -> stage not stated [AlphaFold, ChimeraX, ColabFold, Coot v0.9.8.1, MotionCor2, R, RELION, UCSF Chimera]

### Targeting Ras-, Rho-, and Rab-family GTPases via a conserved cryptic pocket. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.017 | PMCID: PMC11531380 | PMID: 39255801
- Evidence: Bioinformatics Multiple protein sequence alignments were conducted with Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CCP4] -> simulation/modelling [VMD] -> structure determination [PHENIX]

### Mosaic sarbecovirus nanoparticles elicit cross-reactive responses in pre-vaccinated animals. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.052 | PMCID: PMC11460329 | PMID: 39197450
- Evidence: 14 (D) Phylogenetic tree of selected sarbecoviruses calculated using a Jukes-Cantor generic distance model using Geneious Prime 2023.1.2 based on amino acid sequences of RBDs aligned using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega]

### A replisome-associated histone H3-H4 chaperone required for epigenetic inheritance. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.006 | PMCID: PMC11380579 | PMID: 39094570
- Evidence: ...edical School O2 computing cluster N/A In-house mass spectrometry data analysis software 109 N/A ChatGPT3.5 (March 24 version) OpenAI RRID:SCR_023775 Clustal Omega UniProt RRID:SCR_001591 JalView University of Dundee RRID:SCR_006459 AcquireMP Refeyn, Ltd N/A DiscoverMP Refeyn, Ltd N/A ASTRA, version 7.3.2.21 Wyatt RRID:SCR_016255 Bowtie2 John Hopkins University RRID:SCR_016368 MACS Dana Farber Can...
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> dimensionality reduction/clustering [ChimeraX, Clustal Omega, ColabFold, UCSF Chimera] -> stage not stated [AlphaFold, Bowtie2, MACS2]

### Minimal and hybrid hydrogenases are active from archaea. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.032 | PMCID: PMC11216029 | PMID: 38866018
- Version used: **1.2.2**
- Evidence: 107 N/A Clustal Omega v1.2.2 Sievers and Higgins 108 N/A DIAMOND v0.9.31 Buchfink et al.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [Nextflow] -> stage not stated [AlphaFold, BLAST, Clustal Omega v1.2.2, HMMER v3.2.1, IQ-TREE v1.6.12, MAFFT v7.304, R, StringTie v2.2.1]

### A pseudoautosomal glycosylation disorder prompts the revision of dolichol biosynthesis. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.041 | PMCID: PMC11250103 | PMID: 38821050
- Evidence: (D) Conservation of DHRSX amino acids affected by variants, and % sequence identity of the entire protein sequences as determined by ClustalW.
- Full pipeline: stage not stated [AlphaFold, Clustal Omega, ImageJ]

### Multiple independent acquisitions of ACE2 usage in MERS-related coronaviruses. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.031 | PMCID: PMC12360793 | PMID: 39922191
- Evidence: Bioinformatic and structural analysis Sequence alignments of different bats ACE2 were performed using either the MUSCLE algorithm by MEGA-X (version 10.1.8) or ClustalW software ( https://www.genome.jp/tools-bin/clustalw ) with slight position adjustment to align indels.
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [RELION] -> structure determination [IQ-TREE, RELION, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PHENIX, Topaz]

### Designed mosaic nanoparticles enhance cross-reactive immune responses in mice. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.015 | PMCID: PMC11845252 | PMID: 39855201
- Evidence: We first obtained a set of 246 non-redundant sarbecovirus RBDs from the NCBI database, 39 aligned these with the WA1 SARS-CoV-2 RBD using ClustalW, 40 , 41 and filtered the alignment for residues 331–531 of the WA1 SARS-CoV-2 spike since these were the WA1 spike residues used for RBD display in DMS experiments.
- Full pipeline: alignment/mapping [Clustal Omega]

### Structural and functional analysis of the Nipah virus polymerase complex. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.021 | PMCID: PMC11813165 | PMID: 39837328
- Evidence: 28 https://loschmidt.chemi.muni.cz/caverweb/ Clustal Omega Sievers et al.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.5, Clustal Omega, Coot v0.9, MotionCor2 v1.6.4, PHENIX v1.20.1, PyMOL v2.5.5, RELION v3.1.1, UCSF Chimera v1.15]

### Phages communicate across species to shape microbial ecosystems. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.004 | PMCID: PMC13220667 | PMID: 41923642
- Evidence: A multiple sequence alignment (MSA) of AimR protein sequences was performed using ClustalW in Ugene (Unipro).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CCP4, IQ-TREE, R, ggplot2, ggpubr, tidyverse]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Evidence: 209 https://thebiogrid.org/ Clustal Omega Madeira et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### The structure of neurofibromin isoform 2 reveals different functional states. (Nature 2021)

- DOI: 10.1038/s41586-021-04024-x | PMCID: PMC8580823 | PMID: 34707296
- Evidence: 4 , with multiple sequence alignments done in Jalview 51 using Clustal W colouring 52 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX v1.19, UCSF Chimera v1.15] -> stage not stated [ChimeraX, MotionCor2 v2.1.1, RELION v3.1.1]

### Rapid and stable mobilization of CD8<sup>+</sup> T cells by SARS-CoV-2 mRNA vaccine. (Nature 2021)

- DOI: 10.1038/s41586-021-03841-4 | PMCID: PMC8426185 | PMID: 34320609
- Version used: **1.2.2**
- Evidence: Sequence alignment Sequence homology analyses were performed in Geneious Prime 2020.0.3 ( https://www.geneious.com/ ) using Clustal Omega 1.2.2 alignment with default settings 22 .
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2] -> dimensionality reduction/clustering [Bioconductor, R v4.0.2] -> stage not stated [MACS2]

### Close relatives of MERS-CoV in bats use ACE2 as their functional receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-05513-3 | PMCID: PMC9734910 | PMID: 36477529
- Evidence: Bioinformatic and computational analyses Protein sequence alignment was performed using the MUSCLE algorithm by MEGA-X software (v.10.1.8) or ClustalW ( https://www.genome.jp/tools-bin/clustalw ).
- Full pipeline: alignment/mapping [CTFFIND, Clustal Omega, MUSCLE] -> structure determination [Coot v0.9.4, PHENIX v1.19, RELION, UCSF Chimera v1.15] -> stage not stated [ChimeraX v1.1, MotionCor2 v1.3.0]

### Structural basis of tankyrase activation by polymerization. (Nature 2022)

- DOI: 10.1038/s41586-022-05449-8 | PMCID: PMC9712121 | PMID: 36418402
- Evidence: Phylogenetic analyses Multiple sequence alignments were generated with Clustal Omega 60 using the web services from the EMBL-EBI 61 (version January 2021).
- Full pipeline: alignment/mapping [Clustal Omega, EMAN2 v2.31] -> quantification [ImageJ] -> normalisation [ImageJ] -> structure determination [PHENIX v1.18.2] -> visualisation [ChimeraX v1.3] -> stage not stated [CellProfiler, Coot, MotionCor2, RELION v2.10, UCSF Chimera v1.14]

### Medin co-aggregates with vascular amyloid-β in Alzheimer's disease. (Nature 2022)

- DOI: 10.1038/s41586-022-05440-3 | PMCID: PMC9712113 | PMID: 36385530
- Evidence: Sequence alignment and structural modelling Sequence alignment of medin and Aβ42 was performed using Clustal Omega 64 .
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [Fiji v2.3, ImageJ v2.3, SCENIC, WGCNA]

### Nuclear-embedded mitochondrial DNA sequences in 66,083 human genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05288-7 | PMCID: PMC9630118 | PMID: 36198798
- Evidence: (3) The contigs were then aligned against mitochondrial reference genome 85 using Blat 63 and Clustal Omega 86 .
- Full pipeline: alignment/mapping [Clustal Omega, Python, SAMtools, Strelka v2.4.7, minimap2] -> variant calling [Strelka v2.4.7] -> dimensionality reduction/clustering [GCTA, UMAP] -> differential/statistical testing [R] -> machine learning [GCTA] -> visualisation [Matplotlib] -> stage not stated [BEDTools, PLINK v1.90]

### Phosphorylation of muramyl peptides by NAGK is required for NOD2 activation. (Nature 2022)

- DOI: 10.1038/s41586-022-05125-x | PMCID: PMC9477735 | PMID: 36002575
- Evidence: A Clustal Omega alignment was performed to determine the conservation of human NAGK structure-based active site residues.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [R v4.1.0]

### Endocytosis in the axon initial segment maintains neuronal polarity. (Nature 2022)

- DOI: 10.1038/s41586-022-05074-5 | PMCID: PMC9433327 | PMID: 35978188
- Evidence: ( g ) Phylogenetic tree analysis created using Clustal Omega multiple sequence alignments.
- Full pipeline: alignment/mapping [Clustal Omega]

### PI3K drives the de novo synthesis of coenzyme A from vitamin B5. (Nature 2022)

- DOI: 10.1038/s41586-022-04984-8 | PMCID: PMC9352595 | PMID: 35896750
- Evidence: Sequences were aligned using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ]

### Structure of the Dicer-2-R2D2 heterodimer bound to a small RNA duplex. (Nature 2022)

- DOI: 10.1038/s41586-022-04790-2 | PMCID: PMC9279153 | PMID: 35768503
- Evidence: The figure was prepared using Clustal Omega ( http://www.ebi.ac.uk/Tools/msa/clustalo ) and ESPript3 ( http://espript.ibcp.fr/ESPript/ESPript ).
- Full pipeline: structure determination [ChimeraX] -> stage not stated [AlphaFold, Clustal Omega, PHENIX, RELION]

### Grey wolf genomic history reveals a dual ancestry of dogs. (Nature 2022)

- DOI: 10.1038/s41586-022-04824-9 | PMCID: PMC9279150 | PMID: 35768506
- Version used: **1.2.4**
- Evidence: We aligned all sequences using Clustal Omega (v1.2.4) 81 .
- Full pipeline: alignment/mapping [BWA, Clustal Omega v1.2.4, Picard, SAMtools v1.9] -> variant calling [BCFtools, GATK, Picard] -> dimensionality reduction/clustering [R] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b]

### GTSF1 accelerates target RNA cleavage by PIWI-clade Argonaute proteins. (Nature 2022)

- DOI: 10.1038/s41586-022-05009-0 | PMCID: PMC9385479 | PMID: 35772669
- Version used: **1.2.4**
- Evidence: Protein sequences were aligned using Clustal Omega (1.2.4); unrooted tree was constructed using randomized axelerated maximum likelihood (RAxML 1.0.0) with default parameters 84 and visualized in Interactive Tree of Life 85 .
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4, HTSeq v0.9.1, RAxML v1.0.0, SAMtools v1.8, STAR v2.3] -> quantification [HTSeq v0.9.1] -> visualisation [Clustal Omega v1.2.4, RAxML v1.0.0] -> stage not stated [Bowtie2 v2.5]

### Discovery of non-squalene triterpenes. (Nature 2022)

- DOI: 10.1038/s41586-022-04773-3 | PMCID: PMC9177416 | PMID: 35650436
- Version used: **2.0.12**
- Evidence: Phylogenetic analysis of TvTS and MpMS To characterize the evolutionary relationships of TvTS, MpMS and CgCS, 56 characterized fungal chimeric class I TSs were selected and multiple-sequence alignment was performed using ClustalW (version 2.0.12).
- Full pipeline: alignment/mapping [Clustal Omega v2.0.12, RELION] -> visualisation [PyMOL] -> stage not stated [AlphaFold, AutoDock Vina, CTFFIND, PHENIX v1.19.2, UCSF Chimera]

### Intron-mediated induction of phenotypic heterogeneity. (Nature 2022)

- DOI: 10.1038/s41586-022-04633-0 | PMCID: PMC9068511 | PMID: 35444278
- Evidence: 3e ), previously published sequencing data for 1,011 isolates 57 were multiple-sequence aligned using Clustal Omega 58 and visualized using MSA-BIOJS 59 .
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, TopHat, featureCounts] -> quantification [featureCounts] -> visualisation [Clustal Omega] -> stage not stated [ImageJ]

### Visualizing protein breathing motions associated with aromatic ring flipping. (Nature 2022)

- DOI: 10.1038/s41586-022-04417-6 | PMCID: PMC8866124 | PMID: 35173330
- Evidence: Comparison of JIP1-SH3 to other human SH3 domains The sequences of 320 human SH3 domains were obtained 33 , aligned using Clustal Omega 53 and categorized according to the identity of the amino acid at the position of Y526 in JIP1-SH3.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, VMD]

### Broadly neutralizing antibodies target a haemagglutinin anchor epitope. (Nature 2022)

- DOI: 10.1038/s41586-021-04356-8 | PMCID: PMC8828479 | PMID: 34942633
- Evidence: Consensus sequence analysis was performed using WebLogo 41 and sequence alignments were determined using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION, UCSF Chimera] -> simulation/modelling [GROMACS, PLUMED] -> visualisation [RELION] -> stage not stated [Jupyter, PHENIX, R, Seurat]

### Unraveling the functional dark matter through global metagenomics. (Nature 2023)

- DOI: 10.1038/s41586-023-06583-7 | PMCID: PMC10584684 | PMID: 37821698
- Evidence: For each cluster, a multiple-sequence alignment (MSA) was calculated using Clustal Omega 42 .
- Full pipeline: alignment/mapping [Clustal Omega, Python] -> dimensionality reduction/clustering [Clustal Omega] -> differential/statistical testing [R] -> stage not stated [AlphaFold, HMMER v3.1, ggplot2]

### The sex-specific factor SOA controls dosage compensation in Anopheles mosquitoes. (Nature 2023)

- DOI: 10.1038/s41586-023-06641-0 | PMCID: PMC10620080 | PMID: 37769784
- Evidence: Protein and DNA alignments were created using Clustal Omega.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.0] -> alignment/mapping [Bowtie2 v2.4.5, Clustal Omega, Cutadapt v4.0, STAR v2.7.3a, deepTools v3.1.0] -> differential/statistical testing [BEDTools v2.29.2, DESeq2 v1.26.0] -> visualisation [STAR v2.7.3a] -> stage not stated [MACS2, R, RepeatMasker]

### Bacterial pathogens deliver water- and solute-permeable channels to plant cells. (Nature 2023)

- DOI: 10.1038/s41586-023-06531-5 | PMCID: PMC10511319 | PMID: 37704725
- Evidence: AvrE-family protein sequence alignments Sequences of E. amylovora DspE, P. carotovorum DspE, Pst DC3000 AvrE and P. stewartii WtsE were aligned using Clustal Omega 52 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [AlphaFold, ColabFold] -> stage not stated [PyMOL v1.8.0.4]

### TRIM5α restricts poxviruses and is antagonized by CypA and the viral protein C6. (Nature 2023)

- DOI: 10.1038/s41586-023-06401-0 | PMCID: PMC10447239 | PMID: 37558876
- Evidence: Amino acid sequences were aligned using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ImageJ]

### Small protein modules dictate prophage fates during polylysogeny. (Nature 2023)

- DOI: 10.1038/s41586-023-06376-y | PMCID: PMC10432266 | PMID: 37495698
- Evidence: ( a ) Protein sequence alignment (ClustalW) showing TF 72 and TF 63 .
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, Prokka v1.11, Python]

### Axonemal structures reveal mechanoregulatory and disease mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-06140-2 | PMCID: PMC10266980 | PMID: 37258679
- Evidence: Multiple-sequence alignments and phylogenetic trees were calculated using Clustal Omega 81 .
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> structure determination [Coot] -> stage not stated [AlphaFold, ChimeraX, PHENIX, R v4.0, RELION]

### A pan-influenza antibody inhibiting neuraminidase via receptor mimicry. (Nature 2023)

- DOI: 10.1038/s41586-023-06136-y | PMCID: PMC10266979 | PMID: 37258672
- Evidence: The DNA sequences of the VH and VL regions of 14 clonally related mAbs (FNI1–FNI20) were aligned using the online multiple sequence alignment program Clustal Omega ( https://www.ebi.ac.uk/Tools/msa/clustalo/ ).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT, MotionCor2] -> stage not stated [R, RELION, UCSF Chimera]

### Cryo-EM structure of the transposon-associated TnpB enzyme. (Nature 2023)

- DOI: 10.1038/s41586-023-05933-9 | PMCID: PMC10097598 | PMID: 37020030
- Evidence: The figure was prepared using Clustal Omega ( http://www.ebi.ac.uk/Tools/msa/clustalo ) and ESPript3 ( http://espript.ibcp.fr/ESPript/ESPript ).
- Full pipeline: structure determination [ChimeraX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Clustal Omega, PHENIX]

### The giant diploid faba genome unlocks variation in a global protein crop. (Nature 2023)

- DOI: 10.1038/s41586-023-05791-5 | PMCID: PMC10033403 | PMID: 36890232
- Version used: **1.2.4**
- Evidence: Multiple sequence alignment of selected protein sequences was performed using Clustal Omega v1.2.4.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BCFtools v1.8, BEDTools v2.30.0, Clustal Omega v1.2.4, SAMtools v1.15.1, STAR v2.7.8a, minimap2 v2.20] -> quantification [kallisto v0.44.0] -> dimensionality reduction/clustering [R] -> stage not stated [ADMIXTURE v1.3.0, BUSCO v3.0.2b, GEMMA v0.98.5, Kraken2 v2.1.1, RepeatMasker v2.0.1, featureCounts, hifiasm v0.11, lme4]

### Ubiquitin-like conjugation by bacterial cGAS enhances anti-phage defence. (Nature 2023)

- DOI: 10.1038/s41586-023-05862-7 | PMCID: PMC10097602 | PMID: 36848932
- Evidence: Sequences from this PHROG were aligned using Clustal Omega 35 and a phylogenetic tree was generated using the default settings. iTOL: Interactive Tree of Life 36 was used to display the phylogenetic tree.
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [AlphaFold] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### The structural basis for HIV-1 Vif antagonism of human APOBEC3G. (Nature 2023)

- DOI: 10.1038/s41586-023-05779-1 | PMCID: PMC10033410 | PMID: 36754086
- Evidence: These sequences were aligned using Clustal Omega, and logo plots were generated from these alignments with WebLogo 95 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> registration [MotionCor2] -> structure determination [AlphaFold, UCSF Chimera] -> stage not stated [ChimeraX, Coot, PHENIX, PyMOL, RELION]

### Stigma receptors control intraspecies and interspecies barriers in Brassicaceae. (Nature 2023)

- DOI: 10.1038/s41586-022-05640-x | PMCID: PMC9908550 | PMID: 36697825
- Evidence: The amino acid sequence of PCP-Bs and FER alignment was performed by the online software Clustal Omega 54 ( https://www.ebi.ac.uk/Tools/msa/clustalo ) with default parameters then import into ESPript 3.0 (ref.
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE] -> stage not stated [ImageJ v1.53c]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: Multiple sequence alignments of SPOCD1 and SPIN1 were generated with ClustalW 39 and edited in Jalview 40 .
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Mapping glycoprotein structure reveals Flaviviridae evolutionary history. (Nature 2024)

- DOI: 10.1038/s41586-024-07899-8 | PMCID: PMC11410658 | PMID: 39232167
- Version used: **1.2.4**
- Evidence: In brief, flavivirus sequences were aligned using MAFFT, MUSCLE (v5.1) 65 and Clustal Omega (v1.2.4) 76 with default parameters.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Clustal Omega v1.2.4, MAFFT, MUSCLE v5.1] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX] -> stage not stated [AlphaFold v2.3, BLAST v2.0.9, ColabFold v1.5.1, IQ-TREE, InterProScan, Python, phytools v1.5]

### Global marine microbial diversity and its potential in bioprospecting. (Nature 2024)

- DOI: 10.1038/s41586-024-07891-2 | PMCID: PMC11390488 | PMID: 39232160
- Evidence: The six target amino acid sequences were aligned using the ClustalW algorithm in MEGA X 149 , and the alignment results and amino acid residues were analysed and visualized by ESPript (v3.0) 150 .
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.407, MUSCLE v3.8.31] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [AlphaFold v2.3.0, InterProScan v5.0, Prokka v1.14.6, R, ggplot2 v3.5.1]

### Birth of protein folds and functions in the virome. (Nature 2024)

- DOI: 10.1038/s41586-024-07809-y | PMCID: PMC11410667 | PMID: 39187718
- Version used: **1.2.4**
- Evidence: Subsequently, these sequence sets were aligned using Clustal Omega v1.2.4 with default settings 57 .
- Full pipeline: alignment/mapping [AlphaFold, BLAST, Clustal Omega v1.2.4] -> dimensionality reduction/clustering [BLAST, InterProScan] -> differential/statistical testing [R v4.0.3] -> structure determination [IQ-TREE v2.3.3] -> stage not stated [ColabFold, Nextflow]

### An intermediate Rb-E2F activity state safeguards proliferation commitment. (Nature 2024)

- DOI: 10.1038/s41586-024-07554-2 | PMCID: PMC11236703 | PMID: 38926571
- Evidence: Full-length protein sequences were aligned using Clustal Omega ( https://www.ebi.ac.uk/Tools/msa/clustalo/ ) with the default parameters as follows: output guide tree = true, output distance matrix = false, dealign input sequences = false, mBed-like clustering guide tree = true, mBed-like clustering iteration = true, number of iterations = 0, maximum guide tree iterations = –1, maximum HMM iterati...
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [Clustal Omega] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Evidence: Sequence alignments Multiple sequence alignments of FLVCR1 and FLVCR2 from Homo sapiens , Felis catus , Mus musculus and Sus scrofa were performed using Clustal Omega 62 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### Mechanism of single-stranded DNA annealing by RAD52-RPA complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07347-7 | PMCID: PMC11096129 | PMID: 38658755
- Evidence: Multiple-sequence alignment RAD52 protein sequences from different organisms were aligned with Clustal Omega using the default settings 76 .
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega] -> quantification [ImageJ] -> stage not stated [ChimeraX, EMAN2, PHENIX, RELION v3.1]

### Anoxygenic phototroph of the Chloroflexota uses a type I reaction centre. (Nature 2024)

- DOI: 10.1038/s41586-024-07180-y | PMCID: PMC10972752 | PMID: 38480893
- Version used: **1.2.3**
- Evidence: Primary sequences were aligned using Clustal Omega (v1.2.3) 89 , and HMMs were generated using hmmbuild (v3.1b2) 85 .
- Full pipeline: read trimming [DADA2 v1.10.0] -> alignment/mapping [Clustal Omega v1.2.3, featureCounts] -> stage not stated [HMMER v3.1b, IQ-TREE v1.6.9, QIIME 2 v2019.10]

### Selfish conflict underlies RNA-mediated parent-of-origin effects. (Nature 2024)

- DOI: 10.1038/s41586-024-07155-z | PMCID: PMC10990930 | PMID: 38448590
- Evidence: After aligning those sequences to C. elegans Argonautes identified in a previous study 57 using Clustal Omega we conducted phylogenetic analysis using iqtree2 (ref.
- Full pipeline: quality control [deepTools v3.3.1] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Clustal Omega, HISAT2 v2.1, SAMtools v1.10] -> quantification [BEDTools v2.27, R, featureCounts] -> normalisation [BEDTools v2.27, R, featureCounts] -> visualisation [R, featureCounts] -> stage not stated [BLAST, Flye, MACS2]

### The CRL5-SPSB3 ubiquitin ligase targets nuclear cGAS for degradation. (Nature 2024)

- DOI: 10.1038/s41586-024-07112-w | PMCID: PMC10972748 | PMID: 38418882
- Evidence: Sequence alignments A total of 150 human cGAS/SPSB3 orthologues in vertebrates were individually aligned and downloaded in ClustalW format from the Ensembl database.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, CellProfiler, ChimeraX]

### A new family of bacterial ribosome hibernation factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07041-8 | PMCID: PMC10901736 | PMID: 38355796
- Evidence: We then aligned the combined sequences using Clustal Omega 67 with default parameters, which resulted in a multiple sequence alignment (supplementary dataset 6) and a phylogenetic tree (supplementary dataset 7).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, Coot v0.8.9.2, UCSF Chimera v1.14] -> stage not stated [ChimeraX v1.4, HMMER, PHENIX v1.20.1, RELION v3.1]

### Functional and evolutionary significance of unknown genes from uncultivated taxa. (Nature 2024)

- DOI: 10.1038/s41586-023-06955-z | PMCID: PMC10849945 | PMID: 38109938
- Evidence: We computed multiple-sequence alignments for each gene family with Clustal Omega 56 using the translated version of the genes and subsequently reconstructed their phylogeny with FastTree2 (ref.
- Full pipeline: alignment/mapping [BLAST, Clustal Omega, DIAMOND] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [R] -> structure determination [Clustal Omega] -> stage not stated [ColabFold, HMMER, eggNOG]

### Designing allosteric modulators to change GPCR G protein subtype selectivity. (Nature 2025)

- DOI: 10.1038/s41586-025-09643-2 | PMCID: PMC12675282 | PMID: 41125894
- Evidence: Sequences were aligned using the BLOSUM62 matrix in ClustalW.
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega] -> stage not stated [ChimeraX]

### Connecting chemical and protein sequence space to predict biocatalytic reactions. (Nature 2025)

- DOI: 10.1038/s41586-025-09519-5 | PMCID: PMC12488478 | PMID: 41034532
- Evidence: Using NHI123 from Schizosaccharomyces pombe (test set) as an input sequence, Clustal Omega was used to identify the ten most similar enzymes within aKGLib1.
- Full pipeline: stage not stated [Clustal Omega]

### A nanobody specific to prefusion glycoprotein B neutralizes HSV-1 and HSV-2. (Nature 2025)

- DOI: 10.1038/s41586-025-09438-5 | PMCID: PMC12507662 | PMID: 40903574
- Evidence: Multiple sequence alignment for epitope conservation was performed using Clustal Omega 65 and conservation score was calculated as described in refs.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot]

### Global phenology maps reveal the drivers and effects of seasonal asynchrony. (Nature 2025)

- DOI: 10.1038/s41586-025-09410-3 | PMCID: PMC12408380 | PMID: 40866701
- Version used: **2.1**
- Evidence: We aligned sequences using ClustalW (v.2.1) 126 with the default parameter settings and then used jModelTest2 (v.2.1.10) 127 to compare the fit of 44 models of sequence evolution to the sequence data.
- Full pipeline: alignment/mapping [Clustal Omega v2.1, Dask, Matplotlib, NumPy, Python, SciPy, scikit-learn, statsmodels, xarray] -> stage not stated [GDAL v2.2.3, R, TensorFlow]

### Data-driven de novo design of super-adhesive hydrogels. (Nature 2025)

- DOI: 10.1038/s41586-025-09269-4 | PMCID: PMC12328221 | PMID: 40770436
- Evidence: Consensus sequences were computed with Clustal Omega 23 , which performs multiple sequence alignment by generating a distance matrix from pairwise alignments, constructing a guide tree based on evolutionary relationships and progressively aligning sequences from the closest to the most distant.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost] -> machine learning [UMAP] -> stage not stated [Python, scikit-learn v1.0.2]

### A male-essential miRNA is key for avian sex chromosome dosage compensation. (Nature 2025)

- DOI: 10.1038/s41586-025-09256-9 | PMCID: PMC12408383 | PMID: 40670784
- Evidence: These 3′ UTR sequences were then aligned using Clustal Omega.
- Full pipeline: quality control [Bowtie2 v2.5.1] -> read trimming [Bowtie2 v2.5.1, Cutadapt v4.4] -> alignment/mapping [BLAST, Bowtie2 v2.5.1, Clustal Omega, STAR, minimap2] -> quantification [edgeR v4.2.0] -> stage not stated [DESeq2 v1.24.0, SAMtools v1.20]

### Feline infectious peritonitis epizootic caused by a recombinant coronavirus. (Nature 2025)

- DOI: 10.1038/s41586-025-09340-0 | PMCID: PMC12408369 | PMID: 40633571
- Evidence: Multisequence alignments between the population level representative genome. a sample without a spike D0 deletion (2-C11_Re_10276, PQ133182 ) and a sample with a D0 deletion (2-F12_Bl_11350, PQ133177 ) against MT239440.1 , LC742526.1 and KP981644.1 was carried out using ClustalW 66 in Mega7, and recombination analyses carried out using RDP5 37 (v.5.45) with the default settings.
- Full pipeline: alignment/mapping [Clustal Omega, minimap2] -> stage not stated [IQ-TREE]

### RIFINs displayed on malaria-infected erythrocytes bind KIR2DL1 and KIR2DS1. (Nature 2025)

- DOI: 10.1038/s41586-025-09091-y | PMCID: PMC12310515 | PMID: 40500441
- Evidence: Phylogenetic analysis of RIFINs The amino acid sequences of all RIFINs of the P. falciparum 3D7 strain were obtained from PlasmoDB ( https://plasmodb.org/plasmo/app/ ) and aligned using the Clustal Omega program ( https://www.ebi.ac.uk/jdispatcher/msa/clustalo ).
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Clustal Omega, PyMOL, featureCounts] -> normalisation [featureCounts] -> structure determination [Coot v0.8.9.2] -> stage not stated [BWA, Flye, ImageJ v1.54b, Pilon]

### Discovery of FoTO1 and Taxol genes enables biosynthesis of baccatin III. (Nature 2025)

- DOI: 10.1038/s41586-025-09090-z | PMCID: PMC12240809 | PMID: 40500440
- Evidence: Multiple sequence alignment for each family was performed using Clustal Omega, and the phylogenetic trees were constructed using the neighbour-joining method in Geneious Prime (v.2024.0.4) with 100 bootstrap replicates for initial analysis.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [AlphaFold, Clustal Omega, Trimmomatic] -> dimensionality reduction/clustering [SciPy, UMAP] -> stage not stated [HMMER, NumPy, Scanpy v1.10.1]

### Stepwise ATP translocation into the endoplasmic reticulum by human SLC35B1. (Nature 2025)

- DOI: 10.1038/s41586-025-09069-w | PMCID: PMC12267056 | PMID: 40399679
- Evidence: The sequences were aligned using Clustal Omega 62 and the tree was generated using Jalview 63 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, Galaxy, PyMOL]

### A pangenome reference of wild and cultivated rice. (Nature 2025)

- DOI: 10.1038/s41586-025-08883-6 | PMCID: PMC12176639 | PMID: 40240605
- Evidence: Identification of centromeres and telomeres The sequences of CentO satellite repeats in rice, which had been reported previously 92 , were aligned against nuclear genomes using ClustalW 93 (v.2.1).
- Full pipeline: alignment/mapping [Clustal Omega, HISAT2, HMMER, OrthoFinder, QUAST, SAMtools, minimap2] -> dimensionality reduction/clustering [ADMIXTURE, GATK, R, clusterProfiler v4.6.2] -> differential/statistical testing [IQ-TREE] -> stage not stated [AUGUSTUS, BEDTools, BUSCO, InterProScan, MAFFT, PLINK, RepeatMasker, SnpEff, StringTie, VCFtools, fastp, ggplot2, hifiasm]

### Glutamate gating of AMPA-subtype iGluRs at physiological temperatures. (Nature 2025)

- DOI: 10.1038/s41586-025-08770-0 | PMCID: PMC12074995 | PMID: 40140570
- Evidence: Amino acid sequence alignments were generated using Clustal Omega 72 and were visualized with ESPript v.3.0 (ref.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [ChimeraX, PHENIX] -> visualisation [Clustal Omega]

### The conserved HIV-1 spacer peptide 2 triggers matrix lattice maturation. (Nature 2025)

- DOI: 10.1038/s41586-025-08624-9 | PMCID: PMC11964938 | PMID: 40011770
- Evidence: Afterwards, sequences built into the side pocket cryo-EM densities from the central MA trimer were extracted and analysed by the Clustal Omega multiple sequence analysis tool 61 .
- Full pipeline: structure determination [PHENIX] -> visualisation [RELION] -> stage not stated [AlphaFold v2.2.0, ChimeraX v1.3, Clustal Omega, Fiji v1.54f, ImageJ v1.54f]

### De novo designed proteins neutralize lethal snake venom toxins. (Nature 2025)

- DOI: 10.1038/s41586-024-08393-x | PMCID: PMC11882462 | PMID: 39814879
- Evidence: The resultant 86 unique CTX sequences were subjected to multiple sequence alignments in Clustal Omega 62 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### In situ analysis reveals the TRiC duty cycle and PDCD5 as an open-state cofactor. (Nature 2025)

- DOI: 10.1038/s41586-024-08321-z | PMCID: PMC11754096 | PMID: 39663456
- Evidence: Sequence alignment Sequence alignment of CCT1–CCT8 (UniProt: P17987 , P78371 , P49368 , P50991 , P48643 , P40227 , Q99832 and P50990 ) was executed through Clustal Omega 61 .
- Full pipeline: alignment/mapping [Clustal Omega, IMOD] -> structure determination [RELION] -> visualisation [ChimeraX, napari] -> stage not stated [AlphaFold]

### Substrate selectivity of the human RNA m&lt;sup&gt;5&lt;/sup&gt;C methyltransferase NSUN2. (Nature 2026)

- DOI: 10.1038/s41586-026-10582-9 | PMCID: PMC13289585 | PMID: 42203868
- Version used: **1.2.4**
- Evidence: Human NSUN protein multi-sequence alignment was performed with Clustal Omega v.1.2.4 (ref.
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4] -> structure determination [ChimeraX v1.8, PHENIX v1.21.1] -> stage not stated [AlphaFold, CCP4]

### RNA-triggered cell killing with CRISPR-Cas12a2. (Nature 2026)

- DOI: 10.1038/s41586-026-10466-y | PMCID: PMC13323058 | PMID: 42092133
- Evidence: Methods Phylogenetic analysis The amino acid sequence of GeCas12a2 was aligned with other Cas12a2 nuclease sequences 15 , 59 using Clustal Omega 60 .
- Full pipeline: read trimming [IQ-TREE v2.0.3, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, Clustal Omega, IQ-TREE v2.0.3, RSEM, STAR] -> quantification [CellProfiler, Cufflinks v2.1.1, DESeq2 v1.44.0, ilastik] -> normalisation [DESeq2 v1.44.0, R, fgsea v1.30.0] -> differential/statistical testing [DESeq2 v1.44.0, R, fgsea v1.30.0] -> structure determination [IQ-TREE v2.0.3] -> visualisation [Matplotlib, Python] -> stage not stated [BLAST, Fiji, GSEA, ImageJ, SAMtools v1.3.1]

### A pro-carcinogenic bacterial toxin binds claudin-4 to cleave E-cadherin. (Nature 2026)

- DOI: 10.1038/s41586-026-10375-0 | PMCID: PMC13253352 | PMID: 42020735
- Evidence: Sequence alignments were generated using Clustal Omega or EMBOSS Needle 64 and the alignment shown in Extended Data Fig.
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ImageJ, R v4.2.2, ggplot2 v3.4.4]

### Assembly of helper NLR resistosome clusters upon activation of a coiled-coil NLR. (Nature 2026)

- DOI: 10.1038/s41586-026-10215-1 | PMCID: PMC13043302 | PMID: 41813892
- Evidence: Amino acid sequences of N-terminal domains were aligned using ClustalW.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [R v4.3.1, ggplot2] -> differential/statistical testing [lme4] -> visualisation [Matplotlib, NumPy, PyMOL, Python v3.10, R v4.3.1, SciPy, ggplot2] -> stage not stated [AlphaFold, ImageJ, TrackMate]

### B cell imprinting in children impairs antibodies to the haemagglutinin stalk. (Nature 2026)

- DOI: 10.1038/s41586-026-10248-6 | PMCID: PMC13171607 | PMID: 41813896
- Evidence: Multiple-sequence alignments were conducted using Clustal Omega, and the resulting alignments were used to generate sequence logos with WebLogo 3.
- Full pipeline: quality control [Seurat v4.3.0, UMAP] -> alignment/mapping [Clustal Omega] -> normalisation [Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.3.0, UMAP, fgsea] -> differential/statistical testing [Seurat v4.3.0, UMAP] -> structure determination [Coot v0.9.8, PHENIX] -> visualisation [R v4.2, Seurat v4.3.0, UMAP, ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python]

### A prophage-encoded abortive infection protein preserves host and prophage spread. (Nature 2026)

- DOI: 10.1038/s41586-025-10070-6 | PMCID: PMC13043305 | PMID: 41606329
- Evidence: Selected sequences were aligned using Clustal Omega 65 with protein-specific mode and automatic strategy optimization.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT] -> structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BEDTools v2.27.1, PHENIX, SAMtools v1.1]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Evidence: Multiple sequence alignments for SPOCD1 was generated with Clustal Omega 49 and visualised in JalView (2.11.4.1) 50 for the canonical SPOCD1 sequences from UniProt 51 for the following species – Mouse ( Mus musculus , B1ASB6 ), Golden hamster ( Mesocricetus auratus , A0A3Q0D6B7), Ord’s kangaroo rat ( Dipodomys ordii , A0A1S3FIT4), Western European hedgehog ( Erinaceus europaeus , A0A1S3WPZ3), Rabb...
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### RNA-triggered Cas12a3 cleaves tRNA tails to execute bacterial immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09852-9 | PMCID: PMC12851939 | PMID: 41501459
- Evidence: The resulting amino acid sequences, along with Cas12a orthologues used as an outgroup, were aligned using Clustal Omega 59 .
- Full pipeline: read trimming [BWA v0.7.17, IQ-TREE v2.3.6, Trimmomatic v0.39] -> alignment/mapping [BLAST, BWA v0.7.17, Clustal Omega, IQ-TREE v2.3.6] -> structure determination [AlphaFold, ChimeraX v1.7, IQ-TREE v2.3.6, PHENIX v1.20.1] -> visualisation [Matplotlib, Python] -> stage not stated [SAMtools v1.9]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Evidence: 3 Position dependent rescue of gene function by SOS splicing. a , C. elegans RSD-3 protein and its orthologous sequences from S. cerevisiae , A. thaliana , D. melanogaster , D. rerio , X. laevis , M. musculus , and H. sapiens were aligned using Clustal Omega multiple sequence alignment program.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Mutations in mitochondrial ferredoxin FDX2 suppress frataxin deficiency. (Nature 2026)

- DOI: 10.1038/s41586-025-09821-2 | PMCID: PMC12804076 | PMID: 41372402
- Evidence: ...t of NFS1 ( C. elegans residues 239–251) and FDX2 ( C. elegans residues 117–127) including homologues from mammals, fish and invertebrates made using ClustalW. c , Synchronized frataxin-null animals grown at 7% oxygen for 4 days with or without suppressor mutations in fdx-2 and nfs-1 .
- Full pipeline: stage not stated [Clustal Omega]

### Long-read metagenomics reveals phage dynamics in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09786-2 | PMCID: PMC12823448 | PMID: 41299176
- Version used: **1.2.4**
- Evidence: First, we built a tree for all IS30 proteins on all IScream phages using the ‘standard_fasttree‘ workflow from ete3, consisting of a multiple sequence alignment with Clustal Omega (v.1.2.4) and tree construction using FastTree (v.2.1.8) (Extended Data Fig.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.5.4, Clustal Omega v1.2.4, NanoPlot v1.41.6, SAMtools v1.21, minimap2 v2.26] -> differential/statistical testing [R v4.2.2] -> visualisation [R v4.2.2, ggplot2 v3.5.1, tidyverse v2.0.0] -> stage not stated [Flye, HMMER v3.4, Snakemake v5.26.0]

### SIGLEC12 mediates plasma membrane rupture during necroptotic cell death. (Nature 2026)

- DOI: 10.1038/s41586-025-09741-1 | PMCID: PMC12779560 | PMID: 41225007
- Evidence: Alignments were done using Clustal Omega 42 and visualized using Jalview 43 .
- Full pipeline: quality control [FastQC v0.11.2] -> alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [Fiji, ImageJ]

### Complete biosynthesis of the bisbenzylisoquinoline alkaloids guattegaumerine and berbamunine in yeast. (PNAS 2021)

- DOI: 10.1073/pnas.2112520118 | PMCID: PMC8713753 | PMID: 34903659
- Evidence: Clustal Omega was used to generate protein sequence alignments ( 48 ).
- Full pipeline: alignment/mapping [Clustal Omega]

### The cyclic dinucleotide 2'3'-cGAMP induces a broad antibacterial and antiviral response in the sea anemone &lt;i&gt;Nematostella vectensis&lt;/i&gt;. (PNAS 2021)

- DOI: 10.1073/pnas.2109022118 | PMCID: PMC8713801 | PMID: 34903650
- Evidence: Alignments shown were made in Geneious using Clustal Omega.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Clustal Omega, DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto]

### Molecular mechanisms of sperm motility are conserved in an early-branching metazoan. (PNAS 2021)

- DOI: 10.1073/pnas.2109993118 | PMCID: PMC8640785 | PMID: 34810263
- Evidence: In silico comparisons of protein structure were carried out using the Clustal Omega multiple sequence alignment tool ( 82 ), prediction of transmembrane segments using the TMHMM server ( 83 ), and prediction of coiled-coil domains using the DeepCoil server ( 52 ).
- Full pipeline: alignment/mapping [Clustal Omega]

### Protease cleavage of RNF20 facilitates coronavirus replication via stabilization of SREBP1. (PNAS 2021)

- DOI: 10.1073/pnas.2107108118 | PMCID: PMC8449311 | PMID: 34452991
- Evidence: ( J ) Analysis of the protein sequences across species for RNF20 cleavage sites using Clustal Omega online service.
- Full pipeline: stage not stated [Clustal Omega]

### Self-mediated positive selection of T cells sets an obstacle to the recognition of nonself. (PNAS 2021)

- DOI: 10.1073/pnas.2100542118 | PMCID: PMC8449404 | PMID: 34507984
- Version used: **1.2**
- Evidence: Briefly, the k-tuple distance between all peptide sequences was determined in each iteration using Clustal Omega 1.2 ( 59 ).
- Full pipeline: normalisation [edgeR] -> differential/statistical testing [R v3.6.3] -> visualisation [ComplexHeatmap, ggplot2, ggpubr] -> stage not stated [Clustal Omega v1.2]

### <i>ENHANCED GRAVITROPISM 2</i> encodes a STERILE ALPHA MOTIF-containing protein that controls root growth angle in barley and wheat. (PNAS 2021)

- DOI: 10.1073/pnas.2101526118 | PMCID: PMC8536364 | PMID: 34446550
- Evidence: Retrieved protein sequences were aligned by ClustalW in the software MEGA X, with default values ( 70 ): Ancestral states were inferred using the maximum likelihood method ( 71 ) and JTT matrix-based model ( 72 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v7.12, Clustal Omega, DESeq2, HTSeq, R, SAMtools v1.3, STAR] -> variant calling [STAR] -> normalisation [DESeq2, HTSeq, R] -> dimensionality reduction/clustering [DESeq2, HTSeq, R] -> stage not stated [ImageJ]

### A conserved epitope III on hepatitis C virus E2 protein has alternate conformations facilitating cell binding or virus neutralization. (PNAS 2021)

- DOI: 10.1073/pnas.2104242118 | PMCID: PMC8285954 | PMID: 34260404
- Evidence: For each matching structure, all chains were aligned with the PDB ID code 6MEH E2 sequence using Clustal Omega ( 47 , 48 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [seaborn] -> stage not stated [CCP4, PyMOL]

### Fifty million years of beetle evolution along the Antarctic Polar Front. (PNAS 2021)

- DOI: 10.1073/pnas.2017384118 | PMCID: PMC8214695 | PMID: 34108239
- Evidence: Sequence chromatograms were aligned using the ClustalW algorithm ( 91 ) to create consensus sequences for each individual.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Clustal Omega, MAFFT] -> dimensionality reduction/clustering [R, RAxML] -> differential/statistical testing [MrBayes v3.2.6] -> structure determination [MAFFT] -> stage not stated [BEAST v2.5]

### The ORF8 protein of SARS-CoV-2 mediates immune evasion through down-regulating MHC-Ι. (PNAS 2021)

- DOI: 10.1073/pnas.2024202118 | PMCID: PMC8201919 | PMID: 34021074
- Evidence: The protein alignments were created by Clustal Omega software using default parameters conducted in MEGA X ( 55 ).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT]

### ICAM-1 induced rearrangements of capsid and genome prime rhinovirus 14 for activation and uncoating. (PNAS 2021)

- DOI: 10.1073/pnas.2024251118 | PMCID: PMC8126848 | PMID: 33947819
- Evidence: Multiple sequence alignment of capsid proteins of selected viruses from the family Picornaviridae was performed in the Clustal Omega server ( 82 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot v0.9, PHENIX]

### An intracellular nanobody targeting T4SS effector inhibits <i>Ehrlichia</i> infection. (PNAS 2021)

- DOI: 10.1073/pnas.2024102118 | PMCID: PMC8106314 | PMID: 33903242
- Evidence: The CDR3 amino acid sequences of 107 and 65 Nbs bound to nondenatured and denatured rEtf-1, respectively, were aligned using the MegAlign program with the ClustalW algorithm of Lasergene DNASTAR software (DNASTAR).
- Full pipeline: alignment/mapping [Clustal Omega]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Version used: **1.2.4**
- Evidence: Each CAZyme gene, along with highly similar homologs identified by MMSeq2 in the pig shotgun sequencing dataset were aligned using Clustal Omega (v1.2.4) ( 66 ).
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### Structural basis for selective AMPylation of Rac-subfamily GTPases by <i>Bartonella</i> effector protein 1 (Bep1). (PNAS 2021)

- DOI: 10.1073/pnas.2023245118 | PMCID: PMC8000347 | PMID: 33723071
- Evidence: Structure guided multiple sequence alignments (MSA) were generated by manual adjustment of MSA generated using the ClustalW algorithm as implemented in the GENEIOUS software package ( 46 ) version 7.1.7.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [Conda]

### Redox regulation of NADP-malate dehydrogenase is vital for land plants under fluctuating light environment. (PNAS 2021)

- DOI: 10.1073/pnas.2016903118 | PMCID: PMC8017969 | PMID: 33531363
- Evidence: The consensus symbols (*, fully conserved; :, strongly conserved; and ., weakly conserved) obtained via the Clustal Omega analysis ( https://www.ebi.ac.uk/Tools/msa/clustalo/ ) are shown below the alignment result.
- Full pipeline: alignment/mapping [Clustal Omega]

### Conjugative plasmid-encoded toxin-antitoxin system PrpT/PrpA directly controls plasmid copy number. (PNAS 2021)

- DOI: 10.1073/pnas.2011577118 | PMCID: PMC7848731 | PMID: 33483419
- Evidence: ( D ) Multiple sequence alignment constructed by ClustalW to compare the amino acid sequence identity of ParE associated antitoxins from PF03693 and PF09386 in the conjugative plasmids.
- Full pipeline: alignment/mapping [Clustal Omega]

### Bioengineered peptibodies as blockers of ion channels. (PNAS 2022)

- DOI: 10.1073/pnas.2212564119 | PMCID: PMC9897444 | PMID: 36475947
- Evidence: A sequence alignment of Kir3.1, Kir3.4, and Kir3.2 was generated using the ClustalW server ( http://www.genome.jp/-tools/clustalw/ ).
- Full pipeline: alignment/mapping [Clustal Omega]

### A bacterium from a mountain lake harvests light using both proton-pumping xanthorhodopsins and bacteriochlorophyll-based photosystems. (PNAS 2022)

- DOI: 10.1073/pnas.2211018119 | PMCID: PMC9897461 | PMID: 36469764
- Evidence: Nucleotide sequences of the conserved 300-bp upstream intergenic region, the XR gene, and the PS RC subunit M ( pufM ) gene were retrieved from genomes downloaded from NCBI GenBank (October 2021) or from metagenomes ( 23 ) and aligned using ClustalW ( 54 ).
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [featureCounts]

### A novel post-developmental role of the Hox genes underlies normal adult behavior. (PNAS 2022)

- DOI: 10.1073/pnas.2209531119 | PMCID: PMC9894213 | PMID: 36454751
- Evidence: S7 and S8 ) using EMBL-EBI Clustal Omega, Jalview program ( 36 ) and JPred secondary structure prediction programs( 37 ) for these symporter genes reveal that they belong to two independent lineages within the SLC family: SLC5 and SLC2 4 ( 38 – 41 ).
- Full pipeline: differential/statistical testing [edgeR] -> stage not stated [Clustal Omega, ImageJ]

### VpdC is a ubiquitin-activated phospholipase effector that regulates <i>Legionella</i> vacuole expansion during infection. (PNAS 2022)

- DOI: 10.1073/pnas.2209149119 | PMCID: PMC9860323 | PMID: 36413498
- Evidence: Its middle domain (MD; residues 258-609) shows considerable sequence homology to patatin-like phospholipases, most notably VipD from L. pneumophila (26% identity, by Clustal Omega) and ExoU from Pseudomonas aeruginosa (30% identity).
- Full pipeline: stage not stated [ChimeraX, Clustal Omega]

### Silencing RNAs expressed from W-linked &lt;i&gt;PxyMasc&lt;/i&gt; "retrocopies" target that gene during female sex determination in &lt;i&gt;Plutella xylostella&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2206025119 | PMCID: PMC9674220 | PMID: 36343250
- Evidence: ( C ) Phylogeny constructed using Clustal Omega including all 11 identified Pxyfem copies along with 250 bp of up- and downstream genomic flanking sequence.
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [BLAST, Clustal Omega]

### Structural and functional investigation of ABC transporter STE6-2p from <i>Pichia pastoris</i> reveals unexpected interaction with sterol molecules. (PNAS 2022)

- DOI: 10.1073/pnas.2202822119 | PMCID: PMC9618074 | PMID: 36256814
- Evidence: All homologous protein sequences were aligned with ClustalW and a maximum-likelihood tree (50× bootstrap) was generated utilizing MEGA software ( 72 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [BLAST, CTFFIND, MotionCor2, RELION v3.1]

### Deep-branching acetogens in serpentinized subsurface fluids of Oman. (PNAS 2022)

- DOI: 10.1073/pnas.2206845119 | PMCID: PMC9586279 | PMID: 36215489
- Version used: **1.2.4**
- Evidence: Individual marker gene proteins were aligned with Clustal Omega (v.1.2.4) ( 46 ), trimmed with TrimAl (v.1.4) ( 47 ) specifying a gap threshold (gt) value of 0.1 and default parameters otherwise, and then concatenated into a super alignment matrix.
- Full pipeline: read trimming [Clustal Omega v1.2.4] -> alignment/mapping [BLAST, Bowtie2, Clustal Omega v1.2.4, IQ-TREE v1.6.11] -> quantification [Bowtie2] -> differential/statistical testing [IQ-TREE v1.6.11] -> stage not stated [Prokka v1.14.5]

### A single helix repression domain is functional across diverse eukaryotes. (PNAS 2022)

- DOI: 10.1073/pnas.2206986119 | PMCID: PMC9564828 | PMID: 36191192
- Evidence: LisH Helix 1 domains were aligned using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> normalisation [ImageJ] -> visualisation [ggplot2, tidyverse] -> stage not stated [R]

### SPACA9 is a lumenal protein of human ciliary singlet and doublet microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2207605119 | PMCID: PMC9564825 | PMID: 36191189
- Version used: **1.2.2**
- Evidence: S4 B was generated using Clustal Omega version 1.2.2 ( 58 ) and visualized in ESPrint version 3.0 ( 59 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX, Clustal Omega v1.2.2] -> stage not stated [AlphaFold, Coot v0.9.4.1, IMOD, PHENIX, PyMOL v2.3.4, RELION]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Version used: **1.2.0**
- Evidence: Clustal Omega v1.2.0 ( 106 ) was applied for multiple sequence alignment after rotating the mitochondrial sequences using Cyclic DNA Sequence Aligner ( 107 ).
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Plant <i>N</i>-glycan breakdown by human gut <i>Bacteroides</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208168119 | PMCID: PMC9522356 | PMID: 36122227
- Evidence: Sequence identities were determined using Clustal Omega using full sequences ( 46 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [CCP4, Clustal Omega]

### Structure of IMPORTIN-4 bound to the H3-H4-ASF1 histone-histone chaperone complex. (PNAS 2022)

- DOI: 10.1073/pnas.2207177119 | PMCID: PMC9499513 | PMID: 36103578
- Evidence: S6 ) were performed in Clustal Omega ( 33 ), and the image of the alignments was generated by ENDscript ( 34 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [PyMOL]

### Targeting of microvillus protein Eps8 by the NleH effector kinases from enteropathogenic &lt;i&gt;E. coli&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2204332119 | PMCID: PMC9407544 | PMID: 35976880
- Evidence: The protein sequences of Eps8 (accession number Q12929 ), Eps8L1 (accession number Q8TE68 ), and Eps8L2 (accession number Q9H6S3 ) were aligned in Clustal Omega ( 43 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ggplot2]

### Correlations between alignment gaps and nucleotide substitution or amino acid replacement. (PNAS 2022)

- DOI: 10.1073/pnas.2204435119 | PMCID: PMC9407537 | PMID: 35972964
- Version used: **1.2.2**
- Evidence: We examined the test behavior using optimal alignments from Clustal Omega (version 1.2.2) ( 16 ), MAFFT (version 7.475) ( 17 ), Muscle (version 3.8.31) ( 18 ), and Prank (version 170427) ( 19 ).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2, MAFFT v7.475]

### Noncanonical PDK4 action alters mitochondrial dynamics to affect the cellular respiratory status. (PNAS 2022)

- DOI: 10.1073/pnas.2120157119 | PMCID: PMC9407676 | PMID: 35969774
- Evidence: ( E ) ClustalW alignment of SEPT2 amino acid sequences showing that S218 site is conserved among the mammalian species.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ]

### &lt;i&gt;Escherichia coli&lt;/i&gt; RclA is a highly active hypothiocyanite reductase. (PNAS 2022)

- DOI: 10.1073/pnas.2119368119 | PMCID: PMC9335216 | PMID: 35867824
- Evidence: ( C ) Alignment of the N-terminal 60 residues of RclA from E. coli and homologs from the indicated species (Clustal Omega).
- Full pipeline: alignment/mapping [Clustal Omega]

### The Hippo pathway regulates axis formation and morphogenesis in &lt;i&gt;Hydra&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2203257119 | PMCID: PMC9304002 | PMID: 35858299
- Evidence: For generation of the phylogenetic tree, the sequences were aligned using MAFFT (Multiple Alignment using Fast Fourier Transform) ( https://www.ebi.ac.uk/Tools/msa/mafft/ ) or Clustal Omega ( https://www.ebi.ac.uk/Tools/msa/clustalo/ ) and analyzed using Akaike Information Criterion ( www.atgc-montpellier.fr ).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT]

### Essential functions of mosquito ecdysone importers in development and reproduction. (PNAS 2022)

- DOI: 10.1073/pnas.2202932119 | PMCID: PMC9231622 | PMID: 35696563
- Evidence: 1 A ) was generated using ClustalW ( https://www.ddbj.nig.ac.jp/services/clustalw-e.html ) ( 35 , 36 ).
- Full pipeline: stage not stated [BLAST, Clustal Omega, ImageJ v1.53v]

### A peptide-mediated, multilateral molecular dialogue for the coordination of pollen wall formation. (PNAS 2022)

- DOI: 10.1073/pnas.2201446119 | PMCID: PMC9295805 | PMID: 35609199
- Evidence: Fully, strongly, and weakly conserved residues (Clustal W; Gonnet Pam250 matrix) are highlighted in red, blue, and green, respectively.
- Full pipeline: stage not stated [Clustal Omega]

### Dromedary camel nanobodies broadly neutralize SARS-CoV-2 variants. (PNAS 2022)

- DOI: 10.1073/pnas.2201433119 | PMCID: PMC9170159 | PMID: 35476528
- Evidence: Sequence alignment of SARS-CoV-2 neutralizing V H Hs using Clustal Omega Program ( https://www.ebi.ac.uk/Tools/msa/clustalo/ ) with ImMunoGeneTics (IMGT) in bold, Kabat italicized, and Paratome underlined.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS] -> structure determination [PHENIX v1.19.2] -> stage not stated [Pangolin]

### 50S subunit recognition and modification by the &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; ribosomal RNA methyltransferase TlyA. (PNAS 2022)

- DOI: 10.1073/pnas.2120352119 | PMCID: PMC9168844 | PMID: 35357969
- Evidence: A total of 223 representative sequences were aligned using Clustal Omega and an unrooted neighbor joining phylogenetic tree was constructed using MEGA X ( 60 ) with evolutionary distances computed using the JTT matrix-based method ( 61 ).
- Full pipeline: alignment/mapping [Clustal Omega, RELION] -> stage not stated [CTFFIND, Coot, PHENIX v1.19.2]

### Rapid recruitment of p53 to DNA damage sites directs DNA repair choice and integrity. (PNAS 2022)

- DOI: 10.1073/pnas.2113233119 | PMCID: PMC8915893 | PMID: 35235448
- Evidence: We analyzed protein sequence similarity using an alignment tool Clustal Omega ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [Clustal Omega]

### Intragenic suppressors unravel the role of the SCREAM ACT-like domain for bHLH partner selectivity in stomatal development. (PNAS 2022)

- DOI: 10.1073/pnas.2117774119 | PMCID: PMC8892516 | PMID: 35173013
- Evidence: ClustalW was used to generate the alignment.
- Full pipeline: alignment/mapping [Clustal Omega]

### <i>PRDM9</i> losses in vertebrates are coupled to those of paralogs <i>ZCWPW1</i> and <i>ZCWPW2</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2114401119 | PMCID: PMC8892340 | PMID: 35217607
- Evidence: In brief, we first identified putative PRDM9 orthologs using a blastp search ( 30 ) against the RefSeq database and confirmed the orthology of each by visually inspecting where these genes clustered in neighbor-joining trees built with Clustal Omega ( 51 ) for identified KRAB, SSXRD, and SET domain sequences ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [BLAST, Clustal Omega] -> stage not stated [BUSCO, R]

### A dominant negative variant of <i>RAB5B</i> disrupts maturation of surfactant protein B and surfactant protein C. (PNAS 2022)

- DOI: 10.1073/pnas.2105228119 | PMCID: PMC8832968 | PMID: 35121658
- Evidence: Alignment distance values are shown (Clustal Omega).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UMAP]

### Sex-specific splicing of Z- and W-borne <i>nr5a1</i> alleles suggests sex determination is controlled by chromosome conformation. (PNAS 2022)

- DOI: 10.1073/pnas.2116475119 | PMCID: PMC8795496 | PMID: 35074916
- Evidence: Sequences were aligned using ClustalW in Geneious sequence analysis software (Geneious version 8.1 by Biomatters).
- Full pipeline: alignment/mapping [BWA, Clustal Omega] -> quantification [DESeq2 v1.26.0] -> dimensionality reduction/clustering [AlphaFold] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [R, kallisto]

### High-resolution cryo-electron microscopy structure of photosystem II from the mesophilic cyanobacterium, <i>Synechocystis</i> sp. PCC 6803. (PNAS 2022)

- DOI: 10.1073/pnas.2116765118 | PMCID: PMC8740770 | PMID: 34937700
- Evidence: Sequence alignments and identity were generated with Clustal Omega ( 47 ), and conservation identifiers are shown below the alignment.
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [RELION v3.1, UCSF Chimera]

### Disruption of MeCP2-TCF20 complex underlies distinct neurodevelopmental disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2119078119 | PMCID: PMC8794850 | PMID: 35074918
- Evidence: ( B ) ClustalW multispecies alignment obtained with the region containing C322G, yellow bar showing the high level of conservation of the mutated residue.
- Full pipeline: alignment/mapping [Clustal Omega]

### MEnTaT: A machine-learning approach for the identification of mutations to increase protein stability. (PNAS 2023)

- DOI: 10.1073/pnas.2309884120 | PMCID: PMC10710055 | PMID: 38039271
- Evidence: The sequences in this smaller set were aligned to the target protein by multiple sequence alignment using Clustal Omega ( 55 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ColabFold]

### &lt;i&gt;INDETERMINATE1&lt;/i&gt;-mediated expression of &lt;i&gt;FT&lt;/i&gt; family genes is required for proper timing of flowering in &lt;i&gt;Brachypodium distachyon&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2312052120 | PMCID: PMC10655584 | PMID: 37934817
- Evidence: The alignment of the full-length amino acid sequences of ID orthologs in different species was conducted via the ClustalW program ( 81 ).
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, SAMtools v1.9] -> stage not stated [Galaxy, featureCounts v1.6.2, tidyverse]

### Lateral interactions govern self-assembly of the bacterial biofilm matrix protein BslA. (PNAS 2023)

- DOI: 10.1073/pnas.2312022120 | PMCID: PMC7615278 | PMID: 37903266
- Version used: **1.2.4**
- Evidence: Sequence alignment Sequences of BslA and YweA proteins from the Bacillus genus were obtained from the NCBI database and aligned using Clustal Omega (1.2.4) ( 41 ).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4] -> structure determination [Coot]

### Loss of Pde1 function acts as an evolutionary gateway to penicillin resistance in <i>Streptococcus pneumoniae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2308029120 | PMCID: PMC10576035 | PMID: 37796984
- Evidence: Multiple sequence alignments of the translated sequences were produced using Clustal Omega and these were used to identify sequence variation from the consensus sequence at each locus.
- Full pipeline: alignment/mapping [Clustal Omega, HMMER v3.2.1] -> stage not stated [Python, SPAdes v3.15.5]

### Bacterial SEAL domains undergo autoproteolysis and function in regulated intramembrane proteolysis. (PNAS 2023)

- DOI: 10.1073/pnas.2310862120 | PMCID: PMC10556640 | PMID: 37756332
- Evidence: Multiple sequence alignments were generated using Clustal Omega ( https://www.ebi.ac.uk/Tools/msa/clustalo/ ) ( 60 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot] -> stage not stated [AlphaFold, ColabFold, PHENIX v1.20.1]

### Distinct regions of the kinesin-5 C-terminal tail are essential for mitotic spindle midzone localization and sliding force. (PNAS 2023)

- DOI: 10.1073/pnas.2306480120 | PMCID: PMC10523502 | PMID: 37725645
- Evidence: Middle and Lower : ClustalW sequence alignment of kinesin-5 C-terminal tails near the BimC box ( Middle ) and NIMA-family kinase box ( Lower ), adapted from ref.
- Full pipeline: alignment/mapping [Clustal Omega]

### <i>Iditarod</i>, a <i>Drosophila</i> homolog of the Irisin precursor <i>FNDC5</i>, is critical for exercise performance and cardiac autophagy. (PNAS 2023)

- DOI: 10.1073/pnas.2220556120 | PMCID: PMC10523451 | PMID: 37722048
- Evidence: Multiple sequence alignments and tree construction was performed using web-based Clustal Omega ( 58 ) and Mview ( 59 ) tools available at EMBL-EBI, Constraint-based Multiple Alignment ( 60 ) and Fast Minimum Evolution ( 61 ) tools available at NCBI.
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [PyMOL] -> stage not stated [AlphaFold, RoseTTAFold]

### Fungal COP9 signalosome assembly requires connection of two trimeric intermediates for integration of intrinsic deneddylase. (PNAS 2023)

- DOI: 10.1073/pnas.2305049120 | PMCID: PMC10477865 | PMID: 37603767
- Evidence: For multiple sequence alignments ClustalW or Muscle ( 79 ) was used.
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [PyMOL]

### Independent evolution of transposase and TIRs facilitated by recombination between <i>Mutator</i> transposons from divergent clades in maize. (PNAS 2023)

- DOI: 10.1073/pnas.2305298120 | PMCID: PMC10401008 | PMID: 37490540
- Evidence: Bioinformatically identified TIRs were aligned using Clustal W ( 55 ) in the Geneious8 (geneious.com) software interface ( Dataset S5 ) with the IUB cost matrix, a gap open cost of 15, and a cap extend cost of 6.66.
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE]

### T cell deletional tolerance restricts AQP4 but not MOG CNS autoimmunity. (PNAS 2023)

- DOI: 10.1073/pnas.2306572120 | PMCID: PMC10372680 | PMID: 37463205
- Evidence: ...A I N Y TG A SMNPARSF AQP6 182–198 L IG I Y F TG C SMNPA RSF 71 78 Brain and kidney * Each mouse aquaporin was aligned individually to AQP4 using the Clustal Omega Multiple Sequence Alignment Tool (Clustal Omega < Multiple Sequence Alignment < EMBL-EBI), and homologous regions were identified. † Identical residues are identified in bolded black, and core binding regions are underlined. ‡ The % hom...
- Full pipeline: alignment/mapping [Clustal Omega, STAR v2.5.1]

### Ancient vertebrate dermal armor evolved from trunk neural crest. (PNAS 2023)

- DOI: 10.1073/pnas.2221120120 | PMCID: PMC10372632 | PMID: 37459514
- Version used: **1.2.3**
- Evidence: The sterlet has a paralog retention rate of about 70% from its genome duplication; thus, all IDs of candidate genes were used for further analysis, and paralogs ( SI Appendix , Table S2 ) were phylogenetically analyzed (amino acid tree made using the maximum likelihood method [PhyML 3.0 ( 61 ) http://www.atgc-montpellier.fr/phyml/ ] on a Clustal Omega 1.2.3 alignment, bootstrap score n = 100).
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega v1.2.3] -> visualisation [ComplexHeatmap] -> stage not stated [DESeq2, featureCounts]

### The ubiquitin-protein ligase MIEL1 localizes to peroxisomes to promote seedling oleosin degradation and lipid droplet mobilization. (PNAS 2023)

- DOI: 10.1073/pnas.2304870120 | PMCID: PMC10629534 | PMID: 37410814
- Evidence: ( A ) Alignment of MIEL1 and related proteins generated using the MegAlign (DNAStar) Clustal W method (BLOSUM series protein weight matrix).
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Coordination of apicoplast transcription in a malaria parasite by internal and host cues. (PNAS 2023)

- DOI: 10.1073/pnas.2214765120 | PMCID: PMC10334805 | PMID: 37406097
- Evidence: Amino acid sequences (regions 2 to 4) were aligned using ClustalW, and the alignment was refined by eye.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Clustal Omega] -> stage not stated [AlphaFold, ColabFold, R, UCSF Chimera]

### Qualitative metabolomics-based characterization of a phenolic UDP-xylosyltransferase with a broad substrate spectrum from &lt;i&gt;Lentinus brumalis&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2301007120 | PMCID: PMC10334773 | PMID: 37399371
- Evidence: To construct the phylogenetic tree of the UGT family, the UGT proteins were aligned by using ClustalW ( 84 ).
- Full pipeline: read trimming [R v3.26.8, Trim Galore v0.6.6, edgeR v3.26.8] -> alignment/mapping [Clustal Omega, HTSeq, MAFFT v7.310, R v3.26.8, edgeR v3.26.8] -> quantification [R v3.26.8, edgeR v3.26.8] -> normalisation [R v3.26.8, edgeR v3.26.8] -> stage not stated [AlphaFold, ColabFold, HISAT2, HMMER]

### Structure of the priming arabinosyltransferase AftA required for AG biosynthesis of <i>Mycobacterium tuberculosis</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302858120 | PMCID: PMC10265970 | PMID: 37252995
- Evidence: Protein sequence alignments were performed using Clustal Omega ( 51 ) and ESPript ( 52 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX v1.12] -> stage not stated [CTFFIND, ChimeraX, Docker, PyMOL, RDKit, UCSF Chimera]

### A tale of two copies: Evolutionary trajectories of moth pheromone receptors. (PNAS 2023)

- DOI: 10.1073/pnas.2221166120 | PMCID: PMC10193968 | PMID: 37155838
- Version used: **1.2.2**
- Evidence: For the phylogenetic analysis, OR amino acid sequences were aligned with Clustal Omega v1.2.2 ( 49 ) and the tree was built with PhyML v3.0 ( 50 ) Branch support was estimated using a SH-like approximate likelihood ratio-test ( 51 ).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2, MAFFT] -> dimensionality reduction/clustering [AlphaFold, R] -> structure determination [MAFFT] -> stage not stated [ChimeraX]

### Structure of WNT inhibitor adenomatosis polyposis coli down-regulated 1 (APCDD1), a cell-surface lipid-binding protein. (PNAS 2023)

- DOI: 10.1073/pnas.2217096120 | PMCID: PMC10193966 | PMID: 37155902
- Evidence: Structure-based multiple sequence alignment was performed using Clustal Omega ( 53 ) and ESPript ( 80 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CCP4, PyMOL, RoseTTAFold]

### The DedA superfamily member PetA is required for the transbilayer distribution of phosphatidylethanolamine in bacterial membranes. (PNAS 2023)

- DOI: 10.1073/pnas.2301979120 | PMCID: PMC10193950 | PMID: 37155911
- Version used: **1.2.4**
- Evidence: Multiple sequence alignments were performed using Clustal Omega version 1.2.4 ( 44 ) and visualized with Espript 3.0 ( 45 ).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4] -> visualisation [Clustal Omega v1.2.4] -> stage not stated [AlphaFold, ImageJ v2.3]

### CRISPR editing of CCR5 and HIV-1 facilitates viral elimination in antiretroviral drug-suppressed virus-infected humanized mice. (PNAS 2023)

- DOI: 10.1073/pnas.2217887120 | PMCID: PMC10175831 | PMID: 37126704
- Evidence: Sanger sequencing results were analyzed using the Clustal Omega (European Molecular Biology Laboratory (EMBL)-EBI) multiple sequence alignment tool. ddPCR Detection. ddPCR was performed based on the water–oil emulsion droplet technology with probes prepared in the QX200™ Droplet Digital™ PCR system (Bio-Rad Laboratories).
- Full pipeline: alignment/mapping [Clustal Omega]

### TapA acts as specific chaperone in TasA filament formation by strand complementation. (PNAS 2023)

- DOI: 10.1073/pnas.2217070120 | PMCID: PMC10151520 | PMID: 37068239
- Evidence: Alignment was then performed with MEGA11 ( 58 ) and the ClustalW algorithm ( 59 ) with default settings.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [AlphaFold, ColabFold] -> stage not stated [PyMOL]

### Bacterial origin of a key innovation in the evolution of the vertebrate eye. (PNAS 2023)

- DOI: 10.1073/pnas.2214815120 | PMCID: PMC10120077 | PMID: 37036996
- Evidence: Sequences were aligned using Clustal Omega ( 39 ), generating alignments found in Datasets S2–S4 .
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, BLAST, IQ-TREE, RAxML]

### <i>Starships</i> are active eukaryotic transposable elements mobilized by a new family of tyrosine recombinases. (PNAS 2023)

- DOI: 10.1073/pnas.2214521120 | PMCID: PMC10104507 | PMID: 37023132
- Evidence: Sequences were aligned using Clustal Omega ( 58 ) and a phylogeny was inferred using a Bayesian approach implemented in MrBayes using the HKY85 substitution model ( 42 ).
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega, MAFFT, MrBayes] -> differential/statistical testing [Clustal Omega, MrBayes] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.0.3]

### Structural insights into plasmalemma vesicle-associated protein (PLVAP): Implications for vascular endothelial diaphragms and fenestrae. (PNAS 2023)

- DOI: 10.1073/pnas.2221103120 | PMCID: PMC10083539 | PMID: 36996108
- Evidence: Structure-based multiple sequence alignment was performed using Clustal Omega ( 84 ) and ESPript ( 85 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [CCP4, PyMOL]

### Species-specific CD4<sup>+</sup> T cells enable prediction of mucosal immune phenotypes from microbiota composition. (PNAS 2023)

- DOI: 10.1073/pnas.2215914120 | PMCID: PMC10041165 | PMID: 36917674
- Evidence: The 16S rRNA sequences were aligned and pairwise distances were calculated with Clustal Omega ( 41 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ComplexHeatmap, ggplot2]

### Wheat &lt;i&gt;Ym2&lt;/i&gt; originated from &lt;i&gt;Aegilops sharonensis&lt;/i&gt; and confers resistance to soil-borne &lt;i&gt;Wheat yellow mosaic virus&lt;/i&gt; infection to the roots. (PNAS 2023)

- DOI: 10.1073/pnas.2214968120 | PMCID: PMC10089197 | PMID: 36897977
- Evidence: Madsen coding sequences using ClustalW software, and nucleotide variants called using a customized Perl script.
- Full pipeline: read trimming [BLAST, Bowtie2, HISAT2] -> alignment/mapping [Bowtie2, HISAT2] -> differential/statistical testing [edgeR] -> stage not stated [BCFtools v1.10, BWA, Clustal Omega, featureCounts v1.6.3]

### CENP-I directly targets centromeric DNA to support CENP-A deposition and centromere maintenance. (PNAS 2023)

- DOI: 10.1073/pnas.2219170120 | PMCID: PMC10089219 | PMID: 36888657
- Evidence: ( A ) Sequences alignment of the N-terminal tail between CENP-I orthologs across species using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ]

### The book of Lambda does not tell us that naturally occurring lysogens of <i>Escherichia coli</i> are likely to be resistant as well as immune. (PNAS 2023)

- DOI: 10.1073/pnas.2212121120 | PMCID: PMC10089163 | PMID: 36881631
- Version used: **1.2.3**
- Evidence: The malT sequences were in silico translated with an E. coli translation table to obtain the amino acid sequences of the MalT receptors; alignments were generated using Clustal Omega 1.2.3 using default parameters, and a graphical representation of the alignment was obtained using Geneious 2022.0.1.
- Full pipeline: alignment/mapping [Clustal Omega v1.2.3]

### Discovery of a rapidly evolving yeast defense factor, &lt;i&gt;KTD1&lt;/i&gt;, against the secreted killer toxin K28. (PNAS 2023)

- DOI: 10.1073/pnas.2217194120 | PMCID: PMC9974470 | PMID: 36800387
- Evidence: Protein sequence alignments were generated in Clustal Omega ( 71 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [ggpubr] -> visualisation [AlphaFold v2.0.0, PyMOL v2.3.0] -> stage not stated [BLAST, R, ggplot2 v3.3.5]

### Characterization of a unique polysaccharide monooxygenase from the plant pathogen <i>Magnaporthe oryzae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2215426120 | PMCID: PMC9974505 | PMID: 36791100
- Evidence: Sequences in Mo PMO9A-containing cluster (232 sequences) were aligned using Clustal Omega ( 84 ) and visualized with Jalview ( 85 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [ChimeraX, Clustal Omega, Cytoscape] -> visualisation [Clustal Omega, Cytoscape] -> stage not stated [AlphaFold, ColabFold, ImageJ, R]

### Pangenomic analysis reveals plant NAD<sup>+</sup> manipulation as an important virulence activity of bacterial pathogen effectors. (PNAS 2023)

- DOI: 10.1073/pnas.2217114120 | PMCID: PMC9963460 | PMID: 36753463
- Evidence: First, a multi-sequence alignment (MSA) was generated using ClustalW, and a consensus sequence for each OG was generated using hhcon.
- Full pipeline: alignment/mapping [Clustal Omega, HMMER] -> stage not stated [AlphaFold]

### Supramolecular organization and dynamics of mannosylated phosphatidylinositol lipids in the mycobacterial plasma membrane. (PNAS 2023)

- DOI: 10.1073/pnas.2212755120 | PMCID: PMC9945971 | PMID: 36693100
- Evidence: The sequence identity between Mtb and M. smegmatis for the F-ATPase was calculated using Clustal Omega ( 57 ) at 80% and 72% for c- and a-subunits, respectively.
- Full pipeline: simulation/modelling [GROMACS v2021.3, Python] -> stage not stated [AlphaFold, Clustal Omega, Matplotlib, PLUMED]

### Structure-function correlates of fibrinogen binding by <i>Acinetobacter</i> adhesins critical in catheter-associated urinary tract infections. (PNAS 2023)

- DOI: 10.1073/pnas.2212694120 | PMCID: PMC9942807 | PMID: 36652481
- Evidence: Protein alignments were conducted using Clustal Omega, Multiple Sequence Alignment ( https://www.ebi.ac.uk/Tools/msa/clustalo/ ) on default settings ( 22 ).
- Full pipeline: read trimming [PHENIX] -> alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS v2020.1] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Dimerization of the Alzheimer's disease pathogenic receptor SORLA regulates its association with retromer. (PNAS 2023)

- DOI: 10.1073/pnas.2212180120 | PMCID: PMC9942828 | PMID: 36652482
- Evidence: Subsequently, an alignment of the six SORLA 3Fn domains was generated based on their highly conserved pattern of secondary structures and few conserved amino acids using Clustal Omega software.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> stage not stated [AlphaFold, NAMD, PyMOL]

### Crystal structure of LGR ligand α2/β5 from <i>Caenorhabditis elegans</i> with implications for the evolution of glycoprotein hormones. (PNAS 2023)

- DOI: 10.1073/pnas.2218630120 | PMCID: PMC9910494 | PMID: 36574673
- Evidence: Sequence alignments were initially produced using Clustal Omega and then manually adjusted to align cysteine residues in the corresponding disulfide bridges based on actual structures if available or AlphaFold models of each homo/heterodimer.
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [CCP4] -> stage not stated [AlphaFold, ColabFold, PHENIX, PyMOL]

### Large-scale CRISPR/Cas9 deletions within the WFDC gene cluster uncover gene functionality and critical roles in mammalian reproduction. (PNAS 2024)

- DOI: 10.1073/pnas.2413195121 | PMCID: PMC11665854 | PMID: 39665756
- Evidence: This diagram was generated using the Clustal Omega Multiple Sequence Alignment program ( 9 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [R, limma]

### Electrochemical cofactor recycling of bacterial microcompartments. (PNAS 2024)

- DOI: 10.1073/pnas.2414220121 | PMCID: PMC11626177 | PMID: 39585991
- Evidence: Protein sequences were of MNdh were aligned with ClustalW ( 62 ) trimming with trimAl 1.2rev59 ( 63 ) with parameters -gt 0.6 -cons 30 -w 3.
- Full pipeline: read trimming [Clustal Omega] -> alignment/mapping [Clustal Omega, RAxML v0.6.0] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### The RING-type E3 ligase RIE1 sustains leaf longevity by specifically targeting AtACS7 to fine-tune ethylene production in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2411271121 | PMCID: PMC11621758 | PMID: 39565318
- Evidence: ( b ) A sequence alignment of all functional ACS proteins in Arabidopsis using Clustal Omega ( https://www.ebi.ac.uk/jdispatcher/msa/clustalo ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Artificial selection of two antagonistic E3 ubiquitin ligases finetunes soybean photoperiod adaptation and grain yield. (PNAS 2024)

- DOI: 10.1073/pnas.2321473121 | PMCID: PMC11551413 | PMID: 39485802
- Evidence: Amino acid sequences of ZTL proteins and their homologous proteins were aligned using ClustalW in MEGA and manually adjusted.
- Full pipeline: alignment/mapping [Clustal Omega]

### A myeloid differentiation-like protein in partnership with Toll5 from the pest insect &lt;i&gt;Spodoptera litura&lt;/i&gt; senses baculovirus infection. (PNAS 2024)

- DOI: 10.1073/pnas.2415398121 | PMCID: PMC11536157 | PMID: 39441638
- Evidence: Predicted ML proteins from S. litura were aligned using ClustalW ( https://www.genome.jp/tools-bin/clustalw ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [PyMOL] -> stage not stated [ImageJ]

### Structure and function of &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; EfpA as a lipid transporter and its inhibition by BRD-8000.3. (PNAS 2024)

- DOI: 10.1073/pnas.2412653121 | PMCID: PMC11536138 | PMID: 39441632
- Evidence: Protein sequence alignment was performed with Clustal Omega ( 62 ) and structure superposition was carried out in COOT.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4, Coot, UCSF Chimera]

### Cryo-EM structure of the zinc-activated channel (ZAC) in the Cys-loop receptor superfamily. (PNAS 2024)

- DOI: 10.1073/pnas.2405659121 | PMCID: PMC11536092 | PMID: 39441630
- Evidence: The sequence alignment was created by Clustal Omega ( 63 ) and ESPript 3.0 ( 64 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> registration [RELION] -> structure determination [PHENIX] -> stage not stated [CTFFIND v4.1, ChimeraX, PyMOL, UCSF Chimera]

### Cryo-EM structures of a mycobacterial ABC transporter that mediates rifampicin resistance. (PNAS 2024)

- DOI: 10.1073/pnas.2403421121 | PMCID: PMC11406275 | PMID: 39226350
- Evidence: Protein sequence alignments were performed using Clustal W and ESPript.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, GROMACS v2022.2, PyMOL, UCSF Chimera]

### Conserved moonlighting protein pyruvate dehydrogenase induces robust protection against &lt;i&gt;Staphylococcus aureus&lt;/i&gt; infection. (PNAS 2024)

- DOI: 10.1073/pnas.2321939121 | PMCID: PMC11388329 | PMID: 39186649
- Evidence: Multiple sequence alignment was executed by Clustal Omega ( 46 ).
- Full pipeline: read trimming [fastp v0.20.1] -> alignment/mapping [Clustal Omega] -> differential/statistical testing [DESeq2 v1.30.1]

### Identification of a family of peptidoglycan transpeptidases reveals that &lt;i&gt;Clostridioides difficile&lt;/i&gt; requires noncanonical cross-links for viability. (PNAS 2024)

- DOI: 10.1073/pnas.2408540121 | PMCID: PMC11348318 | PMID: 39150786
- Evidence: VanW domain sequences were aligned in Clustal Omega using default parameters as described in SI Appendix .
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, ColabFold v1.5.5]

### Polyomavirus ALTOs, but not MTs, downregulate viral early gene expression by activating the NF-κB pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2403133121 | PMCID: PMC11348336 | PMID: 39141346
- Evidence: Amino acid sequences were aligned using Clustal Omega to create a phylogenetic tree.
- Full pipeline: alignment/mapping [Clustal Omega, STAR] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [GSEA]

### Insights into the interaction between UGGT, the gatekeeper of folding in the ER, and its partner, the selenoprotein SEP15. (PNAS 2024)

- DOI: 10.1073/pnas.2315009121 | PMCID: PMC11348098 | PMID: 39133860
- Evidence: The filtered set of sequences was aligned using Clustal Omega ( 35 ) and uploaded to the webserver for ConSurf analysis.
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Structure of biofilm-forming functional amyloid PSMα1 from &lt;i&gt;Staphylococcus aureus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2406775121 | PMCID: PMC11331129 | PMID: 39116134
- Evidence: ( A ) Sequence alignment of the PSMα1-4 peptides generated using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [RELION] -> simulation/modelling [ChimeraX v1.7] -> structure determination [PHENIX]

### Convergent evolution in toxin detection and resistance provides evidence for conserved bacterial-fungal interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2304382121 | PMCID: PMC11317636 | PMID: 39088389
- Evidence: Sequences of PA4170 orthologs were aligned using ClustalW.
- Full pipeline: read trimming [Bowtie2 v2.4.2] -> alignment/mapping [Bowtie2 v2.4.2, Clustal Omega] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, PyMOL, featureCounts]

### Structural basis for mouse receptor recognition by bat SARS2-like coronaviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2322600121 | PMCID: PMC11317568 | PMID: 39083418
- Evidence: Multiple sequence alignments of SARS-CoV-2 (GISAID: EPI_ISL_402124), BANAL-236 (GenBank: MZ937003.2 ) and RaTG13 (GenBank: MN996532.2 ) were constructed using Clustal W in the Molecular Evolutionary Genetics Analysis (MEGA) software version 11 ( 43 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [CCP4, PHENIX] -> stage not stated [PyMOL]

### An ankyrin G-binding motif mediates TRAAK periodic localization at axon initial segments of hippocampal pyramidal neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2310120121 | PMCID: PMC11295008 | PMID: 39058579
- Evidence: Representative species within the chordate classes were selected and aligned using the Clustal Omega algorithm [CLUSTAL O (1.2.4)] through the UniProt align function.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [Python v3.9] -> stage not stated [AlphaFold, ImageJ, NumPy, napari]

### <i>Caenorhabditis elegans</i> RIG-I-like receptor DRH-1 signals via CARDs to activate antiviral immunity in intestinal cells. (PNAS 2024)

- DOI: 10.1073/pnas.2402126121 | PMCID: PMC11260149 | PMID: 38980902
- Evidence: Pairwise sequence alignment performed with Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold]

### Stearoylation cycle regulates the cell surface distribution of the PCP protein Vangl2. (PNAS 2024)

- DOI: 10.1073/pnas.2400569121 | PMCID: PMC11260150 | PMID: 38985771
- Evidence: ( E ) ClustalW alignment of N-terminal domain sequences of Vangl2 proteins across different species, including human, mouse, Xenopus , zebrafish, and Drosophila .
- Full pipeline: alignment/mapping [Clustal Omega]

### N6-methyladenosine modification of a parvovirus-encoded small noncoding RNA facilitates viral DNA replication through recruiting Y-family DNA polymerases. (PNAS 2024)

- DOI: 10.1073/pnas.2320782121 | PMCID: PMC11194592 | PMID: 38875150
- Evidence: As a base-pairing between EBER2 and nascent transcripts from the TRs of the EBV genome recruits the EBER2–PAX5 complex during viral lytic replication ( 17 ), we aligned the BocaSR sequence to the positive strands of HBoV1 LEH and REH, respectively, by using ClustalW ( 51 ).
- Full pipeline: alignment/mapping [Clustal Omega]

### A pyruvate transporter in the apicoplast of apicomplexan parasites. (PNAS 2024)

- DOI: 10.1073/pnas.2314314121 | PMCID: PMC11194499 | PMID: 38865262
- Evidence: Phylogenetic Analysis on APC Proteins Protein sequences were extracted from VEuPathDB and aligned by Clustal W in Molecular Evolutionary Genetics Analysis X (MEGA X) ( https://megasoftware.net/ ).
- Full pipeline: alignment/mapping [Clustal Omega]

### <i>Vibrio</i> MARTX toxin processing and degradation of cellular Rab GTPases by the cytotoxic effector Makes Caterpillars Floppy. (PNAS 2024)

- DOI: 10.1073/pnas.2316143121 | PMCID: PMC11194500 | PMID: 38861595
- Evidence: Amino acid sequences of Rab isoforms were aligned with ClustalW and manually inspected in MacVector v.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [QuPath] -> dimensionality reduction/clustering [ChimeraX v1.5, ColabFold v1.5.1] -> stage not stated [AlphaFold]

### Different ER-plasma membrane tethers play opposing roles in autophagy of the cortical ER. (PNAS 2024)

- DOI: 10.1073/pnas.2321991121 | PMCID: PMC11181077 | PMID: 38838012
- Evidence: ( A ) Alignment of a conserved portion of the SMP domain of Tcb3 with the corresponding regions of human E-Syts (ESYT1 and ESYT2) using Clustal Omega program.
- Full pipeline: alignment/mapping [Clustal Omega]

### The red alga <i>Porphyridium</i> as a host for molecular farming: Efficient production of immunologically active hepatitis C virus glycoprotein. (PNAS 2024)

- DOI: 10.1073/pnas.2400145121 | PMCID: PMC11181018 | PMID: 38833465
- Evidence: To analyze BiP conservation in P. purpureum , we used the inferred protein sequence (A0A5J4Z1M8) from Uniprot and blasted it against the known sequence of human BiP ( P11021 ) using Clustal Omega (EMBL-EBI).
- Full pipeline: stage not stated [Clustal Omega]

### Duplication and neofunctionalization of a horizontally transferred xyloglucanase as a facet of the Red Queen coevolutionary dynamic. (PNAS 2024)

- DOI: 10.1073/pnas.2218927121 | PMCID: PMC11181080 | PMID: 38830094
- Evidence: P. sojae GH12 protein sequences were aligned using Clustal Omega ( 75 , 76 ), and visualized in Jalview2 ( 77 ).
- Full pipeline: alignment/mapping [BLAST, Clustal Omega] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Clustal Omega] -> stage not stated [R v4.0.3]

### Principles of peptide selection by the transporter associated with antigen processing. (PNAS 2024)

- DOI: 10.1073/pnas.2320879121 | PMCID: PMC11161800 | PMID: 38805290
- Evidence: Multiple sequence alignments were generated using Clustal Omega ( 75 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, RELION]

### Three-component systems represent a common pathway for extracytoplasmic addition of pentofuranose sugars into bacterial glycans. (PNAS 2024)

- DOI: 10.1073/pnas.2402554121 | PMCID: PMC11127046 | PMID: 38748580
- Evidence: Multiple sequence alignments were performed in ClustalW ( 61 ) and TCoffee ( 62 ) (where indicated) and visualized using ESPript ( 63 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [Clustal Omega, PyMOL v2.5.4] -> stage not stated [AlphaFold]

### <i>Myxococcus xanthus</i> encapsulin cargo protein EncD is a flavin-binding protein with ferric reductase activity. (PNAS 2024)

- DOI: 10.1073/pnas.2400426121 | PMCID: PMC11126975 | PMID: 38748579
- Evidence: Sequence alignment was performed by Clustal Omega ( 51 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> structure determination [PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, ColabFold v1.5.3, MotionCor2, RELION v4.0]

### Tailored UPRE2 variants for dynamic gene regulation in yeast. (PNAS 2024)

- DOI: 10.1073/pnas.2315729121 | PMCID: PMC11087760 | PMID: 38687789
- Evidence: The sequence alignment was generated with Clustal Omega and visualized through Jalview.
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [Clustal Omega, PyMOL] -> stage not stated [AlphaFold]

### An essential and highly selective protein import pathway encoded by nucleus-forming phage. (PNAS 2024)

- DOI: 10.1073/pnas.2321190121 | PMCID: PMC11087766 | PMID: 38687783
- Evidence: ( G ) Clustal Omega generated protein sequence alignment of PhiPA3 gp108 and PhiKZ gp104. “*” denotes conserved amino acids. “:” and “.” denote highly similar and weakly similar amino acids, respectively.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, ImageJ]

### A conserved strategy to attack collagen: The activator domain in bacterial collagenases unwinds triple-helical collagen. (PNAS 2024)

- DOI: 10.1073/pnas.2321002121 | PMCID: PMC11032491 | PMID: 38593072
- Evidence: Multiple-sequence alignment of the AD of ColA from Clostridium perfringens ( P43153 ), ColG from Clostridium botulinum (B2TJU5), ColT from Clostridium tetani ( Q899Y1 ), ColG and ColH from Clostridium histolyticum ( Q9X721 & Q46085 ), ColQ1 from B. cereus ( B9J3S4 ) were performed using Clustal Omega ( 48 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [PyMOL]

### &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; telomere-binding proteins TEBP-1 and TEBP-2 adapt the Myb module to dimerize and bind telomeric DNA. (PNAS 2024)

- DOI: 10.1073/pnas.2316651121 | PMCID: PMC11032478 | PMID: 38588418
- Evidence: Alignment of sequences [using Clustal Omega ( 28 )] and structures (using AlphaFold-based ColabFold prediction ( 29 ) of TEBP-1 MCD3) of the MCD3 domain of TEBP-1 and TEBP-2 identified TEBP-1 R364, K412, S413, N416, S419, H420, R422, and K423 as equivalent to TEBP-2 DNA binding residues R357, K405, S406, N409, S412, H413, R415, and K416, suggesting that both proteins use a conserved mechanism to b...
- Full pipeline: alignment/mapping [Clustal Omega, ColabFold] -> structure determination [Coot] -> stage not stated [AlphaFold, PHENIX]

### A billion years of evolution manifest in nanosecond protein dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2318743121 | PMCID: PMC10927572 | PMID: 38412135
- Evidence: From the sequences, we generated a multiple sequence alignment using Clustal Omega (EMBL-EBI) ( 60 ) ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega, RoseTTAFold] -> stage not stated [ColabFold]

### Comparative chemical genomics in <i>Babesia</i> species identifies the alkaline phosphatase PhoD as a determinant of antiparasitic resistance. (PNAS 2024)

- DOI: 10.1073/pnas.2312987121 | PMCID: PMC10907312 | PMID: 38377214
- Evidence: Alignments of whole protein sequences and domain sequences were performed using Geneious v9.1.5, with standard alignment parameters (Neighbor joining clustering method, ClustalW alignment).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BEDTools, BWA, Clustal Omega, PyMOL v2.3.2, SAMtools, VCFtools] -> dimensionality reduction/clustering [Clustal Omega] -> stage not stated [AlphaFold]

### Design of universal Ebola virus vaccine candidates via immunofocusing. (PNAS 2024)

- DOI: 10.1073/pnas.2316960121 | PMCID: PMC10873634 | PMID: 38319964
- Evidence: Protein sequences of GP from six orthoebolavirus species (Ebola– AAG40168.1 , Sudan– AAU43887.1 , Bundibugyo– AYI50307.1 , Täi Forest– AAB37093.1 , Reston– AAC54891.1 and Bombali– ASJ82195.1 ) were aligned using Clustal Omega to create a multiple sequence alignment (MSA).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CellProfiler, Fiji v2.3.0, ImageJ v2.3.0, PyMOL]

### Viral afterlife: SARS-CoV-2 as a reservoir of immunomimetic peptides that reassemble into proinflammatory supramolecular complexes. (PNAS 2024)

- DOI: 10.1073/pnas.2300644120 | PMCID: PMC10861912 | PMID: 38306481
- Evidence: Clustal Omega is used to align SARS-CoV-2 proteins with corresponding proteins from five other human coronaviruses, including SARS-CoV (accession ID: NC_004718 ), HCoV-HKU1 (accession ID: DQ415908 ), HCoV-OC43 (accession ID: MW532115 ), HCoV-229E (accession ID: NC_002645 ), and HCoV-NL63 (accession ID: NC_005831 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [DESeq2 v1.34.0, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2 v1.34.0, clusterProfiler v4.2.2] -> visualisation [ChimeraX]

### A conserved hub protein required for peptidoglycan remodeling and cell division in &lt;i&gt;Acinetobacter baumannii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2529815122 | PMCID: PMC12772221 | PMID: 41428879
- Evidence: These genes could encode divergent LolB proteins [20.6% identity to E. coli LolB by Clustal Omega alignment ( 73 )].
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [STRING db]

### CDCA7 facilitates MET1-mediated CG DNA methylation maintenance in centromeric heterochromatin via linker histone H1. (PNAS 2025)

- DOI: 10.1073/pnas.2526408122 | PMCID: PMC12718391 | PMID: 41370347
- Evidence: To compare the proteins, alignments were carried out with Clustal Omega.
- Full pipeline: alignment/mapping [Bismark v0.19.1, Clustal Omega, STAR v2.7.11a] -> quantification [HTSeq v0.13.5] -> differential/statistical testing [DESeq2 v1.42.0] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Picard, Trim Galore v0.6.7, deepTools v3.0.2]

### Widespread promiscuous alkaline phosphatases underscore ancient microbial phosphite utilization. (PNAS 2025)

- DOI: 10.1073/pnas.2513042122 | PMCID: PMC12704751 | PMID: 41343678
- Evidence: A profile HMM (pHMM) for PhoA was constructed using a MSA of several annotated PhoA sequences generated by ClustalW.
- Full pipeline: stage not stated [AlphaFold, Clustal Omega]

### Lamprey &lt;i&gt;FOXN1&lt;/i&gt; rescues the block of thymic epithelial cell development in the mouse &lt;i&gt;Foxn1&lt;/i&gt;-deficient thymic rudiment. (PNAS 2025)

- DOI: 10.1073/pnas.2520664122 | PMCID: PMC12685072 | PMID: 41289399
- Evidence: Protein sequences were aligned using the Clustal W algorithm implemented in the DNAStar Lasergene suite of programmes ( https://www.dnastar.com ) or by Clustal Omega ( 51 ).
- Full pipeline: read trimming [Cutadapt v4.9, STAR v2.7.11b] -> alignment/mapping [Clustal Omega, HISAT2 v2.1.0, STAR v2.7.11b] -> differential/statistical testing [emmeans, limma] -> visualisation [STAR v2.7.11b] -> stage not stated [featureCounts v1.6.1]

### Coordinated transfer of DNA between Pol θ and Pol δ resets microhomology choice during double-strand break repair. (PNAS 2025)

- DOI: 10.1073/pnas.2513018122 | PMCID: PMC12663940 | PMID: 41259142
- Evidence: Sequencing results were analyzed by ClustalW alignment with reference sequence via MacVector software.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ImageJ]

### Rubisco is slow across the tree of life. (PNAS 2025)

- DOI: 10.1073/pnas.2501433122 | PMCID: PMC12663927 | PMID: 41248286
- Evidence: All sequences were then aligned and a distance matrix was computed using Clustal Omega ( 71 , 72 ).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.475] -> normalisation [UMAP] -> dimensionality reduction/clustering [MAFFT v7.475, UMAP] -> stage not stated [scikit-learn]

### Structure and encapsulation of carbonic anhydrase within the α-carboxysome. (PNAS 2025)

- DOI: 10.1073/pnas.2523723122 | PMCID: PMC12646314 | PMID: 41223214
- Evidence: Hn CsoSCA (UniProt ID O85042 ) and Cy CsoSCA (UniProt ID B5ILN4) sequences were aligned with Clustal Omega ( 66 ) and visualized with ESPript 3.0 ( 67 ).
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, Clustal Omega]

### Switching the strict substrate specificities of the β-ketoacyl-acyl carrier protein synthases, FabH and BioZ. (PNAS 2025)

- DOI: 10.1073/pnas.2509301122 | PMCID: PMC12625853 | PMID: 41183203
- Evidence: ( B ) Clustal W alignments of BioZ and FabH homologues from different bacterial species.
- Full pipeline: alignment/mapping [Clustal Omega]

### Male-derived PBP4 is essential for sperm competition by mediating sperm motility in moths. (PNAS 2025)

- DOI: 10.1073/pnas.2510155122 | PMCID: PMC12595504 | PMID: 41150721
- Evidence: The signal peptides predicted using SignalP-5.0 ( https://services.healthtech.dtu.dk/services/SignalP-5.0/ ) were removed, and then aligned using ClustalW with default parameters.
- Full pipeline: alignment/mapping [Clustal Omega]

### Functional diversity in GII.4 norovirus entry: HBGA binding and capsid clustering dynamics. (PNAS 2025)

- DOI: 10.1073/pnas.2517493122 | PMCID: PMC12519127 | PMID: 41032521
- Evidence: ( A ) Multiple sequence alignment of sequences from clustering and nonclustering GII.4 strains using ClustalW.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [Clustal Omega]

### Structural and functional analysis of the &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; MmpS5L5 efflux pump presages increased bedaquiline resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2516660122 | PMCID: PMC12501195 | PMID: 40986343
- Evidence: Protein sequences were aligned using Clustal Omega ( 93 ) and analyzed with Jalview ( 94 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION] -> structure determination [PHENIX v1.21.2] -> stage not stated [AlphaFold, ChimeraX, Coot v0.9.8.93]

### Structurally diverse viral inhibitors converge on a shared mechanism to stall the antigen transporter TAP. (PNAS 2025)

- DOI: 10.1073/pnas.2516676122 | PMCID: PMC12478189 | PMID: 40956880
- Evidence: Multiple sequence alignments were generated using Clustal Omega ( 76 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, RELION]

### Extracellular salt bridge networks around S4 implicated in HCN channel gating and heart disease. (PNAS 2025)

- DOI: 10.1073/pnas.2502136122 | PMCID: PMC12452848 | PMID: 40932774
- Evidence: The amino acid sequences were aligned using Clustal Omega ( 29 ) and shown using ESPript3 ( 30 ).
- Full pipeline: alignment/mapping [Clustal Omega]

### Female membrane proteins regulate postmating ovulation in &lt;i&gt;Drosophila melanogaster&lt;/i&gt; by ovulin-dependent and -independent pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2508783122 | PMCID: PMC12452909 | PMID: 40920921
- Evidence: Protein sequences from different species were then aligned using Clustal Omega ( 85 ), and inferred maximum likelihood trees were obtained with Simple Phylogeny from ClustalW2 package ( 85 ) and adjusted with a high-confidence reference phylogeny of 155 Drosophila genomes ( 86 ).
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE] -> variant calling [lme4] -> differential/statistical testing [emmeans, lme4] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL v2.5.5]

### &lt;i&gt;Pdgf&lt;/i&gt; mediates a transient regeneration-activated cell state in planarian tissue regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2501874122 | PMCID: PMC12435203 | PMID: 40892924
- Evidence: Multiple sequence alignment of these protein sequences was performed using ClustalW in MEGA X ( 70 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ImageJ, PyMOL v2.6.0] -> stage not stated [AlphaFold v2.2]

### STAGE: A compact and versatile TnpB-based genome editing toolkit for &lt;i&gt;Streptomyces&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2509146122 | PMCID: PMC12415229 | PMID: 40857323
- Evidence: ( C ) Partial sequence alignment of TnpB and TnpB*, generated using Clustal Omega and ESPript 3, with key conserved regions annotated.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS v2025.1] -> stage not stated [AlphaFold v3.0, ChimeraX]

### Mechanistic insights into the small-molecule inhibition of influenza A virus entry. (PNAS 2025)

- DOI: 10.1073/pnas.2503899122 | PMCID: PMC12377760 | PMID: 40802690
- Evidence: Sequences were aligned using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [Coot] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL]

### Structural insights into a citrate transporter that mediates aluminum tolerance in barley. (PNAS 2025)

- DOI: 10.1073/pnas.2501933122 | PMCID: PMC12358922 | PMID: 40763023
- Evidence: Protein sequences of 94 MATE transporters were aligned by ClustalW with the gap opening and gap extension penalties of 10 and 0.2, respectively.
- Full pipeline: alignment/mapping [Clustal Omega, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### C11orf54 catalyzes L-xylulose formation in human metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2506597122 | PMCID: PMC12337341 | PMID: 40737316
- Version used: **1.2.3**
- Evidence: Alignment was performed using Clustal Omega 1.2.3 and visualized with ESPript 3.0.
- Full pipeline: alignment/mapping [Clustal Omega v1.2.3] -> visualisation [Clustal Omega v1.2.3] -> stage not stated [AutoDock Vina v1.2.5, Cytoscape v3.9.1, PyMOL v2.5.0]

### Structural basis for the evolution of a domesticated group II intron-like reverse transcriptase to function in host cell DNA repair. (PNAS 2025)

- DOI: 10.1073/pnas.2504208122 | PMCID: PMC12337344 | PMID: 40729381
- Evidence: WebLogos were based on 130 G2L4 RTs and 500 GsI-IIC RTs identified by BLASTP as having ≥50% amino acid sequence identity aligned by ClustalW ( http://www.clustal.org/clustal2/ ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold v3.0]

### Threonine phosphorylation of STAT1 safeguards gut epithelial integrity and restricts interferon-mediated cytotoxicity. (PNAS 2025)

- DOI: 10.1073/pnas.2511957122 | PMCID: PMC12318237 | PMID: 40694331
- Evidence: Multiple sequence alignment of STAT1 peptide sequences from 22 vertebrate species was performed using Clustal Omega (EMBL-EBI) ( 45 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ImageJ v1.54]

### RACK1A positively regulates opening of the apical hook in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; via suppression of its auxin response gradient. (PNAS 2025)

- DOI: 10.1073/pnas.2407224122 | PMCID: PMC12318229 | PMID: 40690664
- Evidence: Sequences are aligned using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ]

### N<i>-</i>acetyltransferases required for iron uptake and aminoglycoside resistance promote virulence lipid production in <i>Mycobacterium marinum</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2502577122 | PMCID: PMC12305045 | PMID: 40680026
- Evidence: ( B ) Clustering by phylogenetic neighbor joining tree without distance corrections, generated based on protein alignments generated by Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [Clustal Omega] -> stage not stated [AlphaFold, PyMOL v2.4.0]

### The highly conserved C-terminal end segment of troponin T binds tropomyosin and actin to function in modulating contractile kinetics. (PNAS 2025)

- DOI: 10.1073/pnas.2507107122 | PMCID: PMC12260526 | PMID: 40591592
- Evidence: Amino acid sequences of the C-terminal end segment of representative vertebrate TnT isoforms were aligned with DNAStar MegAlign Pro software (Lasergene Inc, Madison, WI) using the Clustal W method to construct phylogenetic tree using the maximum-likelihood method algorithm with 100 bootstrap trials.
- Full pipeline: alignment/mapping [Clustal Omega]

### Structure of the virulence-associated &lt;i&gt;Neisseria meningitidis&lt;/i&gt; filamentous bacteriophage MDAΦ. (PNAS 2025)

- DOI: 10.1073/pnas.2420157122 | PMCID: PMC12207478 | PMID: 40540604
- Evidence: Sequence alignment of MCPs was performed using Clustal Omega as implemented on the EBI web server ( 52 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION, Topaz]

### Enzymatic carbon-fluorine bond cleavage by human gut microbes. (PNAS 2025)

- DOI: 10.1073/pnas.2504122122 | PMCID: PMC12184663 | PMID: 40512801
- Evidence: The resulting list of 114 protein sequences ( SI Appendix , Table S1 ) were aligned using Clustal Omega within the EMBL-EBI Framework ( 63 ) and the presence of the catalytic active residues were verified.
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [R] -> simulation/modelling [AlphaFold, GROMACS] -> visualisation [Cytoscape] -> stage not stated [ColabFold, IQ-TREE]

### Stepwise deactivation of gibberellins during rice internode elongation. (PNAS 2025)

- DOI: 10.1073/pnas.2415835122 | PMCID: PMC12167944 | PMID: 40465627
- Evidence: The amino acid sequences of EUI2 and epoxide hydrolases from potato ( Solanum tuberosum ), Arabidopsis ( A. thaliana ), and soybean ( Glycine max ) were aligned using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega]

### Concerted transport and phosphorylation of diacylglycerol at ER-PM contact sites regulate phospholipid dynamics during stress. (PNAS 2025)

- DOI: 10.1073/pnas.2421334122 | PMCID: PMC12167946 | PMID: 40455983
- Evidence: The protein sequences of all human and Arabidopsis DGKs were obtained from the UniProt database ( https://www.uniprot.org/ ), and the alignment was done by Clustal W ( https://www.ebi.ac.uk/Tools/msa/clustalo/ ) and phylogenetic analyses were conducted using the software MEGA X ( 82 ).
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Clustal Omega, Cufflinks v2.2.1, R] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [AlphaFold, ilastik]

### MyD88 knockdown by RNAi prevents bacterial stimulation of tubeworm metamorphosis. (PNAS 2025)

- DOI: 10.1073/pnas.2505805122 | PMCID: PMC12167997 | PMID: 40455987
- Evidence: Protein sequences of Hydroides homologs were aligned with D. melanogaster , Homo sapiens , Strongylocentrotus purpuratus , Hydra vulgaris, Crassostrea virginica, Magallana gigas, C. elegans, and/or Mizuhopecten yessoensis using Clustal Omega (ClustalO v1.2.3) alignment with mBed algorithm.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [Python]

### Identification of the lydiamycin biosynthetic gene cluster in a plant pathogen guides structural revision and identification of molecular target. (PNAS 2025)

- DOI: 10.1073/pnas.2424388122 | PMCID: PMC12130866 | PMID: 40388608
- Evidence: Sequences were aligned using ClustalW ( 74 ) and a phylogenetic tree was inferred using RAxML ( 75 ) at the CIPRES science gateway ( 76 ).
- Full pipeline: alignment/mapping [ChimeraX v1.5, Clustal Omega, RAxML] -> visualisation [Cytoscape v3.8.2] -> stage not stated [ColabFold v1.2]

### Structure and evolution of photosystem I in the early-branching cyanobacterium &lt;i&gt;Anthocerotibacter panamensis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2427090122 | PMCID: PMC12107172 | PMID: 40366692
- Evidence: Alignments were carried out with Clustal Omega ( 66 ), using 5 combined guided trees and HMM iterations.
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [IQ-TREE v2.2, RELION v3.1, UCSF Chimera]

### Microscopic basis of reaction center modulation in PsbA variants of photosystem II. (PNAS 2025)

- DOI: 10.1073/pnas.2417963122 | PMCID: PMC12107152 | PMID: 40354529
- Evidence: ( A ) Sequences of the three PsbA proteins (A1: T. vulcanus, A2 and A3: T. elongatus) compared using Clustal Omega.
- Full pipeline: simulation/modelling [VMD] -> stage not stated [Clustal Omega]

### Calcium-activated chloride channel TMEM16A opens via pi-helical transition in transmembrane segment 4. (PNAS 2025)

- DOI: 10.1073/pnas.2421900122 | PMCID: PMC12067253 | PMID: 40299692
- Evidence: Sequence alignment was done using the ClustalW program ( 79 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS, PyMOL v2.5] -> stage not stated [AlphaFold, ImageJ, MDAnalysis]

### MDA5 ISGylation is crucial for immune signaling to control viral replication and pathogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2420190122 | PMCID: PMC12002354 | PMID: 40184173
- Evidence: Primary sequence alignment of the amino acid regions containing K23 and K43 in orthologous MDA5 proteins was performed using Clustal Omega (1.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ]

### &lt;i&gt;Staphylococcus aureus&lt;/i&gt; uses a GGDEF protein to recruit diacylglycerol kinase to the membrane for lipid recycling. (PNAS 2025)

- DOI: 10.1073/pnas.2414696122 | PMCID: PMC11962490 | PMID: 40100631
- Version used: **1.2.2**
- Evidence: UniProtKB sequences from Bacillales were aligned with Clustal Omega 1.2.2 ( Datasets S3–S6 ) ( 58 ).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold v1.5.5]

### Conserved leucine-rich repeat proteins in the adhesive projectile slime of velvet worms. (PNAS 2025)

- DOI: 10.1073/pnas.2416282122 | PMCID: PMC11962477 | PMID: 40100627
- Evidence: Sequence alignment was performed using Clustal Omega tool on the European Molecular Biology Laboratory’s European Bioinformatics Institute website ( https://www.ebi.ac.uk/Tools/msa/clustalo/ ) and graphically enhanced either with ESPript 3.0 ( https://espript.ibcp.fr/ESPript/ESPript/ ) and/or Illustrator for Biological Sequences 2.0 ( https://ibs.renlab.org/#/server ) ( 42 , 43 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, ColabFold]

### A mechanistic basis for genetic assimilation in natural fly populations. (PNAS 2025)

- DOI: 10.1073/pnas.2415982122 | PMCID: PMC11929479 | PMID: 40063800
- Evidence: Clustal Omega multiple sequence alignment of the DNA amplification products (A, B, and C bands in gel) and the Drosophila melanogaster Cad96Ca reference mRNA sequence (NCBI RefSeq database: NM_143092.3 ).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.2, Clustal Omega, STAR v2.7.0] -> quantification [featureCounts] -> stage not stated [BEDTools v2.30.0, DESeq2, GATK, MACS2, R]

### Structural basis of SARS-CoV-2 polymerase inhibition by nonnucleoside inhibitor HeE1-2Tyr. (PNAS 2025)

- DOI: 10.1073/pnas.2419854122 | PMCID: PMC11912441 | PMID: 40035759
- Evidence: An MSA was then calculated using Clustal Omega ( 63 , 64 ).
- Full pipeline: alignment/mapping [RELION] -> normalisation [ChimeraX] -> stage not stated [Clustal Omega, PHENIX]

### tRNA selectivity during ribosome-associated quality control regulates the critical sterility-inducing temperature in two-line hybrid rice. (PNAS 2025)

- DOI: 10.1073/pnas.2417526122 | PMCID: PMC11831146 | PMID: 39913205
- Evidence: Multiple sequence alignments were generated using Clustal Omega and displayed using Jalview.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.2.9, Clustal Omega] -> structure determination [Cutadapt v1.18] -> stage not stated [ImageJ, RoseTTAFold]

### PgpP is a broadly conserved phosphatase required for phosphatidylglycerol lipid synthesis. (PNAS 2025)

- DOI: 10.1073/pnas.2418775122 | PMCID: PMC11804483 | PMID: 39869797
- Evidence: Clustal Omega V1.2.4 ( 44 ) was used to align the yeast GEP4 (UniProt P38812 ), B. subtilis 168 PgpP (UniProt P54452 ) and S. aureus NCTC8325 PgpP (UniProt Q2FXX9 ) proteins.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, PyMOL v2.5.3]

### Antiviral Mx proteins have an ancient origin and widespread distribution among eukaryotes. (PNAS 2025)

- DOI: 10.1073/pnas.2416811122 | PMCID: PMC11789081 | PMID: 39854241
- Evidence: We used Clustal Omega ( 128 ) or MAFFT ( 55 ) to align sequences obtained from the same query.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT]

### Itaconate mechanism of action and dissimilation in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2423114122 | PMCID: PMC11789021 | PMID: 39841148
- Evidence: We performed multiple sequence alignment using Clustal Omega to identify and predict the conserved residues involved in substrate binding ( 44 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, AutoDock Vina]

### Structural and functional dynamics of human cone cGMP-phosphodiesterase important for photopic vision. (PNAS 2025)

- DOI: 10.1073/pnas.2419732121 | PMCID: PMC11725853 | PMID: 39739818
- Evidence: ( C ) Clustal Omega multiple sequence alignment of the C termini of Pγ subunits.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UCSF Chimera] -> structure determination [ChimeraX, Coot, PHENIX, UCSF Chimera] -> stage not stated [Topaz]

### Electron transfer in polysaccharide monooxygenase catalysis. (PNAS 2025)

- DOI: 10.1073/pnas.2411229121 | PMCID: PMC11725913 | PMID: 39793048
- Evidence: S8 ) using Clustal Omega ( 48 ).
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, Clustal Omega]

### Metabolic enhancement contributed by horizontal gene transfer is essential for dietary specialization in leaf beetles. (PNAS 2025)

- DOI: 10.1073/pnas.2415717122 | PMCID: PMC11725898 | PMID: 39793087
- Evidence: A total of 784 single-copy genes were concatenated into a supergene for multiple sequence alignment with ClustalW with default parameters ( 53 ).
- Full pipeline: alignment/mapping [Clustal Omega, SAMtools v1.17] -> stage not stated [IQ-TREE v2.2.2.6, OrthoFinder v2.5.4, RepeatMasker v2.0.4, eggNOG, fastp v0.23.4]

### Synapse-specific catecholaminergic modulation of neuronal glutamate release. (PNAS 2025)

- DOI: 10.1073/pnas.2420496121 | PMCID: PMC11725921 | PMID: 39793084
- Evidence: The resulting protein sequence for Unc13A H1723K was checked via ClustalW ( 45 ) to confirm the occurrence of the singular H1723K mutation.
- Full pipeline: stage not stated [Clustal Omega, ImageJ, Python]

### Genome-wide analysis of mRNA regionalization in a giant single cell. (PNAS 2026)

- DOI: 10.1073/pnas.2537760123 | PMCID: PMC13291615 | PMID: 42296355
- Evidence: We performed multiple sequence alignment using a ClustalW ( 29 ) web server ( https://www.genome.jp/tools-bin/clustalw ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [kallisto] -> normalisation [kallisto] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [kallisto]

### Mutational analyses of an instability domain reveal its conserved role in the regulation of class-B ARF levels in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2537963123 | PMCID: PMC13250565 | PMID: 42234526
- Evidence: Fifteen class-B ARFs from Arabidopsis and maize ARF28 were aligned using Clustal W.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ]

### MCM8-9 helicase activity protects primordial germ cell development to prevent premature ovarian insufficiency. (PNAS 2026)

- DOI: 10.1073/pnas.2535910123 | PMCID: PMC13167731 | PMID: 42085144
- Evidence: ( A ) Sequence alignment across the MCM protein family using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega]

### Fatty acid regulation of feeding in &lt;i&gt;Caenorhabditis&lt;/i&gt; elegans reveals the potential ancestral origin of a GLP-1-like multiagonist signaling system. (PNAS 2026)

- DOI: 10.1073/pnas.2530979123 | PMCID: PMC13056082 | PMID: 41911448
- Evidence: ( A ) Sequence alignment of PDF-1a ( G8JYC6 ) peptide with human GLP1 and related peptides involved in regulating food intake, metabolism, and gastrointestinal function performed using the Clustal Omega program.
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega]

### Inhibition of coronaviral exoribonuclease activity by TRIM-mediated SUMOylation. (PNAS 2026)

- DOI: 10.1073/pnas.2528398123 | PMCID: PMC13037866 | PMID: 41871251
- Evidence: Primary sequence alignments of coronaviral Nsp14 proteins were performed using Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, PyMOL]

### Huntington's disease LIG1 modifier variant increases ligase fidelity and suppresses somatic CAG repeat expansion. (PNAS 2026)

- DOI: 10.1073/pnas.2518854123 | PMCID: PMC12974472 | PMID: 41770933
- Evidence: ( B ) Multiple sequence alignment of LIG1 orthologs by Clustal Omega.
- Full pipeline: alignment/mapping [Clustal Omega]

### Functional integrity of the SEL1L-HRD1 complex is critical for endoplasmic reticulum-associated degradation and organismal viability. (PNAS 2026)

- DOI: 10.1073/pnas.2517927123 | PMCID: PMC12891039 | PMID: 41642983
- Evidence: ( B ) ClustalW sequence alignment demonstrating evolutionary conservation of residues L709 (red) and P699 (green).
- Full pipeline: alignment/mapping [Clustal Omega]

### Origin of class B J-domain proteins involved in amyloid transactions. (PNAS 2026)

- DOI: 10.1073/pnas.2522403123 | PMCID: PMC12799103 | PMID: 41512017
- Version used: **1.2.2**
- Evidence: We used Hmmer1.3b1. to generate two profiles based on the well-characterized class A and B C sequences from model systems ( E. coli , A. thaliana , S. cerevisiae, and H. sapiens ) aligned with Clustal Omega v1.2.2.
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega v1.2.2]

### Detoxification of conifer antimicrobial defenses promotes entomopathogenic fungus infection of bark beetles. (PNAS 2026)

- DOI: 10.1073/pnas.2525513122 | PMCID: PMC12773783 | PMID: 41461027
- Version used: **1.2.2**
- Evidence: Phylogenetic analysis of GT and MT proteins was performed on the amino acid sequences using Clustal Omega 1.2.2, and a UPGMA tree was generated using Geneious Prime.
- Full pipeline: stage not stated [AlphaFold, Clustal Omega v1.2.2]

### Mosaic RBD nanoparticles protect against challenge by diverse sarbecoviruses in animal models. (Science 2022)

- DOI: 10.1126/science.abq0839 | PMCID: PMC9273039 | PMID: 35857620
- Evidence: ( D ) Phylogenetic tree of selected sarbecoviruses calculated using PhyML 3.0 ( 90 ) based on amino acid sequences of RBDs aligned using Clustal Omega ( 91 ).
- Full pipeline: alignment/mapping [Clustal Omega]

### Avian-origin influenza A viruses tolerate elevated pyrexic temperatures in mammals. (Science 2025)

- DOI: 10.1126/science.adq4691 | PMCID: PMC7618609 | PMID: 41308154
- Evidence: Residue distribution analysis Representative PB1 protein sequences were aligned using Clustal Omega, the alignment was used for maximum likelihood phylogenetic analysis using standard approaches ( 95 ), and the residue counts at the sites of interest were extracted from subtrees from each pandemic lineage (1918, 1957, 1968, and 2009).
- Full pipeline: alignment/mapping [Clustal Omega]

### Cat1 forms filament networks to degrade NAD&lt;sup&gt;+&lt;/sup&gt; during the type III CRISPR-Cas antiviral response. (Science 2025)

- DOI: 10.1126/science.adv9045 | PMCID: PMC12162218 | PMID: 40208959
- Evidence: Protein sequences for these homologs were downloaded and aligned in Geneious version 2022.2.1 using the built in Clustal Omega alignment tool with default parameters.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold]

### Structural mechanism of LINE-1 target-primed reverse transcription. (Science 2025)

- DOI: 10.1126/science.ads8412 | PMCID: PMC7617806 | PMID: 40048554
- Evidence: ( 108 ) and aligned using Clustal Omega ( 109 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, PHENIX v1.21.1, RELION] -> stage not stated [CTFFIND, ChimeraX, ImageJ, MotionCor2, PyMOL, Python, REFMAC, Topaz]

