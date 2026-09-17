# Clustermap

A clustermap is a heatmap whose rows and columns are reordered by hierarchical clustering to reveal similar groups.

## When to use it

- Use it to explore similarity patterns in a moderately sized numeric matrix.
- Avoid it when the clustering method or distance metric cannot be justified.

## Jupyter notebook

Run the same commented example interactively in [clustermap.ipynb](./clustermap.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib numpy pandas seaborn
```

Save this as `clustermap.py`, then run it. The example saves `clustermap.png` in the current folder.

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Create reproducible feature data, then standardize every feature.
rng = np.random.default_rng(seed=7)
data = pd.DataFrame(rng.normal(size=(12, 5)), index=[f"Customer {n}" for n in range(1, 13)], columns=["Visits", "Orders", "Spend", "Returns", "Support"])
standardized = (data - data.mean()) / data.std()

# Cluster rows and columns, then draw the reordered matrix and dendrograms.
cluster_grid = sns.clustermap(standardized, cmap="vlag", center=0, linewidths=0.5, figsize=(8, 7))

# Add a title, save, and display the clustered heatmap.
cluster_grid.fig.suptitle("Customer Behavior Clusters", y=1.02, fontweight="bold")
cluster_grid.figure.savefig("clustermap.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

