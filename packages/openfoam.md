# OpenFOAM

- **Category:** physical
- **Papers in survey:** 10
- **Journals:** PNAS (9), Nature (1)
- **Years:** 2023 (4), 2024 (3), 2025 (2), 2026 (1)
- **Versions named:** 9.0 (1)
- **Pipeline stages it appears in:** simulation/modelling (4)

## Papers

### Adaptations for stealth in the wing-like flippers of a large ichthyosaur. (Nature 2025)

- DOI: 10.1038/s41586-025-09271-w | PMCID: PMC12390834 | PMID: 40670791
- Evidence: All computations were done using the pimpleFoam solver, which is part of the OpenFOAM package (an open-source computational fluid dynamics software).
- Full pipeline: stage not stated [OpenFOAM]

### Triggering interfacial instabilities during forced imbibition by adjusting the aspect ratio in depth-variable microfluidic porous media. (PNAS 2023)

- DOI: 10.1073/pnas.2310584120 | PMCID: PMC10723151 | PMID: 38048464
- Evidence: We study the immiscible imbibition by preformation of the Navier–Stokes equations with the open-source platform OpenFOAM, where the volume-of-fluid method (interface tracking approach) is applied and has emerged as a powerful tool for diagnosing pore-scale multiphase flow problems.
- Full pipeline: stage not stated [OpenFOAM]

### Hybrid quantum algorithms for flow problems. (PNAS 2023)

- DOI: 10.1073/pnas.2311014120 | PMCID: PMC10710031 | PMID: 38039273
- Evidence: On the other hand, there are software applications such as ANSYS and OpenFOAM that perform solely classical CFD simulations.
- Full pipeline: simulation/modelling [OpenFOAM]

### Scientific machine learning for modeling and simulating complex fluids. (PNAS 2023)

- DOI: 10.1073/pnas.2304669120 | PMCID: PMC10318955 | PMID: 37364093
- Version used: **9.0**
- Evidence: The CFD simulation presented in this work was performed using OpenFOAM v9.0 ( 39 ) with the rheoTool package v5.0 ( 40 ).
- Full pipeline: simulation/modelling [OpenFOAM v9.0]

### Lagrangian stretching reveals stress topology in viscoelastic flows. (PNAS 2023)

- DOI: 10.1073/pnas.2211347120 | PMCID: PMC9945992 | PMID: 36701365
- Evidence: Numerical simulations are implemented using OpenFOAM ( 48 ) and RheoTool ( 49 ).
- Full pipeline: simulation/modelling [OpenFOAM]

### Permeability-selectivity trade-off for a universal leaky channel inspired by mobula filters. (PNAS 2024)

- DOI: 10.1073/pnas.2410018121 | PMCID: PMC11648657 | PMID: 39586001
- Evidence: Fluid flow in the leaky channel is simulated using a pressure-based finite-volume solver, where 2D and 3D simulations are realized in Ansys Fluent and OpenFOAM, respectively (see inlet velocity profiles and definitions of boundary conditions in SI Appendix , Text B and Fig.
- Full pipeline: simulation/modelling [OpenFOAM]

### A network model to predict ionic transport in porous materials. (PNAS 2024)

- DOI: 10.1073/pnas.2401656121 | PMCID: PMC11145279 | PMID: 38787880
- Evidence: The finite-volume method ( 57 , 58 ) was employed for the solution using the open-source software OpenFOAM ( 59 , 60 ).
- Full pipeline: stage not stated [OpenFOAM]

### How particle shape affects granular segregation in industrial and geophysical flows. (PNAS 2024)

- DOI: 10.1073/pnas.2307061121 | PMCID: PMC10861863 | PMID: 38285942
- Evidence: ...-sheared granular bed, the computations were carried out by using the open-source code CFDEM ( 55 ), that couples LIGGGHTS (described previously) and OpenFOAM (which computes the fluid motion in an Eulerian frame).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [OpenFOAM]

### Flamingos use their L-shaped beak and morphing feet to induce vortical traps for prey capture. (PNAS 2025)

- DOI: 10.1073/pnas.2503495122 | PMCID: PMC12130884 | PMID: 40354558
- Evidence: The k-omega SST turbulence and Reynolds averaged Navier–Stokes (RANS) models were used in a finite volume method-based open-source library OpenFOAM ( 38 ).
- Full pipeline: stage not stated [OpenFOAM]

### Fast automated adjoints for spectral PDE solvers. (PNAS 2026)

- DOI: 10.1073/pnas.2530440123 | PMCID: PMC13080004 | PMID: 41961849
- Evidence: This includes SU 2 ( 14 ), FEniCS ( 15 ), Firedrake ( 16 ), Φ Flow ( 17 ), simsopt ( 10 ), OpenFOAM ( 18 ), Exponax ( 19 ), JaxFluids ( 20 , 21 ), JAX-CFD ( 22 , 23 ), Trixi.jl ( 24 ), and Julia’s SciML ecosystem ( 25 ).
- Full pipeline: simulation/modelling [PyTorch] -> machine learning [PyTorch] -> stage not stated [OpenFOAM, Python, SciPy]

