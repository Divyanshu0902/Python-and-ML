# membership testing | np.isin(array, [list])

import numpy as np

a = np.arange(1,6)
b = np.isin(a, (4,3))
print(b)

print("")

## boolean mask 

x = np.array([10, 20,30, 40, 50])
y = x>30
z = x[x>=30]
print(y)
print(z)