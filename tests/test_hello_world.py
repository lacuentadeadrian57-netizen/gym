import pytest

from exercises.hello_world.solution import SUBMIT, hello_world

if not SUBMIT:
    pytest.skip("Solution not submitted", allow_module_level=True)


def test_hello_world_exists() -> None:
    """Check if the function exists and is callable."""
    assert callable(hello_world)


def test_hello_world_return_value() -> None:
    """Check if the return value is exactly 'Hello, World!'."""
    assert hello_world() == "Hello, World!"
