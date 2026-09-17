# Sankey Diagram

A Sankey diagram shows flows between stages or groups. Link width represents the amount moving between nodes.

## When to use it

- Use it to explain how quantities split, combine, or move through a process.
- Avoid it with too many nodes or crossing links.

## Jupyter notebook

Run the same commented example interactively in [sankey_diagram.ipynb](./sankey_diagram.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install plotly
```

Save this as `sankey_diagram.py`, then run it. The example saves `sankey_diagram.html` in the current folder.

```python
import plotly.graph_objects as go

# Define node labels and each link's source, target, and flow amount.
labels = ["Visits", "Product page", "Cart", "Purchase", "Exit"]
sources, targets, values = [0, 0, 1, 1, 2, 2], [1, 4, 2, 4, 3, 4], [700, 300, 420, 280, 260, 160]

# Draw links whose widths are proportional to flow amount.
fig = go.Figure(go.Sankey(node={"label": labels, "pad": 18, "thickness": 22, "color": "#2563EB"}, link={"source": sources, "target": targets, "value": values, "color": "rgba(37,99,235,0.28)"}))

# Save the interactive diagram and display it.
fig.update_layout(title="Website Conversion Flow")
fig.write_html("sankey_diagram.html", include_plotlyjs=True)
fig.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

