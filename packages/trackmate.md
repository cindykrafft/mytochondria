# TrackMate

- **Category:** imaging
- **Papers in survey:** 68
- **Journals:** PNAS (46), Nature (15), Cell (6), Science (1)
- **Years:** 2021 (7), 2022 (9), 2023 (13), 2024 (13), 2025 (18), 2026 (8)
- **Versions named:** 6.0.1 (1), 6.0.3 (1)
- **Pipeline stages it appears in:** simulation/modelling (8), quantification (5), dimensionality reduction/clustering (2), machine learning (1)

## Papers

### Parental genome unification is highly error-prone in mammalian embryos. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.013 | PMCID: PMC8162515 | PMID: 33964210
- Evidence: For each zygote, we tracked the pronuclei using TrackMate ( Tinevez et al., 2017 ) and registered the images along the pronuclei axis.
- Full pipeline: differential/statistical testing [R] -> machine learning [StarDist] -> stage not stated [ImageJ, QuPath v0.2.3, TrackMate]

### The molecular basis for sarcomere organization in vertebrate skeletal muscle. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.047 | PMCID: PMC8054911 | PMID: 33765442
- Evidence: ...ps://bio3d.colorado.edu/PEET/ ISAC Yang et al., 2012 http://sphire.mpg.de/wiki/doku.php?id=gpu_isac SPHIRE Moriya et al., 2017 https://sphire.mpg.de/ TrackMate plug-in in Fiji Tinevez et al., 2017 https://imagej.net/TrackMate Fiji (ImageJ) Schindelin et al., 2012 ; Schneider et al., 2012 https://imagej.net/Fiji TEMPy Farabella et al., 2015 http://tempy.ismb.lon.ac.uk/ SWISS-MODEL Bertoni et al., 2...
- Full pipeline: visualisation [R] -> stage not stated [EMAN2, Fiji, IMOD, ImageJ, RELION, TrackMate]

### G3BPs tether the TSC complex to lysosomes and suppress mTORC1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.024 | PMCID: PMC7868890 | PMID: 33497611
- Evidence: (2019) https://github.com/MolecularBioinformatics/Phylogenetic-analysis RStudio RStudio RRID: SCR_000432 ; https://rstudio.com/products/rstudio/download/ Tecan i-control software version 1.10.4.0 Tecan https://lifesciences.tecan.de/plate_readers/infinite_200_pro?p=tab-3 TrackMate Tinevez et al.
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CellProfiler, RSEM] -> visualisation [Clustal Omega] -> stage not stated [BCFtools, BLAST, ImageJ v1.50b, MACS2, Python, R, SAMtools, TrackMate]

### Cyclin E-induced replicative stress drives p53-dependent whole-genome duplication. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.036 | PMCID: PMC7619399 | PMID: 36681079
- Evidence: ...FlowJo 10.8 FlowJo, LLC https://www.flowjo.com/ MATLAB Mathworks https://www.mathworks.com/ ImageJ 1.53 NIH RRID:SCR_001935 FIJI NIH RRID: SCR_002285 TrackMate plugin for FIJI Tinevez et al.
- Full pipeline: stage not stated [ImageJ v1.53, TrackMate]

### Structural and functional map for forelimb movement phases between cortex and medulla. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.009 | PMCID: PMC9842395 | PMID: 36608651
- Version used: **6.0.3**
- Evidence: ...tplane.com/imaris/imaris RRID:SCR_007370 Bonsai (v2.3) NeuroGEARS Ltd. https://bonsai-rx.org RRID:SCR_017218 Fiji Fiji http://fiji.sc RRID:SCR_002285 TrackMate (v6.0.3) TrackMate https://imagej.net/plugins/trackmate/ Kilosort v2 Cortex lab https://github.com/MouseLand/Kilosort/releases/tag/v2.0 Kilosort v3 Cortex lab https://github.com/MouseLand/Kilosort Phy2 Cortex lab https://github.com/cortex-l...
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [DeepLabCut, Kilosort, Python v3.7, SciPy, TrackMate v6.0.3, scikit-learn]

### Human inherited CCR2 deficiency underlies progressive polycystic lung disease. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.036 | PMCID: PMC10842692 | PMID: 38157855
- Evidence: Images were processed with ImageJ and single-cell trajectories were obtained with TrackMate.
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, Seurat] -> quantification [ComplexHeatmap] -> normalisation [ComplexHeatmap, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [ImageJ, TrackMate] -> stage not stated [MACS2, ggplot2, scDblFinder]

### Actin cables and comet tails organize mitochondrial networks in mitosis. (Nature 2021)

- DOI: 10.1038/s41586-021-03309-5 | PMCID: PMC7990722 | PMID: 33658713
- Evidence: Mitochondria Tracking: Mitochondria trajectories were generated using a semiautomated tracking workflow in the TrackMate 45 Fiji plugin.
- Full pipeline: simulation/modelling [TrackMate] -> stage not stated [ImageJ, ilastik]

### Extracellular fluid viscosity enhances cell migration and cancer dissemination. (Nature 2022)

- DOI: 10.1038/s41586-022-05394-6 | PMCID: PMC9646524 | PMID: 36323783
- Evidence: Cancer cells were tracked in 3D in registered images for up to 12 h from the registered image stacks using the TrackMate plugin for ImageJ 58 .
- Full pipeline: alignment/mapping [HISAT2] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, Python v3.8, TrackMate]

### Retrograde movements determine effective stem cell numbers in the intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-04962-0 | PMCID: PMC7614894 | PMID: 35831497
- Evidence: Processing of in vitro migration data TrackMate plugin (Imagej version 2.3.0) 29 , 32 was used to unbiasedly track the location of individual cells over time (estimated object diameter = 10 μm, linking max distance = 45 um, gap closing max distance = 15 um, gap closing max frame gap = 1).
- Full pipeline: read trimming [STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> differential/statistical testing [Bioconductor v3.14, R v4.1.1] -> stage not stated [ImageJ, NumPy v1.19.5, Python v3.10, TrackMate]

### Nonlinear control of transcription through enhancer-promoter interactions. (Nature 2022)

- DOI: 10.1038/s41586-022-04570-y | PMCID: PMC9021019 | PMID: 35418676
- Evidence: Spot detection is based on the Laplacian of Gaussian method implemented in TrackMate 56 .
- Full pipeline: alignment/mapping [BWA, Bowtie2, Cutadapt, SAMtools, minimap2 v2.17] -> quantification [Bioconductor] -> stage not stated [R, Snakemake, TrackMate]

### A quantitative map of nuclear pore assembly reveals two distinct mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-022-05528-w | PMCID: PMC9849139 | PMID: 36599981
- Evidence: Detection of central peak positions for individual NPCs was carried out with the plugin TrackMate 41 , using DoG detector and adjusting the detection threshold as the spot diameter size.
- Full pipeline: quantification [ImageJ] -> visualisation [ChimeraX] -> stage not stated [R v3.4, TrackMate]

### Motion of VAPB molecules reveals ER-mitochondria contact site subdomains. (Nature 2024)

- DOI: 10.1038/s41586-023-06956-y | PMCID: PMC10830423 | PMID: 38267577
- Evidence: Trajectories were assembled from single-molecule images using the TrackMate plugin in Fiji 63 , 64 .
- Full pipeline: simulation/modelling [TrackMate]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: Image analysis Images were analysed using CellProfiler 70 , TrackMate 71 and MATLAB v.R2021b and R2023b (MathWorks).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: Tracking of the first 8 h of migration was performed with the TrackMate plugin from Fiji (v7.10.2) and custom-made scripts 62 .
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Overlapping nuclear import and export paths unveiled by two-colour MINFLUX. (Nature 2025)

- DOI: 10.1038/s41586-025-08738-0 | PMCID: PMC12003200 | PMID: 40108461
- Evidence: Cargo localizations were connected using the ‘TrackMate’ plugin ( https://www.nature.com/articles/s41592-022-01507-1 ) of Fiji ( https://imagej.net/software/fiji/ ).
- Full pipeline: stage not stated [TrackMate]

### Intrinsic electrical activity drives small-cell lung cancer progression. (Nature 2025)

- DOI: 10.1038/s41586-024-08575-7 | PMCID: PMC11922742 | PMID: 39939778
- Evidence: The TrackMate plugin and Cellpose detector pretrained models cyto and cyto2 were used for automated segmentation of cells and tracking during the time lapse recorded for each field of view.
- Full pipeline: alignment/mapping [RSEM] -> machine learning [Cellpose, TrackMate] -> visualisation [QuPath v0.5.0] -> stage not stated [Enrichr, GSEA, ImageJ]

### Assembly of helper NLR resistosome clusters upon activation of a coiled-coil NLR. (Nature 2026)

- DOI: 10.1038/s41586-026-10215-1 | PMCID: PMC13043302 | PMID: 41813892
- Evidence: Fluorescent particles were detected and tracked using the TrackMate plugin in Fiji 75 .
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [R v4.3.1, ggplot2] -> differential/statistical testing [lme4] -> visualisation [Matplotlib, NumPy, PyMOL, Python v3.10, R v4.3.1, SciPy, ggplot2] -> stage not stated [AlphaFold, ImageJ, TrackMate]

### The integrated stress response promotes immune evasion through lipocalin 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10143-0 | PMCID: PMC13128482 | PMID: 41708864
- Evidence: The number of monocytes was quantified using the TrackMate plug-in in ImageJ.
- Full pipeline: quantification [HTSeq, ImageJ, RSEM, TrackMate] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python, SciPy] -> stage not stated [GSEA, Seurat]

### Single-molecule dynamics of the TRiC chaperonin system in vivo. (Nature 2026)

- DOI: 10.1038/s41586-025-10073-3 | PMCID: PMC13061604 | PMID: 41639457
- Evidence: SPT and colocalization analysis Tracking of individual particles was performed in Fiji 59 with the plugin TrackMate 60 .
- Full pipeline: alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10a] -> visualisation [AlphaFold] -> stage not stated [TrackMate]

### A mechanical ratchet drives unilateral cytokinesis. (Nature 2026)

- DOI: 10.1038/s41586-025-09915-x | PMCID: PMC12916326 | PMID: 41501469
- Evidence: The beads were tracked with TrackMate plugin in Fiji and the tracks were analysed with Python.
- Full pipeline: differential/statistical testing [SciPy] -> visualisation [SciPy] -> stage not stated [Python, TrackMate, scikit-image]

### Secretome translation shaped by lysosomes and lunapark-marked ER junctions. (Nature 2026)

- DOI: 10.1038/s41586-025-09718-0 | PMCID: PMC12727531 | PMID: 41193816
- Evidence: Single-particle tracking analysis L10A-HaloTag and mRNA tracking was performed using TrackMate software (FIJI).
- Full pipeline: read trimming [Cutadapt v2.10, STAR v2.7.5c] -> alignment/mapping [Cutadapt v2.10, STAR v2.7.5c] -> quantification [CellProfiler] -> stage not stated [DESeq2, ImageJ, TrackMate]

### Trapping or slowing the diffusion of T cell receptors at close contacts initiates T cell signaling. (PNAS 2021)

- DOI: 10.1073/pnas.2024250118 | PMCID: PMC8488633 | PMID: 34526387
- Evidence: Single-molecule TCR tracking movies were analyzed in TrackMate ( 60 ).
- Full pipeline: simulation/modelling [Python v3.8] -> stage not stated [TrackMate]

### A self-exciting point process to study multicellular spatial signaling patterns. (PNAS 2021)

- DOI: 10.1073/pnas.2026123118 | PMCID: PMC8364135 | PMID: 34362843
- Evidence: Nuclei were segmented, and Erk activity was measured for each cell over time using the cell-tracking software TrackMate ( 6 ).
- Full pipeline: stage not stated [PyTorch, TrackMate]

### The store-operated Ca<sup>2+</sup> entry complex comprises a small cluster of STIM1 associated with one Orai1 channel. (PNAS 2021)

- DOI: 10.1073/pnas.2010789118 | PMCID: PMC7958290 | PMID: 33649206
- Evidence: ( G ) Fluorescence intensity distributions ( n = 6 cells) for STIM1 puncta identified by TrackMate in TIRF footprint of entire STIM1-EGFP HeLa cells before or 5 min after adding CPA in Ca 2+ -free HBS.
- Full pipeline: stage not stated [TrackMate]

### APC couples neuronal mRNAs to multiple kinesins, EB1, and shrinking microtubule ends for bidirectional mRNA motility. (PNAS 2022)

- DOI: 10.1073/pnas.2211536119 | PMCID: PMC9897468 | PMID: 36469763
- Evidence: Motility data of RNA–protein complexes were analyzed using the TrackMate plugin ( 52 ) for Fiji ( 53 ).
- Full pipeline: stage not stated [TrackMate]

### Sharp turns and gyrotaxis modulate surface accumulation of microorganisms. (PNAS 2022)

- DOI: 10.1073/pnas.2206738119 | PMCID: PMC9586295 | PMID: 36219692
- Evidence: Cells’ trajectories were extracted from the images using the free software ImageJ ( https://imagej.nih.gov/ij/index.html ) and the plug-in unit TrackMate ( https://imagej.net/plugins/trackmate/ ) ( 44 ).
- Full pipeline: simulation/modelling [ImageJ, TrackMate] -> stage not stated [NumPy, Python v3.0]

### Coupling of microtubule bundles isolates them from local disruptions to set the structural stability of the anaphase spindle. (PNAS 2022)

- DOI: 10.1073/pnas.2204068119 | PMCID: PMC9522340 | PMID: 36122237
- Evidence: Postalignment, the following analyses were performed to analyze the motion of bundles: 1) Using TrackMate ( 46 ), PRC1-marked midzone bundles were localized and tracked in the cross-sectional midplane view of the spindle ( Fig.
- Full pipeline: stage not stated [ImageJ, TrackMate]

### Geometric trade-off between contractile force and viscous drag determines the actomyosin-based motility of a cell-sized droplet. (PNAS 2022)

- DOI: 10.1073/pnas.2121147119 | PMCID: PMC9335187 | PMID: 35857875
- Evidence: To extract the position of the beads in force-transmission microscopy, particle-tracking analysis was performed by using the Fiji plugin TrackMate ( 40 ).
- Full pipeline: stage not stated [TrackMate]

### A two-component protein condensate of the EGFR cytoplasmic tail and Grb2 regulates Ras activation by SOS at the membrane. (PNAS 2022)

- DOI: 10.1073/pnas.2122531119 | PMCID: PMC9181613 | PMID: 35507881
- Evidence: Single-molecule images of SOS FL were tracked by an ImageJ plugin, TrackMate ( 66 ), to obtain the number of activated SOS FL molecules on the membrane.
- Full pipeline: stage not stated [ImageJ, TrackMate]

### Scale-dependent tipping points of bacterial colonization resistance. (PNAS 2022)

- DOI: 10.1073/pnas.2115496119 | PMCID: PMC8851462 | PMID: 35145031
- Evidence: The displacement of cells in gaseous phases was automatically tracked with TrackMate in Fiji ( 42 ), and that in jammed phases was manually tracked with the Manual Tracking plugin of ImageJ.
- Full pipeline: stage not stated [ImageJ, TrackMate]

### A role for the Gram-negative outer membrane in bacterial shape determination. (PNAS 2023)

- DOI: 10.1073/pnas.2301987120 | PMCID: PMC10469335 | PMID: 37607228
- Version used: **6.0.1**
- Evidence: Briefly, MreB tracks were detected in TrackMate v6.0.1 ( 56 ) using a LoG detector (0.3-µm radius) and the Kalman filter.
- Full pipeline: stage not stated [TrackMate v6.0.1]

### Migration and division in cell monolayers on substrates with topological defects. (PNAS 2023)

- DOI: 10.1073/pnas.2301197120 | PMCID: PMC10372565 | PMID: 37463218
- Evidence: Cell tracking is achieved using the TrackMate plugin in ImageJ ( 77 ).
- Full pipeline: stage not stated [ImageJ, TrackMate]

### Long noncoding RNA MALAT1 is dynamically regulated in leader cells during collective cancer invasion. (PNAS 2023)

- DOI: 10.1073/pnas.2305410120 | PMCID: PMC10319025 | PMID: 37364126
- Evidence: The tracking of transcripts was processed with Fiji ImageJ plugin “TrackMate”.
- Full pipeline: stage not stated [Fiji, ImageJ, TrackMate]

### Self-organizing actin networks drive sequential endocytic protein recruitment and vesicle release on synthetic lipid bilayers. (PNAS 2023)

- DOI: 10.1073/pnas.2302622120 | PMCID: PMC10235984 | PMID: 37216532
- Evidence: To quantify vesiculation dynamics, we used the TrackMate plugin of ImageJ to manually track the position of vesicles in time-lapse data after the processing steps described in the previous paragraph.
- Full pipeline: quantification [TrackMate] -> stage not stated [ImageJ]

### Deciphering molecular mechanisms stabilizing the reovirus-binding complex. (PNAS 2023)

- DOI: 10.1073/pnas.2220741120 | PMCID: PMC10214207 | PMID: 37186838
- Evidence: Individual viruses were tracked using the TrackMate plugin, and the trajectory data were exported to Microsoft Excel for further analysis.
- Full pipeline: simulation/modelling [NAMD, TrackMate] -> stage not stated [ImageJ v1.52e, VMD]

### Antiparallel dimer structure of CELSR cadherin in solution revealed by high-speed atomic force microscopy. (PNAS 2023)

- DOI: 10.1073/pnas.2302047120 | PMCID: PMC10160967 | PMID: 37094146
- Evidence: In particular, particle tracking was performed using the TrackMate macro in Fiji ( 63 ).
- Full pipeline: read trimming [ImageJ v1.51d] -> stage not stated [TrackMate]

### Size- and position-dependent cytoplasm viscoelasticity through hydrodynamic interactions with the cell surface. (PNAS 2023)

- DOI: 10.1073/pnas.2216839120 | PMCID: PMC9992773 | PMID: 36802422
- Evidence: The position of beads and aggregates was tracked from their fluorescence signal using the TrackMate plugin in Fiji.
- Full pipeline: stage not stated [TrackMate]

### Clathrin mediates both internalization and vesicular release of triggered T cell receptor at the immunological synapse. (PNAS 2023)

- DOI: 10.1073/pnas.2211368120 | PMCID: PMC9963302 | PMID: 36730202
- Evidence: TCR microclusters were tracked using the ImageJ plugin TrackMate ( 59 ), followed by MATLAB-based analysis ( https://github.com/donFellus/loadFijiTracks ).
- Full pipeline: dimensionality reduction/clustering [ImageJ, TrackMate]

### Twist response of actin filaments. (PNAS 2023)

- DOI: 10.1073/pnas.2208536120 | PMCID: PMC9942836 | PMID: 36656858
- Evidence: The positions of the paramagnetic beads were tracked with the TrackMate plugin in ImageJ (NIH, USA) ( 78 ).
- Full pipeline: stage not stated [ImageJ, R, TrackMate]

### Robotic data acquisition with deep learning enables cell image-based prediction of transcriptomic phenotypes. (PNAS 2023)

- DOI: 10.1073/pnas.2210283120 | PMCID: PMC9910600 | PMID: 36577074
- Evidence: As a comparison, we also classified these cells into three clusters based on their morphological and dynamical features ( Datasets S7–S9 ), which were extracted from the cell images by three representative and well-used conventional image analysis software programs ( 17 ): NIS-Elements ( 18 ), CellProfiler 4 ( 17 ), and TrackMate 7 ( 19 ) in Fiji (ImageJ) ( 20 ) ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [CellProfiler, Fiji, ImageJ, TrackMate]

### Microscopic phage adsorption assay: High-throughput quantification of virus particle attachment to host bacterial cells. (PNAS 2024)

- DOI: 10.1073/pnas.2410905121 | PMCID: PMC11670125 | PMID: 39700139
- Evidence: Our algorithm is described in SI Appendix , which is equivalent to popular particle tracking programs such as trackpy in Python, and TrackMate in ImageJ/Fiji.
- Full pipeline: stage not stated [ImageJ, Python, TrackMate]

### Differential roles of kinetic on- and off-rates in T-cell receptor signal integration revealed with a modified Fab'-DNA ligand. (PNAS 2024)

- DOI: 10.1073/pnas.2406680121 | PMCID: PMC11441509 | PMID: 39298491
- Evidence: Fab’-DNA–TCR complexes and LAT condensates were identified and tracked using TrackMate ( 75 ).
- Full pipeline: stage not stated [TrackMate]

### Regulation of intercellular viscosity by E-cadherin-dependent phosphorylation of EGFR in collective cell migration. (PNAS 2024)

- DOI: 10.1073/pnas.2405560121 | PMCID: PMC11406304 | PMID: 39231206
- Evidence: Migration speeds of individual cells (N > 30) were tracked using either the TrackMate plugin for Image J on phase-contrast images or Imaris for fluorescent nucleus images.
- Full pipeline: quantification [ImageJ] -> stage not stated [Cellpose, TrackMate]

### Diffusion barriers imposed by tissue topology shape Hedgehog morphogen gradients. (PNAS 2024)

- DOI: 10.1073/pnas.2400677121 | PMCID: PMC11388384 | PMID: 39190357
- Evidence: ( Bottom ) Result of tracking with the TrackMate plugin in FIJI as described in supplemental methods.
- Full pipeline: simulation/modelling [R] -> visualisation [ggplot2] -> stage not stated [TrackMate]

### Phosphatidylinositol-3-phosphate mediates Arc capsid secretion through the multivesicular body pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2322422121 | PMCID: PMC11363301 | PMID: 39178227
- Evidence: Particles were tracked from the HILO-acquired videos using the FIJI plugin TrackMate ( 76 ) ( Software S1 ), which calculated the particle diffusion coefficient using the co-variance estimation (CVE) method ( 77 , 78 ).
- Full pipeline: stage not stated [TrackMate]

### Advanced surface passivation for high-sensitivity studies of biomolecular condensates. (PNAS 2024)

- DOI: 10.1073/pnas.2403013121 | PMCID: PMC11145189 | PMID: 38781207
- Evidence: The movies were then analyzed using TrackMate in Fiji/ImageJ.
- Full pipeline: stage not stated [Fiji, ImageJ, TrackMate]

### The cAMP signaling module regulates sperm motility in the liverwort <i>Marchantia polymorpha</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2322211121 | PMCID: PMC11032487 | PMID: 38593080
- Evidence: 1.53t (the Fiji distribution) plugin, TrackMate ver.
- Full pipeline: stage not stated [ImageJ, TrackMate]

### NKS1/ELMO4 is an integral protein of a pectin synthesis protein complex and maintains Golgi morphology and cell adhesion in <i>Arabidopsis</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2321759121 | PMCID: PMC11009649 | PMID: 38579009
- Evidence: Golgi movement was tracked using Fiji-TrackMate ( 84 ).
- Full pipeline: read trimming [AlphaFold] -> alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [TrackMate]

### Cancer-on-a-chip model shows that the adenomatous polyposis coli mutation impairs T cell engagement and killing of cancer spheroids. (PNAS 2024)

- DOI: 10.1073/pnas.2316500121 | PMCID: PMC10945811 | PMID: 38442157
- Evidence: CTLs were tracked in the Matrigel using TrackMate software ( 66 ) in ImageJ.
- Full pipeline: quantification [ImageJ] -> stage not stated [TrackMate]

### Building on-chip cytoskeletal circuits via branched microtubule networks. (PNAS 2024)

- DOI: 10.1073/pnas.2315992121 | PMCID: PMC10823238 | PMID: 38232292
- Evidence: We then used TrackMate to detect EB1 spots and obtain trajectories of MT growth using a nearest neighbor algorithm ( 65 ).
- Full pipeline: simulation/modelling [TrackMate]

### Nitric oxide promotes rapid development of motility to accelerate biofilm dispersal in &lt;i&gt;&lt;i&gt;Vibrio cholerae&lt;/i&gt;&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2526864122 | PMCID: PMC12704800 | PMID: 41329732
- Evidence: Trajectories: Examples of single-cell paths tracked using TrackMate (ImageJ).
- Full pipeline: quantification [ImageJ] -> simulation/modelling [TrackMate]

### Contractile forces direct the chiral swirling of minimal cell collectives. (PNAS 2025)

- DOI: 10.1073/pnas.2415028122 | PMCID: PMC12664006 | PMID: 41237213
- Evidence: Tracks, determined in TrackMate, are displayed on top of nuclei (Hoechst staining in white).
- Full pipeline: stage not stated [TrackMate]

### Global profiling of polyketide synthases in facultative multicellular eukaryotes. (PNAS 2025)

- DOI: 10.1073/pnas.2515852122 | PMCID: PMC12625978 | PMID: 41191498
- Evidence: TrackMate was used to track cell masks and extract individual migration paths ( 99 , 100 ).
- Full pipeline: quality control [FastQC, MultiQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> machine learning [Cellpose] -> visualisation [R, clusterProfiler] -> stage not stated [TrackMate]

### Chemical propulsion of hemozoin crystal motion in malaria parasites. (PNAS 2025)

- DOI: 10.1073/pnas.2513845122 | PMCID: PMC12595501 | PMID: 41150719
- Evidence: Single-particle tracking TrackMate We used the Fiji plugin TrackMate to single-particle track hemozoin crystals throughout time lapse images ( 68 , 69 ).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [Python, SciPy, TrackMate]

### Spatial self-organization of confined bacterial suspensions. (PNAS 2025)

- DOI: 10.1073/pnas.2503983122 | PMCID: PMC12541401 | PMID: 41052330
- Evidence: We use the Beer–Lambert law to calibrate cell concentration in the bright-field images, use particle image velocimetry (PIV) in PIVLab to measure the velocity field generated by the swimming cells, and track individual cells using the ImageJ plugin TrackMate.
- Full pipeline: stage not stated [ImageJ, TrackMate]

### Nonmuscle myosin 2 turnover in cells is synergistically controlled by the tail and the motor domain. (PNAS 2025)

- DOI: 10.1073/pnas.2511046122 | PMCID: PMC12501154 | PMID: 40996796
- Evidence: The processed images were converted to 8-bit and analyzed using the TrackMate plugin in ImageJ.
- Full pipeline: quantification [ImageJ] -> stage not stated [TrackMate]

### A model for boundary-driven tissue morphogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2505160122 | PMCID: PMC12478147 | PMID: 40966291
- Evidence: We tracked nuclei semiautomatically in Mastodon ( 54 ), a tool built on the TrackMate ( 55 , 56 ) plugin for Fiji ( 57 ).
- Full pipeline: machine learning [ilastik] -> stage not stated [TrackMate]

### Emergent depth-mechanosensing of epithelial collectives regulates cell clustering and dispersal on layered matrices. (PNAS 2025)

- DOI: 10.1073/pnas.2423875122 | PMCID: PMC12452895 | PMID: 40932776
- Evidence: ImageJ (NIH) with TrackMate 7 ( 45 ) plugin was used to analyze cell migration.
- Full pipeline: stage not stated [ImageJ, TrackMate]

### Pattern formation along signaling gradients driven by active droplet behavior of cell swarms. (PNAS 2025)

- DOI: 10.1073/pnas.2419152122 | PMCID: PMC12130873 | PMID: 40392846
- Evidence: Cell flow fields within the swarm were quantified by tracking (TrackMate: simple LAP tracker, CSVImporter) the centroids of nuclei (masked via watershed segmentation; SCF-MPI-CBG).
- Full pipeline: quantification [TrackMate]

### A responsive living material prepared by diffusion reveals extracellular enzyme activity of cyanobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2424405122 | PMCID: PMC12067278 | PMID: 40310460
- Evidence: These images were analyzed to track the movement of S. elongatus cells into the hydrogel using the open sourced TrackMate plugin for FIJI as previously demonstrated by Ershov and coworkers ( 43 , 45 , 46 ).
- Full pipeline: stage not stated [R v1.009, TrackMate]

### CD70 recruitment to the immunological synapse is dependent on CD20 in B cells. (PNAS 2025)

- DOI: 10.1073/pnas.2414002122 | PMCID: PMC12037035 | PMID: 40232798
- Evidence: Particles were tracked using the TrackMate plugin of Fiji ( 71 ), with a typical particle size of 0.35 microns squared.
- Full pipeline: stage not stated [TrackMate]

### Substrate stress relaxation regulates monolayer fluidity and leader cell formation for collectively migrating epithelia. (PNAS 2025)

- DOI: 10.1073/pnas.2417290122 | PMCID: PMC12012536 | PMID: 40203036
- Evidence: For leader cell quantification, cells extending visible lamellipodial protrusions beyond the leading edge of the monolayer were manually tracked with TrackMate ( 71 ).
- Full pipeline: quantification [ImageJ, TrackMate]

### Bacterial motility depends on a critical flagellum length and energy-optimized assembly. (PNAS 2025)

- DOI: 10.1073/pnas.2413488122 | PMCID: PMC11929379 | PMID: 40067900
- Evidence: Image analysis and tracking of cells was performed using ilastik ( 45 ) and Fiji ( 46 ) equipped with TrackMate ( 47 ).
- Full pipeline: stage not stated [ImageJ, TrackMate, ilastik]

### Co-zorbs: Motile, multispecies biofilms aid transport of diverse bacterial species. (PNAS 2025)

- DOI: 10.1073/pnas.2417327122 | PMCID: PMC11831133 | PMID: 39899715
- Evidence: Tracking of zorb and co-zorb motility in vitro was performed on 5-h timelapse movies (dt = 30 min) using the TrackMate plugin in FIJI/ImageJ ( 47 ) using the Laplacian of Gaussian object detector following preprocessing with a median filter, with estimated object diameters ranging from 40 to 100 µm, depending on each movie/species.
- Full pipeline: stage not stated [ImageJ, TrackMate]

### Amoeboid-mesenchymal transition and the proteolytic control of cancer invasion plasticity. (PNAS 2026)

- DOI: 10.1073/pnas.2520717123 | PMCID: PMC13079982 | PMID: 41961858
- Evidence: Spinning-disk confocal imaging of 4B4-treated HT1080 GFP-NLS spheroid invasion with TrackMate tracing from 1 hour post embedding to 48 hours post-embedding in acid solubilized rat tail collagen (2.2mg/ml, 37°C, pH 7.4).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [TrackMate]

### Light-activated cAMP signaling controls sodium-driven motility in &lt;i&gt;Vibrio cholerae&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2530860123 | PMCID: PMC13079933 | PMID: 41955113
- Evidence: To quantify light-dependent changes in motility, we recorded dark-field videos at 60 fps for 10 to 20 s and extracted single-cell trajectories using ImageJ TrackMate ( 24 ).
- Full pipeline: quantification [ImageJ, TrackMate] -> simulation/modelling [ImageJ, TrackMate]

### Subcellular calcium dynamics and organelle perturbations in resistosome-mediated cell death. (PNAS 2026)

- DOI: 10.1073/pnas.2523470123 | PMCID: PMC13012261 | PMID: 41849389
- Evidence: Membrane–cell wall distance was measured using the TrackMate plugin in ImageJ.
- Full pipeline: differential/statistical testing [ImageJ] -> stage not stated [TrackMate]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: The segmentation masks were then registered over timepoints in Fiji using TrackMate ( 50 ), with feature penalties for circularity, area, and GFP intensity.
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

