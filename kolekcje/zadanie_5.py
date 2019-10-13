"""
policz samogłoski w podanym przez uzytkownika napisie

samogłoski -> aeiouy
'a' in 'aeiouy' -> True

"""
SAMOGLOSKI = "aeiouy"

text = input("Podaj text: ")

licznik = 0
for litera in text:
    if litera in SAMOGLOSKI:
        licznik += 1

print(f"Znaleziono {licznik} samogłosek")
