
import plotly.express as px

# 1. Define data
data = {
    "Category": ['Product A', 'Product B', 'Product C', 'Product D'],
    "Values": [40, 30, 20, 10]
}

# 2. Create the donut chart using the 'hole' parameter
fig = px.pie(
    data, 
    names='Category', 
    values='Values', 
    title='Interactive Plotly Donut Chart',
    hole=0.4, # Creates a hole occupying 40% of the radius
    color_discrete_sequence=px.colors.qualitative.Pastel
)

# 3. Update trace to style text placement
fig.update_traces(textinfo='percent+label', textposition='inside')

# Display the chart
fig.show()