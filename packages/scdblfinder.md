# scDblFinder

- **Category:** single-cell
- **Papers in survey:** 179
- **Journals:** Nature (119), PNAS (33), Cell (18), Science (9)
- **Years:** 2021 (9), 2022 (27), 2023 (32), 2024 (35), 2025 (53), 2026 (23)
- **Versions named:** 2.0.3 (11), 0.2.1 (9), 0.2.3 (5), 2.0 (4), 1.4.0 (3), 2.0.4 (2), 0.2.2 (2), 1.12.0 (2), 1.18.0 (2), 1.2.0 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (17), quality control (9), normalisation (8), differential/statistical testing (4), visualisation (4), simulation/modelling (3), read trimming (1), variant calling (1), alignment/mapping (1)

## Papers

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: ...primers This Study STAR Methods Software and algorithms fgsea Korotkevich et al., 2019 https://bioconductor.org/packages/release/bioc/html/fgsea.html DoubletFinder McGinnis et al., 2019 https://github.com/chris-mcginnis-ucsf/DoubletFinder Seurat Stuart et al., 2019 https://satijalab.org/seurat/ DESeq2 Love et al., 2014 https://bioconductor.org/packages/release/bioc/html/DESeq2.html ChIP-seq Analys...
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### Discovery and functional interrogation of SARS-CoV-2 RNA-host protein interactions. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.012 | PMCID: PMC7951565 | PMID: 33743211
- Version used: **0.2.1**
- Evidence: The data processed using Scanpy version 1.6.0 and Scrublet version 0.2.1.
- Full pipeline: read trimming [HISAT2, fastp] -> alignment/mapping [HISAT2, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cytoscape v3.8.1, DESeq2 v1.28.1, R v3.6] -> visualisation [pheatmap] -> stage not stated [ImageJ, Scanpy v1.6.0, scDblFinder v0.2.1]

### COVID-19 immune features revealed by a large-scale single-cell transcriptome atlas. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.053 | PMCID: PMC7857060 | PMID: 33657410
- Evidence: ....io/en/latest/ CSOmap Ren et al., 2020 https://github.com/zhongguojie1998/CSOmap SCENIC 1.1.2-2 Aibar et al., 2017 https://github.com/aertslab/SCENIC Scrublet ( Wolock et al., 2019 ) https://github.com/AllonKleinLab/scrublet Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulfilled by the Lead Contact, Zemin Zhang ( z...
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [SCENIC v1.1.2, Scanpy v1.4.6, Seurat v2.3.0, kallisto, scDblFinder]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Version used: **2.0.3**
- Evidence: ...oads/latest Seurat v3.1.5 Stuart et al., 2019 https://satijalab.org/seurat SingleR v2.0.3 Aran et al., 2019 https://bioconductor.org/packages/SingleR DoubletFinder v2.0.3 McGinnis et al., 2019 https://github.com/chris-mcginnis-ucsf/DoubletFinder ggplot2 Wickham, 2016 https://ggplot2.tidyverse.org Plotly Sievert, 2020 https://plotly-r.com Analysis scripts This paper https://github.com/BosingerLab/R...
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Version used: **0.2.1**
- Evidence: 75 https://github.com/zktuong/dandelion Scrublet (version 0.2.1) Wolock et al.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### GPC3-Unc5 receptor complex structure and role in cell migration. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.025 | PMCID: PMC9596381 | PMID: 36240740
- Version used: **2.0.3**
- Evidence: Doublet cells were removed with the R package DoubletFinder (v2.0.3).
- Full pipeline: quality control [R] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [GROMACS, MDAnalysis] -> structure determination [Coot] -> stage not stated [CCP4, CellProfiler v2.2.0, ImageJ, Jupyter, PHENIX, REFMAC, Seurat, VMD, scDblFinder v2.0.3]

### Non-canonical odor coding in the mosquito. (Cell 2022)

- DOI: 10.1016/j.cell.2022.07.024 | PMCID: PMC9480278 | PMID: 35985288
- Evidence: (2018) https://github.com/MarioniLab/DropletUtils DoubletFinder McGinnis et al.
- Full pipeline: normalisation [ComplexHeatmap] -> stage not stated [ImageJ, R, Seurat, ggplot2, scDblFinder, tidyverse]

### Multiple early factors anticipate post-acute COVID-19 sequelae. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.014 | PMCID: PMC8786632 | PMID: 35216672
- Version used: **0.2.1**
- Evidence: ...n/robustbase CellRanger v3.1.0 10x Genomics https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/what-is-cell-ranger Scrublet v0.2.1 (Python package) Wolock et al., 2019 https://github.com/AllonKleinLab/scrublet Scanpy v1.6.0 (Python package) Wolf et al., 2018 https://github.com/theislab/scanpy UMAP v0.5.1 (Python package) McInnes et al., 2020 https://github.com/lm...
- Full pipeline: dimensionality reduction/clustering [Scanpy v1.6.0, UMAP v0.5.1, scDblFinder v0.2.1] -> differential/statistical testing [SciPy, XGBoost] -> stage not stated [BLAST v2.12.0, GSVA, Pilon, R, scikit-learn v0.24.2]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: Cell quality was assessed with a suite of metrics that included total UMI (GEX), number of genes detected, percent mitochondrial gene expression, percent ribosomal gene expression, percent IgG expression, Scrublet doublet score ( Wolock et al., 2019 ) and total UMI (ADT).
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Pyramidal neurons form active, transient, multilayered circuits perturbed by autism-associated mutations at the inception of neocortex. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.025 | PMCID: PMC10156177 | PMID: 37071993
- Version used: **0.2.1**
- Evidence: To identify multiplets (cell barcodes associated with multiple cells), we used Scrublet (v0.2.1) to simulate the creation of multiplets from our data and score our observed cells in comparison.
- Full pipeline: alignment/mapping [Python v3.7.7] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scDblFinder v0.2.1] -> stage not stated [Snakemake v5.19.3]

### Human IRF1 governs macrophagic IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.038 | PMCID: PMC9907019 | PMID: 36736301
- Evidence: We then used DoubletFinder package v2.0.3 to identify and filter out any remaining cell doublets 206 .
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq, STAR v2.7.3a] -> quantification [HTSeq] -> normalisation [edgeR v3.26.8] -> dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER v4.11, scDblFinder]

### Molecular and spatial signatures of mouse brain aging at single-cell resolution. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.010 | PMCID: PMC10024607 | PMID: 36580914
- Evidence: 62 https://github.com/ZhuangLab/MERlin Scrublet Wolock et al.
- Full pipeline: quantification [Harmony] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [statsmodels] -> stage not stated [AnnData, Cellpose, Python, Scanpy, scDblFinder, scikit-learn]

### mTOR activity paces human blastocyst stage developmental progression. (Cell 2024)

- DOI: 10.1016/j.cell.2024.08.048 | PMCID: PMC7617234 | PMID: 39332412
- Version used: **1.16.0**
- Evidence: The Cell Ranger filtered feature-barcode matrices were used, doublets detected by scDblFinder v1.16.0 were removed, and only cells meeting quality thresholds were retained; all preimplantation samples: more than 3000 detected genes and less than 7.5% of mitochondrial and less than 50% of ribosomal RNA reads, all postimplantation samples: more than 2000 detected genes and less than 15% of mitochond...
- Full pipeline: alignment/mapping [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [GSEA, R, UMAP, clusterProfiler, tidyverse] -> stage not stated [CellProfiler, Seurat, ggplot2, ggpubr, scDblFinder v1.16.0]

### Human inherited CCR2 deficiency underlies progressive polycystic lung disease. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.036 | PMCID: PMC10842692 | PMID: 38157855
- Evidence: Cells identified as doublets using DoubletFinder 107 (pN = 0.25, pK = 0.01) were also removed.
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, Seurat] -> quantification [ComplexHeatmap] -> normalisation [ComplexHeatmap, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [ImageJ, TrackMate] -> stage not stated [MACS2, ggplot2, scDblFinder]

### A single-nucleus transcriptomic atlas of the adult Aedes aegypti mosquito. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.008 | PMCID: PMC12767863 | PMID: 41172998
- Evidence: Scrublet expects an estimate of doublets as an input, for which we used the formula y = 0.000759 x + 0.052721 from the expected multiplet table provided by 10x Genomics, where x is the total number of cells in the dataframe.
- Full pipeline: quality control [Matplotlib, NumPy, Python, Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [seaborn] -> visualisation [UMAP, scikit-learn] -> stage not stated [AnnData, BLAST v2.9.0, ImageJ, Jupyter, scDblFinder]

### STAMP: Single-cell transcriptomics analysis and multimodal profiling through imaging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.05.027 | PMCID: PMC12551790 | PMID: 40532697
- Evidence: Doublet Identification Potential doublets were identified using the scDblFinder function from the scDblFinder package 53 (v1.16.0), incorporating cluster information via the clusters = colLabels(sce) argument, and subsequently removed by looking at the scDblFinder.score metrics together with canonical markers exclusive of specific populations.
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [UMAP, igraph, scDblFinder] -> machine learning [Cellpose] -> stage not stated [CellChat v2.1.2, DESeq2, ImageJ, QuPath v0.5.0, R, Seurat, Singularity, StarDist, ggplot2, ggpubr, napari]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Version used: **1.18.0**
- Evidence: Individual Seurat objects were then merged and annotated using hg38 before using scDblFinder (v1.18.0), using ‘aggregatefeatures=TRUE’ 119 to filter out cells inferred to be potential doublets.
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### Renal PIEZO2 is an essential regulator of renin. (Cell 2026)

- DOI: 10.1016/j.cell.2025.11.013 | PMCID: PMC12695021 | PMID: 41349545
- Evidence: 101 Cells with cleaned-up reads were then subjected to doublet removal using DoubletFinder.
- Full pipeline: quality control [SoupX v1.6.2] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [scDblFinder]

### An atlas of gene regulatory elements in adult mouse cerebrum. (Nature 2021)

- DOI: 10.1038/s41586-021-03604-1 | PMCID: PMC8494637 | PMID: 34616068
- Evidence: Doublet removal We used a modified version of Scrublet (RRID:SCR_018098) 66 to remove potential doublets for every dataset independently.
- Full pipeline: quality control [R] -> alignment/mapping [R] -> dimensionality reduction/clustering [BEDTools, HOMER, UMAP, scikit-learn] -> differential/statistical testing [HOMER, Monocle v0.2.2] -> stage not stated [Enrichr, MACS2, SAIGE, Seurat v3.0, scDblFinder]

### Spatially resolved cell atlas of the mouse primary motor cortex by MERFISH. (Nature 2021)

- DOI: 10.1038/s41586-021-03705-x | PMCID: PMC8494645 | PMID: 34616063
- Evidence: (7) We removed potential doublets using Scrublet 52 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Scanpy, scDblFinder]

### A transcriptomic and epigenomic cell atlas of the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03500-8 | PMCID: PMC8494649 | PMID: 34616066
- Evidence: Doublets were identified using a modified version of the DoubletFinder algorithm 51 and removed when the doublet score was greater than 0.3.
- Full pipeline: alignment/mapping [Bismark, STAR v2.5.3, Seurat] -> normalisation [deepTools] -> dimensionality reduction/clustering [R, Scanpy, UMAP] -> stage not stated [BEDTools, MACS2, scDblFinder]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Evidence: 2 , 3 , scRNA-seq data were preprocessed using a minimum of 500 genes and 5% mitochondrial cutoff and Scrublet 71 for doublet removal.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Version used: **0.2.1**
- Evidence: A Scrublet (v.0.2.1) score cut-off of 0.25 was applied to assist with doublet exclusion.
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Ovarian cancer mutational processes drive site-specific immune evasion. (Nature 2022)

- DOI: 10.1038/s41586-022-05496-1 | PMCID: PMC9771812 | PMID: 36517593
- Version used: **0.2.1**
- Evidence: Scrublet (version 0.2.1) was used to calculate and filter cells with a doublet score greater than 0.25.
- Full pipeline: quality control [R, Seurat] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [UMAP] -> machine learning [QuPath v0.2.3, StarDist] -> stage not stated [Strelka v2.8.2, scDblFinder v0.2.1]

### Primate gastrulation and early organogenesis at single-cell resolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05526-y | PMCID: PMC9771819 | PMID: 36517595
- Evidence: Next, doublet or multiplet cells were determined with Scrublet, according to the recommended multiplet rate reference table from 10X Genomics 54 .
- Full pipeline: quantification [CellPhoneDB, R, Seurat v4.0.0] -> dimensionality reduction/clustering [R, Seurat v4.0.0, UMAP, clusterProfiler, pheatmap, scVelo] -> simulation/modelling [Scanpy v1.8.2] -> visualisation [pheatmap] -> stage not stated [Docker, SCENIC, ilastik, scDblFinder]

### A transcriptional switch controls sex determination in Plasmodium falciparum. (Nature 2022)

- DOI: 10.1038/s41586-022-05509-z | PMCID: PMC9750867 | PMID: 36477538
- Version used: **1.6.0**
- Evidence: Doublets were identified and were filtered with scDblFinder (v.1.6.0) 47 .
- Full pipeline: alignment/mapping [minimap2 v2.17] -> quantification [HTSeq v0.12.4] -> visualisation [R] -> stage not stated [BEDTools v2.29.1, HISAT2 v2.0.0, SAMtools, Seurat v4.0.4, scDblFinder v1.6.0]

### Single-cell genomic variation induced by mutational processes in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05249-0 | PMCID: PMC9712114 | PMID: 36289342
- Evidence: Scrublet 74 (v.0.2.3) was used to calculate and filter cells predicted to be doublets.
- Full pipeline: alignment/mapping [BWA, DeepVariant, R, WhatsHap, minimap2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [Seurat, Strelka, scDblFinder]

### Maturation and circuit integration of transplanted human cortical organoids. (Nature 2022)

- DOI: 10.1038/s41586-022-05277-w | PMCID: PMC9556304 | PMID: 36224417
- Evidence: ...entile), outlier high-fraction mitochondrial genes (median above the 95th percentile), and/or high proportions of putative doublets identified by the DoubletFinder package 33 (median DoubletFinder score above the 95th percentile). t-hCO samples ( n = 3) and hCO samples ( n = 3) were each separately integrated using the IntegrateData function with the above parameters.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Fiji v2.1.0, ImageJ, R v4.1.2, Seurat v4.1.1, edgeR v3.36.0, scDblFinder]

### Brainstem ADCYAP1<sup>+</sup> neurons control multiple aspects of sickness behaviour. (Nature 2022)

- DOI: 10.1038/s41586-022-05161-7 | PMCID: PMC9492535 | PMID: 36071158
- Evidence: The ambient RNA contamination and doublets were estimated by using DropletUtils ( https://bioconductor.org/packages/release/bioc/html/DropletUtils.html ) and scDblFinder ( https://bioconductor.org/packages/release/bioc/html/scDblFinder.html ), respectively.
- Full pipeline: quality control [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor v1.0.6, Seurat v4.0]

### Embryo model completes gastrulation to neurulation and organogenesis. (Nature 2022)

- DOI: 10.1038/s41586-022-05246-3 | PMCID: PMC9534772 | PMID: 36007540
- Evidence: Cells were filtered based on the number of genes detected (between 700 and 4,000), unique molecular identifiers (UMIs) detected (lower than 7,500), percentage of UMI counts mapping to mitochondrial genes (between 1 and 15%) and doublet scores computed using Scrublet 67 v0.1 (lower than 0.3), which yielded a total of 26,748 cells overall.
- Full pipeline: quality control [FastQC] -> read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, scDblFinder] -> normalisation [scikit-image] -> dimensionality reduction/clustering [Python, UMAP, ggplot2] -> machine learning [ilastik] -> stage not stated [ImageJ, Jupyter, Monocle, Scanpy, Seurat, scVelo, tidyverse]

### Spatial multi-omic map of human myocardial infarction. (Nature 2022)

- DOI: 10.1038/s41586-022-05060-x | PMCID: PMC9364862 | PMID: 35948637
- Version used: **1.4.0**
- Evidence: We discarded nuclei (1) in the top 1% in terms of the number of genes, (2) with less than 300 genes and less than 500 UMIs, (3) with more than 5% of mitochondrial gene expression, and (4) doublets as estimated using scDblFinder (v1.4.0) 60 with default parameters.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.32.1] -> visualisation [UMAP] -> stage not stated [ArchR v1.0.1, CellPhoneDB, ImageJ, MACS2, R v1.16, scDblFinder v1.4.0]

### DOCK2 is involved in the host genetics and biology of severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05163-5 | PMCID: PMC9492544 | PMID: 35940203
- Version used: **0.2.1**
- Evidence: Additionally, putative doublets were removed using Scrublet (v0.2.1) for each sample 47 . scRNA-seq computational pipelines and basic analysis The R package Seurat (v3.2.2) was used for data scaling, transformation, clustering, dimensionality reduction, differential expression analysis and most visualization 48 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR v2.7.9a] -> quantification [RSEM v1.3.3] -> normalisation [RSEM v1.3.3, Seurat v3.2.2, scDblFinder v0.2.1] -> dimensionality reduction/clustering [Seurat v3.2.2, UMAP, scDblFinder v0.2.1] -> differential/statistical testing [Bioconductor, PLINK, R, Seurat v3.2.2, TwoSampleMR, edgeR v3.32.0, scDblFinder v0.2.1] -> visualisation [Seurat v3.2.2, scDblFinder v0.2.1] -> stage not stated [ImageJ, WGCNA, ggplot2]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Evidence: Downstream scRNA-seq analysis Doublet detection We used Scrublet for cell doublet calling on a per-library basis.
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: DoubletFinder 87 was then used to remove predicted doublets from each sample (nExp = 9% of nuclei per sample).
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### The development and evolution of inhibitory neurons in primate cerebrum. (Nature 2022)

- DOI: 10.1038/s41586-022-04510-w | PMCID: PMC8967711 | PMID: 35322231
- Version used: **0.2.2**
- Evidence: Doublets were then detected and removed from the dataset using Scrublet (release 0.2.2; using threshold parameter 0.5).
- Full pipeline: quantification [kallisto v0.46] -> dimensionality reduction/clustering [AnnData, Scanpy, Seurat, UMAP] -> differential/statistical testing [SciPy, statsmodels v0.12.2] -> simulation/modelling [SciPy, scVelo] -> stage not stated [ImageJ, Python, scDblFinder v0.2.2]

### Single-cell delineation of lineage and genetic identity in the mouse brain. (Nature 2022)

- DOI: 10.1038/s41586-021-04237-0 | PMCID: PMC8770128 | PMID: 34912118
- Version used: **2.0.3**
- Evidence: In addition, embryonic datasets were filtered with DoubletFinder version 2.0.3 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [R v3.6.0, Seurat, scDblFinder v2.0.3, velocyto]

### A high-resolution transcriptomic and spatial atlas of cell types in the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06812-z | PMCID: PMC10719114 | PMID: 38092916
- Evidence: Doublets were identified using a modified version of the DoubletFinder algorithm 132 (available in scrattch.hicat, https://github.com/AllenInstitute/scrattch.hicat , v1.0.9) and removed when doublet score >0.3.
- Full pipeline: quantification [UMAP] -> normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> stage not stated [Cellpose, Jupyter, WGCNA, limma, scDblFinder]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Evidence: Putative multiplets were predicted using DoubletFinder 72 and 10% of cells were removed from each sample that had the highest doublet score.
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Molecularly defined and spatially resolved cell atlas of the whole mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06808-9 | PMCID: PMC10719103 | PMID: 38092912
- Evidence: (5) We removed potential doublets using Scrublet 68 as previously described.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> machine learning [Cellpose v2.0] -> stage not stated [CellChat, scDblFinder, scikit-learn]

### Single-cell analysis of chromatin accessibility in the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06824-9 | PMCID: PMC10719105 | PMID: 38092917
- Evidence: We next removed potential doublets in each dataset based on a modified Scrublet 28 procedure using SnapATAC2 29 .
- Full pipeline: dimensionality reduction/clustering [BEDTools, UMAP, clusterProfiler, scikit-learn] -> stage not stated [HOMER, MACS2, Monocle, R, RepeatMasker, Seurat, deepTools, scDblFinder]

### Single-cell, whole-embryo phenotyping of mammalian developmental disorders. (Nature 2023)

- DOI: 10.1038/s41586-023-06548-w | PMCID: PMC10665194 | PMID: 37968388
- Evidence: Subclusters with a detected doublet ratio (by Scrublet) above 15% were annotated as doublet-derived subclusters.
- Full pipeline: read trimming [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [AnnData v0.7.5.2, Monocle, Scanpy, Seurat, UMAP, scDblFinder, scVelo v0.2.4] -> stage not stated [ggplot2 v3.3.5]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: ...and apoptosis with too high proportion of mitochondrial gene expression over the total transcript counts (>10%) and cells predicted to be doublets by Scrublet, as described below.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Evidence: Potential doublets were removed using Scrublet 68 except for patch-seq cells that correspond already to singlets.
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### Complete human day 14 post-implantation embryo models from naive ES cells. (Nature 2023)

- DOI: 10.1038/s41586-023-06604-5 | PMCID: PMC10584686 | PMID: 37673118
- Version used: **1.6**
- Evidence: Doublet cells were also assessed by RNA data using scDblFinder (v.1.6).
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Signac v1.6.0] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [SciPy v1.8.0, seaborn v0.11.0] -> visualisation [SciPy v1.8.0, seaborn v0.11.0] -> stage not stated [R, pheatmap, scDblFinder v1.6]

### Endothelial sensing of AHR ligands regulates intestinal homeostasis. (Nature 2023)

- DOI: 10.1038/s41586-023-06508-4 | PMCID: PMC10533400 | PMID: 37586410
- Evidence: Cells subsequently identified as doublets by DoubletFinder 58 with parameters pN = 0.25, pk = 0.16 for Veh_15k, 0.22 for Ficz_15k and Ficz_60k were removed and the remaining cells were processed with Seurat SCTransform again and samples from Ficz and Veh were integrated using PrepSCTIntegration(), FindIntegrationAnchors() and IntegrateData() functions and the linear dimensional reduction with Seur...
- Full pipeline: alignment/mapping [STAR v2.2.7a, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2, UMAP, scDblFinder] -> differential/statistical testing [GSEA] -> visualisation [DESeq2, R, ggplot2 v3.3.3] -> stage not stated [Bioconductor, ComplexHeatmap v2.2.0, SCENIC v1.2.4, Seurat v3.2.0]

### Mitochondrial integrated stress response controls lung epithelial cell fate. (Nature 2023)

- DOI: 10.1038/s41586-023-06423-8 | PMCID: PMC10447247 | PMID: 37558881
- Version used: **0.2.1**
- Evidence: Doublets were removed using Scrublet v.0.2.1 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [STAR] -> variant calling [pheatmap] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy v1.8.1, UMAP] -> differential/statistical testing [edgeR] -> visualisation [ggplot2, pheatmap] -> stage not stated [DESeq2, Python v3.8.3, Seurat v4.0.6, scDblFinder v0.2.1, scVelo v0.2.4, velocyto v0.17]

### Netrin-1 blockade inhibits tumour growth and EMT features in endometrial cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06367-z | PMCID: PMC10412451 | PMID: 37532934
- Version used: **2.0.3**
- Evidence: Doublets were detected with DoubletFinder (v.2.0.3) and filtered out, together with cells showing a low number of features (nFeature_RNA < 500) or a high percentage of mitochondrial genes (above 25%).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [ggplot2 v3.3.6] -> stage not stated [Bioconductor, CellChat v1.6.0, DESeq2, R v4.0.3, STAR v2.7.10a, Seurat, scDblFinder v2.0.3]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Evidence: Doublets identified by both DoubletDetection (v.3.0) and Scrublet ( https://github.com/swolock/scrublet ; v.0.2.2) were removed.
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### Organization of the human intestine at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-05915-x | PMCID: PMC10356619 | PMID: 37468586
- Evidence: DoubletFinder 85 was run for each non-multiome snRNA sample using principal components 1–20. nExp was set to 0.076 × nCells 2 /10,000, pN to 0.25 and pK was determined using paramSweep_v3, and cells that were classified as doublets were removed before downstream analysis. snRNA data for both multiome and non-multiome cells was corrected for possible ambient RNA correction using DecontX 86 .
- Full pipeline: quality control [ArchR, Seurat, UMAP] -> dimensionality reduction/clustering [ArchR, Scanpy, Seurat, Squidpy, UMAP, limma, scDblFinder] -> differential/statistical testing [limma] -> visualisation [ImageJ, limma] -> stage not stated [MACS2, R]

### Spatially resolved multiomics of human cardiac niches. (Nature 2023)

- DOI: 10.1038/s41586-023-06311-1 | PMCID: PMC10371870 | PMID: 37438528
- Evidence: A Scrublet 57 (v.0.2.3) score cutoff value of 0.3 of was applied to remove doublets.
- Full pipeline: quality control [Matplotlib v3.5.2, NumPy v1.21.5, Scanpy v1.8.2, pandas v1.3.5] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> stage not stated [ArchR v1.0.2, CellPhoneDB, NetworkX v2.6.3, PHENIX, R, SCENIC v0.11.2, scDblFinder]

### Pluripotent stem cell-derived model of the post-implantation human embryo. (Nature 2023)

- DOI: 10.1038/s41586-023-06368-y | PMCID: PMC10584688 | PMID: 37369347
- Evidence: Cells with >500 RNA unique molecular identifier (UMI) counts, <20% mitochondrial reads, >500 ATAC reads, trasncription start site enrichment >1 and were called as singlets using scDblFinder 52 were retained for downstream analysis.
- Full pipeline: registration [kallisto] -> dimensionality reduction/clustering [UMAP] -> visualisation [Cytoscape] -> stage not stated [CellPhoneDB v2.0, SCENIC, Seurat, Signac, scDblFinder]

### Injury prevents Ras mutant cell expansion in mosaic skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06198-y | PMCID: PMC10322723 | PMID: 37344586
- Evidence: Next, the DoubletFinder 63 package ( https://github.com/chris-mcginnis-ucsf/DoubletFinder ) was used to get rid of barcodes that may represent possible doublets.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, Scanpy v1.6, Seurat, SoupX, scDblFinder, scikit-learn v0.24.2]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Evidence: Downstream scRNA-seq and snRNA-seq analysis Detection of doublets by gene expression We used Scrublet for cell doublet calling on a per-library basis.
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: To remove potential doublets from the datasets in a more stringent manner, we used the DoubletFinder package in R, which assesses which barcodes in a dataset are most likely to be doublets based on transcriptional similarity to distinct clusters 68 .
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Tissue CD14&lt;sup&gt;+&lt;/sup&gt;CD8&lt;sup&gt;+&lt;/sup&gt; T cells reprogrammed by myeloid cells and modulated by LPS. (Nature 2023)

- DOI: 10.1038/s41586-022-05645-6 | PMCID: PMC7619353 | PMID: 36697826
- Evidence: The simulated doublet histogram generated using Scrublet was unimodal, likely due to cellular homogeneity 59 .
- Full pipeline: quality control [STAR, Seurat] -> alignment/mapping [STAR] -> quantification [HTSeq v0.10.0, ImageJ, STAR] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [seaborn] -> simulation/modelling [scDblFinder] -> visualisation [seaborn] -> stage not stated [Python v3.6]

### The molecular evolution of spermatogenesis across mammals. (Nature 2023)

- DOI: 10.1038/s41586-022-05547-7 | PMCID: PMC9834047 | PMID: 36544022
- Evidence: Then, we removed potential doublets using doubletFinder_v3 function of DoubletFinder 63 v.2.0.1 (parameters PCs = 1:20, pN = 0.25, nExp = 5% of the total number of cells, identifying pk using paramSweep_v3, summarizeSweep and find.pK functions).
- Full pipeline: read trimming [Cutadapt v1.8.3] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat, UMAP] -> differential/statistical testing [CellPhoneDB] -> simulation/modelling [limma] -> stage not stated [StringTie v1.3.3, ape (R) v5.3, ggplot2 v3.2.1, pheatmap v1.0.12, scDblFinder, tidyverse v1.3.0]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **2.0**
- Evidence: Quality control, filtering, data clustering, visualization and differential expression analysis were performed using the Seurat (v.4.0.3) and DoubletFinder (v.2.0) R packages 85 , 86 .
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Version used: **0.2.3**
- Evidence: For RNA data, Scrublet (v0.2.3) 78 was applied to estimate doublet probability, and a score of more than 0.3 was used as a cut-off value.
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Evidence: Doublets were annotated using Scrublet 43 v.0.2.3.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Adipose tissue retains an epigenetic memory of obesity after weight loss. (Nature 2024)

- DOI: 10.1038/s41586-024-08165-7 | PMCID: PMC11634781 | PMID: 39558077
- Evidence: 76 ) was used to process, integrate and analyse datasets. scDblFinder 77 was used to identify and remove doublets.
- Full pipeline: quality control [FastQC v0.11.9, SoupX] -> read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [HISAT2 v2.2.1] -> quantification [Fiji, ImageJ, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [UMAP] -> stage not stated [DESeq2, GSEA, R, Seurat v4.1.0, scDblFinder]

### A prenatal skin atlas reveals immune regulation of human skin morphogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08002-x | PMCID: PMC11578897 | PMID: 39415002
- Version used: **0.2.1**
- Evidence: Potential doublets were flagged using Scrublet (v.0.2.1) 86 as previously described 87 .
- Full pipeline: quantification [NumPy v1.23.4, QuPath] -> normalisation [Harmony v0.0.5] -> dimensionality reduction/clustering [Harmony v0.0.5, NumPy v1.23.4, SciPy v1.9.3, UMAP] -> differential/statistical testing [scikit-learn] -> visualisation [NumPy v1.23.4, SciPy v1.9.3, UMAP, ggplot2 v3.3.6] -> stage not stated [CellPhoneDB v3.0.0, Enrichr, ImageJ, PHENIX, STRING db, Scanpy v1.4.3, scDblFinder v0.2.1, scVelo]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Evidence: We further applied Scrublet 55 to remove potential doublets.
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Temporal BMP4 effects on mouse embryonic and extraembryonic development. (Nature 2024)

- DOI: 10.1038/s41586-024-07937-5 | PMCID: PMC11485214 | PMID: 39294373
- Evidence: For doublet removal, we ran DoubletFinder separately on the two batches, following the best practice workflow of the package.
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [ImageJ, scDblFinder]

### Human organoids with an autologous tissue-resident immune compartment. (Nature 2024)

- DOI: 10.1038/s41586-024-07791-5 | PMCID: PMC11374719 | PMID: 39143209
- Evidence: Doublet removal with DoubletFinder For each scRNA-seq experiment, DoubletFinder 65 (v.2.3.0) was used to predict doublets in the sequencing data.
- Full pipeline: quality control [R] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [CellChat, CellProfiler v4.2.5, ImageJ v1.54i, Python v3.7, scDblFinder, scVelo]

### Single-cell multiregion dissection of Alzheimer's disease. (Nature 2024)

- DOI: 10.1038/s41586-024-07606-7 | PMCID: PMC11338834 | PMID: 39048816
- Evidence: We separately called doublets using DoubletFinder and flagged and removed clusters with strong doublet profiles and clusters showing strong individual-specific batch effects, leaving a final dataset of 1.35 million cells 88 .
- Full pipeline: alignment/mapping [Seurat] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Seurat, UMAP, edgeR, scDblFinder] -> differential/statistical testing [DESeq2, R, edgeR, emmeans, lme4] -> visualisation [DESeq2, Seurat] -> stage not stated [CellPhoneDB, MAGMA, SCENIC, ggplot2]

### In vivo single-cell CRISPR uncovers distinct TNF programmes in tumour evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07663-y | PMCID: PMC11306103 | PMID: 39020166
- Evidence: Downstream processing of the scRNA-seq data To remove the doublets, the Scrublet 71 Python package was utilized.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [CellChat, ComplexHeatmap, Enrichr, GSEA, Python, R, Seurat, WGCNA, ggplot2, pandas, scDblFinder, seaborn, survival (R), tidyverse]

### Brainstem Dbh&lt;sup&gt;+&lt;/sup&gt; neurons control allergen-induced airway hyperreactivity. (Nature 2024)

- DOI: 10.1038/s41586-024-07608-5 | PMCID: PMC11254774 | PMID: 38987587
- Version used: **2.0**
- Evidence: In addition, DoubletFinder (v2.0) 41 was used to remove doublets and SCTransform was used to normalize feature expression.
- Full pipeline: quality control [R, Seurat v4.0, UMAP] -> normalisation [R, Seurat v4.0, UMAP, scDblFinder v2.0] -> dimensionality reduction/clustering [R, Seurat v4.0, UMAP, ggplot2 v3.3.2, tidyverse] -> differential/statistical testing [R, Seurat v4.0, UMAP] -> visualisation [ggplot2 v3.3.2, tidyverse]

### A maternal brain hormone that builds bone. (Nature 2024)

- DOI: 10.1038/s41586-024-07634-3 | PMCID: PMC11306098 | PMID: 38987585
- Evidence: Scrublet was then used to detect and remove residual duplicates.
- Full pipeline: read trimming [RSEM v1.2.21, STAR v2.4] -> alignment/mapping [RSEM v1.2.21, STAR v2.4, kallisto] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Scanpy v1.9, scDblFinder]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Evidence: Doublet cells were removed using the Scrublet Python package (v.0.2.3) according to previously published instructions 73 .
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Multimodal decoding of human liver regeneration. (Nature 2024)

- DOI: 10.1038/s41586-024-07376-2 | PMCID: PMC11153152 | PMID: 38693268
- Evidence: We used the Scrublet 46 Python module v0.2.3 to identify potential doublets and the SoupX 47 R package v1.5.2 to automatically calculate and correct for background contamination.
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [CellChat, Cellpose, ImageJ, QuPath v0.3.0, R, Scanpy, StarDist]

### Multimodal cell atlas of the ageing human skeletal muscle. (Nature 2024)

- DOI: 10.1038/s41586-024-07348-6 | PMCID: PMC11062927 | PMID: 38649488
- Version used: **2.0.3**
- Evidence: Doublets were identified and filtered by DoubletFinder (v.2.0.3) 61 .
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Python v3.7, Scanpy v1.8.1, Seurat v4.0.2, UMAP] -> simulation/modelling [Monocle] -> visualisation [pheatmap v1.0.12] -> stage not stated [ArchR, CellChat v1.1.0, FUMA, Fiji v2.14.0, ImageJ v2.14.0, LDSC, Metascape, SoupX v1.4.8, scDblFinder v2.0.3]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Version used: **2.0.3**
- Evidence: Doublets were identified using DoubletFinder v.2.0.3 and removed.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Evidence: Empty droplets were detected and removed from the raw feature barcode matrix using the emptyDrops function from the DropletUtils (version 1.16.0) package and doublets were detected and removed using DoubletFinder (verison 2.0.3).
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### Immune microniches shape intestinal T&lt;sub&gt;reg&lt;/sub&gt; function. (Nature 2024)

- DOI: 10.1038/s41586-024-07251-0 | PMCID: PMC11041794 | PMID: 38570678
- Evidence: Doublet detection was performed using the Scrublet algorithm ( https://github.com/AllonKleinLab/scrublet 49 ) with percolation step, as previously described 50 .
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy] -> visualisation [R] -> stage not stated [CellPhoneDB, NumPy v1.20.1, SoupX, pandas v1.2.3, scDblFinder, scVelo v0.2.4, velocyto]

### Formation of memory assemblies through the DNA-sensing TLR9 pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07220-7 | PMCID: PMC10990941 | PMID: 38538785
- Version used: **1.13.13**
- Evidence: Doublets were detected and removed using R package scDblFinder v1.13.13.
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> alignment/mapping [SAMtools, STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, fgsea v1.20.0] -> stage not stated [Fiji, R, SoupX v1.6.2, scDblFinder v1.13.13]

### APOE4/4 is linked to damaging lipid droplets in Alzheimer's disease microglia. (Nature 2024)

- DOI: 10.1038/s41586-024-07185-7 | PMCID: PMC10990924 | PMID: 38480892
- Version used: **0.2.3**
- Evidence: Count data were first screened for doublets with the Scrublet (v.0.2.3) Python package 43 .
- Full pipeline: alignment/mapping [HOMER, STAR v2.5.1b] -> quantification [Fiji, ImageJ] -> normalisation [R v4.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, ImageJ, R v4.3, Seurat] -> stage not stated [Bowtie2, MACS2, Python v3.9.12, Scanpy, scDblFinder v0.2.3]

### Spatially organized cellular communities form the developing human heart. (Nature 2024)

- DOI: 10.1038/s41586-024-07171-z | PMCID: PMC10972757 | PMID: 38480880
- Version used: **2.0**
- Evidence: Potential doublets were removed using DoubletFinder (v.2.0) 63 ( https://github.com/chris-mcginnis-ucsf/DoubletFinder ) using an anticipated doublet rate of 5%, which is the expected rate reported by 10x Genomics for the number of cells loaded onto the 10x Controller.
- Full pipeline: dimensionality reduction/clustering [R, Scanpy v1.8, Seurat v4.0.1, UMAP, scikit-learn v0.22] -> visualisation [Cytoscape v3.8.0, UMAP] -> stage not stated [Bioconductor, CellChat v1.6.1, Cellpose v1.0.2, OpenCV, QuPath v0.4.3, SCENIC v0.12.1, scDblFinder v2.0]

### An atlas of epithelial cell states and plasticity in lung adenocarcinoma. (Nature 2024)

- DOI: 10.1038/s41586-024-07113-9 | PMCID: PMC10954546 | PMID: 38418883
- Evidence: Doublets or multiplets were also identified using the doublet detection algorithm DoubletFinder 43 .
- Full pipeline: normalisation [R] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [R] -> simulation/modelling [Monocle] -> visualisation [Scanpy v1.9.1, UMAP] -> stage not stated [ImageJ, Mutect2, SAMtools v1.15, Seurat, Slingshot, ggplot2 v3.2.0, pheatmap v1.0.12, scDblFinder]

### Crym-positive striatal astrocytes gate perseverative behaviour. (Nature 2024)

- DOI: 10.1038/s41586-024-07138-0 | PMCID: PMC10937394 | PMID: 38418885
- Evidence: Scrublet was embedded in the Seurat pipeline to remove doublets.
- Full pipeline: alignment/mapping [HTSeq, STAR] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, limma] -> visualisation [Cytoscape v3.8, R v4.0.3, Seurat] -> stage not stated [Enrichr, ImageJ, STRING db, WGCNA, scDblFinder]

### Multisensory gamma stimulation promotes glymphatic clearance of amyloid. (Nature 2024)

- DOI: 10.1038/s41586-024-07132-6 | PMCID: PMC10917684 | PMID: 38418876
- Evidence: We used DoubletFinder to remove the potential doublets from snRNA-seq data.
- Full pipeline: alignment/mapping [Suite2p] -> quantification [ImageJ] -> normalisation [ImageJ] -> registration [Suite2p] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> visualisation [UMAP] -> stage not stated [Seurat v4.0.3, scDblFinder]

### A model of human neural networks reveals NPTX2 pathology in ALS and FTLD. (Nature 2024)

- DOI: 10.1038/s41586-024-07042-7 | PMCID: PMC10901740 | PMID: 38355792
- Evidence: Cell doublets were removed with scDblFinder 72 and outlier cells were detected and filtered with the scater R package 73 .
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [STAR v2.7.7a] -> quantification [ilastik] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.36.0] -> machine learning [ilastik] -> stage not stated [ImageJ, Python v3.6.10, R, SpikeInterface, scDblFinder, tidyverse]

### A single-cell time-lapse of mouse prenatal development from gastrula to birth. (Nature 2024)

- DOI: 10.1038/s41586-024-07069-w | PMCID: PMC10901739 | PMID: 38355799
- Evidence: First, we used Scrublet to detect doublets directly.
- Full pipeline: read trimming [STAR v2.6.1d, Trim Galore] -> alignment/mapping [STAR v2.6.1d] -> dimensionality reduction/clustering [Monocle, Scanpy v1.6.0, UMAP] -> differential/statistical testing [Seurat] -> visualisation [ggplot2] -> stage not stated [Cytoscape v3.9.1, Python, scDblFinder]

### A human embryonic limb cell atlas resolved in space and time. (Nature 2024)

- DOI: 10.1038/s41586-023-06806-x | PMCID: PMC7616500 | PMID: 38057666
- Evidence: In the first step of the process, each 10x lane was processed independently using the Scrublet to obtain per-cell doublet scores.
- Full pipeline: alignment/mapping [STAR v2.5.1b] -> quantification [STAR v2.5.1b, scVelo v0.24] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [Scanpy] -> structure determination [AnnData] -> machine learning [ilastik] -> stage not stated [CellPhoneDB, PHENIX, SCENIC, scDblFinder]

### Continuous cell-type diversification in mouse visual cortex development. (Nature 2025)

- DOI: 10.1038/s41586-025-09644-1 | PMCID: PMC12589121 | PMID: 41193844
- Evidence: Doublets were identified using a modified version of the DoubletFinder algorithm (available in scrattch.hicat; https://github.com/AllenInstitute/scrattch.hicat , v.1.0.9) and removed when the doublet score was >0.3.
- Full pipeline: dimensionality reduction/clustering [R, Seurat, UMAP, clusterProfiler v4.0] -> simulation/modelling [Monocle, Slingshot] -> structure determination [Monocle, Slingshot] -> machine learning [Python, scikit-learn] -> stage not stated [ArchR, Cellpose v2.0, SCENIC, XGBoost, limma, scDblFinder]

### Conservation and alteration of mammalian striatal interneurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09592-w | PMCID: PMC12589139 | PMID: 41193841
- Version used: **0.2.3**
- Evidence: Doublets were removed using Scrublet (v.0.2.3) 39 .
- Full pipeline: normalisation [Harmony] -> dimensionality reduction/clustering [Scanpy, SciPy v1.11.2, Seurat, UMAP, igraph] -> simulation/modelling [AnnData, R, Slingshot] -> stage not stated [BLAST v2.9.0, scDblFinder v0.2.3]

### Transcriptomic and spatial organization of telencephalic GABAergic neurons. (Nature 2025)

- DOI: 10.1038/s41586-025-09296-1 | PMCID: PMC12589142 | PMID: 41193843
- Evidence: Doublets were identified using a modified version of the DoubletFinder algorithm, which is available in scrattch.hicat (v.0.1.0, RRID: SCR_01809) 102 .
- Full pipeline: quantification [R, UMAP] -> dimensionality reduction/clustering [R, Seurat v5.1.0, UMAP] -> stage not stated [scDblFinder]

### Multi-omic profiling reveals age-related immune dynamics in healthy adults. (Nature 2025)

- DOI: 10.1038/s41586-025-09686-5 | PMCID: PMC12711581 | PMID: 41162704
- Evidence: Doublets were detected and removed using Scrublet, and minimal inter-batch effects were adjusted in the PCA space for visualization purposes using Harmony.
- Full pipeline: quality control [UMAP] -> normalisation [UMAP, scDblFinder] -> dimensionality reduction/clustering [MACS2, UMAP, scDblFinder] -> differential/statistical testing [DESeq2 v1.42.0, GSEA, R v4.3.2, fgsea] -> simulation/modelling [Slingshot] -> visualisation [scDblFinder] -> stage not stated [ArchR v1.0.2, Scanpy, Seurat v5.0.1, lme4]

### Mapping Plasmodium transitions and interactions in the Anopheles female. (Nature 2025)

- DOI: 10.1038/s41586-025-09653-0 | PMCID: PMC12695668 | PMID: 41125888
- Evidence: The count matrix from each sample was merged into a single AnnData object by Scanpy, and doublets were removed running Scrublet software in Python before conversion to Seurat using SeuratDisk’s function Convert 57 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AnnData, DESeq2, Monocle, Python v3.10, R v4.3, Scanpy v1.9.1, Seurat, scDblFinder]

### Neuronal activity-dependent mechanisms of small cell lung cancer pathogenesis. (Nature 2025)

- DOI: 10.1038/s41586-025-09492-z | PMCID: PMC12571889 | PMID: 40931074
- Evidence: Subsequently, the scCB2 63 (v.1.12.0) package was utilized to filter out empty droplets, employing an FDR threshold of 0.01 to identify real cells, while potential doublets were removed using the scDblFinder 64 (v.1.16.0) package.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scDblFinder] -> stage not stated [Fiji v2.1.0, GSEA, GSVA, ImageJ v2.1.0, Seurat, fgsea]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Evidence: Doublets were filtered out using Scrublet 68 .
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Microglia-neuron crosstalk through Hex-GM2-MGL2 maintains brain homeostasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09477-y | PMCID: PMC12545202 | PMID: 40769205
- Evidence: Doublets were excluded using the scDblFinder package v.1.16.0 (ref.
- Full pipeline: quality control [FastQC v0.73, Trim Galore] -> read trimming [FastQC v0.73, Trim Galore] -> alignment/mapping [STAR] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.0] -> differential/statistical testing [limma] -> visualisation [ggplot2] -> stage not stated [ImageJ v1.54g, R, Seurat v5.0.3, pheatmap v1.0.12, scDblFinder]

### Lithium deficiency and the onset of Alzheimer's disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09335-x | PMCID: PMC12443616 | PMID: 40770094
- Evidence: Potential doublets were removed using DoubletFinder (v.3) 74 following the default parameters.
- Full pipeline: quality control [FastQC v0.11.9, STAR] -> alignment/mapping [FastQC v0.11.9, HTSeq, STAR] -> quantification [HTSeq] -> normalisation [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, Metascape] -> stage not stated [Bioconductor, Fiji v2.9.0, ImageJ v2.9.0, MAGMA, R, Seurat, scDblFinder]

### Microglia regulate GABAergic neurogenesis in prenatal human brain through IGF1. (Nature 2025)

- DOI: 10.1038/s41586-025-09362-8 | PMCID: PMC12527950 | PMID: 40770097
- Version used: **2.0.3**
- Evidence: Gene counts then underwent a doublet removal step using DoubletFinder v.2.0.3 ( https://www.cell.com/cell-systems/fulltext/S2405-4712(19)30073-0 ).
- Full pipeline: quantification [ImageJ v1.54] -> normalisation [UMAP] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [ImageJ v1.54] -> simulation/modelling [Monocle] -> visualisation [Monocle] -> stage not stated [CellChat, Enrichr, Scanpy v1.10.3, Seurat v5.1.0, scDblFinder v2.0.3]

### Mouse lemur cell atlas informs primate genes, physiology and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09114-8 | PMCID: PMC12328237 | PMID: 40739355
- Evidence: These discrepancies may be caused by doublets of B cells and plasma cells (although applying the program Scrublet 71 with default parameters identified only 3 out of the 80 cells with 2 different BLAST or IgBLAST hits as possible doublets) or more probably, reflect dual expression as more recently appreciated 72 .
- Full pipeline: alignment/mapping [MAFFT, RSEM v1.3.1, SAMtools v1.16.1, STAR] -> dimensionality reduction/clustering [R, Seurat, Slingshot v2.14.0, UMAP] -> simulation/modelling [Slingshot v2.14.0] -> visualisation [AnnData v0.7.4, NumPy v1.19.3, pandas v1.1.5] -> stage not stated [BLAST, Bowtie2, CellPhoneDB, Matplotlib v3.3.2, Scanpy, SnpEff, ggplot2 v3.4.4, igraph v0.7.1, pheatmap v1.0.12, scDblFinder, seaborn v0.9.0, tidyverse v1.1.2]

### Respiratory viral infections awaken metastatic breast cancer cells in lungs. (Nature 2025)

- DOI: 10.1038/s41586-025-09332-0 | PMCID: PMC12422975 | PMID: 40739350
- Evidence: The R package scDblFinder 58 was used to identify and subsequently remove doublets from the data.
- Full pipeline: read trimming [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> alignment/mapping [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> quantification [Cutadapt, STAR v2.7.9a, Salmon v1.10.1] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [GSEA, clusterProfiler, limma] -> stage not stated [ImageJ, QuPath, R, Seurat, ggplot2, ggpubr, pheatmap, scDblFinder]

### Selective remodelling of the adipose niche in obesity and weight loss. (Nature 2025)

- DOI: 10.1038/s41586-025-09233-2 | PMCID: PMC12367556 | PMID: 40634602
- Evidence: Potential doublet nuclei were detected using three approaches: expression-based DoubletFinder 56 , using doublet estimates from genotyping to set the expectation; genotype-based, Vireo 57 (details below); and iterative clustering and detection of clusters with high expression or genotype-based doublet fractions.
- Full pipeline: variant calling [IMPUTE2 v2.3.2, SHAPEIT, scDblFinder] -> normalisation [AnnData] -> dimensionality reduction/clustering [AnnData, Scanpy, UMAP, scDblFinder] -> stage not stated [CellChat, ImageJ, QuPath v0.5.1, SCENIC, SciPy, Seurat]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Evidence: For doublet detection, doublets were identified using a combination of two computational methods — Scrublet 60 (v0.2.3) and DoubletDetection 61 (v4.2) — and removed from each sample.
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Developmental trajectory and evolutionary origin of thymic mimetic cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09148-y | PMCID: PMC12286861 | PMID: 40500437
- Evidence: Doublets were removed with scDblFinder 63 .
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Galaxy, HISAT2 v2.1.0, MACS2, Trim Galore, featureCounts v1.6.1.0, scDblFinder]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: Since the samples were not hashed, potential doublet cells were identified using Scrublet applied to the filtered feature barcode matrices from Cell Ranger.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### Mouse liver assembloids model periportal architecture and biliary fibrosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09183-9 | PMCID: PMC12350178 | PMID: 40441268
- Evidence: We further eliminated doublets using Scrublet 77 ( https://github.com/swolock/scrublet ).
- Full pipeline: alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.36.0] -> machine learning [StarDist] -> stage not stated [GSEA, ImageJ, R, Scanpy v1.9.2, fgsea v1.22.0, scDblFinder]

### Cross-tissue multicellular coordination and its rewiring in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09053-4 | PMCID: PMC12240829 | PMID: 40437094
- Evidence: We applied Scrublet 50 , integrated into Scanpy, to each cohort and removed cells with a doublet score exceeding the 90th percentile across all cohorts.
- Full pipeline: quality control [Scanpy] -> normalisation [igraph] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [clusterProfiler] -> visualisation [ComplexHeatmap, R, UMAP, igraph] -> stage not stated [CellChat, CellPhoneDB, SCENIC, Seurat, scDblFinder]

### Single-cell transcriptomics reveal how root tissues adapt to soil stress. (Nature 2025)

- DOI: 10.1038/s41586-025-08941-z | PMCID: PMC12176638 | PMID: 40307555
- Evidence: Putative doublets were identified and removed using DoubletFinder 42 with the estimated doublet rate from the 10X Genomics Chromium Single Cell 3′ Reagent Kit user guide.
- Full pipeline: read trimming [HTSeq, STAR] -> alignment/mapping [HISAT2, HTSeq, STAR, kallisto] -> quantification [HISAT2] -> normalisation [Seurat v3.1.5] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> visualisation [ComplexHeatmap, ImageJ, ggplot2] -> stage not stated [Jupyter, Monocle, R, scDblFinder]

### A distributed coding logic for thermosensation and inflammatory pain. (Nature 2025)

- DOI: 10.1038/s41586-025-08875-6 | PMCID: PMC12222022 | PMID: 40269164
- Evidence: Doublets were identified using DoubletFinder v.3, and doublets and non-neuronal cells were removed from the dataset.
- Full pipeline: quantification [NumPy v1.19.2, SciPy v1.5.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.19.2, SciPy v1.5.2] -> stage not stated [ImageJ, OpenCV, Python, Seurat, scDblFinder]

### Hepatic stellate cells control liver zonation, size and functions via R-spondin 3. (Nature 2025)

- DOI: 10.1038/s41586-025-08677-w | PMCID: PMC12003176 | PMID: 40074890
- Evidence: For human datasets, the output raw_feature_bc_matrix_filtered.h5 from CellBender for each sample was further subjected to doublet removal using Scrublet with the default parameters 80 .
- Full pipeline: alignment/mapping [kallisto v0.44.0] -> quantification [QuPath] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellPhoneDB, CellProfiler v4.2.1, GSEA v4.3.2, ImageJ, R, Seurat, ggplot2, ilastik v1.3.3p, scDblFinder, survival (R)]

### Glycocalyx dysregulation impairs blood-brain barrier in ageing and disease. (Nature 2025)

- DOI: 10.1038/s41586-025-08589-9 | PMCID: PMC11946907 | PMID: 40011765
- Version used: **2.0.4**
- Evidence: Ambient RNA was removed from each sample using SoupX (v1.6.2) and droplets containing multiple nuclei were filtered out using DoubletFinder (v2.0.4).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.32, Metascape] -> visualisation [DESeq2 v1.32] -> stage not stated [ImageJ, Seurat v4.1.1, SoupX v1.6.2, scDblFinder v2.0.4]

### Transcriptomic neuron types vary topographically in function and morphology. (Nature 2025)

- DOI: 10.1038/s41586-024-08518-2 | PMCID: PMC11864986 | PMID: 39939759
- Evidence: In order to filter out doublet cells from the analysis, initial clustering was performed on each batch separately, and the clustering information was used as an input for DoubletFinder 62 .
- Full pipeline: normalisation [ANTs, UMAP] -> registration [Suite2p] -> dimensionality reduction/clustering [SciPy, UMAP, pheatmap, scDblFinder] -> visualisation [pheatmap] -> stage not stated [ImageJ, Monocle, PsychoPy, R, Seurat, napari, scikit-learn]

### A comprehensive spatio-cellular map of the human hypothalamus. (Nature 2025)

- DOI: 10.1038/s41586-024-08504-8 | PMCID: PMC11922758 | PMID: 39910307
- Evidence: We used scran’s quickCluster function 52 to obtain an initial set of clusters that were used as input cluster assignments to scDblFinder, which was run with multiSampleMode set to ‘split’ 53 .
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP, scDblFinder] -> visualisation [R v4.2.1, Scanpy] -> stage not stated [GCTA, MAGMA, NumPy v1.26.4, VEP, edgeR v4.0.16, ggplot2 v3.4.4, igraph v1.5.1, limma v3.58.1, tidyverse v1.1.3]

### A neoantigen vaccine generates antitumour immunity in renal cell carcinoma. (Nature 2025)

- DOI: 10.1038/s41586-024-08507-5 | PMCID: PMC11903305 | PMID: 39910301
- Evidence: Doublets were identified and removed using three different methods: doubletFinder 77 (v.2.0.3), scDblFinder 78 (v.1.12.0) and nFeature_RNA > 2,500.
- Full pipeline: read trimming [Picard] -> alignment/mapping [RSEM v1.3.1, STAR] -> quantification [RSEM v1.3.1] -> registration [Mutect2, Strelka] -> dimensionality reduction/clustering [UMAP] -> structure determination [R v0.1.10] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Python, Seurat v4.3.0, pheatmap v1.0.12, scDblFinder]

### Mapping cells through time and space with moscot. (Nature 2025)

- DOI: 10.1038/s41586-024-08453-2 | PMCID: PMC11864987 | PMID: 39843746
- Evidence: We used Scrublet 116 , scDblFinder 117 , DoubletDetection 118 , scds 119 , SOLO 120 and DoubletFinder 121 .
- Full pipeline: alignment/mapping [Squidpy] -> quantification [ImageJ] -> normalisation [Scanpy, Signac] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> visualisation [Squidpy] -> stage not stated [AnnData, Python, SCENIC, SciPy, Seurat, Singularity, scDblFinder]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Evidence: To ensure that only single nuclei were analysed, we measured the doublet probability by Scrublet 49 and excluded all potential doublets receiving a score greater than 0.3 for downstream analyses.
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: Quality control and cell filtering Before integrating the datasets, doublets were predicted using DoubletFinder 51 and filtered out.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Gliomagenesis mimics an injury response orchestrated by neural crest-like cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08356-2 | PMCID: PMC11821533 | PMID: 39743595
- Version used: **1.4.0**
- Evidence: Doublets and multiplets were identified by scDblFinder (v1.4.0), and low-quality cells (percentage of mitochondrial >12%; number of genes detected per cell <800; number of unique molecular identifier (UMI) per cell <500) were removed as part of the quality control process.
- Full pipeline: quality control [scDblFinder v1.4.0] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat v4.5, UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Slingshot] -> visualisation [Cytoscape v3.9.1, UMAP, igraph] -> stage not stated [ArchR v1.0.1, CellChat v1.1.3, R, Squidpy v1.3.0]

### Aspartate signalling drives lung metastasis via alternative translation. (Nature 2025)

- DOI: 10.1038/s41586-024-08335-7 | PMCID: PMC7618879 | PMID: 39743589
- Version used: **1.8.0**
- Evidence: Our multiplet identification was confirmed based on the distribution of doublet scores estimated across the different cells in each separate sample using the R package scDblFinder (v1.8.0) 48 ( https://bioconductor.org/packages/release/bioc/html/scDblFinder.html ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Trim Galore] -> alignment/mapping [STAR v2.6.1] -> quantification [ImageJ, STAR v2.6.1] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, R, fgsea, limma] -> stage not stated [Bioconductor, DESeq2 v1.34.0, Monocle, Seurat v4.1.0, SoupX v1.6.2, scDblFinder v1.8.0]

### Dysregulation of mTOR signalling is a converging mechanism in lissencephaly. (Nature 2025)

- DOI: 10.1038/s41586-024-08341-9 | PMCID: PMC11798849 | PMID: 39743596
- Evidence: The remaining cells were re-clustered, and doublet scores were calculated using the DoubletFinder package.
- Full pipeline: quality control [PLINK v1.9] -> alignment/mapping [GATK v4.1] -> variant calling [GATK v4.1, PLINK v1.9, UMAP] -> quantification [Bioconductor v3.18, ImageJ] -> normalisation [ImageJ, R] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [Bioconductor v3.18] -> visualisation [UMAP] -> stage not stated [ANNOVAR, AlphaFold, GSEA, Picard, Seurat v4.3.0, SnpEff v5.1, VEP]

### Timely TGFβ signalling inhibition induces notochord. (Nature 2025)

- DOI: 10.1038/s41586-024-08332-w | PMCID: PMC11735409 | PMID: 39695233
- Evidence: Potential doublet cells were filtered out using Scrublet 82 with thresholds between 0.2 and 0.3.
- Full pipeline: dimensionality reduction/clustering [Slingshot, UMAP] -> stage not stated [PyTorch, R, Scanpy, scDblFinder]

### Spatial transcriptomic clocks reveal cell proximity effects in brain ageing. (Nature 2025)

- DOI: 10.1038/s41586-024-08334-8 | PMCID: PMC11798877 | PMID: 39695234
- Evidence: For each experiment, we removed putative doublets using Scrublet 97 and a doublet score cutoff of 0.18.
- Full pipeline: normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [AnnData v0.8.0, Matplotlib v3.5.1, Scanpy, UMAP, statsmodels v0.13.2] -> differential/statistical testing [SciPy, seaborn] -> simulation/modelling [scikit-learn] -> machine learning [PyTorch] -> visualisation [ImageJ v1.53n, UMAP] -> stage not stated [Cellpose v1.0.2, NumPy, QuPath v0.5.1, R, Squidpy, scDblFinder]

### Macrophages excite muscle spindles with glutamate to bolster locomotion. (Nature 2025)

- DOI: 10.1038/s41586-024-08272-5 | PMCID: PMC11735391 | PMID: 39633045
- Evidence: Doublets were removed from the dataset by DoubletFinder package (doublet formation rate was set as 7.5%).
- Full pipeline: quality control [FastQC, Seurat] -> read trimming [FastQC] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.1.2] -> visualisation [UMAP] -> stage not stated [DESeq2, ImageJ, ggplot2, scDblFinder]

### RANK drives structured intestinal epithelial expansion during pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-024-08284-1 | PMCID: PMC11666467 | PMID: 39633049
- Version used: **1.12.0**
- Evidence: Cells were subjected to a quality control step, keeping those cells expressing more than 500 genes, 1,000 UMIs and with less than 5% of UMIs assigned to mitochondrial genes and cells considered singlets by scDblFinder (v.1.12.0) with the default parameters.
- Full pipeline: quality control [scDblFinder v1.12.0] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [DESeq2, UMAP, clusterProfiler v4.4.4, fgsea v1.22.0] -> differential/statistical testing [DESeq2, GSEA, clusterProfiler v4.4.4, fgsea v1.22.0] -> stage not stated [ImageJ v2.3.0, R, Seurat v4.0.5, ggplot2, pheatmap]

### Liver X receptor unlinks intestinal regeneration and tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08247-6 | PMCID: PMC11779645 | PMID: 39567700
- Evidence: Doublet cells were excluded using DoubletFinder 55 .
- Full pipeline: quantification [kallisto] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [Enrichr, edgeR] -> stage not stated [Fiji, ImageJ, Python v3.9, QuPath, R v3.6.3, Seurat, scDblFinder]

### Chromatin accessibility during human first-trimester neurodevelopment. (Nature 2025)

- DOI: 10.1038/s41586-024-07234-1 | PMCID: PMC12589128 | PMID: 38693260
- Evidence: The 5-kb nucleus-by-bin matrix was used for doublet detection using an adapted version of DoubletFinder.
- Full pipeline: quality control [scikit-learn] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, HOMER, LDSC, MACS2, MAGMA, NumPy, scDblFinder]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Evidence: Heterotypic doublets were identified and removed using DoubletFinder (v2) 83 to ensure the integrity of singlet datasets.
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: Doublets were identified and removed using Scrublet 62 with prior set to 0.1.
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Synthetic super-enhancers enable precision viral immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10329-6 | PMCID: PMC13149004 | PMID: 41951744
- Evidence: Potential doublets were identified using the R package ‘DoubletFinder’ (v.2.0.4), with an expected doublets rate of 3%, as guided by Parse.
- Full pipeline: quantification [ImageJ v2.8] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [ImageJ v2.8] -> stage not stated [BEDTools, HOMER, MACS2, PHENIX, R, SCENIC, scDblFinder]

### Androgen activity in the male embryonic hindbrain drives lethal PFA ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10264-6 | PMCID: PMC13083265 | PMID: 41882358
- Version used: **2.0.3**
- Evidence: CellRanger-filtered count matrices per sample were preprocessed individually with the Seurat pipeline and filtered further (nFeature_RNA > 400, percent.mt < 3/4 quartile+ 3 times interquartile, genes expressed > 3 cells) and doublets were identified by DoubletFinder (v.2.0.3) 62 .
- Full pipeline: alignment/mapping [DESeq2] -> quantification [ImageJ v1.54g] -> normalisation [DESeq2] -> dimensionality reduction/clustering [SCENIC v0.10.3, UMAP] -> differential/statistical testing [R, ggplot2 v3.4.4] -> simulation/modelling [Monocle v1.3.1] -> structure determination [Python v3.8.2] -> machine learning [UMAP] -> visualisation [survival (R) v0.4.9] -> stage not stated [Harmony v0.1.1, Seurat, scDblFinder v2.0.3]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Version used: **2.0.4**
- Evidence: For exclusion of doublets, doublet probabilities were estimated using DoubletFinder (v.2.0.4, https://github.com/chris-mcginnis-ucsf/DoubletFinder ), and nuclei with high doublet scores were removed.
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### Precancerous niche remodelling dictates nascent tumour persistence. (Nature 2026)

- DOI: 10.1038/s41586-026-10157-8 | PMCID: PMC13148994 | PMID: 41781610
- Evidence: Doublets were identified using Scrublet 66 (v.0.2.3) and removed, along with low-quality cells, on the basis of per-sample quality-control metrics (Supplementary Table 2 ); cells with more than 15% mitochondrial reads or genes expressed in fewer than three cells were excluded, resulting in 91,347 high-quality cells.
- Full pipeline: variant calling [R] -> dimensionality reduction/clustering [Seurat, UMAP] -> stage not stated [SAMtools, scDblFinder]

### Human hippocampal neurogenesis in adulthood, ageing and Alzheimer's disease. (Nature 2026)

- DOI: 10.1038/s41586-026-10169-4 | PMCID: PMC13048220 | PMID: 41741649
- Evidence: Single-droplet multiplets were detected using the union of two independent methods: Scrublet 50 and DoubletDetection 51 .
- Full pipeline: quantification [edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [Seurat, UMAP, scVelo] -> differential/statistical testing [edgeR, limma] -> stage not stated [CellChat, SCENIC, scDblFinder]

### Single-cell and isoform-specific translational profiling of the mouse brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10118-1 | PMCID: PMC13102718 | PMID: 41708856
- Evidence: Scrublet was used to remove doublets in the data 81 .
- Full pipeline: read trimming [Cutadapt v1.18, STAR] -> alignment/mapping [Python, STAR] -> normalisation [UMAP, seaborn] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [DESeq2 v1.39.3] -> visualisation [seaborn] -> stage not stated [CellProfiler, GSEA, PyMOL, SAMtools, Scanpy, scDblFinder, scikit-learn]

### Agouti integrates environmental cues to regulate paternal behaviour. (Nature 2026)

- DOI: 10.1038/s41586-026-10123-4 | PMCID: PMC13019464 | PMID: 41708861
- Evidence: Data were demultiplexed by barcode and processed with 10X Genomics Cell Ranger, CellBender 64 and the R package scDblFinder 65 to filter and remove doublets and nuclei with high mitochondrial reads or ambient RNA and random barcode swapping.
- Full pipeline: read trimming [R, scDblFinder] -> dimensionality reduction/clustering [Harmony, UMAP] -> stage not stated [DESeq2, Seurat]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Evidence: Doublets were then removed using DoubletFinder (8,406 doublets, 13.2%).
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### PAF15-PCNA exhaustion governs the strand-specific control of DNA replication. (Nature 2026)

- DOI: 10.1038/s41586-025-10011-3 | PMCID: PMC12979207 | PMID: 41606318
- Version used: **1.2.0**
- Evidence: Doublets were estimated and removed using scDblFinder (v.1.2.0) 74 .
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.10.1] -> alignment/mapping [Bowtie2 v2.4, Cutadapt v2.6, Picard] -> normalisation [RSEM] -> dimensionality reduction/clustering [DESeq2, UMAP] -> differential/statistical testing [DESeq2, ggplot2 v3.5.1] -> visualisation [ggplot2 v3.5.1] -> stage not stated [AlphaFold, Fiji, Harmony v1.2.0, ImageJ, PyMOL, SAMtools v1.13, Seurat v4.0.3, deepTools v3.5.4, scDblFinder v1.2.0]

### Critical role for a high-plasticity cell state in lung cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09985-x | PMCID: PMC12960256 | PMID: 41565826
- Evidence: In the case of non-hashed transplant samples, the R package scDblFinder 75 was used to detect doublets, which were then removed before further analysis.
- Full pipeline: dimensionality reduction/clustering [scikit-learn] -> differential/statistical testing [SciPy, scikit-learn] -> machine learning [scikit-learn] -> stage not stated [AnnData, ImageJ, Jupyter, Matplotlib v3.8.4, NumPy, R, pingouin v0.5.4, scDblFinder]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Version used: **1.12**
- Evidence: Doublets were identified from the filtered aggregated count files using Scrublet 74 in Python v.3.6 or scDblFinder v.1.12 in R statistical software v.4.2.2.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### Mimicking opioid analgesia in cortical pain circuits. (Nature 2026)

- DOI: 10.1038/s41586-025-09908-w | PMCID: PMC12823415 | PMID: 41501467
- Evidence: Putative doublets identified by DoubletFinder, as well as residual clusters with mixed cell-type markers or high mean unique molecular identifier, were removed.
- Full pipeline: read trimming [STAR v2.7.1] -> alignment/mapping [STAR v2.7.1] -> dimensionality reduction/clustering [DESeq2, Seurat v4.3, SoupX, UMAP, scDblFinder] -> stage not stated [DeepLabCut]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: In brief, we used Scrublet 72 for cell-doublet calling with a two-step diffusion doublet identification, as previously described 73 .
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Lesion-remote astrocytes govern microglia-mediated white matter repair. (Nature 2026)

- DOI: 10.1038/s41586-025-09887-y | PMCID: PMC12823418 | PMID: 41407858
- Evidence: Scrublet 55 was used to remove predicted doublets from each sample.
- Full pipeline: alignment/mapping [STAR] -> normalisation [ImageJ, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [Enrichr, MACS2, emmeans, scDblFinder, scikit-learn]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **0.2.2**
- Evidence: For doublet detection and removal, we used the Scrublet (v.0.2.2) algorithm as implemented in scanpy, applied to each sample independently.
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### Specification of neuronal subtypes in the spiral ganglion begins prior to birth in the mouse. (PNAS 2022)

- DOI: 10.1073/pnas.2203935119 | PMCID: PMC9860252 | PMID: 36409884
- Version used: **2.0.3**
- Evidence: Data was processed and analyzed using the following R-based packages: Seurat (v3.2) ( 47 ), DoubletFinder (v2.0.3) ( 48 ), Harmony (v1.0) ( 49 ), Slingshot (v1.8) ( 17 ), tradeSeq (v1.4)( 20 ), Monocle 3 ( 21 , 50 ), and SCENIC ( 23 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Monocle, SCENIC, Seurat v3.2, Slingshot v1.8, scDblFinder v2.0.3]

### Ablation of lysophosphatidic acid receptor 1 attenuates hypertrophic cardiomyopathy in a mouse model. (PNAS 2022)

- DOI: 10.1073/pnas.2204174119 | PMCID: PMC9282378 | PMID: 35787042
- Evidence: Scrublet and Solo score was applied to scan for potential doublets.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [Fiji, ImageJ, UMAP] -> stage not stated [R v4.0, Seurat v3.1, scDblFinder]

### The HDAC inhibitor CI-994 acts as a molecular memory aid by facilitating synaptic and intracellular communication after learning. (PNAS 2022)

- DOI: 10.1073/pnas.2116797119 | PMCID: PMC9295763 | PMID: 35613054
- Evidence: DoubletFinder ( 89 ) was used to find and remove doublets and normalization and was done using SCTransform ( 90 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Nextstrain, UMAP] -> stage not stated [HOMER v4.11, Seurat v4.0.3]

### Single-cell transcriptomic classification of rabies-infected cortical neurons. (PNAS 2022)

- DOI: 10.1073/pnas.2203677119 | PMCID: PMC9295789 | PMID: 35609197
- Evidence: Doublets were identified using DoubletFinder ( 39 ) and excluded from analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [GSEA, ImageJ, R v4.1.1, Seurat v4.0, scDblFinder]

### Cellular and transcriptional diversity over the course of human lactation. (PNAS 2022)

- DOI: 10.1073/pnas.2121720119 | PMCID: PMC9169737 | PMID: 35377806
- Evidence: For each sample, Scrublet was run with default parameters and cells identified as doublets were removed from downstream analysis ( 78 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [DESeq2, SciPy, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [UMAP] -> stage not stated [Enrichr, R v3.6.2, Scanpy, Seurat, scDblFinder]

### Epigenetic state determines inflammatory sensing in neuroblastoma. (PNAS 2022)

- DOI: 10.1073/pnas.2102358119 | PMCID: PMC8832972 | PMID: 35121657
- Evidence: DoubletFinder ( 79 ) was used to remove doublets.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Trimmomatic v0.39] -> quantification [RSEM v1.2.12] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.07, MACS2, R, Seurat, ilastik v1.3.3, scDblFinder]

### Cellular and molecular architecture of submucosal glands in wild-type and cystic fibrosis pigs. (PNAS 2022)

- DOI: 10.1073/pnas.2119759119 | PMCID: PMC8794846 | PMID: 35046051
- Evidence: Matrix data were subjected to ambient RNA correction using the SoupX R package ( 72 ), doublet filtering using the Scrublet Python package ( 73 ), and dead and low-quality cell filtering in Seurat ( 74 ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [R, Seurat, SoupX, scDblFinder]

### Genetic and immune determinants of &lt;i&gt;E. coli&lt;/i&gt; liver abscess formation. (PNAS 2023)

- DOI: 10.1073/pnas.2310053120 | PMCID: PMC10743367 | PMID: 38096412
- Evidence: RunPCA and RunUMAP were used prior to doublet removal with DoubletFinder (pN = 0.25, pK = 0.09).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [Seurat v4.3, scDblFinder]

### Gene expression in the primate orbitofrontal cortex related to anxious temperament. (PNAS 2023)

- DOI: 10.1073/pnas.2305775120 | PMCID: PMC10710052 | PMID: 38011550
- Evidence: Data were filtered for doublets using Scrublet ( 29 ), which resulted in the exclusion of 9,687 cells.
- Full pipeline: alignment/mapping [Python v2.7] -> stage not stated [CellProfiler v4.2.1, ImageJ v1.53s, QuPath, Scanpy, limma, scDblFinder]

### Endothelial deletion of EPH receptor A4 alters single-cell profile and Tie2/Akap12 signaling to preserve blood-brain barrier integrity. (PNAS 2023)

- DOI: 10.1073/pnas.2204700120 | PMCID: PMC10576133 | PMID: 37796990
- Evidence: Genes that are not expressed in at least three cells and do not have a minimum 200 expressed genes were excluded, and we filtered for doublets (DoubletFinder package, v2.0.3).
- Full pipeline: quality control [FastQC, Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [Trim Galore, scDblFinder]

### A single-cell multiomic analysis of kidney organoid differentiation. (PNAS 2023)

- DOI: 10.1073/pnas.2219699120 | PMCID: PMC10193973 | PMID: 37155865
- Evidence: The DoubletFinder R package was further used to eliminate cells estimated to be doublets or multiplets.
- Full pipeline: quantification [UMAP] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.20.0] -> stage not stated [MACS2, R, Signac, scDblFinder]

### A tessellated lymphoid network provides whole-body T cell surveillance in zebrafish. (PNAS 2023)

- DOI: 10.1073/pnas.2301137120 | PMCID: PMC10193988 | PMID: 37155881
- Evidence: Doublets were also removed using DoubletFinder with an estimated rate of 3% ( 55 ).
- Full pipeline: normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP] -> stage not stated [ImageJ v2.1.0, scDblFinder]

### Distinctive transcriptomic and epigenomic signatures of bone marrow-derived myeloid cells and microglia in CNS autoimmunity. (PNAS 2023)

- DOI: 10.1073/pnas.2212696120 | PMCID: PMC9963604 | PMID: 36730207
- Evidence: Cell doublets, identified using the R package scDblFinder ( 26 ), and low-quality cells expressing <50 genes were purged.
- Full pipeline: quality control [ArchR] -> dimensionality reduction/clustering [GSEA, Signac, UMAP, clusterProfiler, fgsea] -> differential/statistical testing [MACS2] -> stage not stated [R, Seurat, scDblFinder]

### Neighbor-specific gene expression revealed from physically interacting cells during mouse embryonic development. (PNAS 2023)

- DOI: 10.1073/pnas.2205371120 | PMCID: PMC9926237 | PMID: 36595695
- Evidence: Notably, the frequencies of the heterotypic combinations identified using PICs were significantly high as compared with the combination of erroneous doublets identified using DoubletFinder ( 30 ) ( SI Appendix , Fig.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, Enrichr, scDblFinder]

### Investigating the &lt;i&gt;cis-&lt;/i&gt;regulatory basis of C&lt;sub&gt;3&lt;/sub&gt; and C&lt;sub&gt;4&lt;/sub&gt; photosynthesis in grasses at single-cell resolution. (PNAS 2024)

- DOI: 10.1073/pnas.2402781121 | PMCID: PMC11459142 | PMID: 39312655
- Evidence: Doublets were then removed using the in silico approach Scrublet ( 69 ) ( SI Appendix , Supplemental Methods ).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.16.1, minimap2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt v4.5, OrthoFinder, scDblFinder]

### Loss of primary cilia and dopaminergic neuroprotection in pathogenic LRRK2-driven and idiopathic Parkinson's disease. (PNAS 2024)

- DOI: 10.1073/pnas.2402206121 | PMCID: PMC11317616 | PMID: 39088390
- Evidence: This included removing potential multiplets using “DoubletFinder” [ https://github.com/chris-mcginnis-ucsf/DoubletFinder ( 58 )] and “cells” that displayed high mitochondrial gene expression (using the subset function to remove clusters with high expression of “MT-” genes).
- Full pipeline: dimensionality reduction/clustering [scDblFinder] -> visualisation [CellProfiler] -> stage not stated [Seurat]

### The dynamic behavior of chromatophores marks the transition from bands to spots in leopard geckos. (PNAS 2024)

- DOI: 10.1073/pnas.2400486121 | PMCID: PMC11260152 | PMID: 38976731
- Version used: **1.12.0**
- Evidence: Doublets were detected with scDblFinder v1.12.0 ( 62 ), considering default parameters.
- Full pipeline: alignment/mapping [IMOD] -> dimensionality reduction/clustering [UMAP] -> stage not stated [InterProScan, R, SAMtools v1.9, Seurat v4.2.0, VCFtools v0.1.16, ggplot2, pheatmap, scDblFinder v1.12.0]

### Cholinergic macrophages promote the resolution of peritoneal inflammation. (PNAS 2024)

- DOI: 10.1073/pnas.2402143121 | PMCID: PMC11228479 | PMID: 38923993
- Evidence: Additionally, doublets detected by simulation using the scDblFinder package were also filtered.
- Full pipeline: quantification [velocyto] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R] -> simulation/modelling [scDblFinder] -> stage not stated [FSL, SCENIC, fgsea]

### Pharmacological expansion of type 2 alveolar epithelial cells promotes regenerative lower airway repair. (PNAS 2024)

- DOI: 10.1073/pnas.2400077121 | PMCID: PMC11032444 | PMID: 38598345
- Evidence: In addition, Scrublet pipeline (v0.2.3, https://github.com/swolock/scrublet ) was applied to identify and remove doublets with a detected doublet rate of 4.7% resulting in 175,983 singlets for downstream analysis.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [scVelo] -> stage not stated [Scanpy, scDblFinder]

### Cationic cholesterol-dependent LNP delivery to lung stem cells, the liver, and heart. (PNAS 2024)

- DOI: 10.1073/pnas.2307801120 | PMCID: PMC10945827 | PMID: 38437539
- Evidence: DoubletFinder ( 49 ) was used to identify doublets.
- Full pipeline: stage not stated [ImageJ, Seurat, scDblFinder]

### Putative muscle stem cells promote &lt;i&gt;Xenopus&lt;/i&gt; tail regeneration by modifying macrophage function via &lt;i&gt;c1qtnf3&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2504410122 | PMCID: PMC12663952 | PMID: 41264239
- Evidence: After quality control, doublet removal using DoubletFinder ( 65 ), and normalization, datasets were integrated and visualized with Uniform Manifold Approximation and Projection ( 66 ).
- Full pipeline: quality control [scDblFinder] -> read trimming [HISAT2 v2.2.1, Trimmomatic v0.39] -> alignment/mapping [HISAT2 v2.2.1, Trimmomatic v0.39, edgeR v4.1.25, featureCounts v2.0.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v4.4, edgeR v4.1.25, featureCounts v2.0.6] -> visualisation [UMAP, scDblFinder] -> stage not stated [ImageJ, Monocle v1.2.7, Seurat, scVelo v0.3.1]

### Glycolipid nanoparticles target the spleen and detarget the liver without charge. (PNAS 2025)

- DOI: 10.1073/pnas.2409569122 | PMCID: PMC12625924 | PMID: 41183194
- Evidence: DoubletFinder (v3) was used to identify doublets as previously described ( 51 ).
- Full pipeline: normalisation [Seurat v4.0.4] -> dimensionality reduction/clustering [UMAP] -> stage not stated [scDblFinder]

### A TGF-βR/IL-2R immunomodulatory fusion protein transforms immunosuppression into T cell activation to enhance adoptive T cell therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2516951122 | PMCID: PMC12501114 | PMID: 40986340
- Evidence: Doublets were removed by Scrublet.
- Full pipeline: alignment/mapping [Python, Scanpy] -> stage not stated [GSEA v4.1.0, scDblFinder]

### Biomarkers of immune dysregulation and posttreatment inflammation in spinal muscular atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2506976122 | PMCID: PMC12501130 | PMID: 40986347
- Evidence: Doublets were removed with DoubletFinder ( 43 ) (v2.0.4), and SCTransform ( 44 ) (v0.4.1) was applied for normalization.
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> normalisation [ComplexHeatmap, edgeR, limma, scDblFinder] -> dimensionality reduction/clustering [GSEA, UMAP, clusterProfiler] -> simulation/modelling [Slingshot] -> stage not stated [CellChat, SCENIC, Seurat]

### Foxn3 is required to suppress aberrant ciliogenesis in nonphotoreceptor retinal neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2500871122 | PMCID: PMC12304973 | PMID: 40663603
- Evidence: In brief, cell doublets were removed using Scrublet ( 71 ), and microglia, astrocytes, and endothelial cells were removed as previously described ( 53 ).
- Full pipeline: alignment/mapping [HISAT2] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [HOMER, Seurat, deepTools, scDblFinder]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: Doublets were filtered using Scrublet ( 69 ) (Version 3.7.3).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### Cancer-associated fibroblast-derived SEMA3C facilitates colorectal cancer liver metastasis via NRP2-mediated MAPK activation. (PNAS 2025)

- DOI: 10.1073/pnas.2423077122 | PMCID: PMC12130859 | PMID: 40402249
- Version used: **2.0.3**
- Evidence: ...le-cell dataset was converted into a Seurat object using the R package Seurat (v4.4.0); 2) Doublets were removed from each sample using the R package DoubletFinder (v2.0.3) ( 33 ); 3) Novelty scores were calculated by determining the ratio of nFeature to nCount to assess the complexity of RNA species in each cell; 4) Cells with nFeature less than 200 or greater than 5,000, nCount less than 500 or ...
- Full pipeline: quality control [Harmony, R, Seurat v4.4.0] -> quantification [R, Seurat v4.4.0] -> normalisation [Harmony] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Slingshot] -> stage not stated [CellPhoneDB, GSEA, GSVA, Monocle, scDblFinder v2.0.3, survival (R)]

### Inflammatory cytokine upd3 induces axon length-dependent synapse removal by glia. (PNAS 2025)

- DOI: 10.1073/pnas.2422752122 | PMCID: PMC12130839 | PMID: 40392850
- Version used: **2.0.3**
- Evidence: Cell multiplets were identified by DoubletFinder (version 2.0.3) and removed.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Cutadapt v2.4, FastQC, MultiQC, kallisto v0.46.0] -> alignment/mapping [Cutadapt v2.4, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [DESeq2, Fiji, ImageJ, Seurat, scDblFinder v2.0.3]

### APOBEC2 deficiency disrupts hematopoietic lineage commitment, resulting in emergence of dual identity lymphocytes in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2531122123 | PMCID: PMC13250534 | PMID: 42247564
- Evidence: Doublets were identified and removed using DoubletFinder.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Seurat, scDblFinder]

### Lysosome-related organelles orchestrate guanine crystal formation in pigment cells. (PNAS 2026)

- DOI: 10.1073/pnas.2524305123 | PMCID: PMC13079938 | PMID: 41950095
- Version used: **1.18.0**
- Evidence: Doublet detection was performed using scDblFinder (v1.18.0), and cells identified as doublets were excluded from further analysis.
- Full pipeline: read trimming [Cutadapt, STAR v2.5.2b] -> alignment/mapping [STAR v2.5.2b] -> quantification [DESeq2 v1.36.1, HTSeq] -> normalisation [DESeq2 v1.36.1] -> dimensionality reduction/clustering [Cytoscape, R] -> differential/statistical testing [DESeq2 v1.36.1] -> visualisation [Cytoscape, Matplotlib, NumPy, OpenCV, Python] -> stage not stated [IMOD, ImageJ, Metascape, Seurat v5.1.0, lme4, scDblFinder v1.18.0]

### Meiotic prophase I disruption as a strategy for nonhormonal male contraception using small-molecule inhibitor JQ1. (PNAS 2026)

- DOI: 10.1073/pnas.2517498123 | PMCID: PMC13080027 | PMID: 41945432
- Version used: **2.0**
- Evidence: Ambient RNA contamination was corrected using SoupX (v1.4.5) ( 31 ), and putative doublets were identified and removed with DoubletFinder (v2.0) ( 32 ) following 10x Genomics recommendations.
- Full pipeline: quality control [SoupX v1.4.5, scDblFinder v2.0] -> alignment/mapping [STAR v2.5.3b] -> quantification [R] -> dimensionality reduction/clustering [Slingshot v2.4.0, UMAP] -> stage not stated [DESeq2, ImageJ, Seurat v4.1.1]

### Bacterial reporter-paired scRNA sequencing reveals cross talk between zinc starvation and zinc toxicity in macrophage antibacterial defense. (PNAS 2026)

- DOI: 10.1073/pnas.2530503123 | PMCID: PMC12993976 | PMID: 41802048
- Version used: **1.4.0**
- Evidence: Next, doublets were removed using scDblFinder v1.4.0.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [UMAP, scVelo v0.2.4, velocyto v0.17] -> differential/statistical testing [R v4.0] -> stage not stated [Seurat v4.0.4, scDblFinder v1.4.0]

### Lipid nanoparticle GM-CSF replacement for autoimmune pulmonary alveolar proteinosis. (PNAS 2026)

- DOI: 10.1073/pnas.2511483123 | PMCID: PMC12913010 | PMID: 41671176
- Evidence: Potential doublets were detected and filtered out using DoubletFinder (v3) ( 49 ).
- Full pipeline: normalisation [Seurat v4.0.4] -> dimensionality reduction/clustering [UMAP] -> stage not stated [QuPath, scDblFinder]

### Mapping the developing human immune system across organs. (Science 2022)

- DOI: 10.1126/science.abo0510 | PMCID: PMC7612819 | PMID: 35549310
- Version used: **0.2.3**
- Evidence: Low-quality cells were filtered out (minimum number of reads = 2000, minimum number of genes = 500, Scrublet (v0.2.3) ( 77 ) doublet detection score <0.4).
- Full pipeline: alignment/mapping [AnnData] -> quantification [scikit-learn] -> normalisation [Scanpy, scikit-learn] -> dimensionality reduction/clustering [Squidpy v1.1.2, UMAP, scikit-learn] -> machine learning [AnnData] -> visualisation [AnnData] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder v0.2.3]

### Cross-tissue immune cell analysis reveals tissue-specific features in humans. (Science 2022)

- DOI: 10.1126/science.abl5197 | PMCID: PMC7612735 | PMID: 35549406
- Evidence: Doublets were detected using Scrublet ( 68 ).
- Full pipeline: normalisation [Scanpy v1.6.0] -> dimensionality reduction/clustering [Scanpy v1.6.0, UMAP] -> visualisation [UMAP] -> stage not stated [PHENIX, scDblFinder]

### Yolk sac cell atlas reveals multiorgan functions during human early development. (Science 2023)

- DOI: 10.1126/science.add7564 | PMCID: PMC7614978 | PMID: 37590359
- Evidence: Scrublet ( 60 ) v0.2.3 was applied to each sequencing lane for doublet detection, and clusters with >(Median+(1.48*MAD)) (MAD: Median absolute deviation) of the median cluster doublet detection score were removed ( data S3 ).
- Full pipeline: normalisation [Scanpy] -> registration [OpenCV] -> dimensionality reduction/clustering [Cytoscape, Seurat v3.1, UMAP, scDblFinder, scikit-learn] -> differential/statistical testing [Seurat v3.1, statsmodels v0.13.5] -> visualisation [Cytoscape, Python, UMAP, seaborn v0.12.1] -> stage not stated [BigStitcher, CellPhoneDB v2.1.2, Enrichr, Matplotlib v3.6.2, SCENIC, SciPy, ggplot2, scVelo]

### Drugs of abuse hijack a mesolimbic pathway that processes homeostatic need. (Science 2024)

- DOI: 10.1126/science.adk6742 | PMCID: PMC11077477 | PMID: 38669575
- Evidence: The gene expression count matrix for each sample was processed with the following steps: ( 1 ) Estimate doublet with Scrublet ( https://github.com/swolock/scrublet ) ( 88 ); ( 2 ) Estimate and correct the ambient RNA contaminations with SoupX ( https://github.com/constantAmateur/SoupX ) ( 89 ); ( 3 ) Load the corrected counting matrix into Seurat object with log normalization; ( 4 ) Calculate the ...
- Full pipeline: quality control [Seurat, SoupX, scDblFinder] -> normalisation [Seurat, SoupX, scDblFinder] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [scikit-learn] -> machine learning [TensorFlow] -> stage not stated [ImageJ, Python, SciPy, Suite2p]

### PIEZO channels link mechanical forces to uterine contractions in parturition. (Science 2025)

- DOI: 10.1126/science.ady3045 | PMCID: PMC12807505 | PMID: 41231991
- Evidence: Doublets were detected and filtered using DoubletFinder ( 80 ).
- Full pipeline: alignment/mapping [Seurat] -> quantification [CellProfiler] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [SciPy, edgeR] -> visualisation [UMAP] -> stage not stated [scDblFinder]

### High-resolution spatial mapping of cell state and lineage dynamics in vivo with PEtracer. (Science 2025)

- DOI: 10.1126/science.adx3800 | PMCID: PMC12766569 | PMID: 40705858
- Evidence: Doublets were predicted using DoubletFinder ( 158 ) (v.2.0.3).
- Full pipeline: alignment/mapping [Python, scikit-image v0.24.0] -> normalisation [Scanpy v1.10.0] -> dimensionality reduction/clustering [Scanpy v1.10.0, UMAP] -> stage not stated [Cellpose v3.1.0, R v4.2.3, Seurat, Squidpy v1.6.2, scDblFinder]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: In addition, putative doublets were identified using the pre-SoupX matrix with scDblFinder ( 71 ) followed by removal of mitochondrial genes from the matrix.
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Multiplex generation and single-cell analysis of structural variants in mammalian genomes. (Science 2025)

- DOI: 10.1126/science.ado5978 | PMCID: PMC11931979 | PMID: 39883753
- Version used: **0.2.3**
- Evidence: Scrublet 0.2.3 ( 75 ) was run on filtered cells, and cells with doublet score <0.4 were retained, leaving 12460 and 8499 (K562 and mESC respectively, lane 1) and 20800 (K562, lane 2) high-quality cells for downstream analysis.
- Full pipeline: read trimming [Cutadapt v2.5] -> alignment/mapping [BEDTools v2.29.2] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [Matplotlib v3.8.1, Python, R, SciPy, Seurat v4.3.1, scDblFinder v0.2.3, seaborn v0.13.0]

### Systematic identification of Y-chromosome gene functions in mouse spermatogenesis. (Science 2025)

- DOI: 10.1126/science.ads6495 | PMCID: PMC7617377 | PMID: 39847625
- Evidence: Doublets were identified using the DoubletFinder R package (v2.0.3) ( Supplementary Table 19 ).
- Full pipeline: alignment/mapping [BLAST, BWA, R] -> quantification [DESeq2 v1.34] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [clusterProfiler v4.2.2, limma] -> visualisation [limma] -> stage not stated [GSEA, Python, Seurat, scDblFinder]

