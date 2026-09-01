# CTFFIND

- **Category:** structbio
- **Papers in survey:** 152
- **Journals:** PNAS (77), Nature (52), Cell (14), Science (9)
- **Years:** 2021 (15), 2022 (41), 2023 (32), 2024 (30), 2025 (30), 2026 (4)
- **Versions named:** 4.1 (14), 1.06 (14), 1.18 (5), 4.1.14 (3), 4.1.8 (3), 4.1.13 (2), 4.0 (2), 4.1.10 (1), 1.14 (1), 4.16 (1)
- **Pipeline stages it appears in:** registration (12), alignment/mapping (12), structure determination (3), normalisation (1)

## Papers

### In vitro and in vivo functions of SARS-CoV-2 infection-enhancing and neutralizing antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.021 | PMCID: PMC8232969 | PMID: 34242577
- Evidence: Images were imported, CTF-corrected with CTFFIND, and particles were picked using a spike template from previous 2D class averages of spike alone.
- Full pipeline: stage not stated [CTFFIND, ChimeraX, Coot, PHENIX, PyMOL, RELION, UCSF Chimera]

### Simultaneous binding of Guidance Cues NET1 and RGM blocks extracellular NEO1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.045 | PMCID: PMC8063088 | PMID: 33740419
- Version used: **4.1**
- Evidence: ...ELION 3.1 ( Zivanov et al., 2018 ) https://www3.mrc-lmb.cam.ac.uk/relion/index.php/Main_Page cryoSPARC ( Punjani et al., 2017 ) https://cryosparc.com CTFFIND 4.1 ( Rohou and Grigorieff, 2015 ) https://grigoriefflab.umassmed.edu/ctffind4 UCSF Chimera ( Goddard et al., 2007 ) https://www.cgl.ucsf.edu/chimera/download.html Phenix ( Afonine et al., 2018 ) https://www.phenix-online.org/download/ XIA2 (...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [MotionCor2] -> stage not stated [CTFFIND v4.1, Clustal Omega, ImageJ, PHENIX, PyMOL, RELION v3.1, UCSF Chimera]

### Structural basis for the assembly of the type V CRISPR-associated transposon complex. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.009 | PMCID: PMC9798831 | PMID: 36435179
- Version used: **1.06**
- Evidence: .../doku.php cryoSPARC 3.2.0 Punjani et al., 2017 44 https://cryosparc.com/ MotionCor2 1.4.0 Zheng et al., 2017 45 https://emcore.ucsf.edu/ucsf-software Gctf 1.06 Zhang, 2016 46 https://www2.mrc-lmb.cam.ac.uk/research/locally-developed-software/zhang-software/ crYOLO version 1.7.6 Wagner et al., 2019 47 https://cryolo.readthedocs.io/en/stable/ Phenix 1.19.1–4122 Adams et al., 2010 48 Afonine et al., ...
- Full pipeline: stage not stated [CTFFIND v1.06, ChimeraX v1.2, Coot, MotionCor2 v1.4.0, PHENIX v1.19.1, RELION v3.1.2, UCSF Chimera v1.14]

### BacPROTACs mediate targeted protein degradation in bacteria. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.009 | PMCID: PMC9240326 | PMID: 35662409
- Version used: **1.06**
- Evidence: ...biophysics cryoSPARC v2 ( Punjani et al., 2017 ) https://cryosparc.com/ MotionCor2 1.0.5 ( Zheng et al., 2017 ) https://emcore.ucsf.edu/ucsf-software Gctf 1.06 ( Zhang, 2016 ) N/A crYOLO v1.3.5 ( Wagner et al., 2019 ) http://sphire.mpg.de RELION 3.0 ( Zivanov et al., 2018 ) N/A Coot ( Emsley et al., 2010 ) https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/ Phenix ( Afonine et al., 2018 ), ( Lie...
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX, Coot, MotionCor2 v1.0.5, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Broad neutralization of SARS-CoV-2 variants by an inhalable bispecific single-domain antibody. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.009 | PMCID: PMC8907017 | PMID: 35344711
- Evidence: Parameters of contrast transfer function (CTF) were estimated by using Gctf.
- Full pipeline: stage not stated [CTFFIND, ChimeraX, MotionCor2, PHENIX, PyMOL, RELION v3.0, UCSF Chimera]

### Structural and functional characterizations of infectivity and immune evasion of SARS-CoV-2 Omicron. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.019 | PMCID: PMC8786603 | PMID: 35120603
- Evidence: ...ron S-trimer at pH 7.5 This manuscript PDB ID 7WG6 , EMD-32478 Software igraph (1.2.5) N/A https://cran.r-project.org/web/packages/ igraph/index.html Gctf program (v1.06) N/A https://www2.mrc-lmb.cam.ac.uk/download/gctf/ RELION (v3.07) Zivanov et al., 2018 https://www2.mrc-lmb.cam.ac.uk/relion UCSF Chimera N/A https://www.cgl.ucsf.edu/chimera UCSF ChimeraX N/A https://www.rbvi.ucsf.edu/chimerax/ P...
- Full pipeline: structure determination [Coot] -> stage not stated [CTFFIND, ChimeraX, MotionCor2, PHENIX, RELION v3.07, UCSF Chimera, igraph v1.2.5]

### Structural evolution of fibril polymorphs during amyloid assembly. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.025 | PMCID: PMC7617692 | PMID: 38134875
- Version used: **4.16**
- Evidence: 66 https://relion.readthedocs.io/en/release-4.0/Installation.html#download-relion CTFFIND 4.16 Rohou and Grigorieff 67 https://grigoriefflab.umassmed.edu/ctf_estimation_ctffind_ctftilt crYOLO V1.7 Wagner et al.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND v4.16, ChimeraX, Conda, PyMOL]

### TMEM106B is a receptor mediating ACE2-independent SARS-CoV-2 cell entry. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.005 | PMCID: PMC10409496 | PMID: 37421949
- Version used: **1.06**
- Evidence: 86 https://emcore.ucsf.edu/ucsf-software Gctf (v1.06) Zhang et al.
- Full pipeline: quantification [ImageJ] -> structure determination [Coot] -> machine learning [Topaz] -> stage not stated [AlphaFold, CTFFIND v1.06, PHENIX, RELION v4.0, UCSF Chimera]

### Structure of the endosomal Commander complex linked to Ritscher-Schinzel syndrome. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.003 | PMCID: PMC10187114 | PMID: 37172566
- Evidence: CTFFIND-4.1, integrated within RELION, was used to estimate the contrast transfer function (CTF) parameters for the motion-corrected micrographs.
- Full pipeline: alignment/mapping [ColabFold, MAFFT, PyMOL] -> normalisation [CCP4] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, HMMER v3.3.2, PHENIX, RELION, Topaz]

### Systemwide disassembly and assembly of SCF ubiquitin ligase complexes. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.035 | PMCID: PMC10156175 | PMID: 37028429
- Version used: **4.1**
- Evidence: 69 https://www3.mrc-lmb.cam.ac.uk/relion Gautomatch v0.56 Kai Zhang https://www2.mrc-lmb.cam.ac.uk/download/gautomatch-056/ CTFFIND v4.1 Rohou and Grigorieff 70 https://grigoriefflab.umassmed.edu/ctffind4 GCTF v1.06 Zhang 71 https://www2.mrc-lmb.cam.ac.uk/download/gctf/ MotionCor2 v1.1 Zheng et al.
- Full pipeline: structure determination [PHENIX] -> stage not stated [CTFFIND v4.1, ChimeraX v1.2, ImageJ, MotionCor2 v1.1, PyMOL v2.3.3, RELION v3.1, UCSF Chimera]

### A trailing ribosome speeds up RNA polymerase at the expense of transcript fidelity via force and allostery. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.008 | PMCID: PMC10135430 | PMID: 36931247
- Evidence: Defocus estimation and contrast transfer function (CTF) fitting were performed using the Gctf package 173 in RELION.
- Full pipeline: alignment/mapping [ChimeraX, MotionCor2] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, PyMOL v1.6, RELION v3.1]

### Cryo-EM structure of gas vesicles for buoyancy-controlled motility. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.041 | PMCID: PMC9994262 | PMID: 36868215
- Version used: **1.06**
- Evidence: 41 https://github.com/3dem/relion Gctf 1.06 Zhang 42 https://www.mrc-lmb.cam.ac.uk/kzhang/ cryoSPARC 3.1 and 3.3 Punjani et al.
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX v1.4, ColabFold, HMMER, ImageJ, PHENIX v1.13, RELION v3.1, SciPy]

### Discovery of natural-product-derived sequanamycins as potent oral anti-tuberculosis agents. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.043 | PMCID: PMC9994261 | PMID: 36827973
- Evidence: 44 https://emcore.ucsf.edu/ucsf-software Gctf Zhang 45 https://www2.mrc-lmb.cam.ac.uk/download/gctf/ Gautomatch Kai Zhang http://www.mrc-lmb.cam.ac.uk/kzhang/ MATLAB R2021a MathWorks® https://www.mathworks.com/products/new_products/release2021a.html Other Plate reader Perkin Elmer Envision fluorescent microscope HCS reader Cellomics ArrayScan VTI Thermo Fisher Cellomics ArrayScan VTI RNA extractio...
- Full pipeline: stage not stated [CTFFIND, MotionCor2, PHENIX, PyMOL, RELION]

### Molecular basis for shifted receptor recognition by an encephalitic arbovirus. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.029 | PMCID: PMC12406711 | PMID: 40187345
- Evidence: 64 N/A CTFFIND-4.1 v4.1.14 Rohou et al.
- Full pipeline: structure determination [ChimeraX, Coot v0.9.8.91, PHENIX v1.21r, UCSF Chimera v1.6.1] -> stage not stated [AlphaFold, CTFFIND, MotionCor2 v1.6.4, PyMOL v3.0.2, RELION v3.1]

### Structure of Venezuelan equine encephalitis virus in complex with the LDLRAD3 receptor. (Nature 2021)

- DOI: 10.1038/s41586-021-03963-9 | PMCID: PMC8550936 | PMID: 34646020
- Evidence: Contrast transfer function parameters of the electron micrographs were estimated using Gctf 35 , and particles were auto-picked using crYOLO 36 .
- Full pipeline: differential/statistical testing [RELION] -> structure determination [PHENIX, RELION] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, MotionCor2]

### Structural insights into how Prp5 proofreads the pre-mRNA branch site. (Nature 2021)

- DOI: 10.1038/s41586-021-03789-5 | PMCID: PMC8357632 | PMID: 34349264
- Evidence: The defocus values and equiphase averaging (EPA) of the micrographs were determined using Gctf 28 .
- Full pipeline: structure determination [PHENIX v1.13] -> stage not stated [CTFFIND, ChimeraX v1.1, Coot v0.8.9.2, RELION v3.0, UCSF Chimera v1.13.1]

### Structural basis of GABA<sub>B</sub> receptor-G<sub>i</sub> protein coupling. (Nature 2021)

- DOI: 10.1038/s41586-021-03507-1 | PMCID: PMC8222003 | PMID: 33911284
- Evidence: Contrast transfer function parameters for non-dose-weighted micrographs were determined by Gctf 39 .
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, RELION v3.1]

### Ubiquitin ligation to F-box protein targets by SCF-RBR E3-E3 super-assembly. (Nature 2021)

- DOI: 10.1038/s41586-021-03197-9 | PMCID: PMC7904520 | PMID: 33536622
- Evidence: Each drift-corrected micrograph was then contrast-transfer-function-corrected via Gctf 61 .
- Full pipeline: alignment/mapping [RELION v3.00] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [CTFFIND]

### Functional refolding of the penetration protein on a non-enveloped virus. (Nature 2021)

- DOI: 10.1038/s41586-020-03124-4 | PMCID: PMC8297411 | PMID: 33442061
- Evidence: We determined the contrast transfer function (CTF) parameters using Gctf 31 from total-summed images.
- Full pipeline: alignment/mapping [IMOD, MAFFT, MotionCor2, Python] -> registration [MotionCor2] -> structure determination [EMAN2] -> stage not stated [CTFFIND, Matplotlib, PyMOL]

### Close relatives of MERS-CoV in bats use ACE2 as their functional receptors. (Nature 2022)

- DOI: 10.1038/s41586-022-05513-3 | PMCID: PMC9734910 | PMID: 36477529
- Evidence: The raw data were aligned and averaged into motion-corrected summed images, after which, defocus values for each micrograph were determined using Gctf.
- Full pipeline: alignment/mapping [CTFFIND, Clustal Omega, MUSCLE] -> structure determination [Coot v0.9.4, PHENIX v1.19, RELION, UCSF Chimera v1.15] -> stage not stated [ChimeraX v1.1, MotionCor2 v1.3.0]

### Structure of the OMEGA nickase IsrB in complex with ωRNA and target DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05324-6 | PMCID: PMC9581776 | PMID: 36224386
- Evidence: Defocus parameters were estimated by CTFFIND-4.1 (ref.
- Full pipeline: alignment/mapping [MAFFT, MotionCor2] -> structure determination [ColabFold, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND, Python]

### Structural basis for directional chitin biosynthesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05244-5 | PMCID: PMC9556331 | PMID: 36131020
- Evidence: Contrast transfer function parameters on each summed image were estimated with the Gctf program 45 .
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2019.3] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, RELION v3.08]

### Structures of α-synuclein filaments from human brains with Lewy pathology. (Nature 2022)

- DOI: 10.1038/s41586-022-05319-3 | PMCID: PMC7613749 | PMID: 36108674
- Evidence: Contrast transfer function (CTF) parameters were estimated using CTFFIND-4.1 ( 59 ).
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [CTFFIND, Coot]

### The mechanism of RNA capping by SARS-CoV-2. (Nature 2022)

- DOI: 10.1038/s41586-022-05185-z | PMCID: PMC9492545 | PMID: 35944563
- Evidence: The CTF parameters were calculated using Gctf 49 , and images with estimated CTF max resolution better than 5 Å were selected for further processing.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX, RELION] -> stage not stated [CTFFIND, ImageJ]

### Archaic chaperone-usher pili self-secrete into superelastic zigzag springs. (Nature 2022)

- DOI: 10.1038/s41586-022-05095-0 | PMCID: PMC9452303 | PMID: 35853476
- Version used: **4.1.13**
- Evidence: CTF was estimated using CTFFIND (v.4.1.13).
- Full pipeline: quantification [ImageJ v1.53k] -> registration [MotionCor2 v1.2.3] -> structure determination [MotionCor2 v1.2.3, PHENIX v1.8.2, RELION v3.0.8, UCSF Chimera] -> stage not stated [CTFFIND v4.1.13, Coot v0.9.4]

### Cryo-EM structure of a type IV secretion system. (Nature 2022)

- DOI: 10.1038/s41586-022-04859-y | PMCID: PMC9259494 | PMID: 35732732
- Version used: **4.1**
- Evidence: Image processing of T4SS MOTIONCOR2 46 was used for motion correction and dose weighting, followed by contrast transfer function (CTF) estimation using CTFFIND v4.1 47 .
- Full pipeline: registration [CTFFIND v4.1] -> simulation/modelling [Coot] -> structure determination [Coot, PHENIX v1.18.2, RELION v3.1] -> machine learning [AlphaFold] -> stage not stated [ChimeraX v1.1, HMMER, PyMOL v2.3.2]

### Mechanism of replication origin melting nucleated by CMG helicase assembly. (Nature 2022)

- DOI: 10.1038/s41586-022-04829-4 | PMCID: PMC9242855 | PMID: 35705812
- Evidence: The CTF of each micrograph was estimated using Gctf (ref.
- Full pipeline: structure determination [Coot v0.9.1] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [CTFFIND, PHENIX, RELION]

### Discovery of non-squalene triterpenes. (Nature 2022)

- DOI: 10.1038/s41586-022-04773-3 | PMCID: PMC9177416 | PMID: 35650436
- Evidence: The non-weighted movie sums were used for contrast transfer function (CTF) estimation with Gctf 56 .
- Full pipeline: alignment/mapping [Clustal Omega v2.0.12, RELION] -> visualisation [PyMOL] -> stage not stated [AlphaFold, AutoDock Vina, CTFFIND, PHENIX v1.19.2, UCSF Chimera]

### USP14-regulated allostery of the human proteasome by time-resolved cryo-EM. (Nature 2022)

- DOI: 10.1038/s41586-022-04671-8 | PMCID: PMC9117149 | PMID: 35477760
- Evidence: Drift-corrected micrographs were used for the determination of the micrograph CTF parameters with the Gctf program 47 .
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, Coot, EMAN2, MotionCor2, RELION]

### Opening of glutamate receptor channel to subconductance levels. (Nature 2022)

- DOI: 10.1038/s41586-022-04637-w | PMCID: PMC9068512 | PMID: 35444281
- Version used: **1.06**
- Evidence: Contrast transfer function (CTF) estimation was performed using Gctf 1.06 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot v0.9.2] -> stage not stated [CTFFIND v1.06, PHENIX v1.18, RELION v3.1, UCSF Chimera v1.14, VMD v1.9.3]

### Structural basis of tethered agonism of the adhesion GPCRs ADGRD1 and ADGRF1. (Nature 2022)

- DOI: 10.1038/s41586-022-04580-w | PMCID: PMC9046087 | PMID: 35418679
- Version used: **1.18**
- Evidence: Contrast transfer function (CTF) parameters for each image were determined by Gctf v.1.18 41 .
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold, ChimeraX v1.1, Coot, PHENIX] -> visualisation [PyMOL v1.8, UCSF Chimera v1.15] -> stage not stated [CTFFIND v1.18, RELION v3.1]

### Age-dependent formation of TMEM106B amyloid filaments in human brains. (Nature 2022)

- DOI: 10.1038/s41586-022-04650-z | PMCID: PMC9095482 | PMID: 35344985
- Evidence: The micrographs were used to estimate the contrast transfer function (CTF) using CTFFIND-4.1 (ref.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [AlphaFold, CTFFIND, Coot]

### Activation mechanism of the class D fungal GPCR dimer Ste2. (Nature 2022)

- DOI: 10.1038/s41586-022-04498-3 | PMCID: PMC8942848 | PMID: 35296853
- Evidence: CTF parameters were estimated from non-dose-weighted micrographs in GCTF 45 with equiphase averaging for antagonist-bound and agonist-bound Ste2 datasets and CTFFIND-4.1 in RELION3.1 46 for ligand-free Ste2 dataset.
- Full pipeline: registration [MotionCor2] -> differential/statistical testing [RELION] -> simulation/modelling [GROMACS] -> structure determination [ChimeraX, MotionCor2, PHENIX, RELION] -> visualisation [PyMOL] -> stage not stated [CTFFIND, UCSF Chimera]

### Memory B cell repertoire from triple vaccinees against diverse SARS-CoV-2 variants. (Nature 2022)

- DOI: 10.1038/s41586-022-04466-x | PMCID: PMC8967717 | PMID: 35090164
- Evidence: The defocus value of each image was calculated by Gctf.
- Full pipeline: registration [RELION v3.0] -> simulation/modelling [GROMACS] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND]

### FOXP3 recognizes microsatellites and bridges DNA through multimerization. (Nature 2023)

- DOI: 10.1038/s41586-023-06793-z | PMCID: PMC10719092 | PMID: 38030726
- Version used: **4.1**
- Evidence: The contrast transfer function was estimated using CTFFIND (v.4.1) 46 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> registration [MotionCor2] -> differential/statistical testing [DESeq2] -> structure determination [RELION v4.0.1, UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [BEDTools, CTFFIND v4.1, HOMER, MACS2, PHENIX]

### Structures illustrate step-by-step mitochondrial transcription initiation. (Nature 2023)

- DOI: 10.1038/s41586-023-06643-y | PMCID: PMC10600007 | PMID: 37821701
- Evidence: 42 ) as implemented in the Relion 3.1 package 43 and the contrast transfer function parameters were estimated by CTFFIND-4 (ref.
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.19.2] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, RELION v3.1]

### TDP-43 forms amyloid filaments with a distinct fold in type A FTLD-TDP. (Nature 2023)

- DOI: 10.1038/s41586-023-06405-w | PMCID: PMC10447236 | PMID: 37532939
- Evidence: The motion-corrected micrographs were used to estimate the contrast transfer function using CTFFIND-4.1 (ref.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [CTFFIND, ChimeraX]

### Fanzor is a eukaryotic programmable RNA-guided endonuclease. (Nature 2023)

- DOI: 10.1038/s41586-023-06356-2 | PMCID: PMC10432273 | PMID: 37380027
- Version used: **1.18**
- Evidence: Contrast transfer function parameters for each non-dose-weighted micrograph were determined using Gctf 1.18 (ref.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> registration [MotionCor2] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.4, PHENIX v1.18] -> stage not stated [BLAST, CTFFIND v1.18, HMMER v3.3.2, PyMOL v1.2, RELION v4.0]

### Outer membrane utilisomes mediate glycan uptake in gut Bacteroidetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06146-w | PMCID: PMC7618045 | PMID: 37286596
- Evidence: CTF estimation of motion corrected micrographs was performed using Gctf 57 .
- Full pipeline: registration [CTFFIND] -> differential/statistical testing [limma] -> stage not stated [AlphaFold, CCP4, ChimeraX, PHENIX, R v4.1.1, RELION]

### Structural basis for bacterial energy extraction from atmospheric hydrogen. (Nature 2023)

- DOI: 10.1038/s41586-023-05781-7 | PMCID: PMC10017518 | PMID: 36890228
- Version used: **4.1.8**
- Evidence: Cryo-EM data processing and analysis Micrographs from all datasets were motion-corrected using UCSF Motioncor 1.0.4 and dose-weighted averages had their contrast transfer function (CTF) parameters estimated using CTFFIND 4.1.8, implemented using Relion 3.1.2 (ref.
- Full pipeline: simulation/modelling [GROMACS v2021.3] -> structure determination [ChimeraX v1.3, PHENIX] -> visualisation [AlphaFold, VMD] -> stage not stated [CTFFIND v4.1.8, Coot, RELION v3.1.2]

### MCM double hexamer loading visualized with human proteins. (Nature 2024)

- DOI: 10.1038/s41586-024-08263-6 | PMCID: PMC11634765 | PMID: 39604733
- Version used: **1.06**
- Evidence: Contrast transfer function (CTF) parameters were estimated using Gctf v1.06 49 .
- Full pipeline: differential/statistical testing [AlphaFold] -> structure determination [AlphaFold, Coot v0.9.8.1, PHENIX v1.21] -> stage not stated [CTFFIND v1.06, ChimeraX v1.6.1, RELION, Topaz v0.2.5]

### Nucleosome flipping drives kinetic proofreading and processivity by SWR1. (Nature 2024)

- DOI: 10.1038/s41586-024-08152-y | PMCID: PMC11618073 | PMID: 39506114
- Evidence: Contrast transfer function parameters were determined using Gctf 43 as previously described 12 .
- Full pipeline: alignment/mapping [MotionCor2, RELION] -> structure determination [PHENIX, RELION] -> stage not stated [AlphaFold, CTFFIND, Coot]

### LYCHOS is a human hybrid of a plant-like PIN transporter and a GPCR. (Nature 2024)

- DOI: 10.1038/s41586-024-08012-9 | PMCID: PMC11525196 | PMID: 39358511
- Version used: **4.1.8**
- Evidence: The contrast transfer function (CTF) parameters were estimated with CTFFIND (v.4.1.8) 34 or by patch-based CTF estimation.
- Full pipeline: dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX v1.20.1] -> visualisation [Matplotlib] -> stage not stated [AlphaFold, CTFFIND v4.1.8, ChimeraX, ImageJ v2.14.0, MotionCor2 v1.1.0]

### Heteromeric amyloid filaments of ANXA11 and TDP-43 in FTLD-TDP type C. (Nature 2024)

- DOI: 10.1038/s41586-024-08024-5 | PMCID: PMC11485244 | PMID: 39260416
- Evidence: The motion-corrected micrographs were used to estimate the contrast transfer function (CTF) using CTFFIND-4.1 (ref.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [CTFFIND, ChimeraX]

### Structure of a fully assembled γδ T cell antigen receptor. (Nature 2024)

- DOI: 10.1038/s41586-024-07920-0 | PMCID: PMC11485255 | PMID: 39146975
- Version used: **4.1.14**
- Evidence: Estimation of CTF parameters was made using the CTFFIND 4.1.14 software package 42 .
- Full pipeline: alignment/mapping [MotionCor2] -> differential/statistical testing [Coot v0.9.8.93] -> structure determination [Coot v0.9.8.93, PHENIX v1.21.1] -> visualisation [ChimeraX v1.8] -> stage not stated [CTFFIND v4.1.14, ImageJ v1.54, R v12.1, RELION v4.0]

### Structural basis for transthiolation intermediates in the ubiquitin pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07828-9 | PMCID: PMC11374688 | PMID: 39143218
- Evidence: Estimation of the contrast transfer function (CTF) was performed using Gctf 56 from non-dose weighted micrographs.
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> differential/statistical testing [Topaz] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [IMOD v4.11] -> stage not stated [CTFFIND, ChimeraX, RELION v3.1]

### Cryo-EM architecture of a near-native stretch-sensitive membrane microdomain. (Nature 2024)

- DOI: 10.1038/s41586-024-07720-6 | PMCID: PMC11324527 | PMID: 39048819
- Version used: **1.06**
- Evidence: For native-source eisosomes, movies were aligned using MotionCor2 59 , and CTF correction was completed using Gctf v.1.06 60 .
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> simulation/modelling [GROMACS v2021.5] -> structure determination [Coot v0.8.9.2, PHENIX v1.20] -> visualisation [ChimeraX v1.5] -> stage not stated [AlphaFold, Cellpose v2.0, RELION v2.1.0, VMD v1.9]

### CryoET of β-amyloid and tau within postmortem Alzheimer's disease brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07680-x | PMCID: PMC11269202 | PMID: 38987603
- Version used: **1.14**
- Evidence: 1c ) and contrast transfer function (CTF) parameters were estimated for each micrograph using CTFFIND v.1.14 61 .
- Full pipeline: alignment/mapping [IMOD v4.12.35] -> structure determination [Coot v0.8.9.2, PHENIX v1.17.1] -> machine learning [EMAN2 v2.99] -> stage not stated [CTFFIND v1.14, ChimeraX v1.5, Fiji, ImageJ, RELION v4.0]

### Molecular basis for transposase activation by a dedicated AAA+ ATPase. (Nature 2024)

- DOI: 10.1038/s41586-024-07550-6 | PMCID: PMC11208146 | PMID: 38926614
- Version used: **4.1**
- Evidence: 56 , 57 ) and the contrast transfer function (CTF) was estimated using CTFFIND (v.4.1) 58 .
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX v1.5] -> stage not stated [CCP4, CTFFIND v4.1, RELION, Topaz]

### High-resolution in situ structures of mammalian respiratory supercomplexes. (Nature 2024)

- DOI: 10.1038/s41586-024-07488-9 | PMCID: PMC11222160 | PMID: 38811722
- Evidence: The CTF of each motion-corrected micrograph was estimated using Gctf 61 or cryoSPARC 62 .
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX, IMOD] -> visualisation [ChimeraX, IMOD, PyMOL] -> stage not stated [CTFFIND, EMAN2, RELION]

### Structural insights into the cross-exon to cross-intron spliceosome switch. (Nature 2024)

- DOI: 10.1038/s41586-024-07458-1 | PMCID: PMC11208138 | PMID: 38778104
- Evidence: Defocus values were estimated using Gctf 31 .
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, RELION v3.1]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Evidence: Gctf was used to determine the contrast transfer function (CTF) parameters and perform correction steps 35 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### Streptomyces umbrella toxin particles block hyphal growth of competing species. (Nature 2024)

- DOI: 10.1038/s41586-024-07298-z | PMCID: PMC11062931 | PMID: 38632398
- Evidence: The parameters of the contrast transfer function (CTF) were estimated using CTFFIND 44 .
- Full pipeline: alignment/mapping [ColabFold] -> structure determination [Coot, Topaz] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, Python, RELION, RoseTTAFold, napari]

### Template and target-site recognition by human LINE-1 in retrotransposition. (Nature 2024)

- DOI: 10.1038/s41586-023-06933-5 | PMCID: PMC10830416 | PMID: 38096901
- Version used: **4.1**
- Evidence: Contrast transfer function (CTF) parameters for each micrograph were estimated using CTFFIND (v.4.1) 57 .
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [CTFFIND v4.1, ImageJ, MotionCor2, RELION v3.1.1]

### TAF15 amyloid filaments in frontotemporal lobar degeneration. (Nature 2024)

- DOI: 10.1038/s41586-023-06801-2 | PMCID: PMC10781619 | PMID: 38057661
- Evidence: Motion-corrected micrographs were used to estimate contrast transfer function (CTF) using CTFFIND-4.1 (ref.
- Full pipeline: alignment/mapping [RELION] -> registration [RELION] -> structure determination [RELION] -> stage not stated [CTFFIND, ChimeraX]

### Disease-specific tau filaments assemble via polymorphic intermediates. (Nature 2024)

- DOI: 10.1038/s41586-023-06788-w | PMCID: PMC10764278 | PMID: 38030728
- Evidence: Contrast transfer function (CTF) parameters were estimated using CTFFIND-4.1 (ref.
- Full pipeline: alignment/mapping [RELION] -> quantification [ImageJ] -> registration [RELION] -> visualisation [ImageJ] -> stage not stated [CTFFIND, ChimeraX]

### Helicase-mediated mechanism of SSU processome maturation and disassembly. (Nature 2025)

- DOI: 10.1038/s41586-025-09688-3 | PMCID: PMC12711562 | PMID: 41162712
- Evidence: Micrograph defocus was estimated using Gctf 34 .
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, ChimeraX, RELION]

### Structural basis for the dynamic regulation of mTORC1 by amino acids. (Nature 2025)

- DOI: 10.1038/s41586-025-09428-7 | PMCID: PMC12507694 | PMID: 40836086
- Version used: **4.1.14**
- Evidence: Contrast transfer function (CTF) parameters were determined using CTFFIND (v4.1.14) 42 .
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [AlphaFold, ChimeraX v1.8, Coot v0.9.8] -> machine learning [Topaz] -> stage not stated [CTFFIND v4.1.14, MotionCor2, PHENIX v2.0, RELION v5.0]

### Molecular mechanism of ultrafast transport by plasma membrane Ca&lt;sup&gt;2+&lt;/sup&gt;-ATPases. (Nature 2025)

- DOI: 10.1038/s41586-025-09402-3 | PMCID: PMC12488499 | PMID: 40836084
- Version used: **4.1.10**
- Evidence: Contrast transfer function estimation was also performed within TranSPHIRE using CTFFIND (v4.1.10) 72 .
- Full pipeline: structure determination [Coot, RELION v3.1, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1.10, ChimeraX, MotionCor2, PHENIX]

### BMAL1-HIF2A heterodimer modulates circadian variations of myocardial injury. (Nature 2025)

- DOI: 10.1038/s41586-025-08898-z | PMCID: PMC12095075 | PMID: 40269168
- Version used: **1.18**
- Evidence: Gctf (v.1.18) 79 was used to estimate the parameters of contrast transfer function (CTF) for each micrograph. crYOLO (v.1.10) 80 was used for reference-free automatic particle picking, yielding a total of approximately 710,000 particles.
- Full pipeline: quality control [Cutadapt v4.1, kallisto v0.46.1] -> read trimming [Cutadapt v4.1, kallisto v0.46.1] -> alignment/mapping [Cutadapt v4.1, MotionCor2 v1.4.0, STAR v2.7.10a, kallisto v0.46.1] -> quantification [Cutadapt v4.1, kallisto v0.46.1] -> differential/statistical testing [DESeq2, limma] -> structure determination [Coot v1.1, PHENIX v1.21] -> visualisation [ChimeraX v1.7, PyMOL v2.5.5] -> stage not stated [CTFFIND v1.18, Cytoscape v3.10.0, ImageJ, R, RELION v3.1, STRING db v11.5]

### Structural dynamics of DNA unwinding by a replicative helicase. (Nature 2025)

- DOI: 10.1038/s41586-025-08766-w | PMCID: PMC12043514 | PMID: 40108462
- Version used: **4.1**
- Evidence: 55 ) with dose-weighting, and contrast transfer function (CTF) estimation of the integrated micrographs was performed using CTFFIND 4.1 (ref.
- Full pipeline: structure determination [ChimeraX] -> visualisation [PHENIX, PyMOL v2.6.0, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1, MotionCor2, RELION, Topaz v0.3.0]

### Structural dynamics of human fatty acid synthase in the condensing cycle. (Nature 2025)

- DOI: 10.1038/s41586-025-08782-w | PMCID: PMC12058526 | PMID: 39978408
- Evidence: The contrast transfer function was estimated by CTFFIND-4.1 (ref.
- Full pipeline: registration [MotionCor2, RELION] -> structure determination [ChimeraX, PHENIX] -> machine learning [cryoDRGN] -> visualisation [UCSF Chimera] -> stage not stated [CTFFIND, Coot]

### Conformational protection of molybdenum nitrogenase by Shethna protein II. (Nature 2025)

- DOI: 10.1038/s41586-024-08355-3 | PMCID: PMC11754109 | PMID: 39779845
- Version used: **4.1**
- Evidence: 43 ) and per-micrograph defocus values were estimated using CTFFIND v.4.1 (ref.
- Full pipeline: structure determination [ChimeraX, PHENIX, RELION v3.1] -> visualisation [PyMOL] -> stage not stated [AlphaFold, CCP4, CTFFIND v4.1]

### Molecular basis for methylation-sensitive editing by Cas9. (Nature 2026)

- DOI: 10.1038/s41586-026-10384-z | PMCID: PMC13216068 | PMID: 41986708
- Evidence: Motion correction was executed in bin 2 via MotionCorr2 and contrast transfer function (CTF) estimation was carried out with Gctf 61 .
- Full pipeline: registration [CTFFIND] -> differential/statistical testing [Python, R] -> structure determination [PHENIX, RELION v4.0] -> stage not stated [Topaz]

### Structures of Marburgvirus glycoprotein and its complex with NPC1 receptor. (Nature 2026)

- DOI: 10.1038/s41586-026-10240-0 | PMCID: PMC13171430 | PMID: 41813895
- Version used: **4.1.13**
- Evidence: 41 ), and contrast transfer function parameters were estimated with CTFFIND (v4.1.13) 42 , with data downsampled to three-quarters resolution (0.885333 Å per pixel after downsampling).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX v1.16] -> visualisation [ChimeraX v0.93, PyMOL] -> stage not stated [CTFFIND v4.1.13, Coot v0.8.9]

### Integrase anchors viral RNA to the HIV-1 capsid interior. (Nature 2026)

- DOI: 10.1038/s41586-026-10154-x | PMCID: PMC13102720 | PMID: 41708858
- Evidence: 51 , 52 ), and contrast transfer function (CTF) parameters were estimated from frame sums using Gctf-v1.18 (ref.
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0, RELION] -> normalisation [ImageJ, NAMD v3.0.1] -> simulation/modelling [VMD] -> structure determination [ChimeraX, Coot, IMOD] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PyMOL, Topaz, UCSF Chimera]

### Cryo-EM structures of PI3Kα reveal conformational changes during inhibition and activation. (PNAS 2021)

- DOI: 10.1073/pnas.2109327118 | PMCID: PMC8609346 | PMID: 34725156
- Version used: **1.06**
- Evidence: Contrast transfer function parameters for each micrograph were determined by Gctf v1.06 ( 56 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX v1.2] -> stage not stated [CTFFIND v1.06, RELION]

### Constitutive signal bias mediated by the human GHRHR splice variant 1. (PNAS 2021)

- DOI: 10.1073/pnas.2106606118 | PMCID: PMC8501799 | PMID: 34599099
- Version used: **1.18**
- Evidence: Contrast transfer function (CTF) parameters were estimated by Gctf v1.18 ( 68 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v1.18, RELION]

### Architecture of cell-cell junctions in situ reveals a mechanism for bacterial biofilm inhibition. (PNAS 2021)

- DOI: 10.1073/pnas.2109940118 | PMCID: PMC8346871 | PMID: 34321357
- Evidence: CTF (contrast transfer function) parameters for the aligned stacks were estimated using CTFFIND ( 49 ), and data were reconstructed using Tomo3D ( 50 ).
- Full pipeline: alignment/mapping [CTFFIND, IMOD] -> structure determination [CTFFIND]

### Nanobody cocktails potently neutralize SARS-CoV-2 D614G N501Y variant and protect mice. (PNAS 2021)

- DOI: 10.1073/pnas.2101918118 | PMCID: PMC8126837 | PMID: 33893175
- Evidence: Movies from each of the imaging sessions were subjected to the correction of beam-induced motion using MotionCor2 ( 66 ), followed by contrast transfer function (CTF) estimation using Gctf ( 67 ).
- Full pipeline: dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, MotionCor2]

### Cryo-EM structure of <i>Mycobacterium smegmatis</i> DyP-loaded encapsulin. (PNAS 2021)

- DOI: 10.1073/pnas.2025658118 | PMCID: PMC8072242 | PMID: 33853951
- Version used: **1.06**
- Evidence: Next, the unweighted aligned micrographs were used for contrast transfer function (CTF) estimation using Gctf 1.06 ( 52 ).
- Full pipeline: alignment/mapping [CTFFIND v1.06, MotionCor2] -> dimensionality reduction/clustering [RELION] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [UCSF Chimera]

### Architecture of the mycobacterial succinate dehydrogenase with a membrane-embedded Rieske FeS cluster. (PNAS 2021)

- DOI: 10.1073/pnas.2022308118 | PMCID: PMC8054011 | PMID: 33876763
- Evidence: A total of 5,508 dose-fractionated image stacks were subjected to beam-induced motion correction using MotionCor2 ( 38 ) and the contrast transfer functions were estimated by Gctf ( 39 ).
- Full pipeline: registration [CTFFIND, MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL]

### Supramolecular assembly of the <i>Escherichia coli</i> LdcI upon acid stress. (PNAS 2021)

- DOI: 10.1073/pnas.2014383118 | PMCID: PMC7812809 | PMID: 33372137
- Evidence: After particle extraction, per-particle CTF correction was performed using Gctf ( 65 ).
- Full pipeline: registration [MotionCor2] -> dimensionality reduction/clustering [RELION v1.4] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, ImageJ]

### Human species D adenovirus hexon capsid protein mediates cell entry through a direct interaction with CD46. (PNAS 2021)

- DOI: 10.1073/pnas.2020732118 | PMCID: PMC7826407 | PMID: 33384338
- Evidence: Beam-induced motion was corrected using Relion’s MotionCor2 ( 66 ) implementation and the per-micrograph contrast transfer function (CTF) was estimated using Gctf ( 67 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [CCP4, CTFFIND, ChimeraX, EMAN2, MotionCor2, RELION v3.1]

### In situ structures of polymerase complex of mammalian reovirus illuminate RdRp activation and transcription regulation. (PNAS 2022)

- DOI: 10.1073/pnas.2203054119 | PMCID: PMC9897473 | PMID: 36469786
- Evidence: Frames from each movie were aligned to correct beam-induced drift, and contrast transfer function parameters were estimated using Gctf ( 58 ).
- Full pipeline: alignment/mapping [CTFFIND] -> structure determination [PHENIX, UCSF Chimera] -> stage not stated [RELION]

### Cryo-EM structures of cancer-specific helical and kinase domain mutations of PI3Kα. (PNAS 2022)

- DOI: 10.1073/pnas.2215621119 | PMCID: PMC9674216 | PMID: 36343266
- Version used: **1.06**
- Evidence: Contrast transfer function (CTF) parameters for each micrograph were determined by Gctf v1.06 ( 57 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX v1.18.2] -> visualisation [ChimeraX v1.0, PyMOL v2.1, UCSF Chimera v1.13.1] -> stage not stated [CTFFIND v1.06, RELION]

### Structural and functional investigation of ABC transporter STE6-2p from <i>Pichia pastoris</i> reveals unexpected interaction with sterol molecules. (PNAS 2022)

- DOI: 10.1073/pnas.2202822119 | PMCID: PMC9618074 | PMID: 36256814
- Evidence: Contrast transfer function (CTF) was estimated with Gctf estimation ( 57 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX] -> stage not stated [BLAST, CTFFIND, MotionCor2, RELION v3.1]

### Nanomolar inhibition of SARS-CoV-2 infection by an unmodified peptide targeting the prehairpin intermediate of the spike protein. (PNAS 2022)

- DOI: 10.1073/pnas.2210990119 | PMCID: PMC9546559 | PMID: 36122200
- Evidence: The data were processed using a combination of MotionCor2 ( 32 ), Gctf ( 33 ), EMAN2 ( 34 ), cryoSPARC ( 35 ), and RELION ( 36 ), as described previously ( 16 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, CellProfiler, EMAN2, MotionCor2, RELION, kallisto]

### Nanobodies and chemical cross-links advance the structural and functional analysis of PI3Kα. (PNAS 2022)

- DOI: 10.1073/pnas.2210769119 | PMCID: PMC9499577 | PMID: 36095215
- Version used: **1.06**
- Evidence: Contrast transfer function parameters for each micrograph were determined by Gctf v1.06 ( 55 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX v1.3] -> stage not stated [CTFFIND v1.06, RELION]

### Mechanism by which T7 bacteriophage protein Gp1.2 inhibits &lt;i&gt;Escherichia coli&lt;/i&gt; dGTPase. (PNAS 2022)

- DOI: 10.1073/pnas.2123092119 | PMCID: PMC9478638 | PMID: 36067314
- Evidence: Contrast transfer functions (CTFs) were estimated using CTFFIND-4.1 ( 41 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [Coot] -> machine learning [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, RELION]

### The neutralizing breadth of antibodies targeting diverse conserved epitopes between SARS-CoV and SARS-CoV-2. (PNAS 2022)

- DOI: 10.1073/pnas.2204256119 | PMCID: PMC9407403 | PMID: 35972965
- Evidence: Contrast transfer function fitting and phase-shift estimation were conducted with Gctf ( 51 ).
- Full pipeline: registration [MotionCor2] -> dimensionality reduction/clustering [R v3.6.3] -> structure determination [Coot] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PHENIX]

### Structure of a cholinergic cell membrane. (PNAS 2022)

- DOI: 10.1073/pnas.2207641119 | PMCID: PMC9407305 | PMID: 35969788
- Evidence: Local contrast transfer functions ( CTF s) were estimated from the aligned, nondose-weighted micrographs using Gctf ( 37 ).
- Full pipeline: alignment/mapping [CTFFIND] -> visualisation [PyMOL, UCSF Chimera] -> stage not stated [MotionCor2, RELION]

### Structural basis for high-voltage activation and subtype-specific inhibition of human Na&lt;sub&gt;v&lt;/sub&gt;1.8. (PNAS 2022)

- DOI: 10.1073/pnas.2208211119 | PMCID: PMC9335304 | PMID: 35858452
- Evidence: The defocus values were estimated using Gctf ( 51 ).
- Full pipeline: structure determination [PHENIX, RELION] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, Coot, MotionCor2]

### Cryo-EM structures of wild-type and E138K/M184I mutant HIV-1 RT/DNA complexed with inhibitors doravirine and rilpivirine. (PNAS 2022)

- DOI: 10.1073/pnas.2203660119 | PMCID: PMC9335299 | PMID: 35858448
- Evidence: Individual movie frames were motion-corrected and aligned using MotionCor2 ( 50 ) as implemented in the Relion 3.1 package ( 51 ) and the contrast transfer function (CTF) parameters were estimated by CTFFIND-4 ( 52 ).
- Full pipeline: alignment/mapping [CTFFIND, MotionCor2, RELION v3.1] -> structure determination [Coot, PHENIX v1.19] -> visualisation [PyMOL]

### Structural basis and molecular mechanism of biased GPBAR signaling in regulating NSCLC cell growth via YAP activity. (PNAS 2022)

- DOI: 10.1073/pnas.2117054119 | PMCID: PMC9303995 | PMID: 35858343
- Evidence: Contrast transfer function parameters were determined by Gctf ( 54 , 55 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [ANTs, CTFFIND]

### In situ architecture of the lipid transport protein VPS13C at ER-lysosome membrane contacts. (PNAS 2022)

- DOI: 10.1073/pnas.2203769119 | PMCID: PMC9303930 | PMID: 35858323
- Version used: **1.18**
- Evidence: For defocus-contrast micrographs, contrast transfer function correction was performed in Gctf (version 1.18, https://www2.mrc-lmb.cam.ac.uk/research/locally-developed-software/zhang-software , RRID:SCR_016500) ( 47 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0] -> structure determination [AlphaFold, ChimeraX, IMOD] -> visualisation [RELION, UCSF Chimera v1.13, seaborn v0.11.2] -> stage not stated [CTFFIND v1.18, EMAN2 v2.91]

### Structural basis of peptidomimetic agonism revealed by small- molecule GLP-1R agonists Boc5 and WB4-24. (PNAS 2022)

- DOI: 10.1073/pnas.2200155119 | PMCID: PMC9171782 | PMID: 35561211
- Version used: **1.06**
- Evidence: Contrast transfer function parameters for each micrograph were determined by Gctf v1.06 ( 33 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v1.06]

### Cryo-EM structure of RNA-induced tau fibrils reveals a small C-terminal core that may nucleate fibril formation. (PNAS 2022)

- DOI: 10.1073/pnas.2119952119 | PMCID: PMC9169762 | PMID: 35377792
- Version used: **4.1.8**
- Evidence: Motion correction and dose weighting was performed using Unblur and contrast transfer function estimation was performed using CTFFIND 4.1.8 ( 56 ).
- Full pipeline: registration [CTFFIND v4.1.8] -> structure determination [RELION] -> stage not stated [EMAN2, ImageJ]

### Structural conservation among variants of the SARS-CoV-2 spike postfusion bundle. (PNAS 2022)

- DOI: 10.1073/pnas.2119467119 | PMCID: PMC9169775 | PMID: 35363556
- Evidence: The CTF parameters of the summed micrographs were estimated using Gctf with equi-phase averaging ( 59 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [CTFFIND, ChimeraX, Coot, PyMOL, Python, RELION, UCSF Chimera]

### 50S subunit recognition and modification by the &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; ribosomal RNA methyltransferase TlyA. (PNAS 2022)

- DOI: 10.1073/pnas.2120352119 | PMCID: PMC9168844 | PMID: 35357969
- Evidence: The contrast transfer function was estimated using the program Gctf ( 53 ).
- Full pipeline: alignment/mapping [Clustal Omega, RELION] -> stage not stated [CTFFIND, Coot, PHENIX v1.19.2]

### Structural determinants of dual incretin receptor agonism by tirzepatide. (PNAS 2022)

- DOI: 10.1073/pnas.2116506119 | PMCID: PMC9060465 | PMID: 35333651
- Evidence: Contrast transfer function (CTF) parameters for each micrograph were determined by Gctf ( 47 ).
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND]

### FliL ring enhances the function of periplasmic flagella. (PNAS 2022)

- DOI: 10.1073/pnas.2117245119 | PMCID: PMC8931381 | PMID: 35254893
- Evidence: For the data collected without VPP, Gctf ( 73 ) was used to determine the defocus of each tilt image in the aligned stacks, and the “ctfphaseflip” function in IMOD was used for contrast transfer function correction for the tilt images.
- Full pipeline: alignment/mapping [CTFFIND, IMOD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold]

### Rearrangement of a unique Kv1.3 selectivity filter conformation upon binding of a drug. (PNAS 2022)

- DOI: 10.1073/pnas.2113536119 | PMCID: PMC8812516 | PMID: 35091471
- Evidence: Contrast transfer function (CTF) parameters were estimated with Gctf ( 37 ) using nondose-weighted micrographs.
- Full pipeline: alignment/mapping [MotionCor2] -> registration [MotionCor2] -> simulation/modelling [UCSF Chimera, VMD] -> structure determination [PHENIX] -> stage not stated [CTFFIND, NAMD, RELION]

### Annealing synchronizes the 70<i>S</i> ribosome into a minimum-energy conformation. (PNAS 2022)

- DOI: 10.1073/pnas.2111231119 | PMCID: PMC8872765 | PMID: 35177473
- Evidence: The contrast transfer function (CTF) parameters of the summed micrographs were determined with CTFFIND-4 ( 59 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX v1.17.1, RELION v3.0.8] -> stage not stated [CTFFIND, Python, UCSF Chimera v1.16]

### Structures of the peptidase-containing ABC transporter PCAT1 under equilibrium and nonequilibrium conditions. (PNAS 2022)

- DOI: 10.1073/pnas.2120534119 | PMCID: PMC8794836 | PMID: 35074919
- Evidence: Subframe alignment was carried out using MotionCorr2, and the contrast transfer function (CTF) was estimated using Gctf software ( 24 ).
- Full pipeline: alignment/mapping [CTFFIND] -> dimensionality reduction/clustering [RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [Coot, PHENIX]

### Structural basis of substrate progression through the bacterial chaperonin cycle. (PNAS 2023)

- DOI: 10.1073/pnas.2308933120 | PMCID: PMC10723157 | PMID: 38064510
- Evidence: The CTF parameters of motion-corrected micrographs were estimated using Gctf ( 47 ).
- Full pipeline: stage not stated [CTFFIND, Python, RELION v3.1]

### Structures of the &lt;i&gt;P. aeruginosa&lt;/i&gt; FleQ-FleN master regulators reveal large-scale conformational switching in motility and biofilm control. (PNAS 2023)

- DOI: 10.1073/pnas.2312276120 | PMCID: PMC10723142 | PMID: 38051770
- Evidence: The movies were motion- and CTF-corrected using MotionCor2 ( 38 ) and Gctf ( 39 ), respectively, after which all micrograph processing was continued in cryoSPARC v3 and v4 ( 40 ).
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, MotionCor2]

### Structure determination by cryoEM at 100 keV. (PNAS 2023)

- DOI: 10.1073/pnas.2312905120 | PMCID: PMC10710074 | PMID: 38011573
- Evidence: The micrographs were motion corrected using MotionCorr2 ( 30 ) and their CTFs were estimated using CTFFIND-4.1 ( 10 ).
- Full pipeline: registration [CTFFIND, RELION v4.0]

### Synaptophysin chaperones the assembly of 12 SNAREpins under each ready-release vesicle. (PNAS 2023)

- DOI: 10.1073/pnas.2311484120 | PMCID: PMC10636311 | PMID: 37903271
- Evidence: The contrast transfer function was calculated with CTFFIND-4.1 ( 73 ).
- Full pipeline: stage not stated [CTFFIND, ImageJ, MotionCor2, RELION v3.1]

### Identification of a carbonic anhydrase-Rubisco complex within the alpha-carboxysome. (PNAS 2023)

- DOI: 10.1073/pnas.2308600120 | PMCID: PMC10614612 | PMID: 37862384
- Version used: **4.1**
- Evidence: CTF estimation was performed using CTFFIND 4.1 ( 62 ) from within RELION 3.1.
- Full pipeline: alignment/mapping [MUSCLE, RELION v3.1] -> quantification [ImageJ] -> registration [RELION v3.1] -> structure determination [PHENIX] -> visualisation [ChimeraX, IQ-TREE, PyMOL] -> stage not stated [CTFFIND v4.1]

### Molecular basis of signal transduction mediated by the human GIPR splice variants. (PNAS 2023)

- DOI: 10.1073/pnas.2306145120 | PMCID: PMC10576055 | PMID: 37792509
- Version used: **1.06**
- Evidence: Contrast transfer function parameters for each micrograph were determined by Gctf v1.06 ( 61 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2021.4] -> structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX v1.2.4] -> stage not stated [CTFFIND v1.06, ImageJ, RELION]

### Structural insights into the interaction of three Y-shaped ligands with PI3Kα. (PNAS 2023)

- DOI: 10.1073/pnas.2304071120 | PMCID: PMC10450665 | PMID: 37585458
- Version used: **1.06**
- Evidence: Contrast transfer function (CTF) parameters for each micrograph were determined by Gctf v1.06 ( 43 ).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [GROMACS v2020.1] -> structure determination [Coot v0.9.4.1] -> visualisation [ChimeraX v1.0, PyMOL v2.1, UCSF Chimera v1.13.1] -> stage not stated [CTFFIND v1.06, PHENIX v1.18.2, RELION]

### Two conformations of the Tom20 preprotein receptor in the TOM holo complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301447120 | PMCID: PMC10450662 | PMID: 37579144
- Evidence: Movies were motion-corrected using MotionCor2 ( 49 ), and CTF parameters were initially estimated using CTFFIND-4 ( 50 ), both as implemented in Relion.
- Full pipeline: structure determination [AlphaFold, PHENIX] -> stage not stated [CTFFIND, ChimeraX, MotionCor2, RELION]

### An expandable, modular de novo protein platform for precision redox engineering. (PNAS 2023)

- DOI: 10.1073/pnas.2306046120 | PMCID: PMC10400981 | PMID: 37487099
- Evidence: The dose-fractionated movies were gain normalized, aligned, and dose-weighted using MotionCor2 ( 71 ) and contrast transfer function (CTF) information determined and corrected using Gctf find4.1 ( 72 ).
- Full pipeline: alignment/mapping [CTFFIND, MotionCor2] -> normalisation [CTFFIND, MotionCor2] -> dimensionality reduction/clustering [RELION v3.1]

### Efficient tagging of endogenous proteins in human cell lines for structural studies by single-particle cryo-EM. (PNAS 2023)

- DOI: 10.1073/pnas.2302471120 | PMCID: PMC10401002 | PMID: 37487103
- Evidence: CTF was estimated by CTFFIND-4.1 ( 74 ).
- Full pipeline: structure determination [PHENIX] -> machine learning [Cellpose] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [CTFFIND, Coot, ImageJ, MotionCor2, RELION, Topaz]

### Structures and membrane interactions of native serotonin transporter in complexes with psychostimulants. (PNAS 2023)

- DOI: 10.1073/pnas.2304602120 | PMCID: PMC10629533 | PMID: 37436958
- Evidence: The defocus values were estimated by Gctf ( 81 ) and particles were picked by blob-picker in cryoSPARC ( 82 ).
- Full pipeline: alignment/mapping [RELION] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [CTFFIND, MotionCor2, VMD]

### 30S subunit recognition and G1405 modification by the aminoglycoside-resistance 16S ribosomal RNA methyltransferase RmtC. (PNAS 2023)

- DOI: 10.1073/pnas.2304128120 | PMCID: PMC10288597 | PMID: 37307464
- Evidence: Motion correction and dose weighing was conducted with MotionCorr2 ( 38 ), and contrast transfer function parameters estimated by Gctf ( 39 ).
- Full pipeline: registration [CTFFIND] -> structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, RELION v3.1, UCSF Chimera]

### Structural insights into the assembly of the agrin/LRP4/MuSK signaling complex. (PNAS 2023)

- DOI: 10.1073/pnas.2300453120 | PMCID: PMC10266037 | PMID: 37252960
- Evidence: The CTF parameters were estimated using Gctf ( 28 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, RELION]

### Structure of the priming arabinosyltransferase AftA required for AG biosynthesis of <i>Mycobacterium tuberculosis</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302858120 | PMCID: PMC10265970 | PMID: 37252995
- Evidence: All dose-fractioned images were motion-corrected and dose-weighted by MotionCorr2 software ( 44 ) and their contrast transfer functions were estimated by Gctf (resolution range: 4 to 25 Å; search defocus: 0.1 to 4 μm).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX v1.12] -> stage not stated [CTFFIND, ChimeraX, Docker, PyMOL, RDKit, UCSF Chimera]

### Structure-based design of a SARS-CoV-2 Omicron-specific inhibitor. (PNAS 2023)

- DOI: 10.1073/pnas.2300360120 | PMCID: PMC10068829 | PMID: 36940324
- Evidence: The data were processed using a combination of MotionCor2 ( 24 ), Gctf ( 25 ), EMAN2 ( 26 ), cryoSPARC ( 27 ), and RELION ( 28 ), as described previously ( 14 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, MotionCor2, PyMOL, RELION, UCSF Chimera]

### In situ snapshots along a mammalian selective autophagy pathway. (PNAS 2023)

- DOI: 10.1073/pnas.2221712120 | PMCID: PMC10041112 | PMID: 36917659
- Evidence: Tilt series were preprocessed with TOMOMAN software ( https://github.com/williamnwan/TOMOMAN ), performing beam-induced motion correction with MotionCor2 ( 47 ), tilt-series sorting, and contrast transfer function estimation with CTFFIND ( 48 ).
- Full pipeline: alignment/mapping [IMOD v4.10.49] -> registration [CTFFIND, MotionCor2] -> structure determination [IMOD v4.10.49] -> machine learning [EMAN2] -> visualisation [ChimeraX]

### Differential dynamics and direct interaction of bound ligands with lipids in multidrug transporter ABCG2. (PNAS 2023)

- DOI: 10.1073/pnas.2213437120 | PMCID: PMC9910490 | PMID: 36580587
- Evidence: Gctf was used to measure the contrast transfer function (CTF) parameters ( 46 ).
- Full pipeline: simulation/modelling [NAMD] -> stage not stated [CTFFIND, Coot v0.9, MotionCor2, PHENIX, VMD]

### SUMO enhances unfolding of SUMO-polyubiquitin-modified substrates by the Ufd1/Npl4/Cdc48 complex. (PNAS 2023)

- DOI: 10.1073/pnas.2213703120 | PMCID: PMC9910466 | PMID: 36574706
- Evidence: Estimation of the contrast transfer function (CTF) was performed using Gctf ( 59 ).
- Full pipeline: structure determination [PHENIX, Python] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, Coot, MotionCor2, RELION v3.0]

### Architecture of the Sap S-layer of &lt;i&gt;Bacillus anthracis&lt;/i&gt; revealed by integrative structural biology. (PNAS 2024)

- DOI: 10.1073/pnas.2415351121 | PMCID: PMC11665858 | PMID: 39652757
- Evidence: Initial CTF correction was done using defocus estimation by Gctf ( 41 ) and ctfphaseflip from IMOD ( 42 ).
- Full pipeline: alignment/mapping [VMD] -> registration [MotionCor2] -> simulation/modelling [VMD] -> structure determination [RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, GROMACS, IMOD]

### Molecular architecture of synaptic vesicles. (PNAS 2024)

- DOI: 10.1073/pnas.2407375121 | PMCID: PMC11626200 | PMID: 39602275
- Evidence: For each projection, the defocus values were measured by Gctf ( 82 ), and CTF correction was performed using ctfphaseflip ( 82 ) from IMOD.
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> structure determination [IMOD] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, RELION]

### Structural duality enables a single protein to act as a toxin-antidote pair for meiotic drive. (PNAS 2024)

- DOI: 10.1073/pnas.2408618121 | PMCID: PMC11551426 | PMID: 39485800
- Evidence: CTF parameters were estimated with Gctf ( 71 ).
- Full pipeline: alignment/mapping [minimap2] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2]

### Cryo-EM structure of the zinc-activated channel (ZAC) in the Cys-loop receptor superfamily. (PNAS 2024)

- DOI: 10.1073/pnas.2405659121 | PMCID: PMC11536092 | PMID: 39441630
- Version used: **4.1**
- Evidence: Contrast transfer function (CTF) parameters were estimated by CTFFIND 4.1 ( 57 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [ImageJ] -> registration [RELION] -> structure determination [PHENIX] -> stage not stated [CTFFIND v4.1, ChimeraX, PyMOL, UCSF Chimera]

### Binding adaptability of chemical ligands to polymorphic α-synuclein amyloid fibrils. (PNAS 2024)

- DOI: 10.1073/pnas.2321633121 | PMCID: PMC11363296 | PMID: 39172784
- Evidence: The contrast transfer function of each micrograph was estimated using CTFFIND-4.1.8 ( 62 ).
- Full pipeline: structure determination [ChimeraX, PHENIX v1.13, PyMOL v1.7.4.5, UCSF Chimera v1.13.1] -> visualisation [ChimeraX, PyMOL v1.7.4.5] -> stage not stated [CTFFIND, RELION v3.1]

### Structural basis for DNA recognition by a viral genome-packaging machine. (PNAS 2024)

- DOI: 10.1073/pnas.2406138121 | PMCID: PMC11331095 | PMID: 39116131
- Evidence: After estimation of contrast transfer function (CTF) parameters with CTFFIND-4.1 ( 43 ) micrographs were manually sorted to eliminate empty and icy ones.
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, Coot, RELION v3.1.2, Topaz]

### Influence of lipid bilayer on the structure of the muscle-type nicotinic acetylcholine receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2319913121 | PMCID: PMC11087746 | PMID: 38683987
- Evidence: Local contrast transfer functions were estimated from the aligned, non-dose-weighted micrographs using Gctf ( 30 ).
- Full pipeline: alignment/mapping [CTFFIND, PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, MotionCor2, RELION]

### C-type inactivation and proton modulation mechanisms of the TASK3 channel. (PNAS 2024)

- DOI: 10.1073/pnas.2320345121 | PMCID: PMC11046659 | PMID: 38630723
- Evidence: The contrast transfer function (CTF) parameters for each micrograph were estimated using Gctf ( 53 ).
- Full pipeline: registration [MotionCor2, RELION] -> simulation/modelling [GROMACS v5.1.4] -> structure determination [PHENIX] -> stage not stated [CTFFIND, ChimeraX, PyMOL]

### Structural and mechanistic basis of the central energy-converting methyltransferase complex of methanogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2315568121 | PMCID: PMC10998594 | PMID: 38530900
- Evidence: Initial contrast transfer function parameters for each movie were estimated using Gctf algorithms ( 55 ).
- Full pipeline: alignment/mapping [AlphaFold] -> stage not stated [CTFFIND, PHENIX, RELION]

### Human paraneoplastic antigen Ma2 (PNMA2) forms icosahedral capsids that can be engineered for mRNA delivery. (PNAS 2024)

- DOI: 10.1073/pnas.2307812120 | PMCID: PMC10945824 | PMID: 38437549
- Evidence: Movies were corrected for motion using the RELION implementation of MotionCor2, with 4 × 4 patches and dose-weighting, and CTF parameters were estimated using CTFFIND-4.1 ( 51 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, PyMOL, RELION v4.0, Topaz]

### Structure of mavacamten-free human cardiac thick filaments within the sarcomere by cryoelectron tomography. (PNAS 2024)

- DOI: 10.1073/pnas.2311883121 | PMCID: PMC10907299 | PMID: 38386705
- Evidence: Contrast Transfer Function correction used Gctf ( 86 ).
- Full pipeline: alignment/mapping [EMAN2, IMOD] -> registration [MotionCor2] -> structure determination [EMAN2, IMOD] -> stage not stated [CTFFIND]

### Dissection of the structure-function relationship of Na<sub>v</sub> channels. (PNAS 2024)

- DOI: 10.1073/pnas.2322899121 | PMCID: PMC10907234 | PMID: 38381792
- Evidence: Defocus values were estimated using Gctf ( 44 ) or cryoSPARC ( 45 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND, MotionCor2]

### Puromycin reveals a distinct conformation of neuronal ribosomes. (PNAS 2024)

- DOI: 10.1073/pnas.2306993121 | PMCID: PMC10873636 | PMID: 38315848
- Evidence: CTF parameter estimation was done using CTFFIND-4.1 program ( 48 ) using the dose-weighted averages with a 30 to 5.0 Å resolution range and 512-pixel FFT box size.
- Full pipeline: visualisation [ChimeraX, UCSF Chimera] -> stage not stated [CTFFIND, ImageJ, MotionCor2, RELION]

### Structural basis of modified ligand selectivity from N-terminal PAC1R alternative splicing. (PNAS 2025)

- DOI: 10.1073/pnas.2521157122 | PMCID: PMC12663942 | PMID: 41264251
- Evidence: In short, motion correction ( 38 ) and CTF estimation with CTFFIND-4.1 ( 39 ) were used through RELION 3.1.2 or RELION 5.0 ( 40 , 41 ). crYOLO ( 42 ) picked particles were imported to cryoSPARC (version 3.3.2 or version 4.6.0 for PAC1sR-P27-G s data) for 2D classification, ab-initio reconstruction as well as nonuniform refinement ( 43 ).
- Full pipeline: registration [CTFFIND, RELION v3.1.2] -> structure determination [CTFFIND, RELION v3.1.2] -> stage not stated [ChimeraX, VMD]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Evidence: Contrast transfer function parameter estimation was performed with CTFFIND-4.1 ( 62 ).
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### Structural insights into the dynamic mechanism of bornavirus polymerase. (PNAS 2025)

- DOI: 10.1073/pnas.2504779122 | PMCID: PMC12501175 | PMID: 40996804
- Evidence: Briefly, dose-fractionated movies were subjected to Patch motion correction using MotionCor2 ( 55 ) and Patch CTF estimation using CTFFIND-4.1.13 ( 56 ).
- Full pipeline: registration [CTFFIND, MotionCor2] -> structure determination [PHENIX] -> visualisation [ChimeraX v1.7, UCSF Chimera]

### In situ structures of the &lt;i&gt;Legionella&lt;/i&gt; Dot/Icm T4SS identify the DotA-IcmX complex as the gatekeeper for effector translocation. (PNAS 2025)

- DOI: 10.1073/pnas.2516300122 | PMCID: PMC12501162 | PMID: 40986344
- Evidence: After CTF estimation (Gctf) ( 63 ) and phase flipping (IMOD ctfphaseflip), Tomo3D ( 64 ) was used to generate tomograms either simultaneous iterative reconstruction technique (SIRT) or weighted backprojection (WBP).
- Full pipeline: alignment/mapping [PHENIX v1.21] -> structure determination [CTFFIND, ChimeraX, PHENIX v1.21] -> stage not stated [AlphaFold, Coot v0.8.9.1, IMOD, RELION v3.1]

### Critical role of extracellular loops in differential modulations of TTX-sensitive and TTX-resistant Na&lt;sub&gt;v&lt;/sub&gt; channels. (PNAS 2025)

- DOI: 10.1073/pnas.2510355122 | PMCID: PMC12358880 | PMID: 40768348
- Evidence: The defocus values were estimated with Gctf ( 54 ).
- Full pipeline: registration [MotionCor2] -> structure determination [PHENIX] -> stage not stated [CTFFIND, PyMOL, RELION]

### Structural basis of auxin binding and transport by <i>Arabidopsis thaliana</i> AUX1. (PNAS 2025)

- DOI: 10.1073/pnas.2513424122 | PMCID: PMC12337342 | PMID: 40720658
- Evidence: Dose weighting was simultaneously applied, and the defocus value was calculated with Gctf (Zhang, 2016).
- Full pipeline: registration [MotionCor2] -> simulation/modelling [OpenMM, VMD] -> structure determination [PHENIX] -> machine learning [OpenMM] -> visualisation [VMD] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, Coot]

### Arrestin recognizes GPCRs independently of the receptor state. (PNAS 2025)

- DOI: 10.1073/pnas.2501487122 | PMCID: PMC12107136 | PMID: 40372433
- Version used: **4.1.14**
- Evidence: CTF estimation was conducted using CTFFIND 4.1.14 ( 44 ), with selection criteria based on a maximum CTF resolution of better than 6 Å and defocus between 0.5 to 2.5 µm.
- Full pipeline: quantification [ImageJ] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND v4.1.14, RELION v4.0]

### Subunit specialization in AAA+ proteins and substrate unfolding during transcription complex remodeling. (PNAS 2025)

- DOI: 10.1073/pnas.2425868122 | PMCID: PMC12054792 | PMID: 40273105
- Evidence: Contrast transfer function estimation was carried out with CTFFIND 4 ( 28 ).
- Full pipeline: stage not stated [CTFFIND, RELION v4.0, Topaz]

### FlgY, PflA, and PflB form a spoke-ring network in the high-torque flagellar motor of &lt;i&gt;Helicobacter pylori&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2421632122 | PMCID: PMC12054838 | PMID: 40261933
- Evidence: Gctf ( 57 ) was used to estimate defocus, and the “ctfphaseflip” function in IMOD was used to correct the contrast transfer function (CTF) ( 58 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [ChimeraX] -> stage not stated [AlphaFold, CTFFIND]

### Reducing the effects of radiation damage in cryo-EM using liquid helium temperatures. (PNAS 2025)

- DOI: 10.1073/pnas.2421538122 | PMCID: PMC12054821 | PMID: 40261934
- Evidence: CTF estimation was performed with CTFFIND-4.1.13 ( 43 ).
- Full pipeline: alignment/mapping [Python] -> registration [MotionCor2, RELION v4.0] -> stage not stated [CTFFIND]

### Structural basis of the cysteinyl leukotriene receptor type 2 activation by LTD4. (PNAS 2025)

- DOI: 10.1073/pnas.2417148122 | PMCID: PMC12012480 | PMID: 40193607
- Version used: **4.0**
- Evidence: MotionCor2 was used to perform the frame-based motion-correction algorithm to generate drift-corrected micrograph for further processing and defocus parameters were estimated by CTFFIND 4.0 ( 41 , 42 ).
- Full pipeline: visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v4.0, MotionCor2, PHENIX, R v3.50, UCSF Chimera]

### Biochemical and structural bases for talin ABSs-F-actin interactions. (PNAS 2025)

- DOI: 10.1073/pnas.2405922122 | PMCID: PMC11831117 | PMID: 39903122
- Version used: **4.1**
- Evidence: Motion correction and binning to a working pixel size of 0.83Å/pixel was carried out by MotionCor2 ( 52 ), defocus values were measured by CTFFIND 4.1 ( 53 ) and subsequent image analysis was carried out using RELION 3.1 ( 54 ).
- Full pipeline: registration [CTFFIND v4.1, MotionCor2, RELION v3.1] -> structure determination [PHENIX]

### Structural insights into the role of reduced cysteine residues in SOD1 amyloid filament formation. (PNAS 2025)

- DOI: 10.1073/pnas.2408582122 | PMCID: PMC11804504 | PMID: 39874287
- Evidence: Movie frames were dose-weighted using the MotionCor2 algorithm ( 54 ), and the contrast transfer function was estimated using CTFFIND-4.1 ( 55 ).
- Full pipeline: structure determination [PHENIX v1.21] -> visualisation [ChimeraX v1.4, PyMOL v3.0] -> stage not stated [CTFFIND, ImageJ, MotionCor2, RELION]

### Molecular mechanism of ligand recognition and activation of lysophosphatidic acid receptor LPAR6. (PNAS 2025)

- DOI: 10.1073/pnas.2415426122 | PMCID: PMC11789011 | PMID: 39847322
- Version used: **4.1**
- Evidence: The CTF (Contrast Transfer Function) parameters were determined using CTFFIND 4.1 ( 36 ).
- Full pipeline: alignment/mapping [AlphaFold] -> dimensionality reduction/clustering [RELION] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [CTFFIND v4.1, MotionCor2, R v3.50]

### Structural determinants of oxygen resistance and Zn&lt;sup&gt;2+&lt;/sup&gt;-mediated stability of the [FeFe]-hydrogenase from &lt;i&gt;Clostridium beijerinckii&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2416233122 | PMCID: PMC11760498 | PMID: 39805018
- Evidence: The movie frames were subjected to beam-induced movement correction using MotionCor2.1 and contrast transfer function (CTF) was evaluated using Gctf ( 46 , 47 ).
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, MotionCor2, RELION]

### Tetrameric PilZ protein stabilizes stator ring in complex flagellar motor and is required for motility in &lt;i&gt;Campylobacter jejuni&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2412594121 | PMCID: PMC11725899 | PMID: 39793078
- Evidence: Defocus for all images in the aligned tilt series was estimated using Gctf ( 69 ), and contrast transfer function (CTF) was corrected using the ctfphaseflip function in IMOD ( 70 ).
- Full pipeline: alignment/mapping [CTFFIND, IMOD] -> structure determination [ChimeraX] -> stage not stated [AlphaFold, ColabFold, MotionCor2]

### Structural insight into sodium ion pathway in the bacterial flagellar stator from marine &lt;i&gt;Vibrio&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2415713122 | PMCID: PMC11725901 | PMID: 39793043
- Version used: **4.1**
- Evidence: All micrographs were motion-corrected using MOTIONCORR2 (version 1.3.0) with dose fraction ( 47 ), and CTF values were estimated with CTFFIND 4.1 (version 1.10) ( 48 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CTFFIND v4.1, ChimeraX, RELION]

### RNA-activated protein cleavage with a CRISPR-associated endopeptidase. (Science 2022)

- DOI: 10.1126/science.add7450 | PMCID: PMC10028731 | PMID: 36423276
- Evidence: Movies were corrected for motion using the RELION implementation of MotionCor2, with 5-by-5 patches and dose-weighting, and Contrast Transfer Function (CTF) parameters were estimated using CTFFIND-4.1 ( 38 ).
- Full pipeline: alignment/mapping [PyMOL] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CTFFIND, Coot, Jupyter, MotionCor2, RELION]

### DNSN-1 recruits GINS for CMG helicase assembly during DNA replication initiation in &lt;i&gt;Caenorhabditis elegans&lt;/i&gt;. (Science 2023)

- DOI: 10.1126/science.adi4932 | PMCID: PMC7615117 | PMID: 37590372
- Evidence: CTF parameters were estimated using CTFFIND-4.1 ( 63 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [CTFFIND, ImageJ, RELION]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: CTF parameters were estimated using CTFFIND-4.1 ( 59 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

### Cryo-EM structure of human telomerase dimer reveals H/ACA RNP-mediated dimerization. (Science 2025)

- DOI: 10.1126/science.adr5817 | PMCID: PMC7618144 | PMID: 40638752
- Evidence: CTF parameters were estimated for the motion-corrected micrographs using CTFFIND-4.1 ( 56 ).
- Full pipeline: alignment/mapping [minimap2] -> machine learning [Topaz] -> stage not stated [CTFFIND, ChimeraX, ImageJ, PHENIX v1.20, RELION v5.0, UCSF Chimera]

### TIGR-Tas: A family of modular RNA-guided DNA-targeting systems in prokaryotes and their viruses. (Science 2025)

- DOI: 10.1126/science.adv9789 | PMCID: PMC12045711 | PMID: 40014690
- Evidence: CTF parameters were estimated using CTFFIND-4.1 ( 99 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, MAFFT, PyMOL] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [MAFFT, PHENIX] -> stage not stated [CTFFIND, ColabFold, Coot, HMMER, MotionCor2, RELION, Topaz]

### Structural mechanism of LINE-1 target-primed reverse transcription. (Science 2025)

- DOI: 10.1126/science.ads8412 | PMCID: PMC7617806 | PMID: 40048554
- Evidence: CTF parameters were estimated using CTFFIND-4.1 ( 87 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, PHENIX v1.21.1, RELION] -> stage not stated [CTFFIND, ChimeraX, ImageJ, MotionCor2, PyMOL, Python, REFMAC, Topaz]

### Evolutionary adaptations of doublet microtubules in trypanosomatid parasites. (Science 2025)

- DOI: 10.1126/science.adr5507 | PMCID: PMC7617938 | PMID: 40080577
- Version used: **4.0**
- Evidence: Contrast transfer function (CTF) parameters were estimated using CTFFIND 4.0 ( 46 ).
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [napari] -> stage not stated [AlphaFold, CTFFIND v4.0, ChimeraX, HMMER, ImageJ, RELION]

### Molecular basis of FIGNL1 in dissociating RAD51 from DNA and chromatin. (Science 2025)

- DOI: 10.1126/science.adr7920 | PMCID: PMC7617353 | PMID: 39636933
- Evidence: Image processing of FIGNL1ΔN-RAD51 complex Motion corrected movies (using MOTIONCOR2( 63 )) were also CTF corrected (using Patch CTF estimation) in cryoSPARC as well as in RELION (using CTFFIND-4.1( 64 )).
- Full pipeline: registration [CTFFIND] -> structure determination [AlphaFold, PHENIX] -> visualisation [Fiji, ImageJ, RELION] -> stage not stated [Coot, Topaz]

### Cryo-electron microscopy structure of the budding yeast telomerase holoenzyme. (Science 2026)

- DOI: 10.1126/science.adz5344 | PMCID: PMC7619062 | PMID: 41886584
- Version used: **4.1**
- Evidence: Contrast transfer function (CTF) parameters were estimated using CTFFIND 4.1 within RELION ( 94 ).
- Full pipeline: quantification [ImageJ] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, CTFFIND v4.1, Python, RELION v5.0, Topaz]

