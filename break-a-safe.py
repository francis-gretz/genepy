digits = {1, 5, 8}

for itemA in digits:
    for itemB in digits:
        for itemC in digits:
            for itemD in digits:
                safe = {itemA, itemB, itemC, itemD}

                if 1 in safe and 5 in safe and 8 in safe:
                    print(f"{itemA} {itemB} {itemC} {itemD}")


## ChatGPT refactor of the above code

# from itertools import product

# digits = {1, 5, 8}

# for combo in product(digits, repeat=4):
#     if {1, 5, 8}.issubset(combo):
#         print(*combo)
