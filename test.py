# Open the file in read mode
file = open("words.txt", "r")

# Read the entire content of the file
content = file.read()

print(content)

# Close the file
file.close()