"""
Handling Missing Values in DataFrames
Pandas Milestone - Missing Value Handling (Drop and Fill)

This milestone focuses on:
- Dropping missing values safely
- Filling missing values with constants or statistics
- Understanding trade-offs between dropping and filling
- Avoiding common pitfalls in data cleaning
"""

import pandas as pd
import numpy as np

# =========================
# 1. Loading Data with Missing Values
# =========================
print("=" * 60)
print("1. SAMPLE DATAFRAME WITH MISSING VALUES")
print("=" * 60)

# Create a sample dataset representing energy consumption and costs
data = {
    "Date": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05", "2026-01-06", "2026-01-07"],
    "Customer_ID": ["CUST001", "CUST002", None, "CUST004", "CUST005", "CUST006", "CUST007"],
    "Region": ["North", "South", "East", "West", "North", None, "South"],
    "Consumption_kWh": [250.5, None, 180.2, 320.4, None, 290.1, 210.5],
    "Temperature": [18, 19, None, 21, 22, 20, None],
    "Cost": [150.0, 185.5, 108.8, 192.2, None, 175.0, 130.0],
    "Notes": [None, None, "Faulty meter", None, None, "High usage", None]
}

# Original DataFrame
df = pd.DataFrame(data)

print("\nOriginal DataFrame with missing values:")
print(df)
print("\nInitial Missing Values Count:")
print(df.isnull().sum())
print(f"\nDataFrame Shape: {df.shape}")
print("-" * 60)

# =========================
# 2. Dropping Missing Values
# =========================
print("\n" + "=" * 60)
print("2. DROPPING MISSING VALUES (dropna)")
print("=" * 60)

# Strategy A: Drop any row containing at least one missing value
df_dropped_rows = df.dropna()
print("\nStrategy A: Drop rows with ANY missing value (dropna())")
print(f"Shape after dropping rows: {df_dropped_rows.shape}")
print(df_dropped_rows)

# Strategy B: Drop columns with many missing values
# Let's drop columns where more than 50% of the data is missing (like 'Notes')
df_dropped_cols = df.dropna(axis=1, thresh=4) # Keep columns with at least 4 non-NaN values
print("\nStrategy B: Drop columns with excessive missing data (axis=1)")
print(f"Shape after dropping columns: {df_dropped_cols.shape}")
print(df_dropped_cols.head())

# Strategy C: Drop rows ONLY if specific columns are missing
df_dropped_subset = df.dropna(subset=['Customer_ID', 'Region'])
print("\nStrategy C: Drop rows only if 'Customer_ID' or 'Region' is missing")
print(f"Shape after subset drop: {df_dropped_subset.shape}")
print(df_dropped_subset)
print("-" * 60)

# =========================
# 3. Filling Missing Values
# =========================
print("\n" + "=" * 60)
print("3. FILLING MISSING VALUES (fillna)")
print("=" * 60)

# Create a copy for filling
df_filled = df.copy()

# Strategy A: Fill with a constant value (Categorical)
df_filled['Region'] = df_filled['Region'].fillna("Unknown")
df_filled['Customer_ID'] = df_filled['Customer_ID'].fillna("UNKNOWN_ID")
print("\nStrategy A: Fill categorical missing values with 'Unknown'")

# Strategy B: Fill with Summary Statistics (Numeric)
# Fill Consumption_kWh with Mean
mean_consumption = df_filled['Consumption_kWh'].mean()
df_filled['Consumption_kWh'] = df_filled['Consumption_kWh'].fillna(mean_consumption)
print(f"Strategy B: Fill 'Consumption_kWh' with Mean ({mean_consumption:.2f})")

# Fill Temperature with Median
median_temp = df_filled['Temperature'].median()
df_filled['Temperature'] = df_filled['Temperature'].fillna(median_temp)
print(f"Strategy C: Fill 'Temperature' with Median ({median_temp})")

# Fill Cost with Mode (or zero if appropriate, but let's use mean here)
mean_cost = df_filled['Cost'].mean()
df_filled['Cost'] = df_filled['Cost'].fillna(mean_cost)
print(f"Strategy D: Fill 'Cost' with Mean ({mean_cost:.2f})")

# Strategy E: Fill 'Notes' with 'No Notes'
df_filled['Notes'] = df_filled['Notes'].fillna("No Notes")

print("\nDataFrame after filling ALL missing values:")
print(df_filled)
print("\nMissing Values Count after filling:")
print(df_filled.isnull().sum())
print("-" * 60)

# =========================
# 4. Comparison and Insights
# =========================
print("\n" + "=" * 60)
print("4. COMPARISON AND INSIGHTS")
print("=" * 60)

print(f"Original Shape: {df.shape}")
print(f"Dropped Shape:  {df_dropped_rows.shape} (Lost {len(df) - len(df_dropped_rows)} rows)")
print(f"Filled Shape:   {df_filled.shape} (Preserved all rows)")

print("\nTakeaways:")
print("- Dropping (dropna) is safest for small amounts of missing data but reduces sample size.")
print("- Filling (fillna) preserves data size but introduces assumptions (mean/median).")
print("- Categorical data should be filled with a constant like 'Unknown' or the Mode.")
print("- Numeric data is usually filled with Mean (for normal data) or Median (if outliers exist).")
print("-" * 60)

# =========================
# 5. Best Practices Checklist
# =========================
print("\n" + "=" * 60)
print("5. BEST PRACTICES CHECKLIST")
print("=" * 60)

print("""
✓ Never drop data without checking the percentage missing.
✓ Use subset parameter in dropna() to avoid losing too much data.
✓ Use Mean for numeric data without significant outliers.
✓ Use Median for numeric data with outliers.
✓ Use Mode or 'Unknown' for categorical data.
✓ Always verify the result using .isnull().sum() after cleaning.
✓ Consider if the missing data itself is informative (e.g., 'Notes' missing means no issues).
""")
