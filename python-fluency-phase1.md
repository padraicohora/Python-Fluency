# Python Fluency Plan —  Phase 1
*A drill-based checklist for building real Python mastery (scripts, not notebooks).*

Each drill is designed to take about fifteen to twenty minutes.
Do the task, write your own solution, run simple tests, and reflect briefly.

No copying answers. No skipping fundamentals
---


# Phase 1 — Core Python Fluency Drills (Four Weeks)
*Goal: Speak Python naturally, cleanly, and confidently.*

---

# Week 1 — Core Syntax + Data Types
*Goal: Absolute comfort with basic Python objects.*

---

## Drill 1.1 — Variables + Clean Printing
Task:
Store values and print readable output.

Do:
- Store name, age, country
- Print a formatted sentence

Test:
- Output reads naturally.

Reflection:
- When would you use f-strings?

---

## Drill 1.2 — String Slicing Practice
Task:
Write a function `reverse_string(s)`.

Test:
- `"abc"` → `"cba"`
- `"hello"` → `"olleh"`

Reflection:
- What does slicing syntax mean?

---

## Drill 1.3 — String Parsing
Task:
Write `count_vowels(s)`.

Test:
- `"hello"` → `2`
- `"xyz"` → `0`

Reflection:
- How did you decide what counts as a vowel?

---

## Drill 1.4 — Integers + Float Behavior
Task:
Explore division carefully.

Do:
- Write examples showing `/` vs `//`

Test:
- You can explain the difference clearly.

Reflection:
- Why does this matter in ML?

---

## Drill 1.5 — Boolean Logic Confidence
Task:
Write `is_even(n)`.

Test:
- `4` → True
- `7` → False

Reflection:
- What does `%` mean?

---

## Drill 1.6 — None and Missing Values
Task:
Write a function that returns `None` if input is empty.

Test:
- `""` → None
- `"hi"` → `"hi"`

Reflection:
- Why is `None` useful?

---

## Drill 1.7 — Mini Review Drill
Task:
Combine strings, numbers, and logic.

Do:
Write `describe_number(n)`:
- If even: `"n is even"`
- If odd: `"n is odd"`

Test:
- `3` → `"3 is odd"`

Reflection:
- What felt easiest this week?

---

---

# Week 2 — Collections + Control Flow
*Goal: Become fluent with Python’s core containers.*

---

## Drill 2.1 — List Loop Basics
Task:
Write `sum_list(nums)` without using `sum()`.

Test:
- `[1,2,3]` → `6`

Reflection:
- Why avoid shortcuts during practice?

---

## Drill 2.2 — List Transformations
Task:
Write `square_all(nums)`.

Test:
- `[2,3,4]` → `[4,9,16]`

Reflection:
- When would you use list comprehensions?

---

## Drill 2.3 — Dictionary Lookup
Task:
Write `count_words(sentence)`.

Test:
- `"hi hi bye"` → `{"hi":2,"bye":1}`

Reflection:
- Why are dicts so important?

---

## Drill 2.4 — Safe Access Patterns
Task:
Write `get_value(d, key)` that returns `"missing"` if absent.

Test:
- `{"a":1}, "b"` → `"missing"`

Reflection:
- What is `.get()`?

---

## Drill 2.5 — Tuples and Unpacking
Task:
Swap two variables cleanly.

Test:
- `a=1, b=2` → `a=2, b=1`

Reflection:
- Why does Python support this?

---

## Drill 2.6 — Nested Structures
Task:
Given list of dicts, extract all names.

Test:
- `[{"name":"A"},{"name":"B"}]` → `["A","B"]`

Reflection:
- Where do you see this in JSON APIs?

---

## Drill 2.7 — Week Review Drill
Task:
Write `most_common_word(sentence)`.

Test:
- `"a a b"` → `"a"`

Reflection:
- What collection feels most natural now?

---

---

# Week 3 — Functions + Problem Decomposition
*Goal: Write clean reusable code.*

---

## Drill 3.1 — Function Design Practice
Task:
Write `is_prime(n)`.

Test:
- `7` → True
- `8` → False

Reflection:
- What edge cases did you consider?

---

## Drill 3.2 — Default Parameters
Task:
Write `greet(name="friend")`.

Test:
- greet() → "Hello, friend"
- greet("Padraic") → "Hello, Padraic"

Reflection:
- Why are defaults useful?

---

## Drill 3.3 — Multiple Return Values
Task:
Write `min_max(nums)` returning `(min, max)`.

Test:
- `[3,1,5]` → `(1,5)`

Reflection:
- Why return tuples?

---

## Drill 3.4 — Clean Helper Functions
Task:
Refactor a messy function into two smaller ones.

Test:
- Both still work.

Reflection:
- Why do seniors care about decomposition?

---

## Drill 3.5 — Scope Awareness
Task:
Demonstrate local vs global variables.

Reflection:
- What mistakes happen with scope?

---

## Drill 3.6 — Simple Error Handling
Task:
Write safe division: return None if dividing by zero.

Test:
- `10/0` → None

Reflection:
- When should you raise vs return None?

---

## Drill 3.7 — Week Review Drill
Task:
Write `clean_average(nums)` ignoring None values.

Test:
- `[1,None,3]` → `2`

Reflection:
- Does this feel like real data work?

---

---

# Week 4 — Intermediate Fluency + Real Software Style
*Goal: Transition from scripts to real code structure.*

---

## Drill 4.1 — First Class
Task:
Create class `Dog` with name + `bark()`.

Test:
- Dog("Max").bark() prints `"Woof!"`

Reflection:
- What is `self`?

---

## Drill 4.2 — Simple Class State
Task:
Create `Counter` class that increments.

Test:
- counter.increment() updates count.

Reflection:
- Why store state in objects?

---

## Drill 4.3 — Reading a Text File
Task:
Read a file and count lines.

Test:
- File with 3 lines → returns 3

Reflection:
- Why use `with open()`?

---

## Drill 4.4 — Writing Clean Modules
Task:
Split code into two files:
- `utils.py`
- `main.py`

Test:
- Imports work correctly.

Reflection:
- Why does this matter for ML pipelines?

---

## Drill 4.5 — Simple CLI Script
Task:
Write script that takes user input and responds.

Test:
- Input name → prints greeting.

Reflection:
- How is this different from notebooks?

---

## Drill 4.6 — Basic Debugging Skill
Task:
Use print-debugging or breakpoints on a bug.

Reflection:
- What was the bug and how did you find it?

---

## Drill 4.7 — Final Phase One Project Drill
Task:
Write a small “data cleaner” script:

- Takes a sentence
- Removes punctuation
- Counts word frequency
- Prints top word

Test:
- Works on multiple inputs.

Reflection:
- Do you feel more like a Python programmer now?

---

# End of Phase 1

Next Phase Options:
- Standard library power tools (`collections`, `itertools`)
- Numpy + Pandas
- Matplotlib
- ML fundamentals implementation drills