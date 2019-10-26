def dodaj_macierze(m1, m2):
    print("Jestem funkcja z moduły Algebra")
    wynik = []
    for row_m1, row_m2 in zip(m1, m2):
        row = []
        for col_m1, col_m2 in zip(row_m1, row_m2):
            row.append(col_m1 + col_m2)
        wynik.append(row)
    return wynik
