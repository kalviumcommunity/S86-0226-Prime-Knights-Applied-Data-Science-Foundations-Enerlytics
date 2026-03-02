"""
Performing Basic Mathematical Operations on NumPy Arrays
NumPy Milestone
"""

import numpy as np


# =========================
# Creating Arrays
# =========================

array_a = np.array([10, 20, 30, 40])
array_b = np.array([1, 2, 3, 4])

print("Array A:", array_a)
print("Array B:", array_b)
print()


# =========================
# Element-wise Operations
# =========================

print("Element-wise Addition:", array_a + array_b)
print("Element-wise Subtraction:", array_a - array_b)
print("Element-wise Multiplication:", array_a * array_b)
print("Element-wise Division:", array_a / array_b)
print()


# =========================
# Scalar Operations
# =========================

print("Add Scalar (5) to Array A:", array_a + 5)
print("Multiply Array A by 2:", array_a * 2)
print()


# =========================
# Comparing with Python Lists
# =========================

list_a = [10, 20, 30, 40]
list_b = [1, 2, 3, 4]

print("Python List Addition:", list_a + list_b)
print("NumPy Array Addition:", array_a + array_b)