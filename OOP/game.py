"""
1. Stwórz klasę Postac - niech ma atrybuty: imie, zycie, sila
2. Stwórz klasę Przedmiot - niech ma atrybuty: bonus_do_ataku, bonus_do_obrony, nazwa, miejsce
3. Postac ma atrybut atak wyliczany na podstawie sily i bonusow od przedmiotow
4. Stworz funkcje obslugujaca grę
5. Powinna na w niej byc jakas plansza o wymiarach x, y
6. na planszy moga pojawi sie jakies przedmioty czy inne postaci
7. jak wejdziemy na pole z przedmiotem to go bierzemy o ile ekwipunek pozwoli
8. gdy trafimy na inna postac to wywiazuje sie walka
"""
import random


class Postac:
    def __init__(self, imie, zycie, sila):
        self.imie = imie
        self.zycie = zycie
        self.sila = sila
        self.ekwipunek = []

    @property
    def atak(self):
        base = self.sila + sum([x.bonus_do_ataku for x in self.ekwipunek])
        return int(base * random.random())

    def wez_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def obrazenia(self, sila):
        self.zycie -= sila

    @property
    def zyje(self):
        return self.zycie > 0

    def __str__(self):
        return f"{self.imie}, zyje={self.zyje}"


class Przedmiot:
    def __init__(self, nazwa, bonus_do_ataku, bonus_do_obrony, miejsce):
        self.nazwa = nazwa
        self.bonus_do_ataku = bonus_do_ataku
        self.bonus_do_obrony = bonus_do_obrony
        self.miejsce = miejsce


class Polozenie:
    def __init__(self, x, y, zasieg_x, zasieg_y):
        self.x = x  # polozenie na osi x
        self.y = y
        self.zasieg_x = zasieg_x
        self.zasieg_y = zasieg_y

    def __str__(self):
        return f"Pozycja x={self.x}, y={self.y}"

    def gora(self):
        self.y += 1
        if self.y > self.zasieg_y:
            print("Wypadłeś poza planszę")
            exit()

    def dol(self):
        self.y -= 1
        if self.y < 0:
            print("Wypadłeś poza planszę")
            exit()

    def lewo(self):
        self.x -= 1
        if self.x < 0:
            print("Wypadłeś poza planszę")
            exit()

    def prawo(self):
        self.x += 1
        if self.x > self.zasieg_x:
            print("Wypadłeś poza planszę")
            exit()

class Plansza:

    def __init__(self, gracz, bot, przedmiot, x=10, y=10):
        self.x = x  # wymiar planszy wzdłuż osi x
        self.y = y
        self.gracz = gracz
        self.bot = bot
        self.przedmiot = przedmiot
        self.polozenie_gracza = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)
        self.polozenie_bota = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)
        self.polozenie_przedmiotu = Polozenie(random.randint(1, 10), random.randint(1, 10), x, y)

    def ruch(self):

        kierunek = input("Podaj kierunek g, d, l, p")
        # if kierunek == "g":
        #     self.polozenie_gracza.gora()
        # elif kierunek == "d":
        #     self.polozenie_gracza.dol()
        # elif kierunek == "l":
        #     self.polozenie_gracza.lewo()
        # elif kierunek == "p":
        #     self.polozenie_gracza.prawo()

        ruch = {
            'g':self.polozenie_gracza.gora,
            'd': self.polozenie_gracza.dol,
            'l': self.polozenie_gracza.lewo,
            'p': self.polozenie_gracza.prawo
        }
        ruch[kierunek]()

    def gra(self):
        self.polozenie_bota = self.polozenie_gracza
        if self.polozenie_gracza == self.polozenie_bota:
            while self.gracz.zyje and self.bot.zyje:
                obrazenia = self.gracz.atak
                print(f"{self.gracz.imie} zadaje obrażenia za {obrazenia}")
                self.bot.obrazenia(obrazenia)
                if self.bot.zyje:
                    obrazenia = self.gracz.atak
                    print(f"{self.bot.imie}  przeżył i oddaje za {obrazenia}")
                    self.gracz.obrazenia(obrazenia)

            print(hero1, hero2)


hero1 = Postac("Superman", 200, 200)
hero2 = Postac("Hulk", 200, 200)
przedmiot = Przedmiot("Miecz", 30, 15, 4)

plansza = Plansza(hero1, hero2, przedmiot)
plansza.gra()

