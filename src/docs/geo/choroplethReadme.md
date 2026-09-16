
# Choropleth Map

A choropleth map shades geographic regions according to a numeric value. It is useful for showing how a rate, count, or other measure varies across countries, states, districts, or other defined areas.

## When to use it

Use a choropleth map when:

- Location is essential to the question.
- Values are attached to defined geographic regions.
- Broad spatial patterns matter more than precise value comparisons.

Avoid it when regions differ greatly in area or population and the audience must compare exact values. A ranked bar chart is often clearer; pair it with the map when both geography and ranking matter.

## Python example

Install Plotly and Pandas once, if needed:

```bash
python -m pip install plotly pandas
```

Save the following as `choropleth_map.py`, then run `python choropleth_map.py`. It will open an interactive map and save a self-contained HTML file named `choropleth_map.html` in the current folder.

```python
import pandas as pd
import plotly.express as px

# 1. Define one value for each country using ISO 3166-1 alpha-3 country codes.
#    ISO codes avoid ambiguity that can occur with country names.
data = pd.DataFrame(
    {
        "country": ["United States", "Canada", "Brazil", "Germany", "India", "Japan", "Australia"],
        "iso_alpha": ["USA", "CAN", "BRA", "DEU", "IND", "JPN", "AUS"],
        "renewable_share": [22.5, 66.0, 48.0, 52.0, 23.0, 24.0, 35.0],
    }
)

# 2. Create the map. Each region is colored by its renewable-energy share.
#    `locations` identifies the geographic region; `locationmode` explains the code type.
fig = px.choropleth(
    data,
    locations="iso_alpha",
    locationmode="ISO-3",
    color="renewable_share",
    hover_name="country",
    hover_data={"iso_alpha": False, "renewable_share": ":.1f"},
    color_continuous_scale="Blues",
    range_color=(0, 70),       # Fix the scale so colors have a clear, stable meaning.
    labels={"renewable_share": "Renewable energy (%)"},
    projection="natural earth",
)

# 3. Add a clear title and simplify the base-map styling.
fig.update_layout(
    title={
        "text": "Renewable Energy Share by Country",
        "x": 0.5,
        "xanchor": "center",
    },
    margin={"l": 0, "r": 0, "t": 55, "b": 0},
    coloraxis_colorbar={"title": "Renewable<br>energy (%)"},
)
fig.update_geos(
    showcoastlines=True,
    coastlinecolor="#9CA3AF",
    showframe=False,
    bgcolor="white",
)

# 4. Save an interactive, self-contained chart and open it in the browser.
fig.write_html("choropleth_map.html", include_plotlyjs=True)
fig.show()
```

## Key choices

| Element        | Recommendation                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------- |
| Geographic key | Use stable IDs such as ISO codes or official region identifiers.                                        |
| Measure        | Prefer normalized values—rates, percentages, or per-capita figures—when region sizes differ.          |
| Color scale    | Use a sequential scale for low-to-high values; use a diverging scale only around a meaningful midpoint. |
| Missing data   | Distinguish missing values from zero, and state how they are shown.                                     |
| Comparison     | Use a stable color range when comparing maps over time or across groups.                                |

## Example output

The code colors seven countries by renewable energy’s share of their energy mix. Darker blue indicates a higher share, and hovering over a country reveals its name and exact percentage.
