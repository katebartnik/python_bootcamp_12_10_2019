print(dir())
# To jest moj pierwszy program
# podstawowe typy numeryczne

x = 1 # x - zmienna, nazwa, referencja. 1 - obiekt, wartosc 

print(x)  # uzywam funkcji print do wypisania wartosc na ktora
          # wskazuje referencja x
print(x+1)

# nazwy nie mogą zaczynać się od cyfry
# mogą składać z liter, cyfr i znakow podkreslenia _
# poprawne nazwy to np: x, dziecko, wartosc_1
# niepoprawne to: 1zmienna, wartosc.1, 

##############################
#							 #
# Podstawowe typy numeryczne # 
#							 # 	
##############################

# Liczby całkowite - integer - nazwa typu: int
int
# () po jakieś nazwie to sposób na wywołanie
#  np funkcji. Takie obiekty są callable 

# podstawowe operatory na liczbach:
# + - * / ** pow // %
print(1 + 2)
print(3 - 4)
print(5 * 5)
print(5 / 2)
print(5 // 2)
print(10 % 7)
print(10 ** 2)
print(pow(10, 2))

# wartosci boolowskie
# nazwa typu: bool
# False, True
# operatory logiczne:
# and or not
# Samodzielnie - poczytaj o wartościach logicznych

# Type None
x = None

# operatory porówniania
# ==, > , <, !=, >=, <=, is
# przykłady
x = 4
y = 12
print(x == y) # False`
print(x > y)  # False
print(x != y) # True
#...

# Liczby zmiennoprzecinkowe. 
# nazwa typu: float
# min = 1e-324
# max = 1e308

# liczby zespolone
# nazwa typu: complex

# kolejnosc operacji - PEDMAS
# https://stackoverflow.com/questions/48937457/how-do-order-of-operations-go-on-python

3 * 4 / 2 + 2
# kolejnosc w logice
# () not and or

print(int(2.8))
print(round(2.8, 0))

## zbadaj funkcję print
##  help(print) - poeksperymentuj z parametrami

## Napisy -
# typ: str

print("To jest napis")
x = "To \"jest\" napis\n"   # \ to jest znak ucieczki
y = 'To też "jest" napis\n' # \n - znak nowej linii
z = '''To\tjest  # \\t to jest znak tabulacji
napis
wielolinijkowy'''
print(x, y, z)

# co można robić z napisami?
# napisy można łączyć

x = "Napis pierwszy"
y = "Drugi napis"

print(x+y)
# napis mnożyć

print("#"*40)

# napisy można formatować
template = "{} {} {}"
print(template.format(10, 20, 30))

x = 10
y = 20
z = 30

# formatowanie z f-stringami
print(f"x = {x}, y = {y}, z={z}, x+y = {x+y}")
pi = 3.1415
r = 7

print(f"""
normalnie {pi} x
szerokosc 10 {pi:10} x
szerokosc 10 {pi:<10} x
szerokosc 10 {pi:^10} x
zaokraglenie {pi:.2f} x
""")

# mozemy napisy przeksztalcac
print(help(dir))
print(dir())
print(globals())
print(locals())
print(dir(1))
print(dir(""))

x = "ala ma kotala, ala"
print(x.upper())
print(x.title())
print(x.replace("ala", "Aleksandra"))
print(x.startswith("ala"))

## Wyrażenia warunkowe

x = 1
y = 2

if x < y:
    print("Jedna odnoga programu")
elif x == y:
    print("druga odnoga")
else:
    print("Pozostałe przypadki..")


