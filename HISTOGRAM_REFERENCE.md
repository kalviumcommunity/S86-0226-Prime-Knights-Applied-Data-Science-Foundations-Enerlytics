# Histogram Visualization - Quick Reference Guide

## 📊 What is a Histogram?

A histogram is a graphical representation of the distribution of numerical data. It groups data into bins (ranges) and shows the frequency of values in each bin.

**Key Difference**: Histograms are for CONTINUOUS numeric data, bar charts are for CATEGORICAL data.

---

## 🎯 Key Concepts You've Mastered

### 1. **Bins and Frequencies**
- **Bins**: Ranges that group continuous data (e.g., 0-1, 1-2, 2-3 kWh)
- **Frequency**: Count of data points that fall within each bin
- **Height of bar**: Represents frequency

### 2. **Distribution Shape**

#### **Symmetric (Normal)**
```
     *
   * * *
 * * * * *
-----------
```
- Mean ≈ Median
- Data evenly distributed around center
- Bell-shaped curve

#### **Right-Skewed (Positively Skewed)**
```
 *
 * *
 * * *
 * * * *
 * * * * * *
-------------
```
- Mean > Median
- Long tail on the right
- Most values on the left, few high values
- **Example**: Energy consumption (most households use moderate energy, few use very high)

#### **Left-Skewed (Negatively Skewed)**
```
         *
       * *
     * * *
   * * * *
 * * * * * *
-------------
```
- Mean < Median
- Long tail on the left
- Most values on the right, few low values

### 3. **Interpreting Spread**
- **Wide spread**: High variability (std dev is large)
- **Narrow spread**: Low variability (std dev is small)
- **Range**: Max - Min (total spread)

### 4. **Detecting Outliers Visually**
- **Outliers**: Isolated bars far from the main cluster
- **IQR Method**: Values beyond Q1 - 1.5×IQR or Q3 + 1.5×IQR
- **Visual cue**: Gaps between main distribution and extreme values

---

## 💻 Python Code Templates

### Basic Histogram
```python
import matplotlib.pyplot as plt
import pandas as pd

# Create histogram
plt.hist(df['column_name'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Column Name')
plt.ylabel('Frequency')
plt.title('Distribution of Column Name')
plt.show()
```

### Histogram with Statistics
```python
# Calculate statistics
mean = df['column_name'].mean()
median = df['column_name'].median()
std = df['column_name'].std()

# Create histogram with markers
plt.hist(df['column_name'], bins=20, alpha=0.7)
plt.axvline(mean, color='red', linestyle='--', label=f'Mean: {mean:.2f}')
plt.axvline(median, color='green', linestyle='-', label=f'Median: {median:.2f}')
plt.legend()
plt.show()
```

### Multiple Histograms (Subplots)
```python
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].hist(df['column1'], bins=20, color='skyblue')
axes[0, 0].set_title('Column 1 Distribution')

axes[0, 1].hist(df['column2'], bins=20, color='coral')
axes[0, 1].set_title('Column 2 Distribution')

plt.tight_layout()
plt.show()
```

### Overlapping Histograms (Comparison)
```python
plt.hist([df['group1'], df['group2']], 
         bins=15, 
         label=['Group 1', 'Group 2'],
         alpha=0.6)
plt.legend()
plt.show()
```

---

## ✅ Your Analysis Results

### Energy Consumption Distribution
- **Mean**: 3.72 kWh
- **Median**: 3.50 kWh
- **Shape**: Right-skewed (mean > median)
- **Range**: 1.30 - 7.80 kWh
- **Outliers**: 2 values above 7.0 kWh
- **Interpretation**: Most households use 2-5 kWh, but some peak at 7-8 kWh during evening hours

### Temperature Distribution
- **Mean**: 18.75°C
- **Median**: 18.00°C
- **Shape**: Roughly symmetric
- **Range**: 15 - 23°C
- **Interpretation**: Temperature is relatively stable with moderate variation

### Peak vs Non-Peak Consumption
- **Peak hours average**: 6.01 kWh
- **Non-peak hours average**: 3.04 kWh
- **Difference**: 2.97 kWh (98% higher during peak)
- **Interpretation**: Significant increase in energy usage during peak hours

---

## 🔍 When to Use Histograms

### ✅ Use Histograms When:
- Exploring numeric data distribution
- Checking for normality before statistical tests
- Identifying skewness and outliers
- Comparing spread across multiple variables
- Understanding data before modeling

### ❌ Don't Use Histograms When:
- Data is categorical (use bar chart instead)
- You have very few data points (< 20)
- Exact values matter more than distribution
- You need precise frequency counts (use frequency table)

---

## 📈 EDA Workflow with Histograms

1. **Load data** → View shape and structure
2. **Select numeric columns** → Identify variables to visualize
3. **Create histograms** → One per numeric column
4. **Interpret shape** → Symmetric, skewed, or multi-modal?
5. **Check for outliers** → Isolated bars or extreme values?
6. **Compare distributions** → Similar or different patterns?
7. **Calculate statistics** → Mean, median, std dev, IQR
8. **Make decisions** → Transform data? Remove outliers? Proceed to modeling?

---

## 🎓 Common Mistakes to Avoid

| ❌ Mistake | ✅ Correct Approach |
|-----------|-------------------|
| Using too few bins | Use 10-30 bins depending on data size |
| Confusing histogram with bar chart | Histograms = continuous, Bar charts = categorical |
| Ignoring axis labels | Always label axes clearly |
| Not checking for outliers | Always inspect tails of distribution |
| Relying only on mean | Compare mean AND median for skewness |
| Forgetting context | Interpret numbers in domain context |

---

## 🎯 Milestone Checklist

- [x] Load energy usage dataset
- [x] Create histogram for energy consumption
- [x] Create histogram for temperature
- [x] Interpret distribution shapes (skewness)
- [x] Compare multiple distributions (4 histograms)
- [x] Detect outliers visually and statistically
- [x] Calculate summary statistics
- [x] Generate all visualization files
- [ ] Record 2-minute video walkthrough
- [ ] Submit assignment

---

## 📁 Generated Files

All files are saved in: `outputs/figures/`

1. `histogram_consumption.png` - Basic energy consumption histogram
2. `histogram_temperature.png` - Temperature distribution
3. `histogram_comparison_multi.png` - 2x2 grid comparing 4 distributions
4. `histogram_outliers.png` - Consumption with outlier boundaries marked

---

## 💡 Key Takeaways

1. **Histograms reveal patterns** that summary statistics alone cannot show
2. **Shape matters**: Skewness indicates asymmetry in data
3. **Mean vs Median**: When different, distribution is skewed
4. **Outliers** are visible as isolated bars far from main cluster
5. **Comparison** helps identify variables with different behaviors
6. **Context is crucial**: Always interpret in domain terms (energy usage patterns)

---

## 📚 Additional Resources

- [Pandas Histogram Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html)
- [Matplotlib Histogram Guide](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)
- Understanding distribution shapes for data analysis
- IQR method for outlier detection

---

**Next Steps**: Complete the video recording using `VIDEO_SCRIPT.md` as your guide!
