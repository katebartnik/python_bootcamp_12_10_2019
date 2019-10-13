"""
Napisz program obliczający średnią wartość z podanych przez
użytkownika liczb.
Liczby przyjmuj z wykorzystanie pętli while i funkcji input
Pozwól na podanie maksymalnie 10 liczb
Dodatkowo wydrukuj informajcę o minimalnej i maksymalneh wartosci

Pamietaj o funkcjach len, max, min, sum


"""
lista = []
while len(lista) < 10:
    odp = input("Podaj liczbę lub k by zakończyć")
    if odp == "k":
        break

    try:
        lista.append(int(odp))
    except ValueError:
        print("Wpisuj liczby!!!")

srednia = sum(lista) / len(lista)

print(f"Średnia wartość: {srednia}, min: {min(lista)}, max: {max(lista)}")
