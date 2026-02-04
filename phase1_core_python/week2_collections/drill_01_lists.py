"""
Drill 2.1 — List Loop Basics

Goal:
    Practice iterating through lists

Task:
    Write sum_list(nums) without using built-in sum()

Rules:
    - Write the solution yourself
    - Keep it readable
    - Add at least 2 test cases

Reflection:
    Why avoid shortcuts during practice? What are you learning?
"""


# === Your Code Here ===


def sum_list(nums):
    """
    Calculate the sum of a list of numbers.
    
    Args:
        nums: List of numbers
    
    Returns:
        Sum of all numbers
    """
    pass  # Replace with your implementation


def main():
    """
    Write quick manual tests here.
    """
    
    print("Running tests...")
    
    # Test case 1
    result1 = sum_list([1, 2, 3])
    print(f"sum_list([1, 2, 3]) = {result1}")
    assert result1 == 6, f"Expected 6, got {result1}"
    
    # Test case 2
    result2 = sum_list([10, 20, 30])
    print(f"sum_list([10, 20, 30]) = {result2}")
    assert result2 == 60, f"Expected 60, got {result2}"
    
    print("Done.")


if __name__ == "__main__":
    main()
