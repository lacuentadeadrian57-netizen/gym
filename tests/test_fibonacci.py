import pytest

from exercises.fibonacci.solution import SUBMIT, fibonacci

if not SUBMIT:
    pytest.skip("Solution not submitted", allow_module_level=True)


def test_fibonacci_exists() -> None:
    """Check if the function exists and is callable."""
    assert callable(fibonacci)


def test_fibonacci_base_cases() -> None:
    """Check the fundamental base cases."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
