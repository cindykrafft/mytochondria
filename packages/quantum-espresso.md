# Quantum ESPRESSO

- **Category:** md
- **Papers in survey:** 27
- **Journals:** PNAS (22), Nature (5)
- **Years:** 2021 (2), 2022 (4), 2023 (6), 2024 (6), 2025 (7), 2026 (2)
- **Versions named:** 6.4.1 (1), 6.3 (1)
- **Pipeline stages it appears in:** simulation/modelling (6)

## Papers

### Switchable chiral transport in charge-ordered kagome metal CsV<sub>3</sub>Sb<sub>5</sub>. (Nature 2022)

- DOI: 10.1038/s41586-022-05127-9 | PMCID: PMC9668744 | PMID: 36224393
- Evidence: 1 Basic properties of CsV 3 Sb 5 . a , Crystal structure of CsV 3 Sb 5 . b , XRD pattern of the (001) facet of a CsV 3 Sb 5 crystal. c , Band structure of CsV 3 Sb 5 calculated by density functional theory (DFT) using the Quantum Espresso package (QE) 41 . d , Field dependence of magnetoresistivity and Hall resistivity measured at T = 5 K.
- Full pipeline: stage not stated [QUAST, Quantum ESPRESSO]

### Control of proton transport and hydrogenation in double-gated graphene. (Nature 2024)

- DOI: 10.1038/s41586-024-07435-8 | PMCID: PMC11186788 | PMID: 38898294
- Evidence: DFT calculations of proton transport through graphene The DFT calculations of proton transport through graphene were performed using VASP 63 – 66 and the plane-wave self-consistent field (PWscf) package with Quantum Espresso (QE).
- Full pipeline: stage not stated [Quantum ESPRESSO]

### Single nuclear spin detection and control in a van der Waals material. (Nature 2025)

- DOI: 10.1038/s41586-025-09258-7 | PMCID: PMC12286849 | PMID: 40634604
- Evidence: DFT calculations We use Quantum Espresso 40 , an open-source plane-wave software, to perform the DFT calculations.
- Full pipeline: stage not stated [Quantum ESPRESSO]

### Bottom-up synthesis of molecular nanodiamond from nanographene. (Nature 2026)

- DOI: 10.1038/s41586-026-10669-3 | PMCID: PMC13323094 | PMID: 42191905
- Evidence: Ab initio simulations To investigate structural transformations and high-strain resulting from high-pressure conditions, ab initio calculations using the plane wave approach implemented in the Quantum ESPRESSO package 43 – 45 have been performed.
- Full pipeline: simulation/modelling [Quantum ESPRESSO] -> stage not stated [SciPy]

### Structural modifications in strain-engineered bilayer nickelate thin films. (Nature 2026)

- DOI: 10.1038/s41586-026-10446-2 | PMCID: PMC13149027 | PMID: 41922777
- Version used: **6.4.1**
- Evidence: Band-structure calculations were performed in Quantum ESPRESSO v6.4.1.
- Full pipeline: stage not stated [Quantum ESPRESSO v6.4.1]

### Short hydrogen bonds enhance nonaromatic protein-related fluorescence. (PNAS 2021)

- DOI: 10.1073/pnas.2020389118 | PMCID: PMC8166056 | PMID: 34001606
- Evidence: Calculations were performed using both the CRYSTAL17 ( 15 ) and Quantum ESPRESSO ( 16 ) software packages.
- Full pipeline: stage not stated [Quantum ESPRESSO]

### Evidence of ideal excitonic insulator in bulk MoS<sub>2</sub> under pressure. (PNAS 2021)

- DOI: 10.1073/pnas.2010110118 | PMCID: PMC8020749 | PMID: 33758098
- Evidence: The lattice parameters and the ground-state electronic structure for the three values of pressure were obtained within DFT, with a plane wave basis set as implemented in the Quantum ESPRESSO package ( 52 , 53 ), using the generalized gradient approximation Perdew–Burke–Ernzerhof (PBE) parameterization ( 54 ).
- Full pipeline: stage not stated [Quantum ESPRESSO]

### Ultrahigh-pressure disordered eight-coordinated phase of Mg<sub>2</sub>GeO<sub>4</sub>: Analogue for super-Earth mantles. (PNAS 2022)

- DOI: 10.1073/pnas.2114424119 | PMCID: PMC8872715 | PMID: 35165195
- Evidence: The resulting structures were then optimized using Quantum Espresso ( 17 ).
- Full pipeline: stage not stated [Quantum ESPRESSO]

### A complete description of thermodynamic stabilities of molecular crystals. (PNAS 2022)

- DOI: 10.1073/pnas.2111769119 | PMCID: PMC8832981 | PMID: 35131847
- Version used: **6.3**
- Evidence: The PBE-TS baseline calculations for a Δ -learning approach were performed using Quantum Espresso v6.3, the same k-point grid, a wavefunction cutoff energy of 100 Rydberg, and the optimized, norm-conserving Vanderbilt pseudopotentials from ref.
- Full pipeline: simulation/modelling [Jupyter] -> stage not stated [Quantum ESPRESSO v6.3]

### Thermal conductivity of Fe-Si alloys and thermal stratification in Earth's core. (PNAS 2022)

- DOI: 10.1073/pnas.2119001119 | PMCID: PMC8740763 | PMID: 34969863
- Evidence: FPMD simulations for Fe-Si were performed using Quantum ESPRESSO ( 81 ).
- Full pipeline: simulation/modelling [Quantum ESPRESSO]

### Observation of the most H<sub>2</sub>-dense filled ice under high pressure. (PNAS 2023)

- DOI: 10.1073/pnas.2312665120 | PMCID: PMC10756306 | PMID: 38109537
- Evidence: The C 2 and C 3 phases were simulated using Density Functional (Perturbation) Theory as implemented in Quantum ESPRESSO ( 50 , 51 ), using Optimized Norm-Conserving Vanderbilt pseudopotentials (ONCV) ( 52 ) and optimized Becke88 van der Waals exchange-correlation functional ( 53 – 55 ).
- Full pipeline: simulation/modelling [Quantum ESPRESSO]

### Light-induced shift current vortex crystals in moiré heterobilayers. (PNAS 2023)

- DOI: 10.1073/pnas.2314775120 | PMCID: PMC10741382 | PMID: 38085781
- Evidence: The ground-state electronic properties (mean-field orbital energies, wavefunctions, etc.) are obtained by density functional theory (DFT) with the Quantum Espresso package ( 58 ).
- Full pipeline: alignment/mapping [LAMMPS] -> simulation/modelling [LAMMPS] -> stage not stated [Quantum ESPRESSO]

### The role of dynamics in heterogeneous catalysis: Surface diffusivity and N<sub>2</sub> decomposition on Fe(111). (PNAS 2023)

- DOI: 10.1073/pnas.2313023120 | PMCID: PMC10723053 | PMID: 38060558
- Evidence: In both cases, simulations are performed using the PWscf code of Quantum ESPRESSO ( 73 – 75 ) supplemented by the PLUMED plugin ( 76 ) which is an open-source, community-developed library ( 77 ) for enhanced sampling calculations.
- Full pipeline: simulation/modelling [LAMMPS, PLUMED, Quantum ESPRESSO] -> stage not stated [VMD]

### Compass-like manipulation of electronic nematicity in Sr<sub>3</sub>Ru<sub>2</sub>O<sub>7</sub>. (PNAS 2023)

- DOI: 10.1073/pnas.2308972120 | PMCID: PMC10483601 | PMID: 37639583
- Evidence: We obtain the tight-binding model for a free-standing Sr 2 RuO 4 layer with octahedral rotations from a paramagnetic DFT calculation using Quantum Espresso ( 34 ), using the Perdew–Burke–Ernzerhof exchange correlation functional, a k -grid of 8 × 8 × 1 , a wavefunction cutoff of E cut , wfc = 90 Ry , and a density cutoff of E cut , ρ = 720 Ry .
- Full pipeline: stage not stated [Quantum ESPRESSO]

### PBE-GGA predicts the B8↔B2 phase boundary of FeO at Earth's core conditions. (PNAS 2023)

- DOI: 10.1073/pnas.2304726120 | PMCID: PMC10334785 | PMID: 37399372
- Evidence: DFT and DFPT calculations were performed using the PAW method ( 33 ) as implemented in Quantum ESPRESSO ( 34 ).
- Full pipeline: stage not stated [Quantum ESPRESSO]

### Dislocation-tuned ferroelectricity and ferromagnetism of the BiFeO<sub>3</sub>/SrRuO<sub>3</sub> interface. (PNAS 2023)

- DOI: 10.1073/pnas.2213650120 | PMCID: PMC10068816 | PMID: 36940334
- Evidence: The first-principles calculations were performed within Quantum ESPRESSO using the projector augmented wave pseudopotential Perdew–Burke–Enzerhof exchange-correlation functional.
- Full pipeline: stage not stated [Quantum ESPRESSO]

### Designing multicomponent hydrides with potential high T&lt;sub&gt;&lt;i&gt;c&lt;/i&gt;&lt;/sub&gt; superconductivity. (PNAS 2024)

- DOI: 10.1073/pnas.2413096121 | PMCID: PMC11551333 | PMID: 39485794
- Evidence: We used Quantum Espresso’s default atomic projections for the PDOS calculations.
- Full pipeline: stage not stated [Quantum ESPRESSO]

### Topological polarons in halide perovskites. (PNAS 2024)

- DOI: 10.1073/pnas.2318151121 | PMCID: PMC11127022 | PMID: 38758696
- Evidence: Materials and Methods All ab initio DFT calculations are performed using the Quantum ESPRESSO package ( 81 ) (electronic structure and lattice vibrational properties), the Wannier90 code ( 82 ) (maximally localized Wannier functions) and the EPW code ( 83 , 84 ) (interpolation of electron–phonon matrix elements and polarons).
- Full pipeline: stage not stated [Quantum ESPRESSO]

### Chemical bonding dictates drastic critical temperature difference in two seemingly identical superconductors. (PNAS 2024)

- DOI: 10.1073/pnas.2316101121 | PMCID: PMC10998635 | PMID: 38547068
- Evidence: Band and k-point resolved electron–phonon coupling magnitudes, directly proportional to phonon linewidths (taken at the fourth smearing number), were computed using Quantum Espresso ( 79 , 80 ) via the same DFT parameters as in VASP and overlaid onto phonon dispersion plots.
- Full pipeline: normalisation [ASE] -> simulation/modelling [ASE] -> stage not stated [Quantum ESPRESSO]

### Laser direct overall water splitting for H<sub>2</sub> and H<sub>2</sub>O<sub>2</sub> production. (PNAS 2024)

- DOI: 10.1073/pnas.2319286121 | PMCID: PMC10907277 | PMID: 38394244
- Evidence: The nonadiabatic ab initio molecular dynamics simulations were performed via the rt-TDDFT algorithm ( 45 ) as implemented in the plane-wave code Quantum Espresso ( 46 ).
- Full pipeline: simulation/modelling [Quantum ESPRESSO]

### Tailoring chemical bonds to design unconventional glasses. (PNAS 2024)

- DOI: 10.1073/pnas.2316498121 | PMCID: PMC10786265 | PMID: 38170754
- Evidence: PAW SCF wave function calculations for all the systems for which LIs and DIs have been calculated were performed with the pw.x module of the Quantum Espresso (QE) package ( 39 ).
- Full pipeline: stage not stated [Quantum ESPRESSO]

### Defects at play: Shaping the photophysics and photochemistry of ice. (PNAS 2025)

- DOI: 10.1073/pnas.2516805122 | PMCID: PMC12663945 | PMID: 41264242
- Evidence: As the ID and combined vacancy-ionic defect models carry a total charge of − 1, a uniform compensating jellium background was automatically introduced to ensure electrostatic convergence under periodic boundary conditions, as implemented in the Quantum ESPRESSO package ( 76 , 77 ).
- Full pipeline: stage not stated [Quantum ESPRESSO, SciPy]

### Hund's flat band in a frustrated spinel oxide. (PNAS 2025)

- DOI: 10.1073/pnas.2518213122 | PMCID: PMC12626020 | PMID: 41196354
- Evidence: DFT calculations are performed using the Quantum Espresso software package using the ONCVPSP norm-conserving pseudopotentials ( 78 , 79 ) in conjunction with the Perdew–Burke–Ernzerhof exchange-correlation functional.
- Full pipeline: stage not stated [QUAST, Quantum ESPRESSO]

### Visualization of spin-orbit-entangled 4f electrons in crystalline materials. (PNAS 2025)

- DOI: 10.1073/pnas.2500251122 | PMCID: PMC12541313 | PMID: 41052343
- Evidence: To obtain the atomic form factors for the CDFS analysis, fully relativistic all-electron calculations based on the density functional theory (DFT) were performed for isolated O, Pr, Nd, Eu, and Ir atoms using Quantum ESPRESSO ( 44 ).
- Full pipeline: stage not stated [Quantum ESPRESSO]

### Monitoring chalcogenide ions-guided in situ transform active sites of tailored bismuth electrocatalysts for CO&lt;sub&gt;2&lt;/sub&gt; reduction to formate. (PNAS 2025)

- DOI: 10.1073/pnas.2420922122 | PMCID: PMC11912470 | PMID: 40042908
- Evidence: First-principles AIMD simulations were performed using Quantum ESPRESSO@7.2 and the exchange-correlation functional was GGA-PBE.
- Full pipeline: simulation/modelling [Quantum ESPRESSO]

### Creation, stabilization, and investigation at ambient pressure of pressure-induced superconductivity in Bi&lt;sub&gt;0.5&lt;/sub&gt;Sb&lt;sub&gt;1.5&lt;/sub&gt;Te&lt;sub&gt;3&lt;/sub&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2423102122 | PMCID: PMC11831210 | PMID: 39903112
- Evidence: To account for the doping system in BST, we utilized the virtual crystal approximation in Quantum Espresso, which posed a technical challenge for calculating the properties of the surface states.
- Full pipeline: stage not stated [Quantum ESPRESSO]

### A planar-sheet nongraphitic zero-bandgap sp&lt;sup&gt;2&lt;/sup&gt; carbon phase made by the low-temperature reaction of γ-graphyne. (PNAS 2025)

- DOI: 10.1073/pnas.2413194122 | PMCID: PMC11804621 | PMID: 39874293
- Evidence: A quite similar 0 K enthalpy difference between 5,6,9 ringene and unreacted graphyne was obtained using MD (ReaxFF potential), DFT, and Quantum Espresso (QE) calculations (−1.84, −2.21, and −2.17 kJ/g, respectively).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [Quantum ESPRESSO]

