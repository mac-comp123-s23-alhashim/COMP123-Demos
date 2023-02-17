import math
import pytest


def our_sqrt(x):
    """
    Find the square root of x

    pre-condition: x must be positive
    post-condition: return square root of x
    """
    assert type(x) == int
    assert x >= 0
    return math.sqrt(x)


def test_our_sqrt_positive():
    assert our_sqrt(16) == 4


def test_our_sqrt_zero():
    assert our_sqrt(0) == 0


# catching assertions raised by the method
# you don't need to do this
def test_our_sqrt_negative():
    with pytest.raises(Exception) as e_info:
        our_sqrt(-16)


# if you have pytest package install, you don't need the lines below
test_our_sqrt_positive()
test_our_sqrt_zero()
