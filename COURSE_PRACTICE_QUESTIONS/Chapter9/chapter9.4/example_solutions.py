# Chapter 9: Data Manipulation

import numpy as np

#* 1. Finding Non-Zero Elements
array = np.array([1, 0, 3, 0, 5])
indices = np.nonzero(array)
print("Indices of non-zero elements:", indices[0])

#* 2. Using np.where() for Conditional Selection
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])
result = np.where(x < 3, x, y)
print("Result of np.where():\n", result)

#* 3. Finding Max Indices
array = np.array([[5, 2, 8], [1, 9, 3], [7, 4, 6]])
row_max = np.argmax(array, axis=1)
col_max = np.argmax(array, axis=0)
print("Indices of max values in rows:", row_max)
print("Indices of max values in columns:", col_max)

#* 4. Array Statistics
array = np.array([15, 3, 24, 8, 12])
stats = {
    'max': np.max(array),
    'min': np.min(array),
    'mean': np.mean(array),
    'std': np.std(array)
}
print("Array statistics:", stats)

#* 5. Vector and Matrix Products
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
products = {
    'dot_product': np.dot(a, b),
    'cross_product': np.cross(a, b),
    'outer_product': np.outer(a, b)
}
print("Dot product:", products['dot_product'])
print("Cross product:", products['cross_product'])
print("Outer product:\n", products['outer_product'])