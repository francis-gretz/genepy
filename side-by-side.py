import textwrap


def sidebyside(left, right, width=79):
    col_width = width // 2
    if width % 2 == 0:
        col_width -= 1

    left_lines = textwrap.wrap(left, col_width)
    right_lines = textwrap.wrap(right, col_width)

    result = []

    left_count = len(left_lines)
    right_count = len(right_lines)

    for i in range(left_count):
        left_side = left_lines[i].ljust(col_width, " ")

        if i < right_count:
            right_side = right_lines[i].ljust(col_width, " ")
            s = f"{left_side}|{right_side}"
        else:
            s = f"{left_side}|"

        result.append(s)

    spaces = "".ljust(col_width, " ")
    for j in range(left_count, right_count):
        right_side = right_lines[j].ljust(col_width, " ")
        s = f"{spaces}|{right_side}"
        result.append(s)

    return "\n".join(result)


print(sidebyside("Helloworld!", "Helloworld!", width=10))

# left = (
#     "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
#     "Sed non risus. "
#     "Suspendisse lectus tortor, dignissim sit amet, "
#     "adipiscing nec, utilisez sed sin dolor."
# )

# right = (
#     "Morbi venenatis, felis nec pretium euismod, "
#     "est mauris finibus risus, consectetur laoreet "
#     "sem enim sed arcu. Maecenas sit amet eleifend sem. "
#     "Nullam ac libero metus. Praesent ac finibus nulla, vitae molestie dolor."
#     " Aliquam vestibulum viverra nisl, id porta mi viverra hendrerit."
#     " Ut et porta augue, et convallis ante."
# )

# print(sidebyside(left, right))
