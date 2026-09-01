import numpy as np
from scipy.special import gammaln
from scipy.stats import chi2, f as fdist

a = (4*np.log(2))/(2*np.pi)

def ec_X_fixed(t, v):
    t=np.atleast_1d(t).astype(float)
    b = np.exp(-t/2 - gammaln(v/2))/2**((v-2)/2)
    EC=np.zeros((4,t.size))
    EC[0]=chi2.sf(t,v)
    EC[1]=a**0.5*b*t**(0.5*(v-1))
    EC[2]=a     *b*t**(0.5*(v-2))*(t-(v-1))
    EC[3]=a**1.5*b*t**(0.5*(v-3))*(t**2-(2*v-1)*t+(v-1)*(v-2))
    return EC

def ec_X_buggy(t, v):
    t=np.atleast_1d(t).astype(float)
    b = t**(0.5*(v-1))*np.exp(-t/2 - gammaln(v/2))/2**((v-2)/2)
    EC=np.zeros((4,t.size))
    EC[0]=chi2.sf(t,v)
    EC[1]=a**0.5*b
    EC[2]=a     *b*(t-(v-1))
    EC[3]=a**1.5*b*(t**2-(2*v-1)*t+(v-1)*(v-2))
    return EC

# Reference: F-field EC densities (SPM's F branch, verified-correct) at k=v_chi, v->inf
# chi2_v = v * F(v, inf). SPM F branch evaluated with df=[k, big] and t_F = t_chi/k.
def ec_F(t, k, v):
    t=np.atleast_1d(t).astype(float)
    aa=(4*np.log(2))/(2*np.pi)
    bb=gammaln(v/2)+gammaln(k/2)
    EC=np.zeros((4,t.size))
    EC[0]=fdist.sf(t,k,v)
    EC[1]=aa**0.5*np.exp(gammaln((v+k-1)/2)-bb)*2**0.5*(k*t/v)**(0.5*(k-1))*(1+k*t/v)**(-0.5*(v+k-2))
    EC[2]=aa*np.exp(gammaln((v+k-2)/2)-bb)*(k*t/v)**(0.5*(k-2))*(1+k*t/v)**(-0.5*(v+k-2))*((v-1)*k*t/v-(k-1))
    EC[3]=aa**1.5*np.exp(gammaln((v+k-3)/2)-bb)*2**-0.5*(k*t/v)**(0.5*(k-3))*(1+k*t/v)**(-0.5*(v+k-2))*((v-1)*(v-2)*(k*t/v)**2-(2*v*k-v-k-1)*(k*t/v)+(k-1)*(k-2))
    return EC

for v in [3, 6, 10]:
    tt=np.array([8.0,15.0,25.0])
    fixed=ec_X_fixed(tt,v)
    buggy=ec_X_buggy(tt,v)
    # F-limit reference: k=v, big v2, evaluate at t_F=t_chi/v
    ref=ec_F(tt/v, v, 200000.0)
    print(f"--- chi2 df={v}, t={tt}")
    for d in range(1,4):  # EC orders 2,3,4 (rows 1,2,3)
        print(f" EC{d+1}: fixed/ref ={fixed[d]/ref[d]}  buggy/ref={buggy[d]/ref[d]}")
