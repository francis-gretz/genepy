import random


def pwgen(length: int, with_digits: bool = True, with_uppercase: bool = True):
    s = []

    if with_digits:
        s.append(chr(random.randint(48, 57)))  # ascci for 0 .. 9

    if with_uppercase:
        s.append(chr(random.randint(65, 90)))  # ascci for A .. Z

    for _ in range(length - len(s)):
        s.append(chr(random.randint(97, 122)))  # ascci for a .. z

    random.shuffle(s)

    return "".join(s)


print(pwgen(10, True, True))
print(pwgen(10, True, False))
print(pwgen(10, False, True))
print(pwgen(10, False, False))
