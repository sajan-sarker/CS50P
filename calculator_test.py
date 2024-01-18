from calculator import square
from calculator import main
import unittest

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-5) == 25
    assert square(-6) == 36
    assert square(0) == 0
    assert square(9) == 81

