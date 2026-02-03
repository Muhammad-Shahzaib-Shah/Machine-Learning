"""
np.insert(array,index ,value , axis)
axis 0 for rows
axis 1 for column 
axis None for flatten
"""
import numpy as np 
arr = np.array([1,2,3,5,6,7,8,9,10])
new_arr= np.insert(arr ,3,4 )
print(new_arr)