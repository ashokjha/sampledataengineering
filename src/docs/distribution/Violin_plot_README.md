
# Violin Plot

A violin plot compares distributions across groups. Its width shows where values are more concentrated, while an optional inner box or line shows summary statistics such as the median and quartiles.

## When to use it

Use a violin plot when:

- You want to compare the shape, spread, and concentration of numeric distributions.
- Each group has enough observations to estimate a meaningful density.
- A box plot alone would hide important features such as multiple peaks or skew.

Avoid it for very small samples: density shapes can suggest patterns that the data does not support. Use a box plot with individual points instead.

## Python example

Install Matplotlib and NumPy once, if needed:

```bash
python -m pip install matplotlib numpy
```

Save the following as `violin_plot.py`, then run `python violin_plot.py`. It will open the chart and save a PNG named `violin_plot.png` in the current folder.

```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Create reproducible sample satisfaction scores for three customer plans.
rng = np.random.default_rng(seed=12)
basic_scores = rng.normal(loc=72, scale=8, size=120)
standard_scores = rng.normal(loc=79, scale=6, size=120)
premium_scores = rng.normal(loc=85, scale=5, size=120)

# 2. Keep the data sets and their labels in the same order.
scores_by_plan = [basic_scores, standard_scores, premium_scores]
plans = ["Basic", "Standard", "Premium"]

# 3. Create a figure and axes for the chart.
fig, ax = plt.subplots(figsize=(8, 5.5))

# 4. Draw the violins.
#    `showmedians=True` adds a median line; `showextrema=True` adds min/max bars.
violin_parts = ax.violinplot(
    scores_by_plan,
    showmeans=False,
    showmedians=True,
    showextrema=True,
)

# 5. Style every violin body consistently.
for body in violin_parts["bodies"]:
    body.set_facecolor("#2563EB")
    body.set_edgecolor("#1D4ED8")
    body.set_alpha(0.55)

# 6. Style the summary lines so the median is easy to recognize.
violin_parts["cmedians"].set_color("#1E3A8A")
violin_parts["cmedians"].set_linewidth(2)
for key in ["cbars", "cmins", "cmaxes"]:
    violin_parts[key].set_color("#2563EB")
    violin_parts[key].set_linewidth(1.2)

# 7. Replace numeric positions with the plan names.
ax.set_xticks([1, 2, 3], plans)

# 8. Add a title and labels that explain the data and its scale.
ax.set_title("Customer Satisfaction by Subscription Plan", fontsize=16, fontweight="bold", pad=14)
ax.set_xlabel("Subscription plan", fontsize=11)
ax.set_ylabel("Satisfaction score (out of 100)", fontsize=11)

# 9. Add a light horizontal grid to support distribution comparisons.
ax.set_ylim(0, 100)
ax.grid(axis="y", color="#D1D5DB", linewidth=0.8, alpha=0.8)
ax.set_axisbelow(True)

# 10. Remove unnecessary borders, save a high-resolution image, and display it.
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("violin_plot.png", dpi=200, bbox_inches="tight")
plt.show()
```

## How to read it

- A wider section means more observations are concentrated around that value.
- A narrow section means relatively few observations occur there.
- The central line in this example marks the median.
- The end bars show the range of the observed data.

## Key choices

| Element     | Recommendation                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------ |
| Sample size | Use enough observations for a trustworthy density estimate.                                      |
| Scale       | Use one y-axis scale for every group.                                                            |
| Summary     | Show a median or quartile summary inside the violin.                                             |
| Width       | Do not interpret total violin area as group size unless widths are deliberately scaled that way. |
| Detail      | Overlay individual points when groups are small or transparency permits.                         |

## Example output

The code compares satisfaction-score distributions for three plans. Premium is centered highest and has the tightest spread, while Basic is lower and more variable. The violin widths reveal where scores are concentrated within each plan.
