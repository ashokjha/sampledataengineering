# python 3D Word Cloud static and interactive

To build a **3D Word Cloud** in Python, the standard 2D `wordcloud` library won't suffice. Instead, we can  use **Matplotlib** for a static 3D rendering and **Plotly** for a fully interactive 3D rendering that we can spin, zoom, and hover over= .

Below is the complete implementation for both approaches.

---

## 1. Static 3D Word Cloud (Matplotlib)

This method extracts word sizes based on frequency and maps them onto random `(x, y, z)` coordinates using Matplotlib's 3D projection engine.

```Python
import random
import matplotlib.pyplot as plt
from collections import Counter

# Sample text data
text = "python data-science visualization interactive static plotly matplotlib wordcloud coding analytics machine-learning insights graphics technology future intelligent web design dashboard map scale depth space axis"
words = text.split()
word_counts = Counter(words)

# Setup Matplotlib 3D figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Generate coordinates and plot each word
for word, count in word_counts.items():
    # Randomly position words in a 3D space
    x = random.uniform(-10, 10)
    y = random.uniform(-10, 10)
    z = random.uniform(-10, 10)
  
    # Scale font size dynamically based on word frequency
    font_size = 10 + count * 8  
  
    # Choose a random color for visual flair
    color = (random.random(), random.random(), random.random())
  
    # Render text in 3D space
    ax.text(x, y, z, word, size=font_size, color=color, 
            horizontalalignment='center', verticalalignment='center')

# Bound the axes and hide the grids for a cleaner look
ax.set_xlim(-12, 12)
ax.set_ylim(-12, 12)
ax.set_zlim(-12, 12)
ax.axis('off')

plt.title("Static 3D Word Cloud (Matplotlib)", fontsize=16)
plt.show()
```

## 2. Interactive 3D Word Cloud (Plotly)

For a web-ready visualization you can rotate, pan, and zoom, Plotly is the ideal choice. Since Plotly does not have a native 3d_text geometric trace, the industry workaround is to deploy a 3D scatter plot (go.Scatter3d) and use the text attribute as the visual markers.First, ensure we have Plotly installed:

```Shell
pip install plotly
```

Then run the following script:

```Python
import random
import plotly.graph_objects as go
from collections import Counter

# Sample text data
text = "python data-science visualization interactive static plotly matplotlib wordcloud coding analytics machine-learning insights graphics technology future intelligent web design dashboard map scale depth space axis"
words = text.split()
word_counts = Counter(words)

# Prepare lists to hold data structures
x_coords = []
y_coords = []
z_coords = []
word_list = []
font_sizes = []
color_indices = []

# Generate spatial values
for word, count in word_counts.items():
    x_coords.append(random.uniform(-50, 50))
    y_coords.append(random.uniform(-50, 50))
    z_coords.append(random.uniform(-50, 50))
    word_list.append(word)
  
    # Plotly scales text properties according to array variables
    font_sizes.append(12 + count * 10)
    color_indices.append(random.randint(0, 100))

# Construct the interactive 3D Scatter object
fig = go.Figure(data=[go.Scatter3d(
    x=x_coords,
    y=y_coords,
    z=z_coords,
    mode='text',
    text=word_list,
    hoverinfo='text',  # Shows the word when hovering
    textposition='middle center',
    textfont=dict(
        size=font_sizes,
        color=color_indices,
        colorscale='Viridis'
    )
)])

# Style the scene layout by removing grid lines and axes lines
fig.update_layout(
    title="Interactive 3D Word Cloud (Plotly)",
    scene=dict(
        xaxis=dict(showbackground=False, showticklabels=False, title=''),
        yaxis=dict(showbackground=False, showticklabels=False, title=''),
        zaxis=dict(showbackground=False, showticklabels=False, title='')
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

# Open in browser
fig.show()
```



## Quick Comparison

| Feature                 | Static (Matplotlib)                    | Interactive (Plotly)                            |
| ----------------------- | -------------------------------------- | ----------------------------------------------- |
| **Output Type**   | Image / Fixed window                   | HTML / Web-interactive canvas                   |
| **Interactivity** | None (Static projection)               | Rotatable, Zoomable, Hover Tooltips             |
| **Best Used For** | Paper prints, PDF reports, slide decks | Web applications, Jupyter Notebooks, dashboards |
