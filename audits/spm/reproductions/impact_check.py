import numpy as np
from scipy import stats, special
from numpy import log, pi, sqrt, exp
from ec_check import spm_ECdensity

gammaln = special.gammaln
gamma = special.gamma

def spm_ECdensity_Xfixed(t, v):
    """chi2 densities with corrected powers of t (validated against F-limit)"""
    t = np.atleast_1d(np.asarray(t, float))
    EC = np.zeros((4, t.size))
    a = (4*log(2))/(2*pi)
    def b(power):
        return t**(0.5*power)*exp(-t/2-gammaln(v/2))/2**((v-2)/2)
    EC[0] = 1 - stats.chi2.cdf(t, v)
    EC[1] = a**0.5*b(v-1)
    EC[2] = a*b(v-2)*(t-(v-1))
    EC[3] = a**1.5*b(v-3)*(t**2-(2*v-1)*t+(v-1)*(v-2))
    return EC

def spm_P_RF(c, k, Z, df, STAT, R, n=1, fixedX=False):
    """Transcription of spm_P_RF.m"""
    R = np.asarray(R, float)
    D = np.max(np.nonzero(R)[0]) + 1   # find(R,1,'last')
    R = R[:D]
    G = sqrt(pi)/gamma(np.arange(1, D+1)/2)
    if STAT == 'X' and fixedX:
        EC = spm_ECdensity_Xfixed(Z, df[1])[:, 0]
    else:
        EC = spm_ECdensity(STAT, Z, df)[:, 0]
    EC = np.maximum(EC[:D], np.finfo(float).eps)
    from scipy.linalg import toeplitz
    P = np.triu(toeplitz(EC*G))
    P = np.linalg.matrix_power(P, n)
    P = P[0, :]
    EM = (R/G)*P
    Ec = EM.sum()
    EN = P[0]*R[D-1]
    Ek = EN/EM[D-1]
    D2 = D - 1
    if (not k) or (not D2):
        p = 1.0
    else:
        beta = (gamma(D2/2+1)/Ek)**(2/D2)
        p = exp(-beta*(k**(2/D2)))
    Pval = 1 - stats.poisson.cdf(c-1, (Ec+np.finfo(float).eps)*p)
    return Pval, p, Ec, Ek

# Typical whole-brain search: R for ~1200 cm^3, FWHM ~ 3 voxels
R = [1, 33.4, 354.7, 705.7]

print("=== Impact of chi2 EC-density bug on FWE-corrected peak p (chi2_10 field) ===")
v = 10.0
for t in [25.0, 30.0, 35.0, 40.0]:
    Pb, _, Ecb, _ = spm_P_RF(1, 0, t, [1, v], 'X', R)
    Pf, _, Ecf, _ = spm_P_RF(1, 0, t, [1, v], 'X', R, fixedX=True)
    print(f"t={t}: buggy P_FWE={Pb:.5f}  correct P_FWE={Pf:.5f}  ratio Ec={Ecb/Ecf:.2f}")

print("\n=== Impact on cluster-extent p (chi2_10, u=20, cluster k in resels) ===")
u = 20.0
for k in [0.5, 1.0, 2.0]:
    Pb, pb, _, Ekb = spm_P_RF(1, k, u, [1, v], 'X', R)
    Pf, pf, _, Ekf = spm_P_RF(1, k, u, [1, v], 'X', R, fixedX=True)
    print(f"k={k}: buggy p_unc={pb:.5f} (Ek={Ekb:.3f})  correct p_unc={pf:.5f} (Ek={Ekf:.3f})")

print("\n=== Check T-field FWE against published/known values (sanity of spm_P_RF impl) ===")
# For Z field, expected EC = sum R_d rho_d; compare P with 1-exp(-Ec)
for t in [4.5, 5.0]:
    P, _, Ec, _ = spm_P_RF(1, 0, t, [1, 30], 'T', R)
    print(f"T30, t={t}: P_FWE={P:.5f}, Ec={Ec:.5f}, 1-exp(-Ec)={1-exp(-Ec):.5f}")

print("\n=== BH-FDR check of spm_P_FDR (single-arg branch) ===")
rng = np.random.default_rng(0)
p = np.concatenate([rng.uniform(size=50), rng.uniform(size=10)*1e-3])
S = p.size
si = np.argsort(p)
ps = p[si]
q = ps*S/np.arange(1, S+1)
# spm: sentinel 1, running min from end
qadj = np.minimum.accumulate(np.concatenate([q, [1.0]])[::-1])[::-1][:-1]
spm_adj = np.empty(S); spm_adj[si] = qadj
try:
    import statsmodels.stats.multitest as mt
    ref = mt.multipletests(p, method='fdr_bh')[1]
    print("max |spm - statsmodels| =", np.max(np.abs(spm_adj - ref)))
except ImportError:
    # manual BH adjusted
    ref = np.empty(S)
    ref[si] = np.minimum(np.minimum.accumulate(q[::-1])[::-1], 1)
    print("max |spm - manual BH| =", np.max(np.abs(spm_adj - ref)))
