# Topaz

- **Category:** structbio
- **Papers in survey:** 81
- **Journals:** PNAS (35), Nature (29), Science (9), Cell (8)
- **Years:** 2021 (1), 2022 (2), 2023 (10), 2024 (25), 2025 (33), 2026 (10)
- **Versions named:** 0.2.4 (2), 0.3.0 (1), 0.2.5 (1)
- **Pipeline stages it appears in:** machine learning (27), structure determination (10), visualisation (2), registration (2), differential/statistical testing (1), normalisation (1), alignment/mapping (1), dimensionality reduction/clustering (1)

## Papers

### Structural basis for ion selectivity in potassium-selective channelrhodopsins. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.009 | PMCID: PMC7615185 | PMID: 37652010
- Evidence: Further particles were picked by Template picker and Topaz picker 94 and subjected to 2D classification followed by Heterogeneous refinement.
- Full pipeline: structure determination [AlphaFold, Coot, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Kilosort v2.5, MotionCor2, RELION v4.0, UCSF Chimera]

### TMEM106B is a receptor mediating ACE2-independent SARS-CoV-2 cell entry. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.005 | PMCID: PMC10409496 | PMID: 37421949
- Evidence: 89 Particles belonging to well-defined 2D classes were used for training particle picking using Topaz.
- Full pipeline: quantification [ImageJ] -> structure determination [Coot] -> machine learning [Topaz] -> stage not stated [AlphaFold, CTFFIND v1.06, PHENIX, RELION v4.0, UCSF Chimera]

### Structure of the endosomal Commander complex linked to Ritscher-Schinzel syndrome. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.003 | PMCID: PMC10187114 | PMID: 37172566
- Evidence: The manually picked particles were used to train Topaz 109 which is implemented within RELION.
- Full pipeline: alignment/mapping [ColabFold, MAFFT, PyMOL] -> normalisation [CCP4] -> stage not stated [AlphaFold, CTFFIND, ChimeraX, HMMER v3.3.2, PHENIX, RELION, Topaz]

### A potent pan-sarbecovirus neutralizing antibody resilient to epitope diversification. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.026 | PMCID: PMC11645210 | PMID: 39383863
- Evidence: To improve particle picking further, the Topaz picker 91 was trained on Warp-picked particle sets belonging to the selected classes after heterogeneous 3D refinement.
- Full pipeline: read trimming [BCFtools v1.10.2, BWA v0.7.17] -> differential/statistical testing [RELION, scikit-learn] -> structure determination [Coot, PHENIX, Topaz] -> machine learning [Topaz, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [OpenMM, Pangolin, Python v3.10]

### Genome integrity sensing by the broad-spectrum Hachiman antiphage defense complex. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.020 | PMCID: PMC12278908 | PMID: 39395413
- Evidence: The particles were then submitted for Topaz training, and the resulting Topaz model was used to pick particles from all 3724 micrographs, 99 giving a total of 1,322,669 particles.
- Full pipeline: alignment/mapping [AlphaFold, IQ-TREE] -> simulation/modelling [ChimeraX] -> structure determination [PHENIX v1.20.1] -> machine learning [Topaz] -> visualisation [IQ-TREE, Matplotlib, seaborn] -> stage not stated [ColabFold, MUSCLE, Python]

### Human coronavirus HKU1 recognition of the TMPRSS2 host receptor. (Cell 2024)

- DOI: 10.1016/j.cell.2024.06.006 | PMCID: PMC12854727 | PMID: 38964328
- Evidence: The particles picked using Topaz were extracted and subjected to 2D classification using cryoSPARC, which improved the number of unique 2D views.
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [RELION] -> structure determination [RELION, UCSF Chimera] -> stage not stated [PHENIX, Topaz]

### Rapid DNA unwinding accelerates genome editing by engineered CRISPR-Cas9. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.031 | PMCID: PMC11658890 | PMID: 38781968
- Evidence: Particle picking was optimized using blob, template, and Topaz picking resulting in the extraction of 1,026,723 particles.
- Full pipeline: structure determination [Coot v0.9.8.7] -> stage not stated [AlphaFold, ChimeraX v1.6.1, ColabFold, PHENIX v1.19.2, Python, Topaz, fastp]

### Multiple independent acquisitions of ACE2 usage in MERS-related coronaviruses. (Cell 2025)

- DOI: 10.1016/j.cell.2024.12.031 | PMCID: PMC12360793 | PMID: 39922191
- Evidence: The particles picked using Topaz were extracted and subjected to 2D classification using cryoSPARC, which improved the number of unique 2D views.
- Full pipeline: alignment/mapping [Clustal Omega] -> differential/statistical testing [RELION] -> structure determination [IQ-TREE, RELION, UCSF Chimera] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, PHENIX, Topaz]

### Structure and inhibition mechanism of the human citrate transporter NaCT. (Nature 2021)

- DOI: 10.1038/s41586-021-03230-x | PMCID: PMC7933130 | PMID: 33597751
- Evidence: Initial particle picks from the 20º micrographs were used as templates for repicking using Topaz 57 , yielding 1,151,799 particles from all micrographs.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL] -> stage not stated [MotionCor2, Topaz]

### Mechanism of replication origin melting nucleated by CMG helicase assembly. (Nature 2022)

- DOI: 10.1038/s41586-022-04829-4 | PMCID: PMC9242855 | PMID: 35705812
- Evidence: 26 ) and used as a training dataset for Topaz training 53 .
- Full pipeline: structure determination [Coot v0.9.1] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL, UCSF Chimera] -> stage not stated [CTFFIND, PHENIX, RELION]

### Structural insights into intron catalysis and dynamics during splicing. (Nature 2023)

- DOI: 10.1038/s41586-023-06746-6 | PMCID: PMC10733145 | PMID: 37993708
- Evidence: Topaz picking yielded 1,289,915 particles which were subject to three rounds of 2D classification, leaving 847,534 particles which were extracted with a box size of 384 × 384 pixels.
- Full pipeline: structure determination [ChimeraX v1.2.5, PHENIX v1.20.1, UCSF Chimera] -> stage not stated [PyMOL v2.6.0, Topaz]

### Structure and function of the RAD51B-RAD51C-RAD51D-XRCC2 tumour suppressor. (Nature 2023)

- DOI: 10.1038/s41586-023-06179-1 | PMCID: PMC7614784 | PMID: 37344587
- Evidence: Particles were picked automatically using Topaz 69 from the non-tilt dataset, extracted (FOM = -1), yielding 4,603,811 particles that were iteratively 2D and 3D classified, leading to an initial 3D model.
- Full pipeline: alignment/mapping [ChimeraX] -> machine learning [RELION v3.1] -> stage not stated [AlphaFold, Fiji, ImageJ, PHENIX, Topaz]

### Genome expansion by a CRISPR trimmer-integrase. (Nature 2023)

- DOI: 10.1038/s41586-023-06178-2 | PMCID: PMC10284694 | PMID: 37316664
- Evidence: In the first round, 569 particles were picked manually from 37 micrographs and submitted for Topaz training 45 .
- Full pipeline: structure determination [AlphaFold, Coot v0.9.4.1, PHENIX v1.19.2] -> machine learning [Topaz] -> stage not stated [ChimeraX, HMMER]

### MCM double hexamer loading visualized with human proteins. (Nature 2024)

- DOI: 10.1038/s41586-024-08263-6 | PMCID: PMC11634765 | PMID: 39604733
- Version used: **0.2.5**
- Evidence: Particles were picked using Topaz v0.2.5 48 .
- Full pipeline: differential/statistical testing [AlphaFold] -> structure determination [AlphaFold, Coot v0.9.8.1, PHENIX v1.21] -> stage not stated [CTFFIND v1.06, ChimeraX v1.6.1, RELION, Topaz v0.2.5]

### Molecular architecture of coronavirus double-membrane vesicle pore complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07817-y | PMCID: PMC11374677 | PMID: 39143215
- Evidence: Tomograms were denoised using Topaz 42 for better visualization.
- Full pipeline: alignment/mapping [Python] -> structure determination [ChimeraX, Coot, RELION] -> visualisation [Topaz] -> stage not stated [AlphaFold, IMOD]

### Structural basis for transthiolation intermediates in the ubiquitin pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07828-9 | PMCID: PMC11374688 | PMID: 39143218
- Evidence: Subsequent steps were performed in cryoSPARC 4.0.2 59 with the exception of particle picking using Topaz 60 and Bayesian polishing performed in RELION 3.1 61 .
- Full pipeline: alignment/mapping [MotionCor2] -> normalisation [MotionCor2] -> differential/statistical testing [Topaz] -> structure determination [Coot, PHENIX, UCSF Chimera] -> visualisation [IMOD v4.11] -> stage not stated [CTFFIND, ChimeraX, RELION v3.1]

### Molecular basis for transposase activation by a dedicated AAA+ ATPase. (Nature 2024)

- DOI: 10.1038/s41586-024-07550-6 | PMCID: PMC11208146 | PMID: 38926614
- Evidence: Micrographs were picked using Topaz and subjected to 2D classification using RELION-4.0 (refs.
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX v1.5] -> stage not stated [CCP4, CTFFIND v4.1, RELION, Topaz]

### Structure and topography of the synaptic V-ATPase-synaptophysin complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07610-x | PMCID: PMC11269182 | PMID: 38838737
- Evidence: Using this training set, Topaz picked 33,094 particles from 4,404 micrographs.
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [AlphaFold, PHENIX v1.21] -> machine learning [RELION, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Coot, Python, SciPy, UCSF Chimera]

### Structural basis for pegRNA-guided reverse transcription by a prime editor. (Nature 2024)

- DOI: 10.1038/s41586-024-07497-8 | PMCID: PMC11222144 | PMID: 38811740
- Evidence: For the termination complex, 1,112,419 particles were selected using a Topaz picking model from the 4,363 motion-corrected and dose-weighted micrographs, and extracted at a pixel size of 3.32 Å.
- Full pipeline: registration [MotionCor2] -> stage not stated [AlphaFold, ChimeraX, PHENIX, RELION v3.1.1, Topaz]

### Streptomyces umbrella toxin particles block hyphal growth of competing species. (Nature 2024)

- DOI: 10.1038/s41586-024-07298-z | PMCID: PMC11062931 | PMID: 38632398
- Evidence: To further improve particle picking, we trained the Topaz picker on Warp-picked particle sets belonging to the selected classes after heterogeneous 3D refinement.
- Full pipeline: alignment/mapping [ColabFold] -> structure determination [Coot, Topaz] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, Python, RELION, RoseTTAFold, napari]

### Emergence of fractal geometries in the evolution of a metabolic enzyme. (Nature 2024)

- DOI: 10.1038/s41586-024-07287-2 | PMCID: PMC11041685 | PMID: 38600380
- Evidence: A Topaz particle picking model was generated by running several rounds of Topaz train and Topaz extract from an initial set of 150 manually picked particles.
- Full pipeline: alignment/mapping [MUSCLE v3.8.31, MotionCor2] -> normalisation [RELION v3.1] -> simulation/modelling [GROMACS v2022.2] -> structure determination [MUSCLE v3.8.31, PHENIX v1.19.2] -> stage not stated [PyMOL v2.5.2, Topaz, UCSF Chimera]

### Cryo-EM structures of PP2A:B55-FAM122A and PP2A:B55-ARPP19. (Nature 2024)

- DOI: 10.1038/s41586-023-06870-3 | PMCID: PMC10765524 | PMID: 38123684
- Evidence: Potential particle locations on the full micrograph set were selected using Topaz 55 using a model trained on a random subset of the micrographs.
- Full pipeline: quantification [ImageJ v1.53t] -> structure determination [Coot, PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, RELION v4.0]

### Structural basis for mTORC1 activation on the lysosomal membrane. (Nature 2025)

- DOI: 10.1038/s41586-025-09545-3 | PMCID: PMC12448111 | PMID: 40963021
- Evidence: After identifying a good particle set, it was used to train Topaz particle picking 52 .
- Full pipeline: structure determination [AlphaFold, ChimeraX, PHENIX] -> stage not stated [ImageJ, Topaz]

### Structure and mechanism of the mitochondrial calcium transporter NCLX. (Nature 2025)

- DOI: 10.1038/s41586-025-09491-0 | PMCID: PMC12571890 | PMID: 40931067
- Version used: **0.2.4**
- Evidence: Furthermore, 57,247 particles from 1,304 images were selected for Topaz (v.0.2.4) 63 training.
- Full pipeline: simulation/modelling [VMD] -> structure determination [AlphaFold, PHENIX] -> machine learning [Topaz v0.2.4] -> visualisation [ChimeraX, PyMOL, UCSF Chimera, VMD]

### Structural basis for the dynamic regulation of mTORC1 by amino acids. (Nature 2025)

- DOI: 10.1038/s41586-025-09428-7 | PMCID: PMC12507694 | PMID: 40836086
- Evidence: Motion-corrected micrographs were denoised using Topaz-Denoise 43 with pretrained models.
- Full pipeline: simulation/modelling [GROMACS, VMD] -> structure determination [AlphaFold, ChimeraX v1.8, Coot v0.9.8] -> machine learning [Topaz] -> stage not stated [CTFFIND v4.1.14, MotionCor2, PHENIX v2.0, RELION v5.0]

### Structural basis of fast N-type inactivation in K&lt;sub&gt;v&lt;/sub&gt; channels. (Nature 2025)

- DOI: 10.1038/s41586-025-09339-7 | PMCID: PMC12460158 | PMID: 40770100
- Evidence: The good classes were then used as template to pick particles from all selected micrographs using a different program (including Gautomatch, Topaz pick or Template Picker).
- Full pipeline: structure determination [AlphaFold, Coot, PHENIX, UCSF Chimera] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2, RELION, Topaz]

### Loss of FCoV-23 spike domain 0 enhances fusogenicity and entry kinetics. (Nature 2025)

- DOI: 10.1038/s41586-025-09155-z | PMCID: PMC12408340 | PMID: 40634609
- Evidence: To further improve particle picking, we trained Topaz picker 75 on the Warp-picked particles on the selected classes after 2D classification.
- Full pipeline: structure determination [PHENIX v1.21] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, Coot v0.9.8.8, RELION v5.0b, UCSF Chimera v1.8]

### Interactions between TTYH2 and APOE facilitate endosomal lipid transfer. (Nature 2025)

- DOI: 10.1038/s41586-025-09200-x | PMCID: PMC12328215 | PMID: 40562935
- Evidence: Particles picked using Topaz 56 were analysed using the same pipeline starting from 2D classification.
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, ImageJ, Python, RELION, Topaz]

### Structure of the ATP-driven methyl-coenzyme M reductase activation complex. (Nature 2025)

- DOI: 10.1038/s41586-025-08890-7 | PMCID: PMC12176620 | PMID: 40240609
- Evidence: This was followed by iterative rounds of Topaz training to generate a model that was used to select particles from all micrographs.
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [Coot v0.9.8.92, PHENIX v1.21] -> machine learning [Topaz] -> visualisation [ChimeraX v1.6.1] -> stage not stated [AlphaFold, IQ-TREE, UCSF Chimera v1.17.3]

### Structural dynamics of DNA unwinding by a replicative helicase. (Nature 2025)

- DOI: 10.1038/s41586-025-08766-w | PMCID: PMC12043514 | PMID: 40108462
- Version used: **0.3.0**
- Evidence: The micrographs were denoised before picking with Topaz v.0.3.0 (ref.
- Full pipeline: structure determination [ChimeraX] -> visualisation [PHENIX, PyMOL v2.6.0, UCSF Chimera] -> stage not stated [AlphaFold, CTFFIND v4.1, MotionCor2, RELION, Topaz v0.3.0]

### Converging mechanism of UM171 and KBTBD4 neomorphic cancer mutations. (Nature 2025)

- DOI: 10.1038/s41586-024-08533-3 | PMCID: PMC11882451 | PMID: 39939763
- Evidence: Topaz picker was used to pick more particles for a second round ab initio construction and refinements to achieve further resolution improvement.
- Full pipeline: differential/statistical testing [R, limma] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1, Topaz] -> visualisation [Cytoscape v3.5.10, PyMOL] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, STRING db, ggplot2 v3.5.0, pandas v1.5.1]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Evidence: After two rounds of cleaning by 2D classification, 340,735 particles were selected and subjected to Topaz picking.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### Molecular basis for methylation-sensitive editing by Cas9. (Nature 2026)

- DOI: 10.1038/s41586-026-10384-z | PMCID: PMC13216068 | PMID: 41986708
- Evidence: A total of 6,080 micrographs were collected and 2,516,939 particles were picked using Topaz 62 , followed by multiple rounds of 2D classification using cryoSPARC 63 , resulting in 2,015,088 good particles for 3D classification.
- Full pipeline: registration [CTFFIND] -> differential/statistical testing [Python, R] -> structure determination [PHENIX, RELION v4.0] -> stage not stated [Topaz]

### Structural basis of supercoiling-induced CRISPR-Cas9 off-target activity. (Nature 2026)

- DOI: 10.1038/s41586-026-10255-7 | PMCID: PMC13171457 | PMID: 41882360
- Evidence: On-the-fly processing was performed where particles were picked automatically with Topaz 68 and 2D classification was performed.
- Full pipeline: structure determination [ChimeraX, Coot, PHENIX, RELION] -> stage not stated [AlphaFold, Fiji, ImageJ, Topaz]

### Integrase anchors viral RNA to the HIV-1 capsid interior. (Nature 2026)

- DOI: 10.1038/s41586-026-10154-x | PMCID: PMC13102720 | PMID: 41708858
- Evidence: Particles belonging to well-defined 2D classes were used to train a model for particle picking in Topaz 56 .
- Full pipeline: alignment/mapping [IMOD, MotionCor2 v1.4.0, RELION] -> normalisation [ImageJ, NAMD v3.0.1] -> simulation/modelling [VMD] -> structure determination [ChimeraX, Coot, IMOD] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, PyMOL, Topaz, UCSF Chimera]

### CSN5i-3 is an orthosteric molecular glue inhibitor of COP9 signalosome. (Nature 2026)

- DOI: 10.1038/s41586-026-10129-y | PMCID: PMC13128448 | PMID: 41673158
- Evidence: Particles of good reconstructions were used as template to train model for Topaz picking 36 .
- Full pipeline: structure determination [PHENIX, Topaz] -> stage not stated [ChimeraX, Coot, PyMOL]

### Bacterial immune activation via supramolecular assembly with phage triggers. (Nature 2026)

- DOI: 10.1038/s41586-025-10060-8 | PMCID: PMC13017515 | PMID: 41639456
- Evidence: After 2D classification, two classes corresponding to top and side views (1,470 particles) were selected and used for training with the ‘Topaz Train’ 42 in cryoSPARC, followed by ‘Topaz Extract’.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, Cutadapt v1.15] -> alignment/mapping [Bowtie2 v2.3.4.1, Cutadapt v1.15, MAFFT, NumPy, SAMtools v1.7] -> structure determination [AlphaFold, ChimeraX, Coot, PHENIX] -> machine learning [Topaz]

### Identification of mEAK-7 as a human V-ATPase regulator via cryo-EM data mining. (PNAS 2022)

- DOI: 10.1073/pnas.2203742119 | PMCID: PMC9436323 | PMID: 35994636
- Evidence: Particles were picked using Topaz with a general model ( 23 ).
- Full pipeline: registration [MotionCor2] -> structure determination [AlphaFold] -> stage not stated [Topaz]

### Diacylglycerol-dependent hexamers of the SNARE-assembling chaperone Munc13-1 cooperatively bind vesicles. (PNAS 2023)

- DOI: 10.1073/pnas.2306086120 | PMCID: PMC10623011 | PMID: 37883433
- Evidence: Topaz denoising was used to denoise selected tomograms using a unet-3d-20a pretrained model ( 34 ).
- Full pipeline: alignment/mapping [IMOD] -> machine learning [Topaz]

### Efficient tagging of endogenous proteins in human cell lines for structural studies by single-particle cryo-EM. (PNAS 2023)

- DOI: 10.1073/pnas.2302471120 | PMCID: PMC10401002 | PMID: 37487103
- Evidence: Particle picking was performed either by using Topaz (for 0-h oxidative stress) or template-based particle-picking (8-h oxidation and 24-h oxidation).
- Full pipeline: structure determination [PHENIX] -> machine learning [Cellpose] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [CTFFIND, Coot, ImageJ, MotionCor2, RELION, Topaz]

### Membrane protein isolation and structure determination in cell-derived membrane vesicles. (PNAS 2023)

- DOI: 10.1073/pnas.2302325120 | PMCID: PMC10160969 | PMID: 37098056
- Evidence: After selecting particles using Topaz ( 26 ) with a model trained on manually picked particles, we sorted these particles by two-dimensional (2D) classification, which unambiguously revealed Slo1 channels ( Fig.
- Full pipeline: dimensionality reduction/clustering [Topaz] -> machine learning [Topaz] -> stage not stated [MotionCor2, RELION]

### Structure of yeast RAVE bound to a partial V&lt;sub&gt;1&lt;/sub&gt; complex. (PNAS 2024)

- DOI: 10.1073/pnas.2414511121 | PMCID: PMC11648922 | PMID: 39625975
- Evidence: This process provided 66,347 and 214,437 particle images for Topaz training on IGEPAL and CHAPS datasets, respectively ( 62 ).
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, UCSF Chimera]

### Structural basis of chiral wrap and T-segment capture by &lt;i&gt;Escherichia coli&lt;/i&gt; DNA gyrase. (PNAS 2024)

- DOI: 10.1073/pnas.2407398121 | PMCID: PMC11626157 | PMID: 39589884
- Evidence: 19,0069 particles were picked using Topaz ( 76 ) and extracted with a pixel size of 1.72 Å/px.
- Full pipeline: structure determination [ChimeraX, PHENIX] -> stage not stated [Coot, Topaz]

### Identification of a depupylation regulator for an essential enzyme in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2407239121 | PMCID: PMC11626117 | PMID: 39585979
- Evidence: Particles from the five different views were separately trained within the Topaz Train module ( 62 ) in cryoSPARC (expected # of particles: 1,000, model architecture: ResNet16).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.1, PyMOL, SAMtools v1.13, featureCounts] -> quantification [featureCounts] -> normalisation [DESeq2 v1.40.2, tidyverse v2.0.0] -> differential/statistical testing [DESeq2 v1.40.2, tidyverse v2.0.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, ColabFold]

### Structural basis for DNA recognition by a viral genome-packaging machine. (PNAS 2024)

- DOI: 10.1073/pnas.2406138121 | PMCID: PMC11331095 | PMID: 39116131
- Evidence: Particle picking was performed with Topaz software ( 44 ).
- Full pipeline: registration [MotionCor2] -> visualisation [ChimeraX] -> stage not stated [CTFFIND, Coot, RELION v3.1.2, Topaz]

### Bispecific antibodies targeting two glycoproteins on SFTSV exhibit synergistic neutralization and protection in a mouse model. (PNAS 2024)

- DOI: 10.1073/pnas.2400163121 | PMCID: PMC11181109 | PMID: 38830098
- Evidence: After three rounds of 2D classification, we selected good particles in different views for Topaz training and then generated the Topaz model.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, MUSCLE v3.8.31, MotionCor2] -> variant calling [SAMtools v1.9] -> structure determination [Coot v0.9.3, PHENIX] -> machine learning [Topaz] -> visualisation [PyMOL v2.0] -> stage not stated [fastp]

### Cryo-EM structures elucidate the multiligand receptor nature of megalin. (PNAS 2024)

- DOI: 10.1073/pnas.2318859121 | PMCID: PMC11145282 | PMID: 38771880
- Evidence: After motion correction and contrast transfer function (CTF) estimation, particles were picked using Topaz ( 52 ) and extracted at 3.3 Å/pixel.
- Full pipeline: registration [Topaz] -> structure determination [AlphaFold, Coot] -> visualisation [ChimeraX] -> stage not stated [RELION v3.1]

### Structure and design of Langya virus glycoprotein antigens. (PNAS 2024)

- DOI: 10.1073/pnas.2314990121 | PMCID: PMC11032465 | PMID: 38593070
- Evidence: For the LayV G SM structure (oP4h), movie frame alignment and binning to 1.78 Å was carried out using Warp ( 82 ), estimation of the microscope CTF parameters, particle picking, and extraction (with a box size of 440 pixels 2 ) was carried out in cryoSPARC using Topaz ( 76 , 85 ).
- Full pipeline: alignment/mapping [Topaz] -> differential/statistical testing [RELION] -> structure determination [PHENIX, RELION] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, ChimeraX]

### The structure of PSI-LHCI from <i>Cyanidium caldarium</i> provides evolutionary insights into conservation and diversity of red-lineage LHCs. (PNAS 2024)

- DOI: 10.1073/pnas.2319658121 | PMCID: PMC10945839 | PMID: 38442179
- Version used: **0.2.4**
- Evidence: Two types of the cryo-EM maps were used for the model building of the PSI-LHCI supercomplex: One was a postprocessed map, and the other was a denoised map using Topaz version 0.2.4 ( 30 ).
- Full pipeline: stage not stated [IQ-TREE, Topaz v0.2.4, UCSF Chimera]

### Human paraneoplastic antigen Ma2 (PNMA2) forms icosahedral capsids that can be engineered for mRNA delivery. (PNAS 2024)

- DOI: 10.1073/pnas.2307812120 | PMCID: PMC10945824 | PMID: 38437549
- Evidence: Particles were picked using Topaz and a general model ( 52 ), yielding 722,571 particles which were extracted with a 512 pixel box, binned to 128 pixels, and classified using the VDAM 2D classification algorithm ( SI Appendix , Fig.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [SAMtools, STAR] -> differential/statistical testing [DESeq2] -> structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, MotionCor2, PyMOL, RELION v4.0, Topaz]

### Filament structure and subcellular organization of the bacterial intermediate filament-like protein crescentin. (PNAS 2024)

- DOI: 10.1073/pnas.2309984121 | PMCID: PMC10873595 | PMID: 38324567
- Evidence: Particles centered on individual nodes were picked from all micrographs that had been denoised for picking purposes using a neural network model pre-trained in Topaz ( 50 , 51 ).
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [IMOD, PHENIX] -> machine learning [Topaz] -> stage not stated [Coot, ImageJ, MotionCor2, RELION v3.1]

### Structural basis of σ<sup>54</sup> displacement and promoter escape in bacterial transcription. (PNAS 2024)

- DOI: 10.1073/pnas.2309670120 | PMCID: PMC10786286 | PMID: 38170755
- Evidence: All image processing was carried out in RELION 4.0 ( 32 ), using MOTIONCORR implementation in RELION ( 33 ) and CTFFIND4 ( 34 ) with particles picked using Topaz ( 35 ).
- Full pipeline: structure determination [PHENIX] -> visualisation [ChimeraX] -> stage not stated [RELION v4.0, Topaz]

### De novo design of potent inhibitors of clostridial family toxins. (PNAS 2025)

- DOI: 10.1073/pnas.2509329122 | PMCID: PMC12501149 | PMID: 40982695
- Evidence: Following 2D classification the five best classes, containing 39,344 particle images, were used to train Topaz on all 5963 good micrographs.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [PyMOL, seaborn] -> stage not stated [AlphaFold, ChimeraX, Topaz]

### Capturing the native structure of membrane proteins using vesicles. (PNAS 2025)

- DOI: 10.1073/pnas.2423407122 | PMCID: PMC12435220 | PMID: 40901875
- Evidence: Finally, Topaz picked 1,560,821 particles from all other images, from which 666,048 particles were selected for further processing.
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> machine learning [EMAN2] -> stage not stated [ChimeraX, Topaz, UCSF Chimera]

### Generation of actionable, cancer-specific neoantigens from KRAS(G12C) with adagrasib. (PNAS 2025)

- DOI: 10.1073/pnas.2509012122 | PMCID: PMC12337345 | PMID: 40737322
- Evidence: The 2D-cleaned particles were used for Topaz training ( 30 ).
- Full pipeline: structure determination [UCSF Chimera] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2 v1.5, PHENIX v1.18.2, Python]

### An electron-bifurcating "plug" to a protein nanowire in tungsten-dependent aldehyde detoxification. (PNAS 2025)

- DOI: 10.1073/pnas.2501900122 | PMCID: PMC12318220 | PMID: 40694326
- Evidence: The class containing the whole protein complex was selected and used in Topaz training and picking particles from the micrographs.
- Full pipeline: structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [ChimeraX]

### Structural basis of the inhibition of TRPV1 by analgesic sesquiterpenes. (PNAS 2025)

- DOI: 10.1073/pnas.2506560122 | PMCID: PMC12305030 | PMID: 40663614
- Evidence: Cleaned particles from blob, template, and Topaz picking were combined with removal of duplicates and were further 3D classified (heterogeneous refinement) into four classes.
- Full pipeline: simulation/modelling [NAMD v2.14] -> structure determination [PHENIX, Topaz] -> visualisation [ChimeraX, PHENIX, UCSF Chimera] -> stage not stated [Coot]

### Structure of the virulence-associated &lt;i&gt;Neisseria meningitidis&lt;/i&gt; filamentous bacteriophage MDAΦ. (PNAS 2025)

- DOI: 10.1073/pnas.2420157122 | PMCID: PMC12207478 | PMID: 40540604
- Evidence: Phage particles were picked using Topaz ( 42 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [IMOD, PHENIX] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, MotionCor2, RELION, Topaz]

### Targeting ryanodine receptors with allopurinol and xanthine derivatives for the treatment of cardiac and musculoskeletal weakness disorders. (PNAS 2025)

- DOI: 10.1073/pnas.2422082122 | PMCID: PMC12184490 | PMID: 40512792
- Evidence: Particle picking was performed using Topaz trained with preexisting cryo-EM picked particles.
- Full pipeline: structure determination [Coot, PHENIX] -> machine learning [Topaz] -> stage not stated [ChimeraX]

### Structural insights into the activation of the human prostaglandin E&lt;sub&gt;2&lt;/sub&gt; receptor EP1 subtype by prostaglandin E&lt;sub&gt;2&lt;/sub&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2423840122 | PMCID: PMC12107139 | PMID: 40366695
- Evidence: The best model from the good references was used for Topaz train to generate a Topaz picking model, which was later applied for Topaz extraction.
- Full pipeline: registration [MotionCor2] -> structure determination [Coot, PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, R v7.40, Topaz]

### Subunit specialization in AAA+ proteins and substrate unfolding during transcription complex remodeling. (PNAS 2025)

- DOI: 10.1073/pnas.2425868122 | PMCID: PMC12054792 | PMID: 40273105
- Evidence: Particle picking in the RPi(−11/−8) dataset was carried out using Gautomatch ( https://github.com/JackZhang-Lab/Gautmatch ) using RPi(−12/−11) reference projections ( 29 ), whereas particles of RPi(−10/−1) dataset were picked with Topaz ( 30 ).
- Full pipeline: stage not stated [CTFFIND, RELION v4.0, Topaz]

### A splendid molecular factory: De- and reconstruction of the mammalian respiratory chain. (PNAS 2025)

- DOI: 10.1073/pnas.2416162122 | PMCID: PMC11962478 | PMID: 40100632
- Evidence: Template-based picking was insufficient to separate the two particle sets entirely but was achieved satisfactory using Topaz ( 30 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [ChimeraX, Coot, Topaz]

### Structural basis of DNA replication fidelity of the Mpox virus. (PNAS 2025)

- DOI: 10.1073/pnas.2411686122 | PMCID: PMC11912389 | PMID: 40035768
- Evidence: For the MPXV DNA polymerase holoenzyme in editing state 1, we selected ~600,000 particles from 1,000 micrographs for 2D classification to generate a particle dataset for Topaz Training ( 49 ).
- Full pipeline: structure determination [PHENIX, RELION] -> machine learning [Topaz] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MotionCor2 v1.2.4]

### Cryo-EM of native membranes reveals an intimate connection between the Krebs cycle and aerobic respiration in mycobacteria. (PNAS 2025)

- DOI: 10.1073/pnas.2423761122 | PMCID: PMC11874196 | PMID: 39969994
- Evidence: This approach was repeated several times using Topaz models trained on the best particle images from either 2D classification or 3D heterogenous refinement from the previous iteration.
- Full pipeline: structure determination [Topaz] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, PHENIX, UCSF Chimera]

### Stepwise activation of SARM1 for cell death and axon degeneration revealed by a biosynthetic NMN mimic. (PNAS 2025)

- DOI: 10.1073/pnas.2424906122 | PMCID: PMC11874154 | PMID: 39964720
- Evidence: For the SARM1 (2Cmut)-M1 complex, following motion correction, CTF estimation, particle picking, and Topaz Train, a total of 213,363 particles were subjected to 2D classification, followed by ab initio reconstruction and heterogeneous refinement.
- Full pipeline: quantification [ImageJ] -> registration [MotionCor2, Topaz] -> structure determination [PHENIX, Topaz] -> stage not stated [ChimeraX, PyMOL]

### NPF binding to Arp2 is allosterically linked to the release of ArpC5's N-terminal tail and conformational changes in Arp2/3 complex. (PNAS 2025)

- DOI: 10.1073/pnas.2421557122 | PMCID: PMC11873952 | PMID: 40042350
- Evidence: Topaz picked 740,076 particles, which were extracted with a box size of 352 pixels (303 Å) and binned by two to a box size of 176 pixels.
- Full pipeline: structure determination [ChimeraX, PHENIX] -> visualisation [PyMOL] -> stage not stated [Topaz]

### Structure-guided engineering of a mutation-tolerant inhibitor peptide against variable SARS-CoV-2 spikes. (PNAS 2025)

- DOI: 10.1073/pnas.2413465122 | PMCID: PMC11789008 | PMID: 39854234
- Evidence: Four datasets were collected for the ectodomain with the BA.2-type RBD complex, and the particles were autopicked using Topaz, extracted with rescaling from 600 × 600 to 160 × 160 pixel images, and subjected to 2D classification and 3D classification.
- Full pipeline: normalisation [Topaz] -> structure determination [PHENIX] -> stage not stated [CCP4, RELION]

### Structural and functional dynamics of human cone cGMP-phosphodiesterase important for photopic vision. (PNAS 2025)

- DOI: 10.1073/pnas.2419732121 | PMCID: PMC11725853 | PMID: 39739818
- Evidence: For particle picking in all datasets, a Topaz picking model was generated using Topaz train job and 16,751 particles from 2D classes with high-resolution features as an input.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UCSF Chimera] -> structure determination [ChimeraX, Coot, PHENIX, UCSF Chimera] -> stage not stated [Topaz]

### Structures of methane and ammonia monooxygenases in native membranes. (PNAS 2025)

- DOI: 10.1073/pnas.2417993121 | PMCID: PMC11725843 | PMID: 39739801
- Evidence: The optimized particle stack was used to train a Topaz picking model ( 34 , 35 ), which yielded a particle stack processed as above, this time with further homogeneous, nonuniform, and CTF refinements.
- Full pipeline: structure determination [ChimeraX, PHENIX v1.21, Topaz] -> visualisation [ChimeraX] -> stage not stated [Coot]

### Computational design of an ultrapotent deltacoronavirus miniprotein inhibitor. (PNAS 2026)

- DOI: 10.1073/pnas.2533456123 | PMCID: PMC13142991 | PMID: 42054371
- Evidence: The Topaz picked particles were extracted and sorted using 2D classification and heterogeneous refinement before refinement using nonuniform refinement in cryoSPARC.
- Full pipeline: structure determination [ChimeraX, PHENIX, Topaz] -> stage not stated [AlphaFold, RELION v3.0]

### Synaptic transmission: Munc13 assembles onto PI(4,5)P&lt;sub&gt;2&lt;/sub&gt;-rich domains into trimers that cooperate to capture vesicles. (PNAS 2026)

- DOI: 10.1073/pnas.2523347123 | PMCID: PMC12912961 | PMID: 41671179
- Evidence: The tomograms were denoised using Topaz ( 47 ) for further visualization and analysis.
- Full pipeline: alignment/mapping [IMOD] -> quantification [ImageJ] -> registration [IMOD] -> dimensionality reduction/clustering [ImageJ] -> simulation/modelling [GROMACS] -> visualisation [Topaz] -> stage not stated [AlphaFold, VMD]

### Structural characterization of the HDV virion and its ribonucleoprotein. (PNAS 2026)

- DOI: 10.1073/pnas.2519809123 | PMCID: PMC12846810 | PMID: 41564123
- Evidence: After 2-D classification, classes with side views were used to train Topaz picking model ( 53 ).
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [ChimeraX, Coot, Matplotlib, NumPy, SciPy, Topaz, UCSF Chimera]

### PIM1 controls GBP1 activity to limit self-damage and to guard against pathogen infection. (Science 2023)

- DOI: 10.1126/science.adg2253 | PMCID: PMC7615196 | PMID: 37797010
- Evidence: The particles were used to train Topaz ( 71 ) and re-pick on all micrographs, yielding 420,768 particles.
- Full pipeline: alignment/mapping [MAFFT] -> quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [ChimeraX v0.93, MACS2, PHENIX, Topaz]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: Particle picking was done using Topaz with the general model ( 60 ) and a 110 Å particle diameter, yielding 2,510,771 particles (grid 1) or 2,117,653 particles (grid 2).
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

### Cryo-EM structure of human telomerase dimer reveals H/ACA RNP-mediated dimerization. (Science 2025)

- DOI: 10.1126/science.adr5817 | PMCID: PMC7618144 | PMID: 40638752
- Evidence: For dataset 2, particle picking was done using a Topaz trained model ( 63 ) implemented within RELION 4.0.
- Full pipeline: alignment/mapping [minimap2] -> machine learning [Topaz] -> stage not stated [CTFFIND, ChimeraX, ImageJ, PHENIX v1.20, RELION v5.0, UCSF Chimera]

### Cat1 forms filament networks to degrade NAD&lt;sup&gt;+&lt;/sup&gt; during the type III CRISPR-Cas antiviral response. (Science 2025)

- DOI: 10.1126/science.adv9045 | PMCID: PMC12162218 | PMID: 40208959
- Evidence: 12,213 particles correspond to good 2D classes were chosen by iterative 2D classification and used for Topaz training job.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold]

### TIGR-Tas: A family of modular RNA-guided DNA-targeting systems in prokaryotes and their viruses. (Science 2025)

- DOI: 10.1126/science.adv9789 | PMCID: PMC12045711 | PMID: 40014690
- Evidence: An initial model was generated from 540,459 particles selected from 1500 micrographs by 2D classification of particles picked within RELION using Topaz ( 102 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, MAFFT, PyMOL] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [MAFFT, PHENIX] -> stage not stated [CTFFIND, ColabFold, Coot, HMMER, MotionCor2, RELION, Topaz]

### Structural mechanism of LINE-1 target-primed reverse transcription. (Science 2025)

- DOI: 10.1126/science.ads8412 | PMCID: PMC7617806 | PMID: 40048554
- Evidence: Particle picking was carried out using Topaz with the general model ( 88 ).
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [AlphaFold, PHENIX v1.21.1, RELION] -> stage not stated [CTFFIND, ChimeraX, ImageJ, MotionCor2, PyMOL, Python, REFMAC, Topaz]

### Molecular basis of FIGNL1 in dissociating RAD51 from DNA and chromatin. (Science 2025)

- DOI: 10.1126/science.adr7920 | PMCID: PMC7617353 | PMID: 39636933
- Evidence: Particles were initially picked using Topaz( 65 ) and extracted in a box size of 192 pixels.
- Full pipeline: registration [CTFFIND] -> structure determination [AlphaFold, PHENIX] -> visualisation [Fiji, ImageJ, RELION] -> stage not stated [Coot, Topaz]

### Cryo-electron microscopy structure of the budding yeast telomerase holoenzyme. (Science 2026)

- DOI: 10.1126/science.adz5344 | PMCID: PMC7619062 | PMID: 41886584
- Evidence: Particle picking was done using Topaz ( 97 ), yielding 1,876,851 picked particles.
- Full pipeline: quantification [ImageJ] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, CTFFIND v4.1, Python, RELION v5.0, Topaz]

### Termination of the integrated stress response. (Science 2026)

- DOI: 10.1126/science.adw5137 | PMCID: PMC7618491 | PMID: 41231936
- Evidence: Particle picking was performed on the CTF corrected micrographs using Topaz ( 43 ) with a pre-trained agent.
- Full pipeline: registration [RELION v5.0] -> structure determination [PHENIX] -> machine learning [Topaz] -> stage not stated [AlphaFold, ChimeraX, PyMOL]

