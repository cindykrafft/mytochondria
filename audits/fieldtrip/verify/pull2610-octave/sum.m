function y = sum(x, varargin)
% Octave 8.4 shim: accept MATLAB's sum(x, dim, 'omitnan') by zeroing the NaNs first.
omit = false; args = {};
for k = 1:numel(varargin)
  a = varargin{k};
  if ischar(a) && strcmpi(a, 'omitnan'), omit = true;
  elseif ischar(a) && strcmpi(a, 'includenan'), % default
  else args{end+1} = a; end
end
if omit, x(isnan(x)) = 0; end
y = builtin('sum', x, args{:});
