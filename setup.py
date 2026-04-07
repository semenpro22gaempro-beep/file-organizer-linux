import os
import subprocess
import sys
from pathlib import Path

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Error executing command: {command}")
        sys.exit(1)

def main():
    project_dir = Path(__file__).parent.resolve()
    venv_dir = project_dir / "venv"
    python_path = venv_dir / "bin" / "python"
    pip_path = venv_dir / "bin" / "pip"
    req_file = project_dir / "requirements.txt"

    if not venv_dir.exists():
        print(f"Creating virtual environment in {venv_dir}...")
        run_command(f"'{sys.executable}' -m venv '{venv_dir}'")

    if req_file.exists():
        print("Upgrading pip and installing requirements...")
        run_command(f"'{pip_path}' install --upgrade pip")
        run_command(f"'{pip_path}' install -r '{req_file}'")

    bin_dir = Path.home() / ".local" / "bin"
    bin_dir.mkdir(parents=True, exist_ok=True)

    launcher_path = bin_dir / "org"
    launcher_content = f'#!/bin/sh\nexec "{python_path}" "{project_dir}/main.py" "$@"\n'

    with open(launcher_path, "w") as f:
        f.write(launcher_content)
    os.chmod(launcher_path, 0o755)

    shell_configs = [
        (Path.home() / ".bashrc", 'export PATH="$HOME/.local/bin:$PATH"'),
        (Path.home() / ".zshrc", 'export PATH="$HOME/.local/bin:$PATH"'),
        (Path.home() / ".config/fish/config.fish", 'set -gx PATH $HOME/.local/bin $PATH')
    ]

    for config_path, export_cmd in shell_configs:
        if config_path.parent.exists():
            content = ""
            if config_path.exists():
                with open(config_path, "r") as f:
                    content = f.read()

            if export_cmd not in content:
                print(f"Adding ~/.local/bin to your PATH in {config_path.name}...")
                with open(config_path, "a") as f:
                    f.write(f"\n# Added by setup script\n{export_cmd}\n")

    print(f"\nSetup finished. Command 'org' is ready.")
    print("-" * 40)
    print("To apply changes, restart your terminal or run:")
    print("source ~/.bashrc  # (for Bash)")
    print("source ~/.zshrc   # (for Zsh)")
    print("-" * 40)

if __name__ == "__main__":
    main()
