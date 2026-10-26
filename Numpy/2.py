import numpy as np

a = np.arange(100, 200, 10)
b = a.reshape(5,2)

print(b)

print(b.ndim)
print(b.shape)
print(b.size)