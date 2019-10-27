"""
Zaimplementuj funkcje przycinajaca liste na podstawie podanego
warunku poczatkowego oraz koncowego:
Przykład uzycia:
przytnij(
data=[1, 2, 3, 4, 5, 6, 7],
start=lambda x: x > 3,
stop=lambda x: x == 6,
)
[4, 5, 6]

"""


def przytnij(data, start, stop):
    wynik = []

    czy_zliczac = False

    for element in data:
        if not czy_zliczac and start(element):
            czy_zliczac = True
        if czy_zliczac:
            wynik.append(element)
            if stop(element):
                break
    return wynik

def test_przytnij():
    lista = [1, 2, 3, 4, 5, 6, 7]
    assert przytnij(
        data=lista,
        start=lambda x: x > 3,
        stop=lambda x: x == 6
    ) == [4, 5, 6]
