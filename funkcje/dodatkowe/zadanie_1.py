"""
# Zad 1

* Napisz funkcję (lub funkcje), które zwrócą maksymalną spośród 3 liczb.
* W rozwiązaniu skorzystaj tylko z możliwośći definiowania funkcji i używania w nich operatorów porównania
"""
def max_of_two(a, b):
    if a > b:
        return a
    return b

def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))

def test_max_of_three():
    assert max_of_three(3, 6, -5)
    assert max_of_three(1, 2, 3)
