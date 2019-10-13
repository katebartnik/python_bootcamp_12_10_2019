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
