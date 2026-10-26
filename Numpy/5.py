# array slicing in numpy

import numpy as np

a = np.array([5, 10, 15, 20, 25, 30, 35])

# Q1: print [10,20,30]
a1 = a[1:6:2]
print(a1)

# Q2: print [5,15,25,35]
a2 = a[0:7:2]
print(a2)