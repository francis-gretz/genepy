from enum import Enum

class CardColor(Enum):
    SPADES = "S"
    HEARTS = "H"
    DIAMONDS = "D"
    CLUBS = "C"

from enum import Enum

class CardValue(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"

def missing_card(inputText):
    inputCards = set(inputText.split(" "))  # Use set for faster lookups
    for color in CardColor:
        for value in CardValue:
            card = f"{color.value}{value.value}"
            # Check if the card is missing
            if card not in inputCards:
                return card            

print(
    missing_card(
        "S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA " +
        "H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA " +
        "D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA " +
        "C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK"
    )
)