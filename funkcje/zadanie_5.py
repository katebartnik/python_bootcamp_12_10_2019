import pytest
def silnia(n):
    if n < 0:
        raise ValueError("Argument musi być większy niż 0")
    if n == 0:
        return 1
    return n * silnia(n - 1)


# print(silnia(10))

def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(2) == 2
    assert silnia(3) == 6

def test_silnia_argument_mniejszy_niz_0():
    with pytest.raises(ValueError):
        silnia(-10)
