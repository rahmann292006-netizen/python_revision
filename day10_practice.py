# Day 10 - Python Practice (Lists + Logic)

# 1. Find second largest element
lst = [10, 20, 4, 45, 99]
lst = list(set(lst))
lst.sort()
print("Second largest:", lst[-2])


# 2. Check if list is sorted
lst = [1, 2, 3, 4, 5]

is_sorted = True
for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
        is_sorted = False

print("Sorted" if is_sorted else "Not Sorted")


# 3. Find common elements between two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = []

for i in a:
    if i in b:
        common.append(i)

print("Common:", common)


# 4. Count frequency of elements
lst = [1, 2, 2, 3, 3, 3]

freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency:", freq)
