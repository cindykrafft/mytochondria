# NetworkX

- **Category:** general
- **Papers in survey:** 37
- **Journals:** PNAS (19), Nature (12), Science (3), Cell (3)
- **Years:** 2021 (2), 2022 (3), 2023 (8), 2024 (8), 2025 (13), 2026 (3)
- **Versions named:** 2.0 (1), 2.6.2 (1), 2.5.1 (1), 2.6.3 (1), 2.8.3 (1), 2.1 (1)
- **Pipeline stages it appears in:** visualisation (7), dimensionality reduction/clustering (3), normalisation (1), differential/statistical testing (1)

## Papers

### Whole-body integration of gene expression and single-cell morphology. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.017 | PMCID: PMC8445025 | PMID: 34380046
- Evidence: ...regosa et al., 2012 https://scikit-learn.org vigra N/A http://ukoethe.github.io/vigra/ mahotas Coelho, 2012 https://mahotas.readthedocs.io/en/latest/ networkx Hagberg et al., 2008 https://networkx.org/ pandas McKinney, 2010 https://pandas.pydata.org/ scipy Virtanen et al., 2020 https://www.scipy.org/ numpy van der Walt et al., 2011 https://numpy.org/ snakemake Köster and Rahmann, 2012 https://snak...
- Full pipeline: dimensionality reduction/clustering [ImageJ, Python, Snakemake, UMAP, ilastik, scikit-image, scikit-learn] -> visualisation [BigStitcher] -> stage not stated [Bioconductor, NetworkX, NumPy, SciPy, tidyverse]

### Long shared haplotypes identify the southern Urals as a primary source for the 10th-century Hungarians. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.002 | PMCID: PMC12711333 | PMID: 41106360
- Evidence: We explored several key metrics using the Python package NetworkX ( 120 ): degree centrality as well as within-module degree (kW), representing connections within each predefined cluster; and between-module degree (kB), capturing connections between different clusters.
- Full pipeline: dimensionality reduction/clustering [NetworkX] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools, R]

### Contextual computation by competitive protein dimerization networks. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.036 | PMCID: PMC11973712 | PMID: 39978343
- Evidence: The networkx Python package (version 2.7.1) was used to randomly generate graphs with a desired number of edges from an Erdős–Rényi model; each graph was checked for connectedness (i.e., that there are no fully separate networks) and re-generated if necessary to achieve connectedness.
- Full pipeline: stage not stated [NetworkX, Python v3.8.13, SciPy, seaborn v0.12.2]

### The social and structural architecture of the yeast protein interactome. (Nature 2023)

- DOI: 10.1038/s41586-023-06739-5 | PMCID: PMC10700138 | PMID: 37968396
- Version used: **2.6.2**
- Evidence: Tabular data was loaded via the pandas package (1.3.1) and converted to a network via NetworkX (2.6.2).
- Full pipeline: visualisation [ChimeraX v1.4, Cytoscape, Matplotlib, NumPy v1.20.3] -> stage not stated [AlphaFold, NetworkX v2.6.2, Python]

### Uncovering new families and folds in the natural protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06622-3 | PMCID: PMC10584680 | PMID: 37704037
- Version used: **2.5.1**
- Evidence: To visualize the graph, each connected component was simplified to a set of connected communities, detected using the asynchronous label propagation algorithm, as implemented in the asyn_lpa_communities method in networkx (v.2.5.1) 42 .
- Full pipeline: quality control [scikit-learn v1.1.1] -> alignment/mapping [BLAST, MUSCLE] -> machine learning [PyTorch v1.12.0, scikit-learn v1.1.1] -> visualisation [NetworkX v2.5.1, PyMOL v2.5.0] -> stage not stated [AlphaFold, HMMER v3.3, SciPy v1.5.4]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Version used: **2.6.3**
- Evidence: A network of regulatory TFs and target genes was then constructed by linking individual regulons to create a graph (NetworkX, v.2.6.3) (Fig.
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### Descending networks transform command signals into population motor control. (Nature 2024)

- DOI: 10.1038/s41586-024-07523-9 | PMCID: PMC11186778 | PMID: 38839968
- Evidence: Next, we stored the connectome as a graph using SciPy sparse matrix 74 and NetworkX DirectedGraph 76 representations.
- Full pipeline: differential/statistical testing [NumPy, SciPy] -> stage not stated [NetworkX, SLEAP v1.3.0]

### Neural and behavioural state switching during hippocampal dentate spikes. (Nature 2024)

- DOI: 10.1038/s41586-024-07192-8 | PMCID: PMC11023929 | PMID: 38480889
- Evidence: Maximum Δmutual information values were used to construct the graphs using the NetworkX Python package ( https://networkx.org ).
- Full pipeline: dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [Python] -> machine learning [DeepLabCut] -> stage not stated [Kilosort, NetworkX]

### From genotype to phenotype with 1,086 near telomere-to-telomere yeast genomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09637-0 | PMCID: PMC12711572 | PMID: 41094142
- Evidence: A graph was then built using CDS as nodes and sequence homology as edges, using the python package NetworkX 94 .
- Full pipeline: alignment/mapping [STAR v2.7.9, minimap2 v2.24] -> variant calling [BCFtools v1.18.1] -> stage not stated [BLAST v2.12.0, BUSCO, Flye v2.9, InterProScan v4.65, Medaka, NetworkX, R, SAMtools, SnpEff v5.1, fgsea]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: Graph layouts were computed using the spring layout algorithm (networkx, 10,000 iterations) and visualized using matplotlib.
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: The graph layout was calculated using the software packages Graphviz 94 and NetworkX 95 .
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### NEURD offers automated proofreading and feature extraction for connectomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08660-5 | PMCID: PMC11981913 | PMID: 40205208
- Evidence: Graph decomposition We decompose skeletons of axonal and dendritic processes into a directed tree graph (NetworkX object in Python 22 ; we provide a step-by-step online tutorial on how to export these as SWC files).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [DeepLabCut, SLEAP, Squidpy] -> stage not stated [CaImAn, Kilosort, NetworkX, Python]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Version used: **2.0**
- Evidence: 6f was plotted using the Python package NetworkX (v.2.0).
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Evidence: The analysis was performed using Python, with key libraries including Pandas for data manipulation, Seaborn and Matplotlib for visualization, NetworkX for network analysis, and SciPy for statistical tests.
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### A brain reward circuit inhibited by next-generation weight-loss drugs in mice. (Nature 2026)

- DOI: 10.1038/s41586-026-10444-4 | PMCID: PMC13293854 | PMID: 42092139
- Evidence: Behavioural transition networks were generated using NetworkX 54 , with line colour scaled by the global maximum-normalized transition probability across all plotted groups.
- Full pipeline: normalisation [NetworkX] -> visualisation [NetworkX] -> stage not stated [ImageJ, OpenCV, SLEAP v1.3.3]

### Neural networks to learn protein sequence-function relationships from deep mutational scanning data. (PNAS 2021)

- DOI: 10.1073/pnas.2104878118 | PMCID: PMC8640744 | PMID: 34815338
- Evidence: We used NetworkX ( 57 ) v2.3 to generate all protein structure and baseline graphs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [UMAP] -> stage not stated [NetworkX, TensorFlow]

### Design principles of PI(4,5)P<sub>2</sub> clustering under protein-free conditions: Specific cation effects and calcium-potassium synergy. (PNAS 2022)

- DOI: 10.1073/pnas.2202647119 | PMCID: PMC9295730 | PMID: 35605121
- Version used: **2.1**
- Evidence: Visualization and analysis of networks were carried out using tailored Python scripts and the Python package NetworkX (version 2.1) ( 53 ).
- Full pipeline: simulation/modelling [R] -> visualisation [NetworkX v2.1, Python]

### Small-world connectivity dictates collective endothelial cell signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2118927119 | PMCID: PMC9170162 | PMID: 35482920
- Evidence: The structural network was represented as graphs using the NetworkX library in Python 2.7 ( 52 ).
- Full pipeline: stage not stated [NetworkX, Python v2.7]

### A comprehensive map of genetic relationships among diagnostic categories based on 48.6 million relative pairs from the Danish genealogy. (PNAS 2022)

- DOI: 10.1073/pnas.2118688119 | PMCID: PMC8833149 | PMID: 35131856
- Evidence: Bearing this in mind, we used the networkx module in Python ( 28 ) to explore network connectivity in our data.
- Full pipeline: stage not stated [NetworkX, Python]

### Signatures of cross-modal alignment in children's early concepts. (PNAS 2023)

- DOI: 10.1073/pnas.2309688120 | PMCID: PMC10589699 | PMID: 37819984
- Evidence: Clustering and betweenness measures were obtained using networkx in Python ( 59 ).
- Full pipeline: dimensionality reduction/clustering [NetworkX, Python] -> differential/statistical testing [scikit-learn]

### Multidisciplinary learning through collective performance favors decentralization. (PNAS 2023)

- DOI: 10.1073/pnas.2303568120 | PMCID: PMC10450670 | PMID: 37579171
- Version used: **2.8.3**
- Evidence: Data, Materials, and Software Availability The model and analysis code for this work were developed with Python 3.9.5, Numpy 1.21.6, Scipy 1.9.0, Pandas 1.4.2, NetworkX 2.8.3, Dask 2022.4.1, Statsmodels 0.13.2, Scikit-learn 1.0.2, Matplotlib 3.5.2, and Seaborn 0.11.2.
- Full pipeline: stage not stated [Dask v2022.4.1, Matplotlib v3.5.2, NetworkX v2.8.3, NumPy v1.21.6, Python v3.9.5, SciPy v1.9.0, scikit-learn v1.0.2, seaborn v0.11.2]

### Cortical activity emerges in region-specific patterns during early brain development. (PNAS 2023)

- DOI: 10.1073/pnas.2208654120 | PMCID: PMC10235933 | PMID: 37216522
- Evidence: Network properties were computed using the NetworkX package ( 62 ) for Python.
- Full pipeline: quantification [ImageJ] -> normalisation [Python] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [Matplotlib] -> stage not stated [NetworkX, NumPy, SciPy]

### Theoretical guarantees for phylogeny inference from single-cell lineage tracing. (PNAS 2023)

- DOI: 10.1073/pnas.2203352120 | PMCID: PMC10041172 | PMID: 36927151
- Evidence: The analyses utilized the NetworkX package ( 37 ).
- Full pipeline: simulation/modelling [Python] -> stage not stated [NetworkX]

### Light-regulated chloroplast morphodynamics in a single-celled dinoflagellate. (PNAS 2024)

- DOI: 10.1073/pnas.2411725121 | PMCID: PMC11588079 | PMID: 39546572
- Evidence: Three-dimensional graph analysis was performed after skeletonizing the label image ( 76 ) and generating a NetworkX graph ( 77 ).
- Full pipeline: dimensionality reduction/clustering [NetworkX] -> stage not stated [scikit-image]

### The &lt;i&gt;Drosophila&lt;/i&gt; tracheal terminal cell as a model for branching morphogenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2404462121 | PMCID: PMC11474054 | PMID: 39356666
- Evidence: Trace information was converted into a graph object and analyzed using the python NetworkX package ( 56 ).
- Full pipeline: stage not stated [NetworkX]

### A combinatorially complete epistatic fitness landscape in an enzyme active site. (PNAS 2024)

- DOI: 10.1073/pnas.2400439121 | PMCID: PMC11317637 | PMID: 39074291
- Evidence: For each active variant, networkx ( 56 ) was used to construct a directed graph from that variant to the best variant in the landscape, AIKG.
- Full pipeline: read trimming [minimap2] -> alignment/mapping [minimap2] -> stage not stated [NetworkX, Python, scikit-learn]

### Mechanism of proton-powered c-ring rotation in a mitochondrial ATP synthase. (PNAS 2024)

- DOI: 10.1073/pnas.2314199121 | PMCID: PMC10945847 | PMID: 38451940
- Evidence: When applicable, the shortest water wire for a given frame was then identified using Dijkstra’s algorithm as implemented in NetworkX ( 78 ).
- Full pipeline: simulation/modelling [GROMACS v2020.4, MDAnalysis, SciPy, scikit-learn] -> visualisation [Matplotlib, VMD] -> stage not stated [NetworkX]

### Insights into hippocampal perfusion using high-resolution, multi-modal 7T MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2310044121 | PMCID: PMC10945835 | PMID: 38446857
- Evidence: Skeleton graph XML files are parsed to define segment type (start, termination, branchpoint, or skeleton) by examining the degree of connectivity, as well as connecting edges using the NetworkX package ( 110 ).
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [Python, pingouin] -> structure determination [FreeSurfer v7.1.1] -> visualisation [Connectome Workbench] -> stage not stated [ANTs, FSL, NetworkX, NiBabel v3.2.0, SciPy]

### Computational inference of eIF4F complex function and structure in human cancers. (PNAS 2024)

- DOI: 10.1073/pnas.2313589121 | PMCID: PMC10835048 | PMID: 38266053
- Evidence: We constructed the protein–protein interaction networks using the from_pandas_edgelist() function and plotted them with the draw_networkx() and kamada_kawai_layout() functions from the Python package “networkx”.
- Full pipeline: normalisation [UMAP, scikit-learn] -> dimensionality reduction/clustering [UMAP, clusterProfiler, scikit-learn] -> differential/statistical testing [clusterProfiler] -> visualisation [NetworkX, clusterProfiler] -> stage not stated [AlphaFold, ComplexHeatmap, PyMOL, R, RSEM, STRING db, limma]

### Graph neural networks for predicting metal-ligand coordination of transition metal complexes. (PNAS 2025)

- DOI: 10.1073/pnas.2415658122 | PMCID: PMC12541316 | PMID: 41052327
- Evidence: Weisfeiler–Lehman graph hashing ( 99 , 100 ), as implemented in NetworkX ( 101 ) (2.8.4), was performed on the ligand in the metal-coordinated state (i.e., with a dummy atom present) to identify duplicate ligands, which were removed from the dataset.
- Full pipeline: machine learning [XGBoost] -> stage not stated [NetworkX, Open Babel, RDKit]

### Deciphering Ca&lt;sup&gt;&lt;b&gt;2+&lt;/b&gt;&lt;/sup&gt; permeation and valence selectivity in Ca&lt;sub&gt;V&lt;/sub&gt;1: Molecular dynamics simulations reveal the three-ion knock-on mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2424694122 | PMCID: PMC12146731 | PMID: 40440072
- Evidence: The shortest path algorithm, implemented in the Python package NetworkX, was used to find the MFEP between the two fixed points by minimizing the energy cost.
- Full pipeline: quantification [PLUMED] -> simulation/modelling [GROMACS v2021.2, MDAnalysis, PLUMED] -> structure determination [VMD] -> visualisation [PyMOL] -> stage not stated [NetworkX]

### Identifying intermolecular interactions in single-molecule localization microscopy. (PNAS 2025)

- DOI: 10.1073/pnas.2409426122 | PMCID: PMC12107154 | PMID: 40354526
- Evidence: The resulting graph was fed into NetworkX’s function max_weight_matching ( 35 ), which then returned a graph matching that maximized the sum of proximity probabilities.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> stage not stated [NetworkX, Python]

### Evolutionary rewiring of the dynamic network underpinning allosteric epistasis in NS1 of the influenza A virus. (PNAS 2025)

- DOI: 10.1073/pnas.2410813122 | PMCID: PMC11873825 | PMID: 39977319
- Evidence: The NetworkX package ( 87 ) in Python was used to perform the graph theory analysis.
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [NetworkX, OpenMM v7.6.0, Python]

### Egress thresholds and wildfire fatalities. (PNAS 2026)

- DOI: 10.1073/pnas.2535081123 | PMCID: PMC13250580 | PMID: 42224582
- Evidence: Python analyses relied on the following packages: geopandas, pandas, osmnx, networkx, numpy, matplotlib, rasterio, rasterstats, shapely, tqdm, tenacity, requests, concurrent.futures, multiprocessing, zipfile, io, logging, glob, json, csv, ast, signal, functools, and mpl_toolkits.
- Full pipeline: stage not stated [Matplotlib, NetworkX, NumPy, R v4.4.0, ggplot2, ggpubr, tidyverse]

### The connectome of an insect brain. (Science 2023)

- DOI: 10.1126/science.add9330 | PMCID: PMC7614541 | PMID: 36893230
- Evidence: Code Analyses relied on NumPy ( 125 ), SciPy ( 126 ), Pandas ( 127 ), NetworkX ( 128 ), navis ( 124 ), and pythoncatmaid ( https://pypi.org/project/python-catmaid/ ).
- Full pipeline: stage not stated [Matplotlib, NetworkX, NumPy, SciPy, seaborn]

### Rules of engagement for condensins and cohesins guide mitotic chromosome formation. (Science 2025)

- DOI: 10.1126/science.adq1709 | PMCID: PMC12118822 | PMID: 40208986
- Evidence: The radial profile was constructed in the following manner: For each conformation, the spine of each individual sister chromatid is extracted: The polymer conformation was represented as a graph (using the networkx Python package) where monomers were nodes and edges represented the bonds that connected monomers.
- Full pipeline: dimensionality reduction/clustering [SciPy] -> simulation/modelling [OpenMM] -> visualisation [Matplotlib] -> stage not stated [NetworkX]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Evidence: To investigate the association between conservation and network centrality, we computed the PageRank centrality of the TFs in the human TF-gene network using the networkx package (v2.8.6) and compared centrality estimates across conservation levels.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

