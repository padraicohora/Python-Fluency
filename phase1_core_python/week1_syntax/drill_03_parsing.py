"""
Drill 1.3 — String Parsing

Goal:
    Practice parsing and analyzing strings

Task:
    Write count_vowels(s) that counts vowels in a string

Rules:
    - Write the solution yourself
    - Keep it readable
    - Add at least 2 test cases

Reflection:
    How did you decide what counts as a vowel? What about uppercase?
"""


# === Your Code Here ===


def count_vowels(s):
    """
    Count the number of vowels in a string.
    
    Args:
        s: String to analyze
    
    Returns:
        Number of vowels (a, e, i, o, u)
    """
    pass  # Replace with your implementation


def main():
    """
    Write quick manual tests here.
    """
    
    print("Running tests...")
    
    # Test case 1
    result1 = count_vowels("hello")
    print(f"count_vowels('hello') = {result1}")
    assert result1 == 2, f"Expected 2, got {result1}"
    
    # Test case 2
    result2 = count_vowels("xyz")
    print(f"count_vowels('xyz') = {result2}")
    assert result2 == 0, f"Expected 0, got {result2}"
    
    print("Done.")


if __name__ == "__main__":
    main()
