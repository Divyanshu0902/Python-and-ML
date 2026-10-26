# Day 4, Question 5 

# initialize an N X C membership matrix, where each membership value is between 0 and 1 
# and the memberships for each object sum to 1.

import numpy as np

membership = np.random.rand(3,2)
print(membership)
normalized = membership / np.sum(membership, axis=1, keepdims=True)
print(normalized)