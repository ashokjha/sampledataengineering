# Stacked Area Chart

A stacked area chart shows a total over time and how components contribute to it.

## When to use it

- Use it when composition and total change over time both matter.
- Avoid it when readers need precise comparison of middle layers.

## Jupyter notebook

Run the same commented example interactively in [stacked_area_chart.ipynb](./stacked_area_chart.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib
```

Save this as `stacked_area_chart.py`, then run it. The example saves `stacked_area_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt

# Define a shared time axis and one series for every acquisition channel.
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
organic, paid, referral = [42, 49, 46, 55, 61, 68], [28, 30, 34, 31, 37, 40], [12, 15, 14, 17, 18, 20]

# Stack series in a consistent order.
fig, ax = plt.subplots(figsize=(9, 5.5))
ax.stackplot(months, organic, paid, referral, labels=["Organic", "Paid", "Referral"], colors=["#2563EB", "#14B8A6", "#F59E0B"], alpha=0.82)

# Label, save, and display the chart.
ax.set(title="Website Sessions by Acquisition Channel", xlabel="Month", ylabel="Sessions (thousands)", ylim=(0, 150))
ax.legend(loc="upper left", frameon=False, ncols=3)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("stacked_area_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

