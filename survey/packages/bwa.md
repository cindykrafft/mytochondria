# BWA

- **Category:** genomics
- **Papers in survey:** 418
- **Journals:** Nature (195), PNAS (181), Cell (31), Science (10), NEJM (1)
- **Years:** 2021 (45), 2022 (82), 2023 (71), 2024 (68), 2025 (103), 2026 (49)
- **Versions named:** 0.7.17 (98), 0.7.15 (21), 0.7.12 (19), 0.7.10 (5), 0.7.18 (4), 0.5.10 (4), 0.7.16 (4), 0.7 (3), 0.6.1 (3), 0.7.13 (2)
- **Pipeline stages it appears in:** alignment/mapping (378), read trimming (80), variant calling (20), quality control (10), registration (4), quantification (4), structure determination (2), visualisation (1), normalisation (1), simulation/modelling (1), dimensionality reduction/clustering (1)

## Papers

### Differential pre-malignant programs and microenvironment chart distinct paths to malignancy in human colorectal polyps. (Cell 2021)

- DOI: 10.1016/j.cell.2021.11.031 | PMCID: PMC8941949 | PMID: 34910928
- Evidence: WES reads were aligned to the human reference genome hg19 using BWA ( Li and Durbin, 2009 ), sorted and indexed by Sambamba ( Tarasov et al., 2015 ).
- Full pipeline: read trimming [STAR] -> alignment/mapping [BWA, GATK, STAR] -> variant calling [GATK] -> quantification [STAR] -> normalisation [NumPy, UMAP, seaborn, velocyto] -> dimensionality reduction/clustering [Cytoscape, SCENIC, UMAP, scVelo v0.2.3] -> differential/statistical testing [GSEA, R] -> structure determination [GATK] -> machine learning [R] -> visualisation [Cytoscape, scVelo v0.2.3, seaborn] -> stage not stated [ANNOVAR, AnnData, Dask, Mutect2, Picard, Scanpy, emmeans]

### Emergence of an early SARS-CoV-2 epidemic in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.07.030 | PMCID: PMC8313480 | PMID: 34508652
- Evidence: Consensus sequences were assembled using an inhouse Snakemake ( Köster and Rahmann, 2012 ) pipeline with bwa-mem ( Li, 2013 ) and iVar v1.2.2 ( Grubaugh et al., 2019b ; Li, 2013 ).
- Full pipeline: stage not stated [BWA, Pangolin v2.0, R, Snakemake]

### The genomic history of the Aegean palatial civilizations. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.039 | PMCID: PMC8127963 | PMID: 33930288
- Evidence: Reads were aligned to the human reference genome (GRCh37 for the screening, WGS and nuclear capture data; and to the revised Cambridge Reference Sequence (rCRS, NC_012920.1 ) for the mtDNA capture data) using BWA ALN version 0.7.15 ( Li and Durbin, 2010 ) with disabled seeding (-l 1024) to reduce the effect of post-mortem damage-related error ( Schubert et al., 2012 ).
- Full pipeline: alignment/mapping [BWA, R] -> variant calling [GATK v3.7] -> stage not stated [ADMIXTURE, ANGSD v0.921, BCFtools v1.4, PLINK v1.9, Picard, SAMtools v1.10, Snakemake v5.3.0]

### Emergence and rapid transmission of SARS-CoV-2 B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.052 | PMCID: PMC8009040 | PMID: 33861950
- Evidence: ...ling for nanopore data https://github.com/artic-network/artic-ncov2019 Snakemake Köster and Rahmann, 2012 https://snakemake.readthedocs.io/en/stable/ bwa-mem Li, 2013 https://github.com/lh3/bwa iVar v1.2.2 Grubaugh et al., 2019b https://github.com/andersen-lab/ivar/releases/tag/v1.2.2 Transmissibility estimation Volz et al., 2021 N/A Conditional reference prior for overall clock rate Ferreira and ...
- Full pipeline: variant calling [Snakemake] -> stage not stated [BWA, Pangolin v2.0]

### Early introductions and transmission of SARS-CoV-2 variant B.1.1.7 in the United States. (Cell 2021)

- DOI: 10.1016/j.cell.2021.03.061 | PMCID: PMC8018830 | PMID: 33891875
- Evidence: ...Rambaut et al., 2016 TreeAnnotator https://beast.community/treeannotator Rambaut et al., 2018 BEAST v1.10 http://beast.community Suchard et al., 2018 BWA https://github.com/lh3/bwa Li and Durbin, 2010 MAFFT https://mafft.cbrc.jp/alignment/software/ Katoh and Standley, 2013 iVar 1.2.1 https://github.com/andersen-lab/ivar Grubaugh et al., 2019 Samtools http://samtools.sourceforge.net/ Li et al., 200...
- Full pipeline: alignment/mapping [BWA, MAFFT, SAMtools] -> normalisation [BEAST v1.10] -> differential/statistical testing [BEAST v1.10] -> structure determination [BEAST v1.10] -> stage not stated [Nextstrain, Pangolin, TreeTime v0.8.0, Trim Galore, ggplot2]

### Archaeogenomic distinctiveness of the Isthmo-Colombian area. (Cell 2021)

- DOI: 10.1016/j.cell.2021.02.040 | PMCID: PMC8024902 | PMID: 33761327
- Evidence: .../oxcal.html CutAdapt Martin, 2011 https://github.com/marcelm/cutadapt FastQC Andrews, 2010 https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ BWA Li and Durbin, 2010 http://bio-bwa.sourceforge.net/ Picard MarkDuplicates http://broadinstitute.github.io/picard http://broadinstitute.github.io/picard MapDamage2.0 Jónsson et al., 2013 https://ginolhac.github.io/mapDamage/ ANGSD Korneliussen et ...
- Full pipeline: quality control [BWA, Cutadapt, FastQC, Picard] -> stage not stated [ADMIXTURE, ANGSD, BCFtools, GATK, PLINK v2.0, SAMtools, VCFtools]

### Massive expansion of human gut bacteriophage diversity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.029 | PMCID: PMC7895897 | PMID: 33606979
- Version used: **0.7.16a**
- Evidence: ...pper v2.0 Huerta-Cepas et al., 2017 , 2019 https://github.com/eggnogdb/eggnog-mapper Prokka v1.5-135 Seemann, 2014 https://github.com/tseemann/prokka BWA-MEM v0.7.16a-r1181 Li and Durbin, 2009 https://github.com/lh3/bwa Kraken2 Wood et al., 2019 https://github.com/DerrickWood/kraken2 MAFFT v7.453 Katoh et al., 2002 https://mafft.cbrc.jp/alignment/software/ Easyfig v2.2.5 Sullivan et al., 2011 http...
- Full pipeline: alignment/mapping [BWA v0.7.16a, Kraken2, MAFFT v7.453, SAMtools v1.5] -> machine learning [SPAdes v3.10.0] -> stage not stated [BLAST v2.6.0, HMMER v3.1b, Keras v2.2.4, Prokka v1.5, Python, TensorFlow v1.10.0]

### Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading antibody-mediated immunity. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.037 | PMCID: PMC7843029 | PMID: 33621484
- Evidence: ... Nanopolish https://github.com/jts/nanopolish Version 0.11.3 trim_galore http://www.bioinformatics.babraham.ac.uk/projects/trim_galore/ Version 0.6.5 BWA Li, 2013 Version 0.7.5 iVar Grubaugh et al., 2019 Version 1.2.2 Minimap2 Li, 2018 Version 2.17 Baltic Python library https://github.com/evogytis/baltic N/A Artic sequencing bioinformatic pipeline Artic network https://artic.network/ncov-2019 N/A ...
- Full pipeline: differential/statistical testing [IQ-TREE, R] -> simulation/modelling [MDTraj, SciPy] -> stage not stated [BWA, ChimeraX, Conda, Jupyter, MDAnalysis, NumPy, OpenMM, Pangolin, PyMOL, brms, minimap2, tidyverse]

### Genome-wide data from medieval German Jews show that the Ashkenazi founder event pre-dated the 14<sup>th</sup> century. (Cell 2022)

- DOI: 10.1016/j.cell.2022.11.002 | PMCID: PMC9793425 | PMID: 36455558
- Version used: **0.7.15**
- Evidence: We mapped the sequences to the human genome reference sequence hg19 (GRCh37, https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.13/ ) and the inferred mitochondrial ancestral sequence RSRS ( Behar et al., 2012 ) using the samse command of BWA version 0.7.15 using parameters -n 0.01, -o 2, and -l 16500 ( Li and Durbin, 2009 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BCFtools, BWA v0.7.15] -> quantification [SAMtools] -> dimensionality reduction/clustering [ggplot2] -> differential/statistical testing [BEAST v2.6.6] -> visualisation [ggplot2] -> stage not stated [ADMIXTURE, R]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 subvariants, including BA.4 and BA.5. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.018 | PMCID: PMC9472642 | PMID: 36198317
- Version used: **0.7.17**
- Evidence: ...6V S This study N/A Plasmid: pC-BA.2 R493Q S This study N/A Software and algorithms fastp v0.21.0 Chen et al., 2018 https://github.com/OpenGene/fastp BWA-MEM v0.7.17 Li and Durbin, 2009 http://bio-bwa.sourceforge.net SAMtools v1.9 Li et al., 2009 http://www.htslib.org snpEff v5.0e Cingolani et al., 2012 http://pcingola.github.io/SnpEff roblanf/sarscov2phylo: 13-11-20 (GISAID phylogenetic analysis ...
- Full pipeline: stage not stated [BWA v0.7.17, ImageJ, PHENIX, PyMOL, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Repression and 3D-restructuring resolves regulatory conflicts in evolutionarily rearranged genomes. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.006 | PMCID: PMC9567273 | PMID: 36179666
- Version used: **0.7.12**
- Evidence: DamID-seq analysis Raw reads from DamID-seq experiments were mapped to the mouse mm10 reference genome using the alignment tool BWA-MEM (v.0.7.12) ( Li and Durbin, 2009 ).
- Full pipeline: read trimming [Cutadapt, deepTools] -> alignment/mapping [BWA v0.7.12, Cutadapt, deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2] -> simulation/modelling [LAMMPS] -> structure determination [ImageJ v1.52i] -> visualisation [UMAP] -> stage not stated [BEDTools, Bowtie2, GATK v4.1.4.1, MACS2 v2.0, SAMtools, SciPy]

### High-coverage whole-genome sequencing of the expanded 1000 Genomes Project cohort including 602 trios. (Cell 2022)

- DOI: 10.1016/j.cell.2022.08.004 | PMCID: PMC9439720 | PMID: 36055201
- Version used: **0.7.15**
- Evidence: (2021) http://samtools.github.io/bcftools/bcftools.html BWA-MEM v0.7.15 Li (2013) http://bio-bwa.sourceforge.net/ bedtools v2.26.0 Quinlan and Hall (2010) https://github.com/arq5x/bedtools2 CrossMap v0.5.3 Zhao et al.
- Full pipeline: quality control [FastQC v0.11.3] -> alignment/mapping [MAFFT] -> variant calling [MAFFT] -> dimensionality reduction/clustering [MAFFT] -> stage not stated [BCFtools v1.9, BEDTools v2.26.0, BWA v0.7.15, GATK, Picard v2.4.1, R v3.6, SAMtools, SHAPEIT, VCFtools v0.1.12, VEP, WhatsHap v0.18]

### The genomic origins of the world's first farmers. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.008 | PMCID: PMC9166250 | PMID: 35561686
- Evidence: ...., 2011 ) - ATLAS - version 1.0, commit 6bd2482 ( Link et al., 2017 ) - ATLAS-Pipeline , commit 6df90e7 ( bitbucket.org/wegmannlab/atlas-pipeline ) - BWA - Burrows-Wheeler Alignment Tool - version 0.7.15 ( Li, 2013 ) - ContamMix - version 1.0 ( Fu et al., 2013 ) - fastqc - version 0.11.5 ( www.bioinformatics.babraham.ac.uk/projects/fastqc/ ) - GATK - version 3.7 ( DePristo et al., 2011 ) - mafft -...
- Full pipeline: quality control [BWA, GATK] -> alignment/mapping [BCFtools, BWA, R, SAMtools] -> variant calling [UMAP] -> dimensionality reduction/clustering [UMAP] -> stage not stated [ANGSD, ANNOVAR, BEDTools, Picard, Snakemake, Trim Galore]

### Virological characteristics of the SARS-CoV-2 Omicron BA.2 spike. (Cell 2022)

- DOI: 10.1016/j.cell.2022.04.035 | PMCID: PMC9057982 | PMID: 35568035
- Version used: **0.7.17**
- Evidence: ... et al., 2021 ) N/A Plasmid: pJYDC1 Addgene Cat# 162458 Software and algorithms fastp v0.21.0 ( Chen et al., 2018 ) https://github.com/OpenGene/fastp BWA-MEM v0.7.17 ( Li and Durbin, 2009 ) http://bio-bwa.sourceforge.net SAMtools v1.9 ( Li et al., 2009 ) http://www.htslib.org snpEff v5.0e ( Cingolani et al., 2012 ) http://pcingola.github.io/SnpEff roblanf/sarscov2phylo: 13-11-20 (GISAID phylogenet...
- Full pipeline: stage not stated [BEAST v2.6.6, BWA v0.7.17, ImageJ, R v4.1, RAxML v8.2.12, SAMtools v1.9, SnpEff, Stan v2.28.1, fastp v0.21.0, minimap2 v2.17]

### Ancient genomes reveal origin and rapid trans-Eurasian migration of 7<sup>th</sup> century Avar elites. (Cell 2022)

- DOI: 10.1016/j.cell.2022.03.007 | PMCID: PMC9042794 | PMID: 35366416
- Version used: **0.7.12**
- Evidence: ...tzer et al., 2016 https://eager.readthedocs.io/en/latest/ AdapterRemoval 2.2.0 Schubert et al., 2016 https://github.com/MikkelSchubert/adapterremoval BWA 0.7.12 Li and Durbin, 2009 http://bio-bwa.sourceforge.net/ DeDup 0.12.2 Peltzer et al., 2016 https://github.com/apeltzer/DeDup mapDamage 2.0.6 Jónsson et al., 2013 https://github.com/ginolhac/mapDamage bamUtil 1.0.13 https://github.com/statgen/ba...
- Full pipeline: read trimming [BWA v0.7.12] -> stage not stated [ANGSD v0.910, GATK v3.5, PLINK v1.9, R v4.0, SAMtools v1.3, SHAPEIT]

### Non-cell-autonomous disruption of nuclear architecture as a potential cause of COVID-19-induced anosmia. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.024 | PMCID: PMC8808699 | PMID: 35180380
- Version used: **0.7.17**
- Evidence: Human data were aligned against hg19 and hamster reads were aligned to MesAur1.0_HiC.fasta.gz using BWA 0.7.17 mem algorithm.
- Full pipeline: alignment/mapping [BWA v0.7.17, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [DESeq2, GSEA, ImageJ, R v4.0.5, SAMtools, Seurat, ggplot2, pheatmap]

### Parallel analysis of transcription, integration, and sequence of single HIV-1 proviruses. (Cell 2022)

- DOI: 10.1016/j.cell.2021.12.011 | PMCID: PMC8809251 | PMID: 35026153
- Evidence: ...cancer.gov/tools/pvs_annot.php MUSCLE Edgar, 2004 http://www.drive5.com/muscle/ Geneious Prime 2021.0.3 Biomatters https://www.geneious.com/download/ bwa-mem Li and Durbin, 2009 http://maq.sourceforge.net/ RepeatMasker Institute for Systems Biology http://www.repeatmasker.org/ RSEM (v1.2.22) Li and Dewey, 2011 http://deweylab.github.io/RSEM/ STAR aligner software (2.5.1b) ENCODE https://www.encode...
- Full pipeline: quality control [FastQC, R, SAMtools] -> read trimming [Trimmomatic] -> alignment/mapping [BWA, HOMER v4.10.3, RSEM v1.2.22, RepeatMasker, STAR] -> differential/statistical testing [FastQC, R, STAR] -> stage not stated [Bowtie2, MACS2 v2.1.1.20160309, Python, scikit-learn]

### SND1 binds SARS-CoV-2 negative-sense RNA and promotes viral RNA synthesis through NSP9. (Cell 2023)

- DOI: 10.1016/j.cell.2023.09.002 | PMCID: PMC10617981 | PMID: 37794589
- Evidence: 81 https://imagej.nih.gov/ij/ R The Comprehensive R Archive Network https://cran.r-project.org/ Python Python Programming Language https://www.python.org/ BWA Li and Durbin 82 http://bio-bwa.sourceforge.net/bwa.shtml Picard Tools Broad Institute https://broadinstitute.github.io/picard Samtools Li et al.
- Full pipeline: quality control [Bowtie2 v2.3.0] -> read trimming [Cutadapt v1.18, STAR v2.7.10a, Trimmomatic] -> alignment/mapping [Bowtie2 v2.3.0, IMOD, STAR v2.7.10a, featureCounts] -> normalisation [DESeq2, limma] -> differential/statistical testing [BEDTools, DESeq2] -> structure determination [IMOD] -> stage not stated [BWA, ImageJ, MACS2, NumPy, Picard, SAMtools]

### Stepwise emergence of the neuronal gene expression program in early animal evolution. (Cell 2023)

- DOI: 10.1016/j.cell.2023.08.027 | PMCID: PMC10580291 | PMID: 37729907
- Version used: **0.7.17**
- Evidence: 88 https://github.com/macs3-project/MACS CellRanger 6.1.1 v6.1.1 10X Genomics https://support.10xgenomics.com/cloud-analysis/release-notes BWA 0.7.17 Li and Durbin 89 https://github.com/lh3/bwa Possvm Grau-Bové and Sebé-Pedrós 90 https://github.com/xgrau/possvm-orthology/ deeptools 3.5.1 Ramírez et al.
- Full pipeline: alignment/mapping [BLAST, HMMER v3.3.2, MAFFT v7.475, SAMtools v1.11, kallisto v0.46.2] -> normalisation [UMAP] -> dimensionality reduction/clustering [BLAST, UMAP] -> differential/statistical testing [Seurat v4.1.1] -> visualisation [ChimeraX v1.6.1, ComplexHeatmap v2.10.0, R, igraph] -> stage not stated [AlphaFold, BWA v0.7.17, ColabFold, HOMER v4.11, IQ-TREE v2.1, ImageJ v1.52, MACS2 v2.2.7.1, STAR v2.7.9a, WGCNA v1.71, deepTools v3.5.1]

### DNA hypomethylation silences anti-tumor immune genes in early prostate cancer and CTCs. (Cell 2023)

- DOI: 10.1016/j.cell.2023.05.028 | PMCID: PMC10436379 | PMID: 37327786
- Evidence: MNase ChIP-seq and Cut and Run data analysis ChIP-seq and Cut and Run reads were first trimmed by Trim Galore (v0.4.3) ( https://github.com/FelixKrueger/TrimGalore ) and then mapped to the human or mouse genome using BWA men 74 .
- Full pipeline: read trimming [BWA, Bismark, Trim Galore v0.4.3] -> alignment/mapping [BWA, Bismark, TopHat] -> quantification [ImageJ, SAMtools v1.3.1] -> differential/statistical testing [R v3.1.2] -> stage not stated [Bioconductor, GSEA, MACS2 v2.0.10, deepTools]

### Molecular mechanisms of stress-induced reactivation in mumps virus condensates. (Cell 2023)

- DOI: 10.1016/j.cell.2023.03.015 | PMCID: PMC10156176 | PMID: 37116470
- Version used: **0.7.17**
- Evidence: 92 https://iupred2a.elte.hu/ PSIPRED Jones 93 http://bioinf.cs.ucl.ac.uk/psipred/ BWA-MEM 0.7.17-r1188 N/A https://github.com/lh3/bwa Picard tool 2.9.0 Broad Institute of MIT and Harvard https://broadinstitute.github.io/picard FreeBayes 1.1.0-3 N/A https://github.com/freebayes/freebayes isobarQuant Franken et al.
- Full pipeline: dimensionality reduction/clustering [Bioconductor, clusterProfiler] -> differential/statistical testing [Bioconductor] -> structure determination [Coot, UCSF Chimera] -> visualisation [UCSF Chimera] -> stage not stated [AlphaFold, BWA v0.7.17, ChimeraX v1.1.1, IMOD, PHENIX v1.18, Picard, R v3.6, RELION v3.0, freebayes v1.1.0, limma]

### Bat pluripotent stem cells reveal unusual entanglement between host and viruses. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.011 | PMCID: PMC10085545 | PMID: 36812912
- Evidence: 42 bp paired-end sequencing reads (PE42) were generated by Illumina sequencing (using NextSeq 500) to a depth of at least 83 million total reads and mapped to the GCA_004115265.2 genome (Ensembl, annotation version 102) using the BWA algorithm with default settings (“bwa mem”).
- Full pipeline: quality control [Cutadapt, FastQC v0.11.9, MultiQC v1.9] -> read trimming [Cutadapt, Trimmomatic v0.39] -> alignment/mapping [BWA, Cutadapt, HISAT2 v2.2.1, SAMtools v1.10, featureCounts v2.0.1] -> quantification [Cutadapt] -> differential/statistical testing [DESeq2 v1.10.1, ggplot2] -> visualisation [FastQC v0.11.9, MultiQC v1.9, deepTools, ggplot2] -> stage not stated [Cytoscape, Enrichr, Kraken2 v2.1.2, MACS2, R, ggpubr]

### A bat MERS-like coronavirus circulates in pangolins and utilizes human DPP4 and host proteases for cell entry. (Cell 2023)

- DOI: 10.1016/j.cell.2023.01.019 | PMCID: PMC9933427 | PMID: 36803605
- Version used: **0.7.12**
- Evidence: 43 https://bitbucket.org/genomicepidemiology/mgmapper/src/master/ BWA (v0.7.12-r1039) Li et al.
- Full pipeline: stage not stated [BWA v0.7.12, Cutadapt v1.18, IQ-TREE v1.6.1, ImageJ, Pangolin]

### A potent pan-sarbecovirus neutralizing antibody resilient to epitope diversification. (Cell 2024)

- DOI: 10.1016/j.cell.2024.09.026 | PMCID: PMC11645210 | PMID: 39383863
- Version used: **0.7.17**
- Evidence: Variants were called against the consensus of the respective sample using an in-house pipeline that leverages trimmomatic v.0.39, 123 bwa-mem v.0.7.17, 124 lofreq v.2.1.5, 125 and bcftools v.1.10.2.
- Full pipeline: read trimming [BCFtools v1.10.2, BWA v0.7.17] -> differential/statistical testing [RELION, scikit-learn] -> structure determination [Coot, PHENIX, Topaz] -> machine learning [Topaz, scikit-learn] -> visualisation [ChimeraX] -> stage not stated [OpenMM, Pangolin, Python v3.10]

### Vaginal Lactobacillus fatty acid response mechanisms reveal a metabolite-targeted strategy for bacterial vaginosis treatment. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.029 | PMCID: PMC11429459 | PMID: 39163861
- Evidence: For each sample, reads were aligned to the sample species reference genome (GCF_022455535.1 / ASM2245553v1 for L. crispatus ; GCF_022456925.1 / ASM2245692v1 for L. gasseri ; GCF_022456915.1 / ASM2245691v1 for L. jensenii ) using BWA 95 and read counts were assigned to genes and other genomic features using custom scripts.
- Full pipeline: alignment/mapping [BWA, RAxML] -> quantification [BWA] -> machine learning [mothur] -> stage not stated [DESeq2, Jupyter, MUSCLE v5.1, Matplotlib v3.7.1, NumPy v1.22.3, Python, QIIME 2, SciPy v1.9.3, eggNOG v5.0, ggpubr v0.4.0, phyloseq, seaborn v0.11.2, statsmodels v0.13.2, tidyverse v1.3.1]

### Mining human microbiomes reveals an untapped source of peptide antibiotics. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.027 | PMCID: PMC12821620 | PMID: 39163860
- Evidence: Reads were trimmed of adapters and low quality bases with Trim Galore ( github.com/FelixKrueger/TrimGalore ) and aligned to the P. copri DSM 18205 reference genome (GCF_020735445.1) with the Burrows Wheeler Aligner (default bwa-mem).
- Full pipeline: read trimming [BWA, Trim Galore] -> alignment/mapping [BLAST, BWA, SPAdes, Trim Galore] -> quantification [featureCounts] -> normalisation [featureCounts] -> dimensionality reduction/clustering [UMAP] -> stage not stated [AlphaFold, ColabFold]

### Macrophage-mediated myelin recycling fuels brain cancer malignancy. (Cell 2024)

- DOI: 10.1016/j.cell.2024.07.030 | PMCID: PMC11429458 | PMID: 39137777
- Version used: **0.7.17**
- Evidence: The recorded ATAC-seq data were mapped to the mm10 reference genome with BWA-MEM (version 0.7.17-r1188).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.10] -> quantification [ggplot2] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2 v3.14, GSEA, ggplot2, survival (R)] -> stage not stated [Cellpose, R v4.1.1, Seurat v4.4, edgeR, ggpubr v0.4.0]

### Vertebrate centromeres in mitosis are functionally bipartite structures stabilized by cohesin. (Cell 2024)

- DOI: 10.1016/j.cell.2024.04.014 | PMCID: PMC11164432 | PMID: 38744280
- Version used: **0.7.16**
- Evidence: 79 http://www.usadellab.org/cms/index.php?page=trimmomatic BWA mem v0.7.16 Heng Li https://github.com/lh3/bwa?tab=readme-ov-file deepTools bamCoverage v3.5 deepTools https://deeptools.readthedocs.io/en/develop/ LAMMPS Plimpton 80 https://github.com/lammps/lammps Huygens Professional (v20.10) Scientific Volume Imaging https://svi.nl/Huygens-Professional capC-MAP software Buckle 81 https://github.co...
- Full pipeline: read trimming [BWA v0.7.16, Cutadapt v1.18, ImageJ, LAMMPS, Trimmomatic v0.36, deepTools] -> stage not stated [Snakemake]

### Selection of epigenetically privileged HIV-1 proviruses during treatment with panobinostat and interferon-α2a. (Cell 2024)

- DOI: 10.1016/j.cell.2024.01.037 | PMCID: PMC10903630 | PMID: 38367616
- Evidence: ...tMasker Institute for Systems Biology http://www.repeatmasker.org/ FastQC (v0.11.9) Babraham Bioinformatics https://www.bioinformatics.babraham.ac.uk bwa-mem Li and Durbin 93 http://maq.sourceforge.net/ Ensembl (V109) Ensembl www.ensembl.org UCSC Genome Browser UCSC www.genome.ucsc.edu GENCODE (V43) GENCODE www.gencodegenes.org RSEM (v1.2.22) Li and Dewey 94 http://deweylab.github.io/RSEM/ STAR al...
- Full pipeline: quality control [BWA, FastQC v0.11.9, R, RepeatMasker] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [Bowtie2, RSEM v1.2.22, STAR, Trimmomatic] -> differential/statistical testing [FastQC v0.11.9, R, RepeatMasker] -> stage not stated [DESeq2, MACS2, Python]

### Genomes of critically endangered saola are shaped by population structure and purging. (Cell 2025)

- DOI: 10.1016/j.cell.2025.03.040 | PMCID: PMC12173715 | PMID: 40328258
- Version used: **0.7.17**
- Evidence: 97 https://github.com/MikkelSchubert/adapterremoval BWA v0.7.17 Li and Durbin 98 https://github.com/lh3/bwa Picard tools v2.24 Broad Institute https://broadinstitute.github.io/picard/ Samtools v1.11.0 Li et al.
- Full pipeline: read trimming [BWA v0.7.17, Picard, SAMtools v1.11.0] -> alignment/mapping [MAFFT v7.407] -> stage not stated [ANGSD v0.933, BCFtools, BEDTools v2.29.2, BUSCO v3.0.1, GATK v4.1.7, PLINK v1.9, RepeatMasker v4.0.5, SnpEff]

### An anaerobic pathogen rewires host metabolism to fuel oxidative growth in the inflamed gut. (Cell 2026)

- DOI: 10.1016/j.cell.2026.04.012 | PMCID: PMC13185528 | PMID: 42066751
- Evidence: B. fragilis -derived reads were aligned to a the GCF 023702735.1 ASM2370273v1 reference sequence using BWA 187 and read counts were assigned to RefSeq annotated genes and other genomic features using custom scripts ( https://github.com/broadinstitute/BactRNASeqCount ).
- Full pipeline: alignment/mapping [BWA, featureCounts] -> quantification [BWA, ImageJ, featureCounts] -> differential/statistical testing [edgeR, featureCounts] -> stage not stated [Bowtie2, DESeq2, OrthoFinder, QIIME 2, WGCNA]

### Vaccine Breakthrough Infections with SARS-CoV-2 Variants. (NEJM 2021)

- DOI: 10.1056/nejmoa2105000 | PMCID: PMC8117968 | PMID: 33882219
- Evidence: Detected mutations were confirmed by aligning RNA sequencing reads on the reference genome sequence of SARS-CoV-2 (GenBank number, NC_045512 ) with the Burrows–Wheeler Aligner (BWA-MEM).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [Nextstrain]

### Triangulation supports agricultural spread of the Transeurasian languages. (Nature 2021)

- DOI: 10.1038/s41586-021-04108-8 | PMCID: PMC8612925 | PMID: 34759322
- Version used: **0.7.12**
- Evidence: We mapped the merged reads with a minimum of 30 bp to the human reference genome (hs37d5; GRCh37 with decoy sequences) using BWA v.0.7.12 71 .
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [BWA v0.7.12, SAMtools v1.3] -> simulation/modelling [BEAST v2.6]

### A chickpea genetic variation map based on the sequencing of 3,366 genomes. (Nature 2021)

- DOI: 10.1038/s41586-021-04066-1 | PMCID: PMC8612933 | PMID: 34759320
- Evidence: We aligned sequencing data from the 3,366 chickpea accessions to the reference genome of CDC Frontier 11 , using BWA-MEM 31 v.0.7.15.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ADMIXTURE, BUSCO, PLINK, RAxML, VCFtools]

### Terrestrial-type nitrogen-fixing symbiosis between seagrass and a marine bacterium. (Nature 2021)

- DOI: 10.1038/s41586-021-04063-4 | PMCID: PMC8636270 | PMID: 34732889
- Evidence: C. neptuna metagenome-assembled genome (MAG), the 2 × 250 bp reads of the Illumina metagenome were mapped onto the metaFlye assembly with the BWA-MEM short read aligner 67 using the default settings.
- Full pipeline: quality control [Prokka] -> read trimming [Cutadapt, Trimmomatic v0.32] -> alignment/mapping [BWA, SAMtools v1.10] -> quantification [featureCounts v1.4.6, phyloseq] -> machine learning [scikit-learn] -> visualisation [phyloseq] -> stage not stated [Bowtie2 v2.1.0, HMMER, Pilon v1.23, QIIME 2, minimap2]

### The genomic origins of the Bronze Age Tarim Basin mummies. (Nature 2021)

- DOI: 10.1038/s41586-021-04052-7 | PMCID: PMC8580821 | PMID: 34707286
- Version used: **0.7.12**
- Evidence: Merged reads were mapped to the human reference genome (hs37d5; GRCh37 with decoy sequences) using the aln/samse programs in BWA v.0.7.12 (ref.
- Full pipeline: quality control [ANGSD v0.910] -> alignment/mapping [BWA v0.7.12] -> variant calling [BCFtools v1.7] -> stage not stated [ADMIXTURE v1.3.0, PLINK v1.90]

### eccDNAs are apoptotic products with high innate immunostimulatory activity. (Nature 2021)

- DOI: 10.1038/s41586-021-04009-w | PMCID: PMC9295135 | PMID: 34671165
- Evidence: BWA 49 MEM (version 0.7.17) with default parameters.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [RSEM, minimap2] -> quantification [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, BWA, Bioconductor, Picard v2.23.4, deepTools]

### Exome sequencing and analysis of 454,787 UK Biobank participants. (Nature 2021)

- DOI: 10.1038/s41586-021-04103-z | PMCID: PMC8596853 | PMID: 34662886
- Evidence: In brief, for each sample, NovaSeq WES reads are mapped with BWA MEM to the hg38 reference genome.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [LDSC, REGENIE] -> stage not stated [GCTA v1.91.7, SnpEff]

### Transposon-associated TnpB is a programmable RNA-guided DNA endonuclease. (Nature 2021)

- DOI: 10.1038/s41586-021-04058-1 | PMCID: PMC8612924 | PMID: 34619744
- Evidence: The remaining reads were mapped to the transposon-encoding plasmid (pTWIST-ISDra2; Supplementary Table 1 ) using BWA 35 and converted to the BAM file format with SAMtools 36 .
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [AlphaFold, Cutadapt, Python]

### Genome of a middle Holocene hunter-gatherer from Wallacea. (Nature 2021)

- DOI: 10.1038/s41586-021-03823-6 | PMCID: PMC8387238 | PMID: 34433944
- Evidence: After AdapterRemoval as implemented in EAGER v.1.92.56 58 , the mtDNA-enriched reads were aligned to the mitochondrial reference genome (rCRS) and the reads from the genome-wide captures to the human reference genome (hg19) using a mapping quality filter of 30 for the circularmapper v.1.93.5 and BWA 59 aligner, respectively.
- Full pipeline: read trimming [BWA, SAMtools v1.3] -> alignment/mapping [BWA] -> variant calling [SAMtools v1.3] -> differential/statistical testing [ggplot2 v3.3.3] -> visualisation [ggplot2 v3.3.3] -> stage not stated [PLINK v1.9, QGIS]

### Towards complete and error-free genome assemblies of all vertebrate species. (Nature 2021)

- DOI: 10.1038/s41586-021-03451-0 | PMCID: PMC8081667 | PMID: 33911273
- Evidence: In brief, both ends of a read pair were mapped independently using BWA-MEM 89 with the parameter -B8, and filtered when mapping quality was <10.
- Full pipeline: alignment/mapping [BUSCO, BWA] -> stage not stated [BCFtools, Canu, Pilon, RepeatMasker, freebayes, minimap2]

### Evolutionary and biomedical insights from a marmoset diploid genome assembly. (Nature 2021)

- DOI: 10.1038/s41586-021-03535-x | PMCID: PMC8189906 | PMID: 33910227
- Evidence: Identification of sex-linked sequences and additional Y-chromosome assembly To identify X-linked and Y-linked sequences in mCalJac1 (GCA_011100555.1), we mapped parental short reads to the assembly with BWA ALN (v.0.7.12) 69 .
- Full pipeline: alignment/mapping [BCFtools, BWA, GATK, freebayes v1.3.1, minimap2] -> variant calling [GATK, freebayes v1.3.1]

### Million-year-old DNA sheds light on the genomic history of mammoths. (Nature 2021)

- DOI: 10.1038/s41586-021-03224-9 | PMCID: PMC7116897 | PMID: 33597750
- Evidence: The merged reads were mapped to a composite reference, consisting of the African savannah elephant nuclear genome (LoxAfr4), woolly mammoth mitogenome ( DQ188829 ), and the human genome (hg19) using BWA aln v0.7.8 with deactivated seeding (-l 16,500), allowing for more substitutions (-n 0.01) and up to two gaps (-o 2) 30 , 31 .
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.921, BCFtools, Picard, RepeatMasker v4.0.7, SAMtools v1.10]

### Sequencing of 53,831 diverse genomes from the NHLBI TOPMed Program. (Nature 2021)

- DOI: 10.1038/s41586-021-03205-y | PMCID: PMC7875770 | PMID: 33568819
- Evidence: All sequences were remapped using BWA-MEM 76 to the hs38DH 1000 Genomes build 38 human genome reference including decoy sequences, following the protocol published previously 77 .
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> stage not stated [BWA, Docker, GATK v3.5.0, R, SAMtools, VEP]

### Regulatory genomic circuitry of human disease loci by integrative epigenomics. (Nature 2021)

- DOI: 10.1038/s41586-020-03145-z | PMCID: PMC7875769 | PMID: 33536621
- Evidence: Uniform data processing We downloaded one alignment file per replicate, prioritizing filtered alignments aligned with BWA in hg19 whenever possible.
- Full pipeline: alignment/mapping [BWA] -> dimensionality reduction/clustering [R, UMAP] -> differential/statistical testing [MACS2] -> machine learning [XGBoost] -> visualisation [R]

### Genomic mechanisms of climate adaptation in polyploid bioenergy switchgrass. (Nature 2021)

- DOI: 10.1038/s41586-020-03127-1 | PMCID: PMC7886653 | PMID: 33505029
- Evidence: To account for different library sizes, reads were pruned to ≤50× coverage, then mapped to the v5 assembly using bwa-mem 55 .
- Full pipeline: alignment/mapping [BWA, GATK, HTSeq v0.11.2] -> variant calling [GATK, SAMtools] -> registration [Picard] -> dimensionality reduction/clustering [WGCNA] -> differential/statistical testing [DESeq2, lme4] -> stage not stated [BCFtools, BUSCO, ImageJ, PLINK, R, RepeatMasker, SnpEff, VCFtools]

### Platypus and echidna genomes reveal mammalian biology and evolution. (Nature 2021)

- DOI: 10.1038/s41586-020-03039-0 | PMCID: PMC8081666 | PMID: 33408411
- Evidence: Sex-borne sequence identification Female and male reads were mapped to the genome using BWA ALN 45 (v.0.7.12).
- Full pipeline: alignment/mapping [BWA, HISAT2, minimap2 v2.13] -> quantification [ggplot2 v3.2.1] -> normalisation [ggplot2 v3.2.1] -> stage not stated [ImageJ v2.0.0, RepeatMasker v4.0.6]

### A genetic history of the pre-contact Caribbean. (Nature 2021)

- DOI: 10.1038/s41586-020-03053-2 | PMCID: PMC7864882 | PMID: 33361817
- Version used: **0.7.15**
- Evidence: Merged sequences were mapped to the reconstructed human mtDNA consensus sequence (RSRS) 51 and the human reference genome version hg19 using the samse command in BWA v.0.7.15-r1140 52 with the parameters -n 0.01, -o 2, and -l 16500.
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard] -> structure determination [BWA v0.7.15] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.3.1, SAMtools]

### Chromothripsis drives the evolution of gene amplification in cancer. (Nature 2021)

- DOI: 10.1038/s41586-020-03064-z | PMCID: PMC7933129 | PMID: 33361815
- Evidence: Hi-C data processing was performed as follows: Paired-end HiC sequencing reads were mapped using BWA-MEM to the reference genome (hg19) in single-end mode with default parameter setting for each of the two ends separately.
- Full pipeline: quality control [FastQC, TopHat] -> alignment/mapping [BWA, Bioconductor, Cufflinks, FastQC, TopHat] -> quantification [Bioconductor, Cufflinks] -> differential/statistical testing [Bioconductor, Cufflinks] -> simulation/modelling [Python v2.7] -> stage not stated [Fiji, ImageJ, SAMtools]

### Ovarian cancer mutational processes drive site-specific immune evasion. (Nature 2022)

- DOI: 10.1038/s41586-022-05496-1 | PMCID: PMC9771812 | PMID: 36517593
- Evidence: Bulk WGS Alignment Sequencing reads were aligned to human genome reference GRCh37 (hg19) using the Burrows–Wheeler aligner (BWA-MEM) v0.7.17-r1188 ( https://sourceforge.net/projects/bio-bwa/ ).
- Full pipeline: quality control [R, Seurat] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [UMAP] -> machine learning [QuPath v0.2.3, StarDist] -> stage not stated [Strelka v2.8.2, scDblFinder v0.2.1]

### A 2-million-year-old ecosystem in Greenland uncovered by environmental DNA. (Nature 2022)

- DOI: 10.1038/s41586-022-05453-y | PMCID: PMC9729109 | PMID: 36477129
- Evidence: We mapped these read sets against the consensus Betula chloroplast genome using BWA 89 with ancient DNA parameters (-o 2 -n 0.001 -t 20), then removed unmapped reads, quality filtered for read quality ≥25, and sorted the resulting bam files using samtools 89 .
- Full pipeline: alignment/mapping [BWA, Bowtie2, MAFFT, Picard, Python, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [BCFtools, Kraken2]

### The co-evolution of the genome and epigenome in colorectal cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05202-1 | PMCID: PMC9684080 | PMID: 36289335
- Evidence: The trimmed and filtered reads from each sequencing run and library were separately aligned to the GRCh38 reference assembly of the human genome 63 using the BWA-MEM algorithm v0.7.17 (ref.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, FastQC] -> alignment/mapping [BEDTools, BWA, Bowtie2 v2.3.4.3, FastQC] -> quantification [HTSeq] -> stage not stated [DESeq2, GATK, MACS2 v2.21, Mutect2 v4.1.4.1, Picard v2.5.0, R, SAMtools v1.9, STRING db, VEP v93.2, edgeR v3.30.3]

### Single-cell genomic variation induced by mutational processes in cancer. (Nature 2022)

- DOI: 10.1038/s41586-022-05249-0 | PMCID: PMC9712114 | PMID: 36289342
- Evidence: Sequenced reads were aligned to the human reference GRCh37 (hg19) using BWA-MEM.
- Full pipeline: alignment/mapping [BWA, DeepVariant, R, WhatsHap, minimap2] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [Seurat, Strelka, scDblFinder]

### Semi-automated assembly of high-quality diploid human reference genomes. (Nature 2022)

- DOI: 10.1038/s41586-022-05325-5 | PMCID: PMC9668749 | PMID: 36261518
- Version used: **0.7.15**
- Evidence: Strand-seq analyses To evaluate structural accuracy of each assembly, we first aligned Strand-seq data from HG002 to each assembly using BWA-MEM (version 0.7.15-r1140) 75 with the default parameters.
- Full pipeline: alignment/mapping [BWA v0.7.15, DeepVariant, WhatsHap, hifiasm, minimap2] -> variant calling [WhatsHap, freebayes] -> dimensionality reduction/clustering [R, ggplot2 v3.3.3, tidyverse v1.3.0] -> stage not stated [BUSCO v3.1.0, Canu v2.0, Flye, Galaxy, Medaka, RepeatMasker v4.1.0, SAMtools, Snakemake]

### The Anglo-Saxon migration and the formation of the early English gene pool. (Nature 2022)

- DOI: 10.1038/s41586-022-05247-2 | PMCID: PMC9534755 | PMID: 36131019
- Evidence: We aligned merged sequences to human genome hg19 using BWA 80 v0.7.15 with a maximum number of differences (-n) of 0.01, a maximum number of gap opens (-o) of 2 and seed length (-l) of 16,500.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA, Picard] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK, SAMtools]

### Identification of trypsin-degrading commensals in the large intestine. (Nature 2022)

- DOI: 10.1038/s41586-022-05181-3 | PMCID: PMC9477747 | PMID: 36071157
- Evidence: Paired-end quality-filtered reads were mapped to the same gene catalogue from a previous study 36 with BWA 60 , filtered to include strong mappings with at least 95% sequence identity over the length of the read, counted and normalized to transcripts per million (TPM matrix).
- Full pipeline: read trimming [BWA, Canu v1.8] -> alignment/mapping [BWA, ChimeraX, PyMOL] -> quantification [BWA] -> normalisation [BWA] -> visualisation [ChimeraX, PyMOL] -> stage not stated [AlphaFold, ColabFold, Prokka, fastp v0.20.0, minimap2 v2.17]

### Non-viral, specifically targeted CAR-T cells achieve high safety and efficacy in B-NHL. (Nature 2022)

- DOI: 10.1038/s41586-022-05140-y | PMCID: PMC9452296 | PMID: 36045296
- Evidence: BWA (Burrows–Wheeler aligner) 47 was used to align clean reads for each sample against the reference genome (settings: mem -t 5 -M -R).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> normalisation [Seurat, UMAP] -> dimensionality reduction/clustering [GSVA, UMAP] -> differential/statistical testing [Seurat] -> stage not stated [GSEA, fastp]

### Truncated FGFR2 is a clinically actionable oncogene in multiple cancers. (Nature 2022)

- DOI: 10.1038/s41586-022-05066-5 | PMCID: PMC9436779 | PMID: 35948633
- Version used: **0.7.5a**
- Evidence: In brief, sequencing reads were mapped against the human reference genome GRCh37 using Burrows–Wheeler Alignment (BWA-MEM, v.0.7.5a) 86 .
- Full pipeline: read trimming [edgeR v3.26.6] -> alignment/mapping [BWA v0.7.5a, STAR v2.7.2] -> quantification [RSEM v1.3.0, edgeR v3.26.6, featureCounts v1.6.2] -> normalisation [edgeR v3.26.6] -> differential/statistical testing [R, limma v3.52.1]

### Spatially resolved clonal copy number alterations in benign and malignant tissue. (Nature 2022)

- DOI: 10.1038/s41586-022-05023-2 | PMCID: PMC9365699 | PMID: 35948708
- Evidence: In brief, the steps run were quality control of the FASTQ files using FastQC ( https://www.bioinformatics.babraham.ac.uk/projects/fastqc/ ), alignment of short reads to the human reference genome sequence (GRCh38/hg38) using bwa-mem with the ALT-aware option turned on 40 , sorting of reads and marking of PCR duplicates with GATK MarkDuplicates and base quality score recalibration and joint realign...
- Full pipeline: quality control [BWA, FastQC] -> read trimming [Cutadapt] -> alignment/mapping [BWA, FastQC] -> registration [BWA, FastQC] -> dimensionality reduction/clustering [GATK, UMAP] -> visualisation [Seurat v3.2.2] -> stage not stated [GSEA, Python, R, fgsea, tidyverse]

### Diverse mutational landscapes in human lymphocytes. (Nature 2022)

- DOI: 10.1038/s41586-022-05072-7 | PMCID: PMC9402440 | PMID: 35948631
- Evidence: Sequence data were mapped to the human genome reference GRCh37d5 using the BWA-MEM algorithm.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [R]

### The sequences of 150,119 genomes in the UK Biobank. (Nature 2022)

- DOI: 10.1038/s41586-022-04965-x | PMCID: PMC9329122 | PMID: 35859178
- Evidence: Sequence reads were mapped to human reference genome GRCh38 13 using BWA 14 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [IMPUTE2] -> normalisation [LDSC] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> differential/statistical testing [LDSC] -> stage not stated [GATK, SAMtools v1.9, VEP]

### Grey wolf genomic history reveals a dual ancestry of dogs. (Nature 2022)

- DOI: 10.1038/s41586-022-04824-9 | PMCID: PMC9279150 | PMID: 35768506
- Evidence: Reads were mapped to the dog reference genome canFam3.1 using BWA aln (v.0.7.17) 65 with permissive parameters, including a disabled seed (-l 16500 -n 0.01 -o 2).
- Full pipeline: alignment/mapping [BWA, Clustal Omega v1.2.4, Picard, SAMtools v1.9] -> variant calling [BCFtools, GATK, Picard] -> dimensionality reduction/clustering [R] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b]

### Biosynthetic potential of the global ocean microbiome. (Nature 2022)

- DOI: 10.1038/s41586-022-04862-3 | PMCID: PMC9259500 | PMID: 35732736
- Version used: **0.7.17**
- Evidence: To estimate mapping rates, all 1,038 metagenomic readsets were mapped against the 34,799 genomes included in the OMD using BWA (v.0.7.17-r1188, -a ).
- Full pipeline: read trimming [IQ-TREE v2.0.3] -> alignment/mapping [BWA v0.7.17, DIAMOND v0.9.30, IQ-TREE v2.0.3, MAFFT v7.310, MUSCLE v3.8.1551] -> dimensionality reduction/clustering [MAFFT v7.310, UMAP] -> visualisation [R v4.0.0, ggplot2 v3.3.0] -> stage not stated [HMMER v3.1b, eggNOG v5.0, featureCounts v2.0.1]

### The source of the Black Death in fourteenth-century central Eurasia. (Nature 2022)

- DOI: 10.1038/s41586-022-04800-3 | PMCID: PMC9217749 | PMID: 35705810
- Version used: **0.7.12**
- Evidence: We performed read mapping with BWA v.0.7.12 against the Y. pestis CO92 reference genome ( NC_003143.1 ).
- Full pipeline: alignment/mapping [BWA v0.7.12] -> variant calling [GATK] -> differential/statistical testing [BEAST v6.6, TreeTime v0.8.4] -> structure determination [R] -> stage not stated [BLAST, Picard, QGIS v3.22.1, RAxML, SAMtools v1.3]

### Graph pangenome captures missing heritability and empowers tomato breeding. (Nature 2022)

- DOI: 10.1038/s41586-022-04808-9 | PMCID: PMC9200638 | PMID: 35676474
- Evidence: ...graph pangenome and the linear genome. d , Assessing false-positive ( x -axis) and true-positive ( y -axis) rates for the graph (Giraffe) and linear (BWA-MEM) mappers using 2,000,000 simulated reads.
- Full pipeline: alignment/mapping [HISAT2 v2.10.2, StringTie v1.3.0, minimap2] -> variant calling [DeepVariant v1.0.0] -> quantification [kallisto v0.46.2] -> dimensionality reduction/clustering [PLINK v2.0] -> simulation/modelling [BWA] -> structure determination [WGCNA] -> machine learning [DeepVariant v1.0.0] -> stage not stated [AUGUSTUS v3.3.3, BUSCO, Flye v2.7, GCTA]

### Genome evolution and diversity of wild and cultivated potatoes. (Nature 2022)

- DOI: 10.1038/s41586-022-04822-x | PMCID: PMC9200641 | PMID: 35676481
- Version used: **0.7.5a**
- Evidence: To infer the phylogeny of the 432 accessions, reads were mapped to the DM v4 reference genome using BWA (0.7.5a-r405) 49 , and single-nucleotide polymorphisms (SNPs) were then extracted using SAMtools (v.1.9) 50 and BCFtools (v.1.9) 49 .
- Full pipeline: alignment/mapping [BCFtools v1.9, BWA v0.7.5a, DIAMOND v2.0.6.144, IQ-TREE v2.0.6, MAFFT v7.471, OrthoFinder v2.5.2, Python, SAMtools v1.9, minimap2 v2.21] -> dimensionality reduction/clustering [MAFFT v7.471, R] -> stage not stated [AUGUSTUS v3.4.0, BEDTools v2.29.2, BUSCO v4.1.4, HISAT2 v2.0.1, InterProScan v5.34, Pilon v1.23, RepeatMasker v1.332, StringTie v1.3.3b, hifiasm]

### Clonal dynamics of haematopoiesis across the human lifespan. (Nature 2022)

- DOI: 10.1038/s41586-022-04786-y | PMCID: PMC9177428 | PMID: 35650442
- Evidence: BWA mem was used to align 150 bp paired end reads generated to the human reference genome (NCBI build 37; GRCh37d5).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [R, lme4]

### The longitudinal dynamics and natural history of clonal haematopoiesis. (Nature 2022)

- DOI: 10.1038/s41586-022-04785-z | PMCID: PMC9177423 | PMID: 35650444
- Evidence: Reads were aligned to the human reference genome (NCBI build37) using BWA-MEM.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [R]

### ABO genotype alters the gut microbiota by regulating GalNAc levels in pigs. (Nature 2022)

- DOI: 10.1038/s41586-022-04769-z | PMCID: PMC9157047 | PMID: 35477154
- Version used: **0.7.17**
- Evidence: Clean reads were aligned to the S. scrofa reference genome assembly 11.1 50 using BWA (v.0.7.17) 51 .
- Full pipeline: read trimming [DADA2, Trimmomatic v0.39, fastp v0.19.41] -> alignment/mapping [BLAST, BWA v0.7.17, Bowtie2 v2.4.2, HISAT2 v2.2.1, Pilon v1.23, STAR, featureCounts v1.6.4, minimap2 v2.17] -> variant calling [Beagle, GCTA v1.26, GEMMA v0.97, PLINK v1.9] -> quantification [featureCounts v1.6.4] -> registration [Picard v2.21.4] -> differential/statistical testing [DESeq2] -> stage not stated [Canu v1.7.1, Flye v2.4.2, GATK v4.2, METAL v3.0, QIIME 2 v2018.11, R v3.5.3, SAMtools v1.6, Snakemake v7.0.1, mothur v1.43.0, vegan]

### Nonlinear control of transcription through enhancer-promoter interactions. (Nature 2022)

- DOI: 10.1038/s41586-022-04570-y | PMCID: PMC9021019 | PMID: 35418676
- Evidence: We mapped separately the ITR/splinkerette sides of the read pair to the mouse genome (build mm9) using BWA mem 62 with the default parameters.
- Full pipeline: alignment/mapping [BWA, Bowtie2, Cutadapt, SAMtools, minimap2 v2.17] -> quantification [Bioconductor] -> stage not stated [R, Snakemake, TrackMate]

### Somatic mutation rates scale with lifespan across mammals. (Nature 2022)

- DOI: 10.1038/s41586-022-04618-z | PMCID: PMC9021023 | PMID: 35418684
- Version used: **0.7.17**
- Evidence: Sequence read alignment For each species, sequences were aligned to a reference assembly (Supplementary Table 2 ) using the BWA-MEM algorithm 59 as implemented in BWA v.0.7.17-r1188, with options ‘-T 30 -Y -p -t 8’.
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.17] -> stage not stated [R]

### Ancient DNA and deep population structure in sub-Saharan African foragers. (Nature 2022)

- DOI: 10.1038/s41586-022-04430-9 | PMCID: PMC8907066 | PMID: 35197631
- Version used: **0.6.1**
- Evidence: We merged overlapping reads (at least 15 bases), trimmed barcode and adapter sequences from the ends, and mapped to the mtDNA reference genome RSRS 59 and the human reference genome hg19 using BWA (v.0.6.1) 60 .
- Full pipeline: read trimming [BWA v0.6.1] -> alignment/mapping [BWA v0.6.1] -> variant calling [BCFtools]

### TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. (Nature 2022)

- DOI: 10.1038/s41586-022-04436-3 | PMCID: PMC8891020 | PMID: 35197628
- Version used: **0.7.15**
- Evidence: In brief, paired-end 150-bp reads were aligned to the GRCh38 human reference using the Burrows-Wheeler Aligner (BWA-MEM v0.7.15) 64 and processed using the GATK best-practices workflow.
- Full pipeline: quality control [Picard, SAMtools] -> read trimming [Bowtie2, STAR v2.7.0f, Trimmomatic] -> alignment/mapping [BWA v0.7.15, Bowtie2, GATK, STAR v2.7.0f, Snakemake v5.5.4, Trimmomatic, minimap2] -> quantification [featureCounts] -> differential/statistical testing [DESeq2] -> stage not stated [BEDTools, ImageJ]

### Signatures of TOP1 transcription-associated mutagenesis in cancer and germline. (Nature 2022)

- DOI: 10.1038/s41586-022-04403-y | PMCID: PMC8866115 | PMID: 35140396
- Version used: **0.7.12**
- Evidence: FASTQ reads were aligned to the GSE56939_L03_ref_v2 reference genome 60 (Supplementary Table 5 ) and sorted BAM files were created using BWA-MEM (v.0.7.12) 61 , and deduplicated with SAMBLASTER (v.0.1.22) 62 .
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BCFtools v1.10.2, BWA v0.7.12, Mutect2] -> variant calling [BCFtools v1.10.2, GATK v3.6, Mutect2] -> normalisation [BCFtools v1.10.2] -> differential/statistical testing [SciPy v1.6.3] -> stage not stated [Manta v0.28.0, Python v3.8.5, R v4.0.5, SAMtools v1.9, Strelka v2.4.7]

### Attenuated fusogenicity and pathogenicity of SARS-CoV-2 Omicron variant. (Nature 2022)

- DOI: 10.1038/s41586-022-04462-1 | PMCID: PMC8942852 | PMID: 35104835
- Version used: **0.7.17**
- Evidence: NC_045512.2 ) using BWA-MEM v.0.7.17 47 .
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [fastp v0.21.0] -> variant calling [SAMtools v1.9] -> differential/statistical testing [Stan v2.28.1] -> simulation/modelling [Stan v2.28.1] -> stage not stated [BWA v0.7.17, ImageJ, R v3.6]

### Mutation bias reflects natural selection in Arabidopsis thaliana. (Nature 2022)

- DOI: 10.1038/s41586-021-04269-6 | PMCID: PMC8810380 | PMID: 35022609
- Version used: **0.7.17**
- Evidence: After adapter and quality trimming with cutadapt (version 2.3) and removing duplicates with samtools markdup (version 1.10), reads were aligned to the TAIR10 reference genome with bwa-mem (version 0.7.17) and variants were called independently for each sample with GATK HaplotypeCaller version 4.1.0.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v2.3, SAMtools] -> alignment/mapping [BWA v0.7.17, Bowtie2, Cutadapt v2.3, MACS2, R, SAMtools] -> variant calling [BWA v0.7.17, Cutadapt v2.3, GATK, SAMtools] -> differential/statistical testing [R] -> stage not stated [VCFtools]

### Targeting SWI/SNF ATPases in enhancer-addicted prostate cancer. (Nature 2022)

- DOI: 10.1038/s41586-021-04246-z | PMCID: PMC8770127 | PMID: 34937944
- Version used: **0.7.17**
- Evidence: Raw fastq files were aligned using BWA mem (version 0.7.17-r1198-dirty) with the −5SP options with an index containing only the main chromosome from the human genome release hg38 (available from the UCSC genome).
- Full pipeline: read trimming [SAMtools v1.3.1] -> alignment/mapping [BWA v0.7.17, Bowtie2, HTSeq, SAMtools v1.3.1, TopHat] -> quantification [HTSeq] -> differential/statistical testing [edgeR v3.34.1] -> stage not stated [ComplexHeatmap, GSEA, HOMER v4.10, MACS2 v2.1.1.20160309, PyMOL, R v3.6.0, deepTools v3.3.1, fgsea]

### Enhanced fusogenicity and pathogenicity of SARS-CoV-2 Delta P681R mutation. (Nature 2022)

- DOI: 10.1038/s41586-021-04266-9 | PMCID: PMC8828475 | PMID: 34823256
- Version used: **0.7.17**
- Evidence: 32 ) using BWA-MEM (v.0.7.17) 40 .
- Full pipeline: read trimming [fastp v0.21.0] -> alignment/mapping [MAFFT, fastp v0.21.0] -> variant calling [SAMtools v1.9] -> stage not stated [BWA v0.7.17, IQ-TREE, ImageJ v2.2.0]

### MSL2 ensures biallelic gene expression in mammals. (Nature 2023)

- DOI: 10.1038/s41586-023-06781-3 | PMCID: PMC10700137 | PMID: 38030723
- Evidence: In summary, MAPS aligned the FASTQ-files with BWA to the mm10 reference genome.
- Full pipeline: read trimming [Bismark v0.22.3, STAR v2.7.4, Trim Galore v0.6.5] -> alignment/mapping [BWA, Bismark v0.22.3, Bowtie2 v2.3.5, STAR v2.7.4, featureCounts v2.0.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R v3.6.2] -> stage not stated [BEDTools, DESeq2 v1.26.0, MACS2 v2.2.6, Picard, Seurat v4.1.0, Signac v1.5.0, deepTools, ggplot2 v3.3.2, pheatmap v1.0.12, tidyverse]

### Genetic continuity and change among the Indigenous peoples of California. (Nature 2023)

- DOI: 10.1038/s41586-023-06771-5 | PMCID: PMC10872549 | PMID: 37993721
- Evidence: ... the sequences to the human genome reference sequence (GRCh37 from the 1000 Genomes project) using the samse command of the Burrows-Wheeler Aligner ( BWA ) (version 0.6.1) 55 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.31, Picard v2.23.0, SAMtools, ggplot2 v3.4.3]

### Single-cell CRISPR screens in vivo map T cell fate regulomes in cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06733-x | PMCID: PMC10700132 | PMID: 37968405
- Version used: **0.7.16**
- Evidence: In brief, 2× 50-bp paired-end reads obtained from NovaSeq were trimmed for Nextera adaptor by trimmomatic (v.0.36; paired-end mode, with parameter LEADING:10 TRAILING:10 SLIDINGWINDOW:4:18 MINLEN:25) and aligned to mouse genome mm9 downloaded from GenCode release M1 ( https://www.gencodegenes.org/mouse/releases.html ) by BWA (v.0.7.16, default parameters).
- Full pipeline: quality control [Python] -> read trimming [BWA v0.7.16] -> alignment/mapping [BWA v0.7.16] -> variant calling [GSEA] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP, ggplot2 v3.3.5] -> differential/statistical testing [ComplexHeatmap, R, limma v3.48.3] -> simulation/modelling [Slingshot v2.0.0] -> visualisation [ComplexHeatmap, Cytoscape, UMAP, ggplot2 v3.3.5] -> stage not stated [BEDTools v2.25.0, HOMER, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.0.4]

### Epigenetic regulation during cancer transitions across 11 tumour types. (Nature 2023)

- DOI: 10.1038/s41586-023-06682-5 | PMCID: PMC10632147 | PMID: 37914932
- Evidence: We then used BWA 55 to align these unmapped reads against the constructed virus genome database.
- Full pipeline: quality control [FastQC] -> read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, FastQC, Trim Galore] -> dimensionality reduction/clustering [Slingshot, UMAP, clusterProfiler, scikit-learn v0.24.2] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools, GATK v4.1.2.0, MACS2, Mutect2, Picard v2.6.26, Python, R, SAMtools, SCENIC, Seurat v4.0.5, Signac, Strelka v2.9.10, VarScan v2.3.8, fgsea, scDblFinder, survival (R) v0.4.9]

### Mouse genome rewriting and tailoring of three important disease loci. (Nature 2023)

- DOI: 10.1038/s41586-023-06675-4 | PMCID: PMC10632133 | PMID: 37914927
- Version used: **0.7.17**
- Evidence: Trimmed reads were aligned to references using BWA v0.7.17.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, STAR] -> normalisation [deepTools v3.1.0, featureCounts v1.6.3] -> differential/statistical testing [featureCounts v1.6.3] -> stage not stated [Picard, fastp]

### Chromatin compartmentalization regulates the response to DNA damage. (Nature 2023)

- DOI: 10.1038/s41586-023-06635-y | PMCID: PMC10620078 | PMID: 37853125
- Evidence: BWA-MEM was used for mapping reads to a custom reference genome merging hg19 and dm6 (spike-in) chromosomes.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R, igraph] -> differential/statistical testing [edgeR] -> visualisation [tidyverse] -> stage not stated [HTSeq, deepTools]

### Genotyping, sequencing and analysis of 140,000 adults from Mexico City. (Nature 2023)

- DOI: 10.1038/s41586-023-06595-3 | PMCID: PMC10600010 | PMID: 37821707
- Evidence: Variant calling The MCPS WES and WGS data were reference-aligned using the OQFE protocol 35 , which uses BWA MEM to map all reads to the GRCh38 reference in an alt-aware manner, marks read duplicates and adds additional per-read tags.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BWA] -> dimensionality reduction/clustering [R] -> differential/statistical testing [REGENIE] -> stage not stated [BCFtools, DeepVariant v0.10.0, GATK, WhatsHap]

### Large-scale plasma proteomics comparisons through genetics and disease associations. (Nature 2023)

- DOI: 10.1038/s41586-023-06563-x | PMCID: PMC10567571 | PMID: 37794188
- Version used: **0.7.10**
- Evidence: ...ion-software.html ), Samtools (v1.9, v1.3, https://github.com/samtools/samtools ), samblaster (v0.1.24, https://github.com/GregoryFaust/samblaster ), BWA (v0.7.10 mem, https://github.com/lh3/bwa ), GenomeAnalysisTKLite (v2.3.9, https://github.com/broadgsa/gatk ), Picard tools (v1.117, https://broadinstitute.github.io/picard ), Bedtools (v2.25.0-76-g5e7c696z, https://github.com/arq5x/bedtools2 ), V...
- Full pipeline: quality control [GATK] -> differential/statistical testing [LDSC] -> stage not stated [BWA v0.7.10, Cytoscape v3.7.1, IMPUTE2 v2.3.1, Matplotlib v3.4.3, NumPy v1.20.3, Picard, Python v3.9.1, R v3.6.0, SAMtools v1.9, STRING db, SciPy v1.7.1, VEP]

### Gut microbial carbohydrate metabolism contributes to insulin resistance. (Nature 2023)

- DOI: 10.1038/s41586-023-06466-x | PMCID: PMC10499599 | PMID: 37648852
- Version used: **0.5.9**
- Evidence: The sequenced reads were processed with the MOIRAI pipeline 57 : low quality and rDNA reads were first removed, then the remaining reads were mapped to the human genome version hg38 patch 1 using BWA v.0.5.9 (r16).
- Full pipeline: alignment/mapping [BWA v0.5.9, Bowtie2] -> quantification [R, WGCNA, pheatmap v1.0.12] -> dimensionality reduction/clustering [R, WGCNA, pheatmap v1.0.12] -> differential/statistical testing [lme4 v1.1] -> visualisation [Cytoscape v3.7.0] -> stage not stated [Enrichr]

### Long-molecule scars of backup DNA repair in BRCA1- and BRCA2-deficient cancers. (Nature 2023)

- DOI: 10.1038/s41586-023-06461-2 | PMCID: PMC10482687 | PMID: 37587346
- Evidence: The number of reads in each MAPQ range for homeologous junctions (95,934 total) is: MAPQ 0–29: 19,201, MAPQ 30–39: 1,052, MAPQ 40–49: 868, MAPQ 50–59: 942, MAPQ 60: 73,871. b , Left, reference 150-mer BWA mapping quality in the neighbourhood of homeologous and non-homeologous break ends.
- Full pipeline: alignment/mapping [BWA, Picard] -> variant calling [GATK] -> registration [Picard] -> stage not stated [R, SnpEff]

### Einkorn genomics sheds light on history of the oldest domesticated wheat. (Nature 2023)

- DOI: 10.1038/s41586-023-06389-7 | PMCID: PMC10447253 | PMID: 37532937
- Version used: **0.7.17**
- Evidence: The methylation prediction for CCS reads was called using the model ‘model_ccsmeth_5mCpG_call_mods_attbigru2s_b21.v1.ckpt’ and then aligned to their respective genome using BWA (v.0.7.17) 96 and reads were filtered for hard/soft clips and quality (MAPQ ≥ 60) using SAMtools (v.1.8) 69 .
- Full pipeline: quality control [VCFtools] -> read trimming [BCFtools v1.9, Bowtie2, SAMtools, fastp] -> alignment/mapping [BCFtools v1.9, BWA v0.7.17, Bowtie2, SAMtools, STAR, StringTie, ggplot2, minimap2] -> variant calling [GATK, Python] -> dimensionality reduction/clustering [PLINK, VCFtools] -> visualisation [deepTools, ggplot2] -> stage not stated [BUSCO v5.0.0, Picard, R, SnpEff, featureCounts v2.0.0, hifiasm v15.1]

### Extensive pedigrees reveal the social organization of a Neolithic community. (Nature 2023)

- DOI: 10.1038/s41586-023-06350-8 | PMCID: PMC10432279 | PMID: 37495691
- Evidence: This included clipping adaptors with AdapterRemoval 49 , mapping with BWA (Burrows-Wheeler Aligner, mapping quality ≥30; v.0.7.12) 50 against the human reference genome hs37d5, and removing duplicate reads with the same orientation and start (and end positions for paired-end sequencing reads).
- Full pipeline: quality control [ANGSD] -> read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [QGIS v3.30]

### Early contact between late farming and pastoralist societies in southeastern Europe. (Nature 2023)

- DOI: 10.1038/s41586-023-06334-8 | PMCID: PMC10412445 | PMID: 37468624
- Version used: **0.7.12**
- Evidence: Subsequently, reads were mapped to the human reference genome hs37d5 using BWA v.0.7.12 (ref.
- Full pipeline: quality control [ANGSD] -> read trimming [BCFtools] -> alignment/mapping [BWA v0.7.12] -> variant calling [BCFtools] -> differential/statistical testing [SAMtools v1.3]

### A framework for individualized splice-switching oligonucleotide therapy. (Nature 2023)

- DOI: 10.1038/s41586-023-06277-0 | PMCID: PMC10371869 | PMID: 37438524
- Version used: **0.7.17**
- Evidence: Variant calling WGS reads were aligned to GRCh38/hg38 using BWA (v.0.7.17) (ref.
- Full pipeline: quality control [GATK] -> alignment/mapping [BWA v0.7.17, STAR v2.7.5c] -> variant calling [BWA v0.7.17] -> differential/statistical testing [R, survival (R)] -> stage not stated [DELLY v0.8.6, ImageJ, SAMtools v1.10, VCFtools v0.1.17, WhatsHap v1.0]

### SLC38A2 and glutamine signalling in cDC1s dictate anti-tumour immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06299-8 | PMCID: PMC10396969 | PMID: 37407815
- Version used: **0.7.16**
- Evidence: BWA (version 0.7.16) was used to align reads to mouse genome mm10 with default parameters.
- Full pipeline: alignment/mapping [BWA v0.7.16] -> variant calling [ComplexHeatmap v2.6.2] -> normalisation [R, limma v3.46.0] -> differential/statistical testing [R, limma v3.46.0] -> stage not stated [BEDTools v2.25.0, GSEA, MACS2 v2.1.1.20160309, Picard v2.9.4, Seurat v4.0.2]

### Ultraviolet radiation shapes dendritic cell leukaemia transformation in the skin. (Nature 2023)

- DOI: 10.1038/s41586-023-06156-8 | PMCID: PMC10284703 | PMID: 37286599
- Version used: **0.7.15**
- Evidence: Sequencing data for a total of 12 samples were mapped to the human genome reference (hg19; https://www.ncbi.nlm.nih.gov/data-hub/genome/GCF_000001405.13/ ) using BWA (v.0.7.15) 50 .
- Full pipeline: alignment/mapping [BWA v0.7.15, STAR v2.6.0c] -> variant calling [Seurat] -> quantification [SAMtools] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BCFtools v1.10.2, GATK, Mutect2, Picard v2.5.0, R, data.table, tidyverse]

### Epigenetic dysregulation from chromosomal transit in micronuclei. (Nature 2023)

- DOI: 10.1038/s41586-023-06084-7 | PMCID: PMC10322720 | PMID: 37286593
- Evidence: 6i ), reads were mapped to the mm10 genome using BWA-MEM (default settings), and duplicate marking and sorting were done using NovoSort MarkDuplicates (v.
- Full pipeline: read trimming [Bowtie2, fastp] -> alignment/mapping [BWA, Bowtie2, SAMtools, deepTools] -> normalisation [GSEA, deepTools] -> dimensionality reduction/clustering [clusterProfiler, pheatmap] -> differential/statistical testing [clusterProfiler] -> stage not stated [BEDTools v2.25.0, Bioconductor v3.15, DESeq2, Picard, R v4.2.1]

### In situ tumour arrays reveal early environmental control of cancer immunity. (Nature 2023)

- DOI: 10.1038/s41586-023-06132-2 | PMCID: PMC10284705 | PMID: 37258670
- Evidence: Sequencing reads were mapped to the UCSC mouse genome (GRCm38) using BWA software 31 set to the default parameters.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK, Strelka] -> normalisation [ComplexHeatmap] -> registration [GATK] -> dimensionality reduction/clustering [CellChat, GSEA, UMAP, clusterProfiler v3.18.1] -> differential/statistical testing [GSEA, SciPy v1.8.0, limma v3.46.0] -> machine learning [TensorFlow] -> stage not stated [Python, R, Seurat, edgeR, ggplot2 v3.3.5, ggpubr v0.4.0]

### ERα-associated translocations underlie oncogene amplifications in breast cancer. (Nature 2023)

- DOI: 10.1038/s41586-023-06057-w | PMCID: PMC10307628 | PMID: 37198482
- Version used: **0.7.15**
- Evidence: We used Bazam (v1.0.1) 51 to extract FASTQ files from the BAM or CRAM files and realigned the reads to hs37d5 (as done in PCAWG) using BWA-MEM (v0.7.15) 52 .
- Full pipeline: alignment/mapping [MACS2] -> registration [BWA v0.7.15, Picard v2.8.0, SAMtools v1.3.1] -> stage not stated [GSEA, Kraken2, RepeatMasker v4.1.2]

### Widespread somatic L1 retrotransposition in normal colorectal epithelium. (Nature 2023)

- DOI: 10.1038/s41586-023-06046-z | PMCID: PMC10191854 | PMID: 37165195
- Evidence: Sequences for L1-supporting reads near source elements were extracted and mapped to the L1HS consensus sequences 18 using BWA 60 .
- Full pipeline: read trimming [Bismark] -> alignment/mapping [BWA, Bismark, minimap2] -> stage not stated [Cutadapt, DELLY, Picard]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Evidence: Variant calling on GRCh38 with BWA-MEM and DeepVariant Small variants were also called using a more traditional pipeline.
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Mirusviruses link herpesviruses to giant viruses. (Nature 2023)

- DOI: 10.1038/s41586-023-05962-4 | PMCID: PMC10132985 | PMID: 37076623
- Version used: **0.7.15**
- Evidence: Briefly: anvi’o profiled contigs using Prodigal 43 v2.6.3 with default parameters to identify an initial set of genes; we mapped short reads from the metagenomic set to the contig using BWA v0.7.15 (ref.
- Full pipeline: read trimming [MAFFT] -> alignment/mapping [BLAST, BWA v0.7.15, MAFFT, SAMtools] -> dimensionality reduction/clustering [OrthoFinder] -> differential/statistical testing [IQ-TREE, SAMtools] -> structure determination [BLAST, IQ-TREE] -> visualisation [ChimeraX] -> stage not stated [AlphaFold, HMMER, RoseTTAFold]

### Extrachromosomal DNA in the cancerous transformation of Barrett's oesophagus. (Nature 2023)

- DOI: 10.1038/s41586-023-05937-5 | PMCID: PMC10132967 | PMID: 37046089
- Evidence: Reads were then aligned with BWA-MEM 51 to GRCh37 (1000 Genomes Project human_g1k_v37 with decoy sequences hs37d5).
- Full pipeline: alignment/mapping [BWA] -> registration [GATK] -> differential/statistical testing [SciPy v1.9.1] -> stage not stated [Strelka v2.0.15, VEP]

### The evolution of lung cancer and impact of subclonal selection in TRACERx. (Nature 2023)

- DOI: 10.1038/s41586-023-05783-5 | PMCID: PMC10115649 | PMID: 37046096
- Version used: **0.7.17**
- Evidence: Trimmed reads were aligned to the hg19 genome assembly (including unknown contigs) using BWA-MEM (v.0.7.17) 42 .
- Full pipeline: quality control [Bowtie2, FastQC v0.11.8, SAMtools v1.9] -> read trimming [BWA v0.7.17, Picard] -> alignment/mapping [BWA v0.7.17, Bowtie2, FastQC v0.11.8, Picard, SAMtools v1.9] -> registration [GATK v3.8.1] -> stage not stated [Mutect2 v1.1.7, R, fastp v0.20.0]

### The little skate genome and the evolutionary emergence of wing-like fins. (Nature 2023)

- DOI: 10.1038/s41586-023-05868-1 | PMCID: PMC10115646 | PMID: 37046085
- Evidence: Hi-C analysis Hi-C paired-end reads were mapped to the skate genome using BWA 94 .
- Full pipeline: quality control [Nextflow v19.10.0] -> read trimming [MAFFT v7.3, Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.3, Nextflow v19.10.0, SAMtools, STAR v2.5.2b, minimap2 v2.12] -> quantification [Nextflow v19.10.0] -> differential/statistical testing [DESeq2, MACS2, Nextflow v19.10.0, edgeR] -> visualisation [Nextflow v19.10.0] -> stage not stated [BEDTools, BLAST, BUSCO, IQ-TREE v2.1.1, Picard, Trinity v2.8.4]

### Lung adenocarcinoma promotion by air pollutants. (Nature 2023)

- DOI: 10.1038/s41586-023-05874-3 | PMCID: PMC7614604 | PMID: 37020004
- Version used: **0.7.17**
- Evidence: In brief, sequences were aligned with BWA (v.0.7.17) to mm10, and mutations were called using Mutect2 (gatk4: 4.1.8.1).
- Full pipeline: alignment/mapping [BWA v0.7.17, Mutect2, STAR v2.7.6a] -> quantification [ImageJ, Python, RSEM v1.3.1, scikit-learn] -> dimensionality reduction/clustering [DESeq2, Python, scikit-learn] -> stage not stated [GSEA, Nextflow v21.10.3, QuPath, R, SAMtools v1.12]

### Genomic investigations of unexplained acute hepatitis in children. (Nature 2023)

- DOI: 10.1038/s41586-023-06003-w | PMCID: PMC10170458 | PMID: 36996872
- Evidence: For HHV-6B, short reads were mapped with BWA mem 68 (0.7.17-r1188) using the RefSeq reference NC_000898 .
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Picard v2.26.9, SAMtools, Trim Galore] -> alignment/mapping [BCFtools, BWA, IQ-TREE, MAFFT, Picard v2.26.9, SAMtools, minimap2] -> variant calling [BCFtools] -> visualisation [Picard v2.26.9, SAMtools] -> stage not stated [Bowtie2, Kraken2, R]

### Adeno-associated virus 2 infection in children with non-A-E hepatitis. (Nature 2023)

- DOI: 10.1038/s41586-023-05948-2 | PMCID: PMC7617659 | PMID: 36996873
- Evidence: Illumina adapters were trimmed using Trim Galore ( https://github.com/FelixKrueger/TrimGalore ) and then mapped to the human genome using BWA-MEM ( https://github.com/lh3/bwa ).
- Full pipeline: read trimming [BWA, IQ-TREE, Trim Galore] -> alignment/mapping [BWA, IQ-TREE, MAFFT, Trim Galore] -> quantification [QuPath v0.3.2] -> differential/statistical testing [R]

### Palaeogenomics of Upper Palaeolithic to Neolithic European hunter-gatherers. (Nature 2023)

- DOI: 10.1038/s41586-023-05726-0 | PMCID: PMC9977688 | PMID: 36859578
- Version used: **0.7.12**
- Evidence: Within the pipeline, the adapters were removed by AdapterRemoval 2.2.0 65 , reads were mapped with BWA 0.7.12 aln/samse algorithm 66 , duplications were removed by DeDup 0.12.1 ( https://github.com/apeltzer/DeDup ) and damage patterns of each library were checked with mapDamage 2.0.6 and 2.0.9 67 .
- Full pipeline: quality control [ANGSD v0.934] -> read trimming [BWA v0.7.12] -> alignment/mapping [BWA v0.7.12, SAMtools] -> differential/statistical testing [R v3.5]

### Evolution of the germline mutation rate across vertebrates. (Nature 2023)

- DOI: 10.1038/s41586-023-05752-y | PMCID: PMC9995274 | PMID: 36859541
- Version used: **0.7.15**
- Evidence: The mapping was conducted with BWA-MEM version 0.7.15 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.15, Picard, SAMtools] -> variant calling [GATK v4.0.7.0] -> stage not stated [ANGSD, BCFtools v1.2, IQ-TREE v2.0.3, R]

### A NPAS4-NuA4 complex couples synaptic activity to DNA repair. (Nature 2023)

- DOI: 10.1038/s41586-023-05711-7 | PMCID: PMC9946837 | PMID: 36792830
- Evidence: Mapping using BWA was performed using the default parameters outlined in the package Debarcer v.0.3.1 ( https://github.com/oicr-gsi/debarcer/releases/tag/v0.3.1 ) 38 .
- Full pipeline: alignment/mapping [BEDTools, BWA, Bowtie2] -> quantification [featureCounts] -> dimensionality reduction/clustering [UMAP, scDblFinder] -> differential/statistical testing [DESeq2, R v3.6.1] -> visualisation [BEDTools, UMAP] -> stage not stated [MACS2 v2.1.1, Monocle, Picard, SAMtools, Seurat, edgeR, limma]

### Recurrent repeat expansions in human cancer genomes. (Nature 2023)

- DOI: 10.1038/s41586-022-05515-1 | PMCID: PMC9812771 | PMID: 36517591
- Version used: **0.6**
- Evidence: The base fastq file with a copy number of 2, in addition to the eight copy number-amplified fastq files, was aligned to chromosome 1 of GRCh37 with bwa-mem (v0.6) with the default options.
- Full pipeline: alignment/mapping [BWA v0.6] -> normalisation [DESeq2 v1.32.0, R v4.0.5] -> differential/statistical testing [Python, statsmodels v0.12.2] -> stage not stated [BEDTools, Enrichr, Matplotlib v3.4, SAMtools v1.13, SciPy]

### Non-viral precision T cell receptor replacement for personalized cell therapy. (Nature 2023)

- DOI: 10.1038/s41586-022-05531-1 | PMCID: PMC9768791 | PMID: 36356599
- Evidence: First, WES sequences were aligned to the human reference genome build 37 (GRCh37/hg19) using BWA-MEM 50 .
- Full pipeline: alignment/mapping [BWA, RSEM] -> quantification [RSEM] -> normalisation [RSEM] -> stage not stated [Mutect2]

### Structural variation in the pangenome of wild and domesticated barley. (Nature 2024)

- DOI: 10.1038/s41586-024-08187-1 | PMCID: PMC11655362 | PMID: 39537924
- Evidence: To elucidate tool bias as a confounding factor in the comparison between the mappings, we first produced a linearized version of the pangenome graph using gfatools gfa2fa ( https://github.com/lh3/gfatools ) and then mapped the WGS reads from all five accessions to this new reference sequence, using BWA mem as before for the cv.
- Full pipeline: read trimming [Cutadapt v3.3, Trimmomatic] -> alignment/mapping [BWA, Cutadapt v3.3, MAFFT, StringTie, minimap2 v2.20] -> quantification [Trimmomatic, kallisto] -> dimensionality reduction/clustering [MAFFT, VCFtools, pheatmap, tidyverse] -> differential/statistical testing [GEMMA v0.98.1, VCFtools, pheatmap] -> visualisation [PyMOL v2.5.5, R, ggplot2] -> stage not stated [BCFtools v1.9, BEDTools v2.29.2, BUSCO v3.0.2, SAMtools, data.table, hifiasm v0.11]

### Enhancing transcription-replication conflict targets ecDNA-positive cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07802-5 | PMCID: PMC11540844 | PMID: 39506153
- Evidence: Adaptor sequences were removed from raw fastq files using Trim Galore at default settings, followed by alignment to the hg38 reference genome using Map with BWA-MEM to generate the BAM files.
- Full pipeline: read trimming [Bowtie2, Trimmomatic] -> alignment/mapping [BWA, Bowtie2, Trim Galore, Trimmomatic] -> quantification [CellProfiler v4.2.1] -> normalisation [deepTools] -> visualisation [deepTools] -> stage not stated [HOMER v4.11.1, ImageJ v1.53t, MACS2, SAMtools v1.8]

### Coordinated inheritance of extrachromosomal DNAs in cancer cells. (Nature 2024)

- DOI: 10.1038/s41586-024-07861-8 | PMCID: PMC11541006 | PMID: 39506152
- Evidence: Reads were trimmed of adapter content with Trimmomatic 60 (v.0.39), aligned to the hg19 genome using BWA MEM 61 (0.7.17-r1188) and PCR duplicates were removed using Picard’s MarkDuplicates (v.2.25.3).
- Full pipeline: read trimming [BWA, Bowtie2 v2.1.0, Picard, Trim Galore v0.6.4, Trimmomatic] -> alignment/mapping [BWA, Bowtie2 v2.1.0, MACS2 v2.2.7.1, Picard, SAMtools v1.9, Trimmomatic] -> quantification [ImageJ] -> normalisation [deepTools] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [UMAP] -> visualisation [deepTools] -> stage not stated [ArchR v1.0.1, Seurat v3.2.3]

### The rise and transformation of Bronze Age pastoralists in the Caucasus. (Nature 2024)

- DOI: 10.1038/s41586-024-08113-5 | PMCID: PMC11602729 | PMID: 39478221
- Version used: **0.7.17**
- Evidence: Subsequently, BWA (v0.7.17) was used to map reads to the human reference genome hs37d5, and duplicates were removed using MarkDuplicates (v2.26.0). mapDamage (v2.2.1) was used to determine the deamination rate pattern (G to A and C to T substitutions) in the libraries.
- Full pipeline: quality control [ANGSD, FastQC] -> read trimming [BCFtools] -> alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE]

### Polyclonality overcomes fitness barriers in Apc-driven tumorigenesis. (Nature 2024)

- DOI: 10.1038/s41586-024-08053-0 | PMCID: PMC11525183 | PMID: 39478206
- Evidence: Mutation calling and filtering FASTQ files were aligned against the Genome Reference Consortium mouse genome 39 (GRCm39) 59 using BWA-MEM ( https://github.com/lh3/bwa ).
- Full pipeline: quality control [FastQC v0.11.9, Picard, STAR v2.7.7a] -> read trimming [Picard, Python, STAR v2.7.7a, Trimmomatic v0.39] -> alignment/mapping [BWA, Picard, STAR v2.7.7a, minimap2] -> quantification [QuPath v0.4.3] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [R] -> stage not stated [BEDTools v2.31.1, ImageJ, Mutect2, SAMtools v1.20, VEP]

### Clonal dynamics after allogeneic haematopoietic cell transplantation. (Nature 2024)

- DOI: 10.1038/s41586-024-08128-y | PMCID: PMC11602715 | PMID: 39478227
- Evidence: BWA-MEM was used to align sequences to the human reference genome (NCBI build37).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [lme4] -> stage not stated [R]

### Long-term lineage commitment in haematopoietic stem cell gene therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-08250-x | PMCID: PMC11618100 | PMID: 39442556
- Evidence: Sequences were aligned to the human reference genome (hg19/GRChg37) using BWA-MEM.
- Full pipeline: quality control [R] -> alignment/mapping [BWA] -> variant calling [SAMtools] -> dimensionality reduction/clustering [clusterProfiler, tidyverse] -> differential/statistical testing [NumPy v1.24.1, SciPy v1.10.1, scikit-learn v0.2, tidyverse] -> stage not stated [ggpubr]

### The interplay of mutagenesis and ecDNA shapes urothelial cancer evolution. (Nature 2024)

- DOI: 10.1038/s41586-024-07955-3 | PMCID: PMC11541202 | PMID: 39385020
- Version used: **0.7.15**
- Evidence: In brief, sequencing reads were aligned to GRCh38 with BWA-MEM (v.0.7.15) 56 .
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.18, STAR, minimap2 v2.26] -> quantification [featureCounts] -> normalisation [DESeq2 v1.24.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> visualisation [Enrichr] -> stage not stated [AnnData, Fiji, Flye v2.9.2, ImageJ, Manta v1.4.0, R, RepeatMasker, Scanpy v1.9.6, VEP v93.2]

### Inducing novel endosymbioses by implanting bacteria in fungi. (Nature 2024)

- DOI: 10.1038/s41586-024-08010-x | PMCID: PMC11560845 | PMID: 39358514
- Version used: **0.7**
- Evidence: For variant-calling with bcftools, reads were first aligned to the PacBio assembly of R. microsporus CBS 631.82 or to the M. rhizoxinica reference genome (GCF_000198775.1) using BWA-MEM v0.7 (ref.
- Full pipeline: alignment/mapping [BWA v0.7, SAMtools] -> variant calling [SAMtools] -> stage not stated [BCFtools, BUSCO v5.4.7, Flye v2.9.2, InterProScan, STRING db, SnpEff, eggNOG]

### Genetic links between ovarian ageing, cancer risk and de novo mutation rates. (Nature 2024)

- DOI: 10.1038/s41586-024-07931-x | PMCID: PMC11410666 | PMID: 39261734
- Evidence: Alignment_Alt_Score_diff: the difference in the alignment score between the best and the second best hit as reported by BWA mem.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> differential/statistical testing [REGENIE v2.2.4, statsmodels] -> visualisation [pheatmap, tidyverse] -> stage not stated [R v4.1.2]

### Recurrent evolution and selection shape structural diversity at the amylase locus. (Nature 2024)

- DOI: 10.1038/s41586-024-07911-1 | PMCID: PMC11485256 | PMID: 39232174
- Version used: **0.7.17**
- Evidence: 29 and were mapped to the human reference genome GRCh38 with BWA (v0.7.17; ‘bwa mem’) 48 .
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [R v4.2.2, Snakemake v7.32.3, VCFtools v0.1.16] -> differential/statistical testing [R v4.2.2, ggplot2] -> visualisation [ggplot2] -> stage not stated [BCFtools v1.9, IQ-TREE v2.2.2.3, Python, SAMtools, minimap2]

### Mechanisms that clear mutations drive field cancerization in mammary tissue. (Nature 2024)

- DOI: 10.1038/s41586-024-07882-3 | PMCID: PMC11374684 | PMID: 39232148
- Evidence: The CNA sequence analysis included the use of cutadapt for adaptor sequence removal and BWA for sequence alignment (using bwa aln, bwa mem) to the mm10 mouse genome.
- Full pipeline: alignment/mapping [BWA, Cutadapt] -> dimensionality reduction/clustering [Python] -> simulation/modelling [Python] -> visualisation [ImageJ, ggplot2] -> stage not stated [QuPath]

### Stem cells tightly regulate dead cell clearance to maintain tissue fitness. (Nature 2024)

- DOI: 10.1038/s41586-024-07855-6 | PMCID: PMC11390485 | PMID: 39169186
- Version used: **0.7.18**
- Evidence: ATAC-seq analysis Trimmed FASTQ files were obtained from the Rockefeller University’s Genome Resource Center and aligned to the mouse reference genome (UCSC release mm39) using Burrows-Wheeler Aligner (BWA, v.0.7.18), using BWA-MEM with default parameters.
- Full pipeline: read trimming [BWA v0.7.18] -> alignment/mapping [BWA v0.7.18, STAR v2.6] -> quantification [DESeq2, R v3.6.1, Salmon v1.4.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, GSEA, Jupyter, pandas v2.0.1] -> visualisation [NumPy v1.24.2, SciPy v1.10.1, UMAP, pandas v2.0.1, scikit-learn v1.2.0] -> stage not stated [AnnData v0.9.1, ImageJ v2.9.0, MACS2 v3.0.0, Matplotlib v3.7.1, SAMtools v1.17, deepTools v2.0.0, seaborn v0.13.1]

### Origin and evolution of the bread wheat D genome. (Nature 2024)

- DOI: 10.1038/s41586-024-07808-z | PMCID: PMC11424481 | PMID: 39143210
- Version used: **0.7.17**
- Evidence: Cleaned reads were mapped on the TA1675 assembly using BWA mem (v0.7.17) 79 and sorted with SAMtools (v1.8) 63 .
- Full pipeline: quality control [BUSCO v5.3.1, QUAST v5.0.2] -> read trimming [SAMtools v1.10, STAR v2.7.10b, Trimmomatic v0.40] -> alignment/mapping [BWA v0.7.17, Python, SAMtools v1.10, STAR v2.7.10b] -> visualisation [seaborn] -> stage not stated [BCFtools, BLAST, InterProScan v5.64, OrthoFinder, QGIS v3.32.3, R, RepeatMasker v4.1.2, SciPy, VCFtools v0.1.16, ggplot2 v3.4.2, hifiasm v0.16.1]

### Teosinte Pollen Drive guides maize diversification and domestication by RNAi. (Nature 2024)

- DOI: 10.1038/s41586-024-07788-0 | PMCID: PMC11390486 | PMID: 39112710
- Version used: **0.7.17**
- Evidence: Paired-end reads were aligned to the W22 reference genome 95 with BWA-MEM (v0.7.17) 100 .
- Full pipeline: read trimming [Cutadapt v3.1, STAR] -> alignment/mapping [BWA v0.7.17, Bowtie2, DeepVariant v0.4, GATK v3.0, SAMtools v1.10, STAR, deepTools, minimap2 v2.22] -> quantification [featureCounts] -> normalisation [BEDTools] -> differential/statistical testing [edgeR] -> visualisation [deepTools] -> stage not stated [BCFtools v1.14, BUSCO v5.5.0, Flye v2.9, VCFtools v0.1.16]

### Prognostic genome and transcriptome signatures in colorectal cancers. (Nature 2024)

- DOI: 10.1038/s41586-024-07769-3 | PMCID: PMC11374687 | PMID: 39112715
- Version used: **0.7.17**
- Evidence: Sentieon Genomics software (v.sentieon-genomics-202010; https://www.sentieon.com/ ) was used to map and process high-quality reads for downstream analysis 54 , which included the following optimised steps: (1) BWA-MEM (v.0.7.17-r1188) with the parameters ‘-M -K 100000000’ in alt-aware mapping model was used to align each tumour and control sample to the human genome reference hg38 (containing all ...
- Full pipeline: quality control [GATK, Picard] -> alignment/mapping [BWA v0.7.17, GATK, Picard, STAR v2.7.1a] -> variant calling [Mutect2] -> registration [GATK, Picard] -> dimensionality reduction/clustering [Seurat v4.1.0] -> differential/statistical testing [R, survival (R) v0.4.9] -> stage not stated [Bowtie2 v2.3.4.1, GSEA, GSVA, TensorFlow, tidyverse]

### Bridge RNAs direct programmable recombination of target and donor DNA. (Nature 2024)

- DOI: 10.1038/s41586-024-07552-4 | PMCID: PMC11208160 | PMID: 38926615
- Evidence: Merged fastq files were aligned to the RE–LE-bearing plasmid using bwa-mem 67 .
- Full pipeline: alignment/mapping [BWA, minimap2] -> dimensionality reduction/clustering [HMMER] -> stage not stated [BEDTools, BLAST, Python]

### Harnessing landrace diversity empowers wheat breeding. (Nature 2024)

- DOI: 10.1038/s41586-024-07682-9 | PMCID: PMC11338829 | PMID: 38885696
- Version used: **0.7.17**
- Evidence: Reads mapping, variant discovery, quality control and SNP annotation The clean reads were mapped to IWGSC RefSeq v1.0 using BWA-MEM (v0.7.17) 43 with default parameters.
- Full pipeline: quality control [BWA v0.7.17] -> read trimming [fastp] -> alignment/mapping [BWA v0.7.17, Picard v2.20.3, SAMtools v1.9] -> variant calling [Beagle, PLINK v1.90, scikit-learn] -> quantification [scikit-learn] -> dimensionality reduction/clustering [PLINK v1.90] -> stage not stated [ADMIXTURE, BCFtools, GATK v4.1.2, GEMMA v0.98.1, R, SnpEff v4.3t]

### Strand-resolved mutagenicity of DNA damage and repair. (Nature 2024)

- DOI: 10.1038/s41586-024-07490-1 | PMCID: PMC11186772 | PMID: 38867042
- Version used: **0.7.17**
- Evidence: 59 )) using BWA (v0.7.17) 74 .
- Full pipeline: read trimming [Picard v2.23.8] -> alignment/mapping [Bowtie2 v2.4.5, PyMOL v2.5.2, SAMtools] -> variant calling [SAMtools] -> dimensionality reduction/clustering [SciPy v1.7.1] -> differential/statistical testing [R] -> machine learning [StarDist, TensorFlow] -> stage not stated [BEDTools v2.30.0, BWA v0.7.17, Conda, Cutadapt v2.6, MACS2 v2.1.2, QuPath v0.2.2, Snakemake, data.table]

### Ancient Plasmodium genomes shed light on the history of human malaria. (Nature 2024)

- DOI: 10.1038/s41586-024-07546-2 | PMCID: PMC11222158 | PMID: 38867050
- Evidence: Adapter trimming and merging was performed using leeHom (v.1.1.5-eb382b3 or v.1.1.5-ba378b6) using the flag --ancientdna, and reads were mapped using BWA aln (v.0.7.12) with the following parameters: -n 0.01, -o 2 and -l 16500 (refs.
- Full pipeline: quality control [BEDTools, FastQC] -> read trimming [BWA, fastp v0.20.1] -> alignment/mapping [BEDTools, BWA, Picard, RAxML] -> variant calling [BEDTools, GATK, PLINK v1.90] -> differential/statistical testing [BEAST, SciPy] -> stage not stated [ADMIXTURE v1.3.0, Cartopy v0.20.3, SAMtools v1.3]

### Ancient genomes reveal insights into ritual life at Chichén Itzá. (Nature 2024)

- DOI: 10.1038/s41586-024-07509-7 | PMCID: PMC11208145 | PMID: 38867041
- Version used: **0.7.12**
- Evidence: Preprocessed sequences were mapped to the human genome assembly GRCh37 (hg19) from the Genome Reference Consortium 142 using BWA v.0.7.12 (ref.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.7.12] -> stage not stated [ADMIXTURE v1.3.0, SAMtools]

### Rhizobia-diatom symbiosis fixes missing nitrogen in the ocean. (Nature 2024)

- DOI: 10.1038/s41586-024-07495-w | PMCID: PMC11208148 | PMID: 38723661
- Evidence: T. diatomicola genome using BWA-MEM 61 v.0.7.17-r1188, and the resulting mapping files were filtered requiring at least 95% sequence identity and at least 80% of the read to align (mapping and filtering were done through CoverM v.0.6.1).
- Full pipeline: read trimming [MAFFT, Trimmomatic] -> alignment/mapping [BWA, MAFFT, SAMtools, SPAdes, minimap2] -> quantification [featureCounts] -> dimensionality reduction/clustering [MAFFT] -> machine learning [HMMER v3.1b] -> stage not stated [BLAST, Bowtie2, IQ-TREE, InterProScan, Prokka, eggNOG, hifiasm]

### Spatiotemporally resolved colorectal oncogenesis in mini-colons ex vivo. (Nature 2024)

- DOI: 10.1038/s41586-024-07330-2 | PMCID: PMC11078756 | PMID: 38658753
- Version used: **0.7.17**
- Evidence: DNA reads were mapped to the mouse GRCm39 genome assembly using BWA-MEM (v.0.7.17), filtered using samtools (v.1.9) and visualized using IGV (Integrative Genomics Viewer, Broad Institute, v.2.12.3).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.9] -> normalisation [UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [BWA v0.7.17, Cytoscape, SAMtools v1.9] -> stage not stated [GSEA, ImageJ, MACS2, Seurat v4.2.0, StarDist, edgeR]

### Emx2 underlies the development and evolution of marsupial gliding membranes. (Nature 2024)

- DOI: 10.1038/s41586-024-07305-3 | PMCID: PMC11062917 | PMID: 38658750
- Version used: **0.7.15**
- Evidence: Reads from the three libraries were pooled and mapped to the Hi-C P. breviceps assembly using BWA (v.0.7.15-r1188) 77 .
- Full pipeline: read trimming [Bowtie2 v2.4.2, STAR v2.7.9a, Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.15, Bowtie2 v2.4.2, MAFFT v7.453, SAMtools v1.12, STAR v2.7.9a, Trimmomatic v0.39] -> quantification [featureCounts v2.0.1] -> dimensionality reduction/clustering [UMAP] -> stage not stated [BEDTools, BLAST, BUSCO v5.4.4, Enrichr, MACS2 v2.2.7.1, RAxML v8.2.12, Scanpy, Seurat]

### Hybrid speciation driven by multilocus introgression of ecological traits. (Nature 2024)

- DOI: 10.1038/s41586-024-07263-w | PMCID: PMC11041799 | PMID: 38632397
- Version used: **0.7.15**
- Evidence: 54 ) using BWA-MEM v.0.7.15 (ref.
- Full pipeline: read trimming [Cutadapt v1.8.1] -> alignment/mapping [Cutadapt v1.8.1, GATK] -> variant calling [BCFtools v1.5, Cutadapt v1.8.1] -> registration [GATK] -> differential/statistical testing [Beagle v5.1] -> stage not stated [BEDTools v2.30.0, BWA v0.7.15, Picard v1.119, R, SAMtools]

### Tumour-selective activity of RAS-GTP inhibition in pancreatic cancer. (Nature 2024)

- DOI: 10.1038/s41586-024-07379-z | PMCID: PMC11111406 | PMID: 38588697
- Evidence: For copy number, FASTQ files are mapped to the target genome using the BWA mapper (bwa mem).
- Full pipeline: read trimming [Cutadapt v1.6] -> alignment/mapping [BWA, kallisto v0.44.0] -> quantification [edgeR, kallisto v0.44.0] -> normalisation [edgeR] -> differential/statistical testing [fgsea v1.26.0] -> stage not stated [GATK, ImageJ, R, VEP]

### The variation and evolution of complete human centromeres. (Nature 2024)

- DOI: 10.1038/s41586-024-07278-3 | PMCID: PMC11062924 | PMID: 38570684
- Evidence: We aligned the reads in the FASTQ files to the T2T-CHM13 reference genome 4 (v.2.0) using BWA 58 (v.0.7.17-r1188), sorted the alignments using SAMtools 59 (v.1.9) and marked duplicate reads using sambamba 60 (v.1.0).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BEDTools, BWA, MAFFT, SAMtools, deepTools, minimap2] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> structure determination [IQ-TREE] -> visualisation [ggplot2] -> stage not stated [HMMER, ImageJ v1.53k, RepeatMasker, hifiasm]

### Synthetic reversed sequences reveal default genomic states. (Nature 2024)

- DOI: 10.1038/s41586-024-07128-2 | PMCID: PMC11006607 | PMID: 38448583
- Version used: **0.7.17**
- Evidence: Whole-genome and Capture-seq reads were aligned using BWA v0.7.17 (ref.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Bowtie2 v2.2.9, DELLY, STAR v2.5.2a] -> normalisation [deepTools v3.5.0] -> visualisation [deepTools v3.5.0] -> stage not stated [BEDTools v2.29.2, Python, SAMtools v1.9]

### Mechanisms of action and resistance in histone methylation-targeted therapy. (Nature 2024)

- DOI: 10.1038/s41586-024-07103-x | PMCID: PMC10917674 | PMID: 38383791
- Version used: **0.7.15**
- Evidence: The sequenced data were aligned to the human reference genome hg38 by BWA (v0.7.15) software.
- Full pipeline: quality control [Trimmomatic v0.30] -> read trimming [Bismark v0.22.3, Trim Galore v0.6.7, Trimmomatic v0.30] -> alignment/mapping [BWA v0.7.15, Bismark v0.22.3, STAR] -> quantification [HTSeq v0.6.1] -> normalisation [Seurat] -> dimensionality reduction/clustering [DESeq2, Seurat] -> differential/statistical testing [GSEA, HTSeq v0.6.1] -> visualisation [PyMOL v2.4.0] -> stage not stated [ANNOVAR, Cutadapt, GATK v4.0.12, MACS2, Picard v2.92, Python, SAMtools v1.2, Signac v1.9.0]

### WNT signalling control by KDM5C during development affects cognition. (Nature 2024)

- DOI: 10.1038/s41586-024-07067-y | PMCID: PMC10954547 | PMID: 38383780
- Evidence: Reads were aligned using the BWA algorithm (mem mode; default settings).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.1, DESeq2 v1.18.0, R, SAMtools v1.9, STAR v2.5.2b] -> quantification [Cufflinks v2.1.0] -> normalisation [Cufflinks v2.1.0] -> differential/statistical testing [Cufflinks v2.1.0, DESeq2 v1.18.0, R] -> stage not stated [BEDTools, Bioconductor v3.6, GSEA, MACS2 v2.2.6, ggplot2 v2.2.1]

### Homo sapiens reached the higher latitudes of Europe by 45,000 years ago. (Nature 2024)

- DOI: 10.1038/s41586-023-06923-7 | PMCID: PMC10849966 | PMID: 38297117
- Evidence: Mapping was carried out with BWA 68 using adjustments for ancient DNA (-n 0.01 –o 2 –l 16500) 69 .
- Full pipeline: alignment/mapping [BWA] -> registration [MAFFT v7.453] -> structure determination [MAFFT v7.453] -> stage not stated [BEAST v2.6.6, QGIS, R v4.1, SAMtools]

### Redefining the treponemal history through pre-Columbian genomes from Brazil. (Nature 2024)

- DOI: 10.1038/s41586-023-06965-x | PMCID: PMC10917687 | PMID: 38267579
- Evidence: The mapping was carried out by BWA mem 88 (using parameters: -k 19, -r 2.5).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [Cutadapt v4.1, FastQC v0.11.9] -> alignment/mapping [BLAST, BWA, Cutadapt v4.1, IQ-TREE v1.6.10, MAFFT v7.467] -> differential/statistical testing [BEAST v2.6.7, SAMtools v1.7, VarScan v2.4.3] -> visualisation [ggplot2] -> stage not stated [Kraken2, Picard]

### Elevated genetic risk for multiple sclerosis emerged in steppe pastoralist populations. (Nature 2024)

- DOI: 10.1038/s41586-023-06618-z | PMCID: PMC10781639 | PMID: 38200296
- Version used: **0.7.17**
- Evidence: Single-end collapsed reads of at least 30 bp and paired-end reads were mapped to human reference genome build 37 using BWA (v0.7.17) 54 with seeding disabled to allow for higher sensitivity.
- Full pipeline: quality control [ANGSD v0.931] -> alignment/mapping [BWA v0.7.17] -> quantification [ANGSD v0.931] -> dimensionality reduction/clustering [ADMIXTURE, UMAP] -> stage not stated [PLINK, Picard, R, SAMtools v1.10]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Version used: **0.7.17**
- Evidence: Reads were trimmed with CutAdapt v.1.17, and Dip-C libraries were aligned with BWA 0.7.17.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### Ancient DNA from Shimao city records kinship practices in Neolithic China. (Nature 2025)

- DOI: 10.1038/s41586-025-09799-x | PMCID: PMC12711557 | PMID: 41299168
- Version used: **0.5.10**
- Evidence: Reads were aligned with BWA (v.0.5.10) 52 using the bam2bam command with default parameters, except for samples with no UDG treatment, for which we used the parameters -n 0.01, -l 16500 and -o 2.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.5.10] -> variant calling [PLINK] -> dimensionality reduction/clustering [ADMIXTURE]

### Origins of chromosome instability unveiled by coupled imaging and genomics. (Nature 2025)

- DOI: 10.1038/s41586-025-09632-5 | PMCID: PMC12695650 | PMID: 41162705
- Version used: **0.7.17**
- Evidence: Reads were aligned to GRCh38 reference assembly with BWA-MEM v.0.7.17, yielding a median of ~285,000 mapped unique fragments per cell, and further processed as described below.
- Full pipeline: alignment/mapping [BWA v0.7.17, minimap2] -> variant calling [DELLY, WhatsHap] -> quantification [ImageJ] -> machine learning [XGBoost] -> stage not stated [Bioconductor, Python]

### Evidence for improved DNA repair in the long-lived bowhead whale. (Nature 2025)

- DOI: 10.1038/s41586-025-09694-5 | PMCID: PMC12711569 | PMID: 41162698
- Version used: **0.7.13**
- Evidence: Sequencing analysis and mutation calling were performed as described 45 , using the following tools: Python v.2.7.18, TrimGalore v.0.4.1, BWA v.0.7.13, Samtools v.1.9, Picard v.1.119, GenomeAnalysisTK v.3.5, Bcftools v.1.9, and tabix v.0.2.6.
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [FastQC v0.11.9, Salmon v1.5.1, Trimmomatic v0.39] -> quantification [ImageJ, Python] -> normalisation [DESeq2] -> stage not stated [AlphaFold, BWA v0.7.13, GATK v4.2.5.0, Manta v1.6.0, Picard v1.119, SAMtools v1.9, Trim Galore v0.4.1]

### The Taiwan Precision Medicine Initiative provides a cohort for large-scale studies. (Nature 2025)

- DOI: 10.1038/s41586-025-09680-x | PMCID: PMC12675286 | PMID: 41092961
- Evidence: The sequencing reads were aligned to the human genome reference GRCh38 using BWA 41 .
- Full pipeline: alignment/mapping [BWA] -> variant calling [SHAPEIT] -> dimensionality reduction/clustering [PLINK v2.0] -> differential/statistical testing [REGENIE v4.1, SAIGE] -> stage not stated [ADMIXTURE v1.3.0, ANNOVAR, DeepVariant, WhatsHap]

### Sperm sequencing reveals extensive positive selection in the male germline. (Nature 2025)

- DOI: 10.1038/s41586-025-09448-3 | PMCID: PMC12611766 | PMID: 41062690
- Evidence: BWA-MEM 66 was used to align all sequences to the human reference genome (NCBI build37).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [Bioconductor, ggplot2 v3.4.4, lme4] -> visualisation [R] -> stage not stated [BCFtools, Nextflow]

### Efficient and accurate search in petabase-scale sequence repositories. (Nature 2025)

- DOI: 10.1038/s41586-025-09603-w | PMCID: PMC12657231 | PMID: 41062695
- Version used: **0.7.17**
- Evidence: Moreover, we also aligned all queries to the GENCODE (v.38) reference transcriptome using bwa-mem (v.0.7.17-r1188) 88 and against the hg38 human reference genome (GRCh38.p13, packaged with GENCODE v.38) using STAR (v.2.7.0 f) 89 .
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.0] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [Docker, Python, R v71.2, Snakemake]

### KCTD10 is a sensor for co-directional transcription-replication conflicts. (Nature 2025)

- DOI: 10.1038/s41586-025-09585-9 | PMCID: PMC12675284 | PMID: 41062692
- Evidence: Reads were mapped to the GRCh38 human reference genome using BWA-MEM with default settings 67 .
- Full pipeline: alignment/mapping [BWA, deepTools] -> quantification [deepTools] -> normalisation [deepTools] -> dimensionality reduction/clustering [AlphaFold, Matplotlib, seaborn] -> visualisation [ChimeraX] -> stage not stated [ColabFold v1.5.5, GATK, ImageJ, Metascape, Picard]

### Tracking clonal evolution during treatment in ovarian cancer using cell-free DNA. (Nature 2025)

- DOI: 10.1038/s41586-025-09580-0 | PMCID: PMC12629990 | PMID: 41034582
- Evidence: Sequencing reads were aligned to hg19 using BWA-MEM.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [Mutect2, Seurat]

### The formation and propagation of human Robertsonian chromosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-09540-8 | PMCID: PMC12657243 | PMID: 40993387
- Evidence: Hi-C data analysis We mapped Hi-C reads against the CHM13 genome and the phased genome assemblies of the three cell lines with the BWA aligner 68 , configured to handle the chimeric nature of Hi-C reads by allowing local mapping and tuning the parameters to minimize gaps.
- Full pipeline: read trimming [Bowtie2 v2.5.3, Trim Galore] -> alignment/mapping [BWA, Bowtie2 v2.5.3, SAMtools v1.17] -> differential/statistical testing [R v1.36.0] -> machine learning [Cellpose] -> stage not stated [BUSCO, Bioconductor, ImageJ, RepeatMasker v4.1.5]

### Functional synapses between neurons and small cell lung cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09434-9 | PMCID: PMC12571904 | PMID: 40931078
- Version used: **0.7.15**
- Evidence: Analysis of piggyBac insertions Sequencing reads that contained internal transposon sequences were excluded, and the remaining reads were aligned against the GRCm38 reference using BWA v0.7.15 and samtools v1.3.1.
- Full pipeline: alignment/mapping [BWA v0.7.15, GATK, SAMtools v1.3.1, STAR v2.4.2a] -> quantification [HTSeq v0.6.1p, ImageJ v1.54h] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [NumPy v1.20, SciPy v1.6.3] -> simulation/modelling [ANNOVAR] -> structure determination [IMOD v4.11.7] -> visualisation [Matplotlib v3.4.2, seaborn v0.11.0] -> stage not stated [Python, Scanpy v1.9.3]

### Single-cell transcriptomic and genomic changes in the ageing human brain. (Nature 2025)

- DOI: 10.1038/s41586-025-09435-8 | PMCID: PMC12527935 | PMID: 40903571
- Version used: **0.7.12**
- Evidence: In brief, reads were aligned to the human genome using bwa-mem (v.0.7.12) with default parameters.
- Full pipeline: alignment/mapping [BWA v0.7.12] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [R] -> stage not stated [Cellpose, GATK v4.1.8.1, Picard, Seurat]

### Commensal yeast promotes Salmonella Typhimurium virulence. (Nature 2025)

- DOI: 10.1038/s41586-025-09415-y | PMCID: PMC12460169 | PMID: 40903573
- Version used: **0.7.17**
- Evidence: RNA sequencing and analysis For basic processing of RNA sequencing data, raw reads were aligned to the reference assembly (GCF_000022165.1) using BWA-MEM (v0.7.17) 78 .
- Full pipeline: read trimming [Cutadapt v3.7, QIIME 2 v2019.7] -> alignment/mapping [BWA v0.7.17] -> quantification [edgeR, featureCounts v2.0.3] -> differential/statistical testing [edgeR, featureCounts v2.0.3] -> visualisation [ggplot2] -> stage not stated [DADA2, R v3.5.2, phyloseq, tidyverse]

### Ancient DNA connects large-scale migration with the spread of Slavs. (Nature 2025)

- DOI: 10.1038/s41586-025-09437-6 | PMCID: PMC12507669 | PMID: 40903570
- Evidence: This included clipping sequencing adaptors from reads with AdapterRemoval (v.2.3.1) 93 and mapping of reads with BWA (Burrows–Wheeler aligner) v.0.7.12 94 against the Human Reference Genome Hs37d5, with seed length (-l) disabled, maximum number of differences (-n) of 0.01 and a quality filter (-q) of 30.
- Full pipeline: quality control [ANGSD] -> read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> quantification [ADMIXTURE] -> differential/statistical testing [R v4.1.1] -> visualisation [R v4.1.1] -> stage not stated [PLINK, SAMtools, ggplot2 v3.3.6, tidyverse v1.0.9, vegan v2.6]

### TCF1 and LEF1 promote B-1a cell homeostasis and regulatory function. (Nature 2025)

- DOI: 10.1038/s41586-025-09421-0 | PMCID: PMC12507693 | PMID: 40836098
- Version used: **0.7.15**
- Evidence: FASTQ files were aligned to Enembl’s mouse GRCm38 genome using BWA (v0.7.15).
- Full pipeline: read trimming [limma] -> alignment/mapping [BWA v0.7.15, HISAT2, featureCounts v2.4] -> normalisation [limma] -> dimensionality reduction/clustering [UMAP, clusterProfiler] -> differential/statistical testing [GSEA, limma] -> simulation/modelling [Monocle v2.32.0] -> visualisation [UMAP] -> stage not stated [HOMER v4.8, Picard v2.1.1, R v4.4.1, Scanpy v1.9.8, Seurat]

### A missing enzyme-rescue metabolite as cause of a rare skeletal dysplasia. (Nature 2025)

- DOI: 10.1038/s41586-025-09397-x | PMCID: PMC12488480 | PMID: 40836090
- Evidence: Reads were mapped to the genome using the BWA-MEM algorithm (reference: http://bio-bwa.sourceforge.net/ ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK]

### Elementary 3D organization of active and silenced E. coli genome. (Nature 2025)

- DOI: 10.1038/s41586-025-09396-y | PMCID: PMC12460168 | PMID: 40804527
- Evidence: Mapping was performed using BWA with default pipeline parameters to the reference genome NC_000913.3 .
- Full pipeline: alignment/mapping [BWA] -> quantification [ImageJ] -> differential/statistical testing [DESeq2] -> visualisation [DESeq2] -> stage not stated [BEDTools, Conda, HOMER v4.11.1]

### Complete biosynthesis of salicylic acid from phenylalanine in plants. (Nature 2025)

- DOI: 10.1038/s41586-025-09175-9 | PMCID: PMC12408352 | PMID: 40702181
- Version used: **0.7.17**
- Evidence: To identify the mutation site, we mapped the reads to the rice reference genome using BWA-MEM (v.0.7.17) with the default parameters.
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.526, Picard, RAxML v8.2.12] -> stage not stated [InterProScan v5.69]

### Structural variation in 1,019 diverse humans based on long-read sequencing. (Nature 2025)

- DOI: 10.1038/s41586-025-09290-7 | PMCID: PMC12350158 | PMID: 40702182
- Evidence: To trace transductions to their source loci, transduced sequences were aligned onto CHM13 using BWA-MEM 90 .
- Full pipeline: alignment/mapping [BWA, DELLY, SAMtools] -> variant calling [BCFtools, WhatsHap] -> differential/statistical testing [VCFtools] -> stage not stated [ADMIXTURE v1.3.0, BEDTools, BLAST v2.12.0, RepeatMasker, VEP, minimap2]

### Ongoing genome doubling shapes evolvability and immunity in ovarian cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09240-3 | PMCID: PMC12390843 | PMID: 40670783
- Version used: **0.7.17**
- Evidence: The reads were then aligned with bwa-mem v0.7.17 (ref.
- Full pipeline: quality control [FastQC, Trim Galore] -> read trimming [FastQC, Trim Galore] -> alignment/mapping [BWA v0.7.17, FastQC, Picard v2.27.4, Trim Galore] -> variant calling [Mutect2, SHAPEIT] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [GSEA] -> stage not stated [QuPath, R, Seurat, StarDist]

### A haplotype-resolved pangenome of the barley wild relative Hordeum bulbosum. (Nature 2025)

- DOI: 10.1038/s41586-025-09270-x | PMCID: PMC12422954 | PMID: 40634612
- Version used: **0.7.17**
- Evidence: Reads were trimmed with cutadapt (version 1.15) and aligned to the haplotype 1 sequence assembly of FB19-011-3 with BWA-MEM (v0.7.17-r1188) 73 .
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17, Canu v2.1.1, Cutadapt v1.15, IQ-TREE v2.2.0, MAFFT v7.490, MUSCLE, R, SAMtools v1.16.1, STAR v2.7.8a, StringTie v2.1.5] -> variant calling [BWA v0.7.17, Cutadapt v1.15, DeepVariant v1.6.0] -> machine learning [DeepVariant v1.6.0] -> stage not stated [ADMIXTURE v1.3.0, BCFtools v1.9, BEDTools v2.30.0, BUSCO, PLINK v1.90b, hifiasm v0.13, minimap2 v2.24]

### Phylogenetically informative proteins from an Early Miocene rhinocerotid. (Nature 2025)

- DOI: 10.1038/s41586-025-09231-4 | PMCID: PMC12267063 | PMID: 40634620
- Evidence: We then mapped the collapsed reads against the reference genome of the white rhinoceros (GCF_000283155.1_CerSimSim1) using the BWA MEM function 62 with the shorter split hits being abandoned.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [ANGSD]

### Bimodal centromeres in pentaploid dogroses shed light on their unique meiosis. (Nature 2025)

- DOI: 10.1038/s41586-025-09171-z | PMCID: PMC12222009 | PMID: 40533552
- Evidence: Rubigineae )) that were not sequenced by long reads (Supplementary Data 17 ) were used as queries to map them with the software BWA 73 with the aln command to the R. canina chromosome assembly.
- Full pipeline: read trimming [Bismark v0.23.0, Trimmomatic v0.39] -> alignment/mapping [BCFtools v1.9, Bismark v0.23.0, Bowtie2, GATK, HISAT2 v2.1.0, IQ-TREE, MAFFT, Python, RAxML v8.2.12, SAMtools, SPAdes, Trimmomatic v0.39, minimap2] -> variant calling [GATK, Trimmomatic v0.39] -> registration [GATK] -> dimensionality reduction/clustering [R v4.4.0, RepeatMasker] -> differential/statistical testing [R v4.4.0] -> visualisation [tidyverse] -> stage not stated [BEDTools v2.30.0, BUSCO v5.4.0, BWA, DESeq2, HTSeq v2.0.1, MACS2, OrthoFinder, data.table, ggplot2, hifiasm]

### RIFINs displayed on malaria-infected erythrocytes bind KIR2DL1 and KIR2DS1. (Nature 2025)

- DOI: 10.1038/s41586-025-09091-y | PMCID: PMC12310515 | PMID: 40500441
- Evidence: The genomes of Lek174 and Lek79 were sequenced using MinION (Oxford Nanopore Technologies) and MiSeq, and their genomic contigs were generated from the obtained long reads and short reads using Flye 42 , BWA 43 , 44 and Pilon 45 programs.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.39] -> alignment/mapping [Bowtie2, Clustal Omega, PyMOL, featureCounts] -> normalisation [featureCounts] -> structure determination [Coot v0.8.9.2] -> stage not stated [BWA, Flye, ImageJ v1.54b, Pilon]

### SP140-RESIST pathway regulates interferon mRNA stability and antiviral immunity. (Nature 2025)

- DOI: 10.1038/s41586-025-09152-2 | PMCID: PMC12310523 | PMID: 40500448
- Version used: **0.7.15**
- Evidence: Adapters and low-quality reads were trimmed using BBDuk v.38.05 with the arguments ‘ktrim=r k=23 mink=11 hdist=1 maq=10 qtrim=r trimq=10 tpe tbo’ and mapped to mm10 using BWA-MEM v.0.7.15, and only uniquely mapping reads with a minimum MAPQ of 10 were retained.
- Full pipeline: read trimming [BWA v0.7.15] -> alignment/mapping [BWA v0.7.15, ChimeraX v1.6.1, HISAT2 v2.1.0, MACS2 v2.1.1, SAMtools, Salmon v0.13.1] -> variant calling [DESeq2 v1.38.3] -> quantification [Salmon v0.13.1] -> normalisation [deepTools] -> visualisation [ChimeraX v1.6.1, HISAT2 v2.1.0, SAMtools] -> stage not stated [AlphaFold, BEDTools, R, ggplot2 v3.5.0]

### Domesticated cannabinoid synthases amid a wild mosaic cannabis pangenome. (Nature 2025)

- DOI: 10.1038/s41586-025-09065-0 | PMCID: PMC12286863 | PMID: 40437092
- Version used: **0.7.17**
- Evidence: Sex chromosome SDR–PAR boundary identification and comparisons Y based k -mers (Y-mers) were mapped to X/Y haplotypes using BWA (v.0.7.17) mem, requiring perfect alignments and allowing multimapping up to 10 times.
- Full pipeline: read trimming [OrthoFinder v2.5.4, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.2.1, HMMER v3.3.2, IQ-TREE v1.6.12, MAFFT v7.505, SAMtools, minimap2 v2.24] -> variant calling [BLAST, BWA v0.7.17, R, ggplot2, minimap2 v2.24, tidyverse] -> quantification [Matplotlib, NumPy, SciPy] -> differential/statistical testing [Python, statsmodels] -> visualisation [Matplotlib, NumPy, SciPy] -> stage not stated [BCFtools, BEDTools, BUSCO v5.4.3, Nextflow v24.04.3.5916, RepeatMasker, Singularity v1.1.8, Snakemake, VCFtools, eggNOG, ggpubr]

### Two distinct host-specialized fungal species cause white-nose disease in bats. (Nature 2025)

- DOI: 10.1038/s41586-025-09060-5 | PMCID: PMC12222008 | PMID: 40437097
- Version used: **0.7.17**
- Evidence: Genomes were polished once using pre-trimmed Illumina reads with HyPo (v.1.0.3) after initial mapping using paired-end mapper Burrows–Wheeler aligner—Maximal Exact Match, bwa-mem (v.0.7.17-r1188) 63 , 64 .
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BEDTools, BWA v0.7.17, MAFFT] -> variant calling [BEDTools, R v4.1.1] -> differential/statistical testing [NanoPlot v1.42.0, VCFtools] -> machine learning [BUSCO v5.2.2] -> visualisation [ggplot2 v3.5.0] -> stage not stated [DIAMOND v2.1.7, Flye v2.9, Galaxy, HMMER v3.1, Picard v2.27.1, RepeatMasker, SAMtools, Stan, ape (R) v5.7.1, brms v2.20.3]

### Sequence diversity lost in early pregnancy. (Nature 2025)

- DOI: 10.1038/s41586-025-09031-w | PMCID: PMC12176622 | PMID: 40399685
- Evidence: In brief, reads were aligned with BWA mem 52 (v.0.7.10) and marked for duplicates with Picard tools (v.1.117).
- Full pipeline: alignment/mapping [BWA, Picard, R] -> variant calling [Manta v1.6.0] -> differential/statistical testing [R] -> machine learning [ADMIXTURE] -> stage not stated [PLINK, VEP]

### Genomics reveals zoonotic and sustained human mpox spread in West Africa. (Nature 2025)

- DOI: 10.1038/s41586-025-09128-2 | PMCID: PMC12310364 | PMID: 40388983
- Evidence: In brief, we mapped reads against a clade IIb reference genome ( NC_063383 , an early hMPXV-1 genome from Nigeria) with bwa-mem 34 , and called consensus using samtools 35 and iVar 36 .
- Full pipeline: alignment/mapping [BWA, SAMtools] -> structure determination [IQ-TREE v2.0] -> stage not stated [Nextstrain]

### Divergent DNA methylation dynamics in marsupial and eutherian embryos. (Nature 2025)

- DOI: 10.1038/s41586-025-08992-2 | PMCID: PMC12221971 | PMID: 40369084
- Evidence: Libraries were mapped to the MonDom5 reference genome using BWA-MEM 85 with the command bwa mem -t 32 -M -R.
- Full pipeline: read trimming [Bismark, Trim Galore] -> alignment/mapping [BEDTools, BWA, Bismark, HISAT2, SAMtools, featureCounts] -> quantification [DESeq2, featureCounts] -> stage not stated [BCFtools, GATK, R, RepeatMasker, Seurat v4.3.0, deepTools, ggplot2]

### Genomic and genetic insights into Mendel's pea genes. (Nature 2025)

- DOI: 10.1038/s41586-025-08891-6 | PMCID: PMC12221995 | PMID: 40269167
- Version used: **0.7.17**
- Evidence: 17 ), using BWA-MEM (v.0.7.17) with default parameters 63 .
- Full pipeline: quality control [Trimmomatic v0.39] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [Bismark v0.23.0, DELLY v0.8.7, HMMER v3.1b, MAFFT v7.475] -> variant calling [Beagle] -> dimensionality reduction/clustering [OrthoFinder v2.5.4, scikit-learn] -> visualisation [OrthoFinder v2.5.4] -> stage not stated [ADMIXTURE, BWA v0.7.17, DESeq2, GATK, GEMMA v0.98.1, IQ-TREE v2.1.2, PLINK, Picard v2.20.3, SAMtools, SnpEff, VCFtools v0.1.13]

### Geographic and age variations in mutational processes in colorectal cancer. (Nature 2025)

- DOI: 10.1038/s41586-025-09025-8 | PMCID: PMC12221974 | PMID: 40267983
- Evidence: All sequencing reads were aligned to the GRCh38 human reference genome using the Burrows–Wheeler Aligner MEM (BWA-MEM; v0.7.16a and v0.7.17) 47 .
- Full pipeline: alignment/mapping [BWA, Bowtie2, fastp] -> variant calling [ANNOVAR] -> quantification [R] -> visualisation [R]

### Human de novo mutation rates from a four-generation pedigree reference. (Nature 2025)

- DOI: 10.1038/s41586-025-08922-2 | PMCID: PMC12240836 | PMID: 40269156
- Evidence: Strand-seq data post-processing The demultiplexed FASTQ files were aligned to both GRCh38 and T2T-CHM13 reference assemblies (Supplementary Table 14 ) using BWA 66 (v.0.7.17-r1188) for standard library selection.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, GATK, MAFFT, MUSCLE, SAMtools, minimap2] -> variant calling [DeepVariant, GATK, R] -> stage not stated [BCFtools, BEDTools, HMMER, RAxML, RepeatMasker v4.1.6, VCFtools, hifiasm]

### Punic people were genetically diverse with almost no Levantine ancestors. (Nature 2025)

- DOI: 10.1038/s41586-025-08913-3 | PMCID: PMC12226237 | PMID: 40269169
- Evidence: We restricted our analysis to sequences of at least 30 base pairs in length, which aligned with a minimum mapping quality of least 10 to either the inferred ancestral mitochondrial genome sequence 47 , 48 or the human reference genome sequence (hg19) ( https://www.internationalgenome.org/category/grch37/ ), using the same command from BWA 47 .
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA] -> stage not stated [ADMIXTURE v1.3.0, BCFtools, PLINK, R, SAMtools]

### Mitochondrial metabolism sustains DNMT3A-R882-mutant clonal haematopoiesis. (Nature 2025)

- DOI: 10.1038/s41586-025-08980-6 | PMCID: PMC12158785 | PMID: 40239706
- Version used: **0.7.18**
- Evidence: Whole-exome sequencing data analysis Whole-exome sequencing reads of AML and control samples were mapped to the mouse genome assembly GRCm39 using BWA v.0.7.18 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.18] -> dimensionality reduction/clustering [REGENIE] -> differential/statistical testing [R v0.5.6, REGENIE, TwoSampleMR v0.5.6] -> stage not stated [Enrichr, GATK, Mutect2 v4.5, SAMtools v1.9, VEP]

### Timing and trajectory of BCR::ABL1-driven chronic myeloid leukaemia. (Nature 2025)

- DOI: 10.1038/s41586-025-08817-2 | PMCID: PMC12018454 | PMID: 40205062
- Evidence: Reads were aligned to the human reference genome (GRCh38, NCBI) using the BWA-MEM (Burrows–Wheeler Aligner) algorithm.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [R, lme4, metafor]

### Ancient DNA from the Green Sahara reveals ancestral North African lineage. (Nature 2025)

- DOI: 10.1038/s41586-025-08793-7 | PMCID: PMC12043513 | PMID: 40175549
- Evidence: Read adapters were removed using AdapterRemoval 70 v.2.3.0 as part of the EAGER (v.1.92.56) 71 , and the genome-wide captures were aligned to the human reference genome (hg19) using a mapping quality filter of 25 with BWA aligner 72 v.7.12.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, MAFFT] -> variant calling [SAMtools v1.3] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> stage not stated [PLINK, tidyverse v1.3.0]

### VDAC2 loss elicits tumour destruction and inflammation for cancer therapy. (Nature 2025)

- DOI: 10.1038/s41586-025-08732-6 | PMCID: PMC12018455 | PMID: 40108474
- Version used: **0.7.16**
- Evidence: These reads were then aligned to the mm10 mouse genome by BWA (v.0.7.16, default settings).
- Full pipeline: alignment/mapping [BWA v0.7.16] -> normalisation [DESeq2] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [DESeq2, limma v3.34.9] -> visualisation [R, UMAP, ggplot2] -> stage not stated [BEDTools v2.25.0, ComplexHeatmap v2.6.2, GSEA v4.3.2, MACS2 v2.1.1.20160309, Picard v2.9.4, SAMtools, Seurat v4.1]

### Genomic determinants of antigen expression hierarchy in African trypanosomes. (Nature 2025)

- DOI: 10.1038/s41586-025-08720-w | PMCID: PMC12137147 | PMID: 40074895
- Evidence: For the analysis of the transcriptional switch time courses, reads were mapped with bwa-mem 61 (v.0.7.17) and PCR duplicates were filtered out with Picard (v.3.2.0) ‘MarkDuplicates’ function.
- Full pipeline: read trimming [Python, featureCounts] -> alignment/mapping [BWA, Picard v3.2.0, STAR v2.7.10a, featureCounts, minimap2] -> quantification [deepTools] -> normalisation [deepTools] -> stage not stated [Cutadapt, Jupyter v7.31, Matplotlib v3.6.3, NumPy v1.23.5, SAMtools, Scanpy v1.7.2, SciPy v1.10.1, pandas v1.5.3, seaborn v0.12.2]

### High continuity of forager ancestry in the Neolithic period of the eastern Maghreb. (Nature 2025)

- DOI: 10.1038/s41586-025-08699-4 | PMCID: PMC12094895 | PMID: 40074896
- Evidence: After trimming barcodes and adapters, we aligned the reads to the mitochondrial reference genome RSRS [ 77 ] and the human reference genome (version hg19), using the samse command in BWA [ 78 ].
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> stage not stated [ANGSD]

### MYC ecDNA promotes intratumour heterogeneity and plasticity in PDAC. (Nature 2025)

- DOI: 10.1038/s41586-025-08721-9 | PMCID: PMC12003172 | PMID: 40074906
- Evidence: In brief, Fastp (v0.23.2) 52 removed low-quality bases and adapters, BWA Mem (v0.7.17-r1188) 53 mapped trimmed reads to the reference genome GRCh38 (v1.4.4), provided by the Genome Reference Consortium ( https://www.ncbi.nlm.nih.gov/grc ), mapped reads were marked for duplicates using Picard Markduplicates (v4.2.6.1), and read base-quality scores were recalibrated using GATK BaseRecalibrator (v4.2...
- Full pipeline: read trimming [BWA, Cutadapt v3.4] -> alignment/mapping [BWA, GATK, Picard, RSEM v1.3.3, STAR v2.7] -> quantification [ImageJ, RSEM v1.3.3, STAR v2.7, featureCounts] -> normalisation [DESeq2, Seurat v5.1.0] -> dimensionality reduction/clustering [Seurat v5.1.0] -> visualisation [R] -> stage not stated [deepTools, fgsea]

### Clonal dynamics and somatic evolution of haematopoiesis in mouse. (Nature 2025)

- DOI: 10.1038/s41586-025-08625-8 | PMCID: PMC12074984 | PMID: 40044850
- Evidence: Reads were aligned to the GRCm38 mouse reference genome using bwa-mem.
- Full pipeline: alignment/mapping [BWA] -> simulation/modelling [R] -> stage not stated [VEP, lme4]

### RNA neoantigen vaccines prime long-lived CD8&lt;sup&gt;+&lt;/sup&gt; T cells in pancreatic cancer. (Nature 2025)

- DOI: 10.1038/s41586-024-08508-4 | PMCID: PMC11946889 | PMID: 39972124
- Version used: **0.7.17**
- Evidence: In brief, we aligned reads to the reference human genome (hg19) using BWA (v0.7.17) 43 , and marked duplicates by picard-2.11.0 MarkDuplicates ( https://broadinstitute.github.io/picard/ ).
- Full pipeline: quality control [Scanpy] -> alignment/mapping [BWA v0.7.17] -> dimensionality reduction/clustering [UMAP] -> visualisation [R] -> stage not stated [GATK, GSEA, Mutect2 v1.1.7, Python v3.11.6, SciPy, Strelka v1.0.15]

### Plasmodium blood stage development requires the chromatin remodeller Snf2L. (Nature 2025)

- DOI: 10.1038/s41586-025-08595-x | PMCID: PMC11946908 | PMID: 39972139
- Version used: **0.7.17.2**
- Evidence: Filtered and trimmed reads were then mapped using BWA-MEM (v.0.7.17.2) 85 using paired-end simple Illumina mode to the P. falciparum 3D7 genome ( https://PlasmoDB.org ; release 52) and filtered for multi-mapped reads (MAPQ = 1 option).
- Full pipeline: quality control [FastQC v0.11.8, SAMtools v1.12] -> read trimming [BWA v0.7.17.2, STAR v2.7.9a, Trimmomatic v0.32.3] -> alignment/mapping [BWA v0.7.17.2, FastQC v0.11.8, SAMtools v1.12, STAR v2.7.9a, deepTools] -> quantification [DESeq2, ImageJ, featureCounts v2.12.2] -> differential/statistical testing [DESeq2, featureCounts v2.12.2] -> visualisation [ggpubr, tidyverse]

### Genetic architecture in Greenland is shaped by demography, structure and selection. (Nature 2025)

- DOI: 10.1038/s41586-024-08516-4 | PMCID: PMC11903302 | PMID: 39939757
- Evidence: After adaptor trimming, reads were mapped with BWA-MEM to GRCh38, and genotype calling was carried out with GATK haplotype caller.
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> variant calling [ADMIXTURE, BWA, GATK] -> normalisation [R] -> differential/statistical testing [TwoSampleMR v0.5.10] -> stage not stated [GEMMA v0.98.5, IMPUTE2, Python, SAMtools]

### Expanding the human gut microbiome atlas of Africa. (Nature 2025)

- DOI: 10.1038/s41586-024-08485-8 | PMCID: PMC11839480 | PMID: 39880958
- Version used: **0.7.17**
- Evidence: Reads aligning to version hg38 of the human genome were removed using BWA v.0.7.17 (ref.
- Full pipeline: read trimming [Trim Galore v0.6.7] -> alignment/mapping [BWA v0.7.17] -> quantification [lme4] -> differential/statistical testing [lme4] -> stage not stated [MAFFT v7.407, QUAST v5.2.0, R, ggplot2 v3.4.2, pheatmap v1.0.12, tidyverse v2.0.0, vegan v2.6]

### Bat genomes illuminate adaptations to viral tolerance and disease resistance. (Nature 2025)

- DOI: 10.1038/s41586-024-08471-0 | PMCID: PMC11821529 | PMID: 39880942
- Version used: **0.7.17**
- Evidence: HiC scaffolding To scaffold contigs into chromosome-level scaffolds, we first mapped the Arima V2 HiC data to the genome assemblies using bwa-mem v.0.7.17-r1188 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17, DeepVariant] -> normalisation [ChimeraX] -> dimensionality reduction/clustering [R] -> differential/statistical testing [brms] -> simulation/modelling [GROMACS v2022.1, PyMOL v2.5.0] -> machine learning [RepeatMasker] -> stage not stated [AlphaFold, BCFtools, BUSCO v5.1.1, Canu v2.2, ColabFold v1.3.0, IQ-TREE v2.1.3, ImageJ, RAxML v8.1.16, hifiasm v0.13]

### Continental influx and pervasive matrilocality in Iron Age Britain. (Nature 2025)

- DOI: 10.1038/s41586-024-08409-6 | PMCID: PMC11779635 | PMID: 39814899
- Evidence: Reads were mapped to GRCh37 with decoy contigs (hs37d5) using BWA software 67 with non-default parameters -l 16500, -n 0.02 and -o 2.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA] -> variant calling [BCFtools v1.10.2] -> registration [GATK, Picard, SAMtools] -> visualisation [ggplot2, tidyverse] -> stage not stated [R]

### Functional evaluation and clinical classification of BRCA2 variants. (Nature 2025)

- DOI: 10.1038/s41586-024-08388-8 | PMCID: PMC11821525 | PMID: 39779857
- Version used: **0.7.17**
- Evidence: The single reads were aligned to the human reference genome (GRCh38) utilizing bwa-mem (v.0.7.17).
- Full pipeline: read trimming [Cutadapt v3.5] -> alignment/mapping [BWA v0.7.17, PyMOL] -> dimensionality reduction/clustering [PyMOL] -> stage not stated [JAGS]

### Learning the fitness dynamics of pathogens from phylogenies. (Nature 2025)

- DOI: 10.1038/s41586-024-08309-9 | PMCID: PMC11735385 | PMID: 39743587
- Evidence: Using BWA-MEM 45 (v0.7.17), reads were mapped against the complete Tohama I reference genome (accession number in RefSeq: NC_002929 ) or the complete H37Rv reference genome (accession number in RefSeq: NC_000962.3 ).
- Full pipeline: quality control [Cutadapt, FastQC] -> read trimming [Cutadapt, FastQC] -> alignment/mapping [BWA, GATK, MAFFT] -> structure determination [BEAST v1.10.4] -> stage not stated [Stan]

### Ancient genomes reveal a deep history of Treponema pallidum in the Americas. (Nature 2025)

- DOI: 10.1038/s41586-024-08515-5 | PMCID: PMC11964931 | PMID: 39694065
- Version used: **0.7.12**
- Evidence: Pre-processed sequences were mapped to the human genome assembly GRCh37 (hg19) from the Genome Reference Consortium 76 using BWA v.
- Full pipeline: read trimming [SAMtools] -> alignment/mapping [BWA v0.7.12, SAMtools] -> machine learning [ADMIXTURE] -> visualisation [BEDTools, R v4.2.2, ggplot2] -> stage not stated [ANGSD v0.935, BEAST, RAxML]

### Earliest modern human genomes constrain timing of Neanderthal admixture. (Nature 2025)

- DOI: 10.1038/s41586-024-08420-x | PMCID: PMC11839475 | PMID: 39667410
- Version used: **0.5.10**
- Evidence: We demultiplexed the resulting sequences on the basis of perfect matching of the expected index combinations, and mapped them to the hg19 reference genome with BWA (v.0.5.10-evan.9-1-g44db244, https://github.com/mpieva/network-aware-bwa ) with the ancient parameters (‘-n 0.01 -o 2 -l 16500’) 52 (Supplementary Information 3 ).
- Full pipeline: read trimming [BWA v0.5.10] -> alignment/mapping [BWA v0.5.10, Bowtie2, GATK, SAMtools] -> variant calling [GATK] -> visualisation [ggplot2 v3.4.2, tidyverse v1.1.4] -> stage not stated [BEDTools]

### Fetal hepatocytes protect the HSPC genome via fetuin-A. (Nature 2025)

- DOI: 10.1038/s41586-024-08307-x | PMCID: PMC11711094 | PMID: 39633051
- Evidence: ATAC-seq data processing All reads were aligned to the mm10 genome using the Burrows-Wheeler Aligner (BWA-MEM) after trimming the adapter sequences with Trim_Galore (v0.6.7).
- Full pipeline: quality control [Trim Galore v0.6.7] -> read trimming [BWA] -> alignment/mapping [BWA, Bowtie2 v2.3.5.1, HISAT2 v2.2.1, HTSeq] -> normalisation [deepTools v3.5.1] -> dimensionality reduction/clustering [clusterProfiler v3.14.3] -> differential/statistical testing [DESeq2 v1.26.0, HOMER v4.11] -> visualisation [deepTools v3.5.1] -> stage not stated [ImageJ v1.52p, MACS2, Picard v2.25.5, R]

### Dairy cows inoculated with highly pathogenic avian influenza virus H5N1. (Nature 2025)

- DOI: 10.1038/s41586-024-08166-6 | PMCID: PMC11754099 | PMID: 39406346
- Evidence: The pipeline maps cleaned reads to the reference cattle strain derived from sequencing the stock inoculum of A/dairy cattle/Texas/24-008749-002/2024 using BWA (bwa index –a bwtsw) 40 .
- Full pipeline: stage not stated [BWA, GATK v4.4, R v4.4]

### Genetic architecture of sugarcane traits in a polyploid genomics framework. (Nature 2026)

- DOI: 10.1038/s41586-026-10576-7 | PMCID: PMC13293862 | PMID: 42203877
- Evidence: Hi-C H-trans error: Hi-C alignments by BWA 58 with a mapping quality score (MAPQ) of 0 were discarded to ensure reliable mapping.
- Full pipeline: alignment/mapping [BLAST, BWA, minimap2] -> variant calling [BCFtools] -> quantification [PLINK] -> dimensionality reduction/clustering [R, minimap2] -> structure determination [AUGUSTUS] -> machine learning [AUGUSTUS] -> stage not stated [BEDTools, BUSCO, Cellpose, RepeatMasker, SnpEff, VCFtools, hifiasm]

### Safety and efficacy of intratumoural anti-CTLA4 with intravenous anti-PD1. (Nature 2026)

- DOI: 10.1038/s41586-026-10341-w | PMCID: PMC13323097 | PMID: 42056527
- Version used: **0.7.12**
- Evidence: Reads were mapped to the GRCh37 human reference genome using BWA-MEM (v0.7.12) software.
- Full pipeline: quality control [SAMtools v1.9] -> alignment/mapping [BWA v0.7.12, kallisto] -> quantification [kallisto] -> differential/statistical testing [tidyverse] -> stage not stated [GATK, Mutect2, R, ggplot2 v3.4.4, ggpubr v0.6.0]

### Cytoplasmic competition between separate parental pronuclei in zygotes. (Nature 2026)

- DOI: 10.1038/s41586-026-10417-7 | PMCID: PMC13233321 | PMID: 42056509
- Version used: **0.7**
- Evidence: After mapping the JF1/Ms reads to the mouse genome (mm10) using BWA-MEM v.0.7 with the default parameters, SNPs were called using HaplotypeCaller implemented in GATK v.4.1.4.1 (ref.
- Full pipeline: read trimming [Bowtie2 v2.3, edgeR v3.40.2] -> alignment/mapping [BWA v0.7, Bowtie2 v2.3, GATK v4.1.4.1, featureCounts v2.0.0] -> variant calling [BWA v0.7, GATK v4.1.4.1] -> quantification [deepTools v3.5.1, pheatmap] -> normalisation [deepTools v3.5.1, edgeR v3.40.2] -> differential/statistical testing [edgeR v3.40.2] -> visualisation [deepTools v3.5.1, pheatmap] -> stage not stated [BEDTools v2.26.0, MACS2 v2.2.9.1, fastp v0.20.0]

### Chromosomal fusions trigger rediploidization of autopolyploid genomes. (Nature 2026)

- DOI: 10.1038/s41586-026-10439-1 | PMCID: PMC13275295 | PMID: 42020748
- Version used: **0.7.18**
- Evidence: Then, Hi-C reads were mapped into unitigs using BWA (0.7.18) mem 54 with the -5SP parameter.
- Full pipeline: alignment/mapping [BWA v0.7.18, GATK v4.5.0.0, HISAT2 v2.2.1, IQ-TREE v2.0.3, MAFFT v7.526, StringTie v2.2.3, minimap2 v2.28] -> variant calling [GATK v4.5.0.0, Picard] -> quantification [featureCounts v2.0.6] -> normalisation [featureCounts v2.0.6] -> differential/statistical testing [DESeq2 v1.44] -> structure determination [ImageJ v2.9.0] -> stage not stated [BUSCO v5.7.0, RepeatMasker v4.1.5]

### Ancient DNA reveals pervasive directional selection across West Eurasia. (Nature 2026)

- DOI: 10.1038/s41586-026-10358-1 | PMCID: PMC13189228 | PMID: 41986721
- Evidence: We aligned merged sequences to the hg19 version of the human reference genome with decoy sequences (hs37d5) using the single-ended aligner, BWA SAMSE v.0.7.15 256 with typical ancient DNA alignment parameters −n 0.01 −o 2 and −l 16500 which disables pre-alignment seeding.
- Full pipeline: alignment/mapping [BWA] -> variant calling [BCFtools] -> dimensionality reduction/clustering [Python, scikit-learn] -> differential/statistical testing [LDSC, PLINK] -> stage not stated [GEMMA v0.98.5, Picard]

### Cell-type-targeted mitochondrial transplantation rescues cell degeneration. (Nature 2026)

- DOI: 10.1038/s41586-026-10391-0 | PMCID: PMC13149334 | PMID: 41986718
- Version used: **0.7.17**
- Evidence: Genomic mapping, identification of genetic variations and variant annotation For each sample, we aligned the raw genome-sequencing data to the human reference genome sequence (build hg19/GRCh37) using BWA-MEM (v.0.7.17) 78 .
- Full pipeline: read trimming [Trimmomatic v2.6.0] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.10, STAR v2.7.10b] -> variant calling [GATK] -> quantification [ImageJ] -> dimensionality reduction/clustering [clusterProfiler v4.14.0] -> differential/statistical testing [DESeq2 v1.38] -> machine learning [Cellpose] -> stage not stated [ANNOVAR, AlphaFold, BCFtools v1.10.2, ColabFold, MACS2, Python, R, Scanpy, Snakemake v7.21.0, limma]

### Polyclonal selection of immune checkpoint mutations in thyroid autoimmunity. (Nature 2026)

- DOI: 10.1038/s41586-026-10493-9 | PMCID: PMC13233322 | PMID: 41981327
- Evidence: Sequencing reads were aligned to the GRCh37 (hs37d5 build) reference genome by the Burrows–Wheeler algorithm (BWA-MEM) 55 .
- Full pipeline: alignment/mapping [BWA, SAMtools] -> differential/statistical testing [Picard] -> stage not stated [R, Seurat, ggpubr, tidyverse]

### The 1000 Chinese Pangenome empowers medical and population genetics. (Nature 2026)

- DOI: 10.1038/s41586-026-10315-y | PMCID: PMC13233627 | PMID: 41922767
- Version used: **0.7.17**
- Evidence: For the 1KCP samples, short-read data were aligned using BWA-MEM (v.0.7.17) 62 , and SNV genotypes were called using the GATK (v.4.2.6.1) workflow 63 .
- Full pipeline: read trimming [BEDTools v2.30.0] -> alignment/mapping [BLAST v2.13.0, BWA v0.7.17, GATK v4.2.6.1, HISAT2, STAR v2.7.9, StringTie v2.2.1, minimap2 v2.24] -> variant calling [BWA v0.7.17, DeepVariant v1.4.0, GATK v4.2.6.1, WhatsHap v1.4, hifiasm v0.15.3] -> quantification [STAR v2.7.9] -> normalisation [edgeR v3.22.5] -> dimensionality reduction/clustering [clusterProfiler v4.12.6] -> differential/statistical testing [BCFtools v1.20] -> stage not stated [GCTA, InterProScan v5.66, Manta v1.6.0, PLINK, RepeatMasker v4.1.1]

### Genomic history of early dogs in Europe. (Nature 2026)

- DOI: 10.1038/s41586-026-10112-7 | PMCID: PMC13017524 | PMID: 41882126
- Evidence: Metagenomic screening and authentication Reads not aligning to the dog reference genome were screened for microbial DNA by competitive alignment to a curated pathogen reference panel using BWA aln 62 , with parameters identical to those for host mapping.
- Full pipeline: alignment/mapping [BWA] -> dimensionality reduction/clustering [ADMIXTURE v1.3.0]

### The DNA virome varies with human genes and environments. (Nature 2026)

- DOI: 10.1038/s41586-026-10288-y | PMCID: PMC13215884 | PMID: 41882355
- Evidence: Sequencing reads from libraries prepared with Illumina DNA PCR-Free Library Prep kit were aligned to human reference build GRCh38 with BWA-MEM by the New York Genome Center (NYGC) using Centers for Common Disease Genomics project standards.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [DeepVariant] -> differential/statistical testing [LDSC] -> stage not stated [R]

### A sorghum pangenome reference improves global crop trait discovery. (Nature 2026)

- DOI: 10.1038/s41586-026-10229-9 | PMCID: PMC13128447 | PMID: 41813899
- Version used: **0.7.17**
- Evidence: Homozygous SNPs and indels were corrected to match the consensus call from Illumina fragment reads (2 × 150, 400 bp insert) by aligning the reads using bwa-mem (v.0.7.17-r1188) 63 and identifying homozygous SNPs and indels with the UnifiedGenotyper tool in GATK (v.3.6-0-g89b7209) 64 .
- Full pipeline: alignment/mapping [AUGUSTUS v3.1.0, BWA v0.7.17, GATK v3.6, minimap2 v2.22] -> variant calling [ADMIXTURE v1.3.0, BWA v0.7.17, GATK v3.6, SAMtools v1.7, SnpEff v5.1d] -> registration [Picard] -> dimensionality reduction/clustering [R] -> machine learning [AUGUSTUS v3.1.0, R] -> visualisation [PyMOL] -> stage not stated [AutoDock Vina, BCFtools v1.9, BUSCO, Bioconductor, GEMMA v0.98.3, InterProScan v5.47, OrthoFinder v2.5.5, PLINK v1.90b, RepeatMasker, SHAPEIT]

### Homologous recombination deficiency and hemizygosity drive resistance in breast cancer. (Nature 2026)

- DOI: 10.1038/s41586-026-10197-0 | PMCID: PMC13083263 | PMID: 41781623
- Version used: **0.7.17**
- Evidence: FASTQ files from WES and targeted sequencing were aligned to the hg19 build of the human genome using the Burrows–Wheeler Aligner (BWA v0.7.17-r1188) 63 .
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA v0.7.17, Picard] -> stage not stated [BCFtools v1.11, CNVkit v0.9.8, GATK v3.7, SAMtools, Strelka v2.9.10, VEP]

### DICER cleavage fidelity is governed by 5'-end binding pockets. (Nature 2026)

- DOI: 10.1038/s41586-026-10211-5 | PMCID: PMC13171623 | PMID: 41781616
- Evidence: The processed reads were mapped to the pre-mir-324 reference sequence using the BWA mapping toolkit 45 .
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, Bowtie2, Coot v0.9.8.96] -> dimensionality reduction/clustering [AlphaFold] -> structure determination [ChimeraX v1.7, Coot v0.9.8.96, PHENIX v1.20.1] -> stage not stated [PyMOL]

### Coral microbiomes as reservoirs of unknown genomic and biosynthetic diversity. (Nature 2026)

- DOI: 10.1038/s41586-026-10159-6 | PMCID: PMC13083261 | PMID: 41741644
- Version used: **0.7.17**
- Evidence: Reads were mapped with BWA (v.0.7.17-r1188) 110 , allowing the reads to map at secondary sites (with the -a flag).
- Full pipeline: alignment/mapping [BLAST v2.15.0, BWA v0.7.17, DIAMOND v2.0.15.153, Flye v2.9.3] -> differential/statistical testing [R v4.2.2, ape (R) v5.7] -> structure determination [BLAST v2.15.0] -> visualisation [ape (R) v5.7] -> stage not stated [AlphaFold v2.2.0, ComplexHeatmap v2.14.0, eggNOG v5.0.2, ggplot2 v3.4.2]

### A disease model resource reveals core principles of tissue-specific cancer evolution. (Nature 2026)

- DOI: 10.1038/s41586-026-10187-2 | PMCID: PMC13149333 | PMID: 41741657
- Version used: **0.7.17**
- Evidence: Passing reads were then aligned to the GRCm38.p6 reference genome using BWA-MEM (v.0.7.17) 59 with the default settings.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools] -> normalisation [DESeq2, GSVA, UMAP] -> dimensionality reduction/clustering [UMAP] -> visualisation [ComplexHeatmap v2.16.0, R v4.4.1, data.table v1.14.8, ggplot2 v3.4.2, pheatmap v1.0.12] -> stage not stated [CNVkit, GATK, MACS2 v2.2.7.1, Mutect2, NumPy v1.24.4, Scanpy v1.9.3, VEP, limma v3.5.4, pandas v1.5.3]

### Clonal-aggregative multicellularity tuned by salinity in a choanoflagellate. (Nature 2026)

- DOI: 10.1038/s41586-026-10137-y | PMCID: PMC13017551 | PMID: 41741645
- Version used: **0.7.17**
- Evidence: Qualified reads were aligned to the C. flexa reference genome using BWA-MEM (v.0.7.17) 77 .
- Full pipeline: alignment/mapping [BWA v0.7.17, DIAMOND v2.1.8, SAMtools v1.18] -> variant calling [BCFtools] -> quantification [R v4.1.1, tidyverse v2.0.0] -> normalisation [R v4.1.1, tidyverse v2.0.0] -> machine learning [BUSCO, Cellpose v2.2.3] -> visualisation [R v4.1.1, tidyverse v2.0.0] -> stage not stated [GATK v4.1.9.0, IQ-TREE, ImageJ, InterProScan v5.50]

### Transmission of MPXV from fire-footed rope squirrels to sooty mangabeys. (Nature 2026)

- DOI: 10.1038/s41586-025-10086-y | PMCID: PMC12960232 | PMID: 41673146
- Evidence: Filtered reads were then mapped to the most recent MPXV genome from TNP (GenBank accession number MN346702 ) using BWA MEM v.0.7.17-r1188 (ref.
- Full pipeline: read trimming [BWA, Flye v2.9.2, SPAdes v3.13.0] -> alignment/mapping [BWA, IQ-TREE v2.1.4b, MAFFT v7.505n, Picard v2.13.3] -> structure determination [IQ-TREE v2.1.4b] -> stage not stated [BEAST v1.10.5, Nextstrain v3.12.036, minimap2 v2.17]

### Developmental convergence and divergence in human stem cell models of autism. (Nature 2026)

- DOI: 10.1038/s41586-025-10047-5 | PMCID: PMC12999519 | PMID: 41611887
- Version used: **0.7.17**
- Evidence: The sequencing reads were mapped to the human genome (hg38) using Burrows–Wheeler Aligner (bwa-mem, v.0.7.17) 116 .
- Full pipeline: read trimming [edgeR] -> alignment/mapping [BWA v0.7.17, GATK v3.3, RSEM v1.3.0, STAR v2.5.2b] -> variant calling [GATK v3.3] -> quantification [RSEM v1.3.0, STAR v2.5.2b] -> normalisation [edgeR] -> dimensionality reduction/clustering [ComplexHeatmap, Picard, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [edgeR, metafor v4.6.0] -> stage not stated [DELLY v0.8.7, GSEA, LDSC, PLINK v1.09, R, SAMtools, Seurat, WGCNA, fgsea, scDblFinder]

### CFAP20 salvages arrested RNAPII from the path of co-directional replisomes. (Nature 2026)

- DOI: 10.1038/s41586-025-09943-7 | PMCID: PMC12935552 | PMID: 41535461
- Version used: **0.7.17**
- Evidence: For ChIP–seq, reads were aligned to the human genome 38 GCA_000001405.15_GRCh38 and Drosophila genome BDGP6 using bwa-mem tools (BWA, v.0.7.17) 66 .
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [STAR v2.7.7a, Trim Galore v0.6.5] -> alignment/mapping [BWA v0.7.17, STAR v2.7.7a, Trim Galore v0.6.5] -> quantification [AlphaFold] -> stage not stated [HOMER, SAMtools v1.11]

### Stress controls heterochromatin inheritance via histone H3 ubiquitylation. (Nature 2026)

- DOI: 10.1038/s41586-025-09899-8 | PMCID: PMC12916305 | PMID: 41501458
- Evidence: Genomic sequencing reads were quality trimmed using fastp 61 and aligned to the S. pombe ASM294v2.30 reference sequence 62 with the BWA aligner 63 using default parameters.
- Full pipeline: read trimming [BWA, STAR, fastp] -> alignment/mapping [BWA, STAR, fastp] -> stage not stated [BCFtools, MACS2, Picard, SAMtools, SnpEff]

### RNA-triggered Cas12a3 cleaves tRNA tails to execute bacterial immunity. (Nature 2026)

- DOI: 10.1038/s41586-025-09852-9 | PMCID: PMC12851939 | PMID: 41501459
- Version used: **0.7.17**
- Evidence: The poly(A) tail sequences were trimmed and the reads subsequently mapped to the reference using BWA-MEM (v.0.7.17) 71 with the minimum seed length of 19 (-k 19) and the minimum alignments score of 30 (-T 30).
- Full pipeline: read trimming [BWA v0.7.17, IQ-TREE v2.3.6, Trimmomatic v0.39] -> alignment/mapping [BLAST, BWA v0.7.17, Clustal Omega, IQ-TREE v2.3.6] -> structure determination [AlphaFold, ChimeraX v1.7, IQ-TREE v2.3.6, PHENIX v1.20.1] -> visualisation [Matplotlib, Python] -> stage not stated [SAMtools v1.9]

### An RNA splicing system that excises DNA transposons from animal mRNAs. (Nature 2026)

- DOI: 10.1038/s41586-025-09853-8 | PMCID: PMC12779559 | PMID: 41372403
- Version used: **0.7.17**
- Evidence: Reads were aligned to the C. elegans genome (WBcel235/ce11) using BWA-MEM (v.0.7.17-r1188), and variants were identified using Samtools (v.1.3.1) and bcftools (v.1.13).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [Trim Galore] -> alignment/mapping [BCFtools v1.13, BWA v0.7.17, Bowtie2 v2.5.1, Clustal Omega, GATK v4.1.9.0, SAMtools v1.3.1, STAR v2.7.9a, Snakemake, minimap2 v2.22] -> variant calling [GATK v4.1.9.0] -> normalisation [limma v3.62.2] -> differential/statistical testing [limma v3.62.2] -> visualisation [GATK v4.1.9.0] -> stage not stated [AlphaFold, Nextflow v24.04.4, Picard v2.18.7, PyMOL v2.5.8]

### Gene-drive-capable mosquitoes suppress patient-derived malaria in Tanzania. (Nature 2026)

- DOI: 10.1038/s41586-025-09685-6 | PMCID: PMC12779567 | PMID: 41372414
- Evidence: Adaptor sequences were removed from raw read sequences with Cutadapt 45 and mapped to the P. falciparum 3D7 genome (PlasmoDB v68) with BWA-MEM.
- Full pipeline: alignment/mapping [BWA, Bioconductor, Cutadapt] -> stage not stated [BCFtools, ImageJ]

### Fasting boosts breast cancer therapy efficacy via glucocorticoid activation. (Nature 2026)

- DOI: 10.1038/s41586-025-09869-0 | PMCID: PMC12823405 | PMID: 41372410
- Version used: **0.5.10**
- Evidence: In brief, all samples were aligned to reference genome Hg38/GRCh38 using Burrows-Wheeler Aligner 46 (BWA v.0.5.10).
- Full pipeline: alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, Picard] -> normalisation [Bioconductor, deepTools] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [Bioconductor, DESeq2, GSEA, R v4.0.2, clusterProfiler] -> visualisation [deepTools] -> stage not stated [GSVA, HOMER, MACS2 v2.1.2, QuPath v0.6.0]

### Somatic evolution following cancer treatment in normal tissue. (Nature 2026)

- DOI: 10.1038/s41586-025-09792-4 | PMCID: PMC13190248 | PMID: 41372419
- Version used: **0.7.17**
- Evidence: In brief, FastqToBam was used to extract unique molecular identifiers, followed by alignment using bwa-mem (v.0.7.17) 48 .
- Full pipeline: alignment/mapping [BWA v0.7.17] -> differential/statistical testing [R, lme4] -> stage not stated [Nextflow, SAMtools v1.19.2]

### Decay of driver mutations shapes the landscape of intestinal transformation. (Nature 2026)

- DOI: 10.1038/s41586-025-09762-w | PMCID: PMC12804087 | PMID: 41339549
- Version used: **0.7.17**
- Evidence: Adaptor clipping and PCR duplicate marking were performed using biobambam2 (v.2.0.79) 77 and sequence reads were aligned to GRCm38 using BWA-MEM (v.0.7.17) 78 .
- Full pipeline: alignment/mapping [BWA v0.7.17, R] -> quantification [QuPath] -> visualisation [ggplot2] -> stage not stated [VEP]

### Whole-genome landscapes of 1,364 breast cancers. (Nature 2026)

- DOI: 10.1038/s41586-025-09812-3 | PMCID: PMC12851938 | PMID: 41339552
- Version used: **0.7.17**
- Evidence: WGS data were aligned to the GRCh38 human reference genome using bwa-mem (v.0.7.17-r1188) 59 .
- Full pipeline: alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools v1.9] -> stage not stated [DELLY v0.7.6, GATK v4.0, GSEA, Mutect2, R, VEP]

### Genetic elements promote retention of extrachromosomal DNA in cancer cells. (Nature 2026)

- DOI: 10.1038/s41586-025-09764-8 | PMCID: PMC12727538 | PMID: 41261124
- Evidence: Reads were aligned to the hg19 genome using BWA MEM (v.0.7.17-r1188) 65 and PCR duplicates were removed using MarkDuplicates in Picard (v.2.25.3).
- Full pipeline: quality control [FastQC] -> read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA, FastQC, Picard v2.25.3, SAMtools, minimap2 v2.17] -> quantification [BEDTools v2.30.0, CellProfiler v4.2.7, ImageJ] -> differential/statistical testing [R v3.6.1] -> stage not stated [deepTools v3.5.1]

### A pangenome and pantranscriptome of hexaploid oat. (Nature 2026)

- DOI: 10.1038/s41586-025-09676-7 | PMCID: PMC12727504 | PMID: 41162711
- Evidence: All of the GBS sequencing data from the G.O.D. lines were aligned to a single reference genome (GS7) using BWA followed by sorting using NovoSort and indexing with SAMtools.
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BCFtools, BWA, Cutadapt, DESeq2, R, SAMtools, kallisto, minimap2] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2, R, clusterProfiler] -> visualisation [ggplot2] -> stage not stated [BUSCO, OrthoFinder v2.5.5, PLINK, hifiasm v0.14.1]

### Response of an Afro-Palearctic bird migrant to glaciation cycles. (PNAS 2021)

- DOI: 10.1073/pnas.2023836118 | PMCID: PMC8719893 | PMID: 34949638
- Version used: **0.7.12**
- Evidence: The reads from the 14 resequenced individuals were mapped to the reference genome with Burrows-Wheeler Aligner BWA-MEM (version 0.7.12-r1039).
- Full pipeline: alignment/mapping [BWA v0.7.12] -> registration [GATK, Picard] -> differential/statistical testing [R v3.4.2] -> stage not stated [ANGSD, BEDTools, BUSCO, RepeatMasker]

### Invasion genomics uncover contrasting scenarios of genetic diversity in a widespread marine invader. (PNAS 2021)

- DOI: 10.1073/pnas.2116211118 | PMCID: PMC8713979 | PMID: 34911766
- Version used: **0.7.15**
- Evidence: After removing adapter sequences and low quality bases, paired and unpaired reads were aligned to the M. leidyi reference genome ( 28 ) using the mem algorithm in BWA v0.7.15 ( 51 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7.15, Trimmomatic v0.36] -> alignment/mapping [BWA v0.7.15, Picard v2.6.0] -> variant calling [BCFtools v1.9] -> stage not stated [PLINK v1.90b, VCFtools v0.1.14]

### Parallel genomic responses to historical climate change and high elevation in East Asian songbirds. (PNAS 2021)

- DOI: 10.1073/pnas.2023918118 | PMCID: PMC8685689 | PMID: 34873033
- Version used: **0.7.15**
- Evidence: We aligned reads to the P. major reference genome (Assembly: GCA_001522545.2) ( 33 ) using BWA version 0.7.15 ( 61 ) with default parameters.
- Full pipeline: alignment/mapping [BWA v0.7.15, MUSCLE v3.8.31] -> variant calling [SAMtools v1.3.1] -> registration [GATK] -> differential/statistical testing [Python] -> stage not stated [RAxML v8.2.10, SnpEff v4.3, VCFtools v0.1.13]

### Genomic basis of fishing-associated selection varies with population density. (PNAS 2021)

- DOI: 10.1073/pnas.2020833118 | PMCID: PMC8713780 | PMID: 34903645
- Version used: **0.7.17**
- Evidence: The reads were aligned and mapped to the zebrafish reference genome (GRCz11) using the mem algorithm of Burrows–Wheeler Aligner software (BWA v0.7.17) ( 53 ).
- Full pipeline: read trimming [Cutadapt v1.16, Trimmomatic v0.36] -> alignment/mapping [ANGSD, BWA v0.7.17] -> differential/statistical testing [ggplot2] -> stage not stated [Picard v2.18.14, R v3.5, SnpEff v4.4]

### Molecular characterization of Barrett's esophagus at single-cell resolution. (PNAS 2021)

- DOI: 10.1073/pnas.2113061118 | PMCID: PMC8617519 | PMID: 34795059
- Version used: **0.7.5**
- Evidence: WGS data were mapped against human reference genome GRCh37 by using the BWA (v0.7.5) mapping tool ( 57 ) with settings 'bwa mem -c 100 -M.' Sequence reads were marked for duplicates by using Sambamba (v0.6.8) and realigned per donor by using Genome Analysis Toolkit (GATK) IndelRealigner (v3.8.1) Raw variants were multisample-called by using the GATK HaplotypeCaller (v3.8-0) ( 58 ) and GATK-Queue (...
- Full pipeline: alignment/mapping [BWA v0.7.5, GATK] -> variant calling [BWA v0.7.5, GATK] -> registration [BWA v0.7.5, GATK] -> dimensionality reduction/clustering [pheatmap] -> visualisation [R]

### Linked supergenes underlie split sex ratio and social organization in an ant. (PNAS 2021)

- DOI: 10.1073/pnas.2101427118 | PMCID: PMC8609651 | PMID: 34772805
- Version used: **0.7.17**
- Evidence: We merged overlapping paired-end reads with PEAR version 0.9.10 ( 69 ), aligned the reads to the F. selysi reference genome ( 29 ) using BWA-MEM version 0.7.17 ( 70 ), and removed PCR duplicates with Samtools version 1.8 ( 71 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.8] -> variant calling [VCFtools v0.1.13] -> visualisation [R] -> stage not stated [GEMMA v0.94]

### Assessing the origins of the European Plagues following the Black Death: A synthesis of genomic, historical, and ecological information. (PNAS 2021)

- DOI: 10.1073/pnas.2101940118 | PMCID: PMC8433512 | PMID: 34465619
- Evidence: Subsequently, the filtered reads were mapped against the CO92 assembly with BWA mem model (v0.7.17) ( 37 ), and the aligned reads were extracted from bam files using SAMtools (v1.9) ( 38 ) view command (-bF 4); then, different runs of the same sample were merged using SAMtools merge command.
- Full pipeline: read trimming [BWA, SAMtools v1.9, Trimmomatic v0.38] -> alignment/mapping [BWA, Picard, SAMtools v1.9, phytools v0.7] -> variant calling [GATK v3.8] -> stage not stated [IQ-TREE v1.6.5, R v3.6.1, RAxML v8.2.11, ggplot2]

### Modern Siberian dog ancestry was shaped by several thousand years of Eurasian-wide trade and human dispersal. (PNAS 2021)

- DOI: 10.1073/pnas.2100338118 | PMCID: PMC8488619 | PMID: 34544854
- Evidence: Each sample was aligned to the CanFam3.1 reference dog genome ( 27 ) using the Burrows-Wheeler Alignment Backtrack algorithm (BWA aln) ( 28 , 29 ), subsequently pseudohaploid calling was performed on the samples and a panel of publicly available canid samples with ANGSD ( 30 ) to be used for downstream analyses.
- Full pipeline: alignment/mapping [ANGSD, BWA] -> stage not stated [R]

### Transposition and duplication of MADS-domain transcription factor genes in annual and perennial <i>Arabis</i> species modulates flowering. (PNAS 2021)

- DOI: 10.1073/pnas.2109204118 | PMCID: PMC8488671 | PMID: 34548402
- Evidence: The cleaned reads were mapped to the pooled genomes of A. alpina (Pajares) V5.1 ( 16 ) and A. montbretiana V3.1 using BWA ( 54 ) and the number of read pairs that mapped to each annotated gene was determined.
- Full pipeline: read trimming [MUSCLE] -> alignment/mapping [BWA, MUSCLE] -> normalisation [R] -> stage not stated [DESeq2]

### High frequency of an otherwise rare phenotype in a small and isolated tiger population. (PNAS 2021)

- DOI: 10.1073/pnas.2025273118 | PMCID: PMC8488692 | PMID: 34518374
- Evidence: We aligned the resulting reads to the annotated domestic cat genome (felCat8.0 assembly; RefSeq accession: GCF_000181335.2) using BWA-MEM ( 98 ) with default settings and sorted the reads using Sam-tools ( 99 ).
- Full pipeline: read trimming [Trim Galore] -> alignment/mapping [BCFtools, BWA] -> variant calling [GATK, VCFtools] -> stage not stated [Picard]

### <i>ENHANCED GRAVITROPISM 2</i> encodes a STERILE ALPHA MOTIF-containing protein that controls root growth angle in barley and wheat. (PNAS 2021)

- DOI: 10.1073/pnas.2101526118 | PMCID: PMC8536364 | PMID: 34446550
- Version used: **7.12**
- Evidence: Morex reference genome ( 26 ) with BWA v.7.12 ( 54 ) and variants in the genomic space were called with SAMtools v.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v7.12, Clustal Omega, DESeq2, HTSeq, R, SAMtools v1.3, STAR] -> variant calling [STAR] -> normalisation [DESeq2, HTSeq, R] -> dimensionality reduction/clustering [DESeq2, HTSeq, R] -> stage not stated [ImageJ]

### SAMD9L autoinflammatory or ataxia pancytopenia disease mutations activate cell-autonomous translational repression. (PNAS 2021)

- DOI: 10.1073/pnas.2110190118 | PMCID: PMC8403910 | PMID: 34417303
- Version used: **0.7.10**
- Evidence: Raw reads were aligned to the hs37d5 reference using BWA-MEM v0.7.10-r789 and sorted and duplicate-marked with Novosort v1.03.01 (Novocraft Technologies).
- Full pipeline: alignment/mapping [BWA v0.7.10] -> variant calling [GATK] -> registration [GATK] -> stage not stated [VEP]

### Global range expansion history of pepper (<i>Capsicum</i> spp.) revealed by over 10,000 genebank accessions. (PNAS 2021)

- DOI: 10.1073/pnas.2104315118 | PMCID: PMC8403938 | PMID: 34400501
- Version used: **0.7**
- Evidence: The 10,280 million trimmed reads generated from sequencing of 10,262 samples (germplasm collection plus CM334 control accessions) ( SI Appendix , Table S8 ) were then aligned to reference genome sequence C. annuum CM334 version 1.6 available at http://peppergenome.snu.ac.kr ( 39 ) using BWA-MEM version 0.7 ( 40 ) and converted to binary alignment map format using SAMtools ( 41 ).
- Full pipeline: quality control [FastQC] -> read trimming [BWA v0.7, Cutadapt, SAMtools] -> alignment/mapping [BCFtools v1.9, BWA v0.7, SAMtools] -> variant calling [BCFtools v1.9] -> differential/statistical testing [GEMMA v0.96] -> stage not stated [ADMIXTURE, IQ-TREE, R, SnpEff v3.1, VCFtools v0.1.17, data.table, ggplot2, pheatmap]

### Multiple migrations to the Philippines during the last 50,000 years. (PNAS 2021)

- DOI: 10.1073/pnas.2026132118 | PMCID: PMC8020671 | PMID: 33753512
- Evidence: For processing of aDNA data, paired-end reads were merged, and their adapters were trimmed and subsequently mapped to the human reference genome using BWA ( 53 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [PLINK v1.9] -> visualisation [ADMIXTURE v1.3]

### A versatile platform for locus-scale genome rewriting and verification. (PNAS 2021)

- DOI: 10.1073/pnas.2023952118 | PMCID: PMC7958457 | PMID: 33649239
- Version used: **0.7.17**
- Evidence: Sequencing reads were aligned using BWA v0.7.17 ( 56 ) to a reference genome (GRCh38/hg38 or GRCm38/mm10), including unscaffolded contigs and alternate references, as well as independently to custom references for relevant vectors.
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17] -> variant calling [BCFtools v1.9]

### Accurate SNV detection in single cells by transposon-based whole-genome amplification of complementary strands. (PNAS 2021)

- DOI: 10.1073/pnas.2013106118 | PMCID: PMC7923680 | PMID: 33593904
- Version used: **0.7.17**
- Evidence: We aligned preprocessed single-cell reads with two mappers, BWA-MEM v0.7.17 ( 38 ) and Minimap2 v2.12 ( 39 ), both with their default settings for short reads.
- Full pipeline: alignment/mapping [BWA v0.7.17, minimap2 v2.12] -> stage not stated [BEDTools]

### Genome-wide detection of cytosine methylation by single molecule real-time sequencing. (PNAS 2021)

- DOI: 10.1073/pnas.2019768118 | PMCID: PMC7865158 | PMID: 33495335
- Evidence: Sequencing reads were aligned to the human reference genome (hg19) using BWA aligner ( 33 ).
- Full pipeline: alignment/mapping [BWA] -> machine learning [Keras]

### The genomics of ecological flexibility, large brains, and long lives in capuchin monkeys revealed with fecalFACS. (PNAS 2021)

- DOI: 10.1073/pnas.2010632118 | PMCID: PMC7896301 | PMID: 33574059
- Evidence: Median mapping rates reached 93% (range: 55 to 98%) with BWA-MEM and 82% (range: 11 to 95%) with the more stringent BBsplit settings ( Fig.
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK] -> stage not stated [BCFtools, Picard, SAMtools, SnpEff, VCFtools]

### Microbial dynamics of elevated carbon flux in the open ocean's abyss. (PNAS 2021)

- DOI: 10.1073/pnas.2018269118 | PMCID: PMC7848738 | PMID: 33479184
- Version used: **0.7.15**
- Evidence: The taxonomic affiliations of the SSU rRNA sequences were assessed by homology to the SILVA SSU rRNA NR99 database release 132 ( 65 ) using BWA 0.7.15-r1140 ( 66 ) with matches limited to at least 97% identity over at least 70 bases.
- Full pipeline: read trimming [SPAdes] -> alignment/mapping [SPAdes] -> structure determination [SPAdes, ggplot2, pheatmap] -> visualisation [Cytoscape, ggplot2, pheatmap] -> stage not stated [BWA v0.7.15, R, WGCNA]

### The human pathobiont <i>Malassezia furfur</i> secreted protease Mfsap1 regulates cell dispersal and exacerbates skin inflammation. (PNAS 2022)

- DOI: 10.1073/pnas.2212533119 | PMCID: PMC9894114 | PMID: 36442106
- Evidence: In general, the analysis workflow begins with extracting UMI sequences from raw reads, followed by mapping of the reads onto a custom BWA amplicon reference consisting of the collection of targeted amplicon FASTA sequences.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R v4.0.0]

### Turnover of mammal sex chromosomes in the <i>Sry</i>-deficient Amami spiny rat is due to male-specific upregulation of <i>Sox9</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2211574119 | PMCID: PMC9894122 | PMID: 36442104
- Version used: **0.7.17**
- Evidence: In the pipeline, raw reads were mapped to the whole draft genome using BWA (v0.7.17) ( 33 ).
- Full pipeline: alignment/mapping [BWA v0.7.17]

### Identification and functional validation of super-enhancers in &lt;i&gt;Arabidopsis thaliana&lt;/i&gt;. (PNAS 2022)

- DOI: 10.1073/pnas.2215328119 | PMCID: PMC9860255 | PMID: 36409894
- Evidence: DNase-seq reads were mapped to A. thaliana TAIR10 genome using BWA aln ( 71 ) with default parameters and then convert to BAM format by SAMtools ( 72 ).
- Full pipeline: alignment/mapping [BWA, SAMtools, minimap2] -> stage not stated [BCFtools, BEDTools, R v4.0.4]

### SMC protein RecN drives RecA filament translocation for in vivo homology search. (PNAS 2022)

- DOI: 10.1073/pnas.2209304119 | PMCID: PMC9674259 | PMID: 36346847
- Evidence: First, indexing with the reference genome (4.01 Mbp) (National Center for Biotechnology Information reference sequence: NC-011916.1) was done using BWA ( 68 ).
- Full pipeline: alignment/mapping [BWA] -> quantification [ImageJ]

### Stage-specific transposon activity in the life cycle of the fairy-ring mushroom <i>Marasmius oreades</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2208575119 | PMCID: PMC9674265 | PMID: 36343254
- Evidence: From the eight protoclones, reads were mapped using BWA mem ( 76 ) to the Maror2 reference genome [( 49 ); National Center for Biotechynology (NCBI) accession no.
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BUSCO v5.2.2, BWA, IQ-TREE v1.6.8, MAFFT v7.407, minimap2] -> variant calling [Canu, R v3.5] -> structure determination [Canu] -> stage not stated [BEDTools v2.29.0, BLAST, GATK, NanoPlot, RepeatMasker v4.0.7, SAMtools v1.7, VCFtools]

### Omics analyses of a somatic <i>Trp53<sup>R245W/+</sup></i> breast cancer model identify cooperating driver events activating PI3K/AKT/mTOR signaling. (PNAS 2022)

- DOI: 10.1073/pnas.2210618119 | PMCID: PMC9659373 | PMID: 36322759
- Evidence: After quality check, the reads were aligned to the mouse reference genome (GRCm38 from the Wellcome Sanger Institute) using BWA ( 64 ).
- Full pipeline: quality control [BWA, FastQC, TopHat] -> read trimming [Bioconductor, edgeR] -> alignment/mapping [BWA, GATK, SAMtools, TopHat] -> quantification [Bioconductor, ImageJ, edgeR] -> normalisation [Bioconductor, ImageJ, edgeR] -> registration [GATK] -> differential/statistical testing [SAMtools] -> stage not stated [ANNOVAR, GSEA, Picard, limma]

### Two intrinsic timing mechanisms set start and end times for dendritic arborization of a nociceptive neuron. (PNAS 2022)

- DOI: 10.1073/pnas.2210053119 | PMCID: PMC9659368 | PMID: 36322763
- Evidence: After an initial quality check, the reads were mapped to WS220 using BWA ( 67 ) and filtered using SAMtools ( 68 ).
- Full pipeline: quality control [BWA, SAMtools] -> alignment/mapping [BWA, SAMtools] -> quantification [ImageJ] -> visualisation [MACS2]

### Spatial scale of tuberculosis transmission in Lima, Peru. (PNAS 2022)

- DOI: 10.1073/pnas.2207022119 | PMCID: PMC9659349 | PMID: 36322726
- Evidence: We mapped the paired-end raw sequencing data to the H37Rv reference genome using the BWA-MEM (Burroughs Wheeler Aligner-Maximal Exact Match) algorithm ( 11 ) and used SAMtools and Pilon to identify the single-nucleotide polymorphisms (SNPs) and the insertions and deletions using a coverage-based approach ( 12 , 13 ).
- Full pipeline: alignment/mapping [BWA, Pilon, SAMtools]

### Population dynamics of Baltic herring since the Viking Age revealed by ancient DNA and genomics. (PNAS 2022)

- DOI: 10.1073/pnas.2208703119 | PMCID: PMC9659336 | PMID: 36282902
- Evidence: Modern sequences were aligned using bwa-mem and ancient sequences were aligned using bwa-aln. mapDamage2.0 ( 98 ) plots for postmortem deamination were assessed to validate the ancient samples ( SI Appendix , Fig.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [GATK, IQ-TREE v1.6.12, VCFtools v0.1.16]

### Marine viral particles reveal an expansive repertoire of phage-parasitizing mobile elements. (PNAS 2022)

- DOI: 10.1073/pnas.2212722119 | PMCID: PMC9618062 | PMID: 36256808
- Evidence: Raw reads were mapped against contigs using Burrows-Wheeler Aligner's BWA-MEM algorithm ( 63 ) and used to calculate base by base coverage of contigs at VEIME hit locations.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [HMMER, IQ-TREE, Medaka, R v9.4, eggNOG, minimap2]

### The diverse genetic origins of a Classical period Greek army. (PNAS 2022)

- DOI: 10.1073/pnas.2205272119 | PMCID: PMC9564095 | PMID: 36191217
- Version used: **0.6.1**
- Evidence: Using the samse command of BWA (version 0.6.1) ( 113 ), we mapped the resulting sequences to the human reference genome sequence hg19 [GRCh37], and the sequences resulting from mtDNA capture to the mitochondrial reference genome RSRS ( 114 ).
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.6.1] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [PLINK]

### Genetic adaptation of skin pigmentation in highland Tibetans. (PNAS 2022)

- DOI: 10.1073/pnas.2200421119 | PMCID: PMC9552612 | PMID: 36161951
- Evidence: First, low-quality regions of the end of the sequence were removed using the BWA algorithm, and the threshold was 30; then the joint sequence and the sequence containing the ambiguous base N were trimmed from the raw data.
- Full pipeline: read trimming [BWA] -> alignment/mapping [HISAT2 v2.0.5, featureCounts] -> quantification [featureCounts] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape v3.8.2] -> stage not stated [GEMMA, PLINK v1.07]

### Functional genomics analysis reveals the evolutionary adaptation and demographic history of pygmy lorises. (PNAS 2022)

- DOI: 10.1073/pnas.2123030119 | PMCID: PMC9546566 | PMID: 36161902
- Version used: **0.7.12**
- Evidence: All clean short reads were aligned against the assembled pygmy loris reference genome using BWA-MEM v0.7.12 ( 59 ).
- Full pipeline: alignment/mapping [BUSCO, BWA v0.7.12, Clustal Omega v1.2.0, Cufflinks v2.2.1, HISAT2 v2.0.3, MUSCLE v3.7, SAMtools v1.3.1] -> quantification [Cufflinks v2.2.1, HISAT2 v2.0.3] -> registration [GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [Canu, PLINK v1.9, Pilon v1.22, RAxML, RepeatMasker v4.0.6, VCFtools v0.1.12]

### Evolutionary divergence of duplicated genomes in newly described allotetraploid cottons. (PNAS 2022)

- DOI: 10.1073/pnas.2208496119 | PMCID: PMC9522333 | PMID: 36122204
- Version used: **0.7.8**
- Evidence: The filtered Hi-C reads were aligned against the contig assemblies with BWA (v0.7.8) ( 75 ).
- Full pipeline: alignment/mapping [BWA v0.7.8, HTSeq v0.6.1, MUSCLE v3.8.31, TopHat v2.0.13] -> dimensionality reduction/clustering [R] -> stage not stated [ANNOVAR, BEDTools, BUSCO v3.0.2, HMMER, InterProScan, OrthoFinder v2.2.7, Pilon v1.18, RAxML v8.0.19, RepeatMasker v3.3.0]

### Experimental evolution reveals the synergistic genomic mechanisms of adaptation to ocean warming and acidification in a marine copepod. (PNAS 2022)

- DOI: 10.1073/pnas.2201521119 | PMCID: PMC9499500 | PMID: 36095205
- Evidence: 0.36 ( 73 ) and mapped to the A. tonsa reference genome ( 52 ) with BWA-MEM ( 74 ).
- Full pipeline: quality control [Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [R] -> differential/statistical testing [VarScan] -> stage not stated [MrBayes]

### Heterozygous LRP1 deficiency causes developmental dysplasia of the hip by impairing triradiate chondrocytes differentiation due to inhibition of autophagy. (PNAS 2022)

- DOI: 10.1073/pnas.2203557119 | PMCID: PMC9477389 | PMID: 36067312
- Version used: **0.59**
- Evidence: Burrows–WheelerAligner (BWA version 0.59) ( 33 ) was used to align sequence reads to the human genome reference (build 37).
- Full pipeline: alignment/mapping [BWA v0.59] -> stage not stated [ANNOVAR, GATK, ImageJ]

### Loss-of-function mutation survey revealed that genes with background-dependent fitness are rare and functionally related in yeast. (PNAS 2022)

- DOI: 10.1073/pnas.2204206119 | PMCID: PMC9478683 | PMID: 36067306
- Evidence: The cleaned reads were mapped specifically for each isolate by imputing the corresponding background-specific single-nucleotide polymorphisms (SNPs) into the reference genome ( 26 ) with BWA ( 40 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA] -> stage not stated [R]

### Long noncoding RNA &lt;i&gt;CHROMR&lt;/i&gt; regulates antiviral immunity in humans. (PNAS 2022)

- DOI: 10.1073/pnas.2210321119 | PMCID: PMC9477407 | PMID: 36001732
- Evidence: Reads were trimmed with Trimmomatic ( 51 ) and mapped to hg19 with BWA ( 52 ).
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA, STAR, Trimmomatic, featureCounts] -> quantification [STAR, featureCounts] -> dimensionality reduction/clustering [Cytoscape] -> differential/statistical testing [Bioconductor, DESeq2] -> stage not stated [Enrichr, HOMER, MACS2, R]

### A single introduction of wild rabbits triggered the biological invasion of Australia. (PNAS 2022)

- DOI: 10.1073/pnas.2122734119 | PMCID: PMC9436340 | PMID: 35994668
- Version used: **0.7.10**
- Evidence: Collapsed and paired-end reads were aligned to the rabbit reference genome OryCun2.0 using bwa-mem (version 0.7.10) and default parameters.
- Full pipeline: quality control [FastQC, Trimmomatic v0.32] -> read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA v0.7.10, SAMtools v1.3] -> variant calling [ANGSD v0.935] -> registration [GATK v3.3.0] -> stage not stated [Picard, R, VCFtools, ggplot2]

### The amino acid sensor GCN2 controls red blood cell clearance and iron metabolism through regulation of liver macrophages. (PNAS 2022)

- DOI: 10.1073/pnas.2121251119 | PMCID: PMC9436309 | PMID: 35994670
- Version used: **0.7.12**
- Evidence: Trimmed reads were then aligned to the mouse reference genome mm10 using BWA v0.7.12 ( 69 ).
- Full pipeline: read trimming [BWA v0.7.12] -> alignment/mapping [BWA v0.7.12] -> differential/statistical testing [MACS2] -> stage not stated [HOMER, R, Seurat v3.0.1]

### Radiation and hybridization underpin the spread of the fire ant social supergene. (PNAS 2022)

- DOI: 10.1073/pnas.2201040119 | PMCID: PMC9407637 | PMID: 35969752
- Version used: **0.7.17**
- Evidence: We mapped the Illumina paired-end whole-genome sequences of the 185 individuals on the S. invicta SB reference genome GCA_009650705 ( 22 ) using bwa-mem (v.0.7.17) ( 69 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, MAFFT v7.475, R, ggplot2] -> variant calling [BCFtools, freebayes v1.3.2] -> normalisation [VCFtools v0.1.16] -> visualisation [ape (R)] -> stage not stated [IQ-TREE, SAMtools, phytools]

### Root angle is controlled by &lt;i&gt;EGT1&lt;/i&gt; in cereal crops employing an antigravitropic mechanism. (PNAS 2022)

- DOI: 10.1073/pnas.2201350119 | PMCID: PMC9351459 | PMID: 35881796
- Version used: **7.12**
- Evidence: Reads were aligned to Morex v1 reference sequence ( 44 ) with BWA v7.12 ( 45 ) and variants in the genomic space were called with SAMtools v1.3 ( 46 ), filtering for a minimum read depth of 5×, PHRED quality > 40.
- Full pipeline: alignment/mapping [BWA v7.12, Cufflinks, HISAT2, HTSeq, SAMtools v1.3] -> stage not stated [AlphaFold, DESeq2, ImageJ, R]

### Uncovering the enigmatic evolution of bears in greater depth: The hybrid origin of the Asiatic black bear. (PNAS 2022)

- DOI: 10.1073/pnas.2120307119 | PMCID: PMC9351369 | PMID: 35858381
- Version used: **0.78**
- Evidence: We used BWA-MEM version 0.78 ( 44 ) to align the trimmed paired-end reads from all the bears to the available de novo assembled polar bear reference genome (UrsMar_1.0) ( 41 ).
- Full pipeline: read trimming [BWA v0.78] -> alignment/mapping [BWA v0.78, MAFFT v7.486, SAMtools v0.1.18] -> registration [GATK v3.7] -> structure determination [RAxML v8.2.11] -> stage not stated [Picard v1.87, VCFtools v0.1.14]

### A genetically linked pair of NLR immune receptors shows contrasting patterns of evolution. (PNAS 2022)

- DOI: 10.1073/pnas.2116896119 | PMCID: PMC9271155 | PMID: 35771942
- Evidence: One round of consensus correction was performed using BWA ( 75 ) and HyPo ( https://github.com/kensung-lab/hypo ) on Illumina short reads for the accessions.
- Full pipeline: stage not stated [BWA, IQ-TREE v2.0.3, ImageJ, Medaka]

### An enhancer of &lt;i&gt;Agouti&lt;/i&gt; contributes to parallel evolution of cryptically colored beach mice. (PNAS 2022)

- DOI: 10.1073/pnas.2202862119 | PMCID: PMC9271204 | PMID: 35776547
- Evidence: We mapped sequencing reads to the P. polionotus subgriseus reference genome (see above) using bwa-mem ( 76 ), with –p to indicate interleaved paired-end fastq input and –M to mark short split hits as secondary for compatibility with Picard.
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA, GATK v3.8] -> variant calling [GATK v3.8] -> stage not stated [ANGSD v0.929, AUGUSTUS v3.3.2, BCFtools v1.11, BEAST v2.6.0, BUSCO v3.0.2, HMMER v3.1b, R, RAxML v8.2.12, RepeatMasker, SAMtools v1.10, VCFtools v0.1.15]

### The evening complex integrates photoperiod signals to control flowering in rice. (PNAS 2022)

- DOI: 10.1073/pnas.2122582119 | PMCID: PMC9245669 | PMID: 35733265
- Evidence: For processing ChIP-seq fastq files, BWA was used to map raw reads to rice genome IRGSP-1.0.
- Full pipeline: alignment/mapping [HISAT2] -> quantification [StringTie, deepTools] -> normalisation [deepTools] -> stage not stated [BEDTools v2.30.0, BWA, MACS2, R, SAMtools v1.11]

### Expansion of a retrovirus lineage in the koala genome. (PNAS 2022)

- DOI: 10.1073/pnas.2201844119 | PMCID: PMC9231498 | PMID: 35696585
- Evidence: Sequencing reads were mapped to the koala reference using BWA-MEM ( 31 ), pooled per individual with SAMtools 1.12 ( 32 ), and duplicate reads marked by Picard 2.23.4 (broadinstitute.github.io/picard/).
- Full pipeline: alignment/mapping [BWA, Picard v2.23.4, RepeatMasker, SAMtools v1.12] -> stage not stated [DELLY, R]

### Repeated translocation of a supergene underlying rapid sex chromosome turnover in <i>Takifugu</i> pufferfish. (PNAS 2022)

- DOI: 10.1073/pnas.2121469119 | PMCID: PMC9191631 | PMID: 35658077
- Evidence: We then mapped the resequencing data of 10 males and 8 females ( SI Appendix , Table S5 ) onto the genome assembly of the T. niphobles YY male using the Burrows-Wheeler Aligner Maximal Exact Match (BWA-MEM) algorithm ( 76 ) ( SI Appendix , Methods ).
- Full pipeline: alignment/mapping [BWA, minimap2] -> stage not stated [BUSCO, RAxML v0.8]

### An ancient founder mutation located between <i>ROBO1</i> and <i>ROBO2</i> is responsible for increased microtia risk in Amerindigenous populations. (PNAS 2022)

- DOI: 10.1073/pnas.2203928119 | PMCID: PMC9173816 | PMID: 35584116
- Evidence: Reads were aligned to the hg38 reference genome using the Burrows–Wheeler Aligner (BWA-MEM) and processed in accordance with Genome Analysis Toolkit (GATK; Broad Institute) workflow best practices ( 42 ).
- Full pipeline: alignment/mapping [BWA, GATK, Picard] -> variant calling [PLINK v1.9, Picard] -> quantification [DESeq2] -> differential/statistical testing [DESeq2, PLINK v1.9] -> stage not stated [ADMIXTURE v1.3, HOMER, R, SnpEff]

### Targeted base editing in the mitochondrial genome of <i>Arabidopsis thaliana</i>. (PNAS 2022)

- DOI: 10.1073/pnas.2121177119 | PMCID: PMC9171795 | PMID: 35561225
- Version used: **0.7.12**
- Evidence: Paired-end reads of each strain were mapped to the reference sequences (mitochondrial genome BK010421.1 and chloroplast genome AP000423.1 ) using BWA (v 0.7.12) in single-ended mode ( 45 ).
- Full pipeline: alignment/mapping [BWA v0.7.12] -> stage not stated [BCFtools, SAMtools]

### Gene evolutionary trajectories in <i>Mycobacterium tuberculosis</i> reveal temporal signs of selection. (PNAS 2022)

- DOI: 10.1073/pnas.2113600119 | PMCID: PMC9173582 | PMID: 35452305
- Evidence: Briefly, FASTQ files were trimmed to remove low-quality reads using fastp ( 64 ) (version 0.12.5, arguments –cut_by_quality3, –cut_window_size = 10, –cut_mean_quality = 20, –length_required = 50, –correction) and aligned to the most likely inferred ancestor of the MTBC ( 24 ) using the BWA-MEM algorithm ( 65 ).
- Full pipeline: read trimming [BWA, fastp] -> alignment/mapping [BWA, Picard, fastp] -> variant calling [GATK, SAMtools, VarScan] -> stage not stated [GSEA, IQ-TREE, SnpEff v4.2]

### Ancient DNA gives new insights into a Norman Neolithic monumental cemetery dedicated to male elites. (PNAS 2022)

- DOI: 10.1073/pnas.2120786119 | PMCID: PMC9170172 | PMID: 35446690
- Version used: **0.7.12**
- Evidence: This included clipping adaptors with Adaptor Removal ( 70 ), mapping with BWA v0.7.12 ( 71 ) against the Human Reference Genome hs37d5, and removing duplicate reads with the same orientation and start and end positions.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.7.12] -> stage not stated [SAMtools v1.3.1]

### A generalist-specialist trade-off between switchgrass cytotypes impacts climate adaptation and geographic range. (PNAS 2022)

- DOI: 10.1073/pnas.2118879119 | PMCID: PMC9169841 | PMID: 35377798
- Evidence: Reads were mapped to the P. virgatum v5 assembly ( 18 ) by using bwa-mem ( 64 ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [ADMIXTURE, PLINK v1.9, SAMtools, VCFtools] -> registration [GATK v3.0, Picard] -> stage not stated [R]

### Layered evolution of gene expression in "superfast" muscles for courtship. (PNAS 2022)

- DOI: 10.1073/pnas.2119671119 | PMCID: PMC9168950 | PMID: 35363565
- Evidence: The unmapped read pairs from STAR were then aligned using BWA - mem (v0.7.17-r1188) ( 45 ) using a slightly relaxed mismatch parameter (-B 2), split hits as secondary (-M), and all other command flags default.
- Full pipeline: alignment/mapping [BCFtools, BWA, RAxML, STAR v2.7.3a] -> differential/statistical testing [limma] -> stage not stated [featureCounts v2.0.1]

### The virota and its transkingdom interactions in the healthy infant gut. (PNAS 2022)

- DOI: 10.1073/pnas.2114619119 | PMCID: PMC9060457 | PMID: 35320047
- Evidence: To obtain relative abundances per sample, trimmed reads were mapped to a subset of the NR dataset using BWA-MEM ( 75 ).
- Full pipeline: quality control [R] -> read trimming [BWA, MAFFT, Trimmomatic] -> alignment/mapping [BWA, Kraken2, MAFFT] -> quantification [BWA] -> differential/statistical testing [IQ-TREE, ggplot2, phyloseq] -> visualisation [ggplot2, phyloseq] -> stage not stated [BLAST, DADA2, InterProScan, eggNOG]

### <i>TIC236</i> gain-of-function mutations unveil the link between plastid division and plastid protein import. (PNAS 2022)

- DOI: 10.1073/pnas.2123353119 | PMCID: PMC8931380 | PMID: 35275795
- Evidence: Clean reads were mapped to the TAIR10 genome in BWA-MEM ( 35 ) with default parameters.
- Full pipeline: read trimming [Cutadapt v1.3, R, edgeR] -> alignment/mapping [BWA, TopHat, VCFtools] -> normalisation [R, edgeR] -> differential/statistical testing [R, edgeR] -> stage not stated [SAMtools]

### Purging of deleterious burden in the endangered Iberian lynx. (PNAS 2022)

- DOI: 10.1073/pnas.2110614119 | PMCID: PMC8931242 | PMID: 35238662
- Evidence: Trimmed reads were mapped to the Iberian lynx reference genome using BWA-MEM ( 96 ) with default parameters.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> variant calling [GATK v3.7] -> stage not stated [SnpEff v4.3i]

### Conservation of chromatin conformation in carnivores. (PNAS 2022)

- DOI: 10.1073/pnas.2120555119 | PMCID: PMC8892538 | PMID: 35217621
- Evidence: The pipeline uses BWA ( 40 ) to map reads and remove read duplicates.
- Full pipeline: stage not stated [BWA]

### Ancient DNA at the edge of the world: Continental immigration and the persistence of Neolithic male lineages in Bronze Age Orkney. (PNAS 2022)

- DOI: 10.1073/pnas.2108001119 | PMCID: PMC8872714 | PMID: 35131896
- Evidence: We mapped reads to the human reference genome (UCSC [University of California Santa Cruz] hg19) and the human mitochondrial reference genome (the revised Cambridge reference sequence or rCRS, NC_012920.1 ) ( 57 ) using BWA aln (Burrows–Wheeler alignment tool) (version 0.7.12-r1039) ( 58 ) and filtered for mapping quality ( 56 , 59 ).
- Full pipeline: alignment/mapping [BWA] -> variant calling [GATK v3.8] -> quantification [ADMIXTURE v1.3] -> registration [GATK v3.8] -> differential/statistical testing [ADMIXTURE v1.3]

### Epistatic genetic interactions govern morphogenesis during sexual reproduction and infection in a global human fungal pathogen. (PNAS 2022)

- DOI: 10.1073/pnas.2122293119 | PMCID: PMC8872808 | PMID: 35169080
- Evidence: For each of the above samples, paired-end, 100-bp sequenced reads were aligned to a JEC21(α) C. deneoformans reference genome ( 85 ) using BWA [v0.7.12-r1039 ( 86 )], and binary alignment maps were constructed using SAMtools [v0.1.1996b5f2294a ( 87 )].
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [ImageJ, scikit-learn]

### Stabilizing selection on Atlantic cod supergenes through a millennium of extensive exploitation. (PNAS 2022)

- DOI: 10.1073/pnas.2114904119 | PMCID: PMC8872764 | PMID: 35165196
- Evidence: Reads were aligned to the Atlantic cod reference genome gadMor2 ( 24 ) with the BWA software package ( 89 ) v0.7.5, before the alignments were indexed and sorted with the Samtools software package ( 90 ) v1.3.1.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> dimensionality reduction/clustering [R] -> stage not stated [VCFtools]

### Occasional paternal inheritance of the germline-restricted chromosome in songbirds. (PNAS 2022)

- DOI: 10.1073/pnas.2103960119 | PMCID: PMC8794876 | PMID: 35058355
- Version used: **0.7.17**
- Evidence: We then mapped each library (paired-end reads) against the reference somatic genome, taeGut1 ( 36 ), using BWA-MEM v0.7.17 ( 37 ) with the default settings while marking shorter split hits as secondary.
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard] -> quantification [Picard] -> differential/statistical testing [R v4.0, lme4] -> stage not stated [BCFtools v1.9, GATK, RAxML v1.0.2, SAMtools v1.6]

### Sex-specific splicing of Z- and W-borne <i>nr5a1</i> alleles suggests sex determination is controlled by chromosome conformation. (PNAS 2022)

- DOI: 10.1073/pnas.2116475119 | PMCID: PMC8795496 | PMID: 35074916
- Evidence: BWA (Burrows–Wheeler Alignment Tool Version 0.7.17-r1188) ( 61 ) was used with default parameters to map the reads to the draft Pogona assembly Pvi1.1.
- Full pipeline: alignment/mapping [BWA, Clustal Omega] -> quantification [DESeq2 v1.26.0] -> dimensionality reduction/clustering [AlphaFold] -> differential/statistical testing [DESeq2 v1.26.0] -> stage not stated [R, kallisto]

### Rapid radiation in a highly diverse marine environment. (PNAS 2022)

- DOI: 10.1073/pnas.2020457119 | PMCID: PMC8794831 | PMID: 35042790
- Evidence: The sequences were then back transformed to fq format using GATK, mapped to the hamlet reference genome using BWA ( 76 ), and merged with the uBAM files containing the read group information with GATK (git 1.5).
- Full pipeline: alignment/mapping [BWA, MAFFT] -> variant calling [GATK, MAFFT, SHAPEIT] -> differential/statistical testing [GEMMA] -> structure determination [IQ-TREE] -> stage not stated [BCFtools, R, RAxML, VCFtools]

### Somatic mutations of MLL4/COMPASS induce cytoplasmic localization providing molecular insight into cancer prognosis and treatment. (PNAS 2023)

- DOI: 10.1073/pnas.2310063120 | PMCID: PMC10756272 | PMID: 38113256
- Evidence: Trimmed reads were mapped to human reference genome version hg38 using bwa-mem.
- Full pipeline: quality control [FastQC, Trimmomatic] -> read trimming [BWA, FastQC, Trimmomatic] -> alignment/mapping [BWA, STAR v2.5.2] -> stage not stated [BEDTools v2.30.0, Bioconductor, GATK, MACS2, Metascape, Picard, SAMtools, SnpEff, deepTools v3.5.1, edgeR v3.0.8]

### A role for mutations in &lt;i&gt;AK9&lt;/i&gt; and other genes affecting ependymal cells in idiopathic normal pressure hydrocephalus. (PNAS 2023)

- DOI: 10.1073/pnas.2300681120 | PMCID: PMC10743366 | PMID: 38100419
- Evidence: Single nucleotide variants (SNVs) and insertions/deletions (indels) were identified (Human Genome build GRCh37, bwa-mem, Genome Analysis Toolkit HaplotypeCaller).
- Full pipeline: variant calling [BWA, GATK] -> stage not stated [ImageJ]

### Antimicrobial resistance level and conjugation permissiveness shape plasmid distribution in clinical enterobacteria. (PNAS 2023)

- DOI: 10.1073/pnas.2314135120 | PMCID: PMC10741383 | PMID: 38096417
- Evidence: For computing the PCN, the Illumina trimmed reads were first mapped to their respective genome assembly using BWA MEM v0.7.17 ( 56 ).
- Full pipeline: read trimming [BWA, MAFFT v7.453, Trim Galore v0.6.6] -> alignment/mapping [BWA, IQ-TREE v1.6.12, MAFFT v7.453] -> differential/statistical testing [R] -> stage not stated [BLAST, HMMER v3.3, Prokka v1.14.6, QUAST v5.0.2, SAMtools, SPAdes v3.15.2, ggplot2 v3.3.6, ggpubr v0.4.0, pheatmap v1.0.12, phytools v1.0, tidyverse v1.3.1]

### A suppressor screen &lt;i&gt;in C. elegans&lt;/i&gt; identifies a multiprotein interaction that stabilizes the synaptonemal complex. (PNAS 2023)

- DOI: 10.1073/pnas.2314335120 | PMCID: PMC10723054 | PMID: 38055743
- Evidence: We used BWA MEM ( 60 ) to align reads to the C. elegans reference genome (version WBcel235 from wormbase.org).
- Full pipeline: alignment/mapping [BWA, GATK] -> stage not stated [AlphaFold, SnpEff]

### Downregulation of a transcription factor associated with resistance to Bt toxin Vip3Aa in the invasive fall armyworm. (PNAS 2023)

- DOI: 10.1073/pnas.2306932120 | PMCID: PMC10622909 | PMID: 37874855
- Evidence: Raw reads of 200 bp were filtered using SOAPnuk (v1.5.6) software ( 70 ) with parameter ‘-n 0.1 -q 0.5 -l 12 -Q 2’ and aligned to the S. frugiperda reference genome [ZJ version ( 71 )] using BWA-MEM ( 72 ) with default parameters (version 0.7.17).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM] -> variant calling [GATK v4.2.3] -> quantification [RSEM] -> normalisation [RSEM] -> differential/statistical testing [DESeq2] -> stage not stated [GEMMA, PLINK, SnpEff]

### Functional genomic diversity is correlated with neutral genomic diversity in populations of an endangered rattlesnake. (PNAS 2023)

- DOI: 10.1073/pnas.2303043120 | PMCID: PMC10614936 | PMID: 37844221
- Version used: **0.7.17**
- Evidence: All sequences were mapped to the S. catenatus Hi-C reference genome with BWA v.0.7.17 ( 63 ) using the mem algorithm.
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK, SnpEff v4.3] -> stage not stated [BUSCO, R]

### Pan-centromere reveals widespread centromere repositioning of soybean genomes. (PNAS 2023)

- DOI: 10.1073/pnas.2310177120 | PMCID: PMC10589659 | PMID: 37816061
- Evidence: ...LEN:36 SLIDINGWINDOW: 4:20.” The quality-controlled reads were then aligned to the soybean ZH13 reference genome ( 35 ) using Burrows Wheeler Aligner BWA-MEM software ( 71 ) with default parameters and were further filtered by SAMtools (version 1.3.1) ( 72 ) for nonunique and duplicated reads.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, Picard, SAMtools v1.3.1, Trimmomatic v0.36] -> variant calling [BCFtools, GATK v3.8.1] -> stage not stated [MACS2]

### Changes in parrot diversity after human arrival to the Caribbean. (PNAS 2023)

- DOI: 10.1073/pnas.2301128120 | PMCID: PMC10576146 | PMID: 37748079
- Version used: **0.7.13**
- Evidence: We then mapped contigs to UCE probes and generated an index for the reference sequence and independently mapped reads from each sample using BWA v0.7.13-r1126 ( 76 ).
- Full pipeline: read trimming [fastp] -> alignment/mapping [BWA v0.7.13, IQ-TREE v2.1.2, SAMtools v1.10] -> stage not stated [BCFtools v1.12, MAFFT v7.455, R v4.1]

### Scaphopoda is the sister taxon to Bivalvia: Evidence of ancient incomplete lineage sorting. (PNAS 2023)

- DOI: 10.1073/pnas.2302361120 | PMCID: PMC10556646 | PMID: 37738291
- Evidence: To evaluate genome quality, we first mapped Illumina reads onto the assemblies with BWA ( 74 ).
- Full pipeline: alignment/mapping [BWA, Cufflinks v2.3.1, HISAT2 v2.2.1, MAFFT v7.453] -> differential/statistical testing [MrBayes] -> stage not stated [BLAST v2.13.0, BUSCO v5.4.2b, IQ-TREE, OrthoFinder v2.4.0, RAxML, hifiasm v0.13]

### A methanotrophic bacterium to enable methane removal for climate mitigation. (PNAS 2023)

- DOI: 10.1073/pnas.2310046120 | PMCID: PMC10466089 | PMID: 37603746
- Version used: **0.7.17**
- Evidence: Briefly, reads from the fastq field were aligned to the M. buryatense 5GB1C genome (NCBI accession NZ_CP035467.1 ) using BWA with the BWA-MEM algorithm (BWA version 0.7.17-r1198-dirty, default parameters) ( 45 ).
- Full pipeline: alignment/mapping [BWA v0.7.17] -> quantification [HTSeq]

### Range-wide differential adaptation and genomic offset in critically endangered Asian rosewoods. (PNAS 2023)

- DOI: 10.1073/pnas.2301603120 | PMCID: PMC10438386 | PMID: 37549265
- Version used: **0.7.17**
- Evidence: Reads were aligned against the Dacoc_1.4 genome and the Daoli_0.3 genome using BWA-MEM 0.7.17 ( 84 ).
- Full pipeline: read trimming [Cutadapt v1.18] -> alignment/mapping [BWA v0.7.17, SAMtools v1.9, STAR v2.7.6, Snakemake, minimap2] -> variant calling [Cutadapt v1.18, VCFtools v0.1.16] -> dimensionality reduction/clustering [ADMIXTURE] -> differential/statistical testing [ADMIXTURE] -> visualisation [minimap2] -> stage not stated [AUGUSTUS v3.3.3, BCFtools v1.9, BUSCO, Canu v2.1.1, R v4.1, RepeatMasker v2.0.1]

### Echoes of ancient introgression punctuate stable genomic lineages in the evolution of figs. (PNAS 2023)

- DOI: 10.1073/pnas.2222035120 | PMCID: PMC10334730 | PMID: 37399402
- Evidence: For each sample, reads were mapped to the Ficus carica chloroplast genome (GenBank accession number KY635880.1 ) using BWA ( 71 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA, MAFFT v7.450, RAxML] -> stage not stated [SAMtools]

### Phase variation as a major mechanism of adaptation in &lt;i&gt;Mycobacterium tuberculosis&lt;/i&gt; complex. (PNAS 2023)

- DOI: 10.1073/pnas.2301394120 | PMCID: PMC10334774 | PMID: 37399390
- Evidence: The raw sequence reads from all sequenced isolates were trimmed with version 0.20.4 Prinseq (settings: -min_qual_mean 20) ( 58 ) and then aligned to H37Rv with version 0.7.15 of the BWA mem algorithm using the -M settings ( 59 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [BCFtools, GEMMA, IQ-TREE, Picard, Pilon, SAMtools]

### Mutation rates and adaptive variation among the clinically dominant clusters of <i>Mycobacterium abscessus</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302033120 | PMCID: PMC10235944 | PMID: 37216535
- Evidence: After assigning isolates to a subspecies, reads were mapped to the corresponding reference genome using BWA MEM v0.7.17 ( 36 ).
- Full pipeline: alignment/mapping [BCFtools v1.10.2, BWA, IQ-TREE v1.6.12] -> differential/statistical testing [Python, pingouin, statsmodels] -> structure determination [TreeTime] -> stage not stated [Pilon v1.23, Prokka, R, SPAdes v3.11.1]

### Digital microfluidics-based digital counting of single-cell copy number variation (dd-scCNV Seq). (PNAS 2023)

- DOI: 10.1073/pnas.2221934120 | PMCID: PMC10193948 | PMID: 37155890
- Version used: **0.7.17**
- Evidence: The trimmed data were then aligned to the GRCh37 reference genome ( ftp://ftp.ncbi.nih.gov/genomes/H_sapiens/ ) using BWA-MEM (version 0.7.17) with default parameters.
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.38] -> alignment/mapping [BWA v0.7.17, Picard, SAMtools v1.9] -> differential/statistical testing [SAMtools v1.9] -> stage not stated [BEDTools]

### Conservation management strategy impacts inbreeding and mutation load in scimitar-horned oryx. (PNAS 2023)

- DOI: 10.1073/pnas.2210756120 | PMCID: PMC10160979 | PMID: 37098062
- Evidence: Reads were then mapped to the scimitar-horned oryx reference genome assembly ( Oryx dammah assembly v1.1, Genbank accession number GCF_014754425.2) using BWA MEM v0.7.17 ( 90 ) with default parameters.
- Full pipeline: quality control [Cutadapt v1.16, FastQC v0.11.7] -> read trimming [Cutadapt v1.16, FastQC v0.11.7] -> alignment/mapping [BWA, Picard, SAMtools v1.9] -> variant calling [ANGSD, GATK v3.8, VCFtools] -> stage not stated [BCFtools v1.9, PLINK v1.9, R v4.2, SnpEff v5.0, VEP]

### Epistasis reduces fitness costs of influenza A virus escape from stem-binding antibodies. (PNAS 2023)

- DOI: 10.1073/pnas.2208718120 | PMCID: PMC10151473 | PMID: 37068231
- Evidence: In brief, after removing adapters using Trimmomatic (version 0.39) ( 59 ), reads were aligned to their reference sequence using the option mem from BWA ( 60 ).
- Full pipeline: read trimming [BWA, Trimmomatic v0.39] -> alignment/mapping [BWA, Trimmomatic v0.39] -> stage not stated [GATK, Picard]

### The <i>Holothuria leucospilota</i> genome elucidates sacrificial organ expulsion and bioadhesive trap enriched with amyloid-patterned proteins. (PNAS 2023)

- DOI: 10.1073/pnas.2213512120 | PMCID: PMC10120082 | PMID: 37036994
- Evidence: All cleaned data were mapped onto contigs by using BWA aligner, while LACHESIS was used for scaffolds de novo assemblies.
- Full pipeline: alignment/mapping [BUSCO, BWA, MAFFT, RAxML] -> normalisation [DESeq2] -> visualisation [MAFFT, RAxML] -> stage not stated [AlphaFold, InterProScan]

### Spectra and characteristics of somatic mutations induced by ionizing radiation in hematopoietic stem cells. (PNAS 2023)

- DOI: 10.1073/pnas.2216550120 | PMCID: PMC10104525 | PMID: 37018193
- Version used: **0.7.17**
- Evidence: Sequence reads were mapped to the mouse reference genome (UCSC mm10) using BWA-MEM v.0.7.17 with the “−M” option compatible with Picard v2.18.26 (broadinstitute.github.io/picard) used to remove PCR duplicates.
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v4.1.0.0, Picard v2.18.26, SAMtools] -> variant calling [GATK v4.1.0.0, SAMtools] -> differential/statistical testing [R v4.0.3]

### A mutant fitness assay identifies bacterial interactions in a model ocean hot spot. (PNAS 2023)

- DOI: 10.1073/pnas.2217200120 | PMCID: PMC10041152 | PMID: 36920927
- Evidence: Trimmed reads were mapped to the R. pomeroyi DSS-3 genome (GenBank accession NC_003911 ) with BWA ( 80 ) in “aln” mode allowing for one mismatch, and a wig formatted file was generated indicating each site of insertion and the number of reads that mapped to it ( https://doi.org/10.5281/zenodo.7489904 ) ( 81 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> differential/statistical testing [R v4.0, data.table, tidyverse]

### Wheat &lt;i&gt;Ym2&lt;/i&gt; originated from &lt;i&gt;Aegilops sharonensis&lt;/i&gt; and confers resistance to soil-borne &lt;i&gt;Wheat yellow mosaic virus&lt;/i&gt; infection to the roots. (PNAS 2023)

- DOI: 10.1073/pnas.2214968120 | PMCID: PMC10089197 | PMID: 36897977
- Evidence: Madsen CDS618 sequence using bwa-mem software and assembled using GeneStudio Professional software ( https://en.freedownloadmanager.org/Windows-PC/GeneStudio.html ).
- Full pipeline: read trimming [BLAST, Bowtie2, HISAT2] -> alignment/mapping [Bowtie2, HISAT2] -> differential/statistical testing [edgeR] -> stage not stated [BCFtools v1.10, BWA, Clustal Omega, featureCounts v1.6.3]

### Three amphioxus reference genomes reveal gene and chromosome evolution of chordates. (PNAS 2023)

- DOI: 10.1073/pnas.2201504120 | PMCID: PMC10013865 | PMID: 36867684
- Evidence: We aligned the Illumina reads of either parental species to the contigs by bwa-mem with default parameters, and only kept the alignments with a mapping quality higher than 60.
- Full pipeline: read trimming [Trimmomatic v0.36] -> alignment/mapping [BWA, GATK v3.8, MAFFT v7.294b, OrthoFinder v2.2.7, minimap2 v2.15] -> variant calling [SHAPEIT] -> stage not stated [AUGUSTUS v3.3, BCFtools, BEDTools, BUSCO, Canu v1.6, Cufflinks v2.2.1, HISAT2 v2.0.4, IQ-TREE v2.0, InterProScan v5.35, R, RepeatMasker v1.0.10, StringTie v1.3.3b, VCFtools v0.1.16, featureCounts v1.5.2, igraph]

### Evolutionary analysis of a complete chicken genome. (PNAS 2023)

- DOI: 10.1073/pnas.2216641120 | PMCID: PMC9974502 | PMID: 36780517
- Evidence: We aligned the ChIP-seq reads with the BWA-MEM algorithm with options “-k 50 -c 1000000”.
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.4, SAMtools, featureCounts v1.6.2, minimap2 v2.24] -> quantification [featureCounts v1.6.2] -> machine learning [BUSCO v4.0.5] -> stage not stated [BEDTools, HISAT2 v2.1.0, OrthoFinder v2.5.2, RepeatMasker v4.1.2, StringTie v2.1.1, hifiasm v0.16.0]

### Heterochromatin and RNAi act independently to ensure genome stability in Mucorales human fungal pathogens. (PNAS 2023)

- DOI: 10.1073/pnas.2220475120 | PMCID: PMC9963178 | PMID: 36745785
- Version used: **0.7.17**
- Evidence: Reads were aligned to the M. lusitanicus MU402 genome ( https://mycocosm.jgi.doe.gov/Muccir1_3/Muccir1_3.home.html ) employing BWA-MEM v.0.7.17 for ChIP DNA, STAR v.2.7.10a for long RNA, and ShortStack v3.8.5 for sRNA reads.
- Full pipeline: quality control [Trim Galore] -> read trimming [IQ-TREE v2.2.0.3, MAFFT v7.475, limma] -> alignment/mapping [BWA v0.7.17, IQ-TREE v2.2.0.3, MAFFT v7.475, STAR v2.7.10a] -> quantification [featureCounts v2.0.1] -> normalisation [limma] -> stage not stated [BLAST, BUSCO v5.4.3, InterProScan v5.59, MACS2 v2.2.7.1, RepeatMasker v4.1.3]

### Resurrection genomics provides molecular and phenotypic evidence of rapid adaptation to salinization in a keystone aquatic species. (PNAS 2023)

- DOI: 10.1073/pnas.2217276120 | PMCID: PMC9963159 | PMID: 36730191
- Evidence: Quality trimmed reads were aligned to the chromosome-level D. pulicaria genome assembly ( 76 ) using the BWA mem algorithm ( 77 ).
- Full pipeline: quality control [Trimmomatic] -> read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [R] -> stage not stated [BCFtools, BEDTools, SAMtools, VEP]

### Genome editing in plants using the compact editor CasΦ. (PNAS 2023)

- DOI: 10.1073/pnas.2216822120 | PMCID: PMC9942878 | PMID: 36652483
- Version used: **0.7.17**
- Evidence: Reads were first quality and adaptor trimmed using Trim Galore and then mapped to the target genomic region by the BWA aligner (v0.7.17, BWA-MEM algorithm).
- Full pipeline: read trimming [BWA v0.7.17, Trim Galore] -> alignment/mapping [BWA v0.7.17, Trim Galore] -> stage not stated [GATK v4.2.0.0, R, Strelka v2.9.2]

### <i>Regulator of Awn Elongation 3</i>, an E3 ubiquitin ligase, is responsible for loss of awns during African rice domestication. (PNAS 2023)

- DOI: 10.1073/pnas.2207105120 | PMCID: PMC9942864 | PMID: 36649409
- Evidence: Individual resequencing datasets were downloaded from the internet as raw reads and aligned to the Nipponbare reference genome using BWA software ( 65 , 66 ) for alignment, and GATK’s HaplotypeCaller algorithm ( 67 – 70 ) for variant-calling.
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> stage not stated [AlphaFold]

### Genome-wide parallelism underlies contemporary adaptation in urban lizards. (PNAS 2023)

- DOI: 10.1073/pnas.2216789120 | PMCID: PMC9934206 | PMID: 36634133
- Evidence: We aligned our quality filtered reads to this nonredundant set of A. carolinensis exons using BWA ( 87 ) (v0.7.17-r1188).
- Full pipeline: read trimming [BWA, Trimmomatic] -> alignment/mapping [BWA] -> visualisation [phytools] -> stage not stated [BCFtools, GATK, ImageJ, PLINK, Python, R v4.0.3, VCFtools]

### Similar evolutionary trajectories in an environmental <i>Cryptococcus neoformans</i> isolate after human and murine infection. (PNAS 2023)

- DOI: 10.1073/pnas.2217111120 | PMCID: PMC9926274 | PMID: 36603033
- Version used: **0.7.17**
- Evidence: To identify variants in the mouse-passaged isolates, Illumina reads for CPL and CPB samples were aligned to the CU assembly with BWA-MEM v0.7.17 ( 70 ), and variants were called with our publicly available GATK v4 pipeline ( https://github.com/broadinstitute/fungal-wdl/tree/master/gatk4 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Bioconductor, Bowtie2 v2.3.5, DESeq2 v1.22.2, GATK, HTSeq v1.99.2, RAxML] -> visualisation [R v3.6] -> stage not stated [AlphaFold v2.1.0, Canu v2.1.1, ImageJ, Medaka]

### Non-B-form DNA tends to form in centromeric regions and has undergone changes in polyploid oat subgenomes. (PNAS 2023)

- DOI: 10.1073/pnas.2211683120 | PMCID: PMC9910436 | PMID: 36574697
- Evidence: The trimmed reads were mapped to the reference genomes of Avena sativa (Sang) with BWA-MEM software using default parameters.
- Full pipeline: quality control [FastQC] -> read trimming [BWA, Trimmomatic v0.36] -> alignment/mapping [BWA, MACS2, SAMtools v1.3.1, deepTools] -> normalisation [deepTools] -> visualisation [deepTools]

### High-frequency and functional mitochondrial DNA mutations at the single-cell level. (PNAS 2023)

- DOI: 10.1073/pnas.2201518120 | PMCID: PMC9910596 | PMID: 36577067
- Version used: **0.7.17**
- Evidence: The resulted paired-end reads were then mapped in a first round to the complete human genome (GRCh38 full assembly plus decoy, alternate contigs and HLA sequences, ftp://ftp.1000genomes.ebi.ac.uk ) by BWA-MEM (version 0.7.17) ( 81 ) and were mapped in a second round to a modified mtDNA sequence with the final 120 bp copied to the start.
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools] -> registration [SAMtools] -> stage not stated [ANNOVAR, ggplot2]

### Repeated global adaptation across plant species. (PNAS 2024)

- DOI: 10.1073/pnas.2406832121 | PMCID: PMC11670234 | PMID: 39705310
- Version used: **0.7.17**
- Evidence: Clean reads were then aligned to reference genomes with bwa-mem (v0.7.17-r1188) ( 113 ), using 12 distinct reference genomes to map 17 datasets.
- Full pipeline: read trimming [fastp] -> alignment/mapping [BCFtools, BWA v0.7.17, SAMtools] -> variant calling [BCFtools, VCFtools] -> registration [BCFtools, GATK] -> stage not stated [Picard, R, igraph]

### The genetic origins and impacts of historical Papuan migrations into Wallacea. (PNAS 2024)

- DOI: 10.1073/pnas.2412355121 | PMCID: PMC11670103 | PMID: 39689173
- Version used: **0.7.17**
- Evidence: Briefly, trimmed reads were mapped to the human reference genome GRCh38 (hg38) using BWA mem v0.7.17 with the T parameter set to 0 ( 64 ).
- Full pipeline: read trimming [BWA v0.7.17, fastp] -> alignment/mapping [BWA v0.7.17, GATK, SAMtools v1.9] -> variant calling [BCFtools] -> dimensionality reduction/clustering [ADMIXTURE, R] -> stage not stated [PLINK v1.987]

### A complete DNA repair system assembled by two endosymbionts restores heat tolerance of the insect host. (PNAS 2024)

- DOI: 10.1073/pnas.2415651121 | PMCID: PMC11665910 | PMID: 39656210
- Evidence: APS using software BWA (Burrows-Wheeler Aligner).
- Full pipeline: alignment/mapping [BWA] -> quantification [ImageJ]

### Species-wide inventory of &lt;i&gt;Arabidopsis thaliana&lt;/i&gt; organellar variation reveals ample phenotypic variation for photosynthetic performance. (PNAS 2024)

- DOI: 10.1073/pnas.2414024121 | PMCID: PMC11626173 | PMID: 39602263
- Evidence: The reads were then mapped to the A. thaliana Col-0 reference genome, TAIR10.1, using speedseq and the Burrow-Wheeler aligner, BWA-MEM ( 96 , 97 ).
- Full pipeline: read trimming [Cutadapt] -> alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [GATK, GEMMA, PLINK, R v4.0, ggplot2 v3.3.2, lme4]

### Mismatch between lab-generated and field-evolved resistance to transgenic Bt crops in &lt;i&gt;Helicoverpa zea&lt;/i&gt;. (PNAS 2024)

- DOI: 10.1073/pnas.2416091121 | PMCID: PMC11588094 | PMID: 39503848
- Evidence: Trimmed reads were mapped to the template genome assembly of LAB-S, a susceptible lab strain of H. zea (from Benzon Research Inc.), and to the de novo genome assembly of H. zea strain GA-R ( 61 ) using BWA ( 100 ) and sorted using SAMtools ( 101 ).
- Full pipeline: read trimming [BWA, SAMtools] -> alignment/mapping [BWA, Picard, SAMtools, VarScan] -> variant calling [VarScan] -> normalisation [deepTools] -> dimensionality reduction/clustering [R] -> visualisation [ggplot2] -> stage not stated [BCFtools, SnpEff, VCFtools, pheatmap]

### Maternal genetic variants in kinesin motor domains prematurely increase egg aneuploidy. (PNAS 2024)

- DOI: 10.1073/pnas.2414963121 | PMCID: PMC11551467 | PMID: 39475646
- Evidence: Data were aligned to the human reference genome (hg19) using BWA ( 77 ), and the joint genotyping was performed using the GATK v3.8 pipeline following the GATK best practices ( 78 ).
- Full pipeline: alignment/mapping [BWA, GATK v3.8] -> variant calling [BWA, GATK v3.8] -> stage not stated [ImageJ]

### Enhancer landscape of lung neuroendocrine tumors reveals regulatory and developmental signatures with potential theranostic implications. (PNAS 2024)

- DOI: 10.1073/pnas.2405001121 | PMCID: PMC11474083 | PMID: 39361648
- Version used: **0.7.17**
- Evidence: ChIP-seq reads were aligned to the reference genome (hg38) using the BWA 0.7.17 (ref.
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.10a] -> quantification [QuPath v0.5.1, featureCounts] -> differential/statistical testing [DESeq2] -> visualisation [deepTools] -> stage not stated [BEDTools, HOMER]

### Investigating the &lt;i&gt;cis-&lt;/i&gt;regulatory basis of C&lt;sub&gt;3&lt;/sub&gt; and C&lt;sub&gt;4&lt;/sub&gt; photosynthesis in grasses at single-cell resolution. (PNAS 2024)

- DOI: 10.1073/pnas.2402781121 | PMCID: PMC11459142 | PMID: 39312655
- Version used: **0.7.17**
- Evidence: Reads were aligned using BWA (version 0.7.17) ( 65 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, SAMtools v1.16.1, minimap2] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt v4.5, OrthoFinder, scDblFinder]

### Unraveling the genomic diversity and admixture history of captive tigers in the United States. (PNAS 2024)

- DOI: 10.1073/pnas.2402924121 | PMCID: PMC11441546 | PMID: 39298482
- Version used: **0.7.17**
- Evidence: Reads were mapped to the GenTig1.0 genome ( 66 ) using BWA-MEM v0.7.17 ( 67 ) and variant calling was subsequently performed by Gencove using the Genome Analysis Toolkit v4.1.4.1 ( 68 ) according to best practices ( 69 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v4.1.4.1] -> variant calling [BWA v0.7.17, GATK v4.1.4.1] -> dimensionality reduction/clustering [ADMIXTURE, PLINK] -> stage not stated [BCFtools v1.6, VCFtools, VEP]

### Elucidating the sustainability of 700 y of Inuvialuit beluga whale hunting in the Mackenzie River Delta, Northwest Territories, Canada. (PNAS 2024)

- DOI: 10.1073/pnas.2405993121 | PMCID: PMC11348011 | PMID: 39136992
- Evidence: Processed reads were mapped using BWA ( 75 ) applying the Backtrack algorithm, while disabling the seed function.
- Full pipeline: alignment/mapping [BWA, MAFFT, RepeatMasker, SAMtools] -> registration [GATK, Picard] -> dimensionality reduction/clustering [R] -> visualisation [R] -> stage not stated [ANGSD]

### ZNF91 is an endogenous repressor of the molecular phenotype associated with X-linked dystonia-parkinsonism (XDP). (PNAS 2024)

- DOI: 10.1073/pnas.2401217121 | PMCID: PMC11331120 | PMID: 39102544
- Evidence: Next, the trimmed reads were aligned to the XDP BAC clone using BWA-MEM aligner using default settings ( 67 ).
- Full pipeline: quality control [Bowtie2 v2.3.4.2] -> read trimming [BWA, fastp] -> alignment/mapping [BWA, Bowtie2 v2.3.4.2, featureCounts] -> normalisation [DESeq2, deepTools] -> visualisation [MACS2, deepTools] -> stage not stated [Galaxy, RepeatMasker, SAMtools]

### Resolving the 22q11.2 deletion using CTLR-Seq reveals chromosomal rearrangement mechanisms and individual variance in breakpoints. (PNAS 2024)

- DOI: 10.1073/pnas.2322834121 | PMCID: PMC11295037 | PMID: 39042694
- Evidence: Illumina WGS libraries were aligned with BWA-MEM ( 61 ) as described in Zhou et al.
- Full pipeline: alignment/mapping [BWA, minimap2 v2.18] -> variant calling [Flye] -> stage not stated [Medaka v1.9.1]

### Ancient genomes reveal over two thousand years of dingo population structure. (PNAS 2024)

- DOI: 10.1073/pnas.2407584121 | PMCID: PMC11287250 | PMID: 38976766
- Evidence: The remaining reads were aligned to the canFam3.1 reference genome using BWA ( 71 ) aln v0.7.17-r1188 (-n 0.01 -l 1024 -o 2), and we deduplicated the mapped reads using “MarkDuplicates.jar” in Picard Tools v2.22.9 ( https://github.com/broadinstitute/picard ).
- Full pipeline: quality control [FastQC v0.11.9] -> read trimming [BWA, FastQC v0.11.9, Picard] -> alignment/mapping [BEAST, BWA, Picard, SAMtools] -> normalisation [BEAST] -> dimensionality reduction/clustering [ggplot2, igraph, pheatmap v1.0.12] -> differential/statistical testing [IQ-TREE, igraph, pheatmap v1.0.12] -> visualisation [FastQC v0.11.9, ggplot2]

### Pathogenic variants in autism gene &lt;i&gt;KATNAL2&lt;/i&gt; cause hydrocephalus and disrupt neuronal connectivity by impairing ciliary microtubule dynamics. (PNAS 2024)

- DOI: 10.1073/pnas.2314702121 | PMCID: PMC11228466 | PMID: 38916997
- Evidence: BWA-MEM ( 61 ) was applied to align sequence reads to human reference genome GRCh37/hg19.
- Full pipeline: alignment/mapping [BWA] -> variant calling [ANNOVAR, GATK] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [ImageJ] -> visualisation [ComplexHeatmap, ggplot2, pheatmap]

### Bispecific antibodies targeting two glycoproteins on SFTSV exhibit synergistic neutralization and protection in a mouse model. (PNAS 2024)

- DOI: 10.1073/pnas.2400163121 | PMCID: PMC11181109 | PMID: 38830098
- Version used: **0.7.17**
- Evidence: Then, the filtered reads were mapped to the SFTSV by Burrows–Wheeler aligner (BWA version 0.7.17-r1188).
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, MUSCLE v3.8.31, MotionCor2] -> variant calling [SAMtools v1.9] -> structure determination [Coot v0.9.3, PHENIX] -> machine learning [Topaz] -> visualisation [PyMOL v2.0] -> stage not stated [fastp]

### Genome evolution of the ancient hexaploid <i>Platanus</i> × <i>acerifolia</i> (London planetree). (PNAS 2024)

- DOI: 10.1073/pnas.2319679121 | PMCID: PMC11181145 | PMID: 38830106
- Evidence: Sequence identity was also assessed by aligning the paired-end reads to the assembled genome using BWA ( 69 ).
- Full pipeline: read trimming [MAFFT, fastp] -> alignment/mapping [BWA, Bowtie2, Cufflinks, MAFFT, RSEM, TopHat] -> normalisation [RSEM] -> visualisation [R, pheatmap] -> stage not stated [AUGUSTUS, BUSCO, GATK v4.0.0, InterProScan, OrthoFinder, RAxML, RepeatMasker, VCFtools]

### Extreme elevational migration spurred cryptic speciation in giant hummingbirds. (PNAS 2024)

- DOI: 10.1073/pnas.2313599121 | PMCID: PMC11126955 | PMID: 38739790
- Evidence: Cleaned reads were aligned to the annotated Anna’s hummingbird ( Calypte anna ) reference genome (GenBank Accession GCA_003957555.2) using BWA -mem v0.7.17 ( 72 ).
- Full pipeline: read trimming [Trimmomatic] -> alignment/mapping [BWA] -> variant calling [VCFtools v0.1.16] -> simulation/modelling [RAxML v8.2.4] -> stage not stated [BCFtools v1.14, GATK, ImageJ, Picard v2.26.10, Python, R, SAMtools v1.14, SPAdes v3.15.3]

### Intergenomic signatures of coevolution between Tasmanian devils and an infectious cancer. (PNAS 2024)

- DOI: 10.1073/pnas.2307780121 | PMCID: PMC10962979 | PMID: 38466855
- Evidence: Trimmed reads were aligned to the reference genome mSarHar1.11 ( 25 ) using BWA MEM version 0.7.17 ( 81 ) with the -M flag and default settings, and Samtools ( 82 ) was used to sort the aligned reads.
- Full pipeline: quality control [BCFtools, FastQC, Trim Galore] -> read trimming [BWA, FastQC, HISAT2 v2.1.0, SAMtools, Trim Galore] -> alignment/mapping [BWA, HISAT2 v2.1.0, SAMtools] -> differential/statistical testing [GEMMA] -> stage not stated [GATK v4.2.0.0, Picard v2.25.0, R v4.1.0]

### The extent of introgression between incipient <i>Clarkia</i> species is determined by temporal environmental variation and mating system. (PNAS 2024)

- DOI: 10.1073/pnas.2316008121 | PMCID: PMC10963018 | PMID: 38466849
- Evidence: We used BWA mem to map trimmed reads to the masked reference genome.
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA, Picard, SAMtools] -> variant calling [GATK v3.8.0] -> stage not stated [BCFtools, Canu v2.1, RAxML v8.2.11]

### Genomic ancestry and social dynamics of the last hunter-gatherers of Atlantic France. (PNAS 2024)

- DOI: 10.1073/pnas.2310545121 | PMCID: PMC10927518 | PMID: 38408241
- Evidence: Merged reads were mapped against the human reference genome using BWA aln 0.7.13 ( 58 ).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [PLINK, SAMtools]

### Low-frequency somatic mutations are heritable in tropical trees <i>Dicorynia guianensis</i> and <i>Sextonia rubra</i>. (PNAS 2024)

- DOI: 10.1073/pnas.2313312121 | PMCID: PMC10927512 | PMID: 38412128
- Evidence: The reads are aligned against the reference genome using BWA mem with the option to mark shorter splits (v0.7.17).
- Full pipeline: quality control [FastQC v0.11.9, Trimmomatic v0.39] -> read trimming [FastQC v0.11.9, Trimmomatic v0.39] -> alignment/mapping [BWA, GATK, SAMtools] -> stage not stated [BCFtools v1.10.2, BEDTools, BUSCO, HMMER, R, RepeatMasker v2.0.3]

### Chromosomal evolution, environmental heterogeneity, and migration drive spatial patterns of species richness in <i>Calochortus</i> (Liliaceae). (PNAS 2024)

- DOI: 10.1073/pnas.2305228121 | PMCID: PMC10927571 | PMID: 38394215
- Evidence: Reads were mapped against the reference plastome using BWA with the bwa mem algorithm ( 90 ).
- Full pipeline: read trimming [Trimmomatic v0.40] -> alignment/mapping [BWA, MAFFT v7.023b] -> stage not stated [BEAST v6.6, IQ-TREE, QGIS, R, SAMtools v1.3, lme4]

### Comparative chemical genomics in <i>Babesia</i> species identifies the alkaline phosphatase PhoD as a determinant of antiparasitic resistance. (PNAS 2024)

- DOI: 10.1073/pnas.2312987121 | PMCID: PMC10907312 | PMID: 38377214
- Evidence: Cleaned, paired fastq files were aligned to the respective reference genome [ B. divergens strain 1802A ( 67 ), B. bovis T2Bo ( 109 , 110 ) both accessed via piroplasmaDB] using BWA ( 111 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BEDTools, BWA, Clustal Omega, PyMOL v2.3.2, SAMtools, VCFtools] -> dimensionality reduction/clustering [Clustal Omega] -> stage not stated [AlphaFold]

### The impact of age and number of mutations on the size of clonal hematopoiesis. (PNAS 2024)

- DOI: 10.1073/pnas.2319364121 | PMCID: PMC10895265 | PMID: 38359296
- Version used: **0.7.17**
- Evidence: The paired-end reads from whole-exome sequencing were mapped to human genome (version hg19) by BWA aligner (v0.7.17) ( 45 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, Picard v2.23.0] -> differential/statistical testing [R, ggplot2, tidyverse] -> stage not stated [ANNOVAR, Mutect2 v1.1.7, SnpEff v4.2]

### A massive alteration of gene expression in undescended testicles of dogs and the association of <i>KAT6A</i> variants with cryptorchidism. (PNAS 2024)

- DOI: 10.1073/pnas.2312724121 | PMCID: PMC10873591 | PMID: 38315849
- Evidence: NGS reads were aligned using BWA ( 41 ), and GATK ( 42 ) performed the variant calling.
- Full pipeline: quality control [FastQC] -> alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> normalisation [edgeR] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [edgeR, tidyverse] -> visualisation [ggplot2] -> stage not stated [SAMtools]

### DIDO is necessary for the adipogenesis that promotes diet-induced obesity. (PNAS 2024)

- DOI: 10.1073/pnas.2300096121 | PMCID: PMC10801893 | PMID: 38194457
- Evidence: Transcripts were mapped to a mouse reference genome (GRCm38/mm10 assembly) using BWA-MEM.
- Full pipeline: alignment/mapping [BWA, Picard] -> quantification [StringTie] -> stage not stated [DESeq2]

### Distinct transcription factor interactions drive HOXB13 activity in different stages of prostate cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2500327122 | PMCID: PMC12704779 | PMID: 41343677
- Version used: **0.7.17**
- Evidence: Paired-end reads were aligned to the hg38 genome build using BWA (v0.7.17-r1188) ( 51 ).
- Full pipeline: quality control [FastQC v0.11.9, MultiQC v1.11] -> alignment/mapping [BWA v0.7.17] -> quantification [ImageJ] -> normalisation [edgeR v3.36.0] -> dimensionality reduction/clustering [scikit-learn] -> visualisation [scikit-learn] -> stage not stated [BEDTools v2.30.0, GSVA, MACS2 v3.0.0a, Metascape]

### Recovery of infectious recombinant human norovirus using zebrafish embryos. (PNAS 2025)

- DOI: 10.1073/pnas.2526726122 | PMCID: PMC12704787 | PMID: 41343680
- Version used: **0.7.17**
- Evidence: Adapter sequences were trimmed using Cutadapt version 3.2, and the processed reads were aligned to the HuNoV reference genome (Norovirus GII.2 strain Env/CHN/2016/GII.P16-GII.2/BJSMQ, GenBank accession number: NC039476) using BWA version 0.7.17.
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt v3.2] -> alignment/mapping [BWA v0.7.17, Cutadapt v3.2] -> variant calling [BCFtools v1.9, Mutect2] -> stage not stated [GATK v4.2.0.0, Picard, SAMtools v1.11]

### Chromosomal deletions in banana somaclonal variants reveal negative regulators of immunity underlying &lt;i&gt;Fusarium&lt;/i&gt; wilt resistance. (PNAS 2025)

- DOI: 10.1073/pnas.2511842122 | PMCID: PMC12685060 | PMID: 41284879
- Version used: **2.1.1**
- Evidence: The clean reads were aligned to the DH Pahang v4 genome ( 29 ) or Cavendish genomes ( 36 , 37 ) using BWA (v2.1.1) ( 64 ).
- Full pipeline: read trimming [STAR v2.7.0f, Trimmomatic v0.39] -> alignment/mapping [BWA v2.1.1, DESeq2, MUSCLE, R, STAR v2.7.0f] -> variant calling [GATK] -> quantification [Trimmomatic v0.39] -> normalisation [deepTools v3.4.3] -> dimensionality reduction/clustering [clusterProfiler v3.12.0] -> differential/statistical testing [DESeq2, R]

### Genetic testing predicts appearance but not behavior in dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421752122 | PMCID: PMC12684939 | PMID: 41284863
- Evidence: A total of 3,285 FASTQ files (available on SRA under PRJNA675863) were aligned to the canFam4 (UU_Cfam_GSD_1.0 + ROSY) genome assembly using NVIDIA Clara Parabrick’s (version 4.0) fq2bam wrapper for BWA-MEM on the Sol supercomputer of Arizona State University ( 107 ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [ADMIXTURE, Docker, GCTA v1.94.1, Nextflow, PLINK v1.90b, pandas]

### Genomic and transcriptomic landscape of carcinogenesis in patients with gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS). (PNAS 2025)

- DOI: 10.1073/pnas.2427133122 | PMCID: PMC12595452 | PMID: 41171849
- Evidence: Briefly, sequenced reads were mapped to the human reference genome hg38 using BWA-MEM ( 42 ).
- Full pipeline: alignment/mapping [BWA, Picard, RSEM, SAMtools] -> variant calling [ANNOVAR] -> quantification [RSEM] -> dimensionality reduction/clustering [clusterProfiler v4.2.0] -> differential/statistical testing [R v2.10.0, clusterProfiler v4.2.0, edgeR v2.10.0] -> stage not stated [GATK v4.0, GSEA, Mutect2]

### Museum genomics suggests long-term population decline in a putatively extinct bumble bee. (PNAS 2025)

- DOI: 10.1073/pnas.2509749122 | PMCID: PMC12582279 | PMID: 41115198
- Version used: **0.7.17**
- Evidence: Trimmed reads were mapped to the B. affinis reference genome [GCF_024516045.1; ( 23 )] using bwa-mem v0.7.17 ( 78 ).
- Full pipeline: read trimming [BWA v0.7.17, Trimmomatic v0.39] -> alignment/mapping [BCFtools, BWA v0.7.17, IQ-TREE v2.3.6, MAFFT, PLINK, SAMtools v1.9] -> variant calling [VCFtools v0.1.16] -> differential/statistical testing [PLINK] -> stage not stated [BUSCO, GATK, QUAST, SPAdes]

### Evolutionary histories of functional mutations during the domestication and spread of &lt;i&gt;japonica&lt;/i&gt; rice in Asia. (PNAS 2025)

- DOI: 10.1073/pnas.2514614122 | PMCID: PMC12582302 | PMID: 41115193
- Version used: **0.7.17**
- Evidence: For modern genomes, we used a Nextflow v20.10.0 pipeline in which sequencing reads were aligned to the Shuhui498 v1.0 indica reference genome ( 99 ) using BWA v0.7.17 ( 100 ) in “mem” mode ( 101 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK, Nextflow v20.10.0] -> variant calling [PLINK v1.90] -> dimensionality reduction/clustering [R v4.3] -> stage not stated [VCFtools v1.6]

### Mitotic recombination events and single-base mutations induced by ultraviolet light in G1-arrested yeast cells. (PNAS 2025)

- DOI: 10.1073/pnas.2518046122 | PMCID: PMC12557804 | PMID: 41091767
- Evidence: Raw reads were aligned to the reference genome of S288c using BWA ( 39 ), and the resulting alignments were processed with Samtools ( 40 ) for format conversion, sorting, and indexing.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [VarScan]

### A species interaction kick-starts ecological speciation in allopatry. (PNAS 2025)

- DOI: 10.1073/pnas.2506625122 | PMCID: PMC12557528 | PMID: 41082661
- Evidence: Raw sequences sorted by individual were aligned to the threespine stickleback reference genome v5 using BWA ( 108 ).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [BCFtools, GATK, SAMtools, VCFtools, lme4]

### Distinct and convergent effects of &lt;i&gt;SF3B1&lt;/i&gt; mutations in human breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2505374122 | PMCID: PMC12541443 | PMID: 41055979
- Evidence: Reads were mapped to human genome (GRch38) with BWA ( 53 ).
- Full pipeline: quality control [FastQC] -> read trimming [Cutadapt v4.8] -> alignment/mapping [BWA, STAR v2.7.11a, featureCounts v2.0.6] -> variant calling [GATK] -> differential/statistical testing [DESeq2] -> visualisation [ggplot2] -> stage not stated [ANNOVAR, GSEA]

### Exceedingly low genetic diversity in snow leopards due to persistently small population size. (PNAS 2025)

- DOI: 10.1073/pnas.2502584122 | PMCID: PMC12541318 | PMID: 41055990
- Evidence: Mapping, using BWA-MEM ( 86 ), and SNP calling, using GATK ( 87 ), were performed by Gencove Inc., a service provider.
- Full pipeline: alignment/mapping [BWA, GATK] -> variant calling [BWA, GATK] -> dimensionality reduction/clustering [BCFtools, PLINK, VCFtools] -> stage not stated [R, SAMtools, SnpEff, ggplot2, ggpubr]

### Genetic, phenotypic, and environmental drivers of local adaptation and climate change-induced maladaptation in a migratory songbird. (PNAS 2025)

- DOI: 10.1073/pnas.2518497122 | PMCID: PMC12519128 | PMID: 41021811
- Version used: **0.7.17**
- Evidence: We then mapped reads to the yellow warbler reference genome (NCBI BioProject PRJNA777222) ( 64 ) using BWA 0.7.17 ( 65 ) with the bwa mem Snakemake wrapper (v1.23.3/bio/bwa/mem).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.17, GATK v4.1.6.0, SAMtools v1.16] -> variant calling [BCFtools v1.16, GATK v4.1.6.0] -> differential/statistical testing [GEMMA v0.98.3] -> stage not stated [BEDTools, Picard, R, Snakemake]

### Long-term evolutionary persistence of a cryptic color polymorphism in frogs. (PNAS 2025)

- DOI: 10.1073/pnas.2425898122 | PMCID: PMC12452913 | PMID: 40928876
- Evidence: After quality filtering, reads were aligned to the P. robeensis reference genome using bwa-mem ( 69 ).
- Full pipeline: alignment/mapping [BWA, HISAT2] -> variant calling [ANGSD] -> normalisation [edgeR] -> stage not stated [PLINK, R, StringTie, limma, phytools]

### De novo rates of a &lt;i&gt;Trypanosoma&lt;/i&gt;-resistant mutation in two human populations. (PNAS 2025)

- DOI: 10.1073/pnas.2424538122 | PMCID: PMC12415191 | PMID: 40854136
- Evidence: Approved sequences were mapped to the APOL1 reference sequence (obtained by Sanger-sequencing aliquots from the matching donor samples) using BWA ( 107 ) with parameters -M -t.
- Full pipeline: read trimming [Cutadapt, Trimmomatic] -> alignment/mapping [BWA]

### Aphid herbivory on macrophytes drives adaptive evolution in an aquatic community via indirect effects. (PNAS 2025)

- DOI: 10.1073/pnas.2502742122 | PMCID: PMC12403121 | PMID: 40838887
- Evidence: Raw data were quality-checked and trimmed using TrimGalore v0.6.1 ( 29 ), and reads were mapped toward the D. magna reference genome ( 30 ) using BWA ( 31 ) and SAMtools ( 32 ).
- Full pipeline: quality control [BWA, SAMtools, Trim Galore v0.6.1] -> read trimming [BWA, SAMtools, Trim Galore v0.6.1] -> alignment/mapping [BWA, SAMtools, Trim Galore v0.6.1] -> differential/statistical testing [lme4]

### Synergistic action of specialized metabolites from divergent biosynthesis in the human oral microbiome. (PNAS 2025)

- DOI: 10.1073/pnas.2504492122 | PMCID: PMC12403116 | PMID: 40828023
- Evidence: We screened three previously published metagenomic datasets of caries and caries-free plaque samples for sequence similarity matches with the BGCs via BWA-MEM ( 35 ) and DESeq2 ( 36 ).
- Full pipeline: read trimming [Trimmomatic] -> stage not stated [BWA, DESeq2]

### Inbreeding reduces fitness in spatially structured populations of a threatened rattlesnake. (PNAS 2025)

- DOI: 10.1073/pnas.2501745122 | PMCID: PMC12403008 | PMID: 40825128
- Version used: **07.17**
- Evidence: Briefly, we aligned sequencing data to the eastern massasauga reference genome ( 47 ) using BWA mem v.
- Full pipeline: alignment/mapping [BWA v07.17, SAMtools v1.9] -> variant calling [BCFtools v1.9.64] -> stage not stated [R]

### TRIM24 as a therapeutic target in endocrine treatment-resistant breast cancer. (PNAS 2025)

- DOI: 10.1073/pnas.2507571122 | PMCID: PMC12377727 | PMID: 40815626
- Version used: **0.5.10**
- Evidence: All samples were aligned to reference genome Hg38/GRCh38 using Burrows-Wheeler Aligner [BWA v0.5.10 ( 52 )].
- Full pipeline: quality control [DESeq2] -> alignment/mapping [BWA v0.5.10, HISAT2, HTSeq, SAMtools] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [R, clusterProfiler] -> visualisation [SAMtools] -> stage not stated [GSEA, MACS2 v2.1.2, deepTools v2.5.3]

### DNA polymerase β suppresses somatic indels at CpG dinucleotides in developing cortical neurons. (PNAS 2025)

- DOI: 10.1073/pnas.2506846122 | PMCID: PMC12377747 | PMID: 40802685
- Evidence: Sequence reads were mapped to a mouse reference genome (mm10) using the Burrows–Wheeler aligner with the maximal exact matches (BWA-MEM) algorithm.
- Full pipeline: alignment/mapping [BWA, GATK v4.1.0.0, Picard, SAMtools] -> variant calling [GATK v4.1.0.0, SAMtools] -> stage not stated [HOMER]

### Genomes of nitrogen-fixing eukaryotes reveal an alternate path for organellogenesis. (PNAS 2025)

- DOI: 10.1073/pnas.2507237122 | PMCID: PMC12377750 | PMID: 40794833
- Version used: **0.7.17**
- Evidence: Axenic Illumina data were mapped to the assembly with BWA v0.7.17-r1188 ( 93 ).
- Full pipeline: read trimming [HISAT2 v2.1.0, fastp] -> alignment/mapping [BWA v0.7.17, HISAT2 v2.1.0, SAMtools v1.16.1, deepTools v3.3.1, minimap2] -> normalisation [deepTools v3.3.1] -> dimensionality reduction/clustering [clusterProfiler] -> differential/statistical testing [NanoPlot v1.30.1, QUAST v5.2.0, clusterProfiler] -> stage not stated [BEDTools v2.30.0, BUSCO v5.3.2, RepeatMasker, eggNOG]

### The fetal hydrops-associated single-residue mutation L322P disrupts mechanical but not chemical activation of the PIEZO1 ion channel. (PNAS 2025)

- DOI: 10.1073/pnas.2503793122 | PMCID: PMC12377734 | PMID: 40789030
- Evidence: ...q X platform, raw FASTQ data were generated and processed through the subsequent steps: a) map the short reads to a reference genome (hg19) using the BWA software (v0.7.12-r1039) ( 46 ); b) use the SAMtools software (v0.1.18) to sort the short sequences and convert the format of the data; c) use the Picard software (v1.134) ( http://broadinstitute.github.io/picard/ ) to mark duplicate reads; d) us...
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [ANNOVAR, AlphaFold, BEDTools, GATK v3.7, ImageJ, Picard]

### A genomic test of sex-biased dispersal in white sharks. (PNAS 2025)

- DOI: 10.1073/pnas.2507931122 | PMCID: PMC12358869 | PMID: 40758892
- Evidence: Raw reads were trimmed using trimmomatic-0.39 ( 43 ), aligned against the de novo reference genome ( SI Appendix , Supplementary Note 4 ) using the bwa-mem algorithm ( 44 ), and PCR duplicates were tagged using “MarkDuplicates” of Picard toolkit v2.25.6 ( http://broadinstitute.github.io/picard/ ) ( 45 ).
- Full pipeline: read trimming [BWA, Picard] -> alignment/mapping [BWA, Picard] -> variant calling [GATK v4.0] -> dimensionality reduction/clustering [R] -> stage not stated [BCFtools v1.9, PLINK]

### Common inherited loss-of-function mutations in the innate sensor NOD2 contribute to exceptional immune response to cancer immunotherapy. (PNAS 2025)

- DOI: 10.1073/pnas.2314258122 | PMCID: PMC12280981 | PMID: 40623177
- Version used: **0.7.10**
- Evidence: Raw reads were aligned to the hs37d5 reference using BWA-MEM v0.7.10-r789, sorted and duplicate-marked with Novosort v1.03.01 (Novocraft Technologies).
- Full pipeline: alignment/mapping [BWA v0.7.10, SAMtools v1.14, minimap2 v2.18] -> variant calling [BCFtools v1.14] -> registration [GATK] -> stage not stated [Kraken2 v2.1.1, R v4.2.2, VEP, fastp v0.20.1, tidyverse]

### Genome analyses suggest recent speciation and postglacial isolation in the Norwegian lemming. (PNAS 2025)

- DOI: 10.1073/pnas.2424333122 | PMCID: PMC12280882 | PMID: 40587810
- Evidence: For the nine modern samples, we first trimmed the sequencing adapters from the raw reads using Trimmomatic v0.32 and mapped them to the MITObim-reconstructed mitogenome using BWA mem ( 63 ).
- Full pipeline: read trimming [BUSCO v3.0.2, BWA, QUAST v4.5.4, Trimmomatic v0.32] -> alignment/mapping [BWA, GATK, SAMtools v1.8, Trimmomatic v0.32] -> variant calling [BCFtools v1.8] -> registration [GATK, SAMtools v1.8] -> structure determination [BWA, Trimmomatic v0.32] -> stage not stated [ANGSD, BEDTools, RepeatMasker, SnpEff]

### The importance of small-island populations for the long-term survival of endangered large-bodied insular mammals. (PNAS 2025)

- DOI: 10.1073/pnas.2422690122 | PMCID: PMC12232422 | PMID: 40553499
- Evidence: Each paired-end fastq files sample was trimmed with AdapterRemoval ( 32 ) and aligned to the using the BWA MEM ( 33 ) to a closely related reference genome, i.e., water buffalo and babirusa, and distantly related reference genome, i.e., cow and pig, for anoa and babirusa, respectively, constructing each to a set of close relative alignment and distant relative alignment ( SI Appendix , Supplementa...
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> stage not stated [ANGSD, QGIS, R, VEP]

### Longitudinal sequencing reveals polygenic and epistatic nature of genomic response to selection. (PNAS 2025)

- DOI: 10.1073/pnas.2410452122 | PMCID: PMC12207516 | PMID: 40531879
- Evidence: Following sequencing, we mapped reads to the D. melanogaster reference genome (v6.14) using BWA ( 3 ) 53 , retained only uniquely mapped reads, and removed PCR generated duplicates using Picard (“Picard Toolkit,” 2019).
- Full pipeline: read trimming [Trimmomatic v0.32] -> alignment/mapping [BWA, Picard] -> variant calling [DESeq2] -> dimensionality reduction/clustering [PLINK] -> stage not stated [R, emmeans]

### SARS-CoV-2 nsp15 enhances viral virulence by subverting host antiviral defenses. (PNAS 2025)

- DOI: 10.1073/pnas.2426528122 | PMCID: PMC12184426 | PMID: 40504150
- Evidence: Clean reads were mapped to the Genome Reference Consortium Human Build 38 (GRCh38, accessed from the Ensembl database http://www.ensembl.org/ ) using STAR ( 53 ) and to the SARS-CoV-2 genome using BWA-MEM ( 54 ).
- Full pipeline: quality control [FastQC] -> read trimming [FastQC] -> alignment/mapping [BWA] -> dimensionality reduction/clustering [GSEA, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [pheatmap] -> stage not stated [ImageJ, featureCounts]

### The highly conserved intron of tyrosine tRNA is critical for &lt;sup&gt;m1&lt;/sup&gt;A58 modification and controls the integrated stress response. (PNAS 2025)

- DOI: 10.1073/pnas.2502364122 | PMCID: PMC12168002 | PMID: 40478875
- Evidence: Bases were called using Guppy v3.0.3 and aligned with BWA-MEM to a custom reference of the 42 yeast isoacceptors encoded in the yeast nuclear genome.
- Full pipeline: alignment/mapping [BWA] -> stage not stated [AlphaFold, ChimeraX]

### Population sequencing for phylogenetic diversity and transmission analyses. (PNAS 2025)

- DOI: 10.1073/pnas.2424797122 | PMCID: PMC12167970 | PMID: 40460116
- Version used: **0.7.17**
- Evidence: The reads from the single colonies underwent quality control using fastp v0.20.1 ( 35 ) using default parameters and the SNPs were called using NASP v1.2.0 ( 36 ) which mapped the reads to the reference (accession NC_007795 ) using BWA-MEM v0.7.17 ( 37 ) and called the SNPs using the GATK v3.8 UnifiedGenotyper ( 26 , 38 ) method.
- Full pipeline: quality control [BWA v0.7.17, GATK, fastp v0.20.1] -> alignment/mapping [BWA v0.7.17, GATK, fastp v0.20.1] -> variant calling [BWA v0.7.17, fastp v0.20.1]

### The white lupin CCR1 receptor-like kinase controls systemic Autoregulation of Cluster Root and Nodule Development. (PNAS 2025)

- DOI: 10.1073/pnas.2418411122 | PMCID: PMC12130874 | PMID: 40402250
- Version used: **0.7.17**
- Evidence: We used BWA-MEM v0.7.17 ( 50 ) to map reads to the white lupin reference genome.
- Full pipeline: read trimming [Cutadapt v1.15] -> alignment/mapping [BWA v0.7.17] -> variant calling [GATK] -> normalisation [R] -> differential/statistical testing [R] -> visualisation [PyMOL v2.5.4] -> stage not stated [AlphaFold, BLAST, ColabFold v1.5.5, Picard]

### Partner dependency alters patterns of coevolutionary selection in mutualisms. (PNAS 2025)

- DOI: 10.1073/pnas.2424983122 | PMCID: PMC12130895 | PMID: 40397677
- Evidence: All samples were aligned to the yeast reference genome S. cerevisiae S288C after removing the adaptor sequences and low-quality reads using BWA (V.0.7.17) ( 51 ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> stage not stated [BCFtools, Python, R, SnpEff, VCFtools, emmeans, lme4]

### Ancient DNA suggests a historical demographic decline and genetic erosion in the Atlantic bluefin tuna. (PNAS 2025)

- DOI: 10.1073/pnas.2409302122 | PMCID: PMC12130816 | PMID: 40392844
- Evidence: Forward and reverse reads were collapsed in PALEOMIX with AdapterRemoval v1.5 ( 105 ) and aligned to our pseudochromosome bluefin tuna reference using BWA mem ( 102 ).
- Full pipeline: read trimming [BWA, SAMtools v1.7, Trimmomatic v0.39] -> alignment/mapping [BWA, SAMtools v1.7] -> registration [GATK v3.7] -> differential/statistical testing [R] -> stage not stated [PLINK v1.90b, Picard, VCFtools v0.1.16]

### RNA sequencing analysis of viromes of &lt;i&gt;Aedes albopictus&lt;/i&gt; and &lt;i&gt;Aedes vexans&lt;/i&gt; collected from NEON sites. (PNAS 2025)

- DOI: 10.1073/pnas.2403591122 | PMCID: PMC12107137 | PMID: 40354533
- Evidence: Coverage of contigs was calculated by aligning trimmed reads with Burrows-Wheeler Aligner Minimum Exact Match v0.7.17-r1188 [BWA-MEM ( 42 )] and calculating read coverage with SAMtools v1.9 ( 37 ).
- Full pipeline: read trimming [BWA, fastp v0.21.1] -> alignment/mapping [BLAST, BWA, Kraken2, SAMtools] -> stage not stated [Bowtie2, R]

### Host use drives convergent evolution in clownfish. (PNAS 2025)

- DOI: 10.1073/pnas.2419716122 | PMCID: PMC12054820 | PMID: 40279387
- Evidence: 83.3 Mbp; https://doi.org/10.5061/dryad.nv1sv ; ( 59 )] using BWA [v.0.4.15; ( 63 )].
- Full pipeline: quality control [FastQC v0.11.5, Trimmomatic v0.36] -> read trimming [Trimmomatic v0.36] -> alignment/mapping [MAFFT, RAxML, SAMtools] -> variant calling [GATK] -> structure determination [MAFFT, RAxML, phytools] -> visualisation [R] -> stage not stated [BEAST, BWA]

### Biallelic variants in the conserved ribosomal protein chaperone gene &lt;i&gt;PDCD2&lt;/i&gt; are associated with hydrops fetalis and early pregnancy loss. (PNAS 2025)

- DOI: 10.1073/pnas.2426078122 | PMCID: PMC12012559 | PMID: 40208938
- Version used: **0.7.17**
- Evidence: The sequences were then aligned to the human reference assembly [NCBI GRCh38 (GCA_000001405.15)] with the Burrows-Wheeler Aligner (BWA mem, v0.7.17-r1188) ( 54 ).
- Full pipeline: alignment/mapping [BWA v0.7.17] -> stage not stated [GATK, VEP v103.0, fastp v0.21.0]

### Genomics highlight an underestimation of phenology sensitivity to the urban heat island effect. (PNAS 2025)

- DOI: 10.1073/pnas.2408564122 | PMCID: PMC11962471 | PMID: 40100635
- Evidence: To align sequence reads to the Q. rubra reference genome [ https://phytozome-next.jgi.doe.gov/info/Qrubra_v2_1 ; ( 22 )], we indexed the reference genome and aligned the sequences to the assembly using BWA-MEM ( 40 ) and generated binary alignment map (BAM) files using SAMtools ( 41 ).
- Full pipeline: alignment/mapping [BWA, SAMtools] -> variant calling [freebayes] -> stage not stated [PLINK, R]

### Iguanas rafted more than 8,000 km from North America to Fiji. (PNAS 2025)

- DOI: 10.1073/pnas.2318622122 | PMCID: PMC11962422 | PMID: 40096595
- Version used: **0.7.17**
- Evidence: We mapped the cleaned reads to our target loci with BWA-MEM 0.7.17-r1188 ( 109 ).
- Full pipeline: quality control [FastQC v0.11.8, MultiQC v1.1] -> alignment/mapping [BWA v0.7.17, Picard v2.23.4, SAMtools] -> registration [GATK v3.6] -> differential/statistical testing [R] -> stage not stated [ANGSD v0.933, BEAST, RAxML]

### A mechanistic basis for genetic assimilation in natural fly populations. (PNAS 2025)

- DOI: 10.1073/pnas.2415982122 | PMCID: PMC11929479 | PMID: 40063800
- Evidence: Briefly, reads were aligned to the D. melanogaster reference genome dm6 using the BWA software ( 54 ).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.4.2, Clustal Omega, STAR v2.7.0] -> quantification [featureCounts] -> stage not stated [BEDTools v2.30.0, DESeq2, GATK, MACS2, R]

### Dynamic investigation of hypoxia-induced L-lactylation. (PNAS 2025)

- DOI: 10.1073/pnas.2404899122 | PMCID: PMC11912421 | PMID: 40030031
- Evidence: Reads were mapped to the reference genome by BWA ( 46 ).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [Fiji, ImageJ, MACS2]

### tRNA selectivity during ribosome-associated quality control regulates the critical sterility-inducing temperature in two-line hybrid rice. (PNAS 2025)

- DOI: 10.1073/pnas.2417526122 | PMCID: PMC11831146 | PMID: 39913205
- Evidence: Following the SIMM pipeline as previously described ( 39 ), low-quality reads were filtered out, and the resulting clean reads were aligned to the Nipponbare reference genome (MSU7) using BWA ( 52 ).
- Full pipeline: alignment/mapping [BWA, Bowtie2 v2.2.9, Clustal Omega] -> structure determination [Cutadapt v1.18] -> stage not stated [ImageJ, RoseTTAFold]

### Evolutionary adaptation under climate change: &lt;i&gt;Aedes&lt;/i&gt; sp. demonstrates potential to adapt to warming. (PNAS 2025)

- DOI: 10.1073/pnas.2418199122 | PMCID: PMC11745351 | PMID: 39772738
- Version used: **0.7.12**
- Evidence: We then aligned these reads to the scaffolded reference genome using BWA-MEM v0.7.12, with default parameters ( 138 ).
- Full pipeline: read trimming [Trimmomatic v0.39] -> alignment/mapping [BWA v0.7.12, RepeatMasker v2.0.1] -> differential/statistical testing [R, lme4] -> stage not stated [AUGUSTUS, BCFtools v1.18, GCTA, ImageJ, VCFtools v0.1.16]

### Endonuclease G promotes hepatic mitochondrial respiration by selectively increasing mitochondrial tRNA<sup>Thr</sup> production. (PNAS 2025)

- DOI: 10.1073/pnas.2411298122 | PMCID: PMC11725929 | PMID: 39752519
- Version used: **0.7.10**
- Evidence: The raw reads (5.8 to 7.3 million reads) in fastq format were mapped to mm10 mouse chromosome M reference sequence by BWA (0.7.10-r789) with mem algorithm.
- Full pipeline: quality control [FastQC, HISAT2] -> read trimming [FastQC, HISAT2] -> alignment/mapping [BWA v0.7.10, FastQC, HISAT2, RSEM, STAR] -> quantification [ImageJ] -> normalisation [DESeq2, R] -> differential/statistical testing [DESeq2, GSEA, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [SAMtools v0.1.19]

### Hydroxychloroquine prevents resistance and potentiates the antitumor effect of SHP2 inhibition in NF1-associated malignant peripheral nerve sheath tumors. (PNAS 2025)

- DOI: 10.1073/pnas.2407745121 | PMCID: PMC11725864 | PMID: 39793045
- Evidence: In summary, this assay consists of the following standard workflow: Reads are mapped using BWA MEM and indel-realigned and baseQ-recalibrated using GATK; then mutations are called using MuTect (v1.1.4) and SomaticIndelDetector (GATK v2.3.9).
- Full pipeline: quality control [FastQC, STAR] -> alignment/mapping [BWA, FastQC, GATK v2.3.9, Mutect2 v1.1.4, STAR, featureCounts] -> quantification [ImageJ] -> registration [BWA, GATK v2.3.9, Mutect2 v1.1.4] -> differential/statistical testing [DESeq2, GSEA]

### Family relations of Moche elite burials on the North Coast of Peru (~500 CE): Analyses of the Señora de Cao and relatives. (PNAS 2025)

- DOI: 10.1073/pnas.2416321121 | PMCID: PMC11725780 | PMID: 39715432
- Version used: **0.6.1**
- Evidence: All shotgun-sequenced reads went into mapping with BWA (v0.6.1) ( 49 ) against the human genome reference GRCh37/hg19.
- Full pipeline: quality control [ANGSD] -> alignment/mapping [BWA v0.6.1]

### Genomic reconstruction of upland cotton domestication uncovers staged selection, gene flow, and flowering-time adaptation. (PNAS 2026)

- DOI: 10.1073/pnas.2601246123 | PMCID: PMC13320693 | PMID: 42330268
- Version used: **0.7.17**
- Evidence: Clean reads were aligned to the Texas Marker-1 (TM-1) genome (CR1_v1: https://www.cottongen.org/node/13354433 ) ( 65 ) using BWA-MEM (v0.7.17-r1188 v0.7.17-r1188) ( 66 ), with variants called by GATK (v3.7.0) ( 67 ).
- Full pipeline: alignment/mapping [BWA v0.7.17, GATK v3.7.0, HISAT2 v2.2.1, featureCounts v2.0.1] -> quantification [HISAT2 v2.2.1, featureCounts v2.0.1] -> dimensionality reduction/clustering [ADMIXTURE, IQ-TREE, PLINK v1.9, R] -> stage not stated [ImageJ, SnpEff v4.3t, VCFtools v0.1.16]

### Ultrarapid MC1R protein and associated plumage color evolution in the domestic chicken. (PNAS 2026)

- DOI: 10.1073/pnas.2605288123 | PMCID: PMC13273276 | PMID: 42268884
- Version used: **0.7.17**
- Evidence: Clean reads were aligned to the red junglefowl reference genome (GRCg6a, GCA_000002315.5) with BWA-MEM (version 0.7.17-r1188) ( 48 ) algorithm with default settings.
- Full pipeline: quality control [FastQC v0.11.8] -> alignment/mapping [BWA v0.7.17] -> registration [GATK v3.7] -> stage not stated [Picard v2.18.6, PyMOL, SAMtools v1.9, VCFtools v0.1.16]

### Virus-induced transgene- and tissue culture-free heritable genome editing in tomato. (PNAS 2026)

- DOI: 10.1073/pnas.2530029123 | PMCID: PMC13250589 | PMID: 42241111
- Version used: **0.7.17**
- Evidence: Single-end reads were processed by adapter trimming with Trim Galore using default parameters, and the resulting reads were aligned to the target genomic region with BWA (v0.7.17) employing the BWA-MEM algorithm.
- Full pipeline: read trimming [BWA v0.7.17, Trim Galore] -> alignment/mapping [BWA v0.7.17, Trim Galore] -> stage not stated [R]

### Persistent trade-offs balance competition and colonization across centuries. (PNAS 2026)

- DOI: 10.1073/pnas.2534310123 | PMCID: PMC13250502 | PMID: 42228529
- Evidence: Host-derived reads were removed by mapping all merged reads to the A. thaliana TAIR10 reference genome ( 57 ) using BWA aln v0.7.17 ( 58 ), with the seed disabled to improve alignment of damaged historical reads ( 26 ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [lme4] -> stage not stated [DESeq2, IQ-TREE v2.1.4, R, emmeans]

### Evolution of genome-wide barriers to gene flow during complex speciation in rattlesnakes. (PNAS 2026)

- DOI: 10.1073/pnas.2609058123 | PMCID: PMC13214041 | PMID: 42166239
- Evidence: We mapped filtered reads to the C. pyrrhus reference genome using BWA mem ( 121 ), and called variants using GATK ( 122 ).
- Full pipeline: read trimming [BWA, GATK] -> alignment/mapping [BWA, GATK] -> dimensionality reduction/clustering [ADMIXTURE] -> stage not stated [BUSCO]

### Pneumococcal membrane particles promote serotype-independent cellular and humoral immunity and protect against pneumococcal colonization. (PNAS 2026)

- DOI: 10.1073/pnas.2537226123 | PMCID: PMC13214003 | PMID: 42154558
- Version used: **0.7.19**
- Evidence: For reads with no detectable pspA , reads were mapped to reference nucleotide sequences using BWA-MEM v0.7.19 ( 44 ) with default parameters.
- Full pipeline: alignment/mapping [BCFtools, BWA v0.7.19, SAMtools v1.22] -> stage not stated [SPAdes v3.15.5]

### Layer-specific genetic variation unlocks secondary metabolite diversity in long-lived clonal peppermint. (PNAS 2026)

- DOI: 10.1073/pnas.2532794123 | PMCID: PMC13214039 | PMID: 42101988
- Version used: **0.7.17**
- Evidence: The reads were then mapped using BWA mem version 0.7.17 ( 59 ) to create sam mapping files to the largest 102 scaffolds of the BM genome assembly.
- Full pipeline: alignment/mapping [BLAST, BWA v0.7.17, HTSeq, STAR v2.7.11b, featureCounts v1.6.3] -> variant calling [emmeans, tidyverse] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, emmeans, tidyverse] -> visualisation [minimap2] -> stage not stated [BUSCO, hifiasm, pheatmap]

### Rhesus macaques with an &lt;i&gt;OPA1&lt;/i&gt; mutation demonstrate features of autosomal dominant optic atrophy. (PNAS 2026)

- DOI: 10.1073/pnas.2509165123 | PMCID: PMC13099570 | PMID: 41984835
- Evidence: BWA mem was used to align the sequencing reads to the rhesus reference genome assembly (Mmul_8.0.1 or Mmul_10).
- Full pipeline: alignment/mapping [BWA] -> stage not stated [ANNOVAR, GATK, ImageJ]

### A plasma-based DNA test for quantification of disease burden in acute myeloid leukemia patients undergoing bone marrow transplantation. (PNAS 2026)

- DOI: 10.1073/pnas.2537987123 | PMCID: PMC13099560 | PMID: 41980102
- Evidence: FASTQ files were generated using Illumina’s bcl2fastq or by Complete Genomic’s Ztron Lite Server, then aligned to hg38 reference genome with BWA-MEM with default settings ( 36 ).
- Full pipeline: alignment/mapping [BWA] -> dimensionality reduction/clustering [Picard] -> stage not stated [Mutect2]

### STAG2 loss amplifies EWS-FLI1-driven microsatellite enhancer activity promoting Ewing sarcoma aggressiveness. (PNAS 2026)

- DOI: 10.1073/pnas.2537425123 | PMCID: PMC13079922 | PMID: 41950086
- Evidence: Briefly, reads were aligned using BWA mem with default settings ( 44 ).
- Full pipeline: read trimming [Picard] -> alignment/mapping [BWA] -> normalisation [fgsea] -> differential/statistical testing [Bioconductor, fgsea, limma] -> visualisation [ggplot2, tidyverse] -> stage not stated [BEDTools, DESeq2, GSEA, MACS2]

### A high-coverage Neandertal genome from the Altai Mountains reveals population structure among Neandertals. (PNAS 2026)

- DOI: 10.1073/pnas.2534576123 | PMCID: PMC13037865 | PMID: 41871248
- Evidence: Reads were mapped to the revised human reference genome (hg19) using Burrows-Wheeler Aligner BWA ( 49 ) with parameters “-n 0.01 –o 2 –l 16500” ( 13 ).
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [BEAST]

### Early colonization before inundation consistent with northern glacial refugia in Southern Doggerland revealed by sedimentary ancient DNA. (PNAS 2026)

- DOI: 10.1073/pnas.2508402123 | PMCID: PMC12994208 | PMID: 41805578
- Evidence: For individual species ( Quercus , Alnus , Tilia , Corylus , Salix, and Ulmus ) reads were subsampled from the BLAST dataset using MEGAN and mapped against their respective genomes ( Quercus : GCF_932294415.1; Alnus : GCF_958979055.1; Tilia GCA_020138205.1; Corylus : GCF_901000735.1; Salix : GCA_027405865.1; Ulmus : GCA_010015005.3) with bwa-0.7.15 using the BWA-MEM algorithm ( 78 ).
- Full pipeline: quality control [FastQC v0.11.6] -> read trimming [FastQC v0.11.6] -> alignment/mapping [BWA] -> differential/statistical testing [R] -> stage not stated [BLAST]

### A factor integrating transcription and repression of surface antigen genes in African trypanosomes. (PNAS 2026)

- DOI: 10.1073/pnas.2531377123 | PMCID: PMC12890818 | PMID: 41632842
- Evidence: Reads were aligned to the predicted transcriptome using BWA-MEM with default settings, then filtered to only uniquely mapped reads using samtools view with the command line flags -q 10, -F 0x504 and -f 0x02.
- Full pipeline: alignment/mapping [BWA, SAMtools] -> quantification [edgeR] -> differential/statistical testing [edgeR] -> stage not stated [BLAST, ImageJ]

### The Japanese Archipelago sheltered cave lions, not tigers, during the Late Pleistocene. (PNAS 2026)

- DOI: 10.1073/pnas.2523901123 | PMCID: PMC12890994 | PMID: 41587328
- Version used: **0.7.17**
- Evidence: The resulting clean reads were mapped to mitochondrial reference genomes of cave lion, modern lion, and tiger (GenBank accession numbers: KX258452.1 and OK512998.1 , NC_028302.1 , and KP202268.1 ) using BWA-backtrack algorithm implemented in BWA v0.7.17 ( 78 ).
- Full pipeline: read trimming [Cutadapt v3.2] -> alignment/mapping [ANGSD, BWA v0.7.17, SAMtools v1.11] -> stage not stated [MAFFT v7.505, Python]

### Mutation rate variability in viral populations: Implications for lethal mutagenesis. (PNAS 2026)

- DOI: 10.1073/pnas.2523734123 | PMCID: PMC12799177 | PMID: 41512024
- Version used: **0.7.17**
- Evidence: Sequence reads were trimmed using cutadapt (Version 1.18) ( 46 ) and aligned to the A/Netherlands/499/2017 genome sequence using BWA (version 0.7.17) ( 47 ).
- Full pipeline: read trimming [BWA v0.7.17, Cutadapt] -> alignment/mapping [BWA v0.7.17, Cutadapt]

### &lt;i&gt;Chlamydomonas&lt;/i&gt; chloroplast genes tolerate compression of the genetic code to just 51 codons. (PNAS 2026)

- DOI: 10.1073/pnas.2506263123 | PMCID: PMC12799115 | PMID: 41493811
- Evidence: Raw reads were trimmed to quality score 20, mapped to the reference sequence using Unipro UGENE 52.0 BWA-MEM mapping tool and nucleotide variants were counted ( 53 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [BWA] -> stage not stated [Flye]

### Deep evolutionary conservation of a sex-determining locus without sequence homology. (PNAS 2026)

- DOI: 10.1073/pnas.2522417123 | PMCID: PMC12799146 | PMID: 41490485
- Version used: **0.7.18**
- Evidence: Variant calling for 22 species using individual female resequencing data ( SI Appendix , Table S2 ) was carried out by aligning reads with BWA v0.7.18 ( 49 ), removing PCR duplicates with sambamba markdup v1.2.1 ( 50 ), and calling variants with FreeBayes v1.0.2 ( 51 ) with clustering disabled.
- Full pipeline: alignment/mapping [BWA v0.7.18, freebayes v1.0.2] -> variant calling [BWA v0.7.18, IQ-TREE v2.3.6, SPAdes v3.15.2, freebayes v1.0.2] -> dimensionality reduction/clustering [BWA v0.7.18, freebayes v1.0.2] -> structure determination [IQ-TREE v2.3.6] -> stage not stated [BCFtools v1.21, PLINK v1.9, R v4.4, VCFtools v0.1.16]

### The contribution of historical processes to contemporary extinction risk in placental mammals. (Science 2023)

- DOI: 10.1126/science.abn5856 | PMCID: PMC10184782 | PMID: 37104572
- Version used: **0.7.15**
- Evidence: Briefly, we mapped paired-end sequencing data to the respective genome assemblies using BWA mem (version 0.7.15)( 57 ), marked and removed optical duplicates, and called heterozygous variants using the HaplotypeCaller module of the GATK software suite (version 3.6)( 58 ).
- Full pipeline: alignment/mapping [BWA v0.7.15] -> variant calling [BWA v0.7.15] -> differential/statistical testing [R] -> stage not stated [GATK, SnpEff v5.0e, scikit-learn v1.0.2]

### Phage-triggered reverse transcription assembles a toxic repetitive gene from a noncoding RNA. (Science 2024)

- DOI: 10.1126/science.adq3977 | PMCID: PMC12039810 | PMID: 39208082
- Evidence: Reads were trimmed and mapped to the expression plasmid, host genome, and T5 phage using BWA-MEM ( 51 ).
- Full pipeline: read trimming [BWA] -> alignment/mapping [AlphaFold, BWA, ColabFold, Python] -> quantification [RepeatMasker] -> registration [MAFFT] -> structure determination [PHENIX] -> visualisation [Python] -> stage not stated [CTFFIND, MotionCor2, RELION, Topaz, TrackMate]

### Evolution and host-specific adaptation of &lt;i&gt;Pseudomonas aeruginosa&lt;/i&gt;. (Science 2024)

- DOI: 10.1126/science.adi0908 | PMCID: PMC7618370 | PMID: 38963857
- Evidence: Variants were called by mapping reads against the P. aeruginosa PAO1 reference genome (accession number AE004091.2 ) using the multiple_mappings_to_bam 1.6 pipeline with default parameters ( https://github.com/sanger-pathogens/bact-gen-scripts ) employing BWA ( 63 ) for mapping followed by stringent QC filtering and removing samples with an excess number of minority variants.
- Full pipeline: quality control [BWA] -> alignment/mapping [BWA, kallisto] -> quantification [DESeq2, kallisto] -> normalisation [DESeq2] -> dimensionality reduction/clustering [DESeq2] -> differential/statistical testing [DESeq2] -> visualisation [Cytoscape] -> stage not stated [BEAST v6.6, RAxML v8.2.12, STRING db]

### Diverse somatic genomic alterations in single neurons in chronic traumatic encephalopathy. (Science 2025)

- DOI: 10.1126/science.adu1351 | PMCID: PMC12594281 | PMID: 41166474
- Version used: **0.7.15**
- Evidence: Read mapping and BAM file generation for bulk and PTA data BWA (v0.7.15) ( 44 ) was first used to map reads from bulk WGS and PTA scWGS data onto the human reference genome (GRCh37 with decoy) with default parameters.
- Full pipeline: alignment/mapping [BEDTools, BWA v0.7.15, SAMtools, minimap2 v2.12] -> registration [GATK, Picard v2.8.0] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [BEDTools, R, lme4 v1.1] -> stage not stated [ANNOVAR, Seurat v4.0.5]

### Functional maps of a genomic locus reveal confinement of an enhancer by its target gene. (Science 2025)

- DOI: 10.1126/science.ads6552 | PMCID: PMC7618358 | PMID: 40966339
- Evidence: Sequences were mapped to mm10 reference genome using the BWA alignment tool (0.7.17-r1188) after indexing the mm10 reference genome.
- Full pipeline: alignment/mapping [BWA] -> quantification [deepTools v3.0] -> normalisation [deepTools v3.0] -> visualisation [Signac] -> stage not stated [BCFtools v1.9, MACS2, SnpEff v4.3p]

### Platelets sequester extracellular DNA, capturing tumor-derived and free fetal DNA. (Science 2025)

- DOI: 10.1126/science.adp3971 | PMCID: PMC7618233 | PMID: 40811534
- Version used: **0.7.17**
- Evidence: Reads were adaptor- and quality-trimmed using Trim Galore!( 69 ) (v0.6.5) and aligned to the GATK Genome Reference Consortium Human Build 38 (GRCh38)( 70 ) using bwa-mem (v0.7.17)( 71 ).
- Full pipeline: quality control [FastQC v0.11.8] -> read trimming [BWA v0.7.17, GATK, Trim Galore] -> alignment/mapping [BWA v0.7.17, GATK, Picard, Trim Galore] -> structure determination [ImageJ v2.1.0] -> visualisation [ggplot2] -> stage not stated [BEDTools, CellProfiler v4.0.7, Mutect2 v4.1.7.0, SAMtools v1.13.0, Strelka v2.9.10]

### Introgression dynamics of sex-linked chromosomal inversions shape the Malawi cichlid radiation. (Science 2025)

- DOI: 10.1126/science.adr9961 | PMCID: PMC7617772 | PMID: 40504893
- Evidence: We aligned all sequencing data to the A. calliptera reference genome (fAstCal1.2; RefSeq: GCF_900246225.1) using BWA-MEM ( 79 ) and called variants according to the bcftools paradigm ( 80 ).
- Full pipeline: quality control [SnpEff] -> alignment/mapping [BCFtools, BWA] -> differential/statistical testing [ANGSD, GEMMA]

### Systematic identification of Y-chromosome gene functions in mouse spermatogenesis. (Science 2025)

- DOI: 10.1126/science.ads6495 | PMCID: PMC7617377 | PMID: 39847625
- Evidence: Resulting FastQ reads were aligned to the reference genome using BWA ( Fig.
- Full pipeline: alignment/mapping [BLAST, BWA, R] -> quantification [DESeq2 v1.34] -> normalisation [ImageJ, limma] -> dimensionality reduction/clustering [clusterProfiler v4.2.2, limma] -> visualisation [limma] -> stage not stated [GSEA, Python, Seurat, scDblFinder]

### Distinctive DNA sequence features define epigenetic longevity of inflammatory memory. (Science 2026)

- DOI: 10.1126/science.adz6830 | PMCID: PMC13295011 | PMID: 41886579
- Evidence: Analysis of Cut-and-Run sequencing Forty base pair paired-end reads raw reads were aligned to the mouse reference genome (mm10, GENCODE v.30 annotation) using BWA-MEM in paired-end mode with the -M and -T 10 parameters to mark split alignments and increase mapping stringency.
- Full pipeline: quality control [SAMtools] -> read trimming [Bowtie2, Cutadapt v4.6] -> alignment/mapping [BEDTools, BWA, Bowtie2, SAMtools] -> quantification [ArchR] -> normalisation [AnnData] -> dimensionality reduction/clustering [Seurat, UMAP, clusterProfiler] -> differential/statistical testing [DESeq2, R] -> visualisation [ggplot2 v3.5.2] -> stage not stated [GSEA, ImageJ, MACS2, NumPy, Picard, Scanpy, TensorFlow, deepTools v3.5.6, scikit-learn]

### The evolution of gene regulation in mammalian cerebellum development. (Science 2026)

- DOI: 10.1126/science.adw9154 | PMCID: PMC7618896 | PMID: 41610256
- Evidence: The trimmed and filtered reads were then aligned to the mouse mm10 (GRCm38) assembly using BWA-MEM ( 100 ).
- Full pipeline: quality control [Cutadapt, FastQC, Trim Galore v0.6.6] -> read trimming [BWA, Cutadapt, FastQC, STAR v2.7.9, Trim Galore v0.6.6] -> alignment/mapping [BWA, STAR v2.7.9] -> normalisation [Seurat v4.0] -> dimensionality reduction/clustering [Seurat v4.0, SoupX v1.5.2, UMAP, clusterProfiler v4.0.5] -> differential/statistical testing [DESeq2, lme4 v1.1] -> machine learning [MACS2] -> stage not stated [ArchR v1.0.2, BEDTools, Harmony v0.1.0, NetworkX, R, SCENIC, SciPy, TensorFlow v2.9.1, scikit-learn]

