% FT1a: with cfg.numrandomization='all', the identity permutation reproduces the
% observed statistic exactly; the strict '<' comparison excludes that tie and no
% +1 is added, so the reported p is short by exactly 1/Nperm and can be 0.
pkg load statistics
addpath(getenv('FIELDTRIP')); ft_defaults
warning('off','all');
rand('seed',1); randn('seed',1);
nsubj = 10;
dat    = randn(1, 2*nsubj);            % one sample (channel/time point), paired data
dat(1:nsubj) = dat(1:nsubj) + 3;       % strong effect in condition 1 -> observed t is the most extreme
design = [ones(1,nsubj) 2*ones(1,nsubj); 1:nsubj 1:nsubj];
cfg = [];
cfg.statistic = 'ft_statfun_depsamplesT';
cfg.ivar = 1; cfg.uvar = 2;
cfg.numrandomization = 'all';          % 2^10 = 1024 sign flips, identity included
cfg.correctm = 'no';
cfg.tail = 1;
cfg.feedback = 'no';
stat = ft_statistics_montecarlo(cfg, dat, design);
printf('observed t = %.3f\n', stat.stat);
printf('FieldTrip prob (numrandomization=all, tail=1) = %.6f\n', stat.prob);
printf('exact one-sided permutation p should be 1/1024 = %.6f\n', 1/1024);
% now a non-extreme case: weaker effect so some flips exceed the observed
dat2 = dat; dat2(1:nsubj) = dat2(1:nsubj) - 2.4;
stat2 = ft_statistics_montecarlo(cfg, dat2, design);
% recompute the exact distribution ourselves from the same 1024 flips
d = dat2(1:nsubj) - dat2(nsubj+1:end);
tobs = sqrt(nsubj)*mean(d)/std(d);
T = zeros(1,2^nsubj);
for i = 1:2^nsubj
  s = 1 - 2*(dec2bin(i-1,nsubj)=='1'); ds = d.*s;
  T(i) = sqrt(nsubj)*mean(ds)/std(ds);
end
printf('\nweaker effect: observed t = %.3f\n', tobs);
printf('FieldTrip prob                          = %.6f  (= #{T >  tobs}/1024 = %d/1024)\n', stat2.prob, sum(T>tobs));
printf('standard exact p = #{T >= tobs}/1024    = %.6f  (%d/1024)\n', sum(T>=tobs)/1024, sum(T>=tobs));
