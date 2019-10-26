def czy_jest_pierwsza(liczba):
    """Sprawdza czy liczba jest liczbą pierwszą

    :param liczba int:
    :return: bool

    >>> czy_jest_pierwsza(10)
    False
    >>> czy_jest_pierwsza(17)
    True
    >>> czy_jest_pierwsza(11)
    True

    """
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

