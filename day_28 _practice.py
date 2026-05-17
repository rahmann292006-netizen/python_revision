# Day 28 - List Comprehension and Lambda Functions

# List Comprehension
numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print("Squares List:")
print(squares)

# Lambda Function
add = lambda a, b: a + b

print("\nLambda Function Result:")
print(add(10, 20))

# Even numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

print("\nEven Numbers:")
print(even_numbers)
