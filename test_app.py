from app import add, subtract, multiply

def test_add():
    assert add(2, 3) == 6  # assert - verifies that the result matches what we expect.


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(3, 4) == 12
