import pytest
def func(x):
    return x + 1

def test_answer():
    assert(func(13) == 14)

def test_answer2():
    assert(func(4) == 5)