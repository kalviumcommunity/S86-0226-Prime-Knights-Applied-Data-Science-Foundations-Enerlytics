# Applied Data Science Foundations – Enerlytics  
## Project: S86-0226 Prime Knights  
### Sprint 3 – Data Science  

---

# 📊 PROJECT STATUS

| Milestone | Status | Video |
|------------|--------|--------|
| Milestone 1 – Environment Setup | ✅ Complete | ⏳ Pending |
| Milestone 2 – Jupyter Navigation | ✅ Complete | ⏳ Pending |
| Milestone 3 – Kernel Control & Management | ✅ Complete | ⏳ Pending |
| Milestone 4 – Markdown Documentation | ✅ Complete | ⏳ Pending |
| Milestone 5 – Project Organization & Structure | ✅ Complete | ⏳ Pending |
| Milestone 6 – Python Scripts for Data Analysis | ✅ Complete | ⏳ Pending |
| Milestone 7 – Python Data Types (Numeric & String) | ✅ Complete | ⏳ Pending |
| Milestone 8 – Python Collections (Lists, Tuples, Dictionaries) | ✅ Complete | ⏳ Pending |

---

# 🟢 OVERALL STATUS: SPRINT-READY

The development environment has been successfully installed, verified, documented, and tested.  
All required components are operational and integrated correctly.  
Markdown documentation practices have been implemented in Jupyter notebooks.

---

# 📋 QUICK ENVIRONMENT SUMMARY

| Component | Version | Status |
|------------|----------|--------|
| Python | 3.14.3 | ✅ Installed |
| pip | 26.0 | ✅ Installed |
| Conda | Latest | ✅ Installed |
| Jupyter | Latest | ✅ Installed |
| Active Environment | base | ✅ Active |

---

# TABLE OF CONTENTS

1. System Information  
2. Python Installation Verification  
3. Anaconda Installation  
4. Environment Setup & Package Installation  
5. Milestone 1 – Full Environment Verification  
6. Integration Summary  
7. Video Walkthrough Guide  
8. Troubleshooting  
9. Pull Request Submission  
10. Milestone 2 – Jupyter Notebook Navigation  
11. Milestone 3 – Running, Restarting, and Interrupting Jupyter Kernels  
12. Milestone 4 – Writing Markdown for Professional Documentation  
13. Milestone 5 – Project Organization & Structure  
14. Milestone 6 – Python Scripts for Data Analysis  
15. Milestone 7 – Python Data Types (Numeric & String)  
16. Milestone 8 – Python Collections (Lists, Tuples, Dictionaries)  
17. Submission Guidelines  
18. Professional Best Practices  
19. Why Verification Matters  
20. Final Status Summary  

---

# 1️⃣ SYSTEM INFORMATION

- **Operating System:** Windows  
- **Setup Date:** February 24, 2026  
- **Team:** Prime Knights  
- **Project Code:** S86-0226  
- **Course:** Applied Data Science Foundations  
- **Sprint:** Sprint 3  

---

# 2️⃣ PYTHON INSTALLATION VERIFICATION

## ✅ Status: Installed and Functional

Python is successfully installed and accessible through PowerShell.

## Version Check

```powershell
python --version
```

Output:

```
Python 3.14.3
```

## pip Verification

```powershell
pip --version
```

Output:

```
pip 26.0 (python 3.14)
```

## Python REPL Test

```powershell
python
```

Inside REPL:

```python
print("Hello Data Science")
import sys
print(sys.executable)
exit()
```

### Result

- Python executable verified  
- pip functional  
- PATH correctly configured  
- Interactive shell working  

---

# 3️⃣ ANACONDA INSTALLATION

## ✅ Status: Installed Successfully

Anaconda Individual Edition (Windows 64-bit) installed.

## Installation Summary

1. Downloaded installer from official Anaconda website  
2. Selected Windows 64-bit version  
3. Installed using “Just Me” option  
4. Registered as default Python  
5. Completed installation  

## Verify Conda

Open **Anaconda Prompt** and run:

```powershell
conda --version
```

List environments:

```powershell
conda env list
```

Activate base environment:

```powershell
conda activate base
```

---

# 4️⃣ ENVIRONMENT SETUP & PACKAGE INSTALLATION

## Create Dedicated Sprint Environment (Recommended)

```powershell
conda create -n ds-sprint3 python=3.11 -y
```

Activate:

```powershell
conda activate ds-sprint3
```

Verify:

```powershell
python --version
```

---

## Install Core Data Science Libraries

```powershell
conda install numpy pandas matplotlib seaborn scikit-learn jupyter -y
```

Test installation:

```powershell
python -c "import pandas; import numpy; import matplotlib"
```

If no errors appear, installation is successful.

---

# 5️⃣ MILESTONE 1 – FULL ENVIRONMENT VERIFICATION

## Verification Date
February 24, 2026

## Operating System
Windows

## Status
✅ COMPLETE

---

## 5.1 Python Verification

Commands executed:

```powershell
python --version
pip --version
```

REPL tested successfully.

Result: ✅ PASSED

---

## 5.2 Conda Verification

From Anaconda Prompt:

```powershell
conda --version
conda env list
conda activate base
conda info --envs
```

Result: ✅ PASSED

---

## 5.3 Jupyter Verification

Launch Jupyter:

```powershell
jupyter notebook
```

Browser opened successfully at:

```
http://localhost:8888/
```

---

## Notebook Execution Test

Cell 1:

```python
print("Jupyter is working correctly")
```

Cell 2:

```python
import platform
print(platform.system())
```

Cell 3:

```python
import sys
print(sys.version)
```

All cells executed successfully.

Result: ✅ PASSED

---

# 6️⃣ INTEGRATION SUMMARY

All components verified working together:

- Python executable working  
- pip functional  
- Conda environment activation working  
- Jupyter launching without errors  
- Notebook kernel active  
- Browser integration successful  

Environment is stable and ready for Data Science workflows.

---

# 7️⃣ VIDEO WALKTHROUGH GUIDE

### Required Length
Approximately 2 minutes.

---

## Part 1 – Terminal Verification

Show:

- python --version  
- pip --version  
- conda --version  
- conda env list  
- conda activate base  

---

## Part 2 – Jupyter Demonstration

- Launch notebook  
- Show Home interface  
- Create notebook  
- Run simple print cell  
- Show successful output  

---

## Part 3 – README Walkthrough

- Scroll verification section  
- Highlight checklist  
- Confirm Milestone 1 completion  

---

## Recording Tools

- Windows Game Bar  
- OBS Studio  
- Loom  
- ShareX  

---

# 8️⃣ TROUBLESHOOTING

## Conda Not Recognized

Solution:

- Use Anaconda Prompt  
- Restart terminal  
- Verify PATH includes Anaconda directory  

---

## Python Version Conflict

Solution:

```powershell
conda activate base
python --version
```

---

## Jupyter Not Launching

Try:

```powershell
jupyter notebook --no-browser
```

Or reinstall:

```powershell
conda install jupyter -y
```

---

# 9️⃣ PULL REQUEST SUBMISSION

## Required in PR

- Updated README  
- Verification documentation  
- Video link  
- Confirmation checklist  

---

## PR Template

```markdown
## Milestone 1: Environment Verification

Summary:
Environment fully verified and operational.

System:
OS: Windows
Python: 3.14.3
Conda: Verified
Jupyter: Working

Video:
[Insert Link]

Status:
All checks passed.
```

---

# 🔟 MILESTONE 2 – JUPYTER NOTEBOOK NAVIGATION

## Objective

Gain confidence navigating Jupyter before starting analysis.

---

## Learning Goals

- Launch Jupyter correctly  
- Understand Home interface  
- Navigate directories intentionally  
- Create notebooks in correct folder  
- Run verification cells  

---

## Step 1 – Launch Notebook

```bash
jupyter notebook
```

Ensure correct environment is active.

---

## Step 2 – Explore Interface

Identify:

- File listing  
- Folder navigation  
- Breadcrumb trail  
- New notebook button  
- Upload button  

---

## Step 3 – Navigate Folders

- Enter project directory  
- Move between folders  
- Confirm working location  

---

## Step 4 – Create Notebook

Create new Python 3 notebook.

Test cell:

```python
print("Notebook working correctly")
```

---

## Step 5 – File Management

Practice:

- Rename notebook  
- Save changes  
- Close notebook  
- Reopen from Home page  

---

# 1️⃣1️⃣ MILESTONE 3 – RUNNING, RESTARTING, AND INTERRUPTING JUPYTER KERNELS

## Objective

Master kernel control and debugging techniques for predictable notebook behavior.

---

## Learning Goals

- Understand what a Jupyter kernel is and why it matters  
- Run notebook cells in a controlled way  
- Restart kernels to reset notebook state  
- Interrupt long-running or stuck executions safely  
- Maintain a clean, predictable notebook state  

---

## Status
✅ COMPLETE

---

## Why This Matters

Common notebook problems include:

- Code working once but failing later  
- Variables mysteriously changing values  
- Cells depending on hidden execution order  
- Kernels freezing during execution  

These issues usually come from poor kernel management, not bad logic.

---

## What Was Accomplished

### 1. Running Cells and Understanding Execution Order

**Objective:** Run notebook cells deliberately and observe execution order effects.

**Tasks Completed:**
- Executed cells one by one  
- Observed how outputs depend on execution order  
- Confirmed that kernel remembers variables until restarted  

**Key Learning:**  
Understanding hidden state in notebooks prevents unexpected behavior.

---

### 2. Restarting the Kernel

**Objective:** Reset notebook state for reproducibility testing.

**Tasks Completed:**
- Used restart option from Jupyter menu  
- Observed that variables and memory are cleared  
- Reran cells from the top to restore state  

**Key Learning:**  
Essential for testing notebook reproducibility and cleaning slate.

---

### 3. Interrupting Execution

**Objective:** Safely stop long-running or stuck operations.

**Tasks Completed:**
- Started deliberately long-running operations  
- Interrupted execution using interrupt option  
- Confirmed notebook remained responsive afterward  

**Key Learning:**  
Prevents frozen notebooks and saves debugging time.

---

### 4. Recognizing When to Restart vs Interrupt

**Objective:** Understand the trade-offs between restart and interrupt actions.

**Scenarios Identified:**

#### When to Interrupt:
- Cell taking too long to execute  
- Accidentally triggered infinite loop  
- Want to stop current execution without losing variables  

#### When to Restart:
- Variables in inconsistent state  
- Need to test reproducibility from scratch  
- Debugging mysterious behavior  
- Before final submission  

**Key Learning:**  
Choosing the right action saves time and prevents data loss.

---

## Practical Examples Demonstrated

### Example 1: Execution Order

```python
# Cell 1
x = 10
print(f"x = {x}")
```

```python
# Cell 2
y = x + 5
print(f"y = {y}")
```

**Observation:** Running Cell 2 before Cell 1 causes NameError.

---

### Example 2: Variable Persistence

```python
# Cell 1
counter = 0
```

```python
# Cell 2
counter += 1
print(counter)
```

**Observation:** Running Cell 2 multiple times shows increasing values.  
**Solution:** Restart kernel to reset counter.

---

### Example 3: Interrupting Long Operations

```python
# Deliberately long operation
import time
for i in range(1000000):
    time.sleep(0.001)
    print(i)
```

**Action:** Interrupt execution using kernel interrupt button.  
**Result:** Cell stops, notebook remains responsive.

---

## Video Walkthrough Checklist

✅ Running cells normally  
✅ Interrupting a running cell  
✅ Restarting the kernel  
✅ Rerunning cells after restart  
✅ Explanation of why each action is used  

**Duration:** Approximately 2 minutes  
**Recording Type:** Screen-facing and clearly visible  

---

## Best Practices Learned

1. **Always run cells in order** during development  
2. **Restart and run all cells** before sharing notebooks  
3. **Interrupt first**, restart if that doesn't help  
4. **Use restart for debugging** mysterious state issues  
5. **Test reproducibility** by restarting kernel regularly  

---

## Professional Workflow Integration

Kernel management prevents:
- Subtle hard-to-debug errors  
- Non-reproducible results  
- Collaboration inconsistencies  
- Wasted debugging time  

Kernel management enables:
- Consistent notebook behavior  
- Systematic debugging approach  
- Reproducible results for reviewers  
- Professional development standards  

---

# 1️⃣2️⃣ MILESTONE 4 – WRITING MARKDOWN FOR PROFESSIONAL DOCUMENTATION

## 🎯 Objective

Master Markdown syntax in Jupyter notebooks to create clear, professional, and review-ready documentation that transforms code scratchpads into complete data stories.

## ✅ Status: COMPLETE

All Markdown documentation requirements have been implemented in `Untitled.ipynb`.

---

## 📝 What Was Accomplished

### 1. Heading Hierarchy
- ✅ Demonstrated all 6 heading levels (`#` through `######`)
- ✅ Created logical hierarchical structure
- ✅ Used headings for clear navigation and organization
- ✅ Maintained consistent heading patterns throughout

### 2. Lists for Clear Communication
- ✅ **Unordered lists** for general points and bullet items
- ✅ **Ordered lists** for step-by-step processes
- ✅ **Nested lists** for complex workflows and hierarchies
- ✅ Mixed list structures for comprehensive explanations

### 3. Inline Code and Code Blocks
- ✅ Used backticks for inline code: `variables`, `functions()`, `modules`
- ✅ Created fenced code blocks with syntax highlighting
- ✅ Demonstrated multiple languages (Python, SQL, Bash)
- ✅ Explained when to use code blocks vs code cells

### 4. Combining Markdown and Code
- ✅ Implemented **Explain → Execute → Interpret** pattern
- ✅ Created practical examples with real Python code
- ✅ Documented intent before code execution
- ✅ Interpreted results after code output
- ✅ Maintained clean narrative flow throughout notebook

### 5. Professional Best Practices
- ✅ Added documentation checklist
- ✅ Created common mistakes reference table
- ✅ Provided professional notebook structure template
- ✅ Explained why communication matters in data science

---

## 📊 Notebook Structure

The demonstration notebook includes:

1. **Title and Introduction** – Project context and purpose
2. **Table of Contents** – Complete navigation structure
3. **Section 1: Headings** – Hierarchy and organization examples
4. **Section 2: Lists** – Ordered, unordered, and nested examples
5. **Section 3: Code Formatting** – Inline code and code blocks
6. **Section 4: Narrative Flow** – Combining Markdown and Code
7. **Section 5: Best Practices** – Professional tips and guidelines
8. **Summary** – Key takeaways and assignment completion checklist

---

## 💡 Key Concepts Demonstrated

### The Narrative Flow Pattern

```
EXPLAIN (Markdown) → EXECUTE (Code) → INTERPRET (Markdown)
```

This pattern ensures:
- Clear documentation of intent
- Executable, reproducible code
- Meaningful interpretation of results
- Professional presentation

### Code vs Markdown Decision Guide

| Use Markdown When | Use Code When |
|-------------------|---------------|
| Explaining intent | Executing Python |
| Interpreting results | Producing output |
| Structuring notebook | Performing calculations |
| Writing conclusions | Running analyses |

**Core Principle:** *Code executes. Markdown explains.*

---

## 📁 Files Modified

- **Untitled.ipynb** – Complete Markdown demonstration notebook with:
  - 15 cells total
  - 13 Markdown cells
  - 2 Code cells with practical examples
  - Professional structure and formatting

---

## 🎓 Learning Outcomes Achieved

By completing this milestone, the following skills were demonstrated:

1. ✅ Structure notebooks using meaningful headings
2. ✅ Document steps and assumptions using Markdown text
3. ✅ Use lists to explain workflows and results
4. ✅ Format code snippets inside Markdown cells
5. ✅ Create notebooks that are readable and review-friendly
6. ✅ Combine text and code to tell clear data stories

---

## 📹 Video Requirements

A ~2 minute screen-capture video should demonstrate:

- [ ] Creating a Markdown cell
- [ ] Writing headings at different levels
- [ ] Creating ordered and unordered lists
- [ ] Adding inline code with backticks
- [ ] Adding code blocks with syntax highlighting
- [ ] Switching between Markdown and code cells
- [ ] Brief explanation of why documentation matters

---

## 🔍 Why This Milestone Matters

### Common Notebook Problems Solved

❌ **Before Good Markdown:**
- Notebooks hard to follow or review
- No explanation of what code does
- Results shown without context
- Confusing execution flow
- Looks unprofessional

✅ **After Good Markdown:**
- Clear reasoning documented
- Reviewers understand approach
- Teammates can follow work
- Professional appearance
- Reproducible and maintainable

### Communication as a Technical Skill

> **Markdown is not optional—it's essential.**

- Your code may work perfectly, but if no one understands it, it has limited value
- Notebooks are communication tools, not just execution environments
- Good documentation makes code reviewable, reproducible, and professional
- Clear Markdown improves collaboration and career prospects

---

## ✨ Best Practices Implemented

### Documentation Checklist
- ✅ Title and author information at the top
- ✅ Clear section headings throughout
- ✅ Markdown cells explain the "why" before each analysis
- ✅ Code cells are clean and focused
- ✅ Results are interpreted, not just displayed
- ✅ Summary concludes key findings

### Professional Notebook Structure
```
1. Title and Introduction (Markdown)
2. Table of Contents (Markdown)
3. Import Libraries (Code + Markdown)
4. Load Data (Code + Markdown)
5. Exploration (Alternating)
6. Analysis (Alternating)
7. Results (Markdown)
8. Conclusions (Markdown)
```

---

## 🎯 Assignment Completion Status

| Requirement | Status |
|-------------|--------|
| Write headings to structure content | ✅ Complete |
| Create lists for clear explanations | ✅ Complete |
| Use inline code and code blocks | ✅ Complete |
| Combine Markdown and Code effectively | ✅ Complete |
| Demonstrate professional practices | ✅ Complete |
| Record video walkthrough (~2 min) | ⏳ Pending |

---

# 1️⃣3️⃣ MILESTONE 5 – ORGANIZING RAW DATA, PROCESSED DATA, AND OUTPUT ARTIFACTS

## 🎯 Objective

Master the discipline of separating raw data (immutable), processed data (derived), and output artifacts (results) to ensure data integrity, reproducibility, and professional workflows.

## ✅ Status: Complete

This milestone demonstrates proper data organization through a complete working example with real files and a Python script showing the correct workflow.

---

## 🚀 PRACTICAL DEMONSTRATION

### Files Created for This Milestone

| File/Folder | Purpose | Status |
|-------------|---------|--------|
| [`data/raw/energy_usage_sample.csv`](data/raw/energy_usage_sample.csv) | **Original raw data** (48 records, 2 customers) | ✅ Created |
| [`process_data.py`](process_data.py) | **Processing script** demonstrating workflow | ✅ Created |
| [`data/processed/energy_usage_cleaned.csv`](data/processed/energy_usage_cleaned.csv) | **Processed data** with engineered features | ✅ Generated |
| [`outputs/figures/energy_consumption_analysis.png`](outputs/figures/energy_consumption_analysis.png) | **Visualization** of consumption patterns | ✅ Generated |
| [`outputs/reports/analysis_summary.txt`](outputs/reports/analysis_summary.txt) | **Text report** with key findings | ✅ Generated |
| [`data/README.md`](data/README.md) | **Data organization guide** (comprehensive) | ✅ Created |

### Running the Demonstration

Execute the processing script to see the complete workflow in action:

```bash
python process_data.py
```

**What it demonstrates:**
1. ✅ Reads from `data/raw/` (read-only, never modified)
2. ✅ Processes and cleans data in memory
3. ✅ Saves processed data to `data/processed/`
4. ✅ Generates visualizations in `outputs/figures/`
5. ✅ Creates reports in `outputs/reports/`
6. ✅ Shows clear one-directional data flow

---

## 📊 DATA FLOW DIAGRAM

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA LIFECYCLE                            │
└─────────────────────────────────────────────────────────────┘

   RAW DATA (Immutable)
   📁 data/raw/energy_usage_sample.csv
          │
          │ (READ ONLY - Never Modified)
          ↓
   
   PROCESSING SCRIPT
   🔄 process_data.py
          │
          │ (Transformations Applied)
          │ - Convert timestamps
          │ - Extract features
          │ - Remove duplicates
          │ - Add metadata
          ↓
   
   PROCESSED DATA (Derived)
   📁 data/processed/energy_usage_cleaned.csv
          │
          │ (Analysis Ready)
          ↓
   
   OUTPUT GENERATION
   🎨 Visualization & Reporting
          │
          ├─→ 📊 outputs/figures/energy_consumption_analysis.png
          └─→ 📄 outputs/reports/analysis_summary.txt

✓ One-directional flow
✓ Raw data preserved
✓ Reproducible workflow
```

---

## 🎓 LEARNING OBJECTIVES ACHIEVED

By completing this milestone, you can now:

| Objective | Status | Evidence |
|-----------|--------|----------|
| Understand difference between raw, processed, and output data | ✅ Complete | Data flow diagram & documentation |
| Learn why raw data should never be modified | ✅ Complete | Raw data remains unchanged after script execution |
| Organize data into clearly defined folders | ✅ Complete | Proper folder structure implemented |
| Prevent accidental overwrites and data leakage | ✅ Complete | One-directional workflow demonstrated |
| Build habits that support reproducibility | ✅ Complete | Complete workflow is reproducible |

---

## 1️⃣ UNDERSTANDING RAW DATA

### What is Raw Data?

**Raw data is the original, untouched source** — exactly as received from data collection systems, surveys, sensors, or downloads.

### Golden Rules for Raw Data

| Rule | Rationale | Example |
|------|-----------|---------|
| **NEVER edit raw files directly** | Preserves original evidence | Read with `pd.read_csv()`, never overwrite |
| **Treat as read-only** | Prevents accidental corruption | Use file permissions if possible |
| **Keep original filenames** | Maintains traceability | `energy_usage_sample.csv` not `data.csv` |
| **Store exactly as received** | Enables verification | Don't rename columns in source file |

### Why This Matters

Raw data is **evidence**. Think of it like:
- 🏛️ **Legal evidence** — must remain untampered
- 📜 **Historical record** — preserves what actually happened
- 🔬 **Scientific data** — enables peer verification

**If you modify raw data:**
- ❌ You lose ability to verify your analysis
- ❌ You can't reproduce results from scratch
- ❌ You break the audit trail
- ❌ You risk data corruption

### In Our Demonstration

```python
# ✓ CORRECT: Read raw data without modifying
df_raw = pd.read_csv('data/raw/energy_usage_sample.csv')

# Process on a COPY, never the original
df_processed = df_raw.copy()
```

**Result:** Raw file `energy_usage_sample.csv` remains unchanged after processing.

---

## 2️⃣ ORGANIZING PROCESSED DATA

### What is Processed Data?

**Processed data is derived from raw data** through cleaning, transformation, feature engineering, or aggregation.

### When to Save as Processed Data

Save to `data/processed/` when you:
- ✅ Remove duplicates
- ✅ Handle missing values (impute or drop)
- ✅ Correct data types
- ✅ Engineer features (extract hour, calculate ratios)
- ✅ Normalize or scale data
- ✅ Filter or subset data
- ✅ Aggregate to different time periods

### Naming Convention

Use **descriptive names** that indicate processing:

| ✅ Good Names | ❌ Bad Names | Why Good is Better |
|--------------|-------------|-------------------|
| `energy_usage_cleaned.csv` | `data2.csv` | Indicates cleaning applied |
| `daily_consumption_aggregated.csv` | `final.csv` | Shows aggregation level |
| `features_engineered_v2.csv` | `processed.csv` | Indicates versioning |

### Key Characteristics

- **Derived:** Can be recreated from raw data
- **Documented:** Transformations should be recorded
- **Versioned:** May have multiple versions (v1, v2)
- **Separate:** Never mixed with raw data

### In Our Demonstration

File created: `data/processed/energy_usage_cleaned.csv`

**Transformations applied:**
1. Converted timestamp to datetime type
2. Extracted hour feature
3. Removed duplicates (if any)
4. Added peak consumption indicator
5. Added processing metadata

```python
# Process and save to separate location
df_processed = df_raw.copy()
df_processed['timestamp'] = pd.to_datetime(df_processed['timestamp'])
df_processed['hour'] = df_processed['timestamp'].dt.hour
df_processed.to_csv('data/processed/energy_usage_cleaned.csv', index=False)
```

---

## 3️⃣ MANAGING OUTPUT ARTIFACTS

### What are Output Artifacts?

**Outputs are the final or intermediate results** of your analysis:
- 📊 **Visualizations** (plots, charts, graphs)
- 📄 **Reports** (PDFs, markdown, text files)
- 🤖 **Models** (trained ML models, pickled files)
- 📈 **Summaries** (statistics, tables, insights)

### Where to Store Outputs

```
outputs/
├── figures/        # Plots, charts, visualizations
└── reports/        # Analysis reports, summaries
```

**NOT in `data/` folder!**

### Why Separate Outputs from Data?

| Mixing Outputs with Data | Proper Separation |
|--------------------------|-------------------|
| ❌ Confuses inputs and results | ✅ Clear distinction |
| ❌ Breaks reproducibility | ✅ Can regenerate anytime |
| ❌ Clutters data folders | ✅ Clean organization |

### Best Practices for Outputs

1. **Use Descriptive Filenames**
   ```
   ✅ energy_consumption_analysis_2026-02-26.png
   ✅ peak_load_report_final.pdf
   ❌ plot1.png
   ❌ output.txt
   ```

2. **Include Dates for Versioning**
   - Helps track when analysis was run
   - Useful for before/after comparisons

3. **Organize by Type**
   - `figures/` for visualizations
   - `reports/` for documents
   - `models/` for ML artifacts

### In Our Demonstration

**Files created:**
1. `outputs/figures/energy_consumption_analysis.png`
   - Dual-panel visualization
   - Shows hourly patterns and customer totals

2. `outputs/reports/analysis_summary.txt`
   - Text report with key findings
   - Includes statistics and peak hour identification

```python
# Generate visualization in correct location
plt.savefig('outputs/figures/energy_consumption_analysis.png', dpi=300)

# Generate report in correct location
with open('outputs/reports/analysis_summary.txt', 'w') as f:
    f.write("ENERGY CONSUMPTION ANALYSIS REPORT\n")
    # ... write report content
```

---

## 4️⃣ PREVENTING DATA CONTAMINATION

### What is Data Contamination?

**Data contamination** occurs when you accidentally:
- Overwrite raw data with processed data
- Mix input and output files
- Create circular dependencies
- Lose track of data lineage

### Common Contamination Scenarios

#### ❌ Scenario 1: Overwriting Raw Data

```python
# WRONG! This destroys your original evidence
df = pd.read_csv('data/raw/original.csv')
df = df.dropna()
df.to_csv('data/raw/original.csv')  # ← Original is gone forever!
```

**Impact:** You can never verify if your cleaning was appropriate.

#### ✅ Correct Approach

```python
# RIGHT! Raw data remains intact
df_raw = pd.read_csv('data/raw/original.csv')
df_clean = df_raw.dropna()
df_clean.to_csv('data/processed/original_cleaned.csv')  # ← Separate file
```

---

#### ❌ Scenario 2: Circular Dependencies

```python
# WRONG! Creates confusion about data lineage
df1 = pd.read_csv('data/processed/data_v1.csv')
# ... process ...
df1.to_csv('data/raw/updated.csv')  # ← Processed data in raw folder!

df2 = pd.read_csv('data/raw/updated.csv')  # ← Now reading previously processed data
```

**Impact:** You lose track of what's original vs. derived.

#### ✅ Correct Approach

```python
# RIGHT! One-directional flow
df_raw = pd.read_csv('data/raw/original.csv')
df_v1 = clean_data(df_raw)
df_v1.to_csv('data/processed/clean_v1.csv')

df_v2 = engineer_features(df_v1)
df_v2.to_csv('data/processed/features_v2.csv')
```

---

### The One-Directional Flow Principle

**Data must flow in ONE direction:**

```
RAW → PROCESSED → OUTPUTS
  ↓       ↓          ↓
Never ← Never ← Never  (No backward flow!)
```

### Prevention Checklist

Before running any data script, ask:

- [ ] Am I reading from `data/raw/`?
- [ ] Am I writing to `data/processed/` or `outputs/`?
- [ ] Am I NEVER overwriting files in `data/raw/`?
- [ ] Can I delete processed data and recreate it from raw?
- [ ] Is my data flow one-directional?

### In Our Demonstration

The `process_data.py` script demonstrates perfect separation:

```python
# ✓ Read from raw (read-only)
df_raw = pd.read_csv('data/raw/energy_usage_sample.csv')

# ✓ Process in memory
df_processed = df_raw.copy()
# ... apply transformations ...

# ✓ Write to processed (separate location)
df_processed.to_csv('data/processed/energy_usage_cleaned.csv')

# ✓ Generate outputs (separate location)
plt.savefig('outputs/figures/energy_consumption_analysis.png')
```

**Verification:**
- Raw data file remains unchanged ✅
- Processed data is clearly separate ✅
- Outputs are in dedicated folders ✅
- Workflow is reproducible ✅

---

## 📁 PROJECT STRUCTURE OVERVIEW

```
S86-0226-Prime-Knights-Applied-Data-Science-Foundations-Enerlytics/
│
├── data/                      # Data Storage (NEVER commit raw data to git)
│   ├── raw/                   # Original, immutable data
│   ├── processed/             # Cleaned and transformed datasets
│   └── external/              # Third-party or reference data
│
├── notebooks/                 # Jupyter Notebooks
│   ├── exploratory/           # Initial data exploration and EDA
│   └── analysis/              # Final analysis and reporting notebooks
│
├── src/                       # Source code and scripts
│   └── (Python modules for reusable code)
│
├── outputs/                   # Generated outputs
│   ├── figures/               # Visualizations and plots
│   └── reports/               # Analysis reports and documents
│
├── models/                    # Trained models and model artifacts
│
├── docs/                      # Project documentation
│
├── README.md                  # Project overview and documentation
└── requirements.txt           # Python dependencies (to be created)
```

---

## 📂 FOLDER PURPOSES & BEST PRACTICES

### 1. **`data/` Directory**

#### `data/raw/`
- **Purpose:** Store original, unmodified energy consumption datasets
- **Rule:** NEVER modify files in this folder
- **Example Files:** `energy_usage_2026.csv`, `peak_load_data.xlsx`
- **Best Practice:** Treat as read-only; preserve data integrity

#### `data/processed/`
- **Purpose:** Store cleaned and transformed data ready for analysis
- **Example Files:** `cleaned_energy_data.csv`, `peak_periods_identified.csv`
- **Best Practice:** Document transformations applied

#### `data/external/`
- **Purpose:** Store third-party datasets (weather data, holiday calendars, etc.)
- **Example Files:** `weather_data.csv`, `public_holidays.json`
- **Use Case:** Correlate energy usage with external factors

---

### 2. **`notebooks/` Directory**

#### `notebooks/exploratory/`
- **Purpose:** Initial data exploration and hypothesis generation
- **Naming Convention:** `01_initial_exploration.ipynb`, `02_peak_analysis.ipynb`
- **Content:** EDA, data quality checks, visualization experiments

#### `notebooks/analysis/`
- **Purpose:** Final, polished analysis notebooks
- **Naming Convention:** `final_peak_load_analysis.ipynb`
- **Content:** Production-ready analysis with clear conclusions

**Best Practice:** Use numbered prefixes (01_, 02_) to indicate sequence

---

### 3. **`src/` Directory**

- **Purpose:** Reusable Python scripts and modules
- **Example Files:** `data_cleaning.py`, `peak_detection.py`, `visualization_utils.py`
- **Best Practice:** Extract repeated code from notebooks into modules
- **Benefit:** Keeps notebooks clean and promotes code reuse

---

### 4. **`outputs/` Directory**

#### `outputs/figures/`
- **Purpose:** Store generated plots and visualizations
- **Example Files:** `peak_load_heatmap.png`, `daily_consumption_trend.pdf`
- **Best Practice:** Use descriptive filenames with dates

#### `outputs/reports/`
- **Purpose:** Store analysis reports and presentations
- **Example Files:** `energy_analysis_report.pdf`, `findings_summary.md`
- **Use Case:** Share insights with stakeholders

---

### 5. **`models/` Directory**

- **Purpose:** Store trained machine learning models (if applicable)
- **Example Files:** `peak_predictor.pkl`, `anomaly_detector.h5`
- **Best Practice:** Include model version and training date in filename

---

### 6. **`docs/` Directory**

- **Purpose:** Additional project documentation
- **Example Files:** `data_dictionary.md`, `analysis_methodology.md`
- **Best Practice:** Document assumptions, decisions, and methodologies

---

## 🎯 PROJECT-SPECIFIC CONTEXT: ENERLYTICS

**Project Statement:**  
Energy providers record electricity consumption at granular intervals but struggle to communicate usage patterns to consumers. This project analyzes energy usage data to identify:

1. **Peak Load Periods** – When consumption is highest
2. **Daily Consumption Cycles** – Typical usage patterns throughout the day
3. **Abnormal Spikes** – Unusual consumption events requiring investigation

**How Structure Supports Analysis:**

| Analysis Task | Relevant Folders | Workflow |
|--------------|------------------|----------|
| Load raw energy data | `data/raw/` | Import original CSV/Excel files |
| Clean and preprocess | `src/`, `data/processed/` | Run cleaning scripts, save results |
| Explore patterns | `notebooks/exploratory/` | EDA to identify trends |
| Identify peak periods | `notebooks/analysis/` | Time-series analysis |
| Visualize findings | `outputs/figures/` | Generate plots and heatmaps |
| Document insights | `outputs/reports/` | Create stakeholder reports |

---

## ✅ WHY THIS STRUCTURE MATTERS

### Problems It Solves:
- ❌ **Broken File Paths:** Predictable structure prevents path errors
- ❌ **Lost Files:** Clear organization makes everything easy to find
- ❌ **Data Corruption:** Separation prevents accidental overwrites
- ❌ **Collaboration Confusion:** Team members can navigate intuitively
- ❌ **Reproducibility Issues:** Standardized layout enables replication

### Benefits:
- ✅ **Scalability:** Structure grows with project complexity
- ✅ **Clarity:** Purpose of each folder is immediately clear
- ✅ **Professionalism:** Demonstrates industry best practices
- ✅ **Collaboration:** Team members can contribute seamlessly
- ✅ **Review-Ready:** Instructors and peers can navigate easily

---

## 🔄 BEST PRACTICES IMPLEMENTED

1. **Lowercase and Consistent Naming**
   - Folders use lowercase with underscores
   - No spaces or special characters
   - Predictable and readable

2. **Separation of Concerns**
   - Code, data, and outputs are isolated
   - Prevents accidental modifications
   - Maintains data integrity

3. **Logical Grouping**
   - Related items stored together
   - Minimal nesting (2-3 levels max)
   - Easy to navigate

4. **Documentation First**
   - README.md explains structure
   - Each major folder has clear purpose
   - New team members onboard quickly

5. **Version Control Ready**
   - `.gitignore` should exclude `data/` and large outputs
   - Code and notebooks tracked in git
   - Reproducible without committing raw data

---

## 🎯 WHY THIS MILESTONE MATTERS

### Common Data Management Problems (SOLVED)

This milestone addresses critical issues that plague Data Science projects:

| Problem | Impact | Our Solution |
|---------|--------|--------------|
| **Raw data overwritten accidentally** | Lost evidence, can't verify analysis | Raw data remains read-only |
| **No record of how processed data was created** | Not reproducible | Clear processing script |
| **Outputs mixed with input data** | Confusion about sources | Separate `outputs/` folder |
| **Confusion about final vs intermediate files** | Workflow breaks | Clear naming conventions |
| **Inability to reproduce results later** | Trust issues | Complete workflow documentation |

### What This Discipline Enables

✅ **Data Integrity:** Raw data never corrupted  
✅ **Reproducibility:** Anyone can recreate results  
✅ **Auditability:** Clear trail from raw to results  
✅ **Collaboration:** Team members understand workflow  
✅ **Professional Credibility:** Demonstrates best practices  
✅ **Regulatory Compliance:** Meets data governance standards  

### Think of Raw Data as Evidence

> **"Raw data is like evidence in a trial — it must remain untampered to maintain credibility."**

- You **protect** it
- You **preserve** it
- You **reference** it
- You **never modify** it

Everything else is derived and can be recreated.

---

## 📋 ASSIGNMENT COMPLETION STATUS

| Requirement | Status | Evidence |
|-------------|--------|----------|
| 1. Understanding Raw Data | ✅ Complete | Section with rules & examples |
| 2. Organizing Processed Data | ✅ Complete | Sample processed file created |
| 3. Managing Output Artifacts | ✅ Complete | Figures & reports generated |
| 4. Preventing Data Contamination | ✅ Complete | Contamination scenarios documented |
| 5. Create separate folders | ✅ Complete | Full structure implemented |
| 6. Demonstrate workflow | ✅ Complete | `process_data.py` script |
| 7. Use meaningful naming | ✅ Complete | Descriptive filenames used |
| 8. Never modify raw data | ✅ Complete | Raw file remains unchanged |

---

## 🎥 VIDEO WALKTHROUGH REQUIREMENTS

Your ~2 minute video must demonstrate:

### Required Components

- [ ] **Show `data/raw/` folder and explain:**
  - Purpose: Store original, immutable data
  - Rule: Never modify files here
  - Example: `energy_usage_sample.csv`

- [ ] **Show `data/processed/` folder and explain:**
  - Purpose: Store cleaned, derived datasets
  - How it's different from raw
  - Example: `energy_usage_cleaned.csv`

- [ ] **Show `outputs/` folder and explain:**
  - Purpose: Store analysis results
  - Subfolders: `figures/` and `reports/`
  - Examples: Visualization and report files

- [ ] **Demonstrate the workflow:**
  - Run `python process_data.py`
  - Show it reads from raw (unchanged)
  - Show it creates processed data
  - Show it generates outputs

- [ ] **Explain the rationale:**
  - Why separate data stages?
  - What risks does this prevent?
  - How does this support reproducibility?

### Video Requirements

**Duration:** Approximately 2 minutes  
**Format:** Screen capture with audio narration  
**Must be:** Screen-facing and clearly visible  
**Must show:** Actual files and folder structures, not just slides

---

## 📚 ADDITIONAL RESOURCES

For deeper understanding:

- **Data Organization README:** See [`data/README.md`](data/README.md) for comprehensive guide
- **Processing Script:** Review [`process_data.py`](process_data.py) for complete workflow
- **Industry Standard:** [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
- **Best Practices:** [Good Enough Practices in Scientific Computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)

---

## ✅ VERIFICATION CHECKLIST

Before submitting, verify:

- [ ] Raw data exists in `data/raw/` and is unchanged
- [ ] Processed data exists in `data/processed/` with different content
- [ ] Outputs exist in `outputs/figures/` and `outputs/reports/`
- [ ] Processing script (`process_data.py`) runs successfully
- [ ] Script demonstrates one-directional flow (raw → processed → outputs)
- [ ] No output files are in data folders
- [ ] No data files are in output folders
- [ ] Can delete processed/outputs and recreate from raw
- [ ] Data README explains organization principles
- [ ] Video demonstrates all required components

---

## 🎓 KEY TAKEAWAYS

### Core Principles Learned

1. **Raw Data is Immutable**
   -Read-only, never modified, preserves evidence

2. **Processed Data is Derived**
   - Can be recreated from raw data anytime

3. **Outputs are Results**
   - Generated from data, not part of data pipeline

4. **One-Directional Flow**
   - RAW → PROCESSED → OUTPUTS (no backward flow)

5. **Clear Separation Prevents Errors**
   - Confusion leads to contamination
   - Organization ensures integrity

### Professional Impact

> **"Good data organization is not optional — it's foundational."**

This milestone establishes habits that:
- Prevent costly mistakes
- Enable collaboration
- Build professional credibility
- Support career growth in Data Science

---

# 1️⃣4️⃣ MILESTONE 6 – CREATING AND RUNNING PYTHON SCRIPTS FOR DATA ANALYSIS

## 🎯 Objective

Master the fundamentals of creating and executing standalone Python scripts (.py files) for data analysis. Learn when to use scripts versus notebooks and build confidence running code outside interactive environments.

## ✅ Status: Complete

This milestone demonstrates script-based data analysis through practical examples, showing the complete workflow from creation to execution, and understanding the critical differences between scripts and notebooks.

---

## 🚀 PRACTICAL DEMONSTRATION

### Files Created for This Milestone

| File/Folder | Purpose | Status |
|-------------|---------|--------|
| [`analyze_energy.py`](analyze_energy.py) | **First Python script** for energy data analysis | ✅ Created |
| [`SCRIPT_VS_NOTEBOOK.md`](SCRIPT_VS_NOTEBOOK.md) | **Comprehensive guide** explaining scripts vs notebooks | ✅ Created |

### Running the Script

Execute the analysis script from the command line:

```bash
python analyze_energy.py
```

**What it does:**
1. ✅ Loads energy consumption data from CSV
2. ✅ Calculates basic statistics (mean, max, min, total)
3. ✅ Analyzes consumption by customer
4. ✅ Prints formatted results to console
5. ✅ Executes top-to-bottom without user interaction

---

## 📊 SCRIPT EXECUTION OUTPUT

```
============================================================
ENERGY CONSUMPTION ANALYSIS SCRIPT
============================================================

Step 1: Loading energy data...
✓ Data loaded successfully from data/raw/energy_usage_sample.csv

Step 2: Examining the data...
Number of records: 48
Number of columns: 4
Column names: timestamp, customer_id, consumption_kwh, temperature_celsius

Step 3: First 5 rows of data:
             timestamp customer_id  consumption_kwh  temperature_celsius
0  2026-02-01 00:00:00     CUST001              2.5                   18
1  2026-02-01 01:00:00     CUST001              1.8                   17
2  2026-02-01 02:00:00     CUST001              1.5                   16
3  2026-02-01 03:00:00     CUST001              1.3                   16
4  2026-02-01 04:00:00     CUST001              1.4                   15

Step 4: Calculating statistics...
------------------------------------------------------------
Average energy consumption: 3.72 kWh
Maximum energy consumption: 7.80 kWh
Minimum energy consumption: 1.30 kWh
Total energy consumption: 178.70 kWh

Average temperature: 18.75°C
Maximum temperature: 23.00°C
Minimum temperature: 15.00°C

Step 5: Analyzing consumption by customer...
------------------------------------------------------------
Total consumption by customer:
  CUST001: 77.60 kWh
  CUST002: 101.10 kWh

============================================================
ANALYSIS COMPLETE!
============================================================
Processed 48 records successfully.
All calculations completed without errors.
```

---

## 🔄 SCRIPTS VS NOTEBOOKS: KEY DIFFERENCES

### When to Use Python Scripts

| Use Case | Why Scripts Excel |
|----------|-------------------|
| **Automation** | Can be scheduled, run in pipelines, integrated into systems |
| **Reproducibility** | Same input always produces same output |
| **Version Control** | Git-friendly, easy to track changes |
| **Production** | Reliable, no hidden state, proper error handling |
| **Reusability** | Can be imported as modules, used across projects |

### When to Use Jupyter Notebooks

| Use Case | Why Notebooks Excel |
|----------|---------------------|
| **Exploration** | Interactive, try different approaches quickly |
| **Visualization** | Inline plots and rich media |
| **Communication** | Combine code, results, and narrative |
| **Teaching** | Step-by-step demonstrations |
| **Prototyping** | Rapid iteration and experimentation |

---

## 📝 SCRIPT STRUCTURE EXPLAINED

```python
# 1. DOCSTRING - Explains what the script does
"""
Purpose, author, date, and description
"""

# 2. IMPORTS - Load required libraries
import pandas as pd

# 3. SETUP - Define paths, constants, configurations
data_file = 'data/raw/energy_usage_sample.csv'

# 4. MAIN LOGIC - Execute the analysis
# Runs top to bottom in order
df = pd.read_csv(data_file)
print(df.head())

# 5. RESULTS - Print or save outputs
print("Analysis complete!")
```

---

## ✅ MILESTONE COMPLETION CHECKLIST

| Task | Completed |
|------|-----------|
| Created a Python script file (.py) | ✅ Yes |
| Added clear docstring and comments | ✅ Yes |
| Wrote simple data analysis logic | ✅ Yes |
| Ran script from command line | ✅ Yes |
| Observed and verified output | ✅ Yes |
| Understood script execution flow | ✅ Yes |
| Documented scripts vs notebooks | ✅ Yes |
| Created comparison guide | ✅ Yes |

---

## 🎓 KEY LEARNINGS

### 1. Script Execution Flow
- Scripts run **sequentially** from top to bottom
- No persistent state between runs
- Variables don't remain in memory after execution
- Each run is fresh and independent

### 2. Reproducibility
- Same script + same data = same results
- No hidden cell execution order issues
- Perfect for automated workflows
- Essential for production environments

### 3. Real-World Workflow
```
EXPLORE (Notebook) → REFINE (Notebook) → PRODUCTIONIZE (Script)
      ↓                    ↓                      ↓
  Try ideas         Find what works        Run reliably
  Visualize         Test approaches        Automate
  Iterate           Prototype              Deploy
```

### 4. Professional Practice
- Scripts for **doing** work (automation, pipelines)
- Notebooks for **showing** work (reports, presentations)
- Both are essential tools for Data Scientists

---

## 🔧 HOW TO RUN PYTHON SCRIPTS

### Method 1: Command Line (Recommended)
```bash
# Navigate to project directory
cd path/to/project

# Run the script
python analyze_energy.py
```

### Method 2: With Full Path
```bash
python "b:\BHANU\enerlytics\S86-0226-Prime-Knights-Applied-Data-Science-Foundations-Enerlytics\analyze_energy.py"
```

### Method 3: From VS Code
1. Open the `.py` file
2. Right-click in editor
3. Select "Run Python File in Terminal"

---

## 💡 COMMON BEGINNER MISTAKES TO AVOID

| ❌ Mistake | ✅ Correct Approach |
|------------|---------------------|
| Using notebooks for everything | Use scripts for automation, notebooks for exploration |
| Expecting variables to persist | Scripts have no memory between runs |
| Running cells out of order | Scripts always run top-to-bottom |
| Not testing script execution | Always run the full script to verify |
| Mixing interactive features | Scripts can't use widgets or interactive displays |

---

## 📚 ADDITIONAL RESOURCES

- [`SCRIPT_VS_NOTEBOOK.md`](SCRIPT_VS_NOTEBOOK.md) - Comprehensive comparison guide
- [`analyze_energy.py`](analyze_energy.py) - Working example script
- [`process_data.py`](process_data.py) - Advanced production script example

---

## 🎯 NEXT STEPS

1. **Modify the script** - Change calculations, add new analyses
2. **Run multiple times** - Verify consistent results
3. **Create new scripts** - Practice script-based development
4. **Convert notebook code** - Transform exploration into scripts
5. **Build automation** - Schedule scripts to run regularly

---

### Professional Impact

> **"Scripts are the bridge between experimentation and production."**

This milestone establishes critical skills:
- Writing reproducible analysis code
- Understanding execution models
- Choosing appropriate tools for tasks
- Building automation-ready workflows
- Professional development practices

Mastering both scripts and notebooks makes you a more versatile and employable Data Scientist.

---

# 1️⃣5️⃣ MILESTONE 7 – UNDERSTANDING PYTHON DATA TYPES (NUMERIC & STRING)

## 🎯 Objective

Master Python's core numeric and string data types, which form the foundation of all data processing and analysis. Learn to work with integers, floats, and strings correctly to prevent logical errors and write predictable, reliable code.

## ✅ Status: Complete

This milestone demonstrates comprehensive understanding of Python's fundamental data types through an interactive learning script with practical examples and clear explanations.

---

## 🚀 PRACTICAL DEMONSTRATION

### Files Created for This Milestone

| File/Folder | Purpose | Status |
|-------------|---------|--------|
| [`learn_data_types.py`](learn_data_types.py) | **Comprehensive tutorial** on numeric and string types | ✅ Created |

### Running the Tutorial

Execute the learning script:

```bash
python learn_data_types.py
```

**What it teaches:**
1. ✅ Integer data type and operations
2. ✅ Floating-point data type and operations
3. ✅ String data type and methods
4. ✅ Type inspection with type()
5. ✅ Common errors when mixing types
6. ✅ Type conversion (casting)
7. ✅ Safe ways to combine different types
8. ✅ Practical data analysis example

---

## 📊 KEY CONCEPTS COVERED

### 1. NUMERIC DATA TYPES

#### Integers (int)
- Whole numbers without decimal points
- Examples: `5`, `-3`, `0`, `1000`
- Operations: `+`, `-`, `*`, `/`, `//`, `%`, `**`

```python
age = 25
count = -5
result = 10 + 3  # 13
```

#### Floating-Point Numbers (float)
- Numbers with decimal points
- Examples: `3.14`, `19.99`, `-0.5`, `2.0`
- Result of any division operation

```python
price = 19.99
temperature = 22.5
result = 10 / 2  # 5.0 (always a float!)
```

### 2. STRING DATA TYPE

#### Strings (str)
- Text data enclosed in quotes (single or double)
- Examples: `"Hello"`, `'Python'`, `"CUST001"`
- Operations: concatenation, repetition, slicing

```python
name = "Alice"
product_id = "PROD-123"
full_name = "John" + " " + "Doe"  # "John Doe"
repeated = "Data" * 3  # "DataDataData"
```

### 3. TYPE INSPECTION

```python
type(42)        # <class 'int'>
type(3.14)      # <class 'float'>
type("Hello")   # <class 'str'>
type(10 / 2)    # <class 'float'> - Important!
```

### 4. TYPE CONVERSION (CASTING)

```python
# String to number
num_str = "100"
num_int = int(num_str)      # 100 (integer)
num_float = float(num_str)  # 100.0 (float)

# Number to string
price = 29.99
price_str = str(price)  # "29.99" (string)
```

---

## ⚠️ COMMON ERRORS AND SOLUTIONS

### Error 1: Mixing Numbers and Strings

```python
# ❌ WRONG - This causes an error
age = 25
message = "I am " + age + " years old"
# TypeError: can only concatenate str (not "int") to str

# ✅ CORRECT - Convert number to string
message = "I am " + str(age) + " years old"

# ✅ BETTER - Use f-strings
message = f"I am {age} years old"
```

### Error 2: Division Always Returns Float

```python
result = 10 / 2  # 5.0 (not 5)
type(result)     # <class 'float'>

# Use integer division if you need an integer
result = 10 // 2  # 5 (integer)
```

### Error 3: String Numbers Are Not Numbers

```python
num_str = "25"
result = num_str + 5  # ❌ Error!

# Convert first
result = int(num_str) + 5  # ✅ 30
```

---

## ✅ MILESTONE COMPLETION CHECKLIST

| Task | Completed |
|------|-----------|
| Understand integer data type | ✅ Yes |
| Understand float data type | ✅ Yes |
| Understand string data type | ✅ Yes |
| Perform arithmetic operations | ✅ Yes |
| Perform string operations | ✅ Yes |
| Use type() to inspect types | ✅ Yes |
| Identify type mismatch errors | ✅ Yes |
| Convert between types | ✅ Yes |
| Mix types safely in output | ✅ Yes |
| Apply types in data analysis | ✅ Yes |

---

## 🎓 KEY LEARNINGS

### 1. Data Type Fundamentals

| Type | Description | Example | Common Use |
|------|-------------|---------|------------|
| **int** | Whole numbers | `42`, `-5`, `0` | Counts, IDs, indices |
| **float** | Decimal numbers | `3.14`, `19.99` | Measurements, prices, percentages |
| **str** | Text data | `"Hello"`, `'Python'` | Labels, names, categories |

### 2. Important Rules

✅ **Division (/) always returns a float**
```python
10 / 2  # 5.0 (not 5)
```

✅ **Cannot directly mix numbers and strings**
```python
5 + "5"  # ❌ Error
```

✅ **Use type() to check variable types**
```python
type(variable)  # Shows data type
```

✅ **Use conversion functions when needed**
```python
int("100")    # String to integer
float("3.14") # String to float
str(42)       # Number to string
```

### 3. Safe Mixing with F-Strings

```python
quantity = 5
item = "apples"
price = 1.50

# Best practice: f-strings
message = f"I bought {quantity} {item} for ${price} each."
```

---

## 💡 PRACTICAL DATA ANALYSIS APPLICATION

The tutorial includes a complete energy consumption analysis example:

```python
customer_id = "CUST001"           # String
consumption_kwh = 150.5           # Float
cost_per_kwh = 0.12               # Float
days = 30                         # Integer

total_cost = consumption_kwh * cost_per_kwh      # Float calculation
daily_average = consumption_kwh / days           # Float calculation

report = f"""
Energy Usage Report
-------------------
Customer: {customer_id}
Period: {days} days
Total Consumption: {consumption_kwh} kWh
Average Daily Consumption: {daily_average:.2f} kWh
Total Cost: ${total_cost:.2f}
"""
```

---

## 📚 SCRIPT SECTIONS

The tutorial script is organized into 9 comprehensive sections:

1. **Integer Data Type** - Understanding whole numbers
2. **Floating-Point Data Type** - Understanding decimals
3. **String Data Type** - Understanding text
4. **Inspecting Data Types** - Using type() function
5. **Mixing Numbers and Strings** - Common errors
6. **Type Conversion** - Casting between types
7. **Mixing Types Safely** - Correct approaches
8. **Practical Data Analysis** - Real-world example
9. **Key Takeaways** - Summary of important rules

---

## 🔧 HOW TO USE THIS TUTORIAL

### Run the Complete Tutorial
```bash
python learn_data_types.py
```

### Expected Output
- Demonstrates all numeric operations
- Shows string manipulation techniques
- Displays type inspection results
- Demonstrates error handling
- Provides practical examples
- Includes formatted reports

---

## 🎯 NEXT STEPS

1. **Experiment** - Modify values in the script and observe results
2. **Practice** - Create your own examples with different data types
3. **Apply** - Use correct types in your analysis scripts
4. **Debug** - When errors occur, check types first
5. **Build habits** - Always be aware of variable types

---

## 💼 PROFESSIONAL IMPACT

> **"Understanding data types is the foundation of writing correct code."**

This milestone establishes critical skills:
- **Preventing logic errors** - Type awareness prevents bugs
- **Writing clear code** - Intentional type use improves readability
- **Debugging faster** - Know where type errors come from
- **Data analysis accuracy** - Correct types = correct calculations
- **Professional confidence** - Foundation for advanced topics

Type-related errors are among the most common for beginners. Mastering this fundamentals prevents countless hours of debugging and ensures your analysis is mathematically correct.

---

# 1️⃣6️⃣ MILESTONE 8 – PYTHON COLLECTIONS (LISTS, TUPLES, DICTIONARIES)

## 🎯 Objective

Master Python's three core collection data structures: lists, tuples, and dictionaries. Learn to store, organize, and manipulate multiple values efficiently, which is essential for handling real-world data. Understand when to use each structure based on mutability and access patterns.

## ✅ Status: Complete

This milestone demonstrates comprehensive understanding of Python's collection types through an interactive learning script with practical examples and clear comparisons.

---

## 🚀 PRACTICAL DEMONSTRATION

### Files Created for This Milestone

| File/Folder | Purpose | Status |
|-------------|---------|--------|
| [`learn_collections.py`](learn_collections.py) | **Comprehensive tutorial** on lists, tuples, and dictionaries | ✅ Created |
| [`VIDEO_GUIDE_COLLECTIONS.md`](VIDEO_GUIDE_COLLECTIONS.md) | **Video walkthrough guide** with timing and script | ✅ Created |

### Running the Tutorial

Execute the learning script:

```bash
python learn_collections.py
```

**What it teaches:**
1. ✅ Creating and using lists (mutable, ordered collections)
2. ✅ Accessing and modifying list elements
3. ✅ Creating and using tuples (immutable, ordered collections)
4. ✅ Understanding tuple immutability
5. ✅ Creating and using dictionaries (key-value pairs)
6. ✅ Accessing and modifying dictionary data
7. ✅ Choosing the right data structure for the task
8. ✅ Practical energy analytics examples

---

## 📊 KEY CONCEPTS COVERED

### 1. LISTS - Ordered and Mutable Collections

#### What Are Lists?
- Ordered collections enclosed in square brackets `[]`
- **Mutable** - can be changed after creation
- Accessed by numerical index (0-based)
- Allow duplicate values

```python
# Creating lists
customers = ["Alice", "Bob", "Charlie", "Diana"]
consumption = [120.5, 135.2, 98.7, 142.0]
mixed = [100, "Active", 45.5, True]

# Accessing elements
first = customers[0]      # "Alice"
last = customers[-1]      # "Diana"

# Modifying lists
customers[1] = "Robert"           # Change element
customers.append("Eve")           # Add to end
customers.insert(2, "Frank")      # Insert at position
customers.remove("Charlie")       # Remove specific value
removed = customers.pop()         # Remove and return last

# List operations
length = len(customers)
total = sum([1, 2, 3, 4, 5])
maximum = max([10, 20, 30])
```

#### When to Use Lists
✅ Need an ordered sequence  
✅ Data will change (add/remove/modify)  
✅ Building dynamic collections  
✅ Order matters  

**Examples:** Daily readings, task queues, customer orders

---

### 2. TUPLES - Ordered and Immutable Collections

#### What Are Tuples?
- Ordered collections enclosed in parentheses `()`
- **Immutable** - cannot be changed after creation
- Accessed by numerical index (0-based)
- Protect data from accidental modification

```python
# Creating tuples
location = (40.7128, -74.0060)
customer_record = ("CUST001", "Alice Johnson", 35, "Premium")
single_element = (42,)  # Note the comma!

# Accessing elements
customer_id = customer_record[0]   # "CUST001"
name = customer_record[1]          # "Alice Johnson"

# Attempting to modify (causes error)
location[0] = 50.0  # ❌ TypeError: tuples are immutable

# Tuple unpacking
x, y = location  # x=40.7128, y=-74.0060

# Tuple operations
length = len(location)
count = (1, 2, 2, 3).count(2)  # 2
```

#### When to Use Tuples
✅ Data should NOT change  
✅ Protect from accidental modification  
✅ Use as dictionary keys  
✅ Return multiple values from functions  

**Examples:** Coordinates, RGB colors, database records, configuration

---

### 3. DICTIONARIES - Key-Value Pairs

#### What Are Dictionaries?
- Collections of key-value pairs enclosed in curly braces `{}`
- **Mutable** - can be changed after creation
- Accessed by meaningful keys (not numeric index)
- Keys must be unique

```python
# Creating dictionaries
customer = {
    "id": "CUST001",
    "name": "Alice Johnson",
    "age": 35,
    "membership": "Premium"
}

# Accessing values
name = customer["name"]              # "Alice Johnson"
email = customer.get("email", "N/A") # Safe access with default

# Modifying dictionaries
customer["age"] = 36                 # Update value
customer["email"] = "alice@ex.com"  # Add new key-value
removed = customer.pop("age")        # Remove key-value
del customer["membership"]           # Delete key-value

# Dictionary methods
keys = customer.keys()       # All keys
values = customer.values()   # All values
items = customer.items()     # Key-value pairs

# Iterating
for key, value in customer.items():
    print(f"{key}: {value}")
```

#### When to Use Dictionaries
✅ Key-value relationships  
✅ Need to look up by meaningful names  
✅ Model real-world entities with attributes  
✅ Fast lookups by key  

**Examples:** Customer profiles, configuration settings, API responses

---

## 📋 COMPARISON SUMMARY

| Feature | List `[]` | Tuple `()` | Dictionary `{}` |
|---------|-----------|------------|-----------------|
| **Ordered** | ✅ Yes | ✅ Yes | No (Python 3.7+ maintains insertion order) |
| **Mutable** | ✅ Yes | ❌ No | ✅ Yes |
| **Access** | By index (0, 1, 2...) | By index (0, 1, 2...) | By key (name, id...) |
| **Duplicates** | ✅ Allowed | ✅ Allowed | Keys must be unique |
| **Use Case** | Dynamic sequences | Fixed records | Named attributes |

---

## ⚡ PRACTICAL EXAMPLES

### Example 1: Energy Data Collections

```python
# List - daily readings that change
daily_consumption = [125.5, 130.2, 118.7, 145.0, 122.3, 135.8, 128.9]
daily_consumption.append(140.2)  # Add new reading

# Tuple - fixed meter information
meter_info = ("METER-001", "Industrial", "Building A")
# meter_info[0] = "METER-002"  # ❌ Error - can't change

# Dictionary - customer profile with named fields
customer = {
    "id": "CUST001",
    "name": "TechCorp Industries",
    "meter_id": meter_info[0],
    "daily_readings": daily_consumption
}

# Access and analyze
total = sum(customer["daily_readings"])
average = total / len(customer["daily_readings"])
print(f"Customer: {customer['name']}")
print(f"Average consumption: {average:.2f} kWh")
```

### Example 2: Nested Structures

```python
# Database of customers (dictionary of dictionaries)
customers_db = {
    "CUST001": {
        "name": "Alice Johnson",
        "consumption": 150.5,
        "tier": "Premium"
    },
    "CUST002": {
        "name": "Bob Smith",
        "consumption": 120.3,
        "tier": "Standard"
    }
}

# Access nested data
customer_name = customers_db["CUST001"]["name"]
consumption = customers_db["CUST001"]["consumption"]
```

---

## ✅ MILESTONE COMPLETION CHECKLIST

| Task | Completed |
|------|-----------|
| Create lists with multiple values | ✅ Yes |
| Access list elements by index | ✅ Yes |
| Modify, add, and remove list elements | ✅ Yes |
| Create tuples with fixed values | ✅ Yes |
| Access tuple elements by index | ✅ Yes |
| Observe tuple immutability behavior | ✅ Yes |
| Create dictionaries with key-value pairs | ✅ Yes |
| Access dictionary values using keys | ✅ Yes |
| Modify and add dictionary entries | ✅ Yes |
| Understand when to use each structure | ✅ Yes |
| Apply collections to practical examples | ✅ Yes |

---

## 🎓 KEY LEARNINGS

### Decision Framework: Which Collection to Use?

**Choose LISTS when:**
- You need an ordered sequence
- Elements will be added, removed, or changed
- Accessing by numerical position makes sense
- Example: `daily_temperatures = [22.5, 23.1, 21.8, 24.0]`

**Choose TUPLES when:**
- Data should never change
- You want to protect from accidental modification
- Need to use as dictionary keys
- Example: `coordinates = (40.7128, -74.0060)`

**Choose DICTIONARIES when:**
- You need to look up values by meaningful names
- Modeling real-world entities with properties
- Key-value relationships are natural
- Example: `customer = {"id": "C001", "name": "Alice", "age": 35}`

---

## ⚠️ COMMON MISTAKES TO AVOID

### Mistake 1: Trying to Modify Tuples
```python
location = (10, 20)
location[0] = 30  # ❌ TypeError
```

### Mistake 2: Using Lists as Dictionary Keys
```python
my_dict = {[1, 2]: "value"}  # ❌ TypeError: unhashable type
# Use tuple instead:
my_dict = {(1, 2): "value"}  # ✅ Works
```

### Mistake 3: Unsafe Dictionary Access
```python
customer = {"name": "Alice"}
email = customer["email"]  # ❌ KeyError if key doesn't exist

# Use get() for safety:
email = customer.get("email", "Not provided")  # ✅ Returns default
```

---

## 🎬 VIDEO WALKTHROUGH REQUIREMENTS

Your 2-minute video must demonstrate:

### Required Content (use VIDEO_GUIDE_COLLECTIONS.md):
1. **Lists** (40 seconds)
   - Creating a list
   - Accessing elements
   - Modifying elements (append, remove, change)
   - Explain mutability

2. **Tuples** (35 seconds)
   - Creating a tuple
   - Accessing elements
   - Attempting to modify (show the error!)
   - Explain immutability and when to use

3. **Dictionaries** (35 seconds)
   - Creating a dictionary with key-value pairs
   - Accessing values by key
   - Modifying and adding key-value pairs
   - Explain use cases

4. **Comparison** (10 seconds)
   - Quick summary of differences
   - When to use each structure

### Technical Requirements:
- ✅ Screen capture showing `learn_collections.py`
- ✅ Clear audio explanation
- ✅ Run code to show actual output
- ✅ Demonstrate the error when modifying a tuple
- ✅ Show the comparison table

---

## 🔧 HOW TO USE THIS TUTORIAL

### Run the Complete Tutorial
```bash
python learn_collections.py
```

### Study the Video Guide
```bash
# Open the video guide for detailed instructions
VIDEO_GUIDE_COLLECTIONS.md
```

### Expected Output
- Demonstrates all list operations
- Shows tuple immutability with error example
- Displays dictionary access patterns
- Includes practical energy analytics examples
- Provides clear comparison table
- Shows nested structure usage

---

## 🎯 NEXT STEPS

1. **Run the script** - Execute `learn_collections.py` and study the output
2. **Experiment** - Modify examples to test your understanding
3. **Practice** - Create your own collections for different scenarios
4. **Prepare video** - Follow VIDEO_GUIDE_COLLECTIONS.md
5. **Record walkthrough** - ~2 minutes demonstrating all three structures
6. **Submit** - Pull request + video link as instructed

---

## 💼 PROFESSIONAL IMPACT

> **"Choosing the right data structure is fundamental to writing efficient, maintainable code."**

This milestone establishes critical skills:
- **Logical data organization** - Structure matches purpose
- **Code safety** - Immutability prevents bugs
- **Efficient access** - Right structure = better performance
- **Professional habits** - Industry-standard patterns

Understanding collections is essential for all data work, from simple scripts to complex analytics pipelines.

---

# 1️⃣7️⃣ SUBMISSION GUIDELINES

**General Requirements:**

Video must demonstrate:

- Terminal launch  
- Interface walkthrough  
- Folder navigation  
- Notebook creation  
- Cell execution  
- Markdown cell creation and formatting
- Switching between cell types

**Milestone 4 Video Requirements:**
- Creating Markdown cells
- Writing headings and lists
- Using inline code and code blocks
- Combining Markdown and Code cells
- Explaining why documentation matters

Duration: ~2 minutes

**Milestone 8 Video Requirements:**
- List operations and mutability
- Tuple immutability demonstration (show the error)
- Dictionary key-value access
- Explanation of when to use each structure

Duration: ~2 minutes (follow VIDEO_GUIDE_COLLECTIONS.md)  

---

# 1️⃣8️⃣ PROFESSIONAL BEST PRACTICES

- Always activate correct environment  
- Confirm Python version before work  
- Keep notebooks inside project directory  
- Use consistent environment across team  
- Document setup clearly  
- Restart kernel before final submission  
- Run all cells in order to verify reproducibility  
- **Use Markdown to explain code intent and results**
- **Structure notebooks with clear headings**
- **Interpret outputs, don't just display them**
- **Use appropriate data structures** - lists, tuples, or dictionaries
- **Protect data with tuples** - immutability prevents bugs
- **Use dictionaries for named data** - improves code readability

---

# 1️⃣9️⃣ WHY ENVIRONMENT VERIFICATION MATTERS

Prevents:

- Package conflicts  
- Kernel mismatches  
- Collaboration inconsistencies  
- Reproducibility failures  

Enables:

- Stable workflow  
- Faster debugging  
- Clean project structure  
- Professional development standards  

---

# 2️⃣0️⃣ FINAL STATUS SUMMARY

## Milestone 1 – Environment Setup
✅ COMPLETE  
Python, Jupyter, and Anaconda installed and verified

## Milestone 2 – Jupyter Navigation
✅ COMPLETE  
Notebook interface mastered, cells executed successfully

## Milestone 3 – Kernel Management
✅ COMPLETE  
Kernel operations (run, restart, interrupt) demonstrated

## Milestone 4 – Markdown Documentation
✅ COMPLETE  
Professional notebook formatting with headings, lists, and code blocks

## Milestone 5 – Data Organization
✅ COMPLETE  
Raw, processed, and output data properly separated with working demonstration

## Milestone 6 – Python Scripts for Data Analysis
✅ COMPLETE  
First Python script created, executed successfully, scripts vs notebooks understood

## Milestone 7 – Python Data Types (Numeric & String)
✅ COMPLETE  
Integer, float, and string types mastered with type conversion and safe mixing

## Milestone 8 – Python Collections (Lists, Tuples, Dictionaries)
✅ COMPLETE  
Lists, tuples, and dictionaries mastered with understanding of mutability and appropriate use cases

---

# 🚀 SPRINT STATUS

✅ **Environment stable** – All tools installed and operational  
✅ **Documentation complete** – Professional standards implemented  
✅ **Kernel management mastered** – Full control of notebook execution  
✅ **Markdown proficiency** – Clear communication in notebooks  
✅ **Data organization discipline** – Proper separation of data stages  
✅ **Script development competency** – Reproducible analysis workflows created  
✅ **Data types mastery** – Foundation for accurate data processing established  
✅ **Collections proficiency** – Lists, tuples, and dictionaries used appropriately  

**Status: PRODUCTION-READY**

All foundational skills acquired. Ready for advanced Data Science work including:
- Exploratory Data Analysis (EDA)
- Statistical modeling
- Machine learning pipelines
- Professional reporting and visualization  

