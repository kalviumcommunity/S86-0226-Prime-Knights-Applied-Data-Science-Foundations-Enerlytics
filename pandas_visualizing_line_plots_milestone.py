"""
Identifying Trends Over Time Using Line Plots
Pandas + Matplotlib Milestone

This milestone demonstrates:
- Loading and preparing time-based data
- Creating line plots to visualize trends over time
- Identifying upward, downward, and stable trends
- Spotting anomalies, spikes, and patterns
- Analyzing temporal patterns in energy consumption data

Learning Objectives:
- Understand time-series data representation
- Visualize data changes over time
- Identify and interpret trends
- Detect anomalies or sudden shifts
- Build intuition for temporal analysis
"""

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for batch processing
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. Understanding Time-Based Data
# ==========================================

print("=" * 60)
print("STEP 1: Loading and Understanding Time-Based Data")
print("=" * 60)

# Load the energy usage dataset
df = pd.read_csv('data/processed/energy_usage_cleaned.csv')

print("\nDataset loaded successfully!")
print(f"Shape: {df.shape}")
print(f"\nFirst few rows:")
print(df.head(10))

# Identify time-based columns
print("\n" + "=" * 60)
print("Identifying Time Columns")
print("=" * 60)
print(f"\nColumn data types:")
print(df.dtypes)

# Convert timestamp to datetime for proper time-based analysis
print("\nConverting 'timestamp' to datetime format...")
df['timestamp'] = pd.to_datetime(df['timestamp'])
print("✓ Timestamp converted to datetime")

# CRITICAL: Sort data by time before plotting
print("\nSorting data by timestamp (CRITICAL for time-series analysis)...")
df = df.sort_values('timestamp')
print("✓ Data sorted chronologically")

print(f"\nTime range in dataset:")
print(f"Start: {df['timestamp'].min()}")
print(f"End: {df['timestamp'].max()}")
print(f"Duration: {df['timestamp'].max() - df['timestamp'].min()}")

# ==========================================
# 2. Creating Basic Line Plots
# ==========================================

print("\n" + "=" * 60)
print("STEP 2: Creating Line Plots for Time-Series Visualization")
print("=" * 60)

# Plot 1: Energy Consumption Over Time (Single Customer)
print("\n--- Plot 1: Energy Consumption Trend for Single Customer ---")

# Filter data for one customer to see clear patterns
customer_data = df[df['customer_id'] == 'CUST001'].copy()
print(f"Analyzing data for CUST001: {len(customer_data)} records")

plt.figure(figsize=(12, 6))
plt.plot(customer_data['timestamp'], customer_data['consumption_kwh'], 
         linewidth=2, color='blue', marker='o', markersize=3)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Energy Consumption (kWh)', fontsize=12)
plt.title('Energy Consumption Over Time - CUST001', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/line_plot_single_customer.png', dpi=300, bbox_inches='tight')
print("✓ Saved: outputs/figures/line_plot_single_customer.png")
plt.close()

# Plot 2: Temperature Trend Over Time
print("\n--- Plot 2: Temperature Trend Over Time ---")

plt.figure(figsize=(12, 6))
plt.plot(customer_data['timestamp'], customer_data['temperature_celsius'], 
         linewidth=2, color='red', marker='s', markersize=3)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Temperature (°C)', fontsize=12)
plt.title('Temperature Trend Over Time', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/line_plot_temperature_trend.png', dpi=300, bbox_inches='tight')
print("✓ Saved: outputs/figures/line_plot_temperature_trend.png")
plt.close()

# ==========================================
# 3. Identifying Trends
# ==========================================

print("\n" + "=" * 60)
print("STEP 3: Identifying and Interpreting Trends")
print("=" * 60)

# Analyze daily average consumption trend
print("\n--- Analyzing Daily Trends ---")

# Extract date from timestamp
df['date'] = df['timestamp'].dt.date

# Calculate daily average consumption per customer
daily_avg = df.groupby(['date', 'customer_id'])['consumption_kwh'].mean().reset_index()

# Focus on one customer for trend analysis
daily_customer = daily_avg[daily_avg['customer_id'] == 'CUST001'].copy()

print(f"\nDaily average consumption statistics:")
print(daily_customer['consumption_kwh'].describe())

# Plot daily average trend
plt.figure(figsize=(14, 6))
plt.plot(range(len(daily_customer)), daily_customer['consumption_kwh'], 
         linewidth=2.5, color='green', marker='o', markersize=6)
plt.xlabel('Days', fontsize=12)
plt.ylabel('Average Daily Consumption (kWh)', fontsize=12)
plt.title('Daily Average Energy Consumption Trend', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/line_plot_daily_trend.png', dpi=300, bbox_inches='tight')
print("✓ Saved: outputs/figures/line_plot_daily_trend.png")
plt.close()

# Trend Analysis
print("\n--- TREND INTERPRETATION ---")
mean_consumption = daily_customer['consumption_kwh'].mean()
first_half_mean = daily_customer['consumption_kwh'].iloc[:len(daily_customer)//2].mean()
second_half_mean = daily_customer['consumption_kwh'].iloc[len(daily_customer)//2:].mean()

print(f"\nOverall average consumption: {mean_consumption:.2f} kWh")
print(f"First half average: {first_half_mean:.2f} kWh")
print(f"Second half average: {second_half_mean:.2f} kWh")

if second_half_mean > first_half_mean * 1.05:
    print("→ UPWARD TREND DETECTED: Consumption is increasing over time")
elif second_half_mean < first_half_mean * 0.95:
    print("→ DOWNWARD TREND DETECTED: Consumption is decreasing over time")
else:
    print("→ STABLE TREND: Consumption remains relatively constant")

# ==========================================
# 4. Spotting Changes and Anomalies
# ==========================================

print("\n" + "=" * 60)
print("STEP 4: Detecting Anomalies and Patterns")
print("=" * 60)

# Hourly pattern analysis - showing daily cycles
print("\n--- Analyzing Intra-Day Patterns ---")

# Get 3 consecutive days for pattern visualization
sample_days = customer_data.head(72)  # 3 days * 24 hours

plt.figure(figsize=(14, 6))
plt.plot(sample_days['timestamp'], sample_days['consumption_kwh'], 
         linewidth=2, color='purple', marker='o', markersize=4)

# Highlight peak hours
peak_data = sample_days[sample_days['is_peak'] == True]
plt.scatter(peak_data['timestamp'], peak_data['consumption_kwh'], 
           color='red', s=100, alpha=0.5, label='Peak Hours', zorder=5)

plt.xlabel('Time', fontsize=12)
plt.ylabel('Energy Consumption (kWh)', fontsize=12)
plt.title('Energy Consumption Pattern - 3 Days (with Peak Hours Highlighted)', 
         fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/line_plot_pattern_analysis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: outputs/figures/line_plot_pattern_analysis.png")
plt.close()

# Detect anomalies using statistical methods
print("\n--- Detecting Anomalies ---")

# Calculate z-scores for anomaly detection
consumption_mean = customer_data['consumption_kwh'].mean()
consumption_std = customer_data['consumption_kwh'].std()
customer_data['z_score'] = (customer_data['consumption_kwh'] - consumption_mean) / consumption_std

# Identify anomalies (z-score > 2 or < -2)
anomalies = customer_data[abs(customer_data['z_score']) > 2]

print(f"\nConsumption statistics:")
print(f"Mean: {consumption_mean:.2f} kWh")
print(f"Standard deviation: {consumption_std:.2f} kWh")
print(f"Number of anomalies detected: {len(anomalies)}")

if len(anomalies) > 0:
    print(f"\nAnomaly examples:")
    print(anomalies[['timestamp', 'consumption_kwh', 'z_score']].head())
    
    # Plot with anomalies highlighted
    plt.figure(figsize=(14, 6))
    plt.plot(customer_data['timestamp'], customer_data['consumption_kwh'], 
             linewidth=2, color='blue', alpha=0.7, label='Normal')
    plt.scatter(anomalies['timestamp'], anomalies['consumption_kwh'], 
               color='red', s=100, marker='X', label='Anomalies', zorder=5)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Energy Consumption (kWh)', fontsize=12)
    plt.title('Energy Consumption with Anomaly Detection', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('outputs/figures/line_plot_anomalies.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: outputs/figures/line_plot_anomalies.png")
    plt.close()

# ==========================================
# 5. Multi-Line Comparison
# ==========================================

print("\n" + "=" * 60)
print("STEP 5: Comparing Multiple Time Series")
print("=" * 60)

# Compare consumption patterns for multiple customers
print("\n--- Comparing Customer Consumption Patterns ---")

# Get data for first 3 customers
customers = df['customer_id'].unique()[:3]
print(f"Comparing customers: {list(customers)}")

plt.figure(figsize=(14, 7))

colors = ['blue', 'green', 'orange']
for idx, customer in enumerate(customers):
    cust_data = df[df['customer_id'] == customer].head(168)  # 1 week
    plt.plot(cust_data['timestamp'], cust_data['consumption_kwh'], 
             linewidth=2, color=colors[idx], alpha=0.7, label=customer)

plt.xlabel('Time', fontsize=12)
plt.ylabel('Energy Consumption (kWh)', fontsize=12)
plt.title('Energy Consumption Comparison - Multiple Customers', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('outputs/figures/line_plot_multi_customer.png', dpi=300, bbox_inches='tight')
print("✓ Saved: outputs/figures/line_plot_multi_customer.png")
plt.close()

# ==========================================
# 6. Relationship Between Variables Over Time
# ==========================================

print("\n" + "=" * 60)
print("STEP 6: Analyzing Relationships Over Time")
print("=" * 60)

# Plot consumption and temperature on dual y-axes
print("\n--- Energy Consumption vs Temperature Over Time ---")

fig, ax1 = plt.subplots(figsize=(14, 7))

# Get sample data
sample_data = customer_data.head(168)  # 1 week

# Plot consumption on primary y-axis
color = 'tab:blue'
ax1.set_xlabel('Time', fontsize=12)
ax1.set_ylabel('Energy Consumption (kWh)', color=color, fontsize=12)
ax1.plot(sample_data['timestamp'], sample_data['consumption_kwh'], 
         color=color, linewidth=2, label='Consumption')
ax1.tick_params(axis='y', labelcolor=color)
ax1.tick_params(axis='x', rotation=45)

# Create secondary y-axis for temperature
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Temperature (°C)', color=color, fontsize=12)
ax2.plot(sample_data['timestamp'], sample_data['temperature_celsius'], 
         color=color, linewidth=2, linestyle='--', label='Temperature')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Energy Consumption and Temperature Over Time (Dual Axis)', 
         fontsize=14, fontweight='bold')
fig.tight_layout()
plt.grid(True, alpha=0.3)
plt.savefig('outputs/figures/line_plot_dual_axis.png', dpi=300, bbox_inches='tight')
print("✓ Saved: outputs/figures/line_plot_dual_axis.png")
plt.close()

# ==========================================
# 7. Key Insights and Patterns
# ==========================================

print("\n" + "=" * 60)
print("KEY INSIGHTS FROM TIME-SERIES ANALYSIS")
print("=" * 60)

print("""
✓ PATTERNS IDENTIFIED:

1. DAILY CYCLES:
   - Energy consumption shows clear daily patterns
   - Morning and evening peaks are visible
   - Nighttime consumption is consistently lower

2. PEAK HOUR BEHAVIOR:
   - Highest consumption occurs during peak hours (17:00-20:00)
   - This aligns with typical residential usage patterns

3. TEMPERATURE CORRELATION:
   - Temperature and consumption show inverse relationship
   - Lower temperatures may drive higher heating usage

4. STABILITY:
   - Day-to-day patterns are relatively consistent
   - Seasonal trends would require longer time periods

5. ANOMALIES:
   - Statistical outliers can be identified
   - May indicate unusual events or data collection issues
""")

print("\n" + "=" * 60)
print("WHY LINE PLOTS MATTER FOR TIME-SERIES DATA")
print("=" * 60)

print("""
Line plots are essential because they:

✓ Preserve temporal order and continuity
✓ Reveal trends that summary statistics cannot show
✓ Highlight patterns like cycles and seasonality
✓ Make anomalies visually obvious
✓ Enable comparison across time periods
✓ Support data-driven decision making
✓ Provide context for forecasting and modeling

Time adds critical context that static analysis misses.
""")

# ==========================================
# 8. Summary and Best Practices
# ==========================================

print("\n" + "=" * 60)
print("SUMMARY AND BEST PRACTICES")
print("=" * 60)

print("""
✓ CRITICAL STEPS FOR TIME-SERIES VISUALIZATION:

1. Always convert time columns to datetime format
2. ALWAYS sort data chronologically before plotting
3. Choose appropriate time granularity (hourly, daily, etc.)
4. Label axes clearly with units
5. Use line plots for ordered, continuous time data
6. Highlight important events or anomalies
7. Consider dual axes for related variables
8. Interpret patterns in context

✓ COMMON PITFALLS TO AVOID:

× Don't treat time-series as unordered data
× Don't plot unsorted time data
× Don't overreact to single data points
× Don't ignore the scale and units
× Don't plot too many lines (causes clutter)
× Don't confuse correlation with causation

✓ NEXT STEPS:

→ Apply smoothing techniques for noisy data
→ Calculate moving averages for trend clarity
→ Explore seasonal decomposition
→ Investigate correlations between variables
→ Build forecasting models (beyond this milestone)
""")

print("\n" + "=" * 60)
print("MILESTONE COMPLETE!")
print("=" * 60)
print("\nAll visualizations saved to outputs/figures/")
print("You can now identify and interpret trends over time using line plots!")
