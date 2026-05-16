# Day 26 - Sets and Tuples

# Tuple
student = ("Abdul", 21, "CSE")

print("Tuple Data:")
print(student)

# Access tuple elements
print("Name:", student[0])
print("Age:", student[1])

# Set
numbers = {1, 2, 3, 4, 4, 5}

print("\nSet Data:")
print(numbers)

# Add element
numbers.add(10)

# Remove element
numbers.remove(2)

print("Updated Set:")
print(numbers)

# Loop through set
print("\nLooping through set:")
for num in numbers:
    print(num)
