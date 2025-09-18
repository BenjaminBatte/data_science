# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 06:44:11 2025

@author: bbatte
"""

import numpy as np
#Part 1: Working with Arrays 
# 1. Create array 'a'
a = np.array([
              [3, 8, 15,2],
              [2, 10, 5, 3],
              [4, 0, 2, 4]
              ])
print("\nArray a: \n", a)

# 2. Shape of array
print("\nShape of a:", a.shape)

# 3. Number of dimensions
print("\nDimensions (ndim):", a.ndim)

# 4. len(a) returns length of the first dimension
print("\nlen (a):", len(a))

# 5. Explanation
print("\nShape shows it has 3 rows and 4 columns ==> ndim=2, length =3 (rows).")

# Part 2: Array Creation with NumPy 

# 6. Create a 1D NumPy array with values from 2 to 5, inclusive. 
arr1 = np.arange(2, 6)
print("\nArray from 2 to 5:", arr1)

# 7. Create a 1D array with 10 equally spaced values between 2 and 5, inclusive. 
# np.set_printoptions(precision=2, suppress=True) for future just
arr2 = np.linspace(2, 5, 10)
print("\n10 equally spaced values:", arr2)
# 8. Create a 4 x 4 array filled with ones. 
ones_arr = np.ones((4, 4))
print("4x4 ones:\n", ones_arr)

# 9. Create a 6 x 6 identity matrix. 
identity = np.eye(6)
print("6x6 Identity:\n", identity)

# 10. Create the following diagonal matrix using a single NumPy 
# command: [[1, 0, 0], [0, 2, 0], [0, 0, 3]] 
diag_matrix = np.diag([1, 2, 3])
print("\nDiagonal matrix: \n", diag_matrix)

# 11. Use np.random.randn() to create a (3, 5) array with random numbers 
# from a standard normal distribution (mean = 0, variance = 1). 
random_arr = np.random.randn(3, 5)
print("Random normal array (3x5):\n", random_arr)


# Part 3: Indexing and Slicing 
# 12. Create another array named 'a': 
a= np.array([
    [2, 7, 12, 0], 
    [3, 9, 3, 4], 
    [4, 0, 1, 3]
    ]) 
print("\nArray a:\n", a)

# 13. Retrieve the second row: [3, 9, 3, 4]. 
print("\nSecond row:", a[1])

# 14. Retrieve the third column: [12, 3, 1]. 
print("\nThird column", a[:, 2])
# 15. Create the following two arrays: 


int_arr = np.array(
    [[1, 1, 1, 1], 
     [1, 1, 1, 1], 
     [1, 1, 1, 2], 
     [1, 6, 1, 1]] 
    )
print("\nInteger array:\n", int_arr)

float_arr= np.array(
    [[0., 0., 0., 0., 0.], 
   [2., 0., 0., 0., 0.], 
   [0., 3., 0., 0., 0.], 
   [0., 0., 4., 0., 0.],
   [0., 0., 0., 5., 0.], 
   [0., 0., 0., 0., 6.]] 
    )


print("\nFloat array :\n", float_arr)




# Part 4: Boolean Masks and Statistics 
# 16. Recall array 'a' from earlier: [[2, 7, 12, 0], [3, 9, 3, 4], [4, 0, 1, 3]] 
print("\nArray a:\n", a)
# 17. Use a comparison operation (> 5) to create a Boolean array indicating 
# where elements are greater than 5. 
mask = a >5
print("\nMask (a > 5):\n", mask)

# 18. Use the mask to extract all values from the array that are greater than 5. 
print("\nValues > 5:", a[mask])

# 19. Modify the array in-place so that all values greater than 5 are 
# replaced with 5. 
a[a > 5] = 5
print("\nModified array:\n", a)

# Part 5: Array Aggregation Functions 
# 20. Using array 'a' from earlier, compute the following: 
print("\nArray a:\n", a)
# a. The sum of all values. 
print("\nSum of all values:", a.sum())
# b. The sum of each column. 
print("\nColumn sums:", a.sum(axis=0))
# c. The sum of each row. 
print("\nRow sums:", a.sum(axis=1))
# d. The mean of all values. 
print("\nMean of all values:", a.mean())

# e. The minimum value. 
print("\nMinimum value:", a.min())
# f. The maximum value. 
print("\nMaximum value:", a.max())



















