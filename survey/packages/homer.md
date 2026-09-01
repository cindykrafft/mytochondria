# HOMER

- **Category:** genomics
- **Papers in survey:** 171
- **Journals:** PNAS (94), Nature (62), Cell (12), Science (3)
- **Years:** 2021 (13), 2022 (28), 2023 (30), 2024 (38), 2025 (40), 2026 (22)
- **Versions named:** 4.11 (16), 4.10 (7), 4.11.1 (4), 5.1 (3), 4.1.1 (1), 4.8 (1), 4.4 (1), 4.10.4 (1), 4.9.1 (1), 4.7 (1)
- **Pipeline stages it appears in:** differential/statistical testing (23), alignment/mapping (12), quantification (9), dimensionality reduction/clustering (7), normalisation (4), visualisation (2), variant calling (1)

## Papers

### Endogenous retroviruses promote homeostatic and inflammatory responses to the microbiota. (Cell 2021)

- DOI: 10.1016/j.cell.2021.05.020 | PMCID: PMC8381240 | PMID: 34166614
- Evidence: ...tics RRID: SCR_014583 Fiji image processing package Schindelin et al., 2012 RRID: SCR_003070 FlowJo software version 10.6.1 Treestar RRID: SCR_008520 HOMER software version 4.11 http://homer.ucsd.edu/ RRID: SCR_010881 Imaris software version Bitplane RRID: SCR_007370 Metascape http://metascape.org/gp/index.html#/main/step1 RRID: SCR_016620 Prism software version 9 GraphPad RRID: SCR_002798 R versi...
- Full pipeline: quality control [DESeq2, FastQC] -> alignment/mapping [Metascape, R v4.05, STAR, Seurat] -> dimensionality reduction/clustering [UMAP] -> stage not stated [HOMER]

### Lipolysis drives expression of the constitutively active receptor GPR3 to induce adipose thermogenesis. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.037 | PMCID: PMC8238500 | PMID: 34048700
- Evidence: ...s paper N/A pcDNA3.1(+) with CB1 ORF This paper N/A YFP-Epac-RLuc (CAMYEL) Jiang et al., 2007 N/A Software and algorithms STAR Dobin et al., 2013 N/A HOMER Heinz et al., 2010 N/A iRNA-seq Madsen et al., 2015 N/A DESeq2 Love et al., 2014 N/A Graphpad Prism 8.0 for statistical analysis GraphPad N/A Other Phenomaster home cage system TSE Systems N/A Constant climate chamber Memmert HPP750 Inveon mult...
- Full pipeline: differential/statistical testing [DESeq2, HOMER]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Evidence: ...nalysis pipeline This study https://github.com/MarioPujato/NextGenAligner bedtools Quinlan and Hall, 2010 https://github.com/arq5x/bedtools2/releases HOMER Heinz et al., 2010 http://homer.ucsd.edu/homer/ STAR Dobin et al., 2013 https://github.com/alexdobin/STAR HiCUP Wingett et al., 2015 https://www.bioinformatics.babraham.ac.uk/projects/hicup/ CHiCAGO Cairns et al., 2016 https://bioconductor.org/...
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### The intrinsic and extrinsic effects of TET proteins during gastrulation. (Cell 2022)

- DOI: 10.1016/j.cell.2022.06.049 | PMCID: PMC9432429 | PMID: 35908548
- Evidence: CTCF peaks ( Figure 5 F) where defined as CpGs with the top 0.1% of CTCF motif PWM energy from the HOMER ( http://homer.ucsd.edu/homer/motif/ ) motifs catalog.
- Full pipeline: stage not stated [Bowtie2, HOMER, ImageJ]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Version used: **4.10.3**
- Evidence: HomerTools in the software suite HOMER (version 4.10.3) was used to truncate raw sequencing reads at the restriction enzyme cutting site ( Heinz et al., 2010 ), followed by aligning reads to the human reference genome (GRCh38) with Bowtie2 (version 2.3.4.3) ( Langmead and Salzberg, 2012 ).
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **4.11**
- Evidence: Motif discovery and motif enrichment analysis We used HOMER 4.11 143 to identify novel motifs enriched in the regulatory of genes belonging to each multi-species gene module (calculated with WGCNA , see above).
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Version used: **4.10**
- Evidence: The motif analysis was performed with HOMER (version 4.10).
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### Human IRF1 governs macrophagic IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2022.12.038 | PMCID: PMC9907019 | PMID: 36736301
- Version used: **4.11**
- Evidence: We used the findMotifs.pl script from HOMER v4.11 202 with the human v.6.3 database and the parameter -len 12.
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq, STAR v2.7.3a] -> quantification [HTSeq] -> normalisation [edgeR v3.26.8] -> dimensionality reduction/clustering [R, Seurat v4.0.2, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER v4.11, scDblFinder]

### The primitive endoderm supports lineage plasticity to enable regulative development. (Cell 2024)

- DOI: 10.1016/j.cell.2024.05.051 | PMCID: PMC11290322 | PMID: 38917790
- Evidence: 127 N/A HOMER Heinz et al.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [BEDTools, CellProfiler v4.2.5, DESeq2 v1.40.2, HOMER, ImageJ, R v4.3, SAMtools, Scanpy v1.8.2, Seurat v4.3.0, deepTools, scVelo v0.2.5]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Version used: **4.10**
- Evidence: ...omics-data-analysis/lipid-search-software.html Zen Blue v3.4.0 Zeiss https://www.zeiss.com/microscopy/en/products/software/zeiss-zen.html#zenversions HOMER v4.10 Heinz et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### Repeat-element RNAs integrate a neuronal growth circuit. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.030 | PMCID: PMC12456964 | PMID: 40381624
- Evidence: 92 https://genome.ucsc.edu/ ; RRID:SCR_005780 HOMER algorithm Heinz et al.
- Full pipeline: alignment/mapping [STAR] -> quantification [HTSeq] -> stage not stated [BEDTools, Bioconductor, Bowtie2, DESeq2 v1.36, Fiji, HOMER, ImageJ, RSEM, RepeatMasker, deepTools, edgeR]

### Transcriptional regulation by PHGDH drives amyloid pathology in Alzheimer's disease. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.045 | PMCID: PMC12204802 | PMID: 40273909
- Version used: **4.11**
- Evidence: Motif finding: The findMotifsGenome.pl module of HOMER (version 4.11) was applied to the PHGDH peaks that are reproduced, i.e. called by MACS2, in at least two replicates of the Serum+ experimental groups (Serum+/Src and Serum+/KD).
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [Bowtie2, SAMtools, fastp] -> quantification [Bowtie2, fastp] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bowtie2, fastp] -> visualisation [R] -> stage not stated [AlphaFold, HOMER v4.11, MACS2, Seurat, deepTools]

### An atlas of gene regulatory elements in adult mouse cerebrum. (Nature 2021)

- DOI: 10.1038/s41586-021-03604-1 | PMCID: PMC8494637 | PMID: 34616068
- Evidence: Known motifs from HOMER 61 with enrichment P value < 10 −10 are shown. e , UMAP 58 embedding of cell types involved in adult neurogenesis at the SGZ (top) and SVZ (bottom). f , Predicted transcription factors in different cell types involved in neurogenesis in the SGZ and SVZ. g , UMAP 58 embedding of NIPCs and radial glia-like cells coloured by cell type (top) and brain region (bottom). h , Heat ...
- Full pipeline: quality control [R] -> alignment/mapping [R] -> dimensionality reduction/clustering [BEDTools, HOMER, UMAP, scikit-learn] -> differential/statistical testing [HOMER, Monocle v0.2.2] -> stage not stated [Enrichr, MACS2, SAIGE, Seurat v3.0, scDblFinder]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Evidence: Transcription factor motif enrichment analysis The findMotifsGenome.pl tool from the HOMER suite 65 ( http://homer.ucsd.edu/homer/ ) was used to identify transcription factor motif enrichments in peak sets.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### A multimodal cell census and atlas of the mammalian primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03950-0 | PMCID: PMC8494634 | PMID: 34616075
- Evidence: Displayed are known motifs from HOMER with enrichment -log p-value > 10.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [DESeq2 v1.30.0, MACS2, Python v3.6, UMAP, scikit-learn v0.24.2] -> differential/statistical testing [DESeq2 v1.30.0, HOMER] -> visualisation [UMAP] -> stage not stated [R v3.5.3, Seurat, ggplot2 v3.2.1]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: TF motif enrichment and co-occurrence analyses: Motif enrichment analysis was performed individually on each of the 6 ATAC-peak clusters using the HOMER de novo motif discovery tool 60 using findMotifsGenome command with size = given and length = 8 parameters.
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Evidence: For motif analysis, HOMER findMotifGenome.pl was used with a customized motif database from JASPAR 2018.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### Collagenolysis-dependent DDR1 signalling dictates pancreatic cancer outcome. (Nature 2022)

- DOI: 10.1038/s41586-022-05169-z | PMCID: PMC9588640 | PMID: 36198801
- Version used: **4.11**
- Evidence: Quantification of transcripts was performed using HOMER (v.4.11).
- Full pipeline: quality control [R v4.0.2, Seurat] -> alignment/mapping [STAR] -> quantification [HOMER v4.11] -> dimensionality reduction/clustering [GSEA]

### Single-cell roadmap of human gonadal development. (Nature 2022)

- DOI: 10.1038/s41586-022-04918-4 | PMCID: PMC9300467 | PMID: 35794482
- Evidence: 78 ), SwissRegulon 79 , HOMER 80 . chromVar returns a matrix with binding activity estimates of each TF in each cell, which we used to test for differential TF binding activity between cell types in a one-versus-all fashion with Wilcoxon Rank Sum test (FindAllMarkers function in Seurat).
- Full pipeline: alignment/mapping [Scanpy v1.7.0] -> normalisation [Seurat, Signac] -> dimensionality reduction/clustering [Scanpy v1.7.0, Signac, SoupX, UMAP] -> differential/statistical testing [HOMER] -> machine learning [scikit-learn] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, GSEA, PHENIX, R, scDblFinder, scVelo v0.2.4]

### A joint NCBI and EMBL-EBI transcript set for clinical genomics and research. (Nature 2022)

- DOI: 10.1038/s41586-022-04558-8 | PMCID: PMC9007741 | PMID: 35388217
- Evidence: We used HOMER 39 to analyse nucleotide frequencies, the FIMO 40 tool from the MEME suite to scan for motifs using a position weight matrix (PWM) from JASPAR 41 for analysis of TATA boxes and a PWM from ref.
- Full pipeline: stage not stated [HISAT2 v2.1, HOMER, VEP]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Version used: **4.10**
- Evidence: De novo and known motif enrichment analysis All de novo and known motif enrichment analyses were performed using the HOMER (v.4.10) suite of algorithms43.
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Evidence: Annotation of TEs and TSS proximity For each human element in each category (DMR, peak, loop, boundary), we annotated its TE association and identified its TSS proximity using annotatePeaks.pl with hg38 from HOMER 84 .
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Single-cell analysis of chromatin accessibility in the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06824-9 | PMCID: PMC10719105 | PMID: 38092917
- Evidence: 2 Identification and characterization of cCREs across mouse brain cell types. a , The fraction of cCREs that overlaps with annotated sequences in the mouse genome was determined using HOMER 45 .
- Full pipeline: dimensionality reduction/clustering [BEDTools, UMAP, clusterProfiler, scikit-learn] -> stage not stated [HOMER, MACS2, Monocle, R, RepeatMasker, Seurat, deepTools, scDblFinder]

### FOXP3 recognizes microsatellites and bridges DNA through multimerization. (Nature 2023)

- DOI: 10.1038/s41586-023-06793-z | PMCID: PMC10719092 | PMID: 38030726
- Evidence: Peaks were called using HOMER with an input control 22 and were ranked on the basis of the signal intensity using samtools 55 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> registration [MotionCor2] -> differential/statistical testing [DESeq2] -> structure determination [RELION v4.0.1, UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [BEDTools, CTFFIND v4.1, HOMER, MACS2, PHENIX]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Evidence: The DA OCRs in the ATAC-seq data were assigned for the nearest genes to generate a list of DA genes using HOMER software 76 .
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Version used: **4.11.1**
- Evidence: Motif enrichment analysis was performed using HOMER (v.4.11.1).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### Transient naive reprogramming corrects hiPS cells functionally and epigenetically. (Nature 2023)

- DOI: 10.1038/s41586-023-06424-7 | PMCID: PMC10447250 | PMID: 37587336
- Evidence: Enriched motifs for each cluster were identified using HOMER with findMotifsGenome.pl and the options hg19 -size given 67 .
- Full pipeline: read trimming [Bowtie2, HISAT2, fastp] -> alignment/mapping [Bowtie2, HISAT2, SAMtools v1.13, fastp, minimap2 v2.17] -> normalisation [UMAP] -> dimensionality reduction/clustering [BEDTools v2.30.0, HOMER, UMAP] -> differential/statistical testing [edgeR] -> stage not stated [MACS2, R, Seurat v3.1.1]

### Astrocyte-neuron subproteomes and obsessive-compulsive disorder mechanisms. (Nature 2023)

- DOI: 10.1038/s41586-023-05927-7 | PMCID: PMC10132990 | PMID: 37046092
- Evidence: 1d,e include known and new proteins; the full list in Supplementary Table 1 includes genes that encode synaptic proteins for neurons (for example, GRIA4 , HOMER , Dlg4 , Shank1 and Ank1 ) and genes that encode membrane and cytoskeletal proteins in astrocytes (for example, Ezr , Slc1a2 , Atp1a2 , Kcnj10 and Rdx ).
- Full pipeline: alignment/mapping [STAR] -> quantification [ImageJ] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [Bioconductor, limma v3.54] -> visualisation [Cytoscape v3.8, R, UMAP] -> stage not stated [Enrichr, Fiji, HOMER, STRING db]

### Spatial multiomics map of trophoblast development in early pregnancy. (Nature 2023)

- DOI: 10.1038/s41586-023-05869-0 | PMCID: PMC10076224 | PMID: 36991123
- Evidence: 1.12.2 with positional weight matrices from JASPAR2018 70 , HOCOMOCOv10 71 , SwissRegulon 72 , HOMER 73 . chromVar returns a matrix with binding activity estimates of each transcription factor in each cell, which we used to test for differential transcription factor binding activity between trophoblast cell states with FindMarkers function in Seurat (default parameters) in the same way as describe...
- Full pipeline: alignment/mapping [Scanpy v1.7.1] -> normalisation [Signac] -> dimensionality reduction/clustering [Scanpy v1.7.1, Signac, UMAP] -> differential/statistical testing [HOMER, R, Seurat, edgeR v3.32.1, limma v3.46.0] -> simulation/modelling [R, Seurat, Slingshot v1.8.0, edgeR v3.32.1, limma v3.46.0] -> stage not stated [BEDTools v2.30.0, CellPhoneDB, GSEA, PHENIX, TensorFlow, scDblFinder]

### Telomere-to-mitochondria signalling by ZBP1 mediates replicative crisis. (Nature 2023)

- DOI: 10.1038/s41586-023-05710-8 | PMCID: PMC9946831 | PMID: 36755096
- Version used: **4.10**
- Evidence: Library sizes were normalized to 1 × 10 7 for comparison and the log 2 ratio of enrichment of immunoprecipitates versus input was calculated at each base in the subtelomere using HOMER v.4.10 and the assembly available of human subtelomeres 63 .
- Full pipeline: alignment/mapping [STAR v2.5.3a] -> normalisation [HOMER v4.10] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [R v3.6.1, ggplot2 v3.3.2] -> stage not stated [CellProfiler v4.2.1, ComplexHeatmap, ImageJ]

### Dissecting cell identity via network inference and in silico gene perturbation. (Nature 2023)

- DOI: 10.1038/s41586-022-05688-9 | PMCID: PMC9946838 | PMID: 36755098
- Evidence: This annotation is performed using HOMER ( http://homer.ucsd.edu/homer/ ).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [velocyto] -> visualisation [Matplotlib] -> stage not stated [AnnData, HOMER, Jupyter, Monocle, NumPy, Python, R v3.6, SCENIC, Scanpy, SciPy, Seurat, WGCNA, igraph, scikit-learn]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **4.11**
- Evidence: Stage-specific and constitutive peaks were determined using UpSetR (v.1.4.0) 126 , and both the consensus peak set and the stage-specific peak sets were classified by genomic region using HOMER (v.4.11) 127 and further curated.
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### A DNA methylation atlas of normal human cell types. (Nature 2023)

- DOI: 10.1038/s41586-022-05580-6 | PMCID: PMC9811898 | PMID: 36599988
- Evidence: Motif analysis For each cell type we analysed the top 1,000 differentially unmethylated regions for known motifs (Supplementary Table 6a ) using the HOMER function ‘findMotifsGenome.pl’, with parameters ‘-bits’ and ‘-size 250’ 39 .
- Full pipeline: alignment/mapping [SAMtools v1.9] -> dimensionality reduction/clustering [SciPy v1.6.3] -> differential/statistical testing [HOMER] -> stage not stated [BEDTools v2.26.0, deepTools v3.4.1, scikit-learn]

### Senescence atlas reveals an aged-like inflamed niche that blunts muscle regeneration. (Nature 2023)

- DOI: 10.1038/s41586-022-05535-x | PMCID: PMC9812788 | PMID: 36544018
- Version used: **4.10.4**
- Evidence: Differentially accessible peaks were further annotated by HOMER (v.4.10.4) 95 , the associated motif enrichment analysis was performed by HOMER using the default settings.
- Full pipeline: quality control [FastQC v0.11.8, Seurat v4.0.3, scDblFinder v2.0] -> read trimming [Bioconductor, edgeR v3.30.0] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.5, SAMtools v1.3.1, edgeR v3.30.0, featureCounts v1.6.2] -> quantification [Bioconductor, GSEA v4.0.3, edgeR v3.30.0, featureCounts v1.6.2] -> normalisation [Bioconductor, deepTools v3.3.1, edgeR v3.30.0] -> dimensionality reduction/clustering [Cytoscape v3.7.2, Seurat v4.0.3, UMAP, scDblFinder v2.0] -> differential/statistical testing [DESeq2, HOMER v4.10.4, Seurat v4.0.3, scDblFinder v2.0] -> visualisation [ImageJ, Seurat v4.0.3, scDblFinder v2.0] -> stage not stated [R, Trim Galore v0.5.0]

### Enhancing transcription-replication conflict targets ecDNA-positive cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07802-5 | PMCID: PMC11540844 | PMID: 39506153
- Version used: **4.11.1**
- Evidence: HOMER (v.4.11.1) was used for de novo transcript identification on each strand separately using the default GRO-seq setting.
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, Trim Galore, Trimmomatic] -> quantification [CellProfiler v4.2.1] -> normalisation [deepTools] -> visualisation [deepTools] -> stage not stated [HOMER v4.11.1, ImageJ v1.53t, MACS2, SAMtools v1.8]

### Machine-guided design of cell-type-targeting cis-regulatory elements. (Nature 2024)

- DOI: 10.1038/s41586-024-08070-z | PMCID: PMC11525185 | PMID: 39443793
- Evidence: ( b ) To explore additional genomic features that may overlap DHS-natural and Malinois-natural sequences were annotated using annotatePeaks.pl from the HOMER suite.
- Full pipeline: quantification [DESeq2 v1.32.0] -> normalisation [DESeq2 v1.32.0] -> dimensionality reduction/clustering [SciPy] -> differential/statistical testing [DESeq2 v1.32.0] -> machine learning [PyTorch, Python] -> stage not stated [BEDTools v2.30.0, BLAST, HOMER, scikit-learn v1.2.2]

### DNA methylation controls stemness of astrocytes in health and ischaemia. (Nature 2024)

- DOI: 10.1038/s41586-024-07898-9 | PMCID: PMC11464379 | PMID: 39232166
- Version used: **4.4**
- Evidence: We used HOMER 4.4 61 with the Jaspar2022 motif database 76 to identify motifs enriched in these VMRs: findMotifsGenome.pl VMRs.bed mm10r output/ -len 5,6,7,8,9,10,11,12 -size given -mcheck JASPAR.db -mknown JASPAR.db The same strategy was used to identify motifs enriched in regions with low methylation in the neurogenic lineage (5,000 VMRs with the highest PC2 loading) and in common parenchymal as...
- Full pipeline: read trimming [Bismark v0.22.3, Trim Galore v0.4.4] -> alignment/mapping [Bismark v0.22.3, STAR v2.7.3a, Trim Galore v0.4.4] -> quantification [R] -> normalisation [UMAP] -> dimensionality reduction/clustering [Seurat v4.1.0, UMAP] -> visualisation [ComplexHeatmap v2.12.0, tidyverse v1.3.1] -> stage not stated [BEDTools v2.30.0, Cellpose v2.2.2, HOMER v4.4]

### Position-dependent function of human sequence-specific transcription factors. (Nature 2024)

- DOI: 10.1038/s41586-024-07662-z | PMCID: PMC11269187 | PMID: 39020164
- Evidence: While HOMER2 is used to analyse sequences and account for sequence biases near TSSs, similar to its predecessor HOMER 23 , the software package can be used for a wide range of data analysis.
- Full pipeline: read trimming [Cutadapt v3.4, fastp] -> alignment/mapping [STAR v2.7.10a, fastp] -> variant calling [PLINK v2.00a] -> normalisation [DESeq2] -> stage not stated [BCFtools, HOMER]

### Control of neuronal excitation-inhibition balance by BMP-SMAD1 signalling. (Nature 2024)

- DOI: 10.1038/s41586-024-07317-z | PMCID: PMC11078759 | PMID: 38632412
- Evidence: Motif enrichment analysis for BMP2-responsive peaks and constitutive peaks was performed separately by screening for the enrichment of known motifs with the default settings of HOMER 64 .
- Full pipeline: alignment/mapping [BEDTools, Bioconductor, STAR] -> differential/statistical testing [edgeR] -> visualisation [STAR] -> stage not stated [HOMER, ImageJ, MACS2, Python, R, ggplot2, limma]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: Motif enrichments of differential peaks and grouped peaks were searched with HOMER and findMotifsGenome.pl with default parameters.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Evidence: 1 and in FOXO1-overexpressing CAR T cells as determined by HOMER analysis. d , Principal component analysis of ATAC-seq data for indicated CAR T cell populations. e , Number of peaks with differential accessibility in FOXO1-expressing CAR T cells relative to controls before and after stimulation.
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### APOE4/4 is linked to damaging lipid droplets in Alzheimer's disease microglia. (Nature 2024)

- DOI: 10.1038/s41586-024-07185-7 | PMCID: PMC10990924 | PMID: 38480892
- Evidence: HOMER was used to convert aligned reads into ‘tag directories’ for further analysis 55 .
- Full pipeline: alignment/mapping [HOMER, STAR v2.5.1b] -> quantification [Fiji, ImageJ] -> normalisation [R v4.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, ImageJ, R v4.3, Seurat] -> stage not stated [Bowtie2, MACS2, Python v3.9.12, Scanpy, scDblFinder v0.2.3]

### Autonomous transposons tune their sequences to ensure somatic suppression. (Nature 2024)

- DOI: 10.1038/s41586-024-07081-0 | PMCID: PMC10901741 | PMID: 38355802
- Evidence: UMAP of FLASH data For construction of the UMAP, peak calling was carried out on all profiles using HOMER: findPeaks {tag_directory} -style factor -strand separate -o {peaks.txt} -i {background_tag_directory}.
- Full pipeline: read trimming [Cutadapt v4.1, STAR v2.7.9a] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.7.9a, featureCounts v2.0.1] -> quantification [DESeq2] -> normalisation [Jupyter, scikit-learn] -> dimensionality reduction/clustering [HOMER, Jupyter, UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R] -> visualisation [Jupyter, scikit-learn]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: HOMER findMotifsGenome.pl (version 4.6) 78 was used to investigate the motif enrichment in pairwise comparisons and unbiasedly clustered groups of peaks.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Alternative splicing of latrophilin-3 controls synapse formation. (Nature 2024)

- DOI: 10.1038/s41586-023-06913-9 | PMCID: PMC10830413 | PMID: 38233523
- Evidence: After blocking with 0.5% fish skin gelatin in 1× DPBS at 37 °C for 1 h, the culture was stained with chicken anti-MAP2 (Encor, CPCA-MAP2, 1:1,000), guinea pig anti-vGluT1 (Milipore, AB5905, 1:1,000), and rabbit anti-HOMER (Milipore, ABN37, 1:1,000) antibodies in blocking buffer at 4 °C overnight.
- Full pipeline: alignment/mapping [STAR] -> quantification [scikit-image v0.20.0] -> stage not stated [CaImAn, DESeq2, HOMER, HTSeq, SciPy v1.10.1]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Evidence: For ATAC-seq, regions of open chromatin were identified by running HOMER peak calling in ‘region’ mode, with a fragment size of 150 bp and a peak size of 300 bp.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### In vitro production of cat-restricted Toxoplasma pre-sexual stages. (Nature 2024)

- DOI: 10.1038/s41586-023-06821-y | PMCID: PMC10781626 | PMID: 38093015
- Evidence: From this pipeline, HOMER (annotatePeaks) was used to analyse peak distribution relative to gene features.
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Picard] -> alignment/mapping [MACS2 v2.2, Picard, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, MACS2 v2.2, limma] -> stage not stated [HOMER, SAMtools v1.4]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **4.10**
- Evidence: Transcription factor motif enrichment was done using HOMER (v.4.10).
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Spatial joint profiling of DNA methylome and transcriptome in tissues. (Nature 2025)

- DOI: 10.1038/s41586-025-09478-x | PMCID: PMC12571926 | PMID: 40903587
- Evidence: The HOMER 62 findMotifsGenome function was then applied to analyse the enrichment of known TF motifs using its default database.
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [Python, R, UMAP, clusterProfiler, pheatmap] -> visualisation [Python] -> stage not stated [HOMER, Seurat]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Version used: **4.8**
- Evidence: Peaks were annotated using HOMER (v4.8).
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### The genomic origin of the unique chaetognath body plan. (Nature 2025)

- DOI: 10.1038/s41586-025-09403-2 | PMCID: PMC12460157 | PMID: 40804517
- Evidence: Motif enrichment was performed using HOMER (v.5) for both known and de novo motifs and plant derived motifs were excluded from results relying on known motifs 95 .
- Full pipeline: alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.2, IQ-TREE v2.1.1, MAFFT v7.471, STAR v2.5.2b, Trinity v2.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools v2.30.0] -> structure determination [IQ-TREE v2.1.1, MAFFT v7.471, RepeatMasker v4.1.0] -> stage not stated [BLAST, BUSCO v5.4.1, Bioconductor, HOMER, InterProScan, Seurat]

### Elementary 3D organization of active and silenced E. coli genome. (Nature 2025)

- DOI: 10.1038/s41586-025-09396-y | PMCID: PMC12460168 | PMID: 40804527
- Version used: **4.11.1**
- Evidence: Motifs The motif analysis was performed using HOMER (v4.11.1).
- Full pipeline: alignment/mapping [BWA] -> quantification [ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [DESeq2] -> stage not stated [BEDTools, Conda, HOMER v4.11.1]

### Range extender mediates long-distance enhancer activity. (Nature 2025)

- DOI: 10.1038/s41586-025-09221-6 | PMCID: PMC12267059 | PMID: 40604280
- Evidence: We then performed differential motif enrichment analysis using the findMotifsGenome.pl command in HOMER with a given size 90 comparing short- and long-range E–P sets for (1) predicted E–P pairs for bona fide enhancers (using VISTA enhancer coordinates) and (2) predicted E–P pairs for putative limb enhancers defined by scATAC–seq.
- Full pipeline: alignment/mapping [BEDTools] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [HOMER] -> stage not stated [MACS2, R, Signac]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: HOMER TF motif enrichment TF motif enrichment analysis was performed on the set of peaks that were differentially accessible for patients categorized as HiSquam or HiCol by using HOMER.
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Evidence: Motif analysis Loop anchor regions of M. leidyi ( n = 8,523) and H. californensis ( n = 478) were scanned for enriched motifs with HOMER 114 in de novo motif discovery mode.
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Version used: **5.1**
- Evidence: Motif enrichment was done using findMotifsGenome.pl (HOMER 5.1 (ref.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Evidence: To identify differential accessible sites, we created tag directories using the processed mapped files as input for the makeTagDirectory function of HOMER 78 .
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### Bidirectional histone monoaminylation dynamics regulate neural rhythmicity. (Nature 2025)

- DOI: 10.1038/s41586-024-08371-3 | PMCID: PMC11754111 | PMID: 39779849
- Version used: **4.11**
- Evidence: Peak annotation and motif analysis of MACS2 70 called peaks were performed using HOMER (v.4.11) 71 .
- Full pipeline: alignment/mapping [Bowtie2 v2.5.0, STAR v2.7.11b] -> quantification [ImageJ] -> normalisation [ImageJ, deepTools v3.5.1] -> structure determination [PHENIX] -> visualisation [tidyverse v2.0.0] -> stage not stated [BEDTools, Enrichr, HOMER v4.11, HTSeq v2.0.5, MACS2 v3.0.0a, R, SAMtools v1.9]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Evidence: Circular genome tracks Circular tracks of Micro-C contacts, MNase, ChIP–seq and ATAC–seq were prepared using the HOMER software package 97 in combination with Circos 98 .
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Fetal hepatocytes protect the HSPC genome via fetuin-A. (Nature 2025)

- DOI: 10.1038/s41586-024-08307-x | PMCID: PMC11711094 | PMID: 39633051
- Version used: **4.11**
- Evidence: DNA-binding factor motifs were analysed by determining the motifs in the differential peaks using HOMER (v4.11).
- Full pipeline: quality control [Trim Galore v0.6.7] -> read trimming [BWA] -> alignment/mapping [BWA, Bowtie2 v2.3.5.1, HISAT2 v2.2.1, HTSeq] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.0, HOMER v4.11] -> visualisation [deepTools v3.5.1] -> stage not stated [ImageJ v1.52p, MACS2, Picard v2.25.5, R]

### Chromatin accessibility during human first-trimester neurodevelopment. (Nature 2025)

- DOI: 10.1038/s41586-024-07234-1 | PMCID: PMC12589128 | PMID: 38693260
- Evidence: Peaks overlapping with the ENCODE blacklist were removed and the remainder were annotated using HOMER 54 on the basis of Gencode v32, after which the nucleus-by-peak matrix was generated.
- Full pipeline: quality control [scikit-learn] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, HOMER, LDSC, MACS2, MAGMA, NumPy, scDblFinder]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Version used: **4.1.1**
- Evidence: Peak annotation was conducted using HOMER (v4.1.1) 101 .
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **5.1**
- Evidence: Motif enrichment in DAPs was performed using HOMER (v.5.1) 69 .
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Evidence: Proximal elements were annotated with HOMER 67 , and distal regulatory interactions were inferred on the basis of Cicero 68 co-accessibility scores to link distal enhancers to putative gene targets.
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Synthetic super-enhancers enable precision viral immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10329-6 | PMCID: PMC13149004 | PMID: 41951744
- Evidence: Genomic regions near SOX2 and SOX9 peaks were annotated using HOMER 45 .
- Full pipeline: quantification [ImageJ v2.8] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [ImageJ v2.8] -> stage not stated [BEDTools, HOMER, MACS2, PHENIX, R, SCENIC, scDblFinder]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **4.11**
- Evidence: Transcription factor motif analysis was conducted using the HOMER (v.4.11) transcription factor motif discovery algorithm, and P values were adjusted for multiple testing using the Benjamini–Hochberg procedure to control for false discoveries.
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### Genome modelling and design across all domains of life with Evo 2. (Nature 2026)

- DOI: 10.1038/s41586-026-10176-5 | PMCID: PMC13128491 | PMID: 41781614
- Evidence: For comparison, HOMER 36 , a specialized motif discovery algorithm, only recalls 35% of the same motifs (Extended Data Fig.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HMMER, Pangolin] -> machine learning [AUGUSTUS, UMAP] -> stage not stated [AlphaFold, BLAST, HOMER]

### Activated ATF6α is a hepatic tumour driver restricting immunosurveillance. (Nature 2026)

- DOI: 10.1038/s41586-025-10036-8 | PMCID: PMC12999494 | PMID: 41639449
- Evidence: CUT&RUN analysis identified direct target genes by using the HOMER’s annotatePeaks.pl tool on the final peak set and selecting genes with a peak located within ±1 kb of their transcription start site.
- Full pipeline: quality control [BEDTools v2.30.0, FastQC v0.11.5, MultiQC v1.8, Nextflow v24.04.2, SAMtools v1.17, Trim Galore v0.6.5, deepTools v3.5.1] -> read trimming [Cutadapt v2.3, STAR, Trim Galore v0.6.5] -> alignment/mapping [FastQC v0.11.5, MultiQC v1.8, STAR] -> quantification [Bioconductor, DESeq2 v1.22.2, FastQC v0.11.5, GSVA, MultiQC v1.8, R, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, DESeq2 v1.22.2, R] -> visualisation [Matplotlib v10.5281, UMAP] -> stage not stated [CellProfiler, Cellpose v2.0, GSEA, HOMER, ImageJ v1.54g, QuPath v0.5.1, Scanpy, Seurat, metafor]

### CFAP20 salvages arrested RNAPII from the path of co-directional replisomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09943-7 | PMCID: PMC12935552 | PMID: 41535461
- Evidence: Initiation zones present in both datasets were identified using mergePeaks of HOMER tools (v.4.8.2) 65 , with -d given.
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.7a, Trim Galore v0.6.5] -> alignment/mapping [BWA v0.7.17, STAR v2.7.7a, Trim Galore v0.6.5] -> quantification [AlphaFold] -> stage not stated [HOMER, SAMtools v1.11]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: Consensus peaks set across all Flag antibody samples were created using BEDTools; featureCounts 84 was used to count consensus peaks in each sample; and HOMER was used to annotate peaks relative to gene features and perform motif enrichment analysis.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: The average chromatin landscape at IZs was computed using HOMER on a 1 Mb region centred on each IZ centre and plotted using R.
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Astrocyte CCN1 stabilizes neural circuits in the adult brain. (Nature 2026)

- DOI: 10.1038/s41586-025-09770-w | PMCID: PMC12823447 | PMID: 41407862
- Version used: **4.10**
- Evidence: Raw and normalized (FPKM) gene expression was quantified across all genes using the top-expressed isoform using HOMER (v.4.10).
- Full pipeline: alignment/mapping [STAR] -> quantification [CellProfiler, HOMER v4.10] -> normalisation [DESeq2 v1.14.1, HOMER v4.10] -> dimensionality reduction/clustering [AnnData, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.14.1] -> visualisation [UMAP] -> stage not stated [GSEA, Harmony, ImageJ, PsychoPy v2.22, Python, STRING db, Seurat v5.1.0, Suite2p, napari]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Evidence: Right, average binding motifs of the depicted transcription factors, using HOMER software.
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### Lymph node environment drives FSP1 targetability in metastasizing melanoma. (Nature 2026)

- DOI: 10.1038/s41586-025-09709-1 | PMCID: PMC12779575 | PMID: 41193799
- Evidence: Transcription factor activity and motif enrichment were assessed with Chromvar and HOMER, respectively.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [HISAT2, MACS2, Picard, Salmon v0.7.2] -> quantification [QuPath v0.5, Salmon v0.7.2] -> dimensionality reduction/clustering [igraph] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER]

### Specific hypomethylation programs underpin B cell activation in early multiple sclerosis. (PNAS 2021)

- DOI: 10.1073/pnas.2111920118 | PMCID: PMC8713784 | PMID: 34911760
- Evidence: The P values were calculated using the Hypergeometric Optimization of Motif EnRichment (HOMER) annotatePeaks.pl function.
- Full pipeline: differential/statistical testing [HOMER]

### Trained innate immunity, long-lasting epigenetic modulation, and skewed myelopoiesis by heme. (PNAS 2021)

- DOI: 10.1073/pnas.2102698118 | PMCID: PMC8545490 | PMID: 34663697
- Evidence: Interestingly, HOMER motif analysis revealed several Bach2-binding sites at the Nfix locus, suggesting a potential regulatory axis between Bach2 and Nfix ( Dataset S6 ).
- Full pipeline: alignment/mapping [SAMtools] -> normalisation [R] -> dimensionality reduction/clustering [ArchR v0.9.5, UMAP] -> differential/statistical testing [R] -> visualisation [ArchR v0.9.5] -> stage not stated [HOMER, MACS2, Seurat]

### MSX2 safeguards syncytiotrophoblast fate of human trophoblast stem cells. (PNAS 2021)

- DOI: 10.1073/pnas.2105130118 | PMCID: PMC8449346 | PMID: 34507999
- Evidence: ( E ) De novo motifs identified by HOMER.
- Full pipeline: stage not stated [HOMER]

### Genome accessibility dynamics in response to phosphate limitation is controlled by the PHR1 family of transcription factors in <i>Arabidopsis</i>. (PNAS 2021)

- DOI: 10.1073/pnas.2107558118 | PMCID: PMC8379931 | PMID: 34385324
- Evidence: Peaks were called for each replicate using the find Peaks function within HOMER suite v4.11 ( 44 ) with the following parameters: -style histone -size 75 -minDist 75 and -gsize 1.2e8.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.9.1, SAMtools v1.10, STAR v2.7.5b] -> quantification [HTSeq v0.9.1, STAR v2.7.5b] -> differential/statistical testing [R, edgeR] -> visualisation [deepTools v3.5.0] -> stage not stated [Bioconductor, HOMER]

### Dynamic chromatin regulatory landscape of human CAR T cell exhaustion. (PNAS 2021)

- DOI: 10.1073/pnas.2104758118 | PMCID: PMC8325267 | PMID: 34285077
- Evidence: Peaks were annotated with HOMER ( 60 ).
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [BEDTools, DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, MACS2, Picard, R]

### Muscle injury causes long-term changes in stem-cell DNA methylation. (PNAS 2022)

- DOI: 10.1073/pnas.2212306119 | PMCID: PMC9907067 | PMID: 36534800
- Evidence: For pathway enrichment, we used STRING databases ( 45 ) and assigned genes to specific DMRs using HOMER nearest gene analysis ( 43 ).
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> differential/statistical testing [R] -> stage not stated [DESeq2, HOMER, HTSeq v0.6.0, ImageJ]

### Genome-wide chromatin accessibility analysis unveils open chromatin convergent evolution during polyploidization in cotton. (PNAS 2022)

- DOI: 10.1073/pnas.2209743119 | PMCID: PMC9636936 | PMID: 36279429
- Version used: **4.11**
- Evidence: Annotation of the DHSs relative to genes was performed with the annotatePeaks function of the HOMER v.4.11 package.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools v1.9] -> quantification [Cufflinks v2.2.1, deepTools v3.1.3] -> normalisation [Cufflinks v2.2.1, deepTools v3.1.3] -> visualisation [deepTools v3.1.3] -> stage not stated [BEDTools v2.29.2, DESeq2, HOMER v4.11, MACS2 v2.1.4, OrthoFinder v2.3.8]

### Winter warming post floral initiation delays flowering via bud dormancy activation and affects yield in a winter annual crop. (PNAS 2022)

- DOI: 10.1073/pnas.2204355119 | PMCID: PMC9522361 | PMID: 36122201
- Evidence: For each module, the enriched motif in promoter regions (+100 bp to −2,000 bp) was identified by HOMER with default parameters ( 38 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4, HISAT2 v2.2.1] -> normalisation [deepTools v2.3] -> visualisation [deepTools v2.3] -> stage not stated [HOMER, Picard, R, WGCNA]

### Long noncoding RNA &lt;i&gt;CHROMR&lt;/i&gt; regulates antiviral immunity in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2210321119 | PMCID: PMC9477407 | PMID: 36001732
- Evidence: ( H ) Hypergeometric Optimization of Motif EnRichment (HOMER) analysis of promoter regions depleted of H3K27Ac after CHROMR knockdown, showing transcription factors with highest similarity score in motif indicated in bars.
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA, STAR, Trimmomatic, featureCounts] -> quantification [STAR, featureCounts] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [Enrichr, HOMER, MACS2, R]

### The amino acid sensor GCN2 controls red blood cell clearance and iron metabolism through regulation of liver macrophages. (PNAS 2022)

- DOI: 10.1073/pnas.2121251119 | PMCID: PMC9436309 | PMID: 35994670
- Evidence: Peak annotations, tag directory, bed files, and de novo motif discovery were performed using HOMER (Hypergeometric Optimization of Motif EnRichment) v4.7 ( 71 ).
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BWA v0.7.12] -> differential/statistical testing [MACS2] -> stage not stated [HOMER, R, Seurat v3.0.1]

### Adrenergic receptor signaling induced by Klf15, a regulator of regeneration enhancer, promotes kidney reconstruction. (PNAS 2022)

- DOI: 10.1073/pnas.2204338119 | PMCID: PMC9388080 | PMID: 35939709
- Evidence: De novo identification of transcription factor motifs enriched in open chromatin element was performed with HOMER tools (RRID:SCR_010881; parameters: -size 200 -mask) ( 23 ).
- Full pipeline: differential/statistical testing [MACS2 v2.2.6, edgeR v3.32.1, featureCounts v2.0.1] -> stage not stated [BEDTools v2.30.0, HOMER]

### Tcf-1 promotes genomic instability and T cell transformation in response to aberrant β-catenin activation. (PNAS 2022)

- DOI: 10.1073/pnas.2201493119 | PMCID: PMC9371646 | PMID: 35921443
- Evidence: ( E ) Pathway analysis of down-regulated (blue) and up-regulated (red) genes uniquely bound by Tcf-1 in CAT ( Top ) and the most significantly enriched transcription factor binding motifs (HOMER, Bottom ).
- Full pipeline: normalisation [GSEA] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA] -> stage not stated [HOMER, Metascape]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Version used: **4.10**
- Evidence: Using the HOMER (v4.10) software suite ( 43 ), bedgraph files and tag directories were made.
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### The ZCCHC14/TENT4 complex is required for hepatitis A virus RNA synthesis. (PNAS 2022)

- DOI: 10.1073/pnas.2204511119 | PMCID: PMC9282228 | PMID: 35867748
- Version used: **4.11**
- Evidence: Peaks enriched for reads mapping to cellular RNAs were identified with the CLIPper program as described ( 48 ), and annotated with HOMER version 4.11 ( homer.ucsd.edu/homer/ ).
- Full pipeline: alignment/mapping [HOMER v4.11, deepTools]

### Single-cell transcriptome and accessible chromatin dynamics during endocrine pancreas development. (PNAS 2022)

- DOI: 10.1073/pnas.2201267119 | PMCID: PMC9245718 | PMID: 35733248
- Evidence: ATAC-seq fragments corresponding to the peaks were quantified by using the annotatePeaks.pl function in the HOMER suite, a genome analysis tool (v.4.10) ( 44 ).
- Full pipeline: read trimming [Bowtie2, MACS2] -> alignment/mapping [Bowtie2, MACS2] -> quantification [HOMER] -> dimensionality reduction/clustering [Monocle, R] -> simulation/modelling [Monocle] -> visualisation [R]

### Immune checkpoint inhibitors unleash pathogenic immune responses against the microbiota. (PNAS 2022)

- DOI: 10.1073/pnas.2200348119 | PMCID: PMC9245641 | PMID: 35727974
- Evidence: Gene counts were calculated with HOMER’s analyzeRepeats with parameters -condenseGenes.
- Full pipeline: differential/statistical testing [DESeq2] -> stage not stated [HOMER, Metascape]

### The HDAC inhibitor CI-994 acts as a molecular memory aid by facilitating synaptic and intracellular communication after learning. (PNAS 2022)

- DOI: 10.1073/pnas.2116797119 | PMCID: PMC9295763 | PMID: 35613054
- Version used: **4.11**
- Evidence: We assigned enhancers to genes using HOMER (v4.11) annotatePeaks.pl ( 87 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2 v2.3.5, STAR v2.6] -> normalisation [scDblFinder] -> dimensionality reduction/clustering [Nextstrain, UMAP] -> stage not stated [HOMER v4.11, Seurat v4.0.3]

### H3K9 methylation drives resistance to androgen receptor-antagonist therapy in prostate cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2114324119 | PMCID: PMC9173765 | PMID: 35584120
- Evidence: Resulting intervals with read counts >5 were annotated using HOMER and kept as putative VBIM insertion sites.
- Full pipeline: quality control [Cutadapt] -> read trimming [Cutadapt] -> alignment/mapping [BEDTools, Bowtie2, Cufflinks, TopHat v2.0.7] -> quantification [GSEA, GSVA, HOMER, R, kallisto] -> differential/statistical testing [Cufflinks]

### An ancient founder mutation located between <i>ROBO1</i> and <i>ROBO2</i> is responsible for increased microtia risk in Amerindigenous populations. (PNAS 2022)

- DOI: 10.1073/pnas.2203928119 | PMCID: PMC9173816 | PMID: 35584116
- Evidence: Biological replicates were merged using HOMER.
- Full pipeline: alignment/mapping [BWA, GATK, Picard] -> variant calling [PLINK v1.9, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, PLINK v1.9] -> stage not stated [ADMIXTURE v1.3, HOMER, R, SnpEff]

### Transcriptome-wide subtyping of pediatric and adult T cell acute lymphoblastic leukemia in an international study of 707 cases. (PNAS 2022)

- DOI: 10.1073/pnas.2120787119 | PMCID: PMC9169777 | PMID: 35385357
- Evidence: To predict target genes that might be affected by wrapping/bridging motifs, we employed HOMER ( 39 ), combined with chromatin immunoprecipitation-sequencing data of GATA3 WT in human Jurkat cell lines ( 40 ) ( Dataset S7 ), to define three sets of target genes: genes affected by wrapping motifs (wrapping targets), bridging motifs (bridging targets), and those insusceptible to wrapping/bridging mot...
- Full pipeline: stage not stated [HOMER]

### Natural disaster and immunological aging in a nonhuman primate. (PNAS 2022)

- DOI: 10.1073/pnas.2121663119 | PMCID: PMC8872742 | PMID: 35131902
- Evidence: To characterize putative gene regulatory mechanisms, we tested for enrichment of TF binding motifs within 2 kb upstream and downstream of TF start sites of genes significantly associated with aging and Hurricane Maria using the program HOMER ( 84 ).
- Full pipeline: alignment/mapping [ANGSD, kallisto] -> quantification [limma] -> normalisation [limma] -> differential/statistical testing [R v4.0.2] -> stage not stated [HOMER, Seurat]

### A distinct role of STING in regulating glucose homeostasis through insulin sensitivity and insulin secretion. (PNAS 2022)

- DOI: 10.1073/pnas.2101848119 | PMCID: PMC8851542 | PMID: 35145023
- Version used: **4.11.1**
- Evidence: Motif enrichment analysis and peak-associated gene annotation were performed using HOMER (v4.11.1) ( 56 ) using peaks filtered by |log 2 FC| > 0.5, P < 0.05 and normalized read counts > 0.
- Full pipeline: read trimming [Bowtie2 v2.3.5.1] -> alignment/mapping [Bowtie2 v2.3.5.1] -> quantification [HOMER v4.11.1] -> normalisation [HOMER v4.11.1] -> dimensionality reduction/clustering [clusterProfiler, pheatmap v1.0.12] -> visualisation [clusterProfiler, pheatmap v1.0.12]

### MRP5 and MRP9 play a concerted role in male reproduction and mitochondrial function. (PNAS 2022)

- DOI: 10.1073/pnas.2111617119 | PMCID: PMC8832985 | PMID: 35121660
- Evidence: With two independent analysis platforms (MEME suite and HOMER), we identified significant enrichment of conserved retinoic acid–related binding motifs including putative RXRs and RORA binding sequences ( SI Appendix , Fig.
- Full pipeline: quality control [FastQC v0.11.7] -> differential/statistical testing [Bioconductor v3.4, DESeq2 v1.12.3, R v3.6.1] -> stage not stated [HOMER]

### The m<sup>6</sup>A reader YTHDC2 is essential for escape from KSHV SOX-induced RNA decay. (PNAS 2022)

- DOI: 10.1073/pnas.2116662119 | PMCID: PMC8872733 | PMID: 35177478
- Evidence: ( B ) Most significant DRACH motifs with m 6 A peaks identified by HOMER in latent and lytic cells.
- Full pipeline: dimensionality reduction/clustering [R, clusterProfiler] -> stage not stated [HOMER]

### BRD4-directed super-enhancer organization of transcription repression programs links to chemotherapeutic efficacy in breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2109133119 | PMCID: PMC8832982 | PMID: 35105803
- Evidence: Significantly, HOMER (Hypergeometric Optimization of Motif EnRichment) ( http://homer.ucsd.edu/homer/ ) analysis of the BRD4, LSD1, and MTA3 peaks also revealed that the binding summits of BRD4, LSD1, and MTA3 indeed contained similar sequence motifs ( SI Appendix , Fig.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> alignment/mapping [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [Bioconductor, HOMER, MACS2]

### BRD9 regulates interferon-stimulated genes during macrophage activation via cooperation with BET protein BRD4. (PNAS 2022)

- DOI: 10.1073/pnas.2110812119 | PMCID: PMC8740701 | PMID: 34983841
- Evidence: RNA expression was quantified as raw integer counts using analyzeRepeats.pl in Hypergeometric Optimization of Motif EnRichment (HOMER) using the following parameters: -strand both -count exons -condenseGenes -noadj.
- Full pipeline: alignment/mapping [STAR] -> quantification [HOMER] -> stage not stated [GSEA]

### Antigen exposure reshapes chromatin architecture in central memory CD8&lt;sup&gt;+&lt;/sup&gt; T cells and imprints enhanced recall capacity. (PNAS 2023)

- DOI: 10.1073/pnas.2313476120 | PMCID: PMC10742382 | PMID: 38085779
- Evidence: ( C – E ) Top motifs of CTCF binding sites in Ctcf_C1-3 when regrouped into promoter ( Top ), distal without and with CTCF motif ( Middle and Bottom , respectively) subsets based on HOMER analysis.
- Full pipeline: stage not stated [HOMER]

### The USP7-STAT3-granzyme-Par-1 axis regulates allergic inflammation by promoting differentiation of IL-5-producing Th2 cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302903120 | PMCID: PMC10710068 | PMID: 38015852
- Evidence: HOMER tag directories were created using the HOMER platform ( 51 ) (makeTagDirectory) from the aligned SAM formats using Samtools ( 52 ).
- Full pipeline: alignment/mapping [Bowtie2, Cufflinks v2.0.2, HOMER, SAMtools, TopHat v1.3.2, deepTools v2.0] -> quantification [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Monocle] -> visualisation [Cytoscape v3.7.1, MACS2] -> stage not stated [Seurat]

### Microbiota configuration determines nutritional immune optimization. (PNAS 2023)

- DOI: 10.1073/pnas.2304905120 | PMCID: PMC10710091 | PMID: 38011570
- Evidence: Gene expression was assessed using HOMER’s analyzeRepeats.pl with parameters rna, mm10, -count exons, -condenseGenes.
- Full pipeline: dimensionality reduction/clustering [GSEA, clusterProfiler] -> stage not stated [Bowtie2 v2.4.2, HOMER, HUMAnN v3.0, QIIME 2 v2020.2]

### Epigenetic switch reshapes epithelial progenitor cell signatures and drives inflammatory pathogenesis in hidradenitis suppurativa. (PNAS 2023)

- DOI: 10.1073/pnas.2315096120 | PMCID: PMC10710069 | PMID: 38011564
- Evidence: Right , logo visualization of the top HOMER motif outputs generated from healthy ( F ) and HS ( G ) merged ATAC seq datasets, respectively.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [CellChat] -> visualisation [CellChat, HOMER, UMAP]

### The human adenovirus E1B-55K oncoprotein coordinates cell transformation through regulation of DNA-bound host transcription factors. (PNAS 2023)

- DOI: 10.1073/pnas.2310770120 | PMCID: PMC10622919 | PMID: 37883435
- Evidence: Due to the sheer number of different A12-associated motifs identified by HOMER in this dataset, we chose to focus on the three most significant, namely, TEAD, AP-1, and p53, in a subsequent stringent biological pathway analysis.
- Full pipeline: alignment/mapping [MACS2, R] -> stage not stated [HOMER, Metascape]

### SoxC transcription factors shape the epigenetic landscape to establish competence for sensory differentiation in the mammalian organ of Corti. (PNAS 2023)

- DOI: 10.1073/pnas.2301301120 | PMCID: PMC10450657 | PMID: 37585469
- Evidence: To identify transcription factors that may establish chromatin accessibility as part of acquisition of competence for sensory differentiation, we analyzed the newly accessible E13.5 regulatory elements for enriched DNA motifs (HOMER)( 41 ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [HOMER]

### Comprehensive tissue deconvolution of cell-free DNA by deep learning for disease diagnosis and monitoring. (PNAS 2023)

- DOI: 10.1073/pnas.2305236120 | PMCID: PMC10334733 | PMID: 37399400
- Evidence: We analyzed the enrichment of transcription factor binding motifs at the marker regions using HOMER.
- Full pipeline: stage not stated [HOMER, Python]

### The KEAP1-NRF2 pathway regulates TFEB/TFE3-dependent lysosomal biogenesis. (PNAS 2023)

- DOI: 10.1073/pnas.2217425120 | PMCID: PMC10235939 | PMID: 37216554
- Evidence: Hypergeometric Optimization of Motif EnRichment (HOMER) analysis of known motifs in the DEGs revealed enrichment of genes containing an ARE ( Fig.
- Full pipeline: stage not stated [GSEA, HOMER]

### TRAF4-mediated nonproteolytic ubiquitination of androgen receptor promotes castration-resistant prostate cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2218229120 | PMCID: PMC10193960 | PMID: 37155905
- Evidence: ChIP-Seq normalized signal plots were generated using HOMER ( 80 ).
- Full pipeline: normalisation [HOMER] -> stage not stated [BEDTools, GSEA, MACS2 v2.1.0]

### Tonic-signaling chimeric antigen receptors drive human regulatory T cell exhaustion. (PNAS 2023)

- DOI: 10.1073/pnas.2219086120 | PMCID: PMC10083618 | PMID: 36972454
- Evidence: ( D ) Transcription factor motifs enriched in TS-CAR Tregs were identified by HOMER.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> normalisation [HTSeq v0.11.2, edgeR v3.24.3, limma v3.38.3] -> differential/statistical testing [R] -> visualisation [ggplot2 v3.2.1, pheatmap v1.0.12] -> stage not stated [GSEA, HOMER, fgsea v1.8.0]

### Endoplasmic reticulum-bound ANAC013 factor is cleaved by RHOMBOID-LIKE 2 during the initial response to hypoxia in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2221308120 | PMCID: PMC10242721 | PMID: 36897975
- Evidence: ( D ) The MDM motif is overrepresented in the identified binding peaks under hypoxia as determined by HOMER motif analysis.
- Full pipeline: stage not stated [HOMER]

### KMT2D acetylation by CREBBP reveals a cooperative functional interaction at enhancers in normal and malignant germinal center B cells. (PNAS 2023)

- DOI: 10.1073/pnas.2218330120 | PMCID: PMC10089214 | PMID: 36893259
- Evidence: To identify TF binding motifs enriched in CREBBP/KMT2D-cobound chromatin domains, we used the HOMER motif discovery algorithm (homer2 version) using default parameters and both the de novo and known motif functions ( 60 ).
- Full pipeline: alignment/mapping [HISAT2, featureCounts v1.6.3] -> quantification [ImageJ, featureCounts v1.6.3] -> normalisation [ImageJ] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R v4.2, SciPy] -> stage not stated [GSEA, HOMER]

### Multifaceted role for p53 in pancreatic cancer suppression. (PNAS 2023)

- DOI: 10.1073/pnas.2211937120 | PMCID: PMC10013849 | PMID: 36848578
- Evidence: Peaks with significant changes in accessibility between p53-proficient and deficient acinar cells were further analyzed for motif enrichment using the program HOMER ( 61 ).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, MACS2]

### METTL3 is essential for normal progesterone signaling during embryo implantation via m<sup>6</sup>A-mediated translation control of progesterone receptor. (PNAS 2023)

- DOI: 10.1073/pnas.2214684120 | PMCID: PMC9945998 | PMID: 36693099
- Version used: **4.7**
- Evidence: Motifs in m 6 A peaks were identified using HOMER v4.7 ( 77 ).
- Full pipeline: alignment/mapping [Cufflinks v2.2.1] -> stage not stated [HOMER v4.7, ImageJ, MACS2, R]

### PGC-1α drives small cell neuroendocrine cancer progression toward an ASCL1-expressing subtype with increased mitochondrial capacity. (PNAS 2024)

- DOI: 10.1073/pnas.2416882121 | PMCID: PMC11626175 | PMID: 39589879
- Evidence: To determine whether transcription factors (TFs) coactivated by PGC-1α are more accessible in the ASCL1 subtype than in the POU2F3/ASCL2 subtype, Hypergeometric Optimization of Motif EnRichment (HOMER) analysis was performed to compare the accessible peaks in both tumor subtypes.
- Full pipeline: differential/statistical testing [GSEA] -> stage not stated [HOMER]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: Peaks were tested for overrepresented transcription factor binding motifs using HOMER ( 76 ) and the function “findMotifsGenome.pl”, specifying the parameters “-size given” and “-mset vertebrate”.
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### The glucocorticoid receptor potentiates aldosterone-induced transcription by the mineralocorticoid receptor. (PNAS 2024)

- DOI: 10.1073/pnas.2413737121 | PMCID: PMC11588051 | PMID: 39541347
- Evidence: Subsequent downstream analysis was performed using HOMER pipeline.
- Full pipeline: quality control [Cutadapt v1.18] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Bowtie2, STAR v2.70] -> normalisation [DESeq2] -> stage not stated [HOMER, SAMtools]

### Characterization of the enzyme for 5-hydroxymethyluridine production and its role in silencing transposable elements in dinoflagellates. (PNAS 2024)

- DOI: 10.1073/pnas.2400906121 | PMCID: PMC11572971 | PMID: 39508766
- Evidence: For analyzing repetitive elements, multimapped reads quantification was performed using HOMER’s makeTagDirectory with the “-keepOne” option to retain all primary alignments.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [Bowtie2 v2.2.5, HOMER, STAR v2.7.10a] -> quantification [HOMER] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [deepTools v3.5.5, featureCounts v1.5.3]

### Genome-wide profiling of soybean WRINKLED1 transcription factor binding sites provides insight into seed storage lipid biosynthesis. (PNAS 2024)

- DOI: 10.1073/pnas.2415224121 | PMCID: PMC11551420 | PMID: 39475647
- Evidence: DNA motif enrichment analysis was performed as described ( 29 ), using the DNA motifs AW-BOX (CNTNGNNNNNNNCG), CNC-Box (CNCCNCC), G-Box (CACGTG), RY (CATGCA), and CCAAT-Box (CCAAT) to screen the GmWRI1 and GmLEC1 binding sites and 500 bps windows around the TSS of WRI1 directly regulated genes in Arabidopsis using the “known” function from HOMER ( 56 ).
- Full pipeline: read trimming [edgeR] -> variant calling [edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [HOMER, MACS2]

### Transcriptional repression by HDAC3 mediates T cell exclusion from &lt;i&gt;Kras&lt;/i&gt; mutant lung tumors. (PNAS 2024)

- DOI: 10.1073/pnas.2317694121 | PMCID: PMC11494357 | PMID: 39388266
- Evidence: Sequenced reads were quality tested, aligned to the mouse mm10 genome, and analyses were carried out using HOMER ( 59 ).
- Full pipeline: alignment/mapping [HOMER, STAR] -> stage not stated [Enrichr, GSEA, QuPath]

### Enhancer landscape of lung neuroendocrine tumors reveals regulatory and developmental signatures with potential theranostic implications. (PNAS 2024)

- DOI: 10.1073/pnas.2405001121 | PMCID: PMC11474083 | PMID: 39361648
- Evidence: Regular H3K27ac peaks were called using HOMER ( 49 ), with style “histone” for variable length, and super-enhancer using style “super” and requiring a local fold change of 1 (-L 1).
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.10a] -> quantification [QuPath v0.5.1, featureCounts] -> differential/statistical testing [DESeq2] -> visualisation [deepTools] -> stage not stated [BEDTools, HOMER]

### The androgen receptor in mesenchymal progenitors regulates skeletal muscle mass via &lt;i&gt;Igf1&lt;/i&gt; expression in male mice. (PNAS 2024)

- DOI: 10.1073/pnas.2407768121 | PMCID: PMC11441553 | PMID: 39292748
- Version used: **4.11**
- Evidence: Motif enrichment analysis of AR peaks was performed with HOMER (v4.11) ( 72 ) findMotifs with -size 200 -mask options and AR peaks were annotated to mm10 genes using annotatePeaks (-size 200 -mask) from MACS2 summit files.
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.2.1] -> quantification [featureCounts v2.0.1] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, Metascape, R, SAMtools v1.10, Trim Galore v0.6.7]

### High-throughput screen identifies non inflammatory small molecule inducers of trained immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2400413121 | PMCID: PMC11260140 | PMID: 38976741
- Evidence: In order to determine whether differentially accessible chromatin peaks localized near genes with shared functional biological pathways, we first assigned peaks to genes using HOMER annotatePeaks.pl ( 52 ).
- Full pipeline: quality control [FastQC, R] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> differential/statistical testing [HOMER, edgeR, limma] -> stage not stated [BEDTools, Conda v2020.11, MACS2, Python, SAMtools, fgsea]

### An atlas of the tomato epigenome reveals that KRYPTONITE shapes TAD-like boundaries through the control of H3K9ac distribution. (PNAS 2024)

- DOI: 10.1073/pnas.2400737121 | PMCID: PMC11252963 | PMID: 38968127
- Version used: **4.11**
- Evidence: Valid pairs were further used to identify interactions with HOMER (v 4.11) ( 56 ) for 1 kb resolution.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bismark v0.24.0, Bowtie2 v2.3.5] -> differential/statistical testing [BEDTools v2.28.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, R, deepTools v3.5.0]

### The m<sup>6</sup>A reader SlYTH2 negatively regulates tomato fruit aroma by impeding the translation process. (PNAS 2024)

- DOI: 10.1073/pnas.2405100121 | PMCID: PMC11253005 | PMID: 38950372
- Evidence: ( D ) Sequence motif identified within SlYTH2 & m 6 A targeted sites by HOMER software.
- Full pipeline: differential/statistical testing [R] -> stage not stated [HOMER]

### Class IIa HDAC4 and HDAC7 cooperatively regulate gene transcription in Th17 cell differentiation. (PNAS 2024)

- DOI: 10.1073/pnas.2312111121 | PMCID: PMC11067014 | PMID: 38657041
- Evidence: To gain the mechanistic insights into how Hdac4 activates gene transcription in Th17 cells, we conducted ChIP-seq of Hdac4 in Th17 cells, revealing enriched motifs, including Batf and AP-1 TFs Jun and Fos dimers, through HOMER (Hypergeometric Optimization of Motif EnRichment) analysis ( SI Appendix, Fig.
- Full pipeline: stage not stated [HOMER, MACS2]

### PML::RARA and GATA2 proteins interact via DNA templates to induce aberrant self-renewal in mouse and human hematopoietic cells. (PNAS 2024)

- DOI: 10.1073/pnas.2317690121 | PMCID: PMC11067031 | PMID: 38648485
- Evidence: ( E ) Motif enrichment at PML::RARA WT binding sites by HOMER analysis ( 34 ).
- Full pipeline: normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [HOMER]

### The Myc-associated zinc finger protein epigenetically controls expression of interferon-γ-stimulated genes by recruiting STAT1 to chromatin. (PNAS 2024)

- DOI: 10.1073/pnas.2320938121 | PMCID: PMC11046693 | PMID: 38635637
- Evidence: Subsequently, motif enrichment analysis was conducted using findMotifsGenome.pl from the HOMER package ( 25 ).
- Full pipeline: quality control [FastQC v0.11.9, fastp] -> alignment/mapping [Bowtie2] -> quantification [DESeq2 v1.32.0, R] -> normalisation [deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0, R] -> stage not stated [BEDTools, HOMER, MACS2 v2.2.7.1]

### Hepatocyte regeneration is driven by embryo-like DNA methylation reprogramming. (PNAS 2024)

- DOI: 10.1073/pnas.2314885121 | PMCID: PMC11032470 | PMID: 38588413
- Evidence: Motif analysis was carried out by HOMER with an RRBS background ( 31 ), which is available online at http://homer.ucsd.edu/homer .
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [HISAT2, STAR, TopHat v2.0.13, deepTools] -> quantification [Cufflinks] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, R v3.5.2, featureCounts]

### The neuroimmune CGRP-RAMP1 axis tunes cutaneous adaptive immunity to the microbiota. (PNAS 2024)

- DOI: 10.1073/pnas.2322574121 | PMCID: PMC10945812 | PMID: 38451947
- Evidence: Differential gene expression was calculated using HOMER’s getDiffExpression ( 72 ).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [HOMER, Metascape]

### CHD7 and SOX2 act in a common gene regulatory network during mammalian semicircular canal and cochlear development. (PNAS 2024)

- DOI: 10.1073/pnas.2311720121 | PMCID: PMC10927591 | PMID: 38408234
- Evidence: ( G ) Differential motif discovery using HOMER revealed known SOX2 ( P = 1 × 10 −7 ) and de novo SOX2 ( P = 1 × 10 −49 ) motifs using a nonspecific control CUT&Tag as background.
- Full pipeline: differential/statistical testing [HOMER]

### The GATA transcriptional program dictates cell fate equilibrium to establish the maternal-fetal exchange interface and fetal development. (PNAS 2024)

- DOI: 10.1073/pnas.2310502121 | PMCID: PMC10895349 | PMID: 38346193
- Evidence: HOMER motif analyses identified GATA motifs among most enriched motifs within both GATA2 and GATA3 binding regions ( SI Appendix , Fig.
- Full pipeline: dimensionality reduction/clustering [Seurat] -> stage not stated [HOMER]

### Coordination of rhythmic RNA synthesis and degradation orchestrates 24- and 12-h RNA expression patterns in mouse fibroblasts. (PNAS 2024)

- DOI: 10.1073/pnas.2314690121 | PMCID: PMC10873638 | PMID: 38315868
- Evidence: The remaining reads were then mapped to the mouse mm10 genome (GENECODE: GRCm38.p6.genome.fa), and read counts against gene (transcript per million or TPM), exon, and intron were independently quantified with HOMER (V4.11.1) ( 78 ) using gencode.vM25.annotation.gtf. using option condenseGenes.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HOMER, STAR v2.7.7a] -> quantification [HOMER] -> visualisation [SAMtools v1.11] -> stage not stated [DESeq2 v1.32.0, R]

### Streamlined identification of clinically and functionally relevant genetic regulators of lower-tract urogenital development. (PNAS 2024)

- DOI: 10.1073/pnas.2309466121 | PMCID: PMC10861909 | PMID: 38300866
- Evidence: HOMER ( https://homer.ucsd.edu/homer/ngs/ ) ( 75 ) was used to call and annotate SpDam peaks.
- Full pipeline: quantification [ImageJ, SAMtools] -> stage not stated [HOMER]

### Pharmacological modulation of RB1 activity mitigates resistance to neoadjuvant chemotherapy in locally advanced rectal cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2304619121 | PMCID: PMC10861914 | PMID: 38289962
- Evidence: Motif analysis of H3K27ac peaks in combination treatment using HOMER revealed that the TEAD motif was significantly enriched at H3K27ac peaks ( Fig.
- Full pipeline: stage not stated [GSEA, HOMER]

### Targeting the PHF8/YY1 axis suppresses cancer cell growth through modulation of ROS. (PNAS 2024)

- DOI: 10.1073/pnas.2219352120 | PMCID: PMC10786316 | PMID: 38165927
- Evidence: The P value is calculated using Fisher’s exact test in HOMER.
- Full pipeline: differential/statistical testing [HOMER]

### VGLL1 contributes to both the transcriptome and epigenome of the developing trophoblast compartment. (PNAS 2025)

- DOI: 10.1073/pnas.2508432122 | PMCID: PMC12685074 | PMID: 41284866
- Evidence: We performed Hypergeometric Optimization of Motif EnRichment (HOMER) analysis on common and day/treatment-specific regions to identify accessible TF binding motifs.
- Full pipeline: stage not stated [HOMER]

### Functional genetic elements of a butterfly mimicry supergene. (PNAS 2025)

- DOI: 10.1073/pnas.2509864122 | PMCID: PMC12541413 | PMID: 41060750
- Version used: **4.11**
- Evidence: Peak annotation and motif identification were performed using HOMER 4.11 ( 43 ).
- Full pipeline: stage not stated [Flye, HOMER v4.11, MACS2]

### Targeting the 3D genome by anthracyclines for chemotherapeutic effects. (PNAS 2025)

- DOI: 10.1073/pnas.2500704122 | PMCID: PMC12519215 | PMID: 41042842
- Evidence: ( D ) TF motif enrichment in lost TOP2A peaks from Acla- and Daun-treated K562 cells calculated by HOMER.
- Full pipeline: differential/statistical testing [DESeq2, limma] -> stage not stated [HOMER]

### ALKBH5 demethylates the m&lt;sup&gt;6&lt;/sup&gt;A modification of SOCS3 in microglia/macrophages and alleviates neuroinflammation after brain injury. (PNAS 2025)

- DOI: 10.1073/pnas.2504697122 | PMCID: PMC12501137 | PMID: 40986354
- Evidence: ( D ) Sequence motif was identified within m 6 A peaks by HOMER analysis.
- Full pipeline: stage not stated [HOMER]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Evidence: ( F ) TF motif enrichment analysis on differentially accessible elements by genotypes using HOMER.
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### Symbiosis with and mimicry of corals were facilitated by immune gene loss and body remodeling in the pygmy seahorse. (PNAS 2025)

- DOI: 10.1073/pnas.2423818122 | PMCID: PMC12415253 | PMID: 40854139
- Evidence: Differentially accessible peaks were annotated to the nearest gene using the “annotatePeaks.pl” HOMER script and motif enrichment calculated using the “findMotifsGenome.pl” script.
- Full pipeline: read trimming [Trimmomatic v0.26] -> alignment/mapping [Bowtie2, MAFFT v7.475, TopHat] -> differential/statistical testing [DESeq2, HOMER] -> stage not stated [BUSCO, ImageJ, InterProScan v5.15, OrthoFinder v2.2.7, RAxML v8.2.12, RepeatMasker, SAMtools, hifiasm]

### DNA polymerase β suppresses somatic indels at CpG dinucleotides in developing cortical neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2506846122 | PMCID: PMC12377747 | PMID: 40802685
- Evidence: Motif analysis for indel sites was performed with HOMER with its database of known transcription factor motifs ( 55 ).
- Full pipeline: alignment/mapping [BWA, GATK v4.1.0.0, Picard, SAMtools] -> variant calling [GATK v4.1.0.0, SAMtools] -> stage not stated [HOMER]

### Foxn3 is required to suppress aberrant ciliogenesis in nonphotoreceptor retinal neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2500871122 | PMCID: PMC12304973 | PMID: 40663603
- Evidence: Peak calling, identification of peak positions and distributions, and motif analysis were performed using the HOMER software suite ( http://homer.ucsd.edu/homer/index.html ) and deepTools ( 75 , 76 ).
- Full pipeline: alignment/mapping [HISAT2] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> stage not stated [HOMER, Seurat, deepTools, scDblFinder]

### WT1 directs normal progesterone receptor-chromatin binding essential for uterine receptivity at peri-implantation. (PNAS 2025)

- DOI: 10.1073/pnas.2504361122 | PMCID: PMC12280917 | PMID: 40627402
- Evidence: Motif enrichment analysis was performed using HOMER.
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [DESeq2, MACS2] -> stage not stated [HOMER, deepTools, ggplot2, pheatmap]

### TEAD-targeting small molecules induce a cofactor switch to regulate the Hippo pathway. (PNAS 2025)

- DOI: 10.1073/pnas.2425984122 | PMCID: PMC12260418 | PMID: 40608666
- Evidence: ( E ) De novo motif analysis by HOMER for regions bound by HA-tagged VGLL4.
- Full pipeline: stage not stated [GSEA, HOMER]

### Reactivation of an embryonic cardiac neural crest transcriptional profile during zebrafish heart regeneration. (PNAS 2025)

- DOI: 10.1073/pnas.2423697122 | PMCID: PMC12207451 | PMID: 40531881
- Evidence: HOMER ( 32 ) was used to discover de novo motifs in the regions of chromatin differentially accessible in the CdNC sample.
- Full pipeline: quality control [FastQC, Scanpy] -> read trimming [Bowtie2, Cutadapt v2.8] -> alignment/mapping [Bowtie2] -> quantification [ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP, scVelo, velocyto] -> differential/statistical testing [DESeq2, HOMER, featureCounts] -> stage not stated [R, SAMtools, WGCNA]

### Improving polygenic prediction from whole-genome sequencing data by leveraging predicted epigenomic features. (PNAS 2025)

- DOI: 10.1073/pnas.2419202122 | PMCID: PMC12184400 | PMID: 40504151
- Evidence: TF binding sites are derived using the motif scanning tool HOMER to scan along the reference genome and match the motifs of each TF.
- Full pipeline: alignment/mapping [HOMER] -> stage not stated [VCFtools]

### Ligand-specific regulation of a binary enhancer code dictating cellular senescence. (PNAS 2025)

- DOI: 10.1073/pnas.2506321122 | PMCID: PMC12184664 | PMID: 40493192
- Evidence: Aligned deep-seq reads were processed and analyzed using various programs in the HOMER software package ( 90 ), as detailed in SI Appendix , Extended Methods .
- Full pipeline: alignment/mapping [HOMER] -> stage not stated [GSEA, Metascape]

### Estrogen-related receptors regulate innate and adaptive muscle mitochondrial energetics through cooperative and distinct actions. (PNAS 2025)

- DOI: 10.1073/pnas.2426179122 | PMCID: PMC12107179 | PMID: 40354528
- Evidence: Only uniquely mapped tags were considered, and peak calling and motif analysis were performed with HOMER.
- Full pipeline: alignment/mapping [HOMER] -> visualisation [Metascape]

### The developmental factor TBX3 engages with the Wnt/β-catenin transcriptional complex in colorectal cancer to regulate metastasis genes. (PNAS 2025)

- DOI: 10.1073/pnas.2419691122 | PMCID: PMC12088458 | PMID: 40343989
- Evidence: ( D ) De novo motifs/consensus sequences discovered by HOMER in the TBX3 peaks [q(Benjamini–Hochberg) < 0.0001 for all motifs displayed].
- Full pipeline: stage not stated [AlphaFold, HOMER]

### Hdac1 as an early determinant of intermediate-exhausted CD8<sup>+</sup> T cell fate in chronic viral infection. (PNAS 2025)

- DOI: 10.1073/pnas.2502256122 | PMCID: PMC12088444 | PMID: 40333757
- Evidence: To further define Hdac1’s action, we performed de novo motif analysis of individual clusters of differential ChrAcc sites between WT and Hdac1 –/– T EX cells using HOMER, identifying ETS, RUNX, AP1, and NF-κB as top motifs across clusters, regardless of increase or decrease in ChrAcc ( Dataset S3 ).
- Full pipeline: variant calling [Monocle] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [HOMER] -> simulation/modelling [Monocle] -> visualisation [UMAP]

### Nonproteolytic ubiquitination regulates chromatin occupancy by the NCoR/SMRT/HDAC3 corepressor complex in MCF-7 breast cancer cells. (PNAS 2025)

- DOI: 10.1073/pnas.2502805122 | PMCID: PMC12067245 | PMID: 40305047
- Version used: **4.11**
- Evidence: Peak calling was performed using the function findPeaks of HOMER v4.11 with an option style parameter equal to histone ( 81 ).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2 v2.2.7, SAMtools v1.3] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, HOMER v4.11, R, RSEM]

### &lt;i&gt;NAT10&lt;/i&gt; exacerbates acute renal inflammation by enhancing N4-acetylcytidine modification of the CCL2/CXCL1 axis. (PNAS 2025)

- DOI: 10.1073/pnas.2418409122 | PMCID: PMC12054813 | PMID: 40261924
- Evidence: ( C ) The ac4C consensus motif in H/R-exposed cells with or without NAT10 knockdown was identified using HOMER.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [HOMER]

### Control of circadian muscle glucose metabolism through the BMAL1-HIF axis in obesity. (PNAS 2025)

- DOI: 10.1073/pnas.2424046122 | PMCID: PMC12002348 | PMID: 40127275
- Evidence: ( B ) HOMER Motif analysis on up- and downregulated DEGs in Bmal1 mKO mice.
- Full pipeline: normalisation [edgeR] -> stage not stated [HOMER]

### Pulsatile flow induces chromatin interaction with lamin-associated proteins to enrich H3K9 methylation in endothelial cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424566122 | PMCID: PMC11962468 | PMID: 40117319
- Evidence: Per-sample quality assessment plots were generated with HOMER and Mosaics.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> stage not stated [HOMER, ImageJ, MACS2, OpenCV]

### The SUbventral-Gland Regulator (SUGR-1) of nematode virulence. (PNAS 2025)

- DOI: 10.1073/pnas.2415861122 | PMCID: PMC11929438 | PMID: 40063806
- Evidence: Enriched motifs were identified using HOMER ( 88 ).
- Full pipeline: quality control [FastQC v0.11.9, HTSeq v0.12.4] -> read trimming [FastQC v0.11.9] -> alignment/mapping [STAR v2.7.9a] -> differential/statistical testing [DESeq2 v1.38.3] -> visualisation [AlphaFold] -> stage not stated [HOMER, ImageJ, R v4.2.1, ggplot2 v3.4.2]

### Dynamic changes in histone lysine lactylation during meiosis prophase I in mouse spermatogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2418693122 | PMCID: PMC11848400 | PMID: 39928879
- Evidence: Using HOMER, we identified transcription factor binding motifs enriched in the H4K8la peaks from our data.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, HOMER]

### BCL6 coordinates muscle mass homeostasis with nutritional states. (PNAS 2025)

- DOI: 10.1073/pnas.2408896122 | PMCID: PMC11789089 | PMID: 39841144
- Evidence: HOMER motif analysis identified a putative BCL6 binding motif (TTCCTGGAAAGC) in the promoter region of Socs2 ( Fig.
- Full pipeline: stage not stated [HOMER]

### Fasting primes small intestinal regeneration after damage via a microbiome-metabolite-chromatin axis. (PNAS 2026)

- DOI: 10.1073/pnas.2529215123 | PMCID: PMC13320697 | PMID: 42335240
- Evidence: ( G ) Motif enrichment analysis for enhancers unique to Fast (−Tetra) group using HOMER.
- Full pipeline: dimensionality reduction/clustering [MACS2 v2.2.9.1, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ArchR v1.0.2, GSEA, HOMER, R v1.0.2]

### Elevated MyoD1 levels expand genome-wide binding and the repertoire of regulated genes. (PNAS 2026)

- DOI: 10.1073/pnas.2605749123 | PMCID: PMC13291607 | PMID: 42301790
- Evidence: Motif enrichment analysis was performed using HOMER.
- Full pipeline: quantification [Fiji, ImageJ] -> differential/statistical testing [DESeq2, R] -> stage not stated [HOMER, Matplotlib, NumPy, OpenCV, PHENIX, Python, pheatmap]

### Differential Wnt/β-catenin signaling via TCF7L2/LEF1 binding specificity shapes cellular and tumor phenotypes. (PNAS 2026)

- DOI: 10.1073/pnas.2528450123 | PMCID: PMC13273282 | PMID: 42268900
- Evidence: Motif analysis was done using HOMER ( 60 ) (version 4.11) findMotifsGenome to find motifs in the hg38 genome using -size 200, and annotatePeaks for motif searching and identification.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> visualisation [deepTools] -> stage not stated [Enrichr, HOMER, MACS2, R v4.4, SAMtools, Seurat, Signac]

### ATP2B1 expression identifies human hematopoietic stem cells with superior repopulation and self-renewal. (PNAS 2026)

- DOI: 10.1073/pnas.2604380123 | PMCID: PMC13167729 | PMID: 42085155
- Evidence: HOMER ( http://homer.ucsd.edu/homer/motif/ ) was used to identify enriched motifs and GREAT (v.4.0.4, http://great.stanford.edu/public/html/ ) was used to predict the functions of cis -regulatory regions; details are in the SI Appendix .
- Full pipeline: stage not stated [GSEA, HOMER, ImageJ]

### Versatile SMAD2 and SMAD3 epitope-tagged mouse models for genomic profiling of TGFβ signaling: Uncovering GDF9-SMAD2/3 targets. (PNAS 2026)

- DOI: 10.1073/pnas.2600071123 | PMCID: PMC13056123 | PMID: 41911462
- Version used: **4.11**
- Evidence: Common peaks between replicates were identified with the “mergePeaks” function in HOMER v4.11 ( 89 ).
- Full pipeline: quality control [Bowtie2] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2, STAR v2.7.11b, featureCounts v2.1.1] -> quantification [STAR v2.7.11b] -> stage not stated [DESeq2 v1.48.2, HOMER v4.11, deepTools v2.4.2]

### KLF2 overrides the resident memory CD8 T cell differentiation program, in opposition to KLF3. (PNAS 2026)

- DOI: 10.1073/pnas.2533700123 | PMCID: PMC13037849 | PMID: 41871244
- Version used: **4.9.1**
- Evidence: Peaks were annotated using HOMER (v4.9.1), and heatmaps were generated with deepTools (v3.3.0).
- Full pipeline: quality control [FastQC v0.12.1, featureCounts v2.0.6] -> read trimming [FastQC v0.12.1, featureCounts v2.0.6] -> alignment/mapping [FastQC v0.12.1, featureCounts v2.0.6] -> differential/statistical testing [GSEA] -> stage not stated [HOMER v4.9.1, deepTools v3.3.0]

### Med14 phosphorylation shapes genomic response to GLP-1 agonists. (PNAS 2026)

- DOI: 10.1073/pnas.2536772123 | PMCID: PMC12974444 | PMID: 41779793
- Evidence: ChIPseq reads were aligned to the rn6 reference genome and analyzed for peak detection, read quantification, and motif enrichment using HOMER ( 55 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, Trim Galore] -> quantification [HOMER] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2]

### REV-ERB-alpha and -beta coordinately regulate astrocyte reactivity and proteostatic function. (PNAS 2026)

- DOI: 10.1073/pnas.2511093123 | PMCID: PMC12867698 | PMID: 41615759
- Evidence: Prediction were performed using four computational tools: MORA ( 29 ), HOMER ( 55 ), BART2 ( 56 ), and LISA2 ( 57 ).
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, ImageJ, R]

### Mechanical compression induces neuronal apoptosis, reduces synaptic activity, and promotes glial neuroinflammation in mice and humans. (PNAS 2026)

- DOI: 10.1073/pnas.2513172122 | PMCID: PMC12773780 | PMID: 41481451
- Version used: **5.1**
- Evidence: Motif enrichment analysis was performed using HOMER (v5.1) with the findMotifs module, scanning regions from 400 bp upstream to 100 bp downstream of the TSS.
- Full pipeline: alignment/mapping [STAR, featureCounts v2.0.1] -> normalisation [Seurat v5.2.1, limma v3.62.2] -> dimensionality reduction/clustering [Seurat v5.2.1, clusterProfiler, limma v3.62.2] -> stage not stated [Bioconductor, DESeq2 v1.46.0, GSEA, HOMER v5.1, ImageJ, Python, R, scikit-image v0.25.2]

### A prenylated dsRNA sensor protects against severe COVID-19. (Science 2021)

- DOI: 10.1126/science.abj3624 | PMCID: PMC7612834 | PMID: 34581622
- Evidence: Ungapped motif prediction was performed using both MEME ( 40 ) and HOMER ( 41 ) software, and the top predicted motif was selected for each.
- Full pipeline: quality control [MultiQC] -> read trimming [Cutadapt, SAMtools] -> alignment/mapping [BEDTools, MAFFT v7.453, SAMtools, STAR] -> quantification [BEDTools, MultiQC] -> differential/statistical testing [Bioconductor, R, SAMtools] -> stage not stated [BLAST, DESeq2, HMMER v3.2.1, HOMER]

### Mef2d potentiates type-2 immune responses and allergic lung inflammation. (Science 2024)

- DOI: 10.1126/science.adl0370 | PMCID: PMC7616247 | PMID: 38935708
- Evidence: HOMER ( 81 ) (v4.10.4) software was used for motif find analysis.
- Full pipeline: read trimming [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [BEDTools, HOMER, MACS2]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: HOMER was used to perform motif enrichment analysis ( 65 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

