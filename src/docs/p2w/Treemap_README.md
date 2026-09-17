# Treemap

A treemap uses nested rectangles to show hierarchical parts of a whole; rectangle area represents value.

## When to use it

- Use it to explore a hierarchy with many categories and their relative sizes.
- Avoid it when exact comparisons across rectangles are critical.

## Jupyter notebook

Run the same commented example interactively in [treemap.ipynb](./treemap.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install plotly pandas
```

Save this as `treemap.py`, then run it. The example saves `treemap.html` in the current folder.

```python
import pandas as pd
import plotly.express as px

# Define a two-level organization hierarchy and one value per team.
data = pd.DataFrame({"department": ["Engineering", "Engineering", "Marketing", "Marketing", "Operations", "Operations"], "team": ["Platform", "Product", "Content", "Growth", "Finance", "People"], "headcount": [28, 22, 12, 15, 10, 8]})

# Create nested rectangles where area and color encode headcount.
fig = px.treemap(data, path=["department", "team"], values="headcount", color="headcount", color_continuous_scale="Blues", title="Headcount by Department and Team")

# Save and display the interactive chart.
fig.write_html("treemap.html", include_plotlyjs=True)
fig.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

