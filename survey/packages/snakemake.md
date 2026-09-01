# Snakemake

- **Category:** workflow
- **Papers in survey:** 54
- **Journals:** Nature (24), PNAS (18), Cell (11), Science (1)
- **Years:** 2021 (5), 2022 (9), 2023 (8), 2024 (10), 2025 (14), 2026 (8)
- **Versions named:** 7.21.0 (2), 5.5.4 (2), 8.18.2 (1), 7.24.0 (1), 7.15.1 (1), 5.26.0 (1), 7.32.3 (1), 7.32.4 (1), 7.22.0 (1), 7.0.1 (1)
- **Pipeline stages it appears in:** alignment/mapping (6), dimensionality reduction/clustering (3), read trimming (3), variant calling (2), differential/statistical testing (2), visualisation (1), machine learning (1), quantification (1)

## Papers

### Whole-body integration of gene expression and single-cell morphology. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.017 | PMCID: PMC8445025 | PMID: 34380046
- Evidence: The script for calculation of morphological features is available here: https://github.com/mobie/platybrowser-datasets/blob/master/mmpb/extension/attributes/morphology_impl.py and the Snakemake workflow for clustering analysis is available here: https://github.com/mobie/platybrowser-datasets/tree/master/analysis/morphology_clustering .
- Full pipeline: dimensionality reduction/clustering [ImageJ, Python, Snakemake, UMAP, ilastik, scikit-image, scikit-learn] -> visualisation [BigStitcher] -> stage not stated [Bioconductor, NetworkX, NumPy, SciPy, tidyverse]

### TDP-43 condensation properties specify its RNA-binding and regulatory repertoire. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.018 | PMCID: PMC8445024 | PMID: 34380047
- Version used: **5.31.1**
- Evidence: ...re/prism/ R v 4.0.3 The R Project for Statistical Computing https://www.r-project.org/ Python v 3.7 Python Software Foundation https://www.python.org Snakemake v 5.31.1 Mölder et al., 2021 https://snakemake.github.io/ iCount; iMaps König et al., 2010 https://github.com/tomazc/iCount iCLIP analysis code; pAseq analysis pipeline and code This study https://github.com/ulelab/tdp43-mutants Resource av...
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools] -> quantification [Cutadapt, DESeq2] -> normalisation [DESeq2] -> differential/statistical testing [Fiji, ImageJ, Snakemake v5.31.1] -> visualisation [DESeq2] -> stage not stated [Python v3.7.3]

### Emergence of an early SARS-CoV-2 epidemic in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.030 | PMCID: PMC8313480 | PMID: 34508652
- Evidence: ...v0.1.0 BEAGLE Ayres et al., 2019 https://faculty.washington.edu/browning/beagle/beagle.html#download Baltic GitHub https://github.com/evogytis/baltic Snakemake Köster and Rahmann, 2012 https://snakemake.readthedocs.io/en/stable/ BWA-mem Li, 2013 https://github.com/lh3/bwa BreSeq v.0.34.1 Deatherage and Barrick, 2014 https://github.com/barricklab/breseq iVar v1.2.2 Grubaugh et al., 2019b https://gi...
- Full pipeline: stage not stated [BWA, Pangolin v2.0, R, Snakemake]

### The genomic history of the Aegean palatial civilizations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.039 | PMCID: PMC8127963 | PMID: 33930288
- Version used: **5.3.0**
- Evidence: 1.10 Li et al., 2009 https://github.com/samtools/samtools SeaView v5.0.4 Galtier et al., 1996 ; Gouy et al., 2010 http://doua.prabi.fr/software/seaview Snakemake v5.3.0 ( Mölder et al., 2021 ) https://snakemake.readthedocs.io/en/v5.3.0/ Tablet 1.19.09.03 Milne et al., 2013 https://ics.hutton.ac.uk/tablet/ Other Amicon Ultra-4 Centrifugal Filter Units, 30kDa Merck Millipore, Darmstadt, Germany Cat#...
- Full pipeline: alignment/mapping [BWA, R] -> variant calling [GATK v3.7] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools v1.4, PLINK v1.9, Picard, SAMtools v1.10, Snakemake v5.3.0]

### Emergence and rapid transmission of SARS-CoV-2 B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.052 | PMCID: PMC8009040 | PMID: 33861950
- Evidence: ...ome assembly & variant calling Deng et al., 2020 N/A Andersen Lab consensus calling for nanopore data https://github.com/artic-network/artic-ncov2019 Snakemake Köster and Rahmann, 2012 https://snakemake.readthedocs.io/en/stable/ bwa-mem Li, 2013 https://github.com/lh3/bwa iVar v1.2.2 Grubaugh et al., 2019b https://github.com/andersen-lab/ivar/releases/tag/v1.2.2 Transmissibility estimation Volz et...
- Full pipeline: variant calling [Snakemake] -> stage not stated [BWA, Pangolin v2.0]

### The genomic origins of the world's first farmers. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.008 | PMCID: PMC9166250 | PMID: 35561686
- Evidence: .../samtools/samtools seqtk - version 1.2 N/A https://github.com/lh3/seqtk SHAPEIT4 v1.2 ( Delaneau et al., 2019 ) https://odelaneau.github.io/shapeit4/ Snakemake - version 4.0 ( Köster and Rahmann, 2012 ) https://snakemake.readthedocs.io/en/stable/ Trim Galore! - version 0.4.3 Babraham Bioinformatics www.bioinformatics.babraham.ac.uk/projects/trim_galore/ Yjasc_3752_ry_compute.py, version 0.4 ( Skog...
- Full pipeline: quality control [BWA, GATK] -> alignment/mapping [BCFtools, BWA, R, SAMtools] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ANGSD, ANNOVAR, BEDTools, Picard, Snakemake, Trim Galore]

### Pyramidal neurons form active, transient, multilayered circuits perturbed by autism-associated mutations at the inception of neocortex. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.025 | PMCID: PMC10156177 | PMID: 37071993
- Version used: **5.19.3**
- Evidence: The workflow for the analysis was managed using Snakemake (v5.19.3).
- Full pipeline: alignment/mapping [Python v3.7.7] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scDblFinder v0.2.1] -> stage not stated [Snakemake v5.19.3]

### A pseudovirus system enables deep mutational scanning of the full SARS-CoV-2 spike. (Cell 2023)

- DOI: 10.1016/j.cell.2023.02.001 | PMCID: PMC9922669 | PMID: 36868218
- Evidence: The dms-vep-pipeline consists of a series of Snakemake 72 rules that run Python scripts or Jupyter notebooks, and specifies a conda environment that provides details on the software used for the analysis.
- Full pipeline: stage not stated [Jupyter, Nextstrain, Python, Snakemake]

### Clonal hematopoiesis driven by mutated DNMT3A promotes inflammatory bone loss. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.003 | PMCID: PMC11246233 | PMID: 38838669
- Evidence: Whole-genome bisulfite sequencing analysis The reads were mapped to mouse genome “mm10” using BISulfite-seq CUI Toolkit (BISCUIT), as described in https://github.com/huishenlab/Biscuit_Snakemake_Workflow .
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR, Snakemake] -> normalisation [R, Seurat v4.3.0, UMAP] -> dimensionality reduction/clustering [R, Seurat v4.3.0, UMAP] -> stage not stated [ANNOVAR, CellChat, GATK, Mutect2]

### Vertebrate centromeres in mitosis are functionally bipartite structures stabilized by cohesin. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.014 | PMCID: PMC11164432 | PMID: 38744280
- Evidence: ChIP-seq datasets were processed using a custom built Snakemake pipeline.
- Full pipeline: read trimming [BWA v0.7.16, Cutadapt v1.18, ImageJ, LAMMPS, Trimmomatic v0.36, deepTools] -> stage not stated [Snakemake]

### Mapping chromatin structure at base-pair resolution unveils a unified model of cis-regulatory element interactions. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.013 | PMCID: PMC7618578 | PMID: 41197626
- Evidence: Quantification and Statistical Analysis Micro-Capture-C analysis Data were analysed using the MCCuAnalysis Snakemake pipeline.
- Full pipeline: read trimming [Trim Galore] -> quantification [Snakemake] -> differential/statistical testing [Snakemake] -> structure determination [Trim Galore] -> stage not stated [BEDTools, Bowtie2, DESeq2, LAMMPS, MACS2]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Evidence: To improve reproducibility and transparency, Snakemake ( https://snakemake.readthedocs.io/en/stable/ ) 81 was used for pipeline construction and execution (10.18434/mds2-2578).
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### Spatial profiling of chromatin accessibility in mouse and human tissues. (Nature 2022)

- DOI: 10.1038/s41586-022-05094-1 | PMCID: PMC9452302 | PMID: 35978191
- Evidence: A preprocessing pipeline we developed using Snakemake workflow management system (v5.28.0) is available at GitHub ( https://github.com/dyxmvp/Spatial_ATAC-seq ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [Python, Seurat] -> stage not stated [ArchR, Snakemake]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **7.0.1**
- Evidence: The corresponding pipeline was constructed using Snakemake (v.7.0.1) 103 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Nonlinear control of transcription through enhancer-promoter interactions. (Nature 2022)

- DOI: 10.1038/s41586-022-04570-y | PMCID: PMC9021019 | PMID: 35418676
- Evidence: Nanopore sequencing analysis has been implemented using Snakemake workflow (v.3.13.3).
- Full pipeline: alignment/mapping [BWA, Bowtie2, Cutadapt, SAMtools, minimap2 v2.17] -> quantification [Bioconductor] -> stage not stated [R, Snakemake, TrackMate]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Version used: **5.5.4**
- Evidence: Our alignment pipeline is implemented in Snakemake version 5.5.4 43 and available at: https://github.com/frattalab/rna_seq_snakemake .
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### Early prediction of preeclampsia in pregnancy with cell-free RNA. (Nature 2022)

- DOI: 10.1038/s41586-022-04410-z | PMCID: PMC8971130 | PMID: 35140405
- Version used: **5.8.1**
- Evidence: Across samples, the bioinformatic pipeline was managed using Snakemake (v.5.8.1).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.7] -> read trimming [STAR v2.7.3a, Trimmomatic v0.36] -> alignment/mapping [HTSeq v0.11.1, STAR v2.7.3a, Trimmomatic v0.36] -> quantification [HTSeq v0.11.1] -> normalisation [limma] -> dimensionality reduction/clustering [Python v3.6, SciPy, scikit-learn, seaborn] -> differential/statistical testing [FastQC v0.11.8, MultiQC v1.7] -> visualisation [Python v3.6, SciPy, scikit-learn, seaborn] -> stage not stated [GATK, R v3.5, Snakemake v5.8.1, statsmodels]

### Single-cell DNA methylome and 3D multi-omic atlas of the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06805-y | PMCID: PMC10719113 | PMID: 38092913
- Evidence: Snakemake 65 pipeline files with detailed mapping steps are provided in the Code availability section.
- Full pipeline: quality control [Bowtie2, Cutadapt, Picard v3.0.0, SAMtools] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, Snakemake] -> quantification [kallisto] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, Dask, Enrichr, Jupyter, SCENIC, Scanpy, deepTools, scikit-learn]

### Antiviral type III CRISPR signalling via conjugation of ATP and SAM. (Nature 2023)

- DOI: 10.1038/s41586-023-06620-5 | PMCID: PMC10600005 | PMID: 37853119
- Version used: **7.22.0**
- Evidence: These steps were wrapped in a Snakemake 7.22.0 49 pipeline and an R script (available at Github: https://github.com/vihoikka/Cas10_prober ).
- Full pipeline: visualisation [R v4.1, ggplot2] -> stage not stated [AlphaFold, Snakemake v7.22.0]

### Recurrent evolution and selection shape structural diversity at the amylase locus. (Nature 2024)

- DOI: 10.1038/s41586-024-07911-1 | PMCID: PMC11485256 | PMID: 39232174
- Version used: **7.32.3**
- Evidence: Haplotype deconvolution approach We implemented a pipeline based on the workflow language Snakemake (v7.32.3) to parallelize haplotype deconvolution (that is, assign to a short-read-sequenced individual the haplotype pair in a pangenome that best represents its genotype at a given locus) in thousands of samples.
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [R v4.2.2, Snakemake v7.32.3, VCFtools v0.1.16] -> differential/statistical testing [R v4.2.2, ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, IQ-TREE v2.2.2.3, Python, SAMtools, minimap2]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Evidence: ATAC-seq data processing and analysis ATAC-seq data processing was performed using a Snakemake pipeline (v6.1.1) 72 .
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### Improving prime editing with an endogenous small RNA-binding protein. (Nature 2024)

- DOI: 10.1038/s41586-024-07259-6 | PMCID: PMC11023932 | PMID: 38570691
- Version used: **7.32.4**
- Evidence: The reads were trimmed, aligned and processed using a Snakemake (7.32.4) workflow 49 and R (4.3.2) (scripts available at Zenodo (10.5281/zenodo.10553303) 50 or at GitHub ( https://github.com/Princeton-LSI-ResearchComputing/PE-small-RNA-seq-analysis ) 51 ).
- Full pipeline: read trimming [Bowtie2 v2.5.0, Cutadapt v4.1, Snakemake v7.32.4] -> alignment/mapping [Bowtie2 v2.5.0, STAR, Snakemake v7.32.4] -> quantification [STAR] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [ggplot2 v3.4.1, ggpubr v0.6.0] -> stage not stated [tidyverse v1.1.3]

### Single-cell multiplex chromatin and RNA interactions in ageing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07239-w | PMCID: PMC11023937 | PMID: 38538789
- Evidence: Computational analysis The MUSIC-docker data-processing pipeline We developed MUSIC-docker to process MUSIC sequencing data using Docker to encapsulate a Snakemake 57 pipeline, ensuring cross-platform execution.
- Full pipeline: alignment/mapping [Bowtie2 v5.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Docker, Harmony v0.1.1, R, Seurat v4.3.0, Snakemake]

### Efficient and accurate search in petabase-scale sequence repositories. (Nature 2025)

- DOI: 10.1038/s41586-025-09603-w | PMCID: PMC12657231 | PMID: 41062695
- Evidence: ... a Python API client, the project includes unit tests, benchmarks and integration tests for testing the APIs and the command line interface, a set of Snakemake workflows (compatible with versions ≥5) for simplified index construction and detailed documentation.
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.0] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [Docker, Python, R v71.2, Snakemake]

### Systematic discovery of CRISPR-boosted CAR T cell immunotherapies. (Nature 2025)

- DOI: 10.1038/s41586-025-09507-9 | PMCID: PMC12545207 | PMID: 40993398
- Version used: **7.21.0**
- Evidence: The analyses and visualizations described here were performed using a publicly available Snakemake (7.21.0) 60 workflow (v.1.0.1) 61 .
- Full pipeline: read trimming [Cutadapt v3.4] -> normalisation [limma v3.46.0] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [limma v3.46.0] -> visualisation [PyMOL, Snakemake v7.21.0] -> stage not stated [BEDTools v2.30.0, GSEA, R, SAMtools, edgeR v3.32.1]

### Pathology-oriented multiplexing enables integrative disease mapping. (Nature 2025)

- DOI: 10.1038/s41586-025-09225-2 | PMCID: PMC12350167 | PMID: 40681898
- Evidence: Bulk RNA-sequencing data were processed using our previously published open-source Snakemake 65 workflow for RNA-sequencing analysis with pytximport 66 .
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> quantification [Cellpose, Scanpy, statsmodels] -> registration [Matplotlib, seaborn] -> dimensionality reduction/clustering [Cellpose, Matplotlib, Scanpy, scikit-learn, seaborn, statsmodels] -> differential/statistical testing [statsmodels] -> machine learning [Matplotlib, seaborn] -> visualisation [Fiji, ImageJ, Matplotlib, seaborn] -> stage not stated [AnnData, NetworkX, NumPy, OpenCV, SciPy, Seurat, Snakemake, TrackMate, scikit-image]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Evidence: We developed a Snakemake workflow for running TSEBRA, available here: https://gitlab.com/salk-tm/snake_tsebra .
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Connectome-driven neural inventory of a complete visual system. (Nature 2025)

- DOI: 10.1038/s41586-025-08746-0 | PMCID: PMC12119369 | PMID: 40140576
- Evidence: We defined workflows for long-running and multistep computations with Snakemake 84 .
- Full pipeline: dimensionality reduction/clustering [Python, SciPy] -> structure determination [BigStitcher] -> stage not stated [Jupyter, NumPy, Snakemake]

### Large-scale discovery, analysis and design of protein energy landscapes. (Nature 2026)

- DOI: 10.1038/s41586-026-10465-z | PMCID: PMC13293878 | PMID: 42129553
- Evidence: These pipelines are implemented using Snakemake 83 , 84 , enabling reproducible, scalable and parallel processing across compute clusters, thereby enhancing workflow efficiency and facilitating easy re-execution of the entire analysis.
- Full pipeline: dimensionality reduction/clustering [Snakemake] -> stage not stated [AlphaFold, ColabFold, Jupyter, SciPy]

### Transposable elements are driving rapid adaptation of Enterococcus faecium. (Nature 2026)

- DOI: 10.1038/s41586-026-10373-2 | PMCID: PMC13216065 | PMID: 42020750
- Version used: **8.18.2**
- Evidence: For compatibility with our high-performance computing cluster, the PanGraph workflow was adapted to work for Snakemake (v.8.18.2).
- Full pipeline: read trimming [MAFFT, Trim Galore] -> alignment/mapping [BEDTools v2.27.1, MAFFT, minimap2] -> dimensionality reduction/clustering [Snakemake v8.18.2] -> differential/statistical testing [DESeq2] -> visualisation [R] -> stage not stated [Bowtie2, Flye, NanoPlot, Nextflow, Python, SAMtools]

### Focal white matter lesions drive grey matter inflammation and synapse loss. (Nature 2026)

- DOI: 10.1038/s41586-026-10414-w | PMCID: PMC13293868 | PMID: 42020752
- Version used: **7.24.0**
- Evidence: Spatial barcode demultiplexing and FASTQ file preparation were performed using Snakemake (v.7.24.0) 63 as the workflow management system.
- Full pipeline: read trimming [Snakemake v7.24.0] -> quantification [ImageJ v1.54p] -> dimensionality reduction/clustering [UMAP] -> visualisation [Bioconductor, ComplexHeatmap, UMAP] -> stage not stated [Python, R, Seurat, igraph]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Version used: **7.21.0**
- Evidence: Single-cell transcriptome analysis Sequencing reads were processed to obtain gene counts using Snakemake (v.7.21.0) 88 , a robust workflow management system.
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### Multiomics and deep learning dissect regulatory syntax in human development. (Nature 2026)

- DOI: 10.1038/s41586-026-10326-9 | PMCID: PMC13216069 | PMID: 41951735
- Version used: **7.15.1**
- Evidence: SHARE-seq data pre-processing We developed a highly parallelized, rapid, and storage-efficient pre-processing Snakemake (v7.15.1) 92 pipeline to convert BCL files from sequencers to ATAC fragment files and RNA sparse matrices (Extended Data Fig.
- Full pipeline: read trimming [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> alignment/mapping [Bowtie2 v2.5.0, STAR v2.5.4b, fastp v0.23.2, featureCounts v2.0.1] -> normalisation [R v4.1.2, Seurat v4.3.0] -> dimensionality reduction/clustering [R v4.1.2, Seurat v4.3.0, UMAP] -> stage not stated [ArchR v1.0.2, BEDTools, Bioconductor, Snakemake v7.15.1]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Evidence: Reads were processed using a Snakemake workflow based on the CLAPAnalysis pipeline 54 , with modified alignment parameters.
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Long-read metagenomics reveals phage dynamics in the human gut microbiome. (Nature 2026)

- DOI: 10.1038/s41586-025-09786-2 | PMCID: PMC12823448 | PMID: 41299176
- Version used: **5.26.0**
- Evidence: VirSorter2 was run separately because it relies on Snakemake (v.5.26.0) for execution.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.5.4, Clustal Omega v1.2.4, NanoPlot v1.41.6, SAMtools v1.21, minimap2 v2.26] -> differential/statistical testing [R v4.2.2] -> visualisation [R v4.2.2, ggplot2 v3.5.1, tidyverse v2.0.0] -> stage not stated [Flye, HMMER v3.4, Snakemake v5.26.0]

### Comprehensive mapping of alternative polyadenylation site usage and its dynamics at single-cell resolution. (PNAS 2022)

- DOI: 10.1073/pnas.2113504119 | PMCID: PMC9894249 | PMID: 36454750
- Evidence: We developed a de-novo polyA site identification pipeline with Snakemake ( 49 ), named scPolyA-pipe, to identify a polyA site from sequence data ( https://github.com/WangJL2021/scPolyA-seq ).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Trim Galore v0.6.1] -> alignment/mapping [STAR v2.5.2b] -> quantification [HTSeq] -> dimensionality reduction/clustering [Seurat v3.1.5, UMAP] -> differential/statistical testing [DESeq2, R v3.6.0] -> stage not stated [BEDTools, Metascape, Snakemake]

### Estimating bonobo (<i>Pan</i><i>paniscus</i>) and chimpanzee (<i>Pan</i><i>troglodytes</i>) evolutionary history from nucleotide site patterns. (PNAS 2022)

- DOI: 10.1073/pnas.2200858119 | PMCID: PMC9170072 | PMID: 35452306
- Evidence: 71 and contained in an automated Snakemake ( 73 ) available on GitHub ( https://github.com/thw17/Pan_reassembly ).
- Full pipeline: visualisation [ggplot2 v3.3.3] -> stage not stated [BCFtools, Conda, Jupyter, Snakemake]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Evidence: Pore-C reads (for D. oliveri ) were mapped to the draft genome assembly and used to generate contact map with the Pore-C-Snakemake ( https://github.com/nanoporetech/Pore-C-Snakemake ) and produce a merged_nodups (.mnd) file, which contains a duplicate-free list of paired alignments from the Pore-C reads to the draft assembly.
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### A genome-wide optical pooled screen reveals regulators of cellular antiviral responses. (PNAS 2023)

- DOI: 10.1073/pnas.2210623120 | PMCID: PMC10120039 | PMID: 37043539
- Evidence: Data analysis functions were written in Python using Snakemake for workflow control ( 58 ).
- Full pipeline: alignment/mapping [scikit-image] -> quantification [kallisto] -> normalisation [GSEA] -> differential/statistical testing [Enrichr, edgeR] -> structure determination [scikit-image] -> stage not stated [DESeq2, Keras, Python, Snakemake]

### The genomics of linkage drag in inbred lines of sunflower. (PNAS 2023)

- DOI: 10.1073/pnas.2205783119 | PMCID: PMC10083583 | PMID: 36972449
- Evidence: To ensure that we were not overestimating gene-content variation among the 10 sunflower genomes, we developed a pipeline to filter out gene fragments resulting from TE activity and other genomic processes ( https://github.com/megahitokiri/Sunflower_annotation_Snakemake ) ( 80 ).
- Full pipeline: alignment/mapping [GATK] -> differential/statistical testing [R] -> stage not stated [BUSCO v5.1.2, Snakemake, VCFtools]

### Genes and sites under adaptation at the phylogenetic scale also exhibit adaptation at the population-genetic scale. (PNAS 2023)

- DOI: 10.1073/pnas.2214977120 | PMCID: PMC10089192 | PMID: 36897968
- Evidence: The Snakemake pipeline for integrating polymorphism and divergence data uses custom scripts written in Python 3.9.
- Full pipeline: stage not stated [Python v3.9, Snakemake]

### BIFROST: A method for registering diverse imaging datasets of the &lt;i&gt;Drosophila&lt;/i&gt; brain. (PNAS 2024)

- DOI: 10.1073/pnas.2322687121 | PMCID: PMC11588091 | PMID: 39541350
- Evidence: We provide the BIFROST pipeline as a Snakemake workflow that describes the dependency structure of the whole pipeline ( 64 ).
- Full pipeline: alignment/mapping [scikit-image] -> registration [ANTs, ImageJ] -> visualisation [Jupyter] -> stage not stated [Snakemake]

### Dynamics of transcription-coupled repair of cyclobutane pyrimidine dimers and (6-4) photoproducts in &lt;i&gt;Escherichia coli&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416877121 | PMCID: PMC11536166 | PMID: 39441633
- Evidence: The data analysis is fully reproducible, facilitated by a Snakemake workflow for scalability.
- Full pipeline: read trimming [Cutadapt v3.4, STAR] -> alignment/mapping [Bowtie2 v2.4.5, STAR] -> stage not stated [BEDTools, Snakemake]

### Plasma cell-free RNA signatures of inflammatory syndromes in children. (PNAS 2024)

- DOI: 10.1073/pnas.2403897121 | PMCID: PMC11406294 | PMID: 39240972
- Evidence: Machine learning algorithms were trained using the Caret R package, and pipelines were run using the Snakemake workflow management system ( 50 , 51 ).
- Full pipeline: quality control [SAMtools v1.14] -> alignment/mapping [SAMtools v1.14] -> quantification [DESeq2, R] -> machine learning [Snakemake] -> stage not stated [featureCounts]

### Nanorate sequencing reveals the &lt;i&gt;Arabidopsis&lt;/i&gt; somatic mutation landscape. (PNAS 2025)

- DOI: 10.1073/pnas.2514194122 | PMCID: PMC12685076 | PMID: 41296725
- Evidence: These commands were run as a Snakemake pipeline ( 107 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2] -> stage not stated [MACS2, SAMtools, SciPy, Snakemake]

### Genome-wide strand-specific UV mutagenesis in &lt;i&gt;&lt;i&gt;Escherichia coli&lt;/i&gt;&lt;/i&gt; is directed by the Mfd translocase. (PNAS 2025)

- DOI: 10.1073/pnas.2523368122 | PMCID: PMC12646321 | PMID: 41231941
- Evidence: All steps were executed using a reproducible Snakemake ( 31 ) workflow, with isolated software environments managed through Conda.
- Full pipeline: read trimming [STAR v2.7, Trimmomatic] -> alignment/mapping [SAMtools, STAR v2.7] -> normalisation [deepTools] -> stage not stated [Conda, Snakemake]

### Genetic, phenotypic, and environmental drivers of local adaptation and climate change-induced maladaptation in a migratory songbird. (PNAS 2025)

- DOI: 10.1073/pnas.2518497122 | PMCID: PMC12519128 | PMID: 41021811
- Evidence: To process sequence data, we used the workflow management system Snakemake to create a reproducible bioinformatics pipeline ( 62 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, GATK v4.1.6.0, SAMtools v1.16] -> variant calling [BCFtools v1.16, GATK v4.1.6.0] -> differential/statistical testing [GEMMA v0.98.3] -> stage not stated [BEDTools, Picard, R, Snakemake]

### Circulating cell-free RNA signatures for the characterization and diagnosis of myalgic encephalomyelitis/chronic fatigue syndrome. (PNAS 2025)

- DOI: 10.1073/pnas.2507345122 | PMCID: PMC12377778 | PMID: 40789036
- Evidence: Bioinformatic pipelines were run using the Snakemake workflow management system ( 71 ).
- Full pipeline: quantification [Bracken] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> machine learning [DESeq2 v1.34.0] -> visualisation [ggplot2 v3.3.5] -> stage not stated [Kraken2, Snakemake]

### SCoTCH-seq reveals that 5-hydroxymethylcytosine encodes regulatory information across DNA strands. (PNAS 2025)

- DOI: 10.1073/pnas.2512204122 | PMCID: PMC12337322 | PMID: 40743391
- Version used: **7.3.8**
- Evidence: CpG states were extracted by processing raw reads using a custom bioinformatics pipeline [Snakemake v7.3.8 ( 42 )].
- Full pipeline: read trimming [Cutadapt v4.6, Picard v3.1.1, SAMtools v1.19.2] -> stage not stated [BEDTools v2.31.0, Snakemake v7.3.8, deepTools]

### Accurate, scalable, and fully automated inference of species trees from raw genome assemblies using ROADIES. (PNAS 2025)

- DOI: 10.1073/pnas.2500553122 | PMCID: PMC12088440 | PMID: 40314967
- Evidence: We have implemented ROADIES as a Snakemake workflow ( 109 ), which allows modular implementation and exposes numerous parameters of individual tools to end users to provide flexibility ( SI Appendix ).
- Full pipeline: stage not stated [BUSCO, MAFFT, RAxML, Snakemake]

### Large-scale combination screens reveal small-molecule sensitization of antibiotic-resistant gram-negative ESKAPE pathogens. (PNAS 2025)

- DOI: 10.1073/pnas.2402017122 | PMCID: PMC12002207 | PMID: 40127266
- Evidence: A Snakemake analysis pipeline was developed for the integration of DropArray image analysis and antibiotic potentiation scoring with previously developed custom Python scripts ( SI Appendix , SI Methods ) ( 18 ).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Cutadapt v3.4] -> stage not stated [Python, Snakemake]

### Long-term B cell memory emerges at uniform relative rates in the human immune response. (PNAS 2025)

- DOI: 10.1073/pnas.2406474122 | PMCID: PMC11892634 | PMID: 40020190
- Evidence: To promote reproducibility, we used the Snakemake workflow manager ( 46 ).
- Full pipeline: stage not stated [Snakemake]

### Sex-allocation trade-offs and their genetic architecture revealed by experimental evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2427240123 | PMCID: PMC12799159 | PMID: 41490487
- Evidence: We used the demultiplexed Illumina reads in an integrated analysis pipeline implemented in a reproducible Snakemake workflow ( 64 , 65 ), to build linkage maps and run QTL-analyses for each cross separately (see Supporting Information).
- Full pipeline: read trimming [Snakemake]

### Creation of de novo cryptic splicing for ALS and FTD precision medicine. (Science 2024)

- DOI: 10.1126/science.adk2539 | PMCID: PMC7616720 | PMID: 39361759
- Version used: **5.5.4**
- Evidence: Splice junction parsing pipeline is implemented in Snakemake version 5.5.4 and available at: https://github.com/frattalab/bedops_parse_star_junctions .
- Full pipeline: alignment/mapping [STAR v2.7.0f, minimap2 v2.1] -> quantification [ImageJ, STAR v2.7.0f] -> stage not stated [BEDTools, CellProfiler, R, Snakemake v5.5.4]

