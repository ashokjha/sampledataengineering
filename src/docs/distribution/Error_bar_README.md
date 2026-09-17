
# Error Bar Chart

An error bar chart shows a central estimate—commonly a mean—with a vertical or horizontal interval that communicates uncertainty or variation. The interval might represent standard deviation, standard error, a confidence interval, or a measurement range, so it must be labeled clearly.

## When to use it

Use an error bar chart when:

- You need to compare estimates and their uncertainty across categories.
- The meaning of the interval is well-defined and relevant to the audience.
- There are relatively few categories or measurements.

Avoid it when raw data are available and sample sizes are small; showing individual points or a distribution plot can be more informative.

## Python example

Install Matplotlib and NumPy once, if needed:

```bash
python -m pip install matplotlib numpy
```

Save the following as `error_bar_chart.py`, then run `python error_bar_chart.py`. It will open the chart and save a PNG named `error_bar_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Define category names, their mean scores, and 95% confidence-interval widths.
campaigns = ["Email", "Search", "Social", "Referral"]
mean_conversion_rates = [4.8, 6.1, 5.4, 7.0]
confidence_intervals = [0.6, 0.8, 0.5, 0.9]

# 2. Create numeric positions for each category on the x-axis.
x_positions = np.arange(len(campaigns))

# 3. Create a figure and axes for the chart.
fig, ax = plt.subplots(figsize=(8.5, 5.5))

# 4. Draw the mean markers and their uncertainty intervals.
#    `yerr` supplies the distance above and below each mean.
#    `capsize` adds small horizontal caps so interval endpoints are easy to see.
ax.errorbar(
    x_positions,
    mean_conversion_rates,
    yerr=confidence_intervals,
    fmt="o",
    markersize=8,
    color="#2563EB",
    ecolor="#1D4ED8",
    elinewidth=1.8,
    capsize=5,
    capthick=1.8,
    label="Mean ± 95% confidence interval",
)

# 5. Add a faint line to guide the eye across the category estimates.
ax.plot(x_positions, mean_conversion_rates, color="#93C5FD", linewidth=1.5, zorder=0)

# 6. Put category labels at the numeric positions and add exact mean labels.
ax.set_xticks(x_positions, campaigns)
for x, mean in zip(x_positions, mean_conversion_rates):
    ax.annotate(
        f"{mean:.1f}%",
        xy=(x, mean),
        xytext=(0, 12),
        textcoords="offset points",
        ha="center",
        fontsize=10,
        fontweight="bold",
    )

# 7. Add a title, labels, and legend that define the interval.
ax.set_title("Conversion Rate by Marketing Campaign", fontsize=16, fontweight="bold", pad=14)
ax.set_xlabel("Campaign", fontsize=11)
ax.set_ylabel("Mean conversion rate (%)", fontsize=11)
ax.legend(frameon=False, loc="upper left")

# 8. Use a zero baseline and light grid lines for meaningful comparison.
ax.set_ylim(bottom=0)
ax.grid(axis="y", color="#D1D5DB", linewidth=0.8, alpha=0.8)
ax.set_axisbelow(True)

# 9. Remove unnecessary borders, save a high-resolution image, and display it.
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("error_bar_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element          | Recommendation                                                                                     |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Interval meaning | State whether bars show standard deviation, standard error, confidence interval, or another range. |
| Central estimate | Label whether the marker is a mean, median, proportion, or model estimate.                         |
| Sample size      | Report group sample sizes elsewhere when they differ.                                              |
| Scale            | Keep one common axis scale across all categories.                                                  |
| Raw data         | Consider overlaying points when the sample size is small enough to display.                        |

## Example output

The code compares average conversion rates for four campaigns. Referral has the highest estimate at 7.0%, but its relatively wide 95% confidence interval signals greater uncertainty than some other campaign estimates.
