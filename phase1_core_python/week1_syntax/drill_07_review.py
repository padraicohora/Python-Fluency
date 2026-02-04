"""
Drill 1.7 — Mini Review Drill

Goal:
    Combine strings, numbers, and logic from Week 1

Task:
    Write describe_number(n) that returns:
    - "n is even" if even
    - "n is odd" if odd

Rules:
    - Write the solution yourself
    - Keep it readable
    - Add at least 2 test cases

Reflection:
    What felt easiest this week? What needs more practice?
"""


# === Your Code Here ===


def describe_number(n):
    """
    Describe whether a number is even or odd.
    
    Args:
        n: Integer to describe
    
    Returns:
        String describing the number
    """
    pass  # Replace with your implementation


def main():
    """
    Write quick manual tests here.
    """
    
    print("Running tests...")
    
    # Test case 1
    result1 = describe_number(3)
    print(f"describe_number(3) = '{result1}'")
    assert result1 == "3 is odd", f"Expected '3 is odd', got '{result1}'"
    
    # Test case 2
    result2 = describe_number(4)
    print(f"describe_number(4) = '{result2}'")
    assert result2 == "4 is even", f"Expected '4 is even', got '{result2}'"
    
    print("Done.")


if __name__ == "__main__":
    main()
