# LAMMPS

- **Category:** md
- **Papers in survey:** 131
- **Journals:** PNAS (117), Nature (11), Cell (3)
- **Years:** 2021 (9), 2022 (20), 2023 (31), 2024 (33), 2025 (34), 2026 (4)
- **Pipeline stages it appears in:** simulation/modelling (114), machine learning (3), visualisation (1), alignment/mapping (1), normalisation (1), dimensionality reduction/clustering (1), read trimming (1)

## Papers

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Evidence: Simulations are performed with the LAMMPS package ( Plimpton, 1995 ).
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### Vertebrate centromeres in mitosis are functionally bipartite structures stabilized by cohesin. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.014 | PMCID: PMC11164432 | PMID: 38744280
- Evidence: 79 http://www.usadellab.org/cms/index.php?page=trimmomatic BWA mem v0.7.16 Heng Li https://github.com/lh3/bwa?tab=readme-ov-file deepTools bamCoverage v3.5 deepTools https://deeptools.readthedocs.io/en/develop/ LAMMPS Plimpton 80 https://github.com/lammps/lammps Huygens Professional (v20.10) Scientific Volume Imaging https://svi.nl/Huygens-Professional capC-MAP software Buckle 81 https://github.co...
- Full pipeline: read trimming [BWA v0.7.16, Cutadapt v1.18, ImageJ, LAMMPS, Trimmomatic v0.36, deepTools] -> stage not stated [Snakemake]

### Mapping chromatin structure at base-pair resolution unveils a unified model of cis-regulatory element interactions. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.013 | PMCID: PMC7618578 | PMID: 41197626
- Evidence: ...ts/trim_galore/ FLASh https://doi.org/10.1093/bioinformatics/btr507 John Hopkins Centre for Computational Biology https://ccb.jhu.edu/software/FLASH/ LAMMPS https://doi.org/10.1016/j.cpc.2021.108171 https://www.lammps.org OVITO https://doi.org/10.1088/0965-0393/18/1/015012 https://www.ovito.org SoftWoRx GE Healthcare Available from Cytiva SIMCheck 83 https://doi.org/10.1038/srep15915 https://www.m...
- Full pipeline: read trimming [Trim Galore] -> quantification [Snakemake] -> differential/statistical testing [Snakemake] -> structure determination [Trim Galore] -> stage not stated [BEDTools, Bowtie2, DESeq2, LAMMPS, MACS2]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Evidence: Next, to generate thermodynamic ensembles of 3D conformations of the locus, molecular dynamics simulations were run of the optimal polymers, using the freely available LAMMPS software (v.5june2019) 86 .
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### Extremely anisotropic van der Waals thermal conductors. (Nature 2021)

- DOI: 10.1038/s41586-021-03867-8 | PMCID: PMC8481126 | PMID: 34588671
- Evidence: The structure models were subsequently relaxed using an analytic bond-order potential 61 and implemented in the LAMMPS package 62 .
- Full pipeline: simulation/modelling [Python] -> stage not stated [ImageJ, LAMMPS]

### Hypocrystalline ceramic aerogels for thermal insulation at extreme conditions. (Nature 2022)

- DOI: 10.1038/s41586-022-04784-0 | PMCID: PMC9242853 | PMID: 35768591
- Evidence: All the simulations were carried out with the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) 58 code, and the WTMetaD simulations were carried out with an additional plugin code 59 PLUMED 2.
- Full pipeline: simulation/modelling [LAMMPS, PLUMED]

### Flexible solar cells based on foldable silicon wafers with blunted edges. (Nature 2023)

- DOI: 10.1038/s41586-023-05921-z | PMCID: PMC10208971 | PMID: 37225883
- Evidence: Atomistic simulation Large-scale atomic/molecular massively parallel simulator (LAMMPS) package 47 was used to perform atomistic simulations of mode I loading on c-Si nanofilms with sharp and round channels between surface pyramids.
- Full pipeline: simulation/modelling [LAMMPS]

### Photochromism from wavelength-selective colloidal phase segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05873-4 | PMCID: PMC10191859 | PMID: 37198311
- Evidence: The Brownian dynamics simulations were conducted using the LAMMPS package 1 .
- Full pipeline: simulation/modelling [LAMMPS]

### Visualizing the disordered nuclear transport machinery in situ. (Nature 2023)

- DOI: 10.1038/s41586-023-05990-0 | PMCID: PMC10156602 | PMID: 37100914
- Evidence: MD simulations We used the LAMMPS software package 75 to simulate the polymeric systems.
- Full pipeline: simulation/modelling [GROMACS v2020.6, LAMMPS] -> visualisation [VMD] -> stage not stated [AlphaFold]

### Observation of a promethium complex in solution. (Nature 2024)

- DOI: 10.1038/s41586-024-07267-6 | PMCID: PMC11111410 | PMID: 38778232
- Evidence: The initial structure of the Pm complex–water system (a periodic cubic box of 18 Å length containing one complex and 144 water molecules) was pre-equilibrated for 5 ns in a canonical ensemble at a temperature of 300 K using the extended polymer consistent force field (PCFF+) 58 supported in MedeA-LAMMPS 59 , 60 .
- Full pipeline: simulation/modelling [LAMMPS] -> visualisation [UCSF Chimera]

### The persistence of memory in ionic conduction probed by nonlinear optics. (Nature 2024)

- DOI: 10.1038/s41586-023-06827-6 | PMCID: PMC10808053 | PMID: 38267678
- Evidence: Steady-state molecular dynamics Steady-state classical miolecular dynamics simulations were carried out in LAMMPS 58 using Buckingham pairwise potentials with Coulombic interactions as described previously 7 .
- Full pipeline: simulation/modelling [LAMMPS]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Evidence: Integration was performed with a velocity Verlet algorithm using the LAMMPS software 59 .
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### Light-induced quantum friction of carbon nanotubes in water. (Nature 2026)

- DOI: 10.1038/s41586-026-10632-2 | PMCID: PMC13293881 | PMID: 42271052
- Evidence: Computation of friction and diffusion in water The classical atomistic molecular dynamics simulations were run with an open source LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) 61 to estimate the interfacial friction coefficient and diffusion of graphene and (6,5)-SWCNTs in explicit water.
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [Python v3.10.5]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: We used the free available LAMMPS software (v.30july2016) to run MD simulations highly optimized for parallel computing 153 .
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Stripping away ion hydration shells in electrical double-layer formation: Water networks matter. (PNAS 2021)

- DOI: 10.1073/pnas.2108568118 | PMCID: PMC8617503 | PMID: 34782461
- Evidence: Classical simulations were performed using the LAMMPS ( 50 ) code to simulate 17 aqueous solutions (17,486 water molecules) of 20 mM NaCl confined between parallel charged Au(100) walls with imposed 298 K constant temperature to water and ions all along the simulation.
- Full pipeline: simulation/modelling [LAMMPS]

### One-dimensional van der Waals heterostructures: Growth mechanism and handedness correlation revealed by nondestructive TEM. (PNAS 2021)

- DOI: 10.1073/pnas.2107295118 | PMCID: PMC8449348 | PMID: 34508003
- Evidence: We used the molecular dynamics package LAMMPS as an implementation of this calculation ( 51 ).
- Full pipeline: simulation/modelling [LAMMPS]

### An expression for the angle of repose of dry cohesive granular materials on Earth and in planetary environments. (PNAS 2021)

- DOI: 10.1073/pnas.2107965118 | PMCID: PMC8463844 | PMID: 34518227
- Evidence: The integration was performed using the open source Discrete Element Method particle simulation software LIGGGHTS (which stands for LAMMPS Improved for General Granular and Granular Heat Transfer Simulations) ( 52 ), along with the extensions introduced in ref.
- Full pipeline: simulation/modelling [LAMMPS]

### Two-step deswelling in the Volume Phase Transition of thermoresponsive microgels. (PNAS 2021)

- DOI: 10.1073/pnas.2109560118 | PMCID: PMC8449345 | PMID: 34508008
- Evidence: All simulations are performed with the LAMMPS package ( 60 ) at fixed temperature k B T / ε = 1.0 .
- Full pipeline: simulation/modelling [LAMMPS]

### Ion correlations drive charge overscreening and heterogeneous nucleation at solid-aqueous electrolyte interfaces. (PNAS 2021)

- DOI: 10.1073/pnas.2105154118 | PMCID: PMC8364158 | PMID: 34353907
- Evidence: All MD simulations were carried out on the supercomputers at the National Energy Research Scientific Computing Center (NERSC) using the code Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) ( 48 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Routes to cubic ice through heterogeneous nucleation. (PNAS 2021)

- DOI: 10.1073/pnas.2025245118 | PMCID: PMC8020660 | PMID: 33766916
- Evidence: All simulations are performed with the large-scale atomic/molecular massively parallel simulator (LAMMPS) code ( 83 ); and sampled the constant number of particles, constant volume, and constant temperature (NVT) canonical ensemble, using chains of 10 Nosé–Hoover thermostats with a relaxation times of 0.5 ps; and integrated the equations of motion with a time step of 10 fs.
- Full pipeline: simulation/modelling [LAMMPS]

### Metastable-solid phase diagrams derived from polymorphic solidification kinetics. (PNAS 2021)

- DOI: 10.1073/pnas.2017809118 | PMCID: PMC7936279 | PMID: 33619094
- Evidence: Materials and Methods In this paper, we have presented results of a series of large-scale MD simulations using the LAMMPS code ( 44 ) and the EAM interatomic potential for Cu metal, as constructed by Mishin et al.
- Full pipeline: simulation/modelling [LAMMPS]

### Ice friction at the nanoscale. (PNAS 2022)

- DOI: 10.1073/pnas.2209545119 | PMCID: PMC9894246 | PMID: 36442119
- Evidence: Molecular dynamics simulations in the Np z AT ensemble were performed using LAMMPS ( 55 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Shear transformations in metallic glasses without excessive and predefinable defects. (PNAS 2022)

- DOI: 10.1073/pnas.2213941119 | PMCID: PMC9860280 | PMID: 36409913
- Evidence: This hybrid scheme has been efficiently integrated in LAMMPS ( 53 ).
- Full pipeline: stage not stated [LAMMPS]

### Double-atom dealloying-derived Frank partial dislocations in cobalt nanocatalysts boost metal-air batteries and fuel cells. (PNAS 2022)

- DOI: 10.1073/pnas.2214089119 | PMCID: PMC9659378 | PMID: 36322768
- Evidence: The first-principles-based RMD calculations were performed at 300 K in the LAMMPS package combined with a Local Embedded Cluster Reoptimization procedure on dealloyed Co particles.
- Full pipeline: dimensionality reduction/clustering [LAMMPS]

### Plastic deformation of superionic water ices. (PNAS 2022)

- DOI: 10.1073/pnas.2203397119 | PMCID: PMC9659364 | PMID: 36322744
- Evidence: The MD simulations for the edge dislocations were carried out using the LAMMPS package ( 70 , 71 ) interfaced with the DP module ( 48 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Topological gelation of reconnecting polymers. (PNAS 2022)

- DOI: 10.1073/pnas.2207728119 | PMCID: PMC9636914 | PMID: 36279471
- Evidence: The simulations are performed in LAMMPS ( 31 ) by using a Langevin thermostat and a time step Δ t = 0.001 τ B , with τ B the Brownian time (see SI Appendix for more details).
- Full pipeline: simulation/modelling [LAMMPS]

### Synergetic collision and space separation in microfluidic chip for efficient affinity-discriminated molecular selection. (PNAS 2022)

- DOI: 10.1073/pnas.2211538119 | PMCID: PMC9565315 | PMID: 36191233
- Evidence: For simulations, all the BD simulations were performed in the NVT ensemble using the LAMMPS package (5 September 2018) ( 29 ).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [ImageJ]

### Anomalous water transport in narrow-diameter carbon nanotubes. (PNAS 2022)

- DOI: 10.1073/pnas.2211348119 | PMCID: PMC9522342 | PMID: 36122221
- Evidence: All MD simulations are performed using the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) package ( 32 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Driving force and pathway in polyelectrolyte complex coacervation. (PNAS 2022)

- DOI: 10.1073/pnas.2209975119 | PMCID: PMC9457374 | PMID: 36037377
- Evidence: All our simulations are performed in the canonical ensemble with a Langevin thermostat using the LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator) platform.
- Full pipeline: simulation/modelling [LAMMPS]

### Homogeneous ice nucleation in an ab initio machine-learning model of water. (PNAS 2022)

- DOI: 10.1073/pnas.2207294119 | PMCID: PMC9388152 | PMID: 35939708
- Evidence: Simulations were performed by using LAMMPS ( 69 ) patched with the DeePMD-kit ( 70 ).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [PLUMED]

### Computationally exploring the mechanism of bacteriophage T7 gp4 helicase translocating along ssDNA. (PNAS 2022)

- DOI: 10.1073/pnas.2202239119 | PMCID: PMC9371691 | PMID: 35914145
- Evidence: Using graphics processing units, a 30-fold speedup has been achieved in protein and protein–DNA simulations over the existing LAMMPS-based implementations running on a single central processing unit core.
- Full pipeline: dimensionality reduction/clustering [seaborn] -> simulation/modelling [LAMMPS, NAMD, OpenMM] -> stage not stated [PyMOL, VMD]

### Solvent selection criteria for temperature-resilient lithium-sulfur batteries. (PNAS 2022)

- DOI: 10.1073/pnas.2200392119 | PMCID: PMC9282424 | PMID: 35787034
- Evidence: MD simulations were performed in a Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) using the OPLS-AA force field with the FSI molecules description from previous reports ( 49 , 50 ).
- Full pipeline: simulation/modelling [LAMMPS, VMD]

### Nonisothermal nucleation in the gas phase is driven by cool subcritical clusters. (PNAS 2022)

- DOI: 10.1073/pnas.2201955119 | PMCID: PMC9282380 | PMID: 35787057
- Evidence: All simulations were performed with the LAMMPS MD code ( 37 ) using a Velocity–Verlet integrator and a time step of 0.002.
- Full pipeline: simulation/modelling [LAMMPS]

### Connection between water's dynamical and structural properties: Insights from ab initio simulations. (PNAS 2022)

- DOI: 10.1073/pnas.2121641119 | PMCID: PMC9173753 | PMID: 35588447
- Evidence: We also performed FF (classical MD) simulations via the LAMMPS (large-scale atomic/molecular massively parallel simulator) package ( 106 ).
- Full pipeline: simulation/modelling [LAMMPS]

### How chemical defects influence the charging of nanoporous carbon supercapacitors. (PNAS 2022)

- DOI: 10.1073/pnas.2121945119 | PMCID: PMC9170011 | PMID: 35439053
- Evidence: The particle-particle particle-mesh solver (PPPM) scheme, which is well suited for large systems (in this work, over 30,000 atoms), as implemented in LAMMPS ( 57 ) has been used with a threshold on the forces of 10 −4 .
- Full pipeline: stage not stated [LAMMPS]

### Likelihood-based non-Markovian models from molecular dynamics. (PNAS 2022)

- DOI: 10.1073/pnas.2117586119 | PMCID: PMC9060509 | PMID: 35320038
- Evidence: The dynamics is integrated with a time step of Δ t M D = 0.001 (in LJ units) in the NVE ensemble with the velocity Verlet algorithm using the LAMMPS simulation package ( 58 ).
- Full pipeline: simulation/modelling [LAMMPS, PLUMED] -> machine learning [PLUMED]

### Strain and rupture of HIV-1 capsids during uncoating. (PNAS 2022)

- DOI: 10.1073/pnas.2117781119 | PMCID: PMC8915963 | PMID: 35238630
- Evidence: CG models of the capsids were briefly relaxed in a 20-ps Langevin dynamics run under the canonical (NVT) ensemble with the large-scale atomic/molecular massively parallel simulator (LAMMPS) ( 33 ).
- Full pipeline: alignment/mapping [IMOD] -> simulation/modelling [LAMMPS, NAMD v2.14]

### Atomic-scale probing of heterointerface phonon bridges in nitride semiconductor. (PNAS 2022)

- DOI: 10.1073/pnas.2117027119 | PMCID: PMC8872775 | PMID: 35181607
- Evidence: The MD simulations were performed using the LAMMPS package ( 48 ) with the Stillinger–Weber potential ( 50 , 51 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Ultrafast atomic view of laser-induced melting and breathing motion of metallic liquid clusters with MeV ultrafast electron diffraction. (PNAS 2022)

- DOI: 10.1073/pnas.2111949119 | PMCID: PMC8795546 | PMID: 35074922
- Evidence: The TTM-MD simulations were conducted for a 50- × 60- × 60-nm 3 polycrystalline Al system (∼11 million atoms) with the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) ( 49 – 52 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Light-induced shift current vortex crystals in moiré heterobilayers. (PNAS 2023)

- DOI: 10.1073/pnas.2314775120 | PMCID: PMC10741382 | PMID: 38085781
- Evidence: The structural relaxation of the rotationally aligned WSe 2 /WS 2 moiré superlattice is performed using force fields with the LAMMPS package ( 53 ) with the help of the TWISTER code ( 54 ).
- Full pipeline: alignment/mapping [LAMMPS] -> simulation/modelling [LAMMPS] -> stage not stated [Quantum ESPRESSO]

### The role of dynamics in heterogeneous catalysis: Surface diffusivity and N<sub>2</sub> decomposition on Fe(111). (PNAS 2023)

- DOI: 10.1073/pnas.2313023120 | PMCID: PMC10723053 | PMID: 38060558
- Evidence: Classical molecular dynamics simulations were performed with Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) software ( 91 ), patched with DeepMD-kit 2.1 ( 89 ) and PLUMED ( 76 ).
- Full pipeline: simulation/modelling [LAMMPS, PLUMED, Quantum ESPRESSO] -> stage not stated [VMD]

### Anomalous magnetoresistance in a nonconjugated radical polymer glass. (PNAS 2023)

- DOI: 10.1073/pnas.2308741120 | PMCID: PMC10614627 | PMID: 37862383
- Evidence: The Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) was used to perform all molecular dynamics simulations.
- Full pipeline: simulation/modelling [LAMMPS]

### Identifying microscopic factors that influence ductility in disordered solids. (PNAS 2023)

- DOI: 10.1073/pnas.2307552120 | PMCID: PMC10589640 | PMID: 37812709
- Evidence: Using LAMMPS, we simulate bead-spring polymer nanopillars with N = 5 monomers per chain ( 39 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Collective motion in hcp-Fe at Earth's inner core conditions. (PNAS 2023)

- DOI: 10.1073/pnas.2309952120 | PMCID: PMC10576103 | PMID: 37782810
- Evidence: MLMD were carried out using the LAMMPS code, employing periodic boundary conditions and a time step of 1 fs ( 83 ).
- Full pipeline: stage not stated [LAMMPS]

### Toward a quantitative interfacial description of solvation for Li metal battery operation under extreme conditions. (PNAS 2023)

- DOI: 10.1073/pnas.2310714120 | PMCID: PMC10576153 | PMID: 37782794
- Evidence: Classical, fixed-charge MD simulations were performed in the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) software, with the solvents and Li + described using the General Amber forcefield, while the anion was described with the potential of Gouveia et al.
- Full pipeline: simulation/modelling [LAMMPS]

### Hierarchical bubble size distributions in coarsening wet liquid foams. (PNAS 2023)

- DOI: 10.1073/pnas.2306551120 | PMCID: PMC10515135 | PMID: 37708201
- Evidence: In the framework of the molecular dynamics code LAMMPS ( 59 ), a cubic simulation box was filled by spheres with repulsive, Hertzian interactions with radii randomly chosen from a distribution corresponding to the one we observe experimentally for ϕ = 33 % in the Scaling State ( Fig.
- Full pipeline: normalisation [LAMMPS] -> simulation/modelling [LAMMPS]

### Mechanical Fourier transform for programmable metamaterials. (PNAS 2023)

- DOI: 10.1073/pnas.2305380120 | PMCID: PMC10500267 | PMID: 37669372
- Evidence: The simulations were performed in canonical ensemble by the large-scale atomic molecular massively parallel simulator (LAMMPS).
- Full pipeline: simulation/modelling [LAMMPS]

### Stress-dependent activation entropy in thermally activated cross-slip of dislocations. (PNAS 2023)

- DOI: 10.1073/pnas.2222039120 | PMCID: PMC10450676 | PMID: 37585466
- Evidence: MD simulations of dislocation cross-slip are performed using the LAMMPS package ( 33 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Flexible fluid-based encapsulation platform for water-sensitive materials. (PNAS 2023)

- DOI: 10.1073/pnas.2308804120 | PMCID: PMC10450442 | PMID: 37579173
- Evidence: To run MD simulations, we used LAMMPS ( 27 ) and the OPLS-AA force field ( 28 ), directly given by the Materials Science program, for the lubricant molecules and polymer backbone.
- Full pipeline: simulation/modelling [LAMMPS]

### Scattering evidence of positional charge correlations in polyelectrolyte complexes. (PNAS 2023)

- DOI: 10.1073/pnas.2302151120 | PMCID: PMC10410704 | PMID: 37523553
- Evidence: All simulations were performed using LAMMPS ( 46 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Fluctuotaxis: Nanoscale directional motion away from regions of fluctuation. (PNAS 2023)

- DOI: 10.1073/pnas.2220500120 | PMCID: PMC10401016 | PMID: 37487105
- Evidence: Model and Method All MD simulations were performed using the large-scale atomic/molecular massively parallel simulator (LAMMPS) package ( 62 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Electrolytes with moderate lithium polysulfide solubility for high-performance long-calendar-life lithium-sulfur batteries. (PNAS 2023)

- DOI: 10.1073/pnas.2301260120 | PMCID: PMC10400945 | PMID: 37487097
- Evidence: MD simulations were performed with the LAMMPS package ( 64 ).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [MDAnalysis]

### Detecting dynamic domains and local fluctuations in complex molecular systems via timelapse neighbors shuffling. (PNAS 2023)

- DOI: 10.1073/pnas.2300565120 | PMCID: PMC10372573 | PMID: 37467266
- Evidence: Deep-potential MD simulations of both Cu surfaces are conducted with LAMMPS software ( 82 ) using a neural network potential built using the DeepMD platform ( 83 ), as described in detail in ref.
- Full pipeline: simulation/modelling [GROMACS, LAMMPS] -> machine learning [LAMMPS] -> stage not stated [SciPy]

### Underexcitation prevents crystallization of granular assemblies subjected to high-frequency vibration. (PNAS 2023)

- DOI: 10.1073/pnas.2306209120 | PMCID: PMC10629526 | PMID: 37428926
- Evidence: The center coordinates and diameter of the balls were exported to the open-source software LAMMPS ( 25 ) to determine their crystal arrangements along with the crystallinity fractions using the polyhedral template matching (PTM) ( 20 ) algorithm.
- Full pipeline: stage not stated [LAMMPS]

### Confined water-encapsulated activated carbon for capturing short-chain perfluoroalkyl and polyfluoroalkyl substances from drinking water. (PNAS 2023)

- DOI: 10.1073/pnas.2219179120 | PMCID: PMC10318985 | PMID: 37364117
- Evidence: MD simulations were performed by the LAMMPS software package.
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [VMD]

### Minimal conditions for solidification and thermal processing of colloidal gels. (PNAS 2023)

- DOI: 10.1073/pnas.2215922120 | PMCID: PMC10288545 | PMID: 37307451
- Evidence: We constructed our computational model system using the LAMMPS molecular dynamics package.
- Full pipeline: simulation/modelling [LAMMPS]

### Unveiling the complexity of nanodiamond structures. (PNAS 2023)

- DOI: 10.1073/pnas.2301981120 | PMCID: PMC10266025 | PMID: 37253001
- Evidence: Molecular dynamics simulations were performed on the LAMMPS platform ( 52 ), using a velocity Verlet algorithm with a time step of 0.1 fs, with temperature fluctuating around 300 K.
- Full pipeline: simulation/modelling [LAMMPS]

### Proximity to criticality predicts surface properties of biomolecular condensates. (PNAS 2023)

- DOI: 10.1073/pnas.2220014120 | PMCID: PMC10266063 | PMID: 37252985
- Evidence: Coarse-grained molecular-dynamics simulations were performed using LAMMPS ( 43 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Phosphorylation sites are evolutionary checkpoints against liquid-solid transition in protein condensates. (PNAS 2023)

- DOI: 10.1073/pnas.2215828120 | PMCID: PMC10193986 | PMID: 37155880
- Evidence: The LAMMPS molecular dynamics package was employed to perform the coarse-grained Langevin dynamics simulations ( 35 ).
- Full pipeline: simulation/modelling [LAMMPS, NAMD]

### Electroregulation of graphene-nanofluid interactions to coenhance water permeation and ion rejection in vertical graphene membranes. (PNAS 2023)

- DOI: 10.1073/pnas.2219098120 | PMCID: PMC10175824 | PMID: 37126725
- Evidence: The MD simulations of water transport in the VARGO nanochannels were performed using a large-scale atomic/molecular massive parallel simulator (LAMMPS).
- Full pipeline: simulation/modelling [LAMMPS]

### Morphological transformations of vesicles with confined flexible filaments. (PNAS 2023)

- DOI: 10.1073/pnas.2300380120 | PMCID: PMC10161051 | PMID: 37098058
- Evidence: A constant ambient temperature of 310 K is maintained via the Nosé–Hoover thermostat ( 53 , 54 ), and the canonical (NVT) ensemble is used in our MD simulations based on LAMMPS ( 55 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Colloidal superionic conductors. (PNAS 2023)

- DOI: 10.1073/pnas.2300257120 | PMCID: PMC10104562 | PMID: 37018200
- Evidence: Materials and Methods All of our MD simulations are done using the LAMMPS software package ( 60 – 66 ).
- Full pipeline: simulation/modelling [LAMMPS, VMD]

### Effect of local chemical order on the irradiation-induced defect evolution in CrCoNi medium-entropy alloy. (PNAS 2023)

- DOI: 10.1073/pnas.2218673120 | PMCID: PMC10104586 | PMID: 37014854
- Evidence: MD simulations were carried out to prepare the model alloys using Large-scale Atomic/Molecular Massively Parallel Simulator software (LAMMPS) ( 46 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Disruption of energetic and dynamic base pairing cooperativity in DNA duplexes by an abasic site. (PNAS 2023)

- DOI: 10.1073/pnas.2219124120 | PMCID: PMC10083564 | PMID: 36976762
- Evidence: All systems were simulated using the LAMMPS package ( 59 ) compiled with the 3SPN.2 model plugin ( 23 ).
- Full pipeline: simulation/modelling [LAMMPS, Python] -> stage not stated [PLUMED]

### Self-regulation of the nuclear pore complex enables clogging-free crowded transport. (PNAS 2023)

- DOI: 10.1073/pnas.2212874120 | PMCID: PMC9963888 | PMID: 36757893
- Evidence: The model was simulated using Brownian dynamics with an implicit solvent using the molecular dynamics package LAMMPS ( 55 ) using the resources provided by ComputeCanada.
- Full pipeline: simulation/modelling [LAMMPS]

### The marionette mechanism of domain-domain communication in the antagonist, agonist, and coactivator responses of the estrogen receptor. (PNAS 2023)

- DOI: 10.1073/pnas.2216906120 | PMCID: PMC9963092 | PMID: 36730193
- Evidence: Briefly, the simulations were carried out using the AWSEM-3SPN.2C forcefield for protein–DNA complexes in the LAMMPS open-source software package.
- Full pipeline: simulation/modelling [LAMMPS]

### Molecular understanding of Ni<sup>2+</sup>-nitrogen family metal-coordinated hydrogel relaxation times using free energy landscapes. (PNAS 2023)

- DOI: 10.1073/pnas.2213160120 | PMCID: PMC9942824 | PMID: 36649435
- Evidence: MD simulations implemented in LAMMPS ( 32 ) are used to investigate the energy landscape of imidazole, histidine, and pyridine ligands using the CHARMM22 force field ( 33 , 34 ).
- Full pipeline: simulation/modelling [LAMMPS, PLUMED]

### Probing iron in Earth's core with molecular-spin dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2408897121 | PMCID: PMC11665881 | PMID: 39665761
- Evidence: The LSF implementation described in SI Appendix is available in the GJQL_2 branch of the repository: https://github.com/snikolov3/DEMSI-LAMMPS.git (see examples/spin_oracle directory for additional details) ( 77 ).
- Full pipeline: stage not stated [LAMMPS]

### Molecular insights into the interaction between a disordered protein and a folded RNA. (PNAS 2024)

- DOI: 10.1073/pnas.2409139121 | PMCID: PMC11626198 | PMID: 39589885
- Evidence: See SI Appendix for additional information on sample preparation, data acquisition, and analysis ( 104 – 106 ) CG Simulations in LAMMPS.
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [SciPy]

### Medium-density amorphous ice unveils shear rate as a new dimension in water's phase diagram. (PNAS 2024)

- DOI: 10.1073/pnas.2414444121 | PMCID: PMC11621468 | PMID: 39576349
- Evidence: Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability The datasets for the figures and LAMMPS input files can be accessed and downloaded at https://doi.org/10.5281/zenodo.13947547 ( 54 ).
- Full pipeline: stage not stated [LAMMPS]

### Identifying and controlling the order parameter for ultrafast photoinduced phase transitions in thermosalient materials. (PNAS 2024)

- DOI: 10.1073/pnas.2408366121 | PMCID: PMC11573639 | PMID: 39499639
- Evidence: MD simulations of 4DBpFO were performed using the LAMMPS (23 June 2022) software package ( 42 , 43 ).
- Full pipeline: dimensionality reduction/clustering [PLUMED] -> simulation/modelling [LAMMPS, PLUMED] -> stage not stated [VMD]

### Endosomal membrane budding patterns in plants. (PNAS 2024)

- DOI: 10.1073/pnas.2409407121 | PMCID: PMC11536153 | PMID: 39441629
- Evidence: To simulate and visualize the system, we use the Large-scale Atomic/Molecular Massively Parallel Simulator Molecular Dynamics (LAMMPS MD) simulation package ( 52 ) and Open Visualization Tool (OVITO) ( 53 ).
- Full pipeline: simulation/modelling [LAMMPS] -> visualisation [LAMMPS] -> stage not stated [IMOD]

### The smallest electrochemical bubbles. (PNAS 2024)

- DOI: 10.1073/pnas.2406956121 | PMCID: PMC11474048 | PMID: 39356663
- Evidence: All the simulations were performed with a modified version of the LAMMPS program ( 32 ).
- Full pipeline: simulation/modelling [LAMMPS]

### The role of the water contact layer on hydration and transport at solid/liquid interfaces. (PNAS 2024)

- DOI: 10.1073/pnas.2407877121 | PMCID: PMC11420213 | PMID: 39259594
- Evidence: The results presented in this work are obtained from MD simulations performed with the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) code ( 61 ) that were run in the canonical ensemble at 330 K for 5 ns using C-NNPs.
- Full pipeline: simulation/modelling [LAMMPS]

### Quantitative insights into the mechanism of proton conduction and selectivity for the human voltage-gated proton channel Hv1. (PNAS 2024)

- DOI: 10.1073/pnas.2407479121 | PMCID: PMC11420211 | PMID: 39259593
- Evidence: Simulations were performed by LAMMPS MD package ( 70 ) coupled with RAPTOR ( 36 ) for proton reactions.
- Full pipeline: normalisation [GROMACS] -> simulation/modelling [GROMACS, LAMMPS]

### Supramolecular assembly of polycation/mRNA nanoparticles and in vivo monocyte programming. (PNAS 2024)

- DOI: 10.1073/pnas.2400194121 | PMCID: PMC11363337 | PMID: 39172792
- Evidence: All simulations were carried out with the LAMMPS MD package ( 59 ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [LAMMPS]

### Superionic iron hydride shapes ultralow-velocity zones at Earth's core-mantle boundary. (PNAS 2024)

- DOI: 10.1073/pnas.2406386121 | PMCID: PMC11363269 | PMID: 39163332
- Evidence: With the reliable DP model obtained, we then conducted NPT (constant number of atoms, constant pressure, and constant temperature) simulations on a supercell of Fe 1728 H 1728 using LAMMPS ( 61 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Improving normothermic machine perfusion and blood transfusion through biocompatible blood silicification. (PNAS 2024)

- DOI: 10.1073/pnas.2322418121 | PMCID: PMC11363281 | PMID: 39159377
- Evidence: The whole-RBC level simulations are performed with a modified LAMMPS package and the temperature is kept at T = 296.25 K.
- Full pipeline: simulation/modelling [LAMMPS]

### Evidence of ferroelectric features in low-density supercooled water from ab initio deep neural-network simulations. (PNAS 2024)

- DOI: 10.1073/pnas.2407295121 | PMCID: PMC11317578 | PMID: 39083416
- Evidence: The training has been performed with DeePMD-kit ( 29 ), while the MD simulations are performed with LAMMPS software ( 72 ).
- Full pipeline: simulation/modelling [LAMMPS] -> machine learning [LAMMPS]

### Transport coefficient approach for characterizing nonequilibrium dynamics in soft matter. (PNAS 2024)

- DOI: 10.1073/pnas.2401162121 | PMCID: PMC11295068 | PMID: 39042671
- Evidence: All simulations were performed using the large-scale atomic/molecular massively parallel simulator (LAMMPS) ( 70 ) under the periodic boundary condition.
- Full pipeline: simulation/modelling [LAMMPS]

### Programming patchy particles for materials assembly design. (PNAS 2024)

- DOI: 10.1073/pnas.2311891121 | PMCID: PMC11228463 | PMID: 38913891
- Evidence: However, many standard MD libraries, such as Highly Optimized Object-oriented Many-particle Dynamics (HOOMD)-blue ( 34 ) and Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) ( 35 ), offer support for simulations of nonisotropic objects called rigid bodies.
- Full pipeline: simulation/modelling [LAMMPS]

### Prebiotic chemical reactivity in solution with quantum accuracy and microsecond sampling using neural network potentials. (PNAS 2024)

- DOI: 10.1073/pnas.2322040121 | PMCID: PMC11161780 | PMID: 38809704
- Evidence: The training was done with DeepMD, the exploration with LAMMPS ( 63 ) and Plumed version 2.8.0 ( 64 , 65 ), and the labeling with cp2k.
- Full pipeline: machine learning [LAMMPS]

### Curvature-mediated rapid extravasation and penetration of nanoparticles against interstitial fluid pressure for improved drug delivery. (PNAS 2024)

- DOI: 10.1073/pnas.2319880121 | PMCID: PMC11145294 | PMID: 38768353
- Evidence: All coarse-grained simulations were performed using the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) package.
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [ImageJ]

### Threshold current density for diffusion-controlled stability of electrolytic surface nanobubbles. (PNAS 2024)

- DOI: 10.1073/pnas.2321958121 | PMCID: PMC11126992 | PMID: 38748584
- Evidence: The popular open-source code LAMMPS ( 41 ) is adopted.
- Full pipeline: stage not stated [LAMMPS]

### Liquid-liquid transition and ice crystallization in a machine-learned coarse-grained water model. (PNAS 2024)

- DOI: 10.1073/pnas.2322853121 | PMCID: PMC11098087 | PMID: 38709921
- Evidence: Methods Molecular dynamics simulations are performed with the ML-BOP water model ( 26 ) using LAMMPS ( 59 ) in the NpT ensemble with a time step of 5 fs using periodic cubic simulation cells with periodic boundary conditions in the three Cartesian directions.
- Full pipeline: simulation/modelling [LAMMPS]

### Intrinsic tensile ductility in strain hardening multiprincipal element metallic glass. (PNAS 2024)

- DOI: 10.1073/pnas.2400200121 | PMCID: PMC11067058 | PMID: 38662550
- Evidence: NNP-MD simulations were performed by the large-scale atomic/molecular massively parallel simulator (LAMMPS) ( 69 ) package with the in-house LAMMPS-NNAP interface.
- Full pipeline: simulation/modelling [LAMMPS]

### Impedance of nanocapacitors from molecular simulations to understand the dynamics of confined electrolytes. (PNAS 2024)

- DOI: 10.1073/pnas.2318157121 | PMCID: PMC11067016 | PMID: 38662549
- Evidence: Classical MD simulations were performed using MetalWalls ( 93 , 94 ) and LAMMPS ( 95 ) [equipped with the ELECTRODE package ( 96 )], which allows for the computation of custom properties on-the-fly.
- Full pipeline: simulation/modelling [LAMMPS]

### Topological wetting states of microdroplets on closed-loop structured surfaces: Breakdown of the Gibbs equation at the microscale. (PNAS 2024)

- DOI: 10.1073/pnas.2315730121 | PMCID: PMC11009642 | PMID: 38557188
- Evidence: MD simulations were performed using the Large-scale Molecular Massively Parallel Simulator (LAMMPS) package ( 44 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Integration of photothermal water evaporation with photocatalytic microplastics upcycling via nanofluidic thermal management. (PNAS 2024)

- DOI: 10.1073/pnas.2317192121 | PMCID: PMC10990145 | PMID: 38507451
- Evidence: MD simulations of thermo-osmosis behavior were conducted using the LAMMPS software package and the method previously reported in ref.
- Full pipeline: simulation/modelling [LAMMPS]

### Transcription-induced active forces suppress chromatin motion. (PNAS 2024)

- DOI: 10.1073/pnas.2307309121 | PMCID: PMC10963020 | PMID: 38489381
- Evidence: All the simulations were performed using LAMMPS ( 109 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Elucidating the role of water in collagen self-assembly by isotopically modulating collagen hydration. (PNAS 2024)

- DOI: 10.1073/pnas.2313162121 | PMCID: PMC10945838 | PMID: 38451946
- Evidence: We integrate the system at constant number of particles, N, and constant volume, V, with a Langevin thermostat to simulate Brownian motion of the molecules, with the LAMMPS MD package ( 101 ).
- Full pipeline: simulation/modelling [GROMACS v2020.4, LAMMPS] -> stage not stated [ImageJ]

### Ligand-induced incompatible curvatures control ultrathin nanoplatelet polymorphism and chirality. (PNAS 2024)

- DOI: 10.1073/pnas.2316299121 | PMCID: PMC10907275 | PMID: 38381786
- Evidence: Molecular dynamics (MD) simulations of isolated ligand-coated CdSe NPL were performed at constant volume and temperature (100K for thiol-coated NPL and 300K for the remaining systems), maintained via a Nosé-Hoover thermostat, using the LAMMPS software package ( 31 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Suppressing Zn pulverization with three-dimensional inert-cation diversion dam for long-life Zn metal batteries. (PNAS 2024)

- DOI: 10.1073/pnas.2317796121 | PMCID: PMC10895276 | PMID: 38346201
- Evidence: LAMMPS ( 53 ) was used to perform the molecular simulations.
- Full pipeline: simulation/modelling [LAMMPS]

### How particle shape affects granular segregation in industrial and geophysical flows. (PNAS 2024)

- DOI: 10.1073/pnas.2307061121 | PMCID: PMC10861863 | PMID: 38285942
- Evidence: We use the open-source code LAMMPS improved for general granular and granular heat transfer simulations (LIGGGHTS), which is based on the discrete element method, to compute granular dynamics.
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [OpenFOAM]

### HIV-1 capsid shape, orientation, and entropic elasticity regulate translocation into the nuclear pore complex. (PNAS 2024)

- DOI: 10.1073/pnas.2313737121 | PMCID: PMC10823262 | PMID: 38241438
- Evidence: All CG MD simulations were prepared and simulated in the LAMMPS MD software ( 71 ).
- Full pipeline: simulation/modelling [LAMMPS, VMD] -> visualisation [VMD]

### Unveiling the effect of Ni on the formation and structure of Earth's inner core. (PNAS 2024)

- DOI: 10.1073/pnas.2316477121 | PMCID: PMC10823253 | PMID: 38236737
- Evidence: Classical molecular dynamics (CMD) simulations were performed with LAMMPS (large-scale atomic/molecular massively parallel simulator) code ( 52 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Control of encounter kinetics by chemically active droplets. (PNAS 2025)

- DOI: 10.1073/pnas.2511670122 | PMCID: PMC12704720 | PMID: 41329728
- Evidence: To perform Brownian dynamics simulations, we use the LAMMPS computational package ( 62 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Substantial planar plastic anisotropy in inorganic Mg&lt;sub&gt;3&lt;/sub&gt;Bi&lt;sub&gt;2&lt;/sub&gt; single crystals. (PNAS 2025)

- DOI: 10.1073/pnas.2516449122 | PMCID: PMC12663941 | PMID: 41259148
- Evidence: All simulations were performed using the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) ( 32 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Symmetry transitions beyond the nanoscale in pressurized silica glass. (PNAS 2025)

- DOI: 10.1073/pnas.2524058122 | PMCID: PMC12625967 | PMID: 41201823
- Evidence: All simulations were carried out using the Large-scale Atomic/Molecular Massively Parallel Simulator software (LAMMPS) ( 50 ) with a time step of 1.6 fs.
- Full pipeline: simulation/modelling [LAMMPS]

### Chemical propulsion of hemozoin crystal motion in malaria parasites. (PNAS 2025)

- DOI: 10.1073/pnas.2513845122 | PMCID: PMC12595501 | PMID: 41150719
- Evidence: We performed Brownian dynamics simulations of 40 spheres in confinement using LAMMPS software ( fix brownian ) ( 72 ).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [Python, SciPy, TrackMate]

### Bridging microscopic dynamics and rheology in the yielding of charged colloidal suspensions. (PNAS 2025)

- DOI: 10.1073/pnas.2514216122 | PMCID: PMC12557723 | PMID: 41105713
- Evidence: Dense colloidal suspensions were simulated using LAMMPS ( 74 ) to investigate the effects of interparticle potentials on rheological behavior.
- Full pipeline: simulation/modelling [LAMMPS]

### Ab initio machine-learning simulation of calcium carbonate from aqueous solutions to the solid state. (PNAS 2025)

- DOI: 10.1073/pnas.2415663122 | PMCID: PMC12541341 | PMID: 41052335
- Evidence: All simulations used LAMMPS ( 66 ) patched with the DeePMD-kit ( 59 ) and the PLUMED enhanced sampling plugin ( 67 , 68 ).
- Full pipeline: simulation/modelling [LAMMPS, PLUMED]

### Electrostatics and viscosity are strongly linked in concentrated antibody solutions. (PNAS 2025)

- DOI: 10.1073/pnas.2425974122 | PMCID: PMC12519079 | PMID: 41037634
- Evidence: In all cases, we use LAMMPS ( 63 ), for running simulations in a fast parallel environment.
- Full pipeline: simulation/modelling [LAMMPS]

### Weighted active space protocol for multireference machine-learned potentials. (PNAS 2025)

- DOI: 10.1073/pnas.2513693122 | PMCID: PMC12478124 | PMID: 40953275
- Evidence: Molecular dynamics simulations are performed using the large-scale atomic/molecular massively parallel simulator (LAMMPS) ( 81 ), interfaced with MACE (version 0.3.7) ( 60 ) and PLUMED (version 2.9) ( 82 ).
- Full pipeline: simulation/modelling [LAMMPS, PLUMED v2.9] -> stage not stated [PySCF]

### Chelation-induced anti-Ostwald ripening: Ultrafine bismuth nanocrystals for ultrastable aqueous sodium storage. (PNAS 2025)

- DOI: 10.1073/pnas.2505640122 | PMCID: PMC12452901 | PMID: 40932773
- Evidence: All the molecular dynamics simulations were performed in the framework of the reactive force field (ReaxFF) by the LAMMPS program package ( 54 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Tuning water dissociation at oxide-electrolyte interfaces with electric fields. (PNAS 2025)

- DOI: 10.1073/pnas.2505929122 | PMCID: PMC12403145 | PMID: 40833416
- Evidence: The DPLR molecular dynamics simulations were then carried out using LAMMPS ( 55 ) in conjunction with the revised DeePMD-kit package ( 54 ).
- Full pipeline: simulation/modelling [LAMMPS]

### CO&lt;sub&gt;2&lt;/sub&gt; hydration at the air-water interface: A surface-mediated "in-and-out" mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2502684122 | PMCID: PMC12402993 | PMID: 40833411
- Evidence: Well-tempered metadynamics was performed by coupling LAMMPS with the multiple walker setup available in PLUMED ( 74 – 76 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [LAMMPS, PLUMED]

### Dipole-induced transition in 3 dimensions. (PNAS 2025)

- DOI: 10.1073/pnas.2427273122 | PMCID: PMC12358875 | PMID: 40773229
- Evidence: Open source code LAMMPS ( 6 ) is used to perform the simulations.
- Full pipeline: simulation/modelling [LAMMPS]

### Computational investigation of water glasses using machine-learning potentials. (PNAS 2025)

- DOI: 10.1073/pnas.2509609122 | PMCID: PMC12358917 | PMID: 40763030
- Evidence: Materials and Methods We performed all MD simulations with both SCAN- and MBpol-based Deep Potential models with the LAMMPS simulation software, version 2 August 2023 ( 94 ) patched with the DPMD-kit, version 3.0.0 ( 51 , 54 ).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [GROMACS v2019.6]

### Water content modulation enables selective ion transport in 2D MXene membranes. (PNAS 2025)

- DOI: 10.1073/pnas.2501017122 | PMCID: PMC12304981 | PMID: 40658858
- Evidence: Simulations were performed using LAMMPS ( 69 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Strong strain dependence of friction in graphene kirigami allows engineering a negative coefficient of friction. (PNAS 2025)

- DOI: 10.1073/pnas.2501728122 | PMCID: PMC12280895 | PMID: 40643976
- Evidence: The simulation procedure is implemented and carried out using LAMMPS ( 34 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Structural state governs the mechanism of shear-band propagation in metallic glasses. (PNAS 2025)

- DOI: 10.1073/pnas.2427082122 | PMCID: PMC12260437 | PMID: 40591594
- Evidence: Simulations were conducted in the variable-cell semigrand canonical ensemble with a variance parameter κ set to 1,000 effectively integrated into the LAMMPS simulation package ( 61 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Onset of cavitation and vapor bubble development over hydrophilic and hydrophobic surfaces. (PNAS 2025)

- DOI: 10.1073/pnas.2503033122 | PMCID: PMC12260580 | PMID: 40591596
- Evidence: Data, Materials, and Software Availability Simulations are performed using the open-source DPD-MESO package in the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS).
- Full pipeline: simulation/modelling [LAMMPS]

### Pressure-driven electronegativity inversion in alkali liquids. (PNAS 2025)

- DOI: 10.1073/pnas.2424701122 | PMCID: PMC12232675 | PMID: 40553500
- Evidence: All simulations were carried out using the LAMMPS package ( 50 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Multistage nucleation pathway in LiF molten salt mirrors the crystal-melt interface structure. (PNAS 2025)

- DOI: 10.1073/pnas.2425702122 | PMCID: PMC12207450 | PMID: 40540599
- Evidence: All MD simulations were carried out using the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) ( 82 ).
- Full pipeline: simulation/modelling [LAMMPS] -> machine learning [TensorFlow]

### Surface melting-driven hydrogen absorption for high-pressure polyhydride synthesis. (PNAS 2025)

- DOI: 10.1073/pnas.2413480122 | PMCID: PMC12146707 | PMID: 40440065
- Evidence: The large-scale atomic/molecular massively parallel simulator [LAMMPS ( 66 )] was used for MD simulations.
- Full pipeline: simulation/modelling [LAMMPS]

### Interspecies interactions in dual, fibrous gels enable control of gel structure and rheology. (PNAS 2025)

- DOI: 10.1073/pnas.2423293122 | PMCID: PMC12088379 | PMID: 40327689
- Evidence: All simulations are performed in a version of the software Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) ( 57 ) suitably modified to include this energy function.
- Full pipeline: simulation/modelling [LAMMPS]

### Unsupervised learning of structural relaxation in supercooled liquids from short-term fluctuations. (PNAS 2025)

- DOI: 10.1073/pnas.2427246122 | PMCID: PMC12012455 | PMID: 40215273
- Evidence: We performed molecular dynamics simulations using the package LAMMPS ( 39 ) to obtain equilibrium configurations at reduced temperatures ranging from 0.44 to 0.56.
- Full pipeline: simulation/modelling [LAMMPS]

### Revealing the roles of the solid-electrolyte interphase in designing stable, fast-charging, low-temperature Li-ion batteries. (PNAS 2025)

- DOI: 10.1073/pnas.2420398122 | PMCID: PMC12002247 | PMID: 40127272
- Evidence: All-atom MD simulations were conducted using LAMMPS) ( 35 ) with the OPLS-AA force field ( 36 ) to describe atomic interactions.
- Full pipeline: simulation/modelling [LAMMPS]

### Defects induce phase transition from dynamic to static rippling in graphene. (PNAS 2025)

- DOI: 10.1073/pnas.2416932122 | PMCID: PMC11892612 | PMID: 40020187
- Evidence: The simulations were performed at 300 K and zero stress, with periodic boundary conditions, using the LAMMPS software package ( 70 ).
- Full pipeline: simulation/modelling [LAMMPS, MDAnalysis, Python]

### Multiscale toughening mechanisms in biomimetic tendon-like hydrogels. (PNAS 2025)

- DOI: 10.1073/pnas.2424124122 | PMCID: PMC11892624 | PMID: 40014567
- Evidence: Molecular dynamics simulations were conducted using LAMMPS, and the resulting numerical data were analyzed with OVITO.
- Full pipeline: simulation/modelling [LAMMPS]

### Receptor clustering tunes and sharpens the selectivity of multivalent binding. (PNAS 2025)

- DOI: 10.1073/pnas.2417159122 | PMCID: PMC11848318 | PMID: 39951501
- Evidence: The membrane is modeled using a coarse-grained one-particle thick model ( 34 ), implemented in the LAMMPS Molecular Dynamics package ( 44 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Resolving the dynamic correlated disorder in KTa&lt;sub&gt;1-&lt;i&gt;x&lt;/i&gt;&lt;/sub&gt;Nb&lt;sub&gt;&lt;i&gt;x&lt;/i&gt;&lt;/sub&gt;O&lt;sub&gt;3&lt;/sub&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2419159122 | PMCID: PMC11848325 | PMID: 39928874
- Evidence: MLMD with NVT ensemble were performed at 100 and 300 K with trajectory length 20 ps and 2 fs/step using LAMMPS ( 90 ).
- Full pipeline: simulation/modelling [LAMMPS]

### A planar-sheet nongraphitic zero-bandgap sp&lt;sup&gt;2&lt;/sup&gt; carbon phase made by the low-temperature reaction of γ-graphyne. (PNAS 2025)

- DOI: 10.1073/pnas.2413194122 | PMCID: PMC11804621 | PMID: 39874293
- Evidence: Unless otherwise mentioned, the DFT calculations were done with the Vienna Ab-Initio Simulation Package ( 30 ), and the MD simulations were performed using the LAMMPS package ( 18 ).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [Quantum ESPRESSO]

### Macromolecular interactions and geometrical confinement determine the 3D diffusion of ribosome-sized particles in live &lt;i&gt;Escherichia coli&lt;/i&gt; cells. (PNAS 2025)

- DOI: 10.1073/pnas.2406340121 | PMCID: PMC11789073 | PMID: 39854229
- Evidence: 1 C ) using the massively parallelized molecular dynamics package LAMMPS ( 71 ).
- Full pipeline: simulation/modelling [LAMMPS, VMD] -> visualisation [VMD]

### Automating alloy design and discovery with physics-aware multimodal multiagent AI. (PNAS 2025)

- DOI: 10.1073/pnas.2414074122 | PMCID: PMC11789045 | PMID: 39854228
- Evidence: However, computing various material properties often requires setting up different structures, writing and adjusting multiple LAMMPS scripts, and running numerous simulations, which becomes cumbersome when studying a broad range of materials, especially in alloy design.
- Full pipeline: simulation/modelling [ASE, LAMMPS, Python]

### Strong adsorption of guanidinium cations to the air-water interface. (PNAS 2025)

- DOI: 10.1073/pnas.2418443122 | PMCID: PMC11745392 | PMID: 39792292
- Evidence: In order to gain molecular insight into the driving forces for Gdm + adsorption, we performed molecular dynamics simulations with the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) software package ( 50 ).
- Full pipeline: simulation/modelling [LAMMPS]

### Monofluorinated acetal electrolyte for high-performance lithium metal batteries. (PNAS 2025)

- DOI: 10.1073/pnas.2418623122 | PMCID: PMC11745313 | PMID: 39772742
- Evidence: Classical, fixed-charge MD was conducted using LAMMPS from initial amorphous configurations with ~500 molecules with compositions corresponding to the experimentally investigated systems.
- Full pipeline: simulation/modelling [VMD] -> stage not stated [LAMMPS]

### Moisture-driven carbonation kinetics for ultrafast CO&lt;sub&gt;2&lt;/sub&gt; mineralization. (PNAS 2025)

- DOI: 10.1073/pnas.2418239121 | PMCID: PMC11725878 | PMID: 39793077
- Evidence: The property calculations for this study were conducted using the LAMMPS ( 56 ) package, operating under the canonical (NVT) ensemble at a constant temperature of 298 K.
- Full pipeline: simulation/modelling [PLUMED] -> stage not stated [LAMMPS]

### Extended Rice-Thomson analysis and atomistic simulations revealing grain boundary effects on fracture in refractory high-entropy alloys. (PNAS 2026)

- DOI: 10.1073/pnas.2536219123 | PMCID: PMC13080029 | PMID: 41955106
- Evidence: The resulting structures were quenched to 0 K using the conjugate gradient (CG) algorithm in LAMMPS ( 43 , 44 ) with an energy tolerance of 1 × 10 − 9 .
- Full pipeline: stage not stated [LAMMPS]

### Giant photorefractive and photoexpansion effects in a van der Waals semiconductor. (PNAS 2026)

- DOI: 10.1073/pnas.2531552123 | PMCID: PMC13037868 | PMID: 41894327
- Evidence: All MD simulations were performed using the LAMMPS software package ( 75 ), in combination with the modern machine-learning interatomic potential PET-MAD, which demonstrates superior accuracy in modeling the energies of a wide range of atomic structures ( 76 ).
- Full pipeline: simulation/modelling [LAMMPS]

