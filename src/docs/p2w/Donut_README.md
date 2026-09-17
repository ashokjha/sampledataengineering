# Donut Chart

A donut chart is a pie chart with a central hole, often used to place a total or key metric in the middle.

## When to use it

- Use it for a small part-to-whole comparison when the center adds useful context.
- Avoid it when readers need precise slice comparisons.

## Jupyter notebook

Run the same commented example interactively in [donut_chart.ipynb](./donut_chart.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib
```

Save this as `donut_chart.py`, then run it. The example saves `donut_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt

# Define a small set of task-status counts.
statuses, tasks = ["Complete", "In progress", "Not started"], [58, 29, 13]
colors = ["#14B8A6", "#2563EB", "#CBD5E1"]

# Draw a pie with width less than one to create the center hole.
fig, ax = plt.subplots(figsize=(7, 6))
ax.pie(tasks, labels=statuses, colors=colors, autopct="%1.0f%%", startangle=90, wedgeprops={"width": 0.48, "edgecolor": "white", "linewidth": 2})

# Add the total to the center, then save and display the chart.
ax.text(0, 0, f"{sum(tasks)}\nTasks", ha="center", va="center", fontsize=16, fontweight="bold")
ax.set_title("Project Task Status", fontweight="bold")
ax.axis("equal")
fig.tight_layout()
fig.savefig("donut_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

