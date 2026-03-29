import os
import subprocess
import sys
from pathlib import Path

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(1)

def main():
    project_dir = Path(__file__).parent.absolute()
    venv_dir = project_dir / "venv"
    
    if not venv_dir.exists():
        run_command(f"{sys.executable} -m venv {venv_dir}")

    pip_path = venv_dir / "bin" / "pip"
    req_file = project_dir / "requirements.txt"
    
    if req_file.exists():
        run_command(f"{pip_path} install --upgrade pip")
        run_command(f"{pip_path} install -r {req_file}")

    bin_dir = Path.home() / ".local" / "bin"
    bin_dir.mkdir(parents=True, exist_ok=True)
    launcher_path = bin_dir / "automv"

    launcher_content = f"#!/bin/bash\n{venv_dir}/bin/python3 {project_dir}/main.py \"$@\"\n"

    with open(launcher_path, "w") as f:
        f.write(launcher_content)
    
    os.chmod(launcher_path, 0o755)

    print(f"Setup finished. Command 'automv' created in {bin_dir}")
    print("Restart your terminal or run: source ~/.bashrc")

if __name__ == "__main__":
    main()
