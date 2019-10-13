
wynik = []
for i in range(1, 101):
    wynik.append(i**3)

print(wynik)

wynik = [i**3 for i in range(1, 101)]
wynik2 = {i**3 for i in range(1, 101)}
wynik3 = (i**3 for i in range(1, 101))

print(wynik)
print(wynik2)
print(wynik3)
print(tuple(wynik3))


wynik = [i**3 for i in range(1, 101) if i % 7 == 0]
print(wynik)

wynik = [(i, i**2, i**3) for i in range(1, 101) if i % 7 == 0]
print(wynik)


lista = ["aa", "aaaaa", "aaa", "aaaaaaa"]
print([len(x) for x in lista])


macierz = [[x*y for x in range(10)] for y in range(10)]
print(macierz)