# 田 Windows Setup

## Tools Installation

If something doesn’t work, copy the error and ask your AI assistant for help.

### Step 1: Python

> Check if Python is installed:

```powershell
python --version
```

**If you see an error like "Python is not recognized" or no version is shown, Python is not installed. Choose one of the options below to install it:**

#### Option 1: Microsoft Store

1. Open the **Microsoft Store** (search for it in the Start menu)
2. Search for **Python 3.13**
3. Click **Install**

&nbsp;

#### Option 2: Install using PowerShell

```powershell
winget install Python.Python.3.13
```

&nbsp;

#### Option 3: Manual download

1. Go to <https://www.python.org/downloads/>
2. Download and run the installer
3. **Important:** Check the box "Add Python to PATH" during installation. If you skip this, Python won’t work in the terminal.

&nbsp;

### Step 2: Git

> Check if Git is installed:

```powershell
git --version
```

If you see a version number, you're good — skip to [Virtual Environment](#virtual-environment).

&nbsp;

**Don't have Git?** [Download Git](https://github.com/git-for-windows/git/releases/download/v2.52.0.windows.1/Git-2.52.0-64-bit.exe) and run the installer

> **Note:** Install with all default settings.

&nbsp;

## Virtual Environment

This creates an isolated environment for your project.

### Create a virtual environment

> **💡 Note:** You only need to do this once.

```powershell
python -m venv .venv
```

&nbsp;

### Activate the environment (every time you don't see `(.venv)` in the terminal)

```powershell
.venv\Scripts\activate
```

&nbsp;

**Errors like "running scripts is disabled on this system":**

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**For errors like "developer tools not found":**

```powershell
pip install --upgrade pip setuptools wheel
```

&nbsp;

## Install Packages

> Install libraries (run this every time you add new packages)

```powershell
pip install -r requirements.txt
```

&nbsp;

> Or just install a specific one

```powershell
pip install <package_name>
```
