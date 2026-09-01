# REFMAC

- **Category:** structbio
- **Papers in survey:** 26
- **Journals:** PNAS (15), Nature (8), Cell (2), Science (1)
- **Years:** 2021 (3), 2022 (7), 2023 (9), 2024 (4), 2025 (2), 2026 (1)
- **Versions named:** 5.8 (2), 5.8.0258 (1)
- **Pipeline stages it appears in:** structure determination (21), machine learning (2), differential/statistical testing (1)

## Papers

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Evidence: ....cgic Phenix Liebschner et al., 2019 https://doi.org/10.1107/S2059798319011471 COOT Emsley and Cowtan, 2004 https://doi.org/10.1107/S0907444904019158 REFMAC Murshudov et al., 2011 https://doi.org/10.1107/S0907444911001314 CCP4i2 interface Potterton et al., 2018 https://doi.org/10.1107/S2059798317016035 Super-Pose Maiti et al., 2004 https://doi.org/10.1093/nar/gkh477 Privateer, MKIV version Agirre ...
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### Emergence of immune escape at dominant SARS-CoV-2 killer T cell epitope. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.002 | PMCID: PMC9279490 | PMID: 35931021
- Version used: **5.8**
- Evidence: ..., RRID: SCR_007255 PHASER 2.7 Phoenix Online PHASER, RRID: SCR_014219 Win-COOT 0.9.6 Science and Technology Facilities Council COOT, RRID: SCR_014222 REFMAC 5.8 Science and Technology Facilities Council REFMAC5, RRID: SCR_014225 Other FACSAria II BD Biosciences 643178 Sony MA900 Sorter Sony N/A ACEA NovoCyte 3005 with NovoSampler pro ACEA, Agilent N/A BD FACSCanto II BD Biosciences N/A MACSmix tub...
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT] -> stage not stated [CCP4 v7.1, PyMOL v2.3.4, R v4.0, REFMAC v5.8, tidyverse]

### A peroxisomal ubiquitin ligase complex forms a retrotranslocation channel. (Nature 2022)

- DOI: 10.1038/s41586-022-04903-x | PMCID: PMC9279156 | PMID: 35768507
- Evidence: Refinement was carried out with REFMAC 56 .
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, REFMAC, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.1]

### Phosphoantigens glue butyrophilin 3A1 and 2A1 to activate Vγ9Vδ2 T cells. (Nature 2023)

- DOI: 10.1038/s41586-023-06525-3 | PMCID: PMC10533412 | PMID: 37674084
- Evidence: All structures were refined with COOT and REFMAC 42 – 44 .
- Full pipeline: structure determination [REFMAC] -> visualisation [PyMOL]

### A small-molecule PI3Kα activator for cardioprotection and neuroregeneration. (Nature 2023)

- DOI: 10.1038/s41586-023-05972-2 | PMCID: PMC7614683 | PMID: 37225977
- Evidence: Models were manually adjusted to the densities, using COOT 68 , and the structures were refined firstly with REFMAC 70 and with PHENIX 67 at later stages.
- Full pipeline: quantification [R v4.0.0] -> differential/statistical testing [R v4.0.0] -> structure determination [PHENIX, REFMAC] -> stage not stated [CCP4, ImageJ, PyMOL]

### mRNA decoding in human is kinetically and structurally distinct from bacteria. (Nature 2023)

- DOI: 10.1038/s41586-023-05908-w | PMCID: PMC10156603 | PMID: 37020024
- Evidence: Cross-validation was used to optimize the weight on the experimental density in REFMAC to prevent overfitting 73 .
- Full pipeline: registration [MotionCor2] -> structure determination [CCP4] -> machine learning [REFMAC] -> stage not stated [ChimeraX, Coot, RELION v3.1, UCSF Chimera]

### Fast and sensitive GCaMP calcium indicators for imaging neural populations. (Nature 2023)

- DOI: 10.1038/s41586-023-05828-9 | PMCID: PMC10060165 | PMID: 36922596
- Evidence: Refinement was performed using REFMAC 57 followed by manual remodelling with Coot 58 .
- Full pipeline: structure determination [REFMAC] -> stage not stated [CaImAn, PyMOL, Python, Suite2p, ilastik]

### The ultra-high affinity transport proteins of ubiquitous marine bacteria. (Nature 2024)

- DOI: 10.1038/s41586-024-07924-w | PMCID: PMC11485210 | PMID: 39261732
- Evidence: The structures were then refined by iterative real-space and reciprocal-space refinement in REFMAC 78 , Phenix 79 , and COOT 80 .
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> structure determination [PHENIX, REFMAC] -> stage not stated [AlphaFold]

### Discovery of potent small-molecule inhibitors of lipoprotein(a) formation. (Nature 2024)

- DOI: 10.1038/s41586-024-07387-z | PMCID: PMC11111404 | PMID: 38720069
- Version used: **5.8**
- Evidence: The initial structure coordinates for the dataset were further refined using REFMAC v.5.8 (CCP4), applying anisotropic temperature factors.
- Full pipeline: normalisation [CCP4 v6.5] -> structure determination [REFMAC v5.8] -> stage not stated [Coot v0.8]

### The UFM1 E3 ligase recognizes and releases 60S ribosomes from ER translocons. (Nature 2024)

- DOI: 10.1038/s41586-024-07093-w | PMCID: PMC10937380 | PMID: 38383789
- Evidence: Refinement and model building was performed using REFMAC 60 and Coot 50 (CCP4i2 suite), respectively.
- Full pipeline: registration [RELION v3.1] -> structure determination [AlphaFold, ChimeraX v1.2.5, REFMAC] -> machine learning [cryoDRGN v3.2.0] -> stage not stated [CCP4, Coot v0.9.8.1, PHENIX v1.2.1]

### Potency boost of a <i>Mycobacterium tuberculosis</i> dihydrofolate reductase inhibitor by multienzyme F<sub>420</sub>H<sub>2</sub>-dependent reduction. (PNAS 2021)

- DOI: 10.1073/pnas.2025172118 | PMCID: PMC8237569 | PMID: 34161270
- Evidence: Model building, including manually modeling F 420 into the difference density (mFo–DFc) at the binding site, was done with COOT ( 60 ) and refined using REFMAC ( 61 ).
- Full pipeline: structure determination [REFMAC]

### 2'-O methylation of RNA cap in SARS-CoV-2 captured by serial crystallography. (PNAS 2021)

- DOI: 10.1073/pnas.2100170118 | PMCID: PMC8166198 | PMID: 33972410
- Version used: **5.8.0258**
- Evidence: The structures were refined by multiple cycles in REFMAC v.
- Full pipeline: alignment/mapping [UCSF Chimera] -> structure determination [REFMAC v5.8.0258] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot]

### Cooperativity between the orthosteric and allosteric ligand binding sites of RORγt. (PNAS 2021)

- DOI: 10.1073/pnas.2021287118 | PMCID: PMC8017705 | PMID: 33536342
- Evidence: REFMAC and Crystallographic Object-Oriented Toolkit (COOT) were used for sequential refinement and model building ( 55 , 56 ).
- Full pipeline: simulation/modelling [GROMACS v2019.3] -> structure determination [PHENIX, REFMAC] -> stage not stated [CCP4, PyMOL v2.2.3]

### Human T cells recognize HLA-DP-bound peptides in two orientations. (PNAS 2022)

- DOI: 10.1073/pnas.2214331119 | PMCID: PMC9894132 | PMID: 36442096
- Evidence: Iterative rounds of model building in Coot and restrained refinement using REFMAC (CCP4 suite) ( 27 ) and PhenixRefine (PHENIX) ( 28 ) were carried out.
- Full pipeline: structure determination [Coot, PHENIX, REFMAC] -> machine learning [Coot, PHENIX, REFMAC] -> visualisation [PyMOL] -> stage not stated [CCP4]

### Mechanism-based heparanase inhibitors reduce cancer metastasis in vivo. (PNAS 2022)

- DOI: 10.1073/pnas.2203167119 | PMCID: PMC9351465 | PMID: 35881786
- Evidence: Electron density for sidechains is REFMAC σ A -weighted 2mFo-DFc, contoured to 1σ (0.23–0.26 e − .Å −3 ).
- Full pipeline: stage not stated [REFMAC]

### The flagellar motor protein FliL forms a scaffold of circumferentially positioned rings required for stator activation. (PNAS 2022)

- DOI: 10.1073/pnas.2118401119 | PMCID: PMC8794807 | PMID: 35046042
- Evidence: Refinement and automated placement of ordered water molecules was performed using PHENIX ( 56 ) and REFMAC ( 57 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [PHENIX, REFMAC] -> stage not stated [ChimeraX, PyMOL]

### Oxidative desulfurization pathway for complete catabolism of sulfoquinovose by bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2116022119 | PMCID: PMC8795539 | PMID: 35074914
- Evidence: Structures were built and refined by iterative cycles using Coot ( 46 ) and REFMAC ( 47 ) or Phenix ( 48 ), the latter employing local noncrystallographic symmetry restraints.
- Full pipeline: dimensionality reduction/clustering [BLAST] -> structure determination [PHENIX, REFMAC]

### GAS41 promotes H2A.Z deposition through recognition of the N terminus of histone H3 by the YEATS domain. (PNAS 2023)

- DOI: 10.1073/pnas.2304103120 | PMCID: PMC10614846 | PMID: 37844223
- Evidence: Model building was accomplished with Coot ( 65 ), and structural refinement was performed with REFMAC ( 66 ) and PHENIX ( 67 ).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [R v4.1] -> structure determination [PHENIX, REFMAC] -> visualisation [PyMOL v2.5]

### Structural basis for severe pain caused by mutations in the S4-S5 linkers of voltage-gated sodium channel Na<sub>V</sub>1.7. (PNAS 2023)

- DOI: 10.1073/pnas.2219624120 | PMCID: PMC10083536 | PMID: 36996107
- Evidence: Structures were solved by molecular replacement with PHASER ( 48 ) using the previously determined Na V Ab structure PDB: 3RVY ( 14 ) or PDB: 6MW ( 30 ) as a search model and refined with REFMAC ( 49 ) in the CCP4 program suite ( 50 ).
- Full pipeline: structure determination [CCP4, PHENIX, REFMAC] -> stage not stated [Coot]

### A macrocyclic peptide inhibitor traps MRP1 in a catalytically incompetent conformation. (PNAS 2023)

- DOI: 10.1073/pnas.2220012120 | PMCID: PMC10089224 | PMID: 36893260
- Evidence: The merged coordinates were iteratively refined against the density-modified map using REFMAC incorporating secondary structure restraints generated with ProSMART, and manually manipulated to fit the density-modified map in Coot.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX, REFMAC, UCSF Chimera] -> stage not stated [PyMOL, RELION]

### Discovery of cyanophycin dipeptide hydrolase enzymes suggests widespread utility of the natural biopolymer cyanophycin. (PNAS 2023)

- DOI: 10.1073/pnas.2216547120 | PMCID: PMC9974463 | PMID: 36800389
- Evidence: The structures were refined in REFMAC ( 70 ), Rosetta ( 71 ), PHENIX ( 72 ), and Coot ( 73 ).
- Full pipeline: structure determination [PHENIX, REFMAC] -> visualisation [PyMOL]

### Arabidopsis Sec14 proteins (SFH5 and SFH7) mediate interorganelle transport of phosphatidic acid and regulate chloroplast development. (PNAS 2023)

- DOI: 10.1073/pnas.2221637120 | PMCID: PMC9963013 | PMID: 36716376
- Evidence: Standard refinement was performed with Coot, PHENIX, and REFMAC ( 44 – 46 ).
- Full pipeline: structure determination [PHENIX, REFMAC] -> stage not stated [PyMOL]

### Bioengineering a plant NLR immune receptor with a robust binding interface toward a conserved fungal pathogen effector. (PNAS 2024)

- DOI: 10.1073/pnas.2402872121 | PMCID: PMC11252911 | PMID: 38968126
- Evidence: To arrive at the final structure, a series of manual rebuilding, refinement, and validation steps were carried out using REFMAC ( 66 ) and COOT ( 67 ).
- Full pipeline: structure determination [REFMAC] -> visualisation [ChimeraX, R v4.0] -> stage not stated [ggplot2]

### Engineering a protease-stable, oral single-domain antibody to inhibit IL-23 signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2501635122 | PMCID: PMC12146698 | PMID: 40434646
- Evidence: The model was built in COOT ( 44 ) and subsequently refined with PHENIX ( 45 ) and REFMAC ( 46 ) to final statistics presented in SI Appendix , Table S2 .
- Full pipeline: differential/statistical testing [PHENIX, REFMAC] -> structure determination [PHENIX, REFMAC]

### Spider venom phospholipase D toxin structure: Interfacial binding site, mechanism, activation, and head group preference. (PNAS 2026)

- DOI: 10.1073/pnas.2513997123 | PMCID: PMC13079978 | PMID: 41941646
- Evidence: Model building was done with COOT and model refinement with REFMAC ( 63 ) as implemented in CCP4.
- Full pipeline: alignment/mapping [MAFFT] -> normalisation [CCP4] -> structure determination [REFMAC] -> visualisation [ChimeraX, MAFFT]

### Structural mechanism of LINE-1 target-primed reverse transcription. (Science 2025)

- DOI: 10.1126/science.ads8412 | PMCID: PMC7617806 | PMID: 40048554
- Evidence: The model for ddTTP was imported from the REFMAC monomer library in COOT.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, PHENIX v1.21.1, RELION] -> stage not stated [CTFFIND, ChimeraX, ImageJ, MotionCor2, PyMOL, Python, REFMAC, Topaz]

