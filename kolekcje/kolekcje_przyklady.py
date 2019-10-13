###
### Dziś poznamy tuple, listy, zbiory i słowniki

# tworzenie listy
lista = []  # pusta lista
lista1 = [1, 2, 3]
lista2 = [1, "2", "a", 3]
lista3 = [1, "2", ["a", 3]]

# funkcja tworząca liste : list

lista = list()

# lista ma swoje metody
# 'append', 'clear', 'copy',
# 'count', 'extend', 'index',
# 'insert', 'pop', 'remove',
# 'reverse', 'sort'

print(dir(lista))
print(help(lista.append))
print("lista przed append:", lista)
print(lista.append(10))
print("lista po append:", lista)
print(lista.pop())
print("lista po pop:", lista)

# len
print(help(len))
print(len([]))  # 0
print(len([1, 2, 3]))  # 3

#  w pythonie indeksujemy od 0

[10, 20, 30, 40, 50]  # wartosci
# 0   1   2   3   4   # index

lista = [10, 20, 30, 40, 50]
print(lista.index(50))

print(lista[3])  # 40
print(lista[1])  # 20
print(lista[0])  # 10

# slicing - wybieranie
lista = [10, 20, 30, 40, 1, 2, 3, 4, 50, 60, 70]
print(lista[4:])
print(lista[:4])
print(lista[3:7])
# [start:stop:step]
print(lista[::2])
print(lista[1::2])

print(lista[-1])
print(lista[1:-2:2])

print(lista[::-1])

# Tupla : tuple
# z listy mogę zrobić tuple
print(tuple(lista))
moja_tupla = (1,2,3,4,5,6)
print(moja_tupla)
print(dir(moja_tupla))

a = (1, 2, 3)
b = (2, 3, 4)
print(id(a))
a = a + b
print(id(a))

import sys

x = list(range(1000000))
print(sys.getsizeof(x))
print(sys.getsizeof(tuple(x)))

a = [1, 2, 3]
b = a

b.append(4)
print(a)

print(b is a)

a = (1, 2, 3)
b = a
x = ("a",)
print(x)


# set - zbiór
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# suma
print(A | B)
print(A.union(B))

# różnica
print(A - B)
print(B - A)

# cześć wspólna - koniunkcja
print(A & B)
print(A.intersection(B))

# różnica symetryczna
print(A^B)
print(A.symmetric_difference(B))

print(dir(A))

print(A)
A.add(5)
A.add(5)
A.add(5)
A.add(5)
A.add(5)
print(A)


set() # pusty zbior
# słownik - dict
pusty_slownik = {} # lub dict()


slownik = {
    "a": 1,
    "b": 2
}

ang_pol = {
    "cat": "kot",
    "dog": "pies",
}

pol_ang = dict(kot="cat", pies="dog")

print(ang_pol)
print(pol_ang)

print(ang_pol['cat'])  # wybieramy wartosc dla klucza
ang_pol['bird'] = "ptak"
print(ang_pol)

print("bird" in ang_pol)
print(ang_pol.keys())
print("bird" in ang_pol.keys())

print(ang_pol.values())
print("ptak" in ang_pol.values())

if 'tree' in ang_pol:
    ang_pol['tree']

print(ang_pol.get('tree', "Brak w słowniku"))
print(ang_pol.get('dog'))

liczniki = {}

liczniki['dog'] = liczniki.get('dog', 0) + 1
liczniki['dog'] = liczniki.get('dog', 0) + 1
liczniki['dog'] = liczniki.get('dog', 0) + 1
liczniki['dog'] = liczniki.get('dog', 0) + 1
liczniki['dog'] = liczniki.get('dog', 0) + 1
print(liczniki)

# Frozen set

x = frozenset([1, 2, 1, 1])

# namedtuple

from collections import namedtuple

osoba = namedtuple("Osoba", ['imie', 'nazwisko', 'rok_ur'] )

os1 = osoba(imie="Rafał", nazwisko="Korzeniewski", rok_ur=1980)

print(os1)
print(type(os1))
print(os1.imie)
print(os1.nazwisko)

print(dir(os1))
print(os1.index("Rafał"))
print(os1[0])
