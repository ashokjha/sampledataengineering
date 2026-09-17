
# Horizontal Bar Chart

A horizontal bar chart compares values across discrete categories, with each bar extending from left to right. It is especially useful when category labels are long or when ranking values from highest to lowest.

## When to use it

Use a horizontal bar chart when:

- Category names are long and would be cramped on a vertical chart.
- You want to emphasize a ranked list.
- Readers need to scan labels and values from top to bottom.

Avoid it for a continuous time series; use a line chart instead.

## Python example

Install Matplotlib once, if needed:

```bash
python -m pip install matplotlib
```

Save the following as `horizontal_bar.py`, then run `python horizontal_bar.py`. It will open the chart and save a PNG named `horizontal_bar_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt

# 1. Define category labels and their matching numeric values.
support_topics = [
    "Account access and passwords",
    "Billing and subscriptions",
    "Product setup",
    "Shipping status",
    "Returns and refunds",
]
ticket_counts = [42, 67, 31, 54, 25]

# 2. Sort the values so the largest category appears at the top.
#    `zip` keeps each label matched to its original value during sorting.
ranked_topics = sorted(zip(ticket_counts, support_topics))
ticket_counts, support_topics = zip(*ranked_topics)

# 3. Create a figure and axes. The extra width accommodates longer labels.
fig, ax = plt.subplots(figsize=(10, 5.5))

# 4. Draw horizontal bars with `barh`.
#    The y-axis receives the category labels; bar length represents each value.
bars = ax.barh(
    support_topics,
    ticket_counts,
    color="#14B8A6",
    edgecolor="#0F766E",
    linewidth=0.8,
)

# 5. Add a title and axis labels that explain the data without extra context.
ax.set_title("Customer-Support Tickets by Topic", fontsize=16, fontweight="bold", pad=14)
ax.set_xlabel("Number of tickets", fontsize=11)
ax.set_ylabel("Support topic", fontsize=11)

# 6. Add subtle vertical grid lines to support value comparison.
ax.grid(axis="x", color="#D1D5DB", linewidth=0.8, alpha=0.8)
ax.set_axisbelow(True)

# 7. Start the value axis at zero so bar-length comparisons remain accurate.
ax.set_xlim(left=0)

# 8. Add the exact value at the end of every bar.
ax.bar_label(bars, padding=4, fontsize=10)

# 9. Remove visual clutter and leave enough room for value labels.
ax.spines[["top", "right"]].set_visible(False)
ax.margins(x=0.12)

# 10. Apply spacing, save a high-resolution image, and display it.
fig.tight_layout()
fig.savefig("horizontal_bar_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element  | Recommendation                                               |
| -------- | ------------------------------------------------------------ |
| Ordering | Sort by value for a ranking; put the largest bar at the top. |
| Baseline | Begin the x-axis at zero.                                    |
| Labels   | Prefer this chart when category names are lengthy.           |
| Colors   | Use one color unless colors encode a meaningful group.       |
| Values   | Add labels at bar ends when exact counts matter.             |

## Example output

The code sorts five support topics by ticket count. Billing and subscriptions is the largest category at 67 tickets, while Returns and refunds is the smallest at 25. The horizontal layout leaves every topic label easy to read.
