"""
Computing Summary Statistics for Pandas DataFrames
Pandas Milestone
"""

import pandas as pd
import numpy as np

# ==========================================
# 1. Load / Create a Representative Dataset
# ==========================================

# We create a more varied dataset to better illustrate statistics like spread and outliers
data = {
    "District": ["North", "South", "East", "West", "Central", "Northwest", "Southeast", "Southwest"],
    "Energy_Usage_kWh": [1200, 1500, 1100, 1700, 1300, 2500, 1150, 1250], # Note the 2500 outlier
    "Operation_Cost_INR": [7200, 9000, 6600, 10200, 7800, 15000, 6900, 7500],
    "Staff_Count": [5, 6, 4, 7, 5, 8, 4, 5]
}

df = pd.DataFrame(data)

print("--- Energy Consumption Dataset ---")
print(df)
print("\n")

# ==========================================
# 2. Computing Statistics for a Single Column
# ==========================================

print("--- Statistics for 'Energy_Usage_kWh' ---")
# Selecting a single numeric column
energy_col = df["Energy_Usage_kWh"]

# Computing individual statistics
mean_val = energy_col.mean()
median_val = energy_col.median()
min_val = energy_col.min()
max_val = energy_col.max()
std_val = energy_col.std()
count_val = energy_col.count()

print(f"Count:  {count_val}")
print(f"Mean:   {mean_val:.2f} (Average usage)")
print(f"Median: {median_val:.2f} (Middle value)")
print(f"Min:    {min_val}")
print(f"Max:    {max_val}")
print(f"StdDev: {std_val:.2f} (Spread of data)")
print("\n")

# Interpretation Note:
# If Mean > Median, it suggests the data might be right-skewed (potentially due to high outliers).
# Here, Mean (1462.5) is higher than Median (1275.0), primarily due to the 'Northwest' district (2500).

# ==========================================
# 3. Using .describe() for Quick Summary
# ==========================================

print("--- Quick Summary using .describe() ---")
# Returns a Series with all common statistics
summary_stats = energy_col.describe()
print(summary_stats)
print("\n")

# ==========================================
# 4. Comparing Statistics Across Columns
# ==========================================

print("--- Comparison: Energy Usage vs Staff Count ---")
# Let's compare the variability (Standard Deviation relative to Mean)
energy_rel_std = df["Energy_Usage_kWh"].std() / df["Energy_Usage_kWh"].mean()
staff_rel_std = df["Staff_Count"].std() / df["Staff_Count"].mean()

print(f"Energy Usage Relative Variability: {energy_rel_std:.4f}")
print(f"Staff Count Relative Variability:  {staff_rel_std:.4f}")

if energy_rel_std > staff_rel_std:
    print("Interpretation: Energy usage varies more significantly across districts than staff count.")
else:
    print("Interpretation: Staff count shows higher relative variability than energy usage.")

# ==========================================
# 5. Identifying Unusual Values using Summaries
# ==========================================

# Using the Max and Mean/Median to spot potential outliers
print("\n--- Outlier Intuition ---")
max_energy = df["Energy_Usage_kWh"].max()
avg_energy = df["Energy_Usage_kWh"].mean()

print(f"Max Energy: {max_energy}, Mean Energy: {avg_energy:.2f}")
if max_energy > 1.5 * avg_energy:
    print("Flag: There is an unusually high value in the energy column (Potential Outlier).")
