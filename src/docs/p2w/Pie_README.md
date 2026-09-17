# Pie Chart

A pie chart shows how a small set of parts contributes to one whole.

## When to use it

- Use it for a few clearly distinct shares that total 100%.
- Avoid it with many slices or similar values; a bar chart is clearer.

## Jupyter notebook

Run the same commented example interactively in [pie_chart.ipynb](./pie_chart.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib
```

Save this as `pie_chart.py`, then run it. The example saves `pie_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt

# Define parts of a total and their corresponding colors.
channels, visits = ["Organic", "Paid search", "Email", "Referral"], [46, 27, 17, 10]
colors = ["#2563EB", "#14B8A6", "#F59E0B", "#94A3B8"]

# Draw slices and label each share as a percentage.
fig, ax = plt.subplots(figsize=(7, 6))
ax.pie(visits, labels=channels, colors=colors, autopct="%1.0f%%", startangle=90, wedgeprops={"edgecolor": "white", "linewidth": 2})

# Keep the pie circular, then save and display it.
ax.set_title("Website Visits by Channel", fontweight="bold")
ax.axis("equal")
fig.tight_layout()
fig.savefig("pie_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

