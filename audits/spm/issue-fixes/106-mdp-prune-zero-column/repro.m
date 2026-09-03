% Reproduction for spm/spm#106: spm_MDP_VB_prune returns NaN priors when a
% column of the likelihood tensor is left with no prior mass after pruning.
% Usage (Octave/MATLAB): set SPMSRC to an SPM checkout, then run this file.
S = getenv('SPMSRC'); addpath(S); addpath(fullfile(S,'toolbox','DEM'));
shim = fullfile(fileparts(mfilename('fullpath')),'octshim');
if exist(shim,'dir'), addpath(shim); end     % Octave: sum(x,'all')
P = getenv('PREFIX');                        % optional dir holding the
if ~isempty(P), addpath(P); end              % pre-fix spm_MDP_VB_prune.m
format long g
fprintf('spm_MDP_VB_prune: %s\n', which('spm_MDP_VB_prune'));

fprintf('\n[1] SIMPLE: prior is zero at every entry that survives pruning\n');
qA = [64; 1];  pA = [0; 1];
[sA,rA] = spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
disp('reduced posterior sA ='), disp(sA'), disp('reduced prior rA ='), disp(rA')

fprintf('\n[2] SIMPLE: prior column of zeros (never-visited state), posterior has counts;\n    second column is healthy\n');
qA = [64 64; 1 1];  pA = [0 1; 0 1];
[sA,rA] = spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
disp('sA ='), disp(sA), disp('rA ='), disp(rA)

fprintf('\n[3] MI (default) mode, same input as [2]\n');
[sA,rA] = spm_MDP_VB_prune(qA,pA,0,0);
disp('sA ='), disp(sA), disp('rA ='), disp(rA)

fprintf('\n[4] what the NaN prior does on the next call (as in spm_RDP_update loops)\n');
[sA2,rA2] = spm_MDP_VB_prune(sA + 1, rA, 0, 0, [], 'SIMPLE');
disp('sA ='), disp(sA2), disp('rA ='), disp(rA2)
fprintf('\nany NaN in outputs: %d\n', any(isnan([sA(:);rA(:);sA2(:);rA2(:)])));
