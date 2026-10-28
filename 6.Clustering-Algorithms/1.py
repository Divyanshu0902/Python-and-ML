# K Means Clustering 

"""
***Algorithm :--
1. Initialize the K-value and the corresponding Cluster-Centroids
2. fill the clusters lists initially (by putting each point in cluster with min distance)
3. Calculate the centroids of the clusters
4. Reassign clusters based on distance from newly calculated centroids
5. Iterate centroid calculation and cluster reassigning , desired no of times
"""

points = [
    (1, 1), (2, 1), (1, 2),
    (8, 8), (9, 8), (8, 9)
]

centroids = [(1, 1), (8, 8)]

def distance(point, centroid):
    sq_dist = (point[0]-centroid[0])**2 + (point[1]-centroid[1])**2
    return sq_dist**0.5

def assign_clusters(points,centroids):
    clusters = [[] for _ in centroids]

    for point in points:
        distances = [distance(point,centroid) for centroid in centroids]
        closest = distances.index(min(distances))
        clusters[closest].append(point)

    return clusters

def calculate_centroids(clusters):
    centroids = []
    for cluster in clusters:
        a = 0
        b = 0
        for point in cluster:
            a+=point[0]
            b+=point[1]
        x = a/len(cluster)
        y = b/len(cluster)

        centroids.append((x,y))

    return centroids

for i in range(5):
    clusters = assign_clusters(points, centroids)
    centroids = calculate_centroids(clusters)

print(assign_clusters(points, centroids))
            