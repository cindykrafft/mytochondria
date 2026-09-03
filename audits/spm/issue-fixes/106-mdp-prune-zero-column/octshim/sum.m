function S = sum(varargin)
% Octave shim: support MATLAB's sum(X,'all') (Octave 8.4 lacks it).
if nargin >= 2 && ischar(varargin{2}) && strcmpi(varargin{2},'all')
    S = builtin('sum',varargin{1}(:),varargin{3:end});
else
    S = builtin('sum',varargin{:});
end
