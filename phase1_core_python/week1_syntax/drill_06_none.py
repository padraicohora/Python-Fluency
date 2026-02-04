"""
Drill 1.6 — None and Missing Values

Goal:
    Understand None and how to handle missing values

Task:
    Write a function that returns None if input is empty

Rules:
    - Write the solution yourself
    - Keep it readable
    - Add at least 2 test cases

Reflection:
    Why is None useful? How is it different from empty string or 0?
"""


# === Your Code Here ===


def safe_string(s):
    """
    Return the string if not empty, otherwise return None.
    
    Args:
        s: String to check
    
    Returns:
        The string if not empty, None otherwise
    """
    pass  # Replace with your implementation


def main():
    """
    Write quick manual tests here.
    """
    
    print("Running tests...")
    
    # Test case 1: Empty string
    result1 = safe_string("")
    print(f"safe_string('') = {result1}")
    assert result1 is None, f"Expected None, got {result1}"
    
    # Test case 2: Non-empty string
    result2 = safe_string("hi")
    print(f"safe_string('hi') = {result2}")
    assert result2 == "hi", f"Expected 'hi', got {result2}"
    
    print("Done.")


if __name__ == "__main__":
    main()
