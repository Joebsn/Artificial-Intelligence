# %% Imports
import numpy as np

# %% Creating NumPy Arrays
arr = np.array([1, 2, 3])
print(arr)
 
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
 
arr = np.array((1, 3, 2))
print(arr)

# %% Access array index
arr = np.array([
    [-1, 2, 0, 4],
    [4, -0.5, 6, 0],
    [2.6, 0, 7, 8],
    [3, -7, 4, 2.0]
])

arr2 = arr[:2, ::2]
# :: means Start from the beginning, continue until the end,
# and take every 2nd column.
print("First 2 rows and alternate columns:\n", arr2)

# [1, 1, 0, 3] Row indexes
# [3, 2, 1, 0] Column indexes
arr3 = arr[[1, 1, 0, 3], [3, 2, 1, 0]]
print("Selected elements:", arr3)

# %% Basic operations
a = np.array([[1,2],
              [3,4]])
b = np.array([[4, 3],
              [2, 1]])

print("Adding 1 to every element:\n", a + 1)
print("Subtracting 2 from each element:\n", b - 2)
print("Sum of all array elements:", a.sum())
print("Array sum:\n", a + b)

# %% Data types
x = np.array([1, 2])  
print(x.dtype)         
 
x = np.array([1.0, 2.0]) 
print(x.dtype)  
 
x = np.array([1, 2], dtype = np.int64)   
print(x.dtype)

# %% Math Operations on DataType Array
arr1 = np.array([[4, 7], [2, 6]], dtype=np.float64)
arr2 = np.array([[3, 6], [2, 8]], dtype=np.float64)

print(np.add(arr1, arr2))
print(np.sum(arr1))
print(np.sqrt(arr1)) # Calculates the square root of each element.
print(arr1.T) # Transpose of array by swaping row and columns

# %%
