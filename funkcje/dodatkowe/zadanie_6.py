
def perfect_number(liczba):
    suma = 0
    for x in range(1, liczba):
        if liczba % x == 0:
            suma += x
    return suma == liczba


def test_perfect_number():
    assert perfect_number(6) == True
    assert perfect_number(7) == False
    assert perfect_number(28) == True
    assert perfect_number(496) == True
    assert perfect_number(8128) == True

