"""""
np.split() equal
np.vsplit() 
np.hsplit() 

"""
import numpy as np
arr = [1,2,3,4,5,6,7,8,9,19]
arr1  = np.array(arr)
arr2= np.split(arr1 ,10)
print(arr2)