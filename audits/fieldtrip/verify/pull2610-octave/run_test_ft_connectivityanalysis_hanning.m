pkg load statistics signal
addpath('/home/user/research-software-audit/audits/fieldtrip/verify/pull2610-octave'); addpath('/home/user/research-software-audit/audits/fieldtrip/verify/shims');
addpath('/home/user/fieldtrip'); ft_defaults; addpath('/home/user/fieldtrip/test'); addpath('/home/user/fieldtrip/external/signal/dpss_hack');
addpath('/home/user/research-software-audit/audits/fieldtrip/verify/pull2610-octave'); addpath('/home/user/research-software-audit/audits/fieldtrip/verify/shims');
warning('off','all'); set(0,'DefaultFigureVisible','off');
try
  test_ft_connectivityanalysis_hanning;
  printf('RESULT %s PASS\n', 'test_ft_connectivityanalysis_hanning');
catch e
  msg = strrep(strtrim(e.message), char(10), ' ');
  printf('RESULT %s FAIL: %s\n', 'test_ft_connectivityanalysis_hanning', msg(1:min(end,300)));
end
