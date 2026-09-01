function test_pull2610

% WALLTIME 00:10:00
% MEM 1gb
% DEPENDENCY ft_connectivity_psi
% DATA no

% This test covers pull request 2610 (issue 2609): the phase slope index must
% be computed from the products conj(C(f))*C(f+df) only. Previously the raw
% coherency at the highest frequency was left in the product vector, so the
% last nbin+1 output bins were offset by imag(C(fmax)), and with
% normalize='yes' those bins were +/-Inf. It checks:
%
%   1) ft_connectivity_psi matches an independent implementation of the
%      Nolte et al. (2008) definition at every frequency bin, including the
%      bins whose window reaches the top of the frequency range;
%   2) the normalized variant is finite everywhere and matches its reference.

rng(2,'twister');
nfreq = 20; nbin = 3; nchan = 2;

% synthetic cross-spectral density: 1 replicate, 2 channels, 20 frequencies
csd = zeros(1, nchan, nchan, nfreq);
for f = 1:nfreq
  p1 = 1 + rand; p2 = 1 + rand;
  c  = 0.7*sqrt(p1*p2)*exp(1i*(0.2*f + 0.5*randn));
  csd(1,:,:,f) = [p1 c; conj(c) p2];
end

% ----------------------------------------------------------------------------
% independent reference implementation
% ----------------------------------------------------------------------------
coh = squeeze(csd(1,1,2,:)) ./ sqrt(squeeze(csd(1,1,1,:)) .* squeeze(csd(1,2,2,:)));
prod = conj(coh(1:end-1)) .* coh(2:end);          % products for adjacent bins
% ft_connectivity_psi normalizes each product by the magnitudes of adjacent
% products plus one (the '+1' is inherited from the original implementation);
% beyond the last product there is nothing, so the last normalizer is 1
prodpad = [prod; 0];
w       = abs(prodpad(1:end-1)) .* abs(prodpad(2:end)) + 1;
ref  = zeros(nfreq,1);
refn = zeros(nfreq,1);
for k = 1:nfreq
  b = max(1, k-nbin);
  e = min(nfreq-1, k+nbin);                        % the last product is at index nfreq-1
  ref(k)  = imag(sum(prod(b:e)));
  refn(k) = imag(sum(prod(b:e) ./ w(b:e)));
end

% ----------------------------------------------------------------------------
% 1) unnormalized PSI equals the reference at every bin
% ----------------------------------------------------------------------------
psi = ft_connectivity_psi(csd, 'dimord', 'rpt_chan_chan_freq', 'nbin', nbin, 'normalize', 'no');
y   = squeeze(psi(1,2,:));
assert(all(isfinite(y)), 'phase slope index contains non-finite values');
assert(max(abs(y - ref)) < 1e-10, ...
  'phase slope index differs from the reference definition (max abs diff %g)', max(abs(y - ref)));

% ----------------------------------------------------------------------------
% 2) normalized PSI is finite and equals its reference
% ----------------------------------------------------------------------------
psin = ft_connectivity_psi(csd, 'dimord', 'rpt_chan_chan_freq', 'nbin', nbin, 'normalize', 'yes');
yn   = squeeze(psin(1,2,:));
assert(all(isfinite(yn)), 'normalized phase slope index contains non-finite values');
assert(max(abs(yn - refn)) < 1e-10, ...
  'normalized phase slope index differs from the reference definition (max abs diff %g)', max(abs(yn - refn)));
