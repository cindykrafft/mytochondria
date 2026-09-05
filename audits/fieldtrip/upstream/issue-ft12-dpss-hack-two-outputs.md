Title: ft_specest_mtmfft: taper='dpss' fails through external/signal/dpss_hack (one-output dpss), so the no-toolbox route and Octave cannot use multitapers

<!-- Requested by schoffelen on PR #2610 (2026-09-04): "my suggestion would be to create an issue out of this ... One potential fix here would be to add a second output argument in the dpss_hack route. How to address this in Octave, I wouldn't know." No issue template in this repo. -->

**Description of the problem**

`external/signal/dpss_hack` is the route for users without the Signal Processing Toolbox (its README: made for the 2013 Toronto workshop). `ft_specest_mtmfft` asks the taper function for two outputs:

    [tap, w] = double_dpss(ndatsample, ndatsample*(tapsmofrq./fsample));   % ft_specest_mtmfft.m:172
    ...
    function [tap, w] = double_dpss(a, b, varargin)                         % :429
    [tap, w] = dpss(double(a), double(b), varargin{:});

and `dpss_hack/dpss.m` returns one (`function dps_seq = dpss(seq_length, time_halfbandwidth)`), so every `taper='dpss'` call through the hack stops before any spectrum is computed:

    addpath(fullfile(fileparts(which('ft_defaults')), 'external', 'signal', 'dpss_hack'));
    dat = randn(2, 1000);
    ft_specest_mtmfft(dat, (1:1000)/1000, 'taper', 'dpss', 'tapsmofrq', 2, 'output', 'pow')

    MATLAB (no Signal Processing Toolbox):  Too many output arguments.
    Octave 8.4:                             error: dpss: function called with too many outputs

The same call with `'taper', 'hanning'` runs. `ft_specest_mtmconvol` (:196, :441) and `ft_specest_irasa` (:185, :195) ask `dpss` for one output and are not affected, so through `ft_freqanalysis` it is `method='mtmfft'` with the default `taper='dpss'` that fails, which is what the tutorials use. Octave has no `dpss` at all (the `signal` package does not provide it), so the hack is the only multitaper route there.

The second output is used by `adaptspec_dpss` on every dpss call (`:306`, `:358`), not only for `weightopt='eig'/'adapt'`: with the default `'mean'` it still receives `w` and the `se` output is derived from it.

**Suggested fix**

Return the concentrations from the hack as well. They depend on the time-bandwidth product and the taper index, not on the interpolation to `seq_length`, so they can be precomputed next to the tapers:

    % precompute_dpss.m
    [w{i}, e{i}] = dpss(n, n*s(i)/1000);
    % dpss.m
    function [dps_seq, e] = dpss(seq_length, time_halfbandwidth)
    ...
    e = e{i};

with `precompute_dpss.mat` regenerated once on a machine that has the toolbox (it is a one-off; the file is what ships). `ft_specest_mtmfft` would then run through the hack under both MATLAB-without-toolbox and Octave; the approximation caveat in the hack's README applies to the tapers and the concentrations alike.

**Environment:** FieldTrip master @ 9c4a3af, Octave 8.4; script `audits/fieldtrip/verify/ft12_dpss_hack_two_outputs.m` in https://github.com/cindykrafft/mytochondria.
