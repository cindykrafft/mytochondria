import numpy as np
from scipy import stats, special
from numpy import log, pi, sqrt, exp

gammaln = special.gammaln

def spm_ECdensity(STAT, t, df):
    """Direct transcription of spm_ECdensity.m"""
    t = np.atleast_1d(np.asarray(t, float))
    EC = np.zeros((4, t.size))
    if STAT == 'Z':
        a = 4*log(2)
        b = exp(-t**2/2)
        EC[0] = 1 - stats.norm.cdf(t)
        EC[1] = a**0.5/(2*pi)*b
        EC[2] = a/((2*pi)**1.5)*b*t
        EC[3] = a**1.5/((2*pi)**2)*b*(t**2 - 1)
    elif STAT == 'T':
        v = df[1]
        a = 4*log(2)
        b = exp(gammaln((v+1)/2) - gammaln(v/2))
        c = (1+t**2/v)**((1-v)/2)
        EC[0] = stats.t.cdf(-t, v)
        EC[1] = a**0.5/(2*pi)*c
        EC[2] = a/((2*pi)**1.5)*c*t/((v/2)**0.5)*b
        EC[3] = a**1.5/((2*pi)**2)*c*((v-1)*(t**2)/v - 1)
    elif STAT == 'X':
        v = df[1]
        a = (4*log(2))/(2*pi)
        b = t**(0.5*(v-1))*exp(-t/2-gammaln(v/2))/2**((v-2)/2)
        EC[0] = 1 - stats.chi2.cdf(t, v)
        EC[1] = a**0.5*b
        EC[2] = a*b*(t-(v-1))
        EC[3] = a**1.5*b*(t**2-(2*v-1)*t+(v-1)*(v-2))
    elif STAT == 'F':
        k, v = df
        a = (4*log(2))/(2*pi)
        b = gammaln(v/2) + gammaln(k/2)
        EC[0] = 1 - stats.f.cdf(t, k, v)
        EC[1] = (a**0.5*exp(gammaln((v+k-1)/2)-b)*2**0.5
                 *(k*t/v)**(0.5*(k-1))*(1+k*t/v)**(-0.5*(v+k-2)))
        EC[2] = (a*exp(gammaln((v+k-2)/2)-b)*(k*t/v)**(0.5*(k-2))
                 *(1+k*t/v)**(-0.5*(v+k-2))*((v-1)*k*t/v-(k-1)))
        EC[3] = (a**1.5*exp(gammaln((v+k-3)/2)-b)
                 *2**(-0.5)*(k*t/v)**(0.5*(k-3))*(1+k*t/v)**(-0.5*(v+k-2))
                 *((v-1)*(v-2)*(k*t/v)**2-(2*v*k-v-k-1)*(k*t/v)+(k-1)*(k-2)))
    return EC

u = np.array([2.0, 3.0, 4.0])

print("=== TEST 1: T(v->inf) vs Z (sanity of transcription & T densities) ===")
Zd = spm_ECdensity('Z', u, None)
Td = spm_ECdensity('T', u, [1, 1e7])
print("max rel err:", np.max(np.abs(Td-Zd)/np.abs(Zd)))

print("\n=== TEST 2: F(1,v) vs two-sided T(v):  rho_d^F(1,v)(t^2) ?= 2*rho_d^T(t), d>=1 ===")
v = 12.0
Fd = spm_ECdensity('F', u**2, [1.0, v])
Td = spm_ECdensity('T', u, [1.0, v])
for d in range(4):
    if d == 0:
        # P(F>t^2) = P(|T|>t) = 2*P(T>t)
        print(f"d={d}: F={Fd[d]}, 2T={2*Td[d]}, ratio={Fd[d]/(2*Td[d])}")
    else:
        print(f"d={d}: ratio F/(2T) = {Fd[d]/(2*Td[d])}")

print("\n=== TEST 3: X(v=1) vs two-sided Z:  rho_d^X1(u^2) ?= 2*rho_d^Z(u), d>=1 ===")
Xd = spm_ECdensity('X', u**2, [1.0, 1.0])
Zd = spm_ECdensity('Z', u, None)
for d in range(1, 4):
    print(f"d={d}: ratio X/(2Z) = {Xd[d]/(2*Zd[d])}   (u = {u})")

print("\n=== TEST 4: X(v=k) vs limit of F(k,m->inf): rho_d^X(x) ?= rho_d^F(x/k) ===")
for k in [4.0, 8.0]:
    x = np.array([8.0, 15.0, 25.0])
    m = 1e8
    Fd = spm_ECdensity('F', x/k, [k, m])
    Xd = spm_ECdensity('X', x, [1.0, k])
    for d in range(1, 4):
        print(f"k={k}, d={d}: ratio X/F = {Xd[d]/Fd[d]}  (x={x})")
    print(f"   note sqrt(x) = {np.sqrt(x)}, x = {x}")
