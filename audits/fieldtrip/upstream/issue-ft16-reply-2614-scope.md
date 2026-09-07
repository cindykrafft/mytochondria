Title: (comment on #2614) agreed it is minor; sine tapers as the answer; FAQ draft and an Octave survey on offer

<!-- Reply to schoffelen's two comments of 2026-09-07 on issue #2614. Plain tone; he called the issue low return on investment and proposed larger work instead. -->

Agreed that this one is minor as filed: nobody reaches the hack without editing the path by hand, and `'sine'` and `'hanning'` already cover the no-toolbox case. Two things from your list I can do something about:

**A FAQ.** A draft is in the Mytochondria repository (`audits/fieldtrip/upstream/faq-dpss-without-signal-toolbox.md`): what the error looks like without the toolbox and under Octave, `cfg.taper = 'hanning'` (FieldTrip's own `hanning` in `external/signal`), `cfg.taper = 'sine'` with `tapsmofrq` as the toolbox-free multitaper route, and the hack as not recommended. If that is the shape you want I will open it as a PR on the website repository; edit freely.

**Why only `mtmfft` has the adaptive weighting.** As far as the code shows: `weightopt` calls `adaptspec_dpss` with the taper concentrations to form Thomson's weights for one spectrum per trial. `ft_specest_mtmconvol` builds a separate taper set per frequency of interest (`tapsmofrq` per `freqoi`), so the same weighting would need a concentration vector per frequency and a per-frequency call, and `ft_specest_irasa` uses a single dpss taper, where there is nothing to weight. So it is not inconsistent as much as unfinished: `mtmconvol` could get the same option by asking `dpss` for the second output per frequency and applying `adaptspec_dpss` per frequency. I have not measured how much it changes a time-frequency estimate; if you want it, I would prototype it and report the difference before opening a PR.

**Octave survey.** I have the harness for it (Octave 8.4 plus shims for the handful of MATLAB-only functions; that is how the tests in #2608 and #2610 were run). Running every `DATA no` test function on a recent Octave and writing up what passes, what fails and why, for the Octave FAQ page, is a bounded job. I can do it if the result is something you would use; it would otherwise be noise, so say the word.

Nothing further from me on the hack itself; closing this as "won't fix" with a pointer to the FAQ would be fine by me.
