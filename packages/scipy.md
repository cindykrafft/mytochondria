# SciPy

- **Category:** general
- **Papers in survey:** 472
- **Journals:** Nature (210), PNAS (207), Cell (36), Science (18), Lancet (1)
- **Years:** 2021 (40), 2022 (68), 2023 (75), 2024 (111), 2025 (121), 2026 (57)
- **Versions named:** 1.10.1 (14), 1.4.1 (7), 1.11.4 (6), 1.6.3 (5), 1.9.3 (5), 1.6.2 (5), 1.5.2 (4), 1.7.1 (4), 1.11.2 (3), 1.8.0 (3)
- **Pipeline stages it appears in:** differential/statistical testing (89), dimensionality reduction/clustering (40), visualisation (24), simulation/modelling (20), normalisation (10), quantification (9), alignment/mapping (7), machine learning (4), structure determination (1)

## Papers

### SARS-CoV-2 infection triggers profibrotic macrophage responses and lung fibrosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.033 | PMCID: PMC8626230 | PMID: 34914922
- Version used: **1.5.2**
- Evidence: ...rsion 0.6.7 Gayoso et al., 2021 https://scvi-tools.org/ Python package seaborn version 0.10.1 Waskom, 2021 https://seaborn.pydata.org/ Python package scipy version 1.5.2 Virtanen et al., 2020 https://scipy.org/ Python package numpy version 1.20.3 Harris et al., 2020 https://numpy.org/ Python package matplotlib version 3.3.3 Hunter, 2007 https://matplotlib.org/ Other QExactive HF-x Orbitrap MS Ther...
- Full pipeline: dimensionality reduction/clustering [AnnData v0.7.4, CellChat v0.5.5, UMAP, clusterProfiler v3.14.3, ggpubr v0.4.0, igraph, tidyverse v1.0.2] -> machine learning [AnnData v0.7.4] -> visualisation [UMAP] -> stage not stated [CellProfiler v3.1.8, GSEA v2.0, Matplotlib v3.3.3, NumPy v1.20.3, Python v3.7.8, QuPath, R v3.6, Scanpy, SciPy v1.5.2, Seurat v3.2.2, data.table, ggplot2 v3.3.2, ilastik v1.3.2, pheatmap v1.0.12, seaborn v0.10.1]

### Identification of a therapeutic interfering particle-A single-dose SARS-CoV-2 antiviral intervention with a high barrier to resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.004 | PMCID: PMC8577993 | PMID: 34838159
- Version used: **1.5.4**
- Evidence: NumPy (v1.19.4) and SciPy (v1.5.4) were used with additional optimization for solving ODEs using Numba (v0.51.2).
- Full pipeline: quantification [DESeq2, featureCounts] -> simulation/modelling [Python] -> visualisation [Matplotlib v3.3.3, seaborn v0.11.0] -> stage not stated [ImageJ, NumPy v1.19.4, SciPy v1.5.4]

### Whole-body integration of gene expression and single-cell morphology. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.017 | PMCID: PMC8445025 | PMID: 34380046
- Evidence: ..., 2012 https://mahotas.readthedocs.io/en/latest/ networkx Hagberg et al., 2008 https://networkx.org/ pandas McKinney, 2010 https://pandas.pydata.org/ scipy Virtanen et al., 2020 https://www.scipy.org/ numpy van der Walt et al., 2011 https://numpy.org/ snakemake Köster and Rahmann, 2012 https://snakemake.readthedocs.io/en/stable/ tidyverse Wickham et al., 2017 https://www.tidyverse.org/ rgl CRAN ht...
- Full pipeline: dimensionality reduction/clustering [ImageJ, Python, Snakemake, UMAP, ilastik, scikit-image, scikit-learn] -> visualisation [BigStitcher] -> stage not stated [Bioconductor, NetworkX, NumPy, SciPy, tidyverse]

### Functional diversity for body actions in the mesencephalic locomotor region. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.002 | PMCID: PMC8382160 | PMID: 34302739
- Evidence: To identify peaks in neuronal calcium activity we used SciPy, a Python library for scientific computing.
- Full pipeline: differential/statistical testing [R, scikit-learn] -> visualisation [seaborn] -> stage not stated [DeepLabCut, Python v3.7, SciPy, ilastik v1.1.5]

### Genome-wide gene expression tuning reveals diverse vulnerabilities of M. tuberculosis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.033 | PMCID: PMC8382161 | PMID: 34297925
- Version used: **1.2.2**
- Evidence: ...1/ Subread aligner (version 1.6.0) Liao et al., 2013 http://subread.sourceforge.net/ Python (version 2.7.18) van Rossum, 1995 https://www.python.org/ SciPy (version 1.2.2) Virtanen et al., 2020 https://www.scipy.org/ statsmodels (version 0.10.1) Seabold and Perktold, 2010 https://www.statsmodels.org/stable/index.html Rstan (version 2.19.3) Stan Development Team, 2020 https://mc-stan.org/ Stan (ver...
- Full pipeline: alignment/mapping [Python v2.7.18, SciPy v1.2.2] -> stage not stated [BLAST, Stan v2.19.3, statsmodels v0.10.1]

### A global metagenomic map of urban microbiomes and antimicrobial resistance. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.002 | PMCID: PMC8238498 | PMID: 34043940
- Evidence: ...ioconda/fasttree iTOL v5.5 Letunic and Bork 2019 https://itol.embl.de/ CRISPRCasFinder Couvin et al., 2018 https://github.com/dcouvin/CRISPRCasFinder SciPy Virtanen et al., 2020 https://www.scipy.org/ dendextend v1.12.0 Galili 2015 https://github.com/cran/dendextend MUMmer v3.23 Kurtz et al., 2004 https://github.com/mummer4/mummer ResistomeAnalyzer (commit 15a52dd) Lakin et al., 2017 https://githu...
- Full pipeline: read trimming [BLAST, Bowtie2 v2.3.0] -> dimensionality reduction/clustering [R, UMAP] -> structure determination [R] -> visualisation [UMAP] -> stage not stated [Jupyter, SciPy]

### Transmission, infectivity, and neutralization of a spike L452R SARS-CoV-2 variant. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.025 | PMCID: PMC8057738 | PMID: 33991487
- Evidence: Welch’s t test, as implemented in R (version 4.0.3) using the rstatix_0.7.0 package and Python (version 3.7.9) using scipy package (version 1.5.2), was used to compare the N gene C t values between B.1.427/B.1.429 variant and non-B.1.427/B.1.429 groups.
- Full pipeline: alignment/mapping [BLAST, MAFFT, Nextstrain] -> stage not stated [IQ-TREE v1.6, Python v3.7.9, R v4.0, SciPy]

### In vivo structural characterization of the SARS-CoV-2 RNA genome identifies host proteins vulnerable to repurposed drugs. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.008 | PMCID: PMC7871767 | PMID: 33636127
- Evidence: The Spearman correlation efficient and the two-tailed P values were calculated using the Python package function scipy.stats.spearmanr .
- Full pipeline: read trimming [Bowtie2, SAMtools, Trimmomatic] -> alignment/mapping [MAFFT v7.313] -> differential/statistical testing [SciPy] -> simulation/modelling [UCSF Chimera] -> structure determination [UCSF Chimera] -> visualisation [RAxML v8.2.12] -> stage not stated [AutoDock Vina]

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ...ls Case et al., 2017 Version 17.0 pdb-tools Rodrigues et al., 2018 Version 2.0.5 MDTraj McGibbon et al., 2015 Version 1.9.4 Pandas https://conference.scipy.org/proceedings/scipy2010/pdfs/mckinney.pdf Version 1.0.5 Custom code, molecular dynamics set up and processing This paper https://github.com/choderalab/rbd-ace2-contact-analysis Custom code, evaluation of clinical samples This paper https://gi...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### Dynamic 3D proteomes reveal protein functional alterations at high resolution in situ. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.021 | PMCID: PMC7836100 | PMID: 33357446
- Evidence: To statistically assess the combination of the qvalues, a Fisher's combined probability test has been applied to combine q-values using the “combine_pvalues” function of the open-source python-based Scipy library.
- Full pipeline: differential/statistical testing [SciPy, limma] -> stage not stated [AutoDock Vina v1.1.2, Bioconductor, NAMD v2.13, PyMOL v2.4, Python, R, pheatmap, seaborn]

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Evidence: Area and volume are estimated from the coordinates of the polymer beads belonging to the region under consideration by means of a 3D convex hull approximation, computed with the Python package scipy.spatial.
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Evidence: ...ing ≥10 samples per cancer type, within a TCGA cancer type to the distances between that cancer type and all others through a Mann-Whitney U test via Scipy ( Virtanen et al., 2020 ) with an FDR multiple test correction across cancer types through statsmodels ( Seabold and Perktold, 2010 ), as shown in Data S3.2 G.
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq. (Cell 2022)

- DOI: 10.1016/j.cell.2022.05.013 | PMCID: PMC9380471 | PMID: 35688146
- Evidence: Downstream analyses were performed in Python, using a combination of numpy, scipy, Pandas, scikit-learn, pomegranate, infercnvpy, pygenometracks, scanpy and seaborn libraries.
- Full pipeline: alignment/mapping [STAR v2.7.9a, velocyto] -> quantification [RepeatMasker, STAR v2.7.9a] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [Enrichr, NumPy, Python, Scanpy, SciPy, scikit-learn, seaborn]

### Mapping transcriptomic vector fields of single cells. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.045 | PMCID: PMC9332140 | PMID: 35108499
- Evidence: The fixed points are defined as points where the value of the vector field function is zero: f ( x ) = 0 , and the solution can be obtained using any nonlinear equation solver ( SciPy fsolve is used in our case).
- Full pipeline: quantification [scVelo, scikit-learn] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [SciPy]

### Immune imprinting, breadth of variant recognition, and germinal center response in human SARS-CoV-2 infection and vaccination. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.018 | PMCID: PMC8786601 | PMID: 35148837
- Version used: **1.6.2**
- Evidence: For the analysis of the homogeneity or dispersion of serology measurements in groups differing by vaccination or infection status ( Figures 2 C and 2D) at a particular time point, we plotted each group’s distribution of Euclidean distances to its centroid (calculated with Python package scipy version 1.6.2).
- Full pipeline: dimensionality reduction/clustering [NumPy v1.19.1, scikit-learn v1.0] -> visualisation [SciPy v1.6.2] -> stage not stated [Matplotlib v3.3.2, QuPath v0.2.3, R v4.0.5, ggplot2, seaborn v0.11.2]

### Multiple early factors anticipate post-acute COVID-19 sequelae. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.014 | PMCID: PMC8786632 | PMID: 35216672
- Evidence: Statistics for survival analysis were gathered via a chi-squared test as implemented via scipy.stats.chi2_contingency.
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.6.0, UMAP v0.5.1, scDblFinder v0.2.1] -> differential/statistical testing [SciPy, XGBoost] -> stage not stated [BLAST v2.12.0, GSVA, Pilon, R, scikit-learn v0.24.2]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: ...2 http://bioconductor.org/packages/release/bioc/html/scater.html Scikit-learn ( Pedregosa et al., 2011 ) https://github.com/scikit-learn/scikit-learn Scipy ( Virtanen et al., 2020 ) https://scipy.org/ ScVelo ( Bergen et al., 2020 ) v0.1.24 https://github.com/theislab/scvelo Sparse Decomposition of Arrays ( Hore et al., 2016 ) https://jmarchini.org/software/#sda Seaborn Waskom v0.11.1 https://seabo...
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Transition to invasive breast cancer is associated with progressive changes in the structure and composition of tumor stroma. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.023 | PMCID: PMC8792442 | PMID: 35063072
- Evidence: Python packages used for spatial enrichment analysis and collagen morphometrics were sckikit-image, pandas, numpy, xarray, scipy, statsmodels.
- Full pipeline: quantification [ImageJ] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, R v1.16.0, clusterProfiler v3.19.0] -> visualisation [Matplotlib, Python, pheatmap, seaborn] -> stage not stated [GSEA, NumPy, SciPy, statsmodels, xarray]

### Transmission from vaccinated individuals in a large SARS-CoV-2 Delta variant outbreak. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.027 | PMCID: PMC8695126 | PMID: 35051367
- Evidence: For comparisons of the number of iSNVs by vaccination status we performed an independent t-test using the statistics functions from the SciPy package.
- Full pipeline: dimensionality reduction/clustering [Matplotlib] -> differential/statistical testing [SciPy] -> visualisation [Matplotlib] -> stage not stated [Nextstrain v3.0.3, R]

### Systematic identification and characterization of genes in the regulation and biogenesis of photosynthetic machinery. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.007 | PMCID: PMC10760936 | PMID: 38065083
- Evidence: The resulting genomic positions corresponding to likely cassette insertion positions were clustered (using scipy.cluster.hierarchy.fclusterdata(t=3000, criterion=’distance’, method=’average’)).
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [SciPy] -> stage not stated [AlphaFold, Cutadapt, PyMOL]

### Cytoplasmic division cycles without the nucleus and mitotic CDK/cyclin complexes. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.010 | PMCID: PMC10659773 | PMID: 37832525
- Evidence: The parameters A 1 , A 2 , τ 1 , τ 2 , and B were acquired by fitting the timeseries to a double exponential decay function using SciPy’s curve_fit function: f ( t ) = B + ∑ 1 2 A i e − τ i t The ratio between the corrected mean fluorescence intensity of the two channels was then calculated as: E m i s s i o n R a t i o = C 2 c o r r C 3 c o r r To facilitate the comparison of dynamics, the emissi...
- Full pipeline: quantification [Python] -> stage not stated [ImageJ, SciPy]

### Distinct molecular profiles of skull bone marrow in health and neurological disorders. (Cell 2023)

- DOI: 10.1016/j.cell.2023.07.009 | PMCID: PMC10443631 | PMID: 37562402
- Evidence: Dendrograms With scanpy's dendrogram function SciPy’s hierarchical linkage clustering was calculated on a Pearson correlation matrix over regions which was calculated for 50 averaged principal components.
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC] -> normalisation [UMAP] -> dimensionality reduction/clustering [SciPy, UMAP, scVelo] -> differential/statistical testing [CellPhoneDB, DESeq2] -> structure determination [scVelo] -> machine learning [ilastik] -> visualisation [seaborn] -> stage not stated [AnnData v0.7.5, Enrichr, Fiji, GSEA, ImageJ, PHENIX, Python v3.7, SPM, Scanpy, WGCNA, scikit-learn, velocyto v0.17.17]

### Engineering RNA export for measurement and manipulation of living cells. (Cell 2023)

- DOI: 10.1016/j.cell.2023.06.013 | PMCID: PMC10528933 | PMID: 37437570
- Version used: **1.4.1**
- Evidence: To determine clone growth rates, we fit an exponential growth model f(t) = Ae kt to each clone abundance trajectory, where f(t) is clone abundance (in units of CPMS) and t is time (days), using non-linear least squares with initial parameter guesses of A = 10,000 and k = 0, as implemented in the curve_fit() function of scipy (1.4.1).
- Full pipeline: alignment/mapping [HTSeq, STAR v2.7.8a] -> quantification [SciPy v1.4.1] -> normalisation [scikit-image v0.19.2] -> differential/statistical testing [DESeq2 v1.30.1, R v4.0.5] -> simulation/modelling [SciPy v1.4.1] -> stage not stated [PyMOL]

### Cryo-EM structure of gas vesicles for buoyancy-controlled motility. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.041 | PMCID: PMC9994262 | PMID: 36868215
- Evidence: A sigmoid function with p 0 as the inflection point and k as the width was fitted to the curves using the means and standard deviations of measured triplicates (n = 3) as input for the scipy 'curve_fit' function.
- Full pipeline: stage not stated [AlphaFold, CTFFIND v1.06, ChimeraX v1.4, ColabFold, HMMER, ImageJ, PHENIX v1.13, RELION v3.1, SciPy]

### Structural and functional map for forelimb movement phases between cortex and medulla. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.009 | PMCID: PMC9842395 | PMID: 36608651
- Evidence: 2D density plots were generated using 2D-kernel density estimate (2D-KDE), plotting 5 or 7 density lines covering the space of 10-100% or 30-100% of highest density using Scipy, a Python library for scientific computing.
- Full pipeline: differential/statistical testing [statsmodels] -> stage not stated [DeepLabCut, Kilosort, Python v3.7, SciPy, TrackMate v6.0.3, scikit-learn]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Version used: **1.9.3**
- Evidence: ...oom v.0.7.6, e1071 v.1.7.6, and table1 v.1.4 Python packages N/A biopython v1.79, matplotlib v3.7.1, numpy v1.22.3, pandas v1.5.1, scikit-bio v0.5.8, scipy v1.9.3, seaborn v0.11.2, statannot v0.2.3, and statsmodels v0.13.2 Other Leica Reichert Ultracut-S microtome Leica N/A JEOL 1200EX Transmission electron microscope JEOL USA N/A AMT 2k CCD camera Advanced Microscopy Techniques N/A Illumina NovaS...
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Pan-cancer proteogenomics characterization of tumor immunity. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.027 | PMCID: PMC10988632 | PMID: 38359819
- Evidence: These measurements were aggregated at the slide level, Pearson correlated with cytokine expression pathway scores at the patient level, and significance tested using scipy.stats.pearsonr, which performs a test of the null hypothesis that the underlying sample distributions are uncorrelated and normally distributed.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, Enrichr] -> differential/statistical testing [GSVA, SciPy] -> machine learning [R] -> visualisation [GSVA] -> stage not stated [Cellpose, scikit-image]

### Coordinating brain-distributed network activities in memory resistant to extinction. (Cell 2024)

- DOI: 10.1016/j.cell.2023.12.018 | PMCID: PMC7615560 | PMID: 38242086
- Evidence: We computed the time course of each IMF amplitude ( Figure S2C , upper panel) using the Hilbert transform (scipy.signal.hilbert) and normalized each instantaneous amplitude by its standard deviation.
- Full pipeline: normalisation [SciPy] -> dimensionality reduction/clustering [Kilosort, UMAP] -> differential/statistical testing [NumPy, Python v3.6, seaborn] -> visualisation [Matplotlib] -> stage not stated [Astropy v2.0.2, scikit-learn v0.19.1]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Evidence: 37 Statistical analysis Statistical tests were performed using Python SciPy package v1.9.3.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Evolution of Mycobacterium tuberculosis transcription regulation is associated with increased transmission and drug resistance. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.005 | PMCID: PMC12624571 | PMID: 41033311
- Evidence: Peak positions were called using find_peaks in scipy with a minimum distance of 500 bases between peaks and the top 50 peaks and nearby genes are shown in Table S4 .
- Full pipeline: quality control [Bowtie2, Cutadapt] -> read trimming [Bowtie2, Cutadapt, fastp] -> alignment/mapping [Bowtie2, Cutadapt] -> variant calling [BCFtools] -> stage not stated [BLAST, SAMtools, SciPy]

### Inner speech in motor cortex and implications for speech neuroprostheses. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.015 | PMCID: PMC12360486 | PMID: 40816265
- Version used: **1.11.4**
- Evidence: ...orks.com/products/matlab.html RRID:SCR_001622 BRAND Ali et al 2024 https://github.com/brandbci/brand Python 3.9 python.org/downloads/ RRID:SCR_008394 SciPy 1.11.4 scipy.org RRID:SCR_008058 NumPy 1.26.2 numpy.org RRID:SCR_008633 Pandas 2.1.3 pandas.pydata.org RRID:SCR_018214 scikit-learn 1.3.2 scikit-learn.org RRID:SCR_002577 matplotlib 3.8.2 matplotlib.org RRID:SCR_008624 seaborn 0.13.0 seaborn.py...
- Full pipeline: stage not stated [Matplotlib v3.8.2, NumPy v1.26.2, Python v3.9, SciPy v1.11.4, scikit-learn v1.3.2, seaborn v0.13.0]

### Dopamine encodes deep network teaching signals for individual learning trajectories. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.025 | PMCID: PMC7619352 | PMID: 40505657
- Evidence: Both signals were then de-noised to remove short-pulse artefacts using a median filter with kernel size 5 (medfilt from scipy.signal).
- Full pipeline: normalisation [scikit-learn] -> differential/statistical testing [scikit-learn] -> stage not stated [DeepLabCut, Matplotlib, NumPy, PyTorch v2.5.1, Python, SciPy, seaborn, statsmodels]

### Nanoscale DNA tracing reveals the self-organization mechanism of mitotic chromosomes. (Cell 2025)

- DOI: 10.1016/j.cell.2025.02.028 | PMCID: PMC12127698 | PMID: 40132578
- Evidence: Scaling exponents were calculated by fitting tracing data at selected genomic intervals to a power-law function (y=ax b ) using non-linear least squares fitting (scipy curve_fit).
- Full pipeline: quantification [NumPy] -> normalisation [SciPy] -> simulation/modelling [NumPy, OpenMM] -> machine learning [scikit-learn] -> stage not stated [Python, napari, scikit-image]

### Contextual computation by competitive protein dimerization networks. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.036 | PMCID: PMC11973712 | PMID: 39978343
- Evidence: The optimize.dual_annealing function in the scipy Python package (version 1.10.1) was used to perform such optimizations.
- Full pipeline: stage not stated [NetworkX, Python v3.8.13, SciPy, seaborn v0.12.2]

### Global genetic interaction network of a human cell maps conserved principles and informs functional interpretation of gene co-essentiality profiles. (Cell 2026)

- DOI: 10.1016/j.cell.2026.03.044 | PMCID: PMC13281610 | PMID: 42049019
- Evidence: In doing so, we generated two PCC and P -values using scipy.stats.pearsonr 171 for each pair of genes tested based on Gene A fitness-Gene B expression and Gene A expression-Gene B fitness.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, STAR] -> variant calling [GATK] -> visualisation [Cytoscape] -> stage not stated [ANNOVAR, R, SciPy]

### The E3-ome gene-centric compendium reveals the human E3 ligase landscape. (Cell 2026)

- DOI: 10.1016/j.cell.2026.01.029 | PMCID: PMC13061254 | PMID: 41864206
- Version used: **1.15**
- Evidence: 226 https://scanpy.readthedocs.io/en/stable/ scipy (v1.15) Virtanen et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, AnnData v0.11, Bioconductor v3.19, Clustal Omega, Matplotlib v3.10, NumPy v1.26, Python v3.10, R v4.4.2, Scanpy v1.9, SciPy v1.15, edgeR v4.2.2, limma v3.60.6]

### Symptom prevalence, duration, and risk of hospital admission in individuals infected with SARS-CoV-2 during periods of omicron and delta variant dominance: a prospective observational study from the ZOE COVID Study. (Lancet 2022)

- DOI: 10.1016/s0140-6736(22)00327-0 | PMCID: PMC8989396 | PMID: 35397851
- Evidence: Statistical analysis Statistical analysis was done using Python version 3.8.10 (pandas, NumPy, SciPy, statsmodel).
- Full pipeline: differential/statistical testing [NumPy, SciPy]

### Cortical responses to touch reflect subcortical integration of LTMR signals. (Nature 2021)

- DOI: 10.1038/s41586-021-04094-x | PMCID: PMC9289451 | PMID: 34789880
- Version used: **1.5.2**
- Evidence: Data Analysis and Statistics Data were analyzed in Matlab (versions 2017a and 2017b) and python (version 3.7.7) using the following packages (versions in parentheses): conda (4.8.5), matplotlib (3.3.1), numpy (1.18.5), pims (0.5), pyabf (2.2.6), scipy (1.5.2), scikit-image (0.16.2), scikit-learn (0.23.2), and seaborn (0.11.0).
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [Matplotlib v3.3.1, NumPy v1.18.5, SciPy v1.5.2, scikit-image v0.16.2, seaborn v0.11.0]

### The cellular environment shapes the nuclear pore complex architecture. (Nature 2021)

- DOI: 10.1038/s41586-021-03985-3 | PMCID: PMC8550940 | PMID: 34646014
- Evidence: This workflow was performed using a Python script running SciPy.Stats (for P value and Z -score analysis) 51 , the StatsModels module (for Benjamini–Hochberg analysis) 52 and Matplotlib (for plots) 53 .
- Full pipeline: alignment/mapping [IMOD] -> differential/statistical testing [Matplotlib, Python, SciPy] -> stage not stated [RELION, UCSF Chimera]

### Isoform cell-type specificity in the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03969-3 | PMCID: PMC8494650 | PMID: 34616073
- Evidence: Then we found the outer hull of the MOp by using scipy.spatial.ConvexHull.
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.0.3, NumPy v1.18.1, UMAP, statsmodels v0.12.1] -> stage not stated [Scanpy, SciPy, kallisto, scikit-learn]

### Reconstruction of ancient microbial genomes from the human gut. (Nature 2021)

- DOI: 10.1038/s41586-021-03532-0 | PMCID: PMC8189908 | PMID: 33981035
- Evidence: Simulation of the effects of aDNA damage on assembly was performed using the Python package SciPy.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5.1, IQ-TREE v1.6.11, Picard, SAMtools v1.9] -> variant calling [freebayes v1.1.0] -> normalisation [Picard] -> dimensionality reduction/clustering [ggplot2, ggpubr, pheatmap, tidyverse] -> differential/statistical testing [freebayes v1.1.0, ggplot2, ggpubr, pheatmap, tidyverse] -> simulation/modelling [SciPy] -> visualisation [Matplotlib, NumPy, ggplot2, ggpubr, pheatmap, tidyverse] -> stage not stated [BEAST v2.5.1, Cutadapt v2.8, HMMER v3.1b, Kraken2 v2.0.8, R, RAxML v8.1.15]

### Breast tumours maintain a reservoir of subclonal diversity during expansion. (Nature 2021)

- DOI: 10.1038/s41586-021-03357-x | PMCID: PMC8049101 | PMID: 33762732
- Version used: **1.4.1**
- Evidence: Plots were generated with the R package ‘ggplot2’ (v3.2.1) 65 SciPy (v.1.4.1) 66 and pandas (v1.01) 67 Acoustic Cell Tagmentation Procedure FACS sorted 384 well plates were spun at 1500xg for > 4min.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.6, SAMtools v1.2] -> quantification [Salmon v0.14] -> normalisation [DESeq2 v1.26.0] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ComplexHeatmap v2.2.0] -> stage not stated [ANNOVAR, BEDTools v2.26.0, Bioconductor, GATK v4.1.3, Picard, SciPy v1.4.1, fgsea, ggplot2, igraph]

### The kinetic landscape of an RNA-binding protein in cells. (Nature 2021)

- DOI: 10.1038/s41586-021-03222-x | PMCID: PMC8299502 | PMID: 33568810
- Evidence: ...Fishers’ t-test represented as F). p is theLL hypergeometric p value of enrichment, based on the F-test 50 ) Hypergeometric tests were performed with Scipy hypergeom module 62 (ref.
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [BEDTools, Bowtie2 v2.4.2, Cytoscape v3.4.0, FastQC v0.11.9, SAMtools] -> quantification [ImageJ v1.8.0] -> differential/statistical testing [SciPy] -> structure determination [FastQC v0.11.9] -> visualisation [ggplot2] -> stage not stated [Python v3.9.0, R v2.0.0]

### Skin-resident innate lymphoid cells converge on a pathogenic effector state. (Nature 2021)

- DOI: 10.1038/s41586-021-03188-w | PMCID: PMC8336632 | PMID: 33536623
- Evidence: A negative association between Il2ra and the weights for topic 1 was determined by calculating Spearman’s ρ with the scipy.stats.spearmanr function (v.1.3.2) [ 64 ], using the topic weights and the log-normalized scTransform-corrected expression values for Il2ra as inputs.
- Full pipeline: normalisation [SciPy, Seurat, Signac, UMAP] -> dimensionality reduction/clustering [Scanpy, UMAP] -> visualisation [UMAP] -> stage not stated [Bioconductor]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Evidence: In Python, we used the mannwhitneyu function from scipy package version 1.3.1 70 for nonparametric tests, and corrected for multiple testing with the statsmodels package version 0.10.1 71 .
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### A non-hallucinogenic psychedelic analogue with therapeutic potential. (Nature 2021)

- DOI: 10.1038/s41586-020-3008-z | PMCID: PMC7874389 | PMID: 33299186
- Evidence: This pixel change oscillation was graphically smoothed using the Savgol filter in SciPy.
- Full pipeline: stage not stated [ImageJ, SciPy]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Evidence: Analyses and visualization of data were conducted in a Python environment built on the Numpy, SciPy, matplotlib, scikit-learn package and pandas libraries.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Hydroclimatic vulnerability of peat carbon in the central Congo Basin. (Nature 2022)

- DOI: 10.1038/s41586-022-05389-3 | PMCID: PMC9729114 | PMID: 36323786
- Version used: **1.7.1**
- Evidence: ...), ipython (7.28.0), jupyter (1.0.0), KDE-diffusion (1.0.3), matplotlib (3.4.3), notebook (6.4.4), numpy (1.20.3), pandas (1.3.3), rioxarray (0.7.1), scipy (1.7.1) and shapely (1.7.1) packages.
- Full pipeline: alignment/mapping [Python v3.7.3] -> differential/statistical testing [R] -> stage not stated [Matplotlib v3.4.3, NumPy v1.20.3, SciPy v1.7.1]

### Borgs are giant genetic elements with potential to expand metabolic capacity. (Nature 2022)

- DOI: 10.1038/s41586-022-05256-1 | PMCID: PMC9605863 | PMID: 36261517
- Evidence: The number of reads aligning to each genome was then parsed into a matrix and the correlation between abundance patterns for Methanoperedens and Borg genomes was then calculated using Pearson correlation metric as implemented in scipy 42 .
- Full pipeline: alignment/mapping [BLAST, IQ-TREE v1.6.6, MAFFT, SciPy] -> quantification [SciPy] -> visualisation [BLAST, IQ-TREE v1.6.6, MAFFT] -> stage not stated [HMMER]

### Personalizing exoskeleton assistance while walking in the real world. (Nature 2022)

- DOI: 10.1038/s41586-022-05191-1 | PMCID: PMC9556303 | PMID: 36224415
- Version used: **1.3.2**
- Evidence: The required python packages are numpy (1.17.4), scikit-learn (0.21.3), scipy (1.3.2) and matplotlib (2.0.2).
- Full pipeline: stage not stated [Matplotlib v2.0.2, NumPy v1.17.4, SciPy v1.3.2, scikit-learn v0.21.3]

### Antibiotic combinations reduce Staphylococcus aureus clearance. (Nature 2022)

- DOI: 10.1038/s41586-022-05260-5 | PMCID: PMC9533972 | PMID: 36198788
- Evidence: (3) An exact Euclidean distance transform was used to yield a distance matrix of each pixel to its nearest zero pixel (scipy.ndimage.distance_transform_edt).
- Full pipeline: dimensionality reduction/clustering [scikit-image] -> stage not stated [Python, SciPy]

### Observations of a Magellanic Corona. (Nature 2022)

- DOI: 10.1038/s41586-022-05090-5 | PMCID: PMC9519455 | PMID: 36171382
- Evidence: Furthermore, the following software was used in this work: Astropy 62 , 63 , calcos 33 , cartopy 64 , lmfit 37 , SciPy 65 , VoigtFit 36 , Cloudy 45 and Pingouin 66 .
- Full pipeline: normalisation [Cloudy] -> stage not stated [Astropy, SciPy]

### Delayed fluorescence from inverted singlet and triplet excited states. (Nature 2022)

- DOI: 10.1038/s41586-022-05132-y | PMCID: PMC9477729 | PMID: 36104553
- Evidence: Thus, k r + k nr , k ISC and k RISC were determined without assuming k ISC >> k RISC by fitting the S 1 population in equation ( 1 ) to the transient PL decay data using the scipy.integrate.odeint and scipy.optimize.curve_fit functions in Python 3.7 50 . k r and k nr were determined from Φ PL = k r /( k r + k nr ) assuming negligible non-radiative decay of T 1 to S 0 .
- Full pipeline: stage not stated [Python v3.7, SciPy]

### Divergent genomic trajectories predate the origin of animals and fungi. (Nature 2022)

- DOI: 10.1038/s41586-022-05110-4 | PMCID: PMC9492541 | PMID: 36002568
- Evidence: Mann–Whitney U -tests (one-tailed) were done in Python with SciPy 65 (scipy.stats.mannwhitneyu).
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [BLAST, IQ-TREE, MAFFT, OrthoFinder, eggNOG] -> dimensionality reduction/clustering [OrthoFinder, eggNOG] -> differential/statistical testing [NumPy, Python, ggplot2] -> structure determination [R] -> stage not stated [Keras, SciPy, TensorFlow]

### Visual recognition of social signals by a tectothalamic neural circuit. (Nature 2022)

- DOI: 10.1038/s41586-022-04925-5 | PMCID: PMC9352588 | PMID: 35831500
- Evidence: 1 mean ∆ F / F ( bout ) − mean ∆ F / F ( continuous ) mean ∆ F / F ( bout ) + mean ∆ F / F ( continuous ) Tuning peaks For computing peaks in the tuning of neurons to a variable, mean ∆ F / F responses were interpolated with a one-dimensional spline (scipy.interpolate.InterpolatedUnivariateSpline, k = 2, second degree) and the location of the maximum was computed.
- Full pipeline: quantification [Python] -> normalisation [ANTs] -> registration [ANTs, ImageJ] -> dimensionality reduction/clustering [ANTs, SciPy, scikit-image, seaborn] -> differential/statistical testing [NumPy] -> stage not stated [PsychoPy, Suite2p, pandas v1.3.0, scikit-learn]

### Nanoscale imaging of phonon dynamics by electron microscopy. (Nature 2022)

- DOI: 10.1038/s41586-022-04736-8 | PMCID: PMC9177420 | PMID: 35676428
- Evidence: The fit was obtained using scipy.optimize, a Python library and fitting coefficients, and covariances were extracted.
- Full pipeline: alignment/mapping [Matplotlib] -> visualisation [Matplotlib] -> stage not stated [Python, SciPy]

### MCM complexes are barriers that restrict cohesin-mediated loop extrusion. (Nature 2022)

- DOI: 10.1038/s41586-022-04730-0 | PMCID: PMC9159944 | PMID: 35585235
- Evidence: Both P c ( s ) curves and their log-space slopes are shown following a Gaussian smoothing (using the scipy.ndimage.filters.gaussian_smoothing1d function with radius 0.8).
- Full pipeline: alignment/mapping [kallisto] -> differential/statistical testing [R] -> stage not stated [Fiji, ImageJ, NumPy, Python, SciPy, ggplot2]

### The development and evolution of inhibitory neurons in primate cerebrum. (Nature 2022)

- DOI: 10.1038/s41586-022-04510-w | PMCID: PMC8967711 | PMID: 35322231
- Evidence: To identify genes that were activated or inactivated along trajectories, we used linear regression implemented in SciPy based on latent time values ( x ) versus gene expression values ( y ).
- Full pipeline: quantification [kallisto v0.46] -> dimensionality reduction/clustering [AnnData, Scanpy, Seurat, UMAP] -> differential/statistical testing [SciPy, statsmodels v0.12.2] -> simulation/modelling [SciPy, scVelo] -> stage not stated [ImageJ, Python, scDblFinder v0.2.2]

### A biophysical account of multiplication by a single neuron. (Nature 2022)

- DOI: 10.1038/s41586-022-04428-3 | PMCID: PMC8891015 | PMID: 35197635
- Version used: **1.3**
- Evidence: Data were corrected for the liquid junction potential and analysed using custom-written software in Python v.3.7 (Python Software Foundation) using NumPy v.1.15, Pandas v.0.25, SciPy v.1.3, Matplotlib v.3.0 and pyABF v.2.1 ( https://pypi.org/project/pyabf/ ).
- Full pipeline: stage not stated [ImageJ v2.0, Matplotlib v3.0, NumPy v1.15, Python v3.7, SciPy v1.3]

### Signatures of TOP1 transcription-associated mutagenesis in cancer and germline. (Nature 2022)

- DOI: 10.1038/s41586-022-04403-y | PMCID: PMC8866115 | PMID: 35140396
- Version used: **1.6.3**
- Evidence: Two-sided non-parametric Mann–Whitney U -tests were performed for quantitative measurements; multiple testing correction, FDR set at 0.05; and, for categorical data, Fisher’s exact tests were performed in Python using stats.fisher_exact from scipy v.1.6.3.
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BCFtools v1.10.2, BWA v0.7.12, Mutect2] -> variant calling [BCFtools v1.10.2, GATK v3.6, Mutect2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [SciPy v1.6.3] -> stage not stated [Manta v0.28.0, Python v3.8.5, R v4.0.5, SAMtools v1.9, Strelka v2.4.7]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Evidence: These analyses were performed in Python (v.3.6) using Scikit-learn for PCA (v.0.23.2), Scipy for hierarchical clustering (v.1.5.1) and nheatmap for heat map and clustering visualization (v.0.1.4).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### Toroidal topology of population activity in grid cells. (Nature 2022)

- DOI: 10.1038/s41586-021-04268-7 | PMCID: PMC8810387 | PMID: 35022611
- Evidence: These edge values were then lifted to integer coefficients and subsequently smoothed by minimizing the sum over all edges (using the scipy implementation ‘lsmr’).
- Full pipeline: dimensionality reduction/clustering [Matplotlib v3.1.3, NumPy v1.18.1, UMAP, scikit-learn v0.22.1] -> differential/statistical testing [Python] -> stage not stated [Kilosort v2.5, SciPy]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Version used: **1.3**
- Evidence: Predictor architecture The machine learning framework was built on Python (version 3.7.4) using the following libraries: scikit-learn (version 0.21.2), numpy (version 1.16.4), scipy (version 1.3), pandas (version 0.24.2) within a Singularity container (version 2.4.6-dist).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### Landscape dynamics and the Phanerozoic diversification of the biosphere. (Nature 2023)

- DOI: 10.1038/s41586-023-06777-z | PMCID: PMC10700141 | PMID: 38030724
- Evidence: Top panel shows Strontium isotopic ratio of seawater for the Phanerozoic 39 (grey line represents the data from 39 and the black line shows the corresponding least square regression using SciPy Savitzky-Golay filter).
- Full pipeline: differential/statistical testing [SciPy] -> stage not stated [Jupyter]

### Human mobility networks reveal increased segregation in large cities. (Nature 2023)

- DOI: 10.1038/s41586-023-06757-3 | PMCID: PMC10733138 | PMID: 38030732
- Evidence: We perform interpolation using the interpolate package of the scipy library.
- Full pipeline: stage not stated [SciPy, lme4]

### CD201&lt;sup&gt;+&lt;/sup&gt; fascia progenitors choreograph injury repair. (Nature 2023)

- DOI: 10.1038/s41586-023-06725-x | PMCID: PMC10665192 | PMID: 37968392
- Evidence: Statistics Statistical analyses were performed using the Python toolkit Scipy.
- Full pipeline: alignment/mapping [STAR v2.5.2a, Scanpy] -> quantification [Matplotlib, seaborn] -> dimensionality reduction/clustering [UMAP, scVelo] -> differential/statistical testing [SciPy] -> simulation/modelling [scVelo]

### Neural landscape diffusion resolves conflicts between needs across time. (Nature 2023)

- DOI: 10.1038/s41586-023-06715-z | PMCID: PMC10651489 | PMID: 37938783
- Evidence: These analyses relied heavily on Numpy 57 , Scipy 58 , Pandas 59 , and Scikit-learn 60 .
- Full pipeline: dimensionality reduction/clustering [Scanpy] -> stage not stated [Jupyter, Kilosort, Matplotlib, NumPy, Python, SciPy, scikit-learn, seaborn]

### Preserved neural dynamics across animals performing similar behaviour. (Nature 2023)

- DOI: 10.1038/s41586-023-06714-0 | PMCID: PMC10665198 | PMID: 37938772
- Evidence: All the analyses were implemented in Python using open-source packages such as numpy, matplotlib, sci-kit, scipy and pandas 70 – 74 and custom code.
- Full pipeline: machine learning [PyTorch] -> stage not stated [Jupyter, Kilosort v2.0, Matplotlib, NumPy, Python, SciPy]

### Neural signal propagation atlas of Caenorhabditis elegans. (Nature 2023)

- DOI: 10.1038/s41586-023-06683-4 | PMCID: PMC10632145 | PMID: 37914938
- Evidence: (4) Traces are smoothed using a causal polynomial filtering with a window size of 6.5 s and polynomial order of 1 (Savitzky–Golay filters with windows completely ‘in the past’; for example, obtained with scipy.signal.savgol_coeffs(window_length=13, polyorder=1, pos=12)).
- Full pipeline: stage not stated [SciPy]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Version used: **1.7.3**
- Evidence: A hypergeometric test (scipy v.1.7.3) was used to determine whether genesets of interest were differentially enriched in the condition A geneset vs condition B geneset.
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Version used: **1.7.1**
- Evidence: Data were analysed and figures generated using Python (version 3.9.1), along with packages numpy (version 1.20.3), scipy (version 1.7.1), matplotlib (version 3.4.3), and pandas (version 1.3.0), and R (version 3.6.0).
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Spatial atlas of the mouse central nervous system at molecular resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-06569-5 | PMCID: PMC10709140 | PMID: 37758947
- Version used: **1.6.3**
- Evidence: ...106, Jupyter Notebook 6.0.3, Anaconda 2-2-.02, h5py 3.1.0, hdbscan 0.8.36, hdf5 1.10.4, matplotlib 3.1.3, seaborn 0.11.0, scanpy 1.6.0, numpy 1.19.4, scipy 1.6.3, pandas 1.2.3, scikit-learn 0.22, umap-learn0.4.3, pip 21.0.1, numba 0.51.2, tifffile 2020.10.1, scikit-image 0.18.1, squidpy 1.1.2, anndata 0.8.0 and itertools 8.0.0.
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [AnnData v0.8.0, ChimeraX v1.0, Conda, ImageJ v1.51, Jupyter, Matplotlib v3.1.3, NumPy v1.19.4, Python v3.6, R v4.0, Scanpy v1.6.0, SciPy v1.6.3, Squidpy v1.1.2, UMAP, scikit-image v0.18.1, scikit-learn v0.22, seaborn v0.11.0]

### A foundation model for generalizable disease detection from retinal images. (Nature 2023)

- DOI: 10.1038/s41586-023-06555-x | PMCID: PMC10550819 | PMID: 37704728
- Version used: **1.5.4**
- Evidence: Results were further analysed and visualized with Python v.3.6, NumPy v.1.19.5, SciPy v.1.5.4, seaborn v.0.12.0, Matplotlib v.3.6.1, pandas v.1.5.0, Scikit-Learn v.1.1.3 and Pillow v.9.2.0.
- Full pipeline: visualisation [Matplotlib v3.6.1, NumPy v1.19.5, SciPy v1.5.4, seaborn v0.12.0] -> stage not stated [Keras, PyTorch]

### Uncovering new families and folds in the natural protein universe. (Nature 2023)

- DOI: 10.1038/s41586-023-06622-3 | PMCID: PMC10584680 | PMID: 37704037
- Version used: **1.5.4**
- Evidence: Pearson correlation was computed using SciPy (v.1.5.4).
- Full pipeline: quality control [scikit-learn v1.1.1] -> alignment/mapping [BLAST, MUSCLE] -> machine learning [PyTorch v1.12.0, scikit-learn v1.1.1] -> visualisation [NetworkX v2.5.1, PyMOL v2.5.0] -> stage not stated [AlphaFold, HMMER v3.3, SciPy v1.5.4]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Evidence: We used a 1.13 µm × 1.13 µm grid size (1,024 grid spaces/FOV), with a spatial resolution as in our previous work with GCaMP6f 37 and an automated detection strategy using the open-source Scipy.Signal (v.1.10.0; https://docs.scipy.org/doc/scipy/reference/signal.html ) analysis package and Neurokit2 (v.0.1.6) 88 .
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### Complete human day 14 post-implantation embryo models from naive ES cells. (Nature 2023)

- DOI: 10.1038/s41586-023-06604-5 | PMCID: PMC10584686 | PMID: 37673118
- Version used: **1.8.0**
- Evidence: Visualization and statistical analyses of the cell numbers and SEM efficiencies were performed using Python (v.3.8.5) software with scipy (v.1.8.0) and seaborn (v.0.11.0) libraries.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Signac v1.6.0] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [SciPy v1.8.0, seaborn v0.11.0] -> visualisation [SciPy v1.8.0, seaborn v0.11.0] -> stage not stated [R, pheatmap, scDblFinder v1.6]

### Water in the terrestrial planet-forming zone of the PDS 70 disk. (Nature 2023)

- DOI: 10.1038/s41586-023-06317-9 | PMCID: PMC10432267 | PMID: 37488359
- Evidence: The continuum level is determined by selecting line-free regions and adopting a cubic spline interpolation (scipy.interpolate.interp1d).
- Full pipeline: differential/statistical testing [dynesty] -> visualisation [Matplotlib v3.5.1] -> stage not stated [SciPy]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Evidence: Significance was obtained by chi-square analysis (scipy.stats.chi2_contingency) and the P value was corrected using the Benjamini–Hochberg method.
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### Diverse organic-mineral associations in Jezero crater, Mars. (Nature 2023)

- DOI: 10.1038/s41586-023-06143-z | PMCID: PMC10371864 | PMID: 37438522
- Evidence: This was performed using the SciPy Python package 53 .
- Full pipeline: stage not stated [OpenCV, Python, SciPy]

### Relaxed targeting rules help PIWI proteins silence transposons. (Nature 2023)

- DOI: 10.1038/s41586-023-06257-4 | PMCID: PMC10338343 | PMID: 37344600
- Version used: **1.8.1**
- Evidence: The fit was performed using the Trust Region Reflective algorithm implemented in the optimize.curve_fit function from Python module scipy (v.1.8.1) 59 for the maximum number of 10,000 function evaluations before the termination.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.0, SAMtools v1.0.0, STAR v2.3.1] -> quantification [StringTie v1.3.4] -> differential/statistical testing [DESeq2 v1.18.1, scikit-learn] -> stage not stated [SciPy v1.8.1]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Version used: **1.8.0**
- Evidence: Statistical analysis was performed using GraphPad Prism (v.9.4.1) or Python (v.3.10.3) using SciPy (v.1.8.0).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### Gap junctions desynchronize a neural circuit to stabilize insect flight. (Nature 2023)

- DOI: 10.1038/s41586-023-06099-0 | PMCID: PMC10232364 | PMID: 37225999
- Evidence: For additional functions, the Python libraries NumPy, pickle, SciPy, Matplotlib and seaborn were imported.
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, Python, SciPy, seaborn]

### Personalized RNA neoantigen vaccines stimulate T cells in pancreatic cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06063-y | PMCID: PMC10171177 | PMID: 37165196
- Evidence: We computed this as a Fisher’s exact test (implemented from scipy.stats.fisher_exact) using the categorical table supplied in Extended Data Table 2 .
- Full pipeline: alignment/mapping [SAMtools v1.6] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [Scanpy] -> stage not stated [Mutect2 v1.1.7, SciPy, SnpEff v4.3t, Strelka v1.0.15]

### CTCF is a DNA-tension-dependent barrier to cohesin-mediated loop extrusion. (Nature 2023)

- DOI: 10.1038/s41586-023-05961-5 | PMCID: PMC10132984 | PMID: 37076620
- Version used: **1.5.2**
- Evidence: Statistical analysis and reproducibility Statistical analysis was performed using GraphPad Prism (v.9.4.1) or Python (v.3.7.7) using scipy (v.1.5.2) 61 , numpy (v.1.21.6), trackpy (v.0.4.2) 62 and statsmodels (v.0.12.2).
- Full pipeline: differential/statistical testing [NumPy v1.21.6, SciPy v1.5.2, statsmodels v0.12.2]

### The Smc5/6 complex is a DNA loop-extruding motor. (Nature 2023)

- DOI: 10.1038/s41586-023-05963-3 | PMCID: PMC10132971 | PMID: 37076626
- Evidence: 1e and others), the background was subtracted using the 'white_tophat' filter in scipy 33 .
- Full pipeline: visualisation [napari] -> stage not stated [SciPy]

### Extrachromosomal DNA in the cancerous transformation of Barrett's oesophagus. (Nature 2023)

- DOI: 10.1038/s41586-023-05937-5 | PMCID: PMC10132967 | PMID: 37046089
- Version used: **1.9.1**
- Evidence: Statistical analysis We used SciPy v.1.9.1 (ref.
- Full pipeline: alignment/mapping [BWA] -> registration [GATK] -> differential/statistical testing [SciPy v1.9.1] -> stage not stated [Strelka v2.0.15, VEP]

### Adeno-associated virus type 2 in US children with acute severe hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05949-1 | PMCID: PMC10170441 | PMID: 36996871
- Evidence: Statistical analysis Statistical analyses were carried out using the Python scipy package (version 1.5.2) 46 and rstatix package (version 0.7.0) in R (version 4.0.3) 47 .
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R v4.0.3, SciPy] -> visualisation [Jupyter, Matplotlib v3.3.2, Python, seaborn v0.11.0] -> stage not stated [Bowtie2, IQ-TREE v1.6.1]

### Interhemispheric competition during sleep. (Nature 2023)

- DOI: 10.1038/s41586-023-05827-w | PMCID: PMC10097603 | PMID: 36949193
- Version used: **1.6.2**
- Evidence: Statistics Statistical tests were performed using the standard Python package scipy (v.1.6.2).
- Full pipeline: dimensionality reduction/clustering [Kilosort] -> differential/statistical testing [SciPy v1.6.2]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: KDE was calculated with the scipy.stat.gaussian_kde function.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Visualization of translation and protein biogenesis at the ER membrane. (Nature 2023)

- DOI: 10.1038/s41586-022-05638-5 | PMCID: PMC9892003 | PMID: 36697828
- Version used: **1.7.1**
- Evidence: Polysome analysis For the neighbourhood analysis, ribosome positions and orientations were read from the RELION star files resulting from subtomogram alignment in a python script (Python 3.8.11, Numpy 1.20.3, Scipy 1.7.1).
- Full pipeline: alignment/mapping [IMOD v4.10.25, NumPy v1.20.3, Python v3.8.11, RELION v3.1.1, SciPy v1.7.1] -> structure determination [ChimeraX v1.3.0, UCSF Chimera v1.14.0] -> visualisation [ChimeraX v1.3.0] -> stage not stated [AlphaFold]

### Spontaneous behaviour is structured by reinforcement without explicit reward. (Nature 2023)

- DOI: 10.1038/s41586-022-05611-2 | PMCID: PMC9892006 | PMID: 36653449
- Evidence: Peaks in this velocity changepoint score were discovered using SciPy’s findpeaks function with the following parameters: height 1, width 1, prominence 1 so that consecutive data points around each peak were disregarded. dLight time warping To account for variability in syllable duration, dLight traces were time warped for Extended Data Fig.
- Full pipeline: stage not stated [Cellpose, Matplotlib, NumPy, OpenCV, Python, SciPy, TensorFlow, scikit-learn, seaborn]

### An atlas of substrate specificities for the human serine/threonine kinome. (Nature 2023)

- DOI: 10.1038/s41586-022-05575-3 | PMCID: PMC9876800 | PMID: 36631611
- Evidence: The linkage matrix was computed using the SciPy package in Python (v.3.7.6), using the Ward method.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, PyMOL, Python v3.7.6, SciPy]

### γδ T cells are effectors of immunotherapy in cancers with HLA class I defects. (Nature 2023)

- DOI: 10.1038/s41586-022-05593-1 | PMCID: PMC9876799 | PMID: 36631610
- Evidence: ...d with the clinical benefit rate of patients with MMR-d tumours treated with ICB in the DRUP, we used a Fisher’s exact test (using the Python package Scipy 49 (v.1.3.1)) for unadjusted analyses and logistic regression (as implemented by the Python package Statsmodels ( https://pypi.org/project/statsmodels/ ; v.0.10.1) for analyses adjusted for the continuous TMB per Mb and/or the primary site of t...
- Full pipeline: normalisation [ilastik] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R, SciPy, edgeR, limma, statsmodels] -> visualisation [Jupyter, Matplotlib v3.2.1, UMAP, seaborn v0.9.0] -> stage not stated [CellProfiler, NumPy v1.17.2, Seurat v3.1.5, pandas v0.25.1]

### Early Release Science of the exoplanet WASP-39b with JWST NIRISS. (Nature 2023)

- DOI: 10.1038/s41586-022-05674-1 | PMCID: PMC9946829 | PMID: 36623550
- Evidence: 79 )); (2) finds the maximum-likelihood model for the data (an exposure-integrated transit model together with a quadratic trend model using the Nelder–Mead minimization algorithm included in the SciPy package 80 ; (3) removes outliers that deviate from the maximum-likelihood model by more than three times the standard deviation of the normalized residuals; (4) scales the uncertainties by the RMS ...
- Full pipeline: normalisation [SciPy] -> differential/statistical testing [dynesty] -> simulation/modelling [emcee] -> stage not stated [Astropy, PyMC, PyMC3, Python]

### Early Release Science of the exoplanet WASP-39b with JWST NIRSpec PRISM. (Nature 2023)

- DOI: 10.1038/s41586-022-05677-y | PMCID: PMC9946832 | PMID: 36623548
- Evidence: The parameter uncertainties were calculated as the standard deviation of the diagonal of the covariance matrix that was in turn calculated from the Jacobian returned by scipy.optimize.
- Full pipeline: simulation/modelling [emcee] -> stage not stated [SciPy]

### Early Release Science of the exoplanet WASP-39b with JWST NIRSpec G395H. (Nature 2023)

- DOI: 10.1038/s41586-022-05591-3 | PMCID: PMC9946835 | PMID: 36623549
- Evidence: Fitting pipeline 1: ExoTiC-JEDI We fitted the broadband and spectroscopic light curves produced from the ExoTIC-JEDI [V3] stellar spectra using the least-squares optimizer, scipy.optimize lm (ref.
- Full pipeline: simulation/modelling [emcee] -> stage not stated [SciPy, dynesty]

### A DNA methylation atlas of normal human cell types. (Nature 2023)

- DOI: 10.1038/s41586-022-05580-6 | PMCID: PMC9811898 | PMID: 36599988
- Version used: **1.6.3**
- Evidence: The 205 samples were clustered with the unsupervised agglomerative clustering algorithm 23 , using scipy (v.1.6.3) 56 and L1 norm.
- Full pipeline: alignment/mapping [SAMtools v1.9] -> dimensionality reduction/clustering [SciPy v1.6.3] -> differential/statistical testing [HOMER] -> stage not stated [BEDTools v2.26.0, deepTools v3.4.1, scikit-learn]

### Integrated intracellular organization and its variations in human iPS cells. (Nature 2023)

- DOI: 10.1038/s41586-022-05563-7 | PMCID: PMC9834050 | PMID: 36599983
- Evidence: We used the function cluster.hierarchy.linkage of type ‘average’ from the Python package scipy 38 to produce the clustering represented by the dendrogram in Fig.
- Full pipeline: dimensionality reduction/clustering [SciPy, scikit-learn] -> stage not stated [NumPy]

### Inheritance of paternal DNA damage by histone-mediated repair restriction. (Nature 2023)

- DOI: 10.1038/s41586-022-05544-w | PMCID: PMC9834056 | PMID: 36544019
- Evidence: The over-representation of microhomologous deletions sites were calculated with the binomial test function binom_test in Python’s Scipy-v1.5.1 package.
- Full pipeline: alignment/mapping [GATK v4.1.0.0, SAMtools v1.6] -> dimensionality reduction/clustering [GSEA, R v3.6, clusterProfiler v3.14.3] -> differential/statistical testing [Python v3.6, emmeans v1.5.2, statsmodels v0.11.1] -> stage not stated [SciPy]

### Imprinted SARS-CoV-2 humoral immunity induces convergent Omicron RBD evolution. (Nature 2023)

- DOI: 10.1038/s41586-022-05644-7 | PMCID: PMC9931576 | PMID: 36535326
- Evidence: Pairwise dissimilarities of all antibodies in the dataset are calculated using the scipy package (scipy.spatial.distance.jensenshannon, v1.7.0).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [R, ggplot2 v3.3.3, scikit-learn] -> stage not stated [SciPy]

### Recurrent repeat expansions in human cancer genomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05515-1 | PMCID: PMC9812771 | PMID: 36517591
- Evidence: The ‘stats’ module in the Scipy Python package (v1.7.0) was used to conduct the significance test.
- Full pipeline: alignment/mapping [BWA v0.6] -> normalisation [DESeq2 v1.32.0, R v4.0.5] -> differential/statistical testing [Python, statsmodels v0.12.2] -> stage not stated [BEDTools, Enrichr, Matplotlib v3.4, SAMtools v1.13, SciPy]

### Multiple pathways for SARS-CoV-2 resistance to nirmatrelvir. (Nature 2023)

- DOI: 10.1038/s41586-022-05514-2 | PMCID: PMC9849135 | PMID: 36351451
- Evidence: 2c using ‘seaborn.clustermap’ under default settings, which utilizes the UPGMA algorithm through SciPy 51 , 52 .
- Full pipeline: dimensionality reduction/clustering [SciPy, seaborn] -> stage not stated [CellProfiler v4.0.7, Nextflow, Pangolin v4.0.6]

### Identification of carbon dioxide in an exoplanet atmosphere. (Nature 2023)

- DOI: 10.1038/s41586-022-05269-w | PMCID: PMC9946830 | PMID: 36055338
- Evidence: ...://dynesty.readthedocs.io/en/stable/index.html ) and chromatic ( https://zkbt.github.io/chromatic/ ), each of which use the standard Python libraries scipy 98 , numpy 99 , astropy 100 , 101 and matplotlib 102 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: All the analyses and plots have been made on standard Python (v3.8 or higher) and R (v4.0.4) environments, using the third-party libraries mentioned in the Methods; standard data and single-cell experiment data structures; and basic libraries: numpy, scipy, pandas, scikit-learn, statsmodels, python-igraph, seaborn, matplotlib and ggplot2.
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Version used: **1.13.0**
- Evidence: Scanpy v.1.9.1 with anndata v.0.10.7 and the statistics and plotting libraries pandas v.2.2.2, numpy v.1.26.4, scipy v.1.13.0, seaborn v.0.13.2 and matplotlib v.3.8.4 were used for data analysis and visualization.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### An integrated transcriptomic cell atlas of human neural organoids. (Nature 2024)

- DOI: 10.1038/s41586-024-08172-8 | PMCID: PMC11578878 | PMID: 39567792
- Evidence: We used the scipy fcluster method to cluster genes on the basis of their log-fold changes in the two primary datasets.
- Full pipeline: read trimming [UMAP] -> alignment/mapping [RSEM] -> dimensionality reduction/clustering [SciPy, UMAP] -> structure determination [Python] -> machine learning [R] -> stage not stated [AnnData, Jupyter, Scanpy, Singularity, edgeR]

### Central pattern generator control of a vertebrate ultradian sleep rhythm. (Nature 2024)

- DOI: 10.1038/s41586-024-08162-w | PMCID: PMC11655359 | PMID: 39506115
- Evidence: For SWRs, we low-pass filtered (30 Hz) the LFP and detected negative peaks using the function scipy.find_peaks.
- Full pipeline: differential/statistical testing [pandas v2.0.3, xarray v2023.6.0] -> stage not stated [DeepLabCut, NumPy, Python, SciPy]

### A cellular basis for mapping behavioural structure. (Nature 2024)

- DOI: 10.1038/s41586-024-08145-x | PMCID: PMC11655361 | PMID: 39506112
- Version used: **1.10.1**
- Evidence: This used custom-made code but made use of libraries such as numpy (1.22.0), scipy (1.10.1), matplotlib (3.7.3), sciKit learn (1.3.2), pandas (2.0.3) and seaborn (0.13.2).
- Full pipeline: quantification [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DeepLabCut, ImageJ, Kilosort, Matplotlib v3.7.3, NumPy v1.22.0, SciPy v1.10.1, TensorFlow, seaborn v0.13.2]

### Tumour evolution and microenvironment interactions in 2D and 3D space. (Nature 2024)

- DOI: 10.1038/s41586-024-08087-4 | PMCID: PMC11525187 | PMID: 39478210
- Evidence: The Euclidean distance transforms in the CODEX-aligned slide were then calculated for each pixel using Python’s scipy.ndimage.distance_transform_edt.
- Full pipeline: alignment/mapping [SciPy] -> normalisation [clusterProfiler v3.18.1] -> registration [Fiji, ImageJ] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [clusterProfiler v3.18.1] -> visualisation [napari] -> stage not stated [CellChat, Enrichr, GATK v4.1.9.0, GSEA, Picard v2.6.26, Python, SAMtools, Seurat, Strelka v2.9.10, Trim Galore, VarScan v2.3.8, scikit-image]

### Machine-guided design of cell-type-targeting cis-regulatory elements. (Nature 2024)

- DOI: 10.1038/s41586-024-08070-z | PMCID: PMC11525185 | PMID: 39443793
- Evidence: To make calls of contribution blocks in any given sequence, we took the 200 contribution scores and built a smoothed contribution signal using a one-dimensional Gaussian filter (scipy.ndimage.gaussian_filter1d) with a sigma of 1.15.
- Full pipeline: quantification [DESeq2 v1.32.0] -> normalisation [DESeq2 v1.32.0] -> dimensionality reduction/clustering [SciPy] -> differential/statistical testing [DESeq2 v1.32.0] -> machine learning [PyTorch, Python] -> stage not stated [BEDTools v2.30.0, BLAST, HOMER, scikit-learn v1.2.2]

### Long-term lineage commitment in haematopoietic stem cell gene therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08250-x | PMCID: PMC11618100 | PMID: 39442556
- Version used: **1.10.1**
- Evidence: The following packages have been used for Good–Turing and Bayesian regression: R v.4.2.2 (2022-10-31), plyr_1.8.9, tools_4.2.2, jsonlite_1.8.8, grid_4.2.2, tidyselect_1.2.0; Python v.3.8.15, packaged by conda-forge, sklearn v.0.2, joblib v.1.2.0, numpy v.1.24.1, scipy v.1.10.1 and threadpoolctl v.3.1.0.
- Full pipeline: quality control [R] -> alignment/mapping [BWA] -> variant calling [SAMtools] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [NumPy v1.24.1, SciPy v1.10.1, scikit-learn v0.2, tidyverse] -> stage not stated [ggpubr]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Version used: **1.9.3**
- Evidence: The median transformed gene expression was used to compute the Euclidean distance between prenatal skin, adult skin and SkO for each broad cell cluster, using ‘spatial.distance_matrix’ function in SciPy (v.1.9.3), which was then plotted as a heatmap (Extended Data Fig.
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### Spatial proteomics identifies JAKi as treatment for a lethal skin disease. (Nature 2024)

- DOI: 10.1038/s41586-024-08061-0 | PMCID: PMC11602713 | PMID: 39415009
- Evidence: Significant genes were identified by performing one-way-anove using Scipy’s stats package and a P value cut-off of 0.01.
- Full pipeline: normalisation [pheatmap] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [R, SciPy] -> machine learning [Cellpose] -> visualisation [ggplot2] -> stage not stated [Matplotlib, Python, QuPath v0.4.1, scikit-learn]

### One-shot entorhinal maps enable flexible navigation in novel environments. (Nature 2024)

- DOI: 10.1038/s41586-024-08034-3 | PMCID: PMC11602719 | PMID: 39385034
- Evidence: Spectrograms were computed using scipy.signal.spectrogram with nperseg = 1,600 and noverlap = 1,400, corresponding to segments of width 32 m (or 10 laps on the build-up track) with measurements every 4 m (example single-cell spectrograms in Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [DeepLabCut v2.2.0.6] -> stage not stated [Kilosort, Python, SciPy]

### Quasi-periodic X-ray eruptions years after a nearby tidal disruption event. (Nature 2024)

- DOI: 10.1038/s41586-024-08023-6 | PMCID: PMC11499261 | PMID: 39385028
- Evidence: Each peak has been fit separately with a skewed Gaussian function using SciPy.
- Full pipeline: simulation/modelling [emcee] -> stage not stated [SciPy]

### Whole-brain annotation and multi-connectome cell typing of Drosophila. (Nature 2024)

- DOI: 10.1038/s41586-024-07686-5 | PMCID: PMC11446831 | PMID: 39358521
- Evidence: Statistical analyses Unless otherwise stated, statistical analyses (such as Pearson R or cosine distance) were performed using the implementations in the scipy 123 Python package.
- Full pipeline: differential/statistical testing [SciPy] -> stage not stated [Python]

### Connectomic reconstruction predicts visual features used for navigation. (Nature 2024)

- DOI: 10.1038/s41586-024-07967-z | PMCID: PMC11446847 | PMID: 39358517
- Evidence: Using SciPy’s spatial module, we created Delaunay tessellations using a set of FlyWire coordinates to determine whether synapses were contained within the given regions.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Psychtoolbox, SciPy]

### Calcium-permeable AMPA receptors govern PV neuron feature selectivity. (Nature 2024)

- DOI: 10.1038/s41586-024-08027-2 | PMCID: PMC11560848 | PMID: 39358515
- Evidence: This was done using the minimize_scalar method of SciPy 99 with the shift as the optimization parameter.
- Full pipeline: alignment/mapping [STAR] -> quantification [STAR] -> stage not stated [DESeq2, ImageJ, Psychtoolbox, SciPy]

### Future increase in extreme El Niño supported by past glacial changes. (Nature 2024)

- DOI: 10.1038/s41586-024-07984-y | PMCID: PMC11464383 | PMID: 39322673
- Evidence: Code availability Open-sourced Python code was used to create the figures, perform the analyses and all calculations, including the following modules and their required dependencies: matplotlib 78 , pandas 79 , NumPy 80 , seaborn 81 , xarray 82 , cartopy 83 and SciPy 84 .
- Full pipeline: simulation/modelling [CESM v1.2] -> stage not stated [Matplotlib, NumPy, SciPy, seaborn, xarray]

### Advanced CMOS manufacturing of superconducting qubits on 300 mm wafers. (Nature 2024)

- DOI: 10.1038/s41586-024-07941-9 | PMCID: PMC11446867 | PMID: 39294381
- Evidence: The number of TLSs in each slice was counted using the Python scipy.signal.find_peaks() method.
- Full pipeline: stage not stated [SciPy]

### Multi-pass, single-molecule nanopore reading of long protein strands. (Nature 2024)

- DOI: 10.1038/s41586-024-07935-7 | PMCID: PMC11410661 | PMID: 39261738
- Evidence: All figures with raw traces (those shown in pA) had a low-pass Bessel filter applied using SciPy with N = 10 and W n = 0.025, except for those showing stepping analysis (Figs.
- Full pipeline: quantification [ImageJ] -> stage not stated [PyTorch, SciPy, scikit-learn]

### Brain-wide dynamics linking sensation to action during decision-making. (Nature 2024)

- DOI: 10.1038/s41586-024-07908-w | PMCID: PMC11499283 | PMID: 39261727
- Evidence: The outlier detection model was implemented using custom Python software using the NumPy, SciPy, and PyTorch libraries.
- Full pipeline: machine learning [DeepLabCut] -> stage not stated [Kilosort v2.0, NumPy, PyTorch, SciPy]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **1.10.1**
- Evidence: ...aph). scRNA-sequencing Analysis and visualization of the data were conducted in a Python environment built on Pandas (v.2.0.1), NumPy (v.1.24.2) 73 , SciPy (v.1.10.1) 74 , scikit-learn (v.1.2.0), SCANPY (v1.9.3) 75 , AnnData (v.0.9.1) 75 , matplotlib (v.3.7.1) 76 and seaborn (v.0.13.1) 77 packages.
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Evidence: The mean cumulative k -mer counts were fitted to a logarithmic function ( y = a + b × log( x )] using the Python function optimize.curve_fit from SciPy library (v1.8.0) 77 .
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### De novo design of allosterically switchable protein assemblies. (Nature 2024)

- DOI: 10.1038/s41586-024-07813-2 | PMCID: PMC11338832 | PMID: 39143214
- Evidence: F P s i g n a l = m a x i m u m s i g n a l ( V m ) × [ r i n g m o n o m e r c o n c e n t r a t i o n ) n K d n + [ r i n g m o n o m e r c o n c e n t r a t i o n ] n + b a s e l i n e where b , V m , n and K d are fit by nonlinear regression to a set of polarization signal and protein concentration values using the optimize_curvefit function within SciPy.
- Full pipeline: differential/statistical testing [SciPy] -> structure determination [PHENIX] -> visualisation [ChimeraX, Python] -> stage not stated [PyMOL, UCSF Chimera]

### The ribosome lowers the entropic penalty of protein folding. (Nature 2024)

- DOI: 10.1038/s41586-024-07784-4 | PMCID: PMC11374706 | PMID: 39112704
- Evidence: S2 ln K eq = − Δ H R 1 T + Δ S R The Scipy package with optimize.curve_fit function was used to perform the fits 74 and errors were estimated as one s.d. from the diagonal elements of the parameter covariance matrix.
- Full pipeline: simulation/modelling [GROMACS, PyMOL v2.3] -> structure determination [Python] -> stage not stated [ImageJ, MDAnalysis, MDTraj, SciPy]

### Molecular mimicry in multisystem inflammatory syndrome in children. (Nature 2024)

- DOI: 10.1038/s41586-024-07722-4 | PMCID: PMC11324515 | PMID: 39112696
- Evidence: Statistical methods All statistical analysis was performed in Python using the Scipy Stats package unless otherwise indicated.
- Full pipeline: differential/statistical testing [Python, SciPy, scikit-learn, tidyverse v1.1.4] -> machine learning [scikit-learn] -> stage not stated [Scanpy v1.10.0, Seurat, igraph v2.0.3]

### FANCD2-FANCI surveys DNA and recognizes double- to single-stranded junctions. (Nature 2024)

- DOI: 10.1038/s41586-024-07770-w | PMCID: PMC11358013 | PMID: 39085614
- Version used: **1.11.3**
- Evidence: Single-molecule data interpretation Raw data exported from LUMICKS Bluelake as .h5 files were processed with custom-written Jupyter Notebooks in Python 3.9 using LUMICKS Pylake v.1.2.1, numpy v.1.26.0, matplotlib v.3.7.2, scipy v.1.11.3 and peakutils v.1.3.4 ( https://github.com/singlemoleculegroup ).
- Full pipeline: differential/statistical testing [R] -> structure determination [ChimeraX, Coot, PHENIX] -> stage not stated [Jupyter, Matplotlib v3.7.2, NumPy v1.26.0, Python v3.9, RELION v4.0, SciPy v1.11.3]

### Multiscale topology classifies cells in subcellular spatial transcriptomics. (Nature 2024)

- DOI: 10.1038/s41586-024-07563-1 | PMCID: PMC11208150 | PMID: 38898271
- Evidence: We draw a Voronoi diagram (computed using the implementation in SciPy 39 based on Qhull 40 ) on the basis of these points to simulate cell boundaries.
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [SciPy] -> visualisation [UMAP] -> stage not stated [MACS2]

### The mechanism for directional hearing in fish. (Nature 2024)

- DOI: 10.1038/s41586-024-07507-9 | PMCID: PMC11222163 | PMID: 38898274
- Evidence: This was implemented by solving the system of equations with a least-square solver (scipy.optimize.lsq_linear) with bounds \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$-{B}_{i,l} < {S}_{i,l} < {B}_{i,l}$$\end{docume...
- Full pipeline: stage not stated [ImageJ v1.5, Python, SLEAP, SciPy]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Version used: **1.7.1**
- Evidence: To compute inter-nuclear distance, for each nucleus in a tile represented by its x – y centroid coordinates, nearest neighbours were identified using the k -dimensional tree function from the spatial module of SciPy (v1.7.1) 91 .
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Evidence: Linear regressions were computed using the SciPy stats package.
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### Descending networks transform command signals into population motor control. (Nature 2024)

- DOI: 10.1038/s41586-024-07523-9 | PMCID: PMC11186778 | PMID: 38839968
- Evidence: We used two-sided Mann–Whitney U- tests (scipy.stats.mannwhitneyu 74 ) to statistically analyse these comparisons.
- Full pipeline: differential/statistical testing [NumPy, SciPy] -> stage not stated [NetworkX, SLEAP v1.3.0]

### Structure and topography of the synaptic V-ATPase-synaptophysin complex. (Nature 2024)

- DOI: 10.1038/s41586-024-07610-x | PMCID: PMC11269182 | PMID: 38838737
- Evidence: All calculations were performed using the SciPy module from Python (v3.8).
- Full pipeline: alignment/mapping [IMOD, RELION] -> structure determination [AlphaFold, PHENIX v1.21] -> machine learning [RELION, Topaz] -> visualisation [PyMOL] -> stage not stated [ChimeraX, Coot, Python, SciPy, UCSF Chimera]

### Unlocking bacterial potential to reduce farmland N&lt;sub&gt;2&lt;/sub&gt;O emissions. (Nature 2024)

- DOI: 10.1038/s41586-024-07464-3 | PMCID: PMC11168931 | PMID: 38811724
- Version used: **1.11.2**
- Evidence: The Fieller and bootstrap confidence intervals were calculated using Python (v3.11.5) 77 with Scipy (v1.11.2) 78 and Pandas (v2.1.1) 79 , and Julia (v1.9.3) 80 .
- Full pipeline: stage not stated [SciPy v1.11.2]

### Molecular mechanism of choline and ethanolamine transport in humans. (Nature 2024)

- DOI: 10.1038/s41586-024-07444-7 | PMCID: PMC11168923 | PMID: 38778100
- Evidence: Recorded F 350 / F 330 was analysed by using Python libraries including pandas, numpy, scipy and seaborn in Visual Studio Code (Microsoft).
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [RELION v3.1] -> differential/statistical testing [RELION v3.1] -> simulation/modelling [GROMACS v2022.4, MDAnalysis, PyMOL] -> structure determination [AlphaFold, ChimeraX v1.5, Coot v0.8, PHENIX, RELION v3.1] -> visualisation [MDAnalysis] -> stage not stated [CTFFIND, MotionCor2, NumPy, SciPy, seaborn]

### Life-cycle-coupled evolution of mitosis in close relatives of animals. (Nature 2024)

- DOI: 10.1038/s41586-024-07430-z | PMCID: PMC11153136 | PMID: 38778110
- Evidence: The tracing of bundles and twist calculations were previously written in Python programming language using PyCharm IDE, with external libraries such as NumPy, scikit-image, Matplotlib, PIL, OpenCV and SciPy.
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [HMMER v3.3.2, ImageJ, Matplotlib, NumPy, OpenCV, Python, SciPy, scikit-image]

### A warm Neptune's methane reveals core mass and vigorous atmospheric mixing. (Nature 2024)

- DOI: 10.1038/s41586-024-07395-z | PMCID: PMC11208151 | PMID: 38768633
- Evidence: Moreover, these codes made use ExoTiC-LD 117 ( https://exotic-ld.readthedocs.io/en/latest/ ) and Emcee ( https://emcee.readthedocs.io/en/stable/ ) 118 , which use the Python libraries scipy 119 , numpy 120 , astropy 121 and matplotlib 122 .
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty, emcee]

### The intrinsic substrate specificity of the human tyrosine kinome. (Nature 2024)

- DOI: 10.1038/s41586-024-07407-y | PMCID: PMC11136658 | PMID: 38720073
- Evidence: Linkage matrices were computed using the SciPy package in Python (v.3.7.6), using the ‘ward’ method.
- Full pipeline: visualisation [ggplot2] -> stage not stated [AlphaFold, ChimeraX, Python v3.7.6, SciPy]

### Accurate structure prediction of biomolecular interactions with AlphaFold 3. (Nature 2024)

- DOI: 10.1038/s41586-024-07487-w | PMCID: PMC11168924 | PMID: 38718835
- Version used: **1.9.3**
- Evidence: Model performance analysis and visualization Data analysis used Python v.3.11.7 ( https://www.python.org/ ), NumPy v.1.26.3 ( https://github.com/numpy/numpy ), SciPy v.1.9.3 ( https://www.scipy.org/ ), seaborn v.0.12.2 ( https://github.com/mwaskom/seaborn ), Matplotlib v.3.6.1 ( https://github.com/matplotlib/matplotlib ), pandas v.2.0.3 ( https://github.com/pandas-dev/pandas ), statsmodels v.0.12....
- Full pipeline: visualisation [NumPy v1.26.3, SciPy v1.9.3, seaborn v0.12.2] -> stage not stated [AlphaFold, Matplotlib v3.6.1, RDKit, RoseTTAFold, statsmodels v0.12.2]

### Geographic variation of mutagenic exposures in kidney cancer genomes. (Nature 2024)

- DOI: 10.1038/s41586-024-07368-2 | PMCID: PMC11111402 | PMID: 38693263
- Evidence: Handling of geospatial and other data was conducted using the R packages lme4, matrixStats, Matrix, geojsonio, raster, rgeos, sf, sp, tmaptools, patchwork, leaflet, data.table, dplyr, haven, Hmisc, openxlsx, rgdal, scales, stringr, tidyr, tibble, xlsx, rfPermute, randomForest, forcats, and in python using the packages pandas, numpy, scipy, statsmodels, firthlogist, patsy and jupyter 68 – 97 .
- Full pipeline: quality control [PLINK v1.9b] -> variant calling [PLINK v1.9b] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE, PLINK v1.9b] -> structure determination [R] -> visualisation [Matplotlib, ggpubr, seaborn] -> stage not stated [NumPy, SciPy, data.table, lme4, statsmodels, tidyverse]

### Sleep pressure modulates single-neuron synapse number in zebrafish. (Nature 2024)

- DOI: 10.1038/s41586-024-07367-3 | PMCID: PMC11096099 | PMID: 38693264
- Version used: **1.11.4**
- Evidence: To estimate the size of the puncta, the normalized grey values were interpolated with a cubic polynomial implemented by the SciPy (v.1.11.4) function scipy.interpolate.interp1d before finding the full width at half maximum.
- Full pipeline: normalisation [SciPy v1.11.4] -> stage not stated [ImageJ, Python]

### Discovery of WRN inhibitor HRO761 with synthetic lethality in MSI cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07350-y | PMCID: PMC11078746 | PMID: 38658754
- Evidence: Owing to the heterogenous protein levels across the three sensitive cell lines, paired t -tests (as implemented in the Python Scipy package) were used to calculate significant differences between DMSO-treated versus compound- 4 -treated cells.
- Full pipeline: normalisation [R, fgsea] -> differential/statistical testing [DESeq2, R, fgsea] -> stage not stated [GSEA, PHENIX, SciPy]

### Single-cell analysis reveals context-dependent, cell-level selection of mtDNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07332-0 | PMCID: PMC11078733 | PMID: 38658765
- Version used: **1.7.0**
- Evidence: The analyses were performed using Python v3.7.12, with the following modules: matplotlib v3.4.2, numpy v1.21.0, pandas v1.1.5, plotly v5.16.1, pysam v0.16.0.1, scikit-learn v0.23.1, scipy v1.7.0 and seaborn v0.11.1.
- Full pipeline: quality control [MultiQC v1.11] -> stage not stated [Matplotlib v3.4.2, NumPy v1.21.0, R, SciPy v1.7.0, scikit-learn v0.23.1, seaborn v0.11.1]

### Network-level encoding of local neurotransmitters in cortical astrocytes. (Nature 2024)

- DOI: 10.1038/s41586-024-07311-5 | PMCID: PMC11062919 | PMID: 38632406
- Version used: **1.6.2**
- Evidence: 4h —were correlated, we computed the Spearman ρ between the binary paired responses to GABA and glutamate across cells that could be assessed in both conditions (that is, had >0 propagating baseline Ca 2+ events in both recordings) using SciPy 1.6.2 (ref.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [statsmodels v0.12.2] -> stage not stated [SciPy v1.6.2]

### Immune microniches shape intestinal T&lt;sub&gt;reg&lt;/sub&gt; function. (Nature 2024)

- DOI: 10.1038/s41586-024-07251-0 | PMCID: PMC11041794 | PMID: 38570678
- Evidence: Statistical significance was obtained by chi-square analysis (scipy.stats.chi2_contingency) and the P value was corrected with the Benjamini–Hochberg method.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> visualisation [R] -> stage not stated [CellPhoneDB, NumPy v1.20.1, SoupX, pandas v1.2.3, scDblFinder, scVelo v0.2.4, velocyto]

### A figure of merit for efficiency roll-off in TADF-based organic LEDs. (Nature 2024)

- DOI: 10.1038/s41586-024-07149-x | PMCID: PMC10972759 | PMID: 38538942
- Evidence: J 90 was obtained by minimizing equation (18) using the python package scipy 162 .
- Full pipeline: stage not stated [SciPy]

### Neural and behavioural state switching during hippocampal dentate spikes. (Nature 2024)

- DOI: 10.1038/s41586-024-07192-8 | PMCID: PMC11023929 | PMID: 38480889
- Evidence: To arrange units and DS2 events on the basis of similarity of their activity pattern, agglomerative hierarchical clustering algorithm with a Euclidean distance metric and the Ward variance minimization linkage method was implemented using Scipy Python package ( https://scipy.org/ ).
- Full pipeline: dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [Python] -> machine learning [DeepLabCut] -> stage not stated [Kilosort, NetworkX]

### The Dimorphos ejecta plume properties revealed by LICIACube. (Nature 2024)

- DOI: 10.1038/s41586-023-06998-2 | PMCID: PMC10954540 | PMID: 38418881
- Evidence: The optimize.roots routine of the python library scipy 19 , which can be initiated with guesses of the cone axis and of the aperture angle 2 α , is used for solving this system of nonlinear equations.
- Full pipeline: stage not stated [SciPy]

### Incomplete transcripts dominate the Mycobacterium tuberculosis transcriptome. (Nature 2024)

- DOI: 10.1038/s41586-024-07105-9 | PMCID: PMC10937400 | PMID: 38418874
- Version used: **1.10.1**
- Evidence: Data analysis and visualization scripts used Python packages including Matplotlib (v3.7.1), Numpy (v1.24.3), Scipy (v1.10.1), bioinfokit (v0.3), and pyCircos (v0.3.0).
- Full pipeline: alignment/mapping [Bowtie2 v2.5.1, SAMtools v1.17] -> visualisation [Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1] -> stage not stated [Cutadapt v4.1, Python]

### Influence of pump laser fluence on ultrafast myoglobin structural dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07032-9 | PMCID: PMC10881388 | PMID: 38355794
- Evidence: Structures were analysed using COOT 65 , 66 , PYMOL 67 and custom-written python scripts using NumPy 68 and SciPy 69 .
- Full pipeline: normalisation [CCP4] -> structure determination [CCP4] -> stage not stated [NumPy, SciPy]

### Converting an allocentric goal into an egocentric steering signal. (Nature 2024)

- DOI: 10.1038/s41586-023-07006-3 | PMCID: PMC10881393 | PMID: 38326612
- Evidence: 3f,g , rapid changes in the FC2 phase position were detected by finding peaks in the filtered phase velocity (500-ms boxcar filter) using the SciPy 65 function signal.find_peaks.
- Full pipeline: stage not stated [CaImAn, Python, SciPy]

### A dynamical measure of the black hole mass in a quasar 11 billion years ago. (Nature 2024)

- DOI: 10.1038/s41586-024-07053-4 | PMCID: PMC11636685 | PMID: 38286342
- Evidence: GILDAS is publicly available on the IRAM webpage ( https://www.iram.fr/IRAMFR/GILDAS/ ). astropy, matplotlib, emcee, dynesty, numpy and scipy are all available through the Python Package Index ( https://pypi.org ).
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, SciPy, dynesty]

### Affinity-optimizing enhancer variants disrupt development. (Nature 2024)

- DOI: 10.1038/s41586-023-06922-8 | PMCID: PMC10830414 | PMID: 38233525
- Evidence: MPRA data were analysed using standard Python libraries (pandas, numpy, scipy, seaborn, matplotlib).
- Full pipeline: differential/statistical testing [R] -> stage not stated [Matplotlib, NumPy, SciPy, seaborn]

### Alternative splicing of latrophilin-3 controls synapse formation. (Nature 2024)

- DOI: 10.1038/s41586-023-06913-9 | PMCID: PMC10830413 | PMID: 38233523
- Version used: **1.10.1**
- Evidence: SciPy (v1.10.1) 47 algorithm “find_peaks” (height=0.15, width = (2,20), distance=20) was used to detect the spiking number and signal strength (Δ F / F ) for each synchronized firing trace.
- Full pipeline: alignment/mapping [STAR] -> quantification [scikit-image v0.20.0] -> stage not stated [CaImAn, DESeq2, HOMER, HTSeq, SciPy v1.10.1]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Evidence: Clustering was performed using the linkage function from the Python package scipy.cluster.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### Cell-type-directed design of synthetic enhancers. (Nature 2024)

- DOI: 10.1038/s41586-023-06936-2 | PMCID: PMC10830415 | PMID: 38086419
- Version used: **1.6.0**
- Evidence: Statistics and reproducibility Statistics were calculated using Scipy (v.1.6.0; RRID: SCR_008058 ) 60 .
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore] -> dimensionality reduction/clustering [BEDTools v2.30.0] -> differential/statistical testing [SciPy v1.6.0] -> machine learning [NumPy v1.19.5] -> visualisation [Matplotlib v3.1.1] -> stage not stated [MACS2 v2.1.2.1, deepTools]

### Repeated Omicron exposures override ancestral SARS-CoV-2 immune imprinting. (Nature 2024)

- DOI: 10.1038/s41586-023-06753-7 | PMCID: PMC10764275 | PMID: 37993710
- Evidence: Pair-wise dissimilarities of all antibodies in the dataset are calculated using the SciPy module (scipy.spatial.distance.jensenshannon, v1.7.0).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [R, UMAP, ggplot2 v3.3.3] -> stage not stated [SciPy, igraph]

### Predicting multiple conformations via sequence clustering and AlphaFold2. (Nature 2024)

- DOI: 10.1038/s41586-023-06832-9 | PMCID: PMC10808063 | PMID: 37956700
- Evidence: Spearman correlations and t -tests were performed using Scipy 90 .
- Full pipeline: read trimming [RAxML v8.2.9] -> alignment/mapping [AlphaFold, MAFFT, RAxML v8.2.9] -> dimensionality reduction/clustering [scikit-learn] -> stage not stated [BLAST v2.6.0, ColabFold, IQ-TREE, PyMOL, SciPy]

### Conservation and alteration of mammalian striatal interneurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09592-w | PMCID: PMC12589139 | PMID: 41193841
- Version used: **1.11.2**
- Evidence: To annotate HMBA cells that did not integrate with the homologous types, we found k = 10 nearest neighbours on the scVI latent space, and clustered using scanpy leiden (flavor = “igraph”, resolution = 1, n_iterations = 2), and we calculated the ‘experiment’ entropy for each cluster (scipy.stats.entropy; scipy v.1.11.2).
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [Scanpy, SciPy v1.11.2, Seurat, UMAP, igraph] -> simulation/modelling [AnnData, R, Slingshot] -> stage not stated [BLAST v2.9.0, scDblFinder v0.2.3]

### The astrocytic ensemble acts as a multiday trace to stabilize memory. (Nature 2025)

- DOI: 10.1038/s41586-025-09619-2 | PMCID: PMC12675280 | PMID: 41094146
- Evidence: Astrocytic RCaMP3 signals were bandpass filtered between 0.0003 and 1 Hz with SciPy 85 (v.1.11.4).
- Full pipeline: alignment/mapping [ANTs] -> normalisation [ANTs] -> dimensionality reduction/clustering [Seurat] -> visualisation [Matplotlib] -> stage not stated [ImageJ, Jupyter, NumPy, Python v3.0.0, SciPy, pandas v2.1.4, scikit-learn v1.2.2, tidyverse]

### Efficient and accurate search in petabase-scale sequence repositories. (Nature 2025)

- DOI: 10.1038/s41586-025-09603-w | PMCID: PMC12657231 | PMID: 41062695
- Evidence: All P values are corrected using the Benjamini–Yekutieli procedure to a family-wise error rate of 0.05 and are considered to be significant if they are P < 0.05 after correction (using the Python scipy package v.1.11.3).
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.0] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [Docker, Python, R v71.2, Snakemake]

### Hotspots of human mutation point to clonal expansions in spermatogonia. (Nature 2025)

- DOI: 10.1038/s41586-025-09579-7 | PMCID: PMC12714578 | PMID: 41062699
- Evidence: The β i μ coefficients were determined by the synonymous SFS and β i s coefficients were fit with maximum likelihood using the L-BFGS-B algorithm as implemented in scipy.
- Full pipeline: stage not stated [SciPy]

### Arousal as a universal embedding for spatiotemporal brain dynamics. (Nature 2025)

- DOI: 10.1038/s41586-025-09544-4 | PMCID: PMC12611781 | PMID: 40993399
- Evidence: Specifically, we downsampled and low passed the signals with a 100-Hz cutoff, computed the spectrogram (scipy.signal.spectrogram 82 ) at each channel in sliding windows of 0.5 s with 80% overlap, and averaged spectrograms across all channels falling within ‘VIS’ regions (including primary and secondary visual cortical areas).
- Full pipeline: stage not stated [DeepLabCut, SciPy, scikit-learn]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Version used: **1.6.3**
- Evidence: Pearson and Spearman correlation coefficients and the corresponding P values were calculated using scipy v1.6.3.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### A prudent planetary limit for geologic carbon storage. (Nature 2025)

- DOI: 10.1038/s41586-025-09423-y | PMCID: PMC12408384 | PMID: 40903604
- Evidence: We estimate carbon-storage needs in a given scenario after its time horizon by using a first-order spline interpolation extrapolating beyond the model horizon until 2300 (so-called slinear interpolation in the Python library scipy).
- Full pipeline: stage not stated [SciPy]

### Divergent evolutionary strategies pre-empt tissue collision in gastrulation. (Nature 2025)

- DOI: 10.1038/s41586-025-09447-4 | PMCID: PMC12527943 | PMID: 40903584
- Evidence: Quantitative data were analysed and processed using Excel, or custom-made ImageJ or FIJI macros and Python scripts using Numpy, Pandas and SciPy libraries.
- Full pipeline: alignment/mapping [MUSCLE] -> stage not stated [ImageJ, Matplotlib, NumPy, Python, SciPy, seaborn]

### Seismic detection of a 600-km solid inner core in Mars. (Nature 2025)

- DOI: 10.1038/s41586-025-09361-9 | PMCID: PMC12408336 | PMID: 40903600
- Evidence: Figures were created using matplotlib 73 , seismic data processing was done in ObsPy 74 , and inversions were done in NumPy and SciPy (refs.
- Full pipeline: visualisation [Matplotlib, NumPy, SciPy]

### Global phenology maps reveal the drivers and effects of seasonal asynchrony. (Nature 2025)

- DOI: 10.1038/s41586-025-09410-3 | PMCID: PMC12408380 | PMID: 40866701
- Evidence: Methods Overview of software, data and workflow We conducted our LSP mapping workflow using Google Earth Engine (GEE) (v.0.1.404 or later) 65 and performed additional analyses using Python 66 with a set of core scientific packages (numpy 67 , shapely 68 , pandas 69 , geopandas 70 , rasterio 71 , xarray 72 , rasterstats 73 , dask 74 , scipy 75 , scikit-learn 76 , statsmodels 77 and matplotlib 78 ).
- Full pipeline: alignment/mapping [Clustal Omega v2.1, Dask, Matplotlib, NumPy, Python, SciPy, scikit-learn, statsmodels, xarray] -> stage not stated [GDAL v2.2.3, R, TensorFlow]

### Clone copy number diversity is linked to survival in lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09398-w | PMCID: PMC12488491 | PMID: 40804524
- Version used: **1.10.1**
- Evidence: Statistical information Statistical tests were performed using either R or Python (scipy v1.10.1).
- Full pipeline: dimensionality reduction/clustering [R] -> differential/statistical testing [SciPy v1.10.1]

### One-third of Sun-like stars are born with misaligned planet-forming disks. (Nature 2025)

- DOI: 10.1038/s41586-025-09324-0 | PMCID: PMC12350154 | PMID: 40770103
- Evidence: 97 ), Lightkurve 68 , Astropy 102 , NumPy 103 , SciPy 104 and Matplotlib 105 .
- Full pipeline: simulation/modelling [emcee] -> stage not stated [Astropy, Matplotlib, NumPy, Python, SciPy]

### A generic non-invasive neuromotor interface for human-computer interaction. (Nature 2025)

- DOI: 10.1038/s41586-025-09255-w | PMCID: PMC12443603 | PMID: 40702190
- Evidence: Spikes were detected by peak finding on the sEMG envelope using scipy.signal.find_peaks with prominence=0.5 (ref.
- Full pipeline: stage not stated [SciPy]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: Nonparametric independent Wilcoxon rank-sum testing was performed using the ranksum function of scipy 101 with Benjamini–Hochberg correction.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Selective remodelling of the adipose niche in obesity and weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-09233-2 | PMCID: PMC12367556 | PMID: 40634602
- Evidence: This was achieved using the KDTree function from Scipy’s spatial module.
- Full pipeline: variant calling [IMPUTE2 v2.3.2, SHAPEIT, scDblFinder] -> normalisation [AnnData] -> dimensionality reduction/clustering [AnnData, Scanpy, UMAP, scDblFinder] -> stage not stated [CellChat, ImageJ, QuPath v0.5.1, SCENIC, SciPy, Seurat]

### Evidence for a sub-Jovian planet in the young TWA 7 disk. (Nature 2025)

- DOI: 10.1038/s41586-025-09150-4 | PMCID: PMC12221965 | PMID: 40562924
- Evidence: We used various functions of the following software packages to perform the analysis and create the figures: numpy, astropy, scipy, matplotlib and photutils.
- Full pipeline: stage not stated [Astropy, Matplotlib, NumPy, SciPy]

### The dynamics and geometry of choice in the premotor cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-09199-1 | PMCID: PMC12408350 | PMID: 40562938
- Evidence: For the scalar parameters D and all { C i }, we combined ADAM updates with line searches using the L-BFGS-B algorithm (L-BFGS-B method from the scipy.optimize.minimize toolbox).
- Full pipeline: stage not stated [Brian2, Psychtoolbox v3.0.9, SciPy]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Evidence: The image was rotated using Scipy 68 (v1.7.3) ndi.rotate function.
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Unsupervised pretraining in biological neural networks. (Nature 2025)

- DOI: 10.1038/s41586-025-09180-y | PMCID: PMC12367527 | PMID: 40533561
- Evidence: 8e , the running speed was interpolated to the timepoints of the imaging frames using the function scipy.interpolate.interp1d.
- Full pipeline: visualisation [Matplotlib] -> stage not stated [NumPy, Python, SciPy, Suite2p, scikit-learn]

### Discovery of FoTO1 and Taxol genes enables biosynthesis of baccatin III. (Nature 2025)

- DOI: 10.1038/s41586-025-09090-z | PMCID: PMC12240809 | PMID: 40500440
- Evidence: To identify substructures, genes were hierarchically clustered (SciPy fcluster, Euclidean distance) on both axes. c , Schematic for matrix factorization. mpXsn data were factorized using cNMF 28 . d , Heat map showing the rank of known Taxol biosynthetic genes in each of the modules produced by matrix factorization. e , As in d , but showing only the three modules enriched in Taxol genes (modules ...
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [AlphaFold, Clustal Omega, Trimmomatic] -> dimensionality reduction/clustering [SciPy, UMAP] -> stage not stated [HMMER, NumPy, Scanpy v1.10.1]

### Probing condensate microenvironments with a micropeptide killswitch. (Nature 2025)

- DOI: 10.1038/s41586-025-09141-5 | PMCID: PMC12286862 | PMID: 40468084
- Evidence: Correlation plots were calculated using the SciPy package 77 in Python v.3.10 and plotted with Seaborn (Extended Data Fig.
- Full pipeline: read trimming [Trim Galore v0.6.10] -> alignment/mapping [STAR] -> visualisation [ChimeraX v1.6, Python v3.10, R, SciPy, ggplot2, pheatmap, seaborn] -> stage not stated [AlphaFold, Cellpose, ImageJ v2.14.0]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Version used: **1.10.1**
- Evidence: Python packages such as Scanpy (v.1.9.5), Pandas (v.2.0.0), Statsmodels (v.0.14.0), NumPy (v.1.24.2), Scipy (v.1.10.1), Matplotlib (v.3.8.0), Seaborn (v.0.11.2) and Sklearn (v.1.3.2), were used for data analysis.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Visualizing dynamics of charges and strings in (2 + 1)D lattice gauge theories. (Nature 2025)

- DOI: 10.1038/s41586-025-08999-9 | PMCID: PMC12158766 | PMID: 40468064
- Evidence: For this, we use the default settings of the function scipy.optimize.minimize_scalar from the Python library SciPy 72 , which implements Brent’s algorithm 73 .
- Full pipeline: stage not stated [SciPy]

### Molecular gradients shape synaptic specificity of a visuomotor transformation. (Nature 2025)

- DOI: 10.1038/s41586-025-09037-4 | PMCID: PMC12350164 | PMID: 40468081
- Version used: **1.13.0**
- Evidence: Analysis and plotting were conducted with custom scripts in MATLAB 2022b, and Scipy 1.13.0 and Seaborn 0.13.2 in Python 3.
- Full pipeline: quantification [SAMtools] -> differential/statistical testing [R, emmeans] -> stage not stated [Psychtoolbox, Python, SciPy v1.13.0, Seurat, ggplot2, lme4, seaborn v0.13.2]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: Visualization was performed using a combination of Matplotlib 70 , SciPy 71 and NumPy 72 , and expression values are shown in heat maps as log 2 TPM to represent log fold change.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Unravelling cysteine-deficiency-associated rapid weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-08996-y | PMCID: PMC12267064 | PMID: 40399674
- Version used: **1.1.0**
- Evidence: The resulting blank corrected data matrix was then used for all group-wise comparisons, and t -tests were performed using the Python SciPy (v.1.1.0) 72 library to test for differences and to generate statistics for downstream analyses.
- Full pipeline: normalisation [pheatmap] -> differential/statistical testing [DESeq2 v1.48, SciPy v1.1.0] -> visualisation [DESeq2 v1.48] -> stage not stated [HTSeq, Python, R]

### Dopaminergic action prediction errors serve as a value-free teaching signal. (Nature 2025)

- DOI: 10.1038/s41586-025-09008-9 | PMCID: PMC12310545 | PMID: 40369067
- Evidence: Parameters were fitted using the scipy package in Python (optimize.minimize function).
- Full pipeline: quantification [DeepLabCut] -> differential/statistical testing [Python, scikit-learn, statsmodels] -> stage not stated [SciPy, pingouin]

### Light-microscopy-based connectomic reconstruction of mammalian brain tissue. (Nature 2025)

- DOI: 10.1038/s41586-025-08985-1 | PMCID: PMC12158774 | PMID: 40335689
- Evidence: We then applied background subtraction by applying Gaussian filters of two different widths using scipy.ndimage.gaussian_filter, with σ = 5 voxels and σ = 11 voxels, corresponding to signal and background, respectively, for bassoon ( σ = 6 voxels and σ = 10 voxels for datasets with 200-nm z -step size) and σ = 4 voxels and σ = 11 voxels ( σ = 6 voxels and σ = 12 voxels for datasets with 200-nm and...
- Full pipeline: machine learning [PyTorch v1.12.1] -> stage not stated [BigStitcher, Jupyter, NumPy, Python v3.8, SciPy, scikit-image, seaborn]

### Adversarial testing of global neuronal workspace and integrated information theories of consciousness. (Nature 2025)

- DOI: 10.1038/s41586-025-08888-1 | PMCID: PMC12137136 | PMID: 40307561
- Version used: **1.8.0**
- Evidence: Analysis-specific functional preprocessing Additional, analysis-specific, fMRI data preprocessing was performed using FSL 6.0.2 (FMRIB Software Library) 94 , Statistical Parametric Mapping (SPM 12) software 95 , and custom Python scripts (using NiBabel (3.2.2) 96 and SciPy (1.8.0) 97 after the above-outlined general preprocessing.
- Full pipeline: quality control [MRIQC v0.16.1] -> alignment/mapping [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> differential/statistical testing [FSL v6.0.2, NiBabel v3.2.2, SPM, SciPy v1.8.0] -> machine learning [scikit-learn] -> stage not stated [FreeSurfer, MNE-Python v0.24, Matplotlib v3.3.2, Nipype v1.6.1, NumPy v1.19.2, Psychtoolbox, Python v0.24, dcm2niix, fMRIPrep v20.2.3]

### A distributed coding logic for thermosensation and inflammatory pain. (Nature 2025)

- DOI: 10.1038/s41586-025-08875-6 | PMCID: PMC12222022 | PMID: 40269164
- Version used: **1.5.2**
- Evidence: All quantification and statistical analyses were performed using Python v.3.8, Pandas v.1.1.3, Numpy v.1.19.2 and Scipy v.1.5.2.
- Full pipeline: quantification [NumPy v1.19.2, SciPy v1.5.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.19.2, SciPy v1.5.2] -> stage not stated [ImageJ, OpenCV, Python, Seurat, scDblFinder]

### Functional connectomics spanning multiple areas of mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08790-w | PMCID: PMC11981939 | PMID: 40205214
- Evidence: Next, we applied the minimum weight matching algorithm for bipartite graphs 89 using the linear_sum_assignment function from the scipy.optimize module 90 to perform the matching.
- Full pipeline: machine learning [CaImAn] -> visualisation [Matplotlib, NumPy] -> stage not stated [Python, SciPy]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Evidence: Next, we identified all pairs of vertices from the two skeletons that were within 5 μm of each other by performing spatial queries using the KDTree query_ball_tree method from the scipy.spatial module in SciPy 55 .
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### DNA-guided transcription factor interactions extend human gene regulatory code. (Nature 2025)

- DOI: 10.1038/s41586-025-08844-z | PMCID: PMC12119339 | PMID: 40205063
- Evidence: For statistical testing, the binomtest one-sided function from SciPy library v.1.10.0 was used.
- Full pipeline: differential/statistical testing [Bioconductor, ComplexHeatmap, Python, R, SciPy] -> structure determination [CCP4, PHENIX] -> machine learning [R] -> visualisation [Bioconductor, ComplexHeatmap] -> stage not stated [AlphaFold v2.0, BEDTools v2.30.0, Cytoscape, PyMOL, RoseTTAFold]

### Connectomics of predicted Sst transcriptomic types in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08805-6 | PMCID: PMC11981948 | PMID: 40205210
- Evidence: We used the following libraries for visualization and analysis: Matplotlib 73 , Seaborn 74 , Numpy 75 , Pandas 76 , VTK 77 , Scipy 78 , Scikit-posthocs 79 , Scikit-learn 80 , scrattch-hicat ( https://github.com/AllenInstitute/scrattch.hicat/ ) and statsmodels 81 .
- Full pipeline: differential/statistical testing [limma] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn, seaborn, statsmodels]

### Multimodal cell maps as a foundation for structural and functional genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-08878-3 | PMCID: PMC12137143 | PMID: 40205054
- Version used: **1.7.3**
- Evidence: We calculated the kernel density estimation (KDE) for the mutated genes in cancer assemblies and other genes in the cell map using the stat.gaussian_kde function from the Python package scipy (v1.7.3).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> structure determination [PyTorch] -> machine learning [PyTorch, scikit-learn] -> visualisation [Cytoscape] -> stage not stated [AlphaFold, NumPy v1.21.6, STRING db, SciPy v1.7.3]

### A neural mechanism for learning from delayed postingestive feedback. (Nature 2025)

- DOI: 10.1038/s41586-025-08828-z | PMCID: PMC12176619 | PMID: 40175547
- Evidence: First, we de-noised the FOS imaging volume using a median filter (function, scipy.ndimage.median_filter; size, 3 pixels) before the background-subtraction step.
- Full pipeline: differential/statistical testing [scikit-learn] -> structure determination [Python] -> machine learning [Cellpose, Keras, TensorFlow, scikit-learn] -> visualisation [NumPy] -> stage not stated [Astropy, Kilosort v2.5, R, SciPy]

### Connectome-driven neural inventory of a complete visual system. (Nature 2025)

- DOI: 10.1038/s41586-025-08746-0 | PMCID: PMC12119369 | PMID: 40140576
- Evidence: Clustering was performed in Python using the scipy.hierarchy 92 and fastcluster 93 libraries.
- Full pipeline: dimensionality reduction/clustering [Python, SciPy] -> structure determination [BigStitcher] -> stage not stated [Jupyter, NumPy, Snakemake]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Version used: **1.10.1**
- Evidence: SL-Smart-seq3xpress data analysis Count matrices were processed with JupyterLab (v.4) notebooks using IPython (v.7.31) using the following modules: pandas (v.1.5.3), numpy (v.1.23.5), scipy (v.1.10.1), scanpy (v.1.7.2), openpyxl (v.3.1.2), matplotlib (v.3.6.3) and seaborn (v.0.12.2).
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### Cell-autonomous innate immunity by proteasome-derived defence peptides. (Nature 2025)

- DOI: 10.1038/s41586-025-08615-w | PMCID: PMC11946893 | PMID: 40044870
- Version used: **1.10.1**
- Evidence: Python packages used: beautifulsoup4 v.4.12.2, bio v.1.6.2, GSEApy v.1.1.0, matplotlib v.3.7.1, NumPy v.1.24.3, pandas v.2.0.2, SciPy v.1.10.1, seaborn v.0.12.2, sklearn v.0.0.post5, urllib3 v.2.0.3.
- Full pipeline: visualisation [PyMOL v2.5.7] -> stage not stated [AlphaFold, ComplexHeatmap v2.16.0, ImageJ v2.14.0, Matplotlib v3.7.1, NumPy v1.24.3, SciPy v1.10.1, ggplot2 v3.4.4, scikit-learn v0.0, seaborn v0.12.2, tidyverse v1.1.2]

### A travelling-wave strategy for plant-fungal trade. (Nature 2025)

- DOI: 10.1038/s41586-025-08614-x | PMCID: PMC11882455 | PMID: 40011773
- Evidence: We then fitted a Gaussian function to the resulting curve using the curve_fit function of the scipy.optimize 60 package.
- Full pipeline: machine learning [StarDist] -> visualisation [Matplotlib] -> stage not stated [SciPy, scikit-image, seaborn]

### RNA neoantigen vaccines prime long-lived CD8&lt;sup&gt;+&lt;/sup&gt; T cells in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08508-4 | PMCID: PMC11946889 | PMID: 39972124
- Evidence: The numerical integration was done using scipy.integrate.cumtrapz.
- Full pipeline: quality control [Scanpy] -> alignment/mapping [BWA v0.7.17] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [GATK, GSEA, Mutect2 v1.1.7, Python v3.11.6, SciPy, Strelka v1.0.15]

### A metagenomic 'dark matter' enzyme catalyses oxidative cellulose conversion. (Nature 2025)

- DOI: 10.1038/s41586-024-08553-z | PMCID: PMC11946906 | PMID: 39939775
- Evidence: Initial parameter estimation: g and A tensors were estimated using laboratory-developed scripts in Python (SciPy/NumPy) 74 .
- Full pipeline: quality control [FastQC v0.12.0, Trimmomatic] -> read trimming [FastQC v0.12.0, Trimmomatic] -> alignment/mapping [Bowtie2, RAxML, kallisto v0.46.1] -> quantification [Bowtie2, SAMtools, kallisto v0.46.1] -> normalisation [kallisto v0.46.1] -> simulation/modelling [VMD] -> structure determination [Coot, PHENIX, RAxML] -> stage not stated [NumPy, Prokka, PyMOL v2.3, Python, RoseTTAFold, SciPy, phyloseq v1.20]

### UM171 glues asymmetric CRL3-HDAC1/2 assembly to degrade CoREST corepressors. (Nature 2025)

- DOI: 10.1038/s41586-024-08532-4 | PMCID: PMC11882444 | PMID: 39939761
- Evidence: Data analysis was performed using Python (v.3.9.12) with Biopython (v.1.78), Pandas (v.1.5.1), SciPy package (v.1.10.0) and NumPy (v.1.23.4). sgRNA enrichment was calculated as previously described 52 , 69 .
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Python v3.9.12, statsmodels] -> structure determination [AlphaFold, Coot v0.9.8.91, PHENIX v1.20.1] -> visualisation [Cytoscape v3.9.0, PyMOL v2.5.4, STRING db] -> stage not stated [ChimeraX, Matplotlib v3.7.1, NumPy v1.23.4, R, SciPy, Topaz, ggplot2 v3.5.1, limma, pandas v1.5.1]

### Transcriptomic neuron types vary topographically in function and morphology. (Nature 2025)

- DOI: 10.1038/s41586-024-08518-2 | PMCID: PMC11864986 | PMID: 39939759
- Evidence: The remaining 169 exemplars were clustered using hierarchical clustering (scipy.cluster.hierarchy.linkage, method=‘complete’, metric=‘correlation’; scipy.cluster.hierarchy.fcluster, criterion=‘maxclust’).
- Full pipeline: normalisation [ANTs, UMAP] -> registration [Suite2p] -> dimensionality reduction/clustering [SciPy, UMAP, pheatmap, scDblFinder] -> visualisation [pheatmap] -> stage not stated [ImageJ, Monocle, PsychoPy, R, Seurat, napari, scikit-learn]

### SKI complex loss renders 9p21.3-deleted or MSI-H cancers dependent on PELO. (Nature 2025)

- DOI: 10.1038/s41586-024-08509-3 | PMCID: PMC11864980 | PMID: 39910293
- Evidence: 1a ), and performed a left-tailed Student’s t -test between the two populations for all genetic dependencies in the CRISPR data (using scipy.stats.ttest_ind).
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> differential/statistical testing [DESeq2] -> visualisation [DESeq2] -> stage not stated [ImageJ v1.53k, Picard, RSEM, SciPy]

### Left-right-alternating theta sweeps in entorhinal-hippocampal maps of space. (Nature 2025)

- DOI: 10.1038/s41586-024-08527-1 | PMCID: PMC11946909 | PMID: 39900625
- Evidence: Clustering analyses of grid-cell modules and bursting subtypes of grid cells were conducted using the python package Scanpy 87 and its dependencies (including numpy, pandas, scipy, scikit-learn and matplotlib).
- Full pipeline: dimensionality reduction/clustering [Matplotlib, NumPy, Scanpy, SciPy, UMAP, scikit-learn] -> stage not stated [DeepLabCut, Kilosort v2.5]

### SARS-CoV-2 evolution on a dynamic immune landscape. (Nature 2025)

- DOI: 10.1038/s41586-024-08477-8 | PMCID: PMC11882442 | PMID: 39880955
- Evidence: Parameter estimation was performed using scipy.optimize.root, applying the Levenberg–Marquardt method to solve the ordinary least-square problem. argmin IC 50 ( x ) ^ ( t max , t half ) ∑ t ∥ P Neut ( t , Wuhan-Hu-1 , Delta and IC 50 ( x ) ^ ( t max , t half ) ) − VE ( t , Wuhan-Hu-1 , Delta ) ∥ 2 , in which VE( t , Wuhan-Hu-1, Delta) denotes the vaccine efficacy against the Delta strain t days af...
- Full pipeline: stage not stated [Pangolin, Python v3.11.3, R v4.2.3, SciPy]

### Tissue-resident memory CD8 T cell diversity is spatiotemporally imprinted. (Nature 2025)

- DOI: 10.1038/s41586-024-08466-x | PMCID: PMC11903307 | PMID: 39843748
- Evidence: Transcriptional neighbourhood decomposition was performed using Scikit-learn 71 non-negative matrix factorization on a matrix of the summed transcript count values for the ten nearest neighbours of each cell, calculated with a SciPy 72 K -dimensional tree, to create a transformed data matrix W with 15 latent factors.
- Full pipeline: alignment/mapping [OpenCV, seaborn] -> quantification [QuPath] -> normalisation [Squidpy, scVelo] -> dimensionality reduction/clustering [Scanpy, SciPy, scikit-learn] -> machine learning [TensorFlow v2.18.0] -> visualisation [igraph, seaborn] -> stage not stated [CellChat, Cellpose, XGBoost]

### Complete human recombination maps. (Nature 2025)

- DOI: 10.1038/s41586-024-08450-5 | PMCID: PMC11922761 | PMID: 39843742
- Version used: **1.10.1**
- Evidence: .../DecodeGenetics/NCOurd ; R (v.4.2.2 with lm v.4.2.2, xoi v.0.67-1), https://www.r-project.org/ ; Python (v.3.8.1 with numpy v.1.24.2, pandas v.1.4.0, scipy v.1.10.1, statsmodels v.0.13.2), https://www.python.org/downloads/ .
- Full pipeline: stage not stated [NumPy v1.24.2, SciPy v1.10.1, lme4, statsmodels v0.13.2]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: We calculated Spearman’s correlation values between these imputed expression values and predicted ancestor distributions using scipy.stats.spearmanr 115 .
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### Specification of claustro-amygdalar and palaeocortical neurons and circuits. (Nature 2025)

- DOI: 10.1038/s41586-024-08361-5 | PMCID: PMC11821539 | PMID: 39814878
- Evidence: The analysis was performed using Python, with key libraries including Pandas for data manipulation, Seaborn and Matplotlib for visualization, NetworkX for network analysis, and SciPy for statistical tests.
- Full pipeline: quality control [FastQC, STAR v2.4.0e] -> alignment/mapping [FastQC, STAR v2.4.0e] -> quantification [ImageJ, QuPath] -> dimensionality reduction/clustering [DESeq2 v10.1186, R, UMAP] -> differential/statistical testing [DESeq2 v10.1186, Matplotlib, NetworkX, Python, R, SciPy, seaborn] -> visualisation [Matplotlib, NetworkX, SciPy, seaborn] -> stage not stated [FreeSurfer, Seurat, Signac v1.1.0]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Evidence: Pearson correlation, 95% confidence interval for the correlation, and P value for association between cell-type proportion and sample age was computed using scipy.stats.pearsonr.
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Synthetic GPCRs for programmable sensing and control of cell behaviour. (Nature 2025)

- DOI: 10.1038/s41586-024-08282-3 | PMCID: PMC11666456 | PMID: 39633047
- Evidence: Statistical analysis Graphs and statistical analyses were generated using Python (with Pandas, Seaborn, Scipy and Statsmodels packages).
- Full pipeline: quantification [Matplotlib] -> differential/statistical testing [SciPy, seaborn] -> stage not stated [AlphaFold, ImageJ, MACS2, PHENIX, Python]

### Evolving antibody response to SARS-CoV-2 antigenic shift from XBB to JN.1. (Nature 2025)

- DOI: 10.1038/s41586-024-08315-x | PMCID: PMC11754117 | PMID: 39510125
- Evidence: Pairwise dissimilarities for all antibodies in the dataset were computed using the SciPy module (scipy.spatial.distance.jensenshannon, v.1.7.0).
- Full pipeline: dimensionality reduction/clustering [R, UMAP, ggplot2 v3.3.3, igraph] -> differential/statistical testing [UMAP] -> visualisation [R, UMAP, ggplot2 v3.3.3] -> stage not stated [SciPy]

### Progressive plasticity during colorectal cancer metastasis. (Nature 2025)

- DOI: 10.1038/s41586-024-08150-0 | PMCID: PMC11754107 | PMID: 39478232
- Version used: **1.9.1**
- Evidence: (3) Compute the Shannon entropy of patient labels in the high-scoring subset of cells for each module using the SciPy (v.1.9.1) function scipy.stats.entropy.
- Full pipeline: read trimming [edgeR v3.40.2] -> quantification [CellProfiler v4.2.5, ImageJ v1.53t, edgeR v3.40.2] -> normalisation [edgeR v3.40.2, scikit-learn] -> dimensionality reduction/clustering [GSEA, R, UMAP] -> differential/statistical testing [GSEA, R] -> visualisation [Python, seaborn v0.11.2] -> stage not stated [DESeq2 v1.38.3, GSVA v1.46.0, Matplotlib v3.6.0, NumPy, Scanpy v1.9.1, SciPy v1.9.1, scikit-image v0.23.2, survival (R) v0.4.9]

### Bottom-up synthesis of molecular nanodiamond from nanographene. (Nature 2026)

- DOI: 10.1038/s41586-026-10669-3 | PMCID: PMC13323094 | PMID: 42191905
- Evidence: The data from SIs was processed using open-source Python libraries (Hyperspy 53 , Scipy 54 and Scikit 55 , 56 ).
- Full pipeline: simulation/modelling [Quantum ESPRESSO] -> stage not stated [SciPy]

### Neural representation of action symbols in primate frontal cortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10297-x | PMCID: PMC13233313 | PMID: 42162420
- Version used: **1.10.1**
- Evidence: All behavioural and neural analyses were performed using custom-written Python (v.3.8) code unless otherwise noted, incorporating the analysis and plotting libraries numpy (v.1.24.3), scipy (v.1.10.1), scikit-learn (v.1.3.0), pandas (v.2.0.3), seaborn (v.0.12.2), elephant (v.1.0.0) and statsmodels (v.0.14.0).
- Full pipeline: dimensionality reduction/clustering [Kilosort v2.5, UMAP] -> machine learning [scikit-learn v1.3.0] -> stage not stated [NumPy v1.24.3, SciPy v1.10.1, pandas v2.0.3, seaborn v0.12.2, statsmodels v0.14.0]

### Large-scale discovery, analysis and design of protein energy landscapes. (Nature 2026)

- DOI: 10.1038/s41586-026-10465-z | PMCID: PMC13293878 | PMID: 42129553
- Evidence: PCCs were computed using the pearsonr function from SciPy Stats.
- Full pipeline: dimensionality reduction/clustering [Snakemake] -> stage not stated [AlphaFold, ColabFold, Jupyter, SciPy]

### Genome-wide sweeps create ecological units in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-026-10476-w | PMCID: PMC13322978 | PMID: 42092154
- Evidence: The observed SNP distribution was fitted to the equation using MLE with the L-BFGS-B algorithm in the Python package SciPy 57 .
- Full pipeline: alignment/mapping [MetaPhlAn v4.0.6] -> differential/statistical testing [ComplexHeatmap v2.12.1, ggplot2 v3.5.1, ggpubr v0.6.0] -> stage not stated [Prokka v1.14.6, R, SciPy]

### Pervasive and programmed nucleosome distortion on single chromatin fibres. (Nature 2026)

- DOI: 10.1038/s41586-026-10418-6 | PMCID: PMC13253354 | PMID: 42056506
- Evidence: We used a custom script (compute_mdr_per_sample.py), which uses the find_peaks function from scipy and computes the ratio of maximum peak heights in footprint length histograms for mononucleosome- and dinucleosome-sized footprints per sequencing library.
- Full pipeline: dimensionality reduction/clustering [ChimeraX v1.7.1, Python, Scanpy v1.9.3, UMAP] -> visualisation [ChimeraX v1.7.1, Scanpy v1.9.3, UMAP] -> stage not stated [SciPy]

### Spatial atlas of diabetic kidney disease reveals a B cell-rich subgroup. (Nature 2026)

- DOI: 10.1038/s41586-026-10363-4 | PMCID: PMC13216073 | PMID: 42056516
- Evidence: The count matrices were loaded using scipy.io.mmread and transposed to ensure cells corresponded to rows and genes to columns.
- Full pipeline: read trimming [STAR v2.7.3a] -> alignment/mapping [RSEM, STAR v2.7.3a] -> quantification [RSEM, Squidpy] -> dimensionality reduction/clustering [UMAP, seaborn] -> differential/statistical testing [CellPhoneDB, DESeq2, limma, seaborn] -> visualisation [seaborn] -> stage not stated [AnnData, Enrichr, GSEA, Matplotlib, Scanpy, SciPy, Seurat, Trim Galore v0.4.5]

### Myosin forces remodel F-actin for mechanosensitive protein recognition. (Nature 2026)

- DOI: 10.1038/s41586-026-10398-7 | PMCID: PMC13233326 | PMID: 42020745
- Evidence: A Kolmogorov–Smirnov test as implemented in Scipy 100 was performed to assess whether the observed major axis angle distribution was significantly different from a normal distribution, and no significant difference was found ( P = 0.27).
- Full pipeline: simulation/modelling [Python] -> structure determination [IMOD] -> visualisation [ChimeraX, UCSF Chimera] -> stage not stated [EMAN2, MotionCor2, PHENIX, RELION, SciPy]

### Biodiversity resilience in a tropical rainforest. (Nature 2026)

- DOI: 10.1038/s41586-026-10365-2 | PMCID: PMC13128449 | PMID: 41951739
- Evidence: We used the function optimize.curve_fit from the scipy package v.1.10.0 in Python to fit equation ( 5 ) to the data.
- Full pipeline: stage not stated [Jupyter, Python, R, SciPy]

### Insulin resistance prediction from wearables and routine blood biomarkers. (Nature 2026)

- DOI: 10.1038/s41586-026-10179-2 | PMCID: PMC13061641 | PMID: 41840032
- Version used: **1.16.3**
- Evidence: Data processing, model training and evaluation were implemented in Python using numpy v.2.0.2, tensorflow v.2.19.0, scipy v.1.16.3, statsmodels v.0.14.6, sklearn v.1.6.1, shap v.0.50.0, xgboost v.3.1.2, torch v.2.9.0, pandas v.2.2.2, umap v.0.5.9.post2, pickle v.4.0, pytz v.2025.2, re v.2.2.1, tqdm v.4.67.1, IPython v.7.34.0, json v.2.0.9 and altair v.5.5.0.
- Full pipeline: dimensionality reduction/clustering [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> differential/statistical testing [XGBoost] -> machine learning [Jupyter v7.34.0, NumPy v2.0.2, Python v7.34.0, SciPy v1.16.3, scikit-learn v1.6.1, statsmodels v0.14.6] -> visualisation [Matplotlib v3.10.0, seaborn v0.13.2]

### Assembly of helper NLR resistosome clusters upon activation of a coiled-coil NLR. (Nature 2026)

- DOI: 10.1038/s41586-026-10215-1 | PMCID: PMC13043302 | PMID: 41813892
- Evidence: All computational analyses and visualizations were performed in Python (v3.10), using the NumPy 76 , Pandas 77 , SciPy 78 and Matplotlib 79 libraries.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [R v4.3.1, ggplot2] -> differential/statistical testing [lme4] -> visualisation [Matplotlib, NumPy, PyMOL, Python v3.10, R v4.3.1, SciPy, ggplot2] -> stage not stated [AlphaFold, ImageJ, TrackMate]

### The integrated stress response promotes immune evasion through lipocalin 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10143-0 | PMCID: PMC13128482 | PMID: 41708864
- Evidence: We examined the differential expression of LCN2 and ATF4 between inflamed and immune-excluded phenotypes using analysis done with the Wilcoxon rank-sum test (Mann–Whitney U test), implemented in Python’s scipy.stats library to identify significant differences between these specific immune contexts.
- Full pipeline: quantification [HTSeq, ImageJ, RSEM, TrackMate] -> normalisation [RSEM] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Python, SciPy] -> stage not stated [GSEA, Seurat]

### Astrocytes enable amygdala neural representations supporting memory. (Nature 2026)

- DOI: 10.1038/s41586-025-10068-0 | PMCID: PMC13061616 | PMID: 41673152
- Evidence: The saturating function was fit to F1 scores using the curve_fit function from the SciPy Python package.
- Full pipeline: stage not stated [ImageJ v1.37, SciPy]

### Intestinal macrophages modulate synucleinopathy along the gut-brain axis. (Nature 2026)

- DOI: 10.1038/s41586-025-09984-y | PMCID: PMC12960212 | PMID: 41606336
- Evidence: Plots were prepared using Python v.3.12.4, Plotly and Scipy.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [QuPath, R v4.0, SciPy, Seurat v4.3]

### GlycoRNA complexed with heparan sulfate regulates VEGF-A signalling. (Nature 2026)

- DOI: 10.1038/s41586-025-10052-8 | PMCID: PMC12999495 | PMID: 41606331
- Evidence: Colocalization of spots from paired channels were analysed by implementing a custom Python script ( https://github.com/FlynnLab/jonperr ) to identify the nearest neighbours of each spot (in nm) with a k-d tree algorithm (scipy.spatial.KDTree).
- Full pipeline: read trimming [Cutadapt v4.9, DESeq2 v1.42.1] -> alignment/mapping [Bowtie2 v2.5.4] -> differential/statistical testing [DESeq2 v1.42.1] -> stage not stated [ImageJ, Python, SciPy]

### Baby-to-baby strain transmission shapes the developing gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09983-z | PMCID: PMC12960237 | PMID: 41565819
- Version used: **1.10.1**
- Evidence: Statistical analysis Statistical analyses were performed in Python (v3.10.12) using libraries scikit-bio (v0.5.9), scipy (v1.10.1) and statsmodels (v0.14.0).
- Full pipeline: differential/statistical testing [Python v3.10.12, SciPy v1.10.1, statsmodels v0.14.0] -> stage not stated [BEDTools v2.30, Bowtie2 v2.3.4.3, MetaPhlAn v4.1, SAMtools v1.19, Trim Galore v0.6.6]

### Critical role for a high-plasticity cell state in lung cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09985-x | PMCID: PMC12960256 | PMID: 41565826
- Evidence: Lines of best fit and r 2 values were calculated using scipy.stats.linregress and statistical significance for Pearson correlations was determined using an exact distribution with the built-in scipy.stats.pearsonr function.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AnnData, ImageJ, Jupyter, Matplotlib v3.8.4, NumPy, R, pingouin v0.5.4, scDblFinder]

### Quantum spin resonance in engineered proteins for multimodal sensing. (Nature 2026)

- DOI: 10.1038/s41586-025-09971-3 | PMCID: PMC12851924 | PMID: 41565820
- Version used: **1.15.1**
- Evidence: Data processing was performed using Python (v3.11.11), SciPy (v1.15.1) 64 , NumPy (v.126.4) 65 , scikit-learn (v1.6.1) 66 and scikit-image (v0.20.0) 66 .
- Full pipeline: machine learning [XGBoost] -> stage not stated [NumPy v126.4, SciPy v1.15.1, scikit-image v0.20.0, scikit-learn v1.6.1]

### Ageing promotes microglial accumulation of slow-degrading synaptic proteins. (Nature 2026)

- DOI: 10.1038/s41586-025-09987-9 | PMCID: PMC12935553 | PMID: 41565824
- Evidence: The logarithmically transformed normalized trajectories, consisting of four values per time point, were fitted using scipy.optimize.minimize.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, featureCounts v2.0.6] -> normalisation [SciPy] -> dimensionality reduction/clustering [R] -> differential/statistical testing [Bioconductor] -> simulation/modelling [SciPy] -> stage not stated [DESeq2, Enrichr, ImageJ, MAGMA, Seurat, fastp]

### Dominant contribution of Asgard archaea to eukaryogenesis. (Nature 2026)

- DOI: 10.1038/s41586-025-09960-6 | PMCID: PMC12872458 | PMID: 41535464
- Evidence: To assess and remove such erroneous data, we first estimated the log-normal distribution of all stem lengths using scipy.stats v.1.11.1 and excluded any stems outside the 0–99.5% probability point function interval.
- Full pipeline: dimensionality reduction/clustering [Python, scikit-learn v1.3.0] -> stage not stated [SciPy]

### A nowhere-to-hide mechanism ensures complete piRNA-directed DNA methylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09940-w | PMCID: PMC7618654 | PMID: 41535457
- Evidence: ...r, ggpubr and Hmisc toolkits (versions ggplot2_3.5.1, tidyr_1.3.1, dplyr_1.1.4, ggpubr_0.6.0, Hmisc_5.2.1), Python (version 3.12.9) using the pandas, scipy, scikit-learn, matplotlib and seaborn packages (versions pandas_2.2.3, scipy_1.14.1, scikit-learn_1.5.2, matplotlib_3.9.2, seaborn_0.13.2) or Microsoft Excel for Mac (Office 365, version 16.9).
- Full pipeline: alignment/mapping [Clustal Omega] -> quantification [R v4.4.2, ggplot2, ggpubr, tidyverse] -> differential/statistical testing [R v4.4.2, ggplot2, ggpubr, tidyverse] -> visualisation [AlphaFold, Clustal Omega, ColabFold v1.5.5, Python, R v4.4.2, ggplot2, ggpubr, tidyverse] -> stage not stated [Cellpose, Cutadapt v1.18, ImageJ v1.54k, Matplotlib, PyMOL v3.1.3.1, QuPath v0.5.1, SciPy, Trim Galore v0.6.7, scikit-learn, seaborn]

### The ubiquitin ligase KLHL6 drives resistance to CD8&lt;sup&gt;+&lt;/sup&gt; T cell dysfunction. (Nature 2026)

- DOI: 10.1038/s41586-025-09926-8 | PMCID: PMC12979199 | PMID: 41535474
- Evidence: Embedding density was used for density plots and calculated using scanpy.tl.embedding_density, which is a wrapper for the gaussian density algorithm under scipy.
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, Scanpy] -> read trimming [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> alignment/mapping [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a] -> quantification [Cutadapt v2.9, FastQC v0.11.9, STAR v2.7.7a, edgeR v3.36.0, limma] -> normalisation [Scanpy, edgeR v3.36.0] -> dimensionality reduction/clustering [R, UMAP, clusterProfiler v4.12.0] -> differential/statistical testing [edgeR v3.36.0] -> stage not stated [GSEA, SciPy]

### Plastic landmark anchoring in zebrafish compass neurons. (Nature 2026)

- DOI: 10.1038/s41586-025-09888-x | PMCID: PMC12916487 | PMID: 41501455
- Evidence: The fitting was performed with the ‘curve_fit’ function from the scipy package, and parameters were bounded in the range of \documentclass[12pt]{minimal} \usepackage{amsmath} \usepackage{wasysym} \usepackage{amsfonts} \usepackage{amssymb} \usepackage{amsbsy} \usepackage{mathrsfs} \usepackage{upgreek} \setlength{\oddsidemargin}{-69pt} \begin{document}$$a\ge 0,{b}\in (\,-\,\pi ,\pi ]$$\end{document}...
- Full pipeline: differential/statistical testing [scikit-learn v1.1.2] -> stage not stated [SciPy, Suite2p]

### A mechanical ratchet drives unilateral cytokinesis. (Nature 2026)

- DOI: 10.1038/s41586-025-09915-x | PMCID: PMC12916326 | PMID: 41501469
- Evidence: The P value was calculated using scipy.stats.ttest_ind (two-sided t -test) and the data were plotted in Python.
- Full pipeline: differential/statistical testing [SciPy] -> visualisation [SciPy] -> stage not stated [Python, TrackMate, scikit-image]

### A young progenitor for the most common planetary systems in the Galaxy. (Nature 2026)

- DOI: 10.1038/s41586-025-09840-z | PMCID: PMC12779570 | PMID: 41501195
- Evidence: We used Broyden–Fletcher–Goldfarb–Shanno optimization 51 as implemented in scipy.optimize for initial parameter estimates, followed by posterior sampling with the No-U-Turn Sampler 52 , an efficient gradient-based Hamiltonian Monte Carlo sampler implemented in PyMC3.
- Full pipeline: simulation/modelling [SciPy] -> stage not stated [PyMC, PyMC3]

### Palaeometabolomes yield biological and ecological profiles at early human sites. (Nature 2026)

- DOI: 10.1038/s41586-025-09843-w | PMCID: PMC12851940 | PMID: 41407854
- Evidence: Statistical tests such as ANOVA and Kruskal–Wallis were performed using the SciPy library 98 .
- Full pipeline: dimensionality reduction/clustering [seaborn] -> differential/statistical testing [SciPy, scikit-learn] -> visualisation [seaborn]

### Gut micro-organisms associated with health, nutrition and dietary interventions. (Nature 2026)

- DOI: 10.1038/s41586-025-09854-7 | PMCID: PMC12893911 | PMID: 41372407
- Version used: **1.11.4**
- Evidence: Analyses we carried out with Python (v.3.12.0), using also the following libraries: numpy (v.1.26.2), scipy (v.1.11.4), statsmodels (v.0.14.0), and matplotlib (v.3.8.2) and seabron (v.0.11.2) for visualization.
- Full pipeline: quantification [MetaPhlAn] -> differential/statistical testing [scikit-learn v1.3.2] -> machine learning [scikit-learn v1.3.2] -> visualisation [Matplotlib v3.8.2, NumPy v1.26.2, SciPy v1.11.4, statsmodels v0.14.0] -> stage not stated [Conda, FSL, pingouin]

### Computational enzyme design by catalytic motif scaffolding. (Nature 2026)

- DOI: 10.1038/s41586-025-09747-9 | PMCID: PMC12727513 | PMID: 41339546
- Evidence: Denaturation midpoints were calculated from a sigmoidal fit with the Python SciPy library.
- Full pipeline: simulation/modelling [GROMACS, MDAnalysis] -> structure determination [PHENIX] -> stage not stated [AlphaFold, SciPy]

### Inhibitors supercharge kinase turnover through native proteolytic circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09763-9 | PMCID: PMC12823440 | PMID: 41299171
- Version used: **1.4.1**
- Evidence: This was performed by fitting the equation 100 × e (− x × tau) in Python (v.3.7.6) and the package scipy (v.1.4.1) to each kinase’s CHX screening trajectory. t -SNE plots were generated with sklearn and matplotlib (v.1.0.1 and v.3.5.3, respectively) from ChEMBL drug-binding data processed as described in the Chemical Checker (CC) 24 and compounds were characterized with CC global bioactivity signa...
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.4, Picard, Trim Galore v0.6.6, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.4.5, featureCounts v2.0.1] -> quantification [Bowtie2 v2.4.5, featureCounts v2.0.1] -> normalisation [NumPy v1.21.5, pandas v1.0.1] -> differential/statistical testing [NumPy v1.21.5, pandas v1.0.1] -> simulation/modelling [AlphaFold, Matplotlib v1.0.1, Python v3.7.6, SciPy v1.4.1, scikit-learn] -> visualisation [seaborn v0.12.2] -> stage not stated [Enrichr, Fiji v2.1.1, GATK v4.1.8.1, GROMACS v2023.2, ImageJ v2.1.1, PHENIX, R v4.1.0, SAMtools v1.17, VMD v1.9.4, pheatmap v1.0.12]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Version used: **1.16.0**
- Evidence: Commonly used Python libraries (Python v3.11.13, matplotlib v3.10, Seaborn v0.13, numpy v2.2.6, pandas v2.3.1, scipy v1.16.0, anndata v0.11.4 and shapely v2.1.1) were applied to visualize spatial distribution of cells.
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Semantic design of functional de novo genes from a genomic language model. (Nature 2026)

- DOI: 10.1038/s41586-025-09749-7 | PMCID: PMC12804078 | PMID: 41261132
- Version used: **1.11.4**
- Evidence: Correlation between domain frequencies was assessed using the Pearson correlation coefficient calculated using the pearsonr function in SciPy (v1.11.4) 102 .
- Full pipeline: alignment/mapping [MAFFT v7.526] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [igraph v0.11.6] -> visualisation [ChimeraX, Matplotlib] -> stage not stated [AlphaFold, BLAST, HMMER v3.3.0, Python v3.11.8, SciPy v1.11.4]

### Spatial fibroblast niches define Crohn's fistulae. (Nature 2026)

- DOI: 10.1038/s41586-025-09744-y | PMCID: PMC12804086 | PMID: 41224999
- Evidence: All analyses were conducted using skimage for image processing 71 , 72 , numpy and pandas for data handling, matplotlib and seaborn for visualization, and scipy and scikit-learn for statistical and machine learning operations.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Cutadapt] -> alignment/mapping [Cutadapt, STAR] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Harmony v1.2.1, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, Matplotlib, NumPy, SciPy, scikit-image, scikit-learn, seaborn] -> visualisation [Matplotlib, NumPy, SciPy, ggplot2, scikit-image, scikit-learn, seaborn] -> stage not stated [Python v3.9, QuPath, R, SCENIC, Seurat v5.1.0, featureCounts]

### Comprehensive echocardiogram evaluation with view primed vision language AI. (Nature 2026)

- DOI: 10.1038/s41586-025-09850-x | PMCID: PMC12935550 | PMID: 41219498
- Version used: **1.12.0**
- Evidence: We used scikit-learn (v1.2.0) ( https://scikit-learn.org/ ) for probing methods, umap-learn (v0.5; https://umap-learn.readthedocs.io ) for dimensionality reduction and scipy (v1.12.0; https://scipy.org/ ) for statistics and linear algebra operations.
- Full pipeline: dimensionality reduction/clustering [SciPy v1.12.0] -> differential/statistical testing [SciPy v1.12.0, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [PyTorch v2.1.2]

### Eight millennia of continuity of a previously unknown lineage in Argentina. (Nature 2026)

- DOI: 10.1038/s41586-025-09731-3 | PMCID: PMC12747222 | PMID: 41193808
- Evidence: We computed a complete hierarchical clustering tree with the package linkage from the scipy library 102 , 103 (v.1.16.0).
- Full pipeline: quality control [ANGSD] -> dimensionality reduction/clustering [ADMIXTURE, SciPy] -> stage not stated [PLINK v1.9, Picard, R, ape (R) v5.8, ggplot2, tidyverse]

### Pregnancy and weaning regulate human maternal liver size and function. (PNAS 2021)

- DOI: 10.1073/pnas.2107269118 | PMCID: PMC8640831 | PMID: 34815335
- Evidence: Processing within the pipeline made use of the following Python libraries: Nipype ( 49 ), the Advanced Normalization Tools ( 50 ), the Insight Toolkit ( 51 ), Scikit-image ( 52 ), Scikit-learn ( 53 ), and SciPy ( 54 ).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [RSEM] -> quantification [RSEM] -> normalisation [ANTs, Nipype, SciPy, scikit-learn] -> differential/statistical testing [DESeq2 v1.22.2] -> stage not stated [GSEA]

### Multiparameter persistent homology landscapes identify immune cell spatial patterns in tumors. (PNAS 2021)

- DOI: 10.1073/pnas.2102166118 | PMCID: PMC8522280 | PMID: 34625491
- Evidence: Statistical tests were performed using the Python package scipy.stats ( https://www.scipy.org/ ).
- Full pipeline: differential/statistical testing [SciPy]

### Phytoplankton exudates and lysates support distinct microbial consortia with specialized metabolic and ecophysiological traits. (PNAS 2021)

- DOI: 10.1073/pnas.2101178118 | PMCID: PMC8521717 | PMID: 34620710
- Evidence: These tests were performed with custom python scripts using the “scipy stats” and “skbio” libraries.
- Full pipeline: alignment/mapping [Bowtie2] -> visualisation [R v3.4.0, ggplot2] -> stage not stated [SciPy]

### Deep learning for early warning signals of tipping points. (PNAS 2021)

- DOI: 10.1073/pnas.2106140118 | PMCID: PMC8488604 | PMID: 34544867
- Evidence: The simulation uses the odeint function from the Python package Scipy ( 42 ) with a step size of 0.01.
- Full pipeline: simulation/modelling [SciPy] -> stage not stated [Conda v2020.02, TensorFlow v2.0]

### Microbiome signatures of progression toward celiac disease onset in at-risk children in a longitudinal prospective cohort study. (PNAS 2021)

- DOI: 10.1073/pnas.2020322118 | PMCID: PMC8307711 | PMID: 34253606
- Evidence: Analyses of microbial species, strains, and pathways were performed in Python (using scipy.stats.mannwhitneyu and scipy.stats.wilcoxon functions), and those for metabolites were performed in R [using the Ttest.Anal function of the MetaboAnalyst 4.0 ( 100 ) using parameters nonpar = TRUE and paired = FALSE for the cross-sectional analysis and paired = TRUE for the longitudinal analysis].
- Full pipeline: quality control [MultiQC] -> read trimming [MultiQC] -> stage not stated [Python, SciPy]

### A catalog of tens of thousands of viruses from human metagenomes reveals hidden associations with chronic diseases. (PNAS 2021)

- DOI: 10.1073/pnas.2023202118 | PMCID: PMC8201803 | PMID: 34083435
- Evidence: Wilcoxon rank-sum test was computed with 100 bootstraps using Python, NumPy, and SciPy ( 103 ) for each OTU in a given study in which at least 10% of the total samples had an RPKM of at least 0.05 (bacterial OTUs with “IGGsearch abundance” of at least 0.005 in at least 10% of the samples were kept).
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> quantification [Bowtie2, NumPy, SAMtools, SciPy] -> machine learning [scikit-learn] -> stage not stated [Cytoscape, RepeatMasker]

### Comprehensive pregnancy monitoring with a network of wireless, soft, and flexible sensors in high- and low-resource health settings. (PNAS 2021)

- DOI: 10.1073/pnas.2100466118 | PMCID: PMC8157941 | PMID: 33972445
- Evidence: All time-series analyses were done on Python with the scipy package for signal processing and the matplotlib package for graphing.
- Full pipeline: stage not stated [Matplotlib, SciPy]

### A modular computational framework for medical digital twins. (PNAS 2021)

- DOI: 10.1073/pnas.2024287118 | PMCID: PMC8157963 | PMID: 33972437
- Evidence: These are supported by a wide variety of languages, including Python, Java, C/C++, Julia, Fortran, Mathematica, etc., and are commonly used in the Python programming community to link high performance numerical functions written in C or Fortran to Python programs (e.g., the NumPy and SciPy libraries).
- Full pipeline: stage not stated [Docker, NumPy, Python, SciPy]

### Automated, multiparametric monitoring of respiratory biomarkers and vital signs in clinical and home settings for COVID-19 patients. (PNAS 2021)

- DOI: 10.1073/pnas.2026610118 | PMCID: PMC8126790 | PMID: 33893178
- Evidence: All analysis used Python 3.0 with SciPy, PyWavelets, and TensorFlow packages.
- Full pipeline: stage not stated [Python v3.0, SciPy, TensorFlow]

### Global inequality remotely sensed. (PNAS 2021)

- DOI: 10.1073/pnas.1919913118 | PMCID: PMC8106331 | PMID: 33903226
- Evidence: The analysis was carried out in R ( https://www.r-project.org ) using the packages raster, rasterVis, sp, rgdal, ggplot2, and mixtools and Python ( https://www.python.org/ ) using numpy, matplotlib, scipy, and statsmodels.
- Full pipeline: stage not stated [Matplotlib, NumPy, R, SciPy, ggplot2, statsmodels]

### Gut microbiome contributions to altered metabolism in a pig model of undernutrition. (PNAS 2021)

- DOI: 10.1073/pnas.2024446118 | PMCID: PMC8166152 | PMID: 34001614
- Evidence: The Procrustes test (SciPy package; v1.3.0) ( 63 ) was applied to quantify the degree of similarity between PCA plots.
- Full pipeline: read trimming [Cutadapt, DADA2, R v3.5] -> alignment/mapping [Clustal Omega v1.2.4] -> quantification [SciPy] -> dimensionality reduction/clustering [SciPy, scikit-learn] -> differential/statistical testing [lme4, scikit-learn] -> machine learning [DADA2, R v3.5] -> visualisation [Matplotlib v3.1.0] -> stage not stated [BLAST, Bowtie2, HMMER v3.1, NumPy v1.16.4, Prokka v1.12]

### Declining greenness in Arctic-boreal lakes. (PNAS 2021)

- DOI: 10.1073/pnas.2021219118 | PMCID: PMC8053985 | PMID: 33876758
- Evidence: Trends were calculated using Theil-Sen’s Slope Estimator from the SciPy package ( 138 ), and slopes were tested for significance using a Mann–Kendall test, which is designed to identify monotonic trends and is been widely used to identify terrestrial greening and browning trends ( 15 ).
- Full pipeline: differential/statistical testing [Python, QGIS] -> stage not stated [SciPy]

### &lt;i&gt;ARABIDOPSIS THALIANA HOMEOBOX GENE 1&lt;/i&gt; controls plant architecture by locally restricting environmental responses. (PNAS 2021)

- DOI: 10.1073/pnas.2018615118 | PMCID: PMC8092594 | PMID: 33888582
- Evidence: For statistical analysis and plotting graphs, functions were used from Numerical Python ( https://numpy.org ), Scientific Python ( https://www.scipy.org ), and MatPlotLib ( https://matplotlib.org ).
- Full pipeline: differential/statistical testing [Matplotlib, NumPy, SciPy] -> stage not stated [MACS2]

### Establishment of heterochromatin in domain-size-dependent bursts. (PNAS 2021)

- DOI: 10.1073/pnas.2022887118 | PMCID: PMC8053981 | PMID: 33827924
- Evidence: 4 – 6 were fitted with the curve_fit function of the Scipy.optimize Python package which uses the method of nonlinear least squares to fit the function f ( x ) = a * e − x b to the data points in order to determine the b values of all systems corresponding to the respective parameter configuration.
- Full pipeline: stage not stated [SciPy]

### BABEL enables cross-modality translation between multiomic profiles at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2023070118 | PMCID: PMC8054007 | PMID: 33827925
- Version used: **1.2.1**
- Evidence: All metrics are calculated using the Python packages Sklearn version 0.21.2 ( 53 ), SciPy version 1.2.1 ( 54 ), and NumPy.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [AnnData v0.6.22, ArchR, Astropy, Matplotlib, NumPy, PyTorch v1.2.0, Python v3.7, Scanpy v1.4.3, SciPy v1.2.1, Signac, seaborn]

### Computationally designed peptide macrocycle inhibitors of New Delhi metallo-β-lactamase 1. (PNAS 2021)

- DOI: 10.1073/pnas.2012800118 | PMCID: PMC8000195 | PMID: 33723038
- Evidence: NDM-1 activity was plotted as a function of inhibitor concentration, and data were fitted with SciPy using a modified Hill equation to extract IC 50 values, as described in SI Appendix , section 3.3 .
- Full pipeline: visualisation [SciPy]

### Noninvasive neuromagnetic single-trial analysis of human neocortical population spikes. (PNAS 2021)

- DOI: 10.1073/pnas.2017401118 | PMCID: PMC7980398 | PMID: 33707209
- Version used: **1.4.1**
- Evidence: Data Availability All analyses were performed in the Python programming language in its most recent version (3.8.2) relying on the additional packages numpy (1.18.2), scipy (1.4.1), matplotlib (3.2.1), and the author-made M/EEG-analysis package “meet” in its most recent version ( https://github.com/neurophysics/meet ).
- Full pipeline: stage not stated [Matplotlib v3.2.1, NumPy v1.18.2, SciPy v1.4.1]

### Emergence of diauxie as an optimal growth strategy under resource allocation constraints in cellular metabolism. (PNAS 2021)

- DOI: 10.1073/pnas.2013836118 | PMCID: PMC7923608 | PMID: 33602812
- Evidence: It uses COBRApy ( 42 ) and Optlang ( 43 ) as a back end to ensure compatibility with several open-source (GLPK, scipy) as well as commercial (CPLEX, Gurobi) solvers.
- Full pipeline: stage not stated [SciPy]

### Climate control on terrestrial biospheric carbon turnover. (PNAS 2021)

- DOI: 10.1073/pnas.2011585118 | PMCID: PMC7923348 | PMID: 33593902
- Evidence: Regression analyses were performed using the Numpy and Scipy packages in Python version 3.5; all analysis code is provided in Dataset S1 .
- Full pipeline: differential/statistical testing [NumPy, Python v3.5, SciPy]

### Topographic connectivity reveals task-dependent retinotopic processing throughout the human brain. (PNAS 2021)

- DOI: 10.1073/pnas.2017032118 | PMCID: PMC7812773 | PMID: 33372144
- Evidence: The fitting procedure consisted of an initial grid fit stage, followed by an iterative fitting stage using the L-BFGS-B algorithm as implemented in scipy.optimize.
- Full pipeline: stage not stated [FSL, FreeSurfer, SciPy, statsmodels]

### Correlated gene modules uncovered by high-precision single-cell transcriptomics. (PNAS 2022)

- DOI: 10.1073/pnas.2206938119 | PMCID: PMC9907105 | PMID: 36508663
- Evidence: Hierarchical clustering was performed using the SciPy function “scipy.cluster.hierarchy.linkage” using method “average” and with a distance metric of 1 − abs ( ρ ij ), where ρ ij is the Pearson correlation between genes i and j .
- Full pipeline: read trimming [STAR v2.5.2] -> alignment/mapping [RepeatMasker, STAR v2.5.2] -> dimensionality reduction/clustering [R, SciPy] -> stage not stated [PyTorch, STRING db, Seurat v3.9.9.9024, WGCNA]

### The molecular basis for pore pattern morphogenesis in diatom silica. (PNAS 2022)

- DOI: 10.1073/pnas.2211549119 | PMCID: PMC9894196 | PMID: 36459651
- Evidence: The python code for image processing was partially adapted from the skimage tutorial repository using python 3.7.4 and various packages [scipy, numpy, pandas and scikit-image ( 64 )].
- Full pipeline: dimensionality reduction/clustering [scikit-learn v0.21.3] -> differential/statistical testing [Matplotlib v3.5, seaborn v0.11] -> visualisation [Matplotlib v3.5, seaborn v0.11] -> stage not stated [BLAST, NumPy, SciPy, scikit-image]

### Stochastic survival of the densest and mitochondrial DNA clonal expansion in aging. (PNAS 2022)

- DOI: 10.1073/pnas.2122073119 | PMCID: PMC9894218 | PMID: 36442091
- Evidence: These systems have been integrated numerically using the Python library SciPy.
- Full pipeline: stage not stated [SciPy]

### Impact of cultural and genetic structure on food choices along the Silk Road. (PNAS 2022)

- DOI: 10.1073/pnas.2209311119 | PMCID: PMC9704696 | PMID: 36375050
- Evidence: We built the correlation matrix of “raw” food preferences, and we used the scipy.cluster.hierarchy.linkage() function on this matrix (method = “average”, metric = “euclidean”) to hierarchically cluster the food items (the “average” method is also known as the unweighted pair group method with arithmetic mean algorithm, UPGMA).
- Full pipeline: normalisation [scikit-learn] -> dimensionality reduction/clustering [SciPy, lme4] -> differential/statistical testing [lme4] -> machine learning [ADMIXTURE] -> stage not stated [PLINK v1.9, R, vegan]

### Dynamics of plosive consonants via imaging, computations, and soft electronics. (PNAS 2022)

- DOI: 10.1073/pnas.2214164119 | PMCID: PMC9674252 | PMID: 36343234
- Evidence: All analyses used Python 3.0 with SciPy and TensorFlow packages.
- Full pipeline: stage not stated [Python v3.0, SciPy, TensorFlow]

### A tool for monitoring cell type-specific focused ultrasound neuromodulation and control of chronic epilepsy. (PNAS 2022)

- DOI: 10.1073/pnas.2206828119 | PMCID: PMC9674244 | PMID: 36343238
- Evidence: Epileptiform events were quantified offline in Python by band pass filtering data according to spike dynamics and locating peaks in the absolute signal (Scipy).
- Full pipeline: alignment/mapping [SPM] -> quantification [Python, SciPy] -> differential/statistical testing [NumPy, SPM]

### Adult neurogenesis acts as a neural regularizer. (PNAS 2022)

- DOI: 10.1073/pnas.2206704119 | PMCID: PMC9659416 | PMID: 36322739
- Evidence: Models were built and analyzed in Python 3.6 ( 65 ) with custom scripts that are freely available on GitHub, and were developed using the following packages: PyTorch ( 66 ), Ax ( https://github.com/facebook/Ax ), NumPy ( 67 ), SciPy ( 68 ), Pandas ( 69 ), Matplotlib ( 70 ), Seaborn ( 71 ), and Scikit-learn 0.21.1 ( 72 ).
- Full pipeline: stage not stated [Matplotlib, NumPy, PyTorch, Python v3.6, SciPy, scikit-learn v0.21.1, seaborn]

### Rapid homeostatic modulation of transsynaptic nanocolumn rings. (PNAS 2022)

- DOI: 10.1073/pnas.2119044119 | PMCID: PMC9659372 | PMID: 36322725
- Evidence: Electrophysiology data were acquired with Clampex (Molecular Devices) and analyzed using routines written with scientific python libraries, including numpy, scipy, IPython, and neo ( 43 ). mEPSPs were detected using an implementation of a template-matching algorithm ( 44 , 45 ).
- Full pipeline: stage not stated [ImageJ v1.51n, Jupyter, NumPy, SciPy]

### ADAR regulates APOL1 via A-to-I RNA editing by inhibition of MDA5 activation in a paradoxical biological circuit. (PNAS 2022)

- DOI: 10.1073/pnas.2210150119 | PMCID: PMC9636950 | PMID: 36282916
- Evidence: The Biocircuits and SciPy packages were used to solve the equations ( 43 , 44 ).
- Full pipeline: quality control [STAR] -> read trimming [STAR] -> alignment/mapping [SAMtools v1.13, STAR] -> quantification [DESeq2, HTSeq] -> normalisation [R v4.1.2, featureCounts v2.0.0] -> stage not stated [Matplotlib, SciPy]

### In situ structural analysis reveals membrane shape transitions during autophagosome formation. (PNAS 2022)

- DOI: 10.1073/pnas.2209823119 | PMCID: PMC9522377 | PMID: 36122245
- Version used: **1.6.2**
- Evidence: Statistical analyses were performed with the statistical analysis package in scipy 1.6.2 (scipy.stats) and the pingouin package (v.0.3.11, https://pingouin-stats.org/ ) ( 68 ), using the tests indicated in each respective analysis.
- Full pipeline: alignment/mapping [IMOD v4.10.49] -> differential/statistical testing [SciPy v1.6.2, pingouin] -> structure determination [ChimeraX v1.2.5, IMOD v4.10.49] -> stage not stated [ImageJ v1.53, RELION v3.1.2]

### Microbial functional diversity across biogeochemical provinces in the central Pacific Ocean. (PNAS 2022)

- DOI: 10.1073/pnas.2200014119 | PMCID: PMC9477243 | PMID: 36067300
- Evidence: Stations were clustered using a hierarchical clustering analysis in python using SciPy hierarchical clustering ( 69 ) with a Euclidian distance matrix and Ward variance minimization ( SI Appendix , Fig.
- Full pipeline: quantification [NumPy] -> dimensionality reduction/clustering [SciPy]

### Walking is like slithering: A unifying, data-driven view of locomotion. (PNAS 2022)

- DOI: 10.1073/pnas.2113222119 | PMCID: PMC9477242 | PMID: 36067311
- Version used: **0.17.0**
- Evidence: For the robots, we used a commercial three-dimensional (3D) passive marker tracking system (10 Qualisys Oqus-310+ cameras at 120 fps, running QTM 2.17 build 4,000, interfaced to custom SciPy 0.17.0 code using the Qualisys 1.9 Realtime API) to track body orientation and limb motion.
- Full pipeline: dimensionality reduction/clustering [SciPy v0.17.0] -> stage not stated [Matplotlib]

### Adaptive exchange sustains cullin-RING ubiquitin ligase networks and proper licensing of DNA replication. (PNAS 2022)

- DOI: 10.1073/pnas.2205608119 | PMCID: PMC9456757 | PMID: 36037385
- Version used: **0.17.0**
- Evidence: All additional CRISPR screen data analyses were performed in Python 2.7 using a combination of Numpy (v1.12.1), Pandas (v0.17.1), and Scipy (v0.17.0).
- Full pipeline: stage not stated [NumPy v1.12.1, Python v2.7, SciPy v0.17.0]

### Taxonomic classification of DNA sequences beyond sequence similarity using deep neural networks. (PNAS 2022)

- DOI: 10.1073/pnas.2122636119 | PMCID: PMC9436379 | PMID: 36018838
- Version used: **1.6.1**
- Evidence: BERTax was implemented in Python 3.7 and uses the Python packages scipy (1.6.1) ( 40 ), keras (2.4.3), tensorflow (2.4.1) ( 41 ), numpy (1.19.2) ( 42 ), and keras-bert (0.86.0).
- Full pipeline: stage not stated [Kraken2, NumPy v1.19.2, Python v3.7, SciPy v1.6.1, minimap2]

### Optimizing the human learnability of abstract network representations. (PNAS 2022)

- DOI: 10.1073/pnas.2121338119 | PMCID: PMC9436382 | PMID: 35994661
- Evidence: For some target transition structure A , the optimal input structure A in = A * was determined by using the dual-annealing optimization method in scipy , with D K L ( A | | f ( A in ) ) as the cost function.
- Full pipeline: stage not stated [Python, SciPy]

### Repertoire-scale measures of antigen binding. (PNAS 2022)

- DOI: 10.1073/pnas.2203505119 | PMCID: PMC9407674 | PMID: 35969768
- Version used: **1.4.1**
- Evidence: Recon v3.0 was performed using Python 3.7.6 with NumPy version 1.18.0 and SciPy version 1.4.1.
- Full pipeline: machine learning [scikit-learn] -> stage not stated [NumPy v1.18.0, PyMOL v2.2, Python v3.7.6, SciPy v1.4.1]

### Integrated AlphaFold2 and DEER investigation of the conformational dynamics of a pH-dependent APC antiporter. (PNAS 2022)

- DOI: 10.1073/pnas.2206129119 | PMCID: PMC9407458 | PMID: 35969794
- Evidence: Following quantitation, data were analyzed using Michaelis-Menten kinetics using the curve_fit function implemented in SciPy ( 101 ).
- Full pipeline: quantification [ImageJ v1.53] -> structure determination [OpenMM] -> stage not stated [AlphaFold v2.0.1, ColabFold, SciPy]

### A neural network solves, explains, and generates university math problems by program synthesis and few-shot learning at human level. (PNAS 2022)

- DOI: 10.1073/pnas.2123433119 | PMCID: PMC9371704 | PMID: 35917350
- Evidence: Around half of the courses use math, random, and SciPy.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Matplotlib, NumPy, Python, SciPy]

### Random encounters and amoeba locomotion drive the predation of &lt;i&gt;Listeria monocytogenes&lt;/i&gt; by &lt;i&gt;Acanthamoeba castellanii&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2122659119 | PMCID: PMC9371647 | PMID: 35914149
- Evidence: Prior to tracking of the Listeria cells with Trackpy ( 53 ), two dynamic masks (an Acanthamoeba mask and an interaction mask for each individual frame) were created for each region of interest using mathematical operations from the OpenCV ( 55 ) and SciPy ( 56 ) modules ( Fig.
- Full pipeline: stage not stated [ImageJ, OpenCV, Python, SciPy]

### Evolution and folding of repeat proteins. (PNAS 2022)

- DOI: 10.1073/pnas.2204131119 | PMCID: PMC9351489 | PMID: 35905321
- Evidence: We used scipy library curve_fit to fit and get σ T f , which we used as T f errors.
- Full pipeline: differential/statistical testing [scikit-learn] -> machine learning [scikit-learn] -> stage not stated [SciPy]

### Natural Evolution Provides Strong Hints about Laboratory Evolution of Designer Enzymes. (PNAS 2022)

- DOI: 10.1073/pnas.2207904119 | PMCID: PMC9351539 | PMID: 35901204
- Version used: **1.0**
- Evidence: 2 B ), respectively. [The correlation values reported in this work are all Pearson correlation with P value from the two-tailed test calculated using SciPy 1.0 ( 32 ).] The strong correlation is unexpected because no known natural enzymes catalyze Kemp elimination.
- Full pipeline: differential/statistical testing [SciPy v1.0]

### Archaeal lipids trace ecology and evolution of marine ammonia-oxidizing archaea. (PNAS 2022)

- DOI: 10.1073/pnas.2123193119 | PMCID: PMC9351445 | PMID: 35905325
- Evidence: For ODR regressions, we used scipy.ODR module from the SciPy library ( 100 ).
- Full pipeline: dimensionality reduction/clustering [Jupyter] -> differential/statistical testing [Jupyter, Python, SciPy, scikit-learn] -> visualisation [Jupyter]

### Mass spectrometry imaging to explore molecular heterogeneity in cell culture. (PNAS 2022)

- DOI: 10.1073/pnas.2114365119 | PMCID: PMC9303856 | PMID: 35858333
- Evidence: The binary MALDI images were used as the kernel for a two-dimensional correlation (1-µm step size) with the binary microscopy images (using scipy.signal.correlate2d).
- Full pipeline: normalisation [scikit-learn v0.21.3] -> dimensionality reduction/clustering [SciPy] -> stage not stated [Python, scikit-image v0.14.0]

### Deep learning of dynamically responsive chemical Hamiltonians with semiempirical quantum mechanics. (PNAS 2022)

- DOI: 10.1073/pnas.2120333119 | PMCID: PMC9271210 | PMID: 35776544
- Evidence: The other models use the L-BFGS-B optimizer in SciPy with a tolerance of 10 –3 eV/Å ( 55 ).
- Full pipeline: simulation/modelling [TensorFlow] -> machine learning [TensorFlow] -> stage not stated [PyTorch, RDKit, SciPy]

### Nonequilibrium statistical thermodynamics of multicomponent interfaces. (PNAS 2022)

- DOI: 10.1073/pnas.2121405119 | PMCID: PMC9214509 | PMID: 35675427
- Evidence: Analysis of the simulation data was performed using the Pandas ( 50 ), NumPy ( 51 ), SciPy ( 52 ), and CSAPS ( 53 ) Python packages.
- Full pipeline: simulation/modelling [NumPy, SciPy]

### A male pheromone that improves the quality of the oogenic germline. (PNAS 2022)

- DOI: 10.1073/pnas.2015576119 | PMCID: PMC9173808 | PMID: 35576466
- Evidence: The hypergeometric P value and other calculations were carried out using SciPy ( 83 ) version 1.6.2 and NumPy ( 84 ) version 1.19.2.
- Full pipeline: quality control [MultiQC, Nextflow] -> differential/statistical testing [DESeq2 v1.32.0, NumPy, R v4.1, SciPy] -> stage not stated [Matplotlib, seaborn]

### Geometric control of topological dynamics in a singing saw. (PNAS 2022)

- DOI: 10.1073/pnas.2117241119 | PMCID: PMC9169918 | PMID: 35446615
- Evidence: The smoothed average time series is then fit to an exponential function with a constant offset using SciPy’s in-built nonlinear curve fitting function.
- Full pipeline: stage not stated [Matplotlib, SciPy]

### Infrastructure inequality is a characteristic of urbanization. (PNAS 2022)

- DOI: 10.1073/pnas.2119890119 | PMCID: PMC9169802 | PMID: 35377809
- Evidence: We analyzed the data in R ( https://www.r-project.org/ ) using ggplot2, sf, rgdal, Hmisc, spdep, spatialreg, raster, tmap, and dplyr packages and in python ( https://www.python.org/ ) programming languages using numpy, scipy, pandas, geopandas, osgeo, scikit-image, matplotlib, and rasterio packages.
- Full pipeline: stage not stated [Matplotlib, NumPy, R, SciPy, ggplot2, scikit-image, tidyverse]

### Cellular and transcriptional diversity over the course of human lactation. (PNAS 2022)

- DOI: 10.1073/pnas.2121720119 | PMCID: PMC9169737 | PMID: 35377806
- Evidence: After clustering and merging, we represented the diversity of epithelial cells within each sample using Shannon entropy implemented with the Python function scipy.stats.entropy ( SI Appendix , Fig.
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [DESeq2, SciPy, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [Enrichr, R v3.6.2, Scanpy, Seurat, scDblFinder]

### Face neurons encode nonsemantic features. (PNAS 2022)

- DOI: 10.1073/pnas.2118705119 | PMCID: PMC9169805 | PMID: 35377737
- Evidence: P values associated with Pearson’s r (experiment 6) were calculated using the exact distribution for the null hypothesis that the two variables were drawn from a bivariate normal distribution with zero covariance, as implemented in the Python library “scipy” ( 37 ).
- Full pipeline: differential/statistical testing [SciPy, statsmodels]

### Contiguously hydrophobic sequences are functionally significant throughout the human exome. (PNAS 2022)

- DOI: 10.1073/pnas.2116267119 | PMCID: PMC8944643 | PMID: 35294280
- Evidence: We compute the probability of observing a count as extreme as n (two-tailed) given f using the python scipy ( 68 ) function scipy.stats.binom_test( n , N , f ,alternative= “two-sided”).
- Full pipeline: simulation/modelling [VMD] -> stage not stated [Matplotlib, NumPy, Python v3.6, SciPy]

### A system for multiplexed selection of aptamers with exquisite specificity without counterselection. (PNAS 2022)

- DOI: 10.1073/pnas.2119945119 | PMCID: PMC8944265 | PMID: 35290115
- Evidence: Curve fitting was performed in Python using the “curve_fit” function from the “scipy” library.
- Full pipeline: stage not stated [Python, SciPy]

### Reimport of carbon from cytosolic and vacuolar sugar pools into the Calvin-Benson cycle explains photosynthesis labeling anomalies. (PNAS 2022)

- DOI: 10.1073/pnas.2121531119 | PMCID: PMC8931376 | PMID: 35259011
- Evidence: A nonlinear ordinary least-squares algorithm implemented in the Python package SciPy was used to fit models 1 to 7 ( Fig.
- Full pipeline: stage not stated [SciPy]

### Scaling laws in enzyme function reveal a new kind of biochemical universality. (PNAS 2022)

- DOI: 10.1073/pnas.2106655119 | PMCID: PMC8892295 | PMID: 35217602
- Evidence: We used the module scipy.integrate.simps of the Python package SciPy for the implementation of Simpson’s rule.
- Full pipeline: differential/statistical testing [Python] -> stage not stated [SciPy]

### Label-free sensing of cells with fluorescence lifetime imaging: The quest for metabolic heterogeneity. (PNAS 2022)

- DOI: 10.1073/pnas.2118241119 | PMCID: PMC8892511 | PMID: 35217616
- Evidence: All simulation and data analysis were performed using custom-build Python 3.7 scripts with the use of Numpy, Scipy, Scikit-Learn Matplotlib, Pandas and LmFit modules.
- Full pipeline: simulation/modelling [Matplotlib, NumPy, Python v3.7, SciPy] -> stage not stated [scikit-learn]

### <i>Mycobacterium tuberculosis</i> DNA repair helicase UvrD1 is activated by redox-dependent dimerization via a 2B domain cysteine. (PNAS 2022)

- DOI: 10.1073/pnas.2114501119 | PMCID: PMC8872793 | PMID: 35173050
- Evidence: Python 3 was installed via Anaconda along with modules such as numpy, scipy, matpotlib, lmfit, emcee, corner, os, and pandas, and then the globalfit model was used to fit the data for unwinding using the n-step unwinding model and translocation using a two-step dissociation model ( 64 ).
- Full pipeline: stage not stated [Conda, NumPy, Python, SciPy, emcee]

### Intersecting kinematic encoding and readout of intention in autism. (PNAS 2022)

- DOI: 10.1073/pnas.2114648119 | PMCID: PMC8812545 | PMID: 35101921
- Evidence: The significance of correlation values was assessed using the scipy.stats Python module, with two-sided parametric Student statistics for Pearson correlation and two-sided permutation distribution for Spearman correlation ( 38 ).
- Full pipeline: differential/statistical testing [SciPy] -> stage not stated [PyTorch, R, lme4]

### In vitro cell cycle oscillations exhibit a robust and hysteretic response to changes in cytoplasmic density. (PNAS 2022)

- DOI: 10.1073/pnas.2109547119 | PMCID: PMC8832984 | PMID: 35101974
- Version used: **1.4.1**
- Evidence: For comparison with experimental curves, a logistic function was obtained from the simulation results via fitting using the function curve_fit from the package scipy 1.4.1.
- Full pipeline: differential/statistical testing [Python v3.7.10, scikit-learn v0.22.2] -> simulation/modelling [SciPy v1.4.1] -> stage not stated [ggplot2]

### Sector search strategies for odor trail tracking. (PNAS 2022)

- DOI: 10.1073/pnas.2107431118 | PMCID: PMC8740577 | PMID: 34983837
- Evidence: At each casting step, we optimize (using standard black box optimization methods using the SciPy library in Python) for Δ r = r − r ′ > 0 and θ by expanding Eq.
- Full pipeline: stage not stated [Python, SciPy]

### A synergy between mechanosensitive calcium- and membrane-binding mediates tension-sensing by C2-like domains. (PNAS 2022)

- DOI: 10.1073/pnas.2112390119 | PMCID: PMC8740744 | PMID: 34969839
- Evidence: Specifically, custom Python 3.7 scripts were written based on the Numpy ( 36 ), Scipy ( 37 ), Scikit-image ( 38 ), Allen Cell Structure Segmenter ( 39 ), Cellpose ( 40 ) and Napari libraries ( 41 ).
- Full pipeline: stage not stated [Cellpose, Conda, NumPy, PyMOL, Python v3.7, SciPy]

### High-throughput quantification of red blood cell deformability and oxygen saturation to probe mechanisms of sickle cell disease. (PNAS 2023)

- DOI: 10.1073/pnas.2313755120 | PMCID: PMC10691249 | PMID: 37983504
- Evidence: The fitting was performed using the Python SciPy package.
- Full pipeline: stage not stated [Python, SciPy]

### Machine-guided discovery of a real-world rogue wave model. (PNAS 2023)

- DOI: 10.1073/pnas.2306275120 | PMCID: PMC10691345 | PMID: 37983488
- Evidence: This publication was made possible by the following opensource software stack: JAX ( 57 ), flax ( 58 ), optax ( 59 ), PySR ( 9 ), scikit-learn ( 63 ), PyALE ( 64 ), NumPy ( 65 ), SciPy ( 66 ), matplotlib ( 67 ), Seaborn ( 68 ), pandas ( 69 ), and Jupyter ( 70 ).
- Full pipeline: stage not stated [Jupyter, Matplotlib, NumPy, SciPy, scikit-learn, seaborn]

### Rats respond to aversive emotional arousal of human handlers with the activation of the basolateral and central amygdala. (PNAS 2023)

- DOI: 10.1073/pnas.2302655120 | PMCID: PMC10655214 | PMID: 37934822
- Evidence: For statistical analysis, we used the Scipy package version 1.9.3, specifically running a mixed model ANOVA which included one between-subject factor (Group) and one within-subject factor (Stimulus).
- Full pipeline: registration [AFNI, FSL v5.0.9] -> differential/statistical testing [SciPy] -> stage not stated [ANTs v2.2.0, ImageJ, Nilearn v0.5.2, Nipype v1.2.0, fMRIPrep v1.4.0]

### Interspecies interactions determine growth dynamics of biopolymer-degrading populations in microbial communities. (PNAS 2023)

- DOI: 10.1073/pnas.2305198120 | PMCID: PMC10622921 | PMID: 37878716
- Evidence: Pre-existing linear or exponential regression models from SciPy Stats v1.11.1 were applied in python v3.9 to determine relationships between independent measures.
- Full pipeline: differential/statistical testing [SciPy] -> stage not stated [Python v3.7]

### Universal abundance fluctuations across microbial communities, tropical forests, and urban populations. (PNAS 2023)

- DOI: 10.1073/pnas.2215832120 | PMCID: PMC10622915 | PMID: 37874854
- Evidence: The data were fit and parameters were estimated by maximum likelihood estimation from the Scipy package in Python.
- Full pipeline: stage not stated [Python, SciPy]

### The lack of negative association between TE load and subgenome dominance in synthesized <i>Brassica</i> allotetraploids. (PNAS 2023)

- DOI: 10.1073/pnas.2305208120 | PMCID: PMC10589682 | PMID: 37816049
- Evidence: We also used the non-parametric statistical test of the Mann-Whitney-U test ( 65 ) in the Python package SciPy to identify the significance of differentially expressed gene pairs from a subset of genes.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [featureCounts] -> differential/statistical testing [R, SciPy] -> stage not stated [Bismark, Bowtie2, RepeatMasker v4.0.3]

### Deciphering RNA splicing logic with interpretable machine learning. (PNAS 2023)

- DOI: 10.1073/pnas.2221165120 | PMCID: PMC10576025 | PMID: 37796983
- Evidence: To avoid reporting redundant sequence filters, hierarchical clustering using SciPy ( 51 ) was applied.
- Full pipeline: dimensionality reduction/clustering [SciPy] -> stage not stated [NumPy v1.20, Python v3.8, TensorFlow v2.6]

### Intrinsic structural dynamics dictate enzymatic activity and inhibition. (PNAS 2023)

- DOI: 10.1073/pnas.2310910120 | PMCID: PMC10576142 | PMID: 37782780
- Evidence: The differential equations describing the dynamics of the system were setup and solved numerically using the scipy ( 72 ) function odeint.
- Full pipeline: differential/statistical testing [SciPy]

### Circadian ribosome profiling reveals a role for the <i>Period2</i> upstream open reading frame in sleep. (PNAS 2023)

- DOI: 10.1073/pnas.2214636120 | PMCID: PMC10556633 | PMID: 37769257
- Version used: **1.7**
- Evidence: Lomb–Scargle periodograms were implemented using SciPy version 1.7, and cosinor analysis was implemented using CosinorPy ( 73 ).
- Full pipeline: differential/statistical testing [Jupyter, R v3.4.3] -> stage not stated [SciPy v1.7]

### Multidisciplinary learning through collective performance favors decentralization. (PNAS 2023)

- DOI: 10.1073/pnas.2303568120 | PMCID: PMC10450670 | PMID: 37579171
- Version used: **1.9.0**
- Evidence: Data, Materials, and Software Availability The model and analysis code for this work were developed with Python 3.9.5, Numpy 1.21.6, Scipy 1.9.0, Pandas 1.4.2, NetworkX 2.8.3, Dask 2022.4.1, Statsmodels 0.13.2, Scikit-learn 1.0.2, Matplotlib 3.5.2, and Seaborn 0.11.2.
- Full pipeline: stage not stated [Dask v2022.4.1, Matplotlib v3.5.2, NetworkX v2.8.3, NumPy v1.21.6, Python v3.9.5, SciPy v1.9.0, scikit-learn v1.0.2, seaborn v0.11.2]

### Detecting dynamic domains and local fluctuations in complex molecular systems via timelapse neighbors shuffling. (PNAS 2023)

- DOI: 10.1073/pnas.2300565120 | PMCID: PMC10372573 | PMID: 37467266
- Evidence: To reduce the noise in each δ i (t) signal, we processed them by using a Savitzky–Golay ( 85 ) filter [as implemented in the SciPy python package ( 86 )], obtaining smoothed ⟨ δ i ( t )⟩ signals.
- Full pipeline: simulation/modelling [GROMACS, LAMMPS] -> machine learning [LAMMPS] -> stage not stated [SciPy]

### 3D surface reconstruction of cellular cryo-soft X-ray microscopy tomograms using semisupervised deep learning. (PNAS 2023)

- DOI: 10.1073/pnas.2209938120 | PMCID: PMC10268598 | PMID: 37276395
- Evidence: The implementation from the SciPy package has been used for this purpose ( 71 ).
- Full pipeline: alignment/mapping [IMOD] -> structure determination [IMOD] -> machine learning [TensorFlow] -> stage not stated [SciPy]

### Cortical activity emerges in region-specific patterns during early brain development. (PNAS 2023)

- DOI: 10.1073/pnas.2208654120 | PMCID: PMC10235933 | PMID: 37216522
- Evidence: Quantitative analysis was performed using custom code written in Python and using NumPy, SciPy, Scikit-learn, Pandas, NetworkX, Python-Louvain, Filterpy and Scikit-image.
- Full pipeline: quantification [ImageJ] -> normalisation [Python] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [Matplotlib] -> stage not stated [NetworkX, NumPy, SciPy]

### Marginal specificity in protein interactions constrains evolution of a paralogous family. (PNAS 2023)

- DOI: 10.1073/pnas.2221163120 | PMCID: PMC10160972 | PMID: 37098061
- Evidence: For each variant, the mean frequencies in each bin across three replicates and SD were used to fit Gaussian functions to each distribution [in log 10 (GFP units)], from both the on and off sorts (SciPy optimize package).
- Full pipeline: alignment/mapping [HMMER] -> stage not stated [Python, SciPy]

### Fragmentation landscape of cell-free DNA revealed by deconvolutional analysis of end motifs. (PNAS 2023)

- DOI: 10.1073/pnas.2220982120 | PMCID: PMC10151549 | PMID: 37075072
- Evidence: NNLS was implemented based on the Python function of scipy.optimize.nnls (v1.8.1).
- Full pipeline: stage not stated [SciPy, scikit-learn]

### Johari-Goldstein <i>β</i> relaxation in glassy dynamics originates from two-scale energy landscape. (PNAS 2023)

- DOI: 10.1073/pnas.2215153120 | PMCID: PMC10083593 | PMID: 36989301
- Evidence: The eigenvalue problem of ℳ is solved numerically using the SciPy package ( 71 ).
- Full pipeline: stage not stated [NumPy, SciPy]

### Augmenting astrophysical scaling relations with machine learning: Application to reducing the Sunyaev-Zeldovich flux-mass scatter. (PNAS 2023)

- DOI: 10.1073/pnas.2202074120 | PMCID: PMC10041100 | PMID: 36930602
- Evidence: We use the scipy.fit package and find the following best-fit relations: M ∝ Y 0.59 ± 0.002 and M ∝ Y 0.618 ± 0.002 (1 − [0.61 ± 0.02] c gas ).
- Full pipeline: simulation/modelling [AREPO] -> stage not stated [SciPy]

### KMT2D acetylation by CREBBP reveals a cooperative functional interaction at enhancers in normal and malignant germinal center B cells. (PNAS 2023)

- DOI: 10.1073/pnas.2218330120 | PMCID: PMC10089214 | PMID: 36893259
- Evidence: Statistics were calculated using R 4.2.2 and the SciPy Python library.
- Full pipeline: alignment/mapping [HISAT2, featureCounts v1.6.3] -> quantification [ImageJ, featureCounts v1.6.3] -> normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v4.2, SciPy] -> stage not stated [GSEA, HOMER]

### SIK3-HDAC4 in the suprachiasmatic nucleus regulates the timing of arousal at the dark onset and circadian period in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2218209120 | PMCID: PMC10089210 | PMID: 36877841
- Evidence: Bioluminescence values were detrended by subtracting 24-h moving average values, and then data were smoothened with a Savitzky–Golay filter (12-h window, cubic polynomial) in SciPy.
- Full pipeline: stage not stated [SciPy]

### Elucidation of a dynamic interplay between a beta-2 adrenergic receptor, its agonist, and stimulatory G protein. (PNAS 2023)

- DOI: 10.1073/pnas.2215916120 | PMCID: PMC10013855 | PMID: 36853938
- Evidence: This matrix was then used to calculate a linkage matrix by the hierarchical cluster linkage function of the SciPy package ( 91 ).
- Full pipeline: alignment/mapping [UCSF Chimera] -> dimensionality reduction/clustering [SciPy] -> simulation/modelling [NAMD, VMD]

### State- and stimulus-specific dynamics of SMAD signaling determine fate decisions in individual cells. (PNAS 2023)

- DOI: 10.1073/pnas.2210891120 | PMCID: PMC10013741 | PMID: 36857347
- Evidence: 5 B and D ) was calculated using the least_squares function from the scipy.optimize Python package.
- Full pipeline: stage not stated [CellProfiler, SciPy]

### Closed-loop network of skin-interfaced wireless devices for quantifying vocal fatigue and providing user feedback. (PNAS 2023)

- DOI: 10.1073/pnas.2219394120 | PMCID: PMC9992836 | PMID: 36802437
- Evidence: All analyses used Python 3.0 with SciPy and TensorFlow packages.
- Full pipeline: stage not stated [Python v3.0, SciPy, TensorFlow]

### Data-driven predictions of the time remaining until critical global warming thresholds are reached. (PNAS 2023)

- DOI: 10.1073/pnas.2207183120 | PMCID: PMC9963891 | PMID: 36716375
- Evidence: To test the sensitivity of our predicted time-to-threshold to the definition of the temperature threshold, we repeat our analysis replacing the forced response with a 15-y smoothing of the ensemble-mean time series (using the scipy.signal.savgol_filter with a window length of 15 y and polynomial of order 3).
- Full pipeline: machine learning [TensorFlow v2.7.0] -> stage not stated [SciPy]

### Charge transfer as a mechanism for chlorophyll fluorescence concentration quenching. (PNAS 2023)

- DOI: 10.1073/pnas.2210811120 | PMCID: PMC9945999 | PMID: 36689657
- Evidence: 3 and values of the mean μ and standard deviation σ obtained by fitting the sampled Δ E distribution to a normal distribution using the norm function in the scipy.stats package ( 44 ).
- Full pipeline: simulation/modelling [OpenMM] -> stage not stated [SciPy]

### Inferring the T cell repertoire dynamics of healthy individuals. (PNAS 2023)

- DOI: 10.1073/pnas.2207516120 | PMCID: PMC9942919 | PMID: 36669107
- Evidence: The maximization is performed using the minimize function from the Scipy package, with the Sequential Least Squares Programming (SLSQP) method ( 55 ) with parameters tol=1e-8 and maxiter=300 and initial condition τ = 2, θ = .5 and constraint θ −1 > 10 −3 .
- Full pipeline: stage not stated [SciPy]

### MITE infestation accommodated by genome editing in the germline genome of the ciliate &lt;i&gt;Blepharisma&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2213985120 | PMCID: PMC9942856 | PMID: 36669106
- Evidence: Peak calling on the graph of number of IESs (TA-bound only) vs. length (bp) was performed with the function find_peaks from the Python package scipy.signal v1.3.1 ( 83 ), with height cutoff 100.
- Full pipeline: alignment/mapping [AUGUSTUS, Bowtie2 v2.4.2, MAFFT v7.450, SAMtools v1.10, minimap2 v2.17] -> dimensionality reduction/clustering [RepeatMasker v2.0.1, SAMtools v1.10] -> machine learning [MAFFT v7.450] -> stage not stated [SciPy, featureCounts v2.0.1]

### Microbial population dynamics decouple growth response from environmental nutrient concentration. (PNAS 2023)

- DOI: 10.1073/pnas.2207295120 | PMCID: PMC9926246 | PMID: 36598949
- Evidence: We numerically integrate these equations using standard algorithms in Scipy ( 85 ) ( SI Appendix , section S4 ).
- Full pipeline: stage not stated [SciPy]

### Nutrient colimitation is a quantitative, dynamic property of microbial populations. (PNAS 2024)

- DOI: 10.1073/pnas.2400304121 | PMCID: PMC11670248 | PMID: 39693349
- Evidence: We performed all numerical calculations in Python version 3.10.9, using tools from NumPy ( 76 ) version 1.24.1 and SciPy ( 77 ) version 1.10.0.
- Full pipeline: stage not stated [Matplotlib, NumPy, Python v3.10.9, SciPy]

### Temporal control of acute protein aggregate turnover by UBE3C and NRF1-dependent proteasomal pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2417390121 | PMCID: PMC11648907 | PMID: 39636856
- Evidence: 9.4.1; RRID:SCR_002798) or using python scipy package (RRID:SCR_008058).
- Full pipeline: stage not stated [SciPy]

### Magnetochrome-catalyzed oxidation of ferrous iron by MamP enables magnetite crystal growth in the magnetotactic bacterium AMB-1. (PNAS 2024)

- DOI: 10.1073/pnas.2410245121 | PMCID: PMC11648623 | PMID: 39621904
- Evidence: Determination of peak position and particle size was performed following an established methodology with an in-house Python-based script exploiting the Scipy library.
- Full pipeline: stage not stated [ImageJ, SciPy]

### Diversification of pectoral control through motor pool extension. (PNAS 2024)

- DOI: 10.1073/pnas.2413415121 | PMCID: PMC11626184 | PMID: 39602261
- Evidence: Statistics were performed using the scipy library [1.13.1, ( 46 )]. µCT Scanning and 3D Tissue Reconstruction.
- Full pipeline: differential/statistical testing [SciPy] -> structure determination [SciPy] -> stage not stated [Matplotlib, NumPy, Python, seaborn]

### Molecular insights into the interaction between a disordered protein and a folded RNA. (PNAS 2024)

- DOI: 10.1073/pnas.2409139121 | PMCID: PMC11626198 | PMID: 39589885
- Evidence: The data were fit assuming a 1:1 binding model using nonlinear minimization in SciPy and Python, which is described in detail in SI Appendix .
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [SciPy]

### Homeotic and nonhomeotic patterns in the tetrapod vertebral formula. (PNAS 2024)

- DOI: 10.1073/pnas.2411421121 | PMCID: PMC11588047 | PMID: 39527744
- Evidence: After smoothing the data, we used the find_peaks function from the Python scipy signal library ( 106 ) to detect peaks with a prominence larger than one SD of the signal.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> stage not stated [BLAST, BUSCO, SciPy, phytools]

### Bioenergetic suppression by redox-active metabolites promotes antibiotic tolerance in &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2406555121 | PMCID: PMC11573671 | PMID: 39503891
- Version used: **1.9.3**
- Evidence: Data were analyzed and processed in Python 3.8.17 using Pandas 2.0.3, NumPy 1.24.3, and SciPy 1.9.3.
- Full pipeline: stage not stated [ImageJ v1.52, NumPy v1.24.3, Python v3.8.17, SciPy v1.9.3]

### Atomic view of photosynthetic metabolite permeability pathways and confinement in synthetic carboxysome shells. (PNAS 2024)

- DOI: 10.1073/pnas.2402277121 | PMCID: PMC11551347 | PMID: 39485798
- Evidence: Particle tracking and analysis was performed with python-enabled VMD ( 70 ), extensively using numpy ( 74 ), scipy ( 75 ), and Matplotlib ( 76 ) libraries.
- Full pipeline: simulation/modelling [GROMACS, NAMD v2.14, VMD] -> stage not stated [Matplotlib, NumPy, SciPy]

### The conformational landscape of fold-switcher KaiB is tuned to the circadian rhythm timescale. (PNAS 2024)

- DOI: 10.1073/pnas.2412293121 | PMCID: PMC11551320 | PMID: 39475637
- Evidence: Spearman correlations between actual and predicted chemical shifts were calculated using SciPy ( 52 ).
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> stage not stated [ColabFold, SciPy]

### Seawater alkalization via an energy-efficient electrochemical process for CO&lt;sub&gt;2&lt;/sub&gt; capture. (PNAS 2024)

- DOI: 10.1073/pnas.2410841121 | PMCID: PMC11551434 | PMID: 39467125
- Evidence: The one-way ANOVA was conducted by using the Scipy library (version 1.3.1) in Python.
- Full pipeline: stage not stated [Python, SciPy]

### Protein language models learn evolutionary statistics of interacting sequence motifs. (PNAS 2024)

- DOI: 10.1073/pnas.2406285121 | PMCID: PMC11551344 | PMID: 39467119
- Evidence: The Spearman correlation is calculated in SciPy ( 37 ).
- Full pipeline: alignment/mapping [PyMOL] -> stage not stated [AlphaFold, ColabFold, SciPy]

### AlphaFold-Multimer accurately captures interactions and dynamics of intrinsically disordered protein regions. (PNAS 2024)

- DOI: 10.1073/pnas.2406407121 | PMCID: PMC11536093 | PMID: 39446390
- Evidence: Finding local maxima (peaks) of minD was done by a simple comparison of neighboring values through the use of the scipy.signal.find_peaks function.
- Full pipeline: machine learning [AlphaFold] -> visualisation [PyMOL] -> stage not stated [ColabFold, Matplotlib, NumPy, RoseTTAFold, SciPy, seaborn]

### Hyperspectral oblique plane microscopy enables spontaneous, label-free imaging of biological dynamic processes in live animals. (PNAS 2024)

- DOI: 10.1073/pnas.2404232121 | PMCID: PMC11513980 | PMID: 39401353
- Evidence: The data were randomly shuffled and preprocessed, which included removing the linear trend (using scipy.signal.detrend) of the spectra, subtracting the mean, normalizing to the maximum and finally cropping to the range of 560 cm − 1 to 3,360 cm − 1 .
- Full pipeline: normalisation [SciPy] -> visualisation [ImageJ]

### The pace of change of summertime temperature extremes. (PNAS 2024)

- DOI: 10.1073/pnas.2406143121 | PMCID: PMC11494304 | PMID: 39374381
- Evidence: For the gridbox trends, the two-sided p-value is estimated using the scipy.stats.linregress function, which uses the Wald Test with t-distribution of the test statistic.
- Full pipeline: differential/statistical testing [SciPy]

### Minimal motifs for habituating systems. (PNAS 2024)

- DOI: 10.1073/pnas.2409330121 | PMCID: PMC11474051 | PMID: 39365818
- Evidence: Unless otherwise specified, the numerical trajectories are obtained in Python 3.9.6 using either direct convolution or an implicit Runge–Kutta scheme via the SciPy library.
- Full pipeline: simulation/modelling [Python v3.9.6, SciPy]

### Coupling of cell growth modulation to asymmetric division and cell cycle regulation in &lt;i&gt;Caulobacter crescentus&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2406397121 | PMCID: PMC11474046 | PMID: 39361646
- Evidence: For the Mann–Whitney U tests, P -values were calculated using the built-in MATLAB function ranksum, or the mannwhitneyu function from the scipy.stats module of the SciPy Python library.
- Full pipeline: machine learning [Python] -> stage not stated [SciPy]

### Synaptic weight dynamics underlying memory consolidation: Implications for learning rules, circuit organization, and circuit function. (PNAS 2024)

- DOI: 10.1073/pnas.2406010121 | PMCID: PMC11474072 | PMID: 39365821
- Evidence: All simulations were performed in Python by integrating the differential equations for the learning rules with the Radau solver (implemented in solve_ivp in the scipy.integrate package).
- Full pipeline: differential/statistical testing [Python, SciPy] -> simulation/modelling [Python, SciPy]

### Snowmelt duration controls red algal blooms in the snow of the European Alps. (PNAS 2024)

- DOI: 10.1073/pnas.2400362121 | PMCID: PMC11474047 | PMID: 39312681
- Evidence: We tested multiple supervised machine learning methods to classify pixels in the GBND-RGND space using scipy in Python, namely, nearest neighbors, linear support vector machine (linear SVM), Gaussian process, decision tree, random forest, and neural network.
- Full pipeline: normalisation [Matplotlib] -> machine learning [Python, SciPy] -> visualisation [Matplotlib] -> stage not stated [BLAST]

### COVID-19 lockdown effects on adolescent brain structure suggest accelerated maturation that is more pronounced in females than in males. (PNAS 2024)

- DOI: 10.1073/pnas.2403200121 | PMCID: PMC11420155 | PMID: 39250666
- Evidence: After all Z-scores were calculated, a single-sample t test was performed for each brain region and sex using the “stats” function of the SciPy Python library [v.
- Full pipeline: structure determination [FreeSurfer] -> stage not stated [SciPy, scikit-learn]

### Range expansions across landscapes with quenched noise. (PNAS 2024)

- DOI: 10.1073/pnas.2411487121 | PMCID: PMC11348022 | PMID: 39136984
- Evidence: Fastest paths are computed using the Floyd–Warshall algorithm implemented in the Python SciPy package ( 58 ).
- Full pipeline: stage not stated [SciPy]

### Circadian period is compensated for repressor protein turnover rates in single cells. (PNAS 2024)

- DOI: 10.1073/pnas.2404738121 | PMCID: PMC11348271 | PMID: 39141353
- Evidence: Cells were tracked, and monoexponential decay curves were fitted to time points 3 to 16 of the individual cell time series using the Python package scipy.optimze.curve_fit and Eq.
- Full pipeline: quality control [Python] -> stage not stated [CellProfiler, SciPy]

### MAVS Cys508 palmitoylation promotes its aggregation on the mitochondrial outer membrane and antiviral innate immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2403392121 | PMCID: PMC11348129 | PMID: 39141356
- Evidence: The overlaid histogram with fitted Gaussian distribution was plotted using python script based on python packages Matplotlib and SciPy.
- Full pipeline: quantification [CellProfiler, ImageJ] -> visualisation [Matplotlib, SciPy] -> stage not stated [Fiji]

### Lack of evidence for direct ligand-gated ion channel activity of GluD receptors. (PNAS 2024)

- DOI: 10.1073/pnas.2406655121 | PMCID: PMC11295041 | PMID: 39052831
- Evidence: Statistical analysis was performed using Python mannwhitneyu from scipy.stats, using method = “exact” or using stats.kruskal and posthoc_dunn with Bonferroni p_adjust.
- Full pipeline: differential/statistical testing [SciPy]

### GABA&lt;sub&gt;A&lt;/sub&gt; receptor subunit composition regulates circadian rhythms in rest-wake and synchrony among cells in the suprachiasmatic nucleus. (PNAS 2024)

- DOI: 10.1073/pnas.2400339121 | PMCID: PMC11295074 | PMID: 39047036
- Evidence: We measured intensities by implementing a multidimensional Gaussian filter in SciPy tools using established methods ( 61 ) to generate time series of pixel intensities.
- Full pipeline: dimensionality reduction/clustering [SciPy] -> stage not stated [Python]

### Direct observation correlates NFκB cRel in B cells with activating and terminating their proliferative program. (PNAS 2024)

- DOI: 10.1073/pnas.2309686121 | PMCID: PMC11287273 | PMID: 39024115
- Evidence: 2 C ), using the built-in optimization algorithm in the SciPy.stats package to scan parameters and minimize deviations between fit and data.
- Full pipeline: stage not stated [SciPy]

### Breakthrough-induced loop formation in evolving transport networks. (PNAS 2024)

- DOI: 10.1073/pnas.2401200121 | PMCID: PMC11260131 | PMID: 38985758
- Evidence: Finally, the velocity was smoothed using the Savitzky–Golay filter (function savgol_filter from the Scipy package).
- Full pipeline: stage not stated [SciPy]

### Measuring and modeling the dynamics of mitotic error correction. (PNAS 2024)

- DOI: 10.1073/pnas.2323009121 | PMCID: PMC11194551 | PMID: 38875144
- Evidence: We used Scipy’s curve_fit function on the summed squared residuals for each bin to fit the parameter combinations k b , k b / ( k b + k e ) , and ( C tot - C E , init ) / C tot .
- Full pipeline: stage not stated [NumPy, Python, SciPy]

### Information content and optimization of self-organized developmental systems. (PNAS 2024)

- DOI: 10.1073/pnas.2322326121 | PMCID: PMC11161761 | PMID: 38819997
- Evidence: To find optimal fate thresholds, we use scipy’s differential evolution optimizer ( 89 ).
- Full pipeline: differential/statistical testing [SciPy] -> simulation/modelling [NumPy]

### Biophysical principles predict fitness of SARS-CoV-2 variants. (PNAS 2024)

- DOI: 10.1073/pnas.2314518121 | PMCID: PMC11161772 | PMID: 38820002
- Evidence: Model fitting was performed with nonlinear least square regression ( scipy.optimize package) on a randomly selected training set.
- Full pipeline: differential/statistical testing [SciPy] -> machine learning [SciPy]

### On the role of native contact cooperativity in protein folding. (PNAS 2024)

- DOI: 10.1073/pnas.2319249121 | PMCID: PMC11145220 | PMID: 38776371
- Evidence: We computed the total number of contacts C from PDB structures of each of the proteins in this list using mdtraj ( 54 ), from which linear regression using scipy ( 55 ) gave a relation to the number of residues in each protein, L , as [13] C = 2.534 L − 38.54 .
- Full pipeline: dimensionality reduction/clustering [AlphaFold] -> differential/statistical testing [MDTraj, SciPy]

### An encompassed representation of timescale hierarchies in first-order reaction network. (PNAS 2024)

- DOI: 10.1073/pnas.2317781121 | PMCID: PMC11126998 | PMID: 38758700
- Evidence: This grouping problem is equivalent to complete linkage problem, which can be solved by an efficient algorithm such as CLINK algorithm ( 51 ), and implemented in SciPy.cluster.hierarchy.linkage of Python SciPy package resulting in a dendrogram of indistinguishability.
- Full pipeline: dimensionality reduction/clustering [SciPy]

### A distinct, high-affinity, alkaline phosphatase facilitates occupation of P-depleted environments by marine picocyanobacteria. (PNAS 2024)

- DOI: 10.1073/pnas.2312892121 | PMCID: PMC11098088 | PMID: 38713622
- Version used: **1.10.1**
- Evidence: Activity curves were fitted using Python package Scipy 1.10.1 ( 67 ) to obtain the change in absorbance at 405 nm per minute.
- Full pipeline: alignment/mapping [IQ-TREE v1.6.3, MUSCLE v3.8.31] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, HMMER, SciPy v1.10.1]

### Robust inference of causality in high-dimensional dynamical processes from the Information Imbalance of distance ranks. (PNAS 2024)

- DOI: 10.1073/pnas.2317256121 | PMCID: PMC11087807 | PMID: 38687797
- Evidence: All the dynamical systems were integrated using the 8-th order explicit Runge–Kutta method DOP853 in the Python library SciPy, except for the coupled Lorenz 96 systems for which the SciPy implementation of the LSODA integrator was employed ( 49 ).
- Full pipeline: differential/statistical testing [Python, statsmodels] -> stage not stated [SciPy]

### Dissection and integration of bursty transcriptional dynamics for complex systems. (PNAS 2024)

- DOI: 10.1073/pnas.2306901121 | PMCID: PMC11067469 | PMID: 38669186
- Evidence: Then, to find the optimal kinetic parameters, the KL divergence is minimized using the Nelder–Mead algorithm implemented in SciPy ( 41 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [Python, SciPy, scVelo]

### Functional specialization of hippocampal somatostatin-expressing interneurons. (PNAS 2024)

- DOI: 10.1073/pnas.2306382121 | PMCID: PMC11047068 | PMID: 38640347
- Evidence: Scipy’s scipy.cluster.vq.kmeans2 function was used to distribute the dataset into two clusters using the K-means algorithm.
- Full pipeline: dimensionality reduction/clustering [SciPy] -> stage not stated [scikit-learn]

### Bmal1 integrates circadian function and temperature sensing in the suprachiasmatic nucleus. (PNAS 2024)

- DOI: 10.1073/pnas.2316646121 | PMCID: PMC11047078 | PMID: 38625943
- Evidence: Vectors of spatiotemporal progression of the clusters were calculated by linear regression of the center of mass of the clusters, using the center of mass function from the scipy multidimensional image processing package scipy.ndimage ( 43 ), followed by fitting a linear regression using scikit-learn 1.2.2v ( 41 ).
- Full pipeline: normalisation [Python, scikit-learn v1.2.2] -> dimensionality reduction/clustering [Matplotlib, Python, SciPy, scikit-learn v1.2.2] -> differential/statistical testing [SciPy]

### Toward vanishing droplet friction on repellent surfaces. (PNAS 2024)

- DOI: 10.1073/pnas.2315214121 | PMCID: PMC11047067 | PMID: 38621127
- Version used: **1.0**
- Evidence: The simulations were done by solving the drop’s equation of motion forward in time using Runge–Kutta of 4(5) order algorithm using Python package SciPy 1.0 ( 34 , 44 , 45 ).
- Full pipeline: simulation/modelling [SciPy v1.0]

### Formation of recurring transient Ca<sup>2+</sup>-based intercellular communities during <i>Drosophila</i> hematopoiesis. (PNAS 2024)

- DOI: 10.1073/pnas.2318155121 | PMCID: PMC11032476 | PMID: 38602917
- Evidence: Pearson correlation (scipy.stats.pearsonr) was used to measure the correlation between the Ca 2+ signals of blood progenitors ( Fig.
- Full pipeline: stage not stated [SciPy]

### Optimal reaching subject to computational and physical constraints reveals structure of the sensorimotor control system. (PNAS 2024)

- DOI: 10.1073/pnas.2319313121 | PMCID: PMC10998569 | PMID: 38551834
- Evidence: The system of differential equations comprising the equations of motion, neural and muscle dynamics, and adjoint equations was coded in python using the NumPy and SciPy numerical libraries and integrated using an adaptive fifth order Runge–Kutta method ( 41 , 42 ).
- Full pipeline: differential/statistical testing [NumPy, SciPy] -> machine learning [PyTorch]

### Unraveling sources of emission heterogeneity in Silicon Vacancy color centers with cryo-cathodoluminescence microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2308247121 | PMCID: PMC10998621 | PMID: 38551833
- Evidence: Data analysis was performed in Python, utilizing multiple common packages, such as numpy, scipy, and matplotlib.
- Full pipeline: stage not stated [Matplotlib, NumPy, Python, SciPy]

### Subcallosal cingulate deep brain stimulation evokes two distinct cortical responses via differential white matter activation. (PNAS 2024)

- DOI: 10.1073/pnas.2314918121 | PMCID: PMC10998591 | PMID: 38527192
- Version used: **1.11.2**
- Evidence: The source analysis was performed in python 3.11.5 using the following packages: mne 1.5.1, numpy 1.24.4, matplotlib 3.8.0, scipy 1.11.2, pandas 2.1.1, and seaborn 0.12.2 ( 57 – 62 ).
- Full pipeline: stage not stated [AFNI, Camino, FSL, Matplotlib v3.8.0, NumPy v1.24.4, SciPy v1.11.2, seaborn v0.12.2]

### 4D microvelocimetry reveals multiphase flow field perturbations in porous media. (PNAS 2024)

- DOI: 10.1073/pnas.2316723121 | PMCID: PMC10962996 | PMID: 38478686
- Evidence: These steps are performed using Python/SciPy.
- Full pipeline: stage not stated [SciPy]

### Mechanism of proton-powered c-ring rotation in a mitochondrial ATP synthase. (PNAS 2024)

- DOI: 10.1073/pnas.2314199121 | PMCID: PMC10945847 | PMID: 38451940
- Evidence: Reweighting of eABF simulations was done as detailed in SI Appendix , using SciPy ( 73 , 74 ) for interpolation and scikit-learn ( 75 ) for Kernel Density Estimation.
- Full pipeline: simulation/modelling [GROMACS v2020.4, MDAnalysis, SciPy, scikit-learn] -> visualisation [Matplotlib, VMD] -> stage not stated [NetworkX]

### Insights into hippocampal perfusion using high-resolution, multi-modal 7T MRI. (PNAS 2024)

- DOI: 10.1073/pnas.2310044121 | PMCID: PMC10945835 | PMID: 38446857
- Evidence: Briefly, to generate null distributions, N = 5000 permuted maps are generated by randomly shifting the 2D hippocampal maps across one or both axes using SciPy’s shift function and through rotation using their rotate function ( 113 ).
- Full pipeline: alignment/mapping [Connectome Workbench] -> differential/statistical testing [Python, pingouin] -> structure determination [FreeSurfer v7.1.1] -> visualisation [Connectome Workbench] -> stage not stated [ANTs, FSL, NetworkX, NiBabel v3.2.0, SciPy]

### Optimizing non-Newtonian fluids for impact protection of laminates. (PNAS 2024)

- DOI: 10.1073/pnas.2317832121 | PMCID: PMC10927517 | PMID: 38412136
- Version used: **1.10.1**
- Evidence: We solve for h 0 ( t ) numerically (using SciPy v1.10.1 integrate.odeint) for various C ∝ η , Fig.
- Full pipeline: stage not stated [SciPy v1.10.1]

### Permafrost extent sets drainage density in the Arctic. (PNAS 2024)

- DOI: 10.1073/pnas.2307072120 | PMCID: PMC10861896 | PMID: 38300864
- Evidence: To test the significance of the difference in ratios for each bin, we performed a Mann-Whitney U test using the Python package scipy ( 65 ) on the distributions of drainage density for permafrost and non-permafrost watersheds.
- Full pipeline: stage not stated [SciPy]

### Sparse species interactions reproduce abundance correlation patterns in microbial communities. (PNAS 2024)

- DOI: 10.1073/pnas.2309575121 | PMCID: PMC10853627 | PMID: 38266051
- Evidence: The matrix U can be generated by randomly sampling from a Haar distribution generated using the Python function ortho_group from the scipy package ( 61 ).
- Full pipeline: stage not stated [SciPy]

### Efficient mapping of the thalamocortical monosynaptic connectivity in vivo by tangential insertions of high-density electrodes in the cortex. (PNAS 2024)

- DOI: 10.1073/pnas.2313048121 | PMCID: PMC10823237 | PMID: 38241439
- Evidence: RF contours were interpolated by a factor of two using the 2D-cubic-interpolation function from the SciPy package; only clusters with RFs showing a SNR (1/SD (RF) > 15) were kept for quantification ( Fig.
- Full pipeline: quantification [SciPy] -> dimensionality reduction/clustering [SciPy] -> differential/statistical testing [Kilosort, Python]

### Social anxiety disorder-associated gut microbiota increases social fear. (PNAS 2024)

- DOI: 10.1073/pnas.2308706120 | PMCID: PMC10769841 | PMID: 38147649
- Version used: **1.9.3**
- Evidence: Further statistical analysis was handled in R (v4.2.2) using the R Studio GUI (version 2022.7.2.576) and in Python with SciPy (v1.9.3).
- Full pipeline: differential/statistical testing [Python, SciPy v1.9.3, lme4] -> stage not stated [R v4.2.2, ggplot2]

### Locomotion-dependent use of geometric and body cues in humans mapping 3D space. (PNAS 2025)

- DOI: 10.1073/pnas.2505613122 | PMCID: PMC12745749 | PMID: 41417605
- Evidence: The three temperature parameters were first fit to the object replacements in the baseline test environment, for each model and participant separately, using the Limited-memory BFGS algorithm ( 59 ) via the minimize function of the scipy Python package.
- Full pipeline: differential/statistical testing [R v4.2] -> visualisation [R v4.2] -> stage not stated [SciPy]

### Heavy-tailed update distributions arise from information-driven self-organization in nonequilibrium learning. (PNAS 2025)

- DOI: 10.1073/pnas.2523012122 | PMCID: PMC12745802 | PMID: 41410766
- Evidence: This fitting was implemented using scipy.stats.norm from the SciPy library ( 56 ), which provides statistically efficient estimates of the mean and SD under the assumption of normality.
- Full pipeline: differential/statistical testing [SciPy]

### The variability of evolvability: Properties of dynamic fitness landscapes determine how phenotypic variability evolves. (PNAS 2025)

- DOI: 10.1073/pnas.2519469122 | PMCID: PMC12745803 | PMID: 41397131
- Evidence: Maximum and average fitness was compared between variable and static runs for each fitness landscape pair using the Mann–Whitney U [scipy.stats, ( 48 )] test followed by Benjamini/Hochberg calculation of false discovery rate [statsmodels, ( 49 )] to account for multiple testing across fitness landscape pairs.
- Full pipeline: variant calling [scikit-learn] -> normalisation [scikit-learn] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy, statsmodels]

### HLA-DQB1*03:01 strongly affects age of onset of type 1 narcolepsy independently of DQA1 and ethnicity. (PNAS 2025)

- DOI: 10.1073/pnas.2513989122 | PMCID: PMC12718323 | PMID: 41364757
- Evidence: Next, we built 2 × 2 contingency tables for each segment (i.e., TRAV4 and non-TRAV4 counts in DQB1*0301-positive and negative) and used the chi2_contingency function from scipy.stats in Python to compare groups.
- Full pipeline: stage not stated [Python, SciPy]

### Nanorate sequencing reveals the &lt;i&gt;Arabidopsis&lt;/i&gt; somatic mutation landscape. (PNAS 2025)

- DOI: 10.1073/pnas.2514194122 | PMCID: PMC12685076 | PMID: 41296725
- Evidence: All tests were performed using the SciPy package ( 114 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2] -> stage not stated [MACS2, SAMtools, SciPy, Snakemake]

### Cytomegalovirus disrupts Lamin A/C to control microtubule-mediated nuclear movement and cell migration. (PNAS 2025)

- DOI: 10.1073/pnas.2507831122 | PMCID: PMC12685118 | PMID: 41289383
- Version used: **1.2.1**
- Evidence: The following Python packages were utilized: Matplotlib (version 3.0.3), NumPy (version 1.16.3), Pandas (version 0.24.2), SciPy (version 1.2.1), and Seaborn (version 0.9.0).
- Full pipeline: quantification [CellProfiler] -> visualisation [Conda, Jupyter, Python v3.7.3] -> stage not stated [ImageJ, Matplotlib v3.0.3, NumPy v1.16.3, SciPy v1.2.1, seaborn v0.9.0]

### Engineered calcium-regulated affinity protein for efficient internalization and lysosomal toxin delivery. (PNAS 2025)

- DOI: 10.1073/pnas.2509081122 | PMCID: PMC12685030 | PMID: 41289384
- Evidence: Image processing was performed in Fiji for background subtraction and in Python (OpenCV, SciPy, NumPy, scikit-image) for analysis.
- Full pipeline: structure determination [ChimeraX v1.9, PHENIX v1.21.2] -> visualisation [ChimeraX v1.9, PHENIX v1.21.2] -> stage not stated [AlphaFold, NumPy, OpenCV, Python, SciPy, scikit-image]

### Genetic testing predicts appearance but not behavior in dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421752122 | PMCID: PMC12684939 | PMID: 41284863
- Evidence: We determined significance of the likelihood ratio statistic by computing a P -value using the chi squared (scipy.statst.chi2.sf) with one degree of freedom.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [ADMIXTURE, Docker, GCTA v1.94.1, Nextflow, PLINK v1.90b, pandas]

### The molecular-level diagenetic clock of sinking marine organic matter. (PNAS 2025)

- DOI: 10.1073/pnas.2504769122 | PMCID: PMC12685107 | PMID: 41284868
- Evidence: BCDI ( 66 ) based on the Ward method was performed using the hierarchy module from the SciPy (Scientific library for python) ( 105 ) v1.5.0 package.
- Full pipeline: differential/statistical testing [Python] -> stage not stated [SciPy]

### Interactions between long- and short-term synaptic plasticity transform temporal neural representations into spatial. (PNAS 2025)

- DOI: 10.1073/pnas.2426290122 | PMCID: PMC12663931 | PMID: 41269798
- Evidence: For each connection, parameters for the Tsodyks–Markram model were obtained by running the minimize function of the scipy.optimize package to minimize the mean square error over all 12 response amplitudes A 1 , ⋯ , A 12 .
- Full pipeline: stage not stated [SciPy]

### Defects at play: Shaping the photophysics and photochemistry of ice. (PNAS 2025)

- DOI: 10.1073/pnas.2516805122 | PMCID: PMC12663945 | PMID: 41264242
- Evidence: To generate smooth representations of the distributions, Gaussian kernel density estimation curves were constructed using the gaussian-kde function from the SciPy library ( 86 ).
- Full pipeline: stage not stated [Quantum ESPRESSO, SciPy]

### The adhesion GPCR ADGRL2 engages Gα13 to enable epidermal differentiation. (PNAS 2025)

- DOI: 10.1073/pnas.2508436122 | PMCID: PMC12663980 | PMID: 41252157
- Evidence: To analyze cell enrichment at specific points along the pseudotime axis, a Gaussian kernel density estimate (KDE) was applied to the pseudotimes of all cells, as well as to those cells targeted by guides specific to the gene of interest, using the “scipy.stats.gaussian_kde” function.
- Full pipeline: alignment/mapping [STAR v2.7.1a] -> quantification [Bioconductor, DESeq2, R] -> normalisation [Bioconductor, DESeq2, R] -> registration [MotionCor2, RELION] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> structure determination [Coot, PHENIX] -> stage not stated [CTFFIND, ChimeraX, ImageJ, SciPy, Seurat]

### Estimated impact of 2022-2023 influenza vaccines on annual hospital burden in the United States. (PNAS 2025)

- DOI: 10.1073/pnas.2505175122 | PMCID: PMC12646225 | PMID: 41218113
- Evidence: We used Python’s scipy.optimize.curve_fit function with the Levenberg–Marquardt algorithm to minimize the sum of squared errors between simulated and observed hospitalizations.
- Full pipeline: simulation/modelling [SciPy]

### Neuronal normalization in monkey MT is an intensity-weighted average. (PNAS 2025)

- DOI: 10.1073/pnas.2522104122 | PMCID: PMC12625995 | PMID: 41196346
- Evidence: For each unit that passed the inclusion criterion, we different models to the mean firing rate across stimulus conditions using a nonlinear least squares optimization (scipy.optimize.curve_fit).
- Full pipeline: stage not stated [Kilosort v2.0, SciPy]

### Methanogenic archaea encoding Pyrrolysine maintain ambiguous amber codon usage. (PNAS 2025)

- DOI: 10.1073/pnas.2517473122 | PMCID: PMC12626013 | PMID: 41196353
- Evidence: 2 using the scipy.stats Python package.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [Cufflinks v2.2.1, DESeq2 v1.20.0, HISAT2 v2.1.0, MAFFT] -> stage not stated [Prokka, RAxML, SciPy]

### Revisiting the high-dimensional geometry of population responses in the visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2506535122 | PMCID: PMC12625980 | PMID: 41191501
- Evidence: To solve the nonlinear least squares problem and satisfy constraints on parameters (e.g., power law slope cannot be negative because eigenvalues monotonically decrease), we use the nonlinear least squares function implemented in SciPy ( 36 ).
- Full pipeline: stage not stated [SciPy, Suite2p]

### Chemical propulsion of hemozoin crystal motion in malaria parasites. (PNAS 2025)

- DOI: 10.1073/pnas.2513845122 | PMCID: PMC12595501 | PMID: 41150719
- Evidence: We used scipy.optimize.curve_fit function in Python to empirically fit our data ( 66 ).
- Full pipeline: simulation/modelling [LAMMPS] -> stage not stated [Python, SciPy, TrackMate]

### A steady-state pool of calcium-dependent actin is maintained by Homer and controls epithelial mechanosensation. (PNAS 2025)

- DOI: 10.1073/pnas.2509784122 | PMCID: PMC12582288 | PMID: 41134626
- Evidence: The following python packages were used: numpy, pandas, statsmodels, and scipy for organizing, sorting, and processing (normalization, smoothing, peak/trough finding) to automatically determine analysis windows based on displacement and extract data for various parameters; statsmodels for OLS analysis; matplotlib and seaborn for presentation.
- Full pipeline: quantification [napari] -> normalisation [Matplotlib, NumPy, SciPy, seaborn, statsmodels] -> differential/statistical testing [R] -> stage not stated [ImageJ, scikit-image]

### On the scale of heterogeneity in composite electrodes of batteries. (PNAS 2025)

- DOI: 10.1073/pnas.2520136122 | PMCID: PMC12582338 | PMID: 41129219
- Evidence: In particle matching, a cKDTree (K-Dimensional Tree using scipy.spatial) is constructed using the centroid coordinates to rapidly look up the nearest neighbors of the particles in df2.
- Full pipeline: alignment/mapping [scikit-image] -> dimensionality reduction/clustering [SciPy] -> structure determination [scikit-image] -> visualisation [Matplotlib, NumPy] -> stage not stated [OpenCV, Python]

### Morphological specializations of mosquito CO&lt;sub&gt;2&lt;/sub&gt;-sensing olfactory receptor neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2514666122 | PMCID: PMC12582328 | PMID: 41129220
- Evidence: To reduce noise, the cross-sectional area curve was smoothed using a 1D Gaussian filter (gaussian_filter1d) from the scipy.ndimage package.
- Full pipeline: alignment/mapping [IMOD] -> machine learning [R] -> visualisation [tidyverse] -> stage not stated [ImageJ, SciPy, Stan]

### Foot placement control underlies stable locomotion across species. (PNAS 2025)

- DOI: 10.1073/pnas.2413958122 | PMCID: PMC12582247 | PMID: 41118219
- Evidence: All the statistics were performed using Python3 ( numpy , scipy , and scikit_posthoc ).
- Full pipeline: differential/statistical testing [NumPy, Python, SciPy]

### Generalized convolutional many-body distribution functional representations. (PNAS 2025)

- DOI: 10.1073/pnas.2415662122 | PMCID: PMC12541311 | PMID: 41052323
- Evidence: It relies on the Numpy ( 51 ), Scipy ( 52 ) and Numba ( 53 ) Python libraries.
- Full pipeline: stage not stated [NumPy, PySCF, Python, SciPy, XGBoost]

### A precise metallicity and carbon-to-oxygen ratio for a warm giant exoplanet from its panchromatic JWST emission spectrum. (PNAS 2025)

- DOI: 10.1073/pnas.2416193122 | PMCID: PMC12501160 | PMID: 40982673
- Evidence: We penta-linearly interpolate (using SciPy RegularGridInterpolator) the pressure–temperature profile and gas volume mixing ratios for a given set of parameters, then postprocess models into cloudy emission spectra within the PyMultiNest routine at a spectral resolution of 100,000 (including opacities for H 2 -H 2 /He CIA, H 2 O, CO, CO 2 , CH 4 , NH 3 , HCN, C 2 H 2 , H 2 S, SO 2 , Na, and K) to a...
- Full pipeline: quantification [dynesty] -> stage not stated [SciPy, emcee]

### An open-source photobleacher for fluorescence imaging of large pigment-rich tissues. (PNAS 2025)

- DOI: 10.1073/pnas.2426628122 | PMCID: PMC12478079 | PMID: 40961137
- Evidence: Statistical analyses were performed using SciPy with Python 3.9.
- Full pipeline: differential/statistical testing [Python v3.9, SciPy]

### Φ value analysis underscores strong functional and structural compactness of the GABA&lt;sub&gt;A&lt;/sub&gt; receptor. (PNAS 2025)

- DOI: 10.1073/pnas.2512278122 | PMCID: PMC12478134 | PMID: 40956892
- Evidence: All statistical analyses were performed using Python scripts with the Pandas, Numpy, and Scipy packages.
- Full pipeline: differential/statistical testing [NumPy, SciPy] -> visualisation [ChimeraX] -> stage not stated [Python]

### Optimal transitions between nonequilibrium steady states. (PNAS 2025)

- DOI: 10.1073/pnas.2510654122 | PMCID: PMC12478161 | PMID: 40953253
- Evidence: To validate our fitting routine we have compared it to a trust-constr method from the python package scipy.minimize using squared errors and found very good agreement (not more than ± 2 % ).
- Full pipeline: stage not stated [SciPy]

### STIM1 transmembrane helix dimerization captured by AI-guided transition path sampling. (PNAS 2025)

- DOI: 10.1073/pnas.2506516122 | PMCID: PMC12415195 | PMID: 40857319
- Evidence: Trajectory analysis was carried out using the pytraj ( 96 ), mdtraj ( 97 ), MDAnalysis ( 98 , 99 ), numpy ( 100 ), and SciPy ( 101 ) packages.
- Full pipeline: normalisation [PyTorch] -> simulation/modelling [GROMACS v2020.6, MDAnalysis, MDTraj, NumPy, SciPy] -> machine learning [PyTorch]

### Fragmentation signatures in cancer patients resemble those of patients with vascular or autoimmune diseases. (PNAS 2025)

- DOI: 10.1073/pnas.2426890122 | PMCID: PMC12402995 | PMID: 40833414
- Version used: **1.13.1**
- Evidence: All statistics were generated using python version 3.9.12 and scipy version 1.13.1.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [BEDTools, Bowtie2, SAMtools] -> dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy v1.13.1] -> stage not stated [Picard]

### Warming climate and water withdrawals threaten river flow connectivity in China. (PNAS 2025)

- DOI: 10.1073/pnas.2421046122 | PMCID: PMC12403000 | PMID: 40825132
- Evidence: The SciPy library in Python was used to implement the t -test based on the t -distribution for CI and P -values.
- Full pipeline: stage not stated [Python, SciPy]

### Gene regulatory logic of the interferon-β enhancer is characterized by two selectively deployed modes of transcription factor synergy. (PNAS 2025)

- DOI: 10.1073/pnas.2502800122 | PMCID: PMC12377728 | PMID: 40794834
- Version used: **1.11.4**
- Evidence: For each model, parameters were sampled and then optimized using the Scipy v1.11.4 ( 73 ) implementation of the Nelder Mead algorithm.
- Full pipeline: stage not stated [SciPy v1.11.4]

### Immiscible proteins compete for RNA binding to order condensate layers. (PNAS 2025)

- DOI: 10.1073/pnas.2504778122 | PMCID: PMC12338069 | PMID: 40768359
- Evidence: Fitting was performed in Python using the curve_fit module from scipy.optimize version 1.14.1.
- Full pipeline: stage not stated [ImageJ, Python, SciPy, scikit-image v0.25.0]

### Anisotropic stretch biases the self-organization of actin fibers in multicellular Hydra aggregates. (PNAS 2025)

- DOI: 10.1073/pnas.2423437122 | PMCID: PMC12358849 | PMID: 40758890
- Evidence: 3 and 4 ), the measurement distribution was normalized in the range 0 to 1 and tested against a uniform distribution with a Kolmogorov–Smirnov test using the Python function scipy.stats.kstest.
- Full pipeline: normalisation [SciPy] -> stage not stated [ImageJ, Python]

### Surface delivery quantification reveals distinct trafficking efficiencies among clustered protocadherin isoforms. (PNAS 2025)

- DOI: 10.1073/pnas.2514178122 | PMCID: PMC12337331 | PMID: 40737325
- Version used: **1.11.4**
- Evidence: For each subalignment, the amino acid frequencies were calculated, and the frequency distributions at each position were compared between the two alignments using the entropy function in scipy v.1.11.4 ( 68 ) to calculate the Kullback–Leibler divergence, which we refer to as the KL div score.
- Full pipeline: alignment/mapping [MUSCLE v5.1, Python, SciPy v1.11.4] -> stage not stated [AlphaFold, seaborn v0.13.0]

### A genetically defined pontine nucleus essential for ingestion in mice. (PNAS 2025)

- DOI: 10.1073/pnas.2411174122 | PMCID: PMC12305073 | PMID: 40663610
- Evidence: Depending on the outcome of the normality test, either a paired-samples t test or a Wilcoxon signed-rank test was performed, as appropriate, using the scipy.stats library in Python.
- Full pipeline: differential/statistical testing [NumPy] -> machine learning [DeepLabCut v2.3.8] -> stage not stated [Fiji, ImageJ, Python, SciPy]

### Learning predictive signals within a local recurrent circuit. (PNAS 2025)

- DOI: 10.1073/pnas.2414674122 | PMCID: PMC12260394 | PMID: 40591603
- Version used: **0.18**
- Evidence: All simulations were performed in customized Python3 code written by TA with numpy 1.17.3 and scipy 0.18.
- Full pipeline: simulation/modelling [NumPy v1.17.3, SciPy v0.18]

### Human influence on climate detectable in the late 19th century. (PNAS 2025)

- DOI: 10.1073/pnas.2500829122 | PMCID: PMC12207479 | PMID: 40523188
- Evidence: To avoid phase-shifting of the filtered data, we use the scipy “filtfilt” routine, which applies the Butterworth filter twice (forward and backward; https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.filtfilt.html ).
- Full pipeline: stage not stated [SciPy]

### Generative prediction of causal gene sets responsible for complex traits. (PNAS 2025)

- DOI: 10.1073/pnas.2415071122 | PMCID: PMC12184495 | PMID: 40504147
- Evidence: We use the Python function minimize from SciPy (which implements the L-BFGS-B method) to solve the constrained optimization problem in Eq.
- Full pipeline: machine learning [SciPy] -> stage not stated [Enrichr, PyTorch]

### Controlling DNA-RNA strand displacement kinetics with base distribution. (PNAS 2025)

- DOI: 10.1073/pnas.2416988122 | PMCID: PMC12167940 | PMID: 40478881
- Evidence: Fitting was carried out using optimize.curve_fit from the SciPy library ( 53 ), with F 0 , F ∞ , t 0 , and ( k c ) as free fitting parameters.
- Full pipeline: stage not stated [Python, SciPy]

### Increased excitatory synapse size in hippocampal place cells compared to silent cells. (PNAS 2025)

- DOI: 10.1073/pnas.2505322122 | PMCID: PMC12167973 | PMID: 40472030
- Evidence: Peaks of the tuning curve were defined by scipy.signal.find_peaks function (height = 6) ( 45 ).
- Full pipeline: registration [Suite2p] -> stage not stated [Cellpose, ImageJ, Python, SciPy]

### Microtubule dynamics are defined by conformations and stability of clustered protofilaments. (PNAS 2025)

- DOI: 10.1073/pnas.2424263122 | PMCID: PMC12146719 | PMID: 40440074
- Version used: **1.11**
- Evidence: All postprocessing calculations and data analyses were done with GROMACS internal tools, Python 3.9 ( 95 ), Numpy v1.26 ( 96 ), and SciPy v1.11 ( 97 ).
- Full pipeline: alignment/mapping [IMOD, MotionCor2] -> simulation/modelling [GROMACS, VMD] -> structure determination [IMOD, MotionCor2] -> visualisation [VMD] -> stage not stated [Matplotlib v3.8.2, NumPy v1.26, Python v3.9, SciPy v1.11, seaborn v0.13]

### Micropipette aspiration reveals differential RNA-dependent viscoelasticity of nucleolar subcompartments. (PNAS 2025)

- DOI: 10.1073/pnas.2407423122 | PMCID: PMC12146704 | PMID: 40434645
- Evidence: This was accomplished with Scipy’s curve_fit function with sigma set as the SE and setting absolute_sigma to true.
- Full pipeline: stage not stated [ImageJ, SciPy]

### A direct computational assessment of vinculin-actin unbinding kinetics reveals catch-bonding behavior. (PNAS 2025)

- DOI: 10.1073/pnas.2425982122 | PMCID: PMC12130851 | PMID: 40397673
- Evidence: Interpolation was done using the scipy library ( 78 ).
- Full pipeline: stage not stated [PLUMED, SciPy, VMD]

### Physical activity stimulates clock neurons of the day-active rodent &lt;i&gt;Arvicanthis ansorgei&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2424545122 | PMCID: PMC12130842 | PMID: 40388616
- Version used: **1.7.0**
- Evidence: Data were analyzed using SPSS, Sigma Plot, or the Python module SciPy version 1.7.0.
- Full pipeline: visualisation [Matplotlib v3.4.2, Python v3.0.9] -> stage not stated [SciPy v1.7.0]

### Proteostasis landscapes of cystic fibrosis variants reveal drug response vulnerability. (PNAS 2025)

- DOI: 10.1073/pnas.2418407122 | PMCID: PMC12054793 | PMID: 40261935
- Evidence: To determine statistically significant CFTR interactors, we used a two-tailed paired t test with scipy.stats.ttest_rel ( https://docs.scipy.org/doc/scipy/ ) package in Python to calculate the p-value between the log2 TMT intensity of each protein over the corresponding log2 TMT intensity in the mock-transfected control condition.
- Full pipeline: dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Python, SciPy]

### An integrated AI knowledge graph framework of bacterial enzymology and metabolism. (PNAS 2025)

- DOI: 10.1073/pnas.2425048122 | PMCID: PMC12012490 | PMID: 40193601
- Evidence: The hypergeometric distribution was calculated using the Scipy implementation ( 71 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, HMMER, PyTorch, Python, SciPy]

### Bispecific antibodies against the hepatitis C virus E1E2 envelope glycoprotein. (PNAS 2025)

- DOI: 10.1073/pnas.2420402122 | PMCID: PMC12012487 | PMID: 40193609
- Evidence: Calibrated events were exported and processed by an in-house developed Python pipeline ( 86 ) using NumPy ( 87 ), pandas ( 88 ), Matplotlib ( 89 ), SciPy ( 90 ), and seaborn ( 91 ).
- Full pipeline: visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, Matplotlib, NumPy, SciPy, seaborn]

### Cotranslational membrane insertion of the voltage-sensitive K&lt;sup&gt;+&lt;/sup&gt; channel KvAP. (PNAS 2025)

- DOI: 10.1073/pnas.2412492122 | PMCID: PMC12002286 | PMID: 40163725
- Evidence: 4 was estimated by the multiple comparisons Dunnett’s test ( P < 0.05) ( 50 ), using the Python (version 3.12) library SciPy ( 51 ).
- Full pipeline: stage not stated [ImageJ, Python v3.12, SciPy]

### A solvable model for strongly interacting nonequilibrium excitons. (PNAS 2025)

- DOI: 10.1073/pnas.2424663122 | PMCID: PMC11929435 | PMID: 40085654
- Evidence: Using the sparse matrix routines available in scipy, we can find the eigenvalue–eigenvector pairs with eigenvalues close to zero (or we can directly diagonalize the entire matrix if it is small enough).
- Full pipeline: stage not stated [NumPy, Python, SciPy]

### Learning reshapes the hippocampal representation hierarchy. (PNAS 2025)

- DOI: 10.1073/pnas.2417025122 | PMCID: PMC11929462 | PMID: 40063792
- Evidence: This procedure is computationally demanding; a simplified algorithm with linear complexity in the number of points has been proposed by Müllner ( 66 ) and is implemented in the Scipy library version 1.11 in the function cluster.hierarchy.linkage which was used here for analysis.
- Full pipeline: dimensionality reduction/clustering [SciPy] -> stage not stated [Python v3.11, statsmodels v0.14]

### Brain aging shows nonlinear transitions, suggesting a midlife "critical window" for metabolic intervention. (PNAS 2025)

- DOI: 10.1073/pnas.2416433122 | PMCID: PMC11912423 | PMID: 40030017
- Evidence: We utilized scipy.optimize ( 88 ).
- Full pipeline: stage not stated [Nilearn, SPM, SciPy, fMRIPrep]

### Spatial profiling of the interplay between cell type- and vision-dependent transcriptomic programs in the visual cortex. (PNAS 2025)

- DOI: 10.1073/pnas.2421022122 | PMCID: PMC11848306 | PMID: 39946537
- Evidence: We calculated the area of the convex hull using the python package scipy and its function scipy.spatial.ConvexHull .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Scanpy] -> stage not stated [Enrichr, NumPy, SciPy, scikit-learn, seaborn]

### Machine learning-enhanced surface-enhanced spectroscopic detection of polycyclic aromatic hydrocarbons in the human placenta. (PNAS 2025)

- DOI: 10.1073/pnas.2422537122 | PMCID: PMC11848310 | PMID: 39928861
- Evidence: We first resample all spectra using the “interpolate” function from SciPy, ensuring consistent wavenumbers across spectra ( 65 ).
- Full pipeline: stage not stated [SciPy]

### G-quadruplexes catalyze protein folding by reshaping the energetic landscape. (PNAS 2025)

- DOI: 10.1073/pnas.2414045122 | PMCID: PMC11831120 | PMID: 39913211
- Evidence: Data were fit using Eyring equations ( 25 ) with and without heat capacity using SciPy.
- Full pipeline: stage not stated [SciPy]

### Evidence for domain-general arousal from semantic and neuroimaging meta-analyses reconciles opposing views on arousal. (PNAS 2025)

- DOI: 10.1073/pnas.2413808122 | PMCID: PMC11831115 | PMID: 39899711
- Evidence: We report MNI152 coordinates of the center of mass [computed using ndimage.center_of_mass function from SciPy library (v1.11.2) ( 71 )].
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> stage not stated [SciPy]

### Comparing cooperative geometric puzzle solving in ants versus humans. (PNAS 2025)

- DOI: 10.1073/pnas.2414274121 | PMCID: PMC11725855 | PMID: 39715438
- Evidence: We calculated the Euclidean distance from the boundary for every element in the discretized configuration space using the distance_transform_edt function from the Python package scipy.ndimage.
- Full pipeline: stage not stated [SciPy]

### Damselflies overcome color saturation barriers of photonic glasses via pigment loading and refractive index modulation. (PNAS 2026)

- DOI: 10.1073/pnas.2527433123 | PMCID: PMC13250596 | PMID: 42213815
- Evidence: All calculations were performed using a custom Python script (Python 3.11, NumPy, SciPy, Matplotlib, and Pandas libraries).
- Full pipeline: stage not stated [ImageJ, Matplotlib, NumPy, Python v3.11, SciPy]

### Geometric ordering in bacterial communities. (PNAS 2026)

- DOI: 10.1073/pnas.2526643123 | PMCID: PMC13187718 | PMID: 42118839
- Evidence: To visualize Voronoi tessellations in 2D, we used the voronoi and voronoi_plot_2d functions from the scipy.spatial module from SciPy ( 75 ), v1.11.1, available at: https://scipy.org/ ).
- Full pipeline: simulation/modelling [Python] -> visualisation [Matplotlib v3.7.1, SciPy] -> stage not stated [ImageJ v1.54d, NumPy]

### Multimodal analysis reveals cellular diversity and divergent circuits of the zona incerta. (PNAS 2026)

- DOI: 10.1073/pnas.2509781123 | PMCID: PMC13143026 | PMID: 42054363
- Evidence: Normality was assessed using the Shapiro–Wilk test (scipy) and homoscedasticity was evaluated using Levene’s test (scipy).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [SciPy, statsmodels]

### Interspecies interaction controls &lt;i&gt;Escherichia coli&lt;/i&gt; growth in human gut microbiome samples. (PNAS 2026)

- DOI: 10.1073/pnas.2527793123 | PMCID: PMC13123830 | PMID: 42018414
- Evidence: We processed the data in Python using SciPy.
- Full pipeline: quantification [vegan v2.7] -> normalisation [vegan v2.7] -> dimensionality reduction/clustering [vegan v2.7] -> visualisation [phyloseq v1.46] -> stage not stated [DADA2 v3.18, Matplotlib, Python, SciPy, emmeans]

### Fast automated adjoints for spectral PDE solvers. (PNAS 2026)

- DOI: 10.1073/pnas.2530440123 | PMCID: PMC13080004 | PMID: 41961849
- Evidence: Together, these routines are used to compute the leading singular vectors via the SciPy sparse SVD.
- Full pipeline: simulation/modelling [PyTorch] -> machine learning [PyTorch] -> stage not stated [OpenFOAM, Python, SciPy]

### Reconstruction of human metabolic models with large language models. (PNAS 2026)

- DOI: 10.1073/pnas.2516511123 | PMCID: PMC13079975 | PMID: 41950094
- Version used: **1.7.3**
- Evidence: The analysis and visualization were facilitated by Python 3.7.16, SHAP 0.41.0, scikit-learn 1.0.2, pandas 1.1.3, SciPy 1.7.3, NumPy 1.21.5, and Matplotlib 3.4.3 packages.
- Full pipeline: visualisation [Matplotlib v3.4.3, NumPy v1.21.5, Python v3.7.16, SciPy v1.7.3, scikit-learn v1.0.2]

### Large future genetic diversity losses are predicted from conservation indicators even with habitat protection. (PNAS 2026)

- DOI: 10.1073/pnas.2514371123 | PMCID: PMC13037886 | PMID: 41886371
- Evidence: Optimization was performed using the “Powell” method in scipy.optimize ( 49 – 51 ).
- Full pipeline: variant calling [R v0.0.3] -> stage not stated [ADMIXTURE, PLINK v1.9, SciPy]

### Tau catalyzes amyloid-β aggregation and toxicity in a polymorph-dependent manner. (PNAS 2026)

- DOI: 10.1073/pnas.2532775123 | PMCID: PMC13037932 | PMID: 41880569
- Version used: **1.13.1**
- Evidence: The data were analyzed using GraphPad Prism 10.2 software (San Diego, CA) and Python3 with SciPy 1.13.1 package, by Student’s t test, one-way or two-way ANOVA, and Bonferroni’s or Tukey’s post hoc test.
- Full pipeline: differential/statistical testing [SciPy v1.13.1] -> stage not stated [Python, statsmodels]

### Convergent evolution increases boron transport through SNPs and tandem duplications at &lt;i&gt;BOR1&lt;/i&gt; and &lt;i&gt;BOR2&lt;/i&gt; in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2525676123 | PMCID: PMC13037888 | PMID: 41871252
- Version used: **1.6.2**
- Evidence: To assess excess of significant p-values, we conducted genomic control with SciPy (version 1.6.2) using the following equation: λ = O χ median 2 E χ median 2 , where λ corresponds to the genomic control, O χ median 2 is the observed median of the chi-squared values, and E χ median 2 is 0.4549, the expected median of a chi-squared distribution with one degree of freedom.
- Full pipeline: variant calling [VCFtools] -> normalisation [Python v3.8.3] -> differential/statistical testing [SciPy v1.6.2] -> visualisation [AlphaFold, ChimeraX v1.9] -> stage not stated [DELLY v0.8.3, GATK, GEMMA, PLINK, R v4.4.2, lme4, minimap2]

### Direct evidence of acid-driven protein desolvation. (PNAS 2026)

- DOI: 10.1073/pnas.2525949123 | PMCID: PMC12974452 | PMID: 41785322
- Evidence: Titration curves were fitted using the Scipy module ( 85 ) after calculating the protonation fractions according to Eq.
- Full pipeline: simulation/modelling [GROMACS] -> structure determination [ChimeraX, MDAnalysis, PHENIX] -> stage not stated [RELION, SciPy]

### Cryogenic electron tomography by the numbers: Charting underexplored lineages in structural cell biology. (PNAS 2026)

- DOI: 10.1073/pnas.2518350123 | PMCID: PMC12933124 | PMID: 41706896
- Evidence: For statistical analyses of the amount of cellular material within lamellae a Kruskal–Wallis test was performed ( p = 4 ⨯ 10 −45 ) followed by a pairwise Dunn’s tests between domains (Bact-Euk: P = 1 ⨯ 10 −41 , Bact.-Arch: P = 3 ⨯ 10 −1 , Euk-Arch: P = 3 ⨯ 10 −11 ) using the SciPy and Scikit-posthoc python packages ( 45 , 46 ).
- Full pipeline: differential/statistical testing [SciPy]

### Molecular assemblies and pharmacology of cerebellar GABA&lt;sub&gt;A&lt;/sub&gt; receptors. (PNAS 2026)

- DOI: 10.1073/pnas.2524504123 | PMCID: PMC12890884 | PMID: 41650215
- Evidence: Data analysis was performed in Python using SciPy, applying either a one-site binding or competitive inhibition model.
- Full pipeline: stage not stated [AlphaFold, ChimeraX, Python, SciPy]

### A framework integrating multiscale in silico modeling and experimental data predicts CAR-NK cell cytotoxicity across target cell types. (PNAS 2026)

- DOI: 10.1073/pnas.2500319123 | PMCID: PMC12867702 | PMID: 41615751
- Evidence: 7 using the function solve_ivp with “RK45” method from the Python scipy.integrate library and applied the following formula Eq.
- Full pipeline: stage not stated [SciPy]

### Soluble adenylyl cyclase in nonmammalian sperm is directly controlled by pH, not by HCO&lt;sub&gt;3&lt;/sub&gt;&lt;sup&gt;-&lt;/sup&gt; or Ca&lt;sup&gt;2&lt;/sup&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2505026123 | PMCID: PMC12867704 | PMID: 41591904
- Version used: **1.15.1**
- Evidence: 2 and 4 were performed with scipy (version 1.15.1) and statsmodels (version 0.14.4) in python (3.12.3).
- Full pipeline: alignment/mapping [AlphaFold v2.2.4, ColabFold v1.5.2, MAFFT] -> stage not stated [BLAST, SciPy v1.15.1, statsmodels v0.14.4]

### A temporal and spatial atlas of adaptive immune responses in the lymph node following viral infection. (PNAS 2026)

- DOI: 10.1073/pnas.2504742123 | PMCID: PMC12867689 | PMID: 41587309
- Evidence: For the Outer Cortex control (Control_out_D3 & Control_out_Mock), we computed their convex hull (scipy.spatial.ConvexHull) within the spatial extent of the outer cortex (“Capsule” and “Outer Cortex”) and selected the ones away from “ Ifng -high” areas.
- Full pipeline: stage not stated [AnnData, Docker, Scanpy v1.9.8, SciPy]

### Structural characterization of the HDV virion and its ribonucleoprotein. (PNAS 2026)

- DOI: 10.1073/pnas.2519809123 | PMCID: PMC12846810 | PMID: 41564123
- Evidence: Curves and bar graphs were made using Python with Matplotlib ( 59 ), Pandas ( 60 ), Numpy ( 61 ), and Scipy ( 62 ).
- Full pipeline: structure determination [PHENIX, RELION] -> stage not stated [ChimeraX, Coot, Matplotlib, NumPy, SciPy, Topaz, UCSF Chimera]

### Estimating infectiousness throughout SARS-CoV-2 infection course. (Science 2021)

- DOI: 10.1126/science.abi5273 | PMCID: PMC9267347 | PMID: 34035154
- Version used: **1.4.1**
- Evidence: Software The following Python (version 3.8.2) software packages were used in the data analysis and in the production of figures: Scipy (version 1.4.1) ( 78 ), pandas (version 1.0.3) ( 79 ), statsmodels (version 0.11.1) ( 80 ), matplotlib (version 3.2.1) ( 81 ), numpy (1.18.3) ( 82 ), seaborn_sinaplot ( 83 ), simanneal (version 0.5.0) ( 71 ), and seaborn (version 0.10.1) ( 84 ).
- Full pipeline: alignment/mapping [MAFFT] -> differential/statistical testing [R, brms] -> stage not stated [BCFtools, Bowtie2 v2.4.1, Matplotlib v3.2.1, NumPy v1.18.3, Python v3.8.2, SAMtools v1.9, SciPy v1.4.1, Stan, data.table v1.13.3, ggplot2 v3.3.2, rstanarm v2.21.1, seaborn v0.10.1, statsmodels v0.11.1]

### Reconfigurable asymmetric protein assemblies through implicit negative design. (Science 2022)

- DOI: 10.1126/science.abj7662 | PMCID: PMC9881579 | PMID: 35050655
- Version used: **1.6.3**
- Evidence: S23A ) were numerically integrated using integrate.odeint() as implemented in Scipy (version 1.6.3).
- Full pipeline: structure determination [PHENIX] -> stage not stated [PyMOL, SciPy v1.6.3]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: Peak detection was conducted using the scipy.signal.find_peaks function.
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### The connectome of an insect brain. (Science 2023)

- DOI: 10.1126/science.add9330 | PMCID: PMC7614541 | PMID: 36893230
- Evidence: Code Analyses relied on NumPy ( 125 ), SciPy ( 126 ), Pandas ( 127 ), NetworkX ( 128 ), navis ( 124 ), and pythoncatmaid ( https://pypi.org/project/python-catmaid/ ).
- Full pipeline: stage not stated [Matplotlib, NetworkX, NumPy, SciPy, seaborn]

### Hidden state inference requires abstract contextual representations in the ventral hippocampus. (Science 2024)

- DOI: 10.1126/science.adq5874 | PMCID: PMC7618349 | PMID: 39571013
- Evidence: The python function scipy.optimize.minimize was used to find the set of parameter values that minimized the negative log of the likelihood of the data ( LL ) given the model parameters p ( d 1: T |Θ m , m ): (22) L L = log p ( d 1 : T ∣ Θ m , m ) = ∑ t = 1 T log p ( c t ∣ d 1 : t − 1 , Θ m , m ) To avoid finding the local minima in the minimization procedure, we repeated model fitting procedure 50...
- Full pipeline: differential/statistical testing [R, lme4, pingouin, scikit-learn, statsmodels] -> stage not stated [Python, SciPy]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Version used: **1.11.1**
- Evidence: ChIP-seq signal box plots were generated with Python (v3.11.5) ( 120 ), using Pandas (v2.0.3), Matplotlib (v3.7.2), Seaborn (0.12.2), SciPy (1.11.1) and NumPy (v1.24.3) libraries, starting from deep-Tools computeMatrix output values, summing H2A.Z/H2A.Zac ChIP-seq signal across each peak coordinate, dividing it by the input signal and plotting the resulting ratios.
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Drugs of abuse hijack a mesolimbic pathway that processes homeostatic need. (Science 2024)

- DOI: 10.1126/science.adk6742 | PMCID: PMC11077477 | PMID: 38669575
- Evidence: Peaks of neuronal responses were identified using the SciPy package (find_peak() function) with the peak height threshold set to 3σ) and minimum distance between peaks set to ~1.3 seconds (based on the GCaMP6s decay time).
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> normalisation [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [TensorFlow] -> stage not stated [ImageJ, Python, SciPy, Suite2p]

### PIEZO channels link mechanical forces to uterine contractions in parturition. (Science 2025)

- DOI: 10.1126/science.ady3045 | PMCID: PMC12807505 | PMID: 41231991
- Evidence: The pressure peaks with a minimum height of 40 (mmHg) and prominence of 20 were identified using scipy.find_peaks function and statistical tests (Mann-Whitney test or Kruskal-Wallis test) were conducted in GraphPad Prism.
- Full pipeline: alignment/mapping [Seurat] -> quantification [CellProfiler] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy, edgeR] -> visualisation [UMAP] -> stage not stated [scDblFinder]

### Comparative connectomics of two distantly related nematode species reveals patterns of nervous system evolution. (Science 2025)

- DOI: 10.1126/science.adx2143 | PMCID: PMC12330220 | PMID: 40743352
- Evidence: Quantification and statistical analysis The statistical analysis performed in this paper is a combination of python software packages which include Scikit-learn and SciPy.
- Full pipeline: quantification [SciPy] -> differential/statistical testing [SciPy, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [Cytoscape]

### Conserved brain-wide emergence of emotional response from sensory experience in humans and mice. (Science 2025)

- DOI: 10.1126/science.adt3971 | PMCID: PMC12286656 | PMID: 40440375
- Evidence: Bandpower over time for canonical frequency bands was computed from the local field potential by bandpass filtering and then computing the squared magnitude of the hilbert transform [scipy.signal.hilbert from SciPy ( 76 )] of the bandpassed signal.
- Full pipeline: normalisation [ANTs] -> registration [ANTs] -> dimensionality reduction/clustering [Scanpy, UMAP] -> stage not stated [Connectome Workbench, DeepLabCut, FSL, FreeSurfer v6.0.0, Matplotlib, Nilearn, NumPy, SciPy, scikit-learn, seaborn]

### Rules of engagement for condensins and cohesins guide mitotic chromosome formation. (Science 2025)

- DOI: 10.1126/science.adq1709 | PMCID: PMC12118822 | PMID: 40208986
- Evidence: We used KDTrees ( scipy.spatial.cKDTree.query_pairs ) to identify and remove dots within a radius of 30kbp (same as clustering radius using the dot calling).
- Full pipeline: dimensionality reduction/clustering [SciPy] -> simulation/modelling [OpenMM] -> visualisation [Matplotlib] -> stage not stated [NetworkX]

### Multiplex generation and single-cell analysis of structural variants in mammalian genomes. (Science 2025)

- DOI: 10.1126/science.ado5978 | PMCID: PMC11931979 | PMID: 39883753
- Evidence: The set of barcodes associated with each well were determined as the barcode pairs whose readcounts were >1 standard deviation above the mean readcount for barcode pairs detected in that well using the zscore function in the scipy.stats library.
- Full pipeline: read trimming [Cutadapt v2.5] -> alignment/mapping [BEDTools v2.29.2] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Matplotlib v3.8.1, Python, R, SciPy, Seurat v4.3.1, scDblFinder v0.2.3, seaborn v0.13.0]

### Induction of broadly neutralizing HIV antibodies by a two-step mechanism informs vaccine design. (Science 2026)

- DOI: 10.1126/science.aec6396 | PMCID: PMC13308464 | PMID: 42096521
- Version used: **0.18.0**
- Evidence: Statistical analyses Statistical tests were calculated in GraphPad Prism 10 (version 10.4.2) or using the Stats module from SciPy (version 0.18.0) ( 99 ).
- Full pipeline: alignment/mapping [MUSCLE] -> differential/statistical testing [SciPy v0.18.0] -> structure determination [ChimeraX, Coot v0.8.9, PHENIX] -> visualisation [PyMOL]

### Lifelong behavioral screen reveals an architecture of vertebrate aging. (Science 2026)

- DOI: 10.1126/science.aea9795 | PMCID: PMC13165398 | PMID: 41818367
- Evidence: Velocity was calculated for all key points after first filtering data using scipy.signal.lfilter to alleviate the impact of key point jitter.
- Full pipeline: quality control [Cutadapt v3.1, FastQC] -> read trimming [Cutadapt v3.1, FastQC] -> alignment/mapping [STAR v2.7.1a] -> quantification [STAR v2.7.1a] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler, statsmodels] -> simulation/modelling [clusterProfiler] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [BLAST, Bioconductor, NumPy, SciPy]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: Downstream analyses were performed in Python, using a combination of numpy, scipy, Pandas, scikit-learn, pomegranate, infercnvpy, pygenometracks, scanpy and seaborn libraries as described before ( 49 , 52 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

### Structural ontogeny of protein-protein interactions. (Science 2026)

- DOI: 10.1126/science.adx6931 | PMCID: PMC12904254 | PMID: 41678610
- Evidence: The amplicons were amplified using the following primers: Illumina forward primer: 5'-AATGATACGGCGACCACCGAGATCTACACTCTTTCCCTACACGACGCTCTTCCGA-3' Illumina reverse primer: 5'-CAAGCAGAAGACGGCATACGAGATCGGTCTCGGCATTCCTGCTGAACCGCTCTTC-3' Sequence library filter To identify enriched oligopeptide pairs, a one-sided hypergeometric test was performed using the scipy.stats library.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CCP4, MACS2, SciPy, igraph]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Evidence: We then subsetted the previously estimated cell subset loadings [cell subsets x factors] for the 34 cell subsets that were shared between human, marmoset and mouse and used scipy’s (v1.7.1) implementation of non-negative least squares (scipy.optimisation.nnls) to estimate the [CREs x factors] matrix.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

### Ontogeny of the spinal cord dorsal horn. (Science 2026)

- DOI: 10.1126/science.adx5781 | PMCID: PMC12879194 | PMID: 41505538
- Evidence: The progression of neuronal cell types along the inferred trajectory was analyzed by calculating pairwise pseudotime distances between mean pseudotime values of each group using scipy.spatial.distance.pdist.
- Full pipeline: quality control [R v4.4.1, Seurat] -> dimensionality reduction/clustering [AnnData, R v4.4.1, Seurat, UMAP] -> simulation/modelling [SciPy] -> visualisation [ggplot2] -> stage not stated [ImageJ]

