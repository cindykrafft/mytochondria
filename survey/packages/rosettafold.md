# RoseTTAFold

- **Category:** structbio
- **Papers in survey:** 59
- **Journals:** PNAS (43), Nature (13), Science (3)
- **Years:** 2021 (1), 2022 (7), 2023 (16), 2024 (13), 2025 (18), 2026 (4)
- **Pipeline stages it appears in:** machine learning (7), structure determination (3), dimensionality reduction/clustering (2), alignment/mapping (2), differential/statistical testing (1), quantification (1), simulation/modelling (1)

## Papers

### Structures and mechanism of the plant PIN-FORMED auxin transporter. (Nature 2022)

- DOI: 10.1038/s41586-022-04883-y | PMCID: PMC9477730 | PMID: 35768502
- Evidence: Model building and refinement A PIN8 model prediction was calculated using the RoseTTAFold server 40 and docked into the PIN8 map in Chimera 41 .
- Full pipeline: alignment/mapping [MAFFT] -> structure determination [PHENIX, RoseTTAFold] -> visualisation [PyMOL] -> stage not stated [Coot]

### De novo design of protein structure and function with RFdiffusion. (Nature 2023)

- DOI: 10.1038/s41586-023-06415-8 | PMCID: PMC10468394 | PMID: 37433327
- Evidence: 17 ) (AF2) and RoseTTAFold 18 (RF).
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold]

### Mirusviruses link herpesviruses to giant viruses. (Nature 2023)

- DOI: 10.1038/s41586-023-05962-4 | PMCID: PMC10132985 | PMID: 37076623
- Evidence: 66 , 67 ) (using Cobafold v1.4) and RoseTTAFold 68 v.1.1.0.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [BLAST, BWA v0.7.15, MAFFT, SAMtools] -> dimensionality reduction/clustering [OrthoFinder] -> differential/statistical testing [IQ-TREE, SAMtools] -> structure determination [BLAST, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, RoseTTAFold]

### Accurate structure prediction of biomolecular interactions with AlphaFold 3. (Nature 2024)

- DOI: 10.1038/s41586-024-07487-w | PMCID: PMC11168924 | PMID: 38718835
- Evidence: Even so, AF3 greatly outperforms classical docking tools such as Vina 37 , 38 even while not using any structural inputs (Fisher’s exact test, P = 2.27 × 10 −13 ) and greatly outperforms all other true blind docking like RoseTTAFold All-Atom ( P = 4.45 × 10 −25 ).
- Full pipeline: visualisation [NumPy v1.26.3, SciPy v1.9.3, seaborn v0.12.2] -> stage not stated [AlphaFold, Matplotlib v3.6.1, RDKit, RoseTTAFold, statsmodels v0.12.2]

### Streptomyces umbrella toxin particles block hyphal growth of competing species. (Nature 2024)

- DOI: 10.1038/s41586-024-07298-z | PMCID: PMC11062931 | PMID: 38632398
- Evidence: Notably, RoseTTAFold generated confident models for UmbB1–ALF complexes that closely matched those in our structure for each of the UmbB1-binding ALFs, but not for ALF6 or the other non-UmbB1-binding repeats (Extended Data Fig.
- Full pipeline: alignment/mapping [ColabFold] -> structure determination [Coot, Topaz] -> machine learning [Topaz] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, CTFFIND, Python, RELION, RoseTTAFold, napari]

### De novo design of high-affinity binders of bioactive helical peptides. (Nature 2024)

- DOI: 10.1038/s41586-023-06953-1 | PMCID: PMC10849960 | PMID: 38109936
- Evidence: Overview of ‘base’ RFdiffusion training RFdiffusion 8 is a denoising diffusion probabilistic model fine-tuned from a pretrained structure prediction model; RoseTTAFold 57 , 58 .
- Full pipeline: machine learning [RoseTTAFold] -> stage not stated [AlphaFold]

### Design of facilitated dissociation enables timing of cytokine signalling. (Nature 2025)

- DOI: 10.1038/s41586-025-09549-z | PMCID: PMC12611780 | PMID: 40993395
- Evidence: For the initial fusions including AS0, we extracted the centre four residues of the placeholder helix, then used inpainting with RosettaFold 56 to scaffold that fragment between the switch and the binder.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [CCP4] -> differential/statistical testing [DESeq2] -> simulation/modelling [MDAnalysis] -> structure determination [PHENIX] -> machine learning [AlphaFold] -> stage not stated [GROMACS v2020.2, PyMOL, RoseTTAFold]

### Diffusing protein binders to intrinsically disordered proteins. (Nature 2025)

- DOI: 10.1038/s41586-025-09248-9 | PMCID: PMC12367549 | PMID: 40739343
- Evidence: For an overview of ‘base’ RFdiffusion training, Rfdiffusion 5 is a denoising diffusion probabilistic model, which is fine-tuned from the RoseTTAFold structure prediction model 25 , 56 .
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX v1.21.1] -> machine learning [RoseTTAFold] -> stage not stated [AlphaFold, ImageJ v1.54p, PyMOL v2.4.0, Python v3.9.7, UCSF Chimera v1.14]

### DNA-guided transcription factor interactions extend human gene regulatory code. (Nature 2025)

- DOI: 10.1038/s41586-025-08844-z | PMCID: PMC12119339 | PMID: 40205063
- Evidence: Recently released versions of RoseTTAFold (RoseTTAFold2NA v.0.2) 39 and AlphaFold (AlphaFold v.3.0) 40 , which can predict the structures of protein–nucleic acid complexes ( Methods ), performed much better in predicting the overall geometry of TF–TF–DNA complexes (Fig.
- Full pipeline: differential/statistical testing [Bioconductor, ComplexHeatmap, Python, R, SciPy] -> structure determination [CCP4, PHENIX] -> machine learning [R] -> visualisation [Bioconductor, ComplexHeatmap] -> stage not stated [AlphaFold v2.0, BEDTools v2.30.0, Cytoscape, PyMOL, RoseTTAFold]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: The structures were solved by molecular replacement with Phaser 80 v.2.7.0, using a RoseTTAFold (v.1)-generated model 81 as a search model.
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### Targeting protein-ligand neosurfaces with a generalizable deep learning tool. (Nature 2025)

- DOI: 10.1038/s41586-024-08435-4 | PMCID: PMC11903328 | PMID: 39814890
- Evidence: 1b ), whereas the state-of-art RoseTTAFold All-Atom 27 recovered only 14% (4) of correct binding poses (Supplementary Fig.
- Full pipeline: structure determination [Coot v0.9.5] -> visualisation [ChimeraX, PyMOL v2.4] -> stage not stated [AlphaFold, ColabFold, PHENIX, RDKit, RoseTTAFold]

### Designed endocytosis-inducing proteins degrade targets and amplify signals. (Nature 2025)

- DOI: 10.1038/s41586-024-07948-2 | PMCID: PMC11839401 | PMID: 39322662
- Evidence: The best inpainting outputs were selected by RosettaFold LDDT metrics (>0.5) for the inpainted region and used for sequence design with ProteinMPNN.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, Python, RoseTTAFold]

### LetA defines a structurally distinct transporter family. (Nature 2026)

- DOI: 10.1038/s41586-025-09990-0 | PMCID: PMC13017536 | PMID: 41565823
- Evidence: 58 ) and RoseTTAFold 59 became public.
- Full pipeline: alignment/mapping [Bowtie2, MUSCLE v3.8.31, PyMOL] -> normalisation [ImageJ] -> simulation/modelling [NAMD] -> structure determination [ChimeraX, PHENIX] -> stage not stated [AlphaFold, Cutadapt v1.9.1, MotionCor2, Python, RELION v3.1.0, RoseTTAFold, SAMtools v1.9, UCSF Chimera, VMD]

### Regulated processing and secretion of a peptide precursor in cilia. (PNAS 2022)

- DOI: 10.1073/pnas.2206098119 | PMCID: PMC9351486 | PMID: 35878031
- Evidence: By developing the tools needed to evaluate proGATI processing and secretion during mating and taking advantage of structural predictions made for proGATI using RoseTTAFold ( 33 ) and AlphaFOLD 2 ( 34 ), a role for extensive posttranslational processing and the regulated entry of proGATI and its cleavage products into mating ectosomes were identified.
- Full pipeline: quantification [ImageJ] -> stage not stated [RoseTTAFold]

### Phenol-soluble modulins PSMα3 and PSMβ2 form nanotubes that are cross-α amyloids. (PNAS 2022)

- DOI: 10.1073/pnas.2121586119 | PMCID: PMC9171771 | PMID: 35533283
- Evidence: Notably, the computational algorithm RoseTTAFold ( 59 ) predicted a structural model from the sequence of PSMβ2 that closely resembled that observed for the individual subunits in the atomic model of the PSMβ2 nanotube ( SI Appendix , Fig.
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [EMAN2, RoseTTAFold, UCSF Chimera]

### Conformational snapshots of the bacitracin sensing and resistance transporter BceAB. (PNAS 2022)

- DOI: 10.1073/pnas.2123268119 | PMCID: PMC9169098 | PMID: 35349335
- Evidence: To facilitate model building and refinement of the extracellular loop region of BceB (residues 325 to 513), we utilized the RoseTTAFold ( 33 ) algorithm available through the Robetta web server.
- Full pipeline: structure determination [RELION v3.0, RoseTTAFold]

### Researchers turn to deep learning to decode protein structures. (PNAS 2022)

- DOI: 10.1073/pnas.2202107119 | PMCID: PMC8916015 | PMID: 35235461
- Evidence: That same July, a group at the University of Washington in Seattle unveiled RoseTTAFold, a program that uses neural networks to predict protein structures based on scant genomic information ( 3 ).
- Full pipeline: machine learning [RoseTTAFold] -> stage not stated [AlphaFold]

### Ultrafast end-to-end protein structure prediction enables high-throughput exploration of uncharacterized proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2113348119 | PMCID: PMC8795500 | PMID: 35074909
- Evidence: More recently, RoseTTAFold ( 31 ) and AlphaFold2 ( 26 ) employed direct embeddings of an input MSA to directly output atomic coordinates for a protein structure, with the latter producing models of unprecedented accuracy in many cases.
- Full pipeline: stage not stated [AlphaFold, HMMER, PyTorch, RoseTTAFold]

### In silico evolution of autoinhibitory domains for a PD-L1 antagonist using deep learning models. (PNAS 2023)

- DOI: 10.1073/pnas.2307371120 | PMCID: PMC10710080 | PMID: 38032933
- Evidence: Previous studies have demonstrated that structure prediction models such as AF2 or RoseTTAFold can accurately predict the structure of small de novo proteins without an MSA ( 15 ).
- Full pipeline: stage not stated [AlphaFold, PyMOL, Python v3.8, RoseTTAFold]

### Systematic identification of conditionally folded intrinsically disordered regions by AlphaFold2. (PNAS 2023)

- DOI: 10.1073/pnas.2304302120 | PMCID: PMC10622901 | PMID: 37878721
- Evidence: Two deep learning-based methods, AlphaFold2 ( 3 ) and RoseTTAFold ( 4 ), have recently enabled protein structure prediction with high accuracy ( 5 ).
- Full pipeline: machine learning [AlphaFold, RoseTTAFold] -> stage not stated [Jupyter]

### Sequence-independent activity of a predicted long disordered segment of the human papillomavirus type 16 L2 capsid protein during virus entry. (PNAS 2023)

- DOI: 10.1073/pnas.2307721120 | PMCID: PMC10589650 | PMID: 37819982
- Evidence: Structures of the L2 protein were predicted using AF2 or RoseTTAFold, and structure of the L2 peptide/retromer/SNX3 complex was predicted with AlphaFold Multimer.
- Full pipeline: quantification [ImageJ] -> stage not stated [AlphaFold, RoseTTAFold]

### <i>Iditarod</i>, a <i>Drosophila</i> homolog of the Irisin precursor <i>FNDC5</i>, is critical for exercise performance and cardiac autophagy. (PNAS 2023)

- DOI: 10.1073/pnas.2220556120 | PMCID: PMC10523451 | PMID: 37722048
- Evidence: Structural Prediction and Analyses using AlphaFold and RoseTTAFold.
- Full pipeline: alignment/mapping [Clustal Omega] -> visualisation [PyMOL] -> stage not stated [AlphaFold, RoseTTAFold]

### The transformative power of transformers in protein structure prediction. (PNAS 2023)

- DOI: 10.1073/pnas.2303499120 | PMCID: PMC10410766 | PMID: 37523536
- Evidence: We obtained the sequences of these target proteins from the CASP15 website and predicted their structures using publicly-available versions of AlphaFold2, RoseTTAFold, OmegaFold, and ESMFold ( SI Appendix ) and subsequently evaluated the predictive modeling performance using standard evaluation metrics including GDT-TS ( 9 ), TM-score ( 11 ), lDDT ( 12 ), MolProbity ( 14 ), and GDC-SC ( 15 ) ( SI ...
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold]

### Conformational switching and flexibility in cobalamin-dependent methionine synthase studied by small-angle X-ray scattering and cryoelectron microscopy. (PNAS 2023)

- DOI: 10.1073/pnas.2302531120 | PMCID: PMC10293825 | PMID: 37339208
- Evidence: As structure prediction continues to improve with the advent of AlphaFold2 ( 35 ) and RoseTTAFold ( 42 ), our avenues for structural interpretation and validation continue to expand.
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold]

### An end-to-end deep learning method for protein side-chain packing and inverse folding. (PNAS 2023)

- DOI: 10.1073/pnas.2216438120 | PMCID: PMC10266014 | PMID: 37253017
- Evidence: AlphaFold2 ( 30 ) and RosettaFold ( 31 ) are able to produce highly accurate structures from primary sequence and MSA information along with optional template structures.
- Full pipeline: stage not stated [AlphaFold, ColabFold, RoseTTAFold]

### Structure of WNT inhibitor adenomatosis polyposis coli down-regulated 1 (APCDD1), a cell-surface lipid-binding protein. (PNAS 2023)

- DOI: 10.1073/pnas.2217096120 | PMCID: PMC10193966 | PMID: 37155902
- Evidence: RoseTTAFold ( 28 ) was used to predict models of APCDD1, ABD1, and ABD2.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX] -> stage not stated [AlphaFold, CCP4, PyMOL, RoseTTAFold]

### The cell envelope of <i>Thermotogae</i> suggests a mechanism for outer membrane biogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2303275120 | PMCID: PMC10160955 | PMID: 37094164
- Evidence: Protein localization was predicted using pSORTb ( 64 ), β-barrel prediction was done using BOMP and PRED-TMBB2 ( 65 , 66 ), and tertiary structures were predicted using RoseTTAFold ( 67 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> stage not stated [AlphaFold, ChimeraX, HMMER, IQ-TREE v2.1.4, ImageJ, RoseTTAFold]

### Exploiting conformational dynamics to modulate the function of designed proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2303149120 | PMCID: PMC10161014 | PMID: 37094170
- Evidence: Like the success of AlphaFold2 ( 4 ) and RoseTTAFold ( 5 ) that was based on training with a large set of structures, robust design strategies that include low energy states on an energy landscape must await the development of training sets that correlate how an amino acid sequence is able to access a set of conformers rather than only a single one.
- Full pipeline: machine learning [AlphaFold, RoseTTAFold] -> stage not stated [PyMOL]

### De novo design of small beta barrel proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2207974120 | PMCID: PMC10089152 | PMID: 36897987
- Evidence: Rosetta energy landscape calculations were run for these designs and then in the last step, we filtered the designs using: ff_metric ≤ 20, RoseTTAFold predicted lDDT ≥ 0.8, and the SD of rmsds to the design after sampling refinement trajectories with FastRelax < 0.1.
- Full pipeline: simulation/modelling [RoseTTAFold] -> structure determination [RoseTTAFold] -> machine learning [AlphaFold]

### Design, synthesis, and characterization of protein origami based on self-assembly of a brick and staple artificial protein pair. (PNAS 2023)

- DOI: 10.1073/pnas.2218428120 | PMCID: PMC10089216 | PMID: 36893280
- Evidence: Further increase of structural and functional complexity of the brick itself, within the supramolecular complexes, could be designed with the recent advent of AlphaFold2 ( 54 ), RoseTTAFold ( 55 ), and Protein MPNN ( 56 ) computational platforms.
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> structure determination [IMOD, MotionCor2] -> stage not stated [AlphaFold, RoseTTAFold]

### Peptide-binding specificity prediction using fine-tuned protein structure prediction networks. (PNAS 2023)

- DOI: 10.1073/pnas.2216697120 | PMCID: PMC9992841 | PMID: 36802421
- Evidence: AlphaFold ( 9 ) and RoseTTAFold ( 10 ) predict highly accurate structures ( 11 ) and structure quality confidence metrics that have been used to distinguish pairs of proteins which bind from those that don’t with some success ( 12 , 13 ).
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AlphaFold, Python, RoseTTAFold]

### AlphaFold-Multimer accurately captures interactions and dynamics of intrinsically disordered protein regions. (PNAS 2024)

- DOI: 10.1073/pnas.2406407121 | PMCID: PMC11536093 | PMID: 39446390
- Evidence: Sophisticated protein structure prediction models such as AlphaFold2 ( 21 ) and RosettaFold ( 22 ) demonstrate a remarkable capability to predict protein structures with an accuracy approaching that of experimental methods ( 23 ).
- Full pipeline: machine learning [AlphaFold] -> visualisation [PyMOL] -> stage not stated [ColabFold, Matplotlib, NumPy, RoseTTAFold, SciPy, seaborn]

### Predicting protein conformational motions using energetic frustration analysis and AlphaFold2. (PNAS 2024)

- DOI: 10.1073/pnas.2410662121 | PMCID: PMC11363347 | PMID: 39163334
- Evidence: The successes of AlphaFold2 (AF2) ( 9 ) and RoseTTAFold ( 10 ) in directly generating structure from sequence were made possible by harnessing the evolutionary data.
- Full pipeline: dimensionality reduction/clustering [PyMOL] -> visualisation [PyMOL] -> stage not stated [AlphaFold, ColabFold, RoseTTAFold]

### AlphaFold two years on: Validation and impact. (PNAS 2024)

- DOI: 10.1073/pnas.2315002121 | PMCID: PMC11348012 | PMID: 39133843
- Evidence: One of the first examples was work by Humphreys et al., which used a combination of RoseTTAFold ( 56 ) and AlphaFold to screen 8.3 million protein pairs from Saccharomyces cerevisiae ( 54 ).
- Full pipeline: stage not stated [AlphaFold, CCP4, ChimeraX, ColabFold, PHENIX, RoseTTAFold]

### Unraveling dynamic protein structures by two-dimensional infrared spectra with a pretrained machine learning model. (PNAS 2024)

- DOI: 10.1073/pnas.2409257121 | PMCID: PMC11228460 | PMID: 38917009
- Evidence: Tools like AlphaFold2 ( 4 , 5 ) and RoseTTAFold ( 6 ) can predict the three-dimensional structures of proteins from their amino acid sequences, while the integration of message passing neural network (MPNN) supplements the predictive capability of protein assemblies ( 8 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold, RoseTTAFold] -> simulation/modelling [GROMACS] -> machine learning [AlphaFold, RoseTTAFold]

### Machine learning in biological physics: From biomolecular prediction to design. (PNAS 2024)

- DOI: 10.1073/pnas.2311807121 | PMCID: PMC11228481 | PMID: 38913893
- Evidence: The problem has recently reached a milestone in predictive accuracy with the introduction of AlphaFold2 ( 3 ) and RoseTTAFold ( 59 , 60 ) which owe much of their improvement to transformer-based architectures ( Fig.
- Full pipeline: stage not stated [AlphaFold, ColabFold, RoseTTAFold]

### Democratizing protein language models with parameter-efficient fine-tuning. (PNAS 2024)

- DOI: 10.1073/pnas.2405840121 | PMCID: PMC11214071 | PMID: 38900798
- Evidence: In 2020, AlphaFold2 ( 27 ), closely followed by RoseTTAFold in 2021 ( 28 ), presented a massive jump in performance, reaching near-experimental levels of accuracy.
- Full pipeline: stage not stated [AlphaFold, PyTorch v2.0.1, RoseTTAFold, scikit-learn v1.2.0]

### ZEPPI: Proteome-scale sequence-based evaluation of protein-protein interaction models. (PNAS 2024)

- DOI: 10.1073/pnas.2400260121 | PMCID: PMC11127014 | PMID: 38743624
- Evidence: Recently, RoseTTAFold/AlphaFold was used to screen 4.3 million potential yeast PPIs among proteins comprising 65% of the proteome with paired alignments containing >200 sequences and protein pairs with <1,500 amino acids ( 18 ).
- Full pipeline: alignment/mapping [RoseTTAFold] -> stage not stated [AlphaFold, STRING db]

### Rapid and automated design of two-component protein nanomaterials using ProteinMPNN. (PNAS 2024)

- DOI: 10.1073/pnas.2314646121 | PMCID: PMC10990136 | PMID: 38502697
- Evidence: Deep learning structure prediction methods such as trRosetta ( 1 ), RoseTTAFold ( 2 ), AlphaFold2 ( 3 ), and ESMfold ( 4 ) quickly and accurately generate models of proteins and protein complexes from amino acid sequences.
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> machine learning [AlphaFold, RoseTTAFold]

### A billion years of evolution manifest in nanosecond protein dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2318743121 | PMCID: PMC10927572 | PMID: 38412135
- Evidence: The chosen sequences (refer to SI Appendix , Table S1 ) were initially controlled for by predicting their structure using AlphaFold and RosettaFold and aligning them with experimental structures from H. sapiens and M. musculus .
- Full pipeline: alignment/mapping [AlphaFold, Clustal Omega, RoseTTAFold] -> stage not stated [ColabFold]

### Fine-tuning activation specificity of G-protein-coupled receptors via automated path searching. (PNAS 2024)

- DOI: 10.1073/pnas.2317893121 | PMCID: PMC10895267 | PMID: 38346183
- Evidence: Given the abundance of resolved inactive and active forms of various GPCRs ( 29 ) and the tremendous progress in structure prediction by AlphaFold2 ( 30 ) or RosettaFold ( 31 ), path methods are particularly suitable for dissecting the activation process between the two states.
- Full pipeline: quantification [AlphaFold, RoseTTAFold]

### Structural modeling reveals the allosteric switch controlling the chitin utilization program of &lt;i&gt;&lt;i&gt;Vibrio cholerae&lt;/i&gt;&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2523358122 | PMCID: PMC12704726 | PMID: 41343673
- Evidence: So, employing multiple structural modeling algorithms [e.g., AF-M ( 18 ), AF3 ( 19 ), Chai-1 ( 25 ), RosettaFold2 ( 31 ), and RosettaFold All Atom ( 32 )] and comparing between models may help reveal allosteric conformations in other protein complexes.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, ColabFold, RoseTTAFold]

### Inhibition of ice recrystallization with designed twistless helical repeat proteins. (PNAS 2025)

- DOI: 10.1073/pnas.2514871122 | PMCID: PMC12685108 | PMID: 41289379
- Evidence: Subsequently, structures were predicted from the designed sequences using both AlphaFold2 ( 25 ) and RoseTTAFold ( 26 ).
- Full pipeline: alignment/mapping [PyMOL] -> normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [AlphaFold, ImageJ, RoseTTAFold]

### Modeling protein-small molecule conformational ensembles with PLACER. (PNAS 2025)

- DOI: 10.1073/pnas.2427161122 | PMCID: PMC12625923 | PMID: 41187076
- Evidence: AlphaFold2 (AF2) ( 9 ) and RoseTTAFold (RF) ( 10 ) enabled atomically accurate structure prediction of proteins and protein–protein complexes using sequences and structures of evolutionary-related proteins as inputs.
- Full pipeline: stage not stated [AlphaFold, Open Babel, RoseTTAFold]

### From sequence to scaffold: Computational design of protein nanoparticle vaccines from AlphaFold2-predicted building blocks. (PNAS 2025)

- DOI: 10.1073/pnas.2409566122 | PMCID: PMC12626006 | PMID: 41183183
- Evidence: Design methods like RFdiffusion for backbone generation and ProteinMPNN for amino acid sequence design have dramatically increased the success rate of many de novo design challenges, aided by the use of structure prediction methods such as AlphaFold2 (AF2) and RoseTTAFold as filters for high-quality designed proteins ( 44 – 46 ).
- Full pipeline: structure determination [PHENIX] -> stage not stated [AlphaFold, RoseTTAFold]

### Generative AI for computational chemistry: A roadmap to predicting emergent phenomena. (PNAS 2025)

- DOI: 10.1073/pnas.2415655121 | PMCID: PMC12541333 | PMID: 41052337
- Evidence: The success of AI-driven approaches like AF2 and RoseTTAFold, which can now predict crystal-like protein structures, is largely due to the availability of such high-quality experimental data deposited in the Protein Data Bank (PDB) ( 77 , 78 ).
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold]

### Parametrically guided design of beta barrels and transmembrane nanopores using deep learning. (PNAS 2025)

- DOI: 10.1073/pnas.2425459122 | PMCID: PMC12478100 | PMID: 40953261
- Evidence: We first explored the ability of RFjoint2, an improved version of RoseTTAFold-based RFjoint inpainting ( SI Appendix, Fig.
- Full pipeline: normalisation [CCP4] -> structure determination [PHENIX] -> stage not stated [AlphaFold, RoseTTAFold]

### Structure of the &lt;i&gt;Thomasclavelia ramosa&lt;/i&gt; immunoglobulin A protease reveals a modular and minimizable architecture distinct from other immunoglobulin A proteases. (PNAS 2025)

- DOI: 10.1073/pnas.2503549122 | PMCID: PMC12415215 | PMID: 40854123
- Evidence: These sheets are therefore hypothesized to come together as a single structural unit, and 2) despite the AlphaFold2 PAE metric ( 44 ) and PISA analysis ( 47 ) suggesting that the MD and CTD1 form a domain together, the AlphaFold2 model suggests that the interface is relatively hydrophilic while RosettaFold predicts CTD1 as its own separate domain ( SI Appendix , Fig.
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold]

### In silico evolution of globular protein folds from random sequences. (PNAS 2025)

- DOI: 10.1073/pnas.2509015122 | PMCID: PMC12260532 | PMID: 40587803
- Evidence: The development of machine learning-based tools for fast and robust protein structure prediction including AlphaFold, RoseTTAFold, and ESMfold has changed this situation ( 19 – 22 ).
- Full pipeline: simulation/modelling [ChimeraX, VMD] -> visualisation [ChimeraX, VMD] -> stage not stated [AlphaFold, ColabFold v1.5.5, RoseTTAFold]

### The GRAS protein RAM1 interacts with WRI transcription factors to regulate plant genes required for arbuscule development and function. (PNAS 2025)

- DOI: 10.1073/pnas.2427021122 | PMCID: PMC12130850 | PMID: 40388617
- Evidence: The top-ranked RosettaFold model, representing the predicted structure with the highest confidence, was used for further analysis.
- Full pipeline: stage not stated [RoseTTAFold]

### Structural assembly of the PAS domain drives the catalytic activation of metazoan PASK. (PNAS 2025)

- DOI: 10.1073/pnas.2409685122 | PMCID: PMC11962487 | PMID: 40106358
- Evidence: PAS-B and PAS-C domains were modeled using RosettaFold and ESMFold ( 43 , 44 ).
- Full pipeline: alignment/mapping [HMMER, MAFFT] -> stage not stated [AlphaFold, ChimeraX v1.7, ColabFold, RoseTTAFold]

### AI protocol for retrieving protein dynamic structures from two-dimensional infrared spectra. (PNAS 2025)

- DOI: 10.1073/pnas.2424078122 | PMCID: PMC11848431 | PMID: 39951500
- Evidence: Advances in AI have revolutionized the prediction of a protein’s fully folded three-dimensional structure from its primary amino acid sequence, with models like AlphaFold and RoseTTAFold significantly enhancing our understanding of static protein structures ( 8 – 14 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold, RoseTTAFold]

### tRNA selectivity during ribosome-associated quality control regulates the critical sterility-inducing temperature in two-line hybrid rice. (PNAS 2025)

- DOI: 10.1073/pnas.2417526122 | PMCID: PMC11831146 | PMID: 39913205
- Evidence: The sequences of OsRqc2 and OsRqc2 T552I were predicted using RoseTTAFold at https://robetta.bakerlab.org/ ( 44 ).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.2.9, Clustal Omega] -> structure determination [Cutadapt v1.18] -> stage not stated [ImageJ, RoseTTAFold]

### ProteomeLM: A proteome-scale language model enables accurate and rapid prediction of protein-protein interactions and gene essentiality across taxa. (PNAS 2026)

- DOI: 10.1073/pnas.2524201123 | PMCID: PMC13214046 | PMID: 42160340
- Evidence: Second, heavier structure-based methods like AlphaFold-Multimer ( 36 ) or RoseTTAFold-PPI ( 72 ) are used to further analyze these candidate pairs, through computationally intensive structural modeling.
- Full pipeline: stage not stated [AlphaFold, RoseTTAFold, STRING db]

### Predictions from deep learning propose substantial protein-carbohydrate interplay. (PNAS 2026)

- DOI: 10.1073/pnas.2523342123 | PMCID: PMC13213957 | PMID: 42150072
- Evidence: Another step would a high throughput computational docking of those carbohydrate species to the identified proteins, using CAPSIF2 or PesTo-Carbs ( 15 ) or DeepGlycanSite ( 16 ) to identify an initial hypothesis to feed GlycanDock ( 44 ), or directly de novo with programs like DiffDock ( 11 ), RosettaFold-All Atom (RF-AA) ( 45 ), AlphaFold3 ( 9 ), or Boltz-1 ( 34 ) as explored in Canner et al.
- Full pipeline: differential/statistical testing [RoseTTAFold] -> stage not stated [AlphaFold]

### Deep learning-enabled scaffolding of spatial arrays of PfCSP epitopes. (PNAS 2026)

- DOI: 10.1073/pnas.2521914123 | PMCID: PMC13079917 | PMID: 41945436
- Evidence: Methods De Novo Design of Single-NPNV Scaffolds with RoseTTAFold Hallucination.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [ChimeraX v1.7, RoseTTAFold]

### Accurate prediction of protein structures and interactions using a three-track neural network. (Science 2021)

- DOI: 10.1126/science.abj8754 | PMCID: PMC7612213 | PMID: 34282049
- Evidence: We refer to these networks, which also generate per residue accuracy predictions, as RoseTTAFold.
- Full pipeline: machine learning [AlphaFold] -> stage not stated [RoseTTAFold]

### Hallucinating symmetric protein assemblies. (Science 2022)

- DOI: 10.1126/science.add1964 | PMCID: PMC9724707 | PMID: 36108048
- Evidence: In addition, we independently evaluated the sequences using an updated version of RoseTTAFold (RF2) ( 33 ), and found that RF2 did not confidently predict the structure of most of the original AF2 hallucinated sequences, but successfully predicted almost all ProteinMPNN sequences ( Fig.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, RoseTTAFold]

### Deploying synthetic coevolution and machine learning to engineer protein-protein interactions. (Science 2023)

- DOI: 10.1126/science.adh1720 | PMCID: PMC10403280 | PMID: 37499032
- Evidence: Although AlphaFold and RoseTTAFold are useful for predicting 3D protein structures from the amino acid sequence, predicting de novo protein-protein interactions remains a challenge ( 43 ).
- Full pipeline: dimensionality reduction/clustering [igraph] -> visualisation [scikit-learn v1.2.2] -> stage not stated [AlphaFold, MACS2, PyTorch, RoseTTAFold]

