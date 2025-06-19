def find_consecutive_sum(n):
    adjacent_numbers = 3

    if n == 0:
        numbers = [-1, 0, 1]
        return tuple(numbers)

    for i in range(n - adjacent_numbers + 1):
        sum = 0

        numbers = []
        for j in range(adjacent_numbers):
            number = i + j
            numbers.append(number)
            sum += number

        if sum == n:
            return tuple(numbers)

    return None


res = find_consecutive_sum(0)
print(res)
# (-1, 0, 1)

res = find_consecutive_sum(15)
print(res)
# (4, 5, 6)

res = find_consecutive_sum(10)
print(res)
# None
