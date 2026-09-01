function [L, num] = spm_bwlabel(bw, n)
% Pure-MATLAB/Octave stand-in for SPM's spm_bwlabel mex (connected-component
% labelling of a 1-D, 2-D or 3-D binary array with n = 6, 18 or 26
% connectivity; 6 -> face neighbours, i.e. 4-connectivity in 2-D).
if nargin < 2, n = 6; end
sz = size(bw); if numel(sz) < 3, sz(end+1:3) = 1; end
bw = reshape(bw ~= 0, sz);
L  = zeros(sz); num = 0;
[dx, dy, dz] = ndgrid(-1:1, -1:1, -1:1);
d  = abs(dx) + abs(dy) + abs(dz);
switch n
  case 6,  keep = d == 1;
  case 18, keep = d >= 1 & d <= 2;
  otherwise, keep = d >= 1;
end
offs = [dx(keep) dy(keep) dz(keep)];
idx = find(bw);
for start = idx'
  if L(start), continue; end
  num = num + 1; L(start) = num;
  stack = start;
  while ~isempty(stack)
    cur = stack(end); stack(end) = [];
    [i, j, k] = ind2sub(sz, cur);
    for o = 1:size(offs,1)
      ii = i + offs(o,1); jj = j + offs(o,2); kk = k + offs(o,3);
      if ii < 1 || jj < 1 || kk < 1 || ii > sz(1) || jj > sz(2) || kk > sz(3), continue; end
      nb = sub2ind(sz, ii, jj, kk);
      if bw(nb) && ~L(nb)
        L(nb) = num; stack(end+1) = nb; %#ok<AGROW>
      end
    end
  end
end
L = reshape(L, size(bw));
