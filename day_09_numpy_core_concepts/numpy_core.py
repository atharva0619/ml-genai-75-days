import numpy as np

# Create array
arr = np.array([10, 20, 30, 40, 50])

# Indexing
print("First element:", arr[0])
print("Last element:", arr[-1])

# Slicing
print("Slice (1:4):", arr[1:4])

# Reshape
reshaped = arr.reshape(5, 1)
print("Reshaped array:\n", reshaped)

# Mathematical operations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))

# Boolean filtering
print("Elements > 25:", arr[arr > 25])

# 2D Array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print("2D Array:\n", arr2d)
print("Element at (1,2):", arr2d[1, 2])
print("Column 1:", arr2d[:, 1])
