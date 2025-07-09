# sn0wflake

**sn0wflake** is a demonstration project for a Trojan horse backdoor, designed for educational and research purposes only. This project shows how a backdoor agent can use GitHub as a Command & Control (C2) channel by leveraging issues and pull requests.

> **:warning: WARNING:**  
> This code is for demonstration, research, and educational use only.  
> Running, distributing, or deploying malware without explicit authorization is illegal and unethical.

---

## Features

- **GitHub C2:** Uses GitHub pull requests and comments for agent control and exfiltration.
- **Persistence Options:** Attempts to add persistence on compromised host.
- **Command Execution:** Receives and executes commands from GitHub comments.
- **Self-destruction:** Can remove itself from the host on command.
- **Agent Identification:** Each agent is uniquely identified and reports OS, IP, hostname, and user info.

---

## Usage

### 1. Running the Demo Agent

This project uses the [`uv`](https://github.com/astral-sh/uv) Python runner for convenience. There is no need to set up a virtual environment or install requirements manually.

```sh
uv run main.py
```

- Edit `main.py` to set your `{TOKEN}` and `{REPO}` at the top of the file.

### 2. Building an Executable

To deploy on a target system, you must build the code into a Windows executable.  
Tools like [PyInstaller](https://pyinstaller.org/) can be used:

```sh
pyinstaller --onefile main.py
```

Then, use the generated `.exe` file for installation on the target system.

---

## How It Works

- On execution, the agent registers itself with the configured GitHub repository.
- It creates a new branch and pull request, reporting system info.
- Commands (e.g. `cmd`, `ls`, `persistent`, `selfdestruct`, `terminate`) can be issued via comments on the PR.
- The agent polls for comments, executes commands, and replies with results.

### Supported Commands

- `ls` - List available agents
- `cmd <command>` - Run a shell command on the target system
- `persistent` - Attempt to add startup persistence
- `terminate` - Stop the agent process
- `selfdestruct` - Remove the agent from the system
- `help` - Show command usage help

---

## Disclaimer

This project is provided **for educational and authorized testing purposes only**.  
**Do not use this code on networks or systems that you do not have explicit permission to test.**

---

## License

[MIT](LICENSE)