# AlphaFold

- **Category:** structbio
- **Papers in survey:** 1197
- **Journals:** PNAS (842), Nature (268), Science (45), Cell (41), NEJM (1)
- **Years:** 2021 (6), 2022 (109), 2023 (240), 2024 (295), 2025 (408), 2026 (139)
- **Versions named:** 2.0 (7), 2.2.0 (4), 2.3.2 (4), 3.0 (4), 2.3.1 (3), 2.1.0 (3), 2.2 (2), 2.3 (2), 2.1.1 (2), 2.3.0 (1)
- **Pipeline stages it appears in:** structure determination (71), alignment/mapping (46), dimensionality reduction/clustering (38), machine learning (27), visualisation (26), simulation/modelling (21), differential/statistical testing (5), quantification (3), normalisation (2), read trimming (1), quality control (1)

## Papers

### Deep mutational learning predicts ACE2 binding and antibody escape to combinatorial mutations in the SARS-CoV-2 receptor-binding domain. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.024 | PMCID: PMC9428596 | PMID: 36150393
- Evidence: Structural Prediction of RBD variants by AlphaFold2 Structural predictions were generated with the Alphafold v2.1.0 public iPython notebook using residues 331-530 of the spike protein.
- Full pipeline: alignment/mapping [PyMOL v2.2.3] -> differential/statistical testing [R v4.0] -> machine learning [Keras, TensorFlow v2.5] -> visualisation [Matplotlib v3.3.4, NumPy v1.19.2, PyMOL v2.2.3] -> stage not stated [AlphaFold, ComplexHeatmap v2.4.3, Cytoscape, Python, ggplot2 v3.3.3, igraph v1.2.6, pheatmap v1.0.12, tidyverse v1.0.6]

### BacPROTACs mediate targeted protein degradation in bacteria. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.009 | PMCID: PMC9240326 | PMID: 35662409
- Evidence: ...gene Cat#20188 pGOAL-19 plasmid ( Parish and Stoker, 2000 ) addgene Cat#20190 Software and algorithms MicroCal PEAQ-ITC Analysis Software Malvern N/A AlphaFold ( Jumper et al., 2021 ), ( Varadi et al., 2022 ) N/A DSF data analysis ( Niesen et al., 2007 ) ftp://ftp.sgc.ox.ac.uk/pub/biophysics cryoSPARC v2 ( Punjani et al., 2017 ) https://cryosparc.com/ MotionCor2 1.0.5 ( Zheng et al., 2017 ) https:...
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX, Coot, MotionCor2 v1.0.5, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### A family of conserved bacterial virulence factors dampens interferon responses by blocking calcium signaling. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.028 | PMCID: PMC9596379 | PMID: 35568036
- Evidence: The atomic model of OspC1 was generated with AlphaFold ( Jumper et al., 2021 ), with default parameters.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [DESeq2 v1.28.0, GSEA, R] -> differential/statistical testing [GSEA] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BLAST, ImageJ, Nextflow, RSEM, Singularity]

### SARS-CoV-2 Omicron-B.1.1.529 leads to widespread escape from neutralizing antibody responses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.046 | PMCID: PMC8723827 | PMID: 35081335
- Version used: **0.01**
- Evidence: Alphafold Models of Omicron RBD and NTD were derived using AlphaFold 2.0.01 ( Jumper et al., 2021 ) downloaded and installed on 11 th August 2021 in batch mode.
- Full pipeline: differential/statistical testing [Python v3.7] -> stage not stated [AlphaFold v0.01, PHENIX, PyMOL]

### Systematic identification and characterization of genes in the regulation and biogenesis of photosynthetic machinery. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.007 | PMCID: PMC10760936 | PMID: 38065083
- Evidence: Indeed, we found that MTF1 has a similar AlphaFold-predicted structure to the known E. coli enzyme MTF, with the active-site key residues and hydrophobic pocket conserved 63 , 64 ( Figures S7E and S7F ).
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [SciPy] -> stage not stated [AlphaFold, Cutadapt, PyMOL]

### De novo protein identification in mammalian sperm using in situ cryoelectron tomography and AlphaFold2 docking. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.017 | PMCID: PMC10842264 | PMID: 37865089
- Evidence: After downloading the AlphaFold2 library of the mouse proteome, this code is used to distribute PDB files into subdirectories. i=0; for f in *; do ## Splitting 50 PDBs in each subdirectory d=dir_$(printf %03d $((i/50+1))); mkdir -p $d; mv “$f” $d; let i++; done This code is used to unbiasedly match all PDBs with the target densities in each subdirectory: for file in * do echo $file ## CCDC105_flip...
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler v4.4.1] -> differential/statistical testing [Bioconductor] -> visualisation [IMOD] -> stage not stated [AlphaFold, ChimeraX, ColabFold, Coot v0.9.8.1, MotionCor2, R, RELION, UCSF Chimera]

### ADP-ribosylation from molecular mechanisms to therapeutic implications. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.030 | PMCID: PMC10789625 | PMID: 37832523
- Evidence: 28 (B) Domain composition of all human PARP proteins based on both experimental studies and computational predictions, including AlphaFold 2 models.
- Full pipeline: stage not stated [AlphaFold]

### Synthetic Par polarity induces cytoskeleton asymmetry in unpolarized mammalian cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.034 | PMCID: PMC10765089 | PMID: 37774705
- Evidence: 55 https://napari.org/ Protein structure predictions Par6A AlphaFold2 https://alphafold.ebi.ac.uk/entry/Q9NPB6 * GG refers to the tricistronic His-PC-GBP-TM-VSVG-GBP + Flag iRFP670-Jupiter + PC-GFP-[protein of interest] ** TetOn refers to a bicistronic rtTA3 + Tet promoter driving the given ORF Resource Availability Lead contact Further information and requests for resources and reagents should be...
- Full pipeline: dimensionality reduction/clustering [ImageJ] -> stage not stated [AlphaFold, napari]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Evidence: (D) List of predicted dockings between peptides and receptors, the peptide and receptor names and annotations (same as above), the pLDDT AlphaFold2 score of model quality, pDockQ docking scores and its associated positive predictive value, and the FoldX ΔΔG value of the positive interaction.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### Genetic manipulation of Patescibacteria provides mechanistic insights into microbial dark matter and the epibiotic lifestyle. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.017 | PMCID: PMC10633639 | PMID: 37683634
- Evidence: 44 N/A phmmer and jackhmmer Eddy 40 N/A AlphaFold Jumper et al.
- Full pipeline: alignment/mapping [MUSCLE, minimap2] -> dimensionality reduction/clustering [R] -> stage not stated [AlphaFold, ChimeraX v1.6.1, Flye v2.9, HMMER]

### Structural basis for ion selectivity in potassium-selective channelrhodopsins. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.009 | PMCID: PMC7615185 | PMID: 37652010
- Evidence: Model building and refinement Initial models of Hc KCR1 WT and Hc KCR2 WT were formed by rigid body fitting of the predicted models of Hc KCR1 WT and Hc KCR2 WT, respectively, generated using locally installed AlphaFold2.
- Full pipeline: structure determination [AlphaFold, Coot, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Kilosort v2.5, MotionCor2, RELION v4.0, UCSF Chimera]

### Phage-assisted evolution and protein engineering yield compact, efficient prime editors. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.039 | PMCID: PMC10482982 | PMID: 37657419
- Evidence: (F) AlphaFold-predicted structure of the Ec48 RT enzyme.
- Full pipeline: stage not stated [AlphaFold, Python]

### Mechanism of orphan subunit recognition during assembly quality control. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.016 | PMCID: PMC10501995 | PMID: 37480851
- Evidence: 37 PDB: 3KCI AlphaFold2-predicted model of human CCT4 ( P50991 ) Varadi et al.
- Full pipeline: differential/statistical testing [R] -> stage not stated [AlphaFold, ChimeraX v1.3, ColabFold v1.2]

### TMEM106B is a receptor mediating ACE2-independent SARS-CoV-2 cell entry. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.005 | PMCID: PMC10409496 | PMID: 37421949
- Evidence: 83 http://molprobity.manchester.ac.uk/ AlphaFold Jumper et al.
- Full pipeline: quantification [ImageJ] -> structure determination [Coot] -> machine learning [Topaz] -> stage not stated [AlphaFold, CTFFIND v1.06, PHENIX, RELION v4.0, UCSF Chimera]

### Structure of the endosomal Commander complex linked to Ritscher-Schinzel syndrome. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.003 | PMCID: PMC10187114 | PMID: 37172566
- Evidence: ...ce NCBI O14972 VPS29 human protein sequence NCBI Q9UBQ0 DENND10/FAM45A human protein sequence NCBI Q8TCE6 COMMD1-10+ CCDC22 (1–223) + CCDC93 (1–300) (AlphaFold2 Multimer prediction) Model Archive ( https://www.modelarchive.org ) ma-iplv4 CCDC22+ CCDC93 (AlphaFold2 Multimer prediction) Model Archive ( https://www.modelarchive.org ) ma-9nv72 VPS35L + VPS26C+ VPS29 (AlphaFold2 Multimer prediction) Mo...
- Full pipeline: alignment/mapping [ColabFold, MAFFT, PyMOL] -> normalisation [CCP4] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, HMMER v3.3.2, PHENIX, RELION, Topaz]

### Molecular mechanisms of stress-induced reactivation in mumps virus condensates. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.015 | PMCID: PMC10156176 | PMID: 37116470
- Evidence: 98 https://github.com/irenedet/3d-unet/tree/7bc343971bdb818c5de90570b83731c8d77cde04 AlphaFold2 Evans et al.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [Bioconductor] -> structure determination [Coot, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, BWA v0.7.17, ChimeraX v1.1.1, IMOD, PHENIX v1.18, Picard, R v3.6, RELION v3.0, freebayes v1.1.0, limma]

### Cryo-EM structure of gas vesicles for buoyancy-controlled motility. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.041 | PMCID: PMC9994262 | PMID: 36868215
- Evidence: 48 https://www.cgl.ucsf.edu/chimera/download.html AlphaFold2 Jumper et al.
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX v1.4, ColabFold, HMMER, ImageJ, PHENIX v1.13, RELION v3.1, SciPy]

### Genome integrity sensing by the broad-spectrum Hachiman antiphage defense complex. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.020 | PMCID: PMC12278908 | PMID: 39395413
- Evidence: First, a predicted AlphaFold2 structure of each defense-associated helicase was aligned to the core helicase domain of HamB (PDB ID: 8VXA, this work, residues 286–472, 500–731) 17 , 75 , 91 within the core helicase domain were inferred.
- Full pipeline: alignment/mapping [AlphaFold, IQ-TREE] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX v1.20.1] -> machine learning [Topaz] -> visualisation [IQ-TREE, Matplotlib, seaborn] -> stage not stated [ColabFold, MUSCLE, Python]

### Structural insights into the diversity and DNA cleavage mechanism of Fanzor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.050 | PMCID: PMC11423790 | PMID: 39208796
- Evidence: Model building For the structures of the GtFz1 complexes and PpFz1 complexes, protein models predicted by AlphaFold2 42 , 44 and an ωRNA model generated by RNAcomposer 40 were used as initial models.
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX v1.7, PHENIX v1.18] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, RELION v4.0, UCSF Chimera v1.16]

### Mining human microbiomes reveals an untapped source of peptide antibiotics. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.027 | PMCID: PMC12821620 | PMID: 39163860
- Evidence: Given that AlphaFold is known to predict high-confidence α-helical structures for even spurious small proteins (<100 amino acid residues), 39 we probed the secondary structure tendencies of the peptides through circular dichroism in trifluoroethanol (TFE) and water mixtures (3:2, v:v).
- Full pipeline: read trimming [BWA, Trim Galore] -> alignment/mapping [BLAST, BWA, SPAdes, Trim Galore] -> quantification [featureCounts] -> normalisation [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, ColabFold]

### A replisome-associated histone H3-H4 chaperone required for epigenetic inheritance. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.006 | PMCID: PMC11380579 | PMID: 39094570
- Evidence: All AlphaFold-Multimer-predicted structures and modeled structures are deposited on ModelArchive under the accession number ma-dm-hisrep and are publicly available on the date of publication.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> dimensionality reduction/clustering [ChimeraX, Clustal Omega, ColabFold, UCSF Chimera] -> stage not stated [AlphaFold, Bowtie2, MACS2]

### The fork protection complex promotes parental histone recycling and epigenetic memory. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.017 | PMCID: PMC11383432 | PMID: 39094569
- Evidence: Guided by AlphaFold predictions, we found that Mrc1 binds H3-H4 tetramers and that Mrc1 and Mcm2 act together, co-binding H3-H4 tetramers to facilitate their transmission to the lagging strand.
- Full pipeline: differential/statistical testing [R v4.2.2] -> visualisation [PyMOL v1.2r, ggpubr v0.6.0] -> stage not stated [AlphaFold, Bowtie2 v2.4.2, ChimeraX, MACS2, SAMtools v1.12, deepTools]

### Molecular mechanism of distinct chemokine engagement and functional divergence of the human Duffy antigen receptor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.005 | PMCID: PMC11349380 | PMID: 39089252
- Evidence: Model building and validation The starting coordinates for DARC was derived from an AlphaFold model (AF- Q4VBN9 -F1-model_v4) 112 while the coordinates of CCL7 was obtained from a previously solved crystal structure of chemokine binding protein of orf virus complexed with CCL7 (PDB: 4ZKC ).
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> registration [MotionCor2] -> visualisation [R v3.7] -> stage not stated [AlphaFold, ChimeraX, PHENIX, RELION v4.0, UCSF Chimera]

### Extensive structural rearrangement of intraflagellar transport trains underpins bidirectional cargo transport. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.041 | PMCID: PMC11349379 | PMID: 39067443
- Evidence: Description of steps for subtomogram averaging and AlphaFold modeling of the retrograde train, related to Figure 1 Methods S2.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2, RELION]

### Minimal and hybrid hydrogenases are active from archaea. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.032 | PMCID: PMC11216029 | PMID: 38866018
- Evidence: See codon-optimized sequences in Table S5 N/A Software and algorithms AlphaFold multimer v2.1.1 Tunyasuvunakool et al.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [Nextflow] -> stage not stated [AlphaFold, BLAST, Clustal Omega v1.2.2, HMMER v3.2.1, IQ-TREE v1.6.12, MAFFT v7.304, R, StringTie v2.2.1]

### A pseudoautosomal glycosylation disorder prompts the revision of dolichol biosynthesis. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.041 | PMCID: PMC11250103 | PMID: 38821050
- Evidence: However, in a high-confidence model predicted by AlphaFold 21 , 22 the amino acids substituted in patients (Thr49, Val181, and Leu215) are located in the hydrophobic core of the protein ( Figures 1 E and 1F).
- Full pipeline: stage not stated [AlphaFold, Clustal Omega, ImageJ]

### Rapid DNA unwinding accelerates genome editing by engineered CRISPR-Cas9. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.031 | PMCID: PMC11658890 | PMID: 38781968
- Evidence: Nevertheless, fast-advancing computational tools for protein structural prediction, as exemplified by AlphaFold-latest 46 that has been used to predict the ternary structure of Casλ, 47 can be possibly used to assist the rational engineering of other CRISPR genome editors.
- Full pipeline: structure determination [Coot v0.9.8.7] -> stage not stated [AlphaFold, ChimeraX v1.6.1, ColabFold, PHENIX v1.19.2, Python, Topaz, fastp]

### Synthetic protein circuits for programmable control of mammalian cell death. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.031 | PMCID: PMC11127782 | PMID: 38657604
- Evidence: 105 To examine molecules whose structures are not available, such as engineered GSDMA containing a TEVP cleavage site or leucine zippers, we generated models using AlphaFold2 (ColabFold v1.5.2).
- Full pipeline: visualisation [ImageJ, Matplotlib, PyMOL] -> stage not stated [AlphaFold, ColabFold v1.5.2, Jupyter]

### Global, site-resolved analysis of ubiquitylation occupancy and turnover rate reveals systems properties. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.024 | PMCID: PMC11136510 | PMID: 38626770
- Evidence: The predicted structure of selected human PM-SLC and PM-associated TM (PM-TM) proteins was retrieved from AlphaFold Protein Structure Database.
- Full pipeline: stage not stated [AlphaFold, ComplexHeatmap v2.6.2, PyMOL v2.5.0, Python v3.7.1, R, ggplot2 v3.3.5, tidyverse v1.0.5]

### Mastigoneme structure reveals insights into the O-linked glycosylation code of native hydroxyproline-rich helices. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.005 | PMCID: PMC11015965 | PMID: 38552624
- Evidence: Model building Initial atomic models were generated using AlphaFold2 and ColabFold.
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, ColabFold, InterProScan]

### RAF-like protein kinases mediate a deeply conserved, rapid auxin response. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.021 | PMCID: PMC10783624 | PMID: 38128538
- Evidence: 115 RRID: SCR_003032 http://cytoscape.org AlphaFold2 Jumper et al.
- Full pipeline: quality control [FastQC v0.11.9, HISAT2 v2.1.0] -> visualisation [ggplot2, tidyverse] -> stage not stated [AlphaFold, Cytoscape v3.10.1, DESeq2, ImageJ, MAFFT v7.505, OrthoFinder, featureCounts v2.0.0]

### Uncovering phenotypic inheritance from single cells with Microcolony-seq. (Cell 2025)

- DOI: 10.1016/j.cell.2025.08.001 | PMCID: PMC12456302 | PMID: 40865524
- Evidence: (C) Predicted secondary structures for BfpA and PilW were obtained by AlphaFold.
- Full pipeline: quality control [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> alignment/mapping [Cutadapt, FastQC, Python v3.7.12, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, DESeq2, Prokka, R]

### Principles of cotranslational mitochondrial protein import. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.021 | PMCID: PMC12396113 | PMID: 40795856
- Evidence: In silico protein structure prediction The structure of COQ3-repeat was predicted using ColabFold, 64 a Google Colab-based implementation of AlphaFold, 71 using default settings.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1] -> alignment/mapping [Bowtie2 v2.4.5, STAR v2.7.10a] -> stage not stated [AlphaFold, ColabFold]

### Transcriptional regulation by PHGDH drives amyloid pathology in Alzheimer's disease. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.045 | PMCID: PMC12204802 | PMID: 40273909
- Evidence: 17 , 27 In the AlphaFold folded PHGDH structure, we observed a helix-helix-turn-helix (HHTH) subdomain within the nucleotide binding domain, spanning from amino acid (aa) 103 to 165 (63 aa), which exhibits structural similarity to the three amino acid loop extension (TALE) homeodomain, a DNA-binding structural motif ( Figures S6A – S6C ).
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [Bowtie2, SAMtools, fastp] -> quantification [Bowtie2, fastp] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bowtie2, fastp] -> visualisation [R] -> stage not stated [AlphaFold, HOMER v4.11, MACS2, Seurat, deepTools]

### Molecular basis for shifted receptor recognition by an encephalitic arbovirus. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.029 | PMCID: PMC12406711 | PMID: 40187345
- Evidence: Model building For the WEEV CBA87 VLP: Hs PCDH10 EC1 -Fc, we used coordinates of PCDH10 EC1 from the crystal structure of human PCDH10 EC1–EC4 (PDB:6VFQ) 19 and of WEEV E2–E1 and capsid predicted by AlphaFold2 69 as initial models.
- Full pipeline: structure determination [ChimeraX, Coot v0.9.8.91, PHENIX v1.21r, UCSF Chimera v1.6.1] -> stage not stated [AlphaFold, CTFFIND, MotionCor2 v1.6.4, PyMOL v3.0.2, RELION v3.1]

### Mechanism of DNA capture by the MukBEF SMC complex and its inhibition by a viral DNA mimic. (Cell 2025)

- DOI: 10.1016/j.cell.2025.02.032 | PMCID: PMC7617805 | PMID: 40168993
- Evidence: 82 https://github.com/soedinglab/hh-suite AlphaFold2 Jumper et al.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [AlphaFold, ChimeraX, MAFFT, PHENIX, RELION]

### Therapeutic potential of allosteric HECT E3 ligase inhibition. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.001 | PMCID: PMC12087876 | PMID: 40179885
- Evidence: Figure S2 Structural details of inhibitor binding to SMURF1, conservation of lysine residues on α helix #1, and AlphaFold model of the SMURF1:BMPR2 complex, related to Figures 1 , 2 , 4 , and 6 (A) Crystallography parameters. ∗ The highest resolution shell is shown in parenthesis.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [AlphaFold, PyMOL]

### Multiple independent acquisitions of ACE2 usage in MERS-related coronaviruses. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.031 | PMCID: PMC12360793 | PMID: 39922191
- Evidence: 9 Furthermore, the two insertions and elongated α-helix in the RBM present in AlphaFold2-predicted structures 26 potentially affect receptor recognition ( Figure 1F ).
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [RELION] -> structure determination [IQ-TREE, RELION, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PHENIX, Topaz]

### Structural and functional analysis of the Nipah virus polymerase complex. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.021 | PMCID: PMC11813165 | PMID: 39837328
- Evidence: ...w.graphpad.com , RRID: SCR_002798 UNICORN™ version 7.8 Cytiva https://www.cytivalifesciences.com/en/us/shop/chromatography/software/unicorn-7-p-05649 AlphaFold Server Abramson et al.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.5, Clustal Omega, Coot v0.9, MotionCor2 v1.6.4, PHENIX v1.20.1, PyMOL v2.5.5, RELION v3.1.1, UCSF Chimera v1.15]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Evidence: 217 https://anndata.readthedocs.io/en/stable/ AlphaFold Protein Structure Database Jumper et al. and Fleming et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### The unique architecture of umbrella toxins permits a two-tiered molecular bet-hedging strategy for interbacterial antagonism. (Cell 2026)

- DOI: 10.1016/j.cell.2025.10.044 | PMCID: PMC13274773 | PMID: 41338195
- Evidence: 57 http://www2.mrc-lmb.cam.ac.uk/relion AlphaFold3 Abramson et al.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.8, HMMER, ImageJ, RELION v5.0, UCSF Chimera]

### Adenoviral Inciting Antigen and Somatic Hypermutation in VITT. (NEJM 2026)

- DOI: 10.1056/nejmoa2514824 | PMCID: PMC12900036 | PMID: 41671482
- Evidence: 10 Panel B shows representative paratopes modeled by AlphaFold3 webserver.
- Full pipeline: stage not stated [AlphaFold]

### Transposon-associated TnpB is a programmable RNA-guided DNA endonuclease. (Nature 2021)

- DOI: 10.1038/s41586-021-04058-1 | PMCID: PMC8612924 | PMID: 34619744
- Evidence: Most recently, as the highly accurate AlphaFold2 structure prediction method 45 became publicly available, we sought further investigation of the TnpB structure.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [AlphaFold, Cutadapt, Python]

### Highly accurate protein structure prediction for the human proteome. (Nature 2021)

- DOI: 10.1038/s41586-021-03828-1 | PMCID: PMC8387240 | PMID: 34293799
- Evidence: The structure prediction process was largely as described in the AlphaFold paper 2 , consisting of five steps: MSA construction, template search, inference with five models, model ranking based on mean pLDDT and constrained relaxation of the predicted structures.
- Full pipeline: alignment/mapping [PyMOL] -> machine learning [AlphaFold] -> stage not stated [AutoDock Vina]

### Highly accurate protein structure prediction with AlphaFold. (Nature 2021)

- DOI: 10.1038/s41586-021-03819-2 | PMCID: PMC8371605 | PMID: 34265844
- Evidence: Using our CASP14 configuration for AlphaFold, the trunk of the network is run multiple times with different random choices for the MSA cluster centres (see Supplementary Methods 1.11.2 for details of the ensembling procedure).
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> simulation/modelling [OpenMM v7.3.1] -> machine learning [HMMER, NumPy, OpenMM v7.3.1, Python, TensorFlow]

### Direct activation of a bacterial innate immune system by a viral capsid protein. (Nature 2022)

- DOI: 10.1038/s41586-022-05444-z | PMCID: PMC9712102 | PMID: 36385533
- Evidence: To explore the conformational dynamics of the enzyme, we used AlphaFold 33 to predict possible alternative structures of CapRel SJ46 .
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> stage not stated [AlphaFold, BLAST, CCP4, PHENIX]

### Cryo-EM structure of the SEA complex. (Nature 2022)

- DOI: 10.1038/s41586-022-05370-0 | PMCID: PMC9646525 | PMID: 36289347
- Evidence: Model building Structure predictions for Sea2, Sea3, Sea4, Sea1, Npr2 and Npr3 were downloaded from the AlphaFold data base 14 ( https://alphafold.ebi.ac.uk/ ).
- Full pipeline: quantification [ImageJ v1.52p] -> structure determination [PHENIX v1.20.1] -> visualisation [ChimeraX v1.3] -> stage not stated [AlphaFold, Coot v0.9.8.1, RELION v4.0, UCSF Chimera v1.15]

### Structure of the OMEGA nickase IsrB in complex with ωRNA and target DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05324-6 | PMCID: PMC9581776 | PMID: 36224386
- Evidence: Model building and validation The initial protein model was generated using AlphaFold2 (ref.
- Full pipeline: alignment/mapping [MAFFT, MotionCor2] -> structure determination [ColabFold, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND, Python]

### Structure of the Ebola virus polymerase complex. (Nature 2022)

- DOI: 10.1038/s41586-022-05271-2 | PMCID: PMC9517992 | PMID: 36171293
- Evidence: AlphaFold2 prediction of EBOV L The whole structure of EBOV L protein was predicted by AlphaFold2 64 with default settings.
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [ImageJ] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold]

### A wheat resistosome defines common principles of immune receptor channels. (Nature 2022)

- DOI: 10.1038/s41586-022-05231-w | PMCID: PMC9581773 | PMID: 36163289
- Evidence: Supplementary PDB Files AlphaFold2 structure predictions of Sr35, Ta SH1, Hv SH1, Hv MLA10 and Hv MLA13.
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX v1.15, PHENIX v1.18.2] -> visualisation [ChimeraX v1.15] -> stage not stated [AlphaFold, RELION v3.1]

### Identification of trypsin-degrading commensals in the large intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-05181-3 | PMCID: PMC9477747 | PMID: 36071157
- Evidence: AlphaFold modelling The amino acids sequences of 00502 from P. clara , P. xylaniohila , P. rara , P. rodentium and P. muris were retrieved from GenBank ( NZ_JH376591 , EGG54658 , LFQU01000025 , NZ_JABKKH010000006 and NZ_JABKKF010000005 , respectively).
- Full pipeline: read trimming [BWA, Canu v1.8] -> alignment/mapping [BWA, ChimeraX, PyMOL] -> quantification [BWA] -> normalisation [BWA] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, ColabFold, Prokka, fastp v0.20.0, minimap2 v2.17]

### A phosphoinositide signalling pathway mediates rapid lysosomal repair. (Nature 2022)

- DOI: 10.1038/s41586-022-05164-4 | PMCID: PMC9450835 | PMID: 36071159
- Evidence: AlphaFold structure of ATG2A was visualized in the PyMOL Molecular Graphics System, Version 2.4.0 Schrödinger, LLC.
- Full pipeline: quantification [ImageJ] -> visualisation [AlphaFold, PyMOL]

### Discovery, structure and mechanism of a tetraether lipid synthase. (Nature 2022)

- DOI: 10.1038/s41586-022-05120-2 | PMCID: PMC9433317 | PMID: 35882349
- Evidence: AlphaFold model of GDGT–MAS The AlphaFold model of GDGT–MAS from M. jannaschii can be accessed from UniProt accession number Q58036 (refs.
- Full pipeline: structure determination [Coot] -> visualisation [Cytoscape, PyMOL] -> stage not stated [AlphaFold, PHENIX]

### Structure of the Dicer-2-R2D2 heterodimer bound to a small RNA duplex. (Nature 2022)

- DOI: 10.1038/s41586-022-04790-2 | PMCID: PMC9279153 | PMID: 35768503
- Evidence: Supporting this notion, in the Dicer-2 structure predicted by AlphaFold2 (ref.
- Full pipeline: structure determination [ChimeraX] -> stage not stated [AlphaFold, Clustal Omega, PHENIX, RELION]

### Structural basis for SHOC2 modulation of RAS signalling. (Nature 2022)

- DOI: 10.1038/s41586-022-04838-3 | PMCID: PMC9452301 | PMID: 35768504
- Evidence: Towards the end of this process, the predicted structure of SHOC2 became available in the AlphaFold Protein Structure Database 61 ( https://alphafold.ebi.ac.uk/entry/Q9UQ13 ), and the LRR portion of the predicted structure was used as a molecular replacement solution.
- Full pipeline: structure determination [ChimeraX, PHENIX] -> machine learning [CCP4] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Cryo-EM structure of a type IV secretion system. (Nature 2022)

- DOI: 10.1038/s41586-022-04859-y | PMCID: PMC9259494 | PMID: 35732732
- Evidence: Using AlphaFold 36 , a deep learning method to predict 3D structures, we generated a model for the VirB4–VirB11 interaction for both R388 VirB4–VirB11 and the paralogue from the related pKM101 plasmid (TraB–TraG) (Extended Data Fig.
- Full pipeline: registration [CTFFIND v4.1] -> simulation/modelling [Coot] -> structure determination [Coot, PHENIX v1.18.2, RELION v3.1] -> machine learning [AlphaFold] -> stage not stated [ChimeraX v1.1, HMMER, PyMOL v2.3.2]

### Mechanism of mitoribosomal small subunit biogenesis and preinitiation. (Nature 2022)

- DOI: 10.1038/s41586-022-04795-x | PMCID: PMC9200640 | PMID: 35676484
- Evidence: Structure prediction of RBFA by AlphaFold2 (ref.
- Full pipeline: registration [RELION v3.0] -> differential/statistical testing [limma v3.34.9] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CCP4 v7.0, ChimeraX v0.91]

### Discovery of non-squalene triterpenes. (Nature 2022)

- DOI: 10.1038/s41586-022-04773-3 | PMCID: PMC9177416 | PMID: 35650436
- Evidence: AlphaFold2 prediction and docking analysis UCSF Chimera 58 (version 1.12) and AutoDock Vina 59 (version 1.1.2) were used to perform receptor and ligand preparation and molecular docking analysis.
- Full pipeline: alignment/mapping [Clustal Omega v2.0.12, RELION] -> visualisation [PyMOL] -> stage not stated [AlphaFold, AutoDock Vina, CTFFIND, PHENIX v1.19.2, UCSF Chimera]

### USP14-regulated allostery of the human proteasome by time-resolved cryo-EM. (Nature 2022)

- DOI: 10.1038/s41586-022-04671-8 | PMCID: PMC9117149 | PMID: 35477760
- Evidence: Initial model of the full-length USP14 was first derived from a predicted one by AlphaFold 57 , which was verified by comparing to a crystal structure 5 (PDB 2AYO).
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, Coot, EMAN2, MotionCor2, RELION]

### Structural basis of tethered agonism of the adhesion GPCRs ADGRD1 and ADGRF1. (Nature 2022)

- DOI: 10.1038/s41586-022-04580-w | PMCID: PMC9046087 | PMID: 35418679
- Evidence: Model building and refinement The models of the ADGRD1– and ADGRF1–G protein complexes were built by recruitment of the receptors from AlphaFold predicted models 44 , the subunits of Gα i , Gβ and Gγ from the glucagon–GCGR–G i structure (Protein Data Bank (PDB) ID: 6LML), and the Gα s and Nb35 from the glucagon–GCGR–G s structure (PDB: 6LMK) as initial templates.
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, ChimeraX v1.1, Coot, PHENIX] -> visualisation [PyMOL v1.8, UCSF Chimera v1.15] -> stage not stated [CTFFIND v1.18, RELION v3.1]

### Age-dependent formation of TMEM106B amyloid filaments in human brains. (Nature 2022)

- DOI: 10.1038/s41586-022-04650-z | PMCID: PMC9095482 | PMID: 35344985
- Evidence: In the absence of an experimentally determined native structure, we examined the structure of TMEM106B as predicted by AlphaFold 23 (Extended Data Fig.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [AlphaFold, CTFFIND, Coot]

### Activation mechanism of PINK1. (Nature 2022)

- DOI: 10.1038/s41586-021-04340-2 | PMCID: PMC8828467 | PMID: 34933320
- Evidence: AlphaFold structure prediction The structure of Hs PINK1 as predicted by AlphaFold2 was obtained from the AlphaFold Protein Structure Database ( https://alphafold.ebi.ac.uk/ ) 37 , 38 .
- Full pipeline: structure determination [Coot v0.9] -> visualisation [ChimeraX v1.1.1] -> stage not stated [AlphaFold, ColabFold, EMAN2, Fiji v1.53k, ImageJ v1.53k, PHENIX v1.19.2, RELION v3.1, UCSF Chimera]

### Bacterial cGAS senses a viral RNA to initiate immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06743-9 | PMCID: PMC10686824 | PMID: 37968393
- Evidence: A structure of the Ssc-CdnE03 was predicted using AlphaFold (ColabFold).
- Full pipeline: alignment/mapping [Bowtie2, PyMOL, Python] -> visualisation [Bowtie2] -> stage not stated [AlphaFold, ColabFold]

### The social and structural architecture of the yeast protein interactome. (Nature 2023)

- DOI: 10.1038/s41586-023-06739-5 | PMCID: PMC10700138 | PMID: 37968396
- Evidence: AlphaFold-Multimer version 2.2.0 (ref.
- Full pipeline: visualisation [ChimeraX v1.4, Cytoscape, Matplotlib, NumPy v1.20.3] -> stage not stated [AlphaFold, NetworkX v2.6.2, Python]

### Plant carbonic anhydrase-like enzymes in neuroactive alkaloid biosynthesis. (Nature 2023)

- DOI: 10.1038/s41586-023-06716-y | PMCID: PMC10700139 | PMID: 37938780
- Evidence: The structures of Pt CAL-1a, Pt CAL-2a and Pt CAL-3 were modelled using AlphaFold2 through ColabFold (v.1.5.2) 48 .
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [edgeR] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, ColabFold v1.5.2, HMMER]

### Structure of the native myosin filament in the relaxed cardiac sarcomere. (Nature 2023)

- DOI: 10.1038/s41586-023-06690-5 | PMCID: PMC10665186 | PMID: 37914933
- Evidence: Model building and visualization of the thick filament The model of the thick filament was built using a combination of previously available models and AlphaFold2 predictions 28 .
- Full pipeline: alignment/mapping [ChimeraX, IMOD] -> registration [IMOD] -> structure determination [IMOD] -> visualisation [AlphaFold] -> stage not stated [RELION v3.1]

### Structure and electromechanical coupling of a voltage-gated Na&lt;sup&gt;+&lt;/sup&gt;/H&lt;sup&gt;+&lt;/sup&gt; exchanger. (Nature 2023)

- DOI: 10.1038/s41586-023-06518-2 | PMCID: PMC10620092 | PMID: 37880360
- Evidence: Model building and refinement of SLC9C1 in GDN, nanodiscs and GDN with cAMP The SLC9C1 homology model was taken from AlphaFold 55 and each domain was extensively refitted into the C 2 GDN map using the fit in map utility of Chimera 56 and rebuilt extensively in Coot 57 .
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX] -> stage not stated [PyMOL]

### Antiviral type III CRISPR signalling via conjugation of ATP and SAM. (Nature 2023)

- DOI: 10.1038/s41586-023-06620-5 | PMCID: PMC10600005 | PMID: 37853119
- Evidence: Structural modelling of B. fragilis Cas10 and B. fragilis CorA The structure of the B. fragilis Cas10–Cas5 heterodimer and B. fragilis CorA monomer were predicted using AlphaFold2 50 , 51 (AF2) as implemented by the Colabfold server 52 .
- Full pipeline: visualisation [R v4.1, ggplot2] -> stage not stated [AlphaFold, Snakemake v7.22.0]

### Structures illustrate step-by-step mitochondrial transcription initiation. (Nature 2023)

- DOI: 10.1038/s41586-023-06643-y | PMCID: PMC10600007 | PMID: 37821701
- Evidence: Furthermore, the AlphaFold prediction of y-mtRNAP (UniProt ID: P13433 ) was used for modelling the insertion region (y-ins, residues 1232 to 1328).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.19.2] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, RELION v3.1]

### Unraveling the functional dark matter through global metagenomics. (Nature 2023)

- DOI: 10.1038/s41586-023-06583-7 | PMCID: PMC10584684 | PMID: 37821698
- Evidence: MSAs with at least 0.5 average probability were selected for AlphaFold prediction, alongside the MSAs with enough effective sequences.
- Full pipeline: alignment/mapping [Clustal Omega, Python] -> dimensionality reduction/clustering [Clustal Omega] -> differential/statistical testing [R] -> stage not stated [AlphaFold, HMMER v3.1, ggplot2]

### Proteome census upon nutrient stress reveals Golgiphagy membrane receptors. (Nature 2023)

- DOI: 10.1038/s41586-023-06657-6 | PMCID: PMC10620096 | PMID: 37757899
- Evidence: ColabFold implementation of AlphaFold 23 predicts a YIPF3–YIPF4 heterodimer, with both N-terminal regions being largely unstructured (Fig.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### piRNA processing by a trimeric Schlafen-domain nuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06588-2 | PMCID: PMC10567574 | PMID: 37758951
- Evidence: Phases were determined by molecular replacement using the AlphaFold model of the C. elegans TOFU-6 eTUDOR domain (residues 120–314) ( https://alphafold.ebi.ac.uk/entry/Q09293 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt v4.0] -> alignment/mapping [BEDTools, SAMtools v1.10, featureCounts v2.0.0] -> differential/statistical testing [ggplot2] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, ColabFold, ImageJ, PHENIX]

### Cryo-EM structures reveal native GABA&lt;sub&gt;A&lt;/sub&gt; receptor assemblies and pharmacology. (Nature 2023)

- DOI: 10.1038/s41586-023-06556-w | PMCID: PMC10550821 | PMID: 37730991
- Evidence: The starting structures used were AlphaFold 65 models of mouse GABA A R subunits and the best 8E3 Fab model generated with Rosetta 66 .
- Full pipeline: structure determination [Coot] -> stage not stated [AlphaFold, CCP4, ChimeraX, Python, RELION]

### Clustering predicted structures at the scale of the known protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06510-w | PMCID: PMC10584675 | PMID: 37704730
- Evidence: The AlphaFold Protein Structure Database (AFDB) is a publicly available data repository of protein structures and their confidence metrics, predicted using the AlphaFold2 AI system 1 , 2 .
- Full pipeline: stage not stated [AlphaFold, BLAST, ChimeraX v1.5, ColabFold, Matplotlib v3.6.2, seaborn v0.12.2]

### Bacterial pathogens deliver water- and solute-permeable channels to plant cells. (Nature 2023)

- DOI: 10.1038/s41586-023-06531-5 | PMCID: PMC10511319 | PMID: 37704725
- Evidence: AlphaFold2 analysis and cryo-EM imaging To gain functional insights into the AvrE family of bacterial effectors, we constructed their three-dimensional models predicted by AlphaFold2 26 using the fast homology search of MMseqs2 (ColabFold) 27 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [AlphaFold, ColabFold] -> stage not stated [PyMOL v1.8.0.4]

### Uncovering new families and folds in the natural protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06622-3 | PMCID: PMC10584680 | PMID: 37704037
- Evidence: Shape-mers for all AFDB90 structural representative AlphaFold models were calculated following the approach described in the analysis of AFDBv1 (ref.
- Full pipeline: quality control [scikit-learn v1.1.1] -> alignment/mapping [BLAST, MUSCLE] -> machine learning [PyTorch v1.12.0, scikit-learn v1.1.1] -> visualisation [NetworkX v2.5.1, PyMOL v2.5.0] -> stage not stated [AlphaFold, HMMER v3.3, SciPy v1.5.4]

### Structural mobility tunes signalling of the GluA1 AMPA glutamate receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06528-0 | PMCID: PMC10533411 | PMID: 37704721
- Evidence: The reference structure restraints were prepared with ProSmart 61 using AlphaFold2 predicted models from the Alpha Fold DB 62 , 63 .
- Full pipeline: structure determination [Coot, PHENIX, Python, RELION] -> stage not stated [AlphaFold, ChimeraX, MotionCor2, PyMOL, UCSF Chimera]

### Polθ is phosphorylated by PLK1 to repair double-strand breaks in mitosis. (Nature 2023)

- DOI: 10.1038/s41586-023-06506-6 | PMCID: PMC10499603 | PMID: 37674080
- Evidence: AlphaFold calculations A series of five models were calculated for the complex between TOPBP1 BRCT7-8 and the Polθ peptide E1472–Y1498 in its non-phosphorylated and phosphomimetic (phosphorylated serines being replaced by glutamic acids) states.
- Full pipeline: visualisation [ggplot2] -> stage not stated [AlphaFold]

### Pervasive downstream RNA hairpins dynamically dictate start-codon selection. (Nature 2023)

- DOI: 10.1038/s41586-023-06500-y | PMCID: PMC10499604 | PMID: 37674078
- Evidence: Moreover, through comparisons of protein amino acid sequences, functional domains and structures predicted by AlphaFold 44 , we found that RH11, RH37, and RH52 are orthologous to the yeast Ded1p and human DDX3X (Extended Data Fig.
- Full pipeline: quality control [Cutadapt, FastQC, MultiQC v1.9, Trim Galore v0.6.6] -> read trimming [Bowtie2 v2.4.2, Cutadapt, FastQC, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [AlphaFold, STAR v2.7.8a]

### Identification of an alternative triglyceride biosynthesis pathway. (Nature 2023)

- DOI: 10.1038/s41586-023-06497-4 | PMCID: PMC10482677 | PMID: 37648867
- Evidence: Homology modelling and data analysis The DIESL AlphaFold 22 model was accessed via the EMBL–EBI portal ( https://alphafold.ebi.ac.uk/ ) and visualized using PyMOL.
- Full pipeline: visualisation [AlphaFold, PyMOL] -> stage not stated [ImageJ]

### Direct observation of the conformational states of PIEZO1. (Nature 2023)

- DOI: 10.1038/s41586-023-06427-4 | PMCID: PMC10468401 | PMID: 37587339
- Evidence: Using the AlphaFold II structure of the PIEZO1 blade, we calculated the inter-PIEZO repeat binding energy (−∆ G ) for domain interfaces 43 , with and without the contribution of intracellular and extracellular loops, including domains expected to increase interdomain binding strength, such as the beam (Fig.
- Full pipeline: stage not stated [AlphaFold]

### A viral ADP-ribosyltransferase attaches RNA chains to host proteins. (Nature 2023)

- DOI: 10.1038/s41586-023-06429-2 | PMCID: PMC10468400 | PMID: 37587340
- Evidence: Alphafold prediction of ModB structure The Alphafold prediction of ModB structure was performed with AlphaFold2.ipynb (v.1.3.0, https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ) with default parameters (use_templates = false, use_amber = false; msa_mode = MMseqs2 (UniRef+Environmental), model_type = “AlphaFold2-ptm”, max_msa = null, pair_mode = unpaired+pair...
- Full pipeline: quality control [Cutadapt v1.18, FastQC v0.11.9] -> read trimming [Cutadapt v1.18, FastQC v0.11.9] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.7, featureCounts v2.0.1] -> differential/statistical testing [R v4.2.2, ggpubr] -> stage not stated [AlphaFold, ColabFold, PyMOL]

### Central role of Tim17 in mitochondrial presequence protein translocation. (Nature 2023)

- DOI: 10.1038/s41586-023-06477-8 | PMCID: PMC10511324 | PMID: 37527780
- Evidence: Samples were analysed by SDS–PAGE and autoradiography. b 2 -Tim17, b 2 (84) +7 -DHFR-Tim17 crosslinking product; i, intermediate; p, precursor. d , Immunodecoration depicting the mass shift of tagged Tim17 2xStrep and HisSUMOstar Tim23. e , AlphaFold model of full-length Tim17 ( Saccharomyces cerevisiae ; AF- P39515 ).
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.6.1, ColabFold, ImageJ v1.49v, PyMOL]

### Small protein modules dictate prophage fates during polylysogeny. (Nature 2023)

- DOI: 10.1038/s41586-023-06376-y | PMCID: PMC10432266 | PMID: 37495698
- Evidence: AlphaFold and DALI structural prediction of phage TF 72 and TF 63 AlphaFold2 (ref.
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, Prokka v1.11, Python]

### Mega-scale experimental analysis of protein folding stability in biology and design. (Nature 2023)

- DOI: 10.1038/s41586-023-06328-6 | PMCID: PMC10412457 | PMID: 37468638
- Evidence: We then predicted the structures of these PDB sequences using AlphaFold (even though the PDB structures were known), and used the AlphaFold models to trim amino acids from the N- and C termini that had a low number of contacts with any other residues.
- Full pipeline: read trimming [Cutadapt] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [AlphaFold, Python v3.9]

### Diverse modes of H3K36me3-guided nucleosomal deacetylation by Rpd3S. (Nature 2023)

- DOI: 10.1038/s41586-023-06349-1 | PMCID: PMC10432269 | PMID: 37468628
- Evidence: AlphaFold was used to predict and determine the special knotted coil in Rco1 52 .
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, RELION, UCSF Chimera]

### PLSCR1 is a cell-autonomous defence factor against SARS-CoV-2 infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06322-y | PMCID: PMC10371867 | PMID: 37438530
- Evidence: MDS analysis A coarse-grained simulation using the AlphaFold 57 structure of PLSCR1 with the N-terminal region truncated was assembled using the insane.py Python script 58 , memembed (ref.
- Full pipeline: alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2, R] -> simulation/modelling [AlphaFold, GROMACS v2021.3, Python] -> stage not stated [PyMOL, VMD]

### De novo design of protein structure and function with RFdiffusion. (Nature 2023)

- DOI: 10.1038/s41586-023-06415-8 | PMCID: PMC10468394 | PMID: 37433327
- Evidence: We reasoned that improved diffusion models for protein design could be developed by taking advantage of the deep understanding of protein structure implicit in powerful structure prediction methods such as AlphaFold2 (ref.
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold]

### Fanzor is a eukaryotic programmable RNA-guided endonuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06356-2 | PMCID: PMC10432273 | PMID: 37380027
- Evidence: Construction of a non-redundant eukaryotic structural database The sequences of the 214 million models of eukaryotic protein contained in the AlphaFold EBI database 25 were extracted and clustered at 50% of sequence identity and 50% of coverage with mmseqs2 v.12 (ref.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> registration [MotionCor2] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.4, PHENIX v1.18] -> stage not stated [BLAST, CTFFIND v1.18, HMMER v3.3.2, PyMOL v1.2, RELION v4.0]

### Phase separation of FSP1 promotes ferroptosis. (Nature 2023)

- DOI: 10.1038/s41586-023-06255-6 | PMCID: PMC10338336 | PMID: 37380771
- Evidence: Predicted cartoon structure of hFSP1 WT (yellow) S187C (green), L217R (cyan), and Q319K (magenta) by AlphaFold2 or ColabFold.
- Full pipeline: visualisation [CellProfiler v4.1.3] -> stage not stated [AlphaFold, ColabFold, Fiji, ImageJ]

### Structure and function of the RAD51B-RAD51C-RAD51D-XRCC2 tumour suppressor. (Nature 2023)

- DOI: 10.1038/s41586-023-06179-1 | PMCID: PMC7614784 | PMID: 37344587
- Evidence: BCDX2 structure was modelled using a locally installed version of AlphaFold2 64 .
- Full pipeline: alignment/mapping [ChimeraX] -> machine learning [RELION v3.1] -> stage not stated [AlphaFold, Fiji, ImageJ, PHENIX, Topaz]

### Genome expansion by a CRISPR trimmer-integrase. (Nature 2023)

- DOI: 10.1038/s41586-023-06178-2 | PMCID: PMC10284694 | PMID: 37316664
- Evidence: Model building and refinement The initial models of the Cas1 and Cas2/DEDDh were obtained using the AlphaFold 2 program 47 .
- Full pipeline: structure determination [AlphaFold, Coot v0.9.4.1, PHENIX v1.19.2] -> machine learning [Topaz] -> stage not stated [ChimeraX, HMMER]

### Outer membrane utilisomes mediate glycan uptake in gut Bacteroidetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06146-w | PMCID: PMC7618045 | PMID: 37286596
- Evidence: An AlphaFold2 23 prediction of the dextran SusC was generated and used as an initial model.
- Full pipeline: registration [CTFFIND] -> differential/statistical testing [limma] -> stage not stated [AlphaFold, CCP4, ChimeraX, PHENIX, R v4.1.1, RELION]

### Axonemal structures reveal mechanoregulatory and disease mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-06140-2 | PMCID: PMC10266980 | PMID: 37258679
- Evidence: Structure predictions of other axonemal proteins were obtained using AlphaFold2 (ref.
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> structure determination [Coot] -> stage not stated [AlphaFold, ChimeraX, PHENIX, R v4.0, RELION]

### Heteromeric clusters of ubiquitinated ER-shaping proteins drive ER-phagy. (Nature 2023)

- DOI: 10.1038/s41586-023-06090-9 | PMCID: PMC10247384 | PMID: 37225994
- Evidence: Modelling and simulations of ARL6IP1 The atomic model of human ARL6IP1 was built using the AI-based AlphaFold (v.2) program 40 .
- Full pipeline: simulation/modelling [AlphaFold] -> stage not stated [ImageJ]

### GWAS and meta-analysis identifies 49 genetic variants underlying critical COVID-19. (Nature 2023)

- DOI: 10.1038/s41586-023-06034-3 | PMCID: PMC10208981 | PMID: 37198478
- Evidence: The colour shows linkage disequilibrium (LD) with the missense variant rs117169628. b , Three cartoon views of an AlphaFold 22 model of putative solute carrier family 22 member 31 (SLC22A31; UniProtKB: A6NKX4 ).
- Full pipeline: alignment/mapping [HISAT2, SAMtools] -> variant calling [VCFtools v0.1.12b] -> quantification [DESeq2, HTSeq] -> normalisation [DESeq2, HTSeq] -> differential/statistical testing [SAMtools] -> stage not stated [AlphaFold, COLOC, GCTA v1.9.3, METAL, R]

### Structural basis of NINJ1-mediated plasma membrane rupture in cell death. (Nature 2023)

- DOI: 10.1038/s41586-023-05991-z | PMCID: PMC10307626 | PMID: 37198476
- Evidence: The initial model building was aided by standard poly-alanine helices and in a later step by an AlphaFold2 19 structure prediction of hNINJ1.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, ChimeraX, Python]

### In situ architecture of the ER-mitochondria encounter structure. (Nature 2023)

- DOI: 10.1038/s41586-023-06050-3 | PMCID: PMC7614606 | PMID: 37165187
- Evidence: We predicted the structures of heterodimers (Mmm1-Mdm12 and Mdm12-Mdm34) using FoldDock (FD) 26 , an AlphaFold (AF)-based tool 27 , and assembled a heterotrimeric complex based on the sequential order of the components derived from our STA map and previous findings 16 , 20 , 21 ( Fig.
- Full pipeline: alignment/mapping [IMOD, UCSF Chimera] -> quantification [ImageJ] -> simulation/modelling [NAMD] -> structure determination [IMOD] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, R, VMD]

### Structural atlas of a human gut crassvirus. (Nature 2023)

- DOI: 10.1038/s41586-023-06019-2 | PMCID: PMC10172136 | PMID: 37138077
- Evidence: AlphaFold structure predictions Structure predictions using AlphaFold2 37 were performed for ΦcrAss001 protein sequences: gp46, gp47, gp49, gp50, gp21 and gp29.
- Full pipeline: structure determination [Coot v0.9.8.1, PHENIX v1.19] -> stage not stated [AlphaFold, ChimeraX v1.5, RELION v3.1]

### Visualizing the disordered nuclear transport machinery in situ. (Nature 2023)

- DOI: 10.1038/s41586-023-05990-0 | PMCID: PMC10156602 | PMID: 37100914
- Evidence: The most advanced computational modelling tools, such as the AI-based AlphaFold, can very precisely predict the structures of folded proteins.
- Full pipeline: simulation/modelling [GROMACS v2020.6, LAMMPS] -> visualisation [VMD] -> stage not stated [AlphaFold]

### De novo design of protein interactions with learned surface fingerprints. (Nature 2023)

- DOI: 10.1038/s41586-023-05993-x | PMCID: PMC10131520 | PMID: 37100904
- Evidence: DBR3_03 has an affinity of 80 nM with RBD. e , A cryo-EM structure (dark green) aligns to the AlphaFold prediction with an iRMSD of 1.4 Å.
- Full pipeline: alignment/mapping [AlphaFold] -> normalisation [scikit-learn] -> dimensionality reduction/clustering [scikit-learn] -> structure determination [Coot v0.9.5] -> machine learning [TensorFlow v1.12] -> visualisation [ChimeraX] -> stage not stated [PHENIX v1.20.1, UCSF Chimera]

### Mirusviruses link herpesviruses to giant viruses. (Nature 2023)

- DOI: 10.1038/s41586-023-05962-4 | PMCID: PMC10132985 | PMID: 37076623
- Evidence: The candidate MCP was then modelled using AlphaFold2 (refs.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [BLAST, BWA v0.7.15, MAFFT, SAMtools] -> dimensionality reduction/clustering [OrthoFinder] -> differential/statistical testing [IQ-TREE, SAMtools] -> structure determination [BLAST, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, RoseTTAFold]

### Cryo-EM structure of the transposon-associated TnpB enzyme. (Nature 2023)

- DOI: 10.1038/s41586-023-05933-9 | PMCID: PMC10097598 | PMID: 37020030
- Evidence: Model building and validation The model was built using the predicted model of the ISDra2 TnpB protein created by AlphaFold2 as the reference 31 , followed by manual model building with COOT 32 .
- Full pipeline: structure determination [ChimeraX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Clustal Omega, PHENIX]

### mRNA recognition and packaging by the human transcription-export complex. (Nature 2023)

- DOI: 10.1038/s41586-023-05904-0 | PMCID: PMC7614608 | PMID: 37020021
- Evidence: We then replaced the ALYREF C-UBM helix with that from an AlphaFold model, obtained from a human UAP56–ALYREF C-UBM prediction, which better matched the density.
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ] -> normalisation [ImageJ] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX, ImageJ, PyMOL, R, UCSF Chimera] -> stage not stated [AlphaFold, RELION v3.1]

### Programmable protein delivery with a bacterial contractile injection system. (Nature 2023)

- DOI: 10.1038/s41586-023-05870-7 | PMCID: PMC10097599 | PMID: 36991127
- Evidence: In silico protein structure prediction To predict the structure of novel PVC tail fibre designs, we leveraged ColabFold, a Google Colab-based implementation of AlphaFold2 35 – 37 .
- Full pipeline: quantification [ImageJ] -> visualisation [PyMOL v2.5.2] -> stage not stated [AlphaFold, ColabFold]

### Structural basis for GSDMB pore formation and its targeting by IpaH7.8. (Nature 2023)

- DOI: 10.1038/s41586-023-05832-z | PMCID: PMC10115629 | PMID: 36991122
- Evidence: For the IpaH7.8–GSDMB complex, AlphaFold2-predicted structures of IpaH7.8 and GSDMB were used as starting models 27 .
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, Coot, MotionCor2, RELION, UCSF Chimera]

### Structural basis of mitochondrial membrane bending by the I-II-III&lt;sub&gt;2&lt;/sub&gt;-IV&lt;sub&gt;2&lt;/sub&gt; supercomplex. (Nature 2023)

- DOI: 10.1038/s41586-023-05817-y | PMCID: PMC10060162 | PMID: 36949187
- Evidence: Using AlphaFold2 (ref.
- Full pipeline: registration [IMOD, RELION] -> simulation/modelling [ChimeraX, GROMACS] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Structural basis for bacterial energy extraction from atmospheric hydrogen. (Nature 2023)

- DOI: 10.1038/s41586-023-05781-7 | PMCID: PMC10017518 | PMID: 36890228
- Evidence: Huc model building and visualization A model of the HucS and HucL subunit dimers was generated using AlphaFold and docked into one-half of the high-resolution Huc Dimer maps using ChimeraX 1.3 (refs.
- Full pipeline: simulation/modelling [GROMACS v2021.3] -> structure determination [ChimeraX v1.3, PHENIX] -> visualisation [AlphaFold, VMD] -> stage not stated [CTFFIND v4.1.8, Coot, RELION v3.1.2]

### Coordination of bacterial cell wall and outer membrane biosynthesis. (Nature 2023)

- DOI: 10.1038/s41586-023-05750-0 | PMCID: PMC9995270 | PMID: 36859542
- Evidence: MurA–LpxC complex structure prediction The structure of the LpxC–MurA complex was predicted using the default parameters of AlphaFold 19 .
- Full pipeline: alignment/mapping [Python v3.8.8] -> quantification [ImageJ] -> visualisation [ChimeraX v1.1.1, Python v3.8.8] -> stage not stated [AlphaFold, scikit-learn v1.0.2]

### Ubiquitin-like conjugation by bacterial cGAS enhances anti-phage defence. (Nature 2023)

- DOI: 10.1038/s41586-023-05862-7 | PMCID: PMC10097602 | PMID: 36848932
- Evidence: The data were integrated and scaled to 2.0 Å using HKL-3000 and phased by molecular replacement with PHASER using a predicted structure of Vs.4 that was created using AlphaFold 26 – 29 (Extended Data Fig.
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [AlphaFold] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### De novo design of luciferases using deep learning. (Nature 2023)

- DOI: 10.1038/s41586-023-05696-3 | PMCID: PMC9946828 | PMID: 36813896
- Evidence: Although we were not able to determine the crystal structure of LuxSit, the structure predicted by AlphaFold2 (ref.
- Full pipeline: stage not stated [AlphaFold]

### Aberrant phase separation and nucleolar dysfunction in rare genetic diseases. (Nature 2023)

- DOI: 10.1038/s41586-022-05682-1 | PMCID: PMC9931588 | PMID: 36755093
- Evidence: AlphaFold predictions for protein structures AlphaFold predictions were computed using an in-house implementation of AlphaFold 45 using v.2.0.0 from 16 July 2021.
- Full pipeline: visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BEDTools v2.30.0, ColabFold, R, VEP, ggplot2]

### The structural basis for HIV-1 Vif antagonism of human APOBEC3G. (Nature 2023)

- DOI: 10.1038/s41586-023-05779-1 | PMCID: PMC10033410 | PMID: 36754086
- Evidence: The top body of the consensus reconstruction map shows visible helical features in which we were able to fit the crystal structure of HIV-1 VCBC (PDB: 4N9F ) and the AlphaFold 2-predicted human A3G monomeric structure (AF2: Q9HC16 ) 31 , 65 (Extended Data Fig.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> registration [MotionCor2] -> structure determination [AlphaFold, UCSF Chimera] -> stage not stated [ChimeraX, Coot, PHENIX, PyMOL, RELION]

### Visualization of translation and protein biogenesis at the ER membrane. (Nature 2023)

- DOI: 10.1038/s41586-022-05638-5 | PMCID: PMC9892003 | PMID: 36697828
- Evidence: The initial model for TRAP was built using AlphaFold Colab 37 and Coot 61 .
- Full pipeline: alignment/mapping [IMOD v4.10.25, NumPy v1.20.3, Python v3.8.11, RELION v3.1.1, SciPy v1.7.1] -> structure determination [ChimeraX v1.3.0, UCSF Chimera v1.14.0] -> visualisation [ChimeraX v1.3.0] -> stage not stated [AlphaFold]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Evidence: 2 chordin was lost multiple times in annelids. a , Domain organisation of Chordin (CHRD) and Chordin-like (CHRDL1/2) proteins, as inferred from human orthologs. b , Public AlphaFold protein structure prediction for human Chordin (UniProt: Q9H2X0 ) and Chordin-like 1 (UniProt: Q9BU40 ) revealed a previously unknown and uncharacterised domain in CHRDL1 and CHRDL2 (also depicted in a ). c , d , Ortho...
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### An atlas of substrate specificities for the human serine/threonine kinome. (Nature 2023)

- DOI: 10.1038/s41586-022-05575-3 | PMCID: PMC9876800 | PMID: 36631611
- Evidence: 3 were as follows: ATM (PDB: 7SIC ) 92 and p53 (chimera of AlphaFold AF- P04637 -F1-model_v2_1 (1–95) 61 and 2ATA(96–292) 92 ) (Fig.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, PyMOL, Python v3.7.6, SciPy]

### RNA targeting unleashes indiscriminate nuclease activity of CRISPR-Cas12a2. (Nature 2023)

- DOI: 10.1038/s41586-022-05560-w | PMCID: PMC9849127 | PMID: 36599980
- Evidence: Attempts at using AlphaFold2 (AF2) 48 to generate fragments to fit in the map were unsuccessful as adjacent residues within the WED and RuvC domains were separated by protein sequence and the REC1 and REC2 domain boundaries were not obvious from the sequence alone.
- Full pipeline: structure determination [PHENIX v1.19] -> stage not stated [AlphaFold, ChimeraX v1.0, Coot, PyMOL v2.5]

### Structural basis of broad-spectrum β-lactam resistance in Staphylococcus aureus. (Nature 2023)

- DOI: 10.1038/s41586-022-05583-3 | PMCID: PMC9834060 | PMID: 36599987
- Evidence: AlphaFold2 (not available at the time of initial model building) reproducibly and confidently predicted the C-terminal region of this loop as bound to the sensor-domain β-lactam binding groove, which was supported by low-resolution features in the reconstruction (Extended Data Fig.
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [RELION]

### Principles of mitoribosomal small subunit assembly in eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-022-05621-0 | PMCID: PMC9892005 | PMID: 36482135
- Evidence: To build assembly factors, a combination of homology models generated in the AlphaFold database (NOA1, METTL17, RBFA and ERAL1) and existing X-ray structures (MCAT (PDB: 2C2N) and TFB1M (PDB: 6AAX)) were used as starting models before manual adjustment using COOT 62 .
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [ChimeraX, PyMOL] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, RELION v3.1.1]

### Undecaprenyl phosphate translocases confer conditional microbial fitness. (Nature 2023)

- DOI: 10.1038/s41586-022-05569-1 | PMCID: PMC9876793 | PMID: 36450355
- Evidence: Structural modelling Structural prediction of DUF368 and DedA family proteins in this study was performed with AlphaFold2 on the CoLabFold publicly accessible interface 45 .
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1] -> differential/statistical testing [DESeq2 v1.30.1, R v4.0.3] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, ImageJ v1.53, InterProScan, featureCounts]

### Structures of the holo CRISPR RNA-guided transposon integration complex. (Nature 2023)

- DOI: 10.1038/s41586-022-05573-5 | PMCID: PMC9876797 | PMID: 36442503
- Evidence: Additional models were created using AlphaFold2 43 for the following components: Cas12k, TniQ and S15, and rigid-body docked into the density.
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [AlphaFold, RELION, UCSF Chimera v1.14]

### MCM double hexamer loading visualized with human proteins. (Nature 2024)

- DOI: 10.1038/s41586-024-08263-6 | PMCID: PMC11634765 | PMID: 39604733
- Evidence: Extended Data Table 1 Cryo-EM data collection, refinement and validation statistics – part 1 hDH model building AlphaFold-Multimer 53 was used to generate models of the ATPase tier (including the WH domains) of the hexameric human MCM2–7 assembly as well as the amino-terminal tier.
- Full pipeline: differential/statistical testing [AlphaFold] -> structure determination [AlphaFold, Coot v0.9.8.1, PHENIX v1.21] -> stage not stated [CTFFIND v1.06, ChimeraX v1.6.1, RELION, Topaz v0.2.5]

### Stereochemistry in the disorder-order continuum of protein interactions. (Nature 2024)

- DOI: 10.1038/s41586-024-08271-6 | PMCID: PMC11655355 | PMID: 39604735
- Evidence: AlphaFold structure modelling Protein interaction models of RCD1-RST 499–572 in complex with ANAC046 319–338 or ANAC013 254–274 were generated using AlphaFold3 30 and analysed in PyMOL (The PyMOL Molecular Graphics System, version 3.0 Schrödinger, LLC.).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold, PyMOL]

### Nucleosome flipping drives kinetic proofreading and processivity by SWR1. (Nature 2024)

- DOI: 10.1038/s41586-024-08152-y | PMCID: PMC11618073 | PMID: 39506114
- Evidence: Model building For the Swc2 subunit, an initial template was generated using AlphaFold 25 .
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold, CTFFIND, Coot]

### Anti-viral defence by an mRNA ADP-ribosyltransferase that blocks translation. (Nature 2024)

- DOI: 10.1038/s41586-024-08102-8 | PMCID: PMC11618068 | PMID: 39443800
- Evidence: Predictions of the structures of individual components and CmdTAC as a complex were done using AlphaFold2 52 with the multimer module and default parameters on the reduced database with 1 prediction generated per model.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, NumPy, SAMtools] -> quantification [ImageJ] -> stage not stated [AlphaFold, ChimeraX, HMMER]

### A bacterial immunity protein directly senses two disparate phage proteins. (Nature 2024)

- DOI: 10.1038/s41586-024-08039-y | PMCID: PMC11578894 | PMID: 39415022
- Evidence: Phaser 37 was used to solve the structure by molecular replacement using an AlphaFold 38 model.
- Full pipeline: alignment/mapping [BLAST, MUSCLE] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ColabFold]

### Structural basis of mRNA decay by the human exosome-ribosome supercomplex. (Nature 2024)

- DOI: 10.1038/s41586-024-08015-6 | PMCID: PMC11540850 | PMID: 39385025
- Evidence: Density interpretation, model building and refinement The 80S-bound EXO10-SKI or map1 reconstruction was interpreted by rigid-body fitting pre-existing models of SKI2 (PDB 7QE0 ) 17 , the nuclear human exosome (PDB 6D6Q ) 27 and AlphaFold multimer predictions of either SKI7 EXO or DIS3L with different human exosome subcomplexes 48 .
- Full pipeline: quantification [ImageJ] -> structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ImageJ] -> stage not stated [MotionCor2, RELION v3.1, UCSF Chimera]

### LYCHOS is a human hybrid of a plant-like PIN transporter and a GPCR. (Nature 2024)

- DOI: 10.1038/s41586-024-08012-9 | PMCID: PMC11525196 | PMID: 39358511
- Evidence: Model building In the first instance, a computed model of LYCHOS with C 2 symmetry was generated by AlphaFold 16 using an A6000 GPU with 48 Gb of VRAM.
- Full pipeline: dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX v1.20.1] -> visualisation [Matplotlib] -> stage not stated [AlphaFold, CTFFIND v4.1.8, ChimeraX, ImageJ v2.14.0, MotionCor2 v1.1.0]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: Protein alignments and structure prediction The mouse SPOCD1 AlphaFold2 protein structure prediction model 22 , 23 was downloaded from the AlphaFold Protein Structure Database ( https://www.alphafold.ebi.ac.uk/ ).
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### The ultra-high affinity transport proteins of ubiquitous marine bacteria. (Nature 2024)

- DOI: 10.1038/s41586-024-07924-w | PMCID: PMC11485210 | PMID: 39261732
- Evidence: For SAR11_1210, the structure of an opine-binding protein from Agrobacterium fabrum (PDB ID 5OT8 ) was used as a search model; in the remaining cases, an AlphaFold2 model was used 77 .
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> structure determination [PHENIX, REFMAC] -> stage not stated [AlphaFold]

### Structure of the human TIP60-C histone exchange and acetyltransferase complex. (Nature 2024)

- DOI: 10.1038/s41586-024-08011-w | PMCID: PMC11578891 | PMID: 39260417
- Evidence: The EP400 ATPase C-lobe was modelled in AlphaFold 47 , docked into the map by ADP_EM 48 and manually adjusted according to density.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [cryoDRGN] -> structure determination [PHENIX, cryoDRGN] -> stage not stated [AlphaFold, ChimeraX, Coot, RELION]

### Mapping glycoprotein structure reveals Flaviviridae evolutionary history. (Nature 2024)

- DOI: 10.1038/s41586-024-07899-8 | PMCID: PMC11410658 | PMID: 39232167
- Version used: **2.3**
- Evidence: Structures were predicted for each sequence using the ColabFold (v1.5.1) implementation of AlphaFold2 (v2.3) 19 , with default settings but only generating a single model per target, performed using Google Colab cloud computing.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Clustal Omega v1.2.4, MAFFT, MUSCLE v5.1] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX] -> stage not stated [AlphaFold v2.3, BLAST v2.0.9, ColabFold v1.5.1, IQ-TREE, InterProScan, Python, phytools v1.5]

### Global marine microbial diversity and its potential in bioprospecting. (Nature 2024)

- DOI: 10.1038/s41586-024-07891-2 | PMCID: PMC11390488 | PMID: 39232160
- Version used: **2.3.0**
- Evidence: We predicted their 3D structures using AlphaFold2 (v2.3.0) 128 and checked the conserved key residuals of the active center, leading to a total of 26 Cas9 proteins showing the conserved structure of the key residuals (Supplementary Table 2 ).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.407, MUSCLE v3.8.31] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [AlphaFold v2.3.0, InterProScan v5.0, Prokka v1.14.6, R, ggplot2 v3.5.1]

### Birth of protein folds and functions in the virome. (Nature 2024)

- DOI: 10.1038/s41586-024-07809-y | PMCID: PMC11410667 | PMID: 39187718
- Evidence: Structural alignments against the AlphaFold databases In Fig.
- Full pipeline: alignment/mapping [AlphaFold, BLAST, Clustal Omega v1.2.4] -> dimensionality reduction/clustering [BLAST, InterProScan] -> differential/statistical testing [R v4.0.3] -> structure determination [IQ-TREE v2.3.3] -> stage not stated [ColabFold, Nextflow]

### Growth of complete ammonia oxidizers on guanidine. (Nature 2024)

- DOI: 10.1038/s41586-024-07832-z | PMCID: PMC11410670 | PMID: 39143220
- Evidence: The phase problem was solved with Phaser-MR 78 , using its AlphaFold 79 prediction as a search model.
- Full pipeline: alignment/mapping [ImageJ v1.54f] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ImageJ v1.54f, PyMOL, phytools] -> stage not stated [AlphaFold, BEDTools, HMMER]

### Molecular architecture of coronavirus double-membrane vesicle pore complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07817-y | PMCID: PMC11374677 | PMID: 39143215
- Evidence: The prong tip is in low resolution (12–15 Å resolution) and the Mac2–3 and NAB domain were predicted as a complex using AlphaFold2 (Supplementary Fig.
- Full pipeline: alignment/mapping [Python] -> structure determination [ChimeraX, Coot, RELION] -> visualisation [Topaz] -> stage not stated [AlphaFold, IMOD]

### Structure of the human dopamine transporter and mechanisms of inhibition. (Nature 2024)

- DOI: 10.1038/s41586-024-07739-9 | PMCID: PMC11324517 | PMID: 39112705
- Evidence: Model building and refinement The final cryo-EM map of Δ-hDAT was interpreted by fitting an AlphaFold-derived model 54 ( AF-Q01959-F1 ) of hDAT in ChimeraX 55 using rigid body fitting.
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX v1.20.1] -> stage not stated [PyMOL, VMD]

### A virally encoded tRNA neutralizes the PARIS antiviral defence system. (Nature 2024)

- DOI: 10.1038/s41586-024-07874-3 | PMCID: PMC11464382 | PMID: 39111359
- Evidence: Using this low-resolution initial volume, AlphaFold2-predicted structures of AriA and AriB were fit into the map and used to generate a 20 Å low-pass-filtered map using the Molmap command in ChimeraX v.1.7 (ref.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HMMER v3.3.2, MUSCLE v5.1] -> structure determination [PHENIX v1.20.1] -> stage not stated [AlphaFold, ChimeraX v1.7, SPAdes]

### PTER is a N-acetyltaurine hydrolase that regulates feeding and obesity. (Nature 2024)

- DOI: 10.1038/s41586-024-07801-6 | PMCID: PMC11374699 | PMID: 39112712
- Evidence: Molecular docking The AlphaFold-predicted structure of mouse PTER ( AF-Q60866-F1 ) was used to search for proteins with structural or sequence homology using FoldSeek and BLAST, respectively.
- Full pipeline: stage not stated [AlphaFold, AutoDock Vina, PyMOL v3.7]

### Cryo-EM architecture of a near-native stretch-sensitive membrane microdomain. (Nature 2024)

- DOI: 10.1038/s41586-024-07720-6 | PMCID: PMC11324527 | PMID: 39048819
- Evidence: Model building Structure predictions for Pil1 and Lsp1 from the AlphaFold database ( https://alphafold.ebi.ac.uk/ ) were used as starting models, with the C-terminal region removed, starting from residue 275, for which no density was observed.
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.8.9.2, PHENIX v1.20] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, Cellpose v2.0, RELION v2.1.0, VMD v1.9]

### An intermediate Rb-E2F activity state safeguards proliferation commitment. (Nature 2024)

- DOI: 10.1038/s41586-024-07554-2 | PMCID: PMC11236703 | PMID: 38926571
- Evidence: Protein structural modelling Structures were modelled using ColabFold 56 , a simplified AlphaFold2 algorithm 30 , 57 , without templates ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/beta/AlphaFAlp2_advanced.ipynb ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [Clustal Omega] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold]

### Computational design of soluble and functional membrane protein analogues. (Nature 2024)

- DOI: 10.1038/s41586-024-07601-y | PMCID: PMC11236705 | PMID: 38898281
- Evidence: Recently, structure prediction pipelines, such as AlphaFold2 (AF2) 4 , have achieved unprecedented accuracy in predicting protein structure given the amino acid sequence.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, Python v3.9] -> stage not stated [AlphaFold]

### Oligomerization-mediated autoinhibition and cofactor binding of a plant NLR. (Nature 2024)

- DOI: 10.1038/s41586-024-07668-7 | PMCID: PMC11338831 | PMID: 38866053
- Evidence: Model building and refinement The model of Sl NRC2 monomer predicted by AlphaFold2 was docked into the reconstruction map of Sl NRC2 dimer (Protein Data Bank (PDB) code 8XUO ) and then manually adjusted in COOT 55 – 57 followed by PHENIX 58 refinement in real space with secondary structure and geometry restraints.
- Full pipeline: structure determination [AlphaFold, PHENIX, RELION v3.08] -> stage not stated [MotionCor2]

### MYCT1 controls environmental sensing in human haematopoietic stem cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07478-x | PMCID: PMC11168926 | PMID: 38839950
- Evidence: The colocalization with endosomal markers, together with the topology prediction and the 3D structure predicted with AlphaFold 49 , 50 , suggest that in HSCs and HSC-like cells, MYCT1 acts primarily in endosomes and localizes at the membrane of endosomes through the two TM domains, with a short intraendosomal loop (Fig.
- Full pipeline: quantification [Bioconductor] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> stage not stated [AlphaFold, GSEA, R, Seurat v3.1.2]

### Structure and topography of the synaptic V-ATPase-synaptophysin complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07610-x | PMCID: PMC11269182 | PMID: 38838737
- Evidence: Model building and refinement Initial models of the V-ATPase and synaptophysin complexes for our wild-type (mouse) ISV SPA data were generated based on the deposited rat (PDB IDs: 6VQ6 , 6VQ7 , 6VQ8 and 6VQH ) and human (PDB IDs: 6WM2 , 6WM3 , 6WM4 and 6WLW ) V-ATPase structures and a mouse synaptophysin model predicted by AlphaFold2 29 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [AlphaFold, PHENIX v1.21] -> machine learning [RELION, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Coot, Python, SciPy, UCSF Chimera]

### Membraneless channels sieve cations in ammonia-oxidizing marine archaea. (Nature 2024)

- DOI: 10.1038/s41586-024-07462-5 | PMCID: PMC11153153 | PMID: 38811725
- Version used: **2.2.0**
- Evidence: The domain organization of several obtained matches and many experimentally characterized SLPs (Supplementary Table 1 ) were analysed using HHpred searches with the default settings over the PDB70 and ECOD70 databases, which are versions of the PDB and ECOD databases filtered for a maximum pairwise identity of 70%, and using structural models built using AlphaFold (v.2.2.0) 72 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [NAMD v2.14, VMD v1.94] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold v2.2.0, MotionCor2]

### Structural basis for pegRNA-guided reverse transcription by a prime editor. (Nature 2024)

- DOI: 10.1038/s41586-024-07497-8 | PMCID: PMC11222144 | PMID: 38811740
- Evidence: The initiation complex (light blue) is superimposed onto the pre-initiation complex. h , The AlphaFold-prediction models of G1054–RTΔRH–E1055 (left) and T1068–RTΔRH–G1069 (right) PE2 variants 38 .
- Full pipeline: registration [MotionCor2] -> stage not stated [AlphaFold, ChimeraX, PHENIX, RELION v3.1.1, Topaz]

### Natural proteome diversity links aneuploidy tolerance to protein turnover. (Nature 2024)

- DOI: 10.1038/s41586-024-07442-9 | PMCID: PMC11153158 | PMID: 38778096
- Evidence: ... protein–protein interactions (PPIs): STRING database (accessed November 2022) 74 ; prediction of protein disorder and linear interacting peptides by AlphaFold, MobiDB and anchor: MobiDB (accessed October 2022) 75 ; GC content and percentile mean gRSCU: calculated on the Saccharomyces cerevisiae S288C sequence (NCBI: GCF_000146045.2_R64) using the gc1, gc2, gc3 and gRSCU functions in BioKIT v.0.1....
- Full pipeline: read trimming [edgeR] -> quantification [R, edgeR] -> normalisation [edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [AlphaFold, GSEA, STRING db, data.table]

### Structural insights into the cross-exon to cross-intron spliceosome switch. (Nature 2024)

- DOI: 10.1038/s41586-024-07458-1 | PMCID: PMC11208138 | PMID: 38778104
- Evidence: Model building and refinement Model building was carried out by docking cryo-EM, crystal and AlphaFold2 structures into EM density and adjusting in COOT 35 .
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, RELION v3.1]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Evidence: Model building and geometry refinement The first atomic models of FLVCR1 and FLVCR2 were built into the respective electron microscopy density maps of the as-isolated state in Coot (v0.8) or ISOLDE within ChimeraX (v.1.5 and 1.6) 39 – 41 , using the AlphaFold predicted structures as initial templates 42 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### The intrinsic substrate specificity of the human tyrosine kinome. (Nature 2024)

- DOI: 10.1038/s41586-024-07407-y | PMCID: PMC11136658 | PMID: 38720073
- Evidence: 72 ) and AlphaFold AF- P06213 -F1 ( https://alphafold.ebi.ac.uk/entry/P06213 ) (ref.
- Full pipeline: visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python v3.7.6, SciPy]

### Accurate structure prediction of biomolecular interactions with AlphaFold 3. (Nature 2024)

- DOI: 10.1038/s41586-024-07487-w | PMCID: PMC11168924 | PMID: 38718835
- Evidence: To compare the quality of prediction of protein–protein interfaces and protein monomers against that of AlphaFold-Multimer (v.2.3) 8 , and to compare the dependence of single-protein-chain prediction quality on MSA depth, we restrict the low-homology recent PDB set to complexes with fewer than 20 protein chains and fewer than 2,560 tokens.
- Full pipeline: visualisation [NumPy v1.26.3, SciPy v1.9.3, seaborn v0.12.2] -> stage not stated [AlphaFold, Matplotlib v3.6.1, RDKit, RoseTTAFold, statsmodels v0.12.2]

### Mechanism of single-stranded DNA annealing by RAD52-RPA complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07347-7 | PMCID: PMC11096129 | PMID: 38658755
- Evidence: RPA1, RPA2 and RPA3 AlphaFold2 models were used for Dock and rebuild in Phenix 73 , 74 and the ssDNA model was aligned and extracted from the fungal RPA structure (PDB: 4GOP ) 39 .
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega] -> quantification [ImageJ] -> stage not stated [ChimeraX, EMAN2, PHENIX, RELION v3.1]

### DNA glycosylases provide antiviral defence in prokaryotes. (Nature 2024)

- DOI: 10.1038/s41586-024-07329-9 | PMCID: PMC11078745 | PMID: 38632404
- Evidence: Brig1 structural predictions using AlphaFold2 The structure of the intact (261 amino acid) Brig1 protein was predicted using the colab implementation of AlphaFold2 17 , 18 ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ) using default settings (except that the amber option was turned on to improve side chain rotamers).
- Full pipeline: alignment/mapping [IQ-TREE v1.6.12, MUSCLE, Python] -> normalisation [Python] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BLAST, ColabFold]

### Streptomyces umbrella toxin particles block hyphal growth of competing species. (Nature 2024)

- DOI: 10.1038/s41586-024-07298-z | PMCID: PMC11062931 | PMID: 38632398
- Evidence: Structural modelling of Umb proteins and PPIs Structural predictions for UmbC1–UmbC3, UmbA1–UmbA5 and UmbB1–UmbB3 were made using AlphaFold2 (ref.
- Full pipeline: alignment/mapping [ColabFold] -> structure determination [Coot, Topaz] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, Python, RELION, RoseTTAFold, napari]

### Structural basis of Integrator-dependent RNA polymerase II termination. (Nature 2024)

- DOI: 10.1038/s41586-024-07269-4 | PMCID: PMC11062913 | PMID: 38570683
- Evidence: For the tail module, we rigid-body-docked AlphaFold2 (ref.
- Full pipeline: structure determination [ChimeraX, ColabFold, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, Coot, RELION v3.1]

### Molecular insights into capsular polysaccharide secretion. (Nature 2024)

- DOI: 10.1038/s41586-024-07248-9 | PMCID: PMC11041684 | PMID: 38570679
- Evidence: To improve the KpsT density in classes 0 and 1, a separate 3D classification focused on KpsT was performed, resulting in improved KpsT density for the glycolipid 1 and 2 states (respective map A for both classes), enabling rigid-body docking of an AlphaFold2-predicted KpsT model.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ImageJ]

### Blueprinting extendable nanomaterials with standardized protein blocks. (Nature 2024)

- DOI: 10.1038/s41586-024-07188-4 | PMCID: PMC10972742 | PMID: 38480887
- Evidence: Designs were filtered with AlphaFold 2 available at https://github.com/google-deepmind/alphafold ( Supplementary Methods ).
- Full pipeline: stage not stated [AlphaFold]

### The CRL5-SPSB3 ubiquitin ligase targets nuclear cGAS for degradation. (Nature 2024)

- DOI: 10.1038/s41586-024-07112-w | PMCID: PMC10972748 | PMID: 38418882
- Evidence: The SPSB3–ELOBC model from AlphaFold2 was docked into the cryo-EM map in ChimeraX 37 and tuned by ISOLDE 43 and Coot 44 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, CellProfiler, ChimeraX]

### Automated model building and protein identification in cryo-EM maps. (Nature 2024)

- DOI: 10.1038/s41586-024-07215-4 | PMCID: PMC11006616 | PMID: 38408488
- Evidence: We then extended the models of RSP25 and RSP26 using AlphaFold2 predictions for the EF-hand motifs, which have relatively poor cryo-EM density, demonstrating how ModelAngelo and AI-based structure prediction methods can be used together to build more complete atomic models.
- Full pipeline: stage not stated [AlphaFold, HMMER, PHENIX]

### The UFM1 E3 ligase recognizes and releases 60S ribosomes from ER translocons. (Nature 2024)

- DOI: 10.1038/s41586-024-07093-w | PMCID: PMC10937380 | PMID: 38383789
- Evidence: For the ligase complex, AlphaFold2 models of the individual proteins were separated into smaller segments and then rigid-body fitted into the density map, followed by manual rebuilding in Coot.
- Full pipeline: registration [RELION v3.1] -> structure determination [AlphaFold, ChimeraX v1.2.5, REFMAC] -> machine learning [cryoDRGN v3.2.0] -> stage not stated [CCP4, Coot v0.9.8.1, PHENIX v1.2.1]

### A new family of bacterial ribosome hibernation factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07041-8 | PMCID: PMC10901736 | PMID: 38355796
- Evidence: Model building, refinement and deposition The atomic models of P. urativorans ribosomes and the ribosome-binding proteins were produced using Coot v0.8.9.2 56 and AlphaFold 57 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, Coot v0.8.9.2, UCSF Chimera v1.14] -> stage not stated [ChimeraX v1.4, HMMER, PHENIX v1.20.1, RELION v3.1]

### Structural basis of ribosomal 30S subunit degradation by RNase R. (Nature 2024)

- DOI: 10.1038/s41586-024-07027-6 | PMCID: PMC10901742 | PMID: 38326618
- Evidence: This model was updated in Coot using protein restraints generated by ProSmart from AlphaFold models for all 30S ribosomal proteins 67 – 72 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, MotionCor2] -> visualisation [BEDTools, ImageJ] -> stage not stated [AlphaFold, ChimeraX, Coot, RELION v3.1.3]

### Stress response silencing by an E3 ligase mutated in neurodegeneration. (Nature 2024)

- DOI: 10.1038/s41586-023-06985-7 | PMCID: PMC10881396 | PMID: 38297121
- Evidence: AlphaFold2 modelling indicated that this domain contains two conserved α-helices (Fig.
- Full pipeline: alignment/mapping [kallisto v0.48.0] -> quantification [kallisto v0.48.0] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, Cytoscape, Galaxy v2.11.40.7]

### The HIV capsid mimics karyopherin engagement of FG-nucleoporins. (Nature 2024)

- DOI: 10.1038/s41586-023-06969-7 | PMCID: PMC10881392 | PMID: 38267582
- Evidence: Owing to the length of Nup358, AlphaFold2 predictions were performed as three FG-containing sections (982–2004, 2005–3043 and 3058–3224), with their per-residue RSA-based disorder propensity calculated locally.
- Full pipeline: dimensionality reduction/clustering [IMOD] -> structure determination [IMOD] -> stage not stated [AlphaFold, ImageJ]

### The CRISPR effector Cam1 mediates membrane depolarization for phage defence. (Nature 2024)

- DOI: 10.1038/s41586-023-06902-y | PMCID: PMC10808066 | PMID: 38200316
- Evidence: The structures of apo, cA 4 - and cA 6 - bound Cam1(42–206) were solved by molecular replacement by using the structure predicted by AlphaFold 49 as a search model.
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold]

### Cryo-EM structures of PP2A:B55-FAM122A and PP2A:B55-ARPP19. (Nature 2024)

- DOI: 10.1038/s41586-023-06870-3 | PMCID: PMC10765524 | PMID: 38123684
- Evidence: For PP2A:B55–FAM122A, the relevant segments of the model were built into the B55 and PP2Ac body maps, using the previously determined crystal PP2A:B55 holoenzyme crystal structure (PDB ID 3DW8 ) and the available FAM122A AlphaFold model (UniProt Q96E09 ) as a starting point.
- Full pipeline: quantification [ImageJ v1.53t] -> structure determination [Coot, PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, RELION v4.0]

### The PfRCR complex bridges malaria parasite and erythrocyte during invasion. (Nature 2024)

- DOI: 10.1038/s41586-023-06856-1 | PMCID: PMC10794152 | PMID: 38123677
- Evidence: Model building and refinement To aid model building of the PfRCR–Cy.003 complex, the crystal structures of PfRH5 (PDB ID: 4U0Q , chain C) 3 , the PfCyRPA–Cy.003 Fab complex (PDB ID: 7PI2 , chains D–F) 5 and an AlphaFold2 (ref.
- Full pipeline: differential/statistical testing [RELION v3.1.3] -> structure determination [AlphaFold, PHENIX, RELION v3.1.3] -> visualisation [ChimeraX]

### De novo design of high-affinity binders of bioactive helical peptides. (Nature 2024)

- DOI: 10.1038/s41586-023-06953-1 | PMCID: PMC10849960 | PMID: 38109936
- Evidence: The selected scaffolds were then redesigned in the presence of the threaded target sequence with ProteinMPNN 24 and the complex was predicted with AlphaFold2 28 (AF2; with initial guess 6 ) and filtered on AF2 and Rosetta metrics.
- Full pipeline: machine learning [RoseTTAFold] -> stage not stated [AlphaFold]

### Structures, functions and adaptations of the human LINE-1 ORF2 protein. (Nature 2024)

- DOI: 10.1038/s41586-023-06947-z | PMCID: PMC10830420 | PMID: 38096902
- Evidence: ...creased activity after SEC relative to heparin chromatography alone against an oligo(A) template. c , Comparison of ORF2p core crystal structure with AlphaFold model used for molecular replacement shows remarkable similarity, with a final root-mean-square deviation (RMSD) of 0.946 Å from the search model.
- Full pipeline: alignment/mapping [ChimeraX] -> stage not stated [AlphaFold]

### Template and target-site recognition by human LINE-1 in retrotransposition. (Nature 2024)

- DOI: 10.1038/s41586-023-06933-5 | PMCID: PMC10830416 | PMID: 38096901
- Evidence: Model building and refinement Model building was initiated by rigid-body fitting the AlphaFold 36 model of human L1 ORF2p into the final 3.3 Å cryo-EM density map using UCSF ChimeraX 60 .
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [CTFFIND v4.1, ImageJ, MotionCor2, RELION v3.1.1]

### Structural basis of Gabija anti-phage defence and viral immune evasion. (Nature 2024)

- DOI: 10.1038/s41586-023-06855-2 | PMCID: PMC10781630 | PMID: 37992757
- Evidence: Experimental phase information was determined by molecular replacement using monomeric GajA and GajB AlphaFold2-predicted structures 31 , 32 in PHENIX 45 .
- Full pipeline: structure determination [Coot] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, PHENIX]

### Predicting multiple conformations via sequence clustering and AlphaFold2. (Nature 2024)

- DOI: 10.1038/s41586-023-06832-9 | PMCID: PMC10808063 | PMID: 37956700
- Evidence: AlphaFold2 (AF2) achieved breakthrough performance in the CASP14 competition 6 in part by advancing the state of the art for inferring patterns of interactions between related sequences in a multiple-sequence alignment (MSA), building on a long history of methods for inferring these patterns 7 – 10 , often called evolutionary couplings.
- Full pipeline: read trimming [RAxML v8.2.9] -> alignment/mapping [AlphaFold, MAFFT, RAxML v8.2.9] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST v2.6.0, ColabFold, IQ-TREE, PyMOL, SciPy]

### Florigen activation complex forms via multifaceted assembly in Arabidopsis. (Nature 2025)

- DOI: 10.1038/s41586-025-09704-6 | PMCID: PMC12711580 | PMID: 41225013
- Evidence: Structural modelling The structures of GRF7, full-length FD and truncated and mutant FD were predicted using AlphaFold 70 and AlphaFold2 71 .
- Full pipeline: alignment/mapping [MAFFT] -> quantification [Cellpose v2.2.3] -> stage not stated [AlphaFold, ColabFold, IQ-TREE v1.5.5]

### Viral NblA proteins negatively affect oceanic cyanobacterial photosynthesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09656-x | PMCID: PMC12695635 | PMID: 41224996
- Evidence: Representative structures of NblA dimers were predicted with ColabFold v.1.5.5 (based on AlphaFold2) 65 .
- Full pipeline: alignment/mapping [IQ-TREE v2.1.2, MAFFT v7.475] -> quantification [featureCounts] -> structure determination [IQ-TREE v2.1.2, MAFFT v7.475] -> stage not stated [AlphaFold, BLAST, ColabFold, HMMER v3.4, eggNOG, lme4 v1.1]

### Helicase-mediated mechanism of SSU processome maturation and disassembly. (Nature 2025)

- DOI: 10.1038/s41586-025-09688-3 | PMCID: PMC12711562 | PMID: 41162712
- Evidence: Model building and refinement A combination of AlphaFold structure predictions 39 , existing X-ray/EM structures, and de novo model building was used to build the 16 SSU processome assembly intermediates.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, ChimeraX, RELION]

### Nanobody-based recombinant antivenom for cobra, mamba and rinkhals bites. (Nature 2025)

- DOI: 10.1038/s41586-025-09661-0 | PMCID: PMC12629983 | PMID: 41162699
- Evidence: Structures of the V H Hs in complex with their respective toxins were determined by molecular replacement with Phaser-MR 78 using an AlphaFold 3 model for both the V H H and the target toxin as a search model.
- Full pipeline: structure determination [PHENIX] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, PyMOL]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Evidence: Bowhead whale specific variants are indicated. b , Structural models of human (left, pink) and bowhead whale (right, blue) CIRBP generated using SwissModel and AlphaFold.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### Designing allosteric modulators to change GPCR G protein subtype selectivity. (Nature 2025)

- DOI: 10.1038/s41586-025-09643-2 | PMCID: PMC12675282 | PMID: 41125894
- Evidence: A predicted AlphaFold structure of human NTSR2 was generated and aligned with an SBI-553-bound NTSR1 cryo-EM structure (PDB 8FN0).
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega] -> stage not stated [ChimeraX]

### Hijacking a bacterial ABC transporter for genetic code expansion. (Nature 2025)

- DOI: 10.1038/s41586-025-09576-w | PMCID: PMC12657241 | PMID: 41094137
- Evidence: Arrow indicates full-length sfGFP, asterisk indicates truncated sfGFP. b , AlphaFold2 predicted structure of the Opp transporter, consisting of the periplasmic binding protein OppA, two TMDs (OppB and OppC) and two NBDs (OppD and OppF). c , Extracted ion chromatograms of E. coli K12 lysates for determination of intracellular AisoK concentrations in wild-type K12 versus Δ oppA .
- Full pipeline: stage not stated [AlphaFold]

### Host cell Z-RNAs activate ZBP1 during virus infections. (Nature 2025)

- DOI: 10.1038/s41586-025-09705-5 | PMCID: PMC12711578 | PMID: 41082924
- Evidence: AlphaFold modelling of murine CPSF3 The structure of human JTE-607 bound CPSF3 (PDB: 6MQ8) was aligned with the mouse CPSF3 orthologue AlphaFold database model (AF- Q9QXK7 -F1-v4) in PyMOL.
- Full pipeline: quality control [DESeq2, FastQC, MultiQC] -> read trimming [Nextflow, STAR, fastp] -> alignment/mapping [AlphaFold, PyMOL, STAR] -> visualisation [MultiQC] -> stage not stated [Picard, RepeatMasker, SAMtools v1.2]

### Sex and smoking bias in the selection of somatic mutations in human bladder. (Nature 2025)

- DOI: 10.1038/s41586-025-09521-x | PMCID: PMC12611770 | PMID: 41062697
- Evidence: Structural representation and features Structural models for all proteins used to run Oncodrive3D were obtained from the AlphaFold database (AlphaFold 2 v.4) 78 , 79 .
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold, Nextflow, VEP]

### KCTD10 is a sensor for co-directional transcription-replication conflicts. (Nature 2025)

- DOI: 10.1038/s41586-025-09585-9 | PMCID: PMC12675284 | PMID: 41062692
- Evidence: One protein could not be completed due to limitations of AlphaFold 2 (CHD7). iPTM scores were extracted from individual json files and used to create a heat map with rows clustered using Seaborn and matplotlib (Extended Data Fig.
- Full pipeline: alignment/mapping [BWA, deepTools] -> quantification [deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [AlphaFold, Matplotlib, seaborn] -> visualisation [ChimeraX] -> stage not stated [ColabFold v1.5.5, GATK, ImageJ, Metascape, Picard]

### The Panoptes system uses decoy cyclic nucleotides to defend against phage. (Nature 2025)

- DOI: 10.1038/s41586-025-09557-z | PMCID: PMC12657218 | PMID: 41034579
- Evidence: The structures were determined using molecular replacement conducted by the Phaser-MR program in the PHENIX suite (v.1.21-5207) 58 using a predicted structural model of Kp OptS generated by ColabFold v.1.5.5, which uses a homology search by MMseqs2 with AlphaFold2 59 .
- Full pipeline: differential/statistical testing [tidyverse] -> structure determination [Coot v1.1.17] -> visualisation [PyMOL, tidyverse] -> stage not stated [AlphaFold, ColabFold v1.5.5, PHENIX]

### A miniature CRISPR-Cas10 enzyme confers immunity by inhibitory signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09569-9 | PMCID: PMC12657230 | PMID: 41034576
- Evidence: First, a DALI search was performed against representatives of the clustered AlphaFold Database (AFDB) using an AlphaFold2 model of the mCpol (A0A426EXS8).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Matplotlib v3.7.2, Python, seaborn v0.13.2] -> stage not stated [ColabFold, Galaxy, Jupyter, PHENIX]

### A new paradigm for outer membrane protein biogenesis in the Bacteroidota. (Nature 2025)

- DOI: 10.1038/s41586-025-09532-8 | PMCID: PMC12611786 | PMID: 41034578
- Evidence: This sorting was carried out using Uniprot entry data that included AlphaFold 23 models.
- Full pipeline: structure determination [Coot v0.9, PHENIX v1.21] -> stage not stated [AlphaFold, ChimeraX, RELION v4.03]

### Design of facilitated dissociation enables timing of cytokine signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09549-z | PMCID: PMC12611780 | PMID: 40993395
- Evidence: ...itions relative to the switch from AS1; rebuilt fusions between the switch and the newly located binder; and selected variants that were predicted by AlphaFold2 (AF2) to have substantial deformations spanning a variety of directions (AF2 predictions of the strained AS1 ternary complex were within 1.0 Å Cα RMSD of the target–AS1–effector crystal structure).
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [CCP4] -> differential/statistical testing [DESeq2] -> simulation/modelling [MDAnalysis] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> stage not stated [GROMACS v2020.2, PyMOL, RoseTTAFold]

### Collective homeostasis of condensation-prone proteins via their mRNAs. (Nature 2025)

- DOI: 10.1038/s41586-025-09568-w | PMCID: PMC12629991 | PMID: 40993389
- Evidence: AlphaFold 59 predicted local distance difference test (pLDDT) scores were obtained for the same set of proteins where available from UniProt.
- Full pipeline: read trimming [Cutadapt v4.4, STAR v2.7.0] -> alignment/mapping [STAR v2.7.0, minimap2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, CellProfiler, Cellpose v2.0, Nextflow, R]

### Covariation MS uncovers a protein that controls cysteine catabolism. (Nature 2025)

- DOI: 10.1038/s41586-025-09535-5 | PMCID: PMC12589099 | PMID: 40963025
- Evidence: (19) AlphaFold-Multimer modelling .
- Full pipeline: dimensionality reduction/clustering [ColabFold] -> visualisation [Cytoscape v3.9.1, Matplotlib, ggpubr, seaborn, tidyverse] -> stage not stated [AlphaFold, Python, R v4.2, scikit-learn]

### Structural basis for mTORC1 activation on the lysosomal membrane. (Nature 2025)

- DOI: 10.1038/s41586-025-09545-3 | PMCID: PMC12448111 | PMID: 40963021
- Evidence: Atomic model building and refinement To build the atomic model for the mTORC1–RHEB–RAG–Ragulator–4E-BP1 complex on the membrane, we first fit our previous models into the cryo-EM map as a rigid body using UCSF ChimeraX 56 , with substituted models of mTOR and RAPTOR from AlphaFold2 prediction 57 .
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [ImageJ, Topaz]

### Delta-type glutamate receptors are ligand-gated ion channels. (Nature 2025)

- DOI: 10.1038/s41586-025-09610-x | PMCID: PMC12520249 | PMID: 40957579
- Evidence: Model building was initiated with a predicted structure of a hGluD2 monomer from the AlphaFold Protein Structure Database (AF- O43424 -F1-v4).
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold]

### Programmable antisense oligomers for phage functional genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-09499-6 | PMCID: PMC12571901 | PMID: 40931073
- Evidence: Structure prediction Structures were predicted from protein sequences using Google AlphaFold3 server ( https://alphafoldserver.com/ ) 67 .
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, ImageJ v1.53]

### Structure and mechanism of the mitochondrial calcium transporter NCLX. (Nature 2025)

- DOI: 10.1038/s41586-025-09491-0 | PMCID: PMC12571890 | PMID: 40931067
- Evidence: Model building and refinement The initial model used for NCLX structure was obtained through AlphaFold2 67 prediction.
- Full pipeline: simulation/modelling [VMD] -> structure determination [AlphaFold, PHENIX] -> machine learning [Topaz v0.2.4] -> visualisation [ChimeraX, PyMOL, UCSF Chimera, VMD]

### Microbial iron oxide respiration coupled to sulfide oxidation. (Nature 2025)

- DOI: 10.1038/s41586-025-09467-0 | PMCID: PMC12545173 | PMID: 40866705
- Version used: **2.3.2**
- Evidence: The structure of the DA_402 monomer and oligomer were predicted using AlphaFold2 v2.3.2 at the COSMIC 2 science gateway.
- Full pipeline: alignment/mapping [MAFFT v7.407, RAxML v8.2.12] -> structure determination [RAxML v8.2.12] -> visualisation [R v4.1] -> stage not stated [AlphaFold v2.3.2, AutoDock Vina v1.1.2, DESeq2 v3.19, HMMER, ImageJ, featureCounts]

### One-shot design of functional protein binders with BindCraft. (Nature 2025)

- DOI: 10.1038/s41586-025-09429-6 | PMCID: PMC12507698 | PMID: 40866699
- Evidence: AlphaFold3 predictions of designed BindCraft complexes were performed using the AlphaFold3 server 49 with multiple-sequence alignments and templates enabled.
- Full pipeline: alignment/mapping [AlphaFold] -> quantification [R] -> structure determination [PHENIX] -> visualisation [ChimeraX, Python v3.9]

### Structural basis for the dynamic regulation of mTORC1 by amino acids. (Nature 2025)

- DOI: 10.1038/s41586-025-09428-7 | PMCID: PMC12507694 | PMID: 40836086
- Evidence: These initial models were iteratively rebuilt through cycles of interactive adjustments in Coot (v0.9.8) 53 and refinement in phenix.real_space_refine (Phenix v2.0) 54 , incorporating AlphaFold 2 (refs.
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [AlphaFold, ChimeraX v1.8, Coot v0.9.8] -> machine learning [Topaz] -> stage not stated [CTFFIND v4.1.14, MotionCor2, PHENIX v2.0, RELION v5.0]

### Targeting G1-S-checkpoint-compromised cancers with cyclin A/B RxL inhibitors. (Nature 2025)

- DOI: 10.1038/s41586-025-09433-w | PMCID: PMC12527934 | PMID: 40836083
- Evidence: AlphaFold protein co-folding prediction Co-folding of proteins were done by AlphaFold 2 implemented in ColabFold 76 .
- Full pipeline: alignment/mapping [limma] -> quantification [limma] -> dimensionality reduction/clustering [R v4.3.2, clusterProfiler v4.8.3, limma] -> differential/statistical testing [DESeq2 v1.36.0, GSEA, clusterProfiler v4.8.3] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, ColabFold, GSVA]

### Molecular mechanism of ultrafast transport by plasma membrane Ca&lt;sup&gt;2+&lt;/sup&gt;-ATPases. (Nature 2025)

- DOI: 10.1038/s41586-025-09402-3 | PMCID: PMC12488499 | PMID: 40836084
- Evidence: The AlphaFold model of mouse NPTN (ID: AF- P97300 -F1) was used for molecular replacement using the Phaser program 67 in PHENIX 68 .
- Full pipeline: structure determination [Coot, RELION v3.1, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1.10, ChimeraX, MotionCor2, PHENIX]

### Structural basis of fast N-type inactivation in K&lt;sub&gt;v&lt;/sub&gt; channels. (Nature 2025)

- DOI: 10.1038/s41586-025-09339-7 | PMCID: PMC12460158 | PMID: 40770100
- Evidence: Model building and structure refinement Model building was first carried out by manually fitting the transmembrane domain of Shaker (Protein Data Bank ID: 8TEO ) and the T1 domain generated by AlphaFold3 (ref.
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2, RELION, Topaz]

### Diffusing protein binders to intrinsically disordered proteins. (Nature 2025)

- DOI: 10.1038/s41586-025-09248-9 | PMCID: PMC12367549 | PMID: 40739343
- Evidence: Initial guess is the protocol in which the protein structure provided to the model as an initial guess is first converted to AlphaFold atom positions.
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX v1.21.1] -> machine learning [RoseTTAFold] -> stage not stated [AlphaFold, ImageJ v1.54p, PyMOL v2.4.0, Python v3.9.7, UCSF Chimera v1.14]

### Programmable protein ligation on cell surfaces. (Nature 2025)

- DOI: 10.1038/s41586-025-09287-2 | PMCID: PMC12321220 | PMID: 40739351
- Evidence: The phase information was determined by molecular replacement using PHASER in the CCP4 suite 41 and using an in silico AlphaFold2 (refs.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, CCP4, PyMOL v2.5]

### Design of highly functional genome editors by modelling CRISPR-Cas sequences. (Nature 2025)

- DOI: 10.1038/s41586-025-09298-z | PMCID: PMC12422970 | PMID: 40739342
- Evidence: Heatmap indicates the natural distribution of each protein family across different types of CRISPR–Cas systems. c , AlphaFold2 was used to predict structures for 2,000 randomly selected generated proteins.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### The role of metabolism in shaping enzyme structures over 400 million years. (Nature 2025)

- DOI: 10.1038/s41586-025-09205-6 | PMCID: PMC12328220 | PMID: 40634610
- Evidence: We leveraged the extensive characterization of the Saccharomycotina subphylum, which represents 400 million years of evolution and includes Saccharomyces cerevisiae and Candida albicans 2 , 17 – 19 , and examined 11,269 AlphaFold2-predicted and experimentally determined enzyme structures that belong to 424 orthologue groups (orthogroups) associated with 361 metabolic reactions in 224 metabolic pat...
- Full pipeline: alignment/mapping [UCSF Chimera] -> stage not stated [AlphaFold]

### Loss of FCoV-23 spike domain 0 enhances fusogenicity and entry kinetics. (Nature 2025)

- DOI: 10.1038/s41586-025-09155-z | PMCID: PMC12408340 | PMID: 40634609
- Evidence: Conserved APN-interacting residues are shown in red (except for the FCoV1683 RBD, which is an AlphaFold3-predicted structure 62 ). f , Zoomed-in view of FCoV-23 S domain A and RBDs (domain B) showing the conformational masking and glycan shielding of the receptor-binding loops (labelled loop 1 and loop 2) in the context of the S trimer (only part of two protomers are shown for clarity). g , Amino ...
- Full pipeline: structure determination [PHENIX v1.21] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Coot v0.9.8.8, RELION v5.0b, UCSF Chimera v1.8]

### Electron flow in hydrogenotrophic methanogens under nickel limitation. (Nature 2025)

- DOI: 10.1038/s41586-025-09229-y | PMCID: PMC12350162 | PMID: 40604290
- Version used: **3.0**
- Evidence: 7 ) was predicted with the AlphaFold3.0 server 33 .
- Full pipeline: alignment/mapping [ChimeraX, IQ-TREE, MUSCLE] -> structure determination [PHENIX] -> stage not stated [AlphaFold v3.0, MotionCor2, RELION]

### Gating and noelin clustering of native Ca&lt;sup&gt;2+&lt;/sup&gt;-permeable AMPA receptors. (Nature 2025)

- DOI: 10.1038/s41586-025-09289-0 | PMCID: PMC12422955 | PMID: 40550474
- Evidence: Model building The structural modelling of the A1A4A1A4–scFv complex was carried out using rigid body fitting of the structure of A1A2A1A2 (PDB ID: 7LDD ) and AlphaFold2 predicted models from the Alpha Fold DB using UCSF Chimera 5 , 55 , 56 .
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL v3.1] -> stage not stated [AlphaFold, ChimeraX, UCSF Chimera]

### Decoding 4-vinylanisole biosynthesis and pivotal enzymes in locusts. (Nature 2025)

- DOI: 10.1038/s41586-025-09110-y | PMCID: PMC12350148 | PMID: 40562929
- Version used: **2.0**
- Evidence: The structure was solved by a molecular replacement method using Phaser, with the predicted structure from AlphaFold v2.0 (refs.
- Full pipeline: quantification [ImageJ v1.51k] -> structure determination [PHENIX] -> stage not stated [AlphaFold v2.0]

### Complete computational design of high-efficiency Kemp elimination enzymes. (Nature 2025)

- DOI: 10.1038/s41586-025-09136-2 | PMCID: PMC12310539 | PMID: 40533551
- Evidence: The structures of these sequences were modelled using ColabFold AlphaFold2 (refs.
- Full pipeline: dimensionality reduction/clustering [MDTraj] -> simulation/modelling [MDTraj] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ColabFold, PyMOL, VMD]

### Targeting de novo purine biosynthesis for tuberculosis treatment. (Nature 2025)

- DOI: 10.1038/s41586-025-09177-7 | PMCID: PMC12328218 | PMID: 40533558
- Evidence: Molecular modelling A model of Mt PurF was generated using an AlphaFold model (AF- P9WHQ7 -F1) and compared with crystal structures of other PRPP amindotransferases 9 , 35 – 38 .
- Full pipeline: stage not stated [AlphaFold]

### Discovery of FoTO1 and Taxol genes enables biosynthesis of baccatin III. (Nature 2025)

- DOI: 10.1038/s41586-025-09090-z | PMCID: PMC12240809 | PMID: 40500440
- Evidence: The tree was produced with FastTree, rooted with red algae homologues. g , Structural model of FoTO1, generated by AlphaFold3 and aligned with the Arabidopsis thaliana orthologue with FoldSeek. h , Bar graphs showing the integrated peak area of 2 and 2’a when N- or C-terminally truncated FoTO1 is transiently expressed in N. benthamiana leaves together with TDS and T5αH.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [AlphaFold, Clustal Omega, Trimmomatic] -> dimensionality reduction/clustering [SciPy, UMAP] -> stage not stated [HMMER, NumPy, Scanpy v1.10.1]

### SP140-RESIST pathway regulates interferon mRNA stability and antiviral immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09152-2 | PMCID: PMC12310523 | PMID: 40500448
- Evidence: AlphaFold structure predictions AlphaFold-Multimer (v.2.3.2) 76 was run on equipment hosted by the Cal Cryo EM facility comprising an Nvidia GPU and >72 TB of storage space.
- Full pipeline: read trimming [BWA v0.7.15] -> alignment/mapping [BWA v0.7.15, ChimeraX v1.6.1, HISAT2 v2.1.0, MACS2 v2.1.1, SAMtools, Salmon v0.13.1] -> variant calling [DESeq2 v1.38.3] -> quantification [Salmon v0.13.1] -> normalisation [deepTools] -> visualisation [ChimeraX v1.6.1, HISAT2 v2.1.0, SAMtools] -> stage not stated [AlphaFold, BEDTools, R, ggplot2 v3.5.0]

### Probing condensate microenvironments with a micropeptide killswitch. (Nature 2025)

- DOI: 10.1038/s41586-025-09141-5 | PMCID: PMC12286862 | PMID: 40468084
- Evidence: AlphaFold models AlphaFold models were predicted using AlphaFold (v.3) 33 in multimeric mode using the default parameters.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [STAR] -> visualisation [ChimeraX v1.6, Python v3.10, R, SciPy, ggplot2, pheatmap, seaborn] -> stage not stated [AlphaFold, Cellpose, ImageJ v2.14.0]

### Protein-primed homopolymer synthesis by an antiviral reverse transcriptase. (Nature 2025)

- DOI: 10.1038/s41586-025-09179-5 | PMCID: PMC12483538 | PMID: 40436039
- Evidence: AlphaFold structural modeling.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, MAFFT, SAMtools, featureCounts] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX v1.21.2] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, BLAST, HMMER, R v4.4.0]

### EndoMAP.v1 charts the structural landscape of human early endosome complexes. (Nature 2025)

- DOI: 10.1038/s41586-025-09059-y | PMCID: PMC12222028 | PMID: 40437099
- Evidence: Large-scale AlphaFold Multimer (AF-M) 8 , 9 and AlphaLink2 (ref.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, lme4] -> visualisation [Cytoscape v3.10.1, ggplot2 v3.5.1] -> stage not stated [AlphaFold, ColabFold v1.5.2, ImageJ, PyMOL v2.6.0, igraph, pheatmap v1.0.12, tidyverse v1.1.4]

### Stepwise ATP translocation into the endoplasmic reticulum by human SLC35B1. (Nature 2025)

- DOI: 10.1038/s41586-025-09069-w | PMCID: PMC12267056 | PMID: 40399679
- Evidence: Model building The predicted AlphaFold 2 (ref.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, Galaxy, PyMOL]

### Molecular basis of SIFI activity in the integrated stress response. (Nature 2025)

- DOI: 10.1038/s41586-025-09074-z | PMCID: PMC12286842 | PMID: 40328314
- Evidence: ... analyse data: FlowJo (v.10.8.1), GraphPad Prism (v.9), NMRViewJ (v9.2.0-b27), Bruker TopSpin (v.4.3.0), cryoSPARC (v.4.3), SerialEM (v.4.1), 3DFlex, AlphaFold (v.2; v.3), PHENIX (v.1.21.1-5286), Coot (v.0.9.8.92), PDBePISA (v1.52), Chimera (v.1.17.1), ChimeraX (v.1.8), PyMOL (v.2.5.5), Spectronaut (18.0), ProteoWizard’s msConvert (v.3.0.22335), Kojak (v.2.0.3), Percolator (v.2.08) and ProXL web a...
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, PyMOL, Singularity]

### PLA2G15 is a BMP hydrolase and its targeting ameliorates lysosomal disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08942-y | PMCID: PMC12158761 | PMID: 40335701
- Evidence: DiffDock docking The structure of Homo sapiens PLA2G15 was obtained from the AlphaFold entry Q8NCC3 (UniProt).
- Full pipeline: stage not stated [AlphaFold, CellProfiler v4.2.7, ChimeraX, ImageJ v2.1.0, QuPath]

### Naturally ornate RNA-only complexes revealed by cryo-EM. (Nature 2025)

- DOI: 10.1038/s41586-025-09073-0 | PMCID: PMC12286853 | PMID: 40328315
- Evidence: For visualizing a hypothetical OLE RNA–protein complex, AlphaFold 3 (server version) 47 was used to predict: (1) a OapA dimer with a OapC monomer; and (2) RpsU using the sequences in (Supplementary Table 4 ).
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [Coot v0.9.8, MUSCLE] -> visualisation [AlphaFold] -> stage not stated [ChimeraX v1.8, PHENIX, RELION]

### Chromosome end protection by RAP1-mediated inhibition of DNA-PK. (Nature 2025)

- DOI: 10.1038/s41586-025-08896-1 | PMCID: PMC12221994 | PMID: 40240611
- Evidence: The RAP1 BRCT domain from a KU–RAP1 AlphaFold model (see ‘AlphaFold modelling’) was similarly docked into the cryo-EM map.
- Full pipeline: structure determination [PHENIX v1.20.1] -> stage not stated [AlphaFold, ChimeraX, Coot]

### Histone H1 deamidation facilitates chromatin relaxation for DNA repair. (Nature 2025)

- DOI: 10.1038/s41586-025-08835-0 | PMCID: PMC12074999 | PMID: 40240600
- Evidence: Molecular docking The AlphaFold Protein Structure Database ( https://alphafold.ebi.ac.uk/ ) was used to predict the potential structure of CTPS1 (UniProt P17812 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.5.4, SAMtools] -> stage not stated [AlphaFold, ImageJ, Picard, PyMOL, deepTools v3.5.5]

### Structure of the ATP-driven methyl-coenzyme M reductase activation complex. (Nature 2025)

- DOI: 10.1038/s41586-025-08890-7 | PMCID: PMC12176620 | PMID: 40240609
- Evidence: Moreover, AlphaFold2 (ref.
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [Coot v0.9.8.92, PHENIX v1.21] -> machine learning [Topaz] -> visualisation [ChimeraX v1.6.1] -> stage not stated [AlphaFold, IQ-TREE, UCSF Chimera v1.17.3]

### Comprehensive interrogation of synthetic lethality in the DNA damage response. (Nature 2025)

- DOI: 10.1038/s41586-025-08815-4 | PMCID: PMC12018271 | PMID: 40205037
- Evidence: The entire SPIDR dataset is available at https://spidrweb.org , including the ability to interactively query genes of interest and cross-reference to AlphaFold predictions of potential protein complexes 22 .
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> quantification [Fiji v2.9.0, ImageJ v2.9.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, MACS2 v3.0.0b, Python, R, SAMtools v1.6, limma]

### DNA-guided transcription factor interactions extend human gene regulatory code. (Nature 2025)

- DOI: 10.1038/s41586-025-08844-z | PMCID: PMC12119339 | PMID: 40205063
- Version used: **2.0**
- Evidence: We first used the AlphaFold v.2.0 multimer function ( Methods ) to predict complexes for some indicative TF–TF pairs for which the structure was either previously known or solved by us here.
- Full pipeline: differential/statistical testing [Bioconductor, ComplexHeatmap, Python, R, SciPy] -> structure determination [CCP4, PHENIX] -> machine learning [R] -> visualisation [Bioconductor, ComplexHeatmap] -> stage not stated [AlphaFold v2.0, BEDTools v2.30.0, Cytoscape, PyMOL, RoseTTAFold]

### Multimodal cell maps as a foundation for structural and functional genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08878-3 | PMCID: PMC12137143 | PMID: 40205054
- Evidence: AlphaFold-Multimer analysis All pairs of proteins in small assemblies (<10 proteins) were selected for AlphaFold-Multimer analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [PyTorch] -> machine learning [PyTorch, scikit-learn] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, NumPy v1.21.6, STRING db, SciPy v1.7.3]

### Structural dynamics of DNA unwinding by a replicative helicase. (Nature 2025)

- DOI: 10.1038/s41586-025-08766-w | PMCID: PMC12043514 | PMID: 40108462
- Evidence: The top-ranked AlphaFold2 (ref.
- Full pipeline: structure determination [ChimeraX] -> visualisation [PHENIX, PyMOL v2.6.0, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1, MotionCor2, RELION, Topaz v0.3.0]

### Cell-autonomous innate immunity by proteasome-derived defence peptides. (Nature 2025)

- DOI: 10.1038/s41586-025-08615-w | PMCID: PMC11946893 | PMID: 40044870
- Evidence: AMP accessibility analysis To analyse the position of known AMPs in the structures of mature proteins, we used AlphaFold-predicted monomeric structures 67 from the human proteome (uploaded 14 January 2024).
- Full pipeline: visualisation [PyMOL v2.5.7] -> stage not stated [AlphaFold, ComplexHeatmap v2.16.0, ImageJ v2.14.0, Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1, ggplot2 v3.4.4, scikit-learn v0.0, seaborn v0.12.2, tidyverse v1.1.2]

### Chanoclavine synthase operates by an NADPH-independent superoxide mechanism. (Nature 2025)

- DOI: 10.1038/s41586-025-08670-3 | PMCID: PMC12003167 | PMID: 40044871
- Evidence: The atomic model of apo-form EasC Cf built using AlphaFold2 (ref.
- Full pipeline: structure determination [PHENIX v1.20] -> stage not stated [AlphaFold, Coot v0.9.6, UCSF Chimera]

### The conserved HIV-1 spacer peptide 2 triggers matrix lattice maturation. (Nature 2025)

- DOI: 10.1038/s41586-025-08624-9 | PMCID: PMC11964938 | PMID: 40011770
- Version used: **2.2.0**
- Evidence: Initial coordinates for SP2 11–16 were generated using AlphaFold (v2.2.0) 56 , which were fitted roughly into the SP2 density in USCF Chimera 55 .
- Full pipeline: structure determination [PHENIX] -> visualisation [RELION] -> stage not stated [AlphaFold v2.2.0, ChimeraX v1.3, Clustal Omega, Fiji v1.54f, ImageJ v1.54f]

### In vitro reconstitution of meiotic DNA double-strand-break formation. (Nature 2025)

- DOI: 10.1038/s41586-024-08551-1 | PMCID: PMC11922769 | PMID: 39972125
- Evidence: Structural prediction using AlphaFold 3 AlphaFold 3 was used to predict the structures of the SPO11–TOP6BL heterodimer, the SPO11–TOP6BL tetramer and the SPO11–TOP6BL tetramer in complex with DNA 44 .
- Full pipeline: alignment/mapping [SAMtools v1.9] -> quantification [ImageJ] -> dimensionality reduction/clustering [PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BEDTools v2.25.0]

### Snapshots of acyl carrier protein shuttling in human fatty acid synthase. (Nature 2025)

- DOI: 10.1038/s41586-025-08587-x | PMCID: PMC12058525 | PMID: 39979457
- Evidence: For the modifying portion, two copies of the AlphaFold2 (refs.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Coot, RELION v3.1]

### Reconstitution of SPO11-dependent double-strand break formation. (Nature 2025)

- DOI: 10.1038/s41586-025-08601-2 | PMCID: PMC11922745 | PMID: 39972129
- Evidence: Although we cannot exclude that the Flag tag affects function, we note that even larger tags (FKBP or FRB) do not appear to interfere with activity and that the N-terminus of SPO11 is predicted to be unstructured in the AlphaFold 3 models.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.3, ChimeraX v1.8] -> quantification [ImageJ v1.54g] -> stage not stated [AlphaFold]

### SPO11 dimers are sufficient to catalyse DNA double-strand breaks in vitro. (Nature 2025)

- DOI: 10.1038/s41586-024-08574-8 | PMCID: PMC11922746 | PMID: 39972130
- Evidence: Quantifications show the mean and range from two independent experiments. e , AlphaFold 3 model of SPO11 dimer bound to a 40-bp duplex DNA substrate.
- Full pipeline: quantification [AlphaFold]

### Tumour-wide RNA splicing aberrations generate actionable public neoantigens. (Nature 2025)

- DOI: 10.1038/s41586-024-08552-0 | PMCID: PMC11903331 | PMID: 39972144
- Version used: **2.3.2**
- Evidence: AlphaFold2 structure predictions AlphaFold v2.3.2 and its reference databases were installed.
- Full pipeline: alignment/mapping [STAR] -> quantification [DESeq2, R, RSEM] -> differential/statistical testing [DESeq2, GSEA, R] -> stage not stated [AlphaFold v2.3.2, Picard]

### Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. (Nature 2025)

- DOI: 10.1038/s41586-024-08533-3 | PMCID: PMC11882451 | PMID: 39939763
- Evidence: Model building and refinement The initial structural models of the KBTBD4 dimer, the HDAC1/2–CoREST–ELM–SANT1 complex, were predicted with AlphaFold-Multimer in Google ColabFold2 (ref.
- Full pipeline: differential/statistical testing [R, limma] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1, Topaz] -> visualisation [Cytoscape v3.5.10, PyMOL] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, STRING db, ggplot2 v3.5.0, pandas v1.5.1]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Evidence: Model building and refinement The initial structural models of the KBTBD4 dimer and the HDAC1–CoREST–ELM–SANT1 complex was predicted with AlphaFold-Multimer in Google ColabFold2 76 .
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### Engineering a genomically recoded organism with one stop codon. (Nature 2025)

- DOI: 10.1038/s41586-024-08501-x | PMCID: PMC11903333 | PMID: 39910296
- Evidence: AlphaFold structure of RF2.B3 The 3D structure of RF2.B3 in Fig.
- Full pipeline: stage not stated [AlphaFold, Python]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Evidence: ISG15 3D structure modelling To test whether the Cys78 deletion in ISG15 of some bats affects the formation of stable ISG15 homodimers, we first used AlphaFold2 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Multiscale footprints reveal the organization of cis-regulatory elements. (Nature 2025)

- DOI: 10.1038/s41586-024-08443-4 | PMCID: PMC11839466 | PMID: 39843737
- Evidence: Right: AlphaFold3-predicted structures of Ets1 and Runx1 on example composite motifs.
- Full pipeline: quality control [FastQC v0.25] -> alignment/mapping [FastQC v0.25, PyMOL v2.6] -> quantification [Seurat] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Keras] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, ArchR, MACS2]

### Targeting protein-ligand neosurfaces with a generalizable deep learning tool. (Nature 2025)

- DOI: 10.1038/s41586-024-08435-4 | PMCID: PMC11903328 | PMID: 39814890
- Evidence: Ten sequences per design were generated and folded with AlphaFold2 in the ColabFold software 50 (single sequence mode).
- Full pipeline: structure determination [Coot v0.9.5] -> visualisation [ChimeraX, PyMOL v2.4] -> stage not stated [AlphaFold, ColabFold, PHENIX, RDKit, RoseTTAFold]

### De novo designed proteins neutralize lethal snake venom toxins. (Nature 2025)

- DOI: 10.1038/s41586-024-08393-x | PMCID: PMC11882462 | PMID: 39814879
- Evidence: The resulting designs were filtered on the basis of AlphaFold2 (AF2) initial guess 38 and Rosetta metrics, and the most promising candidates were selected for experimental characterization.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### Autoactive CNGC15 enhances root endosymbiosis in legume and wheat. (Nature 2025)

- DOI: 10.1038/s41586-024-08424-7 | PMCID: PMC11839481 | PMID: 39814887
- Evidence: Alphafold2 and structural homology modelling The structure of M. truncatula CNGC15a homotetramer was predicted with AlphaFold2 multimer, as implemented through ColabFold (v.1.5.2) 55 ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ).
- Full pipeline: quality control [FastQC v0.11.8, STAR v2.5, Trim Galore v0.6.10] -> alignment/mapping [FastQC v0.11.8, MUSCLE v3.8.425, STAR v2.5, Trim Galore v0.6.10] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v3.18, limma v3.18] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, BLAST v2.13, ColabFold v1.5.2, IQ-TREE v2.2.3]

### The sequence-structure-function relationship of intrinsic ERα disorder. (Nature 2025)

- DOI: 10.1038/s41586-024-08400-1 | PMCID: PMC11864982 | PMID: 39779860
- Evidence: Current structural techniques like cryoelectron microscopy 16 and computational tools such as AlphaFold 17 cannot effectively characterize these disordered domains, and limited biophysical data 18 – 21 have constrained our understanding of phosphorylation-triggered activation.
- Full pipeline: quantification [ImageJ] -> machine learning [AlphaFold] -> stage not stated [Python]

### Conformational protection of molybdenum nitrogenase by Shethna protein II. (Nature 2025)

- DOI: 10.1038/s41586-024-08355-3 | PMCID: PMC11754109 | PMID: 39779845
- Evidence: As starting model for MoFe, Protein Data Bank (PDB) entry 3U7Q was used, for the Fe protein PDB entry 1FP6 and for the FeSII protein a model created by AlphaFold2 (refs.
- Full pipeline: structure determination [ChimeraX, PHENIX, RELION v3.1] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4, CTFFIND v4.1]

### Site-saturation mutagenesis of 500 human protein domains. (Nature 2025)

- DOI: 10.1038/s41586-024-08370-4 | PMCID: PMC11754108 | PMID: 39779847
- Evidence: To design a second set of libraries (C1 to C7), based on the results of A1 and B3, we excluded domains without a well-defined hydrophobic core (not having at least 10% of residues with rSASA <25%) and disordered domains defined as having an average AlphaFold2 pLDDT < 50, indicative of protein disorder.
- Full pipeline: machine learning [HMMER] -> stage not stated [AlphaFold, R]

### A foundation model of transcription across human cell types. (Nature 2025)

- DOI: 10.1038/s41586-024-08391-z | PMCID: PMC11754112 | PMID: 39779852
- Evidence: Structural analysis AlphaFold benchmark on intrafamily binder prediction We classified a TF as an intrafamily binder if any two members in its TF family had a known physical interaction annotated in the STRING v.11 database, on the basis of the hypothesis that if a TF can bind as a heterodimer, it should also have the potential to bind as a homodimer owing to sequence and structure similarity (alt...
- Full pipeline: alignment/mapping [BEDTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [AlphaFold, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [ColabFold, MACS2, PyTorch, STRING db]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Evidence: PIDD1 protein structure The predicted protein structure of PIDD1 was obtained from the AlphaFold Protein Structure Database 51 , 52 .
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### Structural diversity of axonemes across mammalian motile cilia. (Nature 2025)

- DOI: 10.1038/s41586-024-08337-5 | PMCID: PMC11779644 | PMID: 39743588
- Evidence: Human proteins were replaced with either predictions from AlphaFold2 (ref.
- Full pipeline: alignment/mapping [IMOD] -> registration [IMOD] -> dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot]

### Four-component protein nanocages designed by programmed symmetry breaking. (Nature 2025)

- DOI: 10.1038/s41586-024-07814-1 | PMCID: PMC11821509 | PMID: 39695226
- Evidence: We obtained a crystal structure of one of the designs, BGL17_A31 (see Supplementary information 1.3 for protein naming), which was very close to the design model and AlphaFold2 (AF2) prediction (Fig.
- Full pipeline: stage not stated [AlphaFold]

### Lithocholic acid binds TULP3 to activate sirtuins and AMPK to slow down ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08348-2 | PMCID: PMC12222023 | PMID: 39695235
- Evidence: The in silico docking assay was then performed using the AutoDock vina software 138 (v.1.1.2), during which the structure of LCA and the AlphaFold-predicted TULP3 structure ( https://alphafold.ebi.ac.uk/entry/O75386 ) 139 , 140 were used.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, AutoDock Vina, PyMOL v2.5]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: Structure prediction of MYC/MAX–TFAP2C complex was performed using AlphaFold-Multimer run in the COSMIC 2 portal using the amino acid sequences of the TF-DBDs only 103 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### In situ analysis reveals the TRiC duty cycle and PDCD5 as an open-state cofactor. (Nature 2025)

- DOI: 10.1038/s41586-024-08321-z | PMCID: PMC11754096 | PMID: 39663456
- Evidence: AlphaFold-Multimer model of the CCT3–CCT1–CCT4–PDCD5 complex The structure of human PDCD5 in a complex with human CCT3, CCT1 and CCT4 was predicted using AlphaFold-Multimer 31 (v.2.2.0).
- Full pipeline: alignment/mapping [Clustal Omega, IMOD] -> structure determination [RELION] -> visualisation [ChimeraX, napari] -> stage not stated [AlphaFold]

### The structure of apolipoprotein B100 from human low-density lipoprotein. (Nature 2025)

- DOI: 10.1038/s41586-024-08467-w | PMCID: PMC11839476 | PMID: 39662503
- Evidence: Note that, since initiating our study, AlphaFold3 (AF3) and an accompanying webserver has been released 39 , which is capable of folding full-length apoB100 in a single run.
- Full pipeline: simulation/modelling [NAMD v2.14, PHENIX v1.20] -> structure determination [PHENIX v1.20] -> machine learning [PHENIX v1.20] -> visualisation [ChimeraX, VMD v1.9.4] -> stage not stated [AlphaFold, ColabFold]

### Structure and mechanism of the Zorya anti-phage defence system. (Nature 2025)

- DOI: 10.1038/s41586-024-08493-8 | PMCID: PMC11946911 | PMID: 39662505
- Evidence: Model building and validation We used AlphaFold2 or AlphaFold3 24 to predict all of the initial models.
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> dimensionality reduction/clustering [ColabFold v1.5.2, MUSCLE v5.1] -> simulation/modelling [GROMACS v2022.5, PyMOL] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, Python, ilastik]

### Synthetic GPCRs for programmable sensing and control of cell behaviour. (Nature 2025)

- DOI: 10.1038/s41586-024-08282-3 | PMCID: PMC11666456 | PMID: 39633047
- Evidence: Data are mean ± s.d. m , AlphaFold2 model of antagonism and antigen-dependent relief of antagonism in PAGER.
- Full pipeline: quantification [Matplotlib] -> differential/statistical testing [SciPy, seaborn] -> stage not stated [AlphaFold, ImageJ, MACS2, PHENIX, Python]

### Autoinhibition of dimeric NINJ1 prevents plasma membrane rupture. (Nature 2025)

- DOI: 10.1038/s41586-024-08273-4 | PMCID: PMC11711097 | PMID: 39476863
- Evidence: Model building and refinement Separate AlphaFold2 9 models of NINJ1 and Nb538 lacking complementarity determining regions (CDRs) were fitted into the final density-modified cryo-EM map using UCSF ChimeraX.
- Full pipeline: simulation/modelling [seaborn] -> structure determination [AlphaFold, ChimeraX] -> visualisation [PyMOL v2.5.2, seaborn] -> stage not stated [PHENIX]

### Designed endocytosis-inducing proteins degrade targets and amplify signals. (Nature 2025)

- DOI: 10.1038/s41586-024-07948-2 | PMCID: PMC11839401 | PMID: 39322662
- Evidence: The minibinders against ASGPR were designed with a Rosetta-based approach integrated with ProteinMPNN and AlphaFold2.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, Python, RoseTTAFold]

### Lethal plague outbreaks in Lake Baikal hunter-gatherers 5,500 years ago. (Nature 2026)

- DOI: 10.1038/s41586-026-10540-5 | PMCID: PMC13275307 | PMID: 42310115
- Evidence: This figure was made using data from the AlphaFold database, accession A0A0U1QV71 . c , Unrooted neighbour-joining tree from the gene sequences of ypm variants, including the pre-LNBA plague form described here. d , Presence of open reading frames around the ypm locus. e , Comparison of ancestral gene content between prehistoric plague strains from reference graph alignments, using normalized brea...
- Full pipeline: quality control [ANGSD v0.940] -> alignment/mapping [AlphaFold, Bowtie2, Picard v2.18.7, RAxML, SAMtools v1.21] -> variant calling [BCFtools v1.21, GATK] -> normalisation [AlphaFold] -> differential/statistical testing [BEDTools v2.23.0]

### Substrate selectivity of the human RNA m&lt;sup&gt;5&lt;/sup&gt;C methyltransferase NSUN2. (Nature 2026)

- DOI: 10.1038/s41586-026-10582-9 | PMCID: PMC13289585 | PMID: 42203868
- Evidence: The AlphaFold-predicted structure of Homo sapiens NSUN2 used for initial model building was accessed from the AlphaFold Protein Structure Database ( https://alphafold.ebi.ac.uk/AFDB:AF-Q08J23-3-F1 ).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4] -> structure determination [ChimeraX v1.8, PHENIX v1.21.1] -> stage not stated [AlphaFold, CCP4]

### Large-scale discovery, analysis and design of protein energy landscapes. (Nature 2026)

- DOI: 10.1038/s41586-026-10465-z | PMCID: PMC13293878 | PMID: 42129553
- Evidence: However, analysis of proline isomerization states in AlphaFold 2 models (Supplementary Fig.
- Full pipeline: dimensionality reduction/clustering [Snakemake] -> stage not stated [AlphaFold, ColabFold, Jupyter, SciPy]

### Vaccination generates broadly cross-neutralizing antibodies to the HIV Env apex. (Nature 2026)

- DOI: 10.1038/s41586-026-10429-3 | PMCID: PMC13275315 | PMID: 42056526
- Evidence: Structure determination was carried out by molecular replacement using Phaser within the Phenix software suite 51 , with an initial model generated by AlphaFold 3 52 .
- Full pipeline: structure determination [AlphaFold, Coot v0.9.8, PHENIX] -> stage not stated [ChimeraX, RELION v4.0]

### Structural basis of fungal β-1,3-glucan synthase inhibition by caspofungin. (Nature 2026)

- DOI: 10.1038/s41586-026-10409-7 | PMCID: PMC13249079 | PMID: 42020744
- Evidence: After we identified this segment as YMR295C , side chains were registered based on the AlphaFold 50 model and the presence of large aromatic side chains.
- Full pipeline: alignment/mapping [UCSF Chimera] -> registration [RELION] -> simulation/modelling [GROMACS, MDAnalysis v2.7.0, Python, VMD v1.9] -> structure determination [Coot v0.98, UCSF Chimera] -> visualisation [MDAnalysis v2.7.0, Python, VMD v1.9] -> stage not stated [AlphaFold, ChimeraX v1.10, PHENIX v1.20, PyMOL v3.1]

### Heart-nosed bat alphacoronaviruses use human CEACAM6 to enter cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10394-x | PMCID: PMC13149331 | PMID: 42020746
- Evidence: The structure of human CEACAM6 in complex with CcCoV-KY43 was solved by molecular replacement using PHASER 66 with AlphaFold 3 (ref.
- Full pipeline: alignment/mapping [BEAST v1.10.5, MAFFT v7.526] -> quantification [statsmodels] -> dimensionality reduction/clustering [MAFFT v7.526] -> structure determination [BEAST v1.10.5, IQ-TREE v2.3.4] -> stage not stated [AlphaFold, ChimeraX, ColabFold, PyMOL, QGIS, R v4.4.1, Seurat v5.3.0]

### A pro-carcinogenic bacterial toxin binds claudin-4 to cleave E-cadherin. (Nature 2026)

- DOI: 10.1038/s41586-026-10375-0 | PMCID: PMC13253352 | PMID: 42020735
- Evidence: AlphaFold modelling To model the hypothetical ternary complex between claudin-4, BFT and E-cadherin, we used AF3 implemented in the AlphaFold server ( https://alphafoldserver.com/ ) 43 .
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ImageJ, R v4.2.2, ggplot2 v3.4.4]

### Template-driven scaffolding of SCF&lt;sup&gt;FBXO42&lt;/sup&gt; regulates PP2A degradation. (Nature 2026)

- DOI: 10.1038/s41586-026-10368-z | PMCID: PMC13233325 | PMID: 41986709
- Evidence: We generated a model of FBXO42–SKP1 using AlphaFold2 29 and rigid body fit into the maps using ChimeraX.
- Full pipeline: quantification [limma] -> differential/statistical testing [limma] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, Coot, PHENIX, R]

### Cytoplasmic lattices are megadalton storage complexes in mammalian oocytes. (Nature 2026)

- DOI: 10.1038/s41586-026-10513-8 | PMCID: PMC13253339 | PMID: 41986725
- Evidence: Once we had pinpointed the locations of these proteins, we replaced the published structures with mouse AlphaFold predictions 48 , 49 .
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [AlphaFold, RELION]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Evidence: AlphaFold2 and AlphaFold3 predictions Structure predictions were done with AlphaFold2 implemented in a google colab notebook 70 available online ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb.Predictions ); predictions using AlphaFold3 71 were done at https://alphafoldserver.com/ .
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### EBV strain interacts with host HLA to drive nasopharyngeal carcinoma risk. (Nature 2026)

- DOI: 10.1038/s41586-026-10416-8 | PMCID: PMC13190245 | PMID: 41986726
- Evidence: AlphaFold3-based structure prediction The structures of peptide–HLA-A*11:01 complexes for the low-risk peptide VVILENVGQ (85841A encoded) and the high-risk peptide VVILENVSR (85841G encoded) were predicted using the AlphaFold3 public web server 94 .
- Full pipeline: quality control [PLINK v1.9] -> read trimming [fastp] -> alignment/mapping [MAFFT v7.490, VCFtools v0.1.13] -> variant calling [PLINK v1.9] -> stage not stated [AlphaFold, GATK, GEMMA, IQ-TREE, Picard v2.18.14, PyMOL v3.1.6.1, R]

### Structural basis of supercoiling-induced CRISPR-Cas9 off-target activity. (Nature 2026)

- DOI: 10.1038/s41586-026-10255-7 | PMCID: PMC13171457 | PMID: 41882360
- Evidence: An AlphaFold3 model of apo Sp Cas9 was used to fill in regions that were previously unmodelled, including residues 512–573, 611–678 and 685–730.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX, RELION] -> stage not stated [AlphaFold, Fiji, ImageJ, Topaz]

### The E3 ubiquitin ligase mechanism specifying targeted microRNA degradation. (Nature 2026)

- DOI: 10.1038/s41586-026-10232-0 | PMCID: PMC13083262 | PMID: 41851464
- Evidence: AlphaFold3 structure predictions supported the expected assembly of the D-domain.
- Full pipeline: read trimming [Cutadapt v4.8] -> quantification [R] -> normalisation [DESeq2 v1.38.3] -> differential/statistical testing [R] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Evidence: Protein structural modelling The structures and binding interfaces of the protein complexes were generated using AlphaFold3 (ref.
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### Assembly of helper NLR resistosome clusters upon activation of a coiled-coil NLR. (Nature 2026)

- DOI: 10.1038/s41586-026-10215-1 | PMCID: PMC13043302 | PMID: 41813892
- Evidence: Protein structure prediction and analysis The 3D structures of the type II CNL proteins and ADR1s were predicted using AlphaFold2 (refs.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [R v4.3.1, ggplot2] -> differential/statistical testing [lme4] -> visualisation [Matplotlib, NumPy, PyMOL, Python v3.10, R v4.3.1, SciPy, ggplot2] -> stage not stated [AlphaFold, ImageJ, TrackMate]

### B cell imprinting in children impairs antibodies to the haemagglutinin stalk. (Nature 2026)

- DOI: 10.1038/s41586-026-10248-6 | PMCID: PMC13171607 | PMID: 41813896
- Evidence: For model building, the AlphaFold3-predicted model and the cryo-EM structure of Mich15 H1 (PDB: 7KNA ) were used as the initial models for HK14 H3 and Mich15 H1, respectively.
- Full pipeline: quality control [Seurat v4.3.0, UMAP] -> alignment/mapping [Clustal Omega] -> normalisation [Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.3.0, UMAP, fgsea] -> differential/statistical testing [Seurat v4.3.0, UMAP] -> structure determination [Coot v0.9.8, PHENIX] -> visualisation [R v4.2, Seurat v4.3.0, UMAP, ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python]

### The molecular basis of force selectivity by PIEZO2. (Nature 2026)

- DOI: 10.1038/s41586-026-10182-7 | PMCID: PMC13149025 | PMID: 41781615
- Evidence: The PIEZO2 cryo-EM structure lacks the extracellular loop containing the tagging location at amino acid 105, so an AlphaFold III model was generated for a monomer of mouse PIEZO2, and the last PIEZO repeat domain was superposed onto the equivalent domain of the 6KG7 cryo-EM structure in UCSF Chimera software.
- Full pipeline: stage not stated [AlphaFold, UCSF Chimera]

### DICER cleavage fidelity is governed by 5'-end binding pockets. (Nature 2026)

- DOI: 10.1038/s41586-026-10211-5 | PMCID: PMC13171623 | PMID: 41781616
- Evidence: The initial RNA models for 26S-UG, 26S-GU and pre-mir-517a_GU were generated using AlphaFold3 for three-dimensional (3D) RNA structure prediction 41 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, Bowtie2, Coot v0.9.8.96] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.7, Coot v0.9.8.96, PHENIX v1.20.1] -> stage not stated [PyMOL]

### Genome modelling and design across all domains of life with Evo 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10176-5 | PMCID: PMC13128491 | PMID: 41781614
- Evidence: AlphaFold 3 (AF3) structure predictions with feature activations overlaid, of EF–Tu in complex with the tRNA (left) and of RpoB and RpoC in complex (right). e , A feature in the human genome with preferential activation immediately after frameshift mutations over other less deleterious mutation types. f , Features with activation on DNA motifs in the human genome that correspond to transcription f...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HMMER, Pangolin] -> machine learning [AUGUSTUS, UMAP] -> stage not stated [AlphaFold, BLAST, HOMER]

### Limited thermal tolerance in tropical insects and its genomic signature. (Nature 2026)

- DOI: 10.1038/s41586-026-10155-w | PMCID: PMC12999521 | PMID: 41781608
- Evidence: 6 ). b , Melting temperatures depend on the stability of the structure of proteins, such as cytochrome P450 4C1 (example AlphaFold predicted structure). c , e , Experimentally tested critical thermal maxima (CT max ) of the six major insect orders ( n = 3,229 individuals) for the Neotropics ( c ) and Afrotropics ( e ).
- Full pipeline: structure determination [phytools] -> visualisation [phytools] -> stage not stated [AlphaFold, BUSCO, Conda]

### A membrane-bound nuclease directly cleaves phage DNA during genome injection. (Nature 2026)

- DOI: 10.1038/s41586-026-10207-1 | PMCID: PMC13190303 | PMID: 41741653
- Evidence: Mutations were mapped onto the SNIPE structure predicted by AlphaFold3 using UCSF ChimeraX.
- Full pipeline: alignment/mapping [AlphaFold, ChimeraX] -> stage not stated [Fiji, HMMER, ImageJ]

### CLCC1 governs ER bilayer equilibration to maintain lipid homeostasis. (Nature 2026)

- DOI: 10.1038/s41586-026-10161-y | PMCID: PMC13061606 | PMID: 41741642
- Evidence: CLCC1 structure prediction The amino acid sequence 91–360 of human CLCC1 was used to predict the monomer and hexamer structure using AlphaFold3 33 .
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2] -> dimensionality reduction/clustering [R] -> structure determination [IMOD] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX v1.7.1, Fiji, ImageJ]

### CLCC1 promotes hepatic neutral lipid flux and nuclear pore complex assembly. (Nature 2026)

- DOI: 10.1038/s41586-025-10064-4 | PMCID: PMC13061601 | PMID: 41741636
- Evidence: Structure predictions Monomeric and multimeric sequences were submitted to AlphaFold2 using MMseqs2 using either the Google Colabatory 43 or COSMIC2 44 or were submitted to DMFold, MultiFOLD, or trRosetta 45 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3] -> quantification [Fiji v1.53e, ImageJ v1.53e, Python v3.0] -> simulation/modelling [ColabFold, GROMACS v2023.3] -> visualisation [Fiji v1.53e, ImageJ v1.53e, PyMOL v2.5.0] -> stage not stated [AlphaFold, DESeq2 v1.5, HMMER, PHENIX, STRING db]

### Coral microbiomes as reservoirs of unknown genomic and biosynthetic diversity. (Nature 2026)

- DOI: 10.1038/s41586-026-10159-6 | PMCID: PMC13083261 | PMID: 41741644
- Version used: **2.2.0**
- Evidence: Protein and protein–complex structures were predicted using AlphaFold (v.2.2.0) 136 .
- Full pipeline: alignment/mapping [BLAST v2.15.0, BWA v0.7.17, DIAMOND v2.0.15.153, Flye v2.9.3] -> differential/statistical testing [R v4.2.2, ape (R) v5.7] -> structure determination [BLAST v2.15.0] -> visualisation [ape (R) v5.7] -> stage not stated [AlphaFold v2.2.0, ComplexHeatmap v2.14.0, eggNOG v5.0.2, ggplot2 v3.4.2]

### Accurate predictions of disordered protein ensembles with STARLING. (Nature 2026)

- DOI: 10.1038/s41586-026-10141-2 | PMCID: PMC13043300 | PMID: 41708867
- Evidence: Although IDRs are often ignored or visualized as AlphaFold ‘orange spaghetti’, STARLING makes it straightforwards for anyone to obtain realistic coarse-grained ensembles.
- Full pipeline: visualisation [AlphaFold]

### Ancient co-option of LTR retrotransposons as yeast centromeres. (Nature 2026)

- DOI: 10.1038/s41586-025-10092-0 | PMCID: PMC13017519 | PMID: 41708848
- Evidence: ( d ) AlphaFold 3 models of Ctf13 from S. cerevisiae and H. occidentalis .
- Full pipeline: read trimming [SAMtools v1.9, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.2.9, HMMER v3.3.2, MAFFT v7.150b, kallisto] -> stage not stated [AlphaFold, BUSCO, Canu v2.2, IQ-TREE, Medaka v1.7, Pilon v1.23, SPAdes v4.1.0, deepTools v3.5.2]

### Bacterial immune activation via supramolecular assembly with phage triggers. (Nature 2026)

- DOI: 10.1038/s41586-025-10060-8 | PMCID: PMC13017515 | PMID: 41639456
- Evidence: The central ring was modelled using an AlphaFold prediction of the RAZR ZFD, fitted with phenix.local_em_fitting 45 and refined through manual rebuilding in Coot and Phenix.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, Cutadapt v1.15] -> alignment/mapping [Bowtie2 v2.3.4.1, Cutadapt v1.15, MAFFT, NumPy, SAMtools v1.7] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> machine learning [Topaz]

### Chemical capture of diazo metabolites reveals biosynthetic hydrazone oxidation. (Nature 2026)

- DOI: 10.1038/s41586-025-10079-x | PMCID: PMC13061610 | PMID: 41639443
- Evidence: A structure homology search of the Dali Webserver 43 using an AlphaFold 44 predicted structure of Dob3 revealed strong structural homology to the characterized ferritin-like diiron oxygenases (FDOs) AurF ( Z = 40.1, 31% sequence identity) and CmlI ( Z = 40.9, 47% sequence identity), which catalyse six-electron N -oxidation of aryl amines to aryl nitro groups during the biosynthesis of aureothin an...
- Full pipeline: visualisation [Cytoscape] -> stage not stated [AlphaFold, BLAST, InterProScan, Prokka]

### Single-molecule dynamics of the TRiC chaperonin system in vivo. (Nature 2026)

- DOI: 10.1038/s41586-025-10073-3 | PMCID: PMC13061604 | PMID: 41639457
- Evidence: The centre line is the mean and error bars show s.e.m. * P = 0.042, ** P = 0.006 (one-way Welch’s ANOVA). h , Actin structure (Protein Data Bank (PDB) visualization of AlphaFold predicted structure: AF_AFP60709F1 ). i , Actin truncations used in experiments.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10a] -> visualisation [AlphaFold] -> stage not stated [TrackMate]

### Human and bacterial genetic variation shape oral microbiomes and health. (Nature 2026)

- DOI: 10.1038/s41586-025-10037-7 | PMCID: PMC12979206 | PMID: 41606319
- Evidence: AlphaFold3 prediction of protein structures To predict protein structures for Streptococcus parasanguinis AbpA or AbpB (bound to human AMY1), the Veillonella sp.
- Full pipeline: quality control [DeepVariant v1.3.0, PLINK v2.00a] -> alignment/mapping [DeepVariant v1.3.0] -> variant calling [DeepVariant v1.3.0] -> differential/statistical testing [LDSC, R] -> visualisation [ChimeraX v1.9] -> stage not stated [AlphaFold, Bowtie2, MetaPhlAn v4.0.6, SAMtools v1.15.1]

### A prophage-encoded abortive infection protein preserves host and prophage spread. (Nature 2026)

- DOI: 10.1038/s41586-025-10070-6 | PMCID: PMC13043305 | PMID: 41606329
- Evidence: For apo-HepS AlphaFold2 models of monomeric HepS were used for molecular replacement.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT] -> structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BEDTools v2.27.1, PHENIX, SAMtools v1.1]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Evidence: AlphaFold-based modelling of protein structures AlphaFold 3 with its implementation in the AlphaFold Server was used to predict the DNA–protein structures 40 .
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### Scalable and multiplexed recorders of gene regulation dynamics across weeks. (Nature 2026)

- DOI: 10.1038/s41586-026-10156-9 | PMCID: PMC13102694 | PMID: 41588170
- Evidence: Molecular dynamics simulations The structure of the protein monomer for simulations was predicted by AlphaFold3 (ref.
- Full pipeline: alignment/mapping [PyMOL] -> dimensionality reduction/clustering [UMAP, scikit-image] -> simulation/modelling [AlphaFold, GROMACS v2021.1] -> stage not stated [ImageJ, PyTorch, napari]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Evidence: During the model-building process, initial reports describing AlphaFold2 (ref.
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Evidence: Protein conservation and structure visualization The mouse SPOCD1 TFIIS-M structure was generated using AlphaFold2 45 using the ColabFold v1.5.5 notebook 46 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### Polyamine-dependent metabolic shielding regulates alternative splicing. (Nature 2026)

- DOI: 10.1038/s41586-025-09965-1 | PMCID: PMC12999471 | PMID: 41535471
- Evidence: As no complete, high-resolution structure is available for this protein, we generated full-atom AlphaFold models and docked Put, Spd and Spm on the phosphorylatable sites (Ser365, Ser367 and Ser369 in SF3A3).
- Full pipeline: stage not stated [AlphaFold, GSEA]

### Microbiota-induced T cell plasticity enables immune-mediated tumour control. (Nature 2026)

- DOI: 10.1038/s41586-025-09913-z | PMCID: PMC12960244 | PMID: 41535459
- Evidence: In panel a , the ribbon-helix model was generated using AlphaFold2 to illustrate the predicted structure of the SFB-3340 protein fragment containing the TCR 7B8 epitope.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [AlphaFold, MACS2, Seurat v5.1.0]

### CFAP20 salvages arrested RNAPII from the path of co-directional replisomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09943-7 | PMCID: PMC12935552 | PMID: 41535461
- Evidence: Scale bar, 10 μm. i , AlphaFold model of CFAP20, highlighting residue R100; positively charged residues are in blue. j , Quantification of nuclear R-loop signal from h for the indicated stable cell lines.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.7a, Trim Galore v0.6.5] -> alignment/mapping [BWA v0.7.17, STAR v2.7.7a, Trim Galore v0.6.5] -> quantification [AlphaFold] -> stage not stated [HOMER, SAMtools v1.11]

### RNA-triggered Cas12a3 cleaves tRNA tails to execute bacterial immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09852-9 | PMCID: PMC12851939 | PMID: 41501459
- Evidence: Model building, refinement and figure preparation All models corresponding to the Ba1 Cas12a3 binary, ternary and quaternary complexes were originally generated by AlphaFold3 (ref.
- Full pipeline: read trimming [BWA v0.7.17, IQ-TREE v2.3.6, Trimmomatic v0.39] -> alignment/mapping [BLAST, BWA v0.7.17, Clustal Omega, IQ-TREE v2.3.6] -> structure determination [AlphaFold, ChimeraX v1.7, IQ-TREE v2.3.6, PHENIX v1.20.1] -> visualisation [Matplotlib, Python] -> stage not stated [SAMtools v1.9]

### Systematic analyses of lipid mobilization by human lipid transfer proteins. (Nature 2026)

- DOI: 10.1038/s41586-025-10040-y | PMCID: PMC12979188 | PMID: 41501472
- Evidence: Colour scheme as in a . d , Visualization of the structures of human PITPNA (Protein Data Bank (PDB): 1UW5 ), PITPNB (AlphaFold model), STARD2 (PDB: 7U9D ) and SEC14L2 (PDB: 4OMJ ) highlighting the presence of a phenylalanine signature (in magenta) in the fatty acid-binding region of PITPNA and PITPNB but not in STARD2 and SEC14L2.
- Full pipeline: visualisation [AlphaFold]

### NAC controls nascent chain fate through tunnel sensing and chaperone action. (Nature 2026)

- DOI: 10.1038/s41586-025-10058-2 | PMCID: PMC13043293 | PMID: 41430436
- Evidence: AlphaFold modelling further supports this mechanism, predicting that the NACβ N terminus forms an amphipathic helix capable of interacting with Late intra-tunnel NC segments (Extended Data Fig.
- Full pipeline: read trimming [Cutadapt v1.4.2] -> alignment/mapping [STAR] -> stage not stated [AlphaFold]

### Cross-regulation of [2Fe-2S] cluster synthesis by ferredoxin-2 and frataxin. (Nature 2026)

- DOI: 10.1038/s41586-025-09822-1 | PMCID: PMC12804074 | PMID: 41372413
- Version used: **2.2**
- Evidence: AlphaFold We used our in-house implementation of ColabFold 1.3 49 , which incorporates AlphaFold 2.2 50 , to generate models for the ISC complex composed of NFS1, ISD11, ACP, ISCU2 and FDX2, with the corresponding Uniprot IDs Q9Y697 , Q9HD34 , O14561 (69–156), Q9H1K1 (35–167) and Q6P4F2 (56-186), respectively.
- Full pipeline: visualisation [PyMOL v3.0] -> stage not stated [AlphaFold v2.2, ColabFold v1.3]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Evidence: AlphaFold3 multimer prediction For each AlphaFold3 protein–protein interaction and docking prediction, the full sequence of proteins was used as input 67 .
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### A direct role for a mitochondrial targeting sequence in signalling stress. (Nature 2026)

- DOI: 10.1038/s41586-025-09834-x | PMCID: PMC7618714 | PMID: 41372412
- Evidence: ( d ) AlphaFold3 modeling of the interaction between Pdr3 (residues 86-856, in orange) and the N-terminus of Mge1 (residues 1-60, in green).
- Full pipeline: quantification [R v4.4.1, featureCounts] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [AlphaFold, BLAST v2.14.0, ImageJ]

### Computational design of metallohydrolases. (Nature 2026)

- DOI: 10.1038/s41586-025-09746-w | PMCID: PMC12727532 | PMID: 41339547
- Evidence: The catalytic geometry and interactions with the transition state of those designs for which the AlphaFold2 35 predicted structure was close to the design model were further optimized using iterative LigandMPNN 36 and constrained Rosetta repacking and minimization 37 (Extended Data Fig.
- Full pipeline: machine learning [AlphaFold]

### Computational enzyme design by catalytic motif scaffolding. (Nature 2026)

- DOI: 10.1038/s41586-025-09747-9 | PMCID: PMC12727513 | PMID: 41339546
- Evidence: In the final evaluation step, these sequences are predicted with AlphaFold2 and ranked with a combination of metrics for structure quality and active site positioning.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis] -> structure determination [PHENIX] -> stage not stated [AlphaFold, SciPy]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Evidence: BLK γ-secretase complex prediction and molecular dynamics simulations The BLK–γ-secretase complex was predicted using AlphaFold3, with template information enabled for γ-secretase 43 .
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Progressive coevolution of the yeast centromere and kinetochore. (Nature 2026)

- DOI: 10.1038/s41586-025-09779-1 | PMCID: PMC12925627 | PMID: 41299172
- Evidence: AlphaFold2-Multimer modelling of Cbf1 dimers We predicted structures for Cbf1 dimers from J. lodderae , J. jinghongensis and J. spencerorum using a local installation of ColabFold 1.5.5 (ref.
- Full pipeline: alignment/mapping [HMMER, MAFFT v7.505] -> structure determination [MAFFT v7.505] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5.5, IQ-TREE, NumPy, Python]

### Structural basis of regulated N-glycosylation at the secretory translocon. (Nature 2026)

- DOI: 10.1038/s41586-025-09756-8 | PMCID: PMC12804085 | PMID: 41261126
- Evidence: 76 ) implementation of AlphaFold2 multimer v3 (ref.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [TopHat v2.1.0] -> quantification [HTSeq v2.0.3] -> structure determination [Coot, PHENIX] -> machine learning [Coot] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

### Semantic design of functional de novo genes from a genomic language model. (Nature 2026)

- DOI: 10.1038/s41586-025-09749-7 | PMCID: PMC12804078 | PMID: 41261132
- Evidence: Structural similarity was evaluated by generating protein structure predictions using AlphaFold 3 (ref.
- Full pipeline: alignment/mapping [MAFFT v7.526] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [igraph v0.11.6] -> visualisation [ChimeraX, Matplotlib] -> stage not stated [AlphaFold, BLAST, HMMER v3.3.0, Python v3.11.8, SciPy v1.11.4]

### ZAK activation at the collided ribosome. (Nature 2026)

- DOI: 10.1038/s41586-025-09772-8 | PMCID: PMC12823453 | PMID: 41261136
- Evidence: The tips of ES6c (690–740) and ES6b (741–800) were built based on AlphaFold3 prediction of 18S rRNA fitting into low-pass-filtered density on the collided 80S and the stable disome reconstructions (Extended Data Fig.
- Full pipeline: read trimming [SAMtools, Trim Galore] -> alignment/mapping [MotionCor2 v1.4.0, SAMtools, STAR] -> structure determination [AlphaFold, ChimeraX v1.9, PHENIX v1.20.1, UCSF Chimera] -> stage not stated [Coot, RELION v5.0]

### Potent neutralization of Marburg virus by a vaccine-elicited antibody. (Nature 2026)

- DOI: 10.1038/s41586-025-09868-1 | PMCID: PMC12893919 | PMID: 41225006
- Evidence: Model building and refinement USCF ChimeraX 74 and Coot 75 were used to fit into the map initial models of the MARV GP (PDB identifier: 6BP2 ) and MARV16 Fab, which was predicted using AlphaFold2 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39] -> differential/statistical testing [RELION] -> structure determination [AlphaFold, ChimeraX, PHENIX]

### An ATP-gated molecular switch orchestrates human mRNA export. (Nature 2026)

- DOI: 10.1038/s41586-025-09832-z | PMCID: PMC12823420 | PMID: 41198879
- Evidence: The ALYREF N-UBM was modelled in Coot based on the superposition of an AlphaFold2 Multimer prediction model of a UAP56–ALYREF complex on UAP56 chain p.
- Full pipeline: visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, Cellpose, Coot, RELION v3.1]

### Atomically accurate de novo design of antibodies with RFdiffusion. (Nature 2026)

- DOI: 10.1038/s41586-025-09721-5 | PMCID: PMC12727541 | PMID: 41193805
- Evidence: Training RFdiffusion for antibody design RFdiffusion uses the AlphaFold2 (ref.
- Full pipeline: machine learning [AlphaFold]

### Targeted in situ cross-linking mass spectrometry and integrative modeling reveal the architectures of three proteins from SARS-CoV-2. (PNAS 2021)

- DOI: 10.1073/pnas.2103554118 | PMCID: PMC8403911 | PMID: 34373319
- Evidence: We have therefore referred to the Nsp2 model generated by AlphaFold2 from DeepMind ( 29 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold]

### Harold A. Scheraga (10/18/1921-8/1/2020): A pioneering scientist who laid the foundations of protein science in the 20th century. (PNAS 2021)

- DOI: 10.1073/pnas.2026796118 | PMCID: PMC7923550 | PMID: 33547253
- Evidence: A breakthrough in this field shook the structural biophysics world 2 weeks ago: AlphaFold, a deep-learning–based computing system has been declared to have solved the 60-year-old “protein-folding” challenge.
- Full pipeline: stage not stated [AlphaFold]

### Creative destruction: New protein folds from old. (PNAS 2022)

- DOI: 10.1073/pnas.2207897119 | PMCID: PMC9907106 | PMID: 36534803
- Evidence: The 3D structures of these constructs (deposited in FigShare, DOI 10.6084/m9.figshare.19412180 as Files 7 and 8 ( 81 )) were predicted with AlphaFold ( 49 ) in ColabFold ( 85 ) using the single-sequence option.
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold]

### Assembly and architecture of the type III secretion sorting platform. (PNAS 2022)

- DOI: 10.1073/pnas.2218010119 | PMCID: PMC9907115 | PMID: 36512499
- Evidence: Coupling AlphaFold 2 (AF2) modeling and in vivo photo-cross-linking to map the needle complex interface with the sorting platform protein OrgA.
- Full pipeline: stage not stated [AlphaFold]

### A de novo protein catalyzes the synthesis of semiconductor quantum dots. (PNAS 2022)

- DOI: 10.1073/pnas.2204050119 | PMCID: PMC9907092 | PMID: 36508665
- Evidence: To study the active site of ConK in the absence of an experimentally determined structure, we used AlphaFold ( 46 ) to predict the structure.
- Full pipeline: stage not stated [AlphaFold]

### MipZ caps the plus-end of FtsZ polymers to promote their rapid disassembly. (PNAS 2022)

- DOI: 10.1073/pnas.2208227119 | PMCID: PMC9897490 | PMID: 36490318
- Evidence: Protein modeling was performed with AlphaFold-Multimer v2.1.0 ( 62 ), as implemented in Google Colab, without the use of homologous structures as templates.
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, R v3.5.1]

### FtsEX-independent control of RipA-mediated cell separation in <i>Corynebacteriales</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2214599119 | PMCID: PMC9897464 | PMID: 36469781
- Evidence: AlphaFold Prediction of Complex Structures.
- Full pipeline: structure determination [IQ-TREE v2.0.6, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CCP4, ColabFold, HMMER]

### Chemical genetic screening identifies nalacin as an inhibitor of GH3 amido synthetase for auxin conjugation. (PNAS 2022)

- DOI: 10.1073/pnas.2209256119 | PMCID: PMC9894192 | PMID: 36454752
- Evidence: We analyzed the binding pockets of all GH3s by sequence alignment and comparing their three-dimensional structures obtained from the Protein Data Bank (PDB), AlphaFold ( 38 ), and our de novo homology modeling results ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [AlphaFold] -> dimensionality reduction/clustering [AlphaFold]

### Mechanism of actin filament branch formation by Arp2/3 complex revealed by a high-resolution cryo-EM structureof the branch junction. (PNAS 2022)

- DOI: 10.1073/pnas.2206722119 | PMCID: PMC9894260 | PMID: 36442092
- Evidence: We also used a model of the Arp2/3 complex determined by cryo-EM (PDB: 6W18) and model of the individual subunits of Arp2/3 complex generated by AlphaFold ( 15 ) as references for cross-validation.
- Full pipeline: registration [RELION v4.0] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> visualisation [ChimeraX] -> stage not stated [Coot, PyMOL]

### A proteome-wide map of chaperone-assisted protein refolding in a cytosol-like milieu. (PNAS 2022)

- DOI: 10.1073/pnas.2210536119 | PMCID: PMC9860312 | PMID: 36417429
- Evidence: To further test this interpretation, for each half-tryptic peptide we used the AlphaFold database to calculate the relative solvent accessible surface area (rSASA) of each PK cut site in the context of its native protein structure ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, Python]

### Structure of the NuA4 histone acetyltransferase complex. (PNAS 2022)

- DOI: 10.1073/pnas.2214313119 | PMCID: PMC9860254 | PMID: 36417436
- Evidence: The long and flexible linkers in AlphaFold-predicted structures of Actin and Arp4 were first deleted using COOT ( 35 ) and then docked into the 3.8 Å Cryo-EM map of the core module using Chimera ( 34 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, PHENIX]

### Are general circulation models obsolete? (PNAS 2022)

- DOI: 10.1073/pnas.2202075119 | PMCID: PMC9704743 | PMID: 36375059
- Evidence: These methods have led to some spectacular successes in various fields: AlphaFold, for example, can decipher the structure of complex molecules directly from data ( 17 ).
- Full pipeline: stage not stated [AlphaFold]

### Structures of NPAS4-ARNT and NPAS4-ARNT2 heterodimers reveal new dimerization modalities in the bHLH-PAS transcription factor family. (PNAS 2022)

- DOI: 10.1073/pnas.2208804119 | PMCID: PMC9674253 | PMID: 36343253
- Evidence: Interestingly, we found that this Jα is also present in the predicted NPAS4 structure by the new AlphaFold2 algorithm ( 43 ), suggesting that the formation of this α-helix may be an intrinsic and preexisting feature of NPAS4 that does not simply form upon dimerization.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Functional genomics of OCTN2 variants informs protein-specific variant effect predictor for Carnitine Transporter Deficiency. (PNAS 2022)

- DOI: 10.1073/pnas.2210247119 | PMCID: PMC9674959 | PMID: 36343260
- Evidence: Four sets of features were generated: 1) sequence-based features describing the resulting amino acid change and position in OCTN2 protein sequence; 2) structure-based features extracted from the AlphaFold-2 structural model [default model download from the AlphaFold Protein Structure Database ( 63 , 64 )]; 3) prediction-based features derived from unsupervised variant effect prediction models, inc...
- Full pipeline: differential/statistical testing [R v3.6.3] -> stage not stated [AlphaFold, ggplot2 v3.3.5]

### Long noncoding RNA-mediated activation of PROTOR1/PRR5-AKT signaling shunt downstream of PI3K in triple-negative breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2203180119 | PMCID: PMC9618063 | PMID: 36269860
- Version used: **2.1.1**
- Evidence: The hnRNPA2 and hnRNPB1 protein structures were predicted using AlphaFold v2.1.1 ( 30 ).
- Full pipeline: quantification [HTSeq] -> stage not stated [AlphaFold v2.1.1, ImageJ, PyMOL v2.5.0]

### A generic framework for hierarchical de novo protein design. (PNAS 2022)

- DOI: 10.1073/pnas.2206111119 | PMCID: PMC9618129 | PMID: 36252041
- Evidence: Structure Predictions Using trRosetta and AlphaFold.
- Full pipeline: stage not stated [AlphaFold, BLAST]

### A blast fungus zinc-finger fold effector binds to a hydrophobic pocket in host Exo70 proteins to modulate immune recognition in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2210559119 | PMCID: PMC9618136 | PMID: 36252011
- Evidence: We then modeled rice OsExo70B1 using AlphaFold2 ( 65 ), as implemented in ColabFold ( 66 ) ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [ChimeraX] -> stage not stated [AlphaFold, ColabFold]

### Cryo-EM structures of light-harvesting 2 complexes from <i>Rhodopseudomonas palustris</i> reveal the molecular origin of absorption tuning. (PNAS 2022)

- DOI: 10.1073/pnas.2210109119 | PMCID: PMC9618040 | PMID: 36251992
- Evidence: We used AlphaFold 2 ( 34 ) to calculate a model for the α- and β-apoproteins in the PucB-LH2, which shows that the 17 untraced C-terminal residues of this α-polypeptide form a unstructured membrane-extrinsic domain ( SI Appendix , Fig.
- Full pipeline: registration [RELION] -> structure determination [PHENIX] -> machine learning [PHENIX] -> stage not stated [AlphaFold, BLAST]

### The unstructured linker of Mlh1 contains a motif required for endonuclease function which is mutated in cancers. (PNAS 2022)

- DOI: 10.1073/pnas.2212870119 | PMCID: PMC9586283 | PMID: 36215471
- Evidence: The carboxyl-terminal regions of Mlh1 and Pms1 were simultaneously modeled as a 1:1 heterodimer using Alphafold ( 49 ) using the web interface at https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/beta/AlphaFold2_advanced.ipynb .
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Docking-based long timescale simulation of cell-size protein systems at atomic resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2210249119 | PMCID: PMC9565162 | PMID: 36191203
- Evidence: In structural biology, AlphaFold has achieved unprecedented near-experimental accuracy in predicting the structure of individual proteins ( 1 ) and, at the same time, a similar approach is successfully used in a different research field—protein docking—to predict the structure of protein complexes ( 2 , 3 ).
- Full pipeline: stage not stated [AlphaFold, PyMOL v2.5]

### Dissecting the stability determinants of a challenging de novo protein fold using massively parallel design and experimentation. (PNAS 2022)

- DOI: 10.1073/pnas.2122676119 | PMCID: PMC9564214 | PMID: 36191185
- Evidence: We also examined whether the structure prediction model AlphaFold 2 ( 21 ) could be applied to differentiate stable and unstable designs.
- Full pipeline: stage not stated [AlphaFold]

### SPACA9 is a lumenal protein of human ciliary singlet and doublet microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2207605119 | PMCID: PMC9564825 | PMID: 36191189
- Evidence: AlphaFold2 models of human MIPs, obtained from the AlphaFold Protein Structure Database (AlphaFold DB) ( 22 ), were superposed onto the models of their bovine orthologs and manually corrected.
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX, Clustal Omega v1.2.2] -> stage not stated [AlphaFold, Coot v0.9.4.1, IMOD, PHENIX, PyMOL v2.3.4, RELION]

### Spns1 is a lysophospholipid transporter mediating lysosomal phospholipid salvage. (PNAS 2022)

- DOI: 10.1073/pnas.2210353119 | PMCID: PMC9546575 | PMID: 36161949
- Evidence: Model of the cytosol-facing conformation of human Spns1 was obtained from the AlphaFold database ( 42 ).
- Full pipeline: stage not stated [AlphaFold]

### A family of unusual immunoglobulin superfamily genes in an invertebrate histocompatibility complex. (PNAS 2022)

- DOI: 10.1073/pnas.2207374119 | PMCID: PMC9546547 | PMID: 36161920
- Evidence: For single-domain predictions, we generated a custom multiple sequence alignment, as detailed in SI Appendix which was submitted to Colabfold via the “AlphaFold2_mmseqs2” notebook, version 1.1 ( 40 ) and were deposited in Zenodo ( 22 ).
- Full pipeline: alignment/mapping [AlphaFold, HISAT2] -> stage not stated [Cufflinks, HMMER]

### Human cone elongation responses can be explained by photoactivated cone opsin and membrane swelling and osmotic response to phosphate produced by RGS9-catalyzed GTPase. (PNAS 2022)

- DOI: 10.1073/pnas.2202485119 | PMCID: PMC9522364 | PMID: 36122241
- Evidence: Q9NYR8 ) was taken from the AlphaFold predicted structural database ( 85 ).
- Full pipeline: stage not stated [AlphaFold]

### Phosphatidylserine orchestrates Myomerger membrane insertions to drive myoblast fusion. (PNAS 2022)

- DOI: 10.1073/pnas.2202490119 | PMCID: PMC9499509 | PMID: 36095199
- Evidence: Secondary-structure prediction algorithms and AlphaFold structural prediction ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Homologous recombination-deficient mutation cluster in tumor suppressor <i>RAD51C</i> identified by comprehensive analysis of cancer variants. (PNAS 2022)

- DOI: 10.1073/pnas.2202727119 | PMCID: PMC9499524 | PMID: 36099300
- Evidence: We generated models of the BCDX2 and CX3 complexes using AlphaFold2 version 1 ( 36 – 38 ) and evaluated them in the context of our experimental results.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Multistate structures of the MLL1-WRAD complex bound to H2B-ubiquitinated nucleosome. (PNAS 2022)

- DOI: 10.1073/pnas.2205691119 | PMCID: PMC9499523 | PMID: 36095189
- Evidence: There is no high-resolution structural information on the Ash2L IDR, and previously proposed models of this region based on the Ash2L yeast homolog, Bre2 ( 38 ), do not fit our EM map well, nor does a recently reported model generated by AlphaFold2 ( 48 ).
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, RELION v3.0, VMD v1.9.3, cryoDRGN]

### Structural mechanism for bidirectional actin cross-linking by T-plastin. (PNAS 2022)

- DOI: 10.1073/pnas.2205370119 | PMCID: PMC9478642 | PMID: 36067297
- Evidence: This homology model is highly similar to the AlphaFold2 model ( 52 ) (AF- P13797 ; SI Appendix , Fig.
- Full pipeline: structure determination [RELION] -> stage not stated [AlphaFold]

### Comparative genomics of mortal and immortal cnidarians unveils novel keys behind rejuvenation. (PNAS 2022)

- DOI: 10.1073/pnas.2118763119 | PMCID: PMC9459311 | PMID: 36037356
- Version used: **2.1.2**
- Evidence: Structural prediction of POT1 in T. dohrnii and T. rubra was performed, alongside with its wild-type human ortholog POT1 and its variants (G272R and G272N), by using the AlphaFold v.2.1.2 pipeline ( https://github.com/deepmind/alphafold/ ).
- Full pipeline: alignment/mapping [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> stage not stated [AlphaFold v2.1.2, BUSCO, ChimeraX, GSEA, fgsea]

### Identification of mEAK-7 as a human V-ATPase regulator via cryo-EM data mining. (PNAS 2022)

- DOI: 10.1073/pnas.2203742119 | PMCID: PMC9436323 | PMID: 35994636
- Evidence: 1 D and E ), and fitted their structural models predicted by AlphaFold into our density map ( 16 ).
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold] -> stage not stated [Topaz]

### A partnership between the lipid scramblase XK and the lipid transfer protein VPS13A at the plasma membrane. (PNAS 2022)

- DOI: 10.1073/pnas.2205425119 | PMCID: PMC9436381 | PMID: 35994651
- Evidence: AlphaFold-Based Predictions.
- Full pipeline: alignment/mapping [PyMOL] -> stage not stated [AlphaFold]

### Deep learning predicts DNA methylation regulatory variants in the human brain and elucidates the genetics of psychiatric disorders. (PNAS 2022)

- DOI: 10.1073/pnas.2206069119 | PMCID: PMC9407663 | PMID: 35969790
- Evidence: It is also notable that the self-attention mechanism of transformer is a key feature of AlphaFold, a deep learning architecture that has led to a breakthrough in predicting protein structure from sequence ( 27 ).
- Full pipeline: variant calling [SHAPEIT] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [LDSC] -> machine learning [AlphaFold] -> stage not stated [Bismark, GSEA, IMPUTE2, PLINK, R, VEP]

### DYF-5/MAK-dependent phosphorylation promotes ciliary tubulin unloading. (PNAS 2022)

- DOI: 10.1073/pnas.2207134119 | PMCID: PMC9407615 | PMID: 35969738
- Evidence: The structural coordinate of C. elegans IFT-74 was obtained from AlphaFold Protein Structure Database (ID: A0A2C9C2L6), and its N-terminal tubulin-binding region (IFT-74N, residues 1 to 132) was used for analysis.
- Full pipeline: quantification [ImageJ] -> simulation/modelling [GROMACS] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Integrated AlphaFold2 and DEER investigation of the conformational dynamics of a pH-dependent APC antiporter. (PNAS 2022)

- DOI: 10.1073/pnas.2206129119 | PMCID: PMC9407458 | PMID: 35969794
- Version used: **2.0.1**
- Evidence: The structure of GadC was modeled using AlphaFold v.2.0.1 using a modified version of ColabFold ( 64 , 108 ).
- Full pipeline: quantification [ImageJ v1.53] -> structure determination [OpenMM] -> stage not stated [AlphaFold v2.0.1, ColabFold, SciPy]

### Structures of the mannose-6-phosphate pathway enzyme, GlcNAc-1-phosphotransferase. (PNAS 2022)

- DOI: 10.1073/pnas.2203518119 | PMCID: PMC9388126 | PMID: 35939698
- Evidence: The GNPTAB structure was solved by molecular replacement using Phaser ( 70 ) in Phenix ( 71 ), with a search model derived from an AlphaFold2 prediction ( 72 ).
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Coot, PHENIX, PyMOL]

### A multidomain connector links the outer membrane and cell wall in phylogenetically deep-branching bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2203156119 | PMCID: PMC9388160 | PMID: 35943982
- Evidence: A structural model of the periplasmic, homotrimeric segment (residues 20 to 252) of D. radiodurans SlpA was built using an installation of AlphaFold-Multimer v2.2.0 ( 36 ) at the Max Planck Computing and Data Facility in Garching.
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2] -> dimensionality reduction/clustering [MotionCor2] -> structure determination [ChimeraX, Coot, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold]

### PTX3 structure determination using a hybrid cryoelectron microscopy and AlphaFold approach offers insights into ligand binding and complement activation. (PNAS 2022)

- DOI: 10.1073/pnas.2208144119 | PMCID: PMC9388099 | PMID: 35939690
- Evidence: As a starting model, the predicted structure for human PTX3 was downloaded from the AlphaFold Protein Structure Database ( 14 ).
- Full pipeline: structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [AlphaFold, ChimeraX, ColabFold v1.3, RELION v3.1]

### The structure and activities of the archaeal transcription termination factor Eta detail vulnerabilities of the transcription elongation complex. (PNAS 2022)

- DOI: 10.1073/pnas.2207581119 | PMCID: PMC9371683 | PMID: 35917344
- Evidence: AlphaFold ( 56 ) was used to predict a model of Eta that was used as a reference for the model building and refinement.
- Full pipeline: alignment/mapping [BLAST] -> structure determination [AlphaFold] -> stage not stated [PHENIX]

### Mechanistic details of CRISPR-associated transposon recruitment and integration revealed by cryo-EM. (PNAS 2022)

- DOI: 10.1073/pnas.2202590119 | PMCID: PMC9371665 | PMID: 35914146
- Evidence: For the TnsB STC cryo-EM map, the TnsB sequence was used to generate an AlphaFold2 ( 21 ) prediction.
- Full pipeline: alignment/mapping [RELION] -> dimensionality reduction/clustering [RELION] -> differential/statistical testing [RELION] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold, UCSF Chimera]

### Structural insight and characterization of human Twinkle helicase in mitochondrial disease. (PNAS 2022)

- DOI: 10.1073/pnas.2207459119 | PMCID: PMC9371709 | PMID: 35914129
- Evidence: Given that there are no published structures of human Twinkle or homologs, we utilized the AlphaFold software and database ( 20 ) to generate models of both Twinkle W315L (AlphaFold software) and WT (AlphaFold database) as starting models for refinement ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, IMOD] -> stage not stated [PHENIX, PyMOL]

### Noncanonical function of Capicua as a growth termination signal in &lt;i&gt;Drosophila&lt;/i&gt; oogenesis. (PNAS 2022)

- DOI: 10.1073/pnas.2123467119 | PMCID: PMC9351367 | PMID: 35881788
- Evidence: ( C ) Structure of N1 domain from zebrafish Cic-L as predicted by AlphaFold ( 76 ).
- Full pipeline: stage not stated [AlphaFold]

### Accurate prediction of ice nucleation from room temperature water. (PNAS 2022)

- DOI: 10.1073/pnas.2205347119 | PMCID: PMC9351478 | PMID: 35878028
- Evidence: Composite models have been a widespread success in artificial intelligence, with famous recent examples being the AlphaZero ( 66 ) and AlphaFold ( 67 ) models, to name just a few.
- Full pipeline: machine learning [Keras, TensorFlow] -> stage not stated [AlphaFold]

### Root angle is controlled by &lt;i&gt;EGT1&lt;/i&gt; in cereal crops employing an antigravitropic mechanism. (PNAS 2022)

- DOI: 10.1073/pnas.2201350119 | PMCID: PMC9351459 | PMID: 35881796
- Evidence: To understand the structure–function relation of these changes, we constructed the structure of the whole EGT1 protein using de novo prediction from the full protein sequence in AlphaFold2 ( 15 ) ( SI Appendix ).
- Full pipeline: alignment/mapping [BWA v7.12, Cufflinks, HISAT2, HTSeq, SAMtools v1.3] -> stage not stated [AlphaFold, DESeq2, ImageJ, R]

### Shelterin is a dimeric complex with extensive structural heterogeneity. (PNAS 2022)

- DOI: 10.1073/pnas.2201662119 | PMCID: PMC9351484 | PMID: 35881804
- Evidence: AlphaFold-Multimer Modeling.
- Full pipeline: stage not stated [AlphaFold, EMAN2, RELION]

### SARS-CoV-2 impairs interferon production via NSP2-induced repression of mRNA translation. (PNAS 2022)

- DOI: 10.1073/pnas.2204539119 | PMCID: PMC9371684 | PMID: 35878012
- Evidence: This fragment is contained within a singular, long alpha helix region (LHR) (723–919), which is predicted by AlphaFold 2 ( 16 , 29 ).
- Full pipeline: quantification [ImageJ] -> visualisation [ImageJ] -> stage not stated [AlphaFold]

### In situ architecture of the lipid transport protein VPS13C at ER-lysosome membrane contacts. (PNAS 2022)

- DOI: 10.1073/pnas.2203769119 | PMCID: PMC9303930 | PMID: 35858323
- Evidence: Rigid-body fitting of AlphaFold-predicted structure into the averaged density map was done in UCSF ChimeraX_Daily (version 1.4.dev202204302327, https://www.cgl.ucsf.edu/chimerax , RRID:SCR_015872) ( 54 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0] -> structure determination [AlphaFold, ChimeraX, IMOD] -> visualisation [RELION, UCSF Chimera v1.13, seaborn v0.11.2] -> stage not stated [CTFFIND v1.18, EMAN2 v2.91]

### The global succinylation of SARS-CoV-2-infected host cells reveals drug targets. (PNAS 2022)

- DOI: 10.1073/pnas.2123065119 | PMCID: PMC9335334 | PMID: 35858407
- Evidence: Two succinyl lysine sites were highlighted within the crystal structure of SARS-CoV-2 M that was in silico predicted by AlphaFold ( 52 ).
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [R v4.0.4, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### C16orf72/HAPSTR1 is a molecular rheostat in an integrated network of stress response pathways. (PNAS 2022)

- DOI: 10.1073/pnas.2111262119 | PMCID: PMC9271168 | PMID: 35776542
- Evidence: ( I ) Predicted structure of HAPSTR1 as a dimer using AlphaFold2 ( 28 , 29 ).
- Full pipeline: stage not stated [AlphaFold]

### Respiratory complex I with charge symmetry in the membrane arm pumps protons. (PNAS 2022)

- DOI: 10.1073/pnas.2123090119 | PMCID: PMC9271201 | PMID: 35759670
- Version used: **1.1**
- Evidence: A structural model of the holo-complex I from E. coli was generated using AlphaFold 2.1.1 ( 63 ) in multimer mode ( 64 ).
- Full pipeline: stage not stated [AlphaFold v1.1]

### Metal cofactor stabilization by a partner protein is a widespread strategy employed for amidase activation. (PNAS 2022)

- DOI: 10.1073/pnas.2201141119 | PMCID: PMC9245657 | PMID: 35733252
- Evidence: AlphaFold2 models were generated using ColabFold ( 65 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, PHENIX]

### Mapping functional regions of essential bacterial proteins with dominant-negative protein fragments. (PNAS 2022)

- DOI: 10.1073/pnas.2200124119 | PMCID: PMC9245647 | PMID: 35749361
- Evidence: AlphaFold Computational Predictions of Peptide–Protein Complexes.
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [AlphaFold, R]

### Archaeal bundling pili of <i>Pyrobaculum calidifontis</i> reveal similarities between archaeal and bacterial biofilms. (PNAS 2022)

- DOI: 10.1073/pnas.2207037119 | PMCID: PMC9245690 | PMID: 35727984
- Evidence: So, the map hand was initially determined by comparing with the AlphaFold prediction, and later validated by the hand of two tiny α-helices.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Interaction between S4 and the phosphatase domain mediates electrochemical coupling in voltage-sensing phosphatase (VSP). (PNAS 2022)

- DOI: 10.1073/pnas.2200364119 | PMCID: PMC9245683 | PMID: 35733115
- Evidence: ColabFold ( 34 ) is an opensource software for protein structure prediction that combines fast multiple sequence alignment generation with AlphaFold2 ( 59 ).
- Full pipeline: alignment/mapping [AlphaFold] -> differential/statistical testing [R] -> visualisation [PyMOL] -> stage not stated [ColabFold, ImageJ]

### Identification of the <i>Bartonella</i> autotransporter CFA as a protective antigen and hypervariable target of neutralizing antibodies in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202059119 | PMCID: PMC9231624 | PMID: 35714289
- Evidence: Protein-folding predictions using AlphaFold ( 35 ) indicated that the passenger domain of CFA is composed of two β-helices separated by a disordered linker ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### Molecular determinants of inhibition of the human proton channel hHv1 by the designer peptide C6 and a bivalent derivative. (PNAS 2022)

- DOI: 10.1073/pnas.2120750119 | PMCID: PMC9191634 | PMID: 35648818
- Evidence: 6 B ), G199 and I202 are away from the proposed hHv1–C6 binding interface in both our model and the AlphaFold model ( SI Appendix , Fig.
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [AlphaFold, VMD]

### Co-component signal transduction systems: Fast-evolving virulence regulation cassettes discovered in enteric bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2203176119 | PMCID: PMC9214523 | PMID: 35648808
- Evidence: Candidate VtrC-like sequences found in tandem with VtrA-like transmembrane transcription factors were submitted to AlphaFold2 ( 32 ) structure prediction using ColabFold ( 35 ), which replaces the homology detection of AlphaFold2 with MMseqs2 ( 69 ), or with a local adaptation of AlphaFold described three paragraphs below.
- Full pipeline: alignment/mapping [MAFFT, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, HMMER]

### Ancient proteins resolve controversy over the identity of <i>Genyornis</i> eggshell. (PNAS 2022)

- DOI: 10.1073/pnas.2109326119 | PMCID: PMC9995833 | PMID: 35609205
- Evidence: The protein structure of XCA-1 was inferred using the ColabFold AlphaFold2 notebook ( 101 , 102 ) ( SI Appendix , Fig.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, MUSCLE v3.8.31] -> stage not stated [AlphaFold, ColabFold, R v4.1, RAxML v1.0.3, phytools]

### Structural insights into galanin receptor signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2121465119 | PMCID: PMC9173784 | PMID: 35594396
- Evidence: GALR1 and GALR2 predicted by AlphaFold ( 40 ) may represent inactive states, since AlphaFold is biased toward the inactive state of GPCRs ( 41 ) and the predicted structures show characteristic features of the inactive state of GPCRs ( 42 ) such as the ionic lock between R133 3.50 and D132 3.49 of the D 3.49 R 3.50 Y 3.51 motif and the less pronounced outward movement of TM6 compared to the active...
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, R v3.50]

### The distal C terminus of the dihydropyridine receptor β<sub>1a</sub> subunit is essential for tetrad formation in skeletal muscle. (PNAS 2022)

- DOI: 10.1073/pnas.2201136119 | PMCID: PMC9171810 | PMID: 35507876
- Evidence: Within the full-length proteins, AlphaFold2 predicts that β 1a residues V 490 to L 500 are alpha helical, whereas β 1a residues S 501 to M 524 are unstructured, as are all the corresponding residues (S 434 to K 468 ) of β 4 (β 1a : https://alphafold.ebi.ac.uk/entry/P19517 ; β 4 : https://alphafold.ebi.ac.uk/entry/D4A055 ), but the confidence of the predictions for both β 1a and β 4 ranges from low...
- Full pipeline: stage not stated [AlphaFold]

### Matching protein surface structural patches for high-resolution blind peptide docking. (PNAS 2022)

- DOI: 10.1073/pnas.2121153119 | PMCID: PMC9170164 | PMID: 35482919
- Evidence: PatchMAN shows performance superior to current peptide-docking methods, including our recent implementation of AlphaFold2 (AF2) ( 20 ) for peptide docking ( 21 ).
- Full pipeline: stage not stated [AlphaFold]

### Clamping of DNA shuts the condensin neck gate. (PNAS 2022)

- DOI: 10.1073/pnas.2120006119 | PMCID: PMC9168836 | PMID: 35349345
- Evidence: The N- and C-terminal low-resolution regions of Ycs4(26–92 and 1159–1168) were built using ab initio models of S. cerevisiae Ycs4 generated by AlphaFold2 (https://alphafold.ebi.ac.uk/entry/ Q06156 ) as a template ( 46 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, PyMOL v2.5, RELION v3.1, UCSF Chimera]

### An allosteric HTRA1-calpain 2 complex with restricted activation profile. (PNAS 2022)

- DOI: 10.1073/pnas.2113520119 | PMCID: PMC9168489 | PMID: 35349341
- Evidence: The structure predicted by AlphaFold for human HTRA1 was used after removing the N-terminal domain.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> simulation/modelling [NAMD v2.9] -> stage not stated [AlphaFold, AutoDock Vina]

### A mixed-valent Fe(II)Fe(III) species converts cysteine to an oxazolone/thioamide pair in methanobactin biosynthesis. (PNAS 2022)

- DOI: 10.1073/pnas.2123566119 | PMCID: PMC9060507 | PMID: 35320042
- Evidence: The interaction with MbnA was modeled using the newly accessible advanced version of ColabFold ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/beta/AlphaFold2_advanced.ipynb ) with the following parameters: MbnABC oligomeric ratio of 1:1:1; msa_method jackhmmer; msa_format fas; pair_mode unpaired+paired; pair_cov 50; pair_qid 20; rank_by pTMscore; use_turbo unchecked; num_...
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold, ColabFold, PHENIX]

### A conserved mechanism affecting hydride shifting and deprotonation in the synthesis of hopane triterpenes as compositions of wax in oat. (PNAS 2022)

- DOI: 10.1073/pnas.2118709119 | PMCID: PMC8944845 | PMID: 35290128
- Evidence: Three-dimensional models of the AsHS1, AsHS2, and AcHS1 proteins were generated by modeling with the HsLAS (Protein Data Bank ID: 1w6k/1w6j) template using SWISS-MODEL software ( 21 , 41 ) and also by AlphaFold2 ( 42 ).
- Full pipeline: alignment/mapping [MUSCLE] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [PyMOL]

### The C terminus of the mycobacterium ESX-1 secretion system substrate ESAT-6 is required for phagosomal membrane damage and virulence. (PNAS 2022)

- DOI: 10.1073/pnas.2122161119 | PMCID: PMC8931374 | PMID: 35271388
- Evidence: ( B and C ) Structure of ESAT-6 alone with methionine residues 83 and 93 highlighted, as determined experimentally by NMR ( B ) or by the predicted model using AlphaFold2 ( C ).
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### Engineered nanoparticles enable deep proteomics studies at scale by leveraging tunable nano-bio interactions. (PNAS 2022)

- DOI: 10.1073/pnas.2106053119 | PMCID: PMC8931255 | PMID: 35275789
- Evidence: Recent work on protein structure and surface property prediction such as molecular surface interaction fingerprinting ( 37 ) and AlphaFold ( 38 ) also presents an intriguing opportunity to identify and understand physicochemical protein properties that drive specific nano–bio interactions.
- Full pipeline: quantification [lme4] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [R, igraph, lme4] -> machine learning [lme4] -> visualisation [ComplexHeatmap] -> stage not stated [AlphaFold]

### A SURF4-to-proteoglycan relay mechanism that mediates the sorting and secretion of a tagged variant of sonic hedgehog. (PNAS 2022)

- DOI: 10.1073/pnas.2113991119 | PMCID: PMC8931250 | PMID: 35271396
- Evidence: ( E ) The structure of SURF4 predicted by AlphaFold.
- Full pipeline: stage not stated [AlphaFold]

### FliL ring enhances the function of periplasmic flagella. (PNAS 2022)

- DOI: 10.1073/pnas.2117245119 | PMCID: PMC8931381 | PMID: 35254893
- Evidence: Guided by the cryo-ET maps, the orientations of the MotB domains were corrected through the flexible loops predicted by AlphaFold2.
- Full pipeline: alignment/mapping [CTFFIND, IMOD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold]

### KARRIKIN UP-REGULATED F-BOX 1 (KUF1) imposes negative feedback regulation of karrikin and KAI2 ligand metabolism in <i>Arabidopsis thaliana</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2112820119 | PMCID: PMC8931227 | PMID: 35254909
- Evidence: However, a de novo structural prediction by AlphaFold indicates that KUF1 may have a six-bladed rather than five-bladed β-propeller structure ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### Dual-function Spot 42 RNA encodes a 15-amino acid protein that regulates the CRP transcription factor. (PNAS 2022)

- DOI: 10.1073/pnas.2119866119 | PMCID: PMC8916003 | PMID: 35239441
- Evidence: Intriguingly, in a CRP–SpfP structure predicted with AlphaFold-Multimer ( 30 ), SpfP binds near the L51, L62, and S84 residues ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### Mitochondrial COA7 is a heme-binding protein with disulfide reductase activity, which acts in the early stages of complex IV assembly. (PNAS 2022)

- DOI: 10.1073/pnas.2110357119 | PMCID: PMC8892353 | PMID: 35210360
- Evidence: The position of the disulfide bonds as determined by crystallography is consistent with that proposed for the previously published model of COA7 ( 15 ) and with that predicted using AlphaFold ( 39 ).
- Full pipeline: stage not stated [AlphaFold]

### Amino acid sensor conserved from bacteria to humans. (PNAS 2022)

- DOI: 10.1073/pnas.2110415119 | PMCID: PMC8915833 | PMID: 35238638
- Evidence: To demonstrate that the motif is capable of binding amino acids and their derivatives in invertebrates, we have run docking experiments using the α2δ-protein structure from Drosophila melanogaster modeled by AlphaFold ( 37 ), amino acid ligands, and their derivatives.
- Full pipeline: stage not stated [AlphaFold, AutoDock Vina, HMMER, MAFFT, MrBayes]

### Researchers turn to deep learning to decode protein structures. (PNAS 2022)

- DOI: 10.1073/pnas.2202107119 | PMCID: PMC8916015 | PMID: 35235461
- Evidence: AlphaFold uses AI to predict the shapes of proteins; structural biologists are using the program to deepen our understanding of the big molecules.
- Full pipeline: machine learning [RoseTTAFold] -> stage not stated [AlphaFold]

### Munc13 structural transitions and oligomers that may choreograph successive stages in vesicle priming for neurotransmitter release. (PNAS 2022)

- DOI: 10.1073/pnas.2121259119 | PMCID: PMC8851502 | PMID: 35135883
- Evidence: Atomic models in D and E (ribbon diagrams) were obtained by modeling of the AlphaFold predicted Munc13C structure into the ∼10 Å 3D maps ( Materials and Methods ).
- Full pipeline: stage not stated [AlphaFold, RELION v3.1]

### A noncanonical cytochrome <i>c</i> stimulates calcium binding by PilY1 for type IVa pili formation. (PNAS 2022)

- DOI: 10.1073/pnas.2115061119 | PMCID: PMC8833165 | PMID: 35121662
- Evidence: In an AlphaFold2 model together with ligand prediction using COACH ( SI Appendix , SI Materials and Methods ), this part of Mxan_0363 adopts a cytochrome c -like fold ( 36 ) that can readily be superimposed on the determined 1.5-Å structure (PDB 2B4Z) of Bos taurus cytochrome c ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### A hyperpromiscuous antitoxin protein domain for the neutralization of diverse toxin domains. (PNAS 2022)

- DOI: 10.1073/pnas.2102212119 | PMCID: PMC8832971 | PMID: 35121656
- Evidence: Additional structural prediction was carried out for PanA Vib. har. with the AlphaFold2 ( 46 ) Colab notebook with default settings (“advanced” version; https://github.com/sokrypton/ColabFold ).
- Full pipeline: alignment/mapping [PyMOL v2.4.2] -> stage not stated [AlphaFold, ColabFold]

### Fungal gasdermin-like proteins are controlled by proteolytic cleavage. (PNAS 2022)

- DOI: 10.1073/pnas.2109418119 | PMCID: PMC8851545 | PMID: 35135876
- Evidence: The HET-Q1 protein was also modeled with AlphaFold2 ( 28 ).
- Full pipeline: stage not stated [AlphaFold]

### Soluble TREM2 inhibits secondary nucleation of Aβ fibrillization and enhances cellular uptake of fibrillar Aβ. (PNAS 2022)

- DOI: 10.1073/pnas.2114486119 | PMCID: PMC8812518 | PMID: 35082148
- Evidence: Given that many studies are conducted using mouse models and mouse TREM2, we also examined the surfaces of mouse TREM2, using AlphaFold ( 68 ) to create a molecular model ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Requirement of Xk and Vps13a for the P2X7-mediated phospholipid scrambling and cell lysis in mouse T cells. (PNAS 2022)

- DOI: 10.1073/pnas.2119286119 | PMCID: PMC8851519 | PMID: 35140185
- Evidence: 7 A ), its tertiary structure predicted by AlphaFold2 ( 50 ) is very similar to that of human XKR8 ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### Domoic acid biosynthesis in the red alga <i>Chondria armata</i> suggests a complex evolutionary history for toxin production. (PNAS 2022)

- DOI: 10.1073/pnas.2117407119 | PMCID: PMC8833176 | PMID: 35110408
- Evidence: ( B ) AlphaFold2 predicted models for RadC1, DabC, and KabC.
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [AlphaFold, BLAST, BUSCO v4.0.5]

### Sex-specific splicing of Z- and W-borne <i>nr5a1</i> alleles suggests sex determination is controlled by chromosome conformation. (PNAS 2022)

- DOI: 10.1073/pnas.2116475119 | PMCID: PMC8795496 | PMID: 35074916
- Evidence: The three-dimensional structure of the putative translated protein of nr5a1 cDNA variants was predicted with AlphaFold ( 66 ).
- Full pipeline: alignment/mapping [BWA, Clustal Omega] -> quantification [DESeq2 v1.26.0] -> dimensionality reduction/clustering [AlphaFold] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [R, kallisto]

### Ultrafast end-to-end protein structure prediction enables high-throughput exploration of uncharacterized proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2113348119 | PMCID: PMC8795500 | PMID: 35074909
- Evidence: We note that a similar strategy also proved effective in AlphaFold2.
- Full pipeline: stage not stated [AlphaFold, HMMER, PyTorch, RoseTTAFold]

### Darwinian genomics and diversity in the tree of life. (PNAS 2022)

- DOI: 10.1073/pnas.2115644119 | PMCID: PMC8795533 | PMID: 35042807
- Evidence: To make protein structure prediction more accurate and efficient, AlphaFold’s neural network-based algorithm predicts energy landscapes rather than calculating binary contact maps ( 21 , 74 ).
- Full pipeline: machine learning [AlphaFold]

### Atomic structure of Lanreotide nanotubes revealed by cryo-EM. (PNAS 2022)

- DOI: 10.1073/pnas.2120346119 | PMCID: PMC8794822 | PMID: 35042822
- Evidence: The recent success of AlphaFold ( 19 ) in predicting protein tertiary structure has depended greatly on the huge database of experimentally determined protein structures.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold]

### Identification of a muropeptide precursor transporter from gut microbiota and its role in preventing intestinal inflammation. (PNAS 2023)

- DOI: 10.1073/pnas.2306863120 | PMCID: PMC10756304 | PMID: 38127978
- Evidence: AlphaFold and SWISS Model Structure Comparaison.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.3, ColabFold, Jupyter]

### Endocannabinoid biosynthetic enzymes regulate pain response via LKB1-AMPK signaling. (PNAS 2023)

- DOI: 10.1073/pnas.2304900120 | PMCID: PMC10756258 | PMID: 38109529
- Evidence: The AlphaFold structure of DAGLβ is shown (AF- Q91WC9 -F1).
- Full pipeline: stage not stated [AlphaFold]

### Structural and physical features that distinguish tumor-controlling from inactive cancer neoepitopes. (PNAS 2023)

- DOI: 10.1073/pnas.2312057120 | PMCID: PMC10742377 | PMID: 38085776
- Evidence: PANDORA is built upon the widely used protein modeling package MODELLER ( 50 , 51 ), whereas TFold is built on the recent and impactful AlphaFold structure prediction tool ( 52 , 53 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL v2.5] -> stage not stated [AlphaFold]

### Structural and thermodynamic framework for PIEZO1 modulation by small molecules. (PNAS 2023)

- DOI: 10.1073/pnas.2310933120 | PMCID: PMC10723123 | PMID: 38060566
- Evidence: Based on these criteria, we examined a partial high-resolution cryo-EM mPIEZO1 structure (PDB ID:6b3r) ( 5 ) as well as the full-length PIEZO1 structural model predicted by AlphaFold2 ( 32 ) to seek possible candidate residues located in extracellularly accessible positions in repeats A and B.
- Full pipeline: alignment/mapping [NAMD] -> simulation/modelling [GROMACS v2016.4, NAMD] -> stage not stated [AlphaFold, AutoDock Vina]

### CD5L is a canonical component of circulatory IgM. (PNAS 2023)

- DOI: 10.1073/pnas.2311265120 | PMCID: PMC10723121 | PMID: 38055740
- Evidence: AlphaFold2 model of CD5L and J-chain was fitted into the structure of IgM core/Fc region with J-chain (PDB: 8ADY).
- Full pipeline: stage not stated [AlphaFold]

### ALPK1 mutants causing ROSAH syndrome or Spiradenoma are activated by human nucleotide sugars. (PNAS 2023)

- DOI: 10.1073/pnas.2313148120 | PMCID: PMC10723048 | PMID: 38060563
- Evidence: Structural predictions using AlphaFold2 ( 27 ) suggest that the catalytic kinase domain interacts with the ADP-heptose binding domain ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### A suppressor screen &lt;i&gt;in C. elegans&lt;/i&gt; identifies a multiprotein interaction that stabilizes the synaptonemal complex. (PNAS 2023)

- DOI: 10.1073/pnas.2314335120 | PMCID: PMC10723054 | PMID: 38055743
- Evidence: Our attempts to model a docking interface between the regions surrounding the mutations using AlphaFold did not yield a high-confidence interface.
- Full pipeline: alignment/mapping [BWA, GATK] -> stage not stated [AlphaFold, SnpEff]

### Structures of the &lt;i&gt;P. aeruginosa&lt;/i&gt; FleQ-FleN master regulators reveal large-scale conformational switching in motility and biofilm control. (PNAS 2023)

- DOI: 10.1073/pnas.2312276120 | PMCID: PMC10723142 | PMID: 38051770
- Evidence: A model for the FleQ HTH motif (residues 431 to 490) was extracted from the AlphaFold ( 31 ) structure prediction for full-length FleQ and input as search model against the PDB database in the DALI protein structure comparison server ( 32 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, MotionCor2]

### Alternative splicing events as peripheral biomarkers for motor learning deficit caused by adverse prenatal environments. (PNAS 2023)

- DOI: 10.1073/pnas.2304074120 | PMCID: PMC10723155 | PMID: 38051767
- Evidence: The AlphaFold2 predicted protein structures of the long and short isoforms of Mtpap, Ets1, Tvp23b, Celf2 and Rasa1 respectively, as annotated in Fig.
- Full pipeline: alignment/mapping [HISAT2, HTSeq, featureCounts] -> stage not stated [AlphaFold, Keras, NumPy, TensorFlow, edgeR v3.24.3]

### Bimodular architecture of bacterial effector SAP05 that drives ubiquitin-independent targeted protein degradation. (PNAS 2023)

- DOI: 10.1073/pnas.2310664120 | PMCID: PMC10710061 | PMID: 38039272
- Evidence: Structural predictions for protein complexes were conducted with AlphaFold2 ( 58 ) and AlphaFold-Multimer v3 ( 35 ).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [AlphaFold]

### In silico evolution of autoinhibitory domains for a PD-L1 antagonist using deep learning models. (PNAS 2023)

- DOI: 10.1073/pnas.2307371120 | PMCID: PMC10710080 | PMID: 38032933
- Evidence: AlphaFold2 (AF2).
- Full pipeline: stage not stated [AlphaFold, PyMOL, Python v3.8, RoseTTAFold]

### An acetyltranferase moonlights as a regulator of the RNA binding repertoire of the RNA chaperone Hfq in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2311509120 | PMCID: PMC10710024 | PMID: 38011569
- Evidence: We used AlphaFold-Multimer ( 36 ) to predict the structure of the HqbA-Hfq 6 complex.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [ImageJ] -> stage not stated [AlphaFold, UCSF Chimera]

### Tad and toxin-coregulated pilus structures reveal unexpected diversity in bacterial type IV pili. (PNAS 2023)

- DOI: 10.1073/pnas.2316668120 | PMCID: PMC10710030 | PMID: 38011558
- Evidence: The C. crescentus tad pilin structure (Uniport Id: WP_010920785 ) predicted by AlphaFold ( 50 ), and crystal structure of V. cholerae TCP (PDB id: 1OQV) were used as initial models for rigid-body-fitting in the respective maps.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### A Novel mechanism of herbicide action through disruption of pyrimidine biosynthesis. (PNAS 2023)

- DOI: 10.1073/pnas.2313197120 | PMCID: PMC10691210 | PMID: 37988466
- Evidence: Based on an AlphaFold model of the At DHODH enzyme ( 27 ) that aligns closely with our internally determined rice structure, A141 maps onto an FMN-adjacent loop region ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [AlphaFold, SAMtools] -> stage not stated [PHENIX]

### Diversity, evolution, and classification of the RNA-guided nucleases TnpB and Cas12. (PNAS 2023)

- DOI: 10.1073/pnas.2308224120 | PMCID: PMC10691335 | PMID: 37983496
- Evidence: Protein structure models were constructed using AlphaFold2 implemented under CollabFold ( 61 , 62 ).
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> stage not stated [AlphaFold]

### Glutamine-rich regions of the disordered CREB transactivation domain mediate dynamic intra- and intermolecular interactions. (PNAS 2023)

- DOI: 10.1073/pnas.2313835120 | PMCID: PMC10666024 | PMID: 37971402
- Evidence: Transient population of these structures is supported by analysis of chemical shifts and PRE intensities and AlphaFold structure predictions.
- Full pipeline: stage not stated [AlphaFold]

### In vivo selection of synthetic nucleocapsids for tissue targeting. (PNAS 2023)

- DOI: 10.1073/pnas.2306129120 | PMCID: PMC10655225 | PMID: 37939083
- Evidence: Although some of the eight selected miniproteins have homologous sequences, AlphaFold2 predictions revealed unique 3D conformations, surface hydrophobic networks, and surface charge distributions ( Figs.
- Full pipeline: alignment/mapping [Python] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, ColabFold]

### Structure and function of the &lt;i&gt;S. pombe&lt;/i&gt; III-IV-cyt &lt;i&gt;c&lt;/i&gt; supercomplex. (PNAS 2023)

- DOI: 10.1073/pnas.2307697120 | PMCID: PMC10655221 | PMID: 37939086
- Evidence: Starting models of CIII subunits were generated from the AlphaFold Protein Structure Database ( 88 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### FAB1C, a phosphatidylinositol 3-phosphate 5-kinase, interacts with PIN-FORMEDs and modulates their lytic trafficking in Arabidopsis. (PNAS 2023)

- DOI: 10.1073/pnas.2310126120 | PMCID: PMC10655590 | PMID: 37934824
- Evidence: The AlphaFold-predicted model of the PD region did not represent a distinctive three-dimensional structure, indicative of certain flexibility in protein interactions ( SI Appendix , Fig.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [AlphaFold]

### AMP-dependent phosphite dehydrogenase, a phosphorylating enzyme in dissimilatory phosphite oxidation. (PNAS 2023)

- DOI: 10.1073/pnas.2309743120 | PMCID: PMC10636320 | PMID: 37922328
- Evidence: ( B ) Pf APD AlphaFold model.
- Full pipeline: stage not stated [AlphaFold, UCSF Chimera]

### FAM91A1-TBC1D23 complex structure reveals human genetic variations susceptible for PCH. (PNAS 2023)

- DOI: 10.1073/pnas.2309910120 | PMCID: PMC10636324 | PMID: 37903274
- Evidence: The complex structure was solved by molecular replacement using the FAM91A1 N AlphaFold2 model and refined to a resolution of 2.51 Å ( SI Appendix , Fig.
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [ImageJ]

### Cytosolic iron-sulfur protein assembly system identifies clients by a C-terminal tripeptide. (PNAS 2023)

- DOI: 10.1073/pnas.2311057120 | PMCID: PMC10623007 | PMID: 37883440
- Evidence: Protein structures are AlphaFold models.
- Full pipeline: stage not stated [AlphaFold]

### Systematic identification of conditionally folded intrinsically disordered regions by AlphaFold2. (PNAS 2023)

- DOI: 10.1073/pnas.2304302120 | PMCID: PMC10622901 | PMID: 37878721
- Evidence: Two deep learning-based methods, AlphaFold2 ( 3 ) and RoseTTAFold ( 4 ), have recently enabled protein structure prediction with high accuracy ( 5 ).
- Full pipeline: machine learning [AlphaFold, RoseTTAFold] -> stage not stated [Jupyter]

### Intracellular <i>Plasmodium</i> aquaporin 2 is important for sporozoite production in the mosquito vector and malaria transmission. (PNAS 2023)

- DOI: 10.1073/pnas.2304339120 | PMCID: PMC10622946 | PMID: 37883438
- Evidence: Prediction of Tertiary Structures Using AlphaFold.
- Full pipeline: alignment/mapping [ColabFold] -> stage not stated [AlphaFold]

### An amino-domino model described by a cross-peptide-bond Ramachandran plot defines amino acid pairs as local structural units. (PNAS 2023)

- DOI: 10.1073/pnas.2301064120 | PMCID: PMC10623034 | PMID: 37878722
- Evidence: For each amino acid pair, corresponding dihedral angles (ψ k , φ k +1 ) were extracted from AlphaFold-predicted structures and assigned the nearest (in the sense of the flat torus distance) of the 20 cluster labels from Fig.
- Full pipeline: dimensionality reduction/clustering [AlphaFold, scikit-learn] -> simulation/modelling [GROMACS]

### Heterologous synthesis of the complex homometallic cores of nitrogenase P- and M-clusters in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2314788120 | PMCID: PMC10622910 | PMID: 37871225
- Evidence: With respect to NifZ, a high-confidence structural model generated with AlphaFold reveals a pseudodimeric architecture of this protein, with a small B-barrel present in each monomeric half ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Diversity of rhodopsin cyclases in zoospore-forming fungi. (PNAS 2023)

- DOI: 10.1073/pnas.2310600120 | PMCID: PMC10622942 | PMID: 37871207
- Evidence: The initial structure of heterodimeric RgRGC1/RgNeoR was modeled using AlphaFold-Multimer ( 28 ) ( SI Appendix , Fig.
- Full pipeline: read trimming [IQ-TREE, SPAdes v3.15.5] -> alignment/mapping [IQ-TREE] -> simulation/modelling [GROMACS v2019.3] -> visualisation [Matplotlib v3.4.3, PyMOL v2.4.1] -> stage not stated [AlphaFold, MDAnalysis v2.4.3]

### Molecular mechanisms controlling the biogenesis of the TGF-β signal Vg1. (PNAS 2023)

- DOI: 10.1073/pnas.2307203120 | PMCID: PMC10614602 | PMID: 37844219
- Evidence: To determine whether these residues are accessible at the surface, we used AlphaFold2 ( 44 ) (there is no biophysically determined Vg1 structure).
- Full pipeline: stage not stated [AlphaFold, Fiji, ImageJ]

### Molecular basis for C-degron recognition by CRL2&lt;sup&gt;APPBP2&lt;/sup&gt; ubiquitin ligase. (PNAS 2023)

- DOI: 10.1073/pnas.2308870120 | PMCID: PMC10614623 | PMID: 37844242
- Evidence: The atomic models of the human CUL2 N-terminal fragment, EB, EC, and APPBP2 were predicted using AlphaFold2 ( 38 ).
- Full pipeline: structure determination [Coot] -> stage not stated [AlphaFold, ChimeraX, PHENIX, PyMOL]

### Co-option of a conserved host glutamine transporter facilitates aphid/&lt;i&gt;Buchnera&lt;/i&gt; metabolic integration. (PNAS 2023)

- DOI: 10.1073/pnas.2308448120 | PMCID: PMC10614625 | PMID: 37844224
- Evidence: Structural homology models were constructed using HHPred and Modeller as previously described ( 12 , 37 ) or AlphaFold ( 58 ).
- Full pipeline: stage not stated [AlphaFold]

### Phage display uncovers a sequence motif that drives polypeptide binding to a conserved regulatory exosite of O-GlcNAc transferase. (PNAS 2023)

- DOI: 10.1073/pnas.2303690120 | PMCID: PMC10589721 | PMID: 37819980
- Evidence: ( C – F ) Comparisons of the human OGT ( Hs OGT) structure against structures and AlphaFold models of OGT homologs.
- Full pipeline: simulation/modelling [PHENIX] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Polyubiquitin ligand-induced phase transitions are optimized by spacing between ubiquitin units. (PNAS 2023)

- DOI: 10.1073/pnas.2306638120 | PMCID: PMC10589717 | PMID: 37824531
- Evidence: Representative structures of these HT6-Ub constructs were determined by refining AlphaFold-predicted starting structures ( 33 ) against our scattering data using conformational ensembles constructed with SASSIE ( 34 ) ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### Amine-recognizing domain in diverse receptors from bacteria and archaea evolved from the universal amino acid sensor. (PNAS 2023)

- DOI: 10.1073/pnas.2305837120 | PMCID: PMC10589655 | PMID: 37819981
- Evidence: Protein structures of the target proteins were modeled using AlphaFold 2 ( 68 ).
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> differential/statistical testing [MrBayes] -> stage not stated [AlphaFold, AutoDock Vina, Open Babel, PyMOL]

### Sequence-independent activity of a predicted long disordered segment of the human papillomavirus type 16 L2 capsid protein during virus entry. (PNAS 2023)

- DOI: 10.1073/pnas.2307721120 | PMCID: PMC10589650 | PMID: 37819982
- Evidence: Structures of the L2 protein were predicted using AF2 or RoseTTAFold, and structure of the L2 peptide/retromer/SNX3 complex was predicted with AlphaFold Multimer.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, RoseTTAFold]

### A non-pheromone GPCR is essential for meiosis and ascosporogenesis in the wheat scab fungus. (PNAS 2023)

- DOI: 10.1073/pnas.2313034120 | PMCID: PMC10589705 | PMID: 37812726
- Evidence: ( F ) Tertiary structures of Gia1, FvGia1 of F. verticillioides , and Gpr-1 of N. crassa predicted with AlphaFold v2 and visualized using the UCSF Chimera tool.
- Full pipeline: visualisation [AlphaFold, UCSF Chimera]

### The inhibitory mechanism of a small protein reveals its role in antimicrobial peptide sensing. (PNAS 2023)

- DOI: 10.1073/pnas.2309607120 | PMCID: PMC10576120 | PMID: 37792514
- Evidence: The PhoQ/MgrB complex was modeled using AlphaFold2 multimer on Colab [PMID: 35637307].
- Full pipeline: quantification [ImageJ] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold]

### Bacterial SEAL domains undergo autoproteolysis and function in regulated intramembrane proteolysis. (PNAS 2023)

- DOI: 10.1073/pnas.2310862120 | PMCID: PMC10556640 | PMID: 37756332
- Evidence: An AlphaFold2 model of RsgI GGG was used for molecular replacement to determine phase information and an initial map was determined using the Phaser program in Phenix v1.20.1 ( 56 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot] -> stage not stated [AlphaFold, ColabFold, PHENIX v1.20.1]

### DAT, deacylating autotransporter toxin, from <i>Bordetella parapertussis</i> demyristoylates Gα<sub>i</sub> GTPases and contributes to cough. (PNAS 2023)

- DOI: 10.1073/pnas.2308260120 | PMCID: PMC10556565 | PMID: 37748060
- Evidence: Indeed, the AlphaFold2 program predicted structures of the DAT passenger domain consisting of elongated β helices, in which no catalytic triad-like structure was found near the GDSL motif with a catalytic residue Ser571 ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Structure of the <i>bc</i><sub>1</sub>-<i>cbb</i><sub>3</sub> respiratory supercomplex from <i>Pseudomonas aeruginosa</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2307093120 | PMCID: PMC10556555 | PMID: 37751552
- Evidence: Starting atomic models were taken from the AlphaFold Protein Structure Database ( 43 ).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold, PHENIX v1.20.1, UCSF Chimera]

### The secret to a successful career in science-according to Magritte. (PNAS 2023)

- DOI: 10.1073/pnas.2304819120 | PMCID: PMC10523505 | PMID: 37732754
- Evidence: The recipients of this year’s Award are Demis Hassabis and John Jumper (Google DeepMind, London) for their invention of AlphaFold.
- Full pipeline: stage not stated [AlphaFold]

### Starting at Go: Protein structure prediction succumbs to machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2311128120 | PMCID: PMC10523586 | PMID: 37732752
- Evidence: These ideas are incorporated into the Multiple Sequence Alignments (MSAs) of homologous proteins that are now key to all predictive algorithms, including AlphaFold.
- Full pipeline: alignment/mapping [AlphaFold]

### A CUG-initiated CATSPERθ functions in the CatSper channel assembly and serves as a checkpoint for flagellar trafficking. (PNAS 2023)

- DOI: 10.1073/pnas.2304409120 | PMCID: PMC10523455 | PMID: 37725640
- Evidence: We compared the structure of the CTG-ORF (opening reading frame) and ATG-ORF encoded CATSPERθ predicted by AlphaFold ( 32 ) ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### An antioxidant feedforward cycle coordinated by linker histone variant H1.2 and NRF2 that drives nonsmall cell lung cancer progression. (PNAS 2023)

- DOI: 10.1073/pnas.2306288120 | PMCID: PMC10523483 | PMID: 37729198
- Evidence: Next, we analyzed possible interaction sites between H1.2 and NRF2 with AlphaFold2, which predicts protein–protein complex with high fidelity ( 36 ).
- Full pipeline: stage not stated [AlphaFold]

### A peptide-binding domain shared with an Antarctic bacterium facilitates <i>Vibrio cholerae</i> human cell binding and intestinal colonization. (PNAS 2023)

- DOI: 10.1073/pnas.2308238120 | PMCID: PMC10523503 | PMID: 37729203
- Evidence: ( B ) AlphaFold prediction of the structure of the FrhA ligand binding region.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### Combined prediction and design reveals the target recognition mechanism of an intrinsically disordered protein interaction domain. (PNAS 2023)

- DOI: 10.1073/pnas.2305603120 | PMCID: PMC10523638 | PMID: 37722056
- Evidence: Another approach is to computationally predict possible complex structures by employing conformation sampling techniques like molecular dynamics (MD) simulation ( 9 , 19 – 21 ) or utilizing machine learning-based structure prediction methods like AlphaFold2 (AF2) ( 22 , 23 ).
- Full pipeline: simulation/modelling [AlphaFold, GROMACS] -> stage not stated [PHENIX]

### <i>Iditarod</i>, a <i>Drosophila</i> homolog of the Irisin precursor <i>FNDC5</i>, is critical for exercise performance and cardiac autophagy. (PNAS 2023)

- DOI: 10.1073/pnas.2220556120 | PMCID: PMC10523451 | PMID: 37722048
- Evidence: Structural Prediction and Analyses using AlphaFold and RoseTTAFold.
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [PyMOL] -> stage not stated [AlphaFold, RoseTTAFold]

### Cryo-EM structure determination of small therapeutic protein targets at 3 Å-resolution using a rigid imaging scaffold. (PNAS 2023)

- DOI: 10.1073/pnas.2305494120 | PMCID: PMC10500258 | PMID: 37669364
- Evidence: Given the important interplay between protein sequence design and protein structure prediction, we considered whether a leading machine learning algorithm, AlphaFold2 ( 55 ), would correctly predict the structure of our designed scaffold based on amino acid sequence.
- Full pipeline: structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### PtdSer as a signaling lipid determined by privileged localization of ORP5 and ORP8 at ER/PM junctional foci to determine PM and ER PtdSer/PI(4)P ratio and cell function. (PNAS 2023)

- DOI: 10.1073/pnas.2301410120 | PMCID: PMC10469337 | PMID: 37607230
- Evidence: The AlphaFold prediction of the ORD8 structure, the ORD8 surface charge, and the position of the mutated residues are shown in SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Specific inhibition of an anticancer target, polo-like kinase 1, by allosterically dismantling its mechanism of substrate recognition. (PNAS 2023)

- DOI: 10.1073/pnas.2305037120 | PMCID: PMC10629583 | PMID: 37603740
- Evidence: Overlaid structures of apo-PBD1 with that of apo-PBD2 ( 52 , 53 ) and apo-PBD3 (AlphaFold Protein Structure database, https://alphafold.ebi.ac.uk ) revealed that their overall folds are similar, with all showing a flexible L2 loop around the Allopole-A-binding pocket ( Fig.
- Full pipeline: normalisation [CCP4] -> simulation/modelling [GROMACS v2022.3, RDKit, VMD v1.9.4] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL, VMD v1.9.4] -> stage not stated [AlphaFold]

### Two conformations of the Tom20 preprotein receptor in the TOM holo complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301447120 | PMCID: PMC10450662 | PMID: 37579144
- Evidence: Atomic model building of the TOM core complex was based on the AlphaFold-Multimer ( 54 ) prediction of the core dimer, then fitted into the refined map using Coot ( 55 ) and ISOLDE ( 56 ) within UCSF ChimeraX.
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, ChimeraX, MotionCor2, RELION]

### Folding stabilities of ribosome-bound nascent polypeptides probed by mass spectrometry. (PNAS 2023)

- DOI: 10.1073/pnas.2303167120 | PMCID: PMC10438377 | PMID: 37552756
- Evidence: SASA values for E. coli were computed using structures available from the AlphaFold Protein Structure Database using AlphaFold2 ( 57 ).
- Full pipeline: stage not stated [AlphaFold]

### The structural basis of hyperpromiscuity in a core combinatorial network of type II toxin-antitoxin and related phage defense systems. (PNAS 2023)

- DOI: 10.1073/pnas.2305393120 | PMCID: PMC10440598 | PMID: 37556498
- Evidence: We have structurally annotated our network of TA-like two-gene architectures through high-throughput prediction of TA complex structures using AlphaFold2 ( 26 ) implemented in the FoldDock pipeline ( 27 ).
- Full pipeline: visualisation [Cytoscape v3.5.0] -> stage not stated [AlphaFold, Python]

### Analysis of the complex between MBD2 and the histone deacetylase core of NuRD reveals key interactions critical for gene silencing. (PNAS 2023)

- DOI: 10.1073/pnas.2307287120 | PMCID: PMC10433457 | PMID: 37552759
- Evidence: AlphaFold2 Model Generation.
- Full pipeline: visualisation [ChimeraX v1.15] -> stage not stated [AlphaFold]

### Insight into the mechanism of H&lt;sup&gt;+&lt;/sup&gt;-coupled nucleobase transport. (PNAS 2023)

- DOI: 10.1073/pnas.2302799120 | PMCID: PMC10438392 | PMID: 37549264
- Evidence: Molecular replacement using the core domain of either the AlphaFold2 prediction or UraA (PDB ID 5XLS) as a search model led to a solution for the initial phase, which was improved by iterations of modeling building in COOT ( 32 ) and refinement in PHENIX ( 33 ).
- Full pipeline: structure determination [AlphaFold, PHENIX]

### Structural polymorphisms within a common powdery mildew effector scaffold as a driver of coevolution with cereal immune receptors. (PNAS 2023)

- DOI: 10.1073/pnas.2307604120 | PMCID: PMC10410722 | PMID: 37523523
- Evidence: Genome-wide AlphaFold2 (AF2) modeling of fungal effectors complements identified extreme expansion of lineage-specific, sequence-unrelated, structurally similar effector families in B. graminis and the rust fungus Puccinia graminis ( 26 ).
- Full pipeline: alignment/mapping [MUSCLE] -> visualisation [ChimeraX v1.3] -> stage not stated [AlphaFold, PHENIX]

### Structural basis for binding of <i>Drosophila</i> Smaug to the GPCR Smoothened and to the germline inducer Oskar. (PNAS 2023)

- DOI: 10.1073/pnas.2304385120 | PMCID: PMC10410706 | PMID: 37523566
- Evidence: For the AlphaFold2 predictions, the ColabFold v1.5.2 web interface ( 60 ) was used with standard settings except for the model_type, which was switched from “auto” to “alphaFold2_multimer_v3”.
- Full pipeline: structure determination [PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold v1.5.2, PHENIX]

### The transformative power of transformers in protein structure prediction. (PNAS 2023)

- DOI: 10.1073/pnas.2303499120 | PMCID: PMC10410766 | PMID: 37523536
- Evidence: We obtained the sequences of these target proteins from the CASP15 website and predicted their structures using publicly-available versions of AlphaFold2, RoseTTAFold, OmegaFold, and ESMFold ( SI Appendix ) and subsequently evaluated the predictive modeling performance using standard evaluation metrics including GDT-TS ( 9 ), TM-score ( 11 ), lDDT ( 12 ), MolProbity ( 14 ), and GDC-SC ( 15 ) ( SI ...
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold]

### Data-driven large-scale genomic analysis reveals an intricate phylogenetic and functional landscape in J-domain proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2218217120 | PMCID: PMC10410713 | PMID: 37523524
- Evidence: To further characterize the architectures of these JDPs, we leveraged the structural predictions available in the AlphaFold Protein Structure Database ( 39 ).
- Full pipeline: alignment/mapping [MAFFT v7.487] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold]

### Plasma membrane association and resistosome formation of plant helper immune receptors. (PNAS 2023)

- DOI: 10.1073/pnas.2222036120 | PMCID: PMC10410763 | PMID: 37523563
- Evidence: Based on an AlphaFold structure model of AtADR1-L1 CC R in the resting state, the two clusters of positively charged residues involved in r3m and r4m are spatially close to each other ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> stage not stated [ImageJ]

### Origin of the OAS-RNase L innate immune pathway before the rise of jawed vertebrates via molecular tinkering. (PNAS 2023)

- DOI: 10.1073/pnas.2304687120 | PMCID: PMC10400998 | PMID: 37487089
- Evidence: Structures of representative OAS-related and RNase proteins predicted by AlphaFold were retrieved from AlphaFold Protein Structure Database ( 58 ).
- Full pipeline: alignment/mapping [MAFFT, minimap2] -> structure determination [MAFFT] -> stage not stated [AlphaFold, HMMER, IQ-TREE v2.0]

### Nsp3-N interactions are critical for SARS-CoV-2 fitness and virulence. (PNAS 2023)

- DOI: 10.1073/pnas.2305674120 | PMCID: PMC10400999 | PMID: 37487098
- Evidence: Based on these published data and using AlphaFold2 in Colab ( 13 ), 3-dimensional structures of SARS-CoV and SARS-CoV-2 SUD were predicted ( Fig.
- Full pipeline: dimensionality reduction/clustering [AlphaFold]

### Toxic antiphage defense proteins inhibited by intragenic antitoxin proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2307382120 | PMCID: PMC10400941 | PMID: 37487082
- Version used: **2.0**
- Evidence: All Rpn proteins structures were predicted with AlphaFold 2.2.0 ( 13 , 29 ) using NIH's Biowulf cluster.
- Full pipeline: dimensionality reduction/clustering [AlphaFold v2.0]

### A bacterial-like Pictet-Spenglerase drives the evolution of fungi to produce β-carboline glycosides together with separate genes. (PNAS 2023)

- DOI: 10.1073/pnas.2303327120 | PMCID: PMC10372676 | PMID: 37467272
- Evidence: To determine the essential binding residues of Fcs1 and Fcs2, we modeled the 3D structures of these two proteins by AlphaFold algorithm ( https://alphafold.ebi.ac.uk/ ).
- Full pipeline: stage not stated [AlphaFold, BLAST, PyMOL v2.4]

### An interchangeable prion-like domain is required for Ty1 retrotransposition. (PNAS 2023)

- DOI: 10.1073/pnas.2303358120 | PMCID: PMC10372613 | PMID: 37459521
- Evidence: This Gag PrLD is predicted to be unstructured by AlphaFold ( 38 ), and no published structures of the region are available, similar to canonical prions ( 9 , 39 – 42 ) ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Structural insights into redox signal transduction mechanisms in the control of nitrogen fixation by the NifLA system. (PNAS 2023)

- DOI: 10.1073/pnas.2302732120 | PMCID: PMC10372690 | PMID: 37459513
- Evidence: Taking advantage of the recent advances in protein structure prediction of AlphaFold ( 32 ), we generated high-quality full-length models of NifL using the RoseTTAfold method on the Robetta server ( 33 ).
- Full pipeline: stage not stated [AlphaFold, UCSF Chimera]

### Modulation of inner junction proteins contributes to axoneme differentiation. (PNAS 2023)

- DOI: 10.1073/pnas.2303955120 | PMCID: PMC10372625 | PMID: 37463209
- Evidence: ( B ) Experimental ( Left , PDB: 6U42) and AlphaFold2 predicted ( Middle ) structures of Chlamydomonas flagellar inner junction complex including FAP20, PACRG, and alpha/beta tubulin dimer.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Regulatory sites in the Mon1-Ccz1 complex control Rab5 to Rab7 transition and endosome maturation. (PNAS 2023)

- DOI: 10.1073/pnas.2303750120 | PMCID: PMC10372576 | PMID: 37463208
- Evidence: The protein complex model was generated using AlphaFold2-Multimer ( 31 ).
- Full pipeline: stage not stated [AlphaFold]

### A periplasmic phospholipase that maintains outer membrane lipid asymmetry in <i>Pseudomonas aeruginosa</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302546120 | PMCID: PMC10374164 | PMID: 37463202
- Evidence: The crystal structures of E. coli PldA (PDB: 1QD6) and PagP (PDB: 1THQ) were obtained from the RCSB Protein Data Bank and compared against the P. aeruginosa AlphaFold database ( 46 , 47 ) using the DALI server ( 73 ).
- Full pipeline: alignment/mapping [BLAST, MAFFT v7.490, PyMOL] -> stage not stated [AlphaFold, IQ-TREE v1.6.12]

### Immunization with lytic polysaccharide monooxygenase CbpD induces protective immunity against <i>Pseudomonas aeruginosa</i> pneumonia. (PNAS 2023)

- DOI: 10.1073/pnas.2301538120 | PMCID: PMC10372616 | PMID: 37459522
- Evidence: Finally, AlphaFold2 ( 62 ) was used to predict the full-length structure of CbpD, which is a three-domain protein.
- Full pipeline: stage not stated [AlphaFold, Metascape]

### General features of transmembrane beta barrels from a large database. (PNAS 2023)

- DOI: 10.1073/pnas.2220762120 | PMCID: PMC10629564 | PMID: 37432995
- Evidence: Although contact information can be extracted from protein structure models, generated for example, by AlphaFold ( 36 ), this solution still does not provide a reliable way to categorize the predicted structures as barrels.
- Full pipeline: stage not stated [AlphaFold]

### Identification of a second glycoform of the clinically prevalent O1 antigen from <i>Klebsiella pneumoniae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2301302120 | PMCID: PMC10629545 | PMID: 37428935
- Evidence: The entries in red in ( A ) have a solved structure or were modeled using AlphaFold and are shown in ( B ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [MAFFT] -> stage not stated [AlphaFold, BLAST]

### ToxR activates the <i>Vibrio cholerae</i> virulence genes by tethering DNA to the membrane through versatile binding to multiple sites. (PNAS 2023)

- DOI: 10.1073/pnas.2304378120 | PMCID: PMC10629549 | PMID: 37428913
- Evidence: Fewer differences are observed when the crystal structure is compared with the AlphaFold model (rmsd = 0.696 Å).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### The ubiquitin-protein ligase MIEL1 localizes to peroxisomes to promote seedling oleosin degradation and lipid droplet mobilization. (PNAS 2023)

- DOI: 10.1073/pnas.2304870120 | PMCID: PMC10629534 | PMID: 37410814
- Evidence: ( C ) Arabidopsis MIEL1 structure predicted by AlphaFold ( 41 , 42 ) depicting the Zn finger-CHY (light purple), RING-H2 (medium purple), and Zn ribbon (dark purple) domains.
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Coordination of apicoplast transcription in a malaria parasite by internal and host cues. (PNAS 2023)

- DOI: 10.1073/pnas.2214765120 | PMCID: PMC10334805 | PMID: 37406097
- Evidence: The 3D structure of ApSigma was predicted using AlphaFold.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Clustal Omega] -> stage not stated [AlphaFold, ColabFold, R, UCSF Chimera]

### Qualitative metabolomics-based characterization of a phenolic UDP-xylosyltransferase with a broad substrate spectrum from &lt;i&gt;Lentinus brumalis&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2301007120 | PMCID: PMC10334773 | PMID: 37399371
- Evidence: We predicted the protein structure of UGT66A1 using AlphaFold2 through ColabFold ( 59 , 60 ), resulting in a high-quality prediction ( SI Appendix , Fig.
- Full pipeline: read trimming [R v3.26.8, Trim Galore v0.6.6, edgeR v3.26.8] -> alignment/mapping [Clustal Omega, HTSeq, MAFFT v7.310, R v3.26.8, edgeR v3.26.8] -> quantification [R v3.26.8, edgeR v3.26.8] -> normalisation [R v3.26.8, edgeR v3.26.8] -> stage not stated [AlphaFold, ColabFold, HISAT2, HMMER]

### More than just pattern recognition: Prediction of uncommon protein structure features by AI methods. (PNAS 2023)

- DOI: 10.1073/pnas.2221745120 | PMCID: PMC10334792 | PMID: 37399411
- Evidence: Protein structure prediction using artificial intelligence (AI) techniques, specifically the AlphaFold2 (AF2) deep learning network, developed by the DeepMind team ( 1 , 2 ), performed spectacularly well during the fourteenth season of the Critical Assessment of Structure Prediction experiment (CASP14) ( 3 ).
- Full pipeline: alignment/mapping [PyMOL] -> machine learning [AlphaFold]

### The evolution of archaeal flagellar filaments. (PNAS 2023)

- DOI: 10.1073/pnas.2304256120 | PMCID: PMC10334743 | PMID: 37399404
- Evidence: For the reassessment of the Aeropyrum filament, a preliminary model for the A. pernix flagellin FlaB2 was generated using AlphaFold2 ( 71 ).
- Full pipeline: alignment/mapping [UCSF Chimera] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, EMAN2]

### GPCR targeting of E3 ubiquitin ligase MDM2 by inactive β-arrestin. (PNAS 2023)

- DOI: 10.1073/pnas.2301934120 | PMCID: PMC10334748 | PMID: 37399373
- Evidence: The Mdm2 model was built by using the AlphaFold model of rat Mdm2 (light green) and rat βarr1-Mdm2 ABR complex (PDB code 8HSV).
- Full pipeline: structure determination [PHENIX] -> machine learning [PHENIX] -> stage not stated [AlphaFold, ColabFold v1.5.2, PyMOL]

### Plant lysin motif extracellular proteins are required for arbuscular mycorrhizal symbiosis. (PNAS 2023)

- DOI: 10.1073/pnas.2301884120 | PMCID: PMC10318984 | PMID: 37368927
- Evidence: To assess whether the MtLysMe proteins may also possess such a structural signature for binding similar molecules, we used AlphaFold ( https://github.com/deepmind/alphafold ) to predict the structures of the LysM domains of the MtLysMe proteins and found that they all possess the classical LysM domain βααβ ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, MAFFT]

### Structural evolution of an immune evasion determinant shapes pathogen host tropism. (PNAS 2023)

- DOI: 10.1073/pnas.2301549120 | PMCID: PMC10319004 | PMID: 37364114
- Evidence: Structure Determination by Crystallization and Prediction by AlphaFold.
- Full pipeline: structure determination [AlphaFold]

### De novo designed ice-binding proteins from twist-constrained helices. (PNAS 2023)

- DOI: 10.1073/pnas.2220380120 | PMCID: PMC10319034 | PMID: 37364125
- Evidence: As an additional check, we also folded the designed sequences using AlphaFold2 ( 22 ) and found excellent agreement for the twist of the ice-binding helix as compared with the Rosetta ab initio predictions ( SI Appendix , Fig.
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ImageJ]

### Conformational switching and flexibility in cobalamin-dependent methionine synthase studied by small-angle X-ray scattering and cryoelectron microscopy. (PNAS 2023)

- DOI: 10.1073/pnas.2302531120 | PMCID: PMC10293825 | PMID: 37339208
- Evidence: Detailed descriptions of protein expression and purification, preparation of pure oxidation states, cofactor reconstitution, limited proteolysis, SAXS, cryo-EM, bioinformatics, and AlphaFold2 analyses are available in SI Appendix .
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold]

### Replitrons: A major group of eukaryotic transposons encoding HUH endonuclease. (PNAS 2023)

- DOI: 10.1073/pnas.2301424120 | PMCID: PMC10288648 | PMID: 37307447
- Evidence: The tertiary structure of the Replitron-1 transposase was inferred using AlphaFold2 ( 22 ), accessed via the AlphaFold2 Colab notebook v1.5.2 ( 65 ).
- Full pipeline: alignment/mapping [MAFFT v7.471] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BEDTools, IQ-TREE v2.0.3]

### McrD binds asymmetrically to methyl-coenzyme M reductase improving active-site accessibility during assembly. (PNAS 2023)

- DOI: 10.1073/pnas.2302815120 | PMCID: PMC10288656 | PMID: 37307484
- Evidence: We docked a previous crystal structure, of the MCR ox1-silent state purified from Methanosarcina barkeri ( 2 ), along with an AlphaFold2 ( 20 , 21 ) prediction of McrD into both densities and then manually rebuilt each model.
- Full pipeline: stage not stated [AlphaFold]

### A spatiotemporal barrier formed by Follistatin is required for left-right patterning. (PNAS 2023)

- DOI: 10.1073/pnas.2219649120 | PMCID: PMC10268237 | PMID: 37276408
- Evidence: Structural modeling of the Fsta–Spaw complex using AlphaFold-Multimer revealed a large buried surface area (1,379 Å 2 ) for the WT Fsta and a medium-buried surface area (750 Å 2 ) for the FstaΔ4 ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, WGCNA]

### Basis for high-affinity ethylene binding by the ethylene receptor ETR1 of Arabidopsis. (PNAS 2023)

- DOI: 10.1073/pnas.2215195120 | PMCID: PMC10266040 | PMID: 37253004
- Evidence: New structural models for the ETR1 homodimer were generated with AlphaFold-Multimer ( 47 , 48 ).
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### HEIP1 is required for efficient meiotic crossover implementation and is conserved from plants to humans. (PNAS 2023)

- DOI: 10.1073/pnas.2221746120 | PMCID: PMC10265981 | PMID: 37252974
- Evidence: AlphaFold-based modeling of HEIP1 proteins predicts a largely disordered or unstructured protein, with only small patches forming helices.
- Full pipeline: stage not stated [AlphaFold]

### Structural insights into the assembly of the agrin/LRP4/MuSK signaling complex. (PNAS 2023)

- DOI: 10.1073/pnas.2300453120 | PMCID: PMC10266037 | PMID: 37252960
- Evidence: The models of β2 and β3 of LRP4 were first generated by AlphaFold2 ( 30 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, RELION]

### An end-to-end deep learning method for protein side-chain packing and inverse folding. (PNAS 2023)

- DOI: 10.1073/pnas.2216438120 | PMCID: PMC10266014 | PMID: 37253017
- Evidence: This component draws two submodules introduced in AlphaFold2’s Evoformer for processing MSA and pair features, namely the use of pair-biased self-attention and triangle updates to revise pairwise features.
- Full pipeline: stage not stated [AlphaFold, ColabFold, RoseTTAFold]

### Identification of broad, potent antibodies to functionally constrained regions of SARS-CoV-2 spike following a breakthrough infection. (PNAS 2023)

- DOI: 10.1073/pnas.2220948120 | PMCID: PMC10265947 | PMID: 37253011
- Evidence: ( E and F ) Cryo-EM reconstruction of C68.59 Fab bound to S6P structure (PDB ID 7SBP) where C68.59 Fab structure is calculated by AlphaFold fitted into map.
- Full pipeline: structure determination [AlphaFold]

### Cryo-EM structure of the Mon1-Ccz1-RMC1 complex reveals molecular basis of metazoan RAB7A activation. (PNAS 2023)

- DOI: 10.1073/pnas.2301725120 | PMCID: PMC10235969 | PMID: 37216550
- Evidence: The DmMon1, DmCcz1, and DmRMC1 models were initially created using AlphaFold 2 ( 40 ).
- Full pipeline: structure determination [PHENIX v1.19] -> machine learning [EMAN2] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ImageJ, RELION v3.1]

### Paf1 complex subunit Rtf1 stimulates H2B ubiquitylation by interacting with the highly conserved N-terminal helix of Rad6. (PNAS 2023)

- DOI: 10.1073/pnas.2220041120 | PMCID: PMC10235976 | PMID: 37216505
- Evidence: In addition, we used AlphaFold-Multimer ( 49 , 50 ) to generate a model of the Rad6–HMD interaction independent of experimental constraints ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [DESeq2, STAR v2.7.5a] -> quantification [DESeq2] -> stage not stated [AlphaFold, ComplexHeatmap, featureCounts]

### Reverse-QTY code design of active human serum albumin self-assembled amphiphilic nanoparticles for effective anti-tumor drug doxorubicin release in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2220173120 | PMCID: PMC10214157 | PMID: 37186820
- Evidence: To evaluate the structural similarity between native HSA and rQTY variants, AlphaFold2 ( 36 ) was used to predicted the variant structures.
- Full pipeline: alignment/mapping [PyMOL] -> stage not stated [AlphaFold]

### Mechanistic insights into the regulation of cell wall hydrolysis by FtsEX and EnvC at the bacterial division site. (PNAS 2023)

- DOI: 10.1073/pnas.2301897120 | PMCID: PMC10214136 | PMID: 37186861
- Evidence: The initial model of FtsE and FtsX was generated by AlphaFold2 ( 34 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold]

### Architecture and genomic arrangement of the MurE-MurF bacterial cell wall biosynthesis complex. (PNAS 2023)

- DOI: 10.1073/pnas.2219540120 | PMCID: PMC10214165 | PMID: 37186837
- Evidence: Hence, a model of B. pertussis MurE–MurF generated by AlphaFold2 ( 49 ) was tested.
- Full pipeline: stage not stated [AlphaFold, Cytoscape]

### The SHDRA syndrome-associated gene <i>TMEM260</i> encodes a protein-specific O-mannosyltransferase. (PNAS 2023)

- DOI: 10.1073/pnas.2302584120 | PMCID: PMC10214176 | PMID: 37186866
- Evidence: AlphaFold ( 23 ) predicts TMEM260 to share the GT-C fold characteristic for mannosyltransferases, including a conserved N-terminal GT-C module and a variable C-terminal module ( Fig.
- Full pipeline: variant calling [GATK, VEP] -> quantification [ImageJ] -> stage not stated [AlphaFold]

### Croquemort elicits activation of the immune deficiency pathway in ticks. (PNAS 2023)

- DOI: 10.1073/pnas.2208673120 | PMCID: PMC10193931 | PMID: 37155900
- Evidence: Then, we modeled the ectodomain of Crq to CD36 and performed homology comparisons between Crq and the crystal structures of LIMP-2 (PDB:4F7B) and CD36 (PDB:5LGD) using Protein Homology/Analogy Recognition Engine (Phyre) 2 ( 35 ) and AlphaFold Protein Structural Database ( 41 ) ( Fig.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### A tale of two copies: Evolutionary trajectories of moth pheromone receptors. (PNAS 2023)

- DOI: 10.1073/pnas.2221166120 | PMCID: PMC10193968 | PMID: 37155838
- Evidence: The AlphaFold2 algorithm ( 60 ) was used to model the 3D structures of both current and ancestral ORs, through the Institut Français de Bioinformatique Core Cluster (ANR-11-INBS-0013).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2, MAFFT] -> dimensionality reduction/clustering [AlphaFold, R] -> structure determination [MAFFT] -> stage not stated [ChimeraX]

### Structure of WNT inhibitor adenomatosis polyposis coli down-regulated 1 (APCDD1), a cell-surface lipid-binding protein. (PNAS 2023)

- DOI: 10.1073/pnas.2217096120 | PMCID: PMC10193966 | PMID: 37155902
- Evidence: Searches for structure-based similarities to APCDD1, ABD1, and ABD2 were performed against the databases of the PDB and AlphaFold ( 36 ) using the DALI server ( 37 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CCP4, PyMOL, RoseTTAFold]

### Vertebrate-tropism of a cressdnavirus lineage implicated by poxvirus gene capture. (PNAS 2023)

- DOI: 10.1073/pnas.2303844120 | PMCID: PMC10193959 | PMID: 37155884
- Version used: **2.1.1**
- Evidence: Protein structures were predicted using AlphaFold v2.1.1 ( 68 ), aligned using the Protein Data Bank (PDB) pairwise structure alignment tool ( 69 ), and visualized using Mol* ( 70 ).
- Full pipeline: read trimming [IQ-TREE v2.2.0, MAFFT v7.487] -> alignment/mapping [AlphaFold v2.1.1, BEDTools, BLAST v2.0.15, IQ-TREE v2.2.0, MAFFT v7.487] -> visualisation [AlphaFold v2.1.1]

### The DedA superfamily member PetA is required for the transbilayer distribution of phosphatidylethanolamine in bacterial membranes. (PNAS 2023)

- DOI: 10.1073/pnas.2301979120 | PMCID: PMC10193950 | PMID: 37155911
- Evidence: Alphafold2 predictions of PetA were downloaded from the AlphaFold Protein Structure Database (available at: https://alphafold.ebi.ac.uk/ ).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4] -> visualisation [Clustal Omega v1.2.4] -> stage not stated [AlphaFold, ImageJ v2.3]

### Structure of the metazoan Rab7 GEF complex Mon1-Ccz1-Bulli. (PNAS 2023)

- DOI: 10.1073/pnas.2301908120 | PMCID: PMC10193976 | PMID: 37155863
- Evidence: Model building started from AlphaFold ( 30 ) predictions that were iteratively refined using Coot ( 43 ) and Phenix ( 44 ).
- Full pipeline: structure determination [AlphaFold, PHENIX]

### Evolution and diversification of the ACT-like domain associated with plant basic helix-loop-helix transcription factors. (PNAS 2023)

- DOI: 10.1073/pnas.2219469120 | PMCID: PMC10175843 | PMID: 37126718
- Evidence: The βαββαβ secondary structures and tertiary protein structures of the ACT-like domains were predicted using PSIPRED ( 54 ) and AlphaFold ( 38 , 39 ) via the ColabFold interface ( 55 ).
- Full pipeline: differential/statistical testing [MrBayes v3.2.7] -> stage not stated [AlphaFold, ColabFold, RAxML v1.1.0]

### The cell envelope of <i>Thermotogae</i> suggests a mechanism for outer membrane biogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2303275120 | PMCID: PMC10160955 | PMID: 37094164
- Evidence: Trimer structure predictions were performed using AlphaFold2 Multimer v2.3.0 ( 31 ), and the surface hydrophobicity and electrostatic charge for the highest ranked model were computed in ChimeraX ( 68 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [AlphaFold, ChimeraX, HMMER, IQ-TREE v2.1.4, ImageJ, RoseTTAFold]

### Structure of the human respiratory complex II. (PNAS 2023)

- DOI: 10.1073/pnas.2216713120 | PMCID: PMC10161127 | PMID: 37098072
- Evidence: The atomic model of complex II was built based on the structure of SDHA/B/C/D predicted from the AlphaFold Protein Structure Database ( 46 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold]

### Exploiting conformational dynamics to modulate the function of designed proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2303149120 | PMCID: PMC10161014 | PMID: 37094170
- Evidence: Like the success of AlphaFold2 ( 4 ) and RoseTTAFold ( 5 ) that was based on training with a large set of structures, robust design strategies that include low energy states on an energy landscape must await the development of training sets that correlate how an amino acid sequence is able to access a set of conformers rather than only a single one.
- Full pipeline: machine learning [AlphaFold, RoseTTAFold] -> stage not stated [PyMOL]

### Cross-linking mass spectrometry discovers, evaluates, and corroborates structures and protein-protein interactions in the human cell. (PNAS 2023)

- DOI: 10.1073/pnas.2219418120 | PMCID: PMC10151615 | PMID: 37071682
- Evidence: Methods Detailed descriptions on how the subcellular fractionation, protein cross-linking, peptide preparation for mass spectrometry, mass spectrometry data acquisition, data analysis, statistical analysis, implementation of AlphaFold Multimer-v2 model predictions and associated analyses can be found in SI Appendix .
- Full pipeline: differential/statistical testing [AlphaFold] -> stage not stated [STRING db]

### Elucidating the origins of phycocyanobilin biosynthesis and phycobiliproteins. (PNAS 2023)

- DOI: 10.1073/pnas.2300770120 | PMCID: PMC10151467 | PMID: 37071675
- Evidence: S4 and see below) and of predicted pre-PcyA structures from the AlphaFold database [( 33 ); SI Appendix , Fig.
- Full pipeline: alignment/mapping [MAFFT v7.450] -> visualisation [VMD] -> stage not stated [AlphaFold]

### Genomic and structural basis for evolution of tropane alkaloid biosynthesis. (PNAS 2023)

- DOI: 10.1073/pnas.2302448120 | PMCID: PMC10151470 | PMID: 37068250
- Evidence: The putative protein structures of En MT4, En CYP81AN15, and Ab CYP82M3 were predicted by AlphaFold2.
- Full pipeline: alignment/mapping [BUSCO, MAFFT] -> dimensionality reduction/clustering [OrthoFinder] -> visualisation [PyMOL v2.4] -> stage not stated [AlphaFold, AutoDock Vina v1.1.2, IQ-TREE]

### TapA acts as specific chaperone in TasA filament formation by strand complementation. (PNAS 2023)

- DOI: 10.1073/pnas.2217070120 | PMCID: PMC10151520 | PMID: 37068239
- Evidence: Three-dimensional structure predictions based on the AlphaFold ( 24 ) algorithm were run via the publicly available ColabFold ( https://github.com/sokrypton/ColabFold ) ( 42 ) infrastructure through Google Colaboratory.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [AlphaFold, ColabFold] -> stage not stated [PyMOL]

### Interdigitated immunoglobulin arrays form the hyperstable surface layer of the extremophilic bacterium &lt;i&gt;Deinococcus radiodurans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2215808120 | PMCID: PMC10120038 | PMID: 37043530
- Version used: **2.2.0**
- Evidence: ...tabases (versions of the Protein Data Bank and ECOD databases filtered for a maximum pairwise identity of 70%) and using structural models built with AlphaFold v2.2.0 using the “monomer_ptm” model ( 27 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold v2.2.0, ChimeraX, MotionCor2, RELION]

### Large-scale invasion of unicellular eukaryotic genomes by integrating DNA viruses. (PNAS 2023)

- DOI: 10.1073/pnas.2300465120 | PMCID: PMC10120064 | PMID: 37036967
- Evidence: Data, Materials, and Software Availability Supplementary raw data are available at https://doi.org/10.6084/m9.figshare.21581355.v3 ( 39 ) and comprise: 1) AlphaFold structural predictions (.pdb) of MCP genes; 2) all MCP genes confirmed by HHpred or Alphafold (Fasta format); 3) Cytoscape network of MCP genes used in Fig.
- Full pipeline: alignment/mapping [BEDTools, ColabFold, MAFFT v7.490, MUSCLE v3.8.1551] -> registration [MAFFT v7.490] -> dimensionality reduction/clustering [ColabFold, HMMER v3.1b, MAFFT v7.490, MUSCLE v3.8.1551] -> stage not stated [AlphaFold, Cytoscape, Flye v2.9, minimap2]

### Evolution of insect innate immunity through domestication of bacterial toxins. (PNAS 2023)

- DOI: 10.1073/pnas.2218334120 | PMCID: PMC10120054 | PMID: 37036995
- Version used: **2.1.0**
- Evidence: D. ananassae CdtB and CdtB::AIP56 sequences were submitted to the AlphaFold v2.1.0 colab notebook ( https://colab.research.google.com/github/deepmind/alphafold/blob/main/notebooks/AlphaFold.ipynb ) ( 45 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.450] -> stage not stated [AlphaFold v2.1.0]

### Clock-regulated coactivators selectively control gene expression in response to different temperature stress conditions in <i>Arabidopsis</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2216183120 | PMCID: PMC10120023 | PMID: 37036986
- Evidence: The structural models of LNK–RVE complexes were generated by using AlphaFold2 ( 24 ) via the Google Colaboratory (ColabFold) interface ( 25 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, PyMOL]

### The <i>Holothuria leucospilota</i> genome elucidates sacrificial organ expulsion and bioadhesive trap enriched with amyloid-patterned proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2213512120 | PMCID: PMC10120082 | PMID: 37036994
- Evidence: 3D structures of the proteins were predicted by AlphaFold based on their amino acid sequences.
- Full pipeline: alignment/mapping [BUSCO, BWA, MAFFT, RAxML] -> normalisation [DESeq2] -> visualisation [MAFFT, RAxML] -> stage not stated [AlphaFold, InterProScan]

### Bacterial origin of a key innovation in the evolution of the vertebrate eye. (PNAS 2023)

- DOI: 10.1073/pnas.2214815120 | PMCID: PMC10120077 | PMID: 37036996
- Evidence: ( D ) Structural comparison of D4 from bovine IRBP (PDB: 7JTI) ( 4 ) and a predicted structure of a bacterial homolog that was generated by AlphaFold2 ( 5 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, BLAST, IQ-TREE, RAxML]

### <i>Starships</i> are active eukaryotic transposable elements mobilized by a new family of tyrosine recombinases. (PNAS 2023)

- DOI: 10.1073/pnas.2214521120 | PMCID: PMC10104507 | PMID: 37023132
- Evidence: AlphaFold Protein Structure Predictions.
- Full pipeline: alignment/mapping [Bowtie2, Clustal Omega, MAFFT, MrBayes] -> differential/statistical testing [Clustal Omega, MrBayes] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.0.3]

### LPS-aggregating proteins GBP1 and GBP2 are each sufficient to enhance caspase-4 activation both in cellulo and in vitro. (PNAS 2023)

- DOI: 10.1073/pnas.2216028120 | PMCID: PMC10104521 | PMID: 37023136
- Evidence: ( A ) PDB entry 1F5N and AlphaFold models AF- P32456 , AF- Q96PP8 .
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Yeast PIC-Mediator structure with RNA polymerase II C-terminal domain. (PNAS 2023)

- DOI: 10.1073/pnas.2220542120 | PMCID: PMC10104585 | PMID: 37014863
- Evidence: Med1 was predicted using AlphaFold 2 ( 16 , 18 ), stripped of long unstructured extensions, rigidly docked into the cryo-EM density, and flexibly fitted with Namdinator ( 19 ).
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [PHENIX, RELION] -> visualisation [ChimeraX, PyMOL v2.4] -> stage not stated [AlphaFold, UCSF Chimera]

### Deciphering the evolution of flavin-dependent monooxygenase stereoselectivity using ancestral sequence reconstruction. (PNAS 2023)

- DOI: 10.1073/pnas.2218248120 | PMCID: PMC10104550 | PMID: 37014851
- Evidence: 1 D ) and created a model of AzaH with AlphaFold ( 51 ) ( Fig.
- Full pipeline: alignment/mapping [MUSCLE] -> normalisation [CCP4] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Altered plasma membrane abundance of the sulfatide-binding protein NF155 links glycosphingolipid imbalances to demyelination. (PNAS 2023)

- DOI: 10.1073/pnas.2218823120 | PMCID: PMC10083573 | PMID: 36996106
- Evidence: Recent advances in artificial intelligence-based deep learning strategies, exemplified by AlphaFold2 (AF2), allow for the highly accurate prediction of protein structures ( 51 ).
- Full pipeline: dimensionality reduction/clustering [ChimeraX] -> structure determination [ChimeraX] -> machine learning [AlphaFold] -> stage not stated [ColabFold v1.3, ImageJ]

### Identification of a broadly conserved family of enzymes that hydrolyze (p)ppApp. (PNAS 2023)

- DOI: 10.1073/pnas.2213771120 | PMCID: PMC10083569 | PMID: 36989297
- Evidence: Overlay of the AlphaFold2 predicted Bc Tas1 structure with crystal structures of Tas1, and the bifunctional (p)ppGpp/(p)ppApp synthetase, SAS1, suggests that Bc Tas1 exhibits greater structural similarity to Tas1 (2.1Å Cα rmsd) than it does to SAS1 (2.7Å Cα rmsd), lending support to our prediction that it synthesizes (p)ppApp ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Intrinsically disordered proteins SAID1/2 condensate on SERRATE for dual inhibition of miRNA biogenesis in Arabidopsis. (PNAS 2023)

- DOI: 10.1073/pnas.2216006120 | PMCID: PMC10083546 | PMID: 36972460
- Evidence: This proposal can be supported by our AlphaFold2 modeling in vitro ( 41 ).
- Full pipeline: stage not stated [AlphaFold]

### A c-di-GMP binding effector controls cell size in a cyanobacterium. (PNAS 2023)

- DOI: 10.1073/pnas.2221874120 | PMCID: PMC10068817 | PMID: 36947515
- Evidence: Moreover, the 3D protein structures of CdgR and Syn_CdgR, predicted by AlphaFold, could be well-superposed with the structure of Syn_CdgR-(c-di-GMP) complex solved in this study, except for the flexible helix α8 at the C-terminal part ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, PHENIX]

### Structure of mycobacterial respiratory complex I. (PNAS 2023)

- DOI: 10.1073/pnas.2214949120 | PMCID: PMC10068793 | PMID: 36952383
- Evidence: Starting models of NuoA–NuoN were generated by one-to-one threading with the Phyre2 server ( 103 ) using the M. smegmatis amino acid sequences and predicted models of M. tuberculosis subunits from the AlphaFold Protein Structure Database ( 104 ).
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [RELION] -> structure determination [PHENIX v1.19.2] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, Coot v0.9.6]

### The debate over understanding in AI's large language models. (PNAS 2023)

- DOI: 10.1073/pnas.2215907120 | PMCID: PMC10068812 | PMID: 36943882
- Evidence: ...e considered a novel form of “understanding”, one that enables extraordinary, superhuman predictive ability, such as in the case of the AlphaZero and AlphaFold systems from DeepMind ( 82 , 83 ), which respectively seem to bring an “alien” form of intuition to the domains of chess playing and protein structure prediction ( 84 , 85 ).
- Full pipeline: stage not stated [AlphaFold]

### Cryo-EM analyses of KIT and oncogenic mutants reveal structural oncogenic plasticity and a target for therapeutic intervention. (PNAS 2023)

- DOI: 10.1073/pnas.2300054120 | PMCID: PMC10068818 | PMID: 36943885
- Evidence: Due to a lack of high-resolution structural data for D5, AlphaFold ( 40 ) structure predictions were used for PDGFR α (UniProt P16234 , AF- P16234 -F1-model_v2), PDGFR β (UniProt P09619 , AF- P09619 -F1-model_v2), CSF1R (UniProt P07333 , AF- P07333 -F1-model_v2), and FLT3 (UniProt P36888 , AF- P36888 -F1-model_v2).
- Full pipeline: structure determination [PHENIX v1.02.1] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, RELION v3.1, UCSF Chimera]

### Cryo-EM structure of the four-subunit <i>Rhodobacter sphaeroides</i> cytochrome <i>bc</i><sub>1</sub> complex in styrene maleic acid nanodiscs. (PNAS 2023)

- DOI: 10.1073/pnas.2217922120 | PMCID: PMC10041115 | PMID: 36913593
- Evidence: We attempted to model the structure of SIV using AlphaFold ( 48 ), which predicted a range of conformations for the soluble domain and could not correctly position SIV within the remainder of the complex.
- Full pipeline: structure determination [Coot v0.9.6, PHENIX v1.19.2] -> stage not stated [AlphaFold, ChimeraX v1.3, RELION v3.1]

### Superhuman artificial intelligence can improve human decision-making by increasing novelty. (PNAS 2023)

- DOI: 10.1073/pnas.2214840120 | PMCID: PMC10041097 | PMID: 36913582
- Evidence: ...agnosing diseases) ( 2 ), transportation (e.g., autonomous driving) ( 3 ), language (e.g., ChatGPT based on GPT-3) ( 4 ), and natural sciences (e.g., AlphaFold) ( 5 ), among others ( 6 ).
- Full pipeline: stage not stated [AlphaFold]

### Classification of domains in predicted structures of the human proteome. (PNAS 2023)

- DOI: 10.1073/pnas.2214069120 | PMCID: PMC10041065 | PMID: 36917664
- Evidence: AlphaFold (AF), developed by DeepMind, demonstrated its ability to predict three-dimensional structures of proteins from their sequences with accuracy approaching that of experimental methods ( 16 , 18 , 19 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold]

### Experimental evidence for the functional importance and adaptive advantage of A-to-I RNA editing in fungi. (PNAS 2023)

- DOI: 10.1073/pnas.2219029120 | PMCID: PMC10041177 | PMID: 36917661
- Evidence: The AlphaFold structure of Cme5 was downloaded from the EMBL-EBI database and visualized by UCSF Chimera 1.16 ( 73 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HISAT2, featureCounts] -> quantification [R v4.1, featureCounts] -> normalisation [featureCounts] -> visualisation [AlphaFold, R v4.1, UCSF Chimera v1.16] -> stage not stated [BLAST]

### De novo design of small beta barrel proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2207974120 | PMCID: PMC10089152 | PMID: 36897987
- Evidence: For this “constrained hallucination” approach, we used trRosetta which predicts interresidue distances and orientations [the more accurate AlphaFold2 ( 24 ) and RoseTTAFold ( 25 ) had not yet been developed].
- Full pipeline: simulation/modelling [RoseTTAFold] -> structure determination [RoseTTAFold] -> machine learning [AlphaFold]

### Dysregulation of PD-L1 by UFMylation imparts tumor immune evasion and identified as a potential therapeutic target. (PNAS 2023)

- DOI: 10.1073/pnas.2215732120 | PMCID: PMC10089188 | PMID: 36893266
- Evidence: We first selected the crystal structure of 3OQC (UFSP2) as the receptor protein from PDB database and the recently published AlphaFold protein structure database.
- Full pipeline: quality control [AlphaFold]

### Structure of the Wnt-Frizzled-LRP6 initiation complex reveals the basis for coreceptor discrimination. (PNAS 2023)

- DOI: 10.1073/pnas.2218238120 | PMCID: PMC10089208 | PMID: 36893265
- Evidence: AlphaFold2 ( 54 ) was used to model hLRP6 E1E4 for superimposition to the XWnt8–mFzd8 CRD –hLRP6 E1E2 model.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ChimeraX]

### Design, synthesis, and characterization of protein origami based on self-assembly of a brick and staple artificial protein pair. (PNAS 2023)

- DOI: 10.1073/pnas.2218428120 | PMCID: PMC10089216 | PMID: 36893280
- Evidence: Further increase of structural and functional complexity of the brick itself, within the supramolecular complexes, could be designed with the recent advent of AlphaFold2 ( 54 ), RoseTTAFold ( 55 ), and Protein MPNN ( 56 ) computational platforms.
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> structure determination [IMOD, MotionCor2] -> stage not stated [AlphaFold, RoseTTAFold]

### Cryo-EM structure of the human chemerin receptor 1-Gi protein complex bound to the C-terminal nonapeptide of chemerin. (PNAS 2023)

- DOI: 10.1073/pnas.2214324120 | PMCID: PMC10089180 | PMID: 36881626
- Evidence: The models were constructed using structure information from PDB ID code 7WXZ for portions of Gi1 and scFv16, and a predicted model from AlphaFold for portions of CMKLR1.
- Full pipeline: structure determination [Coot, PHENIX, UCSF Chimera v1.12] -> stage not stated [AlphaFold]

### Improved global protein homolog detection with major gains in function identification. (PNAS 2023)

- DOI: 10.1073/pnas.2211823120 | PMCID: PMC9992864 | PMID: 36827259
- Evidence: Structures are from AlphaFold2 predictions ( 29 ), with HPO30 on the right and CLRN3 on the left.
- Full pipeline: stage not stated [AlphaFold]

### Integrating comparative modeling and accelerated simulations reveals conformational and energetic basis of actomyosin force generation. (PNAS 2023)

- DOI: 10.1073/pnas.2215836120 | PMCID: PMC9992861 | PMID: 36802417
- Evidence: Recently, a machine learning-based method, AlphaFold2, has successfully demonstrated the ability in predicting protein folds ( 25 ) and multimeric interfaces ( 26 ) given a query sequence.
- Full pipeline: stage not stated [AlphaFold]

### Peptide-binding specificity prediction using fine-tuned protein structure prediction networks. (PNAS 2023)

- DOI: 10.1073/pnas.2216697120 | PMCID: PMC9992841 | PMID: 36802421
- Evidence: AlphaFold Modeling of Peptide-MHC Pairs.
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AlphaFold, Python, RoseTTAFold]

### Discovery of a rapidly evolving yeast defense factor, &lt;i&gt;KTD1&lt;/i&gt;, against the secreted killer toxin K28. (PNAS 2023)

- DOI: 10.1073/pnas.2217194120 | PMCID: PMC9974470 | PMID: 36800387
- Version used: **2.0.0**
- Evidence: The structure of Ktd1p was predicted using AlphaFold (version 2.0.0) ( 36 ) and visualized in PyMOL (version 2.3.0 Open-Source), with the position of the transmembrane helices shown according to Poirey et al.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [ggpubr] -> visualisation [AlphaFold v2.0.0, PyMOL v2.3.0] -> stage not stated [BLAST, R, ggplot2 v3.3.5]

### Characterization of a unique polysaccharide monooxygenase from the plant pathogen <i>Magnaporthe oryzae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2215426120 | PMCID: PMC9974505 | PMID: 36791100
- Evidence: To better understand the role of the DUF, a 3D structure prediction of Mo PMO9A using AlphaFold2 was carried out ( 54 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [ChimeraX, Clustal Omega, Cytoscape] -> visualisation [Clustal Omega, Cytoscape] -> stage not stated [AlphaFold, ColabFold, ImageJ, R]

### 1700029I15Rik orchestrates the biosynthesis of acrosomal membrane proteins required for sperm-egg interaction. (PNAS 2023)

- DOI: 10.1073/pnas.2207263120 | PMCID: PMC9974436 | PMID: 36787362
- Evidence: ( H ) 1700029I15Rik protein structure predicted by AlphaFold (AF- Q8CF31 -F1) ( 17 ).
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### Molecular mechanism of GTP binding- and dimerization-induced enhancement of Sar1-mediated membrane remodeling. (PNAS 2023)

- DOI: 10.1073/pnas.2212513120 | PMCID: PMC9974494 | PMID: 36780528
- Evidence: Methods Materials and Methods We employ AlphaFold2 ( 27 ) to predict the structures of Sar1 in both GDP- PDB code 1F6B ( 8 ) and GTP- PDB code 1M2O ( 9 ) bound states referred to as the h-GDP and y-GTP structures, respectively.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, VMD]

### Angiopoietin-like protein 4/8 complex-mediated plasmin generation leads to cleavage of the complex and restoration of LPL activity. (PNAS 2023)

- DOI: 10.1073/pnas.2214081120 | PMCID: PMC9963551 | PMID: 36763533
- Evidence: From a structural biology perspective, ANGPTL4 is predicted by the artificial intelligence programs AlphaFold2 and Logical Data for Condition Monitoring to exhibit a fibrinogen-like structure ( 38 – 40 ).
- Full pipeline: stage not stated [AlphaFold]

### Pangenomic analysis reveals plant NAD<sup>+</sup> manipulation as an important virulence activity of bacterial pathogen effectors. (PNAS 2023)

- DOI: 10.1073/pnas.2217114120 | PMCID: PMC9963460 | PMID: 36753463
- Evidence: Using AlphaFold2 ( 32 ), we generated a structural model for OG18056.
- Full pipeline: alignment/mapping [Clustal Omega, HMMER] -> stage not stated [AlphaFold]

### PKD autoinhibition in &lt;i&gt;trans&lt;/i&gt; regulates activation loop autophosphorylation in &lt;i&gt;cis&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2212909120 | PMCID: PMC9962925 | PMID: 36745811
- Evidence: The model was compared to the AlphaFold2 ( 21 ) prediction for the PKD1 kinase domain and tested biochemically.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Structural basis of V-ATPase V<sub>O</sub> region assembly by Vma12p, 21p, and 22p. (PNAS 2023)

- DOI: 10.1073/pnas.2217181120 | PMCID: PMC9963935 | PMID: 36724250
- Evidence: The previously published V O model 6O7T ( 36 ), AlphaFold models of Vma12p, Vma21p, and Vma22p ( 35 ), and subunit F from previously published V-ATPase model 7TMQ ( 19 ) were used for rigid body fitting into the maps of V O :Vma12-22p, V O ∆aef:Vma12-22p, and V O :Vma21p with University of California San Francisco (UCSF) Chimera ( 55 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold]

### Supramolecular organization and dynamics of mannosylated phosphatidylinositol lipids in the mycobacterial plasma membrane. (PNAS 2023)

- DOI: 10.1073/pnas.2212755120 | PMCID: PMC9945971 | PMID: 36693100
- Evidence: All predicted protein structures from Mtb (taxonomy id:83332) and E. coli (taxonomy id:83333) labeled as transmembrane on UniProt ( 48 ) were downloaded from the AlphaFold database ( 49 ), totaling 729 for Mtb and 1,229 for E.coli .
- Full pipeline: simulation/modelling [GROMACS v2021.3, Python] -> stage not stated [AlphaFold, Clustal Omega, Matplotlib, PLUMED]

### Destabilizing NF1 variants act in a dominant negative manner through neurofibromin dimerization. (PNAS 2023)

- DOI: 10.1073/pnas.2208960120 | PMCID: PMC9945959 | PMID: 36689660
- Evidence: The core of the NF1 dimer was completely manually modeled in Coot ( 35 ) and then compared with the AlphaFold2 ( 36 ) predictions of separate domains.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, Coot, MotionCor2, RELION]

### The Shr receptor from &lt;i&gt;Streptococcus pyogenes&lt;/i&gt; uses a cap and release mechanism to acquire heme-iron from human hemoglobin. (PNAS 2023)

- DOI: 10.1073/pnas.2211939120 | PMCID: PMC9945957 | PMID: 36693107
- Evidence: A minimal ensemble search procedure was performed using the BILBO-MD service to describe the possible conformational ensembles sampled by the apo Shr H1H2 and Hb–Shr H1H2 complex, with the search models derived from AlphaFold2 predictions and restrained relative to each other as described in further detail in SI Appendix , Materials and Methods ( 79 ).
- Full pipeline: machine learning [AlphaFold]

### Nodavirus RNA replication crown architecture reveals proto-crown precursor and viral protein A conformational switching. (PNAS 2023)

- DOI: 10.1073/pnas.2217412120 | PMCID: PMC9945985 | PMID: 36693094
- Evidence: We found that isolating two adjacent Pol domains for focused refinement gave the best density improvement and provided a map that, combined with the structure predicted by AlphaFold 2 ( 36 ), allowed generating a backbone trace missing the last 35 aa of the Pol domain and covering 80% of the remainder (missing aa 487 to 533, 630 to 653, and 816 to 828).
- Full pipeline: structure determination [AlphaFold] -> stage not stated [ChimeraX, PyMOL]

### Fine structure and assembly pattern of a minimal myophage Pam3. (PNAS 2023)

- DOI: 10.1073/pnas.2213727120 | PMCID: PMC9942802 | PMID: 36656854
- Evidence: The initial models for the protein components of Pam3 were generated by AlphaFold2 ( 38 ).
- Full pipeline: normalisation [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### TMEM161B regulates cerebral cortical gyration, Sonic Hedgehog signaling, and ciliary structure in the developing central nervous system. (PNAS 2023)

- DOI: 10.1073/pnas.2209964120 | PMCID: PMC9942790 | PMID: 36669111
- Evidence: Structural models build with TrRosetta and Tfold (with attendant predicted distance matrices or distograms that highly resemble each other)––that agree well with more recent AlphaFold2 predictions––are drawn for the human TMEM161B as well as its zebrafish ortholog.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### De novo protein fold design through sequence-independent fragment assembly simulations. (PNAS 2023)

- DOI: 10.1073/pnas.2208275120 | PMCID: PMC9942881 | PMID: 36656852
- Evidence: Analysis of the FoldDesign and Rosetta scaffolds using MD ( A and B ) and protein structure prediction by AlphaFold2 ( C and D ).
- Full pipeline: simulation/modelling [GROMACS] -> machine learning [GROMACS] -> stage not stated [AlphaFold]

### Dimerization of the Alzheimer's disease pathogenic receptor SORLA regulates its association with retromer. (PNAS 2023)

- DOI: 10.1073/pnas.2212180120 | PMCID: PMC9942828 | PMID: 36652482
- Evidence: Structure Modeling with AlphaFold.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> stage not stated [AlphaFold, NAMD, PyMOL]

### <i>Regulator of Awn Elongation 3</i>, an E3 ubiquitin ligase, is responsible for loss of awns during African rice domestication. (PNAS 2023)

- DOI: 10.1073/pnas.2207105120 | PMCID: PMC9942864 | PMID: 36649409
- Evidence: Further, the 3D structure predicted by AlphaFold2 ( 50 ) indicated that OsRAE3 contains a transmembrane domain near the N-terminal region ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> stage not stated [AlphaFold]

### Characterization of a glycan-binding complex of minor pilins completes the analysis of <i>Streptococcus sanguinis</i> type 4 pili subunits. (PNAS 2023)

- DOI: 10.1073/pnas.2216237120 | PMCID: PMC9934059 | PMID: 36626560
- Version used: **2.0**
- Evidence: Modeling was done using AlphaFold 2.2.0 ( 38 ) and AlphaFold-Multimer ( 61 ).
- Full pipeline: stage not stated [AlphaFold v2.0, Coot]

### Similar evolutionary trajectories in an environmental <i>Cryptococcus neoformans</i> isolate after human and murine infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217111120 | PMCID: PMC9926274 | PMID: 36603033
- Version used: **2.1.0**
- Evidence: Protein structure predictions were generated with AlphaFold2 v2.1.0 (reduced BFD database) ( 80 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Bioconductor, Bowtie2 v2.3.5, DESeq2 v1.22.2, GATK, HTSeq v1.99.2, RAxML] -> visualisation [R v3.6] -> stage not stated [AlphaFold v2.1.0, Canu v2.1.1, ImageJ, Medaka]

### Opinion: Protein folds vs. protein folding: Differing questions, different challenges. (PNAS 2023)

- DOI: 10.1073/pnas.2214423119 | PMCID: PMC9910419 | PMID: 36580595
- Evidence: Today, these computational methods have now solved more than 200 million protein structures, which are accessible from the AlphaFold Protein Structure Database ( 5 ) ( https://alphafold.ebi.ac.uk/ ).
- Full pipeline: stage not stated [AlphaFold]

### Mec1 regulates PAS recruitment of Atg13 via direct binding with Atg13 during glucose starvation-induced autophagy. (PNAS 2023)

- DOI: 10.1073/pnas.2215126120 | PMCID: PMC9910460 | PMID: 36574691
- Evidence: Concurrently, docking simulations of the M ec1- B inding R egion (MBR)– A tg13- B inding R egion (ABR) by AlphaFold2 indicated that the Atg13 461–474aa region could readily interact with the 141–160aa region of Mec1( SI Appendix , Fig.
- Full pipeline: simulation/modelling [AlphaFold] -> stage not stated [Fiji, ImageJ]

### Crystal structure of LGR ligand α2/β5 from <i>Caenorhabditis elegans</i> with implications for the evolution of glycoprotein hormones. (PNAS 2023)

- DOI: 10.1073/pnas.2218630120 | PMCID: PMC9910494 | PMID: 36574673
- Evidence: AlphaFold models were predicted by ColabFold ( 64 ) and then relaxed and energy-minimized in the Rosetta suite using the FastDesign protocol ( 65 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [CCP4] -> stage not stated [AlphaFold, ColabFold, PHENIX, PyMOL]

### SARS-CoV-2 accessory proteins ORF7a and ORF3a use distinct mechanisms to down-regulate MHC-I surface expression. (PNAS 2023)

- DOI: 10.1073/pnas.2208525120 | PMCID: PMC9910621 | PMID: 36574644
- Evidence: The model of the full length of ORF7a was generated using AlphaFold ( 66 ).
- Full pipeline: simulation/modelling [NAMD, VMD] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### A structure-based mechanism for initiation of AP-3 coated vesicle formation. (PNAS 2024)

- DOI: 10.1073/pnas.2411974121 | PMCID: PMC11670113 | PMID: 39705307
- Evidence: Certain regions of the initial AlphaFold models were rebuilt manually using Coot ( 64 ) before Rosetta analysis.
- Full pipeline: structure determination [PHENIX v1.21.1] -> stage not stated [AlphaFold]

### Zscan4 mediates ubiquitination and degradation of the corepressor complex to promote chromatin accessibility in 2C-like cells. (PNAS 2024)

- DOI: 10.1073/pnas.2407490121 | PMCID: PMC11670194 | PMID: 39705314
- Evidence: ( G ) Protein – protein interaction docking of the predicted structure of mouse Zscan4c (red) by AlphaFold with the crystal structure of human Hdac1 (magenta), Lsd1 (blue), Kap1-Ring (sand), and Trim25-Ring (green), respectively.
- Full pipeline: stage not stated [AlphaFold, R, ggplot2]

### A minimal complex of KHNYN and zinc-finger antiviral protein binds and degrades single-stranded RNA. (PNAS 2024)

- DOI: 10.1073/pnas.2415048121 | PMCID: PMC11670115 | PMID: 39693345
- Evidence: The predicted model for the KHNYN NYN domain was made with AlphaFold2 ( 44 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, ImageJ]

### Binding site maturation modulated by molecular density underlies Ndc80 binding to kinetochore receptor CENP-T. (PNAS 2024)

- DOI: 10.1073/pnas.2401344121 | PMCID: PMC11670232 | PMID: 39700145
- Evidence: In human CENP-T, AlphaFold3 predicts similar positions for central α-helices within the Spc24/25 groove, although these helices differ by four amino acids, altering their charge and hydrophobicity ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### Proteomic analysis of the sponge Aggregation Factor implicates an ancient toolkit for allorecognition and adhesion in animals. (PNAS 2024)

- DOI: 10.1073/pnas.2409125121 | PMCID: PMC11670116 | PMID: 39693348
- Evidence: We used the identified wreath domain of C. prolifera MAFp3 as an input for the AlphaFold3 web server to predict its tertiary structure [cif file of best-performing model as (Supplement ( 42 ))].
- Full pipeline: read trimming [PyMOL, Trimmomatic] -> stage not stated [AlphaFold, BUSCO, HMMER]

### The C-terminal activating domain promotes pannexin 1 channel opening. (PNAS 2024)

- DOI: 10.1073/pnas.2411898121 | PMCID: PMC11665872 | PMID: 39671183
- Evidence: The AlphaFold model of human Panx1 was used due to missing side chains in the currently available cryo-EM structures.
- Full pipeline: registration [RELION v4.0] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Proteomic characterization of a foraminiferal test's organic matrix. (PNAS 2024)

- DOI: 10.1073/pnas.2417845121 | PMCID: PMC11648905 | PMID: 39642195
- Evidence: These sequences were subject to three-dimensional structural prediction through AlphaFold 3 ( 36 ) using both the protein sequences and a single Zn 2+ cation per each run.
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> stage not stated [PyMOL]

### Structural basis of the allosteric regulation of cyanobacterial glucose-6-phosphate dehydrogenase by the redox sensor OpcA. (PNAS 2024)

- DOI: 10.1073/pnas.2411604121 | PMCID: PMC11648896 | PMID: 39642196
- Evidence: AlphaFold structure predictions of Synechocystis G6PDH and OpcA (Uniprot: P73411 , P73720 , respectively) were manually fitted into the consensus and local-refinement maps.
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [ImageJ]

### The essential role of TTC28 in maintaining chromosomal stability via HSPA8 chaperone-mediated autophagy. (PNAS 2024)

- DOI: 10.1073/pnas.2409447121 | PMCID: PMC11648667 | PMID: 39630868
- Evidence: ( C ) 3D structural image of HSPA8 predicted by AlphaFold (alphafold.ebi.ac.uk).
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### Alternative splicing of &lt;i&gt;Clock&lt;/i&gt; transcript mediates the response of circadian clocks to temperature changes. (PNAS 2024)

- DOI: 10.1073/pnas.2410680121 | PMCID: PMC11648895 | PMID: 39630861
- Evidence: We overlaid an AlphaFold ( 70 ) model of Drosophila CLK-bHLH (aa1-71 of CLK-long including the bHLH domain) to the crystal structure of human CLOCK-BMAL1-DNA ( 71 ) and found plausible contacts between S13 and the negatively charged DNA backbone ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### RAD51 plays critical roles in DNMT1-mediated maintenance methylation of genomic DNA by dually regulating the ubiquitin ligase UHRF1. (PNAS 2024)

- DOI: 10.1073/pnas.2410119121 | PMCID: PMC11648659 | PMID: 39621902
- Evidence: It was reported previously that the UBL domain of UHRF1 contacts the RING domain, resulting in more stable association of the RING with an E2 enzyme and therefore stimulating RING’s E3 activity ( 14 , 15 ), The UHRF1 structure simulated by AlphaFold2 also shows that the UBL contacts the RING ( SI Appendix , Fig.
- Full pipeline: simulation/modelling [AlphaFold]

### Structure of yeast RAVE bound to a partial V&lt;sub&gt;1&lt;/sub&gt; complex. (PNAS 2024)

- DOI: 10.1073/pnas.2414511121 | PMCID: PMC11648922 | PMID: 39625975
- Evidence: The previously published V 1 model 7TMQ ( 16 ) and AlphaFold models of Rav1p, Rav2p, and Skp1p ( 27 ) were fit into the map of RAVE:V 1 ∆C with UCSF Chimera ( 64 ).
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, UCSF Chimera]

### Molecular architecture of synaptic vesicles. (PNAS 2024)

- DOI: 10.1073/pnas.2407375121 | PMCID: PMC11626200 | PMID: 39602275
- Evidence: Predictions of structures of potential candidates for observed densities from the AlphaFold2 ( 22 ) database and a scheme of their membrane localization (the membrane is schematically shown in blue).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> structure determination [IMOD] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, RELION]

### A widespread family of ribosomal peptide metallophores involved in bacterial adaptation to metal stress. (PNAS 2024)

- DOI: 10.1073/pnas.2408304121 | PMCID: PMC11626156 | PMID: 39602266
- Evidence: The AlphaFold2 model predicts that the 68-residue long BufA1 peptide—after removal of the predicted Sec signal peptide—contains a 2-stranded β sheet, some α-helical structure, and a disulfide (S–S) bond between the first β strand and the short α helix ( SI Appendix, Fig.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### Proteome-wide bioinformatic annotation and functional validation of the monotopic phosphoglycosyl transferase superfamily. (PNAS 2024)

- DOI: 10.1073/pnas.2417572121 | PMCID: PMC11626204 | PMID: 39602253
- Evidence: Of the 32,467 sequences in the network, all but 4,585 had predicted structures in the AlphaFold database.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Electrochemical cofactor recycling of bacterial microcompartments. (PNAS 2024)

- DOI: 10.1073/pnas.2414220121 | PMCID: PMC11626177 | PMID: 39585991
- Evidence: The structure for the C. botulinum MNdh-BMC-T SE complex was predicted using AlphaFold multimer ( 40 , 65 ), as distributed in version 2.3.1 of AlphaFold.
- Full pipeline: read trimming [Clustal Omega] -> alignment/mapping [Clustal Omega, RAxML v0.6.0] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Identification of a depupylation regulator for an essential enzyme in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407239121 | PMCID: PMC11626117 | PMID: 39585979
- Evidence: For the initial model of CoaX, we used AlphaFold2 ( 64 ) to generate a monomer of CoaX through ColabFold ( 65 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1, PyMOL, SAMtools v1.13, featureCounts] -> quantification [featureCounts] -> normalisation [DESeq2 v1.40.2, tidyverse v2.0.0] -> differential/statistical testing [DESeq2 v1.40.2, tidyverse v2.0.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### Identification of FBLL1 as a neuron-specific RNA 2'-O-methyltransferase mediating neuronal differentiation. (PNAS 2024)

- DOI: 10.1073/pnas.2406961121 | PMCID: PMC11621510 | PMID: 39570315
- Evidence: ( G ) Catalytic domain structure of human FBLL1 compared with human FBL (FBL, PDB: 7SE6; the structure of FBLL1 was predicted by AlphaFold2).
- Full pipeline: stage not stated [AlphaFold, Metascape]

### Molecular basis for chemokine recognition and activation of XCR1. (PNAS 2024)

- DOI: 10.1073/pnas.2405732121 | PMCID: PMC11621518 | PMID: 39565315
- Evidence: The AlphaFold-predicted structure of XCR1 and structures of G i and scFv16 obtained from the GPR84–G i –scFv16 complex (PDB ID 8G05) were used as initial models for docking into the cryo-EM map using Chimera ( 78 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ColabFold, GROMACS, PyMOL v3.0.3]

### Comprehensive deletion scan of anti-CRISPR AcrIIA4 reveals essential and dispensable domains for Cas9 inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2413743121 | PMCID: PMC11621469 | PMID: 39570312
- Evidence: ColabFold (version 1.5.5) ( 49 ), an open-source version of AlphaFold2 ( 21 ), was used to generate the structural models of AcrIIA4 homologs and deletion alleles through ChimeraX; of the predicted structures for each sequence, the highest confidence structure was used (restricting to relaxed structures for the predicted structures for deletion alleles).
- Full pipeline: differential/statistical testing [R, ggplot2] -> visualisation [PyMOL, R, ggplot2] -> stage not stated [AlphaFold, BLAST, ChimeraX, ColabFold v1.5.5]

### Predicting multiple conformations of ligand binding sites in proteins suggests that AlphaFold2 may remember too much. (PNAS 2024)

- DOI: 10.1073/pnas.2412719121 | PMCID: PMC11621821 | PMID: 39565312
- Evidence: The release of the AlphaFold2 (AF2) and RoseTTafold programs has opened the possibility that such studies can be extended to previously uncharacterized proteins ( 5 – 8 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, PyMOL]

### The RING-type E3 ligase RIE1 sustains leaf longevity by specifically targeting AtACS7 to fine-tune ethylene production in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2411271121 | PMCID: PMC11621758 | PMID: 39565318
- Evidence: AlphaFold predictions.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Identification of a dengue 2 virus envelope protein receptor in &lt;i&gt;Aedes aegypti&lt;/i&gt; critical for viral midgut infection. (PNAS 2024)

- DOI: 10.1073/pnas.2417750121 | PMCID: PMC11621822 | PMID: 39565309
- Evidence: The proteins share 83% identity and 91% homology at the amino acid level and their predicted structures as revealed by AlphaFold ( https://alphafold.ebi.ac.uk/ ) are very similar ( SI Appendix, Fig.
- Full pipeline: stage not stated [AlphaFold]

### &lt;i&gt;KCTD10&lt;/i&gt; p.C124W variant contributes to schizophrenia by attenuating LLPS-mediated synapse formation. (PNAS 2024)

- DOI: 10.1073/pnas.2400464121 | PMCID: PMC11621769 | PMID: 39565307
- Evidence: To assess the structural impact of KCTD10 C124W mutation, we utilized AlphaFold3 and observed that the structure of the KCTD10 C124W variant did not display significant alterations compared to WT KCTD10.
- Full pipeline: stage not stated [AlphaFold]

### MurA-catalyzed synthesis of 5-enolpyruvylshikimate-3-phosphate confers glyphosate tolerance in bryophytes. (PNAS 2024)

- DOI: 10.1073/pnas.2412997121 | PMCID: PMC11588093 | PMID: 39527734
- Evidence: Protein Structure Prediction Using AlphaFold.
- Full pipeline: alignment/mapping [MAFFT] -> visualisation [MAFFT] -> stage not stated [AlphaFold, BLAST, ChimeraX]

### Challenging a decades-old paradigm: ProB and ProA do not channel the unstable intermediate in proline synthesis after all. (PNAS 2024)

- DOI: 10.1073/pnas.2413673121 | PMCID: PMC11573504 | PMID: 39514317
- Evidence: AlphaFold 3 Fails to Predict a Complex between ProB and ProA Capable of Channeling GP.
- Full pipeline: stage not stated [AlphaFold]

### A newborn F-box gene blocks gene flow by selectively degrading phosphoglucomutase in species hybrids. (PNAS 2024)

- DOI: 10.1073/pnas.2418037121 | PMCID: PMC11573670 | PMID: 39514314
- Evidence: ( B ) Top : comparison of AlphaFold2-predicted protein structures for human PGM3, Cni- SHLS-1, and Cbr- SHLS-1.
- Full pipeline: stage not stated [AlphaFold]

### Analysis of the structure and interactions of the SARS-CoV-2 ORF7b accessory protein. (PNAS 2024)

- DOI: 10.1073/pnas.2407731121 | PMCID: PMC11573672 | PMID: 39508769
- Evidence: AlphaFold Predictions.
- Full pipeline: stage not stated [AlphaFold, ChimeraX]

### Identification and characterization of the lipoprotein &lt;i&gt;N&lt;/i&gt;-acyltransferase in &lt;i&gt;Bacteroides&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2410909121 | PMCID: PMC11573676 | PMID: 39495918
- Evidence: While S. aureus LnsA and the periplasmic domain of Lnb have no sequence homology, alignment of their AlphaFold-predicted structures shows significant similarities ( Fig.
- Full pipeline: alignment/mapping [AlphaFold] -> stage not stated [CellProfiler, eggNOG]

### Deciphering the RNA-binding protein network during endosomal mRNA transport. (PNAS 2024)

- DOI: 10.1073/pnas.2404091121 | PMCID: PMC11572963 | PMID: 39499630
- Evidence: ( B ) 3D structural models of the MLLE3 Rrm4 domain, generated using TopModel, AlphaFold, and X-ray as indicated.
- Full pipeline: stage not stated [AlphaFold]

### The structures of protein kinase A in complex with CFTR: Mechanisms of phosphorylation and noncatalytic activation. (PNAS 2024)

- DOI: 10.1073/pnas.2409049121 | PMCID: PMC11573500 | PMID: 39495916
- Evidence: Initial protein models were constructed by fitting published CFTR structures (PDB:5UAK and 6O1V) and AlphaFold 2 PKA models into the cryo-EM maps using UCSF Chimera ( 66 ).
- Full pipeline: structure determination [PHENIX, RELION v4.0] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ImageJ, MotionCor2, UCSF Chimera]

### Structural duality enables a single protein to act as a toxin-antidote pair for meiotic drive. (PNAS 2024)

- DOI: 10.1073/pnas.2408618121 | PMCID: PMC11551426 | PMID: 39485800
- Evidence: Based on the AlphaFold-predicted structure of full-length Tdk1, we have delineated three domains: an N-terminal domain (NTD), an extended stalk domain, and a globular C-terminal domain (CTD).
- Full pipeline: alignment/mapping [minimap2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2]

### A meiotic driver hijacks an epigenetic reader to disrupt mitosis in noncarrier offspring. (PNAS 2024)

- DOI: 10.1073/pnas.2408347121 | PMCID: PMC11551393 | PMID: 39485795
- Evidence: Ribbon representation of the Tdk1 structure predicted by AlphaFold ( 31 , 32 ).
- Full pipeline: stage not stated [AlphaFold]

### A noncanonical GTPase signaling mechanism controls exit from mitosis in budding yeast. (PNAS 2024)

- DOI: 10.1073/pnas.2413873121 | PMCID: PMC11551315 | PMID: 39475649
- Evidence: The observed weak nucleotide preference of Cdc15 is further supported by the AlphaFold2 predicted Cdc15–Tem1 interaction ( 23 ) ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### The conformational landscape of fold-switcher KaiB is tuned to the circadian rhythm timescale. (PNAS 2024)

- DOI: 10.1073/pnas.2412293121 | PMCID: PMC11551320 | PMID: 39475637
- Evidence: Finally, we realize that KaiB interconverts with a fourth previously uncharacterized state which we term the “Enigma state.” We provide evidence from NMR chemical shift predictors that this fourth state is a register-shifted version of the Ground state as predicted by AF-Cluster ( 18 ) and other adaptations of AlphaFold2 (AF2) ( 22 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> stage not stated [ColabFold, SciPy]

### Facilitating and restraining virus infection using cell-attachable soluble viral receptors. (PNAS 2024)

- DOI: 10.1073/pnas.2414583121 | PMCID: PMC11551432 | PMID: 39480852
- Evidence: The CD148 structure was modeled by AlphaFold2.
- Full pipeline: stage not stated [AlphaFold, CellProfiler]

### Adaptive CVgen: Leveraging reinforcement learning for advanced sampling in protein folding and chemical reactions. (PNAS 2024)

- DOI: 10.1073/pnas.2414205121 | PMCID: PMC11551409 | PMID: 39475640
- Evidence: For the WW domain variant GTT protein, whose crystal structure is not cataloged in the PDB database, the reference structure is derived from an AlphaFold2 ( 42 ) prediction, with 2F21 being the closest homolog.
- Full pipeline: dimensionality reduction/clustering [PyMOL, scikit-learn] -> simulation/modelling [OpenMM] -> visualisation [Matplotlib, PyMOL] -> stage not stated [AlphaFold, MDTraj]

### SPATEs promote the survival of &lt;i&gt;Shigella&lt;/i&gt; to the plasma complement system upon local hemorrhage and bacteremia. (PNAS 2024)

- DOI: 10.1073/pnas.2319951121 | PMCID: PMC11551430 | PMID: 39475654
- Evidence: To predict the structure of the passenger domain of S. sonnei SigA, the protein sequence Uniprot-ID: Q3YXF8 (NCBI protein sequence WP_052993189 ) from residue Met56 to Asn1008 was submitted to Colabfold v1.5.2 that implements AlphaFold2.
- Full pipeline: stage not stated [AlphaFold, BLAST, ColabFold, PyMOL v1.8.4]

### A novel &lt;i&gt;N&lt;/i&gt;4,&lt;i&gt;N&lt;/i&gt;4-dimethylcytidine in the archaeal ribosome enhances hyperthermophily. (PNAS 2024)

- DOI: 10.1073/pnas.2405999121 | PMCID: PMC11551388 | PMID: 39471227
- Evidence: The structure was solved by molecular replacement using the polypeptide backbone of an AlphaFold predicted structure as the initial search model.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [AlphaFold]

### Protein language models learn evolutionary statistics of interacting sequence motifs. (PNAS 2024)

- DOI: 10.1073/pnas.2406285121 | PMCID: PMC11551344 | PMID: 39467119
- Evidence: We predicted structure models in AlphaFold2 ( 1 ) using ColabFold ( 30 ); OmegaFold ( 2 ) using the OmegaFold notebook available at https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/beta/omegafold.ipynb ; and ESMFold ( 4 ) using the ESMFold server available at https://esmatlas.com/resources?action=fold .
- Full pipeline: alignment/mapping [PyMOL] -> stage not stated [AlphaFold, ColabFold, SciPy]

### Identification of a divalent metal transporter required for cellular iron metabolism in malaria parasites. (PNAS 2024)

- DOI: 10.1073/pnas.2411631121 | PMCID: PMC11551425 | PMID: 39467134
- Evidence: ( B ) Superposition of predicted AlphaFold structures of H. sapiens DMT1 and PfDMT1.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### O-GlcNAcylation of enolase 1 serves as a dual regulator of aerobic glycolysis and immune evasion in colorectal cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2408354121 | PMCID: PMC11536113 | PMID: 39446384
- Evidence: We analyzed the interaction between ENO1 and PD-L1 based on AlphaFold2 predictions and identified four key residues of ENO1 (N52, K54, K197, and E250) located at the interacting interface with PD-L1 ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### Intrinsically disordered region amplifies membrane remodeling to augment selective ER-phagy. (PNAS 2024)

- DOI: 10.1073/pnas.2408071121 | PMCID: PMC11536123 | PMID: 39453744
- Evidence: We used AlphaFold2 ( https://alphafold.ebi.ac.uk/ ) to obtain an initial structural model for the C–terminal IDR (residues 261 to 497) of FAM134B ( 51 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, CellProfiler, MDAnalysis]

### AlphaFold-Multimer accurately captures interactions and dynamics of intrinsically disordered protein regions. (PNAS 2024)

- DOI: 10.1073/pnas.2406407121 | PMCID: PMC11536093 | PMID: 39446390
- Evidence: To avoid any further overlap with the training set of AlphaFold-Multimer, MMSeqs2 ( 49 ) was used to search for sequence similarities between the dataset and PDB SEQRES sequences released on or before 2018 April 30.
- Full pipeline: machine learning [AlphaFold] -> visualisation [PyMOL] -> stage not stated [ColabFold, Matplotlib, NumPy, RoseTTAFold, SciPy, seaborn]

### Structure and function of &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; EfpA as a lipid transporter and its inhibition by BRD-8000.3. (PNAS 2024)

- DOI: 10.1073/pnas.2412653121 | PMCID: PMC11536138 | PMID: 39441632
- Evidence: The initial structure model for EfpA was predicted using AlphaFold 22 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4, Coot, UCSF Chimera]

### FlaG competes with FliS-flagellin complexes for access to FlhA in the flagellar T3SS to control &lt;i&gt;Campylobacter jejuni&lt;/i&gt; filament length. (PNAS 2024)

- DOI: 10.1073/pnas.2414393121 | PMCID: PMC11536152 | PMID: 39441631
- Evidence: This region of FLAG was predicted by AlphaFold 3 to form a part of an alpha helix following an unstructured region ( 52 ).
- Full pipeline: stage not stated [AlphaFold]

### Optogenetically engineered Septin-7 enhances immune cell infiltration of tumor spheroids. (PNAS 2024)

- DOI: 10.1073/pnas.2405717121 | PMCID: PMC11536090 | PMID: 39441641
- Evidence: We performed structural bioinformatics analysis of septin-7 using the three-dimensional structure predicted by AlphaFold (ID: AF- Q16181 -F1).
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> differential/statistical testing [R v3.5.2] -> simulation/modelling [GROMACS] -> visualisation [Jupyter] -> stage not stated [ImageJ v1.52, PyMOL]

### Interferon lambda 4 is a gut antimicrobial protein. (PNAS 2024)

- DOI: 10.1073/pnas.2409684121 | PMCID: PMC11536128 | PMID: 39436662
- Evidence: Structural predictions of IFNλ4 were made using AlphaFold2, with tertiary structure and surface charge distribution analyzed using PyMOL.
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### Hierarchical assembly and environmental enhancement of bacterial ice nucleators. (PNAS 2024)

- DOI: 10.1073/pnas.2409283121 | PMCID: PMC11513900 | PMID: 39418308
- Evidence: Prediction of the Protein Structures with AlphaFold.
- Full pipeline: stage not stated [AlphaFold]

### Evolutionary origins of the lysosome-related organelle sorting machinery reveal ancient homology in post-endosome trafficking pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2403601121 | PMCID: PMC11513930 | PMID: 39418309
- Evidence: Prediction of BLOC-1 and BORC Using AlphaFold3.
- Full pipeline: quality control [Kraken2] -> read trimming [Kraken2] -> alignment/mapping [ChimeraX] -> stage not stated [AlphaFold, BLAST, BUSCO v5.2.2, HMMER, IQ-TREE, InterProScan, Singularity v3.8]

### Constitutive sodium permeability in a &lt;i&gt;C. elegans&lt;/i&gt; two-pore domain potassium channel. (PNAS 2024)

- DOI: 10.1073/pnas.2400650121 | PMCID: PMC11513965 | PMID: 39405352
- Evidence: We used the AlphaFold database model Q22271 ( 50 ) to model K + /Na + occupancy in the UNC-58 selectivity filter.
- Full pipeline: stage not stated [AlphaFold]

### Folds from fold: Exploring topological isoforms of a single-domain protein. (PNAS 2024)

- DOI: 10.1073/pnas.2407355121 | PMCID: PMC11513978 | PMID: 39405345
- Evidence: The designs with progressively shortened linker lengths were subjected to structure prediction by AlphaFold2 (AF2) ( 14 ) and/or Robetta ( 52 ) (Model S1 and S2).
- Full pipeline: stage not stated [AlphaFold]

### Biochemical and structural insights into a 5' to 3' RNA ligase reveal a potential role in tRNA ligation. (PNAS 2024)

- DOI: 10.1073/pnas.2408249121 | PMCID: PMC11494293 | PMID: 39388274
- Evidence: Interestingly, when we superimposed the AlphaFold ( 34 ) model of human RLIG1 with YspRLIG1 (RMSD of 2.91 Å), YspRLIG1 is missing an N-terminal segment that is found in the human protein (aa.
- Full pipeline: stage not stated [AlphaFold]

### CryoSeek: A strategy for bioentity discovery using cryoelectron microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2417046121 | PMCID: PMC11494351 | PMID: 39382995
- Evidence: While no significant matches were found in experimental databases, numerous bacterial proteins with nearly identical folds were identified in AFDB/Uniprot50, which is a reduced database of AlphaFold2 (AF2)-predicted structures clustered at 50% sequence identity by MMseqs2 ( 21 , 22 ).
- Full pipeline: quality control [MultiQC] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [MotionCor2]

### Engineering substrate channeling in a bifunctional terpene synthase. (PNAS 2024)

- DOI: 10.1073/pnas.2408064121 | PMCID: PMC11474042 | PMID: 39365814
- Evidence: Non-native cyclases CotB2 (purple, PDB 4OMG) and SpS (orange, AlphaFold-3 model less 40 disordered residues at the N terminus) cannot dock to the PaFS PT octamer and hence do not engage in substrate channeling.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX]

### Improved deep learning prediction of antigen-antibody interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2410529121 | PMCID: PMC11474075 | PMID: 39361651
- Evidence: In pursuit of this goal, the remarkable success of AlphaFold 2 (AF2) ( 1 ), originally created to predict the atomic structure of individual proteins, has spurred new developments to predict protein–protein complexes using deep learning ( 2 – 4 ).
- Full pipeline: machine learning [AlphaFold] -> visualisation [VMD]

### Lipopeptide antibiotics disrupt interactions of undecaprenyl phosphate with UptA. (PNAS 2024)

- DOI: 10.1073/pnas.2408315121 | PMCID: PMC11474028 | PMID: 39361645
- Evidence: Insert, the model structure of UptA ( AFO31823 -F1) predicted by AlphaFold ( 22 ).
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### Capturing a methanogenic carbon monoxide dehydrogenase/acetyl-CoA synthase complex via cryogenic electron microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2410995121 | PMCID: PMC11474084 | PMID: 39361653
- Evidence: A starting model of CODH/ACS hexamer was generated using the COSMIC2 implementation ( 73 ) of AlphaFold multimer ( 74 ), which gave correct overall shape at low resolution (maps of 5 Å resolution or lower), but upon experimental visualization of secondary structure via EM density, it was evident that the conformation of CODH/ACS differed significantly from the AlphaFold prediction.
- Full pipeline: structure determination [PHENIX] -> visualisation [AlphaFold] -> stage not stated [ChimeraX, RELION v4.0, cryoDRGN v0.3.4]

### Chemical mapping of the surface interactome of PIEZO1 identifies CADM1 as a modulator of channel inactivation. (PNAS 2024)

- DOI: 10.1073/pnas.2415934121 | PMCID: PMC11474052 | PMID: 39356664
- Evidence: ( A ) Color-coded schematic of human CADM1 within the plasma membrane with the corresponding AlphaFold structure (AF- Q9BY67 -F1) shown top right.
- Full pipeline: stage not stated [AlphaFold]

### Membrane association and polar localization of the &lt;i&gt;Legionella pneumophila&lt;/i&gt; T4SS DotO ATPase mediated by two nonredundant receptors. (PNAS 2024)

- DOI: 10.1073/pnas.2401897121 | PMCID: PMC11474061 | PMID: 39352935
- Evidence: Despite IcmT having no detectable sequence homology to VirB3, AlphaFold ( 60 ) predicts that IcmT may adopt a similar conformation as VirB3 ( SI Appendix , Fig.
- Full pipeline: quantification [ImageJ] -> structure determination [ColabFold] -> stage not stated [AlphaFold]

### Halofilins as emerging bactofilin families of archaeal cell shape plasticity orchestrators. (PNAS 2024)

- DOI: 10.1073/pnas.2401583121 | PMCID: PMC11459167 | PMID: 39320913
- Evidence: Subsequent analysis of the structures predicted by AlphaFold2 ( 38 ) revealed that HalA consists of two bactofilin-like domains arranged head-to-head and connected by an α-helical hairpin (between residues Arg122 and Asp161).
- Full pipeline: stage not stated [AlphaFold, BLAST]

### Unveiling the DHX15-G-patch interplay in retroviral RNA packaging. (PNAS 2024)

- DOI: 10.1073/pnas.2407990121 | PMCID: PMC11459146 | PMID: 39320912
- Evidence: ( H ) AlphaFold model of the PR-GP portion of the M-PMV Pro polyprotein precursor, with PR in cyan and GP in yellow.
- Full pipeline: stage not stated [AlphaFold, SAMtools]

### Alternating access of a bacterial homolog of neurotransmitter: sodium symporters determined from AlphaFold2 ensembles and DEER spectroscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2406063121 | PMCID: PMC11459141 | PMID: 39302996
- Evidence: We utilized SPEACH_AF, an in silico mutagenesis method that leverages AlphaFold2 (AF2) to simulate protein ensembles.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [PyMOL, scikit-learn] -> simulation/modelling [AlphaFold]

### Evolution of pH-sensitive transcription termination in &lt;i&gt;Escherichia coli&lt;/i&gt; during adaptation to repeated long-term starvation. (PNAS 2024)

- DOI: 10.1073/pnas.2405546121 | PMCID: PMC11441560 | PMID: 39298488
- Evidence: Using previous structural data for LysR-type proteins and the AlphaFold predicted structure for YdcI, we mapped the locations of these mutations to specific domains to gain insight into their potential functional impact ( Fig.
- Full pipeline: alignment/mapping [AlphaFold] -> differential/statistical testing [R] -> stage not stated [BLAST, PyMOL]

### Nanomechanics of wild-type and mutant dimers of the inner-ear tip-link protein protocadherin 15. (PNAS 2024)

- DOI: 10.1073/pnas.2404829121 | PMCID: PMC11459131 | PMID: 39298473
- Evidence: We then used AlphaFold2 Colab ( 33 – 37 ) to predict the structures of the EC5 domains in wild-type and V507D molecules.
- Full pipeline: stage not stated [AlphaFold]

### Glial &lt;i&gt;swip-10&lt;/i&gt; controls systemic mitochondrial function, oxidative stress, and neuronal viability via copper ion homeostasis. (PNAS 2024)

- DOI: 10.1073/pnas.2320611121 | PMCID: PMC11441482 | PMID: 39288174
- Evidence: In order to determine whether the 3D structure of the MBD of SWIP-10 has a similar fold to that of MBLAC1, as compared with other members of Group 1 and select members of Group 2, we utilized already available structures and AlphaFold ( 33 ) models, as described in SI Appendix , Supplementary Methods , and performed a structural superimposition of the corresponding MBDs using STAMP ( 34 ) ( Fig.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Structure-based design of a soluble human cytomegalovirus glycoprotein B antigen stabilized in a prefusion-like conformation. (PNAS 2024)

- DOI: 10.1073/pnas.2404250121 | PMCID: PMC11406251 | PMID: 39231203
- Evidence: Initial models of gB Base, 1G2 Fab, and 7H3 Fab were predicted using AlphaFold2 (AF2) ( 50 ) while an initial model of gB-C7 was built with ModelAngelo ( 86 ).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold, PHENIX]

### Time-resolved NMR detection of prolyl-hydroxylation in intrinsically disordered region of HIF-1α. (PNAS 2024)

- DOI: 10.1073/pnas.2408104121 | PMCID: PMC11406255 | PMID: 39231207
- Evidence: This is consistent with the overall structure predicted by AlphaFold 2 ( 37 ), showing that only two short α-helices are present whereas the remainder of the ODD is likely unstructured ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### The &lt;i&gt;SORL1&lt;/i&gt; p.Y1816C variant causes impaired endosomal dimerization and autosomal dominant Alzheimer's disease. (PNAS 2024)

- DOI: 10.1073/pnas.2408262121 | PMCID: PMC11406263 | PMID: 39226352
- Evidence: ...8afp; Growth Hormone Receptor GHR: 2aew; Insulin Receptor IR: 7yq6; Tie2: 5myb), with the exceptions of the Fibronectin (FN) structure, which was the AlphaFold2 prediction (AF- Q6MZF4 -F1-model_v4) and the SORLA ectodomain, which was a model created by us using the AlphaFold2 algorithm (ModelArchive: 10.5452/ma-zgbg4) because the deposited structures from AlphaFold2 of type 1 integral membrane pro...
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### microRNA maintains nutrient homeostasis in the symbiont-host interaction. (PNAS 2024)

- DOI: 10.1073/pnas.2406925121 | PMCID: PMC11388328 | PMID: 39196627
- Evidence: Third, AlphaFold 2 and molecular docking with AutoDock Vina indicated that the MRP4 model had a pLDDT of 82.1 (Values between 70 and 90 mean high confidence) and a TM score of 0.76 (pTM score greater than 0.75 can be interpreted as a reasonable prediction).
- Full pipeline: stage not stated [AlphaFold, AutoDock Vina]

### &lt;i&gt;Prevotella&lt;/i&gt; are major contributors of sialidases in the human vaginal microbiome. (PNAS 2024)

- DOI: 10.1073/pnas.2400341121 | PMCID: PMC11388281 | PMID: 39186657
- Evidence: We found that P. timonensis encodes two sialidases of different lengths ( Pt NanH1 413 amino acids; Pt NanH2 1,030 amino acids) and AlphaFold ( 26 ) structure prediction indicates Pt NanH2 may contain four additional domains of unknown function which are not homologous to structurally characterized protein domains ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [HMMER v3.3.2, MAFFT v7.508, RAxML v8.2.10] -> stage not stated [AlphaFold, InterProScan, Python]

### Gcn2 structurally mimics and functionally repurposes the HisRS enzyme for the integrated stress response. (PNAS 2024)

- DOI: 10.1073/pnas.2409628121 | PMCID: PMC11363354 | PMID: 39163341
- Evidence: AlphaFold Prediction.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Predicting protein conformational motions using energetic frustration analysis and AlphaFold2. (PNAS 2024)

- DOI: 10.1073/pnas.2410662121 | PMCID: PMC11363347 | PMID: 39163334
- Evidence: The successes of AlphaFold2 (AF2) ( 9 ) and RoseTTAFold ( 10 ) in directly generating structure from sequence were made possible by harnessing the evolutionary data.
- Full pipeline: dimensionality reduction/clustering [PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, RoseTTAFold]

### Cowpea lipid transfer protein 1 regulates plant defense by inhibiting the cysteine protease of cowpea mosaic virus. (PNAS 2024)

- DOI: 10.1073/pnas.2403424121 | PMCID: PMC11363299 | PMID: 39159367
- Evidence: We also predicted the interaction between LTP1ΔSP and 24KPro with AlphaFold2.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Identification of a family of peptidoglycan transpeptidases reveals that &lt;i&gt;Clostridioides difficile&lt;/i&gt; requires noncanonical cross-links for viability. (PNAS 2024)

- DOI: 10.1073/pnas.2408540121 | PMCID: PMC11348318 | PMID: 39150786
- Evidence: ( C ) AlphaFold2 models of the YkuD-domain from C. difficile Ldt1 and the VanW domain from Ldt5, with the catalytic triads in color: Cys (red), His (green), Asp (cyan).
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, ColabFold v1.5.5]

### Disorder-to-order active site capping regulates the rate-limiting step of the inositol pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2400912121 | PMCID: PMC11348189 | PMID: 39145930
- Evidence: AlphaFold-multimer, run in a local installation, was used for the predictions of the tetrameric assemblies of fungal (Uniprot ID: G0SDP4) and human MIPS (Uniprot ID: Q9NPH2 ) ( 65 ).
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PyMOL, UCSF Chimera]

### Rtt105 stimulates Rad51-ssDNA assembly and orchestrates Rad51 and RPA actions to promote homologous recombination repair. (PNAS 2024)

- DOI: 10.1073/pnas.2402262121 | PMCID: PMC11348298 | PMID: 39145931
- Evidence: ( A ) Predicted structural model of Rtt105 by AlphaFold 3.
- Full pipeline: stage not stated [AlphaFold]

### An additional proofreader contributes to DNA replication fidelity in mycobacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2322938121 | PMCID: PMC11348249 | PMID: 39141351
- Evidence: The Mtb αε complex model was predicted using AlphaFold Multimer ( 67 ), which had an AlphaFold Model Confidence (pLDDT) value of 88 for almost all residues.
- Full pipeline: variant calling [GATK, SAMtools] -> stage not stated [AlphaFold]

### Microsporidian EnP1 alters host cell H2B monoubiquitination and prevents ferroptosis facilitating microsporidia survival. (PNAS 2024)

- DOI: 10.1073/pnas.2400657121 | PMCID: PMC11348272 | PMID: 39141344
- Evidence: AlphaFold ( 27 ) was utilized to predict the structure and interaction sites of EnP1 and H2B ( SI Appendix , Fig.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Addressing epistasis in the design of protein function. (PNAS 2024)

- DOI: 10.1073/pnas.2314999121 | PMCID: PMC11348311 | PMID: 39133844
- Evidence: Most dramatically, these methods have enabled reliable ab initio structure prediction in widely used methods such as AlphaFold and RoseTTAfold ( 85 , 86 ), prediction of mutation effects and function annotation ( 35 , 83 ), and the design of new proteins, including binders ( 87 ) and enzymes with dozens of mutations from the natural starting point yet with comparable activities ( 34 , 81 , 88 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Insights into the interaction between UGGT, the gatekeeper of folding in the ER, and its partner, the selenoprotein SEP15. (PNAS 2024)

- DOI: 10.1073/pnas.2315009121 | PMCID: PMC11348098 | PMID: 39133860
- Evidence: Materials and Methods AlphaFold2 Predictions.
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### AlphaFold2-based prediction of the co-condensation propensity of proteins. (PNAS 2024)

- DOI: 10.1073/pnas.2315005121 | PMCID: PMC11348322 | PMID: 39133858
- Evidence: The protein encoder takes the intermediate features from AlphaFold2, namely { f msa i },{ f pair ij }, and { f struc i }, as input.
- Full pipeline: stage not stated [AlphaFold]

### Protein folding: From physics-chemical rules and cellular machineries of protein quality control to AI solutions. (PNAS 2024)

- DOI: 10.1073/pnas.2411135121 | PMCID: PMC11348304 | PMID: 39133840
- Evidence: DeepMind’s program AlphaFold ( 5 ) enables scientists to predict the 3D shape of proteins and thus their functions.
- Full pipeline: stage not stated [AlphaFold]

### AlphaFold two years on: Validation and impact. (PNAS 2024)

- DOI: 10.1073/pnas.2315002121 | PMCID: PMC11348012 | PMID: 39133843
- Evidence: However, predictions rarely met the bar for near-experimental quality (a GDT_TS score > 90) before CASP14, when the machine learning system AlphaFold2 (referred in this paper as simply AlphaFold) achieved this level of accuracy on the majority of CASP targets ( 10 , 11 ).
- Full pipeline: stage not stated [AlphaFold, CCP4, ChimeraX, ColabFold, PHENIX, RoseTTAFold]

### Structure-driven development of a biomimetic rare earth artificial metalloprotein. (PNAS 2024)

- DOI: 10.1073/pnas.2405836121 | PMCID: PMC11331073 | PMID: 39116128
- Evidence: An initial structure, which was solved using molecular replacement with a manicured AlphaFold model ( 55 , 56 ), was used as a molecular replacement model for the presented PQQ-bound PqqT and PQQ/Gd 3+ -bound PqqT structures.
- Full pipeline: stage not stated [AlphaFold]

### Structural basis for coupling of the WASH subunit FAM21 with the endosomal SNX27-Retromer complex. (PNAS 2024)

- DOI: 10.1073/pnas.2405041121 | PMCID: PMC11331091 | PMID: 39116126
- Evidence: AlphaFold2 ( 74 ) predictions were performed using the open-source ColabFold pipeline ( 75 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### A DNA condensation code for linker histones. (PNAS 2024)

- DOI: 10.1073/pnas.2409167121 | PMCID: PMC11331069 | PMID: 39116133
- Evidence: While AlphaFold is known to lack predictive power for modeling disordered regions ( 49 ), a prediction [using ColabFold with the default parameters ( 50 )] gave CH1 PA as mostly alpha helix, with a high confidence score, in contrast to CH1 ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Leveraging a large language model to predict protein phase transition: A physical, multiscale, and interpretable approach. (PNAS 2024)

- DOI: 10.1073/pnas.2320510121 | PMCID: PMC11331094 | PMID: 39110734
- Evidence: The files were extracted from the AlphaFold database for the +Droplet drivers and the +Amyloids datasets, as their UniProt accession identifier was provided.
- Full pipeline: machine learning [scikit-learn] -> stage not stated [AlphaFold]

### Leveraging coevolutionary insights and AI-based structural modeling to unravel receptor-peptide ligand-binding mechanisms. (PNAS 2024)

- DOI: 10.1073/pnas.2400862121 | PMCID: PMC11331138 | PMID: 39106311
- Evidence: AlphaFold-Multimer (AFM) is an extension of AlphaFold2 (AF2) developed by DeepMind ( 37 ).
- Full pipeline: stage not stated [AlphaFold, HMMER]

### Molecular mechanism and functional significance of Wapl interaction with the Cohesin complex. (PNAS 2024)

- DOI: 10.1073/pnas.2405177121 | PMCID: PMC11331136 | PMID: 39110738
- Evidence: Protein structure was predicted using AlphaFold2.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Convergent evolution in toxin detection and resistance provides evidence for conserved bacterial-fungal interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2304382121 | PMCID: PMC11317636 | PMID: 39088389
- Evidence: ( E ) Overlay (PyMOL) of GliT X-ray structure (PDB: 4NTC, orange) with the high-confidence PA4170 AlphaFold ( 50 ) predicted structure (Cyan) indicates remarkable structural similarity between these two proteins.
- Full pipeline: read trimming [Bowtie2 v2.4.2] -> alignment/mapping [Bowtie2 v2.4.2, Clustal Omega] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, PyMOL, featureCounts]

### Exploring a unique class of flavoenzymes: Identification and biochemical characterization of ribosomal RNA dihydrouridine synthase. (PNAS 2024)

- DOI: 10.1073/pnas.2401981121 | PMCID: PMC11317573 | PMID: 39078675
- Evidence: To elucidate the structural organization of YhiN, an AlphaFold model was generated ( Fig.
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> visualisation [MUSCLE v5.1] -> stage not stated [AlphaFold]

### An ankyrin G-binding motif mediates TRAAK periodic localization at axon initial segments of hippocampal pyramidal neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2310120121 | PMCID: PMC11295008 | PMID: 39058579
- Evidence: ( A ) AlphaFold predicted model for mouse TRAAK (AF- O88454 -F1).
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [Python v3.9] -> stage not stated [AlphaFold, ImageJ, NumPy, napari]

### Disruption of the ZFP574-THAP12 complex suppresses B cell malignancies in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2409232121 | PMCID: PMC11295075 | PMID: 39047044
- Evidence: AlphaFold ( 16 ) predicted structure of ZFP574 showed that histidine 512, which is part of the 10th zinc finger motif, is positioned in an α-helix and not involved in Zn 2+ binding.
- Full pipeline: stage not stated [AlphaFold]

### Molecular mechanisms of proteoglycan-mediated semaphorin signaling in axon guidance. (PNAS 2024)

- DOI: 10.1073/pnas.2402755121 | PMCID: PMC11295036 | PMID: 39042673
- Evidence: The C-terminal central helix predicted by AlphaFold is shown in green.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ImageJ, Python]

### A ~40-kb flavi-like virus does not encode a known error-correcting mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2403805121 | PMCID: PMC11287256 | PMID: 39018195
- Evidence: The structure of each sequence block was predicted using both ColabFold-AlphaFold2 ( 29 , 30 ) and ESMFold ( 31 ) ( SI Appendix , Fig.
- Full pipeline: read trimming [Cutadapt v1.8.3] -> alignment/mapping [Bowtie2 v2.3.31, MAFFT v7.511, MUSCLE v5.1, Pangolin] -> quantification [RSEM v1.3.0] -> stage not stated [AlphaFold, BLAST v2.0.9, ColabFold, HMMER, IQ-TREE v1.6.12, InterProScan v2.1, SPAdes v3.15.5]

### Mfn2-dependent fusion pathway of PE-enriched micron-sized vesicles. (PNAS 2024)

- DOI: 10.1073/pnas.2313609121 | PMCID: PMC11287154 | PMID: 39012824
- Evidence: The open conformation was established according to the AlphaFold protein structure database ( Q80U63 ) whereas the putative closed conformation is based on structural homology with the crystal structure of the chimeric Mfn1 in the presence of GTP (PDB ID: 5YEW).
- Full pipeline: stage not stated [AlphaFold]

### A broad survey of choanoflagellates revises the evolutionary history of the Shaker family of voltage-gated K&lt;sup&gt;+&lt;/sup&gt; channels in animals. (PNAS 2024)

- DOI: 10.1073/pnas.2407461121 | PMCID: PMC11287247 | PMID: 39018191
- Version used: **2.3.2**
- Evidence: Structural models of SheliKvT1.1-1.3 monomers were generated with AlphaFold v2.3.2 ( 49 ) using default parameters.
- Full pipeline: simulation/modelling [NAMD v2.0] -> stage not stated [AlphaFold v2.3.2, BLAST, VMD v1.9.4a]

### Cell-cell transfer of adaptation traits benefits kin and actor in a cooperative microbe. (PNAS 2024)

- DOI: 10.1073/pnas.2402559121 | PMCID: PMC11287280 | PMID: 39012831
- Evidence: SignalP 6.0 was used to search for signal sequences ( 66 ), while domain homology searches and structure predictions were done with CDD ( 67 ) and AlphaFold2 ( 40 ) web portals, respectively.
- Full pipeline: stage not stated [AlphaFold]

### Conformational dynamics underlying atypical chemokine receptor 3 activation. (PNAS 2024)

- DOI: 10.1073/pnas.2404000121 | PMCID: PMC11287255 | PMID: 39008676
- Evidence: AlphaFold Predictions.
- Full pipeline: stage not stated [AlphaFold, R v3.50]

### FAM110A promotes mitotic spindle formation by linking microtubules with actin cytoskeleton. (PNAS 2024)

- DOI: 10.1073/pnas.2321647121 | PMCID: PMC11260166 | PMID: 38995965
- Evidence: Prediction of Protein Structures by AlphaFold.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [ImageJ] -> stage not stated [AlphaFold, PyMOL]

### Structure of the flotillin complex in a native membrane environment. (PNAS 2024)

- DOI: 10.1073/pnas.2409334121 | PMCID: PMC11260169 | PMID: 38985763
- Evidence: Model Building, Refinement, and Analysis To build the Flotillin model in the high-resolution density map, the structure of the dimer of Flotillin-1 and Flotillin-2 predicted by AlphaFold was fitted into the map using molecular dynamic flexible fitting in ISOLDE ( 62 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [AlphaFold, ChimeraX, PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [ColabFold, Coot]

### Mechanistic insights into phosphoactivation of SLAC1 in guard cell signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2323040121 | PMCID: PMC11260165 | PMID: 38985761
- Evidence: AlphaFold-Based Modeling of SLAC1.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### <i>Caenorhabditis elegans</i> RIG-I-like receptor DRH-1 signals via CARDs to activate antiviral immunity in intestinal cells. (PNAS 2024)

- DOI: 10.1073/pnas.2402126121 | PMCID: PMC11260149 | PMID: 38980902
- Evidence: Materials and Methods The predicted protein structure of DRH-1 was obtained from the AlphaFold Protein Structure Database ( http://alphafold.ebi.ac.uk/ ) ( 24 , 25 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold]

### Control of G protein-coupled receptor function via membrane-interacting intrinsically disordered C-terminal domains. (PNAS 2024)

- DOI: 10.1073/pnas.2407744121 | PMCID: PMC11260148 | PMID: 38985766
- Evidence: MD simulations of an mGluR3 construct containing both TM7 and the CTD (residues 796–879) used initial poses generated using AlphaFold2 ( 75 ) and ColabFold ( 76 ) which were equilibrated using the standard CHARMM-GUI-based protocol and scripts followed by a short, 6-ns run using OpenMM ( 77 ) and the CHARMM36m ( 78 ) forcefield and then simulated for 1,370 ns for each of six replicas.
- Full pipeline: simulation/modelling [AlphaFold, ColabFold, OpenMM]

### Overlapping role of synaptophysin and synaptogyrin family proteins in determining the small size of synaptic vesicles. (PNAS 2024)

- DOI: 10.1073/pnas.2409605121 | PMCID: PMC11260120 | PMID: 38985768
- Evidence: ( A ) AlphaFold protein structures (human full length) and pI (isoelectric point) values of each protein.
- Full pipeline: stage not stated [AlphaFold]

### Data-driven inverse design of flexible pressure sensors. (PNAS 2024)

- DOI: 10.1073/pnas.2320222121 | PMCID: PMC11252744 | PMID: 38954542
- Evidence: Second, the scarcity of data in this emerging field makes data-hungry models (e.g., AlphaFold, ChatGPT) far from the optimal choice.
- Full pipeline: stage not stated [AlphaFold]

### POTRA domains of the TamA insertase interact with the outer membrane and modulate membrane properties. (PNAS 2024)

- DOI: 10.1073/pnas.2402543121 | PMCID: PMC11252910 | PMID: 38959031
- Evidence: ( A ) The TAM machinery is composed of the inner membrane protein TamB (depicted in pink, resembling a spiral conduit based on its AlphaFold structural prediction) and TamA (depicted in red, shown in cartoon representation), which act as a periplasmic ladder and an OMP insertase, respectively ( 7 , 47 ).
- Full pipeline: simulation/modelling [NAMD v2.14] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### An all-atom protein generative model. (PNAS 2024)

- DOI: 10.1073/pnas.2311500121 | PMCID: PMC11228509 | PMID: 38916999
- Evidence: To explore the effect of the diversity of training data on this phenomenon, we trained another model on both CATH and the AlphaFold Protein Structure Database (AFDB) ( 59 ) ( SI Appendix , section C ), and observed that we are able to retain a similar level of generation quality ( Fig.
- Full pipeline: dimensionality reduction/clustering [PyTorch] -> machine learning [AlphaFold] -> stage not stated [PyMOL]

### Pairing interacting protein sequences using masked language modeling. (PNAS 2024)

- DOI: 10.1073/pnas.2311887121 | PMCID: PMC11228504 | PMID: 38913900
- Evidence: A major advance in protein structure prediction was achieved by AlphaFold ( 2 ) and other deep learning approaches ( 3 – 5 ).
- Full pipeline: machine learning [AlphaFold] -> stage not stated [ColabFold]

### APACE: AlphaFold2 and advanced computing as a service for accelerated discovery in biophysics. (PNAS 2024)

- DOI: 10.1073/pnas.2311888121 | PMCID: PMC11228474 | PMID: 38913887
- Evidence: Methods Given that Delta and Polaris’s container support is only available for Apptainer/Singularity ( 39 ), we modified the instructions provided in AlphaFold2 GitHub repository, which are intended for Docker containers ( 40 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, Docker, Singularity, Slingshot]

### Unraveling dynamic protein structures by two-dimensional infrared spectra with a pretrained machine learning model. (PNAS 2024)

- DOI: 10.1073/pnas.2409257121 | PMCID: PMC11228460 | PMID: 38917009
- Evidence: Tools like AlphaFold2 ( 4 , 5 ) and RoseTTAFold ( 6 ) can predict the three-dimensional structures of proteins from their amino acid sequences, while the integration of message passing neural network (MPNN) supplements the predictive capability of protein assemblies ( 8 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold, RoseTTAFold] -> simulation/modelling [GROMACS] -> machine learning [AlphaFold, RoseTTAFold]

### Machine learning meets physics: A two-way street. (PNAS 2024)

- DOI: 10.1073/pnas.2403580121 | PMCID: PMC11228530 | PMID: 38913898
- Evidence: ML and the Protein Folding Problem The paradigmatic example of machine learning solving an important physics problem is the performance of AlphaFold ( 1 ) and its successors in determining protein structure from sequence.
- Full pipeline: stage not stated [AlphaFold]

### Machine learning in biological physics: From biomolecular prediction to design. (PNAS 2024)

- DOI: 10.1073/pnas.2311807121 | PMCID: PMC11228481 | PMID: 38913893
- Evidence: The problem has recently reached a milestone in predictive accuracy with the introduction of AlphaFold2 ( 3 ) and RoseTTAFold ( 59 , 60 ) which owe much of their improvement to transformer-based architectures ( Fig.
- Full pipeline: stage not stated [AlphaFold, ColabFold, RoseTTAFold]

### Insights into stereoselective ring formation in canonical strigolactone: Identification of a dirigent domain-containing enzyme catalyzing orobanchol synthesis. (PNAS 2024)

- DOI: 10.1073/pnas.2313683121 | PMCID: PMC11214005 | PMID: 38905237
- Evidence: QM and molecular dynamics (MD) simulation analysis on a SlSRF model predicted by AlphaFold2.
- Full pipeline: simulation/modelling [AlphaFold]

### Democratizing protein language models with parameter-efficient fine-tuning. (PNAS 2024)

- DOI: 10.1073/pnas.2405840121 | PMCID: PMC11214071 | PMID: 38900798
- Evidence: In 2020, AlphaFold2 ( 27 ), closely followed by RoseTTAFold in 2021 ( 28 ), presented a massive jump in performance, reaching near-experimental levels of accuracy.
- Full pipeline: stage not stated [AlphaFold, PyTorch v2.0.1, RoseTTAFold, scikit-learn v1.2.0]

### Multisubstrate specificity shaped the complex evolution of the aminotransferase family across the tree of life. (PNAS 2024)

- DOI: 10.1073/pnas.2405524121 | PMCID: PMC11214133 | PMID: 38885378
- Version used: **2.1.0**
- Evidence: For the other proteins, homodimeric structure models were generated by AI-based structure prediction using AlphaFold v2.1.0 ( 125 , 126 ).
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [seaborn] -> simulation/modelling [AutoDock Vina v4.2.6] -> stage not stated [AlphaFold v2.1.0, HMMER v3.3.1, RAxML v1.2.0]

### Identification of two archaeal GDGT lipid-modifying proteins reveals diverse microbes capable of GMGT biosynthesis and modification. (PNAS 2024)

- DOI: 10.1073/pnas.2318761121 | PMCID: PMC11214058 | PMID: 38885389
- Evidence: Furthermore, AlphaFold models ( 44 , 45 ) predict that this extension forms a distinct domain and binding pocket that is directly connected to the active site via a tunnel and is lined with hydrophobic residues necessary for binding lipids ( SI Appendix , Figs.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [AlphaFold]

### Structural basis for activation of somatostatin receptor 5 by cyclic neuropeptide agonists. (PNAS 2024)

- DOI: 10.1073/pnas.2321710121 | PMCID: PMC11214081 | PMID: 38885377
- Evidence: The predicted SSTR5 structure from AlphaFold2 was used as the starting reference model for the CST17-SSTR5-G i -scFv16 model building ( 49 ).
- Full pipeline: registration [RELION v4.0] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, R v3.50]

### Elongasome core proteins and class A PBP1a display zonal, processive movement at the midcell of <i>Streptococcus pneumoniae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2401831121 | PMCID: PMC11194595 | PMID: 38875147
- Version used: **2.0**
- Evidence: Structures were modeled using the AlphaFold v2.0 webserver.
- Full pipeline: stage not stated [AlphaFold v2.0]

### Illuminating the coevolution of photosynthesis and Bacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2322120121 | PMCID: PMC11194577 | PMID: 38875151
- Evidence: To gain additional support for the estimated rooting for type I and II reaction centers, a tree spanning both reaction center families based on structural homology was constructed using an all-vs.-all comparison of published structures and a structure of the Vulcanimicrobiota RCII predicted by AlphaFold2-Multimer ( 101 ) using the DALI server ( 61 ).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [IQ-TREE v2.1.3, MAFFT] -> stage not stated [AlphaFold, BEAST v2.6.6, Prokka v1.14]

### Control of biofilm formation by an <i>Agrobacterium tumefaciens</i> pterin-binding periplasmic protein conserved among diverse <i>Proteobacteria</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2319903121 | PMCID: PMC11194511 | PMID: 38870058
- Evidence: AlphaFold predictions suggest that the DcpA periplasmic domain forms an unusual four-helix CACHE-type bundle ( 38 ), with overall structural similarity to the four-helix bundles in the periplasmic domains of methyl-accepting dependent chemotaxis proteins (MCPs), that impart chemotactic motility responses to certain solutes ( 39 ).
- Full pipeline: stage not stated [AlphaFold]

### Hundreds of antimicrobial peptides create a selective barrier for insect gut symbionts. (PNAS 2024)

- DOI: 10.1073/pnas.2401802121 | PMCID: PMC11194567 | PMID: 38865264
- Evidence: Despite their sequence divergence, AlphaFold2 predicted similar folds for tested CCR peptides, consisting of three pairs of β-sheets that are probably connected by cystine bridges ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### <i>Vibrio</i> MARTX toxin processing and degradation of cellular Rab GTPases by the cytotoxic effector Makes Caterpillars Floppy. (PNAS 2024)

- DOI: 10.1073/pnas.2316143121 | PMCID: PMC11194500 | PMID: 38861595
- Evidence: 2 C ). aMCF–Rab complex structures for all 48 Rabs used in the screen were generated using AlphaFold2 and overlaid onto the aMCF CS -ARF3 Q71L complex.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [QuPath] -> dimensionality reduction/clustering [ChimeraX v1.5, ColabFold v1.5.1] -> stage not stated [AlphaFold]

### The molecular architecture of &lt;i&gt;Lactobacillus&lt;/i&gt; S-layer: Assembly and attachment to teichoic acids. (PNAS 2024)

- DOI: 10.1073/pnas.2401686121 | PMCID: PMC11181022 | PMID: 38838019
- Evidence: All predictions were made on an AlphaFold Multimer installation with full databases ( 66 , 67 ) in standard configuration for prokaryotes.
- Full pipeline: stage not stated [AlphaFold, CCP4, ChimeraX, PyMOL]

### Duplication and neofunctionalization of a horizontally transferred xyloglucanase as a facet of the Red Queen coevolutionary dynamic. (PNAS 2024)

- DOI: 10.1073/pnas.2218927121 | PMCID: PMC11181080 | PMID: 38830094
- Evidence: Three-dimensional structures were obtained with Phyre2 (Protein Homology/analogY Recognition Engine v2.0 ( 60 ) or AlphaFold ( 61 , 62 ), using protein sequences without their predicted N-terminal signal peptide [determined using SignalP-6.0 ( 78 )].
- Full pipeline: alignment/mapping [BLAST, Clustal Omega] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Clustal Omega] -> stage not stated [R v4.0.3]

### On the role of native contact cooperativity in protein folding. (PNAS 2024)

- DOI: 10.1073/pnas.2319249121 | PMCID: PMC11145220 | PMID: 38776371
- Evidence: Supplementary Material Appendix 01 (PDF) The three-dimensional structure of proteins is encoded in their sequence, a result first demonstrated by Anfinsen’s refolding experiments on RNase H( 1 ), and which underlies the recent success of AlphaFold and other machine learning approaches to sequence-based protein structure prediction ( 2 , 3 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> differential/statistical testing [MDTraj, SciPy]

### CISD3/MiNT is required for complex I function, mitochondrial integrity, and skeletal muscle maintenance. (PNAS 2024)

- DOI: 10.1073/pnas.2405123121 | PMCID: PMC11145280 | PMID: 38781208
- Evidence: ...l crystal structures to the SBM+DCA predicted complex ( 85 ), protonation and amber minimization ( 86 , 87 ), and protein frustratometer analysis and AlphaFold multimer structure prediction ( 50 , 88 , 89 ) are described in detail in SI Appendix , Materials and Methods .
- Full pipeline: alignment/mapping [HMMER] -> simulation/modelling [GROMACS] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold]

### CRISPRi screens identify the lncRNA, <i>LOUP</i>, as a multifunctional locus regulating macrophage differentiation and inflammatory signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2322524121 | PMCID: PMC11145268 | PMID: 38781216
- Evidence: Structural predictions of the three ORF peptides were determined using AlphaFold, but were mostly of low confidence except for an N-terminal alpha helix in the ORF2 peptide ( 36 ) ( SI Appendix , Fig.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, deepTools] -> stage not stated [AlphaFold, DESeq2]

### Cryo-EM structures elucidate the multiligand receptor nature of megalin. (PNAS 2024)

- DOI: 10.1073/pnas.2318859121 | PMCID: PMC11145282 | PMID: 38771880
- Evidence: We generated fragmentary prediction models of megalin by using AlphaFold2; the models were manually fitted to each multibody-refined map and used as the initial template.
- Full pipeline: registration [Topaz] -> structure determination [AlphaFold, Coot] -> visualisation [ChimeraX] -> stage not stated [RELION v3.1]

### Structure and mechanism of the human CTDNEP1-NEP1R1 membrane protein phosphatase complex necessary to maintain ER membrane morphology. (PNAS 2024)

- DOI: 10.1073/pnas.2321167121 | PMCID: PMC11145253 | PMID: 38776370
- Evidence: A truncated CTDNEP1 AlphaFold ( 30 ) model with B-factors adjustments using Phenix was used as a search model.
- Full pipeline: structure determination [Coot] -> stage not stated [AlphaFold, ImageJ, PHENIX]

### YdbH and YnbE form an intermembrane bridge to maintain lipid homeostasis in the outer membrane of <i>Escherichia coli</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2321512121 | PMCID: PMC11126948 | PMID: 38748582
- Evidence: AlphaFold Structural Predictions.
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### Three-component systems represent a common pathway for extracytoplasmic addition of pentofuranose sugars into bacterial glycans. (PNAS 2024)

- DOI: 10.1073/pnas.2402554121 | PMCID: PMC11127046 | PMID: 38748580
- Evidence: Transmembrane helix prediction was performed using DeepTMHMM ( 64 ) and structural models were made using AlphaFold through the Colabfold notebook ( 65 , 66 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [Clustal Omega, PyMOL v2.5.4] -> stage not stated [AlphaFold]

### SRSF1 interactome determined by proximity labeling reveals direct interaction with spliceosomal RNA helicase DDX23. (PNAS 2024)

- DOI: 10.1073/pnas.2322974121 | PMCID: PMC11126954 | PMID: 38743621
- Evidence: ( B ) AlphaFold prediction of the structure of DDX23 (AF- Q9BUQ8 -F1).
- Full pipeline: visualisation [Cytoscape, STRING db] -> stage not stated [AlphaFold]

### ZEPPI: Proteome-scale sequence-based evaluation of protein-protein interaction models. (PNAS 2024)

- DOI: 10.1073/pnas.2400260121 | PMCID: PMC11127014 | PMID: 38743624
- Evidence: AlphaFold-Multimer ( 12 ) (AFM) has fundamentally changed the landscape of the prediction of structures of multiprotein complexes.
- Full pipeline: alignment/mapping [RoseTTAFold] -> stage not stated [AlphaFold, STRING db]

### <i>Myxococcus xanthus</i> encapsulin cargo protein EncD is a flavin-binding protein with ferric reductase activity. (PNAS 2024)

- DOI: 10.1073/pnas.2400426121 | PMCID: PMC11126975 | PMID: 38748579
- Evidence: A model of EncD T was generated using ColabFold v1.5.3: AlphaFold2 ( 47 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> structure determination [PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, ColabFold v1.5.3, MotionCor2, RELION v4.0]

### Requirements for the biogenesis of [2Fe-2S] proteins in the human and yeast cytosol. (PNAS 2024)

- DOI: 10.1073/pnas.2400740121 | PMCID: PMC11126956 | PMID: 38743629
- Evidence: The protein structure of Apd1 modeled by AlphaFold2 supports the assignment of [2Fe-2S] cluster binding by showing a 2Cys2His binding pocket in the FD2 domain of Apd1 nearly perfectly aligning with the 4Cys [2Fe-2S] cluster-binding site of a bacterial ferredoxin from Azotobacter vinelandii (PDB 5ABR, Fig.
- Full pipeline: alignment/mapping [AlphaFold] -> dimensionality reduction/clustering [AlphaFold]

### The 6-kilodalton peptide 1 in plant viruses of the family Potyviridae is a viroporin. (PNAS 2024)

- DOI: 10.1073/pnas.2401748121 | PMCID: PMC11127057 | PMID: 38739789
- Evidence: AlphaFold2 was used to predict three-dimensional models of 6K1 with default settings ( 54 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> visualisation [PyMOL]

### Targeting the <i>Plasmodium falciparum</i> UCHL3 ubiquitin hydrolase using chemically constrained peptides. (PNAS 2024)

- DOI: 10.1073/pnas.2322923121 | PMCID: PMC11126973 | PMID: 38739798
- Evidence: The docking was then performed on the AlphaFold ( 51 ) model structure of PfUCHL3 protein (Uniprot ID: Q8IKM8 ) and the cyclic peptides.
- Full pipeline: stage not stated [AlphaFold]

### A journey to your self: The vague definition of immune self and its practical implications. (PNAS 2024)

- DOI: 10.1073/pnas.2309674121 | PMCID: PMC11161755 | PMID: 38722806
- Evidence: On the other hand, the conformation-based approach could leverage advanced AI-based algorithms such as AlphaFold, which has been utilized to ascertain the 3D structure of peptide–HLA–TCR complexes ( 71 , 153 ).
- Full pipeline: stage not stated [AlphaFold]

### Three-dimensional architecture of ESCRT-III flat spirals on the membrane. (PNAS 2024)

- DOI: 10.1073/pnas.2319115121 | PMCID: PMC11098116 | PMID: 38709931
- Evidence: The model of Snf7 α0 (residues 2 to 11) was predicted by AlphaFold2 ( 76 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [RELION v3.1] -> stage not stated [AlphaFold, UCSF Chimera]

### A distinct, high-affinity, alkaline phosphatase facilitates occupation of P-depleted environments by marine picocyanobacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2312892121 | PMCID: PMC11098088 | PMID: 38713622
- Evidence: To initially characterize Psip1 we used Phyre2 ( 69 ), SwissModel ( 70 ), CDD Search ( 71 , 72 ), and AlphaFold ( 73 ) through the Google Colab notebook (AlphaFold.ipynb— shorturl.at/asY06 ) using the default options.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.3, MUSCLE v3.8.31] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, HMMER, SciPy v1.10.1]

### A finely balanced order-disorder equilibrium sculpts the folding-binding landscape of an antibiotic sequestering protein. (PNAS 2024)

- DOI: 10.1073/pnas.2318855121 | PMCID: PMC11098121 | PMID: 38709926
- Evidence: ( D ) pLDDT score of the five TipAS models predicted by AlphaFold2.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Structural insights into human MHC-II association with invariant chain. (PNAS 2024)

- DOI: 10.1073/pnas.2403031121 | PMCID: PMC11087810 | PMID: 38687785
- Evidence: The atomic coordinates of the Ii were initially generated by AlphaFold models ( 40 , 41 ).
- Full pipeline: structure determination [ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [AlphaFold]

### Tailored UPRE2 variants for dynamic gene regulation in yeast. (PNAS 2024)

- DOI: 10.1073/pnas.2315729121 | PMCID: PMC11087760 | PMID: 38687789
- Evidence: The Hac1 structure was modeled using AlphaFold2, and the double helical secondary structure of UPRE2m DNA was generated via the website https://scfbio-iitd.res.in/software/drugdesign/bdna.jsp# .
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [Clustal Omega, PyMOL] -> stage not stated [AlphaFold]

### An essential and highly selective protein import pathway encoded by nucleus-forming phage. (PNAS 2024)

- DOI: 10.1073/pnas.2321190121 | PMCID: PMC11087766 | PMID: 38687783
- Evidence: ( E ) AlphaFold predicted structure of PhiKZ gp104 with the experimentally determined recognition region required for nuclear localization shown in yellow.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, ImageJ]

### A general approach for selection of epitope-directed binders to proteins. (PNAS 2024)

- DOI: 10.1073/pnas.2317307121 | PMCID: PMC11087759 | PMID: 38683990
- Evidence: Based on our analysis, we used three simple steps for designing EOI decoys for negative selection: i) define the EOI on the antigen using PDB structures or AlphaFold models of the antigen, ii) prioritize mutating large polar residues (D, E, K, N, Q, and R), preferably in a loop, and iii) mutate 4 to 6 of these to alanine or other small residues that generally are less disruptive to structure.
- Full pipeline: quantification [ImageJ] -> visualisation [ImageJ] -> stage not stated [AlphaFold]

### Frequent nonhomologous replacement of replicative helicase loaders by viruses in <i>Vibrionaceae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2317954121 | PMCID: PMC11087808 | PMID: 38683976
- Evidence: The most closely related protein (identity > 90%, best hit) of VdhL1/2 in uniref100 was determined by DIAMOND ( 69 ), and the corresponding structures were downloaded from the AlphaFold Protein Structure Database ( 70 ).
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT v7.212] -> visualisation [PyMOL, R, ggplot2] -> stage not stated [AlphaFold, BLAST, eggNOG]

### Influence of lipid bilayer on the structure of the muscle-type nicotinic acetylcholine receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2319913121 | PMCID: PMC11087746 | PMID: 38683987
- Evidence: In comparison, the nanodisc MX(γ) is foreshortened (and is better represented by the AlphaFold2 version of this subunit) ( 13 , 14 ).
- Full pipeline: alignment/mapping [CTFFIND, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, MotionCor2, RELION]

### Core planar cell polarity genes <i>VANGL1</i> and <i>VANGL2</i> in predisposition to congenital vertebral malformations. (PNAS 2024)

- DOI: 10.1073/pnas.2310283121 | PMCID: PMC11067467 | PMID: 38669183
- Evidence: To further understand the impact of VANGL variants, we analyzed the three-dimensional VANGL structures predicted by AlphaFold ( SI Appendix , Fig.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [AlphaFold]

### Cryo-EM reveals a nearly complete PCNA loading process and unique features of the human alternative clamp loader CTF18-RFC. (PNAS 2024)

- DOI: 10.1073/pnas.2319727121 | PMCID: PMC11067034 | PMID: 38669181
- Evidence: Based on the density features and the AlphaFold prediction, this density was identified to be a β-hairpin from the N-terminal region of CTF18 ( Fig.
- Full pipeline: stage not stated [AlphaFold, ChimeraX]

### HYPK: A marginally disordered protein sensitive to charge decoration. (PNAS 2024)

- DOI: 10.1073/pnas.2316408121 | PMCID: PMC11067017 | PMID: 38657047
- Evidence: The structures of PKIα and HYPK are predicted by AlphaFold2.
- Full pipeline: stage not stated [AlphaFold]

### Protein engineering a PhotoRNR chimera based on a unifying evolutionary apparatus among the natural classes of ribonucleotide reductases. (PNAS 2024)

- DOI: 10.1073/pnas.2317291121 | PMCID: PMC11067019 | PMID: 38648489
- Evidence: 3 C was constructed by utilizing in silico structural modeling from a local version of Colabfold ( 27 ) that integrates AlphaFold2 ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### The monocyte cell surface is a unique site of autoantigen generation in rheumatoid arthritis. (PNAS 2024)

- DOI: 10.1073/pnas.2304199121 | PMCID: PMC11047081 | PMID: 38630712
- Evidence: Citrullinated proteins in isolated monocyte plasma membranes were identified using mass spectrometry, analyzed via PANTHER, and structures were predicted using AlphaFold.
- Full pipeline: stage not stated [AlphaFold]

### Lipoarabinomannan modification as a source of phenotypic heterogeneity in host-adapted <i>Mycobacterium abscessus</i> isolates. (PNAS 2024)

- DOI: 10.1073/pnas.2403206121 | PMCID: PMC11046677 | PMID: 38630725
- Evidence: The predicted AlphaFold model is shown as cartoon.
- Full pipeline: stage not stated [AlphaFold]

### What one genus of showy moths can say about migration, adaptation, and wing pattern. (PNAS 2024)

- DOI: 10.1073/pnas.2319726121 | PMCID: PMC11047066 | PMID: 38630713
- Evidence: In addition, we mapped U. ornatrix proteins to 3D models of Bombyx mori in the AlphaFold protein structure Database ( 63 ).
- Full pipeline: alignment/mapping [AlphaFold, BUSCO, HMMER, IQ-TREE v1.6.12, MAFFT] -> stage not stated [scikit-learn]

### Identification of an active RNAi pathway in <i>Candida albicans</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2315926121 | PMCID: PMC11047096 | PMID: 38625945
- Evidence: Structural prediction of C. albicans Ago1 was performed using AlphaFold.ipynb–Colaboratory (google.com) and visualized with ChimeraX.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BEDTools, Bowtie2 v2.2.5, HISAT2 v2.2.1] -> differential/statistical testing [DESeq2, R v4.2.2] -> visualisation [AlphaFold, ChimeraX] -> stage not stated [RAxML, StringTie v2.2.1]

### The automated lab of tomorrow. (PNAS 2024)

- DOI: 10.1073/pnas.2406320121 | PMCID: PMC11046582 | PMID: 38630717
- Evidence: They just know that they couldn’t have done it themselves. “It is so far beyond what humans can comprehend, it’s amazing,” he says. “AI and machine learning have completely transformed the field of protein science over the last five years.” Probably the most high-profile project in this fast-growing application of AI is AlphaFold.
- Full pipeline: stage not stated [AlphaFold]

### Structure and dynamics of a pentameric KCTD5/CUL3/Gβγ E3 ubiquitin ligase complex. (PNAS 2024)

- DOI: 10.1073/pnas.2315018121 | PMCID: PMC11047111 | PMID: 38625940
- Evidence: Overall, the structure of the KCTD5 C-terminal tail is consistent with the AlphaFold prediction that shows highly exposed residues from 212 to 221 followed by isolated terminal α-helix ( https://alphafold.ebi.ac.uk/entry/Q9NXV2 ).
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Lipid scrambling is a general feature of protein insertases. (PNAS 2024)

- DOI: 10.1073/pnas.2319476121 | PMCID: PMC11047089 | PMID: 38621120
- Evidence: All proteins simulated in this work were obtained from either the Protein Data Bank ( https://www.rcsb.org/ ) or AlphaFold ( 64 ) predicted models available from UniProt ( https://www.uniprot.org/ ).
- Full pipeline: simulation/modelling [AlphaFold, GROMACS] -> stage not stated [ColabFold]

### Carboxyl-terminal sequences in APOA5 are important for suppressing ANGPTL3/8 activity. (PNAS 2024)

- DOI: 10.1073/pnas.2322332121 | PMCID: PMC11046700 | PMID: 38625948
- Evidence: The structure of APOA5 is unknown, but AlphaFold2 (AF2) models of C-terminal sequences in APOA5 (Q330–P366 in human APOA5; H327–G368 in mouse APOA5) predict an alpha-helical structure.
- Full pipeline: stage not stated [AlphaFold]

### Tight-packing of large pilin subunits provides distinct structural and mechanical properties for the <i>Myxococcus xanthus</i> type IVa pilus. (PNAS 2024)

- DOI: 10.1073/pnas.2321989121 | PMCID: PMC11046646 | PMID: 38625941
- Evidence: Additional Material and Methods information regarding Bioinformatics, Dataset S1 , AlphaFold-Multimer model building, Dataset S2 , AFM tip functionalization and FS, T4aP purification and T4aP shearing assays, T4aP-dependent motility assays, antibodies and immunoblot analysis, transmission electron microscopy, persistence length, and T4aP length determination can be found in SI Appendix , Materials...
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, Coot]

### An energy-conserving reaction in amino acid metabolism catalyzed by arginine synthetase. (PNAS 2024)

- DOI: 10.1073/pnas.2401313121 | PMCID: PMC11032458 | PMID: 38602916
- Evidence: Based on the structure predicted by AlphaFold, these most likely correspond to tetramers and higher assemblies of tetramers.
- Full pipeline: stage not stated [AlphaFold]

### &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; telomere-binding proteins TEBP-1 and TEBP-2 adapt the Myb module to dimerize and bind telomeric DNA. (PNAS 2024)

- DOI: 10.1073/pnas.2316651121 | PMCID: PMC11032478 | PMID: 38588418
- Evidence: Molecular replacement was performed in Phaser ( 37 ) within the PHENIX suite ( 38 ) using the AlphaFold prediction ( 26 ) of the TEBP-2 MCD3 as a search model.
- Full pipeline: alignment/mapping [Clustal Omega, ColabFold] -> structure determination [Coot] -> stage not stated [AlphaFold, PHENIX]

### Structure and design of Langya virus glycoprotein antigens. (PNAS 2024)

- DOI: 10.1073/pnas.2314990121 | PMCID: PMC11032465 | PMID: 38593070
- Evidence: ( B ) AlphaFold2 structure prediction of the LayV G tetrameric stalk.
- Full pipeline: alignment/mapping [Topaz] -> differential/statistical testing [RELION] -> structure determination [PHENIX, RELION] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, ChimeraX]

### NKS1/ELMO4 is an integral protein of a pectin synthesis protein complex and maintains Golgi morphology and cell adhesion in <i>Arabidopsis</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2321759121 | PMCID: PMC11009649 | PMID: 38579009
- Evidence: Protein models were retrieved from the AlphaFold Protein Structure Database and trimmed for disordered regions and transmembrane domains.
- Full pipeline: read trimming [AlphaFold] -> alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [TrackMate]

### Cross-prediction-powered inference. (PNAS 2024)

- DOI: 10.1073/pnas.2322083121 | PMCID: PMC11009639 | PMID: 38568975
- Evidence: This makes sense when considering off-the-shelf models such as AlphaFold.
- Full pipeline: stage not stated [AlphaFold, XGBoost]

### Substrate recruitment via eIF2γ enhances catalytic efficiency of a holophosphatase that terminates the integrated stress response. (PNAS 2024)

- DOI: 10.1073/pnas.2320013121 | PMCID: PMC10998612 | PMID: 38547060
- Evidence: Structure prediction by AlphaFold-multimer.
- Full pipeline: quantification [ImageJ] -> structure determination [GROMACS] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, ChimeraX v1.6.1, Coot v0.9.8.7, PHENIX v1.20.1, PyMOL v1.3]

### Structural and mechanistic basis of the central energy-converting methyltransferase complex of methanogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2315568121 | PMCID: PMC10998594 | PMID: 38530900
- Evidence: A composite model made by aligning the cryo-EM model of (MtrA c BCDEFG) 3 and AlphaFold2 models of MtrBH 2 and MtrA s H 2 is outlined in SI Appendix , Fig.
- Full pipeline: alignment/mapping [AlphaFold] -> stage not stated [CTFFIND, PHENIX, RELION]

### Single-sequence protein structure prediction by integrating protein language models. (PNAS 2024)

- DOI: 10.1073/pnas.2308788121 | PMCID: PMC10990103 | PMID: 38507445
- Evidence: Our results, detailed in SI Appendix , Tables S10 and S11 , emphasize the distinct advantage of MSA-based AlphaFold2 over single-sequence methods, particularly on the more challenging CASP14 dataset.
- Full pipeline: machine learning [PyTorch] -> stage not stated [AlphaFold]

### The disordered C-terminal tail of fungal LPMOs from phytopathogens mediates protein dimerization and impacts plant penetration. (PNAS 2024)

- DOI: 10.1073/pnas.2319998121 | PMCID: PMC10990093 | PMID: 38513096
- Evidence: Both R g values are bigger than the ones expected for folded proteins of the same length, as calculated from Flory’s equation (see experimental section) (19 Å and 23 Å, respectively) and also bigger than the R g computed from the AlphaFold2 models (27.3 Å and 34.1 Å, respectively).
- Full pipeline: stage not stated [AlphaFold, ChimeraX]

### Orphan lysosomal solute carrier MFSD1 facilitates highly selective dipeptide transport. (PNAS 2024)

- DOI: 10.1073/pnas.2319686121 | PMCID: PMC10990142 | PMID: 38507452
- Evidence: A phylogenic Bayesian-based study related MFSD1 to SLC29 nucleoside transporters ( 9 ), while a recent study on structure and evolutionary-based classification of SLCs using the AlphaFold model related MFSD1 to monocarboxylate (SLC16) and sugar-phosphate (SLC37) transporters ( 4 ).
- Full pipeline: differential/statistical testing [AlphaFold]

### Reconstitution of a biofilm adhesin system from a sulfate-reducing bacterium in <i>Pseudomonas fluorescens</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2320410121 | PMCID: PMC10990149 | PMID: 38498718
- Evidence: We employed ColabFold (v1.5.5) to generate structural models of the domains of DvhA using AlphaFold2 with default parameters ( 47 , 48 ).
- Full pipeline: differential/statistical testing [R v4.3.0, ggplot2 v3.4.2] -> visualisation [R v4.3.0, ggplot2 v3.4.2] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL]

### Rapid and automated design of two-component protein nanomaterials using ProteinMPNN. (PNAS 2024)

- DOI: 10.1073/pnas.2314646121 | PMCID: PMC10990136 | PMID: 38502697
- Evidence: Deep learning structure prediction methods such as trRosetta ( 1 ), RoseTTAFold ( 2 ), AlphaFold2 ( 3 ), and ESMfold ( 4 ) quickly and accurately generate models of proteins and protein complexes from amino acid sequences.
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> machine learning [AlphaFold, RoseTTAFold]

### Structural insights reveal interplay between LAG-3 homodimerization, ligand binding, and function. (PNAS 2024)

- DOI: 10.1073/pnas.2310866121 | PMCID: PMC10962948 | PMID: 38483996
- Evidence: The structure was solved by the Molecular Replacement method using various domains of the AlphaFold generated model ( 22 , 23 ).
- Full pipeline: quantification [CellProfiler] -> stage not stated [AlphaFold]

### Structure of RADX and mechanism for regulation of RAD51 nucleofilaments. (PNAS 2024)

- DOI: 10.1073/pnas.2316491121 | PMCID: PMC10962997 | PMID: 38466836
- Evidence: We note that AlphaFold does produce a structural model for monomeric RADX with relatively high confidence for 75% of the protein but was unable to produce a viable structure for a RADX trimer or tetramer.
- Full pipeline: structure determination [PHENIX] -> visualisation [PHENIX] -> stage not stated [AlphaFold]

### Sexual stage-specific A-to-I mRNA editing is mediated by tRNA-editing enzymes in fungi. (PNAS 2024)

- DOI: 10.1073/pnas.2319235121 | PMCID: PMC10962958 | PMID: 38466838
- Evidence: Prediction with AlphaFold2 showed that this C-terminal truncation does not affect the overall catalytic core structure of the FgTad2-FgTad3 heterodimers for tRNA editing, which may explain the normal vegetative growth in the FgTAD2 Q375* mutant.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [featureCounts] -> stage not stated [AlphaFold, Picard]

### Fluorescent proteins generate a genetic color polymorphism and counteract oxidative stress in intertidal sea anemones. (PNAS 2024)

- DOI: 10.1073/pnas.2317017121 | PMCID: PMC10945830 | PMID: 38457522
- Evidence: For structural analysis and modeling we used PyMOL version 2.4.0 and AlphaFold2 ( 48 , 94 ).
- Full pipeline: read trimming [MUSCLE] -> alignment/mapping [MUSCLE] -> quantification [ImageJ] -> stage not stated [AlphaFold, IQ-TREE v1.6.1, PyMOL v2.4.0]

### Context-dependent design of induced-fit enzymes using deep learning generates well-expressed, thermally stable and active enzymes. (PNAS 2024)

- DOI: 10.1073/pnas.2313809121 | PMCID: PMC10945820 | PMID: 38437538
- Evidence: To determine the most structurally invariant anchors across the entire protein fold, we developed an algorithm that creates distance maps for all AlphaFold models of proteins within the same PFam fold ( Fig.
- Full pipeline: stage not stated [AlphaFold, ColabFold, PyTorch]

### Human paraneoplastic antigen Ma2 (PNMA2) forms icosahedral capsids that can be engineered for mRNA delivery. (PNAS 2024)

- DOI: 10.1073/pnas.2307812120 | PMCID: PMC10945824 | PMID: 38437549
- Evidence: A structural model was built for each member of the PNMA family using AlphaFold2 ( 32 ) under the colabfold framework ( 33 ) using default parameters.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, PyMOL, RELION v4.0, Topaz]

### Dual membrane-spanning anti-sigma factors regulate vesiculation in <i>Bacteroides thetaiotaomicron</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2321910121 | PMCID: PMC10927553 | PMID: 38422018
- Evidence: AlphaFold structural predictions were used to confirm genes identified during the blast search.
- Full pipeline: alignment/mapping [RAxML v8.2.12] -> stage not stated [AlphaFold]

### Sec7 regulatory domains scaffold autoinhibited and active conformations. (PNAS 2024)

- DOI: 10.1073/pnas.2318615121 | PMCID: PMC10927569 | PMID: 38416685
- Evidence: The published crystal structure of the DCB-HUS domain and AlphaFold prediction ( 17 , 19 ) were used for guidance with de novo building in the few regions with poor side chain density.
- Full pipeline: alignment/mapping [cryoDRGN] -> structure determination [MotionCor2, PHENIX, RELION v3.1] -> stage not stated [AlphaFold, ChimeraX, ImageJ]

### A billion years of evolution manifest in nanosecond protein dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2318743121 | PMCID: PMC10927572 | PMID: 38412135
- Evidence: The chosen sequences (refer to SI Appendix , Table S1 ) were initially controlled for by predicting their structure using AlphaFold and RosettaFold and aligning them with experimental structures from H. sapiens and M. musculus .
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega, RoseTTAFold] -> stage not stated [ColabFold]

### Tom20 gates PINK1 activity and mediates its tethering of the TOM and TIM23 translocases upon mitochondrial stress. (PNAS 2024)

- DOI: 10.1073/pnas.2313540121 | PMCID: PMC10927582 | PMID: 38416681
- Evidence: Using affinity purification-mass spectrometry in combination with AlphaFold, we identify an interaction between the NT-CTE module of PINK1 and the Tom20 subunit of the TOM complex, which we show is required for PINK1-TOM-TIM23 supercomplex assembly, PINK1 kinase activation, and downstream Parkin-mediated mitophagy.
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold]

### Dinickel enzyme evolved to metabolize the pharmaceutical metformin and its implications for wastewater and human microbiomes. (PNAS 2024)

- DOI: 10.1073/pnas.2312652121 | PMCID: PMC10927577 | PMID: 38408229
- Evidence: ( 60 ), two separate models from the AlphaFold database were used (both 93% seq. id.), A0A2S0XPN7 and A0A316GGX0, to model MfmA and MfmB, respectively ( 61 ).
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> structure determination [CCP4] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, AutoDock Vina]

### Extracellular vesicle formation in <i>Euryarchaeota</i> is driven by a small GTPase. (PNAS 2024)

- DOI: 10.1073/pnas.2311321121 | PMCID: PMC10927574 | PMID: 38408251
- Evidence: Tertiary structure of the OapA dimer was predicted with AlphaFold v2 ( 48 , 52 ).
- Full pipeline: alignment/mapping [MUSCLE] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R] -> stage not stated [AlphaFold, ImageJ]

### Mechanism and cellular function of direct membrane binding by the ESCRT and ERES-associated Ca<sup>2+</sup>-sensor ALG-2. (PNAS 2024)

- DOI: 10.1073/pnas.2318046121 | PMCID: PMC10907313 | PMID: 38386713
- Evidence: AlphaFold2 ( https://alphafold.ebi.ac.uk/ ) was run using the ColabFold notebook ( https://colab.research.google.com/github/sokrypton/ColabFold ) using version v1.5.2 on default settings.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis v2.0] -> stage not stated [AlphaFold, ChimeraX v1.3, ColabFold, ImageJ, OpenCV, PyMOL, Python, scikit-image]

### Inverse regulation of SOS1 and HKT1 protein localization and stability by SOS3/CBL4 in <i>Arabidopsis thaliana</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2320657121 | PMCID: PMC10907282 | PMID: 38386704
- Evidence: The dimeric structure of SOS1 (residues 1 to 697) and the complex SOS3-S3BD (residues 460 to 484) were modeled using the AlphaFold Advanced Interface ( 26 ).
- Full pipeline: stage not stated [AlphaFold]

### Diverse cytomegalovirus US11 antagonism and MHC-A evasion strategies reveal a tit-for-tat coevolutionary arms race in hominids. (PNAS 2024)

- DOI: 10.1073/pnas.2315985121 | PMCID: PMC10907249 | PMID: 38377192
- Evidence: The structure of full-length US11 in complex with HLA-A*02:01 was predicted using AlphaFold Multimer v2.3.2 run on a local server ( 73 , 74 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4]

### Comparative chemical genomics in <i>Babesia</i> species identifies the alkaline phosphatase PhoD as a determinant of antiparasitic resistance. (PNAS 2024)

- DOI: 10.1073/pnas.2312987121 | PMCID: PMC10907312 | PMID: 38377214
- Evidence: The structure of BdPhoD and BbPhoD were predicted using AlphaFold ( 72 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BEDTools, BWA, Clustal Omega, PyMOL v2.3.2, SAMtools, VCFtools] -> dimensionality reduction/clustering [Clustal Omega] -> stage not stated [AlphaFold]

### KAT8-catalyzed lactylation promotes eEF1A2-mediated protein synthesis and colorectal carcinogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2314128121 | PMCID: PMC10895275 | PMID: 38359291
- Evidence: We predicted the structure of eEF1A2K408R mutation using AlphaFold ( SI Appendix , Fig.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [STRING db] -> stage not stated [AlphaFold]

### Structure and function of the Si3 insertion integrated into the trigger loop/helix of cyanobacterial RNA polymerase. (PNAS 2024)

- DOI: 10.1073/pnas.2311480121 | PMCID: PMC10895346 | PMID: 38354263
- Evidence: A model of cyNusG was constructed with the AlphaFold2 gene ( 36 ).
- Full pipeline: stage not stated [AlphaFold, PHENIX]

### The structure of the <i>Caenorhabditis elegans</i> TMC-2 complex suggests roles of lipid-mediated subunit contacts in mechanosensory transduction. (PNAS 2024)

- DOI: 10.1073/pnas.2314096121 | PMCID: PMC10895266 | PMID: 38354260
- Evidence: Based on secondary structure prediction and AlphaFold2 analysis, the TM10 helices of TMC-1 and TMC-2 traverse the lipid bilayer and extend into the cytosol, forming an elongated coil-like structure that spans approximately 70 Å and is evolutionarily conserved from nematodes to humans.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, Coot, UCSF Chimera]

### YfmR is a translation factor that prevents ribosome stalling and cell death in the absence of EF-P. (PNAS 2024)

- DOI: 10.1073/pnas.2314437121 | PMCID: PMC10895253 | PMID: 38349882
- Evidence: YfmR structures for B. subtilis and B. anthracis were generated with AlphaFold ( 55 ).
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.5]

### Fine-tuning activation specificity of G-protein-coupled receptors via automated path searching. (PNAS 2024)

- DOI: 10.1073/pnas.2317893121 | PMCID: PMC10895267 | PMID: 38346183
- Evidence: Given the abundance of resolved inactive and active forms of various GPCRs ( 29 ) and the tremendous progress in structure prediction by AlphaFold2 ( 30 ) or RosettaFold ( 31 ), path methods are particularly suitable for dissecting the activation process between the two states.
- Full pipeline: quantification [AlphaFold, RoseTTAFold]

### Filament structure and subcellular organization of the bacterial intermediate filament-like protein crescentin. (PNAS 2024)

- DOI: 10.1073/pnas.2309984121 | PMCID: PMC10873595 | PMID: 38324567
- Evidence: Coiled coil prediction ( 18 ) and three-dimensional (3D) structure prediction by AlphaFold 2 (AF2) ( 19 ) ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [IMOD, PHENIX] -> machine learning [Topaz] -> stage not stated [Coot, ImageJ, MotionCor2, RELION v3.1]

### CURTAIN-A unique web-based tool for exploration and sharing of MS-based proteomics data. (PNAS 2024)

- DOI: 10.1073/pnas.2312676121 | PMCID: PMC10873628 | PMID: 38324566
- Evidence: ( F ) Predicted AlphaFold structure of SGK3.
- Full pipeline: stage not stated [AlphaFold, PyMOL v2.5.2]

### Molecular basis for human aquaporin inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2319682121 | PMCID: PMC10873552 | PMID: 38319972
- Evidence: Initial AQP3 (AF- Q92482 ) and AQP9 (AF- O43315 ) were taken from the AlphaFold2-EMBL database ( 33 , 34 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### Evolution and diversification of carboxylesterase-like [4+2] cyclases in aspidosperma and iboga alkaloid biosynthesis. (PNAS 2024)

- DOI: 10.1073/pnas.2318586121 | PMCID: PMC10873640 | PMID: 38319969
- Evidence: AlphaFold models of these CXE-like proteins revealed that the catalytic Asp may be positioned outside of the active site, offering one plausible explanation for their poor activity ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Learning the shape of protein microenvironments with a holographic convolutional neural network. (PNAS 2024)

- DOI: 10.1073/pnas.2300838121 | PMCID: PMC10861886 | PMID: 38300863
- Evidence: Despite AlphaFold’s remarkable success at predicting protein folding, it still struggles to determine the effect of mutations on the stability and function of a protein ( 13 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [OpenMM] -> machine learning [OpenMM] -> stage not stated [AlphaFold]

### The ubiquitin E3 ligase BFAR promotes degradation of PNPLA3. (PNAS 2024)

- DOI: 10.1073/pnas.2312291121 | PMCID: PMC10861911 | PMID: 38294943
- Evidence: We then inspected the structure model from AlphaFold ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Loss of activation by GABA in vertebrate delta ionotropic glutamate receptors. (PNAS 2024)

- DOI: 10.1073/pnas.2313853121 | PMCID: PMC10861852 | PMID: 38285949
- Evidence: We investigated this by computationally docking GABA and D-serine to a starfish Aca GluD AlphaFold structural model and the Rat GluD2 X-ray structure ( 13 ).
- Full pipeline: alignment/mapping [MAFFT v7.450] -> visualisation [PyMOL v4.6] -> stage not stated [AlphaFold, AutoDock Vina v4.2, ChimeraX v1.4, ColabFold]

### A novel cysteine-rich adaptor protein is required for mucin packaging and secretory granule stability in vivo. (PNAS 2024)

- DOI: 10.1073/pnas.2314309121 | PMCID: PMC10861859 | PMID: 38285943
- Evidence: ( H ) AlphaFold2 was used to model complex formation between Sgs3 and Sgs7.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Transfer learning to leverage larger datasets for improved prediction of protein stability changes. (PNAS 2024)

- DOI: 10.1073/pnas.2314853121 | PMCID: PMC10861915 | PMID: 38285937
- Evidence: This yielded a final Megascale dataset of 272,712 mutations across 298 proteins, including 181 natural protein domains with structures modeled by AlphaFold, all of which had mean pLDDT > 0.75.
- Full pipeline: stage not stated [AlphaFold]

### Recurrent viral capture of cellular phosphodiesterases that antagonize OAS-RNase L. (PNAS 2024)

- DOI: 10.1073/pnas.2312691121 | PMCID: PMC10835031 | PMID: 38277437
- Evidence: We then conducted a series of overlays of AlphaFold2-predicted structural models of reconstructed PDEs as well as the known Hs AKAP7 PDE structure.
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [AlphaFold] -> stage not stated [ChimeraX]

### Structure of <i>Escherichia coli</i> exonuclease VII. (PNAS 2024)

- DOI: 10.1073/pnas.2319644121 | PMCID: PMC10835039 | PMID: 38271335
- Evidence: An AlphaFold2-predicted ( 24 ) structure of an XseA dimer was converted into a density map by Eman2 ( 35 ), and 2D templates were created from the map to pick particles.
- Full pipeline: structure determination [AlphaFold, ChimeraX v1.4, PHENIX v1.20.1] -> stage not stated [Coot v0.9.6, UCSF Chimera v1.15]

### Methylation of ciliary dynein motors involves the essential cytosolic assembly factor DNAAF3/PF22. (PNAS 2024)

- DOI: 10.1073/pnas.2318522121 | PMCID: PMC10835030 | PMID: 38261620
- Evidence: Model structures for human, rat, mouse, zebrafish, and, in some cases, Drosophila dynein assembly factor proteins generated by AlphaFold2 ( 62 ) were downloaded from UniProt.
- Full pipeline: stage not stated [AlphaFold, ColabFold, PyMOL]

### Computational inference of eIF4F complex function and structure in human cancers. (PNAS 2024)

- DOI: 10.1073/pnas.2313589121 | PMCID: PMC10835048 | PMID: 38266053
- Evidence: We employed the AlphaFold multimer approach, which is an extension of the AlphaFold2 algorithm and is capable of predicting the structure of a protein complex as a single entity ( 48 ).
- Full pipeline: normalisation [UMAP, scikit-learn] -> dimensionality reduction/clustering [UMAP, clusterProfiler, scikit-learn] -> differential/statistical testing [clusterProfiler] -> visualisation [NetworkX, clusterProfiler] -> stage not stated [AlphaFold, ComplexHeatmap, PyMOL, R, RSEM, STRING db, limma]

### Bacterial flagella hijack type IV pili proteins to control motility. (PNAS 2024)

- DOI: 10.1073/pnas.2317452121 | PMCID: PMC10823254 | PMID: 38236729
- Evidence: To gain further support for the idea that these proteins form the cage, we used AlphaFold2 ( 23 , 24 ) to predict the H. pylori PilO, PilN, and PilM structures ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### Tumor resistance to anti-mesothelin CAR-T cells caused by binding to shed mesothelin is overcome by targeting a juxtamembrane epitope. (PNAS 2024)

- DOI: 10.1073/pnas.2317283121 | PMCID: PMC10823246 | PMID: 38227666
- Evidence: The light chain, linker, and heavy chain of the humanized 15B6 and SS1 scFv, modeled by AlphaFold2, are shown in ribbon and surface drawing in light blue, dark gray, blue, pink, dark gray, and red, respectively.
- Full pipeline: stage not stated [AlphaFold]

### Decoupled evolution of the <i>Sex Peptide</i> gene family and <i>Sex Peptide Receptor</i> in Drosophilidae. (PNAS 2024)

- DOI: 10.1073/pnas.2312380120 | PMCID: PMC10801855 | PMID: 38215185
- Evidence: ( B ) The AlphaFold prediction of the structure of D. melanogaster SPR as downloaded from UniProt (AF- Q8SWR3 -F1) and coloured by the domain each residue belongs to based on positions listed in the UniProt “Features” table.
- Full pipeline: alignment/mapping [MAFFT] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### A structurally precise mechanism links an epilepsy-associated <i>KCNC2</i> potassium channel mutation to interneuron dysfunction. (PNAS 2024)

- DOI: 10.1073/pnas.2307776121 | PMCID: PMC10801864 | PMID: 38194456
- Evidence: The structure of human Kv3.2 (residue 7 to 500) was taken from the AlphaFold2 EBI database based on the UniProt sequence ID: Q96PR1 .
- Full pipeline: simulation/modelling [GROMACS v2022.1] -> stage not stated [AlphaFold, PyMOL]

### Structure of a tripartite protein complex that targets toxins to the type VII secretion system. (PNAS 2024)

- DOI: 10.1073/pnas.2312455121 | PMCID: PMC10801868 | PMID: 38194450
- Evidence: Protein complex predictions were performed with Colabfold AlphaFold2 using MMseqs2 locally installed on an HPE Apollo 6500 system running Red Hat Enterprise Linux with Nvidia Quadro RTX 8000 GPUs ( 41 , 42 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX]

### Spartin-mediated lipid transfer facilitates lipid droplet turnover. (PNAS 2024)

- DOI: 10.1073/pnas.2314093121 | PMCID: PMC10801920 | PMID: 38190532
- Evidence: Indeed, AlphaFold2 ( 19 ) predictions for the senescence domains of HsSpartin, CeSpartin, and CtSpartinL differ dramatically despite moderate sequence identities in the domain (24% between HsSpartin and CeSpartin; 28% between HsSpartin and CtSpartinL), suggesting that the predictions are unreliable.
- Full pipeline: stage not stated [AlphaFold, Fiji, ImageJ]

### Gut metabolite L-lactate supports <i>Campylobacter jejuni</i> population expansion during acute infection. (PNAS 2024)

- DOI: 10.1073/pnas.2316540120 | PMCID: PMC10786315 | PMID: 38170751
- Evidence: Structural modeling of LctR with AlphaFold 2 indicated distinct N-terminal and C-terminal domains ( 41 , 44 , 45 ).
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### Protective human antibodies against a conserved epitope in pre- and postfusion influenza hemagglutinin. (PNAS 2024)

- DOI: 10.1073/pnas.2316964120 | PMCID: PMC10769852 | PMID: 38147556
- Evidence: We used AlphaFold2 (AF2) ( 30 ) to prepare a model of EHA2 with the sequence of the B/Malaysia/2506/2004 HA2 ectodomain (residues 23 to 181, H3 numbering) in its postfusion conformation.
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> stage not stated [AlphaFold, ChimeraX, PHENIX]

### ANGPTL4 binds to the leptin receptor to regulate ectopic bone formation. (PNAS 2024)

- DOI: 10.1073/pnas.2310685120 | PMCID: PMC10769826 | PMID: 38147550
- Evidence: The 3D structure of protein LepR ( P48356 -F1-model_v2) and ANGPTL4 (AF- Q9Z1P8 -F1-model_v2) were downloaded from AlphaFold Protein Structure Database ( https://alphafold.ebi.ac.uk/ ).
- Full pipeline: alignment/mapping [PyMOL] -> stage not stated [AlphaFold]

### NPC1 trafficking via VPS41-dependent LAMP carriers regulates endosomal cholesterol homeostasis. (PNAS 2025)

- DOI: 10.1073/pnas.2521979122 | PMCID: PMC12772203 | PMID: 41452985
- Evidence: Materials and Methods All the reagents, antibodies, methods used to generate the genome-engineered cells and their molecular analysis, cell culture, transfection, mitochondrial recruitment assay, AlphaFold analysis, and (immuno)-fluorescence and electron microscopy procedures are described in detail in the extended materials and methods section that is included in SI Appendix .
- Full pipeline: stage not stated [AlphaFold]

### Flexible protein-ligand docking with diffusion-based side-chain packing. (PNAS 2025)

- DOI: 10.1073/pnas.2511925122 | PMCID: PMC12772217 | PMID: 41439702
- Evidence: However, multiple studies have demonstrated that docking accuracy using AlphaFold2-predicted structures remains limited compared with crystal structures ( 34 , 66 ), primarily due to the absence of ligand information and the neglect of protein dynamics.
- Full pipeline: machine learning [Open Babel] -> stage not stated [AlphaFold, AutoDock Vina, RDKit]

### Anellovirus protein encoded by &lt;i&gt;ORF2/3&lt;/i&gt; functions as the viral replication initiation protein. (PNAS 2025)

- DOI: 10.1073/pnas.2516306122 | PMCID: PMC12772153 | PMID: 41433061
- Evidence: AlphaFold Server.
- Full pipeline: alignment/mapping [SAMtools v1.20, StringTie v2.2.3] -> quantification [SAMtools v1.20, StringTie v2.2.3] -> stage not stated [AlphaFold, Conda, fastp v0.23.4]

### Arg-Tyr cation-π interactions drive phase separation and β-sheet assembly in native spider dragline silk. (PNAS 2025)

- DOI: 10.1073/pnas.2523198122 | PMCID: PMC12772222 | PMID: 41433062
- Evidence: Molecular dynamics simulations (1 µs) were conducted using GROMACS with the CHARMM36m force field, and structural models were generated with ColabFold and AlphaFold3.
- Full pipeline: simulation/modelling [AlphaFold, ColabFold, GROMACS]

### Sensing the shape of a surface by tightly surface-bound filaments. (PNAS 2025)

- DOI: 10.1073/pnas.2526131122 | PMCID: PMC12772210 | PMID: 41428884
- Evidence: Moving forward, more accurate biochemical measurements of MreB and protein structural insights provided by cryoelectron microscopy experiments and protein structure prediction tools like AlphaFold ( 43 ) will provide a more comprehensive picture of MreB filament properties.
- Full pipeline: simulation/modelling [VMD] -> stage not stated [AlphaFold]

### Multiplex mapping of protein-protein interaction interfaces. (PNAS 2025)

- DOI: 10.1073/pnas.2425774122 | PMCID: PMC12771567 | PMID: 41428874
- Evidence: Constraining AlphaFold3 Predictions with SpARC-Map Data.
- Full pipeline: machine learning [AlphaFold]

### Structural insights into nonpeptide antagonist inhibition of somatostatin receptor subtype 5. (PNAS 2025)

- DOI: 10.1073/pnas.2522515122 | PMCID: PMC12745778 | PMID: 41417603
- Evidence: For both SSTR5 structures, an AlphaFold3-predicted atomic model served as the initial reference for receptor modeling ( 36 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### Structural insights into human signal peptide peptidase. (PNAS 2025)

- DOI: 10.1073/pnas.2528340122 | PMCID: PMC12745688 | PMID: 41405866
- Evidence: An initial structure model for ligand-free SPPL2a or L685,458-bound SPPL2a was generated using AlphaFold2 (AF- Q8TCT8 -F1-model_v4).
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### DNA methylation shapes transcription factor binding beyond canonical CpG contexts. (PNAS 2025)

- DOI: 10.1073/pnas.2520814122 | PMCID: PMC12745676 | PMID: 41405863
- Evidence: ( D ) AlphaFold3-based structural comparison of FoxA2 bound to DNA with either 5mC or unmethylated cytosine at position 7.
- Full pipeline: differential/statistical testing [R v4.2.2] -> stage not stated [AlphaFold]

### Physical exercise increases binding of POMC to blood extracellular vesicles. (PNAS 2025)

- DOI: 10.1073/pnas.2525044122 | PMCID: PMC12745691 | PMID: 41400998
- Evidence: Since the experimental structure of full-length human POMC was not available, the 3D model was retrieved from the AlphaFold repository ( 62 ) (AF- P01189 -F1) and used as 3D structural coordinates.
- Full pipeline: stage not stated [AlphaFold, GROMACS v2021.3, R v4.3]

### Cryo-EM structure of the Rift Valley fever virus envelope protein in complex with a potent neutralization antibody. (PNAS 2025)

- DOI: 10.1073/pnas.2514862122 | PMCID: PMC12745785 | PMID: 41401007
- Evidence: Structures of the full-length Gn and Gc, and the Fab of RVFV-140 were predicted by using AlphaFold ( 41 ), and were used as references for model building.
- Full pipeline: structure determination [Coot, PHENIX, RELION] -> stage not stated [AlphaFold, ChimeraX]

### An abundant membrane protein in the NCAM superfamily is required for epithelial organization in sea anemone embryos. (PNAS 2025)

- DOI: 10.1073/pnas.2521737122 | PMCID: PMC12745706 | PMID: 41400995
- Evidence: Extensive descriptions of all procedures, including biotinylation and isolation of surface proteins, mass spectrometry and data acquisition, embryo manipulations, immunohistochemistry, imaging, image analysis, and AlphaFold predictions are included in SI Appendix , Materials and Methods .
- Full pipeline: stage not stated [AlphaFold]

### SPNS1 is an essential cellular factor for EV-A71 by acting as a transporter of viral pocket factor. (PNAS 2025)

- DOI: 10.1073/pnas.2510020122 | PMCID: PMC12718360 | PMID: 41385544
- Evidence: Molecular docking was performed into the sphingosine-binding pocket of SPNS1 with AlphaFold 3, suggesting that conserved residues, such as R76 and H427, are involved in sphingosine recognition.
- Full pipeline: stage not stated [AlphaFold]

### CDCA7 facilitates MET1-mediated CG DNA methylation maintenance in centromeric heterochromatin via linker histone H1. (PNAS 2025)

- DOI: 10.1073/pnas.2526408122 | PMCID: PMC12718391 | PMID: 41370347
- Evidence: AlphaFold Prediction.
- Full pipeline: alignment/mapping [Bismark v0.19.1, Clustal Omega, STAR v2.7.11a] -> quantification [HTSeq v0.13.5] -> differential/statistical testing [DESeq2 v1.42.0] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Picard, Trim Galore v0.6.7, deepTools v3.0.2]

### Molecular mechanisms underlying p62-dependent secretion of the Alzheimer-associated ubiquitin variant UBB&lt;sup&gt;+1&lt;/sup&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504528122 | PMCID: PMC12718301 | PMID: 41364760
- Evidence: AlphaFold-Based Modeling of UBB +1 –p62 UBA Interaction.
- Full pipeline: visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, ColabFold]

### An electron transport complex required in the gut sensitizes &lt;i&gt;Bacteroides&lt;/i&gt; to a pore-forming type VI secretion toxin. (PNAS 2025)

- DOI: 10.1073/pnas.2523503122 | PMCID: PMC12718326 | PMID: 41364769
- Evidence: AlphaFold3 was used to predict the structure of the multimeric Rnf complex from B. theta ( 69 ).
- Full pipeline: alignment/mapping [ChimeraX v10.1] -> dimensionality reduction/clustering [ChimeraX v10.1] -> stage not stated [AlphaFold, Python]

### Structural basis and evolutionary pathways of glycerol-1-phosphate transport in marine bacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2524546122 | PMCID: PMC12718374 | PMID: 41364767
- Evidence: The crystal structure of the GpxB DSM11874 –G1P complex was determined by molecular replacement using a CCP4 program Phaser ( 38 ) with the structure of GpxB DSM11874 generated by AlphaFold2 ( 39 ) as the search model.
- Full pipeline: quantification [HMMER] -> normalisation [HMMER] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4]

### Genetics of prelingual isolated deafness and Usher syndrome in the Maghreb and Jordan: Harnessing the potential of homozygosity. (PNAS 2025)

- DOI: 10.1073/pnas.2518445122 | PMCID: PMC12718389 | PMID: 41359850
- Evidence: The normal 3D structures of the regions carrying these mutations have been established by X-ray crystallography (12/20) or predicted by AlphaFold2 (7/20) (for local confidence of AlphaFold2, see SI Appendix , Methods ).
- Full pipeline: stage not stated [AlphaFold]

### Multiple weak brakes act in concert to control STIM1 and store-operated calcium entry. (PNAS 2025)

- DOI: 10.1073/pnas.2518622122 | PMCID: PMC12718381 | PMID: 41359834
- Evidence: Generating Structural Models with AlphaFold2.
- Full pipeline: stage not stated [AlphaFold, ColabFold, ImageJ, Python]

### Galectin-related protein, a key contributor, drives diabetes-associated neuropathic pain. (PNAS 2025)

- DOI: 10.1073/pnas.2527641122 | PMCID: PMC12718390 | PMID: 41359849
- Evidence: To determine the specific binding site of LGALSL on vimentin, we generated protein–protein docking models using the AlphaFold 3 server.
- Full pipeline: stage not stated [AlphaFold]

### A ferritin-like diiron oxygenase BioE initiates bacterial biotin synthesis, a promising antivirulence target. (PNAS 2025)

- DOI: 10.1073/pnas.2501226122 | PMCID: PMC12704756 | PMID: 41343663
- Evidence: Using AlphaFold3 and SWISS-MODEL, we prepared structural models of Em BioE (BBD33_16475) and Ci BioE (CEQ15_06550).
- Full pipeline: stage not stated [AlphaFold]

### Structural modeling reveals the allosteric switch controlling the chitin utilization program of &lt;i&gt;&lt;i&gt;Vibrio cholerae&lt;/i&gt;&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2523358122 | PMCID: PMC12704726 | PMID: 41343673
- Evidence: Methods Structural Modeling with AlphaFold.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, ColabFold, RoseTTAFold]

### Origin and adaptive evolutionary trajectory of the 3' UTR-derived sRNA UhpU in Enterobacteriaceae. (PNAS 2025)

- DOI: 10.1073/pnas.2513802122 | PMCID: PMC12704781 | PMID: 41343676
- Evidence: Predicted UhpU binding sites from IntaRNA (blue) and AlphaFold3 (green) are shown relative to the UhpU-L +1 site and the mprA start codon (underlined).
- Full pipeline: stage not stated [AlphaFold]

### Widespread promiscuous alkaline phosphatases underscore ancient microbial phosphite utilization. (PNAS 2025)

- DOI: 10.1073/pnas.2513042122 | PMCID: PMC12704751 | PMID: 41343678
- Evidence: Structures of other PhoAs were estimated using AlphaFold 2.
- Full pipeline: stage not stated [AlphaFold, Clustal Omega]

### Versatile NTP recognition and domain fusions expand the functional repertoire of the ParB-CTPase fold beyond chromosome segregation. (PNAS 2025)

- DOI: 10.1073/pnas.2527592122 | PMCID: PMC12704722 | PMID: 41343662
- Evidence: Neither Sequence Analysis Nor AlphaFold3 Currently Provides Reliable Predictions of Nucleotide Specificity.
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [AlphaFold, AutoDock Vina, Docker, HMMER v3.4, IQ-TREE]

### RAD51AP1 is a versatile RAD51 modulator. (PNAS 2025)

- DOI: 10.1073/pnas.2514728122 | PMCID: PMC12704761 | PMID: 41337480
- Evidence: Models of 6 RAD51 protomers with ssDNA, ATP or ADP, Ca 2+ or Mg 2+ and RAD51AP1 C29 as appropriate were modeled in AlphaFold ( 36 ) and docked into the maps as rigid bodies.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2]

### Torque-generating units of the bacterial flagellar motor are rotary motors. (PNAS 2025)

- DOI: 10.1073/pnas.2515291122 | PMCID: PMC12704724 | PMID: 41337489
- Evidence: AlphaFold prediction of Venus barrel orientations in (Venus-MotB) 2 .
- Full pipeline: stage not stated [AlphaFold]

### Machine learning enables de novo multiepitope design of &lt;i&gt;Plasmodium falciparum&lt;/i&gt; circumsporozoite protein to target trimeric L9 antibody. (PNAS 2025)

- DOI: 10.1073/pnas.2512358122 | PMCID: PMC12704715 | PMID: 41337490
- Evidence: Upon completing the iterative design steps of the pipeline, the top 20 refined designs for each backbone by weighted score as predicted by ESMFold were also predicted using AlphaFold 2 (AF2) ( 35 ) ( SI Appendix , Fig.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2023.2] -> structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX, PyMOL, RELION v5.0]

### Structure of human green cone opsin yields insights into mechanisms underlying the rapid decay of its active, signaling state. (PNAS 2025)

- DOI: 10.1073/pnas.2516318122 | PMCID: PMC12704717 | PMID: 41329744
- Evidence: AlphaFold model of active-state human green cone opsin ( 73 ) and heterotrimeric G proteins and scFv16 from PDB:7P00 ( 74 ) were used as the starting reference models.
- Full pipeline: alignment/mapping [ChimeraX] -> stage not stated [AlphaFold]

### The human endogenous retroviral envelope HEMO protein interacts with BACE2: Novel partnership acquired in the primate lineage. (PNAS 2025)

- DOI: 10.1073/pnas.2515527122 | PMCID: PMC12704712 | PMID: 41329733
- Evidence: ...Layer Interferometry (BLI), RNAseq analysis, Immunohistochemistry assays, Cell–cell interaction assay (Cell-Int), and Disulfide bond prediction using AlphaFold3 are detailed in SI Appendix , SI Methods .
- Full pipeline: stage not stated [AlphaFold]

### Glycoside hydrolase-mediated glucomannan catabolism in &lt;i&gt;Segatella copri&lt;/i&gt;, a target of microbiota-directed foods for malnourished children. (PNAS 2025)

- DOI: 10.1073/pnas.2521522122 | PMCID: PMC12704710 | PMID: 41329729
- Evidence: The right portion of the panel presents an AlphaFold predicted structure without the signal peptide.
- Full pipeline: quality control [DESeq2, kallisto] -> alignment/mapping [DESeq2, kallisto] -> differential/statistical testing [DESeq2, kallisto] -> stage not stated [AlphaFold, GSEA, fgsea]

### ROPGAP3 interacts with PIN2 and modulates its clustering and trafficking in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2517205122 | PMCID: PMC12685110 | PMID: 41296733
- Version used: **2.3.1**
- Evidence: AlphaFold v2.3.1 algorithm ( 31 ) was used to predict 3-dimensional structure of ROPGAP3.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [AlphaFold v2.3.1]

### SUPPRESSOR OF LAZY QUADRUPLE 1 acts at ER-plasma membrane contact sites to control a gravitropism pathway in the &lt;i&gt;Arabidopsis&lt;/i&gt; stem. (PNAS 2025)

- DOI: 10.1073/pnas.2510934122 | PMCID: PMC12685104 | PMID: 41296727
- Evidence: The structural modeling of SLQ1 protein was performed using AlphaFold2 with default setting ( 75 ).
- Full pipeline: stage not stated [AlphaFold, ChimeraX, ImageJ]

### Small siphophage binding to an open state of the LptDE outer membrane lipopolysaccharide translocon. (PNAS 2025)

- DOI: 10.1073/pnas.2516650122 | PMCID: PMC12685063 | PMID: 41296721
- Evidence: Structural models were generated using AlphaFold3 ( 38 ) and fit into cryo-EM density maps using UCSF ChimeraX ( 51 ).
- Full pipeline: alignment/mapping [PyMOL] -> quantification [ImageJ] -> simulation/modelling [GROMACS] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [Coot, MDAnalysis, MDTraj]

### Probing direct interactions between nuclear proteins in cells with nxReLo. (PNAS 2025)

- DOI: 10.1073/pnas.2518711122 | PMCID: PMC12685051 | PMID: 41296720
- Evidence: AlphaFold Structure Prediction.
- Full pipeline: visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### Engineered calcium-regulated affinity protein for efficient internalization and lysosomal toxin delivery. (PNAS 2025)

- DOI: 10.1073/pnas.2509081122 | PMCID: PMC12685030 | PMID: 41289384
- Evidence: The structure of CaRA EGFR in complex with the soluble domain of EGFR in presence of Ca 2+ was predicted using AlphaFold 3 using the AlphaFold Server.
- Full pipeline: structure determination [ChimeraX v1.9, PHENIX v1.21.2] -> visualisation [ChimeraX v1.9, PHENIX v1.21.2] -> stage not stated [AlphaFold, NumPy, OpenCV, Python, SciPy, scikit-image]

### Redox regulation of memory formation by Rrp1 in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2507018122 | PMCID: PMC12685121 | PMID: 41289397
- Evidence: Structural predictions using AlphaFold2 ( 25 ) showed close alignment between the Rrp1 C-terminal core and APE1’s experimental structure (PDB: 1HD7) ( 26 ), while the N-terminal region (residues 1 to 414) forms a random coil, resembling the unstructured APE1 N terminus ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [AlphaFold]

### Inhibition of ice recrystallization with designed twistless helical repeat proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2514871122 | PMCID: PMC12685108 | PMID: 41289379
- Evidence: Subsequently, structures were predicted from the designed sequences using both AlphaFold2 ( 25 ) and RoseTTAFold ( 26 ).
- Full pipeline: alignment/mapping [PyMOL] -> normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ImageJ, RoseTTAFold]

### Modulation of the PGRMC1/NLRP7/HLA-C axis by autophagy is linked to both spontaneous preterm birth and gestational choriocarcinoma. (PNAS 2025)

- DOI: 10.1073/pnas.2509798122 | PMCID: PMC12685102 | PMID: 41284890
- Evidence: ( A ) Protein structures of NLRP7 and NLRP2 (derived from AlphaFold).
- Full pipeline: stage not stated [AlphaFold]

### Dimeric gold nanoparticles enable multiplexed labeling in cryoelectron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2524034122 | PMCID: PMC12685141 | PMID: 41284882
- Evidence: Using the GluN1/2A density maps, the GluN1/2A structure (PDB: 6MMP) ( 31 ), the AlphaFold-predicted 5F11 Fab, and an AuNP template, we constructed a model of the receptor complexed with two Fab-dimeric AuNPs ( Fig.
- Full pipeline: structure determination [AlphaFold, IMOD] -> stage not stated [Python]

### DDHD2 possesses both lipase and transacylase capacities that remodel triglyceride acyl chains. (PNAS 2025)

- DOI: 10.1073/pnas.2500527122 | PMCID: PMC12663969 | PMID: 41264248
- Evidence: Prior studies had identified DDHD2 as a serine hydrolase and AlphaFold ( 50 ) predicted DDHD2 to contain a catalytic triad consisting of serine, histidine, and aspartic acid residues, identical to the catalytic triad of canonical serine proteases whose mechanism is well described ( 51 , 52 ).
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Joubert syndrome 26 protein enforces compartmentalized motility of a ciliary kinesin. (PNAS 2025)

- DOI: 10.1073/pnas.2504374122 | PMCID: PMC12663925 | PMID: 41264249
- Evidence: The structural data for JBTS-26 were obtained from the AlphaFold Protein Structure Database (ID: AF- O44770 -F1-v4).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [FastQC] -> stage not stated [AlphaFold, ImageJ, SnpEff, freebayes v1.3.6]

### A periplasmic zinc capture protein enhances the resistance of &lt;i&gt;Neisseria gonorrhoeae&lt;/i&gt; to nutritional immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2426176122 | PMCID: PMC12663993 | PMID: 41259141
- Evidence: Bioinformatic analyses were performed using EFI-EST, MEME Suite, and AlphaFold.
- Full pipeline: stage not stated [AlphaFold]

### A tripartite protein complex promotes DNA transport during natural transformation in Firmicutes. (PNAS 2025)

- DOI: 10.1073/pnas.2511180122 | PMCID: PMC12663950 | PMID: 41259146
- Evidence: All structural models were obtained using the AlphaFold3 ( 32 ) web server and visualized using the ChimeraX ( 57 ) software.
- Full pipeline: alignment/mapping [ColabFold, MAFFT] -> visualisation [AlphaFold, ChimeraX]

### The lactate sensor NDRG3 decelerates ER-to-Golgi transport through interaction with the long isoform of syntaxin-5. (PNAS 2025)

- DOI: 10.1073/pnas.2511307122 | PMCID: PMC12663949 | PMID: 41252154
- Evidence: Structural information about the N- and C-terminal domains is missing, likely due to an increased flexibility of these protein regions ( 12 ), which is also supported by AlphaFold and low per-residue model confidence scores (pLDDT; https://alphafold.ebi.ac.uk/entry/Q9UGV2 ).
- Full pipeline: stage not stated [AlphaFold]

### Structural basis for Lamassu-based antiviral immunity and its evolution from DNA repair machinery. (PNAS 2025)

- DOI: 10.1073/pnas.2519643122 | PMCID: PMC12663957 | PMID: 41252147
- Evidence: We used AlphaFold3 ( 51 ) with a fixed stoichiometry deduced from the nMS data and cryo-EM structures for comparative structural studies.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX v1.9, UCSF Chimera] -> stage not stated [AlphaFold]

### The function of Mak16 in ribosome biogenesis depends on its [4Fe-4S] cluster. (PNAS 2025)

- DOI: 10.1073/pnas.2513844122 | PMCID: PMC12646323 | PMID: 41231949
- Evidence: Structural predictions from AlphaFold2 show high agreement with cryo-EM data for the N-terminal and central domains.
- Full pipeline: stage not stated [AlphaFold]

### Biomolecular condensation of ERC1 recruits ATG8 and NBR1 to drive autophagosome formation for plant heat tolerance. (PNAS 2025)

- DOI: 10.1073/pnas.2425689122 | PMCID: PMC12646234 | PMID: 41213015
- Evidence: ( D ) Predicted aligned error (PAE) plot for the ERC1–ATG8e interaction predicted by AlphaFold.
- Full pipeline: alignment/mapping [AlphaFold]

### GH25 lysozyme mediates tripartite interkingdom interactions and microbial competition on the plant leaf surface. (PNAS 2025)

- DOI: 10.1073/pnas.2510124122 | PMCID: PMC12626018 | PMID: 41201826
- Evidence: ( C ) 3-D structures of GH25 orthologues obtained by AlphaFold 3 and visualized by pyMOL, showing active site motif (yellow) in the center.
- Full pipeline: alignment/mapping [MAFFT] -> visualisation [AlphaFold] -> stage not stated [ImageJ v1.53K, Python]

### MDFIC2 is a PIEZO channel modulator that can alleviate mechanical allodynia associated with neuropathic pain. (PNAS 2025)

- DOI: 10.1073/pnas.2512426122 | PMCID: PMC12626003 | PMID: 41201821
- Evidence: AlphaFold was accessed at https://alphafold.ebi.ac.uk/ and PyMOL version 3.04 (PyMOL Molecular Graphics System) at https://www.pymol.org/ .
- Full pipeline: stage not stated [AlphaFold, PyMOL v3.04]

### Creating a large designer cellulosome in yeast to boost ethanol production. (PNAS 2025)

- DOI: 10.1073/pnas.2517490122 | PMCID: PMC12625909 | PMID: 41201822
- Evidence: To predict the 3D structures of each protein construct, all the protein sequences were sent to the Colab AlphaFold2 server for 3D structure prediction.
- Full pipeline: stage not stated [AlphaFold]

### Extracellular nanobody screening using conformationally stable GPCR variants. (PNAS 2025)

- DOI: 10.1073/pnas.2508879122 | PMCID: PMC12625997 | PMID: 41187083
- Evidence: M1R-G 11 CT was engineered through an integrative computational design approach including RFdiffusion, ProteinMPNN, and AlphaFold2-Multimer ( 47 – 49 ), following the protocol previously employed for click fusion protein (Clip) design ( 33 ).
- Full pipeline: structure determination [ChimeraX] -> stage not stated [AlphaFold, MACS2, PHENIX]

### Modeling protein-small molecule conformational ensembles with PLACER. (PNAS 2025)

- DOI: 10.1073/pnas.2427161122 | PMCID: PMC12625923 | PMID: 41187076
- Evidence: We evaluated PLACER’s docking performance against AlphaFold3 ( 12 ) and RF All-Atom ( 11 ) using the 428 protein–ligand complexes from the PoseBusters benchmark (as implemented in the 2023 preprint) ( 26 ).
- Full pipeline: stage not stated [AlphaFold, Open Babel, RoseTTAFold]

### Conformational regulation of two essential activators of bacterial cell elongation. (PNAS 2025)

- DOI: 10.1073/pnas.2514198122 | PMCID: PMC12625996 | PMID: 41183199
- Evidence: The method searches the PDB to extend two helices of MreD (AlphaFold prediction), onto which BRIL is superimposed.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, Coot]

### From sequence to scaffold: Computational design of protein nanoparticle vaccines from AlphaFold2-predicted building blocks. (PNAS 2025)

- DOI: 10.1073/pnas.2409566122 | PMCID: PMC12626006 | PMID: 41183183
- Evidence: Design methods like RFdiffusion for backbone generation and ProteinMPNN for amino acid sequence design have dramatically increased the success rate of many de novo design challenges, aided by the use of structure prediction methods such as AlphaFold2 (AF2) and RoseTTAFold as filters for high-quality designed proteins ( 44 – 46 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, RoseTTAFold]

### Accurate site-specific folding via conditional diffusion based on AlphaFold3. (PNAS 2025)

- DOI: 10.1073/pnas.2521048122 | PMCID: PMC12595467 | PMID: 41166421
- Evidence: The revolutionary advancements in artificial intelligence, particularly with the introduction of AlphaFold2 (AF2) [ 1 ], marked a significant leap forward in predicting the three-dimensional structures of individual proteins with unprecedented accuracy.
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> stage not stated [PyMOL]

### FibrilPaint to determine the length of Tau amyloids in fluids. (PNAS 2025)

- DOI: 10.1073/pnas.2502847122 | PMCID: PMC12595476 | PMID: 41144666
- Evidence: R h values can be estimated from the structural coordinates, either by experimental methods or by predictions such as AlphaFold ( SI Appendix , Table S2 ).
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### Exceptional diversity of allorecognition receptors in a nonvertebrate chordate reveals principles of innate allelic discrimination. (PNAS 2025)

- DOI: 10.1073/pnas.2519372122 | PMCID: PMC12582321 | PMID: 41129228
- Evidence: Structures of FF and FcoR proteins were predicted using AlphaFold2 ( 71 ) and AlphaFold3 ( 31 ).
- Full pipeline: alignment/mapping [RSEM, kallisto] -> stage not stated [AlphaFold]

### Nir2 crystal structures reveal a phosphatidic acid-sensing mechanism at ER-PM contact sites. (PNAS 2025)

- DOI: 10.1073/pnas.2516849122 | PMCID: PMC12582312 | PMID: 41129229
- Version used: **2.0**
- Evidence: The structure was determined by molecular replacement using the structure predicted by AlphaFold 2.0 ( 31 ) as a search model and was refined to 2.8 Å resolution (see Materials and Methods and SI Appendix , Table S1 ).
- Full pipeline: structure determination [AlphaFold v2.0]

### All the world's a phage. (PNAS 2025)

- DOI: 10.1073/pnas.2523344122 | PMCID: PMC12582341 | PMID: 41129223
- Evidence: The ability to predict protein structures using AlphaFold ( 82 ) as well as protein–protein interactions will be transformative in addressing these questions and provide a computational impetus to test specific hypotheses about gene function.
- Full pipeline: stage not stated [AlphaFold]

### Intracellular pH regulates ubiquitin-mediated degradation of the MAP kinase ERK3. (PNAS 2025)

- DOI: 10.1073/pnas.2501825122 | PMCID: PMC12582255 | PMID: 41123996
- Evidence: The predicted structure of human ERK3 (Uniprot Q16659 ) was downloaded from the AlphaFold structure database ( https://alphafold.ebi.ac.uk/ ) and visualized with PyMOL v.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [R] -> visualisation [AlphaFold, ImageJ, PyMOL v3.0.4]

### Proteolytically activated antibacterial toxins inhibit the growth of diverse gram-positive bacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2505807122 | PMCID: PMC12582261 | PMID: 41118212
- Evidence: ( D ) AlphaFold3 model of the C-terminal BECR domain of AbpT Sa overlaid with the RelE ribonuclease (PDB 3BPQ).
- Full pipeline: stage not stated [AlphaFold]

### T cell receptor specificity landscape revealed through de novo peptide design. (PNAS 2025)

- DOI: 10.1073/pnas.2504783122 | PMCID: PMC12557503 | PMID: 41100668
- Evidence: Importantly, this scarcity hinders computational prediction methods like AlphaFold in modeling reliable TCR–pMHC structures ( 18 , 19 ).
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### Ubiquitin-mediated degradation restricts spatiotemporal accumulation of the cytoplasmic male sterility protein WA352 to anthers in rice. (PNAS 2025)

- DOI: 10.1073/pnas.2504381122 | PMCID: PMC12557538 | PMID: 41100672
- Evidence: ( C ) Structure of full-length and truncated forms of WA352 as predicted by AlphaFold2, showing an N-terminal transmembrane domain (amino acids 1 to 150, WA352 1–150 ) and C-terminal conserved region (amino acids 151 to 352, WA352 151–352 ).
- Full pipeline: alignment/mapping [HISAT2, StringTie] -> quantification [HISAT2, StringTie] -> stage not stated [AlphaFold, ColabFold]

### FETCH enables fluorescent labeling of membrane proteins in vivo with spatiotemporal control in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2503166122 | PMCID: PMC12557536 | PMID: 41091763
- Evidence: We refer to these regions as membrane linkers, which AlphaFold 3 ( 28 ) predicts to be unstructured ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### Formation of a complex between TMEM217 and the sodium-proton exchanger SLC9C1 is crucial for mouse sperm motility and male fertility. (PNAS 2025)

- DOI: 10.1073/pnas.2513924122 | PMCID: PMC12557800 | PMID: 41091759
- Evidence: ( E , Top ) AlphaFold3 3D structural prediction of the mouse TMEM217–SLC9C1 complex.
- Full pipeline: stage not stated [AlphaFold]

### Emergence of antiphage functions from random sequence libraries reveals mechanisms of gene birth. (PNAS 2025)

- DOI: 10.1073/pnas.2513255122 | PMCID: PMC12557735 | PMID: 41091762
- Evidence: See SI Appendix for methods on measurements of bacterial liquid-growth measurements, fluorescence levels with flow cytometry, western blot analysis, RNA extraction and sequencing, and protein structure prediction with AlphaFold3.
- Full pipeline: stage not stated [AlphaFold, Cutadapt, ImageJ]

### Apusomonad rhodopsins: A new family of ultraviolet to blue light-absorbing rhodopsin channels. (PNAS 2025)

- DOI: 10.1073/pnas.2510619122 | PMCID: PMC12557545 | PMID: 41082663
- Evidence: Particularly, C106 is distal from the chromophore, but this residue in TM4 is likely to form hydrogen bonds between side chains and main chains with H93 in TM3, in the AlphaFold structural model, suggesting helix–helix interactions across TM3–TM4.
- Full pipeline: read trimming [IQ-TREE v1.6.11, MAFFT] -> alignment/mapping [IQ-TREE v1.6.11, MAFFT] -> differential/statistical testing [IQ-TREE v1.6.11] -> structure determination [IQ-TREE v1.6.11] -> stage not stated [AlphaFold, BLAST, GROMACS v4.5.7]

### Temperature adaptation in structure and function in lactate dehydrogenase-A reflects convergent evolution in a few key protein regions. (PNAS 2025)

- DOI: 10.1073/pnas.2517759122 | PMCID: PMC12557798 | PMID: 41071662
- Evidence: To this end, we utilized the AlphaFold -based workflow provided by ColabFold v1.5 to predict 3D structures of LDH-As ( 19 ).
- Full pipeline: alignment/mapping [MAFFT v7.487, R] -> simulation/modelling [GROMACS v2021.3, XGBoost] -> machine learning [TensorFlow] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5, VMD]

### GeoEvoBuilder: A deep learning framework for efficient functional and thermostable protein design. (PNAS 2025)

- DOI: 10.1073/pnas.2504117122 | PMCID: PMC12541336 | PMID: 41071657
- Evidence: ESMFold has demonstrated performance comparable to the groundbreaking algorithm AlphaFold2 (AF2) ( 36 ).
- Full pipeline: stage not stated [AlphaFold]

### Microtubule remodeling by the innate immune factor Trim69 compromises dynein-dependent migration of HIV virion cores toward the nucleus. (PNAS 2025)

- DOI: 10.1073/pnas.2505128122 | PMCID: PMC12541436 | PMID: 41066114
- Version used: **3.0**
- Evidence: To model the full-length Trim69 protein, including its Zn cofactors, we used AlphaFold 3.0, which revealed the three-dimensional organization of the individual domains ( SI Appendix, Fig.S2 A and B ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold v3.0]

### Augmenting rice &lt;i&gt;ANNEXIN&lt;/i&gt; expression to counter planthopper &lt;i&gt;Nl&lt;/i&gt;Annexin-like5 as an antivirulence strategy against a major crop pest. (PNAS 2025)

- DOI: 10.1073/pnas.2505698122 | PMCID: PMC12541338 | PMID: 41066107
- Evidence: ...complementation assays, protoplast isolation and transfection, protein extraction and western blot, RNA isolation and quantitative real-time PCR, and AlphaFold3 predictions can be found in SI Appendix , Supplementary Materials and Methods , some of which are similar to those described previously ( 67 ).
- Full pipeline: stage not stated [AlphaFold]

### Intrinsically disordered linkers and terminal domains codrive aciniform spidroin self-assembly through liquid-liquid phase separation. (PNAS 2025)

- DOI: 10.1073/pnas.2510216122 | PMCID: PMC12541454 | PMID: 41060761
- Evidence: Given their moderate sequence identity (~34%), we further generated a predicted AlphaFold structure of A. tr .
- Full pipeline: stage not stated [AlphaFold]

### A phosphoinositide-mediated switch of GET pathway receptor dimerization in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2514354122 | PMCID: PMC12541409 | PMID: 41060755
- Evidence: To distinguish between an interaction dependent on the physical properties of the R172 residue and its PIP binding capacity, we first performed a structural in silico analysis using AlphaFold3.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, ChimeraX]

### STAR/STARD1: A mitochondrial intermembrane space cholesterol shuttle degraded through mitophagy. (PNAS 2025)

- DOI: 10.1073/pnas.2508809122 | PMCID: PMC12541442 | PMID: 41055982
- Evidence: Murine STAR structure was modeled using AlphaFold (AF- Q60920 -F1), and structural alignments were performed in PyMOL (pymol.org) to compare murine and human STAR and highlight conserved residues.
- Full pipeline: alignment/mapping [AlphaFold, PyMOL]

### A nonenzymatic effector disrupts &lt;i&gt;Bacteroides&lt;/i&gt; cell wall homeostasis via OmpA targeting to mediate interbacterial competition. (PNAS 2025)

- DOI: 10.1073/pnas.2513207122 | PMCID: PMC12541434 | PMID: 41055976
- Evidence: Structural alignments revealed strong agreement between the cryo-EM reconstruction, the crystal structures of BteO 83–end and BtiO 23–end , and an AlphaFold3-predicted model of the BteO 83–end –BtiO 23–end complex, with RMSDs under 1.8 Å across all comparisons ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [AlphaFold, BLAST, MAFFT] -> structure determination [AlphaFold] -> stage not stated [IQ-TREE]

### Design principles of the common Gly-X6-Gly membrane protein building block. (PNAS 2025)

- DOI: 10.1073/pnas.2503134122 | PMCID: PMC12541321 | PMID: 41055983
- Evidence: Predicted structures by AlphaFold-3 (AF3) ( 37 ) were confident but likely incorrect for 4/5 TM sequences, adopting low contact density parallel-oriented helices ( SI Appendix , Fig.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, PHENIX]

### EFCAB10 anchors AK8 to the radial spoke for proper ciliary motility. (PNAS 2025)

- DOI: 10.1073/pnas.2510243122 | PMCID: PMC12541429 | PMID: 41055978
- Evidence: ( C ) Binding prediction for EFCAB10 with AK8 by AlphaFold3.
- Full pipeline: variant calling [ImageJ] -> stage not stated [AlphaFold, PyMOL]

### Methanogenesis inhibition remodels microbial fermentation and stimulates acetogenesis in ruminants. (PNAS 2025)

- DOI: 10.1073/pnas.2514823122 | PMCID: PMC12541428 | PMID: 41052332
- Evidence: Materials and Methods Detailed descriptions of the methods for metabolic annotation of short reads and MAGs, phylogenetic tree inferences, docking simulations of 3-NOP in AlphaFold2 generated models of MCR, calculations of combustion energy, reductant recovery and energy loss, in vitro rumen fluid assays, and isotope ratio measurement are provided in SI Appendix .
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.13] -> alignment/mapping [Salmon v1.10.2] -> normalisation [seaborn] -> simulation/modelling [AlphaFold]

### ProT-VAE: Protein Transformer Variational AutoEncoder for functional protein design. (PNAS 2025)

- DOI: 10.1073/pnas.2408737122 | PMCID: PMC12541330 | PMID: 41052325
- Evidence: We present AlphaFold ( 4 ) predicted structures for the sequence residing at the approximate inflection point of the path (purple) aligned to the structure of the hPAH at the beginning of the path (blue) and hTyrH or bacPAH at the end of the path (red).
- Full pipeline: alignment/mapping [AlphaFold]

### Generative AI for computational chemistry: A roadmap to predicting emergent phenomena. (PNAS 2025)

- DOI: 10.1073/pnas.2415655121 | PMCID: PMC12541333 | PMID: 41052337
- Evidence: RNNs, like long short-term memory (LSTM) networks, and transformer-based architectures ( 53 , 54 ), have made significant strides in natural language processing, speech recognition, and computational chemistry, notably in protein structure prediction with AlphaFold2 (AF2).
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold]

### Autoimmunity-associated DIORA1 binds the MRCK family of serine/threonine kinases and controls cell motility. (PNAS 2025)

- DOI: 10.1073/pnas.2426917122 | PMCID: PMC12519202 | PMID: 41042840
- Evidence: AlphaFold-Based Interaction Modeling.
- Full pipeline: visualisation [STRING db] -> stage not stated [AlphaFold, DESeq2, GSEA, UCSF Chimera]

### Identification of claudin-3 as an entry factor for rat hepacivirus. (PNAS 2025)

- DOI: 10.1073/pnas.2508736122 | PMCID: PMC12519123 | PMID: 41037638
- Evidence: AlphaFold2 prediction indicated that Ile 44 constituted the second β-strand and was exposed on the surface ( SI Appendix , Fig.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### A fixed mutation in the respiratory complex I impairs mitochondrial bioenergetics in the endangered Apennine brown bear. (PNAS 2025)

- DOI: 10.1073/pnas.2504409122 | PMCID: PMC12519208 | PMID: 41026818
- Evidence: The 3D structures of the different versions of the respiratory complex I were constructed using their respective amino acid sequences ( SI Appendix , Table S2 http://www.pnas.org/lookup/doi/10.1073/pnas.2504409122#supplementary-materials ) and the AlphaFold2 (AF2) predictor ( 27 ).
- Full pipeline: simulation/modelling [GROMACS v2022.3] -> visualisation [ChimeraX v1.7, VMD] -> stage not stated [AlphaFold, ImageJ]

### Versatile &lt;i&gt;Xenopus tropicalis&lt;/i&gt; model with targeted integration of human &lt;i&gt;BRAF&lt;sup&gt;V600E&lt;/sup&gt;&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2426981122 | PMCID: PMC12501161 | PMID: 41004227
- Evidence: Although AlphaFold shows intact Mitf structure/DNA-binding post-P2A fusion ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Duplication of a conserved mitochondrial enzyme gene arms parasitoid wasps with venom cytotoxicity and oogenesis regulation. (PNAS 2025)

- DOI: 10.1073/pnas.2512820122 | PMCID: PMC12501140 | PMID: 40996803
- Evidence: The structure of the protein complexes was predicted by AlphaFold 3 ( 67 ).
- Full pipeline: quality control [fastp] -> alignment/mapping [MAFFT] -> quantification [fastp] -> structure determination [phytools] -> stage not stated [AlphaFold, BLAST, HMMER]

### Glycosylated cannabinoids in &lt;i&gt;Cannabis sativa&lt;/i&gt; and enzyme design to modulate their synthesis. (PNAS 2025)

- DOI: 10.1073/pnas.2515688122 | PMCID: PMC12501178 | PMID: 40991441
- Evidence: The structure of CsUGT14 was modeled using AlphaFold2 ColabFold web server ( 43 ).
- Full pipeline: normalisation [R, edgeR] -> stage not stated [AlphaFold, ColabFold, ImageJ]

### Structural and functional analysis of the &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; MmpS5L5 efflux pump presages increased bedaquiline resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2516660122 | PMCID: PMC12501195 | PMID: 40986343
- Evidence: An AlphaFold2 model of a trimer of full-length MmpS5L5 (Model archive accession: ma-l7itj ( 73 )) was used as the starting point for model building.
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION] -> structure determination [PHENIX v1.21.2] -> stage not stated [AlphaFold, ChimeraX, Coot v0.9.8.93]

### Antagonistic SnRK2 and PID kinases' action on auxin transport-mediated root gravitropism. (PNAS 2025)

- DOI: 10.1073/pnas.2512274122 | PMCID: PMC12501181 | PMID: 40986351
- Evidence: Structural modeling using AlphaFold 3 revealed the molecular basis for SnRK2s–PID antagonism.
- Full pipeline: stage not stated [AlphaFold]

### Favorable epistasis in ancestral diterpene synthases promoted convergent evolution of a resin acid precursor in conifers. (PNAS 2025)

- DOI: 10.1073/pnas.2510962122 | PMCID: PMC12501191 | PMID: 40986353
- Evidence: Protein models were generated using AlphaFold2 ( 55 ) and the amino acid sequences of the full globular domains of ancestral sequences.
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### In situ structures of the &lt;i&gt;Legionella&lt;/i&gt; Dot/Icm T4SS identify the DotA-IcmX complex as the gatekeeper for effector translocation. (PNAS 2025)

- DOI: 10.1073/pnas.2516300122 | PMCID: PMC12501162 | PMID: 40986344
- Evidence: The IcmX model was predicted using AlphaFold3 ( 58 ) as an initial template.
- Full pipeline: alignment/mapping [PHENIX v1.21] -> structure determination [CTFFIND, ChimeraX, PHENIX v1.21] -> stage not stated [AlphaFold, Coot v0.8.9.1, IMOD, RELION v3.1]

### De novo design of potent inhibitors of clostridial family toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2509329122 | PMCID: PMC12501149 | PMID: 40982695
- Evidence: We then assigned sequences to the docks using ProteinMPNN and filtered the designs using AlphaFold2 initial guess ( 22 , 23 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL, seaborn] -> stage not stated [AlphaFold, ChimeraX, Topaz]

### Virion proteomics of genetically intact HCMV reveals a regulator of envelope glycoprotein composition that protects against humoral immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2425622122 | PMCID: PMC12478159 | PMID: 40966292
- Evidence: Deep learning structure prediction using AlphaFold3 (AF3) ( 43 ) was used to further understand the potential direct physical interactions between gpUL141 and gH or gB.
- Full pipeline: machine learning [AlphaFold]

### ComFB, a widespread family of c-di-NMP receptor proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2513041122 | PMCID: PMC12448109 | PMID: 40966295
- Evidence: The structures are AlphaFold2 predictions from UniProt/AlphaFold DB, except for Bs ComFB (PDB: 4WAI).
- Full pipeline: stage not stated [AlphaFold]

### Cryo-EM structure of the prohibitin complex in open conformation. (PNAS 2025)

- DOI: 10.1073/pnas.2512430122 | PMCID: PMC12478178 | PMID: 40966277
- Evidence: Initial structural models for PHB1 and PHB2 were generated using AlphaFold3 and rigidly fitted into the cryo-EM density map using ChimeraX ( 51 ).
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX]

### Employing deep mutational scanning in the &lt;i&gt;Escherichia coli&lt;/i&gt; periplasm to decode the thermodynamic landscape for amyloid formation. (PNAS 2025)

- DOI: 10.1073/pnas.2516165122 | PMCID: PMC12478104 | PMID: 40961135
- Evidence: DeepMind’s AlphaFold was recognized by the Nobel Prize for Chemistry in 2024 for its ability to predict protein structures from sequence alone, but its success not only rests on innovative algorithms but also relies on decades of experimental work that filled the Protein Data Bank with atomically accurate and diverse structures ( 1 – 3 ).
- Full pipeline: stage not stated [AlphaFold]

### Characterization of &lt;i&gt;Sr&lt;/i&gt;UGT76G4 reveals a key residue for regioselectivity and efficient Reb M synthesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504698122 | PMCID: PMC12478168 | PMID: 40961143
- Evidence: In order to elucidate the mechanisms underlying the regioselectivity of UGT76G4 and UGT76G1, we conducted MSA and structural superimposition using the crystal structure of UGT76G1 (PDB ID: 6INH) ( 14 ) and AlphaFold ( 31 ) predicted model for UGT76G4.
- Full pipeline: stage not stated [AlphaFold]

### Intercellular propagation of RIPK1/RIPK3 amyloid fibrils. (PNAS 2025)

- DOI: 10.1073/pnas.2507028122 | PMCID: PMC12478036 | PMID: 40956882
- Evidence: Furthermore, we employed AlphaFold3 to predict the structures of RIPK1, RIPK3, and RIPK1/RIPK3 RHIM fibrils ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### DNA-utilization loci enable exogenous DNA metabolism in gut Bacteroidales. (PNAS 2025)

- DOI: 10.1073/pnas.2505388122 | PMCID: PMC12478041 | PMID: 40956896
- Evidence: To predict the structure of the DdbC/DdbD complex, AlphaFold3 was used with default parameters ( 38 ).
- Full pipeline: read trimming [R v4.0.3] -> alignment/mapping [PyMOL] -> visualisation [ImageJ] -> stage not stated [AlphaFold, BLAST]

### Parametrically guided design of beta barrels and transmembrane nanopores using deep learning. (PNAS 2025)

- DOI: 10.1073/pnas.2425459122 | PMCID: PMC12478100 | PMID: 40953261
- Evidence: Structure comparison searches using FoldSeek ( 28 ) indicated that the design’s simple 6 stranded up-and-down barrel topology was not represented in the PDB and AlphaFold Database ( 28 , 29 ) (a total of 200 million structures; we did identify 5 models from the MIGNIFY_ESM30 microbiome database and 1 from the GMGCL_ID microbial metagenomic database with TM-scores > 0.6).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [AlphaFold, RoseTTAFold]

### A widespread family of molecular chaperones promotes the intracellular stability of type VIIb secretion system-exported toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2503581122 | PMCID: PMC12478183 | PMID: 40953262
- Evidence: AlphaFold2 (ColabFold) was used to predict the models of LtcA and LtcB, which were then used as search models to determine the X-ray crystal structures of the two proteins by molecular replacement ( 61 ).
- Full pipeline: alignment/mapping [MUSCLE v3.8.1551] -> structure determination [PHENIX] -> visualisation [IQ-TREE] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### Subtype-specific structural features of the hearing loss-associated human P2X2 receptor. (PNAS 2025)

- DOI: 10.1073/pnas.2417753122 | PMCID: PMC12452952 | PMID: 40938707
- Evidence: Further, the structure of full-length wild-type hP2X2R in the apo closed state establishes the correct helical pitch of each TM helix, not present in either truncated structures of other P2XR subtypes or the AlphaFold 3 predicted model of the hP2X2R ( SI Appendix , Figs.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX]

### Structural basis for Rad54- and Hed1-mediated regulation of Rad51 during the transition from mitotic to meiotic recombination. (PNAS 2025)

- DOI: 10.1073/pnas.2510007122 | PMCID: PMC12452912 | PMID: 40932772
- Evidence: Details of the Bioinformatic analysis, protein purification, AlphaFold3 structure predictions, biochemical assays, and genetic assays are provided as an SI Appendix .
- Full pipeline: structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold]

### Female membrane proteins regulate postmating ovulation in &lt;i&gt;Drosophila melanogaster&lt;/i&gt; by ovulin-dependent and -independent pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2508783122 | PMCID: PMC12452909 | PMID: 40920921
- Evidence: AlphaFold-Multimer Prediction Screen and Candidate Selection.
- Full pipeline: alignment/mapping [Clustal Omega, MUSCLE] -> variant calling [lme4] -> differential/statistical testing [emmeans, lme4] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL v2.5.5]

### Testis expressed 50 is essential for maintaining sperm acrosome integrity during epididymal transit. (PNAS 2025)

- DOI: 10.1073/pnas.2507930122 | PMCID: PMC12435281 | PMID: 40906813
- Evidence: We have also included a 3D image of mouse TEX50 protein as predicted by AlphaFold ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### De novo design of protein binders to stabilize monomeric TDP-43 and inhibit its pathological aggregation. (PNAS 2025)

- DOI: 10.1073/pnas.2505320122 | PMCID: PMC12435299 | PMID: 40901879
- Evidence: Using the AlphaFold2-initial guess method, designs with interface PAE < 6, binder PAE < 5, and pLDDT > 85 were selected for experimental validation.
- Full pipeline: stage not stated [AlphaFold]

### Fatty acid 2-hydroxylase facilitates rotavirus uncoating and endosomal escape. (PNAS 2025)

- DOI: 10.1073/pnas.2511911122 | PMCID: PMC12435199 | PMID: 40901882
- Evidence: ( C ) The protein structure of RRV VP4 ( P12473 ) was predicted by AlphaFold 3 and V184 was squared in red.
- Full pipeline: stage not stated [AlphaFold]

### &lt;i&gt;Pdgf&lt;/i&gt; mediates a transient regeneration-activated cell state in planarian tissue regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2501874122 | PMCID: PMC12435203 | PMID: 40892924
- Version used: **2.2**
- Evidence: Protein structures were predicted using AlphaFold v2.2 ( 71 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [ImageJ, PyMOL v2.6.0] -> stage not stated [AlphaFold v2.2]

### Mechanisms underlying allosteric modulation of antiseizure medication binding to synaptic vesicle protein 2A (SV2A). (PNAS 2025)

- DOI: 10.1073/pnas.2510239122 | PMCID: PMC12435242 | PMID: 40892927
- Evidence: We also compared our structure with the SV2B-PSL complex ( 21 ) and the AlphaFold-predicted ( 34 ) structure of SV2C ( Fig.
- Full pipeline: differential/statistical testing [RELION v3.1] -> structure determination [Coot, PHENIX v1.20.1] -> stage not stated [AlphaFold]

### Tumor-expressed GPNMB orchestrates Siglec-9&lt;sup&gt;+&lt;/sup&gt; TAM polarization and EMT to promote metastasis in triple-negative breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2503081122 | PMCID: PMC12435292 | PMID: 40892920
- Evidence: Structural models of human GPNMB were generated using AlphaFold2, and docking simulations with Siglecs were performed using HDOCK.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [AlphaFold] -> machine learning [UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AutoDock Vina, GSEA, R v4.3.0]

### Structural insights into the substrate uptake and inhibition of the human creatine transporter (hCRT). (PNAS 2025)

- DOI: 10.1073/pnas.2426135122 | PMCID: PMC12435270 | PMID: 40892912
- Evidence: The conformational model of SLC6A8 predicted by AlphaFold ( 67 , 68 ) was integrated into the cryoelectron microscopy density map for model building.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> visualisation [ChimeraX]

### TIGER: A tdTomato in vivo genome-editing reporter mouse for investigating precision-editor delivery approaches. (PNAS 2025)

- DOI: 10.1073/pnas.2506257122 | PMCID: PMC12415246 | PMID: 40880534
- Evidence: ( A ) Left , AlphaFold2-predicted structure of tdTomato ( 23 ).
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Nucleotide- and metalloid-driven conformational changes in the arsenite efflux ATPase ArsA. (PNAS 2025)

- DOI: 10.1073/pnas.2506440122 | PMCID: PMC12415280 | PMID: 40880530
- Evidence: Detailed procedures for cryo-EM sample preparation, data collection and processing, model building and refinement, XAS, ATPase assays, inductively coupled plasma-mass spectroscopy, and AlphaFold 3 modeling are available in the SI Appendix , Materials and Methods .
- Full pipeline: structure determination [AlphaFold, PHENIX]

### A genome-scale drug discovery pipeline uncovers therapeutic targets and a unique p97 allosteric binding site in &lt;i&gt;Schistosoma mansoni&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505710122 | PMCID: PMC12415213 | PMID: 40880532
- Evidence: Utilizing resources such as the Protein Data Bank (PDB) ( 49 , 50 ), AlphaFold ( 51 ), and Clustal ( 52 , 53 ), we have identified 51 potential drug targets that present favorable structural data (PSS ≥ 2) toward the development of selective drug-like molecules ( Dataset S3 ), supplying structural and unique residue differences between the parasite and orthologous mammalian structures ( SI Appendi...
- Full pipeline: stage not stated [AlphaFold, BLAST]

### CHP1 promotes lipid droplet growth and regulates the localization of key enzymes for triacylglycerol synthesis. (PNAS 2025)

- DOI: 10.1073/pnas.2508912122 | PMCID: PMC12415208 | PMID: 40875810
- Evidence: We analyzed the structure of the GPAT/CHP1 complexes using AlphaFold3 ( 10 ).
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### STAGE: A compact and versatile TnpB-based genome editing toolkit for &lt;i&gt;Streptomyces&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2509146122 | PMCID: PMC12415229 | PMID: 40857323
- Version used: **3.0**
- Evidence: Structural modeling using AlphaFold 3.0 ( 33 ) suggested that TnpB* closely resembles ISDra2 TnpB, with TM-score > 0.5 and RMSD value around 1.3 to 1.5 Å, supporting their structural similarity ( Fig.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS v2025.1] -> stage not stated [AlphaFold v3.0, ChimeraX]

### Specificities of chemosensory receptors in the human gut microbiota. (PNAS 2025)

- DOI: 10.1073/pnas.2508950122 | PMCID: PMC12415202 | PMID: 40857311
- Evidence: Comparison with the molecular docking of L-lactate to the AlphaFold 3 ( 28 ) model of K1 LBD ( Fig.
- Full pipeline: alignment/mapping [MAFFT, MrBayes] -> stage not stated [AlphaFold]

### Structure of the &lt;i&gt;Thomasclavelia ramosa&lt;/i&gt; immunoglobulin A protease reveals a modular and minimizable architecture distinct from other immunoglobulin A proteases. (PNAS 2025)

- DOI: 10.1073/pnas.2503549122 | PMCID: PMC12415215 | PMID: 40854123
- Evidence: The MD+CTD1 was modeled using its crystal structure and NTD, CTD2, CTD3, and CTD4 were modeled with their AlphaFold2-predicted models ( 44 , 45 ), which were truncated based on the boundaries outlined previously.
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold]

### CryoEM structure of ALK2:BMP6 reveals distinct mechanism that allow ALK2 to interact with both BMP and activin ligands. (PNAS 2025)

- DOI: 10.1073/pnas.2502788122 | PMCID: PMC12415261 | PMID: 40854140
- Evidence: The model of ALK2 bound to ActA was generated utilizing AlphaFold 2 ( 35 ).
- Full pipeline: structure determination [Coot v0.9.6, PHENIX v1.21] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### FliO is an evolutionarily conserved yet diversified core component of the bacterial flagellar type III secretion system. (PNAS 2025)

- DOI: 10.1073/pnas.2512476122 | PMCID: PMC12403147 | PMID: 40838884
- Evidence: Predicted structures of FliO proteins were retrieved from the AlphaFold structural database ( 30 ) and visualized in PyMOL 3.0.
- Full pipeline: visualisation [AlphaFold, PyMOL v3.0] -> stage not stated [HMMER]

### Definition of the components required for selective packaging of coronavirus genomic RNA. (PNAS 2025)

- DOI: 10.1073/pnas.2513552122 | PMCID: PMC12403154 | PMID: 40838885
- Evidence: At the outset of this study, there were no available structures of the CTD of MHV or any other Embecovirus, but high-confidence structural predictions recently became accessible through the introduction of AlphaFold 3 ( 54 ).
- Full pipeline: stage not stated [AlphaFold]

### Factors underlying a latitudinal gradient in the S/G lignin monomer ratio in natural poplar variants. (PNAS 2025)

- DOI: 10.1073/pnas.2503491122 | PMCID: PMC12403099 | PMID: 40833412
- Evidence: Structural models for PtLAC17-3 and PtLAC5-2 were generated using AlphaFold2, with both proteins showing high model confidence, with pLDDT scores of 96.5 and 97.0, respectively.
- Full pipeline: dimensionality reduction/clustering [R, WGCNA] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BCFtools, SAMtools, SnpEff]

### Protein functional site annotation using local structure embeddings. (PNAS 2025)

- DOI: 10.1073/pnas.2513219122 | PMCID: PMC12403137 | PMID: 40833413
- Evidence: We evaluated on AlphaFold predicted structures for known enzymes in SwissProt, starting with the sequence homologs provided by CSA, which are identified by searching each reference sequence against UniProt using PHMMER ( 59 ) with an e-value cutoff of 1 × 10 − 6 .
- Full pipeline: differential/statistical testing [GSEA] -> stage not stated [AlphaFold, BLAST]

### Structural basis and affinity improvement for an ATP-binding DNA aptamer. (PNAS 2025)

- DOI: 10.1073/pnas.2506491122 | PMCID: PMC12377721 | PMID: 40811466
- Evidence: In addition, computational tools such as the AlphaFold have yet to excel in predicting 3D structures of DNA–ligand complexes ( 14 , 15 ).
- Full pipeline: simulation/modelling [GROMACS v2021.7] -> visualisation [PyMOL] -> stage not stated [AlphaFold, VMD]

### The fetal hydrops-associated single-residue mutation L322P disrupts mechanical but not chemical activation of the PIEZO1 ion channel. (PNAS 2025)

- DOI: 10.1073/pnas.2503793122 | PMCID: PMC12377734 | PMID: 40789030
- Evidence: ( D ) The AlphaFold2-predicted full-length structure of a hPIEZO1 protomer containing 38 TMs with the highlighted domains and the location of the L322P and E997 truncation positions.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [ANNOVAR, AlphaFold, BEDTools, GATK v3.7, ImageJ, Picard]

### Structural insights into a citrate transporter that mediates aluminum tolerance in barley. (PNAS 2025)

- DOI: 10.1073/pnas.2501933122 | PMCID: PMC12358922 | PMID: 40763023
- Evidence: The initial phase information was determined by molecular replacement with Phaser-MR ( 53 ), using a polyalanine model of the predicted structure from AlphaFold2 ( 37 ).
- Full pipeline: alignment/mapping [Clustal Omega, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Structural basis for anaerobic alkane activation by a multisubunit glycyl radical enzyme. (PNAS 2025)

- DOI: 10.1073/pnas.2510389122 | PMCID: PMC12358834 | PMID: 40758891
- Evidence: AlphaFold ( 50 ) models of the individual MASSα and MASSγ subunits were docked into the final EM reconstruction using ChimeraX ( 51 ).
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [RELION v3.1]

### In situ cryo-ET visualization of mitochondrial depolarization and mitophagic engulfment. (PNAS 2025)

- DOI: 10.1073/pnas.2511890122 | PMCID: PMC12337332 | PMID: 40743392
- Evidence: To build models that fit the EM density maps for each class, AlphaFold3 was used to generate an initial protein model of 12 prohibitin 1-2 dimers which was then relaxed into either EM density map using ISOLDE ( https://isolde.cimr.cam.ac.uk/ ), (RRID:SCR_025577) ( 54 ) and PHENIX ( https://phenix-online.org/ ), (RRID:SCR_014224) ( 55 ).
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX, RELION, napari]

### Tat-dependent bundling pilus of a halophilic archaeon assembles by a strand donation mechanism and facilitates biofilm formation. (PNAS 2025)

- DOI: 10.1073/pnas.2514980122 | PMCID: PMC12337348 | PMID: 40737320
- Evidence: The TafE pilin (NJ7G_2828, UniProt ID: I7CYY9) structure predicted by AlphaFold served as the starting model for rigid-body fitting into the cryo-EM density map ( 59 ).
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [AlphaFold, ChimeraX, PHENIX]

### Surface delivery quantification reveals distinct trafficking efficiencies among clustered protocadherin isoforms. (PNAS 2025)

- DOI: 10.1073/pnas.2514178122 | PMCID: PMC12337331 | PMID: 40737325
- Evidence: ( B ) Surface representations of the EC6 cis interface for α4 [ Left ; structure prediction from AlphaFold Protein Structure Database [accession code: AF- O88689 -F1-v4] ( 53 )] and γB7 [ Right ; experimentally determined structure [PDB: 5V5X] ( 28 )].
- Full pipeline: alignment/mapping [MUSCLE v5.1, Python, SciPy v1.11.4] -> stage not stated [AlphaFold, seaborn v0.13.0]

### Structural basis for the evolution of a domesticated group II intron-like reverse transcriptase to function in host cell DNA repair. (PNAS 2025)

- DOI: 10.1073/pnas.2504208122 | PMCID: PMC12337344 | PMID: 40729381
- Version used: **3.0**
- Evidence: The RT3a plug was not predicted by any folding prediction program, including the most recent version of AlphaFold (AlphaFold 3.0, https://alphafoldserver.com/ ), indicating that it was beyond the imagination of AI.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold v3.0]

### Cryo-EM structure and polar assembly of the PS2 S-layer of &lt;i&gt;Corynebacterium glutamicum&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2426928122 | PMCID: PMC12337289 | PMID: 40729392
- Evidence: Finally, we used EMready ( 62 ) to improve the interpretability of the map in those regions where resolution was lower and finally, we built the atomic model using a combination of ModelAngelo ( 63 ), AlphaFold2 ( 64 ) followed by manually rebuilding in Coot ( 65 ).
- Full pipeline: structure determination [ChimeraX, PHENIX] -> visualisation [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Coot]

### Structural basis of auxin binding and transport by <i>Arabidopsis thaliana</i> AUX1. (PNAS 2025)

- DOI: 10.1073/pnas.2513424122 | PMCID: PMC12337342 | PMID: 40720658
- Evidence: The atomic model of AUX1 was initially constructed based on the structure predicted using AlphaFold2 ( 35 , 51 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [OpenMM, VMD] -> structure determination [PHENIX] -> machine learning [OpenMM] -> visualisation [VMD] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, Coot]

### Mechanistic insights into the iron-sulfur cluster-dependent interaction of the autophagy receptor NCOA4 with the E3 ligase HERC2. (PNAS 2025)

- DOI: 10.1073/pnas.2510269122 | PMCID: PMC12318192 | PMID: 40705422
- Evidence: Thus, we predicted the structural model of the full-length human HERC2 using AlphaFold3 ( 60 ).
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [AlphaFold]

### N<i>-</i>acetyltransferases required for iron uptake and aminoglycoside resistance promote virulence lipid production in <i>Mycobacterium marinum</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2502577122 | PMCID: PMC12305045 | PMID: 40680026
- Evidence: Based on structural predictions, MbtK and Eis proteins do not share domains beyond the conserved GNAT domains, with an RMSD score of 5.055, indicating that the two proteins are not structurally similar [AlphaFold ( 82 ), Fig.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [Clustal Omega] -> stage not stated [AlphaFold, PyMOL v2.4.0]

### Emergence of isochorismate-based salicylic acid biosynthesis within Brassicales. (PNAS 2025)

- DOI: 10.1073/pnas.2506170122 | PMCID: PMC12305054 | PMID: 40674416
- Evidence: To understand why ICS enzymes from certain Brassicales species exhibited enhanced activity for SA biosynthesis, we performed structural predictions of A. thaliana ICS1 using AlphaFold2 and compared the results with previously determined ICS structures ( 43 ).
- Full pipeline: stage not stated [AlphaFold]

### Structures of &lt;i&gt;Chaetomium thermophilum&lt;/i&gt; TOM complexes with bound preproteins. (PNAS 2025)

- DOI: 10.1073/pnas.2507279122 | PMCID: PMC12305020 | PMID: 40674418
- Evidence: The TOM holo model was generated using a combination of the previous core model and AlphaFold3 ( 26 ) to generate coordinates for the Tom20 subunit.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2, RELION v3.0]

### De novo design of a fusion protein tool for GPCR research. (PNAS 2025)

- DOI: 10.1073/pnas.2422360122 | PMCID: PMC12304938 | PMID: 40658860
- Evidence: The de novo design of Clips was initiated through a collaborative approach integrating RFdiffusion ( 19 ), ProteinMPNN ( 20 ), and AlphaFold2 ( 18 ).
- Full pipeline: stage not stated [AlphaFold, ChimeraX, PHENIX]

### Sleeping upside-down: Knockdown of a sleep-associated gene induces daytime sleep in the jellyfish &lt;i&gt;Cassiopea&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2505074122 | PMCID: PMC12305049 | PMID: 40658847
- Evidence: Evidence of cholinergic regulation in the nervous system of C assiopea ( A ) AlphaFold protein structure predictions for (a 1 ) Human Chrna-7, and (a 2 ) C. xamachana chrma-like-E (Chrnal-E), with labeled ligand site and CYS-loop indicating alpha-subunit similarity. pLDDT color legend indicates degree of structural confidence.
- Full pipeline: read trimming [STAR v2.5.3a, Trimmomatic v0.39] -> alignment/mapping [MAFFT v7.429, STAR v2.5.3a] -> normalisation [Bioconductor] -> dimensionality reduction/clustering [Python] -> differential/statistical testing [DESeq2, Python] -> structure determination [IQ-TREE v2.2] -> stage not stated [AlphaFold, BLAST, HMMER]

### Arylsulfamates inhibit colonic Bacteroidota growth through a sulfatase-independent mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2414331122 | PMCID: PMC12280919 | PMID: 40638084
- Evidence: To understand how arylsulfamates may interact with BT4322 we performed blind ligand docking (no pocket specified) with arylsulfamates 2 , 17 and Irosustat using the AlphaFold 2 predicted model of BT4322.
- Full pipeline: stage not stated [AlphaFold, BLAST]

### Regulation of the ordinal DNA translocation cycle in bacteriophage Φ29 through trans-subunit interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2504780122 | PMCID: PMC12260519 | PMID: 40608675
- Evidence: Structures of the ATPases of the Φ29 relatives that did not have existing structures (GA-1, SF5, and B103) and were created by folding their subunit sequences into monomers using AlphaFold 2 ( 20 ).
- Full pipeline: simulation/modelling [ChimeraX, VMD] -> visualisation [ChimeraX, VMD] -> stage not stated [AlphaFold, PLUMED]

### A &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; secreted virulence factor Rv1435c/hsr1 disrupts host snRNP biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2423349122 | PMCID: PMC12260434 | PMID: 40601628
- Evidence: Similar structural features were also revealed by AlphaFold Protein Structure Database ( 52 ) ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Expanding the diversity of bacterial DNA partitioning: A CTP-independent ParAB&lt;i&gt;S&lt;/i&gt; system for plasmid partitioning in &lt;i&gt;Streptomyces&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2406398122 | PMCID: PMC12260392 | PMID: 40601632
- Evidence: By integrating biochemical assays, single-molecule in vitro reconstitution, chromatin immunoprecipitation with deep sequencing, and AlphaFold2-based structure prediction, we reveal that the N-terminal peptide of ParT binds to and activates the ATPase activity of its ParA partner.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Molecular basis for substrate recognition and transport of mammalian taurine transporters. (PNAS 2025)

- DOI: 10.1073/pnas.2425549122 | PMCID: PMC12260568 | PMID: 40601627
- Evidence: The models were built using Coot ( 52 ), with the mTAUT structure (AF- O35316 -F1) obtained from the AlphaFold Protein Structure Database ( 53 ) serving as the initial reference.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PyMOL, RELION]

### SpbR controls lipoteichoic acid length by directly inhibiting signal peptidase SpsB in &lt;i&gt;Staphylococcus aureus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2426464122 | PMCID: PMC12260438 | PMID: 40587784
- Evidence: The AlphaFold2_advanced ColabFold notebook was used ( https://colab.research.google.com/github/sokrypton/ColabFold/blob/main/AlphaFold2.ipynb ) to model protein complexes ( 63 , 64 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold]

### In silico evolution of globular protein folds from random sequences. (PNAS 2025)

- DOI: 10.1073/pnas.2509015122 | PMCID: PMC12260532 | PMID: 40587803
- Evidence: The development of machine learning-based tools for fast and robust protein structure prediction including AlphaFold, RoseTTAFold, and ESMfold has changed this situation ( 19 – 22 ).
- Full pipeline: simulation/modelling [ChimeraX, VMD] -> visualisation [ChimeraX, VMD] -> stage not stated [AlphaFold, ColabFold v1.5.5, RoseTTAFold]

### Identification of a VPS29 isoform with restricted association to Retriever and Retromer accessory proteins through autoinhibition. (PNAS 2025)

- DOI: 10.1073/pnas.2501111122 | PMCID: PMC12260524 | PMID: 40587794
- Evidence: To obtain the model of VPS29C and VPS29C containing Retromer, we applied the AlphaFold2 neural network of the open-source ColabFold pipeline.
- Full pipeline: alignment/mapping [ChimeraX v1.6.1, PyMOL] -> differential/statistical testing [R] -> machine learning [AlphaFold, ColabFold] -> visualisation [ChimeraX v1.6.1, Cytoscape v3.3, Metascape v3.5, PyMOL] -> stage not stated [IQ-TREE v2.2.5]

### Enhanced chloroplast FtsZ-ring constriction by the ARC6-ARC3 module in &lt;i&gt;Arabidopsis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2425129122 | PMCID: PMC12232670 | PMID: 40560617
- Evidence: (Scale bar, 10 µm.) ( G ) AlphaFold3-predicted ARC3–ARC6 interaction (ipTM 0.51, pTM 0.47, min interface PAE 4.05 Å).
- Full pipeline: stage not stated [AlphaFold]

### Crystal structure and catalytic mechanism of drimenol synthase, an unusual bifunctional terpene cyclase-phosphatase. (PNAS 2025)

- DOI: 10.1073/pnas.2506584122 | PMCID: PMC12232559 | PMID: 40569382
- Evidence: A model of AsDMS generated with AlphaFold 3 revealed that the first 10 residues at the N terminus had a low predicted local distance difference test score, which reflected low confidence in the model prediction ( 51 ).
- Full pipeline: stage not stated [AlphaFold, PHENIX]

### Fine structural design of 3βHSD1 inhibitors for prostate cancer therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2422267122 | PMCID: PMC12232669 | PMID: 40560608
- Evidence: The structure model of human 3βHSD1 predicted by AlphaFold2 was used for molecular docking ( 31 ).
- Full pipeline: stage not stated [AlphaFold, AutoDock Vina, GSEA]

### The RRM domain-containing protein Rbp3 interacts with ribosomes and the 3' ends of mRNAs encoding photosynthesis proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2506275122 | PMCID: PMC12232666 | PMID: 40553498
- Evidence: ( B ) Rbp3 structure predicted by AlphaFold ( 71 , 72 ).
- Full pipeline: alignment/mapping [DESeq2] -> normalisation [R, limma] -> stage not stated [AlphaFold]

### Structural mechanism for the recognition of E2F1 by the ubiquitin ligase adaptor Cyclin F. (PNAS 2025)

- DOI: 10.1073/pnas.2501057122 | PMCID: PMC12232547 | PMID: 40549918
- Evidence: The initial model for the E2F1 peptide–Cyclin F–Skp1 complex was generated by AlphaFold and docked into the map using Coot v0.9.4 ( 36 ).
- Full pipeline: structure determination [PHENIX v1.20.1] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, ChimeraX v1.8]

### Molecular contacts in self-assembling clusters of membrane proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2507112122 | PMCID: PMC12232663 | PMID: 40549920
- Evidence: The AlphaFold-predicted N terminus (residues 1 to 93) that is not resolved in the detergent structure is shown in dark blue.
- Full pipeline: stage not stated [AlphaFold]

### SARS-CoV-2 nucleocapsid protein directly prevents cGAS-DNA recognition through competitive binding. (PNAS 2025)

- DOI: 10.1073/pnas.2426204122 | PMCID: PMC12232725 | PMID: 40549905
- Evidence: The disordered N-terminal domain was modeled using AlphaFold, with torsion angles adjusted for optimal visualization.
- Full pipeline: visualisation [AlphaFold]

### Structure of the virulence-associated &lt;i&gt;Neisseria meningitidis&lt;/i&gt; filamentous bacteriophage MDAΦ. (PNAS 2025)

- DOI: 10.1073/pnas.2420157122 | PMCID: PMC12207478 | PMID: 40540604
- Evidence: An atomic model of the MDA phage capsid was built with Coot using a structural prediction by AlphaFold2 as a starting model.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION, Topaz]

### Sp140L functions as a herpesvirus restriction factor suppressing viral transcription and activating interferon-stimulated genes. (PNAS 2025)

- DOI: 10.1073/pnas.2426339122 | PMCID: PMC12207491 | PMID: 40526717
- Evidence: To better understand the nature of the putative interaction between EBNA-LP and Sp140L and Sp100, we used AlphaFold3 to predict the structure of a complex between these proteins ( 56 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [AlphaFold]

### A self-assembling surface layer flattens the cytokinetic furrow to aid cell division in an archaeon. (PNAS 2025)

- DOI: 10.1073/pnas.2501044122 | PMCID: PMC12207459 | PMID: 40531877
- Evidence: AlphaFold modeling ( 44 – 47 ) further revealed that, like SlaB, Saci1846 contains three predicted immunoglobulin (Ig)-like domains within its structure ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### Metabolic control of glycosylation forms for establishing glycan-dependent protein interaction networks. (PNAS 2025)

- DOI: 10.1073/pnas.2422936122 | PMCID: PMC12207472 | PMID: 40531880
- Evidence: This difference is expected, as we generated the BSG N268Q mutant structure using AlphaFold2 and modeled the Man9 glycan onto the WT BSG structure using Glycam ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [R] -> visualisation [Cytoscape v3.9.1] -> stage not stated [AlphaFold, ComplexHeatmap, STRING db]

### The oncogene SLC35F2 is a high-specificity transporter for the micronutrients queuine and queuosine. (PNAS 2025)

- DOI: 10.1073/pnas.2425364122 | PMCID: PMC12207525 | PMID: 40526720
- Evidence: Structural models of SLC35F2 sequences from humans, S. pombe strain 972/ATCC 24843, and T. brucei strain 927/4 (UniProt IDs Q8IXU6 , O59785 , and Q57UU3 , respectively) were generated using AlphaFold v4 ( 42 ) and aligned in PROMALS3D ( 64 ).
- Full pipeline: read trimming [MUSCLE v5.2] -> alignment/mapping [AlphaFold, MUSCLE v5.2] -> quantification [ImageJ] -> visualisation [Cytoscape v3.10.1]

### Cryo-EM structures of GnRHR: Foundations for next-generation therapeutics. (PNAS 2025)

- DOI: 10.1073/pnas.2500112122 | PMCID: PMC12207466 | PMID: 40523184
- Evidence: For the GnRH–GnRHR–G q complexes, the AlphaFold2 structure of African clawed fGnRHR and pGnRHR and the structures of miniG q , rat Gβ1, bovine Gγ2, and scFv16 (PDB: 8HCQ) were used as the initial model for model rebuilding and refinement against the electron microscopy map ( 29 , 49 ).
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> visualisation [PyMOL]

### ATF6 enables pathogen infection in ticks by inducing &lt;i&gt;stomatin&lt;/i&gt; and altering cholesterol dynamics. (PNAS 2025)

- DOI: 10.1073/pnas.2501045122 | PMCID: PMC12207416 | PMID: 40526719
- Evidence: AlphaFold was used to model Ixodes ATF6 and Ixodes Stomatin ( 20 , 21 ).
- Full pipeline: alignment/mapping [ChimeraX] -> stage not stated [AlphaFold, ImageJ, R v4.2.2]

### A distinct LHCI arrangement is recruited to photosystem I in Fe-starved green algae. (PNAS 2025)

- DOI: 10.1073/pnas.2500621122 | PMCID: PMC12207447 | PMID: 40523173
- Evidence: The initial TIDI1 model was built using AlphaFold2 from the TIDI1 sequences from either D. salina or D. tertiolecta , docked into the Fe-starved Dunaliella PSI–LHCI 2 complexes using PHENIX dock in map, and subsequently fitted for the side chains in COOT ( 70 ).
- Full pipeline: alignment/mapping [RELION v3.0] -> structure determination [PHENIX v1.21.1] -> visualisation [ChimeraX v1.7.1] -> stage not stated [AlphaFold]

### Enzymatic carbon-fluorine bond cleavage by human gut microbes. (PNAS 2025)

- DOI: 10.1073/pnas.2504122122 | PMCID: PMC12184663 | PMID: 40512801
- Evidence: Within the past few years, major advancements have been made in protein structure prediction using AlphaFold (AF) ( 36 , 37 ), even enabling accurate MD simulations using relaxed AF models ( 38 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [R] -> simulation/modelling [AlphaFold, GROMACS] -> visualisation [Cytoscape] -> stage not stated [ColabFold, IQ-TREE]

### Structural basis of the hepatitis B virus X protein in complex with DDB1. (PNAS 2025)

- DOI: 10.1073/pnas.2421325122 | PMCID: PMC12184330 | PMID: 40512786
- Evidence: These configurations were further validated by simulated AFM images from AlphaFold3 models and were consistent with experimental HS-AFM images of both free and HBx complexed with DDB1 ( SI Appendix , Fig.
- Full pipeline: simulation/modelling [AlphaFold] -> structure determination [ColabFold] -> stage not stated [RELION]

### Structural insights into the activation and inhibition of the ADAM17-iRhom2 complex. (PNAS 2025)

- DOI: 10.1073/pnas.2500732122 | PMCID: PMC12184519 | PMID: 40512800
- Evidence: To build the initial structure, AlphaFold predictive models for the MEDI3622 F ab , Δ363-iRhom2 cytoplasmic deletion mutant and individual domains of ADAM17 were docked into the final density map, manually rebuilt, and refined ( Table 1 ).
- Full pipeline: structure determination [AlphaFold]

### The dependence of the amino acid backbone conformation on the translated synonymous codon is not statistically significant. (PNAS 2025)

- DOI: 10.1073/pnas.2503264122 | PMCID: PMC12184513 | PMID: 40512784
- Evidence: These results are corroborated by repeating the analysis on structures for the same set of proteins extracted from the AlphaFold Database ( 7 ), and shown to be robust with respect to the definition of secondary structural classes and also when considering the nature of the neighbor residues.
- Full pipeline: stage not stated [AlphaFold]

### Pathogenic variants in the polycystin pore helix cause distinct forms of channel dysfunction. (PNAS 2025)

- DOI: 10.1073/pnas.2421362122 | PMCID: PMC12184499 | PMID: 40504156
- Evidence: AlphaFold2 models (PKD2 residues 180-925) containing the variant of interest were pruned in PHENIX ( 57 ) to remove low-confidence residues.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, ImageJ, PHENIX]

### &lt;i&gt;Hamiltonella&lt;/i&gt; symbionts benefit whitefly fertilization by regulating the maternal protein Tudor-mediated piRNA pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2427053122 | PMCID: PMC12184435 | PMID: 40504144
- Evidence: Prediction of the Tud–Aub–piRt00104691 Complex Using AlphaFold3.
- Full pipeline: differential/statistical testing [edgeR] -> visualisation [PyMOL v3.1.0] -> stage not stated [AlphaFold, BLAST, ImageJ]

### The great phage escape: Activating and escaping lactococcal antiphage systems. (PNAS 2025)

- DOI: 10.1073/pnas.2426508122 | PMCID: PMC12184496 | PMID: 40498451
- Version used: **2.3.1**
- Evidence: We performed predictions with either a Colab notebook running AlphaFold v2.3.1 ( https://colab.research.google.com/github/deepmind/alphafold/blob/main/notebooks/AlphaFold.ipynb ) or HPC resources from GENCI-IDRIS running AlphaFold v2.3.1 ( 48 ).
- Full pipeline: stage not stated [AlphaFold v2.3.1, BLAST, ChimeraX, InterProScan]

### Structural basis of the catalytic and allosteric mechanism of bacterial acetyltransferase PatZ. (PNAS 2025)

- DOI: 10.1073/pnas.2419096122 | PMCID: PMC12184503 | PMID: 40498448
- Evidence: Initial models were generated using AlphaFold and fitted to the map using ISOLDE.
- Full pipeline: alignment/mapping [ChimeraX, IQ-TREE, Kraken2] -> structure determination [ChimeraX, PHENIX] -> visualisation [Kraken2] -> stage not stated [AlphaFold]

### Cryptic isoprene emission of soybeans. (PNAS 2025)

- DOI: 10.1073/pnas.2502360122 | PMCID: PMC12184331 | PMID: 40504154
- Evidence: The sequences were rendered into protein structures using Phyre2 (ver 2.0), a protein fold recognition software whose data are supplied by the AlphaFold Protein Structure Database.
- Full pipeline: visualisation [AlphaFold] -> stage not stated [MrBayes, PyMOL v4.6.0]

### An N-terminal domain specifies developmental control by the SMAX1-LIKE family of transcriptional regulators in <i>Arabidopsis thaliana</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2412793122 | PMCID: PMC12184505 | PMID: 40493196
- Evidence: We also considered a prediction of SMAX1 protein structure created by AlphaFold2 ( 69 ).
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### A specific negatively charged sequence confers intramolecular regulation on Munc13-1 function in synaptic exocytosis. (PNAS 2025)

- DOI: 10.1073/pnas.2508915122 | PMCID: PMC12184661 | PMID: 40489622
- Evidence: To test this, we utilized AlphaFold multimer to predict the potential interaction sites of polyE with MUN.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### The highly conserved intron of tyrosine tRNA is critical for &lt;sup&gt;m1&lt;/sup&gt;A58 modification and controls the integrated stress response. (PNAS 2025)

- DOI: 10.1073/pnas.2502364122 | PMCID: PMC12168002 | PMID: 40478875
- Evidence: Sequence reads are available from the sequence read archive ( https://www.ncbi.nlm.nih.gov/bioproject/PRJEB89406/ ) ( 62 ) AlphaFold Predictions and Structural Comparisons.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [AlphaFold, ChimeraX]

### Direct sensing of host ferric iron by an archetype histidine kinase mediates virulence of an enteric pathogen. (PNAS 2025)

- DOI: 10.1073/pnas.2507874122 | PMCID: PMC12167987 | PMID: 40465626
- Evidence: AlphaFold3 structural modeling ( https://alphafold3.org/ ) corroborated canonical histidine kinase architecture ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, MACS2]

### Concerted transport and phosphorylation of diacylglycerol at ER-PM contact sites regulate phospholipid dynamics during stress. (PNAS 2025)

- DOI: 10.1073/pnas.2421334122 | PMCID: PMC12167946 | PMID: 40455983
- Evidence: AlphaFold ( https://alphafold.ebi.ac.uk/ ) ( 76 , 77 ) was used to predict the tertiary structure of DGK1, DGK2, and HsDGKε.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Clustal Omega, Cufflinks v2.2.1, R] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [AlphaFold, ilastik]

### Structure and organization of full-length epidermal growth factor receptor in extracellular vesicles by cryo-electron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2424678122 | PMCID: PMC12167996 | PMID: 40455995
- Evidence: Such a structure is predicted by AlphaFold 3 for a homodimer of the EGFR transmembrane and juxtamembrane regions ( SI Appendix , Fig.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [IMOD] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX] -> visualisation [EMAN2] -> stage not stated [AlphaFold, ImageJ, MotionCor2, RELION]

### Solution structure and synaptic analyses reveal determinants of bispecific T cell engager potency. (PNAS 2025)

- DOI: 10.1073/pnas.2425781122 | PMCID: PMC12146755 | PMID: 40445758
- Evidence: Multistate modeling was performed with MultiFoXS ( 72 ), based on existing start models from the protein data bank (PDB) or AlphaFold2 ( 73 ).
- Full pipeline: stage not stated [AlphaFold, UCSF Chimera, VMD]

### Molecular basis for ligand recognition and receptor activation of the prostaglandin D2 receptor DP1. (PNAS 2025)

- DOI: 10.1073/pnas.2501902122 | PMCID: PMC12146711 | PMID: 40440061
- Evidence: A predicted DP1 structure from AlphaFold2 was used as the starting reference model for receptor building ( 41 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, R v3.50]

### Biochemical and structural basis of Dicer helicase function unveiled by resurrecting ancient proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2500825122 | PMCID: PMC12146746 | PMID: 40434637
- Evidence: All models apart from AncD1D2 are AlphaFold 3 predictions ( 39 ).
- Full pipeline: stage not stated [AlphaFold]

### Evolution of the essential gene &lt;i&gt;MN1&lt;/i&gt; during the macroevolutionary transition toward patterning the vertebrate hindbrain. (PNAS 2025)

- DOI: 10.1073/pnas.2416061122 | PMCID: PMC12146709 | PMID: 40424121
- Version used: **2.3.2**
- Evidence: AlphaFold v2.3.2 ( https://github.com/deepmind/alphafold ) was run using the default parameters ( 84 ), querying the suggested databases.
- Full pipeline: alignment/mapping [BLAST, DESeq2 v1.34.0, HISAT2, IQ-TREE v1.6.12] -> differential/statistical testing [DESeq2 v1.34.0, HISAT2] -> stage not stated [AlphaFold v2.3.2, HMMER, OrthoFinder v2.5.5, R v4.1, ggplot2 v3.5.1, tidyverse]

### HCK regulates NLRP12-mediated PANoptosis. (PNAS 2025)

- DOI: 10.1073/pnas.2422079122 | PMCID: PMC12130821 | PMID: 40408404
- Evidence: Materials and Methods Sequence Retrieval and AlphaFold2 Modeling.
- Full pipeline: differential/statistical testing [limma v3.60.2] -> simulation/modelling [R] -> visualisation [ChimeraX v1.8, R] -> stage not stated [AlphaFold, ColabFold v1.5.5, PyMOL v2.8]

### The white lupin CCR1 receptor-like kinase controls systemic Autoregulation of Cluster Root and Nodule Development. (PNAS 2025)

- DOI: 10.1073/pnas.2418411122 | PMCID: PMC12130874 | PMID: 40402250
- Evidence: AlphaFold structure prediction was performed using ColabFold v1.5.5: AlphaFold2 with MMseqs2 ( 52 , 53 ), providing the amino acid sequence of LalbCCR1 ( LalbChr03g0025491 ).
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17] -> variant calling [GATK] -> normalisation [R] -> differential/statistical testing [R] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, BLAST, ColabFold v1.5.5, Picard]

### A tethering mechanism underlies Pin1-catalyzed proline &lt;i&gt;cis-trans&lt;/i&gt; isomerization at a noncanonical site. (PNAS 2025)

- DOI: 10.1073/pnas.2414606122 | PMCID: PMC12130881 | PMID: 40388619
- Evidence: 2 B on the top scoring AlphaFold 3 model of pAF-1 bound to Pin1 reveals the extent to which regions of AF-1 distal to the canonical pS112 binding site of Pin1 engage with the isomerase ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### Molecular determinants of sialylated IgG anti-inflammatory activity. (PNAS 2025)

- DOI: 10.1073/pnas.2411600122 | PMCID: PMC12107084 | PMID: 40377989
- Evidence: Human IgG Fc allotype amino acid sequences were individually input into AlphaFold 3 (Google DeepMind, Isomorphic Labs) with a “protein” molecule type and a copy number of 2 ( 34 ).
- Full pipeline: visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold]

### Modes of action of a small molecule antiviral compound targeting yellow fever virus NS4B protein. (PNAS 2025)

- DOI: 10.1073/pnas.2505498122 | PMCID: PMC12107144 | PMID: 40378003
- Evidence: To identify the BDAA binding site (pocket) on NS4B, the 3D structure of YFV NS4B was predicted using the AlphaFold 3 program ( 29 ).
- Full pipeline: stage not stated [AlphaFold]

### Phase separation of the oncogenic fusion protein EWS::FLI1 is modulated by its DNA-binding domain. (PNAS 2025)

- DOI: 10.1073/pnas.2221823122 | PMCID: PMC12107149 | PMID: 40377985
- Evidence: We plotted residues with CSPs greater than one SD from the mean and residues with differential signal intensities less than one SD from the mean onto the AlphaFold ( 57 ) structure of human PU.1 ( Fig.
- Full pipeline: differential/statistical testing [AlphaFold] -> visualisation [AlphaFold]

### Molecular insights into human phosphatidylserine synthase 2 and its regulation of SREBP pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2501177122 | PMCID: PMC12107096 | PMID: 40372437
- Evidence: The initial models were built de novo based on the AlphaFold2-predicted structures and then manually adjusted and refined using COOT ( 21 ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [NAMD, VMD] -> structure determination [AlphaFold, PHENIX] -> visualisation [ChimeraX, PyMOL]

### Arrestin recognizes GPCRs independently of the receptor state. (PNAS 2025)

- DOI: 10.1073/pnas.2501487122 | PMCID: PMC12107136 | PMID: 40372433
- Evidence: ( Bottom ) AlphaFold2 model of arrestin2 showing the N- and C-domains (gray).
- Full pipeline: quantification [ImageJ] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND v4.1.14, RELION v4.0]

### Structural insights into the activation of the human prostaglandin E&lt;sub&gt;2&lt;/sub&gt; receptor EP1 subtype by prostaglandin E&lt;sub&gt;2&lt;/sub&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2423840122 | PMCID: PMC12107139 | PMID: 40366695
- Evidence: To assess the accuracy of computational prediction methods, we compared our experimental structure with AlphaFold2-predicted models ( 40 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, R v7.40, Topaz]

### Electric field-induced pore constriction in the human K&lt;sub&gt;v&lt;/sub&gt;2.1 channel. (PNAS 2025)

- DOI: 10.1073/pnas.2426744122 | PMCID: PMC12107148 | PMID: 40366685
- Evidence: A structural model for the depolarized-highK conformation was built by docking four copies of the AlphaFold-predicted ( 66 ) structure of K v 2.1 into the up map (unpolarized dataset) and making adjustments as needed.
- Full pipeline: structure determination [ChimeraX v1.5, PHENIX, PyMOL] -> stage not stated [AlphaFold, RELION]

### Decoding collagen's thermally induced unfolding and refolding pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2420308122 | PMCID: PMC12107170 | PMID: 40359051
- Evidence: AlphaFold3 was used to predict the local disulfide-bridged structure around the cystine knot ( 67 ).
- Full pipeline: stage not stated [AlphaFold]

### The developmental factor TBX3 engages with the Wnt/β-catenin transcriptional complex in colorectal cancer to regulate metastasis genes. (PNAS 2025)

- DOI: 10.1073/pnas.2419691122 | PMCID: PMC12088458 | PMID: 40343989
- Evidence: ( C ) AlphaFold2 predictions of the TBX3’s T-box (plus 20 additional amino acid residues) with and without deletion of NPF or RRM.
- Full pipeline: stage not stated [AlphaFold, HOMER]

### Structural insights into the ubiquitin-independent midnolin-proteasome pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2505345122 | PMCID: PMC12088389 | PMID: 40339123
- Evidence: The initial model for MIDN αHelix-C, Catch domain, and UBL domain was first derived from AlphaFold 2 ( 18 ).
- Full pipeline: alignment/mapping [ChimeraX] -> quantification [ImageJ] -> structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, Coot]

### Unconventional secretion of PARK7 requires lysosomal delivery via chaperone-mediated autophagy and specialized SNARE complex. (PNAS 2025)

- DOI: 10.1073/pnas.2414790122 | PMCID: PMC12088447 | PMID: 40327696
- Evidence: To further validate the SNARE complex formation observed in co-IP experiments, we employed AlphaFold2 multimer analysis.
- Full pipeline: stage not stated [AlphaFold]

### The SIK3-N783Y mutation is associated with the human natural short sleep trait. (PNAS 2025)

- DOI: 10.1073/pnas.2500356122 | PMCID: PMC12088394 | PMID: 40324078
- Evidence: In the protein tertiary structure prediction section, we employed the AlphaFold3 prediction platform ( https://alphafoldserver.com/ ) to predict the structures of both WT and mutant proteins.
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler] -> machine learning [SnpEff] -> visualisation [ggplot2] -> stage not stated [AlphaFold, Cytoscape, ImageJ]

### Incorporation of polylactic acid microplastics into the carbon cycle as a carbon source to remodel the endogenous metabolism of the gut. (PNAS 2025)

- DOI: 10.1073/pnas.2417104122 | PMCID: PMC12088454 | PMID: 40324088
- Evidence: To further characterize esterase FrsA, we predicted its structure using AlphaFold2 and confirmed its identity via the UniProt database.
- Full pipeline: stage not stated [AlphaFold]

### Activity and structure of human (d)CTP deaminase CDADC1. (PNAS 2025)

- DOI: 10.1073/pnas.2424245122 | PMCID: PMC12088426 | PMID: 40324085
- Evidence: For model building, AlphaFold2 ( 24 ) generated CDADC1 monomers were rigid body fitted into the map using UCSF ChimeraX v1.4 ( 39 ) and manually adjusted using Coot ( 40 ).
- Full pipeline: structure determination [PHENIX v1.20.1] -> stage not stated [AlphaFold, ChimeraX v1.4]

### Structure and nucleic acid interactions of the S&lt;sup&gt;Δ60&lt;/sup&gt; domain of the hepatitis delta virus small antigen. (PNAS 2025)

- DOI: 10.1073/pnas.2411890122 | PMCID: PMC12088457 | PMID: 40324079
- Evidence: Using AlphaFold2 ( 33 ), we predicted the structure and found significant structural similarities (rmsd of 0.997 Å for residues G92-R143) between the predicted and experimental structures, as can be observed from the overlay in SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.4]

### Accurate identification and mechanistic evaluation of pathogenic missense variants with &lt;i&gt;Rhapsody-2&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418100122 | PMCID: PMC12067267 | PMID: 40314982
- Evidence: Five categories of features were evaluated for each SAV after mapping them to AlphaFold2 ( 20 ) structures: 1) residue-specific features composed of molecular weight, hydrophobicity, and chemical group; 2) local interactions including contact density, hydrophobic core, salt bridges, hydrogen bonds, and disulfide bonds; 3) intermolecular interface probability using ScanNet ( 56 ); 4) intrinsic dyna...
- Full pipeline: alignment/mapping [AlphaFold] -> machine learning [XGBoost]

### Calcium-activated chloride channel TMEM16A opens via pi-helical transition in transmembrane segment 4. (PNAS 2025)

- DOI: 10.1073/pnas.2421900122 | PMCID: PMC12067253 | PMID: 40299692
- Evidence: Structure Predictions by AlphaFold2.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS, PyMOL v2.5] -> stage not stated [AlphaFold, ImageJ, MDAnalysis]

### Gag proteins encoded by endogenous retroviruses are required for zebrafish development. (PNAS 2025)

- DOI: 10.1073/pnas.2411446122 | PMCID: PMC12067270 | PMID: 40294259
- Evidence: To predict the monomeric structure of Bik-1 Gag, we used AlphaFold2 via the ColabFold notebook ( 30 , 71 ).
- Full pipeline: read trimming [STAR v2.11a, Trimmomatic] -> alignment/mapping [IQ-TREE v2.06, MAFFT, PyMOL, STAR v2.11a, Trimmomatic] -> stage not stated [AlphaFold, BEDTools v2.30.0, BLAST, ColabFold, HMMER v3.3.2, ImageJ, SAMtools v1.18]

### A simple method for mapping the location of cross-β-forming regions within protein domains of low sequence complexity. (PNAS 2025)

- DOI: 10.1073/pnas.2503382122 | PMCID: PMC12054801 | PMID: 40267128
- Evidence: Development of AlphaFold capabilities of protein structure prediction required a foundation consisting of thousands of structures deduced by X-ray crystallography, NMR spectroscopy, and cryoelectron microscopy ( 47 ).
- Full pipeline: stage not stated [AlphaFold]

### FlgY, PflA, and PflB form a spoke-ring network in the high-torque flagellar motor of &lt;i&gt;Helicobacter pylori&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2421632122 | PMCID: PMC12054838 | PMID: 40261933
- Evidence: AlphaFold3 ( 40 ) was used to predict the structures of the FlgY homodimer ( SI Appendix, Fig.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [ChimeraX] -> stage not stated [AlphaFold, CTFFIND]

### Cleavage cascade of the sigma regulator FecR orchestrates TonB-dependent signal transduction. (PNAS 2025)

- DOI: 10.1073/pnas.2500366122 | PMCID: PMC12036975 | PMID: 40244679
- Evidence: Structural Prediction with AlphaFold3.
- Full pipeline: stage not stated [AlphaFold]

### ATM priming and end resection-coupled phosphorylation of MRE11 is important for fork protection and replication restart. (PNAS 2025)

- DOI: 10.1073/pnas.2422720122 | PMCID: PMC12037065 | PMID: 40249789
- Evidence: We used AlphaFold3 ( 44 ) to model MRE11 phosphorylation by ATM and ATR ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### The emergence and loss of cyclic peptides in &lt;i&gt;Nicotiana&lt;/i&gt; illuminate dynamics and mechanisms of plant metabolic evolution. (PNAS 2025)

- DOI: 10.1073/pnas.2425055122 | PMCID: PMC12037056 | PMID: 40228125
- Evidence: ( D ) Overlay of AlphaFold-predicted structures of NatBURP1 (blue) and 5x_Nna (purple), focusing on the active site.
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [AlphaFold]

### Generating the polymorph landscapes of amyloid fibrils using AI: RibbonFold. (PNAS 2025)

- DOI: 10.1073/pnas.2501321122 | PMCID: PMC12037047 | PMID: 40232799
- Evidence: Encoding Parallel-in-Register Constraints into AlphaFold2 for the Prediction of Amyloid Fibrils.
- Full pipeline: stage not stated [AlphaFold]

### Genomic signatures associated with the evolutionary loss of egg yolk in parasitoid wasps. (PNAS 2025)

- DOI: 10.1073/pnas.2422292122 | PMCID: PMC12036997 | PMID: 40232796
- Evidence: To explore the structural and functional impacts, we predicted VgR protein structures using LocalColabFold (AlphaFold) ( 125 , 126 ) and aligned them in ChimeraX ( 127 ) ( SI Appendix , Table S20 ).
- Full pipeline: alignment/mapping [AlphaFold, ChimeraX] -> quantification [RSEM] -> structure determination [IQ-TREE, OrthoFinder] -> stage not stated [AUGUSTUS, BLAST, HMMER]

### Bourbon and Mycbp function with Otu to promote Sxl protein expression in the &lt;i&gt;Drosophila&lt;/i&gt; female germline. (PNAS 2025)

- DOI: 10.1073/pnas.2426524122 | PMCID: PMC12012553 | PMID: 40215271
- Evidence: Structure Modeling of Complexes by AlphaFold.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### DprA recruits ComM to facilitate recombination during natural transformation in Gram-negative bacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2421764122 | PMCID: PMC12012524 | PMID: 40215278
- Version used: **2.3**
- Evidence: For all identified DprA homologs, we performed protein structure prediction using AlphaFold v2.3 ( 30 ) as implemented in the ColabFold v1.5.2 pipeline ( 31 ).
- Full pipeline: alignment/mapping [PyMOL v3.0] -> stage not stated [AlphaFold v2.3, ChimeraX v1.9, ColabFold v1.5.2]

### ID3 enhances PD-L1 expression by restructuring MYC to promote colorectal cancer immune evasion. (PNAS 2025)

- DOI: 10.1073/pnas.2423490122 | PMCID: PMC12012548 | PMID: 40208940
- Evidence: We used the AlphaFold2 program and Discovery Studio 2019 software to create three initial kinetic models (ID3-DNA, MYC-DNA, and ID3-MYC-DNA systems) for comparative kinetic analysis, revealing that ID3 restructured MYC from a loose conformation to a more compact state ( Fig.
- Full pipeline: stage not stated [AlphaFold, STRING db]

### Neddylation modification stabilizes LC3B by antagonizing its ubiquitin-mediated degradation and promoting autophagy in skin. (PNAS 2025)

- DOI: 10.1073/pnas.2411429122 | PMCID: PMC12012473 | PMID: 40208944
- Evidence: ( D ) Mapping the K42 on the tertiary structure of LC3B predicted using AlphaFold.
- Full pipeline: alignment/mapping [AlphaFold]

### NAL1 forms a molecular cage to regulate FZP phase separation. (PNAS 2025)

- DOI: 10.1073/pnas.2419961122 | PMCID: PMC12012508 | PMID: 40203040
- Evidence: AlphaFold2 predictions indicate that FZP comprises a central structured domain flanked by an unstructured region of 126 amino acids at the N terminus and another substantial unstructured segment at the C-terminus ( SI Appendix , Fig.
- Full pipeline: structure determination [PHENIX, RELION v3.1] -> stage not stated [AlphaFold]

### Alpha-tubulin tails regulate axoneme differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2414731122 | PMCID: PMC12012489 | PMID: 40198703
- Evidence: The structures of TBB-4 and TBA-5 tubulin binding to Mg 2+ -GTP predicted by AlphaFold 3 ( www.alphafoldserver.com ) ( 53 ) were used as alpha- and beta-tubulin.
- Full pipeline: quantification [ImageJ] -> simulation/modelling [GROMACS v2024.2] -> visualisation [PyMOL v2.0] -> stage not stated [AlphaFold]

### Structural and functional characterization of the brain-specific dynamin superfamily member RNF112. (PNAS 2025)

- DOI: 10.1073/pnas.2419449122 | PMCID: PMC12012479 | PMID: 40198702
- Evidence: Initial phases were obtained by molecular replacement with a search model generated by AlphaFold2 ( 61 ) and refined using Phaser ( 62 ).
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [ImageJ, PyMOL]

### Structural basis for immune cell binding of &lt;i&gt;Fusobacterium nucleatum&lt;/i&gt; via the trimeric autotransporter adhesin CbpF. (PNAS 2025)

- DOI: 10.1073/pnas.2418155122 | PMCID: PMC12012533 | PMID: 40198705
- Evidence: AlphaFold2 Prediction of CbpF and CbpF/CEACAM1.
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot v0.9.8.7, PHENIX] -> visualisation [R] -> stage not stated [AlphaFold, Fiji, ImageJ, UCSF Chimera]

### An integrated AI knowledge graph framework of bacterial enzymology and metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2425048122 | PMCID: PMC12012490 | PMID: 40193601
- Evidence: Consequently, Transformers form the foundation of state-of-the-art structure prediction methods, such as ESM2 and AlphaFold2 ( 14 – 16 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, HMMER, PyTorch, Python, SciPy]

### Bispecific antibodies against the hepatitis C virus E1E2 envelope glycoprotein. (PNAS 2025)

- DOI: 10.1073/pnas.2420402122 | PMCID: PMC12012487 | PMID: 40193609
- Evidence: For the prediction of AR4A/AR3C IgG3C- structure, AlphaFold-2.3.1 multimer was used ( 93 , 94 ).
- Full pipeline: visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, Matplotlib, NumPy, SciPy, seaborn]

### AcrIE7 inhibits the CRISPR-Cas system by directly binding to the R-loop single-stranded DNA. (PNAS 2025)

- DOI: 10.1073/pnas.2423205122 | PMCID: PMC12002350 | PMID: 40178896
- Evidence: ( C and D ) Comparison of AcrIE7 crystal structure with AlphaFold2 (AF2) and AlphaFold3 (AF3) prediction.
- Full pipeline: stage not stated [AlphaFold]

### Allosterically switchable network orients &lt;i&gt;β&lt;/i&gt;-flap in &lt;i&gt;Clostridioides difficile&lt;/i&gt; toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2419263122 | PMCID: PMC12002228 | PMID: 40172960
- Evidence: For more details on system preparation, particularly on the addition of hydrogens, as well as the protocol for structures generated with AlphaFold2 ( 50 , 51 ), see SI Appendix , sections 1.B and 5 .
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, PLUMED]

### HEATR3 recognizes membrane rupture and facilitates xenophagy in response to &lt;i&gt;Salmonella&lt;/i&gt; invasion. (PNAS 2025)

- DOI: 10.1073/pnas.2420544122 | PMCID: PMC12002282 | PMID: 40178893
- Evidence: AlphaFold2 conformation model prediction was performed and predicted structure is shown in ribbon representation.
- Full pipeline: stage not stated [AlphaFold]

### A conserved ARF-DNA interface underlies auxin-triggered transcriptional response. (PNAS 2025)

- DOI: 10.1073/pnas.2501915122 | PMCID: PMC12002309 | PMID: 40168121
- Evidence: Structures of ARFs were predicted using AlphaFold2 ( 29 ) with default settings.
- Full pipeline: quality control [FastQC] -> alignment/mapping [featureCounts] -> quantification [ilastik v1.3.3] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, HMMER, PyMOL]

### Unveiling Cas8 dynamics and regulation within a transposon-encoded Cascade-TniQ complex. (PNAS 2025)

- DOI: 10.1073/pnas.2422895122 | PMCID: PMC12002280 | PMID: 40172964
- Evidence: To model the Cas8 bundle (residues 277–385) and the missing loops (i.e., ~10 amino acids within the Cas proteins), AlphaFold2 ( 13 ) was combined with PyRosetta ( 14 ) (details in SI Appendix ).
- Full pipeline: simulation/modelling [NAMD v2.14] -> stage not stated [AlphaFold]

### Following phospholipid transfer through the OmpF&lt;sub&gt;3&lt;/sub&gt;-MlaA-MlaC lipid shuttle with native mass spectrometry. (PNAS 2025)

- DOI: 10.1073/pnas.2420041122 | PMCID: PMC12002339 | PMID: 40168124
- Evidence: ( B ) AlphaFold structures of OmpF 3 and OmpF 3 –MlaA with observed fragmentation sites highlighted in red.
- Full pipeline: simulation/modelling [GROMACS v2022.5] -> stage not stated [AlphaFold]

### PHLPP2 is a pseudophosphatase that lost activity in the metazoan ancestor. (PNAS 2025)

- DOI: 10.1073/pnas.2417218122 | PMCID: PMC12002173 | PMID: 40168118
- Evidence: Using the AlphaFold2-predicted structure of the phosphatase domain, which superimposes on the experimentally determined structure of PPM1A with a rmsd of 1.09 Å, the most likely constellation of zinc-coordinating residues was identified as C799, D820, D822, and D1024, which correspond to the M2 metal ion binding site ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Cryo-EM structure of cyanopodophage A4 reveals a pentameric pre-ejectosome in the double-stabilized capsid. (PNAS 2025)

- DOI: 10.1073/pnas.2423403122 | PMCID: PMC12002296 | PMID: 40163721
- Evidence: Cryo-EM map combined with AlphaFold2 prediction ( 33 ) enabled us to finally build the intact atomic model of the trimeric tail fiber/gp24 ( SI Appendix , Fig.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Mechanistic insights into dengue virus inhibition by a clinical trial compound NITD-688. (PNAS 2025)

- DOI: 10.1073/pnas.2426922122 | PMCID: PMC12002330 | PMID: 40153462
- Evidence: The tertiary structure of flavivirus NS4B is currently unavailable; however, AlphaFold2 structural predictions show residues T195 and A222 near neighboring alpha helices, with an estimated C α distance of 7.3 Å ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### Lysosomal PIP&lt;sub&gt;3&lt;/sub&gt; revealed by genetically encoded lipid biosensors. (PNAS 2025)

- DOI: 10.1073/pnas.2426929122 | PMCID: PMC12002240 | PMID: 40127277
- Evidence: The complex structures of the lipid-binding domains and pseudoligand were predicted using the AlphaFold 3 algorithm ( 65 ) via the AlphaFold server.
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Red-light signaling pathway activates desert cyanobacteria to prepare for desiccation tolerance. (PNAS 2025)

- DOI: 10.1073/pnas.2502034122 | PMCID: PMC11962455 | PMID: 40112114
- Evidence: Additionally, structural models of NfPixJ and NfSrr1 were predicted using AlphaFold3 ( https://golgi.sandbox.google.com/ ) ( Fig.
- Full pipeline: quality control [FastQC v0.11.4] -> alignment/mapping [edgeR v3.20.7] -> dimensionality reduction/clustering [Bioconductor] -> differential/statistical testing [edgeR v3.20.7] -> stage not stated [AlphaFold, PyMOL]

### &lt;i&gt;Chlamydomonas&lt;/i&gt; FBB18 is a ubiquitin-like protein essential for the cytoplasmic preassembly of various ciliary dyneins. (PNAS 2025)

- DOI: 10.1073/pnas.2423948122 | PMCID: PMC11962417 | PMID: 40106351
- Evidence: Furthermore, our structural analysis using AlphaFold2 multimer ( 71 ) predicted that DHC5, HC of IDA b that is strongly reduced in both fbb18-2 cilia and cytoplasm ( Figs.
- Full pipeline: stage not stated [AlphaFold, PHENIX, PyMOL]

### ANGPTL3/8 is an atypical unfoldase that regulates intravascular lipolysis by catalyzing unfolding of lipoprotein lipase. (PNAS 2025)

- DOI: 10.1073/pnas.2420721122 | PMCID: PMC11962473 | PMID: 40112106
- Evidence: Using AlphaFold, we built a molecular model of ANGPTL3/8 based on the 2:1 stoichiometry established by mass photometry.
- Full pipeline: stage not stated [AlphaFold]

### Cryo-EM structures reveal the acetylation process of piccolo NuA4. (PNAS 2025)

- DOI: 10.1073/pnas.2414490122 | PMCID: PMC11962513 | PMID: 40100634
- Evidence: The structure of NuA4 fused with the SNAP tag was predicted using AlphaFold3 ( 42 ).
- Full pipeline: alignment/mapping [RELION v4.0] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [AlphaFold, Coot]

### Substrate recognition by a peptide-aminoacyl-tRNA ligase. (PNAS 2025)

- DOI: 10.1073/pnas.2423858122 | PMCID: PMC11962472 | PMID: 40106349
- Evidence: Using AlphaFold3 ( 48 ), we generated a model of the quaternary complex of B h a B C T r p , tRNA Trp , BhaA-Ala, and ATP providing a three-dimensional perspective of peptide substrate and tRNA engagement by the enzyme.
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> stage not stated [ChimeraX]

### Structural assembly of the PAS domain drives the catalytic activation of metazoan PASK. (PNAS 2025)

- DOI: 10.1073/pnas.2409685122 | PMCID: PMC11962487 | PMID: 40106358
- Evidence: AlphaFold Model Generation and Analysis.
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> stage not stated [AlphaFold, ChimeraX v1.7, ColabFold, RoseTTAFold]

### &lt;i&gt;Staphylococcus aureus&lt;/i&gt; uses a GGDEF protein to recruit diacylglycerol kinase to the membrane for lipid recycling. (PNAS 2025)

- DOI: 10.1073/pnas.2414696122 | PMCID: PMC11962490 | PMID: 40100631
- Evidence: AlphaFold2 Modeling of GdpS–DgkB Complexes.
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold v1.5.5]

### Conserved leucine-rich repeat proteins in the adhesive projectile slime of velvet worms. (PNAS 2025)

- DOI: 10.1073/pnas.2416282122 | PMCID: PMC11962477 | PMID: 40100627
- Evidence: Protein structures were predicted using AlphaFold3.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, ColabFold]

### Proteasomal processing of the viral replicase ORF1 facilitates HEV-induced liver fibrosis. (PNAS 2025)

- DOI: 10.1073/pnas.2419946122 | PMCID: PMC11929459 | PMID: 40073055
- Evidence: To better understand how HDSA interacts with and regulates Smad3 at the structural level, we utilized AlphaFold to predict the structure of HDSA ( 36 ).
- Full pipeline: stage not stated [AlphaFold]

### A family of bacterial actin homologs forms a three-stranded tubular structure. (PNAS 2025)

- DOI: 10.1073/pnas.2500913122 | PMCID: PMC11929497 | PMID: 40073056
- Evidence: An initial atomic model of BeeR was generated with AlphaFold and refined in Phenix.
- Full pipeline: structure determination [AlphaFold, PHENIX]

### Characterization of diverse Cas9 orthologs for genome and epigenome editing. (PNAS 2025)

- DOI: 10.1073/pnas.2417674122 | PMCID: PMC11929499 | PMID: 40073054
- Evidence: Structural analyses, leveraging data from the AlphaFold database ( 36 ), revealed close structural alignment (1 to 3 Å RMSD) of SauCas9 with SgaCas9, SpaCas9, and SubCas9, despite sequence identities of only 32 to 34% ( Fig.
- Full pipeline: alignment/mapping [AlphaFold, MUSCLE v3.8.425] -> stage not stated [BLAST, RAxML]

### Structural mechanisms underlying the modulation of CXCR4 by diverse small-molecule antagonists. (PNAS 2025)

- DOI: 10.1073/pnas.2425795122 | PMCID: PMC11929458 | PMID: 40063796
- Evidence: The coordinate of the chimeric receptor CXCR4 κOR predicted by AlphaFold2, and the coordinate of the nanobody Nb6 from PDB 8K2W ( 38 ), were docked into the density maps in ChimeraX ( 39 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> stage not stated [RELION v5.0]

### The SUbventral-Gland Regulator (SUGR-1) of nematode virulence. (PNAS 2025)

- DOI: 10.1073/pnas.2415861122 | PMCID: PMC11929438 | PMID: 40063806
- Evidence: Protein structure was predicted using AlphaFold ( 72 ) and visualized using CCP4MG ( 73 ).
- Full pipeline: quality control [FastQC v0.11.9, HTSeq v0.12.4] -> read trimming [FastQC v0.11.9] -> alignment/mapping [STAR v2.7.9a] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [AlphaFold] -> stage not stated [HOMER, ImageJ, R v4.2.1, ggplot2 v3.4.2]

### State-dependent motion of a genetically encoded fluorescent biosensor. (PNAS 2025)

- DOI: 10.1073/pnas.2426324122 | PMCID: PMC11912384 | PMID: 40048274
- Evidence: AlphaFold3 and Structure Visualization.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [AlphaFold] -> stage not stated [CCP4]

### Structural basis for dimerization and activation of UvrD-family helicases. (PNAS 2025)

- DOI: 10.1073/pnas.2422330122 | PMCID: PMC11912403 | PMID: 40048277
- Evidence: (Tudor) AlphaFold model of the UvrD1 Tudor domain (purple) fits the unaccounted-for experimental density nestled between the 2A and 2B subdomains of each subunit.
- Full pipeline: stage not stated [AlphaFold]

### Allosteric inhibition of the IZUMO1-JUNO fertilization complex by the naturally occurring antisperm antibody OBF13. (PNAS 2025)

- DOI: 10.1073/pnas.2425952122 | PMCID: PMC11912406 | PMID: 40042902
- Evidence: ( K ) Structural overlay of an AlphaFold predicted sperm IZUMO1–SPACA6–TMEM81 complex and egg JUNO with the IZUMO1–OBF13 complex, showing that OBF13 makes a clash with SPACA6 when OBF13 interacts with IZUMO1.
- Full pipeline: stage not stated [AlphaFold]

### MUC5AC filaments illuminate the structural diversification of respiratory and intestinal mucins. (PNAS 2025)

- DOI: 10.1073/pnas.2419717122 | PMCID: PMC11912381 | PMID: 40035770
- Evidence: A model of MUC5AC residues 28 to 1,320 was generated using AlphaFold2 colab ( 18 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX v1.3, PLINK v1.9, PyMOL]

### A horizontally transferred bacterial gene aids the freezing tolerance of Antarctic bdelloid rotifers. (PNAS 2025)

- DOI: 10.1073/pnas.2421910122 | PMCID: PMC11912409 | PMID: 40035762
- Evidence: Among the five structures predicted by AlphaFold for each sequence, the one labeled “best model” was used in this study.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.6r, ColabFold]

### Cas9-mediated gene-editing frequency in microalgae is doubled by harnessing the interaction between importin α and phytopathogenic NLSs. (PNAS 2025)

- DOI: 10.1073/pnas.2415072122 | PMCID: PMC11912399 | PMID: 40030016
- Evidence: AlphaFold Prediction for Putative Impα Proteins.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### TEX38 localizes ZDHHC19 to the plasma membrane and regulates sperm head morphogenesis in mice. (PNAS 2025)

- DOI: 10.1073/pnas.2417943122 | PMCID: PMC11912386 | PMID: 40030029
- Evidence: We predicted the structure of the TEX38–ZDHHC19 heterodimer by AlphaFold3 ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### High-resolution structures of Myosin-IC reveal a unique actin-binding orientation, ADP release pathway, and power stroke trajectory. (PNAS 2025)

- DOI: 10.1073/pnas.2415457122 | PMCID: PMC11892617 | PMID: 40014570
- Evidence: To investigate how force sensitivity may be linked with the second ATP-isomerization, we compared our AM myo1c cryo-EM structures with an AlphaFold-generated model of postrigor ATP-bound myo1c (Uniprot Q5ZLA6x) ( 44 ).
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold]

### Ectopic mouse TMC1 and TMC2 alone form mechanosensitive channels that are potently modulated by TMIE. (PNAS 2025)

- DOI: 10.1073/pnas.2403141122 | PMCID: PMC11892609 | PMID: 39999170
- Evidence: We utilized AlphaFold2 to predict the accessibility of extracellular lysines in mTMC1 and hTMC1( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### A structural atlas of death domain fold proteins reveals their versatile roles in biology and function. (PNAS 2025)

- DOI: 10.1073/pnas.2426986122 | PMCID: PMC11874512 | PMID: 39977327
- Evidence: Annotation of AlphaFold-Predicted Structures.
- Full pipeline: structure determination [RELION] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Cryo-EM of native membranes reveals an intimate connection between the Krebs cycle and aerobic respiration in mycobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2423761122 | PMCID: PMC11874196 | PMID: 39969994
- Evidence: Next, the AlphaFold model of Mqo (Uniprot ID: A0A2U9PPB6; AlphaFold ID: AF-A0A2U9PPB6-F1-v4) was fit into the additional lower-resolution region of the map.
- Full pipeline: structure determination [Topaz] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, PHENIX, UCSF Chimera]

### PSKH1 kinase activity is differentially modulated via allosteric binding of Ca&lt;sup&gt;2+&lt;/sup&gt; sensor proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2420961122 | PMCID: PMC11873932 | PMID: 39964718
- Evidence: ( H ) AlphaFold model of PSKH1.
- Full pipeline: stage not stated [AlphaFold]

### AI protocol for retrieving protein dynamic structures from two-dimensional infrared spectra. (PNAS 2025)

- DOI: 10.1073/pnas.2424078122 | PMCID: PMC11848431 | PMID: 39951500
- Evidence: Advances in AI have revolutionized the prediction of a protein’s fully folded three-dimensional structure from its primary amino acid sequence, with models like AlphaFold and RoseTTAFold significantly enhancing our understanding of static protein structures ( 8 – 14 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold, RoseTTAFold]

### Photoreceptor-induced LHL4 protects the photosystem II monomer in &lt;i&gt;Chlamydomonas reinhardtii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418687122 | PMCID: PMC11848305 | PMID: 39946539
- Evidence: The predicted LHL4 AlphaFold2 model downloadable from UniprotKB was used.
- Full pipeline: alignment/mapping [ChimeraX, STAR v2.7.10b] -> normalisation [Bioconductor, edgeR v3.42.4] -> differential/statistical testing [Bioconductor, edgeR v3.42.4, limma] -> stage not stated [AlphaFold, BLAST, ColabFold, HTSeq v0.11.3, IQ-TREE]

### Structural basis of disease mutation and substrate recognition by the human SLC2A9 transporter. (PNAS 2025)

- DOI: 10.1073/pnas.2418282122 | PMCID: PMC11848319 | PMID: 39937868
- Evidence: A starting model of SLC2A9 from AlphaFold2 (AF- Q9NRM0 -F1, https://www.uniprot.org/uniprotkb/Q9NRM0/entry#structure ) was used for manual rigid-body fitting in COOT ( 37 ) followed by real-space refinement in Phenix ( 38 , 39 ) against the final cryo-EM map.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX]

### Impairment of DET1 causes neurological defects and lethality in mice and humans. (PNAS 2025)

- DOI: 10.1073/pnas.2422631122 | PMCID: PMC11848315 | PMID: 39937864
- Evidence: We generated an AlphaFold2-multimer model that confirmed our model and extended the interpretation of less contiguous DET1 density regions in the EM data ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### Bacterial polysaccharide lyase family 33: Specificity from an evolutionarily conserved binding tunnel. (PNAS 2025)

- DOI: 10.1073/pnas.2421623122 | PMCID: PMC11848413 | PMID: 39932998
- Evidence: Furthermore, we employ a combination of size exclusion chromatography (SEC)-coupled light-scattering, small-angle X-ray scattering (SAXS), AlphaFold2 (AF2) modeling, and molecular dynamic simulations to define the oligomeric state and structural changes of these enzymes in the absence and presence of substrate.
- Full pipeline: simulation/modelling [AlphaFold] -> structure determination [Coot] -> stage not stated [GROMACS]

### Seesaw protein: Design of a protein that adopts interconvertible alternative functional conformations and its dynamics. (PNAS 2025)

- DOI: 10.1073/pnas.2412117122 | PMCID: PMC11848303 | PMID: 39928865
- Evidence: 2 D , the two states of SSPs were predicted by AlphaFold3 ( 40 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, ImageJ]

### Dynamic changes in histone lysine lactylation during meiosis prophase I in mouse spermatogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2418693122 | PMCID: PMC11848400 | PMID: 39928879
- Evidence: ( G ) AlphaFold3 prediction and docking analysis of PRDM9 interact with one nucleosome H4 histone at lysine 8 sites.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, HOMER]

### Reenacting a mouse genetic evolutionary arms race in yeast reveals that SLXL1/SLX compete with SLY1/2 for binding to Spindlins. (PNAS 2025)

- DOI: 10.1073/pnas.2421446122 | PMCID: PMC11848428 | PMID: 39928872
- Evidence: Materials and Methods AlphaFold.
- Full pipeline: alignment/mapping [RepeatMasker] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ColabFold]

### Mec1-mediated Atg9 phosphorylation regulates the PAS recruitment of Atg9 vesicles upon energy stress. (PNAS 2025)

- DOI: 10.1073/pnas.2422582122 | PMCID: PMC11831128 | PMID: 39913206
- Evidence: Regarding the increased interactions between Atg9 3D and Atg proteins upon glucose starvation or DNA damage, while these interactions do not increase in Atg9 3A or mec1-85 cells, we attempted to use AlphaFold3 software to understand the role of Atg9 phosphorylation in promoting interactions with Atg17, Atg23, and Atg27 ( 26 ).
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### The ER-PM interaction is essential for cytokinesis and recruits the actin cytoskeleton through the SCAR/WAVE complex. (PNAS 2025)

- DOI: 10.1073/pnas.2416927122 | PMCID: PMC11831168 | PMID: 39913210
- Evidence: Meanwhile, the interactions between LIP1 and VAP27-1 have been further validated by AlphaFold3 protein docking prediction ( 58 ) ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Rapid restoration of potent neutralization activity against the latest Omicron variant JN.1 via AI rational design and antibody engineering. (PNAS 2025)

- DOI: 10.1073/pnas.2406659122 | PMCID: PMC11831182 | PMID: 39908098
- Evidence: Significant progress has been made in macromolecular drug design based on AlphaFold and Rosetta ( 17 , 18 ).
- Full pipeline: visualisation [UCSF Chimera] -> stage not stated [AlphaFold]

### The C2 domain augments Ras GTPase-activating protein catalytic activity. (PNAS 2025)

- DOI: 10.1073/pnas.2418433122 | PMCID: PMC11831179 | PMID: 39899710
- Evidence: Monomeric AlphaFold structure predictions were obtained from the AlphaFold Protein Structure Database and multimer predictions were generated using ColabFold.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### High-throughput discovery of inhibitory protein fragments with AlphaFold. (PNAS 2025)

- DOI: 10.1073/pnas.2322412122 | PMCID: PMC11831152 | PMID: 39899719
- Evidence: Materials and Methods ColabFold with AlphaFold2 monomer weights was used to predict fragment–protein interactions.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Bacterial sensor evolved by decreasing complexity. (PNAS 2025)

- DOI: 10.1073/pnas.2409881122 | PMCID: PMC11804620 | PMID: 39879239
- Evidence: Initial structural models were generated by AlphaFold2 ( 46 ) to feed Morel ( 75 ).
- Full pipeline: normalisation [CCP4] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Hsp90, DnaK, and ClpB collaborate in protein reactivation. (PNAS 2025)

- DOI: 10.1073/pnas.2422640122 | PMCID: PMC11804706 | PMID: 39879241
- Evidence: ( B ) AlphaFold model of Hsp90 Ec dimer in the apo form showing residues discussed in this paper.
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### Automating the practice of science: Opportunities, challenges, and implications. (PNAS 2025)

- DOI: 10.1073/pnas.2401238121 | PMCID: PMC11804648 | PMID: 39869810
- Evidence: A landmark achievement in this area is the nobel-prize winning AlphaFold, which predicts 3D protein structures from amino acid sequences, facilitating the development of drugs ( 6 ).
- Full pipeline: differential/statistical testing [Stan] -> simulation/modelling [Stan] -> stage not stated [AlphaFold]

### How should the advancement of large language models affect the practice of science? (PNAS 2025)

- DOI: 10.1073/pnas.2401227121 | PMCID: PMC11804466 | PMID: 39869798
- Evidence: This doesn’t preclude the use of AI advances in prediction for aiding human insight; prediction systems like AlphaFold are currently being used to advance basic science.
- Full pipeline: stage not stated [AlphaFold]

### 14-3-3 promotes sarcolemmal expression of cardiac Ca<sub>V</sub>1.2 and nucleates isoproterenol-triggered channel superclustering. (PNAS 2025)

- DOI: 10.1073/pnas.2413308122 | PMCID: PMC11804677 | PMID: 39869803
- Evidence: Modeling of Ca V 1.2 Interaction with 14-3-3 Using AlphaFold 3 (AF3).
- Full pipeline: stage not stated [AlphaFold]

### PgpP is a broadly conserved phosphatase required for phosphatidylglycerol lipid synthesis. (PNAS 2025)

- DOI: 10.1073/pnas.2418775122 | PMCID: PMC11804483 | PMID: 39869797
- Evidence: ( A ) AlphaFold models of Gep4 and B. subtilis PgpP.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, PyMOL v2.5.3]

### Molecular glue for phycobilisome attachment to photosystem II in <i>Synechococcus</i> sp. PCC 7002. (PNAS 2025)

- DOI: 10.1073/pnas.2415222122 | PMCID: PMC11789067 | PMID: 39847327
- Evidence: In the predicted structure by AlphaFold 2, LcpA has a β-sheet fold in the middle of the protein, which could play a role in its interaction with the membranes.
- Full pipeline: quantification [ImageJ v1.8.0] -> stage not stated [AlphaFold]

### Variants in the SOX9 transactivation middle domain induce axial skeleton dysplasia and scoliosis. (PNAS 2025)

- DOI: 10.1073/pnas.2313978121 | PMCID: PMC11789016 | PMID: 39854231
- Evidence: To further characterize the impact of SOX9 variants, we predicted the potential structural effects by AlphaFold ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### A periplasmic protein modulates the proteolysis of peptidoglycan hydrolases to maintain cell wall homeostasis in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2418854122 | PMCID: PMC11789061 | PMID: 39841140
- Evidence: The fitted models in the Prc-NlpI section ( Upper row) utilize the crystal structure of the 2:2 NlpI:Prc complex (PDB ID 5WQL), while the Prc-NlpI-BipP section ( Lower row) uses the predicted 1:1 BipP:NlpI model which was generated using AlphaFold.
- Full pipeline: structure determination [UCSF Chimera] -> stage not stated [AlphaFold, GCTA]

### Structural insights into glucose-6-phosphate recognition and hydrolysis by human G6PC1. (PNAS 2025)

- DOI: 10.1073/pnas.2418316122 | PMCID: PMC11789071 | PMID: 39847333
- Evidence: The predicted AlphaFold2 model of hG6PC1 was fitted into the cryo-EM density map of hG6PC1 apo in Chimera ( 50 ) and was manually inspected and adjusted in Coot ( 51 ).
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ChimeraX, PyMOL]

### Molecular mechanism of ligand recognition and activation of lysophosphatidic acid receptor LPAR6. (PNAS 2025)

- DOI: 10.1073/pnas.2415426122 | PMCID: PMC11789011 | PMID: 39847322
- Evidence: Similar to previous studies ( 31 , 33 , 34 , 41 ), initial models for rebuilding the human LPAR6 structure were generated using AlphaFold predictions ( 42 ) (AF- P43657 -F1-model_v1) and aligned to the electron microscopy map.
- Full pipeline: alignment/mapping [AlphaFold] -> dimensionality reduction/clustering [RELION] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v4.1, MotionCor2, R v3.50]

### Epstein-Barr virus BALF0/1 subverts the Caveolin and ERAD pathways to target B cell receptor complexes for degradation. (PNAS 2025)

- DOI: 10.1073/pnas.2400167122 | PMCID: PMC11789056 | PMID: 39847318
- Evidence: AlphaFold modeling predicts that BALF0/1 and the antiapoptotic BCL2 family member MCL1 share structural homology ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, Cytoscape v3.8.1, ImageJ]

### Preventing inappropriate signals pre- and post-ligand perception by a toggle switch mechanism of ERECTA. (PNAS 2025)

- DOI: 10.1073/pnas.2420196122 | PMCID: PMC11789017 | PMID: 39841143
- Evidence: Next, we examined the predicted AlphaFold2 structures of the ER cytoplasmic domain (ER_CD) ( 46 ).
- Full pipeline: stage not stated [AlphaFold]

### Itaconate mechanism of action and dissimilation in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2423114122 | PMCID: PMC11789021 | PMID: 39841148
- Evidence: We used AlphaFold2 to predict the structures for Rv2503c and Rv2499c and compared these to the sequence homologs obtained from BLAST analysis.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, AutoDock Vina]

### Plant BCL-DOMAIN HOMOLOG proteins play a conserved role in SWI/SNF complex stability. (PNAS 2025)

- DOI: 10.1073/pnas.2413346122 | PMCID: PMC11761322 | PMID: 39823297
- Evidence: The Arabidopsis (MINU1 HSA -ARP4-ARP7-BDH1) and Human (BRG1 HSA -ACTL6-ACTB-BCL7A) complexes, as well as the chimeric Rtt102–Arabidopsis complex, were modeled with AlphaFold2 (v.2) ( 29 ) and AlphaFold-multimer ( 31 ) using a colab notebook running ColabFold ( 48 ) v1.5.5.
- Full pipeline: stage not stated [AlphaFold, ColabFold, deepTools v3.5.1, ggplot2]

### Nitrous oxide production via enzymatic nitroxyl from the nitrifying archaeon &lt;i&gt;Nitrosopumilus maritimus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2416971122 | PMCID: PMC11761707 | PMID: 39823305
- Evidence: An initial model was generated in Phenix 1.2 ( 53 ) using the molecular replacement method and an AlphaFold2 ( 54 ) model of a truncated version of the protein consisting of only the first 300 amino acids.
- Full pipeline: normalisation [CCP4 v7.0] -> stage not stated [AlphaFold, PHENIX v1.2]

### Soil microbiome bacteria protect plants against filamentous fungal infections via intercellular contacts. (PNAS 2025)

- DOI: 10.1073/pnas.2418766122 | PMCID: PMC11762177 | PMID: 39813250
- Evidence: ( D ) The structure of Le1893 was predicted by AlphaFold2.
- Full pipeline: stage not stated [AlphaFold]

### Dual modes of DNA N&lt;sup&gt;6&lt;/sup&gt;-methyladenine maintenance by distinct methyltransferase complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2413037121 | PMCID: PMC11761967 | PMID: 39813249
- Evidence: Using AlphaFold 3 (AF3), we performed structure modeling of AMT6 and AMT7 apo-complexes (without DNA substrate) ( Fig.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### A divergent two-domain structure of the anti-Müllerian hormone prodomain. (PNAS 2025)

- DOI: 10.1073/pnas.2418088122 | PMCID: PMC11760506 | PMID: 39805014
- Evidence: Several large and well-resolved residues within the map allowed for the placement of helices which were modeled using AlphaFold-Multimer and secondarily confirmed using ModelAngelo ( 32 , 33 ) ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### The &lt;i&gt;Aedes aegypti&lt;/i&gt; mosquito evolves two types of prophenoloxidases with diversified functions. (PNAS 2025)

- DOI: 10.1073/pnas.2413131122 | PMCID: PMC11761970 | PMID: 39808654
- Evidence: To analyze the substrate pocket in the classical insect-type PPO1 from An. gambiae (Ang-PPO1), we utilized the AlphaFold 3 server to predict its structural model.
- Full pipeline: alignment/mapping [MAFFT] -> simulation/modelling [GROMACS] -> stage not stated [AlphaFold, AutoDock Vina, ChimeraX v1.8]

### An RNase III-processed sRNA coordinates sialic acid metabolism of &lt;i&gt;Salmonella enterica&lt;/i&gt; during gut colonization. (PNAS 2025)

- DOI: 10.1073/pnas.2414563122 | PMCID: PMC11745405 | PMID: 39792291
- Evidence: Sequence alignments and AlphaFold prediction revealed that proteins encoded by this locus share 26 to 71% amino acid identities with E. coli proteins involved in sialic acid metabolism ( SI Appendix , Table S1 ) ( 37 ).
- Full pipeline: alignment/mapping [AlphaFold] -> quantification [ImageJ] -> normalisation [ImageJ]

### Structural basis for TIR domain-mediated innate immune signaling by Toll-like receptor adaptors TRIF and TRAM. (PNAS 2025)

- DOI: 10.1073/pnas.2418988122 | PMCID: PMC11745336 | PMID: 39786929
- Evidence: Only the TIR domains of the adaptors are shown (TLR4 TIR : purple (AlphaFold two-predicted model); TLR3 TIR : blue (AlphaFold 2-predicted model); TRIF TIR-Fil : gray; TRAM TIR : orange).
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### Mutational analysis of an antimalarial drug target, <i>Pf</i>ATP4. (PNAS 2025)

- DOI: 10.1073/pnas.2403689122 | PMCID: PMC11745376 | PMID: 39773028
- Evidence: AlphaFold ( 29 ) is an AI program that can predict proteins’ three-dimensional structures from a given sequence using deep-learning neural network models.
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> simulation/modelling [NAMD] -> machine learning [AlphaFold]

### TRAMP assembly alters the conformation and RNA binding of Mtr4 and Trf4-Air2. (PNAS 2025)

- DOI: 10.1073/pnas.2414980121 | PMCID: PMC11725892 | PMID: 39752526
- Evidence: To best interpret the data, we have used the high-confidence regions (pLDDT > 40) of an AlphaFold2 Multimer model of full-length Trf4-Air2 ( 48 , 49 ) ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, PyMOL]

### PhiSiCal-Checkup: A Bayesian framework to validate amino acid conformations within experimental protein structures. (PNAS 2025)

- DOI: 10.1073/pnas.2416301121 | PMCID: PMC11725904 | PMID: 39746043
- Evidence: Another study earmarked for immediate future work is to analyze the distribution of conformational angles of protein structures not determined by experimental methods but predicted using programs such as AlphaFold 3 ( 22 ).
- Full pipeline: stage not stated [AlphaFold]

### Molecular basis of hemoglobin binding and heme removal in <i>Corynebacterium diphtheriae</i>. (PNAS 2025)

- DOI: 10.1073/pnas.2411833122 | PMCID: PMC11725911 | PMID: 39739808
- Evidence: Comparison to the AlphaFold Database model is presented in SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### In situ architecture of a nucleoid-associated biomolecular co-condensate that regulates bacterial cell division. (PNAS 2025)

- DOI: 10.1073/pnas.2419610121 | PMCID: PMC11725790 | PMID: 39739804
- Evidence: To overcome this limitation, we used AlphaFold-Multimer to predict potential configurations of PomX.
- Full pipeline: stage not stated [AlphaFold]

### Learning the language of antibody hypervariability. (PNAS 2025)

- DOI: 10.1073/pnas.2418918121 | PMCID: PMC11725859 | PMID: 39793083
- Evidence: Our implementation of structure prediction with AbMAP as a template-finding task shows promise, outperforming AlphaFold 2 and being competitive with OmegaFold in most cases, particularly for the functionally crucial CDR-H3 region.
- Full pipeline: stage not stated [AlphaFold, PyTorch v1.11.0]

### Molecular basis of Spns1-mediated lysophospholipid transport from the lysosome. (PNAS 2025)

- DOI: 10.1073/pnas.2409596121 | PMCID: PMC11725778 | PMID: 39739806
- Evidence: A predicted model of inward-facing Spns1 was generated by AlphaFold ( 32 ).
- Full pipeline: registration [MotionCor2, RELION v3.1] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, NAMD]

### Elucidation of a distinct photoreduction pathway in class II &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; photolyase. (PNAS 2025)

- DOI: 10.1073/pnas.2416284121 | PMCID: PMC11725880 | PMID: 39739803
- Evidence: Finally, the ET driving force, reorganization energy, and reduction potentials were calculated using the Marcus theory by bringing in the above kinetics parameters and ET distances obtained from the protein structure predicted by AlphaFold3.
- Full pipeline: stage not stated [AlphaFold]

### Tamsulosin ameliorates bone loss by inhibiting the release of Cl<sup>-</sup> through wedging into an allosteric site of TMEM16A. (PNAS 2025)

- DOI: 10.1073/pnas.2407493121 | PMCID: PMC11725887 | PMID: 39739807
- Evidence: We used a predicted structure of TMEM16A from AlphaFold2 as a reference for the density map using UCSF Chimera ( 49 , 50 ) to develop the model of TMEM16A.
- Full pipeline: structure determination [AlphaFold, PHENIX, UCSF Chimera] -> visualisation [ChimeraX]

### Tetrameric PilZ protein stabilizes stator ring in complex flagellar motor and is required for motility in &lt;i&gt;Campylobacter jejuni&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2412594121 | PMCID: PMC11725899 | PMID: 39793078
- Evidence: The full-length structure of FlgX was generated using ColabFold, an online implementation of AlphaFold2 ( 60 , 61 ).
- Full pipeline: alignment/mapping [CTFFIND, IMOD] -> structure determination [ChimeraX] -> stage not stated [AlphaFold, ColabFold, MotionCor2]

### Electron transfer in polysaccharide monooxygenase catalysis. (PNAS 2025)

- DOI: 10.1073/pnas.2411229121 | PMCID: PMC11725913 | PMID: 39793048
- Evidence: A structure was generated using AlphaFold2, and AlphaFill was used to position Cu in the active site.
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, Clustal Omega]

### PsDMAP1/PsTIP60-regulated H4K16ac is required for ROS-dependent virulence adaptation of &lt;i&gt;Phytophthora sojae&lt;/i&gt; on host plants. (PNAS 2025)

- DOI: 10.1073/pnas.2413127122 | PMCID: PMC11725902 | PMID: 39793040
- Evidence: Furthermore, we employed AlphaFold3 to predict the protein structures of PsTIP60, PsTIP60 S322A , and PsTIP60 S322D .
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, BLAST, PyMOL v2.6]

### A conifer metabolite corrects episodic ataxia type 1 by voltage sensor-mediated ligand activation of Kv1.1. (PNAS 2025)

- DOI: 10.1073/pnas.2411816122 | PMCID: PMC11745346 | PMID: 39793113
- Evidence: An atomic model for Kv1.1 was constructed from the predicted structure of the Kv1.1 monomer available in the AlphaFold database ( 37 ) (UNIPROT: AF- Q09470 -F1).
- Full pipeline: stage not stated [AlphaFold]

### Genesis and regulation of C-terminal cyclic imides from protein damage. (PNAS 2025)

- DOI: 10.1073/pnas.2415976121 | PMCID: PMC11725857 | PMID: 39793072
- Evidence: For the datasets “random 1”, “random 2”, “deamidation,” and “cleavage”, we extracted structural information by ChimeraX ( 44 ) from either experimentally determined structures that contain the site and have resolution ≤ 3.5Å, or high-confidence structures predicted by AlphaFold ( 45 ) (site pLDDT ≥ 70) if experimental structures were unavailable ( Fig.
- Full pipeline: stage not stated [AlphaFold, ChimeraX]

### Structural basis of nearest-neighbor cooperativity in the ring-shaped gene regulatory protein TRAP from protein engineering and cryo-EM. (PNAS 2025)

- DOI: 10.1073/pnas.2409030121 | PMCID: PMC11725872 | PMID: 39793047
- Evidence: Based on those criteria, and guided in part by loop modeling with Rosetta ( 40 ) and AlphaFold2 ( 41 ) ( Fig.
- Full pipeline: normalisation [ChimeraX] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### A broadly conserved gram-positive lipoprotein regulates cell elongation. (PNAS 2026)

- DOI: 10.1073/pnas.2610431123 | PMCID: PMC13321084 | PMID: 42335227
- Evidence: Large-scale AlphaFold-Multimer (AF-M) screens have emerged as a powerful approach to identify novel protein–protein interactions ( 31 – 33 ).
- Full pipeline: stage not stated [AlphaFold, Cellpose]

### Linear-time prediction of proteome-scale microbial protein interactions. (PNAS 2026)

- DOI: 10.1073/pnas.2610619123 | PMCID: PMC13291599 | PMID: 42308045
- Evidence: For AlphaFold3, we use the reported latency of 22 s per pair (up to 1024 tokens) on 16 A100 GPU (excluding MSA construction time) ( 39 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [PyTorch] -> visualisation [UMAP] -> stage not stated [AlphaFold, BLAST, STRING db]

### A teleost-specific oxygen-immunity axis where FIH activates NF-κB via competitive IκBα binding. (PNAS 2026)

- DOI: 10.1073/pnas.2529211123 | PMCID: PMC13291597 | PMID: 42308032
- Evidence: AlphaFold3-based structural modeling ( 73 ) and phylogenetic analysis ( 74 – 76 ) were used to examine structural features and evolutionary relationships.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### A bacterial symbiont and a plant virus enhance insect fitness by inducing physical defenses against fungal parasites. (PNAS 2026)

- DOI: 10.1073/pnas.2534981123 | PMCID: PMC13291671 | PMID: 42301775
- Evidence: The predicted structural models for Rickettsia TyrB and B. tabaci GOT2 ( Bt GOT2) were generated by the AlphaFold 3 webserver ( 47 ), with details in SI Appendix , Materials and Methods .
- Full pipeline: stage not stated [AlphaFold]

### Cryo-EM reveals a right-handed double-helix dimer architecture of PCDH15. (PNAS 2026)

- DOI: 10.1073/pnas.2607573123 | PMCID: PMC13273323 | PMID: 42263124
- Evidence: The initial model of PCDH15 EC1-7 was predicted using AlphaFold3 ( 14 ).
- Full pipeline: quantification [ImageJ] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold]

### &lt;i&gt;Arabidopsis&lt;/i&gt; YEATS domain proteins facilitate DNA double-strand break repair via homology-directed pathways. (PNAS 2026)

- DOI: 10.1073/pnas.2612171123 | PMCID: PMC13273319 | PMID: 42258726
- Evidence: ( A ) AlphaFold predicted 3D-structure of YAF9B ( 83 , 84 ) where the YEATS domain, A-Box, and B-Box are colored as in ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### mRNA delivery of a class 1/4 SARS-CoV-2 neutralizing antibody protects against diverse sarbecoviruses in a lethal mouse challenge model. (PNAS 2026)

- DOI: 10.1073/pnas.2536870123 | PMCID: PMC13268366 | PMID: 42258728
- Evidence: Although an atomic model of the complex could not be built due to low resolution of the EM density (5.2 Å) ( Table S2 ), we predicted the RBD epitope of this mAb by docking an AlphaFold 3 ( 61 ) model of Fab and Spike RBD into the density, which showed three Fabs interacting with RBDs in “up” conformations ( fig.
- Full pipeline: stage not stated [AlphaFold]

### Active zone plasticity couples sleep need to presynaptic hypophosphorylation. (PNAS 2026)

- DOI: 10.1073/pnas.2524065123 | PMCID: PMC13273273 | PMID: 42258713
- Evidence: Using AlphaFold3 ( 61 ), we predicted that Spn interacts extensively with the most abundant Drosophila PP1 subtype ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, ImageJ, Metascape, PyMOL, STRING db]

### Transition-state analysis of the arginine-specific human ADP-ribosyltransferase 1. (PNAS 2026)

- DOI: 10.1073/pnas.2604770123 | PMCID: PMC13229280 | PMID: 42201951
- Evidence: ( C ) AlphaFold 3 model of the hs ART1:NAD + : hs P2X7 complex, hs ART1 colored in red, hs P2X7 homotrimer colored in green, and NAD + is colored in white.
- Full pipeline: stage not stated [AlphaFold]

### amyloid-predict and LLPS-predict: Predicting phase separation propensities in the intrinsically disordered proteome. (PNAS 2026)

- DOI: 10.1073/pnas.2531932123 | PMCID: PMC13229271 | PMID: 42190015
- Evidence: ( 75 ) recently identified about ~28 k such IDR s—referred to as the IDRome —based on AlphaFold structural confidence scores (i.e. pLDDT).
- Full pipeline: machine learning [scikit-learn] -> stage not stated [AlphaFold]

### Harnessing polyploidy for climate-resilient crops: Lessons from the evolutionary model, allotetraploid cotton. (PNAS 2026)

- DOI: 10.1073/pnas.2522073123 | PMCID: PMC13229195 | PMID: 42189971
- Evidence: Beyond prediction, AI is instrumental in deciphering the complex cis-regulatory codes and underlying gene regulatory mechanisms ( 97 ), predicting protein structures with high accuracy [e.g., AlphaFold3 ( 98 )], and assisting in the design phase of synthetic biology applications ( 94 ).
- Full pipeline: stage not stated [AlphaFold]

### Uncovering ParB-dependent and -independent subclasses of T-dioxygenases from bacteriophage. (PNAS 2026)

- DOI: 10.1073/pnas.2522060123 | PMCID: PMC13229309 | PMID: 42189983
- Evidence: AlphaFold2 (AF2) and structure-based alignment searches consistently reveal Myxococcus xanthus ParB ( Mx ParB) ( 36 ) and Caulobacter crescentus ParB ( Cc ParB) ( 37 ) as the closest structural homologs of 5mYOX-associated ParBs ( Dataset S6 ) ( 40 , 41 ).
- Full pipeline: alignment/mapping [AlphaFold] -> stage not stated [MAFFT]

### ProteomeLM: A proteome-scale language model enables accurate and rapid prediction of protein-protein interactions and gene essentiality across taxa. (PNAS 2026)

- DOI: 10.1073/pnas.2524201123 | PMCID: PMC13214046 | PMID: 42160340
- Evidence: Structure-based ones, including docking ( 32 – 35 ) and multimeric folding algorithms like AlphaFold-Multimer ( 36 ), have achieved remarkable accuracy for specific interactions ( 37 ), but remain computationally intensive.
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold, STRING db]

### Systematic determination of disulfide bond reduction potentials reveals a nonequilibrium redox hierarchy in cyanobacteria. (PNAS 2026)

- DOI: 10.1073/pnas.2600150123 | PMCID: PMC13214033 | PMID: 42154557
- Evidence: ( C ) Distribution of nearest sulfur–sulfur (S–S) distances d for all cysteines in the Synechocystis AlphaFold proteome, used to classify intramolecular disulfides.
- Full pipeline: stage not stated [AlphaFold]

### Predictions from deep learning propose substantial protein-carbohydrate interplay. (PNAS 2026)

- DOI: 10.1073/pnas.2523342123 | PMCID: PMC13213957 | PMID: 42150072
- Evidence: Further, we included the computationally designed and experimentally viable lysozymes from ProGen, ( 23 ) with structures predicted by the Colab distribution of AlphaFold2 ( 53 ).
- Full pipeline: differential/statistical testing [RoseTTAFold] -> stage not stated [AlphaFold]

### Regulation of Pfh1 helicase activity by nucleic acid interactions and mitochondrial SSB. (PNAS 2026)

- DOI: 10.1073/pnas.2602528123 | PMCID: PMC13213944 | PMID: 42150082
- Evidence: ( A , Left ) Pfh1 central helicase domain structure bound to ssDNA and ATP was prepared by superimposing AlphaFold2 ( 58 ) Pfh1 prediction with the human Pif1 helicase bound to AMP-PNP (PDB 6HPH).
- Full pipeline: stage not stated [AlphaFold]

### Chiral inversion mutagenesis identifies geometrically constrained residues within self-associating low-complexity domains. (PNAS 2026)

- DOI: 10.1073/pnas.2535888123 | PMCID: PMC13167773 | PMID: 42090265
- Evidence: ( A ) AlphaFold-predicted structure of the full-length EMD protein and accompanying domain map.
- Full pipeline: stage not stated [AlphaFold]

### Importin-9 recognizes the winged-helix fold of ETS transcription factors to mediate nuclear import. (PNAS 2026)

- DOI: 10.1073/pnas.2536763123 | PMCID: PMC13142979 | PMID: 42066049
- Evidence: Comparisons between our experimentally determined EHF:IPO9 structure and the AlphaFold-multimer-predicted model reveal that, in its current state, AlphaFold Multimer V3 is unable to correctly predict key molecular details of the interaction interface ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Structural basis of iron piracy by human gut &lt;i&gt;Bacteroides&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2528036123 | PMCID: PMC13142918 | PMID: 42066043
- Evidence: The apo structures were solved by molecular replacement with computational models generated by AlphaFold2 ( 37 ).
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [AlphaFold]

### Computational design of an ultrapotent deltacoronavirus miniprotein inhibitor. (PNAS 2026)

- DOI: 10.1073/pnas.2533456123 | PMCID: PMC13142991 | PMID: 42054371
- Evidence: From the 101 MBs, 17 MBs were selected for expression and purification based on AlphaFold 3 metrics ipTM (>0.7) and pTM (>0.8) values and visual assessment of the MB, PDCoV IL121_2014 RBD binding interface from the AF3 predicted structure.
- Full pipeline: structure determination [ChimeraX, PHENIX, Topaz] -> stage not stated [AlphaFold, RELION v3.0]

### LRBA organizes distinct vesicular trafficking systems in distal nephron segments for water and sodium conservation. (PNAS 2026)

- DOI: 10.1073/pnas.2525505123 | PMCID: PMC13142998 | PMID: 42048445
- Evidence: ( A ) Structure of CTLA-4 predicted by AlphaFold 3.
- Full pipeline: stage not stated [AlphaFold]

### PMF proteins mediate mitochondrial fusion in Arabidopsis. (PNAS 2026)

- DOI: 10.1073/pnas.2601242123 | PMCID: PMC13123921 | PMID: 42018423
- Evidence: ( D ) Arabidopsis PMF1 protein structure predicted by AlphaFold3 and modeled in PyMOL3.0, with coloring based on pLDDT value predicted by AlphaFold.
- Full pipeline: differential/statistical testing [ggplot2, pheatmap] -> stage not stated [AlphaFold, ImageJ]

### Novel Knotted Solenoid fold with order-shifted coil arrangement leads to nontrivial 3&lt;sub&gt;1&lt;/sub&gt; topology. (PNAS 2026)

- DOI: 10.1073/pnas.2525920123 | PMCID: PMC13123833 | PMID: 42018416
- Evidence: After the identification of the first two proteins (UniProtKB ID: A0A7W8HX03 and A0A2X1AF08), FoldSeek ( 40 ) was employed on the AlphaFold representative database (afdb50, afdb-proteome, and afdb-swissprot; v4) and PDB to detect structural homologs.
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> simulation/modelling [GROMACS v2023.1] -> stage not stated [AlphaFold]

### Small subunit isoform diversity underlies structural heterogeneity in native plant Rubisco. (PNAS 2026)

- DOI: 10.1073/pnas.2519949123 | PMCID: PMC13099656 | PMID: 41984840
- Evidence: A predicted Rubisco structure using AlphaFold ( 33 ) was used and fitted into the corresponding density maps using Chimera ( 34 ).
- Full pipeline: structure determination [AlphaFold, PHENIX]

### Distinct evolutionary patterns of endemic and emerging parvoviruses and the origin of a new pandemic virus. (PNAS 2026)

- DOI: 10.1073/pnas.2515274123 | PMCID: PMC13099694 | PMID: 41980105
- Evidence: To model the homologous FPV mutations, the canine TfR structure was predicted using AlphaFold3 ( 71 ) and placed into the cryoEM density of the black-backed jackal (bbj) TfR in complex with the CPV-2 capsid using rigid-body fitting (EMDB ID: 20002) (PDB ID: 6OAS) ( 42 ).
- Full pipeline: differential/statistical testing [BEAST v1.10.4] -> simulation/modelling [BEAST v1.10.4] -> stage not stated [AlphaFold, ChimeraX, IQ-TREE]

### A secreted citrus protease cleaves an outer membrane protein of the Huanglongbing pathogen. (PNAS 2026)

- DOI: 10.1073/pnas.2528641123 | PMCID: PMC13079941 | PMID: 41945448
- Evidence: AlphaFold Structural Modeling.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, MAFFT v7.490, MUSCLE v5.1, Trimmomatic v0.39] -> quantification [Bioconductor, DESeq2] -> normalisation [Bioconductor, DESeq2] -> stage not stated [AlphaFold, ChimeraX, HMMER, ImageJ]

### Mycoviruses confer hypovirulence but enhance antifungal volatile organic compound production in a phytopathogenic fungus. (PNAS 2026)

- DOI: 10.1073/pnas.2526822123 | PMCID: PMC13080020 | PMID: 41941638
- Evidence: The 3D structure of SsAShV1 protein was predicted using AlphaFold 2 ( 55 ).
- Full pipeline: alignment/mapping [ChimeraX, MAFFT v7.0] -> normalisation [ComplexHeatmap] -> dimensionality reduction/clustering [ComplexHeatmap, HMMER v3.3.2] -> visualisation [ChimeraX, ComplexHeatmap, ImageJ] -> stage not stated [AlphaFold, BLAST, IQ-TREE v2.2.6]

### Semiochemicals and odorant receptors underlying potato cultivar susceptibility and resistance to potato tuber moth. (PNAS 2026)

- DOI: 10.1073/pnas.2537754123 | PMCID: PMC13079372 | PMID: 41941637
- Evidence: Consistent with this model, AlphaFold3 predictions indicate that PopeOR01, PopeOR15, and PopeOR73 assemble into OR–Orco complexes ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, R v4.1.2]

### Proteome-wide prediction of interactions between structured domains and peptide motifs reveals functionally coherent subnetworks. (PNAS 2026)

- DOI: 10.1073/pnas.2527957123 | PMCID: PMC13080015 | PMID: 41941631
- Evidence: Model Building Using AlphaFold.
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> stage not stated [AlphaFold, HMMER, Python, R, STRING db, scikit-learn]

### Clade C MERS-CoV camel strains vary in protease utilization during viral entry. (PNAS 2026)

- DOI: 10.1073/pnas.2525313123 | PMCID: PMC13056113 | PMID: 41920873
- Evidence: To investigate the structural consequences of the East African clade C aa substitutions in the NTD, we modeled the WT EMC and HKU270/CAC9690/ CAC10200 NTD in AlphaFold 3 ( 32 ).
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, ChimeraX]

### Descent from a common ancestor restricts exploration of protein sequence space. (PNAS 2026)

- DOI: 10.1073/pnas.2532018123 | PMCID: PMC13056090 | PMID: 41915737
- Evidence: A common approach is to train AI models on all natural protein sequences ( 8 ) and have them predict sequences with a desired property that have not occurred in evolution, in a similar manner that AlphaFold predicts structure.
- Full pipeline: stage not stated [AlphaFold]

### Fatty acid regulation of feeding in &lt;i&gt;Caenorhabditis&lt;/i&gt; elegans reveals the potential ancestral origin of a GLP-1-like multiagonist signaling system. (PNAS 2026)

- DOI: 10.1073/pnas.2530979123 | PMCID: PMC13056082 | PMID: 41911448
- Evidence: ( B ) Structural alignment of PDFR-1 by AlphaFold 2 with the active human GLP-1R (PDB:7DUR).
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega]

### Inhibition of coronaviral exoribonuclease activity by TRIM-mediated SUMOylation. (PNAS 2026)

- DOI: 10.1073/pnas.2528398123 | PMCID: PMC13037866 | PMID: 41871251
- Evidence: A model of Nsp14 SUMOylated at K9 and K200 was generated using AlphaFold 3 (see details in SI Appendix , Methods ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [AlphaFold, PyMOL]

### Convergent evolution increases boron transport through SNPs and tandem duplications at &lt;i&gt;BOR1&lt;/i&gt; and &lt;i&gt;BOR2&lt;/i&gt; in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2525676123 | PMCID: PMC13037888 | PMID: 41871252
- Evidence: The structural predictions of BOR1 and BOR2 were generated in AlphaFold2 ( 31 ) and visualized with ChimeraX (version 1.9) ( 64 ).
- Full pipeline: variant calling [VCFtools] -> normalisation [Python v3.8.3] -> differential/statistical testing [SciPy v1.6.2] -> visualisation [AlphaFold, ChimeraX v1.9] -> stage not stated [DELLY v0.8.3, GATK, GEMMA, PLINK, R v4.4.2, lme4, minimap2]

### SUN5 forms a regular protein lattice reinforcing the sperm head-tail junction. (PNAS 2026)

- DOI: 10.1073/pnas.2520626123 | PMCID: PMC13012075 | PMID: 41855266
- Evidence: Transmembrane Region, AlphaFold3 Predictions, and Modeling.
- Full pipeline: alignment/mapping [IMOD v4.12.62, RELION v5.0] -> structure determination [IMOD v4.12.62] -> stage not stated [AlphaFold, ChimeraX]

### Toward AI foundation models for epidemics: Promise, challenges, and paths forward. (PNAS 2026)

- DOI: 10.1073/pnas.2526192123 | PMCID: PMC13037875 | PMID: 41824492
- Evidence: Similar paradigms have already proven transformative across several scientific domains–for example, in molecular biology, physics-based simulations of protein folding generate massive synthetic corpora that underpin models like AlphaFold ( 72 ).
- Full pipeline: simulation/modelling [AlphaFold]

### Smooth-to-rough morphotype switching, a mechanism of phage resistance in &lt;i&gt;&lt;i&gt;Mycobacterium&lt;/i&gt; abscessus&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2531197123 | PMCID: PMC12993973 | PMID: 41811441
- Evidence: AlphaFold Protein Structure Prediction.
- Full pipeline: read trimming [SPAdes] -> stage not stated [AlphaFold, BLAST]

### The &lt;i&gt;Mycobacterium smegmatis bd&lt;/i&gt;-II terminal oxidase employs a carboxylate shift mechanism. (PNAS 2026)

- DOI: 10.1073/pnas.2515348123 | PMCID: PMC12994193 | PMID: 41805574
- Evidence: To obtain insight into substrate menaquinol binding, the Q-loop was explored by MD simulations based on our cryo-EM structure, in combination with an AlphaFold2 ( 32 ) model of the local unresolved parts of the structure ( Materials and Methods and SI Appendix , Table S5 and Fig.
- Full pipeline: simulation/modelling [AlphaFold]

### N6-methyladenosine modification of FZR1 mRNA positively regulates antiviral innate immunity by targeting the MAVS-TRAF3/6 axis. (PNAS 2026)

- DOI: 10.1073/pnas.2536412123 | PMCID: PMC12993966 | PMID: 41805567
- Evidence: To further corroborate this conclusion from a structural standpoint, we modeled the potential interaction patterns among FZR1, MAVS, and TRAF3/6 using AlphaFold3.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### Identification of CD164 as an essential entry receptor for divergent adeno-associated viruses. (PNAS 2026)

- DOI: 10.1073/pnas.2525865123 | PMCID: PMC12974471 | PMID: 41785320
- Evidence: The structure of human CD164 is predicted using AlphaFold3, and is shown with MD1, CRD, and MD2 domains.
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### Phosphatidylinositol 4,5-bisphosphate mediates Arl4D self-interaction to promote Pak1 signaling. (PNAS 2026)

- DOI: 10.1073/pnas.2533102123 | PMCID: PMC12974503 | PMID: 41779780
- Evidence: To test whether Arl4D self-association is functionally required, we used AlphaFold-predicted contacts to design a self-interaction-deficient variant (Arl4D mutant) ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Global analysis of protein degradation reveals instability of diverse regulators in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2515265123 | PMCID: PMC12974527 | PMID: 41774798
- Evidence: Protein features were sourced from the UniProt, EcoCyc, STRING, and AlphaFold databases or computed with the Biopython package ( SI Appendix , Table S1 ) ( 102 ).
- Full pipeline: quantification [limma] -> normalisation [limma] -> differential/statistical testing [XGBoost, limma] -> machine learning [XGBoost] -> stage not stated [AlphaFold, R, STRING db]

### Unified protein-small molecule graph neural networks for binding site prediction. (PNAS 2026)

- DOI: 10.1073/pnas.2524913123 | PMCID: PMC12974528 | PMID: 41774792
- Evidence: The second test set consists of AlphaFold-predicted structures corresponding to the 1,036 systems in the PLINDER test set, allowing evaluation of model performance on predicted protein structures rather than experimentally determined ones.
- Full pipeline: stage not stated [AlphaFold]

### Cryo-EM structure of locked spike glycoprotein from bat SARS-like coronavirus WIV1, molecular dynamics and biophysics across host range. (PNAS 2026)

- DOI: 10.1073/pnas.2516874123 | PMCID: PMC12933149 | PMID: 41706884
- Evidence: ( C ) Ribbon representation of AlphaFold3 generated complexes formed upon interaction of WIV1 S-RBD (dark midnight blue, with RBM highlighted in deep carmine pink) with bACE2 ( Upper Left ), hACE2-WT ( Upper Middle ), and hACE2-T92I ( Upper Right ), cACE2 ( Lower Left ), rdACE2 ( Lower Middle ), and pACE2 ( Lower Right ), as they appear at the end of 500 ns MD simulation; the dynamics of WIV1 S RB...
- Full pipeline: simulation/modelling [AlphaFold]

### A host-derived volatile primes context-dependent foraging behavior in parasitic nematodes via a lysosome-associated neural pathway. (PNAS 2026)

- DOI: 10.1073/pnas.2520778123 | PMCID: PMC12933127 | PMID: 41706887
- Evidence: Predicted tertiary structures were generated by AlphaFold2 ( 67 ) and rendered in PyMOL v3.1 ( https://pymol.org/ ) to highlight domain architecture and substrate-binding residues.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HISAT2 v2.1.0, Picard] -> quantification [HTSeq] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [AlphaFold, PyMOL v3.1]

### RNA-binding activity of PHGDH drives amyloid-beta production in a human brain organoid model of sporadic Alzheimer's disease. (PNAS 2026)

- DOI: 10.1073/pnas.2532234123 | PMCID: PMC12933074 | PMID: 41701839
- Evidence: Structural alignment using AlphaFold indicated no significant alteration to PHGDH’s overall structure ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [AlphaFold]

### GSK-3β coordinates axonal microtubule organization through Shot and Tau. (PNAS 2026)

- DOI: 10.1073/pnas.2516746123 | PMCID: PMC12933142 | PMID: 41701831
- Evidence: Our structural in silico analysis using ColabFold/AlphaFold2 suggests that a key GSK-3β target cluster is in a linker region between Shot’s two Eb1 dimer-binding SxIP sites and the SxLP site ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [AlphaFold, ColabFold] -> visualisation [ChimeraX] -> stage not stated [Fiji, ImageJ]

### Synaptic transmission: Munc13 assembles onto PI(4,5)P&lt;sub&gt;2&lt;/sub&gt;-rich domains into trimers that cooperate to capture vesicles. (PNAS 2026)

- DOI: 10.1073/pnas.2523347123 | PMCID: PMC12912961 | PMID: 41671179
- Evidence: The Syntaxin-1A juxtamembrane peptide was first modeled using AlphaFold2 ( 52 ) to obtain its atomistic structure, which was subsequently converted into a coarse-grained representation and topology using Martinize2 ( 53 ) and finally covalently attached to a coarse-grained DOPE lipid through the Maleimide-specific linker ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [IMOD] -> quantification [ImageJ] -> registration [IMOD] -> dimensionality reduction/clustering [ImageJ] -> simulation/modelling [GROMACS] -> visualisation [Topaz] -> stage not stated [AlphaFold, VMD]

### Functional and antigenic constraints on the Nipah virus fusion protein. (PNAS 2026)

- DOI: 10.1073/pnas.2529505123 | PMCID: PMC12885220 | PMID: 41650235
- Evidence: The prefusion structure is based on PDB 5EVM, the postfusion structure is an AlphaFold2-generated structure of postfusion Nipah virus F using the postfusion Langya virus F as template (PDB 8TVE) ( 21 ).
- Full pipeline: stage not stated [AlphaFold]

### Molecular assemblies and pharmacology of cerebellar GABA&lt;sub&gt;A&lt;/sub&gt; receptors. (PNAS 2026)

- DOI: 10.1073/pnas.2524504123 | PMCID: PMC12890884 | PMID: 41650215
- Evidence: For subunits identified in this study, molecular models of rat α6, β1, and β3 were predicted using the AlphaFold3 server ( 51 ), and residues were renumbered to reflect the removal of signal peptides.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Python, SciPy]

### Identification of a stylet-secreted effector protein family as a core component of root-knot nematode feeding tubes. (PNAS 2026)

- DOI: 10.1073/pnas.2520476123 | PMCID: PMC12890903 | PMID: 41632840
- Evidence: The Minc03784 amino acid sequence was used to generate a predicted 3D structural model via AlphaFold 3 ( 19 ) ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### A J-domain protein enhances memory by promoting physiological amyloid formation in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2516310123 | PMCID: PMC12867707 | PMID: 41615743
- Evidence: We compared the predicted structures of these three JDPs using AlphaFold3 and simulated the docking of Orb2 and Funes.
- Full pipeline: simulation/modelling [AlphaFold]

### OsKAT1 is a short Shaker potassium channel involved in root-to-shoot potassium translocation and contributes to rice grain yield. (PNAS 2026)

- DOI: 10.1073/pnas.2527650123 | PMCID: PMC12867649 | PMID: 41604258
- Evidence: The core structure of OsKAT1 (UniProt: Q5JM04 ), as predicted in the AlphaFold Protein Structure Database ( https://alphafold.ebi.ac.uk ), is nearly identical to that of the Arabidopsis AtKAT1 (UniProt: Q39128 ) ( Fig.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold]

### Germline fate determination by a single ARGONAUTE protein in &lt;i&gt;Ectocarpus&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2518712123 | PMCID: PMC12867755 | PMID: 41604268
- Evidence: Structural predictions for representative eukaryotic AGOs were generated with AlphaFold3 ( 98 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [MAFFT, Trimmomatic] -> alignment/mapping [MAFFT, STAR, featureCounts] -> quantification [DESeq2, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold]

### Soluble adenylyl cyclase in nonmammalian sperm is directly controlled by pH, not by HCO&lt;sub&gt;3&lt;/sub&gt;&lt;sup&gt;-&lt;/sup&gt; or Ca&lt;sup&gt;2&lt;/sup&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2505026123 | PMCID: PMC12867704 | PMID: 41591904
- Version used: **2.2.4**
- Evidence: Modeling in AlphaFold2 v2.2.4 was performed within the ColabFold v1.5.2 pipeline ( 96 ), with multiple sequence alignments generated using MMSeqs2 ( 97 ).
- Full pipeline: alignment/mapping [AlphaFold v2.2.4, ColabFold v1.5.2, MAFFT] -> stage not stated [BLAST, SciPy v1.15.1, statsmodels v0.14.4]

### Incomplete lineage sorting shaped mixed traits during a colobine primate radiation. (PNAS 2026)

- DOI: 10.1073/pnas.2524833123 | PMCID: PMC12867756 | PMID: 41576102
- Version used: **2.3.1**
- Evidence: Three-dimensional structural models of candidate genes were predicted using AlphaFold v2.3.1 ( 84 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold v2.3.1] -> stage not stated [BUSCO, RAxML v8.2.9]

### A surface-exposed cardiolipin synthase provides an unexpected paradigm for maintaining the Gram-negative outer membrane. (PNAS 2026)

- DOI: 10.1073/pnas.2524588123 | PMCID: PMC12846801 | PMID: 41570074
- Evidence: The predicted AlphaFold structure of the mature protein with its lipid anchor is shown in Fig.
- Full pipeline: stage not stated [AlphaFold, BLAST, ChimeraX]

### BORC assemblies integrate BLOC-1 subunits to diversify endosomal trafficking functions. (PNAS 2026)

- DOI: 10.1073/pnas.2515691123 | PMCID: PMC12846789 | PMID: 41557793
- Evidence: Given the presence of BORC and BLOC-1 subunits throughout Eukarya, we first generated AlphaFold3 models of BORC across several model species: Arabidopsis thaliana, Mixina glutinosa, Aplysia californica, Dictyostelium discoideum , Caenorhabditis elegans , and Homo sapiens .
- Full pipeline: stage not stated [AlphaFold]

### Dynamic regulation of receptor-modulated endothelial NADPH oxidases. (PNAS 2026)

- DOI: 10.1073/pnas.2531380123 | PMCID: PMC12846790 | PMID: 41557791
- Evidence: Structural modeling of NOX4 using AlphaFold2 ( 27 ) revealed the prominent loop E extending toward the luminal side of the ER, with the antibody recognition site exposed in this region ( Fig.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Molecular structure of the ESCRT-III-based archaeal CdvAB cell division machinery. (PNAS 2026)

- DOI: 10.1073/pnas.2525941123 | PMCID: PMC12818579 | PMID: 41543908
- Evidence: AlphaFold2 models ( 14 ) of S. acidocaldarius proteins are shown on the right.
- Full pipeline: alignment/mapping [MAFFT, PyMOL] -> structure determination [Coot, PHENIX, RELION] -> visualisation [ChimeraX v1.7.1] -> stage not stated [AlphaFold, MotionCor2]

### Unlocking the benefits of transparent and reusable science for climate risk management. (PNAS 2026)

- DOI: 10.1073/pnas.2422157123 | PMCID: PMC12818561 | PMID: 41533440
- Evidence: For example, Google DeepMind released noncommercial access to AlphaFold3 only after sustained calls from the scientific community, illustrating the synergy between a commercial actor’s pursuit of scientific credibility and the scientific community’s need to scrutinize, extend, test, and interpret the work ( 124 – 127 ).
- Full pipeline: stage not stated [AlphaFold]

### Phosphatase SHP2 pathogenic mutations enhance activity by altering conformational sampling. (PNAS 2026)

- DOI: 10.1073/pnas.2513851123 | PMCID: PMC12818432 | PMID: 41528873
- Evidence: Alternatively, the AlphaFold 2 predicted open conformations of 2P-BTLA bound SHP2 WT and SHP2 E139D suggest an interaction between residue 139 and Arg5 that may stabilize the open state ( SI Appendix , Fig.
- Full pipeline: normalisation [Coot, PHENIX] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Origin of class B J-domain proteins involved in amyloid transactions. (PNAS 2026)

- DOI: 10.1073/pnas.2522403123 | PMCID: PMC12799103 | PMID: 41512017
- Evidence: The presence of helix V in the G/F region was identified as described in ( 47 ) using AB C B’ (ST) -alignment and AlphaFold structural models of analyzed JDPs.
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega v1.2.2]

### Pathogen-inspired engineering of plant protease enhances late blight resistance. (PNAS 2026)

- DOI: 10.1073/pnas.2524700123 | PMCID: PMC12799129 | PMID: 41512033
- Evidence: The protein structures were predicted using AlphaFold Server ( https://alphafoldserver.com/ ) and further analyzed using PyMOL software.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, PyMOL]

### Distinct PlzC mechanisms integrate chemotaxis and c-di-GMP signaling to regulate &lt;i&gt;Vibrio cholerae&lt;/i&gt; motility and biofilm formation. (PNAS 2026)

- DOI: 10.1073/pnas.2511740123 | PMCID: PMC12799141 | PMID: 41512027
- Evidence: AlphaFold modeling predicted, with high confidence, that a specific α-helix in PlzC could mediate interaction with CheX, and identified potential interaction residues ( SI Appendix , Figs.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [AlphaFold]

### E2 variants for probing E3 ubiquitin ligase activities. (PNAS 2026)

- DOI: 10.1073/pnas.2524899122 | PMCID: PMC12773759 | PMID: 41481455
- Evidence: Notably, structural models of RNF14–E2 complexes generated by AlphaFold3 showed clashing between the E3 and UBE2L3 catalytic cysteines ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### A neutralizing APOA5 monoclonal antibody reduces amounts of lipoprotein lipase in capillaries and triggers hypertriglyceridemia. (PNAS 2026)

- DOI: 10.1073/pnas.2528664123 | PMCID: PMC12773762 | PMID: 41481469
- Evidence: ( 10 ) using mass photometry, and the 2:1 stoichiometry was subsequently modeled by AlphaFold3.
- Full pipeline: structure determination [ChimeraX] -> stage not stated [AlphaFold]

### Design of solubly expressed miniaturized SMART MHCs. (PNAS 2026)

- DOI: 10.1073/pnas.2505932123 | PMCID: PMC12773744 | PMID: 41481462
- Evidence: Finally, the resulting designs were evaluated using AlphaFold2 56 predictions with the MHC structure provided as a template.
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, PHENIX]

### Competition between a transmembrane helix on Scap and a membrane cholesterol regulates Scap-Insig interaction and SREBP activation. (PNAS 2026)

- DOI: 10.1073/pnas.2525043123 | PMCID: PMC12773782 | PMID: 41474747
- Evidence: 5 C ) predicted by AlphaFold2 ( 30 ).
- Full pipeline: structure determination [ChimeraX] -> stage not stated [AlphaFold]

### Systematic identification of microtubule lumen proteins reveals a taxane-sensitive luminal resident JPT2 regulating MEC17 accessibility. (PNAS 2026)

- DOI: 10.1073/pnas.2520123123 | PMCID: PMC12773733 | PMID: 41468432
- Evidence: Structural analysis using AlphaFold3 suggests that JPT2 may interact with β-Tubulin at the Paclitaxel-binding site, supporting its role as a key regulatory protein within the microtubule lumen.
- Full pipeline: stage not stated [AlphaFold]

### &lt;i&gt;Legionella&lt;/i&gt; effector Ceg10 acetylates RPS20 to inhibit host translation and induce cell cycle arrest. (PNAS 2026)

- DOI: 10.1073/pnas.2517995123 | PMCID: PMC12773746 | PMID: 41468429
- Evidence: Structural prediction using AlphaFold revealed that the N-terminal (residues 1 to 64) and the C-terminal (residues 286 to 374) regions are intrinsically disordered.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold]

### NFE2L1/Nrf1 forms a coactivator complex post-peptide:&lt;i&gt;N&lt;/i&gt;-glycanase-mediated sequence editing and mitigates proteasome dysfunction. (PNAS 2026)

- DOI: 10.1073/pnas.2517547123 | PMCID: PMC12773725 | PMID: 41468431
- Evidence: The NST region, which contains eight glycosylation sites, was predicted to have a large, disordered structure using the AlphaFold protein structure model (AF- Q14494 -F1-v4).
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### Detoxification of conifer antimicrobial defenses promotes entomopathogenic fungus infection of bark beetles. (PNAS 2026)

- DOI: 10.1073/pnas.2525513122 | PMCID: PMC12773783 | PMID: 41461027
- Evidence: Structural modeling using AlphaFold 3 predicted a potential protein–protein interaction between BbGT86 and BbMT85, and so we continued with our analyses on these candidates to learn if they were part of the methylglucosylation pathway for phenolics ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, Clustal Omega v1.2.2]

### Maintaining microbiota across diverse symbiotic organs in &lt;i&gt;Euprymna scolopes&lt;/i&gt;: Insights into shared immune responses. (PNAS 2026)

- DOI: 10.1073/pnas.2512903122 | PMCID: PMC12773714 | PMID: 41428895
- Evidence: S6 B ) and AlphaFold predicted conserved β-helical and α-helical domains ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold]

### Accurate prediction of protein structures and interactions using a three-track neural network. (Science 2021)

- DOI: 10.1126/science.abj8754 | PMCID: PMC7612213 | PMID: 34282049
- Evidence: The bi-annual Critical Assessment of Structure (CASP) meetings have demonstrated that deep learning methods such as AlphaFold ( 1 , 2 ) and trRosetta ( 3 ), that extract information from the large database of known protein structures in the PDB, outperform more traditional approaches that explicitly model the folding process.
- Full pipeline: machine learning [AlphaFold] -> stage not stated [RoseTTAFold]

### Protein import into peroxisomes occurs through a nuclear pore-like phase. (Science 2022)

- DOI: 10.1126/science.adf3971 | PMCID: PMC9795577 | PMID: 36520918
- Evidence: Secondary structure predictions were performed with AlphaFold ( 65 ).
- Full pipeline: stage not stated [AlphaFold, ImageJ]

### RNA-activated protein cleavage with a CRISPR-associated endopeptidase. (Science 2022)

- DOI: 10.1126/science.add7450 | PMCID: PMC10028731 | PMID: 36423276
- Evidence: Model building Initial protein models were generated using AlphaFold2 ( 40 ) and fit into the cryo-EM maps, and then manually edited using Coot ( 41 ), while RNA molecules were entirely de novo built in Coot.
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, Coot, Jupyter, MotionCor2, RELION]

### Robust deep learning-based protein sequence design using ProteinMPNN. (Science 2022)

- DOI: 10.1126/science.add2187 | PMCID: PMC9997061 | PMID: 36108050
- Evidence: We found that training models on backbones to which Gaussian noise (std=0.02Å) had been added improved sequence recovery on confident protein structure models generated by AlphaFold (average pLDDT>80.0) from UniRef50, while the sequence recovery on unperturbed PDB structures decreased as expected ( Table 1 ).
- Full pipeline: machine learning [AlphaFold]

### Hallucinating symmetric protein assemblies. (Science 2022)

- DOI: 10.1126/science.add1964 | PMCID: PMC9724707 | PMID: 36108048
- Evidence: The loss function guiding the search is computed by inputting N copies of the sequence into the AlphaFold2 (AF2) network ( 26 ), and combining structure prediction confidence metrics (pLDDT; per-residue structural accuracy ( 27 ), and pTM; an estimate of the TM-score ( 28 )) with a measure of cyclic symmetry (the standard deviation of the distances between the center of mass of adjacent protomers ...
- Full pipeline: stage not stated [AlphaFold, ChimeraX, RoseTTAFold]

### Structural basis for potent antibody neutralization of SARS-CoV-2 variants including B.1.1.529. (Science 2022)

- DOI: 10.1126/science.abn8897 | PMCID: PMC9580340 | PMID: 35324257
- Version used: **2.0**
- Evidence: Outputs from AlphaFold 2.0 modelling were used as initial models for Fab A19-46.1 and Fab A19-61.1.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold v2.0, ChimeraX, UCSF Chimera]

### Structural mechanism of outer kinetochore Dam1-Ndc80 complex assembly on microtubules. (Science 2023)

- DOI: 10.1126/science.adj8736 | PMCID: PMC7615550 | PMID: 38060647
- Evidence: Rigid-body placement of an AlphaFold2 prediction of the Ndc80c CH – Dam1 C-ter interface into cryo-EM density shows: (B) The Dam1 C-ter α-helix packs against a hydrophobic interface generated by the Ndc80:Nuf2 coiled-coil emerging from the Ndc80c CH domain (upper panel).
- Full pipeline: stage not stated [AlphaFold]

### Uncovering the functional diversity of rare CRISPR-Cas systems with deep terascale clustering. (Science 2023)

- DOI: 10.1126/science.adi1910 | PMCID: PMC10910872 | PMID: 37995242
- Evidence: Structural modeling of the β-CASP protein with AlphaFold2 ( 49 ) shows two distinct domains, namely, the N-terminal β-CASP domain ( Fig.
- Full pipeline: dimensionality reduction/clustering [Python] -> stage not stated [AlphaFold]

### In silico protein interaction screening uncovers DONSON's role in replication initiation. (Science 2023)

- DOI: 10.1126/science.adi3448 | PMCID: PMC10801813 | PMID: 37590370
- Evidence: AlphaFold2-multimer (AF-M) screen To discover novel DONSON interactors within DNA replication pathways, we performed an in silico screen using the AF-M program developed by DeepMind ( 35 , 61 ).
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, ChimeraX, STRING db]

### DNSN-1 recruits GINS for CMG helicase assembly during DNA replication initiation in &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (Science 2023)

- DOI: 10.1126/science.adi4932 | PMCID: PMC7615117 | PMID: 37590372
- Evidence: Model building and refinement To build the model of the CMG/TIM-1/TIPN-1/DNSN-1 complex bound to a fork DNA substrate, initial models for individual subunits were taken from the AlphaFold Protein Structure Database ( 65 , 66 ) and fitted as rigid-bodies to our cryo-EM density using UCSF Chimera ( 64 ) for MCM-2-7 subunits, the NTDs, AAA+ domains and winged-helix (WH) domains were fitted separately...
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, ImageJ, RELION]

### Deploying synthetic coevolution and machine learning to engineer protein-protein interactions. (Science 2023)

- DOI: 10.1126/science.adh1720 | PMCID: PMC10403280 | PMID: 37499032
- Evidence: Although AlphaFold and RoseTTAFold are useful for predicting 3D protein structures from the amino acid sequence, predicting de novo protein-protein interactions remains a challenge ( 43 ).
- Full pipeline: dimensionality reduction/clustering [igraph] -> visualisation [scikit-learn v1.2.2] -> stage not stated [AlphaFold, MACS2, PyTorch, RoseTTAFold]

### Structure of the R2 non-LTR retrotransposon initiating target-primed reverse transcription. (Science 2023)

- DOI: 10.1126/science.adg7883 | PMCID: PMC10499050 | PMID: 37023171
- Evidence: Structure prediction using AlphaFold ( 34 ) suggests that, in these retrotransposons, the APE domain has a distinct position to the RLE domain in R2Bm, suggesting there may be mechanistic differences in how target cleavage is coupled to reverse transcription ( fig.
- Full pipeline: stage not stated [AlphaFold]

### Systematic in vitro evolution in &lt;i&gt;Plasmodium falciparum&lt;/i&gt; reveals key determinants of drug resistance. (Science 2024)

- DOI: 10.1126/science.adk9893 | PMCID: PMC11809290 | PMID: 39607932
- Evidence: We obtained protein models using either SWISS-MODEL ( 43 ) or AlphaFold ( 44 ) and mapped predicted ligands, including inhibitors, using AlphaFill.
- Full pipeline: alignment/mapping [AlphaFold, GATK v3.5] -> visualisation [Cytoscape v3.9.1] -> stage not stated [DELLY, Picard, SAMtools, SnpEff]

### Identification of a factor that accelerates substrate release from the signal recognition particle. (Science 2024)

- DOI: 10.1126/science.adp0787 | PMCID: PMC7617331 | PMID: 39607913
- Evidence: Using the high-confidence AlphaFold2-predicted structure of TMEM208 ( fig.
- Full pipeline: stage not stated [AlphaFold]

### Regulated N-glycosylation controls chaperone function and receptor trafficking. (Science 2024)

- DOI: 10.1126/science.adp7201 | PMCID: PMC7617332 | PMID: 39509507
- Evidence: Based on an AlphaFold3 model of a pre-N-CCDC134 complex, we made three point mutations (hereafter “RLS”) on one face of a predicted helical segment of the pre-N domain ~40 a.a. distal to the SRT pseudosubstrate site in HSP90B1 ( fig.S7G ).
- Full pipeline: stage not stated [AlphaFold]

### Exploring structural diversity across the protein universe with The Encyclopedia of Domains. (Science 2024)

- DOI: 10.1126/science.adq4946 | PMCID: PMC7618865 | PMID: 39480926
- Evidence: Supplementary Material Supplementary The AlphaFold Protein Structure Database (AFDB) ( 1 , 2 ) is a groundbreaking initiative which significantly broadened the protein structure universe by expanding 3D representation to over 200 million UniProt sequences.
- Full pipeline: stage not stated [AlphaFold, ColabFold]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: A multiple sequence alignment of 5 concatenated repeats from the 42 orthologs was converted to a3m format and provided as the input for the ColabFold implementation of AlphaFold2 ( 21 , 55 ) with settings --num-recycle 40 --num-models 5.
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

### A kalihinol analog disrupts apicoplast function and vesicular trafficking in &lt;i&gt;P. falciparum&lt;/i&gt; malaria. (Science 2024)

- DOI: 10.1126/science.adm7966 | PMCID: PMC11793105 | PMID: 39325875
- Evidence: AlphaFold monomer V2.0 prediction for protein transport protein SEC13 (Q8I5B3) and protein structure were formed through ChimeraX.
- Full pipeline: differential/statistical testing [DESeq2, R] -> stage not stated [AlphaFold, ChimeraX]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Evidence: The structures of the SANT and HD domain of EP400 were predicted by AlphaFold2 and manually docked into their corresponding densities ( 66 , 67 ).
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Structure-guided discovery of ancestral CRISPR-Cas13 ribonucleases. (Science 2024)

- DOI: 10.1126/science.adq0553 | PMCID: PMC12165695 | PMID: 39024377
- Evidence: Specifically, we leveraged a Foldseek-clustered AlphaFold database ( 20 ), whose reduced search space makes slow-but-sensitive DALI-searches feasible (Methods).
- Full pipeline: dimensionality reduction/clustering [AlphaFold]

### Sculpting conducting nanopore size and shape through de novo protein design. (Science 2024)

- DOI: 10.1126/science.adn3796 | PMCID: PMC11549965 | PMID: 39024453
- Evidence: We previously found that AlphaFold2 with multiple recycles ( 30 ) could accurately predict the structures of designed TMBs from single-sequence input without sequence alignments ( 31 ) and that the confidence assigned to the model (pLDDT) was a good discriminator of the sequences with higher probability of experimentally folding ( 32 ).
- Full pipeline: alignment/mapping [AlphaFold]

### An intron endonuclease facilitates interference competition between coinfecting viruses. (Science 2024)

- DOI: 10.1126/science.adl1356 | PMCID: PMC11620839 | PMID: 38963841
- Evidence: Gp210 is an HNH endonuclease that inhibits ΦKZ replication Gp210 is predicted to be a histidine-asparagine-histidine (HNH) endonuclease based on sequence alignments and AlphaFold structure predictions ( Figs.
- Full pipeline: alignment/mapping [AlphaFold]

### Molecular mechanism of dynein-dynactin complex assembly by LIS1. (Science 2024)

- DOI: 10.1126/science.adk8544 | PMCID: PMC7615804 | PMID: 38547289
- Evidence: Models from the Protein Data Bank (PDB) or AlphaFold2 predictions (see section below) were docked into the respective cryo-EM maps as a rigid body using UCSF Chimera ( 107 ).
- Full pipeline: alignment/mapping [ChimeraX] -> quantification [R] -> registration [MotionCor2, RELION] -> differential/statistical testing [R] -> structure determination [PHENIX] -> machine learning [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ColabFold, ImageJ, UCSF Chimera]

### Native architecture of a human GBP1 defense complex for cell-autonomous immunity to infection. (Science 2024)

- DOI: 10.1126/science.abm9903 | PMCID: PMC12091997 | PMID: 38422126
- Evidence: Computational modeling of human GBP1 We enlisted AlphaFold2 to predict functional homologs of the human GBP protein family.
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [EMAN2, UCSF Chimera] -> stage not stated [AlphaFold, CellProfiler, ImageJ]

### A bacterial nutrition strategy for plant disease control. (Science 2025)

- DOI: 10.1126/science.ady8325 | PMCID: PMC12807533 | PMID: 41411414
- Evidence: AvrBs2 catalyzes UDP-α-D-galactose into xanthosan AlphaFold prediction revealed that AvrBs2 includes a C-terminal GDE-like domain ( fig.
- Full pipeline: stage not stated [AlphaFold]

### NUDT5 regulates purine metabolism and thiopurine sensitivity by interacting with PPAT. (Science 2025)

- DOI: 10.1126/science.adx9717 | PMCID: PMC12853130 | PMID: 41196949
- Evidence: AlphaFold3 ( 32 ) predicted that NUDT5 arginine 70 (R70) resides in the interface between NUDT5 and PPAT and forms salt bridges with PPAT glutamine 26 (Q26) and glutamate 228 (E228) ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### Structural basis of T-loop-independent recognition and activation of CDKs by the CDK-activating kinase. (Science 2025)

- DOI: 10.1126/science.adw0053 | PMCID: PMC7618291 | PMID: 41100585
- Evidence: This contradicts an early computational modelling study that suggested a head-to-tail interaction between CDK7 and CDK2 ( 23 ) but is compatible with predictions from AlphaFold3 (see below) ( 24 ).
- Full pipeline: stage not stated [AlphaFold]

### Architecture of the UBR4 complex, a giant E4 ligase central to eukaryotic protein quality control. (Science 2025)

- DOI: 10.1126/science.adv9309 | PMCID: PMC7618180 | PMID: 40875847
- Evidence: This E4 activity depends on the UBL domain which was predicted by AlphaFold3 ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### Vaccination with mRNA-encoded nanoparticles drives early maturation of HIV bnAb precursors in humans. (Science 2025)

- DOI: 10.1126/science.adr8382 | PMCID: PMC13164876 | PMID: 40373112
- Evidence: Model building was performed by docking homology models of trimer (generated by AlphaFold 3 ( 85 )) and Fab Fv (generated by AbodyBuilder2 ( 86 )) in UCSF ChimeraX ( 87 ), manually building and refining in Coot 0.9.8 ( 88 ) and real space refinement using Phenix ( 89 ).
- Full pipeline: differential/statistical testing [Matplotlib, seaborn] -> structure determination [AlphaFold, ChimeraX, Coot v0.9.8, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [NumPy]

### Design of high-specificity binders for peptide-MHC-I complexes. (Science 2025)

- DOI: 10.1126/science.adv0185 | PMCID: PMC13077772 | PMID: 40705892
- Evidence: S1B ), optimized their sequences for folding and binding using ProteinMPNN, and selected those that AlphaFold2 (AF2) ( 13 ) predicted to fold and bind as designed.
- Full pipeline: stage not stated [AlphaFold]

### De novo design and structure of a peptide-centric TCR mimic binding module. (Science 2025)

- DOI: 10.1126/science.adv3813 | PMCID: PMC12313176 | PMID: 40705894
- Evidence: Since crystal structures are not always available for a given pMHC antigen, we used AlphaFold ( 34 ) to predict the NY-ESO-1/HLA-A*02/β-2-microglobulin (β2M) structure, which together stabilize class I pMHC presentation.
- Full pipeline: stage not stated [AlphaFold]

### Cat1 forms filament networks to degrade NAD&lt;sup&gt;+&lt;/sup&gt; during the type III CRISPR-Cas antiviral response. (Science 2025)

- DOI: 10.1126/science.adv9045 | PMCID: PMC12162218 | PMID: 40208959
- Evidence: The AlphaFold3 ( 54 ) model of the CARF and the TIR domains were fitted to the maps using Chimera ( 55 ) and the models was built using Coot ( 56 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold]

### Programmable gene insertion in human cells with a laboratory-evolved CRISPR-associated transposase. (Science 2025)

- DOI: 10.1126/science.adt5199 | PMCID: PMC12326709 | PMID: 40373119
- Evidence: Based on analysis of an AlphaFold3-predicted ( 74 ) TnsC model, D44 is proximal to the ATP binding pocket, and N316 lies at the interaction interface between adjacent TnsC monomers near the target DNA ( fig.
- Full pipeline: stage not stated [AlphaFold]

### TIGR-Tas: A family of modular RNA-guided DNA-targeting systems in prokaryotes and their viruses. (Science 2025)

- DOI: 10.1126/science.adv9789 | PMCID: PMC12045711 | PMID: 40014690
- Evidence: Materials and Methods Structural similarity between SpCas9 RNA binding domain and IS110 To identify structural homologs of RNA-binding domains across Cas9 representatives, we performed a comprehensive structural search using DALI software on the AlphaFold database, clustered at 50% sequence identity using MMseqs2.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, MAFFT, PyMOL] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [MAFFT, PHENIX] -> stage not stated [CTFFIND, ColabFold, Coot, HMMER, MotionCor2, RELION, Topaz]

### Structural mechanism of LINE-1 target-primed reverse transcription. (Science 2025)

- DOI: 10.1126/science.ads8412 | PMCID: PMC7617806 | PMID: 40048554
- Evidence: Model building, refinement and AlphaFold3 prediction An AlphaFold2 ( 98 ) prediction was used as an initial model for model building into the consensus, open and closed fingers maps.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, PHENIX v1.21.1, RELION] -> stage not stated [CTFFIND, ChimeraX, ImageJ, MotionCor2, PyMOL, Python, REFMAC, Topaz]

### Evolutionary adaptations of doublet microtubules in trypanosomatid parasites. (Science 2025)

- DOI: 10.1126/science.adr5507 | PMCID: PMC7617938 | PMID: 40080577
- Evidence: Model building and protein identification Proteins were identified directly form the L. tarentolae maps using a combination of previous DMT structures, AI-guided structure predictions from AlphaFold2 (AF2) ( 54 ), automated de novo modeling using ModelAngelo ( 18 ), and manual de novo modeling using Coot ( 55 ).
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [napari] -> stage not stated [AlphaFold, CTFFIND v4.0, ChimeraX, HMMER, ImageJ, RELION]

### Molecular basis of FIGNL1 in dissociating RAD51 from DNA and chromatin. (Science 2025)

- DOI: 10.1126/science.adr7920 | PMCID: PMC7617353 | PMID: 39636933
- Evidence: Atomic model building and refinement A model of the FIGNL1 AAA domain hexamer was generated using AlphaFold2( 33 ).
- Full pipeline: registration [CTFFIND] -> structure determination [AlphaFold, PHENIX] -> visualisation [Fiji, ImageJ, RELION] -> stage not stated [Coot, Topaz]

### Rewiring STAT signaling from the cell surface with Trikine immunotherapeutics. (Science 2026)

- DOI: 10.1126/science.adx9954 | PMCID: PMC12963926 | PMID: 41712697
- Evidence: We modeled mouse IL-21 in complex with mouse extracellular domains of IL-21Ra and γ c using AlphaFold and then aligned the model with the human IL-21 signaling complex structure (PDB 8ENT) using ChimeraX.
- Full pipeline: quality control [FastQC] -> alignment/mapping [AlphaFold, ChimeraX, featureCounts] -> quantification [ComplexHeatmap, Seurat v5.1.0, featureCounts] -> normalisation [ComplexHeatmap, UMAP] -> dimensionality reduction/clustering [Monocle v1.3.7, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, MACS2, fgsea]

### DefensePredictor: A machine learning model to discover prokaryotic immune systems. (Science 2026)

- DOI: 10.1126/science.adv7924 | PMCID: PMC13092281 | PMID: 41926577
- Evidence: The AlphaFold3-predicted structure of DS-8 ( figs.
- Full pipeline: stage not stated [AlphaFold]

### Cryo-electron microscopy structure of the budding yeast telomerase holoenzyme. (Science 2026)

- DOI: 10.1126/science.adz5344 | PMCID: PMC7619062 | PMID: 41886584
- Evidence: We further verified the potential presence of the ZnF motif in some of these Est2/TERT using AlphaFold3 prediction ( fig.
- Full pipeline: quantification [ImageJ] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, CTFFIND v4.1, Python, RELION v5.0, Topaz]

### Cryo-electron microscopic visualization of RAD51 filament assembly and end-capping by XRCC3-RAD51C-RAD51D-XRCC2. (Science 2026)

- DOI: 10.1126/science.aea1546 | PMCID: PMC7618403 | PMID: 41196948
- Evidence: Heterotetrameric XRCC3-RAD51C-RAD51D-XRCC2 assembles RAD51 filaments AlphaFold3 modeling ( 42 ) of both BCDX2 and CX3 revealed that RAD51B and XRCC3 engage a common interface on RAD51C ( Fig.
- Full pipeline: stage not stated [AlphaFold]

### Termination of the integrated stress response. (Science 2026)

- DOI: 10.1126/science.adw5137 | PMCID: PMC7618491 | PMID: 41231936
- Evidence: Model building Initial models were generated with AlphaFold2 ( 46 ) for each subunit of eIF2 and eIF2B while R15B was predicted in the context of eIF2α and eIF2γ.
- Full pipeline: registration [RELION v5.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, PyMOL]

### Poxvirus attack of antiviral defense pathways unleashes an effector-triggered NF-κB response. (Science 2026)

- DOI: 10.1126/science.adw4937 | PMCID: PMC13041778 | PMID: 41678605
- Evidence: AlphaFold 3 structure predictions Amino acid sequences for proteins of interest were obtained from NCBI.
- Full pipeline: quality control [Cutadapt v1.18, FastQC] -> read trimming [Cutadapt v1.18, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.42.1, featureCounts] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, R]

### Structure and organization of AMPA receptor-TARP complexes in the mammalian cerebellum. (Science 2026)

- DOI: 10.1126/science.aeb3577 | PMCID: PMC7619101 | PMID: 41379938
- Evidence: Initial models for GluA4 and TARP γ7 were generated from AlphaFold3 (Uniprot ID I3L8N9 and P62956 ), while initial models for GluA1 were from PDB 7OCE (LBD and TMD) and Alphafold3 (Uniprot ID A0A286ZS63 for NTD).
- Full pipeline: alignment/mapping [MUSCLE] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [PyMOL v2.5] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

### Recurrent acquisition of nuclease-protease pairs in antiviral immunity. (Science 2026)

- DOI: 10.1126/science.aea8769 | PMCID: PMC12799240 | PMID: 41231971
- Evidence: To understand how proteolysis activates HamM nuclease activity, we compared the AlphaFold-predicted structure of HamM to a homologous MBL hydrolase-type nuclease involved in natural competence ( 20 , 25 ).
- Full pipeline: stage not stated [AlphaFold, Canu]

