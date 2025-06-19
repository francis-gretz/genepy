def list_pretty_print(items):
    chunks = []
    chunk_size = 5
    for i in range(0, len(items), chunk_size):
        chunks.append(items[i : i + chunk_size])

    for chunk in chunks:
        s = f"{chunk}".replace("[", "").replace("]", "")
        print(s)


list_pretty_print([42] * 6)
