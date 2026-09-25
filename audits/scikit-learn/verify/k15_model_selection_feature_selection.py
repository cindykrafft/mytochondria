#!/usr/bin/env python
"""model_selection (every splitter, cross_validate, cross_val_predict, learning_curve,
validation_curve, permutation_test_score with groups, ParameterGrid / ParameterSampler,
RandomizedSearchCV, multi-metric GridSearchCV, HalvingGridSearchCV /
HalvingRandomSearchCV resource schedules, TunedThresholdClassifierCV /
FixedThresholdClassifier) and feature_selection (chi2, r_regression, f_regression
center=False, the univariate selectors incl. exact Benjamini-Hochberg,
mutual_info_regression / continuous mutual_info_classif, VarianceThreshold, RFE, RFECV,
SelectFromModel, SequentialFeatureSelector, the SelectorMixin API) -- every check
against an independent truth: the documented examples (user guide / docstrings),
closed forms in fractions.Fraction / mpmath, or plain-Python / plain-numpy reference
implementations written here from the documented algorithm (greedy GroupKFold and
StratifiedGroupKFold, TimeSeriesSplit index ranges, KSG and Ross nearest-neighbour MI
estimators with the documented 1e-10 noise replicated, RFE / RFECV / SFS greedy loops
on hand-written OLS, successive-halving schedules from the user-guide formulas)."""
import sys, math, warnings, itertools, inspect, collections, zlib
sys.path.insert(0, ".")
from _synth import *
import mpmath
from mpmath import mp, mpf
mp.dps = 30
import scipy.sparse as sp
from scipy import stats
from sklearn.base import BaseEstimator, ClassifierMixin, RegressorMixin, clone
from sklearn.model_selection import (KFold, StratifiedKFold, GroupKFold, StratifiedGroupKFold, RepeatedKFold,
                                     RepeatedStratifiedKFold, LeaveOneOut, LeavePOut, LeaveOneGroupOut,
                                     LeavePGroupsOut, ShuffleSplit, StratifiedShuffleSplit, GroupShuffleSplit,
                                     PredefinedSplit, TimeSeriesSplit, check_cv, train_test_split, cross_validate,
                                     cross_val_predict, cross_val_score, learning_curve, validation_curve,
                                     permutation_test_score, ParameterGrid, ParameterSampler, GridSearchCV,
                                     RandomizedSearchCV)
from sklearn.experimental import enable_halving_search_cv  # noqa
from sklearn.model_selection import HalvingGridSearchCV, HalvingRandomSearchCV
from sklearn.feature_selection import (chi2, r_regression, f_regression, SelectKBest, SelectPercentile, SelectFpr,
                                       SelectFdr, SelectFwe, GenericUnivariateSelect, mutual_info_regression,
                                       mutual_info_classif, VarianceThreshold, RFE, RFECV, SelectFromModel,
                                       SequentialFeatureSelector)
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso, ElasticNetCV
from sklearn.dummy import DummyClassifier
from sklearn.exceptions import FitFailedWarning
from sklearn import metrics
banner(); warnings.filterwarnings("ignore")
V = tuple(int(x) for x in sklearn.__version__.split(".")[:2])
rs = np.random.RandomState(15)


def has_param(obj, name):
    return name in inspect.signature(obj).parameters


def caught(fn, cat=Warning):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        out = fn()
    return out, [x for x in w if issubclass(x.category, cat)]


def raises(fn, exc=Exception):
    try:
        fn()
    except exc as e:
        return type(e).__name__
    return None


def splits_as_lists(it):
    return [(list(map(int, a)), list(map(int, b))) for a, b in it]


def section(t):
    """Print a header and re-seed the shared RandomState, so every section sees the same data on every build
    (sections that are skipped on older builds do not shift the random streams of later ones)."""
    global rs
    print("== " + t); rs = np.random.RandomState(zlib.crc32(t.encode()) % 2 ** 31)


# ---------------------------------------------------------------------------------------------------------------
# reference implementations (plain Python / plain numpy, written from the documented algorithms)
def kfold_ref(order, k):
    n = len(order); sizes = [n // k + (1 if i < n % k else 0) for i in range(k)]; out = []; cur = 0
    for s in sizes:
        te = sorted(order[cur:cur + s]); tr = sorted(set(range(n)) - set(te)); out.append((tr, te)); cur += s
    return out


def groupkfold_ref(groups, k):
    """Greedy: largest groups first (ties: larger group index first = reverse of a stable ascending sort),
    each into the currently lightest fold (ties: lowest fold index)."""
    uniq = sorted(set(groups)); size = {g: list(groups).count(g) for g in uniq}
    order = sorted(range(len(uniq)), key=lambda i: (size[uniq[i]], i), reverse=True)
    load = [0] * k; fold_of = {}
    for i in order:
        f = min(range(k), key=lambda j: (load[j], j)); load[f] += size[uniq[i]]; fold_of[uniq[i]] = f
    return [[i for i, g in enumerate(groups) if fold_of[g] == f] for f in range(k)]


def pstd(v):
    m = sum(v) / len(v); return math.sqrt(sum((x - m) ** 2 for x in v) / len(v))


def isclose(a, b):
    return abs(a - b) <= 1e-8 + 1e-5 * abs(b)


def sgkf_ref(y, groups, k):
    """StratifiedGroupKFold greedy from the user guide implementation notes."""
    classes = sorted(set(y)); ug = sorted(set(groups)); ci = {c: i for i, c in enumerate(classes)}
    ycnt = [list(y).count(c) for c in classes]
    cnt = [[0] * len(classes) for _ in ug]
    for yy, g in zip(y, groups): cnt[ug.index(g)][ci[yy]] += 1
    order = sorted(range(len(ug)), key=lambda gi: -pstd(cnt[gi]))  # stable
    fold = [[0] * len(classes) for _ in range(k)]; gof = {}
    for gi in order:
        best = None; mn = math.inf; mns = math.inf
        for i in range(k):
            tent = [list(r) for r in fold]; tent[i] = [a + b for a, b in zip(tent[i], cnt[gi])]
            ev = sum(pstd([tent[f][c] / ycnt[c] for f in range(k)]) for c in range(len(classes))) / len(classes)
            s = sum(fold[i])
            if ev < mn or (isclose(ev, mn) and s < mns):
                mn, mns, best = ev, s, i
        fold[best] = [a + b for a, b in zip(fold[best], cnt[gi])]; gof[ug[gi]] = best
    return [[i for i, g in enumerate(groups) if gof[g] == f] for f in range(k)]


def tss_ref(n, k, max_train=None, test_size=None, gap=0):
    ts = test_size if test_size is not None else n // (k + 1); out = []
    for i in range(k):
        start = n - (k - i) * ts; end_tr = start - gap
        lo = max(0, end_tr - max_train) if max_train else 0
        out.append((list(range(lo, end_tr)), list(range(start, start + ts))))
    return out


def ols_fit(X, y):
    A = np.hstack([np.ones((len(X), 1)), X]); b = np.linalg.lstsq(A, y, rcond=None)[0]; return b[0], b[1:]


def r2_np(y, p):
    return 1 - np.sum((y - p) ** 2) / np.sum((y - y.mean()) ** 2)


def ols_cv_r2(X, y, folds):
    out = []
    for tr, te in folds:
        b0, b = ols_fit(X[tr], y[tr]); out.append(r2_np(y[te], b0 + X[te] @ b))
    return out


def digamma(x):
    return float(mpmath.digamma(x))


def ksg_ref(x, y, k):
    """Kraskov-Stoegbauer-Grassberger algorithm 1, max-norm, plain Python."""
    n = len(x); psi_sum = 0.0
    for i in range(n):
        d = sorted(max(abs(x[i] - x[j]), abs(y[i] - y[j])) for j in range(n) if j != i); eps = d[k - 1]
        nx = sum(1 for j in range(n) if j != i and abs(x[i] - x[j]) < eps)
        ny = sum(1 for j in range(n) if j != i and abs(y[i] - y[j]) < eps)
        psi_sum += digamma(nx + 1) + digamma(ny + 1)
    return max(0.0, digamma(n) + digamma(k) - psi_sum / n)


def ross_ref(c, d, k):
    """Ross (2014) continuous-discrete estimator; labels with a single member are dropped."""
    cnt = collections.Counter(d); keep = [i for i in range(len(c)) if cnt[d[i]] > 1]; N = len(keep)
    sk = sNx = sm = 0.0
    for i in keep:
        kk = min(k, cnt[d[i]] - 1)
        same = sorted(abs(c[i] - c[j]) for j in keep if j != i and d[j] == d[i]); rad = same[kk - 1]
        m = sum(1 for j in keep if j != i and abs(c[i] - c[j]) <= rad)
        sk += digamma(kk); sNx += digamma(cnt[d[i]]); sm += digamma(m)
    return max(0.0, digamma(N) + (sk - sNx - sm) / N)


def mi_noise(X, y, cont, discrete_target, seed):
    """The documented preprocessing: continuous columns scaled to unit variance (no centring), then
    1e-10 * max(1, mean|x|) standard-normal noise; same for a continuous y (drawn after X's noise)."""
    r = np.random.RandomState(seed); X = np.array(X, dtype=float); y = np.array(y, dtype=float); n = len(y)
    if cont.any():
        Xc = X[:, cont]
        if not (discrete_target and V < (1, 2)):   # 1.1.x did not scale X for a discrete target
            sd = Xc.std(0); sd[sd == 0] = 1; Xc = Xc / sd
        means = np.maximum(1, np.mean(np.abs(Xc), 0)); Xc = Xc + 1e-10 * means * r.standard_normal((n, cont.sum()))
        X[:, cont] = Xc
    if not discrete_target:
        sd = y.std(); y = y / (sd if sd else 1); y = y + 1e-10 * max(1, np.mean(np.abs(y))) * r.standard_normal(n)
    return X, y


# recording / toy estimators
LOG = []


class RecReg(RegressorMixin, BaseEstimator):
    """Records the sample ids (column 0) it is trained on; predicts the training mean."""
    def __init__(self, a=0):
        self.a = a

    def fit(self, X, y):
        X = np.asarray(X); LOG.append((tuple(sorted(int(v) for v in X[:, 0])), tuple(np.asarray(y).tolist())))
        self.m_ = float(np.mean(y)); return self

    def predict(self, X):
        return np.full(len(X), self.m_)


PLOG = []


class MeanReg(RegressorMixin, BaseEstimator):
    def __init__(self, a=0):
        self.a = a

    def fit(self, X, y):
        self.s_ = float(np.sum(y)); self.n_ = len(y); return self

    def partial_fit(self, X, y):
        PLOG.append(len(y)); self.s_ = getattr(self, "s_", 0.0) + float(np.sum(y)); self.n_ = getattr(self, "n_", 0) + len(y)
        return self

    def predict(self, X):
        return np.full(len(X), self.s_ / self.n_)


class Toy(RegressorMixin, BaseEstimator):
    """Score is the parameter a itself (plus nothing): a deterministic, tie-free halving tournament."""
    def __init__(self, a=0.0, budget=1):
        self.a = a; self.budget = budget

    def fit(self, X, y=None):
        return self

    def predict(self, X):
        return np.zeros(len(X))

    def score(self, X, y=None):
        return float(self.a)


class FailOn(RegressorMixin, BaseEstimator):
    """Raises in fit when the training fold contains sample id `bad`."""
    def __init__(self, bad=-1):
        self.bad = bad

    def fit(self, X, y):
        if self.bad in set(np.asarray(X)[:, 0].astype(int).tolist()):
            raise ValueError("planned failure")
        self.m_ = float(np.mean(y)); return self

    def predict(self, X):
        return np.full(len(X), self.m_)


# ===============================================================================================================
section("LeaveOneOut / LeavePOut")
got = splits_as_lists(LeaveOneOut().split([1, 2, 3, 4]))
report("LeaveOneOut: user-guide example [1 2 3] [0] / [0 2 3] [1] / [0 1 3] [2] / [0 1 2] [3]",
       got == [([1, 2, 3], [0]), ([0, 2, 3], [1]), ([0, 1, 3], [2]), ([0, 1, 2], [3])], f"({got})")
report("LeaveOneOut get_n_splits = n_samples (n=11)", LeaveOneOut().get_n_splits(np.zeros(11)) == 11)
report("LeaveOneOut with a single sample raises ValueError", raises(lambda: list(LeaveOneOut().split([[1]]))) == "ValueError")
got = splits_as_lists(LeavePOut(2).split(np.ones(4)))
exp = [([2, 3], [0, 1]), ([1, 3], [0, 2]), ([1, 2], [0, 3]), ([0, 3], [1, 2]), ([0, 2], [1, 3]), ([0, 1], [2, 3])]
report("LeavePOut(2) on 4 samples: user-guide example (lexicographic combinations)", got == exp, f"({got})")
got = splits_as_lists(LeavePOut(3).split(np.ones(7)))
report("LeavePOut(3) on 7: C(7,3) = 35 splits, test sets = itertools.combinations in order, train = complement",
       LeavePOut(3).get_n_splits(np.ones(7)) == 35 and [tuple(t) for _, t in got] == list(itertools.combinations(range(7), 3))
       and all(sorted(a + b) == list(range(7)) for a, b in got))
report("LeavePOut(p) with p >= n_samples raises ValueError ('p must be strictly less than the number of samples')",
       raises(lambda: list(LeavePOut(4).split(np.ones(4)))) == "ValueError")

# ---------------------------------------------------------------------------------------------------------------
section("KFold / RepeatedKFold / RepeatedStratifiedKFold shuffle semantics")
n = 23
kf = KFold(4, shuffle=True, random_state=7)
perm = np.arange(n); np.random.RandomState(7).shuffle(perm)
got = splits_as_lists(kf.split(np.zeros(n)))
report("KFold(shuffle=True, random_state=7): indices shuffled once by RandomState(7).shuffle, then cut into consecutive folds (sizes 6,6,6,5)",
       got == kfold_ref(list(perm), 4), f"(test sizes {[len(t) for _, t in got]})")
report("KFold(shuffle=True, random_state=int): identical splits on repeated split() calls",
       got == splits_as_lists(kf.split(np.zeros(n))))
kfr = KFold(4, shuffle=True, random_state=np.random.RandomState(7))
a1 = splits_as_lists(kfr.split(np.zeros(n))); a2 = splits_as_lists(kfr.split(np.zeros(n)))
report("KFold(shuffle=True, random_state=RandomState instance): each split() call draws a new shuffle (glossary: 'different across calls')",
       a1 != a2 and a1 == got)
e = raises(lambda: KFold(4, shuffle=False, random_state=0))
report("KFold(shuffle=False, random_state=0): docstring says random_state then 'has no effect'",
       e is None, f"(constructor raises {e})" if e else "")
X4 = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
got = splits_as_lists(RepeatedKFold(n_splits=2, n_repeats=2, random_state=12883823).split(X4))
report("RepeatedKFold user-guide example (random_state=12883823): [2 3][0 1] / [0 1][2 3] / [0 2][1 3] / [1 3][0 2]",
       got == [([2, 3], [0, 1]), ([0, 1], [2, 3]), ([0, 2], [1, 3]), ([1, 3], [0, 2])], f"({got})")
rkf = RepeatedKFold(n_splits=3, n_repeats=4, random_state=3)
got = splits_as_lists(rkf.split(np.zeros(n))); r = np.random.RandomState(3); exp = []
for _ in range(4):
    p = np.arange(n); r.shuffle(p); exp += kfold_ref(list(p), 3)
report("RepeatedKFold(3, n_repeats=4, random_state=3): one RandomState(3) drives successive KFold shuffles; 12 splits",
       got == exp and rkf.get_n_splits() == 12)
report("RepeatedKFold: every repetition's test folds partition the samples, and repetitions differ",
       all(sorted(sum((t for _, t in got[3 * i:3 * i + 3]), [])) == list(range(n)) for i in range(4))
       and len({tuple(map(tuple, (t for _, t in got[3 * i:3 * i + 3]))) for i in range(4)}) == 4)
yr = np.array([0] * 10 + [1] * 7 + [2] * 6)
rskf = list(RepeatedStratifiedKFold(n_splits=3, n_repeats=3, random_state=0).split(np.zeros(n), yr))
ok = len(rskf) == 9
for i in range(3):
    folds = rskf[3 * i:3 * i + 3]
    ok &= sorted(np.concatenate([t for _, t in folds]).tolist()) == list(range(n))
    for c in (0, 1, 2):
        cc = [int((yr[t] == c).sum()) for _, t in folds]; ok &= max(cc) - min(cc) <= 1
report("RepeatedStratifiedKFold(3, 3): 9 splits, each repetition a partition with per-class fold counts differing by <= 1", ok)
report("_RepeatedSplits: cvargs must not contain random_state/shuffle (ValueError)",
       raises(lambda: RepeatedKFold(n_splits=3, shuffle=True)) in ("ValueError", "TypeError"))

# ---------------------------------------------------------------------------------------------------------------
section("GroupKFold (greedy balancing, 1.6+ shuffle) and StratifiedGroupKFold")
Xg = [0.1, 0.2, 2.2, 2.4, 2.3, 4.55, 5.8, 8.8, 9, 10]; yg = ["a", "b", "b", "b", "c", "c", "c", "d", "d", "d"]
gg = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
got = splits_as_lists(GroupKFold(n_splits=3).split(Xg, yg, groups=gg))
report("GroupKFold user-guide example: [0..5] [6 7 8 9] / [0 1 2 6 7 8 9] [3 4 5] / [3..9] [0 1 2]",
       got == [([0, 1, 2, 3, 4, 5], [6, 7, 8, 9]), ([0, 1, 2, 6, 7, 8, 9], [3, 4, 5]), ([3, 4, 5, 6, 7, 8, 9], [0, 1, 2])], f"({got})")
got = splits_as_lists(GroupKFold(n_splits=2).split(np.zeros(6), groups=[0, 0, 2, 2, 3, 3]))
report("GroupKFold docstring example (groups 0,0,2,2,3,3; 2 splits): test [0 1 4 5] then [2 3]",
       got == [([2, 3], [0, 1, 4, 5]), ([0, 1, 4, 5], [2, 3])], f"({got})")
sizes = [9, 1, 7, 3, 5, 2, 8, 4, 6, 11, 10]
groups = np.repeat(np.arange(len(sizes)), sizes); rs.shuffle(groups)
got = [sorted(t.tolist()) for _, t in GroupKFold(4).split(np.zeros(len(groups)), groups=groups)]
exp = groupkfold_ref(groups.tolist(), 4)
print("   fold sample counts", [len(t) for t in got], " reference", [len(t) for t in exp])
report("GroupKFold(4), 11 groups of distinct sizes: folds = greedy 'largest group into the lightest fold' (recomputed)", got == exp)
report("GroupKFold: each group appears in exactly one test fold; test folds partition the samples",
       sorted(sum(got, [])) == list(range(len(groups))) and all(len({f for f, t in enumerate(got) if i in t}) == 1 for i in range(len(groups))))
tie_sizes = [3, 3, 3, 2, 2, 2, 1]
gt = np.repeat(np.arange(len(tie_sizes)), tie_sizes)
got = [sorted(t.tolist()) for _, t in GroupKFold(3).split(np.zeros(len(gt)), groups=gt)]
if V >= (1, 6):
    report("GroupKFold(3) with tied group sizes (1.6+ stable argsort): tie order = larger group label first, lightest fold = lowest index (reference)",
           got == groupkfold_ref(gt.tolist(), 3), f"({got})")
else:
    report("GroupKFold(3) with tied group sizes (before 1.6 the tie order is 'arbitrary'): fold sample counts = greedy reference",
           sorted(len(t) for t in got) == sorted(len(t) for t in groupkfold_ref(gt.tolist(), 3)), f"({got})")
# balance claims
gb = np.repeat(np.arange(4), [10, 10, 1, 1])
nosh = [len(t) for _, t in GroupKFold(2).split(np.zeros(22), groups=gb)]
report("user guide: GroupKFold 'attempts to place the same number of samples in each fold when shuffle=False' (sizes 10,10,1,1 -> 11/11)",
       nosh == [11, 11], f"({nosh})")
if has_param(GroupKFold, "shuffle"):
    worst = []
    for seed in range(12):
        fs = [len(t) for _, t in GroupKFold(2, shuffle=True, random_state=seed).split(np.zeros(22), groups=gb)]
        worst.append(max(fs) - min(fs))
    print("   shuffle=True |fold size difference| over seeds 0..11:", worst)
    report("GroupKFold docstring: 'the number of samples is approximately the same in each test fold when `shuffle` is True'",
           max(worst) <= 2, f"(sample counts differ by up to {max(worst)} of 22; shuffle=True balances the NUMBER OF GROUPS, as the user guide says)")
    gs_ = np.repeat(np.arange(len(sizes)), sizes)
    r = np.random.RandomState(5); perm = r.permutation(np.arange(len(sizes)))
    exp = [sorted(np.flatnonzero(np.isin(gs_, part)).tolist()) for part in np.array_split(perm, 4)]
    got = [sorted(t.tolist()) for _, t in GroupKFold(4, shuffle=True, random_state=5).split(np.zeros(len(gs_)), groups=gs_)]
    report("GroupKFold(shuffle=True, random_state=5): groups permuted by RandomState(5).permutation and cut by np.array_split (group counts 3,3,3,2)",
           got == exp)
else:
    print("   GroupKFold(shuffle) not available before 1.6 -- skipped")
g1 = np.repeat(np.arange(11), [10] + [1] * 10)
ng = [len(set(g1[t])) for _, t in GroupKFold(2).split(np.zeros(20), groups=g1)]
report("StratifiedGroupKFold docstring: GroupKFold 'attempts to create balanced folds such that the number of distinct groups is approximately the same in each fold'",
       max(ng) - min(ng) <= 1, f"(default GroupKFold: distinct groups per test fold {ng} -- it balances samples, not groups)")
# StratifiedGroupKFold
Xs = list(range(18)); ys = [1] * 6 + [0] * 12; gsg = [1, 2, 3, 3, 4, 4, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 6]
got = splits_as_lists(StratifiedGroupKFold(n_splits=3).split(Xs, ys, groups=gsg))
report("StratifiedGroupKFold user-guide example: tests [1 8 9 12 13 14] / [2 3 10 15 16 17] / [0 4 5 6 7 11]",
       [t for _, t in got] == [[1, 8, 9, 12, 13, 14], [2, 3, 10, 15, 16, 17], [0, 4, 5, 6, 7, 11]], f"({[t for _, t in got]})")
yd = np.array([0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]); gd = np.array([1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 7, 8, 8])
got = [t for _, t in splits_as_lists(StratifiedGroupKFold(n_splits=3).split(np.ones((17, 2)), yd, gd))]
report("StratifiedGroupKFold docstring example: tests [4 5 6 12 13 14] / [0 1 2 3 15 16] / [7 8 9 10 11]",
       got == [[4, 5, 6, 12, 13, 14], [0, 1, 2, 3, 15, 16], [7, 8, 9, 10, 11]], f"({got})")
ysg = rs.randint(0, 3, 120); gsr = rs.randint(0, 25, 120)
got = [sorted(t.tolist()) for _, t in StratifiedGroupKFold(4).split(np.zeros(120), ysg, gsr)]
report("StratifiedGroupKFold(4) on 120 samples / 25 groups / 3 classes = greedy of the implementation notes (plain-Python recomputation)",
       got == sgkf_ref(ysg.tolist(), gsr.tolist(), 4))
lab = np.array(["Sad", "Happy"])[(ysg > 0).astype(int)]; lab2 = (lab == "Happy").astype(int) * 0 + (lab == "Sad").astype(int)
a = splits_as_lists(StratifiedGroupKFold(3).split(np.zeros(120), lab, gsr)); b = splits_as_lists(StratifiedGroupKFold(3).split(np.zeros(120), 1 - lab2, gsr))
report("StratifiedGroupKFold Notes: 'invariant to class label' (y = ['Happy','Sad'] vs [1, 0] gives the same indices)", a == b)
sh = [sorted(t.tolist()) for _, t in StratifiedGroupKFold(4, shuffle=True, random_state=0).split(np.zeros(120), ysg, gsr)]
report("StratifiedGroupKFold(shuffle=True): still a partition with non-overlapping groups",
       sorted(sum(sh, [])) == list(range(120)) and all(not (set(gsr[a_]) & set(gsr[b_])) for a_, b_ in itertools.combinations(sh, 2)))

# ---------------------------------------------------------------------------------------------------------------
section("LeaveOneGroupOut / LeavePGroupsOut / PredefinedSplit")
gl = np.array([3, 1, 2, 1, 3, 2, 2])
got = [t for _, t in splits_as_lists(LeaveOneGroupOut().split(np.zeros(7), groups=gl))]
report("LeaveOneGroupOut: one split per unique group in sorted label order (1, 2, 3); n_splits = 3",
       got == [[1, 3], [2, 5, 6], [0, 4]] and LeaveOneGroupOut().get_n_splits(groups=gl) == 3, f"({got})")
report("LeaveOneGroupOut with one group raises ValueError", raises(lambda: list(LeaveOneGroupOut().split(np.zeros(3), groups=[1, 1, 1]))) == "ValueError")
got = splits_as_lists(LeavePGroupsOut(n_groups=2).split(np.zeros(3), groups=np.array([1, 2, 3])))
report("LeavePGroupsOut docstring example (groups 1,2,3; p=2): tests [0 1] / [0 2] / [1 2]",
       got == [([2], [0, 1]), ([1], [0, 2]), ([0], [1, 2])])
g4 = np.array([4, 1, 3, 1, 2, 4, 3, 2, 2])
got = [t for _, t in splits_as_lists(LeavePGroupsOut(2).split(np.zeros(9), groups=g4))]
exp = [sorted(np.flatnonzero(np.isin(g4, c)).tolist()) for c in itertools.combinations([1, 2, 3, 4], 2)]
report("LeavePGroupsOut(2) on 4 groups: C(4,2) = 6 splits = combinations of the sorted unique labels",
       got == exp and LeavePGroupsOut(2).get_n_splits(groups=g4) == 6)
report("LeavePGroupsOut(n_groups >= number of groups) raises ValueError", raises(lambda: list(LeavePGroupsOut(4).split(np.zeros(9), groups=g4))) == "ValueError")
got = splits_as_lists(PredefinedSplit([0, 1, -1, 1]).split())
report("PredefinedSplit docstring example (test_fold [0 1 -1 1]): [1 2 3][0] / [0 2][1 3]", got == [([1, 2, 3], [0]), ([0, 2], [1, 3])])
ps = PredefinedSplit([2, 0, 2, -1, 0, 5, -1])
got = splits_as_lists(ps.split())
report("PredefinedSplit: folds in sorted id order (0, 2, 5), -1 samples in every training set, n_splits = 3",
       [t for _, t in got] == [[1, 4], [0, 2], [5]] and all(3 in tr and 6 in tr for tr, _ in got) and ps.get_n_splits() == 3)

# ---------------------------------------------------------------------------------------------------------------
section("ShuffleSplit / StratifiedShuffleSplit / GroupShuffleSplit size rules")
got = [(tr, te) for tr, te in splits_as_lists(ShuffleSplit(n_splits=5, test_size=0.25, random_state=0).split(np.arange(10)))]
exp = [([9, 1, 6, 7, 3, 0, 5], [2, 8, 4]), ([2, 9, 8, 0, 6, 7, 4], [3, 5, 1]), ([4, 5, 1, 0, 6, 9, 7], [2, 3, 8]),
       ([2, 7, 5, 8, 0, 3, 4], [6, 1, 9]), ([4, 1, 0, 6, 8, 9, 3], [5, 2, 7])]
report("ShuffleSplit user-guide example (10 samples, test_size=0.25, random_state=0)", got == exp, f"({got[0]})")
got = splits_as_lists(ShuffleSplit(n_splits=5, train_size=0.5, test_size=.25, random_state=0).split(np.zeros(6)))
report("ShuffleSplit docstring example (train 0.5 / test .25 on 6): train [1 3 0] test [5 2] first",
       got[0] == ([1, 3, 0], [5, 2]) and got[4] == ([3, 5, 1], [2, 4]))
r = np.random.RandomState(4); ok = True
for tr, te in ShuffleSplit(3, test_size=0.3, random_state=4).split(np.zeros(17)):
    p = r.permutation(17); ok &= list(te) == list(p[:6]) and list(tr) == list(p[6:])
report("ShuffleSplit: test = first ceil(0.3*17)=6 of a fresh RandomState permutation, train = the rest (source rule)", ok)
cases = [(0.25, None, 17), (None, 0.6, 17), (0.2, 0.5, 17), (5, None, 17), (None, 4, 17), (0.3, 7, 17), (None, None, 17), (None, None, 25)]
bad = []
for tst, trn, nn in cases:
    tr, te = next(ShuffleSplit(1, test_size=tst, train_size=trn, random_state=0).split(np.zeros(nn)))
    et = (math.ceil(F(str(tst)) * nn) if isinstance(tst, float) else tst) if tst is not None else None
    er = (math.floor(F(str(trn)) * nn) if isinstance(trn, float) else trn) if trn is not None else None
    if et is None and er is None: et = math.ceil(F(1, 10) * nn)
    if er is None: er = nn - et
    if et is None: et = nn - er
    if (len(tr), len(te)) != (er, et): bad.append((tst, trn, nn, len(tr), len(te), er, et))
report("ShuffleSplit sizes: float test_size rounded UP, float train_size rounded DOWN, None = complement, default test 0.1 (8 cases)",
       not bad, f"({bad})")
tr, te = next(ShuffleSplit(1, test_size=0.07, random_state=0).split(np.zeros(100)))
report("ShuffleSplit(test_size=0.07) on 100 samples: 7% of 100 = 7 test samples", len(te) == 7,
       f"(got {len(te)}: ceil(0.07*100) with 0.07*100 = {0.07 * 100!r} in binary floating point)")
tr, te = next(ShuffleSplit(1, train_size=0.29, test_size=0.5, random_state=0).split(np.zeros(100)))
report("ShuffleSplit(train_size=0.29) on 100 samples: 29% of 100 = 29 training samples", len(tr) == 29,
       f"(got {len(tr)}: floor(0.29*100) with 0.29*100 = {0.29 * 100!r})")
a_, b_ = train_test_split(np.arange(100), test_size=0.14, random_state=0)
report("train_test_split(test_size=0.14) on 100 samples: 14 test samples", len(b_) == 14, f"(got {len(b_)}; 0.14*100 = {0.14 * 100!r})")
report("ShuffleSplit: train_size + test_size > n raises ValueError", raises(lambda: next(ShuffleSplit(1, test_size=10, train_size=10).split(np.zeros(17)))) == "ValueError")
# StratifiedShuffleSplit
got = splits_as_lists(StratifiedShuffleSplit(n_splits=5, test_size=0.5, random_state=0).split(np.zeros((6, 2)), np.array([0, 0, 0, 1, 1, 1])))
report("StratifiedShuffleSplit docstring example: fold 0 train [5 2 3] test [4 1 0], fold 4 train [0 5 1] test [3 4 2]",
       got[0] == ([5, 2, 3], [4, 1, 0]) and got[4] == ([0, 5, 1], [3, 4, 2]), f"({got[0]}, {got[4]})")
ysss = np.array([0] * 13 + [1] * 7 + [2] * 5 + [3] * 3); nS = len(ysss)
ok = True; det = []
for tr, te in StratifiedShuffleSplit(20, test_size=0.3, random_state=1).split(np.zeros(nS), ysss):
    ntr, nte = len(tr), len(te); cc = np.bincount(ysss)
    ni = np.bincount(ysss[tr], minlength=4); ti = np.bincount(ysss[te], minlength=4)
    ok &= ntr == nS - math.ceil(F(3, 10) * nS) and nte == math.ceil(F(3, 10) * nS)
    ok &= all(math.floor(F(int(c) * ntr, nS)) <= a <= math.ceil(F(int(c) * ntr, nS)) for c, a in zip(cc, ni))
    rem = cc - ni
    ok &= all(math.floor(F(int(c) * nte, int(rem.sum()))) <= a <= math.ceil(F(int(c) * nte, int(rem.sum()))) for c, a in zip(rem, ti))
    ok &= not (set(tr) & set(te)); det.append(tuple(ni))
report("StratifiedShuffleSplit: per-class train counts within floor/ceil of c*n_train/n, test counts within floor/ceil of the remaining share, disjoint (20 splits)",
       ok, f"(train class counts seen {sorted(set(det))})")
report("StratifiedShuffleSplit: a class with a single member raises ValueError",
       raises(lambda: next(StratifiedShuffleSplit(1, test_size=0.3).split(np.zeros(6), [0, 0, 0, 1, 1, 2]))) == "ValueError")
report("StratifiedShuffleSplit: n_test < n_classes raises ValueError",
       raises(lambda: next(StratifiedShuffleSplit(1, test_size=2).split(np.zeros(9), [0, 0, 0, 1, 1, 1, 2, 2, 2]))) == "ValueError")
# GroupShuffleSplit
gss_g = np.repeat(np.arange(10), [3, 1, 4, 2, 5, 1, 2, 3, 1, 2]) + 100
ok = True; r = np.random.RandomState(9)
for tr, te in GroupShuffleSplit(n_splits=4, test_size=0.25, random_state=9).split(np.zeros(len(gss_g)), groups=gss_g):
    p = r.permutation(10); tg = set((p[:3] + 100).tolist()); rg = set((p[3:] + 100).tolist())
    ok &= set(gss_g[te].tolist()) == tg and set(gss_g[tr].tolist()) == rg
report("GroupShuffleSplit(test_size=0.25) with 10 groups: ceil(2.5) = 3 test GROUPS ('rounded up'), 7 train groups, whole groups only",
       ok)
tr, te = next(GroupShuffleSplit(random_state=0).split(np.zeros(len(gss_g)), groups=gss_g))
report("GroupShuffleSplit default test_size = 0.2 of the groups (2 of 10), n_splits default 5",
       len(set(gss_g[te])) == 2 and len(set(gss_g[tr])) == 8 and GroupShuffleSplit().get_n_splits() == 5)

# ---------------------------------------------------------------------------------------------------------------
section("TimeSeriesSplit")
X6 = np.zeros((6, 2))
got = splits_as_lists(TimeSeriesSplit().split(X6))
report("TimeSeriesSplit() docstring example on 6 samples: train [0..i], test [i+1] for i = 0..4",
       got == [(list(range(i + 1)), [i + 1]) for i in range(5)])
got = splits_as_lists(TimeSeriesSplit(n_splits=3).split(X6))
report("TimeSeriesSplit(3) user-guide example: [0 1 2][3] / [0 1 2 3][4] / [0..4][5]", got == [([0, 1, 2], [3]), ([0, 1, 2, 3], [4]), ([0, 1, 2, 3, 4], [5])])
X12 = np.zeros((12, 2))
got = splits_as_lists(TimeSeriesSplit(n_splits=3, test_size=2).split(X12))
report("TimeSeriesSplit(3, test_size=2) docstring example", got == [(list(range(6)), [6, 7]), (list(range(8)), [8, 9]), (list(range(10)), [10, 11])])
got = splits_as_lists(TimeSeriesSplit(n_splits=3, test_size=2, gap=2).split(X12))
report("TimeSeriesSplit(3, test_size=2, gap=2) docstring example", got == [(list(range(4)), [6, 7]), (list(range(6)), [8, 9]), (list(range(8)), [10, 11])])
bad = []
for nn, k, mt, ts, gap in [(23, 4, None, None, 0), (23, 4, 7, 3, 1), (40, 5, 10, 4, 3), (17, 3, None, 5, 0), (30, 6, 3, None, 2)]:
    got = splits_as_lists(TimeSeriesSplit(k, max_train_size=mt, test_size=ts, gap=gap).split(np.zeros(nn)))
    if got != tss_ref(nn, k, mt, ts, gap): bad.append((nn, k, mt, ts, gap))
report("TimeSeriesSplit exact index ranges: test starts n - (k-i)*test_size, train ends test_start - gap, keeps the LAST max_train_size (5 configs)", not bad, f"({bad})")
nn, k = 11, 5
ts = nn // (k + 1); rr = nn % (k + 1)
actual = [len(tr) for tr, _ in TimeSeriesSplit(k).split(np.zeros(nn))]
literal = [i * nn // (k + 1) + nn % (k + 1) for i in range(1, k + 1)]
report("TimeSeriesSplit Notes: training size in the i-th split = i * (n_samples // (n_splits+1)) + n_samples % (n_splits+1)",
       actual == [i * ts + rr for i in range(1, k + 1)], f"({actual})")
report("TimeSeriesSplit Notes formula typed literally as Python, ``i * n_samples // (n_splits + 1) + n_samples % (n_splits + 1)`` (n=11, k=5)",
       literal == actual, f"(literal evaluation gives {literal}, actual sizes {actual})")
ok_big = raises(lambda: list(TimeSeriesSplit(3, test_size=4).split(np.zeros(13))))
report("TimeSeriesSplit test_size docstring: default n_samples//(n_splits+1) = 3 'is the maximum allowed value with gap=0' (n=13, k=3: test_size=4 must be refused)",
       ok_big is not None, f"(test_size=4 accepted: splits {[(len(a), len(b)) for a, b in TimeSeriesSplit(3, test_size=4).split(np.zeros(13))]})" if ok_big is None else "")
report("TimeSeriesSplit: too many splits for n_samples/test_size/gap raises ValueError",
       raises(lambda: list(TimeSeriesSplit(3, test_size=3, gap=4).split(np.zeros(13)))) == "ValueError")

# ---------------------------------------------------------------------------------------------------------------
section("check_cv defaults")
yb = np.array([0, 1] * 10); ycont = np.linspace(0, 1, 20); yml = np.array([[0, 1], [1, 0]] * 10)
c0 = check_cv(None)
report("check_cv(None) = KFold(5) without shuffling", type(c0) is KFold and c0.n_splits == 5 and not c0.shuffle)
report("check_cv(3, y binary, classifier=True) = StratifiedKFold(3)", type(check_cv(3, yb, classifier=True)) is StratifiedKFold)
report("check_cv(3, y binary, classifier=False) = KFold(3)", type(check_cv(3, yb, classifier=False)) is KFold)
report("check_cv(3, y continuous, classifier=True) = KFold (y neither binary nor multiclass)", type(check_cv(3, ycont, classifier=True)) is KFold)
report("check_cv(3, y multilabel, classifier=True) = KFold", type(check_cv(3, yml, classifier=True)) is KFold)
it = [(np.arange(5, 10), np.arange(5)), (np.arange(5), np.arange(5, 10))]
w = check_cv(it)
report("check_cv(iterable): wrapper with get_n_splits = len and the given splits", w.get_n_splits() == 2 and splits_as_lists(w.split()) == splits_as_lists(it))
kk = KFold(3)
report("check_cv(splitter instance) returns the same object", check_cv(kk) is kk)
if has_param(check_cv, "shuffle"):
    c1 = check_cv(4, yb, classifier=True, shuffle=True, random_state=3)
    report("check_cv(shuffle=True, random_state=3) -> StratifiedKFold(4, shuffle=True, random_state=3)", type(c1) is StratifiedKFold and c1.shuffle and c1.random_state == 3)
else:
    print("   check_cv(shuffle, random_state) not available in this version -- skipped")
# same shuffling for all candidates in a GridSearchCV fit
Xid = np.column_stack([np.arange(30), rs.randn(30)]); yid = rs.randn(30)
LOG.clear(); GridSearchCV(RecReg(), {"a": [0, 1, 2]}, cv=KFold(3, shuffle=True), refit=False).fit(Xid, yid)
per = collections.defaultdict(set)
for i, (ids, _) in enumerate(LOG): per[i % 3].add(ids)
report("user guide: GridSearchCV with KFold(shuffle=True, random_state=None) uses the same shuffling for every parameter setting",
       all(len(v) == 1 for v in per.values()) and len(LOG) == 9)

# ===============================================================================================================
section("cross_validate")
Xr = rs.randn(40, 3); Xr[:, 0] = np.arange(40); yrg = Xr[:, 1] * 2 - Xr[:, 2] + rs.randn(40) * 0.5
cvk = KFold(4, shuffle=True, random_state=2); folds = list(cvk.split(Xr))
res = cross_validate(LinearRegression(), Xr, yrg, cv=cvk, scoring=["r2", "neg_mean_absolute_error"], return_train_score=True, return_estimator=True)
man_te = []; man_tr = []; man_mae = []; man_coef = []
for tr, te in folds:
    b0, b = ols_fit(Xr[tr], yrg[tr]); man_te.append(r2_np(yrg[te], b0 + Xr[te] @ b)); man_tr.append(r2_np(yrg[tr], b0 + Xr[tr] @ b))
    man_mae.append(-np.mean(np.abs(yrg[te] - b0 - Xr[te] @ b))); man_coef.append(b)
report("cross_validate(scoring=[r2, neg_mae]): keys test_r2 / test_neg_mean_absolute_error / train_* / fit_time / score_time / estimator",
       {"test_r2", "test_neg_mean_absolute_error", "train_r2", "train_neg_mean_absolute_error", "fit_time", "score_time", "estimator"} <= set(res))
report("cross_validate test_r2 = R^2 of a fresh OLS fit on each training fold (hand-written OLS)", np.allclose(res["test_r2"], man_te, rtol=1e-9))
report("cross_validate return_train_score: train_r2 = R^2 on the training fold itself", np.allclose(res["train_r2"], man_tr, rtol=1e-9))
report("cross_validate test_neg_mean_absolute_error = -MAE on the test fold", np.allclose(res["test_neg_mean_absolute_error"], man_mae, rtol=1e-9))
report("cross_validate return_estimator: the i-th estimator is the fit on the i-th training fold", all(np.allclose(e.coef_, c, rtol=1e-8) for e, c in zip(res["estimator"], man_coef)))
report("cross_validate fit_time / score_time: one non-negative float per split", len(res["fit_time"]) == 4 and np.all(res["fit_time"] >= 0) and np.all(res["score_time"] >= 0))
res2 = cross_validate(LinearRegression(), Xr, yrg, cv=cvk, scoring={"R": "r2", "M": metrics.make_scorer(metrics.max_error)})
report("cross_validate(scoring=dict): keys test_<name>; make_scorer(max_error) value = max |error| per fold",
       np.allclose(res2["test_R"], man_te) and np.allclose(res2["test_M"], [np.max(np.abs(yrg[te] - ols_fit(Xr[tr], yrg[tr])[0] - Xr[te] @ ols_fit(Xr[tr], yrg[tr])[1])) for tr, te in folds]))
bad_id = int(folds[0][1][0])   # in test of fold 0 -> in the training set of folds 1..3
(resf, wf) = caught(lambda: cross_validate(FailOn(bad=bad_id), Xr, yrg, cv=cvk, error_score=-99.0, return_train_score=True), FitFailedWarning)
report("cross_validate(error_score=-99): folds whose fit fails get test AND train score -99, others are real, FitFailedWarning raised",
       list(resf["test_score"][1:]) == [-99.0] * 3 and np.isfinite(resf["test_score"][0]) and resf["test_score"][0] != -99 and list(resf["train_score"][1:]) == [-99.0] * 3 and len(wf) >= 1,
       f"({resf['test_score']})")
report("cross_validate(error_score='raise') re-raises the fit error", raises(lambda: cross_validate(FailOn(bad=bad_id), Xr, yrg, cv=cvk, error_score="raise")) == "ValueError")
resn = cross_validate(FailOn(bad=bad_id), Xr, yrg, cv=cvk)
report("cross_validate default error_score=np.nan", np.isnan(resn["test_score"][1:]).all() and not np.isnan(resn["test_score"][0]))
if has_param(cross_validate, "return_indices"):
    ri = cross_validate(LinearRegression(), Xr, yrg, cv=cvk, return_indices=True)
    report("cross_validate(return_indices=True): indices['train'/'test'] are the splitter's folds",
           all(np.array_equal(a, b) for a, (b, _) in zip(ri["indices"]["train"], folds)) and all(np.array_equal(a, b) for a, (_, b) in zip(ri["indices"]["test"], folds)))
    report("cross_validate(return_indices=True): docstring 'a list of integer-dtyped NumPy arrays'",
           isinstance(ri["indices"]["train"], list) and all(np.asarray(a).dtype.kind == "i" for a in ri["indices"]["train"]),
           f"(container type {type(ri['indices']['train']).__name__})")
else:
    print("   cross_validate(return_indices) not available before 1.3 -- skipped")

# ---------------------------------------------------------------------------------------------------------------
section("cross_val_predict")
Xc = rs.randn(45, 2); ycls = np.array(["b", "c", "a"])[np.argmax(Xc @ rs.randn(2, 3) + rs.randn(45, 3) * 0.3, 1)]
cvs = KFold(5, shuffle=True, random_state=4)
pp = cross_val_predict(LogisticRegression(max_iter=2000), Xc, ycls, cv=cvs, method="predict_proba")
pred = cross_val_predict(LogisticRegression(max_iter=2000), Xc, ycls, cv=cvs)
exp_p = np.zeros((45, 3)); exp_l = np.empty(45, dtype=object)
for tr, te in cvs.split(Xc):
    m = LogisticRegression(max_iter=2000).fit(Xc[tr], ycls[tr])
    exp_p[te] = m.predict_proba(Xc[te])[:, [list(m.classes_).index(c) for c in ["a", "b", "c"]]]; exp_l[te] = m.predict(Xc[te])
report("cross_val_predict(method='predict_proba'): row i comes from the fold where i is a test sample (order restored), columns in sorted class order a,b,c",
       np.allclose(pp, exp_p, atol=1e-12))
report("cross_val_predict(): predictions restored to the original sample order", list(pred) == list(exp_l))
ysort = np.array([0] * 15 + [1] * 15 + [2] * 15)
(ppm, wm) = caught(lambda: cross_val_predict(LogisticRegression(max_iter=2000), Xc, ysort, cv=KFold(3), method="predict_proba"), RuntimeWarning)
report("cross_val_predict Notes: a class absent from a training fold gets predict_proba 0 in its column (KFold(3) on class-sorted y)",
       np.all(ppm[:15, 0] == 0) and np.all(ppm[15:30, 1] == 0) and np.all(ppm[30:, 2] == 0) and np.allclose(ppm.sum(1), 1) and len(wm) >= 1)
plm = cross_val_predict(LogisticRegression(max_iter=2000), Xc, ysort, cv=KFold(3), method="predict_log_proba")
report("cross_val_predict Notes: for predict_log_proba the missing column is the minimum finite float (not -inf)",
       np.all(plm[:15, 0] == np.finfo(plm.dtype).min))
yb2 = (Xc[:, 0] > 0).astype(int)
df = cross_val_predict(LogisticRegression(max_iter=2000), Xc, yb2, cv=KFold(3), method="decision_function")
report("cross_val_predict(method='decision_function') on a binary target returns shape (n_samples,)", df.shape == (45,))
report("cross_val_predict with overlapping (non-partition) splits raises ValueError ('only works for partitions')",
       raises(lambda: cross_val_predict(LinearRegression(), Xc, Xc[:, 0], cv=ShuffleSplit(3, random_state=0))) == "ValueError")

# ---------------------------------------------------------------------------------------------------------------
section("learning_curve / validation_curve")
Xl = np.column_stack([np.arange(103), rs.randn(103)]); yl = Xl[:, 1] * 3 + rs.randn(103)
sizes_abs, trs, tes = learning_curve(LinearRegression(), Xl, yl, cv=KFold(5), train_sizes=[0.1, 0.33, 0.5, 1.0])
first_train = 103 - 21; max_train = 103 - 20
report("learning_curve float train_sizes -> floor(fraction * n_max), n_max = size of the FIRST fold's training set (82)",
       list(sizes_abs) == [math.floor(F(str(f)) * first_train) for f in (0.1, 0.33, 0.5, 1.0)], f"({list(sizes_abs)})")
report("learning_curve docstring: float train_sizes are 'a fraction of the maximum size of the training set' (KFold(5) on 103: largest training set has 83)",
       sizes_abs[-1] == max_train, f"(train_sizes=1.0 -> {sizes_abs[-1]}; the fraction is taken of the first fold's 82)")
man_tr = np.zeros((4, 5)); man_te = np.zeros((4, 5))
for j, (tr, te) in enumerate(KFold(5).split(Xl)):
    for i, s in enumerate(sizes_abs):
        b0, b = ols_fit(Xl[tr[:s]], yl[tr[:s]]); man_tr[i, j] = r2_np(yl[tr[:s]], b0 + Xl[tr[:s]] @ b); man_te[i, j] = r2_np(yl[te], b0 + Xl[te] @ b)
report("learning_curve scores: fit on train[:n] (prefix of the fold's training indices), train score on that subset, test on the fold", np.allclose(trs, man_tr, rtol=1e-8) and np.allclose(tes, man_te, rtol=1e-8))
(sa, wa) = caught(lambda: learning_curve(LinearRegression(), Xl, yl, cv=KFold(5), train_sizes=[0.01, 0.02, 0.5])[0], RuntimeWarning)
report("learning_curve: tiny fractions clipped to 1 sample and duplicates removed with a RuntimeWarning", list(sa) == [1, 41] and len(wa) >= 1, f"({list(sa)})")
sa2 = learning_curve(LinearRegression(), Xl, yl, cv=KFold(5), train_sizes=[30, 5, 82])[0]
report("learning_curve integer train_sizes are absolute and returned sorted", list(sa2) == [5, 30, 82])
report("learning_curve integer train_size above n_max (first fold) raises ValueError", raises(lambda: learning_curve(LinearRegression(), Xl, yl, cv=KFold(5), train_sizes=[83])) == "ValueError")
PLOG.clear()
s1, tr1, te1 = learning_curve(MeanReg(), Xl, yl, cv=KFold(5), train_sizes=[10, 25, 60], exploit_incremental_learning=True)
s2, tr2, te2 = learning_curve(MeanReg(), Xl, yl, cv=KFold(5), train_sizes=[10, 25, 60])
report("learning_curve(exploit_incremental_learning=True): partial_fit on consecutive chunks 10, 15, 35 per fold", PLOG == [10, 15, 35] * 5, f"({PLOG[:3]})")
report("learning_curve incremental scores equal refitting on train[:n] (running mean = prefix mean)", np.allclose(tr1, tr2, rtol=1e-10) and np.allclose(te1, te2, rtol=1e-10))
LOG.clear()
learning_curve(RecReg(), Xl, yl, cv=KFold(5), train_sizes=[7, 40], shuffle=True, random_state=11)
r = np.random.RandomState(11); exp = []
for tr, te in KFold(5).split(Xl):
    p = r.permutation(tr); exp += [tuple(sorted(p[:7].tolist())), tuple(sorted(p[:40].tolist()))]
report("learning_curve(shuffle=True, random_state=11): each fold's training indices permuted by one RandomState(11) in fold order, prefixes taken",
       [ids for ids, _ in LOG] == exp)
rt = learning_curve(LinearRegression(), Xl, yl, cv=KFold(5), train_sizes=[20, 50], return_times=True)
report("learning_curve(return_times=True): 5 outputs, fit/score times of shape (n_ticks, n_folds)", len(rt) == 5 and rt[3].shape == (2, 5) and rt[4].shape == (2, 5))
vtr, vte = validation_curve(Ridge(), Xl[:, 1:], yl, param_name="alpha", param_range=[0.1, 10.0, 1000.0], cv=KFold(4))
man = np.zeros((3, 4)); mant = np.zeros((3, 4))
for i, al in enumerate([0.1, 10.0, 1000.0]):
    for j, (tr, te) in enumerate(KFold(4).split(Xl)):
        x = Xl[tr, 1]; yy = yl[tr]; xc = x - x.mean(); w_ = (xc @ (yy - yy.mean())) / (xc @ xc + al); b0 = yy.mean() - w_ * x.mean()
        man[i, j] = r2_np(yl[te], b0 + w_ * Xl[te, 1]); mant[i, j] = r2_np(yy, b0 + w_ * x)
report("validation_curve(Ridge, alpha in [0.1, 10, 1000]): scores shape (3 params, 4 folds) = closed-form ridge per fold (test and train)",
       vte.shape == (3, 4) and np.allclose(vte, man, rtol=1e-8) and np.allclose(vtr, mant, rtol=1e-8))

# ---------------------------------------------------------------------------------------------------------------
section("permutation_test_score with groups")
Xp = np.column_stack([np.arange(24), rs.randn(24)]); yp = np.arange(24, dtype=float) * 10; gp = np.repeat([5, 1, 3], 8); rs.shuffle(gp)
LOG.clear(); allidx = np.arange(24)
permutation_test_score(RecReg(), Xp, yp, groups=gp, cv=[(allidx, allidx)], n_permutations=6, random_state=21)
seen = [np.array(yy) for _, yy in LOG]
report("permutation_test_score(groups=...): 'y values are permuted among samples with the same group identifier' (6 permutations)",
       all(sorted(s[gp == g].tolist()) == sorted(yp[gp == g].tolist()) for s in seen[1:] for g in (1, 3, 5)) and any(not np.array_equal(s, yp) for s in seen[1:]))
r = np.random.RandomState(21); exp = []
for _ in range(6):
    idx = np.arange(24)
    for g in np.unique(gp):
        m_ = gp == g; idx[m_] = r.permutation(idx[m_])
    exp.append(yp[idx])
report("permutation_test_score(groups, random_state=21): within-group permutations drawn group by group (sorted labels) from one RandomState",
       all(np.array_equal(a, b) for a, b in zip(seen[1:], exp)))
sc, ps_, pv = permutation_test_score(LinearRegression(), Xp[:, 1:], Xp[:, 1] + rs.randn(24) * 0.1, groups=gp, cv=GroupKFold(3), n_permutations=19, random_state=0)
report("permutation_test_score p-value with groups = (C+1)/(n_permutations+1)", close(pv, (np.sum(ps_ >= sc) + 1) / 20, 1e-12), f"(score {sc:.4f}, p {pv:.4f})")

# ===============================================================================================================
section("ParameterGrid / ParameterSampler")
pg = ParameterGrid({"b": [1, 2], "a": ["x", "y", "z"]})
exp = [{"a": a, "b": b} for a in ["x", "y", "z"] for b in [1, 2]]
report("ParameterGrid: keys sorted, last key varies fastest (a outer, b inner); len = 6", list(pg) == exp and len(pg) == 6)
report("ParameterGrid[i] == list(grid)[i] for every i; out of range raises IndexError",
       all(pg[i] == exp[i] for i in range(6)) and raises(lambda: pg[6]) == "IndexError")
pg2 = ParameterGrid([{"k": ["lin"]}, {"k": ["rbf"], "g": [1, 2, 3]}, {}])
report("ParameterGrid(list of dicts incl. {}): grids concatenated in order, {} yields one empty setting, len = 1 + 3 + 1",
       list(pg2) == [{"k": "lin"}, {"g": 1, "k": "rbf"}, {"g": 2, "k": "rbf"}, {"g": 3, "k": "rbf"}, {}] and len(pg2) == 5 and pg2[4] == {})
psamp = list(ParameterSampler({"a": [1, 2], "b": stats.expon()}, n_iter=4, random_state=np.random.RandomState(0)))
rnd = [{k: round(v, 6) for k, v in d.items()} for d in psamp]
report("ParameterSampler docstring example ({'a': [1, 2], 'b': expon()}, n_iter=4, RandomState(0))",
       rnd == [{"b": 0.89856, "a": 1}, {"b": 0.923223, "a": 1}, {"b": 1.878964, "a": 2}, {"b": 1.038159, "a": 2}], f"({rnd})")
space = {"p": [1, 2, 3, 4], "q": ["u", "v", "w"]}
sam = list(ParameterSampler(space, n_iter=9, random_state=3))
report("ParameterSampler, all lists: sampling WITHOUT replacement (9 distinct settings from the 12-point grid)",
       len(sam) == 9 and len({tuple(sorted(d.items())) for d in sam}) == 9 and all(d in list(ParameterGrid(space)) for d in sam))
(sam2, ws) = caught(lambda: list(ParameterSampler(space, n_iter=20, random_state=3)), UserWarning)
report("ParameterSampler, all lists, n_iter > grid size: returns the whole grid once, with a UserWarning", len(sam2) == 12 and len({tuple(sorted(d.items())) for d in sam2}) == 12 and len(ws) >= 1)
dist = {"c": stats.uniform(0, 5), "a": [10, 20, 30]}
sam3 = list(ParameterSampler(dist, n_iter=6, random_state=8))
r = np.random.RandomState(8); exp = []
for _ in range(6):
    d = r.choice([dist]); ex = {}
    for k_ in sorted(d):
        v = d[k_]; ex[k_] = v.rvs(random_state=r) if hasattr(v, "rvs") else v[r.randint(len(v))]
    exp.append(ex)
report("ParameterSampler with a distribution: with replacement; dict chosen, then keys in sorted order, lists by randint, distributions by rvs (replicated draws)",
       all(a["a"] == b["a"] and close(a["c"], b["c"], 1e-15) for a, b in zip(sam3, exp)))
report("len(ParameterSampler) = min(n_iter, grid) for lists, n_iter with distributions",
       len(ParameterSampler(space, n_iter=20)) == 12 and len(ParameterSampler(dist, n_iter=20)) == 20)

# ---------------------------------------------------------------------------------------------------------------
section("RandomizedSearchCV / multi-metric GridSearchCV / ranks")
Xs_ = rs.randn(60, 2); ys_ = (Xs_[:, 0] + rs.randn(60) * 0.8 > 0).astype(int)
rsc = RandomizedSearchCV(LogisticRegression(max_iter=2000), {"C": stats.loguniform(1e-3, 1e2), "fit_intercept": [True, False]}, n_iter=7, cv=3, random_state=8).fit(Xs_, ys_)
r = np.random.RandomState(8); exp = []
dd = {"C": stats.loguniform(1e-3, 1e2), "fit_intercept": [True, False]}
for _ in range(7):
    d = r.choice([dd]); ex = {}
    for k_ in sorted(d):
        v = d[k_]; ex[k_] = v.rvs(random_state=r) if hasattr(v, "rvs") else v[r.randint(len(v))]
    exp.append(ex)
report("RandomizedSearchCV(n_iter=7, random_state=8): 7 candidates = the replicated draws (distribution + list)",
       len(rsc.cv_results_["params"]) == 7 and all(close(a["C"], b["C"], 1e-15) and a["fit_intercept"] == b["fit_intercept"] for a, b in zip(rsc.cv_results_["params"], exp)))
rs_l = RandomizedSearchCV(LogisticRegression(max_iter=2000), {"C": [0.01, 0.1, 1, 10]}, n_iter=10, cv=3, random_state=0)
(rs_l, wl) = caught(lambda: rs_l.fit(Xs_, ys_), UserWarning)
report("RandomizedSearchCV with only lists and n_iter > grid: each of the 4 settings evaluated exactly once",
       sorted(p["C"] for p in rs_l.cv_results_["params"]) == [0.01, 0.1, 1, 10])
pick = lambda cvr: int(np.argmin(cvr["mean_test_score"]))
rcal = RandomizedSearchCV(LogisticRegression(max_iter=2000), {"C": [0.001, 0.1, 10]}, n_iter=3, cv=3, refit=pick, random_state=0).fit(Xs_, ys_)
report("RandomizedSearchCV(refit=callable): best_index_ = the callable's return value, best_params_ = params[best_index_]",
       rcal.best_index_ == pick(rcal.cv_results_) and rcal.best_params_ == rcal.cv_results_["params"][rcal.best_index_])
report("refit=callable: 'the best_score_ attribute will not be available'", not hasattr(rcal, "best_score_"))
gdum = GridSearchCV(DummyClassifier(), {"strategy": ["most_frequent", "prior", "uniform"], "random_state": [0]}, cv=3).fit(Xs_, ys_)
means = gdum.cv_results_["mean_test_score"]; ranks = gdum.cv_results_["rank_test_score"]
exp_rank = [1 + sum(1 for m in means if m > x) for x in means]
report("rank_test_score: tied means share the MIN rank (most_frequent = prior -> 1, 1, then 3)", list(ranks) == exp_rank and exp_rank[0] == exp_rank[1], f"(means {np.round(means, 4)}, ranks {list(ranks)})")
gnan = GridSearchCV(DummyClassifier(), {"strategy": ["most_frequent", "constant", "uniform"], "random_state": [0]}, cv=3, error_score=np.nan)
(gnan, wn) = caught(lambda: gnan.fit(Xs_, ys_), FitFailedWarning)
mt = gnan.cv_results_["mean_test_score"]; rk = gnan.cv_results_["rank_test_score"]
report("error_score=nan: the failing candidate (strategy='constant' without constant) has mean nan and FitFailedWarning",
       np.isnan(mt[1]) and not np.isnan(mt[0]) and len(wn) >= 1)
report("error_score=nan: failed candidates are ranked last ('tied with the worst performers'), best_index_ is a valid candidate",
       rk[1] == 3 and gnan.best_index_ != 1, f"(ranks {list(rk)}, best_index_ {gnan.best_index_})")
Xm = rs.randn(80, 3); ym = (Xm[:, 0] + Xm[:, 1] * 0.5 + rs.randn(80) > 0).astype(int)
gm = GridSearchCV(LogisticRegression(max_iter=2000), {"C": [0.001, 0.01, 1.0, 100.0]}, cv=KFold(4), scoring={"acc": "accuracy", "nll": "neg_log_loss"}, refit="nll", return_train_score=True).fit(Xm, ym)
man = {"acc": np.zeros((4, 4)), "nll": np.zeros((4, 4))}
for i, C in enumerate([0.001, 0.01, 1.0, 100.0]):
    for j, (tr, te) in enumerate(KFold(4).split(Xm)):
        m = LogisticRegression(C=C, max_iter=2000).fit(Xm[tr], ym[tr]); pr = m.predict_proba(Xm[te])[:, 1]
        man["acc"][i, j] = np.mean((pr > 0.5).astype(int) == ym[te]); man["nll"][i, j] = np.mean(ym[te] * np.log(pr) + (1 - ym[te]) * np.log(1 - pr))
report("multi-metric GridSearchCV: split<i>_test_acc / _nll and mean_test_* recomputed per fold",
       all(np.allclose(gm.cv_results_[f"split{j}_test_{s}"], man[s][:, j], rtol=1e-8) for s in ("acc", "nll") for j in range(4))
       and np.allclose(gm.cv_results_["mean_test_nll"], man["nll"].mean(1), rtol=1e-8))
report("multi-metric GridSearchCV(refit='nll'): best_index_ = argmax mean_test_nll, best_score_ = that mean (not accuracy)",
       gm.best_index_ == int(np.argmax(man["nll"].mean(1))) and close(gm.best_score_, man["nll"].mean(1).max(), 1e-8) and "rank_test_acc" in gm.cv_results_ and "mean_train_nll" in gm.cv_results_)
g_nr = GridSearchCV(LogisticRegression(max_iter=2000), {"C": [0.1, 1.0]}, cv=3, scoring={"acc": "accuracy", "f1": "f1"}, refit=False).fit(Xm, ym)
report("multi-metric with refit=False: no best_estimator_ / best_index_ exposed", not hasattr(g_nr, "best_estimator_") and not hasattr(g_nr, "best_index_"))
report("multi-metric with refit=True raises ValueError (must name a scorer or be callable)",
       raises(lambda: GridSearchCV(LogisticRegression(), {"C": [1.0]}, cv=3, scoring={"acc": "accuracy", "f1": "f1"}, refit=True).fit(Xm, ym)) == "ValueError")

# ---------------------------------------------------------------------------------------------------------------
section("successive halving schedules")
Xh = np.zeros((12, 1)); yh = np.zeros(12)
H = lambda n_cand, **kw: HalvingGridSearchCV(Toy(), {"a": list(np.linspace(0, 1, n_cand))}, resource="budget", cv=KFold(2), refit=False, **kw).fit(Xh, yh)
h70 = H(70, factor=2, min_resources=3, max_resources=96)
print("   70 candidates, min_resources=3, factor=2: n_resources_", h70.n_resources_, "n_candidates_", h70.n_candidates_)
report("user guide table: n_resources_i = factor**i * min_resources = 3, 6, 12, 24, 48, 96", h70.n_resources_ == [3, 6, 12, 24, 48, 96])
report("user guide table: n_candidates_{i+1} = n_candidates_i // factor = 70, 35, 17, 8, 4, 2", h70.n_candidates_ == [70, 35, 17, 8, 4, 2],
       f"(got {h70.n_candidates_}: the code keeps ceil(n_candidates / factor))")
report("n_remaining_candidates_ = ceil(n_candidates_[-1] / factor) (attribute docstring)", h70.n_remaining_candidates_ == math.ceil(F(h70.n_candidates_[-1], 2)))
ok = all(h70.n_candidates_[i + 1] == math.ceil(F(h70.n_candidates_[i], 2)) for i in range(len(h70.n_candidates_) - 1))
report("successive candidates = ceil(previous / factor) (consistent with n_remaining_candidates_ and the aggressive-elimination example)", ok)
it0 = np.asarray(h70.cv_results_["iter"]); prm = np.asarray(h70.cv_results_["params"])
kept = all(set(p["a"] for p in prm[it0 == i + 1]) == set(sorted((p["a"] for p in prm[it0 == i]), reverse=True)[:h70.n_candidates_[i + 1]]) for i in range(len(h70.n_candidates_) - 1))
report("each iteration keeps the top-scoring candidates of the previous one (cv_results_['iter'])", kept)
h6 = H(6, factor=2, min_resources=20, max_resources=40)
report("user-guide aggressive_elimination example, False: n_resources_ [20, 40], n_candidates_ [6, 3]", h6.n_resources_ == [20, 40] and h6.n_candidates_ == [6, 3])
h6a = H(6, factor=2, min_resources=20, max_resources=40, aggressive_elimination=True)
report("user-guide aggressive_elimination example, True: n_resources_ [20, 20, 40], n_candidates_ [6, 3, 2]", h6a.n_resources_ == [20, 20, 40] and h6a.n_candidates_ == [6, 3, 2])
report("n_iterations_ = min(n_possible, n_required) without, = n_required with aggressive_elimination",
       h6.n_iterations_ == min(h6.n_possible_iterations_, h6.n_required_iterations_) and h6a.n_iterations_ == h6a.n_required_iterations_ == 3 and h6.n_possible_iterations_ == 2)
h6b = H(6, factor=2, min_resources=20, max_resources=1000)
report("user-guide example, min_resources=20 and 1000 available: n_resources_ [20, 40, 80]", h6b.n_resources_ == [20, 40, 80])
h6e = H(6, factor=2, min_resources="exhaust", max_resources=1000)
report("user-guide example, min_resources='exhaust': n_resources_ [250, 500, 1000] (last iteration uses as much as possible)", h6e.n_resources_ == [250, 500, 1000])
h9e = H(9, factor=3, min_resources="exhaust", max_resources=1000)
report("min_resources='exhaust' (9 candidates, factor 3, 1000): r0 = 1000 // 3**2 = 111; last = 999 = the highest value <= 1000 that is a multiple of 111 and 3",
       h9e.min_resources_ == 111 and h9e.n_resources_ == [111, 333, 999])
h_sm = H(5, factor=3, min_resources="smallest", max_resources=50)
report("min_resources='smallest' with resource != 'n_samples' -> 1", h_sm.min_resources_ == 1 and h_sm.n_resources_[0] == 1)
Xh3 = rs.randn(150, 2); yh3 = rs.randint(0, 3, 150)
hc = HalvingGridSearchCV(LogisticRegression(max_iter=500), {"C": [0.1, 1.0]}, cv=3, min_resources="smallest", refit=False).fit(Xh3, yh3)
hr = HalvingGridSearchCV(Ridge(), {"alpha": [0.1, 1.0]}, cv=3, min_resources="smallest", refit=False).fit(Xh3, Xh3[:, 0])
report("min_resources='smallest', resource='n_samples': n_classes * n_splits * 2 = 18 for a 3-class classifier, n_splits * 2 = 6 for a regressor",
       hc.min_resources_ == 18 and hr.min_resources_ == 6, f"({hc.min_resources_}, {hr.min_resources_})")
hf = H(12, factor=1.5, min_resources=4, max_resources=100)
print("   factor=1.5, min_resources=4: n_resources_", hf.n_resources_)
report("min_resources docstring: 'the amount of resources used at each iteration is always a multiple of min_resources' (factor=1.5 is allowed: 'int or float')",
       all(v % 4 == 0 for v in hf.n_resources_), f"(n_resources_ {hf.n_resources_})")
h243 = H(243, factor=3, min_resources=1, max_resources=243)
print("   243 candidates, factor 3, min 1, max 243: n_candidates_", h243.n_candidates_, "n_resources_", h243.n_resources_,
      "n_required", h243.n_required_iterations_, "n_possible", h243.n_possible_iterations_)
report("n_required_iterations_ for 243 = 3**5 candidates, factor 3: 6 iterations (243, 81, 27, 9, 3, 1) to end with fewer than factor candidates",
       h243.n_required_iterations_ == 6, f"(got {h243.n_required_iterations_}: 1 + floor(log(243, 3)) with math.log(243, 3) = {math.log(243, 3)!r})")
report("n_possible_iterations_ with min 1, max 243 = 3**5, factor 3: 6 (resources 1, 3, 9, 27, 81, 243 all <= max_resources)",
       h243.n_possible_iterations_ == 6, f"(got {h243.n_possible_iterations_})")
report("n_required_iterations_ docstring: the last iteration evaluates fewer than `factor` candidates (243 candidates)",
       h243.n_candidates_[-1] < 3, f"(last iteration evaluated {h243.n_candidates_[-1]} candidates)")
hre = HalvingRandomSearchCV(Toy(), {"a": stats.uniform(0, 1)}, n_candidates="exhaust", resource="budget", min_resources=4, max_resources=100, factor=3, cv=KFold(2), refit=False, random_state=0).fit(Xh, yh)
report("HalvingRandomSearchCV(n_candidates='exhaust'): first iteration samples max_resources_ // min_resources_ = 25 candidates", hre.n_candidates_[0] == 25 and hre.n_resources_[0] == 4)
report("HalvingRandomSearchCV: n_candidates_ and n_resources_ follow the same ceil / factor**i schedule",
       hre.n_candidates_ == [25, 9, 3] and hre.n_resources_ == [4, 12, 36], f"({hre.n_candidates_}, {hre.n_resources_})")
hb = HalvingGridSearchCV(Toy(), {"a": [0.9, 0.1, 0.5, 0.3]}, resource="budget", min_resources=1, max_resources=8, factor=2, cv=KFold(2)).fit(Xh, yh)
last = np.flatnonzero(np.asarray(hb.cv_results_["iter"]) == max(hb.cv_results_["iter"]))
report("Halving best_index_ / best_params_ / best_score_: best of the LAST iteration", hb.best_index_ in last and hb.best_params_["a"] == 0.9 and close(hb.best_score_, 0.9))
report("Halving: resource parameter injected in the candidates' params with that iteration's amount (cv_results_['n_resources'])",
       all(p["budget"] == nr for p, nr in zip(hb.cv_results_["params"], hb.cv_results_["n_resources"])))
# resource = n_samples: subsampling and random_state
Xn = np.column_stack([np.arange(90), rs.randn(90)]); yn = rs.randn(90)
tr_sizes = {}
for seed in (0, 1):
    LOG.clear()
    hs = HalvingGridSearchCV(RecReg(), {"a": [0, 1, 2, 3]}, factor=2, min_resources=30, cv=KFold(3), refit=False, random_state=seed).fit(Xn, yn)
    tr_sizes[seed] = [ids for ids, _ in LOG]
exp_sizes = [int(nr / 90 * 60) for nr in hs.n_resources_ for _ in range(hs.n_candidates_[hs.n_resources_.index(nr)] * 3)]
report("resource='n_samples': each fold trains on int(n_resources_i / n_samples * |train fold|) samples (subsample drawn inside every training fold)",
       [len(t) for t in tr_sizes[1]] == exp_sizes, f"(n_resources_ {hs.n_resources_}, first training sizes {[len(t) for t in tr_sizes[1]][:3]})")
report("Halving random_state docstring: 'used for subsampling the dataset when resources != n_samples. Ignored otherwise'",
       tr_sizes[0] == tr_sizes[1], "(with resource='n_samples', random_state 0 vs 1 changes the training subsamples)")
report("Halving: cv yielding different folds on each split() call is refused (ValueError)",
       raises(lambda: HalvingGridSearchCV(Toy(), {"a": [0, 1]}, resource="budget", max_resources=4, cv=KFold(2, shuffle=True)).fit(Xh, yh)) == "ValueError")

# ===============================================================================================================
section("TunedThresholdClassifierCV / FixedThresholdClassifier")
if V >= (1, 5):
    from sklearn.model_selection import TunedThresholdClassifierCV, FixedThresholdClassifier
    Xt = rs.randn(160, 3); yt = (Xt[:, 0] + 0.7 * Xt[:, 1] + rs.randn(160) * 1.2 > 0.9).astype(int)

    def bal_acc(yv, pv):
        tp = sum(1 for a, b in zip(yv, pv) if a == 1 and b == 1); tn = sum(1 for a, b in zip(yv, pv) if a == 0 and b == 0)
        P = sum(1 for a in yv if a == 1); N = len(yv) - P
        return float((F(tp, P) + F(tn, N)) / 2)

    tt = TunedThresholdClassifierCV(LogisticRegression(max_iter=2000), store_cv_results=True).fit(Xt, yt)
    fold_thr = []; fold_sc = []
    for tr, te in StratifiedKFold(5).split(Xt, yt):
        m = LogisticRegression(max_iter=2000).fit(Xt[tr], yt[tr]); s = m.predict_proba(Xt[te])[:, 1]
        th = np.linspace(s.min(), s.max(), 100); fold_thr.append(th)
        fold_sc.append(np.array([bal_acc(yt[te], (s >= t).astype(int)) for t in th]))
    grid = np.linspace(min(t.min() for t in fold_thr), max(t.max() for t in fold_thr), 100)
    curve = np.mean([np.interp(grid, t, s_) for t, s_ in zip(fold_thr, fold_sc)], 0)
    bi = int(np.argmax(curve))
    print(f"   best threshold {tt.best_threshold_:.6f} (recomputed {grid[bi]:.6f}), best balanced accuracy {tt.best_score_:.6f} ({curve[bi]:.6f})")
    report("TunedThresholdClassifierCV default: 5-fold stratified, 100 thresholds per fold, balanced accuracy at score >= t, folds linearly interpolated on a common grid and averaged (recomputed)",
           np.allclose(tt.cv_results_["thresholds"], grid, rtol=1e-12) and np.allclose(tt.cv_results_["scores"], curve, rtol=1e-12, atol=1e-12))
    report("TunedThresholdClassifierCV: best_threshold_ / best_score_ = argmax of the stored curve (first maximum)",
           tt.best_threshold_ == tt.cv_results_["thresholds"][np.argmax(tt.cv_results_["scores"])] and tt.best_score_ == np.max(tt.cv_results_["scores"]) and close(tt.best_threshold_, grid[bi], 1e-12))
    full = LogisticRegression(max_iter=2000).fit(Xt, yt)
    report("TunedThresholdClassifierCV (refit=True): estimator_ refit on all data, predict = 1 where predict_proba >= best_threshold_",
           np.allclose(tt.estimator_.coef_, full.coef_, rtol=1e-6) and np.array_equal(tt.predict(Xt), (full.predict_proba(Xt)[:, 1] >= tt.best_threshold_).astype(int)))
    tt2 = TunedThresholdClassifierCV(LogisticRegression(max_iter=2000), thresholds=[0.2, 0.4, 0.6], cv=0.3, random_state=1, store_cv_results=True).fit(Xt, yt)
    tr, te = next(StratifiedShuffleSplit(1, test_size=0.3, random_state=1).split(Xt, yt))
    m = LogisticRegression(max_iter=2000).fit(Xt[tr], yt[tr]); s = m.predict_proba(Xt[te])[:, 1]
    sc3 = [bal_acc(yt[te], (s >= t).astype(int)) for t in (0.2, 0.4, 0.6)]
    report("TunedThresholdClassifierCV(cv=0.3, thresholds=[.2,.4,.6]): one stratified 30% validation split; scores at exactly the given thresholds",
           np.allclose(tt2.cv_results_["scores"], sc3, rtol=1e-12) and tt2.best_threshold_ == [0.2, 0.4, 0.6][int(np.argmax(sc3))], f"({sc3})")
    report("TunedThresholdClassifierCV: refit=False with several folds raises ValueError; cv='prefit' with refit=True raises ValueError",
           raises(lambda: TunedThresholdClassifierCV(LogisticRegression(), cv=3, refit=False).fit(Xt, yt)) == "ValueError"
           and raises(lambda: TunedThresholdClassifierCV(full, cv="prefit", refit=True).fit(Xt, yt)) == "ValueError")
    ttp = TunedThresholdClassifierCV(full, cv="prefit", refit=False, thresholds=[0.3, 0.5], store_cv_results=True).fit(Xt[:80], yt[:80])
    s = full.predict_proba(Xt[:80])[:, 1]
    report("TunedThresholdClassifierCV(cv='prefit', refit=False): the given fitted estimator scored on the fit data, unchanged",
           ttp.estimator_ is full and np.allclose(ttp.cv_results_["scores"], [bal_acc(yt[:80], (s >= t).astype(int)) for t in (0.3, 0.5)]))
    ft = FixedThresholdClassifier(LogisticRegression(max_iter=2000), threshold=0.3).fit(Xt, yt)
    report("FixedThresholdClassifier(threshold=0.3): predict = classes_[predict_proba[:, 1] >= 0.3]", np.array_equal(ft.predict(Xt), (full.predict_proba(Xt)[:, 1] >= 0.3).astype(int)))
    ftd = FixedThresholdClassifier(LogisticRegression(max_iter=2000), threshold=-0.5, response_method="decision_function").fit(Xt, yt)
    report("FixedThresholdClassifier(response_method='decision_function', threshold=-0.5)", np.array_equal(ftd.predict(Xt), (full.decision_function(Xt) >= -0.5).astype(int)))
    ftp = FixedThresholdClassifier(LogisticRegression(max_iter=2000), threshold=0.3, pos_label=0).fit(Xt, yt)
    report("FixedThresholdClassifier(pos_label=0, threshold=0.3): predict 0 where P(y=0) >= 0.3", np.array_equal(ftp.predict(Xt), np.where(full.predict_proba(Xt)[:, 0] >= 0.3, 0, 1)))
    ys = np.array(["no", "yes"])[yt]
    fts = FixedThresholdClassifier(LogisticRegression(max_iter=2000), threshold=0.6, pos_label="yes").fit(Xt, ys)
    report("FixedThresholdClassifier with string classes and pos_label='yes'", np.array_equal(fts.predict(Xt), np.where(full.predict_proba(Xt)[:, 1] >= 0.6, "yes", "no")))
    lr0 = LogisticRegression().fit(np.array([[-1.0], [1.0], [-2.0], [2.0]]), [0, 1, 0, 1])
    lr0.coef_[:] = 1.0; lr0.intercept_[:] = 0.0
    fa = FixedThresholdClassifier(lr0, threshold="auto").fit(np.array([[-1.0], [1.0], [-2.0], [2.0]]), [0, 1, 0, 1])
    fa.estimator_.coef_[:] = 1.0; fa.estimator_.intercept_[:] = 0.0
    xt0 = np.array([[0.0], [0.5], [-0.5]])
    print("   P(y=1|x=0) =", lr0.predict_proba(xt0)[0, 1], " base predict", lr0.predict(xt0).tolist(), " FixedThreshold(auto)", fa.predict(xt0).tolist())
    report("FixedThresholdClassifier(threshold='auto') reproduces the estimator's default cut-off ('0.5 ... i.e. the default threshold'; user guide: positive when P > 0.5)",
           fa.predict(xt0).tolist() == lr0.predict(xt0).tolist(), f"(at P = 0.5 exactly: base predict {lr0.predict(xt0)[0]}, FixedThresholdClassifier {fa.predict(xt0)[0]} -- it uses >=)")
else:
    print("   TunedThresholdClassifierCV / FixedThresholdClassifier not available before 1.5 -- skipped")

# ===============================================================================================================
section("chi2 / r_regression / f_regression(center=False)")
Xd = np.array([[1, 1, 3], [0, 1, 5], [5, 4, 1], [6, 6, 2], [1, 4, 0], [0, 0, 0]]); yd_ = np.array([1, 1, 0, 0, 2, 2])
c2, p2 = chi2(Xd, yd_)
num_ok = lambda got, want: all(abs(g - float(w)) < 10.0 ** -len(w.split(".")[1]) for g, w in zip(got, want))
report("chi2 docstring example: stats [15.3, 6.5, 8.9], p [0.000456, 0.0387, 0.0116] (doctest NUMBER precision)",
       num_ok(c2, ["15.3", "6.5", "8.9"]) and num_ok(p2, ["0.000456", "0.0387", "0.0116"]), f"({c2}, {p2})")


def chi2_exact(X, y):
    classes = sorted(set(y)); n = len(y); out = []
    for j in range(len(X[0])):
        tot = sum(F(int(r[j])) for r in X); st = F(0)
        for c in classes:
            O = sum(F(int(X[i][j])) for i in range(n) if y[i] == c); E = F(sum(1 for v in y if v == c), n) * tot
            st += (O - E) ** 2 / E
        pv = mpmath.gammainc(mpf(len(classes) - 1) / 2, mpf(st.numerator) / st.denominator / 2, mpmath.inf, regularized=True)
        out.append((st, float(pv)))
    return out


Xcnt = rs.poisson(3, size=(50, 5)); Xcnt[:, 2] += rs.poisson(4, 50) * (np.arange(50) % 3 == 0); ycnt = np.arange(50) % 3
ex = chi2_exact(Xcnt.tolist(), ycnt.tolist()); c2, p2 = chi2(Xcnt, ycnt)
report("chi2 = sum_c (O_c - E_c)^2 / E_c with O_c = feature total in class c, E_c = class share * feature total (Fraction), df = n_classes - 1 (mpmath gammainc)",
       all(close(a, float(s), 1e-12) and close(b, pv, 1e-9, 1e-300) for a, b, (s, pv) in zip(c2, p2, ex)), f"(stats {np.round(c2, 4)})")
c2s, p2s = chi2(sp.csr_matrix(Xcnt), ycnt)
report("chi2 on a CSR matrix = dense result", np.allclose(c2s, c2, rtol=1e-12) and np.allclose(p2s, p2, rtol=1e-12))
ybin = (np.arange(50) % 2); exb = chi2_exact(Xcnt.tolist(), ybin.tolist()); c2b, p2b = chi2(Xcnt, ybin)
report("chi2 with a binary target: both classes counted (df = 1)", all(close(a, float(s), 1e-12) and close(b, pv, 1e-9) for a, b, (s, pv) in zip(c2b, p2b, exb)))
report("chi2 with a negative value raises ValueError ('Input X must be non-negative')", raises(lambda: chi2(np.array([[1, -1], [2, 3]]), [0, 1])) == "ValueError")
Xq = rs.randn(30, 4); yq = Xq[:, 0] * 2 + rs.randn(30)
Xq[:, 3] = 5.0


def pearson_exact(x, y, center=True):
    x = [F(float(v)) for v in x]; y = [F(float(v)) for v in y]
    if center:
        mx = sum(x) / len(x); my = sum(y) / len(y); x = [v - mx for v in x]; y = [v - my for v in y]
    num = sum(a * b for a, b in zip(x, y)); den = sum(a * a for a in x) * sum(b * b for b in y)
    if den == 0: return None
    return float(mpf(num.numerator) / num.denominator / mpmath.sqrt(mpf(den.numerator) / den.denominator))


rr = r_regression(Xq, yq)
report("r_regression = Pearson r (exact Fraction sums) per feature", all(close(rr[j], pearson_exact(Xq[:, j], yq), 1e-12) for j in range(3)))
report("r_regression force_finite=True: a constant feature (all 5.0) 'will be forced to a minimal correlation of 0.0'", rr[3] == 0.0, f"(got {rr[3]})")
rr2 = r_regression(Xq, yq, force_finite=False)
report("r_regression(force_finite=False): constant feature (all 5.0) -> nan ('a correlation of np.nan is returned')", np.isnan(rr2[3]), f"(got {rr2[3]})")
Xk = np.column_stack([Xq[:, :3], np.full(30, 0.1)])
report("r_regression constant feature 0.1: 0.0 with force_finite, nan without", r_regression(Xk, yq)[3] == 0.0 and np.isnan(r_regression(Xk, yq, force_finite=False)[3]))
rru = r_regression(Xq[:, :3], yq, center=False)
report("r_regression(center=False) = uncentred cosine x.y / (|x||y|)", all(close(rru[j], pearson_exact(Xq[:, j], yq, center=False), 1e-12) for j in range(3)))
fu, pu = f_regression(Xq[:, :3], yq, center=False)
ok = True
for j in range(3):
    r_ = mpf(pearson_exact(Xq[:, j], yq, center=False)); dof = 29; Fv = r_ ** 2 / (1 - r_ ** 2) * dof
    pvv = mpmath.betainc(mpf(dof) / 2, mpf(1) / 2, 0, dof / (dof + Fv), regularized=True)
    ok &= close(fu[j], float(Fv), 1e-11) and close(pu[j], float(pvv), 1e-9)
report("f_regression(center=False): F = r_unc^2/(1-r_unc^2) * (n-1), p = F(1, n-1) upper tail (mpmath betainc)", ok, f"(F {np.round(fu, 4)})")
n_out = 0; n_bad = 0; first_bad = None; n_neg = 0; n_fin = 0
for seed in range(50):
    yy = np.random.RandomState(1000 + seed).randn(30)
    rp = r_regression(np.column_stack([yy, -2 * yy]), yy); fp_, pp_ = f_regression(np.column_stack([yy, -2 * yy]), yy)
    n_out += int(np.any(np.abs(rp) > 1))
    if not (np.all(fp_ == np.finfo(fp_.dtype).max) and np.all(pp_ == 0)):
        n_bad += 1; first_bad = first_bad if first_bad is not None else (seed, rp.tolist(), fp_.tolist(), pp_.tolist())
        n_neg += int(np.any(fp_ < 0)); n_fin += int(np.all(fp_ > 0) and np.any(fp_ < np.finfo(fp_.dtype).max))
print(f"   50 random targets y (n=30): |r_regression([y, -2y], y)| > 1 in {n_out}; f_regression not (finfo.max, p=0) in {n_bad}"
      f" (negative F with p = 1 in {n_neg}, finite positive F < finfo.max in {n_fin}); first: {first_bad}")
report("r_regression of features y and -2y against y lies in [-1, 1] (f_regression docstring: 'r_regression values lie in [-1, 1]'; 50 random y)", n_out == 0, f"(|r| > 1 for {n_out} of 50 targets)")
report("f_regression force_finite=True: a perfectly (anti-)correlated feature gets F = finfo.max and p-value 0.0 (50 random y)",
       n_bad == 0, f"({n_bad} of 50 targets violate it; e.g. seed {first_bad[0]}: F {first_bad[2]}, p {first_bad[3]})" if first_bad else "")
fc, pc = f_regression(np.column_stack([yq, Xq[:, 3]]), yq)
report("f_regression force_finite=True: constant feature -> F = 0.0, p-value 1.0", fc[1] == 0 and pc[1] == 1)
yb_ = np.random.RandomState(1000 + (first_bad[0] if first_bad else 0)).randn(30)
kb = SelectKBest(f_regression, k=1).fit(np.column_stack([np.random.RandomState(7).randn(30), yb_]), yb_).get_support()
report("SelectKBest(f_regression, k=1) picks a feature equal to y over a pure-noise feature", kb.tolist() == [False, True], f"(support {kb.tolist()})")

# ---------------------------------------------------------------------------------------------------------------
section("SelectKBest / SelectPercentile / SelectFpr / SelectFdr / SelectFwe / GenericUnivariateSelect")


def fixed(scores, pvalues=None):
    s = np.asarray(scores, float); pv = None if pvalues is None else np.asarray(pvalues, float)
    return (lambda X, y: (s, pv)) if pv is not None else (lambda X, y: s)


Xz = rs.randn(10, 8); yz = rs.randn(10)
sc = [3.0, 1.0, 3.0, 2.0, 3.0, 0.5, 2.0, 1.0]
m = SelectKBest(fixed(sc), k=2).fit(Xz, yz).get_support()
report("SelectKBest(k=2) with a 3-way tie at the top: exactly 2 features, all from the tied maximum ('ties broken in an unspecified way')",
       m.sum() == 2 and set(np.flatnonzero(m)) <= {0, 2, 4}, f"(selected {np.flatnonzero(m).tolist()})")
m = SelectKBest(fixed(sc), k=5).fit(Xz, yz).get_support()
report("SelectKBest(k=5): every selected score >= every rejected score", m.sum() == 5 and min(np.array(sc)[m]) >= max(np.array(sc)[~m]))
report("SelectKBest(k='all') keeps all, k=0 keeps none", SelectKBest(fixed(sc), k="all").fit(Xz, yz).get_support().all() and not SelectKBest(fixed(sc), k=0).fit(Xz, yz).get_support().any())
if V >= (1, 5):
    (skb, wk) = caught(lambda: SelectKBest(fixed(sc), k=12).fit(Xz, yz), UserWarning)
    report("SelectKBest(k > n_features): all features returned, with a warning (1.5+ behaviour)", skb.get_support().all() and len(wk) >= 1)
else:
    report("SelectKBest(k > n_features) raises ValueError (behaviour before the 1.5-era change to a warning)", raises(lambda: SelectKBest(fixed(sc), k=12).fit(Xz, yz)) == "ValueError")
m = SelectKBest(fixed([np.nan, 1.0, 2.0, 0.1, 5.0, 3.0, 4.0, 2.5]), k=7).fit(Xz, yz).get_support()
report("SelectKBest: a NaN score ranks below every real score", not m[0] and m.sum() == 7)


def pct_linear(vals, q):
    v = sorted(F(x) for x in vals); pos = F(q) / 100 * (len(v) - 1); lo = math.floor(pos)
    return v[lo] if lo + 1 >= len(v) else v[lo] + (pos - lo) * (v[lo + 1] - v[lo])


def percentile_ref(scores, p):
    n = len(scores); thr = pct_linear(scores, 100 - p); mask = [F(s) > thr for s in scores]
    ties = [i for i, s in enumerate(scores) if F(s) == thr]; mx = int(n * p / 100)
    for i in ties[:max(0, mx - sum(mask))]: mask[i] = True
    return mask


dist_sc = list(rs.permutation(np.arange(1.0, 21.0)))
bad = []; counts = {}
for p in (5, 10, 13, 25, 30, 33, 50, 62.5, 99):
    got = SelectPercentile(fixed(dist_sc), percentile=p).fit(Xz[:, :1].repeat(20, 1), yz).get_support()
    exp = percentile_ref(dist_sc, p); counts[p] = int(got.sum())
    if list(got) != exp or not (math.floor(F(20) * F(str(p)) / 100) <= got.sum() <= math.ceil(F(20) * F(str(p)) / 100)): bad.append(p)
print("   SelectPercentile on 20 distinct scores, features kept per percentile:", counts)
report("SelectPercentile, distinct scores: keeps scores > the linear (100-p)th percentile; count within floor/ceil of p% of n (9 percentiles)", not bad, f"({bad})")
tie_sc = [1.0, 2.0, 2.0, 2.0, 2.0, 3.0, 4.0, 2.0]
got = SelectPercentile(fixed(tie_sc), percentile=50).fit(Xz, yz).get_support()
report("SelectPercentile(50) with ties at the threshold: ties added only up to int(n * p / 100) = 4 features",
       got.sum() == 4 and got[5] and got[6] and list(got) == percentile_ref(tie_sc, 50), f"(selected {np.flatnonzero(got).tolist()})")
report("SelectPercentile(100) keeps all, (0) keeps none (even with NaN scores)",
       SelectPercentile(fixed([np.nan] + sc[1:]), percentile=100).fit(Xz, yz).get_support().all() and not SelectPercentile(fixed(sc), percentile=0).fit(Xz, yz).get_support().any())
pv = np.array([0.001, 0.049, 0.05, 0.2, 0.011, 0.0125, 0.03, 0.9])
report("SelectFpr(alpha=0.05): 'Features with p-values less than alpha' (strict: p = 0.05 rejected)",
       list(SelectFpr(fixed(sc, pv), alpha=0.05).fit(Xz, yz).get_support()) == list(pv < 0.05))
report("SelectFwe(alpha=0.05): Bonferroni p < alpha / n_features = 0.00625",
       list(SelectFwe(fixed(sc, pv), alpha=0.05).fit(Xz, yz).get_support()) == [True] + [False] * 7)


def bh_ref(p, alpha):
    m = len(p); order = sorted(range(m), key=lambda i: F(p[i])); kmax = 0
    for r_, i in enumerate(order, 1):
        if F(p[i]) <= F(alpha) * r_ / m: kmax = r_
    if kmax == 0: return [False] * m
    cut = F(p[order[kmax - 1]]); return [F(v) <= cut for v in p]


ok = True
for trial in range(40):
    pvr = rs.uniform(0, 0.2, 12) ** 2
    ok &= list(SelectFdr(fixed(np.ones(12), pvr), alpha=0.05).fit(Xz[:, :1].repeat(12, 1), yz).get_support()) == bh_ref(pvr.tolist(), 0.05)
report("SelectFdr = Benjamini-Hochberg step-up: largest k with p_(k) <= k*alpha/m, keep all p <= p_(k) (exact Fraction reference, 40 random sets)", ok)
pvh = np.array([0.001, 0.0376, 0.04, 0.041, 0.9])   # p_(2)=0.0376 > 2*0.05/5=0.02 but p_(4)=0.041 > 0.04... step-up picks k=1..
pvh = np.array([0.001, 0.021, 0.0295, 0.039, 0.9])  # 0.021 > 0.02 (k=2 fails) but 0.039 <= 0.04 (k=4 passes)
got = SelectFdr(fixed(np.ones(5), pvh), alpha=0.05).fit(Xz[:, :5], yz).get_support()
report("SelectFdr step-UP: p_(2) = 0.021 above its bound 0.02 is still kept because p_(4) = 0.039 <= 0.04",
       list(got) == [True, True, True, True, False] == bh_ref(pvh.tolist(), 0.05))
found = None
for m_ in range(3, 60):
    for k_ in range(1, m_ + 1):
        ex_ = F(0.05) * k_ / m_; fl = float(ex_)
        if F(fl) > ex_: fl = float(np.nextafter(fl, 0))
        if (0.05 / m_) * k_ < fl: found = (m_, k_, fl); break
    if found: break
if found:
    m_, k_, fl = found
    pvb = np.array([fl * (i + 1) / k_ * 0.999 if i < k_ - 1 else fl for i in range(k_)] + [0.99] * (m_ - k_))
    got = SelectFdr(fixed(np.ones(m_), pvb), alpha=0.05).fit(np.zeros((3, m_)), [0, 1, 2]).get_support()
    report(f"SelectFdr at the exact BH boundary (m={m_} p-values, the largest p_({k_}) = {fl!r} = {k_}*alpha/m exactly, others below their bounds): BH keeps all {k_}",
           list(got) == bh_ref(pvb.tolist(), 0.05), f"(kept {int(got.sum())}, exact BH keeps {sum(bh_ref(pvb.tolist(), 0.05))}: bound computed as (alpha/m)*k = {(0.05 / m_) * k_!r} < p = {fl!r})")
gus = {"percentile": (SelectPercentile, "percentile", 25), "k_best": (SelectKBest, "k", 3), "fpr": (SelectFpr, "alpha", 0.05),
       "fdr": (SelectFdr, "alpha", 0.05), "fwe": (SelectFwe, "alpha", 0.05)}
ok = True
for mode, (cls, pn, val) in gus.items():
    ok &= np.array_equal(GenericUnivariateSelect(fixed(sc, pv), mode=mode, param=val).fit(Xz, yz).get_support(), cls(fixed(sc, pv), **{pn: val}).fit(Xz, yz).get_support())
report("GenericUnivariateSelect(mode, param) = the corresponding selector with that parameter (5 modes)", ok)
report("GenericUnivariateSelect default (percentile, param=1e-5) keeps only the top-scoring feature", GenericUnivariateSelect(fixed([1.0, 5.0, 2.0])).fit(Xz[:, :3], yz).get_support().tolist() == [False, True, False])
e = raises(lambda: GenericUnivariateSelect(fixed(sc), mode="k_best", param=3.0).fit(Xz, yz).get_support())
report("GenericUnivariateSelect(mode='k_best', param=3.0): docstring 'param : \"all\", float or int' -> 3 features", e is None, f"(raises {e})" if e else "")

# ---------------------------------------------------------------------------------------------------------------
section("mutual_info_regression / continuous mutual_info_classif (KSG / Ross recomputed, documented noise replicated)")
nm = 120
Xmi = rs.randn(nm, 3); Xmi[:, 1] = Xmi[:, 0] ** 2 + 0.3 * rs.randn(nm); ymi = np.sin(Xmi[:, 0] * 2) + 0.2 * rs.randn(nm)
Xmi[:, 2] = np.round(Xmi[:, 2] * 2)   # repeated values: the noise is what breaks the ties
got = mutual_info_regression(Xmi, ymi, random_state=4)
Xn_, yn_ = mi_noise(Xmi, ymi, np.array([True, True, True]), False, 4)
exp = [ksg_ref(Xn_[:, j].tolist(), yn_.tolist(), 3) for j in range(3)]
print("   mutual_info_regression", np.round(got, 6).tolist(), " KSG reference", np.round(exp, 6).tolist())
report("mutual_info_regression (n_neighbors=3) = KSG estimator on the scaled + 1e-10-noised data (plain-Python max-norm neighbour counts, mpmath digamma)",
       np.allclose(got, exp, rtol=1e-9, atol=1e-12))
got5 = mutual_info_regression(Xmi, ymi, n_neighbors=5, random_state=4)
exp5 = [ksg_ref(Xn_[:, j].tolist(), yn_.tolist(), 5) for j in range(3)]
report("mutual_info_regression(n_neighbors=5) = KSG with k = 5", np.allclose(got5, exp5, rtol=1e-9, atol=1e-12))
ycl = (Xmi[:, 0] > 0.3).astype(int) + (Xmi[:, 0] > 1.0).astype(int); ycl[:1] = 5   # a singleton class -> dropped
gotc = mutual_info_classif(Xmi, ycl, random_state=6)
Xn2, _ = mi_noise(Xmi, ycl, np.array([True, True, True]), True, 6)
expc = [ross_ref(Xn2[:, j].tolist(), ycl.tolist(), 3) for j in range(3)]
print("   mutual_info_classif", np.round(gotc, 6).tolist(), " Ross reference", np.round(expc, 6).tolist())
report("mutual_info_classif continuous features = Ross (2014) estimator (k-th neighbour within class, m counted in the full data, singleton class dropped)",
       np.allclose(gotc, expc, rtol=1e-9, atol=1e-12))
xdisc = rs.randint(0, 4, nm); Xmix = np.column_stack([Xmi[:, 0], xdisc])
gotm = mutual_info_regression(Xmix, ymi + xdisc, discrete_features=[1], random_state=2)
Xn3, yn3 = mi_noise(Xmix, ymi + xdisc, np.array([True, False]), False, 2)
expm = [ksg_ref(Xn3[:, 0].tolist(), yn3.tolist(), 3), ross_ref(yn3.tolist(), xdisc.tolist(), 3)]
report("mutual_info_regression(discrete_features=[1]): discrete column scored with Ross (continuous target vs discrete feature)", np.allclose(gotm, expm, rtol=1e-9, atol=1e-12))
report("mutual_info_* are clipped at 0 ('A negative value will be replaced by 0')", np.all(mutual_info_regression(rs.randn(60, 4), rs.randn(60), random_state=0) >= 0))
report("mutual_info_regression with the same random_state is reproducible; X is not modified (copy=True)",
       np.array_equal(mutual_info_regression(Xmi, ymi, random_state=4), got) and np.array_equal(Xmi[:, 2], np.round(Xmi[:, 2])))

# ---------------------------------------------------------------------------------------------------------------
section("VarianceThreshold")
Xv = np.array([[0.0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3.0]])
vt = VarianceThreshold().fit(Xv)
report("VarianceThreshold docstring example: keeps columns 1 and 2 (constant columns removed)", list(vt.get_support(indices=True)) == [1, 2] and vt.transform(Xv).tolist() == [[2, 0], [1, 4], [1, 1]])
Xv2 = rs.randn(12, 4) * [1, 3, 0.5, 2]
vt2 = VarianceThreshold(threshold=1.0).fit(Xv2)
exact_var = [float(sum((F(float(v)) - sum(F(float(u)) for u in Xv2[:, j]) / 12) ** 2 for v in Xv2[:, j]) / 12) for j in range(4)]
report("VarianceThreshold(threshold=1.0).variances_ = population variance (ddof=0) of each column", np.allclose(vt2.variances_, exact_var, rtol=1e-12))
Xbig = np.array([[0.0, 1.0], [10.0, 2.0], [0.0, 3.0], [10.0, 4.0]])
vt0 = VarianceThreshold().fit(Xbig)
report("VarianceThreshold() (threshold=0) variances_ 'Variances of individual features' = [25, 1.25]", np.allclose(vt0.variances_, [25.0, 1.25]),
       f"(got {vt0.variances_.tolist()}: with threshold=0 the attribute is min(variance, peak-to-peak))")
Xeq = np.array([[0.0, 0.0], [1.0, 5.0], [0.0, 0.0], [1.0, 5.0]])
vte = VarianceThreshold(threshold=0.25).fit(Xeq)
report("VarianceThreshold docstring: 'Features with a training-set variance lower than this threshold will be removed' (variance exactly 0.25 = threshold is kept)",
       vte.get_support().tolist() == [True, True], f"(support {vte.get_support().tolist()}: the code keeps variance > threshold)")
Xnan = np.array([[1.0, np.nan], [3.0, 2.0], [np.nan, 2.0], [5.0, 4.0]])
vtn = VarianceThreshold(threshold=0.5).fit(Xnan)
report("VarianceThreshold with NaN: variances_ computed ignoring NaN (nanvar)", np.allclose(vtn.variances_, [np.var([1, 3, 5]), np.var([2, 2, 4])]))
report("VarianceThreshold: no feature above the threshold raises ValueError", raises(lambda: VarianceThreshold(threshold=100).fit(Xv2)) == "ValueError")
vts = VarianceThreshold(threshold=0.5).fit(sp.csr_matrix(Xv2))
report("VarianceThreshold on sparse input = dense variances", np.allclose(vts.variances_, exact_var, rtol=1e-10))

# ---------------------------------------------------------------------------------------------------------------
section("RFE / RFECV")
Xf = rs.randn(60, 9); beta = np.array([5, -4, 3, 2.5, -2, 1.5, 1, 0.5, 0.2]); yf = Xf @ beta + rs.randn(60) * 0.5


def rfe_ref(X, y, n_sel, step, score=None):
    nf = X.shape[1]; sup = np.ones(nf, bool); rank = np.ones(nf, int); hist = []
    while sup.sum() > n_sel:
        feats = np.flatnonzero(sup); _, b = ols_fit(X[:, feats], y)
        if score: hist.append((len(feats), score(feats)))
        order = np.argsort(b ** 2, kind="stable"); thr = min(step, sup.sum() - n_sel)
        sup[feats[order[:thr]]] = False; rank[~sup] += 1
    if score: hist.append((int(sup.sum()), score(np.flatnonzero(sup))))
    return sup, rank, hist


for n_sel, step in [(3, 1), (4, 2), (2, 3), (None, 1)]:
    rfe = RFE(LinearRegression(), n_features_to_select=n_sel, step=step).fit(Xf, yf)
    s_, rk_, _ = rfe_ref(Xf, yf, 9 // 2 if n_sel is None else n_sel, step)
    report(f"RFE(n_features_to_select={n_sel}, step={step}): support_ and ranking_ = reference elimination on squared OLS coefficients",
           np.array_equal(rfe.support_, s_) and np.array_equal(rfe.ranking_, rk_), f"(ranking {rfe.ranking_.tolist()})")
rfe = RFE(LinearRegression(), n_features_to_select=3, step=1).fit(Xf, yf)
report("RFE ranking_: selected features rank 1, the first eliminated gets the largest rank (n_features - n_selected + 1 = 7)",
       sorted(rfe.ranking_.tolist()) == [1, 1, 1, 2, 3, 4, 5, 6, 7])
rfe = RFE(LinearRegression(), n_features_to_select=0.5, step=0.25).fit(Xf, yf)
s_, rk_, _ = rfe_ref(Xf, yf, int(9 * 0.5), int(max(1, 0.25 * 9)))
report("RFE float n_features_to_select=0.5 -> int(4.5) = 4; float step=0.25 -> int(2.25) = 2 per iteration ('rounded down')",
       rfe.n_features_ == 4 and np.array_equal(rfe.ranking_, rk_))
Xw = rs.randn(150, 100); yw = Xw[:, :10] @ rs.randn(10) + rs.randn(150)
rfe29 = RFE(LinearRegression(), n_features_to_select=71, step=0.29).fit(Xw, yw)
report("RFE(step=0.29) on 100 features: 'percentage (rounded down)' of 100 -> removes 29 features at the first iteration",
       rfe29.n_features_ == 71 and rfe29.ranking_.max() == 2, f"(first iteration removes {int((rfe29.ranking_ == rfe29.ranking_.max()).sum())} features, a second one removes {int((rfe29.ranking_ == 2).sum())} to reach 71; 0.29*100 = {0.29 * 100!r})")
class FixedCoef(RegressorMixin, BaseEstimator):
    """coef_ = W restricted to the columns it is given (row 0 of X carries the original feature ids)."""
    def __init__(self, W=None):
        self.W = W

    def fit(self, X, y):
        self.coef_ = np.asarray(self.W)[:, np.asarray(X)[0].astype(int)]; return self

    def predict(self, X):
        return np.zeros(len(X))


W2 = np.array([[1.0, -3.0, 0.5, 2.0, 0.1, -1.2], [2.0, 0.2, -0.4, 0.1, 0.3, 1.5]])
Xid6 = np.vstack([np.arange(6.0), rs.randn(9, 6)])
rfe2 = RFE(FixedCoef(W2), n_features_to_select=2, step=1).fit(Xid6, np.zeros(10))
imp2d = (W2 ** 2).sum(0); exp_rank = np.empty(6, int); exp_rank[np.argsort(imp2d)] = np.array([5, 4, 3, 2, 1, 1])
report("RFE with a 2-D coef_ (multi-output/multiclass): importance = sum over rows of coef^2 (hand-set coefficients)",
       np.array_equal(rfe2.ranking_, exp_rank), f"(ranking {rfe2.ranking_.tolist()}, sum of squares {imp2d.tolist()})")
rfe3 = RFE(FixedCoef(W2), n_features_to_select=2, importance_getter=lambda est: np.abs(est.coef_[1])).fit(Xid6, np.zeros(10))
report("RFE(importance_getter=callable): elimination follows the callable's importances (|row 1|)", sorted(rfe3.get_support(indices=True).tolist()) == [0, 5])
report("RFE: estimator_ is refit on the selected features; transform keeps those columns",
       np.allclose(rfe.estimator_.coef_, ols_fit(Xf[:, rfe.support_], yf)[1], rtol=1e-8) and np.array_equal(rfe.transform(Xf), Xf[:, rfe.support_]))
# RFECV
folds = list(KFold(3).split(Xf))
for step, mn in [(1, 1), (3, 2), (4, 3)]:
    rcv = RFECV(LinearRegression(), step=step, min_features_to_select=mn, cv=KFold(3)).fit(Xf, yf)
    per = []
    for tr, te in folds:
        _, _, hist = rfe_ref(Xf[tr], yf[tr], mn, step, score=lambda feats, tr=tr, te=te: r2_np(yf[te], ols_fit(Xf[tr][:, feats], yf[tr])[0] + Xf[te][:, feats] @ ols_fit(Xf[tr][:, feats], yf[tr])[1]))
        per.append(hist)
    nfeat = [h[0] for h in per[0]][::-1]; S = np.array([[h[1] for h in p][::-1] for p in per])
    best_n = nfeat[int(np.argmax(S.sum(0)))]
    ok = rcv.n_features_ == best_n and np.allclose(rcv.cv_results_["mean_test_score"], S.mean(0), rtol=1e-9) and np.allclose(rcv.cv_results_["std_test_score"], S.std(0), rtol=1e-7, atol=1e-12) \
        and all(np.allclose(rcv.cv_results_[f"split{i}_test_score"], S[i], rtol=1e-9) for i in range(3))
    if "n_features" in rcv.cv_results_: ok &= list(rcv.cv_results_["n_features"]) == nfeat
    report(f"RFECV(step={step}, min_features_to_select={mn}): feature counts {nfeat}, cv_results_ (mean/std/split) and n_features_ = argmax of summed fold R^2 (reference)",
           ok, f"(n_features_ {rcv.n_features_}, reference {best_n})")
const = lambda est, X, y: 1.0
rcc = RFECV(LinearRegression(), step=2, min_features_to_select=3, cv=KFold(3), scoring=const).fit(Xf, yf)
report("RFECV tie rule: when all feature counts score equally the SMALLEST count (min_features_to_select = 3) is chosen", rcc.n_features_ == 3)
rsel = RFE(LinearRegression(), n_features_to_select=rcv.n_features_, step=4).fit(Xf, yf)
report("RFECV: final support_ / ranking_ = RFE(n_features_to_select=n_features_) on all data", np.array_equal(rcv.support_, rsel.support_) and np.array_equal(rcv.ranking_, rsel.ranking_))

# ---------------------------------------------------------------------------------------------------------------
section("SelectFromModel")
Xsf = rs.randn(40, 6); ysf = Xsf @ np.array([3, -1, 0.2, 0.05, 2, -0.5]) + rs.randn(40) * 0.1
pre = LinearRegression().fit(Xsf, ysf); pre.coef_ = np.array([3.0, -1.0, 0.2, 0.05, 2.0, -0.5]); imp = np.abs(pre.coef_)
cases = {"mean": imp.mean(), "median": np.median(imp), "1.5*mean": 1.5 * imp.mean(), "0.5*median": 0.5 * np.median(imp), 0.5: 0.5}
bad = []
for thr, val in cases.items():
    sfm = SelectFromModel(pre, threshold=thr, prefit=True)
    if list(sfm.get_support()) != list(imp >= val): bad.append(thr)
report("SelectFromModel(prefit=True) thresholds 'mean', 'median', '1.5*mean', '0.5*median', 0.5: keep |coef| >= threshold (hand-set coefficients)", not bad, f"({bad})")
sfm = SelectFromModel(pre, threshold=1.0, prefit=True).fit(Xsf, ysf)
report("SelectFromModel(prefit=True).fit does not refit (hand-set coef_ preserved in estimator_), threshold_ = 1.0",
       np.array_equal(sfm.estimator_.coef_, pre.coef_) and sfm.threshold_ == 1.0 and list(sfm.get_support()) == list(imp >= 1.0))
sfm = SelectFromModel(pre, threshold=-np.inf, max_features=3, prefit=True).fit(Xsf, ysf)
report("SelectFromModel(threshold=-inf, max_features=3): the 3 largest |coef|", sorted(sfm.get_support(indices=True).tolist()) == [0, 1, 4])
sfm = SelectFromModel(pre, threshold="mean", max_features=4, prefit=True).fit(Xsf, ysf)
report("SelectFromModel(max_features=4, threshold='mean'): both limits apply (top-4 AND >= mean)", list(sfm.get_support()) == list((imp >= imp.mean()) & np.isin(np.arange(6), [0, 1, 4, 5])))
sfm = SelectFromModel(pre, threshold=-np.inf, max_features=lambda X: X.shape[1] // 3, prefit=True).fit(Xsf, ysf)
report("SelectFromModel(max_features=callable): max_features_ = callable(X) = 2", sfm.max_features_ == 2 and sfm.get_support().sum() == 2)
Xmc = rs.randn(90, 5); ymc = rs.randint(0, 3, 90)
lrm = LogisticRegression(max_iter=2000).fit(Xmc, ymc)
Cf = np.array([[1.0, -2.0, 0.1, 0.0, 3.0], [0.5, 0.5, -0.1, 0.0, -3.0], [-2.0, 1.0, 0.2, 0.3, 0.0]]); lrm.coef_ = Cf
bad = []
for order, fn in [(1, lambda c: np.abs(c).sum(0)), (2, lambda c: np.sqrt((c ** 2).sum(0))), (np.inf, lambda c: np.abs(c).max(0))]:
    sfm = SelectFromModel(lrm, threshold="mean", norm_order=order, prefit=True)
    s_ = fn(Cf)
    if list(sfm.get_support()) != list(s_ >= s_.mean()) or not close(sfm.fit(Xmc, ymc).threshold_, s_.mean()): bad.append(order)
report("SelectFromModel norm_order 1 / 2 / inf on a 2-D coef_: importance = column norm of that order, threshold 'mean' of those", not bad, f"({bad})")
sfm = SelectFromModel(pre, threshold=1.0, prefit=True, importance_getter=lambda est: np.array([0, 0, 5, 5, 0, 0.0]))
report("SelectFromModel(importance_getter=callable) overrides coef_", list(sfm.get_support()) == [False, False, True, True, False, False])
from sklearn.pipeline import Pipeline
pl = Pipeline([("lr", LinearRegression())]).fit(Xsf, ysf)
sfm = SelectFromModel(pl, threshold="mean", prefit=True, importance_getter="named_steps.lr.coef_")
imp2 = np.abs(pl.named_steps["lr"].coef_)
report("SelectFromModel(importance_getter='named_steps.lr.coef_') (attrgetter path)", list(sfm.get_support()) == list(imp2 >= imp2.mean()))
las = SelectFromModel(Lasso(alpha=0.05)).fit(Xsf, ysf)
lr_ = SelectFromModel(LinearRegression()).fit(Xsf, ysf)
report("SelectFromModel threshold=None: 1e-5 for Lasso (l1), 'mean' for LinearRegression",
       las.threshold_ == 1e-5 and close(lr_.threshold_, np.abs(lr_.estimator_.coef_).mean(), 1e-12) and list(las.get_support()) == list(np.abs(las.estimator_.coef_) >= 1e-5))
en = SelectFromModel(ElasticNetCV(l1_ratio=1.0, cv=3)).fit(Xf, yf)
impe = np.abs(en.estimator_.coef_); used = impe[en.get_support()].min() if en.get_support().any() else None
print(f"   ElasticNetCV(l1_ratio=1.0): threshold_ = {en.threshold_:.6g}, mean |coef| = {impe.mean():.6g}, features kept = {int(en.get_support().sum())} (>= 1e-5: {int((impe >= 1e-5).sum())}, >= mean: {int((impe >= impe.mean()).sum())})")
report("SelectFromModel(ElasticNetCV(l1_ratio=1.0)): threshold_ ('Threshold value used for feature selection') is the threshold get_support applies",
       list(en.get_support()) == list(impe >= en.threshold_), "" if list(en.get_support()) == list(impe >= en.threshold_) else f"(threshold_ {en.threshold_:.6g} but support uses {'1e-5' if list(en.get_support()) == list(impe >= 1e-5) else 'mean'})")
sfm = SelectFromModel(LinearRegression(), threshold="mean").fit(Xsf, ysf)
b0_, b_ = ols_fit(Xsf, ysf)
report("SelectFromModel(prefit=False): fits a clone; support from the OLS coefficients (hand-written OLS)", list(sfm.get_support()) == list(np.abs(b_) >= np.abs(b_).mean()))

# ---------------------------------------------------------------------------------------------------------------
section("SequentialFeatureSelector")
Xq2 = rs.randn(50, 6); yq2 = Xq2 @ np.array([2.0, 0, -1.5, 0.3, 0, 1.0]) + rs.randn(50) * 0.8
fq = kfold_ref(list(range(50)), 5)


def sfs_ref(X, y, n_iter, direction, tol=None):
    cur = np.zeros(X.shape[1], bool); old = -np.inf; hist = []
    for _ in range(n_iter):
        best = None
        for j in np.flatnonzero(~cur):
            cm = cur.copy(); cm[j] = True
            if direction == "backward": cm = ~cm
            s = np.mean(ols_cv_r2(X[:, cm], y, fq))
            if best is None or s > best[1]: best = (j, s)
        if tol is not None and best[1] - old < tol: break
        old = best[1]; cur[best[0]] = True; hist.append(best)
    return (~cur if direction == "backward" else cur), hist


s1 = SequentialFeatureSelector(LinearRegression(), n_features_to_select=3, direction="forward", cv=5).fit(Xq2, yq2)
e1, h1 = sfs_ref(Xq2, yq2, 3, "forward")
print("   forward greedy picks (feature, mean CV R^2):", [(int(j), round(s, 5)) for j, s in h1])
report("SFS forward (3 of 6): greedy on mean 5-fold R^2 of hand-written OLS", np.array_equal(s1.get_support(), e1))
s2 = SequentialFeatureSelector(LinearRegression(), n_features_to_select=2, direction="backward", cv=5).fit(Xq2, yq2)
e2, _ = sfs_ref(Xq2, yq2, 4, "backward")
report("SFS backward (keep 2 of 6): removes, 4 times, the feature whose removal leaves the best CV score", np.array_equal(s2.get_support(), e2))
s3 = SequentialFeatureSelector(LinearRegression(), n_features_to_select="auto", tol=0.02, direction="forward", cv=5).fit(Xq2, yq2)
e3, h3 = sfs_ref(Xq2, yq2, 5, "forward", tol=0.02)
report("SFS forward 'auto' with tol=0.02: stops at the first addition improving the score by less than tol; n_features_to_select_ = support size",
       np.array_equal(s3.get_support(), e3) and s3.n_features_to_select_ == e3.sum(), f"(selected {np.flatnonzero(s3.get_support()).tolist()})")
s4 = SequentialFeatureSelector(LinearRegression(), n_features_to_select="auto", tol=-0.01, direction="backward", cv=5).fit(Xq2, yq2)
e4, _ = sfs_ref(Xq2, yq2, 5, "backward", tol=-0.01)
report("SFS backward 'auto' with negative tol=-0.01 (allowed for backward): removal continues while the score drops by less than 0.01", np.array_equal(s4.get_support(), e4))
s5 = SequentialFeatureSelector(LinearRegression(), n_features_to_select="auto", tol=1e9, direction="backward", cv=5).fit(Xq2, yq2)
report("SFS backward 'auto', unreachable tol=1e9: the first removal is always accepted (compared with -inf, not with the all-feature score) -> 5 features",
       s5.get_support().sum() == 5)
Xodd = Xq2[:, :5]
f5 = SequentialFeatureSelector(LinearRegression(), n_features_to_select="auto", direction="forward", cv=5).fit(Xodd, yq2).get_support().sum()
b5 = SequentialFeatureSelector(LinearRegression(), n_features_to_select="auto", direction="backward", cv=5).fit(Xodd, yq2).get_support().sum()
report("SFS n_features_to_select='auto', tol=None: 'half of the features are selected' -- 5 features, forward and backward agree",
       f5 == b5, f"(forward keeps {f5}, backward keeps {b5})")
report("SFS float n_features_to_select=0.5 on 6 features -> 3; n_features_to_select >= n_features raises ValueError",
       SequentialFeatureSelector(LinearRegression(), n_features_to_select=0.5, cv=5).fit(Xq2, yq2).get_support().sum() == 3
       and raises(lambda: SequentialFeatureSelector(LinearRegression(), n_features_to_select=6).fit(Xq2, yq2)) == "ValueError")
if V >= (1, 2):
    report("SFS: 'tol is required to be strictly positive when doing forward selection' (1.2+ docstring) -> ValueError",
           raises(lambda: SequentialFeatureSelector(LinearRegression(), n_features_to_select="auto", tol=-1).fit(Xq2, yq2)) == "ValueError")

# ---------------------------------------------------------------------------------------------------------------
section("SelectorMixin API")
sel = SelectKBest(fixed([1.0, 9.0, 3.0, 7.0, 2.0]), k=2).fit(Xz[:, :5], yz)
report("get_support() boolean mask and get_support(indices=True) = [1, 3]", sel.get_support().tolist() == [False, True, False, True, False] and sel.get_support(indices=True).tolist() == [1, 3])
Xt5 = rs.randn(4, 5)
report("transform keeps the selected columns in order", np.array_equal(sel.transform(Xt5), Xt5[:, [1, 3]]))
inv = sel.inverse_transform(sel.transform(Xt5))
report("inverse_transform puts zeros in the removed columns", inv.shape == (4, 5) and np.array_equal(inv[:, [1, 3]], Xt5[:, [1, 3]]) and np.all(inv[:, [0, 2, 4]] == 0))
report("get_feature_names_out() default names x1, x3; with input_features the selected names",
       list(sel.get_feature_names_out()) == ["x1", "x3"] and list(sel.get_feature_names_out(["a", "b", "c", "d", "e"])) == ["b", "d"])
sels = sel.transform(sp.csr_matrix(Xt5))
report("transform of a sparse matrix stays sparse with the same columns", sp.issparse(sels) and np.array_equal(sels.toarray(), Xt5[:, [1, 3]]))
print("== done")
