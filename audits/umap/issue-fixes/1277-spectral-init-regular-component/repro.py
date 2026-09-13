"""Reproduction for lmcinnes/umap#1277: with random_state set, fits on data that
contains duplicate rows are not identical.

Case A (the issue's shape): 1000 unique rows plus 200 of them repeated 4 more times,
metric="cosine", n_components=5, random_state=42 (as in the report; synthetic data).
Three fits are compared: ARPACK's internal generator is process-wide state, so
which fits coincide depends on what ran before.

Case B (minimal): 200 random points plus 16 exact copies of one far-away point,
n_neighbors=16.  The copies' nearest neighbours are all copies at distance 0, so they
form their own connected component in which every edge has weight 1 (a regular graph).
"""
import warnings
import numpy as np
import umap

warnings.simplefilter("ignore")
print("umap-learn", umap.__version__)


def report(label, model_kwargs, X, n_fits=3):
    fits = [umap.UMAP(**model_kwargs).fit_transform(X) for _ in range(n_fits)]
    same = all(np.array_equal(fits[0], f) for f in fits[1:])
    diff = max(np.abs(fits[0] - f).max() for f in fits[1:])
    print(f"{label}: {n_fits} seeded fits identical: {same} | max |diff| = {diff:.3f}")


rng = np.random.RandomState(0)
base = rng.normal(size=(1000, 50)).astype(np.float32)
X_a = np.vstack([base] + [base[:200]] * 4)
report(
    "A (1000 unique + 200 x 4 duplicates)",
    dict(n_neighbors=15, n_components=5, min_dist=0.0, metric="cosine", random_state=42),
    X_a,
)

X_b = np.vstack([rng.normal(size=(200, 5)), np.full((16, 5), 25.0)])
report("B (16 copies of one point)", dict(n_neighbors=16, random_state=42), X_b)
