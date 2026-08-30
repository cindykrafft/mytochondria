# NAMD

- **Category:** md
- **Papers in survey:** 75
- **Journals:** PNAS (63), Nature (10), Cell (2)
- **Years:** 2021 (7), 2022 (18), 2023 (19), 2024 (15), 2025 (12), 2026 (4)
- **Versions named:** 2.14 (10), 2.13 (5), 2.12 (4), 3.0 (2), 2.9 (2), 3.0.1 (1), 2.0 (1)
- **Pipeline stages it appears in:** simulation/modelling (66), normalisation (1), dimensionality reduction/clustering (1), alignment/mapping (1)

## Papers

### Virus-encoded histone doublets are essential and form nucleosome-like structures. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.032 | PMCID: PMC8357426 | PMID: 34297924
- Evidence: ... webserver Waterhouse et al., 2018 https://swissmodel.expasy.org/interactive MODELER (ver 9.20) Sali and Blundell, 1993 https://salilab.org/modeller/ NAMD (CUDA-accelerated, ver 2.13) Chan et al., 2012 https://www.ks.uiuc.edu/Research/namd/ CHARMM36 Forcefield Parameters Huang and MacKerell, 2013 http://mackerell.umaryland.edu/charmm_ff.shtml#charmm VMD (ver 1.9.3) Humphrey et al., 1996 . https://...
- Full pipeline: alignment/mapping [MAFFT] -> quantification [R, RSEM, edgeR] -> normalisation [R, RSEM, edgeR] -> structure determination [PHENIX] -> stage not stated [NAMD, UCSF Chimera, VMD v1.9.3]

### Dynamic 3D proteomes reveal protein functional alterations at high resolution in situ. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.021 | PMCID: PMC7836100 | PMID: 33357446
- Version used: **2.13**
- Evidence: ...//www.chemaxon.com Maestro 11.5 Schrödinger https://www.schrodinger.com/freemaestro AutoDock Vina 1.1.2 Trott and Olson, 2010 http://vina.scripps.edu NAMD 2.13 University of Illinois at Urbana-Champaign https://www.ks.uiuc.edu/Research/namd CHARMM 42b2 Harvard University https://www.charmm.org Other Amicon Desalting Columns 3 kDa MWCO Merck N/A Freezer Mill, 6870 SPEX SamplePrep N/A Ni-IMAC column...
- Full pipeline: differential/statistical testing [SciPy, limma] -> stage not stated [AutoDock Vina v1.1.2, Bioconductor, NAMD v2.13, PyMOL v2.4, Python, R, pheatmap, seaborn]

### Structures of the TMC-1 complex illuminate mechanosensory transduction. (Nature 2022)

- DOI: 10.1038/s41586-022-05314-8 | PMCID: PMC9605866 | PMID: 36224384
- Evidence: The coordination of Ca 2+ ions in this step was maintained by the application of the Extra Bonds algorithm in NAMD 77 , 78 , (3) 200 ps of equilibration during which the restraints on the backbone were maintained whereas the Extra Bonds on the Ca 2+ ions were removed; (4) two additional replicas were generated with the MMP plugin and 1 μs of production runs were performed on each of the three inde...
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [ChimeraX, PHENIX] -> stage not stated [NAMD, UCSF Chimera, VMD]

### Inhibition of calcium-triggered secretion by hydrocarbon-stapled peptides. (Nature 2022)

- DOI: 10.1038/s41586-022-04543-1 | PMCID: PMC8967716 | PMID: 35322233
- Evidence: For all of the simulations, the NAMD program was used 65 .
- Full pipeline: quantification [ImageJ v2.0.0] -> simulation/modelling [NAMD] -> stage not stated [EMAN2, PyMOL v2.5.1, VMD]

### HIV-1 Env trimers asymmetrically engage CD4 receptors in membranes. (Nature 2023)

- DOI: 10.1038/s41586-023-06762-6 | PMCID: PMC10686830 | PMID: 37993716
- Version used: **3.0**
- Evidence: The MDFF simulations were conducted using NAMD v.3.0 alpha 57 with CHARMM36 force-field parameters 58 , at a temperature of 300 K in vacuo.
- Full pipeline: simulation/modelling [NAMD v3.0] -> structure determination [ChimeraX] -> visualisation [ChimeraX, IMOD] -> stage not stated [Python, RELION]

### Class B1 GPCR activation by an intracellular agonist. (Nature 2023)

- DOI: 10.1038/s41586-023-06169-3 | PMCID: PMC10307627 | PMID: 37286611
- Version used: **2.13**
- Evidence: Molecular dynamics simulations were performed with the program NAMD (v.2.13).
- Full pipeline: registration [RELION] -> simulation/modelling [MDTraj v1.9.8, NAMD v2.13, seaborn] -> visualisation [MDTraj v1.9.8, seaborn] -> stage not stated [Fiji, ImageJ, VMD v1.9.3]

### In situ architecture of the ER-mitochondria encounter structure. (Nature 2023)

- DOI: 10.1038/s41586-023-06050-3 | PMCID: PMC7614606 | PMID: 37165187
- Evidence: All the simulations were performed using NAMD Git2021-11-23 with CUDA acceleration 72 .
- Full pipeline: alignment/mapping [IMOD, UCSF Chimera] -> quantification [ImageJ] -> simulation/modelling [NAMD] -> structure determination [IMOD] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, R, VMD]

### Membraneless channels sieve cations in ammonia-oxidizing marine archaea. (Nature 2024)

- DOI: 10.1038/s41586-024-07462-5 | PMCID: PMC11153153 | PMID: 38811725
- Version used: **2.14**
- Evidence: All simulations were conducted using NAMD (v.2.14) 68 and the CHARMM36 force field 38 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [NAMD v2.14, VMD v1.94] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold v2.2.0, MotionCor2]

### The structure of apolipoprotein B100 from human low-density lipoprotein. (Nature 2025)

- DOI: 10.1038/s41586-024-08467-w | PMCID: PMC11839476 | PMID: 39662503
- Version used: **2.14**
- Evidence: All simulations were performed using NAMD (v.2.14) 54 , 55 and the CHARMM36 force field 56 .
- Full pipeline: simulation/modelling [NAMD v2.14, PHENIX v1.20] -> structure determination [PHENIX v1.20] -> machine learning [PHENIX v1.20] -> visualisation [ChimeraX, VMD v1.9.4] -> stage not stated [AlphaFold, ColabFold]

### Snapshots of the dynamic basis of NTSR1 G protein subtype promiscuity. (Nature 2026)

- DOI: 10.1038/s41586-026-10120-7 | PMCID: PMC13083256 | PMID: 41813894
- Evidence: Simulations were performed in NAMD 51 with the CHARMM36 forcefield 52 – 54 using a Langevin thermostat and Nose-Hoover Langevin piston barostat at 1 atm with a period of 150 fs and decay of 75 fs.
- Full pipeline: simulation/modelling [NAMD] -> structure determination [Coot, PHENIX] -> stage not stated [Python, VMD]

### Integrase anchors viral RNA to the HIV-1 capsid interior. (Nature 2026)

- DOI: 10.1038/s41586-026-10154-x | PMCID: PMC13102720 | PMID: 41708858
- Version used: **3.0.1**
- Evidence: For MDFF, we first performed energy minimization, coupling the protein backbone and heavy atoms of IP6 to the cryo-EM density using the gridForces module in NAMD (v.3.0.1) 90 with a gridScaling factor of 0.3 kcal mol −1 amu −1 .
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0, RELION] -> normalisation [ImageJ, NAMD v3.0.1] -> simulation/modelling [VMD] -> structure determination [ChimeraX, Coot, IMOD] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PyMOL, Topaz, UCSF Chimera]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Evidence: Molecular dynamics simulation protocols All the molecular dynamics simulations were executed using the NAMD 93 program.
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### Rational prioritization strategy allows the design of macrolide derivatives that overcome antibiotic resistance. (PNAS 2021)

- DOI: 10.1073/pnas.2113632118 | PMCID: PMC8609559 | PMID: 34750269
- Evidence: Materials and Methods The simulations were carried out using the CHARMM ( 36 , 37 ) and NAMD ( 38 ) programs with the CHARMM36 force field ( 39 – 41 ).
- Full pipeline: simulation/modelling [NAMD]

### Deactivation blocks proton pathways in the mitochondrial complex I. (PNAS 2021)

- DOI: 10.1073/pnas.2019498118 | PMCID: PMC8307655 | PMID: 34272275
- Evidence: The Lennard–Jones cutoff was set to 12 Å using Nanoscale Molecular Dynamics' (NAMD) built-in switching function starting at 10 Å, and rigid bonds were modeled using the ShakeH algorithm.
- Full pipeline: simulation/modelling [GROMACS v2016.3, NAMD, PyMOL v2.4.1]

### Regulation and drug modulation of a voltage-gated sodium channel: Pivotal role of the S4-S5 linker in activation and slow inactivation. (PNAS 2021)

- DOI: 10.1073/pnas.2102285118 | PMCID: PMC8285963 | PMID: 34260401
- Version used: **2.12**
- Evidence: MD simulations were carried out using NAMD 2.12 with the CHARMM36 all-atom potential energy functions for protein and phospholipids, and the TIP3P potential for water molecules.
- Full pipeline: simulation/modelling [NAMD v2.12]

### Periscope Proteins are variable-length regulators of bacterial cell surface interactions. (PNAS 2021)

- DOI: 10.1073/pnas.2101349118 | PMCID: PMC8201768 | PMID: 34074781
- Evidence: Simulations have been performed using the CHARMM36m ( 56 ) force field and NAMD ( 57 ).
- Full pipeline: dimensionality reduction/clustering [BLAST] -> simulation/modelling [NAMD] -> structure determination [PHENIX]

### Cross-subunit interactions that stabilize open states mediate gating in NMDA receptors. (PNAS 2021)

- DOI: 10.1073/pnas.2007511118 | PMCID: PMC7812756 | PMID: 33384330
- Evidence: Targeted molecular dynamics simulations were performed with NAMD V2.9b2 using a putative open-state structure as the target conformation ( 20 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [VMD]

### Mechanism of voltage gating in the voltage-sensing phosphatase Ci-VSP. (PNAS 2022)

- DOI: 10.1073/pnas.2206649119 | PMCID: PMC9636939 | PMID: 36279472
- Evidence: MD simulations were performed using the program NAMD ( 53 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [VMD]

### Mechanism of 4-aminopyridine inhibition of the lysosomal channel TMEM175. (PNAS 2022)

- DOI: 10.1073/pnas.2208882119 | PMCID: PMC9636928 | PMID: 36279431
- Version used: **2.12**
- Evidence: All simulations were conducted with NAMD 2.12 using the CHARMM36 force field for protein and lipids ( 35 – 38 ).
- Full pipeline: alignment/mapping [VMD] -> simulation/modelling [NAMD v2.12] -> structure determination [PHENIX] -> stage not stated [RELION v3.0]

### Discovering design principles of collagen molecular stability using a genetic algorithm, deep learning, and experimental validation. (PNAS 2022)

- DOI: 10.1073/pnas.2209524119 | PMCID: PMC9546622 | PMID: 36161946
- Evidence: MD simulations were performed using the Nanoscale Molecular Dynamics (NAMD) code with the Chemistry at Harvard Macromolecular Mechanics (CHARMM) force field ( 73 , 74 ), which also includes parameters for the hydroxyproline residue.
- Full pipeline: simulation/modelling [NAMD]

### Electric fields control water-gated proton transfer in cytochrome <i>c</i> oxidase. (PNAS 2022)

- DOI: 10.1073/pnas.2207761119 | PMCID: PMC9499568 | PMID: 36095184
- Version used: **2.14**
- Evidence: All DFT calculations were performed with TURBOMOLE v7.2–7.5 ( 81 ), QM/MM calculations with CHARMM v38 ( 82 ) and TURBOMOLE v7.2–7.5 ( 81 ), coupled by a Python interface ( 83 ), and classical MD simulations with NAMD v2.14 and NAMD v3.0 ( 84 ).
- Full pipeline: simulation/modelling [NAMD v2.14]

### Computationally exploring the mechanism of bacteriophage T7 gp4 helicase translocating along ssDNA. (PNAS 2022)

- DOI: 10.1073/pnas.2202239119 | PMCID: PMC9371691 | PMID: 35914145
- Evidence: Then 10,000 steps on equilibration simulation with CHARMM27 force field was carried at NAMD.
- Full pipeline: dimensionality reduction/clustering [seaborn] -> simulation/modelling [LAMMPS, NAMD, OpenMM] -> stage not stated [PyMOL, VMD]

### Posttranslational modifications optimize the ability of SARS-CoV-2 spike for effective interaction with host cell receptors. (PNAS 2022)

- DOI: 10.1073/pnas.2119761119 | PMCID: PMC9282386 | PMID: 35737823
- Evidence: MD simulations of the full-length, membrane-embedded spike structure in both glycosylated and nonglycosylated forms (5 µs each) were then performed in NAMD ( 82 , 83 ) using CHARMM36m ( 84 , 85 ).
- Full pipeline: alignment/mapping [MAFFT] -> simulation/modelling [NAMD, VMD] -> visualisation [MAFFT]

### A fine balance of hydrophobic-electrostatic communication pathways in a pH-switching protein. (PNAS 2022)

- DOI: 10.1073/pnas.2119686119 | PMCID: PMC9245636 | PMID: 35737838
- Evidence: Simulations were performed with the Nanoscale Molecular Dynamics (NAMD) package using the TIP3P water model and AMBER03 force field.
- Full pipeline: simulation/modelling [NAMD]

### Molecular determinants of inhibition of the human proton channel hHv1 by the designer peptide C6 and a bivalent derivative. (PNAS 2022)

- DOI: 10.1073/pnas.2120750119 | PMCID: PMC9191634 | PMID: 35648818
- Evidence: The two final C6-membrane systems were minimized and equilibrated by using NAMD ( 50 ) and then simulated for 1 μs on the special-purpose computer Anton2 ( 51 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [AlphaFold, VMD]

### Mechanism of tethered agonist-mediated signaling by polycystin-1. (PNAS 2022)

- DOI: 10.1073/pnas.2113786119 | PMCID: PMC9171645 | PMID: 35522707
- Evidence: The output files of cMD simulations using NAMD were converted to AMBER format using the ParmEd tool AMBER package ( 61 ).
- Full pipeline: simulation/modelling [NAMD]

### An allosteric HTRA1-calpain 2 complex with restricted activation profile. (PNAS 2022)

- DOI: 10.1073/pnas.2113520119 | PMCID: PMC9168489 | PMID: 35349341
- Version used: **2.9**
- Evidence: The MD simulations (120 ns each, 2 fs time step) were carried out with NAMD 2.9 and the CHARMM22 force field (including energy grid correction map, CMAP) as well as particle mesh Ewald (PME) method for electrostatic interactions.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> simulation/modelling [NAMD v2.9] -> stage not stated [AlphaFold, AutoDock Vina]

### A tethered ligand assay to probe SARS-CoV-2:ACE2 interactions. (PNAS 2022)

- DOI: 10.1073/pnas.2114397119 | PMCID: PMC9168514 | PMID: 35312342
- Evidence: Over 300 SMD simulations were performed employing GPU-accelerated NAMD 3 ( 43 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [Python, VMD]

### Strain and rupture of HIV-1 capsids during uncoating. (PNAS 2022)

- DOI: 10.1073/pnas.2117781119 | PMCID: PMC8915963 | PMID: 35238630
- Version used: **2.14**
- Evidence: All simulations used the AAMD simulation package NAMD 2.14 ( 41 ).
- Full pipeline: alignment/mapping [IMOD] -> simulation/modelling [LAMMPS, NAMD v2.14]

### Bivalent recognition of fatty acyl-CoA by a human integral membrane palmitoyltransferase. (PNAS 2022)

- DOI: 10.1073/pnas.2022050119 | PMCID: PMC8851515 | PMID: 35140179
- Version used: **2.13**
- Evidence: The simulations were carried out using NAMD 2.13 ( 31 , 32 ) and the CHARMM36 force field ( 33 , 34 ) at constant temperature (298 K) and constant pressure (1 atm) with periodic boundary conditions.
- Full pipeline: simulation/modelling [NAMD v2.13] -> structure determination [PHENIX]

### Ultrafast photooxidation of protein-bound anionic flavin radicals. (PNAS 2022)

- DOI: 10.1073/pnas.2118924119 | PMCID: PMC8872763 | PMID: 35181610
- Evidence: For GOX, MDFE simulations for calculating p K a values and full-protein MD simulations were carried out using the NAMD program (version 2.13) ( 75 ).
- Full pipeline: simulation/modelling [NAMD]

### Rearrangement of a unique Kv1.3 selectivity filter conformation upon binding of a drug. (PNAS 2022)

- DOI: 10.1073/pnas.2113536119 | PMCID: PMC8812516 | PMID: 35091471
- Evidence: These were equilibrated with the NAMD program in maintaining constant number of particles, pressure, and temperature (NPT) ensemble at 310 K and 1 atm pressure for 90 ns using a staged MDS protocol with gradually reduced restraints during the first 40 ns ( 48 ).
- Full pipeline: alignment/mapping [MotionCor2] -> registration [MotionCor2] -> simulation/modelling [UCSF Chimera, VMD] -> structure determination [PHENIX] -> stage not stated [CTFFIND, NAMD, RELION]

### Role of internal loop dynamics in antibiotic permeability of outer membrane porins. (PNAS 2022)

- DOI: 10.1073/pnas.2117009119 | PMCID: PMC8872756 | PMID: 35193963
- Evidence: The system was used for 10 independent 1-µs MD simulations in NAMD ( 63 , 64 ) using CHARMM36m ( 65 ) and CHARMM36 ( 66 ) force-field parameters, particle mesh Ewald (PME) ( 67 ), and constant pressure/temperature ( 68 , 69 ).
- Full pipeline: simulation/modelling [NAMD]

### Structural and thermodynamic framework for PIEZO1 modulation by small molecules. (PNAS 2023)

- DOI: 10.1073/pnas.2310933120 | PMCID: PMC10723123 | PMID: 38060566
- Evidence: Two ensemble distributions were computed from a total of 500 ns unbiased trajectories: 1) the distance R between center of mass (COM) of ligand and the binding site and 2) ligand conformational RMSD after rigid-body alignment of the binding site to the initial snapshot, i.e., distance-to-bound-configuration (DBC) in NAMD colvars ( 61 ).
- Full pipeline: alignment/mapping [NAMD] -> simulation/modelling [GROMACS v2016.4, NAMD] -> stage not stated [AlphaFold, AutoDock Vina]

### Ultrafast many-body bright-dark exciton transition in anatase TiO<sub>2</sub>. (PNAS 2023)

- DOI: 10.1073/pnas.2307671120 | PMCID: PMC10666115 | PMID: 37956295
- Evidence: The BSE calculation is performed with the self-developed Hefei-NAMD code ( 50 , 52 ), where GW + rtBSE-NAMD is implemented.
- Full pipeline: stage not stated [NAMD]

### Dimerization mechanism of an inverted-topology ion channel in membranes. (PNAS 2023)

- DOI: 10.1073/pnas.2308454120 | PMCID: PMC10666096 | PMID: 37956279
- Evidence: These trajectories were calculated with NAMD ( 43 ), in the NPT ensemble at 298 K and 1 atm and with periodic boundary conditions.
- Full pipeline: simulation/modelling [GROMACS v2018.8, NAMD] -> stage not stated [PLUMED v2.2.5]

### Coenzyme Q10 trapping in mitochondrial complex I underlies Leber's hereditary optic neuropathy. (PNAS 2023)

- DOI: 10.1073/pnas.2304884120 | PMCID: PMC10523484 | PMID: 37733737
- Evidence: Methods Simulations were performed in NAMD ( 29 ) with the CHARMM36 force field from July 2020 ( 30 – 36 ).
- Full pipeline: simulation/modelling [NAMD, UCSF Chimera, VMD] -> visualisation [UCSF Chimera, VMD]

### Structures and membrane interactions of native serotonin transporter in complexes with psychostimulants. (PNAS 2023)

- DOI: 10.1073/pnas.2304602120 | PMCID: PMC10629533 | PMID: 37436958
- Evidence: 4 H as line representations) were captured from steered MD simulations using the COLVAR module 98 in NAMD, in which the ligand was pulled away from the extracellular ends TM1b and TM6a (residues 145 to 148 and 361 to 364) to the desired distances using a harmonic potential (k = 10 kcal mol −1 Å −2 ) moving at a 0.5 Å ns −1 rate.
- Full pipeline: alignment/mapping [RELION] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [CTFFIND, MotionCor2, VMD]

### Naturally mutagenic sequence diversity in a human type II topoisomerase. (PNAS 2023)

- DOI: 10.1073/pnas.2302064120 | PMCID: PMC10334734 | PMID: 37406101
- Version used: **2.9**
- Evidence: The preproduction and equilibration runs were performed using NAMD 2.9 ( 48 ) on the Anton2 supercomputer at the Pittsburgh Supercomputing Center (PSC).
- Full pipeline: visualisation [ImageJ] -> stage not stated [NAMD v2.9]

### Discovering selective antiferroptotic inhibitors of the 15LOX/PEBP1 complex noninterfering with biosynthesis of lipid mediators. (PNAS 2023)

- DOI: 10.1073/pnas.2218896120 | PMCID: PMC10288584 | PMID: 37327313
- Evidence: MD simulations of 200 to 550 ns were performed for systems selected from molecular docking ( SI Appendix , Table S2 ) using the NAMD software with the CHARMM force field, and 2 fs time steps.
- Full pipeline: simulation/modelling [NAMD]

### Molecular mechanism of fatty acid activation of FFAR1. (PNAS 2023)

- DOI: 10.1073/pnas.2219569120 | PMCID: PMC10235965 | PMID: 37216523
- Version used: **2.14**
- Evidence: All the MD simulations involved in this study were performed by the GPU version of NAMD 2.14 package ( 55 ) with periodic boundary conditions.
- Full pipeline: normalisation [MotionCor2] -> registration [MotionCor2] -> simulation/modelling [NAMD v2.14] -> structure determination [Coot v0.9.4.1, PHENIX v1.19.2] -> stage not stated [R v3.50, RELION v3.1, UCSF Chimera v1.3]

### Deciphering molecular mechanisms stabilizing the reovirus-binding complex. (PNAS 2023)

- DOI: 10.1073/pnas.2220741120 | PMCID: PMC10214207 | PMID: 37186838
- Evidence: Simulation parameters were obtained from QwikMD ( 51 ), and all molecular dynamics (MD) simulations were conducted employing the NAMD three package ( 25 ).
- Full pipeline: simulation/modelling [NAMD, TrackMate] -> stage not stated [ImageJ v1.52e, VMD]

### Phosphorylation sites are evolutionary checkpoints against liquid-solid transition in protein condensates. (PNAS 2023)

- DOI: 10.1073/pnas.2215828120 | PMCID: PMC10193986 | PMID: 37155880
- Evidence: The simulations were performed using the NAMD ( 38 ) molecular dynamics package (see SI Appendix , Supplementary Appendix I for details of atomistic simulations).
- Full pipeline: simulation/modelling [LAMMPS, NAMD]

### Structures of brain-derived 42-residue amyloid-β fibril polymorphs with unusual molecular conformations and intermolecular interactions. (PNAS 2023)

- DOI: 10.1073/pnas.2218831120 | PMCID: PMC10089215 | PMID: 36893281
- Evidence: MD simulations were performed with NAMD software and analyzed with VMD software ( 38 , 39 ).
- Full pipeline: simulation/modelling [Coot, NAMD, VMD] -> structure determination [Coot, RELION]

### Elucidation of a dynamic interplay between a beta-2 adrenergic receptor, its agonist, and stimulatory G protein. (PNAS 2023)

- DOI: 10.1073/pnas.2215916120 | PMCID: PMC10013855 | PMID: 36853938
- Evidence: The systems were equilibrated for 90 ns with gradually reducing protein restraints in the first 40 ns using Nanoscale Molecular Dynamics (NAMD) ( 80 ).
- Full pipeline: alignment/mapping [UCSF Chimera] -> dimensionality reduction/clustering [SciPy] -> simulation/modelling [NAMD, VMD]

### Dimerization of the Alzheimer's disease pathogenic receptor SORLA regulates its association with retromer. (PNAS 2023)

- DOI: 10.1073/pnas.2212180120 | PMCID: PMC9942828 | PMID: 36652482
- Evidence: Subsequent energy minimization was achieved by NAMD ( 55 ) ( http://www.ks.uiuc.edu/Research/namd/ ) with the Generalized Born Implicit Solvent mode ( 56 , 57 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> stage not stated [AlphaFold, NAMD, PyMOL]

### How acidic amino acid residues facilitate DNA target site selection. (PNAS 2023)

- DOI: 10.1073/pnas.2212501120 | PMCID: PMC9934023 | PMID: 36634135
- Version used: **2.14**
- Evidence: All QM/MM ab initio molecular dynamics (AIMD) simulations of the model system containing a single propionate anion interacting with a fully solvated B-DNA decamer were performed with the NAMD 2.14 molecular dynamics engine ( 69 ) interfaced with the Orca 4.2 quantum chemistry program ( 70 ).
- Full pipeline: simulation/modelling [GROMACS v2018.8, NAMD v2.14]

### Differential dynamics and direct interaction of bound ligands with lipids in multidrug transporter ABCG2. (PNAS 2023)

- DOI: 10.1073/pnas.2213437120 | PMCID: PMC9910490 | PMID: 36580587
- Evidence: In NAMD simulations, a 12 Å cutoff was employed for short-range, nonbonded interactions, with switching starting at 10 Å.
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [CTFFIND, Coot v0.9, MotionCor2, PHENIX, VMD]

### SARS-CoV-2 accessory proteins ORF7a and ORF3a use distinct mechanisms to down-regulate MHC-I surface expression. (PNAS 2023)

- DOI: 10.1073/pnas.2208525120 | PMCID: PMC9910621 | PMID: 36574644
- Evidence: Nanoscale Molecular Dynamics (NAMD) V2.13 software ( 67 ) and CHARMM36 force field ( 68 ) were utilized to perform the MD simulations as described previously ( 69 – 71 ).
- Full pipeline: simulation/modelling [NAMD, VMD] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Constitutive opening of the Kv7.2 pore activation gate causes &lt;i&gt;KCNQ2&lt;/i&gt;-developmental encephalopathy. (PNAS 2024)

- DOI: 10.1073/pnas.2412388121 | PMCID: PMC11626135 | PMID: 39602259
- Evidence: We used the NAMD software ( 65 ) and the CHARMM36 ( 66 – 68 ) force field for proteins and lipids and used an integration time step ∆t = 2 fs.
- Full pipeline: alignment/mapping [UCSF Chimera] -> simulation/modelling [NAMD]

### Structural basis for the synergetic neutralization of hepatitis E virus by antibody-antibody interaction. (PNAS 2024)

- DOI: 10.1073/pnas.2408585121 | PMCID: PMC11626150 | PMID: 39585981
- Evidence: MD simulations were performed using the Nanoscale molecular dynamics (NAMD) version 2.14 MD package ( 38 ) Compiled with Compute unified device architecture (CUDA) support on an InfiniBand-based cluster.
- Full pipeline: dimensionality reduction/clustering [NAMD] -> simulation/modelling [NAMD, VMD v1.9.3] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL]

### Inhibition mechanism of potential antituberculosis compound lansoprazole sulfide. (PNAS 2024)

- DOI: 10.1073/pnas.2412780121 | PMCID: PMC11588064 | PMID: 39531492
- Version used: **2.12**
- Evidence: The MD simulations were propagated using NAMD v.
- Full pipeline: simulation/modelling [NAMD v2.12, VMD] -> structure determination [Coot, PHENIX]

### Dilated cardiomyopathy-associated skeletal muscle actin (ACTA1) mutation R256H disrupts actin structure and function and causes cardiomyocyte hypocontractility. (PNAS 2024)

- DOI: 10.1073/pnas.2405020121 | PMCID: PMC11572969 | PMID: 39503885
- Version used: **3.0**
- Evidence: Each simulation was done five times for 1 µs with G-ACTA1 (PDB 1J6Z) ( 17 ) using NAMD 3.0 alpha and the CHARMM36 forcefield ( 66 , 67 ).
- Full pipeline: simulation/modelling [NAMD v3.0] -> stage not stated [ImageJ, MDAnalysis, PyMOL]

### Atomic view of photosynthetic metabolite permeability pathways and confinement in synthetic carboxysome shells. (PNAS 2024)

- DOI: 10.1073/pnas.2402277121 | PMCID: PMC11551347 | PMID: 39485798
- Version used: **2.14**
- Evidence: After a brief equilibration period utilizing NAMD 2.14 ( 71 ), each simulation was converted using TopoGromacs ( 72 ) to GROMACS ( 73 ) for production simulations, which were 3 replicates for 500 ns each.
- Full pipeline: simulation/modelling [GROMACS, NAMD v2.14, VMD] -> stage not stated [Matplotlib, NumPy, SciPy]

### Relative genotoxicity of polycyclic aromatic hydrocarbons inferred from free energy perturbation approaches. (PNAS 2024)

- DOI: 10.1073/pnas.2322155121 | PMCID: PMC11406254 | PMID: 39226345
- Evidence: The approach described above is implemented utilizing molecular dynamics (MD) simulations in NAMD ( 40 – 42 ) with the CHARMM molecular mechanics force field ( 43 – 45 ).
- Full pipeline: simulation/modelling [NAMD, VMD] -> stage not stated [Python]

### A broad survey of choanoflagellates revises the evolutionary history of the Shaker family of voltage-gated K&lt;sup&gt;+&lt;/sup&gt; channels in animals. (PNAS 2024)

- DOI: 10.1073/pnas.2407461121 | PMCID: PMC11287247 | PMID: 39018191
- Version used: **2.0**
- Evidence: NAMD (v2.0 and v3.0) ( 71 ) was used for MD simulations: Energy minimization was performed first for 10,000 steps, followed by 40 ns of unrestricted simulations.
- Full pipeline: simulation/modelling [NAMD v2.0] -> stage not stated [AlphaFold v2.3.2, BLAST, VMD v1.9.4a]

### POTRA domains of the TamA insertase interact with the outer membrane and modulate membrane properties. (PNAS 2024)

- DOI: 10.1073/pnas.2402543121 | PMCID: PMC11252910 | PMID: 38959031
- Version used: **2.14**
- Evidence: The simulations were performed with the NAMD 2.14 program ( 58 ) using the CHARMM36m force field ( 59 ) and TIP3P waters ( 60 , 61 ).
- Full pipeline: simulation/modelling [NAMD v2.14] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### Ca<sup>2+</sup> permeation through C-terminal cleaved, but not full-length human Pannexin1 hemichannels, mediates cell death. (PNAS 2024)

- DOI: 10.1073/pnas.2405468121 | PMCID: PMC11194574 | PMID: 38861601
- Evidence: Both simulations were performed with NAMD ( 70 ) and the CHARMM ( 71 ) force field.
- Full pipeline: simulation/modelling [NAMD, VMD] -> stage not stated [ImageJ v1.64r]

### Hydrogen bonding heterogeneity correlates with protein folding transition state passage time as revealed by data sonification. (PNAS 2024)

- DOI: 10.1073/pnas.2319094121 | PMCID: PMC11145292 | PMID: 38768341
- Evidence: To examine water–hydrogen bonding, we simulated 200 ps of hydrogen bond dynamics using NAMD ( 44 ), sampled every 200 fs, at the midpoints of the 11 categories selected in Results ( SI Appendix , Table S10 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [VMD]

### Identification and characterization of a nonbiological small-molecular mimic of a Zika virus conformational neutralizing epitope. (PNAS 2024)

- DOI: 10.1073/pnas.2312755121 | PMCID: PMC11127016 | PMID: 38743628
- Version used: **2.13**
- Evidence: The final structures from the MD simulations were used as a starting point for metadynamics calculations using Plumed version 2.0.1 ( 39 ) within NAMD version 2.13 ( 40 ).
- Full pipeline: simulation/modelling [NAMD v2.13]

### Identification of the potassium-binding site in serotonin transporter. (PNAS 2024)

- DOI: 10.1073/pnas.2319384121 | PMCID: PMC11067047 | PMID: 38652746
- Version used: **2.13**
- Evidence: The fully atomistic simulations were run with NAMD v2.13 or v3.0a9 using the CHARMM36m force field ( 52 ) with TIP3P waters ( 53 ).
- Full pipeline: simulation/modelling [GROMACS v2018.8, NAMD v2.13] -> stage not stated [Coot v0.8.9.3, VMD v1.9.3]

### Peptide-based allosteric inhibitor targets TNFR1 conformationally active region and disables receptor-ligand signaling complex. (PNAS 2024)

- DOI: 10.1073/pnas.2308132121 | PMCID: PMC10998571 | PMID: 38551841
- Evidence: The atomistic MD simulations were performed with the NAMD software using the CHARMM36 force field.
- Full pipeline: simulation/modelling [NAMD]

### Lipid shape and packing are key for optimal design of pH-sensitive mRNA lipid nanoparticles. (PNAS 2024)

- DOI: 10.1073/pnas.2311700120 | PMCID: PMC10786277 | PMID: 38175863
- Version used: **2.12**
- Evidence: All molecular dynamics simulations were carried out using NAMD 2.12 ( 24 , 42 , 43 ).
- Full pipeline: simulation/modelling [Jupyter, NAMD v2.12] -> stage not stated [VMD]

### Dissociation kinetics of G proteins from G protein-coupled receptors and effects of allosteric modulation. (PNAS 2025)

- DOI: 10.1073/pnas.2512423122 | PMCID: PMC12646235 | PMID: 41231956
- Evidence: The output files of cMD simulations using NAMD were converted to AMBER format using the ParmEd tool AMBER package.
- Full pipeline: simulation/modelling [NAMD]

### Structural basis of the inhibition of TRPV1 by analgesic sesquiterpenes. (PNAS 2025)

- DOI: 10.1073/pnas.2506560122 | PMCID: PMC12305030 | PMID: 40663614
- Version used: **2.14**
- Evidence: All MD simulations (~320,800 atoms) were executed using NAMD 2.14 ( 84 ) with the CHARMM36 force field ( 85 ).
- Full pipeline: simulation/modelling [NAMD v2.14] -> structure determination [PHENIX, Topaz] -> visualisation [ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [Coot]

### Structure-based discovery of positive allosteric modulators of the A&lt;sub&gt;1&lt;/sub&gt; adenosine receptor. (PNAS 2025)

- DOI: 10.1073/pnas.2421687122 | PMCID: PMC12280925 | PMID: 40623180
- Evidence: MD simulations of the A 1 R were performed in NAMD whereas simulations of the P2Y 1 and FFA 1 receptors were performed in GROMACS ( 20 , 21 ).
- Full pipeline: dimensionality reduction/clustering [RDKit] -> simulation/modelling [GROMACS, NAMD]

### Molecular insights into human phosphatidylserine synthase 2 and its regulation of SREBP pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2501177122 | PMCID: PMC12107096 | PMID: 40372437
- Evidence: Subsequent equilibration and production simulations were carried out with NAMD ( 36 ) using the all-atom CHARMM36 parameter set for the protein and lipid molecules ( 35 ) and the TIP3P model for water molecules ( 34 ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [NAMD, VMD] -> structure determination [AlphaFold, PHENIX] -> visualisation [ChimeraX, PyMOL]

### Unveiling Cas8 dynamics and regulation within a transposon-encoded Cascade-TniQ complex. (PNAS 2025)

- DOI: 10.1073/pnas.2422895122 | PMCID: PMC12002280 | PMID: 40172964
- Version used: **2.14**
- Evidence: MDFF simulations were performed using NAMD 2.14 ( 39 ).
- Full pipeline: simulation/modelling [NAMD v2.14] -> stage not stated [AlphaFold]

### Allosteric mechanism in the distinctive coupling of G&lt;sub&gt;q&lt;/sub&gt; and G&lt;sub&gt;s&lt;/sub&gt; to the parathyroid hormone type 1 receptor. (PNAS 2025)

- DOI: 10.1073/pnas.2426178122 | PMCID: PMC12002267 | PMID: 40138341
- Evidence: All-atom MD systems with explicit membrane were set up using GHARMM-GUI membrane builder ( 14 ), and simulations were performed using NAMD ( 15 ) with the CHARMM36m force field ( 16 ) for proteins and the CHARMM36 lipid ( 17 ) for POPC, and the TIP3P water model ( 18 ).
- Full pipeline: simulation/modelling [NAMD] -> visualisation [PyMOL] -> stage not stated [VMD v1.9.4]

### Accelerated peptide bond formation at air-water interfaces. (PNAS 2025)

- DOI: 10.1073/pnas.2501323122 | PMCID: PMC11962484 | PMID: 40117307
- Evidence: The free energy profiles of glycine and diglycine molecules crossing the air–water interface into bulk water were obtained using classical MD simulations coupled with the Adaptive Biasing Force method using the NAMD software package ( 44 , 45 ).
- Full pipeline: simulation/modelling [NAMD]

### Design of a light and Ca<sup>2+</sup> switchable organic-peptide hybrid. (PNAS 2025)

- DOI: 10.1073/pnas.2411316122 | PMCID: PMC11804555 | PMID: 39883844
- Evidence: The equilibrium MD simulations were performed with NAMD package with CHARMM36 force field ( 64 ) to observe the structural stability of design candidates.
- Full pipeline: simulation/modelling [NAMD]

### Enzymes in a human cytoplasm model organize into submetabolon complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2414206122 | PMCID: PMC11804712 | PMID: 39874290
- Evidence: Prior to simulations done on Anton 2 under different sticky parameterization conditions as described in the main text, the molecular dynamics software NAMD ( 69 ) (both versions 2.9 and 3.0 Alpha) was used for initial minimization and pre-equilibration/equilibration steps of the cytoplasm model.
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [MDAnalysis, VMD]

### Mutational analysis of an antimalarial drug target, <i>Pf</i>ATP4. (PNAS 2025)

- DOI: 10.1073/pnas.2403689122 | PMCID: PMC11745376 | PMID: 39773028
- Evidence: The models were equilibrated with all-atom MD simulations in a membrane environment using NAMD software ( 41 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> simulation/modelling [NAMD] -> machine learning [AlphaFold]

### Molecular basis of Spns1-mediated lysophospholipid transport from the lysosome. (PNAS 2025)

- DOI: 10.1073/pnas.2409596121 | PMCID: PMC11725778 | PMID: 39739806
- Evidence: Energy minimizations and geometry optimizations were carried out with NAMD ( 57 ) using the all-atom CHARMM36 parameter set for the protein and lipid molecules ( 58 ) and the TIP3P model for water molecules ( 56 ).
- Full pipeline: registration [MotionCor2, RELION v3.1] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, NAMD]

### D614G reshapes allosteric networks and opening mechanisms of SARS-CoV-2 spikes. (PNAS 2026)

- DOI: 10.1073/pnas.2504793123 | PMCID: PMC13168548 | PMID: 42101997
- Evidence: A tar ball containing selected WE simulation trajectories (psf/pdb/dcd), along with input scripts (Amber and NAMD) and MDAnalysis scripts (py), is available for download on the Amaro Lab website ( https://amarolab.ucsd.edu/data.php#covid19 ) ( 85 ) with the following name: D614G_for_sharing_amarolab.tar.gz.
- Full pipeline: simulation/modelling [MDAnalysis, NAMD]

