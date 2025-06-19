import random


def gen_colors(size: int):
    if (size > 26):
        size = 26
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return LETTERS[:size]


def gen_code(code_size: int, colors):
    length = len(colors)
    result = []

    for i in range(code_size):
        index = random.randint(0, length - 1)
        result.append(colors[index])

    return "".join(result)


def check_guess(guess, code_size: int, colors):
    length = len(guess)
    if length != code_size:
        return False

    for i in range(length):
        if not colors.__contains__(guess[i]):
            return False

    return True


def score_guess(code, guess):
    right = 0
    moved = 0

    length = len(guess)
    for i in range(length):
        if code[i] == guess[i]:
            right += 1
            continue

        if code.__contains__(guess[i]):
            moved += 1

    return (right, moved)


def play_cli(code_size, nb_colors):
    num_attempts = 1

    print(f"Congrats, you won after 3 {num_attempts} attempts !")


if __name__ == "__main__":
    play_cli()
