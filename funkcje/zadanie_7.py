"""
Rozwiązywanie równań kwadratowych

"""
# pip install matplotlib
# pip install plotly


import math
import pytest
import plotly

def delta(a, b, c):
    return b ** 2 - 4 * a * c


def miejsca_zerowe(a, b, c):
    d = delta(a, b, c)

    if d < 0:
        raise ValueError("Brak miejsc zerowych")
    if d == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2


import plotly.graph_objects as go


x = list(range(-10, 10))
y = [2*i**2 + 2*i -20 for i in x]

fig = go.Figure(data=go.Scatter(x=x, y=y))
fig.show()


def test_delta():
    assert delta(1, 0, 0) == 0
    assert delta(1, 1, 1) == -3
    assert delta(2, 2, -2) == 20


def test_miejsca_zerowe():
    with pytest.raises(ValueError):
        miejsca_zerowe(1, 1, 1)
    assert miejsca_zerowe(1, 0, 0) == 0
    assert miejsca_zerowe(2, 2, -2) == (0.6180339887498949, -1.618033988749895)
