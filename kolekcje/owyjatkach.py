
#

try:
    1/0
    tutajcosrobimy
except:
    print("Był jakiś wyjątek")


try:
    # int("a")
    # 1/0
    tutajcosrobimy

except ZeroDivisionError:
    #int("a")
    print("Dzieliłeś przez zero - wstydz sie")
except NameError as e:
    print(e)
    print("tego jeszcze nie zdefiniowales")
except:
    print("Poleciało coś innego")
finally:
    print("To sie wykona zawsze")

print(isinstance("napis", str))
# print(isinstance(ZeroDivisionError, BaseException))

odp = input("wpisz x by rzucic wyjatek")

class MojException(Exception):
    pass

try:
    if odp == "x":
        raise MojException("To jest mój wyjatek. X powoduje wyjatek")
except MojException:
    print("Obsłużyłem własny wyjatek")