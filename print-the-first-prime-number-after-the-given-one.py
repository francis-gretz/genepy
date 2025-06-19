import math


def isPrime(number):
    if number == 1:
        return False
    if number == 2:
        return True

    maxDivisor = int(math.ceil(math.sqrt(number))) + 1
    for x in range(2, maxDivisor):
        if number % x == 0:
            # print(f'{number} is not prime')
            return False
    # print(f'{number} is prime')
    return True


from itertools import count

for number in count(start=100000000, step=1):
    if isPrime(number):
        print(number)  # print statement
        break
