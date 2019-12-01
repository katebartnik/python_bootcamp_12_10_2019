from collections import namedtuple

Samochod = namedtuple("Samochod", ["rocznik", "silnik", "max_predkosc"])

audi = Samochod(rocznik=2010, silnik="diesel", max_predkosc=220)
# mercedes = Samochod(rocznik=1987, silnik="diesel")

print(audi)
print(audi.rocznik)

from collections import defaultdict

tradycyjny = {}
licznik = defaultdict(int)

licznik["a"] += 1
print(licznik)

# tradycyjny['a'] += 1

from collections import deque

# help(deque)

x = deque()

x.append(10)
x.append(20)

print(x)

for i in x:
    print(i)

x.appendleft(30)
print(x)

import collections
print(dir(collections))