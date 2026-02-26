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
13. Submission Guidelines  
14. Professional Best Practices  
15. Why Verification Matters  
16. Final Status Summary  

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

# 1️⃣5️⃣ WHY ENVIRONMENT VERIFICATION MATTERS

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

# 1️⃣3️⃣ SUBMISSION GUIDELINES

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

---

# 1️⃣4️⃣ PROFESSIONAL BEST PRACTICES

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

---

# 1️⃣5️⃣ WHY ENVIRONMENT VERIFICATION MATTERS

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

# 1️⃣6️⃣ FINAL STATUS SUMMARY

## Milestone 1
✅ COMPLETE  

## Milestone 2
✅ COMPLETE  

## Milestone 3
✅ COMPLETE  

## Milestone 4
✅ COMPLETE  

---

# 🚀 SPRINT STATUS

Environment stable.  
Documentation complete.  
Kernel management mastered.  
Markdown documentation implemented.  
Ready to begin advanced Data Science work.  

