"""
Understanding NumPy Broadcasting
NumPy Milestone
"""

import numpy as np


# =========================
# 1. Broadcasting with Scalar
# =========================

array_1d = np.array([10, 20, 30])

print("Original 1D Array:", array_1d)
print("Shape:", array_1d.shape)
print()

scalar_result = array_1d + 5
print("After Adding Scalar 5:", scalar_result)
print()


# =========================
# 2. Broadcasting Between 1D Arrays
# =========================

array_a = np.array([1, 2, 3])
array_b = np.array([10, 20, 30])

print("Array A:", array_a)
print("Array B:", array_b)
print("Element-wise Addition:", array_a + array_b)
print()


# =========================
# 3. Broadcasting 2D and 1D Arrays
# =========================

two_d_array = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

one_d_array = np.array([10, 20, 30])

print("2D Array:")
print(two_d_array)
print("Shape:", two_d_array.shape)

print("1D Array:")
print(one_d_array)
print("Shape:", one_d_array.shape)
print()

broadcast_result = two_d_array + one_d_array
print("Broadcasted Result (2D + 1D):")
print(broadcast_result)
print()


# =========================
# Understanding Shape Logic
# =========================

print("Explanation:")
print("2D Shape:", two_d_array.shape)
print("1D Shape:", one_d_array.shape)
print("NumPy aligns from the rightmost dimension.")
print("Since 3 matches 3, broadcasting works across rows.")