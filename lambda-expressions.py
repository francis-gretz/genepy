def filtered(items, func):
    return filter(func, items)


items = list(range(101))

res = filtered(items, lambda x: x % 3 == 0)
print(", ".join(map(str, res)))

res = filtered(items, lambda x: x % 5 == 0)
print(", ".join(map(str, res)))

res = filtered(items, lambda x: x % 15 == 0)
print(", ".join(map(str, res)))
