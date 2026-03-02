"""
NumPy Arrays Milestone
Demonstrates creating arrays from Python lists,
inspecting properties, and performing basic operations.
"""

# =========================
# Import Section
# =========================

import numpy as np


# =========================
# Creating NumPy Arrays
# =========================

# 1D array from Python list
energy_units_list = [10, 20, 30, 40, 50]
energy_units_array = np.array(energy_units_list)

print("1D NumPy Array:")
print(energy_units_array)
print()


# 2D array from nested list
monthly_data_list = [
    [100, 200, 300],
    [150, 250, 350]
]

monthly_data_array = np.array(monthly_data_list)

print("2D NumPy Array:")
print(monthly_data_array)
print()


# =========================
# Inspecting Array Properties
# =========================

print("Shape of 2D array:", monthly_data_array.shape)
print("Data type of array:", monthly_data_array.dtype)
print("Number of dimensions:", monthly_data_array.ndim)
print()


# =========================
# Basic Array Operations
# =========================

# Element-wise addition
increased_usage = energy_units_array + 5
print("After Adding 5 to Each Element:")
print(increased_usage)

# Element-wise multiplication
scaled_usage = energy_units_array * 2
print("After Multiplying Each Element by 2:")
print(scaled_usage)