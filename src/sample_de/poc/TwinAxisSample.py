import matplotlib.pyplot as plt
import pandas as pd

# Dummy Stock Data
data = {
    'Date': pd.date_range(start='2026-08-01', periods=5, freq='D'),
    'Price': [150.25, 153.40, 152.10, 155.80, 158.20],
    'Volume': [1200000, 1500000, 950000, 2100000, 1800000]
}
df = pd.DataFrame(data)

fig, ax1 = plt.subplots(figsize=(10, 5))

# Primary Axis (Left) - Stock Price
color = '#1f77b4'
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Price ($)', color=color)
ax1.plot(df['Date'], df['Price'], color=color, linewidth=2, marker='o')
ax1.tick_params(axis='y', labelcolor=color)

# Secondary Axis (Right) - Trading Volume
ax2 = ax1.twinx()  
color = '#ff7f0e'
ax2.set_ylabel('Volume', color=color)
ax2.bar(df['Date'], df['Volume'], color=color, alpha=0.3, width=0.4)
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Stock Price vs. Trading Volume (Dual Axis)')
fig.tight_layout()
plt.show()