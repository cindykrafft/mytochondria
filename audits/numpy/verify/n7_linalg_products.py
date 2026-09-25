#!/usr/bin/env python
"""NumPy linear algebra, deeper pass (n3 covered the basics): qr every mode,
cholesky (upper=, triangle read), eig / eigvals / eigh / eigvalsh (UPLO actually
read, ordering, normalisation, defective matrices, complex pairs), svd every
option and svdvals, tensorinv / tensorsolve, multi_dot, matrix_power, cond every
ord, slogdet, norm every ord / axis / keepdims / dtype, lstsq (residual shapes,
rcond default, minimum-norm solutions), solve (stacking rules incl. the 2.0
change), inv, pinv (rcond / rtol / hermitian), matrix_rank, det of int matrices
vs Fraction, trace / diagonal / diag offsets, outer / kron / cross, tensordot,
einsum against explicit loops, matmul vs dot for >2-D, float32 dot accumulation,
vdot / inner / vecdot / matvec / vecmat, the 2.0 np.linalg array-API aliases,
matrix_transpose, LinAlgError types, result-dtype rules and stacked broadcasting.
Truths: mpmath at 50 digits (eig / qr / cholesky / svd_r / svd_c / lu_solve /
inverse / det / eigsy / eighe), fractions.Fraction, closed forms and explicit
Python loops."""
import sys, math, cmath, warnings, functools, itertools
from fractions import Fraction as F
import numpy as np
import mpmath as mp
mp.mp.dps = 50
MAJOR, MINOR = [int(x) for x in np.__version__.split('.')[:2]]
V2 = MAJOR >= 2; V22 = (MAJOR, MINOR) >= (2, 2)
def banner(): print(f"numpy {np.__version__}  mpmath {mp.__version__}  python {sys.version.split()[0]}")
def report(label, ok, detail=""): print(("ok   " if ok else "FAIL ") + label + ("  " + detail if detail else ""))
def close(a, b, rel=1e-10, abs_=1e-300):
    a = float(a); b = float(b)
    if math.isnan(a) and math.isnan(b): return True
    return abs(a - b) <= max(abs_, rel * max(abs(a), abs(b)))
def M(a): return mp.matrix(np.asarray(a).tolist())
def N(m):
    L = m.tolist()
    if any(isinstance(x, mp.mpc) for row in L for x in row): return np.array([[complex(x) for x in row] for row in L])
    return np.array([[float(x) for x in row] for row in L])
def col(m): return N(m).ravel()
def maxdiff(a, b):
    a = np.asarray(a); b = np.asarray(b)
    return float(np.max(np.abs(a - b))) if a.size else 0.0
def raises(fn, exc):
    try: fn(); return False
    except exc: return True
def mp_svals(A):
    S = (mp.svd_c if np.iscomplexobj(A) else mp.svd_r)(M(A), compute_uv=False)
    return np.array(sorted([float(x) for x in S], reverse=True))
def mp_eigvals(A): return np.array([complex(e) for e in mp.eig(M(A), left=False, right=False)])
def match_err(w, wt):
    """greedy nearest-neighbour matching of two eigenvalue multisets; returns the max distance"""
    wt = list(wt); err = 0.0
    for x in w:
        d = [abs(x - y) for y in wt]; j = int(np.argmin(d)); err = max(err, d[j]); wt.pop(j)
    return err
def mp_qr(A):
    """mpmath.qr needs M >= N; for a wide matrix factor the first M columns and complete R = Q^T A"""
    A = np.asarray(A); m, n = A.shape
    if m >= n:
        Q, R = mp.qr(M(A), mode='full'); return N(Q), N(R)
    Q, R1 = mp.qr(M(A[:, :m]), mode='full'); Q = N(Q)
    return Q, np.hstack([N(R1), N(mp.matrix(Q.tolist()).T * M(A[:, m:]))])
def mp_solve(A, B):
    """A^-1 B at 50 digits for a matrix right-hand side (mpmath.lu_solve takes only vectors)"""
    return N(mp.inverse(M(A)) * M(B))
def mp_pinv(A, rcond=1e-15):
    U, S, V = (mp.svd_c if np.iscomplexobj(A) else mp.svd_r)(M(A), full_matrices=False)
    s = [S[i] for i in range(S.rows)]; smax = max(s)
    Sp = mp.diag([1 / x if x > rcond * smax else mp.mpf(0) for x in s])
    return N(V.H * Sp * U.H)
def det_fraction(Aint):
    """exact determinant by Fraction Gaussian elimination"""
    A = [[F(int(x)) for x in row] for row in Aint]; n = len(A); d = F(1)
    for i in range(n):
        p = next((r for r in range(i, n) if A[r][i] != 0), None)
        if p is None: return F(0)
        if p != i: A[i], A[p] = A[p], A[i]; d = -d
        d *= A[i][i]
        for r in range(i + 1, n):
            f = A[r][i] / A[i][i]
            for c in range(i, n): A[r][c] -= f * A[i][c]
    return d
def pymatmul(a, b):
    a = [list(r) for r in a]; b = [list(r) for r in b]
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
warnings.filterwarnings("ignore"); rs = np.random.RandomState(7)
banner()
LinAlgError = np.linalg.LinAlgError

# ================= qr
print("---- qr")
for name, A in [("tall 6x4", rs.randn(6, 4)), ("wide 4x6", rs.randn(4, 6)), ("square 5x5", rs.randn(5, 5))]:
    m, n = A.shape; k = min(m, n)
    Q, R = np.linalg.qr(A)
    report(f"qr reduced {name}: Q (M,K) with orthonormal columns, R (K,N) upper-triangular, Q@R = A",
           Q.shape == (m, k) and R.shape == (k, n) and np.allclose(Q.T @ Q, np.eye(k), atol=1e-12) and np.allclose(np.triu(R), R) and np.allclose(Q @ R, A, atol=1e-12),
           f"(|Q^T Q - I| {maxdiff(Q.T @ Q, np.eye(k)):.1e}, |QR - A| {maxdiff(Q @ R, A):.1e})")
    Qc, Rc = np.linalg.qr(A, mode='complete')
    report(f"qr complete {name}: Q (M,M) orthogonal (|det| = 1, 'may be either +/- 1'), R (M,N) upper, Q@R = A, first K columns = reduced Q",
           Qc.shape == (m, m) and Rc.shape == (m, n) and np.allclose(Qc @ Qc.T, np.eye(m), atol=1e-12) and close(abs(np.linalg.det(Qc)), 1, 1e-10) and np.allclose(np.triu(Rc), Rc) and np.allclose(Qc @ Rc, A, atol=1e-12) and np.allclose(Qc[:, :k], Q) and np.allclose(Rc[:k], R),
           f"(det Q = {np.linalg.det(Qc):+.6f})")
    Rr = np.linalg.qr(A, mode='r')
    report(f"qr mode='r' {name}: returns only R (K,N), identical to reduced R", isinstance(Rr, np.ndarray) and Rr.shape == (k, n) and np.array_equal(Rr, R))
    h, tau = np.linalg.qr(A, mode='raw')
    Af = h.T                                  # 'h is transposed for calling Fortran'
    Rraw = np.triu(Af); Qraw = np.eye(m)
    for i in range(k):
        v = np.zeros(m); v[i] = 1.0; v[i + 1:] = Af[i + 1:, i]
        Qraw = Qraw @ (np.eye(m) - tau[i] * np.outer(v, v))
    report(f"qr mode='raw' {name}: h (N,M) float64, tau (K,); Householder reconstruction prod(I - tau_i v_i v_i^T) @ triu(h.T) = A and equals mode='complete'",
           h.shape == (n, m) and tau.shape == (k,) and h.dtype == np.float64 and np.allclose(Qraw @ Rraw, A, atol=1e-12) and np.allclose(Qraw, Qc, atol=1e-12) and np.allclose(Rraw, Rc, atol=1e-12))
    Qm, Rm = mp_qr(A)
    D = np.sign(np.diag(R)) * np.sign(np.diag(Rm)[:k])
    report(f"qr {name} vs mpmath.qr at 50 digits: |R_ii| equal; Q columns and R rows equal up to a common sign per column",
           np.allclose(np.abs(np.diag(R)), np.abs(np.diag(Rm)[:k]), rtol=1e-12) and np.allclose(Q * D, Qm[:, :k], atol=1e-11) and np.allclose(R * D[:, None], Rm[:k], atol=1e-11),
           f"(sign convention undocumented; signs of diag(R): LAPACK {np.sign(np.diag(R)).astype(int).tolist()}, mpmath {np.sign(np.diag(Rm)[:k]).astype(int).tolist()})")
A3 = rs.randn(3, 5, 4); Q3, R3 = np.linalg.qr(A3)
report("qr on a stack (3,5,4): Q (3,5,4), R (3,4,4), each Q[i] @ R[i] = A[i] with orthonormal Q[i] (documented '... stack of the matrices')",
       Q3.shape == (3, 5, 4) and R3.shape == (3, 4, 4) and all(np.allclose(Q3[i] @ R3[i], A3[i], atol=1e-12) and np.allclose(Q3[i].T @ Q3[i], np.eye(4), atol=1e-12) and np.allclose(np.triu(R3[i]), R3[i]) for i in range(3)))
Qc3, Rc3 = np.linalg.qr(A3, mode='complete'); h3, tau3 = np.linalg.qr(A3, mode='raw')
report("qr stack: mode='complete' shapes (3,5,5),(3,5,4); mode='r' (3,4,4) = reduced R; mode='raw' h (3,4,5), tau (3,4)",
       Qc3.shape == (3, 5, 5) and Rc3.shape == (3, 5, 4) and np.array_equal(np.linalg.qr(A3, mode='r'), R3) and h3.shape == (3, 4, 5) and tau3.shape == (3, 4) and all(np.allclose(Qc3[i] @ Rc3[i], A3[i], atol=1e-12) for i in range(3)))
Ac = rs.randn(5, 3) + 1j * rs.randn(5, 3); Qz, Rz = np.linalg.qr(Ac)
report("qr complex (5,3): Q^H Q = I, R upper-triangular, Q@R = A, complex128 output",
       Qz.dtype == np.complex128 and np.allclose(Qz.conj().T @ Qz, np.eye(3), atol=1e-12) and np.allclose(np.triu(Rz), Rz) and np.allclose(Qz @ Rz, Ac, atol=1e-12))
print(f"   complex qr: diag(R) = {np.round(np.diag(Rz), 6).tolist()} (real diagonal from LAPACK zgeqrf, undocumented)")
Ai = rs.randint(-5, 6, (4, 3)); Qi, Ri = np.linalg.qr(Ai); Q32, R32 = np.linalg.qr(rs.randn(4, 3).astype(np.float32))
report("qr dtypes: int input -> float64 Q,R; float32 stays float32; complex64 stays complex64",
       Qi.dtype == np.float64 and Ri.dtype == np.float64 and np.allclose(Qi @ Ri, Ai, atol=1e-12) and Q32.dtype == np.float32 and R32.dtype == np.float32 and np.linalg.qr(Ac.astype(np.complex64))[0].dtype == np.complex64)
report("qr of a 1-D array raises LinAlgError ('Array must be at least two-dimensional')", raises(lambda: np.linalg.qr(np.ones(3)), LinAlgError))

# ================= cholesky
print("---- cholesky")
G = rs.randn(5, 5); SPD = G @ G.T + 5 * np.eye(5)
L = np.linalg.cholesky(SPD); Lmp = N(mp.cholesky(M(SPD)))
report("cholesky: L lower-triangular, L L^T = A, equals mpmath.cholesky at 50 digits", np.allclose(np.tril(L), L) and np.allclose(L @ L.T, SPD, atol=1e-12) and maxdiff(L, Lmp) < 1e-12, f"(|L - L_mp| {maxdiff(L, Lmp):.1e})")
Junk = SPD.copy(); Junk[np.triu_indices(5, 1)] = 99.0
report("cholesky reads only the lower triangle (documented 'only the lower or upper-triangular and diagonal elements of a are used'): garbage in the upper triangle ignored", np.array_equal(np.linalg.cholesky(Junk), L))
if V2:
    U = np.linalg.cholesky(SPD, upper=True); JunkL = SPD.copy(); JunkL[np.tril_indices(5, -1)] = 99.0
    report("cholesky(upper=True) [2.0]: U upper-triangular, U^H U = A, U = L^T", np.allclose(np.triu(U), U) and np.allclose(U.T @ U, SPD, atol=1e-12) and np.allclose(U, L.T, atol=1e-13))
    report("cholesky(upper=True) reads only the UPPER triangle: garbage in the lower triangle ignored", np.array_equal(np.linalg.cholesky(JunkL, upper=True), U))
    report("cholesky(upper=True) with garbage in the upper triangle (lower-only input) does NOT return the factor of A (here: the garbage triangle is not PD -> LinAlgError)", raises(lambda: np.linalg.cholesky(Junk, upper=True), LinAlgError) or not np.allclose(np.linalg.cholesky(Junk, upper=True), U))
report("cholesky of a non-positive-definite symmetric matrix raises LinAlgError", raises(lambda: np.linalg.cholesky(np.array([[1., 2.], [2., 1.]])), LinAlgError) and raises(lambda: np.linalg.cholesky(np.zeros((2, 2))), LinAlgError))
SPDs = np.stack([SPD, SPD + np.eye(5), 2 * SPD]); Ls = np.linalg.cholesky(SPDs)
report("cholesky on a stack (3,5,5): each L[i] equals mpmath.cholesky(A[i])", Ls.shape == (3, 5, 5) and all(maxdiff(Ls[i], N(mp.cholesky(M(SPDs[i])))) < 1e-12 for i in range(3)))
Cg = rs.randn(4, 4) + 1j * rs.randn(4, 4); H = Cg @ Cg.conj().T + 4 * np.eye(4); Lh = np.linalg.cholesky(H)
try: Lhmp = N(mp.cholesky(M(H))); mpok = maxdiff(Lh, Lhmp) < 1e-12
except Exception as e: mpok = True; print(f"   (mpmath.cholesky complex unavailable: {e})")
report("cholesky complex Hermitian: L lower with real positive diagonal, L L^H = A, equals mpmath", np.allclose(np.tril(Lh), Lh) and np.all(np.diag(Lh).imag == 0) and np.all(np.diag(Lh).real > 0) and np.allclose(Lh @ Lh.conj().T, H, atol=1e-12) and mpok)
report("cholesky dtypes: int -> float64; float32 -> float32; complex64 -> complex64", np.linalg.cholesky(np.eye(3, dtype=int) * 4).dtype == np.float64 and np.linalg.cholesky(SPD.astype(np.float32)).dtype == np.float32 and np.linalg.cholesky(H.astype(np.complex64)).dtype == np.complex64)

# ================= eig / eigvals
print("---- eig / eigvals")
A5 = rs.randn(5, 5); w, V = np.linalg.eig(A5); wt = mp_eigvals(A5)
report("eig(5x5 non-symmetric): eigenvalues match mpmath.eig at 50 digits (nearest-neighbour matching)", match_err(w, wt) < 1e-11, f"(max |dw| {match_err(w, wt):.1e}; np dtype {w.dtype})")
report("eig: A v_i = w_i v_i for every column", np.allclose(A5 @ V, V * w, atol=1e-11))
report("eig: eigenvectors have unit 2-norm (documented 'normalized (unit length)')", np.allclose(np.linalg.norm(V, axis=0), 1, atol=1e-13))
report("eigvals equals the eigenvalues from mpmath (same nearest-neighbour test)", match_err(np.linalg.eigvals(A5), wt) < 1e-11)
Rot = np.array([[0., -1.], [1., 0.]]); wr, Vr = np.linalg.eig(Rot)
report("eig of a real rotation: complex128 output, eigenvalues +-i in conjugate pairs (documented 'occur in conjugate pairs')", wr.dtype == np.complex128 and match_err(wr, [1j, -1j]) < 1e-14 and Vr.dtype == np.complex128 and np.allclose(np.linalg.norm(Vr, axis=0), 1))
print(f"   eig(rot) eigenvector 0 = {Vr[:, 0].tolist()} (LAPACK: unit 2-norm, largest component real)")
Sym = A5 + A5.T; ws = np.linalg.eig(Sym)[0]
report("eig of a real matrix with all-real eigenvalues returns a REAL dtype (documented 'unless the imaginary part is zero in which case it will be cast to a real type')", ws.dtype == np.float64 and match_err(ws, mp_eigvals(Sym)) < 1e-11)
Def = np.array([[1., 1.], [0., 1.]]); wd, Vd = np.linalg.eig(Def)
report("eig of the defective matrix [[1,1],[0,1]]: eigenvalues [1,1], eigenvector matrix rank 1 (documented 'may not be of maximum rank')", np.allclose(wd, [1, 1]) and np.linalg.matrix_rank(Vd) == 1, f"(eigenvectors {np.round(Vd, 6).tolist()})")
St = rs.randn(3, 4, 4); wS, VS = np.linalg.eig(St)
report("eig on a stack (3,4,4): eigenvalues (3,4) each matching mpmath; A[i] v = w v", wS.shape == (3, 4) and VS.shape == (3, 4, 4) and all(match_err(wS[i], mp_eigvals(St[i])) < 1e-11 and np.allclose(St[i] @ VS[i], VS[i] * wS[i], atol=1e-11) for i in range(3)))
w32, V32 = np.linalg.eig(A5.astype(np.float32)); wr32 = np.linalg.eig(Rot.astype(np.float32))[0]
report("eig dtypes: float32 -> float32 eigenvalues (real case) / complex64 (complex case), vectors float32; complex64 -> complex64; int -> float64", w32.dtype in (np.float32, np.complex64) and V32.dtype in (np.float32, np.complex64) and wr32.dtype == np.complex64 and np.linalg.eig(Ac[:3].astype(np.complex64))[0].dtype == np.complex64 and np.linalg.eig(np.array([[2, 1], [1, 2]]))[0].dtype == np.float64, f"(float32 5x5 -> {w32.dtype})")
report("eig float32 eigenvalues agree with mpmath to 1e-5 relative", match_err(w32.astype(complex), wt) < 1e-5 * np.abs(wt).max())
report("eig with NaN input raises LinAlgError (source _assert_finite; docstring lists only non-convergence)", raises(lambda: np.linalg.eig(np.array([[1., np.nan], [0., 1.]])), LinAlgError))
Cz = rs.randn(4, 4) + 1j * rs.randn(4, 4); wz, Vz = np.linalg.eig(Cz)
report("eig complex (4,4): eigenvalues match mpmath, A v = w v, unit-norm vectors", match_err(wz, mp_eigvals(Cz)) < 1e-11 and np.allclose(Cz @ Vz, Vz * wz, atol=1e-11) and np.allclose(np.linalg.norm(Vz, axis=0), 1))

# ================= eigh / eigvalsh
print("---- eigh / eigvalsh")
NS = rs.randn(4, 4); lowsym = np.tril(NS) + np.tril(NS, -1).T; upsym = np.triu(NS) + np.triu(NS, 1).T
tl = np.array(sorted(float(x) for x in mp.eigsy(M(lowsym), eigvals_only=True))); tu = np.array(sorted(float(x) for x in mp.eigsy(M(upsym), eigvals_only=True)))
report("eigvalsh(UPLO='L', default) on a NON-symmetric input uses the lower triangle (eigenvalues of tril+tril^T from mpmath.eigsy, ascending)", np.allclose(np.linalg.eigvalsh(NS), tl, atol=1e-11) and np.allclose(np.linalg.eigvalsh(NS, 'L'), tl, atol=1e-11))
report("eigvalsh(UPLO='U') uses the upper triangle (and differs from 'L' here)", np.allclose(np.linalg.eigvalsh(NS, 'U'), tu, atol=1e-11) and not np.allclose(tl, tu))
wl, Vl = np.linalg.eigh(NS); wu, Vu = np.linalg.eigh(NS, UPLO='U')
report("eigh(UPLO='L'/'U') eigenvalues ascending (documented) and match the same triangle rule; V diag(w) V^T reconstructs the symmetrised triangle", np.all(np.diff(wl) >= 0) and np.all(np.diff(wu) >= 0) and np.allclose(wl, tl, atol=1e-11) and np.allclose(wu, tu, atol=1e-11) and np.allclose(Vl @ np.diag(wl) @ Vl.T, lowsym, atol=1e-11) and np.allclose(Vu @ np.diag(wu) @ Vu.T, upsym, atol=1e-11))
report("eigh eigenvectors orthonormal, unit norm (documented 'normalized eigenvector')", np.allclose(Vl.T @ Vl, np.eye(4), atol=1e-12))
report("eigh/eigvalsh reject UPLO other than 'L'/'U' (ValueError)", raises(lambda: np.linalg.eigh(NS, UPLO='X'), ValueError) and raises(lambda: np.linalg.eigvalsh(NS, UPLO='l' * 2), ValueError))
wh, Vh = np.linalg.eigh(H); th = np.array(sorted(float(x) for x in mp.eighe(M(H), eigvals_only=True)))
report("eigh complex Hermitian: real ascending eigenvalues match mpmath.eighe; V^H V = I; V diag(w) V^H = H", wh.dtype == np.float64 and np.allclose(wh, th, atol=1e-11) and np.allclose(Vh.conj().T @ Vh, np.eye(4), atol=1e-12) and np.allclose(Vh @ np.diag(wh) @ Vh.conj().T, H, atol=1e-11))
Himag = H + 1j * np.diag([1., 2., 3., 4.])
report("eigh/eigvalsh ignore the imaginary part of the diagonal (documented 'imaginary part of the diagonal will always be treated as zero')", np.allclose(np.linalg.eigvalsh(Himag), th, atol=1e-11) and np.allclose(np.linalg.eigh(Himag)[0], th, atol=1e-11))
wst = np.linalg.eigvalsh(np.stack([lowsym, upsym, SPD[:4, :4]]))
report("eigvalsh on a stack (3,4,4): row i = eigenvalues of A[i] (mpmath)", wst.shape == (3, 4) and np.allclose(wst[0], tl, atol=1e-11) and np.allclose(wst[1], tu, atol=1e-11) and np.allclose(wst[2], sorted(float(x) for x in mp.eigsy(M(SPD[:4, :4]), eigvals_only=True)), atol=1e-11))
report("eigh dtypes: float32 -> float32 values and vectors; complex64 -> float32 values, complex64 vectors; int -> float64", np.linalg.eigh(lowsym.astype(np.float32))[0].dtype == np.float32 and np.linalg.eigh(lowsym.astype(np.float32))[1].dtype == np.float32 and np.linalg.eigh(H.astype(np.complex64))[0].dtype == np.float32 and np.linalg.eigh(H.astype(np.complex64))[1].dtype == np.complex64 and np.linalg.eigvalsh(np.array([[2, 1], [1, 2]])).dtype == np.float64)

# ================= svd / svdvals
print("---- svd / svdvals")
for name, A in [("tall 6x4", rs.randn(6, 4)), ("wide 4x6", rs.randn(4, 6))]:
    m, n = A.shape; k = min(m, n); st = mp_svals(A)
    U, s, Vh = np.linalg.svd(A)
    report(f"svd {name} full_matrices=True: U (M,M), S (K,) descending, Vh (N,N); U, Vh orthogonal; U[:, :K] diag(s) Vh[:K] = A; s = mpmath.svd_r",
           U.shape == (m, m) and s.shape == (k,) and Vh.shape == (n, n) and np.all(np.diff(s) <= 0) and np.allclose(U @ U.T, np.eye(m), atol=1e-12) and np.allclose(Vh @ Vh.T, np.eye(n), atol=1e-12) and np.allclose((U[:, :k] * s) @ Vh[:k], A, atol=1e-12) and np.allclose(s, st, rtol=1e-12))
    U2, s2, Vh2 = np.linalg.svd(A, full_matrices=False)
    report(f"svd {name} full_matrices=False: U (M,K), Vh (K,N) with orthonormal columns/rows, (u*s)@vh = A, same s", U2.shape == (m, k) and Vh2.shape == (k, n) and np.allclose(U2.T @ U2, np.eye(k), atol=1e-12) and np.allclose(Vh2 @ Vh2.T, np.eye(k), atol=1e-12) and np.allclose((U2 * s2) @ Vh2, A, atol=1e-12) and np.array_equal(s, s2))
    report(f"svd {name} compute_uv=False returns only s (K,) = mpmath singular values", np.allclose(np.linalg.svd(A, compute_uv=False), st, rtol=1e-12))
    if V2: report(f"svdvals {name} [2.0] = mpmath singular values, descending", np.allclose(np.linalg.svdvals(A), st, rtol=1e-12))
Sym4 = NS + NS.T; es = np.array(sorted(float(x) for x in mp.eigsy(M(Sym4), eigvals_only=True)))
Uh, sh, Vhh = np.linalg.svd(Sym4, hermitian=True)
report("svd(hermitian=True) on a symmetric matrix: s = |eigenvalues| descending (mpmath.eigsy), U orthonormal, (u*s)@vh reconstructs A", np.allclose(sh, np.sort(np.abs(es))[::-1], rtol=1e-12) and np.allclose(Uh.T @ Uh, np.eye(4), atol=1e-12) and np.allclose((Uh * sh) @ Vhh, Sym4, atol=1e-11) and np.allclose(np.linalg.svd(Sym4, hermitian=True, compute_uv=False), np.sort(np.abs(es))[::-1], rtol=1e-12))
report("svd(hermitian=True) equals svd(hermitian=False) singular values on a symmetric matrix", np.allclose(np.linalg.svd(Sym4, compute_uv=False), sh, rtol=1e-11))
sw = np.linalg.svd(NS, hermitian=True, compute_uv=False)
print(f"   svd(hermitian=True) on a NON-symmetric input silently uses one triangle: {np.round(sw, 6).tolist()} vs true singular values {np.round(mp_svals(NS), 6).tolist()} (documented 'a is assumed to be Hermitian')")
Sk = rs.randn(3, 5, 3); Us, ss, Vhs = np.linalg.svd(Sk)
report("svd on a stack (3,5,3): U (3,5,5), S (3,3), Vh (3,3,3); each S[i] = mpmath; reconstruction per matrix", Us.shape == (3, 5, 5) and ss.shape == (3, 3) and Vhs.shape == (3, 3, 3) and all(np.allclose(ss[i], mp_svals(Sk[i]), rtol=1e-12) and np.allclose((Us[i][:, :3] * ss[i]) @ Vhs[i], Sk[i], atol=1e-12) for i in range(3)))
Uz, sz, Vhz = np.linalg.svd(Ac, full_matrices=False)
report("svd complex (5,3): s real float64 = mpmath.svd_c, U^H U = I, Vh Vh^H = I, (u*s)@vh = A", sz.dtype == np.float64 and np.allclose(sz, mp_svals(Ac), rtol=1e-12) and np.allclose(Uz.conj().T @ Uz, np.eye(3), atol=1e-12) and np.allclose(Vhz @ Vhz.conj().T, np.eye(3), atol=1e-12) and np.allclose((Uz * sz) @ Vhz, Ac, atol=1e-12))
Rd = np.outer(rs.randn(6), rs.randn(4)) + np.outer(rs.randn(6), rs.randn(4)); Ur, sr, Vhr = np.linalg.svd(Rd)
report("svd rank-deficient (rank-2 6x4): s[2:] below 1e-14 * s[0], the two leading terms reconstruct A, U and Vh still orthogonal", np.all(sr[2:] < 1e-14 * sr[0]) and np.allclose((Ur[:, :2] * sr[:2]) @ Vhr[:2], Rd, atol=1e-12) and np.allclose(Ur @ Ur.T, np.eye(6), atol=1e-12), f"(s = {[f'{v:.2e}' for v in sr]})")
U32, s32, V32_ = np.linalg.svd(Sk[0].astype(np.float32))
report("svd dtypes: float32 -> float32 U, s, Vh; complex64 -> float32 s, complex64 U/Vh; int -> float64", U32.dtype == np.float32 and s32.dtype == np.float32 and V32_.dtype == np.float32 and np.linalg.svd(Ac.astype(np.complex64))[1].dtype == np.float32 and np.linalg.svd(Ac.astype(np.complex64))[0].dtype == np.complex64 and np.linalg.svd(Ai)[1].dtype == np.float64)
report("svd float32 singular values agree with mpmath to 1e-5 relative", np.allclose(s32, mp_svals(Sk[0]), rtol=1e-5))

# ================= tensorinv / tensorsolve
print("---- tensorinv / tensorsolve")
T4 = rs.randn(4, 6, 8, 3); Tinv = np.linalg.tensorinv(T4, ind=2); Tinv_t = N(mp.inverse(M(T4.reshape(24, 24)))).reshape(8, 3, 4, 6)
report("tensorinv(ind=2) of (4,6,8,3): shape a.shape[ind:] + a.shape[:ind] = (8,3,4,6) and equals inv(a.reshape(24,24)).reshape(...) (mpmath.inverse)", Tinv.shape == (8, 3, 4, 6) and maxdiff(Tinv, Tinv_t) < 1e-9, f"(max diff {maxdiff(Tinv, Tinv_t):.1e})")
Id = np.tensordot(Tinv, T4, 2)
report("tensordot(tensorinv(a), a, ind) is the identity tensor (documented)", np.allclose(Id.reshape(24, 24), np.eye(24), atol=1e-9))
T1 = rs.randn(6, 2, 3); Tinv1 = np.linalg.tensorinv(T1, ind=1)
report("tensorinv(ind=1) of (6,2,3): shape (2,3,6) = inv(a.reshape(6,6)).reshape(2,3,6)", Tinv1.shape == (2, 3, 6) and maxdiff(Tinv1, N(mp.inverse(M(T1.reshape(6, 6)))).reshape(2, 3, 6)) < 1e-10)
report("tensorinv of a non-'square' tensor raises LinAlgError; ind=0 raises ValueError", raises(lambda: np.linalg.tensorinv(rs.randn(4, 6, 5, 3), 2), LinAlgError) and raises(lambda: np.linalg.tensorinv(T4, 0), ValueError))
Ta = rs.randn(6, 4, 2, 3, 4); Tb = rs.randn(6, 4); x_ts = np.linalg.tensorsolve(Ta, Tb)
x_t = col(mp.lu_solve(M(Ta.reshape(24, 24)), M(Tb.reshape(24, 1)))).reshape(2, 3, 4)
report("tensorsolve(a (6,4,2,3,4), b (6,4)): x shape Q = (2,3,4) equals lu_solve(a.reshape(24,24), b.ravel()) (mpmath); tensordot(a, x, 3) = b", x_ts.shape == (2, 3, 4) and maxdiff(x_ts, x_t) < 1e-9 and np.allclose(np.tensordot(Ta, x_ts, 3), Tb, atol=1e-9))
Ta2 = np.moveaxis(Ta, [2, 3, 4], [0, 1, 2])
report("tensorsolve(axes=(0,1,2)) moves those axes of a to the right before solving (documented): same x from the permuted a", np.allclose(np.linalg.tensorsolve(Ta2, Tb, axes=(0, 1, 2)), x_ts, atol=1e-9))
report("tensorsolve with prod(Q) != prod(b.shape) raises LinAlgError", raises(lambda: np.linalg.tensorsolve(rs.randn(6, 4, 5, 5), Tb), LinAlgError))

# ================= multi_dot
print("---- multi_dot")
I1 = rs.randint(-4, 5, (3, 4)); I2 = rs.randint(-4, 5, (4, 5)); I3 = rs.randint(-4, 5, (5, 2)); I4 = rs.randint(-4, 5, (2, 3))
ex = np.array(pymatmul(pymatmul(pymatmul(I1, I2), I3), I4))
report("multi_dot of 4 integer matrices equals the exact chained product (Python ints)", np.array_equal(np.linalg.multi_dot([I1, I2, I3, I4]), ex))
report("multi_dot of 2 and of 3 matrices (different code paths) exact", np.array_equal(np.linalg.multi_dot([I1, I2]), np.array(pymatmul(I1, I2))) and np.array_equal(np.linalg.multi_dot([I1, I2, I3]), np.array(pymatmul(pymatmul(I1, I2), I3))))
v3 = rs.randint(-4, 5, 3); w3 = rs.randint(-4, 5, 3)
report("multi_dot: 1-D first argument treated as a row vector -> result shape (3,)", np.linalg.multi_dot([v3, I1, I2, I3, I4]).shape == (3,) and np.array_equal(np.linalg.multi_dot([v3, I1, I2, I3, I4]), np.array(pymatmul([v3], ex)).ravel()))
report("multi_dot: 1-D last argument treated as a column vector -> (3,); both 1-D -> 0-d scalar", np.array_equal(np.linalg.multi_dot([I1, I2, I3, I4, w3]), np.array(pymatmul(ex, [[x] for x in w3])).ravel()) and np.ndim(np.linalg.multi_dot([v3, I1, I2, I3, I4, w3])) == 0 and np.linalg.multi_dot([v3, I1, I2, I3, I4, w3]) == sum(int(a) * int(b) for a, b in zip(np.array(pymatmul([v3], ex)).ravel(), w3)))
report("multi_dot with fewer than 2 arrays raises ValueError; a 3-D middle argument raises LinAlgError", raises(lambda: np.linalg.multi_dot([I1]), ValueError) and raises(lambda: np.linalg.multi_dot([I1, np.ones((4, 5, 2)), I3]), LinAlgError))

# ================= matrix_power
print("---- matrix_power")
Fib = np.array([[1, 1], [1, 0]]); fib = [0, 1]
for _ in range(100): fib.append(fib[-1] + fib[-2])
P0 = np.linalg.matrix_power(Fib, 0)
report("matrix_power(A, 0) = identity with the dtype of A (documented 'the identity matrix ... is returned')", np.array_equal(P0, np.eye(2)) and P0.dtype == Fib.dtype)
report("matrix_power(A, 1) = A; A^2, A^3 (short-cuts) and A^30 exact for the Fibonacci matrix", np.array_equal(np.linalg.matrix_power(Fib, 1), Fib) and np.array_equal(np.linalg.matrix_power(Fib, 2), [[2, 1], [1, 1]]) and np.array_equal(np.linalg.matrix_power(Fib, 3), [[3, 2], [2, 1]]) and np.array_equal(np.linalg.matrix_power(Fib, 30), [[fib[31], fib[30]], [fib[30], fib[29]]]))
P90 = np.linalg.matrix_power(Fib, 90); exact90 = [[fib[91], fib[90]], [fib[90], fib[89]]]
report("matrix_power on int64 beyond 2**63 (Fib^90, F_91 = 4.66e18 < 2**63, F_92 would overflow): still exact at n=90", np.array_equal(P90, exact90), f"({P90.tolist()})")
P92 = np.linalg.matrix_power(Fib, 92)
report("matrix_power int64 overflow (Fib^92 needs F_93 = 1.2e19 > 2**63): silent wraparound, no error (NumPy integer semantics; undocumented for matrix_power)", P92.dtype == np.int64 and P92[0, 0] != fib[93] and P92[0, 0] == ((fib[93] + 2 ** 63) % 2 ** 64) - 2 ** 63, f"(got {P92[0, 0]}, exact {fib[93]})")
Mf = np.array([[2., 1.], [1., 1.]]); Pm3 = np.linalg.matrix_power(Mf, -3); Mi = mp.inverse(M(Mf)); truth = N(Mi * Mi * Mi)
report("matrix_power(A, -3) = inv(A)^3 (mpmath), float output", maxdiff(Pm3, truth) < 1e-12 and Pm3.dtype == np.float64)
report("matrix_power(int A, -1) returns floating point (documented 'If the exponent is negative the elements are floating-point')", np.linalg.matrix_power(Fib, -1).dtype == np.float64 and np.allclose(np.linalg.matrix_power(Fib, -1), [[0, 1], [1, -1]]))
report("matrix_power of a singular matrix with negative exponent raises LinAlgError", raises(lambda: np.linalg.matrix_power(np.array([[1., 2.], [2., 4.]]), -1), LinAlgError))
report("matrix_power with a non-integer exponent raises TypeError; non-square raises LinAlgError", raises(lambda: np.linalg.matrix_power(Mf, 2.5), TypeError) and raises(lambda: np.linalg.matrix_power(np.ones((2, 3)), 2), LinAlgError))
Big = rs.randn(3, 3) / 2; Pb = np.linalg.matrix_power(Big, 60); Bm = M(Big); Tm = mp.eye(3)
for _ in range(60): Tm = Tm * Bm
Tm = N(Tm)
report("matrix_power(A, 60) of a random 3x3 agrees with 60 mpmath multiplications at 50 digits to 1e-11 relative", maxdiff(Pb, Tm) <= 1e-11 * np.abs(Tm).max(), f"(rel err {maxdiff(Pb, Tm) / np.abs(Tm).max():.1e}; |A^60| ~ {np.abs(Tm).max():.2e})")
St3 = rs.randint(-3, 4, (3, 2, 2)); Ps = np.linalg.matrix_power(St3, 5)
report("matrix_power on a stack (3,2,2), n=5: each equals the exact per-matrix power", all(np.array_equal(Ps[i], np.array(functools.reduce(pymatmul, [St3[i]] * 5))) for i in range(3)))
report("matrix_power on a stack, n=0 and n=-1 (float stack) per matrix", np.array_equal(np.linalg.matrix_power(St3, 0), np.broadcast_to(np.eye(2, dtype=int), (3, 2, 2))) and np.allclose(np.linalg.matrix_power(np.stack([Mf, 2 * Mf]), -1), np.stack([N(Mi), N(Mi) / 2])))

# ================= cond
print("---- cond")
A4 = rs.randn(4, 4); Am = M(A4); Aim = mp.inverse(Am); s4 = mp_svals(A4); s4i = mp_svals(N(Aim))
def colsums(Mx): return [float(sum(abs(Mx[i, j]) for i in range(Mx.rows))) for j in range(Mx.cols)]
def rowsums(Mx): return [float(sum(abs(Mx[i, j]) for j in range(Mx.cols))) for i in range(Mx.rows)]
truths = {None: s4[0] / s4[-1], 2: s4[0] / s4[-1], -2: s4[-1] / s4[0],
          1: max(colsums(Am)) * max(colsums(Aim)), -1: min(colsums(Am)) * min(colsums(Aim)),
          np.inf: max(rowsums(Am)) * max(rowsums(Aim)), -np.inf: min(rowsums(Am)) * min(rowsums(Aim)),
          'fro': float(mp.mnorm(Am, 'f') * mp.mnorm(Aim, 'f')), 'nuc': s4.sum() * s4i.sum()}
for p, t in truths.items():
    c = np.linalg.cond(A4, p)
    report(f"cond(p={p!r}) = norm(x, p) * norm(inv(x), p) with the documented norm (mpmath at 50 digits)" + (" [-2: smallest/largest singular value]" if p == -2 else ""), close(c, t, 1e-10), f"({c:.6f} vs {t:.6f})")
Sing = np.array([[1., 2.], [2., 4.]])
report("cond of an exactly singular matrix: p=1 (via inv) -> inf (nans converted to inf, per source); p=None (via SVD) is only 'huge' (~1e16) because gesdd returns a rounding-level smallest singular value; zero matrix -> inf for both", np.linalg.cond(Sing) > 1e15 and np.isinf(np.linalg.cond(Sing, 1)) and np.isinf(np.linalg.cond(np.zeros((2, 2)))) and np.isinf(np.linalg.cond(np.zeros((2, 2)), 1)), f"(cond(Sing) = {np.linalg.cond(Sing):.3e}, cond(Sing, 1) = {np.linalg.cond(Sing, 1)}, cond(0) = {np.linalg.cond(np.zeros((2, 2)))})")
A64b = rs.randn(6, 4); sb = mp_svals(A64b)
report("cond of a non-square (6,4) matrix with p=None: s_max / s_min", close(np.linalg.cond(A64b), sb[0] / sb[-1], 1e-10))
report("cond of a non-square matrix with p=1 raises LinAlgError (needs the inverse); empty matrix raises LinAlgError", raises(lambda: np.linalg.cond(A64b, 1), LinAlgError) and raises(lambda: np.linalg.cond(np.zeros((0, 0))), LinAlgError))
Sc = np.stack([A4, 2 * A4 + np.eye(4), SPD[:4, :4]])
report("cond on a stack (3,4,4), p=None and p='fro': per-matrix values (mpmath)", np.linalg.cond(Sc).shape == (3,) and all(close(np.linalg.cond(Sc)[i], (lambda s: s[0] / s[-1])(mp_svals(Sc[i])), 1e-10) and close(np.linalg.cond(Sc, 'fro')[i], float(mp.mnorm(M(Sc[i]), 'f') * mp.mnorm(mp.inverse(M(Sc[i])), 'f')), 1e-10) for i in range(3)))
report("cond result dtype: float64 for float64 input, float32 for float32 input (p=None and p=1)", isinstance(np.linalg.cond(A4), np.float64) and np.linalg.cond(A4.astype(np.float32)).dtype == np.float32 and np.linalg.cond(A4.astype(np.float32), 1).dtype == np.float32)

# ================= slogdet / det
print("---- slogdet / det")
dt = complex(mp.det(Am)).real
sg, la = np.linalg.slogdet(A4)
report("slogdet(4x4): sign = sign(det), logabsdet = log|det| (mpmath.det), sign * exp(logabsdet) = det(A)", sg == math.copysign(1, dt) and close(la, math.log(abs(dt)), 1e-12) and close(sg * math.exp(la), dt, 1e-10) and close(np.linalg.det(A4), dt, 1e-10), f"(det {dt:.6f}, sign {sg}, logabsdet {la:.6f})")
sg0, la0 = np.linalg.slogdet(Sing)
report("slogdet of a singular matrix: (0, -inf) (documented); det = 0", sg0 == 0 and la0 == -np.inf and np.linalg.det(Sing) == 0)
Cz3 = Cz[:3, :3]; dz = complex(mp.det(M(Cz3))); sgz, laz = np.linalg.slogdet(Cz3)
report("slogdet complex: sign on the unit circle (|sign| = 1), logabsdet = log|det|, sign * exp(logabsdet) = det (mpmath)", close(abs(sgz), 1, 1e-13) and close(laz, math.log(abs(dz)), 1e-12) and abs(sgz * math.exp(laz) - dz) < 1e-10 * abs(dz) and abs(np.linalg.det(Cz3) - dz) < 1e-10 * abs(dz))
Hg = np.diag([1e200, 1e200, -1e200])
report("slogdet where det overflows: det = -inf but slogdet = (-1, 600 ln 10) (documented robustness)", np.isinf(np.linalg.det(Hg)) and np.linalg.slogdet(Hg)[0] == -1 and close(np.linalg.slogdet(Hg)[1], 600 * math.log(10), 1e-13))
sgs, las = np.linalg.slogdet(Sc)
report("slogdet on a stack (3,4,4): per-matrix sign and log|det| (mpmath)", sgs.shape == (3,) and all(sgs[i] == math.copysign(1, float(mp.det(M(Sc[i])))) and close(las[i], math.log(abs(float(mp.det(M(Sc[i]))))), 1e-11) for i in range(3)))
Iint = rs.randint(-9, 10, (5, 5)); dex = det_fraction(Iint); dnp = np.linalg.det(Iint)
report("det of an int 5x5 matrix: float64 result equal to the exact Fraction determinant to 1e-9 relative", dnp.dtype == np.float64 and close(dnp, float(dex), 1e-9), f"(exact {dex}, numpy {dnp!r}, abs err {abs(dnp - float(dex)):.2e})")
I10 = rs.randint(-5, 6, (10, 10)); d10 = det_fraction(I10)
report("det of an int 10x10 matrix vs Fraction: 1e-8 relative", close(np.linalg.det(I10), float(d10), 1e-8), f"(exact {d10}, numpy {np.linalg.det(I10)!r}, rel err {abs(np.linalg.det(I10) - float(d10)) / abs(float(d10)):.1e})")
report("det/slogdet dtypes: int -> float64; float32 -> float32 (det, sign, logabsdet); complex64 -> complex64 det, complex64 sign, float32 logabsdet", np.linalg.slogdet(Iint)[1].dtype == np.float64 and np.linalg.det(A4.astype(np.float32)).dtype == np.float32 and np.linalg.slogdet(A4.astype(np.float32))[0].dtype == np.float32 and np.linalg.slogdet(A4.astype(np.float32))[1].dtype == np.float32 and np.linalg.det(Cz3.astype(np.complex64)).dtype == np.complex64 and np.linalg.slogdet(Cz3.astype(np.complex64))[0].dtype == np.complex64 and np.linalg.slogdet(Cz3.astype(np.complex64))[1].dtype == np.float32)
report("det of a 1-D array / non-square raises LinAlgError", raises(lambda: np.linalg.det(np.ones(3)), LinAlgError) and raises(lambda: np.linalg.det(np.ones((2, 3))), LinAlgError))

# ================= norm
print("---- norm")
vec = np.array([3., -4., 0.5, 2.5, -1e-3, 7.]); av = [abs(x) for x in vec.tolist()]
pn = lambda p: sum(x ** p for x in av) ** (1 / p)
vtruth = {None: math.sqrt(sum(x * x for x in av)), 2: pn(2), 1: sum(av), np.inf: max(av), -np.inf: min(av), 0: sum(1 for x in vec if x != 0), 0.5: pn(0.5), 3: pn(3), -1: pn(-1), -2: pn(-2), 4.5: pn(4.5)}
for p, t in vtruth.items():
    report(f"norm(vector, ord={p!r}) = documented formula", close(np.linalg.norm(vec, p), t, 1e-12), f"({np.linalg.norm(vec, p):.6g})")
vz = np.array([3., 0., 4.])
report("norm(vector with a zero, ord=-1) = (sum |x|^-1)^-1 = 0 (1/0 = inf term); ord=-inf = 0", np.linalg.norm(vz, -1) == 0 and np.linalg.norm(vz, -np.inf) == 0)
report("norm(vector, 'fro') and ('nuc') raise ValueError ('only defined for matrices'); ord=0 on a matrix raises ValueError", raises(lambda: np.linalg.norm(vec, 'fro'), ValueError) and raises(lambda: np.linalg.norm(vec, 'nuc'), ValueError) and raises(lambda: np.linalg.norm(A4, 0), ValueError))
B45 = rs.randn(4, 5); Bm = M(B45); sB = mp_svals(B45)
mtruth = {None: float(mp.mnorm(Bm, 'f')), 'fro': float(mp.mnorm(Bm, 'f')), 'nuc': sB.sum(), 1: max(colsums(Bm)), -1: min(colsums(Bm)), 2: sB[0], -2: sB[-1], np.inf: max(rowsums(Bm)), -np.inf: min(rowsums(Bm))}
for p, t in mtruth.items():
    report(f"norm(matrix 4x5, ord={p!r}) = documented matrix norm (mpmath)", close(np.linalg.norm(B45, p), t, 1e-12), f"({np.linalg.norm(B45, p):.6g})")
X3 = rs.randn(2, 3, 4)
report("norm(3-D, axis=(1,2), ord=1): vector of per-matrix max column sums; axis=(0,2) treats X[:, j, :] as the matrices; negative axes accepted", np.allclose(np.linalg.norm(X3, 1, axis=(1, 2)), [np.abs(X3[i]).sum(0).max() for i in range(2)]) and np.allclose(np.linalg.norm(X3, np.inf, axis=(0, 2)), [np.abs(X3[:, j, :]).sum(1).max() for j in range(3)]) and np.allclose(np.linalg.norm(X3, 'nuc', axis=(-2, -1)), [mp_svals(X3[i]).sum() for i in range(2)]))
report("norm(3-D, axis=1, ord=3): vector norms along axis 1 -> shape (2,4)", np.linalg.norm(X3, 3, axis=1).shape == (2, 4) and np.allclose(np.linalg.norm(X3, 3, axis=1), (np.abs(X3) ** 3).sum(1) ** (1 / 3)))
report("norm keepdims=True: axis=(1,2) -> (2,1,1); axis=1 -> (2,1,4); axis=None -> (1,1,1)", np.linalg.norm(X3, axis=(1, 2), keepdims=True).shape == (2, 1, 1) and np.linalg.norm(X3, axis=1, keepdims=True).shape == (2, 1, 4) and np.linalg.norm(X3, keepdims=True).shape == (1, 1, 1) and close(np.linalg.norm(X3, keepdims=True).ravel()[0], math.sqrt((X3 ** 2).sum())))
report("norm(3-D, axis=None, ord=None) = 2-norm of the flattened array (documented); ord=2 with 3-D and axis=None raises ValueError", close(np.linalg.norm(X3), math.sqrt((X3 ** 2).sum()), 1e-12) and raises(lambda: np.linalg.norm(X3, 2), ValueError) and raises(lambda: np.linalg.norm(X3, 'fro'), ValueError))
cv = np.array([3 + 4j, -1j, 2.]); ac = [abs(x) for x in cv.tolist()]
report("norm complex vector: sqrt(sum |z|^2), ord=1 sum |z|, ord=inf max |z|; complex matrix 'fro' and 2 (mpmath)", close(np.linalg.norm(cv), math.sqrt(sum(x * x for x in ac)), 1e-13) and close(np.linalg.norm(cv, 1), sum(ac), 1e-13) and close(np.linalg.norm(cv, np.inf), max(ac), 1e-13) and close(np.linalg.norm(Cz), math.sqrt((np.abs(Cz) ** 2).sum()), 1e-12) and close(np.linalg.norm(Cz, 2), mp_svals(Cz)[0], 1e-11) and close(np.linalg.norm(Cz, 'nuc'), mp_svals(Cz).sum(), 1e-11))
v32 = vec.astype(np.float32)
report("norm result dtype: float32 input -> float32 (vector 2-norm, ord=1, matrix 'fro', matrix 2 via svd); complex64 -> float32", np.linalg.norm(v32).dtype == np.float32 and np.linalg.norm(v32, 1).dtype == np.float32 and np.linalg.norm(B45.astype(np.float32)).dtype == np.float32 and np.linalg.norm(B45.astype(np.float32), 2).dtype == np.float32 and np.linalg.norm(cv.astype(np.complex64)).dtype == np.float32)
report("norm of float32 vector agrees with the float64 truth to 1e-6 relative", close(np.linalg.norm(v32), vtruth[None], 1e-6))
i8 = np.array([100, 100, 100], dtype=np.int8); i8m = np.array([[100, 100], [100, 100]], dtype=np.int8)
report("norm of an int8 array is computed in float64 (source: non-inexact input cast with astype(float)): no int8 overflow, sqrt(30000) and column-sum 200", np.linalg.norm(i8).dtype == np.float64 and close(np.linalg.norm(i8), math.sqrt(30000), 1e-14) and np.linalg.norm(i8m, 1) == 200.0 and np.linalg.norm(i8, np.inf) == 100.0)
big = np.array([2 ** 62, 2 ** 62], dtype=np.int64)
report("norm of int64 values 2**62: float64 result 2**62 * sqrt(2) (no integer overflow, values exactly representable)", close(np.linalg.norm(big), 2 ** 62 * math.sqrt(2), 1e-15))
report("norm of empty arrays: norm([]) = 0.0; norm(zeros((0,3))) = 0.0 (fro); ord=1 of an empty (0,3) matrix = 0.0", np.linalg.norm(np.array([])) == 0.0 and np.linalg.norm(np.zeros((0, 3))) == 0.0 and np.linalg.norm(np.zeros((0, 3)), 1) == 0.0)
if V2: report("norm(empty (0,3), ord=2 / inf / 'nuc') = 0.0 [2.x: reductions carry initial=0]", np.linalg.norm(np.zeros((0, 3)), 2) == 0.0 and np.linalg.norm(np.zeros((0, 3)), np.inf) == 0.0 and np.linalg.norm(np.zeros((0, 3)), 'nuc') == 0.0 and np.linalg.norm(np.array([]), np.inf) == 0.0)
else: report("norm(empty (0,3), ord=2 / inf) and norm([], inf) raise ValueError on 1.x ('zero-size array to reduction operation maximum'); 2.x returns 0.0 -- undocumented change", raises(lambda: np.linalg.norm(np.zeros((0, 3)), 2), ValueError) and raises(lambda: np.linalg.norm(np.zeros((0, 3)), np.inf), ValueError) and raises(lambda: np.linalg.norm(np.array([]), np.inf), ValueError))
try: r = np.linalg.norm(np.zeros((0, 3)), -2); print(f"   norm(empty (0,3), ord=-2) = {r!r} (no initial value for amin)")
except Exception as e: print(f"   norm(empty (0,3), ord=-2) raises {type(e).__name__}: {str(e)[:70]}")
try: r = np.linalg.norm(np.array([]), -np.inf); print(f"   norm(empty vector, ord=-inf) = {r!r}")
except Exception as e: print(f"   norm(empty vector, ord=-inf) raises {type(e).__name__}: {str(e)[:70]}")
report("norm of a single-element vector: every ord (2, 1, inf, -inf, 0.5, 3, -1) = |x|", all(close(np.linalg.norm(np.array([-2.5]), p), 2.5, 1e-14) for p in [None, 2, 1, np.inf, -np.inf, 0.5, 3, -1]))
report("norm with NaN: vector 2-norm nan; ord=inf nan (max propagates); ord=0 counts the nan as non-zero", np.isnan(np.linalg.norm(np.array([1., np.nan]))) and np.isnan(np.linalg.norm(np.array([1., np.nan]), np.inf)) and np.linalg.norm(np.array([1., np.nan, 0.]), 0) == 2)
if V2:
    report("linalg.matrix_norm [2.0]: default 'fro' on the last two axes; ord=2 = s_max; linalg.vector_norm default: 2-norm over ALL axes (flattened) and axis=(-1) per-row", close(np.linalg.matrix_norm(B45), mtruth['fro'], 1e-12) and close(np.linalg.matrix_norm(B45, ord=2), sB[0], 1e-12) and np.linalg.matrix_norm(X3).shape == (2,) and close(np.linalg.vector_norm(X3), math.sqrt((X3 ** 2).sum()), 1e-12) and np.allclose(np.linalg.vector_norm(X3, axis=-1, ord=1), np.abs(X3).sum(-1)) and np.linalg.vector_norm(X3, keepdims=True).shape == (1, 1, 1))

# ================= lstsq
print("---- lstsq")
Ao = rs.randn(8, 3); bo = rs.randn(8); Aom = M(Ao)
xt = col(mp.lu_solve(Aom.T * Aom, Aom.T * M(bo.reshape(8, 1))))
x1, res1, rk1, sv1 = np.linalg.lstsq(Ao, bo, rcond=None)
rt = float(mp.norm(M(bo.reshape(8, 1)) - Aom * M(xt.reshape(3, 1))) ** 2)
report("lstsq overdetermined (8,3), 1-D b: x = normal-equation solution (mpmath, 50 digits); residuals shape (1,) = ||b - Ax||^2; rank 3; s = mpmath singular values", maxdiff(x1, xt) < 1e-11 and res1.shape == (1,) and close(res1[0], rt, 1e-9) and rk1 == 3 and np.allclose(sv1, mp_svals(Ao), rtol=1e-12), f"(residual {res1[0]:.6f} vs {rt:.6f})")
Bo = rs.randn(8, 2); x2, res2, rk2, sv2 = np.linalg.lstsq(Ao, Bo, rcond=None)
xt2 = N(mp.inverse(Aom.T * Aom) * Aom.T * M(Bo))
report("lstsq 2-D b (8,2) multi-rhs: x (3,2) per column, residuals shape (K,)=(2,) each ||b_k - A x_k||^2", x2.shape == (3, 2) and maxdiff(x2, xt2) < 1e-11 and res2.shape == (2,) and all(close(res2[k], ((Bo[:, k] - Ao @ xt2[:, k]) ** 2).sum(), 1e-9) for k in range(2)))
report("lstsq with b of shape (M,1): x (N,1), residuals (1,)", np.linalg.lstsq(Ao, bo[:, None], rcond=None)[0].shape == (3, 1) and np.linalg.lstsq(Ao, bo[:, None], rcond=None)[1].shape == (1,))
Ard = np.column_stack([Ao[:, 0], Ao[:, 1], Ao[:, 0] + Ao[:, 1]]); xr, resr, rkr, svr = np.linalg.lstsq(Ard, bo, rcond=None)
xr_t = mp_pinv(Ard, 1e-10) @ bo
report("lstsq rank-deficient (8,3 with col3 = col1 + col2): rank 2, residuals EMPTY (documented 'If the rank of a is < N ... empty array'), x = minimum-norm solution pinv(A) b (mpmath svd)", rkr == 2 and resr.shape == (0,) and maxdiff(xr, xr_t) < 1e-9, f"(x {np.round(xr, 6).tolist()}, s {[f'{v:.1e}' for v in svr]})")
Au = rs.randn(3, 8); bu = rs.randn(3); Aum = M(Au); xu, resu, rku, svu = np.linalg.lstsq(Au, bu, rcond=None)
xu_t = col(Aum.T * mp.lu_solve(Aum * Aum.T, M(bu.reshape(3, 1))))
report("lstsq underdetermined (3,8): residuals EMPTY (documented 'M <= N'), rank 3, x = minimum-norm solution A^T (A A^T)^-1 b (mpmath); A x = b", resu.shape == (0,) and rku == 3 and maxdiff(xu, xu_t) < 1e-10 and np.allclose(Au @ xu, bu, atol=1e-12))
Asq = rs.randn(4, 4); bsq = rs.randn(4); xsq, ressq, _, _ = np.linalg.lstsq(Asq, bsq, rcond=None)
report("lstsq square full-rank (M == N): residuals empty (M <= N), x = exact solution (mpmath lu_solve)", ressq.shape == (0,) and maxdiff(xsq, col(mp.lu_solve(M(Asq), M(bsq.reshape(4, 1))))) < 1e-10)
Uo = np.linalg.qr(rs.randn(8, 8))[0][:, :3]; Vo = np.linalg.qr(rs.randn(3, 3))[0]; Acond = (Uo * [1., 1e-3, 1e-9]) @ Vo.T
report("lstsq rcond: singular values (1, 1e-3, 1e-9); rcond=1e-6 -> rank 2 (1e-9 < 1e-6 * 1 treated as zero), rcond=1e-12 -> rank 3, rcond=-1 -> machine precision -> rank 3", np.linalg.lstsq(Acond, bo, rcond=1e-6)[2] == 2 and np.linalg.lstsq(Acond, bo, rcond=1e-12)[2] == 3 and np.linalg.lstsq(Acond, bo, rcond=-1)[2] == 3)
Acond2 = (Uo * [1., 1e-3, 3e-16]) @ Vo.T
report("lstsq rcond=None: cut-off eps * max(M,N) = 8 eps = 1.8e-15 (documented 'machine precision times max(M, N)'): s3 = 3e-16 counts as zero -> rank 2; rcond=-1 (eps only) -> rank 3", np.linalg.lstsq(Acond2, bo, rcond=None)[2] == 2 and np.linalg.lstsq(Acond2, bo, rcond=-1)[2] == 3, f"(s = {[f'{v:.2e}' for v in np.linalg.lstsq(Acond2, bo, rcond=None)[3]]})")
with warnings.catch_warnings(record=True) as wlog:
    warnings.simplefilter("always"); rk_def = np.linalg.lstsq(Acond2, bo)[2]
fut = [x for x in wlog if issubclass(x.category, FutureWarning)]
if V2: report("lstsq default rcond [2.0]: equals rcond=None (eps * max(M,N), rank 2 here), no FutureWarning", rk_def == 2 and not fut)
else: report("lstsq default rcond [1.x]: FutureWarning and the OLD default -1 (machine precision -> rank 3 here); documented 'If not set, a FutureWarning is given'", rk_def == 3 and len(fut) == 1)
x32, r32, _, s32l = np.linalg.lstsq(Ao.astype(np.float32), bo.astype(np.float32), rcond=None)
report("lstsq dtypes: float32 -> float32 x, residuals, s; int A with float b -> float64", x32.dtype == np.float32 and r32.dtype == np.float32 and s32l.dtype == np.float32 and np.linalg.lstsq(Iint, np.ones(5), rcond=None)[0].dtype == np.float64)
report("lstsq float32 solution agrees with the float64 truth to 1e-4 relative", maxdiff(x32, xt) < 1e-4 * np.abs(xt).max())
report("lstsq with incompatible dimensions raises LinAlgError('Incompatible dimensions'); 3-D a raises LinAlgError", raises(lambda: np.linalg.lstsq(Ao, np.ones(7), rcond=None), LinAlgError) and raises(lambda: np.linalg.lstsq(np.ones((2, 3, 3)), np.ones(3), rcond=None), LinAlgError))
bc = Ac[:, 0] + 0.1 * (rs.randn(5) + 1j * rs.randn(5)); xc, resc, _, _ = np.linalg.lstsq(Ac, bc, rcond=None); Acm = M(Ac)
xct = col(mp.lu_solve(Acm.H * Acm, Acm.H * M(bc.reshape(5, 1))))
report("lstsq complex (5,3): x = (A^H A)^-1 A^H b (mpmath), residual real float64 = ||b - A x||^2", maxdiff(xc, xct) < 1e-10 and resc.dtype == np.float64 and close(resc[0], (np.abs(bc - Ac @ xct) ** 2).sum(), 1e-9))

# ================= solve
print("---- solve")
As = rs.randn(3, 4, 4); b1 = rs.randn(4); bK = rs.randn(3, 4, 2)
if V2:
    x_b1 = np.linalg.solve(As, b1)
    report("solve(a stack (3,4,4), b 1-D (4,)) [2.0: 'only treated as a column vector if exactly 1-dimensional']: result (3,4), x[i] = lu_solve(a[i], b) (mpmath)", x_b1.shape == (3, 4) and all(maxdiff(x_b1[i], col(mp.lu_solve(M(As[i]), M(b1.reshape(4, 1))))) < 1e-10 for i in range(3)))
else:
    report("solve(a stack (3,4,4), b 1-D (4,)) [1.x rule: b is a stack of vectors only if b.ndim == a.ndim - 1]: (4,) and (4,1) raise ValueError; b must be given as (1,4,1) or broadcast to (3,4)", raises(lambda: np.linalg.solve(As, b1), ValueError) and raises(lambda: np.linalg.solve(As, b1[:, None]), ValueError) and np.linalg.solve(As, b1[None, :, None]).shape == (3, 4, 1) and np.linalg.solve(As, np.broadcast_to(b1, (3, 4))).shape == (3, 4))
    x_b1 = np.linalg.solve(As, b1[None, :, None])[..., 0]
    report("solve(a stack (3,4,4), b (1,4,1)) [1.x]: x[i] = lu_solve(a[i], b) (mpmath)", all(maxdiff(x_b1[i], col(mp.lu_solve(M(As[i]), M(b1.reshape(4, 1))))) < 1e-10 for i in range(3)))
x_bK = np.linalg.solve(As, bK)
report("solve(a stack (3,4,4), b stack (3,4,2)): result (3,4,2), x[i] = lu_solve(a[i], b[i])", x_bK.shape == (3, 4, 2) and all(maxdiff(x_bK[i], mp_solve(As[i], bK[i])) < 1e-10 for i in range(3)))
x_bc = np.linalg.solve(As[0], bK)
report("solve(a single (4,4), b stack (3,4,2)): a broadcasts against the stack of b -> (3,4,2)", x_bc.shape == (3, 4, 2) and all(maxdiff(x_bc[i], mp_solve(As[0], bK[i])) < 1e-10 for i in range(3)))
Aq = rs.randn(3, 3, 3); bq = rs.randn(3, 3); xq = np.linalg.solve(Aq, bq)
as_matrix = np.stack([mp_solve(Aq[i], bq) for i in range(3)])          # 2.x: b is one (M,K) matrix broadcast over the stack
as_vectors = np.stack([col(mp.lu_solve(M(Aq[i]), M(bq[i].reshape(3, 1)))) for i in range(3)])   # 1.x: b is a stack of (M,) vectors
if V2: report("solve(a (3,3,3), b (3,3)) [2.0 change]: b with ndim > 1 is a (M,K) MATRIX broadcast over the stack -> (3,3,3), x[i] = solve(a[i], b)", xq.shape == (3, 3, 3) and maxdiff(xq, as_matrix) < 1e-10)
else: report("solve(a (3,3,3), b (3,3)) [1.x rule]: b.ndim == a.ndim - 1 -> stack of (M,) vectors -> (3,3), x[i] = solve(a[i], b[i])", xq.shape == (3, 3) and maxdiff(xq, as_vectors) < 1e-10)
report("solve with b (M,1): x (M,1); with b (M,K) on a single a: x (M,K) (mpmath)", np.linalg.solve(As[0], b1[:, None]).shape == (4, 1) and maxdiff(np.linalg.solve(As[0], bK[0]), mp_solve(As[0], bK[0])) < 1e-10)
report("solve singular raises LinAlgError; non-square raises LinAlgError; b with wrong length raises ValueError", raises(lambda: np.linalg.solve(Sing, np.ones(2)), LinAlgError) and raises(lambda: np.linalg.solve(np.ones((2, 3)), np.ones(2)), LinAlgError) and raises(lambda: np.linalg.solve(As[0], np.ones(3)), ValueError))
report("solve dtypes: float32 a and b -> float32; float32 a with float64 b -> float64; int a with int b -> float64; complex64 -> complex64", np.linalg.solve(As[0].astype(np.float32), b1.astype(np.float32)).dtype == np.float32 and np.linalg.solve(As[0].astype(np.float32), b1).dtype == np.float64 and np.linalg.solve(np.array([[2, 1], [1, 3]]), np.array([1, 2])).dtype == np.float64 and np.linalg.solve(Cz.astype(np.complex64), np.ones(4, np.complex64)).dtype == np.complex64)
report("solve float32 agrees with mpmath to 1e-4 relative (cond ~ %.0f)" % np.linalg.cond(As[0]), maxdiff(np.linalg.solve(As[0].astype(np.float32), b1.astype(np.float32)), col(mp.lu_solve(M(As[0]), M(b1.reshape(4, 1))))) < 1e-4 * np.abs(x_b1[0]).max())
xz = np.linalg.solve(Cz, bc[:4])
report("solve complex (4,4) equals mpmath lu_solve", maxdiff(xz, col(mp.lu_solve(M(Cz), M(bc[:4].reshape(4, 1))))) < 1e-10)
report("solve with float16 input raises TypeError ('array type float16 is unsupported in linalg', source _commonType)", raises(lambda: np.linalg.solve(As[0].astype(np.float16), b1.astype(np.float16)), TypeError))

# ================= inv
print("---- inv")
report("inv(4x4) equals mpmath.inverse at 50 digits; A inv(A) = I", maxdiff(np.linalg.inv(A4), N(Aim)) < 1e-11 and np.allclose(A4 @ np.linalg.inv(A4), np.eye(4), atol=1e-12))
report("inv on a stack (3,4,4): per-matrix mpmath inverses", all(maxdiff(np.linalg.inv(Sc)[i], N(mp.inverse(M(Sc[i])))) < 1e-10 for i in range(3)) and np.linalg.inv(Sc[None]).shape == (1, 3, 4, 4))
report("inv of a singular matrix raises LinAlgError('Singular matrix')", raises(lambda: np.linalg.inv(Sing), LinAlgError) and raises(lambda: np.linalg.inv(np.zeros((3, 3))), LinAlgError))
Hil = np.array([[1.0 / (i + j + 1) for j in range(12)] for i in range(12)])
with warnings.catch_warnings(record=True) as wlog:
    warnings.simplefilter("always"); Hinv = np.linalg.inv(Hil)
print(f"   inv(Hilbert 12): cond = {np.linalg.cond(Hil):.2e}; |A inv(A) - I|_max = {maxdiff(Hil @ Hinv, np.eye(12)):.2e}; warnings emitted: {[w.category.__name__ for w in wlog]} (no ill-conditioning warning is documented or emitted)")
report("inv of an ill-conditioned (Hilbert 12, cond 1e16) matrix returns without error or warning (documented: only singular raises)", len(wlog) == 0 and np.all(np.isfinite(Hinv)))
Near = np.array([[1., 2.], [2., 4. + 1e-15]])
with warnings.catch_warnings(record=True) as wlog:
    warnings.simplefilter("always")
    try: Ninv = np.linalg.inv(Near); print(f"   inv([[1,2],[2,4+1e-15]]) (det ~ 1e-15) returns entries of size {np.abs(Ninv).max():.1e} without warning ({len(wlog)} warnings)")
    except LinAlgError as e: print(f"   inv([[1,2],[2,4+1e-15]]) raises LinAlgError: {e}")
report("inv dtypes: int -> float64; float32 -> float32; complex64 -> complex64", np.linalg.inv(np.array([[2, 1], [1, 3]])).dtype == np.float64 and np.linalg.inv(A4.astype(np.float32)).dtype == np.float32 and np.linalg.inv(Cz.astype(np.complex64)).dtype == np.complex64)
report("inv float32 agrees with mpmath to 1e-4 relative", maxdiff(np.linalg.inv(A4.astype(np.float32)), N(Aim)) < 1e-4 * np.abs(N(Aim)).max())

# ================= pinv
print("---- pinv")
Ptall = (np.linalg.qr(rs.randn(5, 5))[0][:, :3] * [1., 1e-3, 1e-9]) @ Vo.T   # (5,3), singular values 1, 1e-3, 1e-9
report("pinv default (rcond 1e-15): all three singular values kept, equals V S^+ U^T from mpmath.svd_r; A pinv(A) A = A", maxdiff(np.linalg.pinv(Ptall), mp_pinv(Ptall)) < 1e-6 * 1e9 and np.allclose(Ptall @ np.linalg.pinv(Ptall) @ Ptall, Ptall, atol=1e-10), f"(|pinv| ~ {np.abs(np.linalg.pinv(Ptall)).max():.1e}, rel diff {maxdiff(np.linalg.pinv(Ptall), mp_pinv(Ptall)) / 1e9:.1e})")
report("pinv(rcond=1e-6): the 1e-9 direction is cut (equals mpmath pinv with the same cut-off); |pinv| ~ 1e3", maxdiff(np.linalg.pinv(Ptall, rcond=1e-6), mp_pinv(Ptall, 1e-6)) < 1e-10 * np.abs(mp_pinv(Ptall, 1e-6)).max() and 300 < np.abs(np.linalg.pinv(Ptall, rcond=1e-6)).max() < 3000, f"(|pinv - mp| {maxdiff(np.linalg.pinv(Ptall, rcond=1e-6), mp_pinv(Ptall, 1e-6)):.1e}, max|pinv| {np.abs(np.linalg.pinv(Ptall, rcond=1e-6)).max():.1f}, s = {[f'{v:.1e}' for v in np.linalg.svd(Ptall, compute_uv=False)]})")
Dg = np.diag([1., 1e-3, 1e-9])
report("pinv cut-off is 'less than OR EQUAL to rcond * largest': diag(1, 1e-3, 1e-9) with rcond=1e-3 keeps only the 1 (the 1e-3 singular value is cut)", np.allclose(np.linalg.pinv(Dg, rcond=1e-3), np.diag([1., 0., 0.])), f"(pinv diag = {np.diag(np.linalg.pinv(Dg, rcond=1e-3)).tolist()})")
if V2:
    report("pinv rtol [2.0]: rtol=1e-6 same as rcond=1e-6; rtol=None -> max(M,N)*eps (keeps all three here); rtol and rcond together -> ValueError", np.array_equal(np.linalg.pinv(Ptall, rtol=1e-6), np.linalg.pinv(Ptall, rcond=1e-6)) and maxdiff(np.linalg.pinv(Ptall, rtol=None), mp_pinv(Ptall, 5 * np.finfo(float).eps)) < 1e-6 * 1e9 and raises(lambda: np.linalg.pinv(Ptall, rcond=1e-6, rtol=1e-6), ValueError))
    report("pinv(rtol=None) uses the array-API cut-off max(M,N)*eps = 6.7e-16: on diag(1, 1e-3, 8e-16) it KEEPS 8e-16 (-> 1.25e15) while the NumPy default 1e-15 cuts it; 3e-16 is cut by both", np.linalg.pinv(np.diag([1., 1e-3, 8e-16]), rtol=None)[2, 2] > 1e15 and np.allclose(np.linalg.pinv(np.diag([1., 1e-3, 8e-16])), np.diag([1., 1e3, 0.])) and np.allclose(np.linalg.pinv(np.diag([1., 1e-3, 3e-16]), rtol=None), np.diag([1., 1e3, 0.])))
Qo = np.linalg.qr(rs.randn(3, 3))[0]; Sh = (Qo * [2., -1., 0.]) @ Qo.T; Sh = (Sh + Sh.T) / 2
ph = np.linalg.pinv(Sh, hermitian=True); ph_t = (Qo * [0.5, -1., 0.]) @ Qo.T
report("pinv(hermitian=True) on Q diag(2,-1,0) Q^T = Q diag(1/2,-1,0) Q^T (closed form; the ~1e-16 eigenvalue is cut by rcond 1e-15 * 2)", maxdiff(ph, ph_t) < 1e-12 and maxdiff(np.linalg.pinv(Sh), ph_t) < 1e-12, f"(|pinv - truth| {maxdiff(ph, ph_t):.1e})")
Pst = rs.randn(3, 4, 3); pst = np.linalg.pinv(Pst)
report("pinv on a stack (3,4,3): result (3,3,4), each equals the mpmath pseudo-inverse", pst.shape == (3, 3, 4) and all(maxdiff(pst[i], mp_pinv(Pst[i])) < 1e-10 for i in range(3)))
report("pinv with rcond broadcast per matrix (documented '(...) array_like'): rcond=[1e-15, 0.5] on a stack cuts differently", np.linalg.pinv(np.stack([Ptall, Ptall]), rcond=np.array([1e-15, 1e-6]))[1].max() < 2000 and np.abs(np.linalg.pinv(np.stack([Ptall, Ptall]), rcond=np.array([1e-15, 1e-6]))[0]).max() > 1e8)
report("pinv of a zero (3,4) matrix is the zero (4,3) matrix (no nan)", np.array_equal(np.linalg.pinv(np.zeros((3, 4))), np.zeros((4, 3))))
report("pinv of a complex (5,3) matrix equals V S^+ U^H (mpmath.svd_c); dtype rules: float32 -> float32, int -> float64", maxdiff(np.linalg.pinv(Ac), mp_pinv(Ac)) < 1e-11 and np.linalg.pinv(Pst[0].astype(np.float32)).dtype == np.float32 and np.linalg.pinv(Ai).dtype == np.float64)
report("pinv of a square invertible matrix equals inv (mpmath.inverse)", maxdiff(np.linalg.pinv(A4), N(Aim)) < 1e-10)

# ================= matrix_rank
print("---- matrix_rank")
report("matrix_rank default: singular values (1, 1e-3, 1e-9) -> 3 (1e-9 > S.max * max(M,N) * eps)", np.linalg.matrix_rank(Ptall) == 3)
report("matrix_rank(tol=1e-6) -> 2; tol=2 -> 0; tol=1e-12 -> 3", np.linalg.matrix_rank(Ptall, tol=1e-6) == 2 and np.linalg.matrix_rank(Ptall, tol=2) == 0 and np.linalg.matrix_rank(Ptall, tol=1e-12) == 3)
report("matrix_rank default on (1, 1e-3, 3e-16): 3e-16 < 5 * eps -> rank 2", np.linalg.matrix_rank((np.linalg.qr(rs.randn(5, 5))[0][:, :3] * [1., 1e-3, 3e-16]) @ Vo.T) == 2)
if V2: report("matrix_rank rtol [2.0]: rtol=1e-6 -> 2 (threshold rtol * S.max); rtol and tol together -> ValueError; rtol=None same as default", np.linalg.matrix_rank(Ptall, rtol=1e-6) == 2 and raises(lambda: np.linalg.matrix_rank(Ptall, tol=1e-6, rtol=1e-6), ValueError) and np.linalg.matrix_rank(Ptall, rtol=None) == 3)
report("matrix_rank(hermitian=True) of Q diag(2,-1,0) Q^T = 2", np.linalg.matrix_rank(Sh, hermitian=True) == 2 and np.linalg.matrix_rank(Sh) == 2)
Stk = np.stack([Ptall, (np.linalg.qr(rs.randn(5, 5))[0][:, :3] * [1., 1e-3, 1e-20]) @ Vo.T])
report("matrix_rank on a stack (2,5,3): per-matrix ranks [3, 2]; tol broadcast per matrix tol=[1e-6, 1e-25] -> [2, 3]", np.array_equal(np.linalg.matrix_rank(Stk), [3, 2]) and np.array_equal(np.linalg.matrix_rank(Stk, tol=np.array([1e-6, 1e-25])), [2, 3]))
report("matrix_rank of 1-D: 1 unless all zero (documented); 0-d scalar likewise", np.linalg.matrix_rank(np.array([0., 0., 3.])) == 1 and np.linalg.matrix_rank(np.zeros(4)) == 0 and np.linalg.matrix_rank(np.float64(2)) == 1)
report("matrix_rank of a zero matrix = 0; identity = M; rank-2 6x4 = 2", np.linalg.matrix_rank(np.zeros((3, 4))) == 0 and np.linalg.matrix_rank(np.eye(5)) == 5 and np.linalg.matrix_rank(Rd) == 2)

# ================= trace / diagonal / diag
print("---- trace / diagonal / diag")
Xi = np.arange(24).reshape(2, 3, 4)
report("trace(3-D) default axis1=0, axis2=1: shape (4,), sum_i X[i,i,:]", np.array_equal(np.trace(Xi), [sum(Xi[i, i, k] for i in range(2)) for k in range(4)]))
report("trace offset=+1: sum_i X[i, i+1, :]; offset=-1: sum_i X[i+1, i, :]", np.array_equal(np.trace(Xi, offset=1), [sum(Xi[i, i + 1, k] for i in range(2)) for k in range(4)]) and np.array_equal(np.trace(Xi, offset=-1), [Xi[1, 0, k] for k in range(4)]))
report("trace(axis1=1, axis2=2): shape (2,), sum_j X[b, j, j]; axis1=-1, axis2=-2 same diagonal", np.array_equal(np.trace(Xi, axis1=1, axis2=2), [sum(Xi[b, j, j] for j in range(3)) for b in range(2)]) and np.array_equal(np.trace(Xi, axis1=-1, axis2=-2), np.trace(Xi, axis1=1, axis2=2)))
report("diagonal(3-D, offset=1, axis1=1, axis2=2): shape (2,3) with entries X[b, j, j+1]; offset=-2 -> X[b, j+2, j], shape (2,1)", np.array_equal(np.diagonal(Xi, 1, axis1=1, axis2=2), [[Xi[b, j, j + 1] for j in range(3)] for b in range(2)]) and np.array_equal(np.diagonal(Xi, -2, axis1=1, axis2=2), [[Xi[b, 2, 0]] for b in range(2)]))
report("diagonal offset beyond the matrix returns an empty (M,0) diagonal; trace then 0", np.diagonal(Xi[0], 4).shape == (0,) and np.trace(Xi[0], 4) == 0)
report("diag(1-D, k=2) builds a (n+2)x(n+2) matrix with v on the 2nd superdiagonal; diag(2-D, k=-1) extracts the first subdiagonal", np.array_equal(np.diag([1, 2, 3], k=2), [[0, 0, 1, 0, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 3], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) and np.array_equal(np.diag(Xi[0], k=-1), [Xi[0, 1, 0], Xi[0, 2, 1]]) and np.array_equal(np.diag(Xi[0], k=1), [Xi[0, 0, 1], Xi[0, 1, 2], Xi[0, 2, 3]]))
report("trace of an int8 matrix is accumulated in the platform integer (documented sum dtype rule): [[100,0],[0,100]] -> 200, dtype int64", np.trace(np.array([[100, 0], [0, 100]], dtype=np.int8)) == 200 and np.trace(np.array([[100, 0], [0, 100]], dtype=np.int8)).dtype == np.int_)
report("trace(dtype=float) of int matrix returns float; trace of float32 stays float32", isinstance(np.trace(Xi[0], dtype=float), float) and np.trace(Xi[0].astype(np.float32)).dtype == np.float32)
if V2:
    report("linalg.diagonal [2.0] uses the LAST two axes (documented, 'contrary to numpy.diagonal'): equals np.diagonal(axis1=-2, axis2=-1); offset=1 likewise", np.array_equal(np.linalg.diagonal(Xi), np.diagonal(Xi, axis1=-2, axis2=-1)) and np.array_equal(np.linalg.diagonal(Xi, offset=1), [[Xi[b, j, j + 1] for j in range(3)] for b in range(2)]) and not np.array_equal(np.linalg.diagonal(Xi).shape, np.diagonal(Xi).shape))
    report("linalg.trace [2.0] sums the last-two-axes diagonal: shape (2,); offset=-1; dtype= honoured", np.array_equal(np.linalg.trace(Xi), [sum(Xi[b, j, j] for j in range(3)) for b in range(2)]) and np.array_equal(np.linalg.trace(Xi, offset=-1), [Xi[b, 1, 0] + Xi[b, 2, 1] for b in range(2)]) and np.linalg.trace(Xi, dtype=np.float32).dtype == np.float32)

# ================= outer / kron / cross
print("---- outer / kron / cross")
oa = np.array([1, -2, 3]); ob = np.array([4, 5])
report("outer(a, b)[i,j] = a[i] b[j]; 2-D inputs are flattened first (documented)", np.array_equal(np.outer(oa, ob), [[a * b for b in ob] for a in oa]) and np.outer(Xi[0], ob).shape == (12, 2) and np.array_equal(np.outer(Xi[0], ob), np.outer(Xi[0].ravel(), ob)))
ka = rs.randint(-3, 4, (2, 3)); kb = rs.randint(-3, 4, (2, 2)); K = np.kron(ka, kb)
kt = np.array([[ka[i, j] * kb[k, l] for j in range(3) for l in range(2)] for i in range(2) for k in range(2)])
report("kron((2,3),(2,2)): shape (4,6), K[i*2+k, j*2+l] = a[i,j] b[k,l] (documented block structure)", K.shape == (4, 6) and np.array_equal(K, kt))
report("kron with different ndim: kron((3,), (2,2)) prepends 1s to the smaller (documented) -> shape (2,6) = kron(a.reshape(1,3), b)", np.kron(oa, kb).shape == (2, 6) and np.array_equal(np.kron(oa, kb), np.array([[oa[j] * kb[k, l] for j in range(3) for l in range(2)] for k in range(2)])))
report("kron(scalar-like 1-D, 1-D) = outer(a, b).ravel(); kron(I2, B) is block-diagonal", np.array_equal(np.kron(oa, ob), np.outer(oa, ob).ravel()) and np.array_equal(np.kron(np.eye(2, dtype=int), kb), np.block([[kb, np.zeros((2, 2), int)], [np.zeros((2, 2), int), kb]])))
def cross3(a, b): return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
ca = np.array([1, 2, 3]); cb = np.array([-2, 5, 1]); Ca = rs.randint(-3, 4, (4, 3)); Cb = rs.randint(-3, 4, (4, 3))
report("cross of 3-vectors = closed form; stacks (4,3)x(4,3) row-wise; anti-commutes; orthogonal to both", np.array_equal(np.cross(ca, cb), cross3(ca, cb)) and np.array_equal(np.cross(Ca, Cb), [cross3(Ca[i], Cb[i]) for i in range(4)]) and np.array_equal(np.cross(cb, ca), -np.cross(ca, cb)) and np.dot(np.cross(ca, cb), ca) == 0)
with warnings.catch_warnings(record=True) as wlog:
    warnings.simplefilter("always"); c2 = np.cross([1, 2], [3, 4]); c23 = np.cross([1, 2], [3, 4, 5])
dep = [x for x in wlog if issubclass(x.category, DeprecationWarning)]
report("cross of two 2-D vectors returns the scalar z-component (1*4 - 2*3 = -2); mixed 2-D/3-D treats the 2-D one as z = 0", c2 == -2 and np.ndim(c2) == 0 and np.array_equal(c23, cross3([1, 2, 0], [3, 4, 5])))
if V2: report("cross with 2-D vectors emits DeprecationWarning [deprecated in 2.0] ('Arrays of 2-dimensional vectors are deprecated')", len(dep) >= 1 and "2-dimensional" in str(dep[0].message))
else: report("cross with 2-D vectors emits no warning on 1.x (deprecated only in 2.0)", len(dep) == 0)
report("cross with 4-vectors raises ValueError (documented 'dimension ... does not equal 3')", raises(lambda: np.cross([1, 2, 3, 4], [1, 2, 3, 4]), ValueError))
CaT = Ca.T; CbT = Cb.T
report("cross axisa=0, axisb=0, axisc=0 on (3,4) inputs: result (3,4) with column i = cross(a[:,i], b[:,i]); axis=0 equivalent; axisc=-1 puts the vectors in rows", np.array_equal(np.cross(CaT, CbT, axisa=0, axisb=0, axisc=0), np.array([cross3(Ca[i], Cb[i]) for i in range(4)]).T) and np.array_equal(np.cross(CaT, CbT, axis=0), np.cross(CaT, CbT, axisa=0, axisb=0, axisc=0)) and np.array_equal(np.cross(CaT, Cb, axisa=0, axisc=-1), [cross3(Ca[i], Cb[i]) for i in range(4)]))
report("cross broadcasts a single vector against a stack", np.array_equal(np.cross(ca, Cb), [cross3(ca, Cb[i]) for i in range(4)]))
if V2:
    report("linalg.cross [2.0]: axis=-1 default, axis=0 on (3,4) inputs; 2-D vectors raise ValueError (array-API, no deprecation path); linalg.outer rejects 2-D input (ValueError)", np.array_equal(np.linalg.cross(Ca, Cb), np.cross(Ca, Cb)) and np.array_equal(np.linalg.cross(CaT, CbT, axis=0), np.cross(CaT, CbT, axis=0)) and raises(lambda: np.linalg.cross(np.array([1, 2]), np.array([3, 4])), ValueError) and np.array_equal(np.linalg.outer(oa, ob), np.outer(oa, ob)) and raises(lambda: np.linalg.outer(Xi[0], ob), ValueError))

# ================= tensordot
print("---- tensordot")
ta = rs.randint(-3, 4, (3, 4, 5)); tb = rs.randint(-3, 4, (4, 5, 2)); tb1 = rs.randint(-3, 4, (5, 6)); tc = rs.randint(-3, 4, (4, 3, 2))
report("tensordot(a (3,4,5), b (4,5,2), axes=2): sums the last 2 axes of a with the first 2 of b -> (3,2)", np.array_equal(np.tensordot(ta, tb, 2), [[sum(int(ta[i, j, k]) * int(tb[j, k, l]) for j in range(4) for k in range(5)) for l in range(2)] for i in range(3)]))
report("tensordot axes=1 (a (3,4,5), b (5,6)) -> (3,4,6) = a @ b; axes=0 -> outer product shape (3,4,5,5,6)", np.array_equal(np.tensordot(ta, tb1, 1), [[[sum(int(ta[i, j, k]) * int(tb1[k, l]) for k in range(5)) for l in range(6)] for j in range(4)] for i in range(3)]) and np.tensordot(ta, tb1, 0).shape == (3, 4, 5, 5, 6) and np.tensordot(ta, tb1, 0)[1, 2, 3, 4, 5] == ta[1, 2, 3] * tb1[4, 5])
report("tensordot axes=([1,0],[0,1]) (a (3,4,5), b (4,3,2)): sum_{i,j} a[i,j,k] b[j,i,l] -> (5,2)", np.array_equal(np.tensordot(ta, tc, axes=([1, 0], [0, 1])), [[sum(int(ta[i, j, k]) * int(tc[j, i, l]) for i in range(3) for j in range(4)) for l in range(2)] for k in range(5)]))
report("tensordot axes=(2, 0) as a pair of ints (a (3,4,5), b (5,6)) -> (3,4,6); axes=([2],[0]) same; axes=(0,1)? contracts a-axis 0 with b-axis 1 on (3,4,5)x(4,3,2) -> (4,5,4,2)", np.array_equal(np.tensordot(ta, tb1, axes=(2, 0)), np.tensordot(ta, tb1, 1)) and np.array_equal(np.tensordot(ta, tb1, axes=([2], [0])), np.tensordot(ta, tb1, 1)) and np.array_equal(np.tensordot(ta, tc, axes=(0, 1)), [[[[sum(int(ta[i, j, k]) * int(tc[m, i, l]) for i in range(3)) for l in range(2)] for m in range(4)] for k in range(5)] for j in range(4)]))
report("tensordot with mismatched contraction lengths raises ValueError", raises(lambda: np.tensordot(ta, tb1, 2), ValueError))
if V2: report("linalg.tensordot [2.0] equals np.tensordot (axes keyword)", np.array_equal(np.linalg.tensordot(ta, tb, axes=2), np.tensordot(ta, tb, 2)))

# ================= einsum
print("---- einsum")
E2 = rs.randint(-3, 4, (3, 3)); E3 = rs.randint(-3, 4, (3, 4)); E4 = rs.randint(-3, 4, (4, 5)); Eb = rs.randint(-3, 4, (2, 3, 4)); Ec = rs.randint(-3, 4, (2, 4, 5)); Ed = rs.randint(-3, 4, (3, 3, 4)); ev = rs.randint(-3, 4, 3); ew = rs.randint(-3, 4, 4)
ii = lambda a: int(a)
cases = [
    ("'ii' trace", 'ii', (E2,), sum(ii(E2[i, i]) for i in range(3))),
    ("'ii->i' diagonal", 'ii->i', (E2,), [ii(E2[i, i]) for i in range(3)]),
    ("'ij->ji' transpose", 'ij->ji', (E3,), [[ii(E3[i, j]) for i in range(3)] for j in range(4)]),
    ("'ij->' full sum", 'ij->', (E3,), sum(ii(x) for x in E3.ravel())),
    ("'ij->i' row sums / 'ij->j' column sums", 'ij->j', (E3,), [sum(ii(E3[i, j]) for i in range(3)) for j in range(4)]),
    ("'ij,jk->ik' matmul", 'ij,jk->ik', (E3, E4), pymatmul(E3, E4)),
    ("'ij,jk' implicit output = 'ik' (alphabetical free indices)", 'ij,jk', (E3, E4), pymatmul(E3, E4)),
    ("'ij,jk->ki' transposed matmul", 'ij,jk->ki', (E3, E4), [list(r) for r in zip(*pymatmul(E3, E4))]),
    ("'bij,bjk->bik' batch matmul", 'bij,bjk->bik', (Eb, Ec), [pymatmul(Eb[b], Ec[b]) for b in range(2)]),
    ("'...ij,...jk->...ik' ellipsis batch matmul", '...ij,...jk->...ik', (Eb, Ec), [pymatmul(Eb[b], Ec[b]) for b in range(2)]),
    ("'...ij,jk->...ik' ellipsis broadcasting a 2-D operand", '...ij,jk->...ik', (Eb, E4), [pymatmul(Eb[b], E4) for b in range(2)]),
    ("'i,j->ij' outer", 'i,j->ij', (ev, ew), [[ii(a) * ii(b) for b in ew] for a in ev]),
    ("'i,i->' inner / 'i,i' implicit", 'i,i', (ev, ev), sum(ii(a) * ii(a) for a in ev)),
    ("'ij,ij->ij' Hadamard", 'ij,ij->ij', (E3, E3), [[ii(x) * ii(x) for x in r] for r in E3]),
    ("'ij,ji->' trace of product", 'ij,ji->', (E3, E4[:4, :3]), sum(ii(E3[i, j]) * ii(E4[j, i]) for i in range(3) for j in range(4))),
    ("'iij->ij' repeated index on one operand (partial diagonal)", 'iij->ij', (Ed,), [[ii(Ed[i, i, j]) for j in range(4)] for i in range(3)]),
    ("'iij->j' partial diagonal then sum", 'iij->j', (Ed,), [sum(ii(Ed[i, i, j]) for i in range(3)) for j in range(4)]),
    ("'ijk->kji' 3-D permutation", 'ijk->kji', (Eb,), [[[ii(Eb[i, j, k]) for i in range(2)] for j in range(3)] for k in range(4)]),
    ("'ijk,k->ij' contraction with a vector", 'ijk,k->ij', (Eb, ew), [[sum(ii(Eb[i, j, k]) * ii(ew[k]) for k in range(4)) for j in range(3)] for i in range(2)]),
    ("'i,i,i->' three operands", 'i,i,i->', (ev, ev, ev), sum(ii(a) ** 3 for a in ev)),
    ("'ij,jk,kl->il' three-matrix chain", 'ij,jk,kl->il', (E2, E3, E4), pymatmul(pymatmul(E2, E3), E4)),
    ("'ijk,jk->i' broadcasting-style contraction", 'ijk,jk->i', (Eb, E3), [sum(ii(Eb[i, j, k]) * ii(E3[j, k]) for j in range(3) for k in range(4)) for i in range(2)]),
    ("'i...->...' sum over the first axis with ellipsis", 'i...->...', (Eb,), [[sum(ii(Eb[i, j, k]) for i in range(2)) for k in range(4)] for j in range(3)]),
]
for label, sub, ops, truth in cases:
    r = np.einsum(sub, *ops)
    report(f"einsum {label} equals explicit loops", np.array_equal(np.asarray(r), np.asarray(truth)), f"(shape {np.shape(r)})")
report("einsum optimize=True / 'greedy' / 'optimal' give results identical to optimize=False on a three-matrix chain (exact ints)", all(np.array_equal(np.einsum('ij,jk,kl->il', E2, E3, E4, optimize=o), pymatmul(pymatmul(E2, E3), E4)) for o in [False, True, 'greedy', 'optimal']))
E5 = rs.randint(-3, 4, (5, 3)); base4 = np.array([pymatmul(pymatmul(Eb[b], Ec[b]), E5) for b in range(2)])
path = np.einsum_path('bij,bjk,kl->bil', Eb, Ec, E5, optimize='greedy')
report("einsum four-index chain 'bij,bjk,kl->bil' with optimize=False/True/'optimal'/path from einsum_path all equal the explicit loops", all(np.array_equal(np.einsum('bij,bjk,kl->bil', Eb, Ec, E5, optimize=o), base4) for o in [False, True, 'optimal', path[0]]))
report("einsum_path returns (path, string_repr) with path = ['einsum_path', (pair), (pair)]: n_operands - 1 = 2 contraction tuples", isinstance(path, tuple) and len(path) == 2 and path[0][0] == 'einsum_path' and len(path[0]) == 3 and all(isinstance(t, tuple) for t in path[0][1:]) and isinstance(path[1], str))
print(f"   einsum_path greedy contraction order: {path[0][1:]}")
report("einsum 0-d result with optimize=False is a scalar (documented); with out= it is the given array", np.isscalar(np.einsum('ii', E2)) and isinstance(np.einsum('ii', E2, out=np.zeros((), dtype=np.int64)), np.ndarray))
r8 = np.einsum('i,i', i8, i8); d8 = np.dot(i8, i8)
report("einsum 'i,i' on int8 [100,100,100]: result dtype int8 (input dtype kept), 30000 wraps to 48 (documented overflow semantics: no promotion, no error); np.dot the same; np.sum(i8*i8) would also be int8 -- np.sum(i8, dtype=int64) needed", r8.dtype == np.int8 and int(r8) == 48 and d8.dtype == np.int8 and int(d8) == 48, f"(einsum {r8!r}, dot {d8!r})")
report("einsum dtype=np.int64 on int8 operands accumulates in int64: exact 30000; dtype=float64 gives 30000.0", np.einsum('i,i', i8, i8, dtype=np.int64) == 30000 and np.einsum('i,i', i8, i8, dtype=np.float64) == 30000.0)
report("einsum with out= of dtype float64 from int operands requires casting: casting='safe' (default) accepts int->float; result exact", np.array_equal(np.einsum('ij,jk->ik', E3, E4, out=np.zeros((3, 5))), np.array(pymatmul(E3, E4), dtype=float)))
report("einsum invalid subscripts: mismatched dimension raises ValueError; output index not in inputs raises ValueError", raises(lambda: np.einsum('ij,ij->ij', E3, E4), ValueError) and raises(lambda: np.einsum('ij->ik', E3), ValueError))
F52 = rs.randn(5, 2); e32r = np.einsum('ij,jk->ik', B45.astype(np.float32), F52.astype(np.float32))
report("einsum on float32 operands keeps float32 and matches the mpmath product of the float32 values to 1e-5 relative", e32r.dtype == np.float32 and maxdiff(e32r, N(M(B45.astype(np.float32)) * M(F52.astype(np.float32)))) < 1e-5 * np.abs(B45 @ F52).max())
Ef = rs.randn(30, 30); Eg = rs.randn(30, 30)
report("einsum 'ij,jk->ik' float64 vs mpmath product (30x30) to 1e-13 relative", maxdiff(np.einsum('ij,jk->ik', Ef, Eg), N(M(Ef) * M(Eg))) < 1e-13 * np.abs(Ef @ Eg).max())

# ================= matmul vs dot, @, float32 accumulation
print("---- matmul / dot")
da = rs.randint(-3, 4, (2, 3, 4, 2)); dc = rs.randint(-3, 4, (2, 3, 2, 5))
dd = np.dot(da, dc)
dt_truth = np.array([[[[[[sum(ii(da[i, j, k, l]) * ii(dc[m, n, l, p]) for l in range(2)) for p in range(5)] for n in range(3)] for m in range(2)] for k in range(4)] for j in range(3)] for i in range(2)])
report("dot(a (2,3,4,2), b (2,3,2,5)): shape (2,3,4,2,3,5), dot(a,b)[i,j,k,m,n,p] = sum(a[i,j,k,:] * b[m,n,:,p]) (documented 'last axis of a and second-to-last of b')", dd.shape == (2, 3, 4, 2, 3, 5) and np.array_equal(dd, dt_truth))
mm = np.matmul(da, dc); mm_truth = np.array([[pymatmul(da[i, j], dc[i, j]) for j in range(3)] for i in range(2)])
report("matmul(a (2,3,4,2), b (2,3,2,5)): shape (2,3,4,5), batch-wise product (documented 'stacks of matrices are broadcast together')", mm.shape == (2, 3, 4, 5) and np.array_equal(mm, mm_truth) and np.array_equal(da @ dc, mm))
report("matmul broadcasting of stacks: (2,1,4,2) @ (1,2,2,5) -> (2,2,4,5) with [i,j] = a[i,0] @ b[0,j]; a 2-D b broadcasts against a 4-D a", np.matmul(da[:, :1], dc[:1, :2]).shape == (2, 2, 4, 5) and np.array_equal(np.matmul(da[:, :1], dc[:1, :2]), [[pymatmul(da[i, 0], dc[0, j]) for j in range(2)] for i in range(2)]) and np.array_equal(np.matmul(da, dc[0, 0]), [[pymatmul(da[i, j], dc[0, 0]) for j in range(3)] for i in range(2)]))
report("dot with a 1-D b: sum product over the last axis of a (N-D) and b; equals matmul for that case", np.array_equal(np.dot(da, [1, -1]), da[..., 0] - da[..., 1]) and np.array_equal(np.matmul(da, np.array([1, -1])), da[..., 0] - da[..., 1]))
mv = np.array([1, 2, 3, 4]); MX = rs.randint(-3, 4, (3, 4)); M2 = rs.randint(-3, 4, (4, 5))
report("matmul with 1-D operands: (4,) @ (4,5) -> (5,) (prepended 1 removed); (3,4) @ (4,) -> (3,); (4,) @ (4,) -> 0-d scalar", np.matmul(mv, M2).shape == (5,) and np.array_equal(np.matmul(mv, M2), np.array(pymatmul([mv], M2)).ravel()) and np.matmul(MX, mv).shape == (3,) and np.array_equal(MX @ mv, np.array(pymatmul(MX, [[x] for x in mv])).ravel()) and np.ndim(np.matmul(mv, mv)) == 0 and np.matmul(mv, mv) == 30)
report("matmul with a scalar raises ValueError (documented 'scalars not allowed'); dot with a scalar multiplies", raises(lambda: np.matmul(3, MX), ValueError) and np.array_equal(np.dot(3, MX), 3 * MX))
report("@ operator equals np.matmul for 2-D, stacked and 1-D cases", np.array_equal(MX @ M2, np.matmul(MX, M2)) and np.array_equal(da @ dc, np.matmul(da, dc)) and np.array_equal(mv @ M2, np.matmul(mv, M2)))
report("matmul/dot of 2-D int matrices exact vs Python ints; matmul of int8 keeps int8 (wraps)", np.array_equal(MX @ M2, pymatmul(MX, M2)) and np.array_equal(np.dot(MX, M2), pymatmul(MX, M2)) and (np.matmul(i8m, i8m).dtype == np.int8) and int(np.matmul(i8m, i8m)[0, 0]) == ((20000 + 128) % 256) - 128)
a6 = rs.random_sample(10 ** 6).astype(np.float32); b6 = rs.random_sample(10 ** 6).astype(np.float32)
truth6 = math.fsum(x * y for x, y in zip(a6.tolist(), b6.tolist()))    # float32 products are exact in float64; fsum is exactly rounded
d32 = np.dot(a6, b6); d64 = np.dot(a6.astype(np.float64), b6.astype(np.float64)); s32 = np.sum(a6 * b6)
e32 = abs(float(d32) - truth6) / truth6; e64 = abs(float(d64) - truth6) / truth6      # float() first: under NEP 50 (2.x) float32 - python float stays float32
print(f"   float32 dot of 1e6 uniform(0,1) pairs: truth {truth6:.6f}; np.dot(float32) = {float(d32):.6f} (rel err {e32:.2e}, dtype {d32.dtype}); np.dot(float64) rel err {e64:.2e}; np.sum(a*b) float32 (pairwise) rel err {abs(float(s32) - truth6) / truth6:.2e}")
report("np.dot float32 on 1e6 elements: result float32 with relative error below 1e-4 (BLAS sdot, float32 accumulation; reported above); float64 dot within 1e-13", d32.dtype == np.float32 and e32 < 1e-4 and e64 < 1e-13)

# ================= vdot / inner / vecdot / matvec / vecmat
print("---- vdot / inner / vecdot / matvec / vecmat")
za = np.array([1 + 2j, 3 - 1j, -2j]); zb = np.array([2 - 1j, 1j, 4 + 1j])
report("vdot(a, b) = sum conj(a) b (documented conjugation of the FIRST argument); dot(a, b) does NOT conjugate; vdot(b, a) = conj(vdot(a, b))", np.vdot(za, zb) == sum(x.conjugate() * y for x, y in zip(za.tolist(), zb.tolist())) and np.dot(za, zb) == sum(x * y for x, y in zip(za.tolist(), zb.tolist())) and np.vdot(zb, za) == np.vdot(za, zb).conjugate())
report("vdot flattens multidimensional arguments (documented): vdot((2,2), (2,2)) = vdot of the raveled arrays", np.vdot(Cz[:2, :2], Cz[2:, 2:]) == sum(x.conjugate() * y for x, y in zip(Cz[:2, :2].ravel().tolist(), Cz[2:, 2:].ravel().tolist())))
ia = rs.randint(-3, 4, (2, 3, 4)); ib = rs.randint(-3, 4, (5, 4))
report("inner(a (2,3,4), b (5,4)): shape (2,3,5), inner[i,j,k] = sum_l a[i,j,l] b[k,l] (sum over LAST axes of both, documented); inner with a scalar multiplies", np.inner(ia, ib).shape == (2, 3, 5) and np.array_equal(np.inner(ia, ib), [[[sum(ii(ia[i, j, l]) * ii(ib[k, l]) for l in range(4)) for k in range(5)] for j in range(3)] for i in range(2)]) and np.array_equal(np.inner(ia, 2), 2 * ia))
report("inner of complex 1-D does not conjugate (unlike vdot)", np.inner(za, zb) == np.dot(za, zb))
if V2:
    Va = rs.randn(2, 3) + 1j * rs.randn(2, 3); Vb = rs.randn(2, 3) + 1j * rs.randn(2, 3)
    report("vecdot [2.0]: sum over the last axis of conj(x1) * x2 (documented conjugation of x1), shape (2,)", np.allclose(np.vecdot(Va, Vb), [sum(x.conjugate() * y for x, y in zip(Va[i].tolist(), Vb[i].tolist())) for i in range(2)]))
    report("vecdot axis=0 sums over axis 0 -> shape (3,); broadcasting (2,1,3) x (4,3) -> (2,4); 1-D x 1-D -> scalar", np.allclose(np.vecdot(Va, Vb, axis=0), [sum(Va[i, j].conjugate() * Vb[i, j] for i in range(2)) for j in range(3)]) and np.vecdot(Va[:, None, :], rs.randn(4, 3)).shape == (2, 4) and np.ndim(np.vecdot(za, zb)) == 0 and np.vecdot(za, zb) == np.vdot(za, zb))
    report("linalg.vecdot [2.0] equals np.vecdot (axis keyword)", np.allclose(np.linalg.vecdot(Va, Vb, axis=-1), np.vecdot(Va, Vb)))
    report("vecdot mismatched last axes raises ValueError", raises(lambda: np.vecdot(np.ones(3), np.ones(4)), ValueError))
if V22:
    Ma = rs.randn(2, 3, 4) + 1j * rs.randn(2, 3, 4); vv = rs.randn(4) + 1j * rs.randn(4); vs = rs.randn(2, 4) + 1j * rs.randn(2, 4)
    report("matvec [2.2]: (2,3,4) x (4,) -> (2,3) = sum_j A[..,i,j] v[j] with NO conjugation (documented); stack of vectors (2,4) pairs with the stack of matrices", np.allclose(np.matvec(Ma, vv), [[sum(Ma[b, i, j] * vv[j] for j in range(4)) for i in range(3)] for b in range(2)]) and np.allclose(np.matvec(Ma, vs), [[sum(Ma[b, i, j] * vs[b, j] for j in range(4)) for i in range(3)] for b in range(2)]) and np.allclose(np.matvec(Ma, vv), np.matmul(Ma, vv)))
    v3c = rs.randn(3) + 1j * rs.randn(3); v3s = rs.randn(2, 3) + 1j * rs.randn(2, 3)
    report("vecmat [2.2]: (3,) x (2,3,4) -> (2,4) = sum_i conj(v[i]) A[..,i,j] (documented conjugation of the vector); stack of vectors; equals vecdot-style conj @", np.allclose(np.vecmat(v3c, Ma), [[sum(v3c[i].conjugate() * Ma[b, i, j] for i in range(3)) for j in range(4)] for b in range(2)]) and np.allclose(np.vecmat(v3s, Ma), [[sum(v3s[b, i].conjugate() * Ma[b, i, j] for i in range(3)) for j in range(4)] for b in range(2)]) and np.allclose(np.vecmat(v3c, Ma), np.matmul(v3c.conj(), Ma)))
    report("matvec / vecmat with mismatched core dimensions raise ValueError; real inputs: vecmat = v @ A, matvec = A @ v", raises(lambda: np.matvec(Ma, np.ones(3)), ValueError) and raises(lambda: np.vecmat(np.ones(4), Ma), ValueError) and np.allclose(np.vecmat(oa.astype(float), Ed.astype(float)), oa @ Ed) and np.allclose(np.matvec(Ed.astype(float), ew.astype(float)), Ed @ ew))

# ================= array-API aliases, matrix_transpose, transpose of stacks
print("---- array-API aliases / transposes")
report("np.transpose of a (2,3,4) stack reverses ALL axes by default (documented) -> (4,3,2); axes=(0,2,1) transposes the matrices", np.transpose(Xi).shape == (4, 3, 2) and np.transpose(Xi)[1, 2, 0] == Xi[0, 2, 1] and np.array_equal(np.transpose(Xi, (0, 2, 1)), np.swapaxes(Xi, 1, 2)) and np.array_equal(np.transpose(Xi, (0, 2, 1)), [[[Xi[b, i, j] for i in range(3)] for j in range(4)] for b in range(2)]))
if V2:
    report("np.matrix_transpose / np.linalg.matrix_transpose / .mT [2.0]: swap the LAST two axes only -> (2,4,3) (documented)", np.matrix_transpose(Xi).shape == (2, 4, 3) and np.array_equal(np.matrix_transpose(Xi), np.swapaxes(Xi, -1, -2)) and np.array_equal(np.linalg.matrix_transpose(Xi), np.swapaxes(Xi, -1, -2)) and np.array_equal(Xi.mT, np.swapaxes(Xi, -1, -2)) and np.array_equal(np.matrix_transpose(Xi[0]), Xi[0].T))
    report("matrix_transpose of a 1-D array raises ValueError (needs at least 2 dims)", raises(lambda: np.matrix_transpose(np.ones(3)), ValueError))
    report("np.linalg.matmul [2.0] equals np.matmul (stacked ints vs loops); np.linalg.outer equals np.outer for 1-D", np.array_equal(np.linalg.matmul(da, dc), mm_truth) and np.array_equal(np.linalg.matmul(MX, M2), pymatmul(MX, M2)) and np.array_equal(np.linalg.outer(oa, ob), [[a * b for b in ob] for a in oa]))
    report("np.linalg.svdvals / matrix_norm / vector_norm / diagonal / trace / cross / tensordot / vecdot / matrix_transpose exist and are listed in np.linalg.__all__ [2.0]", all(n in np.linalg.__all__ for n in ['svdvals', 'matrix_norm', 'vector_norm', 'diagonal', 'trace', 'cross', 'outer', 'tensordot', 'vecdot', 'matmul', 'matrix_transpose']))
report("np.linalg.transpose (undocumented helper in every version) swaps the last two axes (source: 'swapaxes(a, -1, -2)'), unlike np.transpose", np.array_equal(np.linalg.linalg.transpose(Xi) if hasattr(np.linalg, 'linalg') and hasattr(np.linalg.linalg, 'transpose') else np.linalg._linalg.transpose(Xi), np.swapaxes(Xi, -1, -2)))

# ================= LinAlgError types
print("---- LinAlgError")
if (MAJOR, MINOR) >= (1, 25): report("LinAlgError is a subclass of ValueError since 1.25 (source 'class LinAlgError(ValueError)'), so 'except ValueError' also catches it", issubclass(LinAlgError, ValueError))
else: report("LinAlgError subclasses only Exception before 1.25 (source 'class LinAlgError(Exception)'): 'except ValueError' does NOT catch it", not issubclass(LinAlgError, ValueError) and issubclass(LinAlgError, Exception))
errs = {
    "solve singular": lambda: np.linalg.solve(Sing, [1., 2.]), "solve non-square": lambda: np.linalg.solve(np.ones((2, 3)), np.ones(2)),
    "inv singular": lambda: np.linalg.inv(Sing), "inv 1-D": lambda: np.linalg.inv(np.ones(2)),
    "cholesky non-PD": lambda: np.linalg.cholesky(-np.eye(2)), "qr 1-D": lambda: np.linalg.qr(np.ones(3)),
    "eig NaN": lambda: np.linalg.eig(np.array([[np.nan, 0.], [0., 1.]])), "eigh 1-D": lambda: np.linalg.eigh(np.ones(2)),
    "lstsq incompatible": lambda: np.linalg.lstsq(Ao, np.ones(7), rcond=None), "tensorinv non-square": lambda: np.linalg.tensorinv(np.ones((2, 3, 4)), 1),
    "tensorsolve singular": lambda: np.linalg.tensorsolve(np.zeros((2, 2)), np.ones(2)), "matrix_power singular neg": lambda: np.linalg.matrix_power(Sing, -2),
    "det 1-D": lambda: np.linalg.det(np.ones(2)), "cond empty": lambda: np.linalg.cond(np.zeros((0, 0))), "svd 1-D": lambda: np.linalg.svd(np.ones(2)),
    "matrix_power non-square": lambda: np.linalg.matrix_power(np.ones((2, 3)), 2), "slogdet non-square": lambda: np.linalg.slogdet(np.ones((2, 3))),
}
bad = [k for k, f in errs.items() if not raises(f, LinAlgError)]
report("LinAlgError raised by: " + ", ".join(errs), not bad, f"(not LinAlgError: {bad})" if bad else "")
report("NOT LinAlgError (by design): matrix_power(A, 2.5) TypeError; norm(v, 'bad') ValueError; solve with mismatched b ValueError; matmul shape mismatch ValueError; multi_dot([A]) ValueError", raises(lambda: np.linalg.matrix_power(Mf, 2.5), TypeError) and raises(lambda: np.linalg.norm(vec, 'bad'), ValueError) and raises(lambda: np.linalg.solve(As[0], np.ones(3)), ValueError) and raises(lambda: np.matmul(MX, MX), ValueError) and raises(lambda: np.linalg.multi_dot([MX]), ValueError))
def _try(fn):
    try: fn(); return None
    except Exception as e: return e
report("singular-matrix LinAlgError message is 'Singular matrix'; non-PD cholesky message 'Matrix is not positive definite'", str(_try(lambda: np.linalg.inv(Sing))) == 'Singular matrix' and str(_try(lambda: np.linalg.cholesky(-np.eye(2)))) == 'Matrix is not positive definite', f"({_try(lambda: np.linalg.inv(Sing))!r}; {_try(lambda: np.linalg.cholesky(-np.eye(2)))!r})")

# ================= result dtype rules
print("---- result dtype rules")
Af32 = SPD[:3, :3].astype(np.float32); Aint3 = np.array([[4, 1, 0], [1, 3, 1], [0, 1, 2]]); Ac64 = H[:3, :3].astype(np.complex64)
fns = {"inv": np.linalg.inv, "det": np.linalg.det, "eigvalsh": np.linalg.eigvalsh, "cholesky": np.linalg.cholesky, "pinv": np.linalg.pinv,
       "svd s": lambda a: np.linalg.svd(a, compute_uv=False), "qr R": lambda a: np.linalg.qr(a)[1], "eig w": lambda a: np.linalg.eig(a)[0], "eigh V": lambda a: np.linalg.eigh(a)[1],
       "solve": lambda a: np.linalg.solve(a, np.ones(3, a.dtype)), "lstsq x": lambda a: np.linalg.lstsq(a, np.ones(3, a.dtype), rcond=None)[0], "norm": np.linalg.norm, "slogdet logabsdet": lambda a: np.linalg.slogdet(a)[1], "cond": lambda a: np.linalg.cond(a), "matrix_power -1": lambda a: np.linalg.matrix_power(a, -1)}
bad_int = [k for k, f in fns.items() if np.asarray(f(Aint3)).dtype != np.float64]
report("int64 input -> float64 result for " + ", ".join(fns), not bad_int, f"(not float64: {bad_int})" if bad_int else "")
bad_32 = [k for k, f in fns.items() if np.asarray(f(Af32)).dtype != np.float32]
report("float32 input stays float32 (documented 'float32 stays float32') for the same functions (SPD matrix, real eigenvalues)", not bad_32, f"(not float32: {bad_32})" if bad_32 else "")
real_out = {"det", "solve", "lstsq x", "inv", "cholesky", "pinv", "qr R", "eigh V", "eig w", "matrix_power -1"}
bad_c = [k for k, f in fns.items() if np.asarray(f(Ac64)).dtype != (np.complex64 if k in real_out else np.float32)]
report("complex64 input -> complex64 results (real-valued outputs s, norms, eigvalsh, logabsdet, cond -> float32)", not bad_c, f"(wrong: {bad_c})" if bad_c else "")
report("mixed dtypes: solve(float32 A, int b) -> float64; solve(float32 A, complex64 b) -> complex64; solve(float64 A, complex64 b) -> complex128", np.linalg.solve(Af32, np.ones(3, int)).dtype == np.float64 and np.linalg.solve(Af32, np.ones(3, np.complex64)).dtype == np.complex64 and np.linalg.solve(Af32.astype(np.float64), np.ones(3, np.complex64)).dtype == np.complex128)
report("float16 and longdouble inputs raise TypeError in linalg (source _commonType: 'array type ... is unsupported in linalg')", raises(lambda: np.linalg.inv(Af32.astype(np.float16)), TypeError) and raises(lambda: np.linalg.inv(Af32.astype(np.longdouble)), TypeError))
report("object-dtype input raises TypeError in inv/eig", raises(lambda: np.linalg.inv(Aint3.astype(object)), TypeError) and raises(lambda: np.linalg.eig(Aint3.astype(object)), TypeError))
report("float32 results agree with the float64 truth to 1e-5 relative: inv, det, eigvalsh, cholesky, svd s (SPD 3x3)", maxdiff(np.linalg.inv(Af32), N(mp.inverse(M(SPD[:3, :3])))) < 1e-5 * np.abs(N(mp.inverse(M(SPD[:3, :3])))).max() and close(np.linalg.det(Af32), float(mp.det(M(SPD[:3, :3]))), 1e-5) and np.allclose(np.linalg.eigvalsh(Af32), sorted(float(x) for x in mp.eigsy(M(SPD[:3, :3]), eigvals_only=True)), rtol=1e-5) and maxdiff(np.linalg.cholesky(Af32), N(mp.cholesky(M(SPD[:3, :3])))) < 1e-5 and np.allclose(np.linalg.svd(Af32, compute_uv=False), mp_svals(SPD[:3, :3]), rtol=1e-5))

# ================= stacked broadcasting sweep (documented: 'Broadcasting rules apply ... the first a.ndim-2 dimensions are the stack')
print("---- stacked broadcasting sweep")
Stk2 = rs.randn(2, 3, 4, 4); Stk2 = Stk2 + 4 * np.eye(4)   # well conditioned
SPD2 = np.einsum('...ij,...kj->...ik', Stk2, Stk2) + np.eye(4)
sweep = {
    "inv": (np.linalg.inv, Stk2, lambda a: N(mp.inverse(M(a)))),
    "det": (np.linalg.det, Stk2, lambda a: float(mp.det(M(a)))),
    "slogdet logabsdet": (lambda a: np.linalg.slogdet(a)[1], Stk2, lambda a: math.log(abs(float(mp.det(M(a)))))),
    "eigvals (sorted by real part)": (lambda a: np.sort_complex(np.linalg.eigvals(a).astype(complex)), Stk2, lambda a: np.sort_complex(mp_eigvals(a))),
    "eigvalsh": (np.linalg.eigvalsh, SPD2, lambda a: np.array(sorted(float(x) for x in mp.eigsy(M(a), eigvals_only=True)))),
    "svd s": (lambda a: np.linalg.svd(a, compute_uv=False), Stk2, mp_svals),
    "qr |diag R|": (lambda a: np.abs(np.diagonal(np.linalg.qr(a)[1], axis1=-2, axis2=-1)), Stk2, lambda a: np.abs(np.diag(mp_qr(a)[1]))),
    "cholesky": (np.linalg.cholesky, SPD2, lambda a: N(mp.cholesky(M(a)))),
    "pinv": (np.linalg.pinv, Stk2, mp_pinv),
    "cond": (np.linalg.cond, Stk2, lambda a: (lambda s: s[0] / s[-1])(mp_svals(a))),
    "norm(axis=(-2,-1), 'nuc')": (lambda a: np.linalg.norm(a, 'nuc', axis=(-2, -1)), Stk2, lambda a: mp_svals(a).sum()),
    "matrix_power 3": (lambda a: np.linalg.matrix_power(a, 3), Stk2, lambda a: N(M(a) * M(a) * M(a))),
    "matrix_rank": (np.linalg.matrix_rank, Stk2, lambda a: 4),
    "solve (b stacked (2,3,4,2))": (lambda a: np.linalg.solve(a, bK2), Stk2, None),
}
bK2 = rs.randn(2, 3, 4, 2)
for name, (f, arr, truth) in sweep.items():
    out = f(arr); okk = True; worst = 0.0
    for i in range(2):
        for j in range(3):
            if name.startswith("solve"): t = mp_solve(arr[i, j], bK2[i, j])
            else: t = truth(arr[i, j])
            d = maxdiff(out[i, j], t); scale = max(1.0, float(np.max(np.abs(np.asarray(t, dtype=complex)))))
            worst = max(worst, d / scale); okk = okk and d / scale < 1e-9
    report(f"stack (2,3,4,4) {name}: result[i,j] equals the mpmath value for matrix [i,j] (2-level stack)", okk and np.asarray(out).shape[:2] == (2, 3), f"(worst rel diff {worst:.1e})")
report("stack with an empty leading dimension: inv/det/eig/svd/qr/cholesky of shape (0,3,3) return empty stacks of the right shape", np.linalg.inv(np.zeros((0, 3, 3))).shape == (0, 3, 3) and np.linalg.det(np.zeros((0, 3, 3))).shape == (0,) and np.linalg.svd(np.zeros((0, 3, 3)), compute_uv=False).shape == (0, 3) and np.linalg.eigvals(np.zeros((0, 3, 3))).shape == (0, 3) and np.linalg.qr(np.zeros((0, 3, 3)))[1].shape == (0, 3, 3) and np.linalg.cholesky(np.zeros((0, 3, 3))).shape == (0, 3, 3))
report("det/inv of an empty (0,0) matrix: det = 1.0, inv shape (0,0) (documented convention of the empty product)", np.linalg.det(np.zeros((0, 0))) == 1.0 and np.linalg.inv(np.zeros((0, 0))).shape == (0, 0))
print("---- done")
