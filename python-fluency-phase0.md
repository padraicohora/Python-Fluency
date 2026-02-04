# Python Fluency Plan — Phase 0 + Phase 1
*A drill-based checklist for real Python mastery (scripts, not notebooks).*

Each drill is designed for ~15–20 minutes.

Rules:
- Write the code yourself (no copying solutions)
- Run simple tests every time
- Prioritize correctness first, then readability
- Reflect briefly after each drill
- Commit regularly

---

# Phase 0 — Environment + Workflow Foundations
*Goal: Work like a Python engineer (terminal, scripts, git, testing).*

---

## Drill 0.1 — Confirm Python Installation
Task:
- Verify Python is installed correctly.

Do:
- Check your Python version in the terminal.

Test:
- `python3 --version` prints a valid version.

Reflection:
- Why does Python version matter?

---

## Drill 0.2 — Run Your First Script
Task:
- Create and run a `.py` file from the terminal.

Do:
- Create `hello.py`
- Print a short message

Test:
- `python3 hello.py` prints correctly.

Reflection:
- Script vs notebook: what’s the difference?

---

## Drill 0.3 — Basic Project Folder Structure
Task:
- Create a clean repo layout.

Do:
Create:

- `phase0_environment/`
- `phase1_core_python/`
- `notes/`
- `README.md`

Test:
- You can explain what each folder is for.

Reflection:
- Why does structure matter long-term?

---

## Drill 0.4 — Virtual Environment Setup
Task:
- Create and activate a virtual environment.

Do:
- Create `.venv`
- Activate it

Test:
- Terminal shows environment is active.

Reflection:
- Why should every project have its own venv?

---

## Drill 0.5 — Install One Package Safely
Task:
- Practice installing packages inside the venv.

Do:
- Install `requests`

Test:
- Script imports it successfully.

Reflection:
- Why avoid global installs?

---

## Drill 0.6 — Git Repo Initialization
Task:
- Track your work properly.

Do:
- `git init`
- Make your first commit

Test:
- `git status` is clean.

Reflection:
- Why commit even practice work?

---

## Drill 0.7 — Daily Workflow Habit
Task:
- Practice the full daily routine.

Do:
- Write a small drill script
- Run it
- Commit it

Test:
- You can repeat the cycle without help.

Reflection:
- What part still feels awkward?

---

## Drill 0.8 — Create a Proper `.gitignore`
Task:
- Learn what should never be committed.

Do:
- Create a `.gitignore`

Must ignore:
- `.venv/`
- `__pycache__/`
- `.DS_Store`

Test:
- `git status` does NOT show ignored files.

Reflection:
- Why is committing a venv a mistake?

---

## Drill 0.9 — Create Your Drill Template File
Task:
- Standardize every drill file format.

Do:
- Create `drill_template.py`

Include:
- Goal
- Task
- Tests section
- Reflection question

Test:
- Template runs cleanly.

Reflection:
- Why is consistency valuable?

---

## Drill 0.10 — Your First Pytest Test
Task:
- Learn baseline professional testing.

Do:
- Install pytest
- Create `tests/test_sanity.py`

Write:

```python
def test_basic_math():
    assert 1 + 1 == 2