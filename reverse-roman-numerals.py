from enum import Enum

class NumberToRoman(Enum):
    1           ="I"
    5           ="V"
    10          ="X"
    50          ="L"
    100         ="C"
    500         ="D"
    1000        ="M"

def from_roman_numeral(roman_numeral):
    remaining = 0

    romans = list()    

    for n2r in NumberToRoman:
        value = int(n2r.name)
        roman = n2r.value
        
        if (remaining >= value):
            x = remaining // value
            remaining = remaining % value

            for i in range(1, x +1):
                romans.append(roman)

    return romans

print(from_roman_numeral("V"))
print(from_roman_numeral("XX"))
print(from_roman_numeral("DCCC"))
print(from_roman_numeral("CD"))
print(from_roman_numeral("MMMM"))
