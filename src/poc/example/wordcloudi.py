import plotly.graph_objects as go
import plotly.express as px

# Your original data
numbers = [100, 85, 80, 75, 70, 65, 60, 55, 50, 48]

# 1. Normalize numbers between 0 and 1
min_val, max_val = min(numbers), max(numbers)
normalized = [(x - min_val) / (max_val - min_val) for x in numbers]

# 2. Get a sample colorscale from Plotly Express (e.g., Viridis or Plasma)
colorscale = px.colors.sequential.Viridis

# 3. Map normalized values to color strings
# px.colors.sample_colorscale expects inputs between 0 and 1
color_strings = px.colors.sample_colorscale(colorscale, normalized)

# 4. Use the color strings in your chart
fig = go.Figure(
    data=[
        go.Scatter3d(
            x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            y=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            z=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            mode="markers+text",
            text=[str(n) for n in numbers],
            textfont=dict(color=color_strings),  # Valid list of RGB color strings
        )
    ]
)

fig.show()
