function tf = contains(str, pat, varargin)
% Octave shim for MATLAB contains()
if iscell(str), tf = cellfun(@(s) contains(s,pat), str); return; end
if iscell(pat), tf = any(cellfun(@(p) ~isempty(strfind(str,p)), pat)); return; end
tf = ~isempty(strfind(str, pat));
end
