# Welcome to Your First Coding Project

This is a simple project to help you get started with Python using your preferred IDE: VSCode, Cursor, or Antigravity.  
You'll write your very first scripts here, while your AI assistant acts as your tutor and guide.  
Let's explore this workspace together:

> 💡 **Learning Tip:**
> You don't need to understand everything at once.
> Focus on getting things to work first — understanding comes with practice.

---

## 📋 Table of Contents

1. [Getting Started](#getting-started)
   - [IDE Setup](docs/ide_setup.md)
   - [Get the Project](docs/get_the_project.md)
   - [Getting to Know Your IDE](docs/getting_to_know_your_ide.md)
2. [How to](#how-to)
   - [Use the Terminal](#use-the-terminal)
   - [Activate Your Environment](#activate-your-environment)
   - [Run Code](#run-code)
   - [Using Libraries](#using-libraries)
   - [Working with Secrets](#working-with-secrets-api-keys-passwords)
3. [Start Coding](#start-coding)

&nbsp;

## Getting Started

Let’s get a few things set up to get you started. No worries — you’ll find step-by-step guides for both Windows and Mac in the links below. Follow them in order:

### [IDE Setup](docs/ide_setup.md) 

> Install Python and Git, choose your IDE, and follow the setup guide for your system.


### [Get the Project](docs/get_the_project.md)

> Bring the code onto your machine: download or clone the project onto your computer.

### [Getting to Know Your IDE](docs/getting_to_know_your_ide.md)

> Learn your way around the IDE layout and project files.

&nbsp;

## How to

### Use the Terminal

The terminal is where you talk to your computer — and where your code actually runs.
If this feels unfamiliar, that's normal — you'll get used to it quickly.

#### Opening the Terminal

**In your IDE:** Go to the menu bar and select **Terminal → New Terminal**. A panel will open at the bottom of the screen.

**Outside your IDE:**

- **田 Windows:** Search for **PowerShell** in the Start menu.
- ** Mac:** Search for **Terminal** in Spotlight (`⌘` + `Space`, then type "Terminal").

#### Essential Commands

Here are a few commands you'll use all the time:

| Command | What it does | Example |
|---------|-------------|---------|
| `pwd` | Show your current folder | `pwd` |
| `ls` | List files in the current folder | `ls` |
| `cd` | Move into a folder | `cd session-1` |
| `cd ..` | Go up one folder | `cd ..` |
| `python` | Run a Python file | `python main.py` |
| `clear` | Clear the terminal screen | `clear` |

&nbsp;
> **💡 Note:** On Mac/Linux, the Python command may be `python3` instead of `python`.

> **💡 Tips:** Press **`⇥ Tab`** to autocomplete folder and file names (e.g. `python sess` + `⇥ Tab` → `python session-1/`). Press the **`↑ Up arrow`** to repeat your last command.

&nbsp;

#### Reading Error Messages

When something goes wrong, Python prints an error in the terminal. Don't panic — errors are normal and helpful! Ask your AI assistant: **"I got this error, what does it mean?"** and paste the message. Make sure you understand the explanation.

---

### Activate Your Environment

**Good news** — your Python environment is already prepared for you. 🎉

When you open a terminal, you might see `(.venv)` at the start of the prompt, like this:

```sh
(.venv) vibecoding-02-03-68307615:$
```

If you see `(.venv)`, everything is ready to go. Skip to [Run Code](#run-code).

&nbsp;

If you don't see it, no problem — just run the command below.

**田 Windows:**

```powershell
.\.venv\Scripts\Activate.ps1
```

** Mac:**

```bash
source .venv/bin/activate
```

&nbsp;

#### First Time Setup

Starting from scratch? Follow the full setup guide below:

- **[田 Windows Setup Guide](docs/setup_windows.md)** - Complete instructions including Python installation
- **[ Mac Setup Guide](docs/setup_mac.md)** - Complete instructions including Python installation

---

### Run Code

1. Make sure `main.py` is open in the editor.
2. Click into the **Terminal** at the bottom.
3. Run this command:

```bash
python main.py
```
> **💡 Note:** On Mac/Linux, the Python command may be `python3` instead of `python`.

4. You should see this message appear in the terminal:

```sh
Hello, world!
```

If you see `Hello, world!`, everything is working correctly.

🎉 Congrats, you just ran your first Python program in your IDE!

#### Running Files from Any Directory

> **Important:** The play button in your IDE does **not** use your project environment.
> To avoid confusing bugs, always run your code from the terminal.

To run a Python file from any directory:

1. **Confirm that your virtual environment is activated.**  
   You should see `(.venv)` at the start of your terminal prompt.

2. **Open the Terminal.**

3. **Run the file by providing its relative path:**

```bash
python session-1/1_01.py
```

---

### Using Libraries

This project uses a `requirements.txt` file to list the Python packages it depends on. Here's what's included:

| Package | What it does |
|---------|-------------|
| `pip` | Python's package installer — keeps itself up to date |
| `autopep8` | Automatically formats your code to follow Python style guidelines |

Make sure your virtual environment is activated (you should see `(.venv)` in your terminal), then run:

```bash
pip install -r requirements.txt
```

That's it — Python takes care of the rest. You only need to do this once per environment.

> **💡 Tip:** If you ever add a new package with `pip install <package-name>`, ask your AI assistant to help you add it to `requirements.txt` so the project stays up to date.

&nbsp;

---

### Working with Secrets (API Keys, Passwords)

**Important:** Never put passwords or API keys directly in your code — even for testing.

#### Using a `.env` File

When you need to store secrets (like API keys), create a `.env` file in your project folder:

1. Right-click in the Explorer → New File → Name it `.env`
2. Add your secrets, one per line:

   ```sh
   API_KEY=your_secret_key_here
   PASSWORD=your_password_here
   ```

3. Ask your AI assistant: **"Use my API key from the .env file"**

Your AI assistant will help you load and use these secrets properly in your code.

> **💡 Tip:** Your `.env` file is already protected by `.gitignore`, so it won't be uploaded to GitHub. Your secrets stay private!

&nbsp;

#### ⚠️ Important Rules

- **Never** write secrets directly in your code
- **Always** use a `.env` file for passwords, API keys, and tokens
- **Ask your AI assistant** to help you use environment variables when you need them

&nbsp;

> 💡 **Tip:**
> If something doesn't work, don't try everything at once.
> Change one thing, run it again, and observe what happens.

&nbsp;

## Start Coding

Before running anything, take a moment to understand what the code does. Ask your AI assistant to explain `main.py` — think of it as your first walkthrough.

In the **AI Chat panel**, on the right side, type:

```text
Can you explain what the code in `main.py` does?
```

You'll get a simple, logical explanation of what the program does, not just a code breakdown.


### Keep Exploring

Once you understand `main.py`, try these follow-up prompts with your AI assistant:

- **"What would happen if I changed the message to my own name?"** — then try it!
- **"Can you show me how to make the program ask for my name and greet me?"**
- **"What is a variable? Can you show me an example in this file?"**

There are no wrong questions — use the AI as your guide.

&nbsp;

### Working Through the Sessions

This project is organized into sessions, each with small exercises to build your skills step by step:

Each session builds on the previous one — follow them in order.

```
session-1/   ← Start here
session-2/
session-3/
...
```

To run an exercise, use its path in the terminal:

```bash
python session-1/1_01.py
```

When you're ready to move on, open the next exercise file and **ask your AI assistant to guide you through it.**
