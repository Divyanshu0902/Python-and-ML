# 2D Array indexing and slicing 

import numpy as np

b = np.arange(1,26)
a = b.reshape(5,5)

print(a)
print("")
# print(b[2,2]) #13

print(a[2, : ]) #print entire 3rd row
print("")

print(a[2, 1:4]) #3rd row's index 1 to 3
print("")

print(a[ : , 1]) #all rows of 2nd column