"""
Inspecting DataFrames Using head(), info(), and describe()
Pandas Milestone
"""

import pandas as pd


# =========================
# Creating Sample DataFrame
# =========================

data = {
    "Month": ["January", "February", "March", "April", "May"],
    "Energy_Usage": [1200, 1500, 1100, 1700, 1400],
    "Cost": [7200, 9000, 6600, 10200, 8400]
}

df = pd.DataFrame(data)

print("Full DataFrame:")
print(df)
print()


# =========================
# 1. Using head()
# =========================

print("Using head():")
print(df.head())  # default shows first 5 rows
print()


# =========================
# 2. Using info()
# =========================

print("Using info():")
df.info()
print()


# =========================
# 3. Using describe()
# =========================

print("Using describe():")
print(df.describe())
print()