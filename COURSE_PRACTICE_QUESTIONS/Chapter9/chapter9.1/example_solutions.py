# Chapter 9: NumPy Arrays and Reshaping

import numpy as np

#* 1. Creating a 1D Array
expression_data = np.array([2.1, 4.2, 1.5, 3.8, 2.9])
print("Expression levels:", expression_data)
print("Shape:", expression_data.shape)

#* 2. Creating a 2D Array with np.full()
array2 = np.full((2, 3), 0.5)
print("2x3 array:\n", array2)

#* 3. Using np.arange() and Smart Reshaping
sequence = np.arange(0, 15, 2)
matrix = sequence.reshape(-1, 4)  # -1 will automatically calculate the number of rows
print("Original:", sequence)
print("Smart reshaped:\n", matrix)

#* 4. Creating a 3D Array with np.ones()
array3d = np.ones((2, 2, 2))
print("3D array:\n", array3d)
print("Shape:", array3d.shape)

#* 5. Reshaping an Array
original = np.array(range(1, 13))  # Create an array with numbers from 1 to 12
reshaped = original.reshape(3, 4)
print("Original array:", original)
print("Reshaped matrix:\n", reshaped)