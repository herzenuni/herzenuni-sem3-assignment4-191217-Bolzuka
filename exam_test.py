from Exam import main
import pytest

def test1():
    assert main(1,2,3,4,5,6) == 6

def test2():
    assert main(-1,2,-3,4,-5,6) == -120
