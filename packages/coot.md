# Coot

- **Category:** structbio
- **Papers in survey:** 373
- **Journals:** PNAS (201), Nature (139), Cell (22), Science (11)
- **Years:** 2021 (30), 2022 (79), 2023 (72), 2024 (69), 2025 (91), 2026 (32)
- **Versions named:** 0.9.8.1 (10), 0.9 (7), 0.9.8 (6), 0.9.6 (6), 0.8.9.2 (5), 0.9.4.1 (5), 0.9.8.7 (5), 0.8.9 (3), 0.9.8.91 (3), 0.9.5 (3)
- **Pipeline stages it appears in:** structure determination (241), simulation/modelling (4), alignment/mapping (2), machine learning (2), normalisation (2), differential/statistical testing (1), read trimming (1), visualisation (1)

## Papers

### De novo identification of mammalian ciliary motility proteins using cryo-EM. (Cell 2021)

- DOI: 10.1016/j.cell.2021.10.007 | PMCID: PMC8595878 | PMID: 34715025
- Version used: **0.9**
- Evidence: Model building Model building was performed in Coot v0.9-pre or v0.9.4.1 ( Brown et al., 2015 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX, Coot v0.9, ImageJ v1.44d, RELION v3.1]

### In vitro and in vivo functions of SARS-CoV-2 infection-enhancing and neutralizing antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.021 | PMCID: PMC8232969 | PMID: 34242577
- Evidence: Mutations were made in Coot ( Emsley and Cowtan, 2004 ).
- Full pipeline: stage not stated [CTFFIND, ChimeraX, Coot, PHENIX, PyMOL, RELION, UCSF Chimera]

### Coupling of N7-methyltransferase and 3'-5' exoribonuclease with SARS-CoV-2 polymerase reveals mechanisms for capping and proofreading. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.033 | PMCID: PMC8142856 | PMID: 34143953
- Evidence: The model was manually built in Coot( Emsley et al., 2010 ) with the guidance of the cryo-EM map, and with real space refinement using Phenix( Afonine et al., 2018 ).
- Full pipeline: structure determination [Coot] -> stage not stated [MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Fab-dimerized glycan-reactive antibodies are a structural category of natural antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.042 | PMCID: PMC8135257 | PMID: 34019795
- Evidence: The solution was improved through alternating rounds of manual rebuilding in Coot and reciprocal space refinement in PHENIX, and geometry optimization using Rosetta-Phenix refinement (phenix.rosetta_refine) ( Emsley et al., 2010 ; Adams et al., 2010 ).
- Full pipeline: alignment/mapping [MotionCor2] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX, R, Seurat, UMAP] -> stage not stated [PyMOL, RELION, UCSF Chimera, ggplot2]

### Evidence of escape of SARS-CoV-2 variant B.1.351 from natural and vaccine-induced sera. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.037 | PMCID: PMC7901269 | PMID: 33730597
- Evidence: Structure plots use spike protein structure (original frame from PDB: 6ZWV ) where modeled, and models were extended in Coot for missing loops.
- Full pipeline: stage not stated [Coot, PyMOL]

### Cryo-EM Structure of an Extended SARS-CoV-2 Replication and Transcription Complex Reveals an Intermediate State in Cap Synthesis. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.016 | PMCID: PMC7666536 | PMID: 33232691
- Evidence: The model was manually built in Coot ( Emsley et al., 2010 ) with the guidance of the cryo-EM map, and in combination with real space refinement using Phenix ( Afonine et al., 2018 ).
- Full pipeline: structure determination [Coot] -> stage not stated [ImageJ, MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Structural basis for the assembly of the type V CRISPR-associated transposon complex. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.009 | PMCID: PMC9798831 | PMID: 36435179
- Evidence: 51 The structural models were built in Coot.
- Full pipeline: stage not stated [CTFFIND v1.06, ChimeraX v1.2, Coot, MotionCor2 v1.4.0, PHENIX v1.19.1, RELION v3.1.2, UCSF Chimera v1.14]

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Evidence: Manual model building was performed in Coot ( Emsley and Cowtan, 2004 ), and models were all atom refined using REFMAC ( Murshudov et al., 2011 ) and Phenix ( Liebschner et al., 2019 ).
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### BacPROTACs mediate targeted protein degradation in bacteria. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.009 | PMCID: PMC9240326 | PMID: 35662409
- Evidence: Model building An initial model was built in Coot ( Emsley et al., 2010 ) by rigid body fitting of secondary structure elements of one of the previously reported ClpC structures into the EM-map (PDB: 3J3U) ( Liu et al., 2013 ).
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX, Coot, MotionCor2 v1.0.5, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Cryo-ET of Env on intact HIV virions reveals structural variation and positioning on the Gag lattice. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.013 | PMCID: PMC9000915 | PMID: 35123651
- Evidence: The unstructured loop region at the end of gp41, comprising of amino acid residues 654-664, was fitted into the clearly delineated stalk density using ‘Flexible fitting’ feature in Coot software ( Emsley et al., 2010 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ChimeraX, Coot, EMAN2, IMOD v4.10.15, ImageJ, RELION v2.1, UCSF Chimera]

### Structural and functional characterizations of infectivity and immune evasion of SARS-CoV-2 Omicron. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.019 | PMCID: PMC8786603 | PMID: 35120603
- Evidence: Then the structure was manually adjusted and corrected according to the protein sequences and cryo-EM densities in Coot, and finally, real-space refinement was performed by Phenix.
- Full pipeline: structure determination [Coot] -> stage not stated [CTFFIND, ChimeraX, MotionCor2, PHENIX, RELION v3.07, UCSF Chimera, igraph v1.2.5]

### Comprehensive structure and functional adaptations of the yeast nuclear pore complex. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.015 | PMCID: PMC8928745 | PMID: 34982960
- Evidence: A visual inspection with docked models in Coot did not reveal anomalous features at subunit boundaries in the reassembled 3D maps at the current resolution.
- Full pipeline: registration [IMOD] -> simulation/modelling [PHENIX] -> structure determination [PHENIX] -> stage not stated [Coot, EMAN2, ImageJ, RELION v2.0]

### Structural evolution of fibril polymorphs during amyloid assembly. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.025 | PMCID: PMC7617692 | PMID: 38134875
- Evidence: IAPP-S20G model building For each of the nine deposited cryoEM maps, a corresponding protein model was constructed or docked, iteratively edited in Coot 69 and real-space refined in Phenix 70 before repeating the model to cover three fibril layers and performing a final real-space refinement in Phenix with NCS restraints.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND v4.16, ChimeraX, Conda, PyMOL]

### De novo protein identification in mammalian sperm using in situ cryoelectron tomography and AlphaFold2 docking. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.017 | PMCID: PMC10842264 | PMID: 37865089
- Version used: **0.9.8.1**
- Evidence: Model building was performed in Coot v0.9.8.1 55 and rigid body fitting was achieved using UCSF Chimera.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler v4.4.1] -> differential/statistical testing [Bioconductor] -> visualisation [IMOD] -> stage not stated [AlphaFold, ChimeraX, ColabFold, Coot v0.9.8.1, MotionCor2, R, RELION, UCSF Chimera]

### Structural basis for ion selectivity in potassium-selective channelrhodopsins. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.009 | PMCID: PMC7615185 | PMID: 37652010
- Evidence: 99 This starting model was then subjected to iterative rounds of manual and automated refinement in Coot 89 and Refmac5 100 in Servalcat pipeline, 90 respectively.
- Full pipeline: structure determination [AlphaFold, Coot, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Kilosort v2.5, MotionCor2, RELION v4.0, UCSF Chimera]

### TMEM106B is a receptor mediating ACE2-independent SARS-CoV-2 cell entry. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.005 | PMCID: PMC10409496 | PMID: 37421949
- Evidence: The structure was refined interactively in real-space in Coot, 85 and in reciprocal and real space using phenix.refine.
- Full pipeline: quantification [ImageJ] -> structure determination [Coot] -> machine learning [Topaz] -> stage not stated [AlphaFold, CTFFIND v1.06, PHENIX, RELION v4.0, UCSF Chimera]

### Molecular mechanisms of stress-induced reactivation in mumps virus condensates. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.015 | PMCID: PMC10156176 | PMID: 37116470
- Evidence: After that, the tetramer model was per-residue manually refined in Coot 87 (v0.9) using Peptide and Ramachandran restraints, with attention on the first monomer and molecular interfaces.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [Bioconductor] -> structure determination [Coot, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, BWA v0.7.17, ChimeraX v1.1.1, IMOD, PHENIX v1.18, Picard, R v3.6, RELION v3.0, freebayes v1.1.0, limma]

### A potent pan-sarbecovirus neutralizing antibody resilient to epitope diversification. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.026 | PMCID: PMC11645210 | PMID: 39383863
- Evidence: Model building and refinement RBD and VIR-7229 Fab complex models were built and refined by iterating between manual rebuilding in Coot 99 and refinement in Rosetta 100 , 101 .
- Full pipeline: read trimming [BCFtools v1.10.2, BWA v0.7.17] -> differential/statistical testing [RELION, scikit-learn] -> structure determination [Coot, PHENIX, Topaz] -> machine learning [Topaz, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [OpenMM, Pangolin, Python v3.10]

### Extensive structural rearrangement of intraflagellar transport trains underpins bidirectional cargo transport. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.041 | PMCID: PMC11349379 | PMID: 39067443
- Evidence: For initial model docking we used Chimerax, and then performed manual modifications in Coot V0.9.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2, RELION]

### Rapid DNA unwinding accelerates genome editing by engineered CRISPR-Cas9. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.031 | PMCID: PMC11658890 | PMID: 38781968
- Version used: **0.9.8.7**
- Evidence: Wildtype GeoCas9 model went through several rounds of real space refinement in Phenix version 1.19.2–4158 and manual geometry improvement in Coot version 0.9.8.7 resulting in a final model.
- Full pipeline: structure determination [Coot v0.9.8.7] -> stage not stated [AlphaFold, ChimeraX v1.6.1, ColabFold, PHENIX v1.19.2, Python, Topaz, fastp]

### Molecular basis for shifted receptor recognition by an encephalitic arbovirus. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.029 | PMCID: PMC12406711 | PMID: 40187345
- Version used: **0.9.8.91**
- Evidence: 66 The atomic model was then generated through iterative rounds of model building and adjustment in Coot (version 0.9.8.91) 67 and refined using real space refinement in Phenix (version 1.21rc1–5127).
- Full pipeline: structure determination [ChimeraX, Coot v0.9.8.91, PHENIX v1.21r, UCSF Chimera v1.6.1] -> stage not stated [AlphaFold, CTFFIND, MotionCor2 v1.6.4, PyMOL v3.0.2, RELION v3.1]

### Structural and functional analysis of the Nipah virus polymerase complex. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.021 | PMCID: PMC11813165 | PMID: 39837328
- Version used: **0.9**
- Evidence: Extra residues of P were built manually in Coot version 0.9.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.5, Clustal Omega, Coot v0.9, MotionCor2 v1.6.4, PHENIX v1.20.1, PyMOL v2.5.5, RELION v3.1.1, UCSF Chimera v1.15]

### The structure of neurofibromin isoform 2 reveals different functional states. (Nature 2021)

- DOI: 10.1038/s41586-021-04024-x | PMCID: PMC8580823 | PMID: 34707296
- Evidence: 17 ) and the 2e2x Sec14-PH domain 20 were rigid body fitted using Chimera 40 , 41 into the best GRD-Sec14-PH map and manually corrected and completed by real-space refinement in Coot.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX v1.19, UCSF Chimera v1.15] -> stage not stated [ChimeraX, MotionCor2 v2.1.1, RELION v3.1.1]

### Structural basis of human transcription-DNA repair coupling. (Nature 2021)

- DOI: 10.1038/s41586-021-03906-4 | PMCID: PMC8514338 | PMID: 34526721
- Evidence: The model was fitted into the CSB focused refined map in Chimera 54 and rebuilt in Coot 57 , followed by real-space refinement in PHENIX 58 .
- Full pipeline: quantification [ImageJ] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, ImageJ] -> stage not stated [RELION v3.0, UCSF Chimera]

### Structural insights into how Prp5 proofreads the pre-mRNA branch site. (Nature 2021)

- DOI: 10.1038/s41586-021-03789-5 | PMCID: PMC8357632 | PMID: 34349264
- Version used: **0.8.9.2**
- Evidence: In the central part of the U1 snRNP (resolution ranging from 3.7 Å to 4.3 Å), side chains were manually adjusted into the map using Coot v.0.8.9.2 (ref.
- Full pipeline: structure determination [PHENIX v1.13] -> stage not stated [CTFFIND, ChimeraX v1.1, Coot v0.8.9.2, RELION v3.0, UCSF Chimera v1.13.1]

### The structural basis of odorant recognition in insect olfactory receptors. (Nature 2021)

- DOI: 10.1038/s41586-021-03794-8 | PMCID: PMC8410599 | PMID: 34349260
- Evidence: Model building The Cryo-EM structure of Orco (Protein Data Bank (PDB) accession 6C70) was used as a template for homology modelling of Mh OR5 using Modeller 45 , followed by manual building in Coot 46 .
- Full pipeline: alignment/mapping [MAFFT, MotionCor2, RELION v3.0] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [scikit-learn] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, PyMOL]

### Structural basis of early translocation events on the ribosome. (Nature 2021)

- DOI: 10.1038/s41586-021-03713-x | PMCID: PMC8318882 | PMID: 34234344
- Version used: **0.9.4.1**
- Evidence: ...and ribosomal protein L7/L12 (starting model PDB ID: 1CTF 63 ) were fitted into EM maps and refined through iterative rounds of manual model building in Coot (v.0.9.4.1) 64 , refinement of RNA with ERRASER 65 and real-space refinement using Phenix (v.1.19-4092) 66 . mRNA nucleotide 40 corresponds to the +1 position.
- Full pipeline: normalisation [UCSF Chimera] -> registration [MotionCor2] -> differential/statistical testing [UCSF Chimera] -> structure determination [Coot v0.9.4.1, PHENIX v1.19, RELION, UCSF Chimera] -> visualisation [ChimeraX]

### Structural basis of GABA<sub>B</sub> receptor-G<sub>i</sub> protein coupling. (Nature 2021)

- DOI: 10.1038/s41586-021-03507-1 | PMCID: PMC8222003 | PMID: 33911284
- Evidence: The docked model was subjected to flexible fitting using Rosetta 45 and was further rebuilt in Coot 45 and real-space-refined in Rosetta 45 and Phenix 44 .
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, RELION v3.1]

### Structure and inhibition mechanism of the human citrate transporter NaCT. (Nature 2021)

- DOI: 10.1038/s41586-021-03230-x | PMCID: PMC7933130 | PMID: 33597751
- Evidence: Model building and refinement All maps were sharpened using Auto-sharpen Map in Phenix 66 , built in Coot 67 , and refined in Phenix real space refine 66 .
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [MotionCor2, Topaz]

### Close relatives of MERS-CoV in bats use ACE2 as their functional receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-05513-3 | PMCID: PMC9734910 | PMID: 36477529
- Version used: **0.9.4**
- Evidence: Model building and refinement The NeoCoV RBD–Bat37ACE2 complex structures were manually built into the refined maps using Coot (v.0.9.4) 68 .
- Full pipeline: alignment/mapping [CTFFIND, Clustal Omega, MUSCLE] -> structure determination [Coot v0.9.4, PHENIX v1.19, RELION, UCSF Chimera v1.15] -> stage not stated [ChimeraX v1.1, MotionCor2 v1.3.0]

### Structural basis of tankyrase activation by polymerization. (Nature 2022)

- DOI: 10.1038/s41586-022-05449-8 | PMCID: PMC9712121 | PMID: 36418402
- Evidence: An initial model of a single TNKS2 SAM–PARP G1032W protomer was built in Coot 48 after fitting the TNKS2 PARP domain (PDB code 5NWG, chain IB) 33 and SAM domain (PDB code 5JRT) 4 into the central region of the sharpened cryo-EM map where resolution was highest, using UCSF Chimera (v1.14) 49 .
- Full pipeline: alignment/mapping [Clustal Omega, EMAN2 v2.31] -> quantification [ImageJ] -> normalisation [ImageJ] -> structure determination [PHENIX v1.18.2] -> visualisation [ChimeraX v1.3] -> stage not stated [CellProfiler, Coot, MotionCor2, RELION v2.10, UCSF Chimera v1.14]

### Structural basis of actin filament assembly and aging. (Nature 2022)

- DOI: 10.1038/s41586-022-05241-8 | PMCID: PMC9646518 | PMID: 36289337
- Evidence: The central actin subunit in the map was rebuilt manually in Coot 62 and the other actin subunits were adjusted in Coot by applying non-crystallographic symmetry using the central subunit as master chain.
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX] -> stage not stated [Coot, RELION]

### Cryo-EM structure of the SEA complex. (Nature 2022)

- DOI: 10.1038/s41586-022-05370-0 | PMCID: PMC9646525 | PMID: 36289347
- Version used: **0.9.8.1**
- Evidence: Model building was performed in Coot v.0.9.8.1 (ref.
- Full pipeline: quantification [ImageJ v1.52p] -> structure determination [PHENIX v1.20.1] -> visualisation [ChimeraX v1.3] -> stage not stated [AlphaFold, Coot v0.9.8.1, RELION v4.0, UCSF Chimera v1.15]

### Bending forces and nucleotide state jointly regulate F-actin structure. (Nature 2022)

- DOI: 10.1038/s41586-022-05366-w | PMCID: PMC9646526 | PMID: 36289330
- Evidence: The maps and models were then manually inspected in Coot, and water molecules were added or pruned.
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [Python] -> differential/statistical testing [Matplotlib] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX, RELION] -> machine learning [TensorFlow, cryoDRGN] -> stage not stated [Coot, EMAN2, UCSF Chimera, scikit-image]

### Clathrin-associated AP-1 controls termination of STING signalling. (Nature 2022)

- DOI: 10.1038/s41586-022-05354-0 | PMCID: PMC9605868 | PMID: 36261523
- Evidence: The pSTING tail was docked against the cryo-EM map in Coot and the whole model was refined in PHENIX.
- Full pipeline: quantification [Harmony v4.9] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera]

### Visualizing translation dynamics at atomic detail inside a bacterial cell. (Nature 2022)

- DOI: 10.1038/s41586-022-05255-2 | PMCID: PMC9534751 | PMID: 36171285
- Evidence: Homology models were rigid-body-fitted into the cryo-ET densities using Chimera 63 , followed by iterative refinement using PHENIX real-space refinement 64 and manual adjustment in Coot 65 .
- Full pipeline: alignment/mapping [MAFFT, eggNOG] -> dimensionality reduction/clustering [eggNOG] -> structure determination [Coot, PHENIX, Python v3.7.7] -> visualisation [ChimeraX] -> stage not stated [RELION v3.0]

### Structures of α-synuclein filaments from human brains with Lewy pathology. (Nature 2022)

- DOI: 10.1038/s41586-022-05319-3 | PMCID: PMC7613749 | PMID: 36108674
- Evidence: Model building Atomic models comprising three β-sheet rungs were built de novo in Coot ( 65 ) in the best available map for PDD case 1.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [CTFFIND, Coot]

### Discovery, structure and mechanism of a tetraether lipid synthase. (Nature 2022)

- DOI: 10.1038/s41586-022-05120-2 | PMCID: PMC9433317 | PMID: 35882349
- Evidence: The resulting model was then manually adjusted in Coot and refined in Phenix 49 , 53 .
- Full pipeline: structure determination [Coot] -> visualisation [Cytoscape, PyMOL] -> stage not stated [AlphaFold, PHENIX]

### Akkermansia muciniphila phospholipid induces homeostatic immune responses. (Nature 2022)

- DOI: 10.1038/s41586-022-04985-7 | PMCID: PMC9328018 | PMID: 35896748
- Version used: **0.9**
- Evidence: The Pam3CSK4 ligand was removed from the crystal structure coordinates, and an a15:0-i15:0 PE ligand was prepared using Lidia and AceDRG in Coot v.0.9 (refs.
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.8] -> alignment/mapping [BLAST, kallisto v0.46.1] -> differential/statistical testing [edgeR v3.35.1] -> stage not stated [ChimeraX v1.0, Coot v0.9, FSL]

### Organizing structural principles of the IL-17 ligand-receptor axis. (Nature 2022)

- DOI: 10.1038/s41586-022-05116-y | PMCID: PMC9477748 | PMID: 35863378
- Evidence: Models were then refined using rigid-body refinement with Phenix 48 followed by refinement with ISOLDE 49 , and further iterative manual building and refinement in Coot 50 and Phenix.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX, UCSF Chimera] -> stage not stated [PyMOL]

### Archaic chaperone-usher pili self-secrete into superelastic zigzag springs. (Nature 2022)

- DOI: 10.1038/s41586-022-05095-0 | PMCID: PMC9452303 | PMID: 35853476
- Version used: **0.9.4**
- Evidence: The short linker connecting the donor strand with strand A was modelled using Coot (v.0.9.4) 37 .
- Full pipeline: quantification [ImageJ v1.53k] -> registration [MotionCor2 v1.2.3] -> structure determination [MotionCor2 v1.2.3, PHENIX v1.8.2, RELION v3.0.8, UCSF Chimera] -> stage not stated [CTFFIND v4.1.13, Coot v0.9.4]

### Cryo-EM structure of an active bacterial TIR-STING filament complex. (Nature 2022)

- DOI: 10.1038/s41586-022-04999-1 | PMCID: PMC9402430 | PMID: 35859168
- Evidence: The Fs STING (PDB 6WT5) CBD was used as a starting model docked into the single-fibre c-di-GMP-bound Sf STING density in Coot followed by iterative manual model building 31 .
- Full pipeline: registration [MotionCor2 v1.4.0] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, RELION]

### A peroxisomal ubiquitin ligase complex forms a retrotranslocation channel. (Nature 2022)

- DOI: 10.1038/s41586-022-04903-x | PMCID: PMC9279156 | PMID: 35768507
- Evidence: Structural model building, refinement and analysis All models were built in Coot 50 and refined in PHENIX 51 using the 3.1 Å sharpened density map.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, REFMAC, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.1]

### Structures and mechanism of the plant PIN-FORMED auxin transporter. (Nature 2022)

- DOI: 10.1038/s41586-022-04883-y | PMCID: PMC9477730 | PMID: 35768502
- Evidence: The flexible cytoplasmic loop of PIN8 (residues 165 to 205) is not visible in the maps and was excluded from model building in Coot 42 .
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [PHENIX, RoseTTAFold] -> visualisation [PyMOL] -> stage not stated [Coot]

### Cryo-EM structure of a type IV secretion system. (Nature 2022)

- DOI: 10.1038/s41586-022-04859-y | PMCID: PMC9259494 | PMID: 35732732
- Evidence: The monomer model was improved further using iterative rounds of RosettaCM and manual readjustment in Coot against the map and refined using real space refinement with simulated annealing and secondary structure restraints in Phenix v1.18.
- Full pipeline: registration [CTFFIND v4.1] -> simulation/modelling [Coot] -> structure determination [Coot, PHENIX v1.18.2, RELION v3.1] -> machine learning [AlphaFold] -> stage not stated [ChimeraX v1.1, HMMER, PyMOL v2.3.2]

### Mechanism of replication origin melting nucleated by CMG helicase assembly. (Nature 2022)

- DOI: 10.1038/s41586-022-04829-4 | PMCID: PMC9242855 | PMID: 35705812
- Version used: **0.9.1**
- Evidence: Model building and refinement CMG (from PDB 6SKL ) 31 , Pol2 subunit (from PDB 6HV9 ) 33 and a homology model of the N-terminal domain of Dpb2 obtained from the Phyre2 server 61 were docked initially into the cryo-EM map produced from Resolve CryoEM, using USCF Chimera, and refined against the map using Namdinator 62 as a starting point for modelling with Coot v.0.9.1 (ref.
- Full pipeline: structure determination [Coot v0.9.1] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [CTFFIND, PHENIX, RELION]

### Structural basis of sodium-dependent bile salt uptake into the liver. (Nature 2022)

- DOI: 10.1038/s41586-022-04723-z | PMCID: PMC9242856 | PMID: 35545671
- Evidence: Initial Nb models were created with I-TASSER 66 , and then fit as rigid bodies into the density, followed by manual building and modification in Coot 63 , 64 .
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [Coot]

### USP14-regulated allostery of the human proteasome by time-resolved cryo-EM. (Nature 2022)

- DOI: 10.1038/s41586-022-04671-8 | PMCID: PMC9117149 | PMID: 35477760
- Evidence: The USP14 model was then merged with the initial proteasome model by independently fitting models of the USP14 UBL and USP domains as rigid bodies into the cryo-EM maps, and manually fitting the linker between the UBL and USP domains in Coot 56 .
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, Coot, EMAN2, MotionCor2, RELION]

### Opening of glutamate receptor channel to subconductance levels. (Nature 2022)

- DOI: 10.1038/s41586-022-04637-w | PMCID: PMC9068512 | PMID: 35444281
- Version used: **0.9.2**
- Evidence: Model building and refinement The models of LBD–TMD in seven unique conformations were built in Coot 0.9.2 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot v0.9.2] -> stage not stated [CTFFIND v1.06, PHENIX v1.18, RELION v3.1, UCSF Chimera v1.14, VMD v1.9.3]

### Structural basis of tethered agonism of the adhesion GPCRs ADGRD1 and ADGRF1. (Nature 2022)

- DOI: 10.1038/s41586-022-04580-w | PMCID: PMC9046087 | PMID: 35418679
- Evidence: Each model was docked into the corresponding cryo-EM density map by ChimeraX v.1.1 45 , followed by iterative manual adjustment in Coot 46 and real-space refinement in phenix.real_space_refine of PHENIX 47 .
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, ChimeraX v1.1, Coot, PHENIX] -> visualisation [PyMOL v1.8, UCSF Chimera v1.15] -> stage not stated [CTFFIND v1.18, RELION v3.1]

### Age-dependent formation of TMEM106B amyloid filaments in human brains. (Nature 2022)

- DOI: 10.1038/s41586-022-04650-z | PMCID: PMC9095482 | PMID: 35344985
- Evidence: Atomic models comprising three β-sheet rungs were built de novo in Coot 39 in the best available map for each of the five different structures.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [AlphaFold, CTFFIND, Coot]

### Design of protein-binding proteins from the target structure alone. (Nature 2022)

- DOI: 10.1038/s41586-022-04654-9 | PMCID: PMC9117152 | PMID: 35332283
- Evidence: Initial rebuilding was completed with phenix.autobuild 63 followed by iterative rounds of manual rebuilding in Coot 64 and refinement in Phenix 65 – 67 .
- Full pipeline: quantification [ImageJ] -> normalisation [CCP4] -> structure determination [Coot, PHENIX] -> stage not stated [PyMOL]

### Tryptophan depletion results in tryptophan-to-phenylalanine substitutants. (Nature 2022)

- DOI: 10.1038/s41586-022-04499-2 | PMCID: PMC8942854 | PMID: 35264796
- Evidence: All created homology models were visually inspected in Coot to assess whether the tryptophan residues made structurally important hydrogen bonds through their side-chains that are lost by W>F substitutions.
- Full pipeline: stage not stated [Coot, GSEA]

### Visualizing protein breathing motions associated with aromatic ring flipping. (Nature 2022)

- DOI: 10.1038/s41586-022-04417-6 | PMCID: PMC8866124 | PMID: 35173330
- Evidence: The initial solutions were improved through cycles of manual adjusting in Coot 65 and refined by using Refmac5 66 .
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, VMD]

### Mechanisms of inhibition and activation of extrasynaptic αβ GABA<sub>A</sub> receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-04402-z | PMCID: PMC8850191 | PMID: 35140402
- Evidence: Model building, refinement, validation, analysis and presentation Model building was carried out in Coot 58 using PDB 6HUO as a template for the GABA A R α1β3 GABA map.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [UCSF Chimera]

### Memory B cell repertoire from triple vaccinees against diverse SARS-CoV-2 variants. (Nature 2022)

- DOI: 10.1038/s41586-022-04466-x | PMCID: PMC8967717 | PMID: 35090164
- Evidence: ...the final S-Fab-complexes described above by Chimera, followed by manually adjustment and correction according to the protein sequences and densities in Coot, as well as real space refinement using Phenix.
- Full pipeline: registration [RELION v3.0] -> simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND]

### Activation mechanism of PINK1. (Nature 2022)

- DOI: 10.1038/s41586-021-04340-2 | PMCID: PMC8828467 | PMID: 34933320
- Version used: **0.9**
- Evidence: Model building was performed in Coot (v.0.9) 50 and underwent multiple rounds of refinement in Phenix.
- Full pipeline: structure determination [Coot v0.9] -> visualisation [ChimeraX v1.1.1] -> stage not stated [AlphaFold, ColabFold, EMAN2, Fiji v1.53k, ImageJ v1.53k, PHENIX v1.19.2, RELION v3.1, UCSF Chimera]

### Intermediate conformations of CD4-bound HIV-1 Env heterotrimers. (Nature 2023)

- DOI: 10.1038/s41586-023-06639-8 | PMCID: PMC10686819 | PMID: 37993719
- Version used: **0.8.9.1**
- Evidence: Initial BG505 HT–CD4 models and N -linked glycans were manually refined using Coot v.0.8.9.1 (ref.
- Full pipeline: structure determination [ChimeraX v1.2.5, Coot v0.8.9.1, PHENIX v1.17.1] -> visualisation [PyMOL v2.4.0]

### Structure and electromechanical coupling of a voltage-gated Na&lt;sup&gt;+&lt;/sup&gt;/H&lt;sup&gt;+&lt;/sup&gt; exchanger. (Nature 2023)

- DOI: 10.1038/s41586-023-06518-2 | PMCID: PMC10620092 | PMID: 37880360
- Evidence: Model building and refinement of SLC9C1 in GDN, nanodiscs and GDN with cAMP The SLC9C1 homology model was taken from AlphaFold 55 and each domain was extensively refitted into the C 2 GDN map using the fit in map utility of Chimera 56 and rebuilt extensively in Coot 57 .
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX] -> stage not stated [PyMOL]

### Inactivation of the Kv2.1 channel through electromechanical coupling. (Nature 2023)

- DOI: 10.1038/s41586-023-06582-8 | PMCID: PMC10567553 | PMID: 37758949
- Version used: **0.9.8.1**
- Evidence: The model was then manually built in Coot (v.0.9.8.1) 70 and refined using real space refinement in PHENIX (v.1.19.1) 71 with secondary structure and geometry restraints.
- Full pipeline: structure determination [Coot v0.9.8.1, PHENIX v1.19.1, UCSF Chimera v1.15] -> visualisation [PyMOL v2.4.1] -> stage not stated [MDAnalysis, MotionCor2, RELION v3.0]

### Cryo-EM structures reveal native GABA&lt;sub&gt;A&lt;/sub&gt; receptor assemblies and pharmacology. (Nature 2023)

- DOI: 10.1038/s41586-023-06556-w | PMCID: PMC10550821 | PMID: 37730991
- Evidence: The full complex was then edited to remove unresolved portions and refined extensively to achieve better model–map agreement in Coot 67 .
- Full pipeline: structure determination [Coot] -> stage not stated [AlphaFold, CCP4, ChimeraX, Python, RELION]

### Structural mobility tunes signalling of the GluA1 AMPA glutamate receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06528-0 | PMCID: PMC10533411 | PMID: 37704721
- Evidence: Afterwards, manual refinement was performed in Coot to further refine the geometry.
- Full pipeline: structure determination [Coot, PHENIX, Python, RELION] -> stage not stated [AlphaFold, ChimeraX, MotionCor2, PyMOL, UCSF Chimera]

### Tail engagement of arrestin at the glucagon receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06420-x | PMCID: PMC10447241 | PMID: 37558880
- Version used: **0.8.9**
- Evidence: The models were manually adjusted in Coot 0.8.9 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [Coot v0.8.9]

### Cooperation between bHLH transcription factors and histones for DNA access. (Nature 2023)

- DOI: 10.1038/s41586-023-06282-3 | PMCID: PMC10338342 | PMID: 37407816
- Version used: **0.9.6**
- Evidence: The gap between NCP DNA and MYC-MAX DNA was closed using ideal B-form DNA in Coot (v.0.9.6) 91 and the DNA sequence was adapted accordingly.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bioconductor, Bowtie2, ChimeraX, PyMOL] -> structure determination [PHENIX] -> stage not stated [Coot v0.9.6, ImageJ, RELION, SAMtools v1.6]

### Genome expansion by a CRISPR trimmer-integrase. (Nature 2023)

- DOI: 10.1038/s41586-023-06178-2 | PMCID: PMC10284694 | PMID: 37316664
- Version used: **0.9.4.1**
- Evidence: The complex model was refined using rounds of real-space refinement and rigid body fit tools in Coot (v.0.9.4.1) 49 , and real_space_refine tool in Phenix (v.1.19.2-4158) 50 , using secondary structure, Ramachandran, and rotamer restraints.
- Full pipeline: structure determination [AlphaFold, Coot v0.9.4.1, PHENIX v1.19.2] -> machine learning [Topaz] -> stage not stated [ChimeraX, HMMER]

### Structural basis for FGF hormone signalling. (Nature 2023)

- DOI: 10.1038/s41586-023-06155-9 | PMCID: PMC10284700 | PMID: 37286607
- Evidence: Initial models were then adjusted in Coot 45 and real-space refined in Phenix 46 .
- Full pipeline: differential/statistical testing [ImageJ] -> simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX]

### Axonemal structures reveal mechanoregulatory and disease mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-06140-2 | PMCID: PMC10266980 | PMID: 37258679
- Evidence: For both structures, fit-to-map was optimized using real-space refinement implemented in Coot, Namdinator 78 and Phenix 79 .
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> structure determination [Coot] -> stage not stated [AlphaFold, ChimeraX, PHENIX, R v4.0, RELION]

### Enhanced rare-earth separation with a metal-sensitive lanmodulin dimer. (Nature 2023)

- DOI: 10.1038/s41586-023-05945-5 | PMCID: PMC10232371 | PMID: 37259003
- Evidence: Initial models were generated with phenix.autobuild 59 with subsequent rounds of manual modification and refinement in Coot 60 and phenix.refine 61 .
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> structure determination [Coot] -> visualisation [Cytoscape v3.9.1, PyMOL, R v4.1.0] -> stage not stated [IQ-TREE v2.2.0.3]

### Histone modifications regulate pioneer transcription factor cooperativity. (Nature 2023)

- DOI: 10.1038/s41586-023-06112-6 | PMCID: PMC10338341 | PMID: 37225990
- Evidence: The model of the OCT4 bound to DNA (PDB: 3L1P ) 19 were rigid-body placed using PHENIX, manually adjusted and rebuilt in Coot and refined in Phenix.
- Full pipeline: structure determination [Coot] -> stage not stated [ImageJ, PHENIX, RELION]

### Structural basis of catalytic activation in human splicing. (Nature 2023)

- DOI: 10.1038/s41586-023-06049-w | PMCID: PMC10208982 | PMID: 37165190
- Evidence: Thus, the model building of the B AQR complex was initiated by the docking of the human B act models into the consensus maps (maps 2, 3 and 4) of the complex, followed by manual, residue-by-residue model adjustment in Coot 54 and refinement with phenix.real_space_refine 55 .
- Full pipeline: simulation/modelling [ChimeraX v1.3] -> structure determination [Coot] -> stage not stated [PyMOL, RELION v3.1]

### Ligand and G-protein selectivity in the κ-opioid receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06030-7 | PMCID: PMC10172140 | PMID: 37138078
- Evidence: The complex models (KOR–G-protein–scFv16) were manually built in Coot 65 , followed by several rounds of real-space refinement using Phenix 66 .
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL]

### Structural atlas of a human gut crassvirus. (Nature 2023)

- DOI: 10.1038/s41586-023-06019-2 | PMCID: PMC10172136 | PMID: 37138077
- Version used: **0.9.8.1**
- Evidence: 6 ) were generated by manual building in Coot (0.9.8.1) 46 , followed by real space refinement in Phenix (1.19) 47 .
- Full pipeline: structure determination [Coot v0.9.8.1, PHENIX v1.19] -> stage not stated [AlphaFold, ChimeraX v1.5, RELION v3.1]

### De novo design of protein interactions with learned surface fingerprints. (Nature 2023)

- DOI: 10.1038/s41586-023-05993-x | PMCID: PMC10131520 | PMID: 37100904
- Version used: **0.9.5**
- Evidence: COOT (v.0.9.5) and PHENIX (v.1.20.1-4487) were used for subsequent model building and refinement 73 , 74 .
- Full pipeline: alignment/mapping [AlphaFold] -> normalisation [scikit-learn] -> dimensionality reduction/clustering [scikit-learn] -> structure determination [Coot v0.9.5] -> machine learning [TensorFlow v1.12] -> visualisation [ChimeraX] -> stage not stated [PHENIX v1.20.1, UCSF Chimera]

### mRNA decoding in human is kinetically and structurally distinct from bacteria. (Nature 2023)

- DOI: 10.1038/s41586-023-05908-w | PMCID: PMC10156603 | PMID: 37020024
- Evidence: The model was visually inspected together with the 3D volume and further improved by iterative model building in Coot 77 .
- Full pipeline: registration [MotionCor2] -> structure determination [CCP4] -> machine learning [REFMAC] -> stage not stated [ChimeraX, Coot, RELION v3.1, UCSF Chimera]

### Structural basis for GSDMB pore formation and its targeting by IpaH7.8. (Nature 2023)

- DOI: 10.1038/s41586-023-05832-z | PMCID: PMC10115629 | PMID: 36991122
- Evidence: Models of IpaH7.8 and GSDMB were docked into EM density as a rigid body in UCSF Chimera 48 then manually adjusted in Coot.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, Coot, MotionCor2, RELION, UCSF Chimera]

### Structural basis of mitochondrial membrane bending by the I-II-III&lt;sub&gt;2&lt;/sub&gt;-IV&lt;sub&gt;2&lt;/sub&gt; supercomplex. (Nature 2023)

- DOI: 10.1038/s41586-023-05817-y | PMCID: PMC10060162 | PMID: 36949187
- Evidence: Model building and refinement Manual model building was performed in Coot 44 and new subunits identified directly for the cryo-EM map.
- Full pipeline: registration [IMOD, RELION] -> simulation/modelling [ChimeraX, GROMACS] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### From primordial clocks to circadian oscillators. (Nature 2023)

- DOI: 10.1038/s41586-023-05836-9 | PMCID: PMC10076222 | PMID: 36949197
- Version used: **0.9.81**
- Evidence: 36 )) was manually rebuilt in Coot (v.0.9.81) 54 and refined in Phenix (v.1.20.1-4487) 55 .
- Full pipeline: alignment/mapping [IQ-TREE v1.6, MAFFT, RAxML v8.2.9] -> simulation/modelling [UCSF Chimera v1.15] -> structure determination [Coot v0.9.81, PHENIX v1.20.1] -> visualisation [PyMOL v2.6.0]

### Structural basis for bacterial energy extraction from atmospheric hydrogen. (Nature 2023)

- DOI: 10.1038/s41586-023-05781-7 | PMCID: PMC10017518 | PMID: 36890228
- Evidence: Images and movies were generated in Coot, ChimeraX, and Pymol 56 , 58 .
- Full pipeline: simulation/modelling [GROMACS v2021.3] -> structure determination [ChimeraX v1.3, PHENIX] -> visualisation [AlphaFold, VMD] -> stage not stated [CTFFIND v4.1.8, Coot, RELION v3.1.2]

### The structural basis for HIV-1 Vif antagonism of human APOBEC3G. (Nature 2023)

- DOI: 10.1038/s41586-023-05779-1 | PMCID: PMC10033410 | PMID: 36754086
- Evidence: This starting model was manually rebuilt in Coot 78 , 79 and adjusted in ISOLDE 80 to improve local fitting.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> registration [MotionCor2] -> structure determination [AlphaFold, UCSF Chimera] -> stage not stated [ChimeraX, Coot, PHENIX, PyMOL, RELION]

### Structural basis for substrate selection by the SARS-CoV-2 replicase. (Nature 2023)

- DOI: 10.1038/s41586-022-05664-3 | PMCID: PMC9891196 | PMID: 36725929
- Version used: **0.9.5**
- Evidence: Models were inspected and modified in Coot v.0.9.5 (ref.
- Full pipeline: normalisation [MotionCor2] -> differential/statistical testing [RELION v3.1] -> structure determination [PHENIX] -> stage not stated [Coot v0.9.5]

### RNA targeting unleashes indiscriminate nuclease activity of CRISPR-Cas12a2. (Nature 2023)

- DOI: 10.1038/s41586-022-05560-w | PMCID: PMC9849127 | PMID: 36599980
- Evidence: This was then used as a fiducial to build the rest of the complex de novo using in Coot.
- Full pipeline: structure determination [PHENIX v1.19] -> stage not stated [AlphaFold, ChimeraX v1.0, Coot, PyMOL v2.5]

### Structural basis of broad-spectrum β-lactam resistance in Staphylococcus aureus. (Nature 2023)

- DOI: 10.1038/s41586-022-05583-3 | PMCID: PMC9834060 | PMID: 36599987
- Evidence: Incorrect regions were deleted and iterative model building and refinement carried out in Coot 72 , Phenix real.space refine 73 in the Phenix software package 74 , and density-guided Rosetta refinement with symmetry 39 .
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [RELION]

### MCM double hexamer loading visualized with human proteins. (Nature 2024)

- DOI: 10.1038/s41586-024-08263-6 | PMCID: PMC11634765 | PMID: 39604733
- Version used: **0.9.8.1**
- Evidence: Each chain was refined in Coot v0.9.8.1 EL 55 and sections that could not be confidently built were deleted 54 .
- Full pipeline: differential/statistical testing [AlphaFold] -> structure determination [AlphaFold, Coot v0.9.8.1, PHENIX v1.21] -> stage not stated [CTFFIND v1.06, ChimeraX v1.6.1, RELION, Topaz v0.2.5]

### Nucleosome flipping drives kinetic proofreading and processivity by SWR1. (Nature 2024)

- DOI: 10.1038/s41586-024-08152-y | PMCID: PMC11618073 | PMID: 39506114
- Evidence: Different regions corresponding to secondary structures of the template were manually truncated and docked separately into the recently generated 3.8 Å SWR1–nucleosome map in configuration I in Chimera 12 , 46 , before being further built in Coot 47 .
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold, CTFFIND, Coot]

### Structural basis of mRNA decay by the human exosome-ribosome supercomplex. (Nature 2024)

- DOI: 10.1038/s41586-024-08015-6 | PMCID: PMC11540850 | PMID: 39385025
- Evidence: In several areas of the map (the EXO9 barrel and SKI2 H ), the resolution and quality of the reconstruction allowed us to manually adjust the fit of the models in Coot 50 , followed by real-space refinement from within the PHENIX suite 51 .
- Full pipeline: quantification [ImageJ] -> structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ImageJ] -> stage not stated [MotionCor2, RELION v3.1, UCSF Chimera]

### Structural basis of archaeal FttA-dependent transcription termination. (Nature 2024)

- DOI: 10.1038/s41586-024-07979-9 | PMCID: PMC11616081 | PMID: 39322680
- Evidence: The initial atomic model was subjected to real-space rigid-body refinement in Phenix 57 , and was subjected to iterative cyles of model building in Coot 56 and refinement in Phenix 57 .
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL]

### Structure of the human TIP60-C histone exchange and acetyltransferase complex. (Nature 2024)

- DOI: 10.1038/s41586-024-08011-w | PMCID: PMC11578891 | PMID: 39260417
- Evidence: Model building RuvBL1–RuvBL2 hexamer was extracted from the human INO80–nucleosome structure (Protein Data Bank (PDB) 6HTS ), placed into the map by rigid body fitting in Chimera 45 and used as a starting point for manual editing in Coot 46 .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [cryoDRGN] -> structure determination [PHENIX, cryoDRGN] -> stage not stated [AlphaFold, ChimeraX, Coot, RELION]

### Structure of a fully assembled γδ T cell antigen receptor. (Nature 2024)

- DOI: 10.1038/s41586-024-07920-0 | PMCID: PMC11485255 | PMID: 39146975
- Version used: **0.9.8.93**
- Evidence: Using Coot (v.0.9.8.93) 50 , the domains and linkers were built iteratively before real-space refinement in Phenix, including calculation of model-to-map correlation statistics 48 , 49 .
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [Coot v0.9.8.93] -> structure determination [Coot v0.9.8.93, PHENIX v1.21.1] -> visualisation [ChimeraX v1.8] -> stage not stated [CTFFIND v4.1.14, ImageJ v1.54, R v12.1, RELION v4.0]

### Molecular architecture of coronavirus double-membrane vesicle pore complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07817-y | PMCID: PMC11374677 | PMID: 39143215
- Evidence: The predicted TMDs were manually fitted into the density maps, followed by manual real-space refinement in Coot 34 .
- Full pipeline: alignment/mapping [Python] -> structure determination [ChimeraX, Coot, RELION] -> visualisation [Topaz] -> stage not stated [AlphaFold, IMOD]

### Structural basis for transthiolation intermediates in the ubiquitin pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07828-9 | PMCID: PMC11374688 | PMID: 39143218
- Evidence: Model building and refinement Initial coordinates were generated by docking individual chains from reference structures into cryo-EM maps in UCSF Chimera 65 followed by manual building in Coot 66 .
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> differential/statistical testing [Topaz] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [IMOD v4.11] -> stage not stated [CTFFIND, ChimeraX, RELION v3.1]

### FANCD2-FANCI surveys DNA and recognizes double- to single-stranded junctions. (Nature 2024)

- DOI: 10.1038/s41586-024-07770-w | PMCID: PMC11358013 | PMID: 39085614
- Evidence: After manual inspection and adjustment in Coot 40 and ISOLDE 49 , the model was iteratively refined in Coot and Phenix 50 .
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [Jupyter, Matplotlib v3.7.2, NumPy v1.26.0, Python v3.9, RELION v4.0, SciPy v1.11.3]

### Cryo-EM architecture of a near-native stretch-sensitive membrane microdomain. (Nature 2024)

- DOI: 10.1038/s41586-024-07720-6 | PMCID: PMC11324527 | PMID: 39048819
- Version used: **0.8.9.2**
- Evidence: Iterative rounds of model building, performed in Coot v.0.8.9.2, and real-space refinement, performed in PHENIX v.1.20-4459, were completed until no improvement in the model was observed.
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.8.9.2, PHENIX v1.20] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, Cellpose v2.0, RELION v2.1.0, VMD v1.9]

### CryoET of β-amyloid and tau within postmortem Alzheimer's disease brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07680-x | PMCID: PMC11269202 | PMID: 38987603
- Version used: **0.8.9.2**
- Evidence: Model building of postmortem donor tau PHF cryo-EM structure A published tau PHF fibril structure (Protein Data Bank (PDB) 5o3l ) 24 was docked into the refined cryo-EM map and one chain was adjusted to fit into the density using real-space refine in Coot v.0.8.9.2 64 .
- Full pipeline: alignment/mapping [IMOD v4.12.35] -> structure determination [Coot v0.8.9.2, PHENIX v1.17.1] -> machine learning [EMAN2 v2.99] -> stage not stated [CTFFIND v1.14, ChimeraX v1.5, Fiji, ImageJ, RELION v4.0]

### Computational design of soluble and functional membrane protein analogues. (Nature 2024)

- DOI: 10.1038/s41586-024-07601-y | PMCID: PMC11236705 | PMID: 38898281
- Evidence: Each protein chain was then real-space refined in Coot.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, Python v3.9] -> stage not stated [AlphaFold]

### Structure and topography of the synaptic V-ATPase-synaptophysin complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07610-x | PMCID: PMC11269182 | PMID: 38838737
- Evidence: These models were manually adjusted in Coot before being imported into ISOLDE 77 within ChimeraX to adjust sidechain rotamers.
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [AlphaFold, PHENIX v1.21] -> machine learning [RELION, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Coot, Python, SciPy, UCSF Chimera]

### Membraneless channels sieve cations in ammonia-oxidizing marine archaea. (Nature 2024)

- DOI: 10.1038/s41586-024-07462-5 | PMCID: PMC11153153 | PMID: 38811725
- Evidence: The model was then placed into the hexameric map as six copies and subjected to several rounds of refinement using refmac5 59 inside the CCP-EM software suite 60 and PHENIX 61 , followed by manually rebuilding in Coot 58 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [NAMD v2.14, VMD v1.94] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold v2.2.0, MotionCor2]

### Kainate receptor channel opening and gating mechanism. (Nature 2024)

- DOI: 10.1038/s41586-024-07475-0 | PMCID: PMC11186766 | PMID: 38778115
- Evidence: Model building, refinement and validation Initially, the GluK2–ConA model was constructed in Coot 58 using cryo-EM density alongside the coordinates from the full-length cryo-EM structure of GluK2 (PDB ID: 8FWQ ) and the X-ray crystal structure of ConA (PDB ID: 3ENR ) as references.
- Full pipeline: simulation/modelling [VMD v1.9.4] -> structure determination [Coot, PHENIX, PyMOL] -> visualisation [ChimeraX, PyMOL]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Version used: **0.8**
- Evidence: Model building and geometry refinement The first atomic models of FLVCR1 and FLVCR2 were built into the respective electron microscopy density maps of the as-isolated state in Coot (v0.8) or ISOLDE within ChimeraX (v.1.5 and 1.6) 39 – 41 , using the AlphaFold predicted structures as initial templates 42 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### Discovery of potent small-molecule inhibitors of lipoprotein(a) formation. (Nature 2024)

- DOI: 10.1038/s41586-024-07387-z | PMCID: PMC11111404 | PMID: 38720069
- Version used: **0.8**
- Evidence: Model building was performed with Coot v.0.8 (CCP4) and final structure validation with MolProbity v.4.02 (ref.
- Full pipeline: normalisation [CCP4 v6.5] -> structure determination [REFMAC v5.8] -> stage not stated [Coot v0.8]

### Streptomyces umbrella toxin particles block hyphal growth of competing species. (Nature 2024)

- DOI: 10.1038/s41586-024-07298-z | PMCID: PMC11062931 | PMID: 38632398
- Evidence: Umb1 particle model building and refinement All models were built and refined by iterating between manual rebuilding and refinement in Coot 53 and Rosetta 54 .
- Full pipeline: alignment/mapping [ColabFold] -> structure determination [Coot, Topaz] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, Python, RELION, RoseTTAFold, napari]

### Structural basis of Integrator-dependent RNA polymerase II termination. (Nature 2024)

- DOI: 10.1038/s41586-024-07269-4 | PMCID: PMC11062913 | PMID: 38570683
- Evidence: Manual adjustments to the model were made in Coot (ref.
- Full pipeline: structure determination [ChimeraX, ColabFold, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, Coot, RELION v3.1]

### Molecular insights into capsular polysaccharide secretion. (Nature 2024)

- DOI: 10.1038/s41586-024-07248-9 | PMCID: PMC11041684 | PMID: 38570679
- Evidence: Model building and refinement To generate the initial model of the Apo 1 state of KpsMT-KpE, the Alphafold2 models 25 of the individual subunits were rigid-body-docked into the EM map using Chimera 52 , and the model was iteratively real-space refined in Coot and Phenix:refine 51 , 53 .
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ImageJ]

### Targeted protein degradation via intramolecular bivalent glues. (Nature 2024)

- DOI: 10.1038/s41586-024-07089-6 | PMCID: PMC10917667 | PMID: 38383787
- Version used: **0.9.8.1**
- Evidence: DCAF16 was built using a combination of models from ColabFold 69 , 70 (v1.3), ModelAngelo 71 (v0.2.2) and manual building in Coot (v0.9.8.1).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> visualisation [ChimeraX, PyMOL] -> stage not stated [ColabFold, Coot v0.9.8.1, Nextflow, PHENIX v1.20.1]

### The UFM1 E3 ligase recognizes and releases 60S ribosomes from ER translocons. (Nature 2024)

- DOI: 10.1038/s41586-024-07093-w | PMCID: PMC10937380 | PMID: 38383789
- Version used: **0.9.8.1**
- Evidence: Atomic models were built using Coot (v.0.9.8.1) 50 .
- Full pipeline: registration [RELION v3.1] -> structure determination [AlphaFold, ChimeraX v1.2.5, REFMAC] -> machine learning [cryoDRGN v3.2.0] -> stage not stated [CCP4, Coot v0.9.8.1, PHENIX v1.2.1]

### A new family of bacterial ribosome hibernation factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07041-8 | PMCID: PMC10901736 | PMID: 38355796
- Version used: **0.8.9.2**
- Evidence: The models predicted by AlphaFold2 65 , 66 for Rv2629 and Msmeg1130 were docked into the density maps and adjusted in Coot v0.8.9.2 56 . mRNA was modelled as poly-U and tRNA Phe was modelled in the P site.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, Coot v0.8.9.2, UCSF Chimera v1.14] -> stage not stated [ChimeraX v1.4, HMMER, PHENIX v1.20.1, RELION v3.1]

### Structural basis of ribosomal 30S subunit degradation by RNase R. (Nature 2024)

- DOI: 10.1038/s41586-024-07027-6 | PMCID: PMC10901742 | PMID: 38326618
- Evidence: This model was updated in Coot using protein restraints generated by ProSmart from AlphaFold models for all 30S ribosomal proteins 67 – 72 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, MotionCor2] -> visualisation [BEDTools, ImageJ] -> stage not stated [AlphaFold, ChimeraX, Coot, RELION v3.1.3]

### Translation selectively destroys non-functional transcription complexes. (Nature 2024)

- DOI: 10.1038/s41586-023-07014-3 | PMCID: PMC10881389 | PMID: 38326611
- Evidence: Extra DNA and RNA extensions to the main chains were completed in Coot, before further cycles of refinement and processing in phenix and Coot.
- Full pipeline: differential/statistical testing [ggplot2] -> structure determination [ChimeraX, Coot] -> stage not stated [RELION]

### A new antibiotic traps lipopolysaccharide in its intermembrane transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06799-7 | PMCID: PMC10794137 | PMID: 38172635
- Evidence: Manual model building was carried out in Coot 67 .
- Full pipeline: alignment/mapping [RELION] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX, Coot]

### Cryo-EM structures of PP2A:B55-FAM122A and PP2A:B55-ARPP19. (Nature 2024)

- DOI: 10.1038/s41586-023-06870-3 | PMCID: PMC10765524 | PMID: 38123684
- Evidence: Cryo-EM model building All models were built and refined by iterating between manual rebuilding and refinement in Coot 57 and ISOLDE 58 , and automated global real-space refinement in Phenix 59 .
- Full pipeline: quantification [ImageJ v1.53t] -> structure determination [Coot, PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, RELION v4.0]

### Structural basis of Gabija anti-phage defence and viral immune evasion. (Nature 2024)

- DOI: 10.1038/s41586-023-06855-2 | PMCID: PMC10781630 | PMID: 37992757
- Evidence: Model building was completed in Coot 22 and then refined in PHENIX.
- Full pipeline: structure determination [Coot] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, PHENIX]

### Synthetic α-synuclein fibrils replicate in mice causing MSA-like pathology. (Nature 2025)

- DOI: 10.1038/s41586-025-09698-1 | PMCID: PMC12695662 | PMID: 41193804
- Evidence: To build the 1B P atomic model, one β-rung of the 1B model was fitted into the 1B P density using a rigid-body fit in ChimeraX 51 (v.1.10.1), followed by a jiggle-fit and all-atom refinement in Coot 49 (v.0.9.8.96).
- Full pipeline: structure determination [ChimeraX, Coot, IMOD, PHENIX, RELION v4.0] -> stage not stated [MACS2]

### The Panoptes system uses decoy cyclic nucleotides to defend against phage. (Nature 2025)

- DOI: 10.1038/s41586-025-09557-z | PMCID: PMC12657218 | PMID: 41034579
- Version used: **1.1.17**
- Evidence: The structures of Kp OptS were iteratively refined using the phenix.refine program and the residue positions were manually adjusted in Coot (v.1.1.17) 60 .
- Full pipeline: differential/statistical testing [tidyverse] -> structure determination [Coot v1.1.17] -> visualisation [PyMOL, tidyverse] -> stage not stated [AlphaFold, ColabFold v1.5.5, PHENIX]

### A new paradigm for outer membrane protein biogenesis in the Bacteroidota. (Nature 2025)

- DOI: 10.1038/s41586-025-09532-8 | PMCID: PMC12611786 | PMID: 41034578
- Version used: **0.9**
- Evidence: Model building, structure refinement and figure preparation Iterative model building and real-space refinement using secondary structure, rotamer, and Ramachandran restraints was performed in Coot v0.9 61 and Phenix 1.21 62 , respectively.
- Full pipeline: structure determination [Coot v0.9, PHENIX v1.21] -> stage not stated [AlphaFold, ChimeraX, RELION v4.03]

### A nanobody specific to prefusion glycoprotein B neutralizes HSV-1 and HSV-2. (Nature 2025)

- DOI: 10.1038/s41586-025-09438-5 | PMCID: PMC12507662 | PMID: 40903574
- Evidence: An initial model was built using ModelAngelo 53 and missing residues were added in Coot 54 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot]

### Structural basis for the dynamic regulation of mTORC1 by amino acids. (Nature 2025)

- DOI: 10.1038/s41586-025-09428-7 | PMCID: PMC12507694 | PMID: 40836086
- Version used: **0.9.8**
- Evidence: These initial models were iteratively rebuilt through cycles of interactive adjustments in Coot (v0.9.8) 53 and refinement in phenix.real_space_refine (Phenix v2.0) 54 , incorporating AlphaFold 2 (refs.
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [AlphaFold, ChimeraX v1.8, Coot v0.9.8] -> machine learning [Topaz] -> stage not stated [CTFFIND v4.1.14, MotionCor2, PHENIX v2.0, RELION v5.0]

### Molecular mechanism of ultrafast transport by plasma membrane Ca&lt;sup&gt;2+&lt;/sup&gt;-ATPases. (Nature 2025)

- DOI: 10.1038/s41586-025-09402-3 | PMCID: PMC12488499 | PMID: 40836084
- Evidence: The structure was then iteratively refined using a combination of real-space refinement in PHENIX 68 and model adjustment in Coot until convergence as evaluated by model-to-map fit with valid geometrical parameters.
- Full pipeline: structure determination [Coot, RELION v3.1, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1.10, ChimeraX, MotionCor2, PHENIX]

### SLC45A4 is a pain gene encoding a neuronal polyamine transporter. (Nature 2025)

- DOI: 10.1038/s41586-025-09326-y | PMCID: PMC12507699 | PMID: 40836097
- Version used: **0.9.8.1**
- Evidence: Model building was performed in Coot (v.0.9.8.1 EL) 60 and ISOLDE 61 , refinement in PHENIX (v.1.20.1-4487) real-space refinement 62 and validation in MolProbity 63 .
- Full pipeline: quality control [PLINK v1.90b] -> alignment/mapping [FUMA] -> variant calling [PLINK v1.90b] -> structure determination [Coot v0.9.8.1, PHENIX v1.20.1] -> stage not stated [Cellpose v2.0, ChimeraX, ImageJ, MAGMA, PyMOL, REGENIE v3.4.1, RELION v3.1]

### Structural basis of fast N-type inactivation in K&lt;sub&gt;v&lt;/sub&gt; channels. (Nature 2025)

- DOI: 10.1038/s41586-025-09339-7 | PMCID: PMC12460158 | PMID: 40770100
- Evidence: The model was then manually built in Coot 65 and refined using real_space_ refine in PHENIX 66 with secondary structure and geometry restraints.
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2, RELION, Topaz]

### Programmable protein ligation on cell surfaces. (Nature 2025)

- DOI: 10.1038/s41586-025-09287-2 | PMCID: PMC12321220 | PMID: 40739351
- Evidence: Iterative rounds of model building in Coot 44 and refinements in PHENIX Refine (v.1.17_3644) 45 were performed to obtain the final structure.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, CCP4, PyMOL v2.5]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Evidence: Cryo-EM map contour sigma levels have been reported based on map normalization in Coot.
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### Loss of FCoV-23 spike domain 0 enhances fusogenicity and entry kinetics. (Nature 2025)

- DOI: 10.1038/s41586-025-09155-z | PMCID: PMC12408340 | PMID: 40634609
- Version used: **0.9.8.8**
- Evidence: Cryo-EM model building and analysis Model Angelo 82 was used to generate an initial model, and UCSF Chimera (v.1.8) 83 and Coot (v.0.9.8.8) 84 were used to manually build the model.
- Full pipeline: structure determination [PHENIX v1.21] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Coot v0.9.8.8, RELION v5.0b, UCSF Chimera v1.8]

### Architecture, dynamics and biogenesis of GluA3 AMPA glutamate receptors. (Nature 2025)

- DOI: 10.1038/s41586-025-09325-z | PMCID: PMC12422969 | PMID: 40592473
- Version used: **0.9.8.95**
- Evidence: Model building and refinement UCSF ChimeraX 60 , PHENIX (v.1.20) 61 , COOT (v.0.9.8.95) 62 , Refmac-Servalcat 63 and PyMOL 2.5 (Schrödinger) were used for all molecular modelling and refinement.
- Full pipeline: alignment/mapping [Python] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot v0.9.8.95, PHENIX v1.20, PyMOL v2.5] -> stage not stated [RELION v5.0]

### Gating and noelin clustering of native Ca&lt;sup&gt;2+&lt;/sup&gt;-permeable AMPA receptors. (Nature 2025)

- DOI: 10.1038/s41586-025-09289-0 | PMCID: PMC12422955 | PMID: 40550474
- Evidence: The structure was manually adjusted in Coot, with stereochemical restraints applied 57 and further refined by real-space refinement using Phenix 58 .
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL v3.1] -> stage not stated [AlphaFold, ChimeraX, UCSF Chimera]

### Interactions between TTYH2 and APOE facilitate endosomal lipid transfer. (Nature 2025)

- DOI: 10.1038/s41586-025-09200-x | PMCID: PMC12328215 | PMID: 40562935
- Evidence: The nanobody was placed into the density in Chimera and the CDR loops were manually edited to match the Sb1 sequence in Coot.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, ImageJ, Python, RELION, Topaz]

### RIFINs displayed on malaria-infected erythrocytes bind KIR2DL1 and KIR2DS1. (Nature 2025)

- DOI: 10.1038/s41586-025-09091-y | PMCID: PMC12310515 | PMID: 40500441
- Version used: **0.8.9.2**
- Evidence: Building and refinement cycles were carried out using Coot (v.0.8.9.2) 53 and BUSTER (v.2.10) 54 .
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Clustal Omega, PyMOL, featureCounts] -> normalisation [featureCounts] -> structure determination [Coot v0.8.9.2] -> stage not stated [BWA, Flye, ImageJ v1.54b, Pilon]

### Stepwise ATP translocation into the endoplasmic reticulum by human SLC35B1. (Nature 2025)

- DOI: 10.1038/s41586-025-09069-w | PMCID: PMC12267056 | PMID: 40399679
- Evidence: Model building for the ADP-bound SLC35B1 and AMP–PNP-bound SLC35B1(Q113F) variants was also performed using the apo structure as a starting model, followed by manual adjustment in Coot 58 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, Galaxy, PyMOL]

### Molecular basis of SIFI activity in the integrated stress response. (Nature 2025)

- DOI: 10.1038/s41586-025-09074-z | PMCID: PMC12286842 | PMID: 40328314
- Evidence: Coordinates of the medium-resolution to high-resolution regions were refined with multiple iterations of PHENIX real-space refinement 61 and manual refinement in Coot 62 .
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, PyMOL, Singularity]

### Naturally ornate RNA-only complexes revealed by cryo-EM. (Nature 2025)

- DOI: 10.1038/s41586-025-09073-0 | PMCID: PMC12286853 | PMID: 40328315
- Version used: **0.9.8**
- Evidence: Manual model correction and refinement was accomplished in Coot (version 0.9.8) 54 .
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [Coot v0.9.8, MUSCLE] -> visualisation [AlphaFold] -> stage not stated [ChimeraX v1.8, PHENIX, RELION]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Version used: **1.1**
- Evidence: The model was then manually built and adjusted in Coot (v.1.1) 88 , followed by real-space refinement in Phenix (v.1.21) 89 (Supplementary Table 11 ).
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### Chromosome end protection by RAP1-mediated inhibition of DNA-PK. (Nature 2025)

- DOI: 10.1038/s41586-025-08896-1 | PMCID: PMC12221994 | PMID: 40240611
- Evidence: The composite map (EMD-19065) was subsequently used for model building in Coot 47 and figure generation in ChimeraX 48 .
- Full pipeline: structure determination [PHENIX v1.20.1] -> stage not stated [AlphaFold, ChimeraX, Coot]

### Structure of the ATP-driven methyl-coenzyme M reductase activation complex. (Nature 2025)

- DOI: 10.1038/s41586-025-08890-7 | PMCID: PMC12176620 | PMID: 40240609
- Version used: **0.9.8.92**
- Evidence: Coot (v.0.9.8.92) was used to manually rebuild the model followed by iterative real-space refinements in PHENIX (v.1.21-5207).
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [Coot v0.9.8.92, PHENIX v1.21] -> machine learning [Topaz] -> visualisation [ChimeraX v1.6.1] -> stage not stated [AlphaFold, IQ-TREE, UCSF Chimera v1.17.3]

### Small molecules restore mutant mitochondrial DNA polymerase activity. (Nature 2025)

- DOI: 10.1038/s41586-025-08856-9 | PMCID: PMC12158775 | PMID: 40205042
- Version used: **0.9.8.1**
- Evidence: Model building, refinement and analysis To build the wild-type and mutant POLγ structures, the POLγ ternary complex (PDB ID: 4ZTZ ) was docked into the cryo-EM maps by rigid body fitting in UCSF ChimeraX (v.1.4) and manually fitted in real space in Coot (v.0.9.8.1) and ISOLDE (v.1.4) 31 – 33 .
- Full pipeline: structure determination [ChimeraX v1.4, Coot v0.9.8.1] -> stage not stated [PHENIX]

### A coronavirus assembly inhibitor that targets the viral membrane protein. (Nature 2025)

- DOI: 10.1038/s41586-025-08773-x | PMCID: PMC11981944 | PMID: 40140569
- Evidence: An initial round of molecular-dynamics flexible fitting was then done on the combined model using Namdinator 64 and then manually adjusted in Coot 65 .
- Full pipeline: quantification [ImageJ] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [Coot, UCSF Chimera]

### Chanoclavine synthase operates by an NADPH-independent superoxide mechanism. (Nature 2025)

- DOI: 10.1038/s41586-025-08670-3 | PMCID: PMC12003167 | PMID: 40044871
- Version used: **0.9.6**
- Evidence: The model was manually adjusted in Coot v.0.9.6 (ref.
- Full pipeline: structure determination [PHENIX v1.20] -> stage not stated [AlphaFold, Coot v0.9.6, UCSF Chimera]

### Structural dynamics of human fatty acid synthase in the condensing cycle. (Nature 2025)

- DOI: 10.1038/s41586-025-08782-w | PMCID: PMC12058526 | PMID: 39978408
- Evidence: Final human endogenous FASN models were validated in Coot and using Molprobity 68 .
- Full pipeline: registration [MotionCor2, RELION] -> structure determination [ChimeraX, PHENIX] -> machine learning [cryoDRGN] -> visualisation [UCSF Chimera] -> stage not stated [CTFFIND, Coot]

### Snapshots of acyl carrier protein shuttling in human fatty acid synthase. (Nature 2025)

- DOI: 10.1038/s41586-025-08587-x | PMCID: PMC12058525 | PMID: 39979457
- Evidence: The Ppant arm was built into the models in Coot using the previously reported coordinates for 4HH in the PDB.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Coot, RELION v3.1]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: The initial model was refined using Phenix.Refine 82 v.1.8.3 and manually adjusted in Coot 83 v.0.8.9.
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. (Nature 2025)

- DOI: 10.1038/s41586-024-08533-3 | PMCID: PMC11882451 | PMID: 39939763
- Version used: **0.9.8.91**
- Evidence: The resulting model was subsequently rebuilt in Coot (0.9.8.91) 64 on the basis of the protein sequences and the electron microscopy density and was further improved by real-space refinement in PHENIX (1.20.1-4487-000) 65 , 66 .
- Full pipeline: differential/statistical testing [R, limma] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1, Topaz] -> visualisation [Cytoscape v3.5.10, PyMOL] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, STRING db, ggplot2 v3.5.0, pandas v1.5.1]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Version used: **0.9.8.91**
- Evidence: The resulting model was subsequently rebuilt in Coot (v.0.9.8.91) 78 based on the protein sequences and the EM density and was further improved by real-space refinement in PHENIX (v.1.20.1-4487-000) 79 , 80 .
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### Targeting protein-ligand neosurfaces with a generalizable deep learning tool. (Nature 2025)

- DOI: 10.1038/s41586-024-08435-4 | PMCID: PMC11903328 | PMID: 39814890
- Version used: **0.9.5**
- Evidence: Atomic model adjustment and refinement were completed using COOT (v.0.9.5) and Phenix.refine 79 , 80 (v.1.20.1-4487).
- Full pipeline: structure determination [Coot v0.9.5] -> visualisation [ChimeraX, PyMOL v2.4] -> stage not stated [AlphaFold, ColabFold, PHENIX, RDKit, RoseTTAFold]

### Structural diversity of axonemes across mammalian motile cilia. (Nature 2025)

- DOI: 10.1038/s41586-024-08337-5 | PMCID: PMC11779644 | PMID: 39743588
- Evidence: For densities at intermediate resolution (around 5 Å), we applied one of three structure-based approaches, either (1) manual tracing of helices in Coot, followed by querying AlphaFold2 databases using the DALI server 70 , deepTracerID 71 or FoldSeek 72 ; (2) automatic fitting of AlphaFold predictions into segmented density using the colores algorithm 73 in the Situs package 74 , followed by rankin...
- Full pipeline: alignment/mapping [IMOD] -> registration [IMOD] -> dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot]

### Structure and mechanism of the Zorya anti-phage defence system. (Nature 2025)

- DOI: 10.1038/s41586-024-08493-8 | PMCID: PMC11946911 | PMID: 39662505
- Evidence: The model was refined in Coot 49 , or using StarMap 50 in the case of ZorC, for which the map is anisotropic and the resolution is modest.
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> dimensionality reduction/clustering [ColabFold v1.5.2, MUSCLE v5.1] -> simulation/modelling [GROMACS v2022.5, PyMOL] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, Python, ilastik]

### Vaccination generates broadly cross-neutralizing antibodies to the HIV Env apex. (Nature 2026)

- DOI: 10.1038/s41586-026-10429-3 | PMCID: PMC13275315 | PMID: 42056526
- Version used: **0.9.8**
- Evidence: Manual building was performed in Coot v.0.9.8 and real space refinement in Phenix 57 , 58 .
- Full pipeline: structure determination [AlphaFold, Coot v0.9.8, PHENIX] -> stage not stated [ChimeraX, RELION v4.0]

### Structural basis of fungal β-1,3-glucan synthase inhibition by caspofungin. (Nature 2026)

- DOI: 10.1038/s41586-026-10409-7 | PMCID: PMC13249079 | PMID: 42020744
- Version used: **0.98**
- Evidence: Model building and refinement The Sc Fks1 structure at the L2 state was built de novo in Coot (v.0.98) 49 .
- Full pipeline: alignment/mapping [UCSF Chimera] -> registration [RELION] -> simulation/modelling [GROMACS, MDAnalysis v2.7.0, Python, VMD v1.9] -> structure determination [Coot v0.98, UCSF Chimera] -> visualisation [MDAnalysis v2.7.0, Python, VMD v1.9] -> stage not stated [AlphaFold, ChimeraX v1.10, PHENIX v1.20, PyMOL v3.1]

### Template-driven scaffolding of SCF&lt;sup&gt;FBXO42&lt;/sup&gt; regulates PP2A degradation. (Nature 2026)

- DOI: 10.1038/s41586-026-10368-z | PMCID: PMC13233325 | PMID: 41986709
- Evidence: The resolution in the map was sufficiently high enough for us to manually build CCDC6 in Coot 73 .
- Full pipeline: quantification [limma] -> differential/statistical testing [limma] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, Coot, PHENIX, R]

### Cytoplasmic lattices are megadalton storage complexes in mammalian oocytes. (Nature 2026)

- DOI: 10.1038/s41586-026-10513-8 | PMCID: PMC13253339 | PMID: 41986725
- Evidence: We then iteratively refined the model in Phenix 56 with manual adjustment in Coot 57 .
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [AlphaFold, RELION]

### A µ-opioid receptor superagonist analgesic with minimal adverse effects. (Nature 2026)

- DOI: 10.1038/s41586-026-10299-9 | PMCID: PMC13128446 | PMID: 41922775
- Version used: **0.9.8.1**
- Evidence: Manual model building was performed in Coot v.0.9.8.1 EL 78 with refinement in Phenix 79 .
- Full pipeline: normalisation [R] -> registration [RELION] -> structure determination [Coot v0.9.8.1, PHENIX]

### Structural basis of supercoiling-induced CRISPR-Cas9 off-target activity. (Nature 2026)

- DOI: 10.1038/s41586-026-10255-7 | PMCID: PMC13171457 | PMID: 41882360
- Evidence: Modelling was performed in Coot 69 ; first, the coordinates were rigid-body fitted to each map using ChimeraX 70 , after minimization using Namdinator 71 , and refined further in Coot by real space refinement, manually updating the positioning and ID of each residue, DNA and RNA nucleotide.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX, RELION] -> stage not stated [AlphaFold, Fiji, ImageJ, Topaz]

### Structures of Marburgvirus glycoprotein and its complex with NPC1 receptor. (Nature 2026)

- DOI: 10.1038/s41586-026-10240-0 | PMCID: PMC13171430 | PMID: 41813895
- Version used: **0.8.9**
- Evidence: Initial model building for the RAVV GPcl, RAVV GPcl–NPC1-C complex and RAVV GP-ΔM–Nanosota-MB1 complex was performed in Coot (v0.8.9) 44 using the structure with PDB ID 6BP2 as the starting model.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX v1.16] -> visualisation [ChimeraX v0.93, PyMOL] -> stage not stated [CTFFIND v4.1.13, Coot v0.8.9]

### B cell imprinting in children impairs antibodies to the haemagglutinin stalk. (Nature 2026)

- DOI: 10.1038/s41586-026-10248-6 | PMCID: PMC13171607 | PMID: 41813896
- Version used: **0.9.8**
- Evidence: The models were manually adjusted using Coot (v.0.9.8) 58 and further refined through Rosetta Relax 59 and real-space refinement in Phenix 60 .
- Full pipeline: quality control [Seurat v4.3.0, UMAP] -> alignment/mapping [Clustal Omega] -> normalisation [Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.3.0, UMAP, fgsea] -> differential/statistical testing [Seurat v4.3.0, UMAP] -> structure determination [Coot v0.9.8, PHENIX] -> visualisation [R v4.2, Seurat v4.3.0, UMAP, ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python]

### Snapshots of the dynamic basis of NTSR1 G protein subtype promiscuity. (Nature 2026)

- DOI: 10.1038/s41586-026-10120-7 | PMCID: PMC13083256 | PMID: 41813894
- Evidence: Manual model building was performed in Coot 47 with refinement in Phenix 48 .
- Full pipeline: simulation/modelling [NAMD] -> structure determination [Coot, PHENIX] -> stage not stated [Python, VMD]

### Mechanism of co-transcriptional cap snatching by influenza polymerase. (Nature 2026)

- DOI: 10.1038/s41586-026-10189-0 | PMCID: PMC13128444 | PMID: 41781612
- Evidence: The RNA and DNA were manually adjusted in Coot 68 to fit the sequences used in this study.
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> stage not stated [ChimeraX v1.6.1, Coot, RELION]

### DICER cleavage fidelity is governed by 5'-end binding pockets. (Nature 2026)

- DOI: 10.1038/s41586-026-10211-5 | PMCID: PMC13171623 | PMID: 41781616
- Version used: **0.9.8.96**
- Evidence: These initial models were aligned with the cryo-EM density maps using the Fit-in-Map tool in ChimeraX v.1.7, followed by manual refinement in Coot (WinCoot v.0.9.8.96) 49 , 50 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, Bowtie2, Coot v0.9.8.96] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.7, Coot v0.9.8.96, PHENIX v1.20.1] -> stage not stated [PyMOL]

### Integrase anchors viral RNA to the HIV-1 capsid interior. (Nature 2026)

- DOI: 10.1038/s41586-026-10154-x | PMCID: PMC13102720 | PMID: 41708858
- Evidence: The model was adjusted in Coot 60 to match the amino acid sequence of SIVtal IN and refined using phenix.real_space_refine (v.1.21.2-5419) 61 .
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0, RELION] -> normalisation [ImageJ, NAMD v3.0.1] -> simulation/modelling [VMD] -> structure determination [ChimeraX, Coot, IMOD] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PyMOL, Topaz, UCSF Chimera]

### CSN5i-3 is an orthosteric molecular glue inhibitor of COP9 signalosome. (Nature 2026)

- DOI: 10.1038/s41586-026-10129-y | PMCID: PMC13128448 | PMID: 41673158
- Evidence: The CSN7a from 4D10 served as a template to trace the main chain, and the residue sequence was modified to match CSN7b in Coot 40 .
- Full pipeline: structure determination [PHENIX, Topaz] -> stage not stated [ChimeraX, Coot, PyMOL]

### Bacterial immune activation via supramolecular assembly with phage triggers. (Nature 2026)

- DOI: 10.1038/s41586-025-10060-8 | PMCID: PMC13017515 | PMID: 41639456
- Evidence: The Gp77-focused map enabled docking of residues 1–125 into the inner ring using ‘phenix.local_em_fitting’ in ChimeraX, followed by manual adjustments in Coot and subsequent refinement in Phenix.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, Cutadapt v1.15] -> alignment/mapping [Bowtie2 v2.3.4.1, Cutadapt v1.15, MAFFT, NumPy, SAMtools v1.7] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> machine learning [Topaz]

### A prophage-encoded abortive infection protein preserves host and prophage spread. (Nature 2026)

- DOI: 10.1038/s41586-025-10070-6 | PMCID: PMC13043305 | PMID: 41606329
- Evidence: For both structures, model building was completed in Coot and then refined in PHENIX.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT] -> structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BEDTools v2.27.1, PHENIX, SAMtools v1.1]

### Fibroblastic reticular cells direct the initiation of T cell responses via CD44. (Nature 2026)

- DOI: 10.1038/s41586-025-09988-8 | PMCID: PMC12999478 | PMID: 41565815
- Evidence: The structure was refined via iterative cycles of model building in Coot and refinement using Buster ( http://globalphasing.com/buster/ ).
- Full pipeline: normalisation [CCP4] -> structure determination [Coot] -> stage not stated [CellProfiler, ImageJ, PHENIX, PyMOL]

### Structural basis of regulated N-glycosylation at the secretory translocon. (Nature 2026)

- DOI: 10.1038/s41586-025-09756-8 | PMCID: PMC12804085 | PMID: 41261126
- Evidence: The model was fit using tightly restrained real-space refinement in Coot 79 , including planar and trans peptide restraints, Ramachandran restraints and Geman-McClure local distance restraints.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [TopHat v2.1.0] -> quantification [HTSeq v2.0.3] -> structure determination [Coot, PHENIX] -> machine learning [Coot] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

### ZAK activation at the collided ribosome. (Nature 2026)

- DOI: 10.1038/s41586-025-09772-8 | PMCID: PMC12823453 | PMID: 41261136
- Evidence: The resulting models were fitted into the corresponding density with only minor adjustments in Coot (Extended Data Fig.
- Full pipeline: read trimming [SAMtools, Trim Galore] -> alignment/mapping [MotionCor2 v1.4.0, SAMtools, STAR] -> structure determination [AlphaFold, ChimeraX v1.9, PHENIX v1.20.1, UCSF Chimera] -> stage not stated [Coot, RELION v5.0]

### An ATP-gated molecular switch orchestrates human mRNA export. (Nature 2026)

- DOI: 10.1038/s41586-025-09832-z | PMCID: PMC12823420 | PMID: 41198879
- Evidence: The ALYREF N-UBM was modelled in Coot based on the superposition of an AlphaFold2 Multimer prediction model of a UAP56–ALYREF complex on UAP56 chain p.
- Full pipeline: visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, Cellpose, Coot, RELION v3.1]

### Vascular K<sub>ATP</sub> channel structural dynamics reveal regulatory mechanism by Mg-nucleotides. (PNAS 2021)

- DOI: 10.1073/pnas.2109441118 | PMCID: PMC8694068 | PMID: 34711681
- Evidence: Models were built by fitting previously published Kir6.2/SUR1 structures and in SWISS-MODEL and refined in Coot and Phenix.
- Full pipeline: simulation/modelling [GROMACS v2019.4] -> structure determination [Coot, PHENIX] -> stage not stated [RELION]

### Cryo-EM structure determination of small proteins by nanobody-binding scaffolds (Legobodies). (PNAS 2021)

- DOI: 10.1073/pnas.2115001118 | PMCID: PMC8521671 | PMID: 34620716
- Evidence: All model building was done in Coot.
- Full pipeline: registration [MotionCor2] -> stage not stated [Coot, PHENIX, RELION v3.1]

### Structural basis of rotavirus RNA chaperone displacement and RNA annealing. (PNAS 2021)

- DOI: 10.1073/pnas.2100198118 | PMCID: PMC8521686 | PMID: 34615715
- Evidence: The Namdinator model was used for multiple iterative rounds of manual adjustment in Coot ( 55 ) and real-space refinement in Phenix ( 56 ).
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ImageJ] -> stage not stated [RELION]

### Structure of autoinhibited Akt1 reveals mechanism of PIP&lt;sub&gt;3&lt;/sub&gt;-mediated activation. (PNAS 2021)

- DOI: 10.1073/pnas.2101496118 | PMCID: PMC8379990 | PMID: 34385319
- Evidence: The model was built in Coot ( 60 ) with iterative rounds of refinement and model validation in PHENIX ( 61 ).
- Full pipeline: structure determination [Coot, PHENIX]

### High-resolution asymmetric structure of a Fab-virus complex reveals overlap with the receptor binding site. (PNAS 2021)

- DOI: 10.1073/pnas.2025452118 | PMCID: PMC8201801 | PMID: 34074770
- Evidence: The crystal structures for Fab 14 (PDB ID: 3GK8) ( 18 ) and the CPV capsid (PDB ID: 2CAS) ( 22 ) were fitted into the corresponding densities to initiate the builds followed by manual adjustment in Coot and simulated annealing in PHENIX.
- Full pipeline: registration [RELION] -> simulation/modelling [Coot] -> structure determination [RELION] -> stage not stated [PHENIX]

### PilB from &lt;i&gt;Streptococcus sanguinis&lt;/i&gt; is a bimodular type IV pilin with a direct role in adhesion. (PNAS 2021)

- DOI: 10.1073/pnas.2102092118 | PMCID: PMC8179133 | PMID: 34031252
- Evidence: Manual building in Coot ( 59 ) was performed on the high-resolution dataset, and the full model was then used for molecular replacement in the low-resolution datasets.
- Full pipeline: visualisation [PyMOL] -> stage not stated [Coot, InterProScan]

### ICAM-1 induced rearrangements of capsid and genome prime rhinovirus 14 for activation and uncoating. (PNAS 2021)

- DOI: 10.1073/pnas.2024251118 | PMCID: PMC8126848 | PMID: 33947819
- Version used: **0.9**
- Evidence: The fitted models were subjected to multiple rounds of real-space refinement in Phenix (version dev-3765), reciprocal-space refinement in REFMAC5, combined with manual corrections in Coot 0.9 and ISOLDE ( 75 – 78 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot v0.9, PHENIX]

### 2'-O methylation of RNA cap in SARS-CoV-2 captured by serial crystallography. (PNAS 2021)

- DOI: 10.1073/pnas.2100170118 | PMCID: PMC8166198 | PMID: 33972410
- Evidence: The ligands Cap-1, Cap-0, m7 Gppp, m7 Gpp, AdoMet, AdoHcys, and Zn 2+ were manually placed into electron density in Coot and waters were generated using ARP/wARP ( 44 ).
- Full pipeline: alignment/mapping [UCSF Chimera] -> structure determination [REFMAC v5.8.0258] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot]

### Cryo-EM structure of <i>Mycobacterium smegmatis</i> DyP-loaded encapsulin. (PNAS 2021)

- DOI: 10.1073/pnas.2025658118 | PMCID: PMC8072242 | PMID: 33853951
- Evidence: Then Ms-Enc and Ms-DyP models were built manually in Coot ( 58 ) by mutating amino acid residues and further refined using real-space refinement in Phenix ( 59 ).
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> dimensionality reduction/clustering [RELION] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [UCSF Chimera]

### Architecture of the mycobacterial succinate dehydrogenase with a membrane-embedded Rieske FeS cluster. (PNAS 2021)

- DOI: 10.1073/pnas.2022308118 | PMCID: PMC8054011 | PMID: 33876763
- Evidence: The density quality of the interior region was higher, so model building commenced here, followed by iterative manual fitting adjustment in Coot ( 41 ) and real space refinement in PHENIX ( 42 ).
- Full pipeline: registration [CTFFIND, MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL]

### Early-stage dynamics of chloride ion-pumping rhodopsin revealed by a femtosecond X-ray laser. (PNAS 2021)

- DOI: 10.1073/pnas.2020486118 | PMCID: PMC8020794 | PMID: 33753488
- Evidence: The dark model was used as an initial model for a refinement against the ED ext map by a stepped real-space refinement in Coot ( 42 ) with the torsional restraint switched off (default in Coot).
- Full pipeline: simulation/modelling [GROMACS v5.1.2, VMD] -> structure determination [Coot] -> visualisation [VMD] -> stage not stated [CCP4, PHENIX, UCSF Chimera]

### Structure of a bacterial OapB protein with its OLE RNA target gives insights into the architecture of the OLE ribonucleoprotein complex. (PNAS 2021)

- DOI: 10.1073/pnas.2020393118 | PMCID: PMC7936274 | PMID: 33619097
- Evidence: The initial models were automatically built using the AutoBuild ( 30 ) module of the PHENIX software package ( 31 ) and manually rebuilt in Coot ( 32 ).
- Full pipeline: stage not stated [ChimeraX, Coot, PHENIX, PyMOL]

### The effect of the D614G substitution on the structure of the spike glycoprotein of SARS-CoV-2. (PNAS 2021)

- DOI: 10.1073/pnas.2022586118 | PMCID: PMC7936381 | PMID: 33579792
- Evidence: The model was initially built by rigid body refinement in PHENIX ( 26 ), followed by adjustment in Coot.
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [Coot, PHENIX] -> stage not stated [UCSF Chimera]

### Structure of the SARS-CoV-2 RNA-dependent RNA polymerase in the presence of favipiravir-RTP. (PNAS 2021)

- DOI: 10.1073/pnas.2021946118 | PMCID: PMC7896311 | PMID: 33526596
- Evidence: The atomic model was built based on a previously published atomic model of the nsp12–nsp7–nsp8 complex bound to RNA and remdesivir-RTP (Protein Data Bank [PDB] ID code 7BV2) ( 10 ), with manual model building in Coot ( 25 , 26 ), and real-space refinement in Phenix ( 27 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [RELION v3.1]

### Supramolecular assembly of the <i>Escherichia coli</i> LdcI upon acid stress. (PNAS 2021)

- DOI: 10.1073/pnas.2014383118 | PMCID: PMC7812809 | PMID: 33372137
- Evidence: After several rounds of manual correction in Coot ( 69 ), a final round of real space refinement was then performed using the same settings, but without rigid body refinement and without applying reference restraints, and setting the “nonbonded_weight” parameter to 500.
- Full pipeline: registration [MotionCor2] -> dimensionality reduction/clustering [RELION v1.4] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, ImageJ]

### Human species D adenovirus hexon capsid protein mediates cell entry through a direct interaction with CD46. (PNAS 2021)

- DOI: 10.1073/pnas.2020732118 | PMCID: PMC7826407 | PMID: 33384338
- Evidence: Refinement was carried out by manual model building in Coot ( 59 ) alternated with restraint refinement including anisotropic B-factor refinement using phenix.refine ( 60 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [CCP4, CTFFIND, ChimeraX, EMAN2, MotionCor2, RELION v3.1]

### Mechanism of actin filament branch formation by Arp2/3 complex revealed by a high-resolution cryo-EM structureof the branch junction. (PNAS 2022)

- DOI: 10.1073/pnas.2206722119 | PMCID: PMC9894260 | PMID: 36442092
- Evidence: Our map allowed us to build models for most residues unambiguously in Coot ( 45 ).
- Full pipeline: registration [RELION v4.0] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> visualisation [ChimeraX] -> stage not stated [Coot, PyMOL]

### Human T cells recognize HLA-DP-bound peptides in two orientations. (PNAS 2022)

- DOI: 10.1073/pnas.2214331119 | PMCID: PMC9894132 | PMID: 36442096
- Evidence: Iterative rounds of model building in Coot and restrained refinement using REFMAC (CCP4 suite) ( 27 ) and PhenixRefine (PHENIX) ( 28 ) were carried out.
- Full pipeline: structure determination [Coot, PHENIX, REFMAC] -> machine learning [Coot, PHENIX, REFMAC] -> visualisation [PyMOL] -> stage not stated [CCP4]

### Discovery of small molecules that target a tertiary-structured RNA. (PNAS 2022)

- DOI: 10.1073/pnas.2213117119 | PMCID: PMC9860313 | PMID: 36413497
- Evidence: Structure refinement was carried out in PHENIX, alternating with manual fitting in Coot.
- Full pipeline: structure determination [Coot, PHENIX]

### Structural and functional investigation of ABC transporter STE6-2p from <i>Pichia pastoris</i> reveals unexpected interaction with sterol molecules. (PNAS 2022)

- DOI: 10.1073/pnas.2202822119 | PMCID: PMC9618074 | PMID: 36256814
- Evidence: The model was manually refined in Coot ( 64 ) and real-space refined using Phenix ( 65 ), whereby refinement results were manually corrected if necessary.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [BLAST, CTFFIND, MotionCor2, RELION v3.1]

### Structural basis for host recognition and superinfection exclusion by bacteriophage T5. (PNAS 2022)

- DOI: 10.1073/pnas.2211672119 | PMCID: PMC9586334 | PMID: 36215462
- Evidence: The FhuA crystal structure and the AF2 model of pb5 were rigid-body fit in the map via Phenix DockinMap ( 46 ), and the model was built via several cycles of manual building in Coot ( 47 ) and real-space refinement within Phenix.
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [GROMACS, VMD]

### SPACA9 is a lumenal protein of human ciliary singlet and doublet microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2207605119 | PMCID: PMC9564825 | PMID: 36191189
- Version used: **0.9.4.1**
- Evidence: Model building was performed in Coot version 0.9.4.1 with torsion, planar peptide, trans peptide, and Ramachandran restraints applied ( 53 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX, Clustal Omega v1.2.2] -> stage not stated [AlphaFold, Coot v0.9.4.1, IMOD, PHENIX, PyMOL v2.3.4, RELION]

### Nanomolar inhibition of SARS-CoV-2 infection by an unmodified peptide targeting the prehairpin intermediate of the spike protein. (PNAS 2022)

- DOI: 10.1073/pnas.2210990119 | PMCID: PMC9546559 | PMID: 36122200
- Evidence: The N-terminal extension of HR2 was first built in Coot ( 37 ) and then refined by the automated structure refinement protocol in Rosetta ( 38 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, CellProfiler, EMAN2, MotionCor2, RELION, kallisto]

### Mechanism by which T7 bacteriophage protein Gp1.2 inhibits &lt;i&gt;Escherichia coli&lt;/i&gt; dGTPase. (PNAS 2022)

- DOI: 10.1073/pnas.2123092119 | PMCID: PMC9478638 | PMID: 36067314
- Evidence: Final models were obtained by iterative rounds of manual inspection and building in Coot ( 46 ) and real-space refinement in PHENIX ( 42 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot] -> machine learning [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, RELION]

### Topological crossing in the misfolded <i>Tetrahymena</i> ribozyme resolved by cryo-EM. (PNAS 2022)

- DOI: 10.1073/pnas.2209146119 | PMCID: PMC9477386 | PMID: 36067294
- Evidence: The top-scoring DRRAFTER models were manually inspected and further optimized in Coot ( 17 ) and Phenix ( 18 ).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [Coot, EMAN2, MotionCor2, PHENIX, RELION, UCSF Chimera]

### Constitutive activation of a nuclear-localized calcium channel complex in &lt;i&gt;Medicago truncatula&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2205920119 | PMCID: PMC9407390 | PMID: 35972963
- Evidence: The MtDMI1 RCK domain was built in Coot ( 46 ), and then refined by iterative rounds of manual adjustment with Coot and refinement with Phenix.
- Full pipeline: structure determination [Coot] -> stage not stated [ImageJ, PHENIX]

### The neutralizing breadth of antibodies targeting diverse conserved epitopes between SARS-CoV and SARS-CoV-2. (PNAS 2022)

- DOI: 10.1073/pnas.2204256119 | PMCID: PMC9407403 | PMID: 35972965
- Evidence: We initially fitted the templates into the corresponding final cryo-EM maps using Chimera ( 57 ) and further corrected and adjusted them manually by real-space refinement in Coot ( 58 ).
- Full pipeline: registration [MotionCor2] -> dimensionality reduction/clustering [R v3.6.3] -> structure determination [Coot] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PHENIX]

### Structures of the mannose-6-phosphate pathway enzyme, GlcNAc-1-phosphotransferase. (PNAS 2022)

- DOI: 10.1073/pnas.2203518119 | PMCID: PMC9388126 | PMID: 35939698
- Evidence: All structures were manually built in Coot ( 73 ).
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Coot, PHENIX, PyMOL]

### Structural basis of higher order oligomerization of KSHV inhibitor of cGAS. (PNAS 2022)

- DOI: 10.1073/pnas.2200285119 | PMCID: PMC9388135 | PMID: 35939686
- Evidence: Iterative model building and refinements were carried out in Coot ( 35 ) and Phenix ( 34 ).
- Full pipeline: structure determination [Coot] -> stage not stated [PHENIX]

### A multidomain connector links the outer membrane and cell wall in phylogenetically deep-branching bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2203156119 | PMCID: PMC9388160 | PMID: 35943982
- Evidence: The atomic model was subjected to several rounds of refinement using REFMAC5 ( 87 ) inside the CCP-EM software suite ( 88 ) and PHENIX ( 89 ), followed by manually rebuilding in Coot and interactive refinement using ISOLDE ( 90 ) inside UCSF ChimeraX.
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2] -> dimensionality reduction/clustering [MotionCor2] -> structure determination [ChimeraX, Coot, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold]

### Reversible structural changes in the influenza hemagglutinin precursor at membrane fusion pH. (PNAS 2022)

- DOI: 10.1073/pnas.2208011119 | PMCID: PMC9388137 | PMID: 35939703
- Evidence: Manual adjustment of the models was carried out in Coot ( 70 ) and ISOLDE ( 71 ), refinement was done using REFMAC5 ( 72 ) within the CCP-EM software suite, and model geometry and carbohydrate validation were done using MolProbity ( 73 ) and Privateer ( 74 ), respectively.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, RELION] -> visualisation [ChimeraX]

### Molecular mechanism for strengthening E-cadherin adhesion using a monoclonal antibody. (PNAS 2022)

- DOI: 10.1073/pnas.2204473119 | PMCID: PMC9371698 | PMID: 35921442
- Evidence: The model was refined with iterative rounds of refinement with Phenix ( 31 ) and manual model building in Coot ( 32 , 33 ).
- Full pipeline: dimensionality reduction/clustering [GROMACS v2020.1] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot, PHENIX]

### Single crystal spectroscopy and multiple structures from one crystal (MSOX) define catalysis in copper nitrite reductases. (PNAS 2022)

- DOI: 10.1073/pnas.2205664119 | PMCID: PMC9335323 | PMID: 35862453
- Evidence: Refinement was performed using Refmac5 ( 31 ) in the CCP4 suite ( 32 ) with manual rebuilding in Coot ( 33 ) and isotropic B-factors.
- Full pipeline: structure determination [CCP4, Coot]

### Structural basis for high-voltage activation and subtype-specific inhibition of human Na&lt;sub&gt;v&lt;/sub&gt;1.8. (PNAS 2022)

- DOI: 10.1073/pnas.2208211119 | PMCID: PMC9335304 | PMID: 35858452
- Evidence: All Na v 1.8 residues, lipids, and sugar moieties were manually checked in Coot ( 57 ).
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, Coot, MotionCor2]

### Cryo-EM structures of wild-type and E138K/M184I mutant HIV-1 RT/DNA complexed with inhibitors doravirine and rilpivirine. (PNAS 2022)

- DOI: 10.1073/pnas.2203660119 | PMCID: PMC9335299 | PMID: 35858448
- Evidence: Manual model fitting to the density map was carried out in Coot ( 53 ) followed by real-space model refinement using Phenix 1.19 ( 54 ).
- Full pipeline: alignment/mapping [CTFFIND, MotionCor2, RELION v3.1] -> structure determination [Coot, PHENIX v1.19] -> visualisation [PyMOL]

### Structural basis and molecular mechanism of biased GPBAR signaling in regulating NSCLC cell growth via YAP activity. (PNAS 2022)

- DOI: 10.1073/pnas.2117054119 | PMCID: PMC9303995 | PMID: 35858343
- Evidence: This initial model was then subjected to iterative rounds of manual adjustment and automated refinement in Coot ( 58 ) and Phenix ( 57 ), respectively.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ANTs, CTFFIND]

### Structure of PLA2R reveals presentation of the dominant membranous nephropathy epitope and an immunogenic patch. (PNAS 2022)

- DOI: 10.1073/pnas.2202209119 | PMCID: PMC9303975 | PMID: 35858348
- Evidence: Inspection of the map and model in Coot ( 43 ) revealed in-domain loops and linkers that were not resolved in the map.
- Full pipeline: stage not stated [Coot, PHENIX]

### Structural basis for heme detoxification by an ATP-binding cassette-type efflux pump in gram-positive pathogenic bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2123385119 | PMCID: PMC9271180 | PMID: 35767641
- Evidence: Structural analysis for the Mn•AMPPNP dataset was conducted using the single anomalous dispersion technique, and the other datasets were analyzed using the molecular replacement technique in Coot ( 51 ) and Phenix software package ( 52 ).
- Full pipeline: stage not stated [Coot, PHENIX]

### Structure of the human cation-chloride cotransport KCC1 in an outward-open state. (PNAS 2022)

- DOI: 10.1073/pnas.2109083119 | PMCID: PMC9271165 | PMID: 35759661
- Version used: **0.8.9.3**
- Evidence: The maps were locally sharpened in cryoSPARC 3.0 with an overall b factor of ∼ −120 Å 2 (KCC1 in 150 mM KCl) or −150 Å 2 (KCC1 bound with UV0463271) for model building in Coot 0.8.9.3 ( 63 ).
- Full pipeline: alignment/mapping [MotionCor2] -> dimensionality reduction/clustering [RELION v3.0.7] -> structure determination [PHENIX v1.18] -> stage not stated [Coot v0.8.9.3]

### Archaeal bundling pili of <i>Pyrobaculum calidifontis</i> reveal similarities between archaeal and bacterial biofilms. (PNAS 2022)

- DOI: 10.1073/pnas.2207037119 | PMCID: PMC9245690 | PMID: 35727984
- Evidence: The full-length sequence was threaded into the map using DeepTracer ( 78 ), manually adjusted in Coot ( 79 ), and real-space refined in PHENIX ( 80 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Atomic view of the HIV-1 matrix lattice; implications on virus assembly and envelope incorporation. (PNAS 2022)

- DOI: 10.1073/pnas.2200794119 | PMCID: PMC9191676 | PMID: 35658080
- Evidence: The structure was then iteratively refined with PHENIX ( 64 ) and with manual manipulation in Coot ( 65 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL]

### Structural basis of peptidomimetic agonism revealed by small- molecule GLP-1R agonists Boc5 and WB4-24. (PNAS 2022)

- DOI: 10.1073/pnas.2200155119 | PMCID: PMC9171782 | PMID: 35561211
- Evidence: This starting model was then subjected to iterative rounds of manual adjustment and automated refinement in Coot ( 35 ) and Phenix ( 36 ), respectively.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v1.06]

### Structural convergence for tubulin binding of CPAP and vinca domain microtubule inhibitors. (PNAS 2022)

- DOI: 10.1073/pnas.2120098119 | PMCID: PMC9171608 | PMID: 35507869
- Evidence: Structures were solved by molecular replacement with Phaser ( 43 ) using tubulin–iiH5 (Protein Data Bank identifier [PDB ID] 6GWD) and tubulin–iE5 (PDB ID 6GWC) as search models, and refined with BUSTER ( 44 ) with iterative model building in Coot ( 45 ).
- Full pipeline: structure determination [Coot] -> stage not stated [PyMOL]

### Cryo-EM structures show the mechanistic basis of pan-peptidase inhibition by human α<sub>2</sub>-macroglobulin. (PNAS 2022)

- DOI: 10.1073/pnas.2200102119 | PMCID: PMC9181621 | PMID: 35500114
- Evidence: The model was then rebuilt manually in Coot ( 62 ) to optimize the fit to the density for one set of disulfide-linked subunits (protomers 1 and 2).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4, Coot, RELION v2.1]

### Helical self-assembly of a mucin segment suggests an evolutionary origin for von Willebrand factor tubules. (PNAS 2022)

- DOI: 10.1073/pnas.2116790119 | PMCID: PMC9169620 | PMID: 35377815
- Evidence: A hybrid structure constructed from elements of these two docked models was rebuilt and refined by iterative cycles of Phenix ( 57 ) real-space refinement and interactive rebuilding in Coot.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX]

### Cryo-EM structures of staphylococcal IsdB bound to human hemoglobin reveal the process of heme extraction. (PNAS 2022)

- DOI: 10.1073/pnas.2116708119 | PMCID: PMC9168843 | PMID: 35357971
- Evidence: The atomic model of IsdB:HbCO complex was prepared by manually adjusting and refining in Coot ( 53 ) a starting model made using two different crystallographic structures, which describe IsdB:Hb complex (PDB ID 5VMM) ( 4 ) and native metHb (PDB ID 3P5Q) ( 54 ).
- Full pipeline: stage not stated [Coot, PHENIX, PyMOL, RELION, UCSF Chimera]

### Structural conservation among variants of the SARS-CoV-2 spike postfusion bundle. (PNAS 2022)

- DOI: 10.1073/pnas.2119467119 | PMCID: PMC9169775 | PMID: 35363556
- Evidence: The fitting of side chains in the map was manually inspected and corrected in Coot ( 65 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [CTFFIND, ChimeraX, Coot, PyMOL, Python, RELION, UCSF Chimera]

### Structural insights into the activation of autoinhibited human lipid flippase ATP8B1 upon substrate binding. (PNAS 2022)

- DOI: 10.1073/pnas.2118656119 | PMCID: PMC9168909 | PMID: 35349344
- Evidence: The final sharpened map with a B-factor of −140 Å 2 was used for model building in Coot ( 47 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [Coot, MotionCor2, RELION, UCSF Chimera]

### 50S subunit recognition and modification by the &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; ribosomal RNA methyltransferase TlyA. (PNAS 2022)

- DOI: 10.1073/pnas.2120352119 | PMCID: PMC9168844 | PMID: 35357969
- Evidence: This TlyA structure was subsequently rebuilt in Coot ( 27 ), including a complete rebuilding of the NTD ( Materials and Methods ).
- Full pipeline: alignment/mapping [Clustal Omega, RELION] -> stage not stated [CTFFIND, Coot, PHENIX v1.19.2]

### Clamping of DNA shuts the condensin neck gate. (PNAS 2022)

- DOI: 10.1073/pnas.2120006119 | PMCID: PMC9168836 | PMID: 35349345
- Evidence: Model building was carried out in Coot ( 40 ) and ISOLDE ( 41 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, PyMOL v2.5, RELION v3.1, UCSF Chimera]

### Structural determinants of dual incretin receptor agonism by tirzepatide. (PNAS 2022)

- DOI: 10.1073/pnas.2116506119 | PMCID: PMC9060465 | PMID: 35333651
- Evidence: The starting model was then subjected to iterative rounds of manual and real space refinement in Coot ( 49 , 50 ) and Phenix ( 51 ), respectively.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND]

### Mechanistic insights into the subversion of the linear ubiquitin chain assembly complex by the E3 ligase IpaH1.4 of <i>Shigella flexneri</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116776119 | PMCID: PMC8944867 | PMID: 35294289
- Evidence: All structure models were manually adjusted in Coot ( 57 ) and refined with Phenix suite ( 58 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [PyMOL]

### Re-sensitization of <i>mcr</i> carrying multidrug resistant bacteria to colistin by silver. (PNAS 2022)

- DOI: 10.1073/pnas.2119417119 | PMCID: PMC8931383 | PMID: 35263219
- Evidence: Solvents were added in Coot and refined by Refmac.
- Full pipeline: structure determination [Coot]

### Molecular basis of multistep voltage activation in plant two-pore channel 1. (PNAS 2022)

- DOI: 10.1073/pnas.2110936119 | PMCID: PMC8892357 | PMID: 35210362
- Evidence: The atomic models were generated using the crystal structures of WT AtTPC1 as a reference [PDBs: 5DQQ ( 16 ) and 5E1J ( 22 )] and manipulated in Coot ( 47 ), followed by iterative rounds of phenix.real_space_refine ( 46 ) and flexible fitting using Namdinator ( 48 ).
- Full pipeline: structure determination [Coot, PHENIX, RELION] -> visualisation [UCSF Chimera] -> stage not stated [MotionCor2]

### Structures of the junctophilin/voltage-gated calcium channel interface reveal hot spot for cardiomyopathy mutations. (PNAS 2022)

- DOI: 10.1073/pnas.2120416119 | PMCID: PMC8916002 | PMID: 35238659
- Evidence: All models were completed with iterative cycles of manual model building in Coot ( 57 ) and refinement with Refmac5 in ccp4 ( 58 ) and Phenix ( 59 ).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [ImageJ, PyMOL] -> structure determination [Coot, PHENIX]

### Structure of the Mon1-Ccz1 complex reveals molecular basis of membrane binding for Rab7 activation. (PNAS 2022)

- DOI: 10.1073/pnas.2121494119 | PMCID: PMC8833172 | PMID: 35105815
- Evidence: For model building, a combination of de novo structure prediction by TRRosetta ( 40 ) and manual model building in Coot ( 41 ) was employed.
- Full pipeline: machine learning [PHENIX] -> stage not stated [Coot, RELION]

### Structures of the peptidase-containing ABC transporter PCAT1 under equilibrium and nonequilibrium conditions. (PNAS 2022)

- DOI: 10.1073/pnas.2120534119 | PMCID: PMC8794836 | PMID: 35074919
- Evidence: The structures of the IF conformations under active turnover conditions were built by docking the cryo-EM structure of CtA–PCAT1 complex (PDB: 6V9Z) into the cryo-EM maps using rigid body fitting in Chimera, followed by manual adjustments in Coot.
- Full pipeline: alignment/mapping [CTFFIND] -> dimensionality reduction/clustering [RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [Coot, PHENIX]

### High-resolution cryo-electron microscopy structure of photosystem II from the mesophilic cyanobacterium, <i>Synechocystis</i> sp. PCC 6803. (PNAS 2022)

- DOI: 10.1073/pnas.2116765118 | PMCID: PMC8740770 | PMID: 34937700
- Evidence: Manual fitting and editing were performed in Coot ( 81 ), and automated refinement was performed using real_space_refine ( 82 ) in Phenix ( 83 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [RELION v3.1, UCSF Chimera]

### Molecular basis of differential receptor usage for naturally occurring CD55-binding and -nonbinding coxsackievirus B3 strains. (PNAS 2022)

- DOI: 10.1073/pnas.2118590119 | PMCID: PMC8794823 | PMID: 35046043
- Evidence: Model accuracy was manually adjusted in Coot ( 42 ) for improvement.
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [PHENIX] -> stage not stated [Coot, MotionCor2, PyMOL]

### Tau filaments from amyotrophic lateral sclerosis/parkinsonism-dementia complex adopt the CTE fold. (PNAS 2023)

- DOI: 10.1073/pnas.2306767120 | PMCID: PMC10743375 | PMID: 38100415
- Evidence: For maps with resolutions beyond 4 Å, atomic models were built manually in Coot ( 59 ), based on published structures [CTE type I, PDB:6NWP; CTE type II, PDB:6NWQ; TMEM106B fold I-s, PDB:7QVC; TMEM106B fold I-d, PDB:7QVF; Type II Aβ42, PDB:7Q4M ( 30 , 36 , 41 )].
- Full pipeline: structure determination [RELION] -> visualisation [ChimeraX] -> stage not stated [Coot]

### Structural and physical features that distinguish tumor-controlling from inactive cancer neoepitopes. (PNAS 2023)

- DOI: 10.1073/pnas.2312057120 | PMCID: PMC10742377 | PMID: 38085776
- Evidence: Structures were refined over multiple rounds of automated refinement with REFMAC5 ( 70 ) followed by manual refinement in Coot ( 71 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL v2.5] -> stage not stated [AlphaFold]

### Structures of the &lt;i&gt;P. aeruginosa&lt;/i&gt; FleQ-FleN master regulators reveal large-scale conformational switching in motility and biofilm control. (PNAS 2023)

- DOI: 10.1073/pnas.2312276120 | PMCID: PMC10723142 | PMID: 38051770
- Evidence: The resultant map was sharpened using the integrated Deep EMhancer tool ( 42 ) and used for rigid body fitting of structures of individual FleQ and FleN domains in Chimera, followed by model building and regularization in Coot ( 43 ) and refinements in Phenix ( 44 ) and Namdinator ( 45 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, MotionCor2]

### Structure and function of the &lt;i&gt;S. pombe&lt;/i&gt; III-IV-cyt &lt;i&gt;c&lt;/i&gt; supercomplex. (PNAS 2023)

- DOI: 10.1073/pnas.2307697120 | PMCID: PMC10655221 | PMID: 37939086
- Evidence: Refinement of the model was performed in Coot ( 89 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Lateral interactions govern self-assembly of the bacterial biofilm matrix protein BslA. (PNAS 2023)

- DOI: 10.1073/pnas.2312022120 | PMCID: PMC7615278 | PMID: 37903266
- Evidence: Molecular replacement was followed by iterative cycles of manual model building in Coot ( 38 ) and structure refinement by REFMAC5 ( 39 , 40 ).
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4] -> structure determination [Coot]

### Molecular basis for C-degron recognition by CRL2&lt;sup&gt;APPBP2&lt;/sup&gt; ubiquitin ligase. (PNAS 2023)

- DOI: 10.1073/pnas.2308870120 | PMCID: PMC10614623 | PMID: 37844242
- Evidence: For modeling of the CRL2 APPBP2 dimer, initial templates were generated in Coot ( 39 ) by fitting the predicted protein models into the density map and manually adjusting them to remove the residues with missing densities.
- Full pipeline: structure determination [Coot] -> stage not stated [AlphaFold, ChimeraX, PHENIX, PyMOL]

### Identification, structural, and biophysical characterization of a positive modulator of human Kv3.1 channels. (PNAS 2023)

- DOI: 10.1073/pnas.2220029120 | PMCID: PMC10589703 | PMID: 37812700
- Evidence: The structure was visually inspected and manually refined in Coot ( 44 ) and validated using MolProbity ( 45 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [PyMOL]

### Bacterial SEAL domains undergo autoproteolysis and function in regulated intramembrane proteolysis. (PNAS 2023)

- DOI: 10.1073/pnas.2310862120 | PMCID: PMC10556640 | PMID: 37756332
- Evidence: Model building was performed in Coot ( 57 ) and refinement was performed using Phenix.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot] -> stage not stated [AlphaFold, ColabFold, PHENIX v1.20.1]

### Specific inhibition of an anticancer target, polo-like kinase 1, by allosterically dismantling its mechanism of substrate recognition. (PNAS 2023)

- DOI: 10.1073/pnas.2305037120 | PMCID: PMC10629583 | PMID: 37603740
- Evidence: Structure refinement (1.65 Å resolution) was carried out with phenix.refine in the Phenix suite ( 67 ) and manual fitting in Coot ( 68 ).
- Full pipeline: normalisation [CCP4] -> simulation/modelling [GROMACS v2022.3, RDKit, VMD v1.9.4] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL, VMD v1.9.4] -> stage not stated [AlphaFold]

### Structural insights into the interaction of three Y-shaped ligands with PI3Kα. (PNAS 2023)

- DOI: 10.1073/pnas.2304071120 | PMCID: PMC10450665 | PMID: 37585458
- Version used: **0.9.4.1**
- Evidence: The models were docked into the cryo-EM density maps using Chimera v1.16, followed by iterative manual adjustment and rebuilding in Coot (v0.9.4.1) ( 46 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot v0.9.4.1] -> visualisation [ChimeraX v1.0, PyMOL v2.1, UCSF Chimera v1.13.1] -> stage not stated [CTFFIND v1.06, PHENIX v1.18.2, RELION]

### The structure of <i>Plasmodium falciparum</i> multidrug resistance protein 1 reveals an N-terminal regulatory domain. (PNAS 2023)

- DOI: 10.1073/pnas.2219905120 | PMCID: PMC10410737 | PMID: 37527341
- Evidence: This model was mutated, manually adjusted, and rebuilt in Coot ( 56 ) and refined against the cryo-EM map using phenix.real_space_refine in PHENIX ( 57 ).
- Full pipeline: registration [MotionCor2, RELION v3.0] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [UCSF Chimera]

### Efficient tagging of endogenous proteins in human cell lines for structural studies by single-particle cryo-EM. (PNAS 2023)

- DOI: 10.1073/pnas.2302471120 | PMCID: PMC10401002 | PMID: 37487103
- Evidence: Final GAPDH models were validated in Coot and by using Molprobity ( 79 ).
- Full pipeline: structure determination [PHENIX] -> machine learning [Cellpose] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [CTFFIND, Coot, ImageJ, MotionCor2, RELION, Topaz]

### ToxR activates the <i>Vibrio cholerae</i> virulence genes by tethering DNA to the membrane through versatile binding to multiple sites. (PNAS 2023)

- DOI: 10.1073/pnas.2304378120 | PMCID: PMC10629549 | PMID: 37428913
- Evidence: Atomic models were traced in Coot ( 25 ) and refined using REFMAC5 ( 26 ) and Phenix ( 27 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### The evolution of archaeal flagellar filaments. (PNAS 2023)

- DOI: 10.1073/pnas.2304256120 | PMCID: PMC10334743 | PMID: 37399404
- Evidence: These initial models were then subject to refinement in Coot ( 66 ) and using Phenix real-space refinement ( 67 ).
- Full pipeline: alignment/mapping [UCSF Chimera] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, EMAN2]

### Dual factors required for cytochrome-P450-mediated hydrocarbon ring contraction in bacterial gibberellin phytohormone biosynthesis. (PNAS 2023)

- DOI: 10.1073/pnas.2221549120 | PMCID: PMC10293830 | PMID: 37339230
- Evidence: ( A ) The structures were overlaid in Coot and visualized as cartoon models in PyMol.
- Full pipeline: visualisation [Coot, PyMOL] -> stage not stated [CCP4, PHENIX]

### 30S subunit recognition and G1405 modification by the aminoglycoside-resistance 16S ribosomal RNA methyltransferase RmtC. (PNAS 2023)

- DOI: 10.1073/pnas.2304128120 | PMCID: PMC10288597 | PMID: 37307464
- Evidence: Additional model building was conducted in Coot ( 45 ), with the previously solved RmtC–SAH structure guiding rotamer orientation for areas with poor density.
- Full pipeline: registration [CTFFIND] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, RELION v3.1, UCSF Chimera]

### A specialized integrin-binding motif enables proTGF-β2 activation by integrin αVβ6 but not αVβ8. (PNAS 2023)

- DOI: 10.1073/pnas.2304874120 | PMCID: PMC10268255 | PMID: 37279271
- Evidence: Autobuilding was performed using Phenix followed by iterative rounds of model building in Coot and refinement in Phenix ( 63 – 65 ).
- Full pipeline: alignment/mapping [MAFFT] -> normalisation [CCP4] -> structure determination [Coot, PHENIX]

### Molecular mechanism of fatty acid activation of FFAR1. (PNAS 2023)

- DOI: 10.1073/pnas.2219569120 | PMCID: PMC10235965 | PMID: 37216523
- Version used: **0.9.4.1**
- Evidence: The PDB models were first docked into the cryo-EM density map in Coot v.
- Full pipeline: normalisation [MotionCor2] -> registration [MotionCor2] -> simulation/modelling [NAMD v2.14] -> structure determination [Coot v0.9.4.1, PHENIX v1.19.2] -> stage not stated [R v3.50, RELION v3.1, UCSF Chimera v1.3]

### Structural insights into the transcription activation mechanism of the global regulator GlnR from actinobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2300282120 | PMCID: PMC10235972 | PMID: 37216560
- Evidence: The model of Sae GlnR-DBD complexed with DNA was built in Coot ( 56 ) and refined in Phenix ( 57 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [PyMOL, RELION v3.1]

### Mechanistic insights into the regulation of cell wall hydrolysis by FtsEX and EnvC at the bacterial division site. (PNAS 2023)

- DOI: 10.1073/pnas.2301897120 | PMCID: PMC10214136 | PMID: 37186861
- Evidence: These models were rigid-body fitted to our cryo-EM maps in the University of California, San Francisco (UCSF) Chimera ( 55 ), manually rebuilt in Coot ( 56 ), and refined using real space refinement in Phenix ( 57 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold]

### Structure of the human respiratory complex II. (PNAS 2023)

- DOI: 10.1073/pnas.2216713120 | PMCID: PMC10161127 | PMID: 37098072
- Evidence: To start model building, the predicted domains of four subunits were docked into the EM density map by using Chimera ( 47 ), followed by manual adjustment of main chains and side chains in Coot ( 48 ) and real space refinement in PHENIX ( 49 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold]

### In situ architecture and membrane fusion of SARS-CoV-2 Delta variant. (PNAS 2023)

- DOI: 10.1073/pnas.2213332120 | PMCID: PMC10160983 | PMID: 37094167
- Evidence: The two separate models were merged and manually adjusted in Coot.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD, PHENIX] -> stage not stated [Coot, MotionCor2, RELION, ilastik]

### Structural insights into HIV-1 polyanion-dependent capsid lattice formation revealed by single particle cryo-EM. (PNAS 2023)

- DOI: 10.1073/pnas.2220545120 | PMCID: PMC10160977 | PMID: 37094124
- Evidence: The model was adjusted using the ISOLDE UCSF ChimeraX plugin ( 65 , 66 ), followed by iterative rounds of manual adjustments in Coot ( 67 ) and Real Space Refinements in Phenix ( 64 ).
- Full pipeline: registration [RELION v4.0] -> structure determination [ChimeraX, Coot, PHENIX, UCSF Chimera]

### Interdigitated immunoglobulin arrays form the hyperstable surface layer of the extremophilic bacterium &lt;i&gt;Deinococcus radiodurans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2215808120 | PMCID: PMC10120038 | PMID: 37043530
- Evidence: The atomic model was then placed into the hexameric map as six copies and subjected to several rounds of refinement using refmac5 ( 67 ) inside the Collaborative Computational Project for electron cryo-microscopy (CCP-EM) software suite ( 68 ) and PHENIX ( 69 ), followed by manually rebuilding in Coot ( 66 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold v2.2.0, ChimeraX, MotionCor2, RELION]

### Structural basis for severe pain caused by mutations in the S4-S5 linkers of voltage-gated sodium channel Na<sub>V</sub>1.7. (PNAS 2023)

- DOI: 10.1073/pnas.2219624120 | PMCID: PMC10083536 | PMID: 36996107
- Evidence: Cryo-EM structure of human Na V 1.7 (PDB: 7W9K) was used for modeling in Coot ( 51 ).
- Full pipeline: structure determination [CCP4, PHENIX, REFMAC] -> stage not stated [Coot]

### A general mechanism for transcription bubble nucleation in bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2220874120 | PMCID: PMC10083551 | PMID: 36972428
- Evidence: The model was manually fit into the cryo-EM density maps using ChimeraX ( 41 ) and modified in Coot ( 42 ) followed by real-space refined using PHENIX ( 39 ).
- Full pipeline: quantification [ImageJ] -> normalisation [MotionCor2] -> differential/statistical testing [RELION v3.1] -> structure determination [ChimeraX, Coot, RELION v3.1] -> stage not stated [HMMER, PHENIX]

### Structure of mycobacterial respiratory complex I. (PNAS 2023)

- DOI: 10.1073/pnas.2214949120 | PMCID: PMC10068793 | PMID: 36952383
- Version used: **0.9.6**
- Evidence: Fitting of AcPIM 2 in the cryoEM density was done in Coot v0.9.6 as with fitting of other ligands.
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [RELION] -> structure determination [PHENIX v1.19.2] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, Coot v0.9.6]

### Structure-based design of a SARS-CoV-2 Omicron-specific inhibitor. (PNAS 2023)

- DOI: 10.1073/pnas.2300360120 | PMCID: PMC10068829 | PMID: 36940324
- Evidence: The model near the glycine insertion was first built in Coot ( 29 ) and then refined by an automated structure refinement protocol with Rosetta ( 30 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, MotionCor2, PyMOL, RELION, UCSF Chimera]

### Cryo-EM structure of the four-subunit <i>Rhodobacter sphaeroides</i> cytochrome <i>bc</i><sub>1</sub> complex in styrene maleic acid nanodiscs. (PNAS 2023)

- DOI: 10.1073/pnas.2217922120 | PMCID: PMC10041115 | PMID: 36913593
- Version used: **0.9.6**
- Evidence: The model was docked into the map using the “Fit in map” tool in ChimeraX 1.3 ( 90 ) and manually refined in Coot v0.9.6 ( 91 ).
- Full pipeline: structure determination [Coot v0.9.6, PHENIX v1.19.2] -> stage not stated [AlphaFold, ChimeraX v1.3, RELION v3.1]

### Structures of brain-derived 42-residue amyloid-β fibril polymorphs with unusual molecular conformations and intermolecular interactions. (PNAS 2023)

- DOI: 10.1073/pnas.2218831120 | PMCID: PMC10089215 | PMID: 36893281
- Evidence: 2 C was created in Coot ( 25 ) and refined by simulated annealing in Xplor-NIH ( 26 ), resulting in a bundle of structures from independent annealing calculations with a rmsd of 1.2 Å for backbone atom positions and 1.7 Å for all heavy atom positions in residues 12 to 42 ( SI Appendix , Fig.
- Full pipeline: simulation/modelling [Coot, NAMD, VMD] -> structure determination [Coot, RELION]

### A macrocyclic peptide inhibitor traps MRP1 in a catalytically incompetent conformation. (PNAS 2023)

- DOI: 10.1073/pnas.2220012120 | PMCID: PMC10089224 | PMID: 36893260
- Evidence: The structure was manually fit to the bMRP1 + CPI1 working map in Coot, and real-space refined against the working map in the PHENIX suite.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX, REFMAC, UCSF Chimera] -> stage not stated [PyMOL, RELION]

### Structure of the Wnt-Frizzled-LRP6 initiation complex reveals the basis for coreceptor discrimination. (PNAS 2023)

- DOI: 10.1073/pnas.2218238120 | PMCID: PMC10089208 | PMID: 36893265
- Evidence: The final model was prepared by iterative cycles of rebuilding and interactive refinement in Coot ( 52 ) and reciprocal space refinement in Buster ( 60 ) and Phenix ( 53 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ChimeraX]

### Cryo-EM structure of the human chemerin receptor 1-Gi protein complex bound to the C-terminal nonapeptide of chemerin. (PNAS 2023)

- DOI: 10.1073/pnas.2214324120 | PMCID: PMC10089180 | PMID: 36881626
- Evidence: The models were docked into the EM density map using UCSF Chimera version 1.12, followed by iterative manual building in Coot-0.9.2 and refinement in Phenix-1.18.2.
- Full pipeline: structure determination [Coot, PHENIX, UCSF Chimera v1.12] -> stage not stated [AlphaFold]

### Structure-guided approach to modulate small molecule binding to a promiscuous ligand-activated protein. (PNAS 2023)

- DOI: 10.1073/pnas.2217804120 | PMCID: PMC10013835 | PMID: 36848571
- Evidence: Iterative cycles of model building and refinement were performed in Coot ( 38 ) and Phenix ( 39 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [PHENIX]

### Structure of metallochaperone in complex with the cobalamin-binding domain of its target mutase provides insight into cofactor delivery. (PNAS 2023)

- DOI: 10.1073/pnas.2214085120 | PMCID: PMC9974510 | PMID: 36787360
- Evidence: Subsequent iterative rounds of model building and refinement were performed in Coot ( 45 ) and Phenix, respectively.
- Full pipeline: read trimming [PHENIX] -> structure determination [Coot] -> visualisation [PyMOL v2.3.3] -> stage not stated [CCP4]

### Structural basis of V-ATPase V<sub>O</sub> region assembly by Vma12p, 21p, and 22p. (PNAS 2023)

- DOI: 10.1073/pnas.2217181120 | PMCID: PMC9963935 | PMID: 36724250
- Evidence: Atomic models were constructed by manual model building in Coot ( 56 ), followed by refinement with ISOLDE ( 57 ) and real space refinement with Phenix ( 58 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold]

### Structure and supramolecular organization of the canine distemper virus attachment glycoprotein. (PNAS 2023)

- DOI: 10.1073/pnas.2208866120 | PMCID: PMC9963377 | PMID: 36716368
- Evidence: The neck was completely built de novo in Coot ( 70 ).
- Full pipeline: registration [MotionCor2 v1.4.0] -> simulation/modelling [VMD] -> structure determination [PHENIX v1.19] -> visualisation [VMD] -> stage not stated [ChimeraX v1.3, Coot, PyMOL v2.5.2, RELION v3.1.1, UCSF Chimera v1.12]

### Destabilizing NF1 variants act in a dominant negative manner through neurofibromin dimerization. (PNAS 2023)

- DOI: 10.1073/pnas.2208960120 | PMCID: PMC9945959 | PMID: 36689660
- Evidence: The core of the NF1 dimer was completely manually modeled in Coot ( 35 ) and then compared with the AlphaFold2 ( 36 ) predictions of separate domains.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, Coot, MotionCor2, RELION]

### Characterization of a glycan-binding complex of minor pilins completes the analysis of <i>Streptococcus sanguinis</i> type 4 pili subunits. (PNAS 2023)

- DOI: 10.1073/pnas.2216237120 | PMCID: PMC9934059 | PMID: 36626560
- Evidence: Initial structure was produced using CRANK2 ( 54 ) and autobuild, with some manual building in Coot ( 55 ).
- Full pipeline: stage not stated [AlphaFold v2.0, Coot]

### Structural basis for regulation of SOS response in bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2217493120 | PMCID: PMC9926225 | PMID: 36598938
- Evidence: The cryo-EM structure of RecA filaments (PDB 7JY8) ( 27 ) and the NMR structure of DinI (PDB 1GHH) ( 43 ) were fitted into the cryo-EM density map using Chimera ( 44 ) and were adjusted in Coot ( 45 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [Coot, PHENIX] -> stage not stated [ImageJ]

### Differential dynamics and direct interaction of bound ligands with lipids in multidrug transporter ABCG2. (PNAS 2023)

- DOI: 10.1073/pnas.2213437120 | PMCID: PMC9910490 | PMID: 36580587
- Version used: **0.9**
- Evidence: Model building was performed in Coot 0.9 ( 47 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [CTFFIND, Coot v0.9, MotionCor2, PHENIX, VMD]

### SUMO enhances unfolding of SUMO-polyubiquitin-modified substrates by the Ufd1/Npl4/Cdc48 complex. (PNAS 2023)

- DOI: 10.1073/pnas.2213703120 | PMCID: PMC9910466 | PMID: 36574706
- Evidence: Atomic models were docked into maps and manually rebuilt in Coot ( 61 ).
- Full pipeline: structure determination [PHENIX, Python] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, Coot, MotionCor2, RELION v3.0]

### The C-terminal activating domain promotes pannexin 1 channel opening. (PNAS 2024)

- DOI: 10.1073/pnas.2411898121 | PMCID: PMC11665872 | PMID: 39671183
- Evidence: The existing frog Panx1 structure [PDB:6VD7 ( 27 , 52 )] was fit into the cryo-EM density maps for model building in Coot ( 53 ).
- Full pipeline: registration [RELION v4.0] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Structural basis of the allosteric regulation of cyanobacterial glucose-6-phosphate dehydrogenase by the redox sensor OpcA. (PNAS 2024)

- DOI: 10.1073/pnas.2411604121 | PMCID: PMC11648896 | PMID: 39642196
- Evidence: The models of G6PDG and OpcA underwent manual adjustments and refinements in Coot ( 30 ).
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [ImageJ]

### Structure of yeast RAVE bound to a partial V&lt;sub&gt;1&lt;/sub&gt; complex. (PNAS 2024)

- DOI: 10.1073/pnas.2414511121 | PMCID: PMC11648922 | PMID: 39625975
- Evidence: These models were adjusted manually in Coot ( 65 ), followed by refinement with ISOLDE ( 66 ), and real space refinement with PHENIX ( 67 ).
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, UCSF Chimera]

### Structural basis of chiral wrap and T-segment capture by &lt;i&gt;Escherichia coli&lt;/i&gt; DNA gyrase. (PNAS 2024)

- DOI: 10.1073/pnas.2407398121 | PMCID: PMC11626157 | PMID: 39589884
- Evidence: The model for the cleavage-reunion core was manually built in Coot( 77 ) based on the previously available high-resolution structure [PDB: 7Z9C ( 8 )].
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [Coot, Topaz]

### Molecular basis for chemokine recognition and activation of XCR1. (PNAS 2024)

- DOI: 10.1073/pnas.2405732121 | PMCID: PMC11621518 | PMID: 39565315
- Evidence: The structure of XCL1 CC3–XCR1–G i was subsequently generating using iterative manual building and adjustment in Coot ( 79 ), followed by real-space refinement in Phenix ( 80 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ColabFold, GROMACS, PyMOL v3.0.3]

### Calcineurin-fusion facilitates cryo-EM structure determination of a Family A GPCR. (PNAS 2024)

- DOI: 10.1073/pnas.2414544121 | PMCID: PMC11621825 | PMID: 39565314
- Evidence: The models were docked into the EM density map using UCSF Chimera ( 31 ), followed by iterative manual building in Coot ( 32 ) and refinement in Phenix ( 33 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, UCSF Chimera] -> stage not stated [RELION]

### Inhibition mechanism of potential antituberculosis compound lansoprazole sulfide. (PNAS 2024)

- DOI: 10.1073/pnas.2412780121 | PMCID: PMC11588064 | PMID: 39531492
- Evidence: Initial models were built using a previous structure [PDB: 8OVD ( 17 )] fitted into the maps and manually refined in Coot ( 36 ).
- Full pipeline: simulation/modelling [NAMD v2.12, VMD] -> structure determination [Coot, PHENIX]

### A conserved mechanism couples cytosolic domain movements to pore gating in the TRPM2 channel. (PNAS 2024)

- DOI: 10.1073/pnas.2415548121 | PMCID: PMC11573590 | PMID: 39514307
- Evidence: Real-space refinement was carried out using PHENIX, and manual adjustment was done in Coot.
- Full pipeline: structure determination [Coot, PHENIX]

### A conserved juxtamembrane motif in plant NFR5 receptors is essential for root nodule symbiosis. (PNAS 2024)

- DOI: 10.1073/pnas.2405671121 | PMCID: PMC11572979 | PMID: 39495923
- Evidence: Data refinement was performed using phenix.refine, and the atomic model was built in Coot ( 53 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [PHENIX]

### 2.6-Å resolution cryo-EM structure of a class Ia ribonucleotide reductase trapped with mechanism-based inhibitor N&lt;sub&gt;3&lt;/sub&gt;CDP. (PNAS 2024)

- DOI: 10.1073/pnas.2417157121 | PMCID: PMC11551348 | PMID: 39475643
- Evidence: Water molecules were added by comparison to known crystal structures of the individual α2 ( 24 – 28 ) and β2 ( 27 , 29 , 30 ) subunits ( SI Appendix , Tables S3–S6 ) and by using a combination of the “Find Waters” function in Coot ( 31 ) ( SI Appendix , Table S7 ) and manual inspection ( SI Appendix , Table S8 ).
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [Coot, RELION]

### Biochemical analysis of EGFR exon20 insertion variants insASV and insSVD and their inhibitor sensitivity. (PNAS 2024)

- DOI: 10.1073/pnas.2417144121 | PMCID: PMC11551396 | PMID: 39471218
- Evidence: Structures were phased via molecular replacement and refined using Phenix with iterative rounds of manual model building in Coot ( 62 , 63 ).
- Full pipeline: structure determination [Coot, PHENIX]

### Structure and function of &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; EfpA as a lipid transporter and its inhibition by BRD-8000.3. (PNAS 2024)

- DOI: 10.1073/pnas.2412653121 | PMCID: PMC11536138 | PMID: 39441632
- Evidence: Residues considered to be Ramachandran outliers with poor rotamers were fixed in Coot.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4, Coot, UCSF Chimera]

### Structural basis for adhesin secretion by the outer-membrane usher in type 1 pili. (PNAS 2024)

- DOI: 10.1073/pnas.2410594121 | PMCID: PMC11459180 | PMID: 39316053
- Version used: **0.9.8.7**
- Evidence: Coordinates of the FimD usher, FimC chaperone, FimF tip adapter, and FimH adhesin from PDB 3RFZ and PDB 3JWN were docked, rigid-body fit, and subjected to model building in Coot 0.9.8.7 ( 29 ).
- Full pipeline: read trimming [Coot v0.9.8.7] -> structure determination [PHENIX v1.20.1] -> stage not stated [ChimeraX v1.5]

### Cryo-EM structures of a mycobacterial ABC transporter that mediates rifampicin resistance. (PNAS 2024)

- DOI: 10.1073/pnas.2403421121 | PMCID: PMC11406275 | PMID: 39226350
- Evidence: The structures were manually adjusted in Coot followed by real-space-refinement using PHENIX ( 58 ) with reference to secondary structure and geometry restraints to prevent over-fitting.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, GROMACS v2022.2, PyMOL, UCSF Chimera]

### Structural basis for DNA recognition by a viral genome-packaging machine. (PNAS 2024)

- DOI: 10.1073/pnas.2406138121 | PMCID: PMC11331095 | PMID: 39116131
- Evidence: Atomic model building in the final map was performed in Coot ( 46 ) using crystal structure of HK97 small terminase (pdb 6z6e) as the initial model.
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, Coot, RELION v3.1.2, Topaz]

### Structures of trehalose-6-phosphate synthase, Tps1, from the fungal pathogen &lt;i&gt;Cryptococcus neoformans&lt;/i&gt;: A target for antifungals. (PNAS 2024)

- DOI: 10.1073/pnas.2314087121 | PMCID: PMC11317593 | PMID: 39083421
- Evidence: Coordinates were then fitted manually in Coot ( 76 ) followed by iterative refinement using Phenix ( 77 ) real space refinement to improve the quality of the models.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [UCSF Chimera v1.14]

### Structure of the flotillin complex in a native membrane environment. (PNAS 2024)

- DOI: 10.1073/pnas.2409334121 | PMCID: PMC11260169 | PMID: 38985763
- Evidence: The four Flotillin dimer positions in the map were built manually in Coot ( 63 ) and the other Flotillin subunits were adjusted in Coot by applying noncrystallographic symmetry, using the four Flotillin dimers as master chains.
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [AlphaFold, ChimeraX, PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [ColabFold, Coot]

### Structural insights into the regulation of RyR1 by S100A1. (PNAS 2024)

- DOI: 10.1073/pnas.2400497121 | PMCID: PMC11228480 | PMID: 38917010
- Evidence: Atomic models were manually built in Coot ( 62 ) starting with a cryo-EM structural model of RyR1 (PDB: 7TZC), while models of S100A1 in the apo-conformation and Ca 2+ -bound conformation were obtained from NMR structures (PDB: 2L0P and PDB: 2K2F, respectively).
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [ChimeraX, PHENIX] -> stage not stated [Coot]

### Structural dynamics at cytosolic interprotomer interfaces control gating of a mammalian TRPM5 channel. (PNAS 2024)

- DOI: 10.1073/pnas.2403333121 | PMCID: PMC11228501 | PMID: 38923985
- Version used: **0.98**
- Evidence: All models were built in Coot 0.98 ( 48 ).
- Full pipeline: structure determination [PHENIX v1.20] -> stage not stated [Coot v0.98, UCSF Chimera]

### Peripheral positions encode transport specificity in the small multidrug resistance exporters. (PNAS 2024)

- DOI: 10.1073/pnas.2403273121 | PMCID: PMC11194549 | PMID: 38865266
- Evidence: Processed data were subjected to anisotropic truncation using Staraniso ( 46 ), and phases were calculated by molecular replacement with Phaser ( 47 ), with iterative rounds of refinement in Phenix ( 48 ) and model building in Coot ( 49 ).
- Full pipeline: structure determination [Coot, PHENIX]

### Allosteric activation of VCP, an AAA unfoldase, by small molecule mimicry. (PNAS 2024)

- DOI: 10.1073/pnas.2316892121 | PMCID: PMC11181084 | PMID: 38833472
- Evidence: For each symmetric structure masked on the D2 domains (VCP-VAA1-apo C6 hexamer, VCP-VAA1-apo D6 dodecamer, VCP-VAA1-ADP C6 hexamer), real space sphere refinement in Coot with torsion, planar peptide, trans peptide, and Ramachandran restraints enforced was used to adjust side chains for a single chain.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [MotionCor2, RELION]

### Bispecific antibodies targeting two glycoproteins on SFTSV exhibit synergistic neutralization and protection in a mouse model. (PNAS 2024)

- DOI: 10.1073/pnas.2400163121 | PMCID: PMC11181109 | PMID: 38830098
- Version used: **0.9.3**
- Evidence: The structures of the SFTSV Gn–SF5 (PDB 8WSP) and Gc–SF83 (PDB 8WSU) proteins were rigidly docked into the density map using Chimera ( 35 ); mutation and manual adjustment were performed with Coot v.0.9.3 ( 36 ).
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, MUSCLE v3.8.31, MotionCor2] -> variant calling [SAMtools v1.9] -> structure determination [Coot v0.9.3, PHENIX] -> machine learning [Topaz] -> visualisation [PyMOL v2.0] -> stage not stated [fastp]

### Principles of peptide selection by the transporter associated with antigen processing. (PNAS 2024)

- DOI: 10.1073/pnas.2320879121 | PMCID: PMC11161800 | PMID: 38805290
- Evidence: The models were then iteratively edited and refined in Coot ( 68 ), ISOLDE ( 69 ), and PHENIX ( 70 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, RELION]

### Cryo-EM structures elucidate the multiligand receptor nature of megalin. (PNAS 2024)

- DOI: 10.1073/pnas.2318859121 | PMCID: PMC11145282 | PMID: 38771880
- Evidence: The models were manually rebuilt in Coot ( 53 ), fitted to the density by ISOLDE ( 54 ), implemented in chimeraX ( 55 ), and refined to each multibody-refined map by using phenix.real_space_refine ( 56 ).
- Full pipeline: registration [Topaz] -> structure determination [AlphaFold, Coot] -> visualisation [ChimeraX] -> stage not stated [RELION v3.1]

### Structure and mechanism of the human CTDNEP1-NEP1R1 membrane protein phosphatase complex necessary to maintain ER membrane morphology. (PNAS 2024)

- DOI: 10.1073/pnas.2321167121 | PMCID: PMC11145253 | PMID: 38776370
- Evidence: Additional model building in Coot ( 51 ) and refinement in Phenix produced the final apo model of the CTDNEP1–NEP1R1 fusion ( Table 1 , PDB code: 8UJL).
- Full pipeline: structure determination [Coot] -> stage not stated [AlphaFold, ImageJ, PHENIX]

### c-di-AMP determines the hierarchical organization of bacterial RCK proteins. (PNAS 2024)

- DOI: 10.1073/pnas.2318666121 | PMCID: PMC11067040 | PMID: 38652747
- Evidence: After the extension of the M2D1 helix in Coot ( 56 ), the model underwent 3 cycles of conservative refinement in Phenix ( 57 ).
- Full pipeline: structure determination [Coot, PHENIX]

### Identification of the potassium-binding site in serotonin transporter. (PNAS 2024)

- DOI: 10.1073/pnas.2319384121 | PMCID: PMC11067047 | PMID: 38652746
- Version used: **0.8.9.3**
- Evidence: The inward-open conformation structure [PDB identifier 6DZZ ( 8 ) was truncated at residues 78-85 with Coot v 0.8.9.3-pre ( 47 ) due to inclusive densities in the EM map (EMD-8943)], while the outward-occluded conformation was based on a previously published hybrid model ( 24 ).
- Full pipeline: simulation/modelling [GROMACS v2018.8, NAMD v2.13] -> stage not stated [Coot v0.8.9.3, VMD v1.9.3]

### Dual function of LapB (YciM) in regulating <i>Escherichia coli</i> lipopolysaccharide synthesis. (PNAS 2024)

- DOI: 10.1073/pnas.2321510121 | PMCID: PMC11046580 | PMID: 38635633
- Evidence: The model was manually adjusted in Coot ( 47 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, UCSF Chimera]

### Tight-packing of large pilin subunits provides distinct structural and mechanical properties for the <i>Myxococcus xanthus</i> type IVa pilus. (PNAS 2024)

- DOI: 10.1073/pnas.2321989121 | PMCID: PMC11046646 | PMID: 38625941
- Evidence: An initial homologous model generated via SWISS-MODEL was docked into the cryo-EM map by rigid body fitting in Chimera ( 70 ) and manually edited the model in Coot ( 71 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, Coot]

### &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; telomere-binding proteins TEBP-1 and TEBP-2 adapt the Myb module to dimerize and bind telomeric DNA. (PNAS 2024)

- DOI: 10.1073/pnas.2316651121 | PMCID: PMC11032478 | PMID: 38588418
- Evidence: Structural refinement was performed in PHENIX to generate 2Fo-Fc maps, using which the DNA was built in Coot ( 39 ).
- Full pipeline: alignment/mapping [Clustal Omega, ColabFold] -> structure determination [Coot] -> stage not stated [AlphaFold, PHENIX]

### Substrate recruitment via eIF2γ enhances catalytic efficiency of a holophosphatase that terminates the integrated stress response. (PNAS 2024)

- DOI: 10.1073/pnas.2320013121 | PMCID: PMC10998612 | PMID: 38547060
- Version used: **0.9.8.7**
- Evidence: PPP1R15A 426-434 was manually built to the difference map in Coot (v.0.9.8.7) ( 36 ) with reference to the AFM predicted model.
- Full pipeline: quantification [ImageJ] -> structure determination [GROMACS] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, ChimeraX v1.6.1, Coot v0.9.8.7, PHENIX v1.20.1, PyMOL v1.3]

### Allosteric regulation of nitrate transporter NRT via the signaling protein PII. (PNAS 2024)

- DOI: 10.1073/pnas.2318320121 | PMCID: PMC10945777 | PMID: 38457518
- Evidence: The final sharpened map of NrtBCD-ATP with a B-factor of −168.6 Å 2 was used for model building in Coot ( 55 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, MotionCor2, PyMOL, RELION v3.1]

### Phosphorylation of the alpha-I motif in SYMRK drives root nodule organogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2311522121 | PMCID: PMC10895371 | PMID: 38363863
- Evidence: The structure of the three molecules in the asymmetric unit was built in Coot ( 29 ) and coordinates and B-factors were refined in phenix.refine ( 27 ).
- Full pipeline: structure determination [Coot] -> stage not stated [PyMOL v2.4.1]

### The structure of the <i>Caenorhabditis elegans</i> TMC-2 complex suggests roles of lipid-mediated subunit contacts in mechanosensory transduction. (PNAS 2024)

- DOI: 10.1073/pnas.2314096121 | PMCID: PMC10895266 | PMID: 38354260
- Evidence: The transmembrane helices of TMC-2 (TM1-9, excluding TM10), predicted by Alphafold2 ( 64 ) as a template, were fit into the map with rigid body fitting and de novo model building in Coot ( 65 ) and Isolde ( 66 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, Coot, UCSF Chimera]

### Filament structure and subcellular organization of the bacterial intermediate filament-like protein crescentin. (PNAS 2024)

- DOI: 10.1073/pnas.2309984121 | PMCID: PMC10873595 | PMID: 38324567
- Evidence: These starting atomic models were fitted into the cryo-EM map in Chimera ( 62 ), followed by manual model re-building in Coot ( 63 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [IMOD, PHENIX] -> machine learning [Topaz] -> stage not stated [Coot, ImageJ, MotionCor2, RELION v3.1]

### Structure of <i>Escherichia coli</i> exonuclease VII. (PNAS 2024)

- DOI: 10.1073/pnas.2319644121 | PMCID: PMC10835039 | PMID: 38271335
- Version used: **0.9.6**
- Evidence: The fitted model was then used as an initial model for building in Coot (v.0.9.6) ( 38 ).
- Full pipeline: structure determination [AlphaFold, ChimeraX v1.4, PHENIX v1.20.1] -> stage not stated [Coot v0.9.6, UCSF Chimera v1.15]

### The structure of B-ARR reveals the molecular basis of transcriptional activation by cytokinin. (PNAS 2024)

- DOI: 10.1073/pnas.2319335121 | PMCID: PMC10801921 | PMID: 38198526
- Evidence: All of the models were manually built in Coot ( 61 ) and were refined by iterative rounds of manual adjustment with Coot and refinement with Phenix ( 62 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [BLAST]

### Development of 2nd generation aminomethyl spectinomycins that overcome native efflux in <i>Mycobacterium</i> abscessus. (PNAS 2024)

- DOI: 10.1073/pnas.2314101120 | PMCID: PMC10786304 | PMID: 38165935
- Version used: **0.8.2**
- Evidence: Structural models were built in Coot (version 0.8.2).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt, FastQC, MultiQC] -> alignment/mapping [Bowtie2, featureCounts] -> variant calling [VarScan] -> differential/statistical testing [DESeq2, R] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot v0.8.2]

### Molecular mechanism of substrate transport by human peroxisomal ABCD3. (PNAS 2025)

- DOI: 10.1073/pnas.2513928122 | PMCID: PMC12772208 | PMID: 41428872
- Evidence: ABCD3 apo model was used as a starting point for ABCD3-phytanoyl-CoA and was further fitted and refined in Coot and PHENIX, respectively.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX]

### Cryo-EM structure of the Rift Valley fever virus envelope protein in complex with a potent neutralization antibody. (PNAS 2025)

- DOI: 10.1073/pnas.2514862122 | PMCID: PMC12745785 | PMID: 41401007
- Evidence: The models were improved by iterative rounds of manual rebuilding in Coot ( 42 ) and subsequent refinements using real-space refinement in Phenix ( 43 ).
- Full pipeline: structure determination [Coot, PHENIX, RELION] -> stage not stated [AlphaFold, ChimeraX]

### Structural basis and evolutionary pathways of glycerol-1-phosphate transport in marine bacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2524546122 | PMCID: PMC12718374 | PMID: 41364767
- Evidence: Several rounds of refinement of all structures were carried out in Coot ( 40 ) and Phenix ( 41 ) using default parameters.
- Full pipeline: quantification [HMMER] -> normalisation [HMMER] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4]

### An IMPDH2 variant associated with neurodevelopmental disorder disrupts purine biosynthesis and somite organization. (PNAS 2025)

- DOI: 10.1073/pnas.2511727122 | PMCID: PMC12704788 | PMID: 41343675
- Version used: **0.9.8.8**
- Evidence: The output was manually adjusted residue-by-residue in Coot v0.9.8.8 ( 52 ) and with semiautomated fitting in Isolde v1.6.0 ( 53 ).
- Full pipeline: simulation/modelling [ChimeraX v1.6.1, PHENIX v1.20.1] -> structure determination [ChimeraX v1.6.1, PHENIX v1.20.1] -> stage not stated [Coot v0.9.8.8]

### RAD51AP1 is a versatile RAD51 modulator. (PNAS 2025)

- DOI: 10.1073/pnas.2514728122 | PMCID: PMC12704761 | PMID: 41337480
- Evidence: The models were partially manually rebuilt in Coot ( 58 ).
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2]

### Small siphophage binding to an open state of the LptDE outer membrane lipopolysaccharide translocon. (PNAS 2025)

- DOI: 10.1073/pnas.2516650122 | PMCID: PMC12685063 | PMID: 41296721
- Evidence: Models were then manually rebuilt and corrected in Coot ( 53 ).
- Full pipeline: alignment/mapping [PyMOL] -> quantification [ImageJ] -> simulation/modelling [GROMACS] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [Coot, MDAnalysis, MDTraj]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Evidence: The model was then subjected to iterative rounds of manual adjustment in Coot ( 65 ) and real-space refinement in Phenix ( 66 ).
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### Structural basis for Lamassu-based antiviral immunity and its evolution from DNA repair machinery. (PNAS 2025)

- DOI: 10.1073/pnas.2519643122 | PMCID: PMC12663957 | PMID: 41252147
- Evidence: For the DNA-bound structure, the model building was based on the map generated using EM-ready, then validated against the raw map, further adjusted in Coot, and refined through additional cycles of real-space refinement in PHENIX using the raw map.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX v1.9, UCSF Chimera] -> stage not stated [AlphaFold]

### The mechanism of pathogenic α&lt;sub&gt;1&lt;/sub&gt;-antitrypsin aggregation in the human liver. (PNAS 2025)

- DOI: 10.1073/pnas.2507535122 | PMCID: PMC12646233 | PMID: 41231946
- Evidence: Rigid body fitting within density and stereochemical refinement of linker peptides was performed in Coot ( 58 ) and rigid body fitting and real-space correlation calculations in ChimeraX ( 56 ).
- Full pipeline: normalisation [PHENIX] -> registration [MotionCor2 v1.4, RELION v4.0] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX, PHENIX]

### Structure and encapsulation of carbonic anhydrase within the α-carboxysome. (PNAS 2025)

- DOI: 10.1073/pnas.2523723122 | PMCID: PMC12646314 | PMID: 41223214
- Evidence: The initial model was then manually examined and adjusted in Coot ( 76 ) to fit the density map.
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, Clustal Omega]

### Conformational regulation of two essential activators of bacterial cell elongation. (PNAS 2025)

- DOI: 10.1073/pnas.2514198122 | PMCID: PMC12625996 | PMID: 41183199
- Evidence: The coordinates were built manually in Coot ( 51 ), using starting models generated from a combination of AlphaFold2 predictions and the existing BRIL + anti-BRIL Fab structure ( 31 , 33 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, Coot]

### WrtF from &lt;i&gt;Rhizobium tropici&lt;/i&gt; CIAT 899 is a GT-A fold fucosyltransferase that binds its donor nonproductively. (PNAS 2025)

- DOI: 10.1073/pnas.2512460122 | PMCID: PMC12595478 | PMID: 41166418
- Evidence: After initial rebuilding using Autobuild ( 72 ) in Phenix, ligands were placed and iterative rounds of manual rebuilding in Coot ( 73 ) and refinement in Phenix.refine ( 72 ) were used to refine the structure.
- Full pipeline: structure determination [Coot] -> stage not stated [ColabFold, PHENIX]

### Asymmetric gating of a homopentameric ion channel GLIC revealed by cryo-EM. (PNAS 2025)

- DOI: 10.1073/pnas.2512811122 | PMCID: PMC12582304 | PMID: 41129221
- Version used: **0.9.8.7**
- Evidence: These models were first aligned to our density maps using UCSF ChimeraX and subsequently built manually in Coot (v0.9.8.7) ( 85 ).
- Full pipeline: alignment/mapping [Coot v0.9.8.7] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.9.8.7, PHENIX, RELION v4.0.1] -> stage not stated [ChimeraX]

### Structural and functional analysis of the &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; MmpS5L5 efflux pump presages increased bedaquiline resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2516660122 | PMCID: PMC12501195 | PMID: 40986343
- Version used: **0.9.8.93**
- Evidence: Each subunit was individually rigid-body-fitted into the density in Coot (v.0.9.8.93) ( 74 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION] -> structure determination [PHENIX v1.21.2] -> stage not stated [AlphaFold, ChimeraX, Coot v0.9.8.93]

### In situ structures of the &lt;i&gt;Legionella&lt;/i&gt; Dot/Icm T4SS identify the DotA-IcmX complex as the gatekeeper for effector translocation. (PNAS 2025)

- DOI: 10.1073/pnas.2516300122 | PMCID: PMC12501162 | PMID: 40986344
- Version used: **0.8.9.1**
- Evidence: Individual components were manually adjusted in Coot v0.8.9.1 ( 56 ) to optimize their fit within the map.
- Full pipeline: alignment/mapping [PHENIX v1.21] -> structure determination [CTFFIND, ChimeraX, PHENIX v1.21] -> stage not stated [AlphaFold, Coot v0.8.9.1, IMOD, RELION v3.1]

### De novo design of potent inhibitors of clostridial family toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2509329122 | PMCID: PMC12501149 | PMID: 40982695
- Evidence: Phenix ( 54 ) was used to trim the model to polyA, before further refinement in Coot and Isolde.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL, seaborn] -> stage not stated [AlphaFold, ChimeraX, Topaz]

### Structurally diverse viral inhibitors converge on a shared mechanism to stall the antigen transporter TAP. (PNAS 2025)

- DOI: 10.1073/pnas.2516676122 | PMCID: PMC12478189 | PMID: 40956880
- Evidence: The models were then docked into the density, iteratively edited and refined in Coot ( 71 ), ISOLDE ( 72 ), and PHENIX ( 73 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, RELION]

### Binding of &lt;i&gt;Fusobacterium nucleatum&lt;/i&gt; autotransporter adhesin CbpF to human CEACAM1 and CEACAM5: A Velcro model for bacterium adhesion. (PNAS 2025)

- DOI: 10.1073/pnas.2516574122 | PMCID: PMC12452904 | PMID: 40928870
- Version used: **0.9.8.92**
- Evidence: The model was then manually refined in Coot 0.9.8.92 ( 60 ). and autorefined using Phenix-1.20.1 real space refine program ( 61 ).The stereochemical quality of all models was assessed using MolProbity of Phenix.
- Full pipeline: structure determination [ChimeraX, Coot v0.9.8.92, PHENIX, PyMOL] -> visualisation [PyMOL] -> stage not stated [CCP4, MotionCor2]

### Mechanisms underlying allosteric modulation of antiseizure medication binding to synaptic vesicle protein 2A (SV2A). (PNAS 2025)

- DOI: 10.1073/pnas.2510239122 | PMCID: PMC12435242 | PMID: 40892927
- Evidence: SV2A (PDB: 8UO9) model was fit into cryo-EM density maps, which was manually modeled in Coot ( 53 , 54 ), iteratively real space refined in Phenix (version 1.20.1) ( 55 ), and validated by comparing the half maps and refined model.
- Full pipeline: differential/statistical testing [RELION v3.1] -> structure determination [Coot, PHENIX v1.20.1] -> stage not stated [AlphaFold]

### SHP2 genetic variants in NSML-associated RASopathies disrupt the PZR-IRX transcription factor signaling axis. (PNAS 2025)

- DOI: 10.1073/pnas.2503631122 | PMCID: PMC12415285 | PMID: 40854126
- Evidence: Manual building was then performed in Coot ( 57 ).
- Full pipeline: stage not stated [Coot, PHENIX]

### CryoEM structure of ALK2:BMP6 reveals distinct mechanism that allow ALK2 to interact with both BMP and activin ligands. (PNAS 2025)

- DOI: 10.1073/pnas.2502788122 | PMCID: PMC12415261 | PMID: 40854140
- Version used: **0.9.6**
- Evidence: Manual model building was conducted in Coot 0.9.6, and real space refinement of models was conducted using Phenix 1.21 ( 37 , 38 ).
- Full pipeline: structure determination [Coot v0.9.6, PHENIX v1.21] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### Mechanistic insights into the small-molecule inhibition of influenza A virus entry. (PNAS 2025)

- DOI: 10.1073/pnas.2503899122 | PMCID: PMC12377760 | PMID: 40802690
- Evidence: Model building was performed in Coot ( 44 ), followed by simulated annealing and real-space refinement in Phenix ( 45 ), and iterative manual fitting in Coot ( 44 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [Coot] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL]

### The bacterial ESCRT-III PspA rods thin lipid tubules and increase membrane curvature through helix α0 interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2506286122 | PMCID: PMC12358876 | PMID: 40758888
- Evidence: The auto-refined models were checked/adjusted manually in Coot ( 83 ) and ISOLDE ( 80 ) before a final cycle of auto-refinement with phenix.real_space_refine ( 81 ) (with NCS constraints and NCS refinement).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [ChimeraX]

### Cryo-EM structure and polar assembly of the PS2 S-layer of &lt;i&gt;Corynebacterium glutamicum&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2426928122 | PMCID: PMC12337289 | PMID: 40729392
- Evidence: Finally, we used EMready ( 62 ) to improve the interpretability of the map in those regions where resolution was lower and finally, we built the atomic model using a combination of ModelAngelo ( 63 ), AlphaFold2 ( 64 ) followed by manually rebuilding in Coot ( 65 ).
- Full pipeline: structure determination [ChimeraX, PHENIX] -> visualisation [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Coot]

### Structural basis of auxin binding and transport by <i>Arabidopsis thaliana</i> AUX1. (PNAS 2025)

- DOI: 10.1073/pnas.2513424122 | PMCID: PMC12337342 | PMID: 40720658
- Evidence: De novo model building was performed in Coot ( 48 – 50 ) using the 3.5 Å map of AUX1.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [OpenMM, VMD] -> structure determination [PHENIX] -> machine learning [OpenMM] -> visualisation [VMD] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, Coot]

### Structures of &lt;i&gt;Chaetomium thermophilum&lt;/i&gt; TOM complexes with bound preproteins. (PNAS 2025)

- DOI: 10.1073/pnas.2507279122 | PMCID: PMC12305020 | PMID: 40674418
- Evidence: Lipid molecules were added in Coot where appropriate, as defined by clear density ( 54 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2, RELION v3.0]

### Structural basis of the inhibition of TRPV1 by analgesic sesquiterpenes. (PNAS 2025)

- DOI: 10.1073/pnas.2506560122 | PMCID: PMC12305030 | PMID: 40663614
- Evidence: The model of hTRPV1 solved in the presence of AH was built in Coot ( 76 ), using the previously published apo-state structure of hTRPV1 (PDB ID: 8GF9) ( 45 ) as a guide.
- Full pipeline: simulation/modelling [NAMD v2.14] -> structure determination [PHENIX, Topaz] -> visualisation [ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [Coot]

### Microscopic and structural observations of actin filament capping and severing by cytochalasin D. (PNAS 2025)

- DOI: 10.1073/pnas.2502164122 | PMCID: PMC12304888 | PMID: 40658853
- Evidence: Steric clashes were evaluated using Probe ( 34 ) implemented in Coot ( 35 ).
- Full pipeline: simulation/modelling [GROMACS v2023.1] -> structure determination [PHENIX] -> machine learning [PHENIX] -> visualisation [PyMOL] -> stage not stated [Coot, ImageJ]

### Targeting ryanodine receptors with allopurinol and xanthine derivatives for the treatment of cardiac and musculoskeletal weakness disorders. (PNAS 2025)

- DOI: 10.1073/pnas.2422082122 | PMCID: PMC12184490 | PMID: 40512792
- Evidence: Model fittings and model building were performed in Coot ( 39 ), and final models were refined with Phenix tool RealSpaceRefine ( 40 ).
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [Topaz] -> stage not stated [ChimeraX]

### Cross-reactive sarbecovirus antibodies induced by mosaic RBD nanoparticles. (PNAS 2025)

- DOI: 10.1073/pnas.2501637122 | PMCID: PMC12130868 | PMID: 40402246
- Evidence: The model was refined in Phenix ( 93 ) using real space refinement and the amino acid sequences for the mAbs were manually corrected in Coot ( 94 ).
- Full pipeline: structure determination [Coot, PHENIX, UCSF Chimera]

### Nonenzymatic RNA copying with a potentially primordial genetic alphabet. (PNAS 2025)

- DOI: 10.1073/pnas.2505720122 | PMCID: PMC12130883 | PMID: 40397670
- Evidence: After several cycles of refinement, water molecules and metal atoms with well-defined density were added in Coot ( 54 ).
- Full pipeline: structure determination [Coot, PHENIX]

### Structural insights into the activation of the human prostaglandin E&lt;sub&gt;2&lt;/sub&gt; receptor EP1 subtype by prostaglandin E&lt;sub&gt;2&lt;/sub&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2423840122 | PMCID: PMC12107139 | PMID: 40366695
- Evidence: The model was modified in Coot ( 49 ), followed by adjustments in ISOLDE ( 50 ), and then refined using PHENIX ( 51 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, R v7.40, Topaz]

### Structural insights into the ubiquitin-independent midnolin-proteasome pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2505345122 | PMCID: PMC12088389 | PMID: 40339123
- Evidence: All models were initially fitted individually as a rigid body model into each of the cryo-EM maps followed by adjustments of main-chains in Coot ( 43 ).
- Full pipeline: alignment/mapping [ChimeraX] -> quantification [ImageJ] -> structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, Coot]

### Mechanism and application of thiol-disulfide redox biosensors with a fluorescence-lifetime readout. (PNAS 2025)

- DOI: 10.1073/pnas.2503978122 | PMCID: PMC12088395 | PMID: 40327692
- Evidence: In all cases, refinement was performed using iterative cycles of automated refinement in Phenix and manual model building in Coot ( 71 , 72 ).
- Full pipeline: structure determination [Coot, PHENIX]

### Comparative analysis of STP6 and STP10 unravels molecular selectivity in sugar transport proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2417370122 | PMCID: PMC12054785 | PMID: 40279393
- Evidence: Manual model building was done in Coot ( 68 ) with iterative model adjustment in NAMDINATOR ( 69 ) and model refinement in phenix.refine ( 70 ) with final refinement parameters including individual ADP weighting and grouped TLS (2 groups).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL]

### Structure of a Gcn2 dimer in complex with the large 60S ribosomal subunit. (PNAS 2025)

- DOI: 10.1073/pnas.2415807122 | PMCID: PMC12012509 | PMID: 40198700
- Evidence: Afterward, the model was manually adjusted in Coot ( 81 , 82 ).
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [ChimeraX, Coot, PHENIX, RELION v4.0.1]

### Structural basis for immune cell binding of &lt;i&gt;Fusobacterium nucleatum&lt;/i&gt; via the trimeric autotransporter adhesin CbpF. (PNAS 2025)

- DOI: 10.1073/pnas.2418155122 | PMCID: PMC12012533 | PMID: 40198705
- Version used: **0.9.8.7**
- Evidence: The latter parts were removed and the model was then manually adjusted in Coot (WinCoot version 0.9.8.7) ( 54 ), followed by real-space refinement in PHENIX ( 55 ).
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot v0.9.8.7, PHENIX] -> visualisation [R] -> stage not stated [AlphaFold, Fiji, ImageJ, UCSF Chimera]

### DNA bending mediated by ORC is essential for replication licensing in budding yeast. (PNAS 2025)

- DOI: 10.1073/pnas.2502277122 | PMCID: PMC12002289 | PMID: 40184174
- Evidence: After removal of extra residues that do not fit the observed densities and manual adjustments in Coot ( 63 ), the models were refined against the corresponding cryo-EM density maps with phenix.real_space_refine module in PHENIX package ( 64 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [EMAN2, ImageJ, MotionCor2, RELION]

### Structural basis for neutralizing antibody binding to pertussis toxin. (PNAS 2025)

- DOI: 10.1073/pnas.2419457122 | PMCID: PMC12002313 | PMID: 40172968
- Evidence: Model building and refinement were performed in Coot, Phenix, and ISOLDE.
- Full pipeline: structure determination [Coot, PHENIX]

### Structure of ATP synthase from an early photosynthetic bacterium &lt;i&gt;Chloroflexus aurantiacus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2425824122 | PMCID: PMC12002316 | PMID: 40131952
- Evidence: Based on the density map, the atomic model of the ADP-free Ca F 1 F O , including the amino acid residues and cofactors, was manually built, and adjusted in Coot ( 79 ).
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL]

### Cryo-EM structures reveal the acetylation process of piccolo NuA4. (PNAS 2025)

- DOI: 10.1073/pnas.2414490122 | PMCID: PMC11962513 | PMID: 40100634
- Evidence: The high quality of cryo-EM maps facilitated the model building of the complex by iterative manual adjustment in Coot ( 68 ).
- Full pipeline: alignment/mapping [RELION v4.0] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [AlphaFold, Coot]

### A splendid molecular factory: De- and reconstruction of the mammalian respiratory chain. (PNAS 2025)

- DOI: 10.1073/pnas.2416162122 | PMCID: PMC11962478 | PMID: 40100632
- Evidence: Each residue was manually inspected in Coot to verify the correct side chains position when compared to previous structures and a good fitting of the electron density was achieved, confirming structural integrity was preserved during the process.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, Topaz]

### Epitope-directed selection of GPCR nanobody ligands with evolvable function. (PNAS 2025)

- DOI: 10.1073/pnas.2423931122 | PMCID: PMC11929449 | PMID: 40067891
- Evidence: A model of the complex was built in Coot and refined with Phenix real-space refinement ( 40 , 41 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [MACS2]

### Structural mechanisms underlying the modulation of CXCR4 by diverse small-molecule antagonists. (PNAS 2025)

- DOI: 10.1073/pnas.2425795122 | PMCID: PMC11929458 | PMID: 40063796
- Evidence: These ligands were fitted into the respective density map in Coot ( 41 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> stage not stated [RELION v5.0]

### State-dependent motion of a genetically encoded fluorescent biosensor. (PNAS 2025)

- DOI: 10.1073/pnas.2426324122 | PMCID: PMC11912384 | PMID: 40048274
- Evidence: Model building was performed in Coot, and the associated structures were refined in Phenix ( 49 , 50 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [AlphaFold] -> stage not stated [CCP4]

### Bacterial polysaccharide lyase family 33: Specificity from an evolutionarily conserved binding tunnel. (PNAS 2025)

- DOI: 10.1073/pnas.2421623122 | PMCID: PMC11848413 | PMID: 39932998
- Evidence: The trisaccharides were built and regularized in JLigand and fitted in Coot using real space refinement and bond regularization.
- Full pipeline: simulation/modelling [AlphaFold] -> structure determination [Coot] -> stage not stated [GROMACS]

### Bacterial sensor evolved by decreasing complexity. (PNAS 2025)

- DOI: 10.1073/pnas.2409881122 | PMCID: PMC11804620 | PMID: 39879239
- Evidence: After manual building, ligand identification was done in Coot ( 79 ), and final water inspection and refinement was assessed including Titration–Libration–Screw parameterization ( 80 ).
- Full pipeline: normalisation [CCP4] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Structural insights into glucose-6-phosphate recognition and hydrolysis by human G6PC1. (PNAS 2025)

- DOI: 10.1073/pnas.2418316122 | PMCID: PMC11789071 | PMID: 39847333
- Evidence: The predicted AlphaFold2 model of hG6PC1 was fitted into the cryo-EM density map of hG6PC1 apo in Chimera ( 50 ) and was manually inspected and adjusted in Coot ( 51 ).
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ChimeraX, PyMOL]

### Molecular mechanism of ligand recognition and activation of lysophosphatidic acid receptor LPAR6. (PNAS 2025)

- DOI: 10.1073/pnas.2415426122 | PMCID: PMC11789011 | PMID: 39847322
- Evidence: Iterative manual adjustments were carried out in Coot ( 44 ), followed by further refinement with Rosetta cryo-EM refinement ( 45 ) and Phenix real space refinement ( 46 ).
- Full pipeline: alignment/mapping [AlphaFold] -> dimensionality reduction/clustering [RELION] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v4.1, MotionCor2, R v3.50]

### Structural and functional dynamics of human cone cGMP-phosphodiesterase important for photopic vision. (PNAS 2025)

- DOI: 10.1073/pnas.2419732121 | PMCID: PMC11725853 | PMID: 39739818
- Evidence: Nonuniform refinement was used to generate final maps if it led to an improved GSFSC resolution and/or map quality as assessed by visual inspection in Coot ( 40 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UCSF Chimera] -> structure determination [ChimeraX, Coot, PHENIX, UCSF Chimera] -> stage not stated [Topaz]

### Computational-aided rational mutation design of pertuzumab to overcome active HER2 mutation S310F through antibody-drug conjugates. (PNAS 2025)

- DOI: 10.1073/pnas.2413686122 | PMCID: PMC11725927 | PMID: 39793038
- Evidence: The model was fitted into maps using Chimera, manually adjusted according to the density map in Coot ( 37 ) and was refined against map using real-space refinement in PHENIX ( 38 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.0]

### Structures of methane and ammonia monooxygenases in native membranes. (PNAS 2025)

- DOI: 10.1073/pnas.2417993121 | PMCID: PMC11725843 | PMID: 39739801
- Evidence: Examination and adjustment of copper ligands, copper centers, and membrane-associated molecules were performed manually in Coot [version 0.9.8.93 EL (ccp4)] ( 39 ).
- Full pipeline: structure determination [ChimeraX, PHENIX v1.21, Topaz] -> visualisation [ChimeraX] -> stage not stated [Coot]

### Measurement of atomic scattering factors by cryoelectron microscopy. (PNAS 2026)

- DOI: 10.1073/pnas.2528758123 | PMCID: PMC13167779 | PMID: 42101996
- Evidence: Docking and rebuilding were performed in Coot ( 73 ).
- Full pipeline: registration [MotionCor2] -> structure determination [RELION] -> stage not stated [CCP4, Coot, PyMOL]

### Structural basis of iron piracy by human gut &lt;i&gt;Bacteroides&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2528036123 | PMCID: PMC13142918 | PMID: 42066043
- Evidence: All models underwent cycles of manual building in Coot ( 63 ) and refinement in Phenix ( 64 ) until no further improvement in R factors could be achieved.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [AlphaFold]

### Structural basis of transcription-coupled RNA damage by incorporation of oxidized ribonucleotides. (PNAS 2026)

- DOI: 10.1073/pnas.2602266123 | PMCID: PMC13099631 | PMID: 41980106
- Evidence: Model building and refinement were performed through iterative cycles of manual model building in Coot and automated refinement with Phenix refine ( 53 ).
- Full pipeline: structure determination [Coot] -> stage not stated [PHENIX]

### Deep learning-enabled scaffolding of spatial arrays of PfCSP epitopes. (PNAS 2026)

- DOI: 10.1073/pnas.2521914123 | PMCID: PMC13079917 | PMID: 41945436
- Evidence: The SES-2 scaffold was manually fitted into the observed electron density, followed by multiple rounds of refinement using phenix.refine ( 50 ), with iterative model building in Coot ( 51 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [ChimeraX v1.7, RoseTTAFold]

### Recurrent SARS-CoV-2 Omicron broadly neutralizing humanized antibodies in different single human V&lt;sub&gt;H&lt;/sub&gt;1-2-rearranging mouse models. (PNAS 2026)

- DOI: 10.1073/pnas.2537053123 | PMCID: PMC13037937 | PMID: 41871249
- Evidence: Model building was performed in Coot ( 61 ), and iterative refinement in Phenix ( 62 ) and ISOLDE ( 63 ).
- Full pipeline: structure determination [Coot, PHENIX]

### Discovery and mechanism of negative allosteric modulation of the α7 nicotinic acetylcholine receptor by nanobodies. (PNAS 2026)

- DOI: 10.1073/pnas.2514734123 | PMCID: PMC12846786 | PMID: 41576092
- Evidence: Model was modified in Coot ( 29 ) and refined in Phenix1.21 ( 30 ) using secondary structure and Ramachandran restraints.
- Full pipeline: structure determination [Coot] -> stage not stated [CCP4, ChimeraX, PyMOL]

### Structural basis for iterative methylation by a cobalamin-dependent radical &lt;i&gt;S&lt;/i&gt;-adenosylmethionine enzyme in cystobactamids biosynthesis. (PNAS 2026)

- DOI: 10.1073/pnas.2527019123 | PMCID: PMC12846815 | PMID: 41564129
- Evidence: Iterative manual model building and refinement were performed in Coot and Phenix ( 39 , 43 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [PHENIX]

### Structural characterization of the HDV virion and its ribonucleoprotein. (PNAS 2026)

- DOI: 10.1073/pnas.2519809123 | PMCID: PMC12846810 | PMID: 41564123
- Evidence: Models of ideal double-stranded RNA were generated in Coot with repeating adenosine-uridine (AU) sequence.
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [ChimeraX, Coot, Matplotlib, NumPy, SciPy, Topaz, UCSF Chimera]

### Molecular structure of the ESCRT-III-based archaeal CdvAB cell division machinery. (PNAS 2026)

- DOI: 10.1073/pnas.2525941123 | PMCID: PMC12818579 | PMID: 41543908
- Evidence: A dimer of SiCdvA ΔC from the crystal structure was rigidly docked into the cryo-EM map, and refined in Coot and PHENIX real-space refine.
- Full pipeline: alignment/mapping [MAFFT, PyMOL] -> structure determination [Coot, PHENIX, RELION] -> visualisation [ChimeraX v1.7.1] -> stage not stated [AlphaFold, MotionCor2]

### Phosphatase SHP2 pathogenic mutations enhance activity by altering conformational sampling. (PNAS 2026)

- DOI: 10.1073/pnas.2513851123 | PMCID: PMC12818432 | PMID: 41528873
- Evidence: Images were processed in XDS or iMosflm, scaled and merged in Aimless, and the structure solved and refined in Phenix with model adjustments performed in Coot.
- Full pipeline: normalisation [Coot, PHENIX] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Ultrapotent antibodies against diverse and highly transmissible SARS-CoV-2 variants. (Science 2021)

- DOI: 10.1126/science.abh1766 | PMCID: PMC9269068 | PMID: 34210892
- Evidence: Iterative manual model building and real space refinement were carried out in Coot ( 48 ) and in Phenix ( 49 ), respectively.
- Full pipeline: variant calling [GATK v4.1.9.0] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, UCSF Chimera]

### RNA-activated protein cleavage with a CRISPR-associated endopeptidase. (Science 2022)

- DOI: 10.1126/science.add7450 | PMCID: PMC10028731 | PMID: 36423276
- Evidence: Model building Initial protein models were generated using AlphaFold2 ( 40 ) and fit into the cryo-EM maps, and then manually edited using Coot ( 41 ), while RNA molecules were entirely de novo built in Coot.
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, Coot, Jupyter, MotionCor2, RELION]

### Structural basis for potent antibody neutralization of SARS-CoV-2 variants including B.1.1.529. (Science 2022)

- DOI: 10.1126/science.abn8897 | PMCID: PMC9580340 | PMID: 35324257
- Evidence: Iterative manual model building and real-space refinement were carried out in Coot ( 48 ) and in Phenix ( 62 ), respectively.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold v2.0, ChimeraX, UCSF Chimera]

### Precise targeting of HIV broadly neutralizing antibody precursors in humans. (Science 2025)

- DOI: 10.1126/science.adv5572 | PMCID: PMC12313413 | PMID: 40373114
- Version used: **0.9.8**
- Evidence: Model building was performed by docking homology models of trimer and Fab Fv in UCSF ChimeraX ( 78 ), manually building and refining in Coot 0.9.8 ( 93 ) and real space refinement using Phenix ( 94 ).
- Full pipeline: alignment/mapping [Bowtie2] -> structure determination [Coot v0.9.8, PHENIX] -> stage not stated [ChimeraX, Nextflow, R, RELION v4.0, Trinity]

### Vaccination with mRNA-encoded nanoparticles drives early maturation of HIV bnAb precursors in humans. (Science 2025)

- DOI: 10.1126/science.adr8382 | PMCID: PMC13164876 | PMID: 40373112
- Version used: **0.9.8**
- Evidence: Model building was performed by docking homology models of trimer (generated by AlphaFold 3 ( 85 )) and Fab Fv (generated by AbodyBuilder2 ( 86 )) in UCSF ChimeraX ( 87 ), manually building and refining in Coot 0.9.8 ( 88 ) and real space refinement using Phenix ( 89 ).
- Full pipeline: differential/statistical testing [Matplotlib, seaborn] -> structure determination [AlphaFold, ChimeraX, Coot v0.9.8, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [NumPy]

### TIGR-Tas: A family of modular RNA-guided DNA-targeting systems in prokaryotes and their viruses. (Science 2025)

- DOI: 10.1126/science.adv9789 | PMCID: PMC12045711 | PMID: 40014690
- Evidence: Cryo-EM model building An AlphaFold2 model of the TasR ORF was docked into one corresponding protomer in the cryo-EM density and fitted using ISOLDE and adjusted in Coot ( 103 , 104 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, MAFFT, PyMOL] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [MAFFT, PHENIX] -> stage not stated [CTFFIND, ColabFold, Coot, HMMER, MotionCor2, RELION, Topaz]

### Evolutionary adaptations of doublet microtubules in trypanosomatid parasites. (Science 2025)

- DOI: 10.1126/science.adr5507 | PMCID: PMC7617938 | PMID: 40080577
- Evidence: If the prediction was a reasonable fit to the map, the AF2 model was used as the starting model for iterative real-space refinement in Coot.
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [napari] -> stage not stated [AlphaFold, CTFFIND v4.0, ChimeraX, HMMER, ImageJ, RELION]

### Molecular basis of FIGNL1 in dissociating RAD51 from DNA and chromatin. (Science 2025)

- DOI: 10.1126/science.adr7920 | PMCID: PMC7617353 | PMID: 39636933
- Evidence: The model was visually inspected, and manually corrected in Coot ( 68 ).
- Full pipeline: registration [CTFFIND] -> structure determination [AlphaFold, PHENIX] -> visualisation [Fiji, ImageJ, RELION] -> stage not stated [Coot, Topaz]

### Induction of broadly neutralizing HIV antibodies by a two-step mechanism informs vaccine design. (Science 2026)

- DOI: 10.1126/science.aec6396 | PMCID: PMC13308464 | PMID: 42096521
- Version used: **0.8.9**
- Evidence: Manual adjustments and sequence corrections were performed using Coot v.0.8.9 ( 91 ), followed by iterative cycles of model rebuilding in Coot and refinement using Phenix ( 92 ).
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [SciPy v0.18.0] -> structure determination [ChimeraX, Coot v0.8.9, PHENIX] -> visualisation [PyMOL]

### Structural ontogeny of protein-protein interactions. (Science 2026)

- DOI: 10.1126/science.adx6931 | PMCID: PMC12904254 | PMID: 41678610
- Evidence: Additional refinement was performed interactively in Coot ( 78 ) and in Phenix ( 79 - 82 ) (A2B2, A3B3, A5B5, A6B6, A7B7) or Buster ( 83 , 84 ) with final refinement in Phenix (A4B1, A7B3).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CCP4, MACS2, SciPy, igraph]

### Structure and organization of AMPA receptor-TARP complexes in the mammalian cerebellum. (Science 2026)

- DOI: 10.1126/science.aeb3577 | PMCID: PMC7619101 | PMID: 41379938
- Evidence: Individual chains were first rigid-body fit into the EM density map using ChimeraX ( 85 ), and then manual refinement was performed in Coot to further refine the geometry, and several rounds of PHENIX real-space refinement and manual refinement were performed iteratively.
- Full pipeline: alignment/mapping [MUSCLE] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [PyMOL v2.5] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

