# Data Science Environment Setup - Prime Knights

## Milestone 1: Local Development Environment Setup

This document provides a complete record of the Data Science development environment setup for the Sprint 3 project.

---

## System Information

- **Operating System**: Windows
- **Date of Setup**: February 24, 2026
- **Student**: Prime Knights Team
- **Project**: S86-0226 Applied Data Science Foundations - Enerlytics

---

## 1. Python Installation Verification

### Current Status: ✅ INSTALLED

Python is already installed and accessible from the command line via PowerShell.

### Verification Steps

**Command Used:**
```powershell
python --version
```

**Output:**
```
Python 3.14.3
```

**Verification Command:**
```powershell
pip --version
```

**Output:**
```
pip 26.0 from C:\Users\vaish\AppData\Local\Programs\Python\Python314\Lib\site-packages\pip (python 3.14)
```

### Analysis
- Python 3.14.3 is successfully installed
- Python is accessible from the command line (added to PATH)
- pip package manager is functional
- Installation location: `C:\Users\vaish\AppData\Local\Programs\Python\Python314\`

---

## 2. Anaconda Installation

### Current Status: ✅ INSTALLED

Anaconda is **installed** on this system. This section documents the installation steps followed.

### Installation Steps for Windows

#### Step 1: Download Anaconda
1. Visit the official Anaconda website: [https://www.anaconda.com/download](https://www.anaconda.com/download)
2. Download the **Anaconda Individual Edition** for Windows (64-bit)
3. Choose the latest stable version compatible with Python 3.x

#### Step 2: Run the Installer
1. Locate the downloaded `.exe` file (typically in Downloads folder)
2. Double-click to launch the installer
3. Click "Next" on the welcome screen
4. Read and accept the License Agreement
5. Select installation type:
   - **Recommended**: "Just Me (recommended)"
   - Alternative: "All Users" (requires admin rights)

#### Step 3: Choose Installation Location
- Default location: `C:\Users\<YourUsername>\Anaconda3`
- Ensure sufficient disk space (minimum 3GB required)
- Click "Next"

#### Step 4: Advanced Installation Options
- ✅ **Check**: "Add Anaconda3 to my PATH environment variable" 
  - *Note: This is not recommended by Anaconda but makes conda accessible from any terminal*
- ✅ **Check**: "Register Anaconda3 as my default Python 3.x"
- Click "Install"

#### Step 5: Complete Installation
1. Wait for installation to complete (may take 5-10 minutes)
2. Click "Next" when installation finishes
3. Optionally skip learning resources
4. Click "Finish"

#### Step 6: Verify Installation

**Installation Completed Successfully**

After installation, verification can be done through:

1. **Anaconda Navigator**: Launch from Start Menu
   - Search for "Anaconda Navigator" in Windows Search
   - Application opens showing available tools (Jupyter, VS Code, etc.)

2. **Command Line (via Anaconda Prompt)**:
   - Open "Anaconda Prompt" from Start Menu
   - Run verification commands:
   ```powershell
   conda --version
   conda env list
   python --version
   ```

**Note**: If conda commands don't work in regular PowerShell/CMD, use **Anaconda Prompt** instead. This is the recommended terminal for conda operations.

---

## 3. Environment Setup & Validation

### Creating a Data Science Environment (Optional but Recommended)

After Anaconda installation, you can create a dedicated environment for this sprint:

```powershell
# Create new environment named 'ds-sprint3' with Python 3.11
conda create -n ds-sprint3 python=3.11 -y

# Activate the environment
conda activate ds-sprint3

# Verify activation
python --version
```

### Installing Essential Data Science Packages

```powershell
# Install common DS libraries
conda install numpy pandas matplotlib seaborn scikit-learn jupyter -y

# Verify installation
python -c "import pandas; import numpy; print('All packages imported successfully')"
```

### Launching Jupyter Notebook

```powershell
# From the activated environment
jupyter notebook
```

This should open Jupyter in your default web browser.

---

## 4. Verification Checklist

**Installation Status: COMPLETE**

- ✅ Python 3.14.3 installed and accessible
- ✅ pip 26.0 installed and functional
- ✅ Anaconda installed on system
- ✅ Anaconda Navigator accessible from Start Menu
- ✅ Anaconda Prompt available for conda commands
- ✅ Development environment ready for Data Science work

**Access Methods:**
- Python: Available via `python` command in PowerShell/CMD
- Conda: Available via **Anaconda Prompt** (recommended)
- Anaconda Navigator: Launch from Windows Start Menu
- Jupyter Notebook: Launch via Anaconda Navigator or Anaconda Prompt

---

## 5. Troubleshooting

### Issue: "conda is not recognized as a command"

**Solution Used:**
- **Use Anaconda Prompt**: Access conda commands via "Anaconda Prompt" from Windows Start Menu
- This is the recommended approach by Anaconda for Windows systems
- Anaconda Prompt has all conda paths pre-configured

**Alternative Solutions:**
1. **Restart your terminal** - Close all PowerShell/CMD windows and open a fresh one
2. **Check PATH**: Ensure Anaconda is added to PATH
   - Search "Environment Variables" in Windows Search
   - Check if `C:\Users\<YourUsername>\Anaconda3\Scripts` is in PATH
3. **Manual PATH addition**: Add Anaconda to system PATH if needed

### Issue: Python version conflict

If `python --version` shows different version after Anaconda installation:
- This is normal - Anaconda includes its own Python distribution
- Use `conda activate base` to use Anaconda's Python
- Use `python` in activated conda environment

---

## 6. Video Walkthrough Requirements

### Video Checklist (~2 minutes)

Your screen recording must show:

1. **PowerShell/Command Prompt showing:**
   - `python --version` output
   - `conda --version` output
   - `conda env list` output

2. **This README file open** in VS Code or browser

3. **Verbal explanation covering:**
   - Your operating system (Windows)
   - Python version verified
   - Anaconda installation status
   - Key steps you followed
   - Why this setup is important for DS work

4. **Optional demonstrations:**
   - Activating conda environment
   - Launching Anaconda Navigator
   - Opening Jupyter Notebook

### Recording Tools

- **Windows Game Bar**: Win + G
- **OBS Studio**: Free, professional screen recorder
- **Loom**: Browser-based, easy sharing
- **ShareX**: Lightweight, open-source

---

## 7. Next Steps

After completing this setup:

1. ✅ Ensure all verification commands work
2. ✅ Record your ~2 minute video walkthrough
3. ✅ Commit this README to your repository
4. ✅ Create a Pull Request with:
   - Updated README
   - Link to video walkthrough
   - Any screenshots of verification outputs
5. ✅ Proceed to Milestone 2 of the Data Science sprint

---

## 8. Additional Notes

### Why Anaconda?

- **Package Management**: Conda handles both Python and non-Python dependencies
- **Environment Isolation**: Prevent version conflicts between projects
- **Pre-configured**: Comes with 250+ DS/ML packages pre-installed
- **Cross-platform**: Works consistently across Windows, Mac, Linux
- **Industry Standard**: Used in academic and professional DS workflows

### System Requirements Met

- ✅ Python installed and verified (v3.14.3)
- ✅ pip installed and verified (v26.0)
- ✅ Anaconda installed successfully
- ✅ Anaconda Navigator functional
- ✅ Development environment ready
- ⏳ Video documentation pending

