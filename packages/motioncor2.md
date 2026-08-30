# MotionCor2

- **Category:** structbio
- **Papers in survey:** 290
- **Journals:** PNAS (169), Nature (88), Cell (25), Science (8)
- **Years:** 2021 (30), 2022 (76), 2023 (66), 2024 (54), 2025 (54), 2026 (10)
- **Versions named:** 1.4.0 (9), 1.1.0 (2), 1.5 (2), 1.6.4 (2), 1.3.0 (1), 1.2.3 (1), 2.1.1 (1), 1.4.7 (1), 1.4 (1), 1.2.4 (1)
- **Pipeline stages it appears in:** registration (95), alignment/mapping (73), normalisation (11), structure determination (7), dimensionality reduction/clustering (1)

## Papers

### De novo identification of mammalian ciliary motility proteins using cryo-EM. (Cell 2021)

- DOI: 10.1016/j.cell.2021.10.007 | PMCID: PMC8595878 | PMID: 34715025
- Evidence: A total of 33,755 movie stacks were motion corrected and electron-dose weighted using MotionCor2 ( Zheng et al., 2017 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [CCP4, ChimeraX, Coot v0.9, ImageJ v1.44d, RELION v3.1]

### Selective activation of PFKL suppresses the phagocytic oxidative burst. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.004 | PMCID: PMC8802628 | PMID: 34320407
- Evidence: Movie frames were aligned, dose-weighted and summed using MotionCor2 ( Zheng et al., 2017 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [RELION] -> stage not stated [PHENIX, R v3.5.0]

### Bacterial Vipp1 and PspA are members of the ancient ESCRT-III membrane-remodeling superfamily. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.041 | PMCID: PMC8281802 | PMID: 34166615
- Evidence: Cryo-EM image processing Individual movie frames were aligned with MotionCor2 ( Zheng et al., 2017 ) and the contrast transfer function estimated using CTFFIND4 ( Rohou and Grigorieff, 2015 ).
- Full pipeline: alignment/mapping [Clustal Omega, IQ-TREE, MotionCor2] -> stage not stated [GROMACS, HMMER, ImageJ, PHENIX, RELION v3.1, VMD]

### Coupling of N7-methyltransferase and 3'-5' exoribonuclease with SARS-CoV-2 polymerase reveals mechanisms for capping and proofreading. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.033 | PMCID: PMC8142856 | PMID: 34143953
- Evidence: ...GEX6p-nsp9-nsp10 This paper N/A pRSF-duet-nsp14 This paper N/A Software and algorithms SerialEM Mastronarde, 2005 https://bio3d.colorado.edu/SerialEM MotionCor2 Zheng et al., 2017 https://emcore.ucsf.edu/ucsf-software RELION 3.0 Scheres, 2012 https://www3.mrc-lmb.cam.ac.uk/relion/ cryoSPARC Punjani et al., 2017 https://cryosparc.com/ UCSF Chimera Pettersen et al., 2004 https://www.cgl.ucsf.edu/chi...
- Full pipeline: structure determination [Coot] -> stage not stated [MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Fab-dimerized glycan-reactive antibodies are a structural category of natural antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.042 | PMCID: PMC8135257 | PMID: 34019795
- Evidence: Individual frames were aligned and dose-weighted using MotionCor2 ( Zheng et al., 2017b ) implemented within the Appion pipeline ( Lander et al., 2009 ).
- Full pipeline: alignment/mapping [MotionCor2] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX, R, Seurat, UMAP] -> stage not stated [PyMOL, RELION, UCSF Chimera, ggplot2]

### Simultaneous binding of Guidance Cues NET1 and RGM blocks extracellular NEO1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.045 | PMCID: PMC8063088 | PMID: 33740419
- Evidence: Cryo-EM data processing and model refinement In total 1635 movies were collected and drift correction, beam-induced motion and dose-weighting were performed with MotionCor2 RELION 3.1 ( Zivanov et al., 2018 ) for 1635 movies.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [MotionCor2] -> stage not stated [CTFFIND v4.1, Clustal Omega, ImageJ, PHENIX, PyMOL, RELION v3.1, UCSF Chimera]

### Cryo-EM Structure of an Extended SARS-CoV-2 Replication and Transcription Complex Reveals an Intermediate State in Cap Synthesis. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.016 | PMCID: PMC7666536 | PMID: 33232691
- Evidence: ...N/A pET28a-nsp13 This paper N/A pET28a-nsp9 This paper N/A Software and Algorithms SerialEM ( Mastronarde, 2005 ) https://bio3d.colorado.edu/SerialEM MotionCor2 ( Zheng et al., 2017 ) https://emcore.ucsf.edu/ucsf-software RELION 3.0 ( Scheres, 2012 ) https://www3.mrc-lmb.cam.ac.uk/relion cryoSPARC ( Punjani et al., 2017 ) https://cryosparc.com/ UCSF Chimera ( Pettersen et al., 2004 ) https://www.c...
- Full pipeline: structure determination [Coot] -> stage not stated [ImageJ, MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Structural basis for the assembly of the type V CRISPR-associated transposon complex. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.009 | PMCID: PMC9798831 | PMID: 36435179
- Version used: **1.4.0**
- Evidence: ...ase-3.1/ SPHIRE version 1.3 Moriya et al., 2017 43 https://sphire.mpg.de/wiki/doku.php cryoSPARC 3.2.0 Punjani et al., 2017 44 https://cryosparc.com/ MotionCor2 1.4.0 Zheng et al., 2017 45 https://emcore.ucsf.edu/ucsf-software Gctf 1.06 Zhang, 2016 46 https://www2.mrc-lmb.cam.ac.uk/research/locally-developed-software/zhang-software/ crYOLO version 1.7.6 Wagner et al., 2019 47 https://cryolo.readth...
- Full pipeline: stage not stated [CTFFIND v1.06, ChimeraX v1.2, Coot, MotionCor2 v1.4.0, PHENIX v1.19.1, RELION v3.1.2, UCSF Chimera v1.14]

### A mechanism for SARS-CoV-2 RNA capping and its inhibition by nucleotide analog inhibitors. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.037 | PMCID: PMC9531661 | PMID: 36335936
- Evidence: ...aper N/A pET28a-nsp13 This paper N/A pET28a-nsp9 This paper N/A Software and algorithms SerialEM Mastronarde, 2005 http://bio3d.colorado.edu/SerialEM MotionCor2 ( Zheng et al., 2017 ) https://emcore.ucsf.edu/ucsf-motioncor2 RELION 3.0 Scheres, 2012 https://www2.mrc-lmb.cam.ac.uk/relion cryoSPARC Punjani et al., 2017 https://cryosparc.com/ UCSF Chimera Pettersen et al., 2004 https://www.cgl.ucsf.ed...
- Full pipeline: stage not stated [MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### BacPROTACs mediate targeted protein degradation in bacteria. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.009 | PMCID: PMC9240326 | PMID: 35662409
- Version used: **1.0.5**
- Evidence: ...22 ) N/A DSF data analysis ( Niesen et al., 2007 ) ftp://ftp.sgc.ox.ac.uk/pub/biophysics cryoSPARC v2 ( Punjani et al., 2017 ) https://cryosparc.com/ MotionCor2 1.0.5 ( Zheng et al., 2017 ) https://emcore.ucsf.edu/ucsf-software Gctf 1.06 ( Zhang, 2016 ) N/A crYOLO v1.3.5 ( Wagner et al., 2019 ) http://sphire.mpg.de RELION 3.0 ( Zivanov et al., 2018 ) N/A Coot ( Emsley et al., 2010 ) https://www2.m...
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX, Coot, MotionCor2 v1.0.5, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Protective prototype-Beta and Delta-Omicron chimeric RBD-dimer vaccines against SARS-CoV-2. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.029 | PMCID: PMC9042943 | PMID: 35568034
- Evidence: ... N/A pCAGGS_S309 heavy chain This paper N/A pCAGGS_CR3022 light chain This paper N/A pCAGGS_CR3022 heavy chain This paper N/A Software and algorithms MotionCor2 Zheng et al., 2017 https://emcore.ucsf.edu/ucsf-motioncor2 CTFFIND4.1 Rohou and Grigorieff, 2015 N/A RELION3.1 Zivanov et al., 2018 http://www2.mrc-lmb.cam.ac.uk/relion Chimera Pettersen et al., 2004 http://www.cgl.ucsf.edu/chimera CryoSPA...
- Full pipeline: structure determination [RELION] -> stage not stated [MotionCor2]

### Broad neutralization of SARS-CoV-2 variants by an inhalable bispecific single-domain antibody. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.009 | PMCID: PMC8907017 | PMID: 35344711
- Evidence: N/A MotionCor2 UCSF Software https://docs.google.com/forms/d/e/1FAIpQLSfAQm5MA81qTx90W9JL6ClzSrM77tytsvyyHh1ZZWrFByhmfQ/viewform PHENIX https://phenix-online.org/ N/A Living Image® Software PerkinElmer N/A ForteBio Data Analysis software Pall ForteBio LLC N/A Prism 8.0 GraphPad https://www.graphpad.com/scientific-software/prism/ PyMol PyMol N/A PDBePISA Europea Bioinformatics Institute https://www...
- Full pipeline: stage not stated [CTFFIND, ChimeraX, MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Structural and functional characterizations of infectivity and immune evasion of SARS-CoV-2 Omicron. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.019 | PMCID: PMC8786603 | PMID: 35120603
- Evidence: All the micrographs were processed with MotionCor2 in Relion3.0.
- Full pipeline: structure determination [Coot] -> stage not stated [CTFFIND, ChimeraX, MotionCor2, PHENIX, RELION v3.07, UCSF Chimera, igraph v1.2.5]

### Receptor binding and complex structures of human ACE2 to spike RBD from omicron and delta SARS-CoV-2. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.001 | PMCID: PMC8733278 | PMID: 35093192
- Evidence: Image processing The drift correction of all stacks was performed with MotionCor2 ( Zheng et al., 2017 ) to generate 2 × binned micrographs.
- Full pipeline: stage not stated [MotionCor2, PHENIX, PyMOL, RELION]

### De novo protein identification in mammalian sperm using in situ cryoelectron tomography and AlphaFold2 docking. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.017 | PMCID: PMC10842264 | PMID: 37865089
- Evidence: Movement between frames was corrected using MotionCor2 without dose weighting 60 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler v4.4.1] -> differential/statistical testing [Bioconductor] -> visualisation [IMOD] -> stage not stated [AlphaFold, ChimeraX, ColabFold, Coot v0.9.8.1, MotionCor2, R, RELION, UCSF Chimera]

### Structural basis for ion selectivity in potassium-selective channelrhodopsins. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.009 | PMCID: PMC7615185 | PMID: 37652010
- Evidence: ...is paper N/A pAAV- Hc KCR1 (H225F)-EYFP This paper N/A Software and algorithms Serial EM software Mastronarde 84 https://bio3d.colorado.edu/SerialEM/ MotionCor2 Zheng et al.
- Full pipeline: structure determination [AlphaFold, Coot, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Kilosort v2.5, MotionCor2, RELION v4.0, UCSF Chimera]

### Systemwide disassembly and assembly of SCF ubiquitin ligase complexes. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.035 | PMCID: PMC10156175 | PMID: 37028429
- Version used: **1.1**
- Evidence: 69 https://www3.mrc-lmb.cam.ac.uk/relion Gautomatch v0.56 Kai Zhang https://www2.mrc-lmb.cam.ac.uk/download/gautomatch-056/ CTFFIND v4.1 Rohou and Grigorieff 70 https://grigoriefflab.umassmed.edu/ctffind4 GCTF v1.06 Zhang 71 https://www2.mrc-lmb.cam.ac.uk/download/gctf/ MotionCor2 v1.1 Zheng et al.
- Full pipeline: structure determination [PHENIX] -> stage not stated [CTFFIND v4.1, ChimeraX v1.2, ImageJ, MotionCor2 v1.1, PyMOL v2.3.3, RELION v3.1, UCSF Chimera]

### A trailing ribosome speeds up RNA polymerase at the expense of transcript fidelity via force and allostery. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.008 | PMCID: PMC10135430 | PMID: 36931247
- Evidence: Movie frames were aligned using MotionCor2 172 within RELION and binned 2× (to 1.447 Å/pixel).
- Full pipeline: alignment/mapping [ChimeraX, MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, PyMOL v1.6, RELION v3.1]

### Discovery of natural-product-derived sequanamycins as potent oral anti-tuberculosis agents. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.043 | PMCID: PMC9994261 | PMID: 36827973
- Evidence: 42 http://www.phenix-online.org/ Relion Scheres 43 https://relion.readthedocs.io/en/release-3.1/ MotionCor2 Zheng et al.
- Full pipeline: stage not stated [CTFFIND, MotionCor2, PHENIX, PyMOL, RELION]

### Cryo-EM structure of the RADAR supramolecular anti-phage defense complex. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.012 | PMCID: PMC9994260 | PMID: 36764290
- Version used: **1.3.1**
- Evidence: Cryo-EM data processing Dose-fractionated images of E. coli RdrA were gain normalized and motion corrected with MotionCor2 (v1.3.1) 43 followed by CTF and defocus value determination in CTFFIND4.
- Full pipeline: quality control [RELION] -> normalisation [MotionCor2 v1.3.1] -> registration [MotionCor2 v1.3.1] -> stage not stated [ImageJ, PHENIX v1.13]

### Structural insights into the diversity and DNA cleavage mechanism of Fanzor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.050 | PMCID: PMC11423790 | PMID: 39208796
- Evidence: Image stacks were subjected to beam-induced motion correction using MotionCor2.0 34 .
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX v1.7, PHENIX v1.18] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, RELION v4.0, UCSF Chimera v1.16]

### Molecular mechanism of distinct chemokine engagement and functional divergence of the human Duffy antigen receptor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.005 | PMCID: PMC11349380 | PMID: 39089252
- Evidence: The small dataset movies were subjected to beam-induced motion correction using RELION's own implementation of the UCSF MotionCor2 within Relion 5.0-beta.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> registration [MotionCor2] -> visualisation [R v3.7] -> stage not stated [AlphaFold, ChimeraX, PHENIX, RELION v4.0, UCSF Chimera]

### Extensive structural rearrangement of intraflagellar transport trains underpins bidirectional cargo transport. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.041 | PMCID: PMC11349379 | PMID: 39067443
- Evidence: 58 https://github.com/wan-lab-vanderbilt/TOMOMAN MotionCor2 Zheng et al.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2, RELION]

### Molecular basis for shifted receptor recognition by an encephalitic arbovirus. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.029 | PMCID: PMC12406711 | PMID: 40187345
- Version used: **1.6.4**
- Evidence: Cryo-EM data processing Raw movie stacks were corrected for beam-induced motion using MotionCor2 (version 1.6.4).
- Full pipeline: structure determination [ChimeraX, Coot v0.9.8.91, PHENIX v1.21r, UCSF Chimera v1.6.1] -> stage not stated [AlphaFold, CTFFIND, MotionCor2 v1.6.4, PyMOL v3.0.2, RELION v3.1]

### Structural and functional analysis of the Nipah virus polymerase complex. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.021 | PMCID: PMC11813165 | PMID: 39837328
- Version used: **1.6.4**
- Evidence: 54 https://www.phenix-online.org , RRID: SCR_014224 SerialEM 4.1-beta Mastronarde 55 http://bio3d.colorado.edu/SerialEM/ , RRID: SCR_017293 MotionCor2 1.6.4 Zheng et al.
- Full pipeline: stage not stated [AlphaFold, ChimeraX v1.5, Clustal Omega, Coot v0.9, MotionCor2 v1.6.4, PHENIX v1.20.1, PyMOL v2.5.5, RELION v3.1.1, UCSF Chimera v1.15]

### The structure of neurofibromin isoform 2 reveals different functional states. (Nature 2021)

- DOI: 10.1038/s41586-021-04024-x | PMCID: PMC8580823 | PMID: 34707296
- Version used: **2.1.1**
- Evidence: Movie stacks were motion-corrected and dose-weighted using MotionCor2 v2.1.1 (ref.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX v1.19, UCSF Chimera v1.15] -> stage not stated [ChimeraX, MotionCor2 v2.1.1, RELION v3.1.1]

### Structure of Venezuelan equine encephalitis virus in complex with the LDLRAD3 receptor. (Nature 2021)

- DOI: 10.1038/s41586-021-03963-9 | PMCID: PMC8550936 | PMID: 34646020
- Evidence: Videos from all of the samples were corrected for beam-induced motion using MotionCor2 (ref.
- Full pipeline: differential/statistical testing [RELION] -> structure determination [PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, MotionCor2]

### The structural basis of odorant recognition in insect olfactory receptors. (Nature 2021)

- DOI: 10.1038/s41586-021-03794-8 | PMCID: PMC8410599 | PMID: 34349260
- Evidence: Movie frames were aligned and binned over 2 × 2 pixels using MotionCor2 40 implemented in Relion 3.0 41 , and the contrast transfer function parameters for each motion-corrected image were estimated using CTFFIND4 42 .
- Full pipeline: alignment/mapping [MAFFT, MotionCor2, RELION v3.0] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [scikit-learn] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, PyMOL]

### Structural basis of early translocation events on the ribosome. (Nature 2021)

- DOI: 10.1038/s41586-021-03713-x | PMCID: PMC8318882 | PMID: 34234344
- Evidence: Motion correction was performed on raw super-resolution movie stacks and binned twofold using MotionCor2 software 55 .
- Full pipeline: normalisation [UCSF Chimera] -> registration [MotionCor2] -> differential/statistical testing [UCSF Chimera] -> structure determination [Coot v0.9.4.1, PHENIX v1.19, RELION, UCSF Chimera] -> visualisation [ChimeraX]

### Structure and dynamics of a mycobacterial type VII secretion system. (Nature 2021)

- DOI: 10.1038/s41586-021-03517-z | PMCID: PMC8131196 | PMID: 33981042
- Evidence: For the initial Arctica dataset, movies were motion-corrected using MotionCor2 18 and dose-weighted, and the contrast-transfer function (CTF) was estimated using CTFFIND4 19 .
- Full pipeline: structure determination [ChimeraX v1.0, RELION] -> visualisation [PyMOL v2.40] -> stage not stated [MotionCor2, PHENIX]

### Structural basis of GABA<sub>B</sub> receptor-G<sub>i</sub> protein coupling. (Nature 2021)

- DOI: 10.1038/s41586-021-03507-1 | PMCID: PMC8222003 | PMID: 33911284
- Evidence: Cryo-EM data processing Image stacks for the GABA B –G i1 complex were subjected to beam-induced motion correction using MotionCor2 38 .
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, RELION v3.1]

### Structural and biochemical mechanisms of NLRP1 inhibition by DPP9. (Nature 2021)

- DOI: 10.1038/s41586-021-03320-w | PMCID: PMC8081665 | PMID: 33731929
- Evidence: Image processing and 3D reconstruction The stacks of rNLRP1–rDPP9 and rNLRP1 FIIND–CARD(S969A)–rDPP9 recorded in super-resolution mode were motion-corrected using MotionCor2 and binned twofold, resulting in a physical pixel size of 1.061 Å per pixel and 1.091 Å per pixel, respectively 32 .
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [MotionCor2, PHENIX] -> stage not stated [ImageJ, RELION v3.1]

### Structure and inhibition mechanism of the human citrate transporter NaCT. (Nature 2021)

- DOI: 10.1038/s41586-021-03230-x | PMCID: PMC7933130 | PMID: 33597751
- Evidence: On-the-fly data quality was measured by running MotionCor2 53 and CTFFIND4 54 under control of Appion 55 .
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [MotionCor2, Topaz]

### Functional refolding of the penetration protein on a non-enveloped virus. (Nature 2021)

- DOI: 10.1038/s41586-020-03124-4 | PMCID: PMC8297411 | PMID: 33442061
- Evidence: Movies were motion corrected with MotionCor2 (5×5 patch alignment) 28 .
- Full pipeline: alignment/mapping [IMOD, MAFFT, MotionCor2, Python] -> registration [MotionCor2] -> structure determination [EMAN2] -> stage not stated [CTFFIND, Matplotlib, PyMOL]

### Structure of the class D GPCR Ste2 dimer coupled to two G proteins. (Nature 2021)

- DOI: 10.1038/s41586-020-2994-1 | PMCID: PMC7116888 | PMID: 33268889
- Evidence: Micrographs were subjected to beam-induced motion correction using MotionCor2 42 by dividing each frame into 5 x 5 patches.
- Full pipeline: alignment/mapping [CCP4] -> registration [MotionCor2] -> simulation/modelling [GROMACS] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [RELION]

### Close relatives of MERS-CoV in bats use ACE2 as their functional receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-05513-3 | PMCID: PMC9734910 | PMID: 36477529
- Version used: **1.3.0**
- Evidence: Raw data were processed using MotionCor2 (v.1.3.0).
- Full pipeline: alignment/mapping [CTFFIND, Clustal Omega, MUSCLE] -> structure determination [Coot v0.9.4, PHENIX v1.19, RELION, UCSF Chimera v1.15] -> stage not stated [ChimeraX v1.1, MotionCor2 v1.3.0]

### Structural basis of tankyrase activation by polymerization. (Nature 2022)

- DOI: 10.1038/s41586-022-05449-8 | PMCID: PMC9712121 | PMID: 36418402
- Evidence: Images were motion-corrected and dose-weighted using MotionCor2 (ref.
- Full pipeline: alignment/mapping [Clustal Omega, EMAN2 v2.31] -> quantification [ImageJ] -> normalisation [ImageJ] -> structure determination [PHENIX v1.18.2] -> visualisation [ChimeraX v1.3] -> stage not stated [CellProfiler, Coot, MotionCor2, RELION v2.10, UCSF Chimera v1.14]

### Structural basis of actin filament assembly and aging. (Nature 2022)

- DOI: 10.1038/s41586-022-05241-8 | PMCID: PMC9646518 | PMID: 36289337
- Evidence: Cryo-EM image processing For each dataset, video preprocessing was performed on the fly in TranSPHIRE 52 , the super-resolution videos were binned twice (resulting pixel size of 0.695 Å), gain corrected and motion corrected using UCSF MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX] -> stage not stated [Coot, RELION]

### Bending forces and nucleotide state jointly regulate F-actin structure. (Nature 2022)

- DOI: 10.1038/s41586-022-05366-w | PMCID: PMC9646526 | PMID: 36289330
- Evidence: Micrograph pre-processing Movies were aligned with MotionCor2 using 5 × 5 patches 54 , and dose-weighting sums 55 were generated from twofold binned frames with Fourier cropping, resulting in a pixel size of 1.03 Å in the images.
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [Python] -> differential/statistical testing [Matplotlib] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX, RELION] -> machine learning [TensorFlow, cryoDRGN] -> stage not stated [Coot, EMAN2, UCSF Chimera, scikit-image]

### Structure of the OMEGA nickase IsrB in complex with ωRNA and target DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05324-6 | PMCID: PMC9581776 | PMID: 36224386
- Evidence: The video frames were aligned in 5 × 5 patches and dose weighted in MotionCor2 (ref.
- Full pipeline: alignment/mapping [MAFFT, MotionCor2] -> structure determination [ColabFold, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND, Python]

### Structure of the Ebola virus polymerase complex. (Nature 2022)

- DOI: 10.1038/s41586-022-05271-2 | PMCID: PMC9517992 | PMID: 36171293
- Evidence: Image processing The movie frames were aligned using MotionCor2 56 and the contrast transfer function (CTF) values of each micrograph were determined using CTFFind4 57 .
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [ImageJ] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold]

### A wheat resistosome defines common principles of immune receptor channels. (Nature 2022)

- DOI: 10.1038/s41586-022-05231-w | PMCID: PMC9581773 | PMID: 36163289
- Evidence: The MotionCor2 program was used to perform Motion correction 51 .
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX v1.15, PHENIX v1.18.2] -> visualisation [ChimeraX v1.15] -> stage not stated [AlphaFold, RELION v3.1]

### Structural basis for directional chitin biosynthesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05244-5 | PMCID: PMC9556331 | PMID: 36131020
- Evidence: Cryo-EM data processing For the Ps Chs1 apo structure, the output movie stacks were subjected to beam-induced motion correction and dose-weighting using MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2019.3] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, RELION v3.08]

### The mechanism of RNA capping by SARS-CoV-2. (Nature 2022)

- DOI: 10.1038/s41586-022-05185-z | PMCID: PMC9492545 | PMID: 35944563
- Evidence: Videos were aligned and summed using MotionCor2 48 , with a downsampled pixel size of 1.09 Å.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX, RELION] -> stage not stated [CTFFIND, ImageJ]

### Structural insights into auxin recognition and efflux by Arabidopsis PIN1. (Nature 2022)

- DOI: 10.1038/s41586-022-05143-9 | PMCID: PMC9477737 | PMID: 35917925
- Evidence: Motion correction and dose weighting were performed using the RELION 3.1 implementation of MotionCor2 43 , 44 .
- Full pipeline: registration [MotionCor2, RELION v3.1] -> structure determination [PHENIX]

### A DNA origami rotary ratchet motor. (Nature 2022)

- DOI: 10.1038/s41586-022-04910-y | PMCID: PMC9300469 | PMID: 35859200
- Evidence: The micrographs were motion corrected and contrast transfer function estimated using MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> stage not stated [RELION v3.0]

### Archaic chaperone-usher pili self-secrete into superelastic zigzag springs. (Nature 2022)

- DOI: 10.1038/s41586-022-05095-0 | PMCID: PMC9452303 | PMID: 35853476
- Version used: **1.2.3**
- Evidence: Cryo-EM image processing and reconstruction Dose-fractionated video frames were processed for beam-induced motion correction using MotionCor2 (v.1.2.3) 31 .
- Full pipeline: quantification [ImageJ v1.53k] -> registration [MotionCor2 v1.2.3] -> structure determination [MotionCor2 v1.2.3, PHENIX v1.8.2, RELION v3.0.8, UCSF Chimera] -> stage not stated [CTFFIND v4.1.13, Coot v0.9.4]

### Cryo-EM structure of an active bacterial TIR-STING filament complex. (Nature 2022)

- DOI: 10.1038/s41586-022-04999-1 | PMCID: PMC9402430 | PMID: 35859168
- Version used: **1.4.0**
- Evidence: Global and local (12 × 8 patches) motion correction was repeated in RELION using MotionCor2 v1.4.0 (ref.
- Full pipeline: registration [MotionCor2 v1.4.0] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, RELION]

### A peroxisomal ubiquitin ligase complex forms a retrotranslocation channel. (Nature 2022)

- DOI: 10.1038/s41586-022-04903-x | PMCID: PMC9279156 | PMID: 35768507
- Evidence: Data processing A total of 9,019 dose-fractionated super-resolution movies were subjected to motion correction using the program MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, REFMAC, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.1]

### Structural insights into the HBV receptor and bile acid transporter NTCP. (Nature 2022)

- DOI: 10.1038/s41586-022-04857-0 | PMCID: PMC9242859 | PMID: 35580630
- Evidence: Dose-fractionated image stacks were subjected to beam-induced motion correction using MotionCor2 29 and the contrast transfer function parameters were estimated using CTFFIND4 30 .
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.2.1, PyMOL v2.3, UCSF Chimera v1.15] -> stage not stated [RELION]

### USP14-regulated allostery of the human proteasome by time-resolved cryo-EM. (Nature 2022)

- DOI: 10.1038/s41586-022-04671-8 | PMCID: PMC9117149 | PMID: 35477760
- Evidence: Cryo-EM data processing Drift correction and dose weighting were performed using the MotionCor2 program 46 at a super-resolution pixel size of 0.685 Å.
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, Coot, EMAN2, MotionCor2, RELION]

### Opening of glutamate receptor channel to subconductance levels. (Nature 2022)

- DOI: 10.1038/s41586-022-04637-w | PMCID: PMC9068512 | PMID: 35444281
- Evidence: Frame alignment was done using MotionCor2 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot v0.9.2] -> stage not stated [CTFFIND v1.06, PHENIX v1.18, RELION v3.1, UCSF Chimera v1.14, VMD v1.9.3]

### Structural basis of tethered agonism of the adhesion GPCRs ADGRD1 and ADGRF1. (Nature 2022)

- DOI: 10.1038/s41586-022-04580-w | PMCID: PMC9046087 | PMID: 35418679
- Evidence: Cryo-EM data processing and map construction The image stacks of the ADGRD1– and ADGRF1–G protein complexes were subjected to beam-induced motion correction by MotionCor2 40 .
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, ChimeraX v1.1, Coot, PHENIX] -> visualisation [PyMOL v1.8, UCSF Chimera v1.15] -> stage not stated [CTFFIND v1.18, RELION v3.1]

### Activation mechanism of the class D fungal GPCR dimer Ste2. (Nature 2022)

- DOI: 10.1038/s41586-022-04498-3 | PMCID: PMC8942848 | PMID: 35296853
- Evidence: Cryo-EM data processing and 3D reconstruction Image stacks (15,751 antagonist-bound, 9,369 ligand-free and 6,944 agonist-bound Ste2 movies) were subjected to beam-induced motion correction using MotionCor2 44 by dividing each frame into 5 × 5 patches.
- Full pipeline: registration [MotionCor2] -> differential/statistical testing [RELION] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, MotionCor2, PHENIX, RELION] -> visualisation [PyMOL] -> stage not stated [CTFFIND, UCSF Chimera]

### Broadly neutralizing antibodies target a haemagglutinin anchor epitope. (Nature 2022)

- DOI: 10.1038/s41586-021-04356-8 | PMCID: PMC8828479 | PMID: 34942633
- Evidence: 2,243 micrographs were collected, aligned and CTF-corrected using Leginon, MotionCor2 in Appion, and Patch-CTF in CryoSPARC2, respectively 61 , 62 , 64 , 65 .
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION, UCSF Chimera] -> simulation/modelling [GROMACS, PLUMED] -> visualisation [RELION] -> stage not stated [Jupyter, PHENIX, R, Seurat]

### FOXP3 recognizes microsatellites and bridges DNA through multimerization. (Nature 2023)

- DOI: 10.1038/s41586-023-06793-z | PMCID: PMC10719092 | PMID: 38030726
- Evidence: The dose-fractionated videos were motion corrected using MotionCor2 45 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> registration [MotionCor2] -> differential/statistical testing [DESeq2] -> structure determination [RELION v4.0.1, UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [BEDTools, CTFFIND v4.1, HOMER, MACS2, PHENIX]

### Structures of a sperm-specific solute carrier gated by voltage and cAMP. (Nature 2023)

- DOI: 10.1038/s41586-023-06629-w | PMCID: PMC10620091 | PMID: 37880361
- Version used: **1.4.0**
- Evidence: The data were motion corrected using MotionCor2 1.4.0 (ref.
- Full pipeline: registration [MotionCor2 v1.4.0] -> structure determination [PHENIX v1.20.1] -> stage not stated [ChimeraX v1.6.1, PyMOL v2.5.5, RELION v3.1.0]

### Structures illustrate step-by-step mitochondrial transcription initiation. (Nature 2023)

- DOI: 10.1038/s41586-023-06643-y | PMCID: PMC10600007 | PMID: 37821701
- Evidence: Cryo-EM data processing For each dataset, individual video frames were motion-corrected and aligned using MotionCor2 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.19.2] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, RELION v3.1]

### Sialoglycan binding triggers spike opening in a human coronavirus. (Nature 2023)

- DOI: 10.1038/s41586-023-06599-z | PMCID: PMC10700143 | PMID: 37794193
- Evidence: For the W89A mutant HKU1 spike incubated with disialoside, patch motion correction was carried out in MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CCP4, RELION v3.1.1, VMD]

### Inactivation of the Kv2.1 channel through electromechanical coupling. (Nature 2023)

- DOI: 10.1038/s41586-023-06582-8 | PMCID: PMC10567553 | PMID: 37758949
- Evidence: The beam-induced image motion between frames of each dose-fractionated micrograph was corrected using MotionCor2 (ref.
- Full pipeline: structure determination [Coot v0.9.8.1, PHENIX v1.19.1, UCSF Chimera v1.15] -> visualisation [PyMOL v2.4.1] -> stage not stated [MDAnalysis, MotionCor2, RELION v3.0]

### Structural mobility tunes signalling of the GluA1 AMPA glutamate receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06528-0 | PMCID: PMC10533411 | PMID: 37704721
- Evidence: Cryo-EM data processing and model building Dose-fractionated image stacks were first motion-corrected using MotionCor2 (ref.
- Full pipeline: structure determination [Coot, PHENIX, Python, RELION] -> stage not stated [AlphaFold, ChimeraX, MotionCor2, PyMOL, UCSF Chimera]

### Tail engagement of arrestin at the glucagon receptor. (Nature 2023)

- DOI: 10.1038/s41586-023-06420-x | PMCID: PMC10447241 | PMID: 37558880
- Evidence: Cryo-EM data processing and model building A total of 5,583 movies were collected and subjected to beam-induced motion correction using MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [Coot v0.8.9]

### Diverse modes of H3K36me3-guided nucleosomal deacetylation by Rpd3S. (Nature 2023)

- DOI: 10.1038/s41586-023-06349-1 | PMCID: PMC10432269 | PMID: 37468628
- Evidence: Image processing Motion correction was performed using the MotionCor2 46 .
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, RELION, UCSF Chimera]

### Fanzor is a eukaryotic programmable RNA-guided endonuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06356-2 | PMCID: PMC10432273 | PMID: 37380027
- Evidence: Image stacks were subjected to beam-induced motion correction using MotionCor2.0 (ref.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> registration [MotionCor2] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.4, PHENIX v1.18] -> stage not stated [BLAST, CTFFIND v1.18, HMMER v3.3.2, PyMOL v1.2, RELION v4.0]

### Axonemal structures reveal mechanoregulatory and disease mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-06140-2 | PMCID: PMC10266980 | PMID: 37258679
- Evidence: The dose-fractionated image stacks were aligned and dose-weighted using MotionCor2 software 61 .
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> structure determination [Coot] -> stage not stated [AlphaFold, ChimeraX, PHENIX, R v4.0, RELION]

### A pan-influenza antibody inhibiting neuraminidase via receptor mimicry. (Nature 2023)

- DOI: 10.1038/s41586-023-06136-y | PMCID: PMC10266979 | PMID: 37258672
- Evidence: Dose-weighted movie frame alignment was done using a Relion implementation of MotionCor2 (ref.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT, MotionCor2] -> stage not stated [R, RELION, UCSF Chimera]

### mRNA decoding in human is kinetically and structurally distinct from bacteria. (Nature 2023)

- DOI: 10.1038/s41586-023-05908-w | PMCID: PMC10156603 | PMID: 37020024
- Evidence: Cryo-EM data classification (PLT, ANS, LTM and GTPγS) Motion correction was performed on raw super-resolution video stacks and binned twofold using MotionCor2 software 65 separately for two data collections.
- Full pipeline: registration [MotionCor2] -> structure determination [CCP4] -> machine learning [REFMAC] -> stage not stated [ChimeraX, Coot, RELION v3.1, UCSF Chimera]

### Structural basis for GSDMB pore formation and its targeting by IpaH7.8. (Nature 2023)

- DOI: 10.1038/s41586-023-05832-z | PMCID: PMC10115629 | PMID: 36991122
- Evidence: Cryo-EM image processing Raw movies were corrected by gain reference and for beam-induced motion and summed into motion-corrected images using MotionCor2 (ref.
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, Coot, MotionCor2, RELION, UCSF Chimera]

### CFTR function, pathology and pharmacology at single-molecule resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-05854-7 | PMCID: PMC10115640 | PMID: 36949202
- Evidence: Image stacks were gain-normalized, binned by 2, and corrected for beam-induced specimen motion with MotionCor2 (ref.
- Full pipeline: normalisation [MotionCor2] -> stage not stated [RELION]

### The structural basis for HIV-1 Vif antagonism of human APOBEC3G. (Nature 2023)

- DOI: 10.1038/s41586-023-05779-1 | PMCID: PMC10033410 | PMID: 36754086
- Evidence: Dose-fractionated image stacks were motion corrected, dose weighted and 2× binned to the physical pixel size of 0.835 Å by MotionCor2 in the package SCIPION 62 , 63 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> registration [MotionCor2] -> structure determination [AlphaFold, UCSF Chimera] -> stage not stated [ChimeraX, Coot, PHENIX, PyMOL, RELION]

### Structural basis for substrate selection by the SARS-CoV-2 replicase. (Nature 2023)

- DOI: 10.1038/s41586-022-05664-3 | PMCID: PMC9891196 | PMID: 36725929
- Evidence: Dose-fractionated videos were gain-normalized, drift-corrected, summed and dose-weighted using MotionCor2 (ref.
- Full pipeline: normalisation [MotionCor2] -> differential/statistical testing [RELION v3.1] -> structure determination [PHENIX] -> stage not stated [Coot v0.9.5]

### Structure of the lysosomal mTORC1-TFEB-Rag-Ragulator megacomplex. (Nature 2023)

- DOI: 10.1038/s41586-022-05652-7 | PMCID: PMC9931586 | PMID: 36697823
- Evidence: Cryo-EM data processing Super-resolution video stacks were motion-corrected and binned 2× by Fourier cropping using MotionCor2 (ref.
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [ImageJ v1.47, MotionCor2]

### Structural basis of broad-spectrum β-lactam resistance in Staphylococcus aureus. (Nature 2023)

- DOI: 10.1038/s41586-022-05583-3 | PMCID: PMC9834060 | PMID: 36599987
- Evidence: Motion correction was performed using MotionCor2 62 and the contrast transfer functions (CTFs) of the summed and dose-weighted micrographs were determined using CTFFIND4 63 .
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [RELION]

### Principles of mitoribosomal small subunit assembly in eukaryotes. (Nature 2023)

- DOI: 10.1038/s41586-022-05621-0 | PMCID: PMC9892005 | PMID: 36482135
- Evidence: For each dataset, images were gain corrected, dose weighted, aligned and binned to a pixel size of 1.08 Å using MotionCor2 implementation in RELION 55 , and micrograph defocus was estimated using GCTF1.18 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [ChimeraX, PyMOL] -> structure determination [ChimeraX, PHENIX, PyMOL] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, RELION v3.1.1]

### Structures of the holo CRISPR RNA-guided transposon integration complex. (Nature 2023)

- DOI: 10.1038/s41586-022-05573-5 | PMCID: PMC9876797 | PMID: 36442503
- Evidence: Frames were aligned using MotionCor2 33 through Appion v3.4 34 , which was then imported to cryoSPARC v3.3.1 35 for contrast transfer function (CTF) estimation and downstream image analysis.
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [AlphaFold, RELION, UCSF Chimera v1.14]

### Nucleosome flipping drives kinetic proofreading and processivity by SWR1. (Nature 2024)

- DOI: 10.1038/s41586-024-08152-y | PMCID: PMC11618073 | PMID: 39506114
- Evidence: Cryo-EM data processing Movie frames were aligned using MotionCor2 (ref.
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold, CTFFIND, Coot]

### Structural basis of mRNA decay by the human exosome-ribosome supercomplex. (Nature 2024)

- DOI: 10.1038/s41586-024-08015-6 | PMCID: PMC11540850 | PMID: 39385025
- Evidence: On-the-fly micrograph movie processing was assisted by Focus 41 , which ran MotionCor2 (ref.
- Full pipeline: quantification [ImageJ] -> structure determination [AlphaFold, Coot, PHENIX] -> visualisation [ImageJ] -> stage not stated [MotionCor2, RELION v3.1, UCSF Chimera]

### LYCHOS is a human hybrid of a plant-like PIN transporter and a GPCR. (Nature 2024)

- DOI: 10.1038/s41586-024-08012-9 | PMCID: PMC11525196 | PMID: 39358511
- Version used: **1.1.0**
- Evidence: Dose-fractionated movies were corrected for beam-induced motion and compensated for radiation damage within MotionCor2 (v.1.1.0) 32 .
- Full pipeline: dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX v1.20.1] -> visualisation [Matplotlib] -> stage not stated [AlphaFold, CTFFIND v4.1.8, ChimeraX, ImageJ v2.14.0, MotionCor2 v1.1.0]

### Visualizing chaperonin function in situ by cryo-electron tomography. (Nature 2024)

- DOI: 10.1038/s41586-024-07843-w | PMCID: PMC11390479 | PMID: 39169181
- Version used: **1.4.0**
- Evidence: Frames were aligned using MotionCor2 (v.1.4.0, https://emcore.ucsf.edu/ucsf-software ) 57 .
- Full pipeline: alignment/mapping [MotionCor2 v1.4.0] -> registration [RELION] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX]

### Structure of a fully assembled γδ T cell antigen receptor. (Nature 2024)

- DOI: 10.1038/s41586-024-07920-0 | PMCID: PMC11485255 | PMID: 39146975
- Evidence: Image processing and map generation Following data collection as bias-only, LZW-compressed TIFFs, dose-fractionated videos were aligned, corrected for beam-induced motion, dose weighted and averaged within MotionCor2 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [Coot v0.9.8.93] -> structure determination [Coot v0.9.8.93, PHENIX v1.21.1] -> visualisation [ChimeraX v1.8] -> stage not stated [CTFFIND v4.1.14, ImageJ v1.54, R v12.1, RELION v4.0]

### Structural basis for transthiolation intermediates in the ubiquitin pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07828-9 | PMCID: PMC11374688 | PMID: 39143218
- Evidence: Movie frames from each session were gain normalized, 2× Fourier cropped, aligned and summed with and without dose-weighting using MotionCor2 55 .
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> differential/statistical testing [Topaz] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [IMOD v4.11] -> stage not stated [CTFFIND, ChimeraX, RELION v3.1]

### Cryo-EM architecture of a near-native stretch-sensitive membrane microdomain. (Nature 2024)

- DOI: 10.1038/s41586-024-07720-6 | PMCID: PMC11324527 | PMID: 39048819
- Evidence: For native-source eisosomes, movies were aligned using MotionCor2 59 , and CTF correction was completed using Gctf v.1.06 60 .
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.8.9.2, PHENIX v1.20] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, Cellpose v2.0, RELION v2.1.0, VMD v1.9]

### Oligomerization-mediated autoinhibition and cofactor binding of a plant NLR. (Nature 2024)

- DOI: 10.1038/s41586-024-07668-7 | PMCID: PMC11338831 | PMID: 38866053
- Evidence: Cryo-EM data processing of Sl NRC2 filament The raw stacks of Sl NRC2 filament were motion-corrected by MotionCor2 and binned twofold 50 .
- Full pipeline: structure determination [AlphaFold, PHENIX, RELION v3.08] -> stage not stated [MotionCor2]

### Membraneless channels sieve cations in ammonia-oxidizing marine archaea. (Nature 2024)

- DOI: 10.1038/s41586-024-07462-5 | PMCID: PMC11153153 | PMID: 38811725
- Evidence: Imported videos were motion-corrected, dose-weighted and Fourier cropped (2×) with MotionCor2 52 implemented in RELION-3.1 53 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [NAMD v2.14, VMD v1.94] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold v2.2.0, MotionCor2]

### Structural basis for pegRNA-guided reverse transcription by a prime editor. (Nature 2024)

- DOI: 10.1038/s41586-024-07497-8 | PMCID: PMC11222144 | PMID: 38811740
- Evidence: The dose-fractionated movies of the pre-initiation and elongation (28-nt) complexes were subjected to beam-induced motion correction and dose weighting using MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> stage not stated [AlphaFold, ChimeraX, PHENIX, RELION v3.1.1, Topaz]

### High-resolution in situ structures of mammalian respiratory supercomplexes. (Nature 2024)

- DOI: 10.1038/s41586-024-07488-9 | PMCID: PMC11222160 | PMID: 38811722
- Evidence: Preprocessing For all datasets, motion correction was performed using MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX, IMOD] -> visualisation [ChimeraX, IMOD, PyMOL] -> stage not stated [CTFFIND, EMAN2, RELION]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Evidence: Cryo-EM image processing For each acquired dataset, the same cryo-EM image processing approach was applied: MotionCor2 was used to correct for beam-induced motion and to generate dose-weighted images 34 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### Physiological temperature drives TRPM4 ligand recognition and gating. (Nature 2024)

- DOI: 10.1038/s41586-024-07436-7 | PMCID: PMC11168932 | PMID: 38750366
- Version used: **1.1.0**
- Evidence: In general, the raw super-resolution .tif video files for each dataset were motion-corrected and 2× binned using MotionCor2 (v.1.1.0) 53 .
- Full pipeline: visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2 v1.1.0, RELION]

### Structures of human γδ T cell receptor-CD3 complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07439-4 | PMCID: PMC11153141 | PMID: 38657677
- Evidence: For the dataset of Vγ9Vδ2 TCR–CD3 complex, the video stacks were motion-corrected using MotionCor2 (ref.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [MotionCor2, RELION]

### Emergence of fractal geometries in the evolution of a metabolic enzyme. (Nature 2024)

- DOI: 10.1038/s41586-024-07287-2 | PMCID: PMC11041685 | PMID: 38600380
- Evidence: Micrograph frames were aligned using MotionCor2 (ref.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MotionCor2] -> normalisation [RELION v3.1] -> simulation/modelling [GROMACS v2022.2] -> structure determination [MUSCLE v3.8.31, PHENIX v1.19.2] -> stage not stated [PyMOL v2.5.2, Topaz, UCSF Chimera]

### Cryo-EM structures of RAD51 assembled on nucleosomes containing a DSB site. (Nature 2024)

- DOI: 10.1038/s41586-024-07196-4 | PMCID: PMC10990931 | PMID: 38509361
- Evidence: All frames in the movies of each dataset were aligned using MotionCor2 41 with dose weighting, and the contrast transfer function (CTF) estimation was then performed using CTFFIND4 42 on digital micrographs.
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [ChimeraX, RELION]

### Structural basis of ribosomal 30S subunit degradation by RNase R. (Nature 2024)

- DOI: 10.1038/s41586-024-07027-6 | PMCID: PMC10901742 | PMID: 38326618
- Evidence: Movie frames were aligned with MotionCor2 (ref.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, MotionCor2] -> visualisation [BEDTools, ImageJ] -> stage not stated [AlphaFold, ChimeraX, Coot, RELION v3.1.3]

### Structures of the promoter-bound respiratory syncytial virus polymerase. (Nature 2024)

- DOI: 10.1038/s41586-023-06867-y | PMCID: PMC10794133 | PMID: 38123676
- Evidence: Cryo-EM data processing Motion correction of the data for RSV polymerase in complex with Le10 was carried out with the program MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, PyMOL, RELION v3.1.3] -> stage not stated [ChimeraX, UCSF Chimera]

### Template and target-site recognition by human LINE-1 in retrotransposition. (Nature 2024)

- DOI: 10.1038/s41586-023-06933-5 | PMCID: PMC10830416 | PMID: 38096901
- Evidence: All video frames were motion-corrected using MotionCor2 55 , 56 in RELION v.3.1.1 and the corresponding super-resolution pixel size was binned 2× during this process.
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [CTFFIND v4.1, ImageJ, MotionCor2, RELION v3.1.1]

### Structural snapshots capture nucleotide release at the μ-opioid receptor. (Nature 2025)

- DOI: 10.1038/s41586-025-09677-6 | PMCID: PMC12711574 | PMID: 41193810
- Evidence: Single particle cryoEM image processing Motion correction of micrograph videos was carried out using MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2024.5, MDTraj] -> structure determination [UCSF Chimera v1.17.3] -> stage not stated [ChimeraX v1.9, PyMOL v3.1.6.1]

### Helicase-mediated mechanism of SSU processome maturation and disassembly. (Nature 2025)

- DOI: 10.1038/s41586-025-09688-3 | PMCID: PMC12711562 | PMID: 41162712
- Evidence: A total of 44,272 movies was gain corrected, dose weighted and aligned, with each dataset having different optic groups and binned to a pixel size of 1.08 Å using RELION’s implementation of a MotionCor2-like algorithm 33 .
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, ChimeraX, RELION]

### Structural basis for the dynamic regulation of mTORC1 by amino acids. (Nature 2025)

- DOI: 10.1038/s41586-025-09428-7 | PMCID: PMC12507694 | PMID: 40836086
- Evidence: Large movie datasets recorded with a Titan Krios microscopes (27,853 for apo, 34,122 for Sestrin2 and 23,777 for CASTOR1) were corrected for drift using MotionCor2 implementation in RELION (v5.0) 39 – 41 .
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [AlphaFold, ChimeraX v1.8, Coot v0.9.8] -> machine learning [Topaz] -> stage not stated [CTFFIND v4.1.14, MotionCor2, PHENIX v2.0, RELION v5.0]

### Molecular mechanism of ultrafast transport by plasma membrane Ca&lt;sup&gt;2+&lt;/sup&gt;-ATPases. (Nature 2025)

- DOI: 10.1038/s41586-025-09402-3 | PMCID: PMC12488499 | PMID: 40836084
- Evidence: Cryo-EM data processing Within TranSPHIRE, data preprocessing included drift and gain correction with MotionCor2 (ref.
- Full pipeline: structure determination [Coot, RELION v3.1, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1.10, ChimeraX, MotionCor2, PHENIX]

### Structural basis of fast N-type inactivation in K&lt;sub&gt;v&lt;/sub&gt; channels. (Nature 2025)

- DOI: 10.1038/s41586-025-09339-7 | PMCID: PMC12460158 | PMID: 40770100
- Evidence: In general, the beam-induced sample motion between frames of each dose-fractionated micrograph was corrected and binned by 2 using MotionCor2 (ref.
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2, RELION, Topaz]

### Electron flow in hydrogenotrophic methanogens under nickel limitation. (Nature 2025)

- DOI: 10.1038/s41586-025-09229-y | PMCID: PMC12350162 | PMID: 40604290
- Evidence: Before particle extraction, the raw videos were motion-corrected and dose-weighted with RELION’s MotionCor2 implementation 47 using 5 × 5 patches, and CTF resolution was estimated using CTFFind4.1 (ref.
- Full pipeline: alignment/mapping [ChimeraX, IQ-TREE, MUSCLE] -> structure determination [PHENIX] -> stage not stated [AlphaFold v3.0, MotionCor2, RELION]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Version used: **1.4.0**
- Evidence: The movie frames were aligned using MotionCor2 (v.1.4.0) 78 , resulting in a total of 18,039 micrographs.
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### Swinging lever mechanism of myosin directly shown by time-resolved cryo-EM. (Nature 2025)

- DOI: 10.1038/s41586-025-08876-5 | PMCID: PMC12158783 | PMID: 40205053
- Evidence: Micrographs were corrected for beam-induced motion using MotionCor2, and CTF estimation was carried out using GCTF 43 , 44 .
- Full pipeline: structure determination [PHENIX] -> stage not stated [MotionCor2, RELION]

### Structural dynamics of DNA unwinding by a replicative helicase. (Nature 2025)

- DOI: 10.1038/s41586-025-08766-w | PMCID: PMC12043514 | PMID: 40108462
- Evidence: Cryo-EM data processing Movie stacks were corrected for beam-induced motion using RELION’s implementation 54 of MotionCor2 (ref.
- Full pipeline: structure determination [ChimeraX] -> visualisation [PHENIX, PyMOL v2.6.0, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1, MotionCor2, RELION, Topaz v0.3.0]

### Complex water networks visualized by cryogenic electron microscopy of RNA. (Nature 2025)

- DOI: 10.1038/s41586-025-08855-w | PMCID: PMC12137144 | PMID: 40068818
- Evidence: Image processing All micrographs were motion-corrected using MotionCor2 (ref.
- Full pipeline: simulation/modelling [MDAnalysis] -> structure determination [ChimeraX v1.6.1] -> stage not stated [EMAN2, MotionCor2, RELION]

### Structural dynamics of human fatty acid synthase in the condensing cycle. (Nature 2025)

- DOI: 10.1038/s41586-025-08782-w | PMCID: PMC12058526 | PMID: 39978408
- Evidence: Cryo-EM data processing Raw video stacks were subjected to motion correction, dose weighting and Fourier cropping to 0.835 Å per pixel using MotionCor2 implemented in Relion 58 , 59 .
- Full pipeline: registration [MotionCor2, RELION] -> structure determination [ChimeraX, PHENIX] -> machine learning [cryoDRGN] -> visualisation [UCSF Chimera] -> stage not stated [CTFFIND, Coot]

### Snapshots of acyl carrier protein shuttling in human fatty acid synthase. (Nature 2025)

- DOI: 10.1038/s41586-025-08587-x | PMCID: PMC12058525 | PMID: 39979457
- Evidence: 41 ) at a calibrated pixel size of 1.069 Å and motion corrected using MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Coot, RELION v3.1]

### Myosin forces remodel F-actin for mechanosensitive protein recognition. (Nature 2026)

- DOI: 10.1038/s41586-026-10398-7 | PMCID: PMC13233326 | PMID: 42020745
- Evidence: Cellular cryo-ET data processing Individual tilts were motion-corrected and binned 2× (to a pixel size of 5.05 Å) using MotionCor2 (ref.
- Full pipeline: simulation/modelling [Python] -> structure determination [IMOD] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [EMAN2, MotionCor2, PHENIX, RELION, SciPy]

### Structures of Marburgvirus glycoprotein and its complex with NPC1 receptor. (Nature 2026)

- DOI: 10.1038/s41586-026-10240-0 | PMCID: PMC13171430 | PMID: 41813895
- Evidence: All movies were motion corrected using MotionCor2 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX v1.16] -> visualisation [ChimeraX v0.93, PyMOL] -> stage not stated [CTFFIND v4.1.13, Coot v0.8.9]

### CLCC1 governs ER bilayer equilibration to maintain lipid homeostasis. (Nature 2026)

- DOI: 10.1038/s41586-026-10161-y | PMCID: PMC13061606 | PMID: 41741642
- Evidence: Initially, for TIFF format files, all frames of each tilt were motion corrected using MotionCor2 software 59 .
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2] -> dimensionality reduction/clustering [R] -> structure determination [IMOD] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX v1.7.1, Fiji, ImageJ]

### Integrase anchors viral RNA to the HIV-1 capsid interior. (Nature 2026)

- DOI: 10.1038/s41586-026-10154-x | PMCID: PMC13102720 | PMID: 41708858
- Version used: **1.4.0**
- Evidence: Micrograph movie frames were aligned and combined using MotionCor2 (v.1.4.0) 63 with dose weighting, and CTF parameters were estimated from frame sums using Gctf (v.1.18) 53 .
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0, RELION] -> normalisation [ImageJ, NAMD v3.0.1] -> simulation/modelling [VMD] -> structure determination [ChimeraX, Coot, IMOD] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PyMOL, Topaz, UCSF Chimera]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Evidence: Particle picking was performed in RELION on the motion-corrected micrographs generated by the New York Structural Biology Center using MotionCor2 (ref.
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### Structural basis of regulated N-glycosylation at the secretory translocon. (Nature 2026)

- DOI: 10.1038/s41586-025-09756-8 | PMCID: PMC12804085 | PMID: 41261126
- Evidence: Videos were motion-corrected using MotionCor2 (ref.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [TopHat v2.1.0] -> quantification [HTSeq v2.0.3] -> structure determination [Coot, PHENIX] -> machine learning [Coot] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

### ZAK activation at the collided ribosome. (Nature 2026)

- DOI: 10.1038/s41586-025-09772-8 | PMCID: PMC12823453 | PMID: 41261136
- Version used: **1.4.0**
- Evidence: Gain correction, movie alignment and summation of movie frames were performed using MotionCor2 (v1.4.0) 58 .
- Full pipeline: read trimming [SAMtools, Trim Galore] -> alignment/mapping [MotionCor2 v1.4.0, SAMtools, STAR] -> structure determination [AlphaFold, ChimeraX v1.9, PHENIX v1.20.1, UCSF Chimera] -> stage not stated [Coot, RELION v5.0]

### Cryo-EM structures of PI3Kα reveal conformational changes during inhibition and activation. (PNAS 2021)

- DOI: 10.1073/pnas.2109327118 | PMCID: PMC8609346 | PMID: 34725156
- Evidence: Dose-fractionated image stacks were subjected to beam-induced motion correction and dose weighting using MotionCor2.1 ( 55 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX v1.2] -> stage not stated [CTFFIND v1.06, RELION]

### Cryo-EM structure determination of small proteins by nanobody-binding scaffolds (Legobodies). (PNAS 2021)

- DOI: 10.1073/pnas.2115001118 | PMCID: PMC8521671 | PMID: 34620716
- Evidence: For the KDELR/Legobody complex, dose-fractionated movies were subjected to motion correction using the program MotionCor2 ( 37 ) with dose weighting.
- Full pipeline: registration [MotionCor2] -> stage not stated [Coot, PHENIX, RELION v3.1]

### Constitutive signal bias mediated by the human GHRHR splice variant 1. (PNAS 2021)

- DOI: 10.1073/pnas.2106606118 | PMCID: PMC8501799 | PMID: 34599099
- Evidence: Dose-fractionated image stacks were subjected to beam-induced motion correction using MotionCor2.1 ( 67 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v1.18, RELION]

### Structural basis for isoform-specific inhibition of human CTPS1. (PNAS 2021)

- DOI: 10.1073/pnas.2107968118 | PMCID: PMC8501788 | PMID: 34583994
- Evidence: Movies were aligned, dose-weighted, and summed using the Relion ( 62 ) implementation of MotionCor2 ( 63 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> stage not stated [PHENIX]

### Native structure of the RhopH complex, a key determinant of malaria parasite nutrient acquisition. (PNAS 2021)

- DOI: 10.1073/pnas.2100514118 | PMCID: PMC8536402 | PMID: 34446549
- Evidence: Frames in each movie were aligned, gain reference corrected, and dose weighted to generate a micrograph using MotionCor2 ( 45 ) ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> stage not stated [RELION, UCSF Chimera]

### Nanobody cocktails potently neutralize SARS-CoV-2 D614G N501Y variant and protect mice. (PNAS 2021)

- DOI: 10.1073/pnas.2101918118 | PMCID: PMC8126837 | PMID: 33893175
- Evidence: Movies from each of the imaging sessions were subjected to the correction of beam-induced motion using MotionCor2 ( 66 ), followed by contrast transfer function (CTF) estimation using Gctf ( 67 ).
- Full pipeline: dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, MotionCor2]

### Cryo-EM structure of <i>Mycobacterium smegmatis</i> DyP-loaded encapsulin. (PNAS 2021)

- DOI: 10.1073/pnas.2025658118 | PMCID: PMC8072242 | PMID: 33853951
- Evidence: The dose-fractionated movies were aligned, summed, dose weighted, distortion corrected, and binned by twofold in Fourier space (giving a pixel size of 1.04 Å) using MotionCor2 ( 51 ) to generate unweighted and weighted micrographs for each movie.
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> dimensionality reduction/clustering [RELION] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [UCSF Chimera]

### Architecture of the mycobacterial succinate dehydrogenase with a membrane-embedded Rieske FeS cluster. (PNAS 2021)

- DOI: 10.1073/pnas.2022308118 | PMCID: PMC8054011 | PMID: 33876763
- Evidence: A total of 5,508 dose-fractionated image stacks were subjected to beam-induced motion correction using MotionCor2 ( 38 ) and the contrast transfer functions were estimated by Gctf ( 39 ).
- Full pipeline: registration [CTFFIND, MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL]

### The effect of the D614G substitution on the structure of the spike glycoprotein of SARS-CoV-2. (PNAS 2021)

- DOI: 10.1073/pnas.2022586118 | PMCID: PMC7936381 | PMID: 33579792
- Evidence: The frames of the collected movies were aligned using MotionCor2 ( 17 ) implemented in RELION ( 18 ), and the Contrast Transfer Function (CTF) was fitted using CTFfind4 ( 19 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [Coot, PHENIX] -> stage not stated [UCSF Chimera]

### Molecular mechanisms of assembly and TRIP13-mediated remodeling of the human Shieldin complex. (PNAS 2021)

- DOI: 10.1073/pnas.2024512118 | PMCID: PMC7923543 | PMID: 33597306
- Evidence: Drift correction of the movie frames was performed with MotionCor2 ( 52 ).
- Full pipeline: structure determination [RELION] -> visualisation [PyMOL] -> stage not stated [MotionCor2, PHENIX, UCSF Chimera]

### Supramolecular assembly of the <i>Escherichia coli</i> LdcI upon acid stress. (PNAS 2021)

- DOI: 10.1073/pnas.2014383118 | PMCID: PMC7812809 | PMID: 33372137
- Evidence: Motion correction and dose weighting of the recorded movies were performed using MotionCor2 ( 61 ).
- Full pipeline: registration [MotionCor2] -> dimensionality reduction/clustering [RELION v1.4] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, ImageJ]

### Cross-species recognition of SARS-CoV-2 to bat ACE2. (PNAS 2021)

- DOI: 10.1073/pnas.2020216118 | PMCID: PMC7817217 | PMID: 33335073
- Evidence: The raw dose-fractionated image stacks were 3× Fourier binned, aligned, dose-weighted, and summed using MotionCor2 ( 43 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX, RELION v3.1]

### Human species D adenovirus hexon capsid protein mediates cell entry through a direct interaction with CD46. (PNAS 2021)

- DOI: 10.1073/pnas.2020732118 | PMCID: PMC7826407 | PMID: 33384338
- Evidence: Beam-induced motion was corrected using Relion’s MotionCor2 ( 66 ) implementation and the per-micrograph contrast transfer function (CTF) was estimated using Gctf ( 67 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [CCP4, CTFFIND, ChimeraX, EMAN2, MotionCor2, RELION v3.1]

### Biophysical characterization of calcium-binding and modulatory-domain dynamics in a pentameric ligand-gated ion channel. (PNAS 2022)

- DOI: 10.1073/pnas.2210669119 | PMCID: PMC9897478 | PMID: 36480474
- Evidence: Motion correction was carried out with MotionCor2 ( 43 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS, VMD] -> stage not stated [PHENIX, RELION v3.1, UCSF Chimera]

### Cryo-EM structures of cancer-specific helical and kinase domain mutations of PI3Kα. (PNAS 2022)

- DOI: 10.1073/pnas.2215621119 | PMCID: PMC9674216 | PMID: 36343266
- Evidence: Dose-fractionated image stacks were subjected to beam-induced motion correction and dose weighting using MotionCor2.1.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX v1.18.2] -> visualisation [ChimeraX v1.0, PyMOL v2.1, UCSF Chimera v1.13.1] -> stage not stated [CTFFIND v1.06, RELION]

### Cryo-electron microscopy structure of the H3-H4 octasome: A nucleosome-like particle without histones H2A and H2B. (PNAS 2022)

- DOI: 10.1073/pnas.2206542119 | PMCID: PMC9659345 | PMID: 36322721
- Evidence: In total, 5,517 movies of the H3-H4 octasome were aligned by MotionCor2 software ( 48 ) with dose weighting.
- Full pipeline: alignment/mapping [MotionCor2] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [RELION v3.0]

### The structured organization of &lt;i&gt;Deinococcus radiodurans&lt;/i&gt;' cell envelope. (PNAS 2022)

- DOI: 10.1073/pnas.2209111119 | PMCID: PMC9659351 | PMID: 36322746
- Evidence: For cryo-EC, eight-frame movies were drift corrected using MotionCor2 ( 42 ) on the Focus package ( 43 ).
- Full pipeline: stage not stated [MotionCor2]

### Structural and functional investigation of ABC transporter STE6-2p from <i>Pichia pastoris</i> reveals unexpected interaction with sterol molecules. (PNAS 2022)

- DOI: 10.1073/pnas.2202822119 | PMCID: PMC9618074 | PMID: 36256814
- Evidence: The collected 8,218 images were corrected for electron beam–induced sample motion with MotionCor2 ( 55 ) in RELION 3.1 software ( 56 ) with dose weighting (1e − /Å 2 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [BLAST, CTFFIND, MotionCor2, RELION v3.1]

### SPACA9 is a lumenal protein of human ciliary singlet and doublet microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2207605119 | PMCID: PMC9564825 | PMID: 36191189
- Evidence: Each tilt image was generated by applying motion correction to 8 frames (0.2 electrons per square Angstrom each) with MotionCor2 ( 46 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX, Clustal Omega v1.2.2] -> stage not stated [AlphaFold, Coot v0.9.4.1, IMOD, PHENIX, PyMOL v2.3.4, RELION]

### Quantitative prediction and measurement of Piezo's membrane footprint. (PNAS 2022)

- DOI: 10.1073/pnas.2208027119 | PMCID: PMC9546538 | PMID: 36166475
- Evidence: Full-frame alignment was performed using MotionCor2 ( 27 ).
- Full pipeline: alignment/mapping [MotionCor2]

### Nanomolar inhibition of SARS-CoV-2 infection by an unmodified peptide targeting the prehairpin intermediate of the spike protein. (PNAS 2022)

- DOI: 10.1073/pnas.2210990119 | PMCID: PMC9546559 | PMID: 36122200
- Evidence: The data were processed using a combination of MotionCor2 ( 32 ), Gctf ( 33 ), EMAN2 ( 34 ), cryoSPARC ( 35 ), and RELION ( 36 ), as described previously ( 16 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, CellProfiler, EMAN2, MotionCor2, RELION, kallisto]

### Nanobodies and chemical cross-links advance the structural and functional analysis of PI3Kα. (PNAS 2022)

- DOI: 10.1073/pnas.2210769119 | PMCID: PMC9499577 | PMID: 36095215
- Evidence: Dose-fractionated image stacks were subjected to beam-induced motion correction and dose-weighting using MotionCor2.1 ( 54 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX v1.3] -> stage not stated [CTFFIND v1.06, RELION]

### Multistate structures of the MLL1-WRAD complex bound to H2B-ubiquitinated nucleosome. (PNAS 2022)

- DOI: 10.1073/pnas.2205691119 | PMCID: PMC9499523 | PMID: 36095189
- Evidence: Movie stacks were aligned and down-scaled to a pixel size of 1.058 Å/pix (bin 1) using MotionCor2 ( 69 ), and contrast transfer function (CTF) correction was performed using Ctffind4 ( 70 ).
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, RELION v3.0, VMD v1.9.3, cryoDRGN]

### Mechanism by which T7 bacteriophage protein Gp1.2 inhibits &lt;i&gt;Escherichia coli&lt;/i&gt; dGTPase. (PNAS 2022)

- DOI: 10.1073/pnas.2123092119 | PMCID: PMC9478638 | PMID: 36067314
- Evidence: Briefly, movie frames were aligned using MotionCor2 ( 40 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot] -> machine learning [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, RELION]

### Topological crossing in the misfolded <i>Tetrahymena</i> ribozyme resolved by cryo-EM. (PNAS 2022)

- DOI: 10.1073/pnas.2209146119 | PMCID: PMC9477386 | PMID: 36067294
- Evidence: All micrographs were motion-corrected in MotionCor2 ( 41 ), and the contrast transfer function (CTF) was determined in CTFFIND4 ( 42 ).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [Coot, EMAN2, MotionCor2, PHENIX, RELION, UCSF Chimera]

### Identification of mEAK-7 as a human V-ATPase regulator via cryo-EM data mining. (PNAS 2022)

- DOI: 10.1073/pnas.2203742119 | PMCID: PMC9436323 | PMID: 35994636
- Evidence: Movies were motion corrected using MotionCor2 ( 20 ), the output micrographs were imported into cryoSPARC ( 21 ), and CTFFIND4 was used to perform contrast transfer function estimation ( 22 ).
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold] -> stage not stated [Topaz]

### The neutralizing breadth of antibodies targeting diverse conserved epitopes between SARS-CoV and SARS-CoV-2. (PNAS 2022)

- DOI: 10.1073/pnas.2204256119 | PMCID: PMC9407403 | PMID: 35972965
- Evidence: Drift and beam-induced motion correction were performed with MotionCor2 ( 50 ) to produce a micrograph from each movie.
- Full pipeline: registration [MotionCor2] -> dimensionality reduction/clustering [R v3.6.3] -> structure determination [Coot] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PHENIX]

### Structure of a cholinergic cell membrane. (PNAS 2022)

- DOI: 10.1073/pnas.2207641119 | PMCID: PMC9407305 | PMID: 35969788
- Evidence: Micrograph frame stacks were drift corrected and dose weighted using MotionCor2 ( 36 ).
- Full pipeline: alignment/mapping [CTFFIND] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [MotionCor2, RELION]

### A multidomain connector links the outer membrane and cell wall in phylogenetically deep-branching bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2203156119 | PMCID: PMC9388160 | PMID: 35943982
- Evidence: The clustered movies were motion corrected, dose weighted, and Fourier cropped (2×) with MotionCor2 ( 70 ) implemented in RELION3.1 ( 71 ).
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2] -> dimensionality reduction/clustering [MotionCor2] -> structure determination [ChimeraX, Coot, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold]

### Reversible structural changes in the influenza hemagglutinin precursor at membrane fusion pH. (PNAS 2022)

- DOI: 10.1073/pnas.2208011119 | PMCID: PMC9388137 | PMID: 35939703
- Evidence: Whole-frame motion correction and dose weighting was done with MotionCor2 ( 62 ), and contrast transfer function (CTF) parameters were estimated using CTFFIND4 ( 63 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, RELION] -> visualisation [ChimeraX]

### Structural insight and characterization of human Twinkle helicase in mitochondrial disease. (PNAS 2022)

- DOI: 10.1073/pnas.2207459119 | PMCID: PMC9371709 | PMID: 35914129
- Evidence: Movies from all datasets were aligned using MotionCor2 ( 36 ) using 5 × 5 tiles and binned to a common pixel size of 1.058 Å/px.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, IMOD] -> stage not stated [PHENIX, PyMOL]

### Ciliogenesis requires sphingolipid-dependent membrane and axoneme interaction. (PNAS 2022)

- DOI: 10.1073/pnas.2201096119 | PMCID: PMC9351462 | PMID: 35895683
- Evidence: The MotionCor2 program was used to correct the beam-induced motion ( 49 ).
- Full pipeline: quality control [Bowtie2] -> alignment/mapping [Bowtie2, IMOD] -> dimensionality reduction/clustering [seaborn] -> differential/statistical testing [Bioconductor, Python, edgeR] -> visualisation [seaborn] -> stage not stated [ImageJ, MotionCor2]

### Structural insights into the human PA28-20S proteasome enabled by efficient tagging and purification of endogenous proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2207200119 | PMCID: PMC9388094 | PMID: 35858375
- Evidence: The images were corrected for specimen drift using MotionCor2 ( 36 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [MotionCor2]

### Structural basis for high-voltage activation and subtype-specific inhibition of human Na&lt;sub&gt;v&lt;/sub&gt;1.8. (PNAS 2022)

- DOI: 10.1073/pnas.2208211119 | PMCID: PMC9335304 | PMID: 35858452
- Evidence: The stacks were motion-corrected with MotionCor2 ( 49 ) and binned twofold, resulting in 1.08 Å per pixel.
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, Coot, MotionCor2]

### Structural basis of mammalian complex IV inhibition by steroids. (PNAS 2022)

- DOI: 10.1073/pnas.2205228119 | PMCID: PMC9335260 | PMID: 35858451
- Evidence: Movies were aligned with MotionCor2 ( 63 ) and contrast transfer function (CTF) parameters were estimated in patches with a 7 × 7 grid.
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [PHENIX]

### Cryo-EM structures of wild-type and E138K/M184I mutant HIV-1 RT/DNA complexed with inhibitors doravirine and rilpivirine. (PNAS 2022)

- DOI: 10.1073/pnas.2203660119 | PMCID: PMC9335299 | PMID: 35858448
- Evidence: Individual movie frames were motion-corrected and aligned using MotionCor2 ( 50 ) as implemented in the Relion 3.1 package ( 51 ) and the contrast transfer function (CTF) parameters were estimated by CTFFIND-4 ( 52 ).
- Full pipeline: alignment/mapping [CTFFIND, MotionCor2, RELION v3.1] -> structure determination [Coot, PHENIX v1.19] -> visualisation [PyMOL]

### Structural basis and molecular mechanism of biased GPBAR signaling in regulating NSCLC cell growth via YAP activity. (PNAS 2022)

- DOI: 10.1073/pnas.2117054119 | PMCID: PMC9303995 | PMID: 35858343
- Evidence: Image stacks were subjected to motion correction using MotionCor2.1.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ANTs, CTFFIND]

### In situ architecture of the lipid transport protein VPS13C at ER-lysosome membrane contacts. (PNAS 2022)

- DOI: 10.1073/pnas.2203769119 | PMCID: PMC9303930 | PMID: 35858323
- Version used: **1.4.0**
- Evidence: The frames of each tilt series micrograph were aligned in MotionCor2 (version 1.4.0, https://emcore.ucsf.edu/ucsf-software , RRID:SCR_016499) ( 46 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0] -> structure determination [AlphaFold, ChimeraX, IMOD] -> visualisation [RELION, UCSF Chimera v1.13, seaborn v0.11.2] -> stage not stated [CTFFIND v1.18, EMAN2 v2.91]

### Friction-driven membrane scission by the human ESCRT-III proteins CHMP1B and IST1. (PNAS 2022)

- DOI: 10.1073/pnas.2204536119 | PMCID: PMC9303997 | PMID: 35858336
- Evidence: Movie frames were motion corrected and dose weighted using MotionCor2 ( 72 ).
- Full pipeline: registration [MotionCor2]

### Allosteric role of a structural NADP&lt;sup&gt;+&lt;/sup&gt; molecule in glucose-6-phosphate dehydrogenase activity. (PNAS 2022)

- DOI: 10.1073/pnas.2119695119 | PMCID: PMC9303983 | PMID: 35858355
- Evidence: First, beam-induced motions were corrected using MotionCor2.
- Full pipeline: stage not stated [MotionCor2, PyMOL]

### Sequential rescue and repair of stalled and damaged ribosome by bacterial PrfH and RtcB. (PNAS 2022)

- DOI: 10.1073/pnas.2202464119 | PMCID: PMC9304027 | PMID: 35858322
- Evidence: The drifts of movie frames were corrected using MotionCor2 ( 52 ), and the contrast transfer functions were determined using CTFFIND4 ( 53 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [Cytoscape, MotionCor2]

### Structure of the human cation-chloride cotransport KCC1 in an outward-open state. (PNAS 2022)

- DOI: 10.1073/pnas.2109083119 | PMCID: PMC9271165 | PMID: 35759661
- Evidence: Movie frames were aligned, dose weighted, and then summed into a single micrograph using MotionCor2 ( 58 ).
- Full pipeline: alignment/mapping [MotionCor2] -> dimensionality reduction/clustering [RELION v3.0.7] -> structure determination [PHENIX v1.18] -> stage not stated [Coot v0.8.9.3]

### Structural basis of Tom20 and Tom22 cytosolic domains as the human TOM complex receptors. (PNAS 2022)

- DOI: 10.1073/pnas.2200158119 | PMCID: PMC9245660 | PMID: 35733257
- Evidence: Each micrograph was corrected for subregion motion correction and dose weighted using University of California San Francisco (UCSF) MotionCor2 ( 56 ).
- Full pipeline: registration [MotionCor2] -> structure determination [UCSF Chimera] -> stage not stated [PHENIX, RELION]

### In situ structure of intestinal apical surface reveals nanobristles on microvilli. (PNAS 2022)

- DOI: 10.1073/pnas.2122249119 | PMCID: PMC9214534 | PMID: 35666862
- Evidence: The MotionCor2 program was used to correct the beam-induced motion ( 36 ).
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [IMOD, STAR v2.6.0c] -> stage not stated [ImageJ, MotionCor2, UCSF Chimera]

### Cryo-EM structure of DNA-bound Smc5/6 reveals DNA clamping enabled by multi-subunit conformational changes. (PNAS 2022)

- DOI: 10.1073/pnas.2202799119 | PMCID: PMC9191643 | PMID: 35648833
- Evidence: Motion correction was performed with MotionCor2 ( 25 ), and contrast transfer function parameters were estimated by Ctffind4 ( 26 ).
- Full pipeline: registration [MotionCor2] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [RELION v3.0]

### Structural insights into galanin receptor signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2121465119 | PMCID: PMC9173784 | PMID: 35594396
- Evidence: All movie stacks were collected and processed with MotionCor2 for motion correction ( 67 ), with 2× binned to a pixel size of 1.087 Å.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, R v3.50]

### Structural basis of peptidomimetic agonism revealed by small- molecule GLP-1R agonists Boc5 and WB4-24. (PNAS 2022)

- DOI: 10.1073/pnas.2200155119 | PMCID: PMC9171782 | PMID: 35561211
- Evidence: Dose-fractionated image stacks were subjected to beam-induced motion correction using MotionCor2.1 ( 32 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v1.06]

### The cyclic octapeptide antibiotic argyrin B inhibits translation by trapping EF-G on the ribosome during translocation. (PNAS 2022)

- DOI: 10.1073/pnas.2114214119 | PMCID: PMC9171646 | PMID: 35500116
- Evidence: Particle images for the EF-G-ArgB-70S complex were aligned with MotionCor2 ( 55 ), picked using GAUTOMATCH ( https://www.mrc-lmb.cam.ac.uk/kzhang ) and processed (including final sharpening and automated b-factor application) using RELION 3.0 ( 56 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION v3.0] -> structure determination [PHENIX v1.14] -> stage not stated [ChimeraX, PyMOL, UCSF Chimera]

### Cryoelectron microscopy of Na<sup>+</sup>,K<sup>+</sup>-ATPase in the two E2P states with and without cardiotonic steroids. (PNAS 2022)

- DOI: 10.1073/pnas.2123226119 | PMCID: PMC9169807 | PMID: 35380894
- Evidence: All movies were aligned by MotionCor2 ( 29 ) with dose weighting.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [RELION v3.1]

### Structural conservation among variants of the SARS-CoV-2 spike postfusion bundle. (PNAS 2022)

- DOI: 10.1073/pnas.2119467119 | PMCID: PMC9169775 | PMID: 35363556
- Evidence: The raw movie stacks were aligned, dose-weighted, and summed using RELION’s implementation of the MotionCor2 program ( 58 ), with five patches in the X direction and three patches in the Y direction and a binning factor 2, yielding a pixel size of 0.653 Å.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [CTFFIND, ChimeraX, Coot, PyMOL, Python, RELION, UCSF Chimera]

### Structural insights into the activation of autoinhibited human lipid flippase ATP8B1 upon substrate binding. (PNAS 2022)

- DOI: 10.1073/pnas.2118656119 | PMCID: PMC9168909 | PMID: 35349344
- Evidence: All movie frames were corrected for gain reference and binned by a factor of 2 to yield a pixel size of 1.06 Å in RELION3.1 ( 43 ) through MotionCor2 ( 44 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [Coot, MotionCor2, RELION, UCSF Chimera]

### Structural determinants of dual incretin receptor agonism by tirzepatide. (PNAS 2022)

- DOI: 10.1073/pnas.2116506119 | PMCID: PMC9060465 | PMID: 35333651
- Evidence: Dose-fractionated image stacks were subjected to beam-induced motion correction using MotionCor2 ( 46 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND]

### Replication is the key barrier during the dual-host adaptation of mosquito-borne flaviviruses. (PNAS 2022)

- DOI: 10.1073/pnas.2110491119 | PMCID: PMC8944775 | PMID: 35294288
- Evidence: Micrographs were corrected for beam-induced drift using MotionCorr ( 54 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [MotionCor2]

### Structural basis for the oligomerization-mediated regulation of NLRP3 inflammasome activation. (PNAS 2022)

- DOI: 10.1073/pnas.2121353119 | PMCID: PMC8931350 | PMID: 35254907
- Evidence: Raw movie stacks were motion-corrected using the RELION version of MotionCor2 ( 53 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, MotionCor2, PyMOL, RELION v3.1]

### Molecular basis of multistep voltage activation in plant two-pore channel 1. (PNAS 2022)

- DOI: 10.1073/pnas.2110936119 | PMCID: PMC8892357 | PMID: 35210362
- Evidence: The movies were drift corrected and dose weighted using University of California, San Francisco (UCSF) MotionCor2 ( 43 ) and 2× Fourier binned to a pixel size of 0.835 Å ⋅ pix −1 .
- Full pipeline: structure determination [Coot, PHENIX, RELION] -> visualisation [UCSF Chimera] -> stage not stated [MotionCor2]

### Vimentin intermediate filaments and filamentous actin form unexpected interpenetrating networks that redefine the cell cortex. (PNAS 2022)

- DOI: 10.1073/pnas.2115217119 | PMCID: PMC8915831 | PMID: 35235449
- Evidence: The projection images are binned and subjected to motion correction using MotionCorr ( 48 ), resulting in a final pixel size of 3.4 Å.
- Full pipeline: registration [MotionCor2]

### Rearrangement of a unique Kv1.3 selectivity filter conformation upon binding of a drug. (PNAS 2022)

- DOI: 10.1073/pnas.2113536119 | PMCID: PMC8812516 | PMID: 35091471
- Evidence: Movie frames were aligned with motion correction and dose weighting using University of California San Francisco (UCSF) MotionCor2 ( 36 ).
- Full pipeline: alignment/mapping [MotionCor2] -> registration [MotionCor2] -> simulation/modelling [UCSF Chimera, VMD] -> structure determination [PHENIX] -> stage not stated [CTFFIND, NAMD, RELION]

### Annealing synchronizes the 70<i>S</i> ribosome into a minimum-energy conformation. (PNAS 2022)

- DOI: 10.1073/pnas.2111231119 | PMCID: PMC8872765 | PMID: 35177473
- Evidence: Specifically, raw movie stacks were aligned and summed in accordance with dose weighting with MotionCor2.1 ( 58 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.17.1, RELION v3.0.8] -> stage not stated [CTFFIND, Python, UCSF Chimera v1.16]

### High-resolution cryo-electron microscopy structure of photosystem II from the mesophilic cyanobacterium, <i>Synechocystis</i> sp. PCC 6803. (PNAS 2022)

- DOI: 10.1073/pnas.2116765118 | PMCID: PMC8740770 | PMID: 34937700
- Evidence: To construct the full-dose map, micrograph movies using all 28 frames were corrected, aligned, and dose weighted using MotionCor2 ( 77 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [RELION v3.1, UCSF Chimera]

### Molecular basis of differential receptor usage for naturally occurring CD55-binding and -nonbinding coxsackievirus B3 strains. (PNAS 2022)

- DOI: 10.1073/pnas.2118590119 | PMCID: PMC8794823 | PMID: 35046043
- Evidence: Image stacks were corrected for beam-induced motion using MotionCor2 ( 38 ).
- Full pipeline: dimensionality reduction/clustering [RELION] -> structure determination [PHENIX] -> stage not stated [Coot, MotionCor2, PyMOL]

### Structural transitions in the GTP cap visualized by cryo-electron microscopy of catalytically inactive microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2114994119 | PMCID: PMC8764682 | PMID: 34996871
- Version used: **2.1**
- Evidence: Briefly, MotionCorr 2.1 5 × 5 patch-based alignment was performed on each micrograph ( 39 ).
- Full pipeline: alignment/mapping [MotionCor2 v2.1] -> normalisation [PyMOL] -> structure determination [PHENIX] -> stage not stated [RELION]

### Structures of the &lt;i&gt;P. aeruginosa&lt;/i&gt; FleQ-FleN master regulators reveal large-scale conformational switching in motility and biofilm control. (PNAS 2023)

- DOI: 10.1073/pnas.2312276120 | PMCID: PMC10723142 | PMID: 38051770
- Evidence: The movies were motion- and CTF-corrected using MotionCor2 ( 38 ) and Gctf ( 39 ), respectively, after which all micrograph processing was continued in cryoSPARC v3 and v4 ( 40 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, MotionCor2]

### Vimentin regulates nuclear segmentation in neutrophils. (PNAS 2023)

- DOI: 10.1073/pnas.2307389120 | PMCID: PMC10691343 | PMID: 37983515
- Evidence: The super-resolution frames (10 frames per tilt) of each tilt were motion-corrected and 2× binned using MotionCor2 software ( 33 ) to obtain tilt series with a pixel size of 3.33 Å for neutrophil and 2.24 Å for HeLa cells.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [MotionCor2, RELION v2.1]

### Structure and function of the &lt;i&gt;S. pombe&lt;/i&gt; III-IV-cyt &lt;i&gt;c&lt;/i&gt; supercomplex. (PNAS 2023)

- DOI: 10.1073/pnas.2307697120 | PMCID: PMC10655221 | PMID: 37939086
- Evidence: Movies were aligned with MotionCor2 ( 85 ), and contrast transfer function (CTF) parameters were estimated in patches with a 7 × 7 grid.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold]

### Molecular basis for Nse5-6 mediated regulation of Smc5/6 functions. (PNAS 2023)

- DOI: 10.1073/pnas.2310924120 | PMCID: PMC10636319 | PMID: 37903273
- Evidence: Motion correction was performed with MotionCor2 ( 22 ), and contrast transfer function parameters were estimated by Ctffind4 ( 23 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [ColabFold, RELION v3.0]

### Synaptophysin chaperones the assembly of 12 SNAREpins under each ready-release vesicle. (PNAS 2023)

- DOI: 10.1073/pnas.2311484120 | PMCID: PMC10636311 | PMID: 37903271
- Evidence: All the 731 micrographs were motion-corrected and dose-weighted using MotionCor2 ( 72 ) with a binning factor of 2 and divided into 5 × 5 patches.
- Full pipeline: stage not stated [CTFFIND, ImageJ, MotionCor2, RELION v3.1]

### Membrane remodeling properties of the Parkinson's disease protein LRRK2. (PNAS 2023)

- DOI: 10.1073/pnas.2309698120 | PMCID: PMC10614619 | PMID: 37844218
- Evidence: The initial drift and beam-induced motions were corrected using MotionCor2 (RRID:SCR_016499) ( 47 ).
- Full pipeline: stage not stated [ImageJ, MotionCor2]

### Molecular basis of signal transduction mediated by the human GIPR splice variants. (PNAS 2023)

- DOI: 10.1073/pnas.2306145120 | PMCID: PMC10576055 | PMID: 37792509
- Evidence: Dose-fractionated image stacks were subjected to beam-induced motion correction using MotionCor2.1 ( 60 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2021.4] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX v1.2.4] -> stage not stated [CTFFIND v1.06, ImageJ, RELION]

### Structural insights into the interaction of three Y-shaped ligands with PI3Kα. (PNAS 2023)

- DOI: 10.1073/pnas.2304071120 | PMCID: PMC10450665 | PMID: 37585458
- Evidence: Dose-fractionated image stacks were subjected to beam-induced motion correction using MotionCor2.1 ( 42 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot v0.9.4.1] -> visualisation [ChimeraX v1.0, PyMOL v2.1, UCSF Chimera v1.13.1] -> stage not stated [CTFFIND v1.06, PHENIX v1.18.2, RELION]

### Two conformations of the Tom20 preprotein receptor in the TOM holo complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301447120 | PMCID: PMC10450662 | PMID: 37579144
- Evidence: Movies were motion-corrected using MotionCor2 ( 49 ), and CTF parameters were initially estimated using CTFFIND-4 ( 50 ), both as implemented in Relion.
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, ChimeraX, MotionCor2, RELION]

### Transition State of Arp2/3 Complex Activation by Actin-Bound Dimeric Nucleation-Promoting Factor. (PNAS 2023)

- DOI: 10.1073/pnas.2306165120 | PMCID: PMC10434305 | PMID: 37549294
- Evidence: Micrographs containing particles from cryoSPARC were motion corrected using MotionCor2 in Relion ( 51 ) and CTF corrected with CTFFIND4.1 ( 52 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [RELION v3.1]

### The structure of <i>Plasmodium falciparum</i> multidrug resistance protein 1 reveals an N-terminal regulatory domain. (PNAS 2023)

- DOI: 10.1073/pnas.2219905120 | PMCID: PMC10410737 | PMID: 37527341
- Evidence: Beam-induced motion correction and dose weighting were performed on the collected movie stacks using MotionCor2 ( 53 ) implemented in RELION 3.0 ( 54 ) with a binning factor of 2 (pixel size 1.10 Å).
- Full pipeline: registration [MotionCor2, RELION v3.0] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [UCSF Chimera]

### An expandable, modular de novo protein platform for precision redox engineering. (PNAS 2023)

- DOI: 10.1073/pnas.2306046120 | PMCID: PMC10400981 | PMID: 37487099
- Evidence: The dose-fractionated movies were gain normalized, aligned, and dose-weighted using MotionCor2 ( 71 ) and contrast transfer function (CTF) information determined and corrected using Gctf find4.1 ( 72 ).
- Full pipeline: alignment/mapping [CTFFIND, MotionCor2] -> normalisation [CTFFIND, MotionCor2] -> dimensionality reduction/clustering [RELION v3.1]

### Efficient tagging of endogenous proteins in human cell lines for structural studies by single-particle cryo-EM. (PNAS 2023)

- DOI: 10.1073/pnas.2302471120 | PMCID: PMC10401002 | PMID: 37487103
- Evidence: For the 200 kV datasets, all movies were motion-corrected on-the-fly by MotionCor2 ( 70 ) implemented in Scipion ( 71 ).
- Full pipeline: structure determination [PHENIX] -> machine learning [Cellpose] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [CTFFIND, Coot, ImageJ, MotionCor2, RELION, Topaz]

### Structures and membrane interactions of native serotonin transporter in complexes with psychostimulants. (PNAS 2023)

- DOI: 10.1073/pnas.2304602120 | PMCID: PMC10629533 | PMID: 37436958
- Evidence: The beam-induced motion was corrected by MotionCor2 ( 80 ).
- Full pipeline: alignment/mapping [RELION] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [CTFFIND, MotionCor2, VMD]

### Elucidating interprotein energy transfer dynamics within the antenna network from purple bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2220477120 | PMCID: PMC10334754 | PMID: 37399405
- Evidence: Alignment of frames was done using Relion implementation of MotionCorr.
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [ChimeraX, RELION v3.0]

### Structural insights into the assembly of the agrin/LRP4/MuSK signaling complex. (PNAS 2023)

- DOI: 10.1073/pnas.2300453120 | PMCID: PMC10266037 | PMID: 37252960
- Evidence: A total of 3,560 movie frames of agrin–LRP4–MuSK micrographs were motion-corrected and binned two-fold, resulting in a pixel size of 0.83 Å, and dose-weighted using MotionCor2 ( 27 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, RELION]

### Molecular mechanism of fatty acid activation of FFAR1. (PNAS 2023)

- DOI: 10.1073/pnas.2219569120 | PMCID: PMC10235965 | PMID: 37216523
- Evidence: Briefly, dose-fractioned images were gain normalized, binned two-fold to obtain a pixel size of 1.07 Å, motion corrected, and dose weighted using MotionCor2 ( 45 ).
- Full pipeline: normalisation [MotionCor2] -> registration [MotionCor2] -> simulation/modelling [NAMD v2.14] -> structure determination [Coot v0.9.4.1, PHENIX v1.19.2] -> stage not stated [R v3.50, RELION v3.1, UCSF Chimera v1.3]

### Structural insights into the transcription activation mechanism of the global regulator GlnR from actinobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2300282120 | PMCID: PMC10235972 | PMID: 37216560
- Evidence: Subframes of individual movies were aligned using MotionCor2 ( 58 ), and contrast transfer function for each summed image was estimated using CTFFIND4.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [PyMOL, RELION v3.1]

### Starvation sensing by mycobacterial RelA/SpoT homologue through constitutive surveillance of translation. (PNAS 2023)

- DOI: 10.1073/pnas.2302006120 | PMCID: PMC10235957 | PMID: 37216503
- Evidence: After motion correction of micrograph frames using MotionCor2 ( 58 ), images were processed using the pipeline of RELION ( 59 ).
- Full pipeline: registration [MotionCor2, RELION] -> stage not stated [PHENIX]

### Mechanistic insights into the regulation of cell wall hydrolysis by FtsEX and EnvC at the bacterial division site. (PNAS 2023)

- DOI: 10.1073/pnas.2301897120 | PMCID: PMC10214136 | PMID: 37186861
- Evidence: Dose-fractionated movies collected using K3 Summit direct electron detector were subjected to motion correction using the program MotionCor2 ( 53 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold]

### Membrane protein isolation and structure determination in cell-derived membrane vesicles. (PNAS 2023)

- DOI: 10.1073/pnas.2302325120 | PMCID: PMC10160969 | PMID: 37098056
- Evidence: The raw movies were motion-corrected by MotionCor2 ( 55 ) in Relion V3.1 ( 56 ).
- Full pipeline: dimensionality reduction/clustering [Topaz] -> machine learning [Topaz] -> stage not stated [MotionCor2, RELION]

### Mechanistic insights into DNA binding and cleavage by a compact type I-F CRISPR-Cas system in bacteriophage. (PNAS 2023)

- DOI: 10.1073/pnas.2215098120 | PMCID: PMC10161043 | PMID: 37094126
- Evidence: Motion correction and CTF-estimation for each micrograph were performed using MotionCor2 and CTFFIND4.1, respectively ( 46 , 47 ).
- Full pipeline: quantification [ImageJ] -> registration [MotionCor2] -> dimensionality reduction/clustering [RELION v3.0] -> structure determination [PHENIX, RELION v3.0] -> visualisation [PyMOL]

### In situ architecture and membrane fusion of SARS-CoV-2 Delta variant. (PNAS 2023)

- DOI: 10.1073/pnas.2213332120 | PMCID: PMC10160983 | PMID: 37094167
- Evidence: The electron beam–induced motion was corrected using MotionCor2 ( 38 ) by averaging eight frames for each tilt.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD, PHENIX] -> stage not stated [Coot, MotionCor2, RELION, ilastik]

### Two structural switches in HIV-1 capsid regulate capsid curvature and host factor binding. (PNAS 2023)

- DOI: 10.1073/pnas.2220557120 | PMCID: PMC10120081 | PMID: 37040417
- Evidence: Dose-fractionated movies were aligned, dose-weighted, and averaged with MotionCor2 ( 39 ) in RELION-4.0 ( 40 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [ChimeraX, PHENIX] -> stage not stated [UCSF Chimera]

### Interdigitated immunoglobulin arrays form the hyperstable surface layer of the extremophilic bacterium &lt;i&gt;Deinococcus radiodurans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2215808120 | PMCID: PMC10120038 | PMID: 37043530
- Evidence: Imported movies were motion-corrected, dose-weighted, and Fourier-cropped (2×) with MotionCor2 ( 51 ) implemented in RELION3.1 ( 52 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold v2.2.0, ChimeraX, MotionCor2, RELION]

### A general mechanism for transcription bubble nucleation in bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2220874120 | PMCID: PMC10083551 | PMID: 36972428
- Evidence: Dose-fractionated movies were gain normalized, drift corrected, summed, and dose weighted using MotionCor2 ( 33 ).
- Full pipeline: quantification [ImageJ] -> normalisation [MotionCor2] -> differential/statistical testing [RELION v3.1] -> structure determination [ChimeraX, Coot, RELION v3.1] -> stage not stated [HMMER, PHENIX]

### Structure of mycobacterial respiratory complex I. (PNAS 2023)

- DOI: 10.1073/pnas.2214949120 | PMCID: PMC10068793 | PMID: 36952383
- Evidence: Exposure fractions were aligned with MotionCor2 ( 99 ) using a 7×7 grid.
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [RELION] -> structure determination [PHENIX v1.19.2] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, Coot v0.9.6]

### Structure-based design of a SARS-CoV-2 Omicron-specific inhibitor. (PNAS 2023)

- DOI: 10.1073/pnas.2300360120 | PMCID: PMC10068829 | PMID: 36940324
- Evidence: The data were processed using a combination of MotionCor2 ( 24 ), Gctf ( 25 ), EMAN2 ( 26 ), cryoSPARC ( 27 ), and RELION ( 28 ), as described previously ( 14 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, MotionCor2, PyMOL, RELION, UCSF Chimera]

### In situ snapshots along a mammalian selective autophagy pathway. (PNAS 2023)

- DOI: 10.1073/pnas.2221712120 | PMCID: PMC10041112 | PMID: 36917659
- Evidence: Tilt series were preprocessed with TOMOMAN software ( https://github.com/williamnwan/TOMOMAN ), performing beam-induced motion correction with MotionCor2 ( 47 ), tilt-series sorting, and contrast transfer function estimation with CTFFIND ( 48 ).
- Full pipeline: alignment/mapping [IMOD v4.10.49] -> registration [CTFFIND, MotionCor2] -> structure determination [IMOD v4.10.49] -> machine learning [EMAN2] -> visualisation [ChimeraX]

### A macrocyclic peptide inhibitor traps MRP1 in a catalytically incompetent conformation. (PNAS 2023)

- DOI: 10.1073/pnas.2220012120 | PMCID: PMC10089224 | PMID: 36893260
- Evidence: Subframe image alignment was performed though MotionCor2.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX, REFMAC, UCSF Chimera] -> stage not stated [PyMOL, RELION]

### Design, synthesis, and characterization of protein origami based on self-assembly of a brick and staple artificial protein pair. (PNAS 2023)

- DOI: 10.1073/pnas.2218428120 | PMCID: PMC10089216 | PMID: 36893280
- Evidence: Frames were aligned using MotionCor2 to correct for beam-induced motion and reconstruction was performed in IMOD ( 59 , 60 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> structure determination [IMOD, MotionCor2] -> stage not stated [AlphaFold, RoseTTAFold]

### The SspB adaptor drives structural changes in the AAA+ ClpXP protease during ssrA-tagged substrate delivery. (PNAS 2023)

- DOI: 10.1073/pnas.2219044120 | PMCID: PMC9963277 | PMID: 36730206
- Evidence: Frames in each movie were binned (twofold), aligned, gain-corrected, and dose-weighted using MotionCor2 ( 32 ) to generate micrographs.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.14, RELION v3.1] -> stage not stated [ChimeraX]

### Structure and supramolecular organization of the canine distemper virus attachment glycoprotein. (PNAS 2023)

- DOI: 10.1073/pnas.2208866120 | PMCID: PMC9963377 | PMID: 36716368
- Version used: **1.4.0**
- Evidence: Dose weighting and motion correction of dose-fractionated and gain-corrected movies were performed using MotionCor2 (version 1.4.0) ( 63 ).
- Full pipeline: registration [MotionCor2 v1.4.0] -> simulation/modelling [VMD] -> structure determination [PHENIX v1.19] -> visualisation [VMD] -> stage not stated [ChimeraX v1.3, Coot, PyMOL v2.5.2, RELION v3.1.1, UCSF Chimera v1.12]

### Cryo-EM structure of the whole photosynthetic reaction center apparatus from the green sulfur bacterium <i>Chlorobaculum tepidum</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2216734120 | PMCID: PMC9945994 | PMID: 36693097
- Evidence: For data processing using Relion, all movies were subjected to beam-induced motion correction using MotionCor2 ( 52 ).
- Full pipeline: registration [MotionCor2] -> stage not stated [ChimeraX, PHENIX, RELION v3.0, UCSF Chimera]

### Destabilizing NF1 variants act in a dominant negative manner through neurofibromin dimerization. (PNAS 2023)

- DOI: 10.1073/pnas.2208960120 | PMCID: PMC9945959 | PMID: 36689660
- Evidence: Collected movie frames were motion-corrected and dose-weighed using MotionCorr ( 33 ) followed by contrast transfer function estimation using CTFFIND4 ( 34 ) Initial particles were picked using Laplacian-of-Guassian-based auto-picker.
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, Coot, MotionCor2, RELION]

### prM-reactive antibodies reveal a role for partially mature virions in dengue virus pathogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2218899120 | PMCID: PMC9933121 | PMID: 36638211
- Evidence: Each micrograph was corrected for beam-induced sample motion using MotionCor2 ( 62 ), and CTF parameters for each were estimated using CTFFIND4 ( 63 ).
- Full pipeline: visualisation [ChimeraX] -> stage not stated [MotionCor2, RELION, UCSF Chimera]

### Structural basis for regulation of SOS response in bacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2217493120 | PMCID: PMC9926225 | PMID: 36598938
- Evidence: Subframes were aligned and summed using RELION’s own implementation of the UCSF MotionCor2 ( 40 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [Coot, PHENIX] -> stage not stated [ImageJ]

### Differential dynamics and direct interaction of bound ligands with lipids in multidrug transporter ABCG2. (PNAS 2023)

- DOI: 10.1073/pnas.2213437120 | PMCID: PMC9910490 | PMID: 36580587
- Evidence: Superresolution movies were down-sampled twice and motion-corrected by Fourier cropping, drift-correction, and dose-weighting with MotionCor2 ( 44 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [CTFFIND, Coot v0.9, MotionCor2, PHENIX, VMD]

### SUMO enhances unfolding of SUMO-polyubiquitin-modified substrates by the Ufd1/Npl4/Cdc48 complex. (PNAS 2023)

- DOI: 10.1073/pnas.2213703120 | PMCID: PMC9910466 | PMID: 36574706
- Evidence: Movies from each dataset were corrected for drift and dose-weighted with MotionCor2 in RELION 3.0 ( 58 ).
- Full pipeline: structure determination [PHENIX, Python] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, Coot, MotionCor2, RELION v3.0]

### Molecular basis of lipid and ligand regulation of prostaglandin receptor DP2. (PNAS 2024)

- DOI: 10.1073/pnas.2403304121 | PMCID: PMC11665870 | PMID: 39665758
- Evidence: MotionCor2 was utilized to correct for frame-based motion, producing drift-corrected micrographs suitable for further analysis.
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2]

### Architecture of the Sap S-layer of &lt;i&gt;Bacillus anthracis&lt;/i&gt; revealed by integrative structural biology. (PNAS 2024)

- DOI: 10.1073/pnas.2415351121 | PMCID: PMC11665858 | PMID: 39652757
- Evidence: Motion correction of the acquired movies was performed using MotionCor2 ( 40 ) and the resulting micrographs were assembled into a raw tilt series stack.
- Full pipeline: alignment/mapping [VMD] -> registration [MotionCor2] -> simulation/modelling [VMD] -> structure determination [RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, GROMACS, IMOD]

### Molecular architecture of synaptic vesicles. (PNAS 2024)

- DOI: 10.1073/pnas.2407375121 | PMCID: PMC11626200 | PMID: 39602275
- Evidence: The aligned frames were motion-corrected using MotionCor2 ( 78 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> structure determination [IMOD] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, RELION]

### Calcineurin-fusion facilitates cryo-EM structure determination of a Family A GPCR. (PNAS 2024)

- DOI: 10.1073/pnas.2414544121 | PMCID: PMC11621825 | PMID: 39565314
- Evidence: The image stacks of the β 2 AR-CN fusion protein were collected and subjected for motion correction using MotionCor2 ( 27 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, UCSF Chimera] -> stage not stated [RELION]

### The structures of protein kinase A in complex with CFTR: Mechanisms of phosphorylation and noncatalytic activation. (PNAS 2024)

- DOI: 10.1073/pnas.2409049121 | PMCID: PMC11573500 | PMID: 39495916
- Evidence: These images underwent gain reference correction and were binned by 2 before drift correction via MotionCorr ( 62 ) to pixel size of 0.676 Å.
- Full pipeline: structure determination [PHENIX, RELION v4.0] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ImageJ, MotionCor2, UCSF Chimera]

### Structural duality enables a single protein to act as a toxin-antidote pair for meiotic drive. (PNAS 2024)

- DOI: 10.1073/pnas.2408618121 | PMCID: PMC11551426 | PMID: 39485800
- Evidence: Beam-induced motion was corrected using MotionCor2 ( 69 ).
- Full pipeline: alignment/mapping [minimap2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2]

### CryoSeek: A strategy for bioentity discovery using cryoelectron microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2417046121 | PMCID: PMC11494351 | PMID: 39382995
- Evidence: The stacks were subsequently motion-corrected with MotionCor2 and binned twofold ( 35 ), resulting in a pixel size of 1.0979 Å.
- Full pipeline: quality control [MultiQC] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [MotionCor2]

### Structural basis for DNA recognition by a viral genome-packaging machine. (PNAS 2024)

- DOI: 10.1073/pnas.2406138121 | PMCID: PMC11331095 | PMID: 39116131
- Evidence: Micrographs from the first dataset were motion corrected using RELION’s implementation ( 41 ) of the MotionCor2 algorithm ( 42 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, Coot, RELION v3.1.2, Topaz]

### Structures of trehalose-6-phosphate synthase, Tps1, from the fungal pathogen &lt;i&gt;Cryptococcus neoformans&lt;/i&gt;: A target for antifungals. (PNAS 2024)

- DOI: 10.1073/pnas.2314087121 | PMCID: PMC11317593 | PMID: 39083421
- Evidence: For determination of the structure of CnTps1 bound to UDP-G6P, dose-fractionated movies were aligned with MotionCor2 ( 75 ) and CTF estimation was performed using CTFFIND4.1.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [UCSF Chimera v1.14]

### Structure of the flotillin complex in a native membrane environment. (PNAS 2024)

- DOI: 10.1073/pnas.2409334121 | PMCID: PMC11260169 | PMID: 38985763
- Evidence: Full-frame alignment was performed using MotionCor2 ( 56 ).
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [AlphaFold, ChimeraX, PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [ColabFold, Coot]

### Allosteric activation of VCP, an AAA unfoldase, by small molecule mimicry. (PNAS 2024)

- DOI: 10.1073/pnas.2316892121 | PMCID: PMC11181084 | PMID: 38833472
- Evidence: Correction of interframe movement for each pixel and dose-weighting was performed using MotionCor2 or Relion’s own implementation ( 55 – 57 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [MotionCor2, RELION]

### Bispecific antibodies targeting two glycoproteins on SFTSV exhibit synergistic neutralization and protection in a mouse model. (PNAS 2024)

- DOI: 10.1073/pnas.2400163121 | PMCID: PMC11181109 | PMID: 38830098
- Evidence: All of the raw dose-fractionated image stacks were 2× binned, aligned, dose-weighted, and summed using MotionCor2 ( 32 ).
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, MUSCLE v3.8.31, MotionCor2] -> variant calling [SAMtools v1.9] -> structure determination [Coot v0.9.3, PHENIX] -> machine learning [Topaz] -> visualisation [PyMOL v2.0] -> stage not stated [fastp]

### Principles of peptide selection by the transporter associated with antigen processing. (PNAS 2024)

- DOI: 10.1073/pnas.2320879121 | PMCID: PMC11161800 | PMID: 38805290
- Evidence: Superresolution image stacks were gain-normalized, binned by 2, and corrected for beam-induced motion using MotionCor2 ( 60 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, RELION]

### Molecular basis for antibody recognition of multiple drug-peptide/MHC complexes. (PNAS 2024)

- DOI: 10.1073/pnas.2319029121 | PMCID: PMC11145297 | PMID: 38781214
- Version used: **1.5**
- Evidence: On-the-fly processing was performed using MotionCor2 v 1.5 ( 48 ) and CTFFIND4 v 4.1.13 ( 49 ) under control of Appion ( 50 ).
- Full pipeline: structure determination [UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [MotionCor2 v1.5, PHENIX v1.18.2, Python]

### <i>Myxococcus xanthus</i> encapsulin cargo protein EncD is a flavin-binding protein with ferric reductase activity. (PNAS 2024)

- DOI: 10.1073/pnas.2400426121 | PMCID: PMC11126975 | PMID: 38748579
- Evidence: MotionCor2 was used to motion-correct the 40-frame movie stacks for drift ( 54 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> structure determination [PHENIX] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [AlphaFold, ColabFold v1.5.3, MotionCor2, RELION v4.0]

### Three-dimensional architecture of ESCRT-III flat spirals on the membrane. (PNAS 2024)

- DOI: 10.1073/pnas.2319115121 | PMCID: PMC11098116 | PMID: 38709931
- Evidence: All movies were aligned with MotionCor2 ( 70 ), and the contrast transfer function (CTF) parameters were estimated with patch CTF in cryoSPARC 3.1 ( 71 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [RELION v3.1] -> stage not stated [AlphaFold, UCSF Chimera]

### Influence of lipid bilayer on the structure of the muscle-type nicotinic acetylcholine receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2319913121 | PMCID: PMC11087746 | PMID: 38683987
- Evidence: Micrograph frame stacks were drift-corrected and dose-weighted using MotionCor2 ( 29 ).
- Full pipeline: alignment/mapping [CTFFIND, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, MotionCor2, RELION]

### C-type inactivation and proton modulation mechanisms of the TASK3 channel. (PNAS 2024)

- DOI: 10.1073/pnas.2320345121 | PMCID: PMC11046659 | PMID: 38630723
- Evidence: Movies acquired with K3 and Falcon IV detectors were subjected to motion correction for beam-induced drift and binning from superresolution to physical pixel size using MotionCor2 ( 52 ) and RELION’s own implementation (version: 4.0 beta2), respectively.
- Full pipeline: registration [MotionCor2, RELION] -> simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> stage not stated [CTFFIND, ChimeraX, PyMOL]

### Episymbiotic Saccharibacteria TM7x modulates the susceptibility of its host bacteria to phage infection and promotes their coexistence. (PNAS 2024)

- DOI: 10.1073/pnas.2319790121 | PMCID: PMC11032452 | PMID: 38593079
- Evidence: All recorded images were first drift corrected by the software MotionCor2 ( 59 ) and then stacked by the software package IMOD ( 60 ).
- Full pipeline: quantification [HTSeq v0.9.1] -> differential/statistical testing [HTSeq v0.9.1] -> stage not stated [IMOD, ImageJ, MotionCor2]

### Allosteric regulation of nitrate transporter NRT via the signaling protein PII. (PNAS 2024)

- DOI: 10.1073/pnas.2318320121 | PMCID: PMC10945777 | PMID: 38457518
- Evidence: These stacks were motion-corrected with dose weighting by MotionCor2 ( 50 ) with a binning factor of 2, resulting in a pixel size of 1.07 Å.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, MotionCor2, PyMOL, RELION v3.1]

### Human paraneoplastic antigen Ma2 (PNMA2) forms icosahedral capsids that can be engineered for mRNA delivery. (PNAS 2024)

- DOI: 10.1073/pnas.2307812120 | PMCID: PMC10945824 | PMID: 38437549
- Evidence: Movies were corrected for motion using the RELION implementation of MotionCor2, with 4 × 4 patches and dose-weighting, and CTF parameters were estimated using CTFFIND-4.1 ( 51 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, PyMOL, RELION v4.0, Topaz]

### Structural basis for CFTR inhibition by CFTR<sub>inh</sub>-172. (PNAS 2024)

- DOI: 10.1073/pnas.2316675121 | PMCID: PMC10927578 | PMID: 38422021
- Evidence: Drift correction was performed using MotionCor2 ( 57 ).
- Full pipeline: structure determination [PHENIX, RELION v3.1] -> stage not stated [MotionCor2]

### Sec7 regulatory domains scaffold autoinhibited and active conformations. (PNAS 2024)

- DOI: 10.1073/pnas.2318615121 | PMCID: PMC10927569 | PMID: 38416685
- Evidence: Standard cryoEM data processing tools (MotionCor2, GCTF, CryoSPARC, and Relion 3.1) ( 60 – 63 ) were used to correct beam-induced motion, estimate contrast transfer function parameters, pick, sort, and symmetry expand particles, and refine and reconstruct the final maps.
- Full pipeline: alignment/mapping [cryoDRGN] -> structure determination [MotionCor2, PHENIX, RELION v3.1] -> stage not stated [AlphaFold, ChimeraX, ImageJ]

### Structure of mavacamten-free human cardiac thick filaments within the sarcomere by cryoelectron tomography. (PNAS 2024)

- DOI: 10.1073/pnas.2311883121 | PMCID: PMC10907299 | PMID: 38386705
- Evidence: Damage compensated motion correction used MotionCor2 ( 85 ).
- Full pipeline: alignment/mapping [EMAN2, IMOD] -> registration [MotionCor2] -> structure determination [EMAN2, IMOD] -> stage not stated [CTFFIND]

### Dissection of the structure-function relationship of Na<sub>v</sub> channels. (PNAS 2024)

- DOI: 10.1073/pnas.2322899121 | PMCID: PMC10907234 | PMID: 38381792
- Evidence: The stacks were motion-corrected with MotionCor2 ( 41 ) or Warp ( 42 ) and binned twofold, resulting in 0.8374 Å/pixel for Na v 1.7-M2, and 1.0979 Å/pixel for Na v 1.7-M4 and Na v 1.7-M9.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, MotionCor2]

### Dark and Dronc activation in <i>Drosophila melanogaster</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2312784121 | PMCID: PMC10907274 | PMID: 38381783
- Evidence: The 32 movie frames of each micrograph were motion corrected by MotionCor2 and binned twofold.
- Full pipeline: registration [MotionCor2] -> stage not stated [RELION v3.1]

### Filament structure and subcellular organization of the bacterial intermediate filament-like protein crescentin. (PNAS 2024)

- DOI: 10.1073/pnas.2309984121 | PMCID: PMC10873595 | PMID: 38324567
- Evidence: Movies were corrected for inter-frame motions using MotionCor2 ( 48 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [IMOD, PHENIX] -> machine learning [Topaz] -> stage not stated [Coot, ImageJ, MotionCor2, RELION v3.1]

### Puromycin reveals a distinct conformation of neuronal ribosomes. (PNAS 2024)

- DOI: 10.1073/pnas.2306993121 | PMCID: PMC10873636 | PMID: 38315848
- Evidence: Cryo-EM movies were corrected for beam-induced motion using RELION’s implementation of the MotionCor2 algorithm ( 46 , 47 ).
- Full pipeline: visualisation [ChimeraX, UCSF Chimera] -> stage not stated [CTFFIND, ImageJ, MotionCor2, RELION]

### Graphene sandwich-based biological specimen preparation for cryo-EM analysis. (PNAS 2024)

- DOI: 10.1073/pnas.2309384121 | PMCID: PMC10835136 | PMID: 38252835
- Evidence: During data collection, all these micrographs were fractionated to 32 frames with a total dose of 50 e − /Å 2 , and motion-corrected through MotionCor2 ( 5 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD, RELION] -> stage not stated [MotionCor2]

### Protective human antibodies against a conserved epitope in pre- and postfusion influenza hemagglutinin. (PNAS 2024)

- DOI: 10.1073/pnas.2316964120 | PMCID: PMC10769852 | PMID: 38147556
- Evidence: Dose-fractionated images were gain normalized, aligned, dose-weighted, and summed using MotionCor2.
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> stage not stated [AlphaFold, ChimeraX, PHENIX]

### Structural insights into nonpeptide antagonist inhibition of somatostatin receptor subtype 5. (PNAS 2025)

- DOI: 10.1073/pnas.2522515122 | PMCID: PMC12745778 | PMID: 41417603
- Evidence: The initial processing of cryo-EM micrographs involved motion correction using MotionCor2 ( 34 ), followed by contrast transfer function (CTF) estimation after importing the images into CryoSPARC v4 ( 35 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold]

### The subcellular architecture of &lt;i&gt;Paratrypanosoma confusum&lt;/i&gt; revealed by CryoET: A window into early trypanosome evolution. (PNAS 2025)

- DOI: 10.1073/pnas.2521233122 | PMCID: PMC12718327 | PMID: 41359853
- Version used: **1.4.7**
- Evidence: These were used for motion correction in MotionCor2 version 1.4.7 ( 59 ) and CTF estimation with CTFFIND4 version 4.14 ( 60 ).
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2 v1.4.7] -> structure determination [IMOD]

### RAD51AP1 is a versatile RAD51 modulator. (PNAS 2025)

- DOI: 10.1073/pnas.2514728122 | PMCID: PMC12704761 | PMID: 41337480
- Evidence: For all datasets, movies were processed with MotionCor2 as implemented in relion5 ( 56 ).
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2]

### Machine learning enables de novo multiepitope design of &lt;i&gt;Plasmodium falciparum&lt;/i&gt; circumsporozoite protein to target trimeric L9 antibody. (PNAS 2025)

- DOI: 10.1073/pnas.2512358122 | PMCID: PMC12704715 | PMID: 41337490
- Evidence: Briefly, motion correction was performed in Relion using MotionCor2, and the contrast transfer function (CTF) was estimated with the Patch CTF estimation tool in CryoSPARC.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2023.2] -> structure determination [AlphaFold, PHENIX] -> stage not stated [ChimeraX, PyMOL, RELION v5.0]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Evidence: Briefly, dose-fractionated image stacks were imported into RELION ( 60 ) and subjected to motion correction with MotionCor2 ( 61 ).
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### The mechanism of pathogenic α&lt;sub&gt;1&lt;/sub&gt;-antitrypsin aggregation in the human liver. (PNAS 2025)

- DOI: 10.1073/pnas.2507535122 | PMCID: PMC12646233 | PMID: 41231946
- Version used: **1.4**
- Evidence: Preprocessing of the EM data was performed within CryoSPARC (v4.0 and v4.3.1) for ZZ:9C5 Fab (dataset B) using Patch motion correction and Patch CTF estimation ( 51 ) as well as within RELION (v4.0) for ZZ:4B12 Fab :9C5 Fab (dataset A and C) using MotionCor2 (v1.4 and v1.5) and CTFFIND4 (v4.0 and v4.1) ( 52 – 54 ).
- Full pipeline: normalisation [PHENIX] -> registration [MotionCor2 v1.4, RELION v4.0] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX, PHENIX]

### Structural insights into the dynamic mechanism of bornavirus polymerase. (PNAS 2025)

- DOI: 10.1073/pnas.2504779122 | PMCID: PMC12501175 | PMID: 40996804
- Evidence: Briefly, dose-fractionated movies were subjected to Patch motion correction using MotionCor2 ( 55 ) and Patch CTF estimation using CTFFIND-4.1.13 ( 56 ).
- Full pipeline: registration [CTFFIND, MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.7, UCSF Chimera]

### Structural and functional analysis of the &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; MmpS5L5 efflux pump presages increased bedaquiline resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2516660122 | PMCID: PMC12501195 | PMID: 40986343
- Evidence: Movies of each tilt image were aligned with MotionCor2 ( 79 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2, RELION] -> structure determination [PHENIX v1.21.2] -> stage not stated [AlphaFold, ChimeraX, Coot v0.9.8.93]

### Structurally diverse viral inhibitors converge on a shared mechanism to stall the antigen transporter TAP. (PNAS 2025)

- DOI: 10.1073/pnas.2516676122 | PMCID: PMC12478189 | PMID: 40956880
- Evidence: For the BNLF2a, US6, and RH185 datasets, superresolution image stacks were gain-normalized, binned by 2, and corrected for beam-induced motion using MotionCor2 ( 63 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ChimeraX, RELION]

### How palytoxin transforms the Na&lt;sup&gt;+&lt;/sup&gt;,K&lt;sup&gt;+&lt;/sup&gt; pump into a cation channel. (PNAS 2025)

- DOI: 10.1073/pnas.2506450122 | PMCID: PMC12478176 | PMID: 40956884
- Evidence: All movies were aligned by MotionCor2 ( 49 ) with dose weighting.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [RELION]

### Binding of &lt;i&gt;Fusobacterium nucleatum&lt;/i&gt; autotransporter adhesin CbpF to human CEACAM1 and CEACAM5: A Velcro model for bacterium adhesion. (PNAS 2025)

- DOI: 10.1073/pnas.2516574122 | PMCID: PMC12452904 | PMID: 40928870
- Evidence: Generally, MotionCor2 ( 52 ) was used to generate micrographs from the movies, followed by the CTF estimation ( 53 ), particles picked out and extracted and 2D classification.
- Full pipeline: structure determination [ChimeraX, Coot v0.9.8.92, PHENIX, PyMOL] -> visualisation [PyMOL] -> stage not stated [CCP4, MotionCor2]

### Structural insights into the substrate uptake and inhibition of the human creatine transporter (hCRT). (PNAS 2025)

- DOI: 10.1073/pnas.2426135122 | PMCID: PMC12435270 | PMID: 40892912
- Evidence: Image processing included aligning and summing all 32 frames of each stack using MotionCor2 ( 62 ), followed by merging the resultant images to achieve a final pixel size of 0.8433 Å (hCRTC and hCRTR) and 0.856 Å (hCRTapo).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> visualisation [ChimeraX]

### Critical role of extracellular loops in differential modulations of TTX-sensitive and TTX-resistant Na&lt;sub&gt;v&lt;/sub&gt; channels. (PNAS 2025)

- DOI: 10.1073/pnas.2510355122 | PMCID: PMC12358880 | PMID: 40768348
- Evidence: The stacks were motion corrected with MotionCor2 ( 52 ) and binned twofold, resulting in 1.091 Å/pixel for Na v 1.5-β1-TTX-CaM, and 1.0979 Å/pixel for Na v 1.7 variants with β1.
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [CTFFIND, PyMOL, RELION]

### Generation of actionable, cancer-specific neoantigens from KRAS(G12C) with adagrasib. (PNAS 2025)

- DOI: 10.1073/pnas.2509012122 | PMCID: PMC12337345 | PMID: 40737322
- Version used: **1.5**
- Evidence: On-the-fly processing was performed using MotionCor2 v 1.5 ( 26 ) and CTFFIND4 v 4.1.13 ( 27 ) under the control of Appion ( 28 ).
- Full pipeline: structure determination [UCSF Chimera] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2 v1.5, PHENIX v1.18.2, Python]

### Structural basis of auxin binding and transport by <i>Arabidopsis thaliana</i> AUX1. (PNAS 2025)

- DOI: 10.1073/pnas.2513424122 | PMCID: PMC12337342 | PMID: 40720658
- Evidence: Motion correction was performed using MotionCor2 ( 46 ) with a binning factor of 2, generating a pixel size of 1.0773 Å.
- Full pipeline: registration [MotionCor2] -> simulation/modelling [OpenMM, VMD] -> structure determination [PHENIX] -> machine learning [OpenMM] -> visualisation [VMD] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, Coot]

### Structures of &lt;i&gt;Chaetomium thermophilum&lt;/i&gt; TOM complexes with bound preproteins. (PNAS 2025)

- DOI: 10.1073/pnas.2507279122 | PMCID: PMC12305020 | PMID: 40674418
- Evidence: To account for and correct for beam-induced motion and radiation damage, the Relion 3.0 implementation of MotionCorr was applied to 15,566 movies of the substrate-free TOM complex ( 46 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot, MotionCor2, RELION v3.0]

### Structure of the virulence-associated &lt;i&gt;Neisseria meningitidis&lt;/i&gt; filamentous bacteriophage MDAΦ. (PNAS 2025)

- DOI: 10.1073/pnas.2420157122 | PMCID: PMC12207478 | PMID: 40540604
- Evidence: EER movies were converted to TIF and motion-corrected using the RELION4 implementation of MotionCor2 ( 39 , 40 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION, Topaz]

### Cryo-EM structures of GnRHR: Foundations for next-generation therapeutics. (PNAS 2025)

- DOI: 10.1073/pnas.2500112122 | PMCID: PMC12207466 | PMID: 40523184
- Evidence: Dose-fractionated image stacks were subjected to motion correction by MotionCor2 ( 47 ).
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, ChimeraX, PHENIX] -> visualisation [PyMOL]

### Structure and organization of full-length epidermal growth factor receptor in extracellular vesicles by cryo-electron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2424678122 | PMCID: PMC12167996 | PMID: 40455995
- Evidence: The movies and mdoc files were imported, the frames were motion-corrected using MotionCor2 ( 79 ) and the contrast transfer function (CTF) was measured using the CTFFIND4 package ( 80 ).
- Full pipeline: read trimming [edgeR] -> alignment/mapping [IMOD] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX] -> visualisation [EMAN2] -> stage not stated [AlphaFold, ImageJ, MotionCor2, RELION]

### Molecular basis for ligand recognition and receptor activation of the prostaglandin D2 receptor DP1. (PNAS 2025)

- DOI: 10.1073/pnas.2501902122 | PMCID: PMC12146711 | PMID: 40440061
- Evidence: MotionCor2 was used to perform frame-based motion correction and generate drift-corrected micrographs for further processing ( 38 , 39 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, R v3.50]

### Microtubule dynamics are defined by conformations and stability of clustered protofilaments. (PNAS 2025)

- DOI: 10.1073/pnas.2424263122 | PMCID: PMC12146719 | PMID: 40440074
- Evidence: Tomograms were reconstructed and denoised as described previously, ( 55 , 73 ) using tomograms generated with even and odd frames after alignment with MotionCor2, ( 83 ) and tilt series alignment and back projection performed in IMOD ( 84 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> simulation/modelling [GROMACS, VMD] -> structure determination [IMOD, MotionCor2] -> visualisation [VMD] -> stage not stated [Matplotlib v3.8.2, NumPy v1.26, Python v3.9, SciPy v1.11, seaborn v0.13]

### Structure and evolution of photosystem I in the early-branching cyanobacterium &lt;i&gt;Anthocerotibacter panamensis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2427090122 | PMCID: PMC12107172 | PMID: 40366692
- Evidence: Motion correction, alignment, and dose-weighting was performed with MotionCor2 ( 59 ).
- Full pipeline: alignment/mapping [Clustal Omega, MotionCor2] -> registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [IQ-TREE v2.2, RELION v3.1, UCSF Chimera]

### Structural insights into the activation of the human prostaglandin E&lt;sub&gt;2&lt;/sub&gt; receptor EP1 subtype by prostaglandin E&lt;sub&gt;2&lt;/sub&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2423840122 | PMCID: PMC12107139 | PMID: 40366695
- Evidence: MotionCor2 was used for frame-based motion correction ( 46 ) and defocus parameters were estimated using Patch CTF All subsequent steps were performed using CryoSPARC V4.5.3 ( 47 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, R v7.40, Topaz]

### Reducing the effects of radiation damage in cryo-EM using liquid helium temperatures. (PNAS 2025)

- DOI: 10.1073/pnas.2421538122 | PMCID: PMC12054821 | PMID: 40261934
- Evidence: To process the data, the tiff movies were imported into RELION 4.0 ( 41 ) and motion corrected with RELION’s own implementation of MotionCor2 ( 42 ).
- Full pipeline: alignment/mapping [Python] -> registration [MotionCor2, RELION v4.0] -> stage not stated [CTFFIND]

### Structure of a Gcn2 dimer in complex with the large 60S ribosomal subunit. (PNAS 2025)

- DOI: 10.1073/pnas.2415807122 | PMCID: PMC12012509 | PMID: 40198700
- Evidence: First, preprocessing steps were performed in RELION: Movie frames were aligned with MotionCor2 ( 70 ) using 5 × 5 patches followed by CTF estimation of the resulting micrographs using CTFFIND4 ( 71 ) using power spectra from the MotionCor run.
- Full pipeline: alignment/mapping [MotionCor2] -> stage not stated [ChimeraX, Coot, PHENIX, RELION v4.0.1]

### Structural basis of the cysteinyl leukotriene receptor type 2 activation by LTD4. (PNAS 2025)

- DOI: 10.1073/pnas.2417148122 | PMCID: PMC12012480 | PMID: 40193607
- Evidence: MotionCor2 was used to perform the frame-based motion-correction algorithm to generate drift-corrected micrograph for further processing and defocus parameters were estimated by CTFFIND 4.0 ( 41 , 42 ).
- Full pipeline: visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v4.0, MotionCor2, PHENIX, R v3.50, UCSF Chimera]

### DNA bending mediated by ORC is essential for replication licensing in budding yeast. (PNAS 2025)

- DOI: 10.1073/pnas.2502277122 | PMCID: PMC12002289 | PMID: 40184174
- Evidence: Drift correction of the collected movies was performed using MotionCor2 ( 58 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [EMAN2, ImageJ, MotionCor2, RELION]

### Cryo-EM structure of cyanopodophage A4 reveals a pentameric pre-ejectosome in the double-stabilized capsid. (PNAS 2025)

- DOI: 10.1073/pnas.2423403122 | PMCID: PMC12002296 | PMID: 40163721
- Evidence: The movie frames were motion corrected and dose weighted using MotionCor2 ( 58 ), and the defocus value for each micrograph was determined using CtfFind4 ( 59 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Structural basis of DNA replication fidelity of the Mpox virus. (PNAS 2025)

- DOI: 10.1073/pnas.2411686122 | PMCID: PMC11912389 | PMID: 40035768
- Version used: **1.2.4**
- Evidence: The MotionCor2 (v1.2.4) ( 47 ) was used to correct the beam-induced shifts of raw movies.
- Full pipeline: structure determination [PHENIX, RELION] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2 v1.2.4]

### Stepwise activation of SARM1 for cell death and axon degeneration revealed by a biosynthetic NMN mimic. (PNAS 2025)

- DOI: 10.1073/pnas.2424906122 | PMCID: PMC11874154 | PMID: 39964720
- Evidence: For the SARM1 (WT)-M1 complex, a total of 6,554 movie stacks were processed using MotionCor2 for motion correction, followed by patch-based CTF estimation in CryoSPARC ( 31 ).
- Full pipeline: quantification [ImageJ] -> registration [MotionCor2, Topaz] -> structure determination [PHENIX, Topaz] -> stage not stated [ChimeraX, PyMOL]

### Biochemical and structural bases for talin ABSs-F-actin interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2405922122 | PMCID: PMC11831117 | PMID: 39903122
- Evidence: Motion correction and binning to a working pixel size of 0.83Å/pixel was carried out by MotionCor2 ( 52 ), defocus values were measured by CTFFIND 4.1 ( 53 ) and subsequent image analysis was carried out using RELION 3.1 ( 54 ).
- Full pipeline: registration [CTFFIND v4.1, MotionCor2, RELION v3.1] -> structure determination [PHENIX]

### Structural insights into the role of reduced cysteine residues in SOD1 amyloid filament formation. (PNAS 2025)

- DOI: 10.1073/pnas.2408582122 | PMCID: PMC11804504 | PMID: 39874287
- Evidence: Movie frames were dose-weighted using the MotionCor2 algorithm ( 54 ), and the contrast transfer function was estimated using CTFFIND-4.1 ( 55 ).
- Full pipeline: structure determination [PHENIX v1.21] -> visualisation [ChimeraX v1.4, PyMOL v3.0] -> stage not stated [CTFFIND, ImageJ, MotionCor2, RELION]

### Molecular mechanism of ligand recognition and activation of lysophosphatidic acid receptor LPAR6. (PNAS 2025)

- DOI: 10.1073/pnas.2415426122 | PMCID: PMC11789011 | PMID: 39847322
- Evidence: Similar to previous studies ( 31 – 34 ), the raw movie frames were initially downsampled to a pixel size of 1.1 Å and motion-corrected using MotionCor2 ( 35 ).
- Full pipeline: alignment/mapping [AlphaFold] -> dimensionality reduction/clustering [RELION] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v4.1, MotionCor2, R v3.50]

### Structural determinants of oxygen resistance and Zn&lt;sup&gt;2+&lt;/sup&gt;-mediated stability of the [FeFe]-hydrogenase from &lt;i&gt;Clostridium beijerinckii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2416233122 | PMCID: PMC11760498 | PMID: 39805018
- Evidence: The movie frames were subjected to beam-induced movement correction using MotionCor2.1 and contrast transfer function (CTF) was evaluated using Gctf ( 46 , 47 ).
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, MotionCor2, RELION]

### Molecular basis of Spns1-mediated lysophospholipid transport from the lysosome. (PNAS 2025)

- DOI: 10.1073/pnas.2409596121 | PMCID: PMC11725778 | PMID: 39739806
- Evidence: Motion correction was performed in RELION 3.1 using MotionCor2 ( 42 ) or its own implementation with an EER fractionation of 22 ( 43 ).
- Full pipeline: registration [MotionCor2, RELION v3.1] -> structure determination [PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold, NAMD]

### CryoSeek II: Cryo-EM analysis of glycofibrils from freshwater reveals well-structured glycans coating linear tetrapeptide repeats. (PNAS 2025)

- DOI: 10.1073/pnas.2423943122 | PMCID: PMC11725842 | PMID: 39739783
- Evidence: The stacks were subsequently motion-corrected with MotionCor2 and binned twofold ( 48 ), resulting in a pixel size of 1.0979 Å.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [MotionCor2]

### Tetrameric PilZ protein stabilizes stator ring in complex flagellar motor and is required for motility in &lt;i&gt;Campylobacter jejuni&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2412594121 | PMCID: PMC11725899 | PMID: 39793078
- Evidence: Image drifting induced by the electron beam was corrected by MotionCor2 ( 66 ).
- Full pipeline: alignment/mapping [CTFFIND, IMOD] -> structure determination [ChimeraX] -> stage not stated [AlphaFold, ColabFold, MotionCor2]

### Measurement of atomic scattering factors by cryoelectron microscopy. (PNAS 2026)

- DOI: 10.1073/pnas.2528758123 | PMCID: PMC13167779 | PMID: 42101996
- Evidence: First the movies were motion corrected with MotionCor2 ( 70 ), and the CTFs were fitted using CTFFIND4 ( 71 ).
- Full pipeline: registration [MotionCor2] -> structure determination [RELION] -> stage not stated [CCP4, Coot, PyMOL]

### Molecular structure of the ESCRT-III-based archaeal CdvAB cell division machinery. (PNAS 2026)

- DOI: 10.1073/pnas.2525941123 | PMCID: PMC12818579 | PMID: 41543908
- Evidence: Micrographs were motion-corrected with RELION’s MotionCor2 implementation and CTF estimated with CTFFIND4.
- Full pipeline: alignment/mapping [MAFFT, PyMOL] -> structure determination [Coot, PHENIX, RELION] -> visualisation [ChimeraX v1.7.1] -> stage not stated [AlphaFold, MotionCor2]

### RNA-activated protein cleavage with a CRISPR-associated endopeptidase. (Science 2022)

- DOI: 10.1126/science.add7450 | PMCID: PMC10028731 | PMID: 36423276
- Evidence: Movies were corrected for motion using the RELION implementation of MotionCor2, with 5-by-5 patches and dose-weighting, and Contrast Transfer Function (CTF) parameters were estimated using CTFFIND-4.1 ( 38 ).
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, Coot, Jupyter, MotionCor2, RELION]

### DNSN-1 recruits GINS for CMG helicase assembly during DNA replication initiation in &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (Science 2023)

- DOI: 10.1126/science.adi4932 | PMCID: PMC7615117 | PMID: 37590372
- Evidence: The 41-fraction movies were aligned and dose-weighted (0.977 e-/Å2/fraction, 5 x 5 patches, 300 Å2 B-factor) using RELION’s implementation of a MotionCor2-like program ( 62 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, ImageJ, RELION]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: Movies were corrected for motion using the RELION implementation of MotionCor2, with 6×4 patches and dose-weighting.
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

### Molecular mechanism of dynein-dynactin complex assembly by LIS1. (Science 2024)

- DOI: 10.1126/science.adk8544 | PMCID: PMC7615804 | PMID: 38547289
- Evidence: Global motion correction and dose-weighting were performed in Relion-4.0 ( 99 ) using MotionCor2 ( 100 ) with a B-factor of 150 and 5X5 patches.
- Full pipeline: alignment/mapping [ChimeraX] -> quantification [R] -> registration [MotionCor2, RELION] -> differential/statistical testing [R] -> structure determination [PHENIX] -> machine learning [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, ColabFold, ImageJ, UCSF Chimera]

### Autoinhibition imposed by a large conformational switch of INO80 regulates nucleosome positioning. (Science 2025)

- DOI: 10.1126/science.adr3831 | PMCID: PMC12403922 | PMID: 40674492
- Evidence: In brief, movie stacks were motion-corrected and dose-weighted with MotionCor2 ( 46 ).
- Full pipeline: quantification [ImageJ] -> structure determination [PHENIX, RELION] -> stage not stated [MotionCor2]

### TIGR-Tas: A family of modular RNA-guided DNA-targeting systems in prokaryotes and their viruses. (Science 2025)

- DOI: 10.1126/science.adv9789 | PMCID: PMC12045711 | PMID: 40014690
- Evidence: Cryo-EM data processing Movies were corrected for motion using the RELION implementation of MotionCor2, with 6x4 patches and dose-weighting.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, MAFFT, PyMOL] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [MAFFT, PHENIX] -> stage not stated [CTFFIND, ColabFold, Coot, HMMER, MotionCor2, RELION, Topaz]

### Structural mechanism of LINE-1 target-primed reverse transcription. (Science 2025)

- DOI: 10.1126/science.ads8412 | PMCID: PMC7617806 | PMID: 40048554
- Evidence: 25,374 movies were gain-corrected, dose-weighted and motion-corrected using the RELION implementation of MotionCor2.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, PHENIX v1.21.1, RELION] -> stage not stated [CTFFIND, ChimeraX, ImageJ, MotionCor2, PyMOL, Python, REFMAC, Topaz]

### Structure and organization of AMPA receptor-TARP complexes in the mammalian cerebellum. (Science 2026)

- DOI: 10.1126/science.aeb3577 | PMCID: PMC7619101 | PMID: 41379938
- Evidence: Cryo-EM data processing and model building For the GluA2 containing dataset, a total of 51,245 movies were imported into RELION 5.0 ( 78 ), and beam-induced motion was corrected using MotionCor2 ( 79 ).
- Full pipeline: alignment/mapping [MUSCLE] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [PyMOL v2.5] -> stage not stated [AlphaFold, MotionCor2, RELION v5.0]

