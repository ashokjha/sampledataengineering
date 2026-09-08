import matplotlib.pyplot as plt

# 1. Define data
categories = ["Product A", "Product B", "Product C", "Product D"]
values = [40, 30, 20, 10]
colors = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261"]

# 2. Create figure and axis
fig, ax = plt.subplots(figsize=(6, 6))

# 3. Plot the pie chart with a wedge width
wedges, texts, autotexts = ax.pie(
    values,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    pctdistance=0.75,  # Positions percentages inside the donut ring
    wedgeprops=dict(
        width=0.4, edgecolor="white", linewidth=2
    ),  # Defines the donut hole
)

# 4. Optional: Add center text (e.g., a KPI or grand total)
total_value = sum(values)
ax.text(
    0,
    0,
    f"Total\n{total_value}",
    ha="center",
    va="center",
    fontsize=14,
    fontweight="bold",
)

# Ensure the chart remains a perfect circle
ax.set_aspect("equal")
plt.title("Matplotlib Donut Chart", fontsize=16, fontweight="bold", pad=20)
plt.show()
