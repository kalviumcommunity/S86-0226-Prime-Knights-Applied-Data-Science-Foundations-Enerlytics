"""
Visualizing Data Distributions Using Boxplots
Applied Data Science Foundations – Enerlytics
Pandas + Matplotlib Milestone

This milestone demonstrates:
- Creating boxplots for numeric columns
- Identifying median, quartiles, and IQR
- Detecting potential outliers visually
- Comparing distributions across multiple columns
- Interpreting spread and variability
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# ==========================================
# 1. Load or Generate the Dataset
# ==========================================

print("=" * 60)
print("Loading/Creating Energy Usage Dataset")
print("=" * 60)

# Try to load the cleaned energy usage data, otherwise create synthetic data
DATA_PATH = 'data/processed/energy_usage_cleaned.csv'

if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    print(f"\n✓ Dataset loaded from: {DATA_PATH}")
else:
    print(f"\n⚠ File {DATA_PATH} not found. Generating synthetic data...")
    # Create synthetic data with outliers for demonstration
    np.random.seed(42)
    rows = 100
    df = pd.DataFrame({
        'timestamp': pd.date_range(start='2026-01-01', periods=rows, freq='h'),
        'consumption_kwh': np.random.normal(15, 5, rows),
        'temperature_celsius': np.random.normal(25, 3, rows),
        'cost_in_inr': np.random.normal(150, 40, rows)
    })
    
    # Introduce some outliers
    df.loc[10, 'consumption_kwh'] = 55.0  # High outlier
    df.loc[25, 'consumption_kwh'] = 2.0   # Low outlier
    df.loc[50, 'temperature_celsius'] = 45.0 # High outlier
    
    # Ensure no negative values for consumption
    df['consumption_kwh'] = df['consumption_kwh'].clip(lower=0.5)

print(f"Shape: {df.shape}")
print(f"\nSummary Statistics:")
print(df.describe())

# ==========================================
# 2. Creating a Boxplot for a Single Column
# ==========================================

print("\n" + "=" * 60)
print("Creating Boxplot for Single Column: consumption_kwh")
print("=" * 60)

plt.figure(figsize=(10, 6))
# Create the boxplot
plt.boxplot(df['consumption_kwh'], patch_artist=True, 
            boxprops=dict(facecolor='skyblue', color='blue'),
            medianprops=dict(color='red', linewidth=2),
            flierprops=dict(marker='o', markerfacecolor='red', markersize=8))

plt.ylabel('Energy Consumption (kWh)', fontsize=12)
plt.title('Boxplot of Energy Consumption', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

# Define output directory
OUTPUT_DIR = 'outputs/figures'
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.savefig(f'{OUTPUT_DIR}/boxplot_consumption.png', dpi=100)
print(f"\n✓ Boxplot saved: {OUTPUT_DIR}/boxplot_consumption.png")
plt.close()

# Calculate key metrics for interpretation
Q1 = df['consumption_kwh'].quantile(0.25)
median = df['consumption_kwh'].median()
Q3 = df['consumption_kwh'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"\nInterpretation Table (consumption_kwh):")
print(f"  - Median (Line in box): {median:.2f} kWh")
print(f"  - Q1 (Bottom of box):  {Q1:.2f} kWh")
print(f"  - Q3 (Top of box):     {Q3:.2f} kWh")
print(f"  - IQR (Height of box): {IQR:.2f} kWh")
print(f"  - Lower Whisker Bound: {lower_bound:.2f} kWh")
print(f"  - Upper Whisker Bound: {upper_bound:.2f} kWh")

# ==========================================
# 3. Comparing Boxplots Across Columns
# ==========================================

print("\n" + "=" * 60)
print("Comparing Boxplots Across Numeric Columns")
print("=" * 60)

# Select numeric columns
cols_to_compare = ['consumption_kwh', 'temperature_celsius']

plt.figure(figsize=(12, 7))
# Create side-by-side boxplots
df[cols_to_compare].boxplot(patch_artist=True, 
                             boxprops=dict(facecolor='lightgreen', color='green'),
                             medianprops=dict(color='orange', linewidth=2))

plt.title('Comparison of Energy Consumption vs Temperature', fontsize=14, fontweight='bold')
plt.ylabel('Value', fontsize=12)
plt.grid(axis='y', alpha=0.3)

plt.savefig(f'{OUTPUT_DIR}/boxplot_comparison.png', dpi=100)
print(f"✓ Boxplot comparison saved: {OUTPUT_DIR}/boxplot_comparison.png")
plt.close()

# ==========================================
# 4. Detecting and Identifying Outliers
# ==========================================

print("\n" + "=" * 60)
print("Detecting Potential Outliers Visually")
print("=" * 60)

# Find rows where consumption is an outlier
outliers = df[(df['consumption_kwh'] < lower_bound) | (df['consumption_kwh'] > upper_bound)]

print(f"\nNumber of detected outliers in energy consumption: {len(outliers)}")
if not outliers.empty:
    print("\nOutlier Values:")
    print(outliers[['timestamp', 'consumption_kwh']])
else:
    print("\nNo outliers detected using the 1.5*IQR rule.")

# ==========================================
# 5. Key Takeaways
# ==========================================

print("\n" + "=" * 60)
print("MILESTONE SUMMARY & KEY TAKEAWAYS")
print("=" * 60)

print("""
1. Boxplots summarize 5 key stats: Min, Q1, Median, Q3, Max.
2. The 'Box' represents the Interquartile Range (IQR), containing the middle 50% of data.
3. The 'Median' is the central line inside the box.
4. 'Whiskers' typically extend to 1.5 * IQR from the hinges.
5. 'Outliers' are points plotted individually beyond the whiskers.
6. Boxplots are superior for comparing spreads across different categories or columns.
7. Outliers are not always errors; they often indicate unusual but valid high-impact events.
""")

print("✓ Boxplot Milestone Completed Successfully!")
print("=" * 60)
