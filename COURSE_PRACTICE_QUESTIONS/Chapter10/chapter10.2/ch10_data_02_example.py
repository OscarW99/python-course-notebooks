# Chapter 10: Data Manipulation

import numpy as np

#* 1. Extracting Columns
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
selected_columns = array[:, 1:3]
print("Selected columns:\n", selected_columns)

#* 2. Boolean Indexing
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = [True, False, True]
masked_array = array[mask]
print("Masked array:\n", masked_array)

#* 3. Vertical Stack and Horizontal Split
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
result = np.vstack((array1, array2))
split_result = np.hsplit(result, 2)
print("Vertically stacked:\n", result)
print("Horizontally split:\n", split_result[0], "\n", split_result[1])

#* 4. Vertical Split
array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
split_result = np.vsplit(array, 2)
print("First part of vertical split:\n", split_result[0])
print("Second part of vertical split:\n", split_result[1])

#* 5. Insert and Delete
array = np.array([1, 2, 3, 4, 5])
array = np.insert(array, 2, [10, 11])
final = np.delete(array, [0, 3])
print("After insertion:", array)
print("After deletion:", final)