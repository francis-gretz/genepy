import itertools


def get_sequences_of_string(text, maximum_pattern_length):
    result = set()
    for i in range(len(text)):
        for j in range(i+1, len(text)+1):
            if (j-i) > maximum_pattern_length:
                continue
            result.add(text[i:j])
    return result


def seq_mining(data, minimum_proportion, maximum_pattern_length):
    sequences = []

    for text in data:
        sequences_in_word = get_sequences_of_string(
            text, maximum_pattern_length)
        for sequence in sequences_in_word:
            sequences.append(sequence)

    uniquekeys = dict()
    sequences.sort
    for k, g in itertools.groupby(sequences, key=lambda x: str(x)):
        uniquekeys[k] = uniquekeys.get(k, 0) + len(list(g))

    filtered = dict({k: v for k, v in uniquekeys.items()
                    if v / len(data) >= minimum_proportion})

    return filtered


# res = seq_mining(["UVWXYZ", "ABCDEFG", "DCEFG"], 0.66, 3)
# print(res)


res = seq_mining(['ABC', 'ABAB', 'BCAA'], 0.1, 10000)
print(res)

# Counter({'A': 3, 'B': 3, 'C': 2, 'AB': 2, 'BC': 2, 'ABC': 1, 'ABA': 1, 'AA': 1, 'ABAB': 1, 'CA': 1, 'BA': 1, 'BCAA': 1, 'BCA': 1, 'CAA': 1, 'BAB': 1})
