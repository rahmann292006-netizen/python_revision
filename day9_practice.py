# Day 9 - Python Practice (Logic)

# 1. Check Armstrong number
num = 153
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

print("Armstrong" if total == num else "Not Armstrong")


# 2. Find largest of 3 numbers
a, b, c = 10, 25, 15

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# 3. Count even and odd numbers
lst = [1, 2, 3, 4, 5]
even = odd = 0

for i in lst:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even, "Odd:", odd)
