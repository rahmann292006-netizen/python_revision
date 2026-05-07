# Day 17 - NumPy Practice

import numpy as np

a1 = np.arange(1, 11)

print("Array:")
print(a1)

print("\nOdd Numbers:")
print(a1[::2])

print("\nSum:")
print(np.sum(a1))

print("\nMean:")
print(np.mean(a1))

print("\nSquare:")
print(np.square(a1))

print("\nCube:")
print(np.power(a1, 3))
