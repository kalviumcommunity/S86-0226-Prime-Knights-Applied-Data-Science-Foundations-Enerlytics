"""
Identifying and Removing Duplicate Records
Pandas Milestone - Duplicate Detection and Removal

This milestone focuses on:
- Understanding what duplicate records are
- Detecting duplicate rows in a DataFrame
- Identifying duplicates across all or selected columns
- Removing duplicates safely and intentionally
- Verifying results after deduplication
"""

import pandas as pd
import numpy as np

# =========================
# 1. Understanding Duplicate Records
# =========================
print("=" * 60)
print("1. UNDERSTANDING DUPLICATE RECORDS")
print("=" * 60)

# Create a sample dataset with duplicate records
# Simulating energy consumption data that might have duplicates due to:
# - Data entry errors
# - System glitches
# - Multiple data sources
data = {
    "timestamp": [
        "2026-02-01 08:00:00",
        "2026-02-01 09:00:00",
        "2026-02-01 08:00:00",  # Exact duplicate of row 0
        "2026-02-01 10:00:00",
        "2026-02-01 11:00:00",
        "2026-02-01 09:00:00",  # Exact duplicate of row 1
        "2026-02-01 12:00:00",
        "2026-02-01 10:00:00",  # Partial duplicate (same timestamp, different customer)
        "2026-02-01 13:00:00"
    ],
    "customer_id": [
        "CUST001",
        "CUST001",
        "CUST001",  # Duplicate
        "CUST002",
        "CUST002",
        "CUST001",  # Duplicate
        "CUST003",
        "CUST003",  # Different customer, same timestamp
        "CUST001"
    ],
    "consumption_kwh": [
        45.5,
        52.3,
        45.5,  # Duplicate
        38.9,
        41.2,
        52.3,  # Duplicate
        55.6,
        39.1,  # Different value
        48.7
    ],
    "temperature_celsius": [
        22,
        23,
        22,  # Duplicate
        21,
        22,
        23,  # Duplicate
        24,
        20,
        23
    ]
}

df = pd.DataFrame(data)

print("\nOriginal DataFrame (with duplicates):")
print(df)
print(f"\nDataFrame Shape: {df.shape}")
print(f"Total rows: {len(df)}")
print("\nNote: Rows 0 and 2 are exact duplicates")
print("Note: Rows 1 and 5 are exact duplicates")
print("Note: Rows 3 and 7 have same timestamp but different customers (not true duplicates)")
print("-" * 60)

# =========================
# 2. Detecting Duplicate Rows
# =========================
print("\n" + "=" * 60)
print("2. DETECTING DUPLICATE ROWS")
print("=" * 60)

# Method 1: Using duplicated() - returns boolean Series
print("\nMethod 1: Using duplicated() - Boolean indicators")
duplicate_mask = df.duplicated()
print("\nDuplicate boolean mask:")
print(duplicate_mask)
print(f"\nType: {type(duplicate_mask)}")

# Count duplicates
num_duplicates = duplicate_mask.sum()
print(f"\nNumber of duplicate rows: {num_duplicates}")

# View actual duplicate rows
print("\nActual duplicate rows:")
print(df[duplicate_mask])

# Method 2: Check for duplicates keeping first occurrence
print("\n" + "-" * 60)
print("\nMethod 2: duplicated(keep='first') - Mark duplicates, keep first")
duplicates_first = df.duplicated(keep='first')
print(duplicates_first)
print(f"Duplicates (keeping first): {duplicates_first.sum()}")

# Method 3: Check for duplicates keeping last occurrence
print("\n" + "-" * 60)
print("\nMethod 3: duplicated(keep='last') - Mark duplicates, keep last")
duplicates_last = df.duplicated(keep='last')
print(duplicates_last)
print(f"Duplicates (keeping last): {duplicates_last.sum()}")

# Method 4: Mark all duplicates (including original)
print("\n" + "-" * 60)
print("\nMethod 4: duplicated(keep=False) - Mark all occurrences as duplicates")
duplicates_all = df.duplicated(keep=False)
print(duplicates_all)
print(f"All duplicate occurrences: {duplicates_all.sum()}")

print("\nAll rows involved in duplication:")
print(df[duplicates_all])

# =========================
# 3. Detecting Duplicates on Specific Columns
# =========================
print("\n" + "=" * 60)
print("3. DETECTING DUPLICATES ON SPECIFIC COLUMNS")
print("=" * 60)

# Sometimes we only care about duplicates in specific columns
# For example, duplicate timestamp + customer_id combinations

print("\nScenario: Check for duplicate timestamp + customer_id combinations")
duplicates_subset = df.duplicated(subset=['timestamp', 'customer_id'])
print(f"\nDuplicates based on timestamp and customer_id: {duplicates_subset.sum()}")
print("\nDuplicate rows (based on timestamp + customer_id):")
print(df[duplicates_subset])

print("\n" + "-" * 60)
print("\nScenario: Check for duplicate customer_id only")
duplicates_customer = df.duplicated(subset=['customer_id'], keep=False)
print(f"\nRows with duplicate customer_id: {duplicates_customer.sum()}")
print("\nAll rows with repeated customer_id:")
print(df[duplicates_customer].sort_values('customer_id'))

print("\n" + "-" * 60)
print("\nScenario: Check for duplicate timestamp only")
duplicates_time = df.duplicated(subset=['timestamp'], keep=False)
print(f"\nRows with duplicate timestamp: {duplicates_time.sum()}")
print("\nAll rows with repeated timestamp:")
print(df[duplicates_time].sort_values('timestamp'))

# =========================
# 4. Removing Duplicate Records
# =========================
print("\n" + "=" * 60)
print("4. REMOVING DUPLICATE RECORDS")
print("=" * 60)

print("\nBefore Deduplication:")
print(f"Shape: {df.shape}")
print(f"Total rows: {len(df)}")

# Strategy 1: Remove duplicates, keep first occurrence (default)
print("\n" + "-" * 60)
print("\nStrategy 1: Keep first occurrence (default)")
df_dedup_first = df.drop_duplicates()
print(f"\nAfter removing duplicates (keep='first'):")
print(f"Shape: {df_dedup_first.shape}")
print(f"Total rows: {len(df_dedup_first)}")
print(f"Rows removed: {len(df) - len(df_dedup_first)}")
print("\nCleaned DataFrame:")
print(df_dedup_first)

# Strategy 2: Remove duplicates, keep last occurrence
print("\n" + "-" * 60)
print("\nStrategy 2: Keep last occurrence")
df_dedup_last = df.drop_duplicates(keep='last')
print(f"\nAfter removing duplicates (keep='last'):")
print(f"Shape: {df_dedup_last.shape}")
print(f"Total rows: {len(df_dedup_last)}")
print("\nCleaned DataFrame:")
print(df_dedup_last)

# Strategy 3: Remove all duplicate occurrences
print("\n" + "-" * 60)
print("\nStrategy 3: Remove all occurrences (keep=False)")
df_dedup_none = df.drop_duplicates(keep=False)
print(f"\nAfter removing all duplicate occurrences (keep=False):")
print(f"Shape: {df_dedup_none.shape}")
print(f"Total rows: {len(df_dedup_none)}")
print(f"Rows removed: {len(df) - len(df_dedup_none)}")
print("\nCleaned DataFrame (only unique rows):")
print(df_dedup_none)

# Strategy 4: Remove duplicates based on specific columns
print("\n" + "-" * 60)
print("\nStrategy 4: Remove duplicates based on timestamp + customer_id")
df_dedup_subset = df.drop_duplicates(subset=['timestamp', 'customer_id'])
print(f"\nAfter removing duplicates (based on timestamp + customer_id):")
print(f"Shape: {df_dedup_subset.shape}")
print(f"Total rows: {len(df_dedup_subset)}")
print(f"Rows removed: {len(df) - len(df_dedup_subset)}")
print("\nCleaned DataFrame:")
print(df_dedup_subset)

# =========================
# 5. Verifying Deduplication Results
# =========================
print("\n" + "=" * 60)
print("5. VERIFYING DEDUPLICATION RESULTS")
print("=" * 60)

# Choose the most appropriate cleaning strategy
# For energy data, we want unique timestamp + customer_id combinations
df_cleaned = df.drop_duplicates(subset=['timestamp', 'customer_id'], keep='first')

print("\nFinal Cleaned DataFrame:")
print(df_cleaned)

# Verification Step 1: Compare shapes
print("\n" + "-" * 60)
print("\nVerification Step 1: Shape Comparison")
print(f"Original shape: {df.shape}")
print(f"Cleaned shape: {df_cleaned.shape}")
print(f"Rows removed: {len(df) - len(df_cleaned)}")
print(f"Percentage removed: {((len(df) - len(df_cleaned)) / len(df) * 100):.2f}%")

# Verification Step 2: Recheck for duplicates
print("\n" + "-" * 60)
print("\nVerification Step 2: Recheck for Duplicates")
remaining_duplicates = df_cleaned.duplicated(subset=['timestamp', 'customer_id']).sum()
print(f"Remaining duplicates (timestamp + customer_id): {remaining_duplicates}")

if remaining_duplicates == 0:
    print("✓ SUCCESS: No duplicates remain!")
else:
    print("✗ WARNING: Duplicates still present!")

# Verification Step 3: Check data integrity
print("\n" + "-" * 60)
print("\nVerification Step 3: Data Integrity Check")
print(f"\nUnique timestamps in original: {df['timestamp'].nunique()}")
print(f"Unique timestamps in cleaned: {df_cleaned['timestamp'].nunique()}")
print(f"\nUnique customers in original: {df['customer_id'].nunique()}")
print(f"Unique customers in cleaned: {df_cleaned['customer_id'].nunique()}")

# Verification Step 4: Summary statistics comparison
print("\n" + "-" * 60)
print("\nVerification Step 4: Summary Statistics Comparison")
print("\nOriginal Data - Consumption Statistics:")
print(df['consumption_kwh'].describe())
print("\nCleaned Data - Consumption Statistics:")
print(df_cleaned['consumption_kwh'].describe())

# =========================
# 6. Working with Real Energy Data
# =========================
print("\n" + "=" * 60)
print("6. WORKING WITH REAL ENERGY DATA")
print("=" * 60)

try:
    # Load actual energy data
    energy_df = pd.read_csv('data/processed/energy_usage_cleaned.csv')
    
    print(f"\nLoaded energy dataset: {energy_df.shape}")
    print("\nFirst few rows:")
    print(energy_df.head())
    
    # Check for duplicates
    print("\n" + "-" * 60)
    print("\nChecking for duplicates in real data...")
    
    # Check exact duplicates
    exact_duplicates = energy_df.duplicated().sum()
    print(f"Exact duplicate rows: {exact_duplicates}")
    
    # Check duplicates based on timestamp + customer_id
    time_customer_duplicates = energy_df.duplicated(subset=['timestamp', 'customer_id']).sum()
    print(f"Duplicate timestamp + customer_id combinations: {time_customer_duplicates}")
    
    if exact_duplicates > 0:
        print("\nDuplicate rows found:")
        print(energy_df[energy_df.duplicated(keep=False)])
        
        # Remove duplicates
        energy_df_cleaned = energy_df.drop_duplicates()
        print(f"\nAfter deduplication: {energy_df_cleaned.shape}")
        print(f"Rows removed: {len(energy_df) - len(energy_df_cleaned)}")
    else:
        print("\n✓ No duplicates found in the dataset!")
        energy_df_cleaned = energy_df
    
except FileNotFoundError:
    print("\nNote: Energy data file not found. Using sample data demonstration above.")

# =========================
# 7. Best Practices and Summary
# =========================
print("\n" + "=" * 60)
print("7. BEST PRACTICES AND SUMMARY")
print("=" * 60)

print("""
KEY TAKEAWAYS:

1. DETECTION:
   - Use duplicated() to identify duplicate rows
   - Check duplicates on all columns or specific subsets
   - Use keep='first', 'last', or False to control marking logic

2. REMOVAL:
   - Use drop_duplicates() to remove duplicates
   - Choose keep='first' (default), 'last', or False
   - Specify subset parameter for column-specific deduplication

3. VERIFICATION:
   - Always compare shapes before and after
   - Recheck for remaining duplicates
   - Verify data integrity and statistics
   - Document what changed

4. COMMON SCENARIOS:
   - Exact duplicates: All columns match
   - Partial duplicates: Some columns match (use subset parameter)
   - Business logic duplicates: Define uniqueness rules

5. WHY DUPLICATES OCCUR:
   - Data entry errors
   - System glitches or bugs
   - Multiple data sources
   - Improper data merging
   - Logging errors

6. WHEN TO BE CAREFUL:
   - Don't assume all duplicates are errors
   - Consider time-series data carefully
   - Understand business context before removing
   - Document deduplication decisions

7. IMPACT ON ANALYSIS:
   - Duplicates inflate counts and aggregations
   - They skew statistical measures (mean, median, etc.)
   - They lead to incorrect conclusions
   - They waste computational resources

REMEMBER:
✓ Always inspect duplicates before removing
✓ Choose appropriate subset columns based on business logic
✓ Verify results after deduplication
✓ Document your deduplication strategy
✓ Clean data leads to accurate analysis
""")

print("=" * 60)
print("MILESTONE COMPLETE")
print("=" * 60)
