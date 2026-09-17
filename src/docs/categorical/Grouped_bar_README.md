
# Grouped Bar Chart

A grouped bar chart places related bars side by side within each category. It makes it easy to compare multiple series directly—for example, actual versus target sales across regions.

## When to use it

Use a grouped bar chart when:

- You need to compare values across categories and between a small number of series.
- Precise series-to-series comparisons matter more than showing a combined total.
- Every series uses the same measurement unit and scale.

Avoid it when there are many series or categories; the display becomes crowded. A line chart, heatmap, or small multiples may work better.

## Python example

Install Matplotlib once, if needed:

```bash
python -m pip install matplotlib
```

Save the following as `grouped_bar.py`, then run `python grouped_bar.py`. It will open the chart and save a PNG named `grouped_bar_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Define the main categories and values for each series.
regions = ["North", "South", "East", "West"]
actual_sales = [82, 71, 90, 76]
target_sales = [75, 78, 85, 80]

# 2. Create numeric positions for the category groups.
#    NumPy positions let us offset each series evenly within a group.
x = np.arange(len(regions))
bar_width = 0.36

# 3. Create a figure and axes for the chart.
fig, ax = plt.subplots(figsize=(9, 5.5))

# 4. Draw the Actual bars slightly left of each group center.
actual_bars = ax.bar(
    x - bar_width / 2,
    actual_sales,
    width=bar_width,
    label="Actual",
    color="#2563EB",
)

# 5. Draw the Target bars the same distance to the right.
target_bars = ax.bar(
    x + bar_width / 2,
    target_sales,
    width=bar_width,
    label="Target",
    color="#94A3B8",
)

# 6. Put the original region labels at the center of each bar group.
ax.set_xticks(x, regions)

# 7. Add a title, axis labels, and a legend for the two colors.
ax.set_title("Actual vs. Target Sales by Region", fontsize=16, fontweight="bold", pad=14)
ax.set_xlabel("Region", fontsize=11)
ax.set_ylabel("Sales (thousands of dollars)", fontsize=11)
ax.legend(frameon=False, ncols=2, loc="upper left")

# 8. Add a zero baseline and light grid lines for dependable bar comparisons.
ax.set_ylim(bottom=0)
ax.grid(axis="y", color="#D1D5DB", linewidth=0.8, alpha=0.8)
ax.set_axisbelow(True)

# 9. Add the exact value above every bar.
ax.bar_label(actual_bars, padding=3, fontsize=10)
ax.bar_label(target_bars, padding=3, fontsize=10)

# 10. Remove unnecessary borders, adjust spacing, save, and display the chart.
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("grouped_bar_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element      | Recommendation                                                 |
| ------------ | -------------------------------------------------------------- |
| Series count | Keep groups to two or three series when possible.              |
| Bar width    | Leave a visible gap between category groups.                   |
| Order        | Use a meaningful, consistent series order in each group.       |
| Colors       | Assign one distinct color per series and retain it throughout. |
| Baseline     | Begin the y-axis at zero.                                      |

## Example output

The code compares actual and target sales in four regions. East exceeds its target by 5 thousand dollars, while South and West fall short. Because paired bars share the same baseline, each comparison is quick to read.
