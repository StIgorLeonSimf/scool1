import pytest
from trening import add


def test_add():
    assert add(3, 5) == 8
    assert add(1, 1) == 2