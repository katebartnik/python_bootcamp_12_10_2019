def nazwa_funkcji():  # definicja funkcji
    pass


nazwa_funkcji  # obiekt funkcji

nazwa_funkcji()  # wywołanie funkcji


def powitanie(imie):
    print(f"Hello {imie.upper()}")
    return 123


powitanie("Stara")

WERSJA = "1.0"
LICZNIK = 0
def powitanie(imie):
    global LICZNIK
    LICZNIK += 1
    global WERSJA
    WERSJA = "2.0"
    print(globals())
    print(locals())
    return f"Aloha {imie.upper()} {WERSJA}"




poczatek = powitanie("Nowa")
print(poczatek)
print(WERSJA)

powitanie("Nowa")
powitanie("Nowa")
powitanie("Nowa")
powitanie("Nowa")
print(LICZNIK)


def operacje(a, b, op=3, sep=";"):
    print(f"a = {a}, b={b}, op={op}, sep={sep}")

operacje(1,2)
operacje(b=2, a=1, op=10, sep=".")
operacje(1, 2, op=10, sep=".")
operacje(1,2,4)


