import os
import subprocess
from pathlib import Path

def find_file_upwards(start_path, target):
    current = Path(start_path).resolve()
    while current != current.parent:
        candidate = current / target
        if candidate.exists():
            return candidate
        current = current.parent
    return None

def activate_venv(venv_path):
    scripts = Path(venv_path) / "Scripts" / "activate.bat"
    if scripts.exists():
        return str(scripts)
    return None

if __name__ == "__main__":
    root = Path.cwd()
    reqs = find_file_upwards(root, "requirements.txt")

    if not reqs:
        print("❌ Could not locate requirements.txt. Start inside or below /backend_flask.")
        exit(1)

    venv_dir = reqs.parent / "venv"
    if not venv_dir.exists():
        print("⚙️ Creating virtual environment...")
        subprocess.run(["python", "-m", "venv", str(venv_dir)])

    pip_path = venv_dir / "Scripts" / "pip.exe"
    if not pip_path.exists():
        print("❌ Could not locate pip in the virtual environment.")
        exit(1)

    print(f"📦 Installing requirements from: {reqs}")
    subprocess.run([str(pip_path), "install", "-r", str(reqs)])
    print("✅ Dependencies installed successfully.")

{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Install Python Dependencies",
      "type": "shell",
      "command": "python invoke_deps.py",
      "presentation": {
        "reveal": "always"
      },
      "problemMatcher": []
    },
    {
      "label": "Prep & Ignite All",
      "dependsOn": [
        "Install Python Deps (Auto-Locate)",
        "Run Flask Backend",
        "Run Node Bridge",
        "Run Frontend"
      ],
      "dependsOrder": "sequence"
    }
  ]
}