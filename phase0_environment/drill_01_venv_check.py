"""
Drill 0.1: Virtual Environment Check

Goal:
    Verify you're working inside a virtual environment

Task:
    Write a script that checks if a virtual environment is active

Rules:
    - Write the solution yourself
    - Keep it readable
    - Add at least 2 test cases

Reflection:
    Why should every Python project have its own virtual environment?
"""

import sys


# === Your Code Here ===


def is_venv_active():
    """
    Check if running inside a virtual environment.
    Returns True if in venv, False otherwise.
    """
    # Check if sys.prefix differs from sys.base_prefix
    return sys.prefix != sys.base_prefix


def main():
    """
    Test the virtual environment detection.
    """
    
    print("Running virtual environment check...")
    print(f"Python executable: {sys.executable}")
    print(f"sys.prefix: {sys.prefix}")
    print(f"sys.base_prefix: {sys.base_prefix}")
    
    if is_venv_active():
        print("✓ Virtual environment is ACTIVE")
    else:
        print("✗ Virtual environment is NOT active")
        print("  Run: python3 -m venv .venv")
        print("  Then: source .venv/bin/activate")


if __name__ == "__main__":
    main()
