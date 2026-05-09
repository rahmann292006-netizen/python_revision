numbers = [5, 8, 12, 20, 45, 67]

target = 20

found = False

for num in numbers:
    
    if num == target:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")
