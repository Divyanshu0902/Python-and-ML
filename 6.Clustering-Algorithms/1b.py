# Complete K-Means Program 


import random
import matplotlib.pyplot as plt

# Dataset
points = [
    (1, 1), (2, 1), (1, 2),
    (8, 8), (9, 8), (8, 9)
]

# Calculate Euclidean distance
def distance(point, centroid):
    return (
        (point[0] - centroid[0]) ** 2
        + (point[1] - centroid[1]) ** 2
    ) ** 0.5


# Assign each point to its nearest centroid
def assign_clusters(points, centroids):
    clusters = [[] for _ in centroids]

    for point in points:
        distances = [
            distance(point, centroid)
            for centroid in centroids
        ]

        closest = distances.index(min(distances))
        clusters[closest].append(point)

    return clusters


# Calculate new centroids
def calculate_centroids(clusters, old_centroids):
    centroids = []

    for i, cluster in enumerate(clusters):
        # Keep the old centroid if the cluster is empty
        if len(cluster) == 0:
            centroids.append(old_centroids[i])
            continue

        x = sum(point[0] for point in cluster) / len(cluster)
        y = sum(point[1] for point in cluster) / len(cluster)

        centroids.append((x, y))

    return centroids


# Calculate Sum of Squared Errors
def calculate_sse(clusters, centroids):
    sse = 0

    for i, cluster in enumerate(clusters):
        for point in cluster:
            sse += distance(point, centroids[i]) ** 2

    return sse


# K-Means algorithm
def k_means(points, k, max_iter=100):
    # Randomly select k initial centroids from the points
    centroids = random.sample(points, k)

    for _ in range(max_iter):
        clusters = assign_clusters(points, centroids)

        new_centroids = calculate_centroids(
            clusters, centroids
        )

        # Stop if centroids no longer change
        if new_centroids == centroids:
            centroids = new_centroids
            break

        centroids = new_centroids

    # Assign points using the final centroids
    clusters = assign_clusters(points, centroids)

    return centroids, clusters


# Run K-Means for K = 2
centroids, clusters = k_means(points, 2)

print("Final Clusters:")
for i, cluster in enumerate(clusters):
    print(f"Cluster {i + 1}: {cluster}")

print("Final Centroids:", centroids)
print("SSE:", calculate_sse(clusters, centroids))


# Elbow method: compare different K values
k_values = range(1, min(10, len(points)) + 1)
sse_values = []

for k in k_values:
    centroids, clusters = k_means(points, k)
    sse_values.append(calculate_sse(clusters, centroids))

plt.plot(list(k_values), sse_values, marker="o")
plt.xlabel("Number of clusters (K)")
plt.ylabel("SSE")
plt.title("Elbow Method")
plt.xticks(list(k_values))
plt.grid(True)
plt.show()
