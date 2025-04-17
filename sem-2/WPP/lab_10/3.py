import numpy as np

N = 10  # or any N >= 10
points = np.random.rand(N, 2) * 100  # random points in 2D, scaled up to [0, 100)

# Convert to polar coordinates
x = points[:, 0]
y = points[:, 1]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)

polar_points = np.column_stack((r, theta))
print("Cartesian:\n", points)
print("\nPolar:\n", polar_points)
