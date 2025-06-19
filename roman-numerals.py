number_to_roman = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}


def to_roman_numeral(number):
    remaining = number

    romans = list()

    for value in number_to_roman:
        roman = number_to_roman[value]

        if remaining >= value:
            x = remaining // value
            remaining = remaining % value

        # for i in range(1, x + 1):
            romans.append(roman * x)

    return "".join(romans)


print(to_roman_numeral(4))
print(to_roman_numeral(9))

print(to_roman_numeral(3333))

print(to_roman_numeral(1))
print(to_roman_numeral(2))
print(to_roman_numeral(8))
print(to_roman_numeral(16))
print(to_roman_numeral(32))
