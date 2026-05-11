# Day 22 - Functions & Recursion Basics


# -------------------------------
# Simple Function
# -------------------------------

def greet(name):
    print(f"Hello, {name}!")


greet("Abdul")


print("\n--------------------")


# -------------------------------
# Function with Return
# -------------------------------

def add(a, b):
    return a + b


result = add(10, 20)

print("Sum:", result)


print("\n--------------------")


# -------------------------------
# Check Prime Number
# -------------------------------

def is_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):

        if num % i == 0:
            return False

    return True


number = int(input("Enter number: "))

if is_prime(number):
    print("Prime Number")
else:
    print("Not Prime")


print("\n--------------------")


# -------------------------------
# Recursive Countdown
# -------------------------------

def countdown(n):

    if n == 0:
        print("Done!")
        return

    print(n)

    countdown(n - 1)


countdown(5)


print("\n--------------------")


# -------------------------------
# Recursive Factorial
# -------------------------------

def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n - 1)


print("Factorial:", factorial(5))


print("\n--------------------")


# -------------------------------
# Fibonacci Series
# -------------------------------

def fibonacci(n):

    a = 0
    b = 1

    for _ in range(n):
        print(a, end=" ")

        a, b = b, a + b


fibonacci(10)
