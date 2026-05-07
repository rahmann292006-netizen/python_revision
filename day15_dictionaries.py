# Day 15 - Dictionaries in Python

student = {
    "name": "Abdul",
    "age": 19,
    "course": "CS Engineering"
}

print("Student Details:")
print(student)

print("\nName:", student["name"])

# Add new key
student["city"] = "Bangalore"

print("\nUpdated Dictionary:")
print(student)

# Loop through dictionary
print("\nKeys and Values:")
for key, value in student.items():
    print(key, ":", value)
