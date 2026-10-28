# Fuzzy C Means complete solution
"""
Question 1. Write a program to group \(n\) two-dimensional data samples into clusters 
using the soft clustering technique, Fuzzy C-Means. Consider the level of fuzziness as \(m=1.26\)
and the number of clusters \(c=2\). Take fixed values for the membership matrix and iterate 5 times.

Question 2. Modify the above program to randomly initialize the membership matrix. Consider precision up to 5 digits.
 Iterate and update the membership values until the difference between the old membership 
 and new membership is less than \(\theta\), a user-defined threshold.

Question 3. Modify the above program to randomly initialize the membership matrix. 
Consider precision up to 5 digits. Iterate 5 times. 
Consider the number of clusters provided by the user, with \(c>2\).
"""

import numpy as np

# Sample 2D data points
X = np.array([
    [1, 1],
    [2, 1],
    [1, 2],
    [8, 8],
    [9, 8],
    [8, 9]
], dtype=float)


# Calculate cluster centroids
def calculate_centroids(X, U, m):
    um = U ** m
    return (um.T @ X) / um.sum(axis=0)[:, None]


# Update membership matrix
def update_memberships(X, centroids, m):
    distances = np.linalg.norm(
        X[:, None, :] - centroids[None, :, :],
        axis=2
    )

    U = np.zeros_like(distances)
    exponent = 2 / (m - 1)

    for i, row in enumerate(distances):
        zero_indices = np.where(row == 0)[0]

        if len(zero_indices) > 0:
            U[i, zero_indices] = 1 / len(zero_indices)
        else:
            for j in range(len(row)):
                U[i, j] = 1 / np.sum(
                    (row[j] / row) ** exponent
                )

    return np.round(U, 5)


# Question 1: Fixed membership matrix, c=2, m=1.26, 5 iterations
def fuzzy_c_means_fixed():
    m = 1.26

    U = np.array([
        [0.90, 0.10],
        [0.80, 0.20],
        [0.85, 0.15],
        [0.10, 0.90],
        [0.20, 0.80],
        [0.15, 0.85]
    ], dtype=float)

    for iteration in range(5):
        centroids = calculate_centroids(X, U, m)
        U = update_memberships(X, centroids, m)

    centroids = calculate_centroids(X, U, m)

    print("Question 1: Fixed Membership Matrix")
    print("Final Membership Matrix:\n", U)
    print("Final Centroids:\n", centroids)


# Question 2: Random initialization until convergence
def fuzzy_c_means_converge():
    m = 1.26
    c = 2
    theta = float(input("Enter threshold theta: "))

    U = np.random.rand(len(X), c)
    U = U / U.sum(axis=1, keepdims=True)

    iteration = 0
    max_iter = 1000

    while iteration < max_iter:
        centroids = calculate_centroids(X, U, m)
        new_U = update_memberships(X, centroids, m)

        difference = np.max(np.abs(new_U - U))
        U = new_U
        iteration += 1

        if difference < theta:
            break

    centroids = calculate_centroids(X, U, m)

    print("Question 2: FCM Until Convergence")
    print("Iterations:", iteration)
    print("Final Membership Matrix:\n", U)
    print("Final Centroids:\n", centroids)


# Question 3: Random initialization, user-defined c > 2, 5 iterations
def fuzzy_c_means_multiple():
    m = 1.26
    c = int(input("Enter number of clusters (c > 2): "))

    if c <= 2:
        print("Please enter c greater than 2.")
        return

    U = np.random.rand(len(X), c)
    U = U / U.sum(axis=1, keepdims=True)

    for iteration in range(5):
        centroids = calculate_centroids(X, U, m)
        U = update_memberships(X, centroids, m)

    centroids = calculate_centroids(X, U, m)

    print("Question 3: FCM with c > 2")
    print("Final Membership Matrix:\n", U)
    print("Final Centroids:\n", centroids)


# Run the required question:
fuzzy_c_means_fixed()
# fuzzy_c_means_converge()
# fuzzy_c_means_multiple()
