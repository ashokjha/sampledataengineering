# Connection Map

A connection map draws lines between places to show routes, flows, or relationships across geography.

## When to use it

- Use it for a small set of origin-to-destination relationships.
- Avoid it for dense networks, where intersecting lines obscure the routes.

## Jupyter notebook

Run the same commented example interactively in [connection_map.ipynb](./connection_map.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install plotly
```

Save this as `connection_map.py`, then run it. The example saves `connection_map.html` in the current folder.

```python
import plotly.graph_objects as go

# Define each route as origin and destination coordinates.
routes = [(28.6139, 77.2090, 19.0760, 72.8777), (28.6139, 77.2090, 12.9716, 77.5946)]

# Draw one geographic line for every route.
fig = go.Figure()
for origin_lat, origin_lon, destination_lat, destination_lon in routes:
    fig.add_trace(go.Scattergeo(lat=[origin_lat, destination_lat], lon=[origin_lon, destination_lon], mode="lines", line={"width": 2, "color": "#2563EB"}, showlegend=False))

# Add endpoint markers, configure the map, save, and display it.
fig.add_trace(go.Scattergeo(lat=[28.6139, 19.0760, 12.9716], lon=[77.2090, 72.8777, 77.5946], text=["Delhi", "Mumbai", "Bengaluru"], mode="markers+text", marker={"size": 9, "color": "#F97316"}, textposition="top center", showlegend=False))
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(title="Regional Delivery Routes", margin={"l": 0, "r": 0, "t": 45, "b": 0})
fig.write_html("connection_map.html", include_plotlyjs=True)
fig.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

