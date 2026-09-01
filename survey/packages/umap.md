# UMAP

- **Category:** single-cell
- **Papers in survey:** 1111
- **Journals:** PNAS (544), Nature (453), Cell (77), Science (37)
- **Years:** 2021 (87), 2022 (130), 2023 (181), 2024 (239), 2025 (338), 2026 (136)
- **Versions named:** 0.2.7.0 (1), 3.1 (1), 0.5.1 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (1111), visualisation (282), normalisation (82), differential/statistical testing (20), quality control (17), alignment/mapping (15), variant calling (14), quantification (13), machine learning (11), simulation/modelling (10), read trimming (3), structure determination (3)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: We conducted UMAP dimension reduction on raw scRNA-seq data and observed intermixing of epithelial cells from normal colonic biopsies and immune cells from different participants, indicating the absence of batch effects ( Figure S1D ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Evidence: For two-dimensional data visualization, UMAP was performed based on the first 50 principal components of the “harmony” data reduction.
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Whole-body integration of gene expression and single-cell morphology. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.017 | PMCID: PMC8445025 | PMID: 34380046
- Evidence: ... al., 2012 https://imagej.nih.gov/ij/ Ilastik Berg et al., 2019 https://www.ilastik.org/ Python Louvain N/A https://github.com/taynaud/python-louvain UMAP McInnes et al., 2018 https://umap-learn.readthedocs.io/en/latest/ scikit-image van der Walt et al., 2014 https://scikit-image.org/ scikit-learn Pedregosa et al., 2012 https://scikit-learn.org vigra N/A http://ukoethe.github.io/vigra/ mahotas Coe...
- Full pipeline: dimensionality reduction/clustering [ImageJ, Python, Snakemake, UMAP, ilastik, scikit-image, scikit-learn] -> visualisation [BigStitcher] -> stage not stated [Bioconductor, NetworkX, NumPy, SciPy, tidyverse]

### Impaired local intrinsic immunity to SARS-CoV-2 infection in severe COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.023 | PMCID: PMC8299217 | PMID: 34352228
- Evidence: Using the Jackstraw function within Seurat, we selected the first 36 principal components that described the majority of variance within the dataset, and used these for defining a nearest neighbor graph and Uniform Manifold Approximation and Projection (UMAP) plot.
- Full pipeline: alignment/mapping [STAR, velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.0, R, Seurat v3.2.2] -> stage not stated [Bioconductor, ComplexHeatmap v2.7.3, GSEA, Kraken2, fgsea v1.16.0, ggplot2 v3.3.2, scVelo v0.3.0]

### Endogenous retroviruses promote homeostatic and inflammatory responses to the microbiota. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.020 | PMCID: PMC8381240 | PMID: 34166614
- Evidence: Uniform manifold approximation and projection (UMAP) reduction was performed on this dataset with 25 dimensions.
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [Metascape, R v4.05, STAR, Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [HOMER]

### SARS-CoV-2 mRNA vaccination induces functionally diverse antibodies to NTD, RBD, and S2. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.005 | PMCID: PMC8185186 | PMID: 34192529
- Evidence: Percent of cells expressing genes along the UMAP embedding was visualized using the schex (v1.3.0) R package.
- Full pipeline: quantification [PyMOL] -> normalisation [igraph v1.2.6] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [PyMOL] -> visualisation [PyMOL, UMAP] -> stage not stated [R v4.0.2, Seurat v3.2.2]

### Microbial exposure during early human development primes fetal immune cells. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.039 | PMCID: PMC8240556 | PMID: 34077752
- Evidence: ...owjo.com GraphPad Prism version 7 and 9 Graphpad https://www.graphpad.com/scientific-software/prism/ R 4.4 The R Foundation https://www.r-project.org UMAP ( McInnes et al., 2018 ) https://github.com/lmcinnes/umap SMuRF 1.0 CRAN https://cran.r-project.org/web/packages/smurf/index.html QIIME 1.8.0 QIIME http://qiime.org/ emperor 1.0 Biocore https://biocore.github.io/emperor/ vegan v2.5.7 CRAN https:...
- Full pipeline: alignment/mapping [pandas] -> dimensionality reduction/clustering [QIIME 2 v1.8.0, R v4.4, UMAP] -> stage not stated [ImageJ, Matplotlib v3.2.1, NumPy v1.19.4, Python v2.7.0, seaborn v0.9.0]

### A global metagenomic map of urban microbiomes and antimicrobial resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.002 | PMCID: PMC8238498 | PMID: 34043940
- Evidence: When samples from these flowcells were plotted using UMAP (see global diversity varies according to key covariates for details) the major global trends we described were recapitulated ( Figure S2 F).
- Full pipeline: read trimming [BLAST, Bowtie2 v2.3.0] -> dimensionality reduction/clustering [R, UMAP] -> structure determination [R] -> visualisation [UMAP] -> stage not stated [Jupyter, SciPy]

### Profiling SARS-CoV-2 HLA-I peptidome reveals T cell epitopes from out-of-frame ORFs. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.046 | PMCID: PMC8173604 | PMID: 34171305
- Evidence: These data were used to generate the nearest neighbor graph which was in turn used to generate a UMAP representation that was used for Leiden clustering.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Python v3.7.3, Scanpy v1.6.0]

### Integrated analysis of multimodal single-cell data. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.048 | PMCID: PMC8238499 | PMID: 34062119
- Evidence: UMAP visualizations are computed using RNA, protein, or WNN analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2, R, Seurat v3.2.0, Signac v1.0.0]

### Fab-dimerized glycan-reactive antibodies are a structural category of natural antibodies. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.042 | PMCID: PMC8135257 | PMID: 34019795
- Evidence: (F) Top panel: UMAP visualization of 23 transcriptionally unique immune cell clusters from peripheral blood.
- Full pipeline: alignment/mapping [MotionCor2] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> structure determination [ChimeraX, Coot, PHENIX] -> visualisation [ChimeraX, R, Seurat, UMAP] -> stage not stated [PyMOL, RELION, UCSF Chimera, ggplot2]

### Charting human development using a multi-endodermal organ atlas and organoid models. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.028 | PMCID: PMC8208823 | PMID: 34019796
- Evidence: Uniform manifold approximation and projection (UMAP) ( Becht et al., 2018 ) and Louvain clustering was applied to the top 10 principal components (PCs) of the esophagus and stomach epithelium, and top 20 PCs of the alginate or matrigel embedded HIO dataset to visualize and understand the cellular heterogeneity.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellPhoneDB v2.0, R v3.6.0, SCENIC, Seurat v3.1, igraph]

### Glioblastomas acquire myeloid-affiliated transcriptional programs via epigenetic immunoediting to elicit immune evasion. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.023 | PMCID: PMC8099351 | PMID: 33857425
- Evidence: Clusters were then visualized using Uniform Manifold Approximation and Projection (UMAP).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt, GATK] -> variant calling [CNVkit v0.9.6, Mutect2, freebayes v1.1.0.46] -> dimensionality reduction/clustering [ComplexHeatmap v2.4.2, DESeq2 v1.27.32, UMAP, clusterProfiler v3.15.4] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [Bismark v0.16.3, Bowtie2 v2.3.5.1, Fiji, GSEA v3.0, ImageJ, Python, Trim Galore v0.5.0, kallisto v0.44.0, limma v3.43.11]

### BET inhibition blocks inflammation-induced cardiac dysfunction and SARS-CoV-2 infection. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.026 | PMCID: PMC7962543 | PMID: 33811809
- Evidence: Visualization of the datasets was primarily carried out using nonlinear dimensionality reduction UMAP plots ( Becht et al., 2018 ).
- Full pipeline: quality control [Bioconductor, Cutadapt, RSEM, STAR, Scanpy] -> read trimming [R] -> alignment/mapping [Cutadapt, SAMtools, STAR, featureCounts v2.0.1] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> visualisation [UMAP] -> stage not stated [Enrichr, edgeR]

### Simultaneous binding of Guidance Cues NET1 and RGM blocks extracellular NEO1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.045 | PMCID: PMC8063088 | PMID: 33740419
- Evidence: Based on this a UMAP embedding was computed.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [MotionCor2] -> stage not stated [CTFFIND v4.1, Clustal Omega, ImageJ, PHENIX, PyMOL, RELION v3.1, UCSF Chimera]

### Discovery and functional interrogation of SARS-CoV-2 RNA-host protein interactions. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.012 | PMCID: PMC7951565 | PMID: 33743211
- Evidence: PCA, nearest neighbors, and UMAP calculations were performed using default settings.
- Full pipeline: read trimming [HISAT2, fastp] -> alignment/mapping [HISAT2, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cytoscape v3.8.1, DESeq2 v1.28.1, R v3.6] -> visualisation [pheatmap] -> stage not stated [ImageJ, Scanpy v1.6.0, scDblFinder v0.2.1]

### Time-resolved systems immunology reveals a late juncture linked to fatal COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.018 | PMCID: PMC7874909 | PMID: 33713619
- Evidence: (B) UMAP visualization of single cells based on protein expression profiles for innate and adaptive groupings of cells labeled by the name of the corresponding coarse-level cluster.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> variant calling [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap v2.2.0, GSEA, GSVA, R, Seurat, edgeR v3.26.8, fgsea, limma, lme4 v1.1, tidyverse]

### Maturation and persistence of the anti-SARS-CoV-2 memory B cell response. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.050 | PMCID: PMC7994111 | PMID: 33571429
- Evidence: For UMAP generation and visualization ( Figures 3 A–3C), data from all 83 samples from patients with complete panel acquisition at M0, M3 and M6 ( Table S1 ) in our dataset were individually down-sampled to 3000 cells each using the Downsample (v3.3) plugin in FlowJO.
- Full pipeline: quality control [Seurat v3.2.2] -> alignment/mapping [R v4.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP, igraph v1.2.6] -> stage not stated [Docker, ggplot2 v3.3.2]

### Spatiotemporal analysis of human intestinal development at single-cell resolution. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.016 | PMCID: PMC7864098 | PMID: 33406409
- Evidence: Cell clusters were visualized using UMAP algorithm ( McInnes et al., 2018 ) with principal components as input and n.neighbors = 30, spread = 1 and min.dist = 0.1.
- Full pipeline: quality control [FastQC] -> dimensionality reduction/clustering [UMAP, WGCNA v1.69, clusterProfiler v3.16.1, ggplot2 v3.3.2, pheatmap v1.0.12, velocyto] -> differential/statistical testing [DESeq2] -> simulation/modelling [Monocle, velocyto] -> visualisation [STRING db, UMAP, velocyto] -> stage not stated [Bioconductor, Fiji v2.0.0, Harmony v1.0, ImageJ, R, SCENIC, Scanpy, Seurat v3.1.5.9900, ggpubr v0.2.5, igraph v1.2.4.2]

### Synergism of TNF-α and IFN-γ Triggers Inflammatory Cell Death, Tissue Damage, and Mortality in SARS-CoV-2 Infection and Cytokine Shock Syndromes. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.025 | PMCID: PMC7674074 | PMID: 33278357
- Evidence: The top 15 dimensions and a resolution value of 0.5 were used for UMAP dimension reduction ( Lee et al., 2020b ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Evidence: Uniform Manifold Approximation and Projection (UMAP) ( McInnes et al., 2018 ) method was used to visualize the single cells in 2D embedding.
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: ...S1H ) 12 , 13 and maternal cell evaluation ( Figures S1F and S1J ), we present 71,752 cells shown as a uniform manifold approximation and projection (UMAP) ( Figure 1A ), on which we manually annotated fibroblast, epithelial, endothelial, and erythrocyte/leukocyte lineages ( Figure 1B ).
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Evidence: Raw sequencing data were processed following the partially published method details, explaining the different UMAP obtained in the present study.
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Evidence: For visualization, we used the originally reported Uniform Manifold Approximation and Projection (UMAP) embeddings for the whole placenta and the gastrulation datasets and the t-Distributed Stochastic Neighbor Embedding (tSNE) for the organogenesis dataset.
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### Post-gastrulation synthetic embryos generated ex utero from mouse naive ESCs. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.028 | PMCID: PMC9439721 | PMID: 35988542
- Evidence: (C) UMAP-based plots illustrating the normalized AUC assigned value of all individual cells for each lineage on natural and synthetic embryo samples.
- Full pipeline: alignment/mapping [STAR v2.4.2a] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, R, Seurat, pheatmap]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: As a summary of single-cell cell cycle states, we performed a Uniform Manifold Approximation and Projection (UMAP) dimension reduction based on the expression n=199 known cell cycle genes [obtained from Seurat ( Satija et al., 2015 ) and ( Adamson et al., 2016 )].
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### Mild respiratory COVID can cause multi-lineage neural cell and myelin dysregulation. (Cell 2022)

- DOI: 10.1016/j.cell.2022.06.008 | PMCID: PMC9189143 | PMID: 35768006
- Evidence: UMAP was conducted using the first 20 principal components, and graph-based clustering was used to identify clusters with a resolution parameter of 0.8.
- Full pipeline: dimensionality reduction/clustering [Seurat v4.1.0, UMAP, clusterProfiler] -> differential/statistical testing [Seurat v4.1.0] -> stage not stated [ImageJ, R v4.1.1]

### The genomic origins of the world's first farmers. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.008 | PMCID: PMC9166250 | PMID: 35561686
- Evidence: Uniform manifold approximation and projection In order to represent potentially complex relationships between 90 individuals (85 modern and 25 ancient samples) from Western Eurasia, we performed a Uniform Manifold Approximation and Projection (UMAP) dimension reduction on their genotypes obtained at 2035 neutral polymorphic sites (from the Neutral dataset) that did not present missing data for any...
- Full pipeline: quality control [BWA, GATK] -> alignment/mapping [BCFtools, BWA, R, SAMtools] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ANGSD, ANNOVAR, BEDTools, Picard, Snakemake, Trim Galore]

### Imprinted SARS-CoV-2-specific memory lymphocytes define hybrid immunity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.018 | PMCID: PMC8926873 | PMID: 35413241
- Evidence: High-dimensional analysis of cytometry data AIM-positive (CD154 + CD69 + ) cells from all data files were concatenated with keywords and subjected to Phenograph clustering algorithm using k =40 nearest neighbors ( Levine et al., 2015 ) and UMAP dimensionality reduction plugins using parameters IL-2, IFN-γ, IL-10, IL-4, IL-21, CD127, CD25, and CXCR5 in FlowJo 10 (Becton Dickinson).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Mapping transcriptomic vector fields of single cells. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.045 | PMCID: PMC9332140 | PMID: 35108499
- Evidence: Because the RNA velocity from cscRNA-seq data is relative and scaled by the splicing rate constant β for each gene, we explore whether the velocity directionality would be affected by this scaling with relative RNA velocity, especially in the UMAP space.
- Full pipeline: quantification [scVelo, scikit-learn] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [SciPy]

### Non-cell-autonomous disruption of nuclear architecture as a potential cause of COVID-19-induced anosmia. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.024 | PMCID: PMC8808699 | PMID: 35180380
- Evidence: Then PCA analysis was performed to reduce dimensionality and the first 30 principal components were used UMAP plots.
- Full pipeline: alignment/mapping [BWA v0.7.17, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, GSEA, ImageJ, R v4.0.5, SAMtools, Seurat, ggplot2, pheatmap]

### Multiple early factors anticipate post-acute COVID-19 sequelae. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.014 | PMCID: PMC8786632 | PMID: 35216672
- Version used: **0.5.1**
- Evidence: ...ge) Wolock et al., 2019 https://github.com/AllonKleinLab/scrublet Scanpy v1.6.0 (Python package) Wolf et al., 2018 https://github.com/theislab/scanpy UMAP v0.5.1 (Python package) McInnes et al., 2020 https://github.com/lmcinnes/umap Leiden v0.8.0 (Python package) Traag et al., 2019 https://github.com/vtraag/leidenalg bbKNN v1.3.12 (Python package) Polański et al., 2020 https://github.com/Teichlab/...
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.6.0, UMAP v0.5.1, scDblFinder v0.2.1] -> differential/statistical testing [SciPy, XGBoost] -> stage not stated [BLAST v2.12.0, GSVA, Pilon, R, scikit-learn v0.24.2]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...trieved 17/07/2020 TrimGalore Krueger v0.6.2 https://github.com/FelixKrueger/TrimGalore ttest2 MATLAB https://uk.mathworks.com/help/stats/ttest2.heml UMAP McInnes, Healy, Melville arXiv:1802.03426v2 Velocyto ( La Manno et al., 2018 ) http://velocyto.org/ Vireo ( Huang et al., 2019 ) v0.4.0 https://huangyh09.github.io/vireo-manual/about.html WGCNA ( Langfelder and Horvath, 2008 ) https://horvath.ge...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Spatial proteogenomics reveals distinct and evolutionarily conserved hepatic macrophage niches. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.018 | PMCID: PMC8809252 | PMID: 35021063
- Evidence: The Seurat pipeline was followed to find the clusters and create the UMAP plots.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr, ImageJ, PyTorch, QuPath, R, Scanpy, Seurat, ggplot2, ilastik, pheatmap, tidyverse]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: UMAP was computed with the first 15 PCs.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### Early cellular mechanisms of type I interferon-driven susceptibility to tuberculosis. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.002 | PMCID: PMC10757650 | PMID: 38029747
- Evidence: The data was then scaled and analyzed by PCA with 30 principal components followed by UMAP analysis with 30 dimensions.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR, Trimmomatic v0.36] -> normalisation [Seurat v4.1.1, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [ImageJ, R]

### Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.024 | PMCID: PMC10841658 | PMID: 37875108
- Evidence: We visualized clusters by uniform manifold approximation and projection (UMAP).
- Full pipeline: quality control [STAR v2.6.1d] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, GATK, STAR v2.6.1d] -> variant calling [GATK] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cutadapt, DESeq2] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, SnpEff, fgsea]

### Serotonin reduction in post-acute sequelae of viral infection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.013 | PMCID: PMC11227373 | PMID: 37848036
- Evidence: For symptom clustering analysis, questionnaire data from 1,540 individuals was used, UMAP coordinates were calculated, and average symptom levels per cluster were determined.
- Full pipeline: read trimming [edgeR] -> quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.1, limma] -> stage not stated [Bioconductor v3.8, GSEA, ImageJ v2.1.0, Seurat, kallisto v0.46.0]

### Influence of autozygosity on common disease risk across the phenotypic spectrum. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.028 | PMCID: PMC10580289 | PMID: 37757828
- Evidence: We calculated UMAP coordinates using the umap R package.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [PLINK v1.9, R v4.0]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Evidence: Bottom left: single-cell uniform manifold approximation and projection (UMAP) projection based on normalized CT counts.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: 114 The UMAP was calculated based on a PCA on log-normalized counts (normalization by total counts).
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Evidence: In this case, we decided to use the first 15 PCs for the following steps, including identify neighbors (Seurat::FindNeighbors), made UMAP projection (Seurat::RunUMAP).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### The proteomic landscape of genome-wide genetic perturbations. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.026 | PMCID: PMC7615649 | PMID: 37080200
- Evidence: UMAP visualization The R implementation of the Uniform Manifold Approximation and Projection (UMAP) algorithm 77 , 125 , 126 was used to reduce protein and KO correlation matrices down to two dimensions.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler, limma] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [Bioconductor, ComplexHeatmap, R, WGCNA]

### Pyramidal neurons form active, transient, multilayered circuits perturbed by autism-associated mutations at the inception of neocortex. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.025 | PMCID: PMC10156177 | PMID: 37071993
- Evidence: Community detection was performed by applying a weighted kernel density smoothing to a UMAP embedding (60-nearest-neighbor graph, top 400 overdispersed genes) 71 where the weights are the tdTomato transcript count in each cell and the kernel bandwidth is half of the bandwidth determined by Scott’s rule.
- Full pipeline: alignment/mapping [Python v3.7.7] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scDblFinder v0.2.1] -> stage not stated [Snakemake v5.19.3]

### The T-cell-directed vaccine BNT162b4 encoding conserved non-spike antigens protects animals from severe SARS-CoV-2 infection. (Cell 2023)

- DOI: 10.1016/j.cell.2023.04.007 | PMCID: PMC10099181 | PMID: 37164012
- Evidence: (E) UMAP representation of single-cell transcriptomes from sorted T cells, colored by either cluster assignment (top) or experimental group (bottom).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Python v3.9.15, Scanpy]

### Human IRF1 governs macrophagic IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.038 | PMCID: PMC9907019 | PMID: 36736301
- Evidence: A final UMAP 208 clustering identified 14 different cells, including 11 T cells and 2 B cells; myeloid cells were excluded from further analyses because of the small numbers of these cells in the patient samples, probably due to the poor survival of these cells during sample freezing and shipping.
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq, STAR v2.7.3a] -> quantification [HTSeq] -> normalisation [edgeR v3.26.8] -> dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER v4.11, scDblFinder]

### Lymphatic vessels in bone support regeneration after injury. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.031 | PMCID: PMC11913777 | PMID: 36669473
- Evidence: Cell clustering was visualized using uniform manifold approximation and projection for dimension reduction (UMAP).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP]

### Molecular and spatial signatures of mouse brain aging at single-cell resolution. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.010 | PMCID: PMC10024607 | PMID: 36580914
- Evidence: This batch corrected nearest neighbor graph was subsequently used to further reduce the dimensionality of the dataset via UMAP or to compute integrated clusters via Leiden clustering.
- Full pipeline: quantification [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [AnnData, Cellpose, Python, Scanpy, scDblFinder, scikit-learn]

### mTOR activity paces human blastocyst stage developmental progression. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.048 | PMCID: PMC7617234 | PMID: 39332412
- Evidence: Dimensionality reduction was performed on the top 2000 most variable genes, and canonical correlation analysis (CCA) was used for scaling and alignment of the datasets, followed by projection onto two-dimensional space using Uniform Manifold Approximation and Projection (UMAP) on the top 15 CCA dimensions.
- Full pipeline: alignment/mapping [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, R, UMAP, clusterProfiler, tidyverse] -> stage not stated [CellProfiler, Seurat, ggplot2, ggpubr, scDblFinder v1.16.0]

### Thyroid hormone remodels cortex to coordinate body-wide metabolism and exploration. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.041 | PMCID: PMC11455614 | PMID: 39178853
- Evidence: After applying ScaleData() to set the mean expression of each variable gene to 0 and variance across cells to 1, we performed preliminary principal component analysis (PCA; k=25) and Uniform Manifold Approximation and Projection (UMAP) dimensionality reduction.
- Full pipeline: read trimming [Seurat] -> alignment/mapping [Seurat] -> quantification [ImageJ] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, R v4.2.2] -> stage not stated [GSEA, PyTorch]

### Mining human microbiomes reveals an untapped source of peptide antibiotics. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.027 | PMCID: PMC12821620 | PMID: 39163860
- Evidence: Subsequently, we applied the uniform manifold approximation and projection (UMAP) technique to transform these high-dimensional data into a two-dimensional (2D) space ( Figure S2E ).
- Full pipeline: read trimming [BWA, Trim Galore] -> alignment/mapping [BLAST, BWA, SPAdes, Trim Galore] -> quantification [featureCounts] -> normalisation [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, ColabFold]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Evidence: (B) Uniform manifold approximation and projection (UMAP) representation of major cell populations from scRNA-seq glioblastoma mouse dataset (DCs, dendritic cells; ECs, endothelial cells).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### The primitive endoderm supports lineage plasticity to enable regulative development. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.051 | PMCID: PMC11290322 | PMID: 38917790
- Evidence: Shared nearest neighbour graph was computed using the first 20 principal components, followed by identifying 14 clusters with resolution 0.6 using Louvain clustering, visualised using UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, CellProfiler v4.2.5, DESeq2 v1.40.2, HOMER, ImageJ, R v4.3, SAMtools, Scanpy v1.8.2, Seurat v4.3.0, deepTools, scVelo v0.2.5]

### Therapeutic potential of co-signaling receptor modulation in hepatitis B. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.038 | PMCID: PMC11290321 | PMID: 38897196
- Evidence: In order to visualize velocity fields across all genes and all cells the function scv.pl.velocity_embedding_stream has been used, built on the UMAP previously computed.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Enrichr, R, RSEM, SAMtools, Seurat v4.0.2, edgeR, featureCounts, fgsea, ggplot2, ilastik, limma, pheatmap, scVelo, tidyverse, velocyto]

### Clonal hematopoiesis driven by mutated DNMT3A promotes inflammatory bone loss. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.003 | PMCID: PMC11246233 | PMID: 38838669
- Evidence: Subsequently, data filtering, integration, normalization and scaling were performed using the R package Seurat version 4.3.0 111 , 140 and dimensionality reduction and clustering were further done by Uniform Manifold Approximation and Projection (UMAP) analysis.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR, Snakemake] -> normalisation [R, Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [R, Seurat v4.3.0, UMAP] -> stage not stated [ANNOVAR, CellChat, GATK, Mutect2]

### FLT3L governs the development of partially overlapping hematopoietic lineages in humans and mice. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.009 | PMCID: PMC11149630 | PMID: 38701783
- Evidence: Clusters were visualized by uniform manifold approximation and projection (UMAP).
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> alignment/mapping [HISAT2 v2.2.1] -> variant calling [GATK v3.6, Picard, SAMtools] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Neurotransmitter classification from electron microscopy images at synaptic sites in Drosophila melanogaster. (Cell 2024)

- DOI: 10.1016/j.cell.2024.03.016 | PMCID: PMC11106717 | PMID: 38729112
- Evidence: (E) NBLAST UMAP plots of selected hemilineages that exhibit some degree of predicted split transmitter usage.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, ggplot2, tidyverse]

### Macromolecular condensation organizes nucleolar sub-phases to set up a pH gradient. (Cell 2024)

- DOI: 10.1016/j.cell.2024.02.029 | PMCID: PMC11938373 | PMID: 38503281
- Evidence: 103 https://www.ebi.ac.uk/Tools/msa/muscle/ ImJoy HPA-UMAP plugin Ouyang et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [BLAST, ImageJ, Python]

### Microglia maintain structural integrity during fetal brain morphogenesis. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.012 | PMCID: PMC10869139 | PMID: 38309258
- Evidence: ...0-4000.html ; RRID: SCR_020127 Rhapsody analysis pipeline BD Biosciences https://www.bdbiosciences.com t-SNE GitHub https://github.com/jkrijthe/Rtsne UMAP GitHub https://github.com/lmcinnes/umap Imaris x64 software version 10.0 Bitplane RRID: SCR_007370 Imspector Pro software Miltenyi BioTec https://www.miltenyibiotec.com Gatan DigitalMicrograph software Gatan https://www.gatan.com pClamp 10.3 sof...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Bowtie2, ImageJ, Metascape v3.5.20230501, R, Seurat v4.3.0.1, ggplot2, tidyverse]

### Coordinating brain-distributed network activities in memory resistant to extinction. (Cell 2024)

- DOI: 10.1016/j.cell.2023.12.018 | PMCID: PMC7615560 | PMID: 38242086
- Evidence: We applied Principal Component Analysis on this feature matrix and used the first seven principal components (explaining > 95% of the variance) as feature elements to Uniform Manifold Approximation and Projection (UMAP) 138 for subsequent non-linear, dimensionality reduction.
- Full pipeline: normalisation [SciPy] -> dimensionality reduction/clustering [Kilosort, UMAP] -> differential/statistical testing [NumPy, Python v3.6, seaborn] -> visualisation [Matplotlib] -> stage not stated [Astropy v2.0.2, scikit-learn v0.19.1]

### Human inherited CCR2 deficiency underlies progressive polycystic lung disease. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.036 | PMCID: PMC10842692 | PMID: 38157855
- Evidence: ...ript N/A Software and algorithms R The R Project for Statistical Computing https://www.r-project.org Uni-form Mani-fold Approximation and Projection (UMAP) Becht et al.
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, Seurat] -> quantification [ComplexHeatmap] -> normalisation [ComplexHeatmap, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [ImageJ, TrackMate] -> stage not stated [MACS2, ggplot2, scDblFinder]

### Distinct components of mRNA vaccines cooperate to instruct efficient germinal center responses. (Cell 2025)

- DOI: 10.1016/j.cell.2025.11.023 | PMCID: PMC12878702 | PMID: 41406961
- Evidence: (C) UMAP clustering of sequencing data from Figure 4 before integration.
- Full pipeline: dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [GSEA, R, fgsea] -> stage not stated [Seurat]

### A single-nucleus transcriptomic atlas of the adult Aedes aegypti mosquito. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.008 | PMCID: PMC12767863 | PMID: 41172998
- Evidence: UMAP, tSNE, Force Directed Layout (FDL) visualizations were used for visualization of data in 2D.
- Full pipeline: quality control [Matplotlib, NumPy, Python, Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [seaborn] -> visualisation [UMAP, scikit-learn] -> stage not stated [AnnData, BLAST v2.9.0, ImageJ, Jupyter, scDblFinder]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Evidence: Principal component analysis, clustering, and UMAP dimensionality reduction was performed using Seurat with default parameters and selection of 15 dimensions, based on plotting the percentage of variance explained by each principal component, and a resolution of 0.8.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Molecular and neural control of social hierarchy by a forebrain-thalamocortical circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.07.024 | PMCID: PMC12458795 | PMID: 40795854
- Evidence: To visualize nuclei according to their PC scores, we used the UMAP algorithm to place each nucleus on a two-dimensional plot; subsequently, each nucleus was colored based on cluster identity.
- Full pipeline: normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, GSEA, R, Seurat v2.3.4]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Evidence: To visualize all snATAC nuclei in a two-dimensional embedding, UMAP was created using the Scanpy (v.1.9.3) function scanpy.tl.umap with the LSI latent components corrected by Harmony.
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### Brain endothelial gap junction coupling enables rapid vasodilation propagation during neurovascular coupling. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.030 | PMCID: PMC12337775 | PMID: 40675149
- Evidence: 27 ( https://single-cell.mpi-muenster.mpg.de , UMAP seed #42) was used to analyze connexin expression in endothelial cells.
- Full pipeline: quantification [ImageJ, Python] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.2.4]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: UMAP dimensionality reduction was then applied using the runUMAP function from scater on these components.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Perturb-Multimodal: A platform for pooled genetic screens with imaging and sequencing in intact mammalian tissue. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.022 | PMCID: PMC12324982 | PMID: 40513557
- Evidence: UMAP of individual cells measured by 10X Flex from mice either with ad lib diet, overnight fasting, or 1-month high fat diet (HFD), colored by condition (left) or cell-type and subtype identity (right).
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose, XGBoost] -> stage not stated [AnnData, Scanpy]

### Serotonin transporter inhibits antitumor immunity through regulating the intratumoral serotonin axis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.032 | PMCID: PMC12255530 | PMID: 40403728
- Evidence: 127 – 132 The AddModuleScore function was used to calculate module scores of each gene signature list, while the FeaturePlot function was used to visualize the expression of each signature in the UMAP plots.
- Full pipeline: quantification [R, Seurat v4.0.0] -> dimensionality reduction/clustering [GSEA, R, Seurat v4.0.0, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2, velocyto]

### Design principles of cell-state-specific enhancers in hematopoiesis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.017 | PMCID: PMC12173716 | PMID: 40345201
- Evidence: (D) UMAP of single-cell RNA-seq data from hematopoietic differentiation cultures.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ArchR] -> machine learning [TensorFlow] -> stage not stated [R, ggplot2, kallisto, pheatmap]

### Transcriptional regulation by PHGDH drives amyloid pathology in Alzheimer's disease. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.045 | PMCID: PMC12204802 | PMID: 40273909
- Evidence: Uniform Manifold Approximation and Projection (UMAP) of the single cells was performed with the first 10 PCs.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [Bowtie2, SAMtools, fastp] -> quantification [Bowtie2, fastp] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bowtie2, fastp] -> visualisation [R] -> stage not stated [AlphaFold, HOMER v4.11, MACS2, Seurat, deepTools]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Evidence: UMAP and FindNeighbors were performed using the 2 nd through 30 th Harmony-adjusted LSI embeddings.
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### Inflammation switches the chemoattractant requirements for naive lymphocyte entry into lymph nodes. (Cell 2025)

- DOI: 10.1016/j.cell.2024.11.031 | PMCID: PMC11845304 | PMID: 39708807
- Evidence: Blood endothelial cell clusters were determined by maximal correlation with previously annotated lymph node blood endothelial cell datasets, 50 and were visualized with Uniform Manifold Approximation and Projection (UMAP).
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2 v1.4.2, Metascape] -> visualisation [UMAP] -> stage not stated [R v4.2.1, Seurat v4.3.0, deepTools v3.5.4]

### Genome instability triggers intercellular DNA transfer between human cells. (Cell 2026)

- DOI: 10.1016/j.cell.2026.04.041 | PMCID: PMC13193222 | PMID: 42161273
- Evidence: (F) UMAP embedding of single-cell transcriptomes ( n = 7,601 cells) from the isolated mCherry+ population shown in (A).
- Full pipeline: normalisation [R, Seurat] -> dimensionality reduction/clustering [UMAP]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Evidence: Feature plots show single-cell expression projected onto a precomputed Tabula Sapiens UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### Renal PIEZO2 is an essential regulator of renin. (Cell 2026)

- DOI: 10.1016/j.cell.2025.11.013 | PMCID: PMC12695021 | PMID: 41349545
- Evidence: UMAP projection of mouse kidney stroma split by sample.
- Full pipeline: quality control [SoupX v1.6.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [scDblFinder]

### Cell-type specialization is encoded by specific chromatin topologies. (Nature 2021)

- DOI: 10.1038/s41586-021-04081-2 | PMCID: PMC8612935 | PMID: 34789882
- Evidence: The scaled data were used for a PCA, followed by processing through dimensionality reduction using uniform manifold approximation and projection (UMAP) 72 for visualization purposes using the Seurat R package 71 , with default parameters.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, RSEM, STAR] -> quantification [SAMtools v1.3.1] -> normalisation [R, SAMtools v1.3.1, Seurat v3.1.4, UMAP] -> dimensionality reduction/clustering [Python, R, UMAP] -> simulation/modelling [LAMMPS] -> visualisation [Conda, Python, R, UMAP] -> stage not stated [ArchR, BEDTools, DESeq2]

### An atlas of gene regulatory elements in adult mouse cerebrum. (Nature 2021)

- DOI: 10.1038/s41586-021-03604-1 | PMCID: PMC8494637 | PMID: 34616068
- Evidence: A detailed list of regions is in Supplementary Table 1 . b , Uniform manifold approximation and projection (UMAP) 58 embedding and clustering analysis of snATAC-seq data.
- Full pipeline: quality control [R] -> alignment/mapping [R] -> dimensionality reduction/clustering [BEDTools, HOMER, UMAP, scikit-learn] -> differential/statistical testing [HOMER, Monocle v0.2.2] -> stage not stated [Enrichr, MACS2, SAIGE, Seurat v3.0, scDblFinder]

### Spatially resolved cell atlas of the mouse primary motor cortex by MERFISH. (Nature 2021)

- DOI: 10.1038/s41586-021-03705-x | PMCID: PMC8494645 | PMID: 34616063
- Evidence: For presentation, UMAP 54 was used to embed the cells in two dimensions using the same principal components that were used for clustering.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Scanpy, scDblFinder]

### A transcriptomic and epigenomic cell atlas of the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03500-8 | PMCID: PMC8494649 | PMID: 34616066
- Evidence: Dimensionality reduction by UMAP We performed PCA based on imputed gene expression matrices of 3,792 marker genes using the 10x single-nucleus dataset from the Broad Institute as the reference, and selected the top 50 principal components (93% variance explained).
- Full pipeline: alignment/mapping [Bismark, STAR v2.5.3, Seurat] -> normalisation [deepTools] -> dimensionality reduction/clustering [R, Scanpy, UMAP] -> stage not stated [BEDTools, MACS2, scDblFinder]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Evidence: Clustering and visualization To visualize the high-dimensionality dataset in 2D space, the latent dimensions for the ATAC and RNA data from scAlign were used to construct UMAP 62 graphs from Seurat.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### A multimodal cell census and atlas of the mammalian primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03950-0 | PMCID: PMC8494634 | PMID: 34616075
- Evidence: ...-subclass co-variation between distances in transcriptomic space and morphological space, as seen in similar colour ordering in a (right) and g . h , UMAP visualization of cross-species integration of snRNA-seq data for glutamatergic neurons isolated from mouse, macaque and human, with colours corresponding to cell subclass.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [DESeq2 v1.30.0, MACS2, Python v3.6, UMAP, scikit-learn v0.24.2] -> differential/statistical testing [DESeq2 v1.30.0, HOMER] -> visualisation [UMAP] -> stage not stated [R v3.5.3, Seurat, ggplot2 v3.2.1]

### Morphological diversity of single neurons in molecularly defined cell types. (Nature 2021)

- DOI: 10.1038/s41586-021-03941-1 | PMCID: PMC8494643 | PMID: 34616072
- Evidence: We applied uniform manifold approximation and projection (UMAP) dimension reduction using the Python package ‘UMAP’ 56 .
- Full pipeline: alignment/mapping [STAR v2.5.3] -> quantification [STAR v2.5.3] -> dimensionality reduction/clustering [R, UMAP, igraph]

### DNA methylation atlas of the mouse brain at single-cell resolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03182-8 | PMCID: PMC8494641 | PMID: 34616061
- Evidence: In each round of clustering analysis, the t -SNE 45 , 46 and UMAP 17 embedding were run on the PC matrix the same as the clustering input using the implementation from the scanpy 40 package.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BEDTools, Bismark] -> normalisation [deepTools] -> dimensionality reduction/clustering [BEDTools, R, UMAP, scikit-learn] -> differential/statistical testing [edgeR] -> machine learning [BEDTools, TensorFlow v2.0] -> stage not stated [Scanpy v1.4.3]

### A transcriptomic atlas of mouse cerebellar cortex comprehensively defines cell types. (Nature 2021)

- DOI: 10.1038/s41586-021-03220-z | PMCID: PMC8494635 | PMID: 34616064
- Evidence: 1b , we merged all annotated high-quality nuclei and repeated preliminary preprocessing steps before performing UMAP using 25 principal components.
- Full pipeline: quantification [Monocle] -> normalisation [Monocle, Seurat v2.3.4] -> dimensionality reduction/clustering [Seurat v2.3.4, UMAP] -> stage not stated [ImageJ]

### Human neocortical expansion involves glutamatergic neuron diversification. (Nature 2021)

- DOI: 10.1038/s41586-021-03813-8 | PMCID: PMC8494638 | PMID: 34616067
- Evidence: These PCs were then used to generate a UMAP 61 .
- Full pipeline: alignment/mapping [STAR v2.5.3] -> quantification [ImageJ] -> dimensionality reduction/clustering [Seurat, UMAP, scikit-learn] -> visualisation [scikit-learn] -> stage not stated [statsmodels]

### Isoform cell-type specificity in the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03969-3 | PMCID: PMC8494650 | PMID: 34616073
- Evidence: While UMAP applied to PCA of the data (Supplementary Fig.
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.0.3, NumPy v1.18.1, UMAP, statsmodels v0.12.1] -> stage not stated [Scanpy, SciPy, kallisto, scikit-learn]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Evidence: For cluster visualization, UMAP dimensional reduction was performed in Seurat (v3.1.0, RRID SCR_007322) using the top 75 principal components identified using Pagoda2 (RRID SCR_017094).
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Evidence: 2 Epithelial cells and FCGR2A signalling in tuft cells. a , b , Uniform manifold approximation and projection (UMAP) of fetal ( a ) and postnatal ( b ) epithelial cell types.
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Transcriptional programs of neoantigen-specific TIL in anti-PD-1-treated lung cancers. (Nature 2021)

- DOI: 10.1038/s41586-021-03752-4 | PMCID: PMC8338555 | PMID: 34290408
- Evidence: TRB amino acid sequences were used as a biological barcode to match MANA, EBV or influenza A-specific T cell clonotypes identified from the FEST assay with single-cell VDJ profile and were projected onto CD8 + T cell refined UMAP.
- Full pipeline: alignment/mapping [velocyto] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [velocyto] -> structure determination [UMAP] -> visualisation [pheatmap]

### A vaccine targeting mutant IDH1 in newly diagnosed glioma. (Nature 2021)

- DOI: 10.1038/s41586-021-03363-z | PMCID: PMC8046668 | PMID: 33762734
- Evidence: Technical unicates for CMV/AdV, dendritic cells (DCs) only, LILs only, CMV/AdV PBMCs. b , UMAP plot depicting molecular clusters defined by single-cell transcriptome of LILs ( n = 16,720 cells) from PsPD of patient ID08. c , CXCL13 expression in LILs from PsPD of patient ID08 within clusters as in b . d , Bubble plot mapping top TCR clones in CD4 + and CD8 + T cells defined by single-cell TCR sequ...
- Full pipeline: alignment/mapping [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### NASH limits anti-tumour surveillance in immunotherapy-treated HCC. (Nature 2021)

- DOI: 10.1038/s41586-021-03362-0 | PMCID: PMC8046670 | PMID: 33762733
- Evidence: For UMAP and FlowSOM plots, BD FACSymphony data (mouse and human) were exported from FlowJo (v10).
- Full pipeline: quality control [Seurat] -> alignment/mapping [velocyto v0.6] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2 v1.28.1] -> stage not stated [R v3.4, scVelo v0.2.2]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Evidence: Clustering of Superclones and Subclones Integer single-cell copy number data from multi-sample segmentation was embedded into two dimensions using UMAP 28 , 39 with R package ‘uwot’ (v.0.1.8, min dist = 0, n neighbors = 40, seed = 55 for TNBC tumors and n neighbors = 25, seed = 206 for cell-lines, distance = “manhattan”).
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### Lipid signalling enforces functional specialization of T<sub>reg</sub> cells in tumours. (Nature 2021)

- DOI: 10.1038/s41586-021-03235-6 | PMCID: PMC8168716 | PMID: 33627871
- Evidence: Data visualization To identify different clusters in TILs, data were further analyzed using Seurat and visualized by UMAP [Uniform Manifold Approximation and Projection 49 ], which partitioned cells into 22 unsupervised clusters based on their transcriptomes using resolution = 0.5 in FindClusters function.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, limma v3.34.9] -> visualisation [UMAP] -> stage not stated [GSEA, Seurat, ggplot2 v2.2.1]

### Sulfur sequestration promotes multicellularity during nutrient limitation. (Nature 2021)

- DOI: 10.1038/s41586-021-03270-3 | PMCID: PMC7969356 | PMID: 33627869
- Evidence: Samples were demultiplexed and aligned using Cell Ranger 2.2 (10X genomics) to genome build release 2-12, then processed and analysed in R using Seurat v.3 and uniform manifold approximation and projection (UMAP) as a dimensionality reduction approach.
- Full pipeline: read trimming [Seurat, UMAP, deepTools, featureCounts] -> alignment/mapping [DESeq2, R, Seurat, UMAP, deepTools, featureCounts] -> quantification [DESeq2, R, deepTools, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, R] -> visualisation [DESeq2, R]

### In situ mapping identifies distinct vascular niches for myelopoiesis. (Nature 2021)

- DOI: 10.1038/s41586-021-03201-2 | PMCID: PMC8020897 | PMID: 33568812
- Evidence: Stromal UMAP analysis To identify diverse stromal, hematopoietic, and other cell populations we reanalyzed 19 independent 10x Genomics captures from two complementary stromal bone marrow scRNA-Seq datasets ( GSE128423 27 ) and ( GSE108891 26 ).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Regulatory genomic circuitry of human disease loci by integrative epigenomics. (Nature 2021)

- DOI: 10.1038/s41586-020-03145-z | PMCID: PMC7875769 | PMID: 33536621
- Evidence: Using these Spearman correlation matrices on all observed and imputed signal tracks, we computed UMAP dimensionality reductions for each mark and assay using with the uwot R package 51 with the default parameters, except for n_neighbours = 250, min_dist = 0.25 and repulsion_strength = 0.25.
- Full pipeline: alignment/mapping [BWA] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [MACS2] -> machine learning [XGBoost] -> visualisation [R]

### Skin-resident innate lymphoid cells converge on a pathogenic effector state. (Nature 2021)

- DOI: 10.1038/s41586-021-03188-w | PMCID: PMC8336632 | PMID: 33536623
- Evidence: Initial dimensionality reduction, clustering and visualization To cluster and remove cells unlikely to be ILCs, we computed a principal components analysis on scaled variable genes, as determined above, using Seurat’s RunPCA function, and visualized it by computing a UMAP using Seurat’s RunUMAP function on the top 30 principal components.
- Full pipeline: normalisation [SciPy, Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Scanpy, UMAP] -> visualisation [UMAP] -> stage not stated [Bioconductor]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: Principal Components Analysis (PCA) was then performed for dimensionality reduction, and the top 20 components--which were chosen by inspecting the cumulative variance explained across PCs using the knee point method--were then used as features for a Uniform Manifold Approximation and Projection (UMAP) 66 visualization of the cells in two dimensions ( Figure 5A ).
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Evidence: UMAP plotting was performed using uwot version 0.1.8 using the first 20 principal components of the same genes used in WGCNA analysis after Z-scaling and centering, with a minimum distance of 0.2 61 .
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Histone H1 loss drives lymphoma by disrupting 3D chromatin architecture. (Nature 2021)

- DOI: 10.1038/s41586-020-3017-y | PMCID: PMC7855728 | PMID: 33299181
- Evidence: Centroblasts ( j ) and centrocytes ( k ) were defined based on enrichment for centroblast and centrocyte signature profiles, respectively projected onto the UMAP distribution of cells. l , Top:Expression of G2M cell cycle proliferation gene signature was plotted for each cell on the Y axis with spline curves representing the average for H1c −/− /e −/− and WT cells.
- Full pipeline: quantification [GSEA] -> normalisation [GSEA] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Defining HPV-specific B cell responses in patients with head and neck cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-2931-3 | PMCID: PMC9462833 | PMID: 33208941
- Evidence: Activated B cell populations from metLN and TIL of 3 HPV+ HNSCC patients as well as PBMCs of an Influenza vaccinee were subjected to scRNA-seq. a, Flow plot of CD19 + B cells from metLN showing activated CD71 high cells (red gate). b, UMAP plot showing 4 identified clusters with cells obtained from PBMC (Flu), metLNs, and TILs. c, Heatmap showing relative expression of the top differentially expre...
- Full pipeline: alignment/mapping [HISAT2, SAMtools, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [R, Seurat v3.1.4]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Evidence: UMAPs and Diffusion Maps Integrated full-map UMAP 50 projections ( Figure 1 , 2 , 3 , 4 , 5) were generated via the UMAP Python package ( https://github.com/lmcinnes/umap ) on the reduced corrected dimensions returned from fastMNN setting min_dist to 0.6 and the number of neighbours to square root the number of cells.
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### Identification of SARS-CoV-2 inhibitors using lung and colonic organoids. (Nature 2021)

- DOI: 10.1038/s41586-020-2901-9 | PMCID: PMC8034380 | PMID: 33116299
- Evidence: We ran the UMAP dimensional reduction using the RunUMAP function in the R Seurat 27 package with training epochs setting to 2,000.
- Full pipeline: quality control [R, edgeR] -> alignment/mapping [Bowtie2] -> quantification [R, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, edgeR] -> machine learning [UMAP] -> visualisation [Bowtie2] -> stage not stated [GSEA, Seurat v3.1.0]

### Ovarian cancer mutational processes drive site-specific immune evasion. (Nature 2022)

- DOI: 10.1038/s41586-022-05496-1 | PMCID: PMC9771812 | PMID: 36517593
- Evidence: UMAP embeddings including cohort-level and patient-level embeddings for all major cell types were based on the first 50 principal components.
- Full pipeline: quality control [R, Seurat] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [UMAP] -> machine learning [QuPath v0.2.3, StarDist] -> stage not stated [Strelka v2.8.2, scDblFinder v0.2.1]

### Primate gastrulation and early organogenesis at single-cell resolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05526-y | PMCID: PMC9771819 | PMID: 36517595
- Evidence: Subsequently, the Seurat pipeline was used for dimensionality reduction (UMAP) and unsupervised clustering.
- Full pipeline: quantification [CellPhoneDB, R, Seurat v4.0.0] -> dimensionality reduction/clustering [R, Seurat v4.0.0, UMAP, clusterProfiler, pheatmap, scVelo] -> simulation/modelling [Scanpy v1.8.2] -> visualisation [pheatmap] -> stage not stated [Docker, SCENIC, ilastik, scDblFinder]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Evidence: The first 201 principal components, which captured 50% of the variance in the dataset, were used as an input for nonlinear dimensionality reduction, performed using UMAP implemented in scikit-learn.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Effect of the intratumoral microbiota on spatial and cellular heterogeneity in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05435-0 | PMCID: PMC9684076 | PMID: 36385528
- Evidence: Sequencing reads from the 16S rRNA amplified libraries retain the 10x genomics barcode sequence which facilitated mapping of annotated bacterial reads directly to the host single cells they are associated with. b , UMAP plots showing single-cell transcriptome of HT-29 cells with (orange dots) and without (blue dots) the 1100R 16S primer in the amplification mix before single-cell cDNA generation.
- Full pipeline: alignment/mapping [GATK, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA]

### The neurons that restore walking after paralysis. (Nature 2022)

- DOI: 10.1038/s41586-022-05385-7 | PMCID: PMC9668750 | PMID: 36352232
- Evidence: A detailed description is provided in Methods , ‘Experimental conditions’. b , Uniform manifold approximation and projection (UMAP) visualization of 20,990 nuclei revealing 36 neuron subpopulations.
- Full pipeline: quality control [Seurat] -> alignment/mapping [Seurat, velocyto] -> normalisation [fgsea] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.3, fgsea] -> simulation/modelling [Python v2.7] -> visualisation [UMAP] -> stage not stated [ImageJ, Nextstrain]

### Metastatic recurrence in colorectal cancer arises from residual EMP1&lt;sup&gt;+&lt;/sup&gt; cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05402-9 | PMCID: PMC7616986 | PMID: 36352230
- Evidence: UMAP representation showed that tumor cells from primary tumors and metastases overlapped to a large extent ( Fig.
- Full pipeline: alignment/mapping [STAR v2.5.2] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1, R, limma] -> stage not stated [GSEA, ImageJ, Seurat v4.0.3, scVelo]

### Broad transcriptomic dysregulation occurs across the cerebral cortex in ASD. (Nature 2022)

- DOI: 10.1038/s41586-022-05377-7 | PMCID: PMC9668748 | PMID: 36323788
- Evidence: Utilizing 65 PCs, Harmony (as part of the Pegasus suite) was used to integrate and batch-correct libraries, Louvain clustering was performed to cluster the cells and visualize resulting clusters with UMAP 56 .
- Full pipeline: quality control [FastQC] -> variant calling [Picard] -> quantification [RSEM] -> normalisation [R, limma] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [WGCNA, lme4]

### Single-cell genomic variation induced by mutational processes in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05249-0 | PMCID: PMC9712114 | PMID: 36289342
- Evidence: Samples were clustered by first applying UMAP 61 to the normalized signature probabilities for the HRD SNV signature and all SV signatures with n_neighbors = 20 and min_dist = 0 to produce two-dimensional sample embeddings.
- Full pipeline: alignment/mapping [BWA, DeepVariant, R, WhatsHap, minimap2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [Seurat, Strelka, scDblFinder]

### Maturation and circuit integration of transplanted human cortical organoids. (Nature 2022)

- DOI: 10.1038/s41586-022-05277-w | PMCID: PMC9556304 | PMID: 36224417
- Evidence: Following low-quality nuclei removal, integrated datasets were clustered (resolution = 0.5) and embedded for visualization purposes with UMAP 34 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Fiji v2.1.0, ImageJ, R v4.1.2, Seurat v4.1.1, edgeR v3.36.0, scDblFinder]

### Nuclear-embedded mitochondrial DNA sequences in 66,083 human genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05288-7 | PMCID: PMC9630118 | PMID: 36198798
- Evidence: We performed a uniform manifold approximation and projection (UMAP) 55 based on the NUMTs which were unique to each population in rare disease genomes.
- Full pipeline: alignment/mapping [Clustal Omega, Python, SAMtools, Strelka v2.4.7, minimap2] -> variant calling [Strelka v2.4.7] -> dimensionality reduction/clustering [GCTA, UMAP] -> differential/statistical testing [R] -> machine learning [GCTA] -> visualisation [Matplotlib] -> stage not stated [BEDTools, PLINK v1.90]

### PD-1-cis IL-2R agonism yields better effectors from stem-like CD8<sup>+</sup> T cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05192-0 | PMCID: PMC9534752 | PMID: 36171284
- Evidence: In brief, RNA counts were normalized per 10,000, the top most highly variable genes were selected, total gene and mitochondrial reads were regressed out, PCA was performed and the first 50 principal components were used for nearest-neighbour calculations and Leiden clustering, as well as for UMAP-based visualization.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> quantification [featureCounts] -> normalisation [UMAP] -> dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [ComplexHeatmap, Jupyter, R, UMAP] -> stage not stated [DESeq2, MACS2, Python, Scanpy]

### LRRC15<sup>+</sup> myofibroblasts dictate the stromal setpoint to suppress tumour immunity. (Nature 2022)

- DOI: 10.1038/s41586-022-05272-1 | PMCID: PMC9630141 | PMID: 36171287
- Evidence: Cells were gated on PDPN + CD31 – cells. c , d , Quantification of the total number of PDPN + LRRC15 + cells ( c ) and PDPN + CD31 – cells ( d ) normalized by tumour weight ( n = 12 mice). e , Uniform manifold approximation and projection (UMAP) plot of 6,525 single fibroblasts coloured by cluster membership (left, n = 5 mice per group) and the relative average expression of indicated marker genes...
- Full pipeline: quantification [R, Seurat, UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [R, UMAP]

### Long-primed germinal centres with enduring affinity maturation and clonal migration. (Nature 2022)

- DOI: 10.1038/s41586-022-05216-9 | PMCID: PMC9491273 | PMID: 36131022
- Evidence: UMAP plots were generated using Seurat v.4 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [UCSF Chimera v1.13] -> visualisation [UCSF Chimera v1.13] -> stage not stated [GSEA, RELION v3.0, Seurat, fgsea]

### Brainstem ADCYAP1<sup>+</sup> neurons control multiple aspects of sickness behaviour. (Nature 2022)

- DOI: 10.1038/s41586-022-05161-7 | PMCID: PMC9492535 | PMID: 36071158
- Evidence: In this case, we took the first 25 principal components for clustering and projection with both (UMAP) and t -distributed stochastic neighbour embedding.
- Full pipeline: quality control [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor v1.0.6, Seurat v4.0]

### Novel antigen-presenting cell imparts T&lt;sub&gt;reg&lt;/sub&gt;-dependent tolerance to gut microbiota. (Nature 2022)

- DOI: 10.1038/s41586-022-05309-5 | PMCID: PMC9605865 | PMID: 36070798
- Evidence: Cell clustering was visualized using UMAP 60 , computed from the nearest neighbour graph built by PhenoGraph.
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [SAMtools v1.11, STAR v2.7.7a, featureCounts, velocyto v0.17.17] -> normalisation [Scanpy v1.6.0, Seurat v4.0.4] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> visualisation [Seurat v4.0.4, UMAP] -> stage not stated [ArchR v1.0.1, MACS2 v2.2.7.1, RepeatMasker, scVelo v0.2.4]

### Non-viral, specifically targeted CAR-T cells achieve high safety and efficacy in B-NHL. (Nature 2022)

- DOI: 10.1038/s41586-022-05140-y | PMCID: PMC9452296 | PMID: 36045296
- Evidence: Principal-component analysis (PCA) was performed on the basis of the scaled data with the top 2,000 most highly variable genes and the top ten principal components used for t -SNE construction and UMAP construction.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [GSVA, UMAP] -> differential/statistical testing [Seurat] -> stage not stated [GSEA, fastp]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: Plots were generated using Scanpy (in Python for dot plots and velocity) and Seurat (in R for UMAP plots), as well ggplot2 for the remainder of the plots (in R for bar plots and proportion scatter plots).
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### Spatial profiling of chromatin accessibility in mouse and human tissues. (Nature 2022)

- DOI: 10.1038/s41586-022-05094-1 | PMCID: PMC9452302 | PMID: 35978191
- Evidence: Data normalization and dimensionality reduction was conducted using iterative latent semantic indexing (iterations = 2, resolution = 0.2, varFeatures = 25000, dimsToUse = 1:30, n.start = 10), followed by graph clustering and UMAP embedding (nNeighbors = 30, metric = cosine, minDist = 0.5) 14 .
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [Python, Seurat] -> stage not stated [ArchR, Snakemake]

### MYB orchestrates T cell exhaustion and response to checkpoint inhibition. (Nature 2022)

- DOI: 10.1038/s41586-022-05105-1 | PMCID: PMC9452299 | PMID: 35978192
- Evidence: On the basis of the principal component analysis (PCA), a UMAP of the identified clusters was visualized.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [HTSeq v0.11.4, featureCounts, limma] -> normalisation [DESeq2 v1.26.0, limma] -> dimensionality reduction/clustering [Slingshot v1.4.0, UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> simulation/modelling [Slingshot v1.4.0] -> visualisation [UMAP] -> stage not stated [Fiji, GSEA, ImageJ, R, Seurat, scVelo]

### Spatially resolved clonal copy number alterations in benign and malignant tissue. (Nature 2022)

- DOI: 10.1038/s41586-022-05023-2 | PMCID: PMC9365699 | PMID: 35948708
- Evidence: Finally, a two-dimensional UMAP embedding was constructed from the previously established top principal components for each tissue type.
- Full pipeline: quality control [BWA, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [BWA, FastQC] -> registration [BWA, FastQC] -> dimensionality reduction/clustering [GATK, UMAP] -> visualisation [Seurat v3.2.2] -> stage not stated [GSEA, Python, R, fgsea, tidyverse]

### Spatial multi-omic map of human myocardial infarction. (Nature 2022)

- DOI: 10.1038/s41586-022-05060-x | PMCID: PMC9364862 | PMID: 35948637
- Evidence: To visualize all nuclei in a two-dimensional embedding, a UMAP was created with Seurat’s RunUMAP function using the first 30 principal components of harmony’s PCA correction embedding.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.32.1] -> visualisation [UMAP] -> stage not stated [ArchR v1.0.1, CellPhoneDB, ImageJ, MACS2, R v1.16, scDblFinder v1.4.0]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Evidence: Principal component analysis and UMAP dimension reduction with 30 principal components were performed 49 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### The sequences of 150,119 genomes in the UK Biobank. (Nature 2022)

- DOI: 10.1038/s41586-022-04965-x | PMCID: PMC9329122 | PMID: 35859178
- Evidence: To achieve this, we defined three cohorts based on the most common ancestries identified among the participants, using a combination of (1) uniform manifold approximation and projection (UMAP) dimension reduction of 40 genetic principal components provided by UKB, and (2) ADMIXTURE analysis supervised on five reference populations and self-reported ethnicity information.
- Full pipeline: alignment/mapping [BWA] -> variant calling [IMPUTE2] -> normalisation [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> differential/statistical testing [LDSC] -> stage not stated [GATK, SAMtools v1.9, VEP]

### A transcriptomic axis predicts state modulation of cortical interneurons. (Nature 2022)

- DOI: 10.1038/s41586-022-04915-7 | PMCID: PMC9279161 | PMID: 35794483
- Evidence: Subtypes, types and subclasses are assigned correctly with 76.4%, 96.6% and 98.1% accuracy respectively. d , e , f , Using a 150-gene panel (selected by the ProMMT algorithm 10 , same panel used to generate the UMAP of Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Evidence: The resulting latent representation of each cell in the dataset was used for neighbour identification, Leiden clustering and uniform manifold approximation and projection (UMAP) visualization.
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### Biosynthetic potential of the global ocean microbiome. (Nature 2022)

- DOI: 10.1038/s41586-022-04862-3 | PMCID: PMC9259500 | PMID: 35732736
- Evidence: These distances were dimensionally reduced using UMAP 77 and the resulting embedding was used for unsupervised density-based clustering with HDBSCAN 78 .
- Full pipeline: read trimming [IQ-TREE v2.0.3] -> alignment/mapping [BWA v0.7.17, DIAMOND v0.9.30, IQ-TREE v2.0.3, MAFFT v7.310, MUSCLE v3.8.1551] -> dimensionality reduction/clustering [MAFFT v7.310, UMAP] -> visualisation [R v4.0.0, ggplot2 v3.3.0] -> stage not stated [HMMER v3.1b, eggNOG v5.0, featureCounts v2.0.1]

### Developmental dynamics of two bipotent thymic epithelial progenitor types. (Nature 2022)

- DOI: 10.1038/s41586-022-04752-8 | PMCID: PMC9159946 | PMID: 35614226
- Evidence: The UMAP representation was used for cell cluster visualization 73 .
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor]

### Extricating human tumour immune alterations from tissue inflammation. (Nature 2022)

- DOI: 10.1038/s41586-022-04718-w | PMCID: PMC9132772 | PMID: 35545675
- Evidence: The dimensionality reduction generated by Harmony was used to calculate UMAP, and graph-based clustering with a resolution between 0.2 and 0.6.
- Full pipeline: quality control [Harmony, SAMtools v1.2] -> read trimming [STAR] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [R] -> stage not stated [Galaxy, HTSeq, Seurat]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: BNSTp Esr1 + clusters were visualized with UMAP (runUMAP, dims = 10).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### Intermittent PI3Kδ inhibition sustains anti-tumour immunity and curbs irAEs. (Nature 2022)

- DOI: 10.1038/s41586-022-04685-2 | PMCID: PMC9132770 | PMID: 35508656
- Evidence: UMAP analysis identified 10 T reg cell clusters, implying substantial T reg cell heterogeneity and tissue-dependent adaptations (Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [GSEA, MACS2, Seurat v3.1.5, fgsea v1.10.1]

### The development and evolution of inhibitory neurons in primate cerebrum. (Nature 2022)

- DOI: 10.1038/s41586-022-04510-w | PMCID: PMC8967711 | PMID: 35322231
- Evidence: PFC, prefrontal cortex; POH, preoptic hypothalamus; POA, preoptic area. b , Model of inhibitory neurogenesis. c , d , UMAP projections coloured by progenitor state and initial class for mice ( c ) and macaques ( d ).
- Full pipeline: quantification [kallisto v0.46] -> dimensionality reduction/clustering [AnnData, Scanpy, Seurat, UMAP] -> differential/statistical testing [SciPy, statsmodels v0.12.2] -> simulation/modelling [SciPy, scVelo] -> stage not stated [ImageJ, Python, scDblFinder v0.2.2]

### A multidimensional coding architecture of the vagal interoceptive system. (Nature 2022)

- DOI: 10.1038/s41586-022-04515-5 | PMCID: PMC8967724 | PMID: 35296859
- Evidence: Control scRNA-seq and Projection-seq data were then integrated and processed using the R package Seurat v.3 55 , and 42 cell clusters identified using the top 30 principal components (PCs) were visualized using UMAP 56 ( Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> simulation/modelling [Slingshot] -> visualisation [R, Seurat, UMAP, pheatmap] -> stage not stated [CellPhoneDB, Fiji, ImageJ]

### Twin study reveals non-heritable immune perturbations in multiple sclerosis. (Nature 2022)

- DOI: 10.1038/s41586-022-04419-4 | PMCID: PMC8891021 | PMID: 35173329
- Evidence: Resulting metaclusters were manually merged and annotated based on the median expression profile of individual metaclusters and localization on the UMAP.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [limma] -> simulation/modelling [Monocle, Python] -> visualisation [igraph] -> stage not stated [R, Seurat v4.0.3, ggplot2, pheatmap]

### GD2-CAR T cell therapy for H3K27M-mutated diffuse midline gliomas. (Nature 2022)

- DOI: 10.1038/s41586-022-04489-4 | PMCID: PMC8967714 | PMID: 35130560
- Evidence: UMAP embedding was performed using the first 50 principal components.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### Toroidal topology of population activity in grid cells. (Nature 2022)

- DOI: 10.1038/s41586-021-04268-7 | PMCID: PMC8810387 | PMID: 35022611
- Evidence: The nonlinear dimensionality reduction algorithm UMAP 43 , 44 was then applied to this matrix, yielding a two-dimensional point cloud in which each data point represented the autocorrelogram of one cell (Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.1.3, NumPy v1.18.1, UMAP, scikit-learn v0.22.1] -> differential/statistical testing [Python] -> stage not stated [Kilosort v2.5, SciPy]

### Single-cell delineation of lineage and genetic identity in the mouse brain. (Nature 2022)

- DOI: 10.1038/s41586-021-04237-0 | PMCID: PMC8770128 | PMID: 34912118
- Evidence: We used the first 35 Harmony embeddings for UMAP ( https://github.com/lmcinnes/umap ) visualizations and clustering analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [R v3.6.0, Seurat, scDblFinder v2.0.3, velocyto]

### Signature of long-lived memory CD8<sup>+</sup> T cells in acute SARS-CoV-2 infection. (Nature 2022)

- DOI: 10.1038/s41586-021-04280-x | PMCID: PMC8810382 | PMID: 34875673
- Evidence: Data scaling, principal component analysis, clustering and UMAP visualizations were performed on the integrated dataset using 15 principal components and a resolution of 0.5 for the shared nearest-neighbour clustering algorithm.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R v4.1.0, Seurat v4.0.3, fgsea]

### Human blastoids model blastocyst development and implantation. (Nature 2022)

- DOI: 10.1038/s41586-021-04267-8 | PMCID: PMC8791832 | PMID: 34856602
- Evidence: UMAP was used for visualization.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, HISAT2 v2.2.1] -> alignment/mapping [Bowtie2 v2.3.4.1, HISAT2 v2.2.1, HTSeq v0.13.5, featureCounts] -> quantification [HISAT2 v2.2.1, HTSeq v0.13.5, RSEM v1.3.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.18.1] -> visualisation [DESeq2 v1.18.1, UMAP] -> stage not stated [R v4.0, Seurat v4.0.1]

### Indigenous Australian genomes show deep structure and rich novel variation. (Nature 2023)

- DOI: 10.1038/s41586-023-06831-w | PMCID: PMC10733150 | PMID: 38093005
- Version used: **0.2.7.0**
- Evidence: UMAP (v.0.2.7.0) 70 was applied as per ref.
- Full pipeline: variant calling [GATK v3.8] -> normalisation [R v5.1] -> dimensionality reduction/clustering [R v5.1, UMAP v0.2.7.0] -> stage not stated [ADMIXTURE v1.3, BCFtools, BEAST v2.6.0, PLINK, ggplot2]

### A transcriptomic taxonomy of mouse brain-wide spinal projecting neurons. (Nature 2023)

- DOI: 10.1038/s41586-023-06817-8 | PMCID: PMC10719099 | PMID: 38092914
- Evidence: Finally, UMAP embedding was performed (RunUMAP).
- Full pipeline: quality control [STAR v2.7.1a] -> alignment/mapping [STAR v2.7.1a] -> quantification [QuPath v0.4.1] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [ggpubr] -> machine learning [Cellpose] -> visualisation [ggplot2, pheatmap] -> stage not stated [Seurat v4.3.0]

### A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06812-z | PMCID: PMC10719114 | PMID: 38092916
- Evidence: UMAP projection We performed PCA based on the imputed gene expression matrix of 8,460 marker genes using the 10xv3 reference.
- Full pipeline: quantification [UMAP] -> normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> stage not stated [Cellpose, Jupyter, WGCNA, limma, scDblFinder]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Evidence: To visualize clusters, we performed the UMAP nonlinear dimension reduction technique 70 .
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Molecularly defined and spatially resolved cell atlas of the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06808-9 | PMCID: PMC10719103 | PMID: 38092912
- Evidence: 21 ). b , Uniform manifold approximation and projection (UMAP) of the integrated scRNA-seq and MERFISH data with cells coloured by experimental modalities (left) or by major brain regions in which the registered cells reside (right).
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose v2.0] -> stage not stated [CellChat, scDblFinder, scikit-learn]

### Lung dendritic-cell metabolism underlies susceptibility to viral infection in diabetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06803-0 | PMCID: PMC10733144 | PMID: 38093014
- Evidence: For each of the subsets, variable genes, principal component analysis, clustering and UMAP were recalculated.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, fastp v0.23.0] -> alignment/mapping [Bowtie2 v2.3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools v2.26.0, MACS2, SAMtools v1.9, Seurat v4.0.1]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: Calculate principal components (PCs) in the selected cell-by-CEF matrices and generate the t -SNE 78 and UMAP 79 embeddings for visualization. t -SNE was performed using the openTSNE 80 package using previously described procedures 81 .
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### Evolution of neuronal cell classes and types in the vertebrate retina. (Nature 2023)

- DOI: 10.1038/s41586-023-06638-9 | PMCID: PMC10719112 | PMID: 38092908
- Evidence: We selected the top 20–25 latent variables in the integrated space to identify clusters and generate 2D UMAP visualizations.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat v4.3.0, ggplot2 v3.4.2] -> visualisation [Seurat v4.3.0, UMAP, ggplot2 v3.4.2]

### Single-cell analysis of chromatin accessibility in the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06824-9 | PMCID: PMC10719105 | PMID: 38092917
- Evidence: The total number of cells represents the number of cells covered by our previous study (last) and updated in the current study (new). c , UMAP 81 embedding and clustering analysis of snATAC–seq data.
- Full pipeline: dimensionality reduction/clustering [BEDTools, UMAP, clusterProfiler, scikit-learn] -> stage not stated [HOMER, MACS2, Monocle, R, RepeatMasker, Seurat, deepTools, scDblFinder]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Evidence: The merged dataset was then centred, dimensionally reduced with principal-component analysis using 20 dimensions and embedded with UMAP.
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Evidence: To visualize the distribution of cells with a specific perturbation (at the gene level) on the UMAP, contour density plots were generated using the ggplot2 (v.3.3.5) R package.
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### CD201&lt;sup&gt;+&lt;/sup&gt; fascia progenitors choreograph injury repair. (Nature 2023)

- DOI: 10.1038/s41586-023-06725-x | PMCID: PMC10665192 | PMID: 37968392
- Evidence: The UMAP algorithm was used as the preferred dimensional reduction method.
- Full pipeline: alignment/mapping [STAR v2.5.2a, Scanpy] -> quantification [Matplotlib, seaborn] -> dimensionality reduction/clustering [UMAP, scVelo] -> differential/statistical testing [SciPy] -> simulation/modelling [scVelo]

### Illuminating protein space with a programmable generative model. (Nature 2023)

- DOI: 10.1038/s41586-023-06728-8 | PMCID: PMC10686827 | PMID: 37968394
- Evidence: 13 , we present samples from Chroma and a set of native structures with global topology descriptors derived from knot theory 43 , 44 and embed them into two dimensions with UMAP 45 .
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Single-cell, whole-embryo phenotyping of mammalian developmental disorders. (Nature 2023)

- DOI: 10.1038/s41586-023-06548-w | PMCID: PMC10665194 | PMID: 37968388
- Evidence: The dimensionality of the data was reduced by PCA (30 components) first and then with UMAP, followed by Louvain clustering carried out on the 10 PCs (resolution = 1.2).
- Full pipeline: read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [AnnData v0.7.5.2, Monocle, Scanpy, Seurat, UMAP, scDblFinder, scVelo v0.2.4] -> stage not stated [ggplot2 v3.3.5]

### Embryo-scale reverse genetics at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06720-2 | PMCID: PMC10665197 | PMID: 37968389
- Evidence: Each of these groups was re-processed, embedded in three dimensions with UMAP and subclustered.
- Full pipeline: alignment/mapping [Seurat] -> dimensionality reduction/clustering [Monocle v1.3.1, UMAP] -> differential/statistical testing [GSEA, R] -> stage not stated [ImageJ, fgsea v1.26.0]

### Autoantibodies against type I IFNs in humans with alternative NF-κB pathway deficiency. (Nature 2023)

- DOI: 10.1038/s41586-023-06717-x | PMCID: PMC10665196 | PMID: 37938781
- Evidence: NK, natural killer cells; mDCs and pDCs, myeloid and plasmacytoid dendritic cells, respectively. b , Uniform manifold approximation and projection (UMAP)-based unsupervised clustering analysis of CD19 + B cells from a concatenated group of 10 patients with p52 LOF /IκBδ GOF variants and 31 age-matched controls (HC), with a heat map showing the mean levels of the surface markers included in the clu...
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSVA]

### Deconstruction of rheumatoid arthritis synovium defines inflammatory subtypes. (Nature 2023)

- DOI: 10.1038/s41586-023-06708-y | PMCID: PMC10651487 | PMID: 37938773
- Evidence: OA, osteoarthritis; RA, rheumatoid arthritis; sig., significant. e , Integrative uniform manifold approximation and projection (UMAP) based on mRNA and protein discriminated major cell types, f , Hierarchical clustering of cell-type abundances captures six rheumatoid arthritis subgroups, referred to as CTAPs.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: ...ding, annotation and integration of the atlas, and the biological entities that were investigated. b , Uniform manifold approximation and projection (UMAP) plot of an integrated pan-cancer snATAC-seq object showing the distribution of 250,222 immune, 69,684 stromal, 69,506 normal epithelial and 588,895 cancer cells across 225 samples.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Dopaminergic systems create reward seeking despite adverse consequences. (Nature 2023)

- DOI: 10.1038/s41586-023-06671-8 | PMCID: PMC10632144 | PMID: 37880370
- Evidence: UMAP reduction 79 of the data and clustering was performed using the Seurat v3 R package 80 .
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> stage not stated [ComplexHeatmap v1.10.2, Cytoscape v3.9.1]

### Mexican Biobank advances population and medical genomics of diverse ancestries. (Nature 2023)

- DOI: 10.1038/s41586-023-06560-0 | PMCID: PMC10600006 | PMID: 37821706
- Evidence: 6 and 7 ) were used to carry out the uniform manifold approximation and projection (UMAP) analysis (Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [ADMIXTURE, FUMA, R, REGENIE v3.1.3, VCFtools, VEP, ggplot2, tidyverse]

### Design and testing of a humanized porcine donor for xenotransplantation. (Nature 2023)

- DOI: 10.1038/s41586-023-06594-4 | PMCID: PMC10567564 | PMID: 37821590
- Evidence: UMAP, uniform manifold approximation and projection. e , The 3KO.7TG porcine donors ( n = 3) showed normal measured glomerular filtration rate (mGFR) compared with age-matched WT Yucatan pigs ( n = 4).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Evidence: PCA and nearest neighbour graphs were calculated to visualize on a UMAP projection.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Evidence: Specifically, we excluded genes with either a maximum read count per cell of less than 10 or with expression detected in fewer than 10 cells at a count threshold of 5, computed principal component analysis (PCA) and UMAP, and performed Leiden clustering on the k NN constructed on the principle component space.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### Transcriptional linkage analysis with in vivo AAV-Perturb-seq. (Nature 2023)

- DOI: 10.1038/s41586-023-06570-y | PMCID: PMC10567566 | PMID: 37730998
- Evidence: UMAP embedding of ~8,000 AAV.PHP.B-infected nuclei isolated from the dCas9-KRAB mouse prefrontal cortex. c .
- Full pipeline: normalisation [Seurat v3.0] -> dimensionality reduction/clustering [Seurat v3.0, UMAP] -> differential/statistical testing [R v3.36.0, edgeR] -> stage not stated [Enrichr v2.1, GSEA, Nextstrain v1.0.0, fgsea v3.17]

### Transgenic ferret models define pulmonary ionocyte diversity and function. (Nature 2023)

- DOI: 10.1038/s41586-023-06549-9 | PMCID: PMC10533402 | PMID: 37730992
- Evidence: Created with BioRender.com . b , UMAP of total tracheal epithelial cells captured across all ferret genotypes (WT, FOXI1 -KO and FOXI1 -Cre ERT2 ::ROSA-TG), coloured by broad cell type. c , Cell–cell Pearson correlation coefficient ( r , colour bar) between each pair of cells (large clusters down-sampled to 200 cells for visualization). d , Top, ferret tracheal whole-mount immunostained for ATP6V1...
- Full pipeline: alignment/mapping [kallisto] -> variant calling [UMAP] -> quantification [R, Seurat] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [brms] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2]

### Single-cell brain organoid screening identifies developmental defects in autism. (Nature 2023)

- DOI: 10.1038/s41586-023-06473-y | PMCID: PMC10499611 | PMID: 37704762
- Evidence: To visualize the dataset, the first 20 principal components were used to compute a UMAP embedding.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2, scVelo v0.2.4] -> differential/statistical testing [R, clusterProfiler] -> visualisation [UMAP, ggplot2] -> stage not stated [Cutadapt, MACS2 v2.2.6, Seurat, Signac v1.4.0, kallisto v0.46.2]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Evidence: UMAP visualization was performed by scaling and reducing the dimensionality of the data using the Seurat standard function.
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### Complete human day 14 post-implantation embryo models from naive ES cells. (Nature 2023)

- DOI: 10.1038/s41586-023-06604-5 | PMCID: PMC10584686 | PMID: 37673118
- Evidence: Uniform manifold approximation and projection (UMAP) analysis identified a total of 13 separate cell clusters (Fig.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Signac v1.6.0] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [SciPy v1.8.0, seaborn v0.11.0] -> visualisation [SciPy v1.8.0, seaborn v0.11.0] -> stage not stated [R, pheatmap, scDblFinder v1.6]

### Non-cell-autonomous cancer progression from chromosomal instability. (Nature 2023)

- DOI: 10.1038/s41586-023-06464-z | PMCID: PMC10468402 | PMID: 37612508
- Evidence: We then use scanpy to compute principal components on this matrix, choosing an optimal number of principal components for data dimensionality based on kneepoint analysis of the cumulative variance described by each component, and visualize in two dimensions with UMAP (Extended Data Fig.
- Full pipeline: alignment/mapping [Picard] -> quantification [ImageJ] -> normalisation [GSEA, ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Scanpy, UMAP] -> stage not stated [CellChat, CellPhoneDB, MACS2, Seurat v4.1.1]

### Endothelial AHR activity prevents lung barrier disruption in viral infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06287-y | PMCID: PMC7615136 | PMID: 37587341
- Evidence: Data are representative of four independent experiments with similar results. e, f, Expression of indicated genes in uniform manifold approximation and projection (UMAP) plots of mouse ( e ) and human ( f ) lung scRNA-seq datasets obtained from lungendothelialcellatlas.com. g, Primary human lung microvasculature endothelial cell (HMVEC-L) cultures were treated with AHR agonist FICZ or antagonist C...
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RSEM, STAR v2.5.2a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA v2.2.3, R v3.6.0] -> stage not stated [ImageJ, MACS2, QuPath]

### Transient naive reprogramming corrects hiPS cells functionally and epigenetically. (Nature 2023)

- DOI: 10.1038/s41586-023-06424-7 | PMCID: PMC10447250 | PMID: 37587336
- Evidence: Top 1000 most variable features were used for scaling and PCA of RNA data, using 10 dimensions with a resolution of 0.6 for clustering and UMAP.
- Full pipeline: read trimming [Bowtie2, HISAT2, fastp] -> alignment/mapping [Bowtie2, HISAT2, SAMtools v1.13, fastp, minimap2 v2.17] -> normalisation [UMAP] -> dimensionality reduction/clustering [BEDTools v2.30.0, HOMER, UMAP] -> differential/statistical testing [edgeR] -> stage not stated [MACS2, R, Seurat v3.1.1]

### Platelet factors attenuate inflammation and rescue cognition in ageing. (Nature 2023)

- DOI: 10.1038/s41586-023-06436-3 | PMCID: PMC10468395 | PMID: 37587343
- Evidence: The first 20 PCA components were used to cluster cells by Louvain clustering implemented in Seurat while UMAP plots were independently generated to aid in 2D representation of multidimensional data independent of the clustering.
- Full pipeline: alignment/mapping [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> quantification [DESeq2, ImageJ, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v2.7.3a, RSEM v1.3.1, STAR v2.7.3a] -> stage not stated [Enrichr, Seurat]

### Endothelial sensing of AHR ligands regulates intestinal homeostasis. (Nature 2023)

- DOI: 10.1038/s41586-023-06508-4 | PMCID: PMC10533400 | PMID: 37586410
- Evidence: 1 Single-cell transcriptomics reveals the cellular complexity of enteric vasculature. a , Uniform manifold approximation and projection (UMAP) of small intestine endothelial cells.
- Full pipeline: alignment/mapping [STAR v2.2.7a, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP, scDblFinder] -> differential/statistical testing [GSEA] -> visualisation [DESeq2, R, ggplot2 v3.3.3] -> stage not stated [Bioconductor, ComplexHeatmap v2.2.0, SCENIC v1.2.4, Seurat v3.2.0]

### Dissecting human population variation in single-cell responses to SARS-CoV-2. (Nature 2023)

- DOI: 10.1038/s41586-023-06422-9 | PMCID: PMC10482701 | PMID: 37558883
- Evidence: The diagram was created using BioRender. b , c , Uniform manifold approximation and projection (UMAP) embedding of 1,047,824 PBMCs: resting (non-stimulated; NS) or stimulated with SARS-CoV-2 (COV) or IAV for 6 h. b , The colours indicate the 22 cell types inferred. c , The distribution of cells in the NS, COV and IAV conditions on UMAP coordinates.
- Full pipeline: variant calling [BCFtools, GATK, PLINK v1.9] -> quantification [lme4] -> normalisation [PLINK v1.9, lme4] -> dimensionality reduction/clustering [Harmony v0.1.0, PLINK v1.9, Seurat v4.1.1, UMAP] -> differential/statistical testing [lme4] -> stage not stated [GSEA, R, fgsea]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Evidence: Cells were then clustered with the FindClusters function based on the Louvain algorithm 66 and UMAP embedding was generated with the RunUMAP function.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### cGAS-STING drives ageing-related inflammation and neurodegeneration. (Nature 2023)

- DOI: 10.1038/s41586-023-06373-1 | PMCID: PMC10412454 | PMID: 37532932
- Evidence: Scale bars, 10 μm. d , Brain mRNA expression levels of proinflammatory genes and ISGs from Tmem119-creER T2 -Cgas WT/WT ( n = 5) and Tmem119-creER T2 -Cgas WT/R241E ( n = 6) mice. e , Uniform manifold approximation and projection (UMAP) plots visualizing microglial single nuclei, coloured by cell identity (left, homeostatic microglia (H-MG); disease-associated microglia (DAM-1/2); IFN-associated m...
- Full pipeline: alignment/mapping [HTSeq, STAR, featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.38.2, ImageJ, Seurat]

### Netrin-1 blockade inhibits tumour growth and EMT features in endometrial cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06367-z | PMCID: PMC10412451 | PMID: 37532934
- Evidence: 01-040 with two lung metastasis biopsies—one before treatment (C1D1), and one after two cycles of NP137 treatment (C3D1). b , Uniform manifold approximation and projection (UMAP) plot of 16,375 cells from two lung metastasis biopsies (left) or before treatment with 9,216 cells (C1D1, middle) and after treatment with 7,159 cells (C3D1, right), coloured by their four major cell types. c , Compositio...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, CellChat v1.6.0, DESeq2, R v4.0.3, STAR v2.7.10a, Seurat, scDblFinder v2.0.3]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: Principal components and cluster annotations were then imported into Seurat (v.4.0.0) and uniform manifold approximation and projection (UMAP) dimensionality reduction was performed using the top 50 principal components identified using Pagoda2.
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### A cell-type-specific error-correction signal in the posterior parietal cortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06357-1 | PMCID: PMC10412446 | PMID: 37468637
- Evidence: We clustered cell types using the Leiden algorithm 40 (resolution = 0.7) and visualized cell type clusters with UMAP 41 (default parameters within SnapATAC).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose] -> visualisation [UMAP] -> stage not stated [AnnData, Fiji, ImageJ, Kilosort v2.5, Psychtoolbox, Python, Suite2p]

### Organization of the human intestine at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-05915-x | PMCID: PMC10356619 | PMID: 37468586
- Evidence: After quality control and filtering, doublet scores for all multiome cells and all non-multiome snATAC cells were computed using the ArchR function addDoubletScores with k = 10, knnMethod = “UMAP” and LSIMethod = 1.
- Full pipeline: quality control [ArchR, Seurat, UMAP] -> dimensionality reduction/clustering [ArchR, Scanpy, Seurat, Squidpy, UMAP, limma, scDblFinder] -> differential/statistical testing [limma] -> visualisation [ImageJ, limma] -> stage not stated [MACS2, R]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Evidence: CT, crista terminalis; ENDO, endocardium; EPI, epicardium; IAS, interatrial septum; MS, membranous septum; TV, tricuspid valve. c – e , UMAP embedding of gene expression data of SAN aCMs ( c ), AVN aCMs ( d ), and AX and AVN CMs ( e ).
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### The dynamics of pattern matching in camouflaging cuttlefish. (Nature 2023)

- DOI: 10.1038/s41586-023-06259-2 | PMCID: PMC10322717 | PMID: 37380772
- Evidence: It was used to construct the UMAP visualization, estimate the dimensionality of camouflage pattern space and study camouflage pattern dynamics.
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> machine learning [Keras, OpenCV] -> visualisation [R, UMAP] -> stage not stated [PsychoPy, Scanpy]

### Self-patterning of human stem cells into post-implantation lineages. (Nature 2023)

- DOI: 10.1038/s41586-023-06354-4 | PMCID: PMC10584676 | PMID: 37369348
- Evidence: We used the UMAP algorithm for reduction into two or three dimensions.
- Full pipeline: read trimming [Cutadapt v2.4] -> quantification [ilastik] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [ComplexHeatmap, Slingshot] -> stage not stated [DESeq2, GATK v4.1.4.1, R v4.1.3, SAMtools, Seurat v4.3.0, ggplot2]

### Pluripotent stem cell-derived model of the post-implantation human embryo. (Nature 2023)

- DOI: 10.1038/s41586-023-06368-y | PMCID: PMC10584688 | PMID: 37369347
- Evidence: For UMAP projections, SCTransform was used for RNA counts with percent mitochondrial counts and cell cycle scores regressed.
- Full pipeline: registration [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape] -> stage not stated [CellPhoneDB v2.0, SCENIC, Seurat, Signac, scDblFinder]

### Injury prevents Ras mutant cell expansion in mosaic skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06198-y | PMCID: PMC10322723 | PMID: 37344586
- Evidence: Non-linear dimensionality reduction was carried out by running UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Scanpy v1.6, Seurat, SoupX, scDblFinder, scikit-learn v0.24.2]

### CD4<sup>+</sup> T cell-induced inflammatory cell death controls immune-evasive tumours. (Nature 2023)

- DOI: 10.1038/s41586-023-06199-x | PMCID: PMC10307640 | PMID: 37316667
- Evidence: Subsequently, dimensionality reduction was performed using UMAP with scanpy.tl.umap.
- Full pipeline: quantification [velocyto] -> normalisation [AnnData, Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [ImageJ v1.52i, R, scVelo]

### Ultraviolet radiation shapes dendritic cell leukaemia transformation in the skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06156-8 | PMCID: PMC10284703 | PMID: 37286599
- Evidence: We then used Harmony reduction to determine clusters and UMAP coordinates.
- Full pipeline: alignment/mapping [BWA v0.7.15, STAR v2.6.0c] -> variant calling [Seurat] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BCFtools v1.10.2, GATK, Mutect2, Picard v2.5.0, R, data.table, tidyverse]

### Myelin dysfunction drives amyloid-β deposition in models of Alzheimer's disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06120-6 | PMCID: PMC10247380 | PMID: 37258678
- Evidence: For all cells sequenced from 3-month-old animals, the first 50 PCs were used for further neighbouring embedding using UMAP 79 , as well as for performing the clustering analysis with a resolution of 0.5 using K -nearest neighbour algorithm.
- Full pipeline: quality control [STAR v2.5.2b] -> alignment/mapping [DESeq2 v1.26.0, STAR v2.5.2b, featureCounts v1.6.3] -> quantification [DESeq2 v1.26.0, featureCounts v1.6.3] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP] -> differential/statistical testing [DESeq2 v1.26.0, featureCounts v1.6.3] -> visualisation [DESeq2 v1.26.0, featureCounts v1.6.3] -> stage not stated [MACS2, R v4.04, afex v0.28]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Evidence: With these retained components, we then computed a UMAP embedding and the neighbours for posterior clustering.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### Deterministic evolution and stringent selection during preneoplasia. (Nature 2023)

- DOI: 10.1038/s41586-023-06102-8 | PMCID: PMC10247377 | PMID: 37258665
- Evidence: ...ld change (FC) from previous time points for each culture over time (interpolated passage number). c , Uniform manifold approximation and projection (UMAP) visualizations coloured according to culture (left) and time point (right) for D1, depicting 13,984 cells. d , Dot-plot depicting the expression of selected marker genes for individual cultures and time points.
- Full pipeline: quality control [GSEA] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP]

### Uridine-derived ribose fuels glucose-restricted pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06073-w | PMCID: PMC10232363 | PMID: 37198494
- Evidence: UMAP plot showing the expression of UPP1 at the transcript level, as determined by single cell RNA seq of PDA tissues from two patients (#1238 and 1302). c .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.5.2, limma] -> visualisation [ComplexHeatmap, ggplot2 v3.3.5, tidyverse v0.8.3] -> stage not stated [GSEA v4.0.3]

### Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06063-y | PMCID: PMC10171177 | PMID: 37165196
- Evidence: ( A ) Uniform manifold approximation and projection (UMAP) plots of single peripheral blood T cells by single-cell RNA/TCR sequencing in n = 4 patients (patients 1, 10, 11 and 29) stratified by lineage (CD8 vs.
- Full pipeline: alignment/mapping [SAMtools v1.6] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [Scanpy] -> stage not stated [Mutect2 v1.1.7, SciPy, SnpEff v4.3t, Strelka v1.0.15]

### Learnable latent embeddings for joint behavioural and neural analysis. (Nature 2023)

- DOI: 10.1038/s41586-023-06031-6 | PMCID: PMC10172131 | PMID: 37138088
- Evidence: CEBRA can be used as a dropin replacement in existing data pipelines for algorithms such as t -SNE, UMAP, PCA or FastICA.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [NumPy, PyTorch, scikit-learn]

### Glioblastoma remodelling of human neural circuits decreases survival. (Nature 2023)

- DOI: 10.1038/s41586-023-06036-1 | PMCID: PMC10191851 | PMID: 37138086
- Evidence: FC3 patient sample contains no copy number variation but has high level amplification of NTRK2 gene. d , Single-cell RNA transcriptomic profile UMAP confirms distinct cell populations including non-tumour astrocytes and neurons. e , Gene enrichment profile used to identify each of the UMAP cell populations. f , g , Feature plot for TSP-1 in combined (HFC + LFC) and LFC (n = 7,065 cells, 3 particip...
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [HISAT2, featureCounts] -> normalisation [Python, Seurat v3.0.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Python, R v3.1, Seurat v3.0.1, featureCounts] -> stage not stated [ImageJ]

### Dedifferentiation maintains melanocyte stem cells in a dynamic niche. (Nature 2023)

- DOI: 10.1038/s41586-023-05960-6 | PMCID: PMC10132989 | PMID: 37076619
- Evidence: For each condition, UMAP dimension reduction was performed on the normalized, centred, scaled nUMI count matrices using the first ten PCs.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> structure determination [ImageJ] -> visualisation [Seurat] -> stage not stated [GSEA]

### Astrocyte-neuron subproteomes and obsessive-compulsive disorder mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-05927-7 | PMCID: PMC10132990 | PMID: 37046092
- Evidence: Mean and s.e.m. are shown. c , Left, uniform manifold approximation and projection (UMAP) plot of striatal cells ( n = 31,956 individual cells, replotted from our published scRNA-seq data 36 .
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Bioconductor, limma v3.54] -> visualisation [Cytoscape v3.8, R, UMAP] -> stage not stated [Enrichr, Fiji, HOMER, STRING db]

### Genomic-transcriptomic evolution in lung cancer and metastasis. (Nature 2023)

- DOI: 10.1038/s41586-023-05706-4 | PMCID: PMC10115639 | PMID: 37046093
- Evidence: Finally, tumour regions clustering with tumour-adjacent normal tissue regions (see the section ‘UMAP clustering’) and tumour regions with a low purity were also excluded from further analyses.
- Full pipeline: quality control [FastQC v0.11.2, MultiQC v1.9, STAR v2.5.2a, Trim Galore] -> read trimming [Bismark v0.14.4, Cutadapt, edgeR v3.26.5] -> alignment/mapping [Bismark v0.14.4, RSEM v1.3.3, STAR v2.5.2a] -> variant calling [Mutect2] -> quantification [DESeq2 v1.24.0, RSEM v1.3.3] -> normalisation [DESeq2 v1.24.0, edgeR v3.26.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, fgsea v1.10.1] -> machine learning [Python, TensorFlow v2.6.0, scikit-learn v0.0] -> visualisation [MultiQC v1.9] -> stage not stated [BCFtools v1.10.2, GATK v4.1.7.0, Nextflow v20.07.1, R, SAMtools v1.9, ggplot2 v3.2.1, ggpubr v0.4.0, limma, lme4 v3.1]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Evidence: The resulting latent representation of the data was used for calculating neighbourhood graph, UMAP and further Louvain clustering.
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### Spatial epigenome-transcriptome co-profiling of mammalian tissues. (Nature 2023)

- DOI: 10.1038/s41586-023-05795-1 | PMCID: PMC10076218 | PMID: 36922587
- Evidence: Normalized RNA data were clustered and RNA UMAP was built.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.2] -> visualisation [ArchR v1.0.1, Seurat v4.1] -> stage not stated [Monocle, Signac v1.8]

### An airway-to-brain sensory pathway mediates influenza-induced sickness. (Nature 2023)

- DOI: 10.1038/s41586-023-05796-0 | PMCID: PMC10033449 | PMID: 36890237
- Evidence: Single-cell transcriptomics All UMAP plots in this manuscript were made from published single-cell transcriptome data (GEO Accession ID: GSE145216 ) 22 using Seurat (4.1.0) and R Studio (4.1.2).
- Full pipeline: dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> stage not stated [ImageJ v1.53q]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: An additional PCR step to amplify viral transcripts within the cDNA library was used to assign infection status to each nucleus. b , Left, uniform manifold approximation and projection (UMAP) visualizations of Npas4 fl/fl and Tip60 fl/fl snRNA-seq datasets.
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: (a) UMAP plot of chimeric E8.5 embryos of wild-type (WT) and Tal1 KO cells (25,307 cells and 26,311 cells, respectively) from a published scRNA-seq atlas of mouse gastrulation and organogenesis 30 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Tissue CD14&lt;sup&gt;+&lt;/sup&gt;CD8&lt;sup&gt;+&lt;/sup&gt; T cells reprogrammed by myeloid cells and modulated by LPS. (Nature 2023)

- DOI: 10.1038/s41586-022-05645-6 | PMCID: PMC7619353 | PMID: 36697826
- Evidence: Clustering was performed using the Leiden algorithm (0.6 resolution) and embedded using Uniform Manifold Approximation and Projection (UMAP).
- Full pipeline: quality control [STAR, Seurat] -> alignment/mapping [STAR] -> quantification [HTSeq v0.10.0, ImageJ, STAR] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [seaborn] -> simulation/modelling [scDblFinder] -> visualisation [seaborn] -> stage not stated [Python v3.6]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Evidence: Uniform manifold approximation and projection (UMAP) 58 was used to visualize the cells in a two-dimensional space, followed by the FindNeighbors and FindClusters functions of Seurat.
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Evidence: Right, basal Cdkn1a expression ( n = 3 biological replicates per group). n , Representative uniform manifold approximation and projection (UMAP) plots of Gpr31b and Ltb4r2 expression by single-cell RNA-seq in PND1 lungs. o , BAL AM numbers in adult WT and Ltb4r2 −/− mice ( n = 4 per group). p , BrdU + AMs after GM-CSF culture (left; n = 3 (Uns.) or 6 (GM-CSF) fields of view per group) and basal Cd...
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Phenotypic signatures of immune selection in HIV-1 reservoir cells. (Nature 2023)

- DOI: 10.1038/s41586-022-05538-8 | PMCID: PMC9908552 | PMID: 36599977
- Evidence: For an initial global analysis of the phenotype of HIV-1-infected cells from PB, we visualized in silico-gated CD3 + CD4 + cells (after exclusion of contaminating CD45RA + CCR7 + naive T cells) from the different categories on uniform manifold approximation and projection (UMAP) 25 plots, classifying the mCD4 + T cell pool in five distinct, computationally defined phenotypic clusters (Fig.
- Full pipeline: quality control [UMAP] -> alignment/mapping [MAFFT, SAMtools v1.9] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [R] -> visualisation [MAFFT, UMAP] -> stage not stated [Cutadapt v2.5]

### The molecular evolution of spermatogenesis across mammals. (Nature 2023)

- DOI: 10.1038/s41586-022-05547-7 | PMCID: PMC9834047 | PMID: 36544022
- Evidence: The uniform manifold approximation and projection (UMAP) embedding coordinates were calculated using the RunUMAP function (parameters dims = 1:20, 1:20, 1:20, 1:20, 1:20, 1:20, 1:20, 1:17, 1:10, 1:10 and 1:10, and min_dist = 0.3, 0.3, 0.1, 0.1, 0.3, 0.3, 0.3, 0.1, 0.2, 0.3 and 0.6, respectively, for human, chimpanzee, bonobo, gorilla, gibbon, macaque, marmoset, mouse, opossum, platypus and chicken...
- Full pipeline: read trimming [Cutadapt v1.8.3] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [limma] -> stage not stated [StringTie v1.3.3, ape (R) v5.3, ggplot2 v3.2.1, pheatmap v1.0.12, scDblFinder, tidyverse v1.3.0]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Evidence: PCA was performed for dimensionality reduction and the first 30 components were used for UMAP embedding and clustering.
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Active eosinophils regulate host defence and immune responses in colitis. (Nature 2023)

- DOI: 10.1038/s41586-022-05628-7 | PMCID: PMC9977678 | PMID: 36509106
- Evidence: Clustering and UMAP visualization were performed on the merged dataset using 50 principal components and a resolution of 0.3 for the shared nearest neighbour clustering algorithm.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Monocle v2.3.6] -> dimensionality reduction/clustering [ComplexHeatmap, UMAP] -> differential/statistical testing [GSEA, edgeR] -> simulation/modelling [Monocle v2.3.6] -> visualisation [ComplexHeatmap, UMAP] -> stage not stated [CellPhoneDB v2.0.0, Cellpose v2.0.4, R, SCENIC v1.2.4, Seurat v4.0.3, fgsea, ggplot2, pheatmap, scVelo, scikit-image, velocyto]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Evidence: To obtain a two-dimensional representation of the data, we performed UMAP 57 using RunUMAP() with spread = 0.5, min.dist = 0.2 and otherwise the default parameters.
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: The dimensions of these eight metrics were reduced to generate a neighbourhood graph and UMAP for each sample, which was then clustered at low resolution; these clusters are referred to as quality control (QC) clusters.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### Exaptation of ancestral cell-identity networks enables C&lt;sub&gt;4&lt;/sub&gt; photosynthesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08204-3 | PMCID: PMC11618092 | PMID: 39567684
- Evidence: Subsequent UMAP projections were constructed using the first 30 principal components.
- Full pipeline: dimensionality reduction/clustering [Seurat, Signac, UMAP] -> differential/statistical testing [OrthoFinder] -> stage not stated [DESeq2, MACS2]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Evidence: Latent variables obtained from this were then used to determine neighbourhoods followed by dimensionality reduction in UMAP.
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Evidence: A UMAP visualization was generated based on the WNN graph to represent the weighted combination of both modalities.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### An integrated transcriptomic cell atlas of human neural organoids. (Nature 2024)

- DOI: 10.1038/s41586-024-08172-8 | PMCID: PMC11578878 | PMID: 39567792
- Evidence: The heatmap shows average presence scores per cluster in the primary reference (columns). e , UMAP of primary reference coloured by the dissected regions (right) and the maximum presence scores across the screen conditions (left). f , Gain of cell cluster coverage of screen conditions relative to HNOCA datasets, with negative values trimmed to zero.
- Full pipeline: read trimming [UMAP] -> alignment/mapping [RSEM] -> dimensionality reduction/clustering [SciPy, UMAP] -> structure determination [Python] -> machine learning [R] -> stage not stated [AnnData, Jupyter, Scanpy, Singularity, edgeR]

### Examining the role of common variants in rare neurodevelopmental conditions. (Nature 2024)

- DOI: 10.1038/s41586-024-08217-y | PMCID: PMC11634775 | PMID: 39567701
- Evidence: 11 ) using uniform manifold approximation and projection (UMAP) 76 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GCTA, LDSC] -> stage not stated [PLINK, VEP]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Evidence: 11 Quality metrics of mouse snRNAseq data. a , Gene counts and the number of unique molecular identifiers (UMIs) per condition of mouse epiAT samples. b , UMAP visualization representing integrated epiAT samples from the weight loss study (C, CC, CCC, H, HH, HC, HHC) and from the “yoyo” study (CCH, HCH) coloured by predicted cell subtypes from the Emont et al. mouse epididymal AT dataset.
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### Adult skull bone marrow is an expanding and resilient haematopoietic reservoir. (Nature 2024)

- DOI: 10.1038/s41586-024-08163-9 | PMCID: PMC11618084 | PMID: 39537918
- Evidence: The principal components served as basis for k -nearest neighbour calculation (sc.pp.neighbors, n_neighbors=30), which were used as input for UMAP 70 layout (sc.tl.umap, min_dist=0.3).
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> dimensionality reduction/clustering [Matplotlib, UMAP] -> visualisation [Matplotlib] -> stage not stated [AnnData, ImageJ, Scanpy]

### NK2R control of energy expenditure and feeding to treat metabolic diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-08207-0 | PMCID: PMC11602716 | PMID: 39537932
- Evidence: Plot colours as in key in b . j , Identity of FOS + neurons in the NTS of EB1002-injected mice. k , Uniform manifold approximation and projection (UMAP) plot of expression data from 23,664 neurons coloured by populations according to ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> stage not stated [GEMMA, Seurat v4.3.0, VEP, data.table v1.14.2, tidyverse v1.3.1]

### Coordinated inheritance of extrachromosomal DNAs in cancer cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07861-8 | PMCID: PMC11541006 | PMID: 39506152
- Evidence: Statistical analysis was performed using two-sided Spearman correlation. g , Uniform manifold approximation and projection (UMAP) analysis of scATAC-seq data showing cell line annotations and copy-number (CN) calculations of indicated oncogenes. h , The log-transformed oncogene copy numbers between pairs of oncogenes in the indicated cell lines (Pearson’s R , two-sided test; P < 2.2 × 10 −16 for a...
- Full pipeline: read trimming [BWA, Bowtie2 v2.1.0, Picard, Trim Galore v0.6.4, Trimmomatic] -> alignment/mapping [BWA, Bowtie2 v2.1.0, MACS2 v2.2.7.1, Picard, SAMtools v1.9, Trimmomatic] -> quantification [ImageJ] -> normalisation [deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [deepTools] -> stage not stated [ArchR v1.0.1, Seurat v3.2.3]

### Identification and genetic dissection of convergent persister cell states. (Nature 2024)

- DOI: 10.1038/s41586-024-08124-2 | PMCID: PMC11634777 | PMID: 39506104
- Evidence: See next section for PCA and UMAP in Extended Data Fig.
- Full pipeline: read trimming [Cutadapt, featureCounts] -> alignment/mapping [Cutadapt, featureCounts] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP, edgeR, scikit-learn] -> differential/statistical testing [edgeR, limma] -> stage not stated [BLAST]

### A cellular basis for mapping behavioural structure. (Nature 2024)

- DOI: 10.1038/s41586-024-08145-x | PMCID: PMC11655361 | PMID: 39506112
- Evidence: Manifold analysis To visualize and further quantify the structure of neuronal activity in individual tasks, we embedded activity into a low dimensional space using UMAP, a non-linear dimensionality reduction technique previously used to visualize mFC population activity 34 , 49 .
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Matplotlib v3.7.3, NumPy v1.22.0, SciPy v1.10.1, TensorFlow, seaborn v0.13.2]

### Leptin-activated hypothalamic BNC2 neurons acutely suppress food intake. (Nature 2024)

- DOI: 10.1038/s41586-024-08108-2 | PMCID: PMC11618066 | PMID: 39478220
- Evidence: After the initial quality control, demultiplexing and normalization steps, all the singlets were then scaled and reduced dimensionally with principal component analysis and uniform manifold approximation and projection (UMAP).
- Full pipeline: quality control [UMAP] -> read trimming [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Evidence: ...right panels) on the day of transplantation, that is, 7 days after the first transduction (day 8). b , Uniform manifold approximation and projection (UMAP) representation of integrated single-cell transcriptome data from the six groups of cells shown in a , on day 8. c , Stacked barplots showing fraction of cells in each cluster.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Evidence: Scale bars, 2 mm. amp, amplification; del, deletion; LOH, loss of heterozygosity; NA, not applicable; UMAP, uniform manifold approximation and projection.
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Rhythmic IL-17 production by γδ T cells maintains adipose de novo lipogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08131-3 | PMCID: PMC11618085 | PMID: 39478228
- Evidence: Dimensionality reduction was performed using principal component analysis (PCA) with n = 100 dimensions and 2,000 or 3,000 variable features, and an elbow plot was used to determine the number of PCA dimensions used as input for UMAP 70 .
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v4.1.0]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Evidence: To have a final global visualization of the atlas, a doublet-free UMAP was generated (Fig.
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### One-shot entorhinal maps enable flexible navigation in novel environments. (Nature 2024)

- DOI: 10.1038/s41586-024-08034-3 | PMCID: PMC11602719 | PMID: 39385034
- Evidence: 34 , we used uniform manifold approximation and projection (UMAP) to project the spatial autocorrelograms of individual neurons into two dimensions (Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [DeepLabCut v2.2.0.6] -> stage not stated [Kilosort, Python, SciPy]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Evidence: We then applied UMAP for dimensionality reduction using the Scanpy tl.umap function for each anndata pair (GFP and mCherry cells under the same treatment).
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### CTLA4 blockade abrogates KEAP1/STK11-related resistance to PD-(L)1 inhibitors. (Nature 2024)

- DOI: 10.1038/s41586-024-07943-7 | PMCID: PMC11560846 | PMID: 39385035
- Evidence: Dimensionality reduction and two-dimensional visualization of cell clusters was performed using uniform manifold approximation and projection (UMAP) with the Seurat function RunUMAP.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> normalisation [DESeq2, Harmony v0.1.1, R, Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Temporally distinct 3D multi-omic dynamics in the developing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-08030-7 | PMCID: PMC11560841 | PMID: 39385032
- Evidence: Iterative clustering was then carried out with a combination of Leiden unsupervised clustering and UMAP dimensionality reduction, identifying clusters as cell types by marker gene body CH and CG hypomethylation.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [Bismark, Picard] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [LDSC] -> machine learning [Cellpose] -> stage not stated [Harmony]

### Connectomic reconstruction predicts visual features used for navigation. (Nature 2024)

- DOI: 10.1038/s41586-024-07967-z | PMCID: PMC11446847 | PMID: 39358517
- Evidence: UMAP in Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Psychtoolbox, SciPy]

### Neuronal wiring diagram of an adult brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07558-y | PMCID: PMC11446842 | PMID: 39358518
- Evidence: To visualize information flow for neurons with inputs in the central brain in a common space, we treated the traversal distances starting from each seed population as a neuron embedding and built a uniform manifold approximation and projection (UMAP) from all of these embeddings (Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Evidence: Following the between-sample batch correction above, we computed a neighbourhood graph using the uniform manifold approximation and projection (UMAP) approach implemented in Scanpy and subsequently clustered with the Leiden algorithm.
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Single-cell CAR T atlas reveals type 2 function in 8-year leukaemia remission. (Nature 2024)

- DOI: 10.1038/s41586-024-07762-w | PMCID: PMC11485231 | PMID: 39322664
- Evidence: The diagram was created using BioRender. b , UMAP visualization of 695,819 high-quality single CAR T cells, filtered from 1,029,340 sequenced cells across all patients and donors.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat, Signac v1.12.0]

### The type 2 cytokine Fc-IL-4 revitalizes exhausted CD8&lt;sup&gt;+&lt;/sup&gt; T cells against cancer. (Nature 2024)

- DOI: 10.1038/s41586-024-07962-4 | PMCID: PMC11485240 | PMID: 39322665
- Evidence: Finally, the SCT data assay was reduced to two dimensions using uniform manifold approximation and projection (UMAP) for visualization, with 30 computed PCs as input.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat, Signac v1.12.0]

### Temporal BMP4 effects on mouse embryonic and extraembryonic development. (Nature 2024)

- DOI: 10.1038/s41586-024-07937-5 | PMCID: PMC11485214 | PMID: 39294373
- Evidence: SpA-TGC, spiral artery TGC; p-TGC, parietal TGC. b , UMAP (uniform manifold approximation and projection) of all embryonic and extraembryonic endoderm cells ( n = 57,555 cells, excluding parietal endoderm).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [ImageJ, scDblFinder]

### Connectome-constrained networks predict neural activity across the fly visual system. (Nature 2024)

- DOI: 10.1038/s41586-024-07939-3 | PMCID: PMC11525180 | PMID: 39261740
- Evidence: Next, we computed a nonlinear dimensionality reduction to two dimensions using the UMAP (uniform manifold approximation and projection) algorithm, and fitted Gaussian mixtures of 2 to 5 components, with the number of components that minimize the Bayesian information criterion, using the Python libraries umap-learn and scikit-learn 38 , 74 .
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [UMAP, scikit-learn] -> simulation/modelling [PyTorch] -> machine learning [PyTorch]

### DNA methylation controls stemness of astrocytes in health and ischaemia. (Nature 2024)

- DOI: 10.1038/s41586-024-07898-9 | PMCID: PMC11464379 | PMID: 39232166
- Evidence: Specifically, after normalizing and finding 3,000 highly variable genes using default Seurat parameters for both datasets, we used FindIntegrationAnchors and IntegrateData using 30 dimensions to integrate the datasets, followed by scaling, principal component analysis (PCA) and UMAP on 30 principal components.
- Full pipeline: read trimming [Bismark v0.22.3, Trim Galore v0.4.4] -> alignment/mapping [Bismark v0.22.3, STAR v2.7.3a, Trim Galore v0.4.4] -> quantification [R] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> visualisation [ComplexHeatmap v2.12.0, tidyverse v1.3.1] -> stage not stated [BEDTools v2.30.0, Cellpose v2.2.2, HOMER v4.4]

### Global marine microbial diversity and its potential in bioprospecting. (Nature 2024)

- DOI: 10.1038/s41586-024-07891-2 | PMCID: PMC11390488 | PMID: 39232160
- Evidence: Here we introduce the implementation of uniform manifold approximation and projection (UMAP) to unveil biogeographic patterns within marine microbiomes 11 (Supplementary Note 1 ).
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.407, MUSCLE v3.8.31] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [AlphaFold v2.3.0, InterProScan v5.0, Prokka v1.14.6, R, ggplot2 v3.5.1]

### Spatially clustered type I interferon responses at injury borderzones. (Nature 2024)

- DOI: 10.1038/s41586-024-07806-1 | PMCID: PMC11374671 | PMID: 39198639
- Evidence: Cells from infarcted Irf3 −/− mice were ingested or embedded into the UMAP space of the annotated cells in WT mice we used as reference.
- Full pipeline: quality control [Scanpy, Squidpy] -> normalisation [ImageJ, Scanpy, Seurat, Squidpy] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose, R, SoupX]

### Sympathetic neuropeptide Y protects from obesity by sustaining thermogenic fat. (Nature 2024)

- DOI: 10.1038/s41586-024-07863-6 | PMCID: PMC11446830 | PMID: 39198648
- Evidence: Data were then scaled using ‘ScaleData()’, and linear dimensional reduction performed by principal component analysis and calculation of UMAP coordinates for all cells using Seurat v.4.2.0.
- Full pipeline: normalisation [Seurat v4.2.0, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.2.2]

### Fate induction in CD8 CAR T cells through asymmetric cell division. (Nature 2024)

- DOI: 10.1038/s41586-024-07862-7 | PMCID: PMC11410665 | PMID: 39198645
- Evidence: Dimensionality reduction of antibody-derived sequencing data with uniform manifold approximation and projection (UMAP) demonstrates separation of resting from activated CARTs before the first cell division (Fig.
- Full pipeline: alignment/mapping [velocyto] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ, Python v3.10.4, R, SCENIC v0.11.2, Seurat, scVelo]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Evidence: Data was visualized using UMAP in SCANPY, and clustering was done using the Leiden algorithm (with a resolution setting of 0.5).
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Human organoids with an autologous tissue-resident immune compartment. (Nature 2024)

- DOI: 10.1038/s41586-024-07791-5 | PMCID: PMC11374719 | PMID: 39143209
- Evidence: The first 30 principal component vectors of the new PCA space served as the basis for obtaining a two-dimensional representation of the data through UMAP 69 implemented in RunUMAP() with the 50 nearest neighbours.
- Full pipeline: quality control [R] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [CellChat, CellProfiler v4.2.5, ImageJ v1.54i, Python v3.7, scDblFinder, scVelo]

### In vivo interaction screening reveals liver-derived constraints to metastasis. (Nature 2024)

- DOI: 10.1038/s41586-024-07715-3 | PMCID: PMC11306111 | PMID: 39048831
- Evidence: Clustering and UMAP visualization were performed using ten principal components and a resolution of 0.2 for the shared nearest-neighbour clustering algorithm.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [Bowtie2] -> quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ImageJ, UMAP, ggplot2] -> stage not stated [Bioconductor, CellPhoneDB, Cellpose, Enrichr, GSEA, R v4.1.0, Seurat, Signac, fgsea]

### Neoantigen-specific cytotoxic Tr1 CD4 T cells suppress cancer immunotherapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07752-y | PMCID: PMC11291290 | PMID: 39048822
- Evidence: Each mouse was treated with 25,000 IU in PBS injected intraperitoneally daily for 5 days. scRNA-seq analysis UMAP clustering and separation of total and antigen-specific cells T3 tumour-bearing mice were treated with HDVax, LDVax or PBS 6 days post-tumour transplantation.
- Full pipeline: normalisation [DESeq2 v1.30.1, limma] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [limma] -> stage not stated [R, Seurat, fgsea]

### Single-cell multiregion dissection of Alzheimer's disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07606-7 | PMCID: PMC11338834 | PMID: 39048816
- Evidence: We further filtered the dataset to the top 5,000 most variable genes and used them to calculate the low dimensional embedding of the cells (UMAP) (default parameters, using 50 principal components and 15 nearest neighbours) and clusters using the Leiden clustering algorithm at a high resolution (15), giving 337 preliminary clusters 87 .
- Full pipeline: alignment/mapping [Seurat] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Seurat, UMAP, edgeR, scDblFinder] -> differential/statistical testing [DESeq2, R, edgeR, emmeans, lme4] -> visualisation [DESeq2, Seurat] -> stage not stated [CellPhoneDB, MAGMA, SCENIC, ggplot2]

### Neural circuit basis of placebo pain relief. (Nature 2024)

- DOI: 10.1038/s41586-024-07816-z | PMCID: PMC11358037 | PMID: 39048016
- Evidence: D, dorsal; L, lateral. b , Pn neurons in low-dimensional uniform manifold approximation and projection (UMAP) space, colour coded by cluster.
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, UMAP] -> differential/statistical testing [Seurat v4.0] -> stage not stated [DeepLabCut, ImageJ, R]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: UMAP dimensional reduction technique was used to visualize the data in two dimensions.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Brainstem Dbh&lt;sup&gt;+&lt;/sup&gt; neurons control allergen-induced airway hyperreactivity. (Nature 2024)

- DOI: 10.1038/s41586-024-07608-5 | PMCID: PMC11254774 | PMID: 38987587
- Evidence: The R package Seurat (v4.0) 29 was then used to perform data quality control, normalization, principal components analysis, UMAP generation and differential gene expression testing.
- Full pipeline: quality control [R, Seurat v4.0, UMAP] -> normalisation [R, Seurat v4.0, UMAP, scDblFinder v2.0] -> dimensionality reduction/clustering [R, Seurat v4.0, UMAP, ggplot2 v3.3.2, tidyverse] -> differential/statistical testing [R, Seurat v4.0, UMAP] -> visualisation [ggplot2 v3.3.2, tidyverse]

### Plasmacytoid dendritic cells control homeostasis of megakaryopoiesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07671-y | PMCID: PMC11254756 | PMID: 38987596
- Evidence: GO analysis revealed upregulated genes (false-discovery rate (FDR) < 0.05) associated with terms for transcription and translation (top five terms). e , UMAP plot of scRNA-seq data (sorted CD41 + CD42 − CD9 + KIT + progenitors).
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [Monocle] -> stage not stated [DESeq2 v1.30.0, GSEA, Seurat]

### A liver immune rheostat regulates CD8 T cell immunity in chronic HBV infection. (Nature 2024)

- DOI: 10.1038/s41586-024-07630-7 | PMCID: PMC11269190 | PMID: 38987588
- Evidence: Cells were clustered using the Louvain method, UMAP projection and DEA were carried out using Seurat v.3.2.0.
- Full pipeline: quality control [Seurat] -> read trimming [Trimmomatic v0.36] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape v3.7.1, ggplot2] -> stage not stated [DESeq2, GSEA, QuPath v0.2.3, R, SCENIC, STAR v2.5.3a, igraph]

### A maternal brain hormone that builds bone. (Nature 2024)

- DOI: 10.1038/s41586-024-07634-3 | PMCID: PMC11306098 | PMID: 38987585
- Evidence: Principal component (PC) ‘elbow’ heuristics were used to determine the number of PCs for clustering analysis with UMAP and Leiden algorithm (leidenalg).
- Full pipeline: read trimming [RSEM v1.2.21, STAR v2.4] -> alignment/mapping [RSEM v1.2.21, STAR v2.4, kallisto] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Scanpy v1.9, scDblFinder]

### Single-cell atlas of the human brain vasculature across development, adulthood and disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07493-y | PMCID: PMC11324530 | PMID: 38987604
- Evidence: ECM, extracellular matrix; NVL, neurovascular link; periph., periphery; RPCA, reciprocal principal component analysis; UMAP, uniform manifold approximation and projection.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> stage not stated [Seurat]

### The cortical amygdala consolidates a socially transmitted long-term memory. (Nature 2024)

- DOI: 10.1038/s41586-024-07632-5 | PMCID: PMC11306109 | PMID: 38961294
- Evidence: Cells were visualized using UMAP.
- Full pipeline: alignment/mapping [STAR v2.7.10a, Seurat] -> quantification [ImageJ] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Cellpose, R v4.2.2, featureCounts v2.0.0]

### Adenosine signalling to astrocytes coordinates brain metabolism and function. (Nature 2024)

- DOI: 10.1038/s41586-024-07611-w | PMCID: PMC11291286 | PMID: 38961289
- Evidence: Uniform manifold approximation and projection (UMAP) was used to visualize the cell clusters in two dimensions based on the same 75 principal components used for clustering and yielded 63 distinct cell clusters.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ImageJ, R v4.2.2, Seurat, UMAP] -> stage not stated [Fiji]

### Multiscale topology classifies cells in subcellular spatial transcriptomics. (Nature 2024)

- DOI: 10.1038/s41586-024-07563-1 | PMCID: PMC11208150 | PMID: 38898271
- Evidence: Visualizations of the annotated snRNA-seq dataset in the form of UMAP and violin plots are available in Extended Data Figs.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [SciPy] -> visualisation [UMAP] -> stage not stated [MACS2]

### Human SARS-CoV-2 challenge uncovers local and systemic response dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07575-x | PMCID: PMC11222146 | PMID: 38898278
- Evidence: Clustering and cell-type annotation Principal component analysis was run on corrected gene expression counts from selected hypervariable genes, and the first 30 principal components were selected to construct a nearest neighbour graph and UMAP embedding.
- Full pipeline: alignment/mapping [Seurat v4.1.0] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, Python, R, Scanpy, SoupX, lme4]

### The Space Omics and Medical Atlas (SOMA) and international astronaut biobank. (Nature 2024)

- DOI: 10.1038/s41586-024-07639-y | PMCID: PMC11357981 | PMID: 38862028
- Evidence: ( b ) UMAP projection of the ROIs.
- Full pipeline: quality control [Seurat] -> quantification [Enrichr] -> normalisation [NumPy, featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.36.0, GSEA, R, edgeR, limma]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: PCA and UMAP clustering was performed and clusters annotated using established markers and/or previous literature.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Myelin plasticity in the ventral tegmental area is required for opioid reward. (Nature 2024)

- DOI: 10.1038/s41586-024-07525-7 | PMCID: PMC11186775 | PMID: 38839962
- Evidence: UMAP was conducted using the first 12 principal components and graph-based clustering was used to identify clusters with a resolution parameter of 0.8.
- Full pipeline: dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [Seurat v4.3.0] -> stage not stated [CellChat v1.6.1]

### MYCT1 controls environmental sensing in human haematopoietic stem cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07478-x | PMCID: PMC11168926 | PMID: 38839950
- Evidence: Principal component analysis, t-SNE and UMAP were used to reduce the dimensions of the data.
- Full pipeline: quantification [Bioconductor] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.26.0] -> stage not stated [AlphaFold, GSEA, R, Seurat v3.1.2]

### Epigenetic inheritance of diet-induced and sperm-borne mitochondrial RNAs. (Nature 2024)

- DOI: 10.1038/s41586-024-07472-3 | PMCID: PMC11186758 | PMID: 38839949
- Evidence: ( i - j ) UMAP representation (i) and cluster annotation (j - based on publicly available datasets 64 - GSE112393 ) of single-cell RNA-seq analysis of testes from LFD and HFD-fed mice (n = 3).
- Full pipeline: quality control [MultiQC v1.11] -> read trimming [Cutadapt v2.8, featureCounts] -> alignment/mapping [SAMtools, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, R, UMAP] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> visualisation [ComplexHeatmap] -> stage not stated [Bioconductor v3.14, Enrichr, Seurat]

### Acquisition of epithelial plasticity in human chronic liver disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07465-2 | PMCID: PMC11153150 | PMID: 38778114
- Evidence: UMAP projections were calculated using ‘RunUMAP(n.neighbors = 20, min.dist = 0.3)’.
- Full pipeline: quality control [Seurat v4.0.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [velocyto v0.17.17]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Evidence: Data scaling, PCA, construction of a shared nearest neighbour graph, identification of clusters and dimensional reduction by UMAP were done using the ScaleData, RunPCA, FindNeighbors, FindClusters and runUMAP functions, respectively.
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Multimodal decoding of human liver regeneration. (Nature 2024)

- DOI: 10.1038/s41586-024-07376-2 | PMCID: PMC11153152 | PMID: 38693268
- Evidence: ECM, extracellular matrix; NR, necrotic region. k , UMAP of cell lineage inferred using signatures of known lineage markers (Supplementary Table 2 ).
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [CellChat, Cellpose, ImageJ, QuPath v0.3.0, R, Scanpy, StarDist]

### A body-brain circuit that regulates body inflammatory responses. (Nature 2024)

- DOI: 10.1038/s41586-024-07469-y | PMCID: PMC11186780 | PMID: 38692285
- Evidence: A uniform manifold approximation and projection (UMAP) plot of transcriptomic data reveals 14 glutamatergic neuronal clusters (1–14, in colour) and 6 GABAergic clusters (15–20, in grey). b , scRNA-seq of individual LPS-TRAPed neurons from the cNST.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### PGE&lt;sub&gt;2&lt;/sub&gt; inhibits TIL expansion by disrupting IL-2 signalling and mitochondrial function. (Nature 2024)

- DOI: 10.1038/s41586-024-07352-w | PMCID: PMC11078736 | PMID: 38658764
- Evidence: Based on the metaclustering results, separation between the COXi-treated and control TILs was visualized the using UMAP.
- Full pipeline: alignment/mapping [IMOD, STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma v3.54.0] -> visualisation [UMAP] -> stage not stated [GSEA, GSVA v1.44.5, HTSeq v0.9.1, ImageJ, R]

### Spatiotemporally resolved colorectal oncogenesis in mini-colons ex vivo. (Nature 2024)

- DOI: 10.1038/s41586-024-07330-2 | PMCID: PMC11078756 | PMID: 38658753
- Evidence: The data were log-normalized and scaled, and dimensionality reduction was conducted using UMAP with 10 dimensions.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.9] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [BWA v0.7.17, Cytoscape, SAMtools v1.9] -> stage not stated [GSEA, ImageJ, MACS2, Seurat v4.2.0, StarDist, edgeR]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Evidence: Significant principal components ( n = 30) were identified and used to generate a uniform manifold approximation and projection (UMAP) for dimensional reduction.
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### PGE&lt;sub&gt;2&lt;/sub&gt; limits effector expansion of tumour-infiltrating stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07254-x | PMCID: PMC11078747 | PMID: 38658748
- Evidence: PCA was calculated for the integrated data on the top 1,000 highly variable genes and both k -nearest neighbour graph and UMAP were computed on the 30 nearest neighbours and first 20 PCA dimensions.
- Full pipeline: alignment/mapping [deepTools v3.5.4, featureCounts v1.5.0] -> quantification [featureCounts v1.5.0] -> normalisation [deepTools v3.5.4] -> dimensionality reduction/clustering [SAMtools v1.13, UMAP, ggplot2 v3.4.2, igraph v1.3.2] -> visualisation [ggplot2 v3.4.2] -> stage not stated [DESeq2 v1.36, GSEA v4.3.2, R v4.0.4, Seurat v4.0.1]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Evidence: In brief, myonuclei data were subjected to SCTransform-based normalization, anchor identification between samples, integration, Louvain clustering and projection onto the UMAP space.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: The integrated dataset was scaled, and UMAP dimensionality reduction was performed using the top 30 principal components.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### Distal colonocytes targeted by C. rodentium recruit T-cell help for barrier defence. (Nature 2024)

- DOI: 10.1038/s41586-024-07288-1 | PMCID: PMC11096101 | PMID: 38600382
- Evidence: The clusters were visualized in two dimensions with UMAP.
- Full pipeline: quality control [QIIME 2] -> alignment/mapping [QIIME 2] -> dimensionality reduction/clustering [AnnData, UMAP, velocyto v0.17.16] -> differential/statistical testing [ComplexHeatmap v2.11.1] -> simulation/modelling [AnnData, Scanpy v1.6.1, scVelo, velocyto v0.17.16] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5] -> stage not stated [Python, R, Seurat, fgsea]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Evidence: The single-cell signature explorer program was utilized for visualization of gene signatures across UMAP plots 58 .
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### Immune microniches shape intestinal T&lt;sub&gt;reg&lt;/sub&gt; function. (Nature 2024)

- DOI: 10.1038/s41586-024-07251-0 | PMCID: PMC11041794 | PMID: 38570678
- Evidence: The function scvelo.pl.velocity_embedding_stream was used to project the velocity information onto the UMAP.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> visualisation [R] -> stage not stated [CellPhoneDB, NumPy v1.20.1, SoupX, pandas v1.2.3, scDblFinder, scVelo v0.2.4, velocyto]

### Single-cell multiplex chromatin and RNA interactions in ageing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07239-w | PMCID: PMC11023937 | PMID: 38538789
- Evidence: Single-cell clustering and cell type identification The integrated brain object was then subjected to dimensionality reduction by UMAP methods based on the first 20 principal components from PCA using the Seurat R package.
- Full pipeline: alignment/mapping [Bowtie2 v5.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Docker, Harmony v0.1.1, R, Seurat v4.3.0, Snakemake]

### Formation of memory assemblies through the DNA-sensing TLR9 pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07220-7 | PMCID: PMC10990941 | PMID: 38538785
- Evidence: 6 ). d , Dcx expression superimposed on uniform manifold approximation and projection (UMAP) analysis of snRNA-seq data from dorsal hippocampal cells.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> alignment/mapping [SAMtools, STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, fgsea v1.20.0] -> stage not stated [Fiji, R, SoupX v1.6.2, scDblFinder v1.13.13]

### Mitochondrial complex I activity in microglia sustains neuroinflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07167-9 | PMCID: PMC10990929 | PMID: 38480879
- Evidence: UMAP dimensionality reduction was performed using the CATALYST wrapper around scater runUMAP with the default parameters and data from cell-surface features only.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> quantification [featureCounts v1.6.3, scVelo v0.2.5, velocyto v0.17.17] -> normalisation [scVelo v0.2.5, velocyto v0.17.17] -> dimensionality reduction/clustering [R v4.2.3, UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, MACS2, Seurat v4.3.0.1, edgeR]

### APOE4/4 is linked to damaging lipid droplets in Alzheimer's disease microglia. (Nature 2024)

- DOI: 10.1038/s41586-024-07185-7 | PMCID: PMC10990924 | PMID: 38480892
- Evidence: We then used the batch-corrected neighbourhood graph to run Leiden clustering 46 and to calculate a global UMAP embedding with default parameters in Scanpy (v.1.9.1).
- Full pipeline: alignment/mapping [HOMER, STAR v2.5.1b] -> quantification [Fiji, ImageJ] -> normalisation [R v4.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, ImageJ, R v4.3, Seurat] -> stage not stated [Bowtie2, MACS2, Python v3.9.12, Scanpy, scDblFinder v0.2.3]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Evidence: To this end, we reduced the scRNA-seq dataset to only the 238 genes in the MERFISH gene panel and then performed dimensionality reduction, graph-based clustering and UMAP visualization.
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### Subicular neurons encode concave and convex geometries. (Nature 2024)

- DOI: 10.1038/s41586-024-07139-z | PMCID: PMC10972755 | PMID: 38448584
- Evidence: Next, we selected the top ten principal components from the PCA results to carry out Uniform Manifold Approximation and Projection (UMAP), reducing the ten principal components into a 3D visualization.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### A vagal reflex evoked by airway closure. (Nature 2024)

- DOI: 10.1038/s41586-024-07144-2 | PMCID: PMC10972749 | PMID: 38448588
- Evidence: Transformed matrices from both strains were integrated (nFeature = 3,000) before cluster identification and UMAP representation.
- Full pipeline: quality control [R v4.1.3, Seurat v4.1.1] -> alignment/mapping [R v4.1.3, Seurat v4.1.1] -> normalisation [R v4.1.3, Seurat v4.1.1] -> dimensionality reduction/clustering [R v4.1.3, Seurat v4.1.1, UMAP] -> differential/statistical testing [Enrichr, R v4.1.3, Seurat v4.1.1] -> stage not stated [Fiji v1.52p, ImageJ v1.52p]

### A concerted neuron-astrocyte program declines in ageing and schizophrenia. (Nature 2024)

- DOI: 10.1038/s41586-024-07109-5 | PMCID: PMC10954558 | PMID: 38448582
- Evidence: Lachner (laboratory tools) and pnx (brain exterior side view) under a Creative Commons licence CC0 1.0 . b , Uniform manifold approximation and projection (UMAP; coloured by donor) analysis of the RNA-expression profiles of 1,217,965 nuclei analysed from 191 donors. c , Assignments of nuclei to cell types (same projection as in b ). d , e , Assignments of nuclei to glutamatergic ( n = 524,186) ( d...
- Full pipeline: read trimming [Bowtie2 v2.2.4, Trimmomatic v0.33] -> alignment/mapping [Bowtie2 v2.2.4, SAMtools v1.3.1] -> dimensionality reduction/clustering [ComplexHeatmap v2.10.0, UMAP, data.table v1.14.8, ggplot2 v3.4.2, tidyverse v1.1.2] -> differential/statistical testing [LDSC, MAGMA] -> stage not stated [AnnData v0.8.0, BCFtools v1.16, FUMA v1.5.6, GSEA, Matplotlib v3.5.2, NumPy v1.17.5, SCENIC, SHAPEIT, Scanpy v1.9.1, Seurat v3.2.2, WGCNA, ggpubr v0.5.0, lme4 v1.1, pandas v1.0.5, pheatmap v1.0.12, seaborn v0.10.1]

### An atlas of epithelial cell states and plasticity in lung adenocarcinoma. (Nature 2024)

- DOI: 10.1038/s41586-024-07113-9 | PMCID: PMC10954546 | PMID: 38418883
- Evidence: Dimensionality reduction and 2D visualization of cell clusters was performed using UMAP 45 and the Seurat function RunUMAP.
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [R] -> simulation/modelling [Monocle] -> visualisation [Scanpy v1.9.1, UMAP] -> stage not stated [ImageJ, Mutect2, SAMtools v1.15, Seurat, Slingshot, ggplot2 v3.2.0, pheatmap v1.0.12, scDblFinder]

### Crym-positive striatal astrocytes gate perseverative behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07138-0 | PMCID: PMC10937394 | PMID: 38418885
- Evidence: Uniform manifold approximation and projection (UMAP) of 39,156 cells from the striatum shows cell classes, including astrocytes.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, limma] -> visualisation [Cytoscape v3.8, R v4.0.3, Seurat] -> stage not stated [Enrichr, ImageJ, STRING db, WGCNA, scDblFinder]

### Anti-TIGIT antibody improves PD-L1 blockade through myeloid and T&lt;sub&gt;reg&lt;/sub&gt; cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07121-9 | PMCID: PMC11139643 | PMID: 38418879
- Evidence: A UMAP was generated using the RunUMAP function.
- Full pipeline: alignment/mapping [Bioconductor, R] -> quantification [Bioconductor, R] -> normalisation [Harmony v1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [fgsea] -> stage not stated [Seurat]

### Multisensory gamma stimulation promotes glymphatic clearance of amyloid. (Nature 2024)

- DOI: 10.1038/s41586-024-07132-6 | PMCID: PMC10917684 | PMID: 38418876
- Evidence: The first 30 principal components were used for non-linear dimensionality reduction (UMAP) for visualization.
- Full pipeline: alignment/mapping [Suite2p] -> quantification [ImageJ] -> normalisation [ImageJ] -> registration [Suite2p] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> visualisation [UMAP] -> stage not stated [Seurat v4.0.3, scDblFinder]

### Genomic data in the All of Us Research Program. (Nature 2024)

- DOI: 10.1038/s41586-023-06957-x | PMCID: PMC10937371 | PMID: 38374255
- Evidence: 2 Genetic ancestry in All of Us. a , b , Uniform manifold approximation and projection (UMAP) representations of All of Us WGS PCA data with self-described race ( a ) and ethnicity ( b ) labels. c , Proportion of genetic ancestry per individual in six distinct and coherent ancestry groups defined by Human Genome Diversity Project and 1000 Genomes samples.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [REGENIE] -> stage not stated [Picard]

### B cells orchestrate tolerance to the neuromyelitis optica autoantigen AQP4. (Nature 2024)

- DOI: 10.1038/s41586-024-07079-8 | PMCID: PMC10937377 | PMID: 38383779
- Evidence: Clustering was performed using the Leiden algorithm (leidenalg package, v.0.9.1) with a resolution of r = 0.7 and UMAP dimensionality reduction was computed using the default SCANPY settings.
- Full pipeline: alignment/mapping [velocyto v0.17.17] -> normalisation [DESeq2, GSEA v4.3.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> simulation/modelling [scVelo v0.2.5, velocyto v0.17.17] -> stage not stated [MACS2, QuPath v0.3.2]

### IL-10 constrains sphingolipid metabolism to limit inflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07098-5 | PMCID: PMC10954550 | PMID: 38383790
- Evidence: Mann–Whitney t -test. d , Total macrophages (CD11c + MHCII + ) and CD64 + macrophages from colonic lamina propria from wild-type and Cers2- KO chimeric mice ( n = 4–5). e , UMAP analysis of single-cell RNA-seq (scRNA-seq) data from Il10rb -KO and Il10rb / Cers2 -DKO macrophage clusters in cells sorted from the colon lamina propria. f , UMAP analysis of Cxcl2 and Il6 scRNA-seq data from sorted macr...
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [HTSeq, Picard] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat v4.3.0]

### A model of human neural networks reveals NPTX2 pathology in ALS and FTLD. (Nature 2024)

- DOI: 10.1038/s41586-024-07042-7 | PMCID: PMC10901740 | PMID: 38355792
- Evidence: The UMAP 75 cell embeddings were computed from the top 20 principal components.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [STAR v2.7.7a] -> quantification [ilastik] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.36.0] -> machine learning [ilastik] -> stage not stated [ImageJ, Python v3.6.10, R, SpikeInterface, scDblFinder, tidyverse]

### A single-cell time-lapse of mouse prenatal development from gastrula to birth. (Nature 2024)

- DOI: 10.1038/s41586-024-07069-w | PMCID: PMC10901739 | PMID: 38355799
- Evidence: (3) The dimensionality of the data was reduced by PCA (50 components) first on the top 5,000 most highly dispersed genes and then with UMAP (max_components = 2, n_neighbors = 50, min_dist = 0.1, metric = ‘cosine’) using Monocle 3-alpha 14 .
- Full pipeline: read trimming [STAR v2.6.1d, Trim Galore] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [Monocle, Scanpy v1.6.0, UMAP] -> differential/statistical testing [Seurat] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, Python, scDblFinder]

### Autonomous transposons tune their sequences to ensure somatic suppression. (Nature 2024)

- DOI: 10.1038/s41586-024-07081-0 | PMCID: PMC10901741 | PMID: 38355802
- Evidence: UMAP of FLASH data For construction of the UMAP, peak calling was carried out on all profiles using HOMER: findPeaks {tag_directory} -style factor -strand separate -o {peaks.txt} -i {background_tag_directory}.
- Full pipeline: read trimming [Cutadapt v4.1, STAR v2.7.9a] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.7.9a, featureCounts v2.0.1] -> quantification [DESeq2] -> normalisation [Jupyter, scikit-learn] -> dimensionality reduction/clustering [HOMER, Jupyter, UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R] -> visualisation [Jupyter, scikit-learn]

### Circulating myeloid-derived MMP8 in stress susceptibility and depression. (Nature 2024)

- DOI: 10.1038/s41586-023-07015-2 | PMCID: PMC10901735 | PMID: 38326622
- Evidence: The optimal number of principal components to be used for dimensional reduction using UMAP was determined using ElbowPlot.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, HTSeq v0.12.4, STAR v2.5] -> quantification [ImageJ, Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [R]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: A uniform manifold approximation and projection (UMAP) on the top 12 principal components was used for dimensional reduction and data visualization.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Deciphering cell states and genealogies of human haematopoiesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07066-z | PMCID: PMC10937407 | PMID: 38253266
- Evidence: Subpopulations were visualized on RNA-, ATAC- and WNN-based UMAP.
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP]

### Autoreactive T cells target peripheral nerves in Guillain-Barré syndrome. (Nature 2024)

- DOI: 10.1038/s41586-023-06916-6 | PMCID: PMC10830418 | PMID: 38233524
- Evidence: 2 scRNA-seq analysis of memory CD4 + T cells from patients with GBS. a , Uniform manifold approximation and projection (UMAP) and dot plots describing the average expression levels of activation and proliferation genes in CD4 + memory T cells from patients with GBS after in vitro stimulation with PNS-myelin antigens or influenza vaccine (Flu).
- Full pipeline: quality control [Seurat v4.9.9.9059] -> normalisation [Seurat v4.9.9.9059] -> dimensionality reduction/clustering [Seurat v4.9.9.9059, UMAP] -> stage not stated [R]

### Nasopharyngeal lymphatic plexus is a hub for cerebrospinal fluid drainage. (Nature 2024)

- DOI: 10.1038/s41586-023-06899-4 | PMCID: PMC10808075 | PMID: 38200313
- Evidence: For visualization in two-dimensional space, principal component analysis was performed, and the top 15 principal components were used as the input for UMAP analysis.
- Full pipeline: read trimming [STAR v2.7.9] -> alignment/mapping [STAR v2.7.9] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [R, Seurat, UMAP] -> stage not stated [ImageJ]

### Elevated genetic risk for multiple sclerosis emerged in steppe pastoralist populations. (Nature 2024)

- DOI: 10.1038/s41586-023-06618-z | PMCID: PMC10781639 | PMID: 38200296
- Evidence: PCA and UMAP of WAP and average dosage To sort risk-associated SNPs into ancestry patterns according to that risk, we performed PCA on the average ancestry probability and WAP at each MS-associated SNP (Supplementary Fig.
- Full pipeline: quality control [ANGSD v0.931] -> alignment/mapping [BWA v0.7.17] -> quantification [ANGSD v0.931] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [PLINK, Picard, R, SAMtools v1.10]

### MRE11 liberates cGAS from nucleosome sequestration during tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-023-06889-6 | PMCID: PMC10794148 | PMID: 38200309
- Evidence: Uniform manifold approximation and projection (UMAP) analyses revealed a region where sgControl cells were more abundant than sg Mre11 cells (Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Seurat v3.1.2]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Evidence: Cells were clustered using combined accessibility and gene expression data by weighted nearest neighbours analysis 18 and visualized by UMAP projection.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### Minute-scale oscillatory sequences in medial entorhinal cortex. (Nature 2024)

- DOI: 10.1038/s41586-023-06864-1 | PMCID: PMC10781645 | PMID: 38123682
- Evidence: To take into account potential non-linearities, four additional sorting methods were implemented, based on the following non-linear dimensionality reduction techniques 63 : t -distributed stochastic neighbour embedding ( t -SNE), LEM, Isomap and uniform manifold approximation and projection (UMAP) 64 (see parameters below).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python] -> stage not stated [Kilosort v2.5, Suite2p]

### Modelling post-implantation human development to yolk sac blood emergence. (Nature 2024)

- DOI: 10.1038/s41586-023-06914-8 | PMCID: PMC10849971 | PMID: 38092041
- Evidence: Visualization was achieved by the use of uniform manifold approximation and projection (UMAP) plots identifying cells, clusters and selected gene expression in each cell, as well as heatmaps and violin plots showing the expression level of genes by cluster.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellProfiler, Enrichr, Fiji, ImageJ, Seurat]

### Slide-tags enables single-nucleus barcoding for multimodal spatial genomics. (Nature 2024)

- DOI: 10.1038/s41586-023-06837-4 | PMCID: PMC10764288 | PMID: 38093010
- Evidence: The diagram was created using BioRender. b , UMAP embedding of snRNA-seq profiles coloured by cell type annotations. mDC, myeloid dendritic cells; pDC, plasmacytoid dendritic cells; T FH cells, T follicular helper cells. c , Spatial mapping of snRNA-seq profiles, coloured by cell type as in b . d , Adjacent haematoxylin and eosin (H&E)-stained section of the profiled region. e , Magnified view of ...
- Full pipeline: quality control [Seurat v4.3.0] -> alignment/mapping [RSEM, UMAP] -> quantification [RSEM] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [Enrichr] -> stage not stated [ArchR, MACS2 v2.2.7.1, R v4.2.2, Signac v1.9.0]

### Targeted design of synthetic enhancers for selected tissues in the Drosophila embryo. (Nature 2024)

- DOI: 10.1038/s41586-023-06905-9 | PMCID: PMC10830412 | PMID: 38086418
- Evidence: Bottom: UMAP visualization of cell-x-peak accessibility matrix of cells with inferred age between 10 and 12 h, colored and labeled by tissue annotation.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Keras, TensorFlow v1.14.0] -> visualisation [R, UMAP] -> stage not stated [BEDTools, MACS2, ggplot2 v3.2.1]

### Dictionary of immune responses to cytokines at single-cell resolution. (Nature 2024)

- DOI: 10.1038/s41586-023-06816-9 | PMCID: PMC10781646 | PMID: 38057668
- Evidence: We then performed PCA and visualized the cells using UMAP 48 .
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.1] -> visualisation [UMAP] -> stage not stated [MACS2, R, Seurat]

### A human embryonic limb cell atlas resolved in space and time. (Nature 2024)

- DOI: 10.1038/s41586-023-06806-x | PMCID: PMC7616500 | PMID: 38057666
- Evidence: Following this, further dimension reduction was performed using uniform manifold approximation and projection (UMAP) (scanpy tl.umap with default parameters) based on the corrected neighbourhood graph of bbknn.
- Full pipeline: alignment/mapping [STAR v2.5.1b] -> quantification [STAR v2.5.1b, scVelo v0.24] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Scanpy] -> structure determination [AnnData] -> machine learning [ilastik] -> stage not stated [CellPhoneDB, PHENIX, SCENIC, scDblFinder]

### Hypoblast from human pluripotent stem cells regulates epiblast development. (Nature 2024)

- DOI: 10.1038/s41586-023-06871-2 | PMCID: PMC10849967 | PMID: 38052228
- Evidence: We generated an integrated uniform manifold approximation and projection (UMAP), as proposed previously 43 , which clustered each cell type of the embryos as hypoblast, epiblast, primitive streak, mesoderm, amnion, primordial germ cells (PGCs), extraembryonic mesoderm, TB and ICM (Fig.
- Full pipeline: quality control [Seurat] -> read trimming [Cutadapt v1.15, TopHat] -> alignment/mapping [RSEM v1.3.1, STAR, TopHat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat]

### The genetic legacy of the expansion of Bantu-speaking peoples in Africa. (Nature 2024)

- DOI: 10.1038/s41586-023-06770-6 | PMCID: PMC10794141 | PMID: 38030719
- Evidence: We first used the uniform manifold approximation and projection (UMAP) approach 52 directly on the genotype data.
- Full pipeline: quality control [PLINK v1.90b] -> variant calling [PLINK v1.90b, SHAPEIT, UMAP] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [Python, R]

### Cellular development and evolution of the mammalian cerebellum. (Nature 2024)

- DOI: 10.1038/s41586-023-06884-x | PMCID: PMC10808058 | PMID: 38029793
- Evidence: MB, midbrain; N/A, not available. c , Uniform manifold approximation and projection (UMAP) of 115,282 mouse, 180,956 human and 99,498 opossum cells coloured by cell type.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [SCENIC]

### Repeated Omicron exposures override ancestral SARS-CoV-2 immune imprinting. (Nature 2024)

- DOI: 10.1038/s41586-023-06753-7 | PMCID: PMC10764275 | PMID: 37993710
- Evidence: To project the dataset onto a 2D space for visualization, we performed UMAP based on the constructed k -nearest-neighbour graph using umap-learn module (v0.5.2).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [R, UMAP, ggplot2 v3.3.3] -> stage not stated [SciPy, igraph]

### Anti-progestin therapy targets hallmarks of breast cancer risk. (Nature 2025)

- DOI: 10.1038/s41586-025-09684-7 | PMCID: PMC12711567 | PMID: 41193807
- Evidence: Scater (v1.18.6) was used to generate both principal component analysis and UMAP dimensionality reduction coordinates, with a minimum distance of 0.1 and nearest neighbours of 30 cells.
- Full pipeline: alignment/mapping [Nextflow v19.10.0] -> quantification [clusterProfiler v4.6.0] -> dimensionality reduction/clustering [ComplexHeatmap v2.16.0, R, Scanpy, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [CellChat, DESeq2 v1.26.0, clusterProfiler v4.6.0, ggpubr] -> stage not stated [Python, igraph v1.2.6]

### Lineage-resolved atlas of the developing human cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-09033-8 | PMCID: PMC12589122 | PMID: 41193842
- Evidence: Libraries were integrated using Harmony v0.1.1 77 , and Seurat was used to identify clusters and perform UMAP dimensional reduction.
- Full pipeline: dimensionality reduction/clustering [Harmony, UMAP] -> stage not stated [Seurat v4.3.0.9002]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Evidence: Thirty-nine principal components were used to calculate the UMAP embedding and perform clustering analysis using the Louvain algorithm with a resolution of 2.4.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Evidence: ...ltiome nuclei, age distribution of scRNA-seq cells, age distribution of Multiome nuclei and number of scRNA-seq subclusters for each cluster. c – i , UMAP representations of all cell types coloured by class ( c ), subclass ( d ), cluster ( e ), subcluster ( f ), age ( g ), synchronized age ( h ) and pseudotime ( i ). j , Constellation plot showing the UMAP centroids of subcluster nodes coloured by...
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### Conservation and alteration of mammalian striatal interneurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09592-w | PMCID: PMC12589139 | PMID: 41193841
- Evidence: UMAP coloured by striatal inhibitory neuron terminal classes in adult mouse. b .
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [Scanpy, SciPy v1.11.2, Seurat, UMAP, igraph] -> simulation/modelling [AnnData, R, Slingshot] -> stage not stated [BLAST v2.9.0, scDblFinder v0.2.3]

### Spatial dynamics of brain development and neuroinflammation. (Nature 2025)

- DOI: 10.1038/s41586-025-09663-y | PMCID: PMC12589135 | PMID: 41193846
- Evidence: UMAP visualization and clustering were performed on this combined space using a resolution of 1.0.
- Full pipeline: alignment/mapping [ImageJ] -> dimensionality reduction/clustering [CellChat, Cellpose, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ArchR, Python v3.9, QuPath, R v4.1, Seurat v4.1, Signac v1.8]

### Transcriptomic and spatial organization of telencephalic GABAergic neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09296-1 | PMCID: PMC12589142 | PMID: 41193843
- Evidence: UMAP projection We performed principal component analysis (R package stats, v.4.4.1, RRID: SCR_025968) based on the imputed gene expression matrix of 4,895 marker genes using the 10xv3 reference.
- Full pipeline: quantification [R, UMAP] -> dimensionality reduction/clustering [R, Seurat v5.1.0, UMAP] -> stage not stated [scDblFinder]

### Multi-omic profiling reveals age-related immune dynamics in healthy adults. (Nature 2025)

- DOI: 10.1038/s41586-025-09686-5 | PMCID: PMC12711581 | PMID: 41162704
- Evidence: Clustering and cell subsetting After QC filtering, all remaining cells were clustered using a Scanpy workflow 56 to normalize, log transform, perform principal components analysis (PCA), integrate age groups with Harmony 57 , perform Leiden clustering 58 , and generate two-dimensional UMAP projections.
- Full pipeline: quality control [UMAP] -> normalisation [UMAP, scDblFinder] -> dimensionality reduction/clustering [MACS2, UMAP, scDblFinder] -> differential/statistical testing [DESeq2 v1.42.0, GSEA, R v4.3.2, fgsea] -> simulation/modelling [Slingshot] -> visualisation [scDblFinder] -> stage not stated [ArchR v1.0.2, Scanpy, Seurat v5.0.1, lme4]

### Mapping Plasmodium transitions and interactions in the Anopheles female. (Nature 2025)

- DOI: 10.1038/s41586-025-09653-0 | PMCID: PMC12695668 | PMID: 41125888
- Evidence: Subsequently, a UMAP was generated including the top 12 principal components through the RunUMAP function, with parameters set to min.dist = 0.4, and repulsion.strength = 2.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, DESeq2, Monocle, Python v3.10, R v4.3, Scanpy v1.9.1, Seurat, scDblFinder]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Clustering was then run using the functions RunUMAP, FindNeighbors and FindClusters and the output UMAP graphs were generated by DimPlot.
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Evidence: Comparisons include response groups and CD8 + versus CD4 + for all patients ( n = 13). h , Uniform manifold approximation and projection (UMAP) of CD8 + T cell clusters ( n = 4,588). i , Dotplot of CD8 + T cell clusters and within-sample cluster distributions between responders ( n = 3) and non-responders ( n = 9), indicating log 2 fold change between mean cluster proportions.
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### A parabrachial hub for need-state control of enduring pain. (Nature 2025)

- DOI: 10.1038/s41586-025-09602-x | PMCID: PMC12630001 | PMID: 41062698
- Evidence: PCA results were used to generate a UMAP for visualization, Leiden clustering for identifying distinct cell clusters, and InSituType cell typing, an unsupervised method that detects cell clusters without a reference matrix.
- Full pipeline: quantification [NumPy, Scanpy] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP, seaborn] -> visualisation [UMAP, seaborn] -> stage not stated [AnnData, ImageJ]

### Flexible perceptual encoding by discrete gamma events. (Nature 2025)

- DOI: 10.1038/s41586-025-09604-9 | PMCID: PMC12657229 | PMID: 41062693
- Evidence: Here the reference channel is taken as the closest to Layer 4. c : Spectrotemporal dynamics at the time of candidate events are parameterized using the real and imaginary part of the analytical representation (matlab function hilbert ) of the filtered LFP in each channel ( Supplementary Methods ). d : Three dimensional UMAP embedding showing the cloud of candidate events in the parametric space.
- Full pipeline: dimensionality reduction/clustering [NumPy v1.11.3, UMAP] -> stage not stated [Psychtoolbox]

### Proteotoxic stress response drives T cell exhaustion and immune evasion. (Nature 2025)

- DOI: 10.1038/s41586-025-09539-1 | PMCID: PMC12657239 | PMID: 41034580
- Evidence: UMAP was used for visualization, depicting cellular heterogeneity across batches, datasets, sex, organ origins and cancer types.
- Full pipeline: quality control [AnnData, Scanpy v1.9.5] -> read trimming [HISAT2 v2.2.1, SAMtools v1.17] -> alignment/mapping [HISAT2 v2.2.1, SAMtools v1.17] -> normalisation [AnnData, R, tidyverse v1.3.1] -> dimensionality reduction/clustering [Enrichr, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [ImageJ, scVelo, survival (R)]

### A human-specific regulatory mechanism revealed in a pre-implantation model. (Nature 2025)

- DOI: 10.1038/s41586-025-09571-1 | PMCID: PMC12589118 | PMID: 41034587
- Evidence: The identified annotations and UMAP values were used in our plots and conclusions. scRNA-seq data analysis including transposons Raw data from Kagawa et al.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, HISAT2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, UMAP] -> stage not stated [BLAST, MACS2, RepeatMasker, SAMtools, Seurat]

### Collective homeostasis of condensation-prone proteins via their mRNAs. (Nature 2025)

- DOI: 10.1038/s41586-025-09568-w | PMCID: PMC12629991 | PMID: 40993389
- Evidence: For clustering, UMAP was used to reduce the dimensionality of the data to 4 dimensions, using 50 neighbours and a minimum distance of 0.001.
- Full pipeline: read trimming [Cutadapt v4.4, STAR v2.7.0] -> alignment/mapping [STAR v2.7.0, minimap2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [AlphaFold, CellProfiler, Cellpose v2.0, Nextflow, R]

### Basal cell of origin resolves neuroendocrine-tuft lineage plasticity in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09503-z | PMCID: PMC12589105 | PMID: 40963028
- Evidence: UMAP embedding was performed using sc.tl.umap() with min_dist=0.5.
- Full pipeline: quality control [Python v3.8.8, Scanpy v1.10.0] -> alignment/mapping [STAR] -> variant calling [CellProfiler] -> quantification [CellProfiler] -> normalisation [Python v3.8.8, Scanpy v1.10.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat] -> stage not stated [AnnData, GSEA, QuPath]

### Myeloperoxidase transforms chromatin into neutrophil extracellular traps. (Nature 2025)

- DOI: 10.1038/s41586-025-09523-9 | PMCID: PMC12629992 | PMID: 40963017
- Evidence: To identify possible protein complexes of interest, the embeddings are projected on a 2D manifold (UMAP) (Supplementary Fig.
- Full pipeline: alignment/mapping [IMOD v4.11] -> dimensionality reduction/clustering [UMAP] -> structure determination [IMOD v4.11, PHENIX, RELION v3.1] -> stage not stated [ChimeraX]

### Repeated head trauma causes neuron loss and inflammation in young athletes. (Nature 2025)

- DOI: 10.1038/s41586-025-09534-6 | PMCID: PMC12589125 | PMID: 40963024
- Evidence: Scale bars, 100 μm. c , Uniform manifold approximation and projection (UMAP) analysis of nuclei from all donors labelled for cell type based on cell-type marker expression.
- Full pipeline: quality control [R, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [ArchR v1.0.2, ComplexHeatmap v2.14.0, Metascape, ggplot2 v3.4.2, ggpubr v0.6.0]

### A neuronal architecture underlying autonomic dysreflexia. (Nature 2025)

- DOI: 10.1038/s41586-025-09487-w | PMCID: PMC12571909 | PMID: 40963010
- Evidence: ...ch major cell type of the mouse spinal cord. h , Proportion of mitochondrial counts per nucleus in each major cell type of the mouse spinal cord. i , UMAP visualization of 64,739 nuclei colored by major cell type, segregated by the location of spinal cord tissues (L6, T12) and experimental conditions (SCI only, exposure to repeated episode of autonomic dysreflexia, AD). j , Proportions of nuclei f...
- Full pipeline: quality control [Seurat] -> alignment/mapping [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [tidyverse] -> visualisation [UMAP] -> stage not stated [ImageJ, Nextstrain, QuPath v0.4.3]

### Learning the natural history of human disease with generative transformers. (Nature 2025)

- DOI: 10.1038/s41586-025-09529-3 | PMCID: PMC12589094 | PMID: 40963019
- Evidence: Model interpretation Token embedding UMAP The low-dimensional representation of token space was constructed by applying the UMAP 58 dimensionality reduction algorithm to the learned token embeddings for Delphi-2M (1,270 × 120 matrix).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Jupyter, PyTorch, Python, scikit-learn]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Evidence: Uniform manifold approximation and projection (UMAP) and t -distributed stochastic neighbour embedding projections were calculated using the first 50 principal components.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### Analogue speech recognition based on physical computing. (Nature 2025)

- DOI: 10.1038/s41586-025-09501-1 | PMCID: PMC12460176 | PMID: 40963022
- Evidence: 5 Uniform manifold approximation and projection (UMAP) visualization of RNPU preprocessed dataset.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Evidence: Coarse connectivity of the manifold was calculated using PAGA with scanpy.tl.paga and used as the starting point for uniform manifold approximation and projection (UMAP) embedding with scanpy.umap using standard settings.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### Neuronal activity-dependent mechanisms of small cell lung cancer pathogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09492-z | PMCID: PMC12571889 | PMID: 40931074
- Evidence: Subsequently, UMAP embeddings were generated and cells were clustered using Seurat’s Louvain algorithm-based FindClusters function.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scDblFinder] -> stage not stated [Fiji v2.1.0, GSEA, GSVA, ImageJ v2.1.0, Seurat, fgsea]

### Loss-of-function mutations in PLD4 lead to systemic lupus erythematosus. (Nature 2025)

- DOI: 10.1038/s41586-025-09513-x | PMCID: PMC12611768 | PMID: 40931063
- Evidence: NK, natural killer cells; NKT, natural killer T cells; T mem , memory T cells. d , Uniform manifold approximation and projection (UMAP) plot showing the differences in various cell types between patients P1 and P2 and healthy controls. e , UMAP plot of NF-κB and type I IFN signalling pathways genes.
- Full pipeline: alignment/mapping [ANNOVAR, HISAT2, featureCounts] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2, PyMOL v3.1, R, pheatmap] -> visualisation [DESeq2, R, Seurat, pheatmap] -> stage not stated [GSEA]

### ABCA7 variants impact phosphatidylcholine and mitochondria in neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09520-y | PMCID: PMC12611789 | PMID: 40931065
- Evidence: Genes with ∣ S ∣ > 1.3 in at least one of six major cell types (excitatory neurons, inhibitory neurons, astrocytes, microglia, oligodendrocytes and OPCs) were projected from 6D perturbation-score space into 2D using UMAP (Python umap).
- Full pipeline: read trimming [STAR, Trim Galore, featureCounts] -> alignment/mapping [STAR, Trim Galore, featureCounts] -> variant calling [limma, statsmodels] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [GSEA, limma, statsmodels] -> simulation/modelling [GROMACS v2022.3, VMD v1.94] -> machine learning [Cellpose] -> visualisation [Matplotlib, NetworkX, VMD v1.94] -> stage not stated [PyMOL v2.0, Python, scikit-learn]

### Amygdala-liver signalling orchestrates glycaemic responses to stress. (Nature 2025)

- DOI: 10.1038/s41586-025-09420-1 | PMCID: PMC12527908 | PMID: 40903586
- Evidence: A single major population of Vgat (also known as Slc32a1 )-expressing GABAergic (γ-aminobutyric acid-expressing) neurons was resolved in uniform manifold approximation and projection (UMAP) space, whereas three populations of glutamatergic neurons were resolved on the basis of exclusive expression of Vglut1 (also known as Slc17a7 ) or Vglut2 (also known as Slc17a6 ) or co-expression of both genes ...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.4.2, emmeans, lme4]

### Single-cell transcriptomic and genomic changes in the ageing human brain. (Nature 2025)

- DOI: 10.1038/s41586-025-09435-8 | PMCID: PMC12527935 | PMID: 40903571
- Evidence: The top 8,000 variable features were selected for principal component analysis (PCA), clustering and uniform manifold approximation and projection (UMAP) analysis.
- Full pipeline: alignment/mapping [BWA v0.7.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [Cellpose, GATK v4.1.8.1, Picard, Seurat]

### Spatial joint profiling of DNA methylome and transcriptome in tissues. (Nature 2025)

- DOI: 10.1038/s41586-025-09478-x | PMCID: PMC12571926 | PMID: 40903587
- Evidence: Finally, a UMAP embedding was computed using the same principal components with RunUMAP function.
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [Python, R, UMAP, clusterProfiler, pheatmap] -> visualisation [Python] -> stage not stated [HOMER, Seurat]

### Dynamic fibroblast-immune interactions shape recovery after brain injury. (Nature 2025)

- DOI: 10.1038/s41586-025-09449-2 | PMCID: PMC12545229 | PMID: 40903576
- Evidence: Feature and spatial feature plots, violin plots, and UMAP plots were generated using Seurat.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [Monocle] -> visualisation [CellPhoneDB] -> stage not stated [ComplexHeatmap, DESeq2, Fiji, ImageJ, Jupyter, R, Seurat, data.table, ggpubr, tidyverse]

### Maternal stress triggers early-life eczema through fetal mast cell programming. (Nature 2025)

- DOI: 10.1038/s41586-025-09419-8 | PMCID: PMC12488486 | PMID: 40866704
- Evidence: The k -nearest neighbour graph, UMAP and t-distributed stochastic neighbour embedding projections were computed on the basis of the first 20 corrected principal components.
- Full pipeline: quality control [FastQC] -> alignment/mapping [STAR v2.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2 v1.34.0, ImageJ v2.16.0, Seurat, Signac v1.14.0]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Evidence: 4 Developmental changes in human single-cell RNA and ATAC-seq cell clusters over time. a , Uniform manifold approximation and projection (UMAP) plots for RNA-seq, ATAC-seq, and integrated RNA + ATAC-seq using Weighted Nearest Neighbor (WNN) for E53, E57, E67, and E72 for human ilia + adjacent soft tissue sc-multiomics data.
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: 1 Confinement induces an undifferentiated neuronal gene program. a , Schematic detailing the workflow of spatial transcriptomics and scRNA-seq experiments performed on zebrafish melanomas. b , Uniform manifold approximation and projection (UMAP) of human melanoma scRNA-seq dataset from Jerby-Arnon et al.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Evidence: Clusters were visualized using UMAP via the RunUMAP() function.
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### Thymic epithelial cells amplify epigenetic noise to promote immune tolerance. (Nature 2025)

- DOI: 10.1038/s41586-025-09424-x | PMCID: PMC12527919 | PMID: 40836089
- Evidence: For UMAP plots overlaid with continuous colour scales, MAGIC 67 (v.2.0.3) imputation was used for data smoothing to facilitate better visualization.
- Full pipeline: read trimming [edgeR v4.0.2] -> alignment/mapping [Bowtie2 v2.2.9, TopHat v2.1.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v4.0.2] -> visualisation [UMAP] -> stage not stated [ArchR, MACS2 v2.2.9.1, Picard v2.21.8, R v4.3.2, SAMtools v1.9, Seurat v5.1.0, featureCounts]

### Cancer-induced nerve injury promotes resistance to anti-PD-1 therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-09370-8 | PMCID: PMC12406299 | PMID: 40836096
- Evidence: 4 Mitigating injury signalling inside peripheral sensory (nociceptors) neurons ameliorated intratumoural immunosuppression. a , Uniform manifold approximation and projection (UMAP) plot of scRNA-seq data of DRG neurons innervating mouse paws that were inoculated with either B16F10-OVA melanoma or normal keratinocytes (Extended Data Fig.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Bioconductor, Cutadapt v1.18, STAR v2.5.11, Trimmomatic, edgeR] -> alignment/mapping [STAR v2.5.11, Trimmomatic, featureCounts] -> quantification [Bioconductor, STAR v2.5.11, Trimmomatic, edgeR] -> normalisation [Bioconductor, edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0.5, Enrichr, GSEA, ImageJ, R, Seurat v4.1.1]

### Axonal injury is a targetable driver of glioblastoma progression. (Nature 2025)

- DOI: 10.1038/s41586-025-09411-2 | PMCID: PMC12507684 | PMID: 40836081
- Evidence: Statistical analysis was performed using two-sided unpaired t -tests. n = 10 (WT) and n = 6 ( Sarm1 −/− ) mice. e , Uniform manifold approximation and projection (UMAP) of scRNA-seq data from terminal WT and Sarm1 −/− npp tumours: neural progenitor-like (NPC-like), OPC-like, astrocyte-like (AC-like), MES-like and aNSC-like. f , As in e , but for microenvironmental cells: choroid plexus cells (CP),...
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, ImageJ, R, Seurat, Squidpy, fgsea, scikit-image]

### Expanding the cytokine receptor alphabet reprograms T cells into diverse states. (Nature 2025)

- DOI: 10.1038/s41586-025-09393-1 | PMCID: PMC12460165 | PMID: 40804519
- Evidence: The area under the receiver-operator curve (AUC) scores for all TFs were stored in a designated assay slot (termed scenic) and used for UMAP computation with the Seurat RunUMAP function with the default parameters.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC, MACS2 v3.0.1] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [R v4.4, SCENIC v0.12.1]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Evidence: 2 Single-cell repertoire in the chaetognath P. gotoi. a , Uniform manifold approximation and projection (UMAP) dimensionality reduction of cell expression profiles from pooled juvenile and adult libraries (Extended Data Fig.
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Data-driven de novo design of super-adhesive hydrogels. (Nature 2025)

- DOI: 10.1038/s41586-025-09269-4 | PMCID: PMC12328221 | PMID: 40770436
- Evidence: All adhesion measurements were performed under the same test conditions as the training set: 10 N loading force, 10-s contact time, on a glass substrate and in normal saline. b , UMAP representation of the relationship between F a and reduced monomer proportions ( ϕ i ), highlighting the formulations proposed by GP_KB and RFR-GP (within the SMBO framework) across different rounds.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost] -> machine learning [UMAP] -> stage not stated [Python, scikit-learn v1.0.2]

### Microglia-neuron crosstalk through Hex-GM2-MGL2 maintains brain homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09477-y | PMCID: PMC12545202 | PMID: 40769205
- Evidence: Last, UMAP embedding and shared nearest-neighbours graph construction were performed on the top ten principal components (top seven principal components for human data) (RunUMAP, FindNeighbors), and cell clusters were identified with a resolution set to 1.2 (0.5 for human data) (FindClusters).
- Full pipeline: quality control [FastQC v0.73, Trim Galore] -> read trimming [FastQC v0.73, Trim Galore] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.0] -> differential/statistical testing [limma] -> visualisation [ggplot2] -> stage not stated [ImageJ v1.54g, R, Seurat v5.0.3, pheatmap v1.0.12, scDblFinder]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Evidence: UMAP and TSNE were performed using RunUMAP and RunTSNE using Seurat with dimensions 1:30 and do.fast=TRUE parameter.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### Microglia regulate GABAergic neurogenesis in prenatal human brain through IGF1. (Nature 2025)

- DOI: 10.1038/s41586-025-09362-8 | PMCID: PMC12527950 | PMID: 40770097
- Evidence: Standard data normalization, variable feature identification, linear transformations, dimensional reduction, UMAP embedding and unsupervised clustering were conducted using the standard Seurat pipeline 35 .
- Full pipeline: quantification [ImageJ v1.54] -> normalisation [UMAP] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [ImageJ v1.54] -> simulation/modelling [Monocle] -> visualisation [Monocle] -> stage not stated [CellChat, Enrichr, Scanpy v1.10.3, Seurat v5.1.0, scDblFinder v2.0.3]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Evidence: The top 20 principal components that were not driven by extreme outlier data or immediate early genes were used to construct a two-dimensional (2D) UMAP using cell–cell Euclidean distances as input.
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### A molecular cell atlas of mouse lemur, an emerging model primate. (Nature 2025)

- DOI: 10.1038/s41586-025-09113-9 | PMCID: PMC12328211 | PMID: 40739356
- Evidence: Next, data scaling, dimensionality reduction (PCA), clustering and visualization (t-SNE and UMAP) were performed following the standard Seurat pipeline as previously described 14 , with parameters including the numbers of principal components (PCs), perplexity and resolution manually adjusted for each iteration of cell clustering.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP]

### Contextualizing ancient texts with generative neural networks. (Nature 2025)

- DOI: 10.1038/s41586-025-09292-5 | PMCID: PMC12408360 | PMID: 40702185
- Evidence: 1 presents a visualization of the embedding spaces using uniform manifold approximation and projection (UMAP) dimensionality reduction 84 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Precisely defining disease variant effects in CRISPR-edited single cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09313-3 | PMCID: PMC12488502 | PMID: 40702188
- Evidence: This was followed by batch correction using Harmony 42 and dimension reduction using UMAP (uwot package) 43 .
- Full pipeline: alignment/mapping [kallisto] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> stage not stated [GSEA, R, lme4]

### Mitochondrial origins of the pressure to sleep. (Nature 2025)

- DOI: 10.1038/s41586-025-09261-y | PMCID: PMC12443607 | PMID: 40670797
- Evidence: 1 The transcriptional response of dFBNs to sleep deprivation. a , Uniform manifold approximation and projection (UMAP) representation of glutamatergic neurons (grey) according to their gene expression profiles. dFBNs (purple) form a distinct cluster containing cells from rested (blue, n = 237 cells) and sleep-deprived brains (red, n = 86 cells). b , log-normalized expression levels of dFBN markers...
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [STAR v2.6.1b, Seurat v4.1]

### Ongoing genome doubling shapes evolvability and immunity in ovarian cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09240-3 | PMCID: PMC12390843 | PMID: 40670783
- Evidence: Expression UMAP from scRNA-seq of FNE1 and RPE-1 mixed-WGD samples with cells colored by assignment to the WGD and non-WGD clones. d .
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [BWA v0.7.17, FastQC, Picard v2.27.4, Trim Galore] -> variant calling [Mutect2, SHAPEIT] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [QuPath, R, Seurat, StarDist]

### Neutrophils drive vascular occlusion, tumour necrosis and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09278-3 | PMCID: PMC12422981 | PMID: 40670787
- Evidence: 5h ), and these regions also separated clearly in the low-dimensional uniform manifold approximation and projection (UMAP) representation (Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.2, data.table v1.14.2, edgeR v3.32.1, ggplot2 v3.3.3, ggpubr v0.4.0, igraph v1.2.10, limma v3.46.0, pheatmap v1.0.12] -> simulation/modelling [clusterProfiler v4.2.2, data.table v1.14.2] -> stage not stated [Bioconductor v3.12, CellChat v1.6.1, DESeq2, ImageJ, QuPath, R v4.0, Seurat v4.1.0, tidyverse]

### Imidazole propionate is a driver and therapeutic target in atherosclerosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09263-w | PMCID: PMC12408353 | PMID: 40670786
- Evidence: Then, cells were clustered using the Louvain algorithm and visualized using the uniform manifold approximation and projection for dimension reduction (UMAP) algorithm with the first 25 principal components as input.
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC, R] -> alignment/mapping [RSEM] -> normalisation [ComplexHeatmap, DESeq2] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [UMAP] -> stage not stated [Bioconductor, DADA2, ImageJ, Seurat v4.0.6, fgsea]

### Selective remodelling of the adipose niche in obesity and weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-09233-2 | PMCID: PMC12367556 | PMID: 40634602
- Evidence: BMI, body mass index (kg m –2 ); F insulin, fasting insulin (mIU L –1 ); HbA1c, haemoglobin A1c (%); HDL, high-density lipoprotein cholesterol (mM); DBP, diastolic blood pressure (mm Hg). c , Uniform manifold approximation and projection (UMAP) of 145,452 human AT cells ( n = 74 samples of the primary cohort and n = 13 samples of the Emont published cohort 11 , single nucleus).
- Full pipeline: variant calling [IMPUTE2 v2.3.2, SHAPEIT, scDblFinder] -> normalisation [AnnData] -> dimensionality reduction/clustering [AnnData, Scanpy, UMAP, scDblFinder] -> stage not stated [CellChat, ImageJ, QuPath v0.5.1, SCENIC, SciPy, Seurat]

### Range extender mediates long-distance enhancer activity. (Nature 2025)

- DOI: 10.1038/s41586-025-09221-6 | PMCID: PMC12267059 | PMID: 40604280
- Evidence: From the combined Seurat object, UMAP and nearest-neighbour analyses were performed to identify clusters with a resolution of 1 across 20 dimensions, as indicated by the ElbowPlot function, and based on their chromatin and gene expression profiles.
- Full pipeline: alignment/mapping [BEDTools] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [HOMER] -> stage not stated [MACS2, R, Signac]

### Engrafted nitrergic neurons derived from hPSCs improve gut dysmotility in mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09208-3 | PMCID: PMC12408359 | PMID: 40562934
- Evidence: Principal component analysis was run using default settings, and UMAP dimensionality reduction was performed using the principal component analysis reduction.
- Full pipeline: quality control [R v4.0, Seurat, SpikeInterface] -> read trimming [kallisto] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt, DESeq2, HTSeq]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Evidence: We generated a uniform manifold approximation and projection (UMAP) embedding based on extracted morphometric features with each point representing one cell structure.
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Evidence: TF, transcription factor. b , Uniform manifold approximation and projection (UMAP) of snRNA-seq ( n = 935,371 nuclei) across 14 subtypes (top) and cell proportion of subtypes across diagnostic conditions (CON, MDD and PTSD; bottom). *FDR < 0.05. c , UMAP of snATAC-seq ( n = 473,033 nuclei) across seven cell types (top) and proportion of cell types across conditions (bottom). d , UMAP of snMultiome...
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Kupffer cell programming by maternal obesity triggers fatty liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09190-w | PMCID: PMC12367551 | PMID: 40533564
- Evidence: Again, multimodal neighbours were identified (FindMultiModalNeighbors) using PCA for RNA and Harmony for ATAC, followed by UMAP for dimensionality reduction (RunUMAP) and clustering (FindClusters), as done for the dataset using all cell types.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [kallisto] -> quantification [QuPath, kallisto] -> dimensionality reduction/clustering [CellChat, UMAP, clusterProfiler] -> stage not stated [Bioconductor v3.15, DESeq2, MACS2, Seurat, Signac]

### Metabolic adaptations direct cell fate during tissue regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09097-6 | PMCID: PMC12240837 | PMID: 40500453
- Evidence: 1 Characterization of OGDH expression in the gut. a , UMAP derived from publicly available scRNA-seq data demonstrating distinct transcriptional signatures in various subpopulations of human intestinal and colonic cells. b , AddModule Score showing average expression of the TCA-cycle signature across the indicated intestinal lineages human small intestine.
- Full pipeline: read trimming [Trimmomatic, featureCounts] -> alignment/mapping [Trimmomatic, featureCounts] -> quantification [ImageJ v1.7, featureCounts] -> normalisation [pheatmap] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R, Trimmomatic] -> visualisation [Trimmomatic, pheatmap] -> stage not stated [GSEA, MACS2, Seurat]

### Discovery of FoTO1 and Taxol genes enables biosynthesis of baccatin III. (Nature 2025)

- DOI: 10.1038/s41586-025-09090-z | PMCID: PMC12240809 | PMID: 40500440
- Evidence: For integrated UMAP plots, scVI was used to integrate cells from multiple single-cell experiments 57 .
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [AlphaFold, Clustal Omega, Trimmomatic] -> dimensionality reduction/clustering [SciPy, UMAP] -> stage not stated [HMMER, NumPy, Scanpy v1.10.1]

### Developmental trajectory and evolutionary origin of thymic mimetic cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09148-y | PMCID: PMC12286861 | PMID: 40500437
- Evidence: Using the final signatures, mimetic cells were identified in the uniform manifold approximation and projection (UMAP) graphs calculated from single-cell datasets 20 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Galaxy, HISAT2 v2.1.0, MACS2, Trim Galore, featureCounts v1.6.1.0, scDblFinder]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Visualization of the results was achieved through two-dimensional UMAP plots, illustrating cell types, batches, datasets, gender, organs and cancer types.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### CREM is a regulatory checkpoint of CAR and IL-15 signalling in NK cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09087-8 | PMCID: PMC12286855 | PMID: 40468083
- Evidence: RunPCA() and RunUMAP() were run to generate a UMAP embedding using 20 principal components selected by inspecting the elbow plots.
- Full pipeline: quantification [SCENIC] -> normalisation [ImageJ v1.53t] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [fgsea] -> stage not stated [GSEA, MACS2, R v4.0.1, Scanpy, Seurat, Signac v1.12.0]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: Dashed line indicates P = 0.05. c , UMAP plot of AKP control (23,579 cells) and AKP Atrx KO (25,757 cells) single cells coloured by genotype. d , UMAP plot coloured and numbered by cluster in AKP control and AKP Atrx KO single cells. e , UMAP plots coloured by the expression of genes used for defining colonic differentiation and EMT in AKP control and AKP Atrx KO single cells.
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### Mouse liver assembloids model periportal architecture and biliary fibrosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09183-9 | PMCID: PMC12350178 | PMID: 40441268
- Evidence: UMAP representing the hepatocytes from HM-Wnt and MM media HepOrg and expression of selected periportal ( Cdh1 , Alb ) and pericentral ( Cyp1a2 , Cyp2e1 ) genes in the two media. e.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.36.0] -> machine learning [StarDist] -> stage not stated [GSEA, ImageJ, R, Scanpy v1.9.2, fgsea v1.22.0, scDblFinder]

### Cross-tissue multicellular coordination and its rewiring in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09053-4 | PMCID: PMC12240829 | PMID: 40437094
- Evidence: The batch-corrected graph was then utilized to perform UMAP 56 for visualizing cells on a two-dimensional layout.
- Full pipeline: quality control [Scanpy] -> normalisation [igraph] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ComplexHeatmap, R, UMAP, igraph] -> stage not stated [CellChat, CellPhoneDB, SCENIC, Seurat, scDblFinder]

### A coordinated cellular network regulates tolerance to food. (Nature 2025)

- DOI: 10.1038/s41586-025-09173-x | PMCID: PMC12328219 | PMID: 40425043
- Evidence: Data are mean ± s.d. h , UMAP analysis of H-2Kb–OVA + CD8αβ T cells isolated from the SILP of mice in the standard and Trojan Horse models, 7 days after infection.
- Full pipeline: read trimming [R v4.3.1, Seurat] -> dimensionality reduction/clustering [UMAP]

### Multigenerational cell tracking of DNA replication and heritable DNA damage. (Nature 2025)

- DOI: 10.1038/s41586-025-08986-0 | PMCID: PMC12176655 | PMID: 40399682
- Evidence: Dimension reduction was performed using the UMAP method, using the first 20 principal components.
- Full pipeline: quality control [FastQC, fastp, kallisto] -> alignment/mapping [FastQC, fastp, kallisto] -> dimensionality reduction/clustering [Bioconductor, Enrichr, R, Seurat, UMAP, clusterProfiler, edgeR] -> differential/statistical testing [FastQC, Seurat, edgeR, fastp, kallisto] -> visualisation [ImageJ]

### Clonal tracing with somatic epimutations reveals dynamics of blood ageing. (Nature 2025)

- DOI: 10.1038/s41586-025-09041-8 | PMCID: PMC12240852 | PMID: 40399669
- Evidence: Then we used Seurat’s standard workflow without normalization to obtain a low-dimensional representation of our data using UMAP.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2] -> stage not stated [ComplexHeatmap, Seurat]

### Spatial transcriptomics reveals human cortical layer and area specification. (Nature 2025)

- DOI: 10.1038/s41586-025-09010-1 | PMCID: PMC12328223 | PMID: 40369074
- Evidence: The resulting clusters were visualized using UMAP in Extended Data Fig.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat, UMAP, XGBoost v2.0.3, scikit-learn] -> visualisation [Seurat, UMAP] -> stage not stated [Bioconductor v3.19, CellChat, Cellpose, ImageJ, Python v3.10, R]

### STAT5 and STAT3 balance shapes dendritic cell function and tumour immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09000-3 | PMCID: PMC12240842 | PMID: 40369063
- Evidence: Using the Louvain algorithm for shared nearest neighbours clustering and uniform manifold approximation and projection (UMAP) visualization to distinguish the cells, we conducted an analysis with two major distinct DC clusters, conventional DCs (cDCs) and monocyte-derived DCs (moDCs) (Extended Data Fig.
- Full pipeline: quantification [QuPath v0.5.1, edgeR v4.2.2] -> normalisation [edgeR v4.2.2] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.9.2] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [ImageJ v1.51n, Seurat v4.3.0, ggpubr v0.6.0, limma v3.60.6]

### Interferon-γ orchestrates leptomeningeal anti-tumour response. (Nature 2025)

- DOI: 10.1038/s41586-025-09012-z | PMCID: PMC12286854 | PMID: 40369076
- Evidence: The UMAP was computed with sc.tl.umap, using the default parameters.
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo] -> visualisation [Python] -> stage not stated [DESeq2, Fiji v2.0.0, GSEA, HTSeq, ImageJ v2.0.0]

### Taurine from tumour niche drives glycolysis to promote leukaemogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09018-7 | PMCID: PMC12328231 | PMID: 40369079
- Evidence: UMAP dimensional reduction was also performed using RunUMAP using the first 30 principal components.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> differential/statistical testing [DESeq2 v1.28.1, Enrichr] -> stage not stated [Seurat v4.1.0, tidyverse v1.2.0]

### Oncogene aberrations drive medulloblastoma progression, not initiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08973-5 | PMCID: PMC12222029 | PMID: 40335697
- Evidence: Further, the gene expression matrices from all samples were merged together in the full matrix and processed by means of the Seurat package 43 to normalize, compute top principal complements ( n = 30), find most highly variable genes ( n = 2,500) and visualize by means of UMAP.
- Full pipeline: quality control [Nextflow] -> alignment/mapping [Nextflow, STAR] -> normalisation [Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Seurat, Signac, UMAP, clusterProfiler] -> differential/statistical testing [ArchR, DESeq2, clusterProfiler] -> visualisation [ComplexHeatmap, Seurat, Signac, UMAP] -> stage not stated [BCFtools, Cellpose, GSVA, Python, R, SoupX, featureCounts]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Evidence: Subsequently, uniform manifold approximation and projection (UMAP) nonlinear dimensionality reduction was computed by means of the RunUMAP function using all 50 principal components with default parameters.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### Cell cycle duration determines oncogenic transformation capacity. (Nature 2025)

- DOI: 10.1038/s41586-025-08935-x | PMCID: PMC12119354 | PMID: 40307557
- Evidence: The neighbourhood graph of cells was computed with the top 50 principal components, and then, the graph was embedded into two dimensions using UMAP.
- Full pipeline: quality control [Scanpy, Seurat] -> quantification [ImageJ] -> normalisation [Scanpy, Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr]

### A distributed coding logic for thermosensation and inflammatory pain. (Nature 2025)

- DOI: 10.1038/s41586-025-08875-6 | PMCID: PMC12222022 | PMID: 40269164
- Evidence: Neuronal and non-neuronal cell clusters were identified in UMAP by analysing the expression of Snap25 , Mbp , Apoe , Qk , Pecam1 , Slc17a7 and Slc17a6 .
- Full pipeline: quantification [NumPy v1.19.2, SciPy v1.5.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.19.2, SciPy v1.5.2] -> stage not stated [ImageJ, OpenCV, Python, Seurat, scDblFinder]

### Deep Visual Proteomics maps proteotoxicity in a genetic liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08885-4 | PMCID: PMC12158776 | PMID: 40240610
- Evidence: The resulting 2,048 image features were projected into a two-dimensional space using the UMAP algorithm 44 .
- Full pipeline: dimensionality reduction/clustering [R, UMAP, scikit-learn] -> differential/statistical testing [GSEA, limma] -> stage not stated [Cellpose v2.0, STRING db]

### PRDM16-dependent antigen-presenting cells induce tolerance to gut antigens. (Nature 2025)

- DOI: 10.1038/s41586-025-08982-4 | PMCID: PMC12176658 | PMID: 40228524
- Evidence: 2 RORγt regulates development of PRDM16-expressing tolDCs within mLNs. a , Uniform manifold approximation and projection (UMAP) representation of 21,504 transcriptomes obtained from scRNA-seq of MHCII-expressing innate immune system cells (CD45 + Ly6G − B220 − TCRγδ − TCRβ − MHCII + ) in the mLN, combining data from 3-week-old control and Δ+7 kb mice for joint clustering.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.3, Picard, SAMtools v0.1.19] -> normalisation [Seurat v5.1] -> dimensionality reduction/clustering [Seurat v5.1, UMAP] -> stage not stated [Signac v1.14]

### NEURD offers automated proofreading and feature extraction for connectomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08660-5 | PMCID: PMC11981913 | PMID: 40205208
- Evidence: The spatial distribution of uniform manifold approximation and projection for dimension reduction (UMAP) embeddings (2D projection) for feature vectors of spines sampled from the MICrONS and H01 dataset showed a similar structure, with spines that share similar features embedded in similar locations and a somewhat consistent embedding pattern for inhibitory and excitatory spines in the two volumes...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [DeepLabCut, SLEAP, Squidpy] -> stage not stated [CaImAn, Kilosort, NetworkX, Python]

### Comprehensive interrogation of synthetic lethality in the DNA damage response. (Nature 2025)

- DOI: 10.1038/s41586-025-08815-4 | PMCID: PMC12018271 | PMID: 40205037
- Evidence: UMAP embedding was calculated in R using the strong score across a symmetric version of the entire dataset, without prior dimension or variance reduction.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> quantification [Fiji v2.9.0, ImageJ v2.9.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, MACS2 v3.0.0b, Python, R, SAMtools v1.6, limma]

### Human assembloid model of the ascending neural sensory pathway. (Nature 2025)

- DOI: 10.1038/s41586-025-08808-3 | PMCID: PMC12137141 | PMID: 40205039
- Evidence: The top 50 principal components (PCs) were used for clustering (resolution of 1.0) using the ‘FindNeighbors’ and ‘FindClusters’ functions and for visualization with UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R, Seurat v4.3.0]

### Foundation model of neural activity predicts response to new stimulus types. (Nature 2025)

- DOI: 10.1038/s41586-025-08829-y | PMCID: PMC11981942 | PMID: 40205215
- Evidence: Visualization of the modulation network’s output, projected onto 2 dimensions via UMAP. a , b show the same data from an example recording session and modulation network.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [DeepLabCut] -> visualisation [UMAP] -> stage not stated [Psychtoolbox]

### Inhibitory specificity from a connectomic census of mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-024-07780-8 | PMCID: PMC11981935 | PMID: 40205209
- Evidence: See Methods for detailed feature descriptions. c , Uniform manifold approximation and projection (UMAP) of neuron features coloured by anatomical cluster.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [scikit-learn]

### Perisomatic ultrastructure efficiently classifies cells in mouse cortex. (Nature 2025)

- DOI: 10.1038/s41586-024-07765-7 | PMCID: PMC11981918 | PMID: 40205216
- Evidence: For 2D UMAP embeddings and training of the classifiers, it was important to place all features in approximately similar scales.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [UMAP]

### Multimodal cell maps as a foundation for structural and functional genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08878-3 | PMCID: PMC12137143 | PMID: 40205054
- Evidence: 2 | Multiscale integrated map of a U2OS cell. a , Multimodal embedding of proteins based on integration of AP–MS and imaging data, reduced to two dimensions using the UMAP method 56 (left).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [PyTorch] -> machine learning [PyTorch, scikit-learn] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, NumPy v1.21.6, STRING db, SciPy v1.7.3]

### Bifidobacteria support optimal infant vaccine responses. (Nature 2025)

- DOI: 10.1038/s41586-025-08796-4 | PMCID: PMC12058517 | PMID: 40175554
- Evidence: The blue–red gradient indicates decreased and increased BTM activity, respectively, relative to that of No-ABX infants. b , UMAP projection of whole-blood gene expression data pre- and postvaccination ( n = 329 infant blood samples), adjusted for sex and batch using SVAseq 38 . c , Volcano plot of differentially expressed genes postvaccination. d , Selected BTMs that were statistically enriched am...
- Full pipeline: quality control [FastQC v0.11.4, HISAT2 v2.1.0, MultiQC v1.8, Trimmomatic v0.38] -> read trimming [Cutadapt v1.18, HUMAnN v3.0, QIIME 2 v2023.2, Trimmomatic v0.38, edgeR v3.38] -> alignment/mapping [HISAT2 v2.1.0, SAMtools v1.17] -> quantification [ggplot2 v3.3.6] -> normalisation [edgeR v3.38] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, Bowtie2 v2.5.0, DADA2, GSVA v1.44.1, ImageJ, Kraken2 v2.1.1, R, featureCounts v1.5.0, fgsea, scikit-learn]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Evidence: UMAP dimensionality reduction was used for visualization, and Seurat’s FindClusters function was used to separate cells into unsupervised clusters.
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### TGFβ links EBV to multisystem inflammatory syndrome in children. (Nature 2025)

- DOI: 10.1038/s41586-025-08697-6 | PMCID: PMC12003184 | PMID: 40074901
- Evidence: A UMAP was computed using ScaleData, RunPCA to compute 50 principal components and RunUMAP using 1:50 dimensions.
- Full pipeline: normalisation [GSEA, R v4.1.2, Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [MACS2, pheatmap]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Evidence: After preprocessing, unbiased clustering on all 100 genes was performed using the dimensionality reduction method of principal component analysis (PCA) and uniform manifold approximation and projection (UMAP) 77 .
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### Constitutively active glucagon receptor drives high blood glucose in birds. (Nature 2025)

- DOI: 10.1038/s41586-025-08811-8 | PMCID: PMC12119371 | PMID: 40031956
- Evidence: ...ene expression analysis of snRNA-seq data obtained from liver three days after injection ( n = 3). h , Uniform manifold approximation and projection (UMAP) analysis of M. undulatus liver snRNA-seq data overlaid with hepatic GCGR gene expression data for M. musculus , M. undulatus and H. sapiens ( h ). i , Luciferase (LUC) activity driven by the chicken promoter mutation G291C. n = 3 replicates.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [STAR v2.5.1b] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [Scanpy v1.9.1, Seurat] -> stage not stated [AnnData, R, featureCounts]

### Aspirin prevents metastasis by limiting platelet TXA&lt;sub&gt;2&lt;/sub&gt; suppression of T cell immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-08626-7 | PMCID: PMC12018268 | PMID: 40044852
- Evidence: UMAP was performed with the UMAP Python package.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [DESeq2, GSEA] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3, QuPath]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: Almost all E16 cell types map to a single P65 cell type, with very few off-diagonal correspondence. e , Uniform manifold approximation and projection for dimension reduction (UMAP) across all eight ages for excitatory clusters.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Genome-coverage single-cell histone modifications for embryo lineage tracing. (Nature 2025)

- DOI: 10.1038/s41586-025-08656-1 | PMCID: PMC12003199 | PMID: 40011786
- Evidence: Next, 2:20 or 1:20 (only for H3K4me3) dimensions were used for identifying clusters and for UMAP visualization.
- Full pipeline: quality control [Bowtie2 v2.2.9, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.2.9, FastQC v0.11.5, SAMtools v1.9] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2 v2.1.1, Picard v2.2.4, RepeatMasker, SCENIC]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: Comparative UMAP and clustering of myeloid cells We extracted the raw counts of all MGB cells annotated as myeloid and singlets (non-doublets) from each tumour.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Glycocalyx dysregulation impairs blood-brain barrier in ageing and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08589-9 | PMCID: PMC11946907 | PMID: 40011765
- Evidence: UMAP was performed using the first 15 principal components and 30 nearest neighbours.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.32, Metascape] -> visualisation [DESeq2 v1.32] -> stage not stated [ImageJ, Seurat v4.1.1, SoupX v1.6.2, scDblFinder v2.0.4]

### Human-correlated genetic models identify precision therapy for liver cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08585-z | PMCID: PMC11922762 | PMID: 39972137
- Evidence: UMAP of the combined dataset was executed using R package uwot (v.0.1.11; https://CRAN.R-project.org/package=uwot ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.9] -> read trimming [FastQC v0.11.9, MultiQC v1.9] -> alignment/mapping [FastQC v0.11.9, MultiQC v1.9, STAR v2.7.8a] -> normalisation [DESeq2 v1.28.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, igraph v1.2.11] -> visualisation [ComplexHeatmap v2.4.3, ggplot2 v3.3.6] -> stage not stated [HTSeq, PHENIX, R, featureCounts]

### RNA neoantigen vaccines prime long-lived CD8&lt;sup&gt;+&lt;/sup&gt; T cells in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08508-4 | PMCID: PMC11946889 | PMID: 39972124
- Evidence: 3 mRNA vaccine-induced clones converge in memory phase to effector T cells. a – e , Longitudinal phenotypes of 68 out of 71 CloneTrack clones in blood from 6 vaccine responders by single-cell RNA and TCR sequencing. a , Top left, uniform manifold approximation and projection (UMAP) plots of CloneTrack clone T cells by post-vaccination time and phase.
- Full pipeline: quality control [Scanpy] -> alignment/mapping [BWA v0.7.17] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [GATK, GSEA, Mutect2 v1.1.7, Python v3.11.6, SciPy, Strelka v1.0.15]

### GABAergic neuron-to-glioma synapses in diffuse midline gliomas. (Nature 2025)

- DOI: 10.1038/s41586-024-08579-3 | PMCID: PMC11946904 | PMID: 39972132
- Evidence: We then computed the UMAP x and y values using the top 100 principal components (Extended Data Fig.
- Full pipeline: quantification [ImageJ v2.1.0] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [ggpubr]

### Characterization of single neurons reprogrammed by pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08735-3 | PMCID: PMC12018453 | PMID: 39961335
- Evidence: The resulting gene-expression matrix was used for dimensionality reduction by principal component analysis (prcomp, stats), t -distributed stochastic neighbour embedding ( t -SNE) (Rtsne, Rtsne, v.0.15) and uniform manifold approximation and projection (UMAP) (umap, umap, v.0.2.7.0).
- Full pipeline: alignment/mapping [HTSeq v2.0.1, STAR v2.5.3a] -> quantification [HTSeq v2.0.1, STAR v2.5.3a, UMAP] -> dimensionality reduction/clustering [UMAP, igraph v1.2.10] -> differential/statistical testing [DESeq2 v1.32.0] -> stage not stated [GSEA, QuPath v0.5.1]

### Learning produces an orthogonalized state machine in the hippocampus. (Nature 2025)

- DOI: 10.1038/s41586-024-08548-w | PMCID: PMC11964937 | PMID: 39939774
- Evidence: UMAP To visually interpret the dynamics of high-dimensional neural activity during learning, we utilized UMAP on our deconvolved calcium imaging data.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Suite2p]

### Macrophages protect against sensory axon loss in peripheral neuropathy. (Nature 2025)

- DOI: 10.1038/s41586-024-08535-1 | PMCID: PMC11964918 | PMID: 39939762
- Evidence: Nonlinear dimensional reduction was carried out using UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, R v4.3.2, Seurat v5.0.1]

### Transcriptomic neuron types vary topographically in function and morphology. (Nature 2025)

- DOI: 10.1038/s41586-024-08518-2 | PMCID: PMC11864986 | PMID: 39939759
- Evidence: We then performed batch correction using Harmony 63 , grouping the variables according to their original batch followed by dimensionality reduction with UMAP 64 .
- Full pipeline: normalisation [ANTs, UMAP] -> registration [Suite2p] -> dimensionality reduction/clustering [SciPy, UMAP, pheatmap, scDblFinder] -> visualisation [pheatmap] -> stage not stated [ImageJ, Monocle, PsychoPy, R, Seurat, napari, scikit-learn]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Evidence: A uniform manifold approximation projection (UMAP) plot is shown in Fig.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Evidence: Bottom, example of an injection-site reaction after vaccination, 48 h after priming. b , Uniform manifold approximation and projection (UMAP) representations of scRNA-seq data of skin-infiltrating myeloid and lymphoid cells before (week 0) and after vaccination (week 4) ( n = 9 patients). c , Boxplot of the proportion of antigen-presenting cells (conventional dendritic cell (DC) subsets DC1 and DC...
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### Left-right-alternating theta sweeps in entorhinal-hippocampal maps of space. (Nature 2025)

- DOI: 10.1038/s41586-024-08527-1 | PMCID: PMC11946909 | PMID: 39900625
- Evidence: Decoding internal direction with PCA or UMAP The internal direction signal was also decoded in an unsupervised manner, with PCA or uniform manifold approximation and projection 80 (UMAP).
- Full pipeline: dimensionality reduction/clustering [Matplotlib, NumPy, Scanpy, SciPy, UMAP, scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5]

### Engineered heart muscle allografts for heart repair in primates and humans. (Nature 2025)

- DOI: 10.1038/s41586-024-08463-0 | PMCID: PMC11903342 | PMID: 39880949
- Evidence: Principal component analysis was performed on the variable genes, and UMAP was run on the top 50 principal components 42 .
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: For the displayed UMAP 98 of the E8.0–E8.25 pair of time points, we used the 30-dimensional Seurat PCA latent space and a k NN graph with k = 15.
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### Multiscale footprints reveal the organization of cis-regulatory elements. (Nature 2025)

- DOI: 10.1038/s41586-024-08443-4 | PMCID: PMC11839466 | PMID: 39843737
- Evidence: The data were projected into two-dimensional space by UMAP 58 .
- Full pipeline: quality control [FastQC v0.25] -> alignment/mapping [FastQC v0.25, PyMOL v2.6] -> quantification [Seurat] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Keras] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, ArchR, MACS2]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Evidence: 2e . d - e ) UMAP showing the subclasses of glutamatergic neurons in the adult mouse cerebrum (left) and the expression of Tfap2d within the subclasses representing the BLC, PIR, AON, CLA 37 . f) Coronal sections of the E17 chicken brain showing Tfap2d (red) expression in the nidopallium and arcopallial amygdala detected by RNAscope.
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### IL-33-activated ILC2s induce tertiary lymphoid structures in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08426-5 | PMCID: PMC11864983 | PMID: 39814891
- Evidence: The ensuing consensus expression was projected onto target cell populations using UMAP and violin plot visualizations.
- Full pipeline: read trimming [Cutadapt, DADA2, Nextflow] -> quantification [QIIME 2] -> normalisation [edgeR] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Seurat] -> visualisation [UMAP] -> stage not stated [GSVA, ImageJ v2.3.0, QuPath v0.2.3]

### GZMK-expressing CD8&lt;sup&gt;+&lt;/sup&gt; T cells promote recurrent airway inflammatory diseases. (Nature 2025)

- DOI: 10.1038/s41586-024-08395-9 | PMCID: PMC11821540 | PMID: 39814882
- Evidence: ...ns in Seurat v.4.3.0.1 were used for cluster prediction and projection of the query onto the reference uniform manifold approximation and projection (UMAP) structure on the basis of the total tissue αβ T cell dataset.
- Full pipeline: quantification [ImageJ, Seurat v3.0.2] -> normalisation [ImageJ] -> dimensionality reduction/clustering [Monocle, Seurat v3.0.2, UMAP] -> differential/statistical testing [CellPhoneDB, DESeq2, Seurat v3.0.2, emmeans] -> simulation/modelling [Monocle] -> visualisation [ggplot2] -> stage not stated [Cutadapt, Cytoscape, R v4.3.3]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Evidence: The resulting nearest-neighbour graph was used to perform UMAP embedding and clustering using the SLM algorithm 55 .
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: 1 Identification of diverse cell states in A. thaliana leaves infected by bacterial pathogens. a , Schematic of the time-course snMultiome analysis. b , Two-dimensional embedding of nuclei from all samples by uniform manifold approximation and projection (UMAP) based on the transcriptomic data.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### A foundation model of transcription across human cell types. (Nature 2025)

- DOI: 10.1038/s41586-024-08391-z | PMCID: PMC11754112 | PMID: 39779852
- Evidence: Resolution was arbitrarily chosen to keep the cluster number around 10 and close to the UMAP density.
- Full pipeline: alignment/mapping [BEDTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [AlphaFold, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [ColabFold, MACS2, PyTorch, STRING db]

### Precursors of exhausted T cells are pre-emptively formed in acute infection. (Nature 2025)

- DOI: 10.1038/s41586-024-08451-4 | PMCID: PMC12003159 | PMID: 39778709
- Evidence: Subsequently, PCA, identification of nearest neighbours and Louvain 40 clustering were performed, followed by UMAP dimensional reduction.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [STAR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSEA, UMAP, edgeR] -> stage not stated [MACS2, Nextflow, R v4.1.0, SAMtools, Seurat v4.0.3, Signac v1.3.0, limma]

### Gliomagenesis mimics an injury response orchestrated by neural crest-like cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08356-2 | PMCID: PMC11821533 | PMID: 39743595
- Evidence: We therefore obtained a new set of PCA embeddings, clusters and UMAP visualizations.
- Full pipeline: quality control [scDblFinder v1.4.0] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat v4.5, UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Slingshot] -> visualisation [Cytoscape v3.9.1, UMAP, igraph] -> stage not stated [ArchR v1.0.1, CellChat v1.1.3, R, Squidpy v1.3.0]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Evidence: Principal component analysis (PCA) was then performed on the size factor-normalized and variance-stabilized count matrix restricted to these genes only, followed by 2D UMAP 46 dimensional reduction based on the resulting top 50 principal components (with correlation distance metric, number of neighbors = 15, and minimum distance = 0.1, and without further PCA scaling).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Evidence: Transcriptomic integration of the scRNA-seq data of organoids from different genotypes To embed all cells from different organoids in the same low-dimensional space and to subsequently visualize them on the UMAP, the data were integrated using Seurat.
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### Timely TGFβ signalling inhibition induces notochord. (Nature 2025)

- DOI: 10.1038/s41586-024-08332-w | PMCID: PMC11735409 | PMID: 39695233
- Evidence: ...C clusters showing induction of HOXB/C9 between 7-10S. b , Embedding of chick trunk (4-13S) coloured by markers of endoderm and surface ectoderm. c , UMAP embedding detail plots highlighting the expression of several genes at and around the NMP cluster.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> stage not stated [PyTorch, R, Scanpy, scDblFinder]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Evidence: We obtained batch-balanced nearest neighbours graph using BBKNN (scanpy.external.pp.bbknn) and then used this neighbours graph to generate a UMAP visualization of all cells (scanpy.tl.umap).
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Skin autonomous antibody production regulates host-microbiota interactions. (Nature 2025)

- DOI: 10.1038/s41586-024-08376-y | PMCID: PMC11864984 | PMID: 39662506
- Evidence: ...s of Lta −/− mice at baseline and 14 days post-TA; cells pooled from 5 mice (TA) and 3 mice (TSB). f , Uniform manifold approximation and projection (UMAP) representation of nine different B cell clusters. g , Normalized expansion profile of individual clusters between TSB and TA treatment.
- Full pipeline: normalisation [R, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v5.0.2]

### Macrophages excite muscle spindles with glutamate to bolster locomotion. (Nature 2025)

- DOI: 10.1038/s41586-024-08272-5 | PMCID: PMC11735391 | PMID: 39633045
- Evidence: PCA and uniform manifold approximation and projection (UMAP) were used for dimensionality reduction and visualization.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1.2] -> visualisation [UMAP] -> stage not stated [DESeq2, ImageJ, ggplot2, scDblFinder]

### RANK drives structured intestinal epithelial expansion during pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-024-08284-1 | PMCID: PMC11666467 | PMID: 39633049
- Evidence: Clustering and UMAP dimensionality reduction were performed with Seurat using similar parameters as in their study, that is, considering the first 25 principal components and a k.param of 20 for FindNeighbors and a resolution of 0.6 in FindClusters.
- Full pipeline: quality control [scDblFinder v1.12.0] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, UMAP, clusterProfiler v4.4.4, fgsea v1.22.0] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler v4.4.4, fgsea v1.22.0] -> stage not stated [ImageJ v2.3.0, R, Seurat v4.0.5, ggplot2, pheatmap]

### Evolution of myeloid-mediated immunotherapy resistance in prostate cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08290-3 | PMCID: PMC11779626 | PMID: 39633050
- Evidence: Leiden clustering (default resolution = 1.0) and UMAP plotting were performed, with a resolution of 1.0 applied for both T cell and myeloid cell clustering.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> stage not stated [ImageJ v2.14.0, MACS2]

### Cancer cells impair monocyte-mediated T cell stimulation to evade immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08257-4 | PMCID: PMC7617236 | PMID: 39604727
- Evidence: The 40 harmony embeddings were used for UMAP visualizations.
- Full pipeline: normalisation [Enrichr, GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> visualisation [UMAP] -> stage not stated [GSVA, MACS2, R v4.2.2, SCENIC, Seurat v4.3.0, scVelo v0.2.5, velocyto v0.17]

### Liver X receptor unlinks intestinal regeneration and tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08247-6 | PMCID: PMC11779645 | PMID: 39567700
- Evidence: For the SI dataset, a primary UMAP was performed using all samples (based on the first 20 components of a principal component analysis (PCA) based on the 2,000 most highly variable genes).
- Full pipeline: quantification [kallisto] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [Enrichr, edgeR] -> stage not stated [Fiji, ImageJ, Python v3.9, QuPath, R v3.6.3, Seurat, scDblFinder]

### A cell atlas foundation model for scalable search of similar human cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08411-y | PMCID: PMC11864978 | PMID: 39566551
- Evidence: ...type annotation (0.02 s per cell). b–d , SCimilarity annotation of a kidney scRNA-seq dataset. b , c , Uniform manifold approximation and projection (UMAP) embedding of cell profiles (dots) from SCimilarity’s latent representation of a held-out kidney dataset 25 coloured by author-provided ( b ) or SCimilarity-predicted ( c ) cell type annotations.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R]

### Evolving antibody response to SARS-CoV-2 antigenic shift from XBB to JN.1. (Nature 2025)

- DOI: 10.1038/s41586-024-08315-x | PMCID: PMC11754117 | PMID: 39510125
- Evidence: Two-tailed Wilcoxon rank-sum tests were used to calculate the P values. c , Uniform manifold approximation and projection (UMAP) visualization of antibody DMS escape mutation profiles.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, ggplot2 v3.3.3, igraph] -> differential/statistical testing [UMAP] -> visualisation [R, UMAP, ggplot2 v3.3.3] -> stage not stated [SciPy]

### Endogenous self-peptides guard immune privilege of the central nervous system. (Nature 2025)

- DOI: 10.1038/s41586-024-08279-y | PMCID: PMC11666455 | PMID: 39476864
- Evidence: Principal component analysis (PCA) was conducted and an elbow plot was used to select components for UMAP analysis and clustering.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, edgeR, limma] -> stage not stated [Seurat]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Evidence: 2c ), we generated projections using the UMAP implementation in Scanpy (v.1.9.1), with min_dist = 0.3–0.5 and init_pos = paga.
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Chromatin accessibility during human first-trimester neurodevelopment. (Nature 2025)

- DOI: 10.1038/s41586-024-07234-1 | PMCID: PMC12589128 | PMID: 38693260
- Evidence: Additionally, a uniform manifold approximation and projection was generated using UMAP-learn 57 with default settings.
- Full pipeline: quality control [scikit-learn] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, HOMER, LDSC, MACS2, MAGMA, NumPy, scDblFinder]

### Whole-cortex in situ sequencing reveals input-dependent area identity. (Nature 2025)

- DOI: 10.1038/s41586-024-07221-6 | PMCID: PMC12589132 | PMID: 38658747
- Evidence: ( D )( E ) UMAP plots of gene expression of cortical excitatory neurons (D) and L5 ET neurons (E) calculated from the 104-gene panel with or without an additional 33 genes.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Universal transcriptomic hallmarks of mammalian ageing and mortality. (Nature 2026)

- DOI: 10.1038/s41586-026-10542-3 | PMCID: PMC13233323 | PMID: 42203874
- Evidence: Cells were annotated using established marker gene panels for brain and kidney cell types 197 – 199 . snRNA-seq data were normalized, subjected to PCA, and visualized with UMAP separately for each organ with Seurat 200 .
- Full pipeline: quality control [ggpubr] -> alignment/mapping [STAR v2.7.11b, featureCounts v2.0.6] -> normalisation [Bioconductor, Scanpy, UMAP, WGCNA, lme4 v1.1.35.3] -> dimensionality reduction/clustering [UMAP, WGCNA, clusterProfiler v4.12.0] -> differential/statistical testing [LightGBM, edgeR v4.2.0, ggpubr, limma, lme4 v1.1.35.3, metafor v4.6, scikit-learn] -> simulation/modelling [edgeR v4.2.0] -> visualisation [Python, UMAP] -> stage not stated [GSEA, NumPy, R, Seurat v5.0.1, fgsea v1.30.0]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Evidence: Control RE ( n = 12), NP ( n = 11) and stress RE ( n = 11). g , Uniform manifold approximation and projection (UMAP) of cell clusters. h , Subclustering of the GABA.2 neuronal population showing reduced Drd1 (top) and Drd2 (bottom) expression in control RE. i , j , Representative images for Drd1 and Drd2 mRNAs in dorsal CA1 ( i ) and DG ( j ).
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Neural representation of action symbols in primate frontal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10297-x | PMCID: PMC13233313 | PMID: 42162420
- Evidence: 7 ), we used the uniform manifold approximation and projection (UMAP), performed on D , using values of 40 and 0.1 for the parameters n_neighbors and min_dist.
- Full pipeline: dimensionality reduction/clustering [Kilosort v2.5, UMAP] -> machine learning [scikit-learn v1.3.0] -> stage not stated [NumPy v1.24.3, SciPy v1.10.1, pandas v2.0.3, seaborn v0.12.2, statsmodels v0.14.0]

### Ecotypes of triple-negative breast cancer in response to chemotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10469-9 | PMCID: PMC13293894 | PMID: 42129561
- Evidence: The top 30 PCA components were used to further perform dimensionality reduction to a two-dimensional space of UMAP.
- Full pipeline: quantification [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> visualisation [survival (R)] -> stage not stated [CellChat, GSVA, MACS2, igraph, limma]

### Eosinophils drive intestinal remodelling and innate defence in reproduction. (Nature 2026)

- DOI: 10.1038/s41586-026-10531-6 | PMCID: PMC13233317 | PMID: 42129565
- Evidence: 2 Lactation promotes goblet cell differentiation through a stem-cell-intrinsic mechanism. a , Uniform manifold approximation and projection (UMAP) plots of scRNA-seq data showing the six IEC subsets and signature genes of each subset.
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [Scanpy v1.8.2]

### Non-invasive profiling of the tumour microenvironment with spatial ecotypes. (Nature 2026)

- DOI: 10.1038/s41586-026-10452-4 | PMCID: PMC13293879 | PMID: 42092150
- Evidence: Strikingly, when visualized using uniform manifold approximation and projection (UMAP), each embedding organized into a spatial gradient, with individual neighbourhoods tracing a trajectory from the tumour core to the adjacent stroma (Fig.
- Full pipeline: alignment/mapping [SAMtools] -> quantification [survival (R) v3.6.4] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.14.6] -> differential/statistical testing [survival (R) v3.6.4] -> simulation/modelling [UMAP] -> machine learning [PyTorch v2.2.0] -> visualisation [UMAP] -> stage not stated [R, Seurat v4.3.0, fgsea v1.25.1, metafor]

### Pervasive and programmed nucleosome distortion on single chromatin fibres. (Nature 2026)

- DOI: 10.1038/s41586-026-10418-6 | PMCID: PMC13253354 | PMID: 42056506
- Evidence: UMAP visualization of footprint types within epigenomic domains and at repeat sequences From accessibility data for footprints within histone-modification-defined domains and at mouse repeat elements, we used Scanpy (v.1.9.3) for principal component analysis (PCA)-based dimensionality reduction, construction of a k -nearest neighbours graph (metric = correlation, n _neighbours = 15) and UMAP visua...
- Full pipeline: dimensionality reduction/clustering [ChimeraX v1.7.1, Python, Scanpy v1.9.3, UMAP] -> visualisation [ChimeraX v1.7.1, Scanpy v1.9.3, UMAP] -> stage not stated [SciPy]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: UMAP coordinates were computed based on the scANVI latent space, and Leiden clustering was performed for annotation.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Early fibrotic niches establish tumour-permissive microenvironments. (Nature 2026)

- DOI: 10.1038/s41586-026-10399-6 | PMCID: PMC13149335 | PMID: 42020743
- Evidence: Cells were clustered using Louvain algorithm and visualized using UMAP.
- Full pipeline: quality control [Scanpy, Seurat] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [CellChat, Fiji, ImageJ, QuPath]

### Focal white matter lesions drive grey matter inflammation and synapse loss. (Nature 2026)

- DOI: 10.1038/s41586-026-10414-w | PMCID: PMC13293868 | PMID: 42020752
- Evidence: For visualization, uniform manifold approximation and projection (UMAP) was computed from the first two dimensions of the neighbour graph.
- Full pipeline: read trimming [Snakemake v7.24.0] -> quantification [ImageJ v1.54p] -> dimensionality reduction/clustering [UMAP] -> visualisation [Bioconductor, ComplexHeatmap, UMAP] -> stage not stated [Python, R, Seurat, igraph]

### A spatial atlas of the healthy human liver from live donors. (Nature 2026)

- DOI: 10.1038/s41586-026-10377-y | PMCID: PMC13216088 | PMID: 41986723
- Evidence: To generate a single-cell uniform manifold approximation and projection (UMAP), the data from both patients were combined.
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> machine learning [QuPath] -> visualisation [Scanpy v1.10.0] -> stage not stated [AnnData, Cellpose, GSEA]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Evidence: UMAP embedding on pseudobulk perturbations Pseudobulk knockdown population whole-transcriptome matrices and ATAC peak count matrices were constructed by aggregating all cells with the same sgRNA identity within each treatment condition.
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Emergence of oncofetal plasticity is ubiquitous in early colorectal cancers. (Nature 2026)

- DOI: 10.1038/s41586-026-10344-7 | PMCID: PMC13233332 | PMID: 41986711
- Evidence: Uniform manifold approximation and projection (UMAP) (30 principal components, min.dist = 0.01) was used for dimensionality reduction.
- Full pipeline: quality control [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> read trimming [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> alignment/mapping [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> variant calling [GATK] -> quantification [FastQC v0.12.1, STAR v2.7.9a, Salmon v1.10.1, Trim Galore] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.8.3] -> differential/statistical testing [DESeq2 v1.38.3, ggplot2 v3.5.1, ggpubr v0.6.0] -> simulation/modelling [Monocle] -> visualisation [ape (R) v5.8] -> stage not stated [GSEA, GSVA v1.46.0, ImageJ, QuPath v0.6.0, R, Seurat v5.0.1, Slingshot, fgsea]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: UMAP embeddings for RNA/ATAC spaces were projected individually for visualization.
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Multiomics and deep learning dissect regulatory syntax in human development. (Nature 2026)

- DOI: 10.1038/s41586-026-10326-9 | PMCID: PMC13216069 | PMID: 41951735
- Evidence: Principal components analysis was performed on the merged object with the consensus features, followed by cell clustering using the Louvain algorithm at a resolution of 0.3 with 50 principal components and uniform manifold approximation and projection (UMAP) embedding.
- Full pipeline: read trimming [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> normalisation [R v4.1.2, Seurat v4.3.0] -> dimensionality reduction/clustering [R v4.1.2, Seurat v4.3.0, UMAP] -> stage not stated [ArchR v1.0.2, BEDTools, Bioconductor, Snakemake v7.15.1]

### Synthetic super-enhancers enable precision viral immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10329-6 | PMCID: PMC13149004 | PMID: 41951744
- Evidence: Distribution of SSE-7–mCherry high cells using UMAP plots of scRNA-seq analysis in E21 cells ( n = 23,384 cells) and E28 cells ( n = 35,879). i , SCENIC analysis to determine TF enrichment across replicate libraries.
- Full pipeline: quantification [ImageJ v2.8] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [ImageJ v2.8] -> stage not stated [BEDTools, HOMER, MACS2, PHENIX, R, SCENIC, scDblFinder]

### Saturation editing of RNU4-2 reveals distinct dominant and recessive disorders. (Nature 2026)

- DOI: 10.1038/s41586-026-10334-9 | PMCID: PMC13253345 | PMID: 41951737
- Evidence: UMAP representation was created using the umap package in R.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python]

### Expansion of outer cortical CUX2 neurons requires adaptations for DNA repair. (Nature 2026)

- DOI: 10.1038/s41586-026-10290-4 | PMCID: PMC13190340 | PMID: 41922774
- Evidence: 4 Loss of ATF4 in cortical NPs leads to global alterations in the DDR. a , b , Uniform manifold approximation and projection (UMAP) of integrated E11.5 snRNA-seq data from Atf4 fl/fl and Emx1-Cre; Atf4 fl/fl cortices, colour-coded by genotype ( a ) and cell type ( b ) ( n = 3 biological repeats). c , Violin plots of normalized expression for selected cell-type marker genes. d – i , Gene-set score ...
- Full pipeline: variant calling [UMAP] -> quantification [ImageJ] -> normalisation [UMAP] -> dimensionality reduction/clustering [R, Scanpy v1.8.1, UMAP, clusterProfiler]

### Androgen activity in the male embryonic hindbrain drives lethal PFA ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10264-6 | PMCID: PMC13083265 | PMID: 41882358
- Evidence: Principal components to use for nearest-neighbour analysis and UMAP dimension reduction were selected using a quantitative elbow plot approach ( https://hbctraining.github.io/scRNA-seq/lessons/elbow_plot_metric.html ).
- Full pipeline: alignment/mapping [DESeq2] -> quantification [ImageJ v1.54g] -> normalisation [DESeq2] -> dimensionality reduction/clustering [SCENIC v0.10.3, UMAP] -> differential/statistical testing [R, ggplot2 v3.4.4] -> simulation/modelling [Monocle v1.3.1] -> structure determination [Python v3.8.2] -> machine learning [UMAP] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Seurat, scDblFinder v2.0.3]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Evidence: For snRNA data, normalization and data scaling were performed on the merged snRNA dataset using SCTransform v.2, followed by principal component analysis (PCA) and uniform manifold approximation and projection (UMAP) dimensionality reduction using the RunPCA and RunUMAP function in Seurat (v.5.1.0).
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### Ectopic NMDAR expression in cancer unmasks germline-encoded autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10278-0 | PMCID: PMC13216075 | PMID: 41882353
- Evidence: The diagram was created using BioRender; Kleeman, S. https://BioRender.com/pw3zhmn (2026). b , Uniform manifold approximation and projection (UMAP) of 211,750 8 × 8 μm bins, annotated with cell type ( n = 8) and the proportion of bins classified into each cell type. c , Low- and high-power TNBC section projections depicting the spatial alignment of cell clusters to haematoxylin and eosin (H&E) sta...
- Full pipeline: alignment/mapping [UMAP, edgeR] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX, PHENIX] -> stage not stated [Fiji, ImageJ, MACS2, QuPath, R, RELION, Seurat]

### Biosynthesis of cinchona alkaloids. (Nature 2026)

- DOI: 10.1038/s41586-026-10227-x | PMCID: PMC13149305 | PMID: 41851462
- Evidence: 3 Discovery and functional characterization of MCC. a , Uniform manifold approximation and projection (UMAP) plot of C. pubescens leaf nuclei with high-quality snRNA-seq data, coloured by cell clusters. b , Gene expression heatmap of C. pubescens known upstream alkaloid biosynthetic genes across cell clusters shown in a .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [OrthoFinder]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Evidence: Principal component analysis, UMAP projection and clustering were performed using Seurat (v5) 47 .
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### B cell imprinting in children impairs antibodies to the haemagglutinin stalk. (Nature 2026)

- DOI: 10.1038/s41586-026-10248-6 | PMCID: PMC13171607 | PMID: 41813896
- Evidence: Downstream analyses were performed in R v.4.2.2 using Seurat (v.4.3.0 or newer), including quality control, data normalization, data scaling, dimension reduction (both linear and nonlinear), clustering, differential expression analysis, batch-effect correction, data visualization, and UMAP generation.
- Full pipeline: quality control [Seurat v4.3.0, UMAP] -> alignment/mapping [Clustal Omega] -> normalisation [Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.3.0, UMAP, fgsea] -> differential/statistical testing [Seurat v4.3.0, UMAP] -> structure determination [Coot v0.9.8, PHENIX] -> visualisation [R v4.2, Seurat v4.3.0, UMAP, ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python]

### Facile induction of immune tolerance by an interleukin-2-TGFβ surrogate agonist. (Nature 2026)

- DOI: 10.1038/s41586-026-10208-0 | PMCID: PMC13190267 | PMID: 41813890
- Evidence: UMAP embedding was computed with 10 principal components, with n.neighbors being 20 and min.dist being 0.1.
- Full pipeline: alignment/mapping [featureCounts] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, featureCounts, fgsea] -> stage not stated [Metascape, SCENIC]

### Intestinal interoceptive dysfunction drives age-associated cognitive decline. (Nature 2026)

- DOI: 10.1038/s41586-026-10191-6 | PMCID: PMC13061634 | PMID: 41813891
- Evidence: Clustering was performed using the FindClusters function of Seurat v.4 at a resolution of 0.25 and visualized using UMAP.
- Full pipeline: quality control [Kraken2] -> read trimming [Trimmomatic v0.39, edgeR] -> alignment/mapping [kallisto v0.46.0] -> quantification [QuPath, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor v3.13] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.32.0, ImageJ, QIIME 2 v2021.2.0, Seurat, ape (R) v5.5, phyloseq, tidyverse v1.0.7, vegan v2.6.4]

### Multidimensional profiling of heterogeneity in supratentorial ependymomas. (Nature 2026)

- DOI: 10.1038/s41586-026-10214-2 | PMCID: PMC13102715 | PMID: 41813893
- Evidence: We began by performing an initial annotation of cell lineages through dimensionality reduction using UMAP and unsupervised Louvain clustering.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0, RSEM v1.3.0] -> quantification [HISAT2 v2.1.0, RSEM v1.3.0] -> normalisation [limma] -> dimensionality reduction/clustering [R v1.6.1, Seurat, UMAP, clusterProfiler] -> differential/statistical testing [edgeR v0.27] -> visualisation [ggplot2 v3.5.0] -> stage not stated [Bioconductor, GSEA, ImageJ]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Evidence: We first clustered and projected the samples on to a low-dimensional space (uniform manifold approximation and projection (UMAP)) in Seurat object.
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### Precancerous niche remodelling dictates nascent tumour persistence. (Nature 2026)

- DOI: 10.1038/s41586-026-10157-8 | PMCID: PMC13148994 | PMID: 41781610
- Evidence: 3 Nascent tumour heterogeneity in the epithelial compartment is linked to stromal remodelling. a , Microdissection of squamous upper gastrointestinal tract 8 months after DEN treatment for single-cell RNA sequencing. b , Uniform manifold approximation and projection (UMAP) showing cell-type annotation.
- Full pipeline: variant calling [R] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [SAMtools, scDblFinder]

### Microbiota-mediated induction of beige adipocytes in response to dietary cues. (Nature 2026)

- DOI: 10.1038/s41586-026-10205-3 | PMCID: PMC13051337 | PMID: 41781619
- Evidence: 73 ) was used for quality control, analysis of individual feature matrices, integrated analysis of all eight samples (dim = 8, resolution = 0.5 for liver, dim = 30, resolution = 1.2 for iWAT) and generation of the UMAP plot.
- Full pipeline: quality control [UMAP] -> read trimming [DADA2, R, Trimmomatic] -> alignment/mapping [SAMtools v1.19.2, STAR v2.7.10b, pheatmap] -> dimensionality reduction/clustering [UMAP, clusterProfiler v1.38.3] -> differential/statistical testing [DESeq2, featureCounts] -> simulation/modelling [Slingshot] -> visualisation [SAMtools v1.19.2, pheatmap] -> stage not stated [AnnData, Canu v2.1.1, Flye v2.9, Python, Seurat v4.3.0, eggNOG, minimap2 v2.24]

### Genome modelling and design across all domains of life with Evo 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10176-5 | PMCID: PMC13128491 | PMID: 41781614
- Evidence: Each point in the UMAP (uniform manifold approximation and projection) graph represents a single genome in the training dataset that is embedded on the basis of the genome’s k -mer frequencies.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HMMER, Pangolin] -> machine learning [AUGUSTUS, UMAP] -> stage not stated [AlphaFold, BLAST, HOMER]

### Human hippocampal neurogenesis in adulthood, ageing and Alzheimer's disease. (Nature 2026)

- DOI: 10.1038/s41586-026-10169-4 | PMCID: PMC13048220 | PMID: 41741649
- Evidence: We computed a UMAP of the ATAC–seq data of our NSC and astrocytes, which revealed that the NSCs have a chromatin structure that is distinct from astrocytes (Extended Data Figs.
- Full pipeline: quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [Seurat, UMAP, scVelo] -> differential/statistical testing [edgeR, limma] -> stage not stated [CellChat, SCENIC, scDblFinder]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Evidence: Next, the batch effect was examined based on the clustering of MCCA batches and reference samples in dimensionality-reduction plots (PCA and UMAP).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Dynamic antigen expression and cytotoxic T cell resistance in HIV reservoir clones. (Nature 2026)

- DOI: 10.1038/s41586-026-10298-w | PMCID: PMC13190302 | PMID: 41735521
- Evidence: Residuals were converted into affinity-based similarities using UMAP.
- Full pipeline: normalisation [Seurat v5.1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> visualisation [limma] -> stage not stated [MACS2]

### Host control of persistent Epstein-Barr virus infection. (Nature 2026)

- DOI: 10.1038/s41586-026-10274-4 | PMCID: PMC13171444 | PMID: 41714741
- Evidence: Tissues sorted by P values, with the purple colour indicating significant enrichment. d , Uniform manifold approximation and projection (UMAP) representation plot of the PBMC single-cell RNA-seq data 50 , coloured by cluster labels of cell-type annotation level 1.
- Full pipeline: alignment/mapping [RSEM v1.3.0, SAMtools v1.20] -> variant calling [REGENIE] -> quantification [RSEM v1.3.0] -> dimensionality reduction/clustering [REGENIE, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [FUMA v1.6.3, MAGMA v1.08, PLINK, R v4.4.2, Seurat, TwoSampleMR v0.6.15, VEP]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Evidence: Log normalization, data scaling, principal component analysis, neighbour calculations, UMAP and Leiden clustering were performed.
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### The integrated stress response promotes immune evasion through lipocalin 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10143-0 | PMCID: PMC13128482 | PMID: 41708864
- Evidence: UMAP, uniform manifold approximation and projection. f , LUMICKS AFS measurements of mLCN2-coated beads binding to BMDMs.
- Full pipeline: quantification [HTSeq, ImageJ, RSEM, TrackMate] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python, SciPy] -> stage not stated [GSEA, Seurat]

### Clinical-grade autonomous cytopathology through whole-slide edge tomography. (Nature 2026)

- DOI: 10.1038/s41586-025-10094-y | PMCID: PMC12979202 | PMID: 41708854
- Evidence: Each panel includes four plots (from left to right): (1) a scatter plot for separating leukocytes and irrelevant objects; (2) a histogram of LSIL probability scores; (3) a histogram of HSIL probability scores; and (4) a uniform manifold approximation and projection (UMAP) plot.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels] -> machine learning [Matplotlib, NumPy, OpenCV, PyTorch, Python v3.10, scikit-learn, seaborn, statsmodels]

### Individualized mRNA vaccines evoke durable T cell immunity in adjuvant TNBC. (Nature 2026)

- DOI: 10.1038/s41586-025-10004-2 | PMCID: PMC13017525 | PMID: 41708868
- Evidence: UMAP, uniform manifold approximation and projection.
- Full pipeline: alignment/mapping [SAMtools v0.1.19, STAR v2.4.2a, Strelka] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30, GSEA] -> stage not stated [MACS2, R, Seurat, fgsea v1.20.0]

### Agouti integrates environmental cues to regulate paternal behaviour. (Nature 2026)

- DOI: 10.1038/s41586-026-10123-4 | PMCID: PMC13019464 | PMID: 41708861
- Evidence: UMAP, uniform manifold and approximation projection.
- Full pipeline: read trimming [R, scDblFinder] -> dimensionality reduction/clustering [Harmony, UMAP] -> stage not stated [DESeq2, Seurat]

### Transferable enantioselectivity models from sparse data. (Nature 2026)

- DOI: 10.1038/s41586-026-10239-7 | PMCID: PMC12999503 | PMID: 41673164
- Evidence: EI, expected improvement. b , Beeswarm plot highlighting the ten most important features contributing to the model’s regression, ordered according to their mean absolute SHAP value. c , UMAP chemical space representation of the ligand space for reaction I.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> stage not stated [Jupyter]

### Atlas-guided discovery of transcription factors for T cell programming. (Nature 2026)

- DOI: 10.1038/s41586-025-09989-7 | PMCID: PMC13017511 | PMID: 41639465
- Evidence: UMAP plots were generated by calculating UMAP embeddings using Seurat and then plotting them as scatter plots using ggplot2.
- Full pipeline: quantification [Seurat] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.0.5, ggplot2] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap, tidyverse] -> stage not stated [GSEA, MACS2, R]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Evidence: Cell clustering was performed using the graph-based Leiden clustering approach in Scanpy, and the results were visualized in two dimensions using UMAP.
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### Rete ridges form via evolutionarily distinct mechanisms in mammalian skin. (Nature 2026)

- DOI: 10.1038/s41586-025-10055-5 | PMCID: PMC12959975 | PMID: 41639458
- Evidence: We used standard quality control metrics to filter out low-quality cells, normalized and scaled data using SCTransform, and performed dimensional reduction using UMAP with the SLM algorithm to identify clusters.
- Full pipeline: quality control [UMAP] -> quantification [Fiji v1.53c, ImageJ v1.53c, R v4.2.2] -> normalisation [UMAP] -> registration [Python v3.8.20] -> dimensionality reduction/clustering [CellChat, ComplexHeatmap, UMAP] -> visualisation [Python v3.8.20, R v4.2.2] -> stage not stated [Monocle, Seurat]

### Tumour-brain crosstalk restrains cancer immunity via a sensory-sympathetic axis. (Nature 2026)

- DOI: 10.1038/s41586-025-10028-8 | PMCID: PMC12935554 | PMID: 41639447
- Evidence: (2026) https://BioRender.com/ujbfywi . f , Uniform manifold approximation and projection for dimension reduction (UMAP) plot showing all VSN clusters from scRNA-seq.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP] -> stage not stated [GSEA, ImageJ, QuPath]

### Ontogeny and transcriptional regulation of Thetis cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10198-z | PMCID: PMC13171621 | PMID: 41634202
- Evidence: Cell clustering was visualized using UMAP computed from the same nearest-neighbour graph as that used for clustering.
- Full pipeline: read trimming [Seurat v4.4.0] -> alignment/mapping [STAR v2.7.11a] -> dimensionality reduction/clustering [ArchR v1.0.3, Scanpy, UMAP] -> visualisation [ArchR v1.0.3, UMAP]

### A cross-population compendium of gene-environment interactions. (Nature 2026)

- DOI: 10.1038/s41586-025-10054-6 | PMCID: PMC12999510 | PMID: 41606330
- Evidence: N = 30,683 and 40,226 for male and female participants, respectively. e , UMAP of the Tabula Sapiens scRNA-seq data.
- Full pipeline: variant calling [IMPUTE2] -> dimensionality reduction/clustering [R, Seurat v4.3.0.1, UMAP] -> differential/statistical testing [MAGMA] -> stage not stated [BCFtools, LDSC v1.0.0, PLINK v2.00a]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Evidence: ( e ) Single cell UMAPs of markers used to differentiate cycling and non-cyling NPCs ( f ) Single cell UMAP coloured by Target-gene presence ( g ) Proportion of cells uniquely expressing gRNAs barcodes for each target within each experiment (n = 18 per Gene comprised of 6 technical replicates, 3 gRNAs barcodes per target, for Controls n = 108: 18 gRNAs across 6 technical replicates).
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### Population-scale sequencing resolves determinants of persistent EBV DNA. (Nature 2026)

- DOI: 10.1038/s41586-025-10020-2 | PMCID: PMC12888827 | PMID: 41606327
- Evidence: 4 EBV DNAemia gene associations at cell and pathway resolutions. a , Uniform manifold approximation and projection (UMAP) embedding of 211,000 PBMCs.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, GATK, SAMtools] -> variant calling [GATK] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC] -> stage not stated [PLINK, R, REGENIE v3.5, Seurat]

### Vagal blood volume receptors compensate for haemorrhage and posture change. (Nature 2026)

- DOI: 10.1038/s41586-025-10010-4 | PMCID: PMC13017543 | PMID: 41606321
- Evidence: UMAP plots UMAP plots were generated by analysis of published single-cell transcriptomic data of vagal sensory neurons 16 using Seurat in R.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [Fiji, ImageJ, ilastik, scikit-image]

### Intestinal macrophages modulate synucleinopathy along the gut-brain axis. (Nature 2026)

- DOI: 10.1038/s41586-025-09984-y | PMCID: PMC12960212 | PMID: 41606336
- Evidence: Representative of more than four experiments. b , Uniform manifold approximation and projection (UMAP) of unsupervised clustering of ME-Macs and T cells from ME assigned into colour-coded subclusters. scRNA-seq data obtained from fluorescence-activated cell-sorted ME-Macs and ME CD3 + cells of 4-month 3KL and WT subjected to 10X Genomics scRNA-seq ( n = 2,748 cells).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [QuPath, R v4.0, SciPy, Seurat v4.3]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Evidence: Dimensional reduction by uniform manifold approximation and projection (UMAP) was recalculated using the integrated lower-dimensional space, using the first 50 principal components and with nearest neighbours set to 15.
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### Scalable and multiplexed recorders of gene regulation dynamics across weeks. (Nature 2026)

- DOI: 10.1038/s41586-026-10156-9 | PMCID: PMC13102694 | PMID: 41588170
- Evidence: Scale bar, 10 μm. d , Uniform manifold approximation and projection (UMAP) plot of time-lagged correlations between pCREB and FOS signals across single cells ( n = 77 CytoTapes from 77 cells, 5 cultures). e , Heatmaps showing time-lagged correlations between pCREB and FOS signals for type 1 (left; n = 35 CytoTapes from 35 cells) and type 2 (right; n = 42 CytoTapes from 42 cells) HEK cells. f , g ,...
- Full pipeline: alignment/mapping [PyMOL] -> dimensionality reduction/clustering [UMAP, scikit-image] -> simulation/modelling [AlphaFold, GROMACS v2021.1] -> stage not stated [ImageJ, PyTorch, napari]

### The transition from monocyte to tissue-resident macrophage requires DHPS. (Nature 2026)

- DOI: 10.1038/s41586-025-09972-2 | PMCID: PMC12999486 | PMID: 41565804
- Evidence: Integrated gene expression matrices were visualized with UMAP 68 as a dimensionality reduction approach.
- Full pipeline: quality control [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> read trimming [Cutadapt v2.8, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> alignment/mapping [Cutadapt v2.8, DESeq2, R, SAMtools v1.10, deepTools v3.3.2, fastp v0.20.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ v1.54f, QuPath, Seurat]

### Dissecting gene regulatory networks governing human cortical cell fate. (Nature 2026)

- DOI: 10.1038/s41586-025-09997-7 | PMCID: PMC12999477 | PMID: 41565813
- Evidence: FACS, fluorescence-activated cell sorting. b , Uniform manifold approximation and projections (UMAPs) of cells collected on day 0 (21,151 cells, n = 2 individuals) and day 7 (116,166 cells, n = 4 individuals), coloured by cell class, individual and sex. c , UMAPs highlighting cells from different timepoints. d , UMAP coloured by supervised cell type, with stacked barplots (bottom) showing cell-typ...
- Full pipeline: quantification [Scanpy, velocyto] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, MACS2, Monocle, SCENIC, scVelo]

### Predatory aggression evolved through adaptations to noradrenergic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-10009-x | PMCID: PMC12960248 | PMID: 41565818
- Evidence: For dimensionality reduction and clustering, the preprocessed training data with n = 106 animals from WT recordings on larvae and bacteria were embedded in three dimensions using UMAP (umap module, Python), using the parameters: n_neighbors = 70, min_dist = 0, repulsion_strength = 4, negative_sample_rate = 15, disconnection_distance = 0.85, n_components = 3.
- Full pipeline: dimensionality reduction/clustering [UMAP, XGBoost] -> machine learning [UMAP, XGBoost] -> stage not stated [ImageJ, scikit-learn]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Evidence: Sequence reads corresponding to ribosomal and global genes were removed, cells filtered according to library size and mitochondrial content, normalized, followed by uniform manifold approximation and projection (UMAP) dimension reduction, clustering (louvain) and cell-cycle analysis using Seurat 75 v.4.1.1.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### Language model-guided anticipation and discovery of mammalian metabolites. (Nature 2026)

- DOI: 10.1038/s41586-025-09969-x | PMCID: PMC12960238 | PMID: 41535467
- Evidence: We then sampled CDDD descriptors for an equal number of known metabolites and generated molecules, then embedded the CDDD descriptors for both sets of molecules into two dimensions with UMAP 77 , using the implementation provided in the R package uwot with the n_neighbors parameter set to 5.
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> machine learning [scikit-learn] -> stage not stated [PyTorch, RDKit]

### Microbiota-induced T cell plasticity enables immune-mediated tumour control. (Nature 2026)

- DOI: 10.1038/s41586-025-09913-z | PMCID: PMC12960244 | PMID: 41535459
- Evidence: Cells were then projected onto a UMAP for visualization 61 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [AlphaFold, MACS2, Seurat v5.1.0]

### The ubiquitin ligase KLHL6 drives resistance to CD8&lt;sup&gt;+&lt;/sup&gt; T cell dysfunction. (Nature 2026)

- DOI: 10.1038/s41586-025-09926-8 | PMCID: PMC12979199 | PMID: 41535474
- Evidence: Leiden clustering and UMAP plots were generated based on selected principal component analysis dimensions.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, Scanpy] -> read trimming [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> alignment/mapping [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> quantification [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, edgeR v3.36.0, limma] -> normalisation [Scanpy, edgeR v3.36.0] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.12.0] -> differential/statistical testing [edgeR v3.36.0] -> stage not stated [GSEA, SciPy]

### Mimicking opioid analgesia in cortical pain circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09908-w | PMCID: PMC12823415 | PMID: 41501467
- Evidence: ( g ) Nebulosa density plot of the IEG panel overlaying the UMAP of cell-type clusters.
- Full pipeline: read trimming [STAR v2.7.1] -> alignment/mapping [STAR v2.7.1] -> dimensionality reduction/clustering [DESeq2, Seurat v4.3, SoupX, UMAP, scDblFinder] -> stage not stated [DeepLabCut]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: Thereafter, batch correction was performed on each individual patient sample using harmony 55 , followed by neighbourhood clustering and uniform manifold approximation and projection (UMAP) embedding of the single cells 56 .
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: UMAP projection and clustering of chromatin loops To construct the input feature matrix for projecting chromatin loops, we calculated the proportion of each ChromHMM state at the loop anchors in each cell line.
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Transient hepatic reconstitution of trophic factors enhances aged immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09873-4 | PMCID: PMC12893904 | PMID: 41407851
- Evidence: ...) and CD4 T cells (clusters: CD4_T activated, CD4_T IFN-responsive, CD4_T memory-like/naive, CD4_T naive and Treg; 39,716 cells) were built and a new UMAP embedding based on the harmony components was calculated.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP, ggplot2] -> machine learning [StarDist] -> visualisation [ggplot2] -> stage not stated [CellPhoneDB, GSEA, R v4.3.2, Squidpy]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: UMAP visualization and Leiden clustering were used to identify the three expected cell types 81 , 82 .
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Evidence: UMAP embedding was used to visualize the data.
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: Back in the cell space, we identified highly variable genes, performed principal component analysis, computed the neighbourhood graph, Leiden clustering 75 and UMAP 76 for visualization in two dimensions.
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Lesion-remote astrocytes govern microglia-mediated white matter repair. (Nature 2026)

- DOI: 10.1038/s41586-025-09887-y | PMCID: PMC12823418 | PMID: 41407858
- Evidence: Data were normalized to 10 4 counts and log-transformed before running principal component analysis and UMAP projection.
- Full pipeline: alignment/mapping [STAR] -> normalisation [ImageJ, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [Enrichr, MACS2, emmeans, scDblFinder, scikit-learn]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Evidence: In addition, we manually confirmed the co-expression of marker genes for predefined cell types or pathways and the program activity of cells in the uniform manifold approximation and projection (UMAP) 93 space.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### Human gut M cells resemble dendritic cells and present gluten antigen. (Nature 2026)

- DOI: 10.1038/s41586-025-09829-8 | PMCID: PMC12872457 | PMID: 41372409
- Evidence: Dimensional reduction was performed using the UMAP method based on the top 20 principal components.
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler v3.14.3] -> visualisation [Seurat v3.1.4] -> stage not stated [Enrichr, Python v3.11.9, R, Scanpy]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Evidence: FlowAI 53 was used for quality control of flow data, followed by dimensionality reduction using the UMAP_R plugin 54 .
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Sustained HIV-1 remission after heterozygous CCR5Δ32 stem cell transplantation. (Nature 2026)

- DOI: 10.1038/s41586-025-09893-0 | PMCID: PMC12916306 | PMID: 41326734
- Evidence: Flow cytometry data were analysed using FlowJo (v.10.8.1; BD Life Sciences) with the UMAP and FlowSOM plugin.
- Full pipeline: alignment/mapping [MUSCLE v3.8.155] -> dimensionality reduction/clustering [R v4.4.1, UMAP] -> stage not stated [MACS2, Seurat]

### CD8&lt;sup&gt;+&lt;/sup&gt; T cell stemness precedes post-intervention control of HIV viraemia. (Nature 2026)

- DOI: 10.1038/s41586-025-09932-w | PMCID: PMC12872466 | PMID: 41326735
- Evidence: ...pitope-specific CD8 + T cells. b , Multi-modal clustering by weighted nearest-neighbours plotted using uniform manifold approximation and projection (UMAP) for dimension reduction. c , Left, cluster frequencies among HIV-specific CD8 + T cells from both pre- and post-intervention samples in controllers and non-controllers and among CMV-specific CD8 + T cells and with cluster annotations based on d...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R, Seurat v5.3.0]

### Correlates of HIV-1 control after combination immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-025-09929-5 | PMCID: PMC12872443 | PMID: 41326736
- Evidence: ...he frequency of TCF-1 + cells within the Ki-67 + non-naive CD8 + T cells at the post-R1 timepoint. e , Uniform manifold approximation and projection (UMAP) analysis of non-naive CD8 + T cells including cells from all participants at the baseline, pre-ATI, pre-R and post-R1 timepoints (left).
- Full pipeline: quality control [FastQC v0.11.2, Trim Galore v0.6] -> read trimming [FastQC v0.11.2, Trim Galore v0.6, edgeR] -> alignment/mapping [Bowtie2 v2.4.2, STAR v2.7.10b] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.3, limma v3.1, lme4]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Evidence: Neighbourhood graph was calculated using scanpy.pp.neighbors using default parameters. scanpy.tl.umap was used for UMAP projection of the data.
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Semantic design of functional de novo genes from a genomic language model. (Nature 2026)

- DOI: 10.1038/s41586-025-09749-7 | PMCID: PMC12804078 | PMID: 41261132
- Evidence: Creation of SynGenome UMAP and Leiden clusters To generate the UMAP, first, a random sample of 50,000 sequences encoding at least one ORF with prompts derived from the CDS was extracted from SynGenome.
- Full pipeline: alignment/mapping [MAFFT v7.526] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [igraph v0.11.6] -> visualisation [ChimeraX, Matplotlib] -> stage not stated [AlphaFold, BLAST, HMMER v3.3.0, Python v3.11.8, SciPy v1.11.4]

### Tumour-reactive heterotypic CD8 T cell clusters from clinical samples. (Nature 2026)

- DOI: 10.1038/s41586-025-09754-w | PMCID: PMC12779571 | PMID: 41261135
- Evidence: 3 Tumour-reactive CD8 + T cells from clusters. a , Diagram of the workflow of the scRNA-seq and scTCR-seq analysis. b , scRNA-seq UMAP of CD8 + T cells, highlighting the main cell states (left) and the average frequencies (right). n = 5 patients.
- Full pipeline: normalisation [Harmony v1.2.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cellpose, GSEA, QuPath, Seurat v4.4.0, fgsea v1.28.0, pandas v2.2.3, scikit-learn v1.5.2]

### Rare genetic variants confer a high risk of ADHD and implicate neuronal biology. (Nature 2026)

- DOI: 10.1038/s41586-025-09702-8 | PMCID: PMC12823435 | PMID: 41224997
- Evidence: PCs from the PCAs were then used to compute a neighbourhood graph generated using the Scanpy function ‘pp.neighbors’, which afterwards was embedded and visualized as a UMAP constructed with the Scanpy function tl.umap.
- Full pipeline: quality control [Hail v0.1, SnpEff v4.3] -> variant calling [GATK] -> quantification [Salmon v1.10.2, edgeR v3.40.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MAGMA] -> visualisation [UMAP] -> stage not stated [AnnData, Enrichr, R, Scanpy]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: Principal components were then further batch-corrected using Harmony (v.1.2.1) 59 algorithm for sample integration, and harmonized components were used as input for Louvain clustering and dimensionality reduction using uniform manifold approximation and projection (UMAP).
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### SIGLEC12 mediates plasma membrane rupture during necroptotic cell death. (Nature 2026)

- DOI: 10.1038/s41586-025-09741-1 | PMCID: PMC12779560 | PMID: 41225007
- Evidence: UMAP plots display gene clusters from Louvain clustering of gene expression across all tissue types or single cell types.
- Full pipeline: quality control [FastQC v0.11.2] -> alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UMAP] -> visualisation [Clustal Omega] -> stage not stated [Fiji, ImageJ]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Evidence: Antibodies used to generate the CD8α + T cell UMAP were as follows: CD49a-BUV395, NK1.1-BUV563, CD8α-RB545, CD8b-BUV661, CD4-BUV805, SLAMF6-BV421, CD103-BV480, CD44-BV510, Ly6C-BV570, KLRG1-BV605, CXCR3-BV650, CD39-BV711, PD1-BV750, CD244-BV785, TCRγδ-BB700, CD1D-tetramer-PE, CXCR6-PeDazzle594, CD69-PE-Cy7, CD45.2-SparkNIR685, CD62L-APCR700, TCRβ-APC-Cy7, CD38-APC-Fire810, granzyme-A-e450, TCF1-AF...
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### Constructing local cell-specific networks from single-cell data. (PNAS 2021)

- DOI: 10.1073/pnas.2113178118 | PMCID: PMC8713783 | PMID: 34903665
- Evidence: ( A ) UMAP of human fetal brain single-cell expression from seven cell types involved in development of excitatory neuron cells, ( B ) with developmental trajectories superimposed.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot, UMAP] -> stage not stated [Python v3.7.6, WGCNA]

### Single-cell quantification of a broad RNA spectrum reveals unique noncoding patterns associated with cell types and states. (PNAS 2021)

- DOI: 10.1073/pnas.2113568118 | PMCID: PMC8713755 | PMID: 34911763
- Evidence: Cells were visualized using the uniform manifold approximation and projection (UMAP) algorithm ( 58 ) of the PC-projected data.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [featureCounts v1.6.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [R, UMAP]

### Immunosuppression and outcomes in adult patients with de novo acute myeloid leukemia with normal karyotypes. (PNAS 2021)

- DOI: 10.1073/pnas.2116427118 | PMCID: PMC8673586 | PMID: 34845035
- Evidence: S3 A and B display Uniform Manifold Approximation and Projection (UMAP) projections of normalized expression data from all cells, labeled by cell type ( 18 ) and sample, respectively.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP]

### Neural networks to learn protein sequence-function relationships from deep mutational scanning data. (PNAS 2021)

- DOI: 10.1073/pnas.2104878118 | PMCID: PMC8640744 | PMID: 34815338
- Evidence: UMAP Projection of Latent Space Each neural network encodes a latent representation of the input in its last internal layer before the output node.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [UMAP] -> stage not stated [NetworkX, TensorFlow]

### Altered cell and RNA isoform diversity in aging Down syndrome brains. (PNAS 2021)

- DOI: 10.1073/pnas.2114326118 | PMCID: PMC8617492 | PMID: 34795060
- Evidence: Clustering and UMAP Visualization.
- Full pipeline: normalisation [Seurat v3.0.3] -> dimensionality reduction/clustering [Monocle v0.2.1, UMAP] -> visualisation [UMAP]

### High-dimensional profiling reveals phenotypic heterogeneity and disease-specific alterations of granulocytes in COVID-19. (PNAS 2021)

- DOI: 10.1073/pnas.2109123118 | PMCID: PMC8501786 | PMID: 34548411
- Evidence: ( C ) Gating strategy for the identification of granulocyte subsets and their UMAP projection is shown on Left .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB]

### Integrated spatial multiomics reveals fibroblast fate during tissue repair. (PNAS 2021)

- DOI: 10.1073/pnas.2110025118 | PMCID: PMC8521719 | PMID: 34620713
- Evidence: ( B ) ( Left ) Uniform manifold approximation and projection (UMAP) embedding showing scRNA-seq data from mouse wound fibroblasts FACS isolated using a lineage-negative sort strategy ( 29 ) from POD 2, POD 7, and POD 14, digitally pooled and clustered in a manner agnostic to POD and inner versus outer wound regions.
- Full pipeline: dimensionality reduction/clustering [ArchR, UMAP]

### Trained innate immunity, long-lasting epigenetic modulation, and skewed myelopoiesis by heme. (PNAS 2021)

- DOI: 10.1073/pnas.2102698118 | PMCID: PMC8545490 | PMID: 34663697
- Evidence: LSI scores were then used for clustering, and a visual representation of the clusters was performed using a UMAP projection.
- Full pipeline: alignment/mapping [SAMtools] -> normalisation [R] -> dimensionality reduction/clustering [ArchR v0.9.5, UMAP] -> differential/statistical testing [R] -> visualisation [ArchR v0.9.5] -> stage not stated [HOMER, MACS2, Seurat]

### Profound Treg perturbations correlate with COVID-19 severity. (PNAS 2021)

- DOI: 10.1073/pnas.2111315118 | PMCID: PMC8449354 | PMID: 34433692
- Evidence: Using the Seurat pipeline ( 52 ), PCs and UMAP coordinates were recomputed for just the CD4 + and CD8 + T cell populations.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Translational targeting of inflammation and fibrosis in frozen shoulder: Molecular dissection of the T cell/IL-17A axis. (PNAS 2021)

- DOI: 10.1073/pnas.2102715118 | PMCID: PMC8488623 | PMID: 34544860
- Evidence: ( B ) Uniform Manifold Approximation and Projection (UMAP) embedding of single-cell RNA sequencing and distribution of immune cells from all shoulder capsule tissue ( n = 7, k = 3,347) and split into shoulder capsule of control ( n = 3, k = 555 and frozen shoulder tissue ( n = 4, k = 2,792).
- Full pipeline: quantification [ImageJ] -> normalisation [Seurat] -> dimensionality reduction/clustering [R, UMAP] -> visualisation [ImageJ]

### Morphological cell profiling of SARS-CoV-2 infection identifies drug repurposing candidates for COVID-19. (PNAS 2021)

- DOI: 10.1073/pnas.2105815118 | PMCID: PMC8433531 | PMID: 34413211
- Evidence: UMAP Embedding.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Fiji, ImageJ] -> stage not stated [CellProfiler, scikit-learn]

### Disabling de novo DNA methylation in embryonic stem cells allows an illegitimate fate trajectory. (PNAS 2021)

- DOI: 10.1073/pnas.2109475118 | PMCID: PMC8463881 | PMID: 34518230
- Evidence: Visualization was performed using the UMAP projection method on the first 18 principal components.
- Full pipeline: alignment/mapping [Picard] -> dimensionality reduction/clustering [Monocle v2.14, UMAP] -> differential/statistical testing [DESeq2, Monocle v2.14, R, edgeR] -> simulation/modelling [Monocle v2.14] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat v3.1.5, Trim Galore]

### Pro-inflammatory T helper 17 directly harms oligodendrocytes in neuroinflammation. (PNAS 2021)

- DOI: 10.1073/pnas.2025813118 | PMCID: PMC8403833 | PMID: 34417310
- Evidence: ( A ) UMAP (uniform manifold approximation and projection) showing the results of SNN clustering and bar chart illustrating the proportion of each cluster across the different conditions (glutamate versus control).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ggplot2]

### Single-nuclear transcriptomics reveals diversity of proximal tubule cell states in a dynamic response to acute kidney injury. (PNAS 2021)

- DOI: 10.1073/pnas.2026684118 | PMCID: PMC8271768 | PMID: 34183416
- Evidence: ( G ) UMAP plot of the integrated IRI and control single-nuclei RNA-sequencing datasets.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [Monocle v0.2.3.0, SCENIC v1.1.2, STAR, UMAP] -> visualisation [Monocle v0.2.3.0, R v3.6.3, Seurat v3.2.2, ggplot2 v3.3.2, tidyverse v1.0.2]

### Characterization of neoantigen-specific T cells in cancer resistant to immune checkpoint therapies. (PNAS 2021)

- DOI: 10.1073/pnas.2025570118 | PMCID: PMC8325261 | PMID: 34285073
- Evidence: UMAP Analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Computing the Riemannian curvature of image patch and single-cell RNA sequencing data manifolds using extrinsic differential geometry. (PNAS 2021)

- DOI: 10.1073/pnas.2100473118 | PMCID: PMC8307776 | PMID: 34272279
- Evidence: These tools, such as IsoMAP ( 9 ), t-SNE ( 10 ), and UMAP ( 11 ), appeal to the ansatz that data points in a high-dimensional ambient space are constrained to lie on a low-dimensional manifold.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [UMAP] -> stage not stated [velocyto]

### Developmental and sexual dimorphic atlas of the prenatal mouse external genitalia at the single-cell level. (PNAS 2021)

- DOI: 10.1073/pnas.2103856118 | PMCID: PMC8237666 | PMID: 34155146
- Evidence: To visually present transcriptional and cell population relationships, we used the Uniform Manifold Approximation and Projection (UMAP) dimensionality reduction algorithm ( 17 ) to plot and label each cell based on hierarchal clustering.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R v3.6, Seurat]

### Early role for a Na<sup>+</sup>,K<sup>+</sup>-ATPase (<i>ATP1A3</i>) in brain development. (PNAS 2021)

- DOI: 10.1073/pnas.2023333118 | PMCID: PMC8237684 | PMID: 34161264
- Evidence: ( Right ) Uniform Manifold Approximation and Projection (UMAP) of 125,943 single cells profiled by Drop-seq.
- Full pipeline: normalisation [Monocle] -> dimensionality reduction/clustering [UMAP] -> stage not stated [PyMOL]

### Transfer transcriptomic signatures for infectious diseases. (PNAS 2021)

- DOI: 10.1073/pnas.2022486118 | PMCID: PMC8179160 | PMID: 34031243
- Evidence: ( A , Bottom ) Uniform Manifold Approximation and Projection (UMAP) of the test dataset using the 50-gene long transfer signature obtained from the respective training dataset shown in Top : prevaccine, preinfectious challenge, and postchallenge.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [UMAP]

### Single-cell analyses of renal cell cancers reveal insights into tumor microenvironment, cell of origin, and therapy response. (PNAS 2021)

- DOI: 10.1073/pnas.2103240118 | PMCID: PMC8214680 | PMID: 34099557
- Evidence: UMAP plot of cell types captured from seven different ccRCC samples, where tumor epithelial cells clustered according to patient, while nontumor cells from different patients clustered according to cell types.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Slingshot] -> stage not stated [GSEA]

### Delineating the heterogeneity of matrix-directed differentiation toward soft and stiff tissue lineages via single-cell profiling. (PNAS 2021)

- DOI: 10.1073/pnas.2016322118 | PMCID: PMC8126831 | PMID: 33941688
- Evidence: ( C , i ) Unsupervised clustering of single-cell transcriptomes of TPM1.7, shTPM1, and DDR Control MSCs (two female donors age 43 and 35) that were cultured for 3 d in basal medium and 3 d in bipotential medium is presented on a Uniform Manifold Approximation and Projection (UMAP) field.
- Full pipeline: quantification [ImageJ, UMAP] -> dimensionality reduction/clustering [UMAP]

### Nonparametric coalescent inference of mutation spectrum history and demography. (PNAS 2021)

- DOI: 10.1073/pnas.2013798118 | PMCID: PMC8166128 | PMID: 34016747
- Evidence: We used msprime ( 32 ) and stdpopsim ( 33 ) for simulations, TensorLy ( 78 ) for NNCP tensor decomposition, umap-learn ( 46 ) for UMAP embedding, and several other standard Python packages.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [UMAP] -> stage not stated [BCFtools, Jupyter, Nextflow, Python]

### Identification of EMT signaling cross-talk and gene regulatory networks by single-cell RNA sequencing. (PNAS 2021)

- DOI: 10.1073/pnas.2102050118 | PMCID: PMC8126782 | PMID: 33941680
- Evidence: Dimensionality reduction and visualization were also performed with the UMAP and t-distributed stochastic neighbor embedding (t-SNE) algorithms.
- Full pipeline: quality control [R, Seurat v3.1.0] -> normalisation [R, Seurat v3.1.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [R, Seurat v3.1.0, UMAP] -> stage not stated [GSVA, fgsea]

### Dnmt3a deficiency in the skin causes focal, canonical DNA hypomethylation and a cellular proliferation phenotype. (PNAS 2021)

- DOI: 10.1073/pnas.2022760118 | PMCID: PMC8072215 | PMID: 33846253
- Evidence: ( A ) UMAP representation of single-cell RNA sequencing data from whole epidermis of two pairs of Krt14 -Cre − × Dnmt3a fl/fl ( Dnmt3a WT ; 10,783 cells) and Krt14 -Cre + × Dnmt3a fl/fl mice ( Dnmt3a KO ;16,324 cells) with unbiased graph-based clustering demonstrating known skin populations represented by lineage defining genes ( Right ), including HFB, uHF, bIFE, sbIFE, and sebaceous gland (Seb),...
- Full pipeline: dimensionality reduction/clustering [UMAP]

### CD11c&lt;sup&gt;+&lt;/sup&gt;CD88&lt;sup&gt;+&lt;/sup&gt;CD317&lt;sup&gt;+&lt;/sup&gt; myeloid cells are critical mediators of persistent CNS autoimmunity. (PNAS 2021)

- DOI: 10.1073/pnas.2014492118 | PMCID: PMC8040603 | PMID: 33785592
- Evidence: Expression was visualized after construction of a Uniform Manifold Approximation and Projection (UMAP) to visualize single cells in two dimensions ( 12 ).
- Full pipeline: normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### A single-cell resolution developmental atlas of hematopoietic stem and progenitor cell expansion in zebrafish. (PNAS 2021)

- DOI: 10.1073/pnas.2015748118 | PMCID: PMC8040670 | PMID: 33785593
- Evidence: After quality control and batch correction, a total of 8,432 single cells from human FL at 13 postconception weeks and 10,010 single cells from zebrafish CHT at 3.5 dpf were integrated and subjected to UMAP analysis ( Fig.
- Full pipeline: quality control [UMAP] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, ImageJ]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Evidence: When performing UMAP dimension reduction on single-cell expression data, we use the size-normalized, log-scaled expression.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### Integration and transfer learning of single-cell transcriptomes via cFIT. (PNAS 2021)

- DOI: 10.1073/pnas.2024383118 | PMCID: PMC7958425 | PMID: 33658382
- Evidence: A Uniform Manifold Approximation and Projection (UMAP) visualization revealed the impact of severe batch effects ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Expansions of adaptive-like NK cells with a tissue-resident phenotype in human lung and blood. (PNAS 2021)

- DOI: 10.1073/pnas.2016580118 | PMCID: PMC7980282 | PMID: 33836578
- Evidence: UMAPs were constructed in FlowJo 10.6.1 using the UMAP plugin.
- Full pipeline: read trimming [Cutadapt v1.14] -> dimensionality reduction/clustering [UMAP]

### Single-cell atlas of developing murine adrenal gland reveals relation of Schwann cell precursor signature to neuroblastoma phenotype. (PNAS 2021)

- DOI: 10.1073/pnas.2022350118 | PMCID: PMC7865168 | PMID: 33500353
- Evidence: The first 25 principal components were used to calculate dimensionality reduction using the UMAP technique.
- Full pipeline: normalisation [R, Seurat, limma] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [featureCounts v1.5.2]

### Pluripotent stem cell-derived epithelium misidentified as brain microvascular endothelium requires ETS factors to acquire vascular fate. (PNAS 2021)

- DOI: 10.1073/pnas.2016950118 | PMCID: PMC7923590 | PMID: 33542154
- Evidence: Principal component analysis was subsequently performed on the integrated sample and after reviewing principal component heatmaps and jackstraw plots UMAP visualization was performed using the top 40 components.
- Full pipeline: quality control [FastQC v0.11.5, R, edgeR] -> read trimming [R, STAR, edgeR] -> alignment/mapping [STAR] -> normalisation [R, edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Major alterations in the mononuclear phagocyte landscape associated with COVID-19 severity. (PNAS 2021)

- DOI: 10.1073/pnas.2018587118 | PMCID: PMC8017719 | PMID: 33479167
- Evidence: Algorithms used for dimensionality reduction were UMAP ( 58 ) ( https://github.com/lmcinnes/umap ) and Phenograph ( 59 ) ( https://github.com/JinmiaoChenLab/Rphenograph ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### Activation of NF-κB and p300/CBP potentiates cancer chemoimmunotherapy through induction of MHC-I antigen presentation. (PNAS 2021)

- DOI: 10.1073/pnas.2025840118 | PMCID: PMC7923353 | PMID: 33602823
- Evidence: ( B ) Uniform manifold approximation and projection (UMAP) representation of total T-cell populations profiled by scRNA-seq.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### SOX2 is required independently in both stem and differentiated cells for pituitary tumorigenesis in &lt;i&gt;p27&lt;/i&gt;-null mice. (PNAS 2021)

- DOI: 10.1073/pnas.2017115118 | PMCID: PMC7896314 | PMID: 33574062
- Evidence: Dataset clustering was performed by generating uniform manifold approximation and projection (UMAP) plots ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### The harsh microenvironment in early breast cancer selects for a Warburg phenotype. (PNAS 2021)

- DOI: 10.1073/pnas.2011342118 | PMCID: PMC7826394 | PMID: 33452133
- Evidence: Visualization of this dataset was performed using uniform manifold approximation and projection (UMAP) projections ( 52 , 53 ) of the high-dimensional dataset and further analyses were overlaid onto this representation.
- Full pipeline: read trimming [R] -> alignment/mapping [featureCounts] -> quantification [featureCounts] -> normalisation [R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> visualisation [UMAP] -> stage not stated [Cutadapt, Enrichr]

### Tuning MPL signaling to influence hematopoietic stem cell differentiation and inhibit essential thrombocythemia progenitors. (PNAS 2021)

- DOI: 10.1073/pnas.2017849118 | PMCID: PMC7812794 | PMID: 33384332
- Evidence: Uniform manifold approximation and projection (UMAP) analysis of scRNA-seq data of cultured HSPCs revealed 10 subclusters among which three larger groups are discernable.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Distinct patterns of cortical manifold expansion and contraction underlie human sensorimotor adaptation. (PNAS 2022)

- DOI: 10.1073/pnas.2209960119 | PMCID: PMC9907098 | PMID: 36538479
- Evidence: ( D ) Visualization of the similarity of connectivity matrices, both before and after centering, using UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Hierarchical unimodal processing within the primary somatosensory cortex during a bimodal detection task. (PNAS 2022)

- DOI: 10.1073/pnas.2213847119 | PMCID: PMC9907144 | PMID: 36534792
- Evidence: The UMAP (Uniform Manifold Approximation and Projection) algorithm considers similarities at both the local and global scales ( 30 , 31 ).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Quality assessment and refinement of chromatin accessibility data using a sequence-based predictive model. (PNAS 2022)

- DOI: 10.1073/pnas.2212810119 | PMCID: PMC9907136 | PMID: 36508674
- Evidence: To visualize the cell clusters, we used Uniform Manifold Approximation and Projection for Dimension Reduction (UMAP) ( 60 ).
- Full pipeline: quality control [Jupyter] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [LDSC, MACS2, featureCounts]

### An abstract categorical decision code in dorsal premotor cortex. (PNAS 2022)

- DOI: 10.1073/pnas.2214562119 | PMCID: PMC9897443 | PMID: 36469775
- Evidence: To corroborate these results with a different approach, we used a nonlinear dimensionality reduction technique known as Uniform Manifold Approximation and Projection (UMAP) ( 36 , 37 ).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Vegf signaling between Müller glia and vascular endothelial cells is regulated by immune cells and stimulates retina regeneration. (PNAS 2022)

- DOI: 10.1073/pnas.2211690119 | PMCID: PMC9897474 | PMID: 36469778
- Evidence: ( B ), UMAP plot showing various retinal cell types in the UV light-damaged retina with gene expression of various Vegf receptors overlayed (red). scRNAseq data are from Hoang et al., 2020.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Robust probabilistic modeling for single-cell multimodal mosaic integration and imputation via scVAEIT. (PNAS 2022)

- DOI: 10.1073/pnas.2214414119 | PMCID: PMC9894175 | PMID: 36459654
- Evidence: We performed Uniform Manifold Approximation and Projection for Dimension Reduction (UMAP) ( 21 ) directly on the learned latent variables for scVAEIT, while a similar UMAP visualization based on the trimodal WNN graph was also shown for Seurat.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat, TensorFlow]

### Comprehensive mapping of alternative polyadenylation site usage and its dynamics at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2113504119 | PMCID: PMC9894249 | PMID: 36454750
- Evidence: Synchronized HeLa cells combined with MDA-MB-468 and unsynchronized Hela cells from the other inlet of IFC were projected on UMAP by Seurat 3.1.5 ( 47 , 48 ) ( SI Appendix , Fig.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trim Galore v0.6.1] -> alignment/mapping [STAR v2.5.2b] -> quantification [HTSeq] -> dimensionality reduction/clustering [Seurat v3.1.5, UMAP] -> differential/statistical testing [DESeq2, R v3.6.0] -> stage not stated [BEDTools, Metascape, Snakemake]

### Identification of aceNKPs, a committed common progenitor population of the ILC1 and NK cell continuum. (PNAS 2022)

- DOI: 10.1073/pnas.2203454119 | PMCID: PMC7614094 | PMID: 36442116
- Evidence: ( A ) Uniform manifold approximation and projection (UMAP) visualization of in vivo aceNKP-derived progeny colored by cluster.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### CTLA-4 on thymic epithelial cells complements Aire for T cell central tolerance. (PNAS 2022)

- DOI: 10.1073/pnas.2215474119 | PMCID: PMC9860321 | PMID: 36409920
- Evidence: ( A ) Uniform manifold approximation and projection (UMAP) plots of scRNA-seq of mTECs from Aire +/+ and Aire −/− mice, shown merged ( Left ) or split by genotype ( Right ).
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.1.0, Seurat, edgeR]

### Specification of neuronal subtypes in the spiral ganglion begins prior to birth in the mouse. (PNAS 2022)

- DOI: 10.1073/pnas.2203935119 | PMCID: PMC9860252 | PMID: 36409884
- Evidence: ( B ) UMAP of 5,441 SGNs collected at E14, E16, E18, or P1 with cluster identities indicated.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Monocle, SCENIC, Seurat v3.2, Slingshot v1.8, scDblFinder v2.0.3]

### Hedgehog-interacting protein acts in the habenula to regulate nicotine intake. (PNAS 2022)

- DOI: 10.1073/pnas.2209870119 | PMCID: PMC9674224 | PMID: 36346845
- Evidence: Shown is a UMAP dimensionality reduction plot of cell clustering based on expression profiles.
- Full pipeline: alignment/mapping [HTSeq, STAR, Scanpy] -> quantification [HTSeq] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Enrichr]

### SLC7A8 is a key amino acids supplier for the metabolic programs that sustain homeostasis and activation of type 2 innate lymphoid cells. (PNAS 2022)

- DOI: 10.1073/pnas.2215528119 | PMCID: PMC9674248 | PMID: 36343258
- Evidence: ( C ) UMAP plots depicting the expression of Slc3a2 and ( D ) Slc7a8 in ILC2s from different organs (single-cell RNA-seq data obtained from the Gene Expression Omnibus under accession no.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Intestinal precursors avoid being misinduced to liver cells by activating Cdx-Wnt inhibition cascade. (PNAS 2022)

- DOI: 10.1073/pnas.2205110119 | PMCID: PMC9659337 | PMID: 36396123
- Evidence: UMAP and t-SNE were used for clustering analysis at a resolution of 0.7 to identify distinct clusters of cells and to visualize the clustering results.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat v3.2]

### Ornithine decarboxylase supports ILC3 responses in infectious and autoimmune colitis through positive regulation of IL-22 transcription. (PNAS 2022)

- DOI: 10.1073/pnas.2214900119 | PMCID: PMC9659397 | PMID: 36279426
- Evidence: ( A ) Uniform manifold approximation and projection (UMAP) of intestinal ILC subsets.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Disruption of proteostasis causes IRE1 mediated reprogramming of alveolar epithelial cells. (PNAS 2022)

- DOI: 10.1073/pnas.2123187119 | PMCID: PMC9618079 | PMID: 36252035
- Evidence: Uniform Manifold Approximation and Projection (UMAP) projection and cluster annotation shows all expected lung epithelial populations in the lungs from both timepoints, with no single cluster dominated by Xist+ cells (signifying cells from the female sample) ( SI Appendix , Fig.
- Full pipeline: quantification [Fiji v1.8.0, ImageJ v1.8.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Slingshot] -> stage not stated [MACS2]

### Deterministic programming of human pluripotent stem cells into microglia facilitates studying their role in health and disease. (PNAS 2022)

- DOI: 10.1073/pnas.2123476119 | PMCID: PMC9618131 | PMID: 36251998
- Evidence: Uniform manifold approximation and projection (UMAP) analysis demonstrated a relatively homogenous MGL population in the 2D monoculture ( Fig.
- Full pipeline: dimensionality reduction/clustering [CellPhoneDB, UMAP]

### Sequestration of gut pathobionts in intraluminal casts, a mechanism to avoid dysregulated T cell activation by pathobionts. (PNAS 2022)

- DOI: 10.1073/pnas.2209624119 | PMCID: PMC9565271 | PMID: 36201539
- Evidence: Dimensionality reduction and visualization on a Uniform Manifold Approximation and Projection (UMAP) (representative experiment in Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Conservation at the uterine-placental interface. (PNAS 2022)

- DOI: 10.1073/pnas.2210633119 | PMCID: PMC9565169 | PMID: 36191208
- Evidence: The cell clusters were then visualized with uniform manifold approximation and projection (UMAP).
- Full pipeline: quality control [R, Seurat v4.1.0] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v3.16.1] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, MACS2]

### Highly sensitive single-cell chromatin accessibility assay and transcriptome coassay with METATAC. (PNAS 2022)

- DOI: 10.1073/pnas.2206450119 | PMCID: PMC9546615 | PMID: 36161934
- Evidence: ( A ) Uniform Manifold Approximation and Projection (UMAP) visualization of cells derived from mouse cerebral cortex ( n = 1,370).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, HTSeq v0.11.2, Picard] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [ArchR, BEDTools, MACS2, Python]

### Geometry of neural computation unifies working memory and planning. (PNAS 2022)

- DOI: 10.1073/pnas.2115610119 | PMCID: PMC9478653 | PMID: 36067286
- Evidence: Nonlinear dimensionality reduction via UMAP (uniform manifold approximation and projection) recapitulated the transition from sensory to contingency representations and showed that contingency and sensory tuning are dominant factors driving unit states in the late- vs. early-delay epoch, respectively ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### LAPTM5 mediates immature B cell apoptosis and B cell tolerance by regulating the WWP2-PTEN-AKT pathway. (PNAS 2022)

- DOI: 10.1073/pnas.2205629119 | PMCID: PMC9457450 | PMID: 36037365
- Evidence: ( E ) UMAP projection of BM B220 + cells with major subsets color coded by assigned cell type showing 2,961 cells from three 56R mice ( Left ) and 3,990 cells from three Laptm5 −/− 56R mice ( Right ).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Maternal IL-33 critically regulates tissue remodeling and type 2 immune responses in the uterus during early pregnancy in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2123267119 | PMCID: PMC9436313 | PMID: 35994660
- Evidence: ( E and H ) Uniform manifold approximation and projection (UMAP) shows unbiased clustering of Il33 + cells from Myo ( E ) or Dec ( H ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ v1.52]

### Metastatic triple negative breast cancer adapts its metabolism to destination tissues while retaining key metabolic signatures. (PNAS 2022)

- DOI: 10.1073/pnas.2205456119 | PMCID: PMC9436376 | PMID: 35994654
- Evidence: ( C ) UMAP plot of all samples in the combined dataset.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Single-cell RNA sequencing uncovers the nuclear decoy lincRNA PIRAT as a regulator of systemic monocyte immunity during COVID-19. (PNAS 2022)

- DOI: 10.1073/pnas.2120680119 | PMCID: PMC9457492 | PMID: 35998224
- Evidence: ( C ) UMAP-plot with color-coded cell populations identified in merged scRNA-seq data.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Inferring gene regulation from stochastic transcriptional variation across single cells at steady state. (PNAS 2022)

- DOI: 10.1073/pnas.2207392119 | PMCID: PMC9407670 | PMID: 35969771
- Evidence: ( B ) UMAP of 13,679 unperturbed K562 single cells across six time points (∼1,000 to 4,000 cells per time point), colored by GATA1 scaled counts.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP]

### The glioblastoma multiforme tumor site promotes the commitment of tumor-infiltrating lymphocytes to the T&lt;sub&gt;H&lt;/sub&gt;17 lineage in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2206208119 | PMCID: PMC9407554 | PMID: 35969754
- Evidence: The function RunUMAP from the Seurat package ( https://doi.org/10.1038/nbt.3192 ) was used to calculate the uniform manifold approximation and projection (UMAP) representation of the data based on the first 20 PCs.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [DESeq2 v1.32.0, GSEA, GSVA, R v4.1.0, ggplot2 v3.3.5, tidyverse v1.0.7]

### DARPP32, a target of hyperactive mTORC1 in the retinal pigment epithelium. (PNAS 2022)

- DOI: 10.1073/pnas.2207489119 | PMCID: PMC9388070 | PMID: 35939707
- Evidence: ( B ) Uniform Manifold Approximation and Projection (UMAP) plot of single-cell clusters of RPE/CH.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Early B cell factor 4 modulates FAS-mediated apoptosis and promotes cytotoxic function in human immune cells. (PNAS 2022)

- DOI: 10.1073/pnas.2208522119 | PMCID: PMC9388157 | PMID: 35939714
- Evidence: RQ, relative quantification; PBMC, peripheral blood mononuclear cells; UMAP, uniform manifold approximation and projection. * P ≤ 0.05 and ** P ≤ 0.01.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Postmitotic accumulation of histone variant H3.3 in new cortical neurons establishes neuronal chromatin, transcriptome, and identity. (PNAS 2022)

- DOI: 10.1073/pnas.2116956119 | PMCID: PMC9371731 | PMID: 35930666
- Evidence: ( A) snRNA-seq of wild-type E14.5 cortex visualized by Uniform Manifold Approximation and Projection (UMAP).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP]

### A neural network solves, explains, and generates university math problems by program synthesis and few-shot learning at human level. (PNAS 2022)

- DOI: 10.1073/pnas.2123433119 | PMCID: PMC9371704 | PMID: 35917350
- Evidence: We then use uniform manifold approximation and projection (UMAP) ( 18 , 19 ) to reduce the dimensionality of the 175 question embeddings to 2.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Matplotlib, NumPy, Python, SciPy]

### CFI-402257, a TTK inhibitor, effectively suppresses hepatocellular carcinoma. (PNAS 2022)

- DOI: 10.1073/pnas.2119514119 | PMCID: PMC9371652 | PMID: 35914158
- Evidence: To have an overview on the change of tumor-infiltrating immune populations, we analyzed the samples with uniform manifold approximation and projection (UMAP) dimension reduction and overlaid the plots of vehicle control (Ctrl) and CFI-402257-treated mice to visualize the distribution of CD45 + leukocytes on a two-dimensional map ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA]

### Characterization of T cell receptors reactive to HCRT&lt;sub&gt;NH2&lt;/sub&gt;, pHA&lt;sub&gt;273-287&lt;/sub&gt;, and NP&lt;sub&gt;17-31&lt;/sub&gt; in control and narcolepsy patients. (PNAS 2022)

- DOI: 10.1073/pnas.2205797119 | PMCID: PMC9371724 | PMID: 35914171
- Evidence: ( C ) UMAP of antigen-restricted CD4 + T cells of pHA 273–287 , NP 17–31 , and HCRT NH2 using DQ0602 dCODE dextramer.
- Full pipeline: quality control [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP]

### Elevated Myl9 reflects the Myl9-containing microthrombi in SARS-CoV-2-induced lung exudative vasculitis and predicts COVID-19 severity. (PNAS 2022)

- DOI: 10.1073/pnas.2203437119 | PMCID: PMC9388124 | PMID: 35895716
- Evidence: A total of 57,049 single-cell transcriptomes of peripheral blood mononuclear cells (PBMCs) were analyzed, and uniform manifold approximation and projection (UMAP) identified 8 clusters in the PBMCs of 21 COVID-19 patients ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### High-dimensional immune profiling identifies a biomarker to monitor dimethyl fumarate response in multiple sclerosis. (PNAS 2022)

- DOI: 10.1073/pnas.2205042119 | PMCID: PMC9351505 | PMID: 35881799
- Evidence: UMAP visualization was performed on a reduced dataset of equal numbers of cells randomly selected (100,000 cells per condition) utilizing the UMAP package (n_component = 2, n_neighbors = 15/50, n_epochs = 400, min_dist = 0.1/0.8).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ggplot2]

### Cell atlas of the human ocular anterior segment: Tissue-specific and shared cell types. (PNAS 2022)

- DOI: 10.1073/pnas.2200914119 | PMCID: PMC9303934 | PMID: 35858321
- Evidence: ( A ) Clustering of expression profiles pooled for the integrated analysis and visualized by UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ]

### Id3 expression identifies CD4&lt;sup&gt;+&lt;/sup&gt; memory Th1 cells. (PNAS 2022)

- DOI: 10.1073/pnas.2204254119 | PMCID: PMC9303986 | PMID: 35858332
- Evidence: ...eatures_RNA <200 or >3,000, were removed; counts were normalized with FastMNN; and dimensionality reduction and cluster identification were done with UMAP (dims, 1:30), FindNeighbors (dims, 1:30), FindClusters (resolution, 0.6), and FindAllMarkers function with default parameters and min.pct of 0.25 and logfc.threshold of 0.25.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Seurat v3.5.1]

### Ablation of lysophosphatidic acid receptor 1 attenuates hypertrophic cardiomyopathy in a mouse model. (PNAS 2022)

- DOI: 10.1073/pnas.2204174119 | PMCID: PMC9282378 | PMID: 35787042
- Evidence: Louvain clustering and Uniform Manifold Approximation and Projection (UMAP) visualization were performed for identifying subpopulations and visualization.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Fiji, ImageJ, UMAP] -> stage not stated [R v4.0, Seurat v3.1, scDblFinder]

### Early human B cell signatures of the primary antibody response to mRNA vaccination. (PNAS 2022)

- DOI: 10.1073/pnas.2204607119 | PMCID: PMC9282446 | PMID: 35759653
- Evidence: Spectral Flow Cytometry Data Processing for FlowSOM Clustering and UMAP Embedding.
- Full pipeline: dimensionality reduction/clustering [R v4.0.2, UMAP] -> differential/statistical testing [lme4 v1.1.26] -> machine learning [ggplot2 v3.3.3]

### Latent space of a small genetic network: Geometry of dynamics and information. (PNAS 2022)

- DOI: 10.1073/pnas.2113651119 | PMCID: PMC9245618 | PMID: 35737842
- Evidence: Contrary to more-complex dimensionality reduction techniques [such as t-distributed Stochastic Neighbor Embedding (t-SNE) ( 38 ) or Uniform Manifold Approximation and Projection (UMAP) ( 39 )], the relationship between the full system and its low-dimensional latent space projection is mathematically explicit and intuitive.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Single-cell analyses highlight the proinflammatory contribution of C1q-high monocytes to Behçet's disease. (PNAS 2022)

- DOI: 10.1073/pnas.2204289119 | PMCID: PMC9245671 | PMID: 35727985
- Evidence: ( B ) UMAP visualization of 20 unique cell clusters (colors) in PBMCs from four BD patients and four HCs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [UMAP] -> stage not stated [Monocle, SCENIC]

### Isotype-specific plasma cells express divergent transcriptional programs. (PNAS 2022)

- DOI: 10.1073/pnas.2121260119 | PMCID: PMC9231473 | PMID: 35704755
- Evidence: ( B ) Dimensional reduction on index sorted PCs based on surface phenotype using tSNE (see Materials and Methods for details) or ( C ) based on gene-expression distribution using UMAP (see Materials and Methods for details).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Anti-bat ultrasound production in moths is globally and phylogenetically widespread. (PNAS 2022)

- DOI: 10.1073/pnas.2117485119 | PMCID: PMC9231501 | PMID: 35704762
- Evidence: The dimensionality-reduction algorithm UMAP ( 46 ) was used for finding groups of moth sounds with similar features (clusters).
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [MAFFT, R] -> dimensionality reduction/clustering [UMAP] -> structure determination [R] -> stage not stated [IQ-TREE v1.6.2, scikit-learn]

### Transcriptional and functional motifs defining renal function revealed by single-nucleus RNA sequencing. (PNAS 2022)

- DOI: 10.1073/pnas.2203179119 | PMCID: PMC9231607 | PMID: 35696569
- Evidence: ( A ) A single UMAP of the “fly kidney” contains 11 distinct cell clusters that were annotated on the UMAP.
- Full pipeline: alignment/mapping [SCENIC] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat]

### The HDAC inhibitor CI-994 acts as a molecular memory aid by facilitating synaptic and intracellular communication after learning. (PNAS 2022)

- DOI: 10.1073/pnas.2116797119 | PMCID: PMC9295763 | PMID: 35613054
- Evidence: Seurat then performed UMAP clustering and defined clusters.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Nextstrain, UMAP] -> stage not stated [HOMER v4.11, Seurat v4.0.3]

### Single-cell transcriptomic classification of rabies-infected cortical neurons. (PNAS 2022)

- DOI: 10.1073/pnas.2203677119 | PMCID: PMC9295789 | PMID: 35609197
- Evidence: Following quality-control filtering, principal-component analysis (PCA), and unsupervised graph-based clustering of 8,745 rabies-infected and 9,508 uninfected control nuclei, we applied Uniform Manifold Approximation and Projection (UMAP) to visualize gene expression relationships across infection status.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, ImageJ, R v4.1.1, Seurat v4.0, scDblFinder]

### Transcriptome profiling in swine macrophages infected with African swine fever virus at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2201288119 | PMCID: PMC9171760 | PMID: 35507870
- Evidence: ( D ) UMAP plot showing cell types in unexposed and exposed cells.
- Full pipeline: dimensionality reduction/clustering [SCENIC, UMAP]

### Physicochemical classification of organisms. (PNAS 2022)

- DOI: 10.1073/pnas.2122957119 | PMCID: PMC9171632 | PMID: 35500111
- Evidence: Finally, UMAP was performed as implemented in the Python module created by McInnes et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [scikit-learn]

### Three-dimensional imaging for the quantification of spatial patterns in microbiota of the intestinal mucosa. (PNAS 2022)

- DOI: 10.1073/pnas.2118483119 | PMCID: PMC9171773 | PMID: 35476531
- Evidence: Dimension reduction methods t-SNE and UMAP ( 55 , 56 ) were used for dimension reduction to show the relationship between the branches and the cosine pairwise distance metrics.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Calcium channel blockers potentiate gemcitabine chemotherapy  in pancreatic cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2200143119 | PMCID: PMC9170157 | PMID: 35476525
- Evidence: Following sequencing, cell populations were visualized via Seurat’s uniform manifold approximation and projection (UMAP) dimensionality reduction.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat, UMAP]

### Extracellular vesicles from triple negative breast cancer promote pro-inflammatory macrophages associated with better clinical outcome. (PNAS 2022)

- DOI: 10.1073/pnas.2107394119 | PMCID: PMC9169908 | PMID: 35439048
- Evidence: Visualization of the EV-R signature on the scRNA-seq uniform manifold approximation and projection (UMAP) revealed that EV-R-mo-macs mainly resembled a cluster identified as early-macrophages responsive to IFN (Early-MAC-cluster 4) ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [UMAP, pheatmap] -> stage not stated [Enrichr, MACS2, R, Seurat]

### Single cell enhancer activity distinguishes GABAergic and cholinergic lineages in embryonic mouse basal ganglia. (PNAS 2022)

- DOI: 10.1073/pnas.2108760119 | PMCID: PMC9169651 | PMID: 35377797
- Evidence: ( D ) Visualization of single cells by UMAP, colored by mitotic state (green: M, mitotic; orange: PM, postmitotic).
- Full pipeline: dimensionality reduction/clustering [R, Seurat v3.2.2, UMAP] -> visualisation [R, Seurat v3.2.2, UMAP]

### Cellular and transcriptional diversity over the course of human lactation. (PNAS 2022)

- DOI: 10.1073/pnas.2121720119 | PMCID: PMC9169737 | PMID: 35377806
- Evidence: UMI counts were log-normalized and the top 2,000 variable genes were identified with the batch_key parameter set to “sample.” PC analysis was run on scaled data, and a nearest neighbor map was calculated with 15 neighbors and 25 principal components (PCs prior to running Uniform Manifold Approximation and Projection (UMAP) for visualization.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [DESeq2, SciPy, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [Enrichr, R v3.6.2, Scanpy, Seurat, scDblFinder]

### Transport features predict if a molecule is odorous. (PNAS 2022)

- DOI: 10.1073/pnas.2116576119 | PMCID: PMC9169660 | PMID: 35377807
- Evidence: We visualized known odorants ( n = 8,366; https://pyrfume.org ) within the context of this newly defined odor space using uniform manifold approximation and projection (UMAP), available at http://odormap.pyrfume.org .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [R v3.5.3] -> visualisation [UMAP]

### Neutrophil and natural killer cell imbalances prevent muscle stem cell-mediated regeneration following murine volumetric muscle loss. (PNAS 2022)

- DOI: 10.1073/pnas.2111445119 | PMCID: PMC9169656 | PMID: 35377804
- Evidence: Dimensional reduction was performed in Seurat using principal component analysis, then UMAP ( 32 ) followed by community detection using the Louvain algorithm.
- Full pipeline: dimensionality reduction/clustering [UMAP, scVelo] -> simulation/modelling [scVelo] -> visualisation [ggplot2] -> stage not stated [ImageJ, Seurat, velocyto]

### Synchronous spiking of cerebellar Purkinje cells during control of movements. (PNAS 2022)

- DOI: 10.1073/pnas.2118954119 | PMCID: PMC9168948 | PMID: 35349338
- Evidence: ( B ) Clustering of saccade-aligned change in firing rates for all P cells, using the algorithm UMAP ( 70 ).
- Full pipeline: alignment/mapping [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Kilosort]

### Hemogenic and aortic endothelium arise from a common hemogenic angioblast precursor and are specified by the Etv2 dosage. (PNAS 2022)

- DOI: 10.1073/pnas.2119051119 | PMCID: PMC9060440 | PMID: 35333649
- Evidence: Finally, a plot graph was constructed by shared nearest neighbor–based clusters of the subtypes and transformed to UMAP for dimension reduction for intuitive visualization.
- Full pipeline: alignment/mapping [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ImageJ, R v4.0.2, Seurat]

### <i>Drosophila</i> females have an acoustic preference for symmetric males. (PNAS 2022)

- DOI: 10.1073/pnas.2116136119 | PMCID: PMC9060496 | PMID: 35312357
- Evidence: For embedding, we used UMAP (Uniform Manifold Approximation and Projection for Dimension Reduction) ( 53 ) and for clustering, we used HDBSCAN (hierarchical density-based clustering) ( 54 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Python]

### The 103,200-arm acceleration dataset in the UK Biobank revealed a landscape of human sleep phenotypes. (PNAS 2022)

- DOI: 10.1073/pnas.2116729119 | PMCID: PMC8944865 | PMID: 35302893
- Evidence: We applied four methods—principal component analysis (PCA), t-distributed stochastic neighbor embedding (t-SNE), uniform manifold approximation and projection (UMAP), and a combination of PCA and UMAP—to the 21-dimensional data and converted them to 3-dimensional data, resulting in UMAP dividing the dataset into more interpretable clusters than the other methods ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [XGBoost]

### A single factor elicits multilineage reprogramming of astrocytes in the adult mouse striatum. (PNAS 2022)

- DOI: 10.1073/pnas.2107339119 | PMCID: PMC8931246 | PMID: 35254903
- Evidence: UMAP, Uniform Manifold Approximation and Projection.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [SCENIC]

### Nematode ascarosides attenuate mammalian type 2 inflammatory responses. (PNAS 2022)

- DOI: 10.1073/pnas.2108686119 | PMCID: PMC8892368 | PMID: 35210367
- Evidence: Uniform manifold approximation and projection (UMAP) plots revealed a decreased number of Gata3 -expressing Th2 cells in the lungs of mice sensitized with OVA/alum plus ascr#7 ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### CCR8-targeted specific depletion of clonally expanded Treg cells in tumor tissues evokes potent tumor immunity with long-lasting memory. (PNAS 2022)

- DOI: 10.1073/pnas.2114282119 | PMCID: PMC8851483 | PMID: 35140181
- Evidence: Tregs defined by the expression of the Treg-associated genes, such as Foxp3 , detected by single-cell RNA sequencing (RNA-seq) with UMAP dimensional reduction and Leiden grouping ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### A dominant negative variant of <i>RAB5B</i> disrupts maturation of surfactant protein B and surfactant protein C. (PNAS 2022)

- DOI: 10.1073/pnas.2105228119 | PMCID: PMC8832968 | PMID: 35121658
- Evidence: The AT2 cell Uniform Manifold Approximation and Projection (UMAP) clusters from day-1 and 21-mo datasets were identified using marker genes SFTPB and SFTPC ( SI Appendix , Figs.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [UMAP]

### Convergent clonal selection of donor- and recipient-derived CMV-specific T cells in hematopoietic stem cell transplant patients. (PNAS 2022)

- DOI: 10.1073/pnas.2117031119 | PMCID: PMC8833188 | PMID: 35105810
- Evidence: For whole transcriptome analysis, dimensionality reduction using UMAP and clustering was performed on a subset of variable genes.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat v2.3]

### LINEAGE: Label-free identification of endogenous informative single-cell mitochondrial RNA mutation for lineage analysis. (PNAS 2022)

- DOI: 10.1073/pnas.2119767119 | PMCID: PMC8812554 | PMID: 35086932
- Evidence: The final result of clonal identification was presented as t-distributed stochastic neighbor embedding (t-SNE)/Uniform Manifold Approximation and Projection (UMAP) plot as well as heatmap.
- Full pipeline: alignment/mapping [Python, SAMtools v1.9] -> dimensionality reduction/clustering [R, UMAP] -> stage not stated [GSEA, Seurat]

### Identification of genetic risk loci and prioritization of genes and pathways for myasthenia gravis: a genome-wide association study. (PNAS 2022)

- DOI: 10.1073/pnas.2108672119 | PMCID: PMC8812681 | PMID: 35074870
- Evidence: The control subjects were matched to cases using the “nearest” method based on age, gender, and uniform manifold approximation and projection (UMAP) components 1 and 2 to account for population structure.
- Full pipeline: dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Jupyter, LDSC]

### Redox signaling by glutathione peroxidase 2 links vascular modulation to metabolic plasticity of breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2107266119 | PMCID: PMC8872779 | PMID: 35193955
- Evidence: We performed clustering analysis of the cells and used uniform manifold approximation and projection (UMAP) to visualize the clusters shared by the GPx2 KD and control tumor ( 31 ).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [GSEA, UMAP]

### Executioner caspases 3 and 7 are dispensable for intestinal epithelium turnover and homeostasis at steady state. (PNAS 2022)

- DOI: 10.1073/pnas.2024508119 | PMCID: PMC8832966 | PMID: 35105800
- Evidence: ( M ) UMAP of intraepithelial (IEL) cells extracted from three Casp3/7 fl/fl and Casp3/7 ΔIEC ( n = 3 per genotype) mice.
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Deciphering the endometrial niche of human thin endometrium at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2115912119 | PMCID: PMC8872762 | PMID: 35169075
- Evidence: ( B ) UMAP of cells with the associated cell types in samples of normal endometrium ( n = 3).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, CellPhoneDB]

### Epigenetic state determines inflammatory sensing in neuroblastoma. (PNAS 2022)

- DOI: 10.1073/pnas.2102358119 | PMCID: PMC8832972 | PMID: 35121657
- Evidence: Uniform manifold approximation and projection (UMAP) was generated using the Seurat package.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Trimmomatic v0.39] -> quantification [RSEM v1.2.12] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.07, MACS2, R, Seurat, ilastik v1.3.3, scDblFinder]

### Cell-free DNA profiling informs all major complications of hematopoietic cell transplantation. (PNAS 2022)

- DOI: 10.1073/pnas.2113476118 | PMCID: PMC8795552 | PMID: 35058359
- Evidence: ( A ) Uniform manifold approximation and projection (UMAP) dimensional reduction of cell and tissue methylation profiles.
- Full pipeline: alignment/mapping [BLAST, Bismark] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.5]

### Cellular and molecular architecture of submucosal glands in wild-type and cystic fibrosis pigs. (PNAS 2022)

- DOI: 10.1073/pnas.2119759119 | PMCID: PMC8794846 | PMID: 35046051
- Evidence: ( C ) UMAP of 14 cell clusters in scRNA-seq of SMG and surrounding tissues.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat, SoupX, scDblFinder]

### B cell-derived IL-27 promotes control of persistent LCMV infection. (PNAS 2022)

- DOI: 10.1073/pnas.2116741119 | PMCID: PMC8784116 | PMID: 35022243
- Evidence: ( A , Left ) Dimensionality-reduced uniform manifold approximation and projection (UMAP) plot and expression of cluster marker genes.
- Full pipeline: read trimming [Seurat v4.0.3] -> dimensionality reduction/clustering [Seurat v4.0.3, UMAP] -> differential/statistical testing [Seurat v4.0.3] -> stage not stated [ComplexHeatmap, R v4.1.0, ggplot2]

### Pathogenic TNF-α drives peripheral nerve inflammation in an Aire-deficient model of autoimmunity. (PNAS 2022)

- DOI: 10.1073/pnas.2114406119 | PMCID: PMC8795502 | PMID: 35058362
- Evidence: ( B ) UMAP plot showing clusters of DAPI − CD45 + cells ( n = 11,640) from integrated peripheral nerve samples of NOD.Aire GW/+ mice ( n = 3).
- Full pipeline: normalisation [GSEA] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [CellChat, Seurat]

### Neuronal identities derived by misexpression of the POU IV sensory determinant in a protovertebrate. (PNAS 2022)

- DOI: 10.1073/pnas.2118817119 | PMCID: PMC8794889 | PMID: 35042818
- Evidence: For cells in the control embryos, 10 PCs were used as inputs to UMAP (Uniform Manifold Approximation and Projection) dimension reduction.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> stage not stated [Seurat v2.3.4]

### A virus-specific monocyte inflammatory phenotype is induced by SARS-CoV-2 at the immune-epithelial interface. (PNAS 2022)

- DOI: 10.1073/pnas.2116853118 | PMCID: PMC8740714 | PMID: 34969849
- Evidence: ( C ) Two-dimensional UMAP representation of CD14+ monocyte single cell RNAseq (scRNAseq) extracted from GSE150728 ( 15 ).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Unsupervised embedding of trajectories captures the latent structure of scientific migration. (PNAS 2023)

- DOI: 10.1073/pnas.2305414120 | PMCID: PMC10756268 | PMID: 38134198
- Evidence: To explore the topological structure of the embedding, we use a topology-based dimensionality reduction method [UMAP ( 62 )] to obtain a two-dimensional representation of the embedding space ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### ENPP1 is an innate immune checkpoint of the anticancer cGAMP-STING pathway in breast cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2313693120 | PMCID: PMC10756298 | PMID: 38117852
- Evidence: ( D ) UMAP plots of the annotated clusters of ENPP1 T238A-OE and ENPP1 WT-OE 4T1 primary tumors and metastasis colonized lungs.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP]

### A distinct human cell type expressing MHCII and RORγt with dual characteristics of dendritic cells and type 3 innate lymphoid cells. (PNAS 2023)

- DOI: 10.1073/pnas.2318710120 | PMCID: PMC10756205 | PMID: 38109523
- Evidence: After in silico removal of RORC – cells, the remaining RORC + cells projected onto a Uniform Manifold Approximation and Projection (UMAP) clustered into 7 populations ( Fig.
- Full pipeline: dimensionality reduction/clustering [ArchR, Seurat, UMAP] -> stage not stated [scVelo]

### Antigen perception in T cells by long-term Erk and NFAT signaling dynamics. (PNAS 2023)

- DOI: 10.1073/pnas.2308366120 | PMCID: PMC10756264 | PMID: 38113261
- Evidence: We then performed UMAP dimensionality reduction and clustering of the cells ( 70 , 71 ) ( Fig.
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> quantification [Monocle v1.2.9] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Monocle v1.2.9]

### Genetic and immune determinants of &lt;i&gt;E. coli&lt;/i&gt; liver abscess formation. (PNAS 2023)

- DOI: 10.1073/pnas.2310053120 | PMCID: PMC10743367 | PMID: 38096412
- Evidence: Data were then integrated with FindIntegrationAnchors and IntegrateData, after which PCA (RunPCA), cluster identification (FindNeighbors, dims = 1:15, and FindClusters), and UMAP (RunUMAP, reduction “pca”, n.neighbors = 20, min.dist = 0.3, spread = 1, metric = “Euclidean”) was performed.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v4.3, scDblFinder]

### The USP7-STAT3-granzyme-Par-1 axis regulates allergic inflammation by promoting differentiation of IL-5-producing Th2 cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302903120 | PMCID: PMC10710068 | PMID: 38015852
- Evidence: Specifically, we log-normalized the expression matrix, regressed the data against the total number of unique molecular identifiers (UMIs) detected per cell, performed principal component analysis (PCA), and used PCA dimensions 1 to 4 to find clusters on a UMAP.
- Full pipeline: alignment/mapping [Bowtie2, Cufflinks v2.0.2, HOMER, SAMtools, TopHat v1.3.2, deepTools v2.0] -> quantification [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Monocle] -> visualisation [Cytoscape v3.7.1, MACS2] -> stage not stated [Seurat]

### Single-cell insights into epithelial morphogenesis in the neonatal mouse uterus. (PNAS 2023)

- DOI: 10.1073/pnas.2316410120 | PMCID: PMC10710066 | PMID: 38019863
- Evidence: Cells were clustered with FindNeighbors and FindClusters with a resolution of 0.2, then subjected to UMAP nonlinear dimensional reduction to identify cell populations.
- Full pipeline: quality control [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, UMAP] -> differential/statistical testing [Monocle] -> simulation/modelling [Monocle]

### Deletion of Vβ3&lt;sup&gt;+&lt;/sup&gt;CD4&lt;sup&gt;+&lt;/sup&gt; T cells by endogenous mouse mammary tumor virus 3 prevents type 1 diabetes induction by autoreactive CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2023)

- DOI: 10.1073/pnas.2312039120 | PMCID: PMC10710095 | PMID: 38015847
- Evidence: A dimensionality reduction analysis of recovered CD4 + T cells with a full TCR αβ chain pair revealed 11 distinct clusters by Uniform Manifold Approximation and Projection (UMAP) visualization ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Single-cell bisulfite-free 5mC and 5hmC sequencing with high sensitivity and scalability. (PNAS 2023)

- DOI: 10.1073/pnas.2310367120 | PMCID: PMC10710054 | PMID: 38011566
- Evidence: ( E ) Uniform Manifold Approximation and Projection for Dimension Reduction (UMAP) figure showing the clustering of K562 cells and stomach cells after sequenced by sci-Cabernet.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, MACS2, RepeatMasker, Seurat, deepTools]

### Epigenetic switch reshapes epithelial progenitor cell signatures and drives inflammatory pathogenesis in hidradenitis suppurativa. (PNAS 2023)

- DOI: 10.1073/pnas.2315096120 | PMCID: PMC10710069 | PMID: 38011564
- Evidence: Data were visualized with uniform manifold approximation and projection (UMAP) and colored according to unsupervised clustering.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [CellChat] -> visualisation [CellChat, HOMER, UMAP]

### DNA language models are powerful predictors of genome-wide variant effects. (PNAS 2023)

- DOI: 10.1073/pnas.2311219120 | PMCID: PMC10622914 | PMID: 37883436
- Evidence: UMAP was run with default parameters.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [VEP]

### MHC class Ib-restricted CD8<sup>+</sup> T cells possess strong tumoricidal activities. (PNAS 2023)

- DOI: 10.1073/pnas.2304689120 | PMCID: PMC10614629 | PMID: 37856544
- Evidence: Interestingly, in the UMAP plot, the top ten splenic Ib-CD8 + T cell clones with high TCR frequency were also projected on cluster 4 ( Figs.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP]

### Complete miRNA-15/16 loss in mice promotes hematopoietic progenitor expansion and a myeloid-biased hyperproliferative state. (PNAS 2023)

- DOI: 10.1073/pnas.2308658120 | PMCID: PMC10614620 | PMID: 37844234
- Evidence: Downstream analysis and UMAP visualization were performed using Seurat 4.0.
- Full pipeline: dimensionality reduction/clustering [Monocle, Seurat v4.0, UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> simulation/modelling [Monocle] -> visualisation [Seurat v4.0, UMAP] -> stage not stated [GSEA, ImageJ, SCENIC]

### The developmental hierarchy and scarcity of replicative slender trypanosomes in blood challenges their role in infection maintenance. (PNAS 2023)

- DOI: 10.1073/pnas.2306848120 | PMCID: PMC10589647 | PMID: 37824530
- Evidence: ( A ) UMAP plots of cell transcriptomes at day 7 and day 23 p.i., ±dox induction of HYP2 RNAi.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Seurat v4.1.0, SoupX]

### Trajectories through semantic spaces in schizophrenia and the relationship to ripple bursts. (PNAS 2023)

- DOI: 10.1073/pnas.2305290120 | PMCID: PMC10589662 | PMID: 37816054
- Evidence: ( C ) Initial word lists for 3 PScz visualized as trajectories through semantic space [3-dimensional projection derived from Uniform Manifold Approximation and Projection (UMAP) algorithm ( 41 ) applied to [item, 300] embedding matrix using cosine distance in ambient space.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [UMAP] -> visualisation [UMAP]

### Loss of PPARγ activity characterizes early protumorigenic stromal reprogramming and dictates the therapeutic window of opportunity. (PNAS 2023)

- DOI: 10.1073/pnas.2303774120 | PMCID: PMC10589683 | PMID: 37816052
- Evidence: UMAP projection of cell clusters is shown.
- Full pipeline: read trimming [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.1] -> stage not stated [ImageJ]

### Targeting MFGE8 secreted by cancer-associated fibroblasts blocks angiogenesis and metastasis in esophageal squamous cell carcinoma. (PNAS 2023)

- DOI: 10.1073/pnas.2307914120 | PMCID: PMC10589644 | PMID: 37816055
- Evidence: After quality filtering and doublet removal, 531,143 cells underwent principal component analysis and UMAP algorithm in Seurat software, revealing distinct cell clusters.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### Normal and Sjogren's syndrome models of the murine lacrimal gland studied at single-cell resolution. (PNAS 2023)

- DOI: 10.1073/pnas.2311983120 | PMCID: PMC10589653 | PMID: 37812717
- Evidence: Eleven principal cell clusters were identified with Seurat, and their identities were assigned by reference to published data on the lacrimal gland and other tissues, as seen in the Uniform Manifold Approximation and Projection (UMAP) plots in Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### Endothelial deletion of EPH receptor A4 alters single-cell profile and Tie2/Akap12 signaling to preserve blood-brain barrier integrity. (PNAS 2023)

- DOI: 10.1073/pnas.2204700120 | PMCID: PMC10576133 | PMID: 37796990
- Evidence: ( A ) Cortical cells from iWT and iKO are clustered based on RNA gene expression in a Uniform Manifold Approximation and Projection (UMAP) plot.
- Full pipeline: quality control [FastQC, Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [Trim Galore, scDblFinder]

### Divergent roles for STAT4 in shaping differentiation of cytotoxic ILC1 and NK cells during gut inflammation. (PNAS 2023)

- DOI: 10.1073/pnas.2306761120 | PMCID: PMC10556635 | PMID: 37756335
- Evidence: UMAP shows the transcriptional states of lilp NK cells, ILC1, and ILC3 identified by scRNA-seq.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [GSEA]

### Cell type-specific cytonuclear coevolution in three allopolyploid plant species. (PNAS 2023)

- DOI: 10.1073/pnas.2310881120 | PMCID: PMC10556624 | PMID: 37748065
- Evidence: ( Q and R ) Uniform manifold approximation and projection (UMAP) visualization of pseudotemporal development trajectory of cotton fiber as predicted by −1 to 0 dpa ( Q ) and −2 to 2 dpa ( R ) sc-RNA data.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle, UMAP] -> structure determination [Monocle] -> visualisation [UMAP] -> stage not stated [OrthoFinder]

### Spatial transcriptomics reveals light-induced chlorenchyma cells involved in promoting shoot regeneration in tomato callus. (PNAS 2023)

- DOI: 10.1073/pnas.2310163120 | PMCID: PMC10515167 | PMID: 37703282
- Evidence: Clustering results were displayed by UMAP dimension reduction analysis.
- Full pipeline: quality control [R, Seurat v4.1.0] -> alignment/mapping [STAR] -> normalisation [R, Seurat v4.1.0] -> dimensionality reduction/clustering [R, Seurat v4.1.0, UMAP, clusterProfiler] -> stage not stated [Monocle, velocyto]

### <i>Hey2</i> enhancer activity defines unipotent progenitors for left ventricular cardiomyocytes in juxta-cardiac field of early mouse embryo. (PNAS 2023)

- DOI: 10.1073/pnas.2307658120 | PMCID: PMC10500178 | PMID: 37669370
- Evidence: Cells were divided into 15 clusters based on differentially expressed genes reported in a previous study ( 40 ), as shown in the UMAP plot ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, UMAP] -> stage not stated [R, Seurat v4.0.4]

### IL-6 trans-signaling in a humanized mouse model of scleroderma. (PNAS 2023)

- DOI: 10.1073/pnas.2306965120 | PMCID: PMC10500188 | PMID: 37669366
- Evidence: Uniform Manifold Approximation and Projection (UMAP) embedding of the single-cell cDNA identified 5 cell clusters of human cells, including CD4 and CD8 T cells, monocytes, pericytes, and a population of proliferating cells ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Metascape, edgeR] -> stage not stated [Seurat]

### Rationally designed chimeric PI3K-BET bromodomain inhibitors elicit curative responses in MYC-driven lymphoma. (PNAS 2023)

- DOI: 10.1073/pnas.2306414120 | PMCID: PMC10483632 | PMID: 37643213
- Evidence: ( I ) Uniform Manifold Approximation and Projection (UMAP) plots for the expression of MYC, HEXIM1, and KLF2 in OPM2 cells treated with 500 nM each of JQ1, BKM120, JQ1+BKM120, 18D S, or vehicle for 2 h prior to single-cell RNASeq analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Cell type-specific attenuation of brassinosteroid signaling precedes stomatal asymmetric cell division. (PNAS 2023)

- DOI: 10.1073/pnas.2303758120 | PMCID: PMC10483622 | PMID: 37639582
- Evidence: Normalization of the raw counts, detection of highly variable genes, discovery of clusters, and creation of UMAP plots were done by means of the Seurat pipeline (version 4.0.3).
- Full pipeline: quantification [ImageJ] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, Slingshot, UMAP] -> stage not stated [R]

### IL-15 synergizes with CD40 agonist antibodies to induce durable immunity against bladder cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2306782120 | PMCID: PMC10467355 | PMID: 37607227
- Evidence: Clusters were calculated, and data dimensions were reduced using the t-SNE and UMAP methods.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### Daam2 phosphorylation by CK2α negatively regulates Wnt activity during white matter development and injury. (PNAS 2023)

- DOI: 10.1073/pnas.2304112120 | PMCID: PMC10469030 | PMID: 37607236
- Evidence: ( B ) OPC/OL clusters were visualized by dimension reduction plot, Uniform Manifold Approximation and Projection (UMAP).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ]

### A persistent major mutation in canonical jasmonate signaling is embedded in an herbivory-elicited gene network. (PNAS 2023)

- DOI: 10.1073/pnas.2308500120 | PMCID: PMC10466192 | PMID: 37607232
- Evidence: ( D ) UMAP clustering was performed on the OS-induced transcriptomes of N. attenuata natural accessions, and colored based on the modules returned by the coexpression analysis in panel A .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [emmeans]

### SoxC transcription factors shape the epigenetic landscape to establish competence for sensory differentiation in the mammalian organ of Corti. (PNAS 2023)

- DOI: 10.1073/pnas.2301301120 | PMCID: PMC10450657 | PMID: 37585469
- Evidence: Cells were visualized using uniform manifold approximation and projection (UMAP) plots after clustering and dimension reduction.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [HOMER]

### <i>Ret</i> deficiency decreases neural crest progenitor proliferation and restricts fate potential during enteric nervous system development. (PNAS 2023)

- DOI: 10.1073/pnas.2211986120 | PMCID: PMC10451519 | PMID: 37585461
- Evidence: UMAP was performed on 419 high-dispersion genes using the Umapr R package ( 82 , 83 ).
- Full pipeline: alignment/mapping [HISAT2 v2.0.1] -> quantification [CellProfiler, Cufflinks v2.2.1] -> normalisation [Cufflinks v2.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Monocle, R] -> stage not stated [GSEA, SAMtools v1.2, velocyto]

### Transcriptomic analysis of the ocular posterior segment completes a cell atlas of the human eye. (PNAS 2023)

- DOI: 10.1073/pnas.2306153120 | PMCID: PMC10450437 | PMID: 37566633
- Evidence: ( B ) Clustering of single-nucleus expression profiles from all tissues visualized by UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### XCR1 expression distinguishes human conventional dendritic cell type 1 with full effector functions from their immediate precursors. (PNAS 2023)

- DOI: 10.1073/pnas.2300343120 | PMCID: PMC10438835 | PMID: 37566635
- Evidence: We then incorporated XCR1 into our flow cytometry panel and performed a high-dimensional analysis of the human DC compartment using Uniform Manifold Approximation and Projection ( 41 ) for dimension reduction (UMAP, Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> stage not stated [GSEA, MACS2, Seurat]

### sccomp: Robust differential composition and variability analysis for single-cell data. (PNAS 2023)

- DOI: 10.1073/pnas.2203828120 | PMCID: PMC10438834 | PMID: 37549298
- Evidence: ( A ) UMAP projection of cells for three breast cancer conditions (subtypes).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor] -> machine learning [R] -> stage not stated [Seurat, Stan, limma, tidyverse]

### DNA methylation in the mouse cochlea promotes maturation of supporting cells and contributes to the failure of hair cell regeneration. (PNAS 2023)

- DOI: 10.1073/pnas.2300839120 | PMCID: PMC10438394 | PMID: 37549271
- Evidence: Single-cell data were clustered using “uniform manifold approximation and projection” (UMAP) and “weighted-nearest neighbor” (WNN) using the Seurat R package, which integrates both the gene expression and the accessibility information to define a “joint” cellular state ( 55 ).
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP]

### NMDA-driven dendritic modulation enables multitask representation learning in hierarchical sensory processing pathways. (PNAS 2023)

- DOI: 10.1073/pnas.2300558120 | PMCID: PMC10410730 | PMID: 37523562
- Evidence: ( E ) UMAP projections of the hidden, task-modulated representations from CIFAR-10 for the TMCL-trained network.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [UMAP] -> stage not stated [PyTorch]

### Chromatin conformational changes at human satellite II contribute to the senescence phenotype in the tumor microenvironment. (PNAS 2023)

- DOI: 10.1073/pnas.2305046120 | PMCID: PMC10410700 | PMID: 37523559
- Evidence: To perform UMAP analysis, we used ArchR's “addUMAP()” function after filtering out doublets.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ArchR v1.0.2]

### Data-driven large-scale genomic analysis reveals an intricate phylogenetic and functional landscape in J-domain proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2218217120 | PMCID: PMC10410713 | PMID: 37523524
- Evidence: Dimensionality Reduction of JDP Amino Acid Sequences by UMAP.
- Full pipeline: alignment/mapping [MAFFT v7.487] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold]

### Quantifying common and distinct information in single-cell multimodal data with Tilted Canonical Correlation Analysis. (PNAS 2023)

- DOI: 10.1073/pnas.2303647120 | PMCID: PMC10410705 | PMID: 37523521
- Evidence: ( A ) Summary of the bone marrow CITE-seq dataset, showing either the UMAP of the RNA or protein modality, where cells are colored by the annotated cell types.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Slingshot]

### Resolvin D1 prevents injurious neutrophil swarming in transplanted lungs. (PNAS 2023)

- DOI: 10.1073/pnas.2302938120 | PMCID: PMC10400944 | PMID: 37487095
- Evidence: Briefly, clusters were annotated into major cell populations, each major cell type was subsetted, and renormalized, PCA, Uniform Manifold Approximation and Projection (UMAP) embedding, clustering, and DE analysis performed.
- Full pipeline: quality control [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [Enrichr, ggpubr] -> stage not stated [Seurat v4.0.0]

### Neuronal diversity of neuropeptide signaling, including galanin, in the mouse locus coeruleus. (PNAS 2023)

- DOI: 10.1073/pnas.2222095120 | PMCID: PMC10401028 | PMID: 37487094
- Evidence: We then used uniform manifold approximation and projection (UMAP) to reduce the dimensions of this dataset ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Functional interrogation of lymphocyte subsets in alopecia areata using single-cell RNA sequencing. (PNAS 2023)

- DOI: 10.1073/pnas.2305764120 | PMCID: PMC10629527 | PMID: 37428932
- Evidence: ( B ) UMAP of scRNAseq data from ( A ) split across disease condition.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA]

### A preparative small-molecule mimic of liver CYP450 enzymes in the aliphatic C-H oxidation of carbocyclic <i>N</i>-heterocycles. (PNAS 2023)

- DOI: 10.1073/pnas.2300315120 | PMCID: PMC10629554 | PMID: 37428920
- Evidence: Uniform Manifold Approximation and Projection (UMAP) ( 72 ), a reliable technique that provides a low dimensional representation of multidimensional data, was used to visualize substrates of the C–H oxidation methods (colored) before and after Mn(CF 3 -PDP) 1 compared to drug-like chemical space (gray) ( Figs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [RDKit]

### Decoupling of catalysis and transition state analog binding from mutations throughout a phosphatase revealed by high-throughput enzymology. (PNAS 2023)

- DOI: 10.1073/pnas.2219074120 | PMCID: PMC10629569 | PMID: 37428919
- Evidence: Multiparameter Data Visualization Using UMAP.
- Full pipeline: dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [UMAP] -> stage not stated [Python]

### A cellular and molecular spatial atlas of dystrophic muscle. (PNAS 2023)

- DOI: 10.1073/pnas.2221249120 | PMCID: PMC10629561 | PMID: 37410813
- Evidence: Uniform Manifold Approximation and Projection (UMAP) was initialized in this PCA space to visualize the data on reduced UMAP dimensions.
- Full pipeline: quantification [Python] -> normalisation [Seurat] -> dimensionality reduction/clustering [Python, R, Seurat, Squidpy, UMAP] -> differential/statistical testing [R] -> visualisation [UMAP]

### Functional calcium-responsive parathyroid glands generated using single-step blastocyst complementation. (PNAS 2023)

- DOI: 10.1073/pnas.2216564120 | PMCID: PMC10334775 | PMID: 37379351
- Evidence: Principal component analysis (PCA) was performed using the RunPCA function; uniform manifold approximation and projection (UMAP) was then performed using the RunUMAP function.
- Full pipeline: normalisation [DESeq2, R v4.1, ggplot2] -> dimensionality reduction/clustering [UMAP] -> visualisation [DESeq2, R v4.1, ggplot2] -> stage not stated [Seurat v4.2.1, tidyverse]

### IL-11 induces NLRP3 inflammasome activation in monocytes and inflammatory cell migration to the central nervous system. (PNAS 2023)

- DOI: 10.1073/pnas.2221007120 | PMCID: PMC10293805 | PMID: 37339207
- Evidence: ( B ) The Uniform Manifold Approximation and Projection (UMAP) clustering in 29 immune cell types.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Single-cell transcriptomics reveals maturation of transplanted stem cell-derived retinal pigment epithelial cells toward native state. (PNAS 2023)

- DOI: 10.1073/pnas.2214842120 | PMCID: PMC10293804 | PMID: 37339216
- Evidence: The 13,232 cells were projected into two dimensions by Uniform Manifold Approximation and Projection (UMAP) ( 26 ) using their global gene expression profiles ( Fig.
- Full pipeline: alignment/mapping [R] -> quantification [DESeq2] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [Cytoscape, DESeq2, GSEA] -> simulation/modelling [Scanpy] -> visualisation [Cytoscape, R, Seurat v4.1.1] -> stage not stated [Matplotlib v3.3.2, fgsea, ggplot2 v3.3.6, seaborn v0.11.0]

### Leveraging single-cell RNA sequencing to unravel the impact of aging on stroke recovery mechanisms in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2300012120 | PMCID: PMC10288588 | PMID: 37307473
- Evidence: ( B ) UMAP visualization of a total of 32,446 cells from all 11 nonhemorrhagic sample hemispheres (including sham), clustered into 18 cell types based on core markers shown in Dataset S1 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellChat, R, Seurat]

### Heterogeneous growth of the insula shapes the human brain. (PNAS 2023)

- DOI: 10.1073/pnas.2220200120 | PMCID: PMC10268209 | PMID: 37279278
- Evidence: To better understand this high dimensional dataset, we utilized UMAP (Uniform Manifold Approximation and Projection) to visualize these data, clearly demonstrating a separate clustering of the insula ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib, UMAP, seaborn] -> stage not stated [ANTs, Connectome Workbench, NiBabel, NumPy, Python v3.7]

### Regionally distinct progenitor cells in the lower airway give rise to neuroendocrine and multiciliated cells in the developing human lung. (PNAS 2023)

- DOI: 10.1073/pnas.2210113120 | PMCID: PMC10268599 | PMID: 37279279
- Evidence: With the computed anchors, reference.reduction parameter set to PCA, and reduction.model set to UMAP, the function MapQuery returns the projected UMAP coordinates of the query cells mapped onto the reference UMAP.
- Full pipeline: alignment/mapping [UMAP] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat]

### Tuft cells mediate commensal remodeling of the small intestinal antimicrobial landscape. (PNAS 2023)

- DOI: 10.1073/pnas.2216908120 | PMCID: PMC10266004 | PMID: 37253002
- Evidence: ( B ) Harmonized UMAP plots of ST spots organized by cluster identity ( Left ); corresponding hematoxylin and eosin (H&E)-stained tissue scans with overlaid Seurat clustering ( Right ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Glial dysregulation in the human brain in fragile X-associated tremor/ataxia syndrome. (PNAS 2023)

- DOI: 10.1073/pnas.2300052120 | PMCID: PMC10265985 | PMID: 37252957
- Evidence: ( C ) Cerebellar UMAP plot and dot plot of cell type–specific markers.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> stage not stated [Seurat]

### Principles of nociceptive coding in the anterior cingulate cortex. (PNAS 2023)

- DOI: 10.1073/pnas.2212394120 | PMCID: PMC10265977 | PMID: 37252991
- Evidence: We then used the Uniform Manifold Approximation and Projection (UMAP) algorithm to reduce dimensions in the responsiveness of neurons.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### MicroRNA-205 promotes hair regeneration by modulating mechanical properties of hair follicle stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2220635120 | PMCID: PMC10235966 | PMID: 37216502
- Evidence: After clustering and UMAP dimension reduction, the cluster markers were used to identify distinct cell populations.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v3.0]

### Stem cell decoupling underlies impaired lymphoid development during aging. (PNAS 2023)

- DOI: 10.1073/pnas.2302019120 | PMCID: PMC10236001 | PMID: 37216517
- Evidence: Clustering analysis of the resulting 9,635 cells resulted in 14 clusters visualized in a uniform manifold approximation and projection (UMAP) plot in two dimensions ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### PHGDH preserves one-carbon cycle to confer metabolic plasticity in chemoresistant gastric cancer during nutrient stress. (PNAS 2023)

- DOI: 10.1073/pnas.2217826120 | PMCID: PMC10214193 | PMID: 37192160
- Evidence: Uniform manifold approximation projection (UMAP) visualization of cells is shown after integration.
- Full pipeline: dimensionality reduction/clustering [CellChat, R, SCENIC, Slingshot, UMAP] -> simulation/modelling [Slingshot] -> structure determination [SCENIC] -> visualisation [UMAP] -> stage not stated [GSVA]

### A single-cell multiomic analysis of kidney organoid differentiation. (PNAS 2023)

- DOI: 10.1073/pnas.2219699120 | PMCID: PMC10193973 | PMID: 37155865
- Evidence: We normalized gene expression UMI count data using SCTransform with regressing out percentage of mitochondrial reads (percent.mt) and read count (nCount_RNA) in each cell and performed dimensionality reduction by PCA and UMAP embedding (“dim = 1:50”) with RunPCA and RunUMAP functions, respectively.
- Full pipeline: quantification [UMAP] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.20.0] -> stage not stated [MACS2, R, Signac, scDblFinder]

### Integrated analysis of single-cell chromatin state and transcriptome identified common vulnerability despite glioblastoma heterogeneity. (PNAS 2023)

- DOI: 10.1073/pnas.2210991120 | PMCID: PMC10194019 | PMID: 37155843
- Evidence: Clusters were determined using the Leiden algorithm and visualization using UMAP.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [Enrichr, Monocle] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, Picard, R, Seurat]

### A tessellated lymphoid network provides whole-body T cell surveillance in zebrafish. (PNAS 2023)

- DOI: 10.1073/pnas.2301137120 | PMCID: PMC10193988 | PMID: 37155881
- Evidence: Normalization (SCTransform) and dimensional reduction were done with default parameters in Seurat package prior to clustering and UMAP projection ( 56 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP] -> stage not stated [ImageJ v2.1.0, scDblFinder]

### Direct neuronal reprogramming by temporal identity factors. (PNAS 2023)

- DOI: 10.1073/pnas.2122168120 | PMCID: PMC10175841 | PMID: 37126716
- Evidence: After applying standard quality control filters, and batch correction, we performed dimensional reduction and clustered cells from both conditions using the Uniform Manifold Approximation and Projections (UMAP) ( Fig.
- Full pipeline: quality control [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, Signac] -> stage not stated [Python, Scanpy v1.9.1]

### Stress resilience-enhancing drugs preserve tissue structure and function in degenerating retina via phosphodiesterase inhibition. (PNAS 2023)

- DOI: 10.1073/pnas.2221045120 | PMCID: PMC10175720 | PMID: 37126699
- Evidence: We first utilized Uniform Manifold Approximation and Projection (UMAP) dimensionality reduction to generate a visual representation of transcriptomic differences between individual retinal cells ( 37 ).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Reprogramming by drug-like molecules leads to regeneration of cochlear hair cell-like cells in adult mice. (PNAS 2023)

- DOI: 10.1073/pnas.2215253120 | PMCID: PMC10151514 | PMID: 37068229
- Evidence: ( B ) UMAP plot showing the putative clusters from the integrated analysis of control and Dox groups.
- Full pipeline: dimensionality reduction/clustering [Seurat v3.2, UMAP] -> simulation/modelling [Monocle] -> stage not stated [GSEA]

### Expansion of the sagittal suture induces proliferation of skeletal stem cells and sustains endogenous calvarial bone regeneration. (PNAS 2023)

- DOI: 10.1073/pnas.2120826120 | PMCID: PMC10120053 | PMID: 37040407
- Evidence: ( A – D ) Uniform Manifold Approximation and Projection (UMAP) plot showing unbiased graph-based clusters distribution of all cell populations in sutures isolated from 4-d-old ( A ), 2-mo-old ( B ), 4-mo-old ( C ), and 14-mo-old ( D ) mice.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### microRNA-449a reduces growth hormone-stimulated senescent cell burden through PI3K-mTOR signaling. (PNAS 2023)

- DOI: 10.1073/pnas.2213207120 | PMCID: PMC10083567 | PMID: 36976763
- Evidence: Clustering was performed on the UMAP embedding.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Cholinergic regulation of vascular endothelial function by human ChAT<sup>+</sup> T cells. (PNAS 2023)

- DOI: 10.1073/pnas.2212476120 | PMCID: PMC10083572 | PMID: 36989306
- Evidence: ( C ) Uniform manifold approximation and projection (UMAP) of transcriptomic analysis of single CD4 + cell from patients in circulatory failure ECMO (n = 33).
- Full pipeline: alignment/mapping [Monocle] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [ImageJ] -> stage not stated [MACS2, edgeR]

### Treg cells require Izumo1R to regulate γδT cell-driven inflammation in the skin. (PNAS 2023)

- DOI: 10.1073/pnas.2221255120 | PMCID: PMC10083566 | PMID: 36972453
- Evidence: ( H ) Reanalysis of single-cell RNAseq of spleen and skin Tregs ( 23 , 24 ), UMAP dimensionality reduction plots color coded for expression of Izumo1r ( Top ) or subset-identifying genes ( Bottom ).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### EMBER multidimensional spectral microscopy enables quantitative determination of disease- and cell-specific amyloid strains. (PNAS 2023)

- DOI: 10.1073/pnas.2300769120 | PMCID: PMC10041141 | PMID: 36927157
- Evidence: PCA and UMAP with Quadratic Discriminant Classification.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Functional SARS-CoV-2 cross-reactive CD4<sup>+</sup> T cells established in early childhood decline with age. (PNAS 2023)

- DOI: 10.1073/pnas.2220320120 | PMCID: PMC10041119 | PMID: 36917669
- Evidence: ( B ) Contour UMAP plot of bulk and antigen-specific mCD4 + T cells from four representative donors from each age group.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Single-nuclei RNA sequencing (snRNA-seq) uncovers trophoblast cell types and lineages in the mature bovine placenta. (PNAS 2023)

- DOI: 10.1073/pnas.2221526120 | PMCID: PMC10041116 | PMID: 36913592
- Evidence: The uniform manifold approximation and projection (UMAP) ( 33 ) was used to display these clusters in two dimensions ( Fig.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle, Slingshot] -> stage not stated [STRING db]

### KMT2D acetylation by CREBBP reveals a cooperative functional interaction at enhancers in normal and malignant germinal center B cells. (PNAS 2023)

- DOI: 10.1073/pnas.2218330120 | PMCID: PMC10089214 | PMID: 36893259
- Evidence: On the left, UMAP projection of scRNA profiles obtained from human GC B cells color-coded according to 13 distinct B cell differentiation states identified in ref 33 (see original Fig.
- Full pipeline: alignment/mapping [HISAT2, featureCounts v1.6.3] -> quantification [ImageJ, featureCounts v1.6.3] -> normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v4.2, SciPy] -> stage not stated [GSEA, HOMER]

### Nasal administration of anti-CD3 mAb (Foralumab) downregulates <i>NKG7</i> and increases <i>TGFB1</i> and <i>GIMAP7</i> expression in T cells in subjects with COVID-19. (PNAS 2023)

- DOI: 10.1073/pnas.2220272120 | PMCID: PMC10243127 | PMID: 36881624
- Evidence: ( F ) Graph-based clustering of uniform manifold approximation and projection (UMAP) of T cell subsets at baseline (day -2) and at day 10 in healthy controls, untreated and Foralumab-treated COVID-19 subjects showing effector T cell cluster decrease in treated subjects.
- Full pipeline: read trimming [Seurat v4.1.1] -> alignment/mapping [STAR] -> quantification [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30.1] -> visualisation [Seurat v4.1.1] -> stage not stated [ggplot2 v3.3.6]

### Innate immune cell activation causes lung fibrosis in a humanized model of long COVID. (PNAS 2023)

- DOI: 10.1073/pnas.2217199120 | PMCID: PMC10013740 | PMID: 36848564
- Evidence: In total, high-quality single-cell transcriptomes of 251,612 cells from 5 COVID human lungs and 20 healthy human control lungs were assessed, and their population structure was visualized using Uniform Manifold Approximation and Projection (UMAP).
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP]

### Defining and targeting tumor-associated macrophages in malignant mesothelioma. (PNAS 2023)

- DOI: 10.1073/pnas.2210836120 | PMCID: PMC9992826 | PMID: 36821580
- Evidence: ( E ) Uniform manifold approximation and projection (UMAP) of single cells derived from tumor biopsy of untreated mesothelioma.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Type III interferon drives thymic B cell activation and regulatory T cell generation. (PNAS 2023)

- DOI: 10.1073/pnas.2220120120 | PMCID: PMC9992806 | PMID: 36802427
- Evidence: ( F ) Uniform Manifold Approximation and Projection (UMAP) plot for thymic B cells.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, R v4.0.0, Seurat, edgeR v3.24.3, ggplot2, pheatmap]

### <i>Cspg4<sup>high</sup></i> microglia contribute to microgliosis during neurodegeneration. (PNAS 2023)

- DOI: 10.1073/pnas.2210643120 | PMCID: PMC9974490 | PMID: 36795751
- Evidence: ( A ) UMAP showing the cell populations in the human brain based on the data extracted from the Human Protein Atlas.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, MACS2, Seurat]

### Self-renewing macrophages in dorsal root ganglia contribute to promote nerve regeneration. (PNAS 2023)

- DOI: 10.1073/pnas.2215906120 | PMCID: PMC9963351 | PMID: 36763532
- Evidence: An unbiased clustering (graph-based clustering) was done and presented as UMAP (Uniform Manifold Approximation and Projection), using a dimensional reduction algorithm that shows groups of similar cells as clusters on a scatter plot.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Metascape, R]

### Distinctive transcriptomic and epigenomic signatures of bone marrow-derived myeloid cells and microglia in CNS autoimmunity. (PNAS 2023)

- DOI: 10.1073/pnas.2212696120 | PMCID: PMC9963604 | PMID: 36730207
- Evidence: We performed nonlinear dimension reduction (UMAP) and cluster identification on the top 30 principal components identified via principal component analysis.
- Full pipeline: quality control [ArchR] -> dimensionality reduction/clustering [GSEA, Signac, UMAP, clusterProfiler, fgsea] -> differential/statistical testing [MACS2] -> stage not stated [R, Seurat, scDblFinder]

### Post-transcriptional regulation in cranial neural crest cells expands developmental potential. (PNAS 2023)

- DOI: 10.1073/pnas.2212578120 | PMCID: PMC9963983 | PMID: 36724256
- Evidence: ( B ) Uniform Manifold Approximation and Projection for Dimension Reduction (UMAP) plots showing cell populations obtained from single-cell ATAC and scRNA-seq at each stage.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Losartan controls immune checkpoint blocker-induced edema and improves survival in glioblastoma mouse models. (PNAS 2023)

- DOI: 10.1073/pnas.2219199120 | PMCID: PMC9963691 | PMID: 36724255
- Evidence: Uniform Manifold Approximation and Projection (UMAP) embedding of the top 20 PCs (using RunUMAP with the following settings: min_dist = 0.5, number of neighbors = 30, and distance metric = Euclidean) was used to visualize clustering results, followed by cell-type annotation.
- Full pipeline: quantification [RSEM v1.2.19] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [survival (R)] -> visualisation [UMAP] -> stage not stated [ImageJ, R, Seurat v4.0.0, seaborn v0.9.0]

### Inducible disruption of <i>Tet</i> genes results in myeloid malignancy, readthrough transcription, and a heterochromatin-to-euchromatin switch. (PNAS 2023)

- DOI: 10.1073/pnas.2214824120 | PMCID: PMC9963276 | PMID: 37406303
- Evidence: ( A ) Uniform Manifold Approximation and Projection (UMAP) dimensionality reduction for single-cell RNA-seq data, displaying the different identified populations ( Left ) and the new cell populations present in Tet iTKO BM ( Right ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2]

### Generation and analysis of context-specific genome-scale metabolic models derived from single-cell RNA-Seq data. (PNAS 2023)

- DOI: 10.1073/pnas.2217868120 | PMCID: PMC9963017 | PMID: 36719923
- Evidence: Analysis with Seurat ( 25 ) yielded a good agreement between the cell subtype definition by Booeshaghi et al. and the Uniform Manifold Approximation and Projection (UMAP) projection ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [DESeq2, R v4.1.1]

### Mammalian life depends on two distinct pathways of DNA damage tolerance. (PNAS 2023)

- DOI: 10.1073/pnas.2216055120 | PMCID: PMC9942833 | PMID: 36669105
- Evidence: Uniform Manifold Approximation and Projection (UMAP) clustering of single-cell transcriptomes revealed the existence of three clusters that were populated by all cell types ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### A sex-biased imbalance between Tfr, Tph, and atypical B cells determines antibody responses in COVID-19 patients. (PNAS 2023)

- DOI: 10.1073/pnas.2217902120 | PMCID: PMC9942838 | PMID: 36669118
- Evidence: The initial 100 SOM clusters and meta-clustering were then examined manually (by expression heatmaps and UMAP or t-SNE) to find the point at which significant populations of interest were inappropriately merged.
- Full pipeline: quantification [edgeR] -> dimensionality reduction/clustering [UMAP, edgeR, ggplot2 v3.3.3] -> differential/statistical testing [edgeR, ggplot2 v3.3.3] -> stage not stated [R v4.0.3]

### Distinct and opposite effects of leukemogenic <i>Idh</i> and <i>Tet2</i> mutations in hematopoietic stem and progenitor cells. (PNAS 2023)

- DOI: 10.1073/pnas.2208176120 | PMCID: PMC9942850 | PMID: 36652477
- Evidence: ( C ) t-SNE and UMAP representations of bone marrow LSK cells from mice with the indicated genotypes, clustered based on the similarity of their transcriptome determined by scRNA-seq.
- Full pipeline: alignment/mapping [SCENIC, Seurat, Slingshot] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, MACS2]

### Cardiac progenitors instruct second heart field fate through Wnts. (PNAS 2023)

- DOI: 10.1073/pnas.2217687120 | PMCID: PMC9942880 | PMID: 36649430
- Evidence: We performed dimensionality reduction through UMAP and annotated clusters through known marker genes ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Molecular imaging of chemokine-like receptor 1 (CMKLR1) in experimental acute lung injury. (PNAS 2023)

- DOI: 10.1073/pnas.2216458120 | PMCID: PMC9934297 | PMID: 36626557
- Evidence: Data collection, analysis, and UMAP identification of major cell populations were conducted as previously reported ( 31 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat v4.1.0]

### CITED2 is a conserved regulator of the uterine-placental interface. (PNAS 2023)

- DOI: 10.1073/pnas.2213622120 | PMCID: PMC9934066 | PMID: 36626551
- Evidence: Uniform manifold approximation and projection (UMAP) profiles of the UPI were similar to previously published UMAP profiles for the rat UPI ( 40 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat] -> stage not stated [Metascape]

### Neighbor-specific gene expression revealed from physically interacting cells during mouse embryonic development. (PNAS 2023)

- DOI: 10.1073/pnas.2205371120 | PMCID: PMC9926237 | PMID: 36595695
- Evidence: However, the current visualization algorithms for scRNA-seq including UMAP ( Fig.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, Enrichr, scDblFinder]

### Dry eye disease in mice activates adaptive corneal epithelial regeneration distinct from constitutive renewal in homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2204134120 | PMCID: PMC9926235 | PMID: 36595669
- Evidence: ( C ) UMAP plot of scRNAseq atlas of the mouse corneal epithelium with table delineating cell frequencies for each population (n = 3 independent sequencing experiments).
- Full pipeline: dimensionality reduction/clustering [SCENIC, UMAP] -> stage not stated [Seurat]

### Thioredoxin-interacting protein is essential for memory T cell formation via the regulation of the redox metabolism. (PNAS 2023)

- DOI: 10.1073/pnas.2218345120 | PMCID: PMC9926250 | PMID: 36595680
- Evidence: ( F ) A UMAP projection of transferred T cells at days 7 (blue) and 11 (orange) after cell transfer is depicted.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSVA]

### c-JUN-mediated transcriptional responses in lymphatic endothelial cells are required for lung fluid clearance at birth. (PNAS 2023)

- DOI: 10.1073/pnas.2215449120 | PMCID: PMC9926280 | PMID: 36595691
- Evidence: ( B ) UMAP plot of lung LECs obtained from different developmental stages.
- Full pipeline: dimensionality reduction/clustering [GSVA, Monocle, Slingshot, UMAP]

### Identification of a unique subset of tissue-resident memory CD4<sup>+</sup> T cells in Crohn's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2204269120 | PMCID: PMC9910620 | PMID: 36574662
- Evidence: ( F ) UMAP of the second cohort of patients (n = 18 per group). tSNE overlay of selected markers is shown.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat, Slingshot]

### Epithelial tubule interconnection driven by HGF-Met signaling in the kidney. (PNAS 2024)

- DOI: 10.1073/pnas.2416887121 | PMCID: PMC11670081 | PMID: 39705305
- Evidence: The resulting reduced-dimensional representation of the data was used for all subsequent embeddings such as UMAP.
- Full pipeline: normalisation [limma] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, ImageJ]

### Permanent cilia loss during cerebellar granule cell neurogenesis involves withdrawal of cilia maintenance and centriole capping. (PNAS 2024)

- DOI: 10.1073/pnas.2408083121 | PMCID: PMC11670249 | PMID: 39705308
- Evidence: Cells were clustered by gene expression and UMAP projections using the first 20 principal components were created.
- Full pipeline: dimensionality reduction/clustering [Seurat v4.2.1, UMAP]

### Interplay between Netrin-1 and Norrin controls arteriovenous zonation of blood-retina barrier integrity. (PNAS 2024)

- DOI: 10.1073/pnas.2408674121 | PMCID: PMC11670198 | PMID: 39693351
- Evidence: Retinal cell annotation and clustering were performed based on gene expression profiles and uniform manifold approximation and projection (UMAP) plots were made for visualization.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA]

### Single-cell atlas of &lt;i&gt;Leishmania&lt;/i&gt; development in sandflies reveals the heterogeneity of transmitted parasites and their role in infection. (PNAS 2024)

- DOI: 10.1073/pnas.2406776121 | PMCID: PMC11670217 | PMID: 39700146
- Evidence: ( C ) UMAP visualization of integrated replicates and conditions, with each cell color-coded to indicate its associated time point.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP]

### Genome-wide single-cell and single-molecule footprinting of transcription factors with deaminase. (PNAS 2024)

- DOI: 10.1073/pnas.2423270121 | PMCID: PMC11670102 | PMID: 39689177
- Evidence: For the single-cell data, ArchR ( 50 ) (version 1.0.2) was employed to perform quality control (with TSS Enrichment > 4 and Number of Unique Fragments > 10), followed by LSI-based dimensionality reduction and clustering using UMAP embedding with default parameters.
- Full pipeline: quality control [ArchR, UMAP] -> read trimming [Bismark, Python, Trim Galore v0.6.10, Trimmomatic v0.39] -> alignment/mapping [Bismark, Trim Galore v0.6.10, Trimmomatic v0.39] -> dimensionality reduction/clustering [ArchR, UMAP]

### Corticosteroids reduce pathological angiogenesis yet compromise reparative vascular remodeling in a model of retinopathy. (PNAS 2024)

- DOI: 10.1073/pnas.2411640121 | PMCID: PMC11670060 | PMID: 39693344
- Evidence: Transcriptomic differences between normoxic and OIR cell types were statistically compared using a negative binomial model and analyzed using visualization tools including RidgePlot and UMAP plot from the Seurat R Package.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [UMAP, edgeR] -> structure determination [Seurat] -> visualisation [UMAP, clusterProfiler] -> stage not stated [DESeq2, GSEA, GSVA, ImageJ]

### Complement C3d enables cell-mediated immunity capable of distinguishing spontaneously transformed from nontransformed cells. (PNAS 2024)

- DOI: 10.1073/pnas.2405824121 | PMCID: PMC11670236 | PMID: 39693340
- Evidence: 22 principal components (PCs) were used for clustering and generating the UMAP ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [Seurat, pheatmap]

### Leukemia inhibitory factor (LIF) receptor amplifies pathogenic activation of fibroblasts in lung fibrosis. (PNAS 2024)

- DOI: 10.1073/pnas.2401899121 | PMCID: PMC11648669 | PMID: 39636853
- Evidence: ( C ) UMAP visualization of ( Left ) stromal cell clusters and expression of ( Middle ) COL1A1 and ( Right ) ACTA2 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Seurat v4.3.0, UMAP] -> stage not stated [ImageJ]

### Glutamine is critical for the maintenance of type 1 conventional dendritic cells in normal tissue and the tumor microenvironment. (PNAS 2024)

- DOI: 10.1073/pnas.2412157121 | PMCID: PMC11648871 | PMID: 39625974
- Evidence: The first 20 PCs were used for graph-based cluster identification (FindNeighbors, FindClusters) and UMAP dimensional reduction (RunUMAP).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [MACS2, R v4.3.1, Seurat]

### Transcriptional reprogramming primes CD8+ T cells toward exhaustion in Myalgic encephalomyelitis/chronic fatigue syndrome. (PNAS 2024)

- DOI: 10.1073/pnas.2415119121 | PMCID: PMC11648872 | PMID: 39621903
- Evidence: ( A ) scRNA-seq of T lymphoid cells from 28 cases and 30 controls, depicted by uniform manifold approximation and projection (UMAP).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, GSEA]

### Pharmacological inhibition of HIF2 protects against bone loss in an experimental model of estrogen deficiency. (PNAS 2024)

- DOI: 10.1073/pnas.2416004121 | PMCID: PMC11626196 | PMID: 39602268
- Evidence: Uniform manifold approximation and projection (UMAP) representation displayed a similar cluster distribution between control and mutant groups ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Staggered immunization with mRNA vaccines encoding SARS-CoV-2 polymerase or spike antigens broadens the T cell epitope repertoire. (PNAS 2024)

- DOI: 10.1073/pnas.2406332121 | PMCID: PMC11626164 | PMID: 39589869
- Evidence: Subsequently, based on the top 30 principal components, we generated the UMAP-based visualization, nearest-neighbor computation, and cell clustering.
- Full pipeline: alignment/mapping [R v4.1.2, Seurat v4.0.4] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Chronologically inappropriate morphogenesis (&lt;i&gt;Chinmo&lt;/i&gt;) is required for maintenance of larval stages of fall armyworm. (PNAS 2024)

- DOI: 10.1073/pnas.2411286121 | PMCID: PMC11626174 | PMID: 39589873
- Evidence: Normalization and dimensional reduction techniques such as TF–IDF (Term Frequency–Inverse Document Frequency), SVD (Singular value decomposition), and UMAP (uniform manifold approximation and projection) were applied to reduce noise and emphasize meaningful features for exploratory data analysis.
- Full pipeline: quantification [MACS2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, Seurat, Signac]

### Rescue of cochlear vascular pathology prevents sensory hair cell loss in Norrie disease. (PNAS 2024)

- DOI: 10.1073/pnas.2322124121 | PMCID: PMC11626139 | PMID: 39585982
- Evidence: ( B ) UMAP plot showing cell clusters identified in the 15 pcw human cochlea.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### CD2 expressing innate lymphoid and T cells are critical effectors of immunopathogenesis in hidradenitis suppurativa. (PNAS 2024)

- DOI: 10.1073/pnas.2409274121 | PMCID: PMC11621750 | PMID: 39560648
- Evidence: The datasets were log-normalized, integrated using Harmony, and dimensionally reduced with the Uniform Manifold Approximation and Projection for dimension reduction (UMAP) algorithm ( SI Appendix , Fig.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.0, UMAP]

### Magnetic soft microrobots for erectile dysfunction therapy. (PNAS 2024)

- DOI: 10.1073/pnas.2407809121 | PMCID: PMC11626158 | PMID: 39556757
- Evidence: ( A ) UMAP plots of the four endothelial cell (EC) subclusters in the ED and MSC-Rob groups.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSVA]

### IL-2/anti-IL-2 antibody complexes augment immune responses to therapeutic cancer vaccines. (PNAS 2024)

- DOI: 10.1073/pnas.2322356121 | PMCID: PMC11621762 | PMID: 39556726
- Evidence: ( D ) UMAP clustering of 9,243 cells across conditions.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Loss of XIST lncRNA unlocks stemness and cellular plasticity in ovarian cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2418096121 | PMCID: PMC11588085 | PMID: 39546568
- Evidence: ( E ) UMAP of XIST ( Left ) and CD44 ( Right ) on ovarian cancer patient single-cell sequencing data.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Augmenting antitumor efficacy of Th17-derived Th1 cells through IFN-γ-induced type I interferon response network via IRF7. (PNAS 2024)

- DOI: 10.1073/pnas.2412120121 | PMCID: PMC11588128 | PMID: 39541355
- Evidence: We segregated 18 distinct cell clusters, with 16 of these clusters delineated as various CD4 + T cell subsets, including pre-exhausted, proliferating, resident memory, Th1-like effector, Th17, and Treg cells, by uniform manifold approximation and projection (UMAP) clustering via Seurat ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA, GSVA]

### TARGET-seq: Linking single-cell transcriptomics of human dopaminergic neurons with their target specificity. (PNAS 2024)

- DOI: 10.1073/pnas.2410331121 | PMCID: PMC11588066 | PMID: 39541349
- Evidence: (Scale bar, 20 μm.) ( M and N ) Uniform manifold approximation and projection (UMAP) embeddings showing clustering of analyzed cells from ( M ) fetal VM-derived, and ( N ) VM-patterned hPSC intranigral grafts 12 mo posttransplantation.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [GSEA, Harmony, Slingshot, UMAP, clusterProfiler, fgsea] -> simulation/modelling [Slingshot] -> structure determination [Slingshot] -> visualisation [Harmony] -> stage not stated [ImageJ v2.14.0, R v4.2.1, SAMtools, Seurat v4.3]

### Monocytes give rise to Langerhans cells that preferentially migrate to lymph nodes at steady state. (PNAS 2024)

- DOI: 10.1073/pnas.2404927121 | PMCID: PMC11588065 | PMID: 39541348
- Evidence: Lineage + cells (CD3, CD19, CD335, and Ly6G) were excluded, and UMAP, PHATE, and X-shift analysis was performed on the remaining myeloid cells using FlowJo (FlowJo).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ v1.54, Seurat v5.0.1]

### &lt;i&gt;Samd7&lt;/i&gt; represses short-wavelength cone genes to preserve long-wavelength cone and rod photoreceptor identity. (PNAS 2024)

- DOI: 10.1073/pnas.2402121121 | PMCID: PMC11588049 | PMID: 39531499
- Evidence: ( A ) UMAP (Uniform Manifold Approximation and Projection) of scRNA-seq data from 4-dpf crx:GFP + photoreceptors.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP]

### DeSide: A unified deep learning approach for cellular deconvolution of tumor microenvironment. (PNAS 2024)

- DOI: 10.1073/pnas.2407096121 | PMCID: PMC11573681 | PMID: 39514318
- Evidence: ( C ) UMAP visualization of the integrated scRNA-seq dataset S0.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, Python, TensorFlow]

### CTCF-dependent insulation of &lt;i&gt;Hoxb13&lt;/i&gt; and the heterochronic control of tail length. (PNAS 2024)

- DOI: 10.1073/pnas.2414865121 | PMCID: PMC11573545 | PMID: 39499640
- Evidence: UMAP and k-nearest neighbors were computed using 30 principal components.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools v1.16.1, STAR v2.7.10a, minimap2 v2.28] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.0] -> stage not stated [BEDTools v2.30.0, Picard, R, Seurat v4.3, ggpubr]

### Spatiotemporal transcriptomic map of glial cell response in a mouse model of acute brain ischemia. (PNAS 2024)

- DOI: 10.1073/pnas.2404203121 | PMCID: PMC11573666 | PMID: 39499634
- Evidence: ( C ) UMAP of spatial spots, color-coded by annotated brain regions (shades of gray for intact areas, red for lesions).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Metascape, Seurat]

### Effects of oxycodone on placental lineages: Evidence from the transcriptome profile of mouse trophoblast giant cells. (PNAS 2024)

- DOI: 10.1073/pnas.2412349121 | PMCID: PMC11551428 | PMID: 39475633
- Evidence: In each, the number of recovered nuclei was few, and preliminary UMAP analysis revealed that these nuclei largely distributed into a unique cluster to which the other placental/decidual samples did not contribute.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, Python, Seurat v5.0.1]

### Characterization of RNA editing and gene therapy with a compact CRISPR-Cas13 in the retina. (PNAS 2024)

- DOI: 10.1073/pnas.2408345121 | PMCID: PMC11551378 | PMID: 39475642
- Evidence: ( B ) Uniform Manifold Approximation and Projection (UMAP) plots show retinal cell type clusters for the untreated control, Cas13bt3-NT sgRNA, and Cas13bt3-VEGFA sgRNA treatment groups.
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [BLAST, STAR v2.7] -> quantification [RSEM] -> normalisation [RSEM, Seurat v4.3] -> dimensionality reduction/clustering [Bioconductor, GSEA, R v4.3, Seurat v4.3, UMAP, clusterProfiler]

### Cellular heterogeneity and dynamics of the human uterus in healthy premenopausal women. (PNAS 2024)

- DOI: 10.1073/pnas.2404775121 | PMCID: PMC11551439 | PMID: 39471215
- Evidence: ( B ) Identification of five major cell types from global clustering, visualized in Uniform Manifold Approximation and Projection (UMAP).
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [SCENIC]

### Perturbation-specific transcriptional mapping for unbiased target elucidation of antibiotics. (PNAS 2024)

- DOI: 10.1073/pnas.2409747121 | PMCID: PMC11551328 | PMID: 39467118
- Evidence: ( B ) UMAP visualization of all compound treatments (at the highest dose) of wild-type PA14 and seven engineered hypomorphs at 90 min.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Virtual patient analysis identifies strategies to improve the performance of predictive biomarkers for PD-1 blockade. (PNAS 2024)

- DOI: 10.1073/pnas.2410911121 | PMCID: PMC11551325 | PMID: 39467131
- Evidence: UMAP dimensionality reduction with pretreatment biomarker candidate levels showed no clear separation of patients with different response statuses ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [scikit-learn]

### Regional specialization, polyploidy, and seminal fluid transcripts in the &lt;i&gt;Drosophila&lt;/i&gt; female reproductive tract. (PNAS 2024)

- DOI: 10.1073/pnas.2409850121 | PMCID: PMC11536144 | PMID: 39453739
- Evidence: ( C ) UMAP plot. “SSC” = spermathecal secretory cells. “AGSC” = AG secretory cells. “MUS” = muscle. “FB” = reproductive-associated Fat Body.
- Full pipeline: quality control [SoupX v1.5.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ v2.3.0, R v4.1, Seurat v5.0.3]

### &lt;i&gt;Arabidopsis&lt;/i&gt; uses a molecular grounding mechanism and a biophysical circuit breaker to limit floral abscission signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2405806121 | PMCID: PMC11536089 | PMID: 39453742
- Evidence: Visualization was performed by UMAP embedding.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HTSeq, STAR, kallisto] -> quantification [kallisto] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Jupyter, R v3.6, Seurat]

### QSOX1 facilitates dormant esophageal cancer stem cells to evade immune elimination via PD-L1 upregulation and CD8 T cell exclusion. (PNAS 2024)

- DOI: 10.1073/pnas.2407506121 | PMCID: PMC11536095 | PMID: 39432781
- Evidence: ( A ) UMAP visualization reveals the subpopulations of tumor cells in PT ( n = 5,255 cells) and DT ( n = 525 cells) with the percentage of each subpopulation presented in a pie chart.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ, Monocle]

### The pyruvate-GPR31 axis promotes transepithelial dendrite formation in human intestinal dendritic cells. (PNAS 2024)

- DOI: 10.1073/pnas.2318767121 | PMCID: PMC11536072 | PMID: 39432783
- Evidence: Cells were clustered using the Leiden algorithm and cell clusters were visualized with the UMAP algorithm.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.8, SAMtools v0.1.18, TopHat v2.1.1] -> quantification [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, Metascape v3.5.20230501] -> visualisation [UMAP] -> stage not stated [GSEA, R v4.1, Scanpy v1.9.1, Seurat v4.1.0]

### Single-cell resolution of intestinal regeneration in pythons without crypts illuminates conserved vertebrate regenerative mechanisms. (PNAS 2024)

- DOI: 10.1073/pnas.2405463121 | PMCID: PMC11513969 | PMID: 39423244
- Evidence: Cells were clustered using the top 16 principal components, as determined from an elbow plot, and visualized with Universal Manifold Approximation (UMAP).
- Full pipeline: read trimming [STAR v2.7.10a, Trimmomatic v0.36] -> alignment/mapping [STAR v2.7.10a, Trimmomatic v0.36] -> quantification [STAR v2.7.10a, Trimmomatic v0.36] -> normalisation [Seurat v4.2.0] -> dimensionality reduction/clustering [Seurat v4.2.0, UMAP, pheatmap v1.0.12] -> differential/statistical testing [pheatmap v1.0.12] -> visualisation [UMAP, pheatmap v1.0.12] -> stage not stated [DESeq2 v1.36.0, SCENIC v1.3.1]

### Multiomics profiling of mouse polycystic kidney disease progression at a single-cell resolution. (PNAS 2024)

- DOI: 10.1073/pnas.2410830121 | PMCID: PMC11513963 | PMID: 39405347
- Evidence: ( C ) UMAP plot of the integrated single-nucleus multiomics dataset with weighted nearest neighbor (wnn) clustering.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v4.0.2]

### Injury-induced myosin-specific tissue-resident memory T cells drive immune checkpoint inhibitor myocarditis. (PNAS 2024)

- DOI: 10.1073/pnas.2323052121 | PMCID: PMC11494310 | PMID: 39378095
- Evidence: Following regularized negative binomial regression normalization, cells were clustered via UMAP nonlinear dimensional reduction to allow biological cluster annotation.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> stage not stated [R v4.3.0, Seurat v4.3.0]

### Toward a CRISPR-based mouse model of &lt;i&gt;Vhl&lt;/i&gt;-deficient clear cell kidney cancer: Initial experience and lessons learned. (PNAS 2024)

- DOI: 10.1073/pnas.2408549121 | PMCID: PMC11474080 | PMID: 39365820
- Evidence: ( A ) UMAP of nonimmune cells from 4 Cre-less AAV kidney tumors, colored and labeled by cluster/cell type.
- Full pipeline: read trimming [Cutadapt] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1] -> visualisation [ImageJ v1.53] -> stage not stated [GSEA]

### Paracrine FGF1 signaling directs pituitary architecture and size. (PNAS 2024)

- DOI: 10.1073/pnas.2410269121 | PMCID: PMC11459159 | PMID: 39320918
- Evidence: Cell clusters identified by Uniform Manifold Approximation and Projection (UMAP) ( 43 ) were annotated based on the expression of key pituitary marker genes ( SI Appendix, Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, Seurat]

### Investigating the &lt;i&gt;cis-&lt;/i&gt;regulatory basis of C&lt;sub&gt;3&lt;/sub&gt; and C&lt;sub&gt;4&lt;/sub&gt; photosynthesis in grasses at single-cell resolution. (PNAS 2024)

- DOI: 10.1073/pnas.2402781121 | PMCID: PMC11459142 | PMID: 39312655
- Evidence: UMAP embeddings were then calculated for each species utilizing genomic bins ( 68 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.16.1, minimap2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt v4.5, OrthoFinder, scDblFinder]

### A molecular switch from tumor suppressor to oncogene in ER+ve breast cancer: Role of androgen receptor, JAK-STAT, and lineage plasticity. (PNAS 2024)

- DOI: 10.1073/pnas.2406837121 | PMCID: PMC11459127 | PMID: 39312663
- Evidence: UMAP and violin plots of pathway signatures (basal signature, luminal signature, and AR signature) are shown.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Septo-dentate gyrus cholinergic circuits modulate function and morphogenesis of adult neural stem cells through granule cell intermediaries. (PNAS 2024)

- DOI: 10.1073/pnas.2405117121 | PMCID: PMC11459179 | PMID: 39312657
- Evidence: Uniform Manifold Approximation and Projection (UMAP) analysis uncovered all known major DG cell types ( 32 – 36 ), including mature GCs, interneurons (GABA), mossy cells (MCs), astrocytes, oligodendrocytes (oligo), oligodendrocyte progenitor cells (OPCs), microglia, endothelial cells, along with the neurogenic cell clusters related to AHN, including NSCs, neural progenitors/neuroblasts (NPs/NBs), ...
- Full pipeline: dimensionality reduction/clustering [Seurat, Slingshot, UMAP] -> differential/statistical testing [R v4.1] -> simulation/modelling [Slingshot] -> structure determination [Seurat] -> stage not stated [Fiji, ImageJ]

### Single-cell analysis identifies distinct macrophage phenotypes associated with prodisease and proresolving functions in the endometriotic niche. (PNAS 2024)

- DOI: 10.1073/pnas.2405474121 | PMCID: PMC11420174 | PMID: 39255000
- Evidence: UMAP projection revealed 18 clusters ( Fig.
- Full pipeline: dimensionality reduction/clustering [R v4.3.2, Seurat v4.4.0, UMAP] -> differential/statistical testing [R v4.3.2, Seurat v4.4.0]

### Joint trajectory inference for single-cell genomics using deep learning with a mixture prior. (PNAS 2024)

- DOI: 10.1073/pnas.2316256121 | PMCID: PMC11406253 | PMID: 39226366
- Evidence: Uniform Manifold Approximation and Projection (UMAP) visualizations of the mouse neocortex in Yuzwa and Ruan datasets.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle, Seurat, Slingshot] -> visualisation [UMAP]

### Single-cell analysis via manifold fitting: A framework for RNA clustering and beyond. (PNAS 2024)

- DOI: 10.1073/pnas.2400002121 | PMCID: PMC11406302 | PMID: 39226348
- Evidence: In this part, we show that scAMF’s visualization performance surpasses those of widely used methods like T-SNE ( 28 ), uniform manifold approximation and projection (UMAP)( 32 ), and the classical principle component analysis (PCA)( 33 ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP]

### Qki5 safeguards spinal motor neuron function by defining the motor neuron-specific transcriptome via pre-mRNA processing. (PNAS 2024)

- DOI: 10.1073/pnas.2401531121 | PMCID: PMC11406248 | PMID: 39226364
- Evidence: Dimensionality reduction by Uniform Manifold Approximation and Projection (UMAP) revealed that our hiPSC-MNs model could be divided into six different cell clusters ( Fig.
- Full pipeline: alignment/mapping [Metascape] -> quantification [Metascape, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Metascape, edgeR] -> stage not stated [Seurat]

### An integrated transcription factor framework for Treg identity and diversity. (PNAS 2024)

- DOI: 10.1073/pnas.2411301121 | PMCID: PMC11388289 | PMID: 39196621
- Evidence: 34 ) visualized on UMAP of splenic Treg scATAC-seq data.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Signac v1.4]

### Therapeutic delivery of CCL2 modulates immune response and restores host-microbe homeostasis. (PNAS 2024)

- DOI: 10.1073/pnas.2400528121 | PMCID: PMC11388407 | PMID: 39186644
- Evidence: The 2D Uniform Manifold Approximation and Projection (UMAP) revealed 37 cell clusters, including five macrophages clusters in each experimental group ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [mothur]

### Somatic mutations in tumor-infiltrating lymphocytes impact on antitumor immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2320189121 | PMCID: PMC11363295 | PMID: 39167601
- Evidence: When the cancer-specific clonotypes were plotted in the UMAP figure of scRNA/TCR-seq using each TCR, they were mainly clustered into exhausted T cell clusters characterized by a high expression of exhaustion-related genes ( PDCD1, HAVCR2, LAG3 , etc.) (224/322), which is consistent with previous studies, including ours ( Fig.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Lipid-associated macrophages' promotion of fibrosis resolution during MASH regression requires TREM2. (PNAS 2024)

- DOI: 10.1073/pnas.2405746121 | PMCID: PMC11363294 | PMID: 39172787
- Evidence: Individual UMAPs from each condition are shown in the Left panel and the merged UMAP on the Right.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Hydrogel biomaterials that stiffen and soften on demand reveal that skeletal muscle stem cells harbor a mechanical memory. (PNAS 2024)

- DOI: 10.1073/pnas.2406787121 | PMCID: PMC11363279 | PMID: 39163337
- Evidence: ( A ) Uniform manifold approximation and projection (UMAP) of single-cell RNA sequencing results with myogenic states assigned to clusters and overlaid with cell fate trajectories inferred from RNA velocity analysis revealed differential clustering for cells in the progenitor pool at day 7 for culture on soft versus stiff substrates and at day 3 for culture on stiff substrates with RhoA inhibition...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [UMAP]

### Uncovering underlying physical principles and driving forces of cell differentiation and reprogramming from single-cell transcriptomics. (PNAS 2024)

- DOI: 10.1073/pnas.2401540121 | PMCID: PMC11348339 | PMID: 39150785
- Evidence: Simply put, this method includes Uniform Manifold Approximation and Projection (UMAP)-based identification of cell-type clusters, estimation of RNA velocity, reconstruction of cell development dynamics’ vector field, and quantification of the cell development driving forces as the potential landscape and curl flux.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> structure determination [UMAP]

### Single-nuclei sequencing of uterine serous carcinoma reveals racial differences in immune signaling. (PNAS 2024)

- DOI: 10.1073/pnas.2402998121 | PMCID: PMC11348309 | PMID: 39133838
- Evidence: ( B ) UMAP plot of 102,431 nuclei from 13 patients, colored by the 6 major cell types.
- Full pipeline: read trimming [StringTie, Trimmomatic] -> alignment/mapping [Bowtie2, Picard, StringTie, Trimmomatic] -> quantification [StringTie, Trimmomatic] -> registration [GATK] -> dimensionality reduction/clustering [GSEA, R, Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [CellChat]

### The neocortical infrastructure for language involves region-specific patterns of laminar gene expression. (PNAS 2024)

- DOI: 10.1073/pnas.2401687121 | PMCID: PMC11348331 | PMID: 39133845
- Evidence: ( A ) Uniform manifold approximation and projection mapping (UMAP) helps to visualize the similarities and differences between 12 data-driven clusters, based on combined analysis of data from 48 tissue sections from the inferior frontal gyrus and superior temporal sulcus.
- Full pipeline: quality control [Bioconductor] -> alignment/mapping [MAGMA, STAR v2.5.1b, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> visualisation [UMAP] -> stage not stated [ImageJ v1.53t, R]

### An IL-23-STAT4 pathway is required for the proinflammatory function of classical dendritic cells during CNS inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2400153121 | PMCID: PMC11317592 | PMID: 39088391
- Evidence: Using unsupervised UMAP visualization on normalized RNA gene counts, we identified heterogeneous populations distributed in 25 clusters including five clusters with DC characteristics ( Fig.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Unraveling clonal CD8 T cell expansion and identification of essential factors in γ-herpesvirus-induced lymphomagenesis. (PNAS 2024)

- DOI: 10.1073/pnas.2404536121 | PMCID: PMC11317613 | PMID: 39088396
- Evidence: ( A ) Split UMAP visualization of combined single CD8 + T cell transcriptomes of WT or Mock-infected calves, with unsupervised Seurat clustering analysis.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [Seurat, UMAP] -> stage not stated [GSEA]

### A Markovian dynamics for &lt;i&gt;Caenorhabditis elegans&lt;/i&gt; behavior across scales. (PNAS 2024)

- DOI: 10.1073/pnas.2318805121 | PMCID: PMC11317559 | PMID: 39083417
- Evidence: ( C ) We visualize X K ∗ by projecting onto two-dimensions using UMAP ( 31 ), and coloring each point by the body wave phase velocity ω = − 1 2 π d dt tan − 1 ( a 2 / a 1 ) ( 20 ) ( Left ) and the overall body curvature ( Right ) obtained by summing the tangent angles θ i along the body γ = ∑ i θ i .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Matrix stiffness-dependent regulation of immunomodulatory genes in human MSCs is associated with the lncRNA CYTOR. (PNAS 2024)

- DOI: 10.1073/pnas.2404146121 | PMCID: PMC11317610 | PMID: 39074278
- Evidence: ( A ) Uniform manifold approximation and projection (UMAP) dimensional reductions of MSCs reveal four distinct clusters which exhibit similar patterns of enrichment for gene signatures/modules associated with 150 or 2,000 Pa IPNs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat]

### The RPD3L deacetylation complex is required for facultative heterochromatin repression in &lt;i&gt;Neurospora crassa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2404770121 | PMCID: PMC11317574 | PMID: 39074265
- Evidence: UMAP Analysis Puts RPD3L-Mediated Repression in Context with Other Repressive Mechanisms Acting on Facultative Heterochromatin.
- Full pipeline: alignment/mapping [VCFtools, freebayes] -> normalisation [R] -> dimensionality reduction/clustering [UMAP]

### Transition of signal requirement in hematopoietic stem cell development from hemogenic endothelial cells. (PNAS 2024)

- DOI: 10.1073/pnas.2404193121 | PMCID: PMC11294991 | PMID: 39042698
- Evidence: We next conducted the velocity analysis and projected the result into the UMAP data ( SI Appendix , Fig.
- Full pipeline: quality control [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Jupyter, UMAP, scVelo] -> visualisation [Seurat]

### A therapy for suppressing canonical and noncanonical SARS-CoV-2 viral entry and an intrinsic intrapulmonary inflammatory response. (PNAS 2024)

- DOI: 10.1073/pnas.2408109121 | PMCID: PMC11287264 | PMID: 39028694
- Evidence: In all organoids, the presence and distribution of pulmonary cell types—as represented by the size, composition, location, proportion, and identity of Uniform Manifold Approximation and Projection (UMAP) cell clusters—were always similar from organoid-to-organoid.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Metascape]

### Tropism for ciliated cells is the dominant driver of influenza viral burst size in the human airway. (PNAS 2024)

- DOI: 10.1073/pnas.2320303121 | PMCID: PMC11295045 | PMID: 39008691
- Evidence: A Uniform Manifold Approximation and Projection (UMAP) of our flow cytometry markers showed several distinct clusters of cells, many of which overlapped with the major lineage-defining markers and populations defined by our gating strategy ( Fig.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [Seurat v4.3.0, Trimmomatic] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HTSeq, R, ggplot2, vegan]

### Life stage-specific poly(A) site selection regulated by <i>Trypanosoma brucei</i> DRBD18. (PNAS 2024)

- DOI: 10.1073/pnas.2403188121 | PMCID: PMC11260167 | PMID: 38990950
- Evidence: All four samples were introduced into the canonical correlation analysis integration workflow, followed by Louvain clustering, and UMAP projection.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, R, Seurat]

### Mechanical stress during confined migration causes aberrant mitoses and c-MYC amplification. (PNAS 2024)

- DOI: 10.1073/pnas.2404551121 | PMCID: PMC11260125 | PMID: 38990945
- Evidence: (Scale bar: 20 μm.) ( C ) Low dimensional UMAP embeddings of single-cell RNA-seq data showing automatic clustering based on transcriptomic profile of each cell ( Left ), cell cycle phase clustering ( Middle ) and identification of cells belonging to each batch, straight or constriction ( Right ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Enrichr]

### Orthogonality of sensory and contextual categorical dynamics embedded in a continuum of responses from the second somatosensory cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2316765121 | PMCID: PMC11260089 | PMID: 38990946
- Evidence: Population-level analysis, performed through the Uniform Manifold Approximation and Projection (UMAP) method, confirmed the single-cell level observation that neuronal responses exhibit a grade continuum, from purely sensory to purely categorical, rather than discrete clusters of activity types.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### The dynamic behavior of chromatophores marks the transition from bands to spots in leopard geckos. (PNAS 2024)

- DOI: 10.1073/pnas.2400486121 | PMCID: PMC11260152 | PMID: 38976731
- Evidence: ( A ) Cluster identification within chromatophores and UMAP representation of the expression of selected chromatophore differentiation markers.
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> stage not stated [InterProScan, R, SAMtools v1.9, Seurat v4.2.0, VCFtools v0.1.16, ggplot2, pheatmap, scDblFinder v1.12.0]

### A wound-induced differentiation trajectory for neurons. (PNAS 2024)

- DOI: 10.1073/pnas.2322864121 | PMCID: PMC11260127 | PMID: 38976727
- Evidence: We determined whether neural subpopulations of the UMAP were either over- or underclustered based on known neural marker gene expression.
- Full pipeline: read trimming [RAxML v8.2.4] -> alignment/mapping [MUSCLE v3.8.31, RAxML v8.2.4] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [BUSCO v3.0.2, Pilon v1.23]

### TFEB safeguards trophoblast syncytialization in humans and mice. (PNAS 2024)

- DOI: 10.1073/pnas.2404062121 | PMCID: PMC11253012 | PMID: 38968109
- Evidence: Left panel, the uniform manifold approximation and projection (UMAP) plot of major cell types in WT placentas.
- Full pipeline: dimensionality reduction/clustering [DESeq2, UMAP]

### Single-cell analysis of treatment-resistant prostate cancer: Implications of cell state changes for cell surface antigen-targeted therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2322203121 | PMCID: PMC11252802 | PMID: 38968122
- Evidence: ( A ) UMAP of tumor cells (N = 35,696 cells), colored by patient ID (large panel on Left ), category ( Top Right panel), treatments ( Middle Right panel; categories include untreated, androgen-receptor signaling inhibitor/ARSI, and ARSI plus taxane–based chemotherapy) or TP53/RB1 genomic status ( Bottom Right panel).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, SCENIC]

### NRF2 is a spatiotemporal metabolic hub essential for the polyfunctionality of Th2 cells. (PNAS 2024)

- DOI: 10.1073/pnas.2319994121 | PMCID: PMC11252815 | PMID: 38959032
- Evidence: We used uniform manifold approximation projection (UMAP) to group cells with similar transcriptome profiles into clusters, which revealed ten transcriptionally distinct clusters such as Th17 (cluster 0; Rorc and Il17a ), Th2 (cluster 2; Gata3, Il4, Il5, and Il13 ), Treg (cluster 3; Foxp3 ), Th1 (cluster 5; Tbx21 and Ifng ), central memory-like (cluster 6; Klf2 and S1pr1 ), and interferon-stimulate...
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP] -> stage not stated [Scanpy]

### Multiplexed in situ hybridization reveals distinct lineage identities for major and minor vein initiation during maize leaf development. (PNAS 2024)

- DOI: 10.1073/pnas.2402514121 | PMCID: PMC11252972 | PMID: 38959034
- Evidence: ( A ) Cluster analysis and UMAP plot for the P2 leaf primordium reveals five domains.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose v2.0, ImageJ]

### Cholinergic macrophages promote the resolution of peritoneal inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2402143121 | PMCID: PMC11228479 | PMID: 38923993
- Evidence: The leading 30 PCs were used to calculate the uniform manifold approximation and projection (UMAP) embedding using RunUMAP function.
- Full pipeline: quantification [velocyto] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R] -> simulation/modelling [scDblFinder] -> stage not stated [FSL, SCENIC, fgsea]

### Genomic structural variation contributes to evolved changes in gene expression in high-altitude Tibetan sheep. (PNAS 2024)

- DOI: 10.1073/pnas.2322291121 | PMCID: PMC11228492 | PMID: 38913905
- Evidence: ( A ) UMAP clustering of different cell clusters.
- Full pipeline: alignment/mapping [Bowtie2] -> variant calling [VCFtools] -> dimensionality reduction/clustering [PLINK v1.90, R, UMAP] -> stage not stated [DELLY v0.9.1, Flye v2.9.1, Python, SAMtools v1.12, Seurat v4.3.0]

### Capturing the fusion of two ancestries and kinship structures in Merovingian Flanders. (PNAS 2024)

- DOI: 10.1073/pnas.2406734121 | PMCID: PMC11228521 | PMID: 38913897
- Evidence: Applying UMAP ( 24 ) on the probability of individual connectedness (PiC) scores ( 25 ) estimated for the 32 extracted communities revealed the separation of modern West European genomes by broad geographic regions and the clustering of the majority of Early Medieval genomes with present-day Dutch, Danish, and English genomes ( Fig.
- Full pipeline: quality control [ANGSD, MultiQC] -> dimensionality reduction/clustering [UMAP]

### Modular binder technology by NGS-aided, high-resolution selection in yeast of designed armadillo modules. (PNAS 2024)

- DOI: 10.1073/pnas.2318198121 | PMCID: PMC11228518 | PMID: 38917007
- Evidence: To visualize the highly dimensional sequence space, sequences were one-hot encoded and mapped to two dimensions by UMAP ( 18 ).
- Full pipeline: alignment/mapping [Bowtie2, UMAP] -> dimensionality reduction/clustering [Python, UMAP] -> structure determination [PHENIX] -> visualisation [UMAP] -> stage not stated [CCP4]

### Pathogenic variants in autism gene &lt;i&gt;KATNAL2&lt;/i&gt; cause hydrocephalus and disrupt neuronal connectivity by impairing ciliary microtubule dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2314702121 | PMCID: PMC11228466 | PMID: 38916997
- Evidence: ( A ) UMAP clustering of mouse fetal brain cells ( 25 ), colored by cell type.
- Full pipeline: alignment/mapping [BWA] -> variant calling [ANNOVAR, GATK] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [ImageJ] -> visualisation [ComplexHeatmap, ggplot2, pheatmap]

### Hypoxia inducible factor 2α promotes tolerogenic macrophage development during cardiac transplantation through transcriptional regulation of colony stimulating factor 1 receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2319623121 | PMCID: PMC11214057 | PMID: 38889142
- Evidence: ( B ) Identification of 16 unique clusters by uniform manifold approximation and projection (UMAP) in combined conditions.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Monocle]

### Engineering an inducible leukemia-associated fusion protein enables large-scale ex vivo production of functional human phagocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2312499121 | PMCID: PMC11194515 | PMID: 38857395
- Evidence: The cells’ RNA profiles are visualized using Uniform Manifold Approximation and Projection (UMAP) reflecting the topology of cells in the high-dimensional graph.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Decoding transcriptomic signatures of cysteine string protein alpha-mediated synapse maintenance. (PNAS 2024)

- DOI: 10.1073/pnas.2320064121 | PMCID: PMC11181078 | PMID: 38833477
- Evidence: Then, Uniform Manifold Approximation and Projection for Dimension Reduction (UMAP) was applied to visualize all cell clusters, and the classification and annotation of distinct cell types was based on known marker genes of each major brain cell type.
- Full pipeline: dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP, clusterProfiler] -> visualisation [UMAP]

### Protective function and differentiation cues of brain-resident CD8+ T cells during surveillance of latent <i>Toxoplasma gondii</i> infection. (PNAS 2024)

- DOI: 10.1073/pnas.2403054121 | PMCID: PMC11181119 | PMID: 38838017
- Evidence: After projection on a Uniform Manifold Approximation and Projection (UMAP) plot, parasite-specific CD8+ T cells partitioned in 13 clusters ( Fig.
- Full pipeline: quality control [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### IL-33 controls IL-22-dependent antibacterial defense by modulating the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2310864121 | PMCID: PMC11145264 | PMID: 38781213
- Evidence: Cellular populations were visualized by Uniform Manifold Approximation And Projection (UMAP) ( SI Appendix , Fig.
- Full pipeline: quality control [Cutadapt v3.7] -> read trimming [Cutadapt v3.7] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.0] -> normalisation [GSEA, Seurat, SoupX] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [fgsea] -> visualisation [UMAP]

### Construction of human 3D striato-nigral assembloids to recapitulate medium spiny neuronal projection defects in Huntington's disease. (PNAS 2024)

- DOI: 10.1073/pnas.2316176121 | PMCID: PMC11145230 | PMID: 38771878
- Evidence: ( K ) Uniform Manifold Approximation and Projection (UMAP) visualization of all cell types in the scRNA-seq data split by groups.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### A time-resolved single-cell roadmap of the logic driving anterior neural crest diversification from neural border to migration stages. (PNAS 2024)

- DOI: 10.1073/pnas.2311685121 | PMCID: PMC11087755 | PMID: 38683994
- Evidence: For each stage, we obtained independent standard dimensionality reduction with PCA, computing a neighborhood graph and UMAP ( 60 ) followed by clustering, [Leiden algorithm, ( 21 )].
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Scanpy]

### Incomplete-penetrant hypertrophic cardiomyopathy &lt;i&gt;MYH7&lt;/i&gt; G256E mutation causes hypercontractility and elevated mitochondrial respiration. (PNAS 2024)

- DOI: 10.1073/pnas.2318413121 | PMCID: PMC11087781 | PMID: 38683993
- Evidence: ( A ) UMAP representation of MYH7 G256E mutant cells ( MYH7 WT/G256E , G256E) and the isogenic counterpart ( MYH7 WT/WT , WT) clustered by the presence of G256E mutation.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Dissection and integration of bursty transcriptional dynamics for complex systems. (PNAS 2024)

- DOI: 10.1073/pnas.2306901121 | PMCID: PMC11067469 | PMID: 38669186
- Evidence: ( A ) Previously published ( 22 ) UMAP embedding of hematopoiesis data shows cells colored by annotated progenitor (HSC, hematopoietic stem cell; MEP-like, megakaryocyte and erythrocyte progenitor; GMP-like, granulocyte and monocyte progenitor) and terminal (Ery, erythrocyte; Bas, basophil; Mon, monocyte; Neu, neutrophil; Meg, megakaryocyte) cell types.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [Python, SciPy, scVelo]

### Threonine phosphorylation of STAT1 restricts interferon signaling and promotes innate inflammatory responses. (PNAS 2024)

- DOI: 10.1073/pnas.2402226121 | PMCID: PMC11046697 | PMID: 38621137
- Evidence: ( B ) UMAP feature P of splenocytes assayed by mass cytometry.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ v1.54i]

### Pharmacological expansion of type 2 alveolar epithelial cells promotes regenerative lower airway repair. (PNAS 2024)

- DOI: 10.1073/pnas.2400077121 | PMCID: PMC11032444 | PMID: 38598345
- Evidence: Next, we performed principal component analysis (PCA) as well as UMAP using the first 30 principal components.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> stage not stated [Scanpy, scDblFinder]

### Identification and removal of unexpected proliferative off-target cells emerging after iPSC-derived pancreatic islet cell implantation. (PNAS 2024)

- DOI: 10.1073/pnas.2320883121 | PMCID: PMC11032438 | PMID: 38598342
- Evidence: ( E ) Newly classified cell populations identified by RCA on the UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Evolutionary and developmental specialization of foveal cell types in the marmoset. (PNAS 2024)

- DOI: 10.1073/pnas.2313820121 | PMCID: PMC11032471 | PMID: 38598343
- Evidence: ( A ) Uniform Manifold Approximation and Projection (UMAP) visualization of cell types from individual cell classes (PR, photoreceptors; HC, horizontal cells; BC, bipolar cells; AC, amacrine cells; RGC, retinal ganglion cells; NN, non-neuronal cells) in the fovea of adult marmoset.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### The IRG1-itaconate axis protects from cholesterol-induced inflammation and atherosclerosis. (PNAS 2024)

- DOI: 10.1073/pnas.2400675121 | PMCID: PMC11009655 | PMID: 38564634
- Evidence: Uniform Manifold Approximation and Projection (UMAP) visualization of myeloid cells from human coronary plaques stratified by cell type ( C ) or showing IRG1 NE ( D ), n = 3,556 cells; Mono/Mø, monocyte/macrophage; DC, dendritic cell; NK, natural killer; ILC, innate lymphoid cell.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellChat, ImageJ]

### Innate-like T cell subset commitment in the murine thymus is independent of TCR characteristics and occurs during proliferation. (PNAS 2024)

- DOI: 10.1073/pnas.2311348121 | PMCID: PMC10998581 | PMID: 38530897
- Evidence: .... n = 2,000 highly variable features number was considered, graph-based clustering (Louvain method) was performed using the default parameters, and a UMAP (dims = 7) was constructed with a resolution of 0.5 based on the stability observed with the package clustree.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.2.1, Seurat]

### Dual topologies of myotomal collagen XV and Tenascin C act in concert to guide and shape developing motor axons. (PNAS 2024)

- DOI: 10.1073/pnas.2314588121 | PMCID: PMC10990108 | PMID: 38502691
- Evidence: ( C ) UMAP plot obtained after mapping on the zebrafish genome and clusterization of isolated GFP + cells ( Left panel); UMAP feature plots showing expression patterns of slow muscle lineage markers prdm1a and smyhc1 ( Right panel).
- Full pipeline: alignment/mapping [UMAP] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [STRING db]

### SRF transcriptionally regulates the oligodendrocyte cytoskeleton during CNS myelination. (PNAS 2024)

- DOI: 10.1073/pnas.2307250121 | PMCID: PMC10962977 | PMID: 38483990
- Evidence: ( A ) UMAP plot showing Seurat clusters and their annotation of 10-mo-old SRF-Flox and SRF-cKO NeuN − nuclei sequenced by 10× snRNA-seq.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Unsupervised identification of significant lineages of SARS-CoV-2 through scalable machine learning methods. (PNAS 2024)

- DOI: 10.1073/pnas.2317284121 | PMCID: PMC10962941 | PMID: 38478692
- Evidence: Some of them are nonlinear dimensionality reduction methods such as t-SNE ( 45 ) and UMAP ( 46 ), as well as linear methods such as principal components analysis which we explored.
- Full pipeline: alignment/mapping [MAFFT v7.453] -> dimensionality reduction/clustering [Pangolin, UMAP] -> stage not stated [Python v3.10.0]

### The training process of many deep networks explores the same low-dimensional manifold. (PNAS 2024)

- DOI: 10.1073/pnas.2310002121 | PMCID: PMC10962999 | PMID: 38470929
- Evidence: Such an isometric embedding is different from the one created by methods like t-SNE ( 7 ) or UMAP ( 8 ) which approximately preserve local pairwise distances but distort the global geometry.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [NumPy]

### The neuroimmune CGRP-RAMP1 axis tunes cutaneous adaptive immunity to the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2322574121 | PMCID: PMC10945812 | PMID: 38451947
- Evidence: UMAP plots show all sorted CD8 + T cells from Ramp1 -deficient and control mice ( Bottom ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [HOMER, Metascape]

### CD38-RyR2 axis-mediated signaling impedes CD8&lt;sup&gt;+&lt;/sup&gt; T cell response to anti-PD1 therapy in cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2315989121 | PMCID: PMC10945783 | PMID: 38451948
- Evidence: Uniform manifold approximation and projection (UMAP) analysis based on transcriptomes partitioned chronic CD8 + T cells into five clusters ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Cellular and molecular organization of the Drosophila foregut. (PNAS 2024)

- DOI: 10.1073/pnas.2318760121 | PMCID: PMC10945768 | PMID: 38442150
- Evidence: The initial analysis placed 21,948 high-quality cells in 18 cell clusters on a UMAP plot ( Fig.
- Full pipeline: dimensionality reduction/clustering [Metascape, UMAP] -> stage not stated [Seurat]

### Principled and interpretable alignability testing and integration of single-cell data. (PNAS 2024)

- DOI: 10.1073/pnas.2313719121 | PMCID: PMC10927515 | PMID: 38416677
- Evidence: ( A ) UMAP visualizations of the original (pooled) data under negative control task Neg1, and the integrated data as obtained by five popular methods (Scanorama, Harmony, LIGER, fastMNN, and Seurat).
- Full pipeline: normalisation [R, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> visualisation [UMAP] -> stage not stated [Seurat]

### Single-cell profiling of African swine fever virus disease in the pig spleen reveals viral and host dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2312150121 | PMCID: PMC10927503 | PMID: 38412127
- Evidence: The integrated matrix was scaled, and the top 30 dimensions resulted from the principal component analysis (PCA) were used for the uniform manifold approximation and projection (UMAP).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R, ggplot2] -> stage not stated [GSVA v1.44.3, Seurat]

### OCA-B/Pou2af1 is sufficient to promote CD4&lt;sup&gt;+&lt;/sup&gt; T cell memory and prospectively identifies memory precursors. (PNAS 2024)

- DOI: 10.1073/pnas.2309153121 | PMCID: PMC10907311 | PMID: 38386711
- Evidence: 7, Cells were clustered using a shared nearest neighbor modularity optimization-based clustering algorithm and visualized using two-dimensional UMAP.
- Full pipeline: quality control [STAR v2.7.3a] -> alignment/mapping [STAR v2.7.3a] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v4.0.0, UMAP, pheatmap]

### Variable expression of <i>MECP2, CDKL5,</i> and <i>FMR1</i> in the human brain: Implications for gene restorative therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2312757121 | PMCID: PMC10907246 | PMID: 38386709
- Evidence: ( A ) UMAP of cells in the integrated developing brain dataset across all studies.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [igraph]

### Heterogeneous osteoimmune profiles via single-cell transcriptomics in osteoporotic patients who fail bisphosphonate treatment. (PNAS 2024)

- DOI: 10.1073/pnas.2316871121 | PMCID: PMC10895260 | PMID: 38346184
- Evidence: ( A ) UMAP-embedding, colored by group.
- Full pipeline: quantification [CellChat] -> dimensionality reduction/clustering [UMAP]

### Targeting MYC induces lipid droplet accumulation by upregulation of HILPDA in clear cell renal cell carcinoma. (PNAS 2024)

- DOI: 10.1073/pnas.2310479121 | PMCID: PMC10873620 | PMID: 38335255
- Evidence: The upper graphs represent dimensional reduction plots (UMAP).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Ultrahigh frequencies of peripherally matured LGI1- and CASPR2-reactive B cells characterize the cerebrospinal fluid in autoimmune encephalitis. (PNAS 2024)

- DOI: 10.1073/pnas.2311049121 | PMCID: PMC10873633 | PMID: 38319973
- Evidence: ( C , Left ) UMAP analyses identified LGI1- and CASPR2-specific BCRs are predominantly from ASCs (n = 114 of 131, blue) and cluster separately to B cells (n = 4 of 14; red) and ( Right ) are a higher proportion of ASCs (Fisher’s exact test; P = 0.002 for LGI1, P = 0.001 for CASPR2 and combined P < 0.001).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Learning the shape of protein microenvironments with a holographic convolutional neural network. (PNAS 2024)

- DOI: 10.1073/pnas.2300838121 | PMCID: PMC10861886 | PMID: 38300863
- Evidence: The inferred amino acid preferences cluster well according to the input amino acid type (true label) in the low-dimensional UMAP representation ( 40 ), and amino acids with similar physicochemical properties cluster in nearby regions in the UMAP ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [OpenMM] -> machine learning [OpenMM] -> stage not stated [AlphaFold]

### Effective treatment of optic neuropathies by intraocular delivery of MSC-sEVs through augmenting the G-CSF-macrophage pathway. (PNAS 2024)

- DOI: 10.1073/pnas.2305947121 | PMCID: PMC10861878 | PMID: 38289952
- Evidence: ( E ) UMAP visualization and the percentage of the retinal cells in 10 major clusters.
- Full pipeline: dimensionality reduction/clustering [CellChat, GSEA, UMAP] -> visualisation [UMAP]

### Light controls mesophyll-specific post-transcriptional splicing of photoregulatory genes by AtPRMT5. (PNAS 2024)

- DOI: 10.1073/pnas.2317408121 | PMCID: PMC10861865 | PMID: 38285953
- Evidence: Data visualization was facilitated through the Uniform Manifold Approximation and Projection (UMAP), employed through “scanpy.tl.umap” function (with parameters “min_dist = 0.2”).
- Full pipeline: read trimming [minimap2 v2.10] -> alignment/mapping [Python, minimap2 v2.10] -> quantification [Monocle v2.28.0, Picard, Seurat v4.3.0.1] -> normalisation [Scanpy] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [DESeq2] -> visualisation [UMAP]

### Single-cell analysis of refractory anti-SRP necrotizing myopathy treated with anti-BCMA CAR-T cell therapy. (PNAS 2024)

- DOI: 10.1073/pnas.2315990121 | PMCID: PMC10861907 | PMID: 38289960
- Evidence: ( A ) Uniform manifold approximation and projection (UMAP) plot of 68,350 single-cell transcriptomes of peripheral blood mononuclear cells integrated from the patient with IMNM at baseline, at 1 mo, at 3 mo, at 6 mo, at 9 mo, at 12 mo, at 15 mo, and at 18 mo post-infusion.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSVA] -> stage not stated [GSEA]

### Extraislet expression of islet antigen boosts T cell exhaustion to partially prevent autoimmune diabetes. (PNAS 2024)

- DOI: 10.1073/pnas.2315419121 | PMCID: PMC10861925 | PMID: 38285952
- Evidence: Dimensionality reduction was performed by unsupervised principal component analysis (PCA) and uniform manifold approximation and projection (UMAP) embedding for each sample.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v4.0.0]

### Computational inference of eIF4F complex function and structure in human cancers. (PNAS 2024)

- DOI: 10.1073/pnas.2313589121 | PMCID: PMC10835048 | PMID: 38266053
- Evidence: To perform UMAP, we standardized the gene expression data by scaling it to unit variance using the fit_transform() function from the class StandardScaler() of the Python package “sklearn.preprocessing”.
- Full pipeline: normalisation [UMAP, scikit-learn] -> dimensionality reduction/clustering [UMAP, clusterProfiler, scikit-learn] -> differential/statistical testing [clusterProfiler] -> visualisation [NetworkX, clusterProfiler] -> stage not stated [AlphaFold, ComplexHeatmap, PyMOL, R, RSEM, STRING db, limma]

### Single-cell RNA sequencing unveils unique transcriptomic signatures of endothelial cells and role of ENO1 in response to disturbed flow. (PNAS 2024)

- DOI: 10.1073/pnas.2318904121 | PMCID: PMC10835041 | PMID: 38261622
- Evidence: Uniform manifold approximation and projection (UMAP) of the integrated scRNA-seq data from the two flow conditions led to the identification of eight clusters ( Fig.
- Full pipeline: normalisation [Seurat v4.0.2] -> dimensionality reduction/clustering [GSEA, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [Seurat v4.0.2]

### Targeted checkpoint control of B cells undergoing positive selection in germinal centers by follicular regulatory T cells. (PNAS 2024)

- DOI: 10.1073/pnas.2304020121 | PMCID: PMC10835130 | PMID: 38261619
- Evidence: Graph-based clustering of Tfr was visualized in 2D using the UMAP algorithm.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Adipose-tissue regulatory T cells are a consortium of subtypes that evolves with age and diet. (PNAS 2024)

- DOI: 10.1073/pnas.2320602121 | PMCID: PMC10823167 | PMID: 38227656
- Evidence: ( B ) UMAP representation of the scRNA-seq data from the combined SVFs with the identified cell types.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Scanpy, scVelo]

### A predisposed motor bias shapes individuality in vocal learning. (PNAS 2024)

- DOI: 10.1073/pnas.2308837121 | PMCID: PMC10801888 | PMID: 38198530
- Evidence: UMAP was performed on 37 principal components for visualizing the cells.
- Full pipeline: dimensionality reduction/clustering [UMAP, WGCNA] -> visualisation [UMAP] -> stage not stated [Metascape, R, Seurat]

### Network physics of attractive colloidal gels: Resilience, rigidity, and phase diagram. (PNAS 2024)

- DOI: 10.1073/pnas.2316394121 | PMCID: PMC10801866 | PMID: 38194451
- Evidence: Instead, the spatial configuration of nodes was converted into vectors, allowing for a series of embedded three-dimensional coordinates using the Uniform Manifold Approximation and Projection (UMAP) method.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Control of cardiac contractions using Cre-lox and degron strategies in zebrafish. (PNAS 2024)

- DOI: 10.1073/pnas.2309842121 | PMCID: PMC10801847 | PMID: 38194447
- Evidence: ( B ) Uniform manifold approximation and projection (UMAP) representation of the data; stacked columns represent the numbers of WT (green), mutant (orange), and degron (violet) cells for each annotated population; UMAP is displayed merged ( Left ) or split by genotype ( Right ).
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP]

### Multiscale spatial mapping of cell populations across anatomical sites in healthy human skin and basal cell carcinoma. (PNAS 2024)

- DOI: 10.1073/pnas.2313326120 | PMCID: PMC10786309 | PMID: 38165934
- Evidence: ( B ) Uniform Manifold Approximation and Projection (UMAP) and clustering of 155,401 cells from 33 donors (11 healthy body sites, 14 healthy face sites, and 8 BCC patients) representing 30 skin cell populations and 16 cell types.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> stage not stated [CellPhoneDB]

### Identification of highly selective SIK1/2 inhibitors that modulate innate immune activation and suppress intestinal inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2307086120 | PMCID: PMC10769863 | PMID: 38147543
- Evidence: The cells were visualized using UMAP plots with the Upper panel showing all cells for each condition (unstimulated, 5 ng/mL LPS, 5 ng/mL LPS + 1 µM JRD-SIK1/2i-3, 5 ng/mL LPS + 10 µM JRD-SIK1/2i-3; n = 2 donors per condition) and the Lower panel depicting only cells for the unstimulated and the 5 ng/mL LPS conditions, as indicated (no compound).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### A complete spatial map of mouse retinal ganglion cells reveals density and gene expression specializations. (PNAS 2025)

- DOI: 10.1073/pnas.2515449122 | PMCID: PMC12772174 | PMID: 41452983
- Evidence: Right , UMAP projection of RGC types clustered using GraSP-derived genes from the single-cell dataset.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat]

### Predicting the unseen: A diffusion-based debiasing framework for transcriptional response prediction at single-cell resolution. (PNAS 2025)

- DOI: 10.1073/pnas.2525268122 | PMCID: PMC12772209 | PMID: 41452988
- Evidence: ( B ) UMAP visualization of generated and true cells across all cell types, taken from cfDiffusion ( 21 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Dysregulated NAMPT signaling underlines the immune-suppressive microenvironment in venous leg ulcers. (PNAS 2025)

- DOI: 10.1073/pnas.2512142122 | PMCID: PMC12772187 | PMID: 41439711
- Evidence: ( A ) UMAP of fibroblast subpopulations in NS and VLU.
- Full pipeline: dimensionality reduction/clustering [CellChat, UMAP] -> stage not stated [GSEA]

### Antibiotic-induced microbiota depletion impairs the proregenerative response to a biological scaffold. (PNAS 2025)

- DOI: 10.1073/pnas.2510841122 | PMCID: PMC12772165 | PMID: 41428865
- Evidence: ( B ) Overall immune infiltrate of ECM-treated muscle at day 7-post VML-ECM detected by flow cytometry and displayed by dimensionality reduction algorithms, Uniform Manifold Approximation and Project (UMAP).
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.42.0] -> stage not stated [GSEA, fgsea v1.28.0]

### Maladaptive immunity to the microbiota promotes neuronal hyperinnervation and itch via IL-17A. (PNAS 2025)

- DOI: 10.1073/pnas.2525146122 | PMCID: PMC12772199 | PMID: 41428888
- Evidence: Data were log-normalized, the top 2,000 variable features identified, scaled, and subjected to PCA (35 dimensions), clustering (resolution = 0.5), and UMAP visualization.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.44.0] -> visualisation [UMAP] -> stage not stated [Metascape, R v4.4, Seurat v4.4.0]

### Convergent mutation trajectories convert functional self-tolerance in IGHV4-34 B cells to genetic tolerance encoded in the antibody. (PNAS 2025)

- DOI: 10.1073/pnas.2522257122 | PMCID: PMC12745689 | PMID: 41410768
- Evidence: The pre589+ and pre589− cells nevertheless formed a single cluster by uniform manifold approximation and projection (UMAP) of their overall gene expression profile ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [GSEA]

### Single-nucleus and spatial transcriptomics reveal the cell populations of intercalary meristems in bamboo. (PNAS 2025)

- DOI: 10.1073/pnas.2511701122 | PMCID: PMC12745733 | PMID: 41410774
- Evidence: ( A ) Spatial cluster (spCluster) distribution from Stereo-seq of an IcM section at the RD stage, with UMAP identifying seven transcriptomic cell populations within the IcM.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose]

### MultistageOT: Multistage optimal transport infers trajectories from a snapshot of single-cell data. (PNAS 2025)

- DOI: 10.1073/pnas.2516046122 | PMCID: PMC12718350 | PMID: 41379995
- Evidence: ( 13 ) data, in the absence of prior knowledge about the number of cells represented in each mature blood cell lineage, we picked n 0 = 3 initial cell states and n F = 24 terminal cell states (3 in each of the eight lineages) in regions of the UMAP expressing lineage associated markers ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### IL-27 promotes Treg cell expression of CD122 and fitness at homeostasis. (PNAS 2025)

- DOI: 10.1073/pnas.2519141122 | PMCID: PMC12718373 | PMID: 41364763
- Evidence: UMAP analysis was performed using the UMAP plug-in using the Euclidean distance function with a nearest neighbor score of 15 and a minimum distance rating of 0.5 (v.1802.03426, 2018, 2017, Leland McInness) for FlowJo (v.10.8.1).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Distinguishing subtypes of endothelial cells in the mouse aorta. (PNAS 2025)

- DOI: 10.1073/pnas.2525755122 | PMCID: PMC12704785 | PMID: 41343672
- Evidence: ( A ) UMAP overview of data from studies 1 to 4.
- Full pipeline: quality control [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [Seurat] -> stage not stated [R, SAMtools, featureCounts]

### Prostaglandin E&lt;sub&gt;2&lt;/sub&gt;-EP2/EP4 signaling induces the tumor-infiltrating Treg phenotype for tumor growth. (PNAS 2025)

- DOI: 10.1073/pnas.2424251122 | PMCID: PMC12704795 | PMID: 41343674
- Evidence: We analyzed the scRNA-seq data of nasopharyngeal cancer of 10 patients downloaded from GSE162025 ( 53 ), and segregated 80,848 cells into 14 clusters including various immune cells and epithelial cells on Uniform Manifold Approximation and Projection (UMAP) plot ( Fig.
- Full pipeline: alignment/mapping [GSEA] -> dimensionality reduction/clustering [UMAP]

### Deciphering precursor cell dynamics in esophageal preneoplasia via genetic barcoding and single-cell transcriptomics. (PNAS 2025)

- DOI: 10.1073/pnas.2509534122 | PMCID: PMC12704714 | PMID: 41337486
- Evidence: ( D ) Uniform manifold approximation and projection (UMAP) with annotated cell clusters.
- Full pipeline: dimensionality reduction/clustering [ComplexHeatmap, UMAP, ggplot2] -> simulation/modelling [SAMtools] -> visualisation [ComplexHeatmap, ggplot2] -> stage not stated [GSEA, SCENIC, Scanpy, fgsea, scVelo, velocyto]

### <i>Lrig1</i>-expressing quiescent stem cells maintain vocal fold mucosal homeostasis via <i>Notch</i> signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2513590122 | PMCID: PMC12685045 | PMID: 41289377
- Evidence: Uniform Manifold Approximation and Projection (UMAP) using Seurat package (v5.1.0) shows Lrig1 + and Lrig1 − cells were distributed across the same cell populations ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### Multipotent progenitors with distinct origins, clonal lineage fates, transcriptomes, and surface markers yield two hematopoietic trees. (PNAS 2025)

- DOI: 10.1073/pnas.2505510122 | PMCID: PMC12684921 | PMID: 41284889
- Evidence: ( C ) UMAP plot showing the dimensionality reduction results for MPP based on ADT data from ( A ).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Breast cancer cell coculture induces normal lung fibroblast transition to CAFs, promoting tumor cell dormancy and therapy resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2423894122 | PMCID: PMC12663926 | PMID: 41269792
- Evidence: ( D ) Uniform manifold approximation and projection (UMAP) visualization of MB231 cell subclusters generated from independent reclustering of the tumor cell cluster from integrated scRNAseq of MB231 and LF monocultures with MB231-LF coculture ( E ) Fraction of cocultured or monocultured cells ( Left ) and each cell cycle phase ( Right ) in MB231 cell subclusters from D .
- Full pipeline: dimensionality reduction/clustering [GSVA, UMAP] -> visualisation [UMAP] -> stage not stated [CellChat]

### Dynamics and variegation in the Treg response to Interleukin-2. (PNAS 2025)

- DOI: 10.1073/pnas.2518991122 | PMCID: PMC12663944 | PMID: 41264258
- Evidence: A UMAP projection (Uniform Manifold Approximation and Projection) of the entire dataset is displayed in Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat, Signac v1.14.0]

### Putative muscle stem cells promote &lt;i&gt;Xenopus&lt;/i&gt; tail regeneration by modifying macrophage function via &lt;i&gt;c1qtnf3&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504410122 | PMCID: PMC12663952 | PMID: 41264239
- Evidence: ( A ) Uniform Manifold Approximation and Projection (UMAP) visualization of the integrated scRNA-seq data of the X. laevis tadpole tails, regeneration buds, and SP fraction of the regeneration buds at stage 41.
- Full pipeline: quality control [scDblFinder] -> read trimming [HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, Trimmomatic v0.39, edgeR v4.1.25, featureCounts v2.0.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.4, edgeR v4.1.25, featureCounts v2.0.6] -> visualisation [UMAP, scDblFinder] -> stage not stated [ImageJ, Monocle v1.2.7, Seurat, scVelo v0.3.1]

### Engineering a spatiotemporal macrophage circuit via STING phase separation to override immune suppression in pancreatic cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2504718122 | PMCID: PMC12664005 | PMID: 41264244
- Evidence: Uniform Manifold Approximation and Projection (UMAP) visualization revealed epithelial, T and B lymphocyte, myeloid, and stromal cells within the pancreatic tumor microenvironment.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellChat, GSEA]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Evidence: Consistent with this, uniform manifold approximation and projection ( UMAP ) analysis performed on the Perturb-seq dataset showed that ADGRL2 mRNA levels were low in progenitors but markedly elevated in differentiated cells, concordant with KRTDAP differentiation gene expression and inversely correlated to the MKI67 proliferation marker ( Fig.
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### Thalamus-cortex interactions drive cell type-specific cortical development in human pluripotent stem cell-derived assembloids. (PNAS 2025)

- DOI: 10.1073/pnas.2506573122 | PMCID: PMC12663968 | PMID: 41248276
- Evidence: However, Uniform Manifold Approximation and Projection (UMAP) mapping revealed a distinct separation between gene sets from unfused hCOs and hThCA-derived hCOs ( Fig.
- Full pipeline: alignment/mapping [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ]

### Rubisco is slow across the tree of life. (PNAS 2025)

- DOI: 10.1073/pnas.2501433122 | PMCID: PMC12663927 | PMID: 41248286
- Evidence: Multidimensional scaling (MDS) was performed to convert the distance matrix into a 6-dimensional vector space and a UMAP was subsequently applied to reduce the dimensions to 2.
- Full pipeline: alignment/mapping [Clustal Omega, MAFFT v7.475] -> normalisation [UMAP] -> dimensionality reduction/clustering [MAFFT v7.475, UMAP] -> stage not stated [scikit-learn]

### High-resolution single-cell analyses reveal evolutionary constraints and evolvability of sexual circuits in &lt;i&gt;Drosophila&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2516083122 | PMCID: PMC12663948 | PMID: 41248285
- Evidence: Right : UMAP representations of scRNA-seq data from four species, color-coded to match the dsx + parental clusters on the Left .
- Full pipeline: alignment/mapping [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP]

### An adipo-osteoprogenitor population in the endosteal niche contributes to bone and fat formation in adult mouse bone marrow. (PNAS 2025)

- DOI: 10.1073/pnas.2502436122 | PMCID: PMC12663985 | PMID: 41248279
- Evidence: For downstream analyses, filtered feature matrix files were analyzed with Seurat 4.1.1 for quality control, normalization, variable gene expression, dimension reduction, and clustering with UMAP.
- Full pipeline: quality control [Seurat v4.1.1, UMAP] -> normalisation [Seurat v4.1.1, UMAP] -> dimensionality reduction/clustering [GSEA, Seurat v4.1.1, UMAP]

### The SWI/SNF chromatin-remodeling subunit DPF2 regulates macrophage inflammation in intestinal injury via the CACNA1D-mediated MAPK pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2518762122 | PMCID: PMC12646317 | PMID: 41223220
- Evidence: ( B ) Uniform manifold approximation and projection (UMAP) of intestinal immune cells and macrophages in WTIR and KOIR groups.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> simulation/modelling [Monocle]

### MC1R determines healing outcomes in acute and chronic cutaneous wounds. (PNAS 2025)

- DOI: 10.1073/pnas.2503308122 | PMCID: PMC12646273 | PMID: 41218117
- Evidence: Data were normalized with SCTransform, filtered for quality, and clustered using PCA, UMAP, and shared nearest neighbor (SNN) analysis.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, ImageJ, R v4.2.2, Seurat v4.4]

### Erythroid precursors regulate local oxygen tension and repair outcomes in the bone marrow niche. (PNAS 2025)

- DOI: 10.1073/pnas.2522548122 | PMCID: PMC12646327 | PMID: 41218120
- Evidence: The entire 81,362-cell dataset was visualized in two dimensions using UMAP, and clustering was performed with Louvain clustering.
- Full pipeline: quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA v4.3.3, Seurat v4.0]

### Forward genetic screening in engineered colorectal cancer organoids identifies regulators of metastasis. (PNAS 2025)

- DOI: 10.1073/pnas.2510910122 | PMCID: PMC12646219 | PMID: 41218116
- Evidence: ( H and I ) Uniform Manifold Approximation and Projection (UMAP) for macrophage/monocyte populations profiled from sgSafe and sgBcl2l13–1 APK primary tumors colored by cluster ( H ) and genotype ( I ).
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Seurat]

### METTL3-dependent m6A RNA methylation suppresses aberrant mammary epithelial differentiation and neoplastic transformation. (PNAS 2025)

- DOI: 10.1073/pnas.2514643122 | PMCID: PMC12646209 | PMID: 41218124
- Evidence: ( G ) Uniform manifold approximation and projection (UMAP) visualization of scRNA-seq profiles showing single-cell populations of normal breast organoid culture cells transduced with sgRNA targeting METTL3 (sgMETTL3-4) or control (sgCtrl).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA]

### Early female germline development in &lt;i&gt;Xenopus laevis&lt;/i&gt;: Stem cells, nurse cells, and germline cysts. (PNAS 2025)

- DOI: 10.1073/pnas.2522343122 | PMCID: PMC12646306 | PMID: 41213017
- Evidence: UMAP analysis revealed 12 clusters forming a continuous developmental trajectory with two distinct arrangements ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [UMAP] -> stage not stated [Seurat]

### The RANK/RANKL axis controls vascular dynamics in the bone marrow. (PNAS 2025)

- DOI: 10.1073/pnas.2425366122 | PMCID: PMC12625855 | PMID: 41183210
- Evidence: ( A ) Uniform Manifold Approximation and Projection (UMAP) showing the clustering result of the BMECs ( Cdh5 + , and Pecam1 + ) integrated RANKL treatment and control group.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat]

### Glycolipid nanoparticles target the spleen and detarget the liver without charge. (PNAS 2025)

- DOI: 10.1073/pnas.2409569122 | PMCID: PMC12625924 | PMID: 41183194
- Evidence: This was followed by PCA dimensional reduction and UMAP clustering.
- Full pipeline: normalisation [Seurat v4.0.4] -> dimensionality reduction/clustering [UMAP] -> stage not stated [scDblFinder]

### p53 regulates the expression of histone modifiers to restrict stemness and maintain differentiated luminal identity in breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2522646122 | PMCID: PMC12595495 | PMID: 41160600
- Evidence: ( C ) Single cells from EpiTOF were visualized in two-dimensional space using UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, ggplot2, survival (R), tidyverse]

### Serum response factor is essential for endometrial function and prevention of inflammatory fibrosis. (PNAS 2025)

- DOI: 10.1073/pnas.2510060122 | PMCID: PMC12595411 | PMID: 41150713
- Evidence: We then converted mouse genes to human orthologs in our mouse scRNA-seq dataset and projected the combined Srf f/f and Srf d/d mouse dataset onto the HECA-NH UMAP ( Fig.
- Full pipeline: variant calling [CellChat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### Characterization of endothelin-converting enzyme 1 as a key enzyme in the multienzyme Aβ degradation pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2507450122 | PMCID: PMC12595483 | PMID: 41144673
- Evidence: 8 A and B ), we performed biocomputational analyses, including principal component analysis and uniform manifold approximation and projection (UMAP) for dimension reduction.
- Full pipeline: quantification [ImageJ] -> normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat]

### Single-cell metabolome and RNA-seq multiplexing on single plant cells. (PNAS 2025)

- DOI: 10.1073/pnas.2512828122 | PMCID: PMC12582292 | PMID: 41134629
- Evidence: Concentrations of twelve compounds were used as features for metabolite-guided dimensional reduction, and localization of compounds was used for annotating each cluster in metabolite-guided UMAP.
- Full pipeline: read trimming [RSEM v1.3.1, STAR v2.7.10a, fastp] -> alignment/mapping [RSEM v1.3.1, STAR v2.7.10a, fastp] -> quantification [RSEM v1.3.1, STAR v2.7.10a, fastp] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [Cytoscape] -> stage not stated [ImageJ, Seurat v5.0.1]

### Joint disruption of &lt;i&gt;Ret&lt;/i&gt; and &lt;i&gt;Ednrb&lt;/i&gt; transcription shifts cell fate trajectories in the enteric nervous system in Hirschsprung disease. (PNAS 2025)

- DOI: 10.1073/pnas.2507062122 | PMCID: PMC12582274 | PMID: 41118220
- Evidence: ( B ) UMAP display of WT mouse gut samples.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2] -> differential/statistical testing [DESeq2, clusterProfiler] -> simulation/modelling [Monocle] -> visualisation [clusterProfiler] -> stage not stated [Seurat]

### Disrupted developmental signaling induces novel transcriptional states. (PNAS 2025)

- DOI: 10.1073/pnas.2418351122 | PMCID: PMC12582265 | PMID: 41118206
- Evidence: ( A ) UMAP of the zebrafish embryo data integrated with DAISEE.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA]

### HIF2α negatively regulates MYCN protein levels and promotes a low-risk noradrenergic phenotype in neuroblastoma. (PNAS 2025)

- DOI: 10.1073/pnas.2516922122 | PMCID: PMC12582314 | PMID: 41118218
- Evidence: ( A – D ) Visualization of EPAS1 ( A ), DDC ( B ), and SLC18A1 ( C ) expression in UMAP plot of the developing human adrenal medulla 7 to 17 PCW ( D ), dataset from Jansky et al.
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [DESeq2, FastQC] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [DESeq2, FastQC, GSEA] -> visualisation [UMAP] -> stage not stated [R, Scanpy, Seurat]

### Single-cell sequencing uncovers sensory neuron-mediated CGRP signaling as a driver of sarcoma progression. (PNAS 2025)

- DOI: 10.1073/pnas.2500161122 | PMCID: PMC12582254 | PMID: 41118222
- Evidence: ( A ) Reduced-dimensionality (UMAP) visualization and clustering of xenograft tumor implants harvested from TrkA WT (10,586 cells) and TrkA F592A mice (6,628 cells), pooled from three mice per genotype.
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1.2] -> visualisation [UMAP] -> stage not stated [CellChat, Cytoscape]

### Invariant HVC size in female canaries singing under testosterone: Unlocking function through neural differentiation, not growth. (PNAS 2025)

- DOI: 10.1073/pnas.2426847122 | PMCID: PMC12582222 | PMID: 41115194
- Evidence: The nonlinear reduction UMAP was used to visualize the results.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP, ggplot2] -> stage not stated [ImageJ, R, Seurat v5.0.1]

### TMEM16F phospholipid scramblase regulates tumorigenesis by modulating the tumor immune microenvironment. (PNAS 2025)

- DOI: 10.1073/pnas.2513910122 | PMCID: PMC12557541 | PMID: 41100671
- Evidence: Uniform manifold approximation and projection (UMAP) was used to visualize cell clusters in UMAP plots.
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> visualisation [UMAP] -> stage not stated [ImageJ, Seurat v4.3.0]

### TCR signal-enhancing mutation alters lipid metabolism of thymocytes and impairs antitumor immunity of mature T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2507154122 | PMCID: PMC12557506 | PMID: 41100674
- Evidence: ( A ) UMAP of all thymic T cells from the WT and CD3ε I173A mice was colored by cell type annotation.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle]

### Protein disulfide isomerases regulate androgen receptor stability and promote prostate cancer cell growth and survival. (PNAS 2025)

- DOI: 10.1073/pnas.2509222122 | PMCID: PMC12557534 | PMID: 41086208
- Evidence: ( F ) UMAP showing the distribution of major cell types from a prostate cancer scRNA-seq dataset ( 45 ) ( Left ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v1.8, FastQC] -> alignment/mapping [STAR] -> normalisation [Bioconductor, DESeq2, R v3.4.1] -> dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [Bioconductor, DESeq2, R v3.4.1] -> structure determination [PHENIX v1.19.2, PyMOL v3.1] -> visualisation [PHENIX v1.19.2, PyMOL v3.1] -> stage not stated [Seurat, featureCounts]

### Inter- and intrahemispheric sources of vestibular signals to V1. (PNAS 2025)

- DOI: 10.1073/pnas.2503181122 | PMCID: PMC12541342 | PMID: 41071661
- Evidence: ( Middle ) Uniform manifold approximation and projection (UMAP) sorting of the responses, represented by the averaged Z-score of the FR across neurons.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Unexpected heterogeneity and tissue-specific properties of the thymic hematopoietic antigen-presenting cell network. (PNAS 2025)

- DOI: 10.1073/pnas.2508184122 | PMCID: PMC12541397 | PMID: 41071655
- Evidence: Shown is UMAP visualization of the broad lineages identified.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Structure of a transient protein-folding intermediate by pressure-jump NMR spectroscopy. (PNAS 2025)

- DOI: 10.1073/pnas.2519493122 | PMCID: PMC12541424 | PMID: 41060762
- Evidence: UMAP Embedding.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Biologically grounded neocortex computational primitives implemented on neuromorphic hardware improve vision transformer performance. (PNAS 2025)

- DOI: 10.1073/pnas.2504164122 | PMCID: PMC12541343 | PMID: 41055996
- Evidence: Mechanistically, UMAP projections showed that sWTA reorganizes latent representations into compact, domain-aligned clusters, unlike the diffuse or misaligned embeddings produced by traditional normalization ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP]

### Collagen-disrupting attIL12 TIL therapy boosts deep T cell infiltration via dual signaling activation and CCKAR reduction in sarcomas. (PNAS 2025)

- DOI: 10.1073/pnas.2507542122 | PMCID: PMC12541433 | PMID: 41052334
- Evidence: ( D – F ) UMAP dimension reduction ( Left ), heatmaps ( Top Right ), and graphs ( Bottom Right ) show phenotypic clusters of each treatment group.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R]

### Higher-order interactions in neuronal function: From genes to ionic currents in biophysical models. (PNAS 2025)

- DOI: 10.1073/pnas.2500048122 | PMCID: PMC12519081 | PMID: 41021808
- Evidence: ( A ) UMAP representation of IN transcriptomic clustering based on ion channel-encoding genes.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Scanpy]

### Ectopic transcription due to inherited histone methylation may interfere with the ongoing function of differentiated neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2513137122 | PMCID: PMC12501177 | PMID: 40991443
- Evidence: ( A – C ) UMAP projection of all 219 Wild Type cells (N2) ( A ) and 686 spr-5; met-2 mutant cells ( B ) from single-cell RNAseq integrated with the published ( 29 ) wild type (N2) single cell RNAseq data (purple dots show single-cell RNAseq compared to published data in lighter background).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [Fiji, ImageJ]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: ( A ) UMAP embedding of the 10 scRNA-seq samples consisting of 46,026 high-quality cells, partitioned into 14 distinct cell types.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### Triple checkpoint blockade of PD-1, Tim-3, and Lag-3 enhances adoptive T cell immunotherapy in a mouse model of ovarian cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2419888122 | PMCID: PMC12501118 | PMID: 40982684
- Evidence: Clustering was performed using the “FindNeighbors” function, and a UMAP dimensionality reduction, with the “runUMAP” function, was performed on the graph generated from the “FindNeighbors” function.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.3.1, Seurat v4.1.1.9001]

### Lymphatic dysfunction is linked to disease pathogenesis in Duchenne muscular dystrophy animal models. (PNAS 2025)

- DOI: 10.1073/pnas.2505656122 | PMCID: PMC12478126 | PMID: 40966282
- Evidence: UMAP showed four clusters of LMCs ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Evidence: ( A ) Uniform manifold approximation and projection (UMAP) embeddings of scRNA-seq profiles from in vitro activated CD4 + splenic T cells with or without atRA treatment. n = 5,922, n = 6,577, n = 3,710, and n = 5,394 cells for WT, KO, WT + atRA, and KO + atRA, respectively.
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### Humanization of CD47 enables development of functional human neutrophils via postirradiation remodeling of the bone marrow. (PNAS 2025)

- DOI: 10.1073/pnas.2426546122 | PMCID: PMC12478129 | PMID: 40956886
- Evidence: ( A ) UMAP visualization of sorted BM, blood, and spleen CD66b+ cells from reconstituted MaGIC mice analyzed by 10X Genomics Platform.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [R v4.2.3, Seurat v5.0.1]

### Peritumoral macrophages recruit eosinophils to promote antitumor immune responses in breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2504645122 | PMCID: PMC12478179 | PMID: 40953260
- Evidence: These clusters were then projected onto a Uniform Manifold Approximation and Projection (UMAP) plot, with cells of similar marker profiles clustering together ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Adaptation of seed dormancy to maternal climate occurs via intergenerational transport of abscisic acid. (PNAS 2025)

- DOI: 10.1073/pnas.2519319122 | PMCID: PMC12452922 | PMID: 40932768
- Evidence: ( C ) Genes enriched in expression in fruits or in different regions of seeds ( 25 ) plotted on UMAP plots as in A provide additional evidence to support our annotated tissue types.
- Full pipeline: read trimming [Bowtie2, Cutadapt, featureCounts] -> alignment/mapping [Bowtie2, Cutadapt, SAMtools, deepTools, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2, edgeR] -> visualisation [SAMtools, UMAP, deepTools] -> stage not stated [ImageJ, Seurat]

### Hybridoma-inspired strategy crafts tailored multifunctional exosomes for precision therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2424547122 | PMCID: PMC12452929 | PMID: 40924460
- Evidence: After quality control, 43,531 single cells were visualized using Uniform Manifold Approximation and Projection (UMAP).
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Single-cell transcriptome combined with genetic tracing reveals a roadmap of fibrosis formation during proliferative vitreoretinopathy. (PNAS 2025)

- DOI: 10.1073/pnas.2424487122 | PMCID: PMC12452882 | PMID: 40920930
- Evidence: Uniform manifold approximation and projection (UMAP) visualization unveiled an 8-cluster representation of the cells in PVR ( Fig.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Monocle, Slingshot] -> visualisation [UMAP] -> stage not stated [Cellpose, GSEA]

### Inflammation awakens dormant cancer cells by modulating the epithelial-mesenchymal phenotypic state. (PNAS 2025)

- DOI: 10.1073/pnas.2515009122 | PMCID: PMC12435312 | PMID: 40901881
- Evidence: Sum159low-1 cells, harvested from mice treated with or without bleomycin, could be divided into 9 clusters as illustrated in the two-dimensional space using the Uniform Manifold Approximation and Projection (UMAP) method ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Tumor-expressed GPNMB orchestrates Siglec-9&lt;sup&gt;+&lt;/sup&gt; TAM polarization and EMT to promote metastasis in triple-negative breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2503081122 | PMCID: PMC12435292 | PMID: 40892920
- Evidence: ( F ) scRNA-seq analysis ( GSE169246 ) identifying TAMs and TIMs clusters by UMAP projection.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [AlphaFold] -> machine learning [UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AutoDock Vina, GSEA, R v4.3.0]

### Using large language models to categorize strategic situations and decipher motivations behind human behaviors. (PNAS 2025)

- DOI: 10.1073/pnas.2512075122 | PMCID: PMC12415233 | PMID: 40875803
- Evidence: Behavioral codes are embedded into a high-dimensional semantic space using the OpenAI Ada model, and then reduced to two dimensions using UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Evolutionarily conserved grammar rules viral factories of amoeba-infecting members of the hyperdiverse &lt;i&gt;Nucleocytoviricota&lt;/i&gt; phylum. (PNAS 2025)

- DOI: 10.1073/pnas.2515074122 | PMCID: PMC12415211 | PMID: 40864652
- Evidence: ( C ) Uniform Manifold Approximation and Projection (UMAP) representation of the IDRs in representative genomes and metagenomics giant viruses, based on the 11 features selected for the classifier.
- Full pipeline: quantification [limma] -> dimensionality reduction/clustering [UMAP] -> machine learning [UMAP] -> visualisation [limma] -> stage not stated [HMMER v3.3.2, ImageJ]

### Cellular cartography reveals mouse prostate organization and determinants of castration resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2427116122 | PMCID: PMC12415206 | PMID: 40854129
- Evidence: ( B ) Uniform manifold approximation and projection (UMAP) of individual cells from scRNAseq of 9,439 cells from prostates of C57B6 and FVB mice.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, CellPhoneDB, GSVA, SCENIC]

### Efficiently quantifying dependence in massive scientific datasets using InterDependence Scores. (PNAS 2025)

- DOI: 10.1073/pnas.2509860122 | PMCID: PMC12403096 | PMID: 40833404
- Evidence: ( B ) A 2D UMAP visualization of 15,182 tokens ( SI Appendix , SI Methods , section 5 ) computed using IDS to measure token affinity.
- Full pipeline: dimensionality reduction/clustering [Python, UMAP] -> visualisation [UMAP]

### CO&lt;sub&gt;2&lt;/sub&gt; hydration at the air-water interface: A surface-mediated "in-and-out" mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2502684122 | PMCID: PMC12402993 | PMID: 40833411
- Evidence: S2 as a projected two-dimensional subspace using the UMAP transformation ( 58 , 59 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [LAMMPS, PLUMED]

### Layer 1 NDNF interneurons form distinct subpopulations with opposite activation patterns during sleep in freely behaving mice. (PNAS 2025)

- DOI: 10.1073/pnas.2503139122 | PMCID: PMC12377762 | PMID: 40811472
- Evidence: Parameters used for the UMAP (number of approximate nearest neighbors of 90 and minimum distance between points in low-dimensional space of 0.9) were chosen to preserve the uniformity of the data distribution on the manifold, maintain a locally constant metric, and ensure the manifold’s local connectivity.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [lme4] -> visualisation [ImageJ] -> stage not stated [Python]

### Blood-labyrinth barrier damage mediated by granzymes from cytotoxic lymphocytes results in hearing loss in systemic lupus erythematosus. (PNAS 2025)

- DOI: 10.1073/pnas.2423240122 | PMCID: PMC12377648 | PMID: 40794837
- Evidence: Unbiased clustering by uniform manifold approximation and projection (UMAP) analysis identified 16 distinct cell clusters based on their gene expression profiles ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, Cytoscape, GSVA, STRING db]

### Circulating cell-free RNA signatures for the characterization and diagnosis of myalgic encephalomyelitis/chronic fatigue syndrome. (PNAS 2025)

- DOI: 10.1073/pnas.2507345122 | PMCID: PMC12377778 | PMID: 40789036
- Evidence: ( B ) Uniform manifold approximation and projection (UMAP) from Vu et al.
- Full pipeline: quantification [Bracken] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> machine learning [DESeq2 v1.34.0] -> visualisation [ggplot2 v3.3.5] -> stage not stated [Kraken2, Snakemake]

### &lt;i&gt;Sox11&lt;/i&gt; genes affect neuronal differentiation in the developing zebrafish enteric nervous system. (PNAS 2025)

- DOI: 10.1073/pnas.2510548122 | PMCID: PMC12342651 | PMID: 40789027
- Evidence: After regressing out the source of variation from the expression of mitochondrial genes, we performed PCA and visualized the data in two dimensions by running the UMAP algorithm with the parameter settings as n_neighbors = 20 and n_pcs = 40.
- Full pipeline: alignment/mapping [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Python, Scanpy]

### Immune-responsive gene 1: The mitochondrial key to Th17 cell pathogenicity in CNS autoimmunity. (PNAS 2025)

- DOI: 10.1073/pnas.2427052122 | PMCID: PMC12358831 | PMID: 40758870
- Evidence: ( A ) UMAP projection of single-cell transcriptomes from the spinal cords of wild-type (Wt) and Irg1 -KO mice at 21 d postimmunization (dpi), revealing 11 transcriptionally distinct cell clusters, identified as aMac, iMono, aiMac, T cell-1, cDC, aMG, Neutrophil, T cell-2, B cell, trMac, and moDC.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### A recurrent de novo damaging variant in &lt;i&gt;EMP2&lt;/i&gt; causes progressive symmetric erythrokeratoderma. (PNAS 2025)

- DOI: 10.1073/pnas.2509896122 | PMCID: PMC12358830 | PMID: 40758889
- Evidence: UMAP, uniform manifold approximation and projection.
- Full pipeline: alignment/mapping [GATK] -> variant calling [GATK] -> quantification [QuPath] -> dimensionality reduction/clustering [Monocle, Seurat, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ANNOVAR]

### Serum metabolic patterns reveal the diagnostic and prognostic role of alanine abnormality in ocular adnexal lymphoma. (PNAS 2025)

- DOI: 10.1073/pnas.2506345122 | PMCID: PMC12337266 | PMID: 40743387
- Evidence: ( F ) Principal component analysis (PCA) score plot, ( G ) t-distributed stochastic neighbor embedding (t-SNE) map, and ( H ) uniform manifold approximation and projection (UMAP) visualization of SMPs of OAL patients (red) and non-OAL participants (blue).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R v4.1.1]

### &lt;i&gt;DICER-LIKE 5&lt;/i&gt; loss causes thermosensitive male sterility in durum wheat and reveals an AU-rich motif guiding 24-nt phasiRNA biogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2504349122 | PMCID: PMC12337324 | PMID: 40737328
- Evidence: UMAP clustering of 2,758 cells reveals eight distinct clusters ( A ) representing dcl5 and WT genotypes ( B ) from 0.4 mm premeiotic and 1.0 mm meiotic durum wheat anthers ( C ) categorized by their sterile or fertile status ( D ).
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [BLAST v2.11.0, HISAT2 v2.2.1, SAMtools, StringTie v2.2.1] -> variant calling [UMAP] -> quantification [SAMtools, pheatmap v1.0.12] -> normalisation [Seurat v5.1, edgeR, pheatmap v1.0.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr] -> structure determination [HISAT2 v2.2.1] -> visualisation [R, ggplot2, pheatmap v1.0.12] -> stage not stated [BEDTools, ImageJ]

### SMARCA5 restricts chromatin accessibility to promote male meiosis and fertility in mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422356122 | PMCID: PMC12337329 | PMID: 40743397
- Evidence: Clusters were identified at a resolution of 0.5, RunUMAP() was used to generate UMAP objects, and clusters were further defined using key spermatogenic genes ( 46 , 54 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Picard] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, ImageJ, MACS2, Seurat v4.1.0, SoupX, deepTools, ggplot2]

### <i>Prg4</i>+ fibroadipogenic progenitors in muscle are crucial for bone fracture repair. (PNAS 2025)

- DOI: 10.1073/pnas.2417806122 | PMCID: PMC12337308 | PMID: 40729389
- Evidence: (Scale bar, 20 μm, n = 3 mice.) ( C ) The Uniform Manifold Approximation and Projection (UMAP) plot of nonmyogenic mesenchymal cells in mouse muscle.
- Full pipeline: quantification [ImageJ] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP]

### Integrating spatial omics and single-cell mass spectrometry imaging reveals tumor-host metabolic interplay in hepatocellular carcinoma. (PNAS 2025)

- DOI: 10.1073/pnas.2505789122 | PMCID: PMC12337300 | PMID: 40729385
- Evidence: After integrating the transcriptional data from all ST spots in HCC sections in batch 1, we performed UMAP analysis and generated 12 main clusters ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### A granulin-positive macrophage subtype in mycobacterial granulomas alleviates tissue damage by limiting excessive inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2413946122 | PMCID: PMC12337285 | PMID: 40729382
- Evidence: ( A ) UMAP plot of all cells from the four samples, with 15 generic cell types identified by different colors, as indicated on the Right side of the plot.
- Full pipeline: quality control [HISAT2] -> alignment/mapping [HISAT2] -> quantification [HTSeq] -> normalisation [Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler] -> stage not stated [DESeq2, STRING db]

### Effects of the gut microbiota on placental angiogenesis and intrauterine growth in gnotobiotic mice. (PNAS 2025)

- DOI: 10.1073/pnas.2426341122 | PMCID: PMC12318179 | PMID: 40711921
- Evidence: ( A ) UMAP representation of 32,571 nuclei across ten E11.5 placentas (3 CONV-R, 3 GF, and 4 CONV-D) clustered and assigned to 21 cell types.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, lme4] -> stage not stated [QuPath v0.4.4]

### Epigenetic instability and hypofunctionality of fetal Tregs allow a permissive regulatory environment for T effector memory maturation. (PNAS 2025)

- DOI: 10.1073/pnas.2506673122 | PMCID: PMC12318238 | PMID: 40705427
- Evidence: ( C ) UMAP dimensionality reduction of circulatory CD3 + T cell in ( Left ) cell density contour maps reflecting log percentage frequency distribution or ( Right ) marker expression intensity.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP]

### Cell type-specific purifying selection of synonymous mitochondrial DNA variation. (PNAS 2025)

- DOI: 10.1073/pnas.2505704122 | PMCID: PMC12318227 | PMID: 40705423
- Evidence: For PBMC cell type annotations, granular cell type labels and UMAP coordinates were established by using the Seurat Dictionary Learning ( 45 ) for cross-modality integration.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Cutadapt] -> variant calling [freebayes] -> dimensionality reduction/clustering [UMAP] -> visualisation [Seurat, Signac] -> stage not stated [GATK, Picard]

### &lt;i&gt;Cdc42&lt;/i&gt; defect reveals insights into microvilli organization and function in T cell immunity. (PNAS 2025)

- DOI: 10.1073/pnas.2505291122 | PMCID: PMC12318239 | PMID: 40711916
- Evidence: ( A ) Schematic diagram of scRNA-seq process and UMAP visualization of the cellular composition of Cdc42 f/f (WT) and Cdc42 f/f CD4Cre (KO) mice thymus.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### SETDB1 ensures the continuity of embryonic to adult neural stem cells through metabolic alterations in the dentate gyrus. (PNAS 2025)

- DOI: 10.1073/pnas.2424315122 | PMCID: PMC12318225 | PMID: 40699919
- Evidence: Unsupervised clustering using UMAP identified 14 cell clusters, including neural progenitor cells (such as radial glial cells (RGCs), neuronal intermediate progenitors (nIPCs)) and glial cells (astrocytes and oligodendrocytes (OL)), and neurons ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Monocle]

### Cell-type-informed genotyping of mosaic focal epilepsies reveals cell-autonomous and non-cell-autonomous disease-associated transcriptional programs. (PNAS 2025)

- DOI: 10.1073/pnas.2509622122 | PMCID: PMC12305027 | PMID: 40674414
- Evidence: ( B ) Uniform manifold approximation and projection (UMAP) showing cell type clusters identified in the integrated [Harmony ( 16 )] case and control snRNA-seq atlas.
- Full pipeline: normalisation [Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0, UMAP] -> differential/statistical testing [GSEA] -> stage not stated [CellChat, fgsea v1.28.0]

### Foxn3 is required to suppress aberrant ciliogenesis in nonphotoreceptor retinal neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2500871122 | PMCID: PMC12304973 | PMID: 40663603
- Evidence: Unsupervised combined with marker-based uniform manifold approximation and projection (UMAP) clustering was then performed using Seurat 4 ( 47 ) to identify the clusters of the six major retinal neuron types and the Müller glia (MG) cluster ( Fig.
- Full pipeline: alignment/mapping [HISAT2] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [HOMER, Seurat, deepTools, scDblFinder]

### Patient-reported treatment outcomes in ME/CFS and long COVID. (PNAS 2025)

- DOI: 10.1073/pnas.2426874122 | PMCID: PMC12280984 | PMID: 40627388
- Evidence: Uniform manifold approximation and projection (UMAP) ( 64 , 65 ) was used to transform the high-dimensional patient data, encompassing demographic information, symptoms, and comorbidities into a two-dimensional space.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### CDKN1B (p27/kip1) enhances drug-tolerant persister CTCs by restricting polyploidy following mitotic inhibitors. (PNAS 2025)

- DOI: 10.1073/pnas.2507203122 | PMCID: PMC12280942 | PMID: 40623195
- Evidence: Single-Cell RNA-Seq Data and UMAP Analyses.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [ImageJ]

### Acyl-CoA-binding protein as a driver of pathological aging. (PNAS 2025)

- DOI: 10.1073/pnas.2501584122 | PMCID: PMC12280937 | PMID: 40623176
- Evidence: ( A ) 2D projection of the first two dimensions from the Uniform Manifold Approximation Projection (UMAP) of the 14 clusters, corresponding to cell populations, were identified based on their nuclear transcription profiles.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Spin-informed universal graph neural networks for simulating magnetic ordering. (PNAS 2025)

- DOI: 10.1073/pnas.2422973122 | PMCID: PMC12260432 | PMID: 40591595
- Evidence: To better illustrate this, the extracted atom embeddings were projected into 2D space using UMAP ( 31 ).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### FcγRIIIa is a noncanonical costimulatory molecule for CD8 T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2509016122 | PMCID: PMC12260523 | PMID: 40591599
- Evidence: Cells were clustered and visualized using UMAP reduction (UMAP plugin v.4.0) and populations were identified using self-organizing maps (FlowSOM v.3.0) ( 53 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat v3.0.0]

### Retinoic acid receptor assembly dynamics governs dual functions in cochlear organogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2426739122 | PMCID: PMC12232719 | PMID: 40577120
- Evidence: We used UMAP to visualize the scRNA-seq clustering results and metadata information, such as read depth and sample ID.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Testicular somatic and germ cell maturation during rhesus macaque development. (PNAS 2025)

- DOI: 10.1073/pnas.2419995122 | PMCID: PMC12232671 | PMID: 40569389
- Evidence: (Scale bar, 20 µm.) ( D ) UMAP plot of 227,944 testicular cells revealing distinct clustering of W8 testis samples (red) relative to W15 (green) and W19 (blue) samples.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [limma] -> simulation/modelling [Monocle]

### Genome-scale knockout simulation and clustering analysis of drug-resistant breast cancer cells reveal drug sensitization targets. (PNAS 2025)

- DOI: 10.1073/pnas.2425384122 | PMCID: PMC12232641 | PMID: 40560621
- Evidence: All the materials and methods conducted in this study are detailed in SI Appendix , Materials and Methods : generation of cell-specific GEMs, single-gene knockout simulation, clustering of knockout flux data using UMAP and k -means clustering, flux enrichment analysis, prediction of gene targets using rMTA, cell culture, identification of single nucleotide polymorphisms, metabolome analysis, enric...
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [UMAP]

### Setdb1 ablation in macrophages attenuates fibrosis in heart allografts. (PNAS 2025)

- DOI: 10.1073/pnas.2424534122 | PMCID: PMC12232555 | PMID: 40553495
- Evidence: ( A ) Uniform Manifold Approximation and Projection (UMAP) plots for the identification of different single cell clusters in human myocardial tissue obtained after heart transplantation.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, PyMOL]

### Bone morphogenetic protein-9 controls pulmonary vascular growth and remodeling. (PNAS 2025)

- DOI: 10.1073/pnas.2410229122 | PMCID: PMC12232436 | PMID: 40549904
- Evidence: ( A ) Transcriptomic profile of each cell (dots) represented by a Uniform Manifold Approximation and Projection (UMAP), annotated from C1 to C5 under basal conditions (without BMP-9 stimulation, 0ng/mL) and C1' to C5' upon BMP-9 stimulation (10ng/mL), showing differential expression of BMP receptors across the five clusters (n = 10).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat, UMAP] -> stage not stated [GSEA]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Evidence: This graph was embedded in two dimensions using UMAP (sc.tl.umap).
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### Sp140L functions as a herpesvirus restriction factor suppressing viral transcription and activating interferon-stimulated genes. (PNAS 2025)

- DOI: 10.1073/pnas.2426339122 | PMCID: PMC12207491 | PMID: 40526717
- Evidence: Dimensional reduction integrating all seven samples generated a single Uniform Manifold Approximation and Projection (UMAP) for further analysis ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [AlphaFold]

### Feedback regulation between histone lactylation and ALKBH3-mediated glycolysis regulates age-related macular degeneration pathology. (PNAS 2025)

- DOI: 10.1073/pnas.2416046122 | PMCID: PMC12184506 | PMID: 40493193
- Evidence: Using Seurat UMAP for dimensionality reduction and clustering, we identified 10 cell populations ( Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [GSEA]

### Predicting high-fitness viral protein variants with Bayesian active learning and biophysics. (PNAS 2025)

- DOI: 10.1073/pnas.2503742122 | PMCID: PMC12184641 | PMID: 40489612
- Evidence: ( B ) UMAP visualization of sequence space comparing acquired variants (orange) against all top sequences (blue) and background sequences (gray) using UCB ( Left ) and greedy ( Right ) acquisition strategies.
- Full pipeline: alignment/mapping [MAFFT] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [scikit-learn]

### Cross-species modeling of plant genomes at single-nucleotide resolution using a pretrained DNA language model. (PNAS 2025)

- DOI: 10.1073/pnas.2421738122 | PMCID: PMC12184517 | PMID: 40489624
- Evidence: ( C ) UMAP visualization of embeddings from PlantCaduceus (32 layers) averaged over nonoverlapping 100-bp windows along the sorghum genome without intergenic regions.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [XGBoost] -> visualisation [UMAP] -> stage not stated [BEDTools, BUSCO, VEP]

### Sleep deficiency exacerbates periodontal inflammation via trigeminal TRPV1 neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2424169122 | PMCID: PMC12184432 | PMID: 40489620
- Evidence: ( B ) Cell clusters of TG visualized through UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Amortized template matching of molecular conformations from cryoelectron microscopy images using simulation-based inference. (PNAS 2025)

- DOI: 10.1073/pnas.2420158122 | PMCID: PMC12168013 | PMID: 40465628
- Evidence: A slender appendix in the 2D UMAP’ plot containing high-confidence points detaches from the distribution of points on the top of the plot.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [PyTorch] -> stage not stated [cryoDRGN]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: ( A ) UMAP plots of VEC, AEC, HEC, M-HSPC, L-HSPC, and E-HSPC in integrating scRNA-seq data of WT and jund −/− cells.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Single-cell resolution uncovers neighboring cell subtypes that share steroidogenic capacity during fetal testis development. (PNAS 2025)

- DOI: 10.1073/pnas.2501392122 | PMCID: PMC12167995 | PMID: 40460128
- Evidence: ( A – F ) Uniform manifold approximation and projection (UMAP) representations of E13.5 testis cells colored by ( A ) annotation; ( B ) Star expression; ( C ) Cyp17a1 expression; ( D ) Cyp11a1 expression; ( E ) Hsd3b1 expression; and ( F ) Hsd17b3 expression.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat v5.0.1]

### Mgat4b-mediated selective &lt;i&gt;N&lt;/i&gt;-glycosylation regulates melanocyte development and melanoma progression. (PNAS 2025)

- DOI: 10.1073/pnas.2423831122 | PMCID: PMC12146715 | PMID: 40424122
- Evidence: ( A ) UMAP visualization of the Zebrafish Sox10+ve cells colored by the identified states.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Seurat]

### Manifold fitting reveals metabolomic heterogeneity and disease associations in UK Biobank populations. (PNAS 2025)

- DOI: 10.1073/pnas.2500001122 | PMCID: PMC12146735 | PMID: 40434639
- Evidence: Dimension reduction and two-dimensional UMAP visualization reveal nonlinear dependencies and clustering features among the biomarkers ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Specialized molecular pathways drive the formation of light-scattering assemblies in leucophores. (PNAS 2025)

- DOI: 10.1073/pnas.2424979122 | PMCID: PMC12146710 | PMID: 40434648
- Evidence: UMAP reduction was calculated using also 20 PCs.
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> structure determination [IMOD] -> stage not stated [Seurat v4.3.0]

### The IL-18 receptor is expressed on murine small-intestinal enterochromaffin cells and executes a recovery program upon injury. (PNAS 2025)

- DOI: 10.1073/pnas.2417149122 | PMCID: PMC12146721 | PMID: 40424129
- Evidence: ( A ) UMAP of murine small-intestinal IECs with Louvain clusters labeled.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Learning to estimate sample-specific transcriptional networks for 7,000 tumors. (PNAS 2025)

- DOI: 10.1073/pnas.2411930122 | PMCID: PMC12130817 | PMID: 40408406
- Evidence: UMAP embeddings, colored by disease type, reveal the organization of different data views with respect to known disease types.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Cancer-associated fibroblast-derived SEMA3C facilitates colorectal cancer liver metastasis via NRP2-mediated MAPK activation. (PNAS 2025)

- DOI: 10.1073/pnas.2423077122 | PMCID: PMC12130859 | PMID: 40402249
- Evidence: ( A ) Uniform manifold approximation and projection (UMAP) plot showing 11 cell clusters of primary CRC and liver metastatic patients.
- Full pipeline: quality control [Harmony, R, Seurat v4.4.0] -> quantification [R, Seurat v4.4.0] -> normalisation [Harmony] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [CellPhoneDB, GSEA, GSVA, Monocle, scDblFinder v2.0.3, survival (R)]

### Phase separation of RXRγ drives tumor chemoresistance and represents a therapeutic target for small-cell lung cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2421199122 | PMCID: PMC12130815 | PMID: 40392852
- Evidence: ( C ) UMAP plot showing the expression of the RXRγ gene in various cell types from normal lung, naïve tumors, and chemo-resistant tumors.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Inflammatory cytokine upd3 induces axon length-dependent synapse removal by glia. (PNAS 2025)

- DOI: 10.1073/pnas.2422752122 | PMCID: PMC12130839 | PMID: 40392850
- Evidence: The clustering result was visualized in the UMAP plot with 19 clusters (cluster 0 to cluster 18) for sample 1 and 14 clusters (cluster 0 to cluster 13) for sample 2.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt v2.4, FastQC, MultiQC, kallisto v0.46.0] -> alignment/mapping [Cutadapt v2.4, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DESeq2, Fiji, ImageJ, Seurat, scDblFinder v2.0.3]

### Induction of the ISR by AB5 subtilase cytotoxin drives type-I IFN expression in pDCs via STING activation. (PNAS 2025)

- DOI: 10.1073/pnas.2421258122 | PMCID: PMC12130819 | PMID: 40388626
- Evidence: Uniform Manifold Approximation and Projection (UMAP) dimension reduction applied to multiparameter flow cytometry analysis of CD45 + cells from three healthy donors were performed.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr]

### An RNA-binding regulatory cascade controls the switch from proliferation to differentiation in the &lt;i&gt;Drosophila&lt;/i&gt; male germ cell lineage. (PNAS 2025)

- DOI: 10.1073/pnas.2418279122 | PMCID: PMC12107169 | PMID: 40377994
- Evidence: ( F ) UMAP visualization of single nuclear RNA sequencing data from the Fly Cell Atlas ( 5 ), after the nuclei in the two earliest male germ line clusters (Leiden resolution 6.0) were reclustered.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Shared host genetic landscape of respiratory viral infection. (PNAS 2025)

- DOI: 10.1073/pnas.2414202122 | PMCID: PMC12107129 | PMID: 40372436
- Evidence: In particular for visualization, we apply K-means clustering and layout into two dimensions by UMAP.
- Full pipeline: normalisation [fgsea] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Interferon-induced activation of dendritic cells and monocytes by yellow fever vaccination correlates with early antibody responses. (PNAS 2025)

- DOI: 10.1073/pnas.2422236122 | PMCID: PMC12088451 | PMID: 40333758
- Evidence: ( A ) UMAP visualization of concatenated scRNA-seq data with the annotated cell clusters (Louvain) indicated by colors.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ggpubr v0.5.0] -> visualisation [UMAP] -> stage not stated [DESeq2 v1.34.0, GSEA, HTSeq, Seurat, fgsea, scVelo]

### Circadian clock-gated cell renewal controls time-dependent changes in taste sensitivity. (PNAS 2025)

- DOI: 10.1073/pnas.2421421122 | PMCID: PMC12088436 | PMID: 40339128
- Evidence: The taste cell marker gene-expressing cells are distributed throughout the clusters and did not form specific clusters in the uniformmanifold approximation projection (UMAP) graph ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [R, Seurat]

### Hdac1 as an early determinant of intermediate-exhausted CD8<sup>+</sup> T cell fate in chronic viral infection. (PNAS 2025)

- DOI: 10.1073/pnas.2502256122 | PMCID: PMC12088444 | PMID: 40333757
- Evidence: As visualized on a UMAP, most of Hdac1 –/– cells aggregated next to WT cells with partial overlaps ( Fig.
- Full pipeline: variant calling [Monocle] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [HOMER] -> simulation/modelling [Monocle] -> visualisation [UMAP]

### Single-cell elderly blood-CSF atlas implicates peripherally influenced immune dysregulation in normal pressure hydrocephalus. (PNAS 2025)

- DOI: 10.1073/pnas.2412159122 | PMCID: PMC12087963 | PMID: 40324076
- Evidence: ( A ) Uniform Manifold Approximation and Projection (UMAP) plot representing 13 color-coded cell clusters identified in merged single-cell transcriptomes of blood (128,027) and CSF (12,180) cells from 10 iNPH patients.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### De novo DUOX2 expression in neutrophil subsets shapes the pathogenesis of intestinal disease. (PNAS 2025)

- DOI: 10.1073/pnas.2421747122 | PMCID: PMC12088431 | PMID: 40327691
- Evidence: ( C ) UMAP projection of all combined cells obtained by scRNA-seq of purified sorted colPMNs.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### NEUROD1 efficiently converts peripheral blood cells into neurons with partial reprogramming by pluripotency factors. (PNAS 2025)

- DOI: 10.1073/pnas.2401387122 | PMCID: PMC12067290 | PMID: 40299704
- Evidence: Trajectory analysis using Monocle3 on UMAP indicated a continuum between NSC cluster and neuron cluster, while showing a notable distinction from iPSC cluster ( Fig.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP, scVelo] -> simulation/modelling [Monocle, UMAP]

### Comparative single-cell analysis of transcriptional bursting reveals the role of genome organization in de novo transcript origination. (PNAS 2025)

- DOI: 10.1073/pnas.2425618122 | PMCID: PMC12067204 | PMID: 40305051
- Evidence: When standard batch correction techniques, such as Monocle3’s implementation of batchelor via “align_cds()” ( 6 , 43 ), are applied to remove species-specific effects, Uniform Manifold Approximation and Projection (UMAP) and Principle Component Analysis (PCA) projections show that these effects have been removed with entirely overlapping cell type assignments despite species-specific differences i...
- Full pipeline: alignment/mapping [Monocle, UMAP] -> normalisation [Monocle, UMAP] -> dimensionality reduction/clustering [Monocle, UMAP]

### Integrating single-cell data with biological variables. (PNAS 2025)

- DOI: 10.1073/pnas.2416516122 | PMCID: PMC12067276 | PMID: 40294274
- Evidence: Visualization using uniform manifold approximation and projection (UMAP) ( 21 ) showed that SIGNAL well mixed cells from multiple batches and distinguished different cell types across all datasets ( SI Appendix , Figs.
- Full pipeline: dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [Seurat] -> machine learning [Seurat] -> visualisation [UMAP] -> stage not stated [R]

### LACE-UP: An ensemble machine-learning method for health subtype classification on multidimensional binary data. (PNAS 2025)

- DOI: 10.1073/pnas.2423341122 | PMCID: PMC12054798 | PMID: 40267132
- Evidence: We can utilize principal component analysis to extract the main axes of variation from the posterior probability matrices in the hope that noisy axes average out in the subsequent UMAP nearest neighbor graph stage.
- Full pipeline: dimensionality reduction/clustering [Python, UMAP] -> simulation/modelling [igraph]

### &lt;i&gt;NAT10&lt;/i&gt; exacerbates acute renal inflammation by enhancing N4-acetylcytidine modification of the CCL2/CXCL1 axis. (PNAS 2025)

- DOI: 10.1073/pnas.2418409122 | PMCID: PMC12054813 | PMID: 40261924
- Evidence: ( A ) Uniform manifold approximation and projection (UMAP) of cell type clustering in human kidneys.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [HOMER]

### Proteostasis landscapes of cystic fibrosis variants reveal drug response vulnerability. (PNAS 2025)

- DOI: 10.1073/pnas.2418407122 | PMCID: PMC12054793 | PMID: 40261935
- Evidence: Notably, perpendicular axes shifts, e.g. x vs. y axis, played out in t-SNE and UMAP dimensionality reduction ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Python, SciPy]

### Mapping the developmental profile of ventricular zone-derived neurons in the human cerebellum. (PNAS 2025)

- DOI: 10.1073/pnas.2415425122 | PMCID: PMC12054822 | PMID: 40249772
- Evidence: Single-cell clustering was performed by first using principal component from which 20 principal components were used to construct a uniform manifold approximation and projection (UMAP) embedding in Seurat v4.3.0 ( 49 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [R, Seurat v4.0.2]

### MFRP is a molecular hub that organizes the apical membrane of RPE cells by engaging in interactions with specific proteins and lipids. (PNAS 2025)

- DOI: 10.1073/pnas.2425523122 | PMCID: PMC12036977 | PMID: 40249779
- Evidence: ( C ) UMAP plot showing MFRP expression level in various human ocular cell types.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### St3gal5-mediated sialylation of glyco-CD177 on neutrophils restricts neuroinflammation following CNS injury. (PNAS 2025)

- DOI: 10.1073/pnas.2426187122 | PMCID: PMC12037025 | PMID: 40244680
- Evidence: ( I ) UMAP plot of neutrophils isolated from the brain at 3d after MCAO from CD177 −/− and CD177 +/+ mice.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### FAO-fueled OXPHOS and NRF2-mediated stress resilience in MICs drive lymph node metastasis. (PNAS 2025)

- DOI: 10.1073/pnas.2411241122 | PMCID: PMC12012528 | PMID: 40215279
- Evidence: Utilizing principal component analysis and the Uniform Manifold Approximation and Projection (UMAP) algorithm, we identified eighteen distinct subclusters showing differential gene expression patterns, highlighting the extensive heterogeneity within tumor cell populations ( Fig.
- Full pipeline: dimensionality reduction/clustering [GSEA, UMAP] -> differential/statistical testing [UMAP]

### Astrocytic Ryk signaling coordinates scarring and wound healing after spinal cord injury. (PNAS 2025)

- DOI: 10.1073/pnas.2417400122 | PMCID: PMC12012454 | PMID: 40208942
- Evidence: ( A ) UMAP plot of major cell types (18,203 cells).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat]

### Downregulation of Nesprin1 by Runx2 deficiency is critical for the development of skeletal laminopathy-like pathology. (PNAS 2025)

- DOI: 10.1073/pnas.2320138122 | PMCID: PMC12012476 | PMID: 40208950
- Evidence: In all human iPS cells stimulated for 14 d with OBM, nine major cell types were identified using uniform manifold approximation and projection (UMAP) analysis ( SI Appendix , Fig.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP, scVelo] -> stage not stated [Galaxy, ImageJ, Python, Scanpy, deepTools]

### An integrated AI knowledge graph framework of bacterial enzymology and metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2425048122 | PMCID: PMC12012490 | PMID: 40193601
- Evidence: 4 C catalogs the distribution of these GCFs in a two-dimensional UMAP projection ( 42 ) ( SI Appendix ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, HMMER, PyTorch, Python, SciPy]

### Dual genetic tracing demonstrates the heterogeneous differentiation and function of neuromesodermal progenitors in vivo. (PNAS 2025)

- DOI: 10.1073/pnas.2402305122 | PMCID: PMC12002027 | PMID: 40178900
- Evidence: ( B ) Uniform Manifold Approximation and Projection (UMAP) embedding showing 14 clusters of 15,250 single cells.
- Full pipeline: quality control [Seurat] -> dimensionality reduction/clustering [CellChat, UMAP]

### DDX54 downregulation enhances anti-PD1 therapy in immune-desert lung tumors with high tumor mutational burden. (PNAS 2025)

- DOI: 10.1073/pnas.2412310122 | PMCID: PMC12002276 | PMID: 40172969
- Evidence: ( B ) Uniform Manifold Approximation and Projection (UMAP) embedding of single cells in the cancer tissues from the syngeneic mouse model annotated by cell types using spatial transcriptome data.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Lung B cells in ectopic germinal centers undergo affinity maturation. (PNAS 2025)

- DOI: 10.1073/pnas.2416855122 | PMCID: PMC12002176 | PMID: 40168127
- Evidence: Cell gene expression was reduced to two dimensions with UMAP, and clustered with the Leiden algorithm ( 64 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.3.1] -> stage not stated [Python, Scanpy v1.10.4]

### Signaling networks in cancer stromal senescent cells establish malignant microenvironment. (PNAS 2025)

- DOI: 10.1073/pnas.2412818122 | PMCID: PMC12002233 | PMID: 40168129
- Evidence: ( C ) UMAP visualization of single-cell transcriptomes of tumor stromal cells from the mouse model as in ( A ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA]

### Single cell-resolved cellular, transcriptional, and epigenetic changes in mouse T cell populations linked to age-associated immune decline. (PNAS 2025)

- DOI: 10.1073/pnas.2425992122 | PMCID: PMC12002302 | PMID: 40163732
- Evidence: Uniform ManifoldApproximation and Projection (UMAP) was employed for dimensionality reduction.
- Full pipeline: quality control [Scanpy v1.4.6] -> normalisation [Seurat] -> dimensionality reduction/clustering [ArchR v1.0.1, MACS2, Seurat, UMAP]

### Acute TREM2 inhibition depletes MAFB-high microglia and hinders remyelination. (PNAS 2025)

- DOI: 10.1073/pnas.2426786122 | PMCID: PMC12002275 | PMID: 40131948
- Evidence: ( F ) UMAP plot of 95,255 nuclei showing 7 distinguished cell-type identities determined by expression of specific markers. n = 2 mice in untreated; n = 3 in demyelination + αTREM2; n = 3 in demyelination + Ctrl IgG2a; n = 3 in remyelination + αTREM2; and n = 3 in remyelination + Ctrl IgG2a.
- Full pipeline: alignment/mapping [Monocle, Seurat] -> dimensionality reduction/clustering [Monocle, SCENIC, Seurat, UMAP] -> simulation/modelling [Monocle, Seurat]

### The FBXW7-KMT2 axis in cancer-associated fibroblasts controls tumor growth via an epigenetic-paracrine mechanism. (PNAS 2025)

- DOI: 10.1073/pnas.2423130122 | PMCID: PMC12002300 | PMID: 40127278
- Evidence: Using uniform manifold approximation and projection (UMAP) visualization, the cell populations in pancreatic cancer tissues were delineated into nine distinct clusters with annotations based on specifically expressed genes and canonical markers ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ]

### ETV5 reduces androgen receptor expression and induces neural stem-like properties during neuroendocrine prostate cancer development. (PNAS 2025)

- DOI: 10.1073/pnas.2420313122 | PMCID: PMC11962414 | PMID: 40117308
- Evidence: ( C ) Uniform manifold approximation and projection (UMAP) visualization of eight epithelial cell subclusters from integrated single-cell RNA-seq data from six patients with CRPC or NEPC ( Left ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA]

### Ectopic germinal centers in the nasal turbinates contribute to B cell immunity to intranasal viral infection and vaccination. (PNAS 2025)

- DOI: 10.1073/pnas.2421724122 | PMCID: PMC11962485 | PMID: 40112112
- Evidence: Features were clustered and cells visualized using UMAP ( 62 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat]

### Dnmt3a-mediated hypermethylation of FoxO3 promotes redox imbalance during osteoclastogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2418023122 | PMCID: PMC11962505 | PMID: 40106360
- Evidence: The Unified Manifold Approximation and Projection (UMAP) algorithm was used to reduce dimensionality.
- Full pipeline: quality control [R, Seurat] -> dimensionality reduction/clustering [UMAP]

### An atlas of early human mandibular endochondral and osteogenic paracrine signaling regions of Meckel's cartilage. (PNAS 2025)

- DOI: 10.1073/pnas.2420466122 | PMCID: PMC11962497 | PMID: 40096606
- Evidence: Principal component analysis (PCA) and UMAP were used for dimensionality reduction to visualize cell–cell relationships.
- Full pipeline: normalisation [Harmony v1.2.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib v3.7.2, UMAP] -> stage not stated [CellChat, CellPhoneDB, Seurat v4.0.0]

### iPSCs engrafted in allogeneic hosts without immunosuppression induce donor-specific tolerance to secondary allografts. (PNAS 2025)

- DOI: 10.1073/pnas.2413398122 | PMCID: PMC11929385 | PMID: 40073064
- Evidence: Uniform Manifold Approximation and Projection (UMAP) allowed us to assign cells to thirteen clusters.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2, tidyverse] -> stage not stated [R, Seurat v4.0.1]

### Expansion and pathogenic activation of skeletal muscle-resident macrophages in &lt;i&gt;mdx&lt;sup&gt;5cv&lt;/sup&gt;/Ccr2&lt;sup&gt;-/-&lt;/sup&gt;&lt;/i&gt; mice. (PNAS 2025)

- DOI: 10.1073/pnas.2410095122 | PMCID: PMC11929395 | PMID: 40067893
- Evidence: Sequencing data were first analyzed using Uniform Mani-fold Approximation and Projection (UMAP) for dimension reduction to generate functionally enriched clusters in each sample.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Variable DPP4 expression in multiciliated cells of the human nasal epithelium as a determinant for MERS-CoV tropism. (PNAS 2025)

- DOI: 10.1073/pnas.2410630122 | PMCID: PMC11929475 | PMID: 40048293
- Evidence: ( B ) UMAP plot showing unsupervised clustering of MERS-CoV-infected SAECs.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Hypercholesterolemia-induced LXR signaling in smooth muscle cells contributes to vascular lesion remodeling and visceral function. (PNAS 2025)

- DOI: 10.1073/pnas.2417512122 | PMCID: PMC11912459 | PMID: 40035761
- Evidence: For visualization, we applied dimensionality reduction utilizing Uniform Manifold Approximation and Projection (UMAP) to obtain a 2-dimensional latent space ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [Monocle]

### The synergistic effect of c-Myb hyperactivation and Pu.1 deficiency induces Pelger-Huët anomaly and promotes sAML. (PNAS 2025)

- DOI: 10.1073/pnas.2416121122 | PMCID: PMC11892618 | PMID: 40020188
- Evidence: After PCA, cell clustering, and UMAP visualization, singleR was used for cell annotation.
- Full pipeline: quality control [Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ImageJ]

### Cryo-EM heterogeneity analysis using regularized covariance estimation and kernel regression. (PNAS 2025)

- DOI: 10.1073/pnas.2419140122 | PMCID: PMC11892586 | PMID: 40009640
- Evidence: Despite the particle stack being obtained by heterogeneous refinement, we observe a lot of residual compositional heterogeneity, clearly observable from the clusters in the Uniform Manifold Approximation and Projection (UMAP) visualization of the 20-dimensional embedding.
- Full pipeline: dimensionality reduction/clustering [UMAP, cryoDRGN] -> structure determination [ChimeraX, UMAP, cryoDRGN] -> visualisation [UMAP] -> stage not stated [RELION]

### Multiomics analysis unveils the cellular ecosystem with clinical relevance in aldosterone-producing adenomas with &lt;i&gt;KCNJ5&lt;/i&gt; mutations. (PNAS 2025)

- DOI: 10.1073/pnas.2421489122 | PMCID: PMC11892633 | PMID: 40009643
- Evidence: ( A ) UMAP plot of 53,007 cells from eight APA with KCNJ5 mutations categorized into nine main cell types in the scRNA-seq data.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat v2.1.1, SCENIC]

### Radiation-induced cellular plasticity primes glioblastoma for forskolin-mediated differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2415557122 | PMCID: PMC11892679 | PMID: 40009641
- Evidence: UMAP plots ( A ) of 24 identified clusters that could be attributed to the different treatments.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo]

### RORγt-expressing dendritic cells are functionally versatile and evolutionarily conserved antigen-presenting cells. (PNAS 2025)

- DOI: 10.1073/pnas.2417308122 | PMCID: PMC11892598 | PMID: 39993193
- Evidence: ( A ) RNA-based and ATAC-based UMAP of 11,980 nuclei annotated by cell type (see also SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [SCENIC, Seurat, UMAP]

### The RNA-binding protein RBPMS inhibits smooth muscle cell-driven vascular remodeling in atherosclerosis and vascular injury. (PNAS 2025)

- DOI: 10.1073/pnas.2415933122 | PMCID: PMC11892686 | PMID: 39999164
- Evidence: ( A and B ) Uniform Manifold Approximation and Projection (UMAP) plots illustrating ( A ) all major cell types (cell clusters) within murine aortic roots at baseline and ( B ) the VSMC/fibroblast clusters at baseline, after 8 wk, and after 16 wk of HFD.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Bioconductor]

### pTDP-43 levels correlate with cell type-specific molecular alterations in the prefrontal cortex of &lt;i&gt;C9orf72&lt;/i&gt; ALS/FTD patients. (PNAS 2025)

- DOI: 10.1073/pnas.2419818122 | PMCID: PMC11892677 | PMID: 39999167
- Evidence: Uniform manifold approximation and projection (UMAP) and unsupervised clustering ( 12 ) of the combined snATAC-seq and snRNA-seq datasets identified 31 cell clusters for Emory samples and 20 for Mayo samples, excluding unassigned clusters ( SI Appendix , Figs.
- Full pipeline: quality control [ArchR, Seurat, SoupX] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [WGCNA]

### Agouti and BMP signaling drive a naturally occurring fate conversion of melanophores to leucophores in zebrafish. (PNAS 2025)

- DOI: 10.1073/pnas.2424180122 | PMCID: PMC11874323 | PMID: 40305763
- Evidence: ( I ) Single-cell transcriptomes in UMAP space with cell states ( Left ) and transcript abundances for melanogenesis gene oca2 and purine salvage gene pnp4a ( Right ).
- Full pipeline: alignment/mapping [Monocle] -> quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GEMMA]

### ATP-sensitive potassium channels alter glycolytic flux to modulate cortical activity and sleep. (PNAS 2025)

- DOI: 10.1073/pnas.2416578122 | PMCID: PMC11874466 | PMID: 39964713
- Evidence: ( B ) UMAP plot of cell type designations, Kcnj11 expression, and Abcc8 expression (portal.brain-map.org/atlases-and-data/bkp/abc-atlas).
- Full pipeline: normalisation [AnnData] -> dimensionality reduction/clustering [UMAP] -> visualisation [Matplotlib] -> stage not stated [R]

### Spatial profiling of the interplay between cell type- and vision-dependent transcriptomic programs in the visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421022122 | PMCID: PMC11848306 | PMID: 39946537
- Evidence: ( H ) Subclasses of V1 glutamatergic neurons are represented in UMAP embeddings obtained from integrating snRNA-seq ( Left ; ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [Enrichr, NumPy, SciPy, scikit-learn, seaborn]

### Osteocyte connexin hemichannels and prostaglandin E&lt;sub&gt;2&lt;/sub&gt; release dictate bone marrow mesenchymal stromal cell commitment. (PNAS 2025)

- DOI: 10.1073/pnas.2412144122 | PMCID: PMC11848350 | PMID: 39937859
- Evidence: This lineage mapping was visualized using a UMAP plot, as illustrated in Fig.
- Full pipeline: alignment/mapping [UMAP] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [Monocle, UMAP] -> stage not stated [GSEA]

### Engineered immunological niche directs therapeutic development in models of progressive multiple sclerosis. (PNAS 2025)

- DOI: 10.1073/pnas.2409852122 | PMCID: PMC11848328 | PMID: 39937858
- Evidence: The FindNeighbors and FindClusters functions were used to enable graph-based clustering of the data, with dimensional reduction via UMAP.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [CellChat] -> stage not stated [R, Seurat]

### Dynamic changes in histone lysine lactylation during meiosis prophase I in mouse spermatogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2418693122 | PMCID: PMC11848400 | PMID: 39928879
- Evidence: ( C ) Violin and UMAP plots of expression level and distribution of meiotic genes induced by lactate in scRNAseq cluster.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, HOMER]

### Astrocytic EphA4 signaling is important for the elimination of excitatory synapses in Alzheimer's disease. (PNAS 2025)

- DOI: 10.1073/pnas.2420324122 | PMCID: PMC11848297 | PMID: 39928878
- Evidence: Uniform manifold approximation and projection (UMAP) plot showing 11 cell types identified in a total of 91,845 nuclei from all samples.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat]

### Identification of FSH-regulated and estrous stage-specific transcriptional networks in mouse ovaries. (PNAS 2025)

- DOI: 10.1073/pnas.2411977122 | PMCID: PMC11848299 | PMID: 39928863
- Evidence: ( C ) UMAP projection depicting cell-specific expression for Esr2, Gata6, and Myc .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA]

### Comparative transcriptomics reveals a mixed basal, club, and hillock epithelial cell identity in castration-resistant prostate cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2415308122 | PMCID: PMC11831193 | PMID: 39913208
- Evidence: Visualization of BPECT scores in UMAP plots showed an expected pattern of cells from biopsies with an adenocarcinoma histology having the highest luminal scores, and cells from biopsies with an NEPC histology having the highest NE scores ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Uncovering the hidden RNA virus diversity in Lake Nam Co: Evolutionary insights from an extreme high-altitude environment. (PNAS 2025)

- DOI: 10.1073/pnas.2420162122 | PMCID: PMC11831205 | PMID: 39903107
- Evidence: ( B ) UMAP visualization of tetranucleotide usage frequency (TUF) of RNA viruses and microbes in Lake Nam Co at the superkingdom level.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [BLAST, HMMER] -> visualisation [UMAP]

### Human MAIT cell response profiles biased toward IL-17 or IL-10 are distinct effector states directed by the cytokine milieu. (PNAS 2025)

- DOI: 10.1073/pnas.2414230122 | PMCID: PMC11831165 | PMID: 39903121
- Version used: **3.1**
- Evidence: UMAP (v3.1) was performed using the plug-in of FlowJo after DownSample (v3) to 4296 events and concatenation of 6 samples using the concatenation tool.
- Full pipeline: dimensionality reduction/clustering [UMAP v3.1] -> stage not stated [SCENIC]

### Uterine organoids reveal insights into epithelial specification and plasticity in development and disease. (PNAS 2025)

- DOI: 10.1073/pnas.2422694122 | PMCID: PMC11804710 | PMID: 39883834
- Evidence: ( B ) Uniform Manifold Approximation and Projection (UMAP) of cells colored by cell type ( Left ) or PND ( Right ); circled clusters represent basal and ciliated epithelium present only in the PND3 samples.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [CellChat, GSEA]

### AMH protects the ovary from doxorubicin by regulating cell fate and the response to DNA damage. (PNAS 2025)

- DOI: 10.1073/pnas.2414734122 | PMCID: PMC11804487 | PMID: 39874288
- Evidence: ( C ) UMAP plot featuring five major cell types in the ovary.
- Full pipeline: alignment/mapping [R v4.2.0, Seurat v4.1.0] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [clusterProfiler] -> stage not stated [CellChat, GSEA, scVelo, velocyto]

### Retinoic acid antagonizes estrogen signaling to maintain adult uterine cell fate. (PNAS 2025)

- DOI: 10.1073/pnas.2416089122 | PMCID: PMC11804538 | PMID: 39874292
- Evidence: ( D ) UMAP of epithelial clusters and that of individual samples.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle]

### Lateral olivocochlear neurons modulate cochlear responses to noise exposure. (PNAS 2025)

- DOI: 10.1073/pnas.2404558122 | PMCID: PMC11789013 | PMID: 39854232
- Evidence: ( B ) UMAP representation of clustered single-nucleus sequencing dataset of 99,519 cholinergic brainstem neurons.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ]

### Diffusive topology preserving manifold distances for single-cell data analysis. (PNAS 2025)

- DOI: 10.1073/pnas.2404860121 | PMCID: PMC11789025 | PMID: 39854240
- Evidence: Traditional dimensionality reduction techniques, such as UMAP ( 7 ) and tSNE ( 8 ), play a crucial role in visualizing and interpreting single-cell data.
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> visualisation [UMAP] -> stage not stated [Monocle, Scanpy, scVelo]

### Stimulating the regenerative capacity of the human retina with proneural transcription factors in 3D cultures. (PNAS 2025)

- DOI: 10.1073/pnas.2417228122 | PMCID: PMC11759899 | PMID: 39823300
- Evidence: Top Left UMAP plot from snRNA-seq data organized by cell type [orange; retinal progenitors and dark red: Muller glia (MG)].
- Full pipeline: dimensionality reduction/clustering [UMAP]

### The chromatin remodeler ADNP regulates neurodevelopmental disorder risk genes and neocortical neurogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2405981122 | PMCID: PMC11760920 | PMID: 39808658
- Evidence: ( A ) UMAP embedding of 28,898 neocortical cells derived from the indicated genotypes and timepoints.
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [MACS2]

### ADARp110 promotes hepatocellular carcinoma progression via stabilization of CD24 mRNA. (PNAS 2025)

- DOI: 10.1073/pnas.2409724122 | PMCID: PMC11761664 | PMID: 39808660
- Evidence: ( B ) Left panel: UMAP plot depicting distinct cell populations identified in scRNA-seq data from HCC patients.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Characterizing progenitor cells in developing and injured spinal cord: Insights from single-nucleus transcriptomics and lineage tracing. (PNAS 2025)

- DOI: 10.1073/pnas.2413140122 | PMCID: PMC11745359 | PMID: 39761400
- Evidence: After conducting a quality control procedure, each independent dataset underwent unsupervised clustering to identify cell lineages, which were then projected into two dimensions via UMAP ( Fig.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle]

### Dissecting the cellular architecture and genetic circuitry of the soybean seed. (PNAS 2025)

- DOI: 10.1073/pnas.2416987121 | PMCID: PMC11725896 | PMID: 39793081
- Evidence: ( B ) Uniform Manifold Approximation and Projection (UMAP) dimensional reduction of cotyledon seed cells profiled and separated into 23 clusters.
- Full pipeline: quality control [SoupX v1.6.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat v4.1.1, WGCNA]

### Integrin-activating &lt;i&gt;Yersinia&lt;/i&gt; protein Invasin sustains long-term expansion of primary epithelial cells as 2D organoid sheets. (PNAS 2025)

- DOI: 10.1073/pnas.2420595121 | PMCID: PMC11725944 | PMID: 39793062
- Evidence: ( C ) UMAP of scRNA sequence analysis of reporter ileum cells, differentiated after 12 passages on BME, early (P0) and late passage (P12) on Inv497.
- Full pipeline: quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ]

### Oncogenic IDH1<sup>mut</sup> drives robust loss of histone acetylation and increases chromatin heterogeneity. (PNAS 2025)

- DOI: 10.1073/pnas.2403862122 | PMCID: PMC11725805 | PMID: 39793065
- Evidence: Dimensionality reduction using uniform manifold approximation and projection (UMAP) analysis of IHA cells expressing IDH1-R132H revealed consistent alterations in various epigenetic marks.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Gonadal sex and temperature independently influence germ cell differentiation and meiotic progression in &lt;i&gt;Trachemys scripta&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2413191121 | PMCID: PMC11725912 | PMID: 39793067
- Evidence: Both the UMAP dimensionality reduction and the clusters were calculated from SCVI latent variables using scanpy ( https://github.com/scverse/scanpy ).
- Full pipeline: dimensionality reduction/clustering [Scanpy, UMAP, clusterProfiler]

### Collagen-producing eye cell atlas reveals distinct fibroblast fates in early injury vs. fibrotic subretinal disease. (PNAS 2026)

- DOI: 10.1073/pnas.2519056123 | PMCID: PMC13320955 | PMID: 42361041
- Evidence: ( B – D ) Uniform manifold approximation and projection (UMAP) plot of all cells categorized by ( B ) YFP status, ( C ) cell type, and ( D ) disease state (uninjured, early injury, fibrosis).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, Scanpy v1.9.6]

### Fasting primes small intestinal regeneration after damage via a microbiome-metabolite-chromatin axis. (PNAS 2026)

- DOI: 10.1073/pnas.2529215123 | PMCID: PMC13320697 | PMID: 42335240
- Evidence: Dimensionality reduction was performed via iterative latent semantic indexing (varFeatures = 25,000, dimsToUse = 30, sampleCells = 5,000), followed by Louvain clustering (resolution = 0.2) and UMAP embedding with default parameter.
- Full pipeline: dimensionality reduction/clustering [MACS2 v2.2.9.1, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ArchR v1.0.2, GSEA, HOMER, R v1.0.2]

### Endothelial KLF4 depletion drives age-related neurovascular dysfunction and neuropsychiatric impairment. (PNAS 2026)

- DOI: 10.1073/pnas.2426990123 | PMCID: PMC13291589 | PMID: 42313933
- Evidence: ( A ) Uniform manifold approximation and projection for dimension reduction (UMAP) and unsupervised clustering analysis using Seurat pipeline identified seven distinct cell populations (endothelial cells, microglia, mural cells, pericytes, neutrophils, oligodendrocytes, astrocytes) from the total of 7398 cells (young WT Cre = 1,285 cells, young EC-K4KO = 1,358 cells, old WT Cre = 2,506 cells, old ...
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2]

### Linear-time prediction of proteome-scale microbial protein interactions. (PNAS 2026)

- DOI: 10.1073/pnas.2610619123 | PMCID: PMC13291599 | PMID: 42308045
- Evidence: ( B ) UMAP visualization of the E. coli proteome embedding space.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [PyTorch] -> visualisation [UMAP] -> stage not stated [AlphaFold, BLAST, STRING db]

### Differential Wnt/β-catenin signaling via TCF7L2/LEF1 binding specificity shapes cellular and tumor phenotypes. (PNAS 2026)

- DOI: 10.1073/pnas.2528450123 | PMCID: PMC13273282 | PMID: 42268900
- Evidence: ( 20 ) Dimensionality reduction used PCA and UMAP (5 dims).
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> visualisation [deepTools] -> stage not stated [Enrichr, HOMER, MACS2, R v4.4, SAMtools, Seurat, Signac]

### APOBEC2 deficiency disrupts hematopoietic lineage commitment, resulting in emergence of dual identity lymphocytes in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2531122123 | PMCID: PMC13250534 | PMID: 42247564
- Evidence: Dimensionality reduction (PCA, UMAP) and Louvain clustering were used to identify cellular populations.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Seurat, scDblFinder]

### Reconstructing EBV reactivation and DNA damage response kinetics in morphologic pseudotime. (PNAS 2026)

- DOI: 10.1073/pnas.2609598123 | PMCID: PMC13250554 | PMID: 42234528
- Evidence: UMAP dimensional reduction and clustering of cells by variable morphology ( Middle ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler, Seurat]

### GPIHBP1 on oligodendrocytes binds lipoprotein lipase within the human brain. (PNAS 2026)

- DOI: 10.1073/pnas.2610646123 | PMCID: PMC13250511 | PMID: 42224591
- Evidence: A shared nearest neighbor (SNN) graph was constructed using the FindNeighbors function, and Uniform Manifold Approximation and Projection (UMAP) was used for visualization and identification of cell populations. qRT-PCR Studies.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R v4.3.0, Seurat v5.0.3]

### mRNA-laden LNP-enabled in situ CAR-macrophage alleviates liver fibrosis via inhibiting activated HSCs and modulating the immune microenvironment. (PNAS 2026)

- DOI: 10.1073/pnas.2534673123 | PMCID: PMC13229182 | PMID: 42213756
- Evidence: ( A ) UMAP illustrated cell clustering in both the fibrosis (CCL4-induced fibrosis mice model) and the LNP (αCD163/LNP-FAPCAR) treatment groups.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Toward systems agroecology: Risk-reward balance, emergent plant communities, and temporal weather map in multiplant farming. (PNAS 2026)

- DOI: 10.1073/pnas.2602255123 | PMCID: PMC13229258 | PMID: 42207913
- Evidence: A two-dimensional projection was obtained using Uniform Manifold Approximation and Projection (UMAP, see ref.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Genome-wide association mapping and targeted loss of function studies identify &lt;i&gt;Shroom3&lt;/i&gt; as a driver of hyperpolyploidy and ventricular dilation. (PNAS 2026)

- DOI: 10.1073/pnas.2522068123 | PMCID: PMC13229193 | PMID: 42189988
- Evidence: ( D ) UMAP of annotated clusters identified from single-nucleus RNA sequencing of ventricular tissue in BN-Lx, F344, and M520 (n = 2 hearts per strain).
- Full pipeline: alignment/mapping [GEMMA] -> normalisation [clusterProfiler] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> stage not stated [ImageJ]

### TGFb signaling instructs a conserved fibrosis-associated cell state marked by LRRC15. (PNAS 2026)

- DOI: 10.1073/pnas.2536550123 | PMCID: PMC13214008 | PMID: 42160341
- Evidence: ( A ) UMAP representation of mesenchymal clusters (color and number) from combined normal and IPF lung tissue scRNA-seq.
- Full pipeline: normalisation [DESeq2 v1.40.2, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma v3.56.1] -> simulation/modelling [Slingshot]

### NAT10/ac&lt;sup&gt;4&lt;/sup&gt;C drives intrahepatic cholangiocarcinoma by suppressing transposable elements via chromatin remodeling. (PNAS 2026)

- DOI: 10.1073/pnas.2532263123 | PMCID: PMC13187814 | PMID: 42133812
- Evidence: ( A ) UMAP visualization of major cell types in 25 ICC tumor specimens.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellChat, GSEA]

### VEGF-D-induced intraosseous lymphangiogenesis drives site-specific heterotopic bone resorption. (PNAS 2026)

- DOI: 10.1073/pnas.2524022123 | PMCID: PMC13167802 | PMID: 42085147
- Evidence: ( A ) UMAP clustering of pooled single-cell RNA-seq data from wild-type (WT) and Vegfd-OE hindlimb tissues identifies 14 distinct cell populations, including mesenchymal progenitor cells (MPCs), keratinocytes, endothelial cells, lymphatic endothelial cells (LECs), immune cell subsets, and osteoclast precursors (OC precursors).
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Purine metabolic adaptation protects the endothelium from disturbed flow-induced DNA damage and atherosclerosis. (PNAS 2026)

- DOI: 10.1073/pnas.2526299123 | PMCID: PMC13142911 | PMID: 42060719
- Evidence: ( D ) scATAC-seq data plotted on a single UMAP representing 2D-R, 2D-L, 2W-R, and 2W-L to identify major EC populations.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [R, Seurat]

### Multimodal analysis reveals cellular diversity and divergent circuits of the zona incerta. (PNAS 2026)

- DOI: 10.1073/pnas.2509781123 | PMCID: PMC13143026 | PMID: 42054363
- Evidence: ( D ) UMAP embedding displaying clustering of ZI cells based on snRNA-seq data, and uniformly high Gad2 expression level among the snRNA-seq clusters in UMAP space.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [SciPy, statsmodels]

### Type I interferons induced upon respiratory viral infection impair lung metastatic initiation. (PNAS 2026)

- DOI: 10.1073/pnas.2412919123 | PMCID: PMC13099621 | PMID: 41996163
- Evidence: ( E ) UMAP plot of scRNAseq data from lungs of PBS and IFN-α exposed PyMT-injected mice.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, GSEA]

### FABP7 controls radial glial scaffold stability during human cortical development. (PNAS 2026)

- DOI: 10.1073/pnas.2523130123 | PMCID: PMC13099611 | PMID: 41984827
- Evidence: Unsupervised clustering identified 28 transcriptionally distinct clusters visualized by Uniform Manifold Approximation and Projection (UMAP) and consolidated into six populations: proliferative radial glia (RG-div), quiescent radial glia (RG), cortical hem (CH), intermediate progenitors (IPC), cortical neurons (CN), and ventral progenitors/interneurons (VP/IN) ( Fig.
- Full pipeline: normalisation [Seurat v4.4.0, edgeR v3.40.2] -> dimensionality reduction/clustering [Seurat v4.4.0, UMAP, edgeR v3.40.2] -> differential/statistical testing [Seurat v4.4.0, edgeR v3.40.2] -> visualisation [UMAP] -> stage not stated [GSEA, WGCNA]

### Amoeboid-mesenchymal transition and the proteolytic control of cancer invasion plasticity. (PNAS 2026)

- DOI: 10.1073/pnas.2520717123 | PMCID: PMC13079982 | PMID: 41961858
- Evidence: UMAP plots demonstrate initial clustering results and expression profiles of a cell migration gene set.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [TrackMate]

### Meiotic prophase I disruption as a strategy for nonhormonal male contraception using small-molecule inhibitor JQ1. (PNAS 2026)

- DOI: 10.1073/pnas.2517498123 | PMCID: PMC13080027 | PMID: 41945432
- Evidence: Pseudotime ordering was performed using Slingshot (v2.4.0) ( 12 ) with UMAP coordinates as the reduced-dimensional input and cluster labels as lineage identifiers.
- Full pipeline: quality control [SoupX v1.4.5, scDblFinder v2.0] -> alignment/mapping [STAR v2.5.3b] -> quantification [R] -> dimensionality reduction/clustering [Slingshot v2.4.0, UMAP] -> stage not stated [DESeq2, ImageJ, Seurat v4.1.1]

### Immune cell profiling reveals expanded stem cell-like memory T cells in anti-GAD65-associated neurological syndromes. (PNAS 2026)

- DOI: 10.1073/pnas.2514753123 | PMCID: PMC13038060 | PMID: 41880578
- Evidence: ( C ) UMAP showing 21 color-coded cell clusters of 1,18,492 single cell transcriptomes integrated from CSF cells and PBMC from anti-GAD65 AINS individuals (n = 8) and IIH individuals (n = 8).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [R, Seurat v5.0.1]

### GFAP&lt;sup&gt;+&lt;/sup&gt; FOXF2&lt;sup&gt;+&lt;/sup&gt; ependymal cells promote blood-brain barrier repair via DLL4-NOTCH signaling after neural injury. (PNAS 2026)

- DOI: 10.1073/pnas.2520352123 | PMCID: PMC13037844 | PMID: 41875155
- Evidence: Subsequent analysis of 60,565 quality-controlled cells in Seurat included projections visualized in Uniform Manifold Approximation and Projection (UMAP) space.
- Full pipeline: dimensionality reduction/clustering [GSEA, Seurat, UMAP] -> visualisation [Seurat, UMAP]

### Quantifying the fidelity of in vitro human cell culture systems using a biomedical foundation model. (PNAS 2026)

- DOI: 10.1073/pnas.2520482123 | PMCID: PMC13012098 | PMID: 41860964
- Evidence: S2 and S3 ), uniform manifold approximation and projection (UMAP) analysis revealed the presence of similar clusters in cultures established from three independent donors ( SI Appendix, Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R v4.3.0, Seurat v5.0.0]

### A transcription regulator atlas identifies TOX3 as an Atoh1 coactivator in cerebellar development and tumorigenesis. (PNAS 2026)

- DOI: 10.1073/pnas.2527163123 | PMCID: PMC13012119 | PMID: 41849381
- Evidence: ( C ) UMAP plots showing single-nucleus transcriptomes from control and mutant cerebella.
- Full pipeline: dimensionality reduction/clustering [Monocle, UMAP] -> simulation/modelling [Monocle]

### Mutually exclusive alternative pre-mRNA splicing promotes adaptive metabolic stress signaling by JNK. (PNAS 2026)

- DOI: 10.1073/pnas.2527162123 | PMCID: PMC13012108 | PMID: 41843681
- Evidence: ( E ) Single-cell RNA-seq analysis of hepatic leukocytes from HFD-fed (16 wk) L J1LF , L J17a , L J17b , L J2LF , L J27a , and L J27b mice are presented as a co-clustered UMAP plot [GEO accession number GSE303383 ; ( 32 )].
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Single-cell analyses identify independent aging processes that compete to determine cellular fate in budding yeast. (PNAS 2026)

- DOI: 10.1073/pnas.2534452123 | PMCID: PMC12993945 | PMID: 41811451
- Evidence: Cells of the “young cell” sample, which is an exponentially growing cell culture, displayed a Uniform Manifold Approximation and Projection (UMAP) structure largely driven by the cell cycle ( SI Appendix, Fig.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, kallisto] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Scanpy v1.11.0, statsmodels]

### Bacterial reporter-paired scRNA sequencing reveals cross talk between zinc starvation and zinc toxicity in macrophage antibacterial defense. (PNAS 2026)

- DOI: 10.1073/pnas.2530503123 | PMCID: PMC12993976 | PMID: 41802048
- Evidence: Dimension reduction was performed by principal component analysis and the top 30 principal components were selected for clustering and UMAP two-dimensional projections via DimPlot function in Seurat.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, scVelo v0.2.4, velocyto v0.17] -> differential/statistical testing [R v4.0] -> stage not stated [Seurat v4.0.4, scDblFinder v1.4.0]

### Psoriasis-like disease prevents squamous skin tumor development by neutrophil-driven inflammation. (PNAS 2026)

- DOI: 10.1073/pnas.2536378123 | PMCID: PMC12994166 | PMID: 41802042
- Evidence: ( B ) Two dimensional UMAP projection of 14,746 cells clustered after quality control and annotated according to canonical cell markers ( SI Appendix , Fig.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [CellChat, UMAP]

### The membrane-associated ubiquitin ligase MARCHF8 degrades MHC-I in HPV-positive head and neck cancer for immune evasion. (PNAS 2026)

- DOI: 10.1073/pnas.2525730123 | PMCID: PMC12994185 | PMID: 41802050
- Evidence: The UMAP plots of integrated samples ( A ) and the distribution of each immune cell cluster in Marchf8 knockout (sgR-Marchf8-2 and sgR-Marchf-3) and sgR-scr are shown in the bar graph ( B ).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Seurat]

### Med14 phosphorylation shapes genomic response to GLP-1 agonists. (PNAS 2026)

- DOI: 10.1073/pnas.2536772123 | PMCID: PMC12974444 | PMID: 41779793
- Evidence: Uniform manifold approximation and projection (UMAP) representation of WT and Med14 S983A mutant pancreatic islets untreated ( Top ) or treated for 16 h with 10 nM Ex-4 ( Bottom ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, Trim Galore] -> quantification [HOMER] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Evidence: UMAP embeddings were then computed using the first 30 PCA dimensions as input.
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

### Mfsd2a is important for maintaining epidermal homeostasis. (PNAS 2026)

- DOI: 10.1073/pnas.2531159123 | PMCID: PMC12933103 | PMID: 41712644
- Evidence: ( B ) UMAP visualization of human skin scRNA-seq data from Reynolds et al.
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.4] -> visualisation [UMAP]

### Neuropixels reveal laminar microcircuit organization in monkey V1 in vivo. (PNAS 2026)

- DOI: 10.1073/pnas.2521556123 | PMCID: PMC12933057 | PMID: 41706902
- Evidence: WaveMAP uses uniform manifold approximation and projection (UMAP) on normalized waveforms to first create a high-dimensional graph, followed by Louvain clustering to delineate putative cell types.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP]

### Pichia-CLM: A language model-based codon optimization pipeline for &lt;i&gt;Komagataella phaffii&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2522052123 | PMCID: PMC12933070 | PMID: 41701818
- Evidence: ( A ) Comparison of the predictive accuracy of two alternative architectures using a test set (20% reserved data) ( B ) Scatter plot of the specific productivities of six different recombinant proteins optimized by these models ( C ) UMAP projections of the amino acid and codon embedding learned by the model corresponding to Arch1.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Synaptogyrin-3 plays a critical role in addiction-related dopamine dysfunction and behavioral maladaptations. (PNAS 2026)

- DOI: 10.1073/pnas.2518590123 | PMCID: PMC12912984 | PMID: 41678303
- Evidence: ( D ) Uniform Manifold Approximation and Projection (UMAP) plot of transcriptionally defined clusters of VTA neurons from male and female rat samples, with nonneuronal cell populations in gray.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Lipid nanoparticle GM-CSF replacement for autoimmune pulmonary alveolar proteinosis. (PNAS 2026)

- DOI: 10.1073/pnas.2511483123 | PMCID: PMC12913010 | PMID: 41671176
- Evidence: This was followed by PCA dimensional reduction and uniform manifold approximation and projection (UMAP)/t-SNE clustering.
- Full pipeline: normalisation [Seurat v4.0.4] -> dimensionality reduction/clustering [UMAP] -> stage not stated [QuPath, scDblFinder]

### A systems approach identifies MERTK as a therapeutic vulnerability in ZFTA-RELA-driven ependymomas. (PNAS 2026)

- DOI: 10.1073/pnas.2514518123 | PMCID: PMC12912970 | PMID: 41665993
- Evidence: Left : UMAP plot identifying major cell populations.
- Full pipeline: alignment/mapping [SAMtools v1.19.2, STAR, featureCounts] -> quantification [HTSeq, SAMtools v1.19.2, featureCounts] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [Bioconductor] -> visualisation [ggplot2] -> stage not stated [GSEA, QuPath, Seurat, pheatmap]

### Bridging unpaired single-cell multimodal data for integrative analyses with SuperMap. (PNAS 2026)

- DOI: 10.1073/pnas.2505182123 | PMCID: PMC12890892 | PMID: 41650244
- Evidence: ( A ) UMAP visualization of benchmark datasets (10X Multiome PBMC, 10X Multiome BMMC, SHARE-seq mouse skin and ASAP-seq PBMC), colored by cell types.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [ArchR, Signac]

### Functionally heterogeneous intratumoral CD4&lt;sup&gt;+&lt;/sup&gt;CD8&lt;sup&gt;+&lt;/sup&gt; double-positive T cells can give rise to single-positive T cells. (PNAS 2026)

- DOI: 10.1073/pnas.2506168123 | PMCID: PMC12849695 | PMID: 41557789
- Evidence: Data were scaled to unit variance and zero mean, followed by PCA, Leiden clustering, and UMAP embedding.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler, Monocle, Scanpy]

### Differential &lt;i&gt;Hes1&lt;/i&gt; activation defines neural stem cell lineage commitment and niche maintenance in embryonic and adult mouse cortex. (PNAS 2026)

- DOI: 10.1073/pnas.2511800123 | PMCID: PMC12849698 | PMID: 41557790
- Evidence: ( G ) UMAP of scRNA-seq data showing cell clusters of E14 cortex.
- Full pipeline: dimensionality reduction/clustering [Seurat v5.3, UMAP]

### Piezo1 dictates K&lt;sup&gt;+&lt;/sup&gt; homeostasis through coordinated regulation of the ubiquitin ligase Kelch-like 3 in RBCs and the kidney. (PNAS 2026)

- DOI: 10.1073/pnas.2513222123 | PMCID: PMC12818455 | PMID: 41533447
- Evidence: ( A ) UMAP showing 13 kidney cell clusters from single-cell RNA sequence.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R]

### Combination antiviral and anti-inflammatory therapy mitigates persistent neurological deficits in mice post SARS-CoV-2 infection. (PNAS 2026)

- DOI: 10.1073/pnas.2530209123 | PMCID: PMC12799161 | PMID: 41499397
- Evidence: Principal component analysis (PCA) was performed using the 2,000 most variable genes, and UMAP embedding was generated from the top 40 principal components.
- Full pipeline: quality control [FastQC, Trimmomatic v0.33] -> read trimming [FastQC, Trimmomatic v0.33] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, R v4.5, Seurat v5.3.0, pheatmap]

### Mouse and human share conserved transcriptional programs for interneuron development. (Science 2021)

- DOI: 10.1126/science.abj6641 | PMCID: PMC7618238 | PMID: 34882453
- Evidence: Unsupervised clustering of cellular transcriptional identities by uniform manifold approximation and projection (UMAP) dimensionality reduction revealed the existence of 10 cell clusters ( Fig.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Seurat] -> simulation/modelling [R]

### mRNA vaccines induce durable immune memory to SARS-CoV-2 and variants of concern. (Science 2021)

- DOI: 10.1126/science.abm0829 | PMCID: PMC9284784 | PMID: 34648302
- Evidence: To this end, we applied uniform manifold approximation and projection (UMAP) to visualize the trajectory of vaccine-induced adaptive immunity over time.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> simulation/modelling [UMAP] -> visualisation [UMAP, pheatmap]

### Mapping the developing human immune system across organs. (Science 2022)

- DOI: 10.1126/science.abo0510 | PMCID: PMC7612819 | PMID: 35549310
- Evidence: To generate a joint embedding of query and reference cells, we concatenated the latent dimensions learnt for query cells to the latent dimensions used for the reference embedding and computed the KNN graph and UMAP as described above.
- Full pipeline: alignment/mapping [AnnData] -> quantification [scikit-learn] -> normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [Squidpy v1.1.2, UMAP, scikit-learn] -> machine learning [AnnData] -> visualisation [AnnData] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder v0.2.3]

### Cross-tissue immune cell analysis reveals tissue-specific features in humans. (Science 2022)

- DOI: 10.1126/science.abl5197 | PMCID: PMC7612735 | PMID: 35549406
- Evidence: (A) UMAP visualization of T cells and ILCs across human tissues colored by cell types.
- Full pipeline: normalisation [Scanpy v1.6.0] -> dimensionality reduction/clustering [Scanpy v1.6.0, UMAP] -> visualisation [UMAP] -> stage not stated [PHENIX, scDblFinder]

### KIR<sup>+</sup>CD8<sup>+</sup> T cells suppress pathogenic T cells and are active in autoimmune diseases and COVID-19. (Science 2022)

- DOI: 10.1126/science.abi9591 | PMCID: PMC8995031 | PMID: 35258337
- Evidence: We performed principal components analysis (PCA) dimensionality reduction on the integrated data, then clustered cells with the Louvain algorithm and visualized the data using uniform manifold approximation and projection (UMAP).
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> quantification [HTSeq v0.5.4p, ImageJ] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler, seaborn] -> visualisation [UMAP] -> stage not stated [DESeq2, Python, R, Seurat v3.0]

### Sex-biased gene expression across mammalian organ development and evolution. (Science 2023)

- DOI: 10.1126/science.adf1046 | PMCID: PMC7615307 | PMID: 37917687
- Evidence: (A) UMAP of adult mouse liver snRNA-seq dataset (22512 cells).
- Full pipeline: quality control [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2]

### The &lt;i&gt;-KTS&lt;/i&gt; splice variant of WT1 is essential for ovarian determination in mice. (Science 2023)

- DOI: 10.1126/science.add8831 | PMCID: PMC7615308 | PMID: 37917714
- Evidence: (D) UMAP projection of the 75,360 cells colored by clusters or (E) by associated cell types.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: Dimensionality reduction and marker expression visualization For visualization, the uniform manifold approximation (UMAP) algorithm was run using the sc.tl.umap function in Scanpy.
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### Brassinosteroid gene regulatory networks at cellular resolution in the &lt;i&gt;Arabidopsis&lt;/i&gt; root. (Science 2023)

- DOI: 10.1126/science.adf4721 | PMCID: PMC10119888 | PMID: 36996230
- Evidence: (B) UMAP projection of scRNA-seq from 14,334 wild-type cells, 12,649 bri1-T cells and 7,878 pGL2-BRI1-GFP/bri1-T cells.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat v3.1.5]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Evidence: (C) Uniform manifold approximation and projection (UMAP) of single PBMC transcriptomes.
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### In vivo dendritic cell reprogramming for cancer immunotherapy. (Science 2024)

- DOI: 10.1126/science.adn9083 | PMCID: PMC7616765 | PMID: 39236156
- Evidence: (B) Principal component analysis of CD8 + and CD4 + T cells visualized by Uniform manifold approximation and projection (UMAP) plots from tumors, tdLN and blood (left) across treatment conditions (right).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP]

### Transcripts of repetitive DNA elements signal to block phagocytosis of hematopoietic stem cells. (Science 2024)

- DOI: 10.1126/science.adn1629 | PMCID: PMC12012832 | PMID: 39264994
- Evidence: Y-axis depicts the relative gene expression (E) Uniform manifold and projection (UMAP) of sorted runx1+23-mcherry HSPCs in standard morpholino (gray, Control sdM) and irf8 depleted embryos (yellow, irf8 sdKD) (Original data from ( 6 )).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [CellProfiler, Metascape, R]

### Drugs of abuse hijack a mesolimbic pathway that processes homeostatic need. (Science 2024)

- DOI: 10.1126/science.adk6742 | PMCID: PMC11077477 | PMID: 38669575
- Evidence: The number of PCs used for UMAP calculation was selected with elbow plot ( 91 ).
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> normalisation [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [TensorFlow] -> stage not stated [ImageJ, Python, SciPy, Suite2p]

### The transcription factor ZEB2 drives the formation of age-associated B cells. (Science 2024)

- DOI: 10.1126/science.adf8531 | PMCID: PMC7616037 | PMID: 38271512
- Evidence: Seven distinct clusters were revealed by unsupervised clustering with a two-dimensional uniform manifold approximation and projection (UMAP) ( Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### PIEZO channels link mechanical forces to uterine contractions in parturition. (Science 2025)

- DOI: 10.1126/science.ady3045 | PMCID: PMC12807505 | PMID: 41231991
- Evidence: Uniform manifold approximation and projection (UMAP) was used for visualization after integration.
- Full pipeline: alignment/mapping [Seurat] -> quantification [CellProfiler] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy, edgeR] -> visualisation [UMAP] -> stage not stated [scDblFinder]

### Branched actin networks mediate macrophage-dependent host-microbiota homeostasis. (Science 2025)

- DOI: 10.1126/science.adr9571 | PMCID: PMC7618398 | PMID: 41231985
- Evidence: (D) Uniform manifold approximation and projection (UMAP) of the integrated scRNAseq of 41130 cells from C5 HetVav or C5 ΔVav ileum lamina propria.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat]

### Diverse somatic genomic alterations in single neurons in chronic traumatic encephalopathy. (Science 2025)

- DOI: 10.1126/science.adu1351 | PMCID: PMC12594281 | PMID: 41166474
- Evidence: We then performed dimension reduction (principal component analysis, t-SNE, and UMAP) and cell clustering using Louvain ( 54 ).
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.15, SAMtools, minimap2 v2.12] -> registration [GATK, Picard v2.8.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools, R, lme4 v1.1] -> stage not stated [ANNOVAR, Seurat v4.0.5]

### High-resolution spatial mapping of cell state and lineage dynamics in vivo with PEtracer. (Science 2025)

- DOI: 10.1126/science.adx3800 | PMCID: PMC12766569 | PMID: 40705858
- Evidence: The same principal components were used to generate the UMAP projections with RunUMAP.
- Full pipeline: alignment/mapping [Python, scikit-image v0.24.0] -> normalisation [Scanpy v1.10.0] -> dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> stage not stated [Cellpose v3.1.0, R v4.2.3, Seurat, Squidpy v1.6.2, scDblFinder]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: The top 30 latent semantic indexing (LSI) components, except the first component, were used to perform nonlinear dimension reduction using UMAP and construct a shared nearest neighbor graph before clustering with the SLM algorithm.
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Macrophage-derived oncostatin M repairs the lung epithelial barrier during inflammatory damage. (Science 2025)

- DOI: 10.1126/science.adi8828 | PMCID: PMC12541708 | PMID: 40638741
- Evidence: Uniform manifold approximation and projection (UMAP) clustering and cell cluster annotation of scRNA-seq data from the lungs of mock-infected (0 dpi) and IAV-infected mice at 2 dpi (26,978 total cells) (D).
- Full pipeline: dimensionality reduction/clustering [Enrichr, UMAP]

### Aberrant basal cell clonal dynamics shape early lung carcinogenesis. (Science 2025)

- DOI: 10.1126/science.ads9145 | PMCID: PMC7617789 | PMID: 40310937
- Evidence: Marker gene dotplots and UMAP visualizations were generated to provide robust validation of cell type assignments and distinguish basal cell subtypes.
- Full pipeline: alignment/mapping [SAMtools] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.24.0] -> visualisation [R, UMAP, ggplot2] -> stage not stated [ANNOVAR v1.0.0, Seurat v5.0.1, Slingshot]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: Clusters were obtained with agglomerative clustering using Scanpy ( 97 ): principle components were computed using solver = “arpack”; a neighborhood graph was computed using n_neighbors = 30 and n_pcs = 20; a uniform manifold approximation and projection (UMAP) embedding was computed ( 98 ); and clusters were assigned using leiden clustering on the UMAP embedding ( 99 ).
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

### Deep-tissue transcriptomics and subcellular imaging at high spatial resolution. (Science 2025)

- DOI: 10.1126/science.adq2084 | PMCID: PMC12005972 | PMID: 39977545
- Evidence: The 3D spatial information embedded within our cycleHCR data enables us to dissect these gradients and expression heterogeneity within each UMAP cluster.
- Full pipeline: alignment/mapping [BigStitcher] -> registration [BigStitcher, Nextflow] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cellpose]

### Multiplex generation and single-cell analysis of structural variants in mammalian genomes. (Science 2025)

- DOI: 10.1126/science.ado5978 | PMCID: PMC11931979 | PMID: 39883753
- Evidence: Here, these cells are visualized in UMAP space, colored by clone assignment.
- Full pipeline: read trimming [Cutadapt v2.5] -> alignment/mapping [BEDTools v2.29.2] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Matplotlib v3.8.1, Python, R, SciPy, Seurat v4.3.1, scDblFinder v0.2.3, seaborn v0.13.0]

### Distinct myeloid-derived suppressor cell populations in human glioblastoma. (Science 2025)

- DOI: 10.1126/science.abm5214 | PMCID: PMC12836367 | PMID: 39818911
- Evidence: The 60 principal components were used for dimensional reduction by UMAP as well as generation of a shared nearest neighbor network followed by Louvain clustering.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, R, SCENIC, velocyto]

### RNA polymerase II at histone genes predicts outcome in human cancer. (Science 2025)

- DOI: 10.1126/science.ads2169 | PMCID: PMC12184985 | PMID: 39946483
- Evidence: RNAPII over histone genes predicts aggressiveness in meningiomas and breast tumors To evaluate how effectively FFPE-CUTAC can resolve differences between the seven tumor samples, we constructed a cCRE-based UMAP including 114 individual human datasets.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Affinity maturation of antibody responses is mediated by differential plasma cell proliferation. (Science 2025)

- DOI: 10.1126/science.adr6896 | PMCID: PMC11938350 | PMID: 39700316
- Evidence: Uniform manifold approximation and projection (UMAP) integrating CITEseq data revealed distinct clusters of GC B and PCs characterized by Fas/CD86 and CD138 surface protein expression respectively ( fig.
- Full pipeline: dimensionality reduction/clustering [UMAP]

### Microglia Rank signaling regulates GnRH neuronal function and the hypothalamic-pituitary-gonadal axis. (Science 2026)

- DOI: 10.1126/science.aeb6999 | PMCID: PMC7619046 | PMID: 41818388
- Evidence: Clustering analysis using Uniform Manifold Approximation and Projection (UMAP) and known hypothalamic cell types markers ( 20 , 25 – 27 ) revealed twelve hypothalamic clusters including microglia, astrocytes, oligodendrocytes, among others ( Fig.
- Full pipeline: quality control [FastQC, STAR v2.7.1] -> alignment/mapping [FastQC, GATK, STAR v2.7.1] -> normalisation [FastQC, STAR v2.7.1] -> dimensionality reduction/clustering [FastQC, ImageJ, STAR v2.7.1, UMAP] -> stage not stated [GSEA, Seurat]

### Rewiring STAT signaling from the cell surface with Trikine immunotherapeutics. (Science 2026)

- DOI: 10.1126/science.adx9954 | PMCID: PMC12963926 | PMID: 41712697
- Evidence: To minimize batch effects across mice, we used Harmony (v1.2.1) for integration, and generated Uniform Manifold Approximation and Projection (UMAP) embeddings from the top 50 Harmony dimensions.
- Full pipeline: quality control [FastQC] -> alignment/mapping [AlphaFold, ChimeraX, featureCounts] -> quantification [ComplexHeatmap, Seurat v5.1.0, featureCounts] -> normalisation [ComplexHeatmap, UMAP] -> dimensionality reduction/clustering [Monocle v1.3.7, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, MACS2, fgsea]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: A two-dimensional UMAP (uniform manifold approximation and projection) embedding was then computed using cosine distance with 30 neighbors and a minimum distance of 0.5.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Overcoming T cell tolerance to tumor self-antigens through catch-bond engineering. (Science 2026)

- DOI: 10.1126/science.adx3162 | PMCID: PMC13004167 | PMID: 41855322
- Evidence: ( B ) Uniform Manifold Approximation and Projection (UMAP) representation of TILs from all groups combined.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA]

### Lifelong behavioral screen reveals an architecture of vertebrate aging. (Science 2026)

- DOI: 10.1126/science.aea9795 | PMCID: PMC13165398 | PMID: 41818367
- Evidence: UMAP embeddings to visualize pose features UMAP embeddings of the top 15 PCs describing killifish pose features were used for visualization.
- Full pipeline: quality control [Cutadapt v3.1, FastQC] -> read trimming [Cutadapt v3.1, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [STAR v2.7.1a] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, statsmodels] -> simulation/modelling [clusterProfiler] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [BLAST, Bioconductor, NumPy, SciPy]

### Single intramuscular injection of self-amplifying RNA of &lt;i&gt;Nppa&lt;/i&gt; to treat myocardial infarction. (Science 2026)

- DOI: 10.1126/science.adu9394 | PMCID: PMC13124201 | PMID: 41785353
- Evidence: In total, 21,331 high-quality nuclei were captured and subjected to unsupervised clustering with dimensionality reduction by t-distributed stochastic neighbor embedding (t-SNE) and uniform manifold approximation and projection (UMAP).
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellChat, R, Seurat v5.3.0, Slingshot v2.14.0]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: We applied UMAP to normalized transcriptomic profiles with parameters n_neighbors =2, min_dist=0 and random_state=42 to generate two- dimensional (2D) embeddings for each perturbed gene in either Perturb- seq experiments.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Evidence: These embeddings were used for constructing a neighbor graph (20 NNs), Louvain clustering at a high resolution (3.0) and UMAP projection (metric = “cosine”, min.dist = 0.1, n.neighbors = 20) as implemented in Seurat (v4.0).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

### Ontogeny of the spinal cord dorsal horn. (Science 2026)

- DOI: 10.1126/science.adx5781 | PMCID: PMC12879194 | PMID: 41505538
- Evidence: Subsequently, coordinates were assigned bounding each section, clusters and gene markers were displayed on a UMAP reduction, and non-neuronal and sensory neuron clusters were excluded from further processing (see code Xenium_2024_2_DefineROI_ExtractNeurons on Github).
- Full pipeline: quality control [R v4.4.1, Seurat] -> dimensionality reduction/clustering [AnnData, R v4.4.1, Seurat, UMAP] -> simulation/modelling [SciPy] -> visualisation [ggplot2] -> stage not stated [ImageJ]

### Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation. (Science 2026)

- DOI: 10.1126/science.adx4174 | PMCID: PMC12850507 | PMID: 41477881
- Evidence: Uniform Manifold Approximation and Projection (UMAP) was conducted to reduce dimensions to embed the cells into two-dimensional space.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [BCFtools, GSEA, SAMtools v1.20, minimap2 v2.26] -> variant calling [GATK] -> quantification [DESeq2 v1.34.0, GSEA] -> normalisation [GSEA, Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2 v1.34.0, PLINK v1.9] -> stage not stated [R, fgsea]

