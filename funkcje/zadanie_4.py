def formatuj(*args, **kwargs):
    text = "\n".join(args)
    for k, v in kwargs.items():
        text = text.replace("$"+k, str(v))
    # for k in kwargs:
    #     text = text.replace("$"+k, str(kwargs[k]))
    return text


def test_formatuj():
    assert formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena=10,
    ) == 'koszt 10 PLN\nkwota 10 brutto'

    assert formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        'podatek vat $vat %',
        cena=10,
        vat=19
    ) == 'koszt 10 PLN\nkwota 10 brutto\npodatek vat 19 %'
