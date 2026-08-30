# RELION

- **Category:** structbio
- **Papers in survey:** 466
- **Journals:** PNAS (232), Nature (165), Cell (47), Science (22)
- **Years:** 2021 (55), 2022 (106), 2023 (100), 2024 (88), 2025 (91), 2026 (26)
- **Versions named:** 3.1 (99), 3.0 (38), 4.0 (32), 5.0 (13), 3.1.1 (8), 3.1.2 (7), 2.1 (4), 3.1.3 (3), 4.0.1 (3), 3.0.8 (3)
- **Pipeline stages it appears in:** structure determination (97), alignment/mapping (44), registration (39), dimensionality reduction/clustering (20), differential/statistical testing (16), visualisation (4), normalisation (3), machine learning (2), quantification (1), quality control (1)

## Papers

### The epitope arrangement on flavivirus particles contributes to Mab C10's extraordinary neutralization breadth across Zika and dengue viruses. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.010 | PMCID: PMC8724787 | PMID: 34852239
- Version used: **2.1**
- Evidence: ...2018 http://molprobity.biochem.duke.edu/ Prism GraphPad Version 7.0h Astra 6 Wyatt Technology Corp https://www.wyatt.com/products/software/astra.html Relion 2.1 Scheres, 2012 https://www3.mrc-lmb.cam.ac.uk/relion/ Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulfilled by the Lead Contact, Félix Rey ( felix.rey@past...
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [CCP4, ChimeraX v1.2.5, PHENIX v1.14, PyMOL, RELION v2.1, UCSF Chimera v1.11.2]

### De novo identification of mammalian ciliary motility proteins using cryo-EM. (Cell 2021)

- DOI: 10.1016/j.cell.2021.10.007 | PMCID: PMC8595878 | PMID: 34715025
- Version used: **3.1**
- Evidence: Image processing All image processing was performed using RELION 3.1 ( Zivanov et al., 2018 ) unless otherwise stated.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX, Coot v0.9, ImageJ v1.44d, RELION v3.1]

### Selective activation of PFKL suppresses the phagocytic oxidative burst. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.004 | PMCID: PMC8802628 | PMID: 34320407
- Evidence: Particles from selected 2D classes were then exported to Relion ( Scheres, 2012 ) for 3D auto-refinement and 3D classification.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [RELION] -> stage not stated [PHENIX, R v3.5.0]

### Bacterial Vipp1 and PspA are members of the ancient ESCRT-III membrane-remodeling superfamily. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.041 | PMCID: PMC8281802 | PMID: 34166615
- Version used: **3.1**
- Evidence: ...mafft trimAl 1.3 Capella-Gutiérrez et al., 2009 http://trimal.cgenomics.org/ IQ-Tree 1.6.10 Nguyen et al., 2015 http://www.iqtree.org/release/v1.6.10 Relion 3.1 Scheres, 2012 https://www3.mrc-lmb.cam.ac.uk/relion/index.php?title=Main_Page I-Tasser Zhang, 2008 https://zhanglab.dcmb.med.umich.edu/I-TASSER/ COOT Emsley et al., 2010 https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Rosetta Wang et...
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE, MotionCor2] -> stage not stated [GROMACS, HMMER, ImageJ, PHENIX, RELION v3.1, VMD]

### In vitro and in vivo functions of SARS-CoV-2 infection-enhancing and neutralizing antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.021 | PMCID: PMC8232969 | PMID: 34242577
- Evidence: ...AS Institute NA Cloanalyst Program ( Kepler et al., 2014 ) NA Biacore S200 Evaluation software Cytiva NA Coot ( Emsley et al., 2010 ) Version 0.8.9.2 Relion ( Scheres, 2012 ; Scheres, 2016 ) Version 3.1 Phenix ( Afonine et al., 2018 ; Liebschner et al., 2019 ) Version 1.17 UCSF Chimera ( Pettersen et al., 2004 ) http://www.cgl.ucsf.edu/chimera/ ISOLDE ( Croll, 2018 ) Version 1.1 Chimera X ( Goddar...
- Full pipeline: stage not stated [CTFFIND, ChimeraX, Coot, PHENIX, PyMOL, RELION, UCSF Chimera]

### Coupling of N7-methyltransferase and 3'-5' exoribonuclease with SARS-CoV-2 polymerase reveals mechanisms for capping and proofreading. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.033 | PMCID: PMC8142856 | PMID: 34143953
- Version used: **3.0**
- Evidence: ...are and algorithms SerialEM Mastronarde, 2005 https://bio3d.colorado.edu/SerialEM MotionCor2 Zheng et al., 2017 https://emcore.ucsf.edu/ucsf-software RELION 3.0 Scheres, 2012 https://www3.mrc-lmb.cam.ac.uk/relion/ cryoSPARC Punjani et al., 2017 https://cryosparc.com/ UCSF Chimera Pettersen et al., 2004 https://www.cgl.ucsf.edu/chimera COOT Emsley et al., 2010 https://www.cgl.ucsf.edu/chimera PHENI...
- Full pipeline: structure determination [Coot] -> stage not stated [MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Fab-dimerized glycan-reactive antibodies are a structural category of natural antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.042 | PMCID: PMC8135257 | PMID: 34019795
- Evidence: The RELION program was used for CTF correction, automatic particle picking and 2D class averaging of the single-particle images.
- Full pipeline: alignment/mapping [MotionCor2] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX, R, Seurat, UMAP] -> stage not stated [PyMOL, RELION, UCSF Chimera, ggplot2]

### Structural insight into SARS-CoV-2 neutralizing antibodies and modulation of syncytia. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.033 | PMCID: PMC8064868 | PMID: 33974910
- Version used: **3.1**
- Evidence: ForteBio N/A Biacore T200 Evaluation Software Cytiva Life Sciences N/A cryoSPARC v2.7-3.1 Structura Biotechnology https://cryosparc.com/ Relion 3.1 Laboratory of Molecular Biology, Medical Research Council https://github.com/3dem/relion UCSF ChimeraX 1.1 UCSF https://www.cgl.ucsf.edu/chimerax/ ISOLDE 1.1.0 Cambridge Institute for Medical Research https://isolde.cimr.cam.ac.uk/ Coot 0.9.4.1 Laborat...
- Full pipeline: simulation/modelling [PHENIX] -> machine learning [PHENIX] -> stage not stated [ChimeraX v1.1, RELION v3.1, UCSF Chimera]

### The molecular basis for sarcomere organization in vertebrate skeletal muscle. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.047 | PMCID: PMC8054911 | PMID: 33765442
- Evidence: These segments were extracted from unbinned and 2x binned tomograms with a box size of 128 pixels (450 Å) using RELION ( Bharat and Scheres, 2016 ).
- Full pipeline: visualisation [R] -> stage not stated [EMAN2, Fiji, IMOD, ImageJ, RELION, TrackMate]

### N-terminal domain antigenic mapping reveals a site of vulnerability for SARS-CoV-2. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.028 | PMCID: PMC7962585 | PMID: 33761326
- Version used: **3.0**
- Evidence: ...FX PCR DNA and Gel Band Purification Kit Cytiva Cat# 28903470 Software and Algorithms cryoSPARC v3.0.1 ( Punjani et al., 2017 ) https://cryosparc.com Relion v3.0 ( Zivanov et al., 2018 ) https://www3.mrc-lmb.cam.ac.uk/relion Coot ( Casañal et al., 2019 ) https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix-Refine ( Adams et al., 2010 ) https://www.phenix-online.org/download/ Phenix-Phaser ...
- Full pipeline: structure determination [PHENIX, RELION v3.0] -> visualisation [ChimeraX] -> stage not stated [Pangolin, UCSF Chimera]

### Simultaneous binding of Guidance Cues NET1 and RGM blocks extracellular NEO1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.045 | PMCID: PMC8063088 | PMID: 33740419
- Version used: **3.1**
- Evidence: ...tt https://www.wyatt.com/products/software/astra.html EPU FEI https://www.fei.com/software/epu-automated-single-particles-software-for-life-sciences/ RELION 3.1 ( Zivanov et al., 2018 ) https://www3.mrc-lmb.cam.ac.uk/relion/index.php/Main_Page cryoSPARC ( Punjani et al., 2017 ) https://cryosparc.com CTFFIND 4.1 ( Rohou and Grigorieff, 2015 ) https://grigoriefflab.umassmed.edu/ctffind4 UCSF Chimera...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [MotionCor2] -> stage not stated [CTFFIND v4.1, Clustal Omega, ImageJ, PHENIX, PyMOL, RELION v3.1, UCSF Chimera]

### Extremely potent human monoclonal antibodies from COVID-19 convalescent patients. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.035 | PMCID: PMC7901298 | PMID: 33667349
- Version used: **3.0**
- Evidence: Raw micrographs were stored in the Appion database ( Lander et al., 2009 ), particles were picked with DoGPicker ( Voss et al., 2009 ), and 2D and 3D classification and refinements were performed in RELION 3.0 ( Scheres, 2012 ).
- Full pipeline: quality control [FastQC, MultiQC v1.9, Trimmomatic v0.39] -> read trimming [FastQC, MultiQC v1.9, NumPy, Python v3.7.4, Trimmomatic v0.39] -> structure determination [RELION v3.0] -> visualisation [Matplotlib, seaborn] -> stage not stated [UCSF Chimera]

### The antigenic anatomy of SARS-CoV-2 receptor binding domain. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.032 | PMCID: PMC7891125 | PMID: 33756110
- Version used: **3.1**
- Evidence: Two-times binned movies were then motion corrected and aligned on the fly using Relion(3.1) scheduler ( Zivanov et al., 2018 ) with a 5 × 5 patch based alignment.
- Full pipeline: alignment/mapping [RELION v3.1] -> registration [RELION v3.1] -> stage not stated [PHENIX, PyMOL]

### Cryo-EM Structure of an Extended SARS-CoV-2 Replication and Transcription Complex Reveals an Intermediate State in Cap Synthesis. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.016 | PMCID: PMC7666536 | PMID: 33232691
- Version used: **3.0**
- Evidence: ...Algorithms SerialEM ( Mastronarde, 2005 ) https://bio3d.colorado.edu/SerialEM MotionCor2 ( Zheng et al., 2017 ) https://emcore.ucsf.edu/ucsf-software RELION 3.0 ( Scheres, 2012 ) https://www3.mrc-lmb.cam.ac.uk/relion cryoSPARC ( Punjani et al., 2017 ) https://cryosparc.com/ UCSF Chimera ( Pettersen et al., 2004 ) https://www.cgl.ucsf.edu/chimera COOT ( Emsley et al., 2010 ) https://www.cgl.ucsf.ed...
- Full pipeline: structure determination [Coot] -> stage not stated [ImageJ, MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Structural basis for the assembly of the type V CRISPR-associated transposon complex. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.009 | PMCID: PMC9798831 | PMID: 36435179
- Version used: **3.1.2**
- Evidence: ...0.1519REL ThermoFisher Scientific https:// www.thermofisher.com/ch/en/home/electron-microscopy/products/software-em-3d-vis/epu-software.html#features RELION 3.1.2 Scheres, 2012 42 https://relion.readthedocs.io/en/release-3.1/ SPHIRE version 1.3 Moriya et al., 2017 43 https://sphire.mpg.de/wiki/doku.php cryoSPARC 3.2.0 Punjani et al., 2017 44 https://cryosparc.com/ MotionCor2 1.4.0 Zheng et al., 20...
- Full pipeline: stage not stated [CTFFIND v1.06, ChimeraX v1.2, Coot, MotionCor2 v1.4.0, PHENIX v1.19.1, RELION v3.1.2, UCSF Chimera v1.14]

### A mechanism for SARS-CoV-2 RNA capping and its inhibition by nucleotide analog inhibitors. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.037 | PMCID: PMC9531661 | PMID: 36335936
- Version used: **3.0**
- Evidence: ...nd algorithms SerialEM Mastronarde, 2005 http://bio3d.colorado.edu/SerialEM MotionCor2 ( Zheng et al., 2017 ) https://emcore.ucsf.edu/ucsf-motioncor2 RELION 3.0 Scheres, 2012 https://www2.mrc-lmb.cam.ac.uk/relion cryoSPARC Punjani et al., 2017 https://cryosparc.com/ UCSF Chimera Pettersen et al., 2004 https://www.cgl.ucsf.edu/chimera COOT Emsley et al., 2010 https://www.cgl.ucsf.edu/chimera PHENIX...
- Full pipeline: stage not stated [MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### BacPROTACs mediate targeted protein degradation in bacteria. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.009 | PMCID: PMC9240326 | PMID: 35662409
- Version used: **3.0**
- Evidence: ...( Zheng et al., 2017 ) https://emcore.ucsf.edu/ucsf-software Gctf 1.06 ( Zhang, 2016 ) N/A crYOLO v1.3.5 ( Wagner et al., 2019 ) http://sphire.mpg.de RELION 3.0 ( Zivanov et al., 2018 ) N/A Coot ( Emsley et al., 2010 ) https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix ( Afonine et al., 2018 ), ( Liebschner et al., 2019 ) https://phenix-online.org/ MolProbity ( Williams et al., 2018 ) ht...
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX, Coot, MotionCor2 v1.0.5, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Structure, receptor recognition, and antigenicity of the human coronavirus CCoV-HuPn-2018 spike glycoprotein. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.019 | PMCID: PMC9135795 | PMID: 35700730
- Version used: **3.0**
- Evidence: ... Fitzgerald 88R-P002 Human red blood cells Rockland R407-0050 Software and algorithms cryoSPARC v3.0.1 ( Punjani et al., 2017 ) https://cryosparc.com Relion v3.0 ( Zivanov et al., 2018 ) https://www3.mrc-lmb.cam.ac.uk/relion Coot ( Emsley et al., 2010 ) https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix-Refine ( Liebschner et al., 2019 ) https://www.phenix-online.org/download/ Phenix-Pha...
- Full pipeline: structure determination [PHENIX, RELION v3.0] -> stage not stated [ChimeraX, UCSF Chimera]

### Protective prototype-Beta and Delta-Omicron chimeric RBD-dimer vaccines against SARS-CoV-2. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.029 | PMCID: PMC9042943 | PMID: 35568034
- Evidence: The subsequent image processing and reconstruction were performed using Relion-3.1 ( Zivanov et al., 2018 ) and cryoSPARC ( Punjani et al., 2017 ).
- Full pipeline: structure determination [RELION] -> stage not stated [MotionCor2]

### Broad neutralization of SARS-CoV-2 variants by an inhalable bispecific single-domain antibody. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.009 | PMCID: PMC8907017 | PMID: 35344711
- Version used: **3.0**
- Evidence: ...at# 63891 pSecTag2B expression vector ThermoFisher Cat# V90020 Software and algorithms UCSF Chimera UCSF Software N/A DeepEMhancer python package N/A RELION v3.0 https://www3.mrc-lmb.cam.ac.uk/relion//index.php/Download_&_install N/A COOT https://www2.mrc-lmb.cam.ac.uk/Personal/pemsley/coot N/A cryoSPARC Structura Biotechnology Inc.
- Full pipeline: stage not stated [CTFFIND, ChimeraX, MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Cryo-ET of Env on intact HIV virions reveals structural variation and positioning on the Gag lattice. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.013 | PMCID: PMC9000915 | PMID: 35123651
- Version used: **2.1**
- Evidence: ...3d.colorado.edu/SerialEM/ Motioncor2 UCSF https://emcore.ucsf.edu/ucsf-software IMOD 4.10.15 ( Kremer et al., 1996 ) https://bio3d.colorado.edu/imod/ Relion 2.1 ( Bharat and Scheres, 2016 ; Scheres, 2012 ) https://www3.mrc-lmb.cam.ac.uk/relion/index.php/Main_Page PEET 1.12 ( Nicastro et al., 2006 ) https://bio3d.colorado.edu/PEET/ EMAN2 ( Chen et al., 2019 ) https://blake.bcm.edu/emanwiki/EMAN2/e2...
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ChimeraX, Coot, EMAN2, IMOD v4.10.15, ImageJ, RELION v2.1, UCSF Chimera]

### Structural and functional characterizations of infectivity and immune evasion of SARS-CoV-2 Omicron. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.019 | PMCID: PMC8786603 | PMID: 35120603
- Version used: **3.07**
- Evidence: ... igraph (1.2.5) N/A https://cran.r-project.org/web/packages/ igraph/index.html Gctf program (v1.06) N/A https://www2.mrc-lmb.cam.ac.uk/download/gctf/ RELION (v3.07) Zivanov et al., 2018 https://www2.mrc-lmb.cam.ac.uk/relion UCSF Chimera N/A https://www.cgl.ucsf.edu/chimera UCSF ChimeraX N/A https://www.rbvi.ucsf.edu/chimerax/ PHENIX N/A https://www.phenix-online.org Coot N/A https://www2.mrc-lmb.c...
- Full pipeline: structure determination [Coot] -> stage not stated [CTFFIND, ChimeraX, MotionCor2, PHENIX, RELION v3.07, UCSF Chimera, igraph v1.2.5]

### Receptor binding and complex structures of human ACE2 to spike RBD from omicron and delta SARS-CoV-2. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.001 | PMCID: PMC8733278 | PMID: 35093192
- Evidence: A set of ∼150,000 particles were auto-picked by Laplacian-of-Gaussian from RELION-3.1 ( Zivanov et al., 2018 ) and then subjected to 2D classification to generate templates for auto-picking against the entire dataset.
- Full pipeline: stage not stated [MotionCor2, PHENIX, PyMOL, RELION]

### Comprehensive structure and functional adaptations of the yeast nuclear pore complex. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.015 | PMCID: PMC8928745 | PMID: 34982960
- Version used: **2.0**
- Evidence: For initial screening, particles were extracted in 310 × 310 boxes with a pixel size of 5.32 Å to remove outliers with 2D and 3D Maximum likelihood-based classification in RELION 2.0 ( Scheres; 2012 ), which resulted in 26049 selected NPCs.
- Full pipeline: registration [IMOD] -> simulation/modelling [PHENIX] -> structure determination [PHENIX] -> stage not stated [Coot, EMAN2, ImageJ, RELION v2.0]

### Structural evolution of fibril polymorphs during amyloid assembly. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.025 | PMCID: PMC7617692 | PMID: 38134875
- Evidence: The raw EER movies were fractionated, aligned and summed using motion correction in RELION-4 66 with a dose per frame of 1.0, 1.1, 1.4 and 1.0 e - /Å 2 for the 3 week (FT24), 3 week (FT14), 6 week (FT11) and 22 week (FT14) datasets respectively.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND v4.16, ChimeraX, Conda, PyMOL]

### De novo protein identification in mammalian sperm using in situ cryoelectron tomography and AlphaFold2 docking. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.017 | PMCID: PMC10842264 | PMID: 37865089
- Evidence: 54 https://www.rbvi.ucsf.edu/chimerax/ RELION-4.0 Zivanov et al.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler v4.4.1] -> differential/statistical testing [Bioconductor] -> visualisation [IMOD] -> stage not stated [AlphaFold, ChimeraX, ColabFold, Coot v0.9.8.1, MotionCor2, R, RELION, UCSF Chimera]

### Molecular basis of anaphylatoxin binding, activation, and signaling bias at complement receptors. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.020 | PMCID: PMC7615941 | PMID: 37852260
- Version used: **3.1.2**
- Evidence: Processing of the collected dataset was performed with Relion 3.1.2 61 – 63 where almost 10,000 particles were autopicked and subjected to reference free 2D classification, generating the 2D class averages.
- Full pipeline: stage not stated [ChimeraX, MACS2, PHENIX, RELION v3.1.2, UCSF Chimera]

### Structural basis for ion selectivity in potassium-selective channelrhodopsins. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.009 | PMCID: PMC7615185 | PMID: 37652010
- Version used: **4.0**
- Evidence: 85 https://emcore.ucsf.edu/ucsf-software RELION 4.0 Zivanov et al.
- Full pipeline: structure determination [AlphaFold, Coot, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Kilosort v2.5, MotionCor2, RELION v4.0, UCSF Chimera]

### TMEM106B is a receptor mediating ACE2-independent SARS-CoV-2 cell entry. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.005 | PMCID: PMC10409496 | PMID: 37421949
- Version used: **4.0**
- Evidence: 91 https://github.com/rsanchezgarc/micrograph_cleaner_em Relion (v4.0) Scheres et al.
- Full pipeline: quantification [ImageJ] -> structure determination [Coot] -> machine learning [Topaz] -> stage not stated [AlphaFold, CTFFIND v1.06, PHENIX, RELION v4.0, UCSF Chimera]

### Structure of the endosomal Commander complex linked to Ritscher-Schinzel syndrome. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.003 | PMCID: PMC10187114 | PMID: 37172566
- Evidence: 47 N/A Deposited data Commd5-10-7-9 complex (crystal structure) RCSB Protein DataBank (this study) PDB: 8ESD VPS29-VPS35L peptide complex (crystal structure) RCSB Protein DataBank (this study) PDB: 8ESE CCC complex (cryoEM structure; RELION map) RCSB Protein DataBank (this study) PDB: 8F2R CCC complex (cryoEM structure; CryoSPARC map) RCSB Protein DataBank (this study) PDB: 8F2U CCC complex (cryoE...
- Full pipeline: alignment/mapping [ColabFold, MAFFT, PyMOL] -> normalisation [CCP4] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, HMMER v3.3.2, PHENIX, RELION, Topaz]

### Molecular mechanisms of stress-induced reactivation in mumps virus condensates. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.015 | PMCID: PMC10156176 | PMID: 37116470
- Version used: **3.0**
- Evidence: 83 N/A AV3 Forster and Hegerl 84 N/A RELION 3.0 and 3.1 Zivanov et al.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [Bioconductor] -> structure determination [Coot, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, BWA v0.7.17, ChimeraX v1.1.1, IMOD, PHENIX v1.18, Picard, R v3.6, RELION v3.0, freebayes v1.1.0, limma]

### Systemwide disassembly and assembly of SCF ubiquitin ligase complexes. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.035 | PMCID: PMC10156175 | PMID: 37028429
- Version used: **3.1**
- Evidence: 68 https://imagej.net Prism v5 and 9; GraphPad https://www.graphpad.com/scientific-software/prism/ RELION v3.1 Zivanov et al.
- Full pipeline: structure determination [PHENIX] -> stage not stated [CTFFIND v4.1, ChimeraX v1.2, ImageJ, MotionCor2 v1.1, PyMOL v2.3.3, RELION v3.1, UCSF Chimera]

### A trailing ribosome speeds up RNA polymerase at the expense of transcript fidelity via force and allostery. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.008 | PMCID: PMC10135430 | PMID: 36931247
- Version used: **3.1**
- Evidence: Data Processing The processing of the cryo-EM data was performed using RELION 3.1 168 , 169 and cryoSPARC v3.1.0 170 , 171 as detailed in Data S1 .
- Full pipeline: alignment/mapping [ChimeraX, MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, PyMOL v1.6, RELION v3.1]

### Cryo-EM structure of gas vesicles for buoyancy-controlled motility. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.041 | PMCID: PMC9994262 | PMID: 36868215
- Version used: **3.1**
- Evidence: 27 https://swissmodel.expasy.org/ RELION 3.1 Zivanov et al.
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX v1.4, ColabFold, HMMER, ImageJ, PHENIX v1.13, RELION v3.1, SciPy]

### Discovery of natural-product-derived sequanamycins as potent oral anti-tuberculosis agents. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.043 | PMCID: PMC9994261 | PMID: 36827973
- Evidence: 42 http://www.phenix-online.org/ Relion Scheres 43 https://relion.readthedocs.io/en/release-3.1/ MotionCor2 Zheng et al.
- Full pipeline: stage not stated [CTFFIND, MotionCor2, PHENIX, PyMOL, RELION]

### Cryo-EM structure of the RADAR supramolecular anti-phage defense complex. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.012 | PMCID: PMC9994260 | PMID: 36764290
- Evidence: Following multiple rounds of 2D classification in RELION 46 to remove erroneous picks, contamination, and “junk” particles 1,578,051 particles representing intact RdrA were obtained.
- Full pipeline: quality control [RELION] -> normalisation [MotionCor2 v1.3.1] -> registration [MotionCor2 v1.3.1] -> stage not stated [ImageJ, PHENIX v1.13]

### A potent pan-sarbecovirus neutralizing antibody resilient to epitope diversification. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.026 | PMCID: PMC11645210 | PMID: 39383863
- Evidence: 92 Particles from the NUR were transferred from cryoSPARC to Relion using the pyem program package ( https://github.com/asarnow/pyem ) 93 and subjected to the Bayesian polishing procedure 94 in Relion 95 , 96 during which particles were re-extracted with a box size of 512 pixels and a pixel size of 1.0 Å.
- Full pipeline: read trimming [BCFtools v1.10.2, BWA v0.7.17] -> differential/statistical testing [RELION, scikit-learn] -> structure determination [Coot, PHENIX, Topaz] -> machine learning [Topaz, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [OpenMM, Pangolin, Python v3.10]

### Structural insights into the diversity and DNA cleavage mechanism of Fanzor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.050 | PMCID: PMC11423790 | PMID: 39208796
- Version used: **4.0**
- Evidence: Cryo-EM data processing Image processing was performed on CryoSPARC v4.2.0 32 and RELION 4.0 33 .
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX v1.7, PHENIX v1.18] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, RELION v4.0, UCSF Chimera v1.16]

### The molecular architecture of the nuclear basket. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.020 | PMCID: PMC11416316 | PMID: 39127037
- Evidence: A small number of pore particles were used to generate a C8 symmetrized initial model in Relion.
- Full pipeline: stage not stated [ChimeraX, EMAN2, IMOD, RELION]

### Molecular mechanism of distinct chemokine engagement and functional divergence of the human Duffy antigen receptor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.005 | PMCID: PMC11349380 | PMID: 39089252
- Version used: **4.0**
- Evidence: Arun K Shukla, 88 IIT Kanpur N/A Software and algorithms Relion3.1.2, Relion3.1.3, Relion 4.0 and Relion 5.0-beta Zivanov et al.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> registration [MotionCor2] -> visualisation [R v3.7] -> stage not stated [AlphaFold, ChimeraX, PHENIX, RELION v4.0, UCSF Chimera]

### Extensive structural rearrangement of intraflagellar transport trains underpins bidirectional cargo transport. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.041 | PMCID: PMC11349379 | PMID: 39067443
- Evidence: 64 http://www.warpem.com/warp/ Relion V3.1.3 Zivanov et al.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2, RELION]

### Human coronavirus HKU1 recognition of the TMPRSS2 host receptor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.006 | PMCID: PMC12854727 | PMID: 38964328
- Evidence: After two rounds of heterogeneous refinements and removal of junk particles, 3D refinement was carried out using non-uniform refinement with per-particle defocus refinement in cryoSPARC 104 and the particles were transferred from cryoSPARC to Relion using pyem ( https://github.com/asarnow/pyem ) to be subjected to the Bayesian polishing procedure implemented in Relion 105 during which particles we...
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [RELION] -> structure determination [RELION, UCSF Chimera] -> stage not stated [PHENIX, Topaz]

### Molecular basis for shifted receptor recognition by an encephalitic arbovirus. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.029 | PMCID: PMC12406711 | PMID: 40187345
- Version used: **3.1**
- Evidence: 65 For the WEEV CBA87 VLP in complex with Hs PCDH10 EC1 -Fc, a total 22,075 particles were auto-picked from 7,749 micrographs using crYOLO (version 1.8.2), 62 and particles were extracted with binned two times (pixel size 2.12 Å) in RELION 3.1 (version 3.1.4).
- Full pipeline: structure determination [ChimeraX, Coot v0.9.8.91, PHENIX v1.21r, UCSF Chimera v1.6.1] -> stage not stated [AlphaFold, CTFFIND, MotionCor2 v1.6.4, PyMOL v3.0.2, RELION v3.1]

### Mechanism of DNA capture by the MukBEF SMC complex and its inhibition by a viral DNA mimic. (Cell 2025)

- DOI: 10.1016/j.cell.2025.02.032 | PMCID: PMC7617805 | PMID: 40168993
- Evidence: 76 https://phenix-online.org RELION v5 Scheres 77 https://relion.readthedocs.io/en/release-5/ cryoSPARC v4 https://cryosparc.com/ Fiji Schindelin et al.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [AlphaFold, ChimeraX, MAFFT, PHENIX, RELION]

### Multiple independent acquisitions of ACE2 usage in MERS-related coronaviruses. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.031 | PMCID: PMC12360793 | PMID: 39922191
- Evidence: ...as carried out using non-uniform refinement with per-particle defocus refinement in cryoSPARC 83 and the particles were transferred from cryoSPARC to Relion using pyem ( https://github.com/asarnow/pyem ) to be subjected to the Bayesian polishing procedure implemented in Relion 84 during which particles were re-extracted with a box size of 320 pixels and a pixel size of 1.0 Å.
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [RELION] -> structure determination [IQ-TREE, RELION, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PHENIX, Topaz]

### Structural and functional analysis of the Nipah virus polymerase complex. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.021 | PMCID: PMC11813165 | PMID: 39837328
- Version used: **3.1.1**
- Evidence: 56 https://emcore.ucsf.edu/cryoem-software , RRID: SCR_016499 CTFFind4 4.1.14 Rohou and Grigorieff 57 http://grigoriefflab.janelia.org/ctffind4 , RRID: SCR_016732 Relion 3.1.1 Zivanov et al.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.5, Clustal Omega, Coot v0.9, MotionCor2 v1.6.4, PHENIX v1.20.1, PyMOL v2.5.5, RELION v3.1.1, UCSF Chimera v1.15]

### The unique architecture of umbrella toxins permits a two-tiered molecular bet-hedging strategy for interbacterial antagonism. (Cell 2026)

- DOI: 10.1016/j.cell.2025.10.044 | PMCID: PMC13274773 | PMID: 41338195
- Version used: **5.0**
- Evidence: 56 https://www.cgl.ucsf.edu/chimerax/ ; Relion v5.0 Zivanov et al.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.8, HMMER, ImageJ, RELION v5.0, UCSF Chimera]

### The structure of neurofibromin isoform 2 reveals different functional states. (Nature 2021)

- DOI: 10.1038/s41586-021-04024-x | PMCID: PMC8580823 | PMID: 34707296
- Version used: **3.1.1**
- Evidence: Particles were converted into a STAR file and input into RELION v3.1.1 (ref.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX v1.19, UCSF Chimera v1.15] -> stage not stated [ChimeraX, MotionCor2 v2.1.1, RELION v3.1.1]

### Structure of Venezuelan equine encephalitis virus in complex with the LDLRAD3 receptor. (Nature 2021)

- DOI: 10.1038/s41586-021-03963-9 | PMCID: PMC8550936 | PMID: 34646020
- Evidence: Single-particle analysis, specifically reference-free 2D classification, 3D refinement, video refinement, Bayesian polishing, post-processing and local resolution estimation were performed using RELION-3.1 (ref.
- Full pipeline: differential/statistical testing [RELION] -> structure determination [PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, MotionCor2]

### The cellular environment shapes the nuclear pore complex architecture. (Nature 2021)

- DOI: 10.1038/s41586-021-03985-3 | PMCID: PMC8550940 | PMID: 34646014
- Evidence: Subprotomer volumes were B -factor sharpened using Relion 49 with a B -factor of −2,000 Å 2 .
- Full pipeline: alignment/mapping [IMOD] -> differential/statistical testing [Matplotlib, Python, SciPy] -> stage not stated [RELION, UCSF Chimera]

### Structural basis of gating modulation of Kv4 channel complexes. (Nature 2021)

- DOI: 10.1038/s41586-021-03935-z | PMCID: PMC8566240 | PMID: 34552243
- Version used: **3.0**
- Evidence: Data were processed and structures were determined with RELION v.3.0 or 3.1.
- Full pipeline: stage not stated [RELION v3.0, UCSF Chimera v1.14]

### Structural basis of human transcription-DNA repair coupling. (Nature 2021)

- DOI: 10.1038/s41586-021-03906-4 | PMCID: PMC8514338 | PMID: 34526721
- Version used: **3.0**
- Evidence: Initial 2D classification and 3D classification steps were done in CryoSPARC 50 , followed by further processing in RELION 3.0 (refs 51 – 53 ).
- Full pipeline: quantification [ImageJ] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, ImageJ] -> stage not stated [RELION v3.0, UCSF Chimera]

### Structural insights into how Prp5 proofreads the pre-mRNA branch site. (Nature 2021)

- DOI: 10.1038/s41586-021-03789-5 | PMCID: PMC8357632 | PMID: 34349264
- Version used: **3.0**
- Evidence: They were then extracted with a box size of 440 × 440 pixels, and binned to 110 × 110 pixels (pixel size of 4.64 Å) in RELION 3.0 ( http://www2.mrc-lmb.cam.ac.uk/relion/index.php/Main_Page ).
- Full pipeline: structure determination [PHENIX v1.13] -> stage not stated [CTFFIND, ChimeraX v1.1, Coot v0.8.9.2, RELION v3.0, UCSF Chimera v1.13.1]

### The structural basis of odorant recognition in insect olfactory receptors. (Nature 2021)

- DOI: 10.1038/s41586-021-03794-8 | PMCID: PMC8410599 | PMID: 34349260
- Version used: **3.0**
- Evidence: Movie frames were aligned and binned over 2 × 2 pixels using MotionCor2 40 implemented in Relion 3.0 41 , and the contrast transfer function parameters for each motion-corrected image were estimated using CTFFIND4 42 .
- Full pipeline: alignment/mapping [MAFFT, MotionCor2, RELION v3.0] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [scikit-learn] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, PyMOL]

### Structural basis of early translocation events on the ribosome. (Nature 2021)

- DOI: 10.1038/s41586-021-03713-x | PMCID: PMC8318882 | PMID: 34234344
- Evidence: CTF parameters were determined using CTFFind4 56 and refined later in Relion 57 (v.3.1) and cryoSPARC 58 (v.3).
- Full pipeline: normalisation [UCSF Chimera] -> registration [MotionCor2] -> differential/statistical testing [UCSF Chimera] -> structure determination [Coot v0.9.4.1, PHENIX v1.19, RELION, UCSF Chimera] -> visualisation [ChimeraX]

### Structure and dynamics of a mycobacterial type VII secretion system. (Nature 2021)

- DOI: 10.1038/s41586-021-03517-z | PMCID: PMC8131196 | PMID: 33981042
- Evidence: This map was refined using the default Relion value ‘--tau2fudge 2’ but also ‘--tau2fudge 4’, which increased the overall connectivity of the lower cytosolic area.
- Full pipeline: structure determination [ChimeraX v1.0, RELION] -> visualisation [PyMOL v2.40] -> stage not stated [MotionCor2, PHENIX]

### Structural basis of GABA<sub>B</sub> receptor-G<sub>i</sub> protein coupling. (Nature 2021)

- DOI: 10.1038/s41586-021-03507-1 | PMCID: PMC8222003 | PMID: 33911284
- Version used: **3.1**
- Evidence: Cryo-EM data processing was performed using Relion 3.1 40 and CryoSPARC 2.15 41 .
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, RELION v3.1]

### Structural and biochemical mechanisms of NLRP1 inhibition by DPP9. (Nature 2021)

- DOI: 10.1038/s41586-021-03320-w | PMCID: PMC8081665 | PMID: 33731929
- Version used: **3.1**
- Evidence: On the basis of the CTF estimation, 7,033 and 4,667 micrographs were manually selected for rNLRP1–rDPP9 and rNLRP1 FIIND–CARD(S969A)–rDPP9, respectively, and were further processed in Relion 3.1.
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [MotionCor2, PHENIX] -> stage not stated [ImageJ, RELION v3.1]

### Ubiquitin ligation to F-box protein targets by SCF-RBR E3-E3 super-assembly. (Nature 2021)

- DOI: 10.1038/s41586-021-03197-9 | PMCID: PMC7904520 | PMID: 33536622
- Version used: **3.00**
- Evidence: Data processing RELION 3.00 60 was used to align and dose-weight raw movie frames.
- Full pipeline: alignment/mapping [RELION v3.00] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [CTFFIND]

### Design of biologically active binary protein 2D materials. (Nature 2021)

- DOI: 10.1038/s41586-020-03120-8 | PMCID: PMC7855610 | PMID: 33408408
- Evidence: 49 Single-particle style image processing (including CTF estimation, particle picking, particle extraction, and two-dimensional alignment and averaging) was accomplishing using the Relion software package.
- Full pipeline: alignment/mapping [RELION] -> dimensionality reduction/clustering [RELION] -> stage not stated [CCP4, ImageJ v1.52d, NumPy]

### Structure of the class D GPCR Ste2 dimer coupled to two G proteins. (Nature 2021)

- DOI: 10.1038/s41586-020-2994-1 | PMCID: PMC7116888 | PMID: 33268889
- Evidence: Data processing and model building RELION-3.1 was used for all data processing unless specified otherwise 41 .
- Full pipeline: alignment/mapping [CCP4] -> registration [MotionCor2] -> simulation/modelling [GROMACS] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [RELION]

### Close relatives of MERS-CoV in bats use ACE2 as their functional receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-05513-3 | PMCID: PMC9734910 | PMID: 36477529
- Evidence: Well-defined partial particles were selected for initial model reconstruction in Relion 57 .
- Full pipeline: alignment/mapping [CTFFIND, Clustal Omega, MUSCLE] -> structure determination [Coot v0.9.4, PHENIX v1.19, RELION, UCSF Chimera v1.15] -> stage not stated [ChimeraX v1.1, MotionCor2 v1.3.0]

### Structural basis of tankyrase activation by polymerization. (Nature 2022)

- DOI: 10.1038/s41586-022-05449-8 | PMCID: PMC9712121 | PMID: 36418402
- Version used: **2.10**
- Evidence: Image processing Movies were processed using RELION (v2.10 and 3.08) 37 , 38 .
- Full pipeline: alignment/mapping [Clustal Omega, EMAN2 v2.31] -> quantification [ImageJ] -> normalisation [ImageJ] -> structure determination [PHENIX v1.18.2] -> visualisation [ChimeraX v1.3] -> stage not stated [CellProfiler, Coot, MotionCor2, RELION v2.10, UCSF Chimera v1.14]

### Structural basis of actin filament assembly and aging. (Nature 2022)

- DOI: 10.1038/s41586-022-05241-8 | PMCID: PMC9646518 | PMID: 36289337
- Evidence: The particles were then converted to be compatible with Relion 59 using sp_sphire2relion.py.
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX] -> stage not stated [Coot, RELION]

### Cryo-EM structure of the SEA complex. (Nature 2022)

- DOI: 10.1038/s41586-022-05370-0 | PMCID: PMC9646525 | PMID: 36289347
- Version used: **4.0**
- Evidence: Negative-stain data processing Data were processed using RELION v.4.0 (ref.
- Full pipeline: quantification [ImageJ v1.52p] -> structure determination [PHENIX v1.20.1] -> visualisation [ChimeraX v1.3] -> stage not stated [AlphaFold, Coot v0.9.8.1, RELION v4.0, UCSF Chimera v1.15]

### Bending forces and nucleotide state jointly regulate F-actin structure. (Nature 2022)

- DOI: 10.1038/s41586-022-05366-w | PMCID: PMC9646526 | PMID: 36289330
- Evidence: To select segments from the identified filaments for high-resolution helical reconstructions, a step size of three times the helical rise was used (83.4 Å), and segments that were members of the same filament were flagged in the output metadata (a RELION-formatted STAR file).
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [Python] -> differential/statistical testing [Matplotlib] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX, RELION] -> machine learning [TensorFlow, cryoDRGN] -> stage not stated [Coot, EMAN2, UCSF Chimera, scikit-image]

### Structure of the OMEGA nickase IsrB in complex with ωRNA and target DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05324-6 | PMCID: PMC9581776 | PMID: 36224386
- Evidence: To obtain the 3D reconstruction of complex A, data were processed using RELION-4.0 (ref.
- Full pipeline: alignment/mapping [MAFFT, MotionCor2] -> structure determination [ColabFold, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND, Python]

### Visualizing translation dynamics at atomic detail inside a bacterial cell. (Nature 2022)

- DOI: 10.1038/s41586-022-05255-2 | PMCID: PMC9534751 | PMID: 36171285
- Version used: **3.0**
- Evidence: For the Spc-treated dataset, template matching was performed in PyTom 57 , followed by computational classification in RELION 3.0 (refs.
- Full pipeline: alignment/mapping [MAFFT, eggNOG] -> dimensionality reduction/clustering [eggNOG] -> structure determination [Coot, PHENIX, Python v3.7.7] -> visualisation [ChimeraX] -> stage not stated [RELION v3.0]

### Structure of the Ebola virus polymerase complex. (Nature 2022)

- DOI: 10.1038/s41586-022-05271-2 | PMCID: PMC9517992 | PMID: 36171293
- Evidence: All subsequent classification and reconstruction procedures were performed using Relion-3.0 58 .
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [ImageJ] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold]

### Long-primed germinal centres with enduring affinity maturation and clonal migration. (Nature 2022)

- DOI: 10.1038/s41586-022-05216-9 | PMCID: PMC9491273 | PMID: 36131022
- Version used: **3.0**
- Evidence: Using Relion 3.0 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [UCSF Chimera v1.13] -> visualisation [UCSF Chimera v1.13] -> stage not stated [GSEA, RELION v3.0, Seurat, fgsea]

### A wheat resistosome defines common principles of immune receptor channels. (Nature 2022)

- DOI: 10.1038/s41586-022-05231-w | PMCID: PMC9581773 | PMID: 36163289
- Version used: **3.1**
- Evidence: Local resolution distribution was evaluated using RELION 3.1 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX v1.15, PHENIX v1.18.2] -> visualisation [ChimeraX v1.15] -> stage not stated [AlphaFold, RELION v3.1]

### Structural basis for directional chitin biosynthesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05244-5 | PMCID: PMC9556331 | PMID: 36131020
- Version used: **3.08**
- Evidence: All the processing steps were conducted in RELION 3.08 (ref.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2019.3] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, RELION v3.08]

### Structures of α-synuclein filaments from human brains with Lewy pathology. (Nature 2022)

- DOI: 10.1038/s41586-022-05319-3 | PMCID: PMC7613749 | PMID: 36108674
- Evidence: Helical reconstruction Movie frames were gain-corrected, aligned, dose-weighted and then summed into a single micrograph using RELION’s own motion correction program ( 58 ).
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [CTFFIND, Coot]

### Mechanism of AAA+ ATPase-mediated RuvAB-Holliday junction branch migration. (Nature 2022)

- DOI: 10.1038/s41586-022-05121-1 | PMCID: PMC9477746 | PMID: 36002576
- Version used: **3.0b**
- Evidence: Cryo-EM image processing and atomic model building Single-particle analyses were performed using Relion (v3.0b and v3.1) 58 , 59 .
- Full pipeline: simulation/modelling [ChimeraX v1.2.5] -> structure determination [ChimeraX v1.2.5, PHENIX] -> visualisation [PyMOL v2.4.1] -> stage not stated [RELION v3.0b, UCSF Chimera v1.13]

### The mechanism of RNA capping by SARS-CoV-2. (Nature 2022)

- DOI: 10.1038/s41586-022-05185-z | PMCID: PMC9492545 | PMID: 35944563
- Evidence: Image processing and 3D reconstruction Unless described otherwise, all datasets were processed with Relion 47 .
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX, RELION] -> stage not stated [CTFFIND, ImageJ]

### Architecture and self-assembly of the jumbo bacteriophage nuclear shell. (Nature 2022)

- DOI: 10.1038/s41586-022-05013-4 | PMCID: PMC9365700 | PMID: 35922510
- Evidence: A set of 400 particles were manually picked across the tomograms, extracted at 20 Å per pixel, and aligned in RELION-v3.1.1 to generate an initial reference 31 , 32 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [ChimeraX, MDTraj, PyMOL, VMD] -> structure determination [ChimeraX, PHENIX, PyMOL, VMD] -> visualisation [ChimeraX, PyMOL, VMD] -> stage not stated [UCSF Chimera]

### Structural insights into auxin recognition and efflux by Arabidopsis PIN1. (Nature 2022)

- DOI: 10.1038/s41586-022-05143-9 | PMCID: PMC9477737 | PMID: 35917925
- Version used: **3.1**
- Evidence: Motion correction and dose weighting were performed using the RELION 3.1 implementation of MotionCor2 43 , 44 .
- Full pipeline: registration [MotionCor2, RELION v3.1] -> structure determination [PHENIX]

### A DNA origami rotary ratchet motor. (Nature 2022)

- DOI: 10.1038/s41586-022-04910-y | PMCID: PMC9300469 | PMID: 35859200
- Version used: **3.0**
- Evidence: Cryo-EM image processing The image processing was performed in RELION 3.0 (refs.
- Full pipeline: registration [MotionCor2] -> stage not stated [RELION v3.0]

### Archaic chaperone-usher pili self-secrete into superelastic zigzag springs. (Nature 2022)

- DOI: 10.1038/s41586-022-05095-0 | PMCID: PMC9452303 | PMID: 35853476
- Version used: **3.0.8**
- Evidence: Image processing and helical reconstruction were performed in RELION (v.3.0.8) 32 .
- Full pipeline: quantification [ImageJ v1.53k] -> registration [MotionCor2 v1.2.3] -> structure determination [MotionCor2 v1.2.3, PHENIX v1.8.2, RELION v3.0.8, UCSF Chimera] -> stage not stated [CTFFIND v4.1.13, Coot v0.9.4]

### Cryo-EM structure of an active bacterial TIR-STING filament complex. (Nature 2022)

- DOI: 10.1038/s41586-022-04999-1 | PMCID: PMC9402430 | PMID: 35859168
- Evidence: 27 ) and RELION-3.1 (ref.
- Full pipeline: registration [MotionCor2 v1.4.0] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, RELION]

### Structure of the Dicer-2-R2D2 heterodimer bound to a small RNA duplex. (Nature 2022)

- DOI: 10.1038/s41586-022-04790-2 | PMCID: PMC9279153 | PMID: 35768503
- Evidence: The data were automatically collected by the image shift method using the SerialEM software 41 , with a defocus range of −1.6 to −0.8 μm, and 2,745 movies were obtained and processed using RELION-3.1.
- Full pipeline: structure determination [ChimeraX] -> stage not stated [AlphaFold, Clustal Omega, PHENIX, RELION]

### Structural insights into dsRNA processing by Drosophila Dicer-2-Loqs-PD. (Nature 2022)

- DOI: 10.1038/s41586-022-04911-x | PMCID: PMC9279154 | PMID: 35768513
- Version used: **3.1**
- Evidence: The following steps were then processed in RELION (v.3.1) 34 .
- Full pipeline: structure determination [PHENIX] -> stage not stated [RELION v3.1]

### A peroxisomal ubiquitin ligase complex forms a retrotranslocation channel. (Nature 2022)

- DOI: 10.1038/s41586-022-04903-x | PMCID: PMC9279156 | PMID: 35768507
- Version used: **3.1**
- Evidence: Particles were autopicked in Relion 3.1 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, REFMAC, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.1]

### Cryo-EM structure of a type IV secretion system. (Nature 2022)

- DOI: 10.1038/s41586-022-04859-y | PMCID: PMC9259494 | PMID: 35732732
- Version used: **3.1**
- Evidence: Structure determination Using RELION 3.1 52 , the 1,729,311 particles were re-extracted, re-centred and subjected to 3D refinement using the low pass filtered map mentioned above as initial model, with C14 symmetry applied.
- Full pipeline: registration [CTFFIND v4.1] -> simulation/modelling [Coot] -> structure determination [Coot, PHENIX v1.18.2, RELION v3.1] -> machine learning [AlphaFold] -> stage not stated [ChimeraX v1.1, HMMER, PyMOL v2.3.2]

### BA.2.12.1, BA.4 and BA.5 escape antibodies elicited by Omicron infection. (Nature 2022)

- DOI: 10.1038/s41586-022-04980-y | PMCID: PMC9385493 | PMID: 35714668
- Version used: **3.1**
- Evidence: To improve the density surrounding the RBD–Fab region, UCSF Chimera (v1.16) 54 and Relion (v3.1) 55 were used to generate the masks, and local refinement was then performed using cryoSPARC (v3.2.1).
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat] -> simulation/modelling [GROMACS] -> structure determination [PHENIX v1.20, RELION v3.1, UCSF Chimera v1.16] -> visualisation [ChimeraX v1.3, R, Seurat] -> stage not stated [Pangolin, ggplot2 v3.3.3, scikit-learn]

### Mechanism of replication origin melting nucleated by CMG helicase assembly. (Nature 2022)

- DOI: 10.1038/s41586-022-04829-4 | PMCID: PMC9242855 | PMID: 35705812
- Evidence: NS-EM image processing A subset of particles was manually picked using RELION-3.1 (ref.
- Full pipeline: structure determination [Coot v0.9.1] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [CTFFIND, PHENIX, RELION]

### Mechanism of mitoribosomal small subunit biogenesis and preinitiation. (Nature 2022)

- DOI: 10.1038/s41586-022-04795-x | PMCID: PMC9200640 | PMID: 35676484
- Version used: **3.0**
- Evidence: Beam-induced motion correction was performed for all datasets using RELION 3.0 (ref.
- Full pipeline: registration [RELION v3.0] -> differential/statistical testing [limma v3.34.9] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CCP4 v7.0, ChimeraX v0.91]

### Discovery of non-squalene triterpenes. (Nature 2022)

- DOI: 10.1038/s41586-022-04773-3 | PMCID: PMC9177416 | PMID: 35650436
- Evidence: The movie fractions were aligned, dose weighted and averaged using RELION’s own implementation on 5 × 5 tiled fractions with a B -factor of 300.
- Full pipeline: alignment/mapping [Clustal Omega v2.0.12, RELION] -> visualisation [PyMOL] -> stage not stated [AlphaFold, AutoDock Vina, CTFFIND, PHENIX v1.19.2, UCSF Chimera]

### Structural insights into the HBV receptor and bile acid transporter NTCP. (Nature 2022)

- DOI: 10.1038/s41586-022-04857-0 | PMCID: PMC9242859 | PMID: 35580630
- Evidence: All image processing was performed with RELION-3.1.1 28 .
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.2.1, PyMOL v2.3, UCSF Chimera v1.15] -> stage not stated [RELION]

### USP14-regulated allostery of the human proteasome by time-resolved cryo-EM. (Nature 2022)

- DOI: 10.1038/s41586-022-04671-8 | PMCID: PMC9117149 | PMID: 35477760
- Evidence: Reference-free 2D classification and 3D classification were carried out in software packages RELION 50 version 3.1 and ROME 51 .
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, Coot, EMAN2, MotionCor2, RELION]

### Opening of glutamate receptor channel to subconductance levels. (Nature 2022)

- DOI: 10.1038/s41586-022-04637-w | PMCID: PMC9068512 | PMID: 35444281
- Version used: **3.1**
- Evidence: Image processing The initial processing was carried out using Relion 3.1 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot v0.9.2] -> stage not stated [CTFFIND v1.06, PHENIX v1.18, RELION v3.1, UCSF Chimera v1.14, VMD v1.9.3]

### Structural basis of tethered agonism of the adhesion GPCRs ADGRD1 and ADGRF1. (Nature 2022)

- DOI: 10.1038/s41586-022-04580-w | PMCID: PMC9046087 | PMID: 35418679
- Version used: **3.1**
- Evidence: The particle projections were extracted by template-free auto-picking of RELION 3.1 42 .
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, ChimeraX v1.1, Coot, PHENIX] -> visualisation [PyMOL v1.8, UCSF Chimera v1.15] -> stage not stated [CTFFIND v1.18, RELION v3.1]

### Age-dependent formation of TMEM106B amyloid filaments in human brains. (Nature 2022)

- DOI: 10.1038/s41586-022-04650-z | PMCID: PMC9095482 | PMID: 35344985
- Evidence: Helical reconstruction Movie frames were gain corrected, aligned, dose weighted and then summed into a single micrograph using RELION’s own motion correction program 31 .
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [AlphaFold, CTFFIND, Coot]

### Activation mechanism of the class D fungal GPCR dimer Ste2. (Nature 2022)

- DOI: 10.1038/s41586-022-04498-3 | PMCID: PMC8942848 | PMID: 35296853
- Evidence: These particles were re-extracted in a box-size equivalent to 210 Å and subjected to 3D reconstruction in C1 symmetry followed by iterative rounds of Bayesian polishing, beam-tilt correction and per-particle CTF refinement in RELION-3.1.
- Full pipeline: registration [MotionCor2] -> differential/statistical testing [RELION] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, MotionCor2, PHENIX, RELION] -> visualisation [PyMOL] -> stage not stated [CTFFIND, UCSF Chimera]

### Memory B cell repertoire from triple vaccinees against diverse SARS-CoV-2 variants. (Nature 2022)

- DOI: 10.1038/s41586-022-04466-x | PMCID: PMC8967717 | PMID: 35090164
- Version used: **3.0**
- Evidence: Cryo-EM data processing A total of 3,752, 2,631, 3,955 and 5,014 micrographs of S–XGv265 complex, S–XGv282 complex, S–XGv289 complex and S–XGv347 complex, respectively were recorded and subjected to beam-induced motion correction using motionCorr in Relion 3.0 package 37 .
- Full pipeline: registration [RELION v3.0] -> simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND]

### Broadly neutralizing antibodies target a haemagglutinin anchor epitope. (Nature 2022)

- DOI: 10.1038/s41586-021-04356-8 | PMCID: PMC8828479 | PMID: 34942633
- Evidence: Micrographs were collected with Leginon, single particles were processed with Appion, Relion and XQuartz, and footprints were mapped with UCSF Chimera, and figures were made with UCSF Chimera 60 – 63 .
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION, UCSF Chimera] -> simulation/modelling [GROMACS, PLUMED] -> visualisation [RELION] -> stage not stated [Jupyter, PHENIX, R, Seurat]

### Activation mechanism of PINK1. (Nature 2022)

- DOI: 10.1038/s41586-021-04340-2 | PMCID: PMC8828467 | PMID: 34933320
- Version used: **3.1**
- Evidence: Particle picking, extraction and 2D classification were performed using RELION (v.3.1) 51 .
- Full pipeline: structure determination [Coot v0.9] -> visualisation [ChimeraX v1.1.1] -> stage not stated [AlphaFold, ColabFold, EMAN2, Fiji v1.53k, ImageJ v1.53k, PHENIX v1.19.2, RELION v3.1, UCSF Chimera]

### FOXP3 recognizes microsatellites and bridges DNA through multimerization. (Nature 2023)

- DOI: 10.1038/s41586-023-06793-z | PMCID: PMC10719092 | PMID: 38030726
- Version used: **4.0.1**
- Evidence: Cryo-EM data processing and structure refinement Data were processed using cryoSPARC (v.4.2.0) 42 and RELION (v.4.0.1) 43 , 44 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> registration [MotionCor2] -> differential/statistical testing [DESeq2] -> structure determination [RELION v4.0.1, UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [BEDTools, CTFFIND v4.1, HOMER, MACS2, PHENIX]

### HIV-1 Env trimers asymmetrically engage CD4 receptors in membranes. (Nature 2023)

- DOI: 10.1038/s41586-023-06762-6 | PMCID: PMC10686830 | PMID: 37993716
- Evidence: The Fourier shell correlation curves were calculated using Relion 52 and the local resolutions of averaged structures were determined using ResMap 53 .
- Full pipeline: simulation/modelling [NAMD v3.0] -> structure determination [ChimeraX] -> visualisation [ChimeraX, IMOD] -> stage not stated [Python, RELION]

### Structure of the native myosin filament in the relaxed cardiac sarcomere. (Nature 2023)

- DOI: 10.1038/s41586-023-06690-5 | PMCID: PMC10665186 | PMID: 37914933
- Version used: **3.1**
- Evidence: The classes that did not show a clear presence of thin filaments were discarded and the remaining segments were re-extracted as subtomograms and processed in RELION 3.1 (refs.
- Full pipeline: alignment/mapping [ChimeraX, IMOD] -> registration [IMOD] -> structure determination [IMOD] -> visualisation [AlphaFold] -> stage not stated [RELION v3.1]

### Structures of a sperm-specific solute carrier gated by voltage and cAMP. (Nature 2023)

- DOI: 10.1038/s41586-023-06629-w | PMCID: PMC10620091 | PMID: 37880361
- Version used: **3.1.0**
- Evidence: The particle sets obtained after 2D classification were imported into Relion 3.1.0 (ref.
- Full pipeline: registration [MotionCor2 v1.4.0] -> structure determination [PHENIX v1.20.1] -> stage not stated [ChimeraX v1.6.1, PyMOL v2.5.5, RELION v3.1.0]

### Structures illustrate step-by-step mitochondrial transcription initiation. (Nature 2023)

- DOI: 10.1038/s41586-023-06643-y | PMCID: PMC10600007 | PMID: 37821701
- Version used: **3.1**
- Evidence: 42 ) as implemented in the Relion 3.1 package 43 and the contrast transfer function parameters were estimated by CTFFIND-4 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.19.2] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, RELION v3.1]

### Sialoglycan binding triggers spike opening in a human coronavirus. (Nature 2023)

- DOI: 10.1038/s41586-023-06599-z | PMCID: PMC10700143 | PMID: 37794193
- Version used: **3.1.1**
- Evidence: 42 ), implemented through Relion version 3.1.1 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CCP4, RELION v3.1.1, VMD]

### Inactivation of the Kv2.1 channel through electromechanical coupling. (Nature 2023)

- DOI: 10.1038/s41586-023-06582-8 | PMCID: PMC10567553 | PMID: 37758949
- Version used: **3.0**
- Evidence: Image processing For Kv2.1 (1–598), all processing was completed in RELION (v.3.0) 66 .
- Full pipeline: structure determination [Coot v0.9.8.1, PHENIX v1.19.1, UCSF Chimera v1.15] -> visualisation [PyMOL v2.4.1] -> stage not stated [MDAnalysis, MotionCor2, RELION v3.0]

### Cryo-EM structures reveal native GABA&lt;sub&gt;A&lt;/sub&gt; receptor assemblies and pharmacology. (Nature 2023)

- DOI: 10.1038/s41586-023-06556-w | PMCID: PMC10550821 | PMID: 37730991
- Evidence: Data processing strategy 1 Bin1 GABA A R particles, both images (360 × 360) and the star file converted using pyem 60 , were ported into RELION 61 v.3.1.
- Full pipeline: structure determination [Coot] -> stage not stated [AlphaFold, CCP4, ChimeraX, Python, RELION]

### Structural mobility tunes signalling of the GluA1 AMPA glutamate receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06528-0 | PMCID: PMC10533411 | PMID: 37704721
- Evidence: Next, particle coordinate files generated from Homogeneous Refinement were converted to RELION star files by using the Python script csparc2star.py (ref.
- Full pipeline: structure determination [Coot, PHENIX, Python, RELION] -> stage not stated [AlphaFold, ChimeraX, MotionCor2, PyMOL, UCSF Chimera]

### Neutralization, effector function and immune imprinting of Omicron variants. (Nature 2023)

- DOI: 10.1038/s41586-023-06487-6 | PMCID: PMC10511321 | PMID: 37648855
- Evidence: These selected particles were subjected to two rounds of 3D classification with 50 iterations each (angular sampling 7.5° for 25 iterations and 1.8° with local search for 25 iterations) using Relion 66 , 67 (v3.1) with an initial model generated with ab-initio reconstruction in cryoSPARC.
- Full pipeline: structure determination [RELION, UCSF Chimera]

### TDP-43 forms amyloid filaments with a distinct fold in type A FTLD-TDP. (Nature 2023)

- DOI: 10.1038/s41586-023-06405-w | PMCID: PMC10447236 | PMID: 37532939
- Evidence: Helical reconstruction Video frames were gain-corrected, aligned, dose-weighted and summed using the motion correction program in RELION-4.0 (ref.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [CTFFIND, ChimeraX]

### Diverse modes of H3K36me3-guided nucleosomal deacetylation by Rpd3S. (Nature 2023)

- DOI: 10.1038/s41586-023-06349-1 | PMCID: PMC10432269 | PMID: 37468628
- Evidence: For the Rpd3S complex dataset, after automatic particle picking and 3 rounds of 2D classification in RELION 48 , 49 , ~2.63 million particles were selected for the first round of 3D classification.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, RELION, UCSF Chimera]

### Cooperation between bHLH transcription factors and histones for DNA access. (Nature 2023)

- DOI: 10.1038/s41586-023-06282-3 | PMCID: PMC10338342 | PMID: 37407816
- Evidence: Drift correction was performed with the RELION 3 motioncorr implementation 79 , in which a motion-corrected sum of all frames was generated with and without applying a dose-weighting scheme.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bioconductor, Bowtie2, ChimeraX, PyMOL] -> structure determination [PHENIX] -> stage not stated [Coot v0.9.6, ImageJ, RELION, SAMtools v1.6]

### Fanzor is a eukaryotic programmable RNA-guided endonuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06356-2 | PMCID: PMC10432273 | PMID: 37380027
- Version used: **4.0**
- Evidence: 36 ) and RELION 4.0 (ref.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> registration [MotionCor2] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.4, PHENIX v1.18] -> stage not stated [BLAST, CTFFIND v1.18, HMMER v3.3.2, PyMOL v1.2, RELION v4.0]

### Structure and function of the RAD51B-RAD51C-RAD51D-XRCC2 tumour suppressor. (Nature 2023)

- DOI: 10.1038/s41586-023-06179-1 | PMCID: PMC7614784 | PMID: 37344587
- Version used: **3.1**
- Evidence: For NS-EM SPA, micrographs were imported into Relion 3.1 or 4.0 70 , CTF parameters were calculated using CTFFIND4 and particles picked using a trained crYOLO 67 or Topaz 69 model.
- Full pipeline: alignment/mapping [ChimeraX] -> machine learning [RELION v3.1] -> stage not stated [AlphaFold, Fiji, ImageJ, PHENIX, Topaz]

### Outer membrane utilisomes mediate glycan uptake in gut Bacteroidetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06146-w | PMCID: PMC7618045 | PMID: 37286596
- Evidence: Template-based particle picking within Relion was hindered by the large amount of carbon present in many micrographs.
- Full pipeline: registration [CTFFIND] -> differential/statistical testing [limma] -> stage not stated [AlphaFold, CCP4, ChimeraX, PHENIX, R v4.1.1, RELION]

### Class B1 GPCR activation by an intracellular agonist. (Nature 2023)

- DOI: 10.1038/s41586-023-06169-3 | PMCID: PMC10307627 | PMID: 37286611
- Evidence: The 6,333 dose-fractionated movies were subjected to beam-induced motion correction using RELION-3 (ref.
- Full pipeline: registration [RELION] -> simulation/modelling [MDTraj v1.9.8, NAMD v2.13, seaborn] -> visualisation [MDTraj v1.9.8, seaborn] -> stage not stated [Fiji, ImageJ, VMD v1.9.3]

### Axonemal structures reveal mechanoregulatory and disease mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-06140-2 | PMCID: PMC10266980 | PMID: 37258679
- Evidence: All image processing was done using RELION-3.1 (ref.
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> structure determination [Coot] -> stage not stated [AlphaFold, ChimeraX, PHENIX, R v4.0, RELION]

### A pan-influenza antibody inhibiting neuraminidase via receptor mimicry. (Nature 2023)

- DOI: 10.1038/s41586-023-06136-y | PMCID: PMC10266979 | PMID: 37258672
- Evidence: Cryo-EM data processing For the FNI9–NA (N2 A/Tanzania/205/2010) dataset, Relion 59 , 60 was used for cryo-electron microscopy (cryo-EM) data processing.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT, MotionCor2] -> stage not stated [R, RELION, UCSF Chimera]

### Histone modifications regulate pioneer transcription factor cooperativity. (Nature 2023)

- DOI: 10.1038/s41586-023-06112-6 | PMCID: PMC10338341 | PMID: 37225990
- Evidence: Negative-stain image analysis Several particles were picked using RELION ( n = 450 for arrays in 3 mM MgCl 2 , n = 262 for arrays in 3 mM MgCl 2 with OCT4 and n = 307 for arrays in 3 mM MgCl 2 with the ΔN variant of OCT4).
- Full pipeline: structure determination [Coot] -> stage not stated [ImageJ, PHENIX, RELION]

### Structural basis of catalytic activation in human splicing. (Nature 2023)

- DOI: 10.1038/s41586-023-06049-w | PMCID: PMC10208982 | PMID: 37165190
- Version used: **3.1**
- Evidence: In brief, the Warp-picked, combined B AQR particle images (734,691 particles) were re-extracted in Relion 3.1 using a box size of 640/640 px (672 Å/672 Å) and then 2× binned before being subjected to 2D classification with the ‘Ignore CTFs until the first peak’ option switched on (Extended Data Fig.
- Full pipeline: simulation/modelling [ChimeraX v1.3] -> structure determination [Coot] -> stage not stated [PyMOL, RELION v3.1]

### Structural atlas of a human gut crassvirus. (Nature 2023)

- DOI: 10.1038/s41586-023-06019-2 | PMCID: PMC10172136 | PMID: 37138077
- Version used: **3.1**
- Evidence: In total, four datasets were recorded (Extended Data Table 1 ) and processed together in RELION 3.1 41 .
- Full pipeline: structure determination [Coot v0.9.8.1, PHENIX v1.19] -> stage not stated [AlphaFold, ChimeraX v1.5, RELION v3.1]

### mRNA decoding in human is kinetically and structurally distinct from bacteria. (Nature 2023)

- DOI: 10.1038/s41586-023-05908-w | PMCID: PMC10156603 | PMID: 37020024
- Version used: **3.1**
- Evidence: Particles were picked using cisTEM 67 and the coordinates were transferred to RELION (v.3.1) 68 separately for two data collections.
- Full pipeline: registration [MotionCor2] -> structure determination [CCP4] -> machine learning [REFMAC] -> stage not stated [ChimeraX, Coot, RELION v3.1, UCSF Chimera]

### mRNA recognition and packaging by the human transcription-export complex. (Nature 2023)

- DOI: 10.1038/s41586-023-05904-0 | PMCID: PMC7614608 | PMID: 37020021
- Version used: **3.1**
- Evidence: Light fraction particles were extracted in WARP 1.0.9 with a box size of 132 pixel, while heavy fraction particles were extracted with a 168 pixel box size in RELION 3.1 66 .
- Full pipeline: read trimming [Cutadapt] -> quantification [ImageJ] -> normalisation [ImageJ] -> dimensionality reduction/clustering [R] -> visualisation [ChimeraX, ImageJ, PyMOL, R, UCSF Chimera] -> stage not stated [AlphaFold, RELION v3.1]

### Structural basis for GSDMB pore formation and its targeting by IpaH7.8. (Nature 2023)

- DOI: 10.1038/s41586-023-05832-z | PMCID: PMC10115629 | PMID: 36991122
- Evidence: After 2D classification, 156,037 particles were imported into Relion-4.0 for 3D classification with an initial model generated de novo in cryoSPARC using the same particle set.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, Coot, MotionCor2, RELION, UCSF Chimera]

### CFTR function, pathology and pharmacology at single-molecule resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-05854-7 | PMCID: PMC10115640 | PMID: 36949202
- Evidence: Particles were initially picked with the Laplacian-of-Gaussian implementation in RELION 56 .
- Full pipeline: normalisation [MotionCor2] -> stage not stated [RELION]

### Structural basis of mitochondrial membrane bending by the I-II-III&lt;sub&gt;2&lt;/sub&gt;-IV&lt;sub&gt;2&lt;/sub&gt; supercomplex. (Nature 2023)

- DOI: 10.1038/s41586-023-05817-y | PMCID: PMC10060162 | PMID: 36949187
- Evidence: Cryo-EM data processing Motion correction was performed in the internal implementation of RELION-3.1 (ref.
- Full pipeline: registration [IMOD, RELION] -> simulation/modelling [ChimeraX, GROMACS] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Structural basis for bacterial energy extraction from atmospheric hydrogen. (Nature 2023)

- DOI: 10.1038/s41586-023-05781-7 | PMCID: PMC10017518 | PMID: 36890228
- Version used: **3.1.2**
- Evidence: Cryo-EM data processing and analysis Micrographs from all datasets were motion-corrected using UCSF Motioncor 1.0.4 and dose-weighted averages had their contrast transfer function (CTF) parameters estimated using CTFFIND 4.1.8, implemented using Relion 3.1.2 (ref.
- Full pipeline: simulation/modelling [GROMACS v2021.3] -> structure determination [ChimeraX v1.3, PHENIX] -> visualisation [AlphaFold, VMD] -> stage not stated [CTFFIND v4.1.8, Coot, RELION v3.1.2]

### The structural basis for HIV-1 Vif antagonism of human APOBEC3G. (Nature 2023)

- DOI: 10.1038/s41586-023-05779-1 | PMCID: PMC10033410 | PMID: 36754086
- Evidence: Using Chimera 67 and RELION 68 , a mask was applied to subtract the signal of the bottom body from particle images.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> registration [MotionCor2] -> structure determination [AlphaFold, UCSF Chimera] -> stage not stated [ChimeraX, Coot, PHENIX, PyMOL, RELION]

### Structural basis for substrate selection by the SARS-CoV-2 replicase. (Nature 2023)

- DOI: 10.1038/s41586-022-05664-3 | PMCID: PMC9891196 | PMID: 36725929
- Version used: **3.1**
- Evidence: Particles within each class were further processed through two rounds of RELION v.3.1 Bayesian polishing 40 .
- Full pipeline: normalisation [MotionCor2] -> differential/statistical testing [RELION v3.1] -> structure determination [PHENIX] -> stage not stated [Coot v0.9.5]

### Visualization of translation and protein biogenesis at the ER membrane. (Nature 2023)

- DOI: 10.1038/s41586-022-05638-5 | PMCID: PMC9892003 | PMID: 36697828
- Version used: **3.1.1**
- Evidence: Subtomogram analysis The extracted subtomograms were aligned in RELION (3.1.1) 57 using a spherical mask with a diameter of 300 Å against a reference of an 80S ribosome obtained from a subset of the same data.
- Full pipeline: alignment/mapping [IMOD v4.10.25, NumPy v1.20.3, Python v3.8.11, RELION v3.1.1, SciPy v1.7.1] -> structure determination [ChimeraX v1.3.0, UCSF Chimera v1.14.0] -> visualisation [ChimeraX v1.3.0] -> stage not stated [AlphaFold]

### Structural basis of broad-spectrum β-lactam resistance in Staphylococcus aureus. (Nature 2023)

- DOI: 10.1038/s41586-022-05583-3 | PMCID: PMC9834060 | PMID: 36599987
- Evidence: Approximately 2,000 particles were manually selected to generate reference-free 2D-class averages in RELION 64 .
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [RELION]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Version used: **4.0**
- Evidence: Sub-tomogram averaging of the ribosome Sub-tomogram averaging of ribosomes was performed using RELION (v.4.0) 109 .
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Principles of mitoribosomal small subunit assembly in eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-022-05621-0 | PMCID: PMC9892005 | PMID: 36482135
- Version used: **3.1.1**
- Evidence: Cryo-EM data processing of human complexes All cryo-EM processing steps were completed using RELION 3.1.1 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [ChimeraX, PyMOL] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, RELION v3.1.1]

### Structures of the holo CRISPR RNA-guided transposon integration complex. (Nature 2023)

- DOI: 10.1038/s41586-022-05573-5 | PMCID: PMC9876797 | PMID: 36442503
- Evidence: The particle stacks from both classes were subjected to 3D classification in RELION v4 36 , 37 , which removed junk particles with weak densities of Cas12k or TnsB.
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [AlphaFold, RELION, UCSF Chimera v1.14]

### MCM double hexamer loading visualized with human proteins. (Nature 2024)

- DOI: 10.1038/s41586-024-08263-6 | PMCID: PMC11634765 | PMID: 39604733
- Evidence: Particles were picked using crYOLO 46 and extracted with a box size of 144 pixels in Relion 4 47 .
- Full pipeline: differential/statistical testing [AlphaFold] -> structure determination [AlphaFold, Coot v0.9.8.1, PHENIX v1.21] -> stage not stated [CTFFIND v1.06, ChimeraX v1.6.1, RELION, Topaz v0.2.5]

### Nucleosome flipping drives kinetic proofreading and processivity by SWR1. (Nature 2024)

- DOI: 10.1038/s41586-024-08152-y | PMCID: PMC11618073 | PMID: 39506114
- Evidence: The particles in class 1.1 were then imported and subjected to 3D refinement in RELION before one round of 3D classification without alignment ( T = 30), with a soft mask overlapping the Swc2–bottom gyre DNA interface 45 .
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold, CTFFIND, Coot]

### Design of customized coronavirus receptors. (Nature 2024)

- DOI: 10.1038/s41586-024-08121-5 | PMCID: PMC12187079 | PMID: 39478224
- Evidence: Well-defined particle images ab initio reconstruction followed by non-uniform 3D refinement in CryoSPARC 76 before subjecting particle images to Bayesian polishing using Relion 77 during which particles were re-extracted with a box size of 512 Å at a pixel size of 0.843 Å.
- Full pipeline: differential/statistical testing [RELION] -> structure determination [RELION] -> visualisation [ChimeraX, IQ-TREE v2.0.6] -> stage not stated [PHENIX v1.21, UCSF Chimera]

### Structural basis of mRNA decay by the human exosome-ribosome supercomplex. (Nature 2024)

- DOI: 10.1038/s41586-024-08015-6 | PMCID: PMC11540850 | PMID: 39385025
- Version used: **3.1**
- Evidence: Subsequent particle processing was performed in RELION v.3.1 (ref.
- Full pipeline: quantification [ImageJ] -> structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ImageJ] -> stage not stated [MotionCor2, RELION v3.1, UCSF Chimera]

### LYCHOS is a human hybrid of a plant-like PIN transporter and a GPCR. (Nature 2024)

- DOI: 10.1038/s41586-024-08012-9 | PMCID: PMC11525196 | PMID: 39358511
- Version used: **3.1**
- Evidence: These were subjected to multiple rounds of 2D classification in both RELION (v.3.1, 4.0b) 36 and cryoSPARC 33 , yielding particles of sufficient quality and homogeneity for three-dimensional (3D) classification.
- Full pipeline: dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX v1.20.1] -> visualisation [Matplotlib] -> stage not stated [AlphaFold, CTFFIND v4.1.8, ChimeraX, ImageJ v2.14.0, MotionCor2 v1.1.0]

### Structure of the human TIP60-C histone exchange and acetyltransferase complex. (Nature 2024)

- DOI: 10.1038/s41586-024-08011-w | PMCID: PMC11578891 | PMID: 39260417
- Evidence: The datasets were analysed in RELION-3.1 (ref.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [cryoDRGN] -> structure determination [PHENIX, cryoDRGN] -> stage not stated [AlphaFold, ChimeraX, Coot, RELION]

### Heteromeric amyloid filaments of ANXA11 and TDP-43 in FTLD-TDP type C. (Nature 2024)

- DOI: 10.1038/s41586-024-08024-5 | PMCID: PMC11485244 | PMID: 39260416
- Evidence: Helical reconstruction Movie frames were gain-corrected, aligned, dose-weighted and summed using the motion correction program in RELION-4.0 or RELION-5.0 (ref.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [CTFFIND, ChimeraX]

### Visualizing chaperonin function in situ by cryo-electron tomography. (Nature 2024)

- DOI: 10.1038/s41586-024-07843-w | PMCID: PMC11390479 | PMID: 39169181
- Evidence: EER images were motion corrected using RELION’s implementation of MotionCor2 (ref.
- Full pipeline: alignment/mapping [MotionCor2 v1.4.0] -> registration [RELION] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX]

### Structure of a fully assembled γδ T cell antigen receptor. (Nature 2024)

- DOI: 10.1038/s41586-024-07920-0 | PMCID: PMC11485255 | PMID: 39146975
- Version used: **4.0**
- Evidence: The resultant particles were extracted in RELION 4.0 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [Coot v0.9.8.93] -> structure determination [Coot v0.9.8.93, PHENIX v1.21.1] -> visualisation [ChimeraX v1.8] -> stage not stated [CTFFIND v4.1.14, ImageJ v1.54, R v12.1, RELION v4.0]

### Molecular architecture of coronavirus double-membrane vesicle pore complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07817-y | PMCID: PMC11374677 | PMID: 39143215
- Evidence: The coordinates of picked particles and contrast transfer function information were exported to RELION (v4) 33 for further 3D classification and 3D refinement.
- Full pipeline: alignment/mapping [Python] -> structure determination [ChimeraX, Coot, RELION] -> visualisation [Topaz] -> stage not stated [AlphaFold, IMOD]

### Structural basis for transthiolation intermediates in the ubiquitin pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07828-9 | PMCID: PMC11374688 | PMID: 39143218
- Version used: **3.1**
- Evidence: Initial particle sets were obtained by reference-free auto-picking with Laplacian-of-Gaussian filtering in RELION 3.1 57 , 58 .
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> differential/statistical testing [Topaz] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [IMOD v4.11] -> stage not stated [CTFFIND, ChimeraX, RELION v3.1]

### FANCD2-FANCI surveys DNA and recognizes double- to single-stranded junctions. (Nature 2024)

- DOI: 10.1038/s41586-024-07770-w | PMCID: PMC11358013 | PMID: 39085614
- Version used: **4.0**
- Evidence: All image processing was performed using RELION v.4.0 (ref.
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [Jupyter, Matplotlib v3.7.2, NumPy v1.26.0, Python v3.9, RELION v4.0, SciPy v1.11.3]

### Cryo-EM architecture of a near-native stretch-sensitive membrane microdomain. (Nature 2024)

- DOI: 10.1038/s41586-024-07720-6 | PMCID: PMC11324527 | PMID: 39048819
- Version used: **2.1.0**
- Evidence: Filaments were handpicked using manual picking in RELION v.2.1.0.
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.8.9.2, PHENIX v1.20] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, Cellpose v2.0, RELION v2.1.0, VMD v1.9]

### CryoET of β-amyloid and tau within postmortem Alzheimer's disease brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07680-x | PMCID: PMC11269202 | PMID: 38987603
- Version used: **4.0**
- Evidence: The raw EER videos were initially compressed and converted to TIFF using RELION v.4.0 59 , regrouped to give 38 frames with a dose per frame of 1.2 e − /Å 2 .
- Full pipeline: alignment/mapping [IMOD v4.12.35] -> structure determination [Coot v0.8.9.2, PHENIX v1.17.1] -> machine learning [EMAN2 v2.99] -> stage not stated [CTFFIND v1.14, ChimeraX v1.5, Fiji, ImageJ, RELION v4.0]

### Molecular basis for transposase activation by a dedicated AAA+ ATPase. (Nature 2024)

- DOI: 10.1038/s41586-024-07550-6 | PMCID: PMC11208146 | PMID: 38926614
- Evidence: They were imported to RELION-4.0 (refs.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX v1.5] -> stage not stated [CCP4, CTFFIND v4.1, RELION, Topaz]

### Oligomerization-mediated autoinhibition and cofactor binding of a plant NLR. (Nature 2024)

- DOI: 10.1038/s41586-024-07668-7 | PMCID: PMC11338831 | PMID: 38866053
- Version used: **3.08**
- Evidence: Postmotion-corrected images were loaded into RELION (3.08 and later on 4.0 during last few rounds of 3D refinement) 52 – 54 .
- Full pipeline: structure determination [AlphaFold, PHENIX, RELION v3.08] -> stage not stated [MotionCor2]

### Structure and topography of the synaptic V-ATPase-synaptophysin complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07610-x | PMCID: PMC11269182 | PMID: 38838737
- Evidence: Classes with clear membrane attaching densities were combined for constrained alignment and classification using RELION (v2) 64 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [AlphaFold, PHENIX v1.21] -> machine learning [RELION, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Coot, Python, SciPy, UCSF Chimera]

### Membraneless channels sieve cations in ammonia-oxidizing marine archaea. (Nature 2024)

- DOI: 10.1038/s41586-024-07462-5 | PMCID: PMC11153153 | PMID: 38811725
- Evidence: The roughly aligned subtomogram coordinates were then imported into RELION-4 for further analysis 19 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [NAMD v2.14, VMD v1.94] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold v2.2.0, MotionCor2]

### Structural basis for pegRNA-guided reverse transcription by a prime editor. (Nature 2024)

- DOI: 10.1038/s41586-024-07497-8 | PMCID: PMC11222144 | PMID: 38811740
- Version used: **3.1.1**
- Evidence: 24 ) in RELION v.3.1.1 (ref.
- Full pipeline: registration [MotionCor2] -> stage not stated [AlphaFold, ChimeraX, PHENIX, RELION v3.1.1, Topaz]

### High-resolution in situ structures of mammalian respiratory supercomplexes. (Nature 2024)

- DOI: 10.1038/s41586-024-07488-9 | PMCID: PMC11222160 | PMID: 38811722
- Evidence: Metadata preparation yielded 12,000 subtomogram particles in RELION-4.0 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX, IMOD] -> visualisation [ChimeraX, IMOD, PyMOL] -> stage not stated [CTFFIND, EMAN2, RELION]

### Structural insights into the cross-exon to cross-intron spliceosome switch. (Nature 2024)

- DOI: 10.1038/s41586-024-07458-1 | PMCID: PMC11208138 | PMID: 38778104
- Version used: **3.1**
- Evidence: All subsequent processing was performed using RELION 3.1 ( http://www2.mrc-lmb.cam.ac.uk/relion/index.php/Main_Page ) unless otherwise specified.
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, RELION v3.1]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Version used: **3.1**
- Evidence: Two-dimensional classification, initial model generation, three-dimensional (3D) classification, CTF refinement, Bayesian polishing, 3D sorting and final map reconstructions were performed using RELION (v.3.1 and 4.0) or cryoSPARC (v.3.0 and 4.0) 33 , 37 , 38 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### Physiological temperature drives TRPM4 ligand recognition and gating. (Nature 2024)

- DOI: 10.1038/s41586-024-07436-7 | PMCID: PMC11168932 | PMID: 38750366
- Evidence: Particle picking was performed using gautomatch (v.0.56) ( https://github.com/JackZhang-Lab/Gautmatch ) or topaz (v.0.2.4) 55 or RELION’s template picking 56 .
- Full pipeline: visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2 v1.1.0, RELION]

### Mechanism of single-stranded DNA annealing by RAD52-RPA complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07347-7 | PMCID: PMC11096129 | PMID: 38658755
- Version used: **3.1**
- Evidence: Micrographs were imported into Relion 3.1 or 4.1 54 , 55 , CTF parameters were calculated using CTFFIND4 56 , and particles were picked using crYOLO 57 or Topaz 58 .
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega] -> quantification [ImageJ] -> stage not stated [ChimeraX, EMAN2, PHENIX, RELION v3.1]

### Structures of human γδ T cell receptor-CD3 complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07439-4 | PMCID: PMC11153141 | PMID: 38657677
- Evidence: To eliminate noise on the edge and further improve the map quality, the corresponding particle stacks were transferred to RELION using the csparc2star.py script in the UCSF pyem 61 software suite.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [MotionCor2, RELION]

### Streptomyces umbrella toxin particles block hyphal growth of competing species. (Nature 2024)

- DOI: 10.1038/s41586-024-07298-z | PMCID: PMC11062931 | PMID: 38632398
- Evidence: The particle stack from the micrographs was pre-processed in Relion 46 .
- Full pipeline: alignment/mapping [ColabFold] -> structure determination [Coot, Topaz] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, Python, RELION, RoseTTAFold, napari]

### Emergence of fractal geometries in the evolution of a metabolic enzyme. (Nature 2024)

- DOI: 10.1038/s41586-024-07287-2 | PMCID: PMC11041685 | PMID: 38600380
- Version used: **3.1**
- Evidence: Particles were extracted with a pixel box size of 256 scaled down to 96 using RELION (v.3.1) 64 and underwent several rounds of reference-free 2D classification.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MotionCor2] -> normalisation [RELION v3.1] -> simulation/modelling [GROMACS v2022.2] -> structure determination [MUSCLE v3.8.31, PHENIX v1.19.2] -> stage not stated [PyMOL v2.5.2, Topaz, UCSF Chimera]

### Structural basis of Integrator-dependent RNA polymerase II termination. (Nature 2024)

- DOI: 10.1038/s41586-024-07269-4 | PMCID: PMC11062913 | PMID: 38570683
- Version used: **3.1**
- Evidence: We extracted 9,107,060 picked particles with a box size of 500 pixels and binned 2× to a pixel size of 2.1 Å per pixel using RELION 3.1 (ref.
- Full pipeline: structure determination [ChimeraX, ColabFold, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, Coot, RELION v3.1]

### Cryo-EM structures of RAD51 assembled on nucleosomes containing a DSB site. (Nature 2024)

- DOI: 10.1038/s41586-024-07196-4 | PMCID: PMC10990931 | PMID: 38509361
- Evidence: The following image-processing steps were performed using Relion 4 beta2 16 .
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [ChimeraX, RELION]

### The UFM1 E3 ligase recognizes and releases 60S ribosomes from ER translocons. (Nature 2024)

- DOI: 10.1038/s41586-024-07093-w | PMCID: PMC10937380 | PMID: 38383789
- Version used: **3.1**
- Evidence: UREL–60S image processing Cryo-EM videos were imported, beam-induced motion corrected (MOTIONCOR2) and the CTF parameters were estimated (CTFFIND4.1) using RELION (v.3.1) 41 – 43 .
- Full pipeline: registration [RELION v3.1] -> structure determination [AlphaFold, ChimeraX v1.2.5, REFMAC] -> machine learning [cryoDRGN v3.2.0] -> stage not stated [CCP4, Coot v0.9.8.1, PHENIX v1.2.1]

### A new family of bacterial ribosome hibernation factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07041-8 | PMCID: PMC10901736 | PMID: 38355796
- Version used: **3.1**
- Evidence: Cryo-EM data processing for P. urativorans ribosomes The cryo-EM dataset corresponding to structures 1–3 (Extended Data Table 1 ) was processed using RELION 3.1 54 as summarized in Extended Data Table 1 and Extended Data Fig.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, Coot v0.8.9.2, UCSF Chimera v1.14] -> stage not stated [ChimeraX v1.4, HMMER, PHENIX v1.20.1, RELION v3.1]

### Structural basis of ribosomal 30S subunit degradation by RNase R. (Nature 2024)

- DOI: 10.1038/s41586-024-07027-6 | PMCID: PMC10901742 | PMID: 38326618
- Version used: **3.1.3**
- Evidence: Cryo-EM data processing Processing was performed using RELION 3.1.3 (refs.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, MotionCor2] -> visualisation [BEDTools, ImageJ] -> stage not stated [AlphaFold, ChimeraX, Coot, RELION v3.1.3]

### Translation selectively destroys non-functional transcription complexes. (Nature 2024)

- DOI: 10.1038/s41586-023-07014-3 | PMCID: PMC10881389 | PMID: 38326611
- Evidence: 34 ), in RELION 35 .
- Full pipeline: differential/statistical testing [ggplot2] -> structure determination [ChimeraX, Coot] -> stage not stated [RELION]

### A new antibiotic traps lipopolysaccharide in its intermembrane transporter. (Nature 2024)

- DOI: 10.1038/s41586-023-06799-7 | PMCID: PMC10794137 | PMID: 38172635
- Evidence: For all maps, we also tried classification without alignment in Relion.
- Full pipeline: alignment/mapping [RELION] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX, Coot]

### Cryo-EM structures of PP2A:B55-FAM122A and PP2A:B55-ARPP19. (Nature 2024)

- DOI: 10.1038/s41586-023-06870-3 | PMCID: PMC10765524 | PMID: 38123684
- Version used: **4.0**
- Evidence: All data processing steps were performed using Relion 4.0 53 and are summarized in Extended Data Figs.
- Full pipeline: quantification [ImageJ v1.53t] -> structure determination [Coot, PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, RELION v4.0]

### Structures of the promoter-bound respiratory syncytial virus polymerase. (Nature 2024)

- DOI: 10.1038/s41586-023-06867-y | PMCID: PMC10794133 | PMID: 38123676
- Version used: **3.1.3**
- Evidence: Particle 2D classification, initial 3D model building, 3D classification, 3D refinement, contrast transfer function refinement and polishing were carried out using RELION 3.1.3 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, PyMOL, RELION v3.1.3] -> stage not stated [ChimeraX, UCSF Chimera]

### The PfRCR complex bridges malaria parasite and erythrocyte during invasion. (Nature 2024)

- DOI: 10.1038/s41586-023-06856-1 | PMCID: PMC10794152 | PMID: 38123677
- Version used: **3.1.3**
- Evidence: Following Bayesian polishing of particles in RELION 3.1.3 using default settings 38 and local per-particle contrast transfer function refinement in cryoSPARC, a final non-uniform refinement yielded consensus maps of 3.0 Å for PfRCR–Cy.003 (500,277 particles) and 3.1 Å for PfCyRPA–PfRIPR–Cy.003 (506,797 particles).
- Full pipeline: differential/statistical testing [RELION v3.1.3] -> structure determination [AlphaFold, PHENIX, RELION v3.1.3] -> visualisation [ChimeraX]

### Template and target-site recognition by human LINE-1 in retrotransposition. (Nature 2024)

- DOI: 10.1038/s41586-023-06933-5 | PMCID: PMC10830416 | PMID: 38096901
- Version used: **3.1.1**
- Evidence: All video frames were motion-corrected using MotionCor2 55 , 56 in RELION v.3.1.1 and the corresponding super-resolution pixel size was binned 2× during this process.
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [CTFFIND v4.1, ImageJ, MotionCor2, RELION v3.1.1]

### TAF15 amyloid filaments in frontotemporal lobar degeneration. (Nature 2024)

- DOI: 10.1038/s41586-023-06801-2 | PMCID: PMC10781619 | PMID: 38057661
- Evidence: Helical reconstruction Movie frames were gain-corrected, aligned, dose-weighted and summed using the motion correction programme in RELION-4.0 (ref.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [CTFFIND, ChimeraX]

### Disease-specific tau filaments assemble via polymorphic intermediates. (Nature 2024)

- DOI: 10.1038/s41586-023-06788-w | PMCID: PMC10764278 | PMID: 38030728
- Evidence: Cryo-EM data processing Video frames were gain corrected, aligned and dose weighted using RELION’s motion correction program 67 .
- Full pipeline: alignment/mapping [RELION] -> quantification [ImageJ] -> registration [RELION] -> visualisation [ImageJ] -> stage not stated [CTFFIND, ChimeraX]

### In situ structural mechanism of epothilone-B-induced CNS axon regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09654-z | PMCID: PMC12795760 | PMID: 41224993
- Version used: **5.0**
- Evidence: For subtomogram analysis of F-actin within stress fibres for validation, RELION 5.0 70 was used throughout the workflow (Extended Data Fig.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [ChimeraX, PHENIX] -> visualisation [ImageJ] -> stage not stated [RELION v5.0]

### Synthetic α-synuclein fibrils replicate in mice causing MSA-like pathology. (Nature 2025)

- DOI: 10.1038/s41586-025-09698-1 | PMCID: PMC12695662 | PMID: 41193804
- Version used: **4.0**
- Evidence: Helical reconstruction and model building of recombinant 1B fibrils All the subsequent image processing and helical reconstruction was carried out in RELION (v.4.0) 47 (Extended Data Fig.
- Full pipeline: structure determination [ChimeraX, Coot, IMOD, PHENIX, RELION v4.0] -> stage not stated [MACS2]

### Helicase-mediated mechanism of SSU processome maturation and disassembly. (Nature 2025)

- DOI: 10.1038/s41586-025-09688-3 | PMCID: PMC12711562 | PMID: 41162712
- Evidence: Cryo-EM data processing Dhr1 and Kre33 dataset The Dhr1 and Kre33 dataset was processed using a combination of RELION 5beta 31 and cryoSparc 32 v.4.6.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, ChimeraX, RELION]

### A new paradigm for outer membrane protein biogenesis in the Bacteroidota. (Nature 2025)

- DOI: 10.1038/s41586-025-09532-8 | PMCID: PMC12611786 | PMID: 41034578
- Version used: **4.03**
- Evidence: All downstream processing was carried out in cryoSPARC 4.5.3 57 or RELION 4.03 58 , using the csparc2star.py script within UCSF pyem 0.5 59 to convert between formats.
- Full pipeline: structure determination [Coot v0.9, PHENIX v1.21] -> stage not stated [AlphaFold, ChimeraX, RELION v4.03]

### Myeloperoxidase transforms chromatin into neutrophil extracellular traps. (Nature 2025)

- DOI: 10.1038/s41586-025-09523-9 | PMCID: PMC12629992 | PMID: 40963017
- Version used: **3.1**
- Evidence: The particles were then polished and CTF parameters refined in RELION (v.3.1) 49 .
- Full pipeline: alignment/mapping [IMOD v4.11] -> dimensionality reduction/clustering [UMAP] -> structure determination [IMOD v4.11, PHENIX, RELION v3.1] -> stage not stated [ChimeraX]

### Structural basis for the dynamic regulation of mTORC1 by amino acids. (Nature 2025)

- DOI: 10.1038/s41586-025-09428-7 | PMCID: PMC12507694 | PMID: 40836086
- Version used: **5.0**
- Evidence: Large movie datasets recorded with a Titan Krios microscopes (27,853 for apo, 34,122 for Sestrin2 and 23,777 for CASTOR1) were corrected for drift using MotionCor2 implementation in RELION (v5.0) 39 – 41 .
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [AlphaFold, ChimeraX v1.8, Coot v0.9.8] -> machine learning [Topaz] -> stage not stated [CTFFIND v4.1.14, MotionCor2, PHENIX v2.0, RELION v5.0]

### Molecular mechanism of ultrafast transport by plasma membrane Ca&lt;sup&gt;2+&lt;/sup&gt;-ATPases. (Nature 2025)

- DOI: 10.1038/s41586-025-09402-3 | PMCID: PMC12488499 | PMID: 40836084
- Version used: **3.1**
- Evidence: A subset of particles producing 2D class averages and reconstructions with high-resolution features were then selected for further processing in CryoSPARC 76 or RELION (3.1) 77 .
- Full pipeline: structure determination [Coot, RELION v3.1, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1.10, ChimeraX, MotionCor2, PHENIX]

### SLC45A4 is a pain gene encoding a neuronal polyamine transporter. (Nature 2025)

- DOI: 10.1038/s41586-025-09326-y | PMCID: PMC12507699 | PMID: 40836097
- Version used: **3.1**
- Evidence: All further processing was performed in cryoSPARC (v.3.3.1) 57 and RELION (v.3.1) 58 , using the csparc2star.py script within UCSF pyem 59 to convert between formats.
- Full pipeline: quality control [PLINK v1.90b] -> alignment/mapping [FUMA] -> variant calling [PLINK v1.90b] -> structure determination [Coot v0.9.8.1, PHENIX v1.20.1] -> stage not stated [Cellpose v2.0, ChimeraX, ImageJ, MAGMA, PyMOL, REGENIE v3.4.1, RELION v3.1]

### Structural basis of fast N-type inactivation in K&lt;sub&gt;v&lt;/sub&gt; channels. (Nature 2025)

- DOI: 10.1038/s41586-025-09339-7 | PMCID: PMC12460158 | PMID: 40770100
- Evidence: Image processing All processing was completed in RELION 59 and cryoSPARC 60 .
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2, RELION, Topaz]

### Loss of FCoV-23 spike domain 0 enhances fusogenicity and entry kinetics. (Nature 2025)

- DOI: 10.1038/s41586-025-09155-z | PMCID: PMC12408340 | PMID: 40634609
- Version used: **5.0b**
- Evidence: Particles were transferred from cryoSPARC (v.4.4.1) to Relion (v.5.0b) 77 using pyem 78 ( https://github.com/asarnow/pyem ) to be subjected to one round of 3D classification with 50 iterations, using the NUR map as a reference model (angular sampling 7.5° for 25 iterations and 1.8° with local search for 25 iterations) and without imposing symmetry.
- Full pipeline: structure determination [PHENIX v1.21] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Coot v0.9.8.8, RELION v5.0b, UCSF Chimera v1.8]

### Electron flow in hydrogenotrophic methanogens under nickel limitation. (Nature 2025)

- DOI: 10.1038/s41586-025-09229-y | PMCID: PMC12350162 | PMID: 40604290
- Evidence: To continue with the processing using RELION 4 (ref.
- Full pipeline: alignment/mapping [ChimeraX, IQ-TREE, MUSCLE] -> structure determination [PHENIX] -> stage not stated [AlphaFold v3.0, MotionCor2, RELION]

### Architecture, dynamics and biogenesis of GluA3 AMPA glutamate receptors. (Nature 2025)

- DOI: 10.1038/s41586-025-09325-z | PMCID: PMC12422969 | PMID: 40592473
- Version used: **5.0**
- Evidence: All data were processed using cryoSPARC (v.4.41) 56 and RELION (v.5.0) 57 .
- Full pipeline: alignment/mapping [Python] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot v0.9.8.95, PHENIX v1.20, PyMOL v2.5] -> stage not stated [RELION v5.0]

### Interactions between TTYH2 and APOE facilitate endosomal lipid transfer. (Nature 2025)

- DOI: 10.1038/s41586-025-09200-x | PMCID: PMC12328215 | PMID: 40562935
- Evidence: Cryo-EM data processing All cryo-EM datasets were processed in cryoSPARC 54 , except for the datasets of detergent-purified TTYH2 in complex with lipidated APOE, which were processed in Relion 55 .
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, ImageJ, Python, RELION, Topaz]

### Naturally ornate RNA-only complexes revealed by cryo-EM. (Nature 2025)

- DOI: 10.1038/s41586-025-09073-0 | PMCID: PMC12286853 | PMID: 40328315
- Evidence: Initial models for a monomer were obtained from ModelAngelo (Relion-5.0) 53 ; because current versions of ModelAngelo cannot be run on a pure RNA structure, EMDB-17659 was added to the corner of the map, the corresponding protein sequence (Protein Data Bank (PDB): 8PHE ) was provided, and protein residues were subsequently deleted from the model.
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [Coot v0.9.8, MUSCLE] -> visualisation [AlphaFold] -> stage not stated [ChimeraX v1.8, PHENIX, RELION]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Version used: **3.1**
- Evidence: Next, the remaining particles were subjected to an additional round of 2D classification using RELION (v.3.1) 82 , yielding a stack of 420,000 particles.
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### Swinging lever mechanism of myosin directly shown by time-resolved cryo-EM. (Nature 2025)

- DOI: 10.1038/s41586-025-08876-5 | PMCID: PMC12158783 | PMID: 40205053
- Evidence: All processing was carried out using RELION-3.1 (ref.
- Full pipeline: structure determination [PHENIX] -> stage not stated [MotionCor2, RELION]

### Structural dynamics of DNA unwinding by a replicative helicase. (Nature 2025)

- DOI: 10.1038/s41586-025-08766-w | PMCID: PMC12043514 | PMID: 40108462
- Evidence: Cryo-EM data processing Movie stacks were corrected for beam-induced motion using RELION’s implementation 54 of MotionCor2 (ref.
- Full pipeline: structure determination [ChimeraX] -> visualisation [PHENIX, PyMOL v2.6.0, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1, MotionCor2, RELION, Topaz v0.3.0]

### Complex water networks visualized by cryogenic electron microscopy of RNA. (Nature 2025)

- DOI: 10.1038/s41586-025-08855-w | PMCID: PMC12137144 | PMID: 40068818
- Evidence: Then, particle coordinates were imported to Relion 63 , where three rounds of 2D classification were performed to remove 2D class averages with less resolved features.
- Full pipeline: simulation/modelling [MDAnalysis] -> structure determination [ChimeraX v1.6.1] -> stage not stated [EMAN2, MotionCor2, RELION]

### The conserved HIV-1 spacer peptide 2 triggers matrix lattice maturation. (Nature 2025)

- DOI: 10.1038/s41586-025-08624-9 | PMCID: PMC11964938 | PMID: 40011770
- Evidence: EER videos were rendered as an 8,000 × 8,000 grid and further Fourier-cropped into a 4,000 × 4,000 grid using RELION-4.0 (ref.
- Full pipeline: structure determination [PHENIX] -> visualisation [RELION] -> stage not stated [AlphaFold v2.2.0, ChimeraX v1.3, Clustal Omega, Fiji v1.54f, ImageJ v1.54f]

### Structural dynamics of human fatty acid synthase in the condensing cycle. (Nature 2025)

- DOI: 10.1038/s41586-025-08782-w | PMCID: PMC12058526 | PMID: 39978408
- Evidence: Cryo-EM data processing Raw video stacks were subjected to motion correction, dose weighting and Fourier cropping to 0.835 Å per pixel using MotionCor2 implemented in Relion 58 , 59 .
- Full pipeline: registration [MotionCor2, RELION] -> structure determination [ChimeraX, PHENIX] -> machine learning [cryoDRGN] -> visualisation [UCSF Chimera] -> stage not stated [CTFFIND, Coot]

### Snapshots of acyl carrier protein shuttling in human fatty acid synthase. (Nature 2025)

- DOI: 10.1038/s41586-025-08587-x | PMCID: PMC12058525 | PMID: 39979457
- Version used: **3.1**
- Evidence: The images were imported into RELION 3.1 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Coot, RELION v3.1]

### Conformational protection of molybdenum nitrogenase by Shethna protein II. (Nature 2025)

- DOI: 10.1038/s41586-024-08355-3 | PMCID: PMC11754109 | PMID: 39779845
- Version used: **3.1**
- Evidence: Single-particle analysis, structural modelling and refinement Initially, the raw video stacks were motion-corrected with RELION v.3.1 (ref.
- Full pipeline: structure determination [ChimeraX, PHENIX, RELION v3.1] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4, CTFFIND v4.1]

### Structural diversity of axonemes across mammalian motile cilia. (Nature 2025)

- DOI: 10.1038/s41586-024-08337-5 | PMCID: PMC11779644 | PMID: 39743588
- Version used: **3.1**
- Evidence: For separation of 48-nm repeat from 8-nm particles, we performed three-dimensional classification of tubulin-subtracted DMT particles in Relion 3.1 (ref.
- Full pipeline: alignment/mapping [IMOD] -> registration [IMOD] -> dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot]

### Hierarchical design of pseudosymmetric protein nanocages. (Nature 2025)

- DOI: 10.1038/s41586-024-08360-6 | PMCID: PMC11821544 | PMID: 39695230
- Evidence: These selected particles were subjected to two rounds of 3D classification with 50 iterations each (angular sampling 7.5° for 25 iterations and 1.8° with local search for 25 iterations) using Relion 66 with an initial model generated with ab initio reconstruction in cryoSPARC.
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [RELION, UCSF Chimera] -> visualisation [Matplotlib v3.3.4, Python v3.8.8, seaborn v0.11.1] -> stage not stated [ChimeraX, ImageJ]

### In situ analysis reveals the TRiC duty cycle and PDCD5 as an open-state cofactor. (Nature 2025)

- DOI: 10.1038/s41586-024-08321-z | PMCID: PMC11754096 | PMID: 39663456
- Evidence: 3D classifications (classes = 4, T = 0.5, iterations = 30, without mask) and refinements ( C 1 symmetry) were performed in RELION 56 v.3.1.
- Full pipeline: alignment/mapping [Clustal Omega, IMOD] -> structure determination [RELION] -> visualisation [ChimeraX, napari] -> stage not stated [AlphaFold]

### Vaccination generates broadly cross-neutralizing antibodies to the HIV Env apex. (Nature 2026)

- DOI: 10.1038/s41586-026-10429-3 | PMCID: PMC13275315 | PMID: 42056526
- Version used: **4.0**
- Evidence: Automated data collection was performed using EPU (Thermo Fisher Scientific) and data processing was performed using Relion (v.4.0) 48 , according to standard procedures for reference-free particle picking and 2D classification.
- Full pipeline: structure determination [AlphaFold, Coot v0.9.8, PHENIX] -> stage not stated [ChimeraX, RELION v4.0]

### Structural basis of fungal β-1,3-glucan synthase inhibition by caspofungin. (Nature 2026)

- DOI: 10.1038/s41586-026-10409-7 | PMCID: PMC13249079 | PMID: 42020744
- Evidence: Beam-induced motion correction and dose-weighting were performed using Relion’s own implementation 45 .
- Full pipeline: alignment/mapping [UCSF Chimera] -> registration [RELION] -> simulation/modelling [GROMACS, MDAnalysis v2.7.0, Python, VMD v1.9] -> structure determination [Coot v0.98, UCSF Chimera] -> visualisation [MDAnalysis v2.7.0, Python, VMD v1.9] -> stage not stated [AlphaFold, ChimeraX v1.10, PHENIX v1.20, PyMOL v3.1]

### Myosin forces remodel F-actin for mechanosensitive protein recognition. (Nature 2026)

- DOI: 10.1038/s41586-026-10398-7 | PMCID: PMC13233326 | PMID: 42020745
- Evidence: To prevent the semantic segmentation network from picking the edges of holes or actin filaments over carbon, 15,208 manual picks of hole edges and thick carbon areas were selected from micrographs in the dataset using RELION 106 .
- Full pipeline: simulation/modelling [Python] -> structure determination [IMOD] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [EMAN2, MotionCor2, PHENIX, RELION, SciPy]

### Cytoplasmic lattices are megadalton storage complexes in mammalian oocytes. (Nature 2026)

- DOI: 10.1038/s41586-026-10513-8 | PMCID: PMC13253339 | PMID: 41986725
- Evidence: Particles were then exported to RELION-5 using csparc2star.py in the pyem package 46 .
- Full pipeline: alignment/mapping [ChimeraX] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [AlphaFold, RELION]

### Molecular basis for methylation-sensitive editing by Cas9. (Nature 2026)

- DOI: 10.1038/s41586-026-10384-z | PMCID: PMC13216068 | PMID: 41986708
- Version used: **4.0**
- Evidence: Several rounds of 3D refinement and 3D classification were then performed using Relion 4.0 (ref.
- Full pipeline: registration [CTFFIND] -> differential/statistical testing [Python, R] -> structure determination [PHENIX, RELION v4.0] -> stage not stated [Topaz]

### A µ-opioid receptor superagonist analgesic with minimal adverse effects. (Nature 2026)

- DOI: 10.1038/s41586-026-10299-9 | PMCID: PMC13128446 | PMID: 41922775
- Evidence: Data processing Tiff files were imported in Relion 74 for motion correction with MotionCorr2 75 , CTF estimation with CTFFIND4 76 , and template-based particle picking.
- Full pipeline: normalisation [R] -> registration [RELION] -> structure determination [Coot v0.9.8.1, PHENIX]

### Structural basis of supercoiling-induced CRISPR-Cas9 off-target activity. (Nature 2026)

- DOI: 10.1038/s41586-026-10255-7 | PMCID: PMC13171457 | PMID: 41882360
- Evidence: For focus refinement maps, reference maps were subjected to a soft mask creation in RELION, masks were used to remove noise from the remaining minicircle DNA.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX, RELION] -> stage not stated [AlphaFold, Fiji, ImageJ, Topaz]

### Ectopic NMDAR expression in cancer unmasks germline-encoded autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10278-0 | PMCID: PMC13216075 | PMID: 41882353
- Evidence: Single-particle cryo-EM data processing was performed using WARP 84 , Relion 85 and cryoSPARC 86 (v.3.2.0 to v.4.6.0).
- Full pipeline: alignment/mapping [UMAP, edgeR] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX, PHENIX] -> stage not stated [Fiji, ImageJ, MACS2, QuPath, R, RELION, Seurat]

### Mechanism of co-transcriptional cap snatching by influenza polymerase. (Nature 2026)

- DOI: 10.1038/s41586-026-10189-0 | PMCID: PMC13128444 | PMID: 41781612
- Evidence: For the post-cleavage dataset, 11,935,228 particles were extracted in five batches in RELION-3.1.0 (ref.
- Full pipeline: alignment/mapping [MUSCLE] -> structure determination [PHENIX] -> stage not stated [ChimeraX v1.6.1, Coot, RELION]

### Integrase anchors viral RNA to the HIV-1 capsid interior. (Nature 2026)

- DOI: 10.1038/s41586-026-10154-x | PMCID: PMC13102720 | PMID: 41708858
- Evidence: The movie frames were aligned with dose weighting using Relion-4.0 (refs.
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0, RELION] -> normalisation [ImageJ, NAMD v3.0.1] -> simulation/modelling [VMD] -> structure determination [ChimeraX, Coot, IMOD] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PyMOL, Topaz, UCSF Chimera]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Version used: **3.1.0**
- Evidence: A combination of cryoSPARC (v3.2.0–4.3.0) and RELION (v3.1.0) 57 were used for data processing.
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### Structural basis of regulated N-glycosylation at the secretory translocon. (Nature 2026)

- DOI: 10.1038/s41586-025-09756-8 | PMCID: PMC12804085 | PMID: 41261126
- Version used: **5.0**
- Evidence: Image processing All data processing was performed using RELION 5.0 (ref.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [TopHat v2.1.0] -> quantification [HTSeq v2.0.3] -> structure determination [Coot, PHENIX] -> machine learning [Coot] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

### ZAK activation at the collided ribosome. (Nature 2026)

- DOI: 10.1038/s41586-025-09772-8 | PMCID: PMC12823453 | PMID: 41261136
- Version used: **5.0**
- Evidence: From the combined datasets, 2,246,220 particles were automatically picked from a total of 95,813 micrographs in RELION (v5.0 beta) 60 .
- Full pipeline: read trimming [SAMtools, Trim Galore] -> alignment/mapping [MotionCor2 v1.4.0, SAMtools, STAR] -> structure determination [AlphaFold, ChimeraX v1.9, PHENIX v1.20.1, UCSF Chimera] -> stage not stated [Coot, RELION v5.0]

### Potent neutralization of Marburg virus by a vaccine-elicited antibody. (Nature 2026)

- DOI: 10.1038/s41586-025-09868-1 | PMCID: PMC12893919 | PMID: 41225006
- Evidence: The particle images were then subjected to Bayesian polishing using Relion 69 , during which the box size was adjusted to 512 pixels 2 and the pixel size was adjusted to 0.829 Å.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39] -> differential/statistical testing [RELION] -> structure determination [AlphaFold, ChimeraX, PHENIX]

### An ATP-gated molecular switch orchestrates human mRNA export. (Nature 2026)

- DOI: 10.1038/s41586-025-09832-z | PMCID: PMC12823420 | PMID: 41198879
- Version used: **3.1**
- Evidence: We picked 470,103 particles in Warp using a custom BoxNet model and extracted them in RELION (v.3.1) 84 in a box size of 672 Å.
- Full pipeline: visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, Cellpose, Coot, RELION v3.1]

### Structure and RNA template requirements of <i>Arabidopsis</i> RNA-DEPENDENT RNA POLYMERASE 2. (PNAS 2021)

- DOI: 10.1073/pnas.2115899118 | PMCID: PMC8713982 | PMID: 34903670
- Version used: **3.1**
- Evidence: The map used to build the de novo atomic model was obtained by image processing using Relion 3.1 ( 27 , 28 , 64 ).
- Full pipeline: structure determination [ChimeraX] -> stage not stated [RELION v3.1]

### Nanometer-resolution in situ structure of the SARS-CoV-2 postfusion spike protein. (PNAS 2021)

- DOI: 10.1073/pnas.2112703118 | PMCID: PMC8640741 | PMID: 34782481
- Evidence: To determine the exact ratio of prefusion and postfusion states on a nonbiased basis, an average of all extracted prefusion and postfusion Ss was generated to be used as a single reference for 3D classification in RELION (a computer program for cryo-EM data processing) versions 3.0 and 3.1 ( 39 , 40 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [IMOD, RELION]

### Vascular K<sub>ATP</sub> channel structural dynamics reveal regulatory mechanism by Mg-nucleotides. (PNAS 2021)

- DOI: 10.1073/pnas.2109441118 | PMCID: PMC8694068 | PMID: 34711681
- Evidence: Image processing and analysis were carried out in RELION-3.0 and CryoSPARC.
- Full pipeline: simulation/modelling [GROMACS v2019.4] -> structure determination [Coot, PHENIX] -> stage not stated [RELION]

### Cryo-EM structures of PI3Kα reveal conformational changes during inhibition and activation. (PNAS 2021)

- DOI: 10.1073/pnas.2109327118 | PMCID: PMC8609346 | PMID: 34725156
- Evidence: Particle selection and 2D and 3D classifications were performed on a binned dataset with a pixel size of 2.09 Å using cryoSPARC (v3.0.1) and RELION-3.0-beta2.
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX v1.2] -> stage not stated [CTFFIND v1.06, RELION]

### Structure of the ATP synthase from <i>Mycobacterium smegmatis</i> provides targets for treating tuberculosis. (PNAS 2021)

- DOI: 10.1073/pnas.2111899118 | PMCID: PMC8617483 | PMID: 34782468
- Evidence: ATP synthase particles were picked with crYOLO ( 30 ), and a variety of related structures were determined by hierarchical classification and refinement with RELION ( 31 ).
- Full pipeline: structure determination [PHENIX, RELION]

### Cryo-EM structure determination of small proteins by nanobody-binding scaffolds (Legobodies). (PNAS 2021)

- DOI: 10.1073/pnas.2115001118 | PMCID: PMC8521671 | PMID: 34620716
- Version used: **3.1**
- Evidence: The particles were then subjected to 2D classification (T2, 80 classes, 30 iterations) in Relion 3.1 ( 40 ).
- Full pipeline: registration [MotionCor2] -> stage not stated [Coot, PHENIX, RELION v3.1]

### Constitutive signal bias mediated by the human GHRHR splice variant 1. (PNAS 2021)

- DOI: 10.1073/pnas.2106606118 | PMCID: PMC8501799 | PMID: 34599099
- Evidence: The following data processing was performed using RELION-3.0-beta2 ( 69 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v1.18, RELION]

### Structural basis of rotavirus RNA chaperone displacement and RNA annealing. (PNAS 2021)

- DOI: 10.1073/pnas.2100198118 | PMCID: PMC8521686 | PMID: 34615715
- Evidence: From 23 micrograph images taken with a nominal defocus of −3 µm, 14,740 particles were picked using template-based autopicking within Relion 3.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ImageJ] -> stage not stated [RELION]

### Structural basis for isoform-specific inhibition of human CTPS1. (PNAS 2021)

- DOI: 10.1073/pnas.2107968118 | PMCID: PMC8501788 | PMID: 34583994
- Evidence: Movies were aligned, dose-weighted, and summed using the Relion ( 62 ) implementation of MotionCor2 ( 63 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> stage not stated [PHENIX]

### Structural analysis of receptors and actin polarity in platelet protrusions. (PNAS 2021)

- DOI: 10.1073/pnas.2105004118 | PMCID: PMC8449362 | PMID: 34504018
- Evidence: The 2D projections were further aligned to produce 2D classes that were used for 3D reconstruction by the helical toolbox of RELION ( 30 ).
- Full pipeline: alignment/mapping [RELION] -> structure determination [RELION]

### Native structure of the RhopH complex, a key determinant of malaria parasite nutrient acquisition. (PNAS 2021)

- DOI: 10.1073/pnas.2100514118 | PMCID: PMC8536402 | PMID: 34446549
- Evidence: As such, small datasets of ∼100,000 particles were collected for each fraction, and 2D class averages generated in RELION ( 22 , 44 ) were used to identify fractions containing promising particles ( Fig.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> stage not stated [RELION, UCSF Chimera]

### High-resolution asymmetric structure of a Fab-virus complex reveals overlap with the receptor binding site. (PNAS 2021)

- DOI: 10.1073/pnas.2025452118 | PMCID: PMC8201801 | PMID: 34074770
- Evidence: RELION was used for motion correction, movie refinement, and particle polishing ( 44 ), whereas cryoSPARC was used for particle sorting and high-resolution icosahedral refinement ( 27 ).
- Full pipeline: registration [RELION] -> simulation/modelling [Coot] -> structure determination [RELION] -> stage not stated [PHENIX]

### Nanobody cocktails potently neutralize SARS-CoV-2 D614G N501Y variant and protect mice. (PNAS 2021)

- DOI: 10.1073/pnas.2101918118 | PMCID: PMC8126837 | PMID: 33893175
- Version used: **3.1**
- Evidence: Particle coordinates were imported into Relion 3.1 ( 68 ), extracted and subjected to two-dimensional (2D) classification.
- Full pipeline: dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, MotionCor2]

### Cryo-EM structure of <i>Mycobacterium smegmatis</i> DyP-loaded encapsulin. (PNAS 2021)

- DOI: 10.1073/pnas.2025658118 | PMCID: PMC8072242 | PMID: 33853951
- Evidence: Gautomatch 0.53 ( https://www2.mrc-lmb.cam.ac.uk/download/gautomatch-053/ ) was used to automatically pick particles from parts of micrographs without a template, and the resulting particles stack was subjected to reference-free two-dimensional (2D) classification using RELION (REgularized LIkelihood OptimizatioN) 3.0.5 ( 53 – 55 ).
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> dimensionality reduction/clustering [RELION] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [UCSF Chimera]

### Structure of Gcn1 bound to stalled and colliding 80S ribosomes. (PNAS 2021)

- DOI: 10.1073/pnas.2022756118 | PMCID: PMC8040806 | PMID: 33790014
- Evidence: Automated particle picking was then performed using Gautomatch ( https://www.mrc-lmb.cam.ac.uk/kzhang/ ) and processed using the RELION-3.0 software package ( 49 ).
- Full pipeline: structure determination [PHENIX, UCSF Chimera v1.13.1] -> stage not stated [ChimeraX, RELION]

### The effect of the D614G substitution on the structure of the spike glycoprotein of SARS-CoV-2. (PNAS 2021)

- DOI: 10.1073/pnas.2022586118 | PMCID: PMC7936381 | PMID: 33579792
- Evidence: The frames of the collected movies were aligned using MotionCor2 ( 17 ) implemented in RELION ( 18 ), and the Contrast Transfer Function (CTF) was fitted using CTFfind4 ( 19 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [Coot, PHENIX] -> stage not stated [UCSF Chimera]

### Molecular mechanisms of assembly and TRIP13-mediated remodeling of the human Shieldin complex. (PNAS 2021)

- DOI: 10.1073/pnas.2024512118 | PMCID: PMC7923543 | PMID: 33597306
- Evidence: One of 3D classes showed extra density of SHLD2.3–REV7 4 , and the corresponding 104,023 particles were polished using RELION particle polishing, yielding a consensus electron microscopy map with a resolution of 3.6 Å after 3D autorefinement.
- Full pipeline: structure determination [RELION] -> visualisation [PyMOL] -> stage not stated [MotionCor2, PHENIX, UCSF Chimera]

### Structure of the SARS-CoV-2 RNA-dependent RNA polymerase in the presence of favipiravir-RTP. (PNAS 2021)

- DOI: 10.1073/pnas.2021946118 | PMCID: PMC7896311 | PMID: 33526596
- Version used: **3.1**
- Evidence: All data were processed in RELION 3.1 ( 20 ), using particle picks imported from crYOLO 1.5 ( 21 ) ( SI Appendix , Fig.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [RELION v3.1]

### Long-range structural defects by pathogenic mutations in most severe glucose-6-phosphate dehydrogenase deficiency. (PNAS 2021)

- DOI: 10.1073/pnas.2022790118 | PMCID: PMC7848525 | PMID: 33468660
- Version used: **3.0.6**
- Evidence: Dose-weighted 4,255 and 4,395 movies were aligned by MOTIONCOR2, and following image processing was done using Relion 3.0.6 ( 57 , 58 ) ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [RELION v3.0.6] -> simulation/modelling [GROMACS v2019.4] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX]

### Supramolecular assembly of the <i>Escherichia coli</i> LdcI upon acid stress. (PNAS 2021)

- DOI: 10.1073/pnas.2014383118 | PMCID: PMC7812809 | PMID: 33372137
- Version used: **1.4**
- Evidence: Particle extraction followed by several rounds of cleaning by two-dimensional (2D) classification in RELION 1.4 ( 57 ), resulted in the following number of particles for each dataset: Dendra2 T69A –LdcI = 7,140, mGeosM–LdcI = 5,514, LdcI–Dendra2 T69A = 832, LdcI–mGeosM = 12,211, and LdcI/anti-LdcI-Nb = 14,075.
- Full pipeline: registration [MotionCor2] -> dimensionality reduction/clustering [RELION v1.4] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, ImageJ]

### Cross-species recognition of SARS-CoV-2 to bat ACE2. (PNAS 2021)

- DOI: 10.1073/pnas.2020216118 | PMCID: PMC7817217 | PMID: 33335073
- Version used: **3.1**
- Evidence: All subsequent image processing and reconstruction processes were performed using Relion 3.1 ( 45 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX, RELION v3.1]

### Human species D adenovirus hexon capsid protein mediates cell entry through a direct interaction with CD46. (PNAS 2021)

- DOI: 10.1073/pnas.2020732118 | PMCID: PMC7826407 | PMID: 33384338
- Version used: **3.1**
- Evidence: Data were processed using Relion 3.1 ( 65 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [CCP4, CTFFIND, ChimeraX, EMAN2, MotionCor2, RELION v3.1]

### Sparseness and Smoothness Regularized Imaging for improving the resolution of Cryo-EM single-particle reconstruction. (PNAS 2021)

- DOI: 10.1073/pnas.2013756118 | PMCID: PMC7812788 | PMID: 33402531
- Evidence: We thus postulate that the traditional method in RELION biases the solution toward the 3D map with homogeneous smoothness across space.
- Full pipeline: stage not stated [PHENIX, RELION]

### Biophysical characterization of calcium-binding and modulatory-domain dynamics in a pentameric ligand-gated ion channel. (PNAS 2022)

- DOI: 10.1073/pnas.2210669119 | PMCID: PMC9897478 | PMID: 36480474
- Version used: **3.1**
- Evidence: All subsequent processing was performed through the RELION 3.1 pipeline ( 44 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS, VMD] -> stage not stated [PHENIX, RELION v3.1, UCSF Chimera]

### In situ structures of polymerase complex of mammalian reovirus illuminate RdRp activation and transcription regulation. (PNAS 2022)

- DOI: 10.1073/pnas.2203054119 | PMCID: PMC9897473 | PMID: 36469786
- Evidence: The structures were determined using Relion ( 59 ), applying icosahedral symmetry.
- Full pipeline: alignment/mapping [CTFFIND] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [RELION]

### Mechanism of actin filament branch formation by Arp2/3 complex revealed by a high-resolution cryo-EM structureof the branch junction. (PNAS 2022)

- DOI: 10.1073/pnas.2206722119 | PMCID: PMC9894260 | PMID: 36442092
- Version used: **4.0**
- Evidence: The dataset of images was processed mostly using Relion 4.0 ( 43 ), including the steps from motion correction and contrast transfer function (CTF) estimation to map post-processing, except for the particle picking step.
- Full pipeline: registration [RELION v4.0] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> visualisation [ChimeraX] -> stage not stated [Coot, PyMOL]

### Cryo-EM structures of cancer-specific helical and kinase domain mutations of PI3Kα. (PNAS 2022)

- DOI: 10.1073/pnas.2215621119 | PMCID: PMC9674216 | PMID: 36343266
- Evidence: Particle selection and 2D and 3D classifications were performed on a binned dataset using cryoSPARC (v3.3.2) and RELION-3.0-beta2.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX v1.18.2] -> visualisation [ChimeraX v1.0, PyMOL v2.1, UCSF Chimera v1.13.1] -> stage not stated [CTFFIND v1.06, RELION]

### Voltage-sensor movements in the Eag Kv channel under an applied electric field. (PNAS 2022)

- DOI: 10.1073/pnas.2214151119 | PMCID: PMC9674223 | PMID: 36331999
- Version used: **3.1**
- Evidence: The particles in this reconstruction were subjected to focused classification without alignment in RELION 3.1 ( 53 ), using a mask on the TM while excluding the CTD.
- Full pipeline: alignment/mapping [RELION v3.1] -> structure determination [ChimeraX v1.2.0, PHENIX, PyMOL, RELION v3.1]

### Cryo-electron microscopy structure of the H3-H4 octasome: A nucleosome-like particle without histones H2A and H2B. (PNAS 2022)

- DOI: 10.1073/pnas.2206542119 | PMCID: PMC9659345 | PMID: 36322721
- Version used: **3.0**
- Evidence: RELION 3.0 was used to process the images of the H3-H4 octasome sample as follows ( 50 ).
- Full pipeline: alignment/mapping [MotionCor2] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [RELION v3.0]

### Mechanism of 4-aminopyridine inhibition of the lysosomal channel TMEM175. (PNAS 2022)

- DOI: 10.1073/pnas.2208882119 | PMCID: PMC9636928 | PMID: 36279431
- Version used: **3.0**
- Evidence: Particles were automatically selected in Relion 3.0 using templates previously generated from 2D classification, resulting in 1,128,690 particles ( 29 ).
- Full pipeline: alignment/mapping [VMD] -> simulation/modelling [NAMD v2.12] -> structure determination [PHENIX] -> stage not stated [RELION v3.0]

### Structural and functional investigation of ABC transporter STE6-2p from <i>Pichia pastoris</i> reveals unexpected interaction with sterol molecules. (PNAS 2022)

- DOI: 10.1073/pnas.2202822119 | PMCID: PMC9618074 | PMID: 36256814
- Version used: **3.1**
- Evidence: The collected 8,218 images were corrected for electron beam–induced sample motion with MotionCor2 ( 55 ) in RELION 3.1 software ( 56 ) with dose weighting (1e − /Å 2 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [BLAST, CTFFIND, MotionCor2, RELION v3.1]

### Cryo-EM structures of light-harvesting 2 complexes from <i>Rhodopseudomonas palustris</i> reveal the molecular origin of absorption tuning. (PNAS 2022)

- DOI: 10.1073/pnas.2210109119 | PMCID: PMC9618040 | PMID: 36251992
- Evidence: All raw cryo-EM movies data were motion corrected on 5 × 5 patches within RELION ( 55 ).
- Full pipeline: registration [RELION] -> structure determination [PHENIX] -> machine learning [PHENIX] -> stage not stated [AlphaFold, BLAST]

### Geometrically programmed self-limited assembly of tubules using DNA origami colloids. (PNAS 2022)

- DOI: 10.1073/pnas.2207902119 | PMCID: PMC9618141 | PMID: 36252043
- Evidence: Image processing was performed using RELION-3 ( 32 ).
- Full pipeline: stage not stated [IMOD, RELION]

### SPACA9 is a lumenal protein of human ciliary singlet and doublet microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2207605119 | PMCID: PMC9564825 | PMID: 36191189
- Evidence: All image processing was performed using RELION-3.1 ( 47 ) or RELION-4.0 ( 48 ) unless otherwise stated.
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX, Clustal Omega v1.2.2] -> stage not stated [AlphaFold, Coot v0.9.4.1, IMOD, PHENIX, PyMOL v2.3.4, RELION]

### In situ structural analysis reveals membrane shape transitions during autophagosome formation. (PNAS 2022)

- DOI: 10.1073/pnas.2209823119 | PMCID: PMC9522377 | PMID: 36122245
- Version used: **3.1.2**
- Evidence: Ribosome positions were determined by template matching with StopGAP 0.7.0 ( 63 ), followed by subtomogram averaging and classification using Warp/M ( 64 ) and Relion 3.1.2 ( 65 ).
- Full pipeline: alignment/mapping [IMOD v4.10.49] -> differential/statistical testing [SciPy v1.6.2, pingouin] -> structure determination [ChimeraX v1.2.5, IMOD v4.10.49] -> stage not stated [ImageJ v1.53, RELION v3.1.2]

### Nanomolar inhibition of SARS-CoV-2 infection by an unmodified peptide targeting the prehairpin intermediate of the spike protein. (PNAS 2022)

- DOI: 10.1073/pnas.2210990119 | PMCID: PMC9546559 | PMID: 36122200
- Evidence: The data were processed using a combination of MotionCor2 ( 32 ), Gctf ( 33 ), EMAN2 ( 34 ), cryoSPARC ( 35 ), and RELION ( 36 ), as described previously ( 16 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, CellProfiler, EMAN2, MotionCor2, RELION, kallisto]

### Nanobodies and chemical cross-links advance the structural and functional analysis of PI3Kα. (PNAS 2022)

- DOI: 10.1073/pnas.2210769119 | PMCID: PMC9499577 | PMID: 36095215
- Evidence: Particle selection and 2D and 3D classifications were performed on a binned dataset using cryoSPARC (v3.0.1) and RELION-3.0-beta2.
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX v1.3] -> stage not stated [CTFFIND v1.06, RELION]

### Multistate structures of the MLL1-WRAD complex bound to H2B-ubiquitinated nucleosome. (PNAS 2022)

- DOI: 10.1073/pnas.2205691119 | PMCID: PMC9499523 | PMID: 36095189
- Version used: **3.0**
- Evidence: The full dataset was then manually inspected, and 4,804 movie stacks were selected for further processing in Relion 3.0 ( 71 ).
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, RELION v3.0, VMD v1.9.3, cryoDRGN]

### Mechanism by which T7 bacteriophage protein Gp1.2 inhibits &lt;i&gt;Escherichia coli&lt;/i&gt; dGTPase. (PNAS 2022)

- DOI: 10.1073/pnas.2123092119 | PMCID: PMC9478638 | PMID: 36067314
- Evidence: All data were processed in RELION ( 39 ) using normal procedures ( SI Appendix , Table S2 and Fig.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot] -> machine learning [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, RELION]

### Topological crossing in the misfolded <i>Tetrahymena</i> ribozyme resolved by cryo-EM. (PNAS 2022)

- DOI: 10.1073/pnas.2209146119 | PMCID: PMC9477386 | PMID: 36067294
- Evidence: Then, particle coordinates were imported to Relion ( 23 ), where three rounds of 2D classification were performed to remove 2D class averages with poorly resolved features.
- Full pipeline: visualisation [ChimeraX] -> stage not stated [Coot, EMAN2, MotionCor2, PHENIX, RELION, UCSF Chimera]

### Structural mechanism for bidirectional actin cross-linking by T-plastin. (PNAS 2022)

- DOI: 10.1073/pnas.2205370119 | PMCID: PMC9478642 | PMID: 36067297
- Evidence: Both the +Ca 2+ and –Ca 2+ postbound states were reconstructed using a standard RELION IHRSR workflow ( 53 , 54 ) as previously described ( 26 ), and the –Ca 2+ prebundling state was subsequently recovered through symmetry expansion followed by extensive focused classification in RELION.
- Full pipeline: structure determination [RELION] -> stage not stated [AlphaFold]

### Structure of a cholinergic cell membrane. (PNAS 2022)

- DOI: 10.1073/pnas.2207641119 | PMCID: PMC9407305 | PMID: 35969788
- Evidence: All subsequent image processing steps were performed in RELION ( 38 , 39 ).
- Full pipeline: alignment/mapping [CTFFIND] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [MotionCor2, RELION]

### A multidomain connector links the outer membrane and cell wall in phylogenetically deep-branching bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2203156119 | PMCID: PMC9388160 | PMID: 35943982
- Evidence: Per-particle defocus, anisotropy magnification, and higher-order aberrations ( 71 ) were refined inside RELION-3.1, followed by signal subtraction of the detergent micelle and another round of focused 3D autorefinement, as described in our previous studies using single-particle cryo-EM ( 68 ).
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2] -> dimensionality reduction/clustering [MotionCor2] -> structure determination [ChimeraX, Coot, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold]

### Reversible structural changes in the influenza hemagglutinin precursor at membrane fusion pH. (PNAS 2022)

- DOI: 10.1073/pnas.2208011119 | PMCID: PMC9388137 | PMID: 35939703
- Evidence: Subsequent processing steps were mostly carried out in RELION-3.1 ( 65 , 66 ), but cryoSPARC v2 ( 67 ) was also used for the refinement of the low-pH structure.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, RELION] -> visualisation [ChimeraX]

### PTX3 structure determination using a hybrid cryoelectron microscopy and AlphaFold approach offers insights into ligand binding and complement activation. (PNAS 2022)

- DOI: 10.1073/pnas.2208144119 | PMCID: PMC9388099 | PMID: 35939690
- Version used: **3.1**
- Evidence: All subsequent steps were carried out in Relion 3.1 ( 45 ) and are described in SI Appendix in detail.
- Full pipeline: structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [AlphaFold, ChimeraX, ColabFold v1.3, RELION v3.1]

### Mechanistic details of CRISPR-associated transposon recruitment and integration revealed by cryo-EM. (PNAS 2022)

- DOI: 10.1073/pnas.2202590119 | PMCID: PMC9371665 | PMID: 35914146
- Evidence: Roughly the same refinement procedure was applied to both datasets: cryoSPARC particle alignment parameters and stacks were exported to RELION ( 40 , 41 ) for subsequent refinement, including three-dimensional classification, CTF refinement ( 42 ), and Bayesian polishing ( 43 ).
- Full pipeline: alignment/mapping [RELION] -> dimensionality reduction/clustering [RELION] -> differential/statistical testing [RELION] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold, UCSF Chimera]

### Structural insights into a spindle-shaped archaeal virus with a sevenfold symmetrical tail. (PNAS 2022)

- DOI: 10.1073/pnas.2119439119 | PMCID: PMC9351363 | PMID: 35895681
- Evidence: The defocus value of each image was measured by GCTF in RELION ( 14 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [RELION]

### Unwinding and spiral sliding of S4 and domain rotation of VSD during the electromechanical coupling in Na&lt;sub&gt;v&lt;/sub&gt;1.7. (PNAS 2022)

- DOI: 10.1073/pnas.2209164119 | PMCID: PMC9388133 | PMID: 35878056
- Version used: **3.0**
- Evidence: Local resolutions were calculated in RELION 3.0.
- Full pipeline: visualisation [PyMOL] -> stage not stated [RELION v3.0]

### Shelterin is a dimeric complex with extensive structural heterogeneity. (PNAS 2022)

- DOI: 10.1073/pnas.2201662119 | PMCID: PMC9351484 | PMID: 35881804
- Evidence: Particles were then extracted and subjected to two or three rounds of 2D classification in RELION-3.0 ( 81 ) to remove junk particles.
- Full pipeline: stage not stated [AlphaFold, EMAN2, RELION]

### Cryo-EM structures of alphavirus conformational intermediates in low pH-triggered prefusion states. (PNAS 2022)

- DOI: 10.1073/pnas.2114119119 | PMCID: PMC9335222 | PMID: 35867819
- Evidence: Particle picking, two-dimensional (2D) classification, initial model generation, and three-dimensional (3D) classification were performed in Relion ( 41 ).
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [VMD]

### Structural basis for high-voltage activation and subtype-specific inhibition of human Na&lt;sub&gt;v&lt;/sub&gt;1.8. (PNAS 2022)

- DOI: 10.1073/pnas.2208211119 | PMCID: PMC9335304 | PMID: 35858452
- Evidence: First, the data star from the auto-refinement procedure was fed into the SGD initial model generation procedure of RELION-3.1 (K = 1) ( 53 ), which was initiated from random initial seeds and terminated after only a few iterations (typically between 3 and 10).
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, Coot, MotionCor2]

### Cryo-EM structures of wild-type and E138K/M184I mutant HIV-1 RT/DNA complexed with inhibitors doravirine and rilpivirine. (PNAS 2022)

- DOI: 10.1073/pnas.2203660119 | PMCID: PMC9335299 | PMID: 35858448
- Version used: **3.1**
- Evidence: Individual movie frames were motion-corrected and aligned using MotionCor2 ( 50 ) as implemented in the Relion 3.1 package ( 51 ) and the contrast transfer function (CTF) parameters were estimated by CTFFIND-4 ( 52 ).
- Full pipeline: alignment/mapping [CTFFIND, MotionCor2, RELION v3.1] -> structure determination [Coot, PHENIX v1.19] -> visualisation [PyMOL]

### Correlation between the binding affinity and the conformational entropy of nanobody SARS-CoV-2 spike protein complexes. (PNAS 2022)

- DOI: 10.1073/pnas.2205412119 | PMCID: PMC9351521 | PMID: 35858383
- Evidence: Processing up to two-dimensional classification used the Relion_IT.py processing pipeline implemented at eBIC at Diamond Light Source.
- Full pipeline: dimensionality reduction/clustering [RELION] -> simulation/modelling [GROMACS, PLUMED v2.6.0] -> structure determination [ChimeraX, PHENIX] -> stage not stated [CCP4]

### In situ architecture of the lipid transport protein VPS13C at ER-lysosome membrane contacts. (PNAS 2022)

- DOI: 10.1073/pnas.2203769119 | PMCID: PMC9303930 | PMID: 35858323
- Evidence: The remapping of rods to the original tomogram was done with the scripts i3_to_RELION.py ( https://github.com/scai20/i3 , DOI: 10.5281/zenodo.6618390 ) and ot_remap.py ( https://github.com/anaphaze/ot-tools ) and visualized in UCSF Chimera (version 1.13, https://www.rbvi.ucsf.edu/chimera , RRID:SCR_004097) ( 53 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0] -> structure determination [AlphaFold, ChimeraX, IMOD] -> visualisation [RELION, UCSF Chimera v1.13, seaborn v0.11.2] -> stage not stated [CTFFIND v1.18, EMAN2 v2.91]

### Structure of the human cation-chloride cotransport KCC1 in an outward-open state. (PNAS 2022)

- DOI: 10.1073/pnas.2109083119 | PMCID: PMC9271165 | PMID: 35759661
- Version used: **3.0.7**
- Evidence: At this point, the 446,018 particles from the first round of 2D classification were exported into RELION 3.0.7 ( 61 ) for multiple rounds of three-dimensional (3D) classification with C2 symmetry imposed and using the cryoSPARC 3.0 de novo map as the starting model.
- Full pipeline: alignment/mapping [MotionCor2] -> dimensionality reduction/clustering [RELION v3.0.7] -> structure determination [PHENIX v1.18] -> stage not stated [Coot v0.8.9.3]

### Structural basis of Tom20 and Tom22 cytosolic domains as the human TOM complex receptors. (PNAS 2022)

- DOI: 10.1073/pnas.2200158119 | PMCID: PMC9245660 | PMID: 35733257
- Evidence: After that, 347,601 particles were selected and processed by cryoSPARC and RELION ( 58 – 60 ) separately.
- Full pipeline: registration [MotionCor2] -> structure determination [UCSF Chimera] -> stage not stated [PHENIX, RELION]

### Cryo-EM structure of DNA-bound Smc5/6 reveals DNA clamping enabled by multi-subunit conformational changes. (PNAS 2022)

- DOI: 10.1073/pnas.2202799119 | PMCID: PMC9191643 | PMID: 35648833
- Version used: **3.0**
- Evidence: All other steps of image processing were performed by RELION 3.0 ( 27 ) and Cryosparc v3.3.0 ( 28 ).
- Full pipeline: registration [MotionCor2] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [RELION v3.0]

### Influenza chimeric hemagglutinin structures in complex with broadly protective antibodies to the stem and trimer interface. (PNAS 2022)

- DOI: 10.1073/pnas.2200821119 | PMCID: PMC9173763 | PMID: 35594401
- Evidence: Micrographs were collected using Leginon, particles were picked using difference of Gaussian picker and Appion, and particles were classified and reconstructed in Relion ( 34 – 37 ).
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [PyMOL]

### Structural insights of a highly potent pan-neutralizing SARS-CoV-2 human monoclonal antibody. (PNAS 2022)

- DOI: 10.1073/pnas.2120976119 | PMCID: PMC9171815 | PMID: 35549549
- Version used: **3.1**
- Evidence: The Omicron-CoV-2-6P dataset particles were exported to Relion 3.1 ( 46 ) and downscaled to 1.14 Å/pixel to reduce computational demands resulting from a large box size.
- Full pipeline: normalisation [RELION v3.1] -> stage not stated [PHENIX]

### Phenol-soluble modulins PSMα3 and PSMβ2 form nanotubes that are cross-α amyloids. (PNAS 2022)

- DOI: 10.1073/pnas.2121586119 | PMCID: PMC9171771 | PMID: 35533283
- Evidence: Once the correct helical symmetry was determined, the full dataset of particles was run in RELION ( 94 ) to generate a final reconstruction.
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [EMAN2, RoseTTAFold, UCSF Chimera]

### The cyclic octapeptide antibiotic argyrin B inhibits translation by trapping EF-G on the ribosome during translocation. (PNAS 2022)

- DOI: 10.1073/pnas.2114214119 | PMCID: PMC9171646 | PMID: 35500116
- Version used: **3.0**
- Evidence: Particle images for the EF-G-ArgB-70S complex were aligned with MotionCor2 ( 55 ), picked using GAUTOMATCH ( https://www.mrc-lmb.cam.ac.uk/kzhang ) and processed (including final sharpening and automated b-factor application) using RELION 3.0 ( 56 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION v3.0] -> structure determination [PHENIX v1.14] -> stage not stated [ChimeraX, PyMOL, UCSF Chimera]

### Cryo-EM structures show the mechanistic basis of pan-peptidase inhibition by human α<sub>2</sub>-macroglobulin. (PNAS 2022)

- DOI: 10.1073/pnas.2200102119 | PMCID: PMC9181621 | PMID: 35500114
- Version used: **2.1**
- Evidence: All subsequent image processing was with RELION 2.1 ( 54 , 55 ) within Scipion ( 56 ), unless otherwise stated.
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4, Coot, RELION v2.1]

### Locations and in situ structure of the polymerase complex inside the virion of vesicular stomatitis virus. (PNAS 2022)

- DOI: 10.1073/pnas.2111948119 | PMCID: PMC9170060 | PMID: 35476516
- Version used: **3.0.8**
- Evidence: A total of 82,991 subtomograms containing M and N were extracted, aligned, and averaged with RELION 3.0.8 ( 48 ), resulting a 7.5 Å-resolution averaged density map on the basis of the gold-standard FSC = 0.143 criterion.
- Full pipeline: alignment/mapping [RELION v3.0.8] -> structure determination [IMOD, RELION v3.0.8]

### Cryoelectron microscopy of Na<sup>+</sup>,K<sup>+</sup>-ATPase in the two E2P states with and without cardiotonic steroids. (PNAS 2022)

- DOI: 10.1073/pnas.2123226119 | PMCID: PMC9169807 | PMID: 35380894
- Version used: **3.1**
- Evidence: Relion 3.1 ( 31 ) was used for the following image processing.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [RELION v3.1]

### Cryo-EM structure of RNA-induced tau fibrils reveals a small C-terminal core that may nucleate fibril formation. (PNAS 2022)

- DOI: 10.1073/pnas.2119952119 | PMCID: PMC9169762 | PMID: 35377792
- Evidence: We used RELION to perform particle extraction, 2D classification, helical reconstruction, and 3D refinement ( 58 , 59 ).
- Full pipeline: registration [CTFFIND v4.1.8] -> structure determination [RELION] -> stage not stated [EMAN2, ImageJ]

### Cryo-EM structures of staphylococcal IsdB bound to human hemoglobin reveal the process of heme extraction. (PNAS 2022)

- DOI: 10.1073/pnas.2116708119 | PMCID: PMC9168843 | PMID: 35357971
- Evidence: The single-particle analysis of the IsdB:metHb complex was carried out using RELION ( 51 ).
- Full pipeline: stage not stated [Coot, PHENIX, PyMOL, RELION, UCSF Chimera]

### Structural conservation among variants of the SARS-CoV-2 spike postfusion bundle. (PNAS 2022)

- DOI: 10.1073/pnas.2119467119 | PMCID: PMC9169775 | PMID: 35363556
- Evidence: All datasets were processed with the RELION-3 package ( 45 ) except when explicitly noted ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [CTFFIND, ChimeraX, Coot, PyMOL, Python, RELION, UCSF Chimera]

### Structural insights into the activation of autoinhibited human lipid flippase ATP8B1 upon substrate binding. (PNAS 2022)

- DOI: 10.1073/pnas.2118656119 | PMCID: PMC9168909 | PMID: 35349344
- Evidence: Particles were automatically extracted by RELION with binning factor 2.
- Full pipeline: structure determination [PHENIX] -> stage not stated [Coot, MotionCor2, RELION, UCSF Chimera]

### 50S subunit recognition and modification by the &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; ribosomal RNA methyltransferase TlyA. (PNAS 2022)

- DOI: 10.1073/pnas.2120352119 | PMCID: PMC9168844 | PMID: 35357969
- Evidence: S2 , image alignment and dose-weighting were performed using Motioncor2 ( 51 ) and RELION-3.0/3.1 ( 52 ) was used for subsequent data processing.
- Full pipeline: alignment/mapping [Clustal Omega, RELION] -> stage not stated [CTFFIND, Coot, PHENIX v1.19.2]

### Clamping of DNA shuts the condensin neck gate. (PNAS 2022)

- DOI: 10.1073/pnas.2120006119 | PMCID: PMC9168836 | PMID: 35349345
- Version used: **3.1**
- Evidence: Processing was performed with RELION 3.1, CtfFind4, crYOLO, and cryoSPARC v3.2 ( 34 – 37 ), and RELION was used, unless otherwise specified.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, PyMOL v2.5, RELION v3.1, UCSF Chimera]

### Conformational snapshots of the bacitracin sensing and resistance transporter BceAB. (PNAS 2022)

- DOI: 10.1073/pnas.2123268119 | PMCID: PMC9169098 | PMID: 35349335
- Version used: **3.0**
- Evidence: For the nucleotide-free conformation of wild-type BceAB, heterogeneous refinement in cryoSPARC was followed by classification with residual signal subtraction in Relion 3.0 ( 30 ) to isolate a particle population showing the highest resolution features in the TM and extracellular regions.
- Full pipeline: structure determination [RELION v3.0, RoseTTAFold]

### Structural basis for the oligomerization-mediated regulation of NLRP3 inflammasome activation. (PNAS 2022)

- DOI: 10.1073/pnas.2121353119 | PMCID: PMC8931350 | PMID: 35254907
- Version used: **3.1**
- Evidence: Cryo-EM data were analyzed using RELION 3.1 ( 52 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, MotionCor2, PyMOL, RELION v3.1]

### Molecular basis of multistep voltage activation in plant two-pore channel 1. (PNAS 2022)

- DOI: 10.1073/pnas.2110936119 | PMCID: PMC8892357 | PMID: 35210362
- Evidence: These particle sets were then subjected to gold-standard or resolution-limited refinement in RELION and cisTEM, respectively.
- Full pipeline: structure determination [Coot, PHENIX, RELION] -> visualisation [UCSF Chimera] -> stage not stated [MotionCor2]

### Universal stabilization of the influenza hemagglutinin by structure-based redesign of the pH switch regions. (PNAS 2022)

- DOI: 10.1073/pnas.2115379119 | PMCID: PMC8833195 | PMID: 35131851
- Version used: **3.1**
- Evidence: For 2D class-averaged images, 80 to 200 images were collected, and ∼60,000 to 240,000 particles were picked, classified, and averaged using RELION 3.1 ( 43 ).
- Full pipeline: structure determination [CCP4] -> stage not stated [ImageJ, RELION v3.1]

### Munc13 structural transitions and oligomers that may choreograph successive stages in vesicle priming for neurotransmitter release. (PNAS 2022)

- DOI: 10.1073/pnas.2121259119 | PMCID: PMC8851502 | PMID: 35135883
- Version used: **3.1**
- Evidence: S2 ) via a multistage workflow that involved an iterative process including subtomogram averaging and 3D classification using the emClarity, RELION 3.1 and Warp/M software packages ( 42 – 46 ).
- Full pipeline: stage not stated [AlphaFold, RELION v3.1]

### Rearrangement of a unique Kv1.3 selectivity filter conformation upon binding of a drug. (PNAS 2022)

- DOI: 10.1073/pnas.2113536119 | PMCID: PMC8812516 | PMID: 35091471
- Evidence: Particles were auto picked using the Laplasian function in Relion with 200- to 250-Å-sized particles.
- Full pipeline: alignment/mapping [MotionCor2] -> registration [MotionCor2] -> simulation/modelling [UCSF Chimera, VMD] -> structure determination [PHENIX] -> stage not stated [CTFFIND, NAMD, RELION]

### Annealing synchronizes the 70<i>S</i> ribosome into a minimum-energy conformation. (PNAS 2022)

- DOI: 10.1073/pnas.2111231119 | PMCID: PMC8872765 | PMID: 35177473
- Version used: **3.0.8**
- Evidence: Particles files, including both .star and .mrcs, were selected after autorefinement with RELION 3.0.8 ( 67 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.17.1, RELION v3.0.8] -> stage not stated [CTFFIND, Python, UCSF Chimera v1.16]

### Structure of the Mon1-Ccz1 complex reveals molecular basis of membrane binding for Rab7 activation. (PNAS 2022)

- DOI: 10.1073/pnas.2121494119 | PMCID: PMC8833172 | PMID: 35105815
- Evidence: Per-particle contrast transfer function correction followed by 3D classification and postprocessing was performed in Relion ( 37 ).
- Full pipeline: machine learning [PHENIX] -> stage not stated [Coot, RELION]

### Structures of the peptidase-containing ABC transporter PCAT1 under equilibrium and nonequilibrium conditions. (PNAS 2022)

- DOI: 10.1073/pnas.2120534119 | PMCID: PMC8794836 | PMID: 35074919
- Evidence: Particle picking, two-dimensional (2D) classification, and 3D classification were performed using RELION-3 ( 25 ).
- Full pipeline: alignment/mapping [CTFFIND] -> dimensionality reduction/clustering [RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [Coot, PHENIX]

### High-resolution cryo-electron microscopy structure of photosystem II from the mesophilic cyanobacterium, <i>Synechocystis</i> sp. PCC 6803. (PNAS 2022)

- DOI: 10.1073/pnas.2116765118 | PMCID: PMC8740770 | PMID: 34937700
- Version used: **3.1**
- Evidence: Data processing was performed using Relion 3.1 ( 76 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [RELION v3.1, UCSF Chimera]

### Molecular basis of differential receptor usage for naturally occurring CD55-binding and -nonbinding coxsackievirus B3 strains. (PNAS 2022)

- DOI: 10.1073/pnas.2118590119 | PMCID: PMC8794823 | PMID: 35046043
- Evidence: After that, the 4× binned particle images were extracted and subjected to reference-free two-dimensional (2D) classification with RELION-3.0.8.
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [PHENIX] -> stage not stated [Coot, MotionCor2, PyMOL]

### Structural transitions in the GTP cap visualized by cryo-electron microscopy of catalytically inactive microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2114994119 | PMCID: PMC8764682 | PMID: 34996871
- Evidence: Data processing was done mostly within the RELION framework ( 37 ).
- Full pipeline: alignment/mapping [MotionCor2 v2.1] -> normalisation [PyMOL] -> structure determination [PHENIX] -> stage not stated [RELION]

### Tau filaments from amyotrophic lateral sclerosis/parkinsonism-dementia complex adopt the CTE fold. (PNAS 2023)

- DOI: 10.1073/pnas.2306767120 | PMCID: PMC10743375 | PMID: 38100415
- Evidence: Datasets were processed in RELION using standard helical reconstruction ( 53 ).
- Full pipeline: structure determination [RELION] -> visualisation [ChimeraX] -> stage not stated [Coot]

### Structural basis of substrate progression through the bacterial chaperonin cycle. (PNAS 2023)

- DOI: 10.1073/pnas.2308933120 | PMCID: PMC10723157 | PMID: 38064510
- Version used: **3.1**
- Evidence: Particle coordinates (.box files) were imported into RELION v.3.1 ( 49 ).
- Full pipeline: stage not stated [CTFFIND, Python, RELION v3.1]

### Structure determination by cryoEM at 100 keV. (PNAS 2023)

- DOI: 10.1073/pnas.2312905120 | PMCID: PMC10710074 | PMID: 38011573
- Version used: **4.0**
- Evidence: The movies were imported into RELION 4.0 ( 47 ) for motion correction, CTF estimation using CTFFIND-4.0 ( 10 ), and particle picking.
- Full pipeline: registration [CTFFIND, RELION v4.0]

### Vimentin regulates nuclear segmentation in neutrophils. (PNAS 2023)

- DOI: 10.1073/pnas.2307389120 | PMCID: PMC10691343 | PMID: 37983515
- Version used: **2.1**
- Evidence: A total of 34,248 subtomograms (2× binned) with a box size of 60 cubic pixels were cropped along the traced filaments with 4 nm space using helical tools in RELION 2.1 ( 39 ) and WARP.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [MotionCor2, RELION v2.1]

### Molecular basis for Nse5-6 mediated regulation of Smc5/6 functions. (PNAS 2023)

- DOI: 10.1073/pnas.2310924120 | PMCID: PMC10636319 | PMID: 37903273
- Version used: **3.0**
- Evidence: All other steps of image processing were performed by RELION 3.0 ( 24 ) and Cryosparc v3.3.0 ( 25 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [ColabFold, RELION v3.0]

### Synaptophysin chaperones the assembly of 12 SNAREpins under each ready-release vesicle. (PNAS 2023)

- DOI: 10.1073/pnas.2311484120 | PMCID: PMC10636311 | PMID: 37903271
- Version used: **3.1**
- Evidence: The image processing was done using RELION 3.1 ( 47 ).
- Full pipeline: stage not stated [CTFFIND, ImageJ, MotionCor2, RELION v3.1]

### Identification of a carbonic anhydrase-Rubisco complex within the alpha-carboxysome. (PNAS 2023)

- DOI: 10.1073/pnas.2308600120 | PMCID: PMC10614612 | PMID: 37862384
- Version used: **3.1**
- Evidence: Superresolution electron micrograph movies were aligned using MOTIONCOR2 ( 61 ) from within RELION 3.1 or using the CPU implementation of motion correction within RELION 3.1.
- Full pipeline: alignment/mapping [MUSCLE, RELION v3.1] -> quantification [ImageJ] -> registration [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, IQ-TREE, PyMOL] -> stage not stated [CTFFIND v4.1]

### Molecular basis of signal transduction mediated by the human GIPR splice variants. (PNAS 2023)

- DOI: 10.1073/pnas.2306145120 | PMCID: PMC10576055 | PMID: 37792509
- Evidence: Automated particle selection and data processing were performed using cryoSPARC v3.2.0+211012 and RELION-3.0 beta2 ( 62 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2021.4] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX v1.2.4] -> stage not stated [CTFFIND v1.06, ImageJ, RELION]

### Structural insights into the interaction of three Y-shaped ligands with PI3Kα. (PNAS 2023)

- DOI: 10.1073/pnas.2304071120 | PMCID: PMC10450665 | PMID: 37585458
- Evidence: Automated particle selection and further data processing were performed on a binned dataset using cryoSPARC (v3.3.2) and RELION-3.0-beta2.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot v0.9.4.1] -> visualisation [ChimeraX v1.0, PyMOL v2.1, UCSF Chimera v1.13.1] -> stage not stated [CTFFIND v1.06, PHENIX v1.18.2, RELION]

### Two conformations of the Tom20 preprotein receptor in the TOM holo complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301447120 | PMCID: PMC10450662 | PMID: 37579144
- Evidence: Images were processed using Relion-4.0 ( 48 ).
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, ChimeraX, MotionCor2, RELION]

### Transition State of Arp2/3 Complex Activation by Actin-Bound Dimeric Nucleation-Promoting Factor. (PNAS 2023)

- DOI: 10.1073/pnas.2306165120 | PMCID: PMC10434305 | PMID: 37549294
- Version used: **3.1**
- Evidence: Datasets were processed with cryoSPARC v3.1.1 ( 48 ) and Relion 3.1 ( 49 ) ( SI Appendix , Fig.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.1]

### The structure of <i>Plasmodium falciparum</i> multidrug resistance protein 1 reveals an N-terminal regulatory domain. (PNAS 2023)

- DOI: 10.1073/pnas.2219905120 | PMCID: PMC10410737 | PMID: 37527341
- Version used: **3.0**
- Evidence: Beam-induced motion correction and dose weighting were performed on the collected movie stacks using MotionCor2 ( 53 ) implemented in RELION 3.0 ( 54 ) with a binning factor of 2 (pixel size 1.10 Å).
- Full pipeline: registration [MotionCor2, RELION v3.0] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [UCSF Chimera]

### AcrIIC4 inhibits type II-C Cas9 by preventing R-loop formation. (PNAS 2023)

- DOI: 10.1073/pnas.2303675120 | PMCID: PMC10400994 | PMID: 37494395
- Version used: **3.1**
- Evidence: Data were processed by Relion 3.1, and finally, a map with 3.09 Å resolution was obtained.
- Full pipeline: structure determination [PHENIX] -> stage not stated [RELION v3.1]

### An expandable, modular de novo protein platform for precision redox engineering. (PNAS 2023)

- DOI: 10.1073/pnas.2306046120 | PMCID: PMC10400981 | PMID: 37487099
- Version used: **3.1**
- Evidence: A total of 25,025 particles using RELION 3.1 ( 47 ) from 200 images were picked, and reference free two-dimensional classification was performed leading to 13,396 particles included in final 2D class averages ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [CTFFIND, MotionCor2] -> normalisation [CTFFIND, MotionCor2] -> dimensionality reduction/clustering [RELION v3.1]

### Efficient tagging of endogenous proteins in human cell lines for structural studies by single-particle cryo-EM. (PNAS 2023)

- DOI: 10.1073/pnas.2302471120 | PMCID: PMC10401002 | PMID: 37487103
- Evidence: For GAPDH Krios datasets, motion-correction and dose weighting were performed using MotionCor2 implemented in Relion ( 73 ).
- Full pipeline: structure determination [PHENIX] -> machine learning [Cellpose] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [CTFFIND, Coot, ImageJ, MotionCor2, RELION, Topaz]

### Structures and membrane interactions of native serotonin transporter in complexes with psychostimulants. (PNAS 2023)

- DOI: 10.1073/pnas.2304602120 | PMCID: PMC10629533 | PMID: 37436958
- Evidence: Next, a round of 3D classification without image alignment was performed in RELION-3.1 ( 83 ), with a soft mask excluding the constant domain of 15B8 Fab and micelle.
- Full pipeline: alignment/mapping [RELION] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [CTFFIND, MotionCor2, VMD]

### Elucidating interprotein energy transfer dynamics within the antenna network from purple bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2220477120 | PMCID: PMC10334754 | PMID: 37399405
- Version used: **3.0**
- Evidence: Data processing was carried out using Relion 3.0 suite ( 81 ).
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [ChimeraX, RELION v3.0]

### 30S subunit recognition and G1405 modification by the aminoglycoside-resistance 16S ribosomal RNA methyltransferase RmtC. (PNAS 2023)

- DOI: 10.1073/pnas.2304128120 | PMCID: PMC10288597 | PMID: 37307464
- Version used: **3.1**
- Evidence: Image processing was conducted in Relion 3.1 ( 37 ).
- Full pipeline: registration [CTFFIND] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, RELION v3.1, UCSF Chimera]

### Structural insights into the assembly of the agrin/LRP4/MuSK signaling complex. (PNAS 2023)

- DOI: 10.1073/pnas.2300453120 | PMCID: PMC10266037 | PMID: 37252960
- Evidence: Particles from the classes with fine structural feature were selected for 3D classification using an initial model generated from a subset of the particles in RELION.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, RELION]

### Cryo-EM structure of the Mon1-Ccz1-RMC1 complex reveals molecular basis of metazoan RAB7A activation. (PNAS 2023)

- DOI: 10.1073/pnas.2301725120 | PMCID: PMC10235969 | PMID: 37216550
- Version used: **3.1**
- Evidence: The resulting picked particles were extracted in Relion 3.1 ( 38 ).
- Full pipeline: structure determination [PHENIX v1.19] -> machine learning [EMAN2] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ImageJ, RELION v3.1]

### Molecular mechanism of fatty acid activation of FFAR1. (PNAS 2023)

- DOI: 10.1073/pnas.2219569120 | PMCID: PMC10235965 | PMID: 37216523
- Version used: **3.1**
- Evidence: Movie frames of the hFFAR1-mG sqiN -scFv16 complex in the presence of different ligands were processed in Relion 3.1 ( 44 ).
- Full pipeline: normalisation [MotionCor2] -> registration [MotionCor2] -> simulation/modelling [NAMD v2.14] -> structure determination [Coot v0.9.4.1, PHENIX v1.19.2] -> stage not stated [R v3.50, RELION v3.1, UCSF Chimera v1.3]

### Structural insights into the transcription activation mechanism of the global regulator GlnR from actinobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2300282120 | PMCID: PMC10235972 | PMID: 37216560
- Version used: **3.1**
- Evidence: From the summed images, approximately 10,000 particles were manually picked and subjected to 2D classification in RELION 3.1 ( 59 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [PyMOL, RELION v3.1]

### Starvation sensing by mycobacterial RelA/SpoT homologue through constitutive surveillance of translation. (PNAS 2023)

- DOI: 10.1073/pnas.2302006120 | PMCID: PMC10235957 | PMID: 37216503
- Evidence: After motion correction of micrograph frames using MotionCor2 ( 58 ), images were processed using the pipeline of RELION ( 59 ).
- Full pipeline: registration [MotionCor2, RELION] -> stage not stated [PHENIX]

### The membrane electric field regulates the PIP<sub>2</sub>-binding site to gate the KCNQ1 channel. (PNAS 2023)

- DOI: 10.1073/pnas.2301985120 | PMCID: PMC10214144 | PMID: 37192161
- Version used: **4.0**
- Evidence: Data processing was carried out using cryoSPARC v3.3.1 ( 62 ) and RELION 4.0 ( 63 ).
- Full pipeline: structure determination [ChimeraX v1.2.0, PHENIX, PyMOL] -> stage not stated [RELION v4.0]

### Membrane protein isolation and structure determination in cell-derived membrane vesicles. (PNAS 2023)

- DOI: 10.1073/pnas.2302325120 | PMCID: PMC10160969 | PMID: 37098056
- Evidence: The raw movies were motion-corrected by MotionCor2 ( 55 ) in Relion V3.1 ( 56 ).
- Full pipeline: dimensionality reduction/clustering [Topaz] -> machine learning [Topaz] -> stage not stated [MotionCor2, RELION]

### Mechanistic insights into DNA binding and cleavage by a compact type I-F CRISPR-Cas system in bacteriophage. (PNAS 2023)

- DOI: 10.1073/pnas.2215098120 | PMCID: PMC10161043 | PMID: 37094126
- Version used: **3.0**
- Evidence: Particle picking, two-dimensional (2D) and three-dimensional (3D) classification, and reconstruction steps were performed using RELION 3.0.
- Full pipeline: quantification [ImageJ] -> registration [MotionCor2] -> dimensionality reduction/clustering [RELION v3.0] -> structure determination [PHENIX, RELION v3.0] -> visualisation [PyMOL]

### In situ architecture and membrane fusion of SARS-CoV-2 Delta variant. (PNAS 2023)

- DOI: 10.1073/pnas.2213332120 | PMCID: PMC10160983 | PMID: 37094167
- Evidence: Micrographs were motion-corrected and dose-weighted using RELION implementation of MotionCor2 ( 38 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD, PHENIX] -> stage not stated [Coot, MotionCor2, RELION, ilastik]

### Autocorrelation analysis for cryo-EM with sparsity constraints: Improved sample complexity and projection-based algorithms. (PNAS 2023)

- DOI: 10.1073/pnas.2216507120 | PMCID: PMC10161091 | PMID: 37094135
- Evidence: 3 shows that Algorithm 2 obtains a reasonable ab initio model within roughly 1,000 iterations, which can then be refined using other software packages like RELION or cryoSPARC ( 20 , 25 , 26 ).
- Full pipeline: structure determination [RELION] -> visualisation [UCSF Chimera]

### Structural insights into HIV-1 polyanion-dependent capsid lattice formation revealed by single particle cryo-EM. (PNAS 2023)

- DOI: 10.1073/pnas.2220545120 | PMCID: PMC10160977 | PMID: 37094124
- Version used: **4.0**
- Evidence: SPA image processing was done in RELION 4.0 ( 58 ) [maintained by SBGrid ( 59 )] and CryoSPARC ( 60 ), and motion correction and CTF estimation were carried out using MOTIONCOR2 ( 61 ) and GCTF ( 62 ).
- Full pipeline: registration [RELION v4.0] -> structure determination [ChimeraX, Coot, PHENIX, UCSF Chimera]

### Two structural switches in HIV-1 capsid regulate capsid curvature and host factor binding. (PNAS 2023)

- DOI: 10.1073/pnas.2220557120 | PMCID: PMC10120081 | PMID: 37040417
- Evidence: Dose-fractionated movies were aligned, dose-weighted, and averaged with MotionCor2 ( 39 ) in RELION-4.0 ( 40 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [ChimeraX, PHENIX] -> stage not stated [UCSF Chimera]

### Interdigitated immunoglobulin arrays form the hyperstable surface layer of the extremophilic bacterium &lt;i&gt;Deinococcus radiodurans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2215808120 | PMCID: PMC10120038 | PMID: 37043530
- Evidence: Initially, side views of S-layer sheets were first manually picked along the edge of the lattice using the helical picking tab in RELION while setting the helical rise to 40 Å.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold v2.2.0, ChimeraX, MotionCor2, RELION]

### High-throughput cryo-ET structural pattern mining by unsupervised deep iterative subtomogram clustering. (PNAS 2023)

- DOI: 10.1073/pnas.2213149120 | PMCID: PMC10104553 | PMID: 37027429
- Evidence: For comparison, we applied template matching, manual curation, subtomogram averaging, and classification by Relion ( 60 ) to recover the ribosome structure, which is referred to hereafter as the template-matching approach.
- Full pipeline: stage not stated [RELION]

### Yeast PIC-Mediator structure with RNA polymerase II C-terminal domain. (PNAS 2023)

- DOI: 10.1073/pnas.2220542120 | PMCID: PMC10104585 | PMID: 37014863
- Evidence: Subsequent steps of image processing were performed with RELION-3 (version 3.1.0) ( 34 – 36 ) unless stated otherwise. three-dimensional (3D) classifications and refinements are referred to as “focused” if local masking was applied.
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [PHENIX, RELION] -> visualisation [ChimeraX, PyMOL v2.4] -> stage not stated [AlphaFold, UCSF Chimera]

### A DNA damage-induced phosphorylation circuit enhances Mec1<sup>ATR</sup> Ddc2<sup>ATRIP</sup> recruitment to Replication Protein A. (PNAS 2023)

- DOI: 10.1073/pnas.2300150120 | PMCID: PMC10083555 | PMID: 36996117
- Evidence: ( B and C ) 2-dimensional (2D) classification analysis using RELION of three NSEM datasets for samples; Mec1–Ddc2 + Rfa1-NTD + 0.1 mM ZnCl 2 ; Mec1–Ddc2 + Rfa1-NTD; Mec1–Ddc2 + 0.1 mM ZnCl 2 (control).
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [PHENIX]

### Structural insights into constitutive activity of 5-HT<sub>6</sub> receptor. (PNAS 2023)

- DOI: 10.1073/pnas.2209917120 | PMCID: PMC10083584 | PMID: 36989299
- Version used: **3.1**
- Evidence: The data processing was performed in RELION 3.1 and obtained a final map at 3.0-Å resolution (details are provided in SI Appendix , Materials and Methods and Fig.
- Full pipeline: stage not stated [R v3.50, RELION v3.1]

### A general mechanism for transcription bubble nucleation in bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2220874120 | PMCID: PMC10083551 | PMID: 36972428
- Version used: **3.1**
- Evidence: Curated particles from class 1 and 2 were combined, refined using cryoSPARC Homogenous Refinement with Defocus and Global CTF Refinement enabled, and further processed using RELION 3.1 Bayesian Polishing ( 35 ).
- Full pipeline: quantification [ImageJ] -> normalisation [MotionCor2] -> differential/statistical testing [RELION v3.1] -> structure determination [ChimeraX, Coot, RELION v3.1] -> stage not stated [HMMER, PHENIX]

### Structure of mycobacterial respiratory complex I. (PNAS 2023)

- DOI: 10.1073/pnas.2214949120 | PMCID: PMC10068793 | PMID: 36952383
- Evidence: Image parameters were then converted to RELION ( 100 ) .star file format with pyem ( https://doi.org/10.5281/zenodo.3576630 ) and individual particle motion-correction was performed with Bayesian polishing ( 101 ), with the pixel size binned to 1.18 Å.
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [RELION] -> structure determination [PHENIX v1.19.2] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, Coot v0.9.6]

### Cryo-EM analyses of KIT and oncogenic mutants reveal structural oncogenic plasticity and a target for therapeutic intervention. (PNAS 2023)

- DOI: 10.1073/pnas.2300054120 | PMCID: PMC10068818 | PMID: 36943885
- Version used: **3.1**
- Evidence: 2D classification was performed using RELION 3.1 ( 28 ).
- Full pipeline: structure determination [PHENIX v1.02.1] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, RELION v3.1, UCSF Chimera]

### Structure-based design of a SARS-CoV-2 Omicron-specific inhibitor. (PNAS 2023)

- DOI: 10.1073/pnas.2300360120 | PMCID: PMC10068829 | PMID: 36940324
- Evidence: The data were processed using a combination of MotionCor2 ( 24 ), Gctf ( 25 ), EMAN2 ( 26 ), cryoSPARC ( 27 ), and RELION ( 28 ), as described previously ( 14 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, MotionCor2, PyMOL, RELION, UCSF Chimera]

### Cryo-EM structure of the four-subunit <i>Rhodobacter sphaeroides</i> cytochrome <i>bc</i><sub>1</sub> complex in styrene maleic acid nanodiscs. (PNAS 2023)

- DOI: 10.1073/pnas.2217922120 | PMCID: PMC10041115 | PMID: 36913593
- Version used: **3.1**
- Evidence: Data processing was performed using Relion 3.1 ( 86 ) unless otherwise stated.
- Full pipeline: structure determination [Coot v0.9.6, PHENIX v1.19.2] -> stage not stated [AlphaFold, ChimeraX v1.3, RELION v3.1]

### Structural basis and dynamics of Chikungunya alphavirus RNA capping by nsP1 capping pores. (PNAS 2023)

- DOI: 10.1073/pnas.2213934120 | PMCID: PMC10041110 | PMID: 36913573
- Version used: **3.0**
- Evidence: Datasets were analyzed in parallel in Relion (version 3.0) ( 38 ) and cryoSPARC ( 39 ).
- Full pipeline: stage not stated [PHENIX, RELION v3.0, UCSF Chimera]

### Structures of brain-derived 42-residue amyloid-β fibril polymorphs with unusual molecular conformations and intermolecular interactions. (PNAS 2023)

- DOI: 10.1073/pnas.2218831120 | PMCID: PMC10089215 | PMID: 36893281
- Evidence: Cryo-EM images were processed and density maps were reconstructed with RELION software ( 18 , 24 ). ssNMR data were obtained at 14.1 T and 17.5 T, using Tecmag Redstone spectrometers, magic-angle spinning probes obtained from the research group of Drs.
- Full pipeline: simulation/modelling [Coot, NAMD, VMD] -> structure determination [Coot, RELION]

### A macrocyclic peptide inhibitor traps MRP1 in a catalytically incompetent conformation. (PNAS 2023)

- DOI: 10.1073/pnas.2220012120 | PMCID: PMC10089224 | PMID: 36893260
- Evidence: Individual movie frames were imported into RELION for processing ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX, REFMAC, UCSF Chimera] -> stage not stated [PyMOL, RELION]

### Structures of human gastrin-releasing peptide receptors bound to antagonist and agonist for cancer and itch therapy. (PNAS 2023)

- DOI: 10.1073/pnas.2216230120 | PMCID: PMC9963752 | PMID: 36724251
- Evidence: Data processing was performed using RELION-3.0 ( 91 ).
- Full pipeline: structure determination [ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [R v3.50, RELION]

### The SspB adaptor drives structural changes in the AAA+ ClpXP protease during ssrA-tagged substrate delivery. (PNAS 2023)

- DOI: 10.1073/pnas.2219044120 | PMCID: PMC9963277 | PMID: 36730206
- Version used: **3.1**
- Evidence: RELION 3.1 ( 34 ) was used for 2D/3D classification and refinement ( SI Appendix , Figs.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.14, RELION v3.1] -> stage not stated [ChimeraX]

### Structure and supramolecular organization of the canine distemper virus attachment glycoprotein. (PNAS 2023)

- DOI: 10.1073/pnas.2208866120 | PMCID: PMC9963377 | PMID: 36716368
- Version used: **3.1.1**
- Evidence: A total of 6.47 million particles were picked using the Laplacian-of-Gaussian (LoG) filter in Relion (version 3.1.1) ( 65 , 66 ) (step 2 in SI Appendix , Fig.
- Full pipeline: registration [MotionCor2 v1.4.0] -> simulation/modelling [VMD] -> structure determination [PHENIX v1.19] -> visualisation [VMD] -> stage not stated [ChimeraX v1.3, Coot, PyMOL v2.5.2, RELION v3.1.1, UCSF Chimera v1.12]

### Cryo-EM structure of the whole photosynthetic reaction center apparatus from the green sulfur bacterium <i>Chlorobaculum tepidum</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2216734120 | PMCID: PMC9945994 | PMID: 36693097
- Version used: **3.0**
- Evidence: For the whole RC complex, image processing was performed with cryoSPARC ( 49 ) and Relion 3.0 ( 50 ) using dose-weighted micrographs.
- Full pipeline: registration [MotionCor2] -> stage not stated [ChimeraX, PHENIX, RELION v3.0, UCSF Chimera]

### Destabilizing NF1 variants act in a dominant negative manner through neurofibromin dimerization. (PNAS 2023)

- DOI: 10.1073/pnas.2208960120 | PMCID: PMC9945959 | PMID: 36689660
- Evidence: Data processing was done using the RELION ( 32 ) software package.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, Coot, MotionCor2, RELION]

### Fine structure and assembly pattern of a minimal myophage Pam3. (PNAS 2023)

- DOI: 10.1073/pnas.2213727120 | PMCID: PMC9942802 | PMID: 36656854
- Version used: **3.1**
- Evidence: A total of 130,253 particles (800 × 800 pixels) were manually picked and extracted from the 6,087 micrographs and background-normalized using RELION 3.1 ( 36 ).
- Full pipeline: normalisation [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### prM-reactive antibodies reveal a role for partially mature virions in dengue virus pathogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2218899120 | PMCID: PMC9933121 | PMID: 36638211
- Evidence: Particles were then subjected to nonreference, 2D classification using RELION ( 65 ).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [MotionCor2, RELION, UCSF Chimera]

### Structural basis for regulation of SOS response in bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2217493120 | PMCID: PMC9926225 | PMID: 36598938
- Evidence: Subframes were aligned and summed using RELION’s own implementation of the UCSF MotionCor2 ( 40 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [Coot, PHENIX] -> stage not stated [ImageJ]

### SUMO enhances unfolding of SUMO-polyubiquitin-modified substrates by the Ufd1/Npl4/Cdc48 complex. (PNAS 2023)

- DOI: 10.1073/pnas.2213703120 | PMCID: PMC9910466 | PMID: 36574706
- Version used: **3.0**
- Evidence: Movies from each dataset were corrected for drift and dose-weighted with MotionCor2 in RELION 3.0 ( 58 ).
- Full pipeline: structure determination [PHENIX, Python] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, Coot, MotionCor2, RELION v3.0]

### GSK3β phosphorylation catalyzes the aggregation of tau into Alzheimer's disease-like filaments. (PNAS 2024)

- DOI: 10.1073/pnas.2414176121 | PMCID: PMC11670061 | PMID: 39693350
- Evidence: Fibrils were reconstructed using RELION-3.1.2 ( 34 , 35 ), with several rounds of 3D classification and refinement to optimize helical parameters.
- Full pipeline: structure determination [RELION]

### The C-terminal activating domain promotes pannexin 1 channel opening. (PNAS 2024)

- DOI: 10.1073/pnas.2411898121 | PMCID: PMC11665872 | PMID: 39671183
- Version used: **4.0**
- Evidence: Both frPanx1-ΔC and frPanx1-ΔC+CAD datasets were imported into RELION 4.0 ( 49 ) and motion corrected using MotionCorr2 ( 50 ), accessed through SBgrid.
- Full pipeline: registration [RELION v4.0] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Architecture of the Sap S-layer of &lt;i&gt;Bacillus anthracis&lt;/i&gt; revealed by integrative structural biology. (PNAS 2024)

- DOI: 10.1073/pnas.2415351121 | PMCID: PMC11665858 | PMID: 39652757
- Version used: **3.1**
- Evidence: A cylindrical half shell was used as the refinement mask at higher bin values and a shaped mask generated using RELION 3.1 ( 45 ) Mask Create was used later for lower bin values.
- Full pipeline: alignment/mapping [VMD] -> registration [MotionCor2] -> simulation/modelling [VMD] -> structure determination [RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, GROMACS, IMOD]

### Molecular architecture of synaptic vesicles. (PNAS 2024)

- DOI: 10.1073/pnas.2407375121 | PMCID: PMC11626200 | PMID: 39602275
- Evidence: Subtomogram averaging was performed in Dynamo ( 79 ) and Relion 4 ( 83 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> structure determination [IMOD] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, RELION]

### Calcineurin-fusion facilitates cryo-EM structure determination of a Family A GPCR. (PNAS 2024)

- DOI: 10.1073/pnas.2414544121 | PMCID: PMC11621825 | PMID: 39565314
- Evidence: Particles were autopicked using the templates in RELION and then subjected to 2D classification using cryoSPARC ( 30 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, UCSF Chimera] -> stage not stated [RELION]

### The structures of protein kinase A in complex with CFTR: Mechanisms of phosphorylation and noncatalytic activation. (PNAS 2024)

- DOI: 10.1073/pnas.2409049121 | PMCID: PMC11573500 | PMID: 39495916
- Version used: **4.0**
- Evidence: Further steps, including map reconstruction and resolution estimations, were carried out using RELION 4.0 ( 64 ) and CryoSPARC ( 65 ).
- Full pipeline: structure determination [PHENIX, RELION v4.0] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ImageJ, MotionCor2, UCSF Chimera]

### 2.6-Å resolution cryo-EM structure of a class Ia ribonucleotide reductase trapped with mechanism-based inhibitor N&lt;sub&gt;3&lt;/sub&gt;CDP. (PNAS 2024)

- DOI: 10.1073/pnas.2417157121 | PMCID: PMC11551348 | PMID: 39475643
- Evidence: Cryo-EM data processing was performed using the RELION-4.0 software suite ( 23 ), which was installed and configured by SBGrid ( 59 ).
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [Coot, RELION]

### Cryo-EM structure of the zinc-activated channel (ZAC) in the Cys-loop receptor superfamily. (PNAS 2024)

- DOI: 10.1073/pnas.2405659121 | PMCID: PMC11536092 | PMID: 39441630
- Evidence: Motion correction and further image processing were performed using RELION-3 ( 56 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> registration [RELION] -> structure determination [PHENIX] -> stage not stated [CTFFIND v4.1, ChimeraX, PyMOL, UCSF Chimera]

### Capturing a methanogenic carbon monoxide dehydrogenase/acetyl-CoA synthase complex via cryogenic electron microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2410995121 | PMCID: PMC11474084 | PMID: 39361653
- Version used: **4.0**
- Evidence: Cryo-EM data processing was carried out using a combination of cryoSPARC v3.3.2 ( 65 ), pyem v0.5 ( 72 ), RELION v4.0 ( 66 ), and cryoDRGN v0.3.4 ( 67 , 68 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [AlphaFold] -> stage not stated [ChimeraX, RELION v4.0, cryoDRGN v0.3.4]

### Binding adaptability of chemical ligands to polymorphic α-synuclein amyloid fibrils. (PNAS 2024)

- DOI: 10.1073/pnas.2321633121 | PMCID: PMC11363296 | PMID: 39172784
- Version used: **3.1**
- Evidence: Fibrils were manually picked using the “Manual picking” program in RELION 3.1 ( 63 ).
- Full pipeline: structure determination [ChimeraX, PHENIX v1.13, PyMOL v1.7.4.5, UCSF Chimera v1.13.1] -> visualisation [ChimeraX, PyMOL v1.7.4.5] -> stage not stated [CTFFIND, RELION v3.1]

### Structure of biofilm-forming functional amyloid PSMα1 from &lt;i&gt;Staphylococcus aureus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2406775121 | PMCID: PMC11331129 | PMID: 39116134
- Evidence: In contrast to the abundance of amyloid fiber structures solved with RELION ( 31 ), we are not aware of any other such high-resolution structure determined by CryoSPARC, which has been used successfully for single-particle cryo-EM analyses.
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [RELION] -> simulation/modelling [ChimeraX v1.7] -> structure determination [PHENIX]

### Structural basis for DNA recognition by a viral genome-packaging machine. (PNAS 2024)

- DOI: 10.1073/pnas.2406138121 | PMCID: PMC11331095 | PMID: 39116131
- Version used: **3.1.2**
- Evidence: Both datasets were processed in RELION 3.1.2 ( 40 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, Coot, RELION v3.1.2, Topaz]

### Structure of the flotillin complex in a native membrane environment. (PNAS 2024)

- DOI: 10.1073/pnas.2409334121 | PMCID: PMC11260169 | PMID: 38985763
- Evidence: We conducted 3D classification without image alignment in Relion to eliminate particles with low-resolution contributions to the reconstruction ( 61 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [AlphaFold, ChimeraX, PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [ColabFold, Coot]

### Structural determinants of ivabradine block of the open pore of HCN4. (PNAS 2024)

- DOI: 10.1073/pnas.2402259121 | PMCID: PMC11228525 | PMID: 38917012
- Evidence: Initial steps of data processing were performed using RELION-3.1, as detailed in SI Appendix .
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [PHENIX] -> stage not stated [RELION]

### Structural basis for activation of somatostatin receptor 5 by cyclic neuropeptide agonists. (PNAS 2024)

- DOI: 10.1073/pnas.2321710121 | PMCID: PMC11214081 | PMID: 38885377
- Version used: **4.0**
- Evidence: The 5,043 dose-fractionated movies were subjected to beam-induced motion correction using RELION 4.0 ( 46 ), and the contrast transfer function and the defocus parameters were estimated using CTFFIND4.1 ( 47 ).
- Full pipeline: registration [RELION v4.0] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, R v3.50]

### Allosteric activation of VCP, an AAA unfoldase, by small molecule mimicry. (PNAS 2024)

- DOI: 10.1073/pnas.2316892121 | PMCID: PMC11181084 | PMID: 38833472
- Evidence: Correction of interframe movement for each pixel and dose-weighting was performed using MotionCor2 or Relion’s own implementation ( 55 – 57 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [MotionCor2, RELION]

### Principles of peptide selection by the transporter associated with antigen processing. (PNAS 2024)

- DOI: 10.1073/pnas.2320879121 | PMCID: PMC11161800 | PMID: 38805290
- Evidence: In general, particles were autopicked from the motion-corrected micrographs with crYOLO using its general model ( 62 ), extracted in RELION ( 63 ), and imported into cryoSPARC ( 64 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, RELION]

### Cryo-EM structures elucidate the multiligand receptor nature of megalin. (PNAS 2024)

- DOI: 10.1073/pnas.2318859121 | PMCID: PMC11145282 | PMID: 38771880
- Version used: **3.1**
- Evidence: The data were processed by RELION ver.
- Full pipeline: registration [Topaz] -> structure determination [AlphaFold, Coot] -> visualisation [ChimeraX] -> stage not stated [RELION v3.1]

### <i>Myxococcus xanthus</i> encapsulin cargo protein EncD is a flavin-binding protein with ferric reductase activity. (PNAS 2024)

- DOI: 10.1073/pnas.2400426121 | PMCID: PMC11126975 | PMID: 38748579
- Version used: **4.0**
- Evidence: 142,667 particles were picked using the template-based autopicking feature of RELION 4.0 ( 56 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> structure determination [PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, ColabFold v1.5.3, MotionCor2, RELION v4.0]

### Three-dimensional architecture of ESCRT-III flat spirals on the membrane. (PNAS 2024)

- DOI: 10.1073/pnas.2319115121 | PMCID: PMC11098116 | PMID: 38709931
- Version used: **3.1**
- Evidence: All these coordinates were passed to Relion 3.1 ( 72 , 73 ) for 2D classification, 3D classification, and 3D refinement.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [RELION v3.1] -> stage not stated [AlphaFold, UCSF Chimera]

### Influence of lipid bilayer on the structure of the muscle-type nicotinic acetylcholine receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2319913121 | PMCID: PMC11087746 | PMID: 38683987
- Evidence: All subsequent image processing steps were performed in RELION ( 31 , 32 ).
- Full pipeline: alignment/mapping [CTFFIND, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, MotionCor2, RELION]

### C-type inactivation and proton modulation mechanisms of the TASK3 channel. (PNAS 2024)

- DOI: 10.1073/pnas.2320345121 | PMCID: PMC11046659 | PMID: 38630723
- Evidence: Movies acquired with K3 and Falcon IV detectors were subjected to motion correction for beam-induced drift and binning from superresolution to physical pixel size using MotionCor2 ( 52 ) and RELION’s own implementation (version: 4.0 beta2), respectively.
- Full pipeline: registration [MotionCor2, RELION] -> simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> stage not stated [CTFFIND, ChimeraX, PyMOL]

### Structure and dynamics of a pentameric KCTD5/CUL3/Gβγ E3 ubiquitin ligase complex. (PNAS 2024)

- DOI: 10.1073/pnas.2315018121 | PMCID: PMC11047111 | PMID: 38625940
- Evidence: The unsubtracted particle image set was subdivided into sets A, B, C, and D with cryoSPARC heterogeneous refinement and imported to RELION ( 63 ) for de novo map generation and initial 3D refinement.
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Structure and design of Langya virus glycoprotein antigens. (PNAS 2024)

- DOI: 10.1073/pnas.2314990121 | PMCID: PMC11032465 | PMID: 38593070
- Evidence: Bayesian polishing was done in Relion ( 83 ), followed by nonuniform refinement ( 84 ) another round of reference-free 2D classification and a final nonuniform refinement using cryoSPARC.
- Full pipeline: alignment/mapping [Topaz] -> differential/statistical testing [RELION] -> structure determination [PHENIX, RELION] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, ChimeraX]

### Structural and mechanistic basis of the central energy-converting methyltransferase complex of methanogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2315568121 | PMCID: PMC10998594 | PMID: 38530900
- Evidence: The full dataset was processed with RELION-3.1 ( 25 , 53 ).
- Full pipeline: alignment/mapping [AlphaFold] -> stage not stated [CTFFIND, PHENIX, RELION]

### Allosteric regulation of nitrate transporter NRT via the signaling protein PII. (PNAS 2024)

- DOI: 10.1073/pnas.2318320121 | PMCID: PMC10945777 | PMID: 38457518
- Version used: **3.1**
- Evidence: For the datasets of NrtBCD-ATP, a total of 3,366,180 particles were automatically picked from 4,233 micrographs using RELION 3.1 ( 52 ) and then subjected to reference-free 2D classification.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, MotionCor2, PyMOL, RELION v3.1]

### Human paraneoplastic antigen Ma2 (PNMA2) forms icosahedral capsids that can be engineered for mRNA delivery. (PNAS 2024)

- DOI: 10.1073/pnas.2307812120 | PMCID: PMC10945824 | PMID: 38437549
- Version used: **4.0**
- Evidence: Cryo-EM data were processed using RELION 4.0 ( 50 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, PyMOL, RELION v4.0, Topaz]

### Structural basis for CFTR inhibition by CFTR<sub>inh</sub>-172. (PNAS 2024)

- DOI: 10.1073/pnas.2316675121 | PMCID: PMC10927578 | PMID: 38422021
- Version used: **3.1**
- Evidence: All subsequent steps of map reconstruction and resolution estimation were carried out using RELION 3.1 ( 59 ) ( SI Appendix , Fig.
- Full pipeline: structure determination [PHENIX, RELION v3.1] -> stage not stated [MotionCor2]

### Sec7 regulatory domains scaffold autoinhibited and active conformations. (PNAS 2024)

- DOI: 10.1073/pnas.2318615121 | PMCID: PMC10927569 | PMID: 38416685
- Version used: **3.1**
- Evidence: Standard cryoEM data processing tools (MotionCor2, GCTF, CryoSPARC, and Relion 3.1) ( 60 – 63 ) were used to correct beam-induced motion, estimate contrast transfer function parameters, pick, sort, and symmetry expand particles, and refine and reconstruct the final maps.
- Full pipeline: alignment/mapping [cryoDRGN] -> structure determination [MotionCor2, PHENIX, RELION v3.1] -> stage not stated [AlphaFold, ChimeraX, ImageJ]

### Dark and Dronc activation in <i>Drosophila melanogaster</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2312784121 | PMCID: PMC10907274 | PMID: 38381783
- Version used: **3.1**
- Evidence: The particles from the good class were imported to Relion 3.1 for 3D classification.
- Full pipeline: registration [MotionCor2] -> stage not stated [RELION v3.1]

### Filament structure and subcellular organization of the bacterial intermediate filament-like protein crescentin. (PNAS 2024)

- DOI: 10.1073/pnas.2309984121 | PMCID: PMC10873595 | PMID: 38324567
- Version used: **3.1**
- Evidence: Remaining image processing steps involved the alternate use of Relion 3.1 ( 52 ) and cryoSPARC ( 53 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [IMOD, PHENIX] -> machine learning [Topaz] -> stage not stated [Coot, ImageJ, MotionCor2, RELION v3.1]

### Puromycin reveals a distinct conformation of neuronal ribosomes. (PNAS 2024)

- DOI: 10.1073/pnas.2306993121 | PMCID: PMC10873636 | PMID: 38315848
- Evidence: Cryo-EM movies were corrected for beam-induced motion using RELION’s implementation of the MotionCor2 algorithm ( 46 , 47 ).
- Full pipeline: visualisation [ChimeraX, UCSF Chimera] -> stage not stated [CTFFIND, ImageJ, MotionCor2, RELION]

### Graphene sandwich-based biological specimen preparation for cryo-EM analysis. (PNAS 2024)

- DOI: 10.1073/pnas.2309384121 | PMCID: PMC10835136 | PMID: 38252835
- Evidence: The particles were then imported into Relion ( 54 ) for several rounds of 2D and 3D classification and the final 3D reconstruction.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD, RELION] -> stage not stated [MotionCor2]

### Elf1 promotes Rad26's interaction with lesion-arrested Pol II for transcription-coupled repair. (PNAS 2024)

- DOI: 10.1073/pnas.2314245121 | PMCID: PMC10801861 | PMID: 38194460
- Evidence: All initial refinements and classifications were done in Relion 3 ( 45 ).
- Full pipeline: structure determination [PHENIX, RELION, UCSF Chimera] -> visualisation [ChimeraX]

### Structural basis of σ<sup>54</sup> displacement and promoter escape in bacterial transcription. (PNAS 2024)

- DOI: 10.1073/pnas.2309670120 | PMCID: PMC10786286 | PMID: 38170755
- Version used: **4.0**
- Evidence: All image processing was carried out in RELION 4.0 ( 32 ), using MOTIONCORR implementation in RELION ( 33 ) and CTFFIND4 ( 34 ) with particles picked using Topaz ( 35 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [RELION v4.0, Topaz]

### Substitution of Met-38 to Ile in γ-synuclein found in two patients with amyotrophic lateral sclerosis induces aggregation into amyloid. (PNAS 2024)

- DOI: 10.1073/pnas.2309700120 | PMCID: PMC10786281 | PMID: 38170745
- Evidence: Fibrils from roughly 100 micrographs were manually picked and the data were processed using RELION-4.
- Full pipeline: stage not stated [RELION]

### Cryo-EM structure of the Rift Valley fever virus envelope protein in complex with a potent neutralization antibody. (PNAS 2025)

- DOI: 10.1073/pnas.2514862122 | PMCID: PMC12745785 | PMID: 41401007
- Evidence: The block-based reconstruction, final 3D refinement, and postprocessing were conducted by RELION.
- Full pipeline: structure determination [Coot, PHENIX, RELION] -> stage not stated [AlphaFold, ChimeraX]

### Machine learning enables de novo multiepitope design of &lt;i&gt;Plasmodium falciparum&lt;/i&gt; circumsporozoite protein to target trimeric L9 antibody. (PNAS 2025)

- DOI: 10.1073/pnas.2512358122 | PMCID: PMC12704715 | PMID: 41337490
- Version used: **5.0**
- Evidence: Data processing was performed with Relion v5.0.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2023.2] -> structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX, PyMOL, RELION v5.0]

### Structural basis of modified ligand selectivity from N-terminal PAC1R alternative splicing. (PNAS 2025)

- DOI: 10.1073/pnas.2521157122 | PMCID: PMC12663942 | PMID: 41264251
- Version used: **3.1.2**
- Evidence: In short, motion correction ( 38 ) and CTF estimation with CTFFIND-4.1 ( 39 ) were used through RELION 3.1.2 or RELION 5.0 ( 40 , 41 ). crYOLO ( 42 ) picked particles were imported to cryoSPARC (version 3.3.2 or version 4.6.0 for PAC1sR-P27-G s data) for 2D classification, ab-initio reconstruction as well as nonuniform refinement ( 43 ).
- Full pipeline: registration [CTFFIND, RELION v3.1.2] -> structure determination [CTFFIND, RELION v3.1.2] -> stage not stated [ChimeraX, VMD]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Evidence: Briefly, dose-fractionated image stacks were imported into RELION ( 60 ) and subjected to motion correction with MotionCor2 ( 61 ).
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### Structure of the D1-Val185Asn mutated photosystem II complex with slow O-O bond formation reveals changes in the Cl1 water channel. (PNAS 2025)

- DOI: 10.1073/pnas.2522652122 | PMCID: PMC12663929 | PMID: 41237214
- Evidence: Cryo-EM single particle analysis was performed using cryoSPARC v4 ( 45 ) and then exporting final particles to Relion 4 ( 46 , 47 ) for final reconstruction.
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [ChimeraX]

### The mechanism of pathogenic α&lt;sub&gt;1&lt;/sub&gt;-antitrypsin aggregation in the human liver. (PNAS 2025)

- DOI: 10.1073/pnas.2507535122 | PMCID: PMC12646233 | PMID: 41231946
- Version used: **4.0**
- Evidence: Preprocessing of the EM data was performed within CryoSPARC (v4.0 and v4.3.1) for ZZ:9C5 Fab (dataset B) using Patch motion correction and Patch CTF estimation ( 51 ) as well as within RELION (v4.0) for ZZ:4B12 Fab :9C5 Fab (dataset A and C) using MotionCor2 (v1.4 and v1.5) and CTFFIND4 (v4.0 and v4.1) ( 52 – 54 ).
- Full pipeline: normalisation [PHENIX] -> registration [MotionCor2 v1.4, RELION v4.0] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX, PHENIX]

### Asymmetric gating of a homopentameric ion channel GLIC revealed by cryo-EM. (PNAS 2025)

- DOI: 10.1073/pnas.2512811122 | PMCID: PMC12582304 | PMID: 41129221
- Version used: **4.0.1**
- Evidence: A total of 511,578 particles obtained from this dataset were used for 3D refinement in RELION (v4.0.1) ( 83 ).
- Full pipeline: alignment/mapping [Coot v0.9.8.7] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.9.8.7, PHENIX, RELION v4.0.1] -> stage not stated [ChimeraX]

### Structural and functional analysis of the &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; MmpS5L5 efflux pump presages increased bedaquiline resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2516660122 | PMCID: PMC12501195 | PMID: 40986343
- Evidence: Tilt series alignment and tomogram generation were performed with RELION-5 ( 80 , 81 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION] -> structure determination [PHENIX v1.21.2] -> stage not stated [AlphaFold, ChimeraX, Coot v0.9.8.93]

### In situ structures of the &lt;i&gt;Legionella&lt;/i&gt; Dot/Icm T4SS identify the DotA-IcmX complex as the gatekeeper for effector translocation. (PNAS 2025)

- DOI: 10.1073/pnas.2516300122 | PMCID: PMC12501162 | PMID: 40986344
- Version used: **3.1**
- Evidence: Coordinates and orientation parameters were exported to RELION v3.1 for particle extraction ( 54 ).
- Full pipeline: alignment/mapping [PHENIX v1.21] -> structure determination [CTFFIND, ChimeraX, PHENIX v1.21] -> stage not stated [AlphaFold, Coot v0.8.9.1, IMOD, RELION v3.1]

### Structurally diverse viral inhibitors converge on a shared mechanism to stall the antigen transporter TAP. (PNAS 2025)

- DOI: 10.1073/pnas.2516676122 | PMCID: PMC12478189 | PMID: 40956880
- Evidence: For the BNLF2a dataset, particles were autopicked from the motion-corrected micrographs with crYOLO using its general model ( 65 ), extracted in RELION ( 66 ), and imported into cryoSPARC ( 67 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, RELION]

### How palytoxin transforms the Na&lt;sup&gt;+&lt;/sup&gt;,K&lt;sup&gt;+&lt;/sup&gt; pump into a cation channel. (PNAS 2025)

- DOI: 10.1073/pnas.2506450122 | PMCID: PMC12478176 | PMID: 40956884
- Evidence: Relion 4 ( 51 ) was used for subsequent image processing.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [RELION]

### Measuring multisubunit mechanics of geometrically programmed colloidal assemblies via cryo-EM multi-body refinement. (PNAS 2025)

- DOI: 10.1073/pnas.2500716122 | PMCID: PMC12452858 | PMID: 40924447
- Evidence: Image processing is performed using RELION-4 ( 68 ).
- Full pipeline: structure determination [ChimeraX] -> stage not stated [RELION]

### Mechanisms underlying allosteric modulation of antiseizure medication binding to synaptic vesicle protein 2A (SV2A). (PNAS 2025)

- DOI: 10.1073/pnas.2510239122 | PMCID: PMC12435242 | PMID: 40892927
- Version used: **3.1**
- Evidence: These particles were re-extracted at a box size of 330 or 336 pixels and were subjected to two rounds of Bayesian polishing in RELION v.3.1 ( 51 , 52 ).
- Full pipeline: differential/statistical testing [RELION v3.1] -> structure determination [Coot, PHENIX v1.20.1] -> stage not stated [AlphaFold]

### Critical role of extracellular loops in differential modulations of TTX-sensitive and TTX-resistant Na&lt;sub&gt;v&lt;/sub&gt; channels. (PNAS 2025)

- DOI: 10.1073/pnas.2510355122 | PMCID: PMC12358880 | PMID: 40768348
- Evidence: A total of 3,011,243 particles were automatically picked using RELION ( 55 – 57 ) from 5,780 collected micrographs.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [CTFFIND, PyMOL, RELION]

### Structural basis for anaerobic alkane activation by a multisubunit glycyl radical enzyme. (PNAS 2025)

- DOI: 10.1073/pnas.2510389122 | PMCID: PMC12358834 | PMID: 40758891
- Version used: **3.1**
- Evidence: Subsequent steps were performed using RELION 3.1 and RELION 4.0 software suites, ( 47 ) which were installed through SBGrid ( 48 ).
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [RELION v3.1]

### In situ cryo-ET visualization of mitochondrial depolarization and mitophagic engulfment. (PNAS 2025)

- DOI: 10.1073/pnas.2511890122 | PMCID: PMC12337332 | PMID: 40743392
- Evidence: For subtomogram averaging and template match picking, ATP synthase and prohibitin complexes were manually picked using Napari ( https://www.napari-hub.org/ ) and imported into Relion 5 for particle extraction and downstream processing ( https://github.com/3dem/relion ) (RRID:SCR_016274) ( 91 ).
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX, RELION, napari]

### Structures of &lt;i&gt;Chaetomium thermophilum&lt;/i&gt; TOM complexes with bound preproteins. (PNAS 2025)

- DOI: 10.1073/pnas.2507279122 | PMCID: PMC12305020 | PMID: 40674418
- Version used: **3.0**
- Evidence: To account for and correct for beam-induced motion and radiation damage, the Relion 3.0 implementation of MotionCorr was applied to 15,566 movies of the substrate-free TOM complex ( 46 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2, RELION v3.0]

### Molecular basis for substrate recognition and transport of mammalian taurine transporters. (PNAS 2025)

- DOI: 10.1073/pnas.2425549122 | PMCID: PMC12260568 | PMID: 40601627
- Evidence: Data processing was performed using the software packages cyroSPARC ( 49 ) and Relion ( 50 , 51 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PyMOL, RELION]

### Structure of the virulence-associated &lt;i&gt;Neisseria meningitidis&lt;/i&gt; filamentous bacteriophage MDAΦ. (PNAS 2025)

- DOI: 10.1073/pnas.2420157122 | PMCID: PMC12207478 | PMID: 40540604
- Evidence: All image processing was performed in RELION, apart from the 2D class average shown in SI Appendix , Fig.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION, Topaz]

### A distinct LHCI arrangement is recruited to photosystem I in Fe-starved green algae. (PNAS 2025)

- DOI: 10.1073/pnas.2500621122 | PMCID: PMC12207447 | PMID: 40523173
- Version used: **3.0**
- Evidence: All movies were aligned, gain corrected, and binned by two using MotionCorr2 implemented in RELION (v.3.0) ( 66 ).
- Full pipeline: alignment/mapping [RELION v3.0] -> structure determination [PHENIX v1.21.1] -> visualisation [ChimeraX v1.7.1] -> stage not stated [AlphaFold]

### Structural basis of the hepatitis B virus X protein in complex with DDB1. (PNAS 2025)

- DOI: 10.1073/pnas.2421325122 | PMCID: PMC12184330 | PMID: 40512786
- Evidence: Cryo-EM data were collected using Titan Krios G4 and processed using RELION.
- Full pipeline: simulation/modelling [AlphaFold] -> structure determination [ColabFold] -> stage not stated [RELION]

### Structure and organization of full-length epidermal growth factor receptor in extracellular vesicles by cryo-electron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2424678122 | PMCID: PMC12167996 | PMID: 40455995
- Evidence: Subtomogram Averaging of EGFR in RELION.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [IMOD] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX] -> visualisation [EMAN2] -> stage not stated [AlphaFold, ImageJ, MotionCor2, RELION]

### Arrestin recognizes GPCRs independently of the receptor state. (PNAS 2025)

- DOI: 10.1073/pnas.2501487122 | PMCID: PMC12107136 | PMID: 40372433
- Version used: **4.0**
- Evidence: Recorded EER files were processed in RELION 4.0 ( 42 , 43 ).
- Full pipeline: quantification [ImageJ] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND v4.1.14, RELION v4.0]

### Structure and evolution of photosystem I in the early-branching cyanobacterium &lt;i&gt;Anthocerotibacter panamensis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2427090122 | PMCID: PMC12107172 | PMID: 40366692
- Version used: **3.1**
- Evidence: The contrast transfer functions for the five micrographs were estimated with Ctffind-4.1.13 ( 57 ) within Relion 3.1 ( 58 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [IQ-TREE v2.2, RELION v3.1, UCSF Chimera]

### Electric field-induced pore constriction in the human K&lt;sub&gt;v&lt;/sub&gt;2.1 channel. (PNAS 2025)

- DOI: 10.1073/pnas.2426744122 | PMCID: PMC12107148 | PMID: 40366685
- Evidence: Data processing was carried out using cryoSPARC v3/v4 ( 61 ) and RELION 4/5 ( 62 ).
- Full pipeline: structure determination [ChimeraX v1.5, PHENIX, PyMOL] -> stage not stated [AlphaFold, RELION]

### Structure of the human TWIK-2 potassium channel and its inhibition by pimozide. (PNAS 2025)

- DOI: 10.1073/pnas.2425709122 | PMCID: PMC12088453 | PMID: 40343992
- Version used: **3.1**
- Evidence: For TWIK-2 without pimozide, image processing was performed in RELION 3.1 ( 84 ) and cryoSPARC v.4.5.0 ( 85 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.1]

### Quantitative spatial analysis of chromatin biomolecular condensates using cryoelectron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2426449122 | PMCID: PMC12088439 | PMID: 40327693
- Evidence: Both position and orientation were then further refined using Relion ( 53 ).
- Full pipeline: structure determination [RELION]

### Water-directed pinning is key to tau prion formation. (PNAS 2025)

- DOI: 10.1073/pnas.2421391122 | PMCID: PMC12067210 | PMID: 40294272
- Evidence: RELION-4.0 was used for image processing and EM map generation ( 74 – 76 ).
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [PHENIX, RELION]

### Subunit specialization in AAA+ proteins and substrate unfolding during transcription complex remodeling. (PNAS 2025)

- DOI: 10.1073/pnas.2425868122 | PMCID: PMC12054792 | PMID: 40273105
- Version used: **4.0**
- Evidence: All image processing steps were carried out in RELION 4.0 ( 27 ).
- Full pipeline: stage not stated [CTFFIND, RELION v4.0, Topaz]

### Reducing the effects of radiation damage in cryo-EM using liquid helium temperatures. (PNAS 2025)

- DOI: 10.1073/pnas.2421538122 | PMCID: PMC12054821 | PMID: 40261934
- Version used: **4.0**
- Evidence: To process the data, the tiff movies were imported into RELION 4.0 ( 41 ) and motion corrected with RELION’s own implementation of MotionCor2 ( 42 ).
- Full pipeline: alignment/mapping [Python] -> registration [MotionCor2, RELION v4.0] -> stage not stated [CTFFIND]

### Structural basis of excitatory amino acid transporter 3 substrate recognition. (PNAS 2025)

- DOI: 10.1073/pnas.2501627122 | PMCID: PMC12036983 | PMID: 40249774
- Evidence: For the hEAAT3-X with 10 mM L-Asp dataset, the movies were aligned using MotionCorr2 ( 72 ) implemented in Relion 4, and the micrograph CTF parameters were estimated using CtfFfind-4.1 ( 73 ).
- Full pipeline: alignment/mapping [RELION] -> structure determination [ChimeraX, PHENIX]

### Virion-associated influenza hemagglutinin clusters upon sialic acid binding visualized by cryoelectron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2426427122 | PMCID: PMC12037027 | PMID: 40244672
- Evidence: To generate Warp compatible metadata, Euler angles were converted from Dynamo to Relion convention using the eulerangle library and were written into a star file with its corresponding coordinate using the starfile library ( 41 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UCSF Chimera] -> structure determination [PHENIX] -> machine learning [EMAN2] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Matplotlib, Python, RELION, seaborn]

### NAL1 forms a molecular cage to regulate FZP phase separation. (PNAS 2025)

- DOI: 10.1073/pnas.2419961122 | PMCID: PMC12012508 | PMID: 40203040
- Version used: **3.1**
- Evidence: The main steps were performed for image processing using Relion 3.1 ( 41 ), and the initial models for the model building with Coot and refined with Phenix.
- Full pipeline: structure determination [PHENIX, RELION v3.1] -> stage not stated [AlphaFold]

### Structure of a Gcn2 dimer in complex with the large 60S ribosomal subunit. (PNAS 2025)

- DOI: 10.1073/pnas.2415807122 | PMCID: PMC12012509 | PMID: 40198700
- Version used: **4.0.1**
- Evidence: Processing was performed using CryoSPARC 4.4.1 (Structura Biotechnology Inc.) and RELION 4.0.1 ( 68 , 69 ).
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [ChimeraX, Coot, PHENIX, RELION v4.0.1]

### DNA bending mediated by ORC is essential for replication licensing in budding yeast. (PNAS 2025)

- DOI: 10.1073/pnas.2502277122 | PMCID: PMC12002289 | PMID: 40184174
- Evidence: Particles were automatically picked by Gautomatch ( https://github.com/JackZhang-Lab/Gautmatch ) and extracted by RELION ( 60 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [EMAN2, ImageJ, MotionCor2, RELION]

### The cryo-EM structure and physical basis for anesthetic inhibition of the THIK1 K2P channel. (PNAS 2025)

- DOI: 10.1073/pnas.2421654122 | PMCID: PMC12002230 | PMID: 40178898
- Version used: **3.1.2**
- Evidence: All data processing was performed in RELION 3.1.2 ( 52 ) and details of the data processing scheme and final processing results are described in SI Appendix, Figs.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, RELION v3.1.2]

### Structural elucidation of how ARF small GTPases induce membrane tubulation for vesicle fission. (PNAS 2025)

- DOI: 10.1073/pnas.2417820122 | PMCID: PMC11962421 | PMID: 40117306
- Evidence: Combining the iterative helical real-space reconstruction approach ( 27 ) with refinement using RELION ( 28 ) ( SI Appendix , Fig.
- Full pipeline: structure determination [RELION]

### Cryo-EM structures reveal the acetylation process of piccolo NuA4. (PNAS 2025)

- DOI: 10.1073/pnas.2414490122 | PMCID: PMC11962513 | PMID: 40100634
- Version used: **4.0**
- Evidence: Then, the particles were transferred to RELION 4.0, followed by a round of 3D classification without alignment ( 64 ).
- Full pipeline: alignment/mapping [RELION v4.0] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [AlphaFold, Coot]

### Structural mechanisms underlying the modulation of CXCR4 by diverse small-molecule antagonists. (PNAS 2025)

- DOI: 10.1073/pnas.2425795122 | PMCID: PMC11929458 | PMID: 40063796
- Version used: **5.0**
- Evidence: For the HF51116–CXCR4 κOR –Nb6 complex, 3,519 movies were collected and imported into RELION 5.0 ( 33 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> stage not stated [RELION v5.0]

### Structural basis of DNA replication fidelity of the Mpox virus. (PNAS 2025)

- DOI: 10.1073/pnas.2411686122 | PMCID: PMC11912389 | PMID: 40035768
- Evidence: We applied masked nonalignment 3D classification on the thumb domain using RELION-3.1 ( 50 ) and 66,359 particles were separated to reconstruct a 3.08 Å map of the holoenzyme complex in editing conformation ( SI Appendix , Fig.
- Full pipeline: structure determination [PHENIX, RELION] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2 v1.2.4]

### Structural basis of SARS-CoV-2 polymerase inhibition by nonnucleoside inhibitor HeE1-2Tyr. (PNAS 2025)

- DOI: 10.1073/pnas.2419854122 | PMCID: PMC11912441 | PMID: 40035759
- Evidence: The good particles were then subjected to 3D classification without image alignment in Relion ( 39 ) to separate fully assembled RdRp from smaller subcomplexes, which resulted in ~300,000 good particles of the RdRp complex.
- Full pipeline: alignment/mapping [RELION] -> normalisation [ChimeraX] -> stage not stated [Clustal Omega, PHENIX]

### Cryo-EM heterogeneity analysis using regularized covariance estimation and kernel regression. (PNAS 2025)

- DOI: 10.1073/pnas.2419140122 | PMCID: PMC11892586 | PMID: 40009640
- Evidence: In that case, the weights w are often set using the FSC regularization scheme ( 22 ); for example, it is the default method in popular cryo-EM software such as REgularization LIkelihood OptimisatioN (RELION) ( 22 ) and cryoSPARC ( 23 ).
- Full pipeline: dimensionality reduction/clustering [UMAP, cryoDRGN] -> structure determination [ChimeraX, UMAP, cryoDRGN] -> visualisation [UMAP] -> stage not stated [RELION]

### A structural atlas of death domain fold proteins reveals their versatile roles in biology and function. (PNAS 2025)

- DOI: 10.1073/pnas.2426986122 | PMCID: PMC11874512 | PMID: 39977327
- Evidence: ... all subsequent CARD oligomer or filament structures, and provided a useful benchmark for helical reconstructions in data processing packages such as Relion ( 67 ) and CryoSPARC ( 68 ).
- Full pipeline: structure determination [RELION] -> visualisation [PyMOL] -> stage not stated [AlphaFold]

### Structures and functions of the limited natural polyclonal antibody response to parvovirus infection. (PNAS 2025)

- DOI: 10.1073/pnas.2423460122 | PMCID: PMC11873831 | PMID: 39951487
- Evidence: Subvolumes were then 3D classified without symmetry or alignments in RELION-4.0 ( 68 ).
- Full pipeline: alignment/mapping [RELION] -> structure determination [PHENIX] -> stage not stated [ChimeraX]

### Structural characterization of influenza group 1 chimeric hemagglutinins as broad vaccine immunogens. (PNAS 2025)

- DOI: 10.1073/pnas.2416628122 | PMCID: PMC11848309 | PMID: 39937865
- Evidence: Particles were picked using a Difference of Gaussians (DoG) particle picker, classified, and reconstructed in Relion ( 59 – 62 ).
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [ChimeraX, PyMOL]

### Biochemical and structural bases for talin ABSs-F-actin interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2405922122 | PMCID: PMC11831117 | PMID: 39903122
- Version used: **3.1**
- Evidence: Motion correction and binning to a working pixel size of 0.83Å/pixel was carried out by MotionCor2 ( 52 ), defocus values were measured by CTFFIND 4.1 ( 53 ) and subsequent image analysis was carried out using RELION 3.1 ( 54 ).
- Full pipeline: registration [CTFFIND v4.1, MotionCor2, RELION v3.1] -> structure determination [PHENIX]

### Cryo-ET suggests tubulin chaperones form a subset of microtubule lumenal particles with a role in maintaining neuronal microtubules. (PNAS 2025)

- DOI: 10.1073/pnas.2404017121 | PMCID: PMC11804619 | PMID: 39888918
- Version used: **3.0.5**
- Evidence: Subtomogram analysis for lumenal particles was performed using RELION (version 3.0.5) following published protocols ( 91 ).
- Full pipeline: stage not stated [RELION v3.0.5]

### Structural insights into the role of reduced cysteine residues in SOD1 amyloid filament formation. (PNAS 2025)

- DOI: 10.1073/pnas.2408582122 | PMCID: PMC11804504 | PMID: 39874287
- Evidence: Using RELION-4.0 ( 51 – 53 ), 89 filaments were manually selected from WT SOD1 filaments and 16 from C6A/C111A mutant SOD1 filaments.
- Full pipeline: structure determination [PHENIX v1.21] -> visualisation [ChimeraX v1.4, PyMOL v3.0] -> stage not stated [CTFFIND, ImageJ, MotionCor2, RELION]

### Structure-guided engineering of a mutation-tolerant inhibitor peptide against variable SARS-CoV-2 spikes. (PNAS 2025)

- DOI: 10.1073/pnas.2413465122 | PMCID: PMC11789008 | PMID: 39854234
- Evidence: For all datasets, image processing was performed with the RELION-4.0 ( 54 , 55 ).
- Full pipeline: normalisation [Topaz] -> structure determination [PHENIX] -> stage not stated [CCP4, RELION]

### Molecular mechanism of ligand recognition and activation of lysophosphatidic acid receptor LPAR6. (PNAS 2025)

- DOI: 10.1073/pnas.2415426122 | PMCID: PMC11789011 | PMID: 39847322
- Evidence: Particles were picked with crYOLO ( 37 ), followed by reference-free 2D (2 dimensional) classification in RELION ( 38 ).
- Full pipeline: alignment/mapping [AlphaFold] -> dimensionality reduction/clustering [RELION] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v4.1, MotionCor2, R v3.50]

### Structural determinants of oxygen resistance and Zn&lt;sup&gt;2+&lt;/sup&gt;-mediated stability of the [FeFe]-hydrogenase from &lt;i&gt;Clostridium beijerinckii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2416233122 | PMCID: PMC11760498 | PMID: 39805018
- Evidence: Using a good 2D class average image, a total of 7,759,751 particle images were automatically picked and 2D classifications were performed using RELION-3.1 ( 48 ).
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, MotionCor2, RELION]

### Affinity maturation endows potent activity onto class 6 SARS-CoV-2 broadly neutralizing antibodies. (PNAS 2025)

- DOI: 10.1073/pnas.2417544121 | PMCID: PMC11725916 | PMID: 39746041
- Version used: **3.0**
- Evidence: These particles were exported to Relion 3.0 ( 47 ) to perform focused 3D classification on the Fab + RBD region, selecting particles that contained the 4C12-B12 Fab.
- Full pipeline: stage not stated [RELION v3.0]

### Computational-aided rational mutation design of pertuzumab to overcome active HER2 mutation S310F through antibody-drug conjugates. (PNAS 2025)

- DOI: 10.1073/pnas.2413686122 | PMCID: PMC11725927 | PMID: 39793038
- Version used: **3.0**
- Evidence: All other steps of image processing were performed using RELION 3.0( 36 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.0]

### Molecular basis of Spns1-mediated lysophospholipid transport from the lysosome. (PNAS 2025)

- DOI: 10.1073/pnas.2409596121 | PMCID: PMC11725778 | PMID: 39739806
- Version used: **3.1**
- Evidence: Motion correction was performed in RELION 3.1 using MotionCor2 ( 42 ) or its own implementation with an EER fractionation of 22 ( 43 ).
- Full pipeline: registration [MotionCor2, RELION v3.1] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, NAMD]

### Structural insight into sodium ion pathway in the bacterial flagellar stator from marine &lt;i&gt;Vibrio&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2415713122 | PMCID: PMC11725901 | PMID: 39793043
- Evidence: The image processing was performed using RELION-3.1 ( 49 ) and 4β ( 50 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CTFFIND v4.1, ChimeraX, RELION]

### Measurement of atomic scattering factors by cryoelectron microscopy. (PNAS 2026)

- DOI: 10.1073/pnas.2528758123 | PMCID: PMC13167779 | PMID: 42101996
- Evidence: The electrostatic potential maps were reconstructed from the acquired movies using RELION-4 ( 69 ).
- Full pipeline: registration [MotionCor2] -> structure determination [RELION] -> stage not stated [CCP4, Coot, PyMOL]

### Computational design of an ultrapotent deltacoronavirus miniprotein inhibitor. (PNAS 2026)

- DOI: 10.1073/pnas.2533456123 | PMCID: PMC13142991 | PMID: 42054371
- Version used: **3.0**
- Evidence: Particle data were transferred from cryoSPARC to RELION (v3.0, https://www3.mrclmb.cam.ac.uk/relion ) ( 76 , 77 ) using the pyem program package ( 78 ).
- Full pipeline: structure determination [ChimeraX, PHENIX, Topaz] -> stage not stated [AlphaFold, RELION v3.0]

### SUN5 forms a regular protein lattice reinforcing the sperm head-tail junction. (PNAS 2026)

- DOI: 10.1073/pnas.2520626123 | PMCID: PMC13012075 | PMID: 41855266
- Version used: **5.0**
- Evidence: Subsequently, tomograms and aligned particle coordinates were imported into Relion 5.0 ( 65 ).
- Full pipeline: alignment/mapping [IMOD v4.12.62, RELION v5.0] -> structure determination [IMOD v4.12.62] -> stage not stated [AlphaFold, ChimeraX]

### Direct evidence of acid-driven protein desolvation. (PNAS 2026)

- DOI: 10.1073/pnas.2525949123 | PMCID: PMC12974452 | PMID: 41785322
- Evidence: In detail, each of the collected datasets (p H 3.5: 3,725 images, p H 4: 2,308 images, p H 5: 2,541 images, p H 7: 1,891 images, p H 9: 1,867 images) was imported, corrected for beam-induced motion with RELION motioncorr ( 74 ), and CTF parameters were calculated with gctf ( 75 ).
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [ChimeraX, MDAnalysis, PHENIX] -> stage not stated [RELION, SciPy]

### Molecular architecture and diversity of StopGo/2A translational recoding. (PNAS 2026)

- DOI: 10.1073/pnas.2528667123 | PMCID: PMC12846837 | PMID: 41576085
- Evidence: Cryo-EM data were collected on a Titan Krios microscope and then processed in RELION; a molecular model was built using Coot and refined in Phenix.
- Full pipeline: structure determination [PHENIX, RELION]

### Structural characterization of the HDV virion and its ribonucleoprotein. (PNAS 2026)

- DOI: 10.1073/pnas.2519809123 | PMCID: PMC12846810 | PMID: 41564123
- Evidence: The particles were then exported to Relion for 3-D refinement and multibody refinement ( 54 ), which yielded split maps with nominal resolutions of 7.3 Å and 8.1 Å.
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [ChimeraX, Coot, Matplotlib, NumPy, SciPy, Topaz, UCSF Chimera]

### Molecular structure of the ESCRT-III-based archaeal CdvAB cell division machinery. (PNAS 2026)

- DOI: 10.1073/pnas.2525941123 | PMCID: PMC12818579 | PMID: 41543908
- Evidence: The SiCdvA ΔC and SaciCdvB2 filament structures were solved using helical reconstruction ( 53 ) in RELION-3 ( 54 ) and RELION-4 ( 55 ), respectively.
- Full pipeline: alignment/mapping [MAFFT, PyMOL] -> structure determination [Coot, PHENIX, RELION] -> visualisation [ChimeraX v1.7.1] -> stage not stated [AlphaFold, MotionCor2]

### Effect of natural mutations of SARS-CoV-2 on spike structure, conformation, and antigenicity. (Science 2021)

- DOI: 10.1126/science.abi6226 | PMCID: PMC8611377 | PMID: 34168071
- Evidence: RELION ( 57 ) software was used for particle picking and 2D and 3D class averaging.
- Full pipeline: alignment/mapping [PyMOL] -> dimensionality reduction/clustering [R] -> simulation/modelling [VMD] -> structure determination [ChimeraX, PHENIX] -> visualisation [PyMOL] -> stage not stated [RELION]

### Structural basis for enhanced infectivity and immune evasion of SARS-CoV-2 variants. (Science 2021)

- DOI: 10.1126/science.abi9745 | PMCID: PMC9245151 | PMID: 34168070
- Evidence: We used RELION ( 38 ) for particle picking, two-dimensional (2D) classification, 3D classification, and refinement (figs.
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [RELION]

### Structural impact on SARS-CoV-2 spike protein by D614G substitution. (Science 2021)

- DOI: 10.1126/science.abf2303 | PMCID: PMC8139424 | PMID: 33727252
- Evidence: We determined the cryoelectron microscopy (cryo-EM) structures of the full-length G614 S trimer using RELION ( 36 ).
- Full pipeline: stage not stated [RELION]

### Structure-guided multivalent nanobodies block SARS-CoV-2 infection and suppress mutational escape. (Science 2021)

- DOI: 10.1126/science.abe6230 | PMCID: PMC7932109 | PMID: 33436526
- Version used: **3.1**
- Evidence: For the VHH VE dataset, the particles from refinement job containing angular information was migrated from cryoSPARC to RELION 3.1 ( 62 ) for 3D classification without alignment (1.02 Å per pixel, 35 iterations, T = 8) and classified into four classes using reconstruction in cryoSPARC as reference map (low-pass filtered to 25Å).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2, RELION v3.1, SAMtools] -> variant calling [GATK] -> quantification [ImageJ] -> structure determination [PHENIX, RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [MACS2]

### RNA-activated protein cleavage with a CRISPR-associated endopeptidase. (Science 2022)

- DOI: 10.1126/science.add7450 | PMCID: PMC10028731 | PMID: 36423276
- Evidence: Cryo-EM data processing All cryo-EM data were processed using RELION-4.0 ( 36 ), compiled and configured by SBGRid ( 37 ).
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, Coot, Jupyter, MotionCor2, RELION]

### DNSN-1 recruits GINS for CMG helicase assembly during DNA replication initiation in &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (Science 2023)

- DOI: 10.1126/science.adi4932 | PMCID: PMC7615117 | PMID: 37590372
- Evidence: Cryo-EM data processing Data processing used RELION-4.0 ( 61 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, ImageJ, RELION]

### Specific tRNAs promote mRNA decay by recruiting the CCR4-NOT complex to translating ribosomes. (Science 2024)

- DOI: 10.1126/science.adq8587 | PMCID: PMC11583848 | PMID: 39571015
- Version used: **4.0**
- Evidence: Cryo-EM data processing Data were processed using Relion 4.0 ( 74 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [GSEA, RELION v4.0]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: Cryo-EM data processing All cryo-EM data were processed using RELION-4.0 ( 58 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Version used: **3.1**
- Evidence: Cryo-EM data processing For the full TIP60 complex data sets, the raw movies were subjected to motion correction and CTF estimation using RELION 3.1 software ( 99 – 101 ).
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Ciliopathy patient variants reveal organelle-specific functions for TUBB4B in axonemal microtubules. (Science 2024)

- DOI: 10.1126/science.adf5489 | PMCID: PMC7616230 | PMID: 38662826
- Evidence: Each particle had undergone at least one round of contrast transfer function refinement (CTFRefine) and Bayesian polishing in RELION-4.0 ( 70 ) and was a survivor from multiple rounds of three-dimensional classification.
- Full pipeline: alignment/mapping [IMOD, UCSF Chimera] -> quantification [ImageJ, Seurat, ilastik] -> dimensionality reduction/clustering [RELION] -> differential/statistical testing [RELION] -> structure determination [ChimeraX, IMOD, PHENIX, RELION] -> visualisation [ImageJ, ilastik] -> stage not stated [VEP]

### Molecular mechanism of dynein-dynactin complex assembly by LIS1. (Science 2024)

- DOI: 10.1126/science.adk8544 | PMCID: PMC7615804 | PMID: 38547289
- Evidence: Global motion correction and dose-weighting were performed in Relion-4.0 ( 99 ) using MotionCor2 ( 100 ) with a B-factor of 150 and 5X5 patches.
- Full pipeline: alignment/mapping [ChimeraX] -> quantification [R] -> registration [MotionCor2, RELION] -> differential/statistical testing [R] -> structure determination [PHENIX] -> machine learning [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ColabFold, ImageJ, UCSF Chimera]

### Native architecture of a human GBP1 defense complex for cell-autonomous immunity to infection. (Science 2024)

- DOI: 10.1126/science.abm9903 | PMCID: PMC12091997 | PMID: 38422126
- Evidence: Sub-tomograms were extracted and were initially aligned based on the feature of outer membrane (OM) by Relion package v3 ( 57 ).
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [EMAN2, UCSF Chimera] -> stage not stated [AlphaFold, CellProfiler, ImageJ]

### Precise targeting of HIV broadly neutralizing antibody precursors in humans. (Science 2025)

- DOI: 10.1126/science.adv5572 | PMCID: PMC12313413 | PMID: 40373114
- Version used: **4.0**
- Evidence: Data was automated using EPU Multigrid (TFS) and processed using Relion 4.0 ( 77 ).
- Full pipeline: alignment/mapping [Bowtie2] -> structure determination [Coot v0.9.8, PHENIX] -> stage not stated [ChimeraX, Nextflow, R, RELION v4.0, Trinity]

### Autoinhibition imposed by a large conformational switch of INO80 regulates nucleosome positioning. (Science 2025)

- DOI: 10.1126/science.adr3831 | PMCID: PMC12403922 | PMID: 40674492
- Evidence: To resolve this density, the selected particles were exported into RELION ( 48 ) and further auto-refined.
- Full pipeline: quantification [ImageJ] -> structure determination [PHENIX, RELION] -> stage not stated [MotionCor2]

### Cryo-EM structure of human telomerase dimer reveals H/ACA RNP-mediated dimerization. (Science 2025)

- DOI: 10.1126/science.adr5817 | PMCID: PMC7618144 | PMID: 40638752
- Version used: **5.0**
- Evidence: Negative stain EM data processing Data processing was performed in RELION 5.0 ( 54 , 55 ).
- Full pipeline: alignment/mapping [minimap2] -> machine learning [Topaz] -> stage not stated [CTFFIND, ChimeraX, ImageJ, PHENIX v1.20, RELION v5.0, UCSF Chimera]

### TIGR-Tas: A family of modular RNA-guided DNA-targeting systems in prokaryotes and their viruses. (Science 2025)

- DOI: 10.1126/science.adv9789 | PMCID: PMC12045711 | PMID: 40014690
- Evidence: Cryo-EM data processing Movies were corrected for motion using the RELION implementation of MotionCor2, with 6x4 patches and dose-weighting.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, MAFFT, PyMOL] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [MAFFT, PHENIX] -> stage not stated [CTFFIND, ColabFold, Coot, HMMER, MotionCor2, RELION, Topaz]

### Structural mechanism of LINE-1 target-primed reverse transcription. (Science 2025)

- DOI: 10.1126/science.ads8412 | PMCID: PMC7617806 | PMID: 40048554
- Evidence: Cryo-EM data processing Processing strategy for the consensus reconstruction Data were processed using RELION-5.0 unless otherwise indicated ( fig.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, PHENIX v1.21.1, RELION] -> stage not stated [CTFFIND, ChimeraX, ImageJ, MotionCor2, PyMOL, Python, REFMAC, Topaz]

### Evolutionary adaptations of doublet microtubules in trypanosomatid parasites. (Science 2025)

- DOI: 10.1126/science.adr5507 | PMCID: PMC7617938 | PMID: 40080577
- Evidence: Cryo-EM image processing of the L . tarentolae DMT Image processing was performed in RELION-4 ( 45 ), unless otherwise stated.
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [napari] -> stage not stated [AlphaFold, CTFFIND v4.0, ChimeraX, HMMER, ImageJ, RELION]

### Molecular basis of FIGNL1 in dissociating RAD51 from DNA and chromatin. (Science 2025)

- DOI: 10.1126/science.adr7920 | PMCID: PMC7617353 | PMID: 39636933
- Evidence: The particles were processed in the same way as the Gautomatch/RELION method and plotted and analyzed using GraphPad Prism as previously described.
- Full pipeline: registration [CTFFIND] -> structure determination [AlphaFold, PHENIX] -> visualisation [Fiji, ImageJ, RELION] -> stage not stated [Coot, Topaz]

### Cryo-electron microscopy structure of the budding yeast telomerase holoenzyme. (Science 2026)

- DOI: 10.1126/science.adz5344 | PMCID: PMC7619062 | PMID: 41886584
- Version used: **5.0**
- Evidence: Data processing was done in RELION 5.0 ( 92 , 93 ).
- Full pipeline: quantification [ImageJ] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, CTFFIND v4.1, Python, RELION v5.0, Topaz]

### Termination of the integrated stress response. (Science 2026)

- DOI: 10.1126/science.adw5137 | PMCID: PMC7618491 | PMID: 41231936
- Version used: **5.0**
- Evidence: Cryo-EM image processing R15B 414-713 -eIF2-eIF2B complexes dataset Movies were imported into Relion 5.0 ( 41 ) and motion corrected with Relion’s implementation of MotionCor using 7x6 patches and dose-weighting.
- Full pipeline: registration [RELION v5.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, PyMOL]

### Structure and organization of AMPA receptor-TARP complexes in the mammalian cerebellum. (Science 2026)

- DOI: 10.1126/science.aeb3577 | PMCID: PMC7619101 | PMID: 41379938
- Version used: **5.0**
- Evidence: Cryo-EM data processing and model building For the GluA2 containing dataset, a total of 51,245 movies were imported into RELION 5.0 ( 78 ), and beam-induced motion was corrected using MotionCor2 ( 79 ).
- Full pipeline: alignment/mapping [MUSCLE] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [PyMOL v2.5] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

