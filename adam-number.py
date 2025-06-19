# An Adam number is a number that verifies this property: its square is the reverse of the square of its reverse.
import string

def check_adam_number(num):
    squareA = num**2
    st = str(num)
    reversed = st[::-1]
    numB = int(reversed)
    squareB = numB**2

    stA = str(squareA)
    stB = str(squareB)

    return stA[::-1] == stB


input = 31
res = check_adam_number(input)
print(f"input: {input}")
print(f"result: {res}")
# True

input = 22
res = check_adam_number(input)
print(f"input: {input}")
print(f"result: {res}")
# True

input = 15
res = check_adam_number(input)
print(f"input: {input}")
print(f"result: {res}")
# False