pkg load statistics
addpath(getenv('FIELDTRIP')); ft_defaults
warning('off','all');
randn('seed',4);
nsubj = 6; nper = 8;                                  % 6 subjects x 8 trials, regress data on a covariate
dat = randn(3, nsubj*nper);
design = [randn(1, nsubj*nper); reshape(repmat(1:nsubj, nper, 1), 1, []); repmat([1 1 1 1 2 2 2 2], 1, nsubj)];
cfg = []; cfg.ivar = 1; cfg.uvar = 2;
cfg.cvar = [];
s = ft_statfun_depsamplesregrT(cfg, dat, design); printf('without cvar: ok, stat(1)=%.3f\n', s.stat(1));
cfg.cvar = 3;
try
  s = ft_statfun_depsamplesregrT(cfg, dat, design); printf('with cvar: ok\n');
catch err
  printf('with cvar: ERROR -> %s\n', err.message);
end
