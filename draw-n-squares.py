def draw_n_squares(n):
    lines = []
    for y in range(1, n + 1):
        lineExtrem = ""
        lineCenter = ""
        for x in range(1, n + 1):
            charExtrem = addExtremLine(x)
            charCenter = addCenterLine(x)
            lineExtrem = lineExtrem + charExtrem
            lineCenter = lineCenter + charCenter

        if y == 1:
            lines.append(lineExtrem)
        lines.append(lineCenter)
        lines.append(lineExtrem)

    return "\n".join(lines)


def addExtremLine(index):
    if index == 1:
        return "+---+"
    else:
        return "---+"


def addCenterLine(index):
    if index == 1:
        return "|   |"
    else:
        return "   |"


res = draw_n_squares(3)
print(res)

# >>> print(draw_n_squares(3))
# +---+
# |   |
# +---+
# +---+---+---+
# |   |   |   |
# +---+---+---+
# |   |   |   |
# +---+---+---+
# |   |   |   |
# +---+---+---+
