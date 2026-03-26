import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("cities.csv")

coords = df.values

# help functions
def assignCluster(points, centers):
    city_gaps = np.zeros((len(points), len(centers)))
    # here we are creating a matrix(city_gaps) of size cities* airports
    for i in range(len(centers)):
        city_gaps[:, i] = np.sum((points - centers[i]) ** 2, axis=1)
    return np.argmin(city_gaps, axis=1) #returning least distance airport for each city

def sumSquaredError(points, centers, labels): # measuing distance of city to assigned airport
    sse_list = []
    total_sse = 0.0
    for k in range(len(centers)):
        cluster_points = points[labels == k]
        if len(cluster_points) == 0:
            sse = 0.0
        else:
            sse = np.sum((cluster_points - centers[k]) ** 2)
        sse_list.append(sse)
        total_sse += sse
    return sse_list, total_sse

def gradient_descent_kmeans(points, k=3, learningRate=0.01, max_iter=1000, tol=1e-6):
    # fixed initial centers for reproducibility
    np.random.seed(42) # seed is used so that we get same initial centers every time
    indices = np.random.choice(len(points), k, replace=False)
    centers = points[indices].copy()

    for iteration in range(max_iter):
        labels = assignCluster(points, centers)
        old_centers = centers.copy()
        for i in range(k):
            cluster_points = points[labels == i]
            if len(cluster_points) == 0:
                continue
            n = len(cluster_points)

            # gradient of SSE wrt center = 2*n*center - 2*sum(points)
            grad = 2 * n * centers[i] - 2 * np.sum(cluster_points, axis=0) # move in direction of airport which reduces sse

            # gradient descent update
            centers[i] = centers[i] - learningRate * grad

        shift = np.linalg.norm(centers - old_centers) # we compute how big of a change we get. if it is small we stop the alho
        if shift < tol:
            break

    labels = assignCluster(points, centers)
    sse_list, total_sse = sumSquaredError(points, centers, labels)
    return centers, labels, sse_list, total_sse, iteration + 1


# newton raphson
#this algo moves centre to exact centroid of the cluster in one update hence its faster than gradient descen
def newton_raphson_kmeans(points, k=3, max_iter=3, tol=1e-6):
    # same fixed initial centers for fair comparison
    np.random.seed(42)
    indices = np.random.choice(len(points), k, replace=False)
    centers = points[indices].copy()

    for iteration in range(max_iter):
        labels = assignCluster(points, centers)
        old_centers = centers.copy()
        for i in range(k):
            cluster_points = points[labels == i]
            if len(cluster_points) == 0:
                continue
            n = len(cluster_points)
            grad = 2 * n * centers[i] - 2 * np.sum(cluster_points, axis=0)
            # hessian
            H = 2 * n * np.eye(2)
            # newton update -> c_new = c_old - H^-1 * grad
            step = np.linalg.inv(H).dot(grad)
            centers[i] = centers[i] - step

        shift = np.linalg.norm(centers - old_centers)
        if shift < tol:
            break
    labels = assignCluster(points, centers)
    sse_list, total_sse = sumSquaredError(points, centers, labels)
    return centers, labels, sse_list, total_sse, iteration + 1



gd_centers, gd_labels, gd_sse_list, gd_total_sse, gd_iters = gradient_descent_kmeans(
    coords, k=3, learningRate=0.01, max_iter=1000
)
nr_centers, nr_labels, nr_sse_list, nr_total_sse, nr_iters = newton_raphson_kmeans(
    coords, k=3, max_iter=100
)

print("\n gradient descent method")
for i, center in enumerate(gd_centers):
    print(f"Airport {i+1}: ({center[0]:.4f}, {center[1]:.4f})")
for i, sse in enumerate(gd_sse_list):
    print(f"Cluster {i+1} SSE: {sse:.4f}")
print(f"Total SSE: {gd_total_sse:.4f}")
print(f"Iterations: {gd_iters}")

print("\n newton raphson method")
for i, center in enumerate(nr_centers):
    print(f"Airport {i+1}: ({center[0]:.4f}, {center[1]:.4f})")
for i, sse in enumerate(nr_sse_list):
    print(f"Cluster {i+1} SSE: {sse:.4f}")
print(f"Total SSE: {nr_total_sse:.4f}")
print(f"Iterations: {nr_iters}")


#plotting
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
axes[0].scatter(coords[:, 0], coords[:, 1], c=gd_labels, cmap='viridis', s=30)
axes[0].scatter(gd_centers[:, 0], gd_centers[:, 1], c='red', marker='X', s=200, label='Airports')
axes[0].set_title("gradient descent - 3 airport locations")
axes[0].set_xlabel("A")
axes[0].set_ylabel("B")
axes[0].legend()
axes[0].grid(True)

axes[1].scatter(coords[:, 0], coords[:, 1], c=nr_labels, cmap='viridis', s=30)
axes[1].scatter(nr_centers[:, 0], nr_centers[:, 1], c='red', marker='X', s=200, label='Airports')
axes[1].set_title("newton-raphson - 3  airport locations")
axes[1].set_xlabel("A")
axes[1].set_ylabel("B")
axes[1].legend()
axes[1].grid(True)
plt.tight_layout()
plt.show()

# gradient needs learning rate and goes step by step
# while newton raphson goes directly to the optimal solution in one step hence its faster
#here we run gradient for 1000 and newton for 100

