
"""
Napisz tabliczke mnozenia 1 - 10


     1   2   3

1    1   2   3
2    2   4   6
3    3   6   9


skorzystaj z:
1. pętla for
2. właściwości funkcji print (end, sep)
3. fstring  i metody formatowania   "{x:4}"

"""

print("      ", end="")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]



for i in lista:
    print(f"{i:4}", end="")

print()
print()

for i in lista:
    print(f"{i:2}", end="    ")
    for j in lista:
        print(f"{i*j:4}",end="")
    print()


lista1 = [10,  20,  30,  40]
lista2 = ["a", "b", "c", "d"]

for index, element in enumerate(lista1):
    print(lista2[index] * element)
    print(lista2[index] * lista1[index])

i = 0
while i < len(lista1):
    print(lista2[i] * lista1[i])
    i += 1

macierz_a = [
    [1, 2, 3],
    [4, 5, 6]
]

macierz_b = [
    [5, 6, 7],
    [8, 9, 10]
]

wynik = []

for row_index, row in enumerate(macierz_a):
    # print(row_index, row)
    row_wynikowy = []
    for col_index, col in enumerate(row):
        row_wynikowy.append(col + macierz_b[row_index][col_index])
        # print(f"macierz a wiersz: {row_index}, kolumna: {col_index}", col)
        # print(f"macierz b wiersz: {row_index}, kolumna: {col_index}", macierz_b[row_index][col_index])
    wynik.append(row_wynikowy)
expected = [
    [6, 8, 10],
    [12, 14, 16]
]
print("wynik", wynik)
assert wynik == expected

wynik = []
i = 0
while i < len(macierz_a):
    wiersz_z_a = macierz_a[i]
    wiersz_z_b = macierz_b[i]
    j = 0
    row = []
    while j < len(wiersz_z_a):
        col_z_a = wiersz_z_a[j]
        col_z_b = wiersz_z_b[j]
        row.append(col_z_a + col_z_b)
        j += 1
    wynik.append(row)
    i += 1
print("#"*40)
print(wynik)

# ------------

wynik = []
i = 0
while i < len(macierz_a):
    j = 0
    row = []
    while j < len(macierz_a[i]):
        row.append(macierz_a[i][j] + macierz_b[i][j])
        j += 1
    wynik.append(row)
    i += 1
print("#"*40)
print(wynik)

# -----


