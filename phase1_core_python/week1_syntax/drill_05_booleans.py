"""
Drill 1.5 — Boolean Logic Confidence

Goal:
    Practice boolean logic and conditionals

Task:
    Write is_even(n) that returns True if n is even

Rules:
    - Write the solution yourself
    - Keep it readable
    - Add at least 2 test cases

Reflection:
    What does the % (modulo) operator do? Why is it useful?
"""


# === Your Code Here ===


def is_even(n):
    """
    Check if a number is even.
    
    Args:
        n: Integer to check
    
    Returns:
        True if even, False if odd
    """
    pass  # Replace with your implementation


def main():
    """
    Write quick manual tests here.
    """
    
    print("Running tests...")
    
    # Test case 1
    result1 = is_even(4)
    print(f"is_even(4) = {result1}")
    assert result1 == True, f"Expected True, got {result1}"
    
    # Test case 2
    result2 = is_even(7)
    print(f"is_even(7) = {result2}")
    assert result2 == False, f"Expected False, got {result2}"
    
    print("Done.")


if __name__ == "__main__":
    main()
