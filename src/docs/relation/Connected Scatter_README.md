# Connected Scatter Plot

A connected scatter plot links sequential observations on an x-y plane, showing how two variables change together over time.

## When to use it

- Use it to show a trajectory through two numeric measures.
- Avoid it when observation order is not meaningful or labels would be cluttered.

## Jupyter notebook

Run the same commented example interactively in [connected_scatter.ipynb](./connected_scatter.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib
```

Save this as `connected_scatter.py`, then run it. The example saves `connected_scatter.png` in the current folder.

```python
import matplotlib.pyplot as plt

# Define one x-y pair for each ordered quarter.
quarters = ["Q1", "Q2", "Q3", "Q4"]
satisfaction, retention = [72, 76, 81, 84], [68, 70, 74, 79]

# Connect points in chronological order.
fig, ax = plt.subplots(figsize=(8, 5.5))
ax.plot(satisfaction, retention, color="#93C5FD", linewidth=2)
ax.scatter(satisfaction, retention, color="#2563EB", s=85, zorder=2)

# Label the path, then save and display the chart.
for quarter, x, y in zip(quarters, satisfaction, retention):
    ax.annotate(quarter, (x, y), xytext=(6, 6), textcoords="offset points", fontweight="bold")
ax.set(title="Customer Satisfaction and Retention Over Time", xlabel="Customer satisfaction score", ylabel="Retention rate (%)")
ax.grid(color="#D1D5DB")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("connected_scatter.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

