"""
Comparing Distributions Across Multiple Columns in Pandas
Pandas Milestone
"""

import pandas as pd

# ==========================================
# 1. Load a Multi-Column Dataset
# ==========================================

# Dataset representing energy consumption across different appliance types 
# in different households (kilo-Watt hours)
energy_data = {
    "Household_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "HVAC_Usage": [450, 480, 520, 600, 410, 850, 490, 510],   # High mean, high variability
    "Lighting_Usage": [120, 115, 125, 130, 118, 122, 119, 121], # Low mean, very low variability (stable)
    "Appliance_Usage": [300, 310, 290, 450, 305, 315, 295, 300] # Moderate mean, one outlier (450)
}

df = pd.DataFrame(energy_data)

print("--- Multi-Column Energy Usage Dataset ---")
print(df.drop(columns="Household_ID")) # Dropping ID for cleaner view
print("\n")

# ==========================================
# 2. Computing Summary Statistics Simultaneously
# ==========================================

print("--- Comparative Summary Statistics ---")
# Using .describe() on the whole DataFrame or a selection of numeric columns
stats_comparison = df[["HVAC_Usage", "Lighting_Usage", "Appliance_Usage"]].describe()
print(stats_comparison)
print("\n")

# ==========================================
# 3. Comparing Central Tendency
# ==========================================

print("--- Analysis: Central Tendency (Mean vs Median) ---")
means = df[["HVAC_Usage", "Lighting_Usage", "Appliance_Usage"]].mean()
medians = df[["HVAC_Usage", "Lighting_Usage", "Appliance_Usage"]].median()

comparison_df = pd.DataFrame({"Mean": means, "Median": medians})
comparison_df["Difference"] = comparison_df["Mean"] - comparison_df["Median"]

print(comparison_df)
print("\n")

# Interpretation: 
# Appliance_Usage has a Mean (321) higher than Median (302), suggesting a right-skew 
# likely caused by the outlier of 450.

# ==========================================
# 4. Comparing Spread and Variability
# ==========================================

print("--- Analysis: Spread and Variability ---")
# Calculating Coefficient of Variation (CV) = Std / Mean
# This allows us to compare variability across columns with different scales
cv = df[["HVAC_Usage", "Lighting_Usage", "Appliance_Usage"]].std() / df[["HVAC_Usage", "Lighting_Usage", "Appliance_Usage"]].mean()

print("Coefficient of Variation (Relative Spread):")
print(cv)
print("\n")

# Interpretation:
# Lighting_Usage has the lowest CV, indicating it is the most stable/consistent category.
# HVAC_Usage has a higher CV, showing higher variability in consumption across households.

# ==========================================
# 5. Identifying Distribution Patterns
# ==========================================

print("--- Key Insights from Distribution Comparison ---")

# Compare Ranges
hvac_range = df["HVAC_Usage"].max() - df["HVAC_Usage"].min()
light_range = df["Lighting_Usage"].max() - df["Lighting_Usage"].min()

print(f"HVAC Usage Range: {hvac_range} kWh")
print(f"Lighting Usage Range: {light_range} kWh")

if hvac_range > light_range * 5:
    print("Pattern: HVAC consumption is much more volatile and dependent on household factors than lighting.")

# Final Note: 
# Distribution comparison reveals that while Lighting is predictable, HVAC usage 
# contains significant peaks that might require further investigation (like house size or insulation).
