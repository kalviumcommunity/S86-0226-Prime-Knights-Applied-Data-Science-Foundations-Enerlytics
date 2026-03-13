"""
Exploring Relationships Between Variables Using Scatter Plots
Pandas + Matplotlib Milestone

This milestone demonstrates:
- Creating scatter plots for numeric variable pairs
- Interpreting positive, negative, and weak relationships
- Identifying clusters in grouped data
- Detecting potential outliers visually and with simple rules
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def describe_direction(x_series: pd.Series, y_series: pd.Series) -> str:
    """Estimate relationship direction without using correlation coefficients."""
    median_x = x_series.median()
    low_x_mean = y_series[x_series <= median_x].mean()
    high_x_mean = y_series[x_series > median_x].mean()

    if high_x_mean > low_x_mean + 0.2:
        return "positive"
    if high_x_mean < low_x_mean - 0.2:
        return "negative"
    return "weak or no clear"


print("=" * 60)
print("SCATTER PLOT MILESTONE: Exploring Relationships")
print("=" * 60)

# ==========================================
# 1. Load dataset and inspect numeric columns
# ==========================================

print("\nSTEP 1: Load dataset")
df = pd.read_csv('data/processed/energy_usage_cleaned.csv')

print("Dataset loaded successfully")
print(f"Shape: {df.shape}")
print("\nColumns:")
print(df.columns.tolist())

numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
print("\nNumeric columns available for scatter plots:")
print(numeric_columns)

# ==========================================
# 2. Scatter plot: consumption vs temperature
# ==========================================

print("\n" + "=" * 60)
print("STEP 2: Scatter plot - temperature_celsius vs consumption_kwh")
print("=" * 60)

plt.figure(figsize=(10, 6))
plt.scatter(
    df['temperature_celsius'],
    df['consumption_kwh'],
    alpha=0.65,
    s=45,
    color='steelblue',
    edgecolors='white',
    linewidth=0.5,
)
plt.xlabel('Temperature (C)', fontsize=12)
plt.ylabel('Energy Consumption (kWh)', fontsize=12)
plt.title('Scatter Plot: Temperature vs Energy Consumption', fontsize=14, fontweight='bold')
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('outputs/figures/scatter_temperature_vs_consumption.png', dpi=200)
plt.close()
print("Saved: outputs/figures/scatter_temperature_vs_consumption.png")

direction_1 = describe_direction(df['temperature_celsius'], df['consumption_kwh'])
print(f"Relationship direction: {direction_1}")

# ==========================================
# 3. Scatter plot: hour vs consumption
# ==========================================

print("\n" + "=" * 60)
print("STEP 3: Scatter plot - hour vs consumption_kwh")
print("=" * 60)

plt.figure(figsize=(10, 6))
plt.scatter(
    df['hour'],
    df['consumption_kwh'],
    alpha=0.65,
    s=45,
    color='darkorange',
    edgecolors='white',
    linewidth=0.5,
)
plt.xlabel('Hour of Day', fontsize=12)
plt.ylabel('Energy Consumption (kWh)', fontsize=12)
plt.title('Scatter Plot: Hour of Day vs Energy Consumption', fontsize=14, fontweight='bold')
plt.xticks(range(0, 24, 2))
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('outputs/figures/scatter_hour_vs_consumption.png', dpi=200)
plt.close()
print("Saved: outputs/figures/scatter_hour_vs_consumption.png")

# Interpret trend by comparing daytime vs nighttime
night_mean = df[df['hour'].between(0, 6)]['consumption_kwh'].mean()
evening_mean = df[df['hour'].between(17, 21)]['consumption_kwh'].mean()
print(f"Night average consumption (00:00-06:00): {night_mean:.2f} kWh")
print(f"Evening average consumption (17:00-21:00): {evening_mean:.2f} kWh")

if evening_mean > night_mean + 0.5:
    print("Interpretation: consumption tends to be higher in evening hours")
else:
    print("Interpretation: no strong hour-based difference found")

# ==========================================
# 4. Cluster view using peak vs non-peak groups
# ==========================================

print("\n" + "=" * 60)
print("STEP 4: Identify clusters - peak vs non-peak")
print("=" * 60)

peak_df = df[df['is_peak'] == True]
non_peak_df = df[df['is_peak'] == False]

plt.figure(figsize=(10, 6))
plt.scatter(
    non_peak_df['temperature_celsius'],
    non_peak_df['consumption_kwh'],
    alpha=0.55,
    s=40,
    color='teal',
    label='Non-Peak',
)
plt.scatter(
    peak_df['temperature_celsius'],
    peak_df['consumption_kwh'],
    alpha=0.75,
    s=55,
    color='crimson',
    label='Peak',
)
plt.xlabel('Temperature (C)', fontsize=12)
plt.ylabel('Energy Consumption (kWh)', fontsize=12)
plt.title('Scatter Plot with Clusters: Peak vs Non-Peak', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('outputs/figures/scatter_peak_vs_nonpeak_clusters.png', dpi=200)
plt.close()
print("Saved: outputs/figures/scatter_peak_vs_nonpeak_clusters.png")

print(f"Peak points: {len(peak_df)}")
print(f"Non-peak points: {len(non_peak_df)}")
print(f"Peak average consumption: {peak_df['consumption_kwh'].mean():.2f} kWh")
print(f"Non-peak average consumption: {non_peak_df['consumption_kwh'].mean():.2f} kWh")

# ==========================================
# 5. Outlier detection and visual highlight
# ==========================================

print("\n" + "=" * 60)
print("STEP 5: Detect outliers in consumption and highlight them")
print("=" * 60)

q1 = df['consumption_kwh'].quantile(0.25)
q3 = df['consumption_kwh'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = df[(df['consumption_kwh'] < lower_bound) | (df['consumption_kwh'] > upper_bound)]
normal_points = df[(df['consumption_kwh'] >= lower_bound) & (df['consumption_kwh'] <= upper_bound)]

plt.figure(figsize=(10, 6))
plt.scatter(
    normal_points['temperature_celsius'],
    normal_points['consumption_kwh'],
    alpha=0.55,
    s=40,
    color='slateblue',
    label='Typical points',
)
plt.scatter(
    outliers['temperature_celsius'],
    outliers['consumption_kwh'],
    alpha=1.0,
    s=95,
    color='red',
    marker='X',
    label='Potential outliers',
)
plt.xlabel('Temperature (C)', fontsize=12)
plt.ylabel('Energy Consumption (kWh)', fontsize=12)
plt.title('Scatter Plot: Outlier Highlighting', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig('outputs/figures/scatter_outliers_highlighted.png', dpi=200)
plt.close()
print("Saved: outputs/figures/scatter_outliers_highlighted.png")

print(f"IQR lower bound: {lower_bound:.2f}")
print(f"IQR upper bound: {upper_bound:.2f}")
print(f"Potential outliers detected: {len(outliers)}")
if len(outliers) > 0:
    print("Sample outlier rows:")
    print(outliers[['timestamp', 'customer_id', 'consumption_kwh', 'temperature_celsius']].head())

print("\n" + "=" * 60)
print("MILESTONE COMPLETE")
print("Generated files:")
print("- outputs/figures/scatter_temperature_vs_consumption.png")
print("- outputs/figures/scatter_hour_vs_consumption.png")
print("- outputs/figures/scatter_peak_vs_nonpeak_clusters.png")
print("- outputs/figures/scatter_outliers_highlighted.png")
print("=" * 60)
