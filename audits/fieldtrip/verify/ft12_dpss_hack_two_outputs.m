pkg load statistics signal
addpath('/home/user/fieldtrip'); ft_defaults; warning('off','all');
% the route intended for users without the Signal Processing Toolbox
addpath('/home/user/fieldtrip/external/signal/dpss_hack');
dat = randn(2, 1000); fsample = 1000;
try
  [spec, ntaper, freqoi] = ft_specest_mtmfft(dat, (1:1000)/fsample, 'taper', 'dpss', 'tapsmofrq', 2, 'output', 'pow');
  printf('mtmfft dpss via dpss_hack: OK, %d tapers\n', ntaper(1));
catch e
  printf('mtmfft dpss via dpss_hack: ERROR: %s\n', strtrim(e.message));
end
try
  [spec, ntaper, freqoi] = ft_specest_mtmfft(dat, (1:1000)/fsample, 'taper', 'hanning', 'output', 'pow');
  printf('mtmfft hanning: OK\n');
catch e
  printf('mtmfft hanning: ERROR: %s\n', strtrim(e.message));
end
try
  [spec, ntaper, freqoi] = ft_specest_mtmconvol(dat, (1:1000)/fsample, 'taper', 'dpss', 'tapsmofrq', 4, 'timeoi', 0.5, 'timwin', 0.5*ones(1,5), 'freqoi', 10:10:50);
  printf('mtmconvol dpss via dpss_hack: OK\n');
catch e
  printf('mtmconvol dpss via dpss_hack: ERROR: %s\n', strtrim(e.message));
end
which dpss
