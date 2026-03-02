"""
Creating Pandas Series from Lists and NumPy Arrays
Pandas Milestone
"""

import pandas as pd
import numpy as np


# =========================
# 1. Series from Python List
# =========================

energy_list = [100, 200, 300, 400]

series_from_list = pd.Series(energy_list)

print("Series Created from Python List:")
print(series_from_list)
print()

print("Values:", series_from_list.values)
print("Index:", series_from_list.index)
print()


# =========================
# 2. Series from NumPy Array
# =========================

energy_array = np.array([500, 600, 700, 800])

series_from_array = pd.Series(energy_array)

print("Series Created from NumPy Array:")
print(series_from_array)
print()

print("Values:", series_from_array.values)
print("Index:", series_from_array.index)
print()


# =========================
# 3. Custom Index Example
# =========================

labeled_series = pd.Series(
    [1000, 1200, 1500],
    index=["January", "February", "March"]
)

print("Series with Custom Labels:")
print(labeled_series)
print()

print("Access by Label (February):", labeled_series["February"])
print("Access by Position (0):", labeled_series[0])