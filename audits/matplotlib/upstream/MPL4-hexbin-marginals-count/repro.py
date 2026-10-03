import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt

print("matplotlib", matplotlib.__version__, "numpy", np.__version__)
rng = np.random.default_rng(0)
x, y = rng.standard_normal((2, 600))
fig, ax = plt.subplots()
# no C: "every point has a value of 1"; marginals: "the marginal density"
hb = ax.hexbin(x, y, gridsize=(6, 3), extent=(-4, 4, -4, 4), marginals=True)
xcounts = np.histogram(x, bins=6, range=(-4, 4))[0]  # 6 x strips
ycounts = np.histogram(y, bins=6, range=(-4, 4))[0]  # 2 * 3 y strips
print("hbar observed:", hb.hbar.get_array().tolist())
print("hbar expected:", xcounts[xcounts > 0].astype(float).tolist())
print("vbar observed:", hb.vbar.get_array().tolist())
print("vbar expected:", ycounts[ycounts > 0].astype(float).tolist())
