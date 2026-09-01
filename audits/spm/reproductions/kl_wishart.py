import numpy as np
from scipy.stats import wishart
from scipy.special import multigammaln, psi

rng = np.random.default_rng(0)
d = 3
q, p = 7.0, 5.0
A = rng.standard_normal((d,d)); Q = A@A.T + d*np.eye(d)   # inverse-scale of Q-density
B = rng.standard_normal((d,d)); P = B@B.T + d*np.eye(d)

# SPM parameterization: density with dof q, inverse scale Q -> scipy scale = inv(Q)
Wq = wishart(df=q, scale=np.linalg.inv(Q))
Wp = wishart(df=p, scale=np.linalg.inv(P))

# Monte Carlo KL
N = 400000
X = Wq.rvs(N, random_state=rng)
kl_mc = np.mean(Wq.logpdf(X.transpose(1,2,0)) - Wp.logpdf(X.transpose(1,2,0)))

def spm_kl(q,Q,p,P):
    d = Q.shape[0]
    logdetQ = np.log(np.linalg.det(Q)); logdetP = np.log(np.linalg.det(P))
    LqQ = sum(psi((q+1-i)/2) for i in range(1,d+1)) + d*np.log(2) - logdetQ
    LpP = sum(psi((p+1-i)/2) for i in range(1,d+1)) + d*np.log(2) - logdetP
    logZqQ = 0.5*q*d*np.log(2) - 0.5*q*logdetQ + multigammaln(q/2,d)
    logZpP = 0.5*p*d*np.log(2) - 0.5*p*logdetP + multigammaln(p/2,d)
    kl_code = 0.5*(q-d-1)*LqQ - 0.5*(p-d-1)*LpP - 0.5*q*d + 0.5*q*np.trace(P@np.linalg.inv(Q)) + logZpP - logZqQ
    kl_fix  = 0.5*(q-d-1)*LqQ - 0.5*(p-d-1)*LqQ - 0.5*q*d + 0.5*q*np.trace(P@np.linalg.inv(Q)) + logZpP - logZqQ
    return kl_code, kl_fix

code, fix = spm_kl(q,Q,p,P)
print("MC KL      :", kl_mc)
print("SPM code   :", code)
print("corrected  :", fix)
