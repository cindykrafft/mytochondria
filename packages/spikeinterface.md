# SpikeInterface

- **Category:** neuro-tools
- **Papers in survey:** 3
- **Journals:** Nature (3)
- **Years:** 2024 (1), 2025 (1), 2026 (1)
- **Pipeline stages it appears in:** quality control (1)

## Papers

### A model of human neural networks reveals NPTX2 pathology in ALS and FTLD. (Nature 2024)

- DOI: 10.1038/s41586-024-07042-7 | PMCID: PMC10901740 | PMID: 38355792
- Evidence: 3e ), extracted from SpikeInterface 33 , an open-source Python-based framework to enclose all the spike sorting steps: Half width half maximum (HWHM), half width of trough of the action potential wave at half amplitude.
- Full pipeline: read trimming [Cutadapt v4.1] -> alignment/mapping [STAR v2.7.7a] -> quantification [ilastik] -> normalisation [Seurat] -> dimensionality reduction/clustering [UMAP] -> differential/statistical testing [edgeR v3.36.0] -> machine learning [ilastik] -> stage not stated [ImageJ, Python v3.6.10, R, SpikeInterface, scDblFinder, tidyverse]

### Engrafted nitrergic neurons derived from hPSCs improve gut dysmotility in mice. (Nature 2025)

- DOI: 10.1038/s41586-025-09208-3 | PMCID: PMC12408359 | PMID: 40562934
- Evidence: Data processing Raw data were first spike-sorted with a modified version of SpikeInterface ( https://github.com/SpikeInterface ) using MountainSort to identify high-quality units by manually scoring on the basis of amplitude, waveform shape, firing rate and inter-spike interval contamination.
- Full pipeline: quality control [R v4.0, Seurat, SpikeInterface] -> read trimming [kallisto] -> alignment/mapping [STAR] -> dimensionality reduction/clustering [UMAP] -> stage not stated [Cutadapt, DESeq2, HTSeq]

### Plasticity and language in the anaesthetized human hippocampus. (Nature 2026)

- DOI: 10.1038/s41586-026-10448-0 | PMCID: PMC13275293 | PMID: 42092132
- Evidence: Unit quality metrics were calculated using SpikeInterface 62 and were considered single units if they had a d ′ greater than 1 and fewer than 3% of spikes were violations of a 2 ms interspike interval refractory period.
- Full pipeline: registration [Kilosort] -> structure determination [Python] -> stage not stated [SpikeInterface]

