# Scatter Plot

A scatter plot places one observation at each x-y coordinate to reveal relationships, clusters, and outliers.

## When to use it

- Use it to explore association between two measured variables.
- Avoid it when many points overlap without transparency or aggregation.

## Jupyter notebook

Run the same commented example interactively in [scatter_plot.ipynb](./scatter_plot.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib numpy
```

Save this as `scatter_plot.py`, then run it. The example saves `scatter_plot.png` in the current folder.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create reproducible paired data for ad spend and sales.
rng = np.random.default_rng(seed=4)
ad_spend = rng.uniform(5, 40, 60)
sales = 2.1 * ad_spend + rng.normal(0, 10, 60)

# Draw one point per campaign.
fig, ax = plt.subplots(figsize=(8, 5.5))
ax.scatter(ad_spend, sales, s=60, color="#2563EB", alpha=0.75, edgecolor="white", linewidth=0.7)

# Label, save, and display the figure.
ax.set(title="Sales vs. Advertising Spend", xlabel="Advertising spend (thousands of dollars)", ylabel="Sales (thousands of dollars)")
ax.grid(color="#D1D5DB")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("scatter_plot.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

