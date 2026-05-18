# Day 29 - JSON Handling in Python

import json

student = {
    "name": "Abdul",
    "age": 21,
    "course": "Python"
}

# Convert dictionary to JSON
json_data = json.dumps(student, indent=4)

print("JSON Data:")
print(json_data)

# Convert JSON back to dictionary
python_data = json.loads(json_data)

print("\nPython Dictionary:")
print(python_data)
