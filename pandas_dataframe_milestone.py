"""
Creating Pandas DataFrames from Lists and Dictionaries
Pandas Milestone
"""

import pandas as pd


# =========================
# 1. DataFrame from Dictionary
# =========================

data_dict = {
    "Month": ["January", "February", "March"],
    "Energy_Usage": [1200, 1500, 1100],
    "Cost": [7200, 9000, 6600]
}

df_from_dict = pd.DataFrame(data_dict)

print("DataFrame Created from Dictionary:")
print(df_from_dict)
print()


# =========================
# 2. Inspecting DataFrame Structure
# =========================

print("Columns:", df_from_dict.columns)
print("Index:", df_from_dict.index)
print("Shape:", df_from_dict.shape)
print()


# =========================
# 3. Accessing Columns
# =========================

print("Energy Usage Column:")
print(df_from_dict["Energy_Usage"])
print()


# =========================
# 4. Basic Operations
# =========================

print("Total Energy Usage:", df_from_dict["Energy_Usage"].sum())
print("Average Cost:", df_from_dict["Cost"].mean())