# EMAN2

- **Category:** structbio
- **Papers in survey:** 46
- **Journals:** PNAS (30), Nature (11), Cell (4), Science (1)
- **Years:** 2021 (6), 2022 (17), 2023 (6), 2024 (11), 2025 (5), 2026 (1)
- **Versions named:** 2.91 (2), 2.99 (1), 2.31 (1)
- **Pipeline stages it appears in:** machine learning (8), structure determination (6), alignment/mapping (4), visualisation (3), simulation/modelling (1)

## Papers

### The molecular basis for sarcomere organization in vertebrate skeletal muscle. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.047 | PMCID: PMC8054911 | PMID: 33765442
- Evidence: ...e and algorithms SerialEM Mastronarde, 2005 https://bio3d.colorado.edu/SerialEM/ MotionCorr2 Zheng et al., 2017 https://emcore.ucsf.edu/ucsf-software EMAN2 Tang et al., 2007 https://blake.bcm.edu/emanwiki/EMAN2 IMOD Kremer et al., 1996 https://bio3d.colorado.edu/imod/ crYOLO Wagner et al., 2019 https://cryolo.readthedocs.io RELION3 Bharat and Scheres, 2016 https://www3.mrc-lmb.cam.ac.uk/relion/ind...
- Full pipeline: visualisation [R] -> stage not stated [EMAN2, Fiji, IMOD, ImageJ, RELION, TrackMate]

### Cryo-ET of Env on intact HIV virions reveals structural variation and positioning on the Gag lattice. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.013 | PMCID: PMC9000915 | PMID: 35123651
- Evidence: ...2016 ; Scheres, 2012 ) https://www3.mrc-lmb.cam.ac.uk/relion/index.php/Main_Page PEET 1.12 ( Nicastro et al., 2006 ) https://bio3d.colorado.edu/PEET/ EMAN2 ( Chen et al., 2019 ) https://blake.bcm.edu/emanwiki/EMAN2/e2tomo COOT MRC https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot UCSF Chimera UCSF https://www.cgl.ucsf.edu/chimera/ UCSF ChimeraX UCSF https://www.rbvi.ucsf.edu/chimerax/ ImageJ ( ...
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ChimeraX, Coot, EMAN2, IMOD v4.10.15, ImageJ, RELION v2.1, UCSF Chimera]

### Comprehensive structure and functional adaptations of the yeast nuclear pore complex. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.015 | PMCID: PMC8928745 | PMID: 34982960
- Evidence: After parameter optimization, NPCs were picked with Gautomatch ( https://www.mrc-lmb.cam.ac.uk/kzhang/ ) using an image stack of equi-spaced projection views that were calculated from our tomographic model with C8 symmetry (( Kim et al., 2018 ); EMD-7321) using EMAN2 ( e2project3d.py ( Tang et al., 2007 )).
- Full pipeline: registration [IMOD] -> simulation/modelling [PHENIX] -> structure determination [PHENIX] -> stage not stated [Coot, EMAN2, ImageJ, RELION v2.0]

### The molecular architecture of the nuclear basket. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.020 | PMCID: PMC11416316 | PMID: 39127037
- Evidence: 96 , 111 Local resolution maps were calculated in EMAN2.
- Full pipeline: stage not stated [ChimeraX, EMAN2, IMOD, RELION]

### Functional refolding of the penetration protein on a non-enveloped virus. (Nature 2021)

- DOI: 10.1038/s41586-020-03124-4 | PMCID: PMC8297411 | PMID: 33442061
- Evidence: We used Gautomatch for viral particle picking with template projections obtained with EMAN2 29 from a previous reconstruction 30 .
- Full pipeline: alignment/mapping [IMOD, MAFFT, MotionCor2, Python] -> registration [MotionCor2] -> structure determination [EMAN2] -> stage not stated [CTFFIND, Matplotlib, PyMOL]

### Structural basis of tankyrase activation by polymerization. (Nature 2022)

- DOI: 10.1038/s41586-022-05449-8 | PMCID: PMC9712121 | PMID: 36418402
- Version used: **2.31**
- Evidence: The individual power spectra were then iteratively rotationally aligned using e2align2d.py (from EMAN2 v2.31) 43 , using the sum of three already vertically well-aligned power spectra as initial reference, and the sum of aligned spectra as reference for further alignment iterations.
- Full pipeline: alignment/mapping [Clustal Omega, EMAN2 v2.31] -> quantification [ImageJ] -> normalisation [ImageJ] -> structure determination [PHENIX v1.18.2] -> visualisation [ChimeraX v1.3] -> stage not stated [CellProfiler, Coot, MotionCor2, RELION v2.10, UCSF Chimera v1.14]

### Bending forces and nucleotide state jointly regulate F-actin structure. (Nature 2022)

- DOI: 10.1038/s41586-022-05366-w | PMCID: PMC9646526 | PMID: 36289330
- Evidence: These models were then converted to volume files using the PDB2MRC function in EMAN2 61 .
- Full pipeline: alignment/mapping [MotionCor2] -> quantification [Python] -> differential/statistical testing [Matplotlib] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX, RELION] -> machine learning [TensorFlow, cryoDRGN] -> stage not stated [Coot, EMAN2, UCSF Chimera, scikit-image]

### USP14-regulated allostery of the human proteasome by time-resolved cryo-EM. (Nature 2022)

- DOI: 10.1038/s41586-022-04671-8 | PMCID: PMC9117149 | PMID: 35477760
- Evidence: Micrographs screening and auto-picked particles checking were both preformed in the EMAN2 software 49 .
- Full pipeline: structure determination [PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, CTFFIND, Coot, EMAN2, MotionCor2, RELION]

### Inhibition of calcium-triggered secretion by hydrocarbon-stapled peptides. (Nature 2022)

- DOI: 10.1038/s41586-022-04543-1 | PMCID: PMC8967716 | PMID: 35322233
- Evidence: 6b ) were measured using EMAN2 (ref.
- Full pipeline: quantification [ImageJ v2.0.0] -> simulation/modelling [NAMD] -> stage not stated [EMAN2, PyMOL v2.5.1, VMD]

### Activation mechanism of PINK1. (Nature 2022)

- DOI: 10.1038/s41586-021-04340-2 | PMCID: PMC8828467 | PMID: 34933320
- Evidence: The Ph PINK1 dimer was modelled into the dodecamer map (see below), converted into a volume using UCSF Chimera 53 , low passed to 12 Å and used to create a soft padded mask in EMAN2 ( 54 ).
- Full pipeline: structure determination [Coot v0.9] -> visualisation [ChimeraX v1.1.1] -> stage not stated [AlphaFold, ColabFold, EMAN2, Fiji v1.53k, ImageJ v1.53k, PHENIX v1.19.2, RELION v3.1, UCSF Chimera]

### CryoET of β-amyloid and tau within postmortem Alzheimer's disease brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07680-x | PMCID: PMC11269202 | PMID: 38987603
- Version used: **2.99**
- Evidence: The neural network-based tomogram segmentation pipeline in EMAN2 v.2.99 88 was used to segment tau filaments and Aβ fibrils.
- Full pipeline: alignment/mapping [IMOD v4.12.35] -> structure determination [Coot v0.8.9.2, PHENIX v1.17.1] -> machine learning [EMAN2 v2.99] -> stage not stated [CTFFIND v1.14, ChimeraX v1.5, Fiji, ImageJ, RELION v4.0]

### High-resolution in situ structures of mammalian respiratory supercomplexes. (Nature 2024)

- DOI: 10.1038/s41586-024-07488-9 | PMCID: PMC11222160 | PMID: 38811722
- Evidence: Individual SC particles were picked in EMAN2 (ref.
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX, IMOD] -> visualisation [ChimeraX, IMOD, PyMOL] -> stage not stated [CTFFIND, EMAN2, RELION]

### Mechanism of single-stranded DNA annealing by RAD52-RPA complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07347-7 | PMCID: PMC11096129 | PMID: 38658755
- Evidence: Negative-stain EM data analysis DM3 files were converted to MRC format using e2proc2d.py (EMAN2) 53 .
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega] -> quantification [ImageJ] -> stage not stated [ChimeraX, EMAN2, PHENIX, RELION v3.1]

### Complex water networks visualized by cryogenic electron microscopy of RNA. (Nature 2025)

- DOI: 10.1038/s41586-025-08855-w | PMCID: PMC12137144 | PMID: 40068818
- Evidence: All particles were autopicked using the NeuralNet option in EMAN2 (ref.
- Full pipeline: simulation/modelling [MDAnalysis] -> structure determination [ChimeraX v1.6.1] -> stage not stated [EMAN2, MotionCor2, RELION]

### Myosin forces remodel F-actin for mechanosensitive protein recognition. (Nature 2026)

- DOI: 10.1038/s41586-026-10398-7 | PMCID: PMC13233326 | PMID: 42020745
- Evidence: All of these filament models were bent in a single plane (to prevent supercoil model bias), then converted to volumetric data using the pdb2mrc procedure in EMAN2 (ref.
- Full pipeline: simulation/modelling [Python] -> structure determination [IMOD] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [EMAN2, MotionCor2, PHENIX, RELION, SciPy]

### Entropy-regularized deconvolution of cellular cryotransmission electron tomograms. (PNAS 2021)

- DOI: 10.1073/pnas.2108738118 | PMCID: PMC8685678 | PMID: 34876518
- Evidence: We picked a X-ray crystallography structure of a microtubule from the Protein Data Bank (PDB; ID code 3J2U) to generate a simulated cryo-EM map at 3.3-Å resolution using EMAN2 ( 60 ).
- Full pipeline: alignment/mapping [IMOD] -> simulation/modelling [EMAN2] -> structure determination [IMOD]

### Symmetrical arrangement of proteins under release-ready vesicles in presynaptic terminals. (PNAS 2021)

- DOI: 10.1073/pnas.2024029118 | PMCID: PMC7865176 | PMID: 33468631
- Evidence: The resolution of the final 3D reconstruction was estimated using EMAN2 ( 61 ) ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [EMAN2, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [ImageJ]

### Supramolecular assembly of the <i>Escherichia coli</i> LdcI upon acid stress. (PNAS 2021)

- DOI: 10.1073/pnas.2014383118 | PMCID: PMC7812809 | PMID: 33372137
- Evidence: LdcI stacks were manually picked using e2helixboxer in EMAN2 ( 63 ).
- Full pipeline: registration [MotionCor2] -> dimensionality reduction/clustering [RELION v1.4] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, ImageJ]

### Human species D adenovirus hexon capsid protein mediates cell entry through a direct interaction with CD46. (PNAS 2021)

- DOI: 10.1073/pnas.2020732118 | PMCID: PMC7826407 | PMID: 33384338
- Evidence: A difference map Δρ between the virus–receptor complex HAdV-D56–CD46 and the apo virus HAdV-D56 was calculated using EMAN2 ( 71 ).
- Full pipeline: structure determination [Coot] -> visualisation [PyMOL] -> stage not stated [CCP4, CTFFIND, ChimeraX, EMAN2, MotionCor2, RELION v3.1]

### Nanomolar inhibition of SARS-CoV-2 infection by an unmodified peptide targeting the prehairpin intermediate of the spike protein. (PNAS 2022)

- DOI: 10.1073/pnas.2210990119 | PMCID: PMC9546559 | PMID: 36122200
- Evidence: The data were processed using a combination of MotionCor2 ( 32 ), Gctf ( 33 ), EMAN2 ( 34 ), cryoSPARC ( 35 ), and RELION ( 36 ), as described previously ( 16 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, CellProfiler, EMAN2, MotionCor2, RELION, kallisto]

### Topological crossing in the misfolded <i>Tetrahymena</i> ribozyme resolved by cryo-EM. (PNAS 2022)

- DOI: 10.1073/pnas.2209146119 | PMCID: PMC9477386 | PMID: 36067294
- Evidence: All particles were autopicked via the NeuralNet option in EMAN2 ( 43 ) and further checked manually.
- Full pipeline: visualisation [ChimeraX] -> stage not stated [Coot, EMAN2, MotionCor2, PHENIX, RELION, UCSF Chimera]

### PTX3 structure determination using a hybrid cryoelectron microscopy and AlphaFold approach offers insights into ligand binding and complement activation. (PNAS 2022)

- DOI: 10.1073/pnas.2208144119 | PMCID: PMC9388099 | PMID: 35939690
- Evidence: Particles were picked from motion-corrected micrographs using the neural network within EMAN2 ( 23 ).
- Full pipeline: structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [AlphaFold, ChimeraX, ColabFold v1.3, RELION v3.1]

### Shelterin is a dimeric complex with extensive structural heterogeneity. (PNAS 2022)

- DOI: 10.1073/pnas.2201662119 | PMCID: PMC9351484 | PMID: 35881804
- Evidence: Particles were autopicked using the swarm (for POT1/TPP1 N and POT1/TPP1/TIN2 wt/3×Δ) or Gauss (for other complexes) picker in EMAN2.1 ( 80 ).
- Full pipeline: stage not stated [AlphaFold, EMAN2, RELION]

### In situ architecture of the lipid transport protein VPS13C at ER-lysosome membrane contacts. (PNAS 2022)

- DOI: 10.1073/pnas.2203769119 | PMCID: PMC9303930 | PMID: 35858323
- Version used: **2.91**
- Evidence: Segmentation of ribosomes was done in EMAN2 (version 2.91, https://blake.bcm.edu/emanwiki/EMAN2/Install/BinaryInstallAnaconda/2.91 , RRID:SCR_016867) ( 50 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0] -> structure determination [AlphaFold, ChimeraX, IMOD] -> visualisation [RELION, UCSF Chimera v1.13, seaborn v0.11.2] -> stage not stated [CTFFIND v1.18, EMAN2 v2.91]

### Phenol-soluble modulins PSMα3 and PSMβ2 form nanotubes that are cross-α amyloids. (PNAS 2022)

- DOI: 10.1073/pnas.2121586119 | PMCID: PMC9171771 | PMID: 35533283
- Evidence: After CTF correction, filament images with discrete diameters of 370 Å (346 pixels) and 410 Å (376 pixels) were boxed manually and extracted using e2helixboxer (EMAN2) ( 92 ).
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [EMAN2, RoseTTAFold, UCSF Chimera]

### A unique bacterial secretion machinery with multiple secretion centers. (PNAS 2022)

- DOI: 10.1073/pnas.2119907119 | PMCID: PMC9170169 | PMID: 35471908
- Evidence: IMOD and EMAN2 ( 41 , 44 ) were used to generate 3D surface renderings of P. gingivalis cells and University of California, San Francisco ChimeraX ( http://www.rbvi.ucsf.edu/chimerax ) to visualize subtomogram averages in 3D and molecular modeling.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> visualisation [ChimeraX, EMAN2]

### Cryo-EM structure of RNA-induced tau fibrils reveals a small C-terminal core that may nucleate fibril formation. (PNAS 2022)

- DOI: 10.1073/pnas.2119952119 | PMCID: PMC9169762 | PMID: 35377792
- Evidence: All fibril particles were picked manually using EMAN2 e2helixboxer.py ( 57 ).
- Full pipeline: registration [CTFFIND v4.1.8] -> structure determination [RELION] -> stage not stated [EMAN2, ImageJ]

### Structural conservation among variants of the SARS-CoV-2 spike postfusion bundle. (PNAS 2022)

- DOI: 10.1073/pnas.2119467119 | PMCID: PMC9169775 | PMID: 35363556
- Evidence: Particles were picked using the e2boxer.py in EMAN2 ( 60 ) using a convolutional neural network ( 61 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [PHENIX] -> machine learning [EMAN2] -> stage not stated [CTFFIND, ChimeraX, Coot, PyMOL, Python, RELION, UCSF Chimera]

### Cryo-ET of <i>Toxoplasma</i> parasites gives subnanometer insight into tubulin-based structures. (PNAS 2022)

- DOI: 10.1073/pnas.2111661119 | PMCID: PMC8832990 | PMID: 35121661
- Evidence: Tilt series alignment, tomogram reconstruction, and contrast transfer function estimation are performed automatically using the tomography pipeline in EMAN2 ( 16 ), except the reconstructed tomogram in Fig.
- Full pipeline: alignment/mapping [EMAN2] -> structure determination [ChimeraX, EMAN2] -> stage not stated [IMOD]

### Neutral lysophosphatidylcholine mediates α-synuclein-induced synaptic vesicle clustering. (PNAS 2023)

- DOI: 10.1073/pnas.2310174120 | PMCID: PMC10622907 | PMID: 37883437
- Evidence: Micrographs were lowpass filtered accordingly and displayed in EMAN2.31.
- Full pipeline: stage not stated [EMAN2]

### The evolution of archaeal flagellar filaments. (PNAS 2023)

- DOI: 10.1073/pnas.2304256120 | PMCID: PMC10334743 | PMID: 37399404
- Evidence: S3 E ) using the EMAN2 program e2pdb2mrc ( 72 ).
- Full pipeline: alignment/mapping [UCSF Chimera] -> structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, EMAN2]

### Quantification of gallium cryo-FIB milling damage in biological lamellae. (PNAS 2023)

- DOI: 10.1073/pnas.2301852120 | PMCID: PMC10266028 | PMID: 37216561
- Evidence: 3 A– D , we applied a series of sharp low-pass filters in steps of 0.01 Å −1 to the template using the e2proc3d.py function in EMAN2 ( 39 ).
- Full pipeline: stage not stated [ChimeraX, EMAN2, Python]

### Cryo-EM structure of the Mon1-Ccz1-RMC1 complex reveals molecular basis of metazoan RAB7A activation. (PNAS 2023)

- DOI: 10.1073/pnas.2301725120 | PMCID: PMC10235969 | PMID: 37216550
- Evidence: After CTF estimation by CTFFIND4 ( 36 ), selected micrographs were subjected to EMAN2.31 ( 37 ) for neural network particle picking, with a threshold setting of −0.3 used to maximize inclusion of good particles.
- Full pipeline: structure determination [PHENIX v1.19] -> machine learning [EMAN2] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ImageJ, RELION v3.1]

### Structure-based design of a SARS-CoV-2 Omicron-specific inhibitor. (PNAS 2023)

- DOI: 10.1073/pnas.2300360120 | PMCID: PMC10068829 | PMID: 36940324
- Evidence: The data were processed using a combination of MotionCor2 ( 24 ), Gctf ( 25 ), EMAN2 ( 26 ), cryoSPARC ( 27 ), and RELION ( 28 ), as described previously ( 14 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, EMAN2, MotionCor2, PyMOL, RELION, UCSF Chimera]

### In situ snapshots along a mammalian selective autophagy pathway. (PNAS 2023)

- DOI: 10.1073/pnas.2221712120 | PMCID: PMC10041112 | PMID: 36917659
- Evidence: Microtubules were segmented with the convolutional neural networks of EMAN2 ( 52 ).
- Full pipeline: alignment/mapping [IMOD v4.10.49] -> registration [CTFFIND, MotionCor2] -> structure determination [IMOD v4.10.49] -> machine learning [EMAN2] -> visualisation [ChimeraX]

### Dramatic changes in mitochondrial subcellular location and morphology accompany activation of the CO&lt;sub&gt;2&lt;/sub&gt; concentrating mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2407548121 | PMCID: PMC11513932 | PMID: 39405346
- Evidence: Tomograms were generated using IMOD software ( 71 ) followed by segmentation and visualization using EMAN2 ( 72 ) and USCF Chimera ( 73 ).
- Full pipeline: visualisation [EMAN2, IMOD]

### Structural basis for surface activation of the classical complement cascade by the short pentraxin C-reactive protein. (PNAS 2024)

- DOI: 10.1073/pnas.2404542121 | PMCID: PMC11406272 | PMID: 39240968
- Version used: **2.91**
- Evidence: Manual picking of 133 cryotomograms using the e2spt_boxer_old.py command in EMAN2 (version 2.91) ( 72 ) produced an initial set of 3,428 particles.
- Full pipeline: alignment/mapping [IMOD v4.11] -> simulation/modelling [ChimeraX] -> stage not stated [EMAN2 v2.91]

### Nanoscale architecture of synaptic vesicles and scaffolding complexes revealed by cryo-electron tomography. (PNAS 2024)

- DOI: 10.1073/pnas.2403136121 | PMCID: PMC11228483 | PMID: 38923992
- Evidence: Synaptic vesicles were automatically segmented in EMAN2 using a convolutional neural network trained on a subset of manually annotated vesicle cross-sections ( 83 ).
- Full pipeline: quality control [IMOD] -> alignment/mapping [IMOD] -> machine learning [EMAN2] -> visualisation [ChimeraX] -> stage not stated [Python]

### Structure of mavacamten-free human cardiac thick filaments within the sarcomere by cryoelectron tomography. (PNAS 2024)

- DOI: 10.1073/pnas.2311883121 | PMCID: PMC10907299 | PMID: 38386705
- Evidence: Tilt series were fiducial-free aligned and tomograms calculated by simultaneous iterative reconstruction technique (SIRT) using IMOD and EMAN2 ( 83 , 84 ).
- Full pipeline: alignment/mapping [EMAN2, IMOD] -> registration [MotionCor2] -> structure determination [EMAN2, IMOD] -> stage not stated [CTFFIND]

### Molecular basis for curvature formation in SepF polymerization. (PNAS 2024)

- DOI: 10.1073/pnas.2316922121 | PMCID: PMC10907229 | PMID: 38381790
- Evidence: The outer diameter and width of single ring were measured using EMAN2.
- Full pipeline: stage not stated [EMAN2]

### Dysregulated inter-mitochondrial crosstalk in glioblastoma cells revealed by in situ cryo-electron tomography. (PNAS 2024)

- DOI: 10.1073/pnas.2311160121 | PMCID: PMC10907319 | PMID: 38377189
- Evidence: Tilt series were acquired at a 3° interval from − 60° to +60° and aligned and reconstructed using IMOD ( 79 , 80 ), followed by binning by two in EMAN2 ( 81 ) and denoising using the nonlinear anisotropic diffusion tool in IMOD ( 82 ).
- Full pipeline: alignment/mapping [EMAN2, IMOD] -> structure determination [EMAN2, IMOD]

### Capturing the native structure of membrane proteins using vesicles. (PNAS 2025)

- DOI: 10.1073/pnas.2423407122 | PMCID: PMC12435220 | PMID: 40901875
- Evidence: The Segmentation of EMAN2 ( 79 , 80 ), a convolutional neural network based tool, was employed to locate the membrane density of vesicles in the denoised tomograms and generate 3D volumes of vesicle distribution.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> machine learning [EMAN2] -> stage not stated [ChimeraX, Topaz, UCSF Chimera]

### Structure and organization of full-length epidermal growth factor receptor in extracellular vesicles by cryo-electron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2424678122 | PMCID: PMC12167996 | PMID: 40455995
- Evidence: For better visualization, tomograms were low-pass filtered to 50 Å using e2proc3d.py function from EMAN2 ( 82 ) and tomographic slices were visualized with IMOD ( 81 ).
- Full pipeline: read trimming [edgeR] -> alignment/mapping [IMOD] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX] -> visualisation [EMAN2] -> stage not stated [AlphaFold, ImageJ, MotionCor2, RELION]

### Virion-associated influenza hemagglutinin clusters upon sialic acid binding visualized by cryoelectron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2426427122 | PMCID: PMC12037027 | PMID: 40244672
- Evidence: Tomograms were imported into EMAN2.99 and preprocessed to enhance features for subsequent convolutional neural network-based segmentation and particle picking ( 36 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UCSF Chimera] -> structure determination [PHENIX] -> machine learning [EMAN2] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Matplotlib, Python, RELION, seaborn]

### DNA bending mediated by ORC is essential for replication licensing in budding yeast. (PNAS 2025)

- DOI: 10.1073/pnas.2502277122 | PMCID: PMC12002289 | PMID: 40184174
- Evidence: The micrographs were processed with EMAN2 package for automatic particles picking ( 67 ).
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [EMAN2, ImageJ, MotionCor2, RELION]

### Native architecture of a human GBP1 defense complex for cell-autonomous immunity to infection. (Science 2024)

- DOI: 10.1126/science.abm9903 | PMCID: PMC12091997 | PMID: 38422126
- Evidence: Surface rendering of tomogram was done with EMAN2.23, and refined with UCSF chimera.
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [EMAN2, UCSF Chimera] -> stage not stated [AlphaFold, CellProfiler, ImageJ]

