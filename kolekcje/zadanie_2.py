"""
Napisz program zliczajacy wystąpienia liczb:
 dodatnich i ujemnych
 parzystych i nieparzystych
 w zadanej liscie

lista = [1, 2, 3, 4, -1, -2, -3, -4]
<kod programu>

dodatnich: <x>
ujemnych: <y>
parzystych: <z>
nieparzystych: <e>


"""

lista = [1, 2, 3, 4, -1, -2, -3, -4, 1 , 1 , 1]
liczby_dodatnie = []
liczby_ujemne = []
liczby_parzyste = []
liczby_nieparzyste = []

for element in lista:
    if element > 0:
        liczby_dodatnie.append(element)
    elif element < 0:
        liczby_ujemne.append(element)
    if element % 2 == 0:
        liczby_parzyste.append(element)
    elif element % 2 != 0:
        liczby_nieparzyste.append(element)


print(f"""
Dodatnich: {len(liczby_dodatnie)}
Ujemnych: {len(liczby_ujemne)}
Parzystych: {len(liczby_parzyste)}
Nieparzystych: {len(liczby_nieparzyste)}
""")
