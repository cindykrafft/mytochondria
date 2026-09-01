addpath(getenv('FIELDTRIP')); addpath([getenv('FIELDTRIP') '/connectivity']); ft_defaults
warning('off','all');
randn('seed',3);
m = 20; nbin = 3;
% one replicate, 2 channels, m frequency bins; diag = power, offdiag = csd
C = zeros(1,2,2,m);
coh = 0.6*exp(1i*(0.3*(1:m) + 0.4*randn(1,m)));   % coherency with a phase slope + noise
C(1,1,1,:) = 1; C(1,2,2,:) = 1;
C(1,1,2,:) = coh; C(1,2,1,:) = conj(coh);
psi = ft_connectivity_psi(C, 'dimord', 'rpt_chan_chan_freq', 'nbin', nbin, 'normalize', 'no', 'hasrpt', 1);
psi12 = squeeze(psi(1,2,:))';
% reference: Nolte et al. 2008, PSI(f) = Im( sum_{f' in window, f'+df in window} conj(C(f')) C(f'+df) )
ref = zeros(1,m);
prod = conj(coh(1:end-1)).*coh(2:end);   % m-1 products, product j pairs bins j and j+1
for k = 1:m
  lo = max(1,k-nbin); hi = min(m,k+nbin);
  ref(k) = imag(sum(prod(lo:min(hi,m-1))));
end
printf('bin   FieldTrip    reference   difference   imag(C(fmax))=%.4f\n', imag(coh(end)));
for k = m-nbin-1:m
  printf('%3d  %10.4f  %10.4f  %10.4f\n', k, psi12(k), ref(k), psi12(k)-ref(k));
end
printf('max |diff| over bins 1..%d (below the edge window): %.2e\n', m-nbin-1, max(abs(psi12(1:m-nbin-1)-ref(1:m-nbin-1))));
