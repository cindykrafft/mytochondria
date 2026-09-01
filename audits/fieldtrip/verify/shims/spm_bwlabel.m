function [L, num] = spm_bwlabel(bw, n)
% pure-MATLAB stand-in for the SPM mex, sufficient for vector (1-D) inputs:
% labels contiguous runs of nonzero elements. Errors on higher-dimensional input.
if sum(size(bw)>1) > 1
  error('spm_bwlabel shim only supports 1-D input');
end
v = bw(:)' ~= 0;
L = zeros(size(bw)); num = 0; inrun = false;
for i = 1:numel(v)
  if v(i)
    if ~inrun, num = num + 1; inrun = true; end
    L(i) = num;
  else
    inrun = false;
  end
end
