def collatz_length(n):
    sequence_length = 0

    while n != 1:
        sequence_length += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1

    return sequence_length


# The collatz sequence goes like this:

# Start by any number greater than zero.
# If your number is even, divide it by two.
# If your number os odd, multiply by three and add one.
# For example, starting by 10 we have:

# 1
# 10 → 5 → 16 → 8 → 4 → 2 → 1

res = collatz_length(10)
print(res)
