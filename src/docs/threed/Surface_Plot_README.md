# Scatter Plot Surface Plot

A 3D surface plot represents a numeric value as height above an x-y grid; scatter points can show sampled observations.

## When to use it

- Use it to explore a modeled response across two continuous inputs.
- Avoid it for presentation when a contour or heatmap would be clearer.

## Jupyter notebook

Run the same commented example interactively in [scatter_surface_plot.ipynb](./scatter_surface_plot.ipynb).

## Python example

Install the required packages once:

```bash
python -m pip install matplotlib numpy
```

Save this as `scatter_surface_plot.py`, then run it. The example saves `scatter_surface_plot.png` in the current folder.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create an x-y grid and calculate a smooth response surface.
x_values = np.linspace(-3, 3, 40)
y_values = np.linspace(-3, 3, 40)
x_grid, y_grid = np.meshgrid(x_values, y_values)
z_grid = np.sin(x_grid) * np.cos(y_grid)

# Sample observed points from the same surface with a little noise.
rng = np.random.default_rng(seed=10)
x_points, y_points = rng.uniform(-3, 3, 45), rng.uniform(-3, 3, 45)
z_points = np.sin(x_points) * np.cos(y_points) + rng.normal(0, 0.08, 45)

# Draw the surface and overlay the sampled observations.
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(projection="3d")
ax.plot_surface(x_grid, y_grid, z_grid, cmap="viridis", alpha=0.72, linewidth=0)
ax.scatter(x_points, y_points, z_points, color="#F97316", s=28, label="Observed points")

# Label, save, and display the 3D chart.
ax.set(title="Response Surface with Observations", xlabel="Input X", ylabel="Input Y", zlabel="Response Z")
ax.legend()
fig.tight_layout()
fig.savefig("scatter_surface_plot.png", dpi=200, bbox_inches="tight")
plt.show()
```

## Key choices

| Element | Recommendation |
| --- | --- |
| Purpose | Match the chart to the question the audience needs answered. |
| Labels | State the unit, time period, and measurement clearly. |
| Color | Use color sparingly and keep its meaning consistent. |
| Accessibility | Do not rely on color alone. |

