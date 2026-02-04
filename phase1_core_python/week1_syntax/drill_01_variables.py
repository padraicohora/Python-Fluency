"""
Drill 1.1 — Variables + Clean Printing

Goal:
    Practice storing values and printing readable output

Task:
    Store name, age, country and print a formatted sentence

Rules:
    - Write the solution yourself
    - Keep it readable
    - Add at least 2 test cases

Reflection:
    When would you use f-strings vs .format() vs % formatting?
"""


# === Your Code Here ===


def create_introduction(name, age, country):
    """
    Create a formatted introduction string.
    
    Args:
        name: Person's name
        age: Person's age
        country: Person's country
    
    Returns:
        Formatted introduction string
    """
    pass  # Replace with your implementation


def main():
    """
    Write quick manual tests here.
    """
    
    print("Running tests...")
    
    # Test case 1
    print(create_introduction("Alice", 25, "Ireland"))
    
    # Test case 2
    print(create_introduction("Bob", 30, "USA"))
    
    print("Done.")


if __name__ == "__main__":
    main()
