function tf = endsWith(str, pat, varargin)
if ischar(pat), pat = {pat}; end
f = @(s) any(cellfun(@(p) numel(s)>=numel(p) && strcmp(s(end-numel(p)+1:end), p), pat));
if ischar(str), tf = f(str); else tf = cellfun(f, str); end
end
