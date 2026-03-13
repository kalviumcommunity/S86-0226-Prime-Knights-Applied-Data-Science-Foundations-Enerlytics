# Scatter Plot Milestone - Video Walkthrough Script (~2 Minutes)

## Recording Goal
Show how scatter plots help explore relationships between numeric variables before deeper analysis.

## Setup Before Recording
- Open pandas_visualizing_scatter_plots_milestone.py
- Keep outputs/figures/ open
- Confirm these images exist:
  - scatter_temperature_vs_consumption.png
  - scatter_hour_vs_consumption.png
  - scatter_peak_vs_nonpeak_clusters.png
  - scatter_outliers_highlighted.png

---

## Script Timeline

### 0:00 - 0:15 | Introduction
Say:
"In this milestone, I am exploring relationships between variables using scatter plots. Scatter plots are useful in exploratory data analysis because each point represents one observation and helps us identify trends, clusters, and outliers."

### 0:15 - 0:40 | Plot 1: Temperature vs Consumption
Show: scatter_temperature_vs_consumption.png

Say:
"This scatter plot compares temperature on the x-axis and energy consumption on the y-axis. The points show a generally negative pattern in this dataset, meaning consumption tends to increase when temperature is lower."

### 0:40 - 1:00 | Plot 2: Hour vs Consumption
Show: scatter_hour_vs_consumption.png

Say:
"This plot shows hour of day versus consumption. Points are higher during evening hours, which indicates a time-based pattern in usage. Scatter plots make these patterns visible quickly without building a model."

### 1:00 - 1:25 | Plot 3: Clusters (Peak vs Non-Peak)
Show: scatter_peak_vs_nonpeak_clusters.png

Say:
"Here I use two colors for peak and non-peak points. We can see cluster separation, where peak points are concentrated at higher consumption levels. This helps compare groups in one visual."

### 1:25 - 1:50 | Plot 4: Outliers
Show: scatter_outliers_highlighted.png

Say:
"This chart highlights potential outliers using an IQR rule. Red X markers represent unusual points that are far from most observations. Outliers are important because they may indicate rare events, data quality issues, or critical behavior changes."

### 1:50 - 2:00 | Conclusion
Say:
"Scatter plots are a core EDA tool. They help identify relationship direction, cluster structure, and outliers, which supports better decisions before statistical testing or predictive modeling."

---

## Quick Checklist
- Explain axes and point meaning
- Describe positive, negative, or weak relationship
- Mention clusters and outliers
- Explain why scatter plots are useful
- Keep duration around 2 minutes
