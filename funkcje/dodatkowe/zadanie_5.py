
import string
print(string.ascii_lowercase)
print(len(string.ascii_lowercase))


def ispangram(text, alphabet = string.ascii_lowercase):
    alphabet = set(alphabet)
    text = set(text.lower())
    text.remove(" ")
    # print(alphabet-text)
    return text == alphabet

polish_alphabet = "ąęćńóśźżł" + string.ascii_lowercase.replace("x", '').replace("v", "").replace('q', "")

def test_ispangram():
    assert ispangram('The quick brown fox jumps over the lazy dog') == True
    assert ispangram("Ala ma kota") == False
    assert ispangram("Śnij formę klech z wag bądź żółć pustyń", alphabet = polish_alphabet) == True

