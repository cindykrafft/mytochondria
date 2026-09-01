# Component: mris_ca_label / gcsa / annotation / mri_aparc2aseg / HippoSF
Agent verdict (dev + v6.0.0 + v7.1.1 traced):

F1 CONFIRMED (all versions): GCSArelabelIslands stores double log-likelihood into `int ll`,
   compares truncated ints; ties broken by vertex adjacency order + first-differing-neighbor
   adoption -> small annotation islands absorbed into quasi-arbitrary adjacent gyrus, not the
   max-likelihood one. Biases area/thickness of small ROIs (bankssts, transversetemporal...).
   gcsa.cpp:1557 (v6 gcsa.c:1589; v7.1.1 gcsa.cpp:1370). Runs in EVERY mris_ca_label.

F2 CONFIRMED (all versions, variant differs): mri_aparc2aseg winner-selection falls through when
   all 4 candidates rejected (BRFdotCheck) or tie -> voxel inherits PREVIOUS voxel's ROI and
   hemisphere; v7+: annotid UNINITIALIZED at first such voxel per column (UB); v6: file-scope
   globals + no fallback re-search (more frequent). Wrong-hemisphere labels possible.
   mri_aparc2aseg.cpp:549,720-797,876 (v6 .c:132,705-761).

F3 CONFIRMED (v7.1.1+): mri_aparc2aseg reads the seg it mutates in place -> scan-order dependent
   boundary-correction gating + OpenMP race over adjacent columns -> run-to-run nondeterminism of
   aparc+aseg boundary voxels. Lines 544-546,591,725-761,876.

F4 CONFIRMED defect / no label bias: edge_to_index early-returns, collapsing 4-direction Gibbs
   neighborhood to 2; consistent train/apply so no mislabeling, just weaker MRF than designed.
   gcsa.cpp:1280-1291.

F5 CONFIRMED negligible: gcsaFixSingularCovarianceMatrices inverts stale matrix instead of
   gcs->m_cov. gcsa.cpp:2203.

F6 CONFIRMED off-pipeline: readAnnotationIntoVector off-by-one heap overflow (mris_annot_diff
   only); MRISannotDice builds segidlist2 from seg1 (no in-tree callers).

F7 mechanism CONFIRMED / bug PLAUSIBLE: MRISmodeFilterAnnotations mode scan starts at index 1 —
   "unknown" can never win a vertex; one-way ratchet expands medial-wall-adjacent ROIs
   (entorhinal, parahippocampal, isthmus-cingulate...) during the 10 smoothing iterations.
   mrisurf_vals.cpp:2949. All versions.

VERIFIED CORRECT: GCSA prior/likelihood math; annot RGB -> ctab -> stats-row identity chain
(no scrambling with shipped atlases); HippoSF soft-posterior volume integrals at correct
resolution (0.003% num2str quirk only).

MAPS TO: roi_morphometry (85 papers; F1/F7 bias small + wall-adjacent ROIs everywhere),
aseg_volumes via aparc+aseg/wmparc (F2/F3), hipposf (8 papers: CLEAN — volumes verified correct).
