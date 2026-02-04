# Python Fluency Drills — Setup Guide

This guide will help you get started with the Python Fluency Drills repository.

---

## Quick Start

### 1. Clone or Navigate to Repository

```bash
cd /path/to/Python-Fluency
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate Virtual Environment

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify Setup

```bash
python3 phase0_environment/drill_01_venv_check.py
```

You should see: `✓ Virtual environment is ACTIVE`

---

## Repository Structure

```
Python-Fluency/
├── README.md                    # Project overview
├── SETUP.md                     # This file
├── progress.md                  # Drill checklist
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── drill_template.py            # Template for new drills
│
├── phase0_environment/          # Phase 0: Setup & Workflow
│   ├── drill_00_hello.py
│   ├── drill_01_venv_check.py
│   └── notes.md
│
├── phase1_core_python/          # Phase 1: Core Python (4 weeks)
│   ├── week1_syntax/            # Variables, strings, numbers
│   ├── week2_collections/       # Lists, dicts, tuples
│   ├── week3_functions/         # Functions, scope, errors
│   └── week4_classes_files/     # OOP, files, modules
│
├── phase2_data_stack/           # Phase 2: Data Stack (4 weeks)
│   ├── week5_stdlib/            # Counter, pathlib, itertools
│   ├── week6_numpy/             # Arrays, broadcasting, math
│   ├── week7_pandas/            # DataFrames, groupby, cleaning
│   └── week8_matplotlib_pipeline/ # Plotting, ML workflow
│
└── utils/                       # Helper utilities
    └── helpers.py
```

---

## Daily Workflow

### 1. Activate Environment
```bash
source .venv/bin/activate
```

### 2. Choose Your Drill
Navigate to the appropriate phase/week folder and open a drill file.

### 3. Read the Drill
Each drill has:
- **Goal**: What skill you're practicing
- **Task**: What to implement
- **Rules**: Guidelines to follow
- **Reflection**: Question to answer after completing

### 4. Write Your Solution
Replace the `pass` statement with your implementation.

### 5. Run Tests
```bash
python3 path/to/drill_file.py
```

### 6. Reflect
Answer the reflection question in the week's `notes.md` file.

### 7. Commit Your Work
```bash
git add .
git commit -m "Complete drill X.Y"
```

---

## Drill Progression

### Phase 0: Environment Setup (2 drills)
- Get comfortable with terminal, scripts, and virtual environments
- **Time**: 1-2 days

### Phase 1: Core Python (28 drills)
- **Week 1**: Syntax + Data Types (7 drills)
- **Week 2**: Collections + Control Flow (7 drills)
- **Week 3**: Functions + Decomposition (7 drills)
- **Week 4**: Classes, Files, Modules (7 drills)
- **Time**: 4 weeks (1 drill per day)

### Phase 2: Data Stack (28 drills)
- **Week 5**: Standard Library Tools (7 drills)
- **Week 6**: NumPy Fundamentals (7 drills)
- **Week 7**: Pandas Fundamentals (7 drills)
- **Week 8**: Matplotlib + ML Workflow (7 drills)
- **Time**: 4 weeks (1 drill per day)

**Total**: ~60 drills over 8-10 weeks

---

## Tips for Success

### 1. Write Code Yourself
- Don't copy solutions from LLMs or Stack Overflow
- The goal is muscle memory, not just working code

### 2. Keep It Simple
- Focus on correctness first, optimization later
- Readable code > clever code

### 3. Test Everything
- Run your code after every change
- Add more test cases than the minimum

### 4. Reflect Daily
- Answer the reflection questions honestly
- Note what felt easy and what felt hard

### 5. Commit Regularly
- Commit after each drill
- Use clear commit messages

### 6. Review Weekly
- At the end of each week, review your notes
- Revisit drills that felt unclear

---

## Running Tests

### Individual Drill
```bash
python3 phase1_core_python/week1_syntax/drill_01_variables.py
```

### With pytest (if available)
```bash
pytest phase1_core_python/week1_syntax/
```

---

## Troubleshooting

### Virtual Environment Not Active
```bash
# Deactivate if needed
deactivate

# Reactivate
source .venv/bin/activate
```

### Import Errors
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Module Not Found
```bash
# Make sure you're in the project root
cd /path/to/Python-Fluency

# Run with python3
python3 path/to/drill.py
```

---

## Next Steps

1. ✅ Complete setup (you're here!)
2. Run `drill_00_hello.py` to verify everything works
3. Start Phase 0 drills
4. Move to Phase 1 when ready
5. Track progress in `progress.md`

---

## Resources

- **Python Docs**: https://docs.python.org/3/
- **NumPy Docs**: https://numpy.org/doc/
- **Pandas Docs**: https://pandas.pydata.org/docs/
- **Matplotlib Docs**: https://matplotlib.org/stable/contents.html

---

Happy drilling! 🚀
