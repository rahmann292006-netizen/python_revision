# Day 7 - Python Practice (Nested Loops + Patterns)

# 1. Square pattern
n = 4
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()


# 2. Right triangle pattern
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# 3. Reverse triangle
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# 4. Multiplication table (nested loop)
for i in range(1, 4):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()


# 5. Count digits in a number
num = 12345
count = 0

while num > 0:
    count += 1
    num //= 10

print("Digits:", count)
