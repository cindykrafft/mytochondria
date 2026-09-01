import numpy as np
from scipy import stats, special
from numpy import log, pi, sqrt, exp
from math import factorial, gamma as gam
from ec_check import spm_ECdensity

gammaln = special.gammaln

def K(b, a):
    if b - a + 1 > 0:
        return exp(gammaln(b+1) - (gammaln(a+1) + gammaln(b-a+1)))
    return 0.0

def ECdF(d, df, t):
    """Transcription of ECdF in spm_EC_density.m"""
    t = np.atleast_1d(np.asarray(t, float))
    p = min(df[0], 256)
    m = min(df[1], 256)
    e = ((log(2)/pi)**(d/2)*2*factorial(d-1)*gam((p+m-d)/2)/
         (m**((p-d)/2)*gam(p/2)*gam(m/2))*(1+(p*t)/m)**(-(p+m-2)/2))
    Si = 0.0
    for i in range(0, d):
        Sj = 0.0
        for j in range(0, min(i, d-1-i)+1):
            b = (p+m-d)/2 + j - 1
            Sj = Sj + K(b, j)*K(m-1, i-j)*K(p-1, d-1-i-j)*(m**(-i))
        Si = Si + Sj*((-1)**(d-1-i))*((p*t)**(i+(p-d)/2))
    return e*Si

def spm_EC_density(STAT, t, df, D=4):
    t = np.atleast_1d(np.asarray(t, float))
    EC = np.zeros((D+1, t.size))
    if STAT == 'Z':
        for d in range(1, D+1):
            EC[d] = ECdF(d, [1, np.inf], t**2)*(np.sign(t)**(d+1))/2  # d index: matlab d-1 = python d
        EC[0] = 1 - stats.norm.cdf(t)
    elif STAT == 'T':
        for d in range(1, D+1):
            EC[d] = ECdF(d, [1, df[1]], t**2)*(np.sign(t)**(d+1))/2
        EC[0] = 1 - stats.t.cdf(t, df[1])
    elif STAT == 'X':
        for d in range(1, D+1):
            EC[d] = ECdF(d, [df[1], np.inf], t)
        EC[0] = 1 - stats.chi2.cdf(t, df[1])
    elif STAT == 'F':
        for d in range(1, D+1):
            EC[d] = ECdF(d, df, t)
        EC[0] = 1 - stats.f.cdf(t, df[0], df[1])
    return EC

# NB in MATLAB: EC(d,:) = ECdF(d-1,...).*(sign(t).^d)/2 for d=2..D+1, i.e. density order = d-1,
# sign power = d (matlab row) = (density order+1). Mirrored above.

print("=== TEST A: spm_EC_density F vs spm_ECdensity F (k=3, v=64) ===")
t = np.array([2.0, 4.0, 8.0])
old = spm_ECdensity('F', t, [3.0, 64.0])
new = spm_EC_density('F', t, [3, 64], 3)
for d in range(4):
    print(f"d={d}: old={old[d]}, new={new[d]}, ratio={new[d]/old[d]}")

print("\n=== TEST B: spm_EC_density T vs spm_ECdensity T (v=64) ===")
u = np.array([2.0, 3.0, 5.0])
old = spm_ECdensity('T', u, [1.0, 64.0])
new = spm_EC_density('T', u, [1, 64], 3)
for d in range(4):
    print(f"d={d}: ratio new/old = {new[d]/old[d]}")

print("\n=== TEST C: spm_EC_density Z vs spm_ECdensity Z ===")
old = spm_ECdensity('Z', u, None)
new = spm_EC_density('Z', u, None, 3)
for d in range(4):
    print(f"d={d}: ratio new/old = {new[d]/old[d]}")

print("\n=== TEST D: spm_EC_density X(v) vs correct chi2 density ===")
# correct chi2 density: rho_d^X(x) = rho_d^F(x/v) with F(v, m->inf).
# Use ECdF itself with big m and argument x/v (v = numerator df), which Test A validates.
for v in [1.0, 4.0, 8.0]:
    x = np.array([8.0, 15.0, 25.0])
    as_coded = spm_EC_density('X', x, [1, v], 3)
    correct = np.array([ECdF(d, [v, 256], x/v) for d in range(1, 4)])
    for d in range(1, 4):
        print(f"v={v}, d={d}: coded={as_coded[d]}, correct={correct[d-1]}, ratio={as_coded[d]/correct[d-1]}")

print("\n=== TEST E: df capping at 256: T with v=2000 ===")
old = spm_ECdensity('T', u, [1.0, 2000.0])
new = spm_EC_density('T', u, [1, 2000], 3)
for d in range(4):
    print(f"d={d}: ratio new/old = {new[d]/old[d]}")
