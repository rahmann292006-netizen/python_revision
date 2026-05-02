# Day 12 - File Handling 🔥

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello Abdul!\n")
    file.write("Welcome to Python File Handling.\n")

print("Data written to file")

# Reading from file
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)

# Appending data
with open("sample.txt", "a") as file:
    file.write("This is appended text.\n")

print("\nData appended successfully")

# Reading line by line
print("\nReading line by line:")
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
