import unicodedata

s1 = "é"  # U+00E9
s2 = "e\u0301"  # U+0065 + U+0301

print(s1 == s2)  # False
print(unicodedata.normalize('NFC', s1) == unicodedata.normalize('NFC', s2))  # True
