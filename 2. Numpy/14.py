## Day 4, Question 5 
## Creating a Membership Matxix for Fuzzy C Mens Clustering

import numpy as np

initial_matrix = np.random.rand(10,3)

normalization_values = np.sum(initial_matrix, axis=1, keepdims=True)
membership_matrix = initial_matrix / normalization_values
print("*** Membership Matrix: \n",membership_matrix)

memberships_sum = np.sum(membership_matrix, axis=1, keepdims=True)
print("\n*** Sum of Memberships: \n", memberships_sum)
