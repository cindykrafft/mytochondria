import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

print("matplotlib", matplotlib.__version__, "numpy", np.__version__)
def minimiser(y):  # Byron & Wattenberg 2008, sec. 5.1; layer 0 at the bottom
    dy = np.diff(y, axis=1)
    steps = -(y[:, 1:] * (dy / 2 + np.cumsum(dy, 0) - dy)).sum(0) / y[:, 1:].sum(0)
    return -y[:, 0].sum() / 2 + np.r_[0, np.cumsum(steps)]
def wiggle(g0, y):  # sum over steps and layers of f_i * (slope of midline i)^2
    mid = g0 + np.cumsum(y, axis=0) - y / 2
    return round((y[:, 1:] * np.diff(mid, axis=1) ** 2).sum(), 4)
for y in [[[1, 3], [1, 1]],
          [[1, 1, 2, 3, 3, 2, 1], [1, 2, 3, 5, 4, 2, 2], [2, 1, 1, 1, 2, 4, 6]]]:
    y, n = np.array(y, float), len(y[0])
    colls = plt.figure().subplots().stackplot(range(n), y, baseline="weighted_wiggle")
    g0, exp = colls[0].get_paths()[0].vertices[1:n + 1, 1], minimiser(y)
    print("observed baseline", np.round(g0, 4).tolist(), "wiggle", wiggle(g0, y))
    print("expected baseline", np.round(exp, 4).tolist(), "wiggle", wiggle(exp, y))
    print("  observed == minimiser for the reversed layer order:",
          np.allclose(g0, minimiser(y[::-1])))
