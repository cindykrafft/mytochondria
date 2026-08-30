# Component: mris_anatomical_stats + curvature/thickness stats + stats2table
Agent verdict (dev vs v6.0.0 vs v7.1.1 traced):

F1 CONFIRMED (v5.3/v6.0, fixed v7): global # Measure rows mix voxel counts with mm3
   (BrainVolStatsFixed bug) — same as segstats F1; corrupts aparc.stats header measures AND any
   published ROI value normalized by BrainSegVol-family covariates on non-1mm conforms.

F2 CONFIRMED (all versions): `-i <low> <high>` thickness-range option is a silent NO-OP —
   MRIScomputeCurvatureStats never called; program prints that it filtered but didn't.
   mris_anatomical_stats.cpp:1260-1267 vs 1348-1390. Papers stating outlier exclusion via -i
   actually published unfiltered means.

F3 CONFIRMED mechanism (all versions, small): ill-conditioned curvature fallback halves
   principal curvatures (secant z/r^2 = k/2) and breaks |k1|>=|k2| ordering -> FoldInd gets
   negative contributions at sulcal fundi; downward mesh-quality-dependent bias on
   MeanCurv/GausCurv/FoldInd/CurvInd. mrisurf_metricProperties.cpp:10535,10590-10592,11406-11408.

F4 CONFIRMED (all versions): per-ROI ThickAvg includes non-cortex frozen vertices (thickness~0)
   while GrayVol excludes them via cortex.label mask and global MeanThickness excludes them too.
   Internally inconsistent row: GrayVol != SurfArea*ThickAvg; downward ThickAvg bias + inflated
   ThickStd in entorhinal/parahippocampal/insula/pericallosal ROIs (medial-wall borders).
   mris_anatomical_stats.cpp:839-848 (no filter) vs 245-248 (masked TH3) vs 600-626 (global).

F5 CONFIRMED (all versions): aparcstats2table writes 0.0 silently for any subject missing an
   ROI row (no warning at default verbosity) -> massive low outlier in group tables.
   scripts/aparcstats2table:298-310. asegstats2table has a guard; aparc does not.

F6 minor: TH3 GrayVol hardcodes %s.white/%s.pial ignoring -white/-pial overrides; --transpose
   tables rounded to 6 sig digits ('%g'); -h histogram output is dead code (all zeros).

VERIFIED CORRECT: TH3 tetra decomposition matches srf2vol; ROI face-third accumulation +
dofs bookkeeping; stats2table column mapping + name-based merging (no scrambling).

MAPS TO: roi_morphometry group (85 papers). F4 biases absolute ROI thickness in wall-adjacent
ROIs everywhere; F1 hits v5/v6 hires; F2/F5 depend on invocation.
