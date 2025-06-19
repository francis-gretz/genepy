def internal_bencode(object) -> str:
    if isinstance(object, str):
        return encodeStr(object)

    if isinstance(object, int):
        return encodeInt(object)

    if isinstance(object, list):
        return encodeList(object)

    if isinstance(object, dict):
        return encodeDict(object)

    return ["SHIT"] ** 5


def get_bytes(text: str) -> bytes:
    return bytes(text, 'utf-8')


def bencode(object) -> bytes:
    return bytes(internal_bencode(object), 'utf-8')


def encodeStr(string: str) -> str:
    length = len(string)

    return f"{length}:{string}"


def encodeInt(integer: int) -> str:
    return f"i{integer}e"


def encodeList(list: list) -> str:
    itemsEncoded = []

    for item in list:
        itemsEncoded.append(internal_bencode(item))

    items = "".join(itemsEncoded)

    return f"l{items}e"


def encodeDict(dictionary: dict) -> str:
    itemsEncoded = []

    sorted_dict = dict(sorted(dictionary.items()))

    for k, v in sorted_dict.items():
        itemsEncoded.append(internal_bencode(k))
        itemsEncoded.append(internal_bencode(v))

    items = "".join(itemsEncoded)

    return f"d{items}e"


def bdecode(object: bytes):
    return internal_bencode(object.decode("utf-8"))


def internal_decode(encoded: str):
    match encoded[0]:
        case "i":
            return internal_decode_int(encoded)

        case "l":
            return internal_decode_list(encoded)

        case "d":
            return internal_decode_dict(encoded)

        case _:
            return internal_decode_str(encoded)


def internal_decode_int(encoded: str) -> int:
    return int(encoded[1:-1])


def internal_decode_str(encoded: str) -> str:
    parts = encoded.split(":")
    return parts[1]


def internal_decode_list(encoded: str) -> str:
    items = encoded[1:-1]

    list = []

    decodedItems = internal_decode_list_items(items)
    for decodedItem in decodedItems:
        list.append(decodedItem)

    return list


def internal_decode_list_aux(encoded: str) -> str:
    items = encoded[1:-1]

    list = []

    decodedItems = internal_decode_list_items(items)
    for decodedItem in decodedItems:
        list.append(decodedItem)

    return list


def internal_decode_dict(encoded: str) -> str:
    items = encoded[1:-1]

    list = {}

    decodedItems = internal_decode_list_items(items)
    for decodedItem in decodedItems:
        list.append(decodedItem)

    return list


def internal_decode_dict_aux(encoded: str) -> str:
    items = encoded[1:-1]

    list = {}

    decodedItems = internal_decode_list_items(items)
    for decodedItem in decodedItems:
        list.append(decodedItem)

    return list


def internal_decode_dict_item(encoded: str):
    if len(encoded) == 0:
        return None

    decodedItems = internal_decode_list_items(items)
    for decodedItem in decodedItems:
        list.append(decodedItem)

    return list


def internal_decode_list_items(encoded: str):
    if len(encoded) == 0:
        return None

    match encoded[0]:
        case "i":
            return internal_decode_int_aux(encoded)

        case "l":
            return internal_decode_list_aux(encoded)

        case "d":
            return internal_decode_dict_aux(encoded)

        case _:
            return internal_decode_str_aux(encoded)


def internal_decode_int_aux(encoded: str) -> int:
    index = encoded.find("e")

    first_result = [int(encoded[1:index])]
    rest_of_message = encoded[index+1:]

    next_result = internal_decode_list_items(rest_of_message)
    return list[first_result, next_result]


def internal_decode_str(encoded: str) -> str:
    index = encoded.find(":")

    length = int(encoded[:index])
    lastIndex = index+1+length
    first_result = [encoded[index+1:lastIndex]]
    next_result = internal_decode_list_items(encoded[lastIndex+1:])
    return list[first_result, next_result]


def internal_decode_str_aux(encoded: str) -> str:
    index = encoded.find(":")

    length = int(encoded[:index])
    lastIndex = index+length+1

    first_result = [encoded[index+1:lastIndex]]
    rest_of_message = encoded[lastIndex:]

    next_result = internal_decode_list_items(rest_of_message)
    return list[first_result, next_result]


# res = encodeStr("hello world!")
# print(res)

# res = encodeStr("")
# print(res)

# res = encodeStr("internal_bencode")
# print(res)


encoded = "d7:meaningi42e4:wiki7:bencodee"
result = internal_decode(encoded)
print(result)
