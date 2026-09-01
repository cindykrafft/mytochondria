function r = corr(x, y, varargin)
% Octave shim for MATLAB corr(x, y, 'type', 'Pearson'): column-wise Pearson r
if nargin < 2 || isempty(y), y = x; end
n = size(x,1);
xz = (x - mean(x,1)) ./ std(x,0,1);
yz = (y - mean(y,1)) ./ std(y,0,1);
r = (xz' * yz) / (n-1);
