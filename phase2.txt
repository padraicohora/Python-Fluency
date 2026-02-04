# Python Fluency Plan — Phase 2
*Goal: Transition from core Python into real ML-ready engineering.*

This phase builds three professional skills:

- Writing more Pythonic, standard-library-driven code  
- Working with real data structures (NumPy + Pandas)  
- Visualizing and inspecting data (Matplotlib)

---

# Phase 2 — Standard Library + Data Stack Fluency

---

# Week 5 — Python Standard Library Power Tools
*Goal: Write code that looks like real production Python.*

---

## Drill 5.1 — `collections.Counter`
Task:
Count frequency of items using `Counter`.

Do:
- Count letters in a string

Test:
- `"banana"` → `{"a":3,"b":1,"n":2}`

Reflection:
- Why is this better than manual dict counting?

---

## Drill 5.2 — `defaultdict`
Task:
Rewrite a grouping task using `defaultdict`.

Test:
- Group words by first letter

Reflection:
- What problem does `defaultdict` solve?

---

## Drill 5.3 — `namedtuple` or `dataclass`
Task:
Represent a data record cleanly.

Do:
- Create a Person record with name + age

Test:
- Access fields by name

Reflection:
- Why not just use a dict?

---

## Drill 5.4 — `pathlib` over string paths
Task:
List all `.txt` files in a folder using `pathlib`.

Test:
- Prints valid file paths

Reflection:
- Why is `pathlib` preferred?

---

## Drill 5.5 — `itertools` basics
Task:
Generate combinations or pairs of items.

Test:
- Pairs from `[1,2,3]`

Reflection:
- When is this useful in ML preprocessing?

---

## Drill 5.6 — `enumerate` and `zip`
Task:
Rewrite loops using `enumerate` and `zip`.

Test:
- Loop with index + value cleanly

Reflection:
- Why is this more readable?

---

## Drill 5.7 — Week Review Drill
Task:
Write a clean script that:

- Reads lines from a file
- Counts top five words
- Prints results neatly

Reflection:
- Does your code feel “Pythonic” now?

---

---

# Week 6 — NumPy Fundamentals
*Goal: Think in vectors and arrays, not Python lists.*

---

## Drill 6.1 — Create Arrays
Task:
Create arrays from lists and ranges.

Test:
- Shape and dtype are as expected

Reflection:
- Why does ML prefer arrays?

---

## Drill 6.2 — Array Math
Task:
Compute mean, std, and elementwise operations.

Test:
- `[1,2,3]` mean → `2`

Reflection:
- How is this different from looping?

---

## Drill 6.3 — Broadcasting
Task:
Add a scalar to an array.

Test:
- `[1,2,3] + 10` → `[11,12,13]`

Reflection:
- Why is broadcasting powerful?

---

## Drill 6.4 — Indexing + Slicing
Task:
Extract rows/columns from a 2D array.

Test:
- Correct subset returned

Reflection:
- Why is indexing critical in ML?

---

## Drill 6.5 — Random Numbers
Task:
Generate reproducible random arrays.

Do:
- Set seed
- Generate random values

Reflection:
- Why do seeds matter?

---

## Drill 6.6 — Simple Linear Algebra
Task:
Compute dot product between vectors.

Test:
- `[1,2] · [3,4]` → `11`

Reflection:
- Where does dot product appear in neural nets?

---

## Drill 6.7 — Week Review Drill
Task:
Simulate a dataset with NumPy:

- Generate 100 values
- Normalize them
- Print mean/std after scaling

Reflection:
- Does NumPy feel natural yet?

---

---

# Week 7 — Pandas Fundamentals
*Goal: Work with real-world tabular data confidently.*

---

## Drill 7.1 — Create a DataFrame
Task:
Create a DataFrame from a dict.

Test:
- Columns match expected

Reflection:
- What is a DataFrame conceptually?

---

## Drill 7.2 — Load CSV Data
Task:
Load a CSV file into Pandas.

Test:
- Print `.head()` and `.info()`

Reflection:
- Why inspect data immediately?

---

## Drill 7.3 — Selecting Columns + Rows
Task:
Extract subsets with `.loc` and `.iloc`.

Test:
- Correct row/column returned

Reflection:
- What is the difference between loc and iloc?

---

## Drill 7.4 — Filtering Data
Task:
Filter rows based on a condition.

Test:
- Only matching rows remain

Reflection:
- Why does this matter for cleaning datasets?

---

## Drill 7.5 — Missing Data Handling
Task:
Detect and fill NaN values.

Test:
- Missing values replaced properly

Reflection:
- Why is missing data unavoidable?

---

## Drill 7.6 — GroupBy Aggregations
Task:
Group data and compute summary statistics.

Test:
- Mean per category

Reflection:
- Why is groupby so common in analytics?

---

## Drill 7.7 — Week Review Drill
Task:
Load a dataset and answer:

- How many rows?
- Most common category?
- Average value of one column?

Reflection:
- Can you “interrogate” data now?

---

---

# Week 8 — Matplotlib + ML Workflow Habits
*Goal: Build the core ML notebook-to-production bridge.*

---

## Drill 8.1 — Basic Plot
Task:
Plot a simple line graph.

Test:
- Plot renders correctly

Reflection:
- Why visualize early?

---

## Drill 8.2 — Scatter Plot for Data
Task:
Plot simulated 2D points.

Test:
- Points displayed clearly

Reflection:
- Where do scatter plots help in ML?

---

## Drill 8.3 — Histogram
Task:
Plot distribution of random values.

Test:
- Shape looks reasonable

Reflection:
- Why care about distributions?

---

## Drill 8.4 — Train/Test Split Thinking
Task:
Write a script that splits data into two sets manually.

Test:
- Eighty/twenty split correct

Reflection:
- Why is splitting fundamental?

---

## Drill 8.5 — Simple Dataset Pipeline Script
Task:
Write a mini pipeline:

- Load CSV
- Clean missing values
- Compute summary stats
- Plot one graph

Reflection:
- Does this feel like real ML preparation?

---

## Drill 8.6 — Reproducible Project Structure
Task:
Create structure:

- `data/`
- `src/`
- `notebooks/`
- `requirements.txt`

Reflection:
- Why does structure matter in teams?

---

## Drill 8.7 — Final Phase Two Capstone Drill
Task:
Complete a full mini ML prep workflow:

- Load dataset
- Clean it
- Explore it with groupby
- Plot key distributions
- Save cleaned dataset

Reflection:
- Do you now feel ML-ready in Python?

---

# End of Phase 2

Next Phase Options:
- Scikit-learn drill-based mastery
- Writing training loops in PyTorch
- Implementing ML algorithms from scratch
- Building real end-to-end ML projects