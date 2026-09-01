% Regression test for the spm_ECdensity chi-squared fix.
% Executes the REAL patched MATLAB code (from the pushed branch) in Octave,
% against the pre-fix version extracted from git, using two exact identities
% that rely only on independent, verified branches (Z and F).

addpath('/home/user/spmfork');                              % patched SPM
addpath('/tmp/claude-0/-home-user-afni/d65df75e-7d82-531d-babc-bc1cc192b046/scratchpad/ec_test'); % old copy

t    = [8 15 25];
fail = 0;

fprintf('== Identity A: chi2_1 == Z^2  =>  rho_d^X(t;v=1) = 2*rho_d^Z(sqrt(t)) ==\n');
ECX  = spm_ECdensity('X',t,[1 1]);
ECXo = spm_ECdensity_old('X',t,[1 1]);
ECZ  = spm_ECdensity('Z',sqrt(t),[]);
for d = 2:4
    rn = ECX(d,:)  ./ (2*ECZ(d,:));
    ro = ECXo(d,:) ./ (2*ECZ(d,:));
    ok = all(abs(rn-1) < 1e-10);
    fail = fail + ~ok;
    fprintf(' EC(%d): new/expected = [%.10f %.10f %.10f] %s | old/expected = [%.3f %.3f %.3f]\n', ...
        d, rn, tern(ok,'PASS','FAIL'), ro);
end

fprintf('\n== Identity B: chi2_v == v*F(v,inf)  =>  rho_d^X(t) = rho_d^F(t/v; v,V), V->inf ==\n');
V = 1e8;
for v = [3 6 10]
    ECX  = spm_ECdensity('X',t,[1 v]);
    ECXo = spm_ECdensity_old('X',t,[1 v]);
    ECF  = spm_ECdensity('F',t/v,[v V]);
    for d = 2:4
        rn = ECX(d,:)  ./ ECF(d,:);
        ro = ECXo(d,:) ./ ECF(d,:);
        ok = all(abs(rn-1) < 1e-5);      % reference finite-V error ~1.5e-6 at V=1e8
        fail = fail + ~ok;
        fprintf(' v=%2d EC(%d): new/F-lim = [%.6f %.6f %.6f] %s | old/F-lim = [%.3f %.3f %.3f]\n', ...
            v, d, rn, tern(ok,'PASS','FAIL'), ro);
    end
end

fprintf('\n== No-regression: untouched branches identical old vs new ==\n');
tz = [2 3 4 5];
chk = {{'Z',tz,[]}, {'T',tz,[1 20]}, {'F',[2 4 8],[3 40]}};
nm  = {'Z','T','F'};
for i = 1:3
    dnew = spm_ECdensity(chk{i}{:});
    dold = spm_ECdensity_old(chk{i}{:});
    ok   = isequal(dnew,dold);
    fail = fail + ~ok;
    fprintf(' %s branch: %s\n', nm{i}, tern(ok,'IDENTICAL','DIFFERS'));
end
% chi2 orders 0 and 1 (EC rows 1-2) must also be unchanged
ECX  = spm_ECdensity('X',t,[1 6]);  ECXo = spm_ECdensity_old('X',t,[1 6]);
ok   = max(abs(ECX(1:2,:)(:) - ECXo(1:2,:)(:))) < 1e-14;
fail = fail + ~ok;
fprintf(' X branch EC(1:2) (untouched orders): %s\n', tern(ok,'IDENTICAL','DIFFERS'));

fprintf('\n== End-to-end: spm_P_RF corrected peak p, chi2_10 field, R=[1 33.4 354.7 705.7] ==\n');
R = [1 33.4 354.7 705.7];
for z = [25 31 40]
    Pn = spm_P_RF(1,0,z,[1 10],'X',R,1);
    fprintf(' u=%2d: corrected P (patched) = %.4g\n', z, Pn);
end

fprintf('\n%s\n', tern(fail==0, 'ALL CHECKS PASSED', sprintf('%d CHECK(S) FAILED', fail)));
if fail>0, exit(1); end

