# Singularity

- **Category:** workflow
- **Papers in survey:** 19
- **Journals:** PNAS (9), Nature (8), Cell (2)
- **Years:** 2021 (1), 2022 (3), 2023 (1), 2024 (4), 2025 (8), 2026 (2)
- **Versions named:** 1.1.8 (1), 3.2.1 (1), 3.8 (1)

## Papers

### A family of conserved bacterial virulence factors dampens interferon responses by blocking calcium signaling. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.028 | PMCID: PMC9596379 | PMID: 35568036
- Evidence: (2021) N/A Nfcore/rnaseq pipeline V 3.5 ( Ewels et al., 2020 ) N/A ( Ewels et al., 2020 ) Nextflow domain specific language V 19.10.0 ( Di Tommaso et al., 2017 ) N/A ( DI Tommaso et al., 2017 ) Singularity V 2.6.0 ( Kurtzer et al., 2017 ) N/A( Kurtzer et al., 2017 ) RSEM-STAR Dobin et al.
- Full pipeline: alignment/mapping [Clustal Omega] -> dimensionality reduction/clustering [DESeq2 v1.28.0, GSEA, R] -> differential/statistical testing [GSEA] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, BLAST, ImageJ, Nextflow, RSEM, Singularity]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: DECLARATION OF INTERESTS H.H. is co-founder and chief scientific officer of Omniscope, a scientific advisory board member at Nanostring/Bruker and Mirxes, a consultant for Moderna and Singularity, and has received honoraria from Genentech.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Version used: **3.2.1**
- Evidence: To facilitate reproducible analysis, samples were processed using the publicly available nf-core/RNA-seq pipeline version 1.4.2 implemented in Nextflow 19.10.0 using Singularity 3.2.1–1 with the minimal command nextflow run nf-core/rnaseq -r 1.4.2 –singleEnd -profile singularity –reverseStranded --three_prime_clip_r2 3 53 – 55 .
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Multi-omic machine learning predictor of breast cancer therapy response. (Nature 2022)

- DOI: 10.1038/s41586-021-04278-5 | PMCID: PMC8791834 | PMID: 34875674
- Evidence: Predictor architecture The machine learning framework was built on Python (version 3.7.4) using the following libraries: scikit-learn (version 0.21.2), numpy (version 1.16.4), scipy (version 1.3), pandas (version 0.24.2) within a Singularity container (version 2.4.6-dist).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC, edgeR] -> alignment/mapping [HTSeq v0.6.1p, STAR v2.5.2b] -> variant calling [Mutect2 v4.1.4] -> quantification [HTSeq v0.6.1p] -> normalisation [edgeR] -> registration [GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [pheatmap] -> stage not stated [ANNOVAR, GSEA, GSVA, NumPy v1.16.4, OpenCV, Picard v2.17.0, Python, R, SciPy v1.3, Singularity, VEP, scikit-learn v0.21.2]

### An integrated transcriptomic cell atlas of human neural organoids. (Nature 2024)

- DOI: 10.1038/s41586-024-08172-8 | PMCID: PMC11578878 | PMID: 39567792
- Evidence: Competing interests F.J.T. consults for Immunai Inc., Singularity Bio B.V., CytoReason Ltd, Cellarity, and has ownership interest in Dermagnostix GmbH and Cellarity.
- Full pipeline: read trimming [UMAP] -> alignment/mapping [RSEM] -> dimensionality reduction/clustering [SciPy, UMAP] -> structure determination [Python] -> machine learning [R] -> stage not stated [AnnData, Jupyter, Scanpy, Singularity, edgeR]

### Morphodynamics of human early brain organoid development. (Nature 2025)

- DOI: 10.1038/s41586-025-09151-3 | PMCID: PMC12390842 | PMID: 40533563
- Evidence: Singularity of clones was tracked using an EVOS XL Core over the course of 7 days.
- Full pipeline: alignment/mapping [Bowtie2, STAR v2.7.11b] -> quantification [RSEM v1.2.28] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Scanpy, UMAP] -> machine learning [scikit-image v1.1.1, scikit-learn v0.18.3] -> visualisation [Matplotlib v3.5.2] -> stage not stated [BigStitcher, Cellpose, R v4.4.0, SciPy, Seurat, Singularity, ilastik]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Version used: **1.1.8**
- Evidence: We used the cactus-pangenome command within an Apptainer (v1.1.8) Image 81 ( https://quay.io/comparative-genomics-toolkit/cactus:v2.6.7-gpu ) and the following parameter flags: --reference EH23a EH23b --vcf --vcfReference EH23a EH23b --giraffe --chrom-og --chrom-vg --viz --gfa --gbz.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Molecular basis of SIFI activity in the integrated stress response. (Nature 2025)

- DOI: 10.1038/s41586-025-09074-z | PMCID: PMC12286842 | PMID: 40328314
- Evidence: The trap was brought online with a Bruker PepSep C18 15 cm × 150 µm, 1.9 µm column (Thermo Fisher Scientific, 1893471) connected to a 5 cm × 20 µm inner diameter Sharp Singularity Fossil Ion Tech tapered tip mounted in a custom constructed microspray source.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [AlphaFold, ChimeraX, PyMOL, Singularity]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: Competing interests F.J.T. consults for Immunai, Singularity Bio, CytoReason, Cellarity and Omniscope, and has ownership interest in Dermagnostix and Cellarity.
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### Cusp-singularity-enhanced Coriolis effect for sensitive chip-scale gyroscopes. (Nature 2026)

- DOI: 10.1038/s41586-026-10565-w | PMCID: PMC13190237 | PMID: 42162388
- Evidence: Singularity-enabled PM measurements Furthermore, we find that, when the PhT system operates near X 1,2 , the relative phase ϑ can be a superior metric for rotation readout than the PhT frequency, enabling a PM gyroscope that achieves strategic-grade SNR on silicon chips.
- Full pipeline: stage not stated [Singularity]

### Proteasome complexes experience profound structural and functional rearrangements throughout mammalian spermatogenesis. (PNAS 2022)

- DOI: 10.1073/pnas.2116826119 | PMCID: PMC9169623 | PMID: 35377789
- Evidence: HDX-MS Rationalizes the Spermatoproteasome Structural Singularity.
- Full pipeline: stage not stated [Singularity]

### Mammals sustain amino acid homochirality against chiral conversion by symbiotic microbes. (PNAS 2023)

- DOI: 10.1073/pnas.2300817120 | PMCID: PMC10104486 | PMID: 37014864
- Evidence: NBD-conjugated amino acids were separated on an octadecylsilyl column (Singularity RP18, 1.0 mm inner diameter (ID) × 250 mm) (designed by Kyushu University and KAGAMI Co.
- Full pipeline: stage not stated [Singularity]

### Hierarchical gradients of multiple timescales in the mammalian forebrain. (PNAS 2024)

- DOI: 10.1073/pnas.2415695121 | PMCID: PMC11665873 | PMID: 39671181
- Evidence: This work was supported by a grant from the National Research Foundation of Korea funded by the Korean government NRF-2022R1A2C3008991 (S.-B.P.), the Singularity Professor Research Project of KAIST (S.-B.P.), the National Institute of Health NS118463 (H.S.), MH137210 (D.L), DA047870 (A.S.), and the Research Center Program of the Institute for Basic Science IBS-R002-A1 (M.W.J.).
- Full pipeline: stage not stated [Singularity]

### Evolutionary origins of the lysosome-related organelle sorting machinery reveal ancient homology in post-endosome trafficking pathways. (PNAS 2024)

- DOI: 10.1073/pnas.2403601121 | PMCID: PMC11513930 | PMID: 39418309
- Version used: **3.8**
- Evidence: The TransRate version used was packaged as a part of the Oyster River Protocol ( 81 ) ( https://hub.docker.com/r/macmaneslab/orp ), and executed using Singularity v.
- Full pipeline: quality control [Kraken2] -> read trimming [Kraken2] -> alignment/mapping [ChimeraX] -> stage not stated [AlphaFold, BLAST, BUSCO v5.2.2, HMMER, IQ-TREE, InterProScan, Singularity v3.8]

### APACE: AlphaFold2 and advanced computing as a service for accelerated discovery in biophysics. (PNAS 2024)

- DOI: 10.1073/pnas.2311888121 | PMCID: PMC11228474 | PMID: 38913887
- Evidence: Methods Given that Delta and Polaris’s container support is only available for Apptainer/Singularity ( 39 ), we modified the instructions provided in AlphaFold2 GitHub repository, which are intended for Docker containers ( 40 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, Docker, Singularity, Slingshot]

### Profile of Thomas Y. Hou. (PNAS 2025)

- DOI: 10.1073/pnas.2516518122 | PMCID: PMC12318202 | PMID: 40699922
- Evidence: 3D Euler Singularity Research Hou is now a leading figure in research on the Euler and Navier–Stokes equations.
- Full pipeline: stage not stated [Singularity]

### Singularity formation in 3D Euler equations with smooth initial data and boundary. (PNAS 2025)

- DOI: 10.1073/pnas.2500940122 | PMCID: PMC12260595 | PMID: 40577113
- Evidence: Singularity and asymptotics of weights.
- Full pipeline: stage not stated [Singularity]

### A skin-interfaced wireless wearable device and data analytics approach for sleep-stage and disorder detection. (PNAS 2025)

- DOI: 10.1073/pnas.2501220122 | PMCID: PMC12168010 | PMID: 40478868
- Evidence: ( D ) Singularity spectrum of RRV-MFDFA alpha1 peaks at NREM and REM stages.
- Full pipeline: differential/statistical testing [XGBoost] -> stage not stated [Singularity]

### Aging-associated differences in mammary tumor-initiating populations and immune evasion pathways in breast cancer. (PNAS 2026)

- DOI: 10.1073/pnas.2523254123 | PMCID: PMC12933083 | PMID: 41719331
- Evidence: Somatic mutation calling was performed using the nf-core/sarek pipeline (v3.4.1) with Singularity ( 55 , 56 ).
- Full pipeline: variant calling [GATK] -> quantification [GSVA, R] -> normalisation [Seurat v5.2.0, edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Seurat v5.2.0, UMAP] -> differential/statistical testing [survival (R)] -> visualisation [ComplexHeatmap, Metascape] -> stage not stated [CNVkit, DESeq2, GSEA, QuPath v0.5.1, Singularity, VEP]

