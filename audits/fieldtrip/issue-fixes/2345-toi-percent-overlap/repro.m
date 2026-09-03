% Reproduction for fieldtrip/fieldtrip#2345: cfg.toi = 'NN%' in ft_freqanalysis
% (method = 'mtmconvol') is documented as the percentage of OVERLAP between the
% smallest time windows, but the step between output time points equals
% NN% of the window, i.e. the overlap is 100-NN %.
warning('off','all'); pkg load statistics signal
% FIELDTRIP = checkout under test; FTSHIMS/FTSHIMS2 = audits/fieldtrip/verify/shims and verify/pull2610-octave (Octave only)
FT = getenv('FIELDTRIP'); addpath(getenv('FTSHIMS')); addpath(getenv('FTSHIMS2')); addpath(FT); ft_defaults; addpath(fullfile(FT,'external','signal','dpss_hack'));
warning('off','all');

% synthetic data: 2 trials, 1 channel, 200 Hz, 0..2 s
data = [];
data.label   = {'chan1'};
data.fsample = 200;
for k = 1:2
  data.time{k}  = 0:1/data.fsample:2;
  data.trial{k} = randn(1, numel(data.time{k}));
end

cfg           = [];
cfg.method    = 'mtmconvol';
cfg.taper     = 'hanning';
cfg.foi       = 10;
cfg.t_ftimwin = 0.5;          % 500 ms window
cfg.output    = 'pow';
cfg.feedback  = 'none';

printf('window = %g s\n', cfg.t_ftimwin);
printf('%8s %8s %14s %14s\n', 'cfg.toi', 'ntime', 'step (s)', 'overlap');
for pct = [10 25 50 75 90]
  cfg.toi = sprintf('%d%%', pct);
  freq    = ft_freqanalysis(cfg, data);
  step    = mean(diff(freq.time));
  printf('%8s %8d %14.4f %13.1f%%\n', cfg.toi, numel(freq.time), step, 100*(1 - step/cfg.t_ftimwin));
end
