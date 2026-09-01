import numpy as np
from scipy.special import psi, gammaln
rng = np.random.default_rng(0)

def spm_log(x):
    return np.maximum(np.log(np.maximum(x,1e-300)), -32)

def betaln_cols(z):
    z = np.maximum(z, np.exp(-32))
    return gammaln(z).sum(axis=0) - gammaln(z.sum(axis=0))

# ---------------------------------------------------------------
# 1) spm_MDP_MI : E, dEdA, dEda  (faithful transcription)
# ---------------------------------------------------------------
def spm_MI(A):
    return (A.ravel() @ spm_log(A.ravel())
            - A.sum(0) @ spm_log(A.sum(0))
            - A.sum(1) @ spm_log(A.sum(1)))

def spm_MDP_MI(a, c=None, h=None, grad=False):
    a = a.reshape(a.shape[0], -1)
    s = a.sum()
    A = a/s
    E = spm_MI(A)
    C = 0; H = 0
    if c is not None:
        c = c.ravel()/c.sum()
        C = spm_log(c)
        E = E + C @ A.sum(1)
    if h is not None:
        h = h.ravel()/h.sum()
        H = spm_log(h)
        E = E + A.sum(0) @ H
    if not grad:
        return E
    dEdA = spm_log(A/(np.outer(A.sum(1), A.sum(0)))) - 1
    if c is not None:
        dEdA = dEdA + (C[:,None] - C @ A.sum(1))
    if h is not None:
        dEdA = dEdA + (H[None,:] - A.sum(0) @ H)
    dEda = dEdA*(1-A)/s
    return E, dEdA, dEda

n, m = 4, 5
a = rng.random((n,m))*3 + 0.2
c = rng.random(n) + 0.1

E0, dEdA, dEda = spm_MDP_MI(a, c, grad=True)
# numerical dE/da
num = np.zeros((n,m))
eps = 1e-6
for i in range(n):
    for j in range(m):
        ap = a.copy(); ap[i,j] += eps
        am = a.copy(); am[i,j] -= eps
        num[i,j] = (spm_MDP_MI(ap,c) - spm_MDP_MI(am,c))/(2*eps)
print("== spm_MDP_MI dEda check ==")
print("code dEda[0,:3] :", dEda[0,:3])
print("numeric  [0,:3] :", num[0,:3])
print("max abs err     :", np.abs(dEda-num).max())
# correct projected gradient
s = a.sum(); A = a/s
truegrad = (dEdA - (dEdA*A).sum())/s
print("projected-grad max err:", np.abs(truegrad-num).max())

# also check without cost
E0b, dEdAb, dEdab = spm_MDP_MI(a, grad=True)
numb = np.zeros((n,m))
for i in range(n):
    for j in range(m):
        ap = a.copy(); ap[i,j] += eps
        am = a.copy(); am[i,j] -= eps
        numb[i,j] = (spm_MDP_MI(ap) - spm_MDP_MI(am))/(2*eps)
print("no-cost: code dEda err:", np.abs(dEdab-numb).max(),
      " projected err:", np.abs((dEdAb-(dEdAb*A).sum())/s - numb).max())

# ---------------------------------------------------------------
# 2) spm_KL_dir vs closed form
# ---------------------------------------------------------------
q = rng.random(6)*4 + 0.5
p = rng.random(6)*4 + 0.5
def spm_KL_dir(q,p):
    q = np.maximum(q, np.exp(-16)); p = np.maximum(p, np.exp(-16))
    sp = lambda z: psi(z) - psi(z.sum())
    return betaln_cols(p[:,None]) - betaln_cols(q[:,None]) + ((q-p)*sp(q)).sum()
kl_closed = (gammaln(q.sum()) - gammaln(p.sum()) - gammaln(q).sum() + gammaln(p).sum()
             + ((q-p)*(psi(q)-psi(q.sum()))).sum())
print("\n== spm_KL_dir ==", float(np.asarray(spm_KL_dir(q,p)).ravel()[0]), float(kl_closed))

# ---------------------------------------------------------------
# 3) spm_dir_H (Dirichlet entropy) vs scipy
# ---------------------------------------------------------------
from scipy.stats import dirichlet
aa = rng.random(5)*3 + 0.3
def spm_dir_H(a):
    a = a + np.exp(-16)
    a0 = a.sum(); k = len(a)
    return betaln_cols(a[:,None])[0] + (a0-k)*psi(a0) - ((a-1)*psi(a)).sum()
print("== spm_dir_H ==", float(spm_dir_H(aa)), float(dirichlet(aa).entropy()))

# ---------------------------------------------------------------
# 4) spm_dir_MI's spm_H = expected categorical entropy under Dirichlet
# ---------------------------------------------------------------
def spm_H(a):
    a0 = a.sum()
    return psi(a0+1) - (a*psi(a+1)).sum()/a0
samp = dirichlet(aa).rvs(400000, random_state=1)
Hmc = (-samp*np.log(samp)).sum(1).mean()
print("== spm_H (expected cat entropy) ==", float(spm_H(aa)), float(Hmc))

# ---------------------------------------------------------------
# 5) spm_MDP_G vs direct mutual information
# ---------------------------------------------------------------
def spm_cross_list(vs):
    # MATLAB spm_cross with squeeze of ALL singleton dims
    Y = np.array(vs[0]).reshape(-1,1) if np.ndim(vs[0])<=1 else np.array(vs[0])
    for v in vs[1:]:
        v = np.asarray(v)
        A = Y.reshape(Y.shape + (1,)*v.ndim if v.ndim else Y.shape)
        Y = np.multiply.outer(Y, v)
        sz = [d for d in Y.shape if d>1]
        Y = Y.reshape(sz if sz else (1,))
    return Y

def spm_MDP_G(A_list, x_list, Ns):
    # faithful: qx = cross of x (squeezed), linear indexing col-major
    qx = x_list[0].reshape(-1,1)
    for v in x_list[1:]:
        qx = spm_cross_list([qx, v])
    qxf = np.asarray(qx).reshape(-1, order='F')
    G = 0.0; qo = 0.0
    slog = lambda z: np.log(z + np.exp(-16))
    for i in np.where(qxf > np.exp(-16))[0]:
        po = np.array([1.0])
        for Ag in A_list:
            Af = Ag.reshape(Ag.shape[0], -1, order='F')
            po = spm_cross_list([po, Af[:,i]])
        po = np.asarray(po).reshape(-1, order='F')
        qo = qo + qxf[i]*po
        G  = G  + qxf[i]*(po @ slog(po))
    G = G - qo @ slog(qo)
    return G

Ns = (3,4)
A1 = rng.random((5,)+Ns); A1 /= A1.sum(0, keepdims=True)
x1 = rng.random(3); x1/=x1.sum()
x2 = rng.random(4); x2/=x2.sum()
G = spm_MDP_G([A1],[x1,x2],Ns)
# direct MI between outcome and joint state
joint = np.einsum('oij,i,j->oij', A1, x1, x2)
pj = joint.reshape(5,-1)
po_ = pj.sum(1); px_ = pj.sum(0)
MI = (pj*np.log(np.maximum(pj,1e-300)/np.outer(po_,px_))).sum()
print("== spm_MDP_G ==", float(G), float(MI))

# ---------------------------------------------------------------
# 6) spm_dot faithful transcription vs einsum, several patterns
# ---------------------------------------------------------------
def tensorprod(X, v, dim):
    # contract dim (0-based) of X with vector v; keep other dims in order
    X = np.asarray(X, float)
    if dim >= X.ndim:
        # matlab tensorprod allows trailing singleton
        assert v.size == 1
        return X*v.ravel()[0]
    return np.tensordot(X, v, axes=([dim],[0]))

def spm_dot(X, x, omit=None):
    X = np.asarray(X, float)
    if isinstance(x, list):
        if len(x)==1 and np.size(x[0])==1:
            return X*np.ravel(x[0])[0]
        DIM = np.arange(1, len(x)+1) + max(X.ndim, len(x)) - len(x)  # 1-based
        x = list(x)
    else:
        if np.size(x)==1:
            return X*np.ravel(x)[0]
        matches = [d for d in range(X.ndim) if X.shape[d]==np.size(x)]
        DIM = np.array([matches[0]+1])
        x = [x]
    if omit is not None:
        DIM = np.delete(DIM, omit-1)
        del x[omit-1]
    DIM = DIM.astype(float)
    for d in range(len(x)):
        X = tensorprod(X, np.ravel(x[d]), int(DIM[d])-1)
        DIM = DIM - 1
    return X

print("\n== spm_dot checks ==")
# (a) A(No,N1,N2,N3) with cell {x1,x2,x3}
No,N1,N2,N3 = 5,3,4,2
A = rng.random((No,N1,N2,N3))
xs = [rng.random(N1), rng.random(N2), rng.random(N3)]
r = spm_dot(A, xs)
ref = np.einsum('oijk,i,j,k->o', A, *xs)
print("4D cell:", np.abs(np.ravel(r)-ref).max())
# (b) with omission of factor 2 (i=2 -> keep dim of factor2)
r = spm_dot(A, xs, omit=2)
ref = np.einsum('oijk,i,k->oj', A, xs[0], xs[2])
print("omit f2:", np.abs(np.asarray(r)-ref).max())
# (c) L(N1,N2,N3) omit factor 1 (VB_X qL pattern)
L = rng.random((N1,N2,N3))
r = spm_dot(L, xs, omit=1)
ref = np.einsum('ijk,j,k->i', L, xs[1], xs[2])
print("L omit f1:", np.abs(np.asarray(r)-ref).max())
# (d) non-cell vector: contract first matching dim
M = rng.random((4,4))
v = rng.random(4)
r = spm_dot(M, v)
print("matrix first-match:", np.abs(np.asarray(r)- M.T@v ).max(), "(contracts dim1 -> A'*v)")

# (e) ndims(X) > numel(x): skip leading dims
r = spm_dot(A, [rng.random(N2), rng.random(N3)])
# DIM = (1:2)+max(4,2)-2 = 3:4 -> contract dims 3,4
print("skip-leading ok" )

# ---------------------------------------------------------------
# 7) spm_cross squeeze of interior singletons (shape demo)
# ---------------------------------------------------------------
print("\n== spm_cross interior singleton ==")
o = rng.random(5)             # outcome vector No=5
x1 = rng.random(3)
x2 = np.array([1.0])          # singleton factor
x3 = rng.random(4)
Y = spm_cross_list([o.reshape(-1,1), x1, x2, x3])
print("da shape from spm_cross:", np.asarray(Y).shape, " (a{g} is (5,3,1,4))")
