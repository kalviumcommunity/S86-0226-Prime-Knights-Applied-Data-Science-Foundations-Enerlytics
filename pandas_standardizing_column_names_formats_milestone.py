"""
Standardizing Column Names and Data Formats
Pandas Milestone - Data Standardization and Formatting

This milestone focuses on:
- Cleaning and normalizing column names
- Applying consistent naming conventions (snake_case)
- Standardizing text data formats
- Standardizing numeric and date formats
- Building habits for reusable, clean datasets
"""

import pandas as pd
import numpy as np

# =========================
# 1. Understanding the Need for Standardization
# =========================
print("=" * 60)
print("1. UNDERSTANDING THE NEED FOR STANDARDIZATION")
print("=" * 60)

# Create a sample dataset with messy column names and inconsistent data
# This simulates real-world data from multiple sources
data = {
    "Customer ID": ["CUST001", "cust002", "CUST003", "cust004", "CUST005"],
    "Customer Name": ["  Alice Smith  ", "bob jones", "CHARLIE BROWN", "Diana Prince  ", "  eve torres"],
    "Energy Consumption (kWh)": [250.5, 310.8, 189.3, 425.6, 301.2],
    "Cost $": ["$150.30", "$186.50", "$113.60", "$255.35", "$180.70"],
    "Region/Zone": ["North", "SOUTH", "east", "West", "NORTH"],
    "Date Registered": ["2026-01-15", "01/20/2026", "2026-02-05", "02-10-2026", "2026-02-28"],
    "Email Address": ["alice@email.com  ", "  BOB@EMAIL.COM", "charlie@email.com", "DIANA@EMAIL.COM  ", "eve@email.com"],
    "isActive?": ["Yes", "yes", "NO", "Yes", "YES"]
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame with messy column names and inconsistent data:")
print(df)
print(f"\nDataFrame Shape: {df.shape}")
print("\nColumn names:")
print(df.columns.tolist())

print("\nPROBLEMS IDENTIFIED:")
print("✗ Column names have spaces")
print("✗ Mixed casing in column names")
print("✗ Special characters in column names ($, ?, /, ())")
print("✗ Inconsistent text casing in data")
print("✗ Extra whitespace in string values")
print("✗ Mixed date formats")
print("✗ Inconsistent category values (Yes/yes/YES/No/NO)")
print("✗ Currency symbols in numeric data")
print("-" * 60)

# =========================
# 2. Standardizing Column Names
# =========================
print("\n" + "=" * 60)
print("2. STANDARDIZING COLUMN NAMES")
print("=" * 60)

print("\nSTEP 1: Convert to lowercase")
df_clean = df.copy()
df_clean.columns = df_clean.columns.str.lower()
print("\nAfter converting to lowercase:")
print(df_clean.columns.tolist())

print("\n" + "-" * 60)
print("\nSTEP 2: Replace spaces with underscores")
df_clean.columns = df_clean.columns.str.replace(' ', '_')
print("\nAfter replacing spaces:")
print(df_clean.columns.tolist())

print("\n" + "-" * 60)
print("\nSTEP 3: Remove or replace special characters")
# Remove parentheses and their contents
df_clean.columns = df_clean.columns.str.replace(r'\(.*?\)', '', regex=True)
# Remove remaining special characters
df_clean.columns = df_clean.columns.str.replace(r'[^a-z0-9_]', '_', regex=True)
# Remove trailing underscores
df_clean.columns = df_clean.columns.str.rstrip('_')
# Replace multiple underscores with single underscore
df_clean.columns = df_clean.columns.str.replace(r'_+', '_', regex=True)

print("\nAfter removing special characters:")
print(df_clean.columns.tolist())

print("\n" + "-" * 60)
print("\nSTEP 4: Apply final naming conventions")
# Rename for clarity and consistency
df_clean = df_clean.rename(columns={
    'customer_id': 'customer_id',
    'customer_name': 'customer_name',
    'energy_consumption': 'consumption_kwh',
    'cost': 'cost_usd',
    'region_zone': 'region',
    'date_registered': 'registration_date',
    'email_address': 'email',
    'isactive': 'is_active'
})

print("\nFinal standardized column names:")
print(df_clean.columns.tolist())

print("\n" + "-" * 60)
print("\nCOMPARISON:")
print(f"Original: {df.columns.tolist()}")
print(f"Cleaned:  {df_clean.columns.tolist()}")

print("\nDataFrame with cleaned column names:")
print(df_clean)

# =========================
# 3. Choosing and Applying Naming Conventions
# =========================
print("\n" + "=" * 60)
print("3. NAMING CONVENTIONS BEST PRACTICES")
print("=" * 60)

print("""
RECOMMENDED: snake_case Convention

✓ GOOD EXAMPLES:
  - customer_id
  - consumption_kwh
  - registration_date
  - is_active
  - total_cost_usd
  - peak_hour_usage

✗ BAD EXAMPLES:
  - Customer ID (spaces)
  - customerID (camelCase - harder to read)
  - CUSTOMER_ID (SCREAMING_SNAKE_CASE - too aggressive)
  - cust_id (unclear abbreviation)
  - c_id (too abbreviated)
  - customer-id (hyphens - problematic in Python)

NAMING RULES:
1. Use lowercase letters only
2. Separate words with underscores
3. Use descriptive names (avoid unclear abbreviations)
4. Include units when relevant (kwh, usd, celsius)
5. Use consistent terminology across all columns
6. Prefix boolean columns with 'is_' or 'has_'
7. Keep names concise but clear (3-4 words max)

WHY snake_case?
- Easy to read: consumption_kwh vs consumptionKwh
- Python-friendly: no conflicts with syntax
- Consistent: one clear standard to follow
- Professional: widely used in data science
""")

# =========================
# 4. Standardizing Text Data
# =========================
print("\n" + "=" * 60)
print("4. STANDARDIZING TEXT DATA")
print("=" * 60)

print("\nOriginal text data (before standardization):")
print(df_clean[['customer_id', 'customer_name', 'region', 'email', 'is_active']].head())

print("\n" + "-" * 60)
print("\nSTEP 1: Strip whitespace from all string columns")
string_columns = df_clean.select_dtypes(include=['object']).columns
for col in string_columns:
    df_clean[col] = df_clean[col].str.strip()

print("\nAfter stripping whitespace:")
print(df_clean[['customer_name', 'email']].head())

print("\n" + "-" * 60)
print("\nSTEP 2: Standardize customer_id to uppercase")
df_clean['customer_id'] = df_clean['customer_id'].str.upper()
print("\nCustomer IDs (uppercase):")
print(df_clean['customer_id'])

print("\n" + "-" * 60)
print("\nSTEP 3: Standardize customer_name to title case")
df_clean['customer_name'] = df_clean['customer_name'].str.title()
print("\nCustomer Names (title case):")
print(df_clean['customer_name'])

print("\n" + "-" * 60)
print("\nSTEP 4: Standardize region to consistent capitalization")
df_clean['region'] = df_clean['region'].str.capitalize()
print("\nRegions (capitalized):")
print(df_clean['region'].value_counts())

print("\n" + "-" * 60)
print("\nSTEP 5: Standardize email to lowercase")
df_clean['email'] = df_clean['email'].str.lower()
print("\nEmails (lowercase):")
print(df_clean['email'])

print("\n" + "-" * 60)
print("\nSTEP 6: Standardize boolean values")
# Convert Yes/No variations to True/False
df_clean['is_active'] = df_clean['is_active'].str.upper().map({'YES': True, 'NO': False})
print("\nActive Status (boolean):")
print(df_clean['is_active'])
print(f"Data type: {df_clean['is_active'].dtype}")

print("\n" + "-" * 60)
print("\nAfter text standardization:")
print(df_clean[['customer_id', 'customer_name', 'region', 'email', 'is_active']])

# =========================
# 5. Standardizing Numeric Formats
# =========================
print("\n" + "=" * 60)
print("5. STANDARDIZING NUMERIC FORMATS")
print("=" * 60)

print("\nOriginal cost column (with currency symbols):")
print(df_clean['cost_usd'])
print(f"Data type: {df_clean['cost_usd'].dtype}")

print("\n" + "-" * 60)
print("\nSTEP 1: Remove currency symbols and convert to numeric")
# Remove $ and convert to float
df_clean['cost_usd'] = df_clean['cost_usd'].str.replace('$', '').astype(float)

print("\nCleaned cost column:")
print(df_clean['cost_usd'])
print(f"Data type: {df_clean['cost_usd'].dtype}")

print("\n" + "-" * 60)
print("\nSTEP 2: Verify numeric column is correct type")
print(f"\nConsumption kWh data type: {df_clean['consumption_kwh'].dtype}")
print("Consumption values:")
print(df_clean['consumption_kwh'])

print("\n" + "-" * 60)
print("\nSTEP 3: Round numeric values to consistent decimals")
df_clean['cost_usd'] = df_clean['cost_usd'].round(2)
df_clean['consumption_kwh'] = df_clean['consumption_kwh'].round(1)

print("\nRounded numeric values:")
print(df_clean[['consumption_kwh', 'cost_usd']])

# =========================
# 6. Standardizing Date Formats
# =========================
print("\n" + "=" * 60)
print("6. STANDARDIZING DATE FORMATS")
print("=" * 60)

print("\nOriginal registration_date column (mixed formats):")
print(df_clean['registration_date'])
print(f"Data type: {df_clean['registration_date'].dtype}")

print("\n" + "-" * 60)
print("\nSTEP 1: Convert to datetime (handling mixed formats)")
# Method 1: Use pd.to_datetime with format='mixed' (Pandas 2.0+)
# For older versions, we can parse manually or use errors='coerce'
try:
    df_clean['registration_date'] = pd.to_datetime(df_clean['registration_date'], 
                                                    format='mixed', 
                                                    errors='coerce')
except:
    # Fallback for older pandas versions
    df_clean['registration_date'] = pd.to_datetime(df_clean['registration_date'], 
                                                    infer_datetime_format=True, 
                                                    errors='coerce')

print("\nStandardized dates (datetime format):")
print(df_clean['registration_date'])
print(f"Data type: {df_clean['registration_date'].dtype}")

# Note: NaT (Not a Time) appears when date format couldn't be parsed
nat_count = df_clean['registration_date'].isna().sum()
if nat_count > 0:
    print(f"\nWarning: {nat_count} dates could not be parsed (shown as NaT)")

print("\n" + "-" * 60)
print("\nSTEP 2: Format dates consistently (if needed as string)")
df_clean['registration_date_formatted'] = df_clean['registration_date'].dt.strftime('%Y-%m-%d')

print("\nFormatted dates (YYYY-MM-DD):")
print(df_clean['registration_date_formatted'])

# Remove temporary column
df_clean = df_clean.drop('registration_date_formatted', axis=1)

# =========================
# 7. Final Comparison: Before and After
# =========================
print("\n" + "=" * 60)
print("7. FINAL COMPARISON: BEFORE AND AFTER")
print("=" * 60)

print("\n📋 BEFORE STANDARDIZATION:")
print("=" * 60)
print(df)
print("\nColumn names:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)

print("\n" + "=" * 60)
print("\n✨ AFTER STANDARDIZATION:")
print("=" * 60)
print(df_clean)
print("\nColumn names:", df_clean.columns.tolist())
print("\nData types:")
print(df_clean.dtypes)

print("\n" + "-" * 60)
print("\nIMPROVEMENTS MADE:")
print("✓ Column names: snake_case, no spaces, no special characters")
print("✓ Customer IDs: Consistent uppercase format")
print("✓ Customer names: Title case")
print("✓ Regions: Consistent capitalization")
print("✓ Emails: Lowercase")
print("✓ Boolean values: True/False instead of Yes/No")
print("✓ Cost values: Numeric (no $ symbol)")
print("✓ Dates: Consistent datetime format")
print("✓ All text: Trimmed whitespace")

# =========================
# 8. Creating a Standardization Function
# =========================
print("\n" + "=" * 60)
print("8. REUSABLE STANDARDIZATION FUNCTION")
print("=" * 60)

def standardize_column_names(df):
    """
    Standardize DataFrame column names to snake_case.
    
    Steps:
    1. Convert to lowercase
    2. Replace spaces with underscores
    3. Remove special characters
    4. Clean up multiple underscores
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame to standardize
        
    Returns:
    --------
    df : pd.DataFrame
        DataFrame with standardized column names
    """
    df = df.copy()
    
    # Convert to lowercase
    df.columns = df.columns.str.lower()
    
    # Replace spaces with underscores
    df.columns = df.columns.str.replace(' ', '_')
    
    # Remove parentheses and contents
    df.columns = df.columns.str.replace(r'\(.*?\)', '', regex=True)
    
    # Replace special characters with underscores
    df.columns = df.columns.str.replace(r'[^a-z0-9_]', '_', regex=True)
    
    # Clean up multiple underscores
    df.columns = df.columns.str.replace(r'_+', '_', regex=True)
    
    # Remove trailing/leading underscores
    df.columns = df.columns.str.strip('_')
    
    return df

# Test the function
print("\nTesting standardization function on sample data:")
test_df = pd.DataFrame({
    "Customer ID": [1, 2],
    "Energy Usage (kWh)": [100, 200],
    "Cost-Per-Unit ($)": [0.15, 0.18],
    "Is Active?": ["Yes", "No"]
})

print("\nBefore:")
print(test_df.columns.tolist())

test_df_clean = standardize_column_names(test_df)

print("\nAfter:")
print(test_df_clean.columns.tolist())

# =========================
# 9. Working with Real Energy Data
# =========================
print("\n" + "=" * 60)
print("9. APPLYING TO REAL ENERGY DATA")
print("=" * 60)

try:
    # Load actual energy data
    energy_df = pd.read_csv('data/processed/energy_usage_cleaned.csv')
    
    print(f"\nLoaded energy dataset: {energy_df.shape}")
    print("\nOriginal column names:")
    print(energy_df.columns.tolist())
    
    # Check if standardization is needed
    print("\n" + "-" * 60)
    print("\nChecking column name standards:")
    
    issues = []
    for col in energy_df.columns:
        if ' ' in col:
            issues.append(f"✗ '{col}' contains spaces")
        if col != col.lower():
            issues.append(f"✗ '{col}' is not lowercase")
        if any(char in col for char in ['(', ')', '$', '?', '-', '/']):
            issues.append(f"✗ '{col}' contains special characters")
    
    if issues:
        print("\nIssues found:")
        for issue in issues:
            print(issue)
        
        # Apply standardization
        energy_df_clean = standardize_column_names(energy_df)
        print("\nStandardized column names:")
        print(energy_df_clean.columns.tolist())
    else:
        print("\n✓ Column names are already standardized!")
        print("✓ All lowercase")
        print("✓ Using underscores")
        print("✓ No special characters")
    
    # Show sample data
    print("\n" + "-" * 60)
    print("\nSample of cleaned data:")
    print(energy_df.head())
    
    # Check data types
    print("\n" + "-" * 60)
    print("\nData types:")
    print(energy_df.dtypes)
    
except FileNotFoundError:
    print("\nNote: Energy data file not found. Using demonstration examples above.")

# =========================
# 10. Best Practices and Summary
# =========================
print("\n" + "=" * 60)
print("10. BEST PRACTICES AND SUMMARY")
print("=" * 60)

print("""
KEY TAKEAWAYS:

1. COLUMN NAMING STANDARDS:
   ✓ Use snake_case (all lowercase with underscores)
   ✓ Remove spaces and special characters
   ✓ Be descriptive but concise
   ✓ Include units when relevant (kwh, usd, celsius)
   ✓ Use consistent terminology

2. TEXT DATA STANDARDIZATION:
   ✓ Strip leading/trailing whitespace (.str.strip())
   ✓ Choose consistent casing (lower, upper, title, capitalize)
   ✓ Standardize category values
   ✓ Convert Yes/No to boolean True/False

3. NUMERIC DATA STANDARDIZATION:
   ✓ Remove currency symbols and convert to numeric
   ✓ Ensure correct data types (int, float)
   ✓ Round to consistent decimal places
   ✓ Handle missing or invalid values

4. DATE STANDARDIZATION:
   ✓ Convert to datetime using pd.to_datetime()
   ✓ Use consistent format (YYYY-MM-DD recommended)
   ✓ Handle mixed date formats properly
   ✓ Store as datetime for time operations

5. COMMON STRING OPERATIONS:
   - .str.lower() - Convert to lowercase
   - .str.upper() - Convert to uppercase
   - .str.title() - Title Case
   - .str.capitalize() - Capitalize first letter
   - .str.strip() - Remove whitespace
   - .str.replace() - Replace substrings

6. WHY STANDARDIZATION MATTERS:
   ✓ Makes code cleaner and more readable
   ✓ Prevents errors when merging datasets
   ✓ Easier to reference columns in analysis
   ✓ Improves collaboration and code reuse
   ✓ Enables reliable downstream processing

7. WHEN TO STANDARDIZE:
   ✓ Immediately after loading data
   ✓ Before merging multiple datasets
   ✓ Before any analysis or visualization
   ✓ As part of data cleaning pipeline

8. COMMON PITFALLS TO AVOID:
   ✗ Inconsistent naming across datasets
   ✗ Using spaces in column names
   ✗ Mixing different casing styles
   ✗ Over-abbreviating column names
   ✗ Forgetting to strip whitespace
   ✗ Leaving currency symbols in numeric data

STANDARDIZATION WORKFLOW:
1. Inspect data (df.head(), df.columns, df.dtypes)
2. Standardize column names
3. Standardize text data
4. Standardize numeric data
5. Standardize date formats
6. Verify results
7. Document changes

REMEMBER:
✓ Standardize early in your workflow
✓ Be consistent across all datasets
✓ Create reusable functions
✓ Document your conventions
✓ Clean names = Clean code = Clean analysis
""")

print("=" * 60)
print("MILESTONE COMPLETE")
print("=" * 60)
print("\nYou now know how to:")
print("✓ Clean and standardize column names")
print("✓ Apply snake_case naming convention")
print("✓ Standardize text, numeric, and date formats")
print("✓ Create reusable standardization functions")
print("✓ Build habits for clean, analysis-ready data")
