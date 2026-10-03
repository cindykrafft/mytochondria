import matplotlib
matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cbook

print("matplotlib", matplotlib.__version__, "numpy", np.__version__)
rng = np.random.default_rng(0)
clean = rng.normal(size=40)
# the same 40 values plus three masked ones (50, -50, 3.3)
data = np.ma.masked_array(np.r_[clean, 50.0, -50.0, 3.3],
                          mask=[False] * 40 + [True] * 3)
obs, = cbook.violin_stats(data, quantiles=[[0.25, 0.75]])
exp, = cbook.violin_stats(clean, quantiles=[[0.25, 0.75]])
for key in ["min", "max", "mean", "median", "quantiles"]:
    print(f"{key:9s} observed {obs[key]}  expected {exp[key]}")
fig, ax = plt.subplots()
parts = ax.violinplot(data)
print("violinplot max line at", parts["cmaxes"].get_segments()[0][0][1],
      "expected", clean.max())
