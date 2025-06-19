# Open the file in read mode
file = open("words.txt", "r")

# Read the entire content of the file
content = file.read()

# Close the file
file.close()

count = len("".join(filter(lambda x: x == "e", content)))

print(count)