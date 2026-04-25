# Day 6 - Python Practice (Loops + Patterns)

# 1. Print numbers from 1 to 10 using loop
for i in range(1, 11):
    print(i)


# 2. Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print("Even:", i)


# 3. Simple star pattern
n = 5
for i in range(1, n + 1):
    print("*" * i)


# 4. Sum of first n numbers
n = 5
total = 0
for i in range(1, n + 1):
    total += i

print("Sum:", total)


# 5. Multiplication table of a number
num = 3
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
