
i = 0
suma = 0
while True:
    i += 1
    temp = int(input("Podaj temperaturę: "))
    suma += temp
    if i == 7:
        break

print("""Średnia wynosi:

{}

""".format(suma/i))