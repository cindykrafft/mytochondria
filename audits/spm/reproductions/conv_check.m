addpath('/home/user/spmfork');
t = 25; v = 3;   % worst observed case
ECX = spm_ECdensity('X',t,[1 v]);
for V = [1e5 1e6 1e7 1e8]
    ECF = spm_ECdensity('F',t/v,[v V]);
    fprintf('V=%.0e: |ratio-1| EC2..4 = %.3e %.3e %.3e\n', V, ...
        abs(ECX(2)/ECF(2)-1), abs(ECX(3)/ECF(3)-1), abs(ECX(4)/ECF(4)-1));
end
