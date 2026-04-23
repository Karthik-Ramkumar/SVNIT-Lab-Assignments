# K-Means using Gradient Descent style centroid update (mean update)

points = [2, 4, 10, 12, 20, 25]
k = 2
centroids = [3, 15]

def assign_clusters(points, centroids):
    clusters = [[] for i in range(len(centroids))]

    for p in points:
        best = 0
        min_dist = abs(p - centroids[0])

        for i in range(1, len(centroids)):
            dist = abs(p - centroids[i])
            if dist < min_dist:
                min_dist = dist
                best = i

        clusters[best].append(p)

    return clusters

def update_centroids(clusters, centroids):
    new_centroids = []

    for i in range(len(clusters)):
        if len(clusters[i]) > 0:
            new_centroids.append(sum(clusters[i]) / len(clusters[i]))
        else:
            new_centroids.append(centroids[i])

    return new_centroids

def kmeans(points, centroids, iterations):
    for i in range(iterations):
        clusters = assign_clusters(points, centroids)
        centroids = update_centroids(clusters, centroids)

        print("Iteration", i + 1)
        print("Clusters:", clusters)
        print("Centroids:", centroids)
        print()

kmeans(points, centroids, 3)