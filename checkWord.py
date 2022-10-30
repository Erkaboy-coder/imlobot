from uzwords import words
from difflib import get_close_matches

def checkWord(word, words=words):
    word = word.lower()

    matches = set(get_close_matches(word,words))
    available = False #bu so'z mavjud emas

    if word in matches:
        available = True #mavjud
        matches = word
    elif 'ҳ' in words:
        word = word.replace('x','ҳ')
        matches.update(get_close_matches(word,words))
    elif 'x' in words:
        word = word.replace('ҳ','x')
        matches.update(get_close_matches(word,words))

    return {'available':available,'matches':matches}


# print(get_close_matches('ҳўшшаймоқ',words))
