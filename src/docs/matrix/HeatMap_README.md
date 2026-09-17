# Heatmap

A heatmap uses color in a grid to show magnitude across two dimensions.

## When to use it

- Use it to find patterns across category pairs, dates, or matrix-like data.
- Avoid it when exact values matter more than broad patterns.

## Jupyter notebook

Run the same commented example interactively in [heatmap.ipynb](./heatmap.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib seaborn pandas
```

Save this as `heatmap.py`, then run it. The example saves `heatmap.png` in the current folder.

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Arrange values as a matrix: rows are teams and columns are weekdays.
tickets = pd.DataFrame([[18, 24, 20, 29, 17], [12, 16, 14, 19, 11], [22, 20, 26, 24, 21]], index=["Support", "Sales", "Success"], columns=["Mon", "Tue", "Wed", "Thu", "Fri"])

# Draw one colored, annotated cell for every value.
fig, ax = plt.subplots(figsize=(8, 4.5))
sns.heatmap(tickets, annot=True, fmt="d", cmap="Blues", linewidths=1, linecolor="white", ax=ax)

# Label, save, and display the figure.
ax.set(title="Tickets by Team and Weekday", xlabel="Weekday", ylabel="Team")
fig.tight_layout()
fig.savefig("heatmap.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

