def splaszcz(lista):
    wynik = []
    for element in lista:
        if isinstance(element, list):
            for e in splaszcz(element):
                wynik.append(e)
        else:
            wynik.append(element)
    return wynik


def test_splaszcz_puta_lista():
    assert splaszcz([]) == []


def test_splaszcz_plaska_lista():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]


def test_splaszcz_lista_z_zagniezdzeniami():
    expected = [1, 2, 3, 4, 5, 6, 7 ,8, 9]
    assert splaszcz([1, 2, 3, [4, 5, 6, [7], 8], 9]) == expected
