liczba1 = input("Podaj liczbę 1: ")
liczba2 = input("Podaj liczbę 2: ")

liczba1 = int(liczba1)
liczba2 = int(liczba2)

operacja = input(f"Operacja pomiedzy {liczba1} {liczba2}: ")

if operacja == "+":
    wynik = liczba1 + liczba2
elif operacja == "-":
    wynik = liczba1 - liczba2

try:
    print(f"Wynik: {wynik}")
except NameError:
    print("Nieznana operacja")
