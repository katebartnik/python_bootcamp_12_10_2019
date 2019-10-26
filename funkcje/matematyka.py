import math

FI = 1.61
operatory = ["*", "+", "-"]


# Napisz funkcje, które:
# 1. Policzy pole kwadratu
def pole_kwadratu(a):
    return a ** 2


# 2. Policzy pole prostokata
def pole_prostokata(a, b):
    return a * b


# 3. policzy pole trójkata
def pole_trojkata(a, h):
    return a * h / 2


# 4. policzy pole koła. Niech domyślni promien wynosi 1
def pole_kola(r=1):
    return math.pi * r ** 2


# 5. pozwoli na dodanie dwóch macierzy o jednakowych wymiarch
def dodaj_macierze(m1, m2):
    wynik = []
    for i, row in enumerate(m1):
        new_row = []
        for j, col in enumerate(row):
            new_row.append(col + m2[i][j])
        wynik.append(new_row)
    return wynik


def dodaj_macierze_with_zip(m1, m2):
    wynik = []
    for row_m1, row_m2 in zip(m1, m2):
        row = []
        for col_m1, col_m2 in zip(row_m1, row_m2):
            row.append(col_m1 + col_m2)
        wynik.append(row)
    return wynik


def test_pole_kwadratu():
    assert pole_kwadratu(2) == 4
    assert pole_kwadratu(10) == 100


def test_pole_prostokata():
    assert pole_prostokata(2, 4) == 8
    assert pole_prostokata(10, 20) == 200


def test_pole_trojkata():
    assert pole_trojkata(2, 4) == 4
    assert pole_trojkata(10, 20) == 100


def test_pole_kola():
    assert pole_kola() == math.pi * 1 ** 2
    assert pole_kola(5) == math.pi * 5 ** 2


def test_dodaj_macierze():
    m1 = [[1, 2], [3, 4]]
    m2 = [[3, 4], [5, 6]]
    expected = [[4, 6], [8, 10]]
    assert dodaj_macierze(m1, m2) == expected


def test_dodaj_macierze_with_zip():
    m1 = [[1, 2], [3, 4]]
    m2 = [[3, 4], [5, 6]]
    expected = [[4, 6], [8, 10]]
    assert dodaj_macierze_with_zip(m1, m2) == expected
