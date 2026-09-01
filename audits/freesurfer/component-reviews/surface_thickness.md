# Component: surface placement (mris_make_surfaces / mris_place_surface) + thickness metric
Agent verdict (dev + v6.0.0 + v7.1.1 + v7.4.1 traced):

F1 CONFIRMED v6->v7 change: v7 thickness computed on de-ripped surfaces; pinned medial-wall pial
   vertices (pial==white) become legal closest-vertex candidates up to 20 hops (~6mm FWHM)
   -> thickness UNDERESTIMATED in band bordering medial wall (entorhinal, parahippocampal,
   cingulate, insula) in v7 relative to v6. Devs' own comment concedes it.
   mris_place_surface.cpp:1472-1501, recon-all v7:4142.

F2 CONFIRMED (all versions): ROI thickness means include zero-thickness non-cortex vertices
   (same as anatomical_stats F4, independently confirmed). Downward bias in wall-adjacent ROIs;
   atrophy-dependent mismatch -> potential artifactual thinning correlate in aging/AD studies.

F3 CONFIRMED v6->v7 change (sub-mm data only): v6 auto-enabled first-WM-peak white relocation
   for hires (gated by STALE/uninitialized next_val — real bug, acknowledged in v7 comment);
   v7 turned it off. v6-hires vs v7-hires: thickness shift in high-myelin regions (M1,V1,auditory).
   v6 mrisurf.c:38093-38097,38213; v7 mrisurf_mri.cpp:2101-2108 (flag off).

F4 CONFIRMED v5.3->v6 change: pial border_hi moved GM-0.5σ -> GM-1σ ("push pial surfaces
   further out BRF 12/10/2015") -> v6+ measures cortex systematically THICKER than v5.3.
   mris_make_surfaces.c:740-743 = dev mrisurf_mri.cpp:7921-7923.

F5 CONFIRMED v6->v7 redesign: T2/FLAIR pial refinement — v6 global histogram, 1mm outward cap
   (thins); v7 local histograms, 3mm outward, location cost, FLAIR inside-peak pct 0.01 with
   author's own "typo?" comment (thickens). Cross-version T2pial/FLAIRpial cohorts inherit
   systematic pial offset. (No cohort papers matched T2/FLAIR pial signals, so low exposure.)

F6 PLAUSIBLE (all versions, group-differential): hidden 1mm look-ahead in border acceptance
   rejects true boundary where cortex <1mm or sulci <1mm wide -> white pulled outward in
   thinnest cortex (attenuates atrophy effects), pial outward in tight sulci. mrisurf_mri.cpp:
   2162-2190 + min_val fallback 2486-2501. Same in all versions (bias, not version confound).

F7 mechanism CONFIRMED: ?h.thickness contains exact 0 across medial wall; FS's own qcache masks
   with --cortex, but third-party vertexwise pipelines smoothing without the mask bleed a
   "thinning halo" ~1 FWHM into medial cortex.

VERIFIED CORRECT: thickness metric properly symmetrized (Fischl-Dale, byte-identical v6->dev,
5mm cap, 20-hop search seeded with same-vertex distance); v7 CBV/AutoDetGWStats faithfully
replicate v6 formulas for standard 1mm T1 (intentionally comparable); qcache smoothing masks
medial wall.

MAPS TO: surface_recon/roi_morphometry (85 papers). Key discriminators: version mixing
(F1/F3/F4/F5), hires sub-mm data (F3), atrophy studies of entorhinal/medial ROIs (F2/F6).
