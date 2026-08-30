# OpenMM

- **Category:** md
- **Papers in survey:** 38
- **Journals:** PNAS (30), Nature (3), Cell (3), Science (2)
- **Years:** 2021 (3), 2022 (7), 2023 (6), 2024 (9), 2025 (12), 2026 (1)
- **Versions named:** 7.5 (1), 7.3.1 (1), 8.1.0 (1), 7.4.1 (1), 7.8 (1), 7.6.0 (1), 7.7.0 (1), 7.6 (1), 7.5.0 (1)
- **Pipeline stages it appears in:** simulation/modelling (29), machine learning (3), differential/statistical testing (1), structure determination (1), dimensionality reduction/clustering (1)

## Papers

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ...Kluyver et al., 2016 Version 6.1.5 MDAnalysis Michaud-Agrawal et al., 2011 ; Gowers et al., 2016 Version 1.0.0 NumPy https://numpy.org Version 1.19.1 OpenMM Eastman et al., 2017 Version 7.4.2 OpenMMTools https://github.com/choderalab/openmmtools Version 0.20.0 PyMOL Schrödinger Version 2.3.2 ISOLDE Croll, 2018 Version 1.0.1 ChimeraX Pettersen et al., 2021 Version 1.0 AmberTools Case et al., 2017 V...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### A potent pan-sarbecovirus neutralizing antibody resilient to epitope diversification. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.026 | PMCID: PMC11645210 | PMID: 39383863
- Evidence: Equilibration and production MD were run with OpenMM 8.
- Full pipeline: read trimming [BCFtools v1.10.2, BWA v0.7.17] -> differential/statistical testing [RELION, scikit-learn] -> structure determination [Coot, PHENIX, Topaz] -> machine learning [Topaz, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [OpenMM, Pangolin, Python v3.10]

### Nanoscale DNA tracing reveals the self-organization mechanism of mitotic chromosomes. (Cell 2025)

- DOI: 10.1016/j.cell.2025.02.028 | PMCID: PMC12127698 | PMID: 40132578
- Evidence: 9 3D polymer simulations were performed using the polychrom package which implements OpenMM polymer simulations.
- Full pipeline: quantification [NumPy] -> normalisation [SciPy] -> simulation/modelling [NumPy, OpenMM] -> machine learning [scikit-learn] -> stage not stated [Python, napari, scikit-image]

### Highly accurate protein structure prediction with AlphaFold. (Nature 2021)

- DOI: 10.1038/s41586-021-03819-2 | PMCID: PMC8371605 | PMID: 34265844
- Version used: **7.3.1**
- Evidence: For constrained relaxation of structures, we used OpenMM v.7.3.1 69 with the Amber99sb force field 32 .
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> simulation/modelling [OpenMM v7.3.1] -> machine learning [HMMER, NumPy, OpenMM v7.3.1, Python, TensorFlow]

### Native nucleosomes intrinsically encode genome organization principles. (Nature 2025)

- DOI: 10.1038/s41586-025-08971-7 | PMCID: PMC12240700 | PMID: 40335690
- Evidence: Nucleosome–nucleosome interaction-energy calculations Coarse-grained molecular-dynamics simulations of chromatin were done using OpenMM software 55 .
- Full pipeline: alignment/mapping [Bowtie2, Python] -> simulation/modelling [OpenMM] -> stage not stated [GSEA, Jupyter, scikit-learn]

### Mis-splicing of a neuronal microexon promotes CPEB4 aggregation in ASD. (Nature 2025)

- DOI: 10.1038/s41586-024-08289-w | PMCID: PMC11711090 | PMID: 39633052
- Version used: **7.5**
- Evidence: Molecular simulations Molecular dynamics simulations were performed using the single-bead-per-residue model CALVADOS (v.2) 22 , 23 implemented in OpenMM (v.7.5) 67 .
- Full pipeline: simulation/modelling [MDAnalysis, MDTraj, OpenMM v7.5] -> visualisation [Fiji, ImageJ] -> stage not stated [VMD]

### Enhancing ion transport in charged block copolymers by stabilizing low symmetry morphology: Electrostatic control of interfaces. (PNAS 2021)

- DOI: 10.1073/pnas.2107987118 | PMCID: PMC8364204 | PMID: 34344828
- Evidence: All simulations were performed using OpenMM molecular dynamics package (version 7.4) optimized for massive parallelization with graphical processing unit.
- Full pipeline: simulation/modelling [OpenMM]

### T cell and B cell antigen receptors share a conserved core transmembrane structure. (PNAS 2022)

- DOI: 10.1073/pnas.2208058119 | PMCID: PMC9860311 | PMID: 36409917
- Evidence: All simulations were performed using OpenMM ( 85 , 86 ) with the C36 protein ( 87 ) and lipid ( 88 ) force fields and TIP3P water model ( 89 , 90 ), whose integration time step was set to 2 fs with SHAKE algorithm.
- Full pipeline: simulation/modelling [OpenMM]

### Intrinsically disordered interaction network in an RNA chaperone revealed by native mass spectrometry. (PNAS 2022)

- DOI: 10.1073/pnas.2208780119 | PMCID: PMC9704730 | PMID: 36375072
- Evidence: All simulations were performed with the MD program OpenMM ( 49 ) and CHARMM36m force-field ( 50 ).
- Full pipeline: simulation/modelling [OpenMM]

### Integrated AlphaFold2 and DEER investigation of the conformational dynamics of a pH-dependent APC antiporter. (PNAS 2022)

- DOI: 10.1073/pnas.2206129119 | PMCID: PMC9407458 | PMID: 35969794
- Evidence: Finally, refinement by OpenMM was replaced by Cartesian minimization using Rosetta FastRelax ( 75 ).
- Full pipeline: quantification [ImageJ v1.53] -> structure determination [OpenMM] -> stage not stated [AlphaFold v2.0.1, ColabFold, SciPy]

### Computationally exploring the mechanism of bacteriophage T7 gp4 helicase translocating along ssDNA. (PNAS 2022)

- DOI: 10.1073/pnas.2202239119 | PMCID: PMC9371691 | PMID: 35914145
- Evidence: Discussion We previously introduced OpenAWSEM and Open3SPN2 as coarse-grained models for protein (AWSEM) and DNA (3SPN.2) MD simulations within the OpenMM framework ( 26 ).
- Full pipeline: dimensionality reduction/clustering [seaborn] -> simulation/modelling [LAMMPS, NAMD, OpenMM] -> stage not stated [PyMOL, VMD]

### Molecular determinants of pH sensing in the proton-activated chloride channel. (PNAS 2022)

- DOI: 10.1073/pnas.2200727119 | PMCID: PMC9351481 | PMID: 35878032
- Version used: **7.5.0**
- Evidence: The production phases of simulations were run with OpenMM 7.5.0 ( 35 ) software and CHARMM36 ( 36 ) force-field parameters for both wild-type PAC constructs.
- Full pipeline: alignment/mapping [MAFFT] -> simulation/modelling [OpenMM v7.5.0]

### In situ optical spectroscopy of crystallization: One crystal nucleation at a time. (PNAS 2022)

- DOI: 10.1073/pnas.2122990119 | PMCID: PMC9169808 | PMID: 35394901
- Evidence: Molecular dynamics simulations were run on the zwitterionic form of glycine in an 8 nm 3 water box using the AMOEBA 2013 forcefield ( 60 ) implemented in the OpenMM toolkit ( 61 ) at two concentrations: 3.3 mol L −1 and 5.2 mol L −1 .
- Full pipeline: simulation/modelling [OpenMM] -> stage not stated [Python]

### Glycosite-deleted mRNA of SARS-CoV-2 spike protein as a broad-spectrum vaccine. (PNAS 2022)

- DOI: 10.1073/pnas.2119995119 | PMCID: PMC8892489 | PMID: 35149556
- Evidence: The S-protein three-dimensional (3D) structure model with representative glycan profile was constructed by CHARMM-GUI and OpenMM programs.
- Full pipeline: dimensionality reduction/clustering [OpenMM]

### A biophysical framework for double-drugging kinases. (PNAS 2023)

- DOI: 10.1073/pnas.2304611120 | PMCID: PMC10450579 | PMID: 37590418
- Version used: **7.6**
- Evidence: All-atom molecular dynamics simulations were conducted using OpenMM 7.6 ( 50 ) and “Making it rain” cloud-based notebook environment ( 51 ).
- Full pipeline: simulation/modelling [OpenMM v7.6, VMD v1.9.4a] -> visualisation [ChimeraX, PyMOL]

### Polymer folding through active processes recreates features of genome organization. (PNAS 2023)

- DOI: 10.1073/pnas.2221726120 | PMCID: PMC10194017 | PMID: 37155885
- Evidence: We also develop more realistic polymer simulations by adapting the “polychrom” software package ( 81 ), a thin wrapper around OpenMM ( 126 ): https://github.com/open2c/polychrom .
- Full pipeline: simulation/modelling [OpenMM]

### Transcription shapes 3D chromatin organization by interacting with loop extrusion. (PNAS 2023)

- DOI: 10.1073/pnas.2210480120 | PMCID: PMC10089175 | PMID: 36897969
- Evidence: Polymer simulations with loop extrusion were performed using OpenMM ( 102 , 103 ) and the openmm-polymer library ( https://github.com/mirnylab/openmm-polymer-legacy ), as described previously ( 9 , 62 , 104 ).
- Full pipeline: normalisation [Python] -> simulation/modelling [OpenMM]

### Apolipoprotein E4 has extensive conformational heterogeneity in lipid-free and lipid-bound forms. (PNAS 2023)

- DOI: 10.1073/pnas.2215371120 | PMCID: PMC9963066 | PMID: 36749730
- Evidence: FAST simulations were performed using GROMACS, and Folding@home simulations were performed using OpenMM.
- Full pipeline: simulation/modelling [GROMACS, OpenMM, PyMOL]

### Charge transfer as a mechanism for chlorophyll fluorescence concentration quenching. (PNAS 2023)

- DOI: 10.1073/pnas.2210811120 | PMCID: PMC9945999 | PMID: 36689657
- Evidence: Molecular dynamics simulations were performed using OpenMM ( 37 ) for 12 different systems: a pair of neutral chlorophyll molecules (Chl – Chl) or a pair of chlorophyll ions (Chl + – Chl − ) embedded in light-harvesting complex 2 (LH2) from purple photosynthetic bacteria ( Rps. acidophila ) or solvated in diethyl ether with an Mg–Mg separation of 8, 10, 12, 14, or 20Å.
- Full pipeline: simulation/modelling [OpenMM] -> stage not stated [SciPy]

### Sequence complexity and monomer rigidity control the morphologies and aging dynamics of protein aggregates. (PNAS 2024)

- DOI: 10.1073/pnas.2409973121 | PMCID: PMC11648916 | PMID: 39642206
- Evidence: We employ low friction Langevin dynamics simulations using the OpenMM software package ( 76 ).
- Full pipeline: simulation/modelling [OpenMM] -> stage not stated [MDTraj]

### Adaptive CVgen: Leveraging reinforcement learning for advanced sampling in protein folding and chemical reactions. (PNAS 2024)

- DOI: 10.1073/pnas.2414205121 | PMCID: PMC11551409 | PMID: 39475640
- Evidence: Molecular dynamics trajectories were generated by the OpenMM software ( 51 ).
- Full pipeline: dimensionality reduction/clustering [PyMOL, scikit-learn] -> simulation/modelling [OpenMM] -> visualisation [Matplotlib, PyMOL] -> stage not stated [AlphaFold, MDTraj]

### Secondary structure determines electron transport in peptides. (PNAS 2024)

- DOI: 10.1073/pnas.2403324121 | PMCID: PMC11317557 | PMID: 39052850
- Version used: **7.7.0**
- Evidence: The solvated systems were then subjected to MD simulations with the CHARMM36m protein force field ( 39 , 40 ) using OpenMM 7.7.0 ( 78 ).
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [OpenMM v7.7.0] -> stage not stated [VMD]

### Control of G protein-coupled receptor function via membrane-interacting intrinsically disordered C-terminal domains. (PNAS 2024)

- DOI: 10.1073/pnas.2407744121 | PMCID: PMC11260148 | PMID: 38985766
- Evidence: MD simulations of an mGluR3 construct containing both TM7 and the CTD (residues 796–879) used initial poses generated using AlphaFold2 ( 75 ) and ColabFold ( 76 ) which were equilibrated using the standard CHARMM-GUI-based protocol and scripts followed by a short, 6-ns run using OpenMM ( 77 ) and the CHARMM36m ( 78 ) forcefield and then simulated for 1,370 ns for each of six replicas.
- Full pipeline: simulation/modelling [AlphaFold, ColabFold, OpenMM]

### An α-ketoglutarate conformational switch controls iron accessibility, activation, and substrate selection of the human FTO protein. (PNAS 2024)

- DOI: 10.1073/pnas.2404457121 | PMCID: PMC11194561 | PMID: 38865275
- Evidence: The fully solvated system was simulated with OpenMM ( 55 ) at a temperature of 303.15 K using the Langevin Middle Integrator with a collision frequency of 2 ps, with an integration timestep of 2 fs, and with a Monte Carlo Barostat maintaining the external pressure at 1 bar.
- Full pipeline: simulation/modelling [MDAnalysis, OpenMM] -> stage not stated [MDTraj]

### The physical and evolutionary energy landscapes of devolved protein sequences corresponding to pseudogenes. (PNAS 2024)

- DOI: 10.1073/pnas.2322428121 | PMCID: PMC11127006 | PMID: 38739795
- Evidence: The AWSEM Hamiltonian H AWSEM is defined as follows: [7] H AWSEM = H Backbone + H Contact + H Burial + H Pap + H β + H Helical + H AM AWSEM energies were calculated using OpenAWSEM, an OpenMM implementation of the AWSEM energy function ( 23 ).
- Full pipeline: alignment/mapping [HMMER] -> stage not stated [OpenMM]

### Perturbative diffraction methods resolve a conformational switch that facilitates a two-step enzymatic mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2313192121 | PMCID: PMC10907320 | PMID: 38386706
- Evidence: All MD simulations were run using OpenMM , and a biasing potential was added between Asn23 and Pro53 using a custom distance force to evaluate the allosteric influence of hinge distance.
- Full pipeline: simulation/modelling [OpenMM] -> structure determination [PyMOL]

### Learning the shape of protein microenvironments with a holographic convolutional neural network. (PNAS 2024)

- DOI: 10.1073/pnas.2300838121 | PMCID: PMC10861886 | PMID: 38300863
- Evidence: PISCES Hydrogen OpenMM PDBFixer d = 18 Å – – – 63 Steerable CNN ( 38 ) Yes SCOP & ASTRAL PDB-REDO charge hydrogen SASA d = 24 Å 1.6 × 10 6 3.3 × 10 7 – 58 Protein MPNN ( 20 ) Yes CATH 4.2 – Entire protein backbone – – – 52.4 H-CNN and existing methods trained to classify residues from the surrounding neighborhoods are listed along with the available information and summary statistics of the models...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [OpenMM] -> machine learning [OpenMM] -> stage not stated [AlphaFold]

### Molecular drivers of RNA phase separation. (PNAS 2025)

- DOI: 10.1073/pnas.2511348122 | PMCID: PMC12625925 | PMID: 41187075
- Evidence: A Monte Carlo barostat, as implemented in OpenMM, was used to maintain an average pressure of 1 bar across all systems.
- Full pipeline: simulation/modelling [OpenMM] -> stage not stated [PyMOL]

### Driving forces of RNA condensation revealed through coarse-grained modeling with explicit Mg&lt;sup&gt;2&lt;/sup&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504583122 | PMCID: PMC12582263 | PMID: 41129218
- Version used: **8.1.0**
- Evidence: All CG simulations were performed using OpenMM 8.1.0 ( 136 ) in the NVT ensemble.
- Full pipeline: simulation/modelling [GROMACS, OpenMM v8.1.0]

### A unified model of transient poration induced by antimicrobial peptides. (PNAS 2025)

- DOI: 10.1073/pnas.2510294122 | PMCID: PMC12415194 | PMID: 40880531
- Version used: **7.4.1**
- Evidence: Conventional MD simulations were run with OpenMM version 7.4.1 ( 73 ) and Anton 2 software version 1.57.1c7 ( 74 ), and were performed in the isothermal–isobaric ensemble (T = 310 K and P = 1 atm).
- Full pipeline: simulation/modelling [OpenMM v7.4.1] -> stage not stated [GROMACS v2021.2, VMD]

### Structural basis of auxin binding and transport by <i>Arabidopsis thaliana</i> AUX1. (PNAS 2025)

- DOI: 10.1073/pnas.2513424122 | PMCID: PMC12337342 | PMID: 40720658
- Evidence: Unrestrained production simulations were performed using OpenMM ( 58 ), with each simulation run for 1 μs using a 2 fs integration time step at 300 K.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [OpenMM, VMD] -> structure determination [PHENIX] -> machine learning [OpenMM] -> visualisation [VMD] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, Coot]

### Reversible molecular simulation for training classical and machine-learning force fields. (PNAS 2025)

- DOI: 10.1073/pnas.2426058122 | PMCID: PMC12146726 | PMID: 40434635
- Evidence: One popular implementation is the Langevin middle integrator from OpenMM [ 64 , 65 ], which has been used successfully for DMS [ 26 ].
- Full pipeline: stage not stated [MDAnalysis, OpenMM, PyTorch]

### De novo discovery of a molecular glue-like macrocyclic peptide that induces MCL1 homodimerization. (PNAS 2025)

- DOI: 10.1073/pnas.2426006122 | PMCID: PMC12002256 | PMID: 40131955
- Version used: **7.8**
- Evidence: All simulations were performed using OpenMM (version 7.8) ( 68 ).
- Full pipeline: simulation/modelling [OpenMM v7.8] -> structure determination [CCP4] -> stage not stated [PyMOL]

### Energy landscape analysis of the development of the chromosome structure across the cell cycle. (PNAS 2025)

- DOI: 10.1073/pnas.2425225122 | PMCID: PMC11962442 | PMID: 40112110
- Evidence: Simulations were performed with the OpenMiChroM toolkit ( 69 ) that uses the OpenMM platform ( 70 ) to run Langevin dynamics.
- Full pipeline: simulation/modelling [OpenMM] -> visualisation [VMD] -> stage not stated [Python]

### Evolutionary rewiring of the dynamic network underpinning allosteric epistasis in NS1 of the influenza A virus. (PNAS 2025)

- DOI: 10.1073/pnas.2410813122 | PMCID: PMC11873825 | PMID: 39977319
- Version used: **7.6.0**
- Evidence: Production dynamics runs were performed using OpenMM version 7.6.0 ( 86 ).
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [NetworkX, OpenMM v7.6.0, Python]

### Direct observation of liquid-liquid phase coexistence in deeply supercooled water using an accurate polarizable multipole model. (PNAS 2026)

- DOI: 10.1073/pnas.2526573123 | PMCID: PMC12846770 | PMID: 41576070
- Evidence: All MD simulations were carried out using the OpenMM software package, version 7.4.1 ( 72 ).
- Full pipeline: simulation/modelling [OpenMM]

### Open science discovery of potent noncovalent SARS-CoV-2 main protease inhibitors. (Science 2023)

- DOI: 10.1126/science.abo7201 | PMCID: PMC7615835 | PMID: 37943932
- Evidence: Alchemical free energy calculations were then prepared using the open source perses relative alchemical free energy toolkit( 40 ) ( https://github.com/choderalab/perses ), and nonequilibrium switching alchemical free energy calculations( 81 ) were run on Folding@home using the OpenMM compute core( 43 ).
- Full pipeline: stage not stated [OpenMM]

### Rules of engagement for condensins and cohesins guide mitotic chromosome formation. (Science 2025)

- DOI: 10.1126/science.adq1709 | PMCID: PMC12118822 | PMID: 40208986
- Evidence: This library utilizes OpenMM ( 104 ) for GPU-accelerated molecular dynamics.
- Full pipeline: dimensionality reduction/clustering [SciPy] -> simulation/modelling [OpenMM] -> visualisation [Matplotlib] -> stage not stated [NetworkX]

