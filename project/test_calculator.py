import pytest
from calculator import add
def test_add():
    assert add(4, 5) == 9
    assert add(-1, 1) == 0

def test_sub():
    from calculator import subtract
    assert subtract(10, 5) == 5
    assert subtract(0, 1) == -1