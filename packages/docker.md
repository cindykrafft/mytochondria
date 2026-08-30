# Docker

- **Category:** workflow
- **Papers in survey:** 40
- **Journals:** Nature (18), PNAS (17), Cell (4), Science (1)
- **Years:** 2021 (6), 2022 (7), 2023 (4), 2024 (8), 2025 (9), 2026 (6)
- **Versions named:** 23.0.1 (1), 1.1.0 (1), 1.12.6 (1)
- **Pipeline stages it appears in:** dimensionality reduction/clustering (3), alignment/mapping (2), visualisation (1), machine learning (1), differential/statistical testing (1)

## Papers

### Maturation and persistence of the anti-SARS-CoV-2 memory B cell response. (Cell 2021)

- DOI: 10.1016/j.cell.2021.01.050 | PMCID: PMC7994111 | PMID: 33571429
- Evidence: ....0.2 R Foundation https://www.r-project.org RStudio v1.3.1056 RStudio https://rstudio.com IgBLASTn v1.16.0 NCBI https://www.ncbi.nlm.nih.gov/igblast/ Docker desktop v2.5.0.0 Docker, Inc https://www.docker.com/products/docker-desktop Resource availability Lead contact Further information and requests for resources and reagents should be directed to and will be fulfilled by the Lead Contact, Matthie...
- Full pipeline: quality control [Seurat v3.2.2] -> alignment/mapping [R v4.0] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP, igraph v1.2.6] -> stage not stated [Docker, ggplot2 v3.3.2]

### Baricitinib treatment resolves lower-airway macrophage inflammation and neutrophil recruitment in SARS-CoV-2-infected rhesus macaques. (Cell 2021)

- DOI: 10.1016/j.cell.2020.11.007 | PMCID: PMC7654323 | PMID: 33278358
- Version used: **1.12.6**
- Evidence: .../ggplot2.tidyverse.org Plotly Sievert, 2020 https://plotly-r.com Analysis scripts This paper https://github.com/BosingerLab/RM_Baricitinib_manuscript Docker v 1.12.6 Docker https://www.docker.com/ RStudio v1.1.453 RStudio, Inc. https://rstudio.com/ rocker/rstudio v3.6 Rocker Project https://hub.docker.com/r/rocker/rstudio Other miRNeasy Micro Kit QIAGEN Cat#217084 SMART-Seq v4 Ultra Low Input RNA ...
- Full pipeline: quality control [FastQC] -> alignment/mapping [HTSeq] -> quantification [HTSeq] -> dimensionality reduction/clustering [UMAP] -> visualisation [UMAP] -> stage not stated [ComplexHeatmap, DESeq2 v1.24.0, Docker v1.12.6, GSEA v4.1.0, STAR v2.7.3a, Seurat v3.1.5, ggplot2, scDblFinder v2.0.3, tidyverse]

### Pan-cancer analyses reveal cancer-type-specific fungal ecologies and bacteriome interactions. (Cell 2022)

- DOI: 10.1016/j.cell.2022.09.005 | PMCID: PMC9567272 | PMID: 36179670
- Evidence: ...d by Qiita) Zhu et al., 2022 https://github.com/qiyunzhu/woltka ITS2 classification pipeline This paper https://github.com/microbiofunc/ITS2-pipeline Dockerized host depletion pipeline This paper https://github.com/knightlab-analyses/mycobiome/tree/master/Docker_host_depletion_pipeline Per-sample and aggregate genome coverage Hakim et al., 2022 https://github.com/ucsd-cmi/zebra_filter MMvec co-occ...
- Full pipeline: read trimming [HMMER] -> alignment/mapping [HMMER] -> differential/statistical testing [Cytoscape v3.8.1, SciPy, limma, statsmodels] -> stage not stated [BLAST, BUSCO v5.1.2, Bowtie2, Cutadapt v1.17, Docker, Python v3.6, QIIME 2 v2018.8, R v4.03, SAMtools v0.1.19, XGBoost v1.5.0.1, edgeR v3.36.0, fastp, ggplot2 v3.3.4, ggpubr v0.4.0, minimap2 v2.17, pheatmap v1.0.12, phyloseq v1.34.0, scikit-learn, seaborn, tidyverse v1.0.7, vegan v2.5]

### A blood atlas of COVID-19 defines hallmarks of disease severity and specificity. (Cell 2022)

- DOI: 10.1016/j.cell.2022.01.012 | PMCID: PMC8776501 | PMID: 35216673
- Evidence: Dendrou, Julie Dequaire, Lea Dib, James Docker, Christina Dold, Tao Dong, Damien Downes, Hal Drakesmith, Susanna J.
- Full pipeline: quality control [FastQC, Scanpy, featureCounts, fgsea] -> read trimming [FastQC, STAR v2.7.3, edgeR] -> alignment/mapping [Python, STAR v2.7.3] -> variant calling [GATK, featureCounts, fgsea] -> dimensionality reduction/clustering [FastQC, Python, R, Trim Galore, UMAP, featureCounts, fgsea, survival (R), velocyto] -> differential/statistical testing [GSEA] -> visualisation [AnnData, survival (R)] -> stage not stated [ArchR, Cytoscape, Docker, MACS2, Matplotlib, NumPy, Picard, SAMtools, SciPy, Seurat, WGCNA, ggplot2, limma, scDblFinder, scVelo, scikit-learn, seaborn]

### Swarm Learning for decentralized and confidential clinical machine learning. (Nature 2021)

- DOI: 10.1038/s41586-021-03583-3 | PMCID: PMC8189907 | PMID: 34040261
- Evidence: All scripts used in this study for pre-processing are provided as a docker container on Docker Hub (v 0.1, https://hub.docker.com/r/schultzelab/aml_classifier ).
- Full pipeline: alignment/mapping [kallisto v0.43.1] -> normalisation [DESeq2 v1.22.2, R] -> machine learning [Docker] -> stage not stated [Keras v2.3.1, TensorFlow v2.2.0, scikit-learn]

### Sequencing of 53,831 diverse genomes from the NHLBI TOPMed Program. (Nature 2021)

- DOI: 10.1038/s41586-021-03205-y | PMCID: PMC7875770 | PMID: 33568819
- Evidence: Fusera, samtools and other tools are also packaged in a Docker container for ease of use and are available for download from Docker Hub 83 .
- Full pipeline: dimensionality reduction/clustering [SAIGE] -> stage not stated [BWA, Docker, GATK v3.5.0, R, SAMtools, VEP]

### Primate gastrulation and early organogenesis at single-cell resolution. (Nature 2022)

- DOI: 10.1038/s41586-022-05526-y | PMCID: PMC9771819 | PMID: 36517595
- Evidence: TF analysis The pySCENIC analysis in Docker was carried out following three steps 63 .
- Full pipeline: quantification [CellPhoneDB, R, Seurat v4.0.0] -> dimensionality reduction/clustering [R, Seurat v4.0.0, UMAP, clusterProfiler, pheatmap, scVelo] -> simulation/modelling [Scanpy v1.8.2] -> visualisation [pheatmap] -> stage not stated [Docker, SCENIC, ilastik, scDblFinder]

### Dysregulated naive B cells and de novo autoreactivity in severe COVID-19. (Nature 2022)

- DOI: 10.1038/s41586-022-05273-0 | PMCID: PMC9630115 | PMID: 36044993
- Evidence: Analyses of the single-cell VDJ annotated sequences were performed using the Immcantation tool suite ( http://www.immcantation.org ) v.4.1.0 pipeline in Docker.
- Full pipeline: normalisation [pheatmap] -> stage not stated [Docker, R v3.6.2, ggplot2]

### Autonomous chemical research with large language models. (Nature 2023)

- DOI: 10.1038/s41586-023-06792-0 | PMCID: PMC10733136 | PMID: 38123806
- Evidence: The PYTHON command performs code execution (not reliant upon any language model) using an isolated Docker container to protect the users’ machine from any unexpected actions requested by the Planner.
- Full pipeline: stage not stated [Docker, NumPy, RDKit]

### Specialized astrocytes mediate glutamatergic gliotransmission in the CNS. (Nature 2023)

- DOI: 10.1038/s41586-023-06502-w | PMCID: PMC10550825 | PMID: 37674083
- Evidence: The Docker image of AstroGlu was tested on the above cluster with varying node configurations for CPU cores and RAM.
- Full pipeline: normalisation [Seurat, UMAP] -> registration [DIPY, scikit-image] -> dimensionality reduction/clustering [Docker, GSEA, UMAP] -> differential/statistical testing [GSEA] -> visualisation [UMAP] -> stage not stated [Conda, ImageJ, Jupyter, Matplotlib, NumPy v1.19.5, SciPy, ggplot2 v3.4.2, scDblFinder, tidyverse v1.1.2]

### A draft human pangenome reference. (Nature 2023)

- DOI: 10.1038/s41586-023-05896-x | PMCID: PMC10172123 | PMID: 37165242
- Evidence: Individual tools within the workflow were run in Docker containers with specific tool versions installed for consistency and reproducibility.
- Full pipeline: read trimming [BEDTools, BLAST] -> alignment/mapping [BCFtools, DeepVariant v1.3.0, MAFFT, STAR v2.7.10a, WhatsHap v1.1] -> variant calling [BCFtools, BWA, QUAST, hifiasm] -> registration [GATK v3.8.1, freebayes v1.2.0] -> dimensionality reduction/clustering [R] -> stage not stated [Bowtie2 v2.4.5, Docker, Jupyter, RSEM v1.3.3, RepeatMasker v4.1.2, SAMtools, Salmon v1.9.0, minimap2]

### Ab initio characterization of protein molecular dynamics with AI&lt;sup&gt;2&lt;/sup&gt;BMD. (Nature 2024)

- DOI: 10.1038/s41586-024-08127-z | PMCID: PMC11602711 | PMID: 39506110
- Evidence: The software configuration is fully defined with a Docker image and remains invariant across different machines, which allows us to not only effortlessly deploy the software system to the cloud, but also fine-tune the program against a fixed set of supporting libraries.
- Full pipeline: simulation/modelling [GROMACS, Python] -> stage not stated [Docker, MDTraj]

### AKT and EZH2 inhibitors kill TNBCs by hijacking mechanisms of involution. (Nature 2024)

- DOI: 10.1038/s41586-024-08031-6 | PMCID: PMC11578877 | PMID: 39385030
- Evidence: The acquired images were processed using the Docker-based NextFlow pipeline MCMICRO.
- Full pipeline: alignment/mapping [Bowtie2, HTSeq] -> normalisation [DESeq2] -> differential/statistical testing [DESeq2, R, featureCounts] -> machine learning [Python, scikit-learn] -> stage not stated [CNVkit, ComplexHeatmap, Docker, GSEA, MACS2, SAMtools, Salmon v0.14.1, fgsea, ggplot2, pheatmap]

### Spectroscopic confirmation of two luminous galaxies at a redshift of 14. (Nature 2024)

- DOI: 10.1038/s41586-024-07860-9 | PMCID: PMC11390484 | PMID: 39074505
- Evidence: BEAGLE is available by means of a Docker image upon request at http://www.iap.fr/beagle/ .
- Full pipeline: stage not stated [Docker]

### Single-cell multiplex chromatin and RNA interactions in ageing human brain. (Nature 2024)

- DOI: 10.1038/s41586-024-07239-w | PMCID: PMC11023937 | PMID: 38538789
- Evidence: Computational analysis The MUSIC-docker data-processing pipeline We developed MUSIC-docker to process MUSIC sequencing data using Docker to encapsulate a Snakemake 57 pipeline, ensuring cross-platform execution.
- Full pipeline: alignment/mapping [Bowtie2 v5.4.0] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Docker, Harmony v0.1.1, R, Seurat v4.3.0, Snakemake]

### RNA-mediated symmetry breaking enables singular olfactory receptor choice. (Nature 2024)

- DOI: 10.1038/s41586-023-06845-4 | PMCID: PMC10765522 | PMID: 38123679
- Evidence: In brief, reads were aligned to the mm10 genome using the distiller pipeline ( https://github.com/mirnylab/distiller-nf , requirements: java8, nextflow and Docker); uniquely mapped reads (mapq > 30) were retained, and duplicate reads were discarded.
- Full pipeline: read trimming [BWA v0.7.17] -> alignment/mapping [BWA v0.7.17, Bowtie2, Docker, SAMtools, STAR] -> dimensionality reduction/clustering [PyMOL v2.5.3, SciPy, UMAP] -> structure determination [PyMOL v2.5.3] -> visualisation [ImageJ v2.0.0, UMAP] -> stage not stated [DESeq2, HOMER, LAMMPS, Picard, Seurat v4.1.0, Signac v1.6.0]

### Efficient and accurate search in petabase-scale sequence repositories. (Nature 2025)

- DOI: 10.1038/s41586-025-09603-w | PMCID: PMC12657231 | PMID: 41062695
- Evidence: This web application is deployed in a Docker container (v.1.13.1; API v.1.26) using the Nginx (v.1.16.1) server as a backend.
- Full pipeline: alignment/mapping [BWA v0.7.17, STAR v2.7.0] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [Docker, Python, R v71.2, Snakemake]

### Functional connectomics reveals general wiring rule in mouse visual cortex. (Nature 2025)

- DOI: 10.1038/s41586-025-08840-3 | PMCID: PMC11981947 | PMID: 40205211
- Version used: **23.0.1**
- Evidence: ...yvolume (0.5.2) and Neuroglancer ( https://github.com/seung-lab/neuroglancer ) were used for graphical visualization; and Jupyter (ipykernel:6.21.2), Docker (23.0.1) and Kubernetes (1.22.11) were used for code development and deployment.
- Full pipeline: differential/statistical testing [Matplotlib v3.7.0, NumPy v1.23.5, Python, scikit-learn v1.2.1, seaborn v0.12.2, statsmodels, tidyverse v2.0.0] -> machine learning [DeepLabCut, Matplotlib v3.7.0, NumPy v1.23.5, PyTorch, scikit-learn v1.2.1, seaborn v0.12.2, tidyverse v2.0.0] -> visualisation [Docker v23.0.1, Jupyter, Matplotlib v3.7.0, seaborn v0.12.2] -> stage not stated [R, SciPy, emmeans]

### A rare PRIMER cell state in plant immunity. (Nature 2025)

- DOI: 10.1038/s41586-024-08383-z | PMCID: PMC11798839 | PMID: 39779856
- Evidence: Baysor was run using a downloaded Docker image and parameters -s 250, --n clusters 1, -i 1, --force-2d, min-molecules-per-gene=1, min-molecules-per-cell=50, scale=250, scale-std=“25%”, estimate-scale-from-centers=true, min-molecules-per-segment=15, new-component-weight=0.2, new-component-fraction=0.3.
- Full pipeline: quality control [R, scDblFinder] -> read trimming [STAR v2.6.1b, fastp v0.19.7, featureCounts v1.6.0] -> alignment/mapping [STAR v2.6.1b, featureCounts v1.6.0] -> normalisation [edgeR, limma] -> dimensionality reduction/clustering [Docker, NumPy, UMAP, clusterProfiler, scikit-learn] -> machine learning [Cellpose] -> stage not stated [ImageJ, MACS2, OpenCV, Scanpy, Seurat, Signac, ggplot2]

### Efficient robot navigation inspired by honeybee learning flights. (Nature 2026)

- DOI: 10.1038/s41586-026-10461-3 | PMCID: PMC13216067 | PMID: 42129549
- Evidence: Onboard software The onboard software operates in a modular architecture using Docker containers.
- Full pipeline: stage not stated [Docker, OpenCV]

### An integrated view of the structure and function of the human 4D nucleome. (Nature 2026)

- DOI: 10.1038/s41586-025-09890-3 | PMCID: PMC12804090 | PMID: 41407856
- Evidence: SPIN states enriched caRNA sequence features Processing of iMARGI data was performed with iMARGI-Docker 77 .
- Full pipeline: read trimming [Cutadapt, SAMtools, deepTools] -> alignment/mapping [Bowtie2 v2.3.4.3, Cutadapt, R, RSEM, SAMtools, deepTools] -> quantification [R, RSEM] -> normalisation [R, RSEM] -> dimensionality reduction/clustering [UMAP] -> simulation/modelling [LAMMPS] -> visualisation [HOMER] -> stage not stated [BEDTools, Docker, MACS2, NumPy, OpenCV, scikit-learn]

### Human assembloids recapitulate periportal liver tissue in vitro. (Nature 2026)

- DOI: 10.1038/s41586-025-09884-1 | PMCID: PMC12893922 | PMID: 41407857
- Evidence: The complete software stack for downstream analysis is available as a Docker container (rnaseq-notebook:2025-04-21) archived at https://quay.io/repository/fbnrst/rnaseq-notebook and archived on Zenodo (10.5281/zenodo.17704466).
- Full pipeline: quality control [MultiQC] -> normalisation [Harmony, limma] -> dimensionality reduction/clustering [GSEA, Harmony, UMAP, clusterProfiler] -> visualisation [UMAP] -> stage not stated [Conda, DESeq2, Docker, Enrichr, ImageJ, MACS2, Nextflow v24.10.5, Scanpy]

### A modular computational framework for medical digital twins. (PNAS 2021)

- DOI: 10.1073/pnas.2024287118 | PMCID: PMC8157963 | PMID: 33972437
- Evidence: We address these by encapsulating our environment in a Docker container ( 17 ).
- Full pipeline: stage not stated [Docker, NumPy, Python, SciPy]

### Incubation of palatable food craving is associated with brain-wide neuronal activation in mice. (PNAS 2022)

- DOI: 10.1073/pnas.2209382119 | PMCID: PMC9659381 | PMID: 36603188
- Evidence: We provide the updated SMART2 package repository ( https://github.com/sgoldenlab/SMART2 ) and include a Docker installation image for rapid and user-friendly installation of SMART2 ( https://hub.docker.com/repository/docker/goldenneurolab/wholebrain_smart2 ).
- Full pipeline: stage not stated [Docker]

### Sox8 remodels the cranial ectoderm to generate the ear. (PNAS 2022)

- DOI: 10.1073/pnas.2118938119 | PMCID: PMC9282420 | PMID: 35867760
- Evidence: A custom Docker container used for the downstream analysis pipeline can be found at https://hub.docker.com/repository/docker/alexthiery/otic-reprogramming-r_analysis .
- Full pipeline: read trimming [Cutadapt v2.10] -> alignment/mapping [HISAT2 v2.2.1, Nextflow, STAR] -> quantification [HTSeq v0.12.4] -> differential/statistical testing [MACS2 v2.2.7.1] -> stage not stated [BEDTools v2.29.2, DESeq2, Docker, ImageJ, Monocle, R, velocyto v0.17]

### MoSBi: Automated signature mining for molecular stratification and subtyping. (PNAS 2022)

- DOI: 10.1073/pnas.2118210119 | PMCID: PMC9169782 | PMID: 35412913
- Evidence: The workflow can be executed from our web app on our servers or on a local machine using a public Docker image.
- Full pipeline: dimensionality reduction/clustering [clusterProfiler] -> visualisation [ggplot2, igraph] -> stage not stated [Cytoscape, Docker, R]

### Structure of the priming arabinosyltransferase AftA required for AG biosynthesis of <i>Mycobacterium tuberculosis</i>. (PNAS 2023)

- DOI: 10.1073/pnas.2302858120 | PMCID: PMC10265970 | PMID: 37252995
- Evidence: Then, at the stage of high-resolution docking, the High Res Docker module carries out cycles of rotamer trials (sampling of side chain rotamers, one side chain at a time) or repacking (simultaneous sampling of rotamers for multiple side chains), coupled with small movements of ligand.
- Full pipeline: alignment/mapping [Clustal Omega] -> structure determination [PHENIX v1.12] -> stage not stated [CTFFIND, ChimeraX, Docker, PyMOL, RDKit, UCSF Chimera]

### Aversive memories can be weakened during human sleep via the reactivation of positive interfering memories. (PNAS 2024)

- DOI: 10.1073/pnas.2400678121 | PMCID: PMC11295023 | PMID: 39052838
- Evidence: We utilized a Bayesian hierarchical estimation of the DDM (HDDM 0.8) implemented in the Docker HDDM framework ( 85 ).
- Full pipeline: differential/statistical testing [Docker] -> stage not stated [MNE-Python, Python v3.8]

### APACE: AlphaFold2 and advanced computing as a service for accelerated discovery in biophysics. (PNAS 2024)

- DOI: 10.1073/pnas.2311888121 | PMCID: PMC11228474 | PMID: 38913887
- Evidence: Methods Given that Delta and Polaris’s container support is only available for Apptainer/Singularity ( 39 ), we modified the instructions provided in AlphaFold2 GitHub repository, which are intended for Docker containers ( 40 ).
- Full pipeline: stage not stated [AlphaFold, ColabFold, Docker, Singularity, Slingshot]

### Intergenerational protective anti-gut commensal immunoglobulin G originates in early life. (PNAS 2024)

- DOI: 10.1073/pnas.2309994121 | PMCID: PMC10990157 | PMID: 38517976
- Evidence: All software requiring R or command line used to analyze data was uploaded as precompiled Docker images on the university computer server cluster.
- Full pipeline: read trimming [Bowtie2 v2.4.1, MAFFT v7.475] -> alignment/mapping [Bowtie2 v2.4.1, MAFFT v7.475] -> dimensionality reduction/clustering [Docker] -> visualisation [R v4.0, phyloseq] -> stage not stated [BLAST, RAxML]

### Versatile NTP recognition and domain fusions expand the functional repertoire of the ParB-CTPase fold beyond chromosome segregation. (PNAS 2025)

- DOI: 10.1073/pnas.2527592122 | PMCID: PMC12704722 | PMID: 41343662
- Evidence: For each species, prophage and plasmids were predicted using geNomad ( 118 ) (end-to-end mode, Docker image obtained on 25.04.30).
- Full pipeline: alignment/mapping [MAFFT v7.490] -> stage not stated [AlphaFold, AutoDock Vina, Docker, HMMER v3.4, IQ-TREE]

### Conscious awareness, sensory integration, and evidence accumulation in bodily self-perception. (PNAS 2025)

- DOI: 10.1073/pnas.2503629122 | PMCID: PMC12704745 | PMID: 41337481
- Evidence: Body ownership decision processes ( 115 , 116 ) were decomposed using hierarchical DDM [HDDM; ( 117 )] implemented in Docker ( 118 ).
- Full pipeline: quantification [JAGS] -> differential/statistical testing [JAGS] -> stage not stated [Docker, R]

### Genetic testing predicts appearance but not behavior in dogs. (PNAS 2025)

- DOI: 10.1073/pnas.2421752122 | PMCID: PMC12684939 | PMID: 41284863
- Evidence: This framework, packaged in a Docker container image, enables consistent execution across computing environments and parallelization across multiple phenotypes.
- Full pipeline: alignment/mapping [BWA] -> differential/statistical testing [SciPy, statsmodels] -> stage not stated [ADMIXTURE, Docker, GCTA v1.94.1, Nextflow, PLINK v1.90b, pandas]

### Pervasive horizontal transfer of adeno-associated virus capsid genes. (PNAS 2025)

- DOI: 10.1073/pnas.2505928122 | PMCID: PMC12358894 | PMID: 40773239
- Evidence: All curated sequences, alignments, and analysis workflows are fully documented and openly accessible in the associated repositories, and a Docker image is provided for streamlined, cross-platform reproducibility ( 12 ).
- Full pipeline: alignment/mapping [Docker]

### Longitudinal trajectories of brain development from infancy to school age and their relationship with literacy development. (PNAS 2025)

- DOI: 10.1073/pnas.2414598122 | PMCID: PMC12184337 | PMID: 40493188
- Version used: **1.1.0**
- Evidence: To improve tissue classification accuracy, MPRAGE images were submitted in parallel to iBEATv2.0 Docker 1.1.0 [( 115 – 117 ); https://github.com/iBEAT-V2/iBEAT-V2.0-Docker ], which has been validated for birth to age 6 y ( 115 ).
- Full pipeline: dimensionality reduction/clustering [ANTs, FSL, R] -> differential/statistical testing [R, lme4] -> simulation/modelling [lme4] -> stage not stated [Docker v1.1.0, FreeSurfer v7.3, MRtrix3]

### How can we make sound replication decisions? (PNAS 2025)

- DOI: 10.1073/pnas.2401236121 | PMCID: PMC11804638 | PMID: 39869811
- Evidence: Within the field of computer science, making computational experiments available can be as easy as creating a Docker container ( 60 ) (i.e., an executable package, including the code, system tools, dependencies, and settings necessary to run the experiment), but producing quality software that is open-source, fully documented, and can be reused and extended is a time-consuming and costly endeavor.
- Full pipeline: stage not stated [Docker]

### Large cities lose their growth advantage as countries urbanize. (PNAS 2026)

- DOI: 10.1073/pnas.2529430123 | PMCID: PMC13321366 | PMID: 42348619
- Evidence: It is containerized with Docker.
- Full pipeline: stage not stated [Docker]

### From data to decisions: Toward a Biodiversity Monitoring Standards Framework. (PNAS 2026)

- DOI: 10.1073/pnas.2519347123 | PMCID: PMC12974509 | PMID: 41779789
- Evidence: Reproducibility Package: The entire analysis workflow (code, software environment) is packaged into a Docker container ready for use in BON in a Box or similar platforms.
- Full pipeline: machine learning [QGIS] -> stage not stated [Docker]

### A temporal and spatial atlas of adaptive immune responses in the lymph node following viral infection. (PNAS 2026)

- DOI: 10.1073/pnas.2504742123 | PMCID: PMC12867689 | PMID: 41587309
- Evidence: To begin this analysis, we first assign VDJ genes using IgBLAST ( 28 ) from Immcantation Lab Docker image.
- Full pipeline: stage not stated [AnnData, Docker, Scanpy v1.9.8, SciPy]

### SARS-CoV-2 within-host diversity and transmission. (Science 2021)

- DOI: 10.1126/science.abg0821 | PMCID: PMC8128293 | PMID: 33688063
- Evidence: Docker for assistance in the laboratory; and L.
- Full pipeline: read trimming [Bowtie2, Trimmomatic v0.36] -> alignment/mapping [Bowtie2, IQ-TREE, MAFFT] -> structure determination [IQ-TREE, RAxML] -> stage not stated [Docker, Pangolin]

