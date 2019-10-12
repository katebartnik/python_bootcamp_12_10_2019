
suma = 0
licznik = 0
while True:
    odp = input("Podaj liczbę lub wpisz k by zakończyć: ")
    if odp == "k":
        break
    odp = int(odp)
    suma = suma + odp  # 0 + 10
    licznik += 1 # i = i + 1  i -= 1 i *= 10 i /=

if licznik>0:
    print("Średnia wynosi: ", suma/licznik)
else:
    print("Nie podano liczb")