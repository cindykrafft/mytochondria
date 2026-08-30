# PLUMED

- **Category:** md
- **Papers in survey:** 46
- **Journals:** PNAS (44), Nature (2)
- **Years:** 2021 (3), 2022 (7), 2023 (9), 2024 (10), 2025 (13), 2026 (4)
- **Versions named:** 2.9 (3), 2.4 (3), 2.7 (2), 2.4.3 (2), 2.11.0 (1), 2.8 (1), 2.8.0 (1), 2.2.5 (1), 2.8.1 (1), 2.6.3 (1)
- **Pipeline stages it appears in:** simulation/modelling (33), dimensionality reduction/clustering (2), quantification (1), machine learning (1)

## Papers

### Hypocrystalline ceramic aerogels for thermal insulation at extreme conditions. (Nature 2022)

- DOI: 10.1038/s41586-022-04784-0 | PMCID: PMC9242853 | PMID: 35768591
- Evidence: All the simulations were carried out with the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) 58 code, and the WTMetaD simulations were carried out with an additional plugin code 59 PLUMED 2.
- Full pipeline: simulation/modelling [LAMMPS, PLUMED]

### Broadly neutralizing antibodies target a haemagglutinin anchor epitope. (Nature 2022)

- DOI: 10.1038/s41586-021-04356-8 | PMCID: PMC8828479 | PMID: 34942633
- Evidence: Metadynamics simulations To enhance the sampling of the conformational space, well-tempered bias-exchange metadynamics 85 – 87 simulations were performed in GROMACS 88 , 89 with the PLUMED 2 implementation 90 .
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION, UCSF Chimera] -> simulation/modelling [GROMACS, PLUMED] -> visualisation [RELION] -> stage not stated [Jupyter, PHENIX, R, Seurat]

### Rational design of ASCT2 inhibitors using an integrated experimental-computational approach. (PNAS 2021)

- DOI: 10.1073/pnas.2104093118 | PMCID: PMC8449414 | PMID: 34507995
- Evidence: Details of the MD simulations as well as Protein Data Bank (PDB) files of representative conformations can be found on PLUMED-NEST: https://www.plumed-nest.org (accession code 20.015 ).
- Full pipeline: simulation/modelling [PLUMED]

### Computational studies of anaplastic lymphoma kinase mutations reveal common mechanisms of oncogenic activation. (PNAS 2021)

- DOI: 10.1073/pnas.2019132118 | PMCID: PMC7958353 | PMID: 33674381
- Evidence: The biased simulations were performed using PLUMED.
- Full pipeline: simulation/modelling [PLUMED]

### Immature HIV-1 assembles from Gag dimers leaving partial hexamers at lattice edges as potential substrates for proteolytic maturation. (PNAS 2021)

- DOI: 10.1073/pnas.2020054118 | PMCID: PMC7826355 | PMID: 33397805
- Version used: **2.4**
- Evidence: Metadynamics simulations were performed using the PLUMED 2.4 plugin ( 49 ).
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.4] -> visualisation [UCSF Chimera]

### Intrinsically disordered ectodomain modulates ion permeation through a metal transporter. (PNAS 2022)

- DOI: 10.1073/pnas.2214602119 | PMCID: PMC9889885 | PMID: 36409899
- Version used: **2.6.3**
- Evidence: HREX was performed in GROMACS (version 2019) patched with PLUMED (version 2.6.3) using the REST2 method ( 33 – 36 ).
- Full pipeline: simulation/modelling [MDAnalysis, MDTraj] -> stage not stated [GROMACS, PLUMED v2.6.3, VMD]

### Homogeneous ice nucleation in an ab initio machine-learning model of water. (PNAS 2022)

- DOI: 10.1073/pnas.2207294119 | PMCID: PMC9388152 | PMID: 35939708
- Evidence: The calculation of the ice I h –liquid-water interfacial free energy was performed with LAMMPS augmented with the PLUMED enhanced sampling plugin ( 75 , 76 ).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [PLUMED]

### From data to noise to data for mixing physics across temperatures with generative artificial intelligence. (PNAS 2022)

- DOI: 10.1073/pnas.2203656119 | PMCID: PMC9371742 | PMID: 35925885
- Version used: **2.4**
- Evidence: The structures of AIB 9 were saved every 0.2 ps for all simulations and the dihedral angles were calculated using PLUMED 2.4 ( 45 ).
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.4, PyMOL]

### Correlation between the binding affinity and the conformational entropy of nanobody SARS-CoV-2 spike protein complexes. (PNAS 2022)

- DOI: 10.1073/pnas.2205412119 | PMCID: PMC9351521 | PMID: 35858383
- Version used: **2.6.0**
- Evidence: We extracted 32 configurations from the previous NVT equilibration and initiated two individual EMMI simulations, each consisting of 32 replicas with an aggregate runtime of 1 μs using PLUMED.2.6.0-dev ( 82 ).
- Full pipeline: dimensionality reduction/clustering [RELION] -> simulation/modelling [GROMACS, PLUMED v2.6.0] -> structure determination [ChimeraX, PHENIX] -> stage not stated [CCP4]

### Likelihood-based non-Markovian models from molecular dynamics. (PNAS 2022)

- DOI: 10.1073/pnas.2117586119 | PMCID: PMC9060509 | PMID: 35320038
- Evidence: The FPT is estimated for molecular dynamics starting by restraining the initial position with a parabolic potential as a function of r using PLUMED ( 59 ).
- Full pipeline: simulation/modelling [LAMMPS, PLUMED] -> machine learning [PLUMED]

### The role of dynamics in heterogeneous catalysis: Surface diffusivity and N<sub>2</sub> decomposition on Fe(111). (PNAS 2023)

- DOI: 10.1073/pnas.2313023120 | PMCID: PMC10723053 | PMID: 38060558
- Evidence: In both cases, simulations are performed using the PWscf code of Quantum ESPRESSO ( 73 – 75 ) supplemented by the PLUMED plugin ( 76 ) which is an open-source, community-developed library ( 77 ) for enhanced sampling calculations.
- Full pipeline: simulation/modelling [LAMMPS, PLUMED, Quantum ESPRESSO] -> stage not stated [VMD]

### Dimerization mechanism of an inverted-topology ion channel in membranes. (PNAS 2023)

- DOI: 10.1073/pnas.2308454120 | PMCID: PMC10666096 | PMID: 37956279
- Version used: **2.2.5**
- Evidence: Calculations of d min , E’ and the associated atomic forces were carried out using PLUMED 2.2.5 ( 41 ).
- Full pipeline: simulation/modelling [GROMACS v2018.8, NAMD] -> stage not stated [PLUMED v2.2.5]

### Free energies at QM accuracy from force fields via multimap targeted estimation. (PNAS 2023)

- DOI: 10.1073/pnas.2304308120 | PMCID: PMC10655219 | PMID: 37931103
- Version used: **2.8.1**
- Evidence: For molecules 1 and 6 , we also ran an OPES ( 23 ) simulation using AMBER2020 ( 86 ), and PLUMED 2.8.1 ( 87 ) after converting the CHARMM input files to AMBER format with ParmEd ( 88 ).
- Full pipeline: normalisation [PyTorch] -> simulation/modelling [PLUMED v2.8.1, PyTorch]

### Unveiling the catalytic mechanism of GTP hydrolysis in microtubules. (PNAS 2023)

- DOI: 10.1073/pnas.2305899120 | PMCID: PMC10319017 | PMID: 37364095
- Evidence: All enhanced free-energy sampling was carried out using the open-source, community-developed PLUMED library (interfaced with CP2K), version 2.5.3 ( 49 , 50 ).
- Full pipeline: simulation/modelling [GROMACS v2019.4] -> stage not stated [PLUMED, R]

### Disruption of energetic and dynamic base pairing cooperativity in DNA duplexes by an abasic site. (PNAS 2023)

- DOI: 10.1073/pnas.2219124120 | PMCID: PMC10083564 | PMID: 36976762
- Evidence: To efficiently sample the duplex-to-single-strand thermodynamic free energy landscape at various temperatures, we employed well-tempered metadynamics (WTMetaD) via the PLUMED plugin ( 63 ) to enhance sampling of hybridized, dissociated, and intermediate states by accelerating the dynamics in a predefined collective variable (CV) ( 64 ).
- Full pipeline: simulation/modelling [LAMMPS, Python] -> stage not stated [PLUMED]

### Driving and characterizing nucleation of urea and glycine polymorphs in water. (PNAS 2023)

- DOI: 10.1073/pnas.2216099120 | PMCID: PMC9963467 | PMID: 36757888
- Evidence: The input files necessary to reproduce the simulations done in this work are available on PLUMED NEST at https://www.plumed-nest.org/eggs/22/039/ .
- Full pipeline: simulation/modelling [PLUMED, VMD] -> visualisation [VMD] -> stage not stated [GROMACS]

### Supramolecular organization and dynamics of mannosylated phosphatidylinositol lipids in the mycobacterial plasma membrane. (PNAS 2023)

- DOI: 10.1073/pnas.2212755120 | PMCID: PMC9945971 | PMID: 36693100
- Evidence: The XY-positions of single lipids were tracked with PLUMED ( 45 ) ( Fig.
- Full pipeline: simulation/modelling [GROMACS v2021.3, Python] -> stage not stated [AlphaFold, Clustal Omega, Matplotlib, PLUMED]

### Molecular understanding of Ni<sup>2+</sup>-nitrogen family metal-coordinated hydrogel relaxation times using free energy landscapes. (PNAS 2023)

- DOI: 10.1073/pnas.2213160120 | PMCID: PMC9942824 | PMID: 36649435
- Evidence: The simulations are performed using a LAMMPS patch with the PLUMED v2 package.( 17 , 39 ) The biased collective variables are the distances between the center of mass of the coordinating nitrogens on each ligand and the metal ion.
- Full pipeline: simulation/modelling [LAMMPS, PLUMED]

### Road-blocker HSP disease mutation disrupts pre-organization for ATP hydrolysis in kinesin through a second sphere control. (PNAS 2023)

- DOI: 10.1073/pnas.2215170120 | PMCID: PMC9910451 | PMID: 36574689
- Version used: **2.4.3**
- Evidence: The well-tempered metadynamics ( 36 ) simulations were performed in order to compute the two-dimensional free energy profiles for the stability of the Arg203-Glu236 salt-bridge pair using the PLUMED 2.4.3 plugin ( 37 ) for GROMACS.
- Full pipeline: dimensionality reduction/clustering [PLUMED v2.4.3] -> simulation/modelling [GROMACS v5.1, PLUMED v2.4.3, VMD]

### Correlating enzymatic reactivity for different substrates using transferable data-driven collective variables. (PNAS 2024)

- DOI: 10.1073/pnas.2416621121 | PMCID: PMC11626191 | PMID: 39589882
- Evidence: All topologies and initial coordinates are supplied in the PLUMED-NEST repository.
- Full pipeline: simulation/modelling [GROMACS v2021.5] -> visualisation [PyMOL] -> stage not stated [PLUMED]

### Agonist activation to open the Gα subunit of the GPCR-G protein precoupled complex defines functional agonist activation of TAS2R5. (PNAS 2024)

- DOI: 10.1073/pnas.2409987121 | PMCID: PMC11621838 | PMID: 39565310
- Evidence: All simulations were carried out with a 2 fs time step using GROMACS ( 65 ) with PLUMED ( 66 ).
- Full pipeline: simulation/modelling [GROMACS, PLUMED] -> visualisation [VMD]

### Identifying and controlling the order parameter for ultrafast photoinduced phase transitions in thermosalient materials. (PNAS 2024)

- DOI: 10.1073/pnas.2408366121 | PMCID: PMC11573639 | PMID: 39499639
- Evidence: One-dimensional metadynamics simulations were performed using the PLUMED plugin ( 48 – 51 ) with s as CV.
- Full pipeline: dimensionality reduction/clustering [PLUMED] -> simulation/modelling [LAMMPS, PLUMED] -> stage not stated [VMD]

### Plasticity of the selectivity filter is essential for permeation in lysosomal TPC2 channels. (PNAS 2024)

- DOI: 10.1073/pnas.2320153121 | PMCID: PMC11317647 | PMID: 39074274
- Version used: **2.7**
- Evidence: MD simulations were performed with the GROMACS software package ( 65 ), version 2021 and the REST simulations were conducted using GROMACS, version 2021, patched with PLUMED, version 2.7 ( 66 ).
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.7, Python, VMD] -> visualisation [VMD] -> stage not stated [MDAnalysis]

### Entropy drives the ligand recognition in G-protein-coupled receptor subtypes. (PNAS 2024)

- DOI: 10.1073/pnas.2401091121 | PMCID: PMC11287286 | PMID: 39024109
- Evidence: MD and metadynamics simulations were performed using GROMACS ( 55 ) and PLUMED ( 56 ).
- Full pipeline: simulation/modelling [GROMACS, PLUMED]

### Mechanism of phosphate release from actin filaments. (PNAS 2024)

- DOI: 10.1073/pnas.2408156121 | PMCID: PMC11260136 | PMID: 38980907
- Version used: **2.4**
- Evidence: Simulations were performed by using GROMACS 2020.4 compiled with PLUMED 2.4.
- Full pipeline: simulation/modelling [GROMACS v2020.4, PLUMED v2.4, PyMOL, Python] -> stage not stated [VMD]

### Conformational free-energy landscapes of a Na<sup>+</sup>/Ca<sup>2+</sup> exchanger explain its alternating-access mechanism and functional specificity. (PNAS 2024)

- DOI: 10.1073/pnas.2318009121 | PMCID: PMC11032461 | PMID: 38588414
- Evidence: Conventional and enhanced-sampling MD simulations were carried out using GROMACS2018 or GROMACS 4.5.5 with PLUMED ( 48 – 51 ), at constant temperature (298 K), pressure (1 bar) and periodic-boundary conditions.
- Full pipeline: simulation/modelling [GROMACS v4.5.5, PLUMED]

### Data-driven classification of ligand unbinding pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2313542121 | PMCID: PMC10927508 | PMID: 38412121
- Version used: **2.9**
- Evidence: Langevin dynamics simulations for the 2D Müller Brown potential are performed using the https://www.plumed.org/doc-master/user-doc/html/vesmdlinearexpansion.html module of PLUMED v2.9, with a setup identical to ref.
- Full pipeline: dimensionality reduction/clustering [Python] -> simulation/modelling [GROMACS v2021.5, PLUMED v2.9, Python]

### The elementary reactions for incorporation into crystals. (PNAS 2024)

- DOI: 10.1073/pnas.2320201121 | PMCID: PMC10873555 | PMID: 38315836
- Version used: **2.4.3**
- Evidence: The WTmetaD simulations were performed in the N P z T ensemble at 300 K and 1 bar using the PLUMED 2.4.3 free energy plug-in for GROMACS.
- Full pipeline: simulation/modelling [PLUMED v2.4.3] -> stage not stated [GROMACS v5.1.5]

### B56δ long-disordered arms form a dynamic PP2A regulation interface coupled with global allostery and Jordan's syndrome mutations. (PNAS 2024)

- DOI: 10.1073/pnas.2310727120 | PMCID: PMC10769853 | PMID: 38150499
- Version used: **2.8.0**
- Evidence: Molecular dynamics (MD) simulations were performed using Gromacs ( 66 ) patched with PLUMED 2.8.0 in the Amber ff14SB forcefield ( 67 ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [GROMACS, PLUMED v2.8.0] -> structure determination [PHENIX]

### Data-driven enhanced sampling of mechanistic pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2517169122 | PMCID: PMC12704791 | PMID: 41343671
- Version used: **2.11.0**
- Evidence: Materials and Methods All atomistic simulations were performed using the GROMACS package patched with the PLUMED 2.11.0-dev git: 9045979ca (PLUMED v2.11) ( 72 ) package.
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.11.0] -> machine learning [PyTorch]

### Reaching the full potential of cryo-EM reconstructions with molecular dynamics simulations at 310 K: Actin filaments as an example. (PNAS 2025)

- DOI: 10.1073/pnas.2521421122 | PMCID: PMC12685034 | PMID: 41289381
- Version used: **2.7**
- Evidence: All the MD simulations were performed using GROMACS 2021.5 ( 71 ) with PLUMED 2.7 ( 72 ).
- Full pipeline: simulation/modelling [GROMACS v2021.5, PLUMED v2.7]

### Transcriptional condensates encode a "golden mean" to optimize enhancer-promoter communication across genomic distances. (PNAS 2025)

- DOI: 10.1073/pnas.2513371122 | PMCID: PMC12582294 | PMID: 41134621
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability The necessary files for setting up the Gromacs simulations with PLUMED and the analysis scripts are publicly available at GitHub ( https://github.com/icecolaTao/ChrTFModel ) ( 88 ).
- Full pipeline: dimensionality reduction/clustering [Python] -> simulation/modelling [GROMACS v4.5.7, PLUMED, Python]

### Mineral dissolution by dimeric complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2504109122 | PMCID: PMC12541406 | PMID: 41052339
- Evidence: Both sets of simulations were performed in CP2K ( 73 ) and PLUMED ( 74 ) was used to apply the harmonic restraints.
- Full pipeline: simulation/modelling [PLUMED] -> machine learning [Jupyter, Keras, Python, TensorFlow] -> stage not stated [ImageJ]

### Ab initio machine-learning simulation of calcium carbonate from aqueous solutions to the solid state. (PNAS 2025)

- DOI: 10.1073/pnas.2415663122 | PMCID: PMC12541341 | PMID: 41052335
- Evidence: All simulations used LAMMPS ( 66 ) patched with the DeePMD-kit ( 59 ) and the PLUMED enhanced sampling plugin ( 67 , 68 ).
- Full pipeline: simulation/modelling [LAMMPS, PLUMED]

### Weighted active space protocol for multireference machine-learned potentials. (PNAS 2025)

- DOI: 10.1073/pnas.2513693122 | PMCID: PMC12478124 | PMID: 40953275
- Version used: **2.9**
- Evidence: Molecular dynamics simulations are performed using the large-scale atomic/molecular massively parallel simulator (LAMMPS) ( 81 ), interfaced with MACE (version 0.3.7) ( 60 ) and PLUMED (version 2.9) ( 82 ).
- Full pipeline: simulation/modelling [LAMMPS, PLUMED v2.9] -> stage not stated [PySCF]

### CO&lt;sub&gt;2&lt;/sub&gt; hydration at the air-water interface: A surface-mediated "in-and-out" mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2502684122 | PMCID: PMC12402993 | PMID: 40833411
- Evidence: Well-tempered metadynamics was performed by coupling LAMMPS with the multiple walker setup available in PLUMED ( 74 – 76 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [LAMMPS, PLUMED]

### Regulation of the ordinal DNA translocation cycle in bacteriophage Φ29 through trans-subunit interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2504780122 | PMCID: PMC12260519 | PMID: 40608675
- Evidence: The sampling was set up using the PLUMED library ( 27 , 28 ).
- Full pipeline: simulation/modelling [ChimeraX, VMD] -> visualisation [ChimeraX, VMD] -> stage not stated [AlphaFold, PLUMED]

### Deciphering Ca&lt;sup&gt;&lt;b&gt;2+&lt;/b&gt;&lt;/sup&gt; permeation and valence selectivity in Ca&lt;sub&gt;V&lt;/sub&gt;1: Molecular dynamics simulations reveal the three-ion knock-on mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2424694122 | PMCID: PMC12146731 | PMID: 40440072
- Evidence: We performed Metadynamics simulations using GROMACS patched with PLUMED ( 81 ) to quantify the PMF for ion permeation in Ca V .
- Full pipeline: quantification [PLUMED] -> simulation/modelling [GROMACS v2021.2, MDAnalysis, PLUMED] -> structure determination [VMD] -> visualisation [PyMOL] -> stage not stated [NetworkX]

### A direct computational assessment of vinculin-actin unbinding kinetics reveals catch-bonding behavior. (PNAS 2025)

- DOI: 10.1073/pnas.2425982122 | PMCID: PMC12130851 | PMID: 40397673
- Evidence: To characterize the motion of Vt relative to actin, we used PLUMED ( 74 ) to define two vectors shown in Fig.
- Full pipeline: stage not stated [PLUMED, SciPy, VMD]

### Exploring RNA destabilization mechanisms in biomolecular condensates through atomistic simulations. (PNAS 2025)

- DOI: 10.1073/pnas.2425261122 | PMCID: PMC12012522 | PMID: 40203038
- Version used: **2.8**
- Evidence: Materials and Methods MD simulations were performed using GROMACS 2021.4 ( 65 ) patched with PLUMED 2.8 ( 66 , 67 ) to perform Well-Tempered Metadynamics ( 44 ) (WT-MetaD) and using a general Hamiltonian replica exchange implementation ( 68 ).
- Full pipeline: simulation/modelling [GROMACS v2021.4, PLUMED v2.8]

### Allosterically switchable network orients &lt;i&gt;β&lt;/i&gt;-flap in &lt;i&gt;Clostridioides difficile&lt;/i&gt; toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2419263122 | PMCID: PMC12002228 | PMID: 40172960
- Evidence: Umbrella sampling was implemented with PLUMED ( 61 ), with two harmonic biasing potentials to restrain sampling in ( ξ 1 , ξ 2 ) space.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, PLUMED]

### Moisture-driven carbonation kinetics for ultrafast CO&lt;sub&gt;2&lt;/sub&gt; mineralization. (PNAS 2025)

- DOI: 10.1073/pnas.2418239121 | PMCID: PMC11725878 | PMID: 39793077
- Evidence: The metadynamics simulations were executed with the PLUMED ( 58 ) plugin interfaced with LAMMPS.
- Full pipeline: simulation/modelling [PLUMED] -> stage not stated [LAMMPS]

### Chemical neighborhood exploration for substrate discovery in biocatalysis. (PNAS 2026)

- DOI: 10.1073/pnas.2535430123 | PMCID: PMC13273237 | PMID: 42258720
- Evidence: For each complex, three independent 500 ps metadynamics trajectories were run at 298 K using DFTB+ with GBSA implicit solvation and PLUMED metadynamics module.
- Full pipeline: simulation/modelling [PLUMED]

### Sterol divergence across eukaryotic kingdoms determines membrane susceptibility to saponins, a class of plant defense compounds. (PNAS 2026)

- DOI: 10.1073/pnas.2523859123 | PMCID: PMC13168540 | PMID: 42101991
- Evidence: For inserted systems, starting configurations were generated by pulling saponins from the aqueous phase toward the membrane hydrophobic region using a harmonic bias ( 53 , 54 ) implemented in PLUMED ( 55 – 57 ).
- Full pipeline: simulation/modelling [GROMACS v2021.5] -> stage not stated [PLUMED]

### Oseltamivir aziridines are potent influenza neuraminidase inhibitors and imaging agents. (PNAS 2026)

- DOI: 10.1073/pnas.2504045123 | PMCID: PMC13038069 | PMID: 41871250
- Evidence: Reaction mechanisms, including covalent adduct formation and elimination, were studied using OPES Explore in CP2K with PLUMED.
- Full pipeline: simulation/modelling [VMD] -> machine learning [VMD] -> stage not stated [PLUMED]

### Controlled dynamic remodeling of the spliceosome active site enables the first step of splicing. (PNAS 2026)

- DOI: 10.1073/pnas.2522293123 | PMCID: PMC12773743 | PMID: 41474748
- Version used: **2.9**
- Evidence: Well-tempered metadynamics ( 60 ) simulations were run on the wild type B ACT complex, using PLUMED 2.9 ( 61 ) patched into GROMACS 2023.3 ( 55 ).
- Full pipeline: simulation/modelling [PLUMED v2.9, VMD] -> stage not stated [GROMACS v2023.3, PyMOL]

