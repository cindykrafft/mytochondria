pkg load statistics signal
addpath('/home/user/fieldtrip'); ft_defaults; addpath('/home/user/fieldtrip/test'); addpath('/home/user/fieldtrip/external/signal/dpss_hack');
warning('off','all'); set(0,'DefaultFigureVisible','off');
try
  test_ft_connectivity_psi;
  printf('RESULT %s PASS\n', 'test_ft_connectivity_psi');
catch e
  msg = strrep(strtrim(e.message), char(10), ' ');
  printf('RESULT %s FAIL: %s\n', 'test_ft_connectivity_psi', msg(1:min(end,300)));
end
