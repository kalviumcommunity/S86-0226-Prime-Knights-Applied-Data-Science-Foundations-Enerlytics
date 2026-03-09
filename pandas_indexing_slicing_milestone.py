import pandas as pd
import numpy as np

# ============================================================
# 1. Creating a Sample Dataset for Selection Practice
# ============================================================
# We use a dataset with meaningful labels and positions.
data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Energy_Usage_kWh": [1200, 1500, 1100, 1700, 1400, 1600],
    "Cost_USD": [7200, 9000, 6600, 10200, 8400, 9600],
    "Peak_Status": ["Normal", "Peak", "Normal", "Peak", "Normal", "Peak"]
}

# We set the 'Month' column as the index to demonstrate label-based selection (loc)
df = pd.DataFrame(data).set_index("Month")

print("="*60)
print("PANDAS DATA SELECTION: INDEXING AND SLICING")
print("="*60)
print("Initial DataFrame (Index is Month):")
print(df)
print("-" * 60)
print()

# ============================================================
# 2. Selecting Columns by Name
# ============================================================
print("STEP 1: SELECTING COLUMNS")

# A. Selecting a single column (returns a Series)
energy_col = df["Energy_Usage_kWh"]
print("Single Column Selection (Energy_Usage_kWh):")
print(energy_col.head(3))
print(f"Result type: {type(energy_col)}")
print()

# B. Selecting multiple columns (returns a DataFrame)
subset_cols = df[["Energy_Usage_kWh", "Cost_USD"]]
print("Multiple Column Selection:")
print(subset_cols.head(3))
print(f"Result type: {type(subset_cols)}")
print("-" * 60)
print()

# ============================================================
# 3. Selecting Rows by Position (iloc)
# ============================================================
print("STEP 2: SELECTING ROWS BY POSITION (iloc)")

# A. Selecting a single row by integer position (0 is the first row)
first_row = df.iloc[0]
print("First Row (index 0):")
print(first_row)
print()

# B. Slicing rows by position (stop index is EXCLUSIVE)
# This selects rows at index 1 and 2 (February and March)
row_slice = df.iloc[1:3]
print("Positional Slice [1:3] (Rows at index 1 and 2):")
print(row_slice)
print("Note: In iloc slices, the stop index is EXCLUSIVE.")
print("-" * 60)
print()

# ============================================================
# 4. Selecting Rows by Label (loc)
# ============================================================
print("STEP 3: SELECTING ROWS BY LABEL (loc)")

# A. Selecting a single row by label
march_row = df.loc["March"]
print("Single Row Label ('March'):")
print(march_row)
print()

# B. Slicing rows by label (stop label is INCLUSIVE)
# This selects everything from 'January' to 'March'
label_slice = df.loc["January":"March"]
print("Label Slice ['January':'March']:")
print(label_slice)
print("Note: In loc slices, the stop label is INCLUSIVE.")
print("-" * 60)
print()

# ============================================================
# 5. Selecting Rows and Columns Together
# ============================================================
print("STEP 4: SELECTING ROWS AND COLUMNS TOGETHER")

# A. Using labels (loc[row_label, col_label])
# Selecting Cost_USD for February and April
combined_loc = df.loc[["February", "April"], "Cost_USD"]
print("Specific Rows and Column using loc:")
print(combined_loc)
print()

# B. Using slices for both rows and columns
# First 3 rows, first 2 columns
combined_slice = df.iloc[0:3, 0:2]
print("Row and Column Slice using iloc [0:3, 0:2]:")
print(combined_slice)
print()

print("="*60)
print("SELECTION COMPLETE")
print("="*60)
print("Summary:")
print("1. df['col'] - Basic column selection.")
print("2. df.iloc[pos] - Positional indexing (zero-based).")
print("3. df.loc['label'] - Label-based indexing.")
print("4. loc and iloc can take [rows, cols] for precise selection.")
print("="*60)
