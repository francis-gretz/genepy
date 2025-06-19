import math


def isPrime(number):
    if number == 1:
        return False
    if number == 2:
        return True

    maxDivisor = int(math.ceil(math.sqrt(number))) + 1
    for x in range(2, maxDivisor):
        if number % x == 0:
            return False
    return True


for number in range(222281, 222381):
    binary = bin(number)
    st = str(binary)

    number_of_ones = st.count("1")

    if isPrime(number_of_ones):
        print(number)
