
# Strip / Swarm Plot

Strip and swarm plots show every individual observation in each category. A strip plot uses jitter to reduce overlap; a swarm plot moves points just enough to prevent overlap while preserving their value axis.

## When to use it

Use a strip or swarm plot when:

- You want readers to see the raw observations, not only summary statistics.
- Each category has a small-to-moderate number of data points.
- You need to show clusters, gaps, sample size, or outliers.

Avoid them for very large datasets. Overplotting can make the figure slow or unreadable; use a box plot, violin plot, or density plot instead.

## Python example

Install Matplotlib, NumPy, Pandas, and Seaborn once, if needed:

```bash
python -m pip install matplotlib numpy pandas seaborn
```

Save the following as `strip_swarm_plot.py`, then run `python strip_swarm_plot.py`. Change `plot_kind` to `"strip"` or `"swarm"` to choose the chart style. The script saves a PNG named `strip_swarm_plot.png`.

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Create reproducible sample response times, in hours, for three teams.
rng = np.random.default_rng(seed=35)
support_times = rng.normal(loc=4.8, scale=1.1, size=35)
sales_times = rng.normal(loc=3.9, scale=0.9, size=35)
success_times = rng.normal(loc=4.3, scale=1.0, size=35)

# 2. Put the values into a long-form table for Seaborn.
#    Each row is one observation with its associated team label.
data = pd.DataFrame(
    {
        "Team": ["Support"] * 35 + ["Sales"] * 35 + ["Customer Success"] * 35,
        "Response time (hours)": np.concatenate([support_times, sales_times, success_times]),
    }
)

# 3. Choose the plot style: use "strip" for fast jittered points or
#    "swarm" when avoiding point overlap is more important.
plot_kind = "swarm"

# 4. Create a figure and apply a clean Seaborn theme.
sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(9, 5.5))

# 5. Draw every observation. Both plot types share the same category/value mapping.
if plot_kind == "strip":
    sns.stripplot(
        data=data,
        x="Team",
        y="Response time (hours)",
        jitter=0.22,       # Randomly spreads points horizontally to reduce overlap.
        size=7,
        alpha=0.7,
        color="#2563EB",
        ax=ax,
    )
else:
    sns.swarmplot(
        data=data,
        x="Team",
        y="Response time (hours)",
        size=6,
        color="#2563EB",
        ax=ax,
    )

# 6. Overlay the median for each team as a clear summary reference.
medians = data.groupby("Team", sort=False)["Response time (hours)"].median()
ax.scatter(
    range(len(medians)),
    medians,
    marker="_",
    s=800,
    linewidths=2.5,
    color="#F97316",
    label="Median",
    zorder=3,
)

# 7. Add a title, labels, and legend that describe the comparison.
ax.set_title("First Response Time by Team", fontsize=16, fontweight="bold", pad=14)
ax.set_xlabel("Team", fontsize=11)
ax.set_ylabel("First response time (hours)", fontsize=11)
ax.legend(frameon=False)

# 8. Remove unnecessary borders, save a high-resolution image, and display it.
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("strip_swarm_plot.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Strip vs. swarm

| Type       | Best for                                                | Trade-off                                    |
| ---------- | ------------------------------------------------------- | -------------------------------------------- |
| Strip plot | Larger datasets and fast rendering                      | Jitter can still allow some overlap.         |
| Swarm plot | Smaller datasets where every point must remain distinct | Can become slow or crowded with many points. |

## Key choices

| Element      | Recommendation                                                  |
| ------------ | --------------------------------------------------------------- |
| Sample size  | Use raw points when the number per group remains readable.      |
| Jitter       | Apply it only across categories, never along the value axis.    |
| Summary      | Add a median or mean marker for quick comparison.               |
| Ordering     | Use a meaningful category order or sort by median.              |
| Transparency | Use alpha transparency for strip plots with overlapping points. |

## Example output

The code shows every first-response-time observation for Support, Sales, and Customer Success. The orange marks show each team’s median, while the point patterns reveal variation and possible unusually slow responses.
