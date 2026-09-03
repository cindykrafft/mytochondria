pkg load statistics signal
addpath('/home/user/fieldtrip'); ft_defaults; addpath('/home/user/fieldtrip/test'); addpath('/home/user/fieldtrip/external/signal/dpss_hack');
warning('off','all'); set(0,'DefaultFigureVisible','off');
try
  test_pull2610;
  printf('RESULT %s PASS\n', 'test_pull2610');
catch e
  msg = strrep(strtrim(e.message), char(10), ' ');
  printf('RESULT %s FAIL: %s\n', 'test_pull2610', msg(1:min(end,300)));
end
