
# Radar Chart

A radar chart, also called a spider chart, compares several measures for one or more items on a shared radial scale. Each measure is an axis radiating from the center; connected values form a polygon.

## When to use it

Use a radar chart when:

- You want to show an overall profile across a small set of comparable measures.
- All measures use the same scale, or can be meaningfully normalized to one.
- You are comparing only a few items at once.

Avoid it for precise comparisons or many series. Overlapping polygons can become hard to interpret; a grouped bar chart or heatmap is often more exact.

## Python example

Install Matplotlib and NumPy once, if needed:

```bash
python -m pip install matplotlib numpy
```

Save the following as `radar_chart.py`, then run `python radar_chart.py`. It will open the chart and save a PNG named `radar_chart.png` in the current folder.

```python
import matplotlib.pyplot as plt
import numpy as np

# 1. Define each dimension and scores on one common 0–100 scale.
skills = ["Communication", "Technical", "Leadership", "Strategy", "Execution"]
alex_scores = [82, 91, 74, 79, 88]
maya_scores = [88, 83, 90, 86, 80]

# 2. Calculate evenly spaced angles for the radar axes.
#    `endpoint=False` avoids duplicating the first angle at this stage.
angles = np.linspace(0, 2 * np.pi, len(skills), endpoint=False).tolist()

# 3. Repeat the first angle and score to close each polygon.
angles += angles[:1]
alex_values = alex_scores + alex_scores[:1]
maya_values = maya_scores + maya_scores[:1]

# 4. Create polar axes. `projection="polar"` is required for a radar chart.
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw={"projection": "polar"})

# 5. Put the first category at the top and arrange axes clockwise.
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# 6. Position each category label at its corresponding angle.
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=11)

# 7. Configure the shared radial scale and its reference rings.
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(["20", "40", "60", "80", "100"], color="#6B7280", fontsize=9)
ax.grid(color="#D1D5DB", linewidth=0.8)

# 8. Draw and lightly fill a polygon for each person.
ax.plot(angles, alex_values, color="#2563EB", linewidth=2, label="Alex")
ax.fill(angles, alex_values, color="#2563EB", alpha=0.16)

ax.plot(angles, maya_values, color="#F97316", linewidth=2, label="Maya")
ax.fill(angles, maya_values, color="#F97316", alpha=0.16)

# 9. Add a title and legend. Place the legend outside to avoid covering data.
ax.set_title("Leadership Profile Comparison", fontsize=16, fontweight="bold", pad=28)
ax.legend(loc="upper right", bbox_to_anchor=(1.22, 1.12), frameon=False)

# 10. Apply spacing, save a high-resolution image, and display the chart.
fig.tight_layout()
fig.savefig("radar_chart.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element    | Recommendation                                                  |
| ---------- | --------------------------------------------------------------- |
| Scale      | Use identical minimums, maximums, and intervals for every axis. |
| Dimensions | Limit to about 5–8 meaningful, distinct measures.              |
| Series     | Compare only a few profiles to prevent overlap.                 |
| Fill       | Use transparent fills so overlapping areas remain visible.      |
| Precision  | Use a table or bar chart when readers need exact comparisons.   |

## Example output

The code compares Alex and Maya across five leadership skills. Alex is strongest in Technical skill and Execution, while Maya leads in Communication, Leadership, and Strategy. The polygons provide a quick view of each person’s overall profile.
