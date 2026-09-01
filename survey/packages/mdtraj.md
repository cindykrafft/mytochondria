# MDTraj

- **Category:** md
- **Papers in survey:** 18
- **Journals:** PNAS (9), Nature (7), Science (1), Cell (1)
- **Years:** 2021 (1), 2022 (3), 2023 (2), 2024 (7), 2025 (5)
- **Versions named:** 1.9.8 (1)
- **Pipeline stages it appears in:** simulation/modelling (10), dimensionality reduction/clustering (1), visualisation (1), differential/statistical testing (1)

## Papers

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ...18 Version 1.0.1 ChimeraX Pettersen et al., 2021 Version 1.0 AmberTools Case et al., 2017 Version 17.0 pdb-tools Rodrigues et al., 2018 Version 2.0.5 MDTraj McGibbon et al., 2015 Version 1.9.4 Pandas https://conference.scipy.org/proceedings/scipy2010/pdfs/mckinney.pdf Version 1.0.5 Custom code, molecular dynamics set up and processing This paper https://github.com/choderalab/rbd-ace2-contact-analy...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### Architecture and self-assembly of the jumbo bacteriophage nuclear shell. (Nature 2022)

- DOI: 10.1038/s41586-022-05013-4 | PMCID: PMC9365700 | PMID: 35922510
- Evidence: The resulting molecular dynamics trajectories were analysed through CPPTRAJ-v.25.6 86 and MDTraj-v1.9.4 87 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [ChimeraX, MDTraj, PyMOL, VMD] -> structure determination [ChimeraX, PHENIX, PyMOL, VMD] -> visualisation [ChimeraX, PyMOL, VMD] -> stage not stated [UCSF Chimera]

### Class B1 GPCR activation by an intracellular agonist. (Nature 2023)

- DOI: 10.1038/s41586-023-06169-3 | PMCID: PMC10307627 | PMID: 37286611
- Version used: **1.9.8**
- Evidence: The simulation results were analysed and visualized using mdtraj (v.1.9.8) 51 , seaborn ( https://zenodo.org/record/54844 ) and CUEMOL (v.2.2.3.443) ( http://www.cuemol.org ).
- Full pipeline: registration [RELION] -> simulation/modelling [MDTraj v1.9.8, NAMD v2.13, seaborn] -> visualisation [MDTraj v1.9.8, seaborn] -> stage not stated [Fiji, ImageJ, VMD v1.9.3]

### Ab initio characterization of protein molecular dynamics with AI&lt;sup&gt;2&lt;/sup&gt;BMD. (Nature 2024)

- DOI: 10.1038/s41586-024-08127-z | PMCID: PMC11602711 | PMID: 39506110
- Evidence: The RMSD values were calculated on the basis of Cα coordinates according to the ‘rmsd’ method in MDTraj. Δ G , the free energy for the folding process, was calculated according to the ratio between the folded and unfolded structures.
- Full pipeline: simulation/modelling [GROMACS, Python] -> stage not stated [Docker, MDTraj]

### The ribosome lowers the entropic penalty of protein folding. (Nature 2024)

- DOI: 10.1038/s41586-024-07784-4 | PMCID: PMC11374706 | PMID: 39112704
- Evidence: ...ly, and σ q is the experimental error: S22 χ r 2 = 1 n ∑ q n ( I q calc − I q exp ) 2 σ q 2 Structural analysis The Python package MDAnalysis 122 and MDTraj 128 were used for general analysis of the ensembles involving atomic coordinates.
- Full pipeline: simulation/modelling [GROMACS, PyMOL v2.3] -> structure determination [Python] -> stage not stated [ImageJ, MDAnalysis, MDTraj, SciPy]

### Structural snapshots capture nucleotide release at the μ-opioid receptor. (Nature 2025)

- DOI: 10.1038/s41586-025-09677-6 | PMCID: PMC12711574 | PMID: 41193810
- Evidence: MD trajectory analysis was carried out using the GROMACS analysis toolkit, the MDTraj software package 74 and MDCiao 75 .
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2024.5, MDTraj] -> structure determination [UCSF Chimera v1.17.3] -> stage not stated [ChimeraX v1.9, PyMOL v3.1.6.1]

### Complete computational design of high-efficiency Kemp elimination enzymes. (Nature 2025)

- DOI: 10.1038/s41586-025-09136-2 | PMCID: PMC12310539 | PMID: 40533551
- Evidence: The MDTraj software (version 1.10.0) 85 was applied to convert the trajectories to a CPPTRAJ compatible format, and clustering was performed based on the r.m.s.d. of the substrate heavy atoms, using the average linkage clustering method, with an ε value of 0.75.
- Full pipeline: dimensionality reduction/clustering [MDTraj] -> simulation/modelling [MDTraj] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ColabFold, PyMOL, VMD]

### Mis-splicing of a neuronal microexon promotes CPEB4 aggregation in ASD. (Nature 2025)

- DOI: 10.1038/s41586-024-08289-w | PMCID: PMC11711090 | PMID: 39633052
- Evidence: Simulation trajectories were analysed using MDTraj 70 (v.1.9.6) and MDAnalysis 71 , 72 (v.1.1).
- Full pipeline: simulation/modelling [MDAnalysis, MDTraj, OpenMM v7.5] -> visualisation [Fiji, ImageJ] -> stage not stated [VMD]

### Intrinsically disordered ectodomain modulates ion permeation through a metal transporter. (PNAS 2022)

- DOI: 10.1073/pnas.2214602119 | PMCID: PMC9889885 | PMID: 36409899
- Evidence: Python packages MDTraj and MDAnalysis were used for trajectory analysis ( 49 , 50 ).
- Full pipeline: simulation/modelling [MDAnalysis, MDTraj] -> stage not stated [GROMACS, PLUMED v2.6.3, VMD]

### Structure and dynamics of SARS-CoV-2 proofreading exoribonuclease ExoN. (PNAS 2022)

- DOI: 10.1073/pnas.2106379119 | PMCID: PMC8892293 | PMID: 35165203
- Evidence: MDTraj ( 50 ) was used for some of the MD trajectory analysis.
- Full pipeline: simulation/modelling [MDTraj] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Sequence complexity and monomer rigidity control the morphologies and aging dynamics of protein aggregates. (PNAS 2024)

- DOI: 10.1073/pnas.2409973121 | PMCID: PMC11648916 | PMID: 39642206
- Evidence: We computed the nematic order parameter ( 79 ) using python library MDTraj ( 80 ).
- Full pipeline: simulation/modelling [OpenMM] -> stage not stated [MDTraj]

### Adaptive CVgen: Leveraging reinforcement learning for advanced sampling in protein folding and chemical reactions. (PNAS 2024)

- DOI: 10.1073/pnas.2414205121 | PMCID: PMC11551409 | PMID: 39475640
- Evidence: The calculation of RMSD and the analysis of secondary structures were conducted using the MDTraj program ( 52 ).
- Full pipeline: dimensionality reduction/clustering [PyMOL, scikit-learn] -> simulation/modelling [OpenMM] -> visualisation [Matplotlib, PyMOL] -> stage not stated [AlphaFold, MDTraj]

### An α-ketoglutarate conformational switch controls iron accessibility, activation, and substrate selection of the human FTO protein. (PNAS 2024)

- DOI: 10.1073/pnas.2404457121 | PMCID: PMC11194561 | PMID: 38865275
- Evidence: The surface of the Fe(II) atom accessible to O 2 was calculated with the Shrake-Rupley algorithm in MDTraj ( 57 ) using a probe radius of 1.52 Å corresponding to the radius of the O 2 molecule.
- Full pipeline: simulation/modelling [MDAnalysis, OpenMM] -> stage not stated [MDTraj]

### On the role of native contact cooperativity in protein folding. (PNAS 2024)

- DOI: 10.1073/pnas.2319249121 | PMCID: PMC11145220 | PMID: 38776371
- Evidence: We computed the total number of contacts C from PDB structures of each of the proteins in this list using mdtraj ( 54 ), from which linear regression using scipy ( 55 ) gave a relation to the number of residues in each protein, L , as [13] C = 2.534 L − 38.54 .
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> differential/statistical testing [MDTraj, SciPy]

### Homologous mutations in human β, embryonic, and perinatal muscle myosins have divergent effects on molecular power generation. (PNAS 2024)

- DOI: 10.1073/pnas.2315472121 | PMCID: PMC10907259 | PMID: 38377203
- Evidence: Trajectory analysis was conducted in Python using the library MDTraj ( 89 ).
- Full pipeline: simulation/modelling [GROMACS v2022.4, MDTraj, Python] -> stage not stated [scikit-learn]

### Small siphophage binding to an open state of the LptDE outer membrane lipopolysaccharide translocon. (PNAS 2025)

- DOI: 10.1073/pnas.2516650122 | PMCID: PMC12685063 | PMID: 41296721
- Evidence: The DSSP algorithm ( 67 ) was used to analyze secondary structure, implemented through MDTraj ( 68 ).
- Full pipeline: alignment/mapping [PyMOL] -> quantification [ImageJ] -> simulation/modelling [GROMACS] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [Coot, MDAnalysis, MDTraj]

### STIM1 transmembrane helix dimerization captured by AI-guided transition path sampling. (PNAS 2025)

- DOI: 10.1073/pnas.2506516122 | PMCID: PMC12415195 | PMID: 40857319
- Evidence: Trajectory analysis was carried out using the pytraj ( 96 ), mdtraj ( 97 ), MDAnalysis ( 98 , 99 ), numpy ( 100 ), and SciPy ( 101 ) packages.
- Full pipeline: normalisation [PyTorch] -> simulation/modelling [GROMACS v2020.6, MDAnalysis, MDTraj, NumPy, SciPy] -> machine learning [PyTorch]

### Molecular determinants of ligand efficacy and potency in GPCR signaling. (Science 2023)

- DOI: 10.1126/science.adh1859 | PMCID: PMC7615523 | PMID: 38127743
- Evidence: In addition, we calculated the accessible surface area of the adrenaline binding site with and without the ligand present using MDTraj ( https://www.mdtraj.org ) and GROMACS ( https://www.gromacs.org/ ).
- Full pipeline: stage not stated [GROMACS, MDTraj, PyMOL v2.5.2, R v4.0, ggplot2, ggpubr, tidyverse]

