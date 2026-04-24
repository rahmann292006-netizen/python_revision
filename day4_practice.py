# Day 4 - Python Practice (Strings)

# 1. Count vowels
s = "programming"
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print("Vowels:", count)

# 2. Check palindrome
s = "level"
print("Palindrome" if s == s[::-1] else "Not Palindrome")

# 3. Reverse string
s = "python"
print("Reversed:", s[::-1])

# 4. Count words
s = "I am learning python"
print("Word count:", len(s.split()))
