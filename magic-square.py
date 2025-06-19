import numpy as np


class Pos:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x


class Result:
    def __init__(self, index: int, sum: int, isOk: bool, indexZeroes):
        self.index = index
        self.sum = sum
        self.isOk = isOk
        self.indexZeroes = indexZeroes

    def recalculate(self, square: np.array, magic_square_sum: int):
        mising = magic_square_sum - self.sum

        zeroPosition = self.indexZeroes.pop()
        square[zeroPosition.y, zeroPosition.x] = mising

        self.isOk = len(self.indexZeroes) == 0


def fill_magic_square(square: np.array) -> None:
    shape = square.shape

    rows = shape[0]

    get_sum_value(square, rows)


def get_sum_value(square: np.array, length: int) -> int:
    is_there_zero = len(np.where(square == 0)) > 0

    while is_there_zero:
        magic_square_sum = -1

        list_rows = []
        for row in range(length):
            list_rows.append(get_row_sum(square, length, row))

        list_cols = []
        for col in range(length):
            list_cols.append(get_col_sum(square, length, col))

        list_diag = []
        list_diag.append(get_diag_down_sum(square, length, 0))
        list_diag.append(get_diag_up_sum(square, length, 1))

        magic_square_sum = find_magics_square_sum(
            list_rows, list_cols, list_diag)

        for row in list_rows:
            check_zeroes(row, square, magic_square_sum)

        for col in list_cols:
            check_zeroes(col, square, magic_square_sum)

        for diag in list_diag:
            check_zeroes(diag, square, magic_square_sum)

        is_there_zero = np.any(square == 0)


def check_zeroes(row: Result, square: np.array, magic_square_sum: int):
    if row.isOk:
        return
    if len(row.indexZeroes) > 1:
        return

    recalculate(row, square, magic_square_sum)


def recalculate(row: Result, square: np.array, magic_square_sum: int):
    row.recalculate(square, magic_square_sum)

def find_magics_square_sum(list_rows, list_cols, list_diag):
    for x in list_rows:
        if x.isOk:
            return x.sum

    for x in list_cols:
        if x.isOk:
            return x.sum

    for x in list_diag:
        if x.isOk:
            return x.sum


def get_row_sum(square: np.array, rows: int, row: int) -> Result:
    result = 0
    isOk = True
    indexZeroes = []
    for col in range(rows):
        cell = square[row, col]

        if cell == 0:
            pos = Pos(row, col)
            indexZeroes.append(pos)
            isOk = False
        else:
            result += cell

    return Result(row, result, isOk, indexZeroes)


def get_col_sum(square: np.array, rows: int, col: int) -> Result:
    result = 0
    isOk = True
    indexZeroes = []
    for row in range(rows):
        cell = square[row, col]

        if cell == 0:
            pos = Pos(row, col)
            indexZeroes.append(pos)
            isOk = False
        else:
            result += cell

    return Result(col, result, isOk, indexZeroes)


def get_diag_down_sum(square: np.array, rows: int, diag: int) -> Result:
    result = 0
    isOk = True
    indexZeroes = []
    for row in range(rows):
        cell = square[row, row]

        if cell == 0:
            pos = Pos(row, row)
            indexZeroes.append(pos)
            isOk = False
        else:
            result += cell

    return Result(diag, result, isOk, indexZeroes)


def get_diag_up_sum(square: np.array, rows: int, diag: int) -> Result:
    result = 0
    isOk = True
    indexZeroes = []
    for col in range(rows):
        row = rows - 1 - col
        cell = square[row, col]

        if cell == 0:
            pos = Pos(row, col)
            indexZeroes.append(pos)
            isOk = False
        else:
            result += cell

    return Result(diag, result, isOk, indexZeroes)


harder_square = np.array([
    [4,  0, 15,  0],
    [9,  0,  6, 12],
    [5, 11, 10,  0],
    [16,  0,  0, 13],
])

fill_magic_square(harder_square)
print(harder_square)
