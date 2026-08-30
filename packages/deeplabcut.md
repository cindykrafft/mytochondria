# DeepLabCut

- **Category:** neuro-tools
- **Papers in survey:** 71
- **Journals:** Nature (34), PNAS (27), Cell (9), Science (1)
- **Years:** 2021 (3), 2022 (10), 2023 (14), 2024 (19), 2025 (23), 2026 (2)
- **Versions named:** 2.2.0.6 (1), 2.2.3 (1), 2.3.8 (1), 2.2.1.1 (1), 2.2.0.2 (1), 2.2r (1), 2.1.5.2 (1), 2.2.1 (1)
- **Pipeline stages it appears in:** machine learning (13), structure determination (2), dimensionality reduction/clustering (2), quantification (1), simulation/modelling (1), alignment/mapping (1)

## Papers

### Functional diversity for body actions in the mesencephalic locomotor region. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.002 | PMCID: PMC8382160 | PMID: 34302739
- Evidence: ...(v1.2.1 and 1.4.1) Inscopix https://www.inscopix.com Bonsai (v2.3) NeuroGEARS https://bonsai-rx.org CinePlexStudio (v3.7.1) Plexon https://plexon.com DeepLabCut Mathis Lab ( Mathis et al., 2018 ) http://mackenziemathislab.org/deeplabcut Other 200mm: MFC_200/230-0.48_3.5mm_ZF1.25_FLT Mono Fiberoptic Cannula Doric https://neuro.doriclenses.com/ 200mm: MFC_200/230-0.48_6mm_ZF1.25_FLT Mono Fiberoptic ...
- Full pipeline: differential/statistical testing [R, scikit-learn] -> visualisation [seaborn] -> stage not stated [DeepLabCut, Python v3.7, SciPy, ilastik v1.1.5]

### Cell-type-specific population dynamics of diverse reward computations. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.019 | PMCID: PMC10387374 | PMID: 36113428
- Evidence: Video analysis was performed with the open source software DeepLabCut ( Mathis et al., 2018 ), post experimentation.
- Full pipeline: quality control [Kilosort v2.5] -> stage not stated [DeepLabCut, Python]

### Large-scale two-photon calcium imaging in freely moving mice. (Cell 2022)

- DOI: 10.1016/j.cell.2022.02.017 | PMCID: PMC8970296 | PMID: 35305313
- Evidence: ...e-v2021/ Suite2p (python) Pachitariu et al., 2017 https://github.com/MouseLand/suite2p ROIMatchPub Adam Ranson https://github.com/ransona/ROIMatchPub DeepLabCut (python) Mathis et al., 2018 ; Nath et al., 2019 https://github.com/DeepLabCut/DeepLabCut CIAtah(Matlab) Biafra Ahanonu https://github.com/bahanonu/ciatah AnimalTracker (labview program) This paper Zenodo: https://doi.org/10.5281/zenodo.60...
- Full pipeline: stage not stated [DeepLabCut, ImageJ, Suite2p]

### A midbrain-thalamus-cortex circuit reorganizes cortical dynamics to initiate movement. (Cell 2022)

- DOI: 10.1016/j.cell.2022.02.006 | PMCID: PMC8990337 | PMID: 35245431
- Evidence: We used DeepLabCut ( Mathis et al., 2018 ) to track the movement of the tongue, jaw, and nose ( Figure 1B ; Supplementary movies 1 and 2 ).
- Full pipeline: stage not stated [DeepLabCut]

### Generating parallel representations of position and identity in the olfactory system. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.038 | PMCID: PMC10403364 | PMID: 37236194
- Evidence: 79 RRID: SCR_006278 Fiji Open source RRID: SCR_002285 Bonsai Open source RRID: SCR_017218 DeepLabCut Open source, Mathis et al.
- Full pipeline: differential/statistical testing [survival (R)] -> stage not stated [DeepLabCut, ImageJ, R]

### Structural and functional map for forelimb movement phases between cortex and medulla. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.009 | PMCID: PMC9842395 | PMID: 36608651
- Evidence: ...m/MouseLand/Kilosort/releases/tag/v2.0 Kilosort v3 Cortex lab https://github.com/MouseLand/Kilosort Phy2 Cortex lab https://github.com/cortex-lab/phy DeepLabCut Mathis Lab; Mathis et al.
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [DeepLabCut, Kilosort, Python v3.7, SciPy, TrackMate v6.0.3, scikit-learn]

### Co-opting templated aggregation to degrade pathogenic tau assemblies and improve motor function. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.024 | PMCID: PMC7616835 | PMID: 39276772
- Evidence: ...us-P2A-Tau-RING I18R/M72E This paper N/A AAV PHP.eB-CAG-Venus This paper N/A AAV PHP.eB-CAG-Venus-P2A-Tau-RING This paper N/A Software and algorithms DeepLabCut Mathis et al.
- Full pipeline: stage not stated [DeepLabCut, ImageJ]

### Imaging high-frequency voltage dynamics in multiple neuron classes of behaving mammals. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.028 | PMCID: PMC12616578 | PMID: 40675148
- Version used: **2.2.1**
- Evidence: Behavioral video tracking and pose estimation for freely moving mice To track the mouse’s two-dimensional ( x-y ) position in the raw.avi behavioral movies ( Figures 1 and 3 ), we used the deep learning-based animal tracking algorithm, DeepLabCut (version 2.2.1).
- Full pipeline: dimensionality reduction/clustering [DeepLabCut v2.2.1] -> machine learning [DeepLabCut v2.2.1] -> stage not stated [Psychtoolbox]

### Dopamine encodes deep network teaching signals for individual learning trajectories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.025 | PMCID: PMC7619352 | PMID: 40505657
- Evidence: Pupil analysis We used DeepLabCut 72 to track several points on the mice’s left pupil throughout each task trial.
- Full pipeline: normalisation [scikit-learn] -> differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Matplotlib, NumPy, PyTorch v2.5.1, Python, SciPy, seaborn, statsmodels]

### Mouse prefrontal cortex represents learned rules for categorization. (Nature 2021)

- DOI: 10.1038/s41586-021-03452-z | PMCID: PMC8131197 | PMID: 33883745
- Evidence: 10 ) were manually defined and automatically annotated using DeepLabCut 41 , 42 .
- Full pipeline: stage not stated [DeepLabCut]

### Distinguishing externally from saccade-induced motion in visual cortex. (Nature 2022)

- DOI: 10.1038/s41586-022-05196-w | PMCID: PMC9534749 | PMID: 36104560
- Evidence: In freely moving mice, to delineate the pupil, eight points along the edge of the pupil were tracked post hoc using DeepLabCut 55 and were fitted with an ellipse.
- Full pipeline: visualisation [Kilosort] -> stage not stated [DeepLabCut]

### Hippocampal place cells have goal-oriented vector fields during navigation. (Nature 2022)

- DOI: 10.1038/s41586-022-04913-9 | PMCID: PMC9329099 | PMID: 35794477
- Evidence: Tracking was performed offline using DeepLabCut 33 .
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> stage not stated [DeepLabCut]

### Vagal sensory neurons mediate the Bezold-Jarisch reflex and induce syncope. (Nature 2023)

- DOI: 10.1038/s41586-023-06680-7 | PMCID: PMC10632149 | PMID: 37914931
- Evidence: Video processing We used open-source software FaceMap 38 , 62 and DeepLabCut 63 .
- Full pipeline: visualisation [Seurat] -> stage not stated [DeepLabCut]

### A rise-to-threshold process for a relative-value decision. (Nature 2023)

- DOI: 10.1038/s41586-023-06271-6 | PMCID: PMC10356611 | PMID: 37407812
- Evidence: DeepLabCut 50 was used for offline tracking of body parts, including the neck and ovipositor.
- Full pipeline: registration [CaImAn] -> stage not stated [DeepLabCut, Fiji, ImageJ]

### Dynamic synchronization between hippocampal representations and stepping. (Nature 2023)

- DOI: 10.1038/s41586-023-05928-6 | PMCID: PMC10156593 | PMID: 37046088
- Evidence: A machine-learning algorithm, DeepLabCut 65 (v.2.0.5.1), was trained to track the distinct body parts of the rats, including the nose, forelimbs, hindlimbs and base of the tail.
- Full pipeline: machine learning [DeepLabCut]

### Central pattern generator control of a vertebrate ultradian sleep rhythm. (Nature 2024)

- DOI: 10.1038/s41586-024-08162-w | PMCID: PMC11655359 | PMID: 39506115
- Evidence: 3b ), we used DeepLabCut ( https://github.com/DeepLabCut ) to track four points of each eye (midpoint of upper eyelid, midpoint of lower eyelid, left corner and right corner) from our continuous infrared camera recordings.
- Full pipeline: differential/statistical testing [pandas v2.0.3, xarray v2023.6.0] -> stage not stated [DeepLabCut, NumPy, Python, SciPy]

### A cellular basis for mapping behavioural structure. (Nature 2024)

- DOI: 10.1038/s41586-024-08145-x | PMCID: PMC11655361 | PMID: 39506112
- Evidence: We performed tracking of the mice in the video data using DeepLabCut 61 (version 2.0), a Python package for marker-less pose estimation based in the TensorFlow machine learning library.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Matplotlib v3.7.3, NumPy v1.22.0, SciPy v1.10.1, TensorFlow, seaborn v0.13.2]

### A subcortical feeding circuit linking an interoceptive node to jaw movement. (Nature 2024)

- DOI: 10.1038/s41586-024-08098-1 | PMCID: PMC11618074 | PMID: 39443799
- Evidence: Jaw pose was subsequently estimated with DeepLabCut 68 .
- Full pipeline: quantification [ImageJ] -> stage not stated [DeepLabCut]

### One-shot entorhinal maps enable flexible navigation in novel environments. (Nature 2024)

- DOI: 10.1038/s41586-024-08034-3 | PMCID: PMC11602719 | PMID: 39385034
- Version used: **2.2.0.6**
- Evidence: First, for each arena, we manually labelled 20 frames each from 4 videos and trained a DeepLabCut (v2.2.0.6) 58 , 59 ResNet-50-based neural network for up to 100,000 iterations, as test error plateaued after this.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [DeepLabCut v2.2.0.6] -> stage not stated [Kilosort, Python, SciPy]

### Neural circuit mechanisms underlying context-specific halting in Drosophila. (Nature 2024)

- DOI: 10.1038/s41586-024-07854-7 | PMCID: PMC11446846 | PMID: 39358520
- Version used: **2.2.3**
- Evidence: Camera calibration, two-dimensional pose tracking and 3D pose reconstruction We used DeepLabCut (v.2.2.3, DLC 67 ) to track 33 points of interest on the fly body: the notum, two wing hinges and five joints per leg (thorax-coxa, coxa-trocanter, Fe–Ti, tibia-tarsus and the tarsal tip).
- Full pipeline: dimensionality reduction/clustering [DeepLabCut v2.2.3] -> structure determination [DeepLabCut v2.2.3] -> stage not stated [Cytoscape, ImageJ, Python]

### Brain-wide dynamics linking sensation to action during decision-making. (Nature 2024)

- DOI: 10.1038/s41586-024-07908-w | PMCID: PMC11499283 | PMID: 39261727
- Evidence: Pupil size In order to estimate the pupil size, we trained DeepLabCut 66 to track the pupil size and position using videos acquired with the side camera.
- Full pipeline: machine learning [DeepLabCut] -> stage not stated [Kilosort v2.0, NumPy, PyTorch, SciPy]

### Neural circuit basis of placebo pain relief. (Nature 2024)

- DOI: 10.1038/s41586-024-07816-z | PMCID: PMC11358037 | PMID: 39048016
- Evidence: The recorded videos were analysed using the machine-learning-based algorithm DeepLabCut 67 or Ethovision XT15 (Noldus).
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, UMAP] -> differential/statistical testing [Seurat v4.0] -> stage not stated [DeepLabCut, ImageJ, R]

### Kinetic features dictate sensorimotor alignment in the superior colliculus. (Nature 2024)

- DOI: 10.1038/s41586-024-07619-2 | PMCID: PMC11236723 | PMID: 38961292
- Evidence: The labelled data were used to train a deep convolutional network via transfer learning using open source code 61 ( https://github.com/AlexEMG/DeepLabCut ).
- Full pipeline: stage not stated [CaImAn, DeepLabCut, PsychoPy, Python]

### Distinct µ-opioid ensembles trigger positive and negative fentanyl reinforcement. (Nature 2024)

- DOI: 10.1038/s41586-024-07440-x | PMCID: PMC11153127 | PMID: 38778097
- Evidence: Video data analysis The videos, which have a resolution of 640×480 and a frame rate of 40 fps, were analysed with DeepLabCut 18 .
- Full pipeline: stage not stated [DeepLabCut, ImageJ]

### Volatile working memory representations crystallize with practice. (Nature 2024)

- DOI: 10.1038/s41586-024-07425-w | PMCID: PMC11136659 | PMID: 38750359
- Evidence: To determine whether a neuron’s response was related to the animals’ motor activity, we used DeepLabCut 41 to find the position of the animals’ paws from which we extracted the animals’ movements.
- Full pipeline: stage not stated [DeepLabCut, Kilosort, Suite2p]

### Neural and behavioural state switching during hippocampal dentate spikes. (Nature 2024)

- DOI: 10.1038/s41586-024-07192-8 | PMCID: PMC11023929 | PMID: 38480889
- Evidence: The head position of mice was tracked in real-time using an overhead web camera (Logitech, 30 frames per s) running custom scripts on Bonsai ( https://bonsai-rx.org/ ) with a pretrained model from DeepLabCut ( https://deeplabcut.github.io/DeepLabCut/README.html ).
- Full pipeline: dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [Python] -> machine learning [DeepLabCut] -> stage not stated [Kilosort, NetworkX]

### Visuo-frontal interactions during social learning in freely moving macaques. (Nature 2024)

- DOI: 10.1038/s41586-024-07084-x | PMCID: PMC10959748 | PMID: 38355804
- Evidence: The zero values at 1 second are due to a blink, while the zero values of x and y coordinates at 7 seconds are due to the animal viewing an object located out of the field of view captured by the scene camera. d , Number of objects (sorted) that DeepLabCut labeled in the scene camera frames from one session. e , Session-averaged percentage of scene camera frames out of total recorded that contained...
- Full pipeline: stage not stated [DeepLabCut]

### Arousal as a universal embedding for spatiotemporal brain dynamics. (Nature 2025)

- DOI: 10.1038/s41586-025-09544-4 | PMCID: PMC12611781 | PMID: 40993399
- Evidence: From the face videography, we derived scalar indices of pupil size via DeepLabCut software 77 and whisker motion via the Lucas–Kanade optical flow method 78 applied to and subsequently averaged across five manually selected data points on the whiskers.
- Full pipeline: stage not stated [DeepLabCut, SciPy, scikit-learn]

### A brain-wide map of neural activity during complex behaviour. (Nature 2025)

- DOI: 10.1038/s41586-025-09235-0 | PMCID: PMC12408349 | PMID: 40903598
- Evidence: The whisker pad area was empirically defined using a rectangular bounding box anchored between the nose tip and the eye, both found using DeepLabCut 106 (DLC; see more below).
- Full pipeline: differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5, Python]

### Brain-wide representations of prior information in mouse decision-making. (Nature 2025)

- DOI: 10.1038/s41586-025-09226-1 | PMCID: PMC12408363 | PMID: 40903597
- Evidence: DeepLabCut was not able to achieve sufficiently reliable tracking of the pupils; we therefore used a different pose-estimation algorithm 56 , trained on the same labelled dataset used to train DeepLabCut.
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [DeepLabCut]

### The neural basis of species-specific defensive behaviour in Peromyscus mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09241-2 | PMCID: PMC12422964 | PMID: 40702175
- Evidence: Analysis of optogenetically induced behaviour We extracted the head position of mice from each video with DeepLabCut 73 (v.2.1.9 or newer) and used this to estimate the movement speed of each mouse during optogenetic stimulation.
- Full pipeline: quantification [QuPath v0.2.3] -> normalisation [StarDist] -> differential/statistical testing [Python v3.6.0, R, lme4, scikit-learn] -> machine learning [StarDist] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Psychtoolbox, emmeans]

### Dynamic basal ganglia output signals license and suppress forelimb movements. (Nature 2025)

- DOI: 10.1038/s41586-025-09066-z | PMCID: PMC12367548 | PMID: 40437098
- Evidence: Behavioural analysis in the forelimb reaching task For analysis of forelimb movements executed during the forelimb task, we applied deep-neural-network-based markerless pose estimation using DeepLabCut 63 coupled with high-speed videography of the bottom view of the mouse at 100 fps to track the moving hand and the slit.
- Full pipeline: visualisation [ImageJ] -> stage not stated [DeepLabCut, Kilosort, Python]

### Dopaminergic action prediction errors serve as a value-free teaching signal. (Nature 2025)

- DOI: 10.1038/s41586-025-09008-9 | PMCID: PMC12310545 | PMID: 40369067
- Evidence: Video tracking during photometry recordings and quantification of movement parameters The position of the mouse was tracked using DeepLabCut 71 and variables such as speed, acceleration, angular velocity and angular acceleration were calculated using custom scripts in Python.
- Full pipeline: quantification [DeepLabCut] -> differential/statistical testing [Python, scikit-learn, statsmodels] -> stage not stated [SciPy, pingouin]

### Striatum supports fast learning but not memory recall. (Nature 2025)

- DOI: 10.1038/s41586-025-08969-1 | PMCID: PMC12244412 | PMID: 40335692
- Evidence: We used DeepLabCut 51 to track the 2D position of the paw in each mirror.
- Full pipeline: stage not stated [DeepLabCut, PyTorch, Python, scikit-learn]

### NEURD offers automated proofreading and feature extraction for connectomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08660-5 | PMCID: PMC11981913 | PMID: 40205208
- Evidence: ...alities such as calcium imaging (CaImAn 7 and Suite2P 8 ), Neuropixels recordings (KiloSort 9 and MountainSort 10 ), label-free behavioural tracking (DeepLabCut 11 , MoSeq 12 and SLEAP 13 ) and spatial transcriptomics (Giotto 14 and Squidpy 15 ), the goal of NEURD is to make ‘big neuroscience data’ (in this case, large-scale electron microscopy reconstructions) accessible to a larger community.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [DeepLabCut, SLEAP, Squidpy] -> stage not stated [CaImAn, Kilosort, NetworkX, Python]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Evidence: A DeepLabCut model 49 was trained on 17 manually labelled samples from 11 animals to label each frame of the compressed eye video (intraframe only H.264 compression, CRF:17) with 8 eyelid points and 8 pupil points at cardinal and intercardinal positions.
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### Foundation model of neural activity predicts response to new stimulus types. (Nature 2025)

- DOI: 10.1038/s41586-025-08829-y | PMCID: PMC11981942 | PMID: 40205215
- Evidence: A DeepLabCut model 40 was trained on 17 manually labelled samples from 11 mice to label each frame of the compressed eye video (intraframe only H.264 compression, CRF:17) with 8 eyelid points and 8 pupil points at cardinal and intercardinal positions.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [DeepLabCut] -> visualisation [UMAP] -> stage not stated [Psychtoolbox]

### Changes in neurotensin signalling drive hedonic devaluation in obesity. (Nature 2025)

- DOI: 10.1038/s41586-025-08748-y | PMCID: PMC12119351 | PMID: 40140571
- Evidence: Video-based analysis of behavioural motifs A video-based offline tracking was performed via DeepLabCut 66 .
- Full pipeline: alignment/mapping [kallisto v0.45.1] -> normalisation [kallisto v0.45.1] -> differential/statistical testing [edgeR v3.24.3] -> stage not stated [DeepLabCut, ImageJ, Python v3.6.7, R v3.5.1]

### A hypothalamic circuit underlying the dynamic control of social homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-08617-8 | PMCID: PMC12018270 | PMID: 40011768
- Evidence: Custom MATLAB codes and DeepLabCut software package were used to track frame-by-frame positions of two mice during social reunion, and the social distances between two mice were calculated and averaged across frames during one reunion session (Fig.
- Full pipeline: stage not stated [DeepLabCut, QuPath v0.3.2]

### Left-right-alternating theta sweeps in entorhinal-hippocampal maps of space. (Nature 2025)

- DOI: 10.1038/s41586-024-08527-1 | PMCID: PMC11946909 | PMID: 39900625
- Evidence: DeepLabCut 69 was used to track the positions of each paw, snout and tail base.
- Full pipeline: dimensionality reduction/clustering [Matplotlib, NumPy, Scanpy, SciPy, UMAP, scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5]

### Understanding the neural code of stress to control anhedonia. (Nature 2025)

- DOI: 10.1038/s41586-024-08241-y | PMCID: PMC11735319 | PMID: 39633053
- Evidence: We tracked 12 keypoints using DeepLabCut 65 .
- Full pipeline: dimensionality reduction/clustering [Python, scikit-learn] -> stage not stated [DeepLabCut, Kilosort]

### A combinatorial neural code for long-term motor memory. (Nature 2025)

- DOI: 10.1038/s41586-024-08193-3 | PMCID: PMC11735397 | PMID: 39537930
- Evidence: Video data analysis We used DeepLabCut 69 to track manually defined body parts.
- Full pipeline: registration [Suite2p] -> stage not stated [DeepLabCut]

### Mimicking opioid analgesia in cortical pain circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09908-w | PMCID: PMC12823415 | PMID: 41501467
- Evidence: Using DeepLabCut (DLC) 53 to track 20 body key points, LUPE extracted detailed posture dynamics that were processed through both semi-supervised (A-SOiD 54 ) and unsupervised (B-SOiD 55 ) algorithms to identify six holistic behavioural repertoires: still, walk, rear, groom, lick left hindpaw and lick right hindpaw (Fig.
- Full pipeline: read trimming [STAR v2.7.1] -> alignment/mapping [STAR v2.7.1] -> dimensionality reduction/clustering [DESeq2, Seurat v4.3, SoupX, UMAP, scDblFinder] -> stage not stated [DeepLabCut]

### Neural circuit mechanisms of sensorimotor disability in cancer treatment. (PNAS 2021)

- DOI: 10.1073/pnas.2100428118 | PMCID: PMC8713769 | PMID: 34911753
- Version used: **2.1.5.2**
- Evidence: Video recordings were analyzed on a computer equipped with DeepLabCut (version 2.1.5.2), a software based on deep learning to track user-defined body parts ( 67 , 68 ).
- Full pipeline: machine learning [DeepLabCut v2.1.5.2] -> stage not stated [R v3.5.0, rstanarm]

### Activity in a prefrontal-periaqueductal gray circuit overcomes behavioral and endocrine features of the passive coping stress response. (PNAS 2022)

- DOI: 10.1073/pnas.2210783119 | PMCID: PMC9636920 | PMID: 36306326
- Evidence: Videos of SPDB were analyzed with DeepLabCut software ( 120 ).
- Full pipeline: stage not stated [DeepLabCut, ImageJ]

### TFG regulates secretory and endosomal sorting pathways in neurons to promote their activity and maintenance. (PNAS 2022)

- DOI: 10.1073/pnas.2210649119 | PMCID: PMC9546632 | PMID: 36161950
- Evidence: DeepLabCut was used to extract representative frames from each video, and at least 350 frames were manually annotated and used to train a convolution neural network that was capable of pose estimation tracking ( 44 ).
- Full pipeline: machine learning [DeepLabCut] -> stage not stated [ImageJ]

### Regularly occurring bouts of retinal movements suggest an REM sleep-like state in jumping spiders. (PNAS 2022)

- DOI: 10.1073/pnas.2204754119 | PMCID: PMC9388130 | PMID: 35939710
- Evidence: We also trained a neural network using DeepLabCut ( SI Appendix ), allowing us to estimate angular movement of each retina to illustrate retinal tube movements and visibility of the spider ( Fig.
- Full pipeline: machine learning [DeepLabCut]

### Coordinating tiny limbs and long bodies: Geometric mechanics of lizard terrestrial swimming. (PNAS 2022)

- DOI: 10.1073/pnas.2118456119 | PMCID: PMC9271186 | PMID: 35759665
- Evidence: Positional data were extracted from videos with the animal-pose estimation software DeepLabCut (DLC) ( 23 ).
- Full pipeline: stage not stated [DeepLabCut]

### A unidirectional but not uniform striatal landscape of dopamine signaling for motivational stimuli. (PNAS 2022)

- DOI: 10.1073/pnas.2117270119 | PMCID: PMC9171911 | PMID: 35594399
- Evidence: DeepLabCut software ( 90 ) was used to track rat position in the operant chamber using video data recorded during FSCV measurements.
- Full pipeline: stage not stated [DeepLabCut]

### Sexual differentiation of neural mechanisms of stress sensitivity during puberty. (PNAS 2023)

- DOI: 10.1073/pnas.2306475120 | PMCID: PMC10614610 | PMID: 37847733
- Evidence: Using DeepLabCut ( Fig.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [R] -> stage not stated [DeepLabCut]

### Activity of estrogen receptor β expressing neurons in the medial amygdala regulates preference toward receptive females in male mice. (PNAS 2023)

- DOI: 10.1073/pnas.2305950120 | PMCID: PMC10589649 | PMID: 37819977
- Evidence: The processed fiber photometry data were analyzed and aligned with animal behavioral annotations derived from Behavioral Observation Research Interactive Software (BORIS) ( 50 ) and DeepLabCut ( 51 ) data using Python (ver.
- Full pipeline: alignment/mapping [DeepLabCut]

### Synaptic and cellular endocannabinoid signaling mechanisms regulate stress-induced plasticity of nucleus accumbens somatostatin neurons. (PNAS 2023)

- DOI: 10.1073/pnas.2300585120 | PMCID: PMC10450650 | PMID: 37590414
- Evidence: Active struggle bouts were flagged by DeepLabCut as previously described ( 26 ).
- Full pipeline: differential/statistical testing [R, tidyverse] -> stage not stated [DeepLabCut]

### The mechanosensitive ion channel Piezo1 contributes to ultrasound neuromodulation. (PNAS 2023)

- DOI: 10.1073/pnas.2300291120 | PMCID: PMC10161134 | PMID: 37098060
- Evidence: Videos were captured at a rate of 30 Hz, which was later analyzed by an open-source machine learning toolkit for animal pose estimation DeepLabCut.
- Full pipeline: stage not stated [DeepLabCut, ImageJ]

### The temporal structure of REM sleep shows minute-scale fluctuations across brain and body in mice and humans. (PNAS 2023)

- DOI: 10.1073/pnas.2213438120 | PMCID: PMC10161068 | PMID: 37094161
- Evidence: Facial movements were tracked using DeepLabCut (DLC) ( 28 ).
- Full pipeline: stage not stated [DeepLabCut]

### Associative learning in the cnidarian <i>Nematostella vectensis</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2220685120 | PMCID: PMC10068830 | PMID: 36940325
- Version used: **2.2.0.2**
- Evidence: Animals’ body parts were tracked using DeepLabCut 2.2.0.2 ( 13 ), and the data were analyzed in R ( 17 ).
- Full pipeline: stage not stated [DeepLabCut v2.2.0.2, R]

### A complete biomechanical model of <i>Hydra</i> contractile behaviors, from neural drive to muscle to movement. (PNAS 2023)

- DOI: 10.1073/pnas.2210439120 | PMCID: PMC10089167 | PMID: 36897982
- Evidence: Acquired movies were processed using a combination of ImageJ ( 133 ), the Icy Imaging software suite ( 134 ), DeepLabCut ( 135 ), and custom scripts ( 136 ), with a pipeline shown in Fig.
- Full pipeline: stage not stated [DeepLabCut, ImageJ]

### Encoding of dynamic facial information in the middle dorsal face area. (PNAS 2023)

- DOI: 10.1073/pnas.2212735120 | PMCID: PMC9974491 | PMID: 36787369
- Evidence: To calculate the motion energy of the head, eyes, and mouth in natural face movies, we first tracked facial features using DeepLabCut ( Fig.
- Full pipeline: stage not stated [DeepLabCut]

### Behavioral encoding across timescales by region-specific dopamine dynamics. (PNAS 2023)

- DOI: 10.1073/pnas.2215230120 | PMCID: PMC9963838 | PMID: 36749722
- Version used: **2.2r**
- Evidence: Using top-down recorded videos, mice were tracked using DeepLabCut v2.2rc3 ( 43 ).
- Full pipeline: stage not stated [DeepLabCut v2.2r]

### Geometric phase predicts locomotion performance in undulating living systems across scales. (PNAS 2024)

- DOI: 10.1073/pnas.2320517121 | PMCID: PMC11181092 | PMID: 38848301
- Evidence: For turning data, DeepLabCut ( 92 ) was used to track the self-occluding postures where binarization and skeletonization fails.
- Full pipeline: stage not stated [DeepLabCut]

### Mosaicism-independent mechanisms contribute to Pcdh19-related epilepsy and repetitive behaviors in <i>Xenopus</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2321388121 | PMCID: PMC11126968 | PMID: 38748583
- Evidence: We analyzed the swimming behaviors of complete or mosaic knockdown tadpoles as previously described ( 10 , 11 ) in a 2.5 cm arena for 10 min, extracted their poses using DeepLabCut trained with our dataset, and analyzed the swimming trajectory, swimming activity, and abrupt turning behaviors ( Fig.
- Full pipeline: simulation/modelling [DeepLabCut] -> machine learning [DeepLabCut]

### Predation without direction selectivity. (PNAS 2024)

- DOI: 10.1073/pnas.2317218121 | PMCID: PMC10962952 | PMID: 38483997
- Evidence: Overhead videos were analyzed in DeepLabCut ( 57 , 58 ) to track the positions of the cricket and the mouse’s ears, nose, and tail base.
- Full pipeline: stage not stated [DeepLabCut, OpenCV, PsychoPy]

### Extinct and extant termites reveal the fidelity of behavior fossilization in amber. (PNAS 2024)

- DOI: 10.1073/pnas.2308922121 | PMCID: PMC10963005 | PMID: 38442141
- Version used: **2.2.1.1**
- Evidence: We used DeepLabCut (version 2.2.1.1) for body part tracking ( 47 , 48 ).
- Full pipeline: differential/statistical testing [R] -> stage not stated [DeepLabCut v2.2.1.1]

### Visual guidance fine-tunes probing movements of an insect appendage. (PNAS 2024)

- DOI: 10.1073/pnas.2306937121 | PMCID: PMC10861887 | PMID: 38285936
- Evidence: We used DeepLabCut ( 49 ) to automatically identify the proboscis, head, and thorax position of the hawkmoths ( Fig.
- Full pipeline: alignment/mapping [R v4.1, lme4] -> differential/statistical testing [R v4.1, lme4] -> stage not stated [DeepLabCut]

### Basal forebrain cholinergic activity is necessary for upward firing rate homeostasis in the rodent visual cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2317987121 | PMCID: PMC10769829 | PMID: 38147559
- Evidence: Behavioral state scoring was performed as previously described ( 4 , 8 ), except animal movement was tracked from video recordings using DeepLabCut ( 54 ).
- Full pipeline: stage not stated [DeepLabCut]

### Ultradian rhythms of CRH<sup>PVN</sup> neuron activity, behavior, and stress hormone secretion. (PNAS 2025)

- DOI: 10.1073/pnas.2510083122 | PMCID: PMC12337306 | PMID: 40748956
- Evidence: DeepLabCut was used to track animal movement ( 34 , 48 ).
- Full pipeline: stage not stated [DeepLabCut]

### Diverse and dynamic influences of saccades on visual representations in the mouse superior colliculus. (PNAS 2025)

- DOI: 10.1073/pnas.2425788122 | PMCID: PMC12305052 | PMID: 40668831
- Evidence: The position of the pupil center was tracked offline using open source pose estimation software (DeepLabCut).
- Full pipeline: dimensionality reduction/clustering [Kilosort v2.0] -> machine learning [scikit-learn] -> stage not stated [DeepLabCut, PsychoPy]

### A genetically defined pontine nucleus essential for ingestion in mice. (PNAS 2025)

- DOI: 10.1073/pnas.2411174122 | PMCID: PMC12305073 | PMID: 40663610
- Version used: **2.3.8**
- Evidence: A ResNet-50 deep learning model was trained using DeepLabCut (version 2.3.8) on profile frames of mouse faces, to identify the genu of the jaw.
- Full pipeline: differential/statistical testing [NumPy] -> machine learning [DeepLabCut v2.3.8] -> stage not stated [Fiji, ImageJ, Python, SciPy]

### Dopamine induces fear extinction by activating the reward-responding amygdala neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2501331122 | PMCID: PMC12067255 | PMID: 40294263
- Evidence: Behavior videos were recorded with VideoFreeze software and freezing level was scored manually by experimenters who were blinded to conditions or automatically with DeepLabCut behavior analysis toolbox and custom Python code ( 68 ).
- Full pipeline: alignment/mapping [Python] -> stage not stated [DeepLabCut, ImageJ]

### Active vision in freely moving marmosets using head-mounted eye tracking. (PNAS 2025)

- DOI: 10.1073/pnas.2412954122 | PMCID: PMC11831172 | PMID: 39899712
- Evidence: Such approaches have been successfully applied using commercial software (e.g., DeepLabCut), to track the pupil of freely moving mice ( 16 ).
- Full pipeline: stage not stated [DeepLabCut]

### Place cells in CA1 lack topographical organization of firing locations. (PNAS 2026)

- DOI: 10.1073/pnas.2528601123 | PMCID: PMC12933062 | PMID: 41706904
- Evidence: Body parts (ears, head center, body center, tail root) of the animals in each frame of the tracking movie were detected using DeepLabCut ( 56 ).
- Full pipeline: registration [Suite2p] -> stage not stated [DeepLabCut]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: Videos were analyzed using DeepLabCut ( 61 ) to extract eye closure.
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

