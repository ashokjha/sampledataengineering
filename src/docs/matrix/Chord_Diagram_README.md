# Chord Diagram

A chord diagram shows relationships among categories arranged around a circle; chord width encodes relationship strength.

## When to use it

- Use it for a small, symmetric network of relationships or flows.
- Avoid it for many categories; a matrix or Sankey diagram is easier to read.

## Jupyter notebook

Run the same commented example interactively in [chord_diagram.ipynb](./chord_diagram.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install holoviews bokeh pandas
```

Save this as `chord_diagram.py`, then run it. The example saves `chord_diagram.html` in the current folder.

```python
import holoviews as hv
import pandas as pd

# Activate HoloViews' interactive Bokeh output.
hv.extension("bokeh")

# Define source-target relationships and their strengths.
links = pd.DataFrame({"source": ["Design", "Design", "Engineering", "Marketing"], "target": ["Engineering", "Marketing", "Support", "Sales"], "value": [12, 7, 10, 8]})
names = pd.Index(pd.concat([links["source"], links["target"]]).unique())
nodes = hv.Dataset(pd.DataFrame({"index": range(len(names)), "name": names}), "index")
lookup = {name: index for index, name in enumerate(names)}
links["source"], links["target"] = links["source"].map(lookup), links["target"].map(lookup)

# Draw, save, and display the interactive chord diagram.
chord = hv.Chord((links, nodes)).opts(labels="name", cmap="Category10", edge_color="source", node_color="index", width=700, height=700, title="Collaboration Links")
hv.save(chord, "chord_diagram.html")
chord
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

