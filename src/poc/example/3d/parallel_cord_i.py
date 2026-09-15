import plotly.express as px

# Load sample dataset
df = px.data.iris()

# Create the interactive parallel coordinates plot
fig = px.parallel_coordinates(
    df,
    color="species_id",
    dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
    color_continuous_scale=px.colors.diverging.Tealrose,
    labels={
        "species_id": "Species",
        "sepal_width": "Sepal Width",
        "sepal_length": "Sepal Length",
        "petal_width": "Petal Width",
        "petal_length": "Petal Length",
    },
)

# Display the interactive figure
fig.show()
