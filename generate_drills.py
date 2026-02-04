"""
Script to generate all drill file stubs for the Python Fluency repository.
This creates the complete directory structure with drill templates.
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


# Week 2 - Collections
week2_drills = [
    ("2.2", "List Transformations", "Transform lists using comprehensions", 
     "Write square_all(nums) that squares each number", 
     "When would you use list comprehensions vs loops?"),
    ("2.3", "Dictionary Counting", "Count occurrences using dictionaries",
     "Write count_words(sentence) that returns word frequency dict",
     "Why are dicts so important in Python?"),
    ("2.4", "Safe Dict Access", "Handle missing dictionary keys safely",
     "Write get_value(d, key) that returns 'missing' if key absent",
     "What is the .get() method and when should you use it?"),
    ("2.5", "Tuples + Unpacking", "Practice tuple unpacking",
     "Swap two variables cleanly using tuple unpacking",
     "Why does Python support tuple unpacking?"),
    ("2.6", "Nested Structures", "Work with nested data structures",
     "Extract all names from list of dicts: [{'name':'A'},{'name':'B'}]",
     "Where do you see this pattern in JSON APIs?"),
    ("2.7", "Week Review", "Combine collections knowledge",
     "Write most_common_word(sentence) that returns the most frequent word",
     "What collection type feels most natural now?"),
]

# Week 3 - Functions
week3_drills = [
    ("3.1", "Function Design", "Design clean, reusable functions",
     "Write is_prime(n) that checks if a number is prime",
     "What edge cases did you consider?"),
    ("3.2", "Default Parameters", "Use default parameter values",
     "Write greet(name='friend') with default parameter",
     "Why are default parameters useful?"),
    ("3.3", "Multiple Returns", "Return multiple values from functions",
     "Write min_max(nums) returning (min, max) tuple",
     "Why return tuples instead of lists?"),
    ("3.4", "Helper Functions", "Decompose problems into helper functions",
     "Refactor a messy function into smaller helper functions",
     "Why do senior engineers care about decomposition?"),
    ("3.5", "Scope Awareness", "Understand variable scope",
     "Demonstrate local vs global variable behavior",
     "What mistakes commonly happen with scope?"),
    ("3.6", "Error Handling", "Handle errors gracefully",
     "Write safe_divide(a, b) that returns None for division by zero",
     "When should you raise exceptions vs return None?"),
    ("3.7", "Week Review", "Combine function concepts",
     "Write clean_average(nums) that ignores None values",
     "Does this feel like real data work?"),
]

# Week 4 - Classes and Files
week4_drills = [
    ("4.1", "First Class", "Create your first Python class",
     "Create class Dog with name attribute and bark() method",
     "What is self and why is it needed?"),
    ("4.2", "Class State", "Manage state in classes",
     "Create Counter class that increments and tracks count",
     "Why store state in objects?"),
    ("4.3", "File Reading", "Read data from files",
     "Read a text file and count its lines",
     "Why use 'with open()' instead of just open()?"),
    ("4.4", "Modules", "Organize code into modules",
     "Split code into utils.py and main.py with imports",
     "Why does this matter for ML pipelines?"),
    ("4.5", "CLI Script", "Create command-line scripts",
     "Write script that takes user input and responds",
     "How is this different from notebooks?"),
    ("4.6", "Debugging", "Practice debugging techniques",
     "Debug a buggy function using print statements or breakpoints",
     "What was the bug and how did you find it?"),
    ("4.7", "Phase 1 Capstone", "Combine all Phase 1 skills",
     "Write a data cleaner: remove punctuation, count word frequency, print top word",
     "Do you feel more like a Python programmer now?"),
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
    """Generate all drill files."""
    base_path = Path("phase1_core_python")
    
    # Week 2
    week2_path = base_path / "week2_collections"
    for drill_num, title, goal, task, reflection in week2_drills:
        filename = f"drill_{drill_num.replace('.', '_')}.py"
        create_drill_file(
            week2_path / filename,
            drill_num, title, goal, task, reflection
        )
    create_notes_file(week2_path / "notes.md", "Week 2 Notes — Collections + Control Flow")
    
    # Week 3
    week3_path = base_path / "week3_functions"
    for drill_num, title, goal, task, reflection in week3_drills:
        filename = f"drill_{drill_num.replace('.', '_')}.py"
        create_drill_file(
            week3_path / filename,
            drill_num, title, goal, task, reflection
        )
    create_notes_file(week3_path / "notes.md", "Week 3 Notes — Functions + Decomposition")
    
    # Week 4
    week4_path = base_path / "week4_classes_files"
    for drill_num, title, goal, task, reflection in week4_drills:
        filename = f"drill_{drill_num.replace('.', '_')}.py"
        create_drill_file(
            week4_path / filename,
            drill_num, title, goal, task, reflection
        )
    create_notes_file(week4_path / "notes.md", "Week 4 Notes — Classes, Files, and Real Software")
    
    print("\n✓ All Phase 1 drill files created!")


if __name__ == "__main__":
    main()
