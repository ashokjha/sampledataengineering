# Area Chart

An area chart fills the space below a line to emphasize magnitude over an ordered sequence.

## When to use it

- Use it for a single time series when cumulative magnitude is important.
- Avoid it for multiple overlapping series; fills can obscure comparison.

## Jupyter notebook

Run the same commented example interactively in [area_chart.ipynb](./area_chart.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib
```

Save this as `area_chart.py`, then run it. The example saves `area_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt

# Define an ordered time series.
months, active_users = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], [120, 145, 138, 166, 181, 205]

# Draw the outline and the filled area beneath it.
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(months, active_users, color="#2563EB", linewidth=2.3)
ax.fill_between(months, active_users, color="#2563EB", alpha=0.22)

# Keep the magnitude baseline at zero, then save and display.
ax.set(title="Monthly Active Users", xlabel="Month", ylabel="Active users (thousands)", ylim=(0, 230))
ax.grid(axis="y", color="#D1D5DB")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("area_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

