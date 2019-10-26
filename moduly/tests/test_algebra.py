from mathematica.algebra.matrices import add_matrices


def test_dodaj_macierze():
    m1 = [[1, 2], [3, 4]]
    m2 = [[3, 4], [5, 6]]
    expected = [[4, 6], [8, 10]]
    assert add_matrices(m1, m2) == expected


def test_dodaj_macierze_with_zip():
    m1 = [[1, 2], [3, 4]]
    m2 = [[3, 4], [5, 6]]
    expected = [[4, 6], [8, 10]]
    assert add_matrices(m1, m2) == expected
