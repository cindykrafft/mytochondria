Title: (fieldtrip/website) faq/matlab/octave.md: replace "we don't have precise details" with the survey result

<!-- Draft edit for the website's Octave FAQ page, offered in the last paragraph of reply-2614-survey-results.md. Only turn it into a branch/PR if schoffelen says that is where he wants it. Replace the third paragraph of faq/matlab/octave.md ("Some people have reported that Octave works fine for them, although we don't have precise details on what works and what not.") and the outdated Octave 3.4.0 sentence with the text below; keep the rest of the page. Numbers from audits/fieldtrip/verify/octave_survey/README.md; update them if the fixes have been merged by then. -->

## What works and what not

In September 2026 we ran every FieldTrip test function that needs no data (471 of them) under GNU Octave 8.4 with the `statistics` and `signal` packages, without compiling the MEX files and without a display. With FieldTrip master of that month 61 % of them pass as they are ([details](https://github.com/fieldtrip/fieldtrip/issues/2614)). What stops the others, in order:

- **MATLAB functions that Octave does not have**: `pad`, `strip`, `table`, `save -nocompression`, `round(x, n)`, `envelope`, `parula`, `clim`, `mle` and a few more. These fail in reading atlases (`ft_read_atlas`, `ft_sourceparcellate`), in a few test scripts and in some plotting code.
- **MEX files**: forward modelling (`plgndr`, `meg_leadfield1`, the BEM solvers) and the SPM-based volume functions (`spm_bwlabel`, `file_array`) need the MEX files compiled for Octave with `mkoctfile --mex`; see the [compilation FAQ](/faq/matlab/compile).
- **Plotting**: `ft_multiplotTFR`, `ft_singleplotTFR`, `ft_topoplot*`, `ft_plot_slice`/`ft_plot_ortho`, `ft_plot_headshape` and the interactive functions use MATLAB graphics features that Octave's toolkits do not have (`colormap` per figure, `patch` colour data, `getframe`, `zoom`, `rotate3d`). This is the MATLAB-specific part of FieldTrip.
- **Multitapers**: Octave's `signal` package has no `dpss`, so `ft_freqanalysis` with the default `cfg.taper = 'dpss'` does not run; use `cfg.taper = 'hanning'` or `'sine'`, see [this FAQ](/faq/spectral/dpss_without_toolbox).
- **External toolboxes**: OpenMEEG, dipoli and the xunit/MOxUnit test frameworks are not part of FieldTrip.

Preprocessing, trial definition and redefinition, artifact rejection, timelock and frequency analysis with Hanning or sine tapers, statistics (cluster-based permutation tests without `spm_bwlabel`, i.e. with `cfg.clusterthreshold` on channel neighbours), source analysis with precomputed leadfields, connectivity analysis and the file readers work.
