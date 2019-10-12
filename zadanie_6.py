import random

DEBUG = False
# losuje pozycję skarbu
skarb_x = random.randint(1, 10)
skarb_y = random.randint(1, 10)

# losuję pozycję gracza
gracz_x = random.randint(1, 10)
gracz_y = random.randint(1, 10)

# minimalna liczba ruchow po wylosowaniu

min_l_po_wyl = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
liczba_ruchow = 0

if DEBUG:
    print("Położenie gracza:", gracz_x, gracz_y)
    print("Położenie skarbu:", skarb_x, skarb_y)
    print(min_l_po_wyl)

while True:
    if DEBUG:
        print("Aktualne położenie gracza")
        print("Położenie gracza:", gracz_x, gracz_y)

    min_l_przed = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    ruch = input("Wykonaj ruch w(góra) a(lewo) s(dół) d(prawo): ")
    if ruch == "w":
        gracz_y += 1
    if ruch == "s":
        gracz_y += -1
    if ruch == "a":
        gracz_x += -1
    if ruch == "d":
        gracz_x += 1

    min_l_po = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
    if gracz_x > 10 or gracz_x < 1 or gracz_y > 10 or gracz_y < 1:
        print("Poza planszą!!")
        break

    if skarb_x == gracz_x and skarb_y == gracz_y:
        print("Znalazłeś Skarb!! Brawo")
        break

    if random.randint(1, 5) != 3:
        if min_l_po < min_l_przed:
            print("Ciepło")
        else:
            print("Zimno")

    liczba_ruchow += 1
    if liczba_ruchow > 2 * min_l_po_wyl:
        # losuje pozycję skarbu
        skarb_x = random.randint(1, 10)
        skarb_y = random.randint(1, 10)
        min_l_po_wyl = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
        liczba_ruchow = 0
        print("Jestes gapa. Skarb zmienił swoje położenie!")
