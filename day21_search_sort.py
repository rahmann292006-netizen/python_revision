# Day 21 - Searching & Sorting Basics


# -------------------------------
# Linear Search
# -------------------------------

numbers = [12, 45, 7, 23, 89, 34]

target = int(input("Enter number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"{target} found at index {i}")
        found = True
        break

if not found:
    print("Number not found")


print("\n--------------------")


# -------------------------------
# Find Largest Number
# -------------------------------

nums = [10, 55, 2, 99, 34]

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print("Largest number is:", largest)


print("\n--------------------")


# -------------------------------
# Bubble Sort
# -------------------------------

arr = [5, 1, 4, 2, 8]

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):

        if arr[j] > arr[j + 1]:

            # Swap
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)


print("\n--------------------")


# -------------------------------
# Reverse a List
# -------------------------------

data = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(data) - 1, -1, -1):
    reversed_list.append(data[i])

print("Reversed list:", reversed_list)


print("\n--------------------")


# -------------------------------
# Count Even & Odd Numbers
# -------------------------------

values = [1, 2, 3, 4, 5, 6, 7, 8]

even = 0
odd = 0

for num in values:

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
