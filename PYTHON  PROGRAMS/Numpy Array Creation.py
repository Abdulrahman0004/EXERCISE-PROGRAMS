import numpy as np

array_1D = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1D)

array_2D = np.array([[1, 2, 3],[4, 5, 6]])
print("2D Array: \n", array_2D)

ones_array = np.ones((2, 3), dtype=int)
print("Ones Array:\n", ones_array)

zeros_array = np.zeros((2, 3), dtype=float)
print("Zeros Array:\n", zeros_array)

arange_array = np.arange(10)
print("Arange Array:", arange_array)   #Like range() in python...

arange1_array = np.arange(1, 10, 2, dtype=int)
print("Arange Array:", arange1_array)

linspace_array = np.linspace(1, 2, num=10)
print("Linspace Array:", linspace_array)

empty_array = np.empty((5, 3))
print("Empty Array:\n", empty_array)

full_array = np.full((3, 3), 5)
print("Full Array:\n", full_array)