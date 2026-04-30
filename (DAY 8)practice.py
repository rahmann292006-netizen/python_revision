# Day 8 - Python Practice (Numbers)

# 1. Check prime number
num = 7
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False

print("Prime" if is_prime else "Not Prime")


# 2. Sum of digits
num = 123
total = 0

while num > 0:
    total += num % 10
    num //= 10

print("Sum of digits:", total)


# 3. Fibonacci series
n = 5
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
