"""SR4 version scope: does `sklearn.decomposition.PCA` accept the `np.matrix`
that scrublet's `pipeline_mean_center` produces (`csc_matrix - np.matrix`)?

Run once per scikit-learn version:
  for v in 1.4.2 1.5.2 1.6.1 1.7.2; do uv venv --python 3.12 venv-skl-$v; . venv-skl-$v/bin/activate;
      uv pip install "scikit-learn==$v" numpy scipy; python sr4_sklearn_versions.py; done
(plus the audit venv with 1.9.0). Output appended to sr4_sklearn_versions.out.
"""

import importlib.metadata as md

import numpy as np
import scipy.sparse as sp
from sklearn.decomposition import PCA

X = sp.csc_matrix(np.random.default_rng(0).poisson(1.0, size=(60, 20)).astype(float))
M = X - X.mean(0)  # exactly what pipeline_mean_center stores in _E_obs_norm
assert isinstance(M, np.matrix)
try:
    PCA(n_components=5, svd_solver="arpack", random_state=0).fit(M)
    print(f"scikit-learn {md.version('scikit-learn')}  numpy {md.version('numpy')}: PCA.fit(np.matrix) OK")
except Exception as e:  # noqa: BLE001
    print(f"scikit-learn {md.version('scikit-learn')}  numpy {md.version('numpy')}: {type(e).__name__}: {str(e)[:70]}")
