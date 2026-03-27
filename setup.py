import os
import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

def main():
    print("--- Starting Project Setup ---")

    # 1. Create virtual environment
    if not os.path.exists("venv"):
        print("Creating virtual environment...")
        run_command(f"{sys.executable} -m venv venv")
    else:
        print("Venv already exists, skipping...")

    # 2. Install requirements
    # We use the pip from the newly created venv
    pip_path = os.path.join("venv", "bin", "pip") if os.name != 'nt' else os.path.join("venv", "Scripts", "pip")
    
    if os.path.exists("requirements.txt"):
        print("Installing dependencies...")
        run_command(f"{pip_path} install --upgrade pip")
        run_command(f"{pip_path} install -r requirements.txt")
    else:
        print("requirements.txt not found. Skipping installation.")

    print("\nSetup finished successfully!")
    print("To activate the environment run:")
    print("source venv/bin/activate")

if __name__ == "__main__":
    main()
