# 3D Scatter Plot

A 3D scatter plot places every observation using three numeric coordinates. It can reveal clusters, relationships, and outliers across three variables at once.

## When to use it

- Use it to explore a third numeric dimension when an ordinary scatter plot is insufficient.
- Avoid it for precise comparisons: perspective and point overlap can make values difficult to judge. A 2D scatter plot with color or facets is often clearer.

## Jupyter notebook

Run the same commented example interactively in [scatter_plot_3d.ipynb](./scatter_plot_3d.ipynb).

## Python example

Install Matplotlib and NumPy once:

```bash
python -m pip install matplotlib numpy
```

Save this as `scatter_plot_3d.py`, then run it. The example saves `scatter_plot_3d.png` in the current folder.

```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Create reproducible observations with three numeric dimensions.
rng = np.random.default_rng(seed=21)
ad_spend = rng.uniform(5, 40, 60)
sales_calls = rng.uniform(10, 80, 60)
revenue = 1.8 * ad_spend + 0.45 * sales_calls + rng.normal(0, 8, 60)

# 2. Create a three-dimensional axes object.
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(projection="3d")

# 3. Draw one marker per observation.
#    Color also represents revenue, making high-value observations easy to find.
points = ax.scatter(
    ad_spend,
    sales_calls,
    revenue,
    c=revenue,
    cmap="viridis",
    s=55,
    alpha=0.8,
    edgecolor="white",
    linewidth=0.5,
)

# 4. Add labels, a title, and a color bar explaining the color scale.
ax.set_title("Revenue by Advertising Spend and Sales Calls", fontweight="bold", pad=16)
ax.set_xlabel("Advertising spend (thousands of dollars)")
ax.set_ylabel("Sales calls")
ax.set_zlabel("Revenue (thousands of dollars)")
fig.colorbar(points, ax=ax, pad=0.12, label="Revenue (thousands of dollars)")

# 5. Choose a helpful camera angle, then save and display the chart.
ax.view_init(elev=24, azim=42)
fig.tight_layout()
fig.savefig("scatter_plot_3d.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| View angle | Choose a camera angle that does not hide important clusters. |
| Marker size | Keep points small enough that overlapping observations remain visible. |
| Color | Use color only for a meaningful additional measure. |
| Alternative | Provide a 2D companion chart for precise comparison. |

