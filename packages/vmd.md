# VMD

- **Category:** md
- **Papers in survey:** 165
- **Journals:** PNAS (124), Nature (34), Cell (5), Science (2)
- **Years:** 2021 (9), 2022 (30), 2023 (31), 2024 (38), 2025 (44), 2026 (13)
- **Versions named:** 1.9.3 (9), 1.9.4 (6), 1.9 (2), 1.94 (2), 1.9.4a (2), 2.0.0a (1)
- **Pipeline stages it appears in:** simulation/modelling (73), visualisation (49), structure determination (3), alignment/mapping (2), machine learning (1), quantification (1)

## Papers

### Virus-encoded histone doublets are essential and form nucleosome-like structures. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.032 | PMCID: PMC8357426 | PMID: 34297924
- Version used: **1.9.3**
- Evidence: ...https://www.ks.uiuc.edu/Research/namd/ CHARMM36 Forcefield Parameters Huang and MacKerell, 2013 http://mackerell.umaryland.edu/charmm_ff.shtml#charmm VMD (ver 1.9.3) Humphrey et al., 1996 . https://www.ks.uiuc.edu/Research/vmd/ CPPTRAJ (ver 18) Roe and Cheatham, 2013 https://ambermd.org/AmberTools.php Resource availability Lead contact The lead contact is Karolin Luger ( karolin.luger@colorado.edu...
- Full pipeline: alignment/mapping [MAFFT] -> quantification [R, RSEM, edgeR] -> normalisation [R, RSEM, edgeR] -> structure determination [PHENIX] -> stage not stated [NAMD, UCSF Chimera, VMD v1.9.3]

### Bacterial Vipp1 and PspA are members of the ancient ESCRT-III membrane-remodeling superfamily. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.041 | PMCID: PMC8281802 | PMID: 34166615
- Evidence: Initial structures for minimization were created in VMD by manually copying rung three and translating it N times, where N is the desired number of rungs.
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE, MotionCor2] -> stage not stated [GROMACS, HMMER, ImageJ, PHENIX, RELION v3.1, VMD]

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Evidence: ...0.1002/jcc.21787 Alpha Fold Jumper et al., 2021 ; Varadi et al., 2022 https://doi.org/10.1038/s41586-021-03819-2 https://doi.org/10.1093/nar/gkab1061 VMD Humphrey et al., 1996 https://doi.org/10.1016/0263-7855(9600018-5) Multi-Seq VMD plugin Roberts et al.
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### Structure of a fully assembled tumor-specific T cell receptor ligated by pMHC. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.010 | PMCID: PMC9630439 | PMID: 35985289
- Evidence: ...mit.edu/cb/topaz/ UCSF ChimeraX Pettersen et al., 2021 RRID:SCR_015872 UCSF Chimera Pettersen et al., 2004 RRID:SCR_004097 Visual Molecular Dynamics (VMD) v1.9.3 Humphrey et al., 1996 www.ks.uiuc.edu/Research/vmd/vmd-1.9.3/ Other DNA sequencing Source Bioscience N/A Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulf...
- Full pipeline: simulation/modelling [ChimeraX, UCSF Chimera, VMD] -> stage not stated [CCP4, GROMACS v2020.6, MDAnalysis v0.20.1, NumPy v1.19.5, PHENIX, PyMOL]

### Targeting Ras-, Rho-, and Rab-family GTPases via a conserved cryptic pocket. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.017 | PMCID: PMC11531380 | PMID: 39255801
- Evidence: 65 Visual examination of MD trajectories was performed using VMD package.
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CCP4] -> simulation/modelling [VMD] -> structure determination [PHENIX]

### Structures of the TMC-1 complex illuminate mechanosensory transduction. (Nature 2022)

- DOI: 10.1038/s41586-022-05314-8 | PMCID: PMC9605866 | PMID: 36224384
- Evidence: Starting from the cryo-EM modelled structure, a C-terminal carboxylic cap group, an N-terminal ammonium capping group, missing side chains, and all the hydrogen atoms were modelled using the PSFGEN plugin of VMD 61 .
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [ChimeraX, PHENIX] -> stage not stated [NAMD, UCSF Chimera, VMD]

### Architecture and self-assembly of the jumbo bacteriophage nuclear shell. (Nature 2022)

- DOI: 10.1038/s41586-022-05013-4 | PMCID: PMC9365700 | PMID: 35922510
- Evidence: Structure visualization and figure generation Density maps, coordinate models and simulation trajectories were visualized and figures were generated with PyMOL-v2.5 (Schrödinger2021), UCSF Chimera-v1.15 35 , ChimeraX-v1.2.5 89 , and VMD-1.9.4a35 90 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [ChimeraX, MDTraj, PyMOL, VMD] -> structure determination [ChimeraX, PHENIX, PyMOL, VMD] -> visualisation [ChimeraX, PyMOL, VMD] -> stage not stated [UCSF Chimera]

### Opening of glutamate receptor channel to subconductance levels. (Nature 2022)

- DOI: 10.1038/s41586-022-04637-w | PMCID: PMC9068512 | PMID: 35444281
- Version used: **1.9.3**
- Evidence: 74 ) and VMD 1.9.3 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot v0.9.2] -> stage not stated [CTFFIND v1.06, PHENIX v1.18, RELION v3.1, UCSF Chimera v1.14, VMD v1.9.3]

### Reconstructed covalent organic frameworks. (Nature 2022)

- DOI: 10.1038/s41586-022-04443-4 | PMCID: PMC8986529 | PMID: 35388196
- Evidence: The Multiwfn program 57 was used for IGM analyses and the VMD program 58 was used for visualization.
- Full pipeline: visualisation [VMD]

### Inhibition of calcium-triggered secretion by hydrocarbon-stapled peptides. (Nature 2022)

- DOI: 10.1038/s41586-022-04543-1 | PMCID: PMC8967716 | PMID: 35322233
- Evidence: Initial coordinates for the S 5 residues were generated by mutating the native residues into Lys using PyMol v.2.5.1 (Schrödinger), and then using the VMD mutate command 64 to change Lys into S 5.
- Full pipeline: quantification [ImageJ v2.0.0] -> simulation/modelling [NAMD] -> stage not stated [EMAN2, PyMOL v2.5.1, VMD]

### Visualizing protein breathing motions associated with aromatic ring flipping. (Nature 2022)

- DOI: 10.1038/s41586-022-04417-6 | PMCID: PMC8866124 | PMID: 35173330
- Evidence: Using VMD 73 , coordinates of the dimer from PDB 2FPE were inserted in the box of dimensions with a minimum distance of 2 Å in each direction between each atom and any box side.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, VMD]

### Sialoglycan binding triggers spike opening in a human coronavirus. (Nature 2023)

- DOI: 10.1038/s41586-023-06599-z | PMCID: PMC10700143 | PMID: 37794193
- Evidence: VMD 63 was used to generate molecular graphics.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CCP4, RELION v3.1.1, VMD]

### PLSCR1 is a cell-autonomous defence factor against SARS-CoV-2 infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06322-y | PMCID: PMC10371867 | PMID: 37438530
- Evidence: The hydrogen bond analysis was performed with VMD.
- Full pipeline: alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2, R] -> simulation/modelling [AlphaFold, GROMACS v2021.3, Python] -> stage not stated [PyMOL, VMD]

### Class B1 GPCR activation by an intracellular agonist. (Nature 2023)

- DOI: 10.1038/s41586-023-06169-3 | PMCID: PMC10307627 | PMID: 37286611
- Version used: **1.9.3**
- Evidence: The missing hydrogen atoms were built with the program VMD (v.1.9.3) 44 .
- Full pipeline: registration [RELION] -> simulation/modelling [MDTraj v1.9.8, NAMD v2.13, seaborn] -> visualisation [MDTraj v1.9.8, seaborn] -> stage not stated [Fiji, ImageJ, VMD v1.9.3]

### In situ architecture of the ER-mitochondria encounter structure. (Nature 2023)

- DOI: 10.1038/s41586-023-06050-3 | PMCID: PMC7614606 | PMID: 37165187
- Evidence: Analyses and system preparation were performed using VMD 73 and ChimeraX 64 .
- Full pipeline: alignment/mapping [IMOD, UCSF Chimera] -> quantification [ImageJ] -> simulation/modelling [NAMD] -> structure determination [IMOD] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, R, VMD]

### Visualizing the disordered nuclear transport machinery in situ. (Nature 2023)

- DOI: 10.1038/s41586-023-05990-0 | PMCID: PMC10156602 | PMID: 37100914
- Evidence: We used the VMD software to visualize all systems 85 .
- Full pipeline: simulation/modelling [GROMACS v2020.6, LAMMPS] -> visualisation [VMD] -> stage not stated [AlphaFold]

### Structural basis for bacterial energy extraction from atmospheric hydrogen. (Nature 2023)

- DOI: 10.1038/s41586-023-05781-7 | PMCID: PMC10017518 | PMID: 36890228
- Evidence: Molecular visualization and analyses were performed using VMD software 68 .
- Full pipeline: simulation/modelling [GROMACS v2021.3] -> structure determination [ChimeraX v1.3, PHENIX] -> visualisation [AlphaFold, VMD] -> stage not stated [CTFFIND v4.1.8, Coot, RELION v3.1.2]

### Autoregulation of GPCR signalling through the third intracellular loop. (Nature 2023)

- DOI: 10.1038/s41586-023-05789-z | PMCID: PMC10033409 | PMID: 36890236
- Version used: **1.9.3**
- Evidence: Molecular structure representations were created using VMD (version 1.9.3) 65 and Pymol (version 2.0.6) 66 .
- Full pipeline: simulation/modelling [GROMACS] -> visualisation [ggplot2] -> stage not stated [VMD v1.9.3]

### Population-based heteropolymer design to mimic protein mixtures. (Nature 2023)

- DOI: 10.1038/s41586-022-05675-0 | PMCID: PMC10468399 | PMID: 36890370
- Evidence: VMD was used for visualization of the resulting trajectories 43 .
- Full pipeline: simulation/modelling [VMD] -> visualisation [VMD]

### Structure of the human dopamine transporter and mechanisms of inhibition. (Nature 2024)

- DOI: 10.1038/s41586-024-07739-9 | PMCID: PMC11324517 | PMID: 39112705
- Evidence: The protein was internally hydrated using the DOWSER plugin 67 , 68 of VMD 69 .
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX v1.20.1] -> stage not stated [PyMOL, VMD]

### Cryo-EM architecture of a near-native stretch-sensitive membrane microdomain. (Nature 2024)

- DOI: 10.1038/s41586-024-07720-6 | PMCID: PMC11324527 | PMID: 39048819
- Version used: **1.9**
- Evidence: The CG protein model was then manually positioned around the tubule membrane using VMD v.1.9 70 .
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.8.9.2, PHENIX v1.20] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, Cellpose v2.0, RELION v2.1.0, VMD v1.9]

### Membraneless channels sieve cations in ammonia-oxidizing marine archaea. (Nature 2024)

- DOI: 10.1038/s41586-024-07462-5 | PMCID: PMC11153153 | PMID: 38811725
- Version used: **1.94**
- Evidence: MD simulations The Nm SLP hexamer structure was prepared for atomistic MD simulation using VMD (v.1.94) 67 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [NAMD v2.14, VMD v1.94] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold v2.2.0, MotionCor2]

### Kainate receptor channel opening and gating mechanism. (Nature 2024)

- DOI: 10.1038/s41586-024-07475-0 | PMCID: PMC11186766 | PMID: 38778115
- Version used: **1.9.4**
- Evidence: Molecular dynamics trajectory analysis Post-processing and analysis of the trajectories were carried out using CPPTRAJ 70 module of AmberTools20 and VMD 1.9.4 71 .
- Full pipeline: simulation/modelling [VMD v1.9.4] -> structure determination [Coot, PHENIX, PyMOL] -> visualisation [ChimeraX, PyMOL]

### Dopant-additive synergism enhances perovskite solar modules. (Nature 2024)

- DOI: 10.1038/s41586-024-07228-z | PMCID: PMC11006611 | PMID: 38438066
- Evidence: The structures were visualized using VESTA 45 and VMD 46 software.
- Full pipeline: visualisation [VMD]

### A skin-permeable polymer for non-invasive transdermal insulin delivery. (Nature 2025)

- DOI: 10.1038/s41586-025-09729-x | PMCID: PMC12695667 | PMID: 41261125
- Evidence: VMD 52 was used for trajectory visualization.
- Full pipeline: simulation/modelling [GROMACS v2020.6, VMD] -> visualisation [VMD] -> stage not stated [ImageJ]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Version used: **1.94**
- Evidence: Visualization of the trajectories was carried out using VMD v.1.94 software.
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### Structure and mechanism of the mitochondrial calcium transporter NCLX. (Nature 2025)

- DOI: 10.1038/s41586-025-09491-0 | PMCID: PMC12571890 | PMID: 40931067
- Evidence: Simulations were visualized and analysed using Visual Molecular Dynamics (VMD) 83 and PyMOL 70 .
- Full pipeline: simulation/modelling [VMD] -> structure determination [AlphaFold, PHENIX] -> machine learning [Topaz v0.2.4] -> visualisation [ChimeraX, PyMOL, UCSF Chimera, VMD]

### Experimental determination of partial charges with electron diffraction. (Nature 2025)

- DOI: 10.1038/s41586-025-09405-0 | PMCID: PMC12408337 | PMID: 40836092
- Version used: **2.0.0a**
- Evidence: 10 were generated with VMD v.2.0.0a5 as follows.
- Full pipeline: stage not stated [VMD v2.0.0a]

### Structural basis for the dynamic regulation of mTORC1 by amino acids. (Nature 2025)

- DOI: 10.1038/s41586-025-09428-7 | PMCID: PMC12507694 | PMID: 40836086
- Evidence: Trajectory analyses of RMSD were performed using the RMSD Trajectory Tool in VMD 37 .
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [AlphaFold, ChimeraX v1.8, Coot v0.9.8] -> machine learning [Topaz] -> stage not stated [CTFFIND v4.1.14, MotionCor2, PHENIX v2.0, RELION v5.0]

### Complete computational design of high-efficiency Kemp elimination enzymes. (Nature 2025)

- DOI: 10.1038/s41586-025-09136-2 | PMCID: PMC12310539 | PMID: 40533551
- Evidence: Additionally, the volume of the ligand was calculated using the mol_volume package in VMD 90 .
- Full pipeline: dimensionality reduction/clustering [MDTraj] -> simulation/modelling [MDTraj] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ColabFold, PyMOL, VMD]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: Simulations were performed using the Amber20 package, and structural and trajectory analyses were conducted with visual molecular dynamics (VMD) 73 .
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### The structure of apolipoprotein B100 from human low-density lipoprotein. (Nature 2025)

- DOI: 10.1038/s41586-024-08467-w | PMCID: PMC11839476 | PMID: 39662503
- Version used: **1.9.4**
- Evidence: Model building and visualization were performed using a combination of VMD (v.1.9.4) 52 and ChimeraX (v.1.6.1) 45 , 53 .
- Full pipeline: simulation/modelling [NAMD v2.14, PHENIX v1.20] -> structure determination [PHENIX v1.20] -> machine learning [PHENIX v1.20] -> visualisation [ChimeraX, VMD v1.9.4] -> stage not stated [AlphaFold, ColabFold]

### Mis-splicing of a neuronal microexon promotes CPEB4 aggregation in ASD. (Nature 2025)

- DOI: 10.1038/s41586-024-08289-w | PMCID: PMC11711090 | PMID: 39633052
- Evidence: 2j were generated using VMD 73 (v.1.9.4).
- Full pipeline: simulation/modelling [MDAnalysis, MDTraj, OpenMM v7.5] -> visualisation [Fiji, ImageJ] -> stage not stated [VMD]

### Structural basis of fungal β-1,3-glucan synthase inhibition by caspofungin. (Nature 2026)

- DOI: 10.1038/s41586-026-10409-7 | PMCID: PMC13249079 | PMID: 42020744
- Version used: **1.9**
- Evidence: VMD (v.1.9) 66 was used for visualization of molecular dynamics simulation results; Python 3 and MDAnalysis (v.2.7.0) 67 were used to analyse molecular dynamics results and generate molecular dynamics-related figures.
- Full pipeline: alignment/mapping [UCSF Chimera] -> registration [RELION] -> simulation/modelling [GROMACS, MDAnalysis v2.7.0, Python, VMD v1.9] -> structure determination [Coot v0.98, UCSF Chimera] -> visualisation [MDAnalysis v2.7.0, Python, VMD v1.9] -> stage not stated [AlphaFold, ChimeraX v1.10, PHENIX v1.20, PyMOL v3.1]

### Snapshots of the dynamic basis of NTSR1 G protein subtype promiscuity. (Nature 2026)

- DOI: 10.1038/s41586-026-10120-7 | PMCID: PMC13083256 | PMID: 41813894
- Evidence: VMD 55 and Python scripting were employed for analysis.
- Full pipeline: simulation/modelling [NAMD] -> structure determination [Coot, PHENIX] -> stage not stated [Python, VMD]

### Sea level much higher than assumed in most coastal hazard assessments. (Nature 2026)

- DOI: 10.1038/s41586-026-10196-1 | PMCID: PMC13083249 | PMID: 41781624
- Evidence: To evaluate the relative impact of vertical reference issues with respect to other (DEM-dependent) uncertainties, we performed a detailed meta-analysis for the Vietnamese Mekong Delta (VMD).
- Full pipeline: visualisation [QGIS v3.28.6] -> stage not stated [VMD]

### Integrase anchors viral RNA to the HIV-1 capsid interior. (Nature 2026)

- DOI: 10.1038/s41586-026-10154-x | PMCID: PMC13102720 | PMID: 41708858
- Evidence: The protein complex was then solvated in a periodic box of TIP3P water molecules 86 , 87 using the solvate plug-in in Visual Molecular Dynamics (VMD) v.1.9.4a57, compiled using Python (v.3.9) 88 .
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0, RELION] -> normalisation [ImageJ, NAMD v3.0.1] -> simulation/modelling [VMD] -> structure determination [ChimeraX, Coot, IMOD] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PyMOL, Topaz, UCSF Chimera]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Evidence: For each scenario, lipid positions within the membrane were randomly shuffled using the Membrane Mixer plugin 92 in VMD to minimize any biases from initial lipid placement, resulting in three replicas for each condition, totaling six replicas overall.
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **1.9.4**
- Evidence: Depictions were generated with VMD (v.1.9.4).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Common sequence motifs of nascent chains engage the ribosome surface and trigger factor. (PNAS 2021)

- DOI: 10.1073/pnas.2103015118 | PMCID: PMC8719866 | PMID: 34930833
- Evidence: The analysis of the metadynamics trajectory and the assignment of microstates was carried out in VMD software ( 65 ) using the METAGUI plugin ( 66 ) and Plumed 2.1 ( 62 ).
- Full pipeline: simulation/modelling [GROMACS v5.0.4, MDAnalysis, VMD]

### Amyloid-β peptide dimers undergo a random coil to β-sheet transition in the aqueous phase but not at the neuronal membrane. (PNAS 2021)

- DOI: 10.1073/pnas.2106210118 | PMCID: PMC8488611 | PMID: 34544868
- Evidence: Snapshots of the representative structures from the transition network were rendered using the visual molecular dynamics (VMD) program ( 68 ).
- Full pipeline: simulation/modelling [GROMACS, VMD] -> visualisation [VMD] -> stage not stated [Python]

### Dual nature of human ACE2 glycosylation in binding to SARS-CoV-2 spike. (PNAS 2021)

- DOI: 10.1073/pnas.2100425118 | PMCID: PMC8126795 | PMID: 33903171
- Evidence: The MD trajectories were analyzed with Visual Molecular Dynamics (VMD) ( 40 ) and MDAnalysis package ( 41 ).
- Full pipeline: simulation/modelling [GROMACS v2019.6, MDAnalysis, VMD]

### Early-stage dynamics of chloride ion-pumping rhodopsin revealed by a femtosecond X-ray laser. (PNAS 2021)

- DOI: 10.1073/pnas.2020486118 | PMCID: PMC8020794 | PMID: 33753488
- Evidence: The VMD program ( 52 ) was used to visualize the simulation trajectories, and the distances were extracted using the GROMACS program.
- Full pipeline: simulation/modelling [GROMACS v5.1.2, VMD] -> structure determination [Coot] -> visualisation [VMD] -> stage not stated [CCP4, PHENIX, UCSF Chimera]

### Nonselective cation permeation in an AMPA-type glutamate receptor. (PNAS 2021)

- DOI: 10.1073/pnas.2012843118 | PMCID: PMC7923540 | PMID: 33602810
- Evidence: Molecular visualizations were made with Visual Molecular Dynamics (VMD) ( 66 ).
- Full pipeline: simulation/modelling [VMD] -> visualisation [VMD] -> stage not stated [GROMACS]

### Cross-subunit interactions that stabilize open states mediate gating in NMDA receptors. (PNAS 2021)

- DOI: 10.1073/pnas.2007511118 | PMCID: PMC7812756 | PMID: 33384330
- Evidence: To measure interresidue vdW energies, we used the NAMDEnergy module in the VMD program ( 43 , 44 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [VMD]

### Biophysical characterization of calcium-binding and modulatory-domain dynamics in a pentameric ligand-gated ion channel. (PNAS 2022)

- DOI: 10.1073/pnas.2210669119 | PMCID: PMC9897478 | PMID: 36480474
- Evidence: Distances and center of mass positions were tracked through the trajectories using VMD ( 55 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS, VMD] -> stage not stated [PHENIX, RELION v3.1, UCSF Chimera]

### Integrative analysis reveals structural basis for transcription activation of Nurr1 and Nurr1-RXRα heterodimer. (PNAS 2022)

- DOI: 10.1073/pnas.2206737119 | PMCID: PMC9894219 | PMID: 36442107
- Evidence: Dynamical network analysis was performed with the Network View plugin ( 34 )in VMD.
- Full pipeline: normalisation [CCP4] -> visualisation [PyMOL] -> stage not stated [VMD]

### Intrinsically disordered ectodomain modulates ion permeation through a metal transporter. (PNAS 2022)

- DOI: 10.1073/pnas.2214602119 | PMCID: PMC9889885 | PMID: 36409899
- Evidence: Signaling network analysis was performed using the VMD network-view plugin and the GNCOMMUNITIES and SUBOPT tools ( 53 ).
- Full pipeline: simulation/modelling [MDAnalysis, MDTraj] -> stage not stated [GROMACS, PLUMED v2.6.3, VMD]

### Mechanism of voltage gating in the voltage-sensing phosphatase Ci-VSP. (PNAS 2022)

- DOI: 10.1073/pnas.2206649119 | PMCID: PMC9636939 | PMID: 36279472
- Evidence: The protein was embedded into a lipid bilayer solvated in 0.1 M NaCl solution using the program VMD ( 52 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [VMD]

### Mechanism of 4-aminopyridine inhibition of the lysosomal channel TMEM175. (PNAS 2022)

- DOI: 10.1073/pnas.2208882119 | PMCID: PMC9636928 | PMID: 36279431
- Evidence: These potentials were calculated with the PMEpot plug-in in VMD ( 41 ), using an Ewald factor of 0.25 Å −1 , and mapped onto a lattice of 200 × 200 × 224 grid-points.
- Full pipeline: alignment/mapping [VMD] -> simulation/modelling [NAMD v2.12] -> structure determination [PHENIX] -> stage not stated [RELION v3.0]

### Differential interactions of resting, activated, and desensitized states of the α7 nicotinic acetylcholine receptor with lipidic modulators. (PNAS 2022)

- DOI: 10.1073/pnas.2208081119 | PMCID: PMC9618078 | PMID: 36251999
- Evidence: Visualizations were created in VMD ( 68 ); most analyses were performed with GROMACS and MDAnalysis ( 69 ) and plotted with RainCloudPlot ( 70 ) and Matplotlib ( 71 ).
- Full pipeline: simulation/modelling [GROMACS] -> visualisation [MDAnalysis, Matplotlib, VMD]

### Structural basis for host recognition and superinfection exclusion by bacteriophage T5. (PNAS 2022)

- DOI: 10.1073/pnas.2211672119 | PMCID: PMC9586334 | PMID: 36215462
- Evidence: MD simulations were performed using the GROMACS software package ( 59 ) and the CHARMM36m force field ( 60 , 61 ) and were visualized and analyzed using the VMD software ( 62 ).
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [GROMACS, VMD]

### Computationally guided conversion of the specificity of E-selectin to mimic that of Siglec-8. (PNAS 2022)

- DOI: 10.1073/pnas.2117743119 | PMCID: PMC9564326 | PMID: 36191232
- Evidence: The analyses of high-occupancy water positions in the MD simulation trajectories were performed with the visual molecular dynamics (VMD) volmap plugin ( 74 ), which computed the average densities of water molecules over all matrices of cubic voxels (a cell size of 0.5 Å).
- Full pipeline: simulation/modelling [VMD]

### Multistate structures of the MLL1-WRAD complex bound to H2B-ubiquitinated nucleosome. (PNAS 2022)

- DOI: 10.1073/pnas.2205691119 | PMCID: PMC9499523 | PMID: 36095189
- Version used: **1.9.3**
- Evidence: The cross-correlation coefficient was computed using the MDFF package implemented in VMD 1.9.3 ( 78 ).
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, RELION v3.0, VMD v1.9.3, cryoDRGN]

### Computationally exploring the mechanism of bacteriophage T7 gp4 helicase translocating along ssDNA. (PNAS 2022)

- DOI: 10.1073/pnas.2202239119 | PMCID: PMC9371691 | PMID: 35914145
- Evidence: The structures were loaded in VMD, the corresponding topology files were generated, and then padding with water molecules and sodium and chlorine ions was added.
- Full pipeline: dimensionality reduction/clustering [seaborn] -> simulation/modelling [LAMMPS, NAMD, OpenMM] -> stage not stated [PyMOL, VMD]

### Cryo-EM structures of alphavirus conformational intermediates in low pH-triggered prefusion states. (PNAS 2022)

- DOI: 10.1073/pnas.2114119119 | PMCID: PMC9335222 | PMID: 35867819
- Evidence: Quality of the MDFF fittings was estimated using the CCC generated in VMD ( 45 ) and cross-correlation values (CC mask , CC box ) generated using phenix.real_space_refine (only apply Group B-factor refinement) ( 46 ).
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [VMD]

### Solvent selection criteria for temperature-resilient lithium-sulfur batteries. (PNAS 2022)

- DOI: 10.1073/pnas.2200392119 | PMCID: PMC9282424 | PMID: 35787034
- Evidence: Radial distribution functions were collected using the Visual Molecular Dynamics (VMD) software.
- Full pipeline: simulation/modelling [LAMMPS, VMD]

### Posttranslational modifications optimize the ability of SARS-CoV-2 spike for effective interaction with host cell receptors. (PNAS 2022)

- DOI: 10.1073/pnas.2119761119 | PMCID: PMC9282386 | PMID: 35737823
- Evidence: The stability of these models was evaluated by calculating rmsd, TM tilt/inclination in the membrane, and intermonomeric coordination number [coordNum in the collective variables (COLVARS) module ( 75 , 76 ) of Visual Molecular Dynamics (VMD) ( 77 )].
- Full pipeline: alignment/mapping [MAFFT] -> simulation/modelling [NAMD, VMD] -> visualisation [MAFFT]

### Molecular determinants of inhibition of the human proton channel hHv1 by the designer peptide C6 and a bivalent derivative. (PNAS 2022)

- DOI: 10.1073/pnas.2120750119 | PMCID: PMC9191634 | PMID: 35648818
- Evidence: The six cysteine residues of C6 were patched to form three disulfide bonds using the psfgen plugin of VMD ( 49 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [AlphaFold, VMD]

### Impact of natural selection on global patterns of genetic variation and association with clinical phenotypes at genes involved in SARS-CoV-2 infection. (PNAS 2022)

- DOI: 10.1073/pnas.2123000119 | PMCID: PMC9173769 | PMID: 35580180
- Evidence: All structural analysis and figures were prepared using VMD ( 74 ) ( SI Appendix ) Detecting Signatures of Natural Selection.
- Full pipeline: visualisation [VMD] -> stage not stated [VEP]

### Competing interactions give rise to two-state behavior and switch-like transitions in charge-rich intrinsically disordered proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2200559119 | PMCID: PMC9171777 | PMID: 35512095
- Evidence: The structures were extracted from simulations performed at 340 K and were drawn using VMD.
- Full pipeline: simulation/modelling [VMD]

### Endogenous pannexin1 channels form functional intercellular cell-cell channels with characteristic voltage-dependent properties. (PNAS 2022)

- DOI: 10.1073/pnas.2202104119 | PMCID: PMC9171361 | PMID: 35486697
- Evidence: To build the systems, VMD software was used ( 84 ).
- Full pipeline: stage not stated [VMD]

### A molecular switch controls the impact of cholesterol on a Kir channel. (PNAS 2022)

- DOI: 10.1073/pnas.2109431119 | PMCID: PMC9060494 | PMID: 35333652
- Version used: **1.9.3**
- Evidence: Fractional occupancy maps for POPS and cholesterol were calculated using the VolMap plugin in VMD 1.9.3 with a grid resolution of 1 Å ( 89 ).
- Full pipeline: simulation/modelling [GROMACS v2016.3] -> visualisation [PyMOL] -> stage not stated [ImageJ, Matplotlib, NumPy, VMD v1.9.3]

### A tethered ligand assay to probe SARS-CoV-2:ACE2 interactions. (PNAS 2022)

- DOI: 10.1073/pnas.2114397119 | PMCID: PMC9168514 | PMID: 35312342
- Evidence: We compared the sequence and structural differences between SARS-CoV-1 and SARS-CoV-2 by investigating both RBD:ACE2 interfaces in PDBsum ( 49 ) and VMD ( 50 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [Python, VMD]

### Contiguously hydrophobic sequences are functionally significant throughout the human exome. (PNAS 2022)

- DOI: 10.1073/pnas.2116267119 | PMCID: PMC8944643 | PMID: 35294280
- Evidence: Molecular images were made using Visual Molecular Dynamics (VMD) ( 73 ).
- Full pipeline: simulation/modelling [VMD] -> stage not stated [Matplotlib, NumPy, Python v3.6, SciPy]

### Rearrangement of a unique Kv1.3 selectivity filter conformation upon binding of a drug. (PNAS 2022)

- DOI: 10.1073/pnas.2113536119 | PMCID: PMC8812516 | PMID: 35091471
- Evidence: Simulation trajectories were analyzed using the VMD program.
- Full pipeline: alignment/mapping [MotionCor2] -> registration [MotionCor2] -> simulation/modelling [UCSF Chimera, VMD] -> structure determination [PHENIX] -> stage not stated [CTFFIND, NAMD, RELION]

### Bicarbonate-controlled reduction of oxygen by the Q<sub>A</sub> semiquinone in Photosystem II in membranes. (PNAS 2022)

- DOI: 10.1073/pnas.2116063119 | PMCID: PMC8833163 | PMID: 35115403
- Evidence: All classical MD simulations were performed using NAMD2 ( 65 ), and simulations were analyzed using VMD ( 66 ).
- Full pipeline: simulation/modelling [VMD]

### The role of dynamics in heterogeneous catalysis: Surface diffusivity and N<sub>2</sub> decomposition on Fe(111). (PNAS 2023)

- DOI: 10.1073/pnas.2313023120 | PMCID: PMC10723053 | PMID: 38060558
- Evidence: Made with VMD ( 61 ).
- Full pipeline: simulation/modelling [LAMMPS, PLUMED, Quantum ESPRESSO] -> stage not stated [VMD]

### Coenzyme Q10 trapping in mitochondrial complex I underlies Leber's hereditary optic neuropathy. (PNAS 2023)

- DOI: 10.1073/pnas.2304884120 | PMCID: PMC10523484 | PMID: 37733737
- Evidence: Visualization was done using UCSF Chimera ( 42 ) and Visual Molecular Dynamics, VMD ( 43 ).
- Full pipeline: simulation/modelling [NAMD, UCSF Chimera, VMD] -> visualisation [UCSF Chimera, VMD]

### Specific inhibition of an anticancer target, polo-like kinase 1, by allosterically dismantling its mechanism of substrate recognition. (PNAS 2023)

- DOI: 10.1073/pnas.2305037120 | PMCID: PMC10629583 | PMID: 37603740
- Version used: **1.9.4**
- Evidence: The simulation trajectory was visualized and stored in a video format using the Visual Molecular Dynamics software package (VMD 1.9.4) ( 74 ).
- Full pipeline: normalisation [CCP4] -> simulation/modelling [GROMACS v2022.3, RDKit, VMD v1.9.4] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL, VMD v1.9.4] -> stage not stated [AlphaFold]

### A biophysical framework for double-drugging kinases. (PNAS 2023)

- DOI: 10.1073/pnas.2304611120 | PMCID: PMC10450579 | PMID: 37590418
- Version used: **1.9.4a**
- Evidence: Trajectories were analyzed using VMD 1.9.4a53 ( 59 ).
- Full pipeline: simulation/modelling [OpenMM v7.6, VMD v1.9.4a] -> visualisation [ChimeraX, PyMOL]

### Structures and membrane interactions of native serotonin transporter in complexes with psychostimulants. (PNAS 2023)

- DOI: 10.1073/pnas.2304602120 | PMCID: PMC10629533 | PMID: 37436958
- Evidence: The initial coordinates of CHS, DHA – , and DDM were transferred from the experimental models, while CHOL was constructed into the CHS model, and DHA 0 was constructed by protonating the DHA – model using the PSFGEN plugin in VMD ( 87 ).
- Full pipeline: alignment/mapping [RELION] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [CTFFIND, MotionCor2, VMD]

### Confined water-encapsulated activated carbon for capturing short-chain perfluoroalkyl and polyfluoroalkyl substances from drinking water. (PNAS 2023)

- DOI: 10.1073/pnas.2219179120 | PMCID: PMC10318985 | PMID: 37364117
- Evidence: All the models were built using the Moltemplate software package, and visual analysis was performed using VMD software.
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [VMD]

### Scribble scrambles parathyroid hormone receptor interactions to regulate phosphate and vitamin D homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2220851120 | PMCID: PMC10266016 | PMID: 37252981
- Version used: **1.9.3**
- Evidence: The movie was generated using Visual Molecular Dynamics (VMD 1.9.3).
- Full pipeline: simulation/modelling [VMD v1.9.3] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Deciphering molecular mechanisms stabilizing the reovirus-binding complex. (PNAS 2023)

- DOI: 10.1073/pnas.2220741120 | PMCID: PMC10214207 | PMID: 37186838
- Evidence: Mean correlation between σ1–JAM-A interface residues was calculated using dynamical network analysis ( 29 ) and VMD ( 55 ).
- Full pipeline: simulation/modelling [NAMD, TrackMate] -> stage not stated [ImageJ v1.52e, VMD]

### Imaging of pH distribution inside individual microdroplet by stimulated Raman microscopy. (PNAS 2023)

- DOI: 10.1073/pnas.2219588120 | PMCID: PMC10193990 | PMID: 37155894
- Evidence: And MD configurations were visualized by the VMD package ( 54 ).
- Full pipeline: visualisation [VMD] -> stage not stated [GROMACS v2019.6]

### Elucidating the origins of phycocyanobilin biosynthesis and phycobiliproteins. (PNAS 2023)

- DOI: 10.1073/pnas.2300770120 | PMCID: PMC10151467 | PMID: 37071675
- Evidence: Structural figures were prepared using VMD and Tachyon ( 103 , 104 ).
- Full pipeline: alignment/mapping [MAFFT v7.450] -> visualisation [VMD] -> stage not stated [AlphaFold]

### A mutagenesis study of autoantigen optimization for potential T1D vaccine design. (PNAS 2023)

- DOI: 10.1073/pnas.2214430120 | PMCID: PMC10120010 | PMID: 37040399
- Evidence: Briefly, the intrinsic mimotope in the PDB structure was mutated to the X-idiotype antigen using VMD ( 54 ).
- Full pipeline: stage not stated [VMD]

### Colloidal superionic conductors. (PNAS 2023)

- DOI: 10.1073/pnas.2300257120 | PMCID: PMC10104562 | PMID: 37018200
- Evidence: Images of simulation results are created using VMD ( 67 ).
- Full pipeline: simulation/modelling [LAMMPS, VMD]

### Structures of brain-derived 42-residue amyloid-β fibril polymorphs with unusual molecular conformations and intermolecular interactions. (PNAS 2023)

- DOI: 10.1073/pnas.2218831120 | PMCID: PMC10089215 | PMID: 36893281
- Evidence: MD simulations were performed with NAMD software and analyzed with VMD software ( 38 , 39 ).
- Full pipeline: simulation/modelling [Coot, NAMD, VMD] -> structure determination [Coot, RELION]

### Elucidation of a dynamic interplay between a beta-2 adrenergic receptor, its agonist, and stimulatory G protein. (PNAS 2023)

- DOI: 10.1073/pnas.2215916120 | PMCID: PMC10013855 | PMID: 36853938
- Evidence: Simulation analyses were performed using VMD ( 50 ) and lab-generated codes.
- Full pipeline: alignment/mapping [UCSF Chimera] -> dimensionality reduction/clustering [SciPy] -> simulation/modelling [NAMD, VMD]

### Molecular mechanism of GTP binding- and dimerization-induced enhancement of Sar1-mediated membrane remodeling. (PNAS 2023)

- DOI: 10.1073/pnas.2212513120 | PMCID: PMC9974494 | PMID: 36780528
- Evidence: We build the h-GTP model of Sar1 using the GDP state sequence and the y-GTP structure as a template with the SWISS-MODEL ( 46 ) webserver and the Molefracture plugin of VMD ( 47 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, VMD]

### Driving and characterizing nucleation of urea and glycine polymorphs in water. (PNAS 2023)

- DOI: 10.1073/pnas.2216099120 | PMCID: PMC9963467 | PMID: 36757888
- Evidence: Snapshots are rendered using Visual Molecular Dynamics (VMD) ( 79 ).
- Full pipeline: simulation/modelling [PLUMED, VMD] -> visualisation [VMD] -> stage not stated [GROMACS]

### Synthesis and characterization of Craig-type antiaromatic species with [4<i>n</i> + 2] π electrons. (PNAS 2023)

- DOI: 10.1073/pnas.2215900120 | PMCID: PMC9963141 | PMID: 36735757
- Evidence: The ICSSs analysis calculations were carried out with Multiwfn and visualized by the VMD program.
- Full pipeline: visualisation [VMD]

### Structure and supramolecular organization of the canine distemper virus attachment glycoprotein. (PNAS 2023)

- DOI: 10.1073/pnas.2208866120 | PMCID: PMC9963377 | PMID: 36716368
- Evidence: Images were rendered with VMD (visual molecular dynamics) ( 83 ).
- Full pipeline: registration [MotionCor2 v1.4.0] -> simulation/modelling [VMD] -> structure determination [PHENIX v1.19] -> visualisation [VMD] -> stage not stated [ChimeraX v1.3, Coot, PyMOL v2.5.2, RELION v3.1.1, UCSF Chimera v1.12]

### Macrophages modulate stiffness-related foreign body responses through plasma membrane deformation. (PNAS 2023)

- DOI: 10.1073/pnas.2213837120 | PMCID: PMC9934070 | PMID: 36626552
- Evidence: VMD software was used for molecular dynamics simulations trajectory visualization and analysis.
- Full pipeline: simulation/modelling [GROMACS v2019.2, VMD] -> visualisation [VMD] -> stage not stated [ImageJ]

### Hepatic SEL1L-HRD1 ER-associated degradation regulates systemic iron homeostasis via ceruloplasmin. (PNAS 2023)

- DOI: 10.1073/pnas.2212644120 | PMCID: PMC9926173 | PMID: 36595688
- Evidence: The analysis of hydrogen bonding and atom–atom distance was computed by the VMD ( 84 ) and CPPTRJ program ( 85 ).
- Full pipeline: stage not stated [VMD]

### Differential dynamics and direct interaction of bound ligands with lipids in multidrug transporter ABCG2. (PNAS 2023)

- DOI: 10.1073/pnas.2213437120 | PMCID: PMC9910490 | PMID: 36580587
- Evidence: Unresolved side chains and hydrogen atoms were added to the structures employing the https://www.ks.uiuc.edu/Research/vmd/plugins/psfgen/ plugin of VMD ( 51 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [CTFFIND, Coot v0.9, MotionCor2, PHENIX, VMD]

### SARS-CoV-2 accessory proteins ORF7a and ORF3a use distinct mechanisms to down-regulate MHC-I surface expression. (PNAS 2023)

- DOI: 10.1073/pnas.2208525120 | PMCID: PMC9910621 | PMID: 36574644
- Evidence: The simulation systems consisting of the biomolecular complexes of HC+β2m and HC+ORF7a described above were generated using the QwikMD Toolkit ( 72 ) available as a plugin in Visual Molecular Dynamics (VMD) software V1.9.3 ( 73 ).
- Full pipeline: simulation/modelling [NAMD, VMD] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Road-blocker HSP disease mutation disrupts pre-organization for ATP hydrolysis in kinesin through a second sphere control. (PNAS 2023)

- DOI: 10.1073/pnas.2215170120 | PMCID: PMC9910451 | PMID: 36574689
- Evidence: Visual MD (VMD) 1.9.2 is used in order to study trajectories and explore atomic-level insights ( 35 ).
- Full pipeline: dimensionality reduction/clustering [PLUMED v2.4.3] -> simulation/modelling [GROMACS v5.1, PLUMED v2.4.3, VMD]

### Mechanism of proton release during water oxidation in Photosystem II. (PNAS 2024)

- DOI: 10.1073/pnas.2413396121 | PMCID: PMC11670119 | PMID: 39700151
- Evidence: All simulations were performed using NAMD2.14 and NAMD3.0alpha9 ( 64 , 65 ), and analyzed using VMD ( 66 ).
- Full pipeline: simulation/modelling [VMD]

### Temperature-dependent fold-switching mechanism of the circadian clock protein KaiB. (PNAS 2024)

- DOI: 10.1073/pnas.2412327121 | PMCID: PMC11665890 | PMID: 39671178
- Evidence: PDB IDs 1VGL and 5JYT were used with VMD ( 13 ) to generate the ribbon diagrams for gsKaiB and fsKaiB, respectively.
- Full pipeline: stage not stated [VMD]

### Distinct modulation of calcium-activated chloride channel TMEM16A by drug-binding sites. (PNAS 2024)

- DOI: 10.1073/pnas.2314011121 | PMCID: PMC11665900 | PMID: 39656212
- Evidence: Salt bridges were calculated in VMD ( 43 ) and the cutoff distance was 5 Å.
- Full pipeline: stage not stated [AutoDock Vina, VMD]

### Architecture of the Sap S-layer of &lt;i&gt;Bacillus anthracis&lt;/i&gt; revealed by integrative structural biology. (PNAS 2024)

- DOI: 10.1073/pnas.2415351121 | PMCID: PMC11665858 | PMID: 39652757
- Evidence: Then, each domain of the complete Sap monomer was aligned via alpha-C atoms to the docked structures using visual molecular dynamics (VMD) ( 60 ).
- Full pipeline: alignment/mapping [VMD] -> registration [MotionCor2] -> simulation/modelling [VMD] -> structure determination [RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, GROMACS, IMOD]

### High-temperature high-k polyolefin by rational molecular design. (PNAS 2024)

- DOI: 10.1073/pnas.2415388121 | PMCID: PMC11648892 | PMID: 39642197
- Evidence: Electrostatic potential (ESP) surface plots were generated by using Multiwfn ( 31 ) and VMD ( 32 ).
- Full pipeline: stage not stated [VMD]

### Structural basis for the synergetic neutralization of hepatitis E virus by antibody-antibody interaction. (PNAS 2024)

- DOI: 10.1073/pnas.2408585121 | PMCID: PMC11626150 | PMID: 39585981
- Version used: **1.9.3**
- Evidence: The Autopsf plugin in the Visual Molecular Dynamics software (VMD, version 1.9.3) ( 36 ) was used to generate a dynamics-ready protein atom coordinate file (PDB) and a protein structure file.
- Full pipeline: dimensionality reduction/clustering [NAMD] -> simulation/modelling [NAMD, VMD v1.9.3] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL]

### Agonist activation to open the Gα subunit of the GPCR-G protein precoupled complex defines functional agonist activation of TAS2R5. (PNAS 2024)

- DOI: 10.1073/pnas.2409987121 | PMCID: PMC11621838 | PMID: 39565310
- Evidence: VMD ( 69 ) and Chimera ( 70 ) programs were used for analysis and visualization.
- Full pipeline: simulation/modelling [GROMACS, PLUMED] -> visualisation [VMD]

### Inhibition mechanism of potential antituberculosis compound lansoprazole sulfide. (PNAS 2024)

- DOI: 10.1073/pnas.2412780121 | PMCID: PMC11588064 | PMID: 39531492
- Evidence: The trajectories were analyzed using VMD ( 48 ) and MD analysis ( 49 , 50 ).
- Full pipeline: simulation/modelling [NAMD v2.12, VMD] -> structure determination [Coot, PHENIX]

### The role of astrocytes in depression, its prevention, and treatment by targeting astroglial gliotransmitter release. (PNAS 2024)

- DOI: 10.1073/pnas.2307953121 | PMCID: PMC11572930 | PMID: 39495924
- Evidence: ( F ) Prediction of GAP19-Cx43 C-terminal (CT) putative binding site using VMD software; the CT domain is shown in gray and GAP19 peptide is shown in green.
- Full pipeline: stage not stated [VMD]

### Identifying and controlling the order parameter for ultrafast photoinduced phase transitions in thermosalient materials. (PNAS 2024)

- DOI: 10.1073/pnas.2408366121 | PMCID: PMC11573639 | PMID: 39499639
- Evidence: Datafiles of both the α and β structures were prepared with the use of VMD ( 44 ).
- Full pipeline: dimensionality reduction/clustering [PLUMED] -> simulation/modelling [LAMMPS, PLUMED] -> stage not stated [VMD]

### Atomic view of photosynthetic metabolite permeability pathways and confinement in synthetic carboxysome shells. (PNAS 2024)

- DOI: 10.1073/pnas.2402277121 | PMCID: PMC11551347 | PMID: 39485798
- Evidence: The synthetic T = 4 carboxysome cryo-EM structure ( 6 ) was solvated in a water cube with side length 29 nm and prepared for simulation ( Movie S1 ) with the CHARMM36m force field for proteins ( 69 ) using Visual Molecular Dynamics (VMD) ( 70 ).
- Full pipeline: simulation/modelling [GROMACS, NAMD v2.14, VMD] -> stage not stated [Matplotlib, NumPy, SciPy]

### Improved deep learning prediction of antigen-antibody interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2410529121 | PMCID: PMC11474075 | PMID: 39361651
- Evidence: VMD ( 24 ) was used to visualize the protein structural models.
- Full pipeline: machine learning [AlphaFold] -> visualisation [VMD]

### Molecular-level design of alternative media for energy-saving pilot-scale fibrillation of nanocellulose. (PNAS 2024)

- DOI: 10.1073/pnas.2405107121 | PMCID: PMC11406261 | PMID: 39236244
- Evidence: Reparameterization was conducted using default settings in Force Field Toolkit (ffTK) ( 60 , 61 ) implemented in VMD ( 62 ), where system input files were prepared for Gaussian09 ( 63 ) quantum mechanical (QM) calculations including energy minimization and bond or dihedral optimization and their output files were processed.
- Full pipeline: simulation/modelling [GROMACS, VMD]

### Relative genotoxicity of polycyclic aromatic hydrocarbons inferred from free energy perturbation approaches. (PNAS 2024)

- DOI: 10.1073/pnas.2322155121 | PMCID: PMC11406254 | PMID: 39226345
- Evidence: Briefly, force field parameters for PAH-DNA adducts were assigned and optimized utilizing quantum mechanical target data, the CHARMM General Force Field/ParamChem.com ( 45 – 47 ), and the VMD-Force Field Toolkit ( 48 ).
- Full pipeline: simulation/modelling [NAMD, VMD] -> stage not stated [Python]

### Multifunctional biomolecular corona-inspired nanoremediation of antibiotic residues. (PNAS 2024)

- DOI: 10.1073/pnas.2409955121 | PMCID: PMC11388419 | PMID: 39190351
- Evidence: Electrostatic potential distribution on the molecular surface was calculated, and the independent gradient model based on Hirshfeld partition (IGMH) method was used to visualize weak interactions by Visual Molecular Dynamics (VMD) software 1.9.3 ( 54 ).
- Full pipeline: simulation/modelling [VMD] -> visualisation [VMD]

### Sustainable H<sub>2</sub>O<sub>2</sub> production via solution plasma catalysis. (PNAS 2024)

- DOI: 10.1073/pnas.2410504121 | PMCID: PMC11348095 | PMID: 39150782
- Evidence: The calculation was completed in the Gaussian 16 software package and the Orbital Coupling Value ORCA 5.2 software package and combined with the Multiwfn 3.8 software package for postprocessing and VMD 193 software package visualization.
- Full pipeline: visualisation [VMD] -> stage not stated [scikit-learn]

### Plasticity of the selectivity filter is essential for permeation in lysosomal TPC2 channels. (PNAS 2024)

- DOI: 10.1073/pnas.2320153121 | PMCID: PMC11317647 | PMID: 39074274
- Evidence: Visual Molecular Dynamics (VMD) ( 70 ) was used for visualization and image preparation.
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.7, Python, VMD] -> visualisation [VMD] -> stage not stated [MDAnalysis]

### Secondary structure determines electron transport in peptides. (PNAS 2024)

- DOI: 10.1073/pnas.2403324121 | PMCID: PMC11317557 | PMID: 39052850
- Evidence: Hydrogens were added to the peptides with the VMD plugin PSFGEN ( 77 ) using the NTER and CTER terminal patches to create positively and negatively charged N and C termini, respectively.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [OpenMM v7.7.0] -> stage not stated [VMD]

### A broad survey of choanoflagellates revises the evolutionary history of the Shaker family of voltage-gated K&lt;sup&gt;+&lt;/sup&gt; channels in animals. (PNAS 2024)

- DOI: 10.1073/pnas.2407461121 | PMCID: PMC11287247 | PMID: 39018191
- Version used: **1.9.4a**
- Evidence: Tetramers were assembled in VMD v.1.9.4a55 ( 69 ) using the rotational matrix from the top hit in AlphaFold, an Aplysia Kv3 channel (PDB: 3KVT) ( 35 ) and Zn 2+ was placed at each binding site to mimic the position in this channel.
- Full pipeline: simulation/modelling [NAMD v2.0] -> stage not stated [AlphaFold v2.3.2, BLAST, VMD v1.9.4a]

### Structure-based investigation of a DNA aptamer targeting PTK7 reveals an intricate 3D fold guiding functional optimization. (PNAS 2024)

- DOI: 10.1073/pnas.2404060121 | PMCID: PMC11260122 | PMID: 38985770
- Evidence: The distribution of Mg 2+ was analyzed and plotted using the Visual Molecular Dynamics (VMD) program ( SI Appendix , Fig.
- Full pipeline: simulation/modelling [GROMACS v2021.7, VMD] -> visualisation [PyMOL, VMD]

### Mechanism of phosphate release from actin filaments. (PNAS 2024)

- DOI: 10.1073/pnas.2408156121 | PMCID: PMC11260136 | PMID: 38980907
- Evidence: The system was solvated using the autosolvate plugin in VMD ( 56 ) to add a TIP3P water box with a minimum separation of 11 Å between the protein and the periodic boundary.
- Full pipeline: simulation/modelling [GROMACS v2020.4, PLUMED v2.4, PyMOL, Python] -> stage not stated [VMD]

### Ca<sup>2+</sup> permeation through C-terminal cleaved, but not full-length human Pannexin1 hemichannels, mediates cell death. (PNAS 2024)

- DOI: 10.1073/pnas.2405468121 | PMCID: PMC11194574 | PMID: 38861601
- Evidence: Visual Molecular Dynamics (VMD) software was used to establish the systems and run analysis ( 61 ).
- Full pipeline: simulation/modelling [NAMD, VMD] -> stage not stated [ImageJ v1.64r]

### Asymmetric allostery in estrogen receptor-α homodimers drives responses to the ensemble of estrogens in the hormonal milieu. (PNAS 2024)

- DOI: 10.1073/pnas.2321344121 | PMCID: PMC11181081 | PMID: 38830107
- Evidence: Suboptimal paths between residue sites were visualized as edges in VMD.
- Full pipeline: visualisation [VMD] -> stage not stated [PHENIX, PyMOL, UCSF Chimera]

### Unplugging lateral fenestrations of NALCN reveals a hidden drug binding site within the pore region. (PNAS 2024)

- DOI: 10.1073/pnas.2401591121 | PMCID: PMC11145269 | PMID: 38787877
- Evidence: We imported the cryo-EM structure of human NALCN-FAM155A-UNC79-UNC80 channelosome with calmodulin (CaM) bound (PDB ID: 7SX3) in VMD (Visual Molecular Dynamics, version 1.9.4a57), and removed the three nonconducting auxiliary subunits, CaM and all the bound lipids.
- Full pipeline: simulation/modelling [GROMACS v2021.4, VMD] -> stage not stated [PyMOL]

### Hydrogen bonding heterogeneity correlates with protein folding transition state passage time as revealed by data sonification. (PNAS 2024)

- DOI: 10.1073/pnas.2319094121 | PMCID: PMC11145292 | PMID: 38768341
- Evidence: We used VMD ( 40 ) to obtain time series for three structural parameters: EHA , SASA , and R g .
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [VMD]

### Copper(II) coordination to the intrinsically disordered region of SARS-CoV-2 Nsp1. (PNAS 2024)

- DOI: 10.1073/pnas.2402653121 | PMCID: PMC11098128 | PMID: 38722808
- Evidence: VMD ( 37 ) and Avogadro ( 38 ) programs were used for visualization, and EPR simulations were performed using the EasySpin software package.
- Full pipeline: simulation/modelling [VMD] -> visualisation [VMD]

### Identification of the potassium-binding site in serotonin transporter. (PNAS 2024)

- DOI: 10.1073/pnas.2319384121 | PMCID: PMC11067047 | PMID: 38652746
- Version used: **1.9.3**
- Evidence: Distance analyses were performed with the COLVARS module v2022-05-24 ( 55 ) in VMD v1.9.3 ( 58 ).
- Full pipeline: simulation/modelling [GROMACS v2018.8, NAMD v2.13] -> stage not stated [Coot v0.8.9.3, VMD v1.9.3]

### Mechanism of proton-powered c-ring rotation in a mitochondrial ATP synthase. (PNAS 2024)

- DOI: 10.1073/pnas.2314199121 | PMCID: PMC10945847 | PMID: 38451940
- Evidence: Molecular structures were visualized and rendered with VMD ( 79 ) and Pymol ( 80 ).
- Full pipeline: simulation/modelling [GROMACS v2020.4, MDAnalysis, SciPy, scikit-learn] -> visualisation [Matplotlib, VMD] -> stage not stated [NetworkX]

### Quantifying a light-induced energetic change in bacteriorhodopsin by force spectroscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2313818121 | PMCID: PMC10873598 | PMID: 38324569
- Evidence: Structural renderings were made using VMD ( 61 ).
- Full pipeline: stage not stated [VMD]

### Regulation of anion-Na<sup>+</sup> coordination chemistry in electrolyte solvates for low-temperature sodium-ion batteries. (PNAS 2024)

- DOI: 10.1073/pnas.2316914121 | PMCID: PMC10835037 | PMID: 38252828
- Evidence: The snapshot of MD simulation is produced by VMD software ( 52 ).
- Full pipeline: simulation/modelling [GROMACS, VMD]

### HIV-1 capsid shape, orientation, and entropic elasticity regulate translocation into the nuclear pore complex. (PNAS 2024)

- DOI: 10.1073/pnas.2313737121 | PMCID: PMC10823262 | PMID: 38241438
- Evidence: Visualization of the simulation trajectories was performed in VMD ( 74 ).
- Full pipeline: simulation/modelling [LAMMPS, VMD] -> visualisation [VMD]

### Lipid shape and packing are key for optimal design of pH-sensitive mRNA lipid nanoparticles. (PNAS 2024)

- DOI: 10.1073/pnas.2311700120 | PMCID: PMC10786277 | PMID: 38175863
- Evidence: The addition of excess water and the ionization of the system was carried out using VMD ( 39 ) scripts.
- Full pipeline: simulation/modelling [Jupyter, NAMD v2.12] -> stage not stated [VMD]

### Sensing the shape of a surface by tightly surface-bound filaments. (PNAS 2025)

- DOI: 10.1073/pnas.2526131122 | PMCID: PMC12772210 | PMID: 41428884
- Evidence: Setup, analysis, and rendering of the simulation systems were performed with the software VMD ( 71 ).
- Full pipeline: simulation/modelling [VMD] -> stage not stated [AlphaFold]

### Occludin acts as a dynein adaptor regulating permeability and collateral angiogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2516076122 | PMCID: PMC12745719 | PMID: 41401008
- Evidence: Bergin VMD, MS, DACLAM, DACVP and Yao Lee DVM, MS, PhD, DACVP of the ULAM Pathology Core, RRID:SCR 018823.
- Full pipeline: stage not stated [VMD]

### A balance between glycitein and glyceollins governed by isoflavone 6-hydroxylase confers soybean resistance to &lt;i&gt;Phytophthora sojae&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2525627122 | PMCID: PMC12718328 | PMID: 41380000
- Evidence: The relative biomass of P. sojae was quantified using RT–qPCR with specific primers targeting the P. sojae Actin gene (VMD GeneID: 108986) and the soybean Actin11 gene ( 53 ).
- Full pipeline: quantification [VMD]

### Mechanisms of transport and analgesic compounds recognition by glycine transporter 2. (PNAS 2025)

- DOI: 10.1073/pnas.2506722122 | PMCID: PMC12685064 | PMID: 41284875
- Evidence: The calculation of R.M.S.D. for proteins and ligands was performed using VMD ( 102 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [PHENIX, VMD]

### Structural basis of modified ligand selectivity from N-terminal PAC1R alternative splicing. (PNAS 2025)

- DOI: 10.1073/pnas.2521157122 | PMCID: PMC12663942 | PMID: 41264251
- Evidence: Data is displayed using VMD.
- Full pipeline: registration [CTFFIND, RELION v3.1.2] -> structure determination [CTFFIND, RELION v3.1.2] -> stage not stated [ChimeraX, VMD]

### Synthetic bottlebrush block copolymer prevents disease onset in Duchenne muscular dystrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2513599122 | PMCID: PMC12557544 | PMID: 41082666
- Evidence: Post-MD analyses were performed using Maestro, VMD, and GraphPad Prism.
- Full pipeline: stage not stated [ImageJ, VMD]

### Temperature adaptation in structure and function in lactate dehydrogenase-A reflects convergent evolution in a few key protein regions. (PNAS 2025)

- DOI: 10.1073/pnas.2517759122 | PMCID: PMC12557798 | PMID: 41071662
- Evidence: Hydrogen bonds, which were identified as polar contacts in proteins, were analyzed by both number and distance by the VMD program ( 36 ).
- Full pipeline: alignment/mapping [MAFFT v7.487, R] -> simulation/modelling [GROMACS v2021.3, XGBoost] -> machine learning [TensorFlow] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5, VMD]

### A fixed mutation in the respiratory complex I impairs mitochondrial bioenergetics in the endangered Apennine brown bear. (PNAS 2025)

- DOI: 10.1073/pnas.2504409122 | PMCID: PMC12519208 | PMID: 41026818
- Evidence: Figures and videos were generated using ChimeraX 1.7 molecular visualization program ( 79 ), and analyses were performed with VMD ( 80 ).
- Full pipeline: simulation/modelling [GROMACS v2022.3] -> visualisation [ChimeraX v1.7, VMD] -> stage not stated [AlphaFold, ImageJ]

### A unified model of transient poration induced by antimicrobial peptides. (PNAS 2025)

- DOI: 10.1073/pnas.2510294122 | PMCID: PMC12415194 | PMID: 40880531
- Evidence: Leaflet surface maps and bilayer thickness maps were calculated using the MEMBPLUGIN ( 79 ) tool in VMD ( 80 ), and defects were identified using the protocol introduced in Paper 1 ( 39 ).
- Full pipeline: simulation/modelling [OpenMM v7.4.1] -> stage not stated [GROMACS v2021.2, VMD]

### Scalable high-voltage Zn||MnO&lt;sub&gt;2&lt;/sub&gt; batteries achieved by mild amphiphilic hydrogel electrolytes. (PNAS 2025)

- DOI: 10.1073/pnas.2501935122 | PMCID: PMC12377733 | PMID: 40815628
- Evidence: The visualization is realized by the VMD software ( 37 ).
- Full pipeline: visualisation [VMD]

### Structural basis and affinity improvement for an ATP-binding DNA aptamer. (PNAS 2025)

- DOI: 10.1073/pnas.2506491122 | PMCID: PMC12377721 | PMID: 40811466
- Evidence: 4 A was prepared using VMD ( 52 ).
- Full pipeline: simulation/modelling [GROMACS v2021.7] -> visualisation [PyMOL] -> stage not stated [AlphaFold, VMD]

### Atomistic mechanisms of calcium permeation modulated by Q/R editing and selectivity filter mutations in GluA2 AMPA receptors. (PNAS 2025)

- DOI: 10.1073/pnas.2425172122 | PMCID: PMC12377769 | PMID: 40811461
- Evidence: VMD ( 68 ) and PyMol were used for visualization of the MD trajectories.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis, VMD] -> visualisation [MDAnalysis, Matplotlib, VMD] -> stage not stated [PyMOL]

### The distortion-push mechanism for the γ subunit rotation in F&lt;sub&gt;1&lt;/sub&gt;-ATPase. (PNAS 2025)

- DOI: 10.1073/pnas.2502642122 | PMCID: PMC12377772 | PMID: 40794830
- Evidence: The internal cavities of the protein were hydrated using Dowser++ ( 58 ), and the structures were modeled using the VMD plugin ( 59 ).
- Full pipeline: stage not stated [VMD]

### Nonsubstrate PI(4,5)P<sub>2</sub> interacts with the interdomain linker to control electrochemical coupling in voltage-sensing phosphatase (VSP). (PNAS 2025)

- DOI: 10.1073/pnas.2500651122 | PMCID: PMC12337349 | PMID: 40729387
- Evidence: Simulations were visualized using VMD ( 63 ).
- Full pipeline: simulation/modelling [GROMACS, VMD] -> visualisation [PyMOL, VMD] -> stage not stated [ColabFold]

### Structural basis of auxin binding and transport by <i>Arabidopsis thaliana</i> AUX1. (PNAS 2025)

- DOI: 10.1073/pnas.2513424122 | PMCID: PMC12337342 | PMID: 40720658
- Evidence: Trajectory analyses were conducted using Visual Molecular Dynamics (VMD) ( 59 ) for structural visualization and quantitative evaluation of rmsd (RMSD).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [OpenMM, VMD] -> structure determination [PHENIX] -> machine learning [OpenMM] -> visualisation [VMD] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, Coot]

### Structure reveals a regulation mechanism of plant outward-rectifying K&lt;sup&gt;+&lt;/sup&gt; channel GORK by structural rearrangements in the CNBD-Ankyrin bridge. (PNAS 2025)

- DOI: 10.1073/pnas.2500070122 | PMCID: PMC12318183 | PMID: 40699930
- Evidence: All the figures in this article were prepared using PyMOL (Schrödinger, LLC.), UCSF Chimera and ChimeraX, VMD (University of Illinois at Urbana-Champaign), and BIOVIA Discovery Studio 2017 R2 (Dassault Systèmes).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, PyMOL, UCSF Chimera, VMD]

### Regulation of the ordinal DNA translocation cycle in bacteriophage Φ29 through trans-subunit interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2504780122 | PMCID: PMC12260519 | PMID: 40608675
- Evidence: All structures and trajectories were visualized through ChimeraX ( 25 ) and VMD ( 26 ).
- Full pipeline: simulation/modelling [ChimeraX, VMD] -> visualisation [ChimeraX, VMD] -> stage not stated [AlphaFold, PLUMED]

### In silico evolution of globular protein folds from random sequences. (PNAS 2025)

- DOI: 10.1073/pnas.2509015122 | PMCID: PMC12260532 | PMID: 40587803
- Evidence: For protein structure visualization, ChimeraX and VMD (Visual Molecular Dynamics) were used ( 71 , 72 ).
- Full pipeline: simulation/modelling [ChimeraX, VMD] -> visualisation [ChimeraX, VMD] -> stage not stated [AlphaFold, ColabFold v1.5.5, RoseTTAFold]

### Solution structure and synaptic analyses reveal determinants of bispecific T cell engager potency. (PNAS 2025)

- DOI: 10.1073/pnas.2425781122 | PMCID: PMC12146755 | PMID: 40445758
- Evidence: Paratope (distances between the tips of the heavy chain CDR3 loops) and anchor-to-anchor spacings (distances between the C-terminal domains of CD3εγ and Her2) and measures of flexibility were calculated using custom Text Command Language (TCL) codes in VMD ( 76 ), taking into consideration the weighted effective contribution of each PDB file.
- Full pipeline: stage not stated [AlphaFold, UCSF Chimera, VMD]

### Deciphering Ca&lt;sup&gt;&lt;b&gt;2+&lt;/b&gt;&lt;/sup&gt; permeation and valence selectivity in Ca&lt;sub&gt;V&lt;/sub&gt;1: Molecular dynamics simulations reveal the three-ion knock-on mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2424694122 | PMCID: PMC12146731 | PMID: 40440072
- Evidence: The density map of ions was calculated by the “VolMap Tool” in VMD ( 80 ).
- Full pipeline: quantification [PLUMED] -> simulation/modelling [GROMACS v2021.2, MDAnalysis, PLUMED] -> structure determination [VMD] -> visualisation [PyMOL] -> stage not stated [NetworkX]

### Microtubule dynamics are defined by conformations and stability of clustered protofilaments. (PNAS 2025)

- DOI: 10.1073/pnas.2424263122 | PMCID: PMC12146719 | PMID: 40440074
- Evidence: All structure and cryoET density manipulations to produce images in the figures were performed using Chimera v1.17 ( 100 ) or Visual Molecular Dynamics (VMD) v1.9.3 ( 101 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> simulation/modelling [GROMACS, VMD] -> structure determination [IMOD, MotionCor2] -> visualisation [VMD] -> stage not stated [Matplotlib v3.8.2, NumPy v1.26, Python v3.9, SciPy v1.11, seaborn v0.13]

### A direct computational assessment of vinculin-actin unbinding kinetics reveals catch-bonding behavior. (PNAS 2025)

- DOI: 10.1073/pnas.2425982122 | PMCID: PMC12130851 | PMID: 40397673
- Evidence: Residues in Vt and actin A3 and A5 separated by less than 3 Å are shown in VMD’s ( 63 ) “licorice” representation.
- Full pipeline: stage not stated [PLUMED, SciPy, VMD]

### Molecular insights into human phosphatidylserine synthase 2 and its regulation of SREBP pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2501177122 | PMCID: PMC12107096 | PMID: 40372437
- Evidence: Analyses of the MD trajectories were performed with VMD (Version 1.94) ( 38 ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [NAMD, VMD] -> structure determination [AlphaFold, PHENIX] -> visualisation [ChimeraX, PyMOL]

### Microscopic basis of reaction center modulation in PsbA variants of photosystem II. (PNAS 2025)

- DOI: 10.1073/pnas.2417963122 | PMCID: PMC12107152 | PMID: 40354529
- Evidence: ( 90 ) Binding free energies were calculated using MM-PBSA ( 54 ), and trajectories were analyzed using VMD and CPPTRAJ.
- Full pipeline: simulation/modelling [VMD] -> stage not stated [Clustal Omega]

### Caveolin assemblies displace one bilayer leaflet to organize and bend membranes. (PNAS 2025)

- DOI: 10.1073/pnas.2417024122 | PMCID: PMC12107156 | PMID: 40359049
- Evidence: The systems with 2, 6, and 9 CAV1-8S complexes were assembled manually from copies of single-CAV1-8S bilayers using the Visual Molecular Dynamics (VMD) software ( SI Appendix , Table S1 ).
- Full pipeline: simulation/modelling [VMD] -> stage not stated [GROMACS]

### Allosteric mechanism in the distinctive coupling of G&lt;sub&gt;q&lt;/sub&gt; and G&lt;sub&gt;s&lt;/sub&gt; to the parathyroid hormone type 1 receptor. (PNAS 2025)

- DOI: 10.1073/pnas.2426178122 | PMCID: PMC12002267 | PMID: 40138341
- Version used: **1.9.4**
- Evidence: Contact durations between residues were analyzed using VMD 1.9.4 ( 20 ).
- Full pipeline: simulation/modelling [NAMD] -> visualisation [PyMOL] -> stage not stated [VMD v1.9.4]

### Energy landscape analysis of the development of the chromosome structure across the cell cycle. (PNAS 2025)

- DOI: 10.1073/pnas.2425225122 | PMCID: PMC11962442 | PMID: 40112110
- Evidence: The 3D structures of chromosomes were visualized using VMD software ( 71 ).
- Full pipeline: simulation/modelling [OpenMM] -> visualisation [VMD] -> stage not stated [Python]

### Thermoelastic twisting-assisted crystal jumping based on a self-healing molecular crystal. (PNAS 2025)

- DOI: 10.1073/pnas.2417901122 | PMCID: PMC11848281 | PMID: 39928867
- Evidence: The crystal structures were visualized using VMD ( 77 ).
- Full pipeline: visualisation [VMD]

### Rational design and modular synthesis of biodegradable ionizable lipids via the Passerini reaction for mRNA delivery. (PNAS 2025)

- DOI: 10.1073/pnas.2409572122 | PMCID: PMC11804478 | PMID: 39883839
- Evidence: Finally, the results from Multiwfn were visualized using Visual Molecular Dynamics (VMD) version 1.9.3 to facilitate the interpretation and presentation of the data ( 48 ). mRNA Delivery in the tdTomato Cre Reporter Mice Model.
- Full pipeline: quantification [ImageJ] -> simulation/modelling [VMD] -> visualisation [PyMOL, VMD]

### Subunit-specific conductance of single homomeric and heteromeric HCN pacemaker channels at femtosiemens resolution. (PNAS 2025)

- DOI: 10.1073/pnas.2422533122 | PMCID: PMC11804576 | PMID: 39879240
- Evidence: Molecular visualizations were made with PyMol and Visual MD (VMD) ( 64 ).
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis] -> visualisation [PyMOL, VMD]

### Enzymes in a human cytoplasm model organize into submetabolon complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2414206122 | PMCID: PMC11804712 | PMID: 39874290
- Evidence: VMD software ( 64 ) was then used both for addition of inorganic ions and finally water molecules into the system.
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [MDAnalysis, VMD]

### Macromolecular interactions and geometrical confinement determine the 3D diffusion of ribosome-sized particles in live &lt;i&gt;Escherichia coli&lt;/i&gt; cells. (PNAS 2025)

- DOI: 10.1073/pnas.2406340121 | PMCID: PMC11789073 | PMID: 39854229
- Evidence: Visualizations of the model were created using visual molecular dynamics [VMD, ( 74 )].
- Full pipeline: simulation/modelling [LAMMPS, VMD] -> visualisation [VMD]

### A room temperature rechargeable Li-LiNO&lt;sub&gt;3&lt;/sub&gt; battery with high capacity. (PNAS 2025)

- DOI: 10.1073/pnas.2416817122 | PMCID: PMC11760503 | PMID: 39805020
- Evidence: The snapshot of MD simulation is produced by VMD software ( 27 ).
- Full pipeline: simulation/modelling [GROMACS, VMD]

### Monofluorinated acetal electrolyte for high-performance lithium metal batteries. (PNAS 2025)

- DOI: 10.1073/pnas.2418623122 | PMCID: PMC11745313 | PMID: 39772742
- Evidence: Snapshots of the various solvation shells, sampled from the simulation trajectory, were also obtained using Visual MD (VMD) software.
- Full pipeline: simulation/modelling [VMD] -> stage not stated [LAMMPS]

### From bedside to bench: A multimodal approach uncovering the molecular basis of the &lt;i&gt;MYBPC1&lt;/i&gt;-linked Myotrem myopathy. (PNAS 2026)

- DOI: 10.1073/pnas.2529897123 | PMCID: PMC13250559 | PMID: 42224599
- Evidence: Structural models were analyzed with VMD ( 53 ) and Pymol ( 54 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [VMD]

### Targeting the polyene chain represents an adjuvant strategy for optimizing polyene antifungals. (PNAS 2026)

- DOI: 10.1073/pnas.2534610123 | PMCID: PMC13123897 | PMID: 42012944
- Version used: **1.9.4**
- Evidence: The molecular visualizations were carried out using the VMD v1.9.4 (Visual Molecular Dynamics) software.
- Full pipeline: quantification [ImageJ] -> simulation/modelling [VMD v1.9.4] -> visualisation [VMD v1.9.4]

### Quinones operate as proton-collecting antennas in energy-transducing membranes. (PNAS 2026)

- DOI: 10.1073/pnas.2534025123 | PMCID: PMC13099693 | PMID: 41980103
- Evidence: ( 85 ) The QM/MM-MD simulations were performed with a 1 fs integration timestep and T = 310 K using FermiONs++ ( 86 ), and trajectories were analyzed using Visual Molecular Dynamics (VMD) (79) and MDAnalysis ( 80 ).
- Full pipeline: simulation/modelling [MDAnalysis, VMD] -> stage not stated [Python]

### Oseltamivir aziridines are potent influenza neuraminidase inhibitors and imaging agents. (PNAS 2026)

- DOI: 10.1073/pnas.2504045123 | PMCID: PMC13038069 | PMID: 41871250
- Evidence: A 100 ns production run was conducted with unrestrained dynamics, using AMBER20 for simulations and VMD/cpptraj for analysis.
- Full pipeline: simulation/modelling [VMD] -> machine learning [VMD] -> stage not stated [PLUMED]

### Synaptic transmission: Munc13 assembles onto PI(4,5)P&lt;sub&gt;2&lt;/sub&gt;-rich domains into trimers that cooperate to capture vesicles. (PNAS 2026)

- DOI: 10.1073/pnas.2523347123 | PMCID: PMC12912961 | PMID: 41671179
- Evidence: VMD ( 58 ) was used to display the membrane system containing peptides.
- Full pipeline: alignment/mapping [IMOD] -> quantification [ImageJ] -> registration [IMOD] -> dimensionality reduction/clustering [ImageJ] -> simulation/modelling [GROMACS] -> visualisation [Topaz] -> stage not stated [AlphaFold, VMD]

### Proton-selective conductance and gating of the lysosomal cation channel TMEM175. (PNAS 2026)

- DOI: 10.1073/pnas.2503909123 | PMCID: PMC12818570 | PMID: 41533442
- Evidence: In addition to 4.0 Å as an established interatomic distance threshold for salt bridges, 3.2 Å was chosen as a more conservative threshold, following standard parameters used in the VMD salt bridges plugin ( 31 , 32 ).
- Full pipeline: simulation/modelling [GROMACS v2021.5] -> stage not stated [ColabFold, VMD]

### Controlled dynamic remodeling of the spliceosome active site enables the first step of splicing. (PNAS 2026)

- DOI: 10.1073/pnas.2522293123 | PMCID: PMC12773743 | PMID: 41474748
- Evidence: MD trajectories were analyzed using VMD ( 62 ).
- Full pipeline: simulation/modelling [PLUMED v2.9, VMD] -> stage not stated [GROMACS v2023.3, PyMOL]

### Effect of natural mutations of SARS-CoV-2 on spike structure, conformation, and antigenicity. (Science 2021)

- DOI: 10.1126/science.abi6226 | PMCID: PMC8611377 | PMID: 34168071
- Evidence: Vector-based structure analysis Vector analysis of intraprotomer domain positions was performed as described ( 19 ) using the Visual Molecular Dynamics (VMD) ( 65 ) software package Tcl interface ( 66 ).
- Full pipeline: alignment/mapping [PyMOL] -> dimensionality reduction/clustering [R] -> simulation/modelling [VMD] -> structure determination [ChimeraX, PHENIX] -> visualisation [PyMOL] -> stage not stated [RELION]

### The specificity and structure of DNA cross-linking by the gut bacterial genotoxin colibactin. (Science 2025)

- DOI: 10.1126/science.ady3571 | PMCID: PMC12758445 | PMID: 41343624
- Evidence: ...nt R50CA211256 (PWV) National Institutes of Health grant P30CA077598 (ABSR) National Science Foundation grant CBET-1846426 (HJK) HHMI grant 55108516 (VMD) National Institutes of Health grant R01GM123012 (BAJ) Footnotes Competing interests: EPB is an inventor on patent applications related to detection and inhibition of colibactin biosynthesis (U.S.
- Full pipeline: quantification [ImageJ] -> stage not stated [VMD]

