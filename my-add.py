import sys

if len(sys.argv) == 3:
    first_param = int(sys.argv[1])
    second_param = int(sys.argv[2])

    print(first_param + second_param)
else:
    first_param = "usage: python3 solution.py OP1 OP2"
    print(first_param)
