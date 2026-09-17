
# Stacked Bar Chart

A stacked bar chart shows a total for each category and how that total is divided into parts. Each colored segment represents one component; together, the segments form the full bar.

## When to use it

Use a stacked bar chart when:

- You need to compare totals across categories and show their composition.
- Each bar contains a small, consistent set of components.
- The component values share the same unit.

Avoid it when readers must compare the same middle segment precisely across many bars; only the bottom segment shares a common baseline. A grouped bar chart may be clearer.

## Python example

Install Matplotlib once, if needed:

```bash
python -m pip install matplotlib
```

Save the following as `stacked_bar.py`, then run `python stacked_bar.py`. It will open the chart and save a PNG named `stacked_bar_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt

# 1. Define the main categories and the values for each component.
quarters = ["Q1", "Q2", "Q3", "Q4"]
online_sales = [42, 50, 61, 58]
store_sales = [31, 28, 35, 40]
partner_sales = [12, 16, 14, 19]

# 2. Create a figure and axes for the chart.
fig, ax = plt.subplots(figsize=(9, 5.5))

# 3. Draw the bottom layer first. This layer starts at zero.
online_bars = ax.bar(
    quarters,
    online_sales,
    label="Online",
    color="#2563EB",
)

# 4. Stack the next layer on top by setting `bottom` to the layer beneath it.
store_bars = ax.bar(
    quarters,
    store_sales,
    bottom=online_sales,
    label="Store",
    color="#14B8A6",
)

# 5. Calculate the cumulative height for the final layer.
#    Each Partner segment begins above the combined Online and Store values.
online_and_store = [online + store for online, store in zip(online_sales, store_sales)]
partner_bars = ax.bar(
    quarters,
    partner_sales,
    bottom=online_and_store,
    label="Partner",
    color="#F59E0B",
)

# 6. Add a title, labels, and a legend explaining the color mapping.
ax.set_title("Quarterly Revenue by Sales Channel", fontsize=16, fontweight="bold", pad=14)
ax.set_xlabel("Quarter", fontsize=11)
ax.set_ylabel("Revenue (thousands of dollars)", fontsize=11)
ax.legend(title="Channel", frameon=False, ncols=3, loc="upper left")

# 7. Use a zero baseline and a light horizontal grid for reliable comparisons.
ax.set_ylim(bottom=0)
ax.grid(axis="y", color="#D1D5DB", linewidth=0.8, alpha=0.8)
ax.set_axisbelow(True)

# 8. Label the total at the top of every stack.
totals = [online + store + partner for online, store, partner in zip(online_sales, store_sales, partner_sales)]
for quarter, total in zip(quarters, totals):
    ax.annotate(
        f"{total}",
        xy=(quarter, total),
        xytext=(0, 4),
        textcoords="offset points",
        ha="center",
        fontsize=10,
        fontweight="bold",
    )

# 9. Remove unnecessary borders, adjust spacing, save, and display the chart.
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("stacked_bar_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element            | Recommendation                                                                     |
| ------------------ | ---------------------------------------------------------------------------------- |
| Segment order      | Keep the order and colors consistent across every bar.                             |
| Number of segments | Limit to a few meaningful components; too many become hard to read.                |
| Baseline           | Begin the y-axis at zero.                                                          |
| Totals             | Show total labels when comparing whole-bar size is important.                      |
| Comparison         | Use a grouped bar chart if precise component-to-component comparison matters most. |

## Example output

The code shows quarterly revenue split among Online, Store, and Partner channels. Q4 has the highest total at 117 thousand dollars, while the colors reveal how each channel contributes to that total.
