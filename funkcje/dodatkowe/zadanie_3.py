"""
# Zad 3

Napisz funkcję, która sprawdzi czy podany napis jest palindromem

"""

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

def is_palindrome(text):
    text = text.lower()
    left_position = 0
    right_position = len(text) - 1

    while right_position > left_position:
        if not text[left_position] == text[right_position]:
            return False
        left_position += 1
        right_position -= 1
    return True

def test_is_palindrome():
    assert is_palindrome("aza") == True
    assert is_palindrome("azA") == True
    assert is_palindrome("Raz") == False