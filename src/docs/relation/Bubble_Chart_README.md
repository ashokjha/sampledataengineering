# Bubble Chart

A bubble chart is a scatter plot where marker area encodes a third numeric variable.

## When to use it

- Use it to compare three numeric measures across a modest number of observations.
- Avoid it when bubble overlap or area-based comparisons hide important values.

## Jupyter notebook

Run the same commented example interactively in [bubble_chart.ipynb](./bubble_chart.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib pandas
```

Save this as `bubble_chart.py`, then run it. The example saves `bubble_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt
import pandas as pd

# Define x, y, and bubble-size measures for every product.
products = pd.DataFrame({"product": ["A", "B", "C", "D", "E"], "price": [18, 25, 32, 21, 38], "rating": [4.1, 4.6, 4.4, 3.9, 4.8], "units_sold": [840, 560, 720, 410, 650]})

# Draw bubbles; marker area is scaled from units sold.
fig, ax = plt.subplots(figsize=(8, 5.5))
ax.scatter(products["price"], products["rating"], s=products["units_sold"] * 0.65, color="#2563EB", alpha=0.55, edgecolor="#1D4ED8")

# Label each point, then save and display the chart.
for row in products.itertuples():
    ax.annotate(row.product, (row.price, row.rating), xytext=(5, 5), textcoords="offset points")
ax.set(title="Product Price, Rating, and Units Sold", xlabel="Price (dollars)", ylabel="Customer rating")
ax.grid(color="#D1D5DB")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("bubble_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

