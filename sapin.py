import sys


class LevelData:
    def __init__(self, level: int, lines: int, min_width: int, max_width: int, tail_width: int):
        self.level = level
        self.lines = lines
        self.min_width = min_width
        self.max_width = max_width
        self.tail_width = tail_width

    def __str__(self):
        output = []
        output.append(f"level:{self.level}")
        output.append(f"lines:{self.lines}")
        output.append(f"min_width:{self.min_width}")
        output.append(f"max_width:{self.max_width}")
        output.append(f"tail_width:{self.tail_width}")

        return " - ".join(output)


def get_lines(level: int):
    if level <= 0:
        return 0
    return 3 + level


def max_width_tree(level: int):
    if level <= 0:
        return 0
    if level == 1:
        return 7
    else:
        lines = get_lines(level)
        return ((lines-2)*2) + max_width_tree(level-1)


def fir_tree(levelData: LevelData, max_width: int):
    width = levelData.min_width
    for _ in range(levelData.lines):
        print_character_n_times("*", max_width, width)
        width += 2


def print_tail(levelData: LevelData):
    width = levelData.tail_width
    max_width = levelData.max_width
    for _ in range(levelData.level):
        print_character_n_times("|", max_width, width)


def print_character_n_times(character_to_fil: str, max_width: int, width: int) -> str:
    line = character_to_fil * width
    print(justificate_in_width(max_width, width, line))


def justificate_in_width(max_width: int, width: int, line: str) -> str:
    num_justif = (max_width - width) // 2
    justif = " " * num_justif
    return f"{justif}{line}{justif}"


def sapin(max_level: int):
    if (max_level <= 0):
        return

    levelsData = [-1 for _ in range(max_level + 1)]

    previuous_lines = -1
    previuous_min = -1
    previuous_max = -1

    delta_min = 4

    for level in range(1, max_level + 1):
        if level == 1:
            lines = 4
            min = 1
            max = 7
            tail_width = 1
        else:
            if (level % 2 == 1):
                delta_min += 2
            else:
                tail_width += 2

            lines = previuous_lines + 1
            min = previuous_min + delta_min
            max = previuous_max + delta_min + 2

        levelsData[level] = LevelData(level, lines, min, max, tail_width)

        previuous_lines = lines
        previuous_min = min
        previuous_max = max
    for level in range(1, max_level + 1):
        fir_tree(levelsData[level], max)
    print_tail(levelsData[max_level])


if len(sys.argv) != 2:
    print("input error")
    exit
else:
    first_param = int(sys.argv[1])

    sapin(first_param)
