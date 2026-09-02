function tf = startsWith(str, pat, varargin)
% Octave shim: MATLAB-compatible startsWith for char/cell x char/cell
if ischar(pat), pat = {pat}; end
if ischar(str)
  tf = false; for i=1:numel(pat), tf = tf || strncmp(str, pat{i}, numel(pat{i})); end
else
  tf = false(size(str));
  for j=1:numel(str), for i=1:numel(pat), if strncmp(str{j}, pat{i}, numel(pat{i})), tf(j)=true; end; end; end
end
end
