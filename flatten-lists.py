def flatten_internal(elem):
    if isinstance(elem, list):
        if len(elem) == 0:
            return ""

        sub_list = ""
        for sub_element in elem:
            se = flatten_internal(sub_element)
            st = str(se)
            sub_list = concatenate(sub_list, st)

        return sub_list
    else:
        st = str(elem)
        if len(st) > 0:
            return st
        else:
            return ""


def concatenate(flat_list, st):
    if len(st) > 0:
        if flat_list != "":
            flat_list = f"{flat_list},{st}"
        else:
            flat_list = st

    return flat_list


def flatten(a_list):
    if a_list == []:
        return []

    flat_list = ""
    for xs in a_list:
        fl = flatten_internal(xs)
        st = str(fl)
        flat_list = concatenate(flat_list, st)

    a = flat_list.split(",")
    res = list(map(int, a))

    return res


# input = []
input = [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]
print(f"input: {input}")

res = flatten(input)
print(f"output: {res}")
