# MACS2

- **Category:** genomics
- **Papers in survey:** 475
- **Journals:** PNAS (226), Nature (193), Cell (41), Science (15)
- **Years:** 2021 (44), 2022 (72), 2023 (100), 2024 (92), 2025 (109), 2026 (58)
- **Versions named:** 2.2.7.1 (27), 2.2.6 (11), 2.1.1.20160309 (10), 2.1.1 (8), 2.1.2 (7), 2.1.0 (6), 2.2.9.1 (6), 3.0.0b (3), 3.0.0a (3), 3.0.0 (3)
- **Pipeline stages it appears in:** alignment/mapping (32), differential/statistical testing (28), dimensionality reduction/clustering (9), read trimming (5), quantification (5), visualisation (5), machine learning (4), quality control (4), normalisation (3), registration (1), variant calling (1)

## Papers

### The interferon landscape along the respiratory tract impacts the severity of COVID-19. (Cell 2021)

- DOI: 10.1016/j.cell.2021.08.016 | PMCID: PMC8373821 | PMID: 34492226
- Evidence: Monocytes were positively selected from PBMCs with CD14 MicroBeads (Miltenyi Biotec Cat# 130-050-201) by MACS technology.
- Full pipeline: stage not stated [ComplexHeatmap, GSEA, MACS2]

### Polyamine metabolism is a central determinant of helper T cell lineage fidelity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.06.007 | PMCID: PMC8358979 | PMID: 34216540
- Evidence: ... Institute N/A DAVID Huang et al., 2009 N/A Trimmomatic Bolger et al., 2014 N/A Bowtie2 Langmead and Salzberg, 2012 N/A SAM tools Li et al., 2009 N/A MACS2 Zhang et al., 2008 N/A Bedtools Quinlan and Hall, 2010 N/A Resource availability Lead contact Further information and requests for resources and reagents should be directed and will be fulfilled by the lead contact, Erika L.
- Full pipeline: read trimming [Bowtie2, DESeq2, Galaxy, MACS2, Trimmomatic, deepTools, featureCounts] -> alignment/mapping [R, deepTools] -> quantification [R, deepTools] -> normalisation [R] -> dimensionality reduction/clustering [pheatmap] -> differential/statistical testing [R] -> visualisation [R]

### Integrated analysis of multimodal single-cell data. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.048 | PMCID: PMC8238499 | PMID: 34062119
- Evidence: We called peaks from the ATAC fragment files using the MACS2 callpeak function ( Zhang et al., 2008 ), and kept all peaks with -LOG10(qvalue) > 5 for the downstream ATAC analysis.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2, R, Seurat v3.2.0, Signac v1.0.0]

### A stony coral cell atlas illuminates the molecular and cellular basis of coral symbiosis, calcification, and immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.04.005 | PMCID: PMC8162421 | PMID: 33945788
- Evidence: ...x 20– outFilterMismatchNmax 5–alignIntronMax 3500 3 We used the resulting BAM alignment files to define genomic intervals with MARS-seq signal, using MACS2 ( Zhang et al., 2008 ) with parameters: -g 434000000–keep-dup 20-q 0.01–shift 1–extsize 20–broad–nomodel–min-length 30 4 We used the resulting stranded MARS-seq genomic intervals to elongate the 3' end of S . pistillata gene models, allowing a ...
- Full pipeline: read trimming [IQ-TREE, MAFFT] -> alignment/mapping [Bowtie2, DIAMOND, IQ-TREE, MACS2, MAFFT, edgeR, eggNOG] -> dimensionality reduction/clustering [SAMtools] -> structure determination [IQ-TREE, MAFFT] -> stage not stated [HMMER, R]

### Splice site m<sup>6</sup>A methylation prevents binding of U2AF35 to inhibit RNA splicing. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.062 | PMCID: PMC8208822 | PMID: 33930289
- Evidence: ...tor.org/packages/DESeq2 Bioconductor Huber et al., 2015 https://www.bioconductor.org/ Salmon Patro et al., 2017 https://combine-lab.github.io/salmon/ MACS2 Zhang et al., 2008 https://github.com/macs3-project/MACS MSPC Jalili et al., 2018 https://genometric.github.io/MSPC/ BLAST Altschul et al., 1990 http://blast.ncbi.nlm.nih.gov//blast.ncbi.nlm.nih.gov/Blast.cgi RNAfold Lorenz et al., 2011 https:/...
- Full pipeline: stage not stated [Bioconductor, Cutadapt, DESeq2, MACS2, R]

### TOP1 inhibition therapy protects against SARS-CoV-2-induced lethal inflammation. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.051 | PMCID: PMC8008343 | PMID: 33836156
- Version used: **2.1.0**
- Evidence: Peaks were called using MACS2 (version 2.1.0) ( https://github.com/macs3-project/MACS ) ( Zhang et al., 2008 ) with the control/input aligned reads as background (callpeak -g hs -q 0.01 –broad -c input/control).
- Full pipeline: read trimming [STAR] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.0, SAMtools v1.8, STAR] -> quantification [Bioconductor] -> dimensionality reduction/clustering [Cutadapt, clusterProfiler, limma, scikit-learn] -> differential/statistical testing [Bioconductor] -> stage not stated [BEDTools, DESeq2, GSEA, HOMER, R, Seurat, Trim Galore v0.4.2, featureCounts, fgsea, scDblFinder]

### SARS-CoV-2 evolution in an immunocompromised host reveals shared neutralization escape mechanisms. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.027 | PMCID: PMC7962548 | PMID: 33831372
- Evidence: ... Software https://www.graphpad.com:443/ ; RRID: SCR_002798 O v15.0 Jones et al., 1991 N/A Other anti-CD20 MicroBeads Miltenyi Biotec Cat# 130-091-104 MACS LS column Miltenyi Biotec Cat# 130-042-401 anti-FLAG M2 Affinity Gel Sigma-Aldrich Cat# A2220; RRID: AB_10063035 Protein G UltraLink Thermo Fisher Scientific Cat#: 53125 MabSelect SuRE Resin GE Healthcare Cat# 17547401 Streptavidin biosensor For...
- Full pipeline: stage not stated [MACS2, PHENIX v1.18.2, PyMOL]

### G3BPs tether the TSC complex to lysosomes and suppress mTORC1 signaling. (Cell 2021)

- DOI: 10.1016/j.cell.2020.12.024 | PMCID: PMC7868890 | PMID: 33497611
- Evidence: An LS MACS column was attached to a QuadroMACS magnet, equilibrated with 1 mL PBS and 0.5% BSA, and then washed with 1 mL PBS.
- Full pipeline: alignment/mapping [Clustal Omega] -> normalisation [CellProfiler, RSEM] -> visualisation [Clustal Omega] -> stage not stated [BCFtools, BLAST, ImageJ v1.50b, MACS2, Python, R, SAMtools, TrackMate]

### Genome-wide CRISPR Screens Reveal Host Factors Critical for SARS-CoV-2 Infection. (Cell 2021)

- DOI: 10.1016/j.cell.2020.10.028 | PMCID: PMC7574718 | PMID: 33147444
- Evidence: ...z et al., 2016 N/A Flowjo 10.6.2 FLOWJO https://www.flowjo.com Graphpad Prism 8 Graphpad software https://www.graphpad.com/scientific-software/prism/ MACS2 Zhang et al., 2008 N/A PoolQ version 3.2.9 Broad Institute https://portals.broadinstitute.org/gpp/public/software/poolq/ Picard Tools v2.9.0 Broad Institute http://broadinstitute.github.io/picard/ STAR aligner v2.7.3a Dobin et al., 2013 N/A SAM...
- Full pipeline: read trimming [Picard, STAR, Trimmomatic v0.39] -> alignment/mapping [MACS2, Picard, SAMtools, STAR, Trimmomatic v0.39] -> differential/statistical testing [R, featureCounts v1.6.2] -> stage not stated [BEDTools, Bowtie2 v2.2.9, Cutadapt, DESeq2 v1.32, deepTools v3.1.3]

### A human fetal lung cell atlas uncovers proximal-distal gradients of differentiation and key regulators of epithelial fates. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.005 | PMCID: PMC7618435 | PMID: 36493756
- Evidence: 106 https://github.com/macs3-project/MACS Space Ranger (version: 1.1.0) 10X genomics https://support.10xgenomics.com/spatial-gene-expression/software/pipelines/latest/what-is-space-ranger Seurat (version 3.2.2) Stuart et al.
- Full pipeline: quantification [velocyto] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> visualisation [R] -> stage not stated [ArchR, BLAST v2.12.0, CellPhoneDB, ComplexHeatmap v2.6.2, ImageJ, MACS2, Monocle, SCENIC, Scanpy, Seurat v3.2.2, SoupX, scDblFinder v0.2.1, scVelo, scikit-learn]

### mTOR-regulated mitochondrial metabolism limits mycobacterium-induced cytotoxicity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.018 | PMCID: PMC9596383 | PMID: 36103894
- Evidence: Single-cell suspensions were washed with MACS buffer (0.5% bovine serum albumin, 2mM EDTA in PBS, ph7.2) at 290 x g for 5 minutes at 4°C, and in most cases, fixed in 4% PFA solution overnight at 4°C.
- Full pipeline: stage not stated [ImageJ, MACS2]

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Version used: **2.0**
- Evidence: ...sponding pX459 sgRNAs see Table S1 This study N/A Software and algorithms CRISPR design https://www.benchling.com N/A R https://www.r-project.org N/A MACS2.0 https://github.com/taoliu/MACS N/A Bowtie2 Langmead and Salzberg, 2012 N/A Samtools http://samtools.sourceforge.net N/A HiCUP v0.8.1 Wingett et al., 2015 N/A Cooltools https://zenodo.org/record/5214125 N/A Juicer Durand et al., 2016 N/A Genri...
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### Mobilization-based chemotherapy-free engraftment of gene-edited human hematopoietic stem cells. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.039 | PMCID: PMC9240327 | PMID: 35617958
- Evidence: 5×10 4 - 2×10 5 cells (from culture or mouse samples) were harvested, washed with PBS or MACS buffer (PBS pH 7.2, 0.5% BSA, 2mM EDTA), treated with fragment crystallizable (Fc) Receptor-Block (Miltenyi Biotec), when antibody stained, and then re-suspended in the buffer used for washing.
- Full pipeline: differential/statistical testing [R v3.5] -> stage not stated [MACS2]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: We performed peak calling using MACS2 with the addReproduciblePeakSet (ArchR) function using pseudo-bulk replicates.
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Version used: **2.1.1.20160309**
- Evidence: ...abraham Bioinformatics, https://www.bioinformatics.babraham.ac.uk version 0.11.9 Samtools Genome Research Limited, http://www.htslib.org version 1.14 MACS2 https://github.com/macs3-project/MACS version 2.1.1.20160309 Recombinant Identification Program Los Alamos National Laboratory, https://www.hiv.lanl.gov/content/sequence/RIP/RIP.html Bowtie2 http://bowtie-bio.sourceforge.net/bowtie2/index.shtml...
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### Complement activation induces excessive T cell cytotoxicity in severe COVID-19. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.040 | PMCID: PMC8712270 | PMID: 35032429
- Evidence: ...r Cell Lysis Thermo Fisher Scientific Cat# 88701 DPBS Gibco, Thermo Fisher Scientific Cat# 14190-094 Bovine Albumin Fraction V (BSA) Serva Cat# 11930 MACS BSA Stock solution Miltenyi Biotec Cat# 130-091-376 EDTA Sigma Cat# E5134-100G IL-2 (Proleukin S) Novartis Cat# 02238131 h-C3a Almac Cat# CN-91 Beriglobin CSL Behring PZN 4616123 Anti-Biotin MACSiBead Particles Miltenyi Biotec Cat# 130-092-357 S...
- Full pipeline: normalisation [DESeq2] -> dimensionality reduction/clustering [Bioconductor, UMAP] -> differential/statistical testing [GSEA] -> visualisation [ggplot2, pheatmap] -> stage not stated [ComplexHeatmap, Cutadapt, Cytoscape, MACS2, R, Seurat, fgsea, lme4]

### Super-enhancers include classical enhancers and facilitators to fully activate gene expression. (Cell 2023)

- DOI: 10.1016/j.cell.2023.11.030 | PMCID: PMC10858684 | PMID: 38101409
- Evidence: After supernatant removal, cells were incubated with MACS anti-FITC separation microbeads (Miltenyli; 10 μL per 107 cells) in ice-cold separation buffer (PBS plus 0.5% bovine serum albumin (BSA) and 2 mM EDTA; 90 μL per 107 cells) for 15 min at 4°C, rolling, and washed by adding separation buffer (1 mL per 10 7 cells) and spinning.
- Full pipeline: quality control [Bowtie2] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt] -> registration [Cutadapt] -> differential/statistical testing [Bioconductor, DESeq2, edgeR] -> stage not stated [BEDTools, MACS2, R, SAMtools, deepTools, ggplot2]

### Human MCTS1-dependent translation of JAK2 is essential for IFN-γ immunity to mycobacteria. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.024 | PMCID: PMC10841658 | PMID: 37875108
- Evidence: The cells were cultured for three to four days, assayed for transgene expression by FACS staining for ΔNGFR, and subjected to enrichment for MACS sorting.
- Full pipeline: quality control [STAR v2.6.1d] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, GATK, STAR v2.6.1d] -> variant calling [GATK] -> quantification [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Cutadapt, DESeq2] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, SnpEff, fgsea]

### Mechanopathology of biofilm-like Mycobacterium tuberculosis cords. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.016 | PMCID: PMC10642369 | PMID: 37865090
- Evidence: ... =0.034 inches Cole-Parmer Cat#:95809-26 5-μm syringe filter Millipore Cat#: SLSV025LS BioGen Pro 200 Homogenizer Pro Scientific Cat#: 01-01200 gentleMACS TM Octo Dissociator with Heaters Miltenyi Biosciences Cat#: 130-096-427 LS Columns Miltenyi Biosciences Cat#: 130-042-401 MACS Multistand Miltenyi Biosciences Cat#: 130-042-303 Precellys 24 Tissue Homogenizer Bertin Instruments Cat#: P000669-PR2...
- Full pipeline: quality control [Bioconductor, FastQC, GSEA, STAR v2.7.10b] -> alignment/mapping [STAR v2.7.10b] -> quantification [R, edgeR] -> stage not stated [ImageJ, MACS2]

### Molecular basis of anaphylatoxin binding, activation, and signaling bias at complement receptors. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.020 | PMCID: PMC7615941 | PMID: 37852260
- Evidence: Monocytes were isolated using Lymphoprep density centrifugation (STEMCELL, Melbourne, Australia) followed by CD14 + MACS magnetic bead separation (Miltenyi Biotec, Sydney, Australia).
- Full pipeline: stage not stated [ChimeraX, MACS2, PHENIX, RELION v3.1.2, UCSF Chimera]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Evidence: 83 http://samtools.sourceforge.net/ Bedtools Quinlan and Hall 84 https://github.com/arq5x/bedtools2/blob/master/docs/content/overview.rst MACS2 Zhang et al.
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **2.2.7.1**
- Evidence: 87 https://github.com/alexdobin/STAR MACS2 2.2.7.1 Zhang et al.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### DNA hypomethylation silences anti-tumor immune genes in early prostate cancer and CTCs. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.028 | PMCID: PMC10436379 | PMID: 37327786
- Version used: **2.0.10**
- Evidence: MACS2 (v2.0.10) 76 was used to call the peaks and deepTools 77 were used to compute the ChIP-seq or Cut and Run signal around prostate PMDs.
- Full pipeline: read trimming [BWA, Bismark, Trim Galore v0.4.3] -> alignment/mapping [BWA, Bismark, TopHat] -> quantification [ImageJ, SAMtools v1.3.1] -> differential/statistical testing [R v3.1.2] -> stage not stated [Bioconductor, GSEA, MACS2 v2.0.10, deepTools]

### Biofilm formation on human immune cells is a multicellular predation strategy of Vibrio cholerae. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.008 | PMCID: PMC10256282 | PMID: 37295405
- Evidence: 07801) and were further separated into monocytes, CD4 + T cells, B cells, as well as NK cells with the help of Milteny MACS MicroBeads (CD14, CD4, CD19, CD56) according to the manufacturer’s protocol.
- Full pipeline: stage not stated [MACS2]

### A tissue injury sensing and repair pathway distinct from host pathogen defense. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.031 | PMCID: PMC10321318 | PMID: 37098344
- Evidence: 99 Peak calls for each replicate were made with MACS2 software in BAMPE mode.
- Full pipeline: read trimming [Bowtie2 v2.2.9, Picard] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.9, Picard, RAxML] -> quantification [deepTools v3.1.2] -> normalisation [deepTools v3.1.2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, HMMER, HOMER v4.10, ImageJ, MACS2, R v4.0, SAMtools v1.3.1, Seurat v3.0.0]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Evidence: Genomic regions with high levels of transposition/tagging events were then determined using the MACS2 peak calling algorithm.
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### Recycling of modified H2A-H2B provides short-term memory of chromatin states. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.007 | PMCID: PMC9994263 | PMID: 36750094
- Version used: **2.2.6**
- Evidence: Broad Institute https://github.com/broadinstitute/picard/releases/tag/2.27.3 MACS2 v2.2.6 Zhang et al.
- Full pipeline: stage not stated [BEDTools v2.30.0, Bioconductor, Bowtie2 v2.4.2, ImageJ v1.53k, MACS2 v2.2.6, Picard, R v4.1, SAMtools v1.12, Trim Galore, deepTools v3.5.1]

### SARS-CoV-2 replication in airway epithelia requires motile cilia and microvillar reprogramming. (Cell 2023)

- DOI: 10.1016/j.cell.2022.11.030 | PMCID: PMC9715480 | PMID: 36580912
- Evidence: Lungs were weighted and homogenized in 1 mL of 2% FBS MEM medium with gentle MACS - C tubes (Miltenyi Biotec Catalog# 130-093-237).
- Full pipeline: normalisation [Bioconductor] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [Bioconductor, GSEA] -> stage not stated [ImageJ, MACS2, R]

### A replisome-associated histone H3-H4 chaperone required for epigenetic inheritance. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.006 | PMCID: PMC11380579 | PMID: 39094570
- Evidence: ...59 AcquireMP Refeyn, Ltd N/A DiscoverMP Refeyn, Ltd N/A ASTRA, version 7.3.2.21 Wyatt RRID:SCR_016255 Bowtie2 John Hopkins University RRID:SCR_016368 MACS Dana Farber Cancer Institute RRID:SCR_013291 DANPOS Baylor College of Medicine RRID:SCR_015527 Other MagNA Lyser Instrument Roche Cat# 3358968001 QuantStudio ™ 7 Flex Real-Time PCR System, 384-well, desktop Applied Bioystems Cat# 4485701 6875 Fr...
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> dimensionality reduction/clustering [ChimeraX, Clustal Omega, ColabFold, UCSF Chimera] -> stage not stated [AlphaFold, Bowtie2, MACS2]

### The fork protection complex promotes parental histone recycling and epigenetic memory. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.017 | PMCID: PMC11383432 | PMID: 39094569
- Evidence: 113 http://www.htslib.org/ MACS2 v Zhang et al.
- Full pipeline: differential/statistical testing [R v4.2.2] -> visualisation [PyMOL v1.2r, ggpubr v0.6.0] -> stage not stated [AlphaFold, Bowtie2 v2.4.2, ChimeraX, MACS2, SAMtools v1.12, deepTools]

### Evolution of diapause in the African turquoise killifish by remodeling the ancient gene regulatory landscape. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.048 | PMCID: PMC11970524 | PMID: 38810644
- Evidence: 109 https://deeptools.readthedocs.io/en/develop/ MACS2 Zhang et al.
- Full pipeline: quality control [DESeq2, FastQC v0.11.9, MultiQC v1.8, STAR v2.7.1a] -> quantification [featureCounts] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [GSEA, edgeR v4.0.16] -> machine learning [edgeR v4.0.16] -> visualisation [R v3.6] -> stage not stated [BLAST v2.7.1, Bowtie2, HOMER v4.10, MACS2, OrthoFinder v2.5.4, Picard, RepeatMasker v4.0, SAMtools v1.5, Trim Galore v0.4.1, deepTools v3.2.1]

### Selection of epigenetically privileged HIV-1 proviruses during treatment with panobinostat and interferon-α2a. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.037 | PMCID: PMC10903630 | PMID: 38367616
- Evidence: 12 Millipore Sigma/IDT/Qiagen N/A Software and algorithms BD FACS Diva BD Biosciences N/A MACS2 Zhang et al.
- Full pipeline: quality control [BWA, FastQC v0.11.9, R, RepeatMasker] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, RSEM v1.2.22, STAR, Trimmomatic] -> differential/statistical testing [FastQC v0.11.9, R, RepeatMasker] -> stage not stated [DESeq2, MACS2, Python]

### Human inherited CCR2 deficiency underlies progressive polycystic lung disease. (Cell 2024)

- DOI: 10.1016/j.cell.2023.11.036 | PMCID: PMC10842692 | PMID: 38157855
- Evidence: Cells were filtered with a 70 μm MACS SmartStrainer (#130–098-462, Miltenyi) to remove large debris, washed three times with PBS plus 0.5% FBS, and finally filtered with a 40 μm Falcon Cell Strainer (#352340, Corning).
- Full pipeline: quality control [STAR v2.6.1d] -> alignment/mapping [STAR v2.6.1d, Seurat] -> quantification [ComplexHeatmap] -> normalisation [ComplexHeatmap, R] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> simulation/modelling [ImageJ, TrackMate] -> stage not stated [MACS2, ggplot2, scDblFinder]

### Mapping chromatin structure at base-pair resolution unveils a unified model of cis-regulatory element interactions. (Cell 2025)

- DOI: 10.1016/j.cell.2025.10.013 | PMCID: PMC7618578 | PMID: 41197626
- Evidence: Murine erythroid cells were purified using Ter119 selection (ter119-phycoerythrin antibodies (Biolegend 116208) and anti-PE MACS beads (Miltenyi, 130-048-801)) from the spleen of C57BL/6J adult mice including both sexes following administration of phenylyhydrazine (40 mg/g body weight, 3 doses, 12 h apart).
- Full pipeline: read trimming [Trim Galore] -> quantification [Snakemake] -> differential/statistical testing [Snakemake] -> structure determination [Trim Galore] -> stage not stated [BEDTools, Bowtie2, DESeq2, LAMMPS, MACS2]

### CRATER tumor niches facilitate CD8&lt;sup&gt;+&lt;/sup&gt; T cell engagement and correspond with immunotherapy success. (Cell 2025)

- DOI: 10.1016/j.cell.2025.09.021 | PMCID: PMC12604482 | PMID: 41109214
- Version used: **2.1.0**
- Evidence: We used the MACS2 version 2.1.0 54 peak finding algorithm to identify regions of ATAC-Seq peaks, with the following parameter –nomodel –shift −100 –extsize 200.
- Full pipeline: quality control [Cutadapt, FastQC] -> alignment/mapping [Bowtie2 v2.2.1, STAR v2.7.0] -> quantification [Cufflinks v2.2.1] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [Cufflinks v2.2.1, SciPy, scikit-learn, seaborn] -> visualisation [scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2 v2.1.0, Python, QuPath, R v4.0, Seurat v4.0.2]

### Single-cell multiregion epigenomic rewiring in Alzheimer's disease progression and cognitive resilience. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.031 | PMCID: PMC12573303 | PMID: 40752494
- Version used: **2.2.6**
- Evidence: Identification of cCREs and cCRE-gene pairs across cell types To identify cCREs across 67 cell subtypes, we utilized ArchR (v.1.0.2) functions addGroupCoverages and addReproduciblePeakSet to call accessible chromatin peaks using MACS2 (v.2.2.6).
- Full pipeline: quality control [Scanpy v1.9.3] -> alignment/mapping [Seurat v4.4.0] -> normalisation [Scanpy v1.9.3] -> dimensionality reduction/clustering [ArchR, ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP] -> differential/statistical testing [LDSC v1.0.1, ggpubr, pheatmap] -> visualisation [ComplexHeatmap v2.14.0, Cytoscape, Scanpy v1.9.3, UMAP, pheatmap] -> stage not stated [AnnData, BEDTools v2.30.0, Enrichr, MACS2 v2.2.6, Python, R, deepTools, scikit-learn]

### In vivo prime editing rescues alternating hemiplegia of childhood in mice. (Cell 2025)

- DOI: 10.1016/j.cell.2025.06.038 | PMCID: PMC12702498 | PMID: 40695277
- Evidence: Once the program was complete, homogenate was passed through a 100 μm MACS SmartStrainer into a 15mL falcon tube and 2 mL of additional complete Nuclei Extraction buffer was added to the strained homogenate’s volume.
- Full pipeline: read trimming [Bowtie2, SAMtools] -> alignment/mapping [Bowtie2, SAMtools] -> quantification [Bowtie2] -> machine learning [MACS2]

### Serotonin transporter inhibits antitumor immunity through regulating the intratumoral serotonin axis. (Cell 2025)

- DOI: 10.1016/j.cell.2025.04.032 | PMCID: PMC12255530 | PMID: 40403728
- Evidence: In vitro OT1 T cell culture Spleen and lymph node cells were harvested from the OT1 -Tg or OT1 -Tg/ Sert -KO mice and then subjected to MACS sorting using a Mouse CD8 T Cell Isolation Kit (catalog no.
- Full pipeline: quantification [R, Seurat v4.0.0] -> dimensionality reduction/clustering [GSEA, R, Seurat v4.0.0, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2, velocyto]

### Transcriptional regulation by PHGDH drives amyloid pathology in Alzheimer's disease. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.045 | PMCID: PMC12204802 | PMID: 40273909
- Evidence: MACS2 was used to identify peaks of each ChIP-seq sample using IgG as background with parameters ‘–nomodel -q 0.1’.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [Bowtie2, SAMtools, fastp] -> quantification [Bowtie2, fastp] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bowtie2, fastp] -> visualisation [R] -> stage not stated [AlphaFold, HOMER v4.11, MACS2, Seurat, deepTools]

### HIF regulates multiple translated endogenous retroviruses: Implications for cancer immunotherapy. (Cell 2025)

- DOI: 10.1016/j.cell.2025.01.046 | PMCID: PMC11988688 | PMID: 40023154
- Version used: **2.1.1.20160309**
- Evidence: These reads were used to generate binding sites with Model-Based Analysis of ChIP-seq 2 (MACS v2.1.1.20160309), with a q -value (FDR) threshold of 0.01 105 .
- Full pipeline: read trimming [Cutadapt v1.14] -> alignment/mapping [Bowtie2 v2.3.4.3, SAMtools v1.3.1] -> variant calling [Mutect2, Strelka] -> quantification [HTSeq v0.11.0] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [ImageJ, MACS2 v2.1.1.20160309, R] -> stage not stated [BEDTools, Picard, Seurat v5.1.0, Signac v1.13.0, scDblFinder v1.18.0]

### Inflammation switches the chemoattractant requirements for naive lymphocyte entry into lymph nodes. (Cell 2025)

- DOI: 10.1016/j.cell.2024.11.031 | PMCID: PMC11845304 | PMID: 39708807
- Version used: **1.4.2**
- Evidence: Regions of open chromatin were identified by MACS (version 1.4.2) 64 using a p-value threshold of 1×10 −5 .
- Full pipeline: alignment/mapping [Python] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2 v1.4.2, Metascape] -> visualisation [UMAP] -> stage not stated [R v4.2.1, Seurat v4.3.0, deepTools v3.5.4]

### An atlas of gene regulatory elements in adult mouse cerebrum. (Nature 2021)

- DOI: 10.1038/s41586-021-03604-1 | PMCID: PMC8494637 | PMID: 34616068
- Evidence: Peaks were called using MACS2 scores for aggregate accessibility profiles on each sample.
- Full pipeline: quality control [R] -> alignment/mapping [R] -> dimensionality reduction/clustering [BEDTools, HOMER, UMAP, scikit-learn] -> differential/statistical testing [HOMER, Monocle v0.2.2] -> stage not stated [Enrichr, MACS2, SAIGE, Seurat v3.0, scDblFinder]

### A transcriptomic and epigenomic cell atlas of the mouse primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03500-8 | PMCID: PMC8494649 | PMID: 34616066
- Evidence: Peak calling was performed on the Tn5-corrected single-base insertions using MACS2 63 (RRID: SCR_013291) with parameters: –shift −75–extsize 150–nomodel–call-summits–SPMR–keep-dup all −q 0.01.
- Full pipeline: alignment/mapping [Bismark, STAR v2.5.3, Seurat] -> normalisation [deepTools] -> dimensionality reduction/clustering [R, Scanpy, UMAP] -> stage not stated [BEDTools, MACS2, scDblFinder]

### Single-cell epigenomics reveals mechanisms of human cortical development. (Nature 2021)

- DOI: 10.1038/s41586-021-03209-8 | PMCID: PMC8494642 | PMID: 34616060
- Evidence: Peak calling Fragments from cells were grouped together by broad cell class (RG, IPC, ulEN, dlEN, endo/mural, astro/oligo, nEN, IN-MGE, IN-CGE, MGE progenitor, insular, microglia) and peaks were called on all cluster fragments using MACS2 ( https://github.com/taoliu/MACS ) with the parameters ‘--nomodel --shift -37 --ext 73 --qval 5e-2 -B --SPMR --call-summits’.
- Full pipeline: normalisation [Seurat] -> dimensionality reduction/clustering [MACS2, UMAP, deepTools] -> differential/statistical testing [LDSC v1.0.1] -> visualisation [UMAP, deepTools] -> stage not stated [BEDTools v2.24.0, GATK v3.8, HOMER, ImageJ, Monocle, R, Strelka, WGCNA, freebayes, scDblFinder]

### A multimodal cell census and atlas of the mammalian primary motor cortex. (Nature 2021)

- DOI: 10.1038/s41586-021-03950-0 | PMCID: PMC8494634 | PMID: 34616075
- Evidence: Identification of cCREs For peak calling in the snATAC-seq data, we extracted all the fragments for each cluster, and then performed peak calling on each aggregate profile using MACS2 81 v2.2.7.1. using Python 3.6 with parameter: “--nomodel --shift −100 --ext 200 --qval 1e-2 –B --SPMR”.
- Full pipeline: normalisation [Scanpy] -> dimensionality reduction/clustering [DESeq2 v1.30.0, MACS2, Python v3.6, UMAP, scikit-learn v0.24.2] -> differential/statistical testing [DESeq2 v1.30.0, HOMER] -> visualisation [UMAP] -> stage not stated [R v3.5.3, Seurat, ggplot2 v3.2.1]

### Comparative cellular analysis of motor cortex in human, marmoset and mouse. (Nature 2021)

- DOI: 10.1038/s41586-021-03465-8 | PMCID: PMC8494640 | PMID: 34616062
- Version used: **2.1.2**
- Evidence: Peaks were called using MACS2 v2.1.2 software ( https://github.com/taoliu/MACS ) using the runMACS function in SnapATAC and with the following options ‘–nomodel–shift 100–ext 200–qval 5e-2 –B–SPMR’.
- Full pipeline: alignment/mapping [SAMtools v1.9, STAR v2.7.3a, igraph v1.2.6] -> quantification [R, RSEM v1.3.3] -> dimensionality reduction/clustering [Seurat v3.1.1, UMAP, igraph v1.2.6, limma v3.38.3, scikit-learn v0.21.3] -> visualisation [UMAP, ggplot2 v3.3.2] -> stage not stated [ImageJ v1.52p, MACS2 v2.1.2, Scanpy v1.4.4, Signac v0.1.4, deepTools v3.4.2, edgeR v3.28.1]

### Cells of the human intestinal tract mapped across space and time. (Nature 2021)

- DOI: 10.1038/s41586-021-03852-1 | PMCID: PMC8426186 | PMID: 34497389
- Evidence: All gut region samples (except mLN) proceeded to MACS enrichment.
- Full pipeline: quality control [NumPy v0.25.2, pandas v1.1.2] -> alignment/mapping [STAR] -> quantification [R v0.99.8] -> normalisation [CellPhoneDB v2.0] -> dimensionality reduction/clustering [UMAP, clusterProfiler v3.18.1, scVelo] -> differential/statistical testing [R v0.99.8, limma] -> simulation/modelling [Scanpy v1.5.1] -> visualisation [seaborn] -> stage not stated [MACS2, PHENIX, SoupX, lme4, scDblFinder v0.2.1]

### Rewiring of the ubiquitinated proteome determines ageing in C. elegans. (Nature 2021)

- DOI: 10.1038/s41586-021-03781-z | PMCID: PMC8357631 | PMID: 34321666
- Evidence: Then, samples were incubated with 50 μl of μMACS MicroBeads (Miltenyi Biotec, 130-071-001) for 1 h on the overhead shaker at 4 °C.
- Full pipeline: quantification [ImageJ] -> stage not stated [MACS2]

### Rapid and stable mobilization of CD8<sup>+</sup> T cells by SARS-CoV-2 mRNA vaccine. (Nature 2021)

- DOI: 10.1038/s41586-021-03841-4 | PMCID: PMC8426185 | PMID: 34320609
- Evidence: Enrichment was then performed using anti-PE beads with MACS technology (Miltenyi Biotec) according to the manufacturer’s instructions.
- Full pipeline: alignment/mapping [Clustal Omega v1.2.2] -> dimensionality reduction/clustering [Bioconductor, R v4.0.2] -> stage not stated [MACS2]

### HP1 drives de novo 3D genome reorganization in early Drosophila embryos. (Nature 2021)

- DOI: 10.1038/s41586-021-03460-z | PMCID: PMC8116211 | PMID: 33854237
- Evidence: Supplementary Table 5 HP1 peaks called with MACS2 using the broad peaks option before cycle 9.
- Full pipeline: stage not stated [MACS2, RepeatMasker]

### Structural basis of malaria RIFIN binding by LILRB1-containing antibodies. (Nature 2021)

- DOI: 10.1038/s41586-021-03378-6 | PMCID: PMC8068667 | PMID: 33790470
- Evidence: Identification of target antigens by LC-MS/MS MDB1 + 3D7 IEs cultures that have reached to late trophozoite stage at >5% parasitemia were enriched using MACS magnetic beads to avoid early-stage parasites.
- Full pipeline: differential/statistical testing [R] -> structure determination [PHENIX] -> visualisation [ChimeraX, PyMOL] -> stage not stated [MACS2, UCSF Chimera]

### Loop extrusion as a mechanism for formation of DNA damage repair foci. (Nature 2021)

- DOI: 10.1038/s41586-021-03193-z | PMCID: PMC7116834 | PMID: 33597753
- Evidence: SCC1 and CTCF Peaks were identified using MACS2 program with callpeak algorithm, with default setting, using Input as control and the SCC1 ChIP-seq data before break induction as sample.
- Full pipeline: read trimming [R, SAMtools] -> alignment/mapping [R, SAMtools] -> normalisation [Bioconductor, deepTools] -> differential/statistical testing [deepTools] -> visualisation [Bioconductor] -> stage not stated [MACS2, ggplot2]

### Regulatory genomic circuitry of human disease loci by integrative epigenomics. (Nature 2021)

- DOI: 10.1038/s41586-020-03145-z | PMCID: PMC7875769 | PMID: 33536621
- Evidence: We generated −log 10 P value signal tracks against matched whole cell extracts for both the ChIP–seq and the accessibility datasets using the MACS2 49 and the SPP 48 peak caller and cross-correlation analysis to identify the proper fragment length as in the Roadmap analysis.
- Full pipeline: alignment/mapping [BWA] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [MACS2] -> machine learning [XGBoost] -> visualisation [R]

### A gene-environment-induced epigenetic program initiates tumorigenesis. (Nature 2021)

- DOI: 10.1038/s41586-020-03147-x | PMCID: PMC8482641 | PMID: 33536616
- Evidence: Peaks were called over input using MACS2 51 , and only peaks with a p-value of <=0.001 and outside the ENCODE blacklist region were kept.
- Full pipeline: read trimming [Bowtie2, Cutadapt, Trimmomatic] -> alignment/mapping [Bowtie2, Cutadapt, Trimmomatic, featureCounts] -> quantification [featureCounts] -> normalisation [BEDTools, DESeq2, pheatmap, seaborn] -> dimensionality reduction/clustering [ComplexHeatmap, HOMER, UMAP, seaborn] -> differential/statistical testing [MACS2, Trimmomatic, limma] -> visualisation [ComplexHeatmap, R, Trimmomatic, UMAP, pheatmap, seaborn] -> stage not stated [GSEA, deepTools]

### Elevated NSD3 histone methylation activity drives squamous cell lung cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03170-y | PMCID: PMC7895461 | PMID: 33536620
- Evidence: Contaminating human or mouse hematopoietic and endothelial cells (CD45, Ter119, CD31) are depleted using biotin conjugated anti-mouse CD45, CD31 and Ter119 antibodies and separated on a MACS LS column using anti biotin microbeads.
- Full pipeline: quality control [MACS2] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, HISAT2, Trimmomatic] -> normalisation [RSEM] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, ImageJ, Picard, featureCounts v2.0.0]

### Circuits between infected macrophages and T cells in SARS-CoV-2 pneumonia. (Nature 2021)

- DOI: 10.1038/s41586-020-03148-w | PMCID: PMC7987233 | PMID: 33429418
- Evidence: Lysis was stopped by adding 13 ml of MACS buffer (Miltenyi Biotech).
- Full pipeline: alignment/mapping [STAR v2.6.1d] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP, pheatmap v1.0.12] -> differential/statistical testing [DESeq2 v1.26.0, Python v3.6, R v3.6.3, tidyverse v1.3.0] -> visualisation [ggplot2 v3.3.1, pheatmap v1.0.12] -> stage not stated [MACS2, Matplotlib v3.2.1, Nextflow v19.10.0, Scanpy v1.5.1, SciPy, Singularity v3.2.1, WGCNA, featureCounts v1.6.4, statsmodels]

### Decoding myofibroblast origins in human kidney fibrosis. (Nature 2021)

- DOI: 10.1038/s41586-020-2941-1 | PMCID: PMC7611626 | PMID: 33176333
- Evidence: Tissues were sliced into approximately 0.5-1mm 3 pieces and transferred to a C-tube (Miltenyi Biotec) and processed on a gentle-MACS (Miltenyi Biotec) using the program spleen 4.
- Full pipeline: alignment/mapping [STAR v2.7.0e] -> normalisation [CellPhoneDB v2.1.1] -> dimensionality reduction/clustering [R, Seurat, Slingshot, UMAP, clusterProfiler, igraph] -> simulation/modelling [Slingshot] -> stage not stated [BEDTools v2.17.0, ComplexHeatmap, GSEA, ImageJ, MACS2, Picard, QuPath, SAMtools v1.3.1, fgsea]

### Ras drives malignancy through stem cell crosstalk with the microenvironment. (Nature 2022)

- DOI: 10.1038/s41586-022-05475-6 | PMCID: PMC9750880 | PMID: 36450983
- Version used: **2.1.1**
- Evidence: Peaks were called using MACS2 (v.2.1.1) with the default settings 61 .
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, Picard v2.3.0, STAR v2.6, Salmon v1.4.0] -> quantification [R v3.6.1, RSEM v1.2.30] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Matplotlib, NumPy, SciPy, scikit-learn] -> stage not stated [HOMER, MACS2 v2.1.1, Seurat v3.1.1, pheatmap v1.0.12]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Version used: **2.21**
- Evidence: Peak detection in ATAC peak-calling analysis Peaks were called separately for each tumour region using MACS2 v2.21 (ref.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### SARS-CoV-2 disrupts host epigenetic regulation via histone mimicry. (Nature 2022)

- DOI: 10.1038/s41586-022-05282-z | PMCID: PMC9533993 | PMID: 36198800
- Version used: **2.1.1.20160309**
- Evidence: Peaks were called using MACS2 (v2.1.1.20160309) 54 with the options ‘--call-summits --nomodel --B’.
- Full pipeline: alignment/mapping [Bowtie2 v2.1.0, STAR v2.6.1a] -> normalisation [DESeq2, R] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> stage not stated [BEDTools v2.18.1, ImageJ, MACS2 v2.1.1.20160309, SAMtools v1.9, featureCounts v1.6.2]

### PD-1-cis IL-2R agonism yields better effectors from stem-like CD8<sup>+</sup> T cells. (Nature 2022)

- DOI: 10.1038/s41586-022-05192-0 | PMCID: PMC9534752 | PMID: 36171284
- Evidence: Tumour tissue was transferred to PBS and was disrupted using manual scissors and the Miltenyi Gentle MACS machine.
- Full pipeline: alignment/mapping [HISAT2 v2.1.0] -> quantification [featureCounts] -> normalisation [UMAP] -> dimensionality reduction/clustering [Jupyter, UMAP] -> visualisation [ComplexHeatmap, Jupyter, R, UMAP] -> stage not stated [DESeq2, MACS2, Python, Scanpy]

### Novel antigen-presenting cell imparts T&lt;sub&gt;reg&lt;/sub&gt;-dependent tolerance to gut microbiota. (Nature 2022)

- DOI: 10.1038/s41586-022-05309-5 | PMCID: PMC9605865 | PMID: 36070798
- Version used: **2.2.7.1**
- Evidence: We performed MACS2 v2.2.7.1 on fragments of each group with ‘--gsize mm --qval 0.01 --nomodel --ext 200 --shift −100 --call-summits’.
- Full pipeline: read trimming [STAR v2.7.7a] -> alignment/mapping [SAMtools v1.11, STAR v2.7.7a, featureCounts, velocyto v0.17.17] -> normalisation [Scanpy v1.6.0, Seurat v4.0.4] -> dimensionality reduction/clustering [Seurat v4.0.4, UMAP] -> visualisation [Seurat v4.0.4, UMAP] -> stage not stated [ArchR v1.0.1, MACS2 v2.2.7.1, RepeatMasker, scVelo v0.2.4]

### Spatial multi-omic map of human myocardial infarction. (Nature 2022)

- DOI: 10.1038/s41586-022-05060-x | PMCID: PMC9364862 | PMID: 35948637
- Evidence: Following MACS isolation, cells were cultured in DMEM media (Thermo Fisher cat. no.
- Full pipeline: alignment/mapping [Seurat] -> normalisation [Scanpy] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.32.1] -> visualisation [UMAP] -> stage not stated [ArchR v1.0.1, CellPhoneDB, ImageJ, MACS2, R v1.16, scDblFinder v1.4.0]

### Apoptotic brown adipocytes enhance energy expenditure via extracellular inosine. (Nature 2022)

- DOI: 10.1038/s41586-022-05041-0 | PMCID: PMC9452294 | PMID: 35790189
- Evidence: Samples were centrifuged and the pellet was washed with 2 ml of ice-cold MACS buffer (0.5% BSA, 2 mM EDTA, 1% P/S in PBS pH 7.2).
- Full pipeline: normalisation [DESeq2 v1.32.0] -> stage not stated [MACS2, featureCounts v2.0.1, ggpubr v0.4.0]

### Gene regulation by gonadal hormone receptors underlies brain sex differences. (Nature 2022)

- DOI: 10.1038/s41586-022-04686-1 | PMCID: PMC9159952 | PMID: 35508660
- Evidence: After filtering, peaks were called on individual replicate BAM files using MACS2 callpeak (--min-length 25 -q 0.01) 62 .
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, SAMtools, deepTools, featureCounts] -> quantification [Fiji, ImageJ] -> dimensionality reduction/clustering [ComplexHeatmap, Signac, UMAP, clusterProfiler, pheatmap] -> differential/statistical testing [DESeq2, edgeR] -> visualisation [ComplexHeatmap, UMAP, pheatmap] -> stage not stated [ArchR, BEDTools, MACS2, Picard, SCENIC, Seurat, scDblFinder]

### Intermittent PI3Kδ inhibition sustains anti-tumour immunity and curbs irAEs. (Nature 2022)

- DOI: 10.1038/s41586-022-04685-2 | PMCID: PMC9132770 | PMID: 35508656
- Evidence: The suspension was then diluted with MACS buffer and passed through a 70-μm cell strainer to generate a single-cell suspension.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> stage not stated [GSEA, MACS2, Seurat v3.1.5, fgsea v1.10.1]

### Mutation bias reflects natural selection in Arabidopsis thaliana. (Nature 2022)

- DOI: 10.1038/s41586-021-04269-6 | PMCID: PMC8810380 | PMID: 35022609
- Evidence: Peaks were called for each biological replicate using MACS2 using the following parameters: macs2 callpeak -t [ATACseqlibrary].bam -c [Control_library].bam -f BAM --nomodel --shift −50 --extsize 100 --keep-dup=1 -g 1.35e8 -n [Output_Peaks] -B -q 0.05 Peak files and .bam alignment files from three biological replicates were processed with the R package DiffBind to identify consensus peaks that over...
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v2.3, SAMtools] -> alignment/mapping [BWA v0.7.17, Bowtie2, Cutadapt v2.3, MACS2, R, SAMtools] -> variant calling [BWA v0.7.17, Cutadapt v2.3, GATK, SAMtools] -> differential/statistical testing [R] -> stage not stated [VCFtools]

### Omicron escapes the majority of existing SARS-CoV-2 neutralizing antibodies. (Nature 2022)

- DOI: 10.1038/s41586-021-04385-3 | PMCID: PMC8866119 | PMID: 35016194
- Evidence: Different to FACS experiments, as we couldn’t measure the number of cells retained after MACS selection precisely, here F is considered as a scaling factor to transform raw escape fraction ratios to the 0–1 range, and is calculated from the first and 99th percentiles of raw escape fraction ratios.
- Full pipeline: normalisation [MACS2, R] -> dimensionality reduction/clustering [ComplexHeatmap, R, ggplot2 v3.3.3] -> stage not stated [Python]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Version used: **2.1.1.20160309**
- Evidence: MACS2 (2.1.1.20160309) was used to call ATAC-seq peaks.
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### Conserved and divergent gene regulatory programs of the mammalian neocortex. (Nature 2023)

- DOI: 10.1038/s41586-023-06819-6 | PMCID: PMC10719095 | PMID: 38092918
- Evidence: Comparative analysis of chromatin accessibility across species To identify cCREs on the basis of chromatin accessibility data, we determined the open chromatin regions in each motor cortex cell type in each species using MACS2 29 and identified 384,412 human, 336,463 macaque, 281,297 marmoset and 333,814 mouse cCREs that display accessibility in one or more cell types (Extended Data Fig.
- Full pipeline: quality control [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> read trimming [Bowtie2 v2.3, Cutadapt v2.10] -> alignment/mapping [Bowtie2 v2.3, Cutadapt v2.10, SAMtools v1.9] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [LDSC, edgeR] -> visualisation [UMAP] -> stage not stated [BEDTools, Enrichr, HOMER, MACS2, scDblFinder]

### Lung dendritic-cell metabolism underlies susceptibility to viral infection in diabetes. (Nature 2023)

- DOI: 10.1038/s41586-023-06803-0 | PMCID: PMC10733144 | PMID: 38093014
- Evidence: Following the establishment of a single-cell suspension, cells were incubated for 1 h on ice with anti-MHCII beads (Miltenyi) and the enriched fraction was collected using LS MACS columns (Miltenyi).
- Full pipeline: read trimming [Bowtie2 v2.3.5.1, fastp v0.23.0] -> alignment/mapping [Bowtie2 v2.3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools v2.26.0, MACS2, SAMtools v1.9, Seurat v4.0.1]

### Single-cell analysis of chromatin accessibility in the adult mouse brain. (Nature 2023)

- DOI: 10.1038/s41586-023-06824-9 | PMCID: PMC10719105 | PMID: 38092917
- Evidence: Peak calling was performed on the Tn5-corrected single-base insertions using MACS2 36 with the following parameters: --shift -75 --extsize 150 --nomodel --call-summits --SPMR -q 0.01.
- Full pipeline: dimensionality reduction/clustering [BEDTools, UMAP, clusterProfiler, scikit-learn] -> stage not stated [HOMER, MACS2, Monocle, R, RepeatMasker, Seurat, deepTools, scDblFinder]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Version used: **2.2.6**
- Evidence: To identify accessible chromatin regions, peak calling was performed using MACS2 (v.2.2.6) 70 with the options [--qvalue 0.001], on the total and allele-specific ATAC–seq signal, respectively.
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### FOXP3 recognizes microsatellites and bridges DNA through multimerization. (Nature 2023)

- DOI: 10.1038/s41586-023-06793-z | PMCID: PMC10719092 | PMID: 38030726
- Evidence: Peaks were called using MACS2 56 with either input or MBP pull-down as controls.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [Bowtie2, SAMtools] -> normalisation [DESeq2] -> registration [MotionCor2] -> differential/statistical testing [DESeq2] -> structure determination [RELION v4.0.1, UCSF Chimera] -> visualisation [PyMOL] -> stage not stated [BEDTools, CTFFIND v4.1, HOMER, MACS2, PHENIX]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Version used: **2.1.1.20160309**
- Evidence: Next, peaks were called on nucleosome-free reads using MACS2 (v.2.1.1.20160309, with default parameters with ‘–extsize 200–nomodel’).
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Stress granules plug and stabilize damaged endolysosomal membranes. (Nature 2023)

- DOI: 10.1038/s41586-023-06726-w | PMCID: PMC10686833 | PMID: 37968398
- Evidence: Mononuclear cells were washed twice with MACS rinsing solution (Miltenyi 130-091- 222) to remove platelets, then remaining red blood cells were lysed by incubation at room temperature with 10 mL RBC lysing buffer (Sigma R7757) per pellet for 10 min.
- Full pipeline: dimensionality reduction/clustering [Python] -> stage not stated [Fiji, ImageJ, MACS2, PHENIX, R v3.0]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: Peak calling for snATAC-seq data To call peaks on snATAC-seq data (from regular snATAC-seq and from snMultiome-seq), we used the MACS2 tool (v.2.2.7.1) 72 through the CallPeaks function of the Signac package (v.1.3.0, https://github.com/timoast/signac ).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### The PTPN2/PTPN1 inhibitor ABBV-CLS-484 unleashes potent anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06575-7 | PMCID: PMC10599993 | PMID: 37794185
- Evidence: Primary mouse T cell activation and cytokine production analysis Primary mouse T cells were negatively selected from spleens of C57BL/6N mice (Charles River Laboratories) using a MACS Pan T cell Isolation kit II, a CD4 + T cell Isolation kit and a CD8 + T Cell Isolation kit (Miltenyi Biotech).
- Full pipeline: quality control [FastQC v0.11.7] -> read trimming [Bowtie2 v2.5.0, FastQC v0.11.7, Trimmomatic v0.36, kallisto v0.46.0] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.0] -> quantification [DESeq2, R, kallisto v0.46.0] -> dimensionality reduction/clustering [UMAP, scikit-learn] -> differential/statistical testing [DESeq2, R, SciPy v1.7.3, limma, statsmodels v0.13.5] -> visualisation [ImageJ, PyMOL, UMAP] -> stage not stated [BEDTools v2.30.0, GSEA, HOMER v4.11.1, MACS2, QuPath v0.3.0, SAMtools v1.6, Scanpy v1.7.2]

### The sex-specific factor SOA controls dosage compensation in Anopheles mosquitoes. (Nature 2023)

- DOI: 10.1038/s41586-023-06641-0 | PMCID: PMC10620080 | PMID: 37769784
- Evidence: Bioinformatic and web resources The following resources were used: cutadapt ( https://github.com/marcelm/cutadapt ); Bowtie2 ( https://github.com/BenLangmead/bowtie2 ); macs2 ( https://github.com/macs3-project/MACS ); WiggleTools ( https://github.com/Ensembl/WiggleTools ); MEME ( https://meme-suite.org/meme/ ); Gviz ( https://bioconductor.org/packages/release/bioc/html/Gviz.html ); STAR ( https://...
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.0] -> alignment/mapping [Bowtie2 v2.4.5, Clustal Omega, Cutadapt v4.0, STAR v2.7.3a, deepTools v3.1.0] -> differential/statistical testing [BEDTools v2.29.2, DESeq2 v1.26.0] -> visualisation [STAR v2.7.3a] -> stage not stated [MACS2, R, RepeatMasker]

### Transgenic ferret models define pulmonary ionocyte diversity and function. (Nature 2023)

- DOI: 10.1038/s41586-023-06549-9 | PMCID: PMC10533402 | PMID: 37730992
- Evidence: Non-viable dead cells were removed by using MACS Dead Cell Removal Kit following 10X Genomics recommendations (Document CG00039).
- Full pipeline: alignment/mapping [kallisto] -> variant calling [UMAP] -> quantification [R, Seurat] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [brms] -> visualisation [UMAP] -> stage not stated [ImageJ, MACS2]

### Single-cell brain organoid screening identifies developmental defects in autism. (Nature 2023)

- DOI: 10.1038/s41586-023-06473-y | PMCID: PMC10499611 | PMID: 37704762
- Version used: **2.2.6**
- Evidence: Peaks were called from the fragment file using MACS2 (v.2.2.6) 68 and combined in a common peak set before merging.
- Full pipeline: dimensionality reduction/clustering [R, UMAP, clusterProfiler, ggplot2, scVelo v0.2.4] -> differential/statistical testing [R, clusterProfiler] -> visualisation [UMAP, ggplot2] -> stage not stated [Cutadapt, MACS2 v2.2.6, Seurat, Signac v1.4.0, kallisto v0.46.2]

### Non-cell-autonomous cancer progression from chromosomal instability. (Nature 2023)

- DOI: 10.1038/s41586-023-06464-z | PMCID: PMC10468402 | PMID: 37612508
- Evidence: Tissues were minced with a razor blade in the Miltenyi enzyme mix according to the manufacturer’s specifications and transferred to a Gentle MACS Octo Dissociator with heaters (no.
- Full pipeline: alignment/mapping [Picard] -> quantification [ImageJ] -> normalisation [GSEA, ImageJ] -> dimensionality reduction/clustering [Scanpy, UMAP] -> differential/statistical testing [DESeq2 v1.24.0] -> visualisation [Scanpy, UMAP] -> stage not stated [CellChat, CellPhoneDB, MACS2, Seurat v4.1.1]

### Endothelial AHR activity prevents lung barrier disruption in viral infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06287-y | PMCID: PMC7615136 | PMID: 37587341
- Evidence: Primers for influenza virus Matrix gene were as follows: forward: 5’-AAGACCAATCCTGTCACCTCTGA-3’ reverse: 5’-CAAAGCGTCTACGCTGCAGTCC-3’ probe: 5’-TTTGTGTTCACGCTCACCGT-3’ For the isolation of lung cell subsets, tissue digests were blocked with Fc block in MACS (magnetic-activated cell sorting) buffer prior to incubation with biotinylated anti-CD45.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [RSEM, STAR v2.5.2a] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA v2.2.3, R v3.6.0] -> stage not stated [ImageJ, MACS2, QuPath]

### Transient naive reprogramming corrects hiPS cells functionally and epigenetically. (Nature 2023)

- DOI: 10.1038/s41586-023-06424-7 | PMCID: PMC10447250 | PMID: 37587336
- Evidence: ATAC–seq peaks were called with MACS2 with the options–nomodel–keep-dup all–gsize hs.
- Full pipeline: read trimming [Bowtie2, HISAT2, fastp] -> alignment/mapping [Bowtie2, HISAT2, SAMtools v1.13, fastp, minimap2 v2.17] -> normalisation [UMAP] -> dimensionality reduction/clustering [BEDTools v2.30.0, HOMER, UMAP] -> differential/statistical testing [edgeR] -> stage not stated [MACS2, R, Seurat v3.1.1]

### R-loop-dependent promoter-proximal termination ensures genome stability. (Nature 2023)

- DOI: 10.1038/s41586-023-06515-5 | PMCID: PMC10511320 | PMID: 37557913
- Version used: **2.2.7.1**
- Evidence: Peaks were called using MACS2 (v.2.2.7.1) 60 with the option ‘nomodel’ and peak annotation was performed with R package ChIPseeker (v.1.28.3) 61 .
- Full pipeline: read trimming [Trim Galore v0.6.6] -> alignment/mapping [Picard, SAMtools v1.12] -> quantification [Trim Galore v0.6.6] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [Trim Galore v0.6.6] -> stage not stated [ImageJ, MACS2 v2.2.7.1, R]

### Evolutionary histories of breast cancer and related clones. (Nature 2023)

- DOI: 10.1038/s41586-023-06333-9 | PMCID: PMC10432280 | PMID: 37495687
- Evidence: Next, mammary epithelial cells were isolated from the single-cell suspension using CD326 EpCAM MicroBeads (Miltenyi Biotec (Miltenyi)) (1:5 dilution) and the MACS Cell Separation System (Miltenyi) according to the manufacturer’s instructions.
- Full pipeline: stage not stated [ANNOVAR, MACS2, Mutect2, R, SAMtools]

### An atlas of healthy and injured cell states and niches in the human kidney. (Nature 2023)

- DOI: 10.1038/s41586-023-05769-3 | PMCID: PMC10356613 | PMID: 37468583
- Version used: **3.0.0a**
- Evidence: Peak calling was performed using the CallPeaks function and MACS (v.3.0.0a6; https://github.com/macs3-project/MACS ) separately for clusters, subclass.l1 and subclass.l3 annotations.
- Full pipeline: quality control [Cutadapt v3.1, STAR v2.5.2b, SoupX v1.5.0] -> alignment/mapping [Cutadapt v3.1, STAR v2.5.2b] -> quantification [HTSeq v0.11, WGCNA] -> normalisation [ggplot2] -> dimensionality reduction/clustering [MACS2 v3.0.0a, Seurat v4.0.0, UMAP] -> differential/statistical testing [GSEA] -> simulation/modelling [Slingshot, WGCNA, scVelo] -> visualisation [ggplot2, igraph] -> stage not stated [CellChat, ImageJ, R, Signac, fgsea, scDblFinder, velocyto]

### A common allele of HLA is associated with asymptomatic SARS-CoV-2 infection. (Nature 2023)

- DOI: 10.1038/s41586-023-06331-x | PMCID: PMC10396966 | PMID: 37468623
- Evidence: Cells were resuspended in MACS buffer (PBS, 0.5% BSA, 2 mM EDTA) and were directly single-cell index sorted into PCR plates (Eppendorf) using the BD Aria Fusion system.
- Full pipeline: variant calling [R] -> structure determination [PHENIX v1.20.1] -> stage not stated [CCP4, MACS2, PyMOL v2.5]

### Organization of the human intestine at single-cell resolution. (Nature 2023)

- DOI: 10.1038/s41586-023-05915-x | PMCID: PMC10356619 | PMID: 37468586
- Evidence: Peak calling for single-nucleus data Peak calling was performed with MACS2 using ArchR 52 .
- Full pipeline: quality control [ArchR, Seurat, UMAP] -> dimensionality reduction/clustering [ArchR, Scanpy, Seurat, Squidpy, UMAP, limma, scDblFinder] -> differential/statistical testing [limma] -> visualisation [ImageJ, limma] -> stage not stated [MACS2, R]

### SLC38A2 and glutamine signalling in cDC1s dictate anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06299-8 | PMCID: PMC10396969 | PMID: 37407815
- Version used: **2.1.1.20160309**
- Evidence: Next, these nucleosome-free reads were used for peak calling by MACS2 (version 2.1.1.20160309, with default parameters with ‘–extsize 200–nomodel’) with a higher cut-off (MACS2 −q 0.05).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> variant calling [ComplexHeatmap v2.6.2] -> normalisation [R, limma v3.46.0] -> differential/statistical testing [R, limma v3.46.0] -> stage not stated [BEDTools v2.25.0, GSEA, MACS2 v2.1.1.20160309, Picard v2.9.4, Seurat v4.0.2]

### Heritable transcriptional defects from aberrations of nuclear architecture. (Nature 2023)

- DOI: 10.1038/s41586-023-06157-7 | PMCID: PMC10322708 | PMID: 37286600
- Evidence: In brief, we first performed peak-calling on each sample using MACS2 (ref.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, GATK v4.1.9.0, STAR v2.7.6a] -> quantification [RSEM, featureCounts] -> stage not stated [ImageJ, MACS2, Python]

### Myelin dysfunction drives amyloid-β deposition in models of Alzheimer's disease. (Nature 2023)

- DOI: 10.1038/s41586-023-06120-6 | PMCID: PMC10247380 | PMID: 37258678
- Evidence: MACS of microglia and bulk RNA-seq Microglia were isolated from mouse hemibrains (excluding cerebellum and olfactory bulb) by MACS.
- Full pipeline: quality control [STAR v2.5.2b] -> alignment/mapping [DESeq2 v1.26.0, STAR v2.5.2b, featureCounts v1.6.3] -> quantification [DESeq2 v1.26.0, featureCounts v1.6.3] -> normalisation [Seurat v4.1.1] -> dimensionality reduction/clustering [Seurat v4.1.1, UMAP] -> differential/statistical testing [DESeq2 v1.26.0, featureCounts v1.6.3] -> visualisation [DESeq2 v1.26.0, featureCounts v1.6.3] -> stage not stated [MACS2, R v4.04, afex v0.28]

### ERα-associated translocations underlie oncogene amplifications in breast cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06057-w | PMCID: PMC10307628 | PMID: 37198482
- Evidence: When MACS (v2) 63 -processed output was not available, we downloaded FASTQ files from GEO and aligned the reads to hg19 using Bowtie (v1.2.2.) 64 with the unique mapping option.
- Full pipeline: alignment/mapping [MACS2] -> registration [BWA v0.7.15, Picard v2.8.0, SAMtools v1.3.1] -> stage not stated [GSEA, Kraken2, RepeatMasker v4.1.2]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Evidence: 1D signal bedgraph files were used to call peaks with MACS2 106 using the no model and extsize 147 parameters and FDR < 0.01.
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Whole-genome doubling drives oncogenic loss of chromatin segregation. (Nature 2023)

- DOI: 10.1038/s41586-023-05794-2 | PMCID: PMC10060163 | PMID: 36922594
- Evidence: MACS3 (ref.
- Full pipeline: alignment/mapping [SAMtools v1.10] -> differential/statistical testing [DESeq2] -> visualisation [Matplotlib v3.4.2] -> stage not stated [BEDTools v2.30.0, Enrichr, GATK, MACS2, Mutect2, R, SCENIC, Seurat, deepTools]

### H3K4me3 regulates RNA polymerase II promoter-proximal pause-release. (Nature 2023)

- DOI: 10.1038/s41586-023-05780-8 | PMCID: PMC9995272 | PMID: 36859550
- Evidence: RNA was then purified by phenol–chloroform extraction, denatured by 10 min incubation at 65 °C and added to 200 μl μMACS Streptavidin MicroBeads (Milentyl, 130-074-101).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Cutadapt, FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.4.1, STAR, featureCounts] -> quantification [DESeq2, R] -> normalisation [DESeq2] -> dimensionality reduction/clustering [Enrichr, clusterProfiler] -> differential/statistical testing [DESeq2, ggplot2, limma] -> visualisation [ggplot2] -> stage not stated [Bioconductor, GSEA, MACS2, SAMtools v1.10]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Version used: **2.1.1**
- Evidence: ATAC-seq and ChIP–seq peak calling ATAC-seq enriched peaks were determined using MACS2 (v.2.1.1) parameters –shift 100 -p 1e-5 --nolambda --keep-dup all --slocal 10000, as previously described 56 , 69 .
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Annelid functional genomics reveal the origins of bilaterian life cycles. (Nature 2023)

- DOI: 10.1038/s41586-022-05636-7 | PMCID: PMC9977687 | PMID: 36697830
- Version used: **2.2.7.1**
- Evidence: Peak calling was done using MACS2 (v.2.2.7.1) 122 , 123 (-f BAMPE --min-length 100 --max-gap 75 and -q 0.01).
- Full pipeline: read trimming [STAR v2.5.3a, deepTools v3.4.3] -> alignment/mapping [MAFFT, STAR v2.5.3a, StringTie v1.3.6, Trinity v2.5.1, deepTools v3.4.3, kallisto v0.46.2] -> quantification [DESeq2 v1.30.1, kallisto v0.46.2, scikit-learn v1.0.2] -> normalisation [DESeq2 v1.30.1] -> differential/statistical testing [DESeq2 v1.30.1, MrBayes v3.2.7a] -> structure determination [MAFFT, MrBayes v3.2.7a, OrthoFinder v2.2.7] -> visualisation [Cytoscape v3.8.2] -> stage not stated [AlphaFold, BEDTools v2.28.0, BUSCO, Cutadapt v2.5, DIAMOND v0.9.22, HMMER v2.3.2, HOMER v4.11, IQ-TREE v2.0.3, MACS2 v2.2.7.1, RAxML v8.2.11.9, RepeatMasker v2.0.1, SAMtools v1.9, WGCNA, eggNOG]

### Neonatal imprinting of alveolar macrophages via neutrophil-derived 12-HETE. (Nature 2023)

- DOI: 10.1038/s41586-022-05660-7 | PMCID: PMC9945843 | PMID: 36599368
- Evidence: Peaks were subsequently called using the MACS2 software suite 48 with parameters -q 0.05 and –keep-dup all.
- Full pipeline: read trimming [edgeR v3.34.0] -> alignment/mapping [Bowtie2, HISAT2 v2.1.0, HTSeq, SAMtools] -> quantification [DESeq2, HISAT2 v2.1.0, HTSeq] -> normalisation [Seurat, edgeR v3.34.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HISAT2 v2.1.0, featureCounts] -> stage not stated [GSEA, ImageJ, MACS2, Picard, R, fgsea v1.18.0, limma]

### Inferring and perturbing cell fate regulomes in human brain organoids. (Nature 2023)

- DOI: 10.1038/s41586-022-05279-8 | PMCID: PMC10499607 | PMID: 36198796
- Version used: **2.2.6**
- Evidence: Peaks were called from the fragment file using MACS2 (v.2.2.6).
- Full pipeline: variant calling [BCFtools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [XGBoost, brms, scikit-learn] -> stage not stated [MACS2 v2.2.6, R, Scanpy v1.7.0, Seurat, Signac v1.1, igraph, kallisto v0.46.0, scVelo v0.2.2]

### Formation of a low-mass galaxy from star clusters in a 600-million-year-old Universe. (Nature 2024)

- DOI: 10.1038/s41586-024-08293-0 | PMCID: PMC11634762 | PMID: 39663487
- Evidence: Methods Image preparation The cluster field MACS J1423.8 + 2404 was observed with JWST/NIRCam imaging using filters F090W, F115W, F150W, F200W, F277W, F356W, F410M and F444W with exposure times of 6.4 ks each, reaching a signal-to-noise ratio between 5 and 10 for an m AB = 29 point source.
- Full pipeline: dimensionality reduction/clustering [MACS2]

### Single-cell integration reveals metaplasia in inflammatory gut diseases. (Nature 2024)

- DOI: 10.1038/s41586-024-07571-1 | PMCID: PMC11578898 | PMID: 39567783
- Evidence: Biopsies were stored in MACS tissue storage solution (Miltenyi Biotec) before cryopreservation in freezing medium (Cryostor Cs10, Sigma-Aldrich).
- Full pipeline: quality control [UMAP] -> dimensionality reduction/clustering [Scanpy v1.8.0, UMAP] -> differential/statistical testing [CellChat v1.1.1, CellPhoneDB, DESeq2] -> simulation/modelling [Monocle] -> stage not stated [AnnData, MACS2, Matplotlib, NumPy, PHENIX, QuPath, R, STAR v2.7.9a, SciPy, ggplot2, igraph, scikit-learn, seaborn, statsmodels, velocyto]

### Exaptation of ancestral cell-identity networks enables C&lt;sub&gt;4&lt;/sub&gt; photosynthesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08204-3 | PMCID: PMC11618092 | PMID: 39567684
- Evidence: After the initial peak calling using Cell Ranger (10X Genomics), peaks were subsequently re-called using MACS2 (ref.
- Full pipeline: dimensionality reduction/clustering [Seurat, Signac, UMAP] -> differential/statistical testing [OrthoFinder] -> stage not stated [DESeq2, MACS2]

### A multi-omic atlas of human embryonic skeletal development. (Nature 2024)

- DOI: 10.1038/s41586-024-08189-z | PMCID: PMC11578895 | PMID: 39567793
- Evidence: Images were initially processed using MACS iQ View Software, which performed automatic alignment of the tiles.
- Full pipeline: alignment/mapping [MACS2] -> quantification [velocyto v0.17.17] -> dimensionality reduction/clustering [Scanpy, Seurat, UMAP] -> differential/statistical testing [Seurat] -> visualisation [R] -> stage not stated [AnnData, ArchR, CellPhoneDB v4.0.0, Cellpose, PHENIX, SCENIC, SoupX v1.6.0, scDblFinder v0.2.3, scVelo]

### A spatial human thymus cell atlas mapped to a continuous tissue axis. (Nature 2024)

- DOI: 10.1038/s41586-024-07944-6 | PMCID: PMC11578893 | PMID: 39567784
- Evidence: Cells were again resuspended in cell staining buffer and pelleted and this wash step was repeated once more before cells were resuspended in 200 µl MACS buffer (2% FCS, 2 mM EDTA in PBS) in preparation for sorting.
- Full pipeline: quality control [Jupyter, Seurat, tidyverse v1.1.4] -> registration [scikit-image v0.22.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, seaborn v0.13.2] -> visualisation [AnnData v0.10.7, Matplotlib v3.8.4, NumPy v1.26.4, Scanpy v1.9.1, SciPy v1.13.0, UMAP, ggplot2 v3.5.0, seaborn v0.13.2] -> stage not stated [MACS2, SAMtools v1.12, STAR v2.7.9a, scDblFinder, scikit-learn v0.22.0, statsmodels, velocyto]

### Enhancing transcription-replication conflict targets ecDNA-positive cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07802-5 | PMCID: PMC11540844 | PMID: 39506153
- Evidence: MACS2 (ref.
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, Trim Galore, Trimmomatic] -> quantification [CellProfiler v4.2.1] -> normalisation [deepTools] -> visualisation [deepTools] -> stage not stated [HOMER v4.11.1, ImageJ v1.53t, MACS2, SAMtools v1.8]

### Coordinated inheritance of extrachromosomal DNAs in cancer cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07861-8 | PMCID: PMC11541006 | PMID: 39506152
- Version used: **2.2.7.1**
- Evidence: Aligned reads were filtered for quality using samtools (v.1.9) 71 , duplicate fragments were removed using Picard’s MarkDuplicates (v.2.25.3) and peaks were called using MACS2 (v.2.2.7.1) 72 with a q -value cut-off of 0.01 and with a no-shift model.
- Full pipeline: read trimming [BWA, Bowtie2 v2.1.0, Picard, Trim Galore v0.6.4, Trimmomatic] -> alignment/mapping [BWA, Bowtie2 v2.1.0, MACS2 v2.2.7.1, Picard, SAMtools v1.9, Trimmomatic] -> quantification [ImageJ] -> normalisation [deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [deepTools] -> stage not stated [ArchR v1.0.1, Seurat v3.2.3]

### RAS-mutant leukaemia stem cells drive clinical resistance to venetoclax. (Nature 2024)

- DOI: 10.1038/s41586-024-08137-x | PMCID: PMC11618090 | PMID: 39478230
- Evidence: CD34 + CD45 + HSPCs were obtained after MACS-sorting of CD45 + cells on a day of differentiation when all cells are CD34 + to obtain double positive CD34 + CD45 + HSPCs using the MACS cell separation microbeads and reagents (Miltenyi Biotec).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [Bowtie2 v2.1.0, SAMtools v1.11, STAR] -> quantification [Salmon v1.2.1, deepTools v3.2.1] -> normalisation [DESeq2, R, Seurat, deepTools v3.2.1] -> dimensionality reduction/clustering [UMAP, clusterProfiler, pheatmap v1.0.12] -> differential/statistical testing [DESeq2, R] -> stage not stated [GSEA, MACS2, Picard v2.2.4, Trim Galore, fgsea, ggplot2 v3.4.3]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: MACS2 was used to identify peaks indicating open chromatin region.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### RNA m&lt;sup&gt;5&lt;/sup&gt;C oxidation by TET2 regulates chromatin state and leukaemogenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-07969-x | PMCID: PMC11499264 | PMID: 39358506
- Evidence: Peaks were identified using MACS2 56 with the default mode, except for the parameters ‘--shift −75 --extsize 150 --nomodel --call-summits’.
- Full pipeline: read trimming [Bowtie2 v2.4.1, Cutadapt v4.0, HISAT2 v2.2.1, Picard, Trimmomatic v0.39] -> alignment/mapping [Bowtie2 v2.4.1, HISAT2 v2.2.1, Picard, SAMtools v1.16.1, Trimmomatic v0.39] -> quantification [Fiji, ImageJ] -> normalisation [HTSeq v0.12.4] -> differential/statistical testing [DESeq2, edgeR, featureCounts] -> stage not stated [BEDTools v2.31.0, GSEA, MACS2]

### Single-cell multi-omics map of human fetal blood in Down syndrome. (Nature 2024)

- DOI: 10.1038/s41586-024-07946-4 | PMCID: PMC11446839 | PMID: 39322663
- Evidence: Live-cell enrichment was performed using MACS Dead Cell Removal Kit (130-090-101, Miltenyi Biotec) following the manufacturer’s instructions.
- Full pipeline: normalisation [Seurat v5.0.3, UMAP] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [CellPhoneDB, DESeq2, edgeR] -> visualisation [scVelo] -> stage not stated [GSEA, MACS2, R, Scanpy, Signac v1.13, limma, scDblFinder]

### Single-cell CAR T atlas reveals type 2 function in 8-year leukaemia remission. (Nature 2024)

- DOI: 10.1038/s41586-024-07762-w | PMCID: PMC11485231 | PMID: 39322664
- Evidence: Subsequently, the cells were labelled with anti-PE MicroBeads UltraPure (Miltenyi Biotec, 130-105-639) and loaded onto a MACS column positioned within the magnetic field of a MACS Separator.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat, Signac v1.12.0]

### The type 2 cytokine Fc-IL-4 revitalizes exhausted CD8&lt;sup&gt;+&lt;/sup&gt; T cells against cancer. (Nature 2024)

- DOI: 10.1038/s41586-024-07962-4 | PMCID: PMC11485240 | PMID: 39322665
- Evidence: Subsequently, peak identification accuracy was enhanced using MACS2 (ref.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat, Signac v1.12.0]

### Two-factor authentication underpins the precision of the piRNA pathway. (Nature 2024)

- DOI: 10.1038/s41586-024-07963-3 | PMCID: PMC11499256 | PMID: 39294378
- Evidence: Peak calling was done using MACS2 callpeak 56 on individual replicates as well as all replicates together, with IgG samples set as a control.
- Full pipeline: read trimming [Bowtie2, Trim Galore v10.5281, Trimmomatic v0.35] -> alignment/mapping [AlphaFold, Bowtie2, Clustal Omega, Nextflow, Picard, SAMtools, Trim Galore v10.5281] -> normalisation [deepTools] -> differential/statistical testing [ggplot2, ggpubr] -> visualisation [PyMOL, R, deepTools, ggplot2, ggpubr] -> stage not stated [ColabFold, ImageJ, MACS2, tidyverse]

### Tuberculosis in otherwise healthy adults with inherited TNF deficiency. (Nature 2024)

- DOI: 10.1038/s41586-024-07866-3 | PMCID: PMC11390478 | PMID: 39198650
- Evidence: Thawed cells were washed with medium and filtered with a 70-µm-mesh MACS SmartStrainer (Miltenyi Biotec, 130-098-462).
- Full pipeline: alignment/mapping [STAR, featureCounts v1.6.0] -> quantification [featureCounts v1.6.0] -> normalisation [featureCounts v1.6.0] -> differential/statistical testing [DESeq2 v1.40.2] -> stage not stated [CellChat v1.5, GATK, GSEA, Harmony v3.8, MACS2, Picard, SnpEff v4.5, fgsea]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **3.0.0**
- Evidence: Peaks were called on each replicate using MACS3 (v.3.0.0) using the callpeak command, BAMPE, and a mappable genome estimate of 1.87 × 10 9 (from the ENCODE pipeline).
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Clonal inactivation of TERT impairs stem cell competition. (Nature 2024)

- DOI: 10.1038/s41586-024-07700-w | PMCID: PMC11291281 | PMID: 39020172
- Evidence: Then the bam files were merged by conditions, and MACS2 was used to call peaks with parameter “-q 0.05 --nomodel --shift 0”.
- Full pipeline: quality control [FastQC] -> read trimming [DESeq2, FastQC, TopHat v2.0.13, Trim Galore v0.4.0] -> alignment/mapping [Bowtie2, DESeq2, SAMtools, TopHat v2.0.13, Trim Galore v0.4.0] -> differential/statistical testing [R, ggplot2] -> stage not stated [GSEA, ImageJ, MACS2, Picard]

### Multiscale topology classifies cells in subcellular spatial transcriptomics. (Nature 2024)

- DOI: 10.1038/s41586-024-07563-1 | PMCID: PMC11208150 | PMID: 38898271
- Evidence: ...al RNase inhibitor was added to the lysis buffer and debris removal buffer, polypropylene 1.5 ml Eppendorf collection tubes were coated with 10% BSA (MACS BSA Stock Solution, Miltenyi Biotec, 130-091-376) overnight before use and the final nuclei suspension was filtered through a 40 μm FLOWMI cell strainer (SP Bel-Art, 136800040).
- Full pipeline: dimensionality reduction/clustering [Seurat, UMAP] -> simulation/modelling [SciPy] -> visualisation [UMAP] -> stage not stated [MACS2]

### Human SARS-CoV-2 challenge uncovers local and systemic response dynamics. (Nature 2024)

- DOI: 10.1038/s41586-024-07575-x | PMCID: PMC11222146 | PMID: 38898278
- Evidence: Guo and staff at the Flow Cytometry Translational Technology Platform Manager at UCL Cancer Institute for support and guidance with MACS for the Dextramer assays; staff at the University College London CL3 facility at the Paul O’Gorman building and staff at the Sanger Institute Core Sequencing facility for their assistance; and A.
- Full pipeline: alignment/mapping [Seurat v4.1.0] -> dimensionality reduction/clustering [UMAP, igraph] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, Python, R, Scanpy, SoupX, lme4]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Version used: **2.1.2**
- Evidence: ATAC-seq peaks were called using MACS2 (v2.1.2) 77 on pooled data containing all replicates.
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### A disease-associated gene desert directs macrophage inflammation through ETS2. (Nature 2024)

- DOI: 10.1038/s41586-024-07501-1 | PMCID: PMC11168933 | PMID: 38839969
- Evidence: Genome-wide analyses used consensus MACS2 peaks.
- Full pipeline: quality control [FastQC, MultiQC] -> read trimming [Bowtie2, FastQC, Trim Galore] -> alignment/mapping [BCFtools, Bowtie2, HISAT2] -> variant calling [BCFtools] -> quantification [featureCounts] -> normalisation [Seurat, edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA, GSVA, edgeR, limma] -> stage not stated [ImageJ, MACS2, Picard, R, SAMtools, deepTools, ggplot2, napari v0.4.17]

### Nuclear position and local acetyl-CoA production regulate chromatin state. (Nature 2024)

- DOI: 10.1038/s41586-024-07471-4 | PMCID: PMC11168921 | PMID: 38839952
- Evidence: Peak calling was performed using MACS2 callpeak (v.2.1.1.20160309.6) 32 , 33 .
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [MACS2]

### Molecular basis for differential Igk versus Igh V(D)J joining mechanisms. (Nature 2024)

- DOI: 10.1038/s41586-024-07477-y | PMCID: PMC11153149 | PMID: 38811728
- Evidence: We applied MACS2 to call peaks in the three repeats of published CTCF ChIP-seq data in parental v-Abl line 6 , and only kept ‘reliable’ CBEs with motif score > 13 and overlapping with peaks called in ≥2 repeats.
- Full pipeline: quantification [R v3.6.3] -> differential/statistical testing [R v3.6.3] -> stage not stated [ImageJ v1.53q, MACS2]

### In vitro reconstitution of epigenetic reprogramming in the human germ line. (Nature 2024)

- DOI: 10.1038/s41586-024-07526-6 | PMCID: PMC11222161 | PMID: 38768632
- Version used: **2.2.7.1**
- Evidence: Peak calling was performed using MACS2 (v.2.2.7.1) with the default settings 89 .
- Full pipeline: read trimming [Cutadapt v1.18, TopHat v2.1.1] -> alignment/mapping [Bismark v0.22.1, Bowtie2 v2.3.4.1, Cufflinks v2.2.1, Cutadapt v1.18, SAMtools v1.15.1, TopHat v2.1.1] -> variant calling [BCFtools v1.15.1] -> quantification [CellProfiler v4.2.1, Cufflinks v2.2.1] -> normalisation [UMAP, deepTools v3.5.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, MACS2 v2.2.7.1, Picard, R, Scanpy v1.9.1, Seurat, Trim Galore v0.4.1, ggplot2, scDblFinder, scVelo]

### Spatiotemporally resolved colorectal oncogenesis in mini-colons ex vivo. (Nature 2024)

- DOI: 10.1038/s41586-024-07330-2 | PMCID: PMC11078756 | PMID: 38658753
- Evidence: Isolation of colon cells Healthy colon or tumour pieces were finely chopped using a scalpel and transferred to a gentle-MACS C-tube (Miltenyi, 130-093-237) containing 4 ml of digestion medium (RPMI (Thermo Fisher Scientific, 22400089), 1 mg ml –1 collagenase type IV (Life Technologies, 9001-12-1), 0.5 mg ml –1 dispase II (Life Technologies, 17105041) and 10 μg ml –1 DNase I (Applichem, A3778)).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.9] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [BWA v0.7.17, Cytoscape, SAMtools v1.9] -> stage not stated [GSEA, ImageJ, MACS2, Seurat v4.2.0, StarDist, edgeR]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Version used: **2.2.7.1**
- Evidence: Peak calling on each biological replicate ( n = 2) was conducted using MACS2 (v.2.2.7.1) 56 (parameters: --nomodel -q 0.05 --keep-dup all --shift -100 --extsize 200 -g 2456432000 --nolambda).
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### Control of neuronal excitation-inhibition balance by BMP-SMAD1 signalling. (Nature 2024)

- DOI: 10.1038/s41586-024-07317-z | PMCID: PMC11078759 | PMID: 38632412
- Evidence: Peaks were called for each ChIP replicate against a matched input using the MACS2 callpeak function with the default options.
- Full pipeline: alignment/mapping [BEDTools, Bioconductor, STAR] -> differential/statistical testing [edgeR] -> visualisation [STAR] -> stage not stated [HOMER, ImageJ, MACS2, Python, R, ggplot2, limma]

### FOXO1 is a master regulator of memory programming in CAR T cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07300-8 | PMCID: PMC11062920 | PMID: 38600391
- Evidence: Cell selection tNGFR isolations were performed using either Miltenyi MACS sorting or STEMCELL EasySep sorting unless otherwise stated.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, STAR, Trim Galore] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> normalisation [UMAP, limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.6.2] -> differential/statistical testing [DESeq2 v3.16, HOMER, clusterProfiler v4.6.2] -> stage not stated [GSEA, GSVA v1.46.0, MACS2, R v4.1.0, Seurat v4.3.0, Signac, scDblFinder v2.0.3]

### FOXO1 enhances CAR T cell stemness, metabolic fitness and efficacy. (Nature 2024)

- DOI: 10.1038/s41586-024-07242-1 | PMCID: PMC11062918 | PMID: 38600376
- Version used: **2.1.1**
- Evidence: Peak calling was performed with either MACS2 (v2.1.1) or Genrich (v0.6.0) packages.
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [edgeR] -> alignment/mapping [Bowtie2 v2.3.3, HISAT2] -> quantification [featureCounts] -> normalisation [R, edgeR, pheatmap] -> dimensionality reduction/clustering [GSEA, HOMER, UMAP] -> differential/statistical testing [HOMER, fgsea] -> visualisation [UMAP] -> stage not stated [Cutadapt v2.1, MACS2 v2.1.1, SAMtools v1.4.1, Seurat v4.3.0, scDblFinder]

### Mitochondrial complex I activity in microglia sustains neuroinflammation. (Nature 2024)

- DOI: 10.1038/s41586-024-07167-9 | PMCID: PMC10990929 | PMID: 38480879
- Evidence: Ice-cold buffer (95% autoMACS rinsing solution (Miltenyi Biotec) and 5% MACS BSA (Miltenyi Biotec)) was added to the samples (to fill the 15 ml tubes) and the samples were centrifuged at 800 g for 5 min at 4 °C to remove the remaining Percoll.
- Full pipeline: alignment/mapping [STAR v2.7.10a] -> quantification [featureCounts v1.6.3, scVelo v0.2.5, velocyto v0.17.17] -> normalisation [scVelo v0.2.5, velocyto v0.17.17] -> dimensionality reduction/clustering [R v4.2.3, UMAP] -> stage not stated [Bioconductor, DESeq2, ImageJ, MACS2, Seurat v4.3.0.1, edgeR]

### APOE4/4 is linked to damaging lipid droplets in Alzheimer's disease microglia. (Nature 2024)

- DOI: 10.1038/s41586-024-07185-7 | PMCID: PMC10990924 | PMID: 38480892
- Evidence: 130-105-643) were used to enrich rat microglia using MACS columns according to manufacturer’s instructions.
- Full pipeline: alignment/mapping [HOMER, STAR v2.5.1b] -> quantification [Fiji, ImageJ] -> normalisation [R v4.3] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, ImageJ, R v4.3, Seurat] -> stage not stated [Bowtie2, MACS2, Python v3.9.12, Scanpy, scDblFinder v0.2.3]

### Selfish conflict underlies RNA-mediated parent-of-origin effects. (Nature 2024)

- DOI: 10.1038/s41586-024-07155-z | PMCID: PMC10990930 | PMID: 38448590
- Evidence: Right, example of reproducible peaks identified by MACS2. piRNAs target slow-1 Since the transgenerational repression of slow-1/grow-1 does not stem from an external trigger, we reasoned that endogenous piRNAs could mediate this effect.
- Full pipeline: quality control [deepTools v3.3.1] -> read trimming [Cutadapt v1.18] -> alignment/mapping [Clustal Omega, HISAT2 v2.1, SAMtools v1.10] -> quantification [BEDTools v2.27, R, featureCounts] -> normalisation [BEDTools v2.27, R, featureCounts] -> visualisation [R, featureCounts] -> stage not stated [BLAST, Flye, MACS2]

### B cells orchestrate tolerance to the neuromyelitis optica autoantigen AQP4. (Nature 2024)

- DOI: 10.1038/s41586-024-07079-8 | PMCID: PMC10937377 | PMID: 38383779
- Evidence: Thymocytes were depleted with CD90.2 MACS beads according to the manufacturer’s instructions.
- Full pipeline: alignment/mapping [velocyto v0.17.17] -> normalisation [DESeq2, GSEA v4.3.2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> simulation/modelling [scVelo v0.2.5, velocyto v0.17.17] -> stage not stated [MACS2, QuPath v0.3.2]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Evidence: Peak call for H3K27ac was performed using the MACS algorithm (v2.1.0) with a cut-off P = 10 −7 .
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### WNT signalling control by KDM5C during development affects cognition. (Nature 2024)

- DOI: 10.1038/s41586-024-07067-y | PMCID: PMC10954547 | PMID: 38383780
- Version used: **2.2.6**
- Evidence: MACS (v.2.2.6) was used to call KDM5C peaks on each replicate individually, with the --nolambda parameter.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.1, DESeq2 v1.18.0, R, SAMtools v1.9, STAR v2.5.2b] -> quantification [Cufflinks v2.1.0] -> normalisation [Cufflinks v2.1.0] -> differential/statistical testing [Cufflinks v2.1.0, DESeq2 v1.18.0, R] -> stage not stated [BEDTools, Bioconductor v3.6, GSEA, MACS2 v2.2.6, ggplot2 v2.2.1]

### The nuclear factor ID3 endows macrophages with a potent anti-tumour activity. (Nature 2024)

- DOI: 10.1038/s41586-023-06950-4 | PMCID: PMC10881399 | PMID: 38326607
- Evidence: Human primary cells Human NK cells Human NK cells (IQ Biosciences, IQB-Hu1-NK5) were cultured in NK MACS medium (Miltenyi Biotec) supplemented with 10% heat-inactivated pooled human AB serum (Sigma-Aldrich), 100 U ml −1 penicillin and 100 μg ml −1 streptomycin (Invitrogen) and 20 ng ml −1 hIL-2 incubated at 37 °C in 5% CO 2 .
- Full pipeline: alignment/mapping [BLAST, HTSeq, STAR v2.7.10a] -> quantification [HTSeq, ImageJ] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [DESeq2] -> stage not stated [Harmony v0.1.1, Keras v2.3.1, MACS2, Seurat, fgsea, scikit-learn v0.21.3]

### An epigenetic barrier sets the timing of human neuronal maturation. (Nature 2024)

- DOI: 10.1038/s41586-023-06984-8 | PMCID: PMC10881400 | PMID: 38297124
- Evidence: Enriched regions were discovered using MACS2 with a p-value setting of 0.001 and a matched IgG or ‘no antibody” as the control.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore, Trimmomatic v0.36] -> read trimming [Bowtie2, Cutadapt, Picard, Trim Galore, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, HTSeq, Picard] -> quantification [ImageJ] -> normalisation [BEDTools] -> dimensionality reduction/clustering [HOMER, UMAP] -> differential/statistical testing [DESeq2, GSEA, MACS2] -> visualisation [UMAP] -> stage not stated [R v4.1, Seurat v4.2.0, featureCounts]

### Slide-tags enables single-nucleus barcoding for multimodal spatial genomics. (Nature 2024)

- DOI: 10.1038/s41586-023-06837-4 | PMCID: PMC10764288 | PMID: 38093010
- Version used: **2.2.7.1**
- Evidence: Peaks were recalled using the CallPeaks function, which uses MACS2 (v.2.2.7.1) 78 , across all cells.
- Full pipeline: quality control [Seurat v4.3.0] -> alignment/mapping [RSEM, UMAP] -> quantification [RSEM] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v4.6.0] -> differential/statistical testing [Enrichr] -> stage not stated [ArchR, MACS2 v2.2.7.1, R v4.2.2, Signac v1.9.0]

### Targeted design of synthetic enhancers for selected tissues in the Drosophila embryo. (Nature 2024)

- DOI: 10.1038/s41586-023-06905-9 | PMCID: PMC10830412 | PMID: 38086418
- Evidence: All read fragments from each pseudo-bulk were used for peak calling with MACS2 54 , 55 with the following command: macs2 callpeak --nomodel --keep-dup all --extsize 200 --shift −100 --gsize dm -B.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> machine learning [Keras, TensorFlow v1.14.0] -> visualisation [R, UMAP] -> stage not stated [BEDTools, MACS2, ggplot2 v3.2.1]

### In vitro production of cat-restricted Toxoplasma pre-sexual stages. (Nature 2024)

- DOI: 10.1038/s41586-023-06821-y | PMCID: PMC10781626 | PMID: 38093015
- Version used: **2.2**
- Evidence: Aligned reads were used for peak calling of the ChIP-enriched peaks using MACS v2.2 with a cutoff P value of 10 −4 .
- Full pipeline: quality control [FastQC, MultiQC, Picard] -> read trimming [Picard] -> alignment/mapping [MACS2 v2.2, Picard, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2, MACS2 v2.2, limma] -> stage not stated [HOMER, SAMtools v1.4]

### Cell-type-directed design of synthetic enhancers. (Nature 2024)

- DOI: 10.1038/s41586-023-06936-2 | PMCID: PMC10830415 | PMID: 38086419
- Version used: **2.1.2.1**
- Evidence: Peaks were called using MACS2 (v.2.1.2.1; RRID: SCR_013291 ) callpeak 81 .
- Full pipeline: read trimming [SAMtools v1.16.1, Trim Galore] -> dimensionality reduction/clustering [BEDTools v2.30.0] -> differential/statistical testing [SciPy v1.6.0] -> machine learning [NumPy v1.19.5] -> visualisation [Matplotlib v3.1.1] -> stage not stated [MACS2 v2.1.2.1, deepTools]

### Dictionary of immune responses to cytokines at single-cell resolution. (Nature 2024)

- DOI: 10.1038/s41586-023-06816-9 | PMCID: PMC10781646 | PMID: 38057668
- Evidence: Streptavidin microbeads were then added and the cells were magnetically sorted using MACS MS columns according to the manufacturer’s protocol (Miltenyi Biotec).
- Full pipeline: dimensionality reduction/clustering [UMAP, clusterProfiler v4.2.1] -> visualisation [UMAP] -> stage not stated [MACS2, R, Seurat]

### Synthetic α-synuclein fibrils replicate in mice causing MSA-like pathology. (Nature 2025)

- DOI: 10.1038/s41586-025-09698-1 | PMCID: PMC12695662 | PMID: 41193804
- Evidence: The cells were then plated at 20,000 per well in 96-well plates (Corning, BioCoat poly- d -lysine imaging plates) in neuronal medium (MACS Neuro Medium, Miltenyi Biotech) containing 0.5% penicillin–streptomycin, 0.5 mM alanyl-glutamine and 2% NeuroBrew supplement (Miltenyi Biotech).
- Full pipeline: structure determination [ChimeraX, Coot, IMOD, PHENIX, RELION v4.0] -> stage not stated [MACS2]

### Lymphoid gene expression supports neuroprotective microglia function. (Nature 2025)

- DOI: 10.1038/s41586-025-09662-z | PMCID: PMC12675299 | PMID: 41193812
- Version used: **2.1.0**
- Evidence: Post-filtering Binary Alignment Map files for all samples were merged using the merge function from Samtools (v.1.11), followed by peak calling using MACS2 (v.2.1.0) with parameters --nomodel, --nolambda, --keep-dup all and --slocal 10000, optimized for paired data (−f BAMPE) using the mouse genome (−g mm) 89 .
- Full pipeline: quality control [Cutadapt v2.9, FastQC v0.11.9, HISAT2, Trim Galore] -> read trimming [Bowtie2 v2.2.8, Cutadapt v2.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.2.8, FastQC v0.11.9, HISAT2, MACS2 v2.1.0, SAMtools v1.11, deepTools v3.2.1] -> quantification [CellProfiler, DESeq2, ImageJ, deepTools v3.2.1] -> normalisation [Fiji, deepTools v3.2.1, edgeR, ggplot2 v3.3.5] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [GSEA v4.2.3, limma] -> visualisation [edgeR, ggplot2 v3.3.5] -> stage not stated [Cellpose, Enrichr, HOMER v4.10, Picard v2.2.4, Python, QuPath v0.5.1, R v4.2, Seurat v5.0.3, featureCounts v2.0.0, pheatmap]

### Multi-omic profiling reveals age-related immune dynamics in healthy adults. (Nature 2025)

- DOI: 10.1038/s41586-025-09686-5 | PMCID: PMC12711581 | PMID: 41162704
- Evidence: The following steps were executed using the default ArchR workflow: LSI dimensionality reduction, group coverage, identification of reproducible peaks (MACS3) 65 , peak matrix construction, motif annotation (cisbp database), background peak construction, deviation matrix and weight imputation (MAGIC) 66 .
- Full pipeline: quality control [UMAP] -> normalisation [UMAP, scDblFinder] -> dimensionality reduction/clustering [MACS2, UMAP, scDblFinder] -> differential/statistical testing [DESeq2 v1.42.0, GSEA, R v4.3.2, fgsea] -> simulation/modelling [Slingshot] -> visualisation [scDblFinder] -> stage not stated [ArchR v1.0.2, Scanpy, Seurat v5.0.1, lme4]

### Myocardial reprogramming by HMGN1 underlies heart defects in trisomy 21. (Nature 2025)

- DOI: 10.1038/s41586-025-09593-9 | PMCID: PMC12657217 | PMID: 41125893
- Evidence: Peak calling was performed using MACS2 and differentially accessible peaks marking each cluster was obtained 64 .
- Full pipeline: read trimming [Nextflow v23.10.1.5891, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.13, Nextflow v23.10.1.5891] -> normalisation [BCFtools v1.13] -> dimensionality reduction/clustering [BEDTools, MACS2, UMAP] -> differential/statistical testing [MACS2, WGCNA, edgeR, lme4 v3.1, scikit-learn] -> stage not stated [ArchR, NumPy, R v4.1.1, Seurat, VEP, data.table, deepTools, tidyverse]

### Neoadjuvant immunotherapy in mismatch-repair-proficient colon cancers. (Nature 2025)

- DOI: 10.1038/s41586-025-09679-4 | PMCID: PMC12711568 | PMID: 41115454
- Evidence: The cells were then resuspended in 500 µl MACS buffer (PBS with 0.5% bovine serum albumin (BSA; Sigma) and 2 mM EDTA (Life Technologies)).
- Full pipeline: normalisation [CellProfiler v4.2.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3, GSVA v1.46, survival (R) v0.4.9] -> stage not stated [GATK, MACS2, R v4.3.1, Seurat, ggplot2 v3.4.2, ggpubr v0.6.0, pheatmap v1.0.12, tidyverse v2.0]

### A human-specific regulatory mechanism revealed in a pre-implantation model. (Nature 2025)

- DOI: 10.1038/s41586-025-09571-1 | PMCID: PMC12589118 | PMID: 41034587
- Evidence: Peaks were called using MACS3 (ref.
- Full pipeline: read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, HISAT2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, UMAP] -> stage not stated [BLAST, MACS2, RepeatMasker, SAMtools, Seurat]

### Co-option of an ancestral cloacal regulatory landscape during digit evolution. (Nature 2025)

- DOI: 10.1038/s41586-025-09548-0 | PMCID: PMC12675288 | PMID: 40963014
- Version used: **2.2.7.1**
- Evidence: Peaks were called, and coverage was generated by MACS2 v.2.2.7.1 with --nomodel --keep-dup all --shift -100 --extsize 200 --call-summits -B.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, STAR v2.7.10a] -> alignment/mapping [Bowtie2 v2.4.5, Cufflinks v2.2.1, SAMtools v1.16.1, STAR v2.7.10a] -> normalisation [ggplot2 v3.4.4] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.4.4] -> visualisation [ggplot2 v3.4.4] -> stage not stated [ArchR, BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1, Picard v3.0.0, R, Seurat]

### PICALM Alzheimer's risk allele causes aberrant lipid droplets in microglia. (Nature 2025)

- DOI: 10.1038/s41586-025-09486-x | PMCID: PMC12571902 | PMID: 40903578
- Evidence: For peak calling, MACS2 69 was used to generate peak files (narrowPeak format) with the recommended settings at FDR = 0.05 (-f BAMPE, --nomodel, --call-summits --keep-dup-all -B).
- Full pipeline: quality control [Bowtie2, SAMtools v1.14] -> read trimming [Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools v1.14, STAR v2.7.2] -> variant calling [GATK, deepTools] -> quantification [deepTools, edgeR v4.0.16] -> normalisation [R, deepTools] -> dimensionality reduction/clustering [edgeR v4.0.16] -> differential/statistical testing [MACS2, STAR v2.7.2, limma v3.58.1, lme4] -> stage not stated [Fiji v1.54f, ImageJ v1.54f, Picard]

### The evolution of hominin bipedalism in two steps. (Nature 2025)

- DOI: 10.1038/s41586-025-09399-9 | PMCID: PMC12460174 | PMID: 40866708
- Evidence: For each pseudobulk profile, consensus peaks were inferred using MACS2 69 , which produced.bed files for each cell type that were subsequently used in further analyses.
- Full pipeline: quality control [MultiQC v6.14] -> dimensionality reduction/clustering [UMAP, ggplot2] -> visualisation [Cytoscape, ggplot2] -> stage not stated [AnnData, CellChat, MACS2, SCENIC, Scanpy, Seurat, Signac v1.10, scDblFinder, scVelo v0.24, velocyto v0.17]

### Mechanical confinement governs phenotypic plasticity in melanoma. (Nature 2025)

- DOI: 10.1038/s41586-025-09445-6 | PMCID: PMC12611772 | PMID: 40866703
- Evidence: Peaks were identified using MACS2 (ref.
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.7, Trimmomatic] -> read trimming [Cutadapt, FastQC, Picard, Trim Galore v0.6.7, Trimmomatic] -> alignment/mapping [Bowtie2, FastQC, Trimmomatic] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, CellProfiler, GSEA, MACS2, R v4.3.1, Seurat, TrackMate, deepTools, fgsea]

### Thymic epithelial cells amplify epigenetic noise to promote immune tolerance. (Nature 2025)

- DOI: 10.1038/s41586-025-09424-x | PMCID: PMC12527919 | PMID: 40836089
- Version used: **2.2.9.1**
- Evidence: For scATAC-seq peak calling, the standard ArchR workflow was used using MACS2 (v.2.2.9.1).
- Full pipeline: read trimming [edgeR v4.0.2] -> alignment/mapping [Bowtie2 v2.2.9, TopHat v2.1.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v4.0.2] -> visualisation [UMAP] -> stage not stated [ArchR, MACS2 v2.2.9.1, Picard v2.21.8, R v4.3.2, SAMtools v1.9, Seurat v5.1.0, featureCounts]

### Expanding the cytokine receptor alphabet reprograms T cells into diverse states. (Nature 2025)

- DOI: 10.1038/s41586-025-09393-1 | PMCID: PMC12460165 | PMID: 40804519
- Version used: **3.0.1**
- Evidence: The aligned reads were then subjected to peak calling using MACS3 (v.3.0.1) 60 .
- Full pipeline: quality control [FastQC] -> alignment/mapping [FastQC, MACS2 v3.0.1] -> quantification [Seurat v5.1.0, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [R v4.4, SCENIC v0.12.1]

### Range extender mediates long-distance enhancer activity. (Nature 2025)

- DOI: 10.1038/s41586-025-09221-6 | PMCID: PMC12267059 | PMID: 40604280
- Evidence: Low-quality nuclei were filtered out using standard Signac parameters and MACS2 was used for peak calling 84 .
- Full pipeline: alignment/mapping [BEDTools] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [HOMER] -> stage not stated [MACS2, R, Signac]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: Peak calling was then performed using the MACS3 pipeline 131 with the inclusion of the parameters --broad -g 1.9e+9.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### Single-cell transcriptomic and chromatin dynamics of the human brain in PTSD. (Nature 2025)

- DOI: 10.1038/s41586-025-09083-y | PMCID: PMC12267058 | PMID: 40533550
- Version used: **2.2.9.1**
- Evidence: MACS2 (v2.2.9.1) 70 was then used to call peaks on each pseudobulk replicate.
- Full pipeline: quality control [ArchR, R, Signac, Squidpy] -> normalisation [Enrichr] -> dimensionality reduction/clustering [Seurat, Squidpy, UMAP] -> differential/statistical testing [UMAP] -> stage not stated [BEDTools, CellChat, DESeq2 v1.46.0, LDSC, MACS2 v2.2.9.1, PLINK v2.0, igraph v1.2.6, scDblFinder]

### Kupffer cell programming by maternal obesity triggers fatty liver disease. (Nature 2025)

- DOI: 10.1038/s41586-025-09190-w | PMCID: PMC12367551 | PMID: 40533564
- Evidence: Both modalities were extracted from the 10X Genomics ‘filtered feature matrix file’, in which count data were used for additional filtering of low-quality cells, before using MACS3 to perform the peak calling within the remaining cells to reduce computational time.
- Full pipeline: quality control [FastQC v0.12.1] -> alignment/mapping [kallisto] -> quantification [QuPath, kallisto] -> dimensionality reduction/clustering [CellChat, UMAP, clusterProfiler] -> stage not stated [Bioconductor v3.15, DESeq2, MACS2, Seurat, Signac]

### Metabolic adaptations direct cell fate during tissue regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09097-6 | PMCID: PMC12240837 | PMID: 40500453
- Evidence: Cells were then filtered through a 70-μm mesh, spun down at 290 g for 5 min and resuspended in MACS buffer (0.5% BSA and 2 mM EDTA in Ca 2+ /Mg 2+ -free PBS).
- Full pipeline: read trimming [Trimmomatic, featureCounts] -> alignment/mapping [Trimmomatic, featureCounts] -> quantification [ImageJ v1.7, featureCounts] -> normalisation [pheatmap] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, R, Trimmomatic] -> visualisation [Trimmomatic, pheatmap] -> stage not stated [GSEA, MACS2, Seurat]

### Targeting GRPR for sex hormone-dependent cancer after loss of E-cadherin. (Nature 2025)

- DOI: 10.1038/s41586-025-09111-x | PMCID: PMC12267067 | PMID: 40500450
- Evidence: ...e pharmacological β-catenin inhibitor iCRT3 (10 μM, 48 h). p , β-catenin binding to Esr1 in nephron precursor cells with significant peaks (called by MACS2) indicated.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [ImageJ, RSEM] -> normalisation [GSEA, RSEM] -> stage not stated [Bioconductor, MACS2, Picard, R, edgeR, ggplot2 v3.5.1]

### SP140-RESIST pathway regulates interferon mRNA stability and antiviral immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09152-2 | PMCID: PMC12310523 | PMID: 40500448
- Version used: **2.1.1**
- Evidence: Peak calling was performed using complete and size-subsetted alignment files with MACS2 v.2.1.1 with paired-end options ‘--format BAMPE --SPMR -B --broad’.
- Full pipeline: read trimming [BWA v0.7.15] -> alignment/mapping [BWA v0.7.15, ChimeraX v1.6.1, HISAT2 v2.1.0, MACS2 v2.1.1, SAMtools, Salmon v0.13.1] -> variant calling [DESeq2 v1.38.3] -> quantification [Salmon v0.13.1] -> normalisation [deepTools] -> visualisation [ChimeraX v1.6.1, HISAT2 v2.1.0, SAMtools] -> stage not stated [AlphaFold, BEDTools, R, ggplot2 v3.5.0]

### Developmental trajectory and evolutionary origin of thymic mimetic cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09148-y | PMCID: PMC12286861 | PMID: 40500437
- Evidence: EPCAM + CD45 − cells (after negative enrichment using anti-CD45 magnetic-activated cell sorting (MACS) beads and anti–Ter-119 MACS beads, Miltenyi Biotec) were sorted directly into TRI reagent (T9424, Sigma-Aldrich).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [limma] -> stage not stated [Galaxy, HISAT2 v2.1.0, MACS2, Trim Galore, featureCounts v1.6.1.0, scDblFinder]

### Concurrent loss of the Y chromosome in cancer and T cells impacts outcome. (Nature 2025)

- DOI: 10.1038/s41586-025-09071-2 | PMCID: PMC12221978 | PMID: 40468066
- Evidence: The tumours were cut and transferred immediately to MACS C-tubes along with chilled DMEM and tumour dissociation enzymes for mouse (Miltenyi Biotech, catalogue no.
- Full pipeline: quality control [FastQC v0.12.1, MultiQC v1.13, Scanpy] -> read trimming [STAR, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.12.1, MultiQC v1.13, Picard, STAR, featureCounts v1.5.3] -> quantification [Bioconductor, FastQC v0.12.1, MultiQC v1.13, featureCounts v1.5.3] -> normalisation [AnnData] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [Bioconductor, Python, clusterProfiler] -> machine learning [scikit-learn] -> visualisation [ComplexHeatmap v2.11.1, UMAP, ggplot2 v3.3.5, ggpubr v0.6.0] -> stage not stated [DESeq2, GATK, GSEA, GSVA, MACS2, Matplotlib v3.8.0, NumPy v1.24.2, R, SciPy v1.10.1, pandas v2.0.0, scDblFinder, seaborn v0.11.2, survival (R)]

### CREM is a regulatory checkpoint of CAR and IL-15 signalling in NK cells. (Nature 2025)

- DOI: 10.1038/s41586-025-09087-8 | PMCID: PMC12286855 | PMID: 40468083
- Evidence: Peaks were called using MACS2 (ref.
- Full pipeline: quantification [SCENIC] -> normalisation [ImageJ v1.53t] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [fgsea] -> stage not stated [GSEA, MACS2, R v4.0.1, Scanpy, Seurat, Signac v1.12.0]

### Loss of colonic fidelity enables multilineage plasticity and metastasis. (Nature 2025)

- DOI: 10.1038/s41586-025-09125-5 | PMCID: PMC12350155 | PMID: 40468074
- Evidence: MACS2 (ref.
- Full pipeline: variant calling [QuPath, UMAP] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony, UMAP] -> differential/statistical testing [ComplexHeatmap, DESeq2, HOMER] -> visualisation [ComplexHeatmap] -> stage not stated [BEDTools, GSEA, GSVA, MACS2, R, Seurat]

### In vivo haemopoietic stem cell gene therapy enabled by postnatal trafficking. (Nature 2025)

- DOI: 10.1038/s41586-025-09070-3 | PMCID: PMC12286858 | PMID: 40437086
- Evidence: Between 500,000 and 1,000,000 cells were processed, washed with PBS–2% FBS (FetalClone II, HyClone, Euroclone) or MACS buffer (PBS pH 7.2, 0.5% bovine serum albumin (BSA), 2 mM EDTA), treated with fragment crystallizable (Fc) Receptor-Block (Miltenyi Biotec) when antibody-stained and then resuspended in the buffer used for washing.
- Full pipeline: quantification [R] -> stage not stated [MACS2]

### Molecular basis of positional memory in limb regeneration. (Nature 2025)

- DOI: 10.1038/s41586-025-09036-5 | PMCID: PMC12176643 | PMID: 40399677
- Evidence: Tissues removed were then dissociated into single-cell suspensions using Liberase TM enzyme (Merck, 05401127001) as described previously 63 , with the following modifications: dissociation was done for 55 min (mature sample) or 45 min (blastema samples), and the cells were filtered through a 70-μm MACS SmartStrainer (Miltenyi Biotec, 130-098-462).
- Full pipeline: read trimming [HISAT2, Trimmomatic v0.39] -> alignment/mapping [HISAT2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, ggplot2 v3.3.6, pheatmap]

### Chromatin loops are an ancestral hallmark of the animal regulatory genome. (Nature 2025)

- DOI: 10.1038/s41586-025-08960-w | PMCID: PMC12221973 | PMID: 40335694
- Evidence: ATAC peaks were called with MACS2 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39, fastp] -> alignment/mapping [Bismark, HISAT2, Medaka v1.5.0, STAR, Trimmomatic v0.39, deepTools, fastp, minimap2] -> quantification [STAR] -> stage not stated [BUSCO v5.1.2, Flye v2.9.0, HOMER, IQ-TREE, MACS2, R, RepeatMasker, StringTie]

### Activation of lysosomal iron triggers ferroptosis in cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08974-4 | PMCID: PMC12158755 | PMID: 40335696
- Evidence: Subsequently, the dissociated tumour suspension was applied to a MACS SmartStrainer (30 µm) (Miltenyi).
- Full pipeline: stage not stated [MACS2]

### Microbial metabolite drives ageing-related clonal haematopoiesis via ALPK1. (Nature 2025)

- DOI: 10.1038/s41586-025-08938-8 | PMCID: PMC12137129 | PMID: 40269158
- Evidence: Cells were collected, washed with PBS + 2% FBS + 2 mM EDTA (MACS buffer) and fixed with 4% paraformaldehyde (15710, Electron Microscopy Sciences).
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [HISAT2] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, FastQC v0.11.8, R] -> stage not stated [MACS2, ggplot2, phyloseq]

### Targeting PIKfyve-driven lipid metabolism in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-08917-z | PMCID: PMC12176661 | PMID: 40269157
- Evidence: The cells were then strained using a MACS SmartStrainer (30 μm) (Miltenyi Biotec, 130-110-915) and rinsed with PBS before culturing.
- Full pipeline: read trimming [Bowtie2 v2.4.5, Cutadapt v4.1, Trimmomatic v0.39] -> alignment/mapping [BEDTools, Bowtie2 v2.4.5, SAMtools v1.9, kallisto] -> quantification [Fiji, ImageJ, kallisto] -> normalisation [edgeR, limma] -> differential/statistical testing [edgeR, limma] -> machine learning [MACS2] -> stage not stated [HOMER v5.1, Picard, R, fgsea, ggplot2 v3.4.4, lme4 v1.1]

### Perturbing LSD1 and WNT rewires transcription to synergistically induce AML differentiation. (Nature 2025)

- DOI: 10.1038/s41586-025-08915-1 | PMCID: PMC12158781 | PMID: 40240608
- Version used: **2.2.7.1**
- Evidence: Peaks were then called with MACS2 (2.2.7.1) with replicates being merged for downstream analyses.
- Full pipeline: quality control [Cutadapt v2.1, FastQC v0.11.9, MultiQC] -> read trimming [Cutadapt v2.1, FastQC v0.11.9, Trim Galore v0.6.6] -> alignment/mapping [BEDTools v2.30.0, Bowtie2 v2.4.4, MultiQC, SAMtools v1.15.1, STAR v2.7.0f, Trim Galore v0.6.6, featureCounts] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, ImageJ v1.54g, MACS2 v2.2.7.1, Nextflow v21.10.6, deepTools v3.5.1, edgeR v3.50.3, ggplot2 v3.4.2, limma v3.36.0, survival (R)]

### Comprehensive interrogation of synthetic lethality in the DNA damage response. (Nature 2025)

- DOI: 10.1038/s41586-025-08815-4 | PMCID: PMC12018271 | PMID: 40205037
- Version used: **3.0.0b**
- Evidence: Peaks were called using MACS3 v.3.0.0b1 with RPE-1 wild type set as the control and default settings.
- Full pipeline: alignment/mapping [Bowtie2 v2.4.4] -> quantification [Fiji v2.9.0, ImageJ v2.9.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, MACS2 v3.0.0b, Python, R, SAMtools v1.6, limma]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Version used: **2.1.1.20160309**
- Evidence: Next, peaks in nucleosome-free regions were identified using MACS2 (v.2.1.1.20160309, with the default parameters with ‘--extsize 200--nomodel’).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### TGFβ links EBV to multisystem inflammatory syndrome in children. (Nature 2025)

- DOI: 10.1038/s41586-025-08697-6 | PMCID: PMC12003184 | PMID: 40074901
- Evidence: After stimulation, cells were stained with TotalSeq anti-human Hashtags as previously mentioned, followed by CD154 MACS enrichment according to the manufacturer’s protocol (CD154 MicroBead Kit, human; Miltenyi Biotec).
- Full pipeline: normalisation [GSEA, R v4.1.2, Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [MACS2, pheatmap]

### Sensory input, sex and function shape hypothalamic cell type development. (Nature 2025)

- DOI: 10.1038/s41586-025-08603-0 | PMCID: PMC12589138 | PMID: 40044853
- Evidence: Samples were dounce homogenized in a 3-ml Potter-Elvehjem Tissue Grinder in a 4 °C cold room in 0.1% NP40 lysis buffer, passed through a 70-µm filter (MACS Smart-strainer) and centrifuged at 500 g for 5 min.
- Full pipeline: normalisation [Slingshot] -> dimensionality reduction/clustering [Slingshot, UMAP] -> differential/statistical testing [ArchR, DESeq2, edgeR, ggplot2, limma] -> simulation/modelling [Matplotlib] -> machine learning [Nextstrain v1.0.3] -> visualisation [Matplotlib] -> stage not stated [ComplexHeatmap, MACS2, Python, R, Scanpy, Seurat, pheatmap]

### Genome-coverage single-cell histone modifications for embryo lineage tracing. (Nature 2025)

- DOI: 10.1038/s41586-025-08656-1 | PMCID: PMC12003199 | PMID: 40011786
- Version used: **2.1.1**
- Evidence: For peak calling, MACS2 (v.2.1.1) 56 with the ‘–broad’ parameter was used to call peaks for aggregated profiles of TACIT data.
- Full pipeline: quality control [Bowtie2 v2.2.9, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.2.9, FastQC v0.11.5, SAMtools v1.9] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> simulation/modelling [Monocle] -> visualisation [UMAP] -> stage not stated [MACS2 v2.1.1, Picard v2.2.4, RepeatMasker, SCENIC]

### Programs, origins and immunomodulatory functions of myeloid cells in glioma. (Nature 2025)

- DOI: 10.1038/s41586-025-08633-8 | PMCID: PMC12018266 | PMID: 40011771
- Version used: **2.2.9.1**
- Evidence: MACS2 v.2.2.9.1 was used to call peaks using the following settings: -g hs -f BED -q 0.01 --nomodel --shift -75 --extsize 150 --keep-dup all.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [HOMER, SAMtools, STAR] -> quantification [SCENIC, scikit-learn] -> normalisation [SCENIC, edgeR, scikit-learn] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [HOMER] -> visualisation [NetworkX v2.0, Seurat, ggplot2] -> stage not stated [BEDTools, ComplexHeatmap, GSVA, MACS2 v2.2.9.1, Signac, deepTools]

### The maternal X chromosome affects cognition and brain ageing in female mice. (Nature 2025)

- DOI: 10.1038/s41586-024-08457-y | PMCID: PMC11798838 | PMID: 39843739
- Evidence: Nuclei were filtered through a 30-mm cell strainer (MACS 130-041-407), counted and stored at −80 °C until FACS sorting.
- Full pipeline: quality control [FastQC] -> read trimming [STAR] -> alignment/mapping [Bismark, STAR] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, featureCounts]

### Multiscale footprints reveal the organization of cis-regulatory elements. (Nature 2025)

- DOI: 10.1038/s41586-024-08443-4 | PMCID: PMC11839466 | PMID: 39843737
- Evidence: Open chromatin region peaks were called on individual samples using MACS2 peak caller (v.2.2.9.1) 56 with the following parameters: --nomodel –nolambda –keep-dup -call-summits.
- Full pipeline: quality control [FastQC v0.25] -> alignment/mapping [FastQC v0.25, PyMOL v2.6] -> quantification [Seurat] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> machine learning [Keras] -> visualisation [ChimeraX v1.8] -> stage not stated [AlphaFold, ArchR, MACS2]

### Bidirectional histone monoaminylation dynamics regulate neural rhythmicity. (Nature 2025)

- DOI: 10.1038/s41586-024-08371-3 | PMCID: PMC11754111 | PMID: 39779849
- Version used: **3.0.0a**
- Evidence: Unique read files for each replicate/timepoint/antibody were merged and used for peak calling using MACS2 (v.3.0.0a6) with the callpeak function and the options -f BAMPE -q 0.05 --broad --broad-cutoff .05, using the corresponding IgG sample as the -c.
- Full pipeline: alignment/mapping [Bowtie2 v2.5.0, STAR v2.7.11b] -> quantification [ImageJ] -> normalisation [ImageJ, deepTools v3.5.1] -> structure determination [PHENIX] -> visualisation [tidyverse v2.0.0] -> stage not stated [BEDTools, Enrichr, HOMER v4.11, HTSeq v2.0.5, MACS2 v3.0.0a, R, SAMtools v1.9]

### Molecular and cellular dynamics of the developing human neocortex. (Nature 2025)

- DOI: 10.1038/s41586-024-08351-7 | PMCID: PMC12589127 | PMID: 39779846
- Version used: **2.2.7**
- Evidence: In total, 243,535 nuclei that passed all of the quality control criteria were included for further analysis. snMultiome data integration, dimensionality reduction, clustering and cell-type identification For ATAC data of snMultiome analysis, open chromatin region peaks were called on individual samples using MACS2 (v.2.2.7) 50 .
- Full pipeline: quality control [MACS2 v2.2.7] -> quantification [CellChat v1.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [GSEA, MACS2 v2.2.7, UMAP, clusterProfiler] -> differential/statistical testing [GSEA, Slingshot v2.6.0, clusterProfiler, limma v3.58.1] -> simulation/modelling [Slingshot v2.6.0] -> stage not stated [ImageJ v1.54, R, SCENIC, Signac v1.10.0, Squidpy v1.2.3, edgeR v3.42.4, scDblFinder]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: ...iners (Corning, 08-771-2); dithiothreitol (Thermo, R0861); EDTA, pH 8.0 RNase-free (Invitrogen, AM9260G); KCl (2 M) RNase-free (Invitrogen, AM9640G); MACS SmartStrainers (Milteny Biotec, 130-098-458); MERSCOPE 500 Gene Imaging kits (Vizgen, 10400006); MERSCOPE 500 Gene Panel (Vizgen, 10400003); MERSCOPE Sample Prep kits (Vizgen, 10400012); N , N , N ′, N ′-tetramethylethylenediamine (Sigma, T7024-...
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### A foundation model of transcription across human cell types. (Nature 2025)

- DOI: 10.1038/s41586-024-08391-z | PMCID: PMC11754112 | PMID: 39779852
- Evidence: For the K562 NEAT-seq and bulk chromatin accessibility data, a more permissive version of peaks was called using MACS2 (ref.
- Full pipeline: alignment/mapping [BEDTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [AlphaFold, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [ColabFold, MACS2, PyTorch, STRING db]

### Precursors of exhausted T cells are pre-emptively formed in acute infection. (Nature 2025)

- DOI: 10.1038/s41586-024-08451-4 | PMCID: PMC12003159 | PMID: 39778709
- Evidence: Cells were counted using a Neubauer counting chamber and a CD90.2 MACS enrichment (Miltenyi) was performed according to the manufacturer’s instructions.
- Full pipeline: read trimming [STAR] -> alignment/mapping [STAR] -> quantification [STAR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSEA, UMAP, edgeR] -> stage not stated [MACS2, Nextflow, R v4.1.0, SAMtools, Seurat v4.0.3, Signac v1.3.0, limma]

### Gliomagenesis mimics an injury response orchestrated by neural crest-like cells. (Nature 2025)

- DOI: 10.1038/s41586-024-08356-2 | PMCID: PMC11821533 | PMID: 39743595
- Evidence: Subsequently, open chromatin peaks were called on the basis of pseudo-bulk replicates of different cell types using MACS2, and differentially accessible regions were identified using a Wilcoxon test implemented in ArchR (false discovery rate < 0.1 and fold change > 1.5).
- Full pipeline: quality control [scDblFinder v1.4.0] -> normalisation [Scanpy] -> dimensionality reduction/clustering [Seurat v4.5, UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Slingshot] -> visualisation [Cytoscape v3.9.1, UMAP, igraph] -> stage not stated [ArchR v1.0.1, CellChat v1.1.3, R, Squidpy v1.3.0]

### Engineered extrachromosomal oncogene amplifications promote tumorigenesis. (Nature 2025)

- DOI: 10.1038/s41586-024-08318-8 | PMCID: PMC11754114 | PMID: 39695225
- Version used: **3.0.0b**
- Evidence: To compare ATAC-seq signals between ecDNA amplicons and corresponding chromosomal regions, bamCoverage in deeptools (v.3.5.3) was used to calculate read counts with 10 kb bin size, and MACS (v.3.0.0b1) was used for peak calling.
- Full pipeline: alignment/mapping [Bowtie2, DESeq2, R, STAR] -> quantification [MACS2 v3.0.0b, deepTools v3.5.3] -> differential/statistical testing [DESeq2, R, STAR] -> stage not stated [CNVkit v0.9.10, fgsea]

### Nucleosome fibre topology guides transcription factor binding to enhancers. (Nature 2025)

- DOI: 10.1038/s41586-024-08333-9 | PMCID: PMC11798873 | PMID: 39695228
- Version used: **2.1.1.20160309**
- Evidence: ChIP–seq peak calling ChIP–seq narrowPeaks and summits showing significant enrichment over input DNA were called using MACS2 (v.2.1.1.20160309) 71 , and were controlled to a q -value (minimum FDR) cut-off of 0.01.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2, FastQC, Nextflow, SAMtools, STAR v2.7] -> quantification [featureCounts] -> differential/statistical testing [DESeq2 v1.22.2, MACS2 v2.1.1.20160309] -> visualisation [ImageJ, PyMOL] -> stage not stated [AlphaFold, BEDTools, HOMER, Picard, R, data.table, ggplot2, pheatmap]

### Central control of dynamic gene circuits governs T cell rest and activation. (Nature 2025)

- DOI: 10.1038/s41586-024-08314-y | PMCID: PMC11754113 | PMID: 39663454
- Version used: **2.2.6**
- Evidence: CXXC1 peaks for visualization were identified using bam files from all AAVS1 -knockout donors for MACS2 (v2.2.6) 78 callpeak -q 0.05 with input samples used to define the background.
- Full pipeline: read trimming [Bowtie2 v2.2.5, Cutadapt v2.10, featureCounts] -> alignment/mapping [Bowtie2 v2.2.5, STAR] -> normalisation [GSVA] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0] -> visualisation [Cytoscape, MACS2 v2.2.6, STRING db, ggplot2 v3.4.1] -> stage not stated [BEDTools v2.30.0, R v4.3.1, SAMtools, Seurat]

### Fetal hepatocytes protect the HSPC genome via fetuin-A. (Nature 2025)

- DOI: 10.1038/s41586-024-08307-x | PMCID: PMC11711094 | PMID: 39633051
- Evidence: After incubation, the cells were washed with MACS buffer and stained with streptavidin-conjugated magnetic beads (558451, BD).
- Full pipeline: quality control [Trim Galore v0.6.7] -> read trimming [BWA] -> alignment/mapping [BWA, Bowtie2 v2.3.5.1, HISAT2 v2.2.1, HTSeq] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.0, HOMER v4.11] -> visualisation [deepTools v3.5.1] -> stage not stated [ImageJ v1.52p, MACS2, Picard v2.25.5, R]

### Evolution of myeloid-mediated immunotherapy resistance in prostate cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08290-3 | PMCID: PMC11779626 | PMID: 39633050
- Evidence: Live cell isolation was done using MACS LS columns (Miltenyi Biotec).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Enrichr] -> stage not stated [ImageJ v2.14.0, MACS2]

### Synthetic GPCRs for programmable sensing and control of cell behaviour. (Nature 2025)

- DOI: 10.1038/s41586-024-08282-3 | PMCID: PMC11666456 | PMID: 39633047
- Evidence: Pearson correlation was used for analyses, as summarized in (h). i , Histograms showing percent of human primary T cells expressing α-mCherry PAGER Gi after lentiviral transduction, on Day 11 before MACS enrichment and on Day 15 after MACS enrichment.
- Full pipeline: quantification [Matplotlib] -> differential/statistical testing [SciPy, seaborn] -> stage not stated [AlphaFold, ImageJ, MACS2, PHENIX, Python]

### Cancer cells impair monocyte-mediated T cell stimulation to evade immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08257-4 | PMCID: PMC7617236 | PMID: 39604727
- Evidence: For PGE 2 analysis, tumours were subsequently digested using a MACS dissociator according to the manufacturer’s protocol in PBS supplemented with 1 mM EDTA and 10 µM indomethacin.
- Full pipeline: normalisation [Enrichr, GSEA] -> dimensionality reduction/clustering [Enrichr, UMAP] -> visualisation [UMAP] -> stage not stated [GSVA, MACS2, R v4.2.2, SCENIC, Seurat v4.3.0, scVelo v0.2.5, velocyto v0.17]

### Chromatin accessibility during human first-trimester neurodevelopment. (Nature 2025)

- DOI: 10.1038/s41586-024-07234-1 | PMCID: PMC12589128 | PMID: 38693260
- Evidence: The pseudobulk aggregates were then downsampled to 25 million fragments and MACS2 53 was used to call peaks using the following parameters: callpeak -f BEDPE -g hs --nomodel --shift 100 --ext 200 --qval 5 × 10 −2 -B –SPMR.
- Full pipeline: quality control [scikit-learn] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, HOMER, LDSC, MACS2, MAGMA, NumPy, scDblFinder]

### Confined migration induces non-lethal DNA damage in developing neurons. (Nature 2026)

- DOI: 10.1038/s41586-026-10648-8 | PMCID: PMC13293896 | PMID: 42310452
- Version used: **1.4.3**
- Evidence: For END-seq, peaks were called using MACS (v.1.4.3) 67 with the parameters: -nolambda, -nomodel and -keep-dup = all (keep all redundant reads) and subsequent analysis were done using bedtools (v.2.31.1) 68 and R (v.4.3.2).
- Full pipeline: read trimming [STAR v2.7.11a] -> alignment/mapping [Bowtie2 v2.5.1, DESeq2 v2.11.40.8, HISAT2 v2.1.0, STAR v2.7.11a, Seurat, featureCounts v2.0.8] -> quantification [DESeq2 v2.11.40.8, ImageJ, featureCounts v2.0.8] -> normalisation [ggplot2] -> differential/statistical testing [DESeq2 v2.11.40.8, featureCounts v2.0.8] -> visualisation [ggplot2] -> stage not stated [BEDTools v2.31.1, MACS2 v1.4.3, R v4.3.2, RepeatMasker, StarDist v0.3.0]

### Dopamine drives persistent remodelling of the maternal brain. (Nature 2026)

- DOI: 10.1038/s41586-026-10509-4 | PMCID: PMC13253353 | PMID: 42162419
- Version used: **2.1.0**
- Evidence: For each group, bigwig files were merged and peak calling was conducted using MACS2 (v2.1.0) with the corresponding merged IgG file as control, and filtered for peaks with FDR < 0.05 100 .
- Full pipeline: quality control [SoupX v1.6.2] -> alignment/mapping [Bowtie2 v2.5.0, kallisto v0.46.1] -> quantification [QuPath, kallisto v0.46.1] -> normalisation [Seurat v4.3.0, WGCNA, deepTools] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP] -> differential/statistical testing [DESeq2 v1.38.3, MACS2 v2.1.0, kallisto v0.46.1] -> stage not stated [HOMER v4.1.1, R v4.3.0, SAMtools v1.9, scDblFinder]

### Ecotypes of triple-negative breast cancer in response to chemotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10469-9 | PMCID: PMC13293894 | PMID: 42129561
- Evidence: To remove red blood cells, the cell pellet was nutated at room temperature for 10 min in 10 ml of 1× MACS red blood cell lysis buffer (MACS no.
- Full pipeline: quantification [Seurat] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, survival (R)] -> visualisation [survival (R)] -> stage not stated [CellChat, GSVA, MACS2, igraph, limma]

### Cytoplasmic competition between separate parental pronuclei in zygotes. (Nature 2026)

- DOI: 10.1038/s41586-026-10417-7 | PMCID: PMC13233321 | PMID: 42056509
- Version used: **2.2.9.1**
- Evidence: H3K4me3 peaks were called MACS2 (v.2.2.9.1) 63 with the parameters ‘-g mm --nomodel --nolambda --broad’.
- Full pipeline: read trimming [Bowtie2 v2.3, edgeR v3.40.2] -> alignment/mapping [BWA v0.7, Bowtie2 v2.3, GATK v4.1.4.1, featureCounts v2.0.0] -> variant calling [BWA v0.7, GATK v4.1.4.1] -> quantification [deepTools v3.5.1, pheatmap] -> normalisation [deepTools v3.5.1, edgeR v3.40.2] -> differential/statistical testing [edgeR v3.40.2] -> visualisation [deepTools v3.5.1, pheatmap] -> stage not stated [BEDTools v2.26.0, MACS2 v2.2.9.1, fastp v0.20.0]

### Mapping convergent regulators of melanoma drug resistance by PerturbFate. (Nature 2026)

- DOI: 10.1038/s41586-026-10367-0 | PMCID: PMC13233327 | PMID: 41986722
- Version used: **3.0.0b**
- Evidence: ATAC peaks were called for each treatment condition with a q -value cutoff of 0.01 using MACS3 (v.3.0.0b3) 54 embedded in SnapATAC2 (v.2.6.1).
- Full pipeline: read trimming [Cutadapt v3.4] -> alignment/mapping [Bowtie2, SAMtools v1.13, STAR v2.7.9a] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [STRING db, UMAP] -> differential/statistical testing [DESeq2 v1.50.2] -> visualisation [deepTools v3.5.1] -> stage not stated [BEDTools v2.30.0, HOMER v5.1, MACS2 v3.0.0b, Monocle, Picard v2.27.4, Python v3.8, R, Seurat v4.2.0, featureCounts v2.0.1, scVelo v0.3.2]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Evidence: The cell pellet was resuspended in MACS buffer (80 µl for 10 7 cells) containing autoMACS Rinsing solution (Miltenyi Biotec, 130-091-222) and 0.5% BSA solution (Miltenyi Biotec, 130-091-376).
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### Single-cell spatiotemporal dissection of the human maternal-fetal interface. (Nature 2026)

- DOI: 10.1038/s41586-026-10316-x | PMCID: PMC13149032 | PMID: 41951740
- Version used: **2.2.7**
- Evidence: For snATAC–seq, open-chromatin peaks were called per sample using MACS2 (v.2.2.7) 63 , and merged into a unified peak set after excluding ENCODE blacklist regions 64 .
- Full pipeline: quantification [QuPath] -> dimensionality reduction/clustering [Cellpose, Seurat, UMAP] -> differential/statistical testing [Enrichr, GSEA] -> visualisation [Cytoscape, UMAP] -> stage not stated [CellChat, HOMER, MACS2 v2.2.7, Signac, Squidpy, freebayes, scDblFinder]

### Synthetic super-enhancers enable precision viral immunotherapy. (Nature 2026)

- DOI: 10.1038/s41586-026-10329-6 | PMCID: PMC13149004 | PMID: 41951744
- Evidence: Technical replicates were merged, and peaks were called using MACS2 with default settings.
- Full pipeline: quantification [ImageJ v2.8] -> normalisation [Seurat] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [ImageJ v2.8] -> stage not stated [BEDTools, HOMER, MACS2, PHENIX, R, SCENIC, scDblFinder]

### AhR inhibition promotes axon regeneration via a stress-growth switch. (Nature 2026)

- DOI: 10.1038/s41586-026-10295-z | PMCID: PMC13216071 | PMID: 41922778
- Evidence: In brief, wild-type 6-week-old C57BL/6 male mice were euthanized using CO 2 and the cortex was isolated and transferred to a MACS C-tube, then dissociated using the Miltenyi gentleMACS octo-dissociator on a preset protocol.
- Full pipeline: read trimming [Bowtie2 v2.4.1] -> alignment/mapping [Bowtie2 v2.4.1] -> quantification [DESeq2, Fiji v2.3.0, ImageJ v2.3.0, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [Enrichr, GSEA v4.3.2, MACS2, SAMtools v1.10, STRING db]

### Dominant clones leverage developmental epigenomic states to drive ependymoma. (Nature 2026)

- DOI: 10.1038/s41586-026-10270-8 | PMCID: PMC13102692 | PMID: 41882368
- Version used: **2.1.1.20160309**
- Evidence: MACS2 (v.2.1.1.20160309) was then used to call peaks on the aligned reads using a P value cutoff of 0.01 (parameters –shift −75 –extsize 150 –nomodel –call-summits –nolambda –keep-dup all − P = 0.01).
- Full pipeline: quality control [SoupX] -> read trimming [Bowtie2 v2.3.4.1] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v2.1.1.20160309, STAR v2.7.0] -> quantification [featureCounts v1.6.3] -> normalisation [Harmony v1.2.3, UMAP] -> dimensionality reduction/clustering [Harmony v1.2.3, UMAP] -> differential/statistical testing [MACS2 v2.1.1.20160309, featureCounts v1.6.3] -> simulation/modelling [Monocle v1.3.7, Slingshot v2.14.0] -> visualisation [Harmony v1.2.3] -> stage not stated [DESeq2, Seurat v5.1.0, Signac v1.14.0, scDblFinder v2.0.4]

### Ectopic NMDAR expression in cancer unmasks germline-encoded autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10278-0 | PMCID: PMC13216075 | PMID: 41882353
- Evidence: Tumour samples were separated into fractions for cryo-embedding in optimal cutting temperature compound (OCT) and single-cell suspensions, which were immediately stored in prechilled MACS Tissue Solution (Miltenyi Biotec, 130-100-008) before dissociation.
- Full pipeline: alignment/mapping [UMAP, edgeR] -> quantification [edgeR] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> structure determination [ChimeraX, PHENIX] -> stage not stated [Fiji, ImageJ, MACS2, QuPath, R, RELION, Seurat]

### In vivo site-specific engineering to reprogram T cells. (Nature 2026)

- DOI: 10.1038/s41586-026-10235-x | PMCID: PMC13083257 | PMID: 41851456
- Evidence: Isolated NK cells were cultured at an initial density of 10 6 cells per ml in NK MACS medium (Miltenyi) supplemented with human platelet lysate (5%, Elite Cell), penicillin–streptomycin (0.5%) and IL-2 (1,000 U ml −1 , Peprotech), as previously described 60 .
- Full pipeline: visualisation [Python] -> stage not stated [MACS2, Slingshot]

### Adaptive evolution of gene regulatory networks in mammalian neocortex. (Nature 2026)

- DOI: 10.1038/s41586-026-10226-y | PMCID: PMC13149332 | PMID: 41851468
- Evidence: Peaks were identified using MACS2 ( SCR_013291 ) 63 .
- Full pipeline: quality control [FastQC, TopHat v1.0.13] -> read trimming [HMMER] -> alignment/mapping [Bowtie2, FastQC, SAMtools v1.16, TopHat v1.0.13] -> dimensionality reduction/clustering [R] -> differential/statistical testing [DESeq2, R] -> stage not stated [BEDTools, ImageJ, MACS2]

### Ageing promotes metastasis via activation of the integrated stress response. (Nature 2026)

- DOI: 10.1038/s41586-026-10216-0 | PMCID: PMC13128440 | PMID: 41813904
- Evidence: 130-096-730, MACS Miltenyi Biotec) and the gentleMACS Octo Dissociator (no.
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bowtie2, HTSeq v0.9.1, SAMtools v1.9, STAR v2.7.9a] -> quantification [HTSeq v0.9.1] -> differential/statistical testing [DESeq2 v1.34.0] -> stage not stated [GSEA, MACS2, Picard v2.18.26, R v4.1.2, STRING db v12.0]

### A mechanism to initiate emergency type 2 myelopoiesis. (Nature 2026)

- DOI: 10.1038/s41586-026-10256-6 | PMCID: PMC13148993 | PMID: 41813898
- Version used: **2.1.2**
- Evidence: Peak calling was performed using MACS2 (v2.1.2) 56 with the following parameters: -q 0.05-nomodel–shift -100-extsize 200.
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2 v2.4.1, featureCounts v2.0.1] -> quantification [DESeq2, featureCounts v2.0.1] -> normalisation [DESeq2, deepTools v3.5.3, featureCounts v2.0.1] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [DESeq2] -> visualisation [PyMOL, deepTools v3.5.3] -> stage not stated [AlphaFold, GSEA, MACS2 v2.1.2, R, SAMtools v1.17, fgsea]

### Cell-free chromatin state tracing reveals disease origin and therapy responses. (Nature 2026)

- DOI: 10.1038/s41586-026-10224-0 | PMCID: PMC13171458 | PMID: 41781618
- Version used: **2.1.1**
- Evidence: Peaks were identified using MACS2 (v.2.1.1) 80 with the parameter setting (--nolambda --nomodel --broad) with different cut-offs for different histone markers.
- Full pipeline: read trimming [Bowtie2 v2.2.9, Cutadapt v1.11] -> alignment/mapping [Bowtie2 v2.2.9, Cutadapt v1.11, SAMtools v1.9] -> normalisation [Seurat v4.3.0] -> dimensionality reduction/clustering [Seurat v4.3.0, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2 v1.44.0, HOMER v4.11] -> simulation/modelling [Monocle v1.2.9] -> stage not stated [BEDTools v2.30.0, MACS2 v2.1.1, Picard v2.2.4, R, XGBoost, ggplot2 v4.3.2, pheatmap v1.0.12]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Version used: **2.2.7.1**
- Evidence: CISs were identified with MACS2 (v.2.2.7.1) ( https://github.com/macs3-project/MACS ) using four window sizes (5, 30, 60 and 100 kb) with genome size, shift and extension parameters adjusted accordingly, and with the nomodel and nolambda options enabled.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Dynamic antigen expression and cytotoxic T cell resistance in HIV reservoir clones. (Nature 2026)

- DOI: 10.1038/s41586-026-10298-w | PMCID: PMC13190302 | PMID: 41735521
- Evidence: Flow cytometry, including HIV Gag staining Cells were stained for viability using the live/dead dye in MACS buffer (PBS + 2% FBS + 1 mM EDTA) following the manufacturer’s instructions and with other surface antibodies depending on the experiment, including: CD3 OKT3 (1:100; BioLegend), CD4 OKT4 (1:100; BioLegend), CD8 SK1 (1:100; BioLegend), CD107a H4A3 (1:100; BioLegend), CD56 HCD56 (1:100; BioLe...
- Full pipeline: normalisation [Seurat v5.1.0, limma] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, fgsea] -> visualisation [limma] -> stage not stated [MACS2]

### Reduced cyclin D3 expression in erythroid cells protects against malaria. (Nature 2026)

- DOI: 10.1038/s41586-026-10110-9 | PMCID: PMC12999499 | PMID: 41708853
- Evidence: CD34 + haematopoietic stem and progenitor cells were isolated from peripheral blood from donors and sorted using CD34 + MACS (Miltenyi) according to the manufacturer’s protocol.
- Full pipeline: alignment/mapping [RSEM, STAR] -> quantification [ImageJ] -> differential/statistical testing [VCFtools v0.1.12b] -> stage not stated [MACS2]

### Individualized mRNA vaccines evoke durable T cell immunity in adjuvant TNBC. (Nature 2026)

- DOI: 10.1038/s41586-025-10004-2 | PMCID: PMC13017525 | PMID: 41708868
- Evidence: PBMCs were resuspended and washed in MACS buffer.
- Full pipeline: alignment/mapping [SAMtools v0.1.19, STAR v2.4.2a, Strelka] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.30, GSEA] -> stage not stated [MACS2, R, Seurat, fgsea v1.20.0]

### Atlas-guided discovery of transcription factors for T cell programming. (Nature 2026)

- DOI: 10.1038/s41586-025-09989-7 | PMCID: PMC13017511 | PMID: 41639465
- Evidence: ATAC-seq peaks were called using the MACS2 (ref.
- Full pipeline: quantification [Seurat] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler v4.0.5, ggplot2] -> differential/statistical testing [DESeq2] -> visualisation [pheatmap, tidyverse] -> stage not stated [GSEA, MACS2, R]

### ZFTA-RELA ependymomas make itaconate to epigenetically drive fusion expression. (Nature 2026)

- DOI: 10.1038/s41586-025-10005-1 | PMCID: PMC13102701 | PMID: 41639460
- Evidence: MACS2 was used to call peaks, filtered using bedtools and converted to bigwigs with UCSC wigtoBigwig 70 , 71 .
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [Picard, RSEM, SAMtools, Trimmomatic v0.39] -> differential/statistical testing [Enrichr, GSEA] -> stage not stated [BEDTools, Bioconductor, MACS2, R v3.6.0]

### Dissecting gene regulatory networks governing human cortical cell fate. (Nature 2026)

- DOI: 10.1038/s41586-025-09997-7 | PMCID: PMC12999477 | PMID: 41565813
- Evidence: Peak calling was performed using MACS2 in each cell type and a consensus peak set was generated using the TGCA iterative peak filtering approach following the pycisTopic workflow.
- Full pipeline: quantification [Scanpy, velocyto] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, MACS2, Monocle, SCENIC, scVelo]

### Convergent evolution of scavenger cell development at brain borders. (Nature 2026)

- DOI: 10.1038/s41586-025-10003-3 | PMCID: PMC12999481 | PMID: 41565812
- Evidence: Using ArchR 92 v.1.0.2, the ArchR object shared by the original authors was subset to only include cell types of interest (VEC, VEC_02_03, LEC, arterial EC, endocardium and muLEC) and pseudo replicates and peak calling using MACS2 (ref.
- Full pipeline: quality control [FastQC, MultiQC] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [Seurat, UMAP] -> differential/statistical testing [Python v3.6, scDblFinder v1.12] -> visualisation [ggplot2, ggpubr v0.4.0] -> stage not stated [ArchR, ImageJ, MACS2, R, Slingshot, velocyto]

### Microbiota-induced T cell plasticity enables immune-mediated tumour control. (Nature 2026)

- DOI: 10.1038/s41586-025-09913-z | PMCID: PMC12960244 | PMID: 41535459
- Evidence: Cells were then washed three times with MACS buffer.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [AlphaFold, MACS2, Seurat v5.1.0]

### Stress controls heterochromatin inheritance via histone H3 ubiquitylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09899-8 | PMCID: PMC12916305 | PMID: 41501458
- Evidence: Bedgraphs of ChIP enrichment over input were produced using the MACS2 (ref.
- Full pipeline: read trimming [BWA, STAR, fastp] -> alignment/mapping [BWA, STAR, fastp] -> stage not stated [BCFtools, MACS2, Picard, SAMtools, SnpEff]

### Bidirectional CRISPR screens decode a GLIS3-dependent fibrotic cell circuit. (Nature 2026)

- DOI: 10.1038/s41586-025-09907-x | PMCID: PMC12820784 | PMID: 41501466
- Evidence: The retained high-quality alignment results were used to call narrow peaks using MACS2 (refs.
- Full pipeline: quality control [FastQC, Trim Galore] -> alignment/mapping [MACS2] -> quantification [QuPath v0.6.0] -> normalisation [BEDTools, Scanpy, UMAP] -> dimensionality reduction/clustering [UMAP, scikit-learn v0.22] -> differential/statistical testing [DESeq2, R, edgeR] -> visualisation [BEDTools] -> stage not stated [FSL, GSEA, HOMER, Picard, SAMtools, featureCounts, igraph]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: We then used MACS3 to generate P -value tracks as well as peaks for CUT&RUN data.
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: The isolated PHH preparations (either from fresh tissue from Dresden or Leipzig Hospital or commercially available frozen hepatocytes) were enriched for both EpCAM-negative (hepatocytes) and EpCAM-positive (cholangiocytes) by MACS using an anti-human CD326 antibody (BioLegend) and anti-biotin microbeads (Ultra Pure, Miltenyi) following the manufacturer’s instructions.
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### Spatiotemporal cellular map of the developing human reproductive tract. (Nature 2026)

- DOI: 10.1038/s41586-025-09875-2 | PMCID: PMC12893920 | PMID: 41407855
- Evidence: Cell-type-specific peaks were called using MACS2 94 as implemented in the pycistopic workflow 95 .
- Full pipeline: quantification [Scanpy, Squidpy] -> normalisation [GSEA] -> dimensionality reduction/clustering [Seurat, SoupX, UMAP] -> differential/statistical testing [Scanpy, Seurat, Slingshot] -> simulation/modelling [Slingshot] -> visualisation [UMAP] -> stage not stated [AnnData, ArchR, Cellpose, MACS2, Nextflow, PHENIX, SCENIC, scDblFinder]

### Lesion-remote astrocytes govern microglia-mediated white matter repair. (Nature 2026)

- DOI: 10.1038/s41586-025-09887-y | PMCID: PMC12823418 | PMID: 41407858
- Evidence: Following dissociation, samples were filtered through a 70-μm strainer, and myelin was depleted using 120 μl of Myelin removal beads II (Miltenyi Biotech) in 1,000 μl of MACS Buffer (0.5% BSA, 2 mM EDTA in PBS) using LS columns (modified from PMID: 26919701).
- Full pipeline: alignment/mapping [STAR] -> normalisation [ImageJ, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [Bioconductor, edgeR] -> stage not stated [Enrichr, MACS2, emmeans, scDblFinder, scikit-learn]

### Causal modelling of gene effects from regulators to programs to traits. (Nature 2026)

- DOI: 10.1038/s41586-025-09866-3 | PMCID: PMC12893915 | PMID: 41372418
- Version used: **3.0.3**
- Evidence: Specifically, we trimmed the adapter sequence with TrimGalore (v0.5.0) 72 , aligned to the hg19 reference with Bowtie2 (v2.3.4.1) 73 , filtered duplicates with MACS3 (v3.0.3) 74 and called narrow peaks with the MACS3 (v3.0.3) hmmratac command.
- Full pipeline: read trimming [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> alignment/mapping [Bowtie2 v2.3.4.1, MACS2 v3.0.3, Trim Galore v0.5.0] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [LDSC, PLINK v1.90b, XGBoost] -> stage not stated [BEDTools v2.30.0, REGENIE, VEP]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Version used: **2.1.2**
- Evidence: MACS2 (v.2.1.2) was used to perform peak calling over input ChIP–seq samples; only peaks with a q -value < 0.01 were retained.
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### Architecture of the neutrophil compartment. (Nature 2026)

- DOI: 10.1038/s41586-025-09807-0 | PMCID: PMC12823425 | PMID: 41339555
- Version used: **2.2.9.1**
- Evidence: The CallPeaks() function used MACS2 (v.2.2.9.1) 70 to run.
- Full pipeline: quality control [Signac v1.14.0, UMAP] -> read trimming [Cutadapt v4.9] -> alignment/mapping [Python, SAMtools] -> quantification [ImageJ, RSEM v1.3.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.20.1, limma v3.32.2] -> stage not stated [AnnData, DESeq2 v1.30.1, GSEA, MACS2 v2.2.9.1, Monocle, R, Seurat v4.0.5, StarDist, igraph, scVelo, velocyto v0.17.17]

### Sustained HIV-1 remission after heterozygous CCR5Δ32 stem cell transplantation. (Nature 2026)

- DOI: 10.1038/s41586-025-09893-0 | PMCID: PMC12916306 | PMID: 41326734
- Evidence: Isolation of CD34 + (from bone marrow) and CD3 + (from peripheral blood) cells was performed using a standard MACS technique (Miltenyi Biotec).
- Full pipeline: alignment/mapping [MUSCLE v3.8.155] -> dimensionality reduction/clustering [R v4.4.1, UMAP] -> stage not stated [MACS2, Seurat]

### NSD2 targeting reverses plasticity and drug resistance in prostate cancer. (Nature 2026)

- DOI: 10.1038/s41586-025-09727-z | PMCID: PMC12727498 | PMID: 41299174
- Version used: **2.2.8**
- Evidence: Peak calling was performed using SEACR (v.1.3) or MACS2 (v.2.2.8) with IgG input as control.
- Full pipeline: read trimming [Cutadapt v3.6] -> alignment/mapping [Cufflinks v2.2.1, Cutadapt v3.6, HISAT2 v2.1.0, TopHat v2.0.7, featureCounts v1.6.1] -> quantification [Cufflinks v2.2.1, R v4.1.2] -> normalisation [GSEA] -> differential/statistical testing [DESeq2 v1.28.0, GSEA, Seurat v4.1.3] -> visualisation [deepTools v3.5.5] -> stage not stated [BEDTools v2.27.1, ImageJ, MACS2 v2.2.8, QuPath v0.5.1, Scanpy v1.9.1, limma, scDblFinder v0.2.2, seaborn]

### Inhibitory PD-1 axis maintains high-avidity stem-like CD8&lt;sup&gt;+&lt;/sup&gt; T cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09440-x | PMCID: PMC12727512 | PMID: 41299179
- Evidence: Tissue preparation for flow cytometry Lymphocytes were isolated from lymph nodes and spleens and made into single-cell suspensions using a syringe plunger and 100 µm or 70 µm cell strainers (MACS SmartStrainer, Miltenyi Biotec).
- Full pipeline: quantification [seaborn] -> normalisation [Matplotlib, scikit-learn] -> dimensionality reduction/clustering [Matplotlib, scikit-learn] -> visualisation [Matplotlib, scikit-image, scikit-learn, seaborn] -> stage not stated [Cellpose, MACS2, napari]

### MAPK-driven epithelial cell plasticity drives colorectal cancer therapeutic resistance. (Nature 2026)

- DOI: 10.1038/s41586-025-09916-w | PMCID: PMC12916511 | PMID: 41286180
- Evidence: The homogenized tissue was filtered through a 30-µm strainer (130-098-458, MACS SmartStrainer 30 µm) and centrifuged at 850 rcf × 5 min.
- Full pipeline: alignment/mapping [featureCounts v1.6.4] -> normalisation [DESeq2 v1.42.1] -> dimensionality reduction/clustering [UMAP, scikit-learn v1.7.2] -> differential/statistical testing [ggplot2 v3.5.1, ggpubr v0.6.0] -> visualisation [AnnData v0.11.4, Matplotlib v3.10, NumPy v2.2.6, SciPy v1.16.0, scikit-learn v1.7.2, seaborn v0.13] -> stage not stated [ComplexHeatmap v2.18.0, GSVA v1.50.5, MACS2, QuPath, R v4.5.1, Scanpy v1.11.2, Seurat]

### Lymph node environment drives FSP1 targetability in metastasizing melanoma. (Nature 2026)

- DOI: 10.1038/s41586-025-09709-1 | PMCID: PMC12779575 | PMID: 41193799
- Evidence: Reads were mapped to mm10 (hisat2), duplicates removed (Picard) and peaks were called using MACS2.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [FastQC, Trimmomatic] -> alignment/mapping [HISAT2, MACS2, Picard, Salmon v0.7.2] -> quantification [QuPath v0.5, Salmon v0.7.2] -> dimensionality reduction/clustering [igraph] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER]

### Parity and lactation induce T-cell-mediated breast cancer protection. (Nature 2026)

- DOI: 10.1038/s41586-025-09713-5 | PMCID: PMC12779547 | PMID: 41115453
- Evidence: Adoptive transfer of transgenic T cells OT-I cells were isolated using the negative immunomagnetic cell-separation method, MACS (Stem Cell Technologies), from the spleen of WT OT-I CD45.2 donor mice.
- Full pipeline: read trimming [HISAT2 v2.2] -> alignment/mapping [HISAT2 v2.2, HTSeq v2.0.3] -> quantification [HTSeq v2.0.3, QuPath v0.6] -> normalisation [edgeR] -> dimensionality reduction/clustering [Harmony v1.2.3, Seurat v5.2.1, UMAP] -> differential/statistical testing [GSEA, R, fgsea v1.30.0, limma v3.60.3] -> visualisation [Harmony v1.2.3, Seurat v5.2.1] -> stage not stated [MACS2, emmeans, ggplot2 v3.5.1, tidyverse v1.1.2]

### Acute Csk inhibition hinders B cell activation by constraining the PI3 kinase pathway. (PNAS 2021)

- DOI: 10.1073/pnas.2108957118 | PMCID: PMC8639343 | PMID: 34675079
- Evidence: Primary B cells were isolated from spleen and lymph node cell suspensions using MACS B cell isolation kits (130-090-862; Miltenyi Biotec).
- Full pipeline: stage not stated [ImageJ, MACS2]

### Trained innate immunity, long-lasting epigenetic modulation, and skewed myelopoiesis by heme. (PNAS 2021)

- DOI: 10.1073/pnas.2102698118 | PMCID: PMC8545490 | PMID: 34663697
- Evidence: MACS2 was used to call the peaks.
- Full pipeline: alignment/mapping [SAMtools] -> normalisation [R] -> dimensionality reduction/clustering [ArchR v0.9.5, UMAP] -> differential/statistical testing [R] -> visualisation [ArchR v0.9.5] -> stage not stated [HOMER, MACS2, Seurat]

### Early-life midazolam exposure persistently changes chromatin accessibility to impair adult hippocampal neurogenesis and cognition. (PNAS 2021)

- DOI: 10.1073/pnas.2107596118 | PMCID: PMC8463898 | PMID: 34526402
- Evidence: Open chromatin regions were analyzed using MACS software.
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2, SAMtools v0.1.19]

### Coronavirus induces diabetic macrophage-mediated inflammation via SETDB2. (PNAS 2021)

- DOI: 10.1073/pnas.2101071118 | PMCID: PMC8463849 | PMID: 34479991
- Evidence: For ex vivo infections, freshly isolated splenic macrophages via MACS were counted and plated (5 × 10 5 ) per 24 wells, and infected with MHV-A59 at an MOI of 0.5 in the FBS-free infection media described.
- Full pipeline: normalisation [ImageJ] -> stage not stated [MACS2]

### Disabling de novo DNA methylation in embryonic stem cells allows an illegitimate fate trajectory. (PNAS 2021)

- DOI: 10.1073/pnas.2109475118 | PMCID: PMC8463881 | PMID: 34518230
- Evidence: Peaks were called with MACS2 and parameters “–nomodel –shift -55 –extsize 110 –broad -g mm –broad-cutoff 0.1”.
- Full pipeline: alignment/mapping [Picard] -> dimensionality reduction/clustering [Monocle v2.14, UMAP] -> differential/statistical testing [DESeq2, Monocle v2.14, R, edgeR] -> simulation/modelling [Monocle v2.14] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat v3.1.5, Trim Galore]

### The p53 transcriptional response across tumor types reveals core and senescence-specific signatures modulated by long noncoding RNAs. (PNAS 2021)

- DOI: 10.1073/pnas.2025539118 | PMCID: PMC8346867 | PMID: 34326251
- Evidence: Peaks of p53 binding were identified using MACS2 ( 49 ) using pooled negative control samples for the respective tumor type.
- Full pipeline: alignment/mapping [StringTie, TopHat] -> normalisation [DESeq2] -> stage not stated [BEDTools, GSEA, MACS2]

### VLM catecholaminergic neurons control tumor growth by regulating CD8<sup>+</sup> T cells. (PNAS 2021)

- DOI: 10.1073/pnas.2103505118 | PMCID: PMC8285964 | PMID: 34260392
- Evidence: The single cells were then incubated in MACS buffer (PBS supplemented with 2% FBS and 1 mM ethylenediaminetetraacetic acid [EDTA]) containing 10 µg/mL CD16/CD32 antibody (2.4G2, BD PharMingen) for 30 min at 4 °C and then stained with the antibodies.
- Full pipeline: stage not stated [MACS2]

### Dynamic chromatin regulatory landscape of human CAR T cell exhaustion. (PNAS 2021)

- DOI: 10.1073/pnas.2104758118 | PMCID: PMC8325267 | PMID: 34285077
- Evidence: Peaks were called using MACS2 on Tn5-corrected insertion sites.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [BEDTools, DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, MACS2, Picard, R]

### Hypoimmune induced pluripotent stem cell-derived cell therapeutics treat cardiovascular and pulmonary diseases in immunocompetent allogeneic mice. (PNAS 2021)

- DOI: 10.1073/pnas.2022091118 | PMCID: PMC8285900 | PMID: 34244428
- Evidence: Cells then underwent MACS purification using negative selection with anti-CD15 mAb-coated magnetic microbeads (Miltenyi).
- Full pipeline: stage not stated [MACS2]

### &lt;i&gt;ARABIDOPSIS THALIANA HOMEOBOX GENE 1&lt;/i&gt; controls plant architecture by locally restricting environmental responses. (PNAS 2021)

- DOI: 10.1073/pnas.2018615118 | PMCID: PMC8092594 | PMID: 33888582
- Evidence: ChIP was performed as described previously ( 63 ), except that for ChIP-qPCR the IP buffer included salmon sperm (Sigma; DNA 0.5 mg/mL) and incubation with anti-GFP µMACS microbeads was for 1 h on ice.
- Full pipeline: differential/statistical testing [Matplotlib, NumPy, SciPy] -> stage not stated [MACS2]

### Brd4-bound enhancers drive cell-intrinsic sex differences in glioblastoma. (PNAS 2021)

- DOI: 10.1073/pnas.2017148118 | PMCID: PMC8072233 | PMID: 33850013
- Evidence: Significant calling card peaks or Brd4-enriched enhancer sites were identified by a modified version of the previously described algorithm, which also has similarities to the MACS2 ChIP-seq peak caller ( 43 ).
- Full pipeline: alignment/mapping [Bowtie2 v2.3.4.3, HTSeq v0.11.1] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2]

### Genetic deletion of Nox4 enhances cancerogen-induced formation of solid tumors. (PNAS 2021)

- DOI: 10.1073/pnas.2020152118 | PMCID: PMC7980388 | PMID: 33836590
- Evidence: Fibrosarcoma cells were isolated using the tumor dissociation kit for mouse and the gentle MACS Dissociator from Miltenyi Biotec, following the manufacturer’s instructions.
- Full pipeline: stage not stated [MACS2]

### Lineage-specific selection and the evolution of virulence in the <i>Candida</i> clade. (PNAS 2021)

- DOI: 10.1073/pnas.2016818118 | PMCID: PMC8000421 | PMID: 33723044
- Evidence: Peaks were called using MACS2 ( 65 ) with default settings and C. dubliniensis peaks were lifted over to the C. albicans genome coordinates.
- Full pipeline: differential/statistical testing [edgeR] -> stage not stated [MACS2, R]

### <i>Drosophila</i> Fezf functions as a transcriptional repressor to direct layer-specific synaptic connectivity in the fly visual system. (PNAS 2021)

- DOI: 10.1073/pnas.2025530118 | PMCID: PMC8020669 | PMID: 33766917
- Version used: **2.1.1**
- Evidence: To call the peaks we used MACS2 v2.1.1 ( 42 ) with parameters “-g dm–nomodel–nolambda–keep-dup all,” and peaks were filtered based on default settings and FDR < 0.05.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2] -> quantification [Bioconductor] -> differential/statistical testing [DESeq2, MACS2 v2.1.1] -> stage not stated [Fiji, ImageJ]

### CD47 blockade reduces the pathologic features of experimental cerebral malaria and promotes survival of hosts with <i>Plasmodium</i> infection. (PNAS 2021)

- DOI: 10.1073/pnas.1907653118 | PMCID: PMC7980459 | PMID: 33836556
- Evidence: Human pRBCs were purified from type O donor blood infected in vitro with P. falciparum 3D7HT-GFP (courtesy of the Yeh laboratory at Stanford University, California, strain from BEI resources) using magnetic isolation with MACS columns (Miltenyi Biotech).
- Full pipeline: stage not stated [MACS2]

### Mitochondrial metabolism is essential for invariant natural killer T cell development and function. (PNAS 2021)

- DOI: 10.1073/pnas.2021385118 | PMCID: PMC8020658 | PMID: 33753493
- Evidence: Splenic CD4 + T cells from B6 mice and iNKT cells from Vα14Tg mice were positively selected using MACS (Miltenyi).
- Full pipeline: alignment/mapping [STAR] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [MACS2]

### Massively parallel discovery of human-specific substitutions that alter enhancer activity. (PNAS 2021)

- DOI: 10.1073/pnas.2007049118 | PMCID: PMC7812811 | PMID: 33372131
- Evidence: Reads were mapped using Bowtie2 (option -X 2000) and open chromatin regions were called using MACS2 (options -B–nomodel–shift -25–extsize 50).
- Full pipeline: alignment/mapping [Bowtie2, MACS2]

### Orthosteric-allosteric dual inhibitors of PfHT1 as selective antimalarial agents. (PNAS 2021)

- DOI: 10.1073/pnas.2017749118 | PMCID: PMC7826358 | PMID: 33402433
- Evidence: Late-stage Dd2 parasites in RBCs were magnetically purified from 5% sorbitol-synchronized cultures using MACS LD columns (Miltenyi Biotec) and seeded at 0.8 million RBCs per well in a Seahorse miniplate, which was precoated with Cell-Tak cell and tissue adhesive (Corning).
- Full pipeline: structure determination [PHENIX] -> stage not stated [CCP4, MACS2]

### Quality assessment and refinement of chromatin accessibility data using a sequence-based predictive model. (PNAS 2022)

- DOI: 10.1073/pnas.2212810119 | PMCID: PMC9907136 | PMID: 36508674
- Evidence: Specifically, we ran MACS2 ( 56 ) with no restricted model (--nomodel) using paired-end read pairs with MAPQ >30.
- Full pipeline: quality control [Jupyter] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [LDSC, MACS2, featureCounts]

### Transcriptional control of cone photoreceptor diversity by a thyroid hormone receptor. (PNAS 2022)

- DOI: 10.1073/pnas.2209884119 | PMCID: PMC9894165 | PMID: 36454759
- Version used: **2.2.7.1**
- Evidence: ChAP-seq peaks and ATAC-seq peaks were called using MACS2 (v2.2.7.1) with false discovery rate (FDR) q < 0.01.
- Full pipeline: alignment/mapping [STAR v2.7.3a] -> normalisation [deepTools] -> differential/statistical testing [DESeq2, MACS2 v2.2.7.1, edgeR] -> visualisation [deepTools]

### Tumor-targeted delivery of a STING agonist improvescancer immunotherapy. (PNAS 2022)

- DOI: 10.1073/pnas.2214278119 | PMCID: PMC9894229 | PMID: 36442099
- Evidence: All the following staining steps were done in MACS buffer (PBS + 2% FBS+ 1 mM EDTA).
- Full pipeline: stage not stated [MACS2]

### Synthetic nanobodies as tools to distinguish IgG Fc glycoforms. (PNAS 2022)

- DOI: 10.1073/pnas.2212658119 | PMCID: PMC9860306 | PMID: 36409896
- Evidence: Yeast was incubated with microbeads for 20 min at 4°C, washed in cold staining buffer, and depleted of G2F-binders on a MACS LS column (Miltenyi).
- Full pipeline: stage not stated [MACS2]

### Modulation of cGAS-STING signaling by PPARα in a mouse model of ischemia-induced retinopathy. (PNAS 2022)

- DOI: 10.1073/pnas.2208934119 | PMCID: PMC9860285 | PMID: 36409895
- Evidence: Briefly, fresh retinas were digested with collagenase D to generate single cell suspension, which was further incubated with an anti-CD11b antibody conjugated with magnetic MACS beads (Miltenyi Biotec, Cambridge, MA) for 30 min at 4°C.
- Full pipeline: quantification [ImageJ] -> stage not stated [MACS2]

### Two intrinsic timing mechanisms set start and end times for dendritic arborization of a nociceptive neuron. (PNAS 2022)

- DOI: 10.1073/pnas.2210053119 | PMCID: PMC9659368 | PMID: 36322763
- Evidence: Peaks were called using MACS2 ( 69 ) and visualized using IGV.
- Full pipeline: quality control [BWA, SAMtools] -> alignment/mapping [BWA, SAMtools] -> quantification [ImageJ] -> visualisation [MACS2]

### Genome-wide chromatin accessibility analysis unveils open chromatin convergent evolution during polyploidization in cotton. (PNAS 2022)

- DOI: 10.1073/pnas.2209743119 | PMCID: PMC9636936 | PMID: 36279429
- Version used: **2.1.4**
- Evidence: DHSs were identified by using the MACS2 v.2.1.4 ( 96 ) with the parameters “-f BAMPE –broad –nomodel –keep-dup all”.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools v1.9] -> quantification [Cufflinks v2.2.1, deepTools v3.1.3] -> normalisation [Cufflinks v2.2.1, deepTools v3.1.3] -> visualisation [deepTools v3.1.3] -> stage not stated [BEDTools v2.29.2, DESeq2, HOMER v4.11, MACS2 v2.1.4, OrthoFinder v2.3.8]

### Disruption of proteostasis causes IRE1 mediated reprogramming of alveolar epithelial cells. (PNAS 2022)

- DOI: 10.1073/pnas.2123187119 | PMCID: PMC9618079 | PMID: 36252035
- Evidence: These three gene lists were queried for XBP-1 MACS2 binding scores on The Signaling Pathways Project database ( www.signalingpathways.org/ ), which utilized the published mouse XBP-1 ChIP-seq analysis from Argemí et al.
- Full pipeline: quantification [Fiji v1.8.0, ImageJ v1.8.0] -> dimensionality reduction/clustering [Slingshot, UMAP] -> simulation/modelling [Slingshot] -> stage not stated [MACS2]

### Polycomb group (PcG) proteins prevent the assembly of abnormal synaptonemal complex structures during meiosis. (PNAS 2022)

- DOI: 10.1073/pnas.2204701119 | PMCID: PMC9586294 | PMID: 36215502
- Evidence: ( D ) Heatmap of indicated ChIP signal from whole ovaries showing 6 kb encompassing all Pho and Sfmbt peaks called by MACS2.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR, deepTools] -> normalisation [R, deepTools, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [MACS2]

### Origin recognition complex harbors an intrinsic nucleosome remodeling activity. (PNAS 2022)

- DOI: 10.1073/pnas.2211568119 | PMCID: PMC9586268 | PMID: 36215487
- Evidence: ( 19 ) (SRR034475 and SRR034476), aligned it to the yeast genome (version Scer3) with bowtie2, and used MACS2 to identify the peaks (threshold: effective P = 0.01).
- Full pipeline: alignment/mapping [Bowtie2, MACS2]

### Conservation at the uterine-placental interface. (PNAS 2022)

- DOI: 10.1073/pnas.2210633119 | PMCID: PMC9565169 | PMID: 36191208
- Evidence: Following enzymatic digestion, cellular debris was removed using MACS Debris Removal Solution (130-109-398, Miltenyi Biotec).
- Full pipeline: quality control [R, Seurat v4.1.0] -> dimensionality reduction/clustering [Enrichr, UMAP, clusterProfiler v3.16.1] -> visualisation [UMAP] -> stage not stated [CellPhoneDB, MACS2]

### Ectopic expression of meiotic cohesin generates chromosome instability in cancer cell line. (PNAS 2022)

- DOI: 10.1073/pnas.2204071119 | PMCID: PMC9549395 | PMID: 36179046
- Version used: **2.2**
- Evidence: The initial peak calling was done using MACS2.2 ( 130 , 131 ) and was limited to 21 M. fascicularis female chromosomes.
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, clusterProfiler] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [BEDTools, MACS2 v2.2, RepeatMasker]

### Highly sensitive single-cell chromatin accessibility assay and transcriptome coassay with METATAC. (PNAS 2022)

- DOI: 10.1073/pnas.2206450119 | PMCID: PMC9546615 | PMID: 36161934
- Evidence: Chromatin accessible peaks were called by addReproduciblePeakSet function using MACS2 ( 60 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, HTSeq v0.11.2, Picard] -> dimensionality reduction/clustering [Seurat, UMAP] -> visualisation [UMAP] -> stage not stated [ArchR, BEDTools, MACS2, Python]

### Rpd3 regulates single-copy origins independently of the rDNA array by opposing Fkh1-mediated origin stimulation. (PNAS 2022)

- DOI: 10.1073/pnas.2212134119 | PMCID: PMC9546531 | PMID: 36161938
- Version used: **1.4.2**
- Evidence: BrdU peaks were called by MACS 1.4.2 with no-model mode ( P < 0.01).
- Full pipeline: stage not stated [BEDTools v2.25.0, MACS2 v1.4.2]

### Opportunistic binding of EcR to open chromatin drives tissue-specific developmental responses. (PNAS 2022)

- DOI: 10.1073/pnas.2208935119 | PMCID: PMC9546573 | PMID: 36161884
- Evidence: Peak calling was performed using MACS (), using immunoglobulin G samples as controls.
- Full pipeline: normalisation [DESeq2] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2]

### TGFB2-AS1 inhibits triple-negative breast cancer progression via interaction with SMARCA4 and regulating its targets <i>TGFB2</i> and <i>SOX2</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2117988119 | PMCID: PMC9522332 | PMID: 36126099
- Version used: **2.1.2**
- Evidence: Peaks were called with MACS2 version 2.1.2.
- Full pipeline: alignment/mapping [Bowtie2 v2.3.5] -> stage not stated [GSEA, Galaxy, MACS2 v2.1.2]

### A scalable framework for the discovery of functional helicase substrates and helicase-driven regulatory switches. (PNAS 2022)

- DOI: 10.1073/pnas.2209608119 | PMCID: PMC9499579 | PMID: 36095194
- Evidence: The log 10 FE profiles were obtained with MACS2 bdgcmp v2.1.1 using the R 10 + or R 10 − sample as input and R 0 sample as control.
- Full pipeline: quality control [Cutadapt v1.15, FastQC v0.11.5] -> read trimming [Cutadapt v1.15, FastQC v0.11.5] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [Galaxy, MACS2, Python]

### Different classes of genomic inserts contribute to human antibody diversity. (PNAS 2022)

- DOI: 10.1073/pnas.2205470119 | PMCID: PMC9457163 | PMID: 36037353
- Evidence: For T cell analysis, PBMCs were enriched by MACS using anti-CD3 microbeads (Miltenyi Biotec, Cat#130-050-101).
- Full pipeline: quality control [FastQC] -> read trimming [R, Trim Galore, Trimmomatic] -> alignment/mapping [R, Trimmomatic] -> stage not stated [BEDTools, MACS2, ggplot2]

### Brain endothelial STING1 activation by <i>Plasmodium</i>-sequestered heme promotes cerebral malaria via type I IFN response. (PNAS 2022)

- DOI: 10.1073/pnas.2206327119 | PMCID: PMC9457060 | PMID: 36037380
- Evidence: The pellet resulting from centrifugation at 5,630 × g was designated fraction 1 (Fr1) and the supernatant was further centrifuged at 20,000 × g producing a pellet, “–Fr1.” Fr1 was resuspended in PBS and passed through a LS magnetic exclusion column according to the manufacturer’s instructions (MACS Milteny Biotec).
- Full pipeline: stage not stated [MACS2]

### Hippo signaling cofactor, WWTR1, at the crossroads of human trophoblast progenitor self-renewal and differentiation. (PNAS 2022)

- DOI: 10.1073/pnas.2204069119 | PMCID: PMC9457323 | PMID: 36037374
- Evidence: HLAG + EVTs were depleted from the cell suspension by immune-purification using HLA-G Phycoerythrin-labeled antibodies (Exbio; Clone MEM-G/9, 1P-292-C100), PE MACS beads (Miltenyi Biotec; 130–048-801), and MACS MS columns (Miltenyi Biotec; 130–042-201).
- Full pipeline: quality control [FastQC] -> stage not stated [GSEA, MACS2]

### 3D chromatin remodeling potentiates transcriptional programs driving cell invasion. (PNAS 2022)

- DOI: 10.1073/pnas.2203452119 | PMCID: PMC9457068 | PMID: 36037342
- Evidence: We identified that a majority of CTCF binding sites, 38,775 out of the 44,802 peaks called by MACS2 ( 34 ), were left unchanged between the CTL and CTCF +/− MCF10A cells.
- Full pipeline: quality control [R] -> stage not stated [DESeq2, GSEA, ImageJ, MACS2]

### Long noncoding RNA &lt;i&gt;CHROMR&lt;/i&gt; regulates antiviral immunity in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2210321119 | PMCID: PMC9477407 | PMID: 36001732
- Evidence: Peaks were called for each probe set and replicate via the callpeak function from MACS2 ( 53 ) relative to the input from the same replicate.
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA, STAR, Trimmomatic, featureCounts] -> quantification [STAR, featureCounts] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [Enrichr, HOMER, MACS2, R]

### Regulators of early maize leaf development inferred from transcriptomes of laser capture microdissection (LCM)-isolated embryonic leaf cells. (PNAS 2022)

- DOI: 10.1073/pnas.2208795119 | PMCID: PMC9436337 | PMID: 36001691
- Version used: **2.1.2**
- Evidence: GST-only control using MACS2 (version 2.1.2) ( 59 ) with q value < 0.05.
- Full pipeline: quality control [Bowtie2, TopHat v2.0.14] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bowtie2, SAMtools, TopHat v2.0.14] -> quantification [Cufflinks v2.2.1] -> stage not stated [Cytoscape v3.4.0, MACS2 v2.1.2, R, WGCNA]

### The amino acid sensor GCN2 controls red blood cell clearance and iron metabolism through regulation of liver macrophages. (PNAS 2022)

- DOI: 10.1073/pnas.2121251119 | PMCID: PMC9436309 | PMID: 35994670
- Evidence: Peaks were called using MACS (Model-based Analysis of ChIP-Seq) v2.1.0 software and default parameters (mfold = [5,50]; FDR cutoff = 0.05, –nomodel) using sequenced libraries of either WT or GCN2 KO input DNA as control ( 70 ).
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BWA v0.7.12] -> differential/statistical testing [MACS2] -> stage not stated [HOMER, R, Seurat v3.0.1]

### Identification of basal complex protein that is essential for maturation of transmission-stage malaria parasites. (PNAS 2022)

- DOI: 10.1073/pnas.2204167119 | PMCID: PMC9407223 | PMID: 35972967
- Evidence: PfBLEB-smV5 Tet gametocytes were induced with or without ATc as described above and purified using MACS magnetic columns 5 or 8 d postinduction.
- Full pipeline: stage not stated [ImageJ, MACS2]

### Adrenergic receptor signaling induced by Klf15, a regulator of regeneration enhancer, promotes kidney reconstruction. (PNAS 2022)

- DOI: 10.1073/pnas.2204338119 | PMCID: PMC9388080 | PMID: 35939709
- Version used: **2.2.6**
- Evidence: For differential ATAC-seq peaks, narrow peaks were obtained using MACS2 (2.2.6).
- Full pipeline: differential/statistical testing [MACS2 v2.2.6, edgeR v3.32.1, featureCounts v2.0.1] -> stage not stated [BEDTools v2.30.0, HOMER]

### An anti-CTLA-4 heavy chain-only antibody with enhanced T&lt;sub&gt;reg&lt;/sub&gt; depletion shows excellent preclinical efficacy and safety profile. (PNAS 2022)

- DOI: 10.1073/pnas.2200879119 | PMCID: PMC9371702 | PMID: 35925889
- Evidence: Naive CD4 + T cells were isolated from human PBMCs using the MACS human naive CD4 T-cell isolation kit II (Miltenyi Biotec, 130-094-131).
- Full pipeline: stage not stated [MACS2, PyMOL]

### Microenvironmental sensing by fibroblasts controls macrophage population size. (PNAS 2022)

- DOI: 10.1073/pnas.2205360119 | PMCID: PMC9371703 | PMID: 35930670
- Evidence: Enriched ChIP regions were identified using MACS2 ( 80 ) using the options “'-f BAMPE –bw 200 -B -g mm”.
- Full pipeline: alignment/mapping [kallisto] -> stage not stated [MACS2, Picard]

### Wnt signaling regulates hepatocyte cell division by a transcriptional repressor cascade. (PNAS 2022)

- DOI: 10.1073/pnas.2203849119 | PMCID: PMC9335208 | PMID: 35867815
- Evidence: Peaks were called using MACS2 as previously described ( 68 – 70 ) with modifications from subcommands.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools] -> stage not stated [Fiji, ImageJ, MACS2]

### A mechanism of self-lipid endocytosis mediated by the receptor Mincle. (PNAS 2022)

- DOI: 10.1073/pnas.2120489119 | PMCID: PMC9335232 | PMID: 35867828
- Evidence: Isolation of mouse brain endothelial cells was performed using MACS technology ( 39 ) or using puromycin selection according to a previously published method ( 40 ).
- Full pipeline: quantification [CellProfiler v3.1.8] -> stage not stated [MACS2]

### Sox9 directs divergent epigenomic states in brain tumor subtypes. (PNAS 2022)

- DOI: 10.1073/pnas.2202015119 | PMCID: PMC9303974 | PMID: 35858326
- Version used: **2.2.7.1**
- Evidence: Peaks were called using MACS2 (v2.2.7.1).
- Full pipeline: quality control [MultiQC v0.9] -> alignment/mapping [Bioconductor, Bowtie2 v2.2.6, R, STAR v2.5.0a] -> quantification [ImageJ] -> normalisation [DESeq2 v1.30.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2 v1.30.1, Enrichr, clusterProfiler, ggplot2 v3.3.5, limma] -> visualisation [Enrichr, ggplot2 v3.3.5] -> stage not stated [ComplexHeatmap v2.6.2, HOMER v4.10, MACS2 v2.2.7.1, SAMtools v1.9, deepTools v3.2.0]

### Therapeutic functions of astrocytes to treat α-synuclein pathology in Parkinson's disease. (PNAS 2022)

- DOI: 10.1073/pnas.2110746119 | PMCID: PMC9304026 | PMID: 35858361
- Evidence: However, we cannot exclude that the lack of therapeutic effects may be due to cellular stress accumulated in donor cells during cell dissociation and MACS procedures.
- Full pipeline: quantification [DESeq2 v1.32] -> normalisation [DESeq2 v1.32] -> stage not stated [ImageJ, MACS2]

### Sox8 remodels the cranial ectoderm to generate the ear. (PNAS 2022)

- DOI: 10.1073/pnas.2118938119 | PMCID: PMC9282420 | PMID: 35867760
- Version used: **2.2.7.1**
- Evidence: MACS v2.2.7.1 was used to call broad peaks (false discovery rate [FDR] < 0.1) and narrow peaks (FDR < 0.05) for ChIPseq and ATACseq data, respectively.
- Full pipeline: read trimming [Cutadapt v2.10] -> alignment/mapping [HISAT2 v2.2.1, Nextflow, STAR] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [BEDTools v2.29.2, DESeq2, Docker, ImageJ, Monocle, R, velocyto v0.17]

### Single-cell transcriptome and accessible chromatin dynamics during endocrine pancreas development. (PNAS 2022)

- DOI: 10.1073/pnas.2201267119 | PMCID: PMC9245718 | PMID: 35733248
- Evidence: Trimmed fastq files were then mapped to the mm10 genome with bowtie2 ( 67 ) and the parameter “–very-sensitive.” Lastly, peaks were called using MACS2 ( 68 ) with “-q 0.01 –shift 0 –nomodel.” At the end of PEPATAC processing, 42 to 88 million reads aligned to the mouse genome, and 15,377 to 55,676 peaks per sample were detected.
- Full pipeline: read trimming [Bowtie2, MACS2] -> alignment/mapping [Bowtie2, MACS2] -> quantification [HOMER] -> dimensionality reduction/clustering [Monocle, R] -> simulation/modelling [Monocle] -> visualisation [R]

### The evening complex integrates photoperiod signals to control flowering in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2122582119 | PMCID: PMC9245669 | PMID: 35733265
- Evidence: Peaks were identified using MACS2 and filtered by q value < 0.05.
- Full pipeline: alignment/mapping [HISAT2] -> quantification [StringTie, deepTools] -> normalisation [deepTools] -> stage not stated [BEDTools v2.30.0, BWA, MACS2, R, SAMtools v1.11]

### SpyChIP identifies cell type-specific transcription factor occupancy from complex tissues. (PNAS 2022)

- DOI: 10.1073/pnas.2122900119 | PMCID: PMC9231492 | PMID: 35696584
- Evidence: The reads were mapped to Drosophila genome build dm6 by Bowtie2 ( 16 ) using default settings, and peak calling was performed by MACS2 ( 17 ) with the following parameters: –nomodel –extsize 200 (all other parameters were default).
- Full pipeline: alignment/mapping [Bowtie2, MACS2] -> stage not stated [R, ggplot2]

### Sialic acids on B cells are crucial for their survival and provide protection against apoptosis. (PNAS 2022)

- DOI: 10.1073/pnas.2201129119 | PMCID: PMC9231502 | PMID: 35696562
- Evidence: Total bone marrow cells or MACS purified pro-B/pre-B/immature B cells were cultured in RPMI 1640 media containing 5% fetal calf serum, 1.2 mM L-glutamin, 50 µM β-mercaptoethanol, 100 U/mL penicillin/streptomycin, 1 mM sodium pyruvate, 1× nonessential amino acids (all ingredients obtained from Gibco).
- Full pipeline: stage not stated [MACS2]

### The nonclassical MHC class I Qa-1 expressed in layer 6 neurons regulates activity-dependent plasticity via microglial CD94/NKG2 in the cortex. (PNAS 2022)

- DOI: 10.1073/pnas.2203965119 | PMCID: PMC9191652 | PMID: 35648829
- Evidence: Cortices were gently homogenized by five strokes in MACS buffer, and resulting lysates were filtered through a 70-µm filter and washed to remove debris.
- Full pipeline: stage not stated [MACS2]

### GPR174 signals via G&lt;i&gt;α&lt;/i&gt;s to control a CD86-containing gene expression program in B cells. (PNAS 2022)

- DOI: 10.1073/pnas.2201794119 | PMCID: PMC9191659 | PMID: 35639700
- Evidence: Spleens were isolated and sterilely mashed through a 100-µm filter on ice in cold MACS (PBS with 2% FBS and 1 mM EDTA).
- Full pipeline: alignment/mapping [STAR] -> differential/statistical testing [DESeq2, GSEA] -> stage not stated [MACS2, pheatmap]

### Zinc finger protein 280C contributes to colorectal tumorigenesis by maintaining epigenetic repression at H3K27me3-marked loci. (PNAS 2022)

- DOI: 10.1073/pnas.2120633119 | PMCID: PMC9295756 | PMID: 35605119
- Version used: **2.1.6**
- Evidence: Peak calling from alignment results was performed using MACS2 (version 2.1.6) using default parameters with a significance level at a q value < 0.05.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.9, MACS2 v2.1.6] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> visualisation [deepTools v3.1.3] -> stage not stated [GSEA]

### α<sub>1B/D</sub>-adrenoceptors regulate chemokine receptor-mediated leukocyte migration via formation of heteromeric receptor complexes. (PNAS 2022)

- DOI: 10.1073/pnas.2123511119 | PMCID: PMC9171806 | PMID: 35537053
- Evidence: CD14+/CD16− monocytes were then isolated via negative selection using magnetic-activated cell sorting LS columns (MACS LS), an indirect magnetic labeling system from Miltenyi Biotech (Bergisch Gladbach, Germany).
- Full pipeline: quantification [ImageJ] -> stage not stated [MACS2]

### A synthetic lethality screen reveals ING5 as a genetic dependency of catalytically dead Set1A/COMPASS in mouse embryonic stem cells. (PNAS 2022)

- DOI: 10.1073/pnas.2118385119 | PMCID: PMC9171609 | PMID: 35500115
- Evidence: ( C ) Peak calling was performed by MACS2 for ING5 and Set1A, and a 20% overlap was observed, indicating that one-fifth of the identified regions are cooccupied by Set1A and ING5.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [SAMtools] -> stage not stated [ImageJ, MACS2, Metascape]

### Extracellular vesicles from triple negative breast cancer promote pro-inflammatory macrophages associated with better clinical outcome. (PNAS 2022)

- DOI: 10.1073/pnas.2107394119 | PMCID: PMC9169908 | PMID: 35439048
- Evidence: CCM-mo-macs were slightly higher in M2 signature, and CSF-1-mo-MACS expressed equal low levels of both M1 and M2 signatures.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.22.2] -> visualisation [UMAP, pheatmap] -> stage not stated [Enrichr, MACS2, R, Seurat]

### Definition of a mouse microglial subset that regulates neuronal development and proinflammatory responses in the brain. (PNAS 2022)

- DOI: 10.1073/pnas.2116241119 | PMCID: PMC8872761 | PMID: 35177477
- Evidence: For isolation of CD11c + and CD11c − microglia, single-cell suspensions were incubated with CD11c microbeads (Miltenyi) and cells magnetically bound to columns using MACS were extensively washed before the CD11c + fraction was eluted after lifting the magnetic field.
- Full pipeline: read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> stage not stated [MACS2]

### Butterfly eyespots evolved via cooption of an ancestral gene-regulatory network that also patterns antennae, legs, and wings. (PNAS 2022)

- DOI: 10.1073/pnas.2108661119 | PMCID: PMC8872758 | PMID: 35169073
- Evidence: Peaks were called with MACS2 software ( 33 ), using the aligned enriched and input (control) files with the q value (minimum false discovery rate [FDR]) cutoff to call significant regions.
- Full pipeline: alignment/mapping [BLAST, GATK, HISAT2, MACS2, SAMtools] -> dimensionality reduction/clustering [R] -> differential/statistical testing [HISAT2, MACS2] -> stage not stated [BEDTools, BUSCO, DESeq2, StringTie, deepTools]

### Integrative analysis reveals multiple modes of LXR transcriptional regulation in liver. (PNAS 2022)

- DOI: 10.1073/pnas.2122683119 | PMCID: PMC8851562 | PMID: 35145035
- Evidence: Peaks were called using MACS2 ( 68 ) and quantitated across samples using Seqmonk ( 69 ) generating reads per kilobase per million mapped reads (RPKM).
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Cutadapt] -> alignment/mapping [Bowtie2, Cutadapt, MACS2, SAMtools, STAR v2.6.0c] -> quantification [MACS2] -> differential/statistical testing [DESeq2] -> visualisation [SAMtools] -> stage not stated [Enrichr, R, pheatmap]

### TRIM14 inhibits OPTN-mediated autophagic degradation of KDM4D to epigenetically regulate inflammation. (PNAS 2022)

- DOI: 10.1073/pnas.2113454119 | PMCID: PMC8851536 | PMID: 35145029
- Version used: **2.2.6**
- Evidence: ChIP-seq peaks were called by MACS2 (v 2.2.6) with default options.
- Full pipeline: alignment/mapping [Bowtie2 v2.2.5] -> dimensionality reduction/clustering [clusterProfiler v4.0.5] -> stage not stated [Bioconductor, ImageJ, MACS2 v2.2.6, Picard]

### Epigenetic state determines inflammatory sensing in neuroblastoma. (PNAS 2022)

- DOI: 10.1073/pnas.2102358119 | PMCID: PMC8832972 | PMID: 35121657
- Evidence: Fresh NK cells were activated and expanded using NK MACS medium (Miltenyi Biotec, 130-114-429) supplemented with 5% AB human serum (Sigma Millipore, H4522) containing 500 IU/mL recombinant human IL-2 (Peprotech, 200-02) and 5 ng/mL recombinant human IL-15 (Peprotech, 200-15).
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Trimmomatic v0.39] -> quantification [RSEM v1.2.12] -> dimensionality reduction/clustering [UMAP] -> stage not stated [CellProfiler v4.07, MACS2, R, Seurat, ilastik v1.3.3, scDblFinder]

### BRD4-directed super-enhancer organization of transcription repression programs links to chemotherapeutic efficacy in breast cancer. (PNAS 2022)

- DOI: 10.1073/pnas.2109133119 | PMCID: PMC8832982 | PMID: 35105803
- Evidence: With Model-based Analysis of ChIP-seq version 2 (MACS2) ( 46 ) and a q value cutoff of 0.05, 43,300 BRD4-binding peaks, 65,574 LSD1-binding summits, 40,264 MTA3-binding sites, 149,985 H3K4me1-enriched peaks, and 94,907 H3K27ac-enriched peaks were called.
- Full pipeline: quality control [FastQC, fastp] -> read trimming [FastQC, fastp] -> alignment/mapping [DESeq2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, clusterProfiler] -> stage not stated [Bioconductor, HOMER, MACS2]

### Spatiotemporal analysis identifies ABF2 and ABF3 as key hubs of endodermal response to nitrate. (PNAS 2022)

- DOI: 10.1073/pnas.2107879119 | PMCID: PMC8794810 | PMID: 35046022
- Evidence: ChIP-seq data for each TF was compared with its partner Input DNA control and peaks were identified by MACS2 ( q = 0.05).
- Full pipeline: alignment/mapping [Bowtie2, TopHat] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEDTools, ImageJ, MACS2, R]

### Neuropilin-1, a myeloid cell-specific protein, is an inhibitor of HIV-1 infectivity. (PNAS 2022)

- DOI: 10.1073/pnas.2114884119 | PMCID: PMC8764665 | PMID: 34987100
- Evidence: The obtained virion pellets were resuspended in 200 μL of PBS with 50 μL of anti-CD44 microbeads for 30 min at room temperature, and the viable and infectious HIV-1 particles were further isolated by a magnetic-based method according to the manufacturer’s instructions (µMACS VitalVirus HIV Isolation Kit; Miltenyi Biotec).
- Full pipeline: stage not stated [MACS2]

### The PCY-SAG14 phytocyanin module regulated by PIFs and miR408 promotes dark-induced leaf senescence in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2116623119 | PMCID: PMC8784109 | PMID: 35022242
- Evidence: MACS2 ( https://macs3-project.github.io/MACS/ ) was used to call peaks and the peaks were visualized using DeepTools ( 61 ) and the Integrative Genomics Viewer ( https://igv.org ).
- Full pipeline: quality control [MultiQC] -> alignment/mapping [Bowtie2, HISAT2] -> quantification [StringTie] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [MACS2] -> stage not stated [Cutadapt, Trim Galore, pheatmap]

### The role of ATXR6 expression in modulating genome stability and transposable element repression in <i>Arabidopsis</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2115570119 | PMCID: PMC8784105 | PMID: 35027454
- Version used: **2.1.1**
- Evidence: ChIP-seq peaks in wild type and mutants were called by the callpeak function in MACS2 (v2.1.1.) ( 48 ).
- Full pipeline: alignment/mapping [Cufflinks, HISAT2, SAMtools, TopHat] -> quantification [Cufflinks] -> normalisation [deepTools] -> differential/statistical testing [Cufflinks] -> stage not stated [HTSeq, MACS2 v2.1.1, Picard, R]

### p53 deficient breast cancer cells reprogram preadipocytes toward tumor-protective immunomodulatory cells. (PNAS 2023)

- DOI: 10.1073/pnas.2311460120 | PMCID: PMC10756271 | PMID: 38127986
- Evidence: Cell suspensions were then strained through a 100-µM MACS SmartStrainer, and collected cells were resuspended in PEB buffer (PBS with 0.5% bovine serum albumin and 2 mM EDTA, pH 7.2).
- Full pipeline: quantification [ImageJ] -> normalisation [RSEM] -> machine learning [MACS2] -> stage not stated [GSEA, Metascape, R v4.0.2]

### A dicer-related helicase opposes the age-related pathology from SKN-1 activation in ASI neurons. (PNAS 2023)

- DOI: 10.1073/pnas.2308565120 | PMCID: PMC10756303 | PMID: 38113255
- Version used: **2.2.7.1**
- Evidence: Peak calls were made using MACS2 v2.2.7.1 Peak files were feature annotated using Chipseeker Bioconductor package in R using the annotate Peak function.
- Full pipeline: read trimming [STAR v2.7.6a, Trim Galore] -> alignment/mapping [STAR v2.7.6a] -> quantification [DESeq2, R v3.5.2] -> differential/statistical testing [DESeq2, R v3.5.2] -> stage not stated [Bioconductor, ImageJ, MACS2 v2.2.7.1, SAMtools v1.10]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Evidence: ChIP-seq peaks were called using MACS2 ( 49 ).
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### Identification of Tensin-3 as a MALT1 substrate that controls B cell adhesion and lymphoma dissemination. (PNAS 2023)

- DOI: 10.1073/pnas.2301155120 | PMCID: PMC10756297 | PMID: 38109544
- Evidence: Primary human B and T cells were isolated from healthy donors by magnetic affinity cell sorting (MACS) beads according to the manufacturer's description (Miltenyi MACS 130-045-101 for T cells and MACS 130-091-151 for B cells).
- Full pipeline: quantification [ImageJ] -> stage not stated [MACS2]

### pH-dependent structural transitions in cationic ionizable lipid mesophases are critical for lipid nanoparticle function. (PNAS 2023)

- DOI: 10.1073/pnas.2310491120 | PMCID: PMC10723131 | PMID: 38055742
- Evidence: The pelleted cells were resuspended in MACS isolation buffer (Miltenyi Biotec Norden AB, Lund, Sweden) before being further purified by immunomagnetic cell isolation according to the instructions by the manufacturer.
- Full pipeline: simulation/modelling [GROMACS] -> stage not stated [MACS2]

### The USP7-STAT3-granzyme-Par-1 axis regulates allergic inflammation by promoting differentiation of IL-5-producing Th2 cells. (PNAS 2023)

- DOI: 10.1073/pnas.2302903120 | PMCID: PMC10710068 | PMID: 38015852
- Evidence: MACS2 ( 50 ) was used for peak calling and visualization of binding, with the parameters set as follows: windowsize = 300, gapsize = 300, and false discovery rate = 0.01.
- Full pipeline: alignment/mapping [Bowtie2, Cufflinks v2.0.2, HOMER, SAMtools, TopHat v1.3.2, deepTools v2.0] -> quantification [UMAP] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2] -> simulation/modelling [Monocle] -> visualisation [Cytoscape v3.7.1, MACS2] -> stage not stated [Seurat]

### Single-cell bisulfite-free 5mC and 5hmC sequencing with high sensitivity and scalability. (PNAS 2023)

- DOI: 10.1073/pnas.2310367120 | PMCID: PMC10710054 | PMID: 38011566
- Evidence: Then, we used MACS2 for narrowpeak calling with default parameters.
- Full pipeline: quality control [Trim Galore] -> read trimming [Trim Galore] -> alignment/mapping [Bismark] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ComplexHeatmap, MACS2, RepeatMasker, Seurat, deepTools]

### RAD51-mediated R-loop formation acts to repair transcription-associated DNA breaks driving antigenic variation in &lt;i&gt;Trypanosoma brucei&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2309306120 | PMCID: PMC10691351 | PMID: 37988471
- Evidence: A total of 17,134 and 11,160 BLISS “peaks” were predicted using MACS2 ( 73 ) in WT and rad51 –/ – populations, respectively, with similar distribution across a range of genomic landmarks ( SI Appendix , Fig.
- Full pipeline: stage not stated [MACS2]

### TGF-β broadly modifies rather than specifically suppresses reactivated memory CD8 T cells in a dose-dependent manner. (PNAS 2023)

- DOI: 10.1073/pnas.2313228120 | PMCID: PMC10691214 | PMID: 37988468
- Evidence: To enrich bulk T cells from single-cell suspensions, we used negative T cell isolation MACS (STEMCELL Technologies, Canada).
- Full pipeline: normalisation [limma] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2, R]

### Cellular nucleic acid-binding protein restricts SARS-CoV-2 by regulating interferon and disrupting RNA-protein condensates. (PNAS 2023)

- DOI: 10.1073/pnas.2308355120 | PMCID: PMC10666094 | PMID: 37963251
- Evidence: The mouse lung and spleen were collected and minced in RPMI and filtered through a 70-μm filter, washed and resuspended in red-blood-cell lysis buffer, and then resuspended in MACS buffer.
- Full pipeline: stage not stated [MACS2]

### Ultrafine mapping of chromosome conformation at hundred basepair resolution reveals regulatory genome architecture. (PNAS 2023)

- DOI: 10.1073/pnas.2313285120 | PMCID: PMC10636305 | PMID: 37922325
- Evidence: In order to differentiate interaction loops from the local background interactions that occur with high frequency within TADs, we developed an algorithm resembling MACS ( 17 ) to identify loop sites with overrepresented interaction read counts.
- Full pipeline: quantification [MACS2]

### The human adenovirus E1B-55K oncoprotein coordinates cell transformation through regulation of DNA-bound host transcription factors. (PNAS 2023)

- DOI: 10.1073/pnas.2310770120 | PMCID: PMC10622919 | PMID: 37883435
- Evidence: Briefly, the ChIP-seq FASTQ sequence files were aligned to the rat reference genome, and binding sites (peaks) were identified via MACS2 ( 37 ), verified by the multiple sample peak calling (MSPC) software ( 38 ) and annotated based on their genomic regions using the R package ChIPseeker ( 39 ) ( Fig.
- Full pipeline: alignment/mapping [MACS2, R] -> stage not stated [HOMER, Metascape]

### Pan-centromere reveals widespread centromere repositioning of soybean genomes. (PNAS 2023)

- DOI: 10.1073/pnas.2310177120 | PMCID: PMC10589659 | PMID: 37816061
- Evidence: 3 A – E and 4 B , MACS2 ( 75 ) was used to call CENH3-ChIP-seq peaks using input as a control with the settings: -f BAMPE -g 1.0e 9 .
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, Picard, SAMtools v1.3.1, Trimmomatic v0.36] -> variant calling [BCFtools, GATK v3.8.1] -> stage not stated [MACS2]

### Context-dependent function of the transcriptional regulator Rap1 in gene silencing and activation in <i>Saccharomyces cerevisiae</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2304343120 | PMCID: PMC10556627 | PMID: 37769255
- Evidence: S2 A , peak summits were defined by MACS3 callpeak, using a cutoff of q < 0.01.
- Full pipeline: alignment/mapping [Bowtie2] -> normalisation [ggplot2] -> stage not stated [MACS2]

### A TIAM1-TRIM28 complex mediates epigenetic silencing of protocadherins to promote migration of lung cancer cells. (PNAS 2023)

- DOI: 10.1073/pnas.2300489120 | PMCID: PMC10556593 | PMID: 37748077
- Evidence: Of the total TIAM1 peaks found by MACS peak caller, 41% (394/952) were found at gene promoters/transcriptional start sites (TSS) ( Fig.
- Full pipeline: stage not stated [GSEA, MACS2]

### BRWD3 promotes KDM5 degradation to maintain H3K4 methylation levels. (PNAS 2023)

- DOI: 10.1073/pnas.2305092120 | PMCID: PMC10523488 | PMID: 37722046
- Evidence: Peaks were called with MACS2 callpeak tool with default settings and plots were generated using deepTools plotHeatmap.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [Bowtie2, FastQC, Trimmomatic, fastp] -> alignment/mapping [BEDTools, Bowtie2, SAMtools, STAR, featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2, deepTools]

### Transgenic expression of the HERV-W envelope protein leads to polarized glial cell populations and a neurodegenerative environment. (PNAS 2023)

- DOI: 10.1073/pnas.2308187120 | PMCID: PMC10515160 | PMID: 37695891
- Evidence: Subsequently, astrocytes and microglia were purified using MACS according to the manufacturer’s protocol (Miltenyi Biotec, Bergisch-Gladbach, Germany).
- Full pipeline: quantification [ImageJ] -> stage not stated [MACS2]

### XCR1 expression distinguishes human conventional dendritic cell type 1 with full effector functions from their immediate precursors. (PNAS 2023)

- DOI: 10.1073/pnas.2300343120 | PMCID: PMC10438835 | PMID: 37566635
- Evidence: Then, the tissue was transferred into C-tubes (Miltenyi Biotech), filled with 5 mL RPMI1640, further mechanically disrupted using a Gentle MACS tissue dissociator (Miltenyi Biotech), and enzymatically digested with 400 U/mL collagenase D (Serva) and 100 µg (spleen, tonsil) or 300 µg (thymus) deoxyribonuclease I (Sigma).
- Full pipeline: dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR] -> stage not stated [GSEA, MACS2, Seurat]

### SETD7 functions as a transcription repressor in prostate cancer via methylating FOXA1. (PNAS 2023)

- DOI: 10.1073/pnas.2220472120 | PMCID: PMC10438836 | PMID: 37549269
- Version used: **2.1.4**
- Evidence: ChIP-sequencing reads were mapped to the hg19 human genome, and the significance of enriched peaks was evaluated using MACS2 (version 2.1.4) ( 49 ).
- Full pipeline: alignment/mapping [MACS2 v2.1.4, R] -> dimensionality reduction/clustering [GSEA] -> differential/statistical testing [R]

### NFIA in adipocytes reciprocally regulates mitochondrial and inflammatory gene program to improve glucose homeostasis. (PNAS 2023)

- DOI: 10.1073/pnas.2308750120 | PMCID: PMC10401007 | PMID: 37487068
- Evidence: Peak calling was performed using MACS2 (Galaxy version 2.1.1.20160309) ( 39 ).
- Full pipeline: alignment/mapping [Bowtie2, STAR] -> quantification [StringTie] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, Galaxy, ImageJ, MACS2]

### NOS inhibition reverses TLR2-induced chondrocyte dysfunction and attenuates age-related osteoarthritis. (PNAS 2023)

- DOI: 10.1073/pnas.2207993120 | PMCID: PMC10629581 | PMID: 37428931
- Evidence: Samples were blended using a gentleMACS™ device with M tubes (Miltenyi Biotec). mRNA was then isolated using Oligo (dT) magnetic beads (µMACS TM mRNA Isolation Kit, Miltenyi Biotec) following manufacturer’s instructions. cDNA was reverse-transcribed from isolated mRNA using TaqMan reverse transcription reagents (Thermo Fisher Scientific).
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [featureCounts] -> stage not stated [GSEA, MACS2]

### EMT activates exocytotic Rabs to coordinate invasion and immunosuppression in lung cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2220276120 | PMCID: PMC10334751 | PMID: 37406091
- Evidence: As described previously ( 50 ), 3.5 wk after subcutaneous injection of 1 × 10 6 344SQ_shCTL or 344SQ_shRab6A into the flank of wild-type mice, subcutaneous tumors were processed using the MACS Miltenyl Biotec tumor dissociation kit.
- Full pipeline: stage not stated [Fiji, ImageJ, MACS2]

### Contribution of the IGCR1 regulatory element and the 3'<i>Igh</i> CTCF-binding elements to regulation of <i>Igh</i> V(D)J recombination. (PNAS 2023)

- DOI: 10.1073/pnas.2306564120 | PMCID: PMC10293834 | PMID: 37339228
- Evidence: For peak analysis, 3C-HTGTS profiles were analyzed by MACS2 pipeline to call robust interaction peaks (macs2 bdgpeakcall -c20 -l400 -g1000 was used for pro-B 3C-HTGTS in Fig.
- Full pipeline: stage not stated [MACS2]

### Dynamic interactome of the MHC I peptide loading complex in human dendritic cells. (PNAS 2023)

- DOI: 10.1073/pnas.2219790120 | PMCID: PMC10288655 | PMID: 37307450
- Evidence: The PBMC layer was washed twice with cold MACS buffer and centrifuged at 300 g for 10 min at RT.
- Full pipeline: stage not stated [MACS2]

### Fully synthetic platform to rapidly generate tetravalent bispecific nanobody-based immunoglobulins. (PNAS 2023)

- DOI: 10.1073/pnas.2216612120 | PMCID: PMC10268213 | PMID: 37276407
- Evidence: We used a combination of three rounds of MACS to deplete the library of nonbinding clones, with five rounds of FACS to enrich the population in nanobodies that target SARS-CoV-2 RBD.
- Full pipeline: stage not stated [MACS2]

### CARD9 attenuates Aβ pathology and modifies microglial responses in an Alzheimer's disease mouse model. (PNAS 2023)

- DOI: 10.1073/pnas.2303760120 | PMCID: PMC10268238 | PMID: 37276426
- Evidence: MACS (Magnetic-Activated Cell Sorting) Isolation of Microglia for RNA-Seq.
- Full pipeline: quality control [SAMtools] -> alignment/mapping [HISAT2] -> normalisation [DESeq2 v1.30.0] -> differential/statistical testing [DESeq2 v1.30.0] -> stage not stated [HTSeq, MACS2, R, fgsea, ggplot2, pheatmap, tidyverse]

### Steroid receptor coactivator 3 is a key modulator of regulatory T cell-mediated tumor evasion. (PNAS 2023)

- DOI: 10.1073/pnas.2221707120 | PMCID: PMC10266015 | PMID: 37253006
- Evidence: Finally, T cell isolation was performed using Miltenyi Biotec's MACS CD4 + CD25 + T cell isolation kit using the manufacturer's recommended protocol.
- Full pipeline: quantification [QuPath] -> differential/statistical testing [Bioconductor] -> stage not stated [GSEA, MACS2]

### Mechanoepigenetic regulation of extracellular matrix homeostasis via Yap and Taz. (PNAS 2023)

- DOI: 10.1073/pnas.2211947120 | PMCID: PMC10235980 | PMID: 37216538
- Evidence: BAM files were then used to call peaks using MACS2, with default settings with a q threshold of 0.05 ( 68 ).
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [ImageJ, MACS2, Picard, SAMtools, deepTools, featureCounts]

### Apple-shaped obesity: A risky soil for cytokine-accelerated severity in COVID-19. (PNAS 2023)

- DOI: 10.1073/pnas.2300155120 | PMCID: PMC10235975 | PMID: 37216518
- Evidence: CD45-positive cells were isolated from lung-derived cells using MACS beads (130-052-301, Miltenyi Biotec) according to the manufacturer’s protocol and harvested in 24-well plates at 5 × 105 cells/well.
- Full pipeline: stage not stated [MACS2]

### Activation of P53 pathway contributes to <i>Xenopus</i> hybrid inviability. (PNAS 2023)

- DOI: 10.1073/pnas.2303698120 | PMCID: PMC10214167 | PMID: 37186864
- Evidence: The sequencing coverage of X. tropicalis and X. laevis was calculated using bamCoverage ( 43 ) with options “--binSize 10 --normalizeUsing RPKM –ignoreDuplicates.” Peaks were identified using MACS2 with the options “macs2 callpeak -f BAM -g 1.4e9/2.6e9 -B -q 0.1 --nomodel --shift 70 --extsize 140 --keep-dup all” ( 44 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [HISAT2, SAMtools, fastp] -> quantification [MACS2] -> normalisation [MACS2] -> dimensionality reduction/clustering [R, clusterProfiler v4.2.2] -> differential/statistical testing [DESeq2, STRING db] -> stage not stated [Matplotlib v3.5.1, deepTools v3.5, featureCounts, ggplot2, pheatmap]

### Differentiation of <i>Plasmodium</i> male gametocytes is initiated by the recruitment of a chromatin remodeler to a male-specific cis-element. (PNAS 2023)

- DOI: 10.1073/pnas.2303432120 | PMCID: PMC10193995 | PMID: 37155862
- Evidence: Mapping data were analyzed using MACS2 peak-calling algorithm.
- Full pipeline: alignment/mapping [Bowtie2, MACS2, Picard]

### A single-cell multiomic analysis of kidney organoid differentiation. (PNAS 2023)

- DOI: 10.1073/pnas.2219699120 | PMCID: PMC10193973 | PMID: 37155865
- Evidence: ATAC-seq peaks in the dataset were identified on all cells together using MACS2 ( 75 ) with the default parameters of Signac’s (v1.5.0) CallPeaks function: --gsize 2.7e9 --nomodel False --shift -100 --extsize 200 --d-min 20 --qvalue 0.05 --broad False ( 57 ).
- Full pipeline: quantification [UMAP] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [Monocle v2.20.0] -> stage not stated [MACS2, R, Signac, scDblFinder]

### Integrated analysis of single-cell chromatin state and transcriptome identified common vulnerability despite glioblastoma heterogeneity. (PNAS 2023)

- DOI: 10.1073/pnas.2210991120 | PMCID: PMC10194019 | PMID: 37155843
- Evidence: MACS2 ( 53 ) was used for peak calling with the following parameters: macs2 callpeak -t sample -n sample -f BAM -g hs –nomodel –shift -100 –extsize 200 –slocal 1,000 –keep-dup all -B –SPMR –call-summits -q 1e-4.
- Full pipeline: alignment/mapping [Bowtie2, SAMtools, STAR] -> dimensionality reduction/clustering [Monocle, UMAP] -> differential/statistical testing [Enrichr, Monocle] -> visualisation [UMAP] -> stage not stated [GSEA, MACS2, Picard, R, Seurat]

### CDYL reinforces male gonadal sex determination through epigenetically repressing <i>Wnt4</i> transcription in mice. (PNAS 2023)

- DOI: 10.1073/pnas.2221499120 | PMCID: PMC10193937 | PMID: 37155872
- Evidence: MACS was performed as previously described ( 5 ).
- Full pipeline: alignment/mapping [STAR] -> normalisation [R, Seurat] -> dimensionality reduction/clustering [R, Seurat] -> stage not stated [MACS2, featureCounts v1.6.4]

### TRAF4-mediated nonproteolytic ubiquitination of androgen receptor promotes castration-resistant prostate cancer. (PNAS 2023)

- DOI: 10.1073/pnas.2218229120 | PMCID: PMC10193960 | PMID: 37155905
- Version used: **2.1.0**
- Evidence: Peaks were called using MACS 2.1.0 with default settings ( 78 ).
- Full pipeline: normalisation [HOMER] -> stage not stated [BEDTools, GSEA, MACS2 v2.1.0]

### Circadian clock protein BMAL1 broadly influences autophagy and endolysosomal function in astrocytes. (PNAS 2023)

- DOI: 10.1073/pnas.2220551120 | PMCID: PMC10194014 | PMID: 37155839
- Evidence: Cells were then incubated with red blood cell removal solution (Miltenyi MACS), centrifuged at 300 g, and resuspended in MACS buffer (dPBS, 0.5% BSA, 2mM EDTA).
- Full pipeline: normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [MACS2]

### Targeting SWI/SNF ATPases in H3.3K27M diffuse intrinsic pontine gliomas. (PNAS 2023)

- DOI: 10.1073/pnas.2221175120 | PMCID: PMC10161095 | PMID: 37094128
- Version used: **3.0.0**
- Evidence: Comparative analysis was performed by a standard normalization method, and peaks were determined using the MACS 3.0.0 algorithm at a cutoff of P -value 1×10 7 , without control file, and with the -nomodel option.
- Full pipeline: alignment/mapping [RSEM] -> normalisation [MACS2 v3.0.0] -> differential/statistical testing [GSEA]

### B cell peripheral tolerance is promoted by cathepsin B protease. (PNAS 2023)

- DOI: 10.1073/pnas.2300099120 | PMCID: PMC10120085 | PMID: 37040412
- Evidence: Cells were stained for 20 min on ice in MACS buffer (2% FCS in PBS with 1 mM EDTA) at 0.5 to 1 × 10 6 cells per well in 96-well round-bottom plates unless otherwise specified.
- Full pipeline: quantification [ImageJ v1.53] -> stage not stated [MACS2]

### Optimal generation of hepatic tissue-resident memory CD4 T cells requires IL-1 and IL-2. (PNAS 2023)

- DOI: 10.1073/pnas.2214699120 | PMCID: PMC10120061 | PMID: 37040404
- Evidence: Single-cell suspensions were made as described above, and CD4 T cells were isolated with MACS CD4 T cell selection kit (Miltenyi) following the kit protocol.
- Full pipeline: differential/statistical testing [limma] -> stage not stated [MACS2]

### Cholinergic regulation of vascular endothelial function by human ChAT<sup>+</sup> T cells. (PNAS 2023)

- DOI: 10.1073/pnas.2212476120 | PMCID: PMC10083572 | PMID: 36989306
- Evidence: We observed that ChAT was significantly higher in the CD4 + T cell MACS enriched population as compared with CD4 + MACS-depleted population after 96 h of activation ( Fig.
- Full pipeline: alignment/mapping [Monocle] -> quantification [ImageJ] -> dimensionality reduction/clustering [UMAP] -> visualisation [ImageJ] -> stage not stated [MACS2, edgeR]

### Multifaceted role for p53 in pancreatic cancer suppression. (PNAS 2023)

- DOI: 10.1073/pnas.2211937120 | PMCID: PMC10013849 | PMID: 36848578
- Evidence: Accessible regions of the genome were called using MACS2 ( 58 ).
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [DESeq2] -> stage not stated [HOMER, MACS2]

### <i>Cspg4<sup>high</sup></i> microglia contribute to microgliosis during neurodegeneration. (PNAS 2023)

- DOI: 10.1073/pnas.2210643120 | PMCID: PMC9974490 | PMID: 36795751
- Evidence: Microglia were isolated using MACS according to the manufacturer’s instructions.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [ImageJ, MACS2, Seurat]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Version used: **2.2.7.1**
- Evidence: Broad ChIP-enriched regions were identified by MACS2 v2.2.7.1.
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### Definition of the contribution of an Osteopontin-producing CD11c<sup>+</sup> microglial subset to Alzheimer's disease. (PNAS 2023)

- DOI: 10.1073/pnas.2218915120 | PMCID: PMC9963365 | PMID: 36730200
- Evidence: Briefly, after generation of brain single-cell suspensions, MACS buffer (PBS pH 7.2, 2 mM EDTA and 0.5% BSA) was used to resuspend pelleted cells.
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [STAR, Trimmomatic v0.36] -> alignment/mapping [STAR] -> quantification [ImageJ] -> differential/statistical testing [Bioconductor, R, edgeR] -> stage not stated [MACS2]

### Distinctive transcriptomic and epigenomic signatures of bone marrow-derived myeloid cells and microglia in CNS autoimmunity. (PNAS 2023)

- DOI: 10.1073/pnas.2212696120 | PMCID: PMC9963604 | PMID: 36730207
- Evidence: Peak detection was performed using MACS2 ( 33 ), and peak differential analysis and motif detection were conducted in Signac using the FindMarkers and FindMotifs functions, respectively (the latter restricted to peaks in the top 25th percentile ranked by average log 2 fold-change).
- Full pipeline: quality control [ArchR] -> dimensionality reduction/clustering [GSEA, Signac, UMAP, clusterProfiler, fgsea] -> differential/statistical testing [MACS2] -> stage not stated [R, Seurat, scDblFinder]

### METTL3 is essential for normal progesterone signaling during embryo implantation via m<sup>6</sup>A-mediated translation control of progesterone receptor. (PNAS 2023)

- DOI: 10.1073/pnas.2214684120 | PMCID: PMC9945998 | PMID: 36693099
- Evidence: MACS software v3.0.0a7 ( 75 ) was used for m 6 A peak calling with the significance cutoff q-value < 0.05.
- Full pipeline: alignment/mapping [Cufflinks v2.2.1] -> stage not stated [HOMER v4.7, ImageJ, MACS2, R]

### Distinct and opposite effects of leukemogenic <i>Idh</i> and <i>Tet2</i> mutations in hematopoietic stem and progenitor cells. (PNAS 2023)

- DOI: 10.1073/pnas.2208176120 | PMCID: PMC9942850 | PMID: 36652477
- Evidence: Bone marrow cells were isolated by flushing in cold MACS buffer (phosphate-buffered saline with 0.5% bovine serum albumin and 2 mM EDTA pH8.0).
- Full pipeline: alignment/mapping [SCENIC, Seurat, Slingshot] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [GSEA, MACS2]

### SUMO/deSUMOylation of the BRI1 brassinosteroid receptor modulates plant growth responses to temperature. (PNAS 2023)

- DOI: 10.1073/pnas.2217255120 | PMCID: PMC9942830 | PMID: 36652487
- Evidence: Immunoprecipitation experiments were carried out as previously described ( 25 ), using the μMACS GFP and HA isolation kits (Miltenyi Biotec).
- Full pipeline: stage not stated [Fiji, ImageJ, MACS2]

### Evolution of nanobodies specific for BCL11A. (PNAS 2023)

- DOI: 10.1073/pnas.2218959120 | PMCID: PMC9933118 | PMID: 36626555
- Evidence: Nanobodies were first selected from the synthetic yeast display nanobody library ( 12 ) using MACS with streptavidin microbeads and anti-flag microbeads (Miltenyi).
- Full pipeline: visualisation [PyMOL] -> stage not stated [MACS2, PHENIX]

### Geometrical frustration versus Kitaev interactions in BaCo<sub>2</sub>(AsO<sub>4</sub>)<sub>2</sub>. (PNAS 2023)

- DOI: 10.1073/pnas.2215509119 | PMCID: PMC9926200 | PMID: 36608295
- Evidence: The MACS experiment used 0.88(1) g of sample, while the SEQUOIA and HYSPEC samples totaled 0.96(1) g.
- Full pipeline: stage not stated [MACS2]

### The Maresin 1-LGR6 axis decreases respiratory syncytial virus-induced lung inflammation. (PNAS 2023)

- DOI: 10.1073/pnas.2206480120 | PMCID: PMC9926266 | PMID: 36595677
- Evidence: Lungs were then dissociated with a gentle MACS Dissociator (Miltenyi Biotech) according to the manufacturer’s protocol.
- Full pipeline: stage not stated [MACS2]

### Human ERG oncoprotein represses &lt;i&gt;a Drosophila&lt;/i&gt; LIM domain binding protein-coding gene &lt;i&gt;Chip&lt;/i&gt;. (PNAS 2023)

- DOI: 10.1073/pnas.2211189119 | PMCID: PMC9926275 | PMID: 36595681
- Evidence: Note orange arrowheads mark the ERG-binding MACS peak in control while reduced blue arrowheads display loss of ERG occupancy on LDB1 upon ERG knockdown.
- Full pipeline: stage not stated [MACS2]

### The direct binding of &lt;i&gt;Plasmodium vivax&lt;/i&gt; AMA1 to erythrocytes defines a RON2-independent invasion pathway. (PNAS 2023)

- DOI: 10.1073/pnas.2215003120 | PMCID: PMC9910450 | PMID: 36577076
- Evidence: MACS purification was done as previously described ( 30 , 31 ).
- Full pipeline: stage not stated [MACS2]

### Non-B-form DNA tends to form in centromeric regions and has undergone changes in polyploid oat subgenomes. (PNAS 2023)

- DOI: 10.1073/pnas.2211683120 | PMCID: PMC9910436 | PMID: 36574697
- Evidence: MACS2 was used to detect peaks from the alignments ( 37 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA, Trimmomatic v0.36] -> alignment/mapping [BWA, MACS2, SAMtools v1.3.1, deepTools] -> normalisation [deepTools] -> visualisation [deepTools]

### Histone methyltransferase SETDB1 safeguards mouse fetal hematopoiesis by suppressing activation of cryptic enhancers. (PNAS 2024)

- DOI: 10.1073/pnas.2409656121 | PMCID: PMC11670114 | PMID: 39689172
- Evidence: For intracellular Ki-67 staining, RBC-lysed fetal liver cells were subjected to MACS cell separation to enrich for lineage neg cells.
- Full pipeline: quantification [DESeq2] -> normalisation [DESeq2, RSEM, pheatmap] -> differential/statistical testing [DESeq2] -> visualisation [RSEM, pheatmap] -> stage not stated [BEDTools, GSEA, MACS2, deepTools]

### Glutamine is critical for the maintenance of type 1 conventional dendritic cells in normal tissue and the tumor microenvironment. (PNAS 2024)

- DOI: 10.1073/pnas.2412157121 | PMCID: PMC11648871 | PMID: 39625974
- Evidence: Extracellular staining: Samples were harvested, resuspended in 100 μL of MACS buffer (PBS with 0.5% BSA and 2 mM EDTA), then incubated for 5 min on ice with anti-mouse CD16/32 Fc Block (BD, Clone 2.4G2, # 553142) at 1:200, and subsequently stained at 4 °C with primary-fluorophore conjugated antibodies listed below for 20 min at 4 °C for identification of cell populations by FACS.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> stage not stated [MACS2, R v4.3.1, Seurat]

### The fork protection complex generates DNA topological stress-induced DNA damage while ensuring full and faithful genome duplication. (PNAS 2024)

- DOI: 10.1073/pnas.2413631121 | PMCID: PMC11626154 | PMID: 39589889
- Evidence: For RFA1 analysis duplicates were removed using picard ( https://broadinstitute.github.io/picard ) and the resulting BAM files were used for Model-based Analysis of ChIP-SEQ by MACS2 ( https://github.com/macs3-project/MACS/wiki/Install-macs2 ), using the “call peak” function to generate genome-wide score data.
- Full pipeline: stage not stated [Bowtie2, MACS2, SAMtools]

### Chronologically inappropriate morphogenesis (&lt;i&gt;Chinmo&lt;/i&gt;) is required for maintenance of larval stages of fall armyworm. (PNAS 2024)

- DOI: 10.1073/pnas.2411286121 | PMCID: PMC11626174 | PMID: 39589873
- Evidence: ...raction, curation of high-quality cells, extraction of transcription start site (TSS) positions, TSS enrichment score computation, peak calling using MACS2 ( 59 ), quantification of counts within each peak, annotation of peaks with their nearest genes, and extraction of gene-related information.
- Full pipeline: quantification [MACS2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Bioconductor, Seurat, Signac]

### IFN-γ-induced Th1-Treg polarization in inflamed brains limits exacerbation of experimental autoimmune encephalomyelitis. (PNAS 2024)

- DOI: 10.1073/pnas.2401692121 | PMCID: PMC11621829 | PMID: 39560646
- Evidence: Subsequently, the brain was minced to 2 to 3 mm with scissors in C tubes (Miltenyi) containing 2.5 mL HBSS and mechanically dissociated using MACS Octo Dissociator (Miltenyi), sequentially employing preset programs B and D.
- Full pipeline: quantification [ImageJ] -> differential/statistical testing [Metascape] -> stage not stated [MACS2, Seurat]

### A complex mechanism translating variation of a simple genetic architecture into alternative life histories. (PNAS 2024)

- DOI: 10.1073/pnas.2402386121 | PMCID: PMC11621623 | PMID: 39560647
- Evidence: We used “MACS3” ( https://github.com/macs3-project/MACS ) with parameters “--broad --broad-cutoff 0.1” to identify genome regions associated with H3K27ac, H3K4me3, and VGLL3 (for all samples and for vgll3 genotypes separately).
- Full pipeline: read trimming [STAR, fastp] -> alignment/mapping [Bowtie2, Picard, SAMtools, STAR] -> variant calling [MACS2] -> quantification [DESeq2, R v4.2, featureCounts] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [igraph] -> visualisation [igraph] -> stage not stated [BEDTools, HOMER, WGCNA, edgeR]

### Genome-wide profiling of soybean WRINKLED1 transcription factor binding sites provides insight into seed storage lipid biosynthesis. (PNAS 2024)

- DOI: 10.1073/pnas.2415224121 | PMCID: PMC11551420 | PMID: 39475647
- Evidence: ChIP-Seq data were analyzed as described previously ( 29 ), with the exception that MACS3 software ( https://github.com/macs3-project/MACS ) was used in place of MACS2.
- Full pipeline: read trimming [edgeR] -> variant calling [edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [HOMER, MACS2]

### The &lt;i&gt;ivory&lt;/i&gt; lncRNA regulates seasonal color patterns in buckeye butterflies. (PNAS 2024)

- DOI: 10.1073/pnas.2403426121 | PMCID: PMC11474026 | PMID: 39352931
- Evidence: Comparative noncoding genome alignments for Scaffold 15 were performed using HALPER on J. coenia wing tissue ATAC-seq peak calls (MACS2) ( 7 ).
- Full pipeline: alignment/mapping [HISAT2, MACS2] -> differential/statistical testing [DESeq2] -> stage not stated [AUGUSTUS, BUSCO v5.4.7]

### miR-96-5p expression is sufficient to induce and maintain the senescent cell fate in the absence of stress. (PNAS 2024)

- DOI: 10.1073/pnas.2321182121 | PMCID: PMC11459134 | PMID: 39325426
- Evidence: The Galaxy Platform ( 60 ) was used for narrow and broad peak calling (MACS2) and differential peak calling (DiffBind).
- Full pipeline: quality control [FastQC, GATK] -> alignment/mapping [FastQC, GATK] -> differential/statistical testing [MACS2] -> stage not stated [Enrichr]

### Light-field tomographic fluorescence lifetime imaging microscopy. (PNAS 2024)

- DOI: 10.1073/pnas.2402556121 | PMCID: PMC11459138 | PMID: 39320920
- Evidence: The fibroblast (crawled out population) and epithelial (MACS sorted EpCAM + population) were isolated from the distal tissue and used in this study.
- Full pipeline: stage not stated [MACS2]

### Alveolar macrophage function is impaired following inhalation of berry e-cigarette vapor. (PNAS 2024)

- DOI: 10.1073/pnas.2406294121 | PMCID: PMC11459156 | PMID: 39312670
- Evidence: The pellet was resuspended in 300 µL of isolation buffer and the sample was transferred into a magnetized MACS MS column for magnetic isolation according to the manufacturer’s instructions (Miltenyi Biotec).
- Full pipeline: differential/statistical testing [Metascape] -> structure determination [AutoDock Vina v1.5.7] -> stage not stated [MACS2]

### The androgen receptor in mesenchymal progenitors regulates skeletal muscle mass via &lt;i&gt;Igf1&lt;/i&gt; expression in male mice. (PNAS 2024)

- DOI: 10.1073/pnas.2407768121 | PMCID: PMC11441553 | PMID: 39292748
- Version used: **2.2.7.1**
- Evidence: To identify AR peaks across samples, BAM files were merged across biological replicates (n = 2) to call peaks with MACS2 (v2.2.7.1) (−q 0.05) ( 71 ).
- Full pipeline: read trimming [Bowtie2 v2.4.5] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.2.1] -> quantification [featureCounts v2.0.1] -> normalisation [deepTools v3.5.1] -> differential/statistical testing [DESeq2 v1.36.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, Metascape, R, SAMtools v1.10, Trim Galore v0.6.7]

### cGAS activation in classical dendritic cells causes autoimmunity in TREX1-deficient mice. (PNAS 2024)

- DOI: 10.1073/pnas.2411747121 | PMCID: PMC11420187 | PMID: 39254994
- Evidence: For CD11c + cell isolation, splenocytes were processed with mouse CD11c MicroBeads UltraPure (Miltenyi Biotec) and MACS columns (Miltenyi Biotec).
- Full pipeline: stage not stated [MACS2]

### ERRα and ERRγ coordinate expression of genes associated with Alzheimer's disease, inhibiting &lt;i&gt;DKK1&lt;/i&gt; to suppress tau phosphorylation. (PNAS 2024)

- DOI: 10.1073/pnas.2406854121 | PMCID: PMC11406303 | PMID: 39231208
- Version used: **2.2.7.1**
- Evidence: Reads were aligned to the human genome assembly GRCh38.p13 using STAR (version 2.7.10a) and peak calling was performed using MACS2 (version 2.2.7.1).
- Full pipeline: alignment/mapping [MACS2 v2.2.7.1, STAR v2.7.10a] -> quantification [StringTie]

### Non-CG DNA hypomethylation promotes photosynthesis and nitrogen fixation in soybean. (PNAS 2024)

- DOI: 10.1073/pnas.2402946121 | PMCID: PMC11388380 | PMID: 39213181
- Version used: **2.2.7.1**
- Evidence: Genome-wide regions of open chromatin enrichment were identified using MACS2 (v.2.2.7.1) program with the following parameters: –nomodel, –shift-100 –extsize 200-B-q 0.05 ( 53 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [Trimmomatic] -> alignment/mapping [Bismark, Bowtie2, SAMtools] -> quantification [ImageJ, edgeR] -> dimensionality reduction/clustering [R, clusterProfiler] -> structure determination [SAMtools] -> visualisation [deepTools] -> stage not stated [BEDTools, MACS2 v2.2.7.1, OrthoFinder, Picard v1.112]

### Platelet-activating factor (PAF) promotes immunosuppressive neutrophil differentiation within tumors. (PNAS 2024)

- DOI: 10.1073/pnas.2406748121 | PMCID: PMC11363292 | PMID: 39178229
- Evidence: Anti-Ly-6G Microbeads (Miltenyi Biotec) were added to cell suspension and passed through MACS LC columns (Miltenyi Biotec) to capture neutrophils.
- Full pipeline: alignment/mapping [STAR] -> quantification [STAR] -> normalisation [DESeq2, pheatmap v1.0.12] -> differential/statistical testing [DESeq2] -> stage not stated [MACS2]

### Oxysterol binding protein regulates the resolution of TLR-induced cytokine production in macrophages. (PNAS 2024)

- DOI: 10.1073/pnas.2406492121 | PMCID: PMC11331125 | PMID: 39361877
- Version used: **2.1.0**
- Evidence: Broad peaks were called using MACS2 (2.1.0) ( 54 ).
- Full pipeline: quality control [FastQC v0.11.5] -> quantification [ImageJ, limma] -> normalisation [edgeR v3.26.8] -> differential/statistical testing [R, edgeR v3.26.8, limma] -> stage not stated [GSEA, MACS2 v2.1.0, featureCounts]

### ZNF91 is an endogenous repressor of the molecular phenotype associated with X-linked dystonia-parkinsonism (XDP). (PNAS 2024)

- DOI: 10.1073/pnas.2401217121 | PMCID: PMC11331120 | PMID: 39102544
- Evidence: To determine the relation between ZNF91 affinity and promoter targets, MACS score and the relative distance to a TSS for each binding site were plotted.
- Full pipeline: quality control [Bowtie2 v2.3.4.2] -> read trimming [BWA, fastp] -> alignment/mapping [BWA, Bowtie2 v2.3.4.2, featureCounts] -> normalisation [DESeq2, deepTools] -> visualisation [MACS2, deepTools] -> stage not stated [Galaxy, RepeatMasker, SAMtools]

### Intratumoral NKT cell accumulation promotes antitumor immunity in pancreatic cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2403917121 | PMCID: PMC11260137 | PMID: 38980903
- Evidence: 2 × 10 7 hepatic lymphocytes were centrifuged at 450 g, at 4 °C for 5 min, and resuspended in 500 μL MACS buffer (0.5% BSA, 2 mM EDTA in PBS) containing biotinylated anti-mouse CD8, CD19, CD11b, CD11c, Gr1, TCRγδ, TER-119, CD62L, CD24, and CD49b, and FcR blocking antibodies ( SI Appendix , Table S2 ).
- Full pipeline: quality control [FastQC, RSEM] -> stage not stated [GSEA, ImageJ, MACS2]

### Insulin receptor orchestrates kidney antibacterial defenses. (PNAS 2024)

- DOI: 10.1073/pnas.2400666121 | PMCID: PMC11260129 | PMID: 38976738
- Evidence: ICs and PCs were enriched using FACS or MACS following established protocols ( 6 , 13 , 14 ).
- Full pipeline: differential/statistical testing [Metascape] -> stage not stated [MACS2]

### High-throughput screen identifies non inflammatory small molecule inducers of trained immunity. (PNAS 2024)

- DOI: 10.1073/pnas.2400413121 | PMCID: PMC11260140 | PMID: 38976741
- Evidence: Model-based analysis for ChIP-Seq (MACS2) callpeak (Version 2.2.7.1) in Python (Anaconda 2020.11) was used to distinguish any peaks from background observed in all samples ( 48 ).
- Full pipeline: quality control [FastQC, R] -> read trimming [Bowtie2] -> alignment/mapping [Bowtie2] -> differential/statistical testing [HOMER, edgeR, limma] -> stage not stated [BEDTools, Conda v2020.11, MACS2, Python, SAMtools, fgsea]

### An atlas of the tomato epigenome reveals that KRYPTONITE shapes TAD-like boundaries through the control of H3K9ac distribution. (PNAS 2024)

- DOI: 10.1073/pnas.2400737121 | PMCID: PMC11252963 | PMID: 38968127
- Version used: **2.2.7.1**
- Evidence: MACS2 v 2.2.7.1 was used for peak detection ( 44 ).
- Full pipeline: read trimming [Trimmomatic v0.38] -> alignment/mapping [Bismark v0.24.0, Bowtie2 v2.3.5] -> differential/statistical testing [BEDTools v2.28.0] -> stage not stated [HOMER v4.11, MACS2 v2.2.7.1, R, deepTools v3.5.0]

### The TOX-RAGE axis mediates inflammatory activation and lung injury in severe pulmonary infectious diseases. (PNAS 2024)

- DOI: 10.1073/pnas.2319322121 | PMCID: PMC11214053 | PMID: 38900789
- Evidence: And Pan T cells, monocytes, Neutrophils were isolated using MACS Pan T cell isolation kit (130-096-535, Miltenyi Biotec), Classical monocyte isolation kit (130-117-337, Miltenyi Biotec), MACSxpress Whole blood neutrophil isolation kit (130-104-434, Miltenyi Biotec), respectively.
- Full pipeline: stage not stated [ImageJ v1.43, MACS2]

### Cancer-stromal cell interactions in breast cancer brain metastases induce glycocalyx-mediated resistance to HER2-targeting therapies. (PNAS 2024)

- DOI: 10.1073/pnas.2322688121 | PMCID: PMC11098130 | PMID: 38709925
- Version used: **2.1.1.20160309**
- Evidence: These reads were used to generate binding sites with Model-Based Analysis of ChIP-Seq 2 (MACS v2.1.1.20160309), with a q-value false discovery rate (FDR) threshold of 0.01 ( 54 ).
- Full pipeline: quality control [STAR] -> alignment/mapping [STAR] -> quantification [DESeq2 v1.18.1] -> normalisation [edgeR] -> differential/statistical testing [DESeq2 v1.18.1, MACS2 v2.1.1.20160309] -> stage not stated [GSEA, GSVA]

### Class IIa HDAC4 and HDAC7 cooperatively regulate gene transcription in Th17 cell differentiation. (PNAS 2024)

- DOI: 10.1073/pnas.2312111121 | PMCID: PMC11067014 | PMID: 38657041
- Evidence: Notably, Th17 cell differentiation was performed for murine cells after MACS isolation without blocking antibodies for IL-12, IFNγ, or IL-4.
- Full pipeline: stage not stated [HOMER, MACS2]

### The Myc-associated zinc finger protein epigenetically controls expression of interferon-γ-stimulated genes by recruiting STAT1 to chromatin. (PNAS 2024)

- DOI: 10.1073/pnas.2320938121 | PMCID: PMC11046693 | PMID: 38635637
- Version used: **2.2.7.1**
- Evidence: MACS2 version 2.2.7.1 was employed to detect peaks.
- Full pipeline: quality control [FastQC v0.11.9, fastp] -> alignment/mapping [Bowtie2] -> quantification [DESeq2 v1.32.0, R] -> normalisation [deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2 v1.32.0, R] -> stage not stated [BEDTools, HOMER, MACS2 v2.2.7.1]

### APOBEC2 safeguards skeletal muscle cell fate through binding chromatin and regulating transcription of non-muscle genes during myoblast differentiation. (PNAS 2024)

- DOI: 10.1073/pnas.2312330121 | PMCID: PMC11047093 | PMID: 38625936
- Evidence: To determine the location of bound APOBEC2 within chromatin, we performed chromatin immunoprecipitation-sequencing (ChIP-Seq) experiments, and calculated enrichment of APOBEC2 at specific loci over input using MACS2 ( 41 , 42 ).
- Full pipeline: alignment/mapping [Bioconductor] -> quantification [ImageJ, R] -> dimensionality reduction/clustering [clusterProfiler] -> stage not stated [DESeq2, MACS2]

### Autoimmunity against melanoma differentiation-associated gene 5 induces interstitial lung disease mimicking dermatomyositis in mice. (PNAS 2024)

- DOI: 10.1073/pnas.2313070121 | PMCID: PMC11032490 | PMID: 38588434
- Evidence: Then, the incubated cells were negatively sorted to CD3 + T cells using MACS magnetic beads (Miltenyi Biotec).
- Full pipeline: differential/statistical testing [Metascape] -> stage not stated [GSEA, MACS2]

### The genetic regulatory architecture and epigenomic basis for age-related changes in rattlesnake venom. (PNAS 2024)

- DOI: 10.1073/pnas.2313440121 | PMCID: PMC11032440 | PMID: 38578985
- Version used: **2.2.7.1**
- Evidence: Peaks were called with MACS2 v2.2.7.1 ( 85 ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v3.4, Trim Galore] -> alignment/mapping [Bowtie2, HISAT2 v2.2.1, SAMtools] -> quantification [DESeq2 v1.32.0, HTSeq] -> stage not stated [BUSCO, Canu, MACS2 v2.2.7.1, Picard, hifiasm]

### Timeless noncoding DNA contains cell-type preferential enhancers important for proper Drosophila circadian regulation. (PNAS 2024)

- DOI: 10.1073/pnas.2321338121 | PMCID: PMC11009632 | PMID: 38568969
- Evidence: ChIP-seq libraries were sequenced on a Nextseq 550 (Illumina) and the resulting datasets were mapped to the Drosophila genome (dm6) using Bowtie2 and analyzed using MACS2 ( 51 , 52 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2, MACS2] -> stage not stated [BEDTools, Cellpose, DESeq2, SAMtools]

### Transcription factor C/EBPα is required for the development of Ly6C&lt;sup&gt;hi&lt;/sup&gt; monocytes but not Ly6C&lt;sup&gt;lo&lt;/sup&gt; monocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2315659121 | PMCID: PMC11009651 | PMID: 38564635
- Evidence: All procedures for cell staining were performed in PBS supplemented with 2 % of FBS and 2 mM EDTA (MACS buffer).
- Full pipeline: stage not stated [MACS2]

### Cell division machinery drives cell-specific gene activation during differentiation in <i>Bacillus subtilis</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2400584121 | PMCID: PMC10990147 | PMID: 38502707
- Evidence: Coimmunoprecipitation was performed using the µMACS kit (Miltenyi Biotec).
- Full pipeline: registration [ImageJ] -> stage not stated [MACS2]

### Vulnerability to APOBEC3G linked to the pathogenicity of deltaretroviruses. (PNAS 2024)

- DOI: 10.1073/pnas.2309925121 | PMCID: PMC10990082 | PMID: 38502701
- Evidence: To detect significant peaks in comparison to input DNA, we used MACS2 ( 59 ) with a cutoff p-value less than 1e-5.
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [MACS2] -> visualisation [SAMtools, deepTools] -> stage not stated [GSEA, ImageJ, Picard, RSEM, edgeR]

### Absence of chromosome axis protein recruitment prevents meiotic recombination chromosome-wide in the budding yeast <i>Lachancea kluyveri</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2312820121 | PMCID: PMC10962940 | PMID: 38478689
- Evidence: We used the MACS2 peak calling algorithm to define the Spo11-DSB hotspots ( 57 ).
- Full pipeline: stage not stated [MACS2]

### Machine learning to predict continuous protein properties from binary cell sorting data and map unseen sequence space. (PNAS 2024)

- DOI: 10.1073/pnas.2311726121 | PMCID: PMC10945751 | PMID: 38451939
- Evidence: This library was sorted using a combination of MACS and FACS as follows: one round of expression MACS, two rounds of affinity MACS, two rounds of affinity FACS, and two rounds of specificity FACS.
- Full pipeline: normalisation [scikit-learn] -> machine learning [PyTorch] -> stage not stated [MACS2, NumPy]

### A magnetic separation method for isolating and characterizing the biomolecular corona of lipid nanoparticles. (PNAS 2024)

- DOI: 10.1073/pnas.2307803120 | PMCID: PMC10945860 | PMID: 38437542
- Evidence: MS was performed using a MACS® Cell Separation system composed of MidiMACS Separator, MultiStand, and LD or LS MACS Columns (Miltenyi Biotec Inc.
- Full pipeline: stage not stated [MACS2]

### IL-27 regulates the differentiation of follicular helper NKT cells via metabolic adaptation of mitochondria. (PNAS 2024)

- DOI: 10.1073/pnas.2313964121 | PMCID: PMC10907256 | PMID: 38394242
- Evidence: Cells were subsequently incubated with streptavidin nanobeads (BioLegend) and separated using a LS column (Miltenyi Biotec) in the magnetic field of a MACS Separator (Miltenyi Biotec).
- Full pipeline: read trimming [fastp] -> differential/statistical testing [GSEA] -> stage not stated [ImageJ, MACS2]

### Metabolism of host lysophosphatidylcholine in <i>Plasmodium falciparum</i>-infected erythrocytes. (PNAS 2024)

- DOI: 10.1073/pnas.2320262121 | PMCID: PMC10895272 | PMID: 38349879
- Evidence: MACS Purification and TAMRA-FP Analysis.
- Full pipeline: stage not stated [MACS2]

### COP1 controls light-dependent chromatin remodeling. (PNAS 2024)

- DOI: 10.1073/pnas.2312853121 | PMCID: PMC10895365 | PMID: 38349881
- Evidence: Peak calling used MACS2 and applied q < 0.01.
- Full pipeline: alignment/mapping [Bowtie2, HISAT2, deepTools] -> normalisation [deepTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [ImageJ, MACS2]

### Cell-intrinsic C5a synergizes with Dectin-1 in macrophages to mediate fungal killing. (PNAS 2024)

- DOI: 10.1073/pnas.2314627121 | PMCID: PMC10835034 | PMID: 38252818
- Evidence: Human CD14+ monocytes were isolated from blood using Lymphoprep density centrifugation (STEMCELL) followed by CD14+ MACS magnetic bead separation (Miltenyi Biotec).
- Full pipeline: stage not stated [MACS2]

### γδ T cell antigen receptor polyspecificity enables T cell responses to a broad range of immune challenges. (PNAS 2024)

- DOI: 10.1073/pnas.2315592121 | PMCID: PMC10823224 | PMID: 38227652
- Evidence: The enriched cells were collected from unlabeled cells that passed through MACS column (Miltenyi) and then stained with Cy3-OVA (60 μg/mL), Alexa Fluor 405-labeled HA peptide SAv-dextramer (0.45 μM) on ice for 1 h.
- Full pipeline: stage not stated [MACS2]

### Lysophagy protects against propagation of α-synuclein aggregation through ruptured lysosomal vesicles. (PNAS 2024)

- DOI: 10.1073/pnas.2312306120 | PMCID: PMC10769825 | PMID: 38147546
- Evidence: Primary cortical neurons were collected from E15.5 C57BL/6 J mouse pups, dissociated using a papain dissociation system (Worthington Biochemical Corporation, LK003150 ), and cultured on both sides of the microfluidics chamber in MACS Neuro Medium (Miltenyi Biotec, 130-093-570) supplemented with NeuroBrew B21 (Miltenyi Biotec, 130-097-263), 1% GlutaMAX (Thermo Fisher Scientific, 35050-061), and 1% ...
- Full pipeline: stage not stated [MACS2]

### WDFY4-dependent cross-presentation proceeds via a vacuolar antigen-processing route. (PNAS 2025)

- DOI: 10.1073/pnas.2519922122 | PMCID: PMC12718357 | PMID: 41364771
- Evidence: Dendritic cells were then enriched by positive selection using CD11c microbeads and MACS LS column (Miltenyi Biotec, 130–125-835) Antigen Preparation.
- Full pipeline: stage not stated [MACS2]

### Distinct transcription factor interactions drive HOXB13 activity in different stages of prostate cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2500327122 | PMCID: PMC12704779 | PMID: 41343677
- Version used: **3.0.0a**
- Evidence: ChIPseq: Binding regions were called with MACS3 (v3.0.0a6) ( 52 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.11] -> alignment/mapping [BWA v0.7.17] -> quantification [ImageJ] -> normalisation [edgeR v3.36.0] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [scikit-learn] -> stage not stated [BEDTools v2.30.0, GSVA, MACS2 v3.0.0a, Metascape]

### TGFBR2 coordinates the endometrial response to estrogen, regulating endometrial hyperplasia and fertility. (PNAS 2025)

- DOI: 10.1073/pnas.2518507122 | PMCID: PMC12704753 | PMID: 41337483
- Evidence: We reanalyzed publicly available murine uterine ER ChIP-seq and SMAD4 CUT&RUN datasets, realigning them to the same reference genome (mm10) and calling peaks with MACS2 ( Dataset S3 ) ( 14 , 78 ).
- Full pipeline: alignment/mapping [MACS2] -> registration [MACS2]

### Lineage tracing of both quiescent G0 and active Hoxb5+ LT-HSCs that actively contribute to homeostatic mouse hematopoiesis. (PNAS 2025)

- DOI: 10.1073/pnas.2513724122 | PMCID: PMC12704723 | PMID: 41325518
- Evidence: To enrich for c-Kit positive LT-HSCs, cells were stained with c-KIT APC-Cy7 antibody (BioLegend, 105826) and conjugated to anti-APC microbeads (BioLegend, 100414) before undergoing MACS separation using LS columns (Miltenyi, 130-042-401).
- Full pipeline: stage not stated [MACS2]

### Nanorate sequencing reveals the &lt;i&gt;Arabidopsis&lt;/i&gt; somatic mutation landscape. (PNAS 2025)

- DOI: 10.1073/pnas.2514194122 | PMCID: PMC12685076 | PMID: 41296725
- Evidence: Peaks were called for each replicate using MACS2 callpeak -g 1.1e8 -q 0.7 --nomodel --extsize 200 --shift -100 ( 112 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [Bowtie2] -> stage not stated [MACS2, SAMtools, SciPy, Snakemake]

### Growth hormone regulates the stem cell population in the growth plate. (PNAS 2025)

- DOI: 10.1073/pnas.2512316122 | PMCID: PMC12685065 | PMID: 41289405
- Evidence: Images were processed with MACS iQ View (Miltenyi Biotec) and analyzed using Imaris v10.0.1 (Bitplane).
- Full pipeline: quantification [ImageJ] -> stage not stated [MACS2]

### Targeting orthotopic and metastatic pancreatic cancer with allogeneic stem cell-engineered mesothelin-redirected CAR-NKT cells. (PNAS 2025)

- DOI: 10.1073/pnas.2517786122 | PMCID: PMC12664011 | PMID: 41269799
- Evidence: Healthy donor PBMCs were sorted with MACS via a Human NK Cell Isolation Kit (Miltenyi Biotech) to enrich NK cells, following the manufacturer’s instructions.
- Full pipeline: stage not stated [MACS2]

### Extracellular nanobody screening using conformationally stable GPCR variants. (PNAS 2025)

- DOI: 10.1073/pnas.2508879122 | PMCID: PMC12625997 | PMID: 41187083
- Evidence: Nanobody clones targeting the different purified FLAG-tagged M1R constructs were enriched through two rounds of MACS and two or three rounds of FACS using FACSAria II (BD Biosciences) in selection buffer (20 mM HEPES pH 7.5, 100 mM NaCl, 0.05% MNG, 0.005% CHS, 2 mM CaCl 2 , 0.1% (w/v) bovine serum albumin and 0.2% maltose), as previously reported ( Fig.
- Full pipeline: structure determination [ChimeraX] -> stage not stated [AlphaFold, MACS2, PHENIX]

### Aberrant X chromosome dosage compensation causes hybrid male inviability in &lt;i&gt;Caenorhabditis&lt;/i&gt;. (PNAS 2025)

- DOI: 10.1073/pnas.2507166122 | PMCID: PMC12582268 | PMID: 41129226
- Version used: **3.0.0**
- Evidence: Sequencing data were analyzed with standard pipelines FASTQC(v0.12.1), Trimmomatic(v0.39) ( 52 ), fastp(v1.0.1) ( 53 ), HISAT2(v2.21) ( 54 ), bowtie2(v2.4.5) ( 55 ), featureCounts(v2.0.6) ( 56 ), StringTie(v2.2.3) ( 57 ), MACS3(v3.0.0) ( 58 ), deepTools(v3.4.1) ( 59 ), ChIPseeker(v1.44.0) ( 60 ) and custom pipelines for orthology mapping, transcript model revision, and phylogenetic analysis.
- Full pipeline: quality control [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> read trimming [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6] -> alignment/mapping [Bowtie2 v2.4.5, HISAT2 v2.21, MACS2 v3.0.0, StringTie v2.2.3, Trimmomatic v0.39, deepTools v3.4.1, fastp v1.0.1, featureCounts v2.0.6]

### Functional genetic elements of a butterfly mimicry supergene. (PNAS 2025)

- DOI: 10.1073/pnas.2509864122 | PMCID: PMC12541413 | PMID: 41060750
- Evidence: CUT&RUN peaks were identified using MACS3 and IgG as the control track ( 59 ).
- Full pipeline: stage not stated [Flye, HOMER v4.11, MACS2]

### A time-gated PKA-CREB signaling circuit licenses IL-12 responsiveness and Th1 fate in CD4&lt;sup&gt;+&lt;/sup&gt; T cells. (PNAS 2025)

- DOI: 10.1073/pnas.2517132122 | PMCID: PMC12541411 | PMID: 41052344
- Version used: **2.2.7.1**
- Evidence: Peak calling to identify open chromatin regions was performed using MACS2 (v2.2.7.1) with a q-value threshold of 0.05.
- Full pipeline: alignment/mapping [Bowtie2] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [GSEA, MACS2 v2.2.7.1, Picard, R, SAMtools, deepTools]

### Nuclear receptor coregulator NRIP1 R448G modulates T cell gut homing to control intestinal inflammation. (PNAS 2025)

- DOI: 10.1073/pnas.2508269122 | PMCID: PMC12478152 | PMID: 40966276
- Evidence: After washing, cells were resuspended in MACS buffer with 7-AAD (BioLegend, 1:50) for sorting by BD FACSAria II with FACS Diva 6.1.
- Full pipeline: quality control [SCENIC] -> alignment/mapping [Bowtie2, kallisto] -> variant calling [HOMER] -> quantification [kallisto] -> dimensionality reduction/clustering [SCENIC, UMAP] -> differential/statistical testing [GSEA, HOMER, edgeR] -> visualisation [SCENIC] -> stage not stated [AnnData v0.8.0, BEDTools, MACS2, Scanpy v1.9.1, Seurat v1.9.0, Signac v4.3.0]

### Adaptation of seed dormancy to maternal climate occurs via intergenerational transport of abscisic acid. (PNAS 2025)

- DOI: 10.1073/pnas.2519319122 | PMCID: PMC12452922 | PMID: 40932768
- Evidence: Peaks were called using MACS3 ( 55 ), based on the threshold of FDR < 0.05.
- Full pipeline: read trimming [Bowtie2, Cutadapt, featureCounts] -> alignment/mapping [Bowtie2, Cutadapt, SAMtools, deepTools, featureCounts] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [MACS2, edgeR] -> visualisation [SAMtools, UMAP, deepTools] -> stage not stated [ImageJ, Seurat]

### Sorting nexin 3 promotes ischemic retinopathy through RIP1- and RIP3-mediated myeloid cell necroptosis and mitochondrial fission. (PNAS 2025)

- DOI: 10.1073/pnas.2426578122 | PMCID: PMC12452880 | PMID: 40924459
- Evidence: ( N – Q ) RT-PCR ( O , n = 6) and western blot ( P and Q , n = 5) analyses of the levels of SNX3 in CD11b + cells isolated from retinas of RA and OIR mice using MACS separation.
- Full pipeline: quantification [ImageJ] -> dimensionality reduction/clustering [Seurat] -> stage not stated [MACS2]

### Modeling human retinal ganglion cell axonal outgrowth, development, and pathology using pluripotent stem cell-based microfluidic platforms. (PNAS 2025)

- DOI: 10.1073/pnas.2423682122 | PMCID: PMC12452894 | PMID: 40924455
- Evidence: It is also important to consider that the somatodendritic chamber of the microfluidic platforms was seeded with RGCs that were highly enriched from cultures following MACS purification, but this does not necessarily mean that other cell types were not present.
- Full pipeline: stage not stated [ImageJ, MACS2]

### Dynamic and precise electromagnetic levitation of single cells. (PNAS 2025)

- DOI: 10.1073/pnas.2512246122 | PMCID: PMC12452889 | PMID: 40920932
- Evidence: FACS subjects cells to high shear pressures, reducing postsorting viability, while MACS requires cell attachment to beads that can damage cell membranes ( 35 – 38 ).
- Full pipeline: stage not stated [MACS2, Python]

### PD-1 expression identifies proliferating malignant CLL B cells and is a potential biomarker of response to BTK inhibitor therapy. (PNAS 2025)

- DOI: 10.1073/pnas.2426935122 | PMCID: PMC12435283 | PMID: 40906805
- Evidence: PBMCs were washed three times with Dulbecco’s phosphate buffer saline without calcium or magnesium (DPBS) plus 2% fetal bovine serum (FBS) and 2 mM EDTA (MACS buffer) after lysis of red blood cells using ACK lysing buffer (Lonza), suspended in 90% FBS plus 10% DMSO, frozen in freezing chambers at −80˚C, and then transferred to liquid nitrogen for long term storage.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [HTSeq, Trimmomatic] -> quantification [DESeq2 v1.40.2, HTSeq, R] -> normalisation [DESeq2 v1.40.2, R] -> dimensionality reduction/clustering [ComplexHeatmap] -> differential/statistical testing [DESeq2 v1.40.2, R] -> stage not stated [GSEA, GSVA, MACS2]

### TRIM24 as a therapeutic target in endocrine treatment-resistant breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2507571122 | PMCID: PMC12377727 | PMID: 40815626
- Version used: **2.1.2**
- Evidence: MACS2 (v2.1.2) was used to perform peak calling over input ChIP-seq samples in both single-end and paired-end mode (respective to the type of experiment).
- Full pipeline: quality control [DESeq2] -> alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> visualisation [SAMtools] -> stage not stated [GSEA, MACS2 v2.1.2, deepTools v2.5.3]

### RNA polymerase III transcription-associated polyadenylation promotes the accumulation of noncoding retrotransposons during infection. (PNAS 2025)

- DOI: 10.1073/pnas.2507186122 | PMCID: PMC12358842 | PMID: 40768347
- Evidence: Given the repetitive, degenerate, and arrayed nature of most Pol III transcribed genes, we applied stringent mapping criteria and called peaks using MACS2 ( 52 ).
- Full pipeline: alignment/mapping [MACS2] -> quantification [PyTorch, RepeatMasker]

### Cancer cells suppress NK cell activity by actin-driven polarization of inhibitory ligands to the immunological synapse. (PNAS 2025)

- DOI: 10.1073/pnas.2503259122 | PMCID: PMC12358872 | PMID: 40763024
- Evidence: After washing in MACS buffer (Miltenyi Biotec #130-091-221), Fc receptor blocking solution (Human TruStain FcX, BioLegend #422302) was added for 10 min to minimize nonspecific binding.
- Full pipeline: quantification [ImageJ v1.53t] -> stage not stated [MACS2]

### SMARCA5 restricts chromatin accessibility to promote male meiosis and fertility in mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422356122 | PMCID: PMC12337329 | PMID: 40743397
- Evidence: Bigwig tracks were generated using bamcoverage from the deeptools package and peaks were called using MACS2 ( 60 ) with the –broadpeak option.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Bowtie2, Picard] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, ImageJ, MACS2, Seurat v4.1.0, SoupX, deepTools, ggplot2]

### WT1 directs normal progesterone receptor-chromatin binding essential for uterine receptivity at peri-implantation. (PNAS 2025)

- DOI: 10.1073/pnas.2504361122 | PMCID: PMC12280917 | PMID: 40627402
- Evidence: Peak calling was performed using MACS2 with default and recommended parameters (FDR threshold = 0.05).
- Full pipeline: quality control [Trim Galore] -> alignment/mapping [Bowtie2] -> differential/statistical testing [DESeq2, MACS2] -> stage not stated [HOMER, deepTools, ggplot2, pheatmap]

### Tandem ssDNA in neutrophil extracellular traps binds thrombin and regulates immunothrombosis. (PNAS 2025)

- DOI: 10.1073/pnas.2418191122 | PMCID: PMC12260427 | PMID: 40608679
- Version used: **2.2.7.1**
- Evidence: Peaks were then called using MACS2 (v2.2.7.1) ( 76 ) by comparing thrombin pulldown samples to input controls (parameters: -q 0.01 --nomodel).
- Full pipeline: quality control [FastQC v0.11.9] -> alignment/mapping [SAMtools v1.6] -> stage not stated [BEDTools v2.30.0, ImageJ, MACS2 v2.2.7.1]

### JunB-HBZ nuclear translocation by TGF-β is a key driver in HTLV-1-mediated leukemogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2420756122 | PMCID: PMC12232710 | PMID: 40549917
- Evidence: ChIP-seq peaks were assessed by MACS2 ( 65 ) with the “−p 1e-5” option using the corresponding input-sequenced file as a control.
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, SAMtools, Trimmomatic] -> differential/statistical testing [GSEA, RSEM, edgeR] -> visualisation [deepTools] -> stage not stated [BEDTools, ImageJ, MACS2, Picard, R]

### Direct sensing of host ferric iron by an archetype histidine kinase mediates virulence of an enteric pathogen. (PNAS 2025)

- DOI: 10.1073/pnas.2507874122 | PMCID: PMC12167987 | PMID: 40465626
- Evidence: We identified 73 enriched loci harboring OmpR-binding peaks (enriched >1.5-fold compared with the control sample) using MACS software ( Fig.
- Full pipeline: stage not stated [AlphaFold, MACS2]

### Jund orchestrates &lt;i&gt;cis&lt;/i&gt;-regulatory element dynamics to facilitate endothelial-to-hematopoietic transition. (PNAS 2025)

- DOI: 10.1073/pnas.2426714122 | PMCID: PMC12167990 | PMID: 40472028
- Evidence: MACS2 ( 62 ) (Version 2.2.7.1) was used for the peak calling.
- Full pipeline: read trimming [Bowtie2] -> alignment/mapping [Bowtie2, SAMtools] -> dimensionality reduction/clustering [Metascape, UMAP, clusterProfiler] -> visualisation [Cytoscape] -> stage not stated [ArchR, DESeq2, ImageJ, MACS2, R, SCENIC, Seurat, Trim Galore, deepTools, scDblFinder]

### &lt;i&gt;LMX1B&lt;/i&gt; missense-perturbation of regulatory element footprints disrupts serotonergic forebrain axon arborization. (PNAS 2025)

- DOI: 10.1073/pnas.2411716122 | PMCID: PMC12002326 | PMID: 40168115
- Evidence: Peaks of accessible chromatin regions for each sample were called with MACS2 using the parameters “--gsize mm --nomodel --shift -100 --extsize 200 -broad.” Peaks were annotated to genes using UROPA v4.0.2 ( 60 ) up to a limit of 50 kb.
- Full pipeline: alignment/mapping [SAMtools] -> stage not stated [MACS2, R v4.3, ggplot2 v3.4.4]

### Nuclear Galectin-1 promotes &lt;i&gt;KRAS&lt;/i&gt;-dependent activation of pancreatic cancer stellate cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424051122 | PMCID: PMC12002210 | PMID: 40172967
- Evidence: The MACS peak calling model was generated with an upper MFOLD range of 32 to identify high-confidence enrichment regions in comparison to background signal (ChIP-seq IgG IP control file).
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2] -> stage not stated [ImageJ, MACS2]

### Single cell-resolved cellular, transcriptional, and epigenetic changes in mouse T cell populations linked to age-associated immune decline. (PNAS 2025)

- DOI: 10.1073/pnas.2425992122 | PMCID: PMC12002302 | PMID: 40163732
- Evidence: Clusters were annotated by integrating scRNA-seq data from the same mice, with MACS2 used for peak calling in each CD8+ cluster.
- Full pipeline: quality control [Scanpy v1.4.6] -> normalisation [Seurat] -> dimensionality reduction/clustering [ArchR v1.0.1, MACS2, Seurat, UMAP]

### Pulsatile flow induces chromatin interaction with lamin-associated proteins to enrich H3K9 methylation in endothelial cells. (PNAS 2025)

- DOI: 10.1073/pnas.2424566122 | PMCID: PMC11962468 | PMID: 40117319
- Evidence: Peaks were called using MACS2.
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt] -> alignment/mapping [Bowtie2] -> stage not stated [HOMER, ImageJ, MACS2, OpenCV]

### Wdr5-mediated H3K4 methylation facilitates HSPC development via maintenance of genomic stability in zebrafish. (PNAS 2025)

- DOI: 10.1073/pnas.2420534122 | PMCID: PMC11962412 | PMID: 40112113
- Version used: **2.2.7.1**
- Evidence: After filtering low quality reads (q ≥ 30) by samtools (version 1.9), MACS2 (version 2.2.7.1) was used for the peak calling.
- Full pipeline: read trimming [MACS2 v2.2.7.1] -> alignment/mapping [Bowtie2 v2.3.5.1, HTSeq v0.13.5, SAMtools v1.9] -> quantification [HTSeq v0.13.5, ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [deepTools, ggplot2] -> stage not stated [GSEA v4.0.3]

### Ectopic germinal centers in the nasal turbinates contribute to B cell immunity to intranasal viral infection and vaccination. (PNAS 2025)

- DOI: 10.1073/pnas.2421724122 | PMCID: PMC11962485 | PMID: 40112112
- Evidence: The tissues were placed into gentle-MACS C Tubes (Miltenyi Biotec) or Eppendorf tubes 1.5 mL with RPMI 1640 Medium (#22400089; Gibco) containing 30 μg/mL Collagenase (#05401127001; Roche) and 3 μg/mL DNAse (Cat.
- Full pipeline: dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [MACS2, Seurat]

### Androgen receptors in corticotropin-releasing hormone neurons mediate the sexual dimorphism in restraint-induced thymic atrophy. (PNAS 2025)

- DOI: 10.1073/pnas.2426107122 | PMCID: PMC11962470 | PMID: 40106355
- Evidence: Single-cell suspensions of thymocytes were prepared and incubated in ice-cold MACS buffer (PBS with 1 mM EDTA and 2% FBS) containing 10 μg/mL CD16/CD32 antibody (553142, Clone 2.4G2, BD PharMingen) for 30 min at 4 °C.
- Full pipeline: stage not stated [MACS2]

### The <i>Arabidopsis</i> demethylase REF6 physically interacts with phyB to promote hypocotyl elongation under red light. (PNAS 2025)

- DOI: 10.1073/pnas.2417253122 | PMCID: PMC11929476 | PMID: 40063793
- Version used: **2.2.6**
- Evidence: Peaks were identified by MACS2 (version 2.2.6) ( 84 ), and annotated to their nearest TSS using Bedtools and custom Perl scripts.
- Full pipeline: read trimming [HISAT2 v2.2.1, Trim Galore v0.6.6] -> alignment/mapping [Bowtie2 v2.3.5.1, HISAT2 v2.2.1, Trim Galore v0.6.6, featureCounts v2.0.0] -> quantification [ggplot2, tidyverse] -> normalisation [ggplot2, tidyverse] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [deepTools v3.3.2] -> stage not stated [MACS2 v2.2.6, SAMtools v1.10]

### Epitope-directed selection of GPCR nanobody ligands with evolvable function. (PNAS 2025)

- DOI: 10.1073/pnas.2423931122 | PMCID: PMC11929449 | PMID: 40067891
- Evidence: A total of 4 × 10 8 yeast cells were subjected to a second round of MACS with AlexaFlour647-labeled M1-αFLAG antibody and anti-AlexaFlour647 microbeads.
- Full pipeline: structure determination [Coot, PHENIX] -> visualisation [UCSF Chimera] -> stage not stated [MACS2]

### A mechanistic basis for genetic assimilation in natural fly populations. (PNAS 2025)

- DOI: 10.1073/pnas.2415982122 | PMCID: PMC11929479 | PMID: 40063800
- Evidence: Peak calling was performed with each replicate as a separate input file and IgG as the control library using MACS2 ( 51 ) with the following parameters: -g dm -f BAMPE -q 0.01.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.2, Clustal Omega, STAR v2.7.0] -> quantification [featureCounts] -> stage not stated [BEDTools v2.30.0, DESeq2, GATK, MACS2, R]

### Dynamic investigation of hypoxia-induced L-lactylation. (PNAS 2025)

- DOI: 10.1073/pnas.2404899122 | PMCID: PMC11912421 | PMID: 40030031
- Evidence: MACS2 software was used for peak calling.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [Fiji, ImageJ, MACS2]

### CTCF regulates global chromatin accessibility and transcription during rod photoreceptor development. (PNAS 2025)

- DOI: 10.1073/pnas.2416384122 | PMCID: PMC11892594 | PMID: 39993185
- Version used: **2.2.6**
- Evidence: ATAC-seq peak calling was performed with MACS2 (v2.2.6; pair-end mode -f BAMPE), and differential accessibility was called with the R package DiffBind v3 with default parameters.
- Full pipeline: read trimming [Bowtie2 v2.3.5, Cutadapt v1.10, HISAT2 v2.0.4] -> alignment/mapping [Bowtie2 v2.3.5, HISAT2 v2.0.4, Picard, SAMtools v1.9] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, HISAT2 v2.0.4, MACS2 v2.2.6, R] -> stage not stated [featureCounts v1.5.0]

### Structural variant and nucleosome occupancy dynamics postchemotherapy in a HER2+ breast cancer organoid model. (PNAS 2025)

- DOI: 10.1073/pnas.2415475122 | PMCID: PMC11892646 | PMID: 39993200
- Evidence: Peak calling was performed using MACS2 ( 55 ) for each of the cell lines and combined into the consensus peaks using bedtools to define cis-regulatory regions (CREs) ( 56 ).
- Full pipeline: alignment/mapping [Bowtie2] -> stage not stated [BEDTools, MACS2]

### Substance P receptor signaling contributes to host maladaptive responses during enteric bacterial infection. (PNAS 2025)

- DOI: 10.1073/pnas.2415287122 | PMCID: PMC11848390 | PMID: 39937862
- Evidence: Tissue was digested using MACS digestion enzyme mix as described in manufacturer’s protocol and reduced to a single-cell suspension by the gentleMACS device.
- Full pipeline: stage not stated [ImageJ, MACS2]

### Intercellular mRNA transfer alters the human pluripotent stem cell state. (PNAS 2025)

- DOI: 10.1073/pnas.2413351122 | PMCID: PMC11789055 | PMID: 39841146
- Evidence: After naïve conversion, SUSD2-positive cells with the labeled fluorescent reporter expression were sorted either with FACS or MACS for further characterization.
- Full pipeline: stage not stated [MACS2]

### The chromatin remodeler ADNP regulates neurodevelopmental disorder risk genes and neocortical neurogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2405981122 | PMCID: PMC11760920 | PMID: 39808658
- Evidence: Using MACS2 ( 41 ) to call peaks on both datasets, we found that Chd4 occupied 18,564 genomic loci, whereas the published Adnp cut&run-seq dataset yielded 4,679 peaks.
- Full pipeline: variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [MACS2]

### Mitochondrial DNA lineages determine tumor progression through T cell reactive oxygen signaling. (PNAS 2025)

- DOI: 10.1073/pnas.2417252121 | PMCID: PMC11725793 | PMID: 39752523
- Evidence: The flow through from the MACS column was enriched for CD4 + cells and was verified by flow cytometry for the enrichment of CD4 + cells ( SI Appendix , Fig.
- Full pipeline: read trimming [Cutadapt] -> quantification [HTSeq] -> differential/statistical testing [DESeq2, R] -> stage not stated [MACS2, pheatmap]

### Time evolution of a pumped molecular magnet-A time-resolved inelastic neutron scattering study. (PNAS 2025)

- DOI: 10.1073/pnas.2415300121 | PMCID: PMC11725827 | PMID: 39746040
- Evidence: The MACS instrument at the NIST Center for Neutron Research was used to obtain the spectrum, I ( Q a , Q b , ħ ω ) , in magnetic fields of (0, 1, 2, 3, 4.35) T for ħ ω ∈ [ 0.2 , 1.2 ] meV and momentum transfer, Q covering the plane perpendicular to ( 101 ) , which is spanned by the ( 1 , 0 , − ( c / a ) 2 ) = ( 1 , 0 , − 0.666 ) and ( 010 ) vectors in reciprocal space.
- Full pipeline: stage not stated [MACS2]

### Structure-guided design and synthesis of C22- and C32-modified FK520 analogs with enhanced activity against human pathogenic fungi. (PNAS 2025)

- DOI: 10.1073/pnas.2419883121 | PMCID: PMC11725869 | PMID: 39739817
- Evidence: Cells were resuspended in a MACS buffer and examined via flow cytometry with a BD FACSCantoII and FlowJo (BD Biosciences).
- Full pipeline: stage not stated [MACS2]

### Deletion of metal transporter Zip14 reduces major histocompatibility complex II expression in murine small intestinal epithelial cells. (PNAS 2025)

- DOI: 10.1073/pnas.2422321121 | PMCID: PMC11725848 | PMID: 39793074
- Evidence: The cells were stained with APC anti-mouse CD45 (Blood cells), FITC anti-mouse CD31 (Vascular cells), PE/Cyanine7 anti-mouse TER-119 (Lymphocytes), PE anti-mouse CD326 (EpCAM) (Epithelial cells), then resuspended in MACS buffer and used for FACS ( 53 ).
- Full pipeline: stage not stated [MACS2]

### Fasting primes small intestinal regeneration after damage via a microbiome-metabolite-chromatin axis. (PNAS 2026)

- DOI: 10.1073/pnas.2529215123 | PMCID: PMC13320697 | PMID: 42335240
- Version used: **2.2.9.1**
- Evidence: Peaks were called on pseudobulk replicates grouped by cluster using MACS2 (v2.2.9.1).
- Full pipeline: dimensionality reduction/clustering [MACS2 v2.2.9.1, UMAP] -> differential/statistical testing [QuPath] -> stage not stated [ArchR v1.0.2, GSEA, HOMER, R v1.0.2]

### Tuning reductase activity in monoterpene indole alkaloid biosynthesis. (PNAS 2026)

- DOI: 10.1073/pnas.2605425123 | PMCID: PMC13291617 | PMID: 42296364
- Evidence: Co-immunoprecipitation of GFP tagged (N-terminal) Cr GS1 and Cr SGD with the strictosidine aglycone branch point enzymes ( Cr SGD, Cr GS1, Cr FoGS1, and Cr HYS) were performed using a µMACS TM GFP isolation kit (Miltenyi Biotech) following the manufacturer’s instructions.
- Full pipeline: stage not stated [MACS2]

### Differential Wnt/β-catenin signaling via TCF7L2/LEF1 binding specificity shapes cellular and tumor phenotypes. (PNAS 2026)

- DOI: 10.1073/pnas.2528450123 | PMCID: PMC13273282 | PMID: 42268900
- Evidence: Peaks were called using MACS3 ( 51 ) and further processed using TF-IDF, FindTopFeatures, SVD, and LSI, with standard Signac functions.
- Full pipeline: alignment/mapping [Bowtie2] -> dimensionality reduction/clustering [UMAP] -> visualisation [deepTools] -> stage not stated [Enrichr, HOMER, MACS2, R v4.4, SAMtools, Seurat, Signac]

### Genome-wide CG hypomethylation of the &lt;i&gt;Arabidopsis&lt;/i&gt; ecotype Cvi linked to structural variation and RNAi at the &lt;i&gt;VIM4&lt;/i&gt;-&lt;i&gt;VIM2&lt;/i&gt; locus. (PNAS 2026)

- DOI: 10.1073/pnas.2603682123 | PMCID: PMC13213937 | PMID: 42154559
- Evidence: ATAC-Seq peaks defined by MACS are represented by boxes with labels on each track.
- Full pipeline: read trimming [Bowtie2 v2.4.2, Cutadapt v4.1] -> alignment/mapping [Bowtie2 v2.4.2] -> stage not stated [MACS2]

### Modular genetic architecture underlies human hand and foot evolution. (PNAS 2026)

- DOI: 10.1073/pnas.2603297123 | PMCID: PMC13187773 | PMID: 42118837
- Evidence: The bam files were used for peak calling via MACS software (version 2.1.1.2), using BAMPE and the following flags : --nolambda –bdg –verbose ( 57 ).
- Full pipeline: quality control [FastQC v0.11.9, R] -> alignment/mapping [Bowtie2 v2.3.4.1, featureCounts] -> quantification [RSEM] -> dimensionality reduction/clustering [WGCNA, clusterProfiler] -> stage not stated [BEDTools v2.27.1, DESeq2, MACS2, SAMtools, limma]

### Targeting CRTC2 reverses &lt;i&gt;STK11&lt;/i&gt; mutant NSCLC tumor resistance to immunotherapy. (PNAS 2026)

- DOI: 10.1073/pnas.2508762123 | PMCID: PMC13123801 | PMID: 42018410
- Evidence: Freshly isolated MC38 tumors were cut into pieces and homogenized to single cells by enzymatic treatment with the mouse tumor dissociation kit (Miltenyi) on a gentle MACS tissue dissociator system (Miltenyi) at 37 °C for 40 min.
- Full pipeline: read trimming [edgeR] -> normalisation [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [MACS2]

### STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing sarcoma aggressiveness. (PNAS 2026)

- DOI: 10.1073/pnas.2537425123 | PMCID: PMC13079922 | PMID: 41950086
- Evidence: Peak calling was performed using MACS2 using default settings ( 45 ).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA] -> normalisation [fgsea] -> differential/statistical testing [Bioconductor, fgsea, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [BEDTools, DESeq2, GSEA, MACS2]

### Neuron-derived mitochondrial DNA (mtDNA) activates microglia via the Z-DNA binding protein 1 (ZBP1)-mediated pathway in mild traumatic brain injury. (PNAS 2026)

- DOI: 10.1073/pnas.2527009123 | PMCID: PMC13056099 | PMID: 41926540
- Evidence: Primary microglia were isolated from the mouse cerebral cortex using MACS technology and cultured according to the manufacturer’s recommendations (Miltenyi Biotec).
- Full pipeline: stage not stated [ImageJ, MACS2]

### Histone modification clocks for robust cross-species biological age prediction and elucidating senescence regulation. (PNAS 2026)

- DOI: 10.1073/pnas.2533687123 | PMCID: PMC12993953 | PMID: 41805570
- Version used: **2.2.7.1**
- Evidence: Peaks were called using MACS2 v2.2.7.1 ( 55 ) with the “-C” flag for input background correction.
- Full pipeline: quality control [FastQC v0.11.9, Trim Galore] -> read trimming [FastQC v0.11.9, Trim Galore] -> alignment/mapping [Bowtie2 v2.4.5, SAMtools, deepTools v3.5.1] -> stage not stated [BEDTools v2.31.1, GSEA, MACS2 v2.2.7.1]

### Differential disease tolerance mediates sex-biased illness severity in sepsis. (PNAS 2026)

- DOI: 10.1073/pnas.2522764123 | PMCID: PMC12956862 | PMID: 41734079
- Evidence: After filtration through a 100 μm cell strainer, cell suspensions were centrifuged at 400 g for 5 min, and pellets were resuspended in MACS buffer (Miltenyi).
- Full pipeline: alignment/mapping [kallisto v0.46.1] -> differential/statistical testing [DESeq2 v1.48.1] -> stage not stated [GSEA, MACS2, R v4.5.0, fgsea v1.34.0]

### Foliar dewdroplet-induced redox cascades promote early flowering in &lt;i&gt;Brassicaceae&lt;/i&gt; plants. (PNAS 2026)

- DOI: 10.1073/pnas.2527021123 | PMCID: PMC12933091 | PMID: 41701847
- Evidence: Data were processed using FastQC, Bowtie2, MACS2, and DESeq2.
- Full pipeline: quality control [Bowtie2, DESeq2, FastQC, MACS2] -> stage not stated [WGCNA]

### EPOP and MTF2 activate PRC2 activity through DNA-sequence specificity. (PNAS 2026)

- DOI: 10.1073/pnas.2527303123 | PMCID: PMC12890814 | PMID: 41650228
- Evidence: Peaks were called using MACS3 with parameters: -g mm --keep-dup 1 --nomodel --extsize 300.
- Full pipeline: alignment/mapping [Bowtie2] -> quantification [BEDTools, deepTools] -> normalisation [BEDTools, deepTools] -> visualisation [BEDTools, deepTools] -> stage not stated [ImageJ, MACS2, SAMtools]

### Antagonistic regulation of nitrogen and drought signaling mediated by NIN-like protein 7 transcription factor in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2026)

- DOI: 10.1073/pnas.2509904122 | PMCID: PMC12773779 | PMID: 41481473
- Evidence: Enriched peaks were identified using MACS2 ( 76 ) (q = 0.05) by comparing ChIP samples against their respective Input DNA controls.
- Full pipeline: read trimming [Cutadapt, Trim Galore] -> alignment/mapping [Bowtie2] -> quantification [kallisto] -> normalisation [DESeq2] -> stage not stated [BEDTools, MACS2]

### Structure-guided multivalent nanobodies block SARS-CoV-2 infection and suppress mutational escape. (Science 2021)

- DOI: 10.1126/science.abe6230 | PMCID: PMC7932109 | PMID: 33436526
- Evidence: The DyLight 488 signal was measured in all ACE2-tagRFP-t positive cells using a MACS Quant VYB flow cytometer.
- Full pipeline: quality control [FastQC] -> alignment/mapping [Bowtie2, RELION v3.1, SAMtools] -> variant calling [GATK] -> quantification [ImageJ] -> structure determination [PHENIX, RELION v3.1] -> visualisation [ChimeraX] -> stage not stated [MACS2]

### PIM1 controls GBP1 activity to limit self-damage and to guard against pathogen infection. (Science 2023)

- DOI: 10.1126/science.adg2253 | PMCID: PMC7615196 | PMID: 37797010
- Evidence: For recruitment analysis, the cells were prepared as described above, but were seeded on black-wall, glass bottom 96-well imaging plates CG 1.0 (130-098-264, MACS Miltenyi).
- Full pipeline: alignment/mapping [MAFFT] -> quantification [ImageJ] -> normalisation [ImageJ] -> stage not stated [ChimeraX v0.93, MACS2, PHENIX, Topaz]

### Deploying synthetic coevolution and machine learning to engineer protein-protein interactions. (Science 2023)

- DOI: 10.1126/science.adh1720 | PMCID: PMC10403280 | PMID: 37499032
- Evidence: Antibody-stained cells were washed with MACS buffer (autoMACS ® Running Buffer, Miltenyi, cat. no.
- Full pipeline: dimensionality reduction/clustering [igraph] -> visualisation [scikit-learn v1.2.2] -> stage not stated [AlphaFold, MACS2, PyTorch, RoseTTAFold]

### Inborn errors of OAS-RNase L in SARS-CoV-2-related multisystem inflammatory syndrome in children. (Science 2023)

- DOI: 10.1126/science.abo3627 | PMCID: PMC10451000 | PMID: 36538032
- Evidence: MACS column separation was performed with selection beads for CD271-positive cells (Miltenyi Biotec) if the proportion of CD271-positive cells was <80%.
- Full pipeline: quality control [STAR] -> read trimming [edgeR] -> alignment/mapping [STAR, featureCounts v1.6.0] -> variant calling [BCFtools] -> quantification [featureCounts v1.6.0] -> normalisation [DESeq2, edgeR] -> dimensionality reduction/clustering [BCFtools, ComplexHeatmap, PLINK v1.9, UMAP] -> differential/statistical testing [ComplexHeatmap, edgeR] -> visualisation [ComplexHeatmap] -> stage not stated [CellChat, GSEA, MACS2, fgsea]

### Structural insights into the human NuA4/TIP60 acetyltransferase and chromatin remodeling complex. (Science 2024)

- DOI: 10.1126/science.adl5816 | PMCID: PMC11995519 | PMID: 39088653
- Version used: **2.2.7.1**
- Evidence: Reproducibility between biological replicates was assessed by performing Irreproducible Discovery Rate (IDR) analysis ( 114 ): we first ran MACS2 (v2.2.7.1) ( 115 ) peak calling algorithm with a liberal p-value cutoff (-p 1e-3).
- Full pipeline: quality control [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> alignment/mapping [Bowtie2 v2.4.5, FastQC v0.11.7, STAR] -> quantification [deepTools] -> normalisation [deepTools] -> registration [RELION v3.1] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [AlphaFold, BEDTools v2.30.0, ChimeraX, DESeq2, Galaxy, HTSeq v2.0.2, Matplotlib v3.7.2, NumPy v1.24.3, PLINK, SAMtools v1.15.1, SciPy v1.11.1, seaborn v0.12.2]

### Mef2d potentiates type-2 immune responses and allergic lung inflammation. (Science 2024)

- DOI: 10.1126/science.adl0370 | PMCID: PMC7616247 | PMID: 38935708
- Evidence: Human peripheral blood ILC2s were isolated from healthy volunteers and severe asthmatics using the MACS human ILC2 Isolation Kit (Miltenyi Biotec, #130-114-825) according to the manufacturer’s instructions.
- Full pipeline: read trimming [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> alignment/mapping [Bowtie2 v1.2.3, Cutadapt v1.4.1, DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> differential/statistical testing [DESeq2 v1.18.1, STAR v2.6.0a, Trim Galore v0.50] -> stage not stated [BEDTools, HOMER, MACS2]

### The immunopathological landscape of human pre-TCRα deficiency: From rare to common variants. (Science 2024)

- DOI: 10.1126/science.adh4059 | PMCID: PMC10958617 | PMID: 38422122
- Evidence: Transduced cells were sorted with a magnetic MACS ® Column and the CD271 MicroBead Kit (#130-099-023, Miltenyi Biotec), as recommended by the manufacturer.
- Full pipeline: alignment/mapping [HISAT2 v2.2.1, SAMtools v1.14] -> differential/statistical testing [R, tidyverse] -> visualisation [R, tidyverse] -> stage not stated [MACS2, Seurat v4.0.4, kallisto v0.46.1]

### Functional maps of a genomic locus reveal confinement of an enhancer by its target gene. (Science 2025)

- DOI: 10.1126/science.ads6552 | PMCID: PMC7618358 | PMID: 40966339
- Evidence: After 30 hours, transfected cells were enriched using MACS MS columns (130-042-201, Miltenyi Biotec) and LNGFR MicroBeads (130-091-330, Miltenyi Biotec) according to the manufacturer’s protocol.
- Full pipeline: alignment/mapping [BWA] -> quantification [deepTools v3.0] -> normalisation [deepTools v3.0] -> visualisation [Signac] -> stage not stated [BCFtools v1.9, MACS2, SnpEff v4.3p]

### Divergent FOXA1 mutations drive prostate tumorigenesis and therapy-resistant cellular plasticity. (Science 2025)

- DOI: 10.1126/science.adv2367 | PMCID: PMC12326538 | PMID: 40570057
- Evidence: Peak calling was performed using MACS2, filtered using bedtools, and converted to bigwigs with UCSC wigtoBigwig( 60 , 61 ).
- Full pipeline: quality control [Seurat v4.1, SoupX] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Trimmomatic v0.39, kallisto v0.46.1] -> quantification [Seurat v4.1, Slingshot, SoupX, edgeR] -> normalisation [edgeR] -> dimensionality reduction/clustering [GSVA, UMAP, clusterProfiler v4.10.1] -> differential/statistical testing [limma] -> visualisation [ComplexHeatmap, GSEA, R, fgsea, ggplot2, ggpubr v0.6.0] -> stage not stated [BEDTools, Enrichr, HOMER, ImageJ, MACS2, Picard, SAMtools, Signac v1.5.0, scDblFinder]

### Identification of antigen-presenting cell-T cell interactions driving immune responses to food. (Science 2025)

- DOI: 10.1126/science.ado5088 | PMCID: PMC12017586 | PMID: 39700315
- Evidence: Adoptive T cell transfer. naïve CD4 + T cells from spleen and lymph nodes were isolated by negative selection using biotinylated antibodies against CD8α, CD25, CD11c, CD11b, TER-119, NK1.1, and B220 and anti-biotin MACS beads (Miltenyi Biotec).
- Full pipeline: alignment/mapping [RSEM v1.3.1, STAR] -> stage not stated [DESeq2, MACS2, R, Seurat v4.1.2]

### Rewiring STAT signaling from the cell surface with Trikine immunotherapeutics. (Science 2026)

- DOI: 10.1126/science.adx9954 | PMCID: PMC12963926 | PMID: 41712697
- Evidence: Briefly, CD8+ T cells were isolated from human PBMCs via MACS (Miltenyi).
- Full pipeline: quality control [FastQC] -> alignment/mapping [AlphaFold, ChimeraX, featureCounts] -> quantification [ComplexHeatmap, Seurat v5.1.0, featureCounts] -> normalisation [ComplexHeatmap, UMAP] -> dimensionality reduction/clustering [Monocle v1.3.7, UMAP] -> differential/statistical testing [DESeq2] -> stage not stated [GSEA, MACS2, fgsea]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: Peaks were called for each replicate with MACS3 ( 80 ) using as input the TAG files with the parameters -f BED –nomodel –shift -75 –extsize 150 -g 2652783500 (mouse genome length in base pairs).
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### Mechanisms linking cytoplasmic decay of translation-defective mRNA to transcriptional adaptation. (Science 2026)

- DOI: 10.1126/science.aea1272 | PMCID: PMC13286266 | PMID: 41678638
- Evidence: Biotinylated RNA was isolated using the μMACS Streptavidin Kit (Miltenyi Biotec) and subsequently used for reverse transcription and qPCR analysis.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [Python, STAR v2.5.3a, featureCounts] -> quantification [Python] -> normalisation [DESeq2 v1.38.3, UMAP] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v1.38.3] -> stage not stated [BLAST, MACS2, NumPy, R, Scanpy, SciPy, lme4, scikit-learn, seaborn]

### Structural ontogeny of protein-protein interactions. (Science 2026)

- DOI: 10.1126/science.adx6931 | PMCID: PMC12904254 | PMID: 41678610
- Evidence: After staining, the cells were washed thoroughly with MACS buffer (autoMACS ® Running Buffer, Miltenyi, cat. no.
- Full pipeline: structure determination [Coot, PHENIX] -> stage not stated [CCP4, MACS2, SciPy, igraph]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Evidence: ...pended in 2 ml EBSS (Worthington) supplemented with 0.5 mg/ml DNase (Sigma-Aldrich) and 5 g/l glucose (Thermo Fisher Scientific), strained using 70□m MACS SmartStrainers (Miltenyi Biotec), and subjected to two-step discontinuous density gradient centrifugation (2000 g 12 min with lowered acceleration/deceleration ramps) in 35% / 60% Percoll (5 ml + 5 ml; Sigma-Aldrich) acidified to pH 7.4 with HCl...
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

