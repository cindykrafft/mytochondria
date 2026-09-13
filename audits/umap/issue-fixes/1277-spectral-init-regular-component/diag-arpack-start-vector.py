import warnings, numpy as np, scipy.sparse, scipy.sparse.linalg
def lap(A):
    sqrt_deg = np.sqrt(np.asarray(A.sum(axis=0)).squeeze())
    D = scipy.sparse.spdiags(1.0 / sqrt_deg, 0, A.shape[0], A.shape[0])
    return scipy.sparse.identity(A.shape[0]) - D * A * D
def run(L, v0, dim):
    k = dim + 1
    ncv = max(2 * k + 1, int(np.sqrt(L.shape[0])))
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        try:
            vals, vecs = scipy.sparse.linalg.eigsh(L, k, which="SM", ncv=ncv, tol=1e-4, v0=v0, maxiter=L.shape[0] * 5)
        except Exception as e:
            return "ERR:" + type(e).__name__
    return vecs[:, np.argsort(vals)[1:k]]
def verdict(rs):
    if any(isinstance(r, str) for r in rs): return rs[0] if isinstance(rs[0], str) else "mixed"
    return "identical" if all(np.array_equal(rs[0], r) for r in rs[1:]) else "DIFFERS"
def complete(n): return scipy.sparse.csr_matrix(np.ones((n, n)) - np.eye(n))
def random_regular(n, d, seed):
    # pairing model, rejecting loops / multi-edges
    rng = np.random.RandomState(seed)
    while True:
        stubs = np.repeat(np.arange(n), d); rng.shuffle(stubs)
        A = np.zeros((n, n))
        ok = True
        for u, v in zip(stubs[::2], stubs[1::2]):
            if u == v or A[u, v]: ok = False; break
            A[u, v] = A[v, u] = 1.0
        if ok: return scipy.sparse.csr_matrix(A)
def irregular(n, seed):
    rng = np.random.RandomState(seed)
    A = rng.uniform(size=(n, n)); A = np.triu(A, 1); A = A + A.T
    return scipy.sparse.csr_matrix(A)
print(f"{'graph':28s} {'dim':>3s} | v0=ones (4 calls) | v0=seeded uniform (4 calls)")
for name, A in [("K10 (10 duplicates)", complete(10)), ("K12", complete(12)), ("K16", complete(16)), ("K30", complete(30)), ("K60", complete(60)),
                ("4-regular random n=40", random_regular(40, 4, 0)), ("3-regular random n=100", random_regular(100, 3, 1)),
                ("irregular random n=40", irregular(40, 0))]:
    L = lap(A)
    for dim in (2, 5):
        n = L.shape[0]
        ones = [run(L, np.ones(n), dim) for _ in range(4)]
        seeded = [run(L, np.random.RandomState(42).uniform(-1, 1, n), dim) for _ in range(4)]
        print(f"{name:28s} {dim:3d} | {verdict(ones):17s} | {verdict(seeded)}")
