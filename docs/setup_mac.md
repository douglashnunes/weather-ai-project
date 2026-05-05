# Mac Setup

## Tools Installation

If something doesn’t work, copy the error and ask your AI assistant for help.

### Step 1: Python

> Check if Python is installed:

```bash
python3 --version
```

**If you see an error like "Python3 is not installed" or no version is shown, Python is not installed. Choose one of the options below to install it:**

#### Option 1: Homebrew

Open the terminal and run:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python3
```

&nbsp;

#### Option 2: Manual download

[Download](https://www.python.org/downloads/) and run the installer

&nbsp;

### Step 2: Git

> Check if Git is installed:

```bash
git --version
```

If you see a version number, you're good — skip to [Virtual Environment](#virtual-environment).

&nbsp;

**If Git is not installed, choose one of the options below:**

#### Option 1: Homebrew (recommended)

```bash
brew install git
```

This installs Homebrew (a package manager), then installs Python.

&nbsp;

#### Option 2: Manual download

[Download](https://git-scm.com/downloads) and run the macOS installer

&nbsp;

## Virtual Environment

This creates an isolated environment for your project.

### Create a virtual environment

> **💡 Note:** You only need to do this once.

```bash
python3 -m venv .venv
```

&nbsp;

### Activate the environment

 Run this command whenever you don’t see (.venv) in your terminal.

```bash
source .venv/bin/activate
```

&nbsp;

**Errors like "developer tools not found":**

```bash
xcode-select --install
```

&nbsp;

## Install Packages

> Install libraries (run this every time you add new packages)

```bash
pip install -r requirements.txt
```

&nbsp;

> Or just install a specific one

```bash
pip install <package_name>
```
