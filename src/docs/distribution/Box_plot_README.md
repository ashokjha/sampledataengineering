
# Box Plot

A box plot summarizes the distribution of a numeric variable using its median, quartiles, spread, and potential outliers. It is especially useful for comparing distributions across several groups.

## When to use it

Use a box plot when:

- You want to compare the center and spread of numeric values across groups.
- You need a compact view of distributions with many observations.
- Identifying possible outliers is useful.

Avoid it when the audience needs to see every individual data point or the exact distribution shape. Consider a strip plot, violin plot, or histogram alongside it.

## Python example

Install Matplotlib and NumPy once, if needed:

```bash
python -m pip install matplotlib numpy
```

Save the following as `box_plot.py`, then run `python box_plot.py`. It will open the chart and save a PNG named `box_plot.png` in the current folder.

```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Create reproducible sample delivery times, in minutes, for three regions.
rng = np.random.default_rng(seed=24)
north_times = rng.normal(loc=31, scale=4, size=60)
south_times = rng.normal(loc=36, scale=5, size=60)
west_times = rng.normal(loc=33, scale=3.5, size=60)

# 2. Add two unusually long deliveries so the chart demonstrates outliers.
south_times = np.append(south_times, [53, 56])

# 3. Group the data and matching labels in the same order.
delivery_times = [north_times, south_times, west_times]
regions = ["North", "South", "West"]

# 4. Create a figure and axes for the chart.
fig, ax = plt.subplots(figsize=(8, 5.5))

# 5. Draw the box plot and customize its key visual elements.
#    The box spans the first to third quartile; the central line is the median.
box_plot = ax.boxplot(
    delivery_times,
    tick_labels=regions,
    patch_artist=True,
    medianprops={"color": "#1E3A8A", "linewidth": 2},
    boxprops={"edgecolor": "#2563EB", "linewidth": 1.4},
    whiskerprops={"color": "#2563EB", "linewidth": 1.4},
    capprops={"color": "#2563EB", "linewidth": 1.4},
    flierprops={
        "marker": "o",
        "markerfacecolor": "#F97316",
        "markeredgecolor": "white",
        "markersize": 7,
    },
)

# 6. Fill each box with the same color so all groups read as one measure.
for box in box_plot["boxes"]:
    box.set_facecolor("#BFDBFE")

# 7. Add a title and labels that describe the data and its unit.
ax.set_title("Delivery-Time Distribution by Region", fontsize=16, fontweight="bold", pad=14)
ax.set_xlabel("Region", fontsize=11)
ax.set_ylabel("Delivery time (minutes)", fontsize=11)

# 8. Add a light horizontal grid to support comparisons across groups.
ax.grid(axis="y", color="#D1D5DB", linewidth=0.8, alpha=0.8)
ax.set_axisbelow(True)

# 9. Remove unnecessary borders, save a high-resolution image, and display it.
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("box_plot.png", dpi=200, bbox_inches="tight")
plt.show()
```

## How to read it

- The line inside each box is the median (the middle value).
- The bottom and top of the box are the first and third quartiles; the box contains the middle 50% of values.
- Whiskers extend to the most extreme non-outlier values.
- Individual points beyond the whiskers are potential outliers under the standard 1.5 × IQR rule.

## Key choices

| Element     | Recommendation                                                           |
| ----------- | ------------------------------------------------------------------------ |
| Groups      | Use the same scale for every group.                                      |
| Ordering    | Arrange groups in a meaningful order, such as geography or median value. |
| Outliers    | Keep them visible, but investigate before treating them as errors.       |
| Sample size | Note very small group sizes; their summaries can be unstable.            |
| Detail      | Overlay individual points when sample sizes are small enough to read.    |

## Example output

The code compares delivery times across three regions. South has the highest typical delivery time and two high outliers, while North and West have tighter distributions centered at lower values.
