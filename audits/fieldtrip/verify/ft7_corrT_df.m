pkg load statistics; addpath([pwd '/shims'])
addpath(getenv('FIELDTRIP')); ft_defaults
warning('off','all');
randn('seed',2);
for n = [8 12 20 40]
  dat = randn(3, n); design = randn(1, n);
  cfg = []; cfg.ivar = 1; cfg.computecritval = 'yes'; cfg.computeprob = 'yes'; cfg.tail = 0; cfg.alpha = 0.05;
  s = ft_statfun_correlationT(cfg, dat, design);
  r = s.rho(1); t = s.stat(1);
  printf('n=%2d: FieldTrip df=%d critval=%.4f | correct df=%d critval=%.4f | ratio %.3f\n', n, s.df, s.critval(2), n-2, tinv(0.975,n-2), s.critval(2)/tinv(0.975,n-2));
  printf('       t from r: %.4f uses sqrt(n-2)=%.4f ; FieldTrip prob=%.5f vs prob with df=n-2: %.5f\n', t, r*sqrt(n-2)/sqrt(1-r^2), s.prob(1), 2*tcdf(-abs(t), n-2));
end
