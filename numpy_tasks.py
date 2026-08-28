import numpy as np

# 1. Creating NumPy arrays
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)

# 2. Indexing
print("First element:", arr[0])
print("Third element:", arr[2])

# 3. Slicing
print("First three elements:", arr[:3])

# 4. Mathematical operations
print("Addition:", arr + 5)
print("Subtraction:", arr - 5)
print("Multiplication:", arr * 2)
print("Division:", arr / 2)

# 5. Array calculations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 6. 2D Array
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("2D Array:")
print(matrix)

print("First row:", matrix[0])
print("Second row:", matrix[1])