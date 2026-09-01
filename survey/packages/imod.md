# IMOD

- **Category:** structbio
- **Papers in survey:** 115
- **Journals:** PNAS (71), Nature (31), Cell (11), Science (2)
- **Years:** 2021 (11), 2022 (21), 2023 (24), 2024 (28), 2025 (24), 2026 (7)
- **Versions named:** 4.11 (3), 4.10.49 (2), 4.11.7 (1), 4.12.35 (1), 4.10.25 (1), 4.12.62 (1), 4.11.12 (1), 4.11.13 (1), 4.9 (1), 4.10.15 (1)
- **Pipeline stages it appears in:** alignment/mapping (68), structure determination (53), visualisation (8), registration (7), dimensionality reduction/clustering (2), quality control (1)

## Papers

### The molecular basis for sarcomere organization in vertebrate skeletal muscle. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.047 | PMCID: PMC8054911 | PMID: 33765442
- Evidence: ...orado.edu/SerialEM/ MotionCorr2 Zheng et al., 2017 https://emcore.ucsf.edu/ucsf-software EMAN2 Tang et al., 2007 https://blake.bcm.edu/emanwiki/EMAN2 IMOD Kremer et al., 1996 https://bio3d.colorado.edu/imod/ crYOLO Wagner et al., 2019 https://cryolo.readthedocs.io RELION3 Bharat and Scheres, 2016 https://www3.mrc-lmb.cam.ac.uk/relion/index.php?title=Main_Page PEET Heumann et al., 2011 ; Nicastro e...
- Full pipeline: visualisation [R] -> stage not stated [EMAN2, Fiji, IMOD, ImageJ, RELION, TrackMate]

### Cone-shaped HIV-1 capsids are transported through intact nuclear pores. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.025 | PMCID: PMC7895898 | PMID: 33571428
- Version used: **4.9.2**
- Evidence: ...helper functions for AAV production Matsushita et al., 1998 N/A Software and algorithms FIJI (v 2.1.0/1.53c) Schindelin et al., 2012 RRID: SCR_002285 IMOD (v 4.9.2 and v 4.9.4) Kremer et al., 1996 RRID: SCR_003297 Icy (v.
- Full pipeline: stage not stated [IMOD v4.9.2, UCSF Chimera v1.14]

### DNA origami signposts for identifying proteins on cell membranes by electron cryotomography. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.033 | PMCID: PMC7895908 | PMID: 33606980
- Evidence: ... et al., 2011 https://cando-dna-origami.org/ PEET (Particle Estimation for Electron Tomography) Heumann et al., 2011 https://bio3d.colorado.edu/PEET/ IMOD Kremer et al., 1996 https://bio3d.colorado.edu/imod/ UCSF Chimera Pettersen et al., 2004 https://www.cgl.ucsf.edu/chimera/ FIJI Schindelin et al., 2012 https://imagej.net/Fiji SerialEM Mastronarde, 2005 https://bio3d.colorado.edu/SerialEM/ Micro...
- Full pipeline: stage not stated [IMOD, UCSF Chimera]

### Liquid-to-solid phase transition of oskar ribonucleoprotein granules is essential for their function in Drosophila embryonic development. (Cell 2022)

- DOI: 10.1016/j.cell.2022.02.022 | PMCID: PMC9042795 | PMID: 35325593
- Version used: **4.9**
- Evidence: (2014) http://plaac.wi.mit.edu/ IUPred Mészáros et al., (2018) https://iupred2a.elte.hu IMOD v.4.9 Kremer et al.
- Full pipeline: stage not stated [IMOD v4.9]

### Cryo-ET of Env on intact HIV virions reveals structural variation and positioning on the Gag lattice. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.013 | PMCID: PMC9000915 | PMID: 35123651
- Version used: **4.10.15**
- Evidence: ...arragher et al., 2000 ) N/A SerialEM ( Mastronarde, 2005 ) https://bio3d.colorado.edu/SerialEM/ Motioncor2 UCSF https://emcore.ucsf.edu/ucsf-software IMOD 4.10.15 ( Kremer et al., 1996 ) https://bio3d.colorado.edu/imod/ Relion 2.1 ( Bharat and Scheres, 2016 ; Scheres, 2012 ) https://www3.mrc-lmb.cam.ac.uk/relion/index.php/Main_Page PEET 1.12 ( Nicastro et al., 2006 ) https://bio3d.colorado.edu/PEE...
- Full pipeline: alignment/mapping [Clustal Omega] -> stage not stated [ChimeraX, Coot, EMAN2, IMOD v4.10.15, ImageJ, RELION v2.1, UCSF Chimera]

### Comprehensive structure and functional adaptations of the yeast nuclear pore complex. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.015 | PMCID: PMC8928745 | PMID: 34982960
- Evidence: Chen Xu), which does local motion correction with IMOD ( Kremer et al., 1996 ) on the imaging computer and creates power-pair jpegs with a motion-corrected micrograph image paired with the fitted power spectrum from CTFFIND4.
- Full pipeline: registration [IMOD] -> simulation/modelling [PHENIX] -> structure determination [PHENIX] -> stage not stated [Coot, EMAN2, ImageJ, RELION v2.0]

### De novo protein identification in mammalian sperm using in situ cryoelectron tomography and AlphaFold2 docking. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.017 | PMCID: PMC10842264 | PMID: 37865089
- Evidence: IMOD was used to visualize the tomographic slices 50 .
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler v4.4.1] -> differential/statistical testing [Bioconductor] -> visualisation [IMOD] -> stage not stated [AlphaFold, ChimeraX, ColabFold, Coot v0.9.8.1, MotionCor2, R, RELION, UCSF Chimera]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Evidence: 98 Tomogram reconstruction and analysis TS were aligned using patch tracking and reconstructed with the IMOD software package.
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### ESCRT recruitment to SARS-CoV-2 spike induces virus-like particles that improve mRNA vaccines. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.024 | PMCID: PMC10121106 | PMID: 37146611
- Evidence: ...algorithms Image J Rueden et al., 2017 54 https://imagej.net/ RRID: SCR_003070 SerialEM 3.7 Mastrondarde 55 https://pubmed.ncbi.nlm.nih.gov/16182563/ IMOD Mastronarde and Held 56 https://bio3d.colorado.edu/imod/ RRID: SCR_003297 UCSF ChimeraX Goddard et al.
- Full pipeline: stage not stated [ChimeraX, IMOD, ImageJ]

### Molecular mechanisms of stress-induced reactivation in mumps virus condensates. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.015 | PMCID: PMC10156176 | PMID: 37116470
- Evidence: 78 N/A IMOD package Kremer et al.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [Bioconductor] -> structure determination [Coot, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, BWA v0.7.17, ChimeraX v1.1.1, IMOD, PHENIX v1.18, Picard, R v3.6, RELION v3.0, freebayes v1.1.0, limma]

### The molecular architecture of the nuclear basket. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.020 | PMCID: PMC11416316 | PMID: 39127037
- Evidence: In tomograms, nuclear pores were manually picked in IMOD.
- Full pipeline: stage not stated [ChimeraX, EMAN2, IMOD, RELION]

### The cellular environment shapes the nuclear pore complex architecture. (Nature 2021)

- DOI: 10.1038/s41586-021-03985-3 | PMCID: PMC8550940 | PMID: 34646014
- Evidence: Tilt series were aligned with 4× binned projections using patch tracking in the IMOD software package 46 .
- Full pipeline: alignment/mapping [IMOD] -> differential/statistical testing [Matplotlib, Python, SciPy] -> stage not stated [RELION, UCSF Chimera]

### Functional refolding of the penetration protein on a non-enveloped virus. (Nature 2021)

- DOI: 10.1038/s41586-020-03124-4 | PMCID: PMC8297411 | PMID: 33442061
- Evidence: We extracted subparticle images (corresponding to the location of VP4 proteins) based on the icosahedral alignment from the original polished, and signal-subtracted particle stacks using IMOD 36 .
- Full pipeline: alignment/mapping [IMOD, MAFFT, MotionCor2, Python] -> registration [MotionCor2] -> structure determination [EMAN2] -> stage not stated [CTFFIND, Matplotlib, PyMOL]

### A mitotic chromatin phase transition prevents perforation by microtubules. (Nature 2022)

- DOI: 10.1038/s41586-022-05027-y | PMCID: PMC9433320 | PMID: 35922507
- Evidence: Tomograms were reconstructed using the R-weighted back projection method implemented in the IMOD software package 64 .
- Full pipeline: structure determination [IMOD] -> stage not stated [ImageJ]

### Architecture and self-assembly of the jumbo bacteriophage nuclear shell. (Nature 2022)

- DOI: 10.1038/s41586-022-05013-4 | PMCID: PMC9365700 | PMID: 35922510
- Evidence: Tilt movies were corrected for whole-frame motion and aligned via patch tracking using Etomo (IMOD-v4.10.28) 28 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [ChimeraX, MDTraj, PyMOL, VMD] -> structure determination [ChimeraX, PHENIX, PyMOL, VMD] -> visualisation [ChimeraX, PyMOL, VMD] -> stage not stated [UCSF Chimera]

### HIV-1 Env trimers asymmetrically engage CD4 receptors in membranes. (Nature 2023)

- DOI: 10.1038/s41586-023-06762-6 | PMCID: PMC10686830 | PMID: 37993716
- Evidence: Weighted back projection and tomographic slices were visualized using IMOD 48 .
- Full pipeline: simulation/modelling [NAMD v3.0] -> structure determination [ChimeraX] -> visualisation [ChimeraX, IMOD] -> stage not stated [Python, RELION]

### Structure of the native myosin filament in the relaxed cardiac sarcomere. (Nature 2023)

- DOI: 10.1038/s41586-023-06690-5 | PMCID: PMC10665186 | PMID: 37914933
- Evidence: Tomogram reconstruction and particle picking Motion correction and contrast transfer function estimation were carried out in Warp 54 ; tilt series alignment was carried out in IMOD 55 .
- Full pipeline: alignment/mapping [ChimeraX, IMOD] -> registration [IMOD] -> structure determination [IMOD] -> visualisation [AlphaFold] -> stage not stated [RELION v3.1]

### In situ architecture of the ER-mitochondria encounter structure. (Nature 2023)

- DOI: 10.1038/s41586-023-06050-3 | PMCID: PMC7614606 | PMID: 37165187
- Evidence: Tomogram Reconstruction and Subtomogram Averaging Frames were gain corrected, aligned, dose-weighted and binned to a pixel size of 2.684 Å with the preprocessing script from the subTOM package 51 which executes IMOD’s alignframes and ctfplotter functions 52 .
- Full pipeline: alignment/mapping [IMOD, UCSF Chimera] -> quantification [ImageJ] -> simulation/modelling [NAMD] -> structure determination [IMOD] -> visualisation [ChimeraX, ggplot2] -> stage not stated [AlphaFold, R, VMD]

### Structural basis of mitochondrial membrane bending by the I-II-III&lt;sub&gt;2&lt;/sub&gt;-IV&lt;sub&gt;2&lt;/sub&gt; supercomplex. (Nature 2023)

- DOI: 10.1038/s41586-023-05817-y | PMCID: PMC10060162 | PMID: 36949187
- Evidence: Following motion correction in motionCor2, tomographic reconstruction from the tilt series was performed in IMOD 42 using phase-flipping and a binning factor of 2.
- Full pipeline: registration [IMOD, RELION] -> simulation/modelling [ChimeraX, GROMACS] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold]

### Spatial mapping of mitochondrial networks and bioenergetics in lung cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-05793-3 | PMCID: PMC10033418 | PMID: 36922590
- Evidence: Following data collection, the images were converted to .mrc format and cross-correlation was used for rigid image alignment of the slices using the IMOD image processing package 40 .
- Full pipeline: alignment/mapping [IMOD] -> stage not stated [ImageJ, QuPath]

### Visualization of translation and protein biogenesis at the ER membrane. (Nature 2023)

- DOI: 10.1038/s41586-022-05638-5 | PMCID: PMC9892003 | PMID: 36697828
- Version used: **4.10.25**
- Evidence: The combined stacks were aligned using the gold fiducials in IMOD (4.10.25) 55 .
- Full pipeline: alignment/mapping [IMOD v4.10.25, NumPy v1.20.3, Python v3.8.11, RELION v3.1.1, SciPy v1.7.1] -> structure determination [ChimeraX v1.3.0, UCSF Chimera v1.14.0] -> visualisation [ChimeraX v1.3.0] -> stage not stated [AlphaFold]

### Actin cytoskeleton and complex cell architecture in an Asgard archaeon. (Nature 2023)

- DOI: 10.1038/s41586-022-05550-y | PMCID: PMC9834061 | PMID: 36544020
- Evidence: Tomogram reconstruction, data processing and segmentation Tilt series were drift-corrected using alignframes in IMOD 105 and 4×-binned tomograms were reconstructed by weighted-back projection in IMOD.
- Full pipeline: read trimming [MAFFT v7.427, SPAdes v3.15.2, Trimmomatic v0.36] -> alignment/mapping [BEDTools, IMOD, MAFFT v7.427, SAMtools, minimap2] -> dimensionality reduction/clustering [BLAST] -> structure determination [IMOD, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [Cutadapt, DADA2, Flye v2.8.3, ImageJ, Pilon, Prokka v1.14.6, QIIME 2, RELION v4.0]

### Visualizing chaperonin function in situ by cryo-electron tomography. (Nature 2024)

- DOI: 10.1038/s41586-024-07843-w | PMCID: PMC11390479 | PMID: 39169181
- Evidence: The reconstruction was performed in IMOD using patch tracking (v.4.11.1, RRID:SCR_003297, https://bio3d.colorado.edu/imod/ ) 58 using the TOMOgram MANager (TOMOMAN) wrapper scripts 59 .
- Full pipeline: alignment/mapping [MotionCor2 v1.4.0] -> registration [RELION] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX]

### Molecular architecture of coronavirus double-membrane vesicle pore complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07817-y | PMCID: PMC11374677 | PMID: 39143215
- Evidence: The blank images were removed by calculating the average image intensity using the clip command in IMOD.
- Full pipeline: alignment/mapping [Python] -> structure determination [ChimeraX, Coot, RELION] -> visualisation [Topaz] -> stage not stated [AlphaFold, IMOD]

### Structural basis for transthiolation intermediates in the ubiquitin pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07828-9 | PMCID: PMC11374688 | PMID: 39143218
- Version used: **4.11**
- Evidence: 2D slice views of electron microscopy maps were visualized using IMOD 4.11 72 .
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> differential/statistical testing [Topaz] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [IMOD v4.11] -> stage not stated [CTFFIND, ChimeraX, RELION v3.1]

### CryoET of β-amyloid and tau within postmortem Alzheimer's disease brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07680-x | PMCID: PMC11269202 | PMID: 38987603
- Version used: **4.12.35**
- Evidence: Tilt series stacks were generated in Warp and imported into etomo IMOD (v.4.12.35) 77 , 78 for fine alignment using patch tracking.
- Full pipeline: alignment/mapping [IMOD v4.12.35] -> structure determination [Coot v0.8.9.2, PHENIX v1.17.1] -> machine learning [EMAN2 v2.99] -> stage not stated [CTFFIND v1.14, ChimeraX v1.5, Fiji, ImageJ, RELION v4.0]

### Structure and topography of the synaptic V-ATPase-synaptophysin complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07610-x | PMCID: PMC11269182 | PMID: 38838737
- Evidence: Movie frames were aligned using Motioncor2 59 , and motion-corrected tilt series were then aligned using fiducial tracking with the IMOD software package 60 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [AlphaFold, PHENIX v1.21] -> machine learning [RELION, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Coot, Python, SciPy, UCSF Chimera]

### Membraneless channels sieve cations in ammonia-oxidizing marine archaea. (Nature 2024)

- DOI: 10.1038/s41586-024-07462-5 | PMCID: PMC11153153 | PMID: 38811725
- Evidence: Subtomogram averaging of whole cells for structure determination To obtain initial lattice maps, a previously described strategy was used 16 , in which tilt-series alignment using gold fiducials and tomogram generation was performed using IMOD 45 and initial contrast transfer functions (CTFs) were estimated using CTFFIND4 46 .
- Full pipeline: alignment/mapping [IMOD, RELION] -> simulation/modelling [NAMD v2.14, VMD v1.94] -> structure determination [Coot, IMOD, PHENIX] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold v2.2.0, MotionCor2]

### High-resolution in situ structures of mammalian respiratory supercomplexes. (Nature 2024)

- DOI: 10.1038/s41586-024-07488-9 | PMCID: PMC11222160 | PMID: 38811722
- Evidence: Raw micrographs and reconstructed results were visualized and diagnosed using IMOD 63 and ChimeraX 64 .
- Full pipeline: registration [MotionCor2] -> structure determination [ChimeraX, IMOD] -> visualisation [ChimeraX, IMOD, PyMOL] -> stage not stated [CTFFIND, EMAN2, RELION]

### PGE&lt;sub&gt;2&lt;/sub&gt; inhibits TIL expansion by disrupting IL-2 signalling and mitochondrial function. (Nature 2024)

- DOI: 10.1038/s41586-024-07352-w | PMCID: PMC11078736 | PMID: 38658764
- Evidence: Panoramic alignments were performed with the software IMOD.
- Full pipeline: alignment/mapping [IMOD, STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma v3.54.0] -> visualisation [UMAP] -> stage not stated [GSEA, GSVA v1.44.5, HTSeq v0.9.1, ImageJ, R]

### The HIV capsid mimics karyopherin engagement of FG-nucleoporins. (Nature 2024)

- DOI: 10.1038/s41586-023-06969-7 | PMCID: PMC10881392 | PMID: 38267582
- Evidence: Three-dimensional reconstructions from tilt series were generated with the IMOD package 61 .
- Full pipeline: dimensionality reduction/clustering [IMOD] -> structure determination [IMOD] -> stage not stated [AlphaFold, ImageJ]

### In situ structural mechanism of epothilone-B-induced CNS axon regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09654-z | PMCID: PMC12795760 | PMID: 41224993
- Evidence: The tilt series were aligned using the IMOD ETOMO package 68 .
- Full pipeline: alignment/mapping [IMOD] -> structure determination [ChimeraX, PHENIX] -> visualisation [ImageJ] -> stage not stated [RELION v5.0]

### Synthetic α-synuclein fibrils replicate in mice causing MSA-like pathology. (Nature 2025)

- DOI: 10.1038/s41586-025-09698-1 | PMCID: PMC12695662 | PMID: 41193804
- Evidence: Tomograms were reconstructed using IMOD 46 and filtered with a non-local-means filter with Amira (Thermo Fisher Scientific, Amira v.2021.2).
- Full pipeline: structure determination [ChimeraX, Coot, IMOD, PHENIX, RELION v4.0] -> stage not stated [MACS2]

### Myeloperoxidase transforms chromatin into neutrophil extracellular traps. (Nature 2025)

- DOI: 10.1038/s41586-025-09523-9 | PMCID: PMC12629992 | PMID: 40963017
- Version used: **4.11**
- Evidence: After tilt series alignment in IMOD (v.4.11) 59 , tomograms were reconstructed at binning 4 (pixel size 13.78 Å px −1 ) in Warp 58 .
- Full pipeline: alignment/mapping [IMOD v4.11] -> dimensionality reduction/clustering [UMAP] -> structure determination [IMOD v4.11, PHENIX, RELION v3.1] -> stage not stated [ChimeraX]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Version used: **4.11.7**
- Evidence: Tomograms of ROIs were acquired using SerialEM v3.7.11 and reconstructed using IMOD v4.11.7 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### A coronavirus assembly inhibitor that targets the viral membrane protein. (Nature 2025)

- DOI: 10.1038/s41586-025-08773-x | PMCID: PMC11981944 | PMID: 40140569
- Evidence: The tilt series were reconstructed using IMOD 56 – 58 .
- Full pipeline: quantification [ImageJ] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [Coot, UCSF Chimera]

### Structural diversity of axonemes across mammalian motile cilia. (Nature 2025)

- DOI: 10.1038/s41586-024-08337-5 | PMCID: PMC11779644 | PMID: 39743588
- Evidence: Cryo-ET data processing Videos of ten frames, recorded at each tilt angle, were motion corrected and coarsely aligned into a tilt series of single micrographs using alignframes from IMOD 62 .
- Full pipeline: alignment/mapping [IMOD] -> registration [IMOD] -> dimensionality reduction/clustering [RELION v3.1] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ChimeraX, Coot]

### In situ analysis reveals the TRiC duty cycle and PDCD5 as an open-state cofactor. (Nature 2025)

- DOI: 10.1038/s41586-024-08321-z | PMCID: PMC11754096 | PMID: 39663456
- Evidence: Tilt series were aligned automatically using the IMOD package 52 .
- Full pipeline: alignment/mapping [Clustal Omega, IMOD] -> structure determination [RELION] -> visualisation [ChimeraX, napari] -> stage not stated [AlphaFold]

### Myosin forces remodel F-actin for mechanosensitive protein recognition. (Nature 2026)

- DOI: 10.1038/s41586-026-10398-7 | PMCID: PMC13233326 | PMID: 42020745
- Evidence: 74 ), followed by reconstruction using IMOD 75 with back-projection at a binning of 2 (voxel size of 10.1 Å).
- Full pipeline: simulation/modelling [Python] -> structure determination [IMOD] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [EMAN2, MotionCor2, PHENIX, RELION, SciPy]

### An enteric neuron ionotropic receptor regulates salt stress resistance. (Nature 2026)

- DOI: 10.1038/s41586-026-10348-3 | PMCID: PMC13293861 | PMID: 41922765
- Evidence: Following the alignment, manual segmentation was performed using 3dmod v4.11 from the IMOD suite ( https://bio3d.colorado.edu/imod/ ) to generate the 3D reconstruction of the I3 sensory ending.
- Full pipeline: read trimming [Trim Galore v10.5281] -> alignment/mapping [IMOD, Trim Galore v10.5281] -> structure determination [IMOD] -> stage not stated [Python]

### CLCC1 governs ER bilayer equilibration to maintain lipid homeostasis. (Nature 2026)

- DOI: 10.1038/s41586-026-10161-y | PMCID: PMC13061606 | PMID: 41741642
- Evidence: Subsequently, each tilt series was aligned using patch-tracking method in IMOD software 60 , and then reconstructed using back projection method to obtain a tomogram.
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2] -> dimensionality reduction/clustering [R] -> structure determination [IMOD] -> visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX v1.7.1, Fiji, ImageJ]

### Integrase anchors viral RNA to the HIV-1 capsid interior. (Nature 2026)

- DOI: 10.1038/s41586-026-10154-x | PMCID: PMC13102720 | PMID: 41708858
- Evidence: Tilt images were aligned using patch tracking in IMOD 74 , and CTF-corrected tomograms were reconstructed with WarpTools.
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0, RELION] -> normalisation [ImageJ, NAMD v3.0.1] -> simulation/modelling [VMD] -> structure determination [ChimeraX, Coot, IMOD] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PyMOL, Topaz, UCSF Chimera]

### Entropy-regularized deconvolution of cellular cryotransmission electron tomograms. (PNAS 2021)

- DOI: 10.1073/pnas.2108738118 | PMCID: PMC8685678 | PMID: 34876518
- Evidence: Dose-weighted tilt series were aligned and reconstructed using Etomo, part of the IMOD package ( 66 ).
- Full pipeline: alignment/mapping [IMOD] -> simulation/modelling [EMAN2] -> structure determination [IMOD]

### Nanometer-resolution in situ structure of the SARS-CoV-2 postfusion spike protein. (PNAS 2021)

- DOI: 10.1073/pnas.2112703118 | PMCID: PMC8640741 | PMID: 34782481
- Evidence: All tomograms were deconvolved using Warp ( 17 ) and are displayed using IMOD ( 38 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [IMOD, RELION]

### In-cell structures of conserved supramolecular protein arrays at the mitochondria-cytoskeleton interface in mammalian sperm. (PNAS 2021)

- DOI: 10.1073/pnas.2110996118 | PMCID: PMC8609336 | PMID: 34737233
- Evidence: Tomograms were reconstructed in IMOD ( 86 ) using weighted back-projection, with a simultaneous iterative reconstruction technique (SIRT)–like filter ( 87 ) to aid visualization and segmentation.
- Full pipeline: structure determination [ChimeraX, IMOD] -> visualisation [IMOD] -> stage not stated [R, igraph]

### Architecture of cell-cell junctions in situ reveals a mechanism for bacterial biofilm inhibition. (PNAS 2021)

- DOI: 10.1073/pnas.2109940118 | PMCID: PMC8346871 | PMID: 34321357
- Evidence: Tilt series alignment was carried out using the eTOMO graphical user interface in the IMOD software ( 47 ).
- Full pipeline: alignment/mapping [CTFFIND, IMOD] -> structure determination [CTFFIND]

### Nuclear envelope budding is a response to cellular stress. (PNAS 2021)

- DOI: 10.1073/pnas.2020997118 | PMCID: PMC8325156 | PMID: 34290138
- Evidence: The tomographic reconstruction was performed using the IMOD software package ( 105 ).
- Full pipeline: structure determination [IMOD] -> stage not stated [Pilon]

### Symmetrical arrangement of proteins under release-ready vesicles in presynaptic terminals. (PNAS 2021)

- DOI: 10.1073/pnas.2024029118 | PMCID: PMC7865176 | PMID: 33468631
- Evidence: These were subsequently aligned using gold fiducial markers or fiducial free cross-correlation using the IMOD ( 56 , 57 ) software package.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [EMAN2, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [ImageJ]

### <i>Arabidopsis</i> ORP2A mediates ER-autophagosomal membrane contact sites and regulates PI3P in plant autophagy. (PNAS 2022)

- DOI: 10.1073/pnas.2205314119 | PMCID: PMC9618059 | PMID: 36252028
- Evidence: Dual-axis tomograms were calculated from pairs of image stacks with the etomo program of the IMOD software package.
- Full pipeline: quantification [ImageJ] -> stage not stated [IMOD]

### Geometrically programmed self-limited assembly of tubules using DNA origami colloids. (PNAS 2022)

- DOI: 10.1073/pnas.2207902119 | PMCID: PMC9618141 | PMID: 36252043
- Evidence: Subsequent analysis is performed using Etomo (IMOD) ( 53 ).
- Full pipeline: stage not stated [IMOD, RELION]

### SPACA9 is a lumenal protein of human ciliary singlet and doublet microtubules. (PNAS 2022)

- DOI: 10.1073/pnas.2207605119 | PMCID: PMC9564825 | PMID: 36191189
- Evidence: Tomograms of animal sperm were calculated using patch tracking and CTF corrected using the IMOD package ( 51 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX, Clustal Omega v1.2.2] -> stage not stated [AlphaFold, Coot v0.9.4.1, IMOD, PHENIX, PyMOL v2.3.4, RELION]

### In situ structural analysis reveals membrane shape transitions during autophagosome formation. (PNAS 2022)

- DOI: 10.1073/pnas.2209823119 | PMCID: PMC9522377 | PMID: 36122245
- Version used: **4.10.49**
- Evidence: Frames were aligned using MotionCorr2 (v.1.4.0, https://emcore.ucsf.edu/ucsf-software ) ( 57 ), and reconstruction was performed in IMOD (v.4.10.49, RRID:SCR_003297, https://bio3d.colorado.edu/imod/ ) by using the TomoMAN wrapper scripts ( 58 ).
- Full pipeline: alignment/mapping [IMOD v4.10.49] -> differential/statistical testing [SciPy v1.6.2, pingouin] -> structure determination [ChimeraX v1.2.5, IMOD v4.10.49] -> stage not stated [ImageJ v1.53, RELION v3.1.2]

### A multidomain connector links the outer membrane and cell wall in phylogenetically deep-branching bacteria. (PNAS 2022)

- DOI: 10.1073/pnas.2203156119 | PMCID: PMC9388160 | PMID: 35943982
- Evidence: Tilt series alignment using gold fiducials and tomogram generation was performed in IMOD ( 80 ).
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2] -> dimensionality reduction/clustering [MotionCor2] -> structure determination [ChimeraX, Coot, PHENIX, RELION] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [AlphaFold]

### Structural insight and characterization of human Twinkle helicase in mitochondrial disease. (PNAS 2022)

- DOI: 10.1073/pnas.2207459119 | PMCID: PMC9371709 | PMID: 35914129
- Evidence: ( D and E ) Cryo-EM density maps of ( D ) heptamer (blue-gray) and ( E ) octamer (salmon) colored with size measurements indicated in angstroms of the lumen and width as measured in IMOD ( 49 ).
- Full pipeline: alignment/mapping [MotionCor2] -> structure determination [AlphaFold, IMOD] -> stage not stated [PHENIX, PyMOL]

### Ciliogenesis requires sphingolipid-dependent membrane and axoneme interaction. (PNAS 2022)

- DOI: 10.1073/pnas.2201096119 | PMCID: PMC9351462 | PMID: 35895683
- Evidence: Tilt series were aligned with the patch-tracking method in IMOD software ( 50 ).
- Full pipeline: quality control [Bowtie2] -> alignment/mapping [Bowtie2, IMOD] -> dimensionality reduction/clustering [seaborn] -> differential/statistical testing [Bioconductor, Python, edgeR] -> visualisation [seaborn] -> stage not stated [ImageJ, MotionCor2]

### In situ architecture of the lipid transport protein VPS13C at ER-lysosome membrane contacts. (PNAS 2022)

- DOI: 10.1073/pnas.2203769119 | PMCID: PMC9303930 | PMID: 35858323
- Evidence: Alignment of the tilt series and tomographic reconstructions was performed in Etomo, which is part of the IMOD package (version 4.11.12, https://bio3d.colorado.edu/imod , RRID:SCR_003297) ( 48 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0] -> structure determination [AlphaFold, ChimeraX, IMOD] -> visualisation [RELION, UCSF Chimera v1.13, seaborn v0.11.2] -> stage not stated [CTFFIND v1.18, EMAN2 v2.91]

### In situ structure of intestinal apical surface reveals nanobristles on microvilli. (PNAS 2022)

- DOI: 10.1073/pnas.2122249119 | PMCID: PMC9214534 | PMID: 35666862
- Evidence: Tilt series were aligned with the patch-tracking method in IMOD software ( 37 ).
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [IMOD, STAR v2.6.0c] -> stage not stated [ImageJ, MotionCor2, UCSF Chimera]

### Locations and in situ structure of the polymerase complex inside the virion of vesicular stomatitis virus. (PNAS 2022)

- DOI: 10.1073/pnas.2111948119 | PMCID: PMC9170060 | PMID: 35476516
- Evidence: In total, 40 tilt series were collected and then reconstructed in IMOD ( 47 ).
- Full pipeline: alignment/mapping [RELION v3.0.8] -> structure determination [IMOD, RELION v3.0.8]

### A unique bacterial secretion machinery with multiple secretion centers. (PNAS 2022)

- DOI: 10.1073/pnas.2119907119 | PMCID: PMC9170169 | PMID: 35471908
- Evidence: ... of corrected sums into tilt series, automatic fiducial seed model generation, alignment, and contrast transfer function correction of tilt series by IMOD ( 41 ) and weighted back projection (WBP) reconstruction of tilt series into tomograms using Tomo3D ( 42 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> visualisation [ChimeraX, EMAN2]

### Biological matrix composites from cultured plant cells. (PNAS 2022)

- DOI: 10.1073/pnas.2119523119 | PMCID: PMC9169740 | PMID: 35377816
- Evidence: Images were recorded with US1000 camera (Gatan, Inc.) using the SerialEM software package ( 54 ), and the analysis was conducted using the IMOD software package ( 55 ).
- Full pipeline: stage not stated [IMOD]

### FliL ring enhances the function of periplasmic flagella. (PNAS 2022)

- DOI: 10.1073/pnas.2117245119 | PMCID: PMC8931381 | PMID: 35254893
- Evidence: IMOD ( 72 ) was then used to align tilt series with gold markers.
- Full pipeline: alignment/mapping [CTFFIND, IMOD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold]

### Strain and rupture of HIV-1 capsids during uncoating. (PNAS 2022)

- DOI: 10.1073/pnas.2117781119 | PMCID: PMC8915963 | PMID: 35238630
- Evidence: Tilt series were aligned by using IMOD ( 44 ).
- Full pipeline: alignment/mapping [IMOD] -> simulation/modelling [LAMMPS, NAMD v2.14]

### Cryo-ET of <i>Toxoplasma</i> parasites gives subnanometer insight into tubulin-based structures. (PNAS 2022)

- DOI: 10.1073/pnas.2111661119 | PMCID: PMC8832990 | PMID: 35121661
- Evidence: 1 , which was performed by IMOD ( 53 , 54 ).
- Full pipeline: alignment/mapping [EMAN2] -> structure determination [ChimeraX, EMAN2] -> stage not stated [IMOD]

### The flagellar motor protein FliL forms a scaffold of circumferentially positioned rings required for stator activation. (PNAS 2022)

- DOI: 10.1073/pnas.2118401119 | PMCID: PMC8794807 | PMID: 35046042
- Evidence: Drift correction of the image stacks and alignment of the tilt series were performed using Motioncorr2 ( 45 ) and IMOD ( 46 ), respectively.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [PHENIX, REFMAC] -> stage not stated [ChimeraX, PyMOL]

### Human anti-C1q autoantibodies bind specifically to solid-phase C1q and enhance phagocytosis but not complement activation. (PNAS 2023)

- DOI: 10.1073/pnas.2310666120 | PMCID: PMC10723154 | PMID: 38048459
- Version used: **4.11.13**
- Evidence: Alignment of cryo-electron tomography raw frames was performed using the “alignframes” command from the software program IMOD 4.11.13 ( 45 ).
- Full pipeline: alignment/mapping [IMOD v4.11.13] -> stage not stated [UCSF Chimera v1.16]

### Vimentin regulates nuclear segmentation in neutrophils. (PNAS 2023)

- DOI: 10.1073/pnas.2307389120 | PMCID: PMC10691343 | PMID: 37983515
- Evidence: Tilt series were aligned using patch-tracking mode, and tomograms were reconstructed by back projection by IMOD ( 34 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [MotionCor2, RELION v2.1]

### The genome of a bunyavirus cannot be defined at the level of the viral particle but only at the scale of the viral population. (PNAS 2023)

- DOI: 10.1073/pnas.2309412120 | PMCID: PMC10691328 | PMID: 37983500
- Evidence: Image alignment and three-dimensional reconstructions were performed using Etomo from IMOD package ( 50 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [IMOD] -> structure determination [IMOD] -> stage not stated [BLAST, ImageJ, NanoPlot v1.40.0]

### Diacylglycerol-dependent hexamers of the SNARE-assembling chaperone Munc13-1 cooperatively bind vesicles. (PNAS 2023)

- DOI: 10.1073/pnas.2306086120 | PMCID: PMC10623011 | PMID: 37883433
- Evidence: Movies were aligned and saved as mrc stacks using alignframes from IMOD package ( 47 ).
- Full pipeline: alignment/mapping [IMOD] -> machine learning [Topaz]

### Neutral sphingomyelinase 2 is required for HIV-1 maturation. (PNAS 2023)

- DOI: 10.1073/pnas.2219475120 | PMCID: PMC10334776 | PMID: 37406093
- Evidence: The automated cryoET pipeline developed in-house was used for initial tomograms ( https://github.com/ffyr2w/cet_toolbox ) through performing motion correction ( 96 ) of the raw frames, tilt-series alignment, and final reconstruction with IMOD ( 97 ).
- Full pipeline: alignment/mapping [IMOD] -> registration [IMOD] -> structure determination [IMOD]

### 3D surface reconstruction of cellular cryo-soft X-ray microscopy tomograms using semisupervised deep learning. (PNAS 2023)

- DOI: 10.1073/pnas.2209938120 | PMCID: PMC10268598 | PMID: 37276395
- Evidence: Tracking, alignment, and tomographic reconstruction were performed using 30 iterations of the simultaneous iterative reconstruction technique ( 64 ) in IMOD ( 65 ), using gold nanoparticles as fiducial markers.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> machine learning [TensorFlow] -> stage not stated [SciPy]

### The cell envelope of <i>Thermotogae</i> suggests a mechanism for outer membrane biogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2303275120 | PMCID: PMC10160955 | PMID: 37094164
- Evidence: Tilt series were aligned using IMOD, contrast transfer function (CTF) was corrected using CTFFind4 and novaCTF, and 3D reconstructions were calculated using IMOD with the back-weighted projection method ( 56 – 59 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [AlphaFold, ChimeraX, HMMER, IQ-TREE v2.1.4, ImageJ, RoseTTAFold]

### In situ architecture and membrane fusion of SARS-CoV-2 Delta variant. (PNAS 2023)

- DOI: 10.1073/pnas.2213332120 | PMCID: PMC10160983 | PMID: 37094167
- Evidence: The tilt series were contrast transfer function corrected using Novactf ( 40 ), 162 tilt-series with good fiducial alignment and relative thin ice thickness were reconstructed to tomograms by weighted back projection in IMOD ( 41 ), resulting in a final pixel size of 1.36 Å/pixel.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD, PHENIX] -> stage not stated [Coot, MotionCor2, RELION, ilastik]

### Interdigitated immunoglobulin arrays form the hyperstable surface layer of the extremophilic bacterium &lt;i&gt;Deinococcus radiodurans&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2215808120 | PMCID: PMC10120038 | PMID: 37043530
- Evidence: Tilt series alignment using patch tracking and tomogram generation was performed using IMOD ( 60 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [AlphaFold v2.2.0, ChimeraX, MotionCor2, RELION]

### A spatially resolved elemental nanodomain organization within acidocalcisomes in <i>Trypanosoma cruzi</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2300942120 | PMCID: PMC10120040 | PMID: 37036984
- Evidence: Tilt series from STEM and elemental mappings were prealigned using known structures of the sample as fiducials (i.e., center of mass of acidocalcisomes) and later manually refined using MIDAS (IMOD software package).
- Full pipeline: registration [IMOD] -> structure determination [IMOD] -> stage not stated [ImageJ]

### In situ snapshots along a mammalian selective autophagy pathway. (PNAS 2023)

- DOI: 10.1073/pnas.2221712120 | PMCID: PMC10041112 | PMID: 36917659
- Version used: **4.10.49**
- Evidence: The processed tilt series were aligned with IMOD (v4.10.49) using the patch-tracking method and reconstructed by weighted back-projection at binning 4 ( 49 ).
- Full pipeline: alignment/mapping [IMOD v4.10.49] -> registration [CTFFIND, MotionCor2] -> structure determination [IMOD v4.10.49] -> machine learning [EMAN2] -> visualisation [ChimeraX]

### Design, synthesis, and characterization of protein origami based on self-assembly of a brick and staple artificial protein pair. (PNAS 2023)

- DOI: 10.1073/pnas.2218428120 | PMCID: PMC10089216 | PMID: 36893280
- Evidence: Frames were aligned using MotionCor2 to correct for beam-induced motion and reconstruction was performed in IMOD ( 59 , 60 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> structure determination [IMOD, MotionCor2] -> stage not stated [AlphaFold, RoseTTAFold]

### Collective magnetotaxis of microbial holobionts is optimized by the three-dimensional organization and magnetic properties of ectosymbionts. (PNAS 2023)

- DOI: 10.1073/pnas.2216975120 | PMCID: PMC10013862 | PMID: 36848579
- Evidence: Tomographic reconstruction and simultaneous iterations reconstruction technique (SIRT) deconvolution were performed using IMOD.
- Full pipeline: simulation/modelling [OpenCV] -> structure determination [IMOD] -> stage not stated [ImageJ]

### Architecture of the Sap S-layer of &lt;i&gt;Bacillus anthracis&lt;/i&gt; revealed by integrative structural biology. (PNAS 2024)

- DOI: 10.1073/pnas.2415351121 | PMCID: PMC11665858 | PMID: 39652757
- Evidence: Initial CTF correction was done using defocus estimation by Gctf ( 41 ) and ctfphaseflip from IMOD ( 42 ).
- Full pipeline: alignment/mapping [VMD] -> registration [MotionCor2] -> simulation/modelling [VMD] -> structure determination [RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, GROMACS, IMOD]

### Molecular architecture of synaptic vesicles. (PNAS 2024)

- DOI: 10.1073/pnas.2407375121 | PMCID: PMC11626200 | PMID: 39602275
- Evidence: Tilt-series alignment was performed by DynamoTSA ( 79 ) and manually inspected and refined in IMOD ( 80 , 81 ), using the 10-nm or 5-nm gold fiducial markers.
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> structure determination [IMOD] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, RELION]

### Endosomal membrane budding patterns in plants. (PNAS 2024)

- DOI: 10.1073/pnas.2409407121 | PMCID: PMC11536153 | PMID: 39441629
- Evidence: Tomograms were displayed and analyzed with 3Dmod, the graphic component of the Image Modeler (IMOD) software package ( 51 ).
- Full pipeline: simulation/modelling [LAMMPS] -> visualisation [LAMMPS] -> stage not stated [IMOD]

### Dramatic changes in mitochondrial subcellular location and morphology accompany activation of the CO&lt;sub&gt;2&lt;/sub&gt; concentrating mechanism. (PNAS 2024)

- DOI: 10.1073/pnas.2407548121 | PMCID: PMC11513932 | PMID: 39405346
- Evidence: Tomograms were generated using IMOD software ( 71 ) followed by segmentation and visualization using EMAN2 ( 72 ) and USCF Chimera ( 73 ).
- Full pipeline: visualisation [EMAN2, IMOD]

### Structural basis for surface activation of the classical complement cascade by the short pentraxin C-reactive protein. (PNAS 2024)

- DOI: 10.1073/pnas.2404542121 | PMCID: PMC11406272 | PMID: 39240968
- Version used: **4.11**
- Evidence: Raw frames were aligned using the “alignframes” command from IMOD (version 4.11) ( 71 ).
- Full pipeline: alignment/mapping [IMOD v4.11] -> simulation/modelling [ChimeraX] -> stage not stated [EMAN2 v2.91]

### The dynamic behavior of chromatophores marks the transition from bands to spots in leopard geckos. (PNAS 2024)

- DOI: 10.1073/pnas.2400486121 | PMCID: PMC11260152 | PMID: 38976731
- Evidence: Large montage alignments were performed using Blendmont command-line from IMOD software ( 54 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> stage not stated [InterProScan, R, SAMtools v1.9, Seurat v4.2.0, VCFtools v0.1.16, ggplot2, pheatmap, scDblFinder v1.12.0]

### Nanoscale architecture of synaptic vesicles and scaffolding complexes revealed by cryo-electron tomography. (PNAS 2024)

- DOI: 10.1073/pnas.2403136121 | PMCID: PMC11228483 | PMID: 38923992
- Evidence: Tilt-series stacks were aligned in IMOD using surface contamination features as fiducial markers ( 81 ).
- Full pipeline: quality control [IMOD] -> alignment/mapping [IMOD] -> machine learning [EMAN2] -> visualisation [ChimeraX] -> stage not stated [Python]

### The <i>GPAT4</i>/<i>6</i>/<i>8</i> clade functions in Arabidopsis root suberization nonredundantly with the <i>GPAT5/7</i> clade required for suberin lamellae. (PNAS 2024)

- DOI: 10.1073/pnas.2314570121 | PMCID: PMC11127019 | PMID: 38739804
- Evidence: Panoramas were aligned with the software IMOD ( 56 ).
- Full pipeline: alignment/mapping [IMOD]

### An aldehyde-crosslinking mitochondrial probe for STED imaging in fixed cells. (PNAS 2024)

- DOI: 10.1073/pnas.2317703121 | PMCID: PMC11087744 | PMID: 38687792
- Evidence: Tomograms of 300 nm thick sections were generated using SerialEM ( 57 ) and IMOD ( 58 ).
- Full pipeline: stage not stated [IMOD]

### Episymbiotic Saccharibacteria TM7x modulates the susceptibility of its host bacteria to phage infection and promotes their coexistence. (PNAS 2024)

- DOI: 10.1073/pnas.2319790121 | PMCID: PMC11032452 | PMID: 38593079
- Evidence: All recorded images were first drift corrected by the software MotionCor2 ( 59 ) and then stacked by the software package IMOD ( 60 ).
- Full pipeline: quantification [HTSeq v0.9.1] -> differential/statistical testing [HTSeq v0.9.1] -> stage not stated [IMOD, ImageJ, MotionCor2]

### NKS1/ELMO4 is an integral protein of a pectin synthesis protein complex and maintains Golgi morphology and cell adhesion in <i>Arabidopsis</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2321759121 | PMCID: PMC11009649 | PMID: 38579009
- Evidence: Tomograms were aligned, reconstructed, and modeled in Etomo and IMOD ( 95 ).
- Full pipeline: read trimming [AlphaFold] -> alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [TrackMate]

### Elimination of virus-like particles reduces protein aggregation and extends replicative lifespan in <i>Saccharomyces cerevisiae</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313538121 | PMCID: PMC10998562 | PMID: 38527193
- Evidence: The resulting micrographs were then aligned and analyzed with IMOD ( 78 ) to create 3D reconstructions of organelles and the localization of the gold particles to visualize protein aggregates.
- Full pipeline: alignment/mapping [IMOD] -> quantification [Fiji, ImageJ] -> structure determination [IMOD] -> visualisation [IMOD]

### Structure of mavacamten-free human cardiac thick filaments within the sarcomere by cryoelectron tomography. (PNAS 2024)

- DOI: 10.1073/pnas.2311883121 | PMCID: PMC10907299 | PMID: 38386705
- Evidence: Tilt series were fiducial-free aligned and tomograms calculated by simultaneous iterative reconstruction technique (SIRT) using IMOD and EMAN2 ( 83 , 84 ).
- Full pipeline: alignment/mapping [EMAN2, IMOD] -> registration [MotionCor2] -> structure determination [EMAN2, IMOD] -> stage not stated [CTFFIND]

### Dysregulated inter-mitochondrial crosstalk in glioblastoma cells revealed by in situ cryo-electron tomography. (PNAS 2024)

- DOI: 10.1073/pnas.2311160121 | PMCID: PMC10907319 | PMID: 38377189
- Evidence: Tilt series were acquired at a 3° interval from − 60° to +60° and aligned and reconstructed using IMOD ( 79 , 80 ), followed by binning by two in EMAN2 ( 81 ) and denoising using the nonlinear anisotropic diffusion tool in IMOD ( 82 ).
- Full pipeline: alignment/mapping [EMAN2, IMOD] -> structure determination [EMAN2, IMOD]

### Filament structure and subcellular organization of the bacterial intermediate filament-like protein crescentin. (PNAS 2024)

- DOI: 10.1073/pnas.2309984121 | PMCID: PMC10873595 | PMID: 38324567
- Evidence: Tilt series were aligned automatically using Batchruntomo in IMOD ( 69 , 70 ), and tomograms were reconstructed using the SIRT algorithm in TOMO3D ( 71 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [IMOD, PHENIX] -> machine learning [Topaz] -> stage not stated [Coot, ImageJ, MotionCor2, RELION v3.1]

### Graphene sandwich-based biological specimen preparation for cryo-EM analysis. (PNAS 2024)

- DOI: 10.1073/pnas.2309384121 | PMCID: PMC10835136 | PMID: 38252835
- Evidence: The beam-induced motion was corrected using MotionCor2 ( 5 ), and the tilt series were subsequently imported into IMOD ( 59 ) for alignment and tomogram reconstruction.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD, RELION] -> stage not stated [MotionCor2]

### The subcellular architecture of &lt;i&gt;Paratrypanosoma confusum&lt;/i&gt; revealed by CryoET: A window into early trypanosome evolution. (PNAS 2025)

- DOI: 10.1073/pnas.2521233122 | PMCID: PMC12718327 | PMID: 41359853
- Evidence: Tilt series were aligned with AreTomo (version 1.3.3) ( 62 ) and reconstructed with IMOD ( 63 ) (version 4.11.25) using the weighted back-projection algorithm.
- Full pipeline: alignment/mapping [IMOD] -> registration [MotionCor2 v1.4.7] -> structure determination [IMOD]

### S-cone-specific circuitry in the outer plexiform layer of a cone-dominant mammal. (PNAS 2025)

- DOI: 10.1073/pnas.2504954122 | PMCID: PMC12674004 | PMID: 41325528
- Evidence: Image alignment was performed using the Etomo utility of IMOD ( https://bio3d.colorado.edu/imod/ ), and manual volumetric reconstructions were performed in IMOD and Reconstruct ( https://synapseweb.clm.utexas.edu/ ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [Cellpose, ImageJ]

### Dimeric gold nanoparticles enable multiplexed labeling in cryoelectron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2524034122 | PMCID: PMC12685141 | PMID: 41284882
- Evidence: Cryo-ET tilt series were acquired on a Titan Krios at 300 kV and reconstructed using both AreTomo ( 38 ) and IMOD ( 39 ) pipelines, with final tomograms at 10 Å pixel size.
- Full pipeline: structure determination [AlphaFold, IMOD] -> stage not stated [Python]

### Morphological specializations of mosquito CO&lt;sub&gt;2&lt;/sub&gt;-sensing olfactory receptor neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2514666122 | PMCID: PMC12582328 | PMID: 41129220
- Evidence: After data collection, the images were converted to MRC format, and rigid alignment of the image slices was performed using cross-correlation in the IMOD image processing package ( https://bio3d.colorado.edu/imod/ ).
- Full pipeline: alignment/mapping [IMOD] -> machine learning [R] -> visualisation [tidyverse] -> stage not stated [ImageJ, SciPy, Stan]

### In situ structures of the &lt;i&gt;Legionella&lt;/i&gt; Dot/Icm T4SS identify the DotA-IcmX complex as the gatekeeper for effector translocation. (PNAS 2025)

- DOI: 10.1073/pnas.2516300122 | PMCID: PMC12501162 | PMID: 40986344
- Evidence: Recorded images were initially motion-corrected using MotionCorr2 ( 61 ) and subsequently stacked by IMOD ( 62 ).
- Full pipeline: alignment/mapping [PHENIX v1.21] -> structure determination [CTFFIND, ChimeraX, PHENIX v1.21] -> stage not stated [AlphaFold, Coot v0.8.9.1, IMOD, RELION v3.1]

### Capturing the native structure of membrane proteins using vesicles. (PNAS 2025)

- DOI: 10.1073/pnas.2423407122 | PMCID: PMC12435220 | PMID: 40901875
- Evidence: The tilt series were subsequently transferred into Etomo ( 75 ) of IMOD for image alignment and tomogram reconstruction.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> machine learning [EMAN2] -> stage not stated [ChimeraX, Topaz, UCSF Chimera]

### Structure of the virulence-associated &lt;i&gt;Neisseria meningitidis&lt;/i&gt; filamentous bacteriophage MDAΦ. (PNAS 2025)

- DOI: 10.1073/pnas.2420157122 | PMCID: PMC12207478 | PMID: 40540604
- Evidence: Tomograms were reconstructed using the etomo package implemented in IMOD ( 49 ) using patch tracking and SIRT, or using SART as implemented in AreTomo ( 50 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION, Topaz]

### Structure and organization of full-length epidermal growth factor receptor in extracellular vesicles by cryo-electron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2424678122 | PMCID: PMC12167996 | PMID: 40455995
- Evidence: After poor-quality tilt images were excluded, the tilt series stacks were aligned automatically with the 10-nm fiducials, an IMOD ( 81 ) function adapted within RELION5.
- Full pipeline: read trimming [edgeR] -> alignment/mapping [IMOD] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX] -> visualisation [EMAN2] -> stage not stated [AlphaFold, ImageJ, MotionCor2, RELION]

### Microtubule dynamics are defined by conformations and stability of clustered protofilaments. (PNAS 2025)

- DOI: 10.1073/pnas.2424263122 | PMCID: PMC12146719 | PMID: 40440074
- Evidence: Tomograms were reconstructed and denoised as described previously, ( 55 , 73 ) using tomograms generated with even and odd frames after alignment with MotionCor2, ( 83 ) and tilt series alignment and back projection performed in IMOD ( 84 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> simulation/modelling [GROMACS, VMD] -> structure determination [IMOD, MotionCor2] -> visualisation [VMD] -> stage not stated [Matplotlib v3.8.2, NumPy v1.26, Python v3.9, SciPy v1.11, seaborn v0.13]

### Specialized molecular pathways drive the formation of light-scattering assemblies in leucophores. (PNAS 2025)

- DOI: 10.1073/pnas.2424979122 | PMCID: PMC12146710 | PMID: 40434648
- Evidence: Alignment and reconstruction of the tilt series images were conducted using IMOD ( 71 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> structure determination [IMOD] -> stage not stated [Seurat v4.3.0]

### Engineering spin coherence in core-shell diamond nanocrystals. (PNAS 2025)

- DOI: 10.1073/pnas.2422542122 | PMCID: PMC12130875 | PMID: 40397672
- Evidence: I.G. and D.V.T. acknowledge support by the NSF under Grant DMR-2019444 (IMOD and NSF-STC).
- Full pipeline: stage not stated [IMOD, ImageJ]

### FlgY, PflA, and PflB form a spoke-ring network in the high-torque flagellar motor of &lt;i&gt;Helicobacter pylori&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2421632122 | PMCID: PMC12054838 | PMID: 40261933
- Evidence: IMOD software was used to create image stacks and align images in each tilt series by tracking fiducial gold beads ( 55 , 56 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [ChimeraX] -> stage not stated [AlphaFold, CTFFIND]

### Intraflagellar transport trains can switch rails and move along multiple microtubules in intact primary cilia. (PNAS 2025)

- DOI: 10.1073/pnas.2413968122 | PMCID: PMC12037007 | PMID: 40249775
- Evidence: The image frames of the tilt series were processed and combined with the unblur program and IMOD program ( 39 – 42 ).
- Full pipeline: stage not stated [IMOD, UCSF Chimera]

### Virion-associated influenza hemagglutinin clusters upon sialic acid binding visualized by cryoelectron tomography. (PNAS 2025)

- DOI: 10.1073/pnas.2426427122 | PMCID: PMC12037027 | PMID: 40244672
- Evidence: Dose-weighted tilt series were exported from Warp and imported into IMOD for batched fiducial-based tilt series alignment ( 35 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UCSF Chimera] -> structure determination [PHENIX] -> machine learning [EMAN2] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Matplotlib, Python, RELION, seaborn]

### Microtubule inner proteins of &lt;i&gt;Plasmodium&lt;/i&gt; are essential for transmission of malaria parasites. (PNAS 2025)

- DOI: 10.1073/pnas.2421737122 | PMCID: PMC11831158 | PMID: 39908102
- Evidence: Single images were analyzed with FIJI in a blinded fashion (Version 1.53q), while tilt-series were reconstructed and concatenated using IMOD ( 66 ).
- Full pipeline: structure determination [IMOD]

### Cyanobacteria and Chloroflexota cooperate to structure light-responsive biofilms. (PNAS 2025)

- DOI: 10.1073/pnas.2423574122 | PMCID: PMC11804611 | PMID: 39879238
- Version used: **4.11.12**
- Evidence: Images were binned 4× for visualization, and ultrastructure measurements were performed using IMOD 4.11.12 ( 75 ) or FIJI ( 70 ).
- Full pipeline: visualisation [IMOD v4.11.12] -> stage not stated [ImageJ, R v4.3.1]

### Tetrameric PilZ protein stabilizes stator ring in complex flagellar motor and is required for motility in &lt;i&gt;Campylobacter jejuni&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2412594121 | PMCID: PMC11725899 | PMID: 39793078
- Evidence: IMOD software was used to create image stacks and align all images in each tilt series by tracking with fiducial beads ( 67 , 68 ).
- Full pipeline: alignment/mapping [CTFFIND, IMOD] -> structure determination [ChimeraX] -> stage not stated [AlphaFold, ColabFold, MotionCor2]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Evidence: All measurements were performed using the IMOD software ( 105 ).
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### SUN5 forms a regular protein lattice reinforcing the sperm head-tail junction. (PNAS 2026)

- DOI: 10.1073/pnas.2520626123 | PMCID: PMC13012075 | PMID: 41855266
- Version used: **4.12.62**
- Evidence: For mouse and boar sperm frames were aligned on-the-fly using WARP and tomograms were reconstructed using IMOD 4.12.62 by weighted backprojection and CTF-corrected using ctfphaseflip ( 63 , 64 ).
- Full pipeline: alignment/mapping [IMOD v4.12.62, RELION v5.0] -> structure determination [IMOD v4.12.62] -> stage not stated [AlphaFold, ChimeraX]

### Synaptic transmission: Munc13 assembles onto PI(4,5)P&lt;sub&gt;2&lt;/sub&gt;-rich domains into trimers that cooperate to capture vesicles. (PNAS 2026)

- DOI: 10.1073/pnas.2523347123 | PMCID: PMC12912961 | PMID: 41671179
- Evidence: The collected tilt movies were first subjected to motion correction using MOTIONCOR2 ( 43 ) and then assembled into drift-corrected stack files using alignframes from the IMOD software package ( 44 ).
- Full pipeline: alignment/mapping [IMOD] -> quantification [ImageJ] -> registration [IMOD] -> dimensionality reduction/clustering [ImageJ] -> simulation/modelling [GROMACS] -> visualisation [Topaz] -> stage not stated [AlphaFold, VMD]

### Ciliopathy patient variants reveal organelle-specific functions for TUBB4B in axonemal microtubules. (Science 2024)

- DOI: 10.1126/science.adf5489 | PMCID: PMC7616230 | PMID: 38662826
- Evidence: The tilt series were aligned and reconstructed using IMOD ( 62 ).
- Full pipeline: alignment/mapping [IMOD, UCSF Chimera] -> quantification [ImageJ, Seurat, ilastik] -> dimensionality reduction/clustering [RELION] -> differential/statistical testing [RELION] -> structure determination [ChimeraX, IMOD, PHENIX, RELION] -> visualisation [ImageJ, ilastik] -> stage not stated [VEP]

### Native architecture of a human GBP1 defense complex for cell-autonomous immunity to infection. (Science 2024)

- DOI: 10.1126/science.abm9903 | PMCID: PMC12091997 | PMID: 38422126
- Evidence: Stack files were aligned using patch-tracking function of IMOD.
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [EMAN2, UCSF Chimera] -> stage not stated [AlphaFold, CellProfiler, ImageJ]

