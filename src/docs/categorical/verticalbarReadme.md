
# Vertical Bar Chart

A vertical bar chart compares values across discrete categories. Each bar’s height represents its value, making it useful for comparisons such as sales by product, tickets by priority, or students by grade.

## When to use it

Use a vertical bar chart when:

- Categories are distinct rather than continuous.
- You want readers to compare amounts quickly.
- There are a manageable number of labels (usually fewer than 10–12).

Avoid it for time-series trends with many points; a line chart is usually clearer in that case.

## Python example

Install Matplotlib once, if needed:

```bash
python -m pip install matplotlib
```

Save the following as `vertical_bar.py`, then run `python vertical_bar.py`. It will open the chart and save a PNG named `vertical_bar_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt

# 1. Define the category labels and their corresponding numeric values.
products = ["Notebook", "Pen", "Marker", "Stapler", "Folder"]
units_sold = [125, 210, 85, 60, 145]

# 2. Create a figure and axes. `figsize` is width × height in inches.
fig, ax = plt.subplots(figsize=(9, 5))

# 3. Draw one vertical bar per product.
#    `color` applies the main fill; `edgecolor` makes individual bars distinct.
bars = ax.bar(
    products,
    units_sold,
    color="#3B82F6",
    edgecolor="#1D4ED8",
    linewidth=0.8,
)

# 4. Add a descriptive title and axis labels so the chart stands on its own.
ax.set_title("Units Sold by Product", fontsize=16, fontweight="bold", pad=14)
ax.set_xlabel("Product", fontsize=11)
ax.set_ylabel("Units sold", fontsize=11)

# 5. Add a light horizontal grid to make values easier to estimate.
#    Place it behind the bars so it does not distract from the data.
ax.grid(axis="y", color="#D1D5DB", linewidth=0.8, alpha=0.8)
ax.set_axisbelow(True)

# 6. Start the y-axis at zero; this keeps bar-height comparisons honest.
ax.set_ylim(bottom=0)

# 7. Label each bar with its exact value.
ax.bar_label(bars, padding=3, fontsize=10)

# 8. Remove unnecessary borders for a cleaner presentation.
ax.spines[["top", "right"]].set_visible(False)

# 9. Adjust spacing, save a high-resolution image, and display the chart.
fig.tight_layout()
fig.savefig("vertical_bar_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element  | Recommendation                                                          |
| -------- | ----------------------------------------------------------------------- |
| Baseline | Begin the y-axis at zero.                                               |
| Ordering | Sort bars by value when ranking matters; otherwise use a natural order. |
| Labels   | Keep category names short; rotate labels only when necessary.           |
| Colors   | Use one consistent color unless color carries meaning.                  |
| Values   | Add data labels when readers need exact values, not just comparisons.   |

## Example output

The code produces five bars: Pen is highest at 210 units, while Stapler is lowest at 60 units. The labels show the precise values and the grid supports quick visual comparison.
