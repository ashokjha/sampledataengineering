# Line Chart

A line chart connects values in an ordered sequence, usually time, to show change and trend.

## When to use it

- Use it for continuous time series or other ordered measurements.
- Avoid it for unordered categories, where connecting points implies a relationship.

## Jupyter notebook

Run the same commented example interactively in [line_chart.ipynb](./line_chart.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib
```

Save this as `line_chart.py`, then run it. The example saves `line_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt

# Define an ordered time series.
months, revenue = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], [120, 135, 128, 148, 161, 175]

# Draw a line with visible point markers.
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(months, revenue, color="#2563EB", marker="o", linewidth=2.5, markersize=7)

# Label, save, and display the chart.
ax.set(title="Monthly Revenue", xlabel="Month", ylabel="Revenue (thousands of dollars)")
ax.grid(axis="y", color="#D1D5DB")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("line_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

