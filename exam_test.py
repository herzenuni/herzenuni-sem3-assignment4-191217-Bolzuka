from Exam import *
import pytest

@pytest.mark.parametrize("a, result", [
    ([1, 9, -10, -20, -8, 7, 14, 0, 20, 20, -20], "-8000")])

def test_minumn3(a, result):
    assert minumn3(a) == int(result)
