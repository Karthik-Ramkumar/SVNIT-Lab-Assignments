# K-Means using Newton-Raphson style centroid update
# (for K-means, centroid update still becomes mean)

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

def newton_update(cluster, old_centroid):
    if len(cluster) == 0:
        return old_centroid

    c = old_centroid

    for i in range(5):
        f = 0
        df = 0

        for x in cluster:
            f += 2 * (c - x)
            df += 2

        c = c - f / df

    return c

def update_centroids_newton(clusters, centroids):
    new_centroids = []

    for i in range(len(clusters)):
        new_centroids.append(newton_update(clusters[i], centroids[i]))

    return new_centroids

def kmeans_newton(points, centroids, iterations):
    for i in range(iterations):
        clusters = assign_clusters(points, centroids)
        centroids = update_centroids_newton(clusters, centroids)

        print("Iteration", i + 1)
        print("Clusters:", clusters)
        print("Centroids:", centroids)
        print()

kmeans_newton(points, centroids, 3)