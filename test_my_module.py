import pytest
from my_module import add_numbers
import pytest

def test_add_numbers():
    assert add_numbers(8, 1) == 9
    assert add_numbers(1, 1) == 2
    assert add_numbers(-1, 1) == 0
    assert add_numbers(-5, -2) == -7

