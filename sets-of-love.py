def love_meet(bob, alice):
    bob_set = list(set(bob))
    alice_set = list(set(alice))

    res = set(list(filter(lambda x: x in bob_set, alice_set)))
    return res


def not_meet(list_a, list_b):
    set_a = list(set(list_a))
    set_b = list(set(list_b))

    res = set(list(filter(lambda x: x not in set_b, set_a)))
    return res


def affair_meet(bob, alice, silvester):
    a_s = love_meet(alice, silvester)
    res = not_meet(a_s, bob)
    return res


alice = ["Ⅱ", "Ⅳ", "ⅩⅠⅩ", "ⅩⅤ", "Ⅳ", "Ⅱ"]
bob = ["Ⅳ", "Ⅲ", "Ⅱ", "ⅩⅩ", "Ⅱ", "ⅩⅩ"]
silvester = ["ⅩVⅢ", "ⅩⅠⅩ", "Ⅲ", "Ⅰ", "Ⅲ", "ⅩVⅢ"]

love = love_meet(bob, alice)
print(f"love: {love}")
# Out[4]: {'Ⅱ', 'Ⅳ'}

affair = affair_meet(bob, alice, silvester)
print(f"affair: {affair}")
