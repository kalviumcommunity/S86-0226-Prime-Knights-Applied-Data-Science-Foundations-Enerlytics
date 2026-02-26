"""
Data Processing Script - Demonstrates Proper Data Organization

This script demonstrates the correct workflow for organizing data in a Data Science project:
    1. Read from RAW data (read-only, never modify)
    2. Process and clean the data
    3. Save PROCESSED data to processed/ folder
    4. Generate OUTPUT artifacts (plots, reports) to outputs/ folder

Author: Bhanu (Prime Knights)
Date: February 26, 2026
Project: S86-0226 Enerlytics
"""

import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Define paths - this ensures we read from the correct locations
RAW_DATA_PATH = 'data/raw/energy_usage_sample.csv'
PROCESSED_DATA_PATH = 'data/processed/energy_usage_cleaned.csv'
OUTPUT_FIGURE_PATH = 'outputs/figures/energy_consumption_analysis.png'
OUTPUT_REPORT_PATH = 'outputs/reports/analysis_summary.txt'

print("="*60)
print("DATA PROCESSING WORKFLOW DEMONSTRATION")
print("="*60)
print()

# ========================================
# STEP 1: READ RAW DATA (READ-ONLY)
# ========================================
print("STEP 1: Reading RAW data (read-only, never modified)")
print(f"Source: {RAW_DATA_PATH}")
print("-"*60)

# Read the raw data - this does NOT modify the original file
df_raw = pd.read_csv(RAW_DATA_PATH)

print(f"Raw data loaded successfully:")
print(f"  - Shape: {df_raw.shape}")
print(f"  - Columns: {list(df_raw.columns)}")
print(f"  - Date range: {df_raw['timestamp'].min()} to {df_raw['timestamp'].max()}")
print()

# Display first few rows
print("First 3 rows of raw data:")
print(df_raw.head(3))
print()

# ========================================
# STEP 2: PROCESS AND CLEAN DATA
# ========================================
print("="*60)
print("STEP 2: Processing and cleaning data")
print("-"*60)

# Create a copy to process (preserves raw data)
df_processed = df_raw.copy()

# Data cleaning operations
print("Applying transformations:")
print("  ✓ Converting timestamp to datetime")
df_processed['timestamp'] = pd.to_datetime(df_processed['timestamp'])

print("  ✓ Extracting hour from timestamp")
df_processed['hour'] = df_processed['timestamp'].dt.hour

print("  ✓ Removing any duplicate records")
initial_rows = len(df_processed)
df_processed = df_processed.drop_duplicates()
duplicates_removed = initial_rows - len(df_processed)
print(f"    - Removed {duplicates_removed} duplicate(s)")

print("  ✓ Calculating peak consumption indicator")
df_processed['is_peak'] = df_processed['consumption_kwh'] > df_processed['consumption_kwh'].quantile(0.75)

print("  ✓ Adding processing metadata")
df_processed['processed_date'] = datetime.now().strftime('%Y-%m-%d')

print()
print(f"Processed data shape: {df_processed.shape}")
print()

# ========================================
# STEP 3: SAVE PROCESSED DATA
# ========================================
print("="*60)
print("STEP 3: Saving PROCESSED data to separate location")
print(f"Destination: {PROCESSED_DATA_PATH}")
print("-"*60)

# Ensure the directory exists
os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)

# Save processed data (NEVER overwrite raw data!)
df_processed.to_csv(PROCESSED_DATA_PATH, index=False)
print(f"✓ Processed data saved successfully")
print()

# ========================================
# STEP 4: GENERATE OUTPUT ARTIFACTS
# ========================================
print("="*60)
print("STEP 4: Generating OUTPUT artifacts (visualizations & reports)")
print("-"*60)

# Create output directories if they don't exist
os.makedirs(os.path.dirname(OUTPUT_FIGURE_PATH), exist_ok=True)
os.makedirs(os.path.dirname(OUTPUT_REPORT_PATH), exist_ok=True)

# Generate visualization
print(f"Creating visualization: {OUTPUT_FIGURE_PATH}")
plt.figure(figsize=(12, 6))

# Plot average consumption by hour
hourly_avg = df_processed.groupby('hour')['consumption_kwh'].mean()

plt.subplot(1, 2, 1)
plt.plot(hourly_avg.index, hourly_avg.values, marker='o', linewidth=2, color='#2E86AB')
plt.xlabel('Hour of Day', fontsize=11)
plt.ylabel('Average Consumption (kWh)', fontsize=11)
plt.title('Average Energy Consumption by Hour', fontsize=13, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xticks(range(0, 24, 3))

# Plot consumption by customer
plt.subplot(1, 2, 2)
customer_totals = df_processed.groupby('customer_id')['consumption_kwh'].sum()
plt.bar(customer_totals.index, customer_totals.values, color=['#A23B72', '#F18F01'])
plt.xlabel('Customer ID', fontsize=11)
plt.ylabel('Total Consumption (kWh)', fontsize=11)
plt.title('Total Energy Consumption by Customer', fontsize=13, fontweight='bold')
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig(OUTPUT_FIGURE_PATH, dpi=300, bbox_inches='tight')
print(f"✓ Visualization saved successfully")
print()

# Generate text report
print(f"Creating report: {OUTPUT_REPORT_PATH}")
with open(OUTPUT_REPORT_PATH, 'w') as f:
    f.write("="*60 + "\n")
    f.write("ENERGY CONSUMPTION ANALYSIS REPORT\n")
    f.write("="*60 + "\n\n")
    
    f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"Project: S86-0226 Enerlytics\n\n")
    
    f.write("DATA SUMMARY\n")
    f.write("-"*60 + "\n")
    f.write(f"Raw data source: {RAW_DATA_PATH}\n")
    f.write(f"Records processed: {len(df_processed)}\n")
    f.write(f"Unique customers: {df_processed['customer_id'].nunique()}\n\n")
    
    f.write("KEY FINDINGS\n")
    f.write("-"*60 + "\n")
    f.write(f"Average consumption: {df_processed['consumption_kwh'].mean():.2f} kWh\n")
    f.write(f"Peak consumption: {df_processed['consumption_kwh'].max():.2f} kWh\n")
    f.write(f"Minimum consumption: {df_processed['consumption_kwh'].min():.2f} kWh\n")
    
    peak_hour = hourly_avg.idxmax()
    f.write(f"\nPeak usage hour: {peak_hour}:00\n")
    f.write(f"Peak hour avg consumption: {hourly_avg.max():.2f} kWh\n")
    
    f.write("\n" + "="*60 + "\n")
    f.write("END OF REPORT\n")
    f.write("="*60 + "\n")

print(f"✓ Report saved successfully")
print()

# ========================================
# SUMMARY
# ========================================
print("="*60)
print("WORKFLOW COMPLETE!")
print("="*60)
print()
print("DATA ORGANIZATION SUMMARY:")
print(f"  📁 RAW data (untouched):     {RAW_DATA_PATH}")
print(f"  📁 PROCESSED data (cleaned):  {PROCESSED_DATA_PATH}")
print(f"  📊 OUTPUT figure:             {OUTPUT_FIGURE_PATH}")
print(f"  📄 OUTPUT report:             {OUTPUT_REPORT_PATH}")
print()
print("✓ Raw data remains intact and unchanged")
print("✓ Processed data is clearly separated from raw data")
print("✓ Outputs are organized in dedicated folders")
print("✓ Workflow is reproducible and auditable")
print()
print("="*60)
