"""
Selecting and Filtering Data in Pandas DataFrames
Pandas Milestone
"""

import pandas as pd


# =========================
# Creating Sample DataFrame
# =========================

data = {
    "Month": ["January", "February", "March", "April"],
    "Energy_Usage": [1200, 1500, 1100, 1700],
    "Cost": [7200, 9000, 6600, 10200]
}

df = pd.DataFrame(data)

print("Full DataFrame:")
print(df)
print()


# =========================
# Selecting a Column
# =========================

print("Energy Usage Column:")
print(df["Energy_Usage"])
print()


# =========================
# Selecting Multiple Columns
# =========================

print("Month and Cost Columns:")
print(df[["Month", "Cost"]])
print()


# =========================
# Selecting Rows using iloc
# =========================

print("First Row (Position-based):")
print(df.iloc[0])
print()


# =========================
# Selecting Rows using loc
# =========================

print("Row with Index 2 (Label-based):")
print(df.loc[2])
print()


# =========================
# Filtering with Condition
# =========================

print("Months where Energy Usage > 1300:")
print(df[df["Energy_Usage"] > 1300])