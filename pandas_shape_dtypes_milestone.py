import pandas as pd
import numpy as np

# ============================================================
# 1. Creating a Dataset with Mixed Types and Issues
# ============================================================
# We deliberately include issues like:
# - Numbers stored as strings
# - Missing values (NaN) that affect data types
# - Unexpected data types for columns
data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Energy_Usage_kWh": ["1200", "1500", "1100", "1700", "1400", "1600"],  # Numeric as strings!
    "Cost_USD": [7200, 9000, 6600, 10200, 8400, np.nan],                 # Contains NaN
    "Is_Peak_Month": [False, True, False, True, False, True],             # Boolean
    "Customer_ID": [101, 102, 103, 104, 105, 106]                        # Integer
}

df = pd.DataFrame(data)

print("="*60)
print("PANDAS DATAFRAME INSPECTION: SHAPE & DTYPES")
print("="*60)
print()

# ============================================================
# 2. Inspecting DataFrame Shape
# ============================================================
# .shape returns a tuple: (number of rows, number of columns)
shape = df.shape
rows = shape[0]
cols = shape[1]

print("STEP 1: Understanding DataFrame Shape")
print(f"Full Shape Tuple: {shape}")
print(f"Number of Rows (Observations): {rows}")
print(f"Number of Columns (Features/Attributes): {cols}")
print("-" * 60)
print("Insight: This dataset has 6 records and 5 attributes.")
print()

# ============================================================
# 3. Inspecting Column Data Types
# ============================================================
# .dtypes shows the data type of each column
print("STEP 2: Inspecting Column Data Types")
print(df.dtypes)
print("-" * 60)

# ============================================================
# 4. Detecting Type-Related Issues
# ============================================================
print("STEP 3: Critical Analysis of Data Types")
print()

# Issue 1: Numeric column stored as Object (String)
print("Checking for 'Object' types in numeric columns:")
if df['Energy_Usage_kWh'].dtype == 'object':
    print("⚠️ WARNING: 'Energy_Usage_kWh' is stored as 'object' (string).")
    print("   Analysis: You cannot perform math operations (like .mean()) until converted.")

# Issue 2: Missing values affecting types
print("\nChecking for Missing Values:")
print(df.isnull().sum())
if df['Cost_USD'].isnull().any():
    print("⚠️ NOTE: 'Cost_USD' contains NaN. In Pandas, presence of NaN ")
    print("   often forces numeric columns to become 'float64'.")

# Issue 3: Integer vs Boolean
print(f"\n'Customer_ID' is: {df['Customer_ID'].dtype}")
print(f"'Is_Peak_Month' is: {df['Is_Peak_Month'].dtype}")

print()
print("="*60)
print("INSPECTION COMPLETE")
print("="*60)
print("Summary: Always check shape and dtypes immediately after loading.")
print("This prevents invalid operations and ensures data integrity.")
print("="*60)
