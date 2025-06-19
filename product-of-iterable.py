def mul(numbers):
    existsZero = 0 in numbers
    if existsZero:
        return 0

    res = 1
    for i in numbers:
        res = res * i

    return res

print(mul([1, 2, 3]))  # prints 6
print(mul([0, 1, 2, 3]))  # prints 0
print(mul([2, 3, 4]))  # prints the result of 2 * 3 * 4, being 24
print(mul([2, 3, 4]) + mul([1, 2]))  # prints the result of 2×3×4 + 1×2, which is 26
