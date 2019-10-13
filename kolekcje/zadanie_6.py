"""
Napisz program zliczający liczbę znaków w podanym przez
użytkownika napisie pomiędzy nawiasami <>. Nawiasy
mogę wystąpić tylko raz.
Ala ma <kota>, a kot ma Alę
4
"""
napis = "Ala ma <kota>, <a> <kot> ma Alę"
#print(napis.index(">") - napis.index("<") - 1)

licznik = 0
czy_zliczac = False
for znak in napis:

    if znak == ">":
        czy_zliczac = False

    if czy_zliczac:  # True lub False
        licznik += 1

    if znak == "<":
        czy_zliczac = True


print(licznik)


