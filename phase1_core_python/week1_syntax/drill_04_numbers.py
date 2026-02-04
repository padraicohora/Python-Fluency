"""
Drill 1.4 — Integers + Float Behavior

Goal:
    Understand division operators in Python

Task:
    Explore and demonstrate the difference between / and //

Rules:
    - Write the solution yourself
    - Keep it readable
    - Add at least 2 test cases

Reflection:
    Why does this matter in ML? When would you use each operator?
"""


# === Your Code Here ===


def demonstrate_division():
    """
    Show the difference between / and // operators.
    """
    print("Regular division (/):")
    print(f"  10 / 3 = {10 / 3}")
    print(f"  10 / 2 = {10 / 2}")
    
    print("\nFloor division (//):")
    print(f"  10 // 3 = {10 // 3}")
    print(f"  10 // 2 = {10 // 2}")
    
    print("\nModulo (%):")
    print(f"  10 % 3 = {10 % 3}")
    print(f"  10 % 2 = {10 % 2}")


def main():
    """
    Write quick manual tests here.
    """
    
    print("Running tests...")
    
    demonstrate_division()
    
    # Test case 1: Regular division always returns float
    assert type(10 / 2) == float, "Regular division should return float"
    
    # Test case 2: Floor division returns int
    assert type(10 // 2) == int, "Floor division should return int"
    
    print("\nDone.")


if __name__ == "__main__":
    main()
