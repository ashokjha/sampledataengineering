# Parallel Coordinates Plot

A parallel coordinates plot displays multivariate observations as lines crossing parallel numeric axes.

## When to use it

- Use it to explore patterns across several numeric dimensions.
- Avoid it with many rows unless you use transparency, filtering, or sampling.

## Jupyter notebook

Run the same commented example interactively in [parallel_coordinates_plot.ipynb](./parallel_coordinates_plot.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install plotly pandas
```

Save this as `parallel_coordinates_plot.py`, then run it. The example saves `parallel_coordinates.html` in the current folder.

```python
import pandas as pd
import plotly.express as px

# Create a small multivariate data set; every row becomes one line.
products = pd.DataFrame({"product": ["A", "B", "C", "D", "E", "F"], "quality": [78, 91, 84, 73, 88, 95], "price": [24, 38, 31, 19, 34, 44], "satisfaction": [81, 87, 84, 75, 89, 92], "repeat_rate": [42, 55, 48, 36, 58, 63]})

# Draw one line per product and color it by satisfaction.
fig = px.parallel_coordinates(products, dimensions=["quality", "price", "satisfaction", "repeat_rate"], color="satisfaction", color_continuous_scale="Viridis", title="Product Profile Comparison")

# Save and display the interactive chart.
fig.write_html("parallel_coordinates.html", include_plotlyjs=True)
fig.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

