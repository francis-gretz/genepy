import string


def create_encrypt_cypher_dictionary(key):
    encrypt_cypher = dict()
    for iter in range(97, 123):
        new_key = (iter + key) % 123
        while new_key < 97:
            new_key = new_key + 97
        encrypt_cypher[chr(iter)] = chr(new_key)

    print(encrypt_cypher)
    return encrypt_cypher


def create_decrypt_cypher_dictionary(key):
    decrypt_cypher = dict()
    for iter in range(97, 123):
        new_key = (iter - key) % 123

        while new_key > 122 or new_key < 97:
            if new_key > 122:
                new_key = new_key - 122

            if new_key < 97:
                new_key = 26 + new_key  # 26 = 123 - 97

        decrypt_cypher[chr(iter)] = chr(new_key)

    print(decrypt_cypher)
    return decrypt_cypher


def caesar_cypher_encrypt(s, key):
    encrypt_cypher = create_encrypt_cypher_dictionary(key)

    result = ""
    for ch in s:
        if ch.isalpha() and ch.isascii():
            result = result + get_value_from_cypher(encrypt_cypher, ch)
        else:
            result = result + ch

    print(f"input : {s}")
    print(f"output: {result}")

    return result


def get_value_from_cypher(cypher: dict, s: string):
    encripted = cypher.get(s.lower(), "0")

    if s.isupper():
        return encripted.upper()
    else:
        return encripted


def caesar_cypher_decrypt(s, key):
    decrypt_cypher = create_decrypt_cypher_dictionary(key)

    result = ""
    for ch in s:
        if ch.isalpha() and ch.isascii():
            result = result + get_value_from_cypher(decrypt_cypher, ch)
        else:
            result = result + ch

    print(f"input : {s}")
    print(f"output: {result}")
    return result


# caesar_cypher_encrypt("st", 7)
# caesar_cypher_encrypt("abcdefghijklmnopqrstuvwxyz", 7)

# caesar_cypher_decrypt("abcdefghijklmnopqrstuvwxyz", 7)

# create_encrypt_cypher_dictionary(7)
# create_decrypt_cypher_dictionary(7)


# caesar_cypher_encrypt("Two empty halves of coconuts", 1)
# caesar_cypher_encrypt("Two empty halves of coconuts", 1)
caesar_cypher_decrypt("Uxp fnquz ibmwft pg dpdpovut", 1)
