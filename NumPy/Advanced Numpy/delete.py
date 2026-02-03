"""
np.delete(array ,index, axis = None)
"""
import numpy as np 
arr1 = np.array([1,2,3,4])
new_arr = np.delete(arr1 , 1)
print(new_arr)

#For 2D array
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr)
nw_arr = np.delete(arr ,1, axis=0 )
print(nw_arr)
nw_arr1 = np.delete(arr ,1, axis=1 )
print(nw_arr1)