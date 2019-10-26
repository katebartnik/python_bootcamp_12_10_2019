# 5. pozwoli na dodanie dwóch macierzy o jednakowych wymiarch
def add_matrices(m1, m2):
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


if __name__ == "__main__":
    print(__file__)
    print(dir())
    print(globals())
    print(__name__)
    print("XXXXXXXXXXXXXXXX")

