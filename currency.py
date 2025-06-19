def how_to_pay(amount, currency):
    notesCount = {}

    currency.sort(reverse=True)

    for note in currency:
        if amount >= note:
            notesCount[note] = amount // note
            amount = amount % note

    return notesCount

euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]
how_to_pay(25, euro)