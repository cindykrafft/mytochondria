% Executes the exact assertions of tests/test_spm_ECdensity.m
% (path set by caller decides patched vs old spm_ECdensity)
fails = 0; checks = 0;
function [f,c] = vq(act, expd, rtol, f, c)
  c = c + 1;
  if any(abs(act(:)-expd(:)) > rtol*abs(expd(:))), f = f + 1; end
end

% test_chi2_reference_values
EC = spm_ECdensity('X',15,[1 10]);
[fails,checks]=vq(EC(2),1.875960195166651e-01,1e-12,fails,checks);
[fails,checks]=vq(EC(3),1.930554347139083e-01,1e-12,fails,checks);
[fails,checks]=vq(EC(4),6.622457656369271e-02,1e-12,fails,checks);
EC = spm_ECdensity('X',8,[1 3]);
[fails,checks]=vq(EC(2),7.766134591989517e-02,1e-12,fails,checks);
[fails,checks]=vq(EC(3),1.094369452067079e-01,1e-12,fails,checks);
[fails,checks]=vq(EC(4),1.113765748270419e-01,1e-12,fails,checks);

% test_chi2_df1_matches_gaussian
t = [8 15 25];
ECX = spm_ECdensity('X',t,[1 1]); ECZ = spm_ECdensity('Z',sqrt(t),[]);
[fails,checks]=vq(ECX(1,:),2*ECZ(1,:),1e-8,fails,checks);
for d = 2:4, [fails,checks]=vq(ECX(d,:),2*ECZ(d,:),1e-10,fails,checks); end

% test_chi2_matches_F_limit
V = 1e8;
for v = [3 6 10]
  ECX = spm_ECdensity('X',t,[1 v]); ECF = spm_ECdensity('F',t/v,[v V]);
  for d = 2:4, [fails,checks]=vq(ECX(d,:),ECF(d,:),1e-5,fails,checks); end
end

% test_t_matches_gaussian_limit
tz = [2 3 4 5];
ECT = spm_ECdensity('T',tz,[1 1e8]); ECZ = spm_ECdensity('Z',tz,[]);
for d = 1:4, [fails,checks]=vq(ECT(d,:),ECZ(d,:),1e-5,fails,checks); end

fprintf('%d/%d assertions failed (using %s)\n', fails, checks, which('spm_ECdensity'));
