
"""
1. Utworz liste
2. w petli while wypisz wszystkie elementy listym (print).
Skorzystaj z len
3. zrob to samo bez len - poszukaj obslugi wyjatkow w pythonie
   try:
       cos tam
   except:
       cos jak jest wyjatek
"""

lista = [1,2,3,4,5]
i = 0
while i < len(lista):
    print(lista[i])
    i += 1

i = 0
while True:
    try:
        print(lista[i])
    except IndexError:
        break
    i += 1