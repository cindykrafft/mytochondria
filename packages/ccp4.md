# CCP4

- **Category:** structbio
- **Papers in survey:** 124
- **Journals:** PNAS (81), Nature (30), Cell (12), Science (1)
- **Years:** 2021 (15), 2022 (31), 2023 (28), 2024 (22), 2025 (19), 2026 (9)
- **Versions named:** 7.0 (2), 6.5 (1), 7.1 (1)
- **Pipeline stages it appears in:** normalisation (32), structure determination (15), alignment/mapping (2), machine learning (1), differential/statistical testing (1)

## Papers

### The epitope arrangement on flavivirus particles contributes to Mab C10's extraordinary neutralization breadth across Zika and dengue viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.010 | PMCID: PMC8724787 | PMID: 34852239
- Evidence: ...s://phenix-online.org MODELER UCSF https://salilab.org/modeller/ Pymol 1.7.2 Schrödinger https://pymol.org/2/ XDS Kabsch, 2010 https://xds.mr.mpg.de/ CCP4 Collaborative Computational Project, 1994 https://www.ccp4.ac.uk/ Phaser McCoy et al., 2007 https://www.phaser.cimr.cam.ac.uk/index.php/Phaser_Crystallographic_Software BUSTER-TNT Blanc et al., 2004 https://www.globalphasing.com Staraniso Global...
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CCP4, ChimeraX v1.2.5, PHENIX v1.14, PyMOL, RELION v2.1, UCSF Chimera v1.11.2]

### From structure to clinic: Design of a muscarinic M1 receptor agonist with potential to treatment of Alzheimer's disease. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.001 | PMCID: PMC7616177 | PMID: 34822784
- Evidence: Data from individual crystals were integrated using XDS ( Kabsch, 2010 ) or MOSFLM (Battye et al., 2011) combined using POINTLESS ( EVANS, 2006 ) from the CCP4 suite (Winn et al., 2011) and merged and scaled using AIMLESS ( Evans and Murshudov, 2013 ) and the STARANISO procedure.
- Full pipeline: normalisation [CCP4] -> stage not stated [EEGLAB, ImageJ, PyMOL]

### De novo identification of mammalian ciliary motility proteins using cryo-EM. (Cell 2021)

- DOI: 10.1016/j.cell.2021.10.007 | PMCID: PMC8595878 | PMID: 34715025
- Evidence: Intermolecular contacts were determined using CONTACT from the CCP4 suite ( Winn et al., 2011 ) with a 7 Å distance cutoff.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX, Coot v0.9, ImageJ v1.44d, RELION v3.1]

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Evidence: ..., USA RRID: SCR_002798 DIALS (via XIA2) Winter et al., 2013, 2018 https://doi.org/10.1107/S0907444913015308 https://doi.org/10.1107/S2059798317017235 CCP4 package Winn et al., 2011 https://doi.org/10.1107/S0907444910045749 Staraniso https://staraniso.globalphasing.org/cgi-bin/staraniso.cgic Phenix Liebschner et al., 2019 https://doi.org/10.1107/S2059798319011471 COOT Emsley and Cowtan, 2004 https:...
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### State-selective modulation of heterotrimeric Gαs signaling with macrocyclic peptides. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.019 | PMCID: PMC9747239 | PMID: 36170854
- Evidence: Then the dataset was integrated using the HKL2000 package ( Otwinowski and Minor, 1997 ), scaled with Scala ( Evans, 2006 ) and solved by molecular replacement using Phaser ( McCoy et al., 2007 ) in CCP4 software suite ( Winn et al., 2011 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX]

### Accurate de novo design of membrane-traversing macrocycles. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.019 | PMCID: PMC9490236 | PMID: 36041435
- Evidence: ...bstat Phoenix WinNonlin®, Version 6.3 Pharsight Corp https://www.certara.com/software/phoenix-winnonlin/ XDS Winn et al., 2001 https://xds.mr.mpg.de/ CCP4 Kabsch, 2010 https://www.ccp4.ac.uk/ SHELXL Sheldrick, 2015a , 2015b https://shelx.uni-goettingen.de/ SHELXLe Hübschle, 2011 https://www.shelxle.org/shelx/eingabe.php Other Bruker Avance II 600 MHz NMR System Bruker Biospin, Inc. https://www.bru...
- Full pipeline: dimensionality reduction/clustering [PyMOL] -> visualisation [Matplotlib, PyMOL, seaborn] -> stage not stated [CCP4]

### Structure of a fully assembled tumor-specific T cell receptor ligated by pMHC. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.010 | PMCID: PMC9630439 | PMID: 35985289
- Evidence: ... 187440 P8.91 Addgene ID 187441 Software and algorithms Calcium flux analysis code (custom) In-house generate https://github.com/janehumphrey/calcium CCP4 program suite Winn et al., 2011 RRID:SCR_007255 CHARMM-GUI Jo et al., 2008 ; Lee et al., 2016 charmm-gui.org COOT Emsley and Cowtan, 2004 RRID:SCR_014222 cryoSPARC Punjani et al., 2017 RRID:SCR_016501 Flowjo v10.7.1 N/A https://www.flowjo.com Gr...
- Full pipeline: simulation/modelling [ChimeraX, UCSF Chimera, VMD] -> stage not stated [CCP4, GROMACS v2020.6, MDAnalysis v0.20.1, NumPy v1.19.5, PHENIX, PyMOL]

### Emergence of immune escape at dominant SARS-CoV-2 killer T cell epitope. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.002 | PMCID: PMC9279490 | PMID: 35931021
- Version used: **7.1**
- Evidence: ...ad GraphPad Prism, RRID: SCR_002798 FlowJo FlowJo FlowJo, RRID: SCR_008520 Rock Maker Formulatrix N/A PyMol 2.3.4 Schrodinger PyMOL, RRID: SCR_000305 CCP4 7.1 Science and Technology Facilities Council CCP4, RRID: SCR_007255 PHASER 2.7 Phoenix Online PHASER, RRID: SCR_014219 Win-COOT 0.9.6 Science and Technology Facilities Council COOT, RRID: SCR_014222 REFMAC 5.8 Science and Technology Facilities ...
- Full pipeline: alignment/mapping [IQ-TREE, MAFFT] -> stage not stated [CCP4 v7.1, PyMOL v2.3.4, R v4.0, REFMAC v5.8, tidyverse]

### Structure of the endosomal Commander complex linked to Ritscher-Schinzel syndrome. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.003 | PMCID: PMC10187114 | PMID: 37172566
- Evidence: The data was integrated with XDS 99 and scaled with AIMLESS 100 in the CCP4 suite.
- Full pipeline: alignment/mapping [ColabFold, MAFFT, PyMOL] -> normalisation [CCP4] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, HMMER v3.3.2, PHENIX, RELION, Topaz]

### Targeting Ras-, Rho-, and Rab-family GTPases via a conserved cryptic pocket. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.017 | PMCID: PMC11531380 | PMID: 39255801
- Evidence: The dataset was indexed and integrated using iMosflm, 45 scaled with Scala, 46 and solved by molecular replacement using Phaser 47 in CCP4 software suite.
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CCP4] -> simulation/modelling [VMD] -> structure determination [PHENIX]

### Natural malaria infection elicits rare but potent neutralizing antibodies to the blood-stage antigen RH5. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.037 | PMCID: PMC11383431 | PMID: 39059381
- Evidence: Molecular replacement for each dataset except RH5ΔNL:MAD10-466 was performed using PHASER in the CCP4 suite, using RH5 from PDB 6RCU and an scFv scaffold as search models.
- Full pipeline: structure determination [PHENIX v1.20.1] -> visualisation [ChimeraX] -> stage not stated [CCP4, R]

### Phages communicate across species to shape microbial ecosystems. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.004 | PMCID: PMC13220667 | PMID: 41923642
- Evidence: 37 https://xds.mr.mpg.de Scala (CCP4) Evans et al.
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CCP4, IQ-TREE, R, ggplot2, ggpubr, tidyverse]

### Cross-HLA targeting of intracellular oncoproteins with peptide-centric CARs. (Nature 2021)

- DOI: 10.1038/s41586-021-04061-6 | PMCID: PMC8599005 | PMID: 34732890
- Evidence: Diffraction images were indexed, integrated, and scaled using MOSFLM and Scala in CCP4 Package 55 .
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Design of biologically active binary protein 2D materials. (Nature 2021)

- DOI: 10.1038/s41586-020-03120-8 | PMCID: PMC7855610 | PMID: 33408408
- Evidence: The calculation was done using a CCP4 script based on the “unique” command which generates a unique set of reflection given a symmetry and distances.
- Full pipeline: alignment/mapping [RELION] -> dimensionality reduction/clustering [RELION] -> stage not stated [CCP4, ImageJ v1.52d, NumPy]

### Structure of the class D GPCR Ste2 dimer coupled to two G proteins. (Nature 2021)

- DOI: 10.1038/s41586-020-2994-1 | PMCID: PMC7116888 | PMID: 33268889
- Evidence: 9 Structural features of Ste2 and comparison with mammalian GPCRs. a-c , Alignment of GPCRs was performed by GESAMT 74 (CCP4 suite of programs) in conjunction with 39 other G protein or arrestin-coupled GPCR structures ( Fig.
- Full pipeline: alignment/mapping [CCP4] -> registration [MotionCor2] -> simulation/modelling [GROMACS] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [RELION]

### Direct activation of a bacterial innate immune system by a viral capsid protein. (Nature 2022)

- DOI: 10.1038/s41586-022-05444-z | PMCID: PMC9712102 | PMID: 36385533
- Evidence: In all cases, the unit cell content was estimated with the program MATTHEW COEF from the CCP4 program suite 58 .
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> stage not stated [AlphaFold, BLAST, CCP4, PHENIX]

### Structural basis for SHOC2 modulation of RAS signalling. (Nature 2022)

- DOI: 10.1038/s41586-022-04838-3 | PMCID: PMC9452301 | PMID: 35768504
- Evidence: Yen for discussions about RAS biology; and the The 2021 CCP4/APS School in Macromolecular Crystallography for training.
- Full pipeline: structure determination [ChimeraX, PHENIX] -> machine learning [CCP4] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Mechanism of mitoribosomal small subunit biogenesis and preinitiation. (Nature 2022)

- DOI: 10.1038/s41586-022-04795-x | PMCID: PMC9200640 | PMID: 35676484
- Version used: **7.0**
- Evidence: Geometrical restraints of modified residues and ligands were calculated by Grade Web Server ( http://grade.globalphasing.org ) or obtained from the library of CCP4 7.0 (ref.
- Full pipeline: registration [RELION v3.0] -> differential/statistical testing [limma v3.34.9] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CCP4 v7.0, ChimeraX v0.91]

### Design of protein-binding proteins from the target structure alone. (Nature 2022)

- DOI: 10.1038/s41586-022-04654-9 | PMCID: PMC9117152 | PMID: 35332283
- Evidence: Data were indexed, integrated and scaled using XDS 58 , 59 and merged using Pointless and Aimless from the CCP4 suite 60 – 62 .
- Full pipeline: quantification [ImageJ] -> normalisation [CCP4] -> structure determination [Coot, PHENIX] -> stage not stated [PyMOL]

### Mechanism-based traps enable protease and hydrolase substrate discovery. (Nature 2022)

- DOI: 10.1038/s41586-022-04414-9 | PMCID: PMC8866121 | PMID: 35173328
- Evidence: Datasets were auto-processed with XIA2 DIALS (version 0.7.90), scaled using Aimless and Refmac5 (version 5.8.0258) in the CCP4 suite (version 7.0.078) of programs.
- Full pipeline: normalisation [CCP4] -> visualisation [PyMOL v2.5] -> stage not stated [Python v3.8.1]

### Visualizing protein breathing motions associated with aromatic ring flipping. (Nature 2022)

- DOI: 10.1038/s41586-022-04417-6 | PMCID: PMC8866124 | PMID: 35173330
- Evidence: Aimless, Phaser and Refmac were all used as programs of the CCP4 suite 67 .
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, VMD]

### Targeting of intracellular oncoproteins with peptide-centric CARs. (Nature 2023)

- DOI: 10.1038/s41586-023-06706-0 | PMCID: PMC10665195 | PMID: 37938771
- Evidence: Diffraction images were indexed, integrated and scaled using MOSFLM and Scala in CCP4 Package 56 .
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Sialoglycan binding triggers spike opening in a human coronavirus. (Nature 2023)

- DOI: 10.1038/s41586-023-06599-z | PMCID: PMC10700143 | PMID: 37794193
- Evidence: Domain rotations were calculated with CCP4 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CCP4, RELION v3.1.1, VMD]

### Cryo-EM structures reveal native GABA&lt;sub&gt;A&lt;/sub&gt; receptor assemblies and pharmacology. (Nature 2023)

- DOI: 10.1038/s41586-023-06556-w | PMCID: PMC10550821 | PMID: 37730991
- Evidence: Lipid and lipid-like molecules, including POPC, PIP2, dodecane and octane, were modelled using the CCP4 monomer library.
- Full pipeline: structure determination [Coot] -> stage not stated [AlphaFold, CCP4, ChimeraX, Python, RELION]

### A common allele of HLA is associated with asymptomatic SARS-CoV-2 infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06331-x | PMCID: PMC10396966 | PMID: 37468623
- Evidence: The data were processed using XDS 66 and the structures were determined by molecular replacement using the PHASER program (v.2.8.3) 67 from the CCP4 suite 68 with a model of HLA-B*15:01 without the peptide (derived from Protein Data Bank (PDB) 5TXS ) 69 .
- Full pipeline: variant calling [R] -> structure determination [PHENIX v1.20.1] -> stage not stated [CCP4, MACS2, PyMOL v2.5]

### Outer membrane utilisomes mediate glycan uptake in gut Bacteroidetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06146-w | PMCID: PMC7618045 | PMID: 37286596
- Evidence: Other software used were from CCP4 suite 53 .
- Full pipeline: registration [CTFFIND] -> differential/statistical testing [limma] -> stage not stated [AlphaFold, CCP4, ChimeraX, PHENIX, R v4.1.1, RELION]

### Pan-KRAS inhibitor disables oncogenic signalling and tumour growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06123-3 | PMCID: PMC10322706 | PMID: 37258666
- Evidence: Model building and refinement was performed with standard protocols using CCP4, COOT, autoBUSTER v.2.11.2 ( http://www.globalphasing.com ) and Phenix 35 , 36 .
- Full pipeline: alignment/mapping [HISAT2, HTSeq, Python] -> quantification [ImageJ, edgeR] -> structure determination [CCP4, PHENIX] -> stage not stated [Bioconductor, limma]

### A small-molecule PI3Kα activator for cardioprotection and neuroregeneration. (Nature 2023)

- DOI: 10.1038/s41586-023-05972-2 | PMCID: PMC7614683 | PMID: 37225977
- Evidence: Initial phases were obtained with molecular replacement, using Phaser in the CCP4 suite, with an initial model from PDB entry 4TUU.
- Full pipeline: quantification [R v4.0.0] -> differential/statistical testing [R v4.0.0] -> structure determination [PHENIX, REFMAC] -> stage not stated [CCP4, ImageJ, PyMOL]

### mRNA decoding in human is kinetically and structurally distinct from bacteria. (Nature 2023)

- DOI: 10.1038/s41586-023-05908-w | PMCID: PMC10156603 | PMID: 37020024
- Evidence: Subsequently, ribosomal proteins and rRNAs were automatically built and refined using the ARP/wARP classic EM module in the CCP4 suite of programs 74 .
- Full pipeline: registration [MotionCor2] -> structure determination [CCP4] -> machine learning [REFMAC] -> stage not stated [ChimeraX, Coot, RELION v3.1, UCSF Chimera]

### Ultrafast structural changes direct the first molecular events of vision. (Nature 2023)

- DOI: 10.1038/s41586-023-05863-6 | PMCID: PMC10060157 | PMID: 36949205
- Evidence: For the calculation of F calc − F calc difference maps, the F calc amplitudes were computed using SFall, scaled against experimental data using Scaleit and difference maps were calculated using FFT to a resolution of 1.7 Å, all programs were available in the CCP4 suite 78 .
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Molecular basis for transposase activation by a dedicated AAA+ ATPase. (Nature 2024)

- DOI: 10.1038/s41586-024-07550-6 | PMCID: PMC11208146 | PMID: 38926614
- Evidence: ...ints for the protein, and stacking, hydrogen bonds and base-pair parallel planes restraints for the DNA (generated using LIBG and ProSMART tools from CCP4 package) 68 .
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX v1.5] -> stage not stated [CCP4, CTFFIND v4.1, RELION, Topaz]

### Discovery of potent small-molecule inhibitors of lipoprotein(a) formation. (Nature 2024)

- DOI: 10.1038/s41586-024-07387-z | PMCID: PMC11111404 | PMID: 38720069
- Version used: **6.5**
- Evidence: The diffraction data were indexed and integrated using MOSFLM 7.0.5 and merged and scaled with Scala 3.3 and Truncate 6.5 from the CCP4 6.5 suite 30 .
- Full pipeline: normalisation [CCP4 v6.5] -> structure determination [REFMAC v5.8] -> stage not stated [Coot v0.8]

### The UFM1 E3 ligase recognizes and releases 60S ribosomes from ER translocons. (Nature 2024)

- DOI: 10.1038/s41586-024-07093-w | PMCID: PMC10937380 | PMID: 38383789
- Evidence: Datasets were collected at the European Synchrotron Radiation Facility (ESRF), beamline ID23-EH2, and processed with the autoPROC suite 61 (including XDS 62 , Pointless 63 Aimless 64 , CCP4 (ref.
- Full pipeline: registration [RELION v3.1] -> structure determination [AlphaFold, ChimeraX v1.2.5, REFMAC] -> machine learning [cryoDRGN v3.2.0] -> stage not stated [CCP4, Coot v0.9.8.1, PHENIX v1.2.1]

### Influence of pump laser fluence on ultrafast myoglobin structural dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07032-9 | PMCID: PMC10881388 | PMID: 38355794
- Evidence: To calculate light-dark difference electron density maps, light data were scaled to the dark data using SCALEIT 60 from the CCP4 suite 61 using Wilson scaling.
- Full pipeline: normalisation [CCP4] -> structure determination [CCP4] -> stage not stated [NumPy, SciPy]

### A new antibiotic traps lipopolysaccharide in its intermembrane transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06799-7 | PMCID: PMC10794137 | PMID: 38172635
- Evidence: Cif restraints for E. coli lipopolysaccharide were generated using the sketcher tool in CCP4 (ref.
- Full pipeline: alignment/mapping [RELION] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX, Coot]

### Design of facilitated dissociation enables timing of cytokine signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09549-z | PMCID: PMC12611780 | PMID: 40993395
- Evidence: X-ray intensities and data reduction were evaluated and integrated using XDS 66 and merged and scaled using Pointless or Aimless in the CCP4 program suite 67 .
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [CCP4] -> differential/statistical testing [DESeq2] -> simulation/modelling [MDAnalysis] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> stage not stated [GROMACS v2020.2, PyMOL, RoseTTAFold]

### Diffusing protein binders to intrinsically disordered proteins. (Nature 2025)

- DOI: 10.1038/s41586-025-09248-9 | PMCID: PMC12367549 | PMID: 40739343
- Evidence: X-ray intensities and data reduction were evaluated and integrated using XDS 42 and merged/scaled using Pointless/Aimless in the CCP4 program suite 43 .
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX v1.21.1] -> machine learning [RoseTTAFold] -> stage not stated [AlphaFold, ImageJ v1.54p, PyMOL v2.4.0, Python v3.9.7, UCSF Chimera v1.14]

### Programmable protein ligation on cell surfaces. (Nature 2025)

- DOI: 10.1038/s41586-025-09287-2 | PMCID: PMC12321220 | PMID: 40739351
- Evidence: The phase information was determined by molecular replacement using PHASER in the CCP4 suite 41 and using an in silico AlphaFold2 (refs.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, CCP4, PyMOL v2.5]

### DNA-guided transcription factor interactions extend human gene regulatory code. (Nature 2025)

- DOI: 10.1038/s41586-025-08844-z | PMCID: PMC12119339 | PMID: 40205063
- Evidence: Structure determination and refinement All structures were solved by molecular replacement using the program Phaser 74 as implemented in PHENIX 75 and CCP4 (ref.
- Full pipeline: differential/statistical testing [Bioconductor, ComplexHeatmap, Python, R, SciPy] -> structure determination [CCP4, PHENIX] -> machine learning [R] -> visualisation [Bioconductor, ComplexHeatmap] -> stage not stated [AlphaFold v2.0, BEDTools v2.30.0, Cytoscape, PyMOL, RoseTTAFold]

### Conformational protection of molybdenum nitrogenase by Shethna protein II. (Nature 2025)

- DOI: 10.1038/s41586-024-08355-3 | PMCID: PMC11754109 | PMID: 39779845
- Evidence: Raw data was auto-processed using autoPROC 54 and the resolution was cut at 1.45 Å using AIMLESS 55 from the CCP4 (ref.
- Full pipeline: structure determination [ChimeraX, PHENIX, RELION v3.1] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4, CTFFIND v4.1]

### Substrate selectivity of the human RNA m&lt;sup&gt;5&lt;/sup&gt;C methyltransferase NSUN2. (Nature 2026)

- DOI: 10.1038/s41586-026-10582-9 | PMCID: PMC13289585 | PMID: 42203868
- Evidence: For modelling protein–RNA covalent linkages, monomer restraints for the conjugated cytosine (5DC) were generated in Phenix.eLBOW and link restraints between the 5DC monomer and NSUN2 C321 were generated using AceDRG distributed through the CCP4 software suite v.8.0.011 (refs.
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4] -> structure determination [ChimeraX v1.8, PHENIX v1.21.1] -> stage not stated [AlphaFold, CCP4]

### Fibroblastic reticular cells direct the initiation of T cell responses via CD44. (Nature 2026)

- DOI: 10.1038/s41586-025-09988-8 | PMCID: PMC12999478 | PMID: 41565815
- Evidence: Data were integrated by MOSFLM and scaled using SCALA within the CCP4 suite of programmes (Extended Data Table 1 ).
- Full pipeline: normalisation [CCP4] -> structure determination [Coot] -> stage not stated [CellProfiler, ImageJ, PHENIX, PyMOL]

### A conserved epitope III on hepatitis C virus E2 protein has alternate conformations facilitating cell binding or virus neutralization. (PNAS 2021)

- DOI: 10.1073/pnas.2104242118 | PMCID: PMC8285954 | PMID: 34260404
- Evidence: The structure of the epitope III–mAb1H8 complex was determined as previously described ( 33 ) by molecular replacement using Phaser ( 37 ) in CCP4 ( 38 ) with the anti-HCV epitope II antibody mAb#8 (PDB ID code 4HZL) as the search model ( 33 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [seaborn] -> stage not stated [CCP4, PyMOL]

### Structures suggest an approach for converting weak self-peptide tumor antigens into superagonists for CD8 T cells in cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2100588118 | PMCID: PMC8201969 | PMID: 34074778
- Evidence: The diffraction data were processed using the HKL2000/3000, iMosflm program 6 ( 64 ) and Aimless Pointless in the CCP4 software suite 7 ( 65 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4]

### 2'-O methylation of RNA cap in SARS-CoV-2 captured by serial crystallography. (PNAS 2021)

- DOI: 10.1073/pnas.2100170118 | PMCID: PMC8166198 | PMID: 33972410
- Evidence: The crystal structures of the Nsp10/16 complex were solved by molecular replacement using MolRep ( 41 ) from the CCP4 package.
- Full pipeline: alignment/mapping [UCSF Chimera] -> structure determination [REFMAC v5.8.0258] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot]

### Early-stage dynamics of chloride ion-pumping rhodopsin revealed by a femtosecond X-ray laser. (PNAS 2021)

- DOI: 10.1073/pnas.2020486118 | PMCID: PMC8020794 | PMID: 33753488
- Evidence: From the phased F ext , ED ext maps were calculated with the CCP4 program “fft” ( 41 ).
- Full pipeline: simulation/modelling [GROMACS v5.1.2, VMD] -> structure determination [Coot] -> visualisation [VMD] -> stage not stated [CCP4, PHENIX, UCSF Chimera]

### Cooperativity between the orthosteric and allosteric ligand binding sites of RORγt. (PNAS 2021)

- DOI: 10.1073/pnas.2021287118 | PMCID: PMC8017705 | PMID: 33536342
- Evidence: We also thank the tutors of the DLS-CCP4 Data Collection and Structure Solution Workshop 2017 at Diamond Light Source (Oxfordshire, United Kingdom).
- Full pipeline: simulation/modelling [GROMACS v2019.3] -> structure determination [PHENIX, REFMAC] -> stage not stated [CCP4, PyMOL v2.2.3]

### Long-range structural defects by pathogenic mutations in most severe glucose-6-phosphate dehydrogenase deficiency. (PNAS 2021)

- DOI: 10.1073/pnas.2022790118 | PMCID: PMC7848525 | PMID: 33468660
- Evidence: Datasets were processed by the XDS and CCP4 suites ( 45 – 47 ), and initial model structures were obtained by molecular replacement using Phaser with the truncated G6PD WT structure (PDB ID: 6A08) as a search model ( 21 , 48 ).
- Full pipeline: alignment/mapping [RELION v3.0.6] -> simulation/modelling [GROMACS v2019.4] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX]

### Structure of SARS-CoV-2 ORF8, a rapidly evolving immune evasion protein. (PNAS 2021)

- DOI: 10.1073/pnas.2021785118 | PMCID: PMC7812859 | PMID: 33361333
- Evidence: Integrated reflections were scaled, merged, and truncated using the CCP4 software suit ( 22 ).
- Full pipeline: normalisation [CCP4] -> visualisation [PyMOL] -> stage not stated [PHENIX]

### Human species D adenovirus hexon capsid protein mediates cell entry through a direct interaction with CD46. (PNAS 2021)

- DOI: 10.1073/pnas.2020732118 | PMCID: PMC7826407 | PMID: 33384338
- Evidence: The structure was solved by molecular replacement with Phaser ( 56 ) in CCP4 ( 57 ) using a CHAINSAW ( 58 ) model derived from the HAdV-D37 fiber knob structure (Protein Data Bank [PDB] ID code 1UXE).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [CCP4, CTFFIND, ChimeraX, EMAN2, MotionCor2, RELION v3.1]

### Orthosteric-allosteric dual inhibitors of PfHT1 as selective antimalarial agents. (PNAS 2021)

- DOI: 10.1073/pnas.2017749118 | PMCID: PMC7826358 | PMID: 33402433
- Evidence: Further processing was carried out using the CCP4 suite ( 32 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4, MACS2]

### FtsEX-independent control of RipA-mediated cell separation in <i>Corynebacteriales</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2214599119 | PMCID: PMC9897464 | PMID: 36469781
- Evidence: All datasets were processed using XDS ( 54 ) and AIMLESS from the CCP4 suite ( 55 ) ( SI Appendix, Table S2 ).
- Full pipeline: structure determination [IQ-TREE v2.0.6, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CCP4, ColabFold, HMMER]

### Integrative analysis reveals structural basis for transcription activation of Nurr1 and Nurr1-RXRα heterodimer. (PNAS 2022)

- DOI: 10.1073/pnas.2206737119 | PMCID: PMC9894219 | PMID: 36442107
- Evidence: Then, datasets were scaled using Aimless from the CCP4 program suite ( 46 ).
- Full pipeline: normalisation [CCP4] -> visualisation [PyMOL] -> stage not stated [VMD]

### Human T cells recognize HLA-DP-bound peptides in two orientations. (PNAS 2022)

- DOI: 10.1073/pnas.2214331119 | PMCID: PMC9894132 | PMID: 36442096
- Evidence: Complex structures were solved by molecular replacement in PHASER ( 26 ), CCP4 ( 27 ) suite using a separate search model of HLA-DP5 (PDB ID: 3WEX).
- Full pipeline: structure determination [Coot, PHENIX, REFMAC] -> machine learning [Coot, PHENIX, REFMAC] -> visualisation [PyMOL] -> stage not stated [CCP4]

### Yin and yang regulation of stress granules by Caprin-1. (PNAS 2022)

- DOI: 10.1073/pnas.2207975119 | PMCID: PMC9636964 | PMID: 36279435
- Evidence: The two complex structures were solved by Phaser Molecular Replacement ( 40 ) in the CCP4 suite ( 41 ) with the G3BP1 NTF2L structure (PDB ID code 4FCJ) as the searching model.
- Full pipeline: visualisation [PyMOL] -> stage not stated [CCP4]

### Structural basis for mouse receptor recognition by SARS-CoV-2 omicron variant. (PNAS 2022)

- DOI: 10.1073/pnas.2206509119 | PMCID: PMC9636943 | PMID: 36256797
- Evidence: PHENIX and CCP4 were used for molecular replacement and model refinement ( 43 , 44 ).
- Full pipeline: structure determination [CCP4, PHENIX] -> stage not stated [PyMOL]

### CRY2 isoform selectivity of a circadian clock modulator with antiglioblastoma efficacy. (PNAS 2022)

- DOI: 10.1073/pnas.2203936119 | PMCID: PMC9546630 | PMID: 36161947
- Evidence: The datasets were processed with DIALS (Diffraction Integration for Advanced Light Sources) and xia2 ( 43 ), and scaled with SCALA ( 44 ) in the CCP4 suite ( 45 ).
- Full pipeline: normalisation [CCP4] -> simulation/modelling [GROMACS] -> structure determination [PHENIX]

### Plant <i>N</i>-glycan breakdown by human gut <i>Bacteroides</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208168119 | PMCID: PMC9522356 | PMID: 36122227
- Evidence: Other programs used were from the CCP4 suite ( 40 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [CCP4, Clustal Omega]

### Structural basis of lipoprotein recognition by the bacterial Lol trafficking chaperone LolA. (PNAS 2022)

- DOI: 10.1073/pnas.2208662119 | PMCID: PMC9457489 | PMID: 36037338
- Evidence: The structure was solved using the CCP4 suite ( 51 ).
- Full pipeline: stage not stated [CCP4]

### Divergent evolution of extreme production of variant plant monounsaturated fatty acids. (PNAS 2022)

- DOI: 10.1073/pnas.2201160119 | PMCID: PMC9335243 | PMID: 35867834
- Evidence: Diffraction data were indexed and integrated using DIALS ( 49 ), then scaled and merged using CCP4 programs POINTLESS and AIMLESS ( 50 , 51 ).
- Full pipeline: alignment/mapping [RAxML v8.2.4] -> normalisation [CCP4] -> structure determination [PHENIX] -> visualisation [PyMOL]

### Single crystal spectroscopy and multiple structures from one crystal (MSOX) define catalysis in copper nitrite reductases. (PNAS 2022)

- DOI: 10.1073/pnas.2205664119 | PMCID: PMC9335323 | PMID: 35862453
- Evidence: Refinement was performed using Refmac5 ( 31 ) in the CCP4 suite ( 32 ) with manual rebuilding in Coot ( 33 ) and isotropic B-factors.
- Full pipeline: structure determination [CCP4, Coot]

### Correlation between the binding affinity and the conformational entropy of nanobody SARS-CoV-2 spike protein complexes. (PNAS 2022)

- DOI: 10.1073/pnas.2205412119 | PMCID: PMC9351521 | PMID: 35858383
- Evidence: Crystal structures were solved by molecular replacement with PHASER ( 63 ) implemented in CCP4 ( 64 ) using the RBD and H11-H4 from RCSB Protein Data Bank (PDB) accession 6ZBP ( 29 ).
- Full pipeline: dimensionality reduction/clustering [RELION] -> simulation/modelling [GROMACS, PLUMED v2.6.0] -> structure determination [ChimeraX, PHENIX] -> stage not stated [CCP4]

### Genetic and structural basis of the human anti-α-galactosyl antibody response. (PNAS 2022)

- DOI: 10.1073/pnas.2123212119 | PMCID: PMC9282431 | PMID: 35867757
- Evidence: Space groups were determined with Pointless ( 61 ). and scaling and merging were performed with AIMLESS ( 62 ), both components of CCP4 ( 63 ).
- Full pipeline: normalisation [CCP4] -> differential/statistical testing [limma] -> structure determination [PHENIX] -> machine learning [PHENIX]

### Human endogenous retrovirus-K (HERV-K) reverse transcriptase (RT) structure and biochemistry reveals remarkable similarities to HIV-1 RT and opportunities for HERV-K-specific inhibition. (PNAS 2022)

- DOI: 10.1073/pnas.2200260119 | PMCID: PMC9271190 | PMID: 35771941
- Evidence: SHELXD, PHASER and PARROT were all implemented in the CCP4 suite ( 77 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [CCP4]

### Antibody homotypic interactions are encoded by germline light chain complementarity determining region 2. (PNAS 2022)

- DOI: 10.1073/pnas.2201562119 | PMCID: PMC9191654 | PMID: 35653561
- Evidence: This numbering scheme was then mapped to the Fab-antigen interface residues for all interfaces identified by the PISA program from the CCP4 suite v1.7 ( 25 ).
- Full pipeline: alignment/mapping [CCP4] -> stage not stated [PyMOL]

### Visualization of mutagenic nucleotide processing by <i>Escherichia coli</i> MutT, a Nudix hydrolase. (PNAS 2022)

- DOI: 10.1073/pnas.2203118119 | PMCID: PMC9173781 | PMID: 35594391
- Evidence: To compare the anomalous signal intensities of Mn 2+ ions between the datasets of states 1 through 5, all data (collected using X-rays with a wavelength of 1.5 Å) were scaled together and truncated to 2.5-Å resolution using the SCALEIT program ( SI Appendix , Table S2 ) and used for calculation of the anomalous difference Fourier maps using the program FFT in CCP4 ( 52 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Structural insights into Ras regulation by SIN1. (PNAS 2022)

- DOI: 10.1073/pnas.2119990119 | PMCID: PMC9171633 | PMID: 35522713
- Evidence: Data were indexed, integrated, and scaled using the XDS, CCP4 program Pointless and Aimless ( 62 – 64 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX]

### Cryo-EM structures show the mechanistic basis of pan-peptidase inhibition by human α<sub>2</sub>-macroglobulin. (PNAS 2022)

- DOI: 10.1073/pnas.2200102119 | PMCID: PMC9181621 | PMID: 35500114
- Evidence: A test set for R free monitoring was chosen in thin shells with SFTOOLS within the CCP4 suite of programs ( 66 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4, Coot, RELION v2.1]

### Crystal structures of YeiE from <i>Cronobacter sakazakii</i> and the role of sulfite tolerance in gram-negative bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2118002119 | PMCID: PMC8931317 | PMID: 35271389
- Evidence: The structure of sulfite-bound CsYeiE RD was determined by the molecular replacement method with MOLREP ( 47 ) in the CCP4 package ( 48 ) using the model structure generated using the T-fold service, which is a part of the artificial intelligence–powered drug discovery platform (iDrug) by Tencent AI Lab ( https://drug.ai.tencent.com/ ).
- Full pipeline: quantification [ImageJ v1.53e] -> normalisation [ImageJ v1.53e] -> structure determination [PHENIX] -> stage not stated [CCP4]

### Conformational alterations in unidirectional ion transport of a light-driven chloride pump revealed using X-ray free electron lasers. (PNAS 2022)

- DOI: 10.1073/pnas.2117433119 | PMCID: PMC8892520 | PMID: 35197289
- Evidence: The structure was solved by molecular replacement with Protein Data Bank (PDB) entry 5B2N ( 20 ), and difference Fourier maps were calculated by the CCP4 and PHENIX suites ( 53 , 54 ).
- Full pipeline: stage not stated [CCP4, PHENIX]

### Universal stabilization of the influenza hemagglutinin by structure-based redesign of the pH switch regions. (PNAS 2022)

- DOI: 10.1073/pnas.2115379119 | PMCID: PMC8833195 | PMID: 35131851
- Evidence: Model building and refinement was performed using COOT ( 49 ) and the CCP4 software suite ( SI Appendix , Table S3 ).
- Full pipeline: structure determination [CCP4] -> stage not stated [ImageJ, RELION v3.1]

### Resistance gene-guided genome mining reveals the roseopurpurins as inhibitors of cyclin-dependent kinases. (PNAS 2023)

- DOI: 10.1073/pnas.2310522120 | PMCID: PMC10691236 | PMID: 37983497
- Evidence: Subsequent model building and refinement were performed according to standard protocols with COOT ( 54 ) and the software package CCP4 ( 52 ), respectively.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, PyMOL] -> structure determination [CCP4] -> visualisation [PyMOL]

### Crystal structure and activity of a de novo enzyme, ferric enterobactin esterase Syn-F4. (PNAS 2023)

- DOI: 10.1073/pnas.2218281120 | PMCID: PMC10515146 | PMID: 37695900
- Evidence: The model was built and corrected with the program COOT ( 32 ) and was refined with the program REFMAC5 ( 33 , 34 ) in the CCP4 suite ( 35 ).
- Full pipeline: structure determination [CCP4] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [PHENIX]

### Specific inhibition of an anticancer target, polo-like kinase 1, by allosterically dismantling its mechanism of substrate recognition. (PNAS 2023)

- DOI: 10.1073/pnas.2305037120 | PMCID: PMC10629583 | PMID: 37603740
- Evidence: The datasets were indexed, integrated with the XDS software package ( 64 ), and scaled with Aimless from CCP4 software suite ( 65 ).
- Full pipeline: normalisation [CCP4] -> simulation/modelling [GROMACS v2022.3, RDKit, VMD v1.9.4] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL, VMD v1.9.4] -> stage not stated [AlphaFold]

### Crystal structures of multidrug efflux transporters from <i>Burkholderia pseudomallei</i> suggest details of transport mechanism. (PNAS 2023)

- DOI: 10.1073/pnas.2215072120 | PMCID: PMC10629574 | PMID: 37428905
- Evidence: Further processing was carried out with programs from the CCP4 suite ( 57 ) and Phenix ( 58 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [CCP4, PHENIX]

### De novo designed ice-binding proteins from twist-constrained helices. (PNAS 2023)

- DOI: 10.1073/pnas.2220380120 | PMCID: PMC10319034 | PMID: 37364125
- Evidence: X-ray intensities and data reduction were evaluated and integrated using X-ray Detector Software ( 38 ) and merged/scaled using Pointless/Aimless in the CCP4 program suite ( 39 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ImageJ]

### Dual factors required for cytochrome-P450-mediated hydrocarbon ring contraction in bacterial gibberellin phytohormone biosynthesis. (PNAS 2023)

- DOI: 10.1073/pnas.2221549120 | PMCID: PMC10293830 | PMID: 37339230
- Evidence: The datasets were processed using MOSFLM and AIMLESS from the CCP4 software suite ( 27 – 29 ).
- Full pipeline: visualisation [Coot, PyMOL] -> stage not stated [CCP4, PHENIX]

### A specialized integrin-binding motif enables proTGF-β2 activation by integrin αVβ6 but not αVβ8. (PNAS 2023)

- DOI: 10.1073/pnas.2304874120 | PMCID: PMC10268255 | PMID: 37279271
- Evidence: AIMLESS and POINTLESS in CCP4 were used for scaling, merging, and point group determination ( 59 , 60 ).
- Full pipeline: alignment/mapping [MAFFT] -> normalisation [CCP4] -> structure determination [Coot, PHENIX]

### Activator-induced conformational changes regulate division-associated peptidoglycan amidases. (PNAS 2023)

- DOI: 10.1073/pnas.2302580120 | PMCID: PMC10268282 | PMID: 37276423
- Evidence: In brief, structures of AmiA and the complex between the AmiB enzymatic domain and the EnvC LytM domain were determined using X-ray crystallography using software from CCP4 suite ( 34 ) with molecular replacement probes generated by Alphafold ( 28 , 29 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [CCP4]

### Structure of WNT inhibitor adenomatosis polyposis coli down-regulated 1 (APCDD1), a cell-surface lipid-binding protein. (PNAS 2023)

- DOI: 10.1073/pnas.2217096120 | PMCID: PMC10193966 | PMID: 37155902
- Evidence: All predicted models were superimposed to assess conserved core domains of ABD1 and ABD2 using the SSM algorithm of SUPERPOSE ( 73 ) in the CCP4 suite ( 74 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CCP4, PyMOL, RoseTTAFold]

### Bioactive compounds from Huashi Baidu decoction possess both antiviral and anti-inflammatory effects against COVID-19. (PNAS 2023)

- DOI: 10.1073/pnas.2301775120 | PMCID: PMC10160982 | PMID: 37094153
- Evidence: Based on the search model with PDB code 7CBQ ( 64 ), the structure was solved by molecular replacement using the CCP4 program ( 65 ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [PHENIX] -> structure determination [PHENIX] -> stage not stated [AutoDock Vina, CCP4]

### Deciphering the evolution of flavin-dependent monooxygenase stereoselectivity using ancestral sequence reconstruction. (PNAS 2023)

- DOI: 10.1073/pnas.2218248120 | PMCID: PMC10104550 | PMID: 37014851
- Evidence: Raw data were integrated with XDS ( 61 ) and scaled in Aimless ( 62 ) in the CCP4 suite ( 62 ).
- Full pipeline: alignment/mapping [MUSCLE] -> normalisation [CCP4] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Structural insights into plasmalemma vesicle-associated protein (PLVAP): Implications for vascular endothelial diaphragms and fenestrae. (PNAS 2023)

- DOI: 10.1073/pnas.2221103120 | PMCID: PMC10083539 | PMID: 36996108
- Evidence: Next, an initial model generated by PHENIX AutoBuild ( 35 , 77 ) was manually rebuilt by COOT ( 78 ) and then fed into CCP4 BUCCANEER ( 79 ) and PHENIX Rosetta ( 35 , 80 ) for further model building and geometry optimization.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [CCP4, PyMOL]

### Structural basis for severe pain caused by mutations in the S4-S5 linkers of voltage-gated sodium channel Na<sub>V</sub>1.7. (PNAS 2023)

- DOI: 10.1073/pnas.2219624120 | PMCID: PMC10083536 | PMID: 36996107
- Evidence: Structures were solved by molecular replacement with PHASER ( 48 ) using the previously determined Na V Ab structure PDB: 3RVY ( 14 ) or PDB: 6MW ( 30 ) as a search model and refined with REFMAC ( 49 ) in the CCP4 program suite ( 50 ).
- Full pipeline: structure determination [CCP4, PHENIX, REFMAC] -> stage not stated [Coot]

### Bivalent molecular mimicry by ADP protects metal redox state and promotes coenzyme B<sub>12</sub> repair. (PNAS 2023)

- DOI: 10.1073/pnas.2220677120 | PMCID: PMC10243129 | PMID: 36888659
- Evidence: Structures of MCM•OH 2 Cbl and MCM•cob(II)alamin•ADP were solved by molecular replacement with a previously solved structure of MCM (PDB 2XIJ or PDB 2XIQ) using Phaser ( 45 ) in the CCP4 program suit.
- Full pipeline: structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [CCP4]

### A cryptic oxidoreductase safeguards oxidative protein folding in <i>Corynebacterium diphtheriae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2208675120 | PMCID: PMC9974433 | PMID: 36787356
- Evidence: Several rounds of manual adjustments of structure models using COOT ( 47 ) and anisotropic refinements with Refmac program ( 48 ) from CCP4 suite ( 49 ) were done.
- Full pipeline: structure determination [CCP4] -> stage not stated [PHENIX]

### A conserved zinc-binding site in <i>Acinetobacter baumannii</i> PBP2 required for elongasome-directed bacterial cell shape. (PNAS 2023)

- DOI: 10.1073/pnas.2215237120 | PMCID: PMC9974482 | PMID: 36787358
- Evidence: The model was further improved by several rounds of iterative manual model building with Coot ( 72 ) and refinement with Refmac5 ( 73 ) in the CCP4 suite ( 74 ).
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [CCP4] -> visualisation [PyMOL]

### Structure of metallochaperone in complex with the cobalamin-binding domain of its target mutase provides insight into cofactor delivery. (PNAS 2023)

- DOI: 10.1073/pnas.2214085120 | PMCID: PMC9974510 | PMID: 36787360
- Evidence: The same R -free flags from the preliminary dataset were used and extended in CCP4 ( 46 ).
- Full pipeline: read trimming [PHENIX] -> structure determination [Coot] -> visualisation [PyMOL v2.3.3] -> stage not stated [CCP4]

### Crystal structure of LGR ligand α2/β5 from <i>Caenorhabditis elegans</i> with implications for the evolution of glycoprotein hormones. (PNAS 2023)

- DOI: 10.1073/pnas.2218630120 | PMCID: PMC9910494 | PMID: 36574673
- Evidence: The shape correlation statistic Sc ( 60 ) was calculated using CCP4 Sc program (version 2.0) ( 61 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [CCP4] -> stage not stated [AlphaFold, ColabFold, PHENIX, PyMOL]

### MR1 presents vitamin B6-related compounds for recognition by MR1-reactive T cells. (PNAS 2024)

- DOI: 10.1073/pnas.2414792121 | PMCID: PMC11626183 | PMID: 39589872
- Evidence: Diffraction data were processed using XDS ( 58 ) and programs from the CCP4 suite ( 59 ) and Phenix package ( 60 ).
- Full pipeline: stage not stated [CCP4, PHENIX, PyMOL]

### Targeted degradation of Pin1 by protein-destabilizing compounds. (PNAS 2024)

- DOI: 10.1073/pnas.2403330121 | PMCID: PMC11588135 | PMID: 39531501
- Evidence: Diffraction data were processed with XDS ( 54 ) and with the CCP4 programs Aimless and Pointless ( 55 – 57 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX v1.7] -> stage not stated [CCP4]

### Structure and function of &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; EfpA as a lipid transporter and its inhibition by BRD-8000.3. (PNAS 2024)

- DOI: 10.1073/pnas.2412653121 | PMCID: PMC11536138 | PMID: 39441632
- Evidence: The 3D structures of lipids were generated by the SKETCHER program in CCP4 ( 56 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4, Coot, UCSF Chimera]

### Isoform-specific C-terminal phosphorylation drives autoinhibition of Casein kinase 1. (PNAS 2024)

- DOI: 10.1073/pnas.2415567121 | PMCID: PMC11474029 | PMID: 39356670
- Evidence: Data were indexed, integrated, and merged using CCP4 software suite ( 58 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4, ImageJ, PyMOL]

### An artificially evolved gene for herbicide-resistant rice breeding. (PNAS 2024)

- DOI: 10.1073/pnas.2407285121 | PMCID: PMC11348328 | PMID: 39133859
- Evidence: The initial phase was obtained by molecular replacement using Phaser MR of the CCP4 software suite ( 34 ) and the A. thaliana JOX2 structure ( 27 ) (PDB ID 6LSV) as a search model.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4]

### AlphaFold two years on: Validation and impact. (PNAS 2024)

- DOI: 10.1073/pnas.2315002121 | PMCID: PMC11348012 | PMID: 39133843
- Evidence: Both major software suites for macromolecular crystallography, CCP4 ( 24 , 25 ) and PHENIX ( 26 ), now include import procedures that convert AlphaFold’s pLDDT * confidence metric into an estimated B-factor and remove low-confidence regions.
- Full pipeline: stage not stated [AlphaFold, CCP4, ChimeraX, ColabFold, PHENIX, RoseTTAFold]

### Structural basis for mouse receptor recognition by bat SARS2-like coronaviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2322600121 | PMCID: PMC11317568 | PMID: 39083418
- Evidence: PHENIX and CCP4 were used for molecular replacement and model refinement ( 40 , 41 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [CCP4, PHENIX] -> stage not stated [PyMOL]

### Modular binder technology by NGS-aided, high-resolution selection in yeast of designed armadillo modules. (PNAS 2024)

- DOI: 10.1073/pnas.2318198121 | PMCID: PMC11228518 | PMID: 38917007
- Evidence: Molecular replacement using CCP4 with Phaser ( 26 ) was employed to solve the structure.
- Full pipeline: alignment/mapping [Bowtie2, UMAP] -> dimensionality reduction/clustering [Python, UMAP] -> structure determination [PHENIX] -> visualisation [UMAP] -> stage not stated [CCP4]

### The molecular architecture of &lt;i&gt;Lactobacillus&lt;/i&gt; S-layer: Assembly and attachment to teichoic acids. (PNAS 2024)

- DOI: 10.1073/pnas.2401686121 | PMCID: PMC11181022 | PMID: 38838019
- Evidence: N.G. acknowledges the support of FWF through a Hertha Firnberg fellowship (T-1239), J.C. for Marie Skłodowska-Curie grant 675671, and I.U. for grants PGC2018-101370-B-I00 and PID2021-128751NB-I00 (Ministry of Science and Innovation/Spanish State Research Agency/European Regional Development Fund/European Union) and support from Science and Technology Facilities Council (CCP4-ARCIMBOLDO_LOW).
- Full pipeline: stage not stated [AlphaFold, CCP4, ChimeraX, PyMOL]

### Rapid and automated design of two-component protein nanomaterials using ProteinMPNN. (PNAS 2024)

- DOI: 10.1073/pnas.2314646121 | PMCID: PMC10990136 | PMID: 38502697
- Evidence: X-ray intensities and data reduction were evaluated and integrated using XDS ( 67 ) and merged/scaled using Pointless/Aimless in the CCP4 program suite ( 67 , 68 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> machine learning [AlphaFold, RoseTTAFold]

### A redox switch allows binding of Fe(II) and Fe(III) ions in the cyanobacterial iron-binding protein FutA from <i>Prochlorococcus</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2308478121 | PMCID: PMC10962944 | PMID: 38489389
- Evidence: ...o J.S.; PhD studentships by Hamburg University and the European Synchrotron Radiation Facility (ESRF) to N.C., the Collaborative Computing Project 4 (CCP4) to L.C.
- Full pipeline: stage not stated [CCP4]

### TIFAB regulates the TIFA-TRAF6 signaling pathway involved in innate immunity by forming a heterodimer complex with TIFA. (PNAS 2024)

- DOI: 10.1073/pnas.2318794121 | PMCID: PMC10945758 | PMID: 38442163
- Evidence: The phases were determined by molecular replacement using MOLREP ( 28 ) in the CCP4 program suite ( 29 ), with the coordinates of the TIFA dimer (PDB ID:6L9U) ( 14 ).
- Full pipeline: quantification [ImageJ] -> structure determination [PHENIX] -> stage not stated [CCP4, PyMOL]

### Dinickel enzyme evolved to metabolize the pharmaceutical metformin and its implications for wastewater and human microbiomes. (PNAS 2024)

- DOI: 10.1073/pnas.2312652121 | PMCID: PMC10927577 | PMID: 38408229
- Evidence: Data were processed using XDS (Build January 26, 2018) and molecular replacement; refinement was done using Molrep and Refmac within CCP4 (Version 7.0) and Coot (v0.8.9) ( 55 – 59 ).
- Full pipeline: dimensionality reduction/clustering [Cytoscape] -> structure determination [CCP4] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, AutoDock Vina]

### Diverse cytomegalovirus US11 antagonism and MHC-A evasion strategies reveal a tit-for-tat coevolutionary arms race in hominids. (PNAS 2024)

- DOI: 10.1073/pnas.2315985121 | PMCID: PMC10907249 | PMID: 38377192
- Evidence: Diffraction data were processed using XDS ( 69 ) and merged using AIMLESS ( 70 ) within the CCP4 package (Winn 2010).
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4]

### Development of 2nd generation aminomethyl spectinomycins that overcome native efflux in <i>Mycobacterium</i> abscessus. (PNAS 2024)

- DOI: 10.1073/pnas.2314101120 | PMCID: PMC10786304 | PMID: 38165935
- Evidence: Molecular replacement was performed using PHASER from the CCP4 program suite (version 7.0).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt, FastQC, MultiQC] -> alignment/mapping [Bowtie2, featureCounts] -> variant calling [VarScan] -> differential/statistical testing [DESeq2, R] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot v0.8.2]

### Structural basis and evolutionary pathways of glycerol-1-phosphate transport in marine bacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2524546122 | PMCID: PMC12718374 | PMID: 41364767
- Evidence: The crystal structure of the GpxB DSM11874 –G1P complex was determined by molecular replacement using a CCP4 program Phaser ( 38 ) with the structure of GpxB DSM11874 generated by AlphaFold2 ( 39 ) as the search model.
- Full pipeline: quantification [HMMER] -> normalisation [HMMER] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4]

### Inhibition of ice recrystallization with designed twistless helical repeat proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2514871122 | PMCID: PMC12685108 | PMID: 41289379
- Evidence: X-ray intensities and data reduction were evaluated and integrated using x-ray detector software ( 42 ) and merged/scaled using Pointless/Aimless in the CCP4 program suite ( 42 , 43 ).
- Full pipeline: alignment/mapping [PyMOL] -> normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ImageJ, RoseTTAFold]

### Structural basis for a potent human neutralizing antibody targeting a conserved epitope on the H7 hemagglutinin head. (PNAS 2025)

- DOI: 10.1073/pnas.2503008122 | PMCID: PMC12625957 | PMID: 41196357
- Evidence: ...7, 2 D77, Q78 S106 1 D77 * Numbers represent atom-to-atom contacts between the antibody and HA residues, as analyzed using the Contact program in the CCP4 suite (distance cutoff: 4.0 Å).
- Full pipeline: stage not stated [CCP4]

### Parametrically guided design of beta barrels and transmembrane nanopores using deep learning. (PNAS 2025)

- DOI: 10.1073/pnas.2425459122 | PMCID: PMC12478100 | PMID: 40953261
- Evidence: X-ray intensities and data reduction were evaluated and integrated using XDS ( 44 ) and merged/scaled using Pointless/Aimless in the CCP4 program suite ( 45 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [AlphaFold, RoseTTAFold]

### Binding of &lt;i&gt;Fusobacterium nucleatum&lt;/i&gt; autotransporter adhesin CbpF to human CEACAM1 and CEACAM5: A Velcro model for bacterium adhesion. (PNAS 2025)

- DOI: 10.1073/pnas.2516574122 | PMCID: PMC12452904 | PMID: 40928870
- Evidence: Vdw contacts were analyzed with the Contact program in CCP4 suite at a cutoff of 4.5 Å and hydrogen bonds with the PISA online server at a cutoff of 3.5 Å.
- Full pipeline: structure determination [ChimeraX, Coot v0.9.8.92, PHENIX, PyMOL] -> visualisation [PyMOL] -> stage not stated [CCP4, MotionCor2]

### The prefusion structure of the HERV-K (HML-2) Env spike complex. (PNAS 2025)

- DOI: 10.1073/pnas.2505505122 | PMCID: PMC12280955 | PMID: 40632556
- Evidence: Structural analysis and representation were conducted using PyMol ( 54 ), ChimeraX ( 55 ), and CCP4 ( 56 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX, PyMOL]

### MTA-cooperative PRMT5 inhibitors from cofactor-directed DNA-encoded library screens. (PNAS 2025)

- DOI: 10.1073/pnas.2425052122 | PMCID: PMC12107103 | PMID: 40377999
- Evidence: The structures were solved by molecular replacement using Phaser ( 39 ) from the CCP4 program suite ( 40 ) with 6CKC as a search model.
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4]

### Mitochondria regulate MR1 protein expression and produce self-metabolites that activate MR1-restricted T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2418525122 | PMCID: PMC12107159 | PMID: 40354545
- Evidence: Diffraction data were processed using XDS ( 64 ) and programs from the CCP4 suite ( 65 ) and Phenix package ( 66 ).
- Full pipeline: stage not stated [CCP4, PHENIX, PyMOL]

### De novo discovery of a molecular glue-like macrocyclic peptide that induces MCL1 homodimerization. (PNAS 2025)

- DOI: 10.1073/pnas.2426006122 | PMCID: PMC12002256 | PMID: 40131955
- Evidence: The programs Refmac5 and Coot in the CCP4 suite ( 59 ) were used for the refinement and model building.
- Full pipeline: simulation/modelling [OpenMM v7.8] -> structure determination [CCP4] -> stage not stated [PyMOL]

### State-dependent motion of a genetically encoded fluorescent biosensor. (PNAS 2025)

- DOI: 10.1073/pnas.2426324122 | PMCID: PMC11912384 | PMID: 40048274
- Evidence: The merged data were reindexed in CCP4, and the P12 1 1 data were used successfully for molecular replacement ( 46 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [AlphaFold] -> stage not stated [CCP4]

### Cryo-EM meets crystallography: A model-independent view of the heteronuclear Mn&lt;sub&gt;4&lt;/sub&gt;Ca cluster structure of photosystem II. (PNAS 2025)

- DOI: 10.1073/pnas.2423012122 | PMCID: PMC11912364 | PMID: 40048275
- Evidence: Both σ A -weighted F o −F c and 2F o −F c maps were calculated using CCP4 ( 51 ).
- Full pipeline: stage not stated [CCP4]

### Bacterial sensor evolved by decreasing complexity. (PNAS 2025)

- DOI: 10.1073/pnas.2409881122 | PMCID: PMC11804620 | PMID: 39879239
- Evidence: Data were indexed and integrated with XDS ( 72 ) and scaled and reduced with AIMLESS ( 73 ) of the CCP4 program suite ( 74 ).
- Full pipeline: normalisation [CCP4] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Structure-guided engineering of a mutation-tolerant inhibitor peptide against variable SARS-CoV-2 spikes. (PNAS 2025)

- DOI: 10.1073/pnas.2413465122 | PMCID: PMC11789008 | PMID: 39854234
- Evidence: Manual data processing using XDS ( 46 ) and truncation using the CCP4 program suite ( 47 ) were performed as necessary.
- Full pipeline: normalisation [Topaz] -> structure determination [PHENIX] -> stage not stated [CCP4, RELION]

### Nitrous oxide production via enzymatic nitroxyl from the nitrifying archaeon &lt;i&gt;Nitrosopumilus maritimus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2416971122 | PMCID: PMC11761707 | PMID: 39823305
- Version used: **7.0**
- Evidence: X-ray diffraction data were indexed, integrated, scaled, and merged using the programs XDS3 ( 51 ) and CCP4 7.0 ( 52 ).
- Full pipeline: normalisation [CCP4 v7.0] -> stage not stated [AlphaFold, PHENIX v1.2]

### Measurement of atomic scattering factors by cryoelectron microscopy. (PNAS 2026)

- DOI: 10.1073/pnas.2528758123 | PMCID: PMC13167779 | PMID: 42101996
- Evidence: Chemical knowledge from the CCP4 Monomer Library ( 31 ) and functions available in the package GEMMI ( 32 ) were used for atom type determination.
- Full pipeline: registration [MotionCor2] -> structure determination [RELION] -> stage not stated [CCP4, Coot, PyMOL]

### Spider venom phospholipase D toxin structure: Interfacial binding site, mechanism, activation, and head group preference. (PNAS 2026)

- DOI: 10.1073/pnas.2513997123 | PMCID: PMC13079978 | PMID: 41941646
- Evidence: Intensities were integrated and scaled with the Bruker Proteum3 software suite, and structure factor amplitudes estimated with the CCP4 program suite ( 59 ).
- Full pipeline: alignment/mapping [MAFFT] -> normalisation [CCP4] -> structure determination [REFMAC] -> visualisation [ChimeraX, MAFFT]

### Decoding antibody response to MERS-CoV in wild dromedary camels. (PNAS 2026)

- DOI: 10.1073/pnas.2513716123 | PMCID: PMC12913009 | PMID: 41662528
- Evidence: Structures were determined with PHASER (CCP4 program suite) molecular replacement.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.4, MAFFT v7.310, MUSCLE v3.8.1551] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.3, PyMOL] -> stage not stated [CCP4]

### Discovery and mechanism of negative allosteric modulation of the α7 nicotinic acetylcholine receptor by nanobodies. (PNAS 2026)

- DOI: 10.1073/pnas.2514734123 | PMCID: PMC12846786 | PMID: 41576092
- Evidence: Structure analysis was performed using Pymol (PyMOL Molecular Graphics System, Version 3.0 Schrödinger, LLC), ChimeraX ( 31 ), and PISA ( 32 ) from the CCP4 suite ( 33 ).
- Full pipeline: structure determination [Coot] -> stage not stated [CCP4, ChimeraX, PyMOL]

### Mass spectrometry footprinting reveals how kinetic stabilizers counteract transthyretin dynamics altered by pathogenic mutations. (PNAS 2026)

- DOI: 10.1073/pnas.2519908122 | PMCID: PMC12773722 | PMID: 41474749
- Evidence: Data were integrated and merged using XDS ( 53 ) and scaled, reduced, and further analyzed with CCP4 ( 54 ).
- Full pipeline: normalisation [CCP4] -> visualisation [PyMOL] -> stage not stated [PHENIX v1.19.2]

### Structural ontogeny of protein-protein interactions. (Science 2026)

- DOI: 10.1126/science.adx6931 | PMCID: PMC12904254 | PMID: 41678610
- Evidence: Space groups were assigned using pointless and reflections were merged with aimless from the CCP4 suite ( 74 , 75 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CCP4, MACS2, SciPy, igraph]

