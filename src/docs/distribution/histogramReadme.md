
# Histogram

A histogram shows the distribution of a numeric variable by grouping observations into intervals called bins. The height of each bar represents how many values fall within that interval.

## When to use it

Use a histogram when:

- You want to understand the shape, center, spread, or skew of one numeric variable.
- You need to spot clusters, gaps, or possible outliers.
- You have enough observations for a meaningful distribution.

Avoid it for discrete categories. Use a bar chart for category counts instead.

## Python example

Install Matplotlib and NumPy once, if needed:

```bash
python -m pip install matplotlib numpy
```

Save the following as `histogram.py`, then run `python histogram.py`. It will open the chart and save a PNG named `histogram.png` in the current folder.

```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Create reproducible sample data: 250 delivery times in minutes.
#    A fixed seed ensures the example produces the same data each time it runs.
rng = np.random.default_rng(seed=42)
delivery_times = rng.normal(loc=34, scale=6, size=250)

# 2. Create a figure and axes for the chart.
fig, ax = plt.subplots(figsize=(9, 5.5))

# 3. Draw the histogram.
#    `bins=12` groups the numeric range into 12 equal-width intervals.
#    Matplotlib returns the bar patches, bin counts, and bin edges if you need them.
counts, bin_edges, patches = ax.hist(
    delivery_times,
    bins=12,
    color="#2563EB",
    edgecolor="white",
    linewidth=1.1,
)

# 4. Add a vertical line for the mean to provide a reference point.
mean_time = delivery_times.mean()
ax.axvline(
    mean_time,
    color="#F97316",
    linewidth=2,
    linestyle="--",
    label=f"Mean: {mean_time:.1f} min",
)

# 5. Add a title, labels, and a legend that make the chart self-explanatory.
ax.set_title("Distribution of Delivery Times", fontsize=16, fontweight="bold", pad=14)
ax.set_xlabel("Delivery time (minutes)", fontsize=11)
ax.set_ylabel("Number of deliveries", fontsize=11)
ax.legend(frameon=False)

# 6. Use a zero count baseline and a light horizontal grid.
ax.set_ylim(bottom=0)
ax.grid(axis="y", color="#D1D5DB", linewidth=0.8, alpha=0.8)
ax.set_axisbelow(True)

# 7. Remove unnecessary borders, save a high-resolution image, and display it.
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("histogram.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element       | Recommendation                                                                  |
| ------------- | ------------------------------------------------------------------------------- |
| Bins          | Try a few sensible bin counts; too few hide patterns, while too many add noise. |
| Variable type | Use continuous or ordered numeric values, not category labels.                  |
| Axis labels   | State the measurement unit and make the y-axis meaning clear.                   |
| Comparison    | Use identical bin edges when comparing distributions in separate charts.        |
| Outliers      | Inspect extreme values; they can compress the rest of the distribution.         |

## Example output

The generated delivery times cluster around 34 minutes. The mean reference line helps show the center of the distribution, while the bars reveal how frequently deliveries fall within each time interval.
