x = int(input("Podaj współrzędną x: "))
y = int(input("Podaj współrzędną y: "))
# x, y = 100, 100
# ctrl alt l - formatuje kod zgodnie z PEP8
if x > 100 or y > 100 or x < 0 or y < 0:
    print("Jestes poza planszą")
elif x > 90 and y > 90:
    print("Jesteś w PGR")
elif x > 90 and y < 10:
    print("Jesteś w PDR")
elif x < 10 and y > 90:
    print("Jesteś w LGR")
elif x < 10 and y < 10:
    print("Jesteś w LDR")
elif x > 90:
    print("Jestes na PK")
elif x < 10:
    print("Jestes na LK")
elif y > 90:
    print("Jestes na GK")
elif y < 10:
    print("Jestes na DK")
else:
    print("Jesteś w Centrum")
