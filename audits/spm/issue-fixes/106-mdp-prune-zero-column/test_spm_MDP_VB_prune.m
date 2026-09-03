classdef test_spm_MDP_VB_prune < matlab.unittest.TestCase
% Unit Tests for spm_MDP_VB_prune
%__________________________________________________________________________

% Copyright (C) 2026 Wellcome Centre for Human Neuroimaging


methods (Test)


function test_simple_reduces_column_with_prior_mass(testCase)
% a column whose small entry is pruned: reference behaviour is unchanged
qA = [64; 1];
pA = [ 1; 1];
[sA,rA] = spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
testCase.verifyEqual(sA, [65; 0], 'AbsTol', 1e-10);
testCase.verifyEqual(rA, [ 2; 0], 'AbsTol', 1e-10);
end

function test_simple_prior_zero_at_surviving_entries(testCase)
% pruning removes every entry that carries prior mass (issue #106):
% the column can not be rescaled and must be left unchanged, not NaN
qA = [64; 1];
pA = [ 0; 1];
[sA,rA] = spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
testCase.verifyFalse(any(isnan(sA(:))));
testCase.verifyFalse(any(isnan(rA(:))));
testCase.verifyEqual(sA, qA);
testCase.verifyEqual(rA, pA);
end

function test_simple_zero_prior_column_confined(testCase)
% a prior column of zeros (never-visited state) next to a healthy column:
% the zero column is left unchanged and the healthy column reduces as usual
qA = [64 64; 1 1];
pA = [ 0  1; 0 1];
[sA,rA] = spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
testCase.verifyFalse(any(isnan(sA(:))));
testCase.verifyFalse(any(isnan(rA(:))));
testCase.verifyEqual(sA(:,1), qA(:,1));
testCase.verifyEqual(rA(:,1), pA(:,1));
testCase.verifyEqual(sA(:,2), [65; 0], 'AbsTol', 1e-10);
testCase.verifyEqual(rA(:,2), [ 2; 0], 'AbsTol', 1e-10);
end

function test_mi_zero_prior_column(testCase)
% default (mutual-information) mode with a prior column of zeros
qA = [64 64; 1 1];
pA = [ 0  1; 0 1];
[sA,rA] = spm_MDP_VB_prune(qA,pA,0,0);
testCase.verifyFalse(any(isnan(sA(:))));
testCase.verifyFalse(any(isnan(rA(:))));
testCase.verifyEqual(sA(:,1), qA(:,1));
testCase.verifyEqual(rA(:,1), pA(:,1));
testCase.verifyEqual(sum(rA(:,2)), sum(pA(:,2)), 'AbsTol', 1e-10);
end

function test_tensor_shape_preserved(testCase)
% three-dimensional likelihood tensor with one all-zero prior column
qA = rand(3,2,2) + 1;
pA = ones(3,2,2);
qA(:,1,1) = [64; 1; 1];
pA(:,1,1) = 0;
[sA,rA] = spm_MDP_VB_prune(qA,pA,0,0,[],'SIMPLE');
testCase.verifyEqual(size(sA), size(qA));
testCase.verifyEqual(size(rA), size(pA));
testCase.verifyFalse(any(isnan(sA(:))));
testCase.verifyFalse(any(isnan(rA(:))));
testCase.verifyEqual(sA(:,1,1), qA(:,1,1));
testCase.verifyEqual(rA(:,1,1), pA(:,1,1));
end

end % methods (Test)

end % classdef
