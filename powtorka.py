# int, float, complex, bool, str

# complex
print(1 + 2j + 2 + 3j)

# napisy "" '' """""" ''''''

print('a' in "abecadło")

#
help(print)

import example_random
print(help(example_random))

# operacje aryt
# +-/* // % **

# op logiczne
# and or not

# lista,     tupla, zbior, slownik
# [1, 2, 3]  ()     {}     {1: "a"}

# wyrażenie warunkowe
kozka_skakala = True
if kozka_skakala:
    print("Nożkę złamała")
elif 1 > 2:
    print("")
else:
    print("Nóżka zdrowa")

import example_random
print(example_random.randint(1, 10))