function varargout = license(varargin)
% Octave shim: report every toolbox as licensed (octave-signal provides the functions SPM needs here)
if nargin>=1 && strcmpi(varargin{1},'test'), varargout{1} = true; else varargout{1} = 'octave'; end
end
