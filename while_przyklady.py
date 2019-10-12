

while True:
    print("Zapętliłem się ")
    break  # wychodzi z pętli

i = 0
while i < 10:
    print(i, "Pętla")
    i += 1  # i = i + 1

print("#"*40)

i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i, "Pętla")
    i += 1  # i = i + 1
