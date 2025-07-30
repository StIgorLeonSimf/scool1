import pytest
from trening import add
from calc_d import add, sub, mult, div


@pytest.mark.parametrize("n1, d1, n2, d2, expected", [
    (1, 2, 1, 3, (1 * 3 + 1 * 2, 2 * 3)),  # 1/2 + 1/3 = 5/6
    (1, 4, 3, 4, (1 + 3, 4)),              # 1/4 + 3/4 = 4/4
    (2, 5, -1, 5, (1, 5)),                 # 2/5 - 1/5 = 1/5
])
def test_add(n1, d1, n2, d2, expected):
    assert add(n1, d1, n2, d2) == expected


# @pytest.mark.parametrize("n1,d1,n2,d2,expected", [
#     (1, 2, 1, 3, (1 * 3 - 1 * 2, 2 * 3)),  # 1/2 - 1/3 = 1/6
#     (3, 4, 1, 4, (3 - 1, 4)),              # 3/4 - 1/4 = 2/4
# ])
# def test_sub(n1, d1, n2, d2, expected):
#     assert sub(n1, d1, n2, d2) == expected



def test_sub():
    assert sub(1, 2, 1, 3) == (1 * 3 - 1 * 2, 2 * 3)
    assert sub(3, 4, 1, 4) == (2, 4)


@pytest.mark.parametrize("n1,d1,n2,d2,expected", [
    (1, 2, 2, 3, (2, 6)),  # 1/2 * 2/3 = 2/6
    (3, 5, 5, 7, (15, 35)),
])
def test_mult(n1, d1, n2, d2, expected):
    assert mult(n1, d1, n2, d2) == expected


@pytest.mark.parametrize("n1,d1,n2,d2,expected", [
    (1, 2, 2, 3, (3, 4)),  # 1/2 ÷ 2/3 = 3/4
    (3, 5, 5, 7, (21, 25)),
])
def test_div(n1, d1, n2, d2, expected):
    assert div(n1, d1, n2, d2) == expected
