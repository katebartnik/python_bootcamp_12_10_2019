dane = {"login": "admin", "haslo": "123"} # ** login="admin", haslo="123"
lista = ["admin", "1234"]  # * "admin", "1234"

def zaloguj(login, haslo):
    print(f"Zalogowany, login:{login}, hasło: {haslo}")

zaloguj("admin", "123")
zaloguj(haslo="123",login="admin")

zaloguj(login=dane['login'], haslo=dane['haslo'])
zaloguj(**dane)
zaloguj(*lista)


