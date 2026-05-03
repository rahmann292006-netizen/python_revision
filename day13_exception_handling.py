# Day 13 - Exception Handling 🚀

# Basic try-except
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")


# Multiple exceptions
try:
    a = int(input("\nEnter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Using else
try:
    x = 10
    y = 2
    print("\nDivision:", x / y)
except Exception as e:
    print("Error:", e)
else:
    print("Division successful!")


# Using finally
try:
    file = open("sample.txt", "r")
    print("\nFile opened successfully")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed (finally block always runs)")


# Custom exception
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    return "Access granted"

try:
    age = int(input("\nEnter your age: "))
    print(check_age(age))
except ValueError as e:
    print("Error:", e)
