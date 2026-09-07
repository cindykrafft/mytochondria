# FAQ draft: "dpss" errors without the Signal Processing Toolbox

<!-- For the FieldTrip website (fieldtrip/website, faq/). Requested by schoffelen on #2614 (2026-09-07): "It would be good to have a piece of documentation (as a FAQ on the website) that describes the issue, and what can be done about it." Filing it needs a fork of fieldtrip/website; the text is the deliverable. -->

Title: Why do I get an error about `dpss` and what can I do about it?

FieldTrip's multitaper spectral estimation (`cfg.method = 'mtmfft'` and `'mtmconvol'` with the default `cfg.taper = 'dpss'`) uses Slepian tapers computed by the `dpss` function of the MATLAB Signal Processing Toolbox. Without that toolbox, or under GNU Octave, `ft_freqanalysis` stops with a message such as

    Undefined function 'dpss' for input arguments of type 'double'.
    Too many output arguments.                                   (when external/signal/dpss_hack is on the path)
    error: 'dpss' undefined                                       (Octave)

You have three options.

**1. Use a taper that does not need the toolbox.** Set `cfg.taper = 'hanning'` (FieldTrip ships its own `hanning` in `external/signal`), or any other window from that directory. This gives a single-taper estimate: no spectral smoothing across frequencies, so `cfg.tapsmofrq` is not used. It is the right choice for most event-related analyses of low-frequency activity, and the tutorials that use multitapers for high-frequency (gamma) activity can be run with `'hanning'` at the cost of a noisier high-frequency estimate.

**2. Use sine tapers.** `cfg.taper = 'sine'` with `cfg.tapsmofrq` set as you would for `'dpss'`. Sine tapers (Riedel & Sidorenko, 1995) are an orthogonal family that approximates the Slepian sequences and needs no toolbox; FieldTrip implements them itself. They give the spectral smoothing of the multitaper method with slightly worse sidelobe suppression than true Slepians.

**3. The `dpss_hack` (not recommended).** `external/signal/dpss_hack` interpolates precomputed Slepian tapers. It was made for a 2013 workshop, is only an approximation for settings close to the precomputed ones, and at present cannot be used with `ft_freqanalysis`' `'mtmfft'` method at all, because that method also needs the taper concentrations that the hack does not provide (issue #2614). Prefer option 1 or 2.

Under GNU Octave, options 1 and 2 are the ones that work; see also the [Octave FAQ](/faq/matlab/octave/).
