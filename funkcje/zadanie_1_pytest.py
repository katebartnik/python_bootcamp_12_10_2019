# pip install pytest
def czy_jest_pierwsza(liczba):
    """Sprawdza czy liczba jest liczbą pierwszą

    :param liczba int:
    :return: bool

    """
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(11) == True
    assert czy_jest_pierwsza(7) == True
    assert czy_jest_pierwsza(17) == True


def test_czy_jest_pierwsza_dla_liczby_niepierwszej():
    assert czy_jest_pierwsza(10) == False
    assert czy_jest_pierwsza(9) == False
