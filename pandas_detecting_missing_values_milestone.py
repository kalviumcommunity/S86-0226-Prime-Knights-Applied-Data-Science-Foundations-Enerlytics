"""
Detecting Missing Values in DataFrames
Pandas Milestone - Missing Value Detection

This milestone focuses on:
- Understanding what missing values represent
- Detecting missing values in a DataFrame
- Identifying missing values at row and column level
- Counting and summarizing missing data
- Inspecting rows with missing entries
"""

import pandas as pd
import numpy as np


# =========================
# 1. Understanding Missing Values
# =========================
print("=" * 60)
print("1. UNDERSTANDING MISSING VALUES")
print("=" * 60)

# Missing values in Pandas are represented as:
# - NaN (Not a Number) - for numeric data
# - None - Python's null value
# - pd.NA - Pandas' missing value indicator

print("\nCommon representations of missing data:")
print("- NaN (Not a Number)")
print("- None (Python null)")
print("- pd.NA (Pandas missing indicator)")
print()


# =========================
# 2. Creating Sample Data with Missing Values
# =========================
print("=" * 60)
print("2. SAMPLE DATAFRAME WITH MISSING VALUES")
print("=" * 60)

# Create a sample dataset with intentional missing values
data = {
    "Date": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05"],
    "Customer_ID": ["CUST001", "CUST002", None, "CUST004", "CUST005"],
    "Consumption_kWh": [2.5, None, 1.8, 3.2, None],
    "Temperature": [18, 19, None, 21, 22],
    "Cost": [15.0, 18.5, 10.8, 19.2, None]
}

df = pd.DataFrame(data)

print("\nSample DataFrame:")
print(df)
print()


# =========================
# 3. Detecting Missing Values
# =========================
print("=" * 60)
print("3. DETECTING MISSING VALUES")
print("=" * 60)

# Method 1: Using isnull() - Returns boolean DataFrame
print("\nUsing isnull() - Returns True where values are missing:")
print(df.isnull())
print()

# Method 2: Using isna() - Same as isnull()
print("Using isna() - Identical to isnull():")
print(df.isna())
print()

# Note: isnull() and isna() are equivalent in Pandas
print("Note: isnull() and isna() are equivalent methods")
print()


# =========================
# 4. Counting Missing Values
# =========================
print("=" * 60)
print("4. COUNTING MISSING VALUES")
print("=" * 60)

# Count missing values per column
print("\nMissing values count per column:")
missing_count = df.isnull().sum()
print(missing_count)
print()

# Calculate percentage of missing values per column
print("Percentage of missing values per column:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage)
print()

# Total number of missing values in entire DataFrame
print("Total missing values in DataFrame:", df.isnull().sum().sum())
print()


# =========================
# 5. Identifying Columns with Missing Data
# =========================
print("=" * 60)
print("5. COLUMNS WITH MISSING DATA")
print("=" * 60)

# Get columns that have at least one missing value
columns_with_missing = df.columns[df.isnull().any()].tolist()
print("\nColumns containing missing values:")
print(columns_with_missing)
print()

# Get columns with no missing values
columns_without_missing = df.columns[~df.isnull().any()].tolist()
print("Columns with complete data (no missing values):")
print(columns_without_missing)
print()


# =========================
# 6. Inspecting Rows with Missing Data
# =========================
print("=" * 60)
print("6. INSPECTING ROWS WITH MISSING DATA")
print("=" * 60)

# Get rows that contain at least one missing value
rows_with_missing = df[df.isnull().any(axis=1)]
print("\nRows containing missing values:")
print(rows_with_missing)
print()

# Get rows with no missing values (complete cases)
complete_rows = df[~df.isnull().any(axis=1)]
print("Rows with complete data (no missing values):")
print(complete_rows)
print()

# Count how many rows have missing values
print(f"Number of rows with missing data: {len(rows_with_missing)}")
print(f"Number of complete rows: {len(complete_rows)}")
print()


# =========================
# 7. Detailed Missing Value Summary
# =========================
print("=" * 60)
print("7. COMPREHENSIVE MISSING VALUE SUMMARY")
print("=" * 60)

# Create a summary table for missing values
missing_summary = pd.DataFrame({
    'Column': df.columns,
    'Missing_Count': df.isnull().sum().values,
    'Missing_Percentage': (df.isnull().sum() / len(df) * 100).values,
    'Data_Type': df.dtypes.values
})

print("\nDetailed Missing Value Summary:")
print(missing_summary)
print()


# =========================
# 8. Working with Real Data (if available)
# =========================
print("=" * 60)
print("8. CHECKING REAL DATASET FOR MISSING VALUES")
print("=" * 60)

try:
    # Load the actual energy usage data
    real_df = pd.read_csv("data/raw/energy_usage_sample.csv")
    
    print("\nReal Dataset - First 5 rows:")
    print(real_df.head())
    print()
    
    print("Missing values in real dataset:")
    real_missing = real_df.isnull().sum()
    print(real_missing)
    print()
    
    if real_missing.sum() == 0:
        print("✓ Good news! The real dataset has no missing values.")
    else:
        print(f"⚠ Warning! The real dataset has {real_missing.sum()} missing values.")
    print()
    
except FileNotFoundError:
    print("\n⚠ Real data file not found. Using sample data only.")
    print()


# =========================
# 9. Key Takeaways
# =========================
print("=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
1. Always check for missing values BEFORE analysis
2. Use isnull() or isna() to detect missing values
3. Use .sum() to count missing values per column
4. Calculate percentages to understand severity
5. Inspect rows with missing data for patterns
6. Missing data detection is a critical first step
7. Detection comes BEFORE cleaning or imputation

Remember: Missing data affects all downstream analysis!
""")


# =========================
# 10. Best Practices Checklist
# =========================
print("=" * 60)
print("BEST PRACTICES CHECKLIST")
print("=" * 60)

print("""
✓ Load your DataFrame
✓ Check df.info() for overview
✓ Use df.isnull().sum() for missing counts
✓ Calculate missing percentages
✓ Inspect rows with missing data
✓ Document which columns have missing values
✓ Decide on handling strategy AFTER detection
✓ Never ignore missing values silently
""")
