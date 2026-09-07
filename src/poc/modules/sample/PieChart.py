import matplotlib.pyplot as plt

# 1. Define the data and labels
categories = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [40, 25, 20, 15]  # Proportions (can be raw numbers or percentages)
custom_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# 2. Highlight a specific section (e.g., separating the first slice)
# 0.1 means moving the slice out by 10% of the radius
explode = (0.1, 0, 0, 0)  

# 3. Configure the figure layout
plt.figure(figsize=(6, 6))

# 4. Generate the pie chart
plt.pie(
    sizes, 
    explode=explode, 
    labels=categories, 
    colors=custom_colors,
    autopct='%1.1f%%',       # Formats the values to show percentages with 1 decimal place
    shadow=True,             # Adds a subtle 3D drop-shadow effect
    startangle=140           # Rotates the start of the pie chart counter-clockwise
)

# 5. Set options and display
plt.title("Programming Language Popularity Breakdown", fontsize=14, fontweight='bold')
plt.axis('equal')           # Ensures the chart is drawn perfectly as a circle
plt.show()
