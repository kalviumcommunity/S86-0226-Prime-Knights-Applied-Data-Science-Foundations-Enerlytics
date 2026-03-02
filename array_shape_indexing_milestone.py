"""
Understanding Array Shape, Dimensions, and Index Positions
NumPy Milestone
"""

import numpy as np


# =========================
# 1D Array Example
# =========================

one_d_array = np.array([10, 20, 30, 40, 50])

print("1D Array:")
print(one_d_array)
print("Shape:", one_d_array.shape)
print("Dimensions:", one_d_array.ndim)
print()

# Accessing elements in 1D array
print("First element:", one_d_array[0])
print("Third element:", one_d_array[2])
print()


# =========================
# 2D Array Example
# =========================

two_d_array = np.array([
    [100, 200, 300],
    [400, 500, 600]
])

print("2D Array:")
print(two_d_array)
print("Shape:", two_d_array.shape)
print("Dimensions:", two_d_array.ndim)
print()

# Accessing elements in 2D array
print("Element at row 0, column 1:", two_d_array[0, 1])
print("Element at row 1, column 2:", two_d_array[1, 2])
print()

# Accessing full row
print("First row:", two_d_array[0])

# Accessing full column
print("Second column:", two_d_array[:, 1])