# Scatter Map / Dot Map

A scatter map places markers at geographic coordinates; marker size or color can encode a value.

## When to use it

- Use it for point-level geographic events, sites, or measurements.
- Avoid it when points overlap heavily; aggregate or use a density map.

## Jupyter notebook

Run the same commented example interactively in [scatter_map_dot_map.ipynb](./scatter_map_dot_map.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install plotly pandas
```

Save this as `scatter_map_dot_map.py`, then run it. The example saves `scatter_map.html` in the current folder.

```python
import pandas as pd
import plotly.express as px

# Store locations and the value represented by each marker.
cities = pd.DataFrame({"city": ["Delhi", "Mumbai", "Bengaluru"], "lat": [28.6139, 19.0760, 12.9716], "lon": [77.2090, 72.8777, 77.5946], "orders": [320, 280, 240]})

# Draw an interactive dot map; larger and darker dots mean more orders.
fig = px.scatter_geo(cities, lat="lat", lon="lon", size="orders", color="orders", hover_name="city", color_continuous_scale="Blues", projection="natural earth", title="Orders by City")

# Save a self-contained map and display it.
fig.write_html("scatter_map.html", include_plotlyjs=True)
fig.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

