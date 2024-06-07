'''
Indexing and Slicing
Reshaping Arrays
Change the shape of an array without changing its data using the
reshape() method.

'''

array = np.array([[1, 2, 3], [4, 5, 6]])

# Indexing
print("Element at [0, 1]:", array[0, 1])

# Slicing
print("First row:", array[0, :])
print("First column:", array[:, 0])
print("Sub-array:", array[0:2, 1:3])

array = np.arange(6)
print("Original array:", array)

reshaped_array = array.reshape((2, 3))
print("Reshaped array:\n", reshaped_array)
