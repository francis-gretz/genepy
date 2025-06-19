# Open the file in read mode
file = open("words.txt", "r")

# Read the entire content of the file
content = file.read()

# Close the file
file.close()

counter = dict()

total_caracters = len(content)

for ch in content:
    l = ch.lower()
    counter[l] = counter.get(l, 0) + 1

for key, value in counter.items():
    percentage = value / total_caracters
    print(f"{key}: {percentage:.2f}")
