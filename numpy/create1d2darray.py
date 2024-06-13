'''
NumPy Arrays
Creating Arrays from Lists
'''

import numpy as np

# Creating a 1D array from a list
list_1d = [1, 2, 3, 4, 5]
array_1d = np.array(list_1d)
print("1D Array from list:", array_1d)

# Creating a 2D array from a list of lists
list_2d = [[1, 2, 3], [4, 5, 6]]
array_2d = np.array(list_2d)
print("2D Array from list of lists:\n", array_2d)

