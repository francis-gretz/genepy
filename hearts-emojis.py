import unicodedata

# Loop through a reasonable range of Unicode characters
for codepoint in range(0x110000):  # Unicode range ends at 0x10FFFF
    char = chr(codepoint)
    name = unicodedata.name(char, "")  # Default to '' to avoid exceptions
    if "HEART" in name:
        print(char, end="")

print()  # Optional: add newline at the end
