import pytest
from trening import add
from calc_d import *


def test_add():
    assert add(3, 5) == 8
    assert add(1, 1) == 2

# def test_calc():
#     assert func() ==
