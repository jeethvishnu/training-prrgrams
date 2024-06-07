'''
Array Attributes
Shape and Size: Get the shape and size of a NumPy array using the shape
 and size attributes.
Data Types: NumPy arrays have a single data type for all elements.
You can check the data type with the dtype attribute.
Specify the data type when creating an array.

'''

array = np.array([[1, 2, 3], [4, 5, 6]])

# Shape of the array
print("Shape of array:", array.shape)

# Size of the array
print("Size of array:", array.size)

# Data type of the array
print("Data type of array:", array.dtype)

array_float = np.array([1, 2, 3], dtype=np.float64)
print("Array with specified data type:", array_float)
print("Data type of the array:", array_float.dtype)

