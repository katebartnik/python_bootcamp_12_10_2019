
def policz_znaki(napis, start="<", end=">"):
    licznik = 0
    poziom = 0
    for znak in napis:
        if znak == start:
            poziom += 1
        elif znak == end:
            poziom -= 1
        else:
            licznik += poziom
    return licznik

def test_policz_znaki_empty_string():
    assert policz_znaki("") == 0

def test_policz_znaki_dodatkowe_nawiasy():
    assert policz_znaki("", "[", "]") == 0

def test_policz_znaki_1_poziom_zaglebienia():
    assert policz_znaki("<a>") == 1
    assert policz_znaki("<aaa>") == 3
    assert policz_znaki("<aaa> <bbb>") == 6

def test_policz_znaki_2_poziomy_zaglebienia():
    assert policz_znaki("<<a>>") == 2
    assert policz_znaki("<a<a<a>>>") == 6
    assert policz_znaki("[a[a[a]a]a]","[", "]") == 9


# >> > policz_znaki('ala ma <kota> a kot ma ale')
# 4
# >> > policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']')
# 18
# >> > policz_znaki('a <a<a<a>>>')
# 6
# Materiał