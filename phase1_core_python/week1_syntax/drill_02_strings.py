"""
Drill 1.2 — String Slicing Practice

Goal:
    Master Python string slicing syntax

Task:
    Write a function reverse_string(s) that reverses a string

Rules:
    - Write the solution yourself
    - Keep it readable
    - Add at least 2 test cases

Reflection:
    What does the slicing syntax [::-1] mean? How does it work?
"""


# === Your Code Here ===


def reverse_string(s):
    """
    Reverse a string using slicing.
    
    Args:
        s: String to reverse
    
    Returns:
        Reversed string
    """
    pass  # Replace with your implementation


def main():
    """
    Write quick manual tests here.
    """
    
    print("Running tests...")
    
    # Test case 1
    result1 = reverse_string("abc")
    print(f"reverse_string('abc') = '{result1}'")
    assert result1 == "cba", f"Expected 'cba', got '{result1}'"
    
    # Test case 2
    result2 = reverse_string("hello")
    print(f"reverse_string('hello') = '{result2}'")
    assert result2 == "olleh", f"Expected 'olleh', got '{result2}'"
    
    print("Done.")


if __name__ == "__main__":
    main()
