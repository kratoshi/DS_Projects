import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

file_path = "/home/kratoshi/DataThings/DS_Projects/data_sets/epa-sea-level.csv"
df = pd.read_csv(file_path)

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points', color='blue')

# Line of best fit for all data
slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_pred_all = pd.Series(range(1880, 2051))
y_pred_all = slope * x_pred_all + intercept
plt.plot(x_pred_all, y_pred_all, color='red', label='Best Fit Line (1880-2050)')

# Line of best fit for data from 2000 onward
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
x_pred_recent = pd.Series(range(2000, 2051))
y_pred_recent = slope_recent * x_pred_recent + intercept_recent
plt.plot(x_pred_recent, y_pred_recent, color='green', label='Best Fit Line (2000-2050)')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Display the plot
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("/home/kratoshi/DataThings/DS_Projects/charts/sea_level_plot.png")

#Testing out my github access token