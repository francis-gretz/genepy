import numpy as np


def apply_gravity(sandpile):
    avalanche = True

    while avalanche:
        avalanche = False

        for y in range(sandpile.shape[0]):
            if avalanche:
                break

            for x in range(sandpile.shape[1]):
                if avalanche:
                    break

                if sandpile[y, x] >= 4:
                    avalanche = True

                    sandpile[y-1, x] += 1
                    sandpile[y+1, x] += 1
                    sandpile[y, x-1] += 1
                    sandpile[y, x+1] += 1

                    sandpile[y, x] -= 4


sandpile = np.zeros((5, 5), dtype=np.uint32)
sandpile[2, 2] = 16

print(sandpile)

apply_gravity(sandpile)

print(sandpile)
# [[0 0 1 0 0]
#  [0 2 1 2 0]
#  [1 1 0 1 1]
#  [0 2 1 2 0]
#  [0 0 1 0 0]]
