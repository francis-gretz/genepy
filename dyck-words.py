def is_a_dyck_word(word: str) -> bool:

    index = 0

    starting_character = "."
    set_ending_character = False
    ending_character = "."

    open_brackets = 0

    for ch in word:
        if index == 0:
            starting_character = ch  # Get starting_character

        if ch == starting_character:
            open_brackets = open_brackets + 1
        else:
            if set_ending_character:
                if ch != ending_character:
                    return False  # More than 2 characters
            else:
                set_ending_character = True
                ending_character = ch  # Get ending_character

        if ch == ending_character and set_ending_character:
            if open_brackets > 0:
                open_brackets = open_brackets - 1  # Close bracket
            else:
                return False

        index = index + 1

    return open_brackets == 0


# assert is_a_dyck_word("") is True
assert is_a_dyck_word("()") is True
assert is_a_dyck_word("(((())))") is True
assert is_a_dyck_word("()()()()") is True
assert is_a_dyck_word("()(())()") is True
assert is_a_dyck_word("(((") is False
assert is_a_dyck_word("((()") is False
assert is_a_dyck_word("()))") is False
assert is_a_dyck_word("()()()(") is False
