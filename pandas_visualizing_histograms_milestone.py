"""
Visualizing Data Distributions Using Histograms
Pandas + Matplotlib Milestone

This milestone demonstrates:
- Creating histograms for numeric columns
- Interpreting distribution shape and spread
- Identifying skewed or uneven distributions
- Detecting potential outliers visually
- Comparing distributions across multiple columns
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. Load the Dataset
# ==========================================

print("=" * 60)
print("Loading Energy Usage Dataset")
print("=" * 60)

# Load the cleaned energy usage data
df = pd.read_csv('data/processed/energy_usage_cleaned.csv')

print("\nDataset loaded successfully!")
print(f"Shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head())
print(f"\nColumn data types:")
print(df.dtypes)

# ==========================================
# 2. Identify Numeric Columns
# ==========================================

print("\n" + "=" * 60)
print("Identifying Numeric Columns for Visualization")
print("=" * 60)

# Select only numeric columns
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
print(f"\nNumeric columns available: {numeric_columns}")

# ==========================================
# 3. Creating a Histogram for a Single Column
# ==========================================

print("\n" + "=" * 60)
print("Creating Histogram for Single Column: consumption_kwh")
print("=" * 60)

# Create a histogram for energy consumption
plt.figure(figsize=(10, 6))
plt.hist(df['consumption_kwh'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Energy Consumption (kWh)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Energy Consumption', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/histogram_consumption.png', dpi=100)
print("\n✓ Histogram saved: outputs/figures/histogram_consumption.png")
plt.close()

# Display summary statistics alongside
print("\nSummary Statistics for Energy Consumption:")
print(df['consumption_kwh'].describe())

# ==========================================
# 4. Interpreting Distribution Shape
# ==========================================

print("\n" + "=" * 60)
print("Interpreting Distribution Shape")
print("=" * 60)

# Calculate skewness metrics
mean_consumption = df['consumption_kwh'].mean()
median_consumption = df['consumption_kwh'].median()
std_consumption = df['consumption_kwh'].std()

print(f"\nEnergy Consumption Analysis:")
print(f"  Mean:   {mean_consumption:.2f} kWh")
print(f"  Median: {median_consumption:.2f} kWh")
print(f"  Std Dev: {std_consumption:.2f} kWh")
print(f"  Range:  {df['consumption_kwh'].min():.2f} - {df['consumption_kwh'].max():.2f} kWh")

# Interpret skewness
if mean_consumption > median_consumption + 0.1:
    skew_interpretation = "RIGHT-SKEWED (positively skewed)"
    explanation = "The distribution has a longer tail on the right side, indicating some high consumption values."
elif mean_consumption < median_consumption - 0.1:
    skew_interpretation = "LEFT-SKEWED (negatively skewed)"
    explanation = "The distribution has a longer tail on the left side."
else:
    skew_interpretation = "ROUGHLY SYMMETRIC"
    explanation = "The mean and median are close, suggesting a balanced distribution."

print(f"\nDistribution Shape: {skew_interpretation}")
print(f"Interpretation: {explanation}")

# ==========================================
# 5. Creating Histogram for Temperature
# ==========================================

print("\n" + "=" * 60)
print("Creating Histogram for Temperature")
print("=" * 60)

plt.figure(figsize=(10, 6))
plt.hist(df['temperature_celsius'], bins=15, color='coral', edgecolor='black', alpha=0.7)
plt.xlabel('Temperature (°C)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Distribution of Temperature', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/histogram_temperature.png', dpi=100)
print("\n✓ Histogram saved: outputs/figures/histogram_temperature.png")
plt.close()

print("\nSummary Statistics for Temperature:")
print(df['temperature_celsius'].describe())

# ==========================================
# 6. Comparing Histograms Across Multiple Columns
# ==========================================

print("\n" + "=" * 60)
print("Comparing Distributions Across Multiple Columns")
print("=" * 60)

# Create subplots for side-by-side comparison
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Energy Usage Data: Distribution Comparison', fontsize=16, fontweight='bold')

# Histogram 1: Consumption
axes[0, 0].hist(df['consumption_kwh'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
axes[0, 0].set_xlabel('Energy Consumption (kWh)')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Energy Consumption Distribution')
axes[0, 0].grid(axis='y', alpha=0.3)

# Histogram 2: Temperature
axes[0, 1].hist(df['temperature_celsius'], bins=15, color='coral', edgecolor='black', alpha=0.7)
axes[0, 1].set_xlabel('Temperature (°C)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Temperature Distribution')
axes[0, 1].grid(axis='y', alpha=0.3)

# Histogram 3: Hour of Day
axes[1, 0].hist(df['hour'], bins=24, color='lightgreen', edgecolor='black', alpha=0.7)
axes[1, 0].set_xlabel('Hour of Day')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Hour Distribution')
axes[1, 0].grid(axis='y', alpha=0.3)

# Histogram 4: Customer ID (if numeric) or a transformed column
# Let's create a histogram showing consumption by peak hours
peak_consumption = df[df['is_peak'] == True]['consumption_kwh']
non_peak_consumption = df[df['is_peak'] == False]['consumption_kwh']

axes[1, 1].hist([peak_consumption, non_peak_consumption], 
                bins=15, 
                color=['red', 'blue'], 
                label=['Peak Hours', 'Non-Peak Hours'],
                edgecolor='black', 
                alpha=0.6)
axes[1, 1].set_xlabel('Energy Consumption (kWh)')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_title('Consumption: Peak vs Non-Peak Hours')
axes[1, 1].legend()
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('outputs/figures/histogram_comparison_multi.png', dpi=100)
print("\n✓ Multi-histogram comparison saved: outputs/figures/histogram_comparison_multi.png")
plt.close()

# ==========================================
# 7. Visual Comparison Analysis
# ==========================================

print("\n" + "=" * 60)
print("Visual Comparison Analysis")
print("=" * 60)

print("\nComparative Summary Statistics:")
comparison_stats = df[['consumption_kwh', 'temperature_celsius', 'hour']].describe()
print(comparison_stats)

print("\n--- Key Observations ---")
print("\n1. Energy Consumption (consumption_kwh):")
print(f"   - Mean: {df['consumption_kwh'].mean():.2f} kWh")
print(f"   - Spread: Wide range indicates high variability in usage patterns")
print(f"   - Shape: Check histogram for skewness and outliers")

print("\n2. Temperature (temperature_celsius):")
print(f"   - Mean: {df['temperature_celsius'].mean():.2f}°C")
print(f"   - Spread: {df['temperature_celsius'].std():.2f}°C standard deviation")
print(f"   - Pattern: May show seasonal variations")

print("\n3. Hour of Day (hour):")
print(f"   - Range: 0-23 (full 24-hour cycle)")
print(f"   - Distribution: Check if data is evenly distributed across hours")

print("\n4. Peak vs Non-Peak Consumption:")
peak_mean = df[df['is_peak'] == True]['consumption_kwh'].mean()
non_peak_mean = df[df['is_peak'] == False]['consumption_kwh'].mean()
print(f"   - Peak hours average: {peak_mean:.2f} kWh")
print(f"   - Non-peak hours average: {non_peak_mean:.2f} kWh")
print(f"   - Difference: {abs(peak_mean - non_peak_mean):.2f} kWh")

# ==========================================
# 8. Detecting Potential Outliers Visually
# ==========================================

print("\n" + "=" * 60)
print("Detecting Potential Outliers")
print("=" * 60)

# Calculate IQR for outlier detection
Q1 = df['consumption_kwh'].quantile(0.25)
Q3 = df['consumption_kwh'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['consumption_kwh'] < lower_bound) | (df['consumption_kwh'] > upper_bound)]

print(f"\nOutlier Detection for Energy Consumption:")
print(f"  Q1 (25th percentile): {Q1:.2f} kWh")
print(f"  Q3 (75th percentile): {Q3:.2f} kWh")
print(f"  IQR: {IQR:.2f} kWh")
print(f"  Lower Bound: {lower_bound:.2f} kWh")
print(f"  Upper Bound: {upper_bound:.2f} kWh")
print(f"  Number of potential outliers: {len(outliers)}")

if len(outliers) > 0:
    print(f"\n  Outlier values:")
    print(outliers[['timestamp', 'consumption_kwh', 'temperature_celsius']].head(10))

# Create histogram with outlier boundaries marked
plt.figure(figsize=(12, 6))
plt.hist(df['consumption_kwh'], bins=25, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(lower_bound, color='red', linestyle='--', linewidth=2, label=f'Lower Bound ({lower_bound:.2f})')
plt.axvline(upper_bound, color='red', linestyle='--', linewidth=2, label=f'Upper Bound ({upper_bound:.2f})')
plt.axvline(df['consumption_kwh'].mean(), color='green', linestyle='-', linewidth=2, label=f'Mean ({df["consumption_kwh"].mean():.2f})')
plt.axvline(df['consumption_kwh'].median(), color='orange', linestyle='-', linewidth=2, label=f'Median ({df["consumption_kwh"].median():.2f})')
plt.xlabel('Energy Consumption (kWh)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Energy Consumption Distribution with Outlier Boundaries', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/histogram_outliers.png', dpi=100)
print("\n✓ Outlier analysis histogram saved: outputs/figures/histogram_outliers.png")
plt.close()

# ==========================================
# 9. Summary and Insights
# ==========================================

print("\n" + "=" * 60)
print("SUMMARY AND KEY INSIGHTS")
print("=" * 60)

print("\n✓ Milestone Completed Successfully!")
print("\nWhat We Learned:")
print("  1. Created histograms for multiple numeric columns")
print("  2. Interpreted distribution shapes (skewness, spread, range)")
print("  3. Compared distributions visually across columns")
print("  4. Detected potential outliers using visual and statistical methods")
print("  5. Used histograms to guide exploratory data analysis (EDA)")

print("\nKey Takeaways:")
print("  • Histograms reveal patterns that summary statistics alone cannot show")
print("  • Distribution shape indicates data behavior (normal, skewed, multi-modal)")
print("  • Visual comparison helps identify columns with different characteristics")
print("  • Outliers are visible as isolated bars far from the main distribution")
print("  • Histograms are essential for understanding data before modeling")

print("\n" + "=" * 60)
print("All histograms saved in: outputs/figures/")
print("=" * 60)
