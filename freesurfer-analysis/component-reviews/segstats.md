# Component: mri_segstats / cma.cpp / eTIV (aseg.stats path)
Agent verdict summary (traced dev vs v6.0.0 vs v7.1.1 vs v7.4.1):

F1 CONFIRMED (v6.0 and earlier): header brain-volume measures are voxel COUNTS not mm3, mixed
   with surface mm3 terms; plus `int VoxSize` truncation (0.8mm -> 0.512 -> 0) zeroes the
   supratentorial correction. Any v5.3/v6.0 run on non-1mm conform: BrainSegVol/MaskVol/
   SubCortGrayVol/eTIV-ratios inflated ~1.95x at 0.8mm; CortexVol/TotalGrayVol corrupted.
   Per-structure table rows (hippocampus etc.) UNAFFECTED in all versions (nhits*voxelvolume).
   v7 fixed; stamps "# BrainVolStatsFixed". Evidence: v6 cma.c:977-1024,571,646; dev cma.cpp:1374-1446;
   mri_segstats.cpp:1097-1104.

F2 CONFIRMED (silent v6->v7 formula switch): SupraTentorialVolNotVent (now minus TFFC, ~4-6cm3
   smaller), SupraTentorialVol (surface->voxel based), CerebralWhiteMatterVol (now includes WM
   hypointensities; double-counted if summed with table rows), CortexVol (dropped nonCortexInRibbon
   correction), BrainSegVol (now excludes Optic Chiasm / non-LUT labels). Mixed-version or
   longitudinal studies get 0.1-2% step changes in header measures.

F3 CONFIRMED (v7.0..dev): cache-miss fallback (missing stats/brainvol.stats, or --no-cached)
   computes header measures with the OLD v1 formula -> same binary yields two different value sets
   depending on cache presence. cma.cpp:1580-1590; mri_segstats.cpp:539-545.

F4 CONFIRMED latent (v7.0+): thalamus double-counted in SupraTentorialVolCorrection —
   four id tests collapsed to two after Left_Thalamus aliased to 10; each thalamus voxel outside
   ribbon counted 2x. cma.cpp:538-541 (v6 tested 9/48/10/49: cma.c:600-603). Exercised only via
   F3 fallback path; small (<1cm3). Also: legacy segs using ids 9/48 lose thalamus from
   SubCortGrayVol in v7+.

F5 PLAUSIBLE negligible: asymmetric pv clamp (pv>1 ->1, pv<0 -> skip both) mri.cpp:14535-14549;
   degenerate ties only. Historical max_count type-confusion bug fixed in aseg path but STILL LIVE
   in MRImakeDensityMap (dev mri.cpp:14642) — not in papers' path.

F6 note: FS8 --pv fast-path rewrite verified logically equivalent (no v7.4->8 table shift).

VERIFIED CORRECT: table Volume_mm3 uses all 3 pixdims (all versions); Mean/StdDev formulas;
eTIV formula identical v6.0.0->dev (1948.106*1000/det(talairach.xfm)); TotalGrayVol composition
identical across versions (cerebellar GM included in all).

MAPS TO: aseg_volumes group (16 papers). Highest risk: v5.3/6.0 + submm/hires papers (F1);
mixed-version longitudinal (F2/F3).
