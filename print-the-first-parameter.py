import sys

if len(sys.argv) == 2:
    first_param = sys.argv[1]
else:
    first_param = "usage: python3 solution.py PARAM"

print(first_param)
