import unicodedata


def remove_diacritics(text):
    result = []

    normalized = unicodedata.normalize("NFD", text)

    for char in normalized:
        if not char.isalnum():
            continue

        combining = unicodedata.combining(char)
        if combining == 0:
            result.append(char.lower())

    result.sort()

    return result


def is_anagram(left, right):
    leftClean = remove_diacritics(left)
    rightClean = remove_diacritics(right)
    return leftClean == rightClean


s1 = "Madam Curie"
s2 = "Radium,?   came"
print(s1)
print(s2)
print(is_anagram(s1, s2))
print()

s1 = "funeral"
s2 = "real fun"
print(s1)
print(s2)
print(is_anagram(s1, s2))
print()
