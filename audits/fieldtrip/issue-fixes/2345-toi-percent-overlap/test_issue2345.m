function test_issue2345

% WALLTIME 00:10:00
% MEM 1gb
% DEPENDENCY ft_freqanalysis
% DATA no

% This test covers issue 2345: for cfg.method = 'mtmconvol', a percentage in
% cfg.toi (e.g. '90%') is documented as the degree of overlap between the
% shortest time windows in cfg.t_ftimwin. Previously the percentage was used
% as the step between consecutive time points, so '90%' gave 10% overlap
% (5 time points on 2 s of data with a 0.5 s window) and '10%' gave 90%
% overlap. The test checks that:
%
%   1) the number of output time points equals the number implied by the
%      documented meaning, i.e. a step of (1-overlap)*min(cfg.t_ftimwin);
%   2) more overlap gives more time points, not fewer;
%   3) '50%' gives the same result as before (the only value for which step
%      and overlap coincide), so existing analyses with '50%' are unaffected.

rng(1,'twister');

% synthetic data: 2 trials, 2 channels, 200 Hz, 0 to 2 s
data         = [];
data.label   = {'chan1'; 'chan2'};
data.fsample = 200;
for k = 1:2
  data.time{k}  = 0:1/data.fsample:2;
  data.trial{k} = randn(numel(data.label), numel(data.time{k}));
end

cfg           = [];
cfg.method    = 'mtmconvol';
cfg.taper     = 'hanning';
cfg.foi       = [10 20];
cfg.t_ftimwin = [0.5 0.25];    % the shortest window is 0.25 s
cfg.output    = 'pow';
cfg.feedback  = 'none';

begtim = min(cellfun(@min, data.time));
endtim = max(cellfun(@max, data.time));
minwin = min(cfg.t_ftimwin);

pct   = [10 25 50 75 90];
ntime = zeros(size(pct));
for k = 1:numel(pct)
  cfg.toi  = sprintf('%d%%', pct(k));
  freq     = ft_freqanalysis(cfg, data);
  ntime(k) = numel(freq.time);

  % 1) the documented meaning: step = (1-overlap) * shortest window
  step     = (1 - pct(k)/100) * minwin;
  expected = round((endtim - begtim) / step) + 1;
  assert(ntime(k) == expected, ...
    'cfg.toi = ''%s'' gave %d time points, expected %d for %d%% overlap of a %g s window', ...
    cfg.toi, ntime(k), expected, pct(k), minwin);
  assert(abs(freq.time(1)   - begtim) < 1e-10);
  assert(abs(freq.time(end) - endtim) < 1e-10);
end

% 2) more overlap means more time points
assert(all(diff(ntime) > 0), 'the number of time points should increase with the percentage of overlap');

% 3) '50%' is unchanged: 2 s / (0.5 * 0.25 s) + 1 = 17 time points
assert(ntime(pct == 50) == 17);

% a percentage of 100 or more (a step of zero or less) is an error
try
  cfg.toi = '100%';
  ft_freqanalysis(cfg, data);
  error('a percentage of 100 in cfg.toi should be an error');
catch err
  assert(~isempty(strfind(err.message, 'cfg.toi')), 'unexpected error: %s', err.message);
end
