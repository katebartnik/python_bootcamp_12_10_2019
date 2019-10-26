import math
from mathematica.geometry.figures import pole_kwadratu, pole_prostokata, pole_trojkata, pole_kola


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

