import numpy as np

print("\nCombine a 1D and 2D NumPy array")
arr1= np.array([1, 2, 3])
arr2 = np.array([[4, 5, 6], [7, 8, 9]])
reshaped_1d = arr1.reshape(1, 3)
result = np.concatenate((arr2, reshaped_1d), axis=0)
print(result)


print("\nFlatten a 2D array into a 1D array")
flattened = arr2.flatten()
print("\nFlattened Array:\n", flattened)


print("\nReverse a NumPy array")
reversed_array = arr1[::-1]
print("\nReversed 1D Array:\n", reversed_array)

print("\nMaximum value")
max_val = arr2.max()
print("\nMaximum Value:\n", max_val)

print("\nMinimum value")
min_val = arr2.min()
print("\nMinimum Value:\n", min_val)

print("\nNumber of rows and columns")
shape = arr2.shape
print("\nNumber of Rows and Columns:\n", shape)

print("\nSelecting elements")
all_elements = arr2[:]        # all elements
specific_element = arr2[1, 2] # element at 2nd row, 3rd column
print("\nAll Elements:\n", all_elements)
print("Specific Element [1,2]:", specific_element)

print("\nSum of values in a 2D array using loop")
sum = 0
for row in arr2:
    for val in row:
        sum += val
print("\nSum Using Loop:", sum)

print("\nArithmetic operations\n")
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

add_result = array1 + array2
print("\nAddition:\n", add_result)

sub_result = array1 - array2
print("Subtraction:\n", sub_result)

mul_result = array1 * array2
print("Multiplication:\n", mul_result)

div_result = array1 / array2
print("Division:\n", div_result)
