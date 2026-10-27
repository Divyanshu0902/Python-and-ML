import numpy as np

a = np.random.rand(5, 5)

print("Original array:")
print(a)

print("Odd rows and even columns:")
print(a[::2, 1::2])