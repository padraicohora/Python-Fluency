"""
Script to generate Phase 2 drill files (Data Stack).
"""

import os
from pathlib import Path


DRILL_TEMPLATE = '''"""
Drill {number} — {title}

Goal:
    {goal}

Task:
    {task}

Rules:
    - Write the solution yourself
    - Keep it readable
    - Add at least 2 test cases

Reflection:
    {reflection}
"""


# === Your Code Here ===


def main():
    """
    Write quick manual tests here.
    """
    
    print("Running tests...")
    
    # Test case 1
    # TODO: Add your test
    
    # Test case 2
    # TODO: Add your test
    
    print("Done.")


if __name__ == "__main__":
    main()
'''


NOTES_TEMPLATE = '''# {title}

## Key Learnings

{key_learnings}

## Reflections

### What felt easy?


### What felt challenging?


### What do I want to revisit?


## Next Steps

- [ ] Complete all drills
- [ ] Review any unclear concepts
- [ ] Move to next phase/week
'''


# Week 5 - Standard Library
week5_drills = [
    ("5.1", "collections.Counter", "Use Counter for frequency counting",
     "Count letter frequency in a string using Counter",
     "Why is this better than manual dict counting?"),
    ("5.2", "defaultdict", "Use defaultdict for grouping",
     "Group words by first letter using defaultdict",
     "What problem does defaultdict solve?"),
    ("5.3", "dataclass/namedtuple", "Create structured data types",
     "Create a Person record with name and age using dataclass",
     "Why not just use a dict?"),
    ("5.4", "pathlib", "Use pathlib for file operations",
     "List all .txt files in a folder using pathlib",
     "Why is pathlib preferred over string paths?"),
    ("5.5", "itertools", "Use itertools for combinations",
     "Generate all pairs from a list using itertools",
     "When is this useful in ML preprocessing?"),
    ("5.6", "enumerate + zip", "Use enumerate and zip in loops",
     "Rewrite loops using enumerate and zip",
     "Why is this more readable?"),
    ("5.7", "Week Review", "Combine stdlib tools",
     "Read file, count top 5 words, print results using Counter and pathlib",
     "Does your code feel 'Pythonic' now?"),
]

# Week 6 - NumPy
week6_drills = [
    ("6.1", "Create Arrays", "Create NumPy arrays from lists",
     "Create arrays from lists and ranges, check shape and dtype",
     "Why does ML prefer arrays over lists?"),
    ("6.2", "Array Math", "Perform array operations",
     "Compute mean, std, and elementwise operations on arrays",
     "How is this different from looping?"),
    ("6.3", "Broadcasting", "Understand NumPy broadcasting",
     "Add a scalar to an array, demonstrate broadcasting",
     "Why is broadcasting powerful?"),
    ("6.4", "Indexing + Slicing", "Extract array subsets",
     "Extract rows and columns from 2D arrays",
     "Why is indexing critical in ML?"),
    ("6.5", "Random Numbers", "Generate reproducible random data",
     "Generate random arrays with fixed seed",
     "Why do seeds matter in ML?"),
    ("6.6", "Dot Product", "Compute vector dot products",
     "Compute dot product between two vectors",
     "Where does dot product appear in neural nets?"),
    ("6.7", "Week Review", "Simulate and normalize dataset",
     "Generate 100 random values, normalize them, print mean/std",
     "Does NumPy feel natural yet?"),
]

# Week 7 - Pandas
week7_drills = [
    ("7.1", "Create DataFrame", "Create DataFrames from dicts",
     "Create a DataFrame from a dictionary",
     "What is a DataFrame conceptually?"),
    ("7.2", "Load CSV", "Read CSV files into Pandas",
     "Load a CSV file and print .head() and .info()",
     "Why inspect data immediately?"),
    ("7.3", "loc vs iloc", "Select data with loc and iloc",
     "Extract subsets using .loc and .iloc",
     "What's the difference between loc and iloc?"),
    ("7.4", "Filtering", "Filter DataFrame rows",
     "Filter rows based on conditions",
     "Why is this essential for data cleaning?"),
    ("7.5", "Missing Data", "Handle NaN values",
     "Detect and fill missing values",
     "Why is missing data unavoidable?"),
    ("7.6", "GroupBy", "Aggregate data by groups",
     "Group data and compute summary statistics",
     "Why is groupby so common in analytics?"),
    ("7.7", "Week Review", "Interrogate a dataset",
     "Load dataset, answer: row count, most common category, average value",
     "Can you 'interrogate' data now?"),
]

# Week 8 - Matplotlib + ML Workflow
week8_drills = [
    ("8.1", "Line Plot", "Create basic line plots",
     "Plot a simple line graph",
     "Why visualize early in analysis?"),
    ("8.2", "Scatter Plot", "Create scatter plots",
     "Plot simulated 2D points as scatter plot",
     "Where do scatter plots help in ML?"),
    ("8.3", "Histogram", "Plot data distributions",
     "Plot histogram of random values",
     "Why care about distributions?"),
    ("8.4", "Train/Test Split", "Split data manually",
     "Write script to split data 80/20",
     "Why is splitting fundamental in ML?"),
    ("8.5", "Data Pipeline", "Build mini data pipeline",
     "Load CSV, clean missing values, compute stats, plot graph",
     "Does this feel like real ML preparation?"),
    ("8.6", "Project Structure", "Create reproducible structure",
     "Create folders: data/, src/, notebooks/, requirements.txt",
     "Why does structure matter in teams?"),
    ("8.7", "Phase 2 Capstone", "Complete ML prep workflow",
     "Load dataset, clean, explore with groupby, plot distributions, save cleaned data",
     "Do you feel ML-ready in Python now?"),
]


def create_drill_file(path, number, title, goal, task, reflection):
    """Create a drill file with the template."""
    content = DRILL_TEMPLATE.format(
        number=number,
        title=title,
        goal=goal,
        task=task,
        reflection=reflection
    )
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created: {path}")


def create_notes_file(path, title, key_learnings=""):
    """Create a notes file with the template."""
    content = NOTES_TEMPLATE.format(
        title=title,
        key_learnings=key_learnings
    )
    
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created: {path}")


def main():
    """Generate all Phase 2 drill files."""
    base_path = Path("phase2_data_stack")
    
    # Week 5
    week5_path = base_path / "week5_stdlib"
    for drill_num, title, goal, task, reflection in week5_drills:
        filename = f"drill_{drill_num.replace('.', '_')}.py"
        create_drill_file(
            week5_path / filename,
            drill_num, title, goal, task, reflection
        )
    create_notes_file(week5_path / "notes.md", "Week 5 Notes — Python Standard Library")
    
    # Week 6
    week6_path = base_path / "week6_numpy"
    for drill_num, title, goal, task, reflection in week6_drills:
        filename = f"drill_{drill_num.replace('.', '_')}.py"
        create_drill_file(
            week6_path / filename,
            drill_num, title, goal, task, reflection
        )
    create_notes_file(week6_path / "notes.md", "Week 6 Notes — NumPy Fundamentals")
    
    # Week 7
    week7_path = base_path / "week7_pandas"
    for drill_num, title, goal, task, reflection in week7_drills:
        filename = f"drill_{drill_num.replace('.', '_')}.py"
        create_drill_file(
            week7_path / filename,
            drill_num, title, goal, task, reflection
        )
    create_notes_file(week7_path / "notes.md", "Week 7 Notes — Pandas Fundamentals")
    
    # Week 8
    week8_path = base_path / "week8_matplotlib_pipeline"
    for drill_num, title, goal, task, reflection in week8_drills:
        filename = f"drill_{drill_num.replace('.', '_')}.py"
        create_drill_file(
            week8_path / filename,
            drill_num, title, goal, task, reflection
        )
    create_notes_file(week8_path / "notes.md", "Week 8 Notes — Matplotlib + ML Workflow")
    
    print("\n✓ All Phase 2 drill files created!")


if __name__ == "__main__":
    main()
