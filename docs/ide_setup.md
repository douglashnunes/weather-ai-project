# IDE Setup

## Prerequisites

Before you start coding, make sure you have Python and Git installed.

To run the commands below, open a terminal first:

- **田 Windows:** Search for **PowerShell** in the Start menu.

- ** Mac:** Search for **Terminal** in Spotlight (`⌘` + `Space`, then type "Terminal").

  &nbsp;

### Python 3.13+

Check if Python is installed:

**田 Windows:**

```powershell
python --version
```

** Mac:**

```bash
python3 --version
```

If it's not installed, follow the Python installation steps for your system:

- 田 Windows → [Step 1: Python](setup_windows.md#step-1-python)

-  Mac → [Step 1: Python](setup_mac.md#step-1-python)

  &nbsp;

### Git

Check if Git is installed:

```bash
git --version
```

If it's not installed, follow the Git installation steps for your system:

- 田 Windows → [Step 2: Git](setup_windows.md#step-2-git)

-  Mac → [Step 2: Git](setup_mac.md#step-2-git)

  &nbsp;

## Choosing an IDE

Start with an IDE that follows a more assistive philosophy and offers less abstraction over the development process; then later begin a project with an agent and switch to an editor at different stages of development.

| Tool        | Paradigm     | Abstraction      | Assistant / Agent   | Extensions                                  |
| ----------- | ------------ | ---------------- | ------------------- | ------------------------------------------- |
| VSCode      | IDE          | Low (expandable) | extensions          | [Copilot](#github-copilot), [Claude](#claude), [Codex](#codex), [Cline](#cline-multimodel), OpenCode     |
| Cursor      | AI-first IDE | Medium–High      | Cursor | [Claude](#claude), [Codex](#codex), [Cline](#cline-multimodel), OpenCode              |
| Antigravity | Agentic IDE  | High             | Antigravity         | few options (integrates AI models directly) |

Choose one of these IDE options:

- [VSCode](https://code.visualstudio.com)
- [Cursor](https://cursor.sh)
- [Antigravity](https://antigravity.dev)

&nbsp;

> **💡 Note:** This project works with VSCode, Cursor, and Antigravity.

&nbsp;

## Installing Extensions

Once your IDE is installed, set up the extensions you need.

To install extensions in **VSCode or Cursor**: open the Extensions panel (puzzle piece icon on the left sidebar, or `Ctrl`+`Shift`+`X` / `⌘`+`Shift`+`X`) and search by name.

### Python language

- Search **Python** by Microsoft and install it


### AI extensions

> **💡 Tip:** If you have already a subscription for a Claude or OpenAI, check whether your plan includes an AI assistant and choose that extension

#### GitHub Copilot

- Search **GitHub Copilot** and install it (only in **VSCode**)


#### Claude

- Search **Claude Code for VS Code** by Anthropic and install it

#### Codex

- Search **Codex** by OpenAI and install it

#### Cline (multimodel)

- Search **Cline** and install it
- You can use several AI models with **Cline**; some are completely free. Check their [documentation](https://docs.cline.bot/getting-started/installing-cline).
- **Cline** is available for the three IDE options


&nbsp;

## Full Setup Guides

For complete step-by-step instructions including virtual environment setup:

- [田 Windows Setup Guide](setup_windows.md)
- [ Mac Setup Guide](setup_mac.md)