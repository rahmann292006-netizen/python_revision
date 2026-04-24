# Day 5 - Python Practice (Functions)

# 1. Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print("Factorial:", factorial(5))


# 2. Function to check even/odd
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

print(check_even_odd(7))


# 3. Function to find sum of list
def list_sum(lst):
    return sum(lst)

print(list_sum([1, 2, 3, 4]))


# 4. Function to find max element
def find_max(lst):
    return max(lst)

print(find_max([10, 5, 20, 8]))
