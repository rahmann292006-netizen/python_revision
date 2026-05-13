# Day 24 - File Handling & Data Processing


# -------------------------------
# Write to File
# -------------------------------

file = open("notes.txt", "w")

file.write("Python Practice Day 24\n")
file.write("Consistency is building confidence.\n")

file.close()

print("Data written successfully!")


print("\n--------------------")


# -------------------------------
# Read File
# -------------------------------

file = open("notes.txt", "r")

content = file.read()

print("File Content:\n")
print(content)

file.close()


print("\n--------------------")


# -------------------------------
# Append Data
# -------------------------------

file = open("notes.txt", "a")

file.write("Daily practice matters.\n")

file.close()

print("New data appended!")


print("\n--------------------")


# -------------------------------
# Count Words in File
# -------------------------------

file = open("notes.txt", "r")

text = file.read()

words = text.split()

print("Total words:", len(words))

file.close()


print("\n--------------------")


# -------------------------------
# Count Lines in File
# -------------------------------

file = open("notes.txt", "r")

lines = file.readlines()

print("Total lines:", len(lines))

file.close()


print("\n--------------------")


# -------------------------------
# Search Word in File
# -------------------------------

search_word = "Python"

file = open("notes.txt", "r")

data = file.read()

if search_word in data:
    print(f"{search_word} found in file")
else:
    print(f"{search_word} not found")

file.close()
