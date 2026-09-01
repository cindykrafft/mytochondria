# MDAnalysis

- **Category:** md
- **Papers in survey:** 41
- **Journals:** PNAS (28), Nature (10), Cell (3)
- **Years:** 2021 (3), 2022 (5), 2023 (3), 2024 (12), 2025 (13), 2026 (5)
- **Versions named:** 2.7.0 (1), 2.0 (1), 2.4.3 (1), 0.20.1 (1)
- **Pipeline stages it appears in:** simulation/modelling (24), visualisation (5), structure determination (1)

## Papers

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ...hirts and Pande, 2000 ; Zimmerman et al., 2020 N/A IPython Perez and Granger, 2007 Version 7.14.0 Jupyter Notebook Kluyver et al., 2016 Version 6.1.5 MDAnalysis Michaud-Agrawal et al., 2011 ; Gowers et al., 2016 Version 1.0.0 NumPy https://numpy.org Version 1.19.1 OpenMM Eastman et al., 2017 Version 7.4.2 OpenMMTools https://github.com/choderalab/openmmtools Version 0.20.0 PyMOL Schrödinger Versio...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Evidence: ...20 Abraham et al., 2015 https://doi.org/10.1016/j.softx.2015.06.001 AMBER14SB force field Maier et al., 2015 https://doi.org/10.1021/acs.jctc.5b00255 MDAnalysis Michaud-Agrawal et al., 2011 https://doi.org/10.1002/jcc.21787 Alpha Fold Jumper et al., 2021 ; Varadi et al., 2022 https://doi.org/10.1038/s41586-021-03819-2 https://doi.org/10.1093/nar/gkab1061 VMD Humphrey et al., 1996 https://doi.org/1...
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### Structure of a fully assembled tumor-specific T cell receptor ligated by pMHC. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.010 | PMCID: PMC9630439 | PMID: 35985289
- Version used: **0.20.1**
- Evidence: ... N/A https://www.flowjo.com Gromacs v2020.6 Abraham et al., 2015 RRID: SCR_014565 Illustrate Goodsell et al., 2019 github.com/ccsb-scripps/Illustrate MDAnalysis v0.20.1 Gowers et al., 2016 github.com/MDAnalysis/mdanalysis/releases NumPy v1.19.5 Harris et al., 2020 RRID: SCR_008633 OPM database Lomize et al., 2012 RRID:SCR_011961 Phenix Liebschner et al., 2019 RRID:SCR_014224 Prism v9.2.0 N/A https...
- Full pipeline: simulation/modelling [ChimeraX, UCSF Chimera, VMD] -> stage not stated [CCP4, GROMACS v2020.6, MDAnalysis v0.20.1, NumPy v1.19.5, PHENIX, PyMOL]

### Visualizing protein breathing motions associated with aromatic ring flipping. (Nature 2022)

- DOI: 10.1038/s41586-022-04417-6 | PMCID: PMC8866124 | PMID: 35173330
- Evidence: Trajectories were processed and analysed using the MDAnalysis Python package 74 .
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, VMD]

### Inactivation of the Kv2.1 channel through electromechanical coupling. (Nature 2023)

- DOI: 10.1038/s41586-023-06582-8 | PMCID: PMC10567553 | PMID: 37758949
- Evidence: Pore radii were estimated using the MDAnalysis package (v.2.4.0) 74 implementation of the HOLE program (v.2.2.005) 75 , which reports the radius of the largest sphere that can fit in the pore without intersecting with a neighbouring atom.
- Full pipeline: structure determination [Coot v0.9.8.1, PHENIX v1.19.1, UCSF Chimera v1.15] -> visualisation [PyMOL v2.4.1] -> stage not stated [MDAnalysis, MotionCor2, RELION v3.0]

### Selective ion transport through hydrated micropores in polymer membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-08140-2 | PMCID: PMC11560840 | PMID: 39506120
- Evidence: Radial distribution functions RDFs, g ab ( r ) between two groups of atoms, a and b, within the polymer models were calculated using the MDAnalysis package over trajectories of 20 ns with frames every 10 ps.
- Full pipeline: simulation/modelling [MDAnalysis]

### The ribosome lowers the entropic penalty of protein folding. (Nature 2024)

- DOI: 10.1038/s41586-024-07784-4 | PMCID: PMC11374706 | PMID: 39112704
- Evidence: Thus, we calculated the R g from Cα atoms using MDAnalysis 122 and then converted it to R h using S20 R h = R g α 1 R g − α 2 N 0.33 N 0.60 − N 0.33 + α 3 N is the number of amino acids, α 1 takes a value of 0.216 Å −1 , α 2 takes a value of 4.06 Å, and α 3 has a value of 0.821.
- Full pipeline: simulation/modelling [GROMACS, PyMOL v2.3] -> structure determination [Python] -> stage not stated [ImageJ, MDAnalysis, MDTraj, SciPy]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Evidence: Visual molecular dynamics 58 and MDAnalysis 59 were used to visualize and analyse the trajectories, respectively.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### Design of facilitated dissociation enables timing of cytokine signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09549-z | PMCID: PMC12611780 | PMID: 40993395
- Evidence: Analysis of the trajectories, such as RMSD and root mean square fluctuation (RMSF) calculations, was performed with MDAnalysis 82 .
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [CCP4] -> differential/statistical testing [DESeq2] -> simulation/modelling [MDAnalysis] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> stage not stated [GROMACS v2020.2, PyMOL, RoseTTAFold]

### Complex water networks visualized by cryogenic electron microscopy of RNA. (Nature 2025)

- DOI: 10.1038/s41586-025-08855-w | PMCID: PMC12137144 | PMID: 40068818
- Evidence: The simulations were further analysed using custom scripts with MDAnalysis 81 , 82 including RMSF and distance calculations.
- Full pipeline: simulation/modelling [MDAnalysis] -> structure determination [ChimeraX v1.6.1] -> stage not stated [EMAN2, MotionCor2, RELION]

### Mis-splicing of a neuronal microexon promotes CPEB4 aggregation in ASD. (Nature 2025)

- DOI: 10.1038/s41586-024-08289-w | PMCID: PMC11711090 | PMID: 39633052
- Evidence: Simulation trajectories were analysed using MDTraj 70 (v.1.9.6) and MDAnalysis 71 , 72 (v.1.1).
- Full pipeline: simulation/modelling [MDAnalysis, MDTraj, OpenMM v7.5] -> visualisation [Fiji, ImageJ] -> stage not stated [VMD]

### Structural basis of fungal β-1,3-glucan synthase inhibition by caspofungin. (Nature 2026)

- DOI: 10.1038/s41586-026-10409-7 | PMCID: PMC13249079 | PMID: 42020744
- Version used: **2.7.0**
- Evidence: VMD (v.1.9) 66 was used for visualization of molecular dynamics simulation results; Python 3 and MDAnalysis (v.2.7.0) 67 were used to analyse molecular dynamics results and generate molecular dynamics-related figures.
- Full pipeline: alignment/mapping [UCSF Chimera] -> registration [RELION] -> simulation/modelling [GROMACS, MDAnalysis v2.7.0, Python, VMD v1.9] -> structure determination [Coot v0.98, UCSF Chimera] -> visualisation [MDAnalysis v2.7.0, Python, VMD v1.9] -> stage not stated [AlphaFold, ChimeraX v1.10, PHENIX v1.20, PyMOL v3.1]

### Computational enzyme design by catalytic motif scaffolding. (Nature 2026)

- DOI: 10.1038/s41586-025-09747-9 | PMCID: PMC12727513 | PMID: 41339546
- Evidence: The simulations were analysed using the MDAnalysis Python package version 2.8.0 (ref.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis] -> structure determination [PHENIX] -> stage not stated [AlphaFold, SciPy]

### Common sequence motifs of nascent chains engage the ribosome surface and trigger factor. (PNAS 2021)

- DOI: 10.1073/pnas.2103015118 | PMCID: PMC8719866 | PMID: 34930833
- Evidence: Interactions between the NC and the ribosome were calculated from the trajectory using MDAnalysis python library ( 67 ) and represented using a circular plot generated with Circos ( 68 ).
- Full pipeline: simulation/modelling [GROMACS v5.0.4, MDAnalysis, VMD]

### Dual nature of human ACE2 glycosylation in binding to SARS-CoV-2 spike. (PNAS 2021)

- DOI: 10.1073/pnas.2100425118 | PMCID: PMC8126795 | PMID: 33903171
- Evidence: The MD trajectories were analyzed with Visual Molecular Dynamics (VMD) ( 40 ) and MDAnalysis package ( 41 ).
- Full pipeline: simulation/modelling [GROMACS v2019.6, MDAnalysis, VMD]

### Intrinsically disordered ectodomain modulates ion permeation through a metal transporter. (PNAS 2022)

- DOI: 10.1073/pnas.2214602119 | PMCID: PMC9889885 | PMID: 36409899
- Evidence: Python packages MDTraj and MDAnalysis were used for trajectory analysis ( 49 , 50 ).
- Full pipeline: simulation/modelling [MDAnalysis, MDTraj] -> stage not stated [GROMACS, PLUMED v2.6.3, VMD]

### Differential interactions of resting, activated, and desensitized states of the α7 nicotinic acetylcholine receptor with lipidic modulators. (PNAS 2022)

- DOI: 10.1073/pnas.2208081119 | PMCID: PMC9618078 | PMID: 36251999
- Evidence: Visualizations were created in VMD ( 68 ); most analyses were performed with GROMACS and MDAnalysis ( 69 ) and plotted with RainCloudPlot ( 70 ) and Matplotlib ( 71 ).
- Full pipeline: simulation/modelling [GROMACS] -> visualisation [MDAnalysis, Matplotlib, VMD]

### Diversity of rhodopsin cyclases in zoospore-forming fungi. (PNAS 2023)

- DOI: 10.1073/pnas.2310600120 | PMCID: PMC10622942 | PMID: 37871207
- Version used: **2.4.3**
- Evidence: Hydrogen bond analysis of retinal, water, and the counterion-triad (E136, D140, and E262) was performed using the hydrogen bond analysis module in MDAnalysis 2.4.3 ( 37 ) with a distance cutoff of 3 Å for donor and acceptor and an angle cutoff of 150° for donor–hydrogen–acceptor.
- Full pipeline: read trimming [IQ-TREE, SPAdes v3.15.5] -> alignment/mapping [IQ-TREE] -> simulation/modelling [GROMACS v2019.3] -> visualisation [Matplotlib v3.4.3, PyMOL v2.4.1] -> stage not stated [AlphaFold, MDAnalysis v2.4.3]

### Electrolytes with moderate lithium polysulfide solubility for high-performance long-calendar-life lithium-sulfur batteries. (PNAS 2023)

- DOI: 10.1073/pnas.2301260120 | PMCID: PMC10400945 | PMID: 37487097
- Evidence: The solvation structure analysis was carried out using the MDAnalysis package ( 67 , 68 ).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [MDAnalysis]

### Dilated cardiomyopathy-associated skeletal muscle actin (ACTA1) mutation R256H disrupts actin structure and function and causes cardiomyocyte hypocontractility. (PNAS 2024)

- DOI: 10.1073/pnas.2405020121 | PMCID: PMC11572969 | PMID: 39503885
- Evidence: Data were analyzed using the MDAnalysis Python package ( 68 , 69 ).
- Full pipeline: simulation/modelling [NAMD v3.0] -> stage not stated [ImageJ, MDAnalysis, PyMOL]

### Intrinsically disordered region amplifies membrane remodeling to augment selective ER-phagy. (PNAS 2024)

- DOI: 10.1073/pnas.2408071121 | PMCID: PMC11536123 | PMID: 39453744
- Evidence: Contact maps for IDR–IDR, IDR–KALP 25 , and IDR–RHD interactions were obtained using in-house scripts implementing MDAnalysis ( 68 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, CellProfiler, MDAnalysis]

### Structural insights into KSHV-GPCR constitutive activation and CXCL1 chemokine recognition. (PNAS 2024)

- DOI: 10.1073/pnas.2403217121 | PMCID: PMC11494311 | PMID: 39378089
- Evidence: The analysis of the resulting trajectories was performed using MDAnalysis ( 35 ), visualization and image rendering were performed with PyMOL, and graphical representations were obtained with the Seaborn Package ( 36 ).
- Full pipeline: simulation/modelling [MDAnalysis, R v6.62, seaborn] -> structure determination [PHENIX] -> visualisation [MDAnalysis, PyMOL, seaborn]

### Blobs form during the single-file transport of proteins across nanopores. (PNAS 2024)

- DOI: 10.1073/pnas.2405018121 | PMCID: PMC11420176 | PMID: 39264741
- Evidence: 45 , according to the MDAnalysis Python (“G. van Rossum, Python tutorial, Technical Report CS-R9526, Centrum voor Wiskunde en Informatica (CWI), Amsterdam, May 1995.”) module ( 46 ) to probe the inner radius of each pore along their long axes.
- Full pipeline: structure determination [PHENIX] -> visualisation [Matplotlib, NumPy] -> stage not stated [ChimeraX, MDAnalysis, PyMOL]

### Plasticity of the selectivity filter is essential for permeation in lysosomal TPC2 channels. (PNAS 2024)

- DOI: 10.1073/pnas.2320153121 | PMCID: PMC11317647 | PMID: 39074274
- Evidence: The pore radius profiles of the channels were calculated using the HOLE program ( 67 ), implemented in the MDAnalysis package.
- Full pipeline: simulation/modelling [GROMACS, PLUMED v2.7, Python, VMD] -> visualisation [VMD] -> stage not stated [MDAnalysis]

### An α-ketoglutarate conformational switch controls iron accessibility, activation, and substrate selection of the human FTO protein. (PNAS 2024)

- DOI: 10.1073/pnas.2404457121 | PMCID: PMC11194561 | PMID: 38865275
- Evidence: 5 A during the simulations was calculated with MDAnalysis ( 56 ).
- Full pipeline: simulation/modelling [MDAnalysis, OpenMM] -> stage not stated [MDTraj]

### Molecular dynamics in multidimensional space explains how mutations affect the association path of neomycin to a riboswitch. (PNAS 2024)

- DOI: 10.1073/pnas.2317197121 | PMCID: PMC11009640 | PMID: 38579011
- Evidence: The binding paths were extracted with MDAnalysis ( 48 ).
- Full pipeline: stage not stated [MDAnalysis, Matplotlib]

### Mechanism of proton-powered c-ring rotation in a mitochondrial ATP synthase. (PNAS 2024)

- DOI: 10.1073/pnas.2314199121 | PMCID: PMC10945847 | PMID: 38451940
- Evidence: Water wires connecting residues aE288 and cE111A were identified by analyzing all stratified OOH simulations with the breadth-first algorithm implemented in MDAnalysis ( 76 , 77 ).
- Full pipeline: simulation/modelling [GROMACS v2020.4, MDAnalysis, SciPy, scikit-learn] -> visualisation [Matplotlib, VMD] -> stage not stated [NetworkX]

### Mechanism and cellular function of direct membrane binding by the ESCRT and ERES-associated Ca<sup>2+</sup>-sensor ALG-2. (PNAS 2024)

- DOI: 10.1073/pnas.2318046121 | PMCID: PMC10907313 | PMID: 38386713
- Version used: **2.0**
- Evidence: Simulation trajectories were analyzed through MDAnalysis 2.0 ( 44 , 45 ) in Python 3.6.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis v2.0] -> stage not stated [AlphaFold, ChimeraX v1.3, ColabFold, ImageJ, OpenCV, PyMOL, Python, scikit-image]

### Small siphophage binding to an open state of the LptDE outer membrane lipopolysaccharide translocon. (PNAS 2025)

- DOI: 10.1073/pnas.2516650122 | PMCID: PMC12685063 | PMID: 41296721
- Evidence: HOLE ( 39 , 64 ) was run using the HOLE2 implementation within the MDAnalysis ( 65 , 66 ).
- Full pipeline: alignment/mapping [PyMOL] -> quantification [ImageJ] -> simulation/modelling [GROMACS] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [Coot, MDAnalysis, MDTraj]

### STIM1 transmembrane helix dimerization captured by AI-guided transition path sampling. (PNAS 2025)

- DOI: 10.1073/pnas.2506516122 | PMCID: PMC12415195 | PMID: 40857319
- Evidence: Trajectory analysis was carried out using the pytraj ( 96 ), mdtraj ( 97 ), MDAnalysis ( 98 , 99 ), numpy ( 100 ), and SciPy ( 101 ) packages.
- Full pipeline: normalisation [PyTorch] -> simulation/modelling [GROMACS v2020.6, MDAnalysis, MDTraj, NumPy, SciPy] -> machine learning [PyTorch]

### Atomistic mechanisms of calcium permeation modulated by Q/R editing and selectivity filter mutations in GluA2 AMPA receptors. (PNAS 2025)

- DOI: 10.1073/pnas.2425172122 | PMCID: PMC12377769 | PMID: 40811461
- Evidence: For the quantitative analysis of the trajectories, we wrote custom Python code, using the MDAnalysis package ( 69 , 70 ) for analysis and the matplotlib library ( 71 ) for data visualization.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis, VMD] -> visualisation [MDAnalysis, Matplotlib, VMD] -> stage not stated [PyMOL]

### Deciphering Ca&lt;sup&gt;&lt;b&gt;2+&lt;/b&gt;&lt;/sup&gt; permeation and valence selectivity in Ca&lt;sub&gt;V&lt;/sub&gt;1: Molecular dynamics simulations reveal the three-ion knock-on mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2424694122 | PMCID: PMC12146731 | PMID: 40440072
- Evidence: The MDAnalysis package ( 76 ) was used to analyze the MD simulation results.
- Full pipeline: quantification [PLUMED] -> simulation/modelling [GROMACS v2021.2, MDAnalysis, PLUMED] -> structure determination [VMD] -> visualisation [PyMOL] -> stage not stated [NetworkX]

### Reversible molecular simulation for training classical and machine-learning force fields. (PNAS 2025)

- DOI: 10.1073/pnas.2426058122 | PMCID: PMC12146726 | PMID: 40434635
- Evidence: MDAnalysis [ 77 ] and BioStructures [ 78 ] were used for analysis.
- Full pipeline: stage not stated [MDAnalysis, OpenMM, PyTorch]

### Calcium-activated chloride channel TMEM16A opens via pi-helical transition in transmembrane segment 4. (PNAS 2025)

- DOI: 10.1073/pnas.2421900122 | PMCID: PMC12067253 | PMID: 40299692
- Evidence: All analyses were done with GROMACS tools and bespoke python scripts using the MDAnalysis library ( 77 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS, PyMOL v2.5] -> stage not stated [AlphaFold, ImageJ, MDAnalysis]

### Defects induce phase transition from dynamic to static rippling in graphene. (PNAS 2025)

- DOI: 10.1073/pnas.2416932122 | PMCID: PMC11892612 | PMID: 40020187
- Evidence: The entire postprocessing analysis for all simulations was performed in Python using the ASE ( 71 ), MDAnalysis ( 72 , 73 ), and OVITO ( 74 ) software packages.
- Full pipeline: simulation/modelling [LAMMPS, MDAnalysis, Python]

### Hidden complexity of α7 nicotinic acetylcholine receptor desensitization revealed by MD simulations and Markov state modeling. (PNAS 2025)

- DOI: 10.1073/pnas.2420993122 | PMCID: PMC11848294 | PMID: 39946538
- Evidence: The MD trajectories were analyzed using MDAnalysis package version 2.2.0 ( 72 ) to extract time series of RMSD, interatomic distances, side-chain dihedrals, and atom coordinates.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Jupyter]

### Subunit-specific conductance of single homomeric and heteromeric HCN pacemaker channels at femtosiemens resolution. (PNAS 2025)

- DOI: 10.1073/pnas.2422533122 | PMCID: PMC11804576 | PMID: 39879240
- Evidence: All trajectories were analyzed with GROMACS toolkits and Python3 using MDAnalysis ( 63 ).
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis] -> visualisation [PyMOL, VMD]

### Enzymes in a human cytoplasm model organize into submetabolon complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2414206122 | PMCID: PMC11804712 | PMID: 39874290
- Evidence: D eff calculations were done with the Python-based MDAnalysis package ( 74 – 76 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [MDAnalysis, VMD]

### D614G reshapes allosteric networks and opening mechanisms of SARS-CoV-2 spikes. (PNAS 2026)

- DOI: 10.1073/pnas.2504793123 | PMCID: PMC13168548 | PMID: 42101997
- Evidence: A tar ball containing selected WE simulation trajectories (psf/pdb/dcd), along with input scripts (Amber and NAMD) and MDAnalysis scripts (py), is available for download on the Amaro Lab website ( https://amarolab.ucsd.edu/data.php#covid19 ) ( 85 ) with the following name: D614G_for_sharing_amarolab.tar.gz.
- Full pipeline: simulation/modelling [MDAnalysis, NAMD]

### Quinones operate as proton-collecting antennas in energy-transducing membranes. (PNAS 2026)

- DOI: 10.1073/pnas.2534025123 | PMCID: PMC13099693 | PMID: 41980103
- Evidence: The classical MD simulations were performed with NAMD2.14 ( 77 , 78 ) and the trajectories were analyzed using Visual Molecular Dynamics ( 79 ) and MDAnalysis ( 80 , see SI Appendix, Extended Methods ).
- Full pipeline: simulation/modelling [MDAnalysis, VMD] -> stage not stated [Python]

### Direct evidence of acid-driven protein desolvation. (PNAS 2026)

- DOI: 10.1073/pnas.2525949123 | PMCID: PMC12974452 | PMID: 41785322
- Evidence: A water density map of the regions up to 5 Å around the protein with a grid spacing of 0.5 Å was calculated using the MDAnalysis package ( 86 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [ChimeraX, MDAnalysis, PHENIX] -> stage not stated [RELION, SciPy]

