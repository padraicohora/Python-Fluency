"""
Helper utilities for Python Fluency Drills.

This module contains utility functions that can be used across drills.
"""


def print_test_result(test_name, passed):
    """
    Print a formatted test result.
    
    Args:
        test_name: Name of the test
        passed: Boolean indicating if test passed
    """
    status = "✓ PASS" if passed else "✗ FAIL"
    print(f"{status}: {test_name}")


def compare_values(actual, expected, test_name="Test"):
    """
    Compare two values and print result.
    
    Args:
        actual: The actual value
        expected: The expected value
        test_name: Name of the test
    
    Returns:
        True if values match, False otherwise
    """
    passed = actual == expected
    print_test_result(test_name, passed)
    if not passed:
        print(f"  Expected: {expected}")
        print(f"  Got: {actual}")
    return passed
