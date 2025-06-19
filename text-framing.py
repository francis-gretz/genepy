from dataclasses import dataclass, replace


@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"


fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")


def frame_text(text: str, frame: Frame) -> str:
    max_line_length = -9

    # Get max length of lines
    for line in text.splitlines():
        line_length = len(line)
        if max_line_length < line_length:
            max_line_length = line_length

    # Get top line
    top = frame.top * max_line_length
    top_line = f"{frame.top_left}{top}{frame.top_right}"

    lines = [top_line]

    # Get center lines
    for line in text.splitlines():
        center = line.ljust(max_line_length)
        center_line = f"{frame.left}{center}{frame.right}"
        lines.append(center_line)

    # Get bottom line
    bottom_line = f"{frame.bottom_left}{top}{frame.bottom_right}"

    lines.append(bottom_line)

    return "\n".join(lines)


text = """
      *
     ***
    *****
   *******
    *****
   *******
  *********
 ***********
*************
     |||
     |||"""

frame = Frame(
    top="-",
    left="|",
    bottom="-",
    right="|",
    top_left="+",
    top_right="+",
    bottom_left="+",
    bottom_right="+",
)

res = frame_text(text, frame)
print(res)
