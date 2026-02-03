"""
np.concatenate((array1,array2),axis  )
"""
import numpy as np 
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr3 = np.concatenate((arr1,arr2))
print(arr3)

#2D array


A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([[7, 8, 9],
              [10,11,12]])

C = np.concatenate((A, B), axis=1)
print(C)
D = np.concatenate((A, B), axis=0)
print(D)
