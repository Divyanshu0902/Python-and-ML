# Day 4, Question 3(b)  
# create a 5×5 array of floating-point values and return its odd rows and even columns.

import numpy as np 

# b = np.arange(1,26)
# a = b.reshape(5,5)

a = np.random.rand(5,5)

print(a)
print("")

print(a[ 0:5:2, 1:5:2 ])