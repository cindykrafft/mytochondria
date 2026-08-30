# Open Babel

- **Category:** md
- **Papers in survey:** 6
- **Journals:** PNAS (6)
- **Years:** 2022 (1), 2023 (2), 2025 (3)
- **Pipeline stages it appears in:** machine learning (1), dimensionality reduction/clustering (1)

## Papers

### Inverse molecular design of alkoxides and phenoxides for aqueous direct air capture of CO<sub>2</sub>. (PNAS 2022)

- DOI: 10.1073/pnas.2123496119 | PMCID: PMC9231474 | PMID: 35709322
- Evidence: The SMILES string is converted to XYZ coordinate using Open Babel package ( 50 ), and sufficient stochastic conformational search is performed at the MMFF94 level to obtain the most stable conformation ( 51 ).
- Full pipeline: stage not stated [Open Babel]

### Amine-recognizing domain in diverse receptors from bacteria and archaea evolved from the universal amino acid sensor. (PNAS 2023)

- DOI: 10.1073/pnas.2305837120 | PMCID: PMC10589655 | PMID: 37819981
- Evidence: For the experiments, we downloaded ligands from the ZINC database ( 71 ) in mol2 format and prepared them for the analysis using the Open Babel toolbox ( 72 ) and custom shell script.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> differential/statistical testing [MrBayes] -> stage not stated [AlphaFold, AutoDock Vina, Open Babel, PyMOL]

### Small molecules disaggregate alpha-synuclein and prevent seeding from patient brain-derived fibrils. (PNAS 2023)

- DOI: 10.1073/pnas.2217835120 | PMCID: PMC9963379 | PMID: 36757890
- Evidence: Three-dimensional structures of CNS-11 and CNS-11g were generated using Open Babel.
- Full pipeline: dimensionality reduction/clustering [Open Babel] -> simulation/modelling [GROMACS] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, ImageJ, UCSF Chimera]

### Flexible protein-ligand docking with diffusion-based side-chain packing. (PNAS 2025)

- DOI: 10.1073/pnas.2511925122 | PMCID: PMC12772217 | PMID: 41439702
- Evidence: All training data underwent processing through OpenBabel.
- Full pipeline: machine learning [Open Babel] -> stage not stated [AlphaFold, AutoDock Vina, RDKit]

### Modeling protein-small molecule conformational ensembles with PLACER. (PNAS 2025)

- DOI: 10.1073/pnas.2427161122 | PMCID: PMC12625923 | PMID: 41187076
- Evidence: We used Open Babel ( 42 ) to first compute the small molecule FP4 fingerprints and then to calculate the Tanimoto coefficients.
- Full pipeline: stage not stated [AlphaFold, Open Babel, RoseTTAFold]

### Graph neural networks for predicting metal-ligand coordination of transition metal complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2415658122 | PMCID: PMC12541316 | PMID: 41052327
- Evidence: The cheminformatics packages Open Babel ( 102 , 103 ) (3.1.1) and RDKit ( 75 ) (2023.3.3) were used to write the SMILES string representing each ligand without the metal present.
- Full pipeline: machine learning [XGBoost] -> stage not stated [NetworkX, Open Babel, RDKit]

