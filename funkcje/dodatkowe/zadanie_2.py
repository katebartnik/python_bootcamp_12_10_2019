"""
# Zad 2

Napisz funkcję, która:
1. Jeśli jej argument będzie listą, tuplą bądź zbiroem, zwróci sumę jej elementów
2. Jeśli jej argument będzie słownikiem, zwróci sumę wartościW obu przypadkach ignoruj napisy - o ile napisy nie reprezentują liczb

pip install jupyter
"""

def suma(iterable):
    wynik = 0
    if isinstance(iterable, dict):
        iterable = iterable.values()
    for el in iterable:
        if isinstance(el, int):
            wynik += el
        else:
            try:
                wynik += int(el)
            except ValueError:
                pass
    return wynik




def test_suma():
    assert suma([1, 2, 3]) == 6
    assert suma([1, 2, 3, "4"]) == 10
    assert suma([1, 2, 3, "a"]) == 6
    assert suma({'a':10, 'b':20}) == 30
    assert suma({'a': '10', 'b': 'xx'}) == 10
