
# def wiecej_niz(text, ilosc_znakow):
#     liczniki = {}
#     wynik = set()
#     for znak in text:
#         liczniki[znak] = liczniki.get(znak, 0) + 1
#
#     for znak in liczniki:
#         if liczniki[znak] > ilosc_znakow:
#             wynik.add(znak)
#
#     return wynik
#
# def wiecej_niz(text, ilosc_znakow):
#
#     wynik = set()
#     for znak in set(text):
#         if text.count(znak) > ilosc_znakow:
#             wynik.add(znak)
#
#     return wynik


def wiecej_niz(text, ilosc_znakow):
    return {x for x in text if text.count(x) > ilosc_znakow}



def test_wiecej_niz_dla_pustego_napis():
    assert wiecej_niz('', 3) == set()

def test_wiecej_niz():
    assert wiecej_niz('ala ma kota a kot ma ale', 3) == {'a', ' '}