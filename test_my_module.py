import pytest
from my_module import add
import pytest

def test_add():
    assert add(8, 1) == 9
    assert add(1, 1) == 2
    assert add(-1, 1) == 0
    assert add(-5, -2) == -7

