# Python Scripts vs Notebooks: Understanding the Differences

## Overview
This document explains when to use Python scripts (.py files) versus Jupyter notebooks (.ipynb files) for data analysis tasks.

---

## What is a Python Script?

A Python script is a plain text file with a `.py` extension containing Python code that executes from top to bottom in a single run.

**Example:** `analyze_energy.py`

### Characteristics of Scripts:
- **Sequential execution**: Code runs from line 1 to the last line
- **No persistent state**: Variables don't persist between runs
- **Automated**: Can be scheduled, run in pipelines, or integrated into systems
- **Version control friendly**: Easy to track changes in Git
- **Reproducible**: Same input always produces same output

---

## What is a Jupyter Notebook?

A Jupyter notebook is an interactive document that combines code, visualizations, and narrative text in cells.

**Example:** `Untitled.ipynb`

### Characteristics of Notebooks:
- **Cell-based execution**: Run cells individually in any order
- **Persistent state**: Variables remain in memory between cell executions
- **Interactive**: Great for exploration and experimentation
- **Rich output**: Supports plots, tables, markdown, and HTML
- **Narrative-driven**: Combines code with explanations

---

## When to Use Scripts

Use Python scripts when you need:

### ✅ **Automation**
- Running analysis on a schedule (daily, weekly)
- Processing data in batch jobs
- Integrating with CI/CD pipelines

### ✅ **Reproducibility**
- Ensuring consistent results every time
- Sharing code that "just works"
- Deploys to production environments

### ✅ **Reusability**
- Creating functions/modules used by multiple projects
- Building command-line tools
- Writing utility functions

### ✅ **Version Control**
- Tracking changes clearly in Git
- Code reviews and collaboration
- Merging changes from multiple developers

### Example Use Cases:
- Data cleaning pipelines
- Automated report generation
- Model training workflows
- ETL (Extract, Transform, Load) processes

---

## When to Use Notebooks

Use Jupyter notebooks when you need:

### ✅ **Exploration**
- Investigating new datasets
- Trying different visualizations
- Testing hypotheses interactively

### ✅ **Communication**
- Presenting results to stakeholders
- Creating tutorials or documentation
- Combining analysis with narrative

### ✅ **Prototyping**
- Developing new analysis approaches
- Experimenting with models
- Quick iterations and feedback

### ✅ **Teaching**
- Demonstrating concepts step-by-step
- Interactive learning materials
- Workshop sessions

### Example Use Cases:
- Exploratory Data Analysis (EDA)
- Research and experiments
- Data visualization dashboards
- Tutorial materials

---

## Real-World Workflow

A typical Data Science workflow combines both:

```
1. START: Notebook (exploratory/analysis/)
   ↓ Explore data, try approaches
   
2. REFINE: Notebook → Script
   ↓ Convert working code to functions
   
3. PRODUCTION: Script (process_data.py)
   ↓ Run automatically, reproducibly
   
4. COMMUNICATE: Notebook (reports/)
   ↓ Present findings with visualizations
```

---

## Key Differences Summary

| Aspect | Python Script | Jupyter Notebook |
|--------|--------------|------------------|
| **File Extension** | `.py` | `.ipynb` |
| **Execution** | Top to bottom, all at once | Cell by cell, any order |
| **State** | No persistent state | Persistent state in kernel |
| **Best For** | Automation, production | Exploration, presentation |
| **Version Control** | Git-friendly | Harder to diff/merge |
| **Interactivity** | None (run and finish) | High (iterative) |
| **Output** | Console/files | Inline in document |
| **Debugging** | Standard debuggers | Cell-level inspection |

---

## Common Mistakes to Avoid

### ❌ **Using Notebooks for Production**
- Notebooks can run cells out of order
- Hidden state makes debugging difficult
- Not suitable for scheduled jobs

### ❌ **Using Scripts for Initial Exploration**
- Scripts require re-running entire code for each change
- No inline visualizations
- Slower iteration cycle

### ❌ **Treating Scripts Like Notebooks**
- Don't expect variables to persist
- Can't run "parts" of a script easily
- Need proper error handling

---

## How to Run Each

### Running a Python Script:
```bash
# From command line/terminal
python analyze_energy.py

# Or with full path
python "path/to/analyze_energy.py"

# With arguments
python analyze_energy.py --input data.csv
```

### Running a Jupyter Notebook:
```bash
# Start Jupyter server
jupyter notebook

# Or Jupyter Lab
jupyter lab

# Then interact in browser
```

---

## Best Practices

### For Scripts:
1. ✅ Add docstrings explaining purpose
2. ✅ Include print statements for progress
3. ✅ Handle errors gracefully
4. ✅ Use functions to organize code
5. ✅ Add command-line arguments if needed

### For Notebooks:
1. ✅ Run "Restart & Run All" before sharing
2. ✅ Clear cell outputs before committing to Git
3. ✅ Add markdown cells to explain steps
4. ✅ Name cells with clear headings
5. ✅ Keep notebooks focused on one topic

---

## Transitioning from Notebook to Script

When your notebook code is ready for production:

1. **Extract working code** from notebook cells
2. **Organize into functions** with clear purposes
3. **Add proper error handling**
4. **Remove interactive elements** (widgets, etc.)
5. **Add logging/print statements** for tracking
6. **Test thoroughly** with different inputs
7. **Document** with comments and docstrings

---

## Conclusion

Both Python scripts and Jupyter notebooks are essential tools in Data Science:

- **Scripts** = Production, automation, reproducibility
- **Notebooks** = Exploration, communication, learning

Master both to become an effective Data Scientist!

---

**Next Steps:**
1. Practice running `analyze_energy.py` multiple times
2. Modify the script and observe consistent behavior
3. Create a notebook for exploratory analysis
4. Convert notebook findings into a script
