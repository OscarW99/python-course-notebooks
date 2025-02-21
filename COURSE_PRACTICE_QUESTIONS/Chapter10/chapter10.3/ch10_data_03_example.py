# Chapter 9: Data Manipulation

import numpy as np

#* 1. Broadcasting Addition
array = np.array([[1, 2], [3, 4]])
result = array + 5
print("Result of broadcasting addition:\n", result)

#* 2. Broadcasting Multiplication
array = np.array([[1, 2, 3], [4, 5, 6]])
result = array * 2
print("Result of broadcasting multiplication:\n", result)

#* 3. Broadcasting with 1D Array
ones_array = np.ones((2, 3))
to_add = np.array([10, 20, 30])
result = ones_array + to_add
print("Result of adding 1D array to 2D array:\n", result)

#* 4. Vectorized Squaring
values = np.array([1, 2, 3, 4, 5])
squared = values ** 2
print("Squared values using vectorization:", squared)

#* 5. Element-wise Multiplication
array1 = np.array([1, 2, 3, 4])
array2 = np.array([10, 20, 30, 40])
result = array1 * array2
print("Element-wise multiplication result:", result)