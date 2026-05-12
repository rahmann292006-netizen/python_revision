# Day 23 - DSA Logic Practice


# -------------------------------
# Reverse String
# -------------------------------

text = "python"

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Reversed String:", reversed_text)


print("\n--------------------")


# -------------------------------
# Palindrome Check
# -------------------------------

word = input("Enter word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


print("\n--------------------")


# -------------------------------
# Find Duplicate Elements
# -------------------------------

numbers = [1, 2, 3, 4, 2, 5, 1]

duplicates = []

for num in numbers:

    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicates:", duplicates)


print("\n--------------------")


# -------------------------------
# Second Largest Number
# -------------------------------

nums = [10, 55, 23, 89, 67]

nums.sort()

print("Second Largest:", nums[-2])


print("\n--------------------")


# -------------------------------
# Count Vowels
# -------------------------------

sentence = input("Enter sentence: ").lower()

vowels = "aeiou"

count = 0

for char in sentence:

    if char in vowels:
        count += 1

print("Total vowels:", count)


print("\n--------------------")


# -------------------------------
# Simple Password Checker
# -------------------------------

password = input("Create password: ")

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")
