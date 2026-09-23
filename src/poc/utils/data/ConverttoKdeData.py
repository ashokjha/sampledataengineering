import sys
import numpy as np
import pandas as pd
from scipy.stats import gaussian_kde

# 1. Load data

datafile = sys.argv[1]
df = pd.read_csv(datafile)

kde_records = []
# 2. Compute smooth KDE coordinates for each column group
for category, group in df.groupby("Category"):
    values = group["Value"].values
    kde_func = gaussian_kde(
        values, bw_method=0.3
    )  # Adjust bandwidth to change curve smoothness

    # Generate 200 continuous calculation points along the vertical axis
    y_range = np.linspace(values.min() - 5, values.max() + 5, 200)
    density = kde_func(y_range)

    # Scale density for clean visualization layout width
    density_scaled = density / density.max() * 0.3

    # Generate left and right mirrored coordinate records
    for y, d in zip(y_range, density_scaled):
        kde_records.append(
            {"Category": category, "Value_Axis": y, "Density_Axis": d, "Side": "Right"}
        )
        kde_records.append(
            {"Category": category, "Value_Axis": y, "Density_Axis": -d, "Side": "Left"}
        )

kdefile = datafile[0 : datafile.rfind("/") + 1] + sys.argv[2]
pd.DataFrame(kde_records).to_csv(kdefile, index=False)
