


def nowa_funkcja(func):
    def wrapper(*args, **kwargs):
        print("To jest powitanie")
        rezult = func(*args, **kwargs)
        return rezult

    return wrapper

@nowa_funkcja
def powitanie():
    print("Hello")

@nowa_funkcja
def be_awesome(name):
    print(f"Yo {name}. Be awesome!")

# powitanie = nowa_funkcja(powitanie)
# be_awesome = nowa_funkcja(be_awesome)


# "Ala ma kota"
# @bold
# "<b>Ala ma kota</b>"


# @italic
# "<i>Ala ma kota</i>"


# powitanie()
#
# be_awesome("Rafał")

powitanie()
be_awesome("Rafał")
