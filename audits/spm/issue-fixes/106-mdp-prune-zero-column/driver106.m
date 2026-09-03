% Executes the assertions of tests/test_spm_MDP_VB_prune.m in Octave
% (path set by caller decides patched vs pre-fix spm_MDP_VB_prune)
fails = 0; checks = 0;
function [f,c] = vq(cond, f, c, name)
  c = c + 1;
  if ~cond, f = f + 1; printf('  FAIL: %s\n', name); end
end
qA=[64;1]; pA=[1;1]; [sA,rA]=spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
[fails,checks]=vq(max(abs(sA-[65;0]))<1e-10,fails,checks,'reduce sA');
[fails,checks]=vq(max(abs(rA-[2;0]))<1e-10,fails,checks,'reduce rA');
qA=[64;1]; pA=[0;1]; [sA,rA]=spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
[fails,checks]=vq(~any(isnan(sA(:))),fails,checks,'surviving: sA no NaN');
[fails,checks]=vq(~any(isnan(rA(:))),fails,checks,'surviving: rA no NaN');
[fails,checks]=vq(isequal(sA,qA),fails,checks,'surviving: sA==qA');
[fails,checks]=vq(isequal(rA,pA),fails,checks,'surviving: rA==pA');
qA=[64 64;1 1]; pA=[0 1;0 1]; [sA,rA]=spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
[fails,checks]=vq(~any(isnan(sA(:))),fails,checks,'confined: sA no NaN');
[fails,checks]=vq(~any(isnan(rA(:))),fails,checks,'confined: rA no NaN');
[fails,checks]=vq(isequal(sA(:,1),qA(:,1)),fails,checks,'confined: sA col1');
[fails,checks]=vq(isequal(rA(:,1),pA(:,1)),fails,checks,'confined: rA col1');
[fails,checks]=vq(max(abs(sA(:,2)-[65;0]))<1e-10,fails,checks,'confined: sA col2');
[fails,checks]=vq(max(abs(rA(:,2)-[2;0]))<1e-10,fails,checks,'confined: rA col2');
qA=[64 64;1 1]; pA=[0 1;0 1]; [sA,rA]=spm_MDP_VB_prune(qA,pA,0,0);
[fails,checks]=vq(~any(isnan(sA(:))),fails,checks,'MI: sA no NaN');
[fails,checks]=vq(~any(isnan(rA(:))),fails,checks,'MI: rA no NaN');
[fails,checks]=vq(isequal(sA(:,1),qA(:,1)),fails,checks,'MI: sA col1');
[fails,checks]=vq(isequal(rA(:,1),pA(:,1)),fails,checks,'MI: rA col1');
[fails,checks]=vq(abs(sum(rA(:,2))-sum(pA(:,2)))<1e-10,fails,checks,'MI: mass col2');
rand('seed',1); qA=rand(3,2,2)+1; pA=ones(3,2,2); qA(:,1,1)=[64;1;1]; pA(:,1,1)=0;
[sA,rA]=spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
[fails,checks]=vq(isequal(size(sA),size(qA)),fails,checks,'tensor: size sA');
[fails,checks]=vq(isequal(size(rA),size(pA)),fails,checks,'tensor: size rA');
[fails,checks]=vq(~any(isnan(sA(:))),fails,checks,'tensor: sA no NaN');
[fails,checks]=vq(~any(isnan(rA(:))),fails,checks,'tensor: rA no NaN');
[fails,checks]=vq(isequal(sA(:,1,1),qA(:,1,1)),fails,checks,'tensor: sA col');
[fails,checks]=vq(isequal(rA(:,1,1),pA(:,1,1)),fails,checks,'tensor: rA col');
printf('%d/%d assertions failed (using %s)\n', fails, checks, which('spm_MDP_VB_prune'));
