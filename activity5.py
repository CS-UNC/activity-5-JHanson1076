# activity5.py

def more_than_20(file):
    "Returns a list of all words from the file that have > than 20 characters."
    words = []
    with open(file, 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) > 20:
                words.append(word)
    return words


def has_no_e(word):
    "Returns True if the word contains no 'e', otherwise Fail false."
    return 'e' not in word


def uses_only(word, letters):
    "Returns True if word only uses characters from letters else False."
    for ch in word:
        if ch not in letters:
            return False
    return True


def all_uses_only(file, letters):
    "Returns list of all words from file that only use given letters."
    result = []
    with open(file, 'r') as f:
        for line in f:
            word = line.strip()
            if uses_only(word, letters):
                result.append(word)
    return result
