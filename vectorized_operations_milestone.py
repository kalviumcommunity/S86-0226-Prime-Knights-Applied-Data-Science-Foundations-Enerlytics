"""
Applying Vectorized Operations Instead of Python Loops
NumPy Milestone
"""

import numpy as np


# =========================
# Creating Sample Array
# =========================

data = np.array([10, 20, 30, 40, 50])
print("Original Array:", data)
print()


# =========================
# Loop-Based Approach
# =========================

loop_result = []

for value in data:
    loop_result.append(value * 2)

print("Loop-Based Result (value * 2):", loop_result)
print()


# =========================
# Vectorized Approach
# =========================

vectorized_result = data * 2
print("Vectorized Result (value * 2):", vectorized_result)
print()


# =========================
# Vectorized Comparisons
# =========================

greater_than_25 = data > 25
print("Elements Greater Than 25 (Boolean Mask):", greater_than_25)
print()

# Using boolean mask
filtered_values = data[data > 25]
print("Filtered Values Greater Than 25:", filtered_values)