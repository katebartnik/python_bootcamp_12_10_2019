"""
W zadanym tekście zlicz wystąpienie każdego znaku
Nie używaj metody .count()
Dane przechowuj w słowniku
"""
# napis = "Kryptorurki kKk robaczne ramblowane poprzecznie"
# liczniki = {}
# for znak in napis.lower():
#     if znak != " ":
#         liczniki[znak] = liczniki.get(znak, 0) + 1
# print(liczniki)

from collections import defaultdict

napis = "Kryptorurki kKk robaczne ramblowane poprzecznie"
liczniki = defaultdict(int)
for znak in napis.lower():
    if znak != " ":
        liczniki[znak] += 1
print(liczniki)

#