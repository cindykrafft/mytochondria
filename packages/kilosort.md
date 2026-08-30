# Kilosort

- **Category:** neuro-tools
- **Papers in survey:** 60
- **Journals:** Nature (39), PNAS (17), Cell (4)
- **Years:** 2021 (2), 2022 (6), 2023 (10), 2024 (17), 2025 (18), 2026 (7)
- **Versions named:** 2.5 (12), 2.0 (9), 1.0 (1), 4.0 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (14), registration (2), quality control (2), visualisation (1), differential/statistical testing (1)

## Papers

### Cell-type-specific population dynamics of diverse reward computations. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.019 | PMCID: PMC10387374 | PMID: 36113428
- Version used: **2.5**
- Evidence: Electrophysiology Spike sorting The electrophysiological traces were processed by a custom Python-based pipeline, with preprocessing (CatGT), spike sorting (Kilosort 2.5; ), waveform calculation (C_Waves), quality control metrics calculation (quality_metrics), and activity-behavior synchronization (TPrime) modules, initially written by the Allen Institute for Brain Science and Jennifer Colonell (J...
- Full pipeline: quality control [Kilosort v2.5] -> stage not stated [DeepLabCut, Python]

### Structural basis for ion selectivity in potassium-selective channelrhodopsins. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.009 | PMCID: PMC7615185 | PMID: 37652010
- Version used: **2.5**
- Evidence: Spike sorting was performed by the Kilosort 2.5 package 131 incorporated in a custom Pythonbased pipeline for common average referencing, spike sorting, duplicate spike removal, waveform calculation, and single-unit quality metric calculation.
- Full pipeline: structure determination [AlphaFold, Coot, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Kilosort v2.5, MotionCor2, RELION v4.0, UCSF Chimera]

### Structural and functional map for forelimb movement phases between cortex and medulla. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.009 | PMCID: PMC9842395 | PMID: 36608651
- Evidence: ...td. https://bonsai-rx.org RRID:SCR_017218 Fiji Fiji http://fiji.sc RRID:SCR_002285 TrackMate (v6.0.3) TrackMate https://imagej.net/plugins/trackmate/ Kilosort v2 Cortex lab https://github.com/MouseLand/Kilosort/releases/tag/v2.0 Kilosort v3 Cortex lab https://github.com/MouseLand/Kilosort Phy2 Cortex lab https://github.com/cortex-lab/phy DeepLabCut Mathis Lab; Mathis et al.
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [DeepLabCut, Kilosort, Python v3.7, SciPy, TrackMate v6.0.3, scikit-learn]

### Coordinating brain-distributed network activities in memory resistant to extinction. (Cell 2024)

- DOI: 10.1016/j.cell.2023.12.018 | PMCID: PMC7615560 | PMID: 38242086
- Evidence: Spike detection and unit isolation Spike sorting and unit isolation were performed with an automated clustering pipeline using Kilosort ( https://github.com/cortex-lab/KiloSort ) via the SpikeForest framework ( https://github.com/flatironinstitute/spikeforest ) 132 , 133 .
- Full pipeline: normalisation [SciPy] -> dimensionality reduction/clustering [Kilosort, UMAP] -> differential/statistical testing [NumPy, Python v3.6, seaborn] -> visualisation [Matplotlib] -> stage not stated [Astropy v2.0.2, scikit-learn v0.19.1]

### The orbitofrontal cortex maps future navigational goals. (Nature 2021)

- DOI: 10.1038/s41586-021-04042-9 | PMCID: PMC8599015 | PMID: 34707289
- Evidence: The signals were band-pass filtered at 0.6–6 kHz, and spikes were detected and assigned to separate clusters using Kilosort 31 ( https://github.com/cortex-lab/KiloSort ) under the parameter settings of the spike threshold at −4 and the number of filters at 2× the total channel number.
- Full pipeline: dimensionality reduction/clustering [Kilosort]

### The encoding of touch by somatotopically aligned dorsal column subdivisions. (Nature 2022)

- DOI: 10.1038/s41586-022-05470-x | PMCID: PMC9729103 | PMID: 36418401
- Version used: **2.0**
- Evidence: Spike sorting (MEAs) MEA recordings underwent initial analysis using Kilosort 2.0 (ref.
- Full pipeline: stage not stated [Kilosort v2.0]

### Distinguishing externally from saccade-induced motion in visual cortex. (Nature 2022)

- DOI: 10.1038/s41586-022-05196-w | PMCID: PMC9534749 | PMID: 36104560
- Evidence: Unit isolation Single units from extracellular recordings were isolated using KiloSort 59 and visualized using Phy for further manual merging and splitting.
- Full pipeline: visualisation [Kilosort] -> stage not stated [DeepLabCut]

### Hippocampal place cells have goal-oriented vector fields during navigation. (Nature 2022)

- DOI: 10.1038/s41586-022-04913-9 | PMCID: PMC9329099 | PMID: 35794477
- Evidence: Spike sorting Spikes were automatically sorted using KiloSort 30 followed by manual curation using Phy 31 , which consisted mainly of merging and deleting clusters, using autocorrelations and cross-correlations as a guide.
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> stage not stated [DeepLabCut]

### Toroidal topology of population activity in grid cells. (Nature 2022)

- DOI: 10.1038/s41586-021-04268-7 | PMCID: PMC8810387 | PMID: 35022611
- Version used: **2.5**
- Evidence: Spike sorting and single-unit selection Spike sorting was performed with KiloSort 2.5 26 .
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.1.3, NumPy v1.18.1, UMAP, scikit-learn v0.22.1] -> differential/statistical testing [Python] -> stage not stated [Kilosort v2.5, SciPy]

### Neural landscape diffusion resolves conflicts between needs across time. (Nature 2023)

- DOI: 10.1038/s41586-023-06715-z | PMCID: PMC10651489 | PMID: 37938783
- Evidence: Following preprocessing with CatGT, data was spike sorted using Kilosort3 ( https://github.com/MouseLand/Kilosort ).
- Full pipeline: dimensionality reduction/clustering [Scanpy] -> stage not stated [Jupyter, Kilosort, Matplotlib, NumPy, Python, SciPy, scikit-learn, seaborn]

### Preserved neural dynamics across animals performing similar behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06714-0 | PMCID: PMC10665198 | PMID: 37938772
- Version used: **2.0**
- Evidence: Recorded data were preprocessed using an open-source software KiloSort 2.0 ( https://github.com/MouseLand/Kilosort ) and manually curated using Phy ( https://github.com/cortex-lab/phy ) to identify putative single units in each of the primary motor cortex and dorsolateral striatum.
- Full pipeline: machine learning [PyTorch] -> stage not stated [Jupyter, Kilosort v2.0, Matplotlib, NumPy, Python, SciPy]

### A cell-type-specific error-correction signal in the posterior parietal cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06357-1 | PMCID: PMC10412446 | PMID: 37468637
- Version used: **2.5**
- Evidence: We used Kilosort (v.2.5) 57 with the default parameters to detect spikes.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose] -> visualisation [UMAP] -> stage not stated [AnnData, Fiji, ImageJ, Kilosort v2.5, Psychtoolbox, Python, Suite2p]

### Interhemispheric competition during sleep. (Nature 2023)

- DOI: 10.1038/s41586-023-05827-w | PMCID: PMC10097603 | PMID: 36949193
- Evidence: 52 ; https://github.com/MouseLand/Kilosort ) and the ecephys pipeline ( https://github.com/jenniferColonell/ecephys_spike_sorting ); clusters were curated manually in Phy ( https://github.com/cortex-lab/phy ).
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> differential/statistical testing [SciPy v1.6.2]

### Cardiogenic control of affective behavioural state. (Nature 2023)

- DOI: 10.1038/s41586-023-05748-8 | PMCID: PMC9995271 | PMID: 36859543
- Version used: **2.5**
- Evidence: Spike sorting was performed by Kilosort 2.5 and auxiliary software as previously described 66 .
- Full pipeline: registration [ilastik] -> machine learning [ilastik] -> stage not stated [Kilosort v2.5]

### The cellular coding of temperature in the mammalian cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-05705-5 | PMCID: PMC9946826 | PMID: 36755097
- Evidence: The extracellular recordings were spike sorted using Kilosort (version 2) 43 .
- Full pipeline: registration [Python, Suite2p] -> stage not stated [Fiji, ImageJ, Kilosort]

### A cellular basis for mapping behavioural structure. (Nature 2024)

- DOI: 10.1038/s41586-024-08145-x | PMCID: PMC11655361 | PMID: 39506112
- Evidence: Recordings were spike sorted using Kilosort 60 , versions 2.5 and 3, and manually curated using phy ( https://github.com/kwikteam/phy ).
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Matplotlib v3.7.3, NumPy v1.22.0, SciPy v1.10.1, TensorFlow, seaborn v0.13.2]

### Intermittent rate coding and cue-specific ensembles support working memory. (Nature 2024)

- DOI: 10.1038/s41586-024-08139-9 | PMCID: PMC11634780 | PMID: 39506106
- Evidence: Because we were interested in population-level coding of memory, we analysed both putative single- and multi-unit clusters identified by Kilosort.
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> stage not stated [Psychtoolbox]

### One-shot entorhinal maps enable flexible navigation in novel environments. (Nature 2024)

- DOI: 10.1038/s41586-024-08034-3 | PMCID: PMC11602719 | PMID: 39385034
- Evidence: Kilosort2 was used for spike sorting offline: https://github.com/MouseLand/Kilosort .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [DeepLabCut v2.2.0.6] -> stage not stated [Kilosort, Python, SciPy]

### Brain-wide dynamics linking sensation to action during decision-making. (Nature 2024)

- DOI: 10.1038/s41586-024-07908-w | PMCID: PMC11499283 | PMID: 39261727
- Version used: **2.0**
- Evidence: We spike-sorted electrophysiological data from each probe in each session using KiloSort2.0 65 ( https://github.com/MouseLand/Kilosort ).
- Full pipeline: machine learning [DeepLabCut] -> stage not stated [Kilosort v2.0, NumPy, PyTorch, SciPy]

### Semantic encoding during language comprehension at single-cell resolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07643-2 | PMCID: PMC11254762 | PMID: 38961302
- Evidence: For the Neuropixels recordings, putative units were identified and sorted off-line using Kilosort and only well-isolated single units were used.
- Full pipeline: dimensionality reduction/clustering [SPM] -> visualisation [SPM] -> stage not stated [Kilosort, Python]

### Mental navigation in the primate entorhinal cortex. (Nature 2024)

- DOI: 10.1038/s41586-024-07557-z | PMCID: PMC11224022 | PMID: 38867051
- Version used: **2.0**
- Evidence: Using Kilosort 2.0 software 62 , we isolated 1,478 single units and multi-units (A, 614; M, 864).
- Full pipeline: stage not stated [Kilosort v2.0]

### Volatile working memory representations crystallize with practice. (Nature 2024)

- DOI: 10.1038/s41586-024-07425-w | PMCID: PMC11136659 | PMID: 38750359
- Evidence: Silicon probe data processing and spike sorting were performed using custom code, KiloSort 39 and Phy 40 .
- Full pipeline: stage not stated [DeepLabCut, Kilosort, Suite2p]

### Neural and behavioural state switching during hippocampal dentate spikes. (Nature 2024)

- DOI: 10.1038/s41586-024-07192-8 | PMCID: PMC11023929 | PMID: 38480889
- Evidence: Spikes from single units were sorted using Kilosort ( https://github.com/MouseLand/Kilosort ), followed by manual curation in Phy2 ( https://github.com/cortex-lab/phy ).
- Full pipeline: dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [Python] -> machine learning [DeepLabCut] -> stage not stated [Kilosort, NetworkX]

### Single-neuronal elements of speech production in humans. (Nature 2024)

- DOI: 10.1038/s41586-023-06982-w | PMCID: PMC10866697 | PMID: 38297120
- Version used: **1.0**
- Evidence: Next, single units were isolated from the motion-corrected interpolated signal using Kilosort (v.1.0; https://github.com/cortex-lab/KiloSort ) followed by Phy for cluster curation (v.2.0a1; https://github.com/cortex-lab/phy ; Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [Kilosort v1.0, scikit-learn] -> structure determination [FreeSurfer v7.4.1] -> stage not stated [FieldTrip, statsmodels v0.13.5]

### Minute-scale oscillatory sequences in medial entorhinal cortex. (Nature 2024)

- DOI: 10.1038/s41586-023-06864-1 | PMCID: PMC10781645 | PMID: 38123682
- Version used: **2.5**
- Evidence: Spike Sorting and single-unit selection Spike sorting of Neuropixels data was performed using a version of KiloSort 2.5 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [Kilosort v2.5, Suite2p]

### Large-scale single-neuron speech sound encoding across the depth of human cortex. (Nature 2024)

- DOI: 10.1038/s41586-023-06839-2 | PMCID: PMC10866713 | PMID: 38093008
- Version used: **2.5**
- Evidence: Post hoc motion correction was applied using Kilosort 2.5 (ref.
- Full pipeline: registration [Kilosort v2.5] -> stage not stated [MNE-Python v0.22.0, PyTorch]

### A brain-wide map of neural activity during complex behaviour. (Nature 2025)

- DOI: 10.1038/s41586-025-09235-0 | PMCID: PMC12408349 | PMID: 40903598
- Version used: **2.5**
- Evidence: In brief, spike sorting was performed using a modified version of the Kilosort 2.5 algorithm 14 .
- Full pipeline: differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5, Python]

### A circuit that integrates drive state and social contact to gate mating. (Nature 2025)

- DOI: 10.1038/s41586-025-09327-x | PMCID: PMC12507686 | PMID: 40903568
- Evidence: The cluster automatically labelled by Kilosort algorithm as ‘good’ were in turn manually curated by hand and further analysed with Phy2.
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> stage not stated [ImageJ, Python]

### A compressed hierarchy for visual form processing in the tree shrew. (Nature 2025)

- DOI: 10.1038/s41586-025-09441-w | PMCID: PMC12545169 | PMID: 40866712
- Evidence: The clusters automatically labelled by Kilosort algorithm as ‘good’ were in turn manually curated by hand and further analysed with Phy2.
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> stage not stated [Python]

### The neural basis of species-specific defensive behaviour in Peromyscus mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09241-2 | PMCID: PMC12422964 | PMID: 40702175
- Evidence: Spike sorting We sorted the high-pass filtered neural data using Kilosort2 69 ( https://github.com/MouseLand/Kilosort/releases/tag/v2.0 ), followed by manual curation in phy2 ( https://github.com/cortex-lab/phy ).
- Full pipeline: quantification [QuPath v0.2.3] -> normalisation [StarDist] -> differential/statistical testing [Python v3.6.0, R, lme4, scikit-learn] -> machine learning [StarDist] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Psychtoolbox, emmeans]

### Remote activation of place codes by gaze in a highly visual animal. (Nature 2025)

- DOI: 10.1038/s41586-025-09101-z | PMCID: PMC12356099 | PMID: 40500454
- Evidence: First, we calculated the spatial extent of each unit along the probe, as well as the cluster contamination rate determined by Kilosort, and excluded units that passed a threshold for each.
- Full pipeline: quality control [Kilosort] -> dimensionality reduction/clustering [Kilosort]

### Dynamic basal ganglia output signals license and suppress forelimb movements. (Nature 2025)

- DOI: 10.1038/s41586-025-09066-z | PMCID: PMC12367548 | PMID: 40437098
- Evidence: Subsequently, using the Kilosort helper module, channels with a firing rate below 0.05 Hz were excluded as noisy channels and the channel map for the spatial location of the remaining channels was constructed using the metadata from the recordings.
- Full pipeline: visualisation [ImageJ] -> stage not stated [DeepLabCut, Kilosort, Python]

### NEURD offers automated proofreading and feature extraction for connectomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08660-5 | PMCID: PMC11981913 | PMID: 40205208
- Evidence: Similar to other open source software packages that have supported the widespread adoption of other complex data modalities such as calcium imaging (CaImAn 7 and Suite2P 8 ), Neuropixels recordings (KiloSort 9 and MountainSort 10 ), label-free behavioural tracking (DeepLabCut 11 , MoSeq 12 and SLEAP 13 ) and spatial transcriptomics (Giotto 14 and Squidpy 15 ), the goal of NEURD is to make ‘big neu...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [DeepLabCut, SLEAP, Squidpy] -> stage not stated [CaImAn, Kilosort, NetworkX, Python]

### A neural mechanism for learning from delayed postingestive feedback. (Nature 2025)

- DOI: 10.1038/s41586-025-08828-z | PMCID: PMC12176619 | PMID: 40175547
- Version used: **2.5**
- Evidence: We then used the International Brain Laboratory’s (IBL) Python Kilosort 2.5 implementation 90 , 91 ( https://github.com/int-brain-lab/pykilosort ) to correct for sample drift along the length of the probe, to detect and remove failing channels and to apply a spatial de-striping filter.
- Full pipeline: differential/statistical testing [scikit-learn] -> structure determination [Python] -> machine learning [Cellpose, Keras, TensorFlow, scikit-learn] -> visualisation [NumPy] -> stage not stated [Astropy, Kilosort v2.5, R, SciPy]

### A subcortical switchboard for perseverative, exploratory and disengaged states. (Nature 2025)

- DOI: 10.1038/s41586-025-08672-1 | PMCID: PMC12043504 | PMID: 40044848
- Evidence: Spikes were sorted with Kilosort2 ( https://github.com/cortex-lab/Kilosort ) and Phy 68 .
- Full pipeline: quantification [ImageJ] -> stage not stated [Kilosort]

### Left-right-alternating theta sweeps in entorhinal-hippocampal maps of space. (Nature 2025)

- DOI: 10.1038/s41586-024-08527-1 | PMCID: PMC11946909 | PMID: 39900625
- Version used: **2.5**
- Evidence: Spike sorting and single-unit selection Spike sorting was done using KiloSort 2.5 (ref.
- Full pipeline: dimensionality reduction/clustering [Matplotlib, NumPy, Scanpy, SciPy, UMAP, scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5]

### Understanding the neural code of stress to control anhedonia. (Nature 2025)

- DOI: 10.1038/s41586-024-08241-y | PMCID: PMC11735319 | PMID: 39633053
- Evidence: Spike-sorting Neuropixels action potential signals were preprocessed and spike-sorted offline using Kilosort 2 (ref.
- Full pipeline: dimensionality reduction/clustering [Python, scikit-learn] -> stage not stated [DeepLabCut, Kilosort]

### Nonlinear receptive fields evoke redundant retinal coding of natural scenes. (Nature 2025)

- DOI: 10.1038/s41586-024-08212-3 | PMCID: PMC11711096 | PMID: 39567692
- Evidence: We used Kilosort 62 for spike sorting.
- Full pipeline: stage not stated [Kilosort]

### Neural representation of action symbols in primate frontal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10297-x | PMCID: PMC13233313 | PMID: 42162420
- Version used: **2.5**
- Evidence: We used a three-step approach for extracting and clustering spikes, with a first pass using Kilosort (v.2.5) 95 to extract putative spike clusters, a second pass using a custom-written program to label these clusters as SU, MU or noise, and a final manual curation step.
- Full pipeline: dimensionality reduction/clustering [Kilosort v2.5, UMAP] -> machine learning [scikit-learn v1.3.0] -> stage not stated [NumPy v1.24.3, SciPy v1.10.1, pandas v2.0.3, seaborn v0.12.2, statsmodels v0.14.0]

### Plasticity and language in the anaesthetized human hippocampus. (Nature 2026)

- DOI: 10.1038/s41586-026-10448-0 | PMCID: PMC13275293 | PMID: 42092132
- Evidence: If the estimated motion led to no improvement in the spike locations then spike sorting proceeded with the motion correction package built into Kilosort 4 without performing interpolation.
- Full pipeline: registration [Kilosort] -> structure determination [Python] -> stage not stated [SpikeInterface]

### Rapid concerted switching of the neural code in the inferotemporal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10267-3 | PMCID: PMC13148990 | PMID: 41882367
- Evidence: All Neuropixels data were acquired using SpikeGLX or OpenEphys 60 acquisition software and spike sorted using Kilosort 3 or 4 61 , 62 with the threshold parameter set to (10, 4).
- Full pipeline: machine learning [PyTorch] -> stage not stated [FSL, FreeSurfer, Kilosort]

### Climbing fibres recruit disinhibition to enhance Purkinje cell calcium signals. (Nature 2026)

- DOI: 10.1038/s41586-026-10220-4 | PMCID: PMC13171427 | PMID: 41851460
- Version used: **2.0**
- Evidence: For in vivo Neuropixels recordings, units were sorted using Kilosort 2.0 and manually curated with Phy as described previously 8 .
- Full pipeline: simulation/modelling [Python] -> stage not stated [Kilosort v2.0]

### Evidence accumulation from experience and observation in the cingulate cortex. (Nature 2026)

- DOI: 10.1038/s41586-025-09885-0 | PMCID: PMC12931446 | PMID: 41501452
- Evidence: Spike sorting and curation were carried out using Kilosort 3 ( https://github.com/MouseLand/Kilosort ) and phy ( https://github.com/cortex-lab/phy ).
- Full pipeline: stage not stated [Kilosort]

### Spontaneous activity competes with externally evoked responses in sensory cortex. (PNAS 2021)

- DOI: 10.1073/pnas.2023286118 | PMCID: PMC8237647 | PMID: 34155142
- Evidence: For FR, we sorted the broadband signal into units using KiloSort ( 67 ), inspected each cluster, and defined units based on wave shape and existence of refractory periods.
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> stage not stated [FieldTrip]

### Synchronous spiking of cerebellar Purkinje cells during control of movements. (PNAS 2022)

- DOI: 10.1073/pnas.2118954119 | PMCID: PMC9168948 | PMID: 35349338
- Evidence: We used P-sort ( 71 ) to identify the SSs and CSs in the heptodes and tetrodes recordings, and used Kilosort and Phi ( 72 ) to identify the spikes for the silicon probes.
- Full pipeline: alignment/mapping [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Kilosort]

### Interictal epileptiform discharges affect memory in an Alzheimer's disease mouse model. (PNAS 2023)

- DOI: 10.1073/pnas.2302676120 | PMCID: PMC10450667 | PMID: 37590406
- Evidence: Spike sorting was performed semiautomatically and separately for each channel of Behnke-Fried Microwire signal using Kilosort ( https://github.com/MouseLand/Kilosort ), followed by manual curation of the waveform clusters with the Phy2 software ( https://github.com/cortex-lab/phy ).
- Full pipeline: dimensionality reduction/clustering [Kilosort]

### Transformation of acoustic information to sensory decision variables in the parietal cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2212120120 | PMCID: PMC9926273 | PMID: 36598952
- Evidence: An open source spike package (KiloSort) ( 68 ) was used to extract and cluster spike waveforms.
- Full pipeline: dimensionality reduction/clustering [Kilosort]

### Innate face-selectivity in the brain of young domestic chicks. (PNAS 2024)

- DOI: 10.1073/pnas.2410404121 | PMCID: PMC11459190 | PMID: 39316055
- Version used: **2.0**
- Evidence: Spike detection and sorting was automatically performed in Kilosort 2.0 ( 66 ) with following parameters: ops.minfr_goodchannels = 0.1; ops.Th = [10 5]; ops.lam = 20; ops.AUCsplit = 0.95; ops.ThPre = 8; ops.spkTh = −6.
- Full pipeline: differential/statistical testing [R, ggplot2, tidyverse] -> visualisation [R, ggplot2, tidyverse] -> stage not stated [Kilosort v2.0]

### Correlated variability and its attentional modulation depend on anatomical connectivity. (PNAS 2024)

- DOI: 10.1073/pnas.2318841121 | PMCID: PMC11363273 | PMID: 39172780
- Version used: **2.0**
- Evidence: Some session data were also spike-sorted using the automated spike sorting algorithm Kilosort 2.0 ( 32 ).
- Full pipeline: stage not stated [Kilosort v2.0]

### The olivary input to the cerebellum dissociates sensory events from movement plans. (PNAS 2024)

- DOI: 10.1073/pnas.2318849121 | PMCID: PMC11047103 | PMID: 38630714
- Evidence: We used OpenEphys ( 68 ) for electrophysiology data acquisition, and then used P-sort ( 69 ) to identify the SS and CS in the heptodes and tetrodes recordings, and Kilosort and Phi ( 70 ) to identify the spikes for the silicon probes.
- Full pipeline: stage not stated [Kilosort]

### Efficient mapping of the thalamocortical monosynaptic connectivity in vivo by tangential insertions of high-density electrodes in the cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2313048121 | PMCID: PMC10823237 | PMID: 38241439
- Evidence: Except for sorting with Kilosort ( 31 ) ( https://github.com/MouseLand/Kilosort ) which was done in MATLAB 2018 and 2019 ( www.mathworks.com ), all data analysis was performed in Python 3 ( www.anaconda.com ); statistical tests were performed using either the two-sided Wilcoxon rank-sum test except for the pharmacological recording where we use a two-sided Wilcoxon signed-rank test ( Fig.
- Full pipeline: quantification [SciPy] -> dimensionality reduction/clustering [SciPy] -> differential/statistical testing [Kilosort, Python]

### Population encoding of stimulus features along the visual hierarchy. (PNAS 2024)

- DOI: 10.1073/pnas.2317773121 | PMCID: PMC10823231 | PMID: 38227668
- Evidence: Single units in earlier experiments were identified using MountainSort ( 74 ), or in later experiments Kilosort 3 ( 75 ), in both cases followed by manual curation.
- Full pipeline: stage not stated [Kilosort]

### Neuronal normalization in monkey MT is an intensity-weighted average. (PNAS 2025)

- DOI: 10.1073/pnas.2522104122 | PMCID: PMC12625995 | PMID: 41196346
- Version used: **2.0**
- Evidence: The continuous signal was spike sorted offline using an automated spike sorter (KiloSort 2.0 and KiloSort 4.0) and isolated units were curated using Phy ( 55 ).
- Full pipeline: stage not stated [Kilosort v2.0, SciPy]

### Diverse and dynamic influences of saccades on visual representations in the mouse superior colliculus. (PNAS 2025)

- DOI: 10.1073/pnas.2425788122 | PMCID: PMC12305052 | PMID: 40668831
- Version used: **2.0**
- Evidence: We used Kilosort 2.0, 2.5, and 3.0 to automatically sort extracellular spikes into single- and multiunit clusters.
- Full pipeline: dimensionality reduction/clustering [Kilosort v2.0] -> machine learning [scikit-learn] -> stage not stated [DeepLabCut, PsychoPy]

### Sensory population activity reveals downstream confidence computations in the primate visual system. (PNAS 2025)

- DOI: 10.1073/pnas.2426441122 | PMCID: PMC12232640 | PMID: 40560622
- Evidence: We first automatically spike-sorted the data with Kilosort ( 64 ), followed by manual merging and splitting as needed (with the “phy” user interface, https://github.com/kwikteam/phy ).
- Full pipeline: stage not stated [Kilosort, TensorFlow]

### Multiplexing of cognitive encoding by oculomotor networks leads to incidental gaze shifts. (PNAS 2025)

- DOI: 10.1073/pnas.2422331122 | PMCID: PMC12012544 | PMID: 40198709
- Evidence: Recorded signals were spike-sorted offline (Plexon, Kilosort) except for recordings conducted in the Assad lab which were sorted online with a dual window discriminator (Bak Electronics).
- Full pipeline: stage not stated [Kilosort, Python v3.8]

### Bayesian inference by visuomotor neurons in the prefrontal cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2420815122 | PMCID: PMC12002263 | PMID: 40146856
- Evidence: First, we spike-sorted the data automatically with Kilosort ( 54 ).
- Full pipeline: stage not stated [Kilosort]

### The reuniens thalamus recruits recurrent excitation in the medial prefrontal cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2500321122 | PMCID: PMC11929439 | PMID: 40085651
- Version used: **2.5**
- Evidence: The data were spike-sorted automatically by Kilosort2.5 ( https://github.com/MouseLand/Kilosort ) followed by manual curating using Phy2 ( https://github.com/cortex-lab/phy ).
- Full pipeline: quantification [R] -> differential/statistical testing [R] -> stage not stated [Kilosort v2.5]

### A hemispheric decoding principle for vestibular heading perception in the posterior sylvian area. (PNAS 2026)

- DOI: 10.1073/pnas.2533498123 | PMCID: PMC13187708 | PMID: 42127102
- Version used: **4.0**
- Evidence: Neuronal data acquired via multi-channel recording were spike-sorted offline using Kilosort 4.0 ( 64 ) and subsequently analyzed in MATLAB.
- Full pipeline: stage not stated [Kilosort v4.0]

### Distinct laminar origins of sensory-evoked high-gamma and low-frequency ECoG signals revealed by optogenetics. (PNAS 2026)

- DOI: 10.1073/pnas.2516293123 | PMCID: PMC13056151 | PMID: 41920867
- Evidence: Spike sorting was carried out using Kilosort 3, following the standard preprocessing and analysis described in the reference article ( 40 ).
- Full pipeline: stage not stated [Kilosort]

