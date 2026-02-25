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

---

# 🟢 OVERALL STATUS: SPRINT-READY

The development environment has been successfully installed, verified, documented, and tested.  
All required components are operational and integrated correctly.

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
12. Submission Guidelines  
13. Professional Best Practices  
14. Why Verification Matters  
15. Final Status Summary  

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

# 1️⃣2️⃣ SUBMISSION GUIDELINES

Video must demonstrate:

- Terminal launch  
- Interface walkthrough  
- Folder navigation  
- Notebook creation  
- Cell execution  

Duration: 2 minutes  

---

# 1️⃣3️⃣ PROFESSIONAL BEST PRACTICES

- Always activate correct environment  
- Confirm Python version before work  
- Keep notebooks inside project directory  
- Use consistent environment across team  
- Document setup clearly  
- Restart kernel before final submission  
- Run all cells in order to verify reproducibility  

---

# 1️⃣4️⃣ WHY ENVIRONMENT VERIFICATION MATTERS

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

# 1️⃣5️⃣ FINAL STATUS SUMMARY

## Milestone 1
✅ COMPLETE  

## Milestone 2
✅ COMPLETE  

## Milestone 3
✅ COMPLETE  

---

# 🚀 SPRINT STATUS

Environment stable.  
Documentation complete.  
Kernel management mastered.  
Ready to begin Data Science work.  

