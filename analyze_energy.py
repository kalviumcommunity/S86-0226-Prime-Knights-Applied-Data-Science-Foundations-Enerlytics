"""
First Python Script for Data Analysis
======================================
This script demonstrates basic data analysis using Python.

Purpose: Analyze energy consumption data and calculate simple statistics
Author: Prime Knights Team
Date: February 27, 2026
"""

# Import necessary libraries
import pandas as pd

# Print script start message
print("=" * 60)
print("ENERGY CONSUMPTION ANALYSIS SCRIPT")
print("=" * 60)
print()

# Step 1: Load the data
print("Step 1: Loading energy data...")
data_file = 'data/raw/energy_usage_sample.csv'
df = pd.read_csv(data_file)
print(f"✓ Data loaded successfully from {data_file}")
print()

# Step 2: Display basic information
print("Step 2: Examining the data...")
print(f"Number of records: {len(df)}")
print(f"Number of columns: {len(df.columns)}")
print(f"Column names: {', '.join(df.columns)}")
print()

# Step 3: Display first few rows
print("Step 3: First 5 rows of data:")
print(df.head())
print()

# Step 4: Calculate basic statistics
print("Step 4: Calculating statistics...")
print("-" * 60)

# Energy consumption statistics
avg_consumption = df['consumption_kwh'].mean()
max_consumption = df['consumption_kwh'].max()
min_consumption = df['consumption_kwh'].min()
total_consumption = df['consumption_kwh'].sum()

print(f"Average energy consumption: {avg_consumption:.2f} kWh")
print(f"Maximum energy consumption: {max_consumption:.2f} kWh")
print(f"Minimum energy consumption: {min_consumption:.2f} kWh")
print(f"Total energy consumption: {total_consumption:.2f} kWh")
print()

# Temperature statistics
avg_temp = df['temperature_celsius'].mean()
max_temp = df['temperature_celsius'].max()
min_temp = df['temperature_celsius'].min()

print(f"Average temperature: {avg_temp:.2f}°C")
print(f"Maximum temperature: {max_temp:.2f}°C")
print(f"Minimum temperature: {min_temp:.2f}°C")
print()

# Step 5: Simple analysis - consumption by customer
print("Step 5: Analyzing consumption by customer...")
print("-" * 60)
customer_totals = df.groupby('customer_id')['consumption_kwh'].sum()
print("Total consumption by customer:")
for customer, total in customer_totals.items():
    print(f"  {customer}: {total:.2f} kWh")
print()

# Step 6: Summary message
print("=" * 60)
print("ANALYSIS COMPLETE!")
print("=" * 60)
print(f"Processed {len(df)} records successfully.")
print("All calculations completed without errors.")
print()
