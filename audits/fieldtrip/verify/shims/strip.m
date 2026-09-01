function s = strip(s, varargin)
% Octave stand-in for MATLAB strip (whitespace only)
if iscell(s), s = cellfun(@strtrim, s, 'UniformOutput', false); else, s = strtrim(s); end
