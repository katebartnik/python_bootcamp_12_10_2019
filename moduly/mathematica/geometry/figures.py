import math

FI = 1.61
operatory = ["*", "+", "-"]


# Napisz funkcje, które:
# 1. Policzy pole kwadratu
def pole_kwadratu(a):
    return a ** 2


# 2. Policzy pole prostokata
def pole_prostokata(a, b):
    return a * b


# 3. policzy pole trójkata
def pole_trojkata(a, h):
    return a * h / 2


# 4. policzy pole koła. Niech domyślni promien wynosi 1
def pole_kola(r=1):
    return math.pi * r ** 2

