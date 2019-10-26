import unittest

def czy_jest_pierwsza(liczba):
    """Sprawdza czy liczba jest liczbą pierwszą

    :param liczba int:
    :return: bool

    """
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


class TestCzyJestPierwsza(unittest.TestCase):

    def test_czy_jest_pierwsza_dla_liczby_pierwszej(self):
        self.assertEqual(czy_jest_pierwsza(11), True)
        self.assertEqual(czy_jest_pierwsza(7), True)
        self.assertEqual(czy_jest_pierwsza(17), True)

    def test_czy_jest_pierwsza_dla_liczby_niepierwszej(self):
        self.assertEqual(czy_jest_pierwsza(10), False)
        self.assertEqual(czy_jest_pierwsza(12), False)