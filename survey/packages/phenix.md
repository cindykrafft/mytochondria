# PHENIX

- **Category:** structbio
- **Papers in survey:** 905
- **Journals:** PNAS (558), Nature (256), Cell (62), Science (29)
- **Years:** 2021 (87), 2022 (184), 2023 (170), 2024 (176), 2025 (230), 2026 (58)
- **Versions named:** 1.20.1 (33), 1.19.2 (14), 1.21 (11), 1.20 (8), 1.19 (8), 1.18.2 (8), 1.21.1 (6), 1.18 (5), 1.21.2 (4), 1.17.1 (4)
- **Pipeline stages it appears in:** structure determination (657), machine learning (10), visualisation (8), simulation/modelling (6), normalisation (4), read trimming (3), differential/statistical testing (2), alignment/mapping (2), dimensionality reduction/clustering (1)

## Papers

### The epitope arrangement on flavivirus particles contributes to Mab C10's extraordinary neutralization breadth across Zika and dengue viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.010 | PMCID: PMC8724787 | PMID: 34852239
- Version used: **1.14**
- Evidence: ...am.ac.uk/personal/pemsley/coot UCSF Chimera 1.11.2 UCSF https://www.cgl.ucsf.edu/chimera UCSF ChimeraX 1.2.5 UCSF https://www.rbvi.ucsf.edu/chimerax/ Phenix 1.14-3260 The PHENIX Industrial Consortium https://phenix-online.org MODELER UCSF https://salilab.org/modeller/ Pymol 1.7.2 Schrödinger https://pymol.org/2/ XDS Kabsch, 2010 https://xds.mr.mpg.de/ CCP4 Collaborative Computational Project, 1994...
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CCP4, ChimeraX v1.2.5, PHENIX v1.14, PyMOL, RELION v2.1, UCSF Chimera v1.11.2]

### De novo identification of mammalian ciliary motility proteins using cryo-EM. (Cell 2021)

- DOI: 10.1016/j.cell.2021.10.007 | PMCID: PMC8595878 | PMID: 34715025
- Evidence: The atomic model was then refined into the composite map using Phenix.real_space_refine v1.18.2-3874 ( Afonine et al., 2018 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX, Coot v0.9, ImageJ v1.44d, RELION v3.1]

### Selective activation of PFKL suppresses the phagocytic oxidative burst. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.004 | PMCID: PMC8802628 | PMID: 34320407
- Evidence: Density modification to produce final maps was performed using the ResolveCryoEM application in Phenix ( Adams et al., 2010 ; Terwilliger et al., 2020 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [RELION] -> stage not stated [PHENIX, R v3.5.0]

### Virus-encoded histone doublets are essential and form nucleosome-like structures. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.032 | PMCID: PMC8357426 | PMID: 34297924
- Evidence: While several configurations with reasonable qualitative agreement to the EM density were identified ( Figure S4 ), the loop with the overall best correlation with the density was selected as the initial conformation for further refinement via COOT ( Emsley et al., 2010 ), PHENIX ( Adams et al., 2010 ), and MDFF (see below) ( McGreevy et al., 2016 ).
- Full pipeline: alignment/mapping [MAFFT] -> quantification [R, RSEM, edgeR] -> normalisation [R, RSEM, edgeR] -> structure determination [PHENIX] -> stage not stated [NAMD, UCSF Chimera, VMD v1.9.3]

### Bacterial Vipp1 and PspA are members of the ancient ESCRT-III membrane-remodeling superfamily. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.041 | PMCID: PMC8281802 | PMID: 34166615
- Evidence: ...://www.rosettacommons.org/software Chimera Pettersen et al., 2004 https://www.cgl.ucsf.edu/chimera/ ISOLDE Croll, 2018 https://isolde.cimr.cam.ac.uk/ PHENIX Adams et al., 2010 https://phenix-online.org/ Molprobity Chen et al., 2010 http://molprobity.biochem.duke.edu/ Imagic van Heel et al., 1996 https://www.imagescience.de/imagic.html Ximdisp Smith, 1999 https://www2.mrc-lmb.cam.ac.uk/research/loc...
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE, MotionCor2] -> stage not stated [GROMACS, HMMER, ImageJ, PHENIX, RELION v3.1, VMD]

### In vitro and in vivo functions of SARS-CoV-2 infection-enhancing and neutralizing antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.021 | PMCID: PMC8232969 | PMID: 34242577
- Evidence: ...014 ) NA Biacore S200 Evaluation software Cytiva NA Coot ( Emsley et al., 2010 ) Version 0.8.9.2 Relion ( Scheres, 2012 ; Scheres, 2016 ) Version 3.1 Phenix ( Afonine et al., 2018 ; Liebschner et al., 2019 ) Version 1.17 UCSF Chimera ( Pettersen et al., 2004 ) http://www.cgl.ucsf.edu/chimera/ ISOLDE ( Croll, 2018 ) Version 1.1 Chimera X ( Goddard et al., 2018 ) https://www.rbvi.ucsf.edu/chimerax/ ...
- Full pipeline: stage not stated [CTFFIND, ChimeraX, Coot, PHENIX, PyMOL, RELION, UCSF Chimera]

### Reduced neutralization of SARS-CoV-2 B.1.617 by vaccine and convalescent serum. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.020 | PMCID: PMC8218332 | PMID: 34242578
- Evidence: Screaton) N/A Software and algorithms COOT Emsley and Cowtan, 2004 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Xia2-dials Winter et al., 2018 https://xia2.github.io/parameters.html PHENIX Liebschner et al., 2019 https://phenix-online.org/ PyMOL Schrodinger https://pymol.org/2/ Data Acquisition Software 11.1.0.11 Fortebio https://www.sartorius.com/en/products/protein-analysis/octet-system...
- Full pipeline: stage not stated [PHENIX, PyMOL]

### The monoclonal antibody combination REGEN-COV protects against SARS-CoV-2 mutational escape in preclinical and human studies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.002 | PMCID: PMC8179113 | PMID: 34161776
- Version used: **1.19.1**
- Evidence: ...6.47 EPU Thermofisher Scientific https://www.thermofisher.com/ Coot 0.8.9.2 Emsley et al., 2010 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix v 1.19.1 Liebschner et al., 2019 https://phenix-online.org/ cryoSPARC v2.14.2 Punjani et al., 2017 https://cryosparc.com/ The PyMOL Molecular Graphics System, Version 2.4.1 Schrödinger, LLC https://pymol.org/2/ Minimap2 Li, 2018 https://github...
- Full pipeline: variant calling [GATK, Picard, SAMtools v1.9] -> stage not stated [PHENIX v1.19.1, PyMOL, minimap2]

### Coupling of N7-methyltransferase and 3'-5' exoribonuclease with SARS-CoV-2 polymerase reveals mechanisms for capping and proofreading. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.033 | PMCID: PMC8142856 | PMID: 34143953
- Evidence: ...https://cryosparc.com/ UCSF Chimera Pettersen et al., 2004 https://www.cgl.ucsf.edu/chimera COOT Emsley et al., 2010 https://www.cgl.ucsf.edu/chimera PHENIX Afonine et al., 2018 https://phenix-online.org/ PyMOL Schrodinger, LLC Schrodinger Other Superdex-200 10/300 Increase GE Healthcare Cat# 28990944 Hitrap-Q HP GE Healthcare Cat# 17115401 Hitrap-SP HP GE Healthcare Cat# 17115201 Mono-Q 5/50 GL G...
- Full pipeline: structure determination [Coot] -> stage not stated [MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Fab-dimerized glycan-reactive antibodies are a structural category of natural antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.042 | PMCID: PMC8135257 | PMID: 34019795
- Evidence: The solution was improved through alternating rounds of manual rebuilding in Coot and reciprocal space refinement in PHENIX, and geometry optimization using Rosetta-Phenix refinement (phenix.rosetta_refine) ( Emsley et al., 2010 ; Adams et al., 2010 ).
- Full pipeline: alignment/mapping [MotionCor2] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX, R, Seurat, UMAP] -> stage not stated [PyMOL, RELION, UCSF Chimera, ggplot2]

### Binding and molecular basis of the bat coronavirus RaTG13 virus to ACE2 in humans and other species. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.031 | PMCID: PMC8142884 | PMID: 34139177
- Evidence: ....com/solutions/flowjo/downloads Motioncor2 Zheng et al., 2017 N/A COOT Emsley and Cowtan, 2004 https://www2.mrc-lmb.cam.ac.uk/personal/peemsley/coot/ Phenix Adams et al., 2010 http://www.phenix-online.org/ MolProbity N/A Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulfilled by the Lead Contact, Qihui Wang ( wangqi...
- Full pipeline: stage not stated [PHENIX, PyMOL]

### Structural insight into SARS-CoV-2 neutralizing antibodies and modulation of syncytia. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.033 | PMCID: PMC8064868 | PMID: 33974910
- Evidence: Interactive, density-restrained molecular dynamics simulations in ChimeraX ( Goddard et al., 2018 ) and ISOLDE ( Croll, 2018 ) were used to finalize the models, and atomic b-factors were calculated using PHENIX ( Afonine et al., 2018 ).
- Full pipeline: simulation/modelling [PHENIX] -> machine learning [PHENIX] -> stage not stated [ChimeraX v1.1, RELION v3.1, UCSF Chimera]

### Antibody evasion by the P.1 strain of SARS-CoV-2. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.055 | PMCID: PMC8008340 | PMID: 33852911
- Evidence: Screaton) N/A Software and algorithms COOT Emsley and Cowtan, 2004 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Xia2-dials Winter et al., 2018 https://xia2.github.io/parameters.html PHENIX Liebschner et al., 2019 https://www.phenix-online.org/ PyMOL DeLano https://pymol.org/2/ ; RRID: SCR_000305 Data Acquisition Software 11.1.0.11 Fortebio https://www.sartorius.com/en/products/protein-ana...
- Full pipeline: stage not stated [PHENIX, PyMOL]

### SARS-CoV-2 evolution in an immunocompromised host reveals shared neutralization escape mechanisms. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.027 | PMCID: PMC7962548 | PMID: 33831372
- Version used: **1.18.2**
- Evidence: ...aimless.html ; RRID: SCR_015747 Phaser v2.8.3 McCoy et al., 2007 https://www.phenix-online.org/documentation/reference/phaser.html ; RRID: SCR_014219 Phenix v1.18.2-3874 Adams et al., 2010 https://www.phenix-online.org ; RRID: SCR_014224 Buster v2.10.3 Bricogne et al., 2017 https://www.globalphasing.com/buster/ ; RRID: SCR_015653 Prism v8.4.3 GraphPad Software https://www.graphpad.com:443/ ; RRID:...
- Full pipeline: stage not stated [MACS2, PHENIX v1.18.2, PyMOL]

### N-terminal domain antigenic mapping reveals a site of vulnerability for SARS-CoV-2. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.028 | PMCID: PMC7962585 | PMID: 33761326
- Evidence: ....0 ( Zivanov et al., 2018 ) https://www3.mrc-lmb.cam.ac.uk/relion Coot ( Casañal et al., 2019 ) https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix-Refine ( Adams et al., 2010 ) https://www.phenix-online.org/download/ Phenix-Phaser ( McCoy et al., 2007 ) https://www.phenix-online.org/download/ XDS ( Kabsch, 2010 ) http://xds.mpimf-heidelberg.mpg.de Prism 8 GraphPad Software https://www.gr...
- Full pipeline: structure determination [PHENIX, RELION v3.0] -> visualisation [ChimeraX] -> stage not stated [Pangolin, UCSF Chimera]

### Simultaneous binding of Guidance Cues NET1 and RGM blocks extracellular NEO1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.045 | PMCID: PMC8063088 | PMID: 33740419
- Evidence: ...d Grigorieff, 2015 ) https://grigoriefflab.umassmed.edu/ctffind4 UCSF Chimera ( Goddard et al., 2007 ) https://www.cgl.ucsf.edu/chimera/download.html Phenix ( Afonine et al., 2018 ) https://www.phenix-online.org/download/ XIA2 ( Winter, 2010 ) https://xia2.github.io/ Protein Lynx Global Server software MatrixScience http://www.matrixscience.com/help/instruments_masslynx.html#PLGS Other TALON® Supe...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [MotionCor2] -> stage not stated [CTFFIND v4.1, Clustal Omega, ImageJ, PHENIX, PyMOL, RELION v3.1, UCSF Chimera]

### Reduced neutralization of SARS-CoV-2 B.1.1.7 variant by convalescent and vaccine sera. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.033 | PMCID: PMC7891044 | PMID: 33743891
- Evidence: Screaton) N/A Software and algorithms Xia2-dials Winter et al., 2018 https://xia2.github.io/parameters.html PHENIX Liebschner et al., 2019 https://www.phenix-online.org/ COOT Emsley and Cowtan, 2004 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ PyMOL Warren DeLano and Sarina Bromberg https://pymol.org/2/ Data Acquisition Software 11.1.0.11 Fortebio https://www.sartorius.com/en/products/pro...
- Full pipeline: stage not stated [PHENIX, PyMOL]

### The antigenic anatomy of SARS-CoV-2 receptor binding domain. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.032 | PMCID: PMC7891125 | PMID: 33756110
- Evidence: Screaton) N/A Software and Algorithms Xia2-dials Winter et al., 2018 https://xia2.github.io/parameters.html PHENIX Liebschner et al., 2019 https://www.phenix-online.org/ COOT Emsley and Cowtan, 2004 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ PyMOL DeLano and Bromberg https://pymol.org/2/ Data Acquisition Software 11.1.0.11 Fortebio https://www.sartorius.com/en/products/protein-analysis/...
- Full pipeline: alignment/mapping [RELION v3.1] -> registration [RELION v3.1] -> stage not stated [PHENIX, PyMOL]

### Cryo-EM Structure of an Extended SARS-CoV-2 Replication and Transcription Complex Reveals an Intermediate State in Cap Synthesis. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.016 | PMCID: PMC7666536 | PMID: 33232691
- Evidence: ...cryosparc.com/ UCSF Chimera ( Pettersen et al., 2004 ) https://www.cgl.ucsf.edu/chimera COOT ( Emsley et al., 2010 ) https://www.cgl.ucsf.edu/chimera PHENIX ( Afonine et al., 2018 ) https://www.phenix-online.org PyMOL Schrodinger, LLC Schrodinger ImageJ Fiji distribution ( Schindelin et al., 2012 ) https://imagej.net/Fiji GraphPad Prism GraphPad https://www.graphpad.com/scientific-software/prism/ ...
- Full pipeline: structure determination [Coot] -> stage not stated [ImageJ, MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Structural basis for the assembly of the type V CRISPR-associated transposon complex. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.009 | PMCID: PMC9798831 | PMID: 36435179
- Version used: **1.19.1**
- Evidence: ...mb.cam.ac.uk/research/locally-developed-software/zhang-software/ crYOLO version 1.7.6 Wagner et al., 2019 47 https://cryolo.readthedocs.io/en/stable/ Phenix 1.19.1–4122 Adams et al., 2010 48 Afonine et al., 2018 49 Liebschner et al., 2019 50 http://www.phenix-online.org/ UCSF Chimera 1.14 Pettersen et al., 2004 51 https://www.cgl.ucsf.edu/chimera/ UCSF ChimeraX 1.2 Pettersen et al., 2021 52 https:...
- Full pipeline: stage not stated [CTFFIND v1.06, ChimeraX v1.2, Coot, MotionCor2 v1.4.0, PHENIX v1.19.1, RELION v3.1.2, UCSF Chimera v1.14]

### A mechanism for SARS-CoV-2 RNA capping and its inhibition by nucleotide analog inhibitors. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.037 | PMCID: PMC9531661 | PMID: 36335936
- Evidence: ...https://cryosparc.com/ UCSF Chimera Pettersen et al., 2004 https://www.cgl.ucsf.edu/chimera COOT Emsley et al., 2010 https://www.cgl.ucsf.edu/chimera PHENIX Afonine et al., 2018 https://www.phenix-online.org PyMOL Schrodinger, LLC Schrodinger Other Superdex-200 10/300 Increase GE Healthcare Cat# 28990944 Superdex-75 10/300 Increase GE Healthcare Cat# 29148722 Hitrap-Q HPGE Healthcare GE Healthcare...
- Full pipeline: stage not stated [MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Evidence: ...7017235 CCP4 package Winn et al., 2011 https://doi.org/10.1107/S0907444910045749 Staraniso https://staraniso.globalphasing.org/cgi-bin/staraniso.cgic Phenix Liebschner et al., 2019 https://doi.org/10.1107/S2059798319011471 COOT Emsley and Cowtan, 2004 https://doi.org/10.1107/S0907444904019158 REFMAC Murshudov et al., 2011 https://doi.org/10.1107/S0907444911001314 CCP4i2 interface Potterton et al.,...
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### State-selective modulation of heterotrimeric Gαs signaling with macrocyclic peptides. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.019 | PMCID: PMC9747239 | PMID: 36170854
- Evidence: The structure was manually refined with Coot ( Emsley et al., 2010 ) and PHENIX ( Adams et al., 2010 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 subvariants, including BA.4 and BA.5. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.018 | PMCID: PMC9472642 | PMID: 36198317
- Evidence: .../www.mrc-lmb.cam.ac.uk/personal/peemsley/coot/ Phaser McCoy et al., 2007 https://www.phaser.cimr.cam.ac.uk/index.php/Phaser_Crystallographic_Software Phenix Adams et al., 2010 http://www.phenix-online.org/ Other Centro XS3 LB960 Berthhold Technologies N/A GloMax explorer multimode microplate reader 3500 Promega N/A FACS Canto II BD Biosciences N/A GISAID database Khare et al., 2021 https://www.gis...
- Full pipeline: stage not stated [BWA v0.7.17, ImageJ, PHENIX, PyMOL, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### A serotonergic axon-cilium synapse drives nuclear signaling to alter chromatin accessibility. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.026 | PMCID: PMC9789380 | PMID: 36055200
- Evidence: Characterization of the GRAB-HTR6-PM sensor For dose-dependent curve and selectivity tests, HEK293T cells expressing the GRAB-HTR6-PM sensor were imaged by the Opera Phenix high-content screening system.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python] -> simulation/modelling [ImageJ] -> stage not stated [Conda, Fiji, PHENIX]

### Structure of a fully assembled tumor-specific T cell receptor ligated by pMHC. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.010 | PMCID: PMC9630439 | PMID: 35985289
- Evidence: ...., 2016 github.com/MDAnalysis/mdanalysis/releases NumPy v1.19.5 Harris et al., 2020 RRID: SCR_008633 OPM database Lomize et al., 2012 RRID:SCR_011961 Phenix Liebschner et al., 2019 RRID:SCR_014224 Prism v9.2.0 N/A https://www.graphpad.com/scientific-software/prism/ PyMOL The PyMOL Molecular Graphics System, Version 2.0 Schrödinger, LLC RRID:SCR_000305 Rosetta Conway et al., 2014 RRID:SCR_015701 Ro...
- Full pipeline: simulation/modelling [ChimeraX, UCSF Chimera, VMD] -> stage not stated [CCP4, GROMACS v2020.6, MDAnalysis v0.20.1, NumPy v1.19.5, PHENIX, PyMOL]

### Structural basis of human ACE2 higher binding affinity to currently circulating Omicron SARS-CoV-2 sub-variants BA.2 and BA.1.1. (Cell 2022)

- DOI: 10.1016/j.cell.2022.06.023 | PMCID: PMC9212699 | PMID: 35809570
- Evidence: ...ownloads HKL2000 HKL Research https://www.hkl-xray.com/hkl-2000 COOT ( Emsley and Cowtan, 2004 ) http://www.mrc-lmb.cam.ac.uk/personal/peemsley/coot/ Phenix ( Adams et al., 2010 ) http://www.phenix-online.org/ MolProbity Duke Biochemistry http://molprobity.biochem.duke.edu/index.php GROMACS ( Abraham et al., 2015 ) http://www.gromacs.org/ Resource availability Lead contact Further information and ...
- Full pipeline: stage not stated [GROMACS, PHENIX, PyMOL]

### Antibody escape of SARS-CoV-2 Omicron BA.4 and BA.5 from vaccine and BA.1 serum. (Cell 2022)

- DOI: 10.1016/j.cell.2022.06.005 | PMCID: PMC9181312 | PMID: 35772405
- Evidence: Siebold) N/A Software and algorithms COOT Emsley et al., 2010 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Xia2-dials Winter et al., 2018 https://xia2.github.io PHENIX Liebschner et al., 2019 https://www.phenix-online.org/ PyMOL Warren DeLano and Sarina Bromberg https://pymol.org/ Data Acquisition Software 11.1.0.11 Fortebio https://www.fortebio.com/products/octet-systems-software Data An...
- Full pipeline: stage not stated [PHENIX, PyMOL]

### BacPROTACs mediate targeted protein degradation in bacteria. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.009 | PMCID: PMC9240326 | PMID: 35662409
- Evidence: ...019 ) http://sphire.mpg.de RELION 3.0 ( Zivanov et al., 2018 ) N/A Coot ( Emsley et al., 2010 ) https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix ( Afonine et al., 2018 ), ( Liebschner et al., 2019 ) https://phenix-online.org/ MolProbity ( Williams et al., 2018 ) http://molprobity.biochem.duke.edu/ EMRinger ( Barad et al., 2015 ) N/A UCSF Chimera ( Goddard et al., 2007 ) https://www.cgl...
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX, Coot, MotionCor2 v1.0.5, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Structure, receptor recognition, and antigenicity of the human coronavirus CCoV-HuPn-2018 spike glycoprotein. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.019 | PMCID: PMC9135795 | PMID: 35700730
- Evidence: ...3.0 ( Zivanov et al., 2018 ) https://www3.mrc-lmb.cam.ac.uk/relion Coot ( Emsley et al., 2010 ) https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix-Refine ( Liebschner et al., 2019 ) https://www.phenix-online.org/download/ Phenix-Phaser ( McCoy et al., 2007 ) https://www.phenix-online.org/download/ XDS ( Kabsch, 2010 ) http://xds.mpimf-heidelberg.mpg.de Prism 9 GraphPad Software https://w...
- Full pipeline: structure determination [PHENIX, RELION v3.0] -> stage not stated [ChimeraX, UCSF Chimera]

### Potent cross-reactive antibodies following Omicron breakthrough in vaccinees. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.014 | PMCID: PMC9120130 | PMID: 35662412
- Evidence: (2018) https://xia2.github.io/index.html PHENIX Liebschner et al.
- Full pipeline: structure determination [ChimeraX] -> stage not stated [PHENIX, PyMOL]

### Broad neutralization of SARS-CoV-2 variants by an inhalable bispecific single-domain antibody. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.009 | PMCID: PMC8907017 | PMID: 35344711
- Evidence: N/A MotionCor2 UCSF Software https://docs.google.com/forms/d/e/1FAIpQLSfAQm5MA81qTx90W9JL6ClzSrM77tytsvyyHh1ZZWrFByhmfQ/viewform PHENIX https://phenix-online.org/ N/A Living Image® Software PerkinElmer N/A ForteBio Data Analysis software Pall ForteBio LLC N/A Prism 8.0 GraphPad https://www.graphpad.com/scientific-software/prism/ PyMol PyMol N/A PDBePISA Europea Bioinformatics Institute https://www...
- Full pipeline: stage not stated [CTFFIND, ChimeraX, MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Structural and functional characterizations of infectivity and immune evasion of SARS-CoV-2 Omicron. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.019 | PMCID: PMC8786603 | PMID: 35120603
- Evidence: ...., 2018 https://www2.mrc-lmb.cam.ac.uk/relion UCSF Chimera N/A https://www.cgl.ucsf.edu/chimera UCSF ChimeraX N/A https://www.rbvi.ucsf.edu/chimerax/ PHENIX N/A https://www.phenix-online.org Coot N/A https://www2.mrc-lmb.cam.ac.uk/ Personal/pemsley/coot cryoSPARC 3.2.4 N/A https://cryosparc.com Resource availability Lead contact Further information and requests for resources and reagents should be...
- Full pipeline: structure determination [Coot] -> stage not stated [CTFFIND, ChimeraX, MotionCor2, PHENIX, RELION v3.07, UCSF Chimera, igraph v1.2.5]

### Engineered virus-like particles for efficient in vivo delivery of therapeutic proteins. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.021 | PMCID: PMC8809250 | PMID: 35021064
- Evidence: Cells were washed three times with 1xPBST and two times with PBS before imaging using an Opera Phenix High-Content Screening System (PerkinElmer).
- Full pipeline: quantification [ImageJ] -> stage not stated [PHENIX]

### Receptor binding and complex structures of human ACE2 to spike RBD from omicron and delta SARS-CoV-2. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.001 | PMCID: PMC8733278 | PMID: 35093192
- Evidence: ...jo.com/solutions/flowjo/downloads Motioncor2 Zheng et al., 2017 N/A COOT Emsley and Cowtan, 2004 http://www.mrc-lmb.cam.ac.uk/personal/peemsley/coot/ Phenix Adams et al., 2010 http://www.phenix-online.org/ MolProbity Duke Biochemistry http://molprobity.biochem.duke.edu/index.php Resource availability Lead Contact Further information and requests for resources and reagents should be directed to and...
- Full pipeline: stage not stated [MotionCor2, PHENIX, PyMOL, RELION]

### SARS-CoV-2 Omicron-B.1.1.529 leads to widespread escape from neutralizing antibody responses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.046 | PMCID: PMC8723827 | PMID: 35081335
- Evidence: ...T ( Emsley et al., 2010 ) https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Xia2-dials Winter et al., 2018 https://xia2.github.io/parameters.html PHENIX Liebschner et al., 2019 https://www.phenix-online.org/ PyMOL ( Schrödinger and DeLano, 2020 ) https://pymol.org/ Data Acquisition Software 11.1.0.11 Fortebio https://www.fortebio.com/products/octet-systems-software Data Analysis Software HT 11...
- Full pipeline: differential/statistical testing [Python v3.7] -> stage not stated [AlphaFold v0.01, PHENIX, PyMOL]

### Comprehensive structure and functional adaptations of the yeast nuclear pore complex. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.015 | PMCID: PMC8928745 | PMID: 34982960
- Evidence: We then used manual modeling in Coot ( Casañal et al., 2020 ), Chimera ( Pettersen et al., 2004 ), Phenix realspace_refine ( Afonine et al., 2018 ) and molecular dynamics flexible fitting (MDFF; ( Trabuco et al., 2008 )) to create a model based on a majority of the ~715 ɑ-helices within the spoke.
- Full pipeline: registration [IMOD] -> simulation/modelling [PHENIX] -> structure determination [PHENIX] -> stage not stated [Coot, EMAN2, ImageJ, RELION v2.0]

### Structural evolution of fibril polymorphs during amyloid assembly. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.025 | PMCID: PMC7617692 | PMID: 38134875
- Evidence: IAPP-S20G model building For each of the nine deposited cryoEM maps, a corresponding protein model was constructed or docked, iteratively edited in Coot 69 and real-space refined in Phenix 70 before repeating the model to cover three fibril layers and performing a final real-space refinement in Phenix with NCS restraints.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND v4.16, ChimeraX, Conda, PyMOL]

### Molecular basis of anaphylatoxin binding, activation, and signaling bias at complement receptors. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.020 | PMCID: PMC7615941 | PMID: 37852260
- Evidence: 68 ; Emsley and Cowtan 69 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix Liebschner et al.
- Full pipeline: stage not stated [ChimeraX, MACS2, PHENIX, RELION v3.1.2, UCSF Chimera]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: High-resolution imaging Stained sections were imaged with a Perkin Elmer Opera Phenix Plus High-Content Screening System, in confocal mode with 2 μm z-step size, using a 40X (NA 1.1, 0.149 μm/pixel) water-immersion objective.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### TMEM106B is a receptor mediating ACE2-independent SARS-CoV-2 cell entry. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.005 | PMCID: PMC10409496 | PMID: 37421949
- Evidence: 80 https://xia2.github.io/index.html Phenix Liebschner et al.
- Full pipeline: quantification [ImageJ] -> structure determination [Coot] -> machine learning [Topaz] -> stage not stated [AlphaFold, CTFFIND v1.06, PHENIX, RELION v4.0, UCSF Chimera]

### Structure of the endosomal Commander complex linked to Ritscher-Schinzel syndrome. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.003 | PMCID: PMC10187114 | PMID: 37172566
- Evidence: ...rg.mpg.de/ AIMLESS 100 http://www.ccp4.ac.uk/html/aimless.html Phaser 101 http://www.phaser.cimr.cam.ac.uk/index.php/Phaser_Crystallographic_Software Phenix 102 https://www.phenix-online.org/ Coot 103 , 104 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Molprobity 105 http://molprobity.biochem.duke.edu Pymol Schrodinger, USA. https://pymol.org/2/ ChimeraX 106 https://www.rbvi.ucsf.edu/chime...
- Full pipeline: alignment/mapping [ColabFold, MAFFT, PyMOL] -> normalisation [CCP4] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, HMMER v3.3.2, PHENIX, RELION, Topaz]

### Molecular mechanisms of stress-induced reactivation in mumps virus condensates. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.015 | PMCID: PMC10156176 | PMID: 37116470
- Version used: **1.18**
- Evidence: 87 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix 1.18-3845 Liebschner et al.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [Bioconductor] -> structure determination [Coot, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, BWA v0.7.17, ChimeraX v1.1.1, IMOD, PHENIX v1.18, Picard, R v3.6, RELION v3.0, freebayes v1.1.0, limma]

### Systemwide disassembly and assembly of SCF ubiquitin ligase complexes. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.035 | PMCID: PMC10156175 | PMID: 37028429
- Evidence: 77 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix.refine v1.19.2 Afonine et al.
- Full pipeline: structure determination [PHENIX] -> stage not stated [CTFFIND v4.1, ChimeraX v1.2, ImageJ, MotionCor2 v1.1, PyMOL v2.3.3, RELION v3.1, UCSF Chimera]

### A trailing ribosome speeds up RNA polymerase at the expense of transcript fidelity via force and allostery. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.008 | PMCID: PMC10135430 | PMID: 36931247
- Evidence: 174 For each complex, the models were then iteratively rebuilt in COOT 175 and refined using the real space refinement program in PHENIX.
- Full pipeline: alignment/mapping [ChimeraX, MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, PyMOL v1.6, RELION v3.1]

### Cryo-EM structure of gas vesicles for buoyancy-controlled motility. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.041 | PMCID: PMC9994262 | PMID: 36868215
- Version used: **1.13**
- Evidence: 44 https://bernhardcl.github.io/coot/wincoot-download.html Isolde 1.4 Croll 45 https://isolde.cimr.cam.ac.uk/download/ Phenix 1.13 Liebschner et al.
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX v1.4, ColabFold, HMMER, ImageJ, PHENIX v1.13, RELION v3.1, SciPy]

### Discovery of natural-product-derived sequanamycins as potent oral anti-tuberculosis agents. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.043 | PMCID: PMC9994261 | PMID: 36827973
- Evidence: 41 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix Afonine et al.
- Full pipeline: stage not stated [CTFFIND, MotionCor2, PHENIX, PyMOL, RELION]

### Cryo-EM structure of the RADAR supramolecular anti-phage defense complex. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.012 | PMCID: PMC9994260 | PMID: 36764290
- Version used: **1.13**
- Evidence: N/A Deposited data Ec RdrA unsplit This paper EMD: 29323, PDB: 8FNT Ec RdrA single split This paper EMD: 29324 Ec RdrA double split This paper EMD: 29325 Ss RdrA This paper EMD: 29326, PDB: 8FNU Ec RdrB This paper EMD: 29327, PDB: 8FNV Ec RdrA– Ec RdrB This paper EMD: 29328, PDB: 8FNW Oligonucleotides Primers, see Table S5 This paper N/A Software and algorithms Phenix 1.13-2998 Adams et al.
- Full pipeline: quality control [RELION] -> normalisation [MotionCor2 v1.3.1] -> registration [MotionCor2 v1.3.1] -> stage not stated [ImageJ, PHENIX v1.13]

### A potent pan-sarbecovirus neutralizing antibody resilient to epitope diversification. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.026 | PMCID: PMC11645210 | PMID: 39383863
- Evidence: Subsequent rounds of model building and refinement were performed using Coot, 83 Refmac5, 84 and Phenix.
- Full pipeline: read trimming [BCFtools v1.10.2, BWA v0.7.17] -> differential/statistical testing [RELION, scikit-learn] -> structure determination [Coot, PHENIX, Topaz] -> machine learning [Topaz, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [OpenMM, Pangolin, Python v3.10]

### Genome integrity sensing by the broad-spectrum Hachiman antiphage defense complex. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.020 | PMCID: PMC12278908 | PMID: 39395413
- Version used: **1.20.1**
- Evidence: 86 There were significant differences in nearly every region of the structure which required iterative manual refinement with a combination of Coot v0.9.4.1, 87 ISOLDE v1.6.0, 88 and Phenix 1.20.1–4487.
- Full pipeline: alignment/mapping [AlphaFold, IQ-TREE] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX v1.20.1] -> machine learning [Topaz] -> visualisation [IQ-TREE, Matplotlib, seaborn] -> stage not stated [ColabFold, MUSCLE, Python]

### Targeting Ras-, Rho-, and Rab-family GTPases via a conserved cryptic pocket. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.017 | PMCID: PMC11531380 | PMID: 39255801
- Evidence: The structure was manually refined with Coot 38 and PHENIX.
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CCP4] -> simulation/modelling [VMD] -> structure determination [PHENIX]

### Structural insights into the diversity and DNA cleavage mechanism of Fanzor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.050 | PMCID: PMC11423790 | PMID: 39208796
- Version used: **1.18**
- Evidence: Real space and reciprocal refinements were performed using PHENIX 1.18 45 .
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX v1.7, PHENIX v1.18] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, RELION v4.0, UCSF Chimera v1.16]

### Molecular mechanism of distinct chemokine engagement and functional divergence of the human Duffy antigen receptor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.005 | PMCID: PMC11349380 | PMID: 39089252
- Evidence: 94 ;Emsley and Cowtan 95 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix Liebschner et al.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> registration [MotionCor2] -> visualisation [R v3.7] -> stage not stated [AlphaFold, ChimeraX, PHENIX, RELION v4.0, UCSF Chimera]

### Natural malaria infection elicits rare but potent neutralizing antibodies to the blood-stage antigen RH5. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.037 | PMCID: PMC11383431 | PMID: 39059381
- Version used: **1.20.1**
- Evidence: Models were built and refined in cycles using COOT (0.9.3), 55 BUSTER (2.10.4) 56 and PHENIX (1.20.1-4487).
- Full pipeline: structure determination [PHENIX v1.20.1] -> visualisation [ChimeraX] -> stage not stated [CCP4, R]

### Human coronavirus HKU1 recognition of the TMPRSS2 host receptor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.006 | PMCID: PMC12854727 | PMID: 38964328
- Evidence: Validation used Molprobity 112 , Phenix 113 and Privateer 114 .
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [RELION] -> structure determination [RELION, UCSF Chimera] -> stage not stated [PHENIX, Topaz]

### Rapid DNA unwinding accelerates genome editing by engineered CRISPR-Cas9. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.031 | PMCID: PMC11658890 | PMID: 38781968
- Version used: **1.19.2**
- Evidence: 54 https://github.com/3dem/model-angelo Phenix version 1.19.2–4158 Liebschner et al.
- Full pipeline: structure determination [Coot v0.9.8.7] -> stage not stated [AlphaFold, ChimeraX v1.6.1, ColabFold, PHENIX v1.19.2, Python, Topaz, fastp]

### Mastigoneme structure reveals insights into the O-linked glycosylation code of native hydroxyproline-rich helices. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.005 | PMCID: PMC11015965 | PMID: 38552624
- Evidence: The final atomic model was refined against the C1 map using real-space refinement in Phenix 69 with Ramachandran and rotamer restraints applied.
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, ColabFold, InterProScan]

### The essential host genome for Cryptosporidium survival exposes metabolic dependencies that can be leveraged for treatment. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.001 | PMCID: PMC7618951 | PMID: 40706591
- Evidence: Fixed and stained plates were imaged using an Opera Phenix High Content Screening system (Revvity).
- Full pipeline: quality control [FastQC, ImageJ v2.1.0, kallisto] -> differential/statistical testing [DESeq2] -> stage not stated [PHENIX, STRING db v12.0]

### Molecular basis for shifted receptor recognition by an encephalitic arbovirus. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.029 | PMCID: PMC12406711 | PMID: 40187345
- Version used: **1.21r**
- Evidence: 66 The atomic model was then generated through iterative rounds of model building and adjustment in Coot (version 0.9.8.91) 67 and refined using real space refinement in Phenix (version 1.21rc1–5127).
- Full pipeline: structure determination [ChimeraX, Coot v0.9.8.91, PHENIX v1.21r, UCSF Chimera v1.6.1] -> stage not stated [AlphaFold, CTFFIND, MotionCor2 v1.6.4, PyMOL v3.0.2, RELION v3.1]

### Mechanism of DNA capture by the MukBEF SMC complex and its inhibition by a viral DNA mimic. (Cell 2025)

- DOI: 10.1016/j.cell.2025.02.032 | PMCID: PMC7617805 | PMID: 40168993
- Evidence: 73 https://cryolo.readthedocs.io/en/stable CTFFIND4 Rohou and Grigorieff 74 https://grigoriefflab.umassmed.edu/ctffind4 ISOLDE Croll 75 https://isolde.cimr.cam.ac.uk/ PHENIX V1.20 Afonine et al.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [AlphaFold, ChimeraX, MAFFT, PHENIX, RELION]

### Multiple independent acquisitions of ACE2 usage in MERS-related coronaviruses. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.031 | PMCID: PMC12360793 | PMID: 39922191
- Evidence: Validation used Molprobity 91 , Phenix 92 and Privateer 93 .
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [RELION] -> structure determination [IQ-TREE, RELION, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PHENIX, Topaz]

### Structural and functional analysis of the Nipah virus polymerase complex. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.021 | PMCID: PMC11813165 | PMID: 39837328
- Version used: **1.20.1**
- Evidence: 53 https://www.cgl.ucsf.edu/chimerax/ , RRID: SCR_015872 PyMOL 2.5.5 The PyMOL Molecular Graphics System, Version 3.0 Schrödinger, LLC. https://pymol.org/2/ , RRID: SCR_000305 Phenix 1.20.1-4487 Adams et al.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.5, Clustal Omega, Coot v0.9, MotionCor2 v1.6.4, PHENIX v1.20.1, PyMOL v2.5.5, RELION v3.1.1, UCSF Chimera v1.15]

### Accuracy mechanism of eukaryotic ribosome translocation. (Nature 2021)

- DOI: 10.1038/s41586-021-04131-9 | PMCID: PMC8674143 | PMID: 34853469
- Evidence: The initial molecular replacement solution was refined in PHENIX by rigid-body refinement with the 40S and 60S subunits treated as rigid bodies.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL]

### Cross-HLA targeting of intracellular oncoproteins with peptide-centric CARs. (Nature 2021)

- DOI: 10.1038/s41586-021-04061-6 | PMCID: PMC8599005 | PMID: 34732890
- Evidence: Model building and refinement were performed using COOT 59 and Phenix 60 , respectively.
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### A conserved mechanism for regulating replisome disassembly in eukaryotes. (Nature 2021)

- DOI: 10.1038/s41586-021-04145-3 | PMCID: PMC8695382 | PMID: 34700328
- Evidence: Extended Data Table 1 Cryo-EM statistics Model statistics generated using Phenix comprehensive validation (cryo-EM) 40 . †, refer to Extended Data Figs.
- Full pipeline: differential/statistical testing [PHENIX] -> stage not stated [UCSF Chimera]

### The structure of neurofibromin isoform 2 reveals different functional states. (Nature 2021)

- DOI: 10.1038/s41586-021-04024-x | PMCID: PMC8580823 | PMID: 34707296
- Version used: **1.19**
- Evidence: The core model as well as the GRD-Sec14-PH model were real-space refined with PHENIX v1.19-4092 real-space-refine 42 into the corresponding domain maps.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX v1.19, UCSF Chimera v1.15] -> stage not stated [ChimeraX, MotionCor2 v2.1.1, RELION v3.1.1]

### Structure of Venezuelan equine encephalitis virus in complex with the LDLRAD3 receptor. (Nature 2021)

- DOI: 10.1038/s41586-021-03963-9 | PMCID: PMC8550936 | PMID: 34646020
- Evidence: The model underwent real-space refinement in PHENIX 23 using the default parameters plus Morphing and secondary-structure, rotamer and torsion restraints with the initial model as the reference.
- Full pipeline: differential/statistical testing [RELION] -> structure determination [PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, MotionCor2]

### Structural basis of human transcription-DNA repair coupling. (Nature 2021)

- DOI: 10.1038/s41586-021-03906-4 | PMCID: PMC8514338 | PMID: 34526721
- Evidence: The model was fitted into the CSB focused refined map in Chimera 54 and rebuilt in Coot 57 , followed by real-space refinement in PHENIX 58 .
- Full pipeline: quantification [ImageJ] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, ImageJ] -> stage not stated [RELION v3.0, UCSF Chimera]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Evidence: Stained sections were imaged with a Perkin Elmer Opera Phenix High-Content Screening System, in confocal mode with 1 μm z -step size, using a 20× water-immersion objective (NA 0.16, 0.299 μm per pixel).
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Structural insights into how Prp5 proofreads the pre-mRNA branch site. (Nature 2021)

- DOI: 10.1038/s41586-021-03789-5 | PMCID: PMC8357632 | PMID: 34349264
- Version used: **1.13**
- Evidence: The entire model of the U1 snRNP, excluding Prp40, was combined and subjected to real-space refinement in PHENIX v.1.13-2998 (ref.
- Full pipeline: structure determination [PHENIX v1.13] -> stage not stated [CTFFIND, ChimeraX v1.1, Coot v0.8.9.2, RELION v3.0, UCSF Chimera v1.13.1]

### The structural basis of odorant recognition in insect olfactory receptors. (Nature 2021)

- DOI: 10.1038/s41586-021-03794-8 | PMCID: PMC8410599 | PMID: 34349260
- Evidence: The models were refined using real-space refinement implemented in PHENIX 47 for five macro-cycles with four-fold non-crystallographic symmetry applied and secondary structure restraints applied.
- Full pipeline: alignment/mapping [MAFFT, MotionCor2, RELION v3.0] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [scikit-learn] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, PyMOL]

### Structural basis of early translocation events on the ribosome. (Nature 2021)

- DOI: 10.1038/s41586-021-03713-x | PMCID: PMC8318882 | PMID: 34234344
- Version used: **1.19**
- Evidence: ... refined through iterative rounds of manual model building in Coot (v.0.9.4.1) 64 , refinement of RNA with ERRASER 65 and real-space refinement using Phenix (v.1.19-4092) 66 . mRNA nucleotide 40 corresponds to the +1 position.
- Full pipeline: normalisation [UCSF Chimera] -> registration [MotionCor2] -> differential/statistical testing [UCSF Chimera] -> structure determination [Coot v0.9.4.1, PHENIX v1.19, RELION, UCSF Chimera] -> visualisation [ChimeraX]

### Nanobodies from camelid mice and llamas neutralize SARS-CoV-2 variants. (Nature 2021)

- DOI: 10.1038/s41586-021-03676-z | PMCID: PMC8260353 | PMID: 34098567
- Evidence: The coordinates were then fit to the electron density more precisely through an iterative process of manual fitting using Coot and real space refinement within Phenix, Molprobity and EMRinger were used to check geometry and evaluate structures at each iteration step.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [UCSF Chimera, fastp]

### Structure and dynamics of a mycobacterial type VII secretion system. (Nature 2021)

- DOI: 10.1038/s41586-021-03517-z | PMCID: PMC8131196 | PMID: 33981042
- Evidence: Model free density modification in Phenix.Resolve_Cryo_EM 22 further improved the resolution to 4.3 Å and 5.8 Å, respectively.
- Full pipeline: structure determination [ChimeraX v1.0, RELION] -> visualisation [PyMOL v2.40] -> stage not stated [MotionCor2, PHENIX]

### Structural basis of GABA<sub>B</sub> receptor-G<sub>i</sub> protein coupling. (Nature 2021)

- DOI: 10.1038/s41586-021-03507-1 | PMCID: PMC8222003 | PMID: 33911284
- Evidence: The docked model was subjected to flexible fitting using Rosetta 45 and was further rebuilt in Coot 45 and real-space-refined in Rosetta 45 and Phenix 44 .
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, RELION v3.1]

### A biosensor for the direct visualization of auxin. (Nature 2021)

- DOI: 10.1038/s41586-021-03425-2 | PMCID: PMC8081663 | PMID: 33828298
- Evidence: Molecular replacement was performed with Phenix using the coordinates of wild-type TrpR (PDB ID: 1WRP 32 or 1TRO 33 ) as search model.
- Full pipeline: stage not stated [ImageJ, PHENIX]

### Structural basis of malaria RIFIN binding by LILRB1-containing antibodies. (Nature 2021)

- DOI: 10.1038/s41586-021-03378-6 | PMCID: PMC8068667 | PMID: 33790470
- Evidence: The coordinates were then fit to the electron density more precisely through an iterative process of manual fitting using Coot 21 and real space refinement within Phenix 22 , Molprobity 23 and EMRinger 24 were used to check geometry and evaluate structures at each iteration step.
- Full pipeline: differential/statistical testing [R] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MACS2, UCSF Chimera]

### Structural and biochemical mechanisms of NLRP1 inhibition by DPP9. (Nature 2021)

- DOI: 10.1038/s41586-021-03320-w | PMCID: PMC8081665 | PMID: 33731929
- Evidence: The model from the molecular replacement was manually rebuilt to the sequence of rNLRP1 FIIND in the program Coot 41 and subsequently subjected to refinement by the program Refine_Phenix 42 .
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [MotionCor2, PHENIX] -> stage not stated [ImageJ, RELION v3.1]

### Structure and inhibition mechanism of the human citrate transporter NaCT. (Nature 2021)

- DOI: 10.1038/s41586-021-03230-x | PMCID: PMC7933130 | PMID: 33597751
- Evidence: Model building and refinement All maps were sharpened using Auto-sharpen Map in Phenix 66 , built in Coot 67 , and refined in Phenix real space refine 66 .
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [MotionCor2, Topaz]

### Ubiquitin ligation to F-box protein targets by SCF-RBR E3-E3 super-assembly. (Nature 2021)

- DOI: 10.1038/s41586-021-03197-9 | PMCID: PMC7904520 | PMID: 33536622
- Evidence: COOT70 63 was used for manual modelling and Phenix.refine71 64 was used for real space refinement.
- Full pipeline: alignment/mapping [RELION v3.00] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [CTFFIND]

### Structure of the class D GPCR Ste2 dimer coupled to two G proteins. (Nature 2021)

- DOI: 10.1038/s41586-020-2994-1 | PMCID: PMC7116888 | PMID: 33268889
- Evidence: Model building and refinement were performed using the CCP-EM 48 and PHENIX 49 software suites.
- Full pipeline: alignment/mapping [CCP4] -> registration [MotionCor2] -> simulation/modelling [GROMACS] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [RELION]

### Close relatives of MERS-CoV in bats use ACE2 as their functional receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-05513-3 | PMCID: PMC9734910 | PMID: 36477529
- Version used: **1.19**
- Evidence: The atomic models were further refined by positional and B -factor refinement in real space using Phenix (v.1.19) 59 .
- Full pipeline: alignment/mapping [CTFFIND, Clustal Omega, MUSCLE] -> structure determination [Coot v0.9.4, PHENIX v1.19, RELION, UCSF Chimera v1.15] -> stage not stated [ChimeraX v1.1, MotionCor2 v1.3.0]

### Structural basis of tankyrase activation by polymerization. (Nature 2022)

- DOI: 10.1038/s41586-022-05449-8 | PMCID: PMC9712121 | PMID: 36418402
- Version used: **1.18.2**
- Evidence: Model building, refinement and validation To aid model building, the post-processed map was locally sharpened using Phenix Autosharpen (from Phenix v1.18.2-3874) 47 using a high-resolution cut-off of 3.0 Å.
- Full pipeline: alignment/mapping [Clustal Omega, EMAN2 v2.31] -> quantification [ImageJ] -> normalisation [ImageJ] -> structure determination [PHENIX v1.18.2] -> visualisation [ChimeraX v1.3] -> stage not stated [CellProfiler, Coot, MotionCor2, RELION v2.10, UCSF Chimera v1.14]

### Direct activation of a bacterial innate immune system by a viral capsid protein. (Nature 2022)

- DOI: 10.1038/s41586-022-05444-z | PMCID: PMC9712102 | PMID: 36385533
- Evidence: The MR solution from Phaser was used in combination with Rosetta as implemented in the MR-Rosetta 61 suit from the Phenix package 62 .
- Full pipeline: alignment/mapping [MAFFT, MUSCLE] -> stage not stated [AlphaFold, BLAST, CCP4, PHENIX]

### Cryo-EM structure of the SEA complex. (Nature 2022)

- DOI: 10.1038/s41586-022-05370-0 | PMCID: PMC9646525 | PMID: 36289347
- Version used: **1.20.1**
- Evidence: 41 ) and real-space refinement in Phenix v.1.20.1-4487 (ref.
- Full pipeline: quantification [ImageJ v1.52p] -> structure determination [PHENIX v1.20.1] -> visualisation [ChimeraX v1.3] -> stage not stated [AlphaFold, Coot v0.9.8.1, RELION v4.0, UCSF Chimera v1.15]

### Bending forces and nucleotide state jointly regulate F-actin structure. (Nature 2022)

- DOI: 10.1038/s41586-022-05366-w | PMCID: PMC9646526 | PMID: 36289330
- Evidence: These models, containing three actin protomers with associated ADP, and Mg 2+ (and PO 4 3− ) ligands were refined using PHENIX real-space refinement 74 with non-crystallographic symmetry (NCS) restraints.
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [Python] -> differential/statistical testing [Matplotlib] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX, RELION] -> machine learning [TensorFlow, cryoDRGN] -> stage not stated [Coot, EMAN2, UCSF Chimera, scikit-image]

### Clathrin-associated AP-1 controls termination of STING signalling. (Nature 2022)

- DOI: 10.1038/s41586-022-05354-0 | PMCID: PMC9605868 | PMID: 36261523
- Evidence: The pSTING tail was docked against the cryo-EM map in Coot and the whole model was refined in PHENIX.
- Full pipeline: quantification [Harmony v4.9] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera]

### Structures of the TMC-1 complex illuminate mechanosensory transduction. (Nature 2022)

- DOI: 10.1038/s41586-022-05314-8 | PMCID: PMC9605866 | PMID: 36224384
- Evidence: Structure determination and model building The initial electron microscopy density map was sharpened with Phenix AutoSharpen 55 , and both sharpened and unsharpened maps were used for structure determination.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [ChimeraX, PHENIX] -> stage not stated [NAMD, UCSF Chimera, VMD]

### Structure of the OMEGA nickase IsrB in complex with ωRNA and target DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05324-6 | PMCID: PMC9581776 | PMID: 36224386
- Evidence: One of the top ten scoring models was selected for further refinement by ISOLDE and Phenix 6 , together with the protein model, to optimize the geometry and improve the fit to the cryo-EM density.
- Full pipeline: alignment/mapping [MAFFT, MotionCor2] -> structure determination [ColabFold, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND, Python]

### Visualizing translation dynamics at atomic detail inside a bacterial cell. (Nature 2022)

- DOI: 10.1038/s41586-022-05255-2 | PMCID: PMC9534751 | PMID: 36171285
- Evidence: Homology models were rigid-body-fitted into the cryo-ET densities using Chimera 63 , followed by iterative refinement using PHENIX real-space refinement 64 and manual adjustment in Coot 65 .
- Full pipeline: alignment/mapping [MAFFT, eggNOG] -> dimensionality reduction/clustering [eggNOG] -> structure determination [Coot, PHENIX, Python v3.7.7] -> visualisation [ChimeraX] -> stage not stated [RELION v3.0]

### Structure of the Ebola virus polymerase complex. (Nature 2022)

- DOI: 10.1038/s41586-022-05271-2 | PMCID: PMC9517992 | PMID: 36171293
- Evidence: The initial coordinates were refined against the corresponding maps using PHENIX 60 with secondary-structure restraints and Ramachandran restraints applied.
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [ImageJ] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold]

### A wheat resistosome defines common principles of immune receptor channels. (Nature 2022)

- DOI: 10.1038/s41586-022-05231-w | PMCID: PMC9581773 | PMID: 36163289
- Version used: **1.18.2**
- Evidence: Model building and refinement The final density map was obtained by merging the global map and the local map which contained LRR and AvrSr35, using a ‘combine_focused_map’ in PHENIX 1.18.2 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX v1.15, PHENIX v1.18.2] -> visualisation [ChimeraX v1.15] -> stage not stated [AlphaFold, RELION v3.1]

### Structural basis for directional chitin biosynthesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05244-5 | PMCID: PMC9556331 | PMID: 36131020
- Evidence: The dimeric structure was real-space refined using Phenix 49 in C2 symmetry.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2019.3] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, RELION v3.08]

### Mechanism of AAA+ ATPase-mediated RuvAB-Holliday junction branch migration. (Nature 2022)

- DOI: 10.1038/s41586-022-05121-1 | PMCID: PMC9477746 | PMID: 36002576
- Evidence: Finally, the resulting coordinate files were refined with Phenix.real_space_refine (v1.19.1-4122) 72 using reference model restraints, strict rotamer matching and disabled grid search settings.
- Full pipeline: simulation/modelling [ChimeraX v1.2.5] -> structure determination [ChimeraX v1.2.5, PHENIX] -> visualisation [PyMOL v2.4.1] -> stage not stated [RELION v3.0b, UCSF Chimera v1.13]

### R-loop formation and conformational activation mechanisms of Cas9. (Nature 2022)

- DOI: 10.1038/s41586-022-05114-0 | PMCID: PMC9433323 | PMID: 36002571
- Evidence: Phases were obtained by molecular replacement using the Phaser module of the Phenix package 48 using the NUC lobe of the PDB ID: 5FQ5 as initial search model.
- Full pipeline: visualisation [ChimeraX] -> stage not stated [PHENIX]

### The mechanism of RNA capping by SARS-CoV-2. (Nature 2022)

- DOI: 10.1038/s41586-022-05185-z | PMCID: PMC9492545 | PMID: 35944563
- Evidence: The model was manually rebuilt into the map using Coot 52 , and refined using Phenix real space refinement 53 .
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX, RELION] -> stage not stated [CTFFIND, ImageJ]

### Architecture and self-assembly of the jumbo bacteriophage nuclear shell. (Nature 2022)

- DOI: 10.1038/s41586-022-05013-4 | PMCID: PMC9365700 | PMID: 35922510
- Evidence: Coordinate model building and refinement Initial monomer models were generated via the DeepTracer web server 49 followed by manual building in COOT-v0.9.1 50 and subjected to real-space refinement in PHENIX-v1.19.2 51 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [ChimeraX, MDTraj, PyMOL, VMD] -> structure determination [ChimeraX, PHENIX, PyMOL, VMD] -> visualisation [ChimeraX, PyMOL, VMD] -> stage not stated [UCSF Chimera]

### Structural insights into auxin recognition and efflux by Arabidopsis PIN1. (Nature 2022)

- DOI: 10.1038/s41586-022-05143-9 | PMCID: PMC9477737 | PMID: 35917925
- Evidence: Structure refinements were carried out by PHENIX in real space 51 .
- Full pipeline: registration [MotionCor2, RELION v3.1] -> structure determination [PHENIX]

### A physical wiring diagram for the human immune system. (Nature 2022)

- DOI: 10.1038/s41586-022-05028-x | PMCID: PMC9365698 | PMID: 35922511
- Evidence: These were then imaged at 20× magnification on a Perkin Elmer Opera Phenix High Content Screening System with water immersion.
- Full pipeline: differential/statistical testing [DESeq2, Seurat] -> stage not stated [CellProfiler, PHENIX, Python, R v1.0.0, Scanpy, igraph]

### Discovery, structure and mechanism of a tetraether lipid synthase. (Nature 2022)

- DOI: 10.1038/s41586-022-05120-2 | PMCID: PMC9433317 | PMID: 35882349
- Evidence: Phenix.autobuild was used to generate an initial model of 366 residues out of 506 with an Rwork/Rfree of 0.30/0.37.
- Full pipeline: structure determination [Coot] -> visualisation [Cytoscape, PyMOL] -> stage not stated [AlphaFold, PHENIX]

### Organizing structural principles of the IL-17 ligand-receptor axis. (Nature 2022)

- DOI: 10.1038/s41586-022-05116-y | PMCID: PMC9477748 | PMID: 35863378
- Evidence: Models were then refined using rigid-body refinement with Phenix 48 followed by refinement with ISOLDE 49 , and further iterative manual building and refinement in Coot 50 and Phenix.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX, UCSF Chimera] -> stage not stated [PyMOL]

### Archaic chaperone-usher pili self-secrete into superelastic zigzag springs. (Nature 2022)

- DOI: 10.1038/s41586-022-05095-0 | PMCID: PMC9452303 | PMID: 35853476
- Version used: **1.8.2**
- Evidence: The structure was refined by combining manual adjustments in Coot and real space refinement in PHENIX (v.1.8.2) 38 .
- Full pipeline: quantification [ImageJ v1.53k] -> registration [MotionCor2 v1.2.3] -> structure determination [MotionCor2 v1.2.3, PHENIX v1.8.2, RELION v3.0.8, UCSF Chimera] -> stage not stated [CTFFIND v4.1.13, Coot v0.9.4]

### Cryo-EM structure of an active bacterial TIR-STING filament complex. (Nature 2022)

- DOI: 10.1038/s41586-022-04999-1 | PMCID: PMC9402430 | PMID: 35859168
- Evidence: Multiple rounds of Phenix real-space refine 32 was applied with manual correction in Coot in between.
- Full pipeline: registration [MotionCor2 v1.4.0] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, RELION]

### Structure of the MRAS-SHOC2-PP1C phosphatase complex. (Nature 2022)

- DOI: 10.1038/s41586-022-05086-1 | PMCID: PMC9452295 | PMID: 35830882
- Evidence: The final model was built in the Coot molecular graphics application 44 and refined in Phenix 45 .
- Full pipeline: structure determination [PHENIX] -> stage not stated [Bioconductor, R]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Evidence: Stained sections were imaged with a Perkin Elmer Opera Phenix High-Content Screening System, in confocal mode with 1 μm z-step size, using a ×20 (numerical aperture (NA) 0.16, 0.299 μm per pixel), ×40 (NA 1.1, 0.149 μm per pixel) or ×63 (NA 1.15, 0.091 μm per pixel) water-immersion objectives.
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### Structure of the Dicer-2-R2D2 heterodimer bound to a small RNA duplex. (Nature 2022)

- DOI: 10.1038/s41586-022-04790-2 | PMCID: PMC9279153 | PMID: 35768503
- Evidence: The structures were validated using MolProbity 50 from the PHENIX package.
- Full pipeline: structure determination [ChimeraX] -> stage not stated [AlphaFold, Clustal Omega, PHENIX, RELION]

### Structural insights into dsRNA processing by Drosophila Dicer-2-Loqs-PD. (Nature 2022)

- DOI: 10.1038/s41586-022-04911-x | PMCID: PMC9279154 | PMID: 35768513
- Evidence: Finally, all of the models were refined against the EM map by PHENIX 42 in real space with secondary structure and geometry restraints.
- Full pipeline: structure determination [PHENIX] -> stage not stated [RELION v3.1]

### A peroxisomal ubiquitin ligase complex forms a retrotranslocation channel. (Nature 2022)

- DOI: 10.1038/s41586-022-04903-x | PMCID: PMC9279156 | PMID: 35768507
- Evidence: Structural model building, refinement and analysis All models were built in Coot 50 and refined in PHENIX 51 using the 3.1 Å sharpened density map.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, REFMAC, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.1]

### Structures and mechanism of the plant PIN-FORMED auxin transporter. (Nature 2022)

- DOI: 10.1038/s41586-022-04883-y | PMCID: PMC9477730 | PMID: 35768502
- Evidence: Models could be further improved by iterative manual model building in Coot combined with real-space refinement using Phenix, initially with an Amber force-field molecular dynamic refinement 45 .
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [PHENIX, RoseTTAFold] -> visualisation [PyMOL] -> stage not stated [Coot]

### Structural basis for SHOC2 modulation of RAS signalling. (Nature 2022)

- DOI: 10.1038/s41586-022-04838-3 | PMCID: PMC9452301 | PMID: 35768504
- Evidence: The refinement and building were undertaken with Phenix 58 Real Space Refine and COOT 59 respectively.
- Full pipeline: structure determination [ChimeraX, PHENIX] -> machine learning [CCP4] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Cryo-EM structure of a type IV secretion system. (Nature 2022)

- DOI: 10.1038/s41586-022-04859-y | PMCID: PMC9259494 | PMID: 35732732
- Version used: **1.18.2**
- Evidence: All maps used for model building were subjected to sharpening using AutoSharpen in Phenix v1.18.2 53 and local resolution estimated using cryoSPARC.
- Full pipeline: registration [CTFFIND v4.1] -> simulation/modelling [Coot] -> structure determination [Coot, PHENIX v1.18.2, RELION v3.1] -> machine learning [AlphaFold] -> stage not stated [ChimeraX v1.1, HMMER, PyMOL v2.3.2]

### BA.2.12.1, BA.4 and BA.5 escape antibodies elicited by Omicron infection. (Nature 2022)

- DOI: 10.1038/s41586-022-04980-y | PMCID: PMC9385493 | PMID: 35714668
- Version used: **1.20**
- Evidence: Coot (v0.8.9.2) 56 and Phenix (v1.20) 57 were used for structural modelling and refinement.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> simulation/modelling [GROMACS] -> structure determination [PHENIX v1.20, RELION v3.1, UCSF Chimera v1.16] -> visualisation [ChimeraX v1.3, R, Seurat] -> stage not stated [Pangolin, ggplot2 v3.3.3, scikit-learn]

### Mechanism of replication origin melting nucleated by CMG helicase assembly. (Nature 2022)

- DOI: 10.1038/s41586-022-04829-4 | PMCID: PMC9242855 | PMID: 35705812
- Evidence: The final RELION half-maps were used to produce a density modified map using the PHENIX Resolve CryoEM (refs.
- Full pipeline: structure determination [Coot v0.9.1] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [CTFFIND, PHENIX, RELION]

### Mechanism of mitoribosomal small subunit biogenesis and preinitiation. (Nature 2022)

- DOI: 10.1038/s41586-022-04795-x | PMCID: PMC9200640 | PMID: 35676484
- Evidence: Final models were subjected to refinement of energy minimization and atomic displacement parameters (ADP) estimation by Phenix.real_space_refine v1.18 (ref.
- Full pipeline: registration [RELION v3.0] -> differential/statistical testing [limma v3.34.9] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CCP4 v7.0, ChimeraX v0.91]

### Discovery of non-squalene triterpenes. (Nature 2022)

- DOI: 10.1038/s41586-022-04773-3 | PMCID: PMC9177416 | PMID: 35650436
- Version used: **1.19.2**
- Evidence: Molecular replacement was performed with Phaser in PHENIX (version 1.19.2-4158-000) 51 , 52 .
- Full pipeline: alignment/mapping [Clustal Omega v2.0.12, RELION] -> visualisation [PyMOL] -> stage not stated [AlphaFold, AutoDock Vina, CTFFIND, PHENIX v1.19.2, UCSF Chimera]

### Structural insights into the HBV receptor and bile acid transporter NTCP. (Nature 2022)

- DOI: 10.1038/s41586-022-04857-0 | PMCID: PMC9242859 | PMID: 35580630
- Evidence: The entire structure was further manually adjusted and refined using PHENIX 36 with phenix.real_space refine.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.2.1, PyMOL v2.3, UCSF Chimera v1.15] -> stage not stated [RELION]

### Structural basis of sodium-dependent bile salt uptake into the liver. (Nature 2022)

- DOI: 10.1038/s41586-022-04723-z | PMCID: PMC9242856 | PMID: 35545671
- Evidence: All atomic models were refined using PHENIX 67 .
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [Coot]

### USP14-regulated allostery of the human proteasome by time-resolved cryo-EM. (Nature 2022)

- DOI: 10.1038/s41586-022-04671-8 | PMCID: PMC9117149 | PMID: 35477760
- Evidence: After manually rebuilding, atomic models were all subjected to the real-space refinement in Phenix 58 .
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, Coot, EMAN2, MotionCor2, RELION]

### Reversible RNA phosphorylation stabilizes tRNA for cellular thermotolerance. (Nature 2022)

- DOI: 10.1038/s41586-022-04677-2 | PMCID: PMC9095486 | PMID: 35477761
- Evidence: The model was further modified with Coot 61 and refined with Phenix 62 .
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [PHENIX, PyMOL] -> visualisation [PyMOL]

### Opening of glutamate receptor channel to subconductance levels. (Nature 2022)

- DOI: 10.1038/s41586-022-04637-w | PMCID: PMC9068512 | PMID: 35444281
- Version used: **1.18**
- Evidence: The models were tested for overfitting by shifting their coordinates by 0.5 Å (using shake) in Phenix 1.18 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot v0.9.2] -> stage not stated [CTFFIND v1.06, PHENIX v1.18, RELION v3.1, UCSF Chimera v1.14, VMD v1.9.3]

### Structural basis of tethered agonism of the adhesion GPCRs ADGRD1 and ADGRF1. (Nature 2022)

- DOI: 10.1038/s41586-022-04580-w | PMCID: PMC9046087 | PMID: 35418679
- Evidence: Each model was docked into the corresponding cryo-EM density map by ChimeraX v.1.1 45 , followed by iterative manual adjustment in Coot 46 and real-space refinement in phenix.real_space_refine of PHENIX 47 .
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, ChimeraX v1.1, Coot, PHENIX] -> visualisation [PyMOL v1.8, UCSF Chimera v1.15] -> stage not stated [CTFFIND v1.18, RELION v3.1]

### Phage anti-CBASS and anti-Pycsar nucleases subvert bacterial immunity. (Nature 2022)

- DOI: 10.1038/s41586-022-04716-y | PMCID: PMC9117128 | PMID: 35395152
- Evidence: For Acb1 and Apyc1 phase determination, anomalous data were collected using selenomethionine-labelled Acb1 crystals, heavy sites were identified with HySS in Phenix (ref.
- Full pipeline: read trimming [Cutadapt v2.8, SPAdes] -> visualisation [PyMOL v2.3.0] -> stage not stated [BLAST, IQ-TREE, PHENIX]

### Design of protein-binding proteins from the target structure alone. (Nature 2022)

- DOI: 10.1038/s41586-022-04654-9 | PMCID: PMC9117152 | PMID: 35332283
- Evidence: Refinement was carried out in Phenix 54 , alternating with manual rebuilding and adjustment in COOT 55 .
- Full pipeline: quantification [ImageJ] -> normalisation [CCP4] -> structure determination [Coot, PHENIX] -> stage not stated [PyMOL]

### Activation mechanism of the class D fungal GPCR dimer Ste2. (Nature 2022)

- DOI: 10.1038/s41586-022-04498-3 | PMCID: PMC8942848 | PMID: 35296853
- Evidence: Portions of the receptor that differed from the initial model were rebuilt manually in COOT 53 followed by iterative rounds of refinements in CCP-EM 54 and PHENIX 55 software suites and manual model building in COOT.
- Full pipeline: registration [MotionCor2] -> differential/statistical testing [RELION] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, MotionCor2, PHENIX, RELION] -> visualisation [PyMOL] -> stage not stated [CTFFIND, UCSF Chimera]

### Structural basis for mismatch surveillance by CRISPR-Cas9. (Nature 2022)

- DOI: 10.1038/s41586-022-04470-1 | PMCID: PMC8907077 | PMID: 35236982
- Evidence: Further modelling was performed using Isolde 40 , and the models were ultimately subjected to real-space refinement as implemented in PHENIX.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX]

### Mechanisms of inhibition and activation of extrasynaptic αβ GABA<sub>A</sub> receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-04402-z | PMCID: PMC8850191 | PMID: 35140402
- Evidence: The model was docked into the cryo-EM density map using the dock_in_map program, PHENIX suite 59 .
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [UCSF Chimera]

### Memory B cell repertoire from triple vaccinees against diverse SARS-CoV-2 variants. (Nature 2022)

- DOI: 10.1038/s41586-022-04466-x | PMCID: PMC8967717 | PMID: 35090164
- Evidence: ...mera, followed by manually adjustment and correction according to the protein sequences and densities in Coot, as well as real space refinement using Phenix.
- Full pipeline: registration [RELION v3.0] -> simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND]

### Structural insights into inhibitor regulation of the DNA repair protein DNA-PKcs. (Nature 2022)

- DOI: 10.1038/s41586-021-04274-9 | PMCID: PMC8791830 | PMID: 34987222
- Evidence: The template was first rigid-body-fitted into the maps in CHIMERA and CHIMERAX followed by real-space refinement in PHENIX 40 – 42 .
- Full pipeline: structure determination [PHENIX]

### Broadly neutralizing antibodies target a haemagglutinin anchor epitope. (Nature 2022)

- DOI: 10.1038/s41586-021-04356-8 | PMCID: PMC8828479 | PMID: 34942633
- Evidence: The final model and map were evaluated using MolProbity, EMRinger 68 , 69 , Phenix and the PDB validation server.
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION, UCSF Chimera] -> simulation/modelling [GROMACS, PLUMED] -> visualisation [RELION] -> stage not stated [Jupyter, PHENIX, R, Seurat]

### Activation mechanism of PINK1. (Nature 2022)

- DOI: 10.1038/s41586-021-04340-2 | PMCID: PMC8828467 | PMID: 34933320
- Version used: **1.19.2**
- Evidence: Data were merged using AIMLESS (v.0.5.21) 46 implemented in CCP4i (v.7.0.001) 47 and molecular replacement was performed using PHASER (v.2.8.3) 48 implemented in Phenix (v.1.19.2-4158) 49 using Ph PINK1 from the Ph PINK1–Ub TVLN complex (PDB: 6EQI ) 10 as the search model.
- Full pipeline: structure determination [Coot v0.9] -> visualisation [ChimeraX v1.1.1] -> stage not stated [AlphaFold, ColabFold, EMAN2, Fiji v1.53k, ImageJ v1.53k, PHENIX v1.19.2, RELION v3.1, UCSF Chimera]

### FOXP3 recognizes microsatellites and bridges DNA through multimerization. (Nature 2023)

- DOI: 10.1038/s41586-023-06793-z | PMCID: PMC10719092 | PMID: 38030726
- Evidence: The structure validation was performed using MolProbity 51 from the PHENIX package.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> registration [MotionCor2] -> differential/statistical testing [DESeq2] -> structure determination [RELION v4.0.1, UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [BEDTools, CTFFIND v4.1, HOMER, MACS2, PHENIX]

### Intermediate conformations of CD4-bound HIV-1 Env heterotrimers. (Nature 2023)

- DOI: 10.1038/s41586-023-06639-8 | PMCID: PMC10686819 | PMID: 37993719
- Version used: **1.17.1**
- Evidence: Iterative rounds of whole-complex refinements using Phenix v.1.17.1 (phenix.real_space_refine) 59 , 60 and Coot v.0.8.9.1 (ref.
- Full pipeline: structure determination [ChimeraX v1.2.5, Coot v0.8.9.1, PHENIX v1.17.1] -> visualisation [PyMOL v2.4.0]

### Structural insights into intron catalysis and dynamics during splicing. (Nature 2023)

- DOI: 10.1038/s41586-023-06746-6 | PMCID: PMC10733145 | PMID: 37993708
- Version used: **1.20.1**
- Evidence: The final pre-1F, pre-2F and post-2F models were improved by iterative rounds of real-space refinement against the sharpened cryoEM map in PHENIX (Phenix v.1.20.1-4487) using secondary structure restraints for RNA, protein and DNA, as well Ramachandran and rotamer restraints for protein chains and subsequent rebuilding in COOT 46 – 48 .
- Full pipeline: structure determination [ChimeraX v1.2.5, PHENIX v1.20.1, UCSF Chimera] -> stage not stated [PyMOL v2.6.0, Topaz]

### Stress granules plug and stabilize damaged endolysosomal membranes. (Nature 2023)

- DOI: 10.1038/s41586-023-06726-w | PMCID: PMC10686833 | PMID: 37968398
- Evidence: The plate was sealed with parafilm and placed in a pre-heated (37 °C) Opera Phenix microscope with a 40× or 60× water-immersion lens (PerkinElmer) with 5% CO 2 .
- Full pipeline: dimensionality reduction/clustering [Python] -> stage not stated [Fiji, ImageJ, MACS2, PHENIX, R v3.0]

### Targeting of intracellular oncoproteins with peptide-centric CARs. (Nature 2023)

- DOI: 10.1038/s41586-023-06706-0 | PMCID: PMC10665195 | PMID: 37938771
- Evidence: Model building and refinement were performed using COOT 60 and Phenix 61 , respectively.
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Structure and electromechanical coupling of a voltage-gated Na&lt;sup&gt;+&lt;/sup&gt;/H&lt;sup&gt;+&lt;/sup&gt; exchanger. (Nature 2023)

- DOI: 10.1038/s41586-023-06518-2 | PMCID: PMC10620092 | PMID: 37880360
- Evidence: The structure was refined using real-space refinement in Phenix 58 .
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX] -> stage not stated [PyMOL]

### Structures of a sperm-specific solute carrier gated by voltage and cAMP. (Nature 2023)

- DOI: 10.1038/s41586-023-06629-w | PMCID: PMC10620091 | PMID: 37880361
- Version used: **1.20.1**
- Evidence: 71 ) followed by refinement in Phenix v.1.20.1-4487 (ref.
- Full pipeline: registration [MotionCor2 v1.4.0] -> structure determination [PHENIX v1.20.1] -> stage not stated [ChimeraX v1.6.1, PyMOL v2.5.5, RELION v3.1.0]

### Structures illustrate step-by-step mitochondrial transcription initiation. (Nature 2023)

- DOI: 10.1038/s41586-023-06643-y | PMCID: PMC10600007 | PMID: 37821701
- Version used: **1.19.2**
- Evidence: Model building was coupled with iterative rounds of real-space structure refinement using Phenix 1.19.2 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.19.2] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, RELION v3.1]

### Sialoglycan binding triggers spike opening in a human coronavirus. (Nature 2023)

- DOI: 10.1038/s41586-023-06599-z | PMCID: PMC10700143 | PMID: 37794193
- Evidence: Models were refined by carrying out iterative cycles of manual model building using Coot 48 and real-space refinement using Phenix 49 .
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CCP4, RELION v3.1.1, VMD]

### Inactivation of the Kv2.1 channel through electromechanical coupling. (Nature 2023)

- DOI: 10.1038/s41586-023-06582-8 | PMCID: PMC10567553 | PMID: 37758949
- Version used: **1.19.1**
- Evidence: The model was then manually built in Coot (v.0.9.8.1) 70 and refined using real space refinement in PHENIX (v.1.19.1) 71 with secondary structure and geometry restraints.
- Full pipeline: structure determination [Coot v0.9.8.1, PHENIX v1.19.1, UCSF Chimera v1.15] -> visualisation [PyMOL v2.4.1] -> stage not stated [MDAnalysis, MotionCor2, RELION v3.0]

### piRNA processing by a trimeric Schlafen-domain nuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06588-2 | PMCID: PMC10567574 | PMID: 37758951
- Evidence: Molecular replacement was performed using Phaser 63 within Phenix 64 .
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt v4.0] -> alignment/mapping [BEDTools, SAMtools v1.10, featureCounts v2.0.0] -> differential/statistical testing [ggplot2] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, ColabFold, ImageJ, PHENIX]

### Structural mobility tunes signalling of the GluA1 AMPA glutamate receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06528-0 | PMCID: PMC10533411 | PMID: 37704721
- Evidence: Model building and refinement for high-resolution systems were performed using Coot 58 , PHENIX 59 real-space refinement and Refmac-Servalcat 60 .
- Full pipeline: structure determination [Coot, PHENIX, Python, RELION] -> stage not stated [AlphaFold, ChimeraX, MotionCor2, PyMOL, UCSF Chimera]

### Tail engagement of arrestin at the glucagon receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06420-x | PMCID: PMC10447241 | PMID: 37558880
- Evidence: 57 ) and refined by several rounds of real-space refinement in PHENIX 58 .
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [Coot v0.8.9]

### Diverse modes of H3K36me3-guided nucleosomal deacetylation by Rpd3S. (Nature 2023)

- DOI: 10.1038/s41586-023-06349-1 | PMCID: PMC10432269 | PMID: 37468628
- Evidence: The models were refined in real space using Phenix 53 .
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, RELION, UCSF Chimera]

### A common allele of HLA is associated with asymptomatic SARS-CoV-2 infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06331-x | PMCID: PMC10396966 | PMID: 37468623
- Version used: **1.20.1**
- Evidence: Manual model building was conducted using COOT 70 followed by refinement with BUSTER 71 and PHENIX (v.1.20.1-4487) 72 .
- Full pipeline: variant calling [R] -> structure determination [PHENIX v1.20.1] -> stage not stated [CCP4, MACS2, PyMOL v2.5]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Evidence: Stained sections were imaged using a Perkin Elmer Opera Phenix High-Content Screening System with a ×20 water-immersion objective (NA of 0.16, 0.299 μm per pixel).
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### Cooperation between bHLH transcription factors and histones for DNA access. (Nature 2023)

- DOI: 10.1038/s41586-023-06282-3 | PMCID: PMC10338342 | PMID: 37407816
- Evidence: For the NCP SHL–6.2 -CLOCK-BMAL1 map, a composite map of two refinements was generated using combine_focus_maps implementation in PHENIX 87 .
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bioconductor, Bowtie2, ChimeraX, PyMOL] -> structure determination [PHENIX] -> stage not stated [Coot v0.9.6, ImageJ, RELION, SAMtools v1.6]

### Fanzor is a eukaryotic programmable RNA-guided endonuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06356-2 | PMCID: PMC10432273 | PMID: 37380027
- Version used: **1.18**
- Evidence: Real space and reciprocal refinements were performed using PHENIX 1.18 (ref.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> registration [MotionCor2] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.4, PHENIX v1.18] -> stage not stated [BLAST, CTFFIND v1.18, HMMER v3.3.2, PyMOL v1.2, RELION v4.0]

### Structure and function of the RAD51B-RAD51C-RAD51D-XRCC2 tumour suppressor. (Nature 2023)

- DOI: 10.1038/s41586-023-06179-1 | PMCID: PMC7614784 | PMID: 37344587
- Evidence: Atomic model building All model building was achieved using Phenix 74 , ISOLDE and COOT 75 .
- Full pipeline: alignment/mapping [ChimeraX] -> machine learning [RELION v3.1] -> stage not stated [AlphaFold, Fiji, ImageJ, PHENIX, Topaz]

### Genome expansion by a CRISPR trimmer-integrase. (Nature 2023)

- DOI: 10.1038/s41586-023-06178-2 | PMCID: PMC10284694 | PMID: 37316664
- Version used: **1.19.2**
- Evidence: The complex model was refined using rounds of real-space refinement and rigid body fit tools in Coot (v.0.9.4.1) 49 , and real_space_refine tool in Phenix (v.1.19.2-4158) 50 , using secondary structure, Ramachandran, and rotamer restraints.
- Full pipeline: structure determination [AlphaFold, Coot v0.9.4.1, PHENIX v1.19.2] -> machine learning [Topaz] -> stage not stated [ChimeraX, HMMER]

### Outer membrane utilisomes mediate glycan uptake in gut Bacteroidetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06146-w | PMCID: PMC7618045 | PMID: 37286596
- Evidence: Data collected for SeMet SGBP lev allowed solving the phase problem and partial model building via single anomalous dispersion (Se-SAD) using Phenix AUTOSOL 54 .
- Full pipeline: registration [CTFFIND] -> differential/statistical testing [limma] -> stage not stated [AlphaFold, CCP4, ChimeraX, PHENIX, R v4.1.1, RELION]

### Structural basis for FGF hormone signalling. (Nature 2023)

- DOI: 10.1038/s41586-023-06155-9 | PMCID: PMC10284700 | PMID: 37286607
- Evidence: Initial models were then adjusted in Coot 45 and real-space refined in Phenix 46 .
- Full pipeline: differential/statistical testing [ImageJ] -> simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX]

### Axonemal structures reveal mechanoregulatory and disease mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-06140-2 | PMCID: PMC10266980 | PMID: 37258679
- Evidence: Maps were postprocessed using Phenix_autosharpen and merged in ChimeraX to generate a composite map.
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> structure determination [Coot] -> stage not stated [AlphaFold, ChimeraX, PHENIX, R v4.0, RELION]

### Pan-KRAS inhibitor disables oncogenic signalling and tumour growth. (Nature 2023)

- DOI: 10.1038/s41586-023-06123-3 | PMCID: PMC10322706 | PMID: 37258666
- Evidence: Model building and refinement was performed with standard protocols using CCP4, COOT, autoBUSTER v.2.11.2 ( http://www.globalphasing.com ) and Phenix 35 , 36 .
- Full pipeline: alignment/mapping [HISAT2, HTSeq, Python] -> quantification [ImageJ, edgeR] -> structure determination [CCP4, PHENIX] -> stage not stated [Bioconductor, limma]

### Histone modifications regulate pioneer transcription factor cooperativity. (Nature 2023)

- DOI: 10.1038/s41586-023-06112-6 | PMCID: PMC10338341 | PMID: 37225990
- Evidence: Density modification in Phenix improved the map to 2.5 Å (ref.
- Full pipeline: structure determination [Coot] -> stage not stated [ImageJ, PHENIX, RELION]

### A small-molecule PI3Kα activator for cardioprotection and neuroregeneration. (Nature 2023)

- DOI: 10.1038/s41586-023-05972-2 | PMCID: PMC7614683 | PMID: 37225977
- Evidence: After several iterations of rigid-body, maximum-likelihood and TLS refinement using the PHENIX suite 67 , manual building and model inspection using COOT 68 , the final model converged to a final Rwork/Rfree of 0.1964/0.2456 at a maximum resolution of 2.20 Å.
- Full pipeline: quantification [R v4.0.0] -> differential/statistical testing [R v4.0.0] -> structure determination [PHENIX, REFMAC] -> stage not stated [CCP4, ImageJ, PyMOL]

### Ligand and G-protein selectivity in the κ-opioid receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06030-7 | PMCID: PMC10172140 | PMID: 37138078
- Evidence: The complex models (KOR–G-protein–scFv16) were manually built in Coot 65 , followed by several rounds of real-space refinement using Phenix 66 .
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL]

### Structural atlas of a human gut crassvirus. (Nature 2023)

- DOI: 10.1038/s41586-023-06019-2 | PMCID: PMC10172136 | PMID: 37138077
- Version used: **1.19**
- Evidence: 6 ) were generated by manual building in Coot (0.9.8.1) 46 , followed by real space refinement in Phenix (1.19) 47 .
- Full pipeline: structure determination [Coot v0.9.8.1, PHENIX v1.19] -> stage not stated [AlphaFold, ChimeraX v1.5, RELION v3.1]

### De novo design of protein interactions with learned surface fingerprints. (Nature 2023)

- DOI: 10.1038/s41586-023-05993-x | PMCID: PMC10131520 | PMID: 37100904
- Version used: **1.20.1**
- Evidence: The structures were determined using molecular replacement with the program Phaser MR in PHENIX (v.1.20.1-4487), with the reported PD-L1 structure (PDB: 3RRQ ) as the search model 72 .
- Full pipeline: alignment/mapping [AlphaFold] -> normalisation [scikit-learn] -> dimensionality reduction/clustering [scikit-learn] -> structure determination [Coot v0.9.5] -> machine learning [TensorFlow v1.12] -> visualisation [ChimeraX] -> stage not stated [PHENIX v1.20.1, UCSF Chimera]

### Cryo-EM structure of the transposon-associated TnpB enzyme. (Nature 2023)

- DOI: 10.1038/s41586-023-05933-9 | PMCID: PMC10097598 | PMID: 37020030
- Evidence: The metal coordination restraints were generated using ReadySet, as implemented in PHENIX.
- Full pipeline: structure determination [ChimeraX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Clustal Omega, PHENIX]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Evidence: Stained sections were imaged with a Perkin Elmer Opera Phenix Plus High-Content Screening System, in confocal mode with 2 μm z -step size, using a 40× (NA 1.1, 0.149 μm/pixel) water-immersion objective.
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### Structural basis for GSDMB pore formation and its targeting by IpaH7.8. (Nature 2023)

- DOI: 10.1038/s41586-023-05832-z | PMCID: PMC10115629 | PMID: 36991122
- Evidence: Model building and structure analysis Atomic models of both the IpaH7.8–GSDMB complex and GSDMB pore were built and refined into cryo-EM density using Coot 46 and PHENIX 47 .
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, Coot, MotionCor2, RELION, UCSF Chimera]

### Ultrafast structural changes direct the first molecular events of vision. (Nature 2023)

- DOI: 10.1038/s41586-023-05863-6 | PMCID: PMC10060157 | PMID: 36949205
- Evidence: The dark-state structure was obtained after several iterative cycles of refinement and iterative model building using Phenix.refine 75 and Coot 76 .
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Structural basis of mitochondrial membrane bending by the I-II-III&lt;sub&gt;2&lt;/sub&gt;-IV&lt;sub&gt;2&lt;/sub&gt; supercomplex. (Nature 2023)

- DOI: 10.1038/s41586-023-05817-y | PMCID: PMC10060162 | PMID: 36949187
- Evidence: Real-space refinement of atomic models was performed in PHENIX using secondary structure restraints 45 .
- Full pipeline: registration [IMOD, RELION] -> simulation/modelling [ChimeraX, GROMACS] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### From primordial clocks to circadian oscillators. (Nature 2023)

- DOI: 10.1038/s41586-023-05836-9 | PMCID: PMC10076222 | PMID: 36949197
- Version used: **1.20.1**
- Evidence: 36 )) was manually rebuilt in Coot (v.0.9.81) 54 and refined in Phenix (v.1.20.1-4487) 55 .
- Full pipeline: alignment/mapping [IQ-TREE v1.6, MAFFT, RAxML v8.2.9] -> simulation/modelling [UCSF Chimera v1.15] -> structure determination [Coot v0.9.81, PHENIX v1.20.1] -> visualisation [PyMOL v2.6.0]

### Structural basis for bacterial energy extraction from atmospheric hydrogen. (Nature 2023)

- DOI: 10.1038/s41586-023-05781-7 | PMCID: PMC10017518 | PMID: 36890228
- Evidence: 58 ). [NiFe], [3Fe–4S], and menaquinone cofactors associated with Huc were downloaded from the PDB and customized restraints generated using Elbow within the PHENIX package before they were fitted and refined into maps using Coot 59 , 60 .
- Full pipeline: simulation/modelling [GROMACS v2021.3] -> structure determination [ChimeraX v1.3, PHENIX] -> visualisation [AlphaFold, VMD] -> stage not stated [CTFFIND v4.1.8, Coot, RELION v3.1.2]

### Ubiquitin-like conjugation by bacterial cGAS enhances anti-phage defence. (Nature 2023)

- DOI: 10.1038/s41586-023-05862-7 | PMCID: PMC10097602 | PMID: 36848932
- Evidence: The structure was refined with iterative rounds of refinement and model building using PHENIX and Coot 29 , 30 .
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [AlphaFold] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### The structural basis for HIV-1 Vif antagonism of human APOBEC3G. (Nature 2023)

- DOI: 10.1038/s41586-023-05779-1 | PMCID: PMC10033410 | PMID: 36754086
- Evidence: 2 – 4 for map-model fit analysis by PHENIX 86 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> registration [MotionCor2] -> structure determination [AlphaFold, UCSF Chimera] -> stage not stated [ChimeraX, Coot, PHENIX, PyMOL, RELION]

### Structural basis for substrate selection by the SARS-CoV-2 replicase. (Nature 2023)

- DOI: 10.1038/s41586-022-05664-3 | PMCID: PMC9891196 | PMID: 36725929
- Evidence: Locally refined maps were combined into a RTC composite map using PHENIX ‘combine focused maps’ to aid model building 42 .
- Full pipeline: normalisation [MotionCor2] -> differential/statistical testing [RELION v3.1] -> structure determination [PHENIX] -> stage not stated [Coot v0.9.5]

### Structure of the lysosomal mTORC1-TFEB-Rag-Ragulator megacomplex. (Nature 2023)

- DOI: 10.1038/s41586-022-05652-7 | PMCID: PMC9931586 | PMID: 36697823
- Evidence: A composite map combining the three focused-refinement maps was assembled using PHENIX 57 .
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [ImageJ v1.47, MotionCor2]

### RNA targeting unleashes indiscriminate nuclease activity of CRISPR-Cas12a2. (Nature 2023)

- DOI: 10.1038/s41586-022-05560-w | PMCID: PMC9849127 | PMID: 36599980
- Version used: **1.19**
- Evidence: 49 ) was used to improve the fit of the model to the map, and real-space refinement as implemented within Phenix v1.19 (ref.
- Full pipeline: structure determination [PHENIX v1.19] -> stage not stated [AlphaFold, ChimeraX v1.0, Coot, PyMOL v2.5]

### Structural basis of broad-spectrum β-lactam resistance in Staphylococcus aureus. (Nature 2023)

- DOI: 10.1038/s41586-022-05583-3 | PMCID: PMC9834060 | PMID: 36599987
- Evidence: Incorrect regions were deleted and iterative model building and refinement carried out in Coot 72 , Phenix real.space refine 73 in the Phenix software package 74 , and density-guided Rosetta refinement with symmetry 39 .
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [RELION]

### Programming multicellular assembly with synthetic cell adhesion molecules. (Nature 2023)

- DOI: 10.1038/s41586-022-05622-z | PMCID: PMC9892004 | PMID: 36509107
- Evidence: Confocal microscopy was performed using the Opera Phenix automated spinning-disk confocal microscope with a ×20 water-immersion objective in 384-well plates; the Nikon TiE with CSU-X1 spinning-disk confocal unit with ×60 and ×100 oil-immersion objectives; or the Zeiss LSM 980 with Airyscan 2 with a ×40 water-immersion objective.
- Full pipeline: stage not stated [ImageJ, PHENIX]

### Principles of mitoribosomal small subunit assembly in eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-022-05621-0 | PMCID: PMC9892005 | PMID: 36482135
- Evidence: Finally, entire models for each state were adjusted with three cycles of refinement in PHENIX using phenix.real_space_refine using secondary structure restraints 59 .
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [ChimeraX, PyMOL] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, RELION v3.1.1]

### MCM double hexamer loading visualized with human proteins. (Nature 2024)

- DOI: 10.1038/s41586-024-08263-6 | PMCID: PMC11634765 | PMID: 39604733
- Version used: **1.21**
- Evidence: This was followed by an iterative process of real space refinement with restraints on geometry, secondary structure, metal coordination and nucleic acid planarity in Phenix v1.21 (ref.
- Full pipeline: differential/statistical testing [AlphaFold] -> structure determination [AlphaFold, Coot v0.9.8.1, PHENIX v1.21] -> stage not stated [CTFFIND v1.06, ChimeraX v1.6.1, RELION, Topaz v0.2.5]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: Stained sections were imaged with a Perkin Elmer Opera Phenix High-Content Screening System, in confocal mode with 1-μm z -step size, using a 20× water-immersion objective (NA 0.16, 0.299 μm per pixel).
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Evidence: Imaging was conducted using a Perkin Elmer Opera Phenix Plus High-Content Screening System in confocal mode with 1-μm z -step size, using a 63× (NA 1.15, 0.097 μm pixel −1 ) water-immersion objective.
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### Nucleosome flipping drives kinetic proofreading and processivity by SWR1. (Nature 2024)

- DOI: 10.1038/s41586-024-08152-y | PMCID: PMC11618073 | PMID: 39506114
- Evidence: The final coordinates were subjected to real-space refinement in Phenix 48 .
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold, CTFFIND, Coot]

### Design of customized coronavirus receptors. (Nature 2024)

- DOI: 10.1038/s41586-024-08121-5 | PMCID: PMC12187079 | PMID: 39478224
- Version used: **1.21**
- Evidence: Model validation and analysis used MolProbity 87 , EMRinger 88 , Privateer 89 , and Phenix version 1.21 90 .
- Full pipeline: differential/statistical testing [RELION] -> structure determination [RELION] -> visualisation [ChimeraX, IQ-TREE v2.0.6] -> stage not stated [PHENIX v1.21, UCSF Chimera]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Evidence: 4-plex RNAscope slides with FOXP3 , SHH , SLC26A7 , NDP , CDH5 , CD68 and P2RY12 probes were imaged on a Perkin Elmer Opera Phenix Plus High-Content Screening System using a ×40 (NA 1.1, 0.149 μm per pixel) water-immersion objective with a 2 µm z step.
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### A bacterial immunity protein directly senses two disparate phage proteins. (Nature 2024)

- DOI: 10.1038/s41586-024-08039-y | PMCID: PMC11578894 | PMID: 39415022
- Evidence: The molecular replacement solution was refined in PHENIX 39 with manual model building done with Coot 40 .
- Full pipeline: alignment/mapping [BLAST, MUSCLE] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ColabFold]

### Structural basis of mRNA decay by the human exosome-ribosome supercomplex. (Nature 2024)

- DOI: 10.1038/s41586-024-08015-6 | PMCID: PMC11540850 | PMID: 39385025
- Evidence: In several areas of the map (the EXO9 barrel and SKI2 H ), the resolution and quality of the reconstruction allowed us to manually adjust the fit of the models in Coot 50 , followed by real-space refinement from within the PHENIX suite 51 .
- Full pipeline: quantification [ImageJ] -> structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ImageJ] -> stage not stated [MotionCor2, RELION v3.1, UCSF Chimera]

### LYCHOS is a human hybrid of a plant-like PIN transporter and a GPCR. (Nature 2024)

- DOI: 10.1038/s41586-024-08012-9 | PMCID: PMC11525196 | PMID: 39358511
- Version used: **1.20.1**
- Evidence: Finally, real space refinement was conducted in PHENIX (v.1.20.1) 42 using harmonic potential restraints.
- Full pipeline: dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX v1.20.1] -> visualisation [Matplotlib] -> stage not stated [AlphaFold, CTFFIND v4.1.8, ChimeraX, ImageJ v2.14.0, MotionCor2 v1.1.0]

### Structural basis of archaeal FttA-dependent transcription termination. (Nature 2024)

- DOI: 10.1038/s41586-024-07979-9 | PMCID: PMC11616081 | PMID: 39322680
- Evidence: The initial atomic model was subjected to real-space rigid-body refinement in Phenix 57 , and was subjected to iterative cyles of model building in Coot 56 and refinement in Phenix 57 .
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL]

### The ultra-high affinity transport proteins of ubiquitous marine bacteria. (Nature 2024)

- DOI: 10.1038/s41586-024-07924-w | PMCID: PMC11485210 | PMID: 39261732
- Evidence: The structures were then refined by iterative real-space and reciprocal-space refinement in REFMAC 78 , Phenix 79 , and COOT 80 .
- Full pipeline: alignment/mapping [MUSCLE v3.8.31] -> structure determination [PHENIX, REFMAC] -> stage not stated [AlphaFold]

### Structure of the human TIP60-C histone exchange and acetyltransferase complex. (Nature 2024)

- DOI: 10.1038/s41586-024-08011-w | PMCID: PMC11578891 | PMID: 39260417
- Evidence: The atomic model was refined in PHENIX by real-space refinement with secondary structure restrains 50 and in Isolde 51 .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [cryoDRGN] -> structure determination [PHENIX, cryoDRGN] -> stage not stated [AlphaFold, ChimeraX, Coot, RELION]

### Agonist antibody to guanylate cyclase receptor NPR1 regulates vascular tone. (Nature 2024)

- DOI: 10.1038/s41586-024-07903-1 | PMCID: PMC11410649 | PMID: 39261724
- Evidence: These models were then manually rebuilt using Coot 46 , and real-space refined against the map using Phenix 47 .
- Full pipeline: differential/statistical testing [REGENIE] -> structure determination [PHENIX]

### Visualizing chaperonin function in situ by cryo-electron tomography. (Nature 2024)

- DOI: 10.1038/s41586-024-07843-w | PMCID: PMC11390479 | PMID: 39169181
- Evidence: The models were subsequently refined in real space with Phenix 82 .
- Full pipeline: alignment/mapping [MotionCor2 v1.4.0] -> registration [RELION] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX]

### Structure of a fully assembled γδ T cell antigen receptor. (Nature 2024)

- DOI: 10.1038/s41586-024-07920-0 | PMCID: PMC11485255 | PMID: 39146975
- Version used: **1.21.1**
- Evidence: Atomic model building and refinement Following finalization of the cryo-EM maps, crystal structures of the previously solved G83.C4 TCR (PDB 7LLI ) 4 , αβ TCR (PDB 7PHR ) 3 and UCHT1 Fab (PDB 1XIW ) 24 were used as starting models for domain placement using rigid body refinement in Phenix (v.1.21.1) 48 , 49 .
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [Coot v0.9.8.93] -> structure determination [Coot v0.9.8.93, PHENIX v1.21.1] -> visualisation [ChimeraX v1.8] -> stage not stated [CTFFIND v4.1.14, ImageJ v1.54, R v12.1, RELION v4.0]

### Growth of complete ammonia oxidizers on guanidine. (Nature 2024)

- DOI: 10.1038/s41586-024-07832-z | PMCID: PMC11410670 | PMID: 39143220
- Evidence: The structure was further refined in iterative cycles of the manual model building using COOT 80 and maximum-likelihood refinement using the PHENIX software suite 81 .
- Full pipeline: alignment/mapping [ImageJ v1.54f] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ImageJ v1.54f, PyMOL, phytools] -> stage not stated [AlphaFold, BEDTools, HMMER]

### De novo design of allosterically switchable protein assemblies. (Nature 2024)

- DOI: 10.1038/s41586-024-07813-2 | PMCID: PMC11338832 | PMID: 39143214
- Evidence: Phenix 67 real-space refinement was subsequently performed as a final step before the final model quality was analysed using MolProbity 68 .
- Full pipeline: differential/statistical testing [SciPy] -> structure determination [PHENIX] -> visualisation [ChimeraX, Python] -> stage not stated [PyMOL, UCSF Chimera]

### Structural basis for transthiolation intermediates in the ubiquitin pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07828-9 | PMCID: PMC11374688 | PMID: 39143218
- Evidence: Coordinates for all models were produced via iterative rounds of refinement and building in real space using Phenix and Coot 66 , 68 .
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> differential/statistical testing [Topaz] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [IMOD v4.11] -> stage not stated [CTFFIND, ChimeraX, RELION v3.1]

### Structure of the human dopamine transporter and mechanisms of inhibition. (Nature 2024)

- DOI: 10.1038/s41586-024-07739-9 | PMCID: PMC11324517 | PMID: 39112705
- Version used: **1.20.1**
- Evidence: The fitted model and map were then manually adjusted using COOT (v0.9.8.6) 56 and then further refined in Phenix v1.20.1-4487 57 using real space refinement 58 in an iterative manner.
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX v1.20.1] -> stage not stated [PyMOL, VMD]

### A virally encoded tRNA neutralizes the PARIS antiviral defence system. (Nature 2024)

- DOI: 10.1038/s41586-024-07874-3 | PMCID: PMC11464382 | PMID: 39111359
- Version used: **1.20.1**
- Evidence: Following initial equilibration, PDB files were saved and used as inputs for real-space refinement using PHENIX v.1.20.1 (ref.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HMMER v3.3.2, MUSCLE v5.1] -> structure determination [PHENIX v1.20.1] -> stage not stated [AlphaFold, ChimeraX v1.7, SPAdes]

### FANCD2-FANCI surveys DNA and recognizes double- to single-stranded junctions. (Nature 2024)

- DOI: 10.1038/s41586-024-07770-w | PMCID: PMC11358013 | PMID: 39085614
- Evidence: After manual inspection and adjustment in Coot 40 and ISOLDE 49 , the model was iteratively refined in Coot and Phenix 50 .
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [Jupyter, Matplotlib v3.7.2, NumPy v1.26.0, Python v3.9, RELION v4.0, SciPy v1.11.3]

### Cryo-EM architecture of a near-native stretch-sensitive membrane microdomain. (Nature 2024)

- DOI: 10.1038/s41586-024-07720-6 | PMCID: PMC11324527 | PMID: 39048819
- Version used: **1.20**
- Evidence: Iterative rounds of model building, performed in Coot v.0.8.9.2, and real-space refinement, performed in PHENIX v.1.20-4459, were completed until no improvement in the model was observed.
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.8.9.2, PHENIX v1.20] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, Cellpose v2.0, RELION v2.1.0, VMD v1.9]

### CryoET of β-amyloid and tau within postmortem Alzheimer's disease brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07680-x | PMCID: PMC11269202 | PMID: 38987603
- Version used: **1.17.1**
- Evidence: The model was real-space refined using Phenix v.1.17.1 65 with noncrystallographic symmetry restraints applied to limit inter-chain divergence.
- Full pipeline: alignment/mapping [IMOD v4.12.35] -> structure determination [Coot v0.8.9.2, PHENIX v1.17.1] -> machine learning [EMAN2 v2.99] -> stage not stated [CTFFIND v1.14, ChimeraX v1.5, Fiji, ImageJ, RELION v4.0]

### Molecular basis for transposase activation by a dedicated AAA+ ATPase. (Nature 2024)

- DOI: 10.1038/s41586-024-07550-6 | PMCID: PMC11208146 | PMID: 38926614
- Evidence: The complete monomer was then subjected to a round of model building and real space refinement with COOT and PHENIX-1.19 using Ramachandran, rotamer, geometry and secondary structure restraints 65 , 66 .
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX v1.5] -> stage not stated [CCP4, CTFFIND v4.1, RELION, Topaz]

### Computational design of soluble and functional membrane protein analogues. (Nature 2024)

- DOI: 10.1038/s41586-024-07601-y | PMCID: PMC11236705 | PMID: 38898281
- Evidence: Atomic model refinement was completed using COOT 73 and Phenix.refine 72 .
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, Python v3.9] -> stage not stated [AlphaFold]

### Oligomerization-mediated autoinhibition and cofactor binding of a plant NLR. (Nature 2024)

- DOI: 10.1038/s41586-024-07668-7 | PMCID: PMC11338831 | PMID: 38866053
- Evidence: Model building and refinement The model of Sl NRC2 monomer predicted by AlphaFold2 was docked into the reconstruction map of Sl NRC2 dimer (Protein Data Bank (PDB) code 8XUO ) and then manually adjusted in COOT 55 – 57 followed by PHENIX 58 refinement in real space with secondary structure and geometry restraints.
- Full pipeline: structure determination [AlphaFold, PHENIX, RELION v3.08] -> stage not stated [MotionCor2]

### Structure and topography of the synaptic V-ATPase-synaptophysin complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07610-x | PMCID: PMC11269182 | PMID: 38838737
- Version used: **1.21**
- Evidence: The final models were evaluated through multiple rounds of refinement using Coot and Phenix (v.1.21) 78 and validated with EMRinger 79 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [AlphaFold, PHENIX v1.21] -> machine learning [RELION, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Coot, Python, SciPy, UCSF Chimera]

### Membraneless channels sieve cations in ammonia-oxidizing marine archaea. (Nature 2024)

- DOI: 10.1038/s41586-024-07462-5 | PMCID: PMC11153153 | PMID: 38811725
- Evidence: The model was then placed into the hexameric map as six copies and subjected to several rounds of refinement using refmac5 59 inside the CCP-EM software suite 60 and PHENIX 61 , followed by manually rebuilding in Coot 58 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [NAMD v2.14, VMD v1.94] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold v2.2.0, MotionCor2]

### Structural basis for pegRNA-guided reverse transcription by a prime editor. (Nature 2024)

- DOI: 10.1038/s41586-024-07497-8 | PMCID: PMC11222144 | PMID: 38811740
- Evidence: The structure validation was performed using MolProbity in the PHENIX package 34 .
- Full pipeline: registration [MotionCor2] -> stage not stated [AlphaFold, ChimeraX, PHENIX, RELION v3.1.1, Topaz]

### Kainate receptor channel opening and gating mechanism. (Nature 2024)

- DOI: 10.1038/s41586-024-07475-0 | PMCID: PMC11186766 | PMID: 38778115
- Evidence: Subsequently, the combine_focused_maps algorithm implemented in Phenix was used to create composite maps for GluK2 bound to either one or two ConA dimers, with 4.29-Å and 6.66-Å resolutions, as well as the locally refined ATD, ConA and LBD–TMD regions as inputs.
- Full pipeline: simulation/modelling [VMD v1.9.4] -> structure determination [Coot, PHENIX, PyMOL] -> visualisation [ChimeraX, PyMOL]

### Structural insights into the cross-exon to cross-intron spliceosome switch. (Nature 2024)

- DOI: 10.1038/s41586-024-07458-1 | PMCID: PMC11208138 | PMID: 38778104
- Evidence: Coordinates of the tri-snRNP parts of the various complexes were refined in real space using PHENIX 36 .
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, RELION v3.1]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Evidence: After manual backbone tracing and docking of side chains, real-space refinement in Phenix was performed (v.1.18) 43 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### Mechanism of single-stranded DNA annealing by RAD52-RPA complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07347-7 | PMCID: PMC11096129 | PMID: 38658755
- Evidence: All model building was performed using Phenix 67 , 68 , COOT 69 and ISOLDE 70 in ChimeraX 71 .
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega] -> quantification [ImageJ] -> stage not stated [ChimeraX, EMAN2, PHENIX, RELION v3.1]

### Discovery of WRN inhibitor HRO761 with synthetic lethality in MSI cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07350-y | PMCID: PMC11078746 | PMID: 38658754
- Evidence: Images were captured and analysed using the PerkinElmer Opera Phenix imager and Harmony 4.9 software.
- Full pipeline: normalisation [R, fgsea] -> differential/statistical testing [DESeq2, R, fgsea] -> stage not stated [GSEA, PHENIX, SciPy]

### Structures of human γδ T cell receptor-CD3 complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07439-4 | PMCID: PMC11153141 | PMID: 38657677
- Evidence: The resolution of the reconstruction was determined on the basis of the gold standard Fourier shell correlation (FSC) 0.143 criterion in cryoSPARC (v.4) 59 , Relion (v.3.1) 62 or using Phenix.mtriage 65 .
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [MotionCor2, RELION]

### Emergence of fractal geometries in the evolution of a metabolic enzyme. (Nature 2024)

- DOI: 10.1038/s41586-024-07287-2 | PMCID: PMC11041685 | PMID: 38600380
- Version used: **1.19.2**
- Evidence: All structures were determined by molecular replacement with PHASER 54 , manually built in WinCOOT (v.0.9.6) 55 and refined with PHENIX (v.1.19.2) 56 .
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MotionCor2] -> normalisation [RELION v3.1] -> simulation/modelling [GROMACS v2022.2] -> structure determination [MUSCLE v3.8.31, PHENIX v1.19.2] -> stage not stated [PyMOL v2.5.2, Topaz, UCSF Chimera]

### Structural basis of Integrator-dependent RNA polymerase II termination. (Nature 2024)

- DOI: 10.1038/s41586-024-07269-4 | PMCID: PMC11062913 | PMID: 38570683
- Evidence: Various parts of the model were refined against respective focused refined maps using the phenix.real_space_refine tool in the PHENIX package 42 , 66 .
- Full pipeline: structure determination [ChimeraX, ColabFold, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, Coot, RELION v3.1]

### Molecular insights into capsular polysaccharide secretion. (Nature 2024)

- DOI: 10.1038/s41586-024-07248-9 | PMCID: PMC11041684 | PMID: 38570679
- Evidence: Using the Phenix Combine Focused Maps job 51 , a composite map 1 was created from maps A and B, on the basis of the model and half maps from the focused refinements.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ImageJ]

### The CRL5-SPSB3 ubiquitin ligase targets nuclear cGAS for degradation. (Nature 2024)

- DOI: 10.1038/s41586-024-07112-w | PMCID: PMC10972748 | PMID: 38418882
- Evidence: The whole model was then refined in PHENIX 45 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, CellProfiler, ChimeraX]

### Automated model building and protein identification in cryo-EM maps. (Nature 2024)

- DOI: 10.1038/s41586-024-07215-4 | PMCID: PMC11006616 | PMID: 38408488
- Evidence: We therefore applied ModelAngelo without using its sequence module to a Phenix auto-sharpened version of the map, as the original map was post-processed using DeepEMhancer 49 .
- Full pipeline: stage not stated [AlphaFold, HMMER, PHENIX]

### Targeted protein degradation via intramolecular bivalent glues. (Nature 2024)

- DOI: 10.1038/s41586-024-07089-6 | PMCID: PMC10917667 | PMID: 38383787
- Version used: **1.20.1**
- Evidence: Initial restraints for IBG1 were generated using a SMILES string with eLBOW (in Phenix v1.20.1-4487) 68 , then run through the GRADE webserver (Grade2 v1.3.0).
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, Cutadapt v2.8, featureCounts v2.0.1] -> visualisation [ChimeraX, PyMOL] -> stage not stated [ColabFold, Coot v0.9.8.1, Nextflow, PHENIX v1.20.1]

### The UFM1 E3 ligase recognizes and releases 60S ribosomes from ER translocons. (Nature 2024)

- DOI: 10.1038/s41586-024-07093-w | PMCID: PMC10937380 | PMID: 38383789
- Version used: **1.2.1**
- Evidence: UREL–60S model building The ligase-bound 60S map was sharpened using Phenix (v.1.2.1) 48 autosharpen map job and the ligase-only map was sharpened using the DeepEMhancer 49 tight target sharpening protocol.
- Full pipeline: registration [RELION v3.1] -> structure determination [AlphaFold, ChimeraX v1.2.5, REFMAC] -> machine learning [cryoDRGN v3.2.0] -> stage not stated [CCP4, Coot v0.9.8.1, PHENIX v1.2.1]

### A new family of bacterial ribosome hibernation factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07041-8 | PMCID: PMC10901736 | PMID: 38355796
- Version used: **1.20.1**
- Evidence: These rRNA and protein models were morph-fitted into the cryo-EM maps using ChimeraX 1.4 58 and Phenix 1.20.1 59 and then rebuilt using Coot on the basis of the information about the genomic sequence of P. urativorans (RefSeq GCF_001298525.1 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, Coot v0.8.9.2, UCSF Chimera v1.14] -> stage not stated [ChimeraX v1.4, HMMER, PHENIX v1.20.1, RELION v3.1]

### Oxygen-evolving photosystem II structures during S&lt;sub&gt;1&lt;/sub&gt;-S&lt;sub&gt;2&lt;/sub&gt;-S&lt;sub&gt;3&lt;/sub&gt; transitions. (Nature 2024)

- DOI: 10.1038/s41586-023-06987-5 | PMCID: PMC10866707 | PMID: 38297122
- Evidence: Structural refinement for the dark and 1F datasets Molecular replacement for the dark data was performed using Phaser-MR from PHENIX 55 with the PSII structure solved at 2.35-Å resolution and at room temperature (PDB code: 5WS5 ) as the search model, in which water molecules and the OEC were removed 4 .
- Full pipeline: structure determination [PHENIX]

### A new antibiotic traps lipopolysaccharide in its intermembrane transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06799-7 | PMCID: PMC10794137 | PMID: 38172635
- Evidence: The coordinates were then refined using Phenix 63 , 64 .
- Full pipeline: alignment/mapping [RELION] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX, Coot]

### Cryo-EM structures of PP2A:B55-FAM122A and PP2A:B55-ARPP19. (Nature 2024)

- DOI: 10.1038/s41586-023-06870-3 | PMCID: PMC10765524 | PMID: 38123684
- Evidence: Cryo-EM model building All models were built and refined by iterating between manual rebuilding and refinement in Coot 57 and ISOLDE 58 , and automated global real-space refinement in Phenix 59 .
- Full pipeline: quantification [ImageJ v1.53t] -> structure determination [Coot, PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, RELION v4.0]

### Structures of the promoter-bound respiratory syncytial virus polymerase. (Nature 2024)

- DOI: 10.1038/s41586-023-06867-y | PMCID: PMC10794133 | PMID: 38123676
- Evidence: The final structures of the RSV polymerase in complex with Le10 or TrC10 were built and refined using COOT and PHENIX, and the model geometries were validated using MolProbity 29 – 31 .
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, PyMOL, RELION v3.1.3] -> stage not stated [ChimeraX, UCSF Chimera]

### The PfRCR complex bridges malaria parasite and erythrocyte during invasion. (Nature 2024)

- DOI: 10.1038/s41586-023-06856-1 | PMCID: PMC10794152 | PMID: 38123677
- Evidence: Composite maps for PfRCR–Cy.003 and PfCyRPA–PfRIPR–Cy.003 were generated from consensus and local refinement maps in PHENIX 42 .
- Full pipeline: differential/statistical testing [RELION v3.1.3] -> structure determination [AlphaFold, PHENIX, RELION v3.1.3] -> visualisation [ChimeraX]

### Template and target-site recognition by human LINE-1 in retrotransposition. (Nature 2024)

- DOI: 10.1038/s41586-023-06933-5 | PMCID: PMC10830416 | PMID: 38096901
- Evidence: The L1 ORF2p protein was first manually inspected in COOT 61 to correct the amino acid sequence and then processed for real-space refinement in PHENIX 62 .
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [CTFFIND v4.1, ImageJ, MotionCor2, RELION v3.1.1]

### A human embryonic limb cell atlas resolved in space and time. (Nature 2024)

- DOI: 10.1038/s41586-023-06806-x | PMCID: PMC7616500 | PMID: 38057666
- Evidence: The stained sections were imaged with either AxioScan.Z1 (Zeiss) or the Opera Phenix High-Content Screening System (PerkinElmer).
- Full pipeline: alignment/mapping [STAR v2.5.1b] -> quantification [STAR v2.5.1b, scVelo v0.24] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Scanpy] -> structure determination [AnnData] -> machine learning [ilastik] -> stage not stated [CellPhoneDB, PHENIX, SCENIC, scDblFinder]

### Structural basis of Gabija anti-phage defence and viral immune evasion. (Nature 2024)

- DOI: 10.1038/s41586-023-06855-2 | PMCID: PMC10781630 | PMID: 37992757
- Evidence: Experimental phase information was determined by molecular replacement using monomeric GajA and GajB AlphaFold2-predicted structures 31 , 32 in PHENIX 45 .
- Full pipeline: structure determination [Coot] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, PHENIX]

### In situ structural mechanism of epothilone-B-induced CNS axon regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09654-z | PMCID: PMC12795760 | PMID: 41224993
- Evidence: Model building and refinement The initial model was prepared using PDB code 6DPU , fit into the cryo-EM map using ChimeraX 74 and further refined by rounds of manual fitting in COOT 75 with subsequent real-space refinement in PHENIX 76 .
- Full pipeline: alignment/mapping [IMOD] -> structure determination [ChimeraX, PHENIX] -> visualisation [ImageJ] -> stage not stated [RELION v5.0]

### Synthetic α-synuclein fibrils replicate in mice causing MSA-like pathology. (Nature 2025)

- DOI: 10.1038/s41586-025-09698-1 | PMCID: PMC12695662 | PMID: 41193804
- Evidence: The atomic model for the backbone of the core of the 1B fibrils encompassing residues 34 to 95 was built de novo using Coot 49 (v.0.9.8.96) Initially, three β-rungs were modelled in coot and were refined in real-space in PHENIX 45 (v.1.21.2) Finally, these chains were extended to 9 β-rungs per protofilament and refined in tandem with phenix.real_space_refine and in coot to improve the Ramachandran...
- Full pipeline: structure determination [ChimeraX, Coot, IMOD, PHENIX, RELION v4.0] -> stage not stated [MACS2]

### Mechanism of conductance control and neurosteroid binding in NMDA receptors. (Nature 2025)

- DOI: 10.1038/s41586-025-09695-4 | PMCID: PMC12951714 | PMID: 41162707
- Version used: **1.20.1**
- Evidence: Further processing was done using Phenix (v1.20.1-4487) 53 and manually refined using winCOOT (v.0.9.8.95) 54 .
- Full pipeline: structure determination [ChimeraX v1.4, PHENIX v1.20.1] -> stage not stated [GROMACS]

### Helicase-mediated mechanism of SSU processome maturation and disassembly. (Nature 2025)

- DOI: 10.1038/s41586-025-09688-3 | PMCID: PMC12711562 | PMID: 41162712
- Evidence: The final models for the 16 states were real-space refined with three cycles of refinement in PHENIX using phenix.real_space_refine 41 using secondary structure restraints for proteins and RNA.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, ChimeraX, RELION]

### Nanobody-based recombinant antivenom for cobra, mamba and rinkhals bites. (Nature 2025)

- DOI: 10.1038/s41586-025-09661-0 | PMCID: PMC12629983 | PMID: 41162699
- Evidence: Model building and refinement were performed with Phenix.refine 77 and Coot 79 .
- Full pipeline: structure determination [PHENIX] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, PyMOL]

### The Panoptes system uses decoy cyclic nucleotides to defend against phage. (Nature 2025)

- DOI: 10.1038/s41586-025-09557-z | PMCID: PMC12657218 | PMID: 41034579
- Evidence: The structures were determined using molecular replacement conducted by the Phaser-MR program in the PHENIX suite (v.1.21-5207) 58 using a predicted structural model of Kp OptS generated by ColabFold v.1.5.5, which uses a homology search by MMseqs2 with AlphaFold2 59 .
- Full pipeline: differential/statistical testing [tidyverse] -> structure determination [Coot v1.1.17] -> visualisation [PyMOL, tidyverse] -> stage not stated [AlphaFold, ColabFold v1.5.5, PHENIX]

### A miniature CRISPR-Cas10 enzyme confers immunity by inhibitory signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09569-9 | PMCID: PMC12657230 | PMID: 41034576
- Evidence: The structure was solved by molecular replacement 67 using a ColabFold-generated 68 model (pLDDT = 95.12) of mCpol with residual residues from the C-terminal cleavage site (mCpol-ENLYFQ) in PHENIX 69 .
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT] -> dimensionality reduction/clustering [AlphaFold] -> visualisation [Matplotlib v3.7.2, Python, seaborn v0.13.2] -> stage not stated [ColabFold, Galaxy, Jupyter, PHENIX]

### A new paradigm for outer membrane protein biogenesis in the Bacteroidota. (Nature 2025)

- DOI: 10.1038/s41586-025-09532-8 | PMCID: PMC12611786 | PMID: 41034578
- Version used: **1.21**
- Evidence: Model building, structure refinement and figure preparation Iterative model building and real-space refinement using secondary structure, rotamer, and Ramachandran restraints was performed in Coot v0.9 61 and Phenix 1.21 62 , respectively.
- Full pipeline: structure determination [Coot v0.9, PHENIX v1.21] -> stage not stated [AlphaFold, ChimeraX, RELION v4.03]

### Design of facilitated dissociation enables timing of cytokine signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09549-z | PMCID: PMC12611780 | PMID: 40993395
- Evidence: Structures were refined in PHENIX 69 .
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [CCP4] -> differential/statistical testing [DESeq2] -> simulation/modelling [MDAnalysis] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> stage not stated [GROMACS v2020.2, PyMOL, RoseTTAFold]

### Myeloperoxidase transforms chromatin into neutrophil extracellular traps. (Nature 2025)

- DOI: 10.1038/s41586-025-09523-9 | PMCID: PMC12629992 | PMID: 40963017
- Evidence: Using these, a non-uniform refinement resulted in a reconstruction at 3.76 Å that was sharpened in PHENIX 50 by applying a sharpening B -factor of 252.6 Å 2 .
- Full pipeline: alignment/mapping [IMOD v4.11] -> dimensionality reduction/clustering [UMAP] -> structure determination [IMOD v4.11, PHENIX, RELION v3.1] -> stage not stated [ChimeraX]

### Structural basis for mTORC1 activation on the lysosomal membrane. (Nature 2025)

- DOI: 10.1038/s41586-025-09545-3 | PMCID: PMC12448111 | PMID: 40963021
- Evidence: Model refinement against local maps was accomplished using PHENIX for real-space refinement 58 .
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [ImageJ, Topaz]

### Delta-type glutamate receptors are ligand-gated ion channels. (Nature 2025)

- DOI: 10.1038/s41586-025-09610-x | PMCID: PMC12520249 | PMID: 40957579
- Evidence: Model building, refinement, and structural analysis ChimeraX 63 , Coot 64 , ISOLDE 65 and PHENIX 66 compiled by the SBgrid Consortium 67 were used in combination to perform model building, refinement, and structural analysis.
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold]

### Structure and mechanism of the mitochondrial calcium transporter NCLX. (Nature 2025)

- DOI: 10.1038/s41586-025-09491-0 | PMCID: PMC12571890 | PMID: 40931067
- Evidence: The rebuilt model was then subjected to refinement in Phenix 69 to optimize its geometry and stereochemistry and was assessed by MolProbity.
- Full pipeline: simulation/modelling [VMD] -> structure determination [AlphaFold, PHENIX] -> machine learning [Topaz v0.2.4] -> visualisation [ChimeraX, PyMOL, UCSF Chimera, VMD]

### A nanobody specific to prefusion glycoprotein B neutralizes HSV-1 and HSV-2. (Nature 2025)

- DOI: 10.1038/s41586-025-09438-5 | PMCID: PMC12507662 | PMID: 40903574
- Evidence: In CCP-EM Doppio ( https://www.ccpem.ac.uk/ ), the model was fitted in the map using MolRep 56 and the structure was refined using Refmac Servalcat 57 and Phenix 58 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot]

### One-shot design of functional protein binders with BindCraft. (Nature 2025)

- DOI: 10.1038/s41586-025-09429-6 | PMCID: PMC12507698 | PMID: 40866699
- Evidence: Atomic model refinement was completed using COOT 59 and Phenix.refine 58 .
- Full pipeline: alignment/mapping [AlphaFold] -> quantification [R] -> structure determination [PHENIX] -> visualisation [ChimeraX, Python v3.9]

### Structural basis for the dynamic regulation of mTORC1 by amino acids. (Nature 2025)

- DOI: 10.1038/s41586-025-09428-7 | PMCID: PMC12507694 | PMID: 40836086
- Version used: **2.0**
- Evidence: Finally, high-occupancy composite maps (both unsharpened and DeepEMhancer sharpened) were generated in phenix.combine_focused_maps (Phenix v2.0) 51 by combining rigid bodies within the respective sc-GATOR2 complexes (Supplementary Figs.
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [AlphaFold, ChimeraX v1.8, Coot v0.9.8] -> machine learning [Topaz] -> stage not stated [CTFFIND v4.1.14, MotionCor2, PHENIX v2.0, RELION v5.0]

### Molecular mechanism of ultrafast transport by plasma membrane Ca&lt;sup&gt;2+&lt;/sup&gt;-ATPases. (Nature 2025)

- DOI: 10.1038/s41586-025-09402-3 | PMCID: PMC12488499 | PMID: 40836084
- Evidence: The AlphaFold model of mouse NPTN (ID: AF- P97300 -F1) was used for molecular replacement using the Phaser program 67 in PHENIX 68 .
- Full pipeline: structure determination [Coot, RELION v3.1, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1.10, ChimeraX, MotionCor2, PHENIX]

### SLC45A4 is a pain gene encoding a neuronal polyamine transporter. (Nature 2025)

- DOI: 10.1038/s41586-025-09326-y | PMCID: PMC12507699 | PMID: 40836097
- Version used: **1.20.1**
- Evidence: Model building was performed in Coot (v.0.9.8.1 EL) 60 and ISOLDE 61 , refinement in PHENIX (v.1.20.1-4487) real-space refinement 62 and validation in MolProbity 63 .
- Full pipeline: quality control [PLINK v1.90b] -> alignment/mapping [FUMA] -> variant calling [PLINK v1.90b] -> structure determination [Coot v0.9.8.1, PHENIX v1.20.1] -> stage not stated [Cellpose v2.0, ChimeraX, ImageJ, MAGMA, PyMOL, REGENIE v3.4.1, RELION v3.1]

### Structural basis of fast N-type inactivation in K&lt;sub&gt;v&lt;/sub&gt; channels. (Nature 2025)

- DOI: 10.1038/s41586-025-09339-7 | PMCID: PMC12460158 | PMID: 40770100
- Evidence: The model was then manually built in Coot 65 and refined using real_space_ refine in PHENIX 66 with secondary structure and geometry restraints.
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2, RELION, Topaz]

### Diffusing protein binders to intrinsically disordered proteins. (Nature 2025)

- DOI: 10.1038/s41586-025-09248-9 | PMCID: PMC12367549 | PMID: 40739343
- Version used: **1.21.1**
- Evidence: Structures were refined in Phenix (v1.21.1_5286) 45 .
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX v1.21.1] -> machine learning [RoseTTAFold] -> stage not stated [AlphaFold, ImageJ v1.54p, PyMOL v2.4.0, Python v3.9.7, UCSF Chimera v1.14]

### Programmable protein ligation on cell surfaces. (Nature 2025)

- DOI: 10.1038/s41586-025-09287-2 | PMCID: PMC12321220 | PMID: 40739351
- Evidence: Iterative rounds of model building in Coot 44 and refinements in PHENIX Refine (v.1.17_3644) 45 were performed to obtain the final structure.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, CCP4, PyMOL v2.5]

### ACLY inhibition promotes tumour immunity and suppresses liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09297-0 | PMCID: PMC12422966 | PMID: 40739358
- Evidence: ...h the atomic models for the CSS and CSH modules (extracted from Protein Data Bank (PDB) ID 6XHX ) were fitted using Chimera and real-space refined in Phenix 82 using reference restraints to the starting model.
- Full pipeline: quality control [Cutadapt, FastQC, Seurat] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [HISAT2] -> normalisation [Coot, Seurat] -> dimensionality reduction/clustering [Bioconductor, R, Seurat, clusterProfiler v4.4.4] -> differential/statistical testing [DESeq2, Seurat, limma v3.52.3] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [pheatmap] -> stage not stated [ImageJ, WGCNA v1.71]

### Loss of FCoV-23 spike domain 0 enhances fusogenicity and entry kinetics. (Nature 2025)

- DOI: 10.1038/s41586-025-09155-z | PMCID: PMC12408340 | PMID: 40634609
- Version used: **1.21**
- Evidence: The model was refined and rebuilt into the maps using Coot (v.0.9.8.8), Phenix (v.1.21) 85 and Rosetta (v.2021.07.61567) 86 , 87 .
- Full pipeline: structure determination [PHENIX v1.21] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Coot v0.9.8.8, RELION v5.0b, UCSF Chimera v1.8]

### Electron flow in hydrogenotrophic methanogens under nickel limitation. (Nature 2025)

- DOI: 10.1038/s41586-025-09229-y | PMCID: PMC12350162 | PMID: 40604290
- Evidence: Iterative rounds of PHENIX real-space refinement 55 and manual inspection and readjustment in COOT were performed to optimize the model stereochemistry and the fit to the cryo-EM density map as assessed with PHENIX, MolProbity 56 and Q-score 57 .
- Full pipeline: alignment/mapping [ChimeraX, IQ-TREE, MUSCLE] -> structure determination [PHENIX] -> stage not stated [AlphaFold v3.0, MotionCor2, RELION]

### Architecture, dynamics and biogenesis of GluA3 AMPA glutamate receptors. (Nature 2025)

- DOI: 10.1038/s41586-025-09325-z | PMCID: PMC12422969 | PMID: 40592473
- Version used: **1.20**
- Evidence: Model building and refinement UCSF ChimeraX 60 , PHENIX (v.1.20) 61 , COOT (v.0.9.8.95) 62 , Refmac-Servalcat 63 and PyMOL 2.5 (Schrödinger) were used for all molecular modelling and refinement.
- Full pipeline: alignment/mapping [Python] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot v0.9.8.95, PHENIX v1.20, PyMOL v2.5] -> stage not stated [RELION v5.0]

### Gating and noelin clustering of native Ca&lt;sup&gt;2+&lt;/sup&gt;-permeable AMPA receptors. (Nature 2025)

- DOI: 10.1038/s41586-025-09289-0 | PMCID: PMC12422955 | PMID: 40550474
- Evidence: The structure was manually adjusted in Coot, with stereochemical restraints applied 57 and further refined by real-space refinement using Phenix 58 .
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL v3.1] -> stage not stated [AlphaFold, ChimeraX, UCSF Chimera]

### Interactions between TTYH2 and APOE facilitate endosomal lipid transfer. (Nature 2025)

- DOI: 10.1038/s41586-025-09200-x | PMCID: PMC12328215 | PMID: 40562935
- Evidence: The structure of the complex was refined in Phenix 60 .
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, ImageJ, Python, RELION, Topaz]

### Decoding 4-vinylanisole biosynthesis and pivotal enzymes in locusts. (Nature 2025)

- DOI: 10.1038/s41586-025-09110-y | PMCID: PMC12350148 | PMID: 40562929
- Evidence: 21 , 22 ) as the search model and refined using Coot and Phenix.
- Full pipeline: quantification [ImageJ v1.51k] -> structure determination [PHENIX] -> stage not stated [AlphaFold v2.0]

### Complete computational design of high-efficiency Kemp elimination enzymes. (Nature 2025)

- DOI: 10.1038/s41586-025-09136-2 | PMCID: PMC12310539 | PMID: 40533551
- Evidence: Initial models were iteratively rebuilt and refined using COOT 63 and PHENIX 64 .
- Full pipeline: dimensionality reduction/clustering [MDTraj] -> simulation/modelling [MDTraj] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ColabFold, PyMOL, VMD]

### Protein-primed homopolymer synthesis by an antiviral reverse transcriptase. (Nature 2025)

- DOI: 10.1038/s41586-025-09179-5 | PMCID: PMC12483538 | PMID: 40436039
- Version used: **1.21.2**
- Evidence: After building the ncRNA, the complete model for the trimer was refined into the raw map using Phenix (v1.21.2–5419) RealSpaceRefinement 61 with reference model, secondary structure, and NCS restraints enabled.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, MAFFT, SAMtools, featureCounts] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX v1.21.2] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, BLAST, HMMER, R v4.4.0]

### Stepwise ATP translocation into the endoplasmic reticulum by human SLC35B1. (Nature 2025)

- DOI: 10.1038/s41586-025-09069-w | PMCID: PMC12267056 | PMID: 40399679
- Evidence: The final model containing the SLC35B1 transporter-Fv fragment was refined using real-space refinement in Phenix 59 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, Galaxy, PyMOL]

### Molecular basis of SIFI activity in the integrated stress response. (Nature 2025)

- DOI: 10.1038/s41586-025-09074-z | PMCID: PMC12286842 | PMID: 40328314
- Evidence: Coordinates of the medium-resolution to high-resolution regions were refined with multiple iterations of PHENIX real-space refinement 61 and manual refinement in Coot 62 .
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, PyMOL, Singularity]

### Naturally ornate RNA-only complexes revealed by cryo-EM. (Nature 2025)

- DOI: 10.1038/s41586-025-09073-0 | PMCID: PMC12286853 | PMID: 40328315
- Evidence: Validation metrics were calculated using Phenix, including phenix.rna_validate 59 – 61 .
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [Coot v0.9.8, MUSCLE] -> visualisation [AlphaFold] -> stage not stated [ChimeraX v1.8, PHENIX, RELION]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Version used: **1.21**
- Evidence: The model was then manually built and adjusted in Coot (v.1.1) 88 , followed by real-space refinement in Phenix (v.1.21) 89 (Supplementary Table 11 ).
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### Chromosome end protection by RAP1-mediated inhibition of DNA-PK. (Nature 2025)

- DOI: 10.1038/s41586-025-08896-1 | PMCID: PMC12221994 | PMID: 40240611
- Version used: **1.20.1**
- Evidence: Maps for the full end-binding complex and the locally refined densities were sharpened in cryoSPARC and combined using Phenix (v1.20.1) combine_focused_maps 46 .
- Full pipeline: structure determination [PHENIX v1.20.1] -> stage not stated [AlphaFold, ChimeraX, Coot]

### Structure of the ATP-driven methyl-coenzyme M reductase activation complex. (Nature 2025)

- DOI: 10.1038/s41586-025-08890-7 | PMCID: PMC12176620 | PMID: 40240609
- Version used: **1.21**
- Evidence: Coot (v.0.9.8.92) was used to manually rebuild the model followed by iterative real-space refinements in PHENIX (v.1.21-5207).
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [Coot v0.9.8.92, PHENIX v1.21] -> machine learning [Topaz] -> visualisation [ChimeraX v1.6.1] -> stage not stated [AlphaFold, IQ-TREE, UCSF Chimera v1.17.3]

### Re-adenylation by TENT5A enhances efficacy of SARS-CoV-2 mRNA vaccines. (Nature 2025)

- DOI: 10.1038/s41586-025-08842-1 | PMCID: PMC12095053 | PMID: 40240603
- Evidence: The imaging was started 4 h after transfection in Opera Phenix from Perkin Elmer using three channels: 488 nm (time: 50 ms, power: 20%, height: −8.0 µm); bright-field (time: 20 ms, power: 20%, height: −0.0 µm); digital phase contrast (time: 20 ms, power: 20 %, height: −1.0 µm); water objective 20× non-confocal; binning 2 × 2.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [SAMtools v1.9, STAR, minimap2 v2.17] -> quantification [featureCounts] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [Bioconductor, DESeq2 v1.22, R, STAR] -> visualisation [ggplot2] -> stage not stated [PHENIX, Python]

### DNA-guided transcription factor interactions extend human gene regulatory code. (Nature 2025)

- DOI: 10.1038/s41586-025-08844-z | PMCID: PMC12119339 | PMID: 40205063
- Evidence: Structure determination and refinement All structures were solved by molecular replacement using the program Phaser 74 as implemented in PHENIX 75 and CCP4 (ref.
- Full pipeline: differential/statistical testing [Bioconductor, ComplexHeatmap, Python, R, SciPy] -> structure determination [CCP4, PHENIX] -> machine learning [R] -> visualisation [Bioconductor, ComplexHeatmap] -> stage not stated [AlphaFold v2.0, BEDTools v2.30.0, Cytoscape, PyMOL, RoseTTAFold]

### Swinging lever mechanism of myosin directly shown by time-resolved cryo-EM. (Nature 2025)

- DOI: 10.1038/s41586-025-08876-5 | PMCID: PMC12158783 | PMID: 40205053
- Evidence: Real-space refinement was performed using Phenix 52 .
- Full pipeline: structure determination [PHENIX] -> stage not stated [MotionCor2, RELION]

### Small molecules restore mutant mitochondrial DNA polymerase activity. (Nature 2025)

- DOI: 10.1038/s41586-025-08856-9 | PMCID: PMC12158775 | PMID: 40205042
- Evidence: All final maps were sharpened using DeepEMhancer and Phenix Autosharpen 29 , 30 .
- Full pipeline: structure determination [ChimeraX v1.4, Coot v0.9.8.1] -> stage not stated [PHENIX]

### Glutamate gating of AMPA-subtype iGluRs at physiological temperatures. (Nature 2025)

- DOI: 10.1038/s41586-025-08770-0 | PMCID: PMC12074995 | PMID: 40140570
- Evidence: Model building, refinements and structural analysis ChimeraX 65 , ISOLDE 66 , Coot 67 and PHENIX 68 compiled by the SBgrid Consortium 69 were used in combination to perform the model building, refinements and structural analysis.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [ChimeraX, PHENIX] -> visualisation [Clustal Omega]

### A coronavirus assembly inhibitor that targets the viral membrane protein. (Nature 2025)

- DOI: 10.1038/s41586-025-08773-x | PMCID: PMC11981944 | PMID: 40140569
- Evidence: The model was then refined by performing iterative cycles of manual model building using Coot 65 and real-space refinement using Phenix 66 ; eLBOW was used to generate ligand restraints for CIM-834 (ref.
- Full pipeline: quantification [ImageJ] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [Coot, UCSF Chimera]

### A small-molecule SARS-CoV-2 inhibitor targeting the membrane protein. (Nature 2025)

- DOI: 10.1038/s41586-025-08651-6 | PMCID: PMC11981937 | PMID: 40140563
- Evidence: The FabB was fitted into the 3D map using Chimera and then further refined manually with COOT followed by real-space refinement in Phenix 69 .
- Full pipeline: structure determination [PHENIX]

### Structural dynamics of DNA unwinding by a replicative helicase. (Nature 2025)

- DOI: 10.1038/s41586-025-08766-w | PMCID: PMC12043514 | PMID: 40108462
- Evidence: Local resolution maps were calculated in Phenix and rendered on the full map (before postprocessing) with adjusted colouring.
- Full pipeline: structure determination [ChimeraX] -> visualisation [PHENIX, PyMOL v2.6.0, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1, MotionCor2, RELION, Topaz v0.3.0]

### Chanoclavine synthase operates by an NADPH-independent superoxide mechanism. (Nature 2025)

- DOI: 10.1038/s41586-025-08670-3 | PMCID: PMC12003167 | PMID: 40044871
- Version used: **1.20**
- Evidence: 50 ), followed by refinement against the corresponding map using the phenix.real_space_refine program in Phenix v.1.20 with geometry and secondary structure restraints imposed 51 .
- Full pipeline: structure determination [PHENIX v1.20] -> stage not stated [AlphaFold, Coot v0.9.6, UCSF Chimera]

### The conserved HIV-1 spacer peptide 2 triggers matrix lattice maturation. (Nature 2025)

- DOI: 10.1038/s41586-025-08624-9 | PMCID: PMC11964938 | PMID: 40011770
- Evidence: A single round of real-space refinement was then performed in Phenix-1.21.
- Full pipeline: structure determination [PHENIX] -> visualisation [RELION] -> stage not stated [AlphaFold v2.2.0, ChimeraX v1.3, Clustal Omega, Fiji v1.54f, ImageJ v1.54f]

### Structural dynamics of human fatty acid synthase in the condensing cycle. (Nature 2025)

- DOI: 10.1038/s41586-025-08782-w | PMCID: PMC12058526 | PMID: 39978408
- Evidence: The initial models were manually modified using Coot 66 , followed by several rounds of real-space refinement in Phenix 67 .
- Full pipeline: registration [MotionCor2, RELION] -> structure determination [ChimeraX, PHENIX] -> machine learning [cryoDRGN] -> visualisation [UCSF Chimera] -> stage not stated [CTFFIND, Coot]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Evidence: Quantitative analysis of fluorescence immunohistochemistry Fluorescent tiled images were generated on the Opera Phenix High-Content Screening System (Perkin Elmer) at ×20 magnification.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### Snapshots of acyl carrier protein shuttling in human fatty acid synthase. (Nature 2025)

- DOI: 10.1038/s41586-025-08587-x | PMCID: PMC12058525 | PMID: 39979457
- Evidence: For the condensing region, PDB 3HHD was manually fit into the density using ChimeraX and further refined using a combination of Coot 49 and Phenix 50 .
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Coot, RELION v3.1]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: The initial model was refined using Phenix.Refine 82 v.1.8.3 and manually adjusted in Coot 83 v.0.8.9.
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. (Nature 2025)

- DOI: 10.1038/s41586-024-08533-3 | PMCID: PMC11882451 | PMID: 39939763
- Version used: **1.20.1**
- Evidence: The resulting model was subsequently rebuilt in Coot (0.9.8.91) 64 on the basis of the protein sequences and the electron microscopy density and was further improved by real-space refinement in PHENIX (1.20.1-4487-000) 65 , 66 .
- Full pipeline: differential/statistical testing [R, limma] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1, Topaz] -> visualisation [Cytoscape v3.5.10, PyMOL] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, STRING db, ggplot2 v3.5.0, pandas v1.5.1]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Version used: **1.20.1**
- Evidence: The resulting model was subsequently rebuilt in Coot (v.0.9.8.91) 78 based on the protein sequences and the EM density and was further improved by real-space refinement in PHENIX (v.1.20.1-4487-000) 79 , 80 .
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### Targeting protein-ligand neosurfaces with a generalizable deep learning tool. (Nature 2025)

- DOI: 10.1038/s41586-024-08435-4 | PMCID: PMC11903328 | PMID: 39814890
- Evidence: Phases were obtained by molecular replacement using the Phaser module of the Phenix package (v.1.20.1-4487) and a model from PDB 1LRY in complex with our designed binder DBAct553_1 (ref.
- Full pipeline: structure determination [Coot v0.9.5] -> visualisation [ChimeraX, PyMOL v2.4] -> stage not stated [AlphaFold, ColabFold, PHENIX, RDKit, RoseTTAFold]

### De novo designed proteins neutralize lethal snake venom toxins. (Nature 2025)

- DOI: 10.1038/s41586-024-08393-x | PMCID: PMC11882462 | PMID: 39814879
- Evidence: Following molecular replacement, the model was improved and refined using Phenix 67 .
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### Engineered enzymes for enantioselective nucleophilic aromatic substitutions. (Nature 2025)

- DOI: 10.1038/s41586-025-08611-0 | PMCID: PMC11903332 | PMID: 39814071
- Evidence: Iterative cycles of rebuilding and refinement were performed in COOT 47 and Phenix.refine 48 , respectively.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [PHENIX] -> stage not stated [AutoDock Vina]

### Conformational protection of molybdenum nitrogenase by Shethna protein II. (Nature 2025)

- DOI: 10.1038/s41586-024-08355-3 | PMCID: PMC11754109 | PMID: 39779845
- Evidence: All models were rigid-body fitted into the density map using UCSF ChimeraX 50 , hand-refined using COOT 51 , applied C 2 symmetry and real-space refined in PHENIX 52 .
- Full pipeline: structure determination [ChimeraX, PHENIX, RELION v3.1] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4, CTFFIND v4.1]

### Bidirectional histone monoaminylation dynamics regulate neural rhythmicity. (Nature 2025)

- DOI: 10.1038/s41586-024-08371-3 | PMCID: PMC11754111 | PMID: 39779849
- Evidence: All structures were refined using PHENIX 58 , with iterative manual model building using COOT 59 .
- Full pipeline: alignment/mapping [Bowtie2 v2.5.0, STAR v2.7.11b] -> quantification [ImageJ] -> normalisation [ImageJ, deepTools v3.5.1] -> structure determination [PHENIX] -> visualisation [tidyverse v2.0.0] -> stage not stated [BEDTools, Enrichr, HOMER v4.11, HTSeq v2.0.5, MACS2 v3.0.0a, R, SAMtools v1.9]

### Structural diversity of axonemes across mammalian motile cilia. (Nature 2025)

- DOI: 10.1038/s41586-024-08337-5 | PMCID: PMC11779644 | PMID: 39743588
- Evidence: Individual PDB files were merged and given unique chain IDs in ChimeraX, then real-space refined in Phenix 78 using a non-bonded weight of 500.
- Full pipeline: alignment/mapping [IMOD] -> registration [IMOD] -> dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot]

### The structure of apolipoprotein B100 from human low-density lipoprotein. (Nature 2025)

- DOI: 10.1038/s41586-024-08467-w | PMCID: PMC11839476 | PMID: 39662503
- Version used: **1.20**
- Evidence: To refine the model stereochemistry, the entire apoB100 structure was first subjected to a series of restrained equilibration simulations and conjugate gradient energy minimizations in explicit solvent, followed by real-space refinement in Phenix (v.1.20) 50 and, finally, manual refinement using ISOLDE 51 .
- Full pipeline: simulation/modelling [NAMD v2.14, PHENIX v1.20] -> structure determination [PHENIX v1.20] -> machine learning [PHENIX v1.20] -> visualisation [ChimeraX, VMD v1.9.4] -> stage not stated [AlphaFold, ColabFold]

### Structure and mechanism of the Zorya anti-phage defence system. (Nature 2025)

- DOI: 10.1038/s41586-024-08493-8 | PMCID: PMC11946911 | PMID: 39662505
- Evidence: The model was then refined against the map using PHENIX real space refinement 51 .
- Full pipeline: alignment/mapping [MUSCLE v5.1] -> dimensionality reduction/clustering [ColabFold v1.5.2, MUSCLE v5.1] -> simulation/modelling [GROMACS v2022.5, PyMOL] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, Python, ilastik]

### Synthetic GPCRs for programmable sensing and control of cell behaviour. (Nature 2025)

- DOI: 10.1038/s41586-024-08282-3 | PMCID: PMC11666456 | PMID: 39633047
- Evidence: Fluorescence imaging of GRAB sensors and PAGER FL The Opera Phenix high-content screening system (PerkinElmer) was utilized for GRAB sensors and PAGER FL imaging, equipped with a 20× 0.4-NA objective, a 40× 0.6-NA objective, a 40× 1.15-NA water-immersion objective, a 488-nm laser, and a 561-nm laser.
- Full pipeline: quantification [Matplotlib] -> differential/statistical testing [SciPy, seaborn] -> stage not stated [AlphaFold, ImageJ, MACS2, PHENIX, Python]

### Autoinhibition of dimeric NINJ1 prevents plasma membrane rupture. (Nature 2025)

- DOI: 10.1038/s41586-024-08273-4 | PMCID: PMC11711097 | PMID: 39476863
- Evidence: Map interpretability was further improved by density modification using Phenix Resolve cryo-EM 28 .
- Full pipeline: simulation/modelling [seaborn] -> structure determination [AlphaFold, ChimeraX] -> visualisation [PyMOL v2.5.2, seaborn] -> stage not stated [PHENIX]

### Substrate selectivity of the human RNA m&lt;sup&gt;5&lt;/sup&gt;C methyltransferase NSUN2. (Nature 2026)

- DOI: 10.1038/s41586-026-10582-9 | PMCID: PMC13289585 | PMID: 42203868
- Version used: **1.21.1**
- Evidence: Initial models ( Extended Data Table 1 ) were docked into cryo-EM maps using ChimeraX v.1.8 and were further built and refined using COOT v.0.9.8.7 and Phenix v.1.21.1 (refs.
- Full pipeline: alignment/mapping [Clustal Omega v1.2.4] -> structure determination [ChimeraX v1.8, PHENIX v1.21.1] -> stage not stated [AlphaFold, CCP4]

### Vaccination generates broadly cross-neutralizing antibodies to the HIV Env apex. (Nature 2026)

- DOI: 10.1038/s41586-026-10429-3 | PMCID: PMC13275315 | PMID: 42056526
- Evidence: Structure determination was carried out by molecular replacement using Phaser within the Phenix software suite 51 , with an initial model generated by AlphaFold 3 52 .
- Full pipeline: structure determination [AlphaFold, Coot v0.9.8, PHENIX] -> stage not stated [ChimeraX, RELION v4.0]

### Structural basis of fungal β-1,3-glucan synthase inhibition by caspofungin. (Nature 2026)

- DOI: 10.1038/s41586-026-10409-7 | PMCID: PMC13249079 | PMID: 42020744
- Version used: **1.20**
- Evidence: The restraints for lipids and ligands, including PE, UDP, CFN and GTPγS were generated in the Grade2 server 51 and optimized in eLBOW (as implemented in Phenix v.1.20 (ref.
- Full pipeline: alignment/mapping [UCSF Chimera] -> registration [RELION] -> simulation/modelling [GROMACS, MDAnalysis v2.7.0, Python, VMD v1.9] -> structure determination [Coot v0.98, UCSF Chimera] -> visualisation [MDAnalysis v2.7.0, Python, VMD v1.9] -> stage not stated [AlphaFold, ChimeraX v1.10, PHENIX v1.20, PyMOL v3.1]

### Myosin forces remodel F-actin for mechanosensitive protein recognition. (Nature 2026)

- DOI: 10.1038/s41586-026-10398-7 | PMCID: PMC13233326 | PMID: 42020745
- Evidence: These 25 protomers were combined into a single PDB model for each map, and these combined models were subjected to Phenix geometry minimization with default parameters of 500 maximum iterations and 5 macro cycles in order to remove clashes.
- Full pipeline: simulation/modelling [Python] -> structure determination [IMOD] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [EMAN2, MotionCor2, PHENIX, RELION, SciPy]

### Template-driven scaffolding of SCF&lt;sup&gt;FBXO42&lt;/sup&gt; regulates PP2A degradation. (Nature 2026)

- DOI: 10.1038/s41586-026-10368-z | PMCID: PMC13233325 | PMID: 41986709
- Evidence: Images were taken either using a ×20 objective and analysed using the OPERA PHENIX confocal screening system or a ×60 objective on the Nikon Crest spinning-disc confocal microscope.
- Full pipeline: quantification [limma] -> differential/statistical testing [limma] -> stage not stated [AlphaFold, Bioconductor, ChimeraX, Coot, PHENIX, R]

### Cytoplasmic lattices are megadalton storage complexes in mammalian oocytes. (Nature 2026)

- DOI: 10.1038/s41586-026-10513-8 | PMCID: PMC13253339 | PMID: 41986725
- Evidence: We then iteratively refined the model in Phenix 56 with manual adjustment in Coot 57 .
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [AlphaFold, RELION]

### Molecular basis for methylation-sensitive editing by Cas9. (Nature 2026)

- DOI: 10.1038/s41586-026-10384-z | PMCID: PMC13216068 | PMID: 41986708
- Evidence: Structural models were built in COOT 66 and refined in PHENIX 67 to satisfactory stereochemistry and real-space map correlation parameters.
- Full pipeline: registration [CTFFIND] -> differential/statistical testing [Python, R] -> structure determination [PHENIX, RELION v4.0] -> stage not stated [Topaz]

### Synthetic super-enhancers enable precision viral immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10329-6 | PMCID: PMC13149004 | PMID: 41951744
- Evidence: Images were acquired using an Opera Phenix Plus high-content imaging system (Revvity) equipped with a ×40/1.1 NA water-immersion objective.
- Full pipeline: quantification [ImageJ v2.8] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [ImageJ v2.8] -> stage not stated [BEDTools, HOMER, MACS2, PHENIX, R, SCENIC, scDblFinder]

### A µ-opioid receptor superagonist analgesic with minimal adverse effects. (Nature 2026)

- DOI: 10.1038/s41586-026-10299-9 | PMCID: PMC13128446 | PMID: 41922775
- Evidence: Manual model building was performed in Coot v.0.9.8.1 EL 78 with refinement in Phenix 79 .
- Full pipeline: normalisation [R] -> registration [RELION] -> structure determination [Coot v0.9.8.1, PHENIX]

### Structural basis of supercoiling-induced CRISPR-Cas9 off-target activity. (Nature 2026)

- DOI: 10.1038/s41586-026-10255-7 | PMCID: PMC13171457 | PMID: 41882360
- Evidence: Finally, the initial models were used as a reference for real-space refinement in Phenix with three macro cycles under the default reference restraints.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX, RELION] -> stage not stated [AlphaFold, Fiji, ImageJ, Topaz]

### Ectopic NMDAR expression in cancer unmasks germline-encoded autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10278-0 | PMCID: PMC13216075 | PMID: 41882353
- Evidence: Models were built using UCSF ChimeraX 90 and WinCoot 91 , with real-space refinement performed in PHENIX 92 (non-bonded weight set to 500).
- Full pipeline: alignment/mapping [UMAP, edgeR] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX, PHENIX] -> stage not stated [Fiji, ImageJ, MACS2, QuPath, R, RELION, Seurat]

### The E3 ubiquitin ligase mechanism specifying targeted microRNA degradation. (Nature 2026)

- DOI: 10.1038/s41586-026-10232-0 | PMCID: PMC13083262 | PMID: 41851464
- Evidence: Iterative manual model building in COOT and real-space refinement using Phenix.refine were performed until a satisfactory map-to-model correlation was achieved 79 , 80 .
- Full pipeline: read trimming [Cutadapt v4.8] -> quantification [R] -> normalisation [DESeq2 v1.38.3] -> differential/statistical testing [R] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold]

### Structures of Marburgvirus glycoprotein and its complex with NPC1 receptor. (Nature 2026)

- DOI: 10.1038/s41586-026-10240-0 | PMCID: PMC13171430 | PMID: 41813895
- Version used: **1.16**
- Evidence: Refinement was performed using Phenix (v1.16) 45 , with additional manual adjustments in Coot (v0.8.9).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX v1.16] -> visualisation [ChimeraX v0.93, PyMOL] -> stage not stated [CTFFIND v4.1.13, Coot v0.8.9]

### B cell imprinting in children impairs antibodies to the haemagglutinin stalk. (Nature 2026)

- DOI: 10.1038/s41586-026-10248-6 | PMCID: PMC13171607 | PMID: 41813896
- Evidence: The models were manually adjusted using Coot (v.0.9.8) 58 and further refined through Rosetta Relax 59 and real-space refinement in Phenix 60 .
- Full pipeline: quality control [Seurat v4.3.0, UMAP] -> alignment/mapping [Clustal Omega] -> normalisation [Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.3.0, UMAP, fgsea] -> differential/statistical testing [Seurat v4.3.0, UMAP] -> structure determination [Coot v0.9.8, PHENIX] -> visualisation [R v4.2, Seurat v4.3.0, UMAP, ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python]

### Snapshots of the dynamic basis of NTSR1 G protein subtype promiscuity. (Nature 2026)

- DOI: 10.1038/s41586-026-10120-7 | PMCID: PMC13083256 | PMID: 41813894
- Evidence: Manual model building was performed in Coot 47 with refinement in Phenix 48 .
- Full pipeline: simulation/modelling [NAMD] -> structure determination [Coot, PHENIX] -> stage not stated [Python, VMD]

### Mechanism of co-transcriptional cap snatching by influenza polymerase. (Nature 2026)

- DOI: 10.1038/s41586-026-10189-0 | PMCID: PMC13128444 | PMID: 41781612
- Evidence: Then, the individual protein components were subjected to Real Space Refinement in PHENIX 70 and manual curation in Coot.
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> stage not stated [ChimeraX v1.6.1, Coot, RELION]

### DICER cleavage fidelity is governed by 5'-end binding pockets. (Nature 2026)

- DOI: 10.1038/s41586-026-10211-5 | PMCID: PMC13171623 | PMID: 41781616
- Version used: **1.20.1**
- Evidence: The manually fitted models were further refined using phenix.real_space_refine in PHENIX (v.1.20.1) 51 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, Bowtie2, Coot v0.9.8.96] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.7, Coot v0.9.8.96, PHENIX v1.20.1] -> stage not stated [PyMOL]

### CLCC1 promotes hepatic neutral lipid flux and nuclear pore complex assembly. (Nature 2026)

- DOI: 10.1038/s41586-025-10064-4 | PMCID: PMC13061601 | PMID: 41741636
- Evidence: Live cells were imaged using an Opera Phenix Plus High-Content Screening System (Perkin Elmer) confocal microscope equipped with a 40× water immersion objective using DAPI and GFP filters.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3] -> quantification [Fiji v1.53e, ImageJ v1.53e, Python v3.0] -> simulation/modelling [ColabFold, GROMACS v2023.3] -> visualisation [Fiji v1.53e, ImageJ v1.53e, PyMOL v2.5.0] -> stage not stated [AlphaFold, DESeq2 v1.5, HMMER, PHENIX, STRING db]

### CSN5i-3 is an orthosteric molecular glue inhibitor of COP9 signalosome. (Nature 2026)

- DOI: 10.1038/s41586-026-10129-y | PMCID: PMC13128448 | PMID: 41673158
- Evidence: The CSN5i-3 model from 5JOG was fitted into the 3.3 Å CSN5i-3–CSN EM map and refined using Phenix.
- Full pipeline: structure determination [PHENIX, Topaz] -> stage not stated [ChimeraX, Coot, PyMOL]

### Bacterial immune activation via supramolecular assembly with phage triggers. (Nature 2026)

- DOI: 10.1038/s41586-025-10060-8 | PMCID: PMC13017515 | PMID: 41639456
- Evidence: The Gp77-focused map enabled docking of residues 1–125 into the inner ring using ‘phenix.local_em_fitting’ in ChimeraX, followed by manual adjustments in Coot and subsequent refinement in Phenix.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, Cutadapt v1.15] -> alignment/mapping [Bowtie2 v2.3.4.1, Cutadapt v1.15, MAFFT, NumPy, SAMtools v1.7] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> machine learning [Topaz]

### A prophage-encoded abortive infection protein preserves host and prophage spread. (Nature 2026)

- DOI: 10.1038/s41586-025-10070-6 | PMCID: PMC13043305 | PMID: 41606329
- Evidence: Data were processed with autoPROC and Aimless 56 – 58 Experimental phase information was determined by molecular replacement using Phaser-MR in PHENIX 59 .
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT] -> structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [AlphaFold, BEDTools v2.27.1, PHENIX, SAMtools v1.1]

### Fibroblastic reticular cells direct the initiation of T cell responses via CD44. (Nature 2026)

- DOI: 10.1038/s41586-025-09988-8 | PMCID: PMC12999478 | PMID: 41565815
- Evidence: Cultures were imaged with the Opera Phenix Plus High-Content Screening System (PerkinElmer) for 4 h at 37 °C with 5% CO 2 .
- Full pipeline: normalisation [CCP4] -> structure determination [Coot] -> stage not stated [CellProfiler, ImageJ, PHENIX, PyMOL]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Evidence: Each model was real space refined into its respective map using PHENIX 61 with global minimization, Ramachandran, secondary structure and ligand restraints.
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### RNA-triggered Cas12a3 cleaves tRNA tails to execute bacterial immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09852-9 | PMCID: PMC12851939 | PMID: 41501459
- Version used: **1.20.1**
- Evidence: The resulting models were further refined with real-space refinement and validated in Phenix (v.1.20.1) 79 .
- Full pipeline: read trimming [BWA v0.7.17, IQ-TREE v2.3.6, Trimmomatic v0.39] -> alignment/mapping [BLAST, BWA v0.7.17, Clustal Omega, IQ-TREE v2.3.6] -> structure determination [AlphaFold, ChimeraX v1.7, IQ-TREE v2.3.6, PHENIX v1.20.1] -> visualisation [Matplotlib, Python] -> stage not stated [SAMtools v1.9]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: Stained sections were imaged with a Perkin Elmer Opera Phenix High-Content Screening system in confocal mode with 1-μm z step size, using a ×20 (NA 0.16, 0.299 μm pixel –1 ), ×40 (NA 1.1, 0.149 μm pixel –1 ) or ×63 (NA 1.15, 0.091 μm pixel –1 ) water-immersion objective.
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Computational enzyme design by catalytic motif scaffolding. (Nature 2026)

- DOI: 10.1038/s41586-025-09747-9 | PMCID: PMC12727513 | PMID: 41339546
- Evidence: The best solution was refined in reciprocal space with PHENIX 61 with 5% of the data used for R free and by real-space fitting steps against σA -weighted 2 F o – F c and F o – F c electron density maps using COOT 62 .
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis] -> structure determination [PHENIX] -> stage not stated [AlphaFold, SciPy]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Evidence: High-content confocal imaging and data analysis Cells were imaged using the PerkinElmer Opera Phenix automated microscope run on the Harmony software (v.4.9 or later) and using the pre-set filter settings for DAPI (BFP), AF-488 (GFP), AF-647 (TMUB1), mCherry and brightfield.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### Structural basis of regulated N-glycosylation at the secretory translocon. (Nature 2026)

- DOI: 10.1038/s41586-025-09756-8 | PMCID: PMC12804085 | PMID: 41261126
- Evidence: The translocon model was subjected to real-space refinement in PHENIX 80 alone (versus Map 1) or after combining with the 60S model (versus Map 2).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [TopHat v2.1.0] -> quantification [HTSeq v2.0.3] -> structure determination [Coot, PHENIX] -> machine learning [Coot] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

### ZAK activation at the collided ribosome. (Nature 2026)

- DOI: 10.1038/s41586-025-09772-8 | PMCID: PMC12823453 | PMID: 41261136
- Version used: **1.20.1**
- Evidence: These models were processed by manual real-space refinement in WinCoot (v0.9.8.93) 63 and merged into a disome model followed by real-space refinement in Phenix (v1.20.1-4487) 64 .
- Full pipeline: read trimming [SAMtools, Trim Galore] -> alignment/mapping [MotionCor2 v1.4.0, SAMtools, STAR] -> structure determination [AlphaFold, ChimeraX v1.9, PHENIX v1.20.1, UCSF Chimera] -> stage not stated [Coot, RELION v5.0]

### Hepatic zonation determines tumorigenic potential of mutant β-catenin. (Nature 2026)

- DOI: 10.1038/s41586-025-09733-1 | PMCID: PMC12804091 | PMID: 41261129
- Evidence: Image analysis Immunofluorescent images were acquired in up to four fluorescent channels at ×20 magnification on an Opera Phenix high-content imaging system (Perkin Elmer) and subsequently analysed using the Columbus software (v2.9.1.532; Perkin Elmer).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.18, HISAT2 v2.1.0, SAMtools v1.9, Trim Galore, featureCounts v1.6.4] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.1.0, featureCounts v1.6.4] -> normalisation [DESeq2 v1.36, RSEM] -> visualisation [ggplot2] -> stage not stated [Fiji, GSEA, GSVA, ImageJ, PHENIX, R]

### Potent neutralization of Marburg virus by a vaccine-elicited antibody. (Nature 2026)

- DOI: 10.1038/s41586-025-09868-1 | PMCID: PMC12893919 | PMID: 41225006
- Evidence: The model was then built and refined into the map using Coot, Rosetta 77 , 78 , ISOLDE 79 and Phenix 80 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39] -> differential/statistical testing [RELION] -> structure determination [AlphaFold, ChimeraX, PHENIX]

### Nanometer-resolution in situ structure of the SARS-CoV-2 postfusion spike protein. (PNAS 2021)

- DOI: 10.1073/pnas.2112703118 | PMCID: PMC8640741 | PMID: 34782481
- Evidence: The final model was refined according to the map using PHENIX.Refine ( 42 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [IMOD, RELION]

### Kinetic proofreading of lipochitooligosaccharides determines signal activation of symbiotic plant receptors. (PNAS 2021)

- DOI: 10.1073/pnas.2111031118 | PMCID: PMC8612216 | PMID: 34716271
- Evidence: Model building of both NFP and LYS11 was done in COOT ( 45 ) and refined using the PHENIX suite ( 46 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL v2.4.1]

### Vascular K<sub>ATP</sub> channel structural dynamics reveal regulatory mechanism by Mg-nucleotides. (PNAS 2021)

- DOI: 10.1073/pnas.2109441118 | PMCID: PMC8694068 | PMID: 34711681
- Evidence: Models were built by fitting previously published Kir6.2/SUR1 structures and in SWISS-MODEL and refined in Coot and Phenix.
- Full pipeline: simulation/modelling [GROMACS v2019.4] -> structure determination [Coot, PHENIX] -> stage not stated [RELION]

### A designer rice NLR immune receptor confers resistance to the rice blast fungus carrying noncorresponding avirulence effectors. (PNAS 2021)

- DOI: 10.1073/pnas.2110751118 | PMCID: PMC8612214 | PMID: 34702740
- Evidence: Structures were improved by rebuilding amino acids into the electron density using Coot ( 54 ) and further refined using PHENIX with Translation/Libration/Screw restraints ( 55 ).
- Full pipeline: differential/statistical testing [ImageJ] -> structure determination [PHENIX]

### Structure of the ATP synthase from <i>Mycobacterium smegmatis</i> provides targets for treating tuberculosis. (PNAS 2021)

- DOI: 10.1073/pnas.2111899118 | PMCID: PMC8617483 | PMID: 34782468
- Evidence: Model building into focused maps was performed with Coot ( 32 ), and real space refinement with PHENIX ( 33 – 35 ).
- Full pipeline: structure determination [PHENIX, RELION]

### Cryo-EM structure determination of small proteins by nanobody-binding scaffolds (Legobodies). (PNAS 2021)

- DOI: 10.1073/pnas.2115001118 | PMCID: PMC8521671 | PMID: 34620716
- Evidence: For the crystal structure of Nb_0/Fab_8D3, the initial phases were obtained by molecular replacement using the Phaser module in Phenix ( 42 ).
- Full pipeline: registration [MotionCor2] -> stage not stated [Coot, PHENIX, RELION v3.1]

### Constitutive signal bias mediated by the human GHRHR splice variant 1. (PNAS 2021)

- DOI: 10.1073/pnas.2106606118 | PMCID: PMC8501799 | PMID: 34599099
- Evidence: The models were then subjected to ISOLDE ( 74 ) for further rebuilding and finalized using real-space refinement in PHENIX ( 75 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v1.18, RELION]

### Structural basis of rotavirus RNA chaperone displacement and RNA annealing. (PNAS 2021)

- DOI: 10.1073/pnas.2100198118 | PMCID: PMC8521686 | PMID: 34615715
- Evidence: The Namdinator model was used for multiple iterative rounds of manual adjustment in Coot ( 55 ) and real-space refinement in Phenix ( 56 ).
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ImageJ] -> stage not stated [RELION]

### Mechanistic insights into central spindle assembly mediated by the centralspindlin complex. (PNAS 2021)

- DOI: 10.1073/pnas.2112039118 | PMCID: PMC8501884 | PMID: 34588311
- Evidence: Model refinement was done with Phenix, with R work /R free = 0.2348/0.2765, Ramachandran outlier 0.13% for Z430-555/C120 and R work /R free = 0.2331/0.2706, Ramachandran outlier 0.0% for Z530-601.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ImageJ]

### Structural basis for isoform-specific inhibition of human CTPS1. (PNAS 2021)

- DOI: 10.1073/pnas.2107968118 | PMCID: PMC8501788 | PMID: 34583994
- Evidence: Finally, density modification was performed using ResolveCryoEM in Phenix ( 66 , 67 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> stage not stated [PHENIX]

### The citron homology domain as a scaffold for Rho1 signaling. (PNAS 2021)

- DOI: 10.1073/pnas.2110298118 | PMCID: PMC8488606 | PMID: 34544876
- Evidence: Experimental phases were obtained from the derivative data by Selenium Single-wavelength anomalous diffraction (Se-SAD) phasing with the AutoSol and Autobuild options in PHENIX program suite ( 64 ).
- Full pipeline: stage not stated [PHENIX, PyMOL]

### DNA-encoded chemistry technology yields expedient access to SARS-CoV-2 M&lt;sup&gt;pro&lt;/sup&gt; inhibitors. (PNAS 2021)

- DOI: 10.1073/pnas.2111172118 | PMCID: PMC8433497 | PMID: 34426525
- Evidence: Structures were further refined several rounds using PHENIX.refine and Crystallography Object-Oriented Toolkit (Coot) ( 46 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [UCSF Chimera]

### Structure of autoinhibited Akt1 reveals mechanism of PIP&lt;sub&gt;3&lt;/sub&gt;-mediated activation. (PNAS 2021)

- DOI: 10.1073/pnas.2101496118 | PMCID: PMC8379990 | PMID: 34385319
- Evidence: The model was built in Coot ( 60 ) with iterative rounds of refinement and model validation in PHENIX ( 61 ).
- Full pipeline: structure determination [Coot, PHENIX]

### Native structure of the RhopH complex, a key determinant of malaria parasite nutrient acquisition. (PNAS 2021)

- DOI: 10.1073/pnas.2100514118 | PMCID: PMC8536402 | PMID: 34446549
- Evidence: Finally, resulting models for the complexes were subjected to iterative cycles of automated refinement using the phenix.real_space_refine program in PHENIX ( 53 ) followed by further manual refinement, performed against a map visually determined to possess the best mix of overall features for each local region, to achieve the final structure.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> stage not stated [RELION, UCSF Chimera]

### Molecular insights into differentiated ligand recognition of the human parathyroid hormone receptor 2. (PNAS 2021)

- DOI: 10.1073/pnas.2101279118 | PMCID: PMC8364112 | PMID: 34353904
- Evidence: Real-space refinement was performed using Phenix ( 34 ).
- Full pipeline: simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> visualisation [PyMOL]

### Evolution of a σ-(c-di-GMP)-anti-σ switch. (PNAS 2021)

- DOI: 10.1073/pnas.2105447118 | PMCID: PMC8325347 | PMID: 34290147
- Evidence: Autosol in Phenix was used to locate selenium sites, perform heavy atom refinement, and carry out density modification ( 46 ).
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX, RAxML v8.2.10]

### Postinfection treatment with a protease inhibitor increases survival of mice with a fatal SARS-CoV-2 infection. (PNAS 2021)

- DOI: 10.1073/pnas.2101555118 | PMCID: PMC8307543 | PMID: 34210738
- Evidence: Structure refinement and manual model building were conducted with Phenix ( 55 ) and Coot ( 56 ), respectively.
- Full pipeline: structure determination [PHENIX]

### Structural basis for ligand binding modes of CTP synthase. (PNAS 2021)

- DOI: 10.1073/pnas.2026621118 | PMCID: PMC8325340 | PMID: 34301892
- Evidence: The tetramer models were subsequently real-space refined in Python-based hierarchical environment for integrated xtallography (Phenix) software ( 40 ).
- Full pipeline: structure determination [PHENIX, Python]

### Computational design of a synthetic PD-1 agonist. (PNAS 2021)

- DOI: 10.1073/pnas.2102164118 | PMCID: PMC8307378 | PMID: 34272285
- Evidence: The structure was solved by molecular replacement using PHASER ( 43 ) in the PHENIX software suite ( 44 ) and the helix (residues 18 to 31) from the GR918 design model as a search model, with SHELXE ( 45 ) used for model completion.
- Full pipeline: stage not stated [PHENIX]

### Large-scale ratcheting in a bacterial DEAH/RHA-type RNA helicase that modulates antibiotics susceptibility. (PNAS 2021)

- DOI: 10.1073/pnas.2100370118 | PMCID: PMC8325345 | PMID: 34290142
- Evidence: Experimental phases for HrpA 1-783,SeMet were determined via the single anomalous diffraction strategy using Phenix ( 74 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [PHENIX]

### Structural differences in the FAD-binding pockets and lid loops of mammalian CRY1 and CRY2 for isoform-selective regulation. (PNAS 2021)

- DOI: 10.1073/pnas.2026191118 | PMCID: PMC8255803 | PMID: 34172584
- Evidence: A polder (omit) map (gray mesh) was produced by omitting KL001 in the Phenix Polder Maps utility and is shown for KL001 with a contour level of 3.0 σ.
- Full pipeline: stage not stated [PHENIX]

### Periscope Proteins are variable-length regulators of bacterial cell surface interactions. (PNAS 2021)

- DOI: 10.1073/pnas.2101349118 | PMCID: PMC8201768 | PMID: 34074781
- Evidence: Models were manually built using Coot ( 42 ) and refined to completion with REFMAC5 ( 43 ) for Sgo_R3-4 and PHENIX ( 44 ) for Sgo_R10 ( Table 1 ).
- Full pipeline: dimensionality reduction/clustering [BLAST] -> simulation/modelling [NAMD] -> structure determination [PHENIX]

### High-resolution asymmetric structure of a Fab-virus complex reveals overlap with the receptor binding site. (PNAS 2021)

- DOI: 10.1073/pnas.2025452118 | PMCID: PMC8201801 | PMID: 34074770
- Evidence: Atomic models were built using Coot ( 29 ) and Phenix ( 30 ), using crystal structures 2CAS (CPV) and 3GK8 (Fab 14) as starting models ( 18 , 22 ), before validation in MolProbity ( 45 ).
- Full pipeline: registration [RELION] -> simulation/modelling [Coot] -> structure determination [RELION] -> stage not stated [PHENIX]

### Structures suggest an approach for converting weak self-peptide tumor antigens into superagonists for CD8 T cells in cancer. (PNAS 2021)

- DOI: 10.1073/pnas.2100588118 | PMCID: PMC8201969 | PMID: 34074778
- Evidence: The models from the molecular replacement were built using Crystallographic Object-Oriented Toolkit, program 9 ( 67 ) and subsequently subjected to refinement using Phenix software ( 68 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4]

### Structure of AMH bound to AMHR2 provides insight into a unique signaling pair in the TGF-β family. (PNAS 2021)

- DOI: 10.1073/pnas.2104809118 | PMCID: PMC8256043 | PMID: 34155118
- Evidence: A molecular replacement solution was identified using Phaser within the Phenix suite ( 38 ).
- Full pipeline: stage not stated [PHENIX]

### ICAM-1 induced rearrangements of capsid and genome prime rhinovirus 14 for activation and uncoating. (PNAS 2021)

- DOI: 10.1073/pnas.2024251118 | PMCID: PMC8126848 | PMID: 33947819
- Evidence: The fitted models were subjected to multiple rounds of real-space refinement in Phenix (version dev-3765), reciprocal-space refinement in REFMAC5, combined with manual corrections in Coot 0.9 and ISOLDE ( 75 – 78 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot v0.9, PHENIX]

### Nanobody cocktails potently neutralize SARS-CoV-2 D614G N501Y variant and protect mice. (PNAS 2021)

- DOI: 10.1073/pnas.2101918118 | PMCID: PMC8126837 | PMID: 33893175
- Evidence: For the “best RBD+WNb 2+WNb 10” map, the high-resolution model of RBD-WNb 2 from the crystal structure was used for rigid-body docking of the RBD, WNb2, and WNb 10, followed by iterative model adjustment, rebuilding in COOT ( 71 ), and real-space refinement in PHENIX ( 72 ).
- Full pipeline: dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, MotionCor2]

### Cryo-EM structure of <i>Mycobacterium smegmatis</i> DyP-loaded encapsulin. (PNAS 2021)

- DOI: 10.1073/pnas.2025658118 | PMCID: PMC8072242 | PMID: 33853951
- Evidence: Then Ms-Enc and Ms-DyP models were built manually in Coot ( 58 ) by mutating amino acid residues and further refined using real-space refinement in Phenix ( 59 ).
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> dimensionality reduction/clustering [RELION] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [UCSF Chimera]

### Structure of Gcn1 bound to stalled and colliding 80S ribosomes. (PNAS 2021)

- DOI: 10.1073/pnas.2022756118 | PMCID: PMC8040806 | PMID: 33790014
- Evidence: Molecular models were generated using SWISS-MODEL ( 50 ), UCSF Chimera 1.13.1 ( 51 ), Coot ( 52 ), and ISOLDE ( 53 ), and refinement was performed using PHENIX ( 54 ).
- Full pipeline: structure determination [PHENIX, UCSF Chimera v1.13.1] -> stage not stated [ChimeraX, RELION]

### Architecture of the mycobacterial succinate dehydrogenase with a membrane-embedded Rieske FeS cluster. (PNAS 2021)

- DOI: 10.1073/pnas.2022308118 | PMCID: PMC8054011 | PMID: 33876763
- Evidence: The density quality of the interior region was higher, so model building commenced here, followed by iterative manual fitting adjustment in Coot ( 41 ) and real space refinement in PHENIX ( 42 ).
- Full pipeline: registration [CTFFIND, MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL]

### Transferrin receptor targeting by de novo sheet extension. (PNAS 2021)

- DOI: 10.1073/pnas.2021569118 | PMCID: PMC8092486 | PMID: 33879614
- Evidence: Structures were refined in Phenix ( 43 ) using phenix.autobuild and phenix.refine or Refmac ( 44 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [Python]

### Early-stage dynamics of chloride ion-pumping rhodopsin revealed by a femtosecond X-ray laser. (PNAS 2021)

- DOI: 10.1073/pnas.2020486118 | PMCID: PMC8020794 | PMID: 33753488
- Evidence: Restraints for RLY were prepared using the eLBOW program in PHENIX ( 43 , 44 ).
- Full pipeline: simulation/modelling [GROMACS v5.1.2, VMD] -> structure determination [Coot] -> visualisation [VMD] -> stage not stated [CCP4, PHENIX, UCSF Chimera]

### Structure of a bacterial OapB protein with its OLE RNA target gives insights into the architecture of the OLE ribonucleoprotein complex. (PNAS 2021)

- DOI: 10.1073/pnas.2020393118 | PMCID: PMC7936274 | PMID: 33619097
- Evidence: The initial models were automatically built using the AutoBuild ( 30 ) module of the PHENIX software package ( 31 ) and manually rebuilt in Coot ( 32 ).
- Full pipeline: stage not stated [ChimeraX, Coot, PHENIX, PyMOL]

### <i>Phytophthora sojae</i> effector Avr1d functions as an E2 competitor and inhibits ubiquitination activity of GmPUB13 to facilitate infection. (PNAS 2021)

- DOI: 10.1073/pnas.2018312118 | PMCID: PMC7958378 | PMID: 33658365
- Evidence: The PHENIX software suite was used for initial model building.
- Full pipeline: alignment/mapping [PyMOL] -> stage not stated [PHENIX]

### The effect of the D614G substitution on the structure of the spike glycoprotein of SARS-CoV-2. (PNAS 2021)

- DOI: 10.1073/pnas.2022586118 | PMCID: PMC7936381 | PMID: 33579792
- Evidence: The model was initially built by rigid body refinement in PHENIX ( 26 ), followed by adjustment in Coot.
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [Coot, PHENIX] -> stage not stated [UCSF Chimera]

### Molecular mechanisms of assembly and TRIP13-mediated remodeling of the human Shieldin complex. (PNAS 2021)

- DOI: 10.1073/pnas.2024512118 | PMCID: PMC7923543 | PMID: 33597306
- Evidence: Both structures were determined by molecular replacement in PHENIX.Phaser ( 48 , 49 ) using the modified REV7–REV3 complex structure (PDB code 3ABD) as the search model.
- Full pipeline: structure determination [RELION] -> visualisation [PyMOL] -> stage not stated [MotionCor2, PHENIX, UCSF Chimera]

### Cooperativity between the orthosteric and allosteric ligand binding sites of RORγt. (PNAS 2021)

- DOI: 10.1073/pnas.2021287118 | PMCID: PMC8017705 | PMID: 33536342
- Evidence: Final refinement was performed using phenix.refine from the Phenix software suite (version 1.16_3459) (stereo images are available in SI Appendix , Figs.
- Full pipeline: simulation/modelling [GROMACS v2019.3] -> structure determination [PHENIX, REFMAC] -> stage not stated [CCP4, PyMOL v2.2.3]

### Structure of the SARS-CoV-2 RNA-dependent RNA polymerase in the presence of favipiravir-RTP. (PNAS 2021)

- DOI: 10.1073/pnas.2021946118 | PMCID: PMC7896311 | PMID: 33526596
- Evidence: The atomic model was built based on a previously published atomic model of the nsp12–nsp7–nsp8 complex bound to RNA and remdesivir-RTP (Protein Data Bank [PDB] ID code 7BV2) ( 10 ), with manual model building in Coot ( 25 , 26 ), and real-space refinement in Phenix ( 27 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [RELION v3.1]

### Long-range structural defects by pathogenic mutations in most severe glucose-6-phosphate dehydrogenase deficiency. (PNAS 2021)

- DOI: 10.1073/pnas.2022790118 | PMCID: PMC7848525 | PMID: 33468660
- Evidence: Refinement and model building were performed using PHENIX and Coot ( 49 , 50 ).
- Full pipeline: alignment/mapping [RELION v3.0.6] -> simulation/modelling [GROMACS v2019.4] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX]

### DeepTracer for fast de novo cryo-EM protein structure modeling and special studies on CoV-related complexes. (PNAS 2021)

- DOI: 10.1073/pnas.2017525118 | PMCID: PMC7812826 | PMID: 33361332
- Evidence: Unfortunately, existing tools ( 11 – 15 ) such as Rosetta, MAINMAST (Mainchin model tracing from spanning tree), and Phenix determine only fragments of a protein complex, or require extensive manual processing steps.
- Full pipeline: stage not stated [PHENIX]

### Supramolecular assembly of the <i>Escherichia coli</i> LdcI upon acid stress. (PNAS 2021)

- DOI: 10.1073/pnas.2014383118 | PMCID: PMC7812809 | PMID: 33372137
- Evidence: Refinement was performed using the Phenix software package ( 68 ) and was identical for both 3D reconstructions.
- Full pipeline: registration [MotionCor2] -> dimensionality reduction/clustering [RELION v1.4] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, ImageJ]

### Cross-species recognition of SARS-CoV-2 to bat ACE2. (PNAS 2021)

- DOI: 10.1073/pnas.2020216118 | PMCID: PMC7817217 | PMID: 33335073
- Evidence: The atomic models were completed with Coot ( 41 ) and refined with phenix.refine in Phenix ( 40 ), and the stereochemical qualities of the final models were assessed with MolProbity ( 42 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX, RELION v3.1]

### Structure of SARS-CoV-2 ORF8, a rapidly evolving immune evasion protein. (PNAS 2021)

- DOI: 10.1073/pnas.2021785118 | PMCID: PMC7812859 | PMID: 33361333
- Evidence: Initial phases were obtained for the SeMet dataset using the Phenix autosol pipeline ( 23 ).
- Full pipeline: normalisation [CCP4] -> visualisation [PyMOL] -> stage not stated [PHENIX]

### Sparseness and Smoothness Regularized Imaging for improving the resolution of Cryo-EM single-particle reconstruction. (PNAS 2021)

- DOI: 10.1073/pnas.2013756118 | PMCID: PMC7812788 | PMID: 33402531
- Evidence: We then compared the postprocessed map with respect to the corresponding published atomic model(s) by calculating model versus map FSC using Phenix.Mtriage ( 32 ).
- Full pipeline: stage not stated [PHENIX, RELION]

### Orthosteric-allosteric dual inhibitors of PfHT1 as selective antimalarial agents. (PNAS 2021)

- DOI: 10.1073/pnas.2017749118 | PMCID: PMC7826358 | PMID: 33402433
- Evidence: The structural model was adjusted through COOT ( 34 ) and refined by PHENIX ( 35 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4, MACS2]

### Mechanistic insights into the synergistic activation of the RXR-PXR heterodimer by endocrine disruptor mixtures. (PNAS 2021)

- DOI: 10.1073/pnas.2020551118 | PMCID: PMC7817120 | PMID: 33361153
- Evidence: The structure was solved and refined using Phenix ( 13 ) and COOT ( 27 ).
- Full pipeline: quantification [ImageJ] -> structure determination [PHENIX] -> visualisation [PyMOL]

### Repurposed dihydroorotate dehydrogenase inhibitors with efficacy against drug-resistant <i>Acinetobacter baumannii</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2213116119 | PMCID: PMC9907071 | PMID: 36512492
- Evidence: The resulting model from Phaser was used as a starting model for the AutoBuild routine of Phenix ( 42 ).
- Full pipeline: stage not stated [PHENIX, PyMOL]

### Biophysical characterization of calcium-binding and modulatory-domain dynamics in a pentameric ligand-gated ion channel. (PNAS 2022)

- DOI: 10.1073/pnas.2210669119 | PMCID: PMC9897478 | PMID: 36480474
- Evidence: Postprocessed densities were improved using ResolveCryoEM, a part of the PHENIX package (release 1.18 and later) ( 46 ) based on maximum-likelihood density modification ( 47 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS, VMD] -> stage not stated [PHENIX, RELION v3.1, UCSF Chimera]

### FtsEX-independent control of RipA-mediated cell separation in <i>Corynebacteriales</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2214599119 | PMCID: PMC9897464 | PMID: 36469781
- Evidence: All structures were refined through iterative cycles of manual model building with COOT ( 59 ) and reciprocal space refinement with PHENIX ( 60 ) or BUSTER ( 61 ).
- Full pipeline: structure determination [IQ-TREE v2.0.6, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CCP4, ColabFold, HMMER]

### In situ structures of polymerase complex of mammalian reovirus illuminate RdRp activation and transcription regulation. (PNAS 2022)

- DOI: 10.1073/pnas.2203054119 | PMCID: PMC9897473 | PMID: 36469786
- Evidence: The models were then corrected and improved by iterative refinement using COOT ( 62 ) and Phenix ( 63 ).
- Full pipeline: alignment/mapping [CTFFIND] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [RELION]

### A structural mechanism of nuclear receptor biased agonism. (PNAS 2022)

- DOI: 10.1073/pnas.2215333119 | PMCID: PMC9897460 | PMID: 36469765
- Evidence: Data integration and scaling was performed in HKL3000, and structures were solved by molecular replacement using the PHASER package in PHENIX on the previously published PPARγ structure 5TTO as a search model.
- Full pipeline: normalisation [PHENIX]

### DHX15 is involved in SUGP1-mediated RNA missplicing by mutant SF3B1 in cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2216712119 | PMCID: PMC9894173 | PMID: 36459648
- Evidence: The structure refinement was carried out with Python-based Hierarchical ENvironment for Integrated Xtallography (PHENIX) ( 50 ) and manual model building with Coot (Crystallographic Object-Oriented Toolkit) ( 51 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [PyMOL]

### Mechanism of actin filament branch formation by Arp2/3 complex revealed by a high-resolution cryo-EM structureof the branch junction. (PNAS 2022)

- DOI: 10.1073/pnas.2206722119 | PMCID: PMC9894260 | PMID: 36442092
- Evidence: We refined the modeled structure using PHENIX ( 46 ) in real space.
- Full pipeline: registration [RELION v4.0] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> visualisation [ChimeraX] -> stage not stated [Coot, PyMOL]

### Human T cells recognize HLA-DP-bound peptides in two orientations. (PNAS 2022)

- DOI: 10.1073/pnas.2214331119 | PMCID: PMC9894132 | PMID: 36442096
- Evidence: Iterative rounds of model building in Coot and restrained refinement using REFMAC (CCP4 suite) ( 27 ) and PhenixRefine (PHENIX) ( 28 ) were carried out.
- Full pipeline: structure determination [Coot, PHENIX, REFMAC] -> machine learning [Coot, PHENIX, REFMAC] -> visualisation [PyMOL] -> stage not stated [CCP4]

### Insertions and deletions mediated functional divergence of Rossmann fold enzymes. (PNAS 2022)

- DOI: 10.1073/pnas.2207965119 | PMCID: PMC9860332 | PMID: 36417431
- Evidence: The missing residues were built manually using Coot ( 46 ) during the refinement rounds with Phenix ( 47 ).
- Full pipeline: simulation/modelling [GROMACS v2020.1] -> structure determination [PHENIX, PyMOL]

### Structure of the NuA4 histone acetyltransferase complex. (PNAS 2022)

- DOI: 10.1073/pnas.2214313119 | PMCID: PMC9860254 | PMID: 36417436
- Evidence: All the model buildings were performed using the cryo-EM module of Phenix package ( 33 ), Chimera ( 34 ), and COOT ( 35 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, PHENIX]

### Discovery of small molecules that target a tertiary-structured RNA. (PNAS 2022)

- DOI: 10.1073/pnas.2213117119 | PMCID: PMC9860313 | PMID: 36413497
- Evidence: Atomic coordinates of the previously reported NMR structure of the theophylline aptamer ( 19 ) (PDB ID 1O15) were used as a search model for molecular replacement using REFINE within the PHENIX package.
- Full pipeline: structure determination [Coot, PHENIX]

### Structures of NPAS4-ARNT and NPAS4-ARNT2 heterodimers reveal new dimerization modalities in the bHLH-PAS transcription factor family. (PNAS 2022)

- DOI: 10.1073/pnas.2208804119 | PMCID: PMC9674253 | PMID: 36343253
- Evidence: Further manual model building was facilitated using Coot ( 52 ), combined with structure refinement using Phenix ( 53 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Cryo-EM structures of cancer-specific helical and kinase domain mutations of PI3Kα. (PNAS 2022)

- DOI: 10.1073/pnas.2215621119 | PMCID: PMC9674216 | PMID: 36343266
- Version used: **1.18.2**
- Evidence: Density maps were optimized using DeepEMhancer (v1.19-2-4158) ( 59 ) and Coot (v0.9.4.1), and real space refinement coordinates were conducted using Phenix (v1.18.2-3874) ( 60 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX v1.18.2] -> visualisation [ChimeraX v1.0, PyMOL v2.1, UCSF Chimera v1.13.1] -> stage not stated [CTFFIND v1.06, RELION]

### Voltage-sensor movements in the Eag Kv channel under an applied electric field. (PNAS 2022)

- DOI: 10.1073/pnas.2214151119 | PMCID: PMC9674223 | PMID: 36331999
- Evidence: The model was edited and refined using the ISOLDE ( 54 ) plugin in ChimeraX, version 1.2.0 ( 55 ), or WinCoot, version 0.98.1 ( 56 ), followed by real-space refinement in Phenix ( 57 ).
- Full pipeline: alignment/mapping [RELION v3.1] -> structure determination [ChimeraX v1.2.0, PHENIX, PyMOL, RELION v3.1]

### Mechanism of 4-aminopyridine inhibition of the lysosomal channel TMEM175. (PNAS 2022)

- DOI: 10.1073/pnas.2208882119 | PMCID: PMC9636928 | PMID: 36279431
- Evidence: The final reconstruction was subjected to density modification using the two unfiltered half-maps with a soft mask in Phenix ( 32 ).
- Full pipeline: alignment/mapping [VMD] -> simulation/modelling [NAMD v2.12] -> structure determination [PHENIX] -> stage not stated [RELION v3.0]

### Structural basis for mouse receptor recognition by SARS-CoV-2 omicron variant. (PNAS 2022)

- DOI: 10.1073/pnas.2206509119 | PMCID: PMC9636943 | PMID: 36256797
- Evidence: PHENIX and CCP4 were used for molecular replacement and model refinement ( 43 , 44 ).
- Full pipeline: structure determination [CCP4, PHENIX] -> stage not stated [PyMOL]

### Structural and functional investigation of ABC transporter STE6-2p from <i>Pichia pastoris</i> reveals unexpected interaction with sterol molecules. (PNAS 2022)

- DOI: 10.1073/pnas.2202822119 | PMCID: PMC9618074 | PMID: 36256814
- Evidence: The model was manually refined in Coot ( 64 ) and real-space refined using Phenix ( 65 ), whereby refinement results were manually corrected if necessary.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [BLAST, CTFFIND, MotionCor2, RELION v3.1]

### Cryo-EM structures of light-harvesting 2 complexes from <i>Rhodopseudomonas palustris</i> reveal the molecular origin of absorption tuning. (PNAS 2022)

- DOI: 10.1073/pnas.2210109119 | PMCID: PMC9618040 | PMID: 36251992
- Evidence: This model was subjected to restrained global refinement using Phenix ( 61 ) real_space_refine, creating a final PucD-LH2 model.
- Full pipeline: registration [RELION] -> structure determination [PHENIX] -> machine learning [PHENIX] -> stage not stated [AlphaFold, BLAST]

### Structural basis for host recognition and superinfection exclusion by bacteriophage T5. (PNAS 2022)

- DOI: 10.1073/pnas.2211672119 | PMCID: PMC9586334 | PMID: 36215462
- Evidence: The FhuA crystal structure and the AF2 model of pb5 were rigid-body fit in the map via Phenix DockinMap ( 46 ), and the model was built via several cycles of manual building in Coot ( 47 ) and real-space refinement within Phenix.
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [GROMACS, VMD]

### Crystal structure and biochemical analysis suggest that YjoB ATPase is a putative substrate-specific molecular chaperone. (PNAS 2022)

- DOI: 10.1073/pnas.2207856119 | PMCID: PMC9565160 | PMID: 36191235
- Evidence: MAD phasing, molecular replacement phasing, model building, and structure refinement were performed using PHENIX.autosol ( 43 ), Phaser ( 44 ), Coot ( 45 ), and PHENIX.refine ( 46 ) programs, respectively.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL]

### Structural and inhibitor sensitivity analysis of influenza B-like viral neuraminidases derived from Asiatic toad and spiny eel. (PNAS 2022)

- DOI: 10.1073/pnas.2210724119 | PMCID: PMC9586306 | PMID: 36191180
- Evidence: Further rounds of refinement were performed using the phenix.refine program implemented in the Phenix package ( 54 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL]

### SPACA9 is a lumenal protein of human ciliary singlet and doublet microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2207605119 | PMCID: PMC9564825 | PMID: 36191189
- Evidence: Maps were sharpened using RELION postprocessing, Phenix.auto_sharpen ( 27 ), or DeepEMhancer ( 50 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX, Clustal Omega v1.2.2] -> stage not stated [AlphaFold, Coot v0.9.4.1, IMOD, PHENIX, PyMOL v2.3.4, RELION]

### CRY2 isoform selectivity of a circadian clock modulator with antiglioblastoma efficacy. (PNAS 2022)

- DOI: 10.1073/pnas.2203936119 | PMCID: PMC9546630 | PMID: 36161947
- Evidence: Final refinement was performed in PHENIX (Python-based Hierarchical ENvironment for Integrated Xtallography) ( 50 ).
- Full pipeline: normalisation [CCP4] -> simulation/modelling [GROMACS] -> structure determination [PHENIX]

### Nanomolar inhibition of SARS-CoV-2 infection by an unmodified peptide targeting the prehairpin intermediate of the spike protein. (PNAS 2022)

- DOI: 10.1073/pnas.2210990119 | PMCID: PMC9546559 | PMID: 36122200
- Evidence: The structure was then subjected to real space refinement (minimization_global, local_grid_search, adp) in PHENIX ( 39 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, CellProfiler, EMAN2, MotionCor2, RELION, kallisto]

### Structure of IMPORTIN-4 bound to the H3-H4-ASF1 histone-histone chaperone complex. (PNAS 2022)

- DOI: 10.1073/pnas.2207177119 | PMCID: PMC9499513 | PMID: 36103578
- Evidence: The final model was subjected to real-space refinement in Phenix ( 40 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [PyMOL]

### Tissue-restricted inhibition of mTOR using chemical genetics. (PNAS 2022)

- DOI: 10.1073/pnas.2204083119 | PMCID: PMC9499525 | PMID: 36095197
- Evidence: Molecular replacement was performed using Protein Data Bank 1FKB as a search model, and the model was refined and built using PHENIX ( 48 ) and Coot ( 49 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX]

### Multistate structures of the MLL1-WRAD complex bound to H2B-ubiquitinated nucleosome. (PNAS 2022)

- DOI: 10.1073/pnas.2205691119 | PMCID: PMC9499523 | PMID: 36095189
- Evidence: To correct any rotamer outliers that may occur from MDFF refinement, the model of the full complex underwent 1,000 iterations of minimization with secondary structure restraints using the Phenix geometry minimization module.
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, RELION v3.0, VMD v1.9.3, cryoDRGN]

### Mechanism by which T7 bacteriophage protein Gp1.2 inhibits &lt;i&gt;Escherichia coli&lt;/i&gt; dGTPase. (PNAS 2022)

- DOI: 10.1073/pnas.2123092119 | PMCID: PMC9478638 | PMID: 36067314
- Evidence: Postprocessed maps were generated from the final half-maps in RELION ( 39 ), autosharpened maps in PHENIX ( 42 ), and the DeepEMhancer postprocessing artificial neural network ( 43 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot] -> machine learning [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, RELION]

### Topological crossing in the misfolded <i>Tetrahymena</i> ribozyme resolved by cryo-EM. (PNAS 2022)

- DOI: 10.1073/pnas.2209146119 | PMCID: PMC9477386 | PMID: 36067294
- Evidence: The top-scoring DRRAFTER models were manually inspected and further optimized in Coot ( 17 ) and Phenix ( 18 ).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [Coot, EMAN2, MotionCor2, PHENIX, RELION, UCSF Chimera]

### Constitutive activation of a nuclear-localized calcium channel complex in &lt;i&gt;Medicago truncatula&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2205920119 | PMCID: PMC9407390 | PMID: 35972963
- Evidence: The data were processed with HKL-3000 ( 44 ), and the initial phase was determined by molecular replacement with Phenix ( 45 ), using the crystal structure of the LjCASTOR gating ring (Protein Data Bank ID code 6O6J) as a template.
- Full pipeline: structure determination [Coot] -> stage not stated [ImageJ, PHENIX]

### The neutralizing breadth of antibodies targeting diverse conserved epitopes between SARS-CoV and SARS-CoV-2. (PNAS 2022)

- DOI: 10.1073/pnas.2204256119 | PMCID: PMC9407403 | PMID: 35972965
- Evidence: Fluorescence images were captured by Opera Phenix (PerkinElmer) and quantitatively analyzed by the Columbus system (PerkinElmer).
- Full pipeline: registration [MotionCor2] -> dimensionality reduction/clustering [R v3.6.3] -> structure determination [Coot] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PHENIX]

### A flexible and highly sensitive organic electrochemical transistor-based biosensor for continuous and wireless nitric oxide detection. (PNAS 2022)

- DOI: 10.1073/pnas.2208060119 | PMCID: PMC9407321 | PMID: 35972962
- Evidence: The optical microscopy images are taken by an optical microscope (MC-D800U; Phenix Optics Co., Ltd.).
- Full pipeline: stage not stated [PHENIX]

### Structures of the mannose-6-phosphate pathway enzyme, GlcNAc-1-phosphotransferase. (PNAS 2022)

- DOI: 10.1073/pnas.2203518119 | PMCID: PMC9388126 | PMID: 35939698
- Evidence: The GNPTAB structure was solved by molecular replacement using Phaser ( 70 ) in Phenix ( 71 ), with a search model derived from an AlphaFold2 prediction ( 72 ).
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Coot, PHENIX, PyMOL]

### Structural basis of higher order oligomerization of KSHV inhibitor of cGAS. (PNAS 2022)

- DOI: 10.1073/pnas.2200285119 | PMCID: PMC9388135 | PMID: 35939686
- Evidence: The structure was determined by molecular replacement coupled with single-wavelength anomalous diffraction using Phenix ( 34 ).
- Full pipeline: structure determination [Coot] -> stage not stated [PHENIX]

### A multidomain connector links the outer membrane and cell wall in phylogenetically deep-branching bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2203156119 | PMCID: PMC9388160 | PMID: 35943982
- Evidence: The atomic model was subjected to several rounds of refinement using REFMAC5 ( 87 ) inside the CCP-EM software suite ( 88 ) and PHENIX ( 89 ), followed by manually rebuilding in Coot and interactive refinement using ISOLDE ( 90 ) inside UCSF ChimeraX.
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2] -> dimensionality reduction/clustering [MotionCor2] -> structure determination [ChimeraX, Coot, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold]

### PTX3 structure determination using a hybrid cryoelectron microscopy and AlphaFold approach offers insights into ligand binding and complement activation. (PNAS 2022)

- DOI: 10.1073/pnas.2208144119 | PMCID: PMC9388099 | PMID: 35939690
- Evidence: The monomer fit was automatically refined using Phenix real-space refine ( 47 ) before another monomer was placed into the opposing site ( SI Appendix , Fig.
- Full pipeline: structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [AlphaFold, ChimeraX, ColabFold v1.3, RELION v3.1]

### The structure and activities of the archaeal transcription termination factor Eta detail vulnerabilities of the transcription elongation complex. (PNAS 2022)

- DOI: 10.1073/pnas.2207581119 | PMCID: PMC9371683 | PMID: 35917344
- Evidence: With both isomorphous and anomalous signals from native and Ta 6 Br 12 datasets, 11 Ta 6 Br 12 sites in the asymmetric unit were located and the experimental phase (figure of merit: 0.480) was calculated using Automated structure solution (AutoSol) in PHENIX ( 65 ).
- Full pipeline: alignment/mapping [BLAST] -> structure determination [AlphaFold] -> stage not stated [PHENIX]

### Molecular mechanism for strengthening E-cadherin adhesion using a monoclonal antibody. (PNAS 2022)

- DOI: 10.1073/pnas.2204473119 | PMCID: PMC9371698 | PMID: 35921442
- Evidence: The model was refined with iterative rounds of refinement with Phenix ( 31 ) and manual model building in Coot ( 32 , 33 ).
- Full pipeline: dimensionality reduction/clustering [GROMACS v2020.1] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot, PHENIX]

### Mechanistic details of CRISPR-associated transposon recruitment and integration revealed by cryo-EM. (PNAS 2022)

- DOI: 10.1073/pnas.2202590119 | PMCID: PMC9371665 | PMID: 35914146
- Evidence: Protein and DNA geometry was subjected to Phenix real-space refinement ( 47 ).
- Full pipeline: alignment/mapping [RELION] -> dimensionality reduction/clustering [RELION] -> differential/statistical testing [RELION] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold, UCSF Chimera]

### Structural insight and characterization of human Twinkle helicase in mitochondrial disease. (PNAS 2022)

- DOI: 10.1073/pnas.2207459119 | PMCID: PMC9371709 | PMID: 35914129
- Evidence: Atomic models were built into the maps with Chimera ( 39 ), Coot ( 40 ), Phenix ( 41 ), and PyMOL ( 42 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, IMOD] -> stage not stated [PHENIX, PyMOL]

### Structural insights into a spindle-shaped archaeal virus with a sevenfold symmetrical tail. (PNAS 2022)

- DOI: 10.1073/pnas.2119439119 | PMCID: PMC9351363 | PMID: 35895681
- Evidence: The models of the capsid protein were built based on the cryo-EM density maps using the COOT software ( 33 ) and refined using real-space refinement as implemented in Phenix ( 34 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [RELION]

### C-terminal glutamine acts as a C-degron targeted by E3 ubiquitin ligase TRIM7. (PNAS 2022)

- DOI: 10.1073/pnas.2203218119 | PMCID: PMC9335266 | PMID: 35867826
- Evidence: The models were refined with PHENIX ( 50 ) and rebuilt with Coot ( 51 ).
- Full pipeline: quantification [ImageJ] -> structure determination [PHENIX]

### Divergent evolution of extreme production of variant plant monounsaturated fatty acids. (PNAS 2022)

- DOI: 10.1073/pnas.2201160119 | PMCID: PMC9335243 | PMID: 35867834
- Evidence: Model building and refinement were performed in COOT ( 53 ) and PHENIX.REFINE ( 54 , 55 ), respectively.
- Full pipeline: alignment/mapping [RAxML v8.2.4] -> normalisation [CCP4] -> structure determination [PHENIX] -> visualisation [PyMOL]

### Molecular mechanism of the severe MH/CCD mutation Y522S in skeletal ryanodine receptor (RyR1) by cryo-EM. (PNAS 2022)

- DOI: 10.1073/pnas.2122140119 | PMCID: PMC9335238 | PMID: 35867837
- Evidence: A single subunit of rabbit RyR1 R164C (PDB: 6WOT) ( 17 ) with the Cys164 mutated back to Arg was used as an initial model for real space refinement in Phenix ( 47 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [PyMOL]

### Structural insights into the human PA28-20S proteasome enabled by efficient tagging and purification of endogenous proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2207200119 | PMCID: PMC9388094 | PMID: 35858375
- Evidence: Atomic models were built into the cryo-EM density maps using Coot ( 38 , 39 ) and Phenix ( 40 , 41 ) with Torsion, Planar Peptide, Trans Peptide, and Ramachandran restraints turned on.
- Full pipeline: structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [MotionCor2]

### Structural basis for high-voltage activation and subtype-specific inhibition of human Na&lt;sub&gt;v&lt;/sub&gt;1.8. (PNAS 2022)

- DOI: 10.1073/pnas.2208211119 | PMCID: PMC9335304 | PMID: 35858452
- Evidence: Structural refinement was performed using the phenix.real_space_refine application in PHENIX ( 58 ) real space with secondary structure and geometry restraints.
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, Coot, MotionCor2]

### Structural basis of mammalian complex IV inhibition by steroids. (PNAS 2022)

- DOI: 10.1073/pnas.2205228119 | PMCID: PMC9335260 | PMID: 35858451
- Evidence: A validation report for the rigid body fit was produced with Phenix ( SI Appendix , Table S1 ).
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [PHENIX]

### Cryo-EM structures of wild-type and E138K/M184I mutant HIV-1 RT/DNA complexed with inhibitors doravirine and rilpivirine. (PNAS 2022)

- DOI: 10.1073/pnas.2203660119 | PMCID: PMC9335299 | PMID: 35858448
- Version used: **1.19**
- Evidence: Manual model fitting to the density map was carried out in Coot ( 53 ) followed by real-space model refinement using Phenix 1.19 ( 54 ).
- Full pipeline: alignment/mapping [CTFFIND, MotionCor2, RELION v3.1] -> structure determination [Coot, PHENIX v1.19] -> visualisation [PyMOL]

### Correlation between the binding affinity and the conformational entropy of nanobody SARS-CoV-2 spike protein complexes. (PNAS 2022)

- DOI: 10.1073/pnas.2205412119 | PMCID: PMC9351521 | PMID: 35858383
- Evidence: The final models were obtained by multiple rounds of jelly body refinement using RefMac5 via CCP-EM GUI ( 65 , 69 ) or Phenix real space refinement ( 70 ) and manual intervention with coot ( 71 ).
- Full pipeline: dimensionality reduction/clustering [RELION] -> simulation/modelling [GROMACS, PLUMED v2.6.0] -> structure determination [ChimeraX, PHENIX] -> stage not stated [CCP4]

### Structural basis and molecular mechanism of biased GPBAR signaling in regulating NSCLC cell growth via YAP activity. (PNAS 2022)

- DOI: 10.1073/pnas.2117054119 | PMCID: PMC9303995 | PMID: 35858343
- Evidence: This initial model was then subjected to iterative rounds of manual adjustment and automated refinement in Coot ( 58 ) and Phenix ( 57 ), respectively.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ANTs, CTFFIND]

### Structure of PLA2R reveals presentation of the dominant membranous nephropathy epitope and an immunogenic patch. (PNAS 2022)

- DOI: 10.1073/pnas.2202209119 | PMCID: PMC9303975 | PMID: 35858348
- Evidence: This structure was placed into the map using Phenix.dock_in_map ( 42 ).
- Full pipeline: stage not stated [Coot, PHENIX]

### Sequential rescue and repair of stalled and damaged ribosome by bacterial PrfH and RtcB. (PNAS 2022)

- DOI: 10.1073/pnas.2202464119 | PMCID: PMC9304027 | PMID: 35858322
- Evidence: The structures were refined in Phenix ( 59 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [Cytoscape, MotionCor2]

### Genetic and structural basis of the human anti-α-galactosyl antibody response. (PNAS 2022)

- DOI: 10.1073/pnas.2123212119 | PMCID: PMC9282431 | PMID: 35867757
- Evidence: Rigid body and restrained B-factor refinement were performed with a combination of REFMAC5 ( 65 ) and Phenix.Refine ( 66 ), interspersed with manual inspection and modification using Coot ( 67 ).
- Full pipeline: normalisation [CCP4] -> differential/statistical testing [limma] -> structure determination [PHENIX] -> machine learning [PHENIX]

### A broad and potent neutralization epitope in SARS-related coronaviruses. (PNAS 2022)

- DOI: 10.1073/pnas.2205784119 | PMCID: PMC9304036 | PMID: 35767670
- Evidence: Iterative model building and refinement were carried out in COOT ( 48 ) and PHENIX ( 49 ), respectively.
- Full pipeline: structure determination [PHENIX]

### Structural basis for heme detoxification by an ATP-binding cassette-type efflux pump in gram-positive pathogenic bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2123385119 | PMCID: PMC9271180 | PMID: 35767641
- Evidence: Structural analysis for the Mn•AMPPNP dataset was conducted using the single anomalous dispersion technique, and the other datasets were analyzed using the molecular replacement technique in Coot ( 51 ) and Phenix software package ( 52 ).
- Full pipeline: stage not stated [Coot, PHENIX]

### Structure of the human cation-chloride cotransport KCC1 in an outward-open state. (PNAS 2022)

- DOI: 10.1073/pnas.2109083119 | PMCID: PMC9271165 | PMID: 35759661
- Version used: **1.18**
- Evidence: The best pose was further refined in Phenix 1.18 ( 67 ).
- Full pipeline: alignment/mapping [MotionCor2] -> dimensionality reduction/clustering [RELION v3.0.7] -> structure determination [PHENIX v1.18] -> stage not stated [Coot v0.8.9.3]

### Metal cofactor stabilization by a partner protein is a widespread strategy employed for amidase activation. (PNAS 2022)

- DOI: 10.1073/pnas.2201141119 | PMCID: PMC9245657 | PMID: 35733252
- Evidence: Preliminary molecular replacement solutions using Phaser ( 56 ) through the Phenix Software Suite ( 57 ) with an amidase from C. difficile (PDB ID code 4RN7) as a search model demonstrated a trimer forming between three units of LytH, with interactions between helices spanning residues 179 to 185 and 242 to 247 on one subunit and a loop from residues 196 to 203 on the other.
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, PHENIX]

### Archaeal bundling pili of <i>Pyrobaculum calidifontis</i> reveal similarities between archaeal and bacterial biofilms. (PNAS 2022)

- DOI: 10.1073/pnas.2207037119 | PMCID: PMC9245690 | PMID: 35727984
- Evidence: The full-length sequence was threaded into the map using DeepTracer ( 78 ), manually adjusted in Coot ( 79 ), and real-space refined in PHENIX ( 80 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Structural basis of Tom20 and Tom22 cytosolic domains as the human TOM complex receptors. (PNAS 2022)

- DOI: 10.1073/pnas.2200158119 | PMCID: PMC9245660 | PMID: 35733257
- Evidence: The initial models of Tom22, Tom5, Tom6, and Tom7 were generated separately with PHENIX ( 64 ) (map to model function) for supplying segmented maps and sequences.
- Full pipeline: registration [MotionCor2] -> structure determination [UCSF Chimera] -> stage not stated [PHENIX, RELION]

### Structural basis for ultrapotent antibody-mediated neutralization of human metapneumovirus. (PNAS 2022)

- DOI: 10.1073/pnas.2203326119 | PMCID: PMC9231621 | PMID: 35696580
- Evidence: Models were built further and iteratively refined using a combination of Coot ( 56 ), PHENIX ( 57 ), and ISOLDE ( 58 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX]

### Reversible modification of mitochondrial ADP/ATP translocases by paired <i>Legionella</i> effector proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2122872119 | PMCID: PMC9191684 | PMID: 35653564
- Evidence: SAD phasing and automatic model building were performed using the AUTOSOL protocol in PHENIX ( 66 ).
- Full pipeline: stage not stated [ANTs, PHENIX, PyMOL]

### Atomic view of the HIV-1 matrix lattice; implications on virus assembly and envelope incorporation. (PNAS 2022)

- DOI: 10.1073/pnas.2200794119 | PMCID: PMC9191676 | PMID: 35658080
- Evidence: The structure was then iteratively refined with PHENIX ( 64 ) and with manual manipulation in Coot ( 65 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL]

### Potent monoclonal antibody-mediated neutralization of a divergent Hendra virus variant. (PNAS 2022)

- DOI: 10.1073/pnas.2122769119 | PMCID: PMC9295758 | PMID: 35617431
- Evidence: Phaser, Coot, and phenix.refine in the program suite PHENIX were used for structure determination, model building, and refinement ( 45 – 47 ).
- Full pipeline: structure determination [PHENIX]

### Visualization of mutagenic nucleotide processing by <i>Escherichia coli</i> MutT, a Nudix hydrolase. (PNAS 2022)

- DOI: 10.1073/pnas.2203118119 | PMCID: PMC9173781 | PMID: 35594391
- Evidence: The structure of MutT–8-oxo-dGTP was determined and refined using PHENIX ( 50 ) and COOT ( 51 ), with the coordinates of MutT–8-oxo-dGMP (PDB ID 3A6T) as a starting model ( 23 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Influenza chimeric hemagglutinin structures in complex with broadly protective antibodies to the stem and trimer interface. (PNAS 2022)

- DOI: 10.1073/pnas.2200821119 | PMCID: PMC9173763 | PMID: 35594401
- Evidence: Initial rigid-body refinement was performed in REFMAC5 ( 30 ), and subsequently rigid-body and group ADP refinement was carried out in Phenix ( 31 ).
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [PyMOL]

### Structural insights into galanin receptor signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2121465119 | PMCID: PMC9173784 | PMID: 35594396
- Evidence: All the models were manually built in COOT ( 72 ) and are subjected to real_space_refinement in Phenix ( 73 ) using the reference structure and secondary structure restraints.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, R v3.50]

### SHAPE-enabled fragment-based ligand discovery for RNA. (PNAS 2022)

- DOI: 10.1073/pnas.2122660119 | PMCID: PMC9171761 | PMID: 35561226
- Evidence: The structure was solved by molecular replacement using Phenix ( 53 ) and the 2GDI or 2HOJ riboswitch RNA structures ( 28 , 29 ).
- Full pipeline: stage not stated [PHENIX]

### Structural basis of peptidomimetic agonism revealed by small- molecule GLP-1R agonists Boc5 and WB4-24. (PNAS 2022)

- DOI: 10.1073/pnas.2200155119 | PMCID: PMC9171782 | PMID: 35561211
- Evidence: This starting model was then subjected to iterative rounds of manual adjustment and automated refinement in Coot ( 35 ) and Phenix ( 36 ), respectively.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v1.06]

### Structural insights of a highly potent pan-neutralizing SARS-CoV-2 human monoclonal antibody. (PNAS 2022)

- DOI: 10.1073/pnas.2120976119 | PMCID: PMC9171815 | PMID: 35549549
- Evidence: Images were acquired with an Opera Phenix high-content confocal microscope (PerkinElmer).
- Full pipeline: normalisation [RELION v3.1] -> stage not stated [PHENIX]

### Phenol-soluble modulins PSMα3 and PSMβ2 form nanotubes that are cross-α amyloids. (PNAS 2022)

- DOI: 10.1073/pnas.2121586119 | PMCID: PMC9171771 | PMID: 35533283
- Evidence: The models were refined in PHENIX ( 97 ), using real-space refinement.
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [EMAN2, RoseTTAFold, UCSF Chimera]

### Structural insights into Ras regulation by SIN1. (PNAS 2022)

- DOI: 10.1073/pnas.2119990119 | PMCID: PMC9171633 | PMID: 35522713
- Evidence: The structural models were built using Coot ( 66 ) and refined using PHENIX ( 67 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX]

### The cyclic octapeptide antibiotic argyrin B inhibits translation by trapping EF-G on the ribosome during translocation. (PNAS 2022)

- DOI: 10.1073/pnas.2114214119 | PMCID: PMC9171646 | PMID: 35500116
- Version used: **1.14**
- Evidence: Molecular models were fitted and adjusted by using Coot ( 59 ) and refined in Phenix 1.14 ( 60 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION v3.0] -> structure determination [PHENIX v1.14] -> stage not stated [ChimeraX, PyMOL, UCSF Chimera]

### Cryo-EM structures show the mechanistic basis of pan-peptidase inhibition by human α<sub>2</sub>-macroglobulin. (PNAS 2022)

- DOI: 10.1073/pnas.2200102119 | PMCID: PMC9181621 | PMID: 35500114
- Evidence: A first step of real-space refinement was performed with Phenix ( 61 ) applying global minimization, local grid search, and atomic displacement parameter refinement protocols.
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4, Coot, RELION v2.1]

### Studies on enmetazobactam clarify mechanisms of widely used β-lactamase inhibitors. (PNAS 2022)

- DOI: 10.1073/pnas.2117310119 | PMCID: PMC9170034 | PMID: 35486701
- Evidence: Alternating cycles of refinement using PHENIX ( 67 ) and model building using Coot ( 68 ) were performed until R work and R free converged.
- Full pipeline: structure determination [PHENIX]

### Dromedary camel nanobodies broadly neutralize SARS-CoV-2 variants. (PNAS 2022)

- DOI: 10.1073/pnas.2201433119 | PMCID: PMC9170159 | PMID: 35476528
- Version used: **1.19.2**
- Evidence: Final structure refinement was performed using Phenix (1.19.2_4158) ( 50 ) followed by manual correction using Chimera.
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS] -> structure determination [PHENIX v1.19.2] -> stage not stated [Pangolin]

### Agonists of prostaglandin E<sub>2</sub> receptors as potential first in class treatment for nephronophthisis and related ciliopathies. (PNAS 2022)

- DOI: 10.1073/pnas.2115960119 | PMCID: PMC9170064 | PMID: 35482924
- Evidence: For ciliogenesis assays, images were acquired using the Opera Phenix (40×, Perkin-Elmer).
- Full pipeline: alignment/mapping [R, featureCounts] -> quantification [ImageJ] -> stage not stated [Metascape, PHENIX]

### A saturation mutagenesis screen uncovers resistant and sensitizing secondary <i>KRAS</i> mutations to clinical KRAS<sup>G12C</sup> inhibitors. (PNAS 2022)

- DOI: 10.1073/pnas.2120512119 | PMCID: PMC9170150 | PMID: 35471904
- Evidence: Images were acquired on the Opera Phenix Plus High-Content Screening System (PerkinElmer) using the 40× water immersion (numerical aperture = 1.1) objective and the confocal mode for better resolution.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [Bioconductor, PHENIX]

### Structural basis for replicase polyprotein cleavage and substrate specificity of main protease from SARS-CoV-2. (PNAS 2022)

- DOI: 10.1073/pnas.2117142119 | PMCID: PMC9172370 | PMID: 35380892
- Version used: **1.17.1**
- Evidence: The apo structure was determined by molecular replacement (MR) with PHASER ( 37 ), a program inside the Phenix 1.17.1 package ( 38 ).
- Full pipeline: stage not stated [PHENIX v1.17.1]

### Helical self-assembly of a mucin segment suggests an evolutionary origin for von Willebrand factor tubules. (PNAS 2022)

- DOI: 10.1073/pnas.2116790119 | PMCID: PMC9169620 | PMID: 35377815
- Evidence: A hybrid structure constructed from elements of these two docked models was rebuilt and refined by iterative cycles of Phenix ( 57 ) real-space refinement and interactive rebuilding in Coot.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX]

### Cryoelectron microscopy of Na<sup>+</sup>,K<sup>+</sup>-ATPase in the two E2P states with and without cardiotonic steroids. (PNAS 2022)

- DOI: 10.1073/pnas.2123226119 | PMCID: PMC9169807 | PMID: 35380894
- Evidence: The atomic model for NKA in E2P Pi ·Mg 2+ (OBN) was built first on Coot ( 32 ) starting from its crystal structure (PDB ID: 7WYT) and was refined using Phenix ( 33 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [RELION v3.1]

### Cryo-EM structures of staphylococcal IsdB bound to human hemoglobin reveal the process of heme extraction. (PNAS 2022)

- DOI: 10.1073/pnas.2116708119 | PMCID: PMC9168843 | PMID: 35357971
- Evidence: The maps were modified for interpretation using the auto_sharpen tools of the Phenix package ( 50 ).
- Full pipeline: stage not stated [Coot, PHENIX, PyMOL, RELION, UCSF Chimera]

### Structural conservation among variants of the SARS-CoV-2 spike postfusion bundle. (PNAS 2022)

- DOI: 10.1073/pnas.2119467119 | PMCID: PMC9169775 | PMID: 35363556
- Evidence: The PDB ID code 6lxt was used as the template for real-space refinement (minimization_global, local_grid_search, adp) in PHENIX ( 46 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [CTFFIND, ChimeraX, Coot, PyMOL, Python, RELION, UCSF Chimera]

### Structural insights into the activation of autoinhibited human lipid flippase ATP8B1 upon substrate binding. (PNAS 2022)

- DOI: 10.1073/pnas.2118656119 | PMCID: PMC9168909 | PMID: 35349344
- Evidence: After several rounds of manual building, the model was almost completely built and automatically refined against the map by the real_space_refine program in PHENIX ( 50 ) with secondary structure and geometry restraints.
- Full pipeline: structure determination [PHENIX] -> stage not stated [Coot, MotionCor2, RELION, UCSF Chimera]

### 50S subunit recognition and modification by the &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; ribosomal RNA methyltransferase TlyA. (PNAS 2022)

- DOI: 10.1073/pnas.2120352119 | PMCID: PMC9168844 | PMID: 35357969
- Version used: **1.19.2**
- Evidence: The 50S subunit model was created by docking an existing Msm 50S subunit structure (PDB ID code 5O60), after de novo modeling of the NM6-modified C2144, into the 50S-TlyA map and using Coot (v0.9-pre EL, ccpem) ( 27 ) and Phenix (v1.19.2-4158-000) ( 55 , 56 ).
- Full pipeline: alignment/mapping [Clustal Omega, RELION] -> stage not stated [CTFFIND, Coot, PHENIX v1.19.2]

### Clamping of DNA shuts the condensin neck gate. (PNAS 2022)

- DOI: 10.1073/pnas.2120006119 | PMCID: PMC9168836 | PMID: 35349345
- Evidence: For Form II of the head module from the tetramer dataset the refined model of Form I was docked into the 3.05-Å map and rigid-body-refined in PHENIX, followed by manual adjustments in Coot.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, PyMOL v2.5, RELION v3.1, UCSF Chimera]

### Structural determinants of dual incretin receptor agonism by tirzepatide. (PNAS 2022)

- DOI: 10.1073/pnas.2116506119 | PMCID: PMC9060465 | PMID: 35333651
- Evidence: The starting model was then subjected to iterative rounds of manual and real space refinement in Coot ( 49 , 50 ) and Phenix ( 51 ), respectively.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND]

### A mixed-valent Fe(II)Fe(III) species converts cysteine to an oxazolone/thioamide pair in methanobactin biosynthesis. (PNAS 2022)

- DOI: 10.1073/pnas.2123566119 | PMCID: PMC9060507 | PMID: 35320042
- Evidence: All additional structures were solved by molecular replacement using Phenix ( 37 ).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold, ColabFold, PHENIX]

### An extended conformation of SARS-CoV-2 main protease reveals allosteric targets. (PNAS 2022)

- DOI: 10.1073/pnas.2120913119 | PMCID: PMC9169858 | PMID: 35324337
- Evidence: The structure determination of the complex of the M pro and NB2B4 or NB1A2 was solved with the molecular replacement using Phaser in the PHENIX package ( 33 ), and the model (PDB ID code 7LMC) of SARS-CoV-2 M pro was used.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL]

### Replication is the key barrier during the dual-host adaptation of mosquito-borne flaviviruses. (PNAS 2022)

- DOI: 10.1073/pnas.2110491119 | PMCID: PMC8944775 | PMID: 35294288
- Evidence: This model was further refined by positional and B-factor refinement in real space with Phenix ( 58 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [MotionCor2]

### Mechanistic insights into the subversion of the linear ubiquitin chain assembly complex by the E3 ligase IpaH1.4 of <i>Shigella flexneri</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116776119 | PMCID: PMC8944867 | PMID: 35294289
- Evidence: All structure models were manually adjusted in Coot ( 57 ) and refined with Phenix suite ( 58 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [PyMOL]

### Interleukin-2 superkines by computational design. (PNAS 2022)

- DOI: 10.1073/pnas.2117401119 | PMCID: PMC8944926 | PMID: 35294290
- Evidence: The structure was initially rebuilt using phenix.autobuild ( 40 ) with subsequent cycles of interactive rebuilding in coot ( 41 ) and reciprocal space refinement in Phenix ( 42 , 43 ).
- Full pipeline: structure determination [PHENIX]

### Crystal structures of YeiE from <i>Cronobacter sakazakii</i> and the role of sulfite tolerance in gram-negative bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2118002119 | PMCID: PMC8931317 | PMID: 35271389
- Evidence: The final structures of CsYeiE RD were refined using the PHENIX software suite ( 49 ) ( SI Appendix , Table S1 ).
- Full pipeline: quantification [ImageJ v1.53e] -> normalisation [ImageJ v1.53e] -> structure determination [PHENIX] -> stage not stated [CCP4]

### Accurate positioning of functional residues with robotics-inspired computational protein design. (PNAS 2022)

- DOI: 10.1073/pnas.2115480119 | PMCID: PMC8931229 | PMID: 35254891
- Evidence: We obtained initial phase information for calculation of electron density maps by molecular replacement using the program Phaser ( 47 ), as implemented in the PHENIX suite ( 48 ).
- Full pipeline: structure determination [PHENIX]

### FliL ring enhances the function of periplasmic flagella. (PNAS 2022)

- DOI: 10.1073/pnas.2117245119 | PMCID: PMC8931381 | PMID: 35254893
- Evidence: The models for MotA, MotB, and the FliL ring were placed into segmented WT and Δ motB focus-refined cryo-ET maps and fitted using the ChimeraX “fit to map” function ( 78 ) and refined with the PHENIX real-space refinement ( 79 ).
- Full pipeline: alignment/mapping [CTFFIND, IMOD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold]

### Structural basis for the oligomerization-mediated regulation of NLRP3 inflammasome activation. (PNAS 2022)

- DOI: 10.1073/pnas.2121353119 | PMCID: PMC8931350 | PMID: 35254907
- Evidence: The atomic models of human NLRP3ΔP hexamer and mouse NLRP3 dodecamer were subjected to iterative cycles of manual model adjustment using the COOT program ( 56 ) and real-space refinement in the Phenix program ( 57 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, MotionCor2, PyMOL, RELION v3.1]

### Molecular basis of multistep voltage activation in plant two-pore channel 1. (PNAS 2022)

- DOI: 10.1073/pnas.2110936119 | PMCID: PMC8892357 | PMID: 35210362
- Evidence: Unfiltered, unmasked half maps from the refinement were subjected to both Deepemhancer ( 45 ) and density modification in Phenix (phenix.resolve_cryo_em) ( 46 ) for assistance with model building and atomic interpretation.
- Full pipeline: structure determination [Coot, PHENIX, RELION] -> visualisation [UCSF Chimera] -> stage not stated [MotionCor2]

### Structure and dynamics of SARS-CoV-2 proofreading exoribonuclease ExoN. (PNAS 2022)

- DOI: 10.1073/pnas.2106379119 | PMCID: PMC8892293 | PMID: 35165203
- Evidence: Iterative model building and refinement were performed using COOT ( 42 ) and PHENIX ( 43 ), respectively.
- Full pipeline: simulation/modelling [MDTraj] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Structures of the junctophilin/voltage-gated calcium channel interface reveal hot spot for cardiomyopathy mutations. (PNAS 2022)

- DOI: 10.1073/pnas.2120416119 | PMCID: PMC8916002 | PMID: 35238659
- Evidence: All models were completed with iterative cycles of manual model building in Coot ( 57 ) and refinement with Refmac5 in ccp4 ( 58 ) and Phenix ( 59 ).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [ImageJ, PyMOL] -> structure determination [Coot, PHENIX]

### Conformational alterations in unidirectional ion transport of a light-driven chloride pump revealed using X-ray free electron lasers. (PNAS 2022)

- DOI: 10.1073/pnas.2117433119 | PMCID: PMC8892520 | PMID: 35197289
- Evidence: The structure was solved by molecular replacement with Protein Data Bank (PDB) entry 5B2N ( 20 ), and difference Fourier maps were calculated by the CCP4 and PHENIX suites ( 53 , 54 ).
- Full pipeline: stage not stated [CCP4, PHENIX]

### Bivalent recognition of fatty acyl-CoA by a human integral membrane palmitoyltransferase. (PNAS 2022)

- DOI: 10.1073/pnas.2022050119 | PMCID: PMC8851515 | PMID: 35140179
- Evidence: The final model was obtained after iterative cycles of manual model building with COOT and refinement using PHENIX.
- Full pipeline: simulation/modelling [NAMD v2.13] -> structure determination [PHENIX]

### A distinct RNA recognition mechanism governs Np<sub>4</sub> decapping by RppH. (PNAS 2022)

- DOI: 10.1073/pnas.2117318119 | PMCID: PMC8833179 | PMID: 35131855
- Evidence: The crystal structure was solved by molecular replacement using the structure of E. coli RppH (Protein Data Bank [PDB] code 4S2W) as a search model and the Phaser-MR implementation in PHENIX ( 50 ).
- Full pipeline: quantification [ImageJ] -> visualisation [ImageJ] -> stage not stated [PHENIX]

### Rearrangement of a unique Kv1.3 selectivity filter conformation upon binding of a drug. (PNAS 2022)

- DOI: 10.1073/pnas.2113536119 | PMCID: PMC8812516 | PMID: 35091471
- Evidence: For the four NADP + cofactors that bind Kvβ2, restraints were generated using the eLBOW ( 41 ) tool from the PHENIX software package and used during refinement.
- Full pipeline: alignment/mapping [MotionCor2] -> registration [MotionCor2] -> simulation/modelling [UCSF Chimera, VMD] -> structure determination [PHENIX] -> stage not stated [CTFFIND, NAMD, RELION]

### Annealing synchronizes the 70<i>S</i> ribosome into a minimum-energy conformation. (PNAS 2022)

- DOI: 10.1073/pnas.2111231119 | PMCID: PMC8872765 | PMID: 35177473
- Version used: **1.17.1**
- Evidence: The atomic model was further optimized for improved local density fitting with Coot 0.8.9.1 ( 62 ) and real-space refinement with PHENIX 1.17.1 ( 63 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.17.1, RELION v3.0.8] -> stage not stated [CTFFIND, Python, UCSF Chimera v1.16]

### Structure of the Mon1-Ccz1 complex reveals molecular basis of membrane binding for Rab7 activation. (PNAS 2022)

- DOI: 10.1073/pnas.2121494119 | PMCID: PMC8833172 | PMID: 35105815
- Evidence: To facilitate map interpretation, we used maps for model building, which were sharpened by local anisotropic sharpening in Phenix ( 38 ) and by a deep-learning–based approach by DeepEMhancer ( 39 ) with the implemented highRes training model.
- Full pipeline: machine learning [PHENIX] -> stage not stated [Coot, RELION]

### Structures of the peptidase-containing ABC transporter PCAT1 under equilibrium and nonequilibrium conditions. (PNAS 2022)

- DOI: 10.1073/pnas.2120534119 | PMCID: PMC8794836 | PMID: 35074919
- Evidence: Two independent half maps and a polyalanine model without nucleotide ligands were used as inputs for the density modification procedure implemented in Phenix.
- Full pipeline: alignment/mapping [CTFFIND] -> dimensionality reduction/clustering [RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [Coot, PHENIX]

### The flagellar motor protein FliL forms a scaffold of circumferentially positioned rings required for stator activation. (PNAS 2022)

- DOI: 10.1073/pnas.2118401119 | PMCID: PMC8794807 | PMID: 35046042
- Evidence: Refinement and automated placement of ordered water molecules was performed using PHENIX ( 56 ) and REFMAC ( 57 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [PHENIX, REFMAC] -> stage not stated [ChimeraX, PyMOL]

### High-resolution cryo-electron microscopy structure of photosystem II from the mesophilic cyanobacterium, <i>Synechocystis</i> sp. PCC 6803. (PNAS 2022)

- DOI: 10.1073/pnas.2116765118 | PMCID: PMC8740770 | PMID: 34937700
- Evidence: Manual fitting and editing were performed in Coot ( 81 ), and automated refinement was performed using real_space_refine ( 82 ) in Phenix ( 83 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [RELION v3.1, UCSF Chimera]

### Molecular basis of differential receptor usage for naturally occurring CD55-binding and -nonbinding coxsackievirus B3 strains. (PNAS 2022)

- DOI: 10.1073/pnas.2118590119 | PMCID: PMC8794823 | PMID: 35046043
- Evidence: The models were further improved by real space refinement using Phenix ( 43 ).
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [PHENIX] -> stage not stated [Coot, MotionCor2, PyMOL]

### SNX27 suppresses SARS-CoV-2 infection by inhibiting viral lysosome/late endosome entry. (PNAS 2022)

- DOI: 10.1073/pnas.2117576119 | PMCID: PMC8794821 | PMID: 35022217
- Evidence: The ACE2-PBM peptide was manually built into the map using the program Coot ( 61 ), and the structure was refined using phenix.refine in Phenix ( 62 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ImageJ]

### Oxidative desulfurization pathway for complete catabolism of sulfoquinovose by bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2116022119 | PMCID: PMC8795539 | PMID: 35074914
- Evidence: Structures were built and refined by iterative cycles using Coot ( 46 ) and REFMAC ( 47 ) or Phenix ( 48 ), the latter employing local noncrystallographic symmetry restraints.
- Full pipeline: dimensionality reduction/clustering [BLAST] -> structure determination [PHENIX, REFMAC]

### Structural transitions in the GTP cap visualized by cryo-electron microscopy of catalytically inactive microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2114994119 | PMCID: PMC8764682 | PMID: 34996871
- Evidence: Each tubulin subunit was rigid-body docked with PHENIX and refined using the real-space refinement program within PHENIX ( 41 , 42 ).
- Full pipeline: alignment/mapping [MotionCor2 v2.1] -> normalisation [PyMOL] -> structure determination [PHENIX] -> stage not stated [RELION]

### Atomic structure of Lanreotide nanotubes revealed by cryo-EM. (PNAS 2022)

- DOI: 10.1073/pnas.2120346119 | PMCID: PMC8794822 | PMID: 35042822
- Evidence: Model building and refinement were performed with Coot ( 22 ) and PHENIX real-space refinement ( 25 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold]

### Defining a de novo non-RBM antibody as RBD-8 and its synergistic rescue of immune-evaded antibodies to neutralize Omicron SARS-CoV-2. (PNAS 2023)

- DOI: 10.1073/pnas.2314193120 | PMCID: PMC10756187 | PMID: 38109549
- Evidence: The atomic models were completed with Coot ( 41 ) and refined with phenix.refine in Phenix ( 42 ), and the stereochemical qualities of the final models were assessed with MolProbity ( 43 ).
- Full pipeline: structure determination [PHENIX]

### Structures of the &lt;i&gt;P. aeruginosa&lt;/i&gt; FleQ-FleN master regulators reveal large-scale conformational switching in motility and biofilm control. (PNAS 2023)

- DOI: 10.1073/pnas.2312276120 | PMCID: PMC10723142 | PMID: 38051770
- Evidence: The resultant map was sharpened using the integrated Deep EMhancer tool ( 42 ) and used for rigid body fitting of structures of individual FleQ and FleN domains in Chimera, followed by model building and regularization in Coot ( 43 ) and refinements in Phenix ( 44 ) and Namdinator ( 45 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, MotionCor2]

### Structure of the <i>Lysinibacillus sphaericus</i> Tpp49Aa1 pesticidal protein elucidated from natural crystals using MHz-SFX. (PNAS 2023)

- DOI: 10.1073/pnas.2203241120 | PMCID: PMC10710082 | PMID: 38015839
- Evidence: The phasing pipeline MRage in Phenix ( 73 , 74 ) was used for initial phasing, using the sequence information and a component stoichiometry of two as input.
- Full pipeline: stage not stated [PHENIX]

### Tad and toxin-coregulated pilus structures reveal unexpected diversity in bacterial type IV pili. (PNAS 2023)

- DOI: 10.1073/pnas.2316668120 | PMCID: PMC10710030 | PMID: 38011558
- Evidence: The models underwent iterative cycles of model building in COOT ( 51 ) and automatic refinement by Phenix Real Space Refinement ( 52 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### The mechanism of &lt;i&gt;Gα&lt;sub&gt;q&lt;/sub&gt;&lt;/i&gt; regulation of &lt;i&gt;PLCβ3&lt;/i&gt;-catalyzed &lt;i&gt;PIP2&lt;/i&gt; hydrolysis. (PNAS 2023)

- DOI: 10.1073/pnas.2315011120 | PMCID: PMC10691244 | PMID: 37991948
- Evidence: Atomic models from previously determined structures were fit into our density maps, refined using PHENIX real-space refine ( 36 ), and manually adjusted.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX]

### A Novel mechanism of herbicide action through disruption of pyrimidine biosynthesis. (PNAS 2023)

- DOI: 10.1073/pnas.2313197120 | PMCID: PMC10691210 | PMID: 37988466
- Evidence: The structure of rat DHODH (PDB: 1UUM) provided a molecular replacement model for PHENIX.
- Full pipeline: alignment/mapping [AlphaFold, SAMtools] -> stage not stated [PHENIX]

### Tunable force transduction through the &lt;i&gt;Escherichia coli&lt;/i&gt; cell envelope. (PNAS 2023)

- DOI: 10.1073/pnas.2306707120 | PMCID: PMC10666116 | PMID: 37972066
- Evidence: Due to the resolution of the map, only rigid body refinement was run in Phenix ( 75 ).
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [PHENIX]

### Structure and function of the &lt;i&gt;S. pombe&lt;/i&gt; III-IV-cyt &lt;i&gt;c&lt;/i&gt; supercomplex. (PNAS 2023)

- DOI: 10.1073/pnas.2307697120 | PMCID: PMC10655221 | PMID: 37939086
- Evidence: The final refinement and calculation of atomic displacement parameters were done with real space refine in Phenix ( 90 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Molecular basis for Nse5-6 mediated regulation of Smc5/6 functions. (PNAS 2023)

- DOI: 10.1073/pnas.2310924120 | PMCID: PMC10636319 | PMID: 37903273
- Evidence: The structures of the S. cerevisiae Smc5/6 5-mer and 8-mer complexes were refined by real-space refinement in PHENIX ( 27 ) and manually real space refined against the cryo-EM density map in COOT ( 28 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [ColabFold, RELION v3.0]

### FAM91A1-TBC1D23 complex structure reveals human genetic variations susceptible for PCH. (PNAS 2023)

- DOI: 10.1073/pnas.2309910120 | PMCID: PMC10636324 | PMID: 37903274
- Evidence: Model building and crystallographic refinement were conducted with COOT and PHENIX software ( 53 , 54 ), respectively.
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [ImageJ]

### Red fluorescent proteins engineered from green fluorescent proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2307687120 | PMCID: PMC10636333 | PMID: 37871160
- Evidence: The initial phase was calculated by the molecular replacement method with the Phaser-MR in Phenix ( 47 ) program using the structure of AG (PDB ID: 6CIU) as a search model.
- Full pipeline: stage not stated [MAFFT, PHENIX]

### Identification of a carbonic anhydrase-Rubisco complex within the alpha-carboxysome. (PNAS 2023)

- DOI: 10.1073/pnas.2308600120 | PMCID: PMC10614612 | PMID: 37862384
- Evidence: The coordinate models for the two H. neapolitanus Rubisco–NTD 1-50 complex maps were built and refined similarly using a combination of COOT-v0.9.1 ( 63 ) and PHENIX-v1.19.1-4122 ( 64 ).
- Full pipeline: alignment/mapping [MUSCLE, RELION v3.1] -> quantification [ImageJ] -> registration [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, IQ-TREE, PyMOL] -> stage not stated [CTFFIND v4.1]

### GAS41 promotes H2A.Z deposition through recognition of the N terminus of histone H3 by the YEATS domain. (PNAS 2023)

- DOI: 10.1073/pnas.2304103120 | PMCID: PMC10614846 | PMID: 37844223
- Evidence: Model building was accomplished with Coot ( 65 ), and structural refinement was performed with REFMAC ( 66 ) and PHENIX ( 67 ).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [R v4.1] -> structure determination [PHENIX, REFMAC] -> visualisation [PyMOL v2.5]

### Molecular basis for C-degron recognition by CRL2&lt;sup&gt;APPBP2&lt;/sup&gt; ubiquitin ligase. (PNAS 2023)

- DOI: 10.1073/pnas.2308870120 | PMCID: PMC10614623 | PMID: 37844242
- Evidence: The models were analyzed by MolProbity in Phenix ( 40 ) to show the quality.
- Full pipeline: structure determination [Coot] -> stage not stated [AlphaFold, ChimeraX, PHENIX, PyMOL]

### Phage display uncovers a sequence motif that drives polypeptide binding to a conserved regulatory exosite of O-GlcNAc transferase. (PNAS 2023)

- DOI: 10.1073/pnas.2303690120 | PMCID: PMC10589721 | PMID: 37819980
- Evidence: Simulated annealing was run on the structure solution through Phenix before cycles of refinement and interactive model building were undertaken using REFMAC5 and Coot ( 61 – 64 ).
- Full pipeline: simulation/modelling [PHENIX] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Identification, structural, and biophysical characterization of a positive modulator of human Kv3.1 channels. (PNAS 2023)

- DOI: 10.1073/pnas.2220029120 | PMCID: PMC10589703 | PMID: 37812700
- Evidence: The coordinates and restraints for compound-4 were generated using Grade (Global Phasing Ltd.), and the ligand was manually fitted into the density using real-space refinement in Coot ( 44 ) and further refined using Phenix ( 46 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [PyMOL]

### Structure-based design of nanobodies that inhibit seeding of Alzheimer's patient-extracted tau fibrils. (PNAS 2023)

- DOI: 10.1073/pnas.2300258120 | PMCID: PMC10576031 | PMID: 37801475
- Evidence: Refinement and structure building was performed in PHENIX ( 62 ) and Coot ( 63 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ImageJ]

### Molecular basis of signal transduction mediated by the human GIPR splice variants. (PNAS 2023)

- DOI: 10.1073/pnas.2306145120 | PMCID: PMC10576055 | PMID: 37792509
- Evidence: Real space refinement was performed using Phenix ( 65 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2021.4] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX v1.2.4] -> stage not stated [CTFFIND v1.06, ImageJ, RELION]

### Dual-pocket inhibition of Na<sub>v</sub> channels by the antiepileptic drug lamotrigine. (PNAS 2023)

- DOI: 10.1073/pnas.2309773120 | PMCID: PMC10576118 | PMID: 37782796
- Evidence: Subsequently, refinement against the relevant map was conducted using PHENIX's Real-space Refinement tool ( 38 ).
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX]

### Multiomic prediction of therapeutic targets for human diseases associated with protein phase separation. (PNAS 2023)

- DOI: 10.1073/pnas.2300215120 | PMCID: PMC10556643 | PMID: 37774095
- Evidence: Plates were imaged using the Opera Phenix High-Content Confocal microscope at a magnification of 40X to examine the distribution and morphology of potential protein condensates.
- Full pipeline: differential/statistical testing [STRING db] -> stage not stated [PHENIX]

### Bacterial SEAL domains undergo autoproteolysis and function in regulated intramembrane proteolysis. (PNAS 2023)

- DOI: 10.1073/pnas.2310862120 | PMCID: PMC10556640 | PMID: 37756332
- Version used: **1.20.1**
- Evidence: An AlphaFold2 model of RsgI GGG was used for molecular replacement to determine phase information and an initial map was determined using the Phaser program in Phenix v1.20.1 ( 56 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot] -> stage not stated [AlphaFold, ColabFold, PHENIX v1.20.1]

### Structure of the <i>bc</i><sub>1</sub>-<i>cbb</i><sub>3</sub> respiratory supercomplex from <i>Pseudomonas aeruginosa</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2307093120 | PMCID: PMC10556555 | PMID: 37751552
- Version used: **1.20.1**
- Evidence: These models were then rigid body fit into the composite map and optimized with Coot v0.9 ( 69 ), ISOLDE v1.4 ( 70 ), and PHENIX v1.20.1-4487 ( 71 ).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold, PHENIX v1.20.1, UCSF Chimera]

### Combined prediction and design reveals the target recognition mechanism of an intrinsically disordered protein interaction domain. (PNAS 2023)

- DOI: 10.1073/pnas.2305603120 | PMCID: PMC10523638 | PMID: 37722056
- Evidence: Automatic protein model building was performed with the Autobuild module in PHENIX ( 48 ).
- Full pipeline: simulation/modelling [AlphaFold, GROMACS] -> stage not stated [PHENIX]

### Crystal structure and activity of a de novo enzyme, ferric enterobactin esterase Syn-F4. (PNAS 2023)

- DOI: 10.1073/pnas.2218281120 | PMCID: PMC10515146 | PMID: 37695900
- Evidence: The program AutoSol in Phenix was used to locate the heavy atom sites and to calculate the phases by the MAD method, and the program was used for the density modification and partial model building ( 30 , 31 ).
- Full pipeline: structure determination [CCP4] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [PHENIX]

### Cryo-EM structure determination of small therapeutic protein targets at 3 Å-resolution using a rigid imaging scaffold. (PNAS 2023)

- DOI: 10.1073/pnas.2305494120 | PMCID: PMC10500258 | PMID: 37669364
- Evidence: Manual adjustments to the models were performed using Coot ( 49 ), and automated refinement was performed using Phenix ( 50 ).
- Full pipeline: structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### Molecular recognition of trehalose and trehalose analogues by <i>Mycobacterium tuberculosis</i> LpqY-SugABC. (PNAS 2023)

- DOI: 10.1073/pnas.2307625120 | PMCID: PMC10466184 | PMID: 37603751
- Evidence: Several iterations of real-space refinement were performed in PHENIX ( 38 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [UCSF Chimera]

### Specific inhibition of an anticancer target, polo-like kinase 1, by allosterically dismantling its mechanism of substrate recognition. (PNAS 2023)

- DOI: 10.1073/pnas.2305037120 | PMCID: PMC10629583 | PMID: 37603740
- Evidence: Structure refinement (1.65 Å resolution) was carried out with phenix.refine in the Phenix suite ( 67 ) and manual fitting in Coot ( 68 ).
- Full pipeline: normalisation [CCP4] -> simulation/modelling [GROMACS v2022.3, RDKit, VMD v1.9.4] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL, VMD v1.9.4] -> stage not stated [AlphaFold]

### Structural insights into the interaction of three Y-shaped ligands with PI3Kα. (PNAS 2023)

- DOI: 10.1073/pnas.2304071120 | PMCID: PMC10450665 | PMID: 37585458
- Version used: **1.18.2**
- Evidence: Ligand coordinates and geometry restraints were generated using electronic Ligand Builder and Optimization Workbench (eLBOW) ( 44 ) and fitted into the cryo-EM density by LigandFit GUI ( 45 ) in Phenix (v1.18.2-3874).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot v0.9.4.1] -> visualisation [ChimeraX v1.0, PyMOL v2.1, UCSF Chimera v1.13.1] -> stage not stated [CTFFIND v1.06, PHENIX v1.18.2, RELION]

### Two conformations of the Tom20 preprotein receptor in the TOM holo complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301447120 | PMCID: PMC10450662 | PMID: 37579144
- Evidence: Additional real-space refinement was performed in Phenix ( 57 ).
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, ChimeraX, MotionCor2, RELION]

### Structural analysis of the dual agonism at GLP-1R and GCGR. (PNAS 2023)

- DOI: 10.1073/pnas.2303696120 | PMCID: PMC10438375 | PMID: 37549266
- Version used: **1.19.1**
- Evidence: Real-space refinement was performed using Phenix v1.19.1 ( 49 ).
- Full pipeline: structure determination [PHENIX v1.19.1] -> visualisation [PyMOL v2.1] -> stage not stated [UCSF Chimera v1.15]

### Transition State of Arp2/3 Complex Activation by Actin-Bound Dimeric Nucleation-Promoting Factor. (PNAS 2023)

- DOI: 10.1073/pnas.2306165120 | PMCID: PMC10434305 | PMID: 37549294
- Evidence: The cryo-EM structures of NPF-bound Arp2/3 complex (6UHC) and CapZ-bound dynactin (6F1T) were used as starting models for model building and refinement using Coot ( 55 ) and Phenix ( 56 ), respectively ( Table 1 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.1]

### Insight into the mechanism of H&lt;sup&gt;+&lt;/sup&gt;-coupled nucleobase transport. (PNAS 2023)

- DOI: 10.1073/pnas.2302799120 | PMCID: PMC10438392 | PMID: 37549264
- Evidence: Molecular replacement using the core domain of either the AlphaFold2 prediction or UraA (PDB ID 5XLS) as a search model led to a solution for the initial phase, which was improved by iterations of modeling building in COOT ( 32 ) and refinement in PHENIX ( 33 ).
- Full pipeline: structure determination [AlphaFold, PHENIX]

### The structure of <i>Plasmodium falciparum</i> multidrug resistance protein 1 reveals an N-terminal regulatory domain. (PNAS 2023)

- DOI: 10.1073/pnas.2219905120 | PMCID: PMC10410737 | PMID: 37527341
- Evidence: This model was mutated, manually adjusted, and rebuilt in Coot ( 56 ) and refined against the cryo-EM map using phenix.real_space_refine in PHENIX ( 57 ).
- Full pipeline: registration [MotionCor2, RELION v3.0] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [UCSF Chimera]

### Structural polymorphisms within a common powdery mildew effector scaffold as a driver of coevolution with cereal immune receptors. (PNAS 2023)

- DOI: 10.1073/pnas.2307604120 | PMCID: PMC10410722 | PMID: 37523523
- Evidence: The crystal structures of these five AVR effectors were determined by molecular replacement (MR) with Phenix using structures predicted by AF2 as the initial search model.
- Full pipeline: alignment/mapping [MUSCLE] -> visualisation [ChimeraX v1.3] -> stage not stated [AlphaFold, PHENIX]

### Structural basis for binding of <i>Drosophila</i> Smaug to the GPCR Smoothened and to the germline inducer Oskar. (PNAS 2023)

- DOI: 10.1073/pnas.2304385120 | PMCID: PMC10410706 | PMID: 37523566
- Evidence: The phases were determined with multiwavelength anomalous dispersion using the reflections from the peak of SeMet derivatives and the native crystal using the AutoSol program of the PHENIX suite ( 77 ).
- Full pipeline: structure determination [PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold v1.5.2, PHENIX]

### AcrIIC4 inhibits type II-C Cas9 by preventing R-loop formation. (PNAS 2023)

- DOI: 10.1073/pnas.2303675120 | PMCID: PMC10400994 | PMID: 37494395
- Evidence: Model building and refinement were performed in COOT and PHENIX, respectively.
- Full pipeline: structure determination [PHENIX] -> stage not stated [RELION v3.1]

### Efficient tagging of endogenous proteins in human cell lines for structural studies by single-particle cryo-EM. (PNAS 2023)

- DOI: 10.1073/pnas.2302471120 | PMCID: PMC10401002 | PMID: 37487103
- Evidence: Crystal structure of GAPDH (PDB:4WNC) was docked into cryo-EM density using USCF Chimera, and manually modified by using Coot ( 77 ), followed by several rounds of real-space refinement in Phenix ( 78 ).
- Full pipeline: structure determination [PHENIX] -> machine learning [Cellpose] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [CTFFIND, Coot, ImageJ, MotionCor2, RELION, Topaz]

### Mechanism of RanGTP priming H2A-H2B release from Kap114 in an atypical RanGTP•Kap114•H2A-H2B complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301199120 | PMCID: PMC10629556 | PMID: 37450495
- Evidence: All the models were roughly docked into the map using UCSF Chimera ( 45 ) before subjected to real-space refinement with default settings of global minimization, rigid body, local grid search, Atomic Displacement Parameters (ADP or B-factors), and NQH flip refinement for 10 macrocycles, with secondary structure and Ramachandran restraints on Phenix ( 46 ).
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [ChimeraX, PHENIX, UCSF Chimera] -> visualisation [MAFFT] -> stage not stated [PyMOL v2.5]

### Structures and membrane interactions of native serotonin transporter in complexes with psychostimulants. (PNAS 2023)

- DOI: 10.1073/pnas.2304602120 | PMCID: PMC10629533 | PMID: 37436958
- Evidence: The model was further refined using real-space refinement in PHENIX ( 86 ).
- Full pipeline: alignment/mapping [RELION] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [CTFFIND, MotionCor2, VMD]

### Crystal structures of multidrug efflux transporters from <i>Burkholderia pseudomallei</i> suggest details of transport mechanism. (PNAS 2023)

- DOI: 10.1073/pnas.2215072120 | PMCID: PMC10629574 | PMID: 37428905
- Evidence: Further processing was carried out with programs from the CCP4 suite ( 57 ) and Phenix ( 58 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [CCP4, PHENIX]

### ToxR activates the <i>Vibrio cholerae</i> virulence genes by tethering DNA to the membrane through versatile binding to multiple sites. (PNAS 2023)

- DOI: 10.1073/pnas.2304378120 | PMCID: PMC10629549 | PMID: 37428913
- Evidence: Atomic models were traced in Coot ( 25 ) and refined using REFMAC5 ( 26 ) and Phenix ( 27 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### The evolution of archaeal flagellar filaments. (PNAS 2023)

- DOI: 10.1073/pnas.2304256120 | PMCID: PMC10334743 | PMID: 37399404
- Evidence: These initial models were then subject to refinement in Coot ( 66 ) and using Phenix real-space refinement ( 67 ).
- Full pipeline: alignment/mapping [UCSF Chimera] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, EMAN2]

### GPCR targeting of E3 ubiquitin ligase MDM2 by inactive β-arrestin. (PNAS 2023)

- DOI: 10.1073/pnas.2301934120 | PMCID: PMC10334748 | PMID: 37399373
- Evidence: Subsequent manual model building was carried out using the COOT program ( 72 ), and restrained refinement was performed using the software REFMAC5 ( 73 ) and PHENIX ( 74 ).
- Full pipeline: structure determination [PHENIX] -> machine learning [PHENIX] -> stage not stated [AlphaFold, ColabFold v1.5.2, PyMOL]

### De novo designed ice-binding proteins from twist-constrained helices. (PNAS 2023)

- DOI: 10.1073/pnas.2220380120 | PMCID: PMC10319034 | PMID: 37364125
- Evidence: Structures were refined in Phenix ( 40 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ImageJ]

### Dual factors required for cytochrome-P450-mediated hydrocarbon ring contraction in bacterial gibberellin phytohormone biosynthesis. (PNAS 2023)

- DOI: 10.1073/pnas.2221549120 | PMCID: PMC10293830 | PMID: 37339230
- Evidence: Morphing of the molecular replacement output model, using Morph model ( 33 ) in the Phenix software suite ( 34 ), was necessary prior to model rebuilding.
- Full pipeline: visualisation [Coot, PyMOL] -> stage not stated [CCP4, PHENIX]

### 30S subunit recognition and G1405 modification by the aminoglycoside-resistance 16S ribosomal RNA methyltransferase RmtC. (PNAS 2023)

- DOI: 10.1073/pnas.2304128120 | PMCID: PMC10288597 | PMID: 37307464
- Evidence: Refined maps were postprocessed in both Relion ( 37 ) and in Phenix ( 43 ), and the maps with the best density in each region were used for model building.
- Full pipeline: registration [CTFFIND] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, RELION v3.1, UCSF Chimera]

### A specialized integrin-binding motif enables proTGF-β2 activation by integrin αVβ6 but not αVβ8. (PNAS 2023)

- DOI: 10.1073/pnas.2304874120 | PMCID: PMC10268255 | PMID: 37279271
- Evidence: Autobuilding was performed using Phenix followed by iterative rounds of model building in Coot and refinement in Phenix ( 63 – 65 ).
- Full pipeline: alignment/mapping [MAFFT] -> normalisation [CCP4] -> structure determination [Coot, PHENIX]

### Structural insights into the assembly of the agrin/LRP4/MuSK signaling complex. (PNAS 2023)

- DOI: 10.1073/pnas.2300453120 | PMCID: PMC10266037 | PMID: 37252960
- Evidence: The model was refined by using the real-space refinement module in the Phenix package (V1.17) ( 32 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, RELION]

### Scribble scrambles parathyroid hormone receptor interactions to regulate phosphate and vitamin D homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2220851120 | PMCID: PMC10266016 | PMID: 37252981
- Evidence: The solutions produced by Phaser were manually rebuilt over multiple cycles using Coot ( 43 ) and refined using PHENIX ( 44 ).
- Full pipeline: simulation/modelling [VMD v1.9.3] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Structure of the priming arabinosyltransferase AftA required for AG biosynthesis of <i>Mycobacterium tuberculosis</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302858120 | PMCID: PMC10265970 | PMID: 37252995
- Version used: **1.12**
- Evidence: Manual adjustment of the complete model was first performed in COOT 0.8.8 ( 48 ), followed by iterative rounds of real-space refinement in PHENIX 1.12 ( 49 ) and manual adjustment in COOT.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX v1.12] -> stage not stated [CTFFIND, ChimeraX, Docker, PyMOL, RDKit, UCSF Chimera]

### Cryo-EM structure of the Mon1-Ccz1-RMC1 complex reveals molecular basis of metazoan RAB7A activation. (PNAS 2023)

- DOI: 10.1073/pnas.2301725120 | PMCID: PMC10235969 | PMID: 37216550
- Version used: **1.19**
- Evidence: These models were then fitted into the EM density map using UCSF Chimera1.14 ( 41 ), and underwent rounds of manual adjustment and real-space refinement using Coot 0.8.9.2 ( 42 ) and Phenix 1.19 ( 43 ), respectively.
- Full pipeline: structure determination [PHENIX v1.19] -> machine learning [EMAN2] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ImageJ, RELION v3.1]

### Molecular mechanism of fatty acid activation of FFAR1. (PNAS 2023)

- DOI: 10.1073/pnas.2219569120 | PMCID: PMC10235965 | PMID: 37216523
- Version used: **1.19.2**
- Evidence: A full model was built in Coot and subjected to multiple rounds of iterative real-space refinement in Phenix v.
- Full pipeline: normalisation [MotionCor2] -> registration [MotionCor2] -> simulation/modelling [NAMD v2.14] -> structure determination [Coot v0.9.4.1, PHENIX v1.19.2] -> stage not stated [R v3.50, RELION v3.1, UCSF Chimera v1.3]

### Structural insights into the transcription activation mechanism of the global regulator GlnR from actinobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2300282120 | PMCID: PMC10235972 | PMID: 37216560
- Evidence: The model of Sae GlnR-DBD complexed with DNA was built in Coot ( 56 ) and refined in Phenix ( 57 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [PyMOL, RELION v3.1]

### Starvation sensing by mycobacterial RelA/SpoT homologue through constitutive surveillance of translation. (PNAS 2023)

- DOI: 10.1073/pnas.2302006120 | PMCID: PMC10235957 | PMID: 37216503
- Evidence: Cryo-EM maps were analyzed using Chimera ( 60 ), Coot ( 61 ), and PHENIX ( 62 ).
- Full pipeline: registration [MotionCor2, RELION] -> stage not stated [PHENIX]

### The membrane electric field regulates the PIP<sub>2</sub>-binding site to gate the KCNQ1 channel. (PNAS 2023)

- DOI: 10.1073/pnas.2301985120 | PMCID: PMC10214144 | PMID: 37192161
- Evidence: The model was edited and refined using the ISOLDE ( 65 ) plugin in ChimeraX v1.2.0 ( 66 ) or WinCoot v0.98.1 ( 67 ) followed by real-space refinement in Phenix ( 68 ).
- Full pipeline: structure determination [ChimeraX v1.2.0, PHENIX, PyMOL] -> stage not stated [RELION v4.0]

### Mechanistic insights into the regulation of cell wall hydrolysis by FtsEX and EnvC at the bacterial division site. (PNAS 2023)

- DOI: 10.1073/pnas.2301897120 | PMCID: PMC10214136 | PMID: 37186861
- Evidence: These models were rigid-body fitted to our cryo-EM maps in the University of California, San Francisco (UCSF) Chimera ( 55 ), manually rebuilt in Coot ( 56 ), and refined using real space refinement in Phenix ( 57 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold]

### <i>Gβγ</i> activates <i>PIP2</i> hydrolysis by recruiting and orienting <i>PLCβ</i> on the membrane surface. (PNAS 2023)

- DOI: 10.1073/pnas.2301121120 | PMCID: PMC10194004 | PMID: 37172014
- Evidence: Atomic models from previously determined structures were fit into our density maps, refined using PHENIX real-space refine ( 52 ), and manually adjusted.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX]

### Structure of WNT inhibitor adenomatosis polyposis coli down-regulated 1 (APCDD1), a cell-surface lipid-binding protein. (PNAS 2023)

- DOI: 10.1073/pnas.2217096120 | PMCID: PMC10193966 | PMID: 37155902
- Evidence: The model of eMBP-APCDD1 was completed by manual building in COOT ( 76 ) and refinement was performed using REFMAC5 ( 77 ) and PHENIX Refine ( 78 ) with translation-libration-screw (TLS) parameterization.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CCP4, PyMOL, RoseTTAFold]

### Structure of the metazoan Rab7 GEF complex Mon1-Ccz1-Bulli. (PNAS 2023)

- DOI: 10.1073/pnas.2301908120 | PMCID: PMC10193976 | PMID: 37155863
- Evidence: Model building started from AlphaFold ( 30 ) predictions that were iteratively refined using Coot ( 43 ) and Phenix ( 44 ).
- Full pipeline: structure determination [AlphaFold, PHENIX]

### Direct tests of cytochrome <i>c</i> and <i>c</i><sub>1</sub> functions in the electron transport chain of malaria parasites. (PNAS 2023)

- DOI: 10.1073/pnas.2301047120 | PMCID: PMC10175771 | PMID: 37126705
- Evidence: Initial phases were determined by single-wavelength anomalous dispersion (SAD) phasing methods in PHENIX using the anomalous signal from the heme iron.
- Full pipeline: alignment/mapping [PyMOL v2.0] -> visualisation [PyMOL v2.0] -> stage not stated [Fiji, ImageJ, PHENIX]

### Identification of small-molecule protein-protein interaction inhibitors for NKG2D. (PNAS 2023)

- DOI: 10.1073/pnas.2216342120 | PMCID: PMC10160951 | PMID: 37098070
- Evidence: The structure was refined by iterative cycling between Coot ( 30 ) and Phenix ( 31 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL]

### Structures of Vac8-containing protein complexes reveal the underlying mechanism by which Vac8 regulates multiple cellular processes. (PNAS 2023)

- DOI: 10.1073/pnas.2211501120 | PMCID: PMC10161063 | PMID: 37094131
- Evidence: Following rigid-body and positional refinement of the model with the phaser (PHENIX), the complete sequence of tVac17 (residues 290 to 308 and residues 330 to 344) could be positioned into residual electron density.
- Full pipeline: structure determination [PHENIX]

### Mechanistic insights into DNA binding and cleavage by a compact type I-F CRISPR-Cas system in bacteriophage. (PNAS 2023)

- DOI: 10.1073/pnas.2215098120 | PMCID: PMC10161043 | PMID: 37094126
- Evidence: The atomic models were built using Coot, refined using Phenix ( 44 ), and assessed using MolProbity ( 45 ).
- Full pipeline: quantification [ImageJ] -> registration [MotionCor2] -> dimensionality reduction/clustering [RELION v3.0] -> structure determination [PHENIX, RELION v3.0] -> visualisation [PyMOL]

### Structure of the human respiratory complex II. (PNAS 2023)

- DOI: 10.1073/pnas.2216713120 | PMCID: PMC10161127 | PMID: 37098072
- Evidence: To start model building, the predicted domains of four subunits were docked into the EM density map by using Chimera ( 47 ), followed by manual adjustment of main chains and side chains in Coot ( 48 ) and real space refinement in PHENIX ( 49 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold]

### In situ architecture and membrane fusion of SARS-CoV-2 Delta variant. (PNAS 2023)

- DOI: 10.1073/pnas.2213332120 | PMCID: PMC10160983 | PMID: 37094167
- Evidence: Then, the model was real-space refined in PHENIX.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD, PHENIX] -> stage not stated [Coot, MotionCor2, RELION, ilastik]

### Bioactive compounds from Huashi Baidu decoction possess both antiviral and anti-inflammatory effects against COVID-19. (PNAS 2023)

- DOI: 10.1073/pnas.2301775120 | PMCID: PMC10160982 | PMID: 37094153
- Evidence: The models were built using Coot ( 66 ) and refined with a simulated annealing protocol implemented in the program PHENIX ( 67 ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [PHENIX] -> structure determination [PHENIX] -> stage not stated [AutoDock Vina, CCP4]

### Structural insights into HIV-1 polyanion-dependent capsid lattice formation revealed by single particle cryo-EM. (PNAS 2023)

- DOI: 10.1073/pnas.2220545120 | PMCID: PMC10160977 | PMID: 37094124
- Evidence: An initial reference model was prepared in UCSF Chimera ( 63 ) by docking the crystal structure of full-length hexameric CA (PDB 4XFX) into the cryo-EM map of SUV-templated CA lattice prepared at pH 7.4 with IP 6 and then refined using the Real Space Refinement tool in Phenix ( 64 ).
- Full pipeline: registration [RELION v4.0] -> structure determination [ChimeraX, Coot, PHENIX, UCSF Chimera]

### Interactions of TonB-dependent transporter FoxA with siderophores and antibiotics that affect binding, uptake, and signal transduction. (PNAS 2023)

- DOI: 10.1073/pnas.2221253120 | PMCID: PMC10120069 | PMID: 37043535
- Evidence: The structure was determined using molecular replacement with PHENIX Phaser using apo-FoxA as a starting model (PDB: 6I98) and refined using phenix.refine ( 51 ).
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AutoDock Vina]

### Two structural switches in HIV-1 capsid regulate capsid curvature and host factor binding. (PNAS 2023)

- DOI: 10.1073/pnas.2220557120 | PMCID: PMC10120081 | PMID: 37040417
- Evidence: Models were finally refined as complete hexameric or pentameric assemblies using PHENIX.real_space_refinement ( 47 ) with noncrystallographic symmetry enforced where appropriate.
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [ChimeraX, PHENIX] -> stage not stated [UCSF Chimera]

### Interdigitated immunoglobulin arrays form the hyperstable surface layer of the extremophilic bacterium &lt;i&gt;Deinococcus radiodurans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2215808120 | PMCID: PMC10120038 | PMID: 37043530
- Evidence: The atomic model was then placed into the hexameric map as six copies and subjected to several rounds of refinement using refmac5 ( 67 ) inside the Collaborative Computational Project for electron cryo-microscopy (CCP-EM) software suite ( 68 ) and PHENIX ( 69 ), followed by manually rebuilding in Coot ( 66 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold v2.2.0, ChimeraX, MotionCor2, RELION]

### Yeast PIC-Mediator structure with RNA polymerase II C-terminal domain. (PNAS 2023)

- DOI: 10.1073/pnas.2220542120 | PMCID: PMC10104585 | PMID: 37014863
- Evidence: Real space refinement was conducted with the PHENIX suite ( 41 , 42 ).
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [PHENIX, RELION] -> visualisation [ChimeraX, PyMOL v2.4] -> stage not stated [AlphaFold, UCSF Chimera]

### Deciphering the evolution of flavin-dependent monooxygenase stereoselectivity using ancestral sequence reconstruction. (PNAS 2023)

- DOI: 10.1073/pnas.2218248120 | PMCID: PMC10104550 | PMID: 37014851
- Evidence: Refinement was done using Phenix ( 64 ) and model building with Coot ( 65 ).
- Full pipeline: alignment/mapping [MUSCLE] -> normalisation [CCP4] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Structural insights into plasmalemma vesicle-associated protein (PLVAP): Implications for vascular endothelial diaphragms and fenestrae. (PNAS 2023)

- DOI: 10.1073/pnas.2221103120 | PMCID: PMC10083539 | PMID: 36996108
- Evidence: The substructures found in SHELX D were refined and completed for the final 24 substructure sites using PHASER ( 75 ) at PHENIX AutoSol ( 34 , 35 ) with a resolution cutoff at 2.4 Å, and 4 noncrystallographic symmetry copies using THOROUGH for further substructure searches.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [CCP4, PyMOL]

### Structural basis for severe pain caused by mutations in the S4-S5 linkers of voltage-gated sodium channel Na<sub>V</sub>1.7. (PNAS 2023)

- DOI: 10.1073/pnas.2219624120 | PMCID: PMC10083536 | PMID: 36996107
- Evidence: Subsequently structures were refined with Phenix.refine module and the final structures were analyzed and validated using MolProbity in the Phenix program suite ( 52 ) ( SI Appendix , Table S3 ).
- Full pipeline: structure determination [CCP4, PHENIX, REFMAC] -> stage not stated [Coot]

### Neuronal activity-induced, equilibrative nucleoside transporter-dependent, somatodendritic adenosine release revealed by a GRAB sensor. (PNAS 2023)

- DOI: 10.1073/pnas.2212387120 | PMCID: PMC10083574 | PMID: 36996110
- Evidence: To screen the medium affinity adenosine sensor, HEK293T cells were imaged using an Opera Phenix High-Content Screening System (PerkinElmer).
- Full pipeline: stage not stated [DIPY, ImageJ, PHENIX]

### A DNA damage-induced phosphorylation circuit enhances Mec1<sup>ATR</sup> Ddc2<sup>ATRIP</sup> recruitment to Replication Protein A. (PNAS 2023)

- DOI: 10.1073/pnas.2300150120 | PMCID: PMC10083555 | PMID: 36996117
- Evidence: The crystal structures were determined by molecular replacement using Phaser (PDB 5OMB) and refined in the PHENIX package.
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [PHENIX]

### A general mechanism for transcription bubble nucleation in bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2220874120 | PMCID: PMC10083551 | PMID: 36972428
- Evidence: Combined maps for model building were generated using phenix.combine_focused_maps from the PHENIX package ( 39 ).
- Full pipeline: quantification [ImageJ] -> normalisation [MotionCor2] -> differential/statistical testing [RELION v3.1] -> structure determination [ChimeraX, Coot, RELION v3.1] -> stage not stated [HMMER, PHENIX]

### Indoline CD4-mimetic compounds mediate potent and broad HIV-1 inhibition and sensitization to antibody-dependent cellular cytotoxicity. (PNAS 2023)

- DOI: 10.1073/pnas.2222073120 | PMCID: PMC10068826 | PMID: 36961924
- Evidence: Crystal structures were solved by the molecular replacement module in PHENIX using the unliganded HIV-1C 1086 gp120 core e structure (PDB ID: 3TGR) and refined with phenix.refine.
- Full pipeline: structure determination [PHENIX]

### A c-di-GMP binding effector controls cell size in a cyanobacterium. (PNAS 2023)

- DOI: 10.1073/pnas.2221874120 | PMCID: PMC10068817 | PMID: 36947515
- Evidence: The AutoSol program in Phenix ( 43 ) was used to search the selenium atoms and to calculate the phase.
- Full pipeline: stage not stated [AlphaFold, PHENIX]

### Structure of mycobacterial respiratory complex I. (PNAS 2023)

- DOI: 10.1073/pnas.2214949120 | PMCID: PMC10068793 | PMID: 36952383
- Version used: **1.19.2**
- Evidence: Optimization of model-to-map fit and atomic model dihedral angles was done with Coot v0.9.6 ( 106 ), followed by several rounds of refinement with ISOLDE v1.3 ( 107 ) and PHENIX v1.19.2 ( 108 ).
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [RELION] -> structure determination [PHENIX v1.19.2] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, Coot v0.9.6]

### Cryo-EM analyses of KIT and oncogenic mutants reveal structural oncogenic plasticity and a target for therapeutic intervention. (PNAS 2023)

- DOI: 10.1073/pnas.2300054120 | PMCID: PMC10068818 | PMID: 36943885
- Version used: **1.02.1**
- Evidence: Following model building, the model was refined using real-space refinement in Phenix (version 1.02.1-4487-000) ( 34 ).
- Full pipeline: structure determination [PHENIX v1.02.1] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, RELION v3.1, UCSF Chimera]

### Structure-based design of a SARS-CoV-2 Omicron-specific inhibitor. (PNAS 2023)

- DOI: 10.1073/pnas.2300360120 | PMCID: PMC10068829 | PMID: 36940324
- Evidence: The structure was then subjected to real space refinement (global minimization, local grid search, adp) in PHENIX ( 31 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, MotionCor2, PyMOL, RELION, UCSF Chimera]

### Cryo-EM structure of the four-subunit <i>Rhodobacter sphaeroides</i> cytochrome <i>bc</i><sub>1</sub> complex in styrene maleic acid nanodiscs. (PNAS 2023)

- DOI: 10.1073/pnas.2217922120 | PMCID: PMC10041115 | PMID: 36913593
- Version used: **1.19.2**
- Evidence: The complete model was further optimized using the ISOLDE 1.2 plugin for ChimeraX ( 58 ) followed by final real-space refinement in Phenix v1.19.2 ( 92 ).
- Full pipeline: structure determination [Coot v0.9.6, PHENIX v1.19.2] -> stage not stated [AlphaFold, ChimeraX v1.3, RELION v3.1]

### Structural basis and dynamics of Chikungunya alphavirus RNA capping by nsP1 capping pores. (PNAS 2023)

- DOI: 10.1073/pnas.2213934120 | PMCID: PMC10041110 | PMID: 36913573
- Evidence: Resulting maps were sharpened suing Phenix autosharpen map ( 44 ).
- Full pipeline: stage not stated [PHENIX, RELION v3.0, UCSF Chimera]

### Biocatalytic control of site-selectivity and chain length-selectivity in radical amino acid halogenases. (PNAS 2023)

- DOI: 10.1073/pnas.2214512120 | PMCID: PMC10041140 | PMID: 36913566
- Evidence: The structures were iteratively refined in COOT and Phenix.
- Full pipeline: structure determination [PHENIX]

### Bivalent molecular mimicry by ADP protects metal redox state and promotes coenzyme B<sub>12</sub> repair. (PNAS 2023)

- DOI: 10.1073/pnas.2220677120 | PMCID: PMC10243129 | PMID: 36888659
- Evidence: Iterative rounds of model building and refinement were performed with COOT ( 46 ) and Phenix ( 47 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [CCP4]

### A macrocyclic peptide inhibitor traps MRP1 in a catalytically incompetent conformation. (PNAS 2023)

- DOI: 10.1073/pnas.2220012120 | PMCID: PMC10089224 | PMID: 36893260
- Evidence: The structure was manually fit to the bMRP1 + CPI1 working map in Coot, and real-space refined against the working map in the PHENIX suite.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX, REFMAC, UCSF Chimera] -> stage not stated [PyMOL, RELION]

### Structure of the Wnt-Frizzled-LRP6 initiation complex reveals the basis for coreceptor discrimination. (PNAS 2023)

- DOI: 10.1073/pnas.2218238120 | PMCID: PMC10089208 | PMID: 36893265
- Evidence: The model was refined with Phenix ( 53 ) using global minimization and B-factor with the starting model as a reference model.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ChimeraX]

### Cryo-EM structure of the human chemerin receptor 1-Gi protein complex bound to the C-terminal nonapeptide of chemerin. (PNAS 2023)

- DOI: 10.1073/pnas.2214324120 | PMCID: PMC10089180 | PMID: 36881626
- Evidence: The models were docked into the EM density map using UCSF Chimera version 1.12, followed by iterative manual building in Coot-0.9.2 and refinement in Phenix-1.18.2.
- Full pipeline: structure determination [Coot, PHENIX, UCSF Chimera v1.12] -> stage not stated [AlphaFold]

### Structure-guided approach to modulate small molecule binding to a promiscuous ligand-activated protein. (PNAS 2023)

- DOI: 10.1073/pnas.2217804120 | PMCID: PMC10013835 | PMID: 36848571
- Evidence: Rifamycin S was placed with Phenix LigandFit ( 36 , 37 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [PHENIX]

### Discovery of cyanophycin dipeptide hydrolase enzymes suggests widespread utility of the natural biopolymer cyanophycin. (PNAS 2023)

- DOI: 10.1073/pnas.2216547120 | PMCID: PMC9974463 | PMID: 36800389
- Evidence: The structures were refined in REFMAC ( 70 ), Rosetta ( 71 ), PHENIX ( 72 ), and Coot ( 73 ).
- Full pipeline: structure determination [PHENIX, REFMAC] -> visualisation [PyMOL]

### A cryptic oxidoreductase safeguards oxidative protein folding in <i>Corynebacterium diphtheriae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2208675120 | PMCID: PMC9974433 | PMID: 36787356
- Evidence: The stereochemistry of the structure was validated with PHENIX suite ( 50 ) incorporating MOLPROBITY ( 51 ) tools.
- Full pipeline: structure determination [CCP4] -> stage not stated [PHENIX]

### Structure of metallochaperone in complex with the cobalamin-binding domain of its target mutase provides insight into cofactor delivery. (PNAS 2023)

- DOI: 10.1073/pnas.2214085120 | PMCID: PMC9974510 | PMID: 36787360
- Evidence: The structure was solved by molecular replacement with the Phenix implementation of Phaser ( 42 ) using data trimmed to 3.1 Å resolution.
- Full pipeline: read trimming [PHENIX] -> structure determination [Coot] -> visualisation [PyMOL v2.3.3] -> stage not stated [CCP4]

### Allosteric mechanism of transcription inhibition by NusG-dependent pausing of RNA polymerase. (PNAS 2023)

- DOI: 10.1073/pnas.2218516120 | PMCID: PMC9963633 | PMID: 36745813
- Evidence: The cryo-EM density maps were improved by Local anisotropic sharpening by Phenix ( 58 ).
- Full pipeline: quantification [ImageJ] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [UCSF Chimera]

### Structures of human gastrin-releasing peptide receptors bound to antagonist and agonist for cancer and itch therapy. (PNAS 2023)

- DOI: 10.1073/pnas.2216230120 | PMCID: PMC9963752 | PMID: 36724251
- Evidence: The generated final model was refined in Phenix ( 95 ).
- Full pipeline: structure determination [ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [R v3.50, RELION]

### The SspB adaptor drives structural changes in the AAA+ ClpXP protease during ssrA-tagged substrate delivery. (PNAS 2023)

- DOI: 10.1073/pnas.2219044120 | PMCID: PMC9963277 | PMID: 36730206
- Version used: **1.14**
- Evidence: ClpX domains were rigid-body-refined using Coot ( 37 ), and real-space refinement was performed using Phenix 1.14 ( 38 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.14, RELION v3.1] -> stage not stated [ChimeraX]

### Structural basis of V-ATPase V<sub>O</sub> region assembly by Vma12p, 21p, and 22p. (PNAS 2023)

- DOI: 10.1073/pnas.2217181120 | PMCID: PMC9963935 | PMID: 36724250
- Evidence: Atomic models were constructed by manual model building in Coot ( 56 ), followed by refinement with ISOLDE ( 57 ) and real space refinement with Phenix ( 58 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold]

### Structure and supramolecular organization of the canine distemper virus attachment glycoprotein. (PNAS 2023)

- DOI: 10.1073/pnas.2208866120 | PMCID: PMC9963377 | PMID: 36716368
- Version used: **1.19**
- Evidence: The final protein model (residues 130 (chain A)/134 ( chain B)/136 (chain C)/133 (chain D) to 602 (chains A–D) was obtained by several iterations of manual model building in Coot ( 70 ), real-space refinement in Phenix (version 1.19) ( 71 ), and structure validation using MolProbity ( 72 ).
- Full pipeline: registration [MotionCor2 v1.4.0] -> simulation/modelling [VMD] -> structure determination [PHENIX v1.19] -> visualisation [VMD] -> stage not stated [ChimeraX v1.3, Coot, PyMOL v2.5.2, RELION v3.1.1, UCSF Chimera v1.12]

### Arabidopsis Sec14 proteins (SFH5 and SFH7) mediate interorganelle transport of phosphatidic acid and regulate chloroplast development. (PNAS 2023)

- DOI: 10.1073/pnas.2221637120 | PMCID: PMC9963013 | PMID: 36716376
- Evidence: Standard refinement was performed with Coot, PHENIX, and REFMAC ( 44 – 46 ).
- Full pipeline: structure determination [PHENIX, REFMAC] -> stage not stated [PyMOL]

### Structural and functional insights into the chloroplast division site regulators PARC6 and PDV1 in the intermembrane space. (PNAS 2023)

- DOI: 10.1073/pnas.2215575120 | PMCID: PMC9945983 | PMID: 36696445
- Evidence: The structures were refined manually with COOT ( 39 ) and PHENIX ( 40 ).
- Full pipeline: structure determination [PHENIX]

### Cryo-EM structure of human voltage-gated sodium channel Na<sub>v</sub>1.6. (PNAS 2023)

- DOI: 10.1073/pnas.2220578120 | PMCID: PMC9945969 | PMID: 36696443
- Evidence: The refitted model was modified and adjusted in COOT based on sequence alignment in SnapGene and then refined against the corresponding map by the Real-space Refinement option in PHENIX with secondary structure and geometry restraints ( 52 , 53 ).
- Full pipeline: alignment/mapping [PHENIX] -> structure determination [PHENIX]

### Cryo-EM structure of the whole photosynthetic reaction center apparatus from the green sulfur bacterium <i>Chlorobaculum tepidum</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2216734120 | PMCID: PMC9945994 | PMID: 36693097
- Evidence: Restraints for all ligands were generated by eLBOW in Phenix ( 60 ).
- Full pipeline: registration [MotionCor2] -> stage not stated [ChimeraX, PHENIX, RELION v3.0, UCSF Chimera]

### Destabilizing NF1 variants act in a dominant negative manner through neurofibromin dimerization. (PNAS 2023)

- DOI: 10.1073/pnas.2208960120 | PMCID: PMC9945959 | PMID: 36689660
- Evidence: Structure refinement was done in Phenix ( 37 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, Coot, MotionCor2, RELION]

### Fine structure and assembly pattern of a minimal myophage Pam3. (PNAS 2023)

- DOI: 10.1073/pnas.2213727120 | PMCID: PMC9942802 | PMID: 36656854
- Evidence: Afterward, the models were manually adjusted and rebuilt by COOT ( 40 ) followed by the automatic refinement using the real-space refinement in PHENIX ( 41 ).
- Full pipeline: normalisation [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### Structural remodeling of AAA+ ATPase p97 by adaptor protein ASPL facilitates posttranslational methylation by METTL21D. (PNAS 2023)

- DOI: 10.1073/pnas.2208941120 | PMCID: PMC9942839 | PMID: 36656859
- Evidence: The structure of p97-ND1:ASPL-C ∆ :METTL21D was manually built using COOT ( 44 , 45 ) and refined with PHENIX ( 46 ) in an iterative manner until structure factor amplitudes derived from the built model fitted the experimentally observed diffraction pattern, reflected in the R work and R free values in a range expected for the given resolution.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL]

### Structure-function correlates of fibrinogen binding by <i>Acinetobacter</i> adhesins critical in catheter-associated urinary tract infections. (PNAS 2023)

- DOI: 10.1073/pnas.2212694120 | PMCID: PMC9942807 | PMID: 36652481
- Evidence: The dataset was solved by molecular replacement and refinement performed in Phenix, using MrkD (3U4K) for Abp2D, Abp2D (8DEZ) for R86E, and a trimmed model of Abp2D (8DEZ) for Abp1D.
- Full pipeline: read trimming [PHENIX] -> alignment/mapping [Clustal Omega] -> simulation/modelling [GROMACS v2020.1] -> structure determination [PHENIX] -> stage not stated [PyMOL]

### Evolution of nanobodies specific for BCL11A. (PNAS 2023)

- DOI: 10.1073/pnas.2218959120 | PMCID: PMC9933118 | PMID: 36626555
- Evidence: The phases of complexes were solved by the selenium single-wavelength anomalous diffraction (SAD) method using PHENIX ( 54 ).
- Full pipeline: visualisation [PyMOL] -> stage not stated [MACS2, PHENIX]

### Oligomer-to-monomer transition underlies the chaperone function of AAGAB in AP1/AP2 assembly. (PNAS 2023)

- DOI: 10.1073/pnas.2205199120 | PMCID: PMC9926252 | PMID: 36598941
- Evidence: Further model improvement was carried out with alternate rounds of refinement using Phenix.refine ( 32 ) and model building via COOT ( 33 ).
- Full pipeline: structure determination [PHENIX]

### Structural basis for regulation of SOS response in bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2217493120 | PMCID: PMC9926225 | PMID: 36598938
- Evidence: The coordinates were real-space refined with secondary structure restraints in Phenix ( 46 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [Coot, PHENIX] -> stage not stated [ImageJ]

### Differential dynamics and direct interaction of bound ligands with lipids in multidrug transporter ABCG2. (PNAS 2023)

- DOI: 10.1073/pnas.2213437120 | PMCID: PMC9910490 | PMID: 36580587
- Evidence: The restraint of tariquidar was generated in eLBOW of Phenix ( 48 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [CTFFIND, Coot v0.9, MotionCor2, PHENIX, VMD]

### SUMO enhances unfolding of SUMO-polyubiquitin-modified substrates by the Ufd1/Npl4/Cdc48 complex. (PNAS 2023)

- DOI: 10.1073/pnas.2213703120 | PMCID: PMC9910466 | PMID: 36574706
- Evidence: Composite maps were generated in Python-based Hierarchical ENvironment for Integrated Xtallography (PHENIX) ( 63 ) with focused refinement maps and atomic models were refined using PHENIX ( 63 ) and model geometry analyzed using Molprobity ( 64 ).
- Full pipeline: structure determination [PHENIX, Python] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, Coot, MotionCor2, RELION v3.0]

### Crystal structure of LGR ligand α2/β5 from <i>Caenorhabditis elegans</i> with implications for the evolution of glycoprotein hormones. (PNAS 2023)

- DOI: 10.1073/pnas.2218630120 | PMCID: PMC9910494 | PMID: 36574673
- Evidence: Phase evaluation and density modification were performed using Phenix.AutoSol ( 53 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [CCP4] -> stage not stated [AlphaFold, ColabFold, PHENIX, PyMOL]

### Structural basis of transition from initiation to elongation in de novo viral RNA-dependent RNA polymerases. (PNAS 2023)

- DOI: 10.1073/pnas.2211425120 | PMCID: PMC9910504 | PMID: 36577062
- Evidence: Manual model building and structure refinement were done using Coot and PHENIX, respectively ( 44 , 45 ).
- Full pipeline: structure determination [PHENIX]

### A structure-based mechanism for initiation of AP-3 coated vesicle formation. (PNAS 2024)

- DOI: 10.1073/pnas.2411974121 | PMCID: PMC11670113 | PMID: 39705307
- Version used: **1.21.1**
- Evidence: Final models were then further refined using Rosetta Relax, followed by B-factor refinement in Phenix (v1.21.1) ( 63 ).
- Full pipeline: structure determination [PHENIX v1.21.1] -> stage not stated [AlphaFold]

### A minimal complex of KHNYN and zinc-finger antiviral protein binds and degrades single-stranded RNA. (PNAS 2024)

- DOI: 10.1073/pnas.2415048121 | PMCID: PMC11670115 | PMID: 39693345
- Evidence: The model was refined with Phenix ( 41 ) iteratively with manual building in COOT ( 42 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, ImageJ]

### The C-terminal activating domain promotes pannexin 1 channel opening. (PNAS 2024)

- DOI: 10.1073/pnas.2411898121 | PMCID: PMC11665872 | PMID: 39671183
- Evidence: Models were iteratively refined using Phenix Real Space Refine ( 54 ) until the refinement parameters stopped improving.
- Full pipeline: registration [RELION v4.0] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Molecular basis of lipid and ligand regulation of prostaglandin receptor DP2. (PNAS 2024)

- DOI: 10.1073/pnas.2403304121 | PMCID: PMC11665870 | PMID: 39665758
- Evidence: This integration and subsequent model adjustments were carried out using UCSF Chimera ( 37 ), with iterative manual and automated refinements performed in COOT ( 38 ) and PHENIX ( 39 ), respectively.
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2]

### Structural insights into the assembly and energy transfer of haptophyte photosystem I-light-harvesting supercomplex. (PNAS 2024)

- DOI: 10.1073/pnas.2413678121 | PMCID: PMC11648859 | PMID: 39642204
- Evidence: The constructed model was refined using Phenix real-space refinement, incorporating geometry, and secondary structure restraints ( 76 ).
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Python]

### Structural basis of the allosteric regulation of cyanobacterial glucose-6-phosphate dehydrogenase by the redox sensor OpcA. (PNAS 2024)

- DOI: 10.1073/pnas.2411604121 | PMCID: PMC11648896 | PMID: 39642196
- Evidence: Iterative rounds of real-space refinement in PHENIX ( 31 ), accompanied by manual adjustments in Coot, were performed.
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [ImageJ]

### Structure of yeast RAVE bound to a partial V&lt;sub&gt;1&lt;/sub&gt; complex. (PNAS 2024)

- DOI: 10.1073/pnas.2414511121 | PMCID: PMC11648922 | PMID: 39625975
- Evidence: These models were adjusted manually in Coot ( 65 ), followed by refinement with ISOLDE ( 66 ), and real space refinement with PHENIX ( 67 ).
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, UCSF Chimera]

### Structural basis of chiral wrap and T-segment capture by &lt;i&gt;Escherichia coli&lt;/i&gt; DNA gyrase. (PNAS 2024)

- DOI: 10.1073/pnas.2407398121 | PMCID: PMC11626157 | PMID: 39589884
- Evidence: The complete model was refined in real space using Phenix ( 81 ) against an unsharpened map using Ramachandran restraints and secondary structure restraints for protein and DNA bases.
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [Coot, Topaz]

### MR1 presents vitamin B6-related compounds for recognition by MR1-reactive T cells. (PNAS 2024)

- DOI: 10.1073/pnas.2414792121 | PMCID: PMC11626183 | PMID: 39589872
- Evidence: Diffraction data were processed using XDS ( 58 ) and programs from the CCP4 suite ( 59 ) and Phenix package ( 60 ).
- Full pipeline: stage not stated [CCP4, PHENIX, PyMOL]

### Structural basis for the synergetic neutralization of hepatitis E virus by antibody-antibody interaction. (PNAS 2024)

- DOI: 10.1073/pnas.2408585121 | PMCID: PMC11626150 | PMID: 39585981
- Evidence: Models were built using COOT, refined by Phenix, and analyzed by PROCHECK ( SI Appendix, Table S1 ).
- Full pipeline: dimensionality reduction/clustering [NAMD] -> simulation/modelling [NAMD, VMD v1.9.3] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL]

### Identification of a depupylation regulator for an essential enzyme in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407239121 | PMCID: PMC11626117 | PMID: 39585979
- Evidence: The locally refined maps of Dop and Pup 91 were combined with the consensus map using PHENIX “Combine Focused Map” ( 66 ) to generate a composite map at 2.04 Å-resolution for model building.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1, PyMOL, SAMtools v1.13, featureCounts] -> quantification [featureCounts] -> normalisation [DESeq2 v1.40.2, tidyverse v2.0.0] -> differential/statistical testing [DESeq2 v1.40.2, tidyverse v2.0.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

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
- Evidence: The models were further refined using real-space refinement in Phenix ( 37 ) followed by manual adjustments in Coot.
- Full pipeline: simulation/modelling [NAMD v2.12, VMD] -> structure determination [Coot, PHENIX]

### Targeted degradation of Pin1 by protein-destabilizing compounds. (PNAS 2024)

- DOI: 10.1073/pnas.2403330121 | PMCID: PMC11588135 | PMID: 39531501
- Evidence: The structure of each inhibitor-modified protein was generated in an iterative process of rebuilding structure in COOT and refining each rebuild structure with phenix.refine from the PHENIX suite ( 60 , 61 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX v1.7] -> stage not stated [CCP4]

### A conserved mechanism couples cytosolic domain movements to pore gating in the TRPM2 channel. (PNAS 2024)

- DOI: 10.1073/pnas.2415548121 | PMCID: PMC11573590 | PMID: 39514307
- Evidence: Real-space refinement was carried out using PHENIX, and manual adjustment was done in Coot.
- Full pipeline: structure determination [Coot, PHENIX]

### A conserved juxtamembrane motif in plant NFR5 receptors is essential for root nodule symbiosis. (PNAS 2024)

- DOI: 10.1073/pnas.2405671121 | PMCID: PMC11572979 | PMID: 39495923
- Evidence: The NFR5-Nb200 dataset was analyzed in xtriage from the PHENIX program suite ( 50 ) and was due to high anisotropy elliptically truncated using the STARANISO Server [Global Phasing Ltd.
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [PHENIX]

### The structures of protein kinase A in complex with CFTR: Mechanisms of phosphorylation and noncatalytic activation. (PNAS 2024)

- DOI: 10.1073/pnas.2409049121 | PMCID: PMC11573500 | PMID: 39495916
- Evidence: These models were then adjusted based on the cryo-EM densities using Coot ( 67 ) and refined using PHENIX ( 68 ).
- Full pipeline: structure determination [PHENIX, RELION v4.0] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ImageJ, MotionCor2, UCSF Chimera]

### Structural duality enables a single protein to act as a toxin-antidote pair for meiotic drive. (PNAS 2024)

- DOI: 10.1073/pnas.2408618121 | PMCID: PMC11551426 | PMID: 39485800
- Evidence: To model Tdk1* tetramer, the Tdk1 monomer structure from the Tdk1(211–357)-Bdf1(372–554) complex structure was adjusted in COOT and real-space refined in PHENIX against the DeepEMhancer map.
- Full pipeline: alignment/mapping [minimap2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2]

### 2.6-Å resolution cryo-EM structure of a class Ia ribonucleotide reductase trapped with mechanism-based inhibitor N&lt;sub&gt;3&lt;/sub&gt;CDP. (PNAS 2024)

- DOI: 10.1073/pnas.2417157121 | PMCID: PMC11551348 | PMID: 39475643
- Evidence: The refined cryo-EM map was subjected to further sharpening by density modification in Phenix ( 61 ).
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [Coot, RELION]

### Toward understanding lipid reorganization in RNA lipid nanoparticles in acidic environments. (PNAS 2024)

- DOI: 10.1073/pnas.2404555121 | PMCID: PMC11551392 | PMID: 39475644
- Evidence: Imaging was carried out within a humidified imaging chamber on an Opera Phenix (Perkin Elmer, #HH14001000) spinning disk confocal microscope using a 20x Objective.
- Full pipeline: stage not stated [PHENIX]

### Biochemical analysis of EGFR exon20 insertion variants insASV and insSVD and their inhibitor sensitivity. (PNAS 2024)

- DOI: 10.1073/pnas.2417144121 | PMCID: PMC11551396 | PMID: 39471218
- Evidence: Structures were phased via molecular replacement and refined using Phenix with iterative rounds of manual model building in Coot ( 62 , 63 ).
- Full pipeline: structure determination [Coot, PHENIX]

### A protein phosphatase 1 specific &lt;i&gt;phos&lt;/i&gt;phatase &lt;i&gt;ta&lt;/i&gt;rgeting &lt;i&gt;p&lt;/i&gt;eptide (PhosTAP) to identify the PP1 phosphatome. (PNAS 2024)

- DOI: 10.1073/pnas.2415383121 | PMCID: PMC11536154 | PMID: 39446389
- Evidence: All structures were completed using multiple cycles of manual building and refinement using WinCoot and Phenix Refine ( 83 ), respectively.
- Full pipeline: structure determination [PHENIX]

### Structure and function of &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; EfpA as a lipid transporter and its inhibition by BRD-8000.3. (PNAS 2024)

- DOI: 10.1073/pnas.2412653121 | PMCID: PMC11536138 | PMID: 39441632
- Evidence: Subsequently, the dimeric model of EfpA was subjected to global refinement using the real-space feature in the PHENIX and the quality of the model was further analyzed in MolProbity ( 57 , 58 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4, Coot, UCSF Chimera]

### Cryo-EM structure of the zinc-activated channel (ZAC) in the Cys-loop receptor superfamily. (PNAS 2024)

- DOI: 10.1073/pnas.2405659121 | PMCID: PMC11536092 | PMID: 39441630
- Evidence: Real-space refinement was performed using PHENIX software ( 60 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> registration [RELION] -> structure determination [PHENIX] -> stage not stated [CTFFIND v4.1, ChimeraX, PyMOL, UCSF Chimera]

### CryoSeek: A strategy for bioentity discovery using cryoelectron microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2417046121 | PMCID: PMC11494351 | PMID: 39382995
- Evidence: The final models were refined using PHENIX with secondary structure and geometry restraints in real space ( 38 ).
- Full pipeline: quality control [MultiQC] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [MotionCor2]

### Structural insights into KSHV-GPCR constitutive activation and CXCL1 chemokine recognition. (PNAS 2024)

- DOI: 10.1073/pnas.2403217121 | PMCID: PMC11494311 | PMID: 39378089
- Evidence: Real-space refinements were performed using Phenix.
- Full pipeline: simulation/modelling [MDAnalysis, R v6.62, seaborn] -> structure determination [PHENIX] -> visualisation [MDAnalysis, PyMOL, seaborn]

### Engineering substrate channeling in a bifunctional terpene synthase. (PNAS 2024)

- DOI: 10.1073/pnas.2408064121 | PMCID: PMC11474042 | PMID: 39365814
- Evidence: As previously outlined in the cryo-EM structure determination of full-length PaFS ( 24 , 26 ), map analysis using PHENIX ( 57 ) indicated C 2 symmetry, which was confirmed with ProShade ( 58 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX]

### Capturing a methanogenic carbon monoxide dehydrogenase/acetyl-CoA synthase complex via cryogenic electron microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2410995121 | PMCID: PMC11474084 | PMID: 39361653
- Evidence: Models were iteratively real-space refined in Phenix ( 77 ) using noncrystallographic symmetry (NCS) restraints for the tetramer and hexamer.
- Full pipeline: structure determination [PHENIX] -> visualisation [AlphaFold] -> stage not stated [ChimeraX, RELION v4.0, cryoDRGN v0.3.4]

### Isoform-specific C-terminal phosphorylation drives autoinhibition of Casein kinase 1. (PNAS 2024)

- DOI: 10.1073/pnas.2415567121 | PMCID: PMC11474029 | PMID: 39356670
- Evidence: Model building was performed with Coot ( 60 ) and structure refinement was performed with PHENIX ( 61 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4, ImageJ, PyMOL]

### Structural basis for adhesin secretion by the outer-membrane usher in type 1 pili. (PNAS 2024)

- DOI: 10.1073/pnas.2410594121 | PMCID: PMC11459180 | PMID: 39316053
- Version used: **1.20.1**
- Evidence: Iterative rounds of model adjustment in Coot followed by real-space refinement in Phenix 1.20.1 ( 31 ) were performed until outliers were minimized based upon Ramachandron plot ( 32 , 33 ).
- Full pipeline: read trimming [Coot v0.9.8.7] -> structure determination [PHENIX v1.20.1] -> stage not stated [ChimeraX v1.5]

### Conformational ensembles in &lt;i&gt;Klebsiella pneumoniae&lt;/i&gt; FimH impact uropathogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2409655121 | PMCID: PMC11441496 | PMID: 39288182
- Evidence: Data were collected at ALS 4.2.2 macromolecular crystallography beamline, and the structure was solved by molecular replacement and refinement in Phenix using E. coli FimH lectin domain (PDB 1KLF trimmed to the lectin domain) as the search model ( SI Appendix , Table S6 ).
- Full pipeline: read trimming [PHENIX] -> simulation/modelling [GROMACS v2020.1] -> structure determination [PHENIX]

### Blobs form during the single-file transport of proteins across nanopores. (PNAS 2024)

- DOI: 10.1073/pnas.2405018121 | PMCID: PMC11420176 | PMID: 39264741
- Evidence: Manual rebuilding was performed with COOT ( 42 ) and refinement with PHENIX ( 43 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [Matplotlib, NumPy] -> stage not stated [ChimeraX, MDAnalysis, PyMOL]

### Structure-based design of a soluble human cytomegalovirus glycoprotein B antigen stabilized in a prefusion-like conformation. (PNAS 2024)

- DOI: 10.1073/pnas.2404250121 | PMCID: PMC11406251 | PMID: 39231203
- Evidence: The resulting local map was combined with the global map using PHENIX combine_focused_maps ( 49 ).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [AlphaFold, PHENIX]

### Cryo-EM structures of a mycobacterial ABC transporter that mediates rifampicin resistance. (PNAS 2024)

- DOI: 10.1073/pnas.2403421121 | PMCID: PMC11406275 | PMID: 39226350
- Evidence: The structures were manually adjusted in Coot followed by real-space-refinement using PHENIX ( 58 ) with reference to secondary structure and geometry restraints to prevent over-fitting.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, GROMACS v2022.2, PyMOL, UCSF Chimera]

### Structural basis of transcription: RNA polymerase II substrate binding and metal coordination using a free-electron laser. (PNAS 2024)

- DOI: 10.1073/pnas.2318527121 | PMCID: PMC11388330 | PMID: 39190355
- Evidence: Model building and refinement were performed using Coot ( 94 ) and Phenix ( 60 ).
- Full pipeline: structure determination [PHENIX]

### A potential role for RNA aminoacylation prior to its role in peptide synthesis. (PNAS 2024)

- DOI: 10.1073/pnas.2410206121 | PMCID: PMC11363276 | PMID: 39178230
- Evidence: The structures were solved using molecular replacement of the Fab BL3-6 from the previously reported structure [PDB code: 7SZU ( 57 )] as search model in Phenix Phaser ( 58 ), and the RNA was built into the emerging density after multiple rounds of refinement using Coot and Phenix Refine ( 59 – 61 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [XGBoost]

### Binding adaptability of chemical ligands to polymorphic α-synuclein amyloid fibrils. (PNAS 2024)

- DOI: 10.1073/pnas.2321633121 | PMCID: PMC11363296 | PMID: 39172784
- Version used: **1.13**
- Evidence: Subsequently, adjustments to the models were made in WinCoot 0.8.9.2 ( 67 ), followed by refinement against the respective maps using the phenix.real_space_refine program in PHENIX 1.13 ( 65 ), applying rotamer, Ramachandran, and geometry restraints.
- Full pipeline: structure determination [ChimeraX, PHENIX v1.13, PyMOL v1.7.4.5, UCSF Chimera v1.13.1] -> visualisation [ChimeraX, PyMOL v1.7.4.5] -> stage not stated [CTFFIND, RELION v3.1]

### Evolving dual-trait EPSP synthase variants using a synthetic yeast selection system. (PNAS 2024)

- DOI: 10.1073/pnas.2317027121 | PMCID: PMC11363307 | PMID: 39159366
- Evidence: The molecular replacement solution for wild-type EPSP synthase was iteratively built and refined using Coot ( 43 ) and Phenix ( 44 ) refinement packages.
- Full pipeline: structure determination [PHENIX]

### Disorder-to-order active site capping regulates the rate-limiting step of the inositol pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2400912121 | PMCID: PMC11348189 | PMID: 39145930
- Evidence: Models were subsequently real space refined using the PHENIX software package ( 66 ), applying secondary structure as well as map symmetry restraints.
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PyMOL, UCSF Chimera]

### Lipidomic scanning of self-lipids identifies headless antigens for natural killer T cells. (PNAS 2024)

- DOI: 10.1073/pnas.2321686121 | PMCID: PMC11348285 | PMID: 39141352
- Evidence: Diffraction data were collected at the Australian Synchrotron with molecular replacement using the PHASER-MR, Phenix, crystallographic object-oriented toolkit, and PyMOL programs.
- Full pipeline: stage not stated [PHENIX, PyMOL]

### An artificially evolved gene for herbicide-resistant rice breeding. (PNAS 2024)

- DOI: 10.1073/pnas.2407285121 | PMCID: PMC11348328 | PMID: 39133859
- Evidence: The model was optimized by interactive model correction with COOT ( 35 ) and refinement with PHENIX ( 36 ) until the R work and R free values converged.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4]

### AlphaFold two years on: Validation and impact. (PNAS 2024)

- DOI: 10.1073/pnas.2315002121 | PMCID: PMC11348012 | PMID: 39133843
- Evidence: Both major software suites for macromolecular crystallography, CCP4 ( 24 , 25 ) and PHENIX ( 26 ), now include import procedures that convert AlphaFold’s pLDDT * confidence metric into an estimated B-factor and remove low-confidence regions.
- Full pipeline: stage not stated [AlphaFold, CCP4, ChimeraX, ColabFold, PHENIX, RoseTTAFold]

### Structure of biofilm-forming functional amyloid PSMα1 from &lt;i&gt;Staphylococcus aureus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2406775121 | PMCID: PMC11331129 | PMID: 39116134
- Evidence: The model was then refined in PHENIX with default restrains and automated weight optimization ( 27 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [RELION] -> simulation/modelling [ChimeraX v1.7] -> structure determination [PHENIX]

### Structural basis for mouse receptor recognition by bat SARS2-like coronaviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2322600121 | PMCID: PMC11317568 | PMID: 39083418
- Evidence: PHENIX and CCP4 were used for molecular replacement and model refinement ( 40 , 41 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [CCP4, PHENIX] -> stage not stated [PyMOL]

### Structures of trehalose-6-phosphate synthase, Tps1, from the fungal pathogen &lt;i&gt;Cryptococcus neoformans&lt;/i&gt;: A target for antifungals. (PNAS 2024)

- DOI: 10.1073/pnas.2314087121 | PMCID: PMC11317593 | PMID: 39083421
- Evidence: Coordinates were then fitted manually in Coot ( 76 ) followed by iterative refinement using Phenix ( 77 ) real space refinement to improve the quality of the models.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [UCSF Chimera v1.14]

### Molecular mechanisms of proteoglycan-mediated semaphorin signaling in axon guidance. (PNAS 2024)

- DOI: 10.1073/pnas.2402755121 | PMCID: PMC11295036 | PMID: 39042673
- Evidence: This initial molecular replacement solution was further completed by several cycles of manual rebuilding in COOT ( 62 ) and refinement in Phenix ( 63 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ImageJ, Python]

### Structure of the flotillin complex in a native membrane environment. (PNAS 2024)

- DOI: 10.1073/pnas.2409334121 | PMCID: PMC11260169 | PMID: 38985763
- Evidence: The structure underwent iterative refinement using Coot and Phenix real-space refine ( 64 ) with noncrystallographic symmetry restraints while omitting geometry restraints.
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [AlphaFold, ChimeraX, PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [ColabFold, Coot]

### Nanopore tweezers show fractional-nucleotide translocation in sequence-dependent pausing by RNA polymerase. (PNAS 2024)

- DOI: 10.1073/pnas.2321017121 | PMCID: PMC11260103 | PMID: 38990947
- Evidence: Data were processed using HKL2000, structures determined using Phaser MR in Phenix and Coot, and iteratively updated using RNAP T.
- Full pipeline: stage not stated [PHENIX]

### Structural and mechanistic analysis of Ca<sup>2+</sup>-dependent regulation of transglutaminase 2 activity using a Ca<sup>2+</sup>-bound intermediate state. (PNAS 2024)

- DOI: 10.1073/pnas.2407066121 | PMCID: PMC11252922 | PMID: 38959038
- Evidence: The structures were refined by using Phenix ( 36 ) and manually fitted using the Coot ( 37 ) program.
- Full pipeline: quantification [ImageJ] -> structure determination [PHENIX]

### POTRA domains of the TamA insertase interact with the outer membrane and modulate membrane properties. (PNAS 2024)

- DOI: 10.1073/pnas.2402543121 | PMCID: PMC11252910 | PMID: 38959031
- Evidence: The Phenix suite and Coot ( 52 , 53 ) software were used during structure determination, refinement, and building cycles.
- Full pipeline: simulation/modelling [NAMD v2.14] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### Structural insights into the regulation of RyR1 by S100A1. (PNAS 2024)

- DOI: 10.1073/pnas.2400497121 | PMCID: PMC11228480 | PMID: 38917010
- Evidence: Atomic models were refined using real-space refinement in Phenix ( 63 ).
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [ChimeraX, PHENIX] -> stage not stated [Coot]

### Structural dynamics at cytosolic interprotomer interfaces control gating of a mammalian TRPM5 channel. (PNAS 2024)

- DOI: 10.1073/pnas.2403333121 | PMCID: PMC11228501 | PMID: 38923985
- Version used: **1.20**
- Evidence: At the final stage, models were subjected to a round of real space refinement using the PHENIX 1.20 real space refine ( 50 ) utility.
- Full pipeline: structure determination [PHENIX v1.20] -> stage not stated [Coot v0.98, UCSF Chimera]

### Modular binder technology by NGS-aided, high-resolution selection in yeast of designed armadillo modules. (PNAS 2024)

- DOI: 10.1073/pnas.2318198121 | PMCID: PMC11228518 | PMID: 38917007
- Evidence: The refinement was done in CCP4 using refmac5 ( 27 ) and in Phenix with PhenixRefine ( 28 ).
- Full pipeline: alignment/mapping [Bowtie2, UMAP] -> dimensionality reduction/clustering [Python, UMAP] -> structure determination [PHENIX] -> visualisation [UMAP] -> stage not stated [CCP4]

### Structural determinants of ivabradine block of the open pore of HCN4. (PNAS 2024)

- DOI: 10.1073/pnas.2402259121 | PMCID: PMC11228525 | PMID: 38917012
- Evidence: HCN4 – IVA model was rigid body fitted with UCSF CHIMERA and real-space refinement was performed with PHENIX using the previous HCN4 (PDB: 7NMN) coordinates as template.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [PHENIX] -> stage not stated [RELION]

### Structural basis for activation of somatostatin receptor 5 by cyclic neuropeptide agonists. (PNAS 2024)

- DOI: 10.1073/pnas.2321710121 | PMCID: PMC11214081 | PMID: 38885377
- Evidence: All models were fitted into the EM density map using UCSF Chimera ( 52 ) followed by iterative rounds of manual adjustment and automated rebuilding in COOT ( 53 ) and PHENIX ( 54 ), respectively.
- Full pipeline: registration [RELION v4.0] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, R v3.50]

### Peripheral positions encode transport specificity in the small multidrug resistance exporters. (PNAS 2024)

- DOI: 10.1073/pnas.2403273121 | PMCID: PMC11194549 | PMID: 38865266
- Evidence: Processed data were subjected to anisotropic truncation using Staraniso ( 46 ), and phases were calculated by molecular replacement with Phaser ( 47 ), with iterative rounds of refinement in Phenix ( 48 ) and model building in Coot ( 49 ).
- Full pipeline: structure determination [Coot, PHENIX]

### Cep57 regulates human centrosomes through multivalent interactions. (PNAS 2024)

- DOI: 10.1073/pnas.2305260121 | PMCID: PMC11194501 | PMID: 38857398
- Evidence: The crystal structure of Cep57C was solved by the molecular replacement program Phaser-MR in Phenix ( 58 ) using a previously determined structure (PDB ID: 4L0R) as the search model.
- Full pipeline: stage not stated [PHENIX, PyMOL]

### Asymmetric allostery in estrogen receptor-α homodimers drives responses to the ensemble of estrogens in the hormonal milieu. (PNAS 2024)

- DOI: 10.1073/pnas.2321344121 | PMCID: PMC11181081 | PMID: 38830107
- Evidence: The ERα-L372S/L536S mutant LBD was purified and crystallized, and the structures were solved as previously described ( 46 , 47 ) PHENIX software suite version 1.20 ( 48 ) and COOT ( 49 ).
- Full pipeline: visualisation [VMD] -> stage not stated [PHENIX, PyMOL, UCSF Chimera]

### Allosteric activation of VCP, an AAA unfoldase, by small molecule mimicry. (PNAS 2024)

- DOI: 10.1073/pnas.2316892121 | PMCID: PMC11181084 | PMID: 38833472
- Evidence: Only minor adjustments (real space sphere refinement within Coot and real space refinement within Phenix; see Materials and Methods ) to the docked VCP coordinates were required ( SI Appendix , Fig.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [MotionCor2, RELION]

### Bispecific antibodies targeting two glycoproteins on SFTSV exhibit synergistic neutralization and protection in a mouse model. (PNAS 2024)

- DOI: 10.1073/pnas.2400163121 | PMCID: PMC11181109 | PMID: 38830098
- Evidence: The atomic models were completed with COOT ( 30 ) and refined with PHENIX ( 31 ).
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, MUSCLE v3.8.31, MotionCor2] -> variant calling [SAMtools v1.9] -> structure determination [Coot v0.9.3, PHENIX] -> machine learning [Topaz] -> visualisation [PyMOL v2.0] -> stage not stated [fastp]

### Principles of peptide selection by the transporter associated with antigen processing. (PNAS 2024)

- DOI: 10.1073/pnas.2320879121 | PMCID: PMC11161800 | PMID: 38805290
- Evidence: The models were then iteratively edited and refined in Coot ( 68 ), ISOLDE ( 69 ), and PHENIX ( 70 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, RELION]

### Structural basis for EROS binding to human phagocyte NADPH oxidase NOX2. (PNAS 2024)

- DOI: 10.1073/pnas.2320388121 | PMCID: PMC11161758 | PMID: 38805284
- Evidence: The models were further refined and validated using the Phenix-1.20 programs.
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL]

### Molecular basis for antibody recognition of multiple drug-peptide/MHC complexes. (PNAS 2024)

- DOI: 10.1073/pnas.2319029121 | PMCID: PMC11145297 | PMID: 38781214
- Version used: **1.18.2**
- Evidence: The maps obtained for R023_soto-p 8 /A03, R023_soto-p 7 /A03, and R023_soto-p 7 /A11 were used to build the three structure models using WinCoot ( 55 ) and Phenix 1.18.2 software ( 56 ).
- Full pipeline: structure determination [UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [MotionCor2 v1.5, PHENIX v1.18.2, Python]

### Structure and mechanism of the human CTDNEP1-NEP1R1 membrane protein phosphatase complex necessary to maintain ER membrane morphology. (PNAS 2024)

- DOI: 10.1073/pnas.2321167121 | PMCID: PMC11145253 | PMID: 38776370
- Evidence: Phases were determined by molecular replacement in Phenix ( 49 ) using Phaser ( 50 ).
- Full pipeline: structure determination [Coot] -> stage not stated [AlphaFold, ImageJ, PHENIX]

### Inhibition of mRNA nuclear export promotes SARS-CoV-2 pathogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2314166121 | PMCID: PMC11145185 | PMID: 38768348
- Evidence: 1.5 glass coverslip) of a 24-well culture plate (Phenix Research Products).
- Full pipeline: stage not stated [PHENIX]

### Ultrapotent influenza hemagglutinin fusion inhibitors developed through SuFEx-enabled high-throughput medicinal chemistry. (PNAS 2024)

- DOI: 10.1073/pnas.2310677121 | PMCID: PMC11145270 | PMID: 38753503
- Evidence: Refinement was carried out in Phenix ( 50 ) and REFMAC5 ( 51 ) alternating with manual rebuilding and adjustment in COOT ( 5 ).
- Full pipeline: structure determination [PHENIX]

### <i>Myxococcus xanthus</i> encapsulin cargo protein EncD is a flavin-binding protein with ferric reductase activity. (PNAS 2024)

- DOI: 10.1073/pnas.2400426121 | PMCID: PMC11126975 | PMID: 38748579
- Evidence: The final structure was obtained after multiple rounds of model building with Coot and refinement with Phenix Refine ( 49 , 50 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> structure determination [PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, ColabFold v1.5.3, MotionCor2, RELION v4.0]

### Point mutation in a virus-like capsid drives symmetry reduction to form tetrahedral cages. (PNAS 2024)

- DOI: 10.1073/pnas.2321260121 | PMCID: PMC11098114 | PMID: 38722807
- Version used: **1.20.1**
- Evidence: Phenix v1.20.1-4487 ( 61 ) was used to find the symmetry operators from the map of the T = 1 shell using the symmetry-from-map function.
- Full pipeline: stage not stated [ChimeraX v1.25, PHENIX v1.20.1]

### Structural insights into human MHC-II association with invariant chain. (PNAS 2024)

- DOI: 10.1073/pnas.2403031121 | PMCID: PMC11087810 | PMID: 38687785
- Evidence: The models of HLA-DR/Ii and HLA-DQ/Ii complexes were refined against the corresponding map using PHENIX in real space with secondary structure and geometry restraints ( 44 ).
- Full pipeline: structure determination [ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [AlphaFold]

### Engineering tertiary chirality in helical biopolymers. (PNAS 2024)

- DOI: 10.1073/pnas.2321992121 | PMCID: PMC11087804 | PMID: 38684000
- Evidence: Structures were solved via molecular replacement on the PHENIX program package using search model 5W6W as a frame ( 51 ).
- Full pipeline: stage not stated [PHENIX]

### c-di-AMP determines the hierarchical organization of bacterial RCK proteins. (PNAS 2024)

- DOI: 10.1073/pnas.2318666121 | PMCID: PMC11067040 | PMID: 38652747
- Evidence: After the extension of the M2D1 helix in Coot ( 56 ), the model underwent 3 cycles of conservative refinement in Phenix ( 57 ).
- Full pipeline: structure determination [Coot, PHENIX]

### Dual function of LapB (YciM) in regulating <i>Escherichia coli</i> lipopolysaccharide synthesis. (PNAS 2024)

- DOI: 10.1073/pnas.2321510121 | PMCID: PMC11046580 | PMID: 38635633
- Evidence: The fitted model was refined in Phenix.real_space_refine with secondary structure restraints enabled ( 48 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, UCSF Chimera]

### C-type inactivation and proton modulation mechanisms of the TASK3 channel. (PNAS 2024)

- DOI: 10.1073/pnas.2320345121 | PMCID: PMC11046659 | PMID: 38630723
- Evidence: Manual adjustments were performed in COOT ( 56 ) where map density can reliably correct the initial model, before the structural models were subjected to real-space refinement against the corresponding cryo-EM map in Phenix ( 57 ).
- Full pipeline: registration [MotionCor2, RELION] -> simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> stage not stated [CTFFIND, ChimeraX, PyMOL]

### Structure and dynamics of a pentameric KCTD5/CUL3/Gβγ E3 ubiquitin ligase complex. (PNAS 2024)

- DOI: 10.1073/pnas.2315018121 | PMCID: PMC11047111 | PMID: 38625940
- Evidence: Models for KCTD5 (3DRX), CUL3 NTD (4EOZ), and Gβγ (1GP2) were docked into the maps and rebuilt and refined with COOT ( 61 ) and Phenix ( 62 ) to give final coordinates for KCTD5 CTD /Gβγ and KCTD5 BTB /CUL3 NTD .
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Tight-packing of large pilin subunits provides distinct structural and mechanical properties for the <i>Myxococcus xanthus</i> type IVa pilus. (PNAS 2024)

- DOI: 10.1073/pnas.2321989121 | PMCID: PMC11046646 | PMID: 38625941
- Evidence: The modified monomeric model was then real-space refined using Phenix ( 72 ) to improve the stereochemistry as well as the model-map correlation coefficient.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, Coot]

### Structural insights into the regulation of protein-arginine kinase McsB by McsA. (PNAS 2024)

- DOI: 10.1073/pnas.2320312121 | PMCID: PMC11046695 | PMID: 38625935
- Evidence: Cycles of refinement and model building were performed at 2.90 Å resolution using PHENIX.refine ( 40 ) and COOT ( 39 ).
- Full pipeline: normalisation [ImageJ] -> structure determination [PHENIX] -> visualisation [PyMOL]

### Proof-of-concept studies with a computationally designed M<sup>pro</sup> inhibitor as a synergistic combination regimen alternative to Paxlovid. (PNAS 2024)

- DOI: 10.1073/pnas.2320713121 | PMCID: PMC11046628 | PMID: 38621119
- Evidence: Phenix was used for successive rounds of refinement and COOT was used for model building.
- Full pipeline: structure determination [PHENIX]

### &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; telomere-binding proteins TEBP-1 and TEBP-2 adapt the Myb module to dimerize and bind telomeric DNA. (PNAS 2024)

- DOI: 10.1073/pnas.2316651121 | PMCID: PMC11032478 | PMID: 38588418
- Evidence: Molecular replacement was performed in Phaser ( 37 ) within the PHENIX suite ( 38 ) using the AlphaFold prediction ( 26 ) of the TEBP-2 MCD3 as a search model.
- Full pipeline: alignment/mapping [Clustal Omega, ColabFold] -> structure determination [Coot] -> stage not stated [AlphaFold, PHENIX]

### Structure and design of Langya virus glycoprotein antigens. (PNAS 2024)

- DOI: 10.1073/pnas.2314990121 | PMCID: PMC11032465 | PMID: 38593070
- Evidence: Models were refined into the cryoEM maps using Rosetta ( 93 – 95 ), Phenix ( 96 ), and ISOLDE ( 97 ) Validation used MolProbity ( 98 ), Phenix ( 96 ), and Privateer ( 99 ).
- Full pipeline: alignment/mapping [Topaz] -> differential/statistical testing [RELION] -> structure determination [PHENIX, RELION] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, ChimeraX]

### Conformational changes in the Niemann-Pick type C1 protein NCR1 drive sterol translocation. (PNAS 2024)

- DOI: 10.1073/pnas.2315575121 | PMCID: PMC11009665 | PMID: 38568972
- Evidence: The models were gradually improved by iterative rounds of real-space refinement using PHENIX ( 52 , 53 ) and manual adjustments in COOT.
- Full pipeline: alignment/mapping [ImageJ] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.3, Matplotlib, Python]

### Substrate recruitment via eIF2γ enhances catalytic efficiency of a holophosphatase that terminates the integrated stress response. (PNAS 2024)

- DOI: 10.1073/pnas.2320013121 | PMCID: PMC10998612 | PMID: 38547060
- Version used: **1.20.1**
- Evidence: The structure was solved by molecular replacement using Phaser ( 34 ) in Phenix (1.20.1-4487) ( 35 ) and a copy of AFM predicted human eIF2γ and eIF2α-CTD were found in an asymmetric unit.
- Full pipeline: quantification [ImageJ] -> structure determination [GROMACS] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, ChimeraX v1.6.1, Coot v0.9.8.7, PHENIX v1.20.1, PyMOL v1.3]

### Structural and mechanistic basis of the central energy-converting methyltransferase complex of methanogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2315568121 | PMCID: PMC10998594 | PMID: 38530900
- Evidence: Density modification was performed in PHENIX ( 27 ).
- Full pipeline: alignment/mapping [AlphaFold] -> stage not stated [CTFFIND, PHENIX, RELION]

### Rapid and automated design of two-component protein nanomaterials using ProteinMPNN. (PNAS 2024)

- DOI: 10.1073/pnas.2314646121 | PMCID: PMC10990136 | PMID: 38502697
- Evidence: Structures were refined in Phenix ( 70 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> machine learning [AlphaFold, RoseTTAFold]

### Structure of RADX and mechanism for regulation of RAD51 nucleofilaments. (PNAS 2024)

- DOI: 10.1073/pnas.2316491121 | PMCID: PMC10962997 | PMID: 38466836
- Evidence: The initial model was then further refined using both the real space refine package and secondary structure/stereochemical restraints in Phenix ( 41 ) and visualized using Coot ( 42 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [PHENIX] -> stage not stated [AlphaFold]

### Allosteric regulation of nitrate transporter NRT via the signaling protein PII. (PNAS 2024)

- DOI: 10.1073/pnas.2318320121 | PMCID: PMC10945777 | PMID: 38457518
- Evidence: Structure refinements were carried out by PHENIX ( 57 ) in real space with secondary structure and geometry restraints to prevent structure overfitting.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, MotionCor2, PyMOL, RELION v3.1]

### An unusual aromatase/cyclase programs the formation of the phenyldimethylanthrone framework in anthrabenzoxocinones and fasamycin. (PNAS 2024)

- DOI: 10.1073/pnas.2321722121 | PMCID: PMC10945814 | PMID: 38446858
- Evidence: The structure of Abx (+) D was determined by molecular replacement method using the program Phaser in the PHENIX package, with the atomic coordinates of 1TUW serving as the searching model.
- Full pipeline: stage not stated [PHENIX, PyMOL]

### TIFAB regulates the TIFA-TRAF6 signaling pathway involved in innate immunity by forming a heterodimer complex with TIFA. (PNAS 2024)

- DOI: 10.1073/pnas.2318794121 | PMCID: PMC10945758 | PMID: 38442163
- Evidence: The structure of TIFA/TIFAB was built and refined using COOT ( 30 ) and PHENIX ( 31 ).
- Full pipeline: quantification [ImageJ] -> structure determination [PHENIX] -> stage not stated [CCP4, PyMOL]

### Human paraneoplastic antigen Ma2 (PNMA2) forms icosahedral capsids that can be engineered for mRNA delivery. (PNAS 2024)

- DOI: 10.1073/pnas.2307812120 | PMCID: PMC10945824 | PMID: 38437549
- Evidence: The extra monomers were then deleted and the original monomer was duplicated with I4 symmetry and refined using PHENIX real_space_refine ( 55 ) into the I4-symmetric overall map using the starting model as a reference (sigma = 0.1), one macrocycle of global minimization and ADP refinement, and a nonbonded weight of 2,000.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, PyMOL, RELION v4.0, Topaz]

### Tertiary folds of the SL5 RNA from the 5' proximal region of SARS-CoV-2 and related coronaviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2320493121 | PMCID: PMC10927501 | PMID: 38427602
- Evidence: The stereochemical and map-to-model scores were calculated using the pipeline ( https://github.com/DasLab/CASP15_RNA_EM ), which includes using MolProbity ( 59 ), Phenix cross-correlation scores, CC volume , CC mask , and CC peaks ( 60 ), Q-score ( 42 ), and TEMPy for Mutual Information (MI) and segment-based Manders’ overlap coefficient (SMOC) scores ( 61 ).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [PHENIX]

### Structural basis for CFTR inhibition by CFTR<sub>inh</sub>-172. (PNAS 2024)

- DOI: 10.1073/pnas.2316675121 | PMCID: PMC10927578 | PMID: 38422021
- Evidence: CFTR inh -172 was built into the density and refined in PHENIX ( 61 ) using restraints generated by the Global Phasing web server ( grade.globalphasing.org ).
- Full pipeline: structure determination [PHENIX, RELION v3.1] -> stage not stated [MotionCor2]

### Sec7 regulatory domains scaffold autoinhibited and active conformations. (PNAS 2024)

- DOI: 10.1073/pnas.2318615121 | PMCID: PMC10927569 | PMID: 38416685
- Evidence: Atomic models and composite maps were generated, refined, and validated using Real Space Refine ( 64 ) and Phenix Combine Maps in Phenix ( 65 – 67 ).
- Full pipeline: alignment/mapping [cryoDRGN] -> structure determination [MotionCor2, PHENIX, RELION v3.1] -> stage not stated [AlphaFold, ChimeraX, ImageJ]

### The ALOG domain defines a family of plant-specific transcription factors acting during Arabidopsis flower development. (PNAS 2024)

- DOI: 10.1073/pnas.2310464121 | PMCID: PMC10927535 | PMID: 38412122
- Evidence: Model building was performed using Coot ( 66 ) and all refinements were carried out in Phenix ( 67 ).
- Full pipeline: quality control [FastQC v0.11.5, MultiQC v1.12] -> alignment/mapping [R v4.0.2] -> differential/statistical testing [DESeq2 v1.28.1, R v4.0.2] -> structure determination [PHENIX] -> stage not stated [Bioconductor, Bowtie2 v2.3.4.1, ColabFold, ggplot2 v3.3.5]

### The spindle protein CKAP2 regulates microtubule dynamics and ensures faithful chromosome segregation. (PNAS 2024)

- DOI: 10.1073/pnas.2318782121 | PMCID: PMC10907244 | PMID: 38381793
- Evidence: S1 B , cells were imaged on a spinning disk confocal Opera Phenix Plus High-Content Screening System containing a 63×/1.15 NA water objective.
- Full pipeline: stage not stated [Fiji, ImageJ, PHENIX]

### Dissection of the structure-function relationship of Na<sub>v</sub> channels. (PNAS 2024)

- DOI: 10.1073/pnas.2322899121 | PMCID: PMC10907234 | PMID: 38381792
- Evidence: Structural refinement was performed using phenix.real_space_refine application in PHENIX ( 48 ) with secondary structure and geometry restraints.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, MotionCor2]

### Diverse cytomegalovirus US11 antagonism and MHC-A evasion strategies reveal a tit-for-tat coevolutionary arms race in hominids. (PNAS 2024)

- DOI: 10.1073/pnas.2315985121 | PMCID: PMC10907249 | PMID: 38377192
- Evidence: One solution was identified, and sequential rounds of model refinement and model building were performed in PHENIX ( 71 ) and COOT ( 72 ), respectively, until convergence was reached.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4]

### Structure and function of the Si3 insertion integrated into the trigger loop/helix of cyanobacterial RNA polymerase. (PNAS 2024)

- DOI: 10.1073/pnas.2311480121 | PMCID: PMC10895346 | PMID: 38354263
- Evidence: With the anomalous signal from SeMet, the experimental phase (figure of merit: 0.273) was calculated using automated structure solution (AutoSol) in PHENIX ( 32 ).
- Full pipeline: stage not stated [AlphaFold, PHENIX]

### The structure of the <i>Caenorhabditis elegans</i> TMC-2 complex suggests roles of lipid-mediated subunit contacts in mechanosensory transduction. (PNAS 2024)

- DOI: 10.1073/pnas.2314096121 | PMCID: PMC10895266 | PMID: 38354260
- Evidence: The TMIE and CALM-1 subunits were then manually adjusted in Coot, followed by real-space refinement in Phenix.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, Coot, UCSF Chimera]

### Filament structure and subcellular organization of the bacterial intermediate filament-like protein crescentin. (PNAS 2024)

- DOI: 10.1073/pnas.2309984121 | PMCID: PMC10873595 | PMID: 38324567
- Evidence: The atomic coordinates were subsequently refined against the map in real space using Phenix ( 64 , 65 ), where secondary structure restraints were applied.
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [IMOD, PHENIX] -> machine learning [Topaz] -> stage not stated [Coot, ImageJ, MotionCor2, RELION v3.1]

### Molecular basis for human aquaporin inhibition. (PNAS 2024)

- DOI: 10.1073/pnas.2319682121 | PMCID: PMC10873552 | PMID: 38319972
- Evidence: The AQP7 cryo-EM model (PDB ID:8AMW) was fitted into the cryo-EM map in Chimera ( 22 ), after which the model was refined by real space refinement in Phenix ( 23 ) and edited manually using coot ( 24 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### Discovery of lirafugratinib (RLY-4008), a highly selective irreversible small-molecule inhibitor of FGFR2. (PNAS 2024)

- DOI: 10.1073/pnas.2317756121 | PMCID: PMC10861881 | PMID: 38300868
- Evidence: After iterative rounds of modeling and refining all protein components, the compound was modeled into composite omit maps, and the final model was refined in Phenix using ligand restraints generated in eLBOW.
- Full pipeline: structure determination [PHENIX]

### Structure of <i>Escherichia coli</i> exonuclease VII. (PNAS 2024)

- DOI: 10.1073/pnas.2319644121 | PMCID: PMC10835039 | PMID: 38271335
- Version used: **1.20.1**
- Evidence: A final round of real-space refinement of the model against the composite map was performed in Phenix (v.1.20.1) ( 41 ).
- Full pipeline: structure determination [AlphaFold, ChimeraX v1.4, PHENIX v1.20.1] -> stage not stated [Coot v0.9.6, UCSF Chimera v1.15]

### Increased expression of SSEA-4 on TKI-resistant non-small cell lung cancer with EGFR-T790M mutation. (PNAS 2024)

- DOI: 10.1073/pnas.2313397121 | PMCID: PMC10835044 | PMID: 38252815
- Evidence: ( E and F ) Opera Phenix Image of CL68 lung cancer cells stained with FICT-conjugated VK9 (green, targeting Globo-H) only or with a mixture of APC-conjugated MC813–70 (red, targeting SSEA-4) and FICT-conjugated VK9 in a 1:50 ratio.
- Full pipeline: stage not stated [PHENIX]

### Structure of saguaro cactus virus 3' translational enhancer mimics 5' cap for eIF4E binding. (PNAS 2024)

- DOI: 10.1073/pnas.2313677121 | PMCID: PMC10823258 | PMID: 38241435
- Evidence: The initial phases were obtained by molecular replacement with the previously reported structure of Fab BL3-6 (PDB code: 8DP3) ( 43 ) as the search model using Phaser on Phenix ( 54 ).
- Full pipeline: stage not stated [PHENIX]

### The structure of B-ARR reveals the molecular basis of transcriptional activation by cytokinin. (PNAS 2024)

- DOI: 10.1073/pnas.2319335121 | PMCID: PMC10801921 | PMID: 38198526
- Evidence: All of the models were manually built in Coot ( 61 ) and were refined by iterative rounds of manual adjustment with Coot and refinement with Phenix ( 62 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [BLAST]

### Structure of a tripartite protein complex that targets toxins to the type VII secretion system. (PNAS 2024)

- DOI: 10.1073/pnas.2312455121 | PMCID: PMC10801868 | PMID: 38194450
- Evidence: Coot was used to adjust the model manually to the electron density while computational structural refinement was performed with Phenix.refine until the R work and R free converged to 21.5% and 25.8%, respectively ( 49 , 50 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX]

### Elf1 promotes Rad26's interaction with lesion-arrested Pol II for transcription-coupled repair. (PNAS 2024)

- DOI: 10.1073/pnas.2314245121 | PMCID: PMC10801861 | PMID: 38194460
- Evidence: A selected model was refined using PHENIX real space refinement ( 51 ) with secondary structure restrains option followed by second round of Rosetta Relax, in which 10 models were generated.
- Full pipeline: structure determination [PHENIX, RELION, UCSF Chimera] -> visualisation [ChimeraX]

### Structural basis of σ<sup>54</sup> displacement and promoter escape in bacterial transcription. (PNAS 2024)

- DOI: 10.1073/pnas.2309670120 | PMCID: PMC10786286 | PMID: 38170755
- Evidence: All structural models were built using COOT ( 36 ) and refined using real-space refine in PHENIX ( 37 , 38 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [RELION v4.0, Topaz]

### Development of 2nd generation aminomethyl spectinomycins that overcome native efflux in <i>Mycobacterium</i> abscessus. (PNAS 2024)

- DOI: 10.1073/pnas.2314101120 | PMCID: PMC10786304 | PMID: 38165935
- Evidence: Initial molecular replacement solutions were refined by rigid-body refinement with the ribosome split into multiple domains, followed by positional and individual B-factor refinement using the PHENIX software (version 1.17).
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt, FastQC, MultiQC] -> alignment/mapping [Bowtie2, featureCounts] -> variant calling [VarScan] -> differential/statistical testing [DESeq2, R] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [CCP4, Coot v0.8.2]

### B56δ long-disordered arms form a dynamic PP2A regulation interface coupled with global allostery and Jordan's syndrome mutations. (PNAS 2024)

- DOI: 10.1073/pnas.2310727120 | PMCID: PMC10769853 | PMID: 38150499
- Evidence: The structural model was refined using the phenix.real_space_refine program in PHENIX ( 64 ) with secondary structure and geometry restraints.
- Full pipeline: quantification [ImageJ] -> simulation/modelling [GROMACS, PLUMED v2.8.0] -> structure determination [PHENIX]

### Protective human antibodies against a conserved epitope in pre- and postfusion influenza hemagglutinin. (PNAS 2024)

- DOI: 10.1073/pnas.2316964120 | PMCID: PMC10769852 | PMID: 38147556
- Evidence: Atomic models of B/MY04 EHA2 and S1V2-72 Fab were predicted with AF2 and fit to the cryoEM map with UCSF ChimeraX and Phenix.
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> stage not stated [AlphaFold, ChimeraX, PHENIX]

### Molecular mechanism of substrate transport by human peroxisomal ABCD3. (PNAS 2025)

- DOI: 10.1073/pnas.2513928122 | PMCID: PMC12772208 | PMID: 41428872
- Evidence: Real space refinement of the structures were performed in PHENIX to obtain the final model ( 43 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX]

### Structural insights into nonpeptide antagonist inhibition of somatostatin receptor subtype 5. (PNAS 2025)

- DOI: 10.1073/pnas.2522515122 | PMCID: PMC12745778 | PMID: 41417603
- Evidence: Models were fitted into the EM density maps using UCSF Chimera ( 37 ), then iteratively refined through manual adjustments in COOT ( 38 ) and automated rebuilding in PHENIX ( 39 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### Interprotomer communication and functional asymmetry in H/ACA snoRNPs. (PNAS 2025)

- DOI: 10.1073/pnas.2514683122 | PMCID: PMC12745780 | PMID: 41410763
- Evidence: Cryo-EM data were processed using Cryosparc and atomic models for the H/ACA subunits were generated using Alphafold2 refined using Phenix and edited using Coot.
- Full pipeline: structure determination [PHENIX]

### Structural insights into human signal peptide peptidase. (PNAS 2025)

- DOI: 10.1073/pnas.2528340122 | PMCID: PMC12745688 | PMID: 41405866
- Evidence: The restraint file for refinement was generated using PHENIX with secondary structure and geometry restraints ( 69 , 70 ).
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

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
- Version used: **1.20.1**
- Evidence: The initial model was rigid-body fit into the final volume in UCSF ChimeraX v1.6.1 ( 49 ), and automated fitting was done with real space refinement in PHENIX v1.20.1-4487, with rigid-body refinement, noncrystallographic symmetry constraints, gradient-driven minimization, and simulated annealing ( 50 , 51 ).
- Full pipeline: simulation/modelling [ChimeraX v1.6.1, PHENIX v1.20.1] -> structure determination [ChimeraX v1.6.1, PHENIX v1.20.1] -> stage not stated [Coot v0.9.8.8]

### Machine learning enables de novo multiepitope design of &lt;i&gt;Plasmodium falciparum&lt;/i&gt; circumsporozoite protein to target trimeric L9 antibody. (PNAS 2025)

- DOI: 10.1073/pnas.2512358122 | PMCID: PMC12704715 | PMID: 41337490
- Evidence: The model was docked into the M-TIM:L9 density map in Phenix and refined using Coot and Phenix refinement.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2023.2] -> structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX, PyMOL, RELION v5.0]

### Small siphophage binding to an open state of the LptDE outer membrane lipopolysaccharide translocon. (PNAS 2025)

- DOI: 10.1073/pnas.2516650122 | PMCID: PMC12685063 | PMID: 41296721
- Evidence: Rigid-body refinement was then performed in PHENIX ( 52 ).
- Full pipeline: alignment/mapping [PyMOL] -> quantification [ImageJ] -> simulation/modelling [GROMACS] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [Coot, MDAnalysis, MDTraj]

### Engineered calcium-regulated affinity protein for efficient internalization and lysosomal toxin delivery. (PNAS 2025)

- DOI: 10.1073/pnas.2509081122 | PMCID: PMC12685030 | PMID: 41289384
- Version used: **1.21.2**
- Evidence: ( 38 ) The AlphaFold 3 model was docked into the EM density map using Phenix (v1.21.2) ( 56 ) and the results were visualized by superposition in USCF ChimeraX (v1.9).
- Full pipeline: structure determination [ChimeraX v1.9, PHENIX v1.21.2] -> visualisation [ChimeraX v1.9, PHENIX v1.21.2] -> stage not stated [AlphaFold, NumPy, OpenCV, Python, SciPy, scikit-image]

### Inhibition of ice recrystallization with designed twistless helical repeat proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2514871122 | PMCID: PMC12685108 | PMID: 41289379
- Evidence: Structures were refined in Phenix ( 45 ).
- Full pipeline: alignment/mapping [PyMOL] -> normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ImageJ, RoseTTAFold]

### Mechanisms of transport and analgesic compounds recognition by glycine transporter 2. (PNAS 2025)

- DOI: 10.1073/pnas.2506722122 | PMCID: PMC12685064 | PMID: 41284875
- Evidence: The models for the ligands and their geometric constraints were generated via the elBOW module in PHENIX ( 92 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [PHENIX, VMD]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Evidence: The model was then subjected to iterative rounds of manual adjustment in Coot ( 65 ) and real-space refinement in Phenix ( 66 ).
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### Structural basis for Lamassu-based antiviral immunity and its evolution from DNA repair machinery. (PNAS 2025)

- DOI: 10.1073/pnas.2519643122 | PMCID: PMC12663957 | PMID: 41252147
- Evidence: Model building was performed using AlphaFold3 predictions, Coot, and Phenix real-space refinement.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX v1.9, UCSF Chimera] -> stage not stated [AlphaFold]

### Structure of the D1-Val185Asn mutated photosystem II complex with slow O-O bond formation reveals changes in the Cl1 water channel. (PNAS 2025)

- DOI: 10.1073/pnas.2522652122 | PMCID: PMC12663929 | PMID: 41237214
- Evidence: Automated refinement was performed in Phenix ( 49 ) version 1.19.2-4158 using real_space_refine ( 50 ) with NQH flips turned off and nonbonded weight set to 1,000.
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [ChimeraX]

### The mechanism of pathogenic α&lt;sub&gt;1&lt;/sub&gt;-antitrypsin aggregation in the human liver. (PNAS 2025)

- DOI: 10.1073/pnas.2507535122 | PMCID: PMC12646233 | PMID: 41231946
- Evidence: Data reduction, integration, scaling, and merging were performed using XDS ( 59 ) and Aimless ( 60 ); the structures were solved by molecular replacement using Phaser ( 61 ); model refinement was undertaken with Phenix ( 62 ); and model visualization and building were performed with Coot ( 58 ).
- Full pipeline: normalisation [PHENIX] -> registration [MotionCor2 v1.4, RELION v4.0] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX, PHENIX]

### Structure and encapsulation of carbonic anhydrase within the α-carboxysome. (PNAS 2025)

- DOI: 10.1073/pnas.2523723122 | PMCID: PMC12646314 | PMID: 41223214
- Evidence: Subsequent refinements of the model were performed iteratively with real-space refinement in Phenix ( 77 ) and adjusted in Coot.
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, Clustal Omega]

### Extracellular nanobody screening using conformationally stable GPCR variants. (PNAS 2025)

- DOI: 10.1073/pnas.2508879122 | PMCID: PMC12625997 | PMID: 41187083
- Evidence: Coordinates and chemical constraints for atropine and iperoxo were created using Phenix.elbow (1.20.1 to 4,487) ( 52 ).
- Full pipeline: structure determination [ChimeraX] -> stage not stated [AlphaFold, MACS2, PHENIX]

### Conformational regulation of two essential activators of bacterial cell elongation. (PNAS 2025)

- DOI: 10.1073/pnas.2514198122 | PMCID: PMC12625996 | PMID: 41183199
- Evidence: The structure was refined using real-space refinement in Phenix ( 52 , 53 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, Coot]

### From sequence to scaffold: Computational design of protein nanoparticle vaccines from AlphaFold2-predicted building blocks. (PNAS 2025)

- DOI: 10.1073/pnas.2409566122 | PMCID: PMC12626006 | PMID: 41183183
- Evidence: A final real-space refinement with grid searching, Ramachandran and rotamer restraints all turned off, and “use starting model as reference” turned on, was then performed in Phenix ( 82 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, RoseTTAFold]

### Neutron crystallography of the covalent intermediate of β-glucosidase reveals remodeling of the catalytic center. (PNAS 2025)

- DOI: 10.1073/pnas.2502828122 | PMCID: PMC12595480 | PMID: 41166426
- Version used: **1.19.2**
- Evidence: Joint XN refinement was performed using PHENIX 1.19.2_4158 ( 49 ) and Coot ( 50 ).
- Full pipeline: structure determination [PHENIX v1.19.2] -> visualisation [PyMOL]

### Glycosaminoglycans activate peptidylarginine deiminase 4 by enhancing calcium affinity. (PNAS 2025)

- DOI: 10.1073/pnas.2508369122 | PMCID: PMC12595441 | PMID: 41166417
- Evidence: Model fitting, refinement, and validation: The previously solved crystal structure of PAD4 (PDB ID: 3APN) was manually docked using UCSF ChimeraX ( 42 ), followed by the “Dock in Map” tool in Phenix ( 43 ).
- Full pipeline: structure determination [ChimeraX, PHENIX] -> visualisation [PyMOL]

### WrtF from &lt;i&gt;Rhizobium tropici&lt;/i&gt; CIAT 899 is a GT-A fold fucosyltransferase that binds its donor nonproductively. (PNAS 2025)

- DOI: 10.1073/pnas.2512460122 | PMCID: PMC12595478 | PMID: 41166418
- Evidence: All structures were determined through molecular replacement using Phaser ( 71 ) in Phenix using a truncated ColabFold model of WrtF.
- Full pipeline: structure determination [Coot] -> stage not stated [ColabFold, PHENIX]

### A cytoplasmic motif in HLA-E that drives clathrin-mediated endocytosis and VCP-associated postendocytic trafficking. (PNAS 2025)

- DOI: 10.1073/pnas.2514956122 | PMCID: PMC12582296 | PMID: 41134633
- Evidence: The plate was imaged on a high-content laser-based spinning disk confocal microscope (Opera Phenix Plus, Revvity), using a 60× water objective.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [STRING db] -> stage not stated [Cytoscape v3.10.1, PHENIX]

### Asymmetric gating of a homopentameric ion channel GLIC revealed by cryo-EM. (PNAS 2025)

- DOI: 10.1073/pnas.2512811122 | PMCID: PMC12582304 | PMID: 41129221
- Evidence: Real-space refinement was performed using the phenix.real_space_refine tool from the PHENIX package (v1.21rc1-4985) ( 86 ), with default settings, except for enabling full NCS constraints, refining NCS operators fully, and setting the “max reasonable bond distance” to 500.
- Full pipeline: alignment/mapping [Coot v0.9.8.7] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.9.8.7, PHENIX, RELION v4.0.1] -> stage not stated [ChimeraX]

### Protein disulfide isomerases regulate androgen receptor stability and promote prostate cancer cell growth and survival. (PNAS 2025)

- DOI: 10.1073/pnas.2509222122 | PMCID: PMC12557534 | PMID: 41086208
- Version used: **1.19.2**
- Evidence: The 2Fo-Fc density map was generated from the deposited structure factors using Phenix (version 1.19.2-4158-000) and visualized at an RMSD level of 1.0 Å and carve radius of 1.8 Å in PyMOL (version 3.1).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.8, FastQC] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2, R v3.4.1] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [Bioconductor, DESeq2, R v3.4.1] -> structure determination [PHENIX v1.19.2, PyMOL v3.1] -> visualisation [PHENIX v1.19.2, PyMOL v3.1] -> stage not stated [Seurat, featureCounts]

### Design principles of the common Gly-X6-Gly membrane protein building block. (PNAS 2025)

- DOI: 10.1073/pnas.2503134122 | PMCID: PMC12541321 | PMID: 41055983
- Evidence: The design model for molecular replacement in Phenix ( 68 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [AlphaFold, PHENIX]

### Structural insights into the dynamic mechanism of bornavirus polymerase. (PNAS 2025)

- DOI: 10.1073/pnas.2504779122 | PMCID: PMC12501175 | PMID: 40996804
- Evidence: Real-space refinements in Phenix-1.16 ( 62 ) were performed to obtain the final models.
- Full pipeline: registration [CTFFIND, MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.7, UCSF Chimera]

### Structural and functional analysis of the &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; MmpS5L5 efflux pump presages increased bedaquiline resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2516660122 | PMCID: PMC12501195 | PMID: 40986343
- Version used: **1.21.2**
- Evidence: Real-space refinement was performed using PHENIX (v.1.21.2) ( 75 ) using globally sharpened maps, with Ramachandran and secondary structure restraints enabled, followed by inspection and manual building in Coot.
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION] -> structure determination [PHENIX v1.21.2] -> stage not stated [AlphaFold, ChimeraX, Coot v0.9.8.93]

### In situ structures of the &lt;i&gt;Legionella&lt;/i&gt; Dot/Icm T4SS identify the DotA-IcmX complex as the gatekeeper for effector translocation. (PNAS 2025)

- DOI: 10.1073/pnas.2516300122 | PMCID: PMC12501162 | PMID: 40986344
- Version used: **1.21**
- Evidence: Model refinement was performed iteratively using Phenix 1.21 ( 57 ) to improve residue alignment with the density map.
- Full pipeline: alignment/mapping [PHENIX v1.21] -> structure determination [CTFFIND, ChimeraX, PHENIX v1.21] -> stage not stated [AlphaFold, Coot v0.8.9.1, IMOD, RELION v3.1]

### De novo design of potent inhibitors of clostridial family toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2509329122 | PMCID: PMC12501149 | PMID: 40982695
- Evidence: Phenix ( 54 ) was used to trim the model to polyA, before further refinement in Coot and Isolde.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL, seaborn] -> stage not stated [AlphaFold, ChimeraX, Topaz]

### Cryo-EM structure of the prohibitin complex in open conformation. (PNAS 2025)

- DOI: 10.1073/pnas.2512430122 | PMCID: PMC12478178 | PMID: 40966277
- Evidence: The refined coordinates were further refined in real space using PHENIX, applying secondary structure and geometric constraints ( 53 ).
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX]

### Structurally diverse viral inhibitors converge on a shared mechanism to stall the antigen transporter TAP. (PNAS 2025)

- DOI: 10.1073/pnas.2516676122 | PMCID: PMC12478189 | PMID: 40956880
- Evidence: The models were then docked into the density, iteratively edited and refined in Coot ( 71 ), ISOLDE ( 72 ), and PHENIX ( 73 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, RELION]

### How palytoxin transforms the Na&lt;sup&gt;+&lt;/sup&gt;,K&lt;sup&gt;+&lt;/sup&gt; pump into a cation channel. (PNAS 2025)

- DOI: 10.1073/pnas.2506450122 | PMCID: PMC12478176 | PMID: 40956884
- Evidence: The atomic models were refined with Phenix ( 48 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [RELION]

### Parametrically guided design of beta barrels and transmembrane nanopores using deep learning. (PNAS 2025)

- DOI: 10.1073/pnas.2425459122 | PMCID: PMC12478100 | PMID: 40953261
- Evidence: Structures were refined in Phenix ( 47 ).
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [AlphaFold, RoseTTAFold]

### A widespread family of molecular chaperones promotes the intracellular stability of type VIIb secretion system-exported toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2503581122 | PMCID: PMC12478183 | PMID: 40953262
- Evidence: Further refinement of all structures was performed using the Phenix.refine and Coot software.
- Full pipeline: alignment/mapping [MUSCLE v3.8.1551] -> structure determination [PHENIX] -> visualisation [IQ-TREE] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### Subtype-specific structural features of the hearing loss-associated human P2X2 receptor. (PNAS 2025)

- DOI: 10.1073/pnas.2417753122 | PMCID: PMC12452952 | PMID: 40938707
- Evidence: Models were subsequently built using Coot and real-space refinements were performed within PHENIX ( 77 , 78 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX]

### Structural basis for Rad54- and Hed1-mediated regulation of Rad51 during the transition from mitotic to meiotic recombination. (PNAS 2025)

- DOI: 10.1073/pnas.2510007122 | PMCID: PMC12452912 | PMID: 40932772
- Evidence: After initial rigid-body refinement in Phenix ( 86 ), amino acid residue sidechains were manually inspected and corrected for fitting into the density map using Coot ( 87 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold]

### Binding of &lt;i&gt;Fusobacterium nucleatum&lt;/i&gt; autotransporter adhesin CbpF to human CEACAM1 and CEACAM5: A Velcro model for bacterium adhesion. (PNAS 2025)

- DOI: 10.1073/pnas.2516574122 | PMCID: PMC12452904 | PMID: 40928870
- Evidence: The model was then manually refined in Coot 0.9.8.92 ( 60 ). and autorefined using Phenix-1.20.1 real space refine program ( 61 ).The stereochemical quality of all models was assessed using MolProbity of Phenix.
- Full pipeline: structure determination [ChimeraX, Coot v0.9.8.92, PHENIX, PyMOL] -> visualisation [PyMOL] -> stage not stated [CCP4, MotionCor2]

### Mechanisms underlying allosteric modulation of antiseizure medication binding to synaptic vesicle protein 2A (SV2A). (PNAS 2025)

- DOI: 10.1073/pnas.2510239122 | PMCID: PMC12435242 | PMID: 40892927
- Version used: **1.20.1**
- Evidence: SV2A (PDB: 8UO9) model was fit into cryo-EM density maps, which was manually modeled in Coot ( 53 , 54 ), iteratively real space refined in Phenix (version 1.20.1) ( 55 ), and validated by comparing the half maps and refined model.
- Full pipeline: differential/statistical testing [RELION v3.1] -> structure determination [Coot, PHENIX v1.20.1] -> stage not stated [AlphaFold]

### Structural insights into the substrate uptake and inhibition of the human creatine transporter (hCRT). (PNAS 2025)

- DOI: 10.1073/pnas.2426135122 | PMCID: PMC12435270 | PMID: 40892912
- Evidence: The main chain of the atomic model was refined using the real_space_refine module of PHENIX ( 70 ), incorporating secondary structure and geometric constraints to mitigate overfitting.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> visualisation [ChimeraX]

### Nucleotide- and metalloid-driven conformational changes in the arsenite efflux ATPase ArsA. (PNAS 2025)

- DOI: 10.1073/pnas.2506440122 | PMCID: PMC12415280 | PMID: 40880530
- Evidence: Model building and refinement were performed using Phenix ( 47 ) and Coot ( 48 ).
- Full pipeline: structure determination [AlphaFold, PHENIX]

### SHP2 genetic variants in NSML-associated RASopathies disrupt the PZR-IRX transcription factor signaling axis. (PNAS 2025)

- DOI: 10.1073/pnas.2503631122 | PMCID: PMC12415285 | PMID: 40854126
- Evidence: Initial model building was performed automatically in Phenix autobuild ( 56 ) which built and placed residues 6 to 153 and 179 to 197 from Shp-2, including the linker between N-SH2 and C-SH2 (residues 105 to 111) and the backbone of residues 166 to 176.
- Full pipeline: stage not stated [Coot, PHENIX]

### Broad neutralizing antibody response of a monomeric spike-based SARS-CoV-2 bivalent vaccine against diverse variants. (PNAS 2025)

- DOI: 10.1073/pnas.2503254122 | PMCID: PMC12415226 | PMID: 40854137
- Evidence: After a 48-h incubation at 37 °C, fluorescence imaging of the cells was conducted using an Opera Phenix high-content imaging system (PerkinElmer).
- Full pipeline: stage not stated [PHENIX]

### CryoEM structure of ALK2:BMP6 reveals distinct mechanism that allow ALK2 to interact with both BMP and activin ligands. (PNAS 2025)

- DOI: 10.1073/pnas.2502788122 | PMCID: PMC12415261 | PMID: 40854140
- Version used: **1.21**
- Evidence: Manual model building was conducted in Coot 0.9.6, and real space refinement of models was conducted using Phenix 1.21 ( 37 , 38 ).
- Full pipeline: structure determination [Coot v0.9.6, PHENIX v1.21] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### Identification of broadly inhibitory anti-PfEMP1 antibodies by mass spectrometry sequencing of plasma IgG from a malaria-exposed child. (PNAS 2025)

- DOI: 10.1073/pnas.2508744122 | PMCID: PMC12403141 | PMID: 40833410
- Version used: **1.21.5**
- Evidence: Full minimization refinement was performed using real-space refinement in PHENIX v1.21.5 ( 34 ).
- Full pipeline: structure determination [PHENIX v1.21.5] -> visualisation [ChimeraX]

### Aspartic acid residues in BBE-like enzymes from &lt;i&gt;Morus alba&lt;/i&gt; promote a function shift from oxidative cyclization to dehydrogenation. (PNAS 2025)

- DOI: 10.1073/pnas.2504346122 | PMCID: PMC12403149 | PMID: 40828030
- Evidence: The structure was solved using a molecular replacement method with Phaser, employing the MaDA3 structure (PDB ID 7E2V) as the search model, and refined with Coot and Phenix.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AutoDock Vina v1.1.2]

### Mechanistic insights into the small-molecule inhibition of influenza A virus entry. (PNAS 2025)

- DOI: 10.1073/pnas.2503899122 | PMCID: PMC12377760 | PMID: 40802690
- Evidence: ...tion Software cryoSPARC cryoSPARC Particles 155,278 195,885 Symmetry C3 C3 Box size (pix) 360 360 Resolution (Å) (FSC 0.143 ) * 2.77 2.76 Refinement (Phenix) † Protein residues 1470 1470 Chimera CC 0.9 0.9 Resolution (Å) (FSC 0.5 ) 3 2.9 EMRinger Score 3.62 3.94 R.m.s. deviations Bond lengths (Å) 0.003 0.003 Bond angles (°) 0.554 0.599 Validation MolProbity score 1.88 1.87 Clash score 4.52 4.3 Rot...
- Full pipeline: alignment/mapping [Clustal Omega] -> simulation/modelling [Coot] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL]

### Dural ectopic lymphatic structures accumulate during aging and exhibit dysregulation in neurodegenerative diseases. (PNAS 2025)

- DOI: 10.1073/pnas.2425081122 | PMCID: PMC12377736 | PMID: 40794835
- Evidence: Slides were scanned using The Opera Phenix® Plus High-Content Screening Confocal System by Revvity.
- Full pipeline: differential/statistical testing [R] -> visualisation [ggplot2] -> stage not stated [PHENIX]

### Structural insights into VRC01-class bnAb precursors with diverse light chains elicited in the IAVI G001 human vaccine trial. (PNAS 2025)

- DOI: 10.1073/pnas.2510163122 | PMCID: PMC12377726 | PMID: 40789024
- Evidence: Iterative model building and refinement were carried out using Coot and Phenix, respectively.
- Full pipeline: structure determination [PHENIX]

### Measuring the selective packaging of RNA molecules by viral coat proteins in cells. (PNAS 2025)

- DOI: 10.1073/pnas.2505190122 | PMCID: PMC12377776 | PMID: 40789029
- Evidence: Refinement was carried out using Phenix ( 71 ) and model adjustments were carried out in COOT ( 72 ).
- Full pipeline: read trimming [fastp v0.23.2] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1] -> structure determination [PHENIX]

### Critical role of extracellular loops in differential modulations of TTX-sensitive and TTX-resistant Na&lt;sub&gt;v&lt;/sub&gt; channels. (PNAS 2025)

- DOI: 10.1073/pnas.2510355122 | PMCID: PMC12358880 | PMID: 40768348
- Evidence: Structure refinement was performed using phenix.real_space_refine application in PHENIX ( 63 ) real space with secondary structure and geometry restraints.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [CTFFIND, PyMOL, RELION]

### The bacterial ESCRT-III PspA rods thin lipid tubules and increase membrane curvature through helix α0 interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2506286122 | PMCID: PMC12358876 | PMID: 40758888
- Evidence: The 3D reconstructions were B-factor sharpened in Phenix ( phenix.auto-sharpen ) ( 77 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [ChimeraX]

### Protective antigen-mediated delivery of an anti-CRISPR protein for precision genome editing. (PNAS 2025)

- DOI: 10.1073/pnas.2426960122 | PMCID: PMC12358904 | PMID: 40758882
- Evidence: After 48 h, live cells were stained with 2 µg/mL Hoechst 33342 (37 °C, 20 min) in FluoroBrite DMEM (Gibco, A1896701) and imaged using high-throughput confocal microscopy (Revvity Opera Phenix; 20× objective, 488 and 561 nm excitation for fluorescence, transmitted light for digital phase contrast).
- Full pipeline: stage not stated [PHENIX]

### Structural basis for anaerobic alkane activation by a multisubunit glycyl radical enzyme. (PNAS 2025)

- DOI: 10.1073/pnas.2510389122 | PMCID: PMC12358834 | PMID: 40758891
- Evidence: Iterative rounds of model building and refinement of MASSα 2 γ 2 were done using Coot ( 52 ) and Phenix Real Space Refine ( 53 ), respectively.
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [RELION v3.1]

### In situ cryo-ET visualization of mitochondrial depolarization and mitophagic engulfment. (PNAS 2025)

- DOI: 10.1073/pnas.2511890122 | PMCID: PMC12337332 | PMID: 40743392
- Evidence: To build models that fit the EM density maps for each class, AlphaFold3 was used to generate an initial protein model of 12 prohibitin 1-2 dimers which was then relaxed into either EM density map using ISOLDE ( https://isolde.cimr.cam.ac.uk/ ), (RRID:SCR_025577) ( 54 ) and PHENIX ( https://phenix-online.org/ ), (RRID:SCR_014224) ( 55 ).
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX, RELION, napari]

### Generation of actionable, cancer-specific neoantigens from KRAS(G12C) with adagrasib. (PNAS 2025)

- DOI: 10.1073/pnas.2509012122 | PMCID: PMC12337345 | PMID: 40737322
- Version used: **1.18.2**
- Evidence: Atomic models were built using Coot ( 33 ) and Phenix 1.18.2 software ( 34 ).
- Full pipeline: structure determination [UCSF Chimera] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2 v1.5, PHENIX v1.18.2, Python]

### Tat-dependent bundling pilus of a halophilic archaeon assembles by a strand donation mechanism and facilitates biofilm formation. (PNAS 2025)

- DOI: 10.1073/pnas.2514980122 | PMCID: PMC12337348 | PMID: 40737320
- Evidence: This initial model was further refined through several iterative rounds of model adjustment using COOT ( 60 ), followed by automated real-space refinement in Phenix ( 61 ).
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [AlphaFold, ChimeraX, PHENIX]

### Cryo-EM structure and polar assembly of the PS2 S-layer of &lt;i&gt;Corynebacterium glutamicum&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2426928122 | PMCID: PMC12337289 | PMID: 40729392
- Evidence: A final round of refinement was performed using Phenix ( 66 ), and figures were generated using ChimeraX ( 67 ).
- Full pipeline: structure determination [ChimeraX, PHENIX] -> visualisation [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Coot]

### How RAG1/2 evolved from ancestral transposases to initiate V(D)J recombination without transposition. (PNAS 2025)

- DOI: 10.1073/pnas.2512362122 | PMCID: PMC12337333 | PMID: 40729386
- Evidence: Phenix real-space refinement was used to refine the models.
- Full pipeline: structure determination [PHENIX]

### Structural basis of auxin binding and transport by <i>Arabidopsis thaliana</i> AUX1. (PNAS 2025)

- DOI: 10.1073/pnas.2513424122 | PMCID: PMC12337342 | PMID: 40720658
- Evidence: The model was further improved through iterative manual adjustments in Coot, followed by real_space_refinement in Phenix ( 52 , 53 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [OpenMM, VMD] -> structure determination [PHENIX] -> machine learning [OpenMM] -> visualisation [VMD] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, Coot]

### Combining MicroED and native mass spectrometry for structural discovery of enzyme-small molecule complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2503780122 | PMCID: PMC12337315 | PMID: 40720654
- Evidence: Structure refinement was performed in PHENIX ( 53 ) by the following strategy: Reference model restraints from the original search model from the PDB were applied, while three cycles of refinement of XYZ coordinates in real and reciprocal space, group B-factors, and occupancies were performed.
- Full pipeline: structure determination [PHENIX]

### Structure reveals a regulation mechanism of plant outward-rectifying K&lt;sup&gt;+&lt;/sup&gt; channel GORK by structural rearrangements in the CNBD-Ankyrin bridge. (PNAS 2025)

- DOI: 10.1073/pnas.2500070122 | PMCID: PMC12318183 | PMID: 40699930
- Evidence: The model was subjected to iterative manual rebuilding using Coot software and real-space refinement with the use of PHENIX.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, PyMOL, UCSF Chimera, VMD]

### A multifunctional anti-O-Antigen human monoclonal antibody protects against &lt;i&gt;Shigella sonnei&lt;/i&gt; infection in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2426211122 | PMCID: PMC12318208 | PMID: 40699929
- Evidence: Images were taken by the Opera Phenix confocal microscope at the different time points (in minutes) indicated in the figure.
- Full pipeline: stage not stated [PHENIX]

### An electron-bifurcating "plug" to a protein nanowire in tungsten-dependent aldehyde detoxification. (PNAS 2025)

- DOI: 10.1073/pnas.2501900122 | PMCID: PMC12318220 | PMID: 40694326
- Evidence: All atomic models were then manually rebuilt or refined with the program COOT ( 48 ) followed by real-space refinement in the PHENIX program ( 49 ).
- Full pipeline: structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [ChimeraX]

### Neutron and time-resolved X-ray crystallography reveal the substrate recognition and catalytic mechanism of human Nudix hydrolase MTH1. (PNAS 2025)

- DOI: 10.1073/pnas.2510085122 | PMCID: PMC12305053 | PMID: 40674425
- Evidence: NX refinement was performed using PHENIX and COOT ( 35 , 48 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [PyMOL]

### Structures of &lt;i&gt;Chaetomium thermophilum&lt;/i&gt; TOM complexes with bound preproteins. (PNAS 2025)

- DOI: 10.1073/pnas.2507279122 | PMCID: PMC12305020 | PMID: 40674418
- Evidence: Finally, all models were globally refined in Phenix with global minimization and B-factor (ADP) refinement ( 56 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2, RELION v3.0]

### De novo design of a fusion protein tool for GPCR research. (PNAS 2025)

- DOI: 10.1073/pnas.2422360122 | PMCID: PMC12304938 | PMID: 40658860
- Evidence: Phenix.elbow (1.20.1-4487) was used to generate the coordinates and chemical constraints for atropine, PD168368 , and balovaptan ( 34 ).
- Full pipeline: stage not stated [AlphaFold, ChimeraX, PHENIX]

### Structural basis of the inhibition of TRPV1 by analgesic sesquiterpenes. (PNAS 2025)

- DOI: 10.1073/pnas.2506560122 | PMCID: PMC12305030 | PMID: 40663614
- Evidence: The resulting model was real-space refined in Phenix ( 77 ) and visualized using UCSF Chimera, UCSF ChimeraX, and Pymol ( 78 ).
- Full pipeline: simulation/modelling [NAMD v2.14] -> structure determination [PHENIX, Topaz] -> visualisation [ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [Coot]

### Microscopic and structural observations of actin filament capping and severing by cytochalasin D. (PNAS 2025)

- DOI: 10.1073/pnas.2502164122 | PMCID: PMC12304888 | PMID: 40658853
- Evidence: Restrained refinement was performed with Refmac5 ( 60 ) and Phenix_refine ( 61 ), and model inspection was carried out using Coot ( 35 ).
- Full pipeline: simulation/modelling [GROMACS v2023.1] -> structure determination [PHENIX] -> machine learning [PHENIX] -> visualisation [PyMOL] -> stage not stated [Coot, ImageJ]

### The prefusion structure of the HERV-K (HML-2) Env spike complex. (PNAS 2025)

- DOI: 10.1073/pnas.2505505122 | PMCID: PMC12280955 | PMID: 40632556
- Evidence: This model was then manually completed and refined using Coot ( 52 ) and real-space refinement in Phenix ( 53 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX, PyMOL]

### Molecular basis for substrate recognition and transport of mammalian taurine transporters. (PNAS 2025)

- DOI: 10.1073/pnas.2425549122 | PMCID: PMC12260568 | PMID: 40601627
- Evidence: Real-space model refinement ( 54 ) and validation ( 55 ) were performed in Phenix.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PyMOL, RELION]

### De novo design of D-peptide ligands: Application to influenza virus hemagglutinin. (PNAS 2025)

- DOI: 10.1073/pnas.2426554122 | PMCID: PMC12232713 | PMID: 40577121
- Evidence: Refinement was carried out in Phenix ( 53 ), alternating with manual rebuilding and adjustment in COOT ( 54 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [GROMACS]

### Crystal structure and catalytic mechanism of drimenol synthase, an unusual bifunctional terpene cyclase-phosphatase. (PNAS 2025)

- DOI: 10.1073/pnas.2506584122 | PMCID: PMC12232559 | PMID: 40569382
- Evidence: The dataset from condition 1 was phased using molecular replacement with the PHASER module of PHENIX ( 54 , 55 ), and an AlphaFold 3-predicted ( 51 ) structure of AsDMS was used as the search model.
- Full pipeline: stage not stated [AlphaFold, PHENIX]

### Structural mechanism for the recognition of E2F1 by the ubiquitin ligase adaptor Cyclin F. (PNAS 2025)

- DOI: 10.1073/pnas.2501057122 | PMCID: PMC12232547 | PMID: 40549918
- Version used: **1.20.1**
- Evidence: Further modeling, coordinate refinement, and energy minimization were performed using Coot v0.9.4 and Phenix v.
- Full pipeline: structure determination [PHENIX v1.20.1] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, ChimeraX v1.8]

### Structure of the virulence-associated &lt;i&gt;Neisseria meningitidis&lt;/i&gt; filamentous bacteriophage MDAΦ. (PNAS 2025)

- DOI: 10.1073/pnas.2420157122 | PMCID: PMC12207478 | PMID: 40540604
- Evidence: Refinement was initially performed in PHENIX ( 45 ) and then in Servalcat ( 46 ) using Servalcat’s helical refinement pipeline.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION, Topaz]

### Cryo-EM structures of GnRHR: Foundations for next-generation therapeutics. (PNAS 2025)

- DOI: 10.1073/pnas.2500112122 | PMCID: PMC12207466 | PMID: 40523184
- Evidence: Real-space refinements were performed using Phenix programs ( 53 ).
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> visualisation [PyMOL]

### A distinct LHCI arrangement is recruited to photosystem I in Fe-starved green algae. (PNAS 2025)

- DOI: 10.1073/pnas.2500621122 | PMCID: PMC12207447 | PMID: 40523173
- Version used: **1.21.1**
- Evidence: The atomic models for the PSI structures were built by fitting the existing structure of D. salina (PDB identifier 6SL5) ( 20 ) as a template using PHENIX v.1.21.1 dock in map and subsequently refined with PHENIX real-space refinement ( 68 ).
- Full pipeline: alignment/mapping [RELION v3.0] -> structure determination [PHENIX v1.21.1] -> visualisation [ChimeraX v1.7.1] -> stage not stated [AlphaFold]

### Targeting ryanodine receptors with allopurinol and xanthine derivatives for the treatment of cardiac and musculoskeletal weakness disorders. (PNAS 2025)

- DOI: 10.1073/pnas.2422082122 | PMCID: PMC12184490 | PMID: 40512792
- Evidence: Model fittings and model building were performed in Coot ( 39 ), and final models were refined with Phenix tool RealSpaceRefine ( 40 ).
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [Topaz] -> stage not stated [ChimeraX]

### Pathogenic variants in the polycystin pore helix cause distinct forms of channel dysfunction. (PNAS 2025)

- DOI: 10.1073/pnas.2421362122 | PMCID: PMC12184499 | PMID: 40504156
- Evidence: AlphaFold2 models (PKD2 residues 180-925) containing the variant of interest were pruned in PHENIX ( 57 ) to remove low-confidence residues.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, ImageJ, PHENIX]

### Structural basis of the catalytic and allosteric mechanism of bacterial acetyltransferase PatZ. (PNAS 2025)

- DOI: 10.1073/pnas.2419096122 | PMCID: PMC12184503 | PMID: 40498448
- Evidence: Manual model fitting was performed using the Coot program, followed by model refinement through Real-space refinement in Phenix.
- Full pipeline: alignment/mapping [ChimeraX, IQ-TREE, Kraken2] -> structure determination [ChimeraX, PHENIX] -> visualisation [Kraken2] -> stage not stated [AlphaFold]

### Molecular basis for ligand recognition and receptor activation of the prostaglandin D2 receptor DP1. (PNAS 2025)

- DOI: 10.1073/pnas.2501902122 | PMCID: PMC12146711 | PMID: 40440061
- Evidence: All models were initially fitted into the EM density map using UCSF Chimera ( 43 ), followed by iterative rounds of manual adjustment and automated rebuilding in COOT ( 44 ) and PHENIX ( 45 ), respectively.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, R v3.50]

### Cocrystal structure reveals the mechanism of FSP1 inhibition by FSEN1. (PNAS 2025)

- DOI: 10.1073/pnas.2505197122 | PMCID: PMC12146761 | PMID: 40440064
- Evidence: Model building and crystallographic refinement were carried out using COOT and PHENIX software packages ( 34 , 35 ).
- Full pipeline: structure determination [PHENIX]

### Engineering a protease-stable, oral single-domain antibody to inhibit IL-23 signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2501635122 | PMCID: PMC12146698 | PMID: 40434646
- Evidence: The model was built in COOT ( 44 ) and subsequently refined with PHENIX ( 45 ) and REFMAC ( 46 ) to final statistics presented in SI Appendix , Table S2 .
- Full pipeline: differential/statistical testing [PHENIX, REFMAC] -> structure determination [PHENIX, REFMAC]

### Cross-reactive sarbecovirus antibodies induced by mosaic RBD nanoparticles. (PNAS 2025)

- DOI: 10.1073/pnas.2501637122 | PMCID: PMC12130868 | PMID: 40402246
- Evidence: The model was refined in Phenix ( 93 ) using real space refinement and the amino acid sequences for the mAbs were manually corrected in Coot ( 94 ).
- Full pipeline: structure determination [Coot, PHENIX, UCSF Chimera]

### Nonenzymatic RNA copying with a potentially primordial genetic alphabet. (PNAS 2025)

- DOI: 10.1073/pnas.2505720122 | PMCID: PMC12130883 | PMID: 40397670
- Evidence: All structures were refined by Phenix ( 52 ) and Refmac in CCP4i ( 53 ).
- Full pipeline: structure determination [Coot, PHENIX]

### MTA-cooperative PRMT5 inhibitors from cofactor-directed DNA-encoded library screens. (PNAS 2025)

- DOI: 10.1073/pnas.2425052122 | PMCID: PMC12107103 | PMID: 40377999
- Evidence: The structures were refined using Phenix ( 41 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4]

### Molecular insights into human phosphatidylserine synthase 2 and its regulation of SREBP pathways. (PNAS 2025)

- DOI: 10.1073/pnas.2501177122 | PMCID: PMC12107096 | PMID: 40372437
- Evidence: The models were refined in real space using PHENIX ( 22 ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [NAMD, VMD] -> structure determination [AlphaFold, PHENIX] -> visualisation [ChimeraX, PyMOL]

### Structure and evolution of photosystem I in the early-branching cyanobacterium &lt;i&gt;Anthocerotibacter panamensis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2427090122 | PMCID: PMC12107172 | PMID: 40366692
- Evidence: Automated refinement was performed using real_space_refine ( 64 ) in Phenix ( 65 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [IQ-TREE v2.2, RELION v3.1, UCSF Chimera]

### Structural insights into the activation of the human prostaglandin E&lt;sub&gt;2&lt;/sub&gt; receptor EP1 subtype by prostaglandin E&lt;sub&gt;2&lt;/sub&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2423840122 | PMCID: PMC12107139 | PMID: 40366695
- Evidence: The model was modified in Coot ( 49 ), followed by adjustments in ISOLDE ( 50 ), and then refined using PHENIX ( 51 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, R v7.40, Topaz]

### Electric field-induced pore constriction in the human K&lt;sub&gt;v&lt;/sub&gt;2.1 channel. (PNAS 2025)

- DOI: 10.1073/pnas.2426744122 | PMCID: PMC12107148 | PMID: 40366685
- Evidence: The model was edited and refined using the ISOLDE ( 67 ) plugin in ChimeraX v1.5 ( 68 ) or WinCoot v0.98.1 ( 69 ) followed by real-space refinement in Phenix ( 70 ).
- Full pipeline: structure determination [ChimeraX v1.5, PHENIX, PyMOL] -> stage not stated [AlphaFold, RELION]

### Mitochondria regulate MR1 protein expression and produce self-metabolites that activate MR1-restricted T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2418525122 | PMCID: PMC12107159 | PMID: 40354545
- Evidence: Diffraction data were processed using XDS ( 64 ) and programs from the CCP4 suite ( 65 ) and Phenix package ( 66 ).
- Full pipeline: stage not stated [CCP4, PHENIX, PyMOL]

### Architecture of &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt; glutamyl-tRNA synthetase defines a subfamily of dimeric class Ib aminoacyl-tRNA synthetases. (PNAS 2025)

- DOI: 10.1073/pnas.2504757122 | PMCID: PMC12088422 | PMID: 40343997
- Evidence: Manual model building, automated structural refinement, and model validation were performed using Coot ( 108 ), PHENIX ( 109 ), and MolProbity ( 110 ), respectively.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX]

### Structure of the human TWIK-2 potassium channel and its inhibition by pimozide. (PNAS 2025)

- DOI: 10.1073/pnas.2425709122 | PMCID: PMC12088453 | PMID: 40343992
- Evidence: Atomic models were built de novo, refined in real space using COOT ( 87 ), and further refined in real-space using PHENIX ( 88 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.1]

### Structural insights into the ubiquitin-independent midnolin-proteasome pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2505345122 | PMCID: PMC12088389 | PMID: 40339123
- Evidence: Structure refinement was carried out in real space with PHENIX.real_space_refine ( 44 ) with global minimization applied with noncrystallographic symmetry (NCS), rotamer, and Ramachandran constraints.
- Full pipeline: alignment/mapping [ChimeraX] -> quantification [ImageJ] -> structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, Coot]

### Molecular insights into de novo small-molecule recognition by an intron RNA structure. (PNAS 2025)

- DOI: 10.1073/pnas.2502425122 | PMCID: PMC12088405 | PMID: 40339124
- Version used: **1.20.1**
- Evidence: For visualization, final maps were autosharpened with Phenix 1.20.1 ( 57 , 58 ) and displayed using PyMOL 2.5.4 and UCSF Chimera ( 59 , 60 ).
- Full pipeline: visualisation [ChimeraX, PHENIX v1.20.1, PyMOL v2.5.4, UCSF Chimera]

### Mechanism and application of thiol-disulfide redox biosensors with a fluorescence-lifetime readout. (PNAS 2025)

- DOI: 10.1073/pnas.2503978122 | PMCID: PMC12088395 | PMID: 40327692
- Evidence: In all cases, refinement was performed using iterative cycles of automated refinement in Phenix and manual model building in Coot ( 71 , 72 ).
- Full pipeline: structure determination [Coot, PHENIX]

### Activity and structure of human (d)CTP deaminase CDADC1. (PNAS 2025)

- DOI: 10.1073/pnas.2424245122 | PMCID: PMC12088426 | PMID: 40324085
- Version used: **1.20.1**
- Evidence: Phenix 1.20.1 was used for automated real-space refinement ( 41 ).
- Full pipeline: structure determination [PHENIX v1.20.1] -> stage not stated [AlphaFold, ChimeraX v1.4]

### Water-directed pinning is key to tau prion formation. (PNAS 2025)

- DOI: 10.1073/pnas.2421391122 | PMCID: PMC12067210 | PMID: 40294272
- Evidence: Coot and Phenix were used for model building ( 77 – 79 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [PHENIX, RELION]

### Mechanism of read-through enhancement by aminoglycosides and mefloquine. (PNAS 2025)

- DOI: 10.1073/pnas.2420261122 | PMCID: PMC12054815 | PMID: 40273100
- Evidence: The structures were determined by molecular replacement using the deposited 80S ribosome structure (PDB ID: 7PZY) as a search model and then subjected to refinement using Phenix.refine ( 62 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, PyMOL v1.5]

### Structural basis of excitatory amino acid transporter 3 substrate recognition. (PNAS 2025)

- DOI: 10.1073/pnas.2501627122 | PMCID: PMC12036983 | PMID: 40249774
- Evidence: The models were manually adjusted in COOT ( 79 ) and subjected to real-space refinement in Phenix ( 80 ).
- Full pipeline: alignment/mapping [RELION] -> structure determination [ChimeraX, PHENIX]

### Virion-associated influenza hemagglutinin clusters upon sialic acid binding visualized by cryoelectron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2426427122 | PMCID: PMC12037027 | PMID: 40244672
- Evidence: Postrigid body fitting, real space refinement was conducted using the Phenix software package ( 24 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UCSF Chimera] -> structure determination [PHENIX] -> machine learning [EMAN2] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Matplotlib, Python, RELION, seaborn]

### Cryo-EM structure of the conjugation H-pilus reveals the cyclic nature of the TrhA pilin. (PNAS 2025)

- DOI: 10.1073/pnas.2427228122 | PMCID: PMC12037004 | PMID: 40244678
- Evidence: Ab initio model building and real space refinement were performed in PHENIX ( 40 , 41 ).
- Full pipeline: structure determination [PHENIX]

### The Q226L mutation can convert a highly pathogenic H5 2.3.4.4e virus to bind human-type receptors. (PNAS 2025)

- DOI: 10.1073/pnas.2419800122 | PMCID: PMC12036971 | PMID: 40232794
- Evidence: Model building and refinement were carried out by Coot and Phenix ( 78 , 79 ) ( SI Appendix , Table S1 ) and validated by MolProbity ( 80 ).
- Full pipeline: structure determination [PHENIX]

### NAL1 forms a molecular cage to regulate FZP phase separation. (PNAS 2025)

- DOI: 10.1073/pnas.2419961122 | PMCID: PMC12012508 | PMID: 40203040
- Evidence: The model was then manually built with Coot and refined with Phenix ( 39 , 40 ).
- Full pipeline: structure determination [PHENIX, RELION v3.1] -> stage not stated [AlphaFold]

### Structure of a Gcn2 dimer in complex with the large 60S ribosomal subunit. (PNAS 2025)

- DOI: 10.1073/pnas.2415807122 | PMCID: PMC12012509 | PMID: 40198700
- Evidence: The final model was validated using Phenix ( 86 ).
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [ChimeraX, Coot, PHENIX, RELION v4.0.1]

### Structural and functional characterization of the brain-specific dynamin superfamily member RNF112. (PNAS 2025)

- DOI: 10.1073/pnas.2419449122 | PMCID: PMC12012479 | PMID: 40198702
- Evidence: Initial models were built with COOT ( 63 ) and refined with PHENIX ( 64 ).
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [ImageJ, PyMOL]

### Structural basis for immune cell binding of &lt;i&gt;Fusobacterium nucleatum&lt;/i&gt; via the trimeric autotransporter adhesin CbpF. (PNAS 2025)

- DOI: 10.1073/pnas.2418155122 | PMCID: PMC12012533 | PMID: 40198705
- Evidence: The latter parts were removed and the model was then manually adjusted in Coot (WinCoot version 0.9.8.7) ( 54 ), followed by real-space refinement in PHENIX ( 55 ).
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot v0.9.8.7, PHENIX] -> visualisation [R] -> stage not stated [AlphaFold, Fiji, ImageJ, UCSF Chimera]

### Structural basis of the cysteinyl leukotriene receptor type 2 activation by LTD4. (PNAS 2025)

- DOI: 10.1073/pnas.2417148122 | PMCID: PMC12012480 | PMID: 40193607
- Evidence: The model was extensively modified using COOT ( 47 ) and PHENIX ( 48 ).
- Full pipeline: visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v4.0, MotionCor2, PHENIX, R v3.50, UCSF Chimera]

### DNA bending mediated by ORC is essential for replication licensing in budding yeast. (PNAS 2025)

- DOI: 10.1073/pnas.2502277122 | PMCID: PMC12002289 | PMID: 40184174
- Evidence: After removal of extra residues that do not fit the observed densities and manual adjustments in Coot ( 63 ), the models were refined against the corresponding cryo-EM density maps with phenix.real_space_refine module in PHENIX package ( 64 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [EMAN2, ImageJ, MotionCor2, RELION]

### The cryo-EM structure and physical basis for anesthetic inhibition of the THIK1 K2P channel. (PNAS 2025)

- DOI: 10.1073/pnas.2421654122 | PMCID: PMC12002230 | PMID: 40178898
- Evidence: Following manual building, global real space refinement with stereochemistry restraints was performed in Phenix ( 61 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, RELION v3.1.2]

### Structural basis for neutralizing antibody binding to pertussis toxin. (PNAS 2025)

- DOI: 10.1073/pnas.2419457122 | PMCID: PMC12002313 | PMID: 40172968
- Evidence: Model building and refinement were performed in Coot, Phenix, and ISOLDE.
- Full pipeline: structure determination [Coot, PHENIX]

### Cryo-EM structure of cyanopodophage A4 reveals a pentameric pre-ejectosome in the double-stabilized capsid. (PNAS 2025)

- DOI: 10.1073/pnas.2423403122 | PMCID: PMC12002296 | PMID: 40163721
- Evidence: Afterward, the models were manually adjusted and rebuilt by COOT ( 63 ) followed by the automatic refinement using the real-space refinement in PHENIX ( 64 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Cholesterol-dependent enzyme activity of human TSPO1. (PNAS 2025)

- DOI: 10.1073/pnas.2323045122 | PMCID: PMC12002307 | PMID: 40146857
- Version used: **1.16**
- Evidence: The structure was refined with Phenix version 1.16-3549 ( 58 ).
- Full pipeline: structure determination [PHENIX v1.16]

### Structure of ATP synthase from an early photosynthetic bacterium &lt;i&gt;Chloroflexus aurantiacus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2425824122 | PMCID: PMC12002316 | PMID: 40131952
- Evidence: Then real-space refinement in PHENIX ( 80 ) was used for model refinement, using the Ramachandran restraints followed by manual rebuilding in Coot.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL]

### &lt;i&gt;Chlamydomonas&lt;/i&gt; FBB18 is a ubiquitin-like protein essential for the cytoplasmic preassembly of various ciliary dyneins. (PNAS 2025)

- DOI: 10.1073/pnas.2423948122 | PMCID: PMC11962417 | PMID: 40106351
- Evidence: S2 C and D ) was determined by single-wavelength anomalous dispersion using AutoSol in the PHENIX software ( 60 , 61 ).
- Full pipeline: stage not stated [AlphaFold, PHENIX, PyMOL]

### Cryo-EM structures reveal the acetylation process of piccolo NuA4. (PNAS 2025)

- DOI: 10.1073/pnas.2414490122 | PMCID: PMC11962513 | PMID: 40100634
- Evidence: The structures were then refined in Phenix ( 69 ) for one round of real space refinement with secondary structure restraints.
- Full pipeline: alignment/mapping [RELION v4.0] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [AlphaFold, Coot]

### A splendid molecular factory: De- and reconstruction of the mammalian respiratory chain. (PNAS 2025)

- DOI: 10.1073/pnas.2416162122 | PMCID: PMC11962478 | PMID: 40100632
- Evidence: The PHENIX ( 42 ) software was used to dock the reference structure in the map, and real-space refinement cycles were conducted until the minimum number of validation errors was found.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, Topaz]

### A family of bacterial actin homologs forms a three-stranded tubular structure. (PNAS 2025)

- DOI: 10.1073/pnas.2500913122 | PMCID: PMC11929497 | PMID: 40073056
- Evidence: An initial atomic model of BeeR was generated with AlphaFold and refined in Phenix.
- Full pipeline: structure determination [AlphaFold, PHENIX]

### Epitope-directed selection of GPCR nanobody ligands with evolvable function. (PNAS 2025)

- DOI: 10.1073/pnas.2423931122 | PMCID: PMC11929449 | PMID: 40067891
- Evidence: A model of the complex was built in Coot and refined with Phenix real-space refinement ( 40 , 41 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [MACS2]

### Structural mechanisms underlying the modulation of CXCR4 by diverse small-molecule antagonists. (PNAS 2025)

- DOI: 10.1073/pnas.2425795122 | PMCID: PMC11929458 | PMID: 40063796
- Evidence: The structure of the complexes was then manually adjusted in Coot and refined in Phenix ( 42 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> stage not stated [RELION v5.0]

### State-dependent motion of a genetically encoded fluorescent biosensor. (PNAS 2025)

- DOI: 10.1073/pnas.2426324122 | PMCID: PMC11912384 | PMID: 40048274
- Evidence: Model building was performed in Coot, and the associated structures were refined in Phenix ( 49 , 50 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [AlphaFold] -> stage not stated [CCP4]

### Structural basis of DNA replication fidelity of the Mpox virus. (PNAS 2025)

- DOI: 10.1073/pnas.2411686122 | PMCID: PMC11912389 | PMID: 40035768
- Evidence: The initial coordinates were refined in real space using PHENIX ( 52 ) with the application of secondary structural restraints, distance and dihedral restraints, and Ramachandran restraints.
- Full pipeline: structure determination [PHENIX, RELION] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2 v1.2.4]

### MUC5AC filaments illuminate the structural diversification of respiratory and intestinal mucins. (PNAS 2025)

- DOI: 10.1073/pnas.2419717122 | PMCID: PMC11912381 | PMID: 40035770
- Evidence: Refinement was performed using Phenix ( 44 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX v1.3, PLINK v1.9, PyMOL]

### Structural basis of SARS-CoV-2 polymerase inhibition by nonnucleoside inhibitor HeE1-2Tyr. (PNAS 2025)

- DOI: 10.1073/pnas.2419854122 | PMCID: PMC11912441 | PMID: 40035759
- Evidence: Restraints for HeE1-2Tyr molecules were generated in phenix.elbow ( 58 ), and the model quality was assessed using MolProbity within Phenix ( 59 ), which revealed excellent stereochemistry ( SI Appendix , Table S1 ).
- Full pipeline: alignment/mapping [RELION] -> normalisation [ChimeraX] -> stage not stated [Clustal Omega, PHENIX]

### High-resolution structures of Myosin-IC reveal a unique actin-binding orientation, ADP release pathway, and power stroke trajectory. (PNAS 2025)

- DOI: 10.1073/pnas.2415457122 | PMCID: PMC11892617 | PMID: 40014570
- Evidence: Initial structure models were built using the model-angelo automated tool ( 53 ), and further building and refinement was done manually using Isolde ( 54 ), COOT ( 55 ), and Phenix ( 56 ); Isolde was used for the final refinement cycles.
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold]

### Cryo-EM of native membranes reveals an intimate connection between the Krebs cycle and aerobic respiration in mycobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2423761122 | PMCID: PMC11874196 | PMID: 39969994
- Evidence: Fitting was done with UCSF Chimera ( 47 ) and Phenix ( 48 ).
- Full pipeline: structure determination [Topaz] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, PHENIX, UCSF Chimera]

### Stepwise activation of SARM1 for cell death and axon degeneration revealed by a biosynthetic NMN mimic. (PNAS 2025)

- DOI: 10.1073/pnas.2424906122 | PMCID: PMC11874154 | PMID: 39964720
- Evidence: The model was docked into cryo-EM map using Chimera ( 32 ), and then manually adjusted in COOT ( 33 ), followed by real-space-refinement in Phenix ( 34 ).
- Full pipeline: quantification [ImageJ] -> registration [MotionCor2, Topaz] -> structure determination [PHENIX, Topaz] -> stage not stated [ChimeraX, PyMOL]

### NPF binding to Arp2 is allosterically linked to the release of ArpC5's N-terminal tail and conformational changes in Arp2/3 complex. (PNAS 2025)

- DOI: 10.1073/pnas.2421557122 | PMCID: PMC11873952 | PMID: 40042350
- Evidence: Coot ( 40 ) and Phenix ( 41 ) were used for model building and refinement, starting from the high-resolution crystal structure of nucleotide-free, inactive Arp2/3 complex (PDB code 1K8K) ( 2 ) and the cryo-EM structure of the transition complex with NPF and actin bound (PDB code 7T5Q) ( 6 ).
- Full pipeline: structure determination [ChimeraX, PHENIX] -> visualisation [PyMOL] -> stage not stated [Topaz]

### Structures and functions of the limited natural polyclonal antibody response to parvovirus infection. (PNAS 2025)

- DOI: 10.1073/pnas.2423460122 | PMCID: PMC11873831 | PMID: 39951487
- Evidence: The homology model of the cFab 7C8 was combined with the CPV VP2 asymmetric unit and refined within the icosahedral map by using ISOLDE and real space refinement in PHENIX.
- Full pipeline: alignment/mapping [RELION] -> structure determination [PHENIX] -> stage not stated [ChimeraX]

### Structural characterization of influenza group 1 chimeric hemagglutinins as broad vaccine immunogens. (PNAS 2025)

- DOI: 10.1073/pnas.2416628122 | PMCID: PMC11848309 | PMID: 39937865
- Evidence: Further iterative manual building and refinement of models were carried out using Phenix ( 56 ).
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [ChimeraX, PyMOL]

### Structural basis of disease mutation and substrate recognition by the human SLC2A9 transporter. (PNAS 2025)

- DOI: 10.1073/pnas.2418282122 | PMCID: PMC11848319 | PMID: 39937868
- Evidence: A starting model of SLC2A9 from AlphaFold2 (AF- Q9NRM0 -F1, https://www.uniprot.org/uniprotkb/Q9NRM0/entry#structure ) was used for manual rigid-body fitting in COOT ( 37 ) followed by real-space refinement in Phenix ( 38 , 39 ) against the final cryo-EM map.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX]

### HflX-mediated drug resistance through ribosome splitting and rRNA disordering in mycobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2419826122 | PMCID: PMC11831132 | PMID: 39913204
- Version used: **1.14**
- Evidence: The models were subsequently refined in PHENIX 1.14 ( 51 ).
- Full pipeline: structure determination [PHENIX v1.14] -> stage not stated [ChimeraX v1.0]

### Biochemical and structural bases for talin ABSs-F-actin interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2405922122 | PMCID: PMC11831117 | PMID: 39903122
- Evidence: The composite model was then subjected to rounds of manual building in COOT and real-space refinement in PHENIX ( 60 ) to remove clashes and correct the stereochemistry.
- Full pipeline: registration [CTFFIND v4.1, MotionCor2, RELION v3.1] -> structure determination [PHENIX]

### Bacterial sensor evolved by decreasing complexity. (PNAS 2025)

- DOI: 10.1073/pnas.2409881122 | PMCID: PMC11804620 | PMID: 39879239
- Evidence: Refinement was initiated with phenix.refine ( 76 ) of the PHENIX suite ( 77 ) and Refmac ( 78 ) of the CCP4 program suite.
- Full pipeline: normalisation [CCP4] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Structural insights into the role of reduced cysteine residues in SOD1 amyloid filament formation. (PNAS 2025)

- DOI: 10.1073/pnas.2408582122 | PMCID: PMC11804504 | PMID: 39874287
- Version used: **1.21**
- Evidence: Refinement was performed using the real-space refinement program in Phenix 1.21 ( 58 ).
- Full pipeline: structure determination [PHENIX v1.21] -> visualisation [ChimeraX v1.4, PyMOL v3.0] -> stage not stated [CTFFIND, ImageJ, MotionCor2, RELION]

### Lipid-induced condensate formation from the Alzheimer's Aβ peptide triggers amyloid aggregation. (PNAS 2025)

- DOI: 10.1073/pnas.2401307122 | PMCID: PMC11789053 | PMID: 39854227
- Evidence: Imaging was done using the Opera Phenix High-Content confocal microscope.
- Full pipeline: stage not stated [PHENIX]

### Structure-guided engineering of a mutation-tolerant inhibitor peptide against variable SARS-CoV-2 spikes. (PNAS 2025)

- DOI: 10.1073/pnas.2413465122 | PMCID: PMC11789008 | PMID: 39854234
- Evidence: The atomic model was rebuilt by manual model building in COOT ( 49 ) and refinement in PHENIX ( 50 ) and Refmac5 ( 51 ).
- Full pipeline: normalisation [Topaz] -> structure determination [PHENIX] -> stage not stated [CCP4, RELION]

### Structural insights into glucose-6-phosphate recognition and hydrolysis by human G6PC1. (PNAS 2025)

- DOI: 10.1073/pnas.2418316122 | PMCID: PMC11789071 | PMID: 39847333
- Evidence: The refinement and geometric constraints were carried out in PHENIX ( 52 ).
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ChimeraX, PyMOL]

### Molecular mechanism of ligand recognition and activation of lysophosphatidic acid receptor LPAR6. (PNAS 2025)

- DOI: 10.1073/pnas.2415426122 | PMCID: PMC11789011 | PMID: 39847322
- Evidence: Iterative manual adjustments were carried out in Coot ( 44 ), followed by further refinement with Rosetta cryo-EM refinement ( 45 ) and Phenix real space refinement ( 46 ).
- Full pipeline: alignment/mapping [AlphaFold] -> dimensionality reduction/clustering [RELION] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v4.1, MotionCor2, R v3.50]

### Nitrous oxide production via enzymatic nitroxyl from the nitrifying archaeon &lt;i&gt;Nitrosopumilus maritimus&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2416971122 | PMCID: PMC11761707 | PMID: 39823305
- Version used: **1.2**
- Evidence: An initial model was generated in Phenix 1.2 ( 53 ) using the molecular replacement method and an AlphaFold2 ( 54 ) model of a truncated version of the protein consisting of only the first 300 amino acids.
- Full pipeline: normalisation [CCP4 v7.0] -> stage not stated [AlphaFold, PHENIX v1.2]

### A histochemical approach to activity-based copper sensing reveals cuproplasia-dependent vulnerabilities in cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2412816122 | PMCID: PMC11761388 | PMID: 39813247
- Evidence: Cells were imaged using a Zeiss LSM880 laser scanning confocal microscopy system with a 20x dry objective lens or a Perkin Elmer Opera Phenix automated confocal microscope using a 10x dry objective lens.
- Full pipeline: normalisation [ImageJ] -> stage not stated [PHENIX]

### Structural determinants of oxygen resistance and Zn&lt;sup&gt;2+&lt;/sup&gt;-mediated stability of the [FeFe]-hydrogenase from &lt;i&gt;Clostridium beijerinckii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2416233122 | PMCID: PMC11760498 | PMID: 39805018
- Evidence: H-, Fd-, Zn-, and SLBB- domains were manually repositioned and refined iteratively using COOT and PHENIX real space refinement ( 51 , 52 ).
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, MotionCor2, RELION]

### CryoEM structure of an MHC-I/TAPBPR peptide-bound intermediate reveals the mechanism of antigen proofreading. (PNAS 2025)

- DOI: 10.1073/pnas.2416992122 | PMCID: PMC11745410 | PMID: 39786927
- Evidence: The model of the MHC-I/TAPBPR complex was built iteratively in ISOLDE ( 76 ), Coot ( 77 ), and PHENIX ( 78 ), using PDB 2VLL as the starting model.
- Full pipeline: visualisation [ChimeraX] -> stage not stated [PHENIX]

### Structural and functional dynamics of human cone cGMP-phosphodiesterase important for photopic vision. (PNAS 2025)

- DOI: 10.1073/pnas.2419732121 | PMCID: PMC11725853 | PMID: 39739818
- Evidence: The model was subsequently refined using NAMDinator and iterative cycles in Phenix real space refine and manual modification in Coot ( 40 , 45 , 46 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UCSF Chimera] -> structure determination [ChimeraX, Coot, PHENIX, UCSF Chimera] -> stage not stated [Topaz]

### Dual-action kinase inhibitors influence p38α MAP kinase dephosphorylation. (PNAS 2025)

- DOI: 10.1073/pnas.2415150122 | PMCID: PMC11725910 | PMID: 39739785
- Evidence: The data were integrated with XDS ( 74 ), scaled and merged in Aimless ( 75 ), and data quality was assessed using Xtriage (Phenix) ( 76 ).
- Full pipeline: normalisation [PHENIX] -> stage not stated [ChimeraX]

### Computational-aided rational mutation design of pertuzumab to overcome active HER2 mutation S310F through antibody-drug conjugates. (PNAS 2025)

- DOI: 10.1073/pnas.2413686122 | PMCID: PMC11725927 | PMID: 39793038
- Evidence: The model was fitted into maps using Chimera, manually adjusted according to the density map in Coot ( 37 ) and was refined against map using real-space refinement in PHENIX ( 38 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.0]

### Molecular basis of Spns1-mediated lysophospholipid transport from the lysosome. (PNAS 2025)

- DOI: 10.1073/pnas.2409596121 | PMCID: PMC11725778 | PMID: 39739806
- Evidence: The model was then refined iteratively using Coot ( 48 ) and Phenix ( 49 ).
- Full pipeline: registration [MotionCor2, RELION v3.1] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, NAMD]

### Structures of methane and ammonia monooxygenases in native membranes. (PNAS 2025)

- DOI: 10.1073/pnas.2417993121 | PMCID: PMC11725843 | PMID: 39739801
- Version used: **1.21**
- Evidence: Further refinement of the models involved iterative rounds of real-space refinement using the Phenix (version 1.21-5207) cryoEM suite along with automatic addition of waters ( 40 ), followed by manual inspection and refinement within Coot.
- Full pipeline: structure determination [ChimeraX, PHENIX v1.21, Topaz] -> visualisation [ChimeraX] -> stage not stated [Coot]

### CryoSeek II: Cryo-EM analysis of glycofibrils from freshwater reveals well-structured glycans coating linear tetrapeptide repeats. (PNAS 2025)

- DOI: 10.1073/pnas.2423943122 | PMCID: PMC11725842 | PMID: 39739783
- Evidence: The final model of TLP-4 was refined using PHENIX with secondary structure and geometry restraints in real space ( 52 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [MotionCor2]

### RAP-2 and CNH-MAP4 Kinase MIG-15 confer resistance in bystander epithelium to cell-fate transformation by excess Ras or Notch activity. (PNAS 2025)

- DOI: 10.1073/pnas.2414321121 | PMCID: PMC11725784 | PMID: 39739816
- Evidence: Immunoactive proteins were detected by film processor, SRX-101A (Konica Minolta) on X-ray film (Phenix) for MIG-15 and BioRad ChemiDoc XRS for RAP-2 and MIG-15 AID* validation.
- Full pipeline: quantification [ImageJ] -> stage not stated [PHENIX]

### Tamsulosin ameliorates bone loss by inhibiting the release of Cl<sup>-</sup> through wedging into an allosteric site of TMEM16A. (PNAS 2025)

- DOI: 10.1073/pnas.2407493121 | PMCID: PMC11725887 | PMID: 39739807
- Evidence: COOT ( 51 ) was used for manual modeling of the TMEM16A structure, while PHENIX ( 52 ) was used for real-space refinement.
- Full pipeline: structure determination [AlphaFold, PHENIX, UCSF Chimera] -> visualisation [ChimeraX]

### Structural basis of nearest-neighbor cooperativity in the ring-shaped gene regulatory protein TRAP from protein engineering and cryo-EM. (PNAS 2025)

- DOI: 10.1073/pnas.2409030121 | PMCID: PMC11725872 | PMID: 39793047
- Evidence: The C6 reconstructed map and initial model were used to refine a linked dTRAP protomer using multiple iterations of Coot, ISOLDE, and PHENIX Real Space Refinement ( 51 – 54 ).
- Full pipeline: normalisation [ChimeraX] -> structure determination [PHENIX] -> stage not stated [AlphaFold]

### Structural insight into sodium ion pathway in the bacterial flagellar stator from marine &lt;i&gt;Vibrio&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2415713122 | PMCID: PMC11725901 | PMID: 39793043
- Evidence: The atomic models were constructed by Coot ( 51 ) and refined using Phenix ( 52 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CTFFIND v4.1, ChimeraX, RELION]

### Elevated MyoD1 levels expand genome-wide binding and the repertoire of regulated genes. (PNAS 2026)

- DOI: 10.1073/pnas.2605749123 | PMCID: PMC13291607 | PMID: 42301790
- Evidence: Confocal microscopy was performed on a Perkin Elmer Opera Phenix microscope.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [DESeq2, R] -> stage not stated [HOMER, Matplotlib, NumPy, OpenCV, PHENIX, Python, pheatmap]

### Cryo-EM reveals a right-handed double-helix dimer architecture of PCDH15. (PNAS 2026)

- DOI: 10.1073/pnas.2607573123 | PMCID: PMC13273323 | PMID: 42263124
- Evidence: All molecular modeling, refinement, and analysis were performed using UCSF ChimeraX ( 37 ), ChimeraX ( 38 ), ISOLDE ( 39 ), Coot ( 40 , 41 ), and Phenix ( 42 ), accessed via the SBGrid consortium ( 43 ).
- Full pipeline: quantification [ImageJ] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold]

### Anti-CRISPR-mediated continuous directed evolution of CRISPR-Cas9 in human cells. (PNAS 2026)

- DOI: 10.1073/pnas.2536003123 | PMCID: PMC13229284 | PMID: 42189993
- Evidence: High-throughput fluorescent imaging of JF646 (Alexa 647 channel) and Hoechst 33342 was performed using a 60× water objective on an automated Opera Phenix High-Content Imaging System (PerkinElmer), and image analysis was conducted with Harmony software (v4.9, PerkinElmer) across a z-stack comprising 0.5 μm sections.
- Full pipeline: alignment/mapping [minimap2] -> stage not stated [PHENIX]

### A PKA-selective inhibitor captures an open but more ordered conformation of the PKA catalytic subunit. (PNAS 2026)

- DOI: 10.1073/pnas.2536312123 | PMCID: PMC13167742 | PMID: 42096309
- Evidence: The BLU0588 inhibitor was built into the model using Coot’s ligand builder AceDRG ( 49 ), followed with real space refinement and ligand restraints file (cif) from Phenix Ready Set ( 50 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL]

### Structural basis of iron piracy by human gut &lt;i&gt;Bacteroides&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2528036123 | PMCID: PMC13142918 | PMID: 42066043
- Evidence: All models underwent cycles of manual building in Coot ( 63 ) and refinement in Phenix ( 64 ) until no further improvement in R factors could be achieved.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [AlphaFold]

### Computational design of an ultrapotent deltacoronavirus miniprotein inhibitor. (PNAS 2026)

- DOI: 10.1073/pnas.2533456123 | PMCID: PMC13142991 | PMID: 42054371
- Evidence: The models were refined and validated using Phenix ( https://www.phenix-online.org/ ) ( 83 ), Molprobity ( http://molprobity.biochem.duke.edu/ ) ( 84 ), and Privateer ( https://github.com/glycojones/privateer ) ( 85 ).
- Full pipeline: structure determination [ChimeraX, PHENIX, Topaz] -> stage not stated [AlphaFold, RELION v3.0]

### Restoring the 14-3-3/CRAF regulatory interaction in Noonan syndrome using molecular glues. (PNAS 2026)

- DOI: 10.1073/pnas.2602101123 | PMCID: PMC13142914 | PMID: 42048443
- Version used: **1.21.2**
- Evidence: GraphPad Prism 10 (10.0.3), Adobe Illustrator (29.7.1), Biorender, Pymol (3.1.6.1), CCP4i2 (1.0.2), COOT (0.9.3), Phenix (1.21.2) Supplementary Material Appendix 01 (PDF) Data, Materials, and Software Availability Supplementary figures, tables, and crystallography data (PDF).
- Full pipeline: stage not stated [PHENIX v1.21.2, PyMOL]

### Small subunit isoform diversity underlies structural heterogeneity in native plant Rubisco. (PNAS 2026)

- DOI: 10.1073/pnas.2519949123 | PMCID: PMC13099656 | PMID: 41984840
- Evidence: Structural refinements were performed using the phenix.real_space_refine program ( 36 ) from the PHENIX suite ( 37 ).
- Full pipeline: structure determination [AlphaFold, PHENIX]

### Structural basis of transcription-coupled RNA damage by incorporation of oxidized ribonucleotides. (PNAS 2026)

- DOI: 10.1073/pnas.2602266123 | PMCID: PMC13099631 | PMID: 41980106
- Evidence: All structures were solved by molecular replacement using Phaser from the Phenix software suite, with the undamaged 10-subunit Pol II structure (PDB ID: 6UQ2) as the search model ( 51 , 52 ).
- Full pipeline: structure determination [Coot] -> stage not stated [PHENIX]

### Deep learning-enabled scaffolding of spatial arrays of PfCSP epitopes. (PNAS 2026)

- DOI: 10.1073/pnas.2521914123 | PMCID: PMC13079917 | PMID: 41945436
- Evidence: The complete model was then refined iteratively with Coot v9.8.7 ( 54 ), Phenix real space refine ( 55 ), and Rosetta Relax ( 56 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [ChimeraX v1.7, RoseTTAFold]

### Small molecule-constrained paratope mimetic bicyclic peptides as potent inhibitors of group 1 and 2 influenza A virus hemagglutinins. (PNAS 2026)

- DOI: 10.1073/pnas.2537533123 | PMCID: PMC13037862 | PMID: 41875158
- Evidence: Iterative refinement was performed with Phenix ( 49 ), with manual rebuilding in COOT ( 50 ).
- Full pipeline: structure determination [PHENIX]

### Recurrent SARS-CoV-2 Omicron broadly neutralizing humanized antibodies in different single human V&lt;sub&gt;H&lt;/sub&gt;1-2-rearranging mouse models. (PNAS 2026)

- DOI: 10.1073/pnas.2537053123 | PMCID: PMC13037937 | PMID: 41871249
- Evidence: Model building was performed in Coot ( 61 ), and iterative refinement in Phenix ( 62 ) and ISOLDE ( 63 ).
- Full pipeline: structure determination [Coot, PHENIX]

### Direct evidence of acid-driven protein desolvation. (PNAS 2026)

- DOI: 10.1073/pnas.2525949123 | PMCID: PMC12974452 | PMID: 41785322
- Evidence: The amino acid sequence of the H. sapiens ApoF heavy chain (Uniprot id: P02794 ) monomer was fit into each of the different p H EM reconstructions using ChimeraX ( 80 ), and then real space refined in PHENIX ( 27 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [ChimeraX, MDAnalysis, PHENIX] -> stage not stated [RELION, SciPy]

### Decoding antibody response to MERS-CoV in wild dromedary camels. (PNAS 2026)

- DOI: 10.1073/pnas.2513716123 | PMCID: PMC12913009 | PMID: 41662528
- Evidence: Model building and refinement were established using COOT and PHENIX, respectively.
- Full pipeline: alignment/mapping [IQ-TREE v2.1.4, MAFFT v7.310, MUSCLE v3.8.1551] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.3, PyMOL] -> stage not stated [CCP4]

### Molecular architecture and diversity of StopGo/2A translational recoding. (PNAS 2026)

- DOI: 10.1073/pnas.2528667123 | PMCID: PMC12846837 | PMID: 41576085
- Evidence: Cryo-EM data were collected on a Titan Krios microscope and then processed in RELION; a molecular model was built using Coot and refined in Phenix.
- Full pipeline: structure determination [PHENIX, RELION]

### Structural basis for iterative methylation by a cobalamin-dependent radical &lt;i&gt;S&lt;/i&gt;-adenosylmethionine enzyme in cystobactamids biosynthesis. (PNAS 2026)

- DOI: 10.1073/pnas.2527019123 | PMCID: PMC12846815 | PMID: 41564129
- Evidence: An Alpha fold model ( https://alphafold.ebi.ac.uk/entry/A0A3A8HCN5 ) was used for molecular replacement using Phenix Phaser-MR ( 39 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [PHENIX]

### Structural characterization of the HDV virion and its ribonucleoprotein. (PNAS 2026)

- DOI: 10.1073/pnas.2519809123 | PMCID: PMC12846810 | PMID: 41564123
- Evidence: The final model was refined iteratively with Phenix’s phenix.real_space_refine ( 57 ).
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [ChimeraX, Coot, Matplotlib, NumPy, SciPy, Topaz, UCSF Chimera]

### Liganded LolCDE structures reveal a common substrate-LolE interaction guiding bacterial lipoprotein transport. (PNAS 2026)

- DOI: 10.1073/pnas.2520579123 | PMCID: PMC12846838 | PMID: 41557797
- Evidence: All maps were anisotropically sharpened as implemented within PHENIX ( 66 ) and deposited to the EMDB.
- Full pipeline: visualisation [ChimeraX] -> stage not stated [PHENIX]

### Molecular structure of the ESCRT-III-based archaeal CdvAB cell division machinery. (PNAS 2026)

- DOI: 10.1073/pnas.2525941123 | PMCID: PMC12818579 | PMID: 41543908
- Evidence: A dimer of SiCdvA ΔC from the crystal structure was rigidly docked into the cryo-EM map, and refined in Coot and PHENIX real-space refine.
- Full pipeline: alignment/mapping [MAFFT, PyMOL] -> structure determination [Coot, PHENIX, RELION] -> visualisation [ChimeraX v1.7.1] -> stage not stated [AlphaFold, MotionCor2]

### Phosphatase SHP2 pathogenic mutations enhance activity by altering conformational sampling. (PNAS 2026)

- DOI: 10.1073/pnas.2513851123 | PMCID: PMC12818432 | PMID: 41528873
- Evidence: Images were processed in XDS or iMosflm, scaled and merged in Aimless, and the structure solved and refined in Phenix with model adjustments performed in Coot.
- Full pipeline: normalisation [Coot, PHENIX] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Design of solubly expressed miniaturized SMART MHCs. (PNAS 2026)

- DOI: 10.1073/pnas.2505932123 | PMCID: PMC12773744 | PMID: 41481462
- Evidence: The crystal structure was determined by molecular replacement with Phaser-MR in PHENIX 69 with the design model employed as the search model.
- Full pipeline: visualisation [PyMOL] -> stage not stated [AlphaFold, PHENIX]

### Mass spectrometry footprinting reveals how kinetic stabilizers counteract transthyretin dynamics altered by pathogenic mutations. (PNAS 2026)

- DOI: 10.1073/pnas.2519908122 | PMCID: PMC12773722 | PMID: 41474749
- Version used: **1.19.2**
- Evidence: The structures of TTR/M-23 and V30M-TTR/tolcapone complexes were determined by molecular replacement with Phenix (version 1.19.2-4158) ( 55 ) using a previous TTR structure (PDB 1F41) as a search model.
- Full pipeline: normalisation [CCP4] -> visualisation [PyMOL] -> stage not stated [PHENIX v1.19.2]

### Ultrapotent antibodies against diverse and highly transmissible SARS-CoV-2 variants. (Science 2021)

- DOI: 10.1126/science.abh1766 | PMCID: PMC9269068 | PMID: 34210892
- Evidence: Iterative manual model building and real space refinement were carried out in Coot ( 48 ) and in Phenix ( 49 ), respectively.
- Full pipeline: variant calling [GATK v4.1.9.0] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, UCSF Chimera]

### Effect of natural mutations of SARS-CoV-2 on spike structure, conformation, and antigenicity. (Science 2021)

- DOI: 10.1126/science.abi6226 | PMCID: PMC8611377 | PMID: 34168071
- Evidence: Phenix ( 54 , 59 ), Coot ( 60 ), Pymol ( 61 ), Chimera ( 62 ), ChimeraX ( 63 ), and Isolde ( 64 ) were used for model building and refinement.
- Full pipeline: alignment/mapping [PyMOL] -> dimensionality reduction/clustering [R] -> simulation/modelling [VMD] -> structure determination [ChimeraX, PHENIX] -> visualisation [PyMOL] -> stage not stated [RELION]

### Structure-guided multivalent nanobodies block SARS-CoV-2 infection and suppress mutational escape. (Science 2021)

- DOI: 10.1126/science.abe6230 | PMCID: PMC7932109 | PMID: 33436526
- Evidence: Iterative model building and refinement were carried out in COOT ( 57 ) and PHENIX ( 58 ), respectively.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2, RELION v3.1, SAMtools] -> variant calling [GATK] -> quantification [ImageJ] -> structure determination [PHENIX, RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [MACS2]

### RNA-activated protein cleavage with a CRISPR-associated endopeptidase. (Science 2022)

- DOI: 10.1126/science.add7450 | PMCID: PMC10028731 | PMID: 36423276
- Evidence: Coordinates were refined in real space using PHENIX ( 43 ), performing one macrocycle of global minimization and atomic displacement parameter (ADP) refinement and skipping local grid searches.
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, Coot, Jupyter, MotionCor2, RELION]

### Mapping the developing human immune system across organs. (Science 2022)

- DOI: 10.1126/science.abo0510 | PMCID: PMC7612819 | PMID: 35549310
- Evidence: The sections were imaged on a Perkin Elmer Opera Phenix High Content Screening System (16-bit sCMOS camera, PerkinElmer) with a 20X water objective (High NA, PerkinElmer).
- Full pipeline: alignment/mapping [AnnData] -> quantification [scikit-learn] -> normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [Squidpy v1.1.2, UMAP, scikit-learn] -> machine learning [AnnData] -> visualisation [AnnData] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder v0.2.3]

### Cross-tissue immune cell analysis reveals tissue-specific features in humans. (Science 2022)

- DOI: 10.1126/science.abl5197 | PMCID: PMC7612735 | PMID: 35549406
- Evidence: Slides were imaged on the Perkin Elmer Opera Phenix High-Content Screening System, in confocal mode with 1 μm z-step size, using 20X (NA 0.16, 0.299 μm/pixel) and 40X (NA 1.1, 0.149 μm/pixel) water-immersion objectives.
- Full pipeline: normalisation [Scanpy v1.6.0] -> dimensionality reduction/clustering [Scanpy v1.6.0, UMAP] -> visualisation [UMAP] -> stage not stated [PHENIX, scDblFinder]

### Structural basis for potent antibody neutralization of SARS-CoV-2 variants including B.1.1.529. (Science 2022)

- DOI: 10.1126/science.abn8897 | PMCID: PMC9580340 | PMID: 35324257
- Evidence: Iterative manual model building and real-space refinement were carried out in Coot ( 48 ) and in Phenix ( 62 ), respectively.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold v2.0, ChimeraX, UCSF Chimera]

### Reconfigurable asymmetric protein assemblies through implicit negative design. (Science 2022)

- DOI: 10.1126/science.abj7662 | PMCID: PMC9881579 | PMID: 35050655
- Evidence: Structures were refined in Phenix ( 50 ) using phenix.autobuild and phenix.refine or Refmac ( 51 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [PyMOL, SciPy v1.6.3]

### PIM1 controls GBP1 activity to limit self-damage and to guard against pathogen infection. (Science 2023)

- DOI: 10.1126/science.adg2253 | PMCID: PMC7615196 | PMID: 37797010
- Evidence: For recruitment analysis, plates were imaged on an Opera Phenix High-Content Screening System (Perkin Elmer) or a Celldiscoverer 7 (Zeiss) using 20x/40x magnification.
- Full pipeline: alignment/mapping [MAFFT] -> quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [ChimeraX v0.93, MACS2, PHENIX, Topaz]

### DNSN-1 recruits GINS for CMG helicase assembly during DNA replication initiation in &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (Science 2023)

- DOI: 10.1126/science.adi4932 | PMCID: PMC7615117 | PMID: 37590372
- Evidence: After the completion of model building, the model was refined in the cryo-EM reconstruction encompassing the complete CMG/TIM-1/TIPN-1/DNSN-1 complex (3.75 Å resolution), using Phenix real-space refinement ( 73 ), enabling secondary structure restraints and using the input model as a reference to generate restraints with a sigma value of 0.1, and performing global minimisation with an nonbonded we...
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, ImageJ, RELION]

### Engineering synthetic suppressor T cells that execute locally targeted immunoprotective programs. (Science 2024)

- DOI: 10.1126/science.adl4793 | PMCID: PMC11831968 | PMID: 39636990
- Evidence: The media was changed the next day, then every other day until days 27 to 29. eBC organoid In vitro microscopy assays In vitro assays for suppression of T cell killing of enriched beta cell clusters was performed on an Incucyte Live-Cell Analysis System (Sartorius) or Opera Phenix Plus High-Content Screening System.
- Full pipeline: dimensionality reduction/clustering [PHENIX] -> visualisation [ImageJ]

### Specific tRNAs promote mRNA decay by recruiting the CCR4-NOT complex to translating ribosomes. (Science 2024)

- DOI: 10.1126/science.adq8587 | PMCID: PMC11583848 | PMID: 39571015
- Evidence: After manual rebuilding in COOT ( 81 ), the final model was refined in PHENIX using phenix.real_space_refine ( 82 ) with Ramachandran and secondary structure restraints.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [GSEA, RELION v4.0]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: The model was refined first using ISOLDE, then with Phenix real_space_refine ( 63 ), just performing one macro-cycle.
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

### Ciliopathy patient variants reveal organelle-specific functions for TUBB4B in axonemal microtubules. (Science 2024)

- DOI: 10.1126/science.adf5489 | PMCID: PMC7616230 | PMID: 38662826
- Evidence: ISOLDE’s command `write phenixRsrInputˋ was used to create a parameter file for subsequent refinement in Phenix.real_space_refinement ( 72 ).
- Full pipeline: alignment/mapping [IMOD, UCSF Chimera] -> quantification [ImageJ, Seurat, ilastik] -> dimensionality reduction/clustering [RELION] -> differential/statistical testing [RELION] -> structure determination [ChimeraX, IMOD, PHENIX, RELION] -> visualisation [ImageJ, ilastik] -> stage not stated [VEP]

### Molecular mechanism of dynein-dynactin complex assembly by LIS1. (Science 2024)

- DOI: 10.1126/science.adk8544 | PMCID: PMC7615804 | PMID: 38547289
- Evidence: Model building and refinement Model building and restrained flexible fitting of models in the density was done in COOT ( 105 ) and refinements were performed in PHENIX ( 106 ).
- Full pipeline: alignment/mapping [ChimeraX] -> quantification [R] -> registration [MotionCor2, RELION] -> differential/statistical testing [R] -> structure determination [PHENIX] -> machine learning [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ColabFold, ImageJ, UCSF Chimera]

### Precise targeting of HIV broadly neutralizing antibody precursors in humans. (Science 2025)

- DOI: 10.1126/science.adv5572 | PMCID: PMC12313413 | PMID: 40373114
- Evidence: Model building was performed by docking homology models of trimer and Fab Fv in UCSF ChimeraX ( 78 ), manually building and refining in Coot 0.9.8 ( 93 ) and real space refinement using Phenix ( 94 ).
- Full pipeline: alignment/mapping [Bowtie2] -> structure determination [Coot v0.9.8, PHENIX] -> stage not stated [ChimeraX, Nextflow, R, RELION v4.0, Trinity]

### Vaccination with mRNA-encoded nanoparticles drives early maturation of HIV bnAb precursors in humans. (Science 2025)

- DOI: 10.1126/science.adr8382 | PMCID: PMC13164876 | PMID: 40373112
- Evidence: Model building was performed by docking homology models of trimer (generated by AlphaFold 3 ( 85 )) and Fab Fv (generated by AbodyBuilder2 ( 86 )) in UCSF ChimeraX ( 87 ), manually building and refining in Coot 0.9.8 ( 88 ) and real space refinement using Phenix ( 89 ).
- Full pipeline: differential/statistical testing [Matplotlib, seaborn] -> structure determination [AlphaFold, ChimeraX, Coot v0.9.8, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [NumPy]

### Autoinhibition imposed by a large conformational switch of INO80 regulates nucleosome positioning. (Science 2025)

- DOI: 10.1126/science.adr3831 | PMCID: PMC12403922 | PMID: 40674492
- Evidence: The structures were refined using Phenix ( 53 ) with secondary structure constraints.
- Full pipeline: quantification [ImageJ] -> structure determination [PHENIX, RELION] -> stage not stated [MotionCor2]

### Cryo-EM structure of human telomerase dimer reveals H/ACA RNP-mediated dimerization. (Science 2025)

- DOI: 10.1126/science.adr5817 | PMCID: PMC7618144 | PMID: 40638752
- Version used: **1.20**
- Evidence: Phenix 1.20 was used to calculate model-versus-map FSCs and EMRinger scores ( 74 ).
- Full pipeline: alignment/mapping [minimap2] -> machine learning [Topaz] -> stage not stated [CTFFIND, ChimeraX, ImageJ, PHENIX v1.20, RELION v5.0, UCSF Chimera]

### Cat1 forms filament networks to degrade NAD&lt;sup&gt;+&lt;/sup&gt; during the type III CRISPR-Cas antiviral response. (Science 2025)

- DOI: 10.1126/science.adv9045 | PMCID: PMC12162218 | PMID: 40208959
- Evidence: Phenix real-space refinement program was used to remove the outliers and refine the models with a model vs. data correlation value (CC mask) of 0.89 and 0.86 for the triagonal filament bundle and pentameric filament bundle respectively.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold]

### TIGR-Tas: A family of modular RNA-guided DNA-targeting systems in prokaryotes and their viruses. (Science 2025)

- DOI: 10.1126/science.adv9789 | PMCID: PMC12045711 | PMID: 40014690
- Evidence: The model was refined first using ISOLDE, then with Phenix real_space_refine ( 105 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, MAFFT, PyMOL] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [MAFFT, PHENIX] -> stage not stated [CTFFIND, ColabFold, Coot, HMMER, MotionCor2, RELION, Topaz]

### Structural mechanism of LINE-1 target-primed reverse transcription. (Science 2025)

- DOI: 10.1126/science.ads8412 | PMCID: PMC7617806 | PMID: 40048554
- Version used: **1.21.1**
- Evidence: Models were first refined using PHENIX 1.21.1-5286 ( 102 ) then Servalcat 0.4.72 ( 103 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, PHENIX v1.21.1, RELION] -> stage not stated [CTFFIND, ChimeraX, ImageJ, MotionCor2, PyMOL, Python, REFMAC, Topaz]

### Evolutionary adaptations of doublet microtubules in trypanosomatid parasites. (Science 2025)

- DOI: 10.1126/science.adr5507 | PMCID: PMC7617938 | PMID: 40080577
- Evidence: Once all chains had been built, they were combined into a single PDB file and refined against the composite map using Phenix real-space refinement ( 58 ).
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [napari] -> stage not stated [AlphaFold, CTFFIND v4.0, ChimeraX, HMMER, ImageJ, RELION]

### Molecular basis of FIGNL1 in dissociating RAD51 from DNA and chromatin. (Science 2025)

- DOI: 10.1126/science.adr7920 | PMCID: PMC7617353 | PMID: 39636933
- Evidence: This model was then split into the component protomers and fit into the generated map and subjected to real space refinement in Phenix ( 67 ).
- Full pipeline: registration [CTFFIND] -> structure determination [AlphaFold, PHENIX] -> visualisation [Fiji, ImageJ, RELION] -> stage not stated [Coot, Topaz]

### Induction of broadly neutralizing HIV antibodies by a two-step mechanism informs vaccine design. (Science 2026)

- DOI: 10.1126/science.aec6396 | PMCID: PMC13308464 | PMID: 42096521
- Evidence: Manual adjustments and sequence corrections were performed using Coot v.0.8.9 ( 91 ), followed by iterative cycles of model rebuilding in Coot and refinement using Phenix ( 92 ).
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [SciPy v0.18.0] -> structure determination [ChimeraX, Coot v0.8.9, PHENIX] -> visualisation [PyMOL]

### Cryo-electron microscopy structure of the budding yeast telomerase holoenzyme. (Science 2026)

- DOI: 10.1126/science.adz5344 | PMCID: PMC7619062 | PMID: 41886584
- Evidence: Model refinements were performed using Phenix and Servalcat ( 107 , 108 ).Models were validated using Molprobity ( 109 ) and wwPDB validation system ( https://validate-rcsb-1.wwpdb.org/ ).
- Full pipeline: quantification [ImageJ] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, CTFFIND v4.1, Python, RELION v5.0, Topaz]

### Termination of the integrated stress response. (Science 2026)

- DOI: 10.1126/science.adw5137 | PMCID: PMC7618491 | PMID: 41231936
- Evidence: The Refmac-refined models were subsequently subjected to real-space refinement in Phenix ( 50 ).
- Full pipeline: registration [RELION v5.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, PyMOL]

### Structural ontogeny of protein-protein interactions. (Science 2026)

- DOI: 10.1126/science.adx6931 | PMCID: PMC12904254 | PMID: 41678610
- Evidence: Additional refinement was performed interactively in Coot ( 78 ) and in Phenix ( 79 - 82 ) (A2B2, A3B3, A5B5, A6B6, A7B7) or Buster ( 83 , 84 ) with final refinement in Phenix (A4B1, A7B3).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CCP4, MACS2, SciPy, igraph]

### Structure and organization of AMPA receptor-TARP complexes in the mammalian cerebellum. (Science 2026)

- DOI: 10.1126/science.aeb3577 | PMCID: PMC7619101 | PMID: 41379938
- Evidence: S3 ) Model building and refinement for high-resolution structures were performed using Coot ( 81 ), Refmac-Servalcat ( 82 ), ISOLDE ( 83 ) and PHENIX real space refinement ( 84 ).
- Full pipeline: alignment/mapping [MUSCLE] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [PyMOL v2.5] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

