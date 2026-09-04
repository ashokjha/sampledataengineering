import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np

# Seed for consistency
random.seed(42)

# Source data pools
products = {
    "Electronics": {
        "Smartphones": ["iPhone 15", "Galaxy S24", "Pixel 8"],
        "Laptops": ["MacBook Air", "Dell XPS 13", "ThinkPad T14"],
        "Accessories": ["AirPods Pro", "Anker Power Bank", "Logitech Mouse"]
    },
    "Clothing": {
        "Topwear": ["Hoodie", "Graphic T-Shirt", "Flannel Shirt"],
        "Bottomwear": ["Jeans", "Chino Shorts", "Sweatpants"],
        "Footwear": ["Running Shoes", "Leather Boots", "White Sneakers"]
    },
    "Home & Kitchen": {
        "Appliances": ["Air Fryer", "Blender", "Espresso Machine"],
        "Cookware": ["Cast Iron Skillet", "Non-Stick Pan", "Knife Set"]
    }
}
regions = ["North", "South", "East", "West"]
start_date = datetime(2026, 1, 1)

base_data = []

# 1. Generate 80 unique records
for i in range(1, 81):
    category = random.choice(list(products.keys()))
    subcategory = random.choice(list(products[category].keys()))
    
    base_data.append({
        "Order_ID": f"ORD{1000 + i}",
        "Date": (start_date + timedelta(days=random.randint(0, 180))).strftime("%Y-%m-%d"),
        "Product": random.choice(products[category][subcategory]),
        "Category": category,
        "Subcategory": subcategory,
        "Quantity": random.randint(1, 15),
        "Price_Per_Unit": random.randint(15, 1200) if category == "Electronics" else random.randint(15, 150),
        "Region": random.choice(regions)
    })

# 2. Add 10 exact duplicate rows
exact_duplicates = random.choices(base_data, k=10)

# 3. Add 10 fuzzy duplicates (Simulate keying errors by changing one field)
fuzzy_duplicates = []
for item in random.choices(base_data, k=10):
    dupe = item.copy()
    error_field = random.choice(["Quantity", "Region", "Price_Per_Unit"])
    if error_field == "Quantity":
        dupe["Quantity"] = dupe["Quantity"] + 1
    elif error_field == "Price_Per_Unit":
        dupe["Price_Per_Unit"] = int(dupe["Price_Per_Unit"] * 1.05)
    else:
        dupe["Region"] = random.choice([r for r in regions if r != dupe["Region"]])
    fuzzy_duplicates.append(dupe)

# Combine and mix everything together
all_records = base_data + exact_duplicates + fuzzy_duplicates
for row in all_records:
    if random.random() < 0.10:
        row["Date"] = None  # Missing Date string
    if random.random() < 0.08:
        row["Product"] = ""  # Empty string representation
    if random.random() < 0.10:
        row["Quantity"] = np.nan  # NaN float representation
    if random.random() < 0.07:
        row["Region"] = None
random.shuffle(all_records)

# Convert to DataFrame
df = pd.DataFrame(all_records)
df.to_csv("order_data_with_duplicates.csv", index=False)
