'''
Random Arrays
rand: Creates an array of given shape with random values between 0 and 1.
randn: Creates an array of given shape with random values from a
standard normal distribution.
randint: Creates an array with random integers within a specified range.

'''

array_rand = np.random.rand(2, 3)
print("Random array with rand:\n", array_rand)

array_randn = np.random.randn(2, 3)
print("Random array with randn:\n", array_randn)

array_randint = np.random.randint(0, 10, (2, 3))
print("Random array with randint:\n", array_randint)
