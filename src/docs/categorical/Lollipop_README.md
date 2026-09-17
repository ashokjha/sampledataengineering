
# Lollipop Chart

A lollipop chart is a streamlined alternative to a bar chart. A thin line connects each category to its value, and a marker at the end highlights that value. It works well when the values are the focus and a full bar would feel visually heavy.

## When to use it

Use a lollipop chart when:

- You are comparing a modest number of discrete category values.
- The chart benefits from a lighter visual treatment than a bar chart.
- Values are sorted or naturally ordered.

Avoid it when there are many categories, very small differences that require exact comparison, or negative values that make the baseline more complex. A standard bar chart can be clearer in those cases.

## Python example

Install Matplotlib once, if needed:

```bash
python -m pip install matplotlib
```

Save the following as `lollipop.py`, then run `python lollipop.py`. It will open the chart and save a PNG named `lollipop_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt

# 1. Define category labels and their corresponding values.
departments = ["Support", "Sales", "Marketing", "Product", "Engineering"]
satisfaction_scores = [78, 84, 81, 89, 92]

# 2. Sort the data by value to make the ranking easy to scan.
ranked_data = sorted(zip(satisfaction_scores, departments))
satisfaction_scores, departments = zip(*ranked_data)

# 3. Create a figure and axes. The vertical layout works well for rankings.
fig, ax = plt.subplots(figsize=(9, 5.5))

# 4. Draw thin horizontal lines from zero to each value.
#    `hlines` creates the sticks of the lollipops.
ax.hlines(
    y=departments,
    xmin=0,
    xmax=satisfaction_scores,
    color="#93C5FD",
    linewidth=3,
    zorder=1,
)

# 5. Draw a circle at the end of each line.
#    A higher `zorder` ensures markers sit above the lines.
ax.scatter(
    satisfaction_scores,
    departments,
    color="#2563EB",
    s=110,
    zorder=2,
)

# 6. Add exact values just to the right of their markers.
for department, score in zip(departments, satisfaction_scores):
    ax.annotate(
        f"{score}",
        xy=(score, department),
        xytext=(7, 0),
        textcoords="offset points",
        va="center",
        fontsize=10,
        fontweight="bold",
    )

# 7. Add a descriptive title and labels.
ax.set_title("Employee Satisfaction by Department", fontsize=16, fontweight="bold", pad=14)
ax.set_xlabel("Satisfaction score (out of 100)", fontsize=11)
ax.set_ylabel("Department", fontsize=11)

# 8. Use a zero baseline and subtle vertical grid lines to support comparison.
ax.set_xlim(left=0, right=max(satisfaction_scores) + 12)
ax.grid(axis="x", color="#D1D5DB", linewidth=0.8, alpha=0.8)
ax.set_axisbelow(True)

# 9. Remove unnecessary borders, save a high-resolution image, and display it.
ax.spines[["top", "right", "left"]].set_visible(False)
fig.tight_layout()
fig.savefig("lollipop_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element     | Recommendation                                             |
| ----------- | ---------------------------------------------------------- |
| Orientation | Use horizontal lollipops for long labels or ranked values. |
| Baseline    | Begin the value axis at zero when comparing magnitudes.    |
| Markers     | Make markers visually stronger than the stems.             |
| Ordering    | Sort values to make a rank order immediately apparent.     |
| Labels      | Add value labels when exact numbers are important.         |

## Example output

The code ranks five departments by satisfaction score. Engineering leads at 92, while Support has the lowest score at 78. The thin stems preserve the comparison context without the visual weight of solid bars.
