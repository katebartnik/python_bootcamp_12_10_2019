import matematyka
import sys

print(sys.path)

print(matematyka.pole_kwadratu(2))

print(r"\nowe")

from matematyka import pole_kwadratu, pole_kola, FI, operatory
print(pole_kwadratu(2))

from matematyka import *
from algebra import *

from matematyka import dodaj_macierze as dodawanie1
from algebra import dodaj_macierze as dodawanie2

print(dodawanie1([[1, 2]], [[3, 4]]))
print(dodawanie2([[1, 2]], [[3, 4]]))
