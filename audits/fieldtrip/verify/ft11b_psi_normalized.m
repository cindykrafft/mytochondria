addpath(getenv('FIELDTRIP')); addpath([getenv('FIELDTRIP') '/connectivity']); ft_defaults
warning('off','all'); randn('seed',3);
m = 20; nbin = 3;
C = zeros(1,2,2,m); coh = 0.6*exp(1i*(0.3*(1:m) + 0.4*randn(1,m)));
C(1,1,1,:) = 1; C(1,2,2,:) = 1; C(1,1,2,:) = coh; C(1,2,1,:) = conj(coh);
psi = ft_connectivity_psi(C, 'dimord', 'rpt_chan_chan_freq', 'nbin', nbin, 'normalize', 'yes', 'hasrpt', 1);
p = squeeze(psi(1,2,:))';
printf('normalize=yes: PSI at bins %d..%d = ', m-nbin-1, m); printf('%g ', p(m-nbin-1:m)); printf('\n');
printf('bins 1..%d finite: %d of %d\n', m-nbin-1, sum(isfinite(p(1:m-nbin-1))), m-nbin-1);
