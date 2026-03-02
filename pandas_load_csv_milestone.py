"""
Loading CSV Data into Pandas DataFrames
Pandas Milestone
"""

import pandas as pd


# =========================
# 1. Create a Sample CSV File
# =========================

sample_data = {
    "Month": ["January", "February", "March", "April"],
    "Energy_Usage": [1200, 1500, 1100, 1700],
    "Cost": [7200, 9000, 6600, 10200]
}

df_sample = pd.DataFrame(sample_data)

# Save to CSV
df_sample.to_csv("energy_data.csv", index=False)

print("Sample CSV file created.")
print()


# =========================
# 2. Load CSV File into DataFrame
# =========================

df_loaded = pd.read_csv("energy_data.csv")

print("Data Loaded from CSV:")
print(df_loaded)
print()


# =========================
# 3. Inspect Loaded Data
# =========================

print("First 3 Rows:")
print(df_loaded.head(3))
print()

print("Column Names:")
print(df_loaded.columns)
print()

print("Shape (Rows, Columns):", df_loaded.shape)
print()

print("Data Types:")
print(df_loaded.dtypes)