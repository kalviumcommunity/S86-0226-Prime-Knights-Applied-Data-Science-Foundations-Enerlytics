# applied Data Science Foundations – Enerlytics
## Project: S86-0226 Prime Knights
### Sprint 3 – Data Science

---

# 📊 PROJECT STATUS

| Milestone | Status |
|------------|--------|
| Milestone 1 – Environment Setup | ✅ Complete |
| Milestone 2 – Jupyter Navigation | ✅ Complete |
| Milestone 3 – Kernel Control & Management | ✅ Complete |
| Milestone 4 – Markdown Documentation | ✅ Complete |
| Milestone 5 – Project Organization & Structure | ✅ Complete |
| Milestone 6 – Python Scripts for Data Analysis | ✅ Complete |
| Milestone 7 – Python Data Types (Numeric & String) | ✅ Complete |
| Milestone 8 – Python Collections (Lists, Tuples, Dictionaries) | ✅ Complete |
| Milestone 9 – Pandas DataFrame Shape and Column Data Types | ✅ Complete |
| Milestone 10 – Pandas Indexing and Slicing | ✅ Complete |
| Milestone 11 – Handling Missing Values (Drop and Fill) | ✅ Complete |
| Milestone 12 – Basic Summary Statistics | ✅ Complete |
| Milestone 13 – Comparing Distributions Across Columns | ✅ Complete |
| Milestone 14 – Visualizing Distributions with Boxplots | ✅ Complete |
| Milestone 15 – Detecting Outliers (Visual + IQR Rules) | ✅ Complete |

---

# 🟢 OVERALL STATUS: SPRINT-READY
The development environment is verified, documented, and fully operational for Data Science workflows.

---

# 📋 MILESTONE SUMMARIES

### 1️⃣ Milestone 1 – Environment Setup
**Objective:** Establish a stable Python environment.
- **Concepts:** Python versioning, `pip` package management, Anaconda environment isolation, and library installation (`numpy`, `pandas`, `matplotlib`).

### 2️⃣ Milestone 2 – Jupyter Navigation
**Objective:** Mastering the Jupyter interface.
- **Concepts:** Launching notebooks, navigating the home interface, creating/renaming `.ipynb` files, and using the breadcrumb trail for folder management.

### 3️⃣ Milestone 3 – Kernel Management
**Objective:** Controlling the execution state of a notebook.
- **Concepts:** Understanding the Jupyter Kernel (execution engine), cell execution order, interrupting long-running processes, and restarting the kernel to clear memory/state.

### 4️⃣ Milestone 4 – Markdown Documentation
**Objective:** Creating professional data stories.
- **Concepts:** Heading hierarchies (# to ######), lists (ordered/unordered), inline code vs. code blocks, and the "Explain → Execute → Interpret" flow.

### 5️⃣ Milestone 5 – Project Organization
**Objective:** Implementing professional data architecture.
- **Concepts:**
    - **Raw Data:** Immutable original source (Read-only).
    - **Processed Data:** Cleaned/transformed data ready for analysis.
    - **Outputs:** Figures, reports, and models isolated from data.
    - **One-Directional Flow:** Raw → Processed → Outputs.

### 6️⃣ Milestone 6 – Python Scripts (.py)
**Objective:** Independent code execution.
- **Concepts:** Standalone execution, automation readiness, reproducibility vs. exploration (Notebooks for exploration, Scripts for production), and script structure (Imports → Setup → Main Logic).

### 7️⃣ Milestone 7 – Python Data Types
**Objective:** Understanding fundamental data units.
- **Concepts:**
    - **int:** Whole numbers (Counts/IDs).
    - **float:** Decimal numbers (Measurements/Calculations).
    - **str:** Text data (Labels/IDs).
    - **Type Conversion:** Using `int()`, `float()`, and `str()` to safely cast between types.

### 8️⃣ Milestone 8 – Python Collections
**Objective:** Managing groups of data.
- **Concepts:**
    - **Lists `[]`:** Ordered, mutable sequences.
    - **Tuples `()`:** Ordered, immutable records (Data protection).
    - **Dictionaries `{}`:** Key-value pairs for named attribute access.

### 9️⃣ Milestone 9 – DataFrame Shape & Dtypes
**Objective:** Structural inspection of DataFrames.
- **Concepts:**
    - **Shape:** Tuple representing `(rows, columns)`.
    - **Dtypes:** Column types like `int64`, `float64`, and `object` (string).
    - **Type Detection:** Identifying when numbers are incorrectly stored as strings.

### 🔟 Milestone 10 – Indexing and Slicing
**Objective:** Precise data extraction.
- **Concepts:**
    - **Column Selection:** Using `df['Name']` or `df[['Col1', 'Col2']]`.
    - **Positional Indexing (`iloc`):** Zero-based selection (exclusive stop).
    - **Label Indexing (`loc`):** Selection by name (inclusive stop).

### 1️⃣1️⃣ Milestone 11 – Handling Missing Values
**Objective:** Responsible data cleaning.
- **Concepts:**
    - **Dropping (`dropna`):** Removing incomplete rows/columns safely using `subset` and `thresh`.
    - **Filling (`fillna`):** Imputing missing data using mean, median, or constant placeholders ("Unknown").
    - **Trade-offs:** Balancing data preservation (filling) vs. data quality (dropping).

### 1️⃣2️⃣ Milestone 12 – Basic Summary Statistics
**Objective:** Quantitatively understanding individual data columns.
- **Concepts:**
    - **Central Tendency:** Using `mean()` and `median()` to find the center of the data.
    - **Spread:** Understanding `std()` (standard deviation) and `min`/`max` ranges.
    - **Distribution Intuition:** Comparing mean vs. median to detect skewness and potential outliers.
    - **Quick Overview:** Using `describe()` for a comprehensive statistical snapshot.

### 1️⃣3️⃣ Milestone 13 – Comparing Distributions
**Objective:** Analyzing how different variables behave relative to each other.
- **Concepts:**
    - **Multi-Column Statistics:** Batch computing summaries for numeric variables.
    - **Relative Variability:** Comparing spread using Coefficient of Variation (Std/Mean).
    - **Stability vs. Volatility:** Identifying consistent patterns (e.g., Lighting) vs. high-range variables (e.g., HVAC).
    - **Comparative Interpretation:** Using differences in mean and range to guide root-cause analysis.

### 1️⃣4️⃣ Milestone 14 – Visualizing with Boxplots
**Objective:** Using boxplots to understand data spread and detect outliers.
- **Concepts:**
    - **5-Number Summary:** Visual representation of Min, Q1, Median, Q3, and Max.
    - **Interquartile Range (IQR):** Understanding the "box" height as the middle 50% of data.
    - **Outlier Detection:** Identifying data points beyond 1.5 * IQR whiskers.
    - **Comparative Visualization:** Placing boxplots side-by-side to compare variability and central tendency across different columns.

### 1️⃣5️⃣ Milestone 15 – Detecting Outliers (Visual Inspection + Simple Rules)
**Objective:** Identify unusual data points thoughtfully using visual tools and basic statistical rules.
- **Script:** `pandas_outlier_detection_milestone.py`
- **Concepts:**
    - **What is an Outlier:** A value that differs significantly from the majority of the data, potentially caused by measurement error, data entry mistakes, or rare but valid events.
    - **Visual Inspection – Boxplots:** Using single and side-by-side boxplots to spot points beyond the 1.5×IQR whiskers across all numeric columns (`consumption_kwh`, `temperature_celsius`, `cost_inr`, `humidity_pct`).
    - **Visual Inspection – Scatter Plots:** Isolating extreme points by colour-coding outliers (red ✗) against the main data cluster; annotating values directly on the chart.
    - **IQR Rule (Statistical):** `Lower Bound = Q1 − 1.5×IQR`, `Upper Bound = Q3 + 1.5×IQR`. Applied per-column to systematically flag candidates.
    - **Threshold / Domain Rules:** Cross-checking flagged values against domain knowledge (e.g., consumption expected in [1, 50] kWh/h) to separate genuine anomalies from sensor artefacts.
    - **Outlier Count Bar Chart:** Bar chart summarising flagged count per column for a quick multi-column overview.
    - **Contextual Interpretation:** Reasoning through each flagged value (equipment fault, heat-wave, billing anomaly) before any removal or transformation decision.
- **Key Outputs:** 4 chart files in `outputs/figures/`:
    - `outlier_boxplot_consumption.png`
    - `outlier_boxplots_all_columns.png`
    - `outlier_scatter_highlighted.png`
    - `outlier_count_barchart.png`

---

# 🚀 FINAL SPRINT SUMMARY
The project is structurally sound with a clear data pipeline. All foundational Python and Pandas concepts have been mastered, establishing a production-ready environment for advanced analytics and modeling.

**Milestone 15 added:** Outlier detection using visual inspection (boxplots & scatter plots) and the IQR statistical rule, combined with domain-knowledge threshold checks. No values were removed — detection and reasoning precede any cleaning action.

---

# 🎞️ SUBMISSION GUIDELINES
All milestones include a ~2 minute video walkthrough demonstrating:
1. Tool/Interface interaction.
2. Concept application in code.
3. Rationale behind technical decisions.
4. Final verification of results.

---

# 🛠️ BEST PRACTICES
- **Environment Isolation:** Always use dedicated Conda environments.
- **Documentation:** Code explains "how", Markdown explains "why".
- **Data Integrity:** Never modify raw source files.
- **Redundancy:** Use `git` for version control and regular commits.
