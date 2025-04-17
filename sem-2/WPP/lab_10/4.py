import numpy as np

arr = np.array(['hello', 'world', 'python', 'rocks'])

arr_centered = np.array([s.center(15, '_') for s in arr])
arr_left = np.array([s.ljust(15, '_') for s in arr])
arr_right = np.array([s.rjust(15, '_') for s in arr])

print("Centered:\n", arr_centered)
print("\nLeft-justified:\n", arr_left)
print("\nRight-justified:\n", arr_right)