# Sunburst Chart

A sunburst chart shows hierarchical data as concentric rings; each ring adds a deeper level.

## When to use it

- Use it to show a compact hierarchy with a small number of levels.
- Avoid it when labels are long or exact comparison is the priority.

## Jupyter notebook

Run the same commented example interactively in [sunburst.ipynb](./sunburst.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install plotly pandas
```

Save this as `sunburst.py`, then run it. The example saves `sunburst.html` in the current folder.

```python
import pandas as pd
import plotly.express as px

# Define a hierarchy from region to category to product.
data = pd.DataFrame({"region": ["North", "North", "South", "South"], "category": ["Home", "Tech", "Home", "Tech"], "product": ["Chair", "Headphones", "Lamp", "Keyboard"], "sales": [42, 61, 35, 54]})

# Draw one ring per hierarchy level; angular size represents sales.
fig = px.sunburst(data, path=["region", "category", "product"], values="sales", color="sales", color_continuous_scale="Blues", title="Sales Hierarchy by Region and Product")

# Save and display the interactive chart.
fig.write_html("sunburst.html", include_plotlyjs=True)
fig.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

