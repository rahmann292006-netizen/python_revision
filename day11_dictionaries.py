# Day 11 - Dictionaries 🚀

# Creating a dictionary
student = {
    "name": "Abdul",
    "age": 20,
    "course": "CS"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))

# Adding new key-value
student["grade"] = "A"
print("After adding grade:", student)

# Updating value
student["age"] = 21
print("After update:", student)

# Removing item
student.pop("course")
print("After removal:", student)

# Looping through dictionary
print("\nKeys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)

# Check key existence
if "name" in student:
    print("\nName exists in dictionary")
