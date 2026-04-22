# Day 2 - Python Practice

# 1. Check if a number is palindrome
num = 121
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# 2. Find second largest element in list
lst = [10, 20, 4, 45, 99]
lst.sort()
print("Second largest:", lst[-2])


# 3. Count frequency of elements in list
lst = [1, 2, 2, 3, 1, 4, 2]
freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

print(freq)
