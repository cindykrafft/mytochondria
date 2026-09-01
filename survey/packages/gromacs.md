# GROMACS

- **Category:** md
- **Papers in survey:** 249
- **Journals:** PNAS (197), Nature (45), Cell (5), Science (2)
- **Years:** 2021 (28), 2022 (38), 2023 (44), 2024 (59), 2025 (64), 2026 (16)
- **Versions named:** 2021.5 (8), 2020.1 (6), 2021.3 (5), 2018.8 (5), 5.1.4 (5), 2020.6 (4), 2022.5 (4), 2019.4 (4), 2019.3 (4), 2021.4 (4)
- **Pipeline stages it appears in:** simulation/modelling (214), normalisation (2), dimensionality reduction/clustering (2), structure determination (1), machine learning (1), visualisation (1)

## Papers

### Bacterial Vipp1 and PspA are members of the ancient ESCRT-III membrane-remodeling superfamily. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.041 | PMCID: PMC8281802 | PMID: 34166615
- Evidence: SMOG2 ( Noel et al., 2016 ) with the template “ENM” was used to create topology files for the MD software GROMACS ( Abraham et al., 2015 ) using the Vipp1 C11 PDB structure as input (PDB: 6ZVR ).
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE, MotionCor2] -> stage not stated [GROMACS, HMMER, ImageJ, PHENIX, RELION v3.1, VMD]

### Antidepressant drugs act by directly binding to TRKB neurotrophin receptors. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.034 | PMCID: PMC7938888 | PMID: 33606976
- Evidence: ...Kaisa Haapasalo TRKB.T1 Plasmid to express FLAG-tagged TM domain of truncated TRKB (TRKB.T1) Anna-Kaisa Haapasalo TRKB.T1.ΔEC Software and algorithms GROMACS ( https://linkinghub.elsevier.com/retrieve/pii/S2352711015000059 ) https://github.com/ElsevierSoftwareX/SOFTX-D-15-00003 GROMACS Graphpad Prism v6.01 https://www.graphpad.com/ Graphpad Prism JASP https://jasp-stats.org/ JASP Resource availabi...
- Full pipeline: stage not stated [GROMACS, ImageJ]

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Evidence: AceDRG Long et al., 2017 https://doi.org/10.1107/S2059798317000067 MODELLER Webb and Sali, 2016 https://doi.org/10.1002/cpbi.3 GROMACS 2020 Abraham et al., 2015 https://doi.org/10.1016/j.softx.2015.06.001 AMBER14SB force field Maier et al., 2015 https://doi.org/10.1021/acs.jctc.5b00255 MDAnalysis Michaud-Agrawal et al., 2011 https://doi.org/10.1002/jcc.21787 Alpha Fold Jumper et al., 2021 ; Varadi...
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### Structure of a fully assembled tumor-specific T cell receptor ligated by pMHC. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.010 | PMCID: PMC9630439 | PMID: 35985289
- Version used: **2020.6**
- Evidence: ... charmm-gui.org COOT Emsley and Cowtan, 2004 RRID:SCR_014222 cryoSPARC Punjani et al., 2017 RRID:SCR_016501 Flowjo v10.7.1 N/A https://www.flowjo.com Gromacs v2020.6 Abraham et al., 2015 RRID: SCR_014565 Illustrate Goodsell et al., 2019 github.com/ccsb-scripps/Illustrate MDAnalysis v0.20.1 Gowers et al., 2016 github.com/MDAnalysis/mdanalysis/releases NumPy v1.19.5 Harris et al., 2020 RRID: SCR_008...
- Full pipeline: simulation/modelling [ChimeraX, UCSF Chimera, VMD] -> stage not stated [CCP4, GROMACS v2020.6, MDAnalysis v0.20.1, NumPy v1.19.5, PHENIX, PyMOL]

### Structural basis of human ACE2 higher binding affinity to currently circulating Omicron SARS-CoV-2 sub-variants BA.2 and BA.1.1. (Cell 2022)

- DOI: 10.1016/j.cell.2022.06.023 | PMCID: PMC9212699 | PMID: 35809570
- Evidence: .../peemsley/coot/ Phenix ( Adams et al., 2010 ) http://www.phenix-online.org/ MolProbity Duke Biochemistry http://molprobity.biochem.duke.edu/index.php GROMACS ( Abraham et al., 2015 ) http://www.gromacs.org/ Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulfilled by the Lead Contact, George F.
- Full pipeline: stage not stated [GROMACS, PHENIX, PyMOL]

### Structure of the class D GPCR Ste2 dimer coupled to two G proteins. (Nature 2021)

- DOI: 10.1038/s41586-020-2994-1 | PMCID: PMC7116888 | PMID: 33268889
- Evidence: The modelled full dimer complex was energy minimized using GROMACS package 62 with CHARMM36m 63 force field, with restraints of 5 kcal/mol-Å 2 applied on all backbone heavy atoms during the minimization process.
- Full pipeline: alignment/mapping [CCP4] -> registration [MotionCor2] -> simulation/modelling [GROMACS] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [RELION]

### Structures of the TMC-1 complex illuminate mechanosensory transduction. (Nature 2022)

- DOI: 10.1038/s41586-022-05314-8 | PMCID: PMC9605866 | PMID: 36224384
- Evidence: Coarse-grained simulation protocol CG systems were simulated using GROMACS 74 , with the standard Martini v2.2 simulation parameters 66 .
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [ChimeraX, PHENIX] -> stage not stated [NAMD, UCSF Chimera, VMD]

### Structural basis for directional chitin biosynthesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05244-5 | PMCID: PMC9556331 | PMID: 36131020
- Version used: **2019.3**
- Evidence: Molecular dynamics simulation The molecular dynamics software package GROMACS v2019.3 was used with the Gromos53a5 force field to compare the structural properties obtained from computational simulation with the structural properties determined from experiments 52 .
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2019.3] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, RELION v3.08]

### Teixobactin kills bacteria by a two-pronged attack on the cell envelope. (Nature 2022)

- DOI: 10.1038/s41586-022-05019-y | PMCID: PMC9365693 | PMID: 35922513
- Version used: **4.6.3**
- Evidence: Molecular dynamics simulations Molecular dynamics calculations were performed with GROMACS, version 4.6.3 using the g54a7 forcefield 59 .
- Full pipeline: simulation/modelling [GROMACS v4.6.3] -> stage not stated [ImageJ]

### BA.2.12.1, BA.4 and BA.5 escape antibodies elicited by Omicron infection. (Nature 2022)

- DOI: 10.1038/s41586-022-04980-y | PMCID: PMC9385493 | PMID: 35714668
- Evidence: After that, the structures were simulated with GROMACS-2021 59 .
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> simulation/modelling [GROMACS] -> structure determination [PHENIX v1.20, RELION v3.1, UCSF Chimera v1.16] -> visualisation [ChimeraX v1.3, R, Seurat] -> stage not stated [Pangolin, ggplot2 v3.3.3, scikit-learn]

### Activation mechanism of the class D fungal GPCR dimer Ste2. (Nature 2022)

- DOI: 10.1038/s41586-022-04498-3 | PMCID: PMC8942848 | PMID: 35296853
- Evidence: Molecular dynamics simulations All-atom molecular dynamics simulations were performed using the CHARMM36m forcefield 62 and GROMACS MD package.
- Full pipeline: registration [MotionCor2] -> differential/statistical testing [RELION] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, MotionCor2, PHENIX, RELION] -> visualisation [PyMOL] -> stage not stated [CTFFIND, UCSF Chimera]

### Altered TMPRSS2 usage by SARS-CoV-2 Omicron impacts infectivity and fusogenicity. (Nature 2022)

- DOI: 10.1038/s41586-022-04474-x | PMCID: PMC8942856 | PMID: 35104837
- Evidence: Further processing of steps involving minimization and peptide bond building (after deletions for B.1.617.2 and B.1.529 spike) were performed using the Gromacs.
- Full pipeline: read trimming [Bowtie2 v2.3.4.3] -> alignment/mapping [Bowtie2 v2.3.4.3] -> dimensionality reduction/clustering [Fiji] -> visualisation [ChimeraX v1.3] -> stage not stated [GROMACS, ImageJ, Pangolin, Scanpy v1.7.1]

### Memory B cell repertoire from triple vaccinees against diverse SARS-CoV-2 variants. (Nature 2022)

- DOI: 10.1038/s41586-022-04466-x | PMCID: PMC8967717 | PMID: 35090164
- Evidence: After that, the structure was simulated by GROMACS-2021.
- Full pipeline: registration [RELION v3.0] -> simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND]

### Broadly neutralizing antibodies target a haemagglutinin anchor epitope. (Nature 2022)

- DOI: 10.1038/s41586-021-04356-8 | PMCID: PMC8828479 | PMID: 34942633
- Evidence: Metadynamics simulations To enhance the sampling of the conformational space, well-tempered bias-exchange metadynamics 85 – 87 simulations were performed in GROMACS 88 , 89 with the PLUMED 2 implementation 90 .
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION, UCSF Chimera] -> simulation/modelling [GROMACS, PLUMED] -> visualisation [RELION] -> stage not stated [Jupyter, PHENIX, R, Seurat]

### PLSCR1 is a cell-autonomous defence factor against SARS-CoV-2 infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06322-y | PMCID: PMC10371867 | PMID: 37438530
- Version used: **2021.3**
- Evidence: Simulations were run using GROMACS v.2021.3 (ref.
- Full pipeline: alignment/mapping [featureCounts] -> differential/statistical testing [DESeq2, R] -> simulation/modelling [AlphaFold, GROMACS v2021.3, Python] -> stage not stated [PyMOL, VMD]

### Femtosecond proton transfer in urea solutions probed by X-ray spectroscopy. (Nature 2023)

- DOI: 10.1038/s41586-023-06182-6 | PMCID: PMC10371863 | PMID: 37380782
- Version used: **2018.8**
- Evidence: To sample the possible configuration structures in the liquid phase, we first performed force-field molecular-dynamics calculations for a 10 M and a 5 M aqueous urea solution using Gromacs (v.2018.8) 38 using the GROMOS 54A7 force field 39 .
- Full pipeline: simulation/modelling [GROMACS v2018.8]

### Entropic repulsion of cholesterol-containing layers counteracts bioadhesion. (Nature 2023)

- DOI: 10.1038/s41586-023-06033-4 | PMCID: PMC10284698 | PMID: 37344647
- Version used: **2019.4**
- Evidence: The system was energy minimized and equilibration simulations for both cholesterol- and stigmasterol-containing systems were conducted using Gromacs 2019.4 (for details see Supplementary Note 4 ) 46 , 47 .
- Full pipeline: simulation/modelling [GROMACS v2019.4]

### Structural basis for FGF hormone signalling. (Nature 2023)

- DOI: 10.1038/s41586-023-06155-9 | PMCID: PMC10284700 | PMID: 37286607
- Evidence: A 300 ns all-atom MD simulation trajectory was generated using GROMACS 2021 (ref.
- Full pipeline: differential/statistical testing [ImageJ] -> simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX]

### Structural basis of NINJ1-mediated plasma membrane rupture in cell death. (Nature 2023)

- DOI: 10.1038/s41586-023-05991-z | PMCID: PMC10307626 | PMID: 37198476
- Evidence: All simulations were performed at room temperature (293 K) using GROMACS 2020 or 2021 63 , 64 .
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, ChimeraX, Python]

### Ligand and G-protein selectivity in the κ-opioid receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06030-7 | PMCID: PMC10172140 | PMID: 37138078
- Evidence: Molecular dynamics simulations The Gromacs simulation engine (v.2020.3) 68 was used to run all molecular dynamics simulations under the Charmm36 force-field topologies and parameters 69 , 70 .
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL]

### The electron-proton bottleneck of photosynthetic oxygen evolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06008-5 | PMCID: PMC10191853 | PMID: 37138082
- Evidence: Molecular dynamics simulations were performed using the GROMACS software package 79 .
- Full pipeline: simulation/modelling [GROMACS]

### Visualizing the disordered nuclear transport machinery in situ. (Nature 2023)

- DOI: 10.1038/s41586-023-05990-0 | PMCID: PMC10156602 | PMID: 37100914
- Version used: **2020.6**
- Evidence: The Martini MD simulations were performed with GROMACS 2020.6 (refs.
- Full pipeline: simulation/modelling [GROMACS v2020.6, LAMMPS] -> visualisation [VMD] -> stage not stated [AlphaFold]

### Structural basis of mitochondrial membrane bending by the I-II-III&lt;sub&gt;2&lt;/sub&gt;-IV&lt;sub&gt;2&lt;/sub&gt; supercomplex. (Nature 2023)

- DOI: 10.1038/s41586-023-05817-y | PMCID: PMC10060162 | PMID: 36949187
- Evidence: The simulations were performed using the Gromacs software (version 2021) 55 .
- Full pipeline: registration [IMOD, RELION] -> simulation/modelling [ChimeraX, GROMACS] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Structural basis for bacterial energy extraction from atmospheric hydrogen. (Nature 2023)

- DOI: 10.1038/s41586-023-05781-7 | PMCID: PMC10017518 | PMID: 36890228
- Version used: **2021.3**
- Evidence: Molecular dynamics simulations were performed with the GROMACS v 2021.3 simulations suite.
- Full pipeline: simulation/modelling [GROMACS v2021.3] -> structure determination [ChimeraX v1.3, PHENIX] -> visualisation [AlphaFold, VMD] -> stage not stated [CTFFIND v4.1.8, Coot, RELION v3.1.2]

### Autoregulation of GPCR signalling through the third intracellular loop. (Nature 2023)

- DOI: 10.1038/s41586-023-05789-z | PMCID: PMC10033409 | PMID: 36890236
- Evidence: Starting from the last frame of the equilibration protocol, we performed 400 ns all-atom molecular dynamics simulation runs with NPT ensemble at 310 K with 2 fs time step using GROMACS with CHARMM36mFF 55 .
- Full pipeline: simulation/modelling [GROMACS] -> visualisation [ggplot2] -> stage not stated [VMD v1.9.3]

### Ab initio characterization of protein molecular dynamics with AI&lt;sup&gt;2&lt;/sup&gt;BMD. (Nature 2024)

- DOI: 10.1038/s41586-024-08127-z | PMCID: PMC11602711 | PMID: 39506110
- Evidence: For barnase, 20 parallel simulations starting from the folded structure and 20 simulations starting from the unfolded structures were performed by GROMACS 2018 with the CHARMM36 force field at pH 4.1 and at temperatures of 295 K, 315 K and 335 K.
- Full pipeline: simulation/modelling [GROMACS, Python] -> stage not stated [Docker, MDTraj]

### The ribosome lowers the entropic penalty of protein folding. (Nature 2024)

- DOI: 10.1038/s41586-024-07784-4 | PMCID: PMC11374706 | PMID: 39112704
- Evidence: GROMACS (version 2021) 84 was used for all all-atom molecular dynamics simulations in explicit solvent.
- Full pipeline: simulation/modelling [GROMACS, PyMOL v2.3] -> structure determination [Python] -> stage not stated [ImageJ, MDAnalysis, MDTraj, SciPy]

### Cryo-EM architecture of a near-native stretch-sensitive membrane microdomain. (Nature 2024)

- DOI: 10.1038/s41586-024-07720-6 | PMCID: PMC11324527 | PMID: 39048819
- Version used: **2021.5**
- Evidence: The simulations were performed using GROMACS v.2021.5 66 and the Martini3 force field 72 , 73 .
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.8.9.2, PHENIX v1.20] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, Cellpose v2.0, RELION v2.1.0, VMD v1.9]

### Glutamate acts on acid-sensing ion channels to worsen ischaemic brain injury. (Nature 2024)

- DOI: 10.1038/s41586-024-07684-7 | PMCID: PMC11269185 | PMID: 38987597
- Version used: **2020.3**
- Evidence: All simulations used the program GROMACS 2020.3.
- Full pipeline: simulation/modelling [GROMACS v2020.3]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Version used: **2022.4**
- Evidence: Molecular dynamics simulations All molecular dynamics simulations were performed using the GROMACS 2022.4 (ref.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### Emergence of fractal geometries in the evolution of a metabolic enzyme. (Nature 2024)

- DOI: 10.1038/s41586-024-07287-2 | PMCID: PMC11041685 | PMID: 38600380
- Version used: **2022.2**
- Evidence: Calculation of R g values Calculation of R g values was done using gmx gyrate from the GROMACS 2022.2 simulation package 72 from the atomic models of the 6mer, 18mer and the 54mer.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MotionCor2] -> normalisation [RELION v3.1] -> simulation/modelling [GROMACS v2022.2] -> structure determination [MUSCLE v3.8.31, PHENIX v1.19.2] -> stage not stated [PyMOL v2.5.2, Topaz, UCSF Chimera]

### Designer phospholipid capping ligands for soft metal halide nanocrystals. (Nature 2024)

- DOI: 10.1038/s41586-023-06932-6 | PMCID: PMC10866715 | PMID: 38109940
- Evidence: All reported simulations were performed using GROMACS software package 63 .
- Full pipeline: simulation/modelling [GROMACS]

### Slipknot-gauged mechanical transmission and robotic operation. (Nature 2025)

- DOI: 10.1038/s41586-025-09673-w | PMCID: PMC12657242 | PMID: 41299050
- Evidence: DNA slipknot molecular dynamic simulation Coarse-grained molecular dynamic simulations were performed using the program Gromacs with the Martini 2 force field for nucleic acids.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [OpenCV]

### A skin-permeable polymer for non-invasive transdermal insulin delivery. (Nature 2025)

- DOI: 10.1038/s41586-025-09729-x | PMCID: PMC12695667 | PMID: 41261125
- Version used: **2020.6**
- Evidence: All MD simulations were carried out using the program GROMACS 2020.6 50 , 51 .
- Full pipeline: simulation/modelling [GROMACS v2020.6, VMD] -> visualisation [VMD] -> stage not stated [ImageJ]

### A molecularly impermeable polymer from two-dimensional polyaramids. (Nature 2025)

- DOI: 10.1038/s41586-025-09674-9 | PMCID: PMC12611783 | PMID: 41224978
- Evidence: Because of the computational cost of DFT, energy minimizations were performed using the Optimized Potentials for Liquid Simulations classical interatomic potential in GROMACS 74 – 76 .
- Full pipeline: simulation/modelling [GROMACS]

### Structural snapshots capture nucleotide release at the μ-opioid receptor. (Nature 2025)

- DOI: 10.1038/s41586-025-09677-6 | PMCID: PMC12711574 | PMID: 41193810
- Version used: **2024.5**
- Evidence: MD simulations For our MD simulation, we deployed GROMACS v.2024.5 (ref.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2024.5, MDTraj] -> structure determination [UCSF Chimera v1.17.3] -> stage not stated [ChimeraX v1.9, PyMOL v3.1.6.1]

### Mechanism of conductance control and neurosteroid binding in NMDA receptors. (Nature 2025)

- DOI: 10.1038/s41586-025-09695-4 | PMCID: PMC12951714 | PMID: 41162707
- Evidence: The free-energy profile was obtained using umbrella sampling combined with the GROMACS weighted histogram analysis method (WHAM).
- Full pipeline: structure determination [ChimeraX v1.4, PHENIX v1.20.1] -> stage not stated [GROMACS]

### Design of facilitated dissociation enables timing of cytokine signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09549-z | PMCID: PMC12611780 | PMID: 40993395
- Version used: **2020.2**
- Evidence: All three steps were performed with the GROMACS 2020.2 MD engine 79 , 80 .
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [CCP4] -> differential/statistical testing [DESeq2] -> simulation/modelling [MDAnalysis] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> stage not stated [GROMACS v2020.2, PyMOL, RoseTTAFold]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Version used: **2022.3**
- Evidence: Four simulations were performed (GROMACS 2022.3; CHARMM36M force field; Supplementary Table 15 ).
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### Structural basis for the dynamic regulation of mTORC1 by amino acids. (Nature 2025)

- DOI: 10.1038/s41586-025-09428-7 | PMCID: PMC12507694 | PMID: 40836086
- Evidence: Molecular dynamics simulations Molecular dynamics simulations were performed using GROMACS (2024-rc) 32 .
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [AlphaFold, ChimeraX v1.8, Coot v0.9.8] -> machine learning [Topaz] -> stage not stated [CTFFIND v4.1.14, MotionCor2, PHENIX v2.0, RELION v5.0]

### Architecture, dynamics and biogenesis of GluA3 AMPA glutamate receptors. (Nature 2025)

- DOI: 10.1038/s41586-025-09325-z | PMCID: PMC12422969 | PMID: 40592473
- Evidence: System preparation and MD simulations for both the full NTD–LBD tri-domain system and an extracted NTD dimer were performed using GROMACS 2023 70 , 71 with the July 2021 release of the CHARMM36m all-atom force field 72 and the standard CHARMM-modified TIP3P water model 73 , 74 on which the CHARMM36m protein force field is based.
- Full pipeline: alignment/mapping [Python] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot v0.9.8.95, PHENIX v1.20, PyMOL v2.5] -> stage not stated [RELION v5.0]

### Observation of plastic ice VII by quasi-elastic neutron scattering. (Nature 2025)

- DOI: 10.1038/s41586-025-08750-4 | PMCID: PMC12003197 | PMID: 39938568
- Version used: **2020.2**
- Evidence: Classical molecular dynamics simulations were performed with the GROMACS v.2020.2 software package 59 .
- Full pipeline: simulation/modelling [GROMACS v2020.2]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Version used: **2022.1**
- Evidence: 16 ), we conducted three replicate molecular dynamics simulations for ISG15 of human, R. sinicus and D. cyclops using GROMACS v.2022.1 (refs.
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Engineered enzymes for enantioselective nucleophilic aromatic substitutions. (Nature 2025)

- DOI: 10.1038/s41586-025-08611-0 | PMCID: PMC11903332 | PMID: 39814071
- Evidence: Molecular dynamics simulations were then carried out using GROMACS 2018 (refs.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [PHENIX] -> stage not stated [AutoDock Vina]

### Structure and mechanism of the Zorya anti-phage defence system. (Nature 2025)

- DOI: 10.1038/s41586-024-08493-8 | PMCID: PMC11946911 | PMID: 39662505
- Version used: **2022.5**
- Evidence: Local conformations were manually adjusted in PyMol 52 (v.2.5) and optimized through energy minimization using GROMACS (v.2022.5) 53 with CHARMM27 force field.
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> dimensionality reduction/clustering [ColabFold v1.5.2, MUSCLE v5.1] -> simulation/modelling [GROMACS v2022.5, PyMOL] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, Python, ilastik]

### Structural basis of fungal β-1,3-glucan synthase inhibition by caspofungin. (Nature 2026)

- DOI: 10.1038/s41586-026-10409-7 | PMCID: PMC13249079 | PMID: 42020744
- Evidence: All simulations were executed in GROMACS 65 with input files generated by CHARMM-GUI.
- Full pipeline: alignment/mapping [UCSF Chimera] -> registration [RELION] -> simulation/modelling [GROMACS, MDAnalysis v2.7.0, Python, VMD v1.9] -> structure determination [Coot v0.98, UCSF Chimera] -> visualisation [MDAnalysis v2.7.0, Python, VMD v1.9] -> stage not stated [AlphaFold, ChimeraX v1.10, PHENIX v1.20, PyMOL v3.1]

### CLCC1 promotes hepatic neutral lipid flux and nuclear pore complex assembly. (Nature 2026)

- DOI: 10.1038/s41586-025-10064-4 | PMCID: PMC13061601 | PMID: 41741636
- Version used: **2023.3**
- Evidence: General molecular dynamics simulation details Simulations were performed with Gromacs (v.2023.3 40 ) using the molecular dynamics integrator (unless stated otherwise), and the Martini 3 force field (v.3.0.0 48 ) at a 20 fs time step.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3] -> quantification [Fiji v1.53e, ImageJ v1.53e, Python v3.0] -> simulation/modelling [ColabFold, GROMACS v2023.3] -> visualisation [Fiji v1.53e, ImageJ v1.53e, PyMOL v2.5.0] -> stage not stated [AlphaFold, DESeq2 v1.5, HMMER, PHENIX, STRING db]

### Scalable and multiplexed recorders of gene regulation dynamics across weeks. (Nature 2026)

- DOI: 10.1038/s41586-026-10156-9 | PMCID: PMC13102694 | PMID: 41588170
- Version used: **2021.1**
- Evidence: All molecular dynamics simulations were performed using GROMACS 2021.1 packages.
- Full pipeline: alignment/mapping [PyMOL] -> dimensionality reduction/clustering [UMAP, scikit-image] -> simulation/modelling [AlphaFold, GROMACS v2021.1] -> stage not stated [ImageJ, PyTorch, napari]

### Computational enzyme design by catalytic motif scaffolding. (Nature 2026)

- DOI: 10.1038/s41586-025-09747-9 | PMCID: PMC12727513 | PMID: 41339546
- Evidence: Molecular dynamics simulations Molecular dynamics simulations were performed using GROMACS 65 version 2023.4.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis] -> structure determination [PHENIX] -> stage not stated [AlphaFold, SciPy]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **2023.2**
- Evidence: GROMACS (v.2023.2) input files were generated according to CHARMM-GUI’s standard protocol, comprising energy minimization (step 6.0), six-step equilibration (steps 6.1–6.6), and production dynamics (step 7), which were extended to 50 ns.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Common sequence motifs of nascent chains engage the ribosome surface and trigger factor. (PNAS 2021)

- DOI: 10.1073/pnas.2103015118 | PMCID: PMC8719866 | PMID: 34930833
- Version used: **5.0.4**
- Evidence: Simulations were run in GROMACS 5.0.4 ( 61 ) with Plumed 2.1 ( 62 ) libraries used to introduce RDC restraints and well-tempered bias-exchange metadynamics protocols.
- Full pipeline: simulation/modelling [GROMACS v5.0.4, MDAnalysis, VMD]

### Identification and characterization of an atypical Gαs-biased β<sub>2</sub>AR agonist that fails to evoke airway smooth muscle cell tachyphylaxis. (PNAS 2021)

- DOI: 10.1073/pnas.2026668118 | PMCID: PMC8670521 | PMID: 34857633
- Evidence: MD simulations were carried out using GROMACS (Uppsala University) as described ( 41 ), with optimization as indicated in SI Appendix , SI Expanded Methods .
- Full pipeline: simulation/modelling [GROMACS]

### Vascular K<sub>ATP</sub> channel structural dynamics reveal regulatory mechanism by Mg-nucleotides. (PNAS 2021)

- DOI: 10.1073/pnas.2109441118 | PMCID: PMC8694068 | PMID: 34711681
- Version used: **2019.4**
- Evidence: Pairwise distances were analyzed from the simulated trajectories using the gmx pairdist tool in Gromacs 2019.4 ( 66 ).
- Full pipeline: simulation/modelling [GROMACS v2019.4] -> structure determination [Coot, PHENIX] -> stage not stated [RELION]

### Constitutive signal bias mediated by the human GHRHR splice variant 1. (PNAS 2021)

- DOI: 10.1073/pnas.2106606118 | PMCID: PMC8501799 | PMID: 34599099
- Version used: **5.1.4**
- Evidence: On the basis of the CHARMM36m all-atom force field ( 82 , 83 ), MD simulations were conducted using GROMACS 5.1.4 ( 84 , 85 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v1.18, RELION]

### Amyloid-β peptide dimers undergo a random coil to β-sheet transition in the aqueous phase but not at the neuronal membrane. (PNAS 2021)

- DOI: 10.1073/pnas.2106210118 | PMCID: PMC8488611 | PMID: 34544868
- Evidence: The all-atom MD simulations were performed using GROMACS/2018.2 ( 59 ) along with the CHARMM36m force field for A β 42 ( 60 ) and Charmm36 for the lipids ( 61 ).
- Full pipeline: simulation/modelling [GROMACS, VMD] -> visualisation [VMD] -> stage not stated [Python]

### Probing solution structure of the pentameric ligand-gated ion channel GLIC by small-angle neutron scattering. (PNAS 2021)

- DOI: 10.1073/pnas.2108006118 | PMCID: PMC8449418 | PMID: 34504004
- Evidence: Energy minimization, equilibration, and MD simulations were performed using Gromacs ( 56 ), versions 2018.4 and 2019.3.
- Full pipeline: simulation/modelling [GROMACS] -> visualisation [Matplotlib]

### Hydrogen bonding rearrangement by a mitochondrial disease mutation in cytochrome <i>bc</i><sub>1</sub> perturbs heme <i>b</i><sub>H</sub> redox potential and spin state. (PNAS 2021)

- DOI: 10.1073/pnas.2026169118 | PMCID: PMC8379992 | PMID: 34389670
- Version used: **2016.4**
- Evidence: All simulations were performed with GROMACS 2016.4 and 2020.3 software ( 46 ) at 310 K and 1 atm pressure, with the temperature and pressure being controlled by the Nose-Hoover thermostat ( 47 , 48 ) and Parrinello-Rahman barostat ( 49 , 50 ), respectively.
- Full pipeline: simulation/modelling [GROMACS v2016.4]

### Functional cross-talk between phosphorylation and disease-causing mutations in the cardiac sodium channel Na<sub>v</sub>1.5. (PNAS 2021)

- DOI: 10.1073/pnas.2025320118 | PMCID: PMC8379932 | PMID: 34373326
- Version used: **2019.3**
- Evidence: Simulations were performed using GROMACS 2019.3 ( 84 , 85 ).
- Full pipeline: simulation/modelling [GROMACS v2019.3]

### Non-Markovian modeling of protein folding. (PNAS 2021)

- DOI: 10.1073/pnas.2023856118 | PMCID: PMC8346879 | PMID: 34326249
- Evidence: All simulations are performed in the NVT ensemble using the Gromacs 2019 MD package ( 50 ).
- Full pipeline: simulation/modelling [GROMACS, Python]

### Molecular insights into differentiated ligand recognition of the human parathyroid hormone receptor 2. (PNAS 2021)

- DOI: 10.1073/pnas.2101279118 | PMCID: PMC8364112 | PMID: 34353904
- Version used: **5.1.4**
- Evidence: On the basis of the CHARMM36m all-atom force field ( 39 – 41 ), molecular dynamics simulations were conducted using GROMACS 5.1.4 ( 42 , 43 ).
- Full pipeline: simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> visualisation [PyMOL]

### Targeted in situ cross-linking mass spectrometry and integrative modeling reveal the architectures of three proteins from SARS-CoV-2. (PNAS 2021)

- DOI: 10.1073/pnas.2103554118 | PMCID: PMC8403911 | PMID: 34373319
- Evidence: MD simulations were performed on the dimerization domain of the N protein model with docked RNA using GROMACS 2020 software ( 51 ) and the PARMBSC1 force field ( 52 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold]

### Design and proof of concept for targeted phage-based COVID-19 vaccination strategies with a streamlined cold-free supply chain. (PNAS 2021)

- DOI: 10.1073/pnas.2105739118 | PMCID: PMC8325333 | PMID: 34234013
- Evidence: All-atom explicit-solvent simulations of the epitope sequences were performed with the GROMACS 2020 software package ( 65 , 66 ).
- Full pipeline: simulation/modelling [GROMACS]

### Quantification and demonstration of the collective constriction-by-ratchet mechanism in the dynamin molecular motor. (PNAS 2021)

- DOI: 10.1073/pnas.2101144118 | PMCID: PMC8285958 | PMID: 34244431
- Version used: **4.5.3**
- Evidence: Simulations were performed using GROMACS 4.5.3 ( 59 ) containing code edits implementing Gaussian contact interactions (available at ).
- Full pipeline: simulation/modelling [GROMACS v4.5.3]

### Deactivation blocks proton pathways in the mitochondrial complex I. (PNAS 2021)

- DOI: 10.1073/pnas.2019498118 | PMCID: PMC8307655 | PMID: 34272275
- Version used: **2016.3**
- Evidence: All CGMD simulations were performed using Gromacs 2016.3 ( 66 ).
- Full pipeline: simulation/modelling [GROMACS v2016.3, NAMD, PyMOL v2.4.1]

### Revealing atomic-scale molecular diffusion of a plant-transcription factor WRKY domain protein along DNA. (PNAS 2021)

- DOI: 10.1073/pnas.2102621118 | PMCID: PMC8201915 | PMID: 34074787
- Evidence: ...n DNA, which were accumulated to ∼100 μs [under Amber99SB-ILDN force field ( 40 ) for proteins and Amber94 force field ( 41 ) for nucleic acids using Gromacs ( 42 ) ( SI Appendix , Methods )], including several 10-μs–long MD simulations and multiple distributed 2- to 4-μs runs to improve samplings ( SI Appendix , Table S1 ).
- Full pipeline: simulation/modelling [GROMACS]

### AI-based spectroscopic monitoring of real-time interactions between SARS-CoV-2 and human ACE2. (PNAS 2021)

- DOI: 10.1073/pnas.2025879118 | PMCID: PMC8256048 | PMID: 34185681
- Evidence: Methods MD simulations for SARS-CoV-1 (PDB ID code 2AMQ) were performed with the GROMACS package ( 39 ) and the OPLS-AA force fields ( 40 ).
- Full pipeline: simulation/modelling [GROMACS]

### Membrane fusion and drug delivery with carbon nanotube porins. (PNAS 2021)

- DOI: 10.1073/pnas.2016974118 | PMCID: PMC8126853 | PMID: 33941689
- Version used: **2018.7**
- Evidence: Simulations were performed using GROMACS 2018.7 ( 38 ) with the recommended new parameter set for MARTINI simulations ( 39 ).
- Full pipeline: normalisation [ImageJ] -> simulation/modelling [GROMACS v2018.7]

### Dual nature of human ACE2 glycosylation in binding to SARS-CoV-2 spike. (PNAS 2021)

- DOI: 10.1073/pnas.2100425118 | PMCID: PMC8126795 | PMID: 33903171
- Version used: **2019.6**
- Evidence: The interaction of the ACE2 receptor with the RBD of the spike protein was studied with all-atom explicit solvent MD simulation using GROMACS v2019.6 ( 33 ).
- Full pipeline: simulation/modelling [GROMACS v2019.6, MDAnalysis, VMD]

### Early-stage dynamics of chloride ion-pumping rhodopsin revealed by a femtosecond X-ray laser. (PNAS 2021)

- DOI: 10.1073/pnas.2020486118 | PMCID: PMC8020794 | PMID: 33753488
- Version used: **5.1.2**
- Evidence: The constant pressure and temperature (NPT) ensemble (at 1 atm pressure and room temperature of 293.15 K) was simulated using GROMACS 5.1.2 ( 51 ).
- Full pipeline: simulation/modelling [GROMACS v5.1.2, VMD] -> structure determination [Coot] -> visualisation [VMD] -> stage not stated [CCP4, PHENIX, UCSF Chimera]

### Nonthermal and reversible control of neuronal signaling and behavior by midinfrared stimulation. (PNAS 2021)

- DOI: 10.1073/pnas.2015685118 | PMCID: PMC7958416 | PMID: 33649213
- Version used: **5.1.4**
- Evidence: All simulations were performed using the software GROMACS 5.1.4 ( 51 ).
- Full pipeline: simulation/modelling [GROMACS v5.1.4]

### Protein design-scapes generated by microfluidic DNA assembly elucidate domain coupling in the bacterial histidine kinase CpxA. (PNAS 2021)

- DOI: 10.1073/pnas.2017719118 | PMCID: PMC8000134 | PMID: 33723045
- Evidence: 7 A ) in explicit solvent with CHARMM36 parameters ( 51 ) as implemented in GROMACS 2018.
- Full pipeline: stage not stated [GROMACS]

### Nonselective cation permeation in an AMPA-type glutamate receptor. (PNAS 2021)

- DOI: 10.1073/pnas.2012843118 | PMCID: PMC7923540 | PMID: 33602810
- Evidence: In the amber setup, insertion of the AMPAR TMD into a POPC lipid bilayer was performed with the Gromacs internal embedding function, whereas in the charmm setup, this process was carried out in charmm– GUI ( 56 ).
- Full pipeline: simulation/modelling [VMD] -> visualisation [VMD] -> stage not stated [GROMACS]

### Cooperativity between the orthosteric and allosteric ligand binding sites of RORγt. (PNAS 2021)

- DOI: 10.1073/pnas.2021287118 | PMCID: PMC8017705 | PMID: 33536342
- Version used: **2019.3**
- Evidence: The GROMACS 2019.3 MD package was used to perform the simulations ( 59 ).
- Full pipeline: simulation/modelling [GROMACS v2019.3] -> structure determination [PHENIX, REFMAC] -> stage not stated [CCP4, PyMOL v2.2.3]

### Long-range structural defects by pathogenic mutations in most severe glucose-6-phosphate dehydrogenase deficiency. (PNAS 2021)

- DOI: 10.1073/pnas.2022790118 | PMCID: PMC7848525 | PMID: 33468660
- Version used: **2019.4**
- Evidence: MD simulations were carried out with the GROMACS 2019.4 package ( 61 ).
- Full pipeline: alignment/mapping [RELION v3.0.6] -> simulation/modelling [GROMACS v2019.4] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX]

### Immature HIV-1 assembles from Gag dimers leaving partial hexamers at lattice edges as potential substrates for proteolytic maturation. (PNAS 2021)

- DOI: 10.1073/pnas.2020054118 | PMCID: PMC7826355 | PMID: 33397805
- Evidence: All simulations were prepared and simulated with GROMACS 2016 ( 46 ) using the CHARMM36m forcefield ( 47 ).
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.4] -> visualisation [UCSF Chimera]

### Biophysical characterization of calcium-binding and modulatory-domain dynamics in a pentameric ligand-gated ion channel. (PNAS 2022)

- DOI: 10.1073/pnas.2210669119 | PMCID: PMC9897478 | PMID: 36480474
- Evidence: The CHARMM36m force-field was used ( 53 ), and simulations were performed using GROMACS-2020.3 ( 54 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS, VMD] -> stage not stated [PHENIX, RELION v3.1, UCSF Chimera]

### Coupling dual metal active sites and low-solvation architecture toward high-performance aqueous ammonium-ion batteries. (PNAS 2022)

- DOI: 10.1073/pnas.2214545119 | PMCID: PMC9897483 | PMID: 36472961
- Version used: **2020.4**
- Evidence: The calculation was made by Gromacs 2020.4 using the AMBER03 force field ( 55 ).
- Full pipeline: simulation/modelling [GROMACS v2020.4]

### Exact reaction coordinates for flap opening in HIV-1 protease. (PNAS 2022)

- DOI: 10.1073/pnas.2214906119 | PMCID: PMC9894123 | PMID: 36459640
- Evidence: Methods All simulations are performed using the Amber 99sb force field with the Onufriev-Bashford-Case (OBC) implicit solvent model 65 and the Groningen Machine for Chemical Simulations (GROMACS) 4.5.4 simulation suite 66 , 67 .
- Full pipeline: simulation/modelling [GROMACS]

### Insertions and deletions mediated functional divergence of Rossmann fold enzymes. (PNAS 2022)

- DOI: 10.1073/pnas.2207965119 | PMCID: PMC9860332 | PMID: 36417431
- Version used: **2020.1**
- Evidence: The MD simulations were performed using Gromacs version 2020.1 ( 50 ) and the charmm36-mar2019 force field ( 51 ).
- Full pipeline: simulation/modelling [GROMACS v2020.1] -> structure determination [PHENIX, PyMOL]

### Intrinsically disordered ectodomain modulates ion permeation through a metal transporter. (PNAS 2022)

- DOI: 10.1073/pnas.2214602119 | PMCID: PMC9889885 | PMID: 36409899
- Evidence: HREX was performed in GROMACS (version 2019) patched with PLUMED (version 2.6.3) using the REST2 method ( 33 – 36 ).
- Full pipeline: simulation/modelling [MDAnalysis, MDTraj] -> stage not stated [GROMACS, PLUMED v2.6.3, VMD]

### Temperature-sensitive contacts in disordered loops tune enzyme I activity. (PNAS 2022)

- DOI: 10.1073/pnas.2210537119 | PMCID: PMC9704738 | PMID: 36375052
- Version used: **2018.8**
- Evidence: Molecular dynamics simulations were carried out in GROMACS 2018.8 using the leapfrog integration method with 2fs timesteps ( 20 – 23 ).
- Full pipeline: normalisation [ImageJ] -> simulation/modelling [GROMACS v2018.8] -> visualisation [PyMOL]

### Differential interactions of resting, activated, and desensitized states of the α7 nicotinic acetylcholine receptor with lipidic modulators. (PNAS 2022)

- DOI: 10.1073/pnas.2208081119 | PMCID: PMC9618078 | PMID: 36251999
- Evidence: All simulations were performed with GROMACS 2020 ( 60 ).
- Full pipeline: simulation/modelling [GROMACS] -> visualisation [MDAnalysis, Matplotlib, VMD]

### Structural basis for host recognition and superinfection exclusion by bacteriophage T5. (PNAS 2022)

- DOI: 10.1073/pnas.2211672119 | PMCID: PMC9586334 | PMID: 36215462
- Evidence: MD simulations were performed using the GROMACS software package ( 59 ) and the CHARMM36m force field ( 60 , 61 ) and were visualized and analyzed using the VMD software ( 62 ).
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [GROMACS, VMD]

### CRY2 isoform selectivity of a circadian clock modulator with antiglioblastoma efficacy. (PNAS 2022)

- DOI: 10.1073/pnas.2203936119 | PMCID: PMC9546630 | PMID: 36161947
- Evidence: All MD simulations were performed using GROMACS ( 52 ).
- Full pipeline: normalisation [CCP4] -> simulation/modelling [GROMACS] -> structure determination [PHENIX]

### DYF-5/MAK-dependent phosphorylation promotes ciliary tubulin unloading. (PNAS 2022)

- DOI: 10.1073/pnas.2207134119 | PMCID: PMC9407615 | PMID: 35969738
- Evidence: Molecular dynamics analysis was performed as described previously ( 34 ) using GROMACS (RRID: SCR_014565) version 4.6.7 using the OPLS-AA force field parameter set.
- Full pipeline: quantification [ImageJ] -> simulation/modelling [GROMACS] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### De novo designed protein inhibitors of amyloid aggregation and seeding. (PNAS 2022)

- DOI: 10.1073/pnas.2206240119 | PMCID: PMC9407671 | PMID: 35969734
- Evidence: Simulations in an explicit cubic water box were carried out in GROMACS 2018 for 200 ns ( 46 ).
- Full pipeline: simulation/modelling [GROMACS]

### From data to noise to data for mixing physics across temperatures with generative artificial intelligence. (PNAS 2022)

- DOI: 10.1073/pnas.2203656119 | PMCID: PMC9371742 | PMID: 35925885
- Evidence: Simulations were performed using GROMACS 2016 ( 44 ).
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.4, PyMOL]

### Molecular mechanism for strengthening E-cadherin adhesion using a monoclonal antibody. (PNAS 2022)

- DOI: 10.1073/pnas.2204473119 | PMCID: PMC9371698 | PMID: 35921442
- Version used: **2020.1**
- Evidence: MD simulations were performed with GROMACS 2020.1 using the FARM high-performance computing cluster at University of California, Davis as described previously ( 38 ).
- Full pipeline: dimensionality reduction/clustering [GROMACS v2020.1] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot, PHENIX]

### Correlation between the binding affinity and the conformational entropy of nanobody SARS-CoV-2 spike protein complexes. (PNAS 2022)

- DOI: 10.1073/pnas.2205412119 | PMCID: PMC9351521 | PMID: 35858383
- Evidence: The system was subsequently energy minimized, equilibrated in an NPT and subsequent NVT molecular dynamics equilibration using GROMACS-2018.6 ( 78 ).
- Full pipeline: dimensionality reduction/clustering [RELION] -> simulation/modelling [GROMACS, PLUMED v2.6.0] -> structure determination [ChimeraX, PHENIX] -> stage not stated [CCP4]

### Targeting oncogenic KRAS with molecular brush-conjugated antisense oligonucleotides. (PNAS 2022)

- DOI: 10.1073/pnas.2113180119 | PMCID: PMC9304022 | PMID: 35858356
- Evidence: All simulations were performed using the GROMACS 2018 package ( 58 ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [GROMACS]

### Multi-eGO: An in silico lens to look into protein aggregation kinetics at atomic resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2203181119 | PMCID: PMC9245614 | PMID: 35737839
- Evidence: Materials and Methods MD simulations in this work were performed with GROMACS ( 83 ).
- Full pipeline: simulation/modelling [GROMACS]

### Affinity of disordered protein complexes is modulated by entropy-energy reinforcement. (PNAS 2022)

- DOI: 10.1073/pnas.2120456119 | PMCID: PMC9245678 | PMID: 35727975
- Evidence: GROMACS simulation package 5.1.5 ( 71 ) was used to run Langevin dynamics simulations with a friction coefficient of 0.1 ps −1 and a time step of 10 fs for a total of 2 μs for equilibration of the complexes.
- Full pipeline: simulation/modelling [GROMACS]

### ESCPE-1 mediates retrograde endosomal sorting of the SARS-CoV-2 host factor Neuropilin-1. (PNAS 2022)

- DOI: 10.1073/pnas.2201980119 | PMCID: PMC9231623 | PMID: 35696571
- Evidence: Twenty nanosecond atomistic dynamic simulations of the modeled complexes were carried out using the amber99sb-ildn forcefield in TIP3P waters and GROMACS ( 56 ) (2019.2) according to the method described recently ( 57 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [ImageJ, Metascape]

### Lung surfactant negatively affects the photodynamic inactivation of bacteria-in vitro and molecular dynamic simulation analyses. (PNAS 2022)

- DOI: 10.1073/pnas.2123564119 | PMCID: PMC9231493 | PMID: 35696565
- Version used: **2021.1**
- Evidence: All simulations were performed using the Gromacs 2021.1 program and the Gromos54a7 force field.
- Full pipeline: simulation/modelling [GROMACS v2021.1]

### Membrane insertion mechanism of the caveola coat protein Cavin1. (PNAS 2022)

- DOI: 10.1073/pnas.2202295119 | PMCID: PMC9231606 | PMID: 35696574
- Evidence: All simulations were performed using GROMACS 2018 software ( 37 ), and the mouse Cavin1 HR1 domain structure (PDB ID code 4QKV) was used as the initial model ( 15 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [ImageJ]

### A modular approach to map out the conformational landscapes of unbound intrinsically disordered proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2113572119 | PMCID: PMC9191344 | PMID: 35658083
- Evidence: Molecular dynamics simulations in explicit solvent were performed using the GROMACS package, the Charmm22* force field, and the TIP3P water model.
- Full pipeline: simulation/modelling [GROMACS]

### Structural basis of peptidomimetic agonism revealed by small- molecule GLP-1R agonists Boc5 and WB4-24. (PNAS 2022)

- DOI: 10.1073/pnas.2200155119 | PMCID: PMC9171782 | PMID: 35561211
- Version used: **2020.1**
- Evidence: Molecular dynamics simulation studies were performed using Gromacs 2020.1.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v1.06]

### Dromedary camel nanobodies broadly neutralize SARS-CoV-2 variants. (PNAS 2022)

- DOI: 10.1073/pnas.2201433119 | PMCID: PMC9170159 | PMID: 35476528
- Evidence: The nanobody models were subjected to molecular dynamics calculations [Gromacs 2021 ( 44 )] to build a diverse set of conformations for macromolecular docking [ZDock v 3.0.2 ( 45 )] and rigid body fitting to the maps using Chimera, version 1.15 (Mac build 42258) ( 46 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS] -> structure determination [PHENIX v1.19.2] -> stage not stated [Pangolin]

### A molecular switch controls the impact of cholesterol on a Kir channel. (PNAS 2022)

- DOI: 10.1073/pnas.2109431119 | PMCID: PMC9060494 | PMID: 35333652
- Version used: **2016.3**
- Evidence: The CG simulations were carried out with the Martini force field, version 2.2 for protein and version 2 for lipids ( 63 – 65 ), using GROMACS version 2016.3 ( 66 ).
- Full pipeline: simulation/modelling [GROMACS v2016.3] -> visualisation [PyMOL] -> stage not stated [ImageJ, Matplotlib, NumPy, VMD v1.9.3]

### Bending-torsional elasticity and energetics of the plus-end microtubule tip. (PNAS 2022)

- DOI: 10.1073/pnas.2115516119 | PMCID: PMC8944587 | PMID: 35302883
- Evidence: All subsequent MD simulations were carried out with GROMACS 2019 ( 85 ).
- Full pipeline: simulation/modelling [GROMACS]

### Elucidation of the key role of Pt···Pt interactions in the directional self-assembly of platinum(II) complexes. (PNAS 2022)

- DOI: 10.1073/pnas.2116543119 | PMCID: PMC8944581 | PMID: 35298336
- Version used: **4.5.5**
- Evidence: All MD simulations were performed by the GROMACS (version 4.5.5) package ( 65 ).
- Full pipeline: simulation/modelling [GROMACS v4.5.5]

### ATP allosterically stabilizes integrin-linked kinase for efficient force generation. (PNAS 2022)

- DOI: 10.1073/pnas.2106098119 | PMCID: PMC8933812 | PMID: 35259013
- Version used: **2018.1**
- Evidence: MD simulations were performed by using GROMACS 2018.1 ( 57 ), the Amber99sb*-ILDNP force-field ( 58 , 59 ), the TIP3-water model ( 60 ), and ATP parameters ( 61 ).
- Full pipeline: simulation/modelling [GROMACS v2018.1]

### Structural and thermodynamic framework for PIEZO1 modulation by small molecules. (PNAS 2023)

- DOI: 10.1073/pnas.2310933120 | PMCID: PMC10723123 | PMID: 38060566
- Version used: **2016.4**
- Evidence: Summary of three computational methods Absolute binding free energy (ABFE) Relative binding free energy (RBFE) SILCS MD engine NAMD2.14 AMBER20 GROMACS 2016.4 Methods FEP/REMD Double decoupling Soft-core potential AMBET-TI Dual ligand topology Soft-core potential Unified protocol GCMC/MD Force field Charmm36ff, TIP3P, CGenFF ff19SB, Lipid 17, GAFF2.1, TIP3P Charmm36ff, TIP3P, CGenFF Nonbonded para...
- Full pipeline: alignment/mapping [NAMD] -> simulation/modelling [GROMACS v2016.4, NAMD] -> stage not stated [AlphaFold, AutoDock Vina]

### pH-dependent structural transitions in cationic ionizable lipid mesophases are critical for lipid nanoparticle function. (PNAS 2023)

- DOI: 10.1073/pnas.2310491120 | PMCID: PMC10723131 | PMID: 38055742
- Evidence: The Gromacs package (v-2019) ( 52 ) was used to perform the MD simulations.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [MACS2]

### Fully activated structure of the sterol-bound Smoothened GPCR-Gi protein complex. (PNAS 2023)

- DOI: 10.1073/pnas.2300919120 | PMCID: PMC10710022 | PMID: 38015850
- Evidence: All equilibration was done using the CHARMM36 force field ( 42 ) and the GROMACS MD package ( 43 ) at a temperature of 310 K.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [PyMOL]

### Dimerization mechanism of an inverted-topology ion channel in membranes. (PNAS 2023)

- DOI: 10.1073/pnas.2308454120 | PMCID: PMC10666096 | PMID: 37956279
- Version used: **2018.8**
- Evidence: To equilibrate each of these systems, we carried out an MD simulation of 50 μs at 1 atm and 303 K, using GROMACS 2018.8 ( 40 ).
- Full pipeline: simulation/modelling [GROMACS v2018.8, NAMD] -> stage not stated [PLUMED v2.2.5]

### An amino-domino model described by a cross-peptide-bond Ramachandran plot defines amino acid pairs as local structural units. (PNAS 2023)

- DOI: 10.1073/pnas.2301064120 | PMCID: PMC10623034 | PMID: 37878722
- Evidence: Molecular dynamics was preformed using GROMACS ( 27 , 28 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold, scikit-learn] -> simulation/modelling [GROMACS]

### Diversity of rhodopsin cyclases in zoospore-forming fungi. (PNAS 2023)

- DOI: 10.1073/pnas.2310600120 | PMCID: PMC10622942 | PMID: 37871207
- Version used: **2019.3**
- Evidence: The simulations were performed with GROMACS 2019.3 and 2021.3 ( 31 ) using the CHARMM36m force field ( 32 ) extended by the retinal parameters ( 33 ).
- Full pipeline: read trimming [IQ-TREE, SPAdes v3.15.5] -> alignment/mapping [IQ-TREE] -> simulation/modelling [GROMACS v2019.3] -> visualisation [Matplotlib v3.4.3, PyMOL v2.4.1] -> stage not stated [AlphaFold, MDAnalysis v2.4.3]

### Molecular basis of signal transduction mediated by the human GIPR splice variants. (PNAS 2023)

- DOI: 10.1073/pnas.2306145120 | PMCID: PMC10576055 | PMID: 37792509
- Version used: **2021.4**
- Evidence: Molecular dynamic simulations were performed by Gromacs 2021.4.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2021.4] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX v1.2.4] -> stage not stated [CTFFIND v1.06, ImageJ, RELION]

### Combined prediction and design reveals the target recognition mechanism of an intrinsically disordered protein interaction domain. (PNAS 2023)

- DOI: 10.1073/pnas.2305603120 | PMCID: PMC10523638 | PMID: 37722056
- Evidence: The simulations were conducted using the GROMACS-2021.5 software package ( 50 ) with the CHARMM36 force field ( 51 ) and TIP3P water model.
- Full pipeline: simulation/modelling [AlphaFold, GROMACS] -> stage not stated [PHENIX]

### Mixed, nonclassical behavior in a classic allosteric protein. (PNAS 2023)

- DOI: 10.1073/pnas.2308338120 | PMCID: PMC10515163 | PMID: 37695919
- Version used: **2020.3**
- Evidence: Molecular dynamics simulations were run in the GROMACS 2020.3 package ( 62 , 63 ) using the CHARMM3.6 ( 64 ) force field.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [GROMACS v2020.3] -> stage not stated [PyMOL, R]

### Specific inhibition of an anticancer target, polo-like kinase 1, by allosterically dismantling its mechanism of substrate recognition. (PNAS 2023)

- DOI: 10.1073/pnas.2305037120 | PMCID: PMC10629583 | PMID: 37603740
- Version used: **2022.3**
- Evidence: The simulation system was first energy-minimized by the GROMACS 2022.3 simulation package ( https://doi.org/10.5281/zenodo.7037337 ) using the 5,000-step steepest descent method, followed by a 25 ps NVT equilibration with position restraints on the protein heavy atoms.
- Full pipeline: normalisation [CCP4] -> simulation/modelling [GROMACS v2022.3, RDKit, VMD v1.9.4] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL, VMD v1.9.4] -> stage not stated [AlphaFold]

### Structural insights into the interaction of three Y-shaped ligands with PI3Kα. (PNAS 2023)

- DOI: 10.1073/pnas.2304071120 | PMCID: PMC10450665 | PMID: 37585458
- Version used: **2020.1**
- Evidence: MD simulations were carried out using GROMACS 2020.1.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot v0.9.4.1] -> visualisation [ChimeraX v1.0, PyMOL v2.1, UCSF Chimera v1.13.1] -> stage not stated [CTFFIND v1.06, PHENIX v1.18.2, RELION]

### Detecting dynamic domains and local fluctuations in complex molecular systems via timelapse neighbors shuffling. (PNAS 2023)

- DOI: 10.1073/pnas.2300565120 | PMCID: PMC10372573 | PMID: 37467266
- Evidence: All the trajectories analyzed for the systems simulated above are obtained using the GROMACS software ( 81 ).
- Full pipeline: simulation/modelling [GROMACS, LAMMPS] -> machine learning [LAMMPS] -> stage not stated [SciPy]

### Unveiling the catalytic mechanism of GTP hydrolysis in microtubules. (PNAS 2023)

- DOI: 10.1073/pnas.2305899120 | PMCID: PMC10319017 | PMID: 37364095
- Version used: **2019.4**
- Evidence: Each system was initially equilibrated in the NVT ensemble for 100 ns in a 121.5-Å side-length cubic periodic box (124.4 Å for the free heterodimer) with 100 mM NaCl at 310 K using the CHARMM36m force field and GROMACS 2019.4 ( 34 , 35 ).
- Full pipeline: simulation/modelling [GROMACS v2019.4] -> stage not stated [PLUMED, R]

### Pressure pushes tRNA<sup>Lys3</sup> into excited conformational states. (PNAS 2023)

- DOI: 10.1073/pnas.2215556120 | PMCID: PMC10293818 | PMID: 37339210
- Version used: **4.6.7**
- Evidence: Gromacs 4.6.7 was used as the computation engine to run the simulations ( 93 ).
- Full pipeline: simulation/modelling [GROMACS v4.6.7]

### Closed-loop fluid-fluid immiscibility in binary lipid-sterol membranes. (PNAS 2023)

- DOI: 10.1073/pnas.2216002120 | PMCID: PMC10288576 | PMID: 37314933
- Evidence: Using GROMACS for integrating the equation of motion with a time step of 2 fs, we first minimize the energy of the bilayer membrane.
- Full pipeline: stage not stated [GROMACS]

### Phase separation of intrinsically disordered FG-Nups is driven by highly dynamic FG motifs. (PNAS 2023)

- DOI: 10.1073/pnas.2221804120 | PMCID: PMC10288634 | PMID: 37307457
- Evidence: All simulations are performed at 300 K and physiological salt concentration of 150 mM using GROMACS ( 69 ) molecular dynamics software (version 2019.4), where the stochastic dynamics integrator operates with a time step of 0.02 ps and inverse friction coefficient γ −1 = 50 ps.
- Full pipeline: simulation/modelling [GROMACS]

### Activator-induced conformational changes regulate division-associated peptidoglycan amidases. (PNAS 2023)

- DOI: 10.1073/pnas.2302580120 | PMCID: PMC10268282 | PMID: 37276423
- Evidence: Molecular dynamics simulations used Gromacs ( 38 ) with the Charm forcefield ( 39 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [CCP4]

### Imaging of pH distribution inside individual microdroplet by stimulated Raman microscopy. (PNAS 2023)

- DOI: 10.1073/pnas.2219588120 | PMCID: PMC10193990 | PMID: 37155894
- Version used: **2019.6**
- Evidence: All the MD calculations were executed by the software package of GROMACS 2019.6.
- Full pipeline: visualisation [VMD] -> stage not stated [GROMACS v2019.6]

### A large conserved family of small-molecule carboxyl methyltransferases identified from microorganisms. (PNAS 2023)

- DOI: 10.1073/pnas.2301389120 | PMCID: PMC10193983 | PMID: 37155856
- Version used: **2018.5**
- Evidence: MD simulations and analysis were performed using GROMACS 2018.5 ( SI Appendix , Fig.
- Full pipeline: simulation/modelling [GROMACS v2018.5]

### Universality in RNA and DNA deformations induced by salt, temperature change, stretching force, and protein binding. (PNAS 2023)

- DOI: 10.1073/pnas.2218425120 | PMCID: PMC10193934 | PMID: 37155848
- Evidence: Our all-atom MD simulations used the GROMACS program ( 47 ) and OL3 force field ( 48 ).
- Full pipeline: simulation/modelling [GROMACS]

### Gatekeeper mutations activate FGF receptor tyrosine kinases by destabilizing the autoinhibited state. (PNAS 2023)

- DOI: 10.1073/pnas.2213090120 | PMCID: PMC9974468 | PMID: 36791110
- Version used: **5.1.4**
- Evidence: Simulations were built in either Amber 16.06 or Amber 20.11 and ran in either Gromacs 5.1.4 and Gromacs 2020.4 for 2PVF and 3KY2, respectively.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> simulation/modelling [GROMACS v5.1.4]

### Molecular mechanism and energetics of coupling between substrate binding and product release in the F<sub>1</sub>-ATPase catalytic cycle. (PNAS 2023)

- DOI: 10.1073/pnas.2215650120 | PMCID: PMC9974484 | PMID: 36780529
- Evidence: All simulations were performed using the Gromacs suite ( 51 ).
- Full pipeline: simulation/modelling [GROMACS]

### Molecular mechanism of GTP binding- and dimerization-induced enhancement of Sar1-mediated membrane remodeling. (PNAS 2023)

- DOI: 10.1073/pnas.2212513120 | PMCID: PMC9974494 | PMID: 36780528
- Evidence: Explicit solvent all-atom MD simulations are performed using GROMACS ( 48 , 49 ) version 2018.3 and the CHARMM36m ( 50 ) force field with the TIP3P explicit solvent model.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, VMD]

### Driving and characterizing nucleation of urea and glycine polymorphs in water. (PNAS 2023)

- DOI: 10.1073/pnas.2216099120 | PMCID: PMC9963467 | PMID: 36757888
- Evidence: GROMACS and PLUMED are both free and open source software packages available for download at https://www.gromacs.org and https://www.plumed.org , respectively.
- Full pipeline: simulation/modelling [PLUMED, VMD] -> visualisation [VMD] -> stage not stated [GROMACS]

### Small molecules disaggregate alpha-synuclein and prevent seeding from patient brain-derived fibrils. (PNAS 2023)

- DOI: 10.1073/pnas.2217835120 | PMCID: PMC9963379 | PMID: 36757890
- Evidence: MD was performed using GROMACS version 2020 using a CHARMM36 force field.
- Full pipeline: dimensionality reduction/clustering [Open Babel] -> simulation/modelling [GROMACS] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, ImageJ, UCSF Chimera]

### Apolipoprotein E4 has extensive conformational heterogeneity in lipid-free and lipid-bound forms. (PNAS 2023)

- DOI: 10.1073/pnas.2215371120 | PMCID: PMC9963066 | PMID: 36749730
- Evidence: FAST simulations were performed using GROMACS, and Folding@home simulations were performed using OpenMM.
- Full pipeline: simulation/modelling [GROMACS, OpenMM, PyMOL]

### Supramolecular organization and dynamics of mannosylated phosphatidylinositol lipids in the mycobacterial plasma membrane. (PNAS 2023)

- DOI: 10.1073/pnas.2212755120 | PMCID: PMC9945971 | PMID: 36693100
- Version used: **2021.3**
- Evidence: Simulations were run using GROMACS version 2021.3 ( 33 ).
- Full pipeline: simulation/modelling [GROMACS v2021.3, Python] -> stage not stated [AlphaFold, Clustal Omega, Matplotlib, PLUMED]

### De novo protein fold design through sequence-independent fragment assembly simulations. (PNAS 2023)

- DOI: 10.1073/pnas.2208275120 | PMCID: PMC9942881 | PMID: 36656852
- Evidence: MD is a useful tool as it allows for the study of protein motion and stability beyond static measurements such as energy calculations, where 20 ns unconstrained MD simulations were carried out using GROMACS ( 46 ) with the CHARMM36 force field (see Methods ).
- Full pipeline: simulation/modelling [GROMACS] -> machine learning [GROMACS] -> stage not stated [AlphaFold]

### Structure-function correlates of fibrinogen binding by <i>Acinetobacter</i> adhesins critical in catheter-associated urinary tract infections. (PNAS 2023)

- DOI: 10.1073/pnas.2212694120 | PMCID: PMC9942807 | PMID: 36652481
- Version used: **2020.1**
- Evidence: MD simulations were run with Gromacs 2020.1 at 310 K using the AMBER99SB-ILDN force field with explicit TIP3P solvent ( 42 – 44 ).
- Full pipeline: read trimming [PHENIX] -> alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS v2020.1] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### How acidic amino acid residues facilitate DNA target site selection. (PNAS 2023)

- DOI: 10.1073/pnas.2212501120 | PMCID: PMC9934023 | PMID: 36634135
- Version used: **2018.8**
- Evidence: All force field-based molecular dynamics (MD) simulations were carried out in the isothermal–isobaric (NPT) ensemble using Gromacs 2018.8 ( 60 ) and the Amber-parmbsc1 force field ( 61 ).
- Full pipeline: simulation/modelling [GROMACS v2018.8, NAMD v2.14]

### Macrophages modulate stiffness-related foreign body responses through plasma membrane deformation. (PNAS 2023)

- DOI: 10.1073/pnas.2213837120 | PMCID: PMC9934070 | PMID: 36626552
- Version used: **2019.2**
- Evidence: The molecular dynamics simulation was performed by the GROMACS 2019.2 package with a charmm36 force field.
- Full pipeline: simulation/modelling [GROMACS v2019.2, VMD] -> visualisation [VMD] -> stage not stated [ImageJ]

### Road-blocker HSP disease mutation disrupts pre-organization for ATP hydrolysis in kinesin through a second sphere control. (PNAS 2023)

- DOI: 10.1073/pnas.2215170120 | PMCID: PMC9910451 | PMID: 36574689
- Version used: **5.1**
- Evidence: The classical MD simulations have been performed to equilibrate the ATP-bound enzyme complexes using Gromacs 5.1 simulations program ( 27 ).
- Full pipeline: dimensionality reduction/clustering [PLUMED v2.4.3] -> simulation/modelling [GROMACS v5.1, PLUMED v2.4.3, VMD]

### Lanthanide binding peptide surfactants at air-aqueous interfaces for interfacial separation of rare earth elements. (PNAS 2024)

- DOI: 10.1073/pnas.2411763121 | PMCID: PMC11670062 | PMID: 39700142
- Evidence: MD simulations are performed to model the uncomplexed and the LBT:Tb 3+ binding complex in aqueous solution using GROMACS package ( 77 , 78 ).
- Full pipeline: simulation/modelling [GROMACS]

### Ion permeation through a narrow cavity constriction in KCNQ1 channels: Mechanism and implications for pathogenic variants. (PNAS 2024)

- DOI: 10.1073/pnas.2411182121 | PMCID: PMC11665860 | PMID: 39671184
- Evidence: Materials and Methods The CompEL (computational electrophysiology) method ( 39 ) with dual membrane configuration implemented in GROMACS was used to investigate ion permeations through the pore region of the KCNQ1 channel as previously described ( 41 ).
- Full pipeline: stage not stated [GROMACS]

### Architecture of the Sap S-layer of &lt;i&gt;Bacillus anthracis&lt;/i&gt; revealed by integrative structural biology. (PNAS 2024)

- DOI: 10.1073/pnas.2415351121 | PMCID: PMC11665858 | PMID: 39652757
- Evidence: GROMACS 2021 ( 57 ) was then used to incorporate hydrogen atoms with standard protonation states.
- Full pipeline: alignment/mapping [VMD] -> registration [MotionCor2] -> simulation/modelling [VMD] -> structure determination [RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, GROMACS, IMOD]

### Understanding paralogous epilepsy-associated GABA&lt;sub&gt;A&lt;/sub&gt; receptor variants: Clinical implications, mechanisms, and potential pitfalls. (PNAS 2024)

- DOI: 10.1073/pnas.2413011121 | PMCID: PMC11648851 | PMID: 39642202
- Version used: **2021.4**
- Evidence: Each system was converted to united-atom representation ( 44 , 45 ) and simulated using GROMACS 2021.4 ( 46 ) for 500 ns in triplicate following equilibration.
- Full pipeline: simulation/modelling [GROMACS v2021.4]

### OmpA controls order in the outer membrane and shares the mechanical load. (PNAS 2024)

- DOI: 10.1073/pnas.2416426121 | PMCID: PMC11648852 | PMID: 39630873
- Evidence: All simulations were performed using the Gromacs simulation package ( 71 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [BLAST, ImageJ, Matplotlib]

### Correlating enzymatic reactivity for different substrates using transferable data-driven collective variables. (PNAS 2024)

- DOI: 10.1073/pnas.2416621121 | PMCID: PMC11626191 | PMID: 39589882
- Version used: **2021.5**
- Evidence: All simulations were conducted using GROMACS 2021.5 ( 51 ), with trajectory frames saved every 10 ps.
- Full pipeline: simulation/modelling [GROMACS v2021.5] -> visualisation [PyMOL] -> stage not stated [PLUMED]

### Molecular basis for chemokine recognition and activation of XCR1. (PNAS 2024)

- DOI: 10.1073/pnas.2405732121 | PMCID: PMC11621518 | PMID: 39565315
- Evidence: After assembly, the system was downloaded in GROMACS format.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ColabFold, GROMACS, PyMOL v3.0.3]

### Agonist activation to open the Gα subunit of the GPCR-G protein precoupled complex defines functional agonist activation of TAS2R5. (PNAS 2024)

- DOI: 10.1073/pnas.2409987121 | PMCID: PMC11621838 | PMID: 39565310
- Evidence: All simulations were carried out with a 2 fs time step using GROMACS ( 65 ) with PLUMED ( 66 ).
- Full pipeline: simulation/modelling [GROMACS, PLUMED] -> visualisation [VMD]

### The interplay between liquid-liquid and ferroelectric phase transitions in supercooled water. (PNAS 2024)

- DOI: 10.1073/pnas.2412456121 | PMCID: PMC11588139 | PMID: 39546564
- Evidence: The MD simulations, performed with GROMACS, employed the classical TIP4P/Ice water model ( 56 ) with N = 1 , 000 molecules in NpT ensemble, using a time-step of 2 f s .
- Full pipeline: simulation/modelling [GROMACS]

### Origins of synergy in multilipid lubrication. (PNAS 2024)

- DOI: 10.1073/pnas.2408223121 | PMCID: PMC11588124 | PMID: 39531494
- Evidence: 47 and carried out with the modified GROMACS version published by ref.
- Full pipeline: stage not stated [GROMACS]

### Mineral-associated organic matter is heterogeneous and structured by hydrophobic, charged, and polar interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2413216121 | PMCID: PMC11573572 | PMID: 39514311
- Version used: **2022.4**
- Evidence: Molecular dynamics simulations were performed using GROMACS 2022.4 on the Department of Energy’s (DOE) Deception High Performance Compute cluster at the Pacific Northwest National Laboratory, utilizing the CHARMM3.6 derived CGenFF force field for SOM molecules, the ClayFF force field for minerals and aqueous cations, and the SPC/E model for water.
- Full pipeline: dimensionality reduction/clustering [GROMACS v2022.4, RDKit] -> simulation/modelling [GROMACS v2022.4]

### Atomic view of photosynthetic metabolite permeability pathways and confinement in synthetic carboxysome shells. (PNAS 2024)

- DOI: 10.1073/pnas.2402277121 | PMCID: PMC11551347 | PMID: 39485798
- Evidence: After a brief equilibration period utilizing NAMD 2.14 ( 71 ), each simulation was converted using TopoGromacs ( 72 ) to GROMACS ( 73 ) for production simulations, which were 3 replicates for 500 ns each.
- Full pipeline: simulation/modelling [GROMACS, NAMD v2.14, VMD] -> stage not stated [Matplotlib, NumPy, SciPy]

### Intrinsically disordered region amplifies membrane remodeling to augment selective ER-phagy. (PNAS 2024)

- DOI: 10.1073/pnas.2408071121 | PMCID: PMC11536123 | PMID: 39453744
- Evidence: All MD simulations, including energy minimization, equilibrations (NVT and NPT), and production runs, were performed with GROningen MAchine for Chemical Simulations (GROMACS) v2021.5 ( 52 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, CellProfiler, MDAnalysis]

### Optogenetically engineered Septin-7 enhances immune cell infiltration of tumor spheroids. (PNAS 2024)

- DOI: 10.1073/pnas.2405717121 | PMCID: PMC11536090 | PMID: 39441641
- Evidence: After simulations, we calculated the distance between residues at the insertion site using GROMACS ( 66 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> differential/statistical testing [R v3.5.2] -> simulation/modelling [GROMACS] -> visualisation [Jupyter] -> stage not stated [ImageJ v1.52, PyMOL]

### CD73 promotes non-small cell lung cancer metastasis by regulating Axl signaling independent of GAS6. (PNAS 2024)

- DOI: 10.1073/pnas.2404709121 | PMCID: PMC11513981 | PMID: 39423241
- Version used: **2018.4**
- Evidence: MD stimulation of the Axl-CD73 complex was carried out using Gromacs 2018.4 package, applying the Amber14SB all-atom force field combining the TIP3P water model.
- Full pipeline: simulation/modelling [GROMACS v2018.4]

### A molten globule ensemble primes Arf1-GDP for the nucleotide switch. (PNAS 2024)

- DOI: 10.1073/pnas.2413100121 | PMCID: PMC11441498 | PMID: 39292747
- Version used: **4.5.4**
- Evidence: Using these fractional contact maps as bias on the topology of the protein, the conformational ensemble was generated at various pressures using 50 ns C α coarse-grained simulations as previously described ( 50 ) using Gromacs 4.5.4 ( 85 ).
- Full pipeline: simulation/modelling [GROMACS v4.5.4]

### Conformational ensembles in &lt;i&gt;Klebsiella pneumoniae&lt;/i&gt; FimH impact uropathogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2409655121 | PMCID: PMC11441496 | PMID: 39288182
- Version used: **2020.1**
- Evidence: Molecular dynamics simulations were run with Gromacs 2020.1 ( 51 – 53 ) using the FAST algorithm ( 54 ).
- Full pipeline: read trimming [PHENIX] -> simulation/modelling [GROMACS v2020.1] -> structure determination [PHENIX]

### Quantitative insights into the mechanism of proton conduction and selectivity for the human voltage-gated proton channel Hv1. (PNAS 2024)

- DOI: 10.1073/pnas.2407479121 | PMCID: PMC11420211 | PMID: 39259593
- Evidence: Models were built and equilibrated using a standard protocol in CHARMM-GUI ( 64 ) and simulations were performed in GROMACS ( 65 , 66 ) version 2020.4 with the Velocity Verlet integrator using a time step of 2 fs in the isothermal–isobaric [constant particle Number, Pressure, Temperature (NPT)] ensemble using a semi-isotropic Parrinello–Rahman barostat ( 67 ) at 1 atm and a velocity rescaling ther...
- Full pipeline: normalisation [GROMACS] -> simulation/modelling [GROMACS, LAMMPS]

### Molecular-level design of alternative media for energy-saving pilot-scale fibrillation of nanocellulose. (PNAS 2024)

- DOI: 10.1073/pnas.2405107121 | PMCID: PMC11406261 | PMID: 39236244
- Evidence: We used the GROMACS program ( 52 ) and the CHARMM36 force fields for cellulose ( 53 , 54 ) and for small molecules ( 55 , 56 ) other than water, for which the TIP3P model ( 57 ) was used.
- Full pipeline: simulation/modelling [GROMACS, VMD]

### Cryo-EM structures of a mycobacterial ABC transporter that mediates rifampicin resistance. (PNAS 2024)

- DOI: 10.1073/pnas.2403421121 | PMCID: PMC11406275 | PMID: 39226350
- Version used: **2022.2**
- Evidence: We then performed the energy minimization using the steepest descent method implemented in the GROMACS 2022.2 package ( 68 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, GROMACS v2022.2, PyMOL, UCSF Chimera]

### Perpendicular crossing chains enable high mobility in a noncrystalline conjugated polymer. (PNAS 2024)

- DOI: 10.1073/pnas.2403879121 | PMCID: PMC11406284 | PMID: 39226361
- Evidence: All MD simulations were carried out in GROMACS 2018 ( 55 ).
- Full pipeline: simulation/modelling [GROMACS]

### Sound-mediated nucleation and growth of amyloid fibrils. (PNAS 2024)

- DOI: 10.1073/pnas.2315510121 | PMCID: PMC11348332 | PMID: 39133851
- Version used: **2022.1**
- Evidence: Gromacs 2022.1 was used with the Amber99SB-ILDN force field and the SPCE water model.
- Full pipeline: differential/statistical testing [ImageJ] -> simulation/modelling [GROMACS v2022.1] -> visualisation [ChimeraX]

### Plasticity of the selectivity filter is essential for permeation in lysosomal TPC2 channels. (PNAS 2024)

- DOI: 10.1073/pnas.2320153121 | PMCID: PMC11317647 | PMID: 39074274
- Evidence: MD simulations were performed with the GROMACS software package ( 65 ), version 2021 and the REST simulations were conducted using GROMACS, version 2021, patched with PLUMED, version 2.7 ( 66 ).
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.7, Python, VMD] -> visualisation [VMD] -> stage not stated [MDAnalysis]

### Entropy drives the ligand recognition in G-protein-coupled receptor subtypes. (PNAS 2024)

- DOI: 10.1073/pnas.2401091121 | PMCID: PMC11287286 | PMID: 39024109
- Evidence: MD and metadynamics simulations were performed using GROMACS ( 55 ) and PLUMED ( 56 ).
- Full pipeline: simulation/modelling [GROMACS, PLUMED]

### Structure-based investigation of a DNA aptamer targeting PTK7 reveals an intricate 3D fold guiding functional optimization. (PNAS 2024)

- DOI: 10.1073/pnas.2404060121 | PMCID: PMC11260122 | PMID: 38985770
- Version used: **2021.7**
- Evidence: The DNA structure was calculated by rMD simulations on GROMACS 2021.7 using NOE-derived distance restraints, as well as hydrogen bond distance, hydrogen bond angle, and planarity restraints for Watson–Crick base pairs in 2-41, 3-40, 4-39, 5-38, 6-37, 9-13, 10-12, 18-36, 19-35, and 20-34.
- Full pipeline: simulation/modelling [GROMACS v2021.7, VMD] -> visualisation [PyMOL, VMD]

### Mechanism of phosphate release from actin filaments. (PNAS 2024)

- DOI: 10.1073/pnas.2408156121 | PMCID: PMC11260136 | PMID: 38980907
- Version used: **2020.4**
- Evidence: Simulations were performed by using GROMACS 2020.4 compiled with PLUMED 2.4.
- Full pipeline: simulation/modelling [GROMACS v2020.4, PLUMED v2.4, PyMOL, Python] -> stage not stated [VMD]

### Superior sodiophilicity and molecule crowding of crown ether boost the electrochemical performance of all-climate sodium-ion batteries. (PNAS 2024)

- DOI: 10.1073/pnas.2312337121 | PMCID: PMC11228459 | PMID: 38923987
- Evidence: The Gromacs program was used to perform MD calculations.
- Full pipeline: stage not stated [GROMACS]

### Structural determinants of ivabradine block of the open pore of HCN4. (PNAS 2024)

- DOI: 10.1073/pnas.2402259121 | PMCID: PMC11228525 | PMID: 38917012
- Evidence: As detailed in SI Appendix , simulations were conducted using GROMACS with the Amber99sb*-ILDN force field for the protein together with the GAFF2 parameters for IVA+/neutral IVA.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [PHENIX] -> stage not stated [RELION]

### Unraveling dynamic protein structures by two-dimensional infrared spectra with a pretrained machine learning model. (PNAS 2024)

- DOI: 10.1073/pnas.2409257121 | PMCID: PMC11228460 | PMID: 38917009
- Evidence: To capture the dynamic conformations, MD simulations were conducted for each protein using the Gromacs ( 60 ) software, with detailed settings provided below.
- Full pipeline: dimensionality reduction/clustering [AlphaFold, RoseTTAFold] -> simulation/modelling [GROMACS] -> machine learning [AlphaFold, RoseTTAFold]

### Transient interactions modulate the affinity of NF-κB transcription factors for DNA. (PNAS 2024)

- DOI: 10.1073/pnas.2405555121 | PMCID: PMC11161749 | PMID: 38805268
- Version used: **2021.7**
- Evidence: GROMACS 2021.7 package ( 67 ) and AMBER ff19SB force field ( 68 ) with OL15 parameters for DNAs ( 69 ) were used in all simulations.
- Full pipeline: simulation/modelling [GROMACS v2021.7]

### Unplugging lateral fenestrations of NALCN reveals a hidden drug binding site within the pore region. (PNAS 2024)

- DOI: 10.1073/pnas.2401591121 | PMCID: PMC11145269 | PMID: 38787877
- Version used: **2021.4**
- Evidence: Unbiased molecular dynamics (MD) simulation was conducted on the AAAA MT with 2-APB complex using Gromacs (version 2021.4) ( 68 ) with the primary aim to determine the optimal binding poses of 2-APB.
- Full pipeline: simulation/modelling [GROMACS v2021.4, VMD] -> stage not stated [PyMOL]

### CISD3/MiNT is required for complex I function, mitochondrial integrity, and skeletal muscle maintenance. (PNAS 2024)

- DOI: 10.1073/pnas.2405123121 | PMCID: PMC11145280 | PMID: 38781208
- Evidence: Movie of a GROMACS-generated trajectory of the CISD3-NDUFV2 complex from the SBM+DCA simulation with coevolutionary constraints.
- Full pipeline: alignment/mapping [HMMER] -> simulation/modelling [GROMACS] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold]

### Identification of the potassium-binding site in serotonin transporter. (PNAS 2024)

- DOI: 10.1073/pnas.2319384121 | PMCID: PMC11067047 | PMID: 38652746
- Version used: **2018.8**
- Evidence: In each case, the protein structure was placed in a hydrated palmitoylolyeoylphosphatidylcholine (POPC) lipid bilayer at a salt concentration of 0.15 M NaCl, which was then equilibrated at coarse-grained resolution using Gromacs v2018.8 ( 48 ) and the Martini v2.2 force field ( 49 ) for 50 µs.
- Full pipeline: simulation/modelling [GROMACS v2018.8, NAMD v2.13] -> stage not stated [Coot v0.8.9.3, VMD v1.9.3]

### C-type inactivation and proton modulation mechanisms of the TASK3 channel. (PNAS 2024)

- DOI: 10.1073/pnas.2320345121 | PMCID: PMC11046659 | PMID: 38630723
- Version used: **5.1.4**
- Evidence: All MD simulations were performed with GROMACS 5.1.4 ( 63 ) using the CHARMM36 force field ( 64 ).
- Full pipeline: registration [MotionCor2, RELION] -> simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> stage not stated [CTFFIND, ChimeraX, PyMOL]

### Lipid scrambling is a general feature of protein insertases. (PNAS 2024)

- DOI: 10.1073/pnas.2319476121 | PMCID: PMC11047089 | PMID: 38621120
- Evidence: Subsequently, CG-MD simulations were carried out using the GROMACS software, version 2019.6 ( 97 ), and the Martini 3 force field ( 98 ).
- Full pipeline: simulation/modelling [AlphaFold, GROMACS] -> stage not stated [ColabFold]

### Molecular mechanism underlying SNARE-mediated membrane fusion enlightened by all-atom molecular dynamics simulations. (PNAS 2024)

- DOI: 10.1073/pnas.2321447121 | PMCID: PMC11032479 | PMID: 38593076
- Evidence: All-atom MD simulations were performed using Gromacs ( 51 , 52 ) with the CHARMM36 force field ( 70 ).
- Full pipeline: simulation/modelling [GROMACS]

### Conformational free-energy landscapes of a Na<sup>+</sup>/Ca<sup>2+</sup> exchanger explain its alternating-access mechanism and functional specificity. (PNAS 2024)

- DOI: 10.1073/pnas.2318009121 | PMCID: PMC11032461 | PMID: 38588414
- Version used: **4.5.5**
- Evidence: Conventional and enhanced-sampling MD simulations were carried out using GROMACS2018 or GROMACS 4.5.5 with PLUMED ( 48 – 51 ), at constant temperature (298 K), pressure (1 bar) and periodic-boundary conditions.
- Full pipeline: simulation/modelling [GROMACS v4.5.5, PLUMED]

### Substrate recruitment via eIF2γ enhances catalytic efficiency of a holophosphatase that terminates the integrated stress response. (PNAS 2024)

- DOI: 10.1073/pnas.2320013121 | PMCID: PMC10998612 | PMID: 38547060
- Evidence: To refine the solvated constructs, each system underwent a 500-step energy minimization using the steepest descents algorithm, as implemented in GROMACS ( 45 ).
- Full pipeline: quantification [ImageJ] -> structure determination [GROMACS] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, ChimeraX v1.6.1, Coot v0.9.8.7, PHENIX v1.20.1, PyMOL v1.3]

### Elucidating the behavior of the SARS-CoV-2 virus surface at vapor-liquid interfaces using molecular dynamics simulation. (PNAS 2024)

- DOI: 10.1073/pnas.2317194121 | PMCID: PMC10990154 | PMID: 38502700
- Evidence: The simulations were carried out using the open source code GROMACS ( 11 ) Version 2022.
- Full pipeline: simulation/modelling [GROMACS]

### Elucidating the role of water in collagen self-assembly by isotopically modulating collagen hydration. (PNAS 2024)

- DOI: 10.1073/pnas.2313162121 | PMCID: PMC10945838 | PMID: 38451946
- Version used: **2020.4**
- Evidence: All simulations were run using the GROMACS 2020.4 software package ( 92 , 93 ), the CHARMM36m forcefield ( 94 ) and explicit solvent molecules, i.e., TIP3P for water and modified TIP3P-HW for heavy water ( 95 ).
- Full pipeline: simulation/modelling [GROMACS v2020.4, LAMMPS] -> stage not stated [ImageJ]

### Mechanism of proton-powered c-ring rotation in a mitochondrial ATP synthase. (PNAS 2024)

- DOI: 10.1073/pnas.2314199121 | PMCID: PMC10945847 | PMID: 38451940
- Version used: **2020.4**
- Evidence: MD simulations were run with GROMACS 2020.4 ( 69 ) using the CHARMM36m force-field ( 70 ).
- Full pipeline: simulation/modelling [GROMACS v2020.4, MDAnalysis, SciPy, scikit-learn] -> visualisation [Matplotlib, VMD] -> stage not stated [NetworkX]

### Data-driven classification of ligand unbinding pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2313542121 | PMCID: PMC10927508 | PMID: 38412121
- Version used: **2021.5**
- Evidence: Gas phase Alanine Dipeptide is modeled using AMBER99SB-ILDN force field and simulated at 300 K using the GROMACS v2021.5 package patched with PLUMED v2.9.
- Full pipeline: dimensionality reduction/clustering [Python] -> simulation/modelling [GROMACS v2021.5, PLUMED v2.9, Python]

### Mechanism and cellular function of direct membrane binding by the ESCRT and ERES-associated Ca<sup>2+</sup>-sensor ALG-2. (PNAS 2024)

- DOI: 10.1073/pnas.2318046121 | PMCID: PMC10907313 | PMID: 38386713
- Evidence: MD simulations were performed with GROMACS 2020 ( 33 ) using the CHARMM36m force field ( 34 ).
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis v2.0] -> stage not stated [AlphaFold, ChimeraX v1.3, ColabFold, ImageJ, OpenCV, PyMOL, Python, scikit-image]

### Homologous mutations in human β, embryonic, and perinatal muscle myosins have divergent effects on molecular power generation. (PNAS 2024)

- DOI: 10.1073/pnas.2315472121 | PMCID: PMC10907259 | PMID: 38377203
- Version used: **2022.4**
- Evidence: Preparation and simulation of all systems was done using GROMACS 2022.4 (ref.
- Full pipeline: simulation/modelling [GROMACS v2022.4, MDTraj, Python] -> stage not stated [scikit-learn]

### The elementary reactions for incorporation into crystals. (PNAS 2024)

- DOI: 10.1073/pnas.2320201121 | PMCID: PMC10873555 | PMID: 38315836
- Version used: **5.1.5**
- Evidence: We employed GROMACS 5.1.5 ( 95 ).
- Full pipeline: simulation/modelling [PLUMED v2.4.3] -> stage not stated [GROMACS v5.1.5]

### Molecular basis for human aquaporin inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2319682121 | PMCID: PMC10873552 | PMID: 38319972
- Evidence: All simulations were performed using GROMACS ( 26 ) software and the CHARMM36m force field ( 27 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### Highly parallelizable path sampling with minimal rejections using asynchronous replica exchange and infinite swaps. (PNAS 2024)

- DOI: 10.1073/pnas.2318731121 | PMCID: PMC10873605 | PMID: 38315841
- Evidence: The running of MD, engine input/output, and data storage are mainly handled by the PyRETIS functions that externally start and stop GROMACS/CP2K simulations.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [Dask]

### Regulation of anion-Na<sup>+</sup> coordination chemistry in electrolyte solvates for low-temperature sodium-ion batteries. (PNAS 2024)

- DOI: 10.1073/pnas.2316914121 | PMCID: PMC10835037 | PMID: 38252828
- Evidence: Molecular dynamics (MD) simulations were conducted by using the GROMACS package with AMBER03 force field ( 50 ).
- Full pipeline: simulation/modelling [GROMACS, VMD]

### High UV damage and low repair, but not cytosine deamination, stimulate mutation hotspots at ETS binding sites in melanoma. (PNAS 2024)

- DOI: 10.1073/pnas.2310854121 | PMCID: PMC10823218 | PMID: 38241433
- Evidence: The MD simulations were done in GROMACS software package ( 54 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, Python] -> simulation/modelling [GROMACS, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [BEDTools, SAMtools]

### Interfacial solvation-structure regulation for stable Li metal anode by a desolvation coating technique. (PNAS 2024)

- DOI: 10.1073/pnas.2311732121 | PMCID: PMC10823240 | PMID: 38232289
- Version used: **2016.3**
- Evidence: All MD simulations were carried out based on the OPLS/AA force field database ( 43 , 44 ) from GROMACS, v2016.3.
- Full pipeline: simulation/modelling [GROMACS v2016.3]

### A structurally precise mechanism links an epilepsy-associated <i>KCNC2</i> potassium channel mutation to interneuron dysfunction. (PNAS 2024)

- DOI: 10.1073/pnas.2307776121 | PMCID: PMC10801864 | PMID: 38194456
- Version used: **2022.1**
- Evidence: All simulations were simulated with a 2 fs timestep using the CHARMM36m forcefield in GROMACS 2022.1 ( https://doi.org/10.5281/zenodo.6103835 ).
- Full pipeline: simulation/modelling [GROMACS v2022.1] -> stage not stated [AlphaFold, PyMOL]

### B56δ long-disordered arms form a dynamic PP2A regulation interface coupled with global allostery and Jordan's syndrome mutations. (PNAS 2024)

- DOI: 10.1073/pnas.2310727120 | PMCID: PMC10769853 | PMID: 38150499
- Evidence: Molecular dynamics (MD) simulations were performed using Gromacs ( 66 ) patched with PLUMED 2.8.0 in the Amber ff14SB forcefield ( 67 ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [GROMACS, PLUMED v2.8.0] -> structure determination [PHENIX]

### Arg-Tyr cation-π interactions drive phase separation and β-sheet assembly in native spider dragline silk. (PNAS 2025)

- DOI: 10.1073/pnas.2523198122 | PMCID: PMC12772222 | PMID: 41433062
- Evidence: Molecular dynamics simulations (1 µs) were conducted using GROMACS with the CHARMM36m force field, and structural models were generated with ColabFold and AlphaFold3.
- Full pipeline: simulation/modelling [AlphaFold, ColabFold, GROMACS]

### Molecular mechanism of substrate transport by human peroxisomal ABCD3. (PNAS 2025)

- DOI: 10.1073/pnas.2513928122 | PMCID: PMC12772208 | PMID: 41428872
- Evidence: All-atom molecular dynamics (MD) simulations were performed to investigate the protein and substrate dynamics within a lipid bilayer environment using the GROMACS simulation package ( 48 ) and the CHARMM36 force field ( 49 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX]

### Physical exercise increases binding of POMC to blood extracellular vesicles. (PNAS 2025)

- DOI: 10.1073/pnas.2525044122 | PMCID: PMC12745691 | PMID: 41400998
- Version used: **2021.3**
- Evidence: The solvent accessible surface areas (SASA) analysis was carried out through the gmx sasa module of GROMACS v2021.3 ( 65 ) using the default parameter settings.
- Full pipeline: stage not stated [AlphaFold, GROMACS v2021.3, R v4.3]

### Data-driven enhanced sampling of mechanistic pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2517169122 | PMCID: PMC12704791 | PMID: 41343671
- Evidence: Materials and Methods All atomistic simulations were performed using the GROMACS package patched with the PLUMED 2.11.0-dev git: 9045979ca (PLUMED v2.11) ( 72 ) package.
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.11.0] -> machine learning [PyTorch]

### Machine learning enables de novo multiepitope design of &lt;i&gt;Plasmodium falciparum&lt;/i&gt; circumsporozoite protein to target trimeric L9 antibody. (PNAS 2025)

- DOI: 10.1073/pnas.2512358122 | PMCID: PMC12704715 | PMID: 41337490
- Version used: **2023.2**
- Evidence: All-atom MD simulations were performed using GROMACS v2023.2 ( 49 ) using the AMBER99SB-ILDN protein force field ( 50 ) with the TIP3P ( 51 ) water model.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2023.2] -> structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX, PyMOL, RELION v5.0]

### Small siphophage binding to an open state of the LptDE outer membrane lipopolysaccharide translocon. (PNAS 2025)

- DOI: 10.1073/pnas.2516650122 | PMCID: PMC12685063 | PMID: 41296721
- Evidence: All simulations used the CHARMM36m ( 62 ) forcefield and MD simulations were performed using the GROMACS ( 63 ) software package (version 2022.4).
- Full pipeline: alignment/mapping [PyMOL] -> quantification [ImageJ] -> simulation/modelling [GROMACS] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [Coot, MDAnalysis, MDTraj]

### SurFlex microscopy: Measuring flexibility of surface-tethered biomolecules. (PNAS 2025)

- DOI: 10.1073/pnas.2508828122 | PMCID: PMC12685047 | PMID: 41289389
- Evidence: To determine the effect of sequence specific interactions between the tip bases of DNA oligomers and the attached fluorophore, we conducted all-atom molecular dynamic simulations using GROMACS.
- Full pipeline: simulation/modelling [GROMACS]

### Reaching the full potential of cryo-EM reconstructions with molecular dynamics simulations at 310 K: Actin filaments as an example. (PNAS 2025)

- DOI: 10.1073/pnas.2521421122 | PMCID: PMC12685034 | PMID: 41289381
- Version used: **2021.5**
- Evidence: All the MD simulations were performed using GROMACS 2021.5 ( 71 ) with PLUMED 2.7 ( 72 ).
- Full pipeline: simulation/modelling [GROMACS v2021.5, PLUMED v2.7]

### Mechanisms of transport and analgesic compounds recognition by glycine transporter 2. (PNAS 2025)

- DOI: 10.1073/pnas.2506722122 | PMCID: PMC12685064 | PMID: 41284875
- Evidence: All simulations were performed using Gromacs v2021 ( 95 ), with the system parameterized using the Amber14SB force field ( 96 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [PHENIX, VMD]

### A cell-based scrambling assay reveals the phospholipid headgroup preference of TMEM16F on the plasma membrane. (PNAS 2025)

- DOI: 10.1073/pnas.2516822122 | PMCID: PMC12595458 | PMID: 41166415
- Version used: **2023.3**
- Evidence: CGMD simulations were performed using the Martini 3.0.0 force field ( 70 ) and Gromacs 2023.3 ( 71 ) using a 20 fs time step.
- Full pipeline: simulation/modelling [GROMACS v2023.3]

### Transcriptional condensates encode a "golden mean" to optimize enhancer-promoter communication across genomic distances. (PNAS 2025)

- DOI: 10.1073/pnas.2513371122 | PMCID: PMC12582294 | PMID: 41134621
- Version used: **4.5.7**
- Evidence: All MD simulations were conducted using Gromacs (version 4.5.7) ( 85 ), with the Plumed plugin (version 2.5.0) ( 86 ) to implement spherical confinement.
- Full pipeline: dimensionality reduction/clustering [Python] -> simulation/modelling [GROMACS v4.5.7, PLUMED, Python]

### Asymmetric gating of a homopentameric ion channel GLIC revealed by cryo-EM. (PNAS 2025)

- DOI: 10.1073/pnas.2512811122 | PMCID: PMC12582304 | PMID: 41129221
- Version used: **2021.5**
- Evidence: Molecular dynamics (MD) simulations were performed with GROMACS 2021.5 ( 79 , 99 – 105 ), using a 2 fs integration time-step.
- Full pipeline: alignment/mapping [Coot v0.9.8.7] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.9.8.7, PHENIX, RELION v4.0.1] -> stage not stated [ChimeraX]

### Driving forces of RNA condensation revealed through coarse-grained modeling with explicit Mg&lt;sup&gt;2&lt;/sup&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504583122 | PMCID: PMC12582263 | PMID: 41129218
- Evidence: Materials and Methods All atomistic simulations were performed using the GROMACS 2022 package ( 118 – 120 ) in the NPT ensemble.
- Full pipeline: simulation/modelling [GROMACS, OpenMM v8.1.0]

### Apusomonad rhodopsins: A new family of ultraviolet to blue light-absorbing rhodopsin channels. (PNAS 2025)

- DOI: 10.1073/pnas.2510619122 | PMCID: PMC12557545 | PMID: 41082663
- Version used: **4.5.7**
- Evidence: The structures were hydrated with Dowser-3 ( 99 ) and minimized with GROMACS v.4.5.7 ( 100 , 101 ) as implemented in the preparatory steps of the PyARM workflow ( 102 ).
- Full pipeline: read trimming [IQ-TREE v1.6.11, MAFFT] -> alignment/mapping [IQ-TREE v1.6.11, MAFFT] -> differential/statistical testing [IQ-TREE v1.6.11] -> structure determination [IQ-TREE v1.6.11] -> stage not stated [AlphaFold, BLAST, GROMACS v4.5.7]

### Temperature adaptation in structure and function in lactate dehydrogenase-A reflects convergent evolution in a few key protein regions. (PNAS 2025)

- DOI: 10.1073/pnas.2517759122 | PMCID: PMC12557798 | PMID: 41071662
- Version used: **2021.3**
- Evidence: Molecular dynamics were calculated in Gromacs v2021.3 ( 41 ) using the OPLS-AA/M force field ( 7 ).
- Full pipeline: alignment/mapping [MAFFT v7.487, R] -> simulation/modelling [GROMACS v2021.3, XGBoost] -> machine learning [TensorFlow] -> stage not stated [AlphaFold, BLAST v2.13.0, ColabFold v1.5, VMD]

### Design principles of the common Gly-X6-Gly membrane protein building block. (PNAS 2025)

- DOI: 10.1073/pnas.2503134122 | PMCID: PMC12541321 | PMID: 41055983
- Evidence: MD simulations were prepared in Charmm-GUI ( 66 ) and run using GROMACS ( 67 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, PHENIX]

### A fixed mutation in the respiratory complex I impairs mitochondrial bioenergetics in the endangered Apennine brown bear. (PNAS 2025)

- DOI: 10.1073/pnas.2504409122 | PMCID: PMC12519208 | PMID: 41026818
- Version used: **2022.3**
- Evidence: The MD simulations were performed using the GROMACS 2022.3 software using the CHARMM36m force field ( 28 , 73 ).
- Full pipeline: simulation/modelling [GROMACS v2022.3] -> visualisation [ChimeraX v1.7, VMD] -> stage not stated [AlphaFold, ImageJ]

### Directed evolution of a plant Rubisco chaperone with altered client recognition. (PNAS 2025)

- DOI: 10.1073/pnas.2510701122 | PMCID: PMC12452902 | PMID: 40932770
- Version used: **2022.5**
- Evidence: All simulations were conducted using GROMACS 2022.5 software ( 36 ) and the CHARMM36m force field ( 37 ).
- Full pipeline: simulation/modelling [GROMACS v2022.5] -> stage not stated [ImageJ]

### A unified model of transient poration induced by antimicrobial peptides. (PNAS 2025)

- DOI: 10.1073/pnas.2510294122 | PMCID: PMC12415194 | PMID: 40880531
- Version used: **2021.2**
- Evidence: US calculations used the extended pore reaction coordinate ξ ( 76 , 77 ), implemented via a custom version of GROMACS 2021.2.
- Full pipeline: simulation/modelling [OpenMM v7.4.1] -> stage not stated [GROMACS v2021.2, VMD]

### STAGE: A compact and versatile TnpB-based genome editing toolkit for &lt;i&gt;Streptomyces&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2509146122 | PMCID: PMC12415229 | PMID: 40857323
- Version used: **2025.1**
- Evidence: MD simulations were carried out with the GROMACS 2025.1 software suite ( 58 ), and dynamics cross-correlation matrices were subsequently calculated for structural analysis.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS v2025.1] -> stage not stated [AlphaFold v3.0, ChimeraX]

### STIM1 transmembrane helix dimerization captured by AI-guided transition path sampling. (PNAS 2025)

- DOI: 10.1073/pnas.2506516122 | PMCID: PMC12415195 | PMID: 40857319
- Version used: **2020.6**
- Evidence: Simulations were carried out with GROMACS 2020.6 ( 86 – 89 ) and the CHARMM36m force field ( 90 , 91 ).
- Full pipeline: normalisation [PyTorch] -> simulation/modelling [GROMACS v2020.6, MDAnalysis, MDTraj, NumPy, SciPy] -> machine learning [PyTorch]

### Structural basis and affinity improvement for an ATP-binding DNA aptamer. (PNAS 2025)

- DOI: 10.1073/pnas.2506491122 | PMCID: PMC12377721 | PMID: 40811466
- Version used: **2021.7**
- Evidence: The DNA structure was calculated by rMD simulations on GROMACS 2021.7 ( 44 ) using NOE-derived distance restraints in time averaging form ( 45 ), as well as backbone restraints, hydrogen bond distance, and planarity restraints for Watson–Crick base pairs in 1-34, 2-33, 3-32, 4-31, 7-29, 8-28, 16-26, 17-25, 18-24, and 19-23.
- Full pipeline: simulation/modelling [GROMACS v2021.7] -> visualisation [PyMOL] -> stage not stated [AlphaFold, VMD]

### Atomistic mechanisms of calcium permeation modulated by Q/R editing and selectivity filter mutations in GluA2 AMPA receptors. (PNAS 2025)

- DOI: 10.1073/pnas.2425172122 | PMCID: PMC12377769 | PMID: 40811461
- Evidence: For our all-atom MD simulations, we employed the GROMACS software suite ( 62 ) version 2019.6.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis, VMD] -> visualisation [MDAnalysis, Matplotlib, VMD] -> stage not stated [PyMOL]

### Computational investigation of water glasses using machine-learning potentials. (PNAS 2025)

- DOI: 10.1073/pnas.2509609122 | PMCID: PMC12358917 | PMID: 40763030
- Version used: **2019.6**
- Evidence: Initial configurations for ice Ih were generated with proton disorder using the GenIce2 ( 95 ) package, while liquid configurations were generated by the Gromacs version 2019.6 ( 96 ) insert-molecules tool before subsequent equilibration.
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [GROMACS v2019.6]

### Nonsubstrate PI(4,5)P<sub>2</sub> interacts with the interdomain linker to control electrochemical coupling in voltage-sensing phosphatase (VSP). (PNAS 2025)

- DOI: 10.1073/pnas.2500651122 | PMCID: PMC12337349 | PMID: 40729387
- Evidence: MD simulations were performed by using GROMACS program ( 62 ).
- Full pipeline: simulation/modelling [GROMACS, VMD] -> visualisation [PyMOL, VMD] -> stage not stated [ColabFold]

### Amino acid transfer free energies reveal thermodynamic driving forces in biomolecular condensate formation. (PNAS 2025)

- DOI: 10.1073/pnas.2425422122 | PMCID: PMC12318233 | PMID: 40690668
- Evidence: Alchemical free energy calculations were performed in GROMACS-2021.5 ( 90 ).
- Full pipeline: stage not stated [GROMACS]

### Microscopic and structural observations of actin filament capping and severing by cytochalasin D. (PNAS 2025)

- DOI: 10.1073/pnas.2502164122 | PMCID: PMC12304888 | PMID: 40658853
- Version used: **2023.1**
- Evidence: MD simulations were performed using the GROMACS 2023.1 ( 62 ) with CHARMM36-jul2021 force field ( 63 ) and TIP3p force field ( 64 ) on FUJITSU PRIMERGY CX2570 M5 computer at Nagoya University Information and Communications.
- Full pipeline: simulation/modelling [GROMACS v2023.1] -> structure determination [PHENIX] -> machine learning [PHENIX] -> visualisation [PyMOL] -> stage not stated [Coot, ImageJ]

### Unveiling the charge transport blockade in the D2 branch of the photosystem II reaction center. (PNAS 2025)

- DOI: 10.1073/pnas.2405023122 | PMCID: PMC12280951 | PMID: 40627392
- Evidence: Once the whole structure is complete, the topology file for different protein chains was generated using the pdb2gmx module of GROMACS 2022 ( 56 ).
- Full pipeline: stage not stated [GROMACS]

### Structure-based discovery of positive allosteric modulators of the A&lt;sub&gt;1&lt;/sub&gt; adenosine receptor. (PNAS 2025)

- DOI: 10.1073/pnas.2421687122 | PMCID: PMC12280925 | PMID: 40623180
- Evidence: MD simulations of the A 1 R were performed in NAMD whereas simulations of the P2Y 1 and FFA 1 receptors were performed in GROMACS ( 20 , 21 ).
- Full pipeline: dimensionality reduction/clustering [RDKit] -> simulation/modelling [GROMACS, NAMD]

### De novo design of D-peptide ligands: Application to influenza virus hemagglutinin. (PNAS 2025)

- DOI: 10.1073/pnas.2426554122 | PMCID: PMC12232713 | PMID: 40577121
- Evidence: Single mutations were accepted and added to the design pool if ∆∆G was smaller than −0.5 RU, solvent accessible surface area, as calculated by GROMACS ( 48 ), was larger than 1,100 Å 2 , and the total number of mutations (N mut ) was not larger than 10.
- Full pipeline: structure determination [PHENIX] -> stage not stated [GROMACS]

### Enzymatic carbon-fluorine bond cleavage by human gut microbes. (PNAS 2025)

- DOI: 10.1073/pnas.2504122122 | PMCID: PMC12184663 | PMID: 40512801
- Evidence: MD simulations were performed using the GROMACS package version 2022.5 ( 71 , 72 ) compiled with CUDA support and run on NVIDIA GeForce RTX 2080 Ti graphic cards.
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [R] -> simulation/modelling [AlphaFold, GROMACS] -> visualisation [Cytoscape] -> stage not stated [ColabFold, IQ-TREE]

### Deciphering Ca&lt;sup&gt;&lt;b&gt;2+&lt;/b&gt;&lt;/sup&gt; permeation and valence selectivity in Ca&lt;sub&gt;V&lt;/sub&gt;1: Molecular dynamics simulations reveal the three-ion knock-on mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2424694122 | PMCID: PMC12146731 | PMID: 40440072
- Version used: **2021.2**
- Evidence: The MD simulations were performed with the program GROMACS version 2021.2 ( 70 ), using the CHARMM36m force field ( 71 ) and CHARMM TIP3P water model.
- Full pipeline: quantification [PLUMED] -> simulation/modelling [GROMACS v2021.2, MDAnalysis, PLUMED] -> structure determination [VMD] -> visualisation [PyMOL] -> stage not stated [NetworkX]

### Microtubule dynamics are defined by conformations and stability of clustered protofilaments. (PNAS 2025)

- DOI: 10.1073/pnas.2424263122 | PMCID: PMC12146719 | PMID: 40440074
- Evidence: Data, Materials, and Software Availability All MD simulations were done using GROMACS 2023 ( 94 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> simulation/modelling [GROMACS, VMD] -> structure determination [IMOD, MotionCor2] -> visualisation [VMD] -> stage not stated [Matplotlib v3.8.2, NumPy v1.26, Python v3.9, SciPy v1.11, seaborn v0.13]

### Effective polarization in potassium channel simulations: Ion conductance, occupancy, voltage response, and selectivity. (PNAS 2025)

- DOI: 10.1073/pnas.2423866122 | PMCID: PMC12130843 | PMID: 40392847
- Version used: **2022.5**
- Evidence: The ion solvation free energy calculation was performed using Gromacs 2022.5.
- Full pipeline: alignment/mapping [PyMOL] -> stage not stated [GROMACS v2022.5]

### Caveolin assemblies displace one bilayer leaflet to organize and bend membranes. (PNAS 2025)

- DOI: 10.1073/pnas.2417024122 | PMCID: PMC12107156 | PMID: 40359049
- Evidence: The systems were solvated and ionized with Gromacs.
- Full pipeline: simulation/modelling [VMD] -> stage not stated [GROMACS]

### Calcium-activated chloride channel TMEM16A opens via pi-helical transition in transmembrane segment 4. (PNAS 2025)

- DOI: 10.1073/pnas.2421900122 | PMCID: PMC12067253 | PMID: 40299692
- Evidence: The simulations were performed using GROMACS ( 63 ) version 2021, with a time step of 2 fs.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS, PyMOL v2.5] -> stage not stated [AlphaFold, ImageJ, MDAnalysis]

### Water-directed pinning is key to tau prion formation. (PNAS 2025)

- DOI: 10.1073/pnas.2421391122 | PMCID: PMC12067210 | PMID: 40294272
- Evidence: All replica-exchange molecular dynamics (REMD) simulations of the jR2R3 and jR2R3-P301L peptides were performed using the Gromacs package (versions 2019.6 and 2020.1) ( 80 , 81 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [PHENIX, RELION]

### Exploring RNA destabilization mechanisms in biomolecular condensates through atomistic simulations. (PNAS 2025)

- DOI: 10.1073/pnas.2425261122 | PMCID: PMC12012522 | PMID: 40203038
- Version used: **2021.4**
- Evidence: Materials and Methods MD simulations were performed using GROMACS 2021.4 ( 65 ) patched with PLUMED 2.8 ( 66 , 67 ) to perform Well-Tempered Metadynamics ( 44 ) (WT-MetaD) and using a general Hamiltonian replica exchange implementation ( 68 ).
- Full pipeline: simulation/modelling [GROMACS v2021.4, PLUMED v2.8]

### Uniform elementary fibrils in diverse plant cell walls. (PNAS 2025)

- DOI: 10.1073/pnas.2426467122 | PMCID: PMC12012456 | PMID: 40193604
- Version used: **2021.1**
- Evidence: All-atom MD simulations were conducted using GROMACS version 2021.1, which employs the CHARMM carbohydrate force field ( 46 , 47 ).
- Full pipeline: simulation/modelling [GROMACS v2021.1] -> visualisation [PyMOL]

### Alpha-tubulin tails regulate axoneme differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2414731122 | PMCID: PMC12012489 | PMID: 40198703
- Version used: **2024.2**
- Evidence: Simulations were performed using the GROMACS 2024.2 software package with the CHARMM36m force field ( 56 ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [GROMACS v2024.2] -> visualisation [PyMOL v2.0] -> stage not stated [AlphaFold]

### Allosterically switchable network orients &lt;i&gt;β&lt;/i&gt;-flap in &lt;i&gt;Clostridioides difficile&lt;/i&gt; toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2419263122 | PMCID: PMC12002228 | PMID: 40172960
- Evidence: All molecular dynamics simulations were simulated with GROMACS ( 58 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, PLUMED]

### Following phospholipid transfer through the OmpF&lt;sub&gt;3&lt;/sub&gt;-MlaA-MlaC lipid shuttle with native mass spectrometry. (PNAS 2025)

- DOI: 10.1073/pnas.2420041122 | PMCID: PMC12002339 | PMID: 40168124
- Version used: **2022.5**
- Evidence: MD simulations were performed using GROMACS version 2022.5 ( 37 ).
- Full pipeline: simulation/modelling [GROMACS v2022.5] -> stage not stated [AlphaFold]

### Structural mechanisms underlying the modulation of CXCR4 by diverse small-molecule antagonists. (PNAS 2025)

- DOI: 10.1073/pnas.2425795122 | PMCID: PMC11929458 | PMID: 40063796
- Evidence: All systems’ MD simulations were carried out using the charmm36 force field topologies and parameters in the GROMACS software package (version 2021).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> stage not stated [RELION v5.0]

### Identifying the interactions conferring functional mechanical rigidity on RNase-resistant RNA from Zika virus. (PNAS 2025)

- DOI: 10.1073/pnas.2417234122 | PMCID: PMC11929477 | PMID: 40063803
- Evidence: All-atom MD simulations of the xrRNA were performed in the presence and absence of an external load force applied on the 5′ end, using the GROMACS package ( 50 , 51 ) with TIP3P explicit water and AMBER14 force fields, at a temperature of 310 K with a stochastic velocity rescaling thermostat.
- Full pipeline: quantification [ImageJ v1.8.0] -> normalisation [GROMACS] -> simulation/modelling [GROMACS]

### Molecular mechanism of Arp2/3 complex activation by nucleation-promoting factors and an actin monomer. (PNAS 2025)

- DOI: 10.1073/pnas.2421467122 | PMCID: PMC11912402 | PMID: 40048273
- Version used: **2021.5**
- Evidence: The AA MD simulations were carried out using Gromacs version 2021.5 ( 58 ).
- Full pipeline: simulation/modelling [GROMACS v2021.5]

### Hidden complexity of α7 nicotinic acetylcholine receptor desensitization revealed by MD simulations and Markov state modeling. (PNAS 2025)

- DOI: 10.1073/pnas.2420993122 | PMCID: PMC11848294 | PMID: 39946538
- Evidence: 2 ; and Gromacs input files, starting coordinates, topology, and parameters for running the all-atom MD simulations are available at Zenodo ( 82 ).
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Jupyter]

### Structural basis of disease mutation and substrate recognition by the human SLC2A9 transporter. (PNAS 2025)

- DOI: 10.1073/pnas.2418282122 | PMCID: PMC11848319 | PMID: 39937868
- Evidence: All-atom MDs simulations were performed using GROMACS ( 45 ) with the CHARMM36 force field ( 46 ) The protein was embedded in a POPC lipid bilayer using CHARMM-GUI ( 47 ) and solvated with TIP3P water and 150 mM NaCl.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX]

### Bacterial polysaccharide lyase family 33: Specificity from an evolutionarily conserved binding tunnel. (PNAS 2025)

- DOI: 10.1073/pnas.2421623122 | PMCID: PMC11848413 | PMID: 39932998
- Evidence: Eigenvector analysis was performed on the combined results with GROMACS and DynDom ( 30 ) used to characterize the maximum and minimum projected protein structures of the top three eigenvectors.
- Full pipeline: simulation/modelling [AlphaFold] -> structure determination [Coot] -> stage not stated [GROMACS]

### Subunit-specific conductance of single homomeric and heteromeric HCN pacemaker channels at femtosiemens resolution. (PNAS 2025)

- DOI: 10.1073/pnas.2422533122 | PMCID: PMC11804576 | PMID: 39879240
- Evidence: All the simulations were performed with GROMACS software package version 2023.3 ( 57 ) with 900 mM KCl.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis] -> visualisation [PyMOL, VMD]

### The &lt;i&gt;Aedes aegypti&lt;/i&gt; mosquito evolves two types of prophenoloxidases with diversified functions. (PNAS 2025)

- DOI: 10.1073/pnas.2413131122 | PMCID: PMC11761970 | PMID: 39808654
- Evidence: Protein–ligand complexes resulting from docking were validated through MD simulations using GROMACS (version 2021) ( 91 ).
- Full pipeline: alignment/mapping [MAFFT] -> simulation/modelling [GROMACS] -> stage not stated [AlphaFold, AutoDock Vina, ChimeraX v1.8]

### A room temperature rechargeable Li-LiNO&lt;sub&gt;3&lt;/sub&gt; battery with high capacity. (PNAS 2025)

- DOI: 10.1073/pnas.2416817122 | PMCID: PMC11760503 | PMID: 39805020
- Evidence: The molecular dynamics simulations were conducted by GROMACS with AMBER force field ( 25 ).
- Full pipeline: simulation/modelling [GROMACS, VMD]

### Sterol divergence across eukaryotic kingdoms determines membrane susceptibility to saponins, a class of plant defense compounds. (PNAS 2026)

- DOI: 10.1073/pnas.2523859123 | PMCID: PMC13168540 | PMID: 42101991
- Version used: **2021.5**
- Evidence: Simulations were conducted under physiological temperature and pressure conditions using GROMACS 2021.5 ( 61 – 63 ).
- Full pipeline: simulation/modelling [GROMACS v2021.5] -> stage not stated [PLUMED]

### Novel Knotted Solenoid fold with order-shifted coil arrangement leads to nontrivial 3&lt;sub&gt;1&lt;/sub&gt; topology. (PNAS 2026)

- DOI: 10.1073/pnas.2525920123 | PMCID: PMC13123833 | PMID: 42018416
- Version used: **2023.1**
- Evidence: The all-atom explicit solvent molecular dynamics simulations were performed in GROMACS 2023.1 software using the CHARMM36 force field.
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> simulation/modelling [GROMACS v2023.1] -> stage not stated [AlphaFold]

### Biomechanical anticoagulation by spherical platelets in extracorporeal systems. (PNAS 2026)

- DOI: 10.1073/pnas.2535113123 | PMCID: PMC13056125 | PMID: 41911452
- Evidence: An all-atom model of α IIb β 3 was developed using GROMACS ( 41 ) to investigate the biomechanical mechanisms underlying integrin unfolding under different motion conditions.
- Full pipeline: stage not stated [GROMACS]

### Direct evidence of acid-driven protein desolvation. (PNAS 2026)

- DOI: 10.1073/pnas.2525949123 | PMCID: PMC12974452 | PMID: 41785322
- Evidence: The phbuilder tool ( 82 ) was used to prepare the CpHMD simulations for the GROMACS software.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [ChimeraX, MDAnalysis, PHENIX] -> stage not stated [RELION, SciPy]

### Synaptic transmission: Munc13 assembles onto PI(4,5)P&lt;sub&gt;2&lt;/sub&gt;-rich domains into trimers that cooperate to capture vesicles. (PNAS 2026)

- DOI: 10.1073/pnas.2523347123 | PMCID: PMC12912961 | PMID: 41671179
- Evidence: All simulations were carried out using the GROMACS 2023 software package ( 54 ).
- Full pipeline: alignment/mapping [IMOD] -> quantification [ImageJ] -> registration [IMOD] -> dimensionality reduction/clustering [ImageJ] -> simulation/modelling [GROMACS] -> visualisation [Topaz] -> stage not stated [AlphaFold, VMD]

### OsKAT1 is a short Shaker potassium channel involved in root-to-shoot potassium translocation and contributes to rice grain yield. (PNAS 2026)

- DOI: 10.1073/pnas.2527650123 | PMCID: PMC12867649 | PMID: 41604258
- Evidence: Dynamic interactions between a classical C1-terminus and the C-linker were predicted with molecular dynamics simulation using Gromacs.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold]

### Proton-selective conductance and gating of the lysosomal cation channel TMEM175. (PNAS 2026)

- DOI: 10.1073/pnas.2503909123 | PMCID: PMC12818570 | PMID: 41533442
- Version used: **2021.5**
- Evidence: All simulations were run with Gromacs 2021.5 ( 29 ).
- Full pipeline: simulation/modelling [GROMACS v2021.5] -> stage not stated [ColabFold, VMD]

### A pothole-filling strategy for selective targeting of rCUG-repeats associated with myotonic dystrophy type 1. (PNAS 2026)

- DOI: 10.1073/pnas.2507065123 | PMCID: PMC12799113 | PMID: 41512040
- Evidence: All MD simulations were performed in GROMACS with a 2 fs time step.
- Full pipeline: quantification [ImageJ] -> simulation/modelling [GROMACS] -> stage not stated [CellProfiler]

### SARS-CoV-2 peptide fragments selectively dysregulate specific immune cell populations via Gaussian curvature targeting. (PNAS 2026)

- DOI: 10.1073/pnas.2521841122 | PMCID: PMC12799121 | PMID: 41505524
- Version used: **2018.3**
- Evidence: Molecular dynamics simulations were performed using GROMACS 2018.3.
- Full pipeline: simulation/modelling [GROMACS v2018.3]

### Controlled dynamic remodeling of the spliceosome active site enables the first step of splicing. (PNAS 2026)

- DOI: 10.1073/pnas.2522293123 | PMCID: PMC12773743 | PMID: 41474748
- Version used: **2023.3**
- Evidence: First, an energy minimization was performed using the steepest descent algorithm implemented in GROMACS 2023.3 ( 55 ), with harmonic positional restraints of 5,000 kJ/mol nm 2 applied to all heavy atoms and catalytic ions (M1, M2, K + ).
- Full pipeline: simulation/modelling [PLUMED v2.9, VMD] -> stage not stated [GROMACS v2023.3, PyMOL]

### Molecular determinants of ligand efficacy and potency in GPCR signaling. (Science 2023)

- DOI: 10.1126/science.adh1859 | PMCID: PMC7615523 | PMID: 38127743
- Evidence: In addition, we calculated the accessible surface area of the adrenaline binding site with and without the ligand present using MDTraj ( https://www.mdtraj.org ) and GROMACS ( https://www.gromacs.org/ ).
- Full pipeline: stage not stated [GROMACS, MDTraj, PyMOL v2.5.2, R v4.0, ggplot2, ggpubr, tidyverse]

### Structure and organization of AMPA receptor-TARP complexes in the mammalian cerebellum. (Science 2026)

- DOI: 10.1126/science.aeb3577 | PMCID: PMC7619101 | PMID: 41379938
- Evidence: ...ethod ( 97 ) adding water and 0.15 M Na + and Cl - ions, performing an initial energy minimization in CHARMM and preparing simulation input files for GROMACS.
- Full pipeline: alignment/mapping [MUSCLE] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [PyMOL v2.5] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

