# Day 3 - Python Practice

# 1. Find common elements in two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = list(set(a) & set(b))
print("Common elements:", common)


# 2. Remove duplicates from list
lst = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(lst))
print("Unique list:", unique)


# 3. Find factorial of a number
num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)
