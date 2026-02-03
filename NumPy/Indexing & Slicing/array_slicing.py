import numpy as np 
""""" 
array[star:end] 1d array
array[which array : which position] 2d array
"""
arr = np.array([10,244,50,549])
print(arr)
print(arr[1:4])
arrs = np.array([[10,244,50,549],[1,2,3,4]])
print(arrs[1,0:3])
print(arrs[0,0:3])
print(arrs[:,0:3])
